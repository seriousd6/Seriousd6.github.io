"""
MKT James chapters 1–2 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-james-1-2.py

Translation decisions:
- G3986 πειρασμός / G3985 πειράζω (trial/temptation): The same Greek root covers both
    external trials (1:2–4, 12) and internal enticements (1:13–14). In L: "trials" for
    the external sense, "tempted/temptation" for the internal. In M: same context-driven
    split. In T: "trials" (v2–4) and "desire pulling at you" (v13–14) — the inner and
    outer sources are distinguished explicitly. Mixing them would collapse a deliberate
    contrast James builds: God sends hardships to refine faith; God sends nothing to
    lure us into sin.
- G5281 ὑπομονή (endurance): "endurance" in L/M throughout — not "patience" (KJV).
    The word denotes active, sustained holding-under-load, not passive waiting. In T:
    "endurance that holds under pressure" (1:3) and "holds firm" (1:12) to surface the
    active quality.
- G4678 σοφία (wisdom, 1:5): "wisdom" in all tiers. The request for wisdom echoes
    Proverbs 2; James invites readers into the Wisdom tradition. In T the divine source
    and liberality are emphasized: "Ask God. He gives generously."
- G3056 λόγος (word, 1:18, 21–23, 25): "word" in all tiers — God's spoken truth that
    regenerates (1:18), can save (1:21), and must be acted on (1:22–23). Same Hebrews
    usage: not Greek philosophical Logos but Hebrew dabar, God's active word.
- G1343 δικαιοσύνη (righteousness, 1:20): "righteousness" in L/M; "what God's
    righteousness calls for" in T — human rage does not produce the right conduct and
    right relationship that God desires. Not a forensic term here; it is ethical.
- G4382 προσωπολημψία / G4380 προσωπολημπτέω (partiality/show favoritism): "partiality"
    (noun) / "show partiality" (verb) in all tiers. The compound literally means
    "receive a face" — judging by external appearance. In T: "play favorites" (2:1) and
    "divided people into classes" (2:4) to surface the social stratification dynamic.
- G4864 συναγωγή (assembly, 2:2): "assembly" in L — this is the only NT occurrence of
    συναγωγή used for a Christian gathering. Its presence signals an extremely early
    date or a deeply Jewish-Christian community. In M: "meeting"; in T: "assembly" —
    the Jewish-Christian texture is preserved rather than smoothed over.
- G1344 δικαιόω (justify/declared righteous, 2:21–25): "justified" in L; "considered
    righteous" in M; "shown to be in right standing" in T. James uses this in a
    demonstration sense (before human observers — cf. 2:18 "show me"); Paul uses it
    for the forensic declaration before God. They are compatible: James addresses
    the visible evidence of saving faith, Paul addresses its origin and ground. In T
    this distinction is surfaced so the Pauline tension does not mislead.
- G4102 πίστις (faith, throughout ch 2): "faith" in all tiers. In T for 2:14–26, the
    rendering makes clear that what James condemns is not genuine faith but a merely
    intellectual assent disconnected from any changed life — "dead faith" vs. "living
    faith."
- G2041 ἔργον (works/deeds, ch 2): "works" in L/M; "deeds" or "actions" in T to avoid
    the wooden ecclesiastical ring of "works" alone, while keeping the same concept.
- G3551 νόμος (law): "law" in all tiers. The "law of liberty" (1:25; 2:12) and "royal
    law" (2:8) are retained as-is — they are established phrases.
- G26 ἀγάπη / G25 ἀγαπάω (love, 2:8; "those who love him" 1:12; 2:5): "love" in all
    tiers — the royal law quotation (Lev 19:18) uses the verb; "those who love him"
    (1:12; 2:5) echoes covenant-loyalty language. No deviation from "love."
- G1391 δόξα (glory, 2:1 "Lord of glory"): "glory" in L/M; "glorious" in T for the
    genitive of quality. "The Lord of glory" = the glorious Lord.
- Aspect notes: 1:3 present participle κατεργάζεται — ongoing production ("produces"
    not "produced"). 1:15 sequence of aorist participles and verb: lust "conceiving" →
    "gives birth" → "having matured brings forth" — rendered as a completed progression.
    2:21 aorist ἀνήνεγκεν — a single completed act of offering. 2:22 imperfect
    συνήργει — "was working together" (ongoing cooperation of faith + deeds).
- OT intertextuality: 1:10–11 echoes Isa 40:6–7 (grass/flower fading). 1:12 "crown
    of life" echoes apocalyptic promise literature. 2:8 quotes Lev 19:18. 2:11 quotes
    Exod 20:13–14 (Decalogue order matches LXX). 2:21 refers to Gen 22:9–12. 2:23
    quotes Gen 15:6 and notes Abraham is called "friend of God" (cf. 2 Chr 20:7;
    Isa 41:8). 2:25 refers to Josh 2:1–21 (Rahab).
- 1:5 "without reproach" (ἁπλῶς καὶ μὴ ὀνειδίζοντος): "generously and without
    finding fault" in M; L preserves both adverb and participle. ἁπλῶς = "without
    fold/division" = single-mindedly, generously.
- 1:17 "Father of lights" (πατὴρ τῶν φώτων): the heavenly bodies, not light in
    general. God as creator of the luminaries (Gen 1:14–18). "Shadow of turning"
    (σκιὰ τροπῆς): astronomical — no parallax, no solstice-shift, no variability
    in the source of all good gifts. Retained as-is in L/M; unpacked in T.
- 1:18 "firstfruits" (ἀπαρχή): the advance offering that consecrates the whole
    harvest. In T: "the advance offering — of all his new creation" to surface the
    eschatological dimension.
- 2:7 "the noble name by which you were called": likely a reference to the name
    spoken at baptism (Christ/Jesus). In T: "the name of Christ that was spoken
    over you at your baptism."
- No LORD/Yahweh issue: James is NT Greek; θεός = "God" throughout.
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

JAMES = {
  "1": {
    "1": {
      "L": "James, a servant of God and of the Lord Jesus Christ, to the twelve tribes in the Dispersion: Greetings.",
      "M": "James, a servant of God and of the Lord Jesus Christ, to the twelve tribes scattered among the nations: Greetings.",
      "T": "From James — a slave bound to God and to the Lord Jesus Christ — to the twelve tribes of Israel living in exile among the nations: Peace to you."
    },
    "2": {
      "L": "Count it all joy, my brothers, whenever you fall into various trials,",
      "M": "Consider it pure joy, my brothers and sisters, whenever you face trials of many kinds,",
      "T": "Welcome it as nothing but joy, my brothers and sisters — even when you find yourselves caught in trials of every kind."
    },
    "3": {
      "L": "knowing that the testing of your faith produces endurance.",
      "M": "because you know that the testing of your faith produces endurance.",
      "T": "For you know this: when faith is tested, it forges endurance — the kind that holds under sustained pressure."
    },
    "4": {
      "L": "And let endurance have its perfect work, that you may be perfect and complete, lacking in nothing.",
      "M": "Let endurance complete its full work, so that you may be mature and complete, lacking nothing.",
      "T": "Give endurance room to do its full work in you, and you will come through complete and mature — with no weak places left."
    },
    "5": {
      "L": "And if any of you lacks wisdom, let him ask from God, who gives to all generously and without reproach, and it will be given to him.",
      "M": "If any of you lacks wisdom, let him ask God, who gives generously to all without finding fault, and it will be given to him.",
      "T": "Does any of you feel you lack wisdom? Ask God. He gives generously to everyone who asks and never utters a word of reproach — and he will give it."
    },
    "6": {
      "L": "But let him ask in faith, with no doubting; for the one who doubts is like a wave of the sea, driven and tossed by the wind.",
      "M": "But when you ask, you must believe and not doubt, for the one who doubts is like a wave of the sea, blown and tossed by the wind.",
      "T": "Only ask in faith, with no second-guessing — because the person who doubts is like a wave on the open sea, driven wherever the wind takes it."
    },
    "7": {
      "L": "For that person must not think that he will receive anything from the Lord;",
      "M": "For that person should not expect to receive anything from the Lord;",
      "T": "A person like that should not imagine the Lord will give him anything at all."
    },
    "8": {
      "L": "he is a double-minded man, unstable in all his ways.",
      "M": "he is a double-minded man, unstable in every way.",
      "T": "He is split down the middle — pulled two ways at once — and that instability runs through everything he does."
    },
    "9": {
      "L": "Let the lowly brother boast in his exaltation,",
      "M": "Let the believer in humble circumstances take pride in his high position,",
      "T": "The follower of Jesus who is poor in the world's eyes should boast in his true dignity before God —"
    },
    "10": {
      "L": "and the rich in his humiliation, because he will pass away like a flower of the grass.",
      "M": "but the one who is rich should take pride in his humiliation, because he will pass away like a wildflower.",
      "T": "and the one who is rich should take pride in being brought low — for wealth fades like a wildflower on the hillside."
    },
    "11": {
      "L": "For the sun rises with its scorching heat and withers the grass; its flower falls, and the beauty of its appearance perishes. So also will the rich man fade away in the midst of his pursuits.",
      "M": "For the sun rises with scorching heat and withers the plant; its blossom falls and its beauty is destroyed. In the same way, the rich man will fade away even while he goes about his business.",
      "T": "The sun comes up blazing and burns off the grass; the blossom drops and its beauty is gone. So the rich man — for all his busy striving — will wither away in mid-stride."
    },
    "12": {
      "L": "Blessed is the man who endures testing, for when he has stood the test he will receive the crown of life, which God has promised to those who love him.",
      "M": "Blessed is the man who perseveres under trial, because when he has stood the test he will receive the crown of life that God has promised to those who love him.",
      "T": "How fortunate is the person who holds firm under trial! Once proven, he will receive the victor's crown — the life that belongs to the age to come — which God has promised to everyone who loves him."
    },
    "13": {
      "L": "Let no one say when he is tempted, 'I am being tempted by God,' for God cannot be tempted with evil, and he himself tempts no one.",
      "M": "When tempted, no one should say, 'God is tempting me.' For God cannot be tempted by evil, nor does he tempt anyone;",
      "T": "When desire pulls at you, never say that God is the source of it. God is untouched by evil and draws no one toward it."
    },
    "14": {
      "L": "but each person is tempted when he is lured and enticed by his own desire.",
      "M": "but each person is tempted when they are drawn away by their own evil desire and enticed.",
      "T": "The source is always within: each of us is tempted when our own craving hooks us and drags us off course."
    },
    "15": {
      "L": "Then desire, having conceived, gives birth to sin; and sin, when it is fully grown, brings forth death.",
      "M": "Then, after desire has conceived, it gives birth to sin; and sin, when it is full-grown, gives birth to death.",
      "T": "Once desire conceives, it gives birth to sin. Once sin is fully grown, its own offspring is death."
    },
    "16": {
      "L": "Do not be deceived, my beloved brothers.",
      "M": "Do not be deceived, my dear brothers and sisters.",
      "T": "Do not let anyone mislead you here, my dear friends."
    },
    "17": {
      "L": "Every good gift and every perfect gift is from above, coming down from the Father of lights, with whom there is no variation or shadow of turning.",
      "M": "Every good and perfect gift is from above, coming down from the Father of the heavenly lights, who does not change like shifting shadows.",
      "T": "Every good thing given and every complete gift streams down from above — from the Father who made the lights of heaven, in whom there is no shadow, no shift, no variation of any kind."
    },
    "18": {
      "L": "Of his own will he brought us forth by the word of truth, that we should be a kind of firstfruits of his creatures.",
      "M": "He chose to give us birth through the word of truth, that we might be a kind of firstfruits of all he created.",
      "T": "By his own free choice he brought us into being through the word that is true — so that we would stand as the firstfruits, the advance offering, of all his new creation."
    },
    "19": {
      "L": "Know this, my beloved brothers: let every person be quick to hear, slow to speak, slow to anger;",
      "M": "My dear brothers and sisters, take note of this: everyone should be quick to listen, slow to speak and slow to become angry,",
      "T": "Mark this well, my dear friends: be quick to listen and slow to open your mouth — and let anger take a long time to arrive."
    },
    "20": {
      "L": "for the anger of man does not produce the righteousness of God.",
      "M": "because human anger does not produce the righteousness that God desires.",
      "T": "For human rage never brings about what God's righteousness calls for."
    },
    "21": {
      "L": "Therefore, putting away all filthiness and overflow of wickedness, receive with meekness the implanted word, which is able to save your souls.",
      "M": "Therefore, get rid of all moral filth and the evil that is so prevalent, and humbly accept the word planted in you, which can save you.",
      "T": "Strip off every kind of moral squalor and rank wickedness, and with open humility welcome the word that has been rooted in you — the word that has power to save your whole selves."
    },
    "22": {
      "L": "But be doers of the word, and not hearers only, deceiving yourselves.",
      "M": "Do not merely listen to the word, and so deceive yourselves. Do what it says.",
      "T": "Act on what the word says — do not merely take it in. Listening without doing is self-deception."
    },
    "23": {
      "L": "For if anyone is a hearer of the word and not a doer, he is like a man observing his natural face in a mirror.",
      "M": "Anyone who listens to the word but does not do what it says is like someone who looks at his face in a mirror",
      "T": "If you hear the word but do not act on it, you are like someone who glances at his own face in a mirror —"
    },
    "24": {
      "L": "for he looks at himself and goes away, and immediately forgets what kind of person he was.",
      "M": "and, after looking at himself, goes away and immediately forgets what he looks like.",
      "T": "looks, walks away, and within moments has forgotten what he saw."
    },
    "25": {
      "L": "But the one who looks into the perfect law, the law of liberty, and perseveres, not being a hearer who forgets but a doer who acts, he will be blessed in his doing.",
      "M": "But whoever looks intently into the perfect law that gives freedom, and continues in it — not forgetting what they have heard, but doing it — they will be blessed in what they do.",
      "T": "But the one who leans into the perfect law — the law of freedom — and keeps at it; the one who does not hear and forget but hears and acts: that person will find blessing in their obedience."
    },
    "26": {
      "L": "If anyone thinks he is religious and does not bridle his tongue but deceives his heart, this person's religion is worthless.",
      "M": "Those who consider themselves religious and yet do not keep a tight rein on their tongues deceive themselves, and their religion is worthless.",
      "T": "If someone thinks themselves devout but cannot govern their own tongue, they have only fooled themselves — whatever they call religion, it amounts to nothing."
    },
    "27": {
      "L": "Religion that is pure and undefiled before God the Father is this: to visit orphans and widows in their affliction, and to keep oneself unstained from the world.",
      "M": "Religion that God our Father accepts as pure and faultless is this: to look after orphans and widows in their distress and to keep oneself from being polluted by the world.",
      "T": "True devotion — the kind that God the Father calls pure and without spot — looks like this: coming to the aid of orphans and widows in their suffering, and keeping yourself uncorrupted by the world's influence."
    }
  },
  "2": {
    "1": {
      "L": "My brothers, show not partiality with the faith of our Lord Jesus Christ, the Lord of glory.",
      "M": "My brothers and sisters, believers in our glorious Lord Jesus Christ must not show favoritism.",
      "T": "Brothers and sisters, you cannot hold the faith of our glorious Lord Jesus Christ and at the same time play favorites."
    },
    "2": {
      "L": "For if a man enters your assembly with gold rings in fine clothing, and a poor man also enters in shabby clothing,",
      "M": "Suppose a man comes into your meeting wearing a gold ring and fine clothes, and a poor man in filthy old clothes also comes in.",
      "T": "Imagine two people walk into your assembly: one wearing a gold ring and fine clothes, the other dressed in rags."
    },
    "3": {
      "L": "and you pay attention to the one wearing the fine clothing and say, 'You sit here in a good seat,' but you say to the poor man, 'You stand there,' or, 'Sit at my feet,'",
      "M": "If you show special attention to the man wearing fine clothes and say, 'Here is a good seat for you,' but say to the poor man, 'You stand there' or 'Sit on the floor by my feet,'",
      "T": "If you fawn over the well-dressed one and offer the best seat, then turn to the poor person and say 'Stand over there' or 'Sit on the floor at my feet' —"
    },
    "4": {
      "L": "have you not made distinctions among yourselves and become judges with evil thoughts?",
      "M": "have you not discriminated among yourselves and become judges with evil thoughts?",
      "T": "have you not divided people into classes and set yourselves up as judges — driven by the worst kind of bias?"
    },
    "5": {
      "L": "Listen, my beloved brothers: has not God chosen the poor of the world to be rich in faith and heirs of the kingdom, which he has promised to those who love him?",
      "M": "Listen, my dear brothers and sisters: Has not God chosen those who are poor in the eyes of the world to be rich in faith and to inherit the kingdom he promised those who love him?",
      "T": "Pay close attention, dear friends: Has not God himself chosen those whom the world calls poor to be rich in faith — to inherit the kingdom he promised to those who love him?"
    },
    "6": {
      "L": "But you have dishonored the poor man. Are not the rich the ones who oppress you, and who drag you into court?",
      "M": "But you have dishonored the poor. Is it not the rich who are exploiting you? Are they not the ones who are dragging you into court?",
      "T": "And yet you humiliate the very people God has honored. It is the wealthy who exploit you and haul you before the judges —"
    },
    "7": {
      "L": "Do they not blaspheme the honorable name by which you were called?",
      "M": "Are they not the ones who are blaspheming the noble name of him to whom you belong?",
      "T": "— the same people who slander the name of Christ that was spoken over you at your baptism."
    },
    "8": {
      "L": "If you truly fulfill the royal law according to the Scripture, 'You shall love your neighbor as yourself,' you are doing well.",
      "M": "If you really keep the royal law found in Scripture — 'Love your neighbor as yourself' — you are doing right.",
      "T": "Now, if you genuinely keep the royal law — 'Love your neighbor as yourself' — you are doing exactly right."
    },
    "9": {
      "L": "But if you show partiality, you are committing sin and are convicted by the law as transgressors.",
      "M": "But if you show favoritism, you sin and are convicted by the law as lawbreakers.",
      "T": "But the moment you show partiality, you break the law. The law itself puts you on trial and pronounces you a transgressor."
    },
    "10": {
      "L": "For whoever keeps the whole law but stumbles in one point has become accountable for all of it.",
      "M": "For whoever keeps the whole law and yet stumbles at just one point is guilty of breaking all of it.",
      "T": "God's law is not a list of separate items — it is a whole. Break any single point and you have broken the law."
    },
    "11": {
      "L": "For he who said, 'Do not commit adultery,' also said, 'Do not murder.' If you do not commit adultery but do commit murder, you have become a transgressor of the law.",
      "M": "For he who said, 'You shall not commit adultery,' also said, 'You shall not murder.' If you do not commit adultery but do commit murder, you have become a lawbreaker.",
      "T": "The same lawgiver who said 'Do not commit adultery' also said 'Do not murder.' You may keep one and shatter the other — but the lawgiver's authority stands behind both commands, and you have broken his law."
    },
    "12": {
      "L": "So speak and so act as those who are to be judged by the law of liberty.",
      "M": "Speak and act as those who are going to be judged by the law that gives freedom,",
      "T": "Live and speak as people who will be judged by the law of freedom — the law that both liberates and holds you accountable."
    },
    "13": {
      "L": "for judgment is merciless to the one who has shown no mercy; mercy triumphs over judgment.",
      "M": "because judgment without mercy will be shown to anyone who has not been merciful. Mercy triumphs over judgment.",
      "T": "When the day of judgment comes, mercy will not be shown to those who showed none. But mercy wins — it stands in triumph over judgment."
    },
    "14": {
      "L": "What does it profit, my brothers, if someone says he has faith but does not have works? Can that faith save him?",
      "M": "What good is it, my brothers and sisters, if someone claims to have faith but has no deeds? Can such faith save them?",
      "T": "What use is it, my friends, for someone to claim faith while showing nothing by way of deeds? Can that kind of dead faith save anyone?"
    },
    "15": {
      "L": "If a brother or sister is poorly clothed and lacking in daily food,",
      "M": "Suppose a brother or a sister is without clothes and daily food.",
      "T": "Say a fellow believer — a brother or sister — is without clothes and going hungry."
    },
    "16": {
      "L": "and one of you says to them, 'Go in peace, be warmed and filled,' without giving them the things needed for the body, what does it profit?",
      "M": "If one of you says to them, 'Go in peace; keep warm and well fed,' but does nothing about their physical needs, what good is it?",
      "T": "If one of you says to them 'God bless you, stay warm, eat well' but hands them nothing — what good is the blessing?"
    },
    "17": {
      "L": "So also faith by itself, if it does not have works, is dead.",
      "M": "In the same way, faith by itself, if it is not accompanied by action, is dead.",
      "T": "Faith without deeds is exactly the same: dead on its own."
    },
    "18": {
      "L": "But someone will say, 'You have faith and I have works.' Show me your faith apart from your works, and I will show you my faith by my works.",
      "M": "But someone will say, 'You have faith; I have deeds.' Show me your faith without deeds, and I will show you my faith by my deeds.",
      "T": "Someone might argue: 'You have faith; I have deeds — two separate things.' Then show me this faith of yours with no deeds to back it up. I will show you mine by everything I do."
    },
    "19": {
      "L": "You believe that God is one. You do well. The demons also believe — and shudder.",
      "M": "You believe that there is one God. Good! Even the demons believe that — and shudder.",
      "T": "You say you believe in one God — fine. The demons believe that too. And they do not just believe; they tremble with terror."
    },
    "20": {
      "L": "Do you wish to know, O foolish man, that faith apart from works is useless?",
      "M": "You foolish person, do you want evidence that faith without deeds is useless?",
      "T": "Are you willing to be shown something, you empty-headed person? Faith cut off from deeds is barren — completely useless."
    },
    "21": {
      "L": "Was not Abraham our father justified by works when he offered up his son Isaac on the altar?",
      "M": "Was not our father Abraham considered righteous for what he did when he offered his son Isaac on the altar?",
      "T": "Consider Abraham, the father of our people: was he not shown to be in right standing with God precisely by his actions — when he laid his son Isaac on the altar?"
    },
    "22": {
      "L": "You see that faith was working together with his works, and by the works the faith was made perfect.",
      "M": "You see that his faith and his actions were working together, and his faith was made complete by what he did.",
      "T": "You see it plainly: his faith and his deeds worked as one. The deeds completed the faith — brought it to full expression."
    },
    "23": {
      "L": "And the Scripture was fulfilled that says, 'Abraham believed God, and it was counted to him as righteousness,' and he was called a friend of God.",
      "M": "And the scripture was fulfilled that says, 'Abraham believed God, and it was credited to him as righteousness,' and he was called God's friend.",
      "T": "The Scripture was thus proven true: 'Abraham trusted God, and it was counted as righteousness.' And he was given the title that tells us everything: Friend of God."
    },
    "24": {
      "L": "You see that a person is justified by works and not by faith alone.",
      "M": "You see that a person is considered righteous by what they do and not by faith alone.",
      "T": "The lesson is plain: a person is vindicated — shown to be in right standing — by their deeds, not merely by a declaration of belief."
    },
    "25": {
      "L": "And in the same way was not also Rahab the harlot justified by works when she received the messengers and sent them out by another way?",
      "M": "In the same way, was not even Rahab the prostitute considered righteous for what she did when she gave lodging to the spies and sent them off in a different direction?",
      "T": "Or take Rahab, known as a prostitute: was she not also vindicated by what she did — by sheltering the Israelite scouts and sending them safely away by another road?"
    },
    "26": {
      "L": "For just as the body apart from the spirit is dead, so also faith apart from works is dead.",
      "M": "As the body without the spirit is dead, so faith without deeds is dead.",
      "T": "A body without breath in it is a corpse. Faith without action is no different — it is dead."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'james')
        merge_tier(existing, JAMES, tier_key)
        save(tier_dir, 'james', existing)
    print('James 1–2 written.')

if __name__ == '__main__':
    main()
