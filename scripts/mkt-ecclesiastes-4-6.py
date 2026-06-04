"""
MKT Ecclesiastes chapters 4–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ecclesiastes-4-6.py

Translation decisions:

- H1892 (הֶבֶל hebel): This is Qohelet's central term, used as a refrain throughout.
  Literally "breath / vapor / mist" — something weightless and quickly gone. KJV "vanity"
  conflates two ideas (transience + emptiness); "meaningless" (NIV) over-interprets.
  Decision: L="vapor" (literal); M="vapor" (preserves the image; readers understand the idiom);
  T=contextually varied — "emptiness," "breath," "nothing," "smoke" depending on the
  rhetorical point. The set phrase הֲבֵל הֲבָלִים (hebel hevalim) = "vapor of vapors" in L/M;
  "pure vapor — everything is vapor" in T.

- H7469 (רְעוּת / re'ut) + H7307 (רוּחַ ruach) — the paired phrase KJV "vexation of spirit":
  H7469 root is disputed — either "herding/shepherding" (→ impossible task of herding wind)
  or "desire/longing" (→ yearning for what cannot be had). Modern consensus favors "chasing."
  H7307 in this phrase = "wind" (the physical phenomenon), not "spirit."
  Decision: L="herding of wind"; M="chasing the wind"; T="grasping at the wind."
  Note: 4:16 uses H7475 (רַעְיוֹן rayon) instead of H7469 — same semantic range, same rendering.

- H7307 (רוּחַ ruach) standalone (not in the compound phrase):
  5:16: "labored for the wind" — literal wind; rendered "wind" across all tiers.
  4:4: appears in the compound phrase (see above).

- H5315 (נֶפֶשׁ nephesh):
  6:2: "his soul" = desire/appetite — M/T render "appetite" or "desires."
  6:3: "his soul be not satisfied" = inner satisfaction — M/T render "satisfaction" / "contentment."
  6:7: "appetite is not satisfied" — all tiers render "appetite" here (context explicit).
  6:9: "wandering of the soul" = restless desire — M/T render "appetite" / "restless desire."
  L always "soul"; M/T contextual.

- H430 (אֱלֹהִים Elohim): "God" consistently across all tiers. H3068 (יהוה) does not appear
  in these chapters. Ecclesiastes uses only Elohim, not the covenant name.

- H5999 (עָמָל 'amal): "toil" in L; "toil" or "labor" in M/T — the exhausting burden of work.
  Distinct from H6045 (עִנְיָן inyan = business/occupation/concern, rendered "business" or
  "concern" in M/T) and H4639 (מַעֲשֶׂה ma'aseh = work/deed, rendered "work" or "deed").

- H2470 (חָלָה chalah): "grievous" / "sore" in adjectival/adverbial use.
  5:13, 5:16: "a sore evil" / "grievous evil" — M/T render "painful irony" or "painful evil."
  6:2: same — M/T render "grievous affliction."

- H3206 (יֶלֶד yeled): "child" or "youth" depending on context. 4:13-15: the rival "youth"
  challenging the old king — rendered "young man" in M/T for clarity.

- H5087/H5088 (נָדַר / נֶדֶר nadar/neder): "vow" verb and noun. Ch. 5:4-5 — maintained
  as "vow" / "vow" across all tiers; no special rendering needed.

- H4397 (מַלְאָךְ malak) in 5:6: here the temple official/priest who received and registered
  vows, not a supernatural angel. M/T render "priest" for clarity.

- Hebrew imperfect in Qohelet's observations: timeless present tense in English ("he eats,"
  "they go") — the philosopher's register of perennial observation.

- Aspect note: Qohelet's narrative uses waw-consecutive past ("I returned," "I saw") to report
  observations; rendered as simple past in all tiers.

- OT echo: 5:2 echoes the vastness of God established in creation texts (Isa 55:8-9 later
  makes the same point). 6:12 echoes Ps 102:11 / 144:4 (human life as shadow). Noted in T.

- Poetry/prose note: Ecclesiastes 4–6 is elevated prose with some verse-like couplets
  (4:5-6, 4:9-12, 5:10-12). T preserves the rhythmic pairings in those sections.
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
  "4": {
    "1": {
      "L": "So I returned and considered all the oppressions that are done under the sun; and behold, the tears of the oppressed, and they had no comforter; and on the side of their oppressors there was power, but they had no comforter.",
      "M": "I turned and considered all the acts of oppression done under the sun. I saw the tears of the oppressed — they had no one to comfort them. Power was on the side of their oppressors, and there was no one to comfort the oppressed.",
      "T": "I looked again at all the acts of oppression carried out in this world. I saw the tears of those who had been crushed — no one coming to comfort them. The oppressors had all the power, and still no comforter came."
    },
    "2": {
      "L": "So I declared the dead who are already dead more fortunate than the living who are still alive.",
      "M": "So I counted the dead who have already died more fortunate than the living who are still alive.",
      "T": "And so I concluded: the dead are more fortunate than the living — at least the dead are done with it."
    },
    "3": {
      "L": "But better than both is he who has not yet existed, who has not seen the evil work that is done under the sun.",
      "M": "But better off than either is the one not yet born, who has not seen the evil that is done under the sun.",
      "T": "Better still is the one who has never been born at all — who has never had to witness the evil that goes on in this world."
    },
    "4": {
      "L": "Then I saw that all toil and every skillful work comes from a man's envy of his neighbor. This also is vapor and a herding of wind.",
      "M": "Then I saw that all toil and every skilled achievement springs from a person's envy of his neighbor. This too is vapor — a chasing after wind.",
      "T": "Then I saw the truth beneath it all: every act of toil and skilled work is driven by envy of the neighbor. Even this is vapor — nothing but grasping at the wind."
    },
    "5": {
      "L": "The fool folds his hands and eats his own flesh.",
      "M": "The fool folds his hands and devours himself.",
      "T": "The lazy fool crosses his arms and gnaws himself down to nothing."
    },
    "6": {
      "L": "Better is one handful with quietness than two handfuls with toil and a herding of wind.",
      "M": "Better is one hand full of quietness than two hands full of toil and chasing the wind.",
      "T": "One handful of peace is worth more than two fistfuls of exhausting labor — all that striving after the wind."
    },
    "7": {
      "L": "Then I returned, and I saw vapor under the sun.",
      "M": "Again I turned and observed something futile under the sun.",
      "T": "I looked again and saw another example of emptiness in this world."
    },
    "8": {
      "L": "There is one who is alone, with no second one — he has neither son nor brother — yet there is no end to all his toil, and his eye is never satisfied with riches. 'For whom do I toil and deprive my soul of good?' This also is vapor and an unhappy travail.",
      "M": "Here is a solitary man with no companion — neither son nor brother — yet his labor has no end and his eyes are never satisfied with wealth. He never asks, 'For whom am I working, and why am I denying myself any pleasure?' This too is vapor — a miserable way to live.",
      "T": "Consider the man who labors alone, with no one beside him — no son, no brother — yet he works without end, and wealth never satisfies him. He never once asks: 'Who am I doing all this for? Why am I robbing myself of every enjoyment?' This too is emptiness — a wretched existence."
    },
    "9": {
      "L": "Two are better than one, because they have a good reward for their toil.",
      "M": "Two are better than one, because they get a better return for their labor.",
      "T": "Two are better than one — together they accomplish more than either could alone."
    },
    "10": {
      "L": "For if they fall, one will lift up his fellow. But woe to him who is alone when he falls, for there is not another to lift him up.",
      "M": "For if one falls, the other will lift his companion up. But terrible is the fate of the one who is alone when he falls — there is no one to help him up.",
      "T": "If one falls, the other can pull him to his feet. But the person alone when he falls — God help him, because no one else will."
    },
    "11": {
      "L": "Again, if two lie together they keep warm; but how can one keep warm alone?",
      "M": "Also, if two lie together they keep each other warm. But how can one person keep warm alone?",
      "T": "Two people lying together stay warm. But what warmth does anyone get sleeping alone?"
    },
    "12": {
      "L": "And though a man might prevail against one who is alone, two will withstand him. And a threefold cord is not quickly broken.",
      "M": "Though one person may be overpowered, two can stand their ground. A cord of three strands is not quickly broken.",
      "T": "One person can be overwhelmed, but two can hold their ground. And a rope of three strands — that takes real force to break."
    },
    "13": {
      "L": "Better is a poor and wise youth than an old and foolish king who will no longer be warned.",
      "M": "Better a poor but wise young man than an old and foolish king who no longer heeds counsel.",
      "T": "A poor young man with wisdom is worth more than an aging king who is too proud to listen to advice."
    },
    "14": {
      "L": "For from prison he came out to reign, though in that kingdom he was born poor.",
      "M": "The young man rose from prison to the throne, though he had been born poor in that very kingdom.",
      "T": "This young man had risen from a prison cell to kingship — he had started out as one of the poor of that land."
    },
    "15": {
      "L": "I considered all the living who walk under the sun, with the second youth who was to stand in the king's place.",
      "M": "I saw all the living — those who walk under the sun — rally to the side of the second young man who would succeed him.",
      "T": "I watched how everyone alive in this world threw their support behind the second young man, the one positioned to replace the old king."
    },
    "16": {
      "L": "There was no end to all the people, to all before whom he stood; yet those who come after will not rejoice in him. Surely this also is vapor and a herding of wind.",
      "M": "There was no end to all the people who followed him; yet those who come later will take no delight in him either. This too is vapor — a chasing after wind.",
      "T": "The crowds were endless — and yet the generation that follows will not think highly of him either. Even this is empty: nothing but grasping at the wind."
    }
  },
  "5": {
    "1": {
      "L": "Guard your steps when you go to the house of God. To draw near to hear is better than to offer the sacrifice of fools, for they do not know that they are doing evil.",
      "M": "Guard your steps when you go to the house of God. To draw near to listen is better than to offer the sacrifice of fools, who do not realize they are doing wrong.",
      "T": "Watch how you approach God's house. Better to go there ready to listen than to bring an offering the way fools do — they don't even know they are doing wrong."
    },
    "2": {
      "L": "Do not be rash with your mouth, and do not let your heart be hasty to utter a word before God, for God is in heaven and you are on earth. Therefore let your words be few.",
      "M": "Do not be hasty with your words or quick in your heart to speak before God, for God is in heaven and you are on earth. So let your words be few.",
      "T": "Don't rush to speak, and don't let your heart race ahead of your tongue when you address God. He is in heaven; you are on earth. Say less rather than more."
    },
    "3": {
      "L": "For a dream comes through much business, and a fool's voice through many words.",
      "M": "For a dream comes from too many concerns, and a fool's chatter from too many words.",
      "T": "Just as dreams come when you are exhausted from overwork, a fool's babbling comes from too much talking."
    },
    "4": {
      "L": "When you vow a vow to God, do not delay to pay it, for he has no pleasure in fools. Pay what you vow.",
      "M": "When you make a vow to God, do not delay in fulfilling it, for he takes no pleasure in fools. Pay what you have vowed.",
      "T": "When you make a promise to God, honor it without delay. He has no patience with fools — keep your word."
    },
    "5": {
      "L": "Better that you should not vow than that you should vow and not pay.",
      "M": "It is better not to vow than to vow and not fulfill it.",
      "T": "Better to make no promise at all than to make one you won't keep."
    },
    "6": {
      "L": "Do not let your mouth bring your flesh into sin, and do not say before the messenger that it was an error. Why should God be angry at your voice and destroy the work of your hands?",
      "M": "Do not let your mouth lead you into sin, and do not tell the priest it was a mistake. Why should God be angry at your words and destroy everything you have built?",
      "T": "Don't let careless talk lead you into sin, and when the priest comes to collect on your vow, don't shrug it off as an oversight. Why give God reason to be angry with you and undo everything you have worked for?"
    },
    "7": {
      "L": "For in the multitude of dreams and many words there are also many vapors; but fear God.",
      "M": "When there are many dreams, there are futile words aplenty. Fear God.",
      "T": "Dreams multiply, words multiply, and with them comes much that is worthless. The one thing that matters above all else: fear God."
    },
    "8": {
      "L": "If you see the oppression of the poor and the violent perverting of justice and righteousness in a province, do not be amazed at the matter, for the high one is watched over by one higher, and there are still higher ones above them.",
      "M": "If you see the poor being oppressed and justice and equity denied in a district, do not be surprised — for one official is covered by a higher one, and above them both are officials higher still.",
      "T": "When you see the poor being exploited and justice twisted in some province, don't be shocked. Corruption thrives in hierarchy: every official is protected by someone above him, and above that person, yet another."
    },
    "9": {
      "L": "Moreover, the profit of the land is for all; a king himself is served by the field.",
      "M": "Yet in all this, there is an advantage that belongs to everyone: even a king is served by the cultivated land.",
      "T": "And yet there is something that ultimately benefits all alike: even the king depends on the harvest of his fields."
    },
    "10": {
      "L": "He who loves silver will not be satisfied with silver, nor he who loves abundance with its increase. This also is vapor.",
      "M": "Whoever loves money is never satisfied with money; whoever loves wealth is never satisfied with income. This too is vapor.",
      "T": "Love money and money will never be enough. Love abundance and abundance will never satisfy. Another emptiness."
    },
    "11": {
      "L": "When goods increase, those who eat them increase; and what gain is there to their owners except the seeing of them with their eyes?",
      "M": "As goods increase, so do those who consume them. What benefit remains for the owner beyond seeing them with his own eyes?",
      "T": "More wealth brings more people to eat it. What does the owner actually gain? Nothing but the sight of it."
    },
    "12": {
      "L": "Sweet is the sleep of the laboring man, whether he eats little or much; but the abundance of the rich will not let him sleep.",
      "M": "The sleep of the laborer is sweet, whether he eats little or much. But the excess of wealth allows the rich man no sleep.",
      "T": "A laborer sleeps soundly, whether he ate much or little. But the rich man's abundance keeps him awake at night."
    },
    "13": {
      "L": "There is a grievous evil that I have seen under the sun: riches kept by their owner to his hurt.",
      "M": "Here is a grievous evil I have observed under the sun: wealth hoarded by its owner at his own expense.",
      "T": "I have seen a painful irony in this world: riches carefully guarded by their owner — and those same riches destroying him."
    },
    "14": {
      "L": "And those riches were lost in an evil venture; and he had fathered a son, and there was nothing in his hand.",
      "M": "Those riches were lost in a bad venture; and he had fathered a son, but had nothing to leave him.",
      "T": "One bad venture wiped out everything. He had a son to provide for, and nothing left to give him."
    },
    "15": {
      "L": "As he came from his mother's womb, naked he shall return to go as he came, and he shall take nothing for his labor that he may carry away in his hand.",
      "M": "As he came from his mother's womb, so he will leave — naked. He can take nothing for his labor that he could carry in his hand.",
      "T": "He came into the world with nothing, and he will leave the same way — naked. Everything he worked for? He cannot take a single thing with him."
    },
    "16": {
      "L": "This also is a grievous evil: in all points as he came, so shall he go. And what does he gain who toils for the wind?",
      "M": "This too is a grievous evil: just as he came, so he goes. What does anyone gain who labors for the wind?",
      "T": "Here is the painful truth: he entered empty-handed and leaves the same way. What has he gained from all his striving — was it anything more than working for the wind?"
    },
    "17": {
      "L": "Also, all his days he eats in darkness, with much vexation and sickness and anger.",
      "M": "Throughout his days he eats in darkness, burdened with much sickness, vexation, and anger.",
      "T": "He spends his days eating in gloom — sick, bitter, enraged."
    },
    "18": {
      "L": "Behold, what I have seen to be good and fitting is to eat and drink and find enjoyment in all the toil with which one toils under the sun the few days of his life that God has given him, for this is his lot.",
      "M": "This is what I have found to be good and fitting: to eat and drink and find enjoyment in all one's labor under the sun during the few days of life God has given — for that is one's portion.",
      "T": "This is what I have concluded to be genuinely good: eat, drink, and take real pleasure in your work — the brief span of life God has given you. That is what you have been allotted; embrace it."
    },
    "19": {
      "L": "Everyone also to whom God has given wealth and possessions and power to enjoy them, and to accept his lot and rejoice in his toil — this is the gift of God.",
      "M": "Furthermore, when God gives someone wealth and possessions and enables them to enjoy these things — to accept their portion and find joy in their labor — that is a gift of God.",
      "T": "When God gives a person wealth and the actual capacity to enjoy it — to embrace what they have and find joy in their work — that capacity itself is God's gift."
    },
    "20": {
      "L": "For he will not much remember the days of his life, because God keeps him occupied with joy in his heart.",
      "M": "Such a person will not brood much over the years of their life, because God keeps their heart occupied with joy.",
      "T": "A person like this does not dwell on how short life is — God has filled their heart with so much joy there is no room left for that kind of grief."
    }
  },
  "6": {
    "1": {
      "L": "There is an evil that I have seen under the sun, and it lies heavy upon mankind.",
      "M": "There is an evil I have observed under the sun, and it is widespread among human beings.",
      "T": "I have seen a particular evil in this world — one that lies heavily on the human race."
    },
    "2": {
      "L": "A man to whom God gives wealth, riches, and honor, so that he lacks nothing of all he desires, yet God does not give him power to enjoy them, but a stranger enjoys them. This is vapor and a grievous affliction.",
      "M": "Here is a man to whom God gives wealth, riches, and honor, so that nothing he desires is lacking — yet God does not give him the capacity to enjoy any of it, and a stranger devours it all instead. This is vapor — a grievous affliction.",
      "T": "God gives a man wealth, honor, and everything he could ever want — and then withholds the capacity to enjoy a single bit of it. A stranger ends up consuming it all. This is pure emptiness — one of life's cruelest ironies."
    },
    "3": {
      "L": "If a man fathers a hundred children and lives many years, so that the days of his years are many, but his soul is not satisfied with good, and he also has no burial, I say that a stillborn child is better off than he.",
      "M": "A man may father a hundred children and live a long life with many years, yet if he cannot fill himself with good things and in the end receives no burial, I say a stillborn child is better off than he.",
      "T": "Even if a man fathers a hundred children and lives to a great old age — if he never finds real contentment and doesn't even receive a decent burial, I say a stillborn child is better off than he ever was."
    },
    "4": {
      "L": "For it comes in vapor and goes in darkness, and in darkness its name is covered.",
      "M": "For the stillborn comes in vapor and departs in darkness, and its name is buried in darkness.",
      "T": "Such a child arrives as a breath and vanishes into darkness, its very name swallowed by the dark."
    },
    "5": {
      "L": "Moreover it has not seen the sun nor known anything; yet it has more rest than the other.",
      "M": "It has never seen the sun or known anything — yet it finds more rest than the other.",
      "T": "It has never seen daylight, never known a thing — and still it has found more peace than this man ever did."
    },
    "6": {
      "L": "Even if he were to live a thousand years twice over, yet sees no good — do not all go to one place?",
      "M": "Even if that man were to live two thousand years and yet find nothing good — does not everyone go to the same place in the end?",
      "T": "Even if he lived two thousand years — if he found no real good in life, what does it matter? We all end up in the same place."
    },
    "7": {
      "L": "All the toil of man is for his mouth, yet his appetite is not satisfied.",
      "M": "All of a person's labor goes toward filling the mouth, yet the appetite is never satisfied.",
      "T": "Everything a person works for goes to feed the mouth — and still the appetite is never full."
    },
    "8": {
      "L": "For what advantage does the wise man have over the fool? And what does the poor man have who knows how to conduct himself before the living?",
      "M": "What real advantage does the wise person have over the fool? And what does even the poor person gain from knowing how to navigate life?",
      "T": "In the end, what does the wise person have that the fool does not? And what does even a street-smart poor man actually gain from it all?"
    },
    "9": {
      "L": "Better is the seeing of the eyes than the wandering of the soul. This also is vapor and a herding of wind.",
      "M": "Better what the eyes can actually see than the restless wandering of desire. This too is vapor — a chasing after wind.",
      "T": "Better to enjoy what is right in front of you than to keep chasing what you do not have. Even that satisfaction is fleeting — another gust of wind."
    },
    "10": {
      "L": "Whatever has come into being has already been named, and it is known what man is; he cannot contend with one mightier than he.",
      "M": "Whatever exists has already been named; it is known what a human being is — and no one can contend with one far more powerful.",
      "T": "Everything that exists has already been given its name; human nature is no mystery. And no one can win an argument with the One who holds all the power."
    },
    "11": {
      "L": "The more words there are, the more vapor there is; what is the advantage for man?",
      "M": "The more words there are, the more futility — what benefit is there for a person?",
      "T": "More words mean more emptiness. What does any of it actually accomplish for us?"
    },
    "12": {
      "L": "For who knows what is good for man in life, all the days of his vain life which he passes like a shadow? For who can tell man what will be after him under the sun?",
      "M": "For who knows what is truly good for a person in life — during all those fleeting days spent like a shadow? And who can tell anyone what will happen under the sun after they are gone?",
      "T": "For who truly knows what is good for us in this brief life we pass through like a shadow — as the psalms say, our days are a shadow that passes? And who can tell us what the world will look like after we are gone?"
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ecclesiastes')
        merge_tier(existing, ECCLESIASTES, tier_key)
        save(tier_dir, 'ecclesiastes', existing)
    print('Ecclesiastes 4–6 written.')

if __name__ == '__main__':
    main()
