"""
MKT Job chapters 34–36 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-job-34-36.py

=== Overview of this unit ===

Ch 34 — Elihu's Second Speech to Job and the Wise (37 verses): Elihu addresses both
         Job and the assembled wise men, making the case that God cannot commit iniquity.
         He quotes Job's own charges (vv.5-9), then argues from God's role as sole
         governor of creation: no one appointed God; if he withdrew his Spirit all flesh
         would die; he sees every step and hides nothing. He closes by calling Job's
         speech the speech of wicked men and demanding more testing.

Ch 35 — Elihu's Argument on Profit (16 verses): Elihu addresses the implied claim that
         Job's righteousness exceeds God's. His answer: human sin and virtue do not
         affect God — they land horizontally on other human beings. The oppressed cry
         but without genuinely seeking their Maker (they cry from pain, not from prayer),
         so God does not answer. Job's many words are empty because they come from
         a place of misunderstanding rather than genuine seeking.

Ch 36 — Elihu's Final Defense of God (33 verses): Elihu claims to speak on God's
         behalf from wide-ranging knowledge. He defends divine pedagogy: God watches
         the righteous, and when they fall into chains of affliction he shows them their
         fault, opens their ears to instruction, and invites them to turn. The godless
         respond to binding with stored resentment; the genuinely afflicted receive
         deliverance through oppression. Elihu closes with a warning to Job followed
         by a nature hymn (vv.22–33) that anticipates the Yahweh speeches of chs 38–41.

=== Contested-term decisions (carried forward from mkt-job-31-33.py) ===

H410  (אֵל, El): "God" in all tiers.
H433  (אֱלוֹהַּ, Eloah): "God" in all tiers — Job's preferred singular poetic form.
H7706 (שַׁדַּי, Shaddai): "the Almighty" in all tiers — consistent across all Job scripts.
H3068 (יהוה): does not appear in these chapters; Elihu's speeches use El/Eloah/Shaddai.
H136  (אֲדֹנָי, Adonai): not present in these chapters.

H7307 (רוּחַ, ruach):
      34:14 — "his Spirit" — the animating divine breath that if withdrawn would collapse
               all living things; capital S throughout tiers, as in ch 32–33.

H5315 (נֶפֶשׁ, nefesh):
      36:14 — "their life" in M/T — the embodied self dying early among the degraded.

H4941 (מִשְׁפָּט, mishpat): "judgment / justice" — rendered by context; the legal register
      of vv.34:5,17 and the ethical-governance sense of 36:17.

H7562 (רֶשַׁע, resha): "wickedness / wrong" — God cannot commit it (34:10,12).

H2611 (חָנֵף, chaneph, 34:30; 36:13): "godless / hypocrite in heart" — rendered "godless"
      in M/T (the person who is profane, empty of real reverence) and "hypocrite in heart"
      in L following the Hebrew's literalness.

H6921 (קֶדֶם, qedem): "from afar / from a distance" in 36:3 — Elihu says he will fetch
      his knowledge from a wide range, reaching beyond local tradition.

H7489 (רָעַע, ra'a, 34:12): "do wickedly / pervert" — used of what God will never do
      to justice.

=== Aspect and tense notes ===

Ch.34: The verse pattern alternates between Elihu's assertions (imperfect/present) and
       quotations of Job (past/perfect, reporting Job's stated positions). In L, maintain
       the modal/conditional flavour of rhetorical questions (vv.17-19). The closing
       section (vv.31-37) has a strongly argumentative present-tense character.

Ch.35: The questions in vv.2-7 are genuine interrogatives forcing Job to see the
       implications of his position. Aorist-equivalent Hebrew perfects in vv.9-12 describe
       habitual behaviour of the oppressed (they cry; he does not answer).

Ch.36: Elihu's final address mixes conditional sequences (vv.8-12: if they are bound...
       if they obey...) with indicative declarations about God's character. The nature
       hymn (vv.27-33) uses participial and imperfect forms to describe ongoing divine
       activity — God continuously makes, draws up, commands. T should sustain that
       present-tense dynamism.

=== OT echo notes ===

34:14-15 — The withdrawal of Spirit and breath echoes Genesis 2:7 (breath of life) and
            Psalm 104:29-30 (withdraw breath → they die; send Spirit → they are created).
            T surfaces this in those verses.

35:10   — "songs in the night" echoes the nighttime praise of Ps 42:8 and anticipates
            the Pauline tradition of singing at midnight (Acts 16:25). T notes this.

36:8-10 — The pattern of chains → instruction → turning parallels the Assyrian-captivity
            framework in Hos 5:15 and the Deuteronomic exile-and-return theology. T notes
            the structural echo without overclaiming.

36:27-33 — This passage is the immediate warm-up to the Yahweh speeches. Elihu's nature
            hymn covers the same territory (rain, thunder, lightning) but from the outside.
            When Yahweh speaks in chs 38–41 he will cover the same ground from inside.
            T notes this positioning in v.33.
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


JOB = {
  # ============================================================
  # Chapter 34 — Elihu's Second Speech: God Cannot Do Wrong
  # ============================================================
  "34": {
    "1": {
      "L": "Furthermore Elihu answered and said:",
      "M": "Elihu answered and said:",
      "T": "Elihu speaks again — still not finished."
    },
    "2": {
      "L": "Hear my words, O wise men; and give ear unto me, ye that have knowledge.",
      "M": "Hear my words, O wise men; listen to me, you who have knowledge.",
      "T": "He turns from Job to the wider audience — the assembled wise. He is not making a private argument; he is making a public case and calling those with discernment to evaluate it."
    },
    "3": {
      "L": "For the ear trieth words as the mouth tasteth meat.",
      "M": "For the ear tests words as the palate tastes food.",
      "T": "The opening analogy is precise: wisdom requires active discernment, not mere reception. Words must be tested as food is tasted — some nourish, some are bitter, some are rotten. Listen, but evaluate what you are hearing."
    },
    "4": {
      "L": "Let us choose to us what is right; let us know among ourselves what is good.",
      "M": "Let us choose together what is right; let us determine among ourselves what is good.",
      "T": "An invitation to communal deliberation, not a lecture to be absorbed. Elihu presents himself as asking the wise to reason alongside him toward a verdict — though he already knows what his verdict is."
    },
    "5": {
      "L": "For Job hath said: I am righteous, and God hath taken away my right.",
      "M": "For Job has said, 'I am righteous, and God has denied me my right.'",
      "T": "Here is Job's claim, stated plainly. Two assertions: first, his innocence — maintained throughout and never honestly rebutted. Second, that God has acted unjustly toward him. Elihu is about to accept the first and contest the second."
    },
    "6": {
      "L": "Should I lie about my right? My wound is incurable, though I am without transgression.",
      "M": "Must I lie about my case? My wound is past healing, though I have done no wrong.",
      "T": "Job's complaint comes out raw and honest as ever: if he said his suffering was deserved, he would be lying. The wound is real. The innocence is real. Holding both together is precisely what the book cannot resolve through any easy framework."
    },
    "7": {
      "L": "What man is like Job, who drinketh up scorning like water?",
      "M": "What man is like Job, who drinks mockery like water?",
      "T": "A caustic question. Cynical dismissal of God's governance flows through Job easily, naturally, in great quantity — like drinking water. Elihu's charge is at least partly apt: Job's speech has been scathing, and some of it has been aimed at God's justice itself."
    },
    "8": {
      "L": "Which goeth in company with the workers of iniquity and walketh with wicked men.",
      "M": "Who keeps company with evildoers and walks with wicked men.",
      "T": "The company Job is keeping is theological rather than literal. When a man says 'it profits nothing to delight in God,' he is voicing the same cynicism as those who have no use for God at all. Elihu is saying Job's words have drifted into dangerous alignment."
    },
    "9": {
      "L": "For he hath said: It profiteth a man nothing that he should be pleasing to God.",
      "M": "For he has said, 'A man gains nothing by delighting in God.'",
      "T": "This is the theological crux of Elihu's indictment. Job has said, in effect, that virtue is a losing transaction — that obedience earns nothing with God. The difficulty is that Job's own experience has seemed to demonstrate exactly this: he was blameless, and look at him. Elihu is dealing with a real problem."
    },
    "10": {
      "L": "Therefore hearken unto me, ye men of understanding: far be it from God to do wickedness, and from the Almighty to do iniquity.",
      "M": "Therefore, men of understanding, listen to me: far be it from God to do evil, far from the Almighty to commit wrong.",
      "T": "Elihu's foundational premise. God is not capable of wickedness — not merely that he happens not to have been wicked, but that wickedness is incompatible with his nature. But Elihu does not deal with the reverse problem: if God cannot be unjust, how does one explain Job's experience?"
    },
    "11": {
      "L": "For the work of a man shall he render unto him and cause every man to find according to his ways.",
      "M": "For he repays each person according to their work and deals with everyone according to their conduct.",
      "T": "God is a perfect rewarder. He gives back exactly what each person's work deserves. The difficulty is that Job's work — by his own claim and by the book's prologue — does not warrant what happened to him. Elihu is reasserting a principle the narrative has already complicated."
    },
    "12": {
      "L": "Yea, surely God will not do wickedly, neither will the Almighty pervert judgment.",
      "M": "Of a truth, God will not act wickedly; the Almighty will not pervert justice.",
      "T": "The double affirmation: God will not be wicked; the Almighty will not bend the moral order of the universe away from what is right. Elihu states this as a fixed axiom. Job has been living the apparent exception."
    },
    "13": {
      "L": "Who hath given him charge over the earth? Or who hath disposed the whole world?",
      "M": "Who gave him his charge over the earth? Who appointed him over the whole world?",
      "T": "The rhetorical questions are devastating in their simplicity: no one appointed God. He is not an administrator who received authority from above and could be held accountable to a higher charter. He is the original authority. There is no court above him to which Job's appeal could be lodged."
    },
    "14": {
      "L": "If he set his heart upon man, if he gather unto himself his Spirit and his breath —",
      "M": "If he should set his heart against us and gather to himself his Spirit and breath —",
      "T": "The most radical of Elihu's arguments: if God withdrew what he put in. The Spirit — the animating breath of God poured into every living thing at creation (Gen 2:7; Ps 104:29) — is his to withdraw. Nothing in creation is self-sustaining. We live entirely by divine loan."
    },
    "15": {
      "L": "All flesh shall perish together, and man shall return again unto dust.",
      "M": "All flesh would perish together, and human beings would return to dust.",
      "T": "Without that breath, everything collapses. Genesis 3 runs in reverse. The dust waits, as it always has. The entire universe of living things is sustained by an act of God's ongoing will — not by any independent vitality of its own."
    },
    "16": {
      "L": "If now thou hast understanding, hear this; hearken to the voice of my words.",
      "M": "If you have understanding, hear this; listen to what I am saying.",
      "T": "The theology established, Elihu turns back to Job. If Job has the capacity for understanding that Elihu believes he does, let him follow the argument now."
    },
    "17": {
      "L": "Shall even he that hateth justice govern? And wilt thou condemn him who is most right?",
      "M": "Shall one who hates justice govern? Will you condemn the One who is righteous and mighty?",
      "T": "The inversion Elihu wants Job to see: to say God has dealt unjustly is to say the governor of all things hates justice, and that the most righteous being in existence can be condemned by one of his creatures. Both conclusions are impossible. Backing out from the impossibility of the conclusion should tell Job something about the premise."
    },
    "18": {
      "L": "Is it right to say to a king, 'Thou art worthless!' and to nobles, 'Ye are wicked'?",
      "M": "Is it right to say to a king, 'You are worthless,' and to nobles, 'You are wicked'?",
      "T": "A question about the fitness of language to its object. No one addresses a king this way — not because kings are infallible, but because the language does not match the relationship. Elihu is pressing the category issue: if such language is unfit for a king, what makes Job think it fits the one who made kings?"
    },
    "19": {
      "L": "How much less to him who accepteth not the persons of princes, nor regardeth the rich more than the poor, for they are all the work of his hands?",
      "M": "How much less to him who shows no partiality to princes and does not favor the rich over the poor, for they are all the work of his hands?",
      "T": "The argument takes an unexpected turn: God himself does not operate by the rules of human status. He made them all — rich and poor, noble and peasant — with the same hands. He does not favor anyone. The one Elihu says Job should not address as 'wicked' is precisely the one who already treats everyone as equal. The social hierarchy that makes kings untouchable does not apply to the one who is above all kings."
    },
    "20": {
      "L": "In a moment they die; at midnight the people are shaken and pass away, and the mighty are removed without hand.",
      "M": "In a moment they die; at midnight the people are convulsed and pass away, and the mighty are removed — without human effort.",
      "T": "The mighty die without being killed. In a moment, at midnight — when no army is gathered, no revolution is mounting, no force could account for it — they are simply gone. God does not need instruments. Power does not protect against the one who granted it."
    },
    "21": {
      "L": "For his eyes are upon the ways of a man, and he seeth all his goings.",
      "M": "For his eyes are on the ways of everyone, and he sees all their steps.",
      "T": "Total surveillance — not hostile but simply the fact of perfect knowledge. Every path, every step, seen without exception. This is the same reality Job has been invoking when he complained that God was watching him too closely; Elihu states it as a general principle rather than something directed at Job personally."
    },
    "22": {
      "L": "There is no darkness nor shadow of death where the workers of iniquity may hide themselves.",
      "M": "There is no darkness or deep shadow where evildoers can hide themselves.",
      "T": "The darkness that criminals escape into does not exist for those fleeing God. The shadow of death — the deepest darkness available to human experience — is not dark to him."
    },
    "23": {
      "L": "For he will not lay upon man more than is right, that he enter into judgment with God.",
      "M": "For he does not impose on anyone more than is warranted to bring them before God in judgment.",
      "T": "His judgments are precise and fair. He does not heap on a human being more than the case requires. When people face God in judgment, the charge is exactly what the evidence warrants — not inflated, not manufactured, not designed to overwhelm. Job's demand for a hearing is based on the assumption that God has over-burdened him. Elihu says that cannot happen."
    },
    "24": {
      "L": "He shall break in pieces mighty men without inquiry and set others in their place.",
      "M": "He shatters the mighty without investigation and sets others in their place.",
      "T": "The turnover of power is God's work, done without lengthy inquiry — no trial, no careful assembly of evidence. He removes the mighty and installs others. From inside a human life this looks arbitrary; from outside it is the consistent expression of a will that sees what human courts do not."
    },
    "25": {
      "L": "Therefore he knoweth their works; he overturneth them in the night, so that they are crushed.",
      "M": "For he knows their deeds, and he overturns them in the night; they are crushed.",
      "T": "He knows, then he acts. In the night — quietly, suddenly, without announcement — the overturning happens. The crushing comes at the moment no one expected."
    },
    "26": {
      "L": "He striketh them as wicked men in the sight of others —",
      "M": "He strikes them for their wickedness in an open place where others can see —",
      "T": "The judgment is not private. It happens where it can be witnessed. The striking is part of the public record of the universe — part of what observing people can learn from, if they are paying attention."
    },
    "27": {
      "L": "Because they turned aside from him and would not consider any of his ways —",
      "M": "Because they turned away from following him and gave no thought to any of his ways —",
      "T": "The reason the mighty fall is not arbitrary malice. They turned. Not that they were born wicked, but that they looked away from God — from following his ways, from considering his paths — and refused to look back."
    },
    "28": {
      "L": "So that they caused the cry of the poor to come before him, and he heard the cry of the afflicted.",
      "M": "So that they brought the cry of the poor before him, and he heard the outcry of the afflicted.",
      "T": "The oppression produced a cry that reached God. He heard it — the specific voices of those the mighty were grinding down. That hearing is the mechanism by which the mighty fall. It is not abstract justice; it is a response to a voice, individual and particular."
    },
    "29": {
      "L": "When he giveth quietness, who then can condemn? And when he hideth his face, who then can behold him? Whether it be done against a nation, or against a man only —",
      "M": "When he is quiet, who can condemn? When he hides his face, who can see him? Whether dealing with a nation or with a single person —",
      "T": "The sovereignty of divine silence. When God is quiet, no one has standing to convict him of injustice. When he withdraws his visible presence, no one can locate him well enough to summon him to court. This applies to nations and to individuals alike. Job, one individual, cannot hold God in contempt of court for choosing silence."
    },
    "30": {
      "L": "That the godless reign not, that they be not a snare to the people.",
      "M": "lest a godless person reign and ensnare the people.",
      "T": "The purpose of God's overturning of power is not chaos — it is protection. If the godless ruled without restraint, the people beneath them would be trapped, their lives bent entirely around the interests of those who have no use for God. God removes power to prevent that outcome."
    },
    "31": {
      "L": "Surely it is meet to be said unto God: I have borne chastisement; I will not offend any more.",
      "M": "Has anyone said to God, 'I have endured my punishment; I will not sin any more'?",
      "T": "Here is what Elihu thinks Job should have said. Not defiant demands for a hearing, not charges of divine injustice — but the honest acknowledgment of someone who has received a lesson: I have borne this. I understand. I will change. Whether Job's suffering was actually chastisement for sin is precisely what the book is questioning."
    },
    "32": {
      "L": "Teach me what I see not; if I have done iniquity, I will do it no more.",
      "M": "And: 'Teach me what I cannot see; if I have done wrong, I will not do it again.'",
      "T": "The posture Elihu commends is genuine teachability: Lord, show me what I'm missing. If I have sinned, I want to know it. That is the prayer of a person open to correction. Whether Job's situation fits this prescription is another matter, but the prayer itself is right."
    },
    "33": {
      "L": "Should he recompense it according to thy mind? For thou dost refuse it, so thou must choose, not I; speak therefore what thou knowest.",
      "M": "Should he repay you on your own terms because you reject his? For you must choose, not I; tell me then what you know.",
      "T": "A pointed challenge. If Job insists on his own terms for how God should deal with him, let him state them plainly and explain his reasoning. Elihu will not choose for him. The argument returns to Job: you are the one making the claims. Make them openly, or stop making them."
    },
    "34": {
      "L": "Men of understanding will say to me, yea, every wise man that heareth me:",
      "M": "People of understanding will agree with me, and every wise person who hears me will say:",
      "T": "Elihu appeals to the tribunal of wisdom one more time. He is confident that those who are genuinely discerning — not those who merely sound discerning — will endorse his verdict."
    },
    "35": {
      "L": "'Job speaketh without knowledge, and his words are without wisdom.'",
      "M": "'Job speaks without knowledge; his words are without insight.'",
      "T": "The verdict of the wise: Job speaks without knowledge, without wisdom. This is a striking judgment against the man the book's prologue commended as blameless, the man God himself praised. Elihu's verdict here will be reversed at the end of the book when God tells the friends they have not spoken rightly as Job did."
    },
    "36": {
      "L": "My desire is that Job be tried unto the end, because of his answers like those of wicked men.",
      "M": "Would that Job were tested to the limit, because his answers are like those of wicked men.",
      "T": "Elihu would have Job tested further — pressed harder by the examination. The answers Job has given sound to him like the speech of the wicked. He wants more testing because he is convinced that continued pressure will reveal the hidden sin he is certain must be there."
    },
    "37": {
      "L": "For he addeth rebellion unto his sin; he clappeth his hands among us and multiplieth his words against God.",
      "M": "For he adds rebellion to his sin; he mocks us and heaps up words against God.",
      "T": "Job's speech is not just wrong, in Elihu's reckoning — it compounds whatever original offense started all this. Each word against God is an act of rebellion added to the account. The clapping of hands is a gesture of contempt. The multiplication of words against God is a kind of escalating spiritual defiance that Elihu finds intolerable. On this note — fierce and certain — his second speech ends."
    }
  },

  # ============================================================
  # Chapter 35 — Elihu on Profit: Human Virtue Does Not Affect God
  # ============================================================
  "35": {
    "1": {
      "L": "Elihu spake moreover and said:",
      "M": "Elihu continued and said:",
      "T": "Still not done. Elihu has more."
    },
    "2": {
      "L": "Thinkest thou this to be right, that thou saidst: My righteousness is more than God's?",
      "M": "Do you think this is just when you say, 'My righteousness is more than God's'?",
      "T": "Elihu takes aim at what he hears as the logical implication of Job's complaint. If God has been unjust to Job, and Job is innocent, then in this case Job is morally superior to God. Elihu is pressing Job to see where the argument leads when followed to its end."
    },
    "3": {
      "L": "For thou saidst: What advantage will it be to thee? What profit shall I have more than if I had sinned?",
      "M": "For you say, 'What does it benefit you? What do I gain from not sinning?'",
      "T": "Elihu hears in Job's words a transactional complaint: righteousness has cost Job everything and produced nothing. The implied question is whether faithfulness to God is a paying proposition. Job has run the experiment and found it doesn't pay. This is a real problem, and Elihu has to answer it."
    },
    "4": {
      "L": "I will answer thee and thy companions with thee.",
      "M": "I will give you an answer, and your companions along with you.",
      "T": "Not just Job but the friends who have been sitting in silence — Elihu addresses the whole circle. The answer he is about to give is not private counsel; it is a public theological statement."
    },
    "5": {
      "L": "Look unto the heavens and see; and behold the clouds, which are higher than thou.",
      "M": "Look up at the sky and see; behold the clouds, higher than you.",
      "T": "Before the argument: a reorientation of scale. Look up. The clouds are above you. Now think about how far above them God is. Perspective before reasoning — the common problem is that we reason about God while looking at our own level."
    },
    "6": {
      "L": "If thou sinnest, what doest thou against him? Or if thy transgressions be multiplied, what doest thou unto him?",
      "M": "If you sin, what do you accomplish against him? If your transgressions multiply, what do you do to him?",
      "T": "The central theological claim: your sin does not wound God. It does not diminish him, disturb his functioning, or take something essential from him. He is not harmed by human wrongdoing. This cuts in both directions, as the next verse shows."
    },
    "7": {
      "L": "If thou be righteous, what givest thou him? Or what receiveth he of thine hand?",
      "M": "If you are righteous, what do you give him? What does he receive from your hand?",
      "T": "The reverse: your righteousness is not a gift that enriches God. He does not need your goodness to function. This is a corrective to any transactional view of obedience — the idea that by being good we put God in our debt, and that God therefore owes us something in return."
    },
    "8": {
      "L": "Thy wickedness may hurt a man as thou art, and thy righteousness may profit the son of man.",
      "M": "Your wickedness harms only someone like yourself, and your righteousness benefits only other people.",
      "T": "Here is where goodness and wickedness actually go: horizontally, not vertically. They land on the people around you. The widow who was helped or refused, the poor man who was fed or not — they are the ones who receive the impact. God receives nothing either way. This is Elihu's answer to Job's implied question about the profit of righteousness."
    },
    "9": {
      "L": "By reason of the multitude of oppressions they cry out; they cry for help because of the arm of the mighty.",
      "M": "Under the weight of great oppression people cry out; they call for help from the arm of the powerful.",
      "T": "The oppressed cry out. This is not an abstraction — it is the specific, audible crying of people being ground down by power. Elihu is about to explain why God's response depends on the quality of that cry."
    },
    "10": {
      "L": "But none saith: Where is God my Maker, who giveth songs in the night?",
      "M": "But no one asks, 'Where is God my Maker, who gives songs in the night?'",
      "T": "The crying is real but its orientation is wrong. The oppressed cry in pain but not toward God — not asking where their Maker is, not seeking his person. They want relief from the pressure, not relationship with God. The one who gives songs even in the night — who makes praise possible in the darkest hours (Ps 42:8; Acts 16:25) — goes unsought."
    },
    "11": {
      "L": "Who teacheth us more than the beasts of the earth, and maketh us wiser than the fowls of heaven?",
      "M": "Who teaches us more than the animals of the earth and makes us wiser than the birds of the sky?",
      "T": "The question points back to God as the source of human understanding. He is the one who gave human beings capacity above the animals — not through accumulated culture alone, but through divine instruction. To use that intelligence to cry anywhere but toward him is to misuse the greatest gift he gave."
    },
    "12": {
      "L": "There they cry, but none giveth answer, because of the pride of evil men.",
      "M": "There they cry, but he does not answer, because of the pride of evil people.",
      "T": "The prayer goes unanswered because the pride behind it blocks reception. It is not that God is indifferent to suffering. It is that the cry is launched from inside a posture of self-sufficiency that has not genuinely opened toward God. Pride is the acoustic barrier between the person crying and the one who could hear."
    },
    "13": {
      "L": "Surely God will not hear vanity, neither will the Almighty regard it.",
      "M": "Certainly God does not hear a hollow cry; the Almighty does not regard it.",
      "T": "An empty, misdirected, self-centered prayer — a cry that is really just noise from pain with no genuine seeking of God in it — is not what God answers. He hears differently: chapter 34 shows him hearing the cry of the afflicted who bring their case before him. But a shout into the void that is not really addressed to him receives silence back."
    },
    "14": {
      "L": "Although thou sayest thou seest him not, and the case is before him, and thou waitest for him —",
      "M": "How much less when you say you cannot see him, that the case is before him, and you must wait for him —",
      "T": "Job's own situation acknowledged: he says he cannot see God, that his case is laid before God, and that he waits for God to respond. Elihu hears even in this genuine posture the same problem. If the simple cries of the oppressed go unanswered because of pride, how much more is Job's sophisticated legal demand at risk of the same failure?"
    },
    "15": {
      "L": "But now, because his anger hath not visited and he taketh no great notice of sin —",
      "M": "But now, because God has not punished in his anger and does not take sharp notice of every transgression —",
      "T": "God's patience is being mistaken for indifference. Because punishment has not fallen immediately, because God has not made an example of every sin as it occurred, Job and others have drawn conclusions about what God notices or values. The very mercy of God's restraint has been misread as evidence of God's absence or unconcern."
    },
    "16": {
      "L": "Therefore doth Job open his mouth in vanity; without knowledge he multiplieth words.",
      "M": "So Job opens his mouth with empty words; he heaps up words without knowledge.",
      "T": "And this is why Job's words have come out as they have — many but empty. They arise from a place of misunderstanding about how God operates, not from a place of actually knowing God. The multiplying of words is not the same thing as the deepening of insight."
    }
  },

  # ============================================================
  # Chapter 36 — Elihu's Final Defense: God Teaches Through Suffering
  # ============================================================
  "36": {
    "1": {
      "L": "Elihu also proceeded and said:",
      "M": "Elihu continued and said:",
      "T": "Elihu is not done. This is his final address before the Yahweh speeches arrive."
    },
    "2": {
      "L": "Suffer me a little and I will show thee, for I have yet to speak on God's behalf.",
      "M": "Bear with me a little longer and I will show you, for I still have something to say in God's defense.",
      "T": "He asks for more patience. He is the last human voice before God himself speaks. He knows he has something important to complete, and he claims explicitly that he is speaking for God — a claim that will be interesting to hold in mind when God finally arrives and gives his own speech."
    },
    "3": {
      "L": "I will fetch my knowledge from afar and will ascribe righteousness to my Maker.",
      "M": "I will draw my knowledge from a wide range and ascribe righteousness to my Maker.",
      "T": "He will range far — not just received tradition but the full sweep of what can be known about God and the world. And his conclusion is already stated before the argument begins: righteousness belongs to the Maker. He is building a case for a conclusion he already holds."
    },
    "4": {
      "L": "For truly my words shall not be false; one perfect in knowledge is with you.",
      "M": "For truly my words are not false; one complete in knowledge stands before you.",
      "T": "A remarkable claim of authority. One 'perfect in knowledge' is speaking — whether Elihu means himself or claims some kind of divine endorsement is deliberately ambiguous. What is certain is that he believes he is right. What is also certain is that when God speaks next, he will not commend Elihu's words as he commends Job's."
    },
    "5": {
      "L": "Behold, God is mighty and despiseth not any; he is mighty in strength of understanding.",
      "M": "Behold, God is mighty and despises no one; he is mighty in strength of understanding.",
      "T": "Power without contempt. God does not look down on those he has made — not the weakest, not the most broken. His strength is not the strength of the powerful who diminish others to feel larger. He is great enough not to need to reduce anyone."
    },
    "6": {
      "L": "He preserveth not the life of the wicked, but giveth right to the poor.",
      "M": "He does not keep the wicked alive, but gives justice to the poor.",
      "T": "The alignment of God's power with the poor is stated without qualification. He will not protect wicked life — not because he is cruel but because wickedness is incompatible with the life he gives. And the poor, whose cry he heard in chapter 34, receive what is right from him."
    },
    "7": {
      "L": "He withdraweth not his eyes from the righteous; but with kings on the throne he doth establish them for ever, and they are exalted.",
      "M": "He does not take his eyes off the righteous; he seats them on the throne with kings and exalts them forever.",
      "T": "God's watchfulness over the righteous is not merely observational — it is actively promotional. He places the righteous among the powerful; he does not leave them crushed at the bottom while the wicked rise. The trajectory of the righteous, if not immediate, moves upward. Job's present position is not the final position."
    },
    "8": {
      "L": "And if they be bound in chains and be holden in cords of affliction —",
      "M": "And if they are bound in chains, caught in ropes of affliction —",
      "T": "But before the exaltation: the chains. The righteous can be bound — fettered in the cords of affliction. Elihu is not promising immunity from suffering; he is describing what God does with suffering when it comes. The chains are not the end of the story."
    },
    "9": {
      "L": "Then he sheweth them their work and their transgressions, that they have exceeded.",
      "M": "Then he shows them what they have done and their transgressions — that they have acted arrogantly.",
      "T": "In the chains, something is shown to them. Not punishment as final verdict but instruction about where they went wrong, what overstepping occurred. The affliction is a teaching moment — the one reading Elihu's theodicy finds here his most defensible point. Suffering as divine pedagogy rather than divine hostility is a real insight, even if its application to Job is misguided."
    },
    "10": {
      "L": "He openeth also their ear to discipline and commandeth that they return from iniquity.",
      "M": "He opens their ears to correction and commands that they turn from evil.",
      "T": "The ear opened. In ordinary life, the noise of comfort and activity makes it hard to hear. In affliction, when everything else has been stripped away, the ear clears. God uses the enforced stillness of suffering to get through what a busy life could not receive. The command is not to suffer more but to turn from what the suffering has revealed. This is the same theological structure as the exile-and-return framework of the Deuteronomic prophets (Hos 5:15)."
    },
    "11": {
      "L": "If they obey and serve him, they shall spend their days in prosperity and their years in pleasures.",
      "M": "If they listen and serve him, they will complete their days in prosperity and their years in comfort.",
      "T": "Obedience opens the door to the life that affliction temporarily closes. Days completed in prosperity, years lived in pleasantness — these are the outcome of genuine response to what suffering teaches. This is not an overnight guarantee; it is a direction, a trajectory opened by the turning."
    },
    "12": {
      "L": "But if they obey not, they shall perish by the sword and they shall die without knowledge.",
      "M": "But if they do not listen, they will perish by the sword and die without ever understanding.",
      "T": "The alternative is stark. Death by violence — and worse: death without understanding. To miss what the affliction was trying to teach, to die still demanding answers rather than receiving instruction, still not having turned — that is the deeper loss. The sword ends the body; dying without knowledge ends something harder to name."
    },
    "13": {
      "L": "But the hypocrites in heart heap up wrath; they cry not when he bindeth them.",
      "M": "The godless in heart store up resentment; they do not cry to God when he binds them.",
      "T": "The godless respond to affliction not with prayer but with accumulated anger. They do not cry to God when bound — they absorb the suffering into their resentment and harden against both the lesson and the teacher. And so the binding tightens, not because God is implacable but because the person has sealed themselves shut."
    },
    "14": {
      "L": "They die in youth and their life is among the unclean.",
      "M": "They die young, and their life ends among the cult prostitutes.",
      "T": "An early and degraded death. Dying young — before wisdom could accumulate, before the trajectory of obedience could open — and ending among the cult slaves whose lives were given over to degradation at pagan shrines. The godless do not just miss prosperity; they miss everything worth having, and what they reach instead is shameful."
    },
    "15": {
      "L": "He delivereth the poor in his affliction and openeth their ears in oppression.",
      "M": "But he rescues the afflicted person through their suffering and opens their ears through oppression.",
      "T": "The contrast with the godless is sharp. For the genuinely afflicted poor — those who cry to God, who have not sealed themselves against instruction — the oppression itself becomes the means of deliverance. The pressure that would crush the closed person opens the one who is receptive. This is Elihu's most profound insight: suffering is not proof of abandonment but can be the specific mechanism of rescue."
    },
    "16": {
      "L": "Even so would he have enticed thee out of a strait into a broad place, where there is no straitness; and that which is set on thy table should be full of fatness.",
      "M": "Indeed, he was drawing you from the jaws of distress into a broad place, free from pressure, where your table would be spread with rich food.",
      "T": "God's intention for Job, in Elihu's reading: a broad place — room, freedom, the release from the suffocating narrowness that extreme affliction produces. And abundance at the table. Elihu is describing what was available to Job if he had received the suffering as instruction rather than as injustice."
    },
    "17": {
      "L": "But thou art full of the judgment of the wicked; judgment and justice take hold of thee.",
      "M": "But now you are full of the judgment due the wicked; judgment and justice have seized you.",
      "T": "And instead of the broad place, Job is caught. Judgment has its grip. Not because God has turned against him out of spite, in Elihu's reading, but because Job's response to affliction has been the response of the wicked: defiant, self-justifying, charging God with injustice instead of receiving the lesson the affliction was sent to teach."
    },
    "18": {
      "L": "Because there is wrath, beware lest he take thee away with his stroke; then a great ransom cannot deliver thee.",
      "M": "Beware that anger does not lead you into scoffing; do not let the greatness of the required payment turn you away.",
      "T": "Two warnings in one verse. First: Job's anger at God risks becoming scoffing — the bitter, settled dismissal of God that closes every door. Second: when the ransom is eventually available — when what is needed to restore the broken relationship is offered — don't let its magnitude become an obstacle. Don't turn away from the price of restoration because it seems too high."
    },
    "19": {
      "L": "Will he esteem thy riches? No, nor all the forces of thy strength.",
      "M": "Will your wealth hold you in distress, or all the forces of your strength?",
      "T": "The resources Job might try to substitute for genuine turning: wealth, influence, the great power that made him who he was. Will any of it serve him here? None of it can purchase what only repentance and restored relationship can obtain."
    },
    "20": {
      "L": "Desire not the night when peoples are cut off in their place.",
      "M": "Do not long for the night, when people vanish from where they stand.",
      "T": "A warning against the dark wish. Job has in earlier chapters longed for death — for the night of non-existence, for escape through annihilation (Job 3:3-13; 7:15). Elihu warns against it. The night when people are cut off is not a solution; it is flight from what needs to be faced and turned from."
    },
    "21": {
      "L": "Take heed, regard not iniquity, for thou hast chosen this rather than affliction.",
      "M": "Be careful not to turn toward evil, for this is what you have been choosing over enduring affliction.",
      "T": "The choice set before Job: face the affliction as divine instruction and turn from whatever caused it — or turn toward evil as an alternative path. Elihu sees Job at that fork. The bitter words against God, the demands for vindication on Job's own terms — these are the first steps toward the wrong road."
    },
    "22": {
      "L": "Behold, God is exalted by his power; who is a teacher like him?",
      "M": "Behold, God is exalted in his power; who is a teacher like him?",
      "T": "And here the speech pivots — from warning to wonder. God's power is not just sovereign force; it is the power of the greatest teacher. No curriculum equals his. No pedagogy is as complete, as personalized, as persistently aimed at bringing people back. The suffering itself is the classroom."
    },
    "23": {
      "L": "Who hath enjoined him his way? Or who can say: Thou hast wrought iniquity?",
      "M": "Who has prescribed his path for him? Who can say, 'You have done wrong'?",
      "T": "The unanswerable questions: who tells God what to do? Who holds him to a standard above himself? No one mapped his course. No one has standing to say he went wrong. Job's attempt to convene a hearing in which God would be the defendant runs against this reality. The judge cannot be put on trial in his own court."
    },
    "24": {
      "L": "Remember that thou magnify his work, which men have sung of.",
      "M": "Remember to extol his work, which people have sung about through the ages.",
      "T": "Instead of charging God: praise him. The work of God — visible to every generation, sung about by human beings in every age — calls for magnification, not indictment. Job knows the hymns. He has sung them himself. Return to that posture before the accusations harden into something irreversible."
    },
    "25": {
      "L": "Every man hath seen it; man beholdeth it afar off.",
      "M": "All people have seen it; everyone looks at it from a distance.",
      "T": "The work is visible to all — seen from afar, which is the only vantage point any creature has relative to God's work. From that distance it is still magnificent. Understood from that distance it is still revelatory. The remove is not a failure of access; it is the condition of creaturely vision."
    },
    "26": {
      "L": "Behold, God is great and we know him not; the number of his years cannot be searched out.",
      "M": "Behold, God is great, beyond our knowing; the number of his years cannot be counted.",
      "T": "Genuine doxology arrives. God is great — not merely powerful-great, but great in the sense of exceeding any framework we build to contain him. We do not know him. Not adequately, not fully. The years of his existence cannot be numbered: he is not subject to the categories of time we use to measure everything else. Before this vastness, Job's demand for a scheduled court hearing in which God must appear starts to look different."
    },
    "27": {
      "L": "For he maketh small the drops of water; they distil rain according to the mist thereof —",
      "M": "For he draws up the drops of water; they distill as rain from the mist —",
      "T": "The nature hymn begins. God is involved in the specific mechanics of the water cycle: the evaporation of surface water into vapor, the collection of drops too small to see individually, the distillation back into rain. The smallest drop of water in the air is part of his working."
    },
    "28": {
      "L": "Which the clouds do drop and distil upon man abundantly.",
      "M": "which the clouds pour down and drop on people in abundance.",
      "T": "The rain reaches people. What God does in the invisible processes of the sky finds its way to the ground, to the humans below, who receive the abundance without seeing or understanding the mechanism. This is characteristic of how God works: the process is hidden; the gift is real and generous."
    },
    "29": {
      "L": "Also can any understand the spreadings of the clouds or the thunderings of his pavilion?",
      "M": "Can anyone understand the spreading of the clouds or the thunder from his canopy?",
      "T": "Can we understand? The question is genuine inquiry, not contemptuous dismissal. The motion and formation of clouds is beyond our comprehension even now, after centuries of meteorology. And the thunder — the booming voice from his pavilion, the heavenly dwelling place — announces what no human instrument can fully explain."
    },
    "30": {
      "L": "Behold, he spreadeth his light upon it and covereth the roots of the sea.",
      "M": "See, he scatters his lightning around him and covers the depths of the sea.",
      "T": "Lightning is God's light, scattered outward from himself. And below: the roots of the sea, the ocean depths where no human foot has gone, covered — known to him, belonging to him. The light above and the depth below are both in his domain."
    },
    "31": {
      "L": "For by these he judgeth the peoples; he giveth food in abundance.",
      "M": "For by these he governs peoples and provides food in abundance.",
      "T": "The natural processes Elihu has been describing are not merely spectacular. Rain and storm and the cycles of the sky are the mechanisms of governance and provision. God's sovereignty operates through what we call nature. By these, peoples are fed or judged."
    },
    "32": {
      "L": "With clouds he covereth the light; and he commandeth it, and it striketh the mark.",
      "M": "He covers his hands with the lightning and commands it to strike its mark.",
      "T": "God handles lightning with his hands — a startling, intimate image of sovereignty. The bolt that strikes a particular target does so under command, personally directed. The power in the storm is not mechanical but personal, wielded with precision."
    },
    "33": {
      "L": "The noise thereof telleth concerning it; the cattle also concerning the rising storm.",
      "M": "Its thunder announces his presence; the cattle also sense the coming storm.",
      "T": "The thunder is advance announcement — God declaring himself before the full arrival. Even the cattle feel it before human instruments detect it and respond accordingly. The whole creation is attuned to the voice of God in ways that humanity has largely lost. With this — nature bearing witness to its maker — Elihu's speech ends. The next voice will be God's own, covering the same ground from inside."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'job')
        merge_tier(existing, JOB, tier_key)
        save(tier_dir, 'job', existing)
    print('Job 34–36 written.')

if __name__ == '__main__':
    main()
