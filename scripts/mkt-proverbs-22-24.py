"""
MKT Proverbs chapters 22–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-proverbs-22-24.py

Translation decisions:

- H3068 (יהוה, YHWH): "LORD" in L/M; "the LORD" in T — consistent with chs. 1–21.

- H2617 (חֶסֶד, hesed): Not prominent in these chapters. Where present, rendered contextually
  as "steadfast love" or "faithful love" in M/T; "mercy" in L where that reading fits.

- H5315 (נֶפֶשׁ, nephesh):
  * 22:25 = "soul" (snare to thy soul) — embodied selfhood endangered; L: "soul", M: "yourself"
  * 23:2 = implied control over the throat/appetite; rendered as "appetite" in T
  * 24:12 = "soul" (he that keepeth thy soul) — God guards your life; L: "soul", M: "life"

- H8441 (תּוֹעֲבַת, to'evah): "abomination" in L, "detestable" in M/L-adjacent; "abomination" in T —
  consistent with chs. 10–21.

- H5869 רָע (evil eye, 23:6): rendered "stingy" in M/T — the Hebrew idiom "evil eye" (ayin ra')
  denotes miserliness/grudging attitude; not superstition. L preserves "evil eye", M/T clarify.

- H1397 (גֶּבֶר, gever): "man" throughout L/M; T varies for readability.

- Proverbs 22:6 — חֲנֹךְ + עַל־פִּי דַרְכּוֹ: "train up a child in the way he should go."
  The phrase could be read as "according to his way" (following the child's bent) or as the
  traditional positive directive. The traditional directive reading is followed in all three tiers,
  consistent with the broader Proverbs emphasis on active formation.

- Proverbs 22:17–21: Opens the "Words of the Wise" section (22:17–24:22). The shift to second-person
  direct address is preserved in all tiers. The reference to "thirty sayings" (22:20) is explicit in M/T.

- Proverbs 23:7 ("as he thinketh in his heart, so is he"): The Hebrew is disputed — some read
  "as one who calculates" (miserly, calculating the cost of every bite). The miser/calculator
  reading is adopted in M/T as it fits the immediate context (eating with a stingy man).

- Proverbs 23:13–14: The rod of discipline — carried forward from ch. 13 and 22 treatment.
  Consistent with the Proverbs view that physical correction is an act of rescue, not cruelty.

- Proverbs 23:29–35: Extended wine poem — the most sustained piece of rhetoric in Proverbs chs. 19–24.
  L preserves the rhetorical questions and imagery. T amplifies the arc: enticement → deception →
  harm → addiction. The final verse (35) is the pivot: the drinker wakes up asking not "what
  happened to me?" but "when can I drink again?" — the portrait of compulsion.

- Proverbs 24:3–4: Wisdom as building material. "House" is both literal household and life structure.
  T invites that double reading without collapsing either.

- Proverbs 24:11–12: The call to rescue those being led to death. The "we did not know" excuse
  is directly addressed; the LORD who "weighs hearts" (H8505) penetrates all rationalizations.
  T tier makes this accountability explicit.

- Proverbs 24:16: The righteous fall "seven times" — seven is completeness, not a literal count.
  T tier notes that falling is not the point; rising is. The contrast with the wicked (who stay down)
  is the heart of the verse.

- Proverbs 24:17–18: Warning against gloating over an enemy's fall — the LORD may redirect his
  wrath from the enemy toward the gloater. T tier makes this dynamic explicit without moralizing.

- Proverbs 24:30–34: Closing poem on the sluggard's field. The teacher recounts an observation
  (first-person "I went by"). T tier honors the empirical, observed-wisdom character of this passage.

- Gnomic aspect: Hebrew participles and imperfects used for timeless statements throughout rendered
  as simple present or future in English, consistent with chs. 1–21.

- Antithetical couplet structure: preserved faithfully in all three tiers. Synonymous parallelism
  in the "Words of the Wise" sections given natural flow in M/T.
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
  "22": {
    "1": {
      "L": "A good name is rather to be chosen than great riches, and loving favour rather than silver and gold.",
      "M": "A good name is to be chosen over great riches, and favor is better than silver and gold.",
      "T": "Your reputation is worth more than a fortune. Being well-regarded — trusted, respected, genuinely liked — outlasts silver and gold and is far harder to replace once lost."
    },
    "2": {
      "L": "The rich and poor meet together; the LORD is the maker of them both.",
      "M": "The rich and the poor have this in common: the LORD made them both.",
      "T": "Whatever separates the rich from the poor — and much does — this is not one of the differences: the LORD made both. Every gap between them exists within a shared origin."
    },
    "3": {
      "L": "A prudent man foreseeth the evil and hideth himself, but the simple pass on and are punished.",
      "M": "A prudent person sees danger and takes cover, but the naive keep going and suffer for it.",
      "T": "The shrewd person reads what is coming and steps out of the way before it arrives. The naive walk straight into it, still expecting things to be fine. The consequences are entirely predictable."
    },
    "4": {
      "L": "By humility and the fear of the LORD are riches and honour and life.",
      "M": "The reward of humility and the fear of the LORD is riches, honor, and life.",
      "T": "If you want the things everyone wants — wealth, honor, life — here is the path: humility before others, reverence before God. It is the opposite of what most people reach for."
    },
    "5": {
      "L": "Thorns and snares are in the way of the froward; he that doth keep his soul shall be far from them.",
      "M": "Thorns and snares are in the path of the perverse; whoever guards his life will stay far from them.",
      "T": "The road the wicked have chosen is booby-trapped — thorns and snares that the self-preserving person avoids simply by not going there."
    },
    "6": {
      "L": "Train up a child in the way he should go, and when he is old he will not depart from it.",
      "M": "Train a child in the way he should go, and when he is old he will not turn from it.",
      "T": "Invest the early years in genuine formation — shaping a child in the direction that truly fits them — and what is built will hold. The training of childhood becomes the character of old age."
    },
    "7": {
      "L": "The rich ruleth over the poor, and the borrower is servant to the lender.",
      "M": "The rich rule over the poor, and the borrower is slave to the lender.",
      "T": "Money creates hierarchy. The rich have leverage over the poor whether they mean to or not. And anyone who borrows has handed a measure of their freedom to the person who lent it to them. Debt is a form of servitude."
    },
    "8": {
      "L": "He that soweth iniquity shall reap vanity, and the rod of his anger shall fail.",
      "M": "Whoever sows injustice will reap trouble, and the weapon of his rage will be broken.",
      "T": "You reap what you sow — and the person who sows cruelty and injustice harvests emptiness. The rod of anger they wield over others will eventually break in their hands."
    },
    "9": {
      "L": "He that hath a bountiful eye shall be blessed, for he giveth of his bread to the poor.",
      "M": "A generous person will be blessed, for he shares his bread with the poor.",
      "T": "The person with a generous eye — who looks at others and sees their need — will be blessed. The mechanism is simple: they give their bread to those who have none. Generosity comes first; blessing follows."
    },
    "10": {
      "L": "Cast out the scorner, and contention shall go out; yea, strife and reproach shall cease.",
      "M": "Drive out the mocker, and conflict goes with him; strife and dishonor will stop.",
      "T": "One toxic person can poison an entire community. Remove the mocker — the one who has contempt for correction and delights in tearing others down — and the conflict they generate disappears with them. Peace is sometimes about subtraction."
    },
    "11": {
      "L": "He that loveth pureness of heart, for the grace of his lips the king shall be his friend.",
      "M": "Whoever loves a pure heart and whose speech is gracious will have the king as his friend.",
      "T": "Inner purity and gracious speech are a combination that opens doors at every level, including the highest. The person who has both finds themselves welcome where others cannot go."
    },
    "12": {
      "L": "The eyes of the LORD preserve knowledge, and he overthroweth the words of the transgressor.",
      "M": "The eyes of the LORD watch over knowledge, and he frustrates the words of the treacherous.",
      "T": "God is actively watching over truth — preserving it, keeping it intact. And the lies of the faithless, however cleverly constructed, he undoes."
    },
    "13": {
      "L": "The slothful man saith, There is a lion without; I shall be slain in the streets.",
      "M": "The sluggard says, \"There is a lion outside! I will be killed in the streets!\"",
      "T": "The lazy person always has a dramatic excuse. No lion has ever prowled the streets of a normal town — but this will do as a reason not to go out. The imagination of the idle is apparently quite vivid."
    },
    "14": {
      "L": "The mouth of strange women is a deep pit; he that is abhorred of the LORD shall fall therein.",
      "M": "The mouth of an adulterous woman is a deep pit; the one under the LORD's displeasure will fall into it.",
      "T": "The seductive speech of the immoral woman is not just an attraction — it is a trap, a pit with no easy way out. The one who falls in has not merely made a bad choice; they have entered a space marked by divine judgment."
    },
    "15": {
      "L": "Foolishness is bound in the heart of a child, but the rod of correction shall drive it far from him.",
      "M": "Foolishness is bound up in the heart of a child, but the rod of discipline will drive it out.",
      "T": "Every child has foolishness built in — not as a defect but as the starting condition. What drives it out is not lectures alone but consistent, physical correction. The rod of discipline does what gentle words alone cannot."
    },
    "16": {
      "L": "He that oppresseth the poor to increase his riches, and he that giveth to the rich, shall surely come to want.",
      "M": "Oppressing the poor to enrich yourself, or giving gifts to the wealthy — both lead only to poverty.",
      "T": "Two opposite approaches to money, both wrong: crushing the poor to get ahead, and fawning on the rich to get favor. Both strategies end in want. There is no shortcut to genuine wealth."
    },
    "17": {
      "L": "Bow down thine ear, and hear the words of the wise, and apply thine heart unto my knowledge.",
      "M": "Turn your ear and listen to the words of the wise; apply your heart to my teaching.",
      "T": "This is a posture: lean in, lower yourself to listen. The wise have something to say, and you need to bring not just your ears but your whole inner attention to it."
    },
    "18": {
      "L": "For it is a pleasant thing if thou keep them within thee; they shall withal be fitted in thy lips.",
      "M": "For it is good to keep them in your heart, and to have them ready on your lips.",
      "T": "Wisdom stored in the heart does not sit idle. It surfaces at the right moment, already in your mouth — and it is pleasing: the right word for the right occasion."
    },
    "19": {
      "L": "That thy trust may be in the LORD, I have made known to thee this day, even to thee.",
      "M": "I am teaching you today — you specifically — so that your confidence may be in the LORD.",
      "T": "The whole point of the instruction is this: that you would come to trust the LORD. This is personal — addressed to you, today. The knowledge being offered is not abstract; it is a path to a specific destination."
    },
    "20": {
      "L": "Have not I written to thee excellent things in counsels and knowledge?",
      "M": "Have I not written down for you thirty excellent sayings of counsel and knowledge?",
      "T": "The question is rhetorical and confident. What has been written here is substantial — thirty sayings of genuine counsel and hard-won knowledge. The teacher knows the value of what they have put down."
    },
    "21": {
      "L": "That I might make thee know the certainty of the words of truth, that thou mightest answer the words of truth to them that send unto thee.",
      "M": "To teach you true and reliable words, so that you may give an accurate answer to those who send you.",
      "T": "The goal is reliability — to equip you so that when someone sends you with a question, or asks you to report, you can be trusted absolutely. This is wisdom in service of integrity."
    },
    "22": {
      "L": "Rob not the poor because he is poor; neither oppress the afflicted in the gate.",
      "M": "Do not rob the poor because they are poor, or crush the afflicted at the city gate.",
      "T": "The poor are an obvious target precisely because they cannot fight back. Do not exploit that. The gate — where disputes were settled and contracts made — was the place where the powerless were most vulnerable. The LORD is watching."
    },
    "23": {
      "L": "For the LORD will plead their cause, and spoil the soul of those that spoiled them.",
      "M": "For the LORD will take up their case and will plunder those who plundered them.",
      "T": "God himself is the advocate for the poor. Take from them and you have taken from someone whose patron has the power and the will to respond. The spoiler becomes the spoiled."
    },
    "24": {
      "L": "Make no friendship with an angry man, and with a furious man thou shalt not go.",
      "M": "Do not befriend an angry man or associate with someone hot-tempered.",
      "T": "The chronically angry person shapes everyone around them. Spend enough time with a furious man and you begin to absorb his way of responding to the world. This is not primarily a safety warning — it is a formation warning."
    },
    "25": {
      "L": "Lest thou learn his ways and get a snare to thy soul.",
      "M": "Lest you learn his ways and set a trap for yourself.",
      "T": "Character is contagious. The reason to avoid the angry man's company is not only what he might do to you but what you might become. His ways are learnable — and once learned, they trap you."
    },
    "26": {
      "L": "Be not thou one of them that strike hands, or of them that are sureties for debts.",
      "M": "Do not be one of those who shakes hands in a pledge or puts up security for loans.",
      "T": "Do not guarantee anyone else's debt. The handshake of surety seems like generosity — and then the debt comes due and it was not generosity at all. It was a transfer of risk onto yourself."
    },
    "27": {
      "L": "If thou hast nothing to pay, why should he take away thy bed from under thee?",
      "M": "If you have nothing to pay with, why let him take away your bed from under you?",
      "T": "The rhetorical question makes the point sharply: you pledged what you could not cover, and now you are losing your bed to pay for it. Was the surety worth this?"
    },
    "28": {
      "L": "Remove not the ancient landmark which thy fathers have set.",
      "M": "Do not move the ancient boundary stone that your ancestors put in place.",
      "T": "The boundary stone was a legal marker, but it carried the weight of everything past — the settled order of the land, the agreements of those who came before. To move it was fraud. Do not touch what has been permanently placed."
    },
    "29": {
      "L": "Seest thou a man diligent in his business? He shall stand before kings; he shall not stand before mean men.",
      "M": "Do you see a man skilled in his work? He will serve kings — not obscure people.",
      "T": "Excellence in what you do is a promoter. The diligent, skilled person rises — not because they sought influence, but because excellence is noticed by those with the power to use it. You end up standing before kings."
    }
  },
  "23": {
    "1": {
      "L": "When thou sittest to eat with a ruler, consider diligently what is before thee.",
      "M": "When you sit down to eat with a ruler, give careful thought to what is before you.",
      "T": "The meal with a ruler is not an ordinary meal. Pay attention to everything — what is being served, what is expected, what is being communicated. The wise guest knows they are being observed as much as they are observing."
    },
    "2": {
      "L": "And put a knife to thy throat if thou be a man given to appetite.",
      "M": "Put a knife to your throat if you have an unruly appetite.",
      "T": "This is a dramatic way of saying: apply the harshest possible self-discipline at this table. If you are a person of strong appetite, control yourself before you embarrass yourself — and compromise yourself."
    },
    "3": {
      "L": "Be not desirous of his dainties, for they are deceitful meat.",
      "M": "Do not crave his delicacies, for that food is deceptive.",
      "T": "The ruler's food is rich, but it is bait. What is on his table is not just food — it is part of a transaction. Craving it is how you give him leverage over you."
    },
    "4": {
      "L": "Labour not to be rich; cease from thine own wisdom.",
      "M": "Do not wear yourself out trying to get rich; have the wisdom to show restraint.",
      "T": "Stop. The relentless pursuit of wealth wears you out and makes you clever in the wrong ways. Real wisdom includes knowing when to stop reaching."
    },
    "5": {
      "L": "Wilt thou set thine eyes upon that which is not? For riches certainly make themselves wings; they fly away as an eagle toward heaven.",
      "M": "Will you exhaust your eyes chasing what is not there? Riches sprout wings and fly away like an eagle into the sky.",
      "T": "Riches are not there — not in the way you think. They disappear. Not slowly, not gradually, but with the sudden lift of an eagle: in a moment they are gone, and you are squinting at empty sky."
    },
    "6": {
      "L": "Eat thou not the bread of him that hath an evil eye, neither desire thou his dainty meats.",
      "M": "Do not eat the bread of a stingy man, and do not covet his choice food.",
      "T": "The miser's table is a trap. An 'evil eye' means a grudging, calculating gaze — nothing offered there is truly given. Do not take it; do not even want it."
    },
    "7": {
      "L": "For as he thinketh in his heart, so is he; Eat and drink, saith he to thee, but his heart is not with thee.",
      "M": "For he is one who keeps a running count in his mind; he says, \"Eat and drink,\" but his heart is not with you.",
      "T": "The miser is not what he appears. His mouth says welcome, but his heart is calculating the cost of every bite you take. He is his inner monologue — and his inner monologue does not want you there."
    },
    "8": {
      "L": "The morsel which thou hast eaten shalt thou vomit up, and lose thy sweet words.",
      "M": "You will vomit up the little you ate, and your pleasant words will have been wasted.",
      "T": "When you finally understand what the miser's table has cost you — the obligation, the discomfort, the strings attached — you will regret every bite. And the compliments you offered to be polite will have counted for nothing."
    },
    "9": {
      "L": "Speak not in the ears of a fool, for he will despise the wisdom of thy words.",
      "M": "Do not speak to a fool, for he will only scorn the wisdom behind your words.",
      "T": "Wisdom is not equally receivable by everyone. The fool will not take in what you say — not because they cannot hear the words but because they despise the wisdom behind them. Save your breath."
    },
    "10": {
      "L": "Remove not the old landmark, and enter not into the fields of the fatherless.",
      "M": "Do not move an ancient boundary stone, and do not enter the fields of orphans.",
      "T": "These two prohibitions protect those who cannot protect themselves. The orphan has no father to defend their land. The ancient landmark, once moved, strips them of their inheritance. Do not be the one who exploits that."
    },
    "11": {
      "L": "For their redeemer is mighty; he shall plead their cause with thee.",
      "M": "For their Redeemer is strong; he will plead their case against you.",
      "T": "The orphan may have no father, but they have a Redeemer — the LORD himself — and he is not weak. If you take what belongs to them, you are not stealing from a defenceless child; you are stealing from the LORD's ward. He will take up their case."
    },
    "12": {
      "L": "Apply thine heart unto instruction, and thine ears to the words of knowledge.",
      "M": "Devote your heart to instruction and your ears to words of knowledge.",
      "T": "Instruction requires more than passive hearing — it requires orienting your whole inner life toward it. The words of knowledge ask everything of you."
    },
    "13": {
      "L": "Withhold not correction from the child; for if thou beatest him with the rod, he shall not die.",
      "M": "Do not withhold discipline from a child; if you strike him with the rod, he will not die.",
      "T": "The parent who recoils from correcting their child out of misplaced tenderness is not protecting them — they are failing them. A child corrected with the rod does not die from it. A child left uncorrected may."
    },
    "14": {
      "L": "Thou shalt beat him with the rod, and shalt deliver his soul from hell.",
      "M": "If you discipline him with the rod, you will save his life from death.",
      "T": "The physical discipline the parent fears to give is, in this view, life-saving. The child who is corrected is a child being pulled back from a path that leads toward destruction. The rod is rescue."
    },
    "15": {
      "L": "My son, if thine heart be wise, my heart shall rejoice, even mine.",
      "M": "My son, if your heart is wise, then my heart will be glad as well.",
      "T": "The teacher drops the instruction for a moment to speak personally: if you become wise, it is my joy too. Your wisdom is not only yours — it comes back to the one who poured it into you."
    },
    "16": {
      "L": "Yea, my reins shall rejoice when thy lips speak right things.",
      "M": "Yes, my inmost being will rejoice when your lips speak what is right.",
      "T": "The joy is not merely intellectual. When a student speaks wisdom — genuinely right things — the teacher feels it somewhere deep inside. This is the satisfaction of having given someone something they now carry for themselves."
    },
    "17": {
      "L": "Let not thine heart envy sinners, but be thou in the fear of the LORD all the day long.",
      "M": "Do not let your heart envy sinners, but live in the fear of the LORD all day long.",
      "T": "Sinners often appear to be winning. Do not let that appearance get inside you. Envy of the wicked is the first step toward becoming one. Instead, let reverence for the LORD be the atmosphere you live in — not just in the morning or the sanctuary, but all day."
    },
    "18": {
      "L": "For surely there is an end, and thine expectation shall not be cut off.",
      "M": "For surely there is a future, and your hope will not be cut off.",
      "T": "This is the counterweight to envy: there is a future. The sinner's apparent success has a termination point. Your expectation — what you are hoping for from God — will not be taken from you."
    },
    "19": {
      "L": "Hear thou, my son, and be wise, and guide thine heart in the way.",
      "M": "Listen, my son, and be wise; keep your heart on the right path.",
      "T": "This is a distillation: hear, grow wise, direct your heart. The heart does not naturally stay on the right road. Your job is to guide it there."
    },
    "20": {
      "L": "Be not among winebibbers, among riotous eaters of flesh.",
      "M": "Do not be among those who drink too much wine or those who gorge themselves on meat.",
      "T": "Choose your company carefully. The people who organize their life around drinking and feasting will pull you into their patterns. You do not have to become them — but you should not be among them."
    },
    "21": {
      "L": "For the drunkard and the glutton shall come to poverty, and drowsiness shall clothe a man with rags.",
      "M": "For the drunkard and the glutton will come to poverty, and drowsiness will clothe them in rags.",
      "T": "Indulgence has a downstream. The drunkard and the glutton are not ruined by a single bad decision — they are ground down by the accumulated weight of their appetites. Eventually they wear their poverty as visibly as clothing."
    },
    "22": {
      "L": "Hearken unto thy father that begat thee, and despise not thy mother when she is old.",
      "M": "Listen to your father who gave you life, and do not despise your mother when she grows old.",
      "T": "Honor belongs to the ones who gave you life — not only when it is easy, not only when they are at their strongest. Your mother in her old age deserves the same attention she gave you when you were young."
    },
    "23": {
      "L": "Buy the truth and sell it not; also wisdom, and instruction, and understanding.",
      "M": "Buy the truth and do not sell it — wisdom, instruction, and understanding as well.",
      "T": "Some things you acquire are meant to be kept, not traded. Truth is one of them — wisdom, instruction, understanding. Get them at whatever cost, and do not be persuaded to part with them for anything."
    },
    "24": {
      "L": "The father of the righteous shall greatly rejoice; and he that begetteth a wise child shall have joy of him.",
      "M": "The father of a righteous child will greatly rejoice; the one who fathers a wise son will have joy from him.",
      "T": "A righteous, wise child is one of the deepest satisfactions a father can know. The joy is not pride in an achievement — it is the pleasure of having helped produce a person worth being."
    },
    "25": {
      "L": "Thy father and thy mother shall be glad, and she that bare thee shall rejoice.",
      "M": "Let your father and mother be glad; let the one who bore you rejoice.",
      "T": "When you become who wisdom calls you to be, your parents — both of them — share in it. Your mother who carried you, your father who raised you: their gladness is a gift you give them by becoming wise."
    },
    "26": {
      "L": "My son, give me thine heart, and let thine eyes observe my ways.",
      "M": "My son, give me your heart, and let your eyes keep watch over my ways.",
      "T": "The teacher asks for the most intimate thing: not compliance, not performance, but the heart. And then — watch carefully how I live. The instruction being offered is not just words; it is a life held out as a pattern."
    },
    "27": {
      "L": "For a whore is a deep ditch, and a strange woman is a narrow pit.",
      "M": "For a prostitute is a deep pit, and an immoral woman is a narrow well.",
      "T": "The imagery is of confinement and depth — not seduction but entrapment. The immoral woman is not an open door; she is a pit. You go in and there is no climbing back out."
    },
    "28": {
      "L": "She also lieth in wait as for a prey, and increaseth the transgressors among men.",
      "M": "She lies in wait like a hunter and multiplies the unfaithful among men.",
      "T": "She is not passive. She waits, she watches, she hunts. And the result is not only individual ruin — she grows the population of the faithless. One by one, she converts ordinary men into those who have broken faith."
    },
    "29": {
      "L": "Who hath woe? Who hath sorrow? Who hath contentions? Who hath babbling? Who hath wounds without cause? Who hath redness of eyes?",
      "M": "Who has grief? Who has anguish? Who has quarreling? Who has needless wounds? Who has bleary eyes?",
      "T": "The questions roll forward in a catalogue of afflictions — each one a recognizable symptom of a single cause the passage is building toward. The rhetorical build demands one answer."
    },
    "30": {
      "L": "They that tarry long at the wine; they that go to seek mixed wine.",
      "M": "Those who linger over wine and go looking for spiced wine.",
      "T": "The answer: the one who sits at the wine too long, who goes looking for the stronger blend. All those symptoms of woe have a single cause. It is not fate; it is choice."
    },
    "31": {
      "L": "Look not thou upon the wine when it is red, when it giveth his colour in the cup, when it moveth itself aright.",
      "M": "Do not look at wine when it is red and sparkling in the cup, when it goes down smoothly.",
      "T": "The danger begins before the first sip — it begins with the eyes. The wine that looks beautiful, that catches the light, that invites with its surface appeal — do not look. The trap is in the looking."
    },
    "32": {
      "L": "At the last it biteth like a serpent, and stingeth like an adder.",
      "M": "In the end it bites like a snake and stings like a viper.",
      "T": "What went in smoothly comes out with fangs. The pleasant journey in becomes a serpent bite on the way out. This is the whole arc of wine's deception: smooth entry, venomous conclusion."
    },
    "33": {
      "L": "Thine eyes shall behold strange women, and thine heart shall utter perverse things.",
      "M": "Your eyes will see things that are not there, and your heart will say perverse things.",
      "T": "The drunk person's vision becomes corrupted — they see women in distorted ways, and what comes out of them is perverse. The wine has not just affected their head; it has reached their eyes and their heart."
    },
    "34": {
      "L": "Yea, thou shalt be as he that lieth down in the midst of the sea, or as he that lieth upon the top of a mast.",
      "M": "You will be like one asleep in the middle of the sea, like one sprawled on top of a ship's mast.",
      "T": "A man asleep in open water, a man sprawled on the top of a mast — both images of precarious, oblivious danger. The drunk person is in the middle of peril and has no awareness of it. That is the real danger: not just the risk, but the inability to perceive it."
    },
    "35": {
      "L": "They have stricken me, shalt thou say, and I was not sick; they have beaten me, and I felt it not. When shall I awake? I will seek it yet again.",
      "M": "\"They beat me, but I felt no pain; they struck me, but I did not know it. When will I wake up so I can have another drink?\"",
      "T": "The drinker wakes with bruises from a beating they do not remember. Their first thought is not: what has this done to me? Their first thought is: when can I drink again? This is the portrait of compulsion — the harm thoroughly absorbed, the desire entirely intact."
    }
  },
  "24": {
    "1": {
      "L": "Be not thou envious against evil men, neither desire to be with them.",
      "M": "Do not envy evil people or wish to be in their company.",
      "T": "Evil people sometimes look attractive. Do not let yourself be drawn toward them by envy of what they seem to have. And do not desire their company — what you absorb by proximity is not worth it."
    },
    "2": {
      "L": "For their heart studieth destruction, and their lips talk of mischief.",
      "M": "For their heart plans violence, and their lips talk about causing trouble.",
      "T": "Look at what they are actually doing with their minds and their words: planning harm, discussing trouble. This is not ambition in an awkward form — it is malice. You should not want to be anywhere near it."
    },
    "3": {
      "L": "Through wisdom is an house builded, and by understanding it is established.",
      "M": "By wisdom a house is built, and by understanding it is established.",
      "T": "A house built on wisdom holds together. Not wealth alone, not effort alone — but the quality of understanding behind the building. What understanding establishes does not easily fall."
    },
    "4": {
      "L": "And by knowledge shall the chambers be filled with all precious and pleasant riches.",
      "M": "Through knowledge the rooms are filled with all kinds of precious and pleasant treasures.",
      "T": "And the interior of that house — room after room — fills up with good things. Knowledge is generative. It does not just build walls; it fills them with the best the world offers."
    },
    "5": {
      "L": "A wise man is strong; yea, a man of knowledge increaseth strength.",
      "M": "A wise man is strong, and a man of knowledge grows in might.",
      "T": "Wisdom is not opposed to strength — it produces it. The person of genuine knowledge does not grow weaker as they learn more; they become more capable, more resilient, stronger than their physical resources alone would make them."
    },
    "6": {
      "L": "For by wise counsel thou shalt make thy war; and in multitude of counsellors there is safety.",
      "M": "For by wise guidance you can wage war, and victory depends on having many advisers.",
      "T": "War is not won by bravery alone. Before the battle there is strategy, and strategy requires multiple voices. The general who has gathered counsel around him has access to what no single brilliant mind can provide."
    },
    "7": {
      "L": "Wisdom is too high for a fool; he openeth not his mouth in the gate.",
      "M": "Wisdom is beyond a fool's reach; he has nothing to say at the city gate.",
      "T": "The gate was where serious community decisions were made — where elders deliberated and matters of consequence were decided. The fool has nothing to contribute there. Wisdom operates at a level he simply cannot reach."
    },
    "8": {
      "L": "He that deviseth to do evil shall be called a mischievous person.",
      "M": "Whoever schemes to do evil will be known as a troublemaker.",
      "T": "Planning harm is not just bad behavior — it gives you a name. The community sees what you are and assigns you a label. Your scheming becomes your identity."
    },
    "9": {
      "L": "The thought of foolishness is sin, and the scorner is an abomination to men.",
      "M": "The intention behind foolish schemes is sin, and the mocker is detestable to everyone.",
      "T": "The sinfulness is not just in the act — it is in the intention, the thought behind the fool's scheming. And the mocker, who treats wisdom and its bearers with contempt, makes themselves repugnant to everyone around them."
    },
    "10": {
      "L": "If thou faint in the day of adversity, thy strength is small.",
      "M": "If you falter in times of trouble, how small is your strength!",
      "T": "What the day of adversity reveals is not just how hard things got — it reveals how much strength you actually had. If you collapse under pressure, the pressure has not defeated you so much as exposed you."
    },
    "11": {
      "L": "If thou forbear to deliver them that are drawn unto death, and those that are ready to be slain.",
      "M": "Rescue those being taken away to death; hold back those stumbling toward slaughter.",
      "T": "When people are being led toward death, your silence is a choice. Inaction in the face of their destruction is not neutrality — it is abandonment. Rescue the ones who can still be rescued."
    },
    "12": {
      "L": "If thou sayest, Behold, we knew it not; doth not he that pondereth the heart consider it? And he that keepeth thy soul, doth not he know it? And shall not he render to every man according to his works?",
      "M": "If you say, \"We did not know this,\" does not he who weighs the heart perceive it? Does not he who guards your life know it? Will he not repay each person according to what they have done?",
      "T": "The excuse of ignorance does not hold before the one who weighs hearts. You say you did not know. He knows whether you knew or could have known — he knows the inside of you. And he will render accordingly."
    },
    "13": {
      "L": "My son, eat thou honey, because it is good, and the honeycomb, which is sweet to thy taste.",
      "M": "My son, eat honey because it is good, and the honeycomb that is sweet to your taste.",
      "T": "The comparison that follows makes the honey into more than honey — but first, just taste it. It is genuinely good. The illustration respects the original thing before it uses it."
    },
    "14": {
      "L": "So shall the knowledge of wisdom be unto thy soul; when thou hast found it, then there shall be a reward, and thy expectation shall not be cut off.",
      "M": "So is wisdom to your soul; when you find it, there is a future, and your hope will not be cut off.",
      "T": "Wisdom is honey for the soul — sweetness, nourishment, genuine goodness. And when you find it, something is secured: there is a future ahead of you, a reward, an expectation that will not be disappointed. This is the taste of something permanent."
    },
    "15": {
      "L": "Lay not wait, O wicked man, against the dwelling of the righteous; spoil not his resting place.",
      "M": "Do not lie in wait against the home of the righteous, O wicked man; do not raid his dwelling.",
      "T": "This is an address to the wicked directly — an unusual, confrontational move. Do not target the righteous. Do not plot against their household. You think you are targeting them; you are stepping into a conflict with the God who protects them."
    },
    "16": {
      "L": "For a just man falleth seven times and riseth up again, but the wicked shall fall into mischief.",
      "M": "For a righteous person falls seven times and gets up again, but the wicked are brought down by calamity.",
      "T": "Seven times fallen, seven times rising. The righteous are not immune to collapse — they fall repeatedly. What distinguishes them is that they get back up. The wicked fall too — but they stay down, brought low by what they themselves have done."
    },
    "17": {
      "L": "Rejoice not when thine enemy falleth, and let not thine heart be glad when he stumbleth.",
      "M": "Do not gloat when your enemy falls, and do not let your heart be glad when he stumbles.",
      "T": "Even when the enemy you have endured finally trips and falls, do not let satisfaction take over your heart. This is not only about your enemy's dignity — it is about yours. And what follows explains the risk."
    },
    "18": {
      "L": "Lest the LORD see it, and it displease him, and he turn away his wrath from him.",
      "M": "Lest the LORD see it and be displeased, and he turns his anger away from your enemy.",
      "T": "Your gloating can change the equation. If the LORD sees you delighting in your enemy's fall, he may turn his judgment away from them — toward you. The vindication you thought was coming gets redirected by your own indulgence in it."
    },
    "19": {
      "L": "Fret not thyself because of evil men, neither be thou envious at the wicked.",
      "M": "Do not fret because of evildoers or be envious of the wicked.",
      "T": "Do not exhaust yourself worrying about the wicked. Do not let their apparent success make you envious. They are not winning — not in the way that ultimately matters."
    },
    "20": {
      "L": "For there shall be no reward to the evil man; the candle of the wicked shall be put out.",
      "M": "For the evil person has no future reward; the lamp of the wicked will be snuffed out.",
      "T": "The wicked person's light goes out. There is no long arc of prosperity for them — no ongoing reward, no burning lamp at the end. It ends. This is why envy is so completely misplaced."
    },
    "21": {
      "L": "My son, fear thou the LORD and the king, and meddle not with them that are given to change.",
      "M": "My son, fear the LORD and the king, and do not associate with those who seek to undermine either.",
      "T": "The fear of the LORD and appropriate respect for the king go together here. And the warning against those who are always agitating for destabilizing change is practical: the people who traffic in revolution put everyone near them at risk."
    },
    "22": {
      "L": "For their calamity shall rise suddenly; and who knoweth the ruin of them both?",
      "M": "For their disaster will come suddenly, and who knows what destruction may come from both?",
      "T": "The LORD and the king both have the power to destroy suddenly and unpredictably. Align yourself against either, and you have taken on risks you cannot calculate. The collapse, when it comes, will surprise you."
    },
    "23": {
      "L": "These things also belong to the wise. It is not good to have respect of persons in judgment.",
      "M": "These also are sayings of the wise: showing partiality in judgment is not right.",
      "T": "The wise know this: favoritism in legal proceedings is a corruption of the whole system. Justice must be blind to the identity of who stands before it."
    },
    "24": {
      "L": "He that saith unto the wicked, Thou art righteous; him shall the people curse, nations shall abhor him.",
      "M": "Whoever tells the guilty, \"You are innocent,\" will be cursed by peoples and condemned by nations.",
      "T": "Declaring the wicked to be righteous — in court, in public, anywhere truth is meant to govern — is a betrayal that earns universal condemnation. People curse it; nations abhor it. This is not an unpopular position — it is the consensus of those who understand what justice is for."
    },
    "25": {
      "L": "But to them that rebuke him shall be delight, and a good blessing shall come upon them.",
      "M": "But those who rebuke the wicked will find delight, and a generous blessing will come over them.",
      "T": "The judge who tells the truth, who rebukes the wicked for what they are, will find themselves blessed. The unpopular verdict becomes, in the end, the path to favor — not with the wicked, but with the God who watches over justice."
    },
    "26": {
      "L": "Every man shall kiss his lips that giveth a right answer.",
      "M": "Whoever gives an honest answer is like a kiss on the lips.",
      "T": "An honest answer is an act of genuine affection — more intimate than it appears. To speak the truth plainly, to give the answer that actually fits the situation, is a gift as warm as a kiss."
    },
    "27": {
      "L": "Prepare thy work without, and make it fit for thyself in the field; and afterwards build thine house.",
      "M": "Prepare your outdoor work and get your fields ready; after that, build your house.",
      "T": "Do the work that produces income before you invest in your living arrangements. Get the field productive first. Build the house when the farm can support it. This is about sequence: do not build comfort on a foundation that has not yet been established."
    },
    "28": {
      "L": "Be not a witness against thy neighbour without cause; and deceive not with thy lips.",
      "M": "Do not testify against your neighbor without cause, and do not deceive with your lips.",
      "T": "There is no legitimate reason to bring false or unjustified charges against your neighbor. Your lips are capable of destroying someone. Do not use them that way."
    },
    "29": {
      "L": "Say not, I will do so to him as he hath done to me; I will render to the man according to his work.",
      "M": "Do not say, \"I will do to him what he did to me; I will repay him for what he has done.\"",
      "T": "Vengeance feels like justice, but it is not yours to execute. Do not make yourself the instrument of your own payback — the one who decides what someone deserves and delivers it. That judgment belongs elsewhere."
    },
    "30": {
      "L": "I went by the field of the slothful, and by the vineyard of the man void of understanding.",
      "M": "I passed by the field of a lazy man and the vineyard of a man who lacked sense.",
      "T": "The teacher is reporting an observation — a lesson drawn from what they actually saw walking past. This is wisdom grounded in experience, not theory."
    },
    "31": {
      "L": "And, lo, it was all grown over with thorns, and nettles had covered the face thereof, and the stone wall thereof was broken down.",
      "M": "It was all overgrown with thorns; the ground was covered with nettles, and the stone wall was in ruins.",
      "T": "Neglect has its own visible grammar. Thorns, nettles, a collapsed wall — these are the vocabulary of abandonment. The field tells you everything about its owner without a word being said."
    },
    "32": {
      "L": "Then I saw, and considered it well; I looked upon it, and received instruction.",
      "M": "I saw it and took it to heart; I looked and received instruction.",
      "T": "The wise person does not just pass by — they stop, look carefully, and receive what the moment offers. A ruined field is a classroom for anyone willing to let it teach them."
    },
    "33": {
      "L": "Yet a little sleep, a little slumber, a little folding of the hands to sleep.",
      "M": "A little sleep, a little slumber, a little folding of the hands to rest —",
      "T": "This is the lazy person's inner voice — the never-quite-decisive drift into just a little more. Not an outright refusal to work; just postponing it by increments. The hands fold. The eyes close. Just a little more."
    },
    "34": {
      "L": "So shall thy poverty come as one that travelleth; and thy want as an armed man.",
      "M": "Then poverty will come on you like a wanderer, and your need like an armed man.",
      "T": "Poverty does not always arrive with warning. Sometimes it moves like a traveler appearing on the road — you did not see it coming, and now it is here. And sometimes it arrives like a soldier: unmovable and demanding. The little sleep prepared the way for both."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'proverbs')
        merge_tier(existing, PROVERBS, tier_key)
        save(tier_dir, 'proverbs', existing)
    print('Proverbs 22–24 written.')

if __name__ == '__main__':
    main()
