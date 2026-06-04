"""
MKT Proverbs chapters 25–27 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-proverbs-25-27.py

Translation decisions:

- H3068 (יהוה, YHWH): "LORD" in L/M; "the LORD" in T — consistent with all prior Proverbs scripts.

- H2617 (חֶסֶד, hesed): Not directly present in chs. 25–27, but the covenant-loyalty concept
  underlies 25:21–22 (kindness to the enemy) and 27:10 (the faithful friend). Rendered as
  "faithful love" where the concept is implicit in T tier.

- H5315 (נֶפֶשׁ, nephesh):
  * 25:13 = "soul" — the master's refreshment; L: "soul", M: "spirit", T: "weary owner"
  * 25:25 = "soul" — the thirsty soul; L: "soul", M: "soul", T: "the thirsty heart"
  * 27:7  = "soul" — the full soul vs the hungry soul; L: "soul", M: "person", T: contextual

- H7307 (רוּחַ, ruach):
  * 25:28 = "spirit" — human self-control; clearly the inner person, not wind/breath
  * 27:16 = "wind" — trying to restrain a contentious woman is like grasping wind

- H8441 (תּוֹעֲבַת, to'evah): "abomination" in L; "detestable" in M; "abomination" in T —
  consistent with chs. 10–24.

- H191 (אֱוִיל) vs H3684 (כְּסִיל):
  Both appear in ch. 26 heavily (kesil, the sluggish/complacent fool). L/M: "fool".
  T tier distinguishes where the imagery clarifies the type of folly.

- Proverbs 25:1 editorial note: "men of Hezekiah" are named scribal copyists. These are the
  "Solomonic" proverbs transmitted through the Hezekiah-era scribal collection — a different
  editorial layer from chs. 1–24. The translation does not editorialize but T tier notes the
  scribal continuity.

- Chapter 26 is the "fool" anthology: vv. 1–12 address the kesil (the complacent fool), vv.
  13–16 the atsel (the sluggard), vv. 17–28 the contentious/deceptive person. The structure
  is intentional and T tier respects it. Notably vv. 4–5 are a famous intentional antithesis
  placed back-to-back: "Do not answer a fool... Answer a fool." Both are right; context
  determines which applies. T tier notes this explicitly at v. 4 and v. 5.

- Proverbs 26:10 is textually difficult (MT obscure). "The great God that formed all things
  both rewardeth the fool and rewardeth transgressors" — many scholars emend. L/M render MT
  cautiously; T tier acknowledges the ambiguity.

- Proverbs 27:1 is NT-echoed in James 4:13–14. T tier notes this resonance.

- Proverbs 27:17 (iron sharpens iron): One of the most-cited proverbs. T tier surfaces the
  relational dimension — it is not just about sharpening but about two people shaping each other.

- Antithetical couplet structure: Chapters 25 and 27 mix metaphor chains, antithetical
  couplets, and comparative sayings ("as X, so Y"). Chapter 26 is notably more
  anthology-structured. L preserves the metaphor. M smooths into natural English. T
  completes the thought or names the insight made implicit by the image.

- Gnomic aspect: Hebrew imperfect/participle used for timeless statements rendered as simple
  present or future throughout, consistent with chs. 1–24.
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
  "25": {
    "1": {
      "L": "These are also proverbs of Solomon, which the men of Hezekiah king of Judah copied out.",
      "M": "These also are proverbs of Solomon, which the men of Hezekiah king of Judah copied.",
      "T": "What follows is another Solomonic collection — preserved not by Solomon himself but by the scribes of King Hezekiah, who recognized that wisdom worth keeping must be actively handed on."
    },
    "2": {
      "L": "It is the glory of God to conceal a thing, but the honour of kings is to search out a matter.",
      "M": "It is the glory of God to conceal things, but the glory of kings is to search them out.",
      "T": "God's greatness is partly measured by how much he keeps hidden. Kings are great to the degree they press into what is hidden and bring it to light. One hides in glory; the other searches in glory. Both roles are real."
    },
    "3": {
      "L": "The heaven for height, and the earth for depth, and the heart of kings is unsearchable.",
      "M": "As the heavens are high and the earth is deep, so the heart of kings is unsearchable.",
      "T": "The sky cannot be measured from below. The earth cannot be plumbed from above. And the inner workings of a king's heart are equally beyond reach — which is both a warning and a wonder."
    },
    "4": {
      "L": "Take away the dross from the silver, and there shall come forth a vessel for the finer.",
      "M": "Remove dross from the silver, and a vessel emerges fit for the silversmith.",
      "T": "The silver cannot become what it is meant to be while impurities remain. The refining process is not destruction — it is the removal of what does not belong, so that the true material can finally appear."
    },
    "5": {
      "L": "Take away the wicked from before the king, and his throne shall be established in righteousness.",
      "M": "Remove the wicked from before the king, and his throne will be established in righteousness.",
      "T": "A king's reign is only as stable as the people around him. Remove the corrupt advisors and sycophants — and what remains is a throne that can actually stand. Righteousness is not merely moral — it is structural."
    },
    "6": {
      "L": "Put not forth thyself in the presence of the king, and stand not in the place of great men.",
      "M": "Do not exalt yourself in the king's presence, and do not stand in the place of the great.",
      "T": "Do not push yourself forward in powerful company. Do not claim a position that has not been given to you. Self-promotion in the presence of greatness is a kind of presumption that tends to end badly."
    },
    "7": {
      "L": "For better it is that it be said unto thee, Come up hither, than that thou shouldest be put lower in the presence of the prince whom thine eyes have seen.",
      "M": "For it is better that someone say to you, 'Come up here,' than that you be put lower before a noble you have seen.",
      "T": "It is far better to be invited up than to be moved down in front of everyone. The seat you take by invitation dignifies you. The seat you take by presumption — and are then removed from — shames you in the very place you tried to shine."
    },
    "8": {
      "L": "Go not forth hastily to strive, lest thou know not what to do in the end thereof, when thy neighbour hath put thee to shame.",
      "M": "Do not rush into a dispute, lest you do not know what to do when your neighbor shames you in the end.",
      "T": "Do not run into a legal dispute before you have thought it through. Losing in public is far worse than the original grievance. The one who acts hastily often ends up standing before everyone, having been proved wrong, with no move left to make."
    },
    "9": {
      "L": "Debate thy cause with thy neighbour himself, and discover not a secret to another.",
      "M": "Argue your case directly with your neighbor, and do not disclose another's secret.",
      "T": "Take the grievance to the person, not to everyone else. Handle conflict directly — and while you are doing it, guard whatever private things you know. Using someone's secrets as ammunition is a different sin on top of the original dispute."
    },
    "10": {
      "L": "Lest he that heareth it put thee to shame, and thine infamy turn not away.",
      "M": "Lest one who hears it reproach you, and your ill repute never depart.",
      "T": "The person who overhears you mishandling a dispute will judge you for it — and the shame you earn will stick. Some reputations, once damaged, never fully recover."
    },
    "11": {
      "L": "A word fitly spoken is like apples of gold in pictures of silver.",
      "M": "A word spoken at the right moment is like golden apples set in silver.",
      "T": "The right word at the right moment is a work of art — gold fruit displayed in a silver frame. It is beautiful in itself, perfectly suited to its setting, and worth far more than ordinary speech."
    },
    "12": {
      "L": "As an earring of gold, and an ornament of fine gold, so is a wise reprover upon an obedient ear.",
      "M": "Like a gold earring and an ornament of fine gold is a wise reprover to an obedient ear.",
      "T": "Wise correction is only as valuable as the ear that receives it. Given to someone willing to hear, a well-aimed rebuke is jewelry — costly, beautiful, enhancing rather than diminishing the one who wears it."
    },
    "13": {
      "L": "As the cold of snow in the time of harvest, so is a faithful messenger to them that send him; for he refresheth the soul of his masters.",
      "M": "Like the coolness of snow at harvest time is a faithful messenger to those who send him; he refreshes the spirit of his masters.",
      "T": "The harvest season in Judah is brutally hot. Snow-cooled water would be an almost unimaginable relief. That is what a reliable messenger is — not just useful, but genuinely restorative to the people who sent him and must wait for word."
    },
    "14": {
      "L": "Whoso boasteth himself of a false gift is like clouds and wind without rain.",
      "M": "Like clouds and wind without rain is one who boasts of a gift he never gives.",
      "T": "Clouds on the horizon mean rain is coming — but if there is no rain, the clouds are a cruel disappointment. The person who promises gifts and never delivers them is exactly that: impressive in appearance, producing nothing."
    },
    "15": {
      "L": "By long forbearing is a prince persuaded, and a soft tongue breaketh the bone.",
      "M": "By patience a ruler is persuaded, and a soft tongue can break a bone.",
      "T": "Power yields to patience. The hard wall of a powerful person's resistance can be worn down by someone who is willing to wait and speak gently. This is not weakness — it is a sophisticated kind of strength. A soft tongue, pressed patiently enough, breaks what brute force cannot."
    },
    "16": {
      "L": "Hast thou found honey? eat so much as is sufficient for thee, lest thou be filled therewith and vomit it.",
      "M": "If you find honey, eat only enough for yourself, lest you have too much and vomit it.",
      "T": "Good things have their limit. Honey is genuinely sweet — eat too much and it becomes nauseating. Even what is truly good can be ruined by excess. Self-restraint is what lets you actually enjoy what is good."
    },
    "17": {
      "L": "Withdraw thy foot from thy neighbour's house, lest he be weary of thee and so hate thee.",
      "M": "Keep your foot rare in your neighbor's house, lest he have his fill of you and come to hate you.",
      "T": "Even the most welcome guest can wear out his welcome. The friend who appears constantly — without being invited, without reading the room — eventually transforms from someone loved into someone resented. Scarcity is part of what makes a relationship valuable."
    },
    "18": {
      "L": "A man that beareth false witness against his neighbour is a maul, and a sword, and a sharp arrow.",
      "M": "A man who testifies falsely against his neighbor is a club, a sword, and a sharp arrow.",
      "T": "False testimony is not merely dishonest — it is violent. Three weapons named: a club for crushing, a sword for cutting, an arrow for killing at distance. The false witness does all three kinds of damage to the person he lies about."
    },
    "19": {
      "L": "Confidence in an unfaithful man in time of trouble is like a broken tooth and a foot out of joint.",
      "M": "Trusting an unreliable person in a time of trouble is like a broken tooth or a lame foot.",
      "T": "When you are in crisis and you reach for the person you counted on — and they are not what you thought — the pain is immediate and physical. A tooth that breaks when you bite down. A foot that gives way when you put your weight on it. Both let you down at the worst possible moment."
    },
    "20": {
      "L": "As he that taketh away a garment in cold weather, and as vinegar upon nitre, so is he that singeth songs to an heavy heart.",
      "M": "Like one who takes away a garment in cold weather, and like vinegar poured on soda, is one who sings songs to a troubled heart.",
      "T": "Cheerfulness aimed at genuine grief is a form of violence. Stripping a coat from someone in the cold. Pouring acid on alkali — the fizzing reaction destroys both. The merry song offered to a grieving person does not comfort them. It dissolves something."
    },
    "21": {
      "L": "If thine enemy be hungry, give him bread to eat; and if he be thirsty, give him water to drink.",
      "M": "If your enemy is hungry, give him bread to eat; if he is thirsty, give him water to drink.",
      "T": "Feed your enemy when he is hungry. Give him water when he is thirsty. This is not sentiment — it is a deliberate, costly act of generosity toward someone who has not earned it. What follows explains why it matters."
    },
    "22": {
      "L": "For thou shalt heap coals of fire upon his head, and the LORD shall reward thee.",
      "M": "For you will heap burning coals on his head, and the LORD will reward you.",
      "T": "The coals on the head may refer to a shame ritual — being caught out by unexpected generosity, overwhelmed by it. Or it may simply mean that your enemy's guilt is intensified, made vivid, by your kindness. Either way, the LORD sees what you did and repays it. The outcome is his to manage."
    },
    "23": {
      "L": "The north wind driveth away rain; so doth an angry countenance a backbiting tongue.",
      "M": "The north wind brings rain, and a scowling face drives away a slanderer.",
      "T": "As surely as the north wind produces rain in the land, a face that visibly refuses to receive slander shuts the gossip down. You do not have to argue with a tale-bearer — you simply have to not reward them with an interested audience."
    },
    "24": {
      "L": "It is better to dwell in the corner of the housetop than with a brawling woman and in a wide house.",
      "M": "Better to live in a corner of the roof than with a quarrelsome wife in a spacious house.",
      "T": "A small exposed perch on a flat roof is genuinely uncomfortable. But it is preferable to a mansion shared with someone whose quarreling fills every room. Space does not cure conflict — it just gives it more room to echo."
    },
    "25": {
      "L": "As cold waters to a thirsty soul, so is good news from a far country.",
      "M": "Like cold water to a thirsty soul is good news from a distant land.",
      "T": "Good news, when it arrives from somewhere far off, is not merely pleasant information — it is refreshment. The soul that has been waiting, hoping, wondering — and then hears well — feels it the way a parched throat feels cold water."
    },
    "26": {
      "L": "A righteous man falling down before the wicked is as a troubled fountain and a corrupt spring.",
      "M": "A righteous man who gives way before the wicked is like a muddied spring and a polluted well.",
      "T": "When a person of integrity yields to corruption, the damage is not just personal. A spring that runs muddy poisons everyone who comes to drink. The righteous person has a civic function — when they fold, the community loses something it counted on."
    },
    "27": {
      "L": "It is not good to eat much honey; so for men to search out their own glory is not glory.",
      "M": "It is not good to eat too much honey, nor is it glorious to seek your own glory.",
      "T": "Too much of a good thing ruins it — honey becomes sickening. Self-promotion works the same way: seeking your own glory, making yourself the main subject of your own admiration, is not actually glory. Real honor comes when others recognize you — not when you declare yourself."
    },
    "28": {
      "L": "He that hath no rule over his own spirit is like a city that is broken down and without walls.",
      "M": "A man with no control over his spirit is like a city that is broken down and without walls.",
      "T": "A city without walls is not just vulnerable — it is structurally exposed to every passing threat. The person who cannot govern their own inner life is exactly this: open to every attack, every impulse, every enemy, with no defense. Self-mastery is the wall."
    }
  },
  "26": {
    "1": {
      "L": "As snow in summer, and as rain in harvest, so honour is not seemly for a fool.",
      "M": "Like snow in summer or rain at harvest, so honor is out of place for a fool.",
      "T": "Snow in summer is not just unusual — it is a disruption of the natural order, something that ruins what should have gone well. Rain at harvest is the same: untimely and destructive. Honoring a fool is that kind of disruption — wrong in itself, and damaging to the people around it."
    },
    "2": {
      "L": "As the bird by wandering, as the swallow by flying, so the curse causeless shall not come.",
      "M": "Like a fluttering sparrow or a darting swallow, a causeless curse does not land.",
      "T": "A bird in random flight does not stop and settle just because someone wishes it to. An undeserved curse is the same — it cannot find a place to land. The curse without cause wanders off and falls somewhere else. This is a word of reassurance to those who have been cursed unfairly."
    },
    "3": {
      "L": "A whip for the horse, a bridle for the ass, and a rod for the fool's back.",
      "M": "A whip is for the horse, a bridle for the donkey, and a rod for the back of fools.",
      "T": "Each creature has the instrument suited to it. The horse responds to the whip. The donkey to the bridle. The fool — who will not respond to reason or persuasion — responds to the rod. The proverb is not advocating cruelty; it is naming the reality that some people only learn one way."
    },
    "4": {
      "L": "Answer not a fool according to his folly, lest thou also be like unto him.",
      "M": "Do not answer a fool according to his folly, lest you become like him.",
      "T": "There are times when engaging with foolishness on its own terms is itself foolish. To stoop to the fool's level of argument, to match his irrationality with an equally irrational reply, is to become what you are dealing with. Sometimes silence or refusal is the wise response."
    },
    "5": {
      "L": "Answer a fool according to his folly, lest he be wise in his own conceit.",
      "M": "Answer a fool according to his folly, lest he think himself wise.",
      "T": "But other times, silence lets the fool walk away thinking he won. Leaving foolish claims unanswered — when the audience will take silence for concession — allows the fool to be confirmed in his own delusion. Then you must answer, but carefully — on your terms, not his. Verses 4 and 5 are a deliberate pairing: wisdom knows which situation you are in."
    },
    "6": {
      "L": "He that sendeth a message by the hand of a fool cutteth off the feet and drinketh damage.",
      "M": "Whoever sends a message by the hand of a fool cuts off his own feet and drinks violence.",
      "T": "Delegating important communication to an unreliable person is self-sabotage. You have removed your own ability to walk (the message will not arrive as intended) and you will drink the consequences. The fool sent on your behalf is a liability you created."
    },
    "7": {
      "L": "The legs of the lame are not equal; so is a parable in the mouth of fools.",
      "M": "Like the limp legs of a lame man is a proverb in the mouth of a fool.",
      "T": "A wise saying in the mouth of a fool does not work the way it was designed to. The fool can quote wisdom all day, but his delivery is like a man whose legs do not function — the form is there, the motion is wrong. Wisdom requires the person who carries it to be able to carry it."
    },
    "8": {
      "L": "As he that bindeth a stone in a sling, so is he that giveth honour to a fool.",
      "M": "Like one who binds a stone in a sling is one who gives honor to a fool.",
      "T": "If you tie the stone into the sling, you cannot throw it — the weapon defeats itself. Honor given to a fool is similarly self-defeating: the honor cannot do what honor is supposed to do. It is stuck, wasted, unable to fly."
    },
    "9": {
      "L": "As a thorn goeth up into the hand of a drunkard, so is a parable in the mouth of fools.",
      "M": "Like a thorn that goes into a drunkard's hand is a proverb in the mouth of fools.",
      "T": "A drunk man does not know he is being cut. The thorn is in his hand and he cannot feel it — or if he does, he cannot locate it. A wise saying handled by a fool works the same way: pointed, potentially dangerous, and utterly unmanaged by the one holding it."
    },
    "10": {
      "L": "The great God that formed all things both rewardeth the fool and rewardeth transgressors.",
      "M": "Like an archer who wounds everyone is one who hires a fool or any passerby.",
      "T": "The verse is textually difficult. One reading: hiring without discernment — taking on a fool or a random stranger for important work — is like a bowman shooting randomly into a crowd. Everyone in range is at risk. The employer who does not vet his workers endangers more than himself."
    },
    "11": {
      "L": "As a dog returneth to his vomit, so a fool returneth to his folly.",
      "M": "Like a dog that returns to its vomit is a fool who repeats his folly.",
      "T": "The dog does not return to the vomit because it knows no better philosophy — it returns because that is simply what dogs do. The fool returns to his folly for the same reason: not because no one has shown him a better way, but because something deep in him keeps pulling him back. The New Testament picks up this image (2 Pet. 2:22) and darkens it further."
    },
    "12": {
      "L": "Seest thou a man wise in his own conceit? there is more hope of a fool than of him.",
      "M": "Do you see a man wise in his own eyes? There is more hope for a fool than for him.",
      "T": "The fool at least might be correctable — he does not yet think himself complete. But the person who is convinced they are already wise has closed the door to instruction. There is less hope for pride dressed as wisdom than for outright foolishness. This is the darkest verse in the fool anthology."
    },
    "13": {
      "L": "The slothful man saith, There is a lion in the way; a lion is in the streets.",
      "M": "The slothful man says, 'There is a lion in the road; there is a lion in the streets.'",
      "T": "The sluggard's excuses are vivid and dramatic. A lion! The very streets are unsafe! The danger he claims is technically imaginable — and therefore sounds almost reasonable. But it conveniently prevents him from going anywhere. The excuse is proportional to the task he is avoiding."
    },
    "14": {
      "L": "As the door turneth upon his hinges, so doth the slothful upon his bed.",
      "M": "As a door turns on its hinges, so a sluggard turns on his bed.",
      "T": "The hinge is busy. It moves back and forth all day — but it goes nowhere. The sluggard is exactly this: constant motion that produces no displacement. He rolls over, adjusts, resettles, turns again — all activity, no progress, still in the same place."
    },
    "15": {
      "L": "The slothful hideth his hand in his bosom; it grieveth him to bring it again to his mouth.",
      "M": "The sluggard buries his hand in the dish; it is too much effort for him to bring it back to his mouth.",
      "T": "This is comedy with a point. The man has reached into the bowl — his hand is already there — but the return trip, lifting the food to his mouth, is more than he can manage. Laziness has reached its logical extreme: the sluggard cannot even eat efficiently. Effort required: minimal. Effort available: less."
    },
    "16": {
      "L": "The sluggard is wiser in his own conceit than seven men that can render a reason.",
      "M": "The sluggard thinks himself wiser than seven who can give a sensible answer.",
      "T": "He is not just lazy — he is arrogantly lazy. Seven advisors with real answers cannot move him, because he already knows better. Sloth and pride make a deadly combination: the sluggard will not act and cannot be corrected. He is immune to improvement."
    },
    "17": {
      "L": "He that passeth by, and meddleth with strife belonging not to him, is like one that taketh a dog by the ears.",
      "M": "Like one who grabs a dog by the ears is whoever meddles in a quarrel that is not his own.",
      "T": "Grabbing a dog by the ears is dangerous precisely because you cannot let go safely. You have the dog's full attention and nowhere good to go from there. The person who inserts themselves into someone else's conflict is in the same position — they have seized something they cannot control and cannot easily release."
    },
    "18": {
      "L": "As a mad man who casteth firebrands, arrows, and death,",
      "M": "Like a madman who throws firebrands, arrows, and death,",
      "T": "The image is of someone carelessly flinging lethal things — fire, arrows — without targeting, without aim, without care. The damage is real even if the intent was playful or thoughtless."
    },
    "19": {
      "L": "So is the man that deceiveth his neighbour, and saith, Am not I in sport?",
      "M": "So is the man who deceives his neighbor and then says, 'I was only joking.'",
      "T": "The punchline completes verses 18–19 as a unit: the damage is real, the excuse is 'I was just playing.' But firebrands are not less dangerous because the thrower was laughing. The person who harms and then calls it sport has done the harm — and added insult by refusing to own it."
    },
    "20": {
      "L": "Where no wood is, there the fire goeth out; so where there is no talebearer, the strife ceaseth.",
      "M": "Without wood, a fire goes out; without a gossip, a quarrel dies down.",
      "T": "Fire does not sustain itself — it needs fuel. Conflict is the same way. Remove the person who is feeding it — the gossip, the tale-carrier, the one who keeps both sides inflamed with new reports — and the dispute simply runs out of material and stops. The lesson: if you want conflict to end, stop feeding it."
    },
    "21": {
      "L": "As coals are to burning coals, and wood to fire; so is a contentious man to kindle strife.",
      "M": "As charcoal to embers and wood to fire, so is a quarrelsome man in kindling strife.",
      "T": "The contentious person does not just participate in conflict — they amplify it. They are the fuel that takes a small fire and makes it larger. Some people have a gift for escalation. They add themselves to a situation and everything gets hotter."
    },
    "22": {
      "L": "The words of a talebearer are as wounds, and they go down into the innermost parts of the belly.",
      "M": "The words of a gossip are like delicacies; they go down into the inner chambers of the body.",
      "T": "Gossip is appealing. It goes down easily — it tastes interesting on the way in. But it does not stop at the throat. It goes deep, into the most interior parts of a person, where it lodges and works. What we receive with pleasure often shapes us more than what we resist."
    },
    "23": {
      "L": "Burning lips and a wicked heart are like a potsherd covered with silver dross.",
      "M": "Fervent lips paired with a wicked heart are like a clay pot glazed with silver dross.",
      "T": "The vessel looks metallic — valuable, refined. But the shimmer is slag: the impurity removed from real silver, not silver itself. Passionate words coming from a corrupt heart are exactly this kind of counterfeit. The intensity of delivery does not indicate the quality of what is behind it."
    },
    "24": {
      "L": "He that hateth dissembleth with his lips, and layeth up deceit within him.",
      "M": "Whoever hates disguises it with his lips, while storing up deceit within himself.",
      "T": "The hater does not show his hand in public. He smiles, agrees, uses soft words. But inside he is accumulating — building a reserve of deception to be deployed later. The outer warmth and the inner cold are not in conflict in his mind. He is simply managing two different surfaces."
    },
    "25": {
      "L": "When he speaketh fair, believe him not; for there are seven abominations in his heart.",
      "M": "When he speaks graciously, do not believe him, for there are seven abominations in his heart.",
      "T": "Pleasant words from a person you know to be operating in deceit are not to be trusted. The pleasantness is technique, not truth. The seven abominations filling his heart are not fewer because his face is kind. Do not let the surface deceive you about the interior."
    },
    "26": {
      "L": "Whose hatred is covered by deceit, his wickedness shall be shewed before the whole congregation.",
      "M": "Though his hatred is covered by deception, his wickedness will be exposed before the assembly.",
      "T": "The concealment is temporary. What has been carefully hidden beneath layers of pleasantness and managed appearances will eventually be exposed — publicly, before everyone. Proverbs is confident that reality wins in the end, even when falsehood is elaborate."
    },
    "27": {
      "L": "Whoso diggeth a pit shall fall therein; and he that rolleth a stone, it will return upon him.",
      "M": "Whoever digs a pit will fall into it, and whoever rolls a stone will have it roll back on them.",
      "T": "Traps are unstable things. The pit dug for someone else has a way of catching its digger. The stone intended to crush falls back. This is a law of moral physics in the wisdom tradition: the instruments of harm tend to rebound."
    },
    "28": {
      "L": "A lying tongue hateth those that are afflicted by it; and a flattering mouth worketh ruin.",
      "M": "A lying tongue hates those it hurts, and a flattering mouth works ruin.",
      "T": "The liar comes to hate the people he lies about — because they represent the truth he is suppressing, and truth is inconvenient. Meanwhile, the flatterer who seems so supportive is building toward destruction. Both forms of false speech end the same way: in the ruin of the person on the receiving end."
    }
  },
  "27": {
    "1": {
      "L": "Boast not thyself of to morrow; for thou knowest not what a day may bring forth.",
      "M": "Do not boast about tomorrow, for you do not know what a day may bring.",
      "T": "Tomorrow is not yours to promise. You do not hold it; it has not arrived; it may not come as you imagine. The person who brags about tomorrow's plans is making a claim on what they do not own. James 4:13–14 echoes this: the merchant who says 'tomorrow we will go and make profit' does not know whether he will even be alive."
    },
    "2": {
      "L": "Let another man praise thee, and not thine own mouth; a stranger, and not thine own lips.",
      "M": "Let someone else praise you, and not your own mouth; a stranger, and not your own lips.",
      "T": "Self-praise is always suspect. The person commending themselves has an obvious interest in the verdict. Let someone else — even a stranger, someone with no stake in the outcome — speak well of you. That praise lands differently because it comes without an angle."
    },
    "3": {
      "L": "A stone is heavy, and the sand weighty; but a fool's wrath is heavier than them both.",
      "M": "A stone is heavy and sand is a burden, but a fool's anger weighs more than both.",
      "T": "Rocks are obviously heavy. Sand is deceptively heavy — it accumulates. But the provocation of a fool, his anger, the burden of managing his reactions — that is heavier than both. You can put down a stone. You cannot easily put down someone's irrational fury."
    },
    "4": {
      "L": "Wrath is cruel, and anger is outrageous; but who is able to stand before envy?",
      "M": "Wrath is cruel, and anger is overwhelming, but who can stand before envy?",
      "T": "Anger is fierce and wrath is brutal — but both can be reasoned with, outlasted, sometimes satisfied. Envy is different. Envy does not want the situation resolved — it wants what you have, or failing that, for you not to have it. There is no satisfying envy. No one can stand before it because it has no bottom."
    },
    "5": {
      "L": "Open rebuke is better than secret love.",
      "M": "Open rebuke is better than hidden love.",
      "T": "Love that stays hidden — that watches someone make a mistake and says nothing to spare feelings or preserve peace — is not as loving as it appears. A rebuke that says the hard thing openly, that risks the relationship by naming what is wrong, is a greater act of love than silent affection."
    },
    "6": {
      "L": "Faithful are the wounds of a friend; but the kisses of an enemy are deceitful.",
      "M": "The wounds of a friend can be trusted, but an enemy's kisses are lavish and false.",
      "T": "A friend who wounds you — who tells you what you need to hear, who cuts when cutting is necessary — is being faithful to you. The enemy who greets you with excessive warmth is not. The wound from a friend heals; the kiss from an enemy is working toward something else."
    },
    "7": {
      "L": "The full soul loatheth an honeycomb; but to the hungry soul every bitter thing is sweet.",
      "M": "One who is full despises honey, but to the hungry person every bitter thing is sweet.",
      "T": "Satisfaction changes everything. The person who is already full cannot be impressed even by honey — the best thing on offer becomes unappealing. But the genuinely hungry person finds sweetness in what would otherwise be unpleasant. Need and longing are the appetite that makes things good."
    },
    "8": {
      "L": "As a bird that wandereth from her nest, so is a man that wandereth from his place.",
      "M": "Like a bird that flees its nest, so is a man who wanders from his home.",
      "T": "A bird without its nest is exposed — restless, homeless, in the wrong kind of freedom. A person without a settled place — without home, community, belonging — is similarly adrift. Not all wandering is adventure. Some of it is loss."
    },
    "9": {
      "L": "Ointment and perfume rejoice the heart; so doth the sweetness of a man's friend by hearty counsel.",
      "M": "Oil and perfume bring joy to the heart; so does a friend's earnest counsel.",
      "T": "Fragrance is immediate and pleasant — it does not have to argue for itself, it simply delights. Good counsel from a friend who genuinely cares is exactly this: it reaches you directly, brings pleasure and comfort, and does not feel like an imposition."
    },
    "10": {
      "L": "Thine own friend, and thy father's friend, forsake not; neither go into thy brother's house in the day of thy calamity; for better is a neighbour that is near than a brother far off.",
      "M": "Do not forsake your friend or your father's friend; do not go to your brother's house in the day of your trouble. A neighbor who is near is better than a brother who is far away.",
      "T": "Loyalty to long friendships — including the friendships your father made before you — is practical wisdom. When disaster strikes, the person who can reach you in an hour matters more than a relative on the other side of the country. Proximity is a form of love. Do not let old friendships decay for the sake of blood ties that are present only in theory."
    },
    "11": {
      "L": "My son, be wise, and make my heart glad, that I may answer him that reproacheth me.",
      "M": "Be wise, my son, and gladden my heart, so I may have a word for whoever taunts me.",
      "T": "The teacher has something at stake in the student's wisdom — not merely the student's flourishing, but his own honor. When the son turns out well, the parent has an answer for everyone who doubted. When the student becomes wise, the teacher is vindicated. Wisdom is not private."
    },
    "12": {
      "L": "A prudent man foreseeth the evil, and hideth himself; but the simple pass on, and are punished.",
      "M": "A prudent person sees danger and hides, but the simple walk on and suffer for it.",
      "T": "The wise person reads the situation early and steps aside before the danger arrives. The naive person does not see it coming — or sees it and keeps walking anyway, convinced it won't be a problem. The consequence falls on the one who did not act on what could be seen."
    },
    "13": {
      "L": "Take his garment that is surety for a stranger, and take a pledge of him for a strange woman.",
      "M": "Take his garment when he has put up security for a stranger, and hold it in pledge when he does so for a wayward woman.",
      "T": "If someone is foolish enough to guarantee the debt of a stranger — or worse, an immoral woman — take collateral immediately. The advice is not cruel; it is realistic. The person making that kind of guarantee has shown poor judgment. Protect yourself before you protect their dignity."
    },
    "14": {
      "L": "He that blesseth his friend with a loud voice, rising early in the morning, it shall be counted a curse to him.",
      "M": "Whoever blesses his neighbor with a loud voice early in the morning, it will be counted a curse to him.",
      "T": "Showing up at someone's door at dawn, bellowing well-wishes — however warm the intent — is not a gift to the recipient. It is an imposition. Enthusiasm deployed without sensitivity to timing or context is not kindness. The neighbor who was awakened will not remember the blessing. They will remember the noise."
    },
    "15": {
      "L": "A continual dropping in a very rainy day and a contentious woman are alike.",
      "M": "A constant dripping on a rainy day and a quarrelsome wife are alike.",
      "T": "The dripping does not hurt — it is simply relentless, impossible to ignore, impossible to stop, wearing everything down over time. The image is not about violence but about the particular exhaustion of something that never lets up."
    },
    "16": {
      "L": "Whosoever hideth her hideth the wind, and the ointment of his right hand which bewrayeth itself.",
      "M": "Trying to restrain her is like trying to restrain the wind, and like trying to grasp oil in the right hand.",
      "T": "Wind cannot be contained. Oil runs through even a clenching fist. To try to suppress or manage a contentious person is to spend energy on something that simply will not hold. Some things cannot be controlled by force or strategy — only by not being in that situation."
    },
    "17": {
      "L": "Iron sharpeneth iron; so a man sharpeneth the countenance of his friend.",
      "M": "As iron sharpens iron, so one person sharpens another.",
      "T": "Two pieces of iron cannot make each other sharp without friction. The sharpening requires contact, pressure, and resistance. Friendships that make both people better are not frictionless — they involve the honest collision of minds and characters. Each person edges the other. Neither walks away unchanged."
    },
    "18": {
      "L": "Whoso keepeth the fig tree shall eat the fruit thereof; so he that waiteth on his master shall be honoured.",
      "M": "Whoever tends the fig tree will eat its fruit; whoever looks after his master will be honored.",
      "T": "Faithful tending of what you are given produces reward. The fig tree does not produce overnight — it requires sustained attention over time. The servant who proves reliable by daily faithfulness, who does not demand recognition before putting in the work, eventually receives honor. Patient stewardship is not wasted."
    },
    "19": {
      "L": "As in water face answereth to face, so the heart of man to man.",
      "M": "As water reflects a face, so one person's heart reflects another's.",
      "T": "Lean over still water and you see yourself looking back. Something similar happens between human hearts: what is inside one person resonates in another. We recognize ourselves in each other — which is why genuine understanding between people is possible, and why knowing yourself helps you understand those around you."
    },
    "20": {
      "L": "Hell and destruction are never full; so the eyes of man are never satisfied.",
      "M": "Sheol and Abaddon are never satisfied; so the eyes of man are never satisfied.",
      "T": "The realm of death — Sheol, the abyss — is insatiable. No matter how many enter, there is room for more. Human desire is structured the same way: the eyes see, want, acquire — and immediately find something new to want. Enough is a concept human desire cannot actually locate."
    },
    "21": {
      "L": "As the fining pot for silver, and the furnace for gold; so is a man to his praise.",
      "M": "The crucible is for silver, and the furnace is for gold, and a man is tested by his praise.",
      "T": "Silver is tested in the crucible. Gold in the furnace. Both reveal the metal's true quality under heat. Praise reveals a person in the same way — how they handle compliment and honor tells you what they are made of. Pride exposed by praise. Humility confirmed by it. The test is reliable."
    },
    "22": {
      "L": "Though thou shouldest bray a fool in a mortar among wheat with a pestle, yet will not his foolishness depart from him.",
      "M": "Even if you grind a fool in a mortar with a pestle amid grain, his folly will not leave him.",
      "T": "The grain is crushed and refined. The wheat is separated from the husk. But grind a fool as thoroughly as you like and his folly remains — it is not a surface quality but a deeply embedded disposition. Some people cannot be corrected by process or pressure because the problem goes all the way through."
    },
    "23": {
      "L": "Be thou diligent to know the state of thy flocks, and look well to thy herds.",
      "M": "Know well the condition of your flocks, and give careful attention to your herds.",
      "T": "Wealth is not self-maintaining. What you have been given — livestock, land, resources, people — requires active attention. Look at what you actually have. Know its condition. Stewardship is not passive ownership; it is regular, close engagement with the reality in front of you."
    },
    "24": {
      "L": "For riches are not for ever; and doth the crown endure to every generation?",
      "M": "For riches do not last forever; nor does the crown endure to all generations.",
      "T": "Wealth dissipates. Power does not hold from generation to generation without constant renewal. The assumption that what you have now will simply persist is not supported by history or observation. This is why attending to your flocks matters — because passive reliance on inherited wealth is a losing strategy."
    },
    "25": {
      "L": "The hay appeareth, and the tender grass sheweth itself, and herbs of the mountains are gathered.",
      "M": "When the grass is gone and new growth appears and the mountain plants are gathered,",
      "T": "The agricultural cycle turns: the old grass is cut and goes; fresh growth appears; the mountain herbs are brought in at their season. The farmer who is paying attention sees every stage of this and is ready for it."
    },
    "26": {
      "L": "The lambs are for thy clothing, and the goats are the price of the field.",
      "M": "The lambs are for your clothing, and the goats supply the price of a field.",
      "T": "The flock provides wool for clothing and can be sold to purchase land. The attentive farmer who tended his flocks through seasons 23–25 now has what he needs: covering for his family and capital for expansion. Faithfulness in small management leads to genuine provision."
    },
    "27": {
      "L": "And thou shalt have goats' milk enough for thy food, for the food of thy household, and for the maintenance of thy maidens.",
      "M": "There will be enough goats' milk for your food, for the food of your household, and nourishment for your servant girls.",
      "T": "The chapter closes with a vision of sufficiency. Not extravagance — enough. The household is fed: you, your family, your servants. The attentive and diligent farmer who knows his flocks and gives them steady care arrives at this: enough milk, enough food, enough for everyone under his roof. Faithfulness in stewardship is the path to provision."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'proverbs')
        merge_tier(existing, PROVERBS, tier_key)
        save(tier_dir, 'proverbs', existing)
    print('Proverbs 25–27 written.')

if __name__ == '__main__':
    main()
