"""
MKT Proverbs chapters 4–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-proverbs-4-6.py

Translation decisions:

- H3068 (יהוה, YHWH): "LORD" (all caps) in L/M; "the LORD" in T. Maintained
  throughout the OT series.

- H2451 (חָכְמָה, chokmah): "wisdom" in all tiers. In ch 4 wisdom is personified in
  the T tier as in ch 1-3, but without the "Lady Wisdom" label (ch 4 uses second-person
  imperatives addressed to the son, not Wisdom's own speech).

- H3820 (לֵב, lev): "heart" in all tiers. The Hebrew lev is the seat of will, thought,
  and character — not mere emotion. T tier unpacks this where the context demands it
  (esp. 4:23, "guard your heart above all else").

- H7585 (שְׁאוֹל, Sheol): "Sheol" in L; "the grave" in M; "Sheol" / "realm of the dead"
  in T. Retaining the proper noun in L and T preserves the Hebrew cosmology where
  Sheol is the gathering place of the dead, not a vague "the grave."

- H2114 (זָרָה, zarah) / H5237 (נָכְרִיָּה, nokhriyah): "strange woman / forbidden woman"
  in L; "immoral woman / adulteress" in M; "the woman who will destroy you" in T.
  These terms denote the woman outside covenant relationship, not necessarily ethnically
  foreign. The T tier makes the destructive telos explicit.

- H5315 (נֶפֶשׁ, nephesh): "soul / life" depending on context. In 6:26, "precious soul"
  captures both senses — the man's life and the most valuable thing about him. In 6:32,
  "his own soul" (destroys his own soul).

- H1100 (בְּלִיַּעַל, beliyaal) in 6:12: "worthless man" in L; "scoundrel" in M; "man
  bent toward destruction" in T. Beliyaal in later texts becomes the demonic figure
  Belial; here it denotes total worthlessness / someone given over to destruction.

- H6102 (עָצֵל, atzel): "sluggard" in L/M; "the lazy one" in T. The satirical portrait
  in 6:6-11 contrasts the ant's self-directed industry with the sluggard's helpless
  inertia.

- H5244 (נְמָלָה, nemulah): "ant" in all tiers.

- H6148 (עָרַב, arab): "pledge / become surety" in L; "become surety" in M;
  "pledged your financial security" in T. The danger of becoming a financial guarantor
  for a neighbor's debt is a common wisdom theme (see also Prov 11:15; 17:18; 22:26-27).

- Proverbs 5:16 — Rendered as a rhetorical question ("Should your springs overflow
  in the streets?"), consistent with the NIV/ESV tradition and the structural logic of
  the passage: vv 15-17 form a unit counseling fidelity (v15 positive counsel, v16
  rhetorical reductio ad absurdum, v17 conclusion). The alternative (positive reading:
  "Let your children fill the streets") is possible but less coherent with the adultery
  warning context.

- Proverbs 6:16-19 — "Six things / yea seven" is the x, x+1 wisdom-numerical formula
  common to OT poetry (Amos 1-2; Job 5:19). The graduation emphasizes the final item
  (sowing discord among brothers) as the culmination. T tier notes this.

- Proverbs 6:26 — "nephesh yekarah" (precious soul/life): the adulteress hunts for what
  is most valuable about a man, his very life. The contrast with "a loaf of bread"
  (the price of a prostitute = you lose only money) is deliberate irony. T tier makes
  the horror of this explicit.

- Aspect notes: Most Proverbs sentences are gnomic present or general future, expressing
  timeless truths. Imperatives in ch 4 address the student directly; warnings in ch 5-6
  use imperfects for probable outcomes. L preserves the imperative force; M and T
  render in natural English present or future.

- OT echoes: Prov 4:18 ("path of the righteous like the dawn / shining to full day")
  echoes the creation of light in Gen 1 and is picked up in NT contexts as a figure
  of eschatological brightness. T tier notes the trajectory metaphor.

- Prov 4:23 ("guard your heart, for from it flow the springs of life") is the theological
  center of this section. The Hebrew "motzaei chayyim" (goings-forth / springs of life)
  treats the heart as the source from which all of life flows. T tier draws this out.
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
  "4": {
    "1": {
      "L": "Hear, O children, the instruction of a father, and give heed to know understanding;",
      "M": "Hear, my children, a father's instruction, and pay attention so that you may gain understanding,",
      "T": "Children, listen to what a father teaches — give it your full attention, because this is how understanding is gained."
    },
    "2": {
      "L": "For I give you good doctrine; forsake not my law.",
      "M": "For I give you sound teaching; do not abandon my instruction.",
      "T": "What I am giving you is reliable teaching — the real thing. Do not walk away from it."
    },
    "3": {
      "L": "For I was a son to my father, tender and an only one in the sight of my mother;",
      "M": "For when I was a son, tender in age and the only child in my mother's eyes,",
      "T": "I was once where you are — my father's son, young and cherished, the center of my mother's attention."
    },
    "4": {
      "L": "He taught me and said to me: 'Let your heart hold fast my words; keep my commandments and live.'",
      "M": "He taught me and said: 'Hold my words in your heart; keep my commands and you will live.'",
      "T": "My father taught me, and these are his words: 'Let what I tell you take hold of you — all the way down. Keep these commands, and you will live.'"
    },
    "5": {
      "L": "Get wisdom, get understanding; do not forget, nor turn from the words of my mouth.",
      "M": "Get wisdom, get understanding; do not forget or turn away from my words.",
      "T": "Pursue wisdom. Pursue understanding. Make them yours — and do not let them go. Do not drift from what I am telling you."
    },
    "6": {
      "L": "Do not forsake her and she will keep you; love her and she will guard you.",
      "M": "Do not abandon wisdom and she will protect you; love her and she will guard you.",
      "T": "Wisdom is loyal to those who stay with her. Love her and she becomes your protection — stay with her and she will not leave you."
    },
    "7": {
      "L": "The beginning of wisdom is this: get wisdom, and with all you acquire, get understanding.",
      "M": "Getting wisdom is the most important thing — so pursue wisdom; and along with everything else you acquire, gain understanding.",
      "T": "Here is the hierarchy: wisdom first, above everything else. Every resource you have — spend it in the pursuit of wisdom and understanding. Nothing you could acquire matters more."
    },
    "8": {
      "L": "Prize her and she will lift you up; embrace her and she will bring you to honor.",
      "M": "Honor her and she will honor you; embrace her and she will lift you up.",
      "T": "Give wisdom the highest place in your life and she will raise you up. Hold on to her and she will make you someone worth honoring."
    },
    "9": {
      "L": "She will place on your head a garland of grace; a crown of glory she will bestow on you.",
      "M": "She will give you a graceful wreath for your head and place a glorious crown on you.",
      "T": "Wisdom adorns her people — she puts a garland of grace on your head and sets a crown of glory there. These are honors she alone can give."
    },
    "10": {
      "L": "Hear, my son, and receive my sayings, and the years of your life will be many.",
      "M": "Listen, my son, accept my words, and the years of your life will be multiplied.",
      "T": "My son, hear me and take this in — wisdom is not just morally right, it is literally life-extending."
    },
    "11": {
      "L": "I have taught you in the way of wisdom; I have led you in right paths.",
      "M": "I have instructed you in the way of wisdom; I have guided you along straight paths.",
      "T": "I am not sending you out unprepared. I have shown you the road — straight paths, the way of wisdom. You already know the route."
    },
    "12": {
      "L": "When you walk, your steps will not be hampered; when you run, you will not stumble.",
      "M": "When you walk, your path will not be obstructed; when you run, you will not trip.",
      "T": "On wisdom's paths there is room to move. Walk them and you are not hemmed in; run them and you will not fall. The way ahead stays open."
    },
    "13": {
      "L": "Take hold of instruction; do not let her go; guard her, for she is your life.",
      "M": "Hold tightly to instruction; do not let her go — guard her, for she is your life.",
      "T": "Seize instruction and do not release it. This is not optional: instruction is your life. Let it go and you lose more than a lesson — you lose yourself."
    },
    "14": {
      "L": "Do not enter the path of the wicked, and do not go in the way of evil men.",
      "M": "Do not set foot on the path of the wicked or walk in the way of evil people.",
      "T": "The wicked have their own road. Do not even step onto it — not to explore, not out of curiosity. That road has a destination."
    },
    "15": {
      "L": "Avoid it; pass not by it; turn from it and pass on.",
      "M": "Shun it; do not travel it; turn away from it and keep going.",
      "T": "Avoid it entirely. Do not go near it. Turn, and keep walking the other way without looking back."
    },
    "16": {
      "L": "For they cannot sleep unless they do evil; their sleep is robbed from them unless they cause someone to fall.",
      "M": "They cannot sleep unless they have done wrong; their sleep is taken from them unless they have made someone stumble.",
      "T": "These people are wired for harm. They cannot rest until they have hurt someone — the very thing they need to unwind them is causing someone else's ruin. Evil is their rest."
    },
    "17": {
      "L": "For they eat the bread of wickedness and drink the wine of violence.",
      "M": "For they feed on wickedness and drink violence like wine.",
      "T": "Wickedness is their daily bread. Violence is what they drink. It has become sustenance — they cannot live without it."
    },
    "18": {
      "L": "But the path of the righteous is like the light of dawn, shining ever brighter until the full day.",
      "M": "The path of the righteous is like the light of dawn — it shines brighter and brighter until midday.",
      "T": "But the road of the just is like the first light of morning — it keeps growing clearer and brighter, more and more, until there is nothing but full day. This is the trajectory of a life shaped by wisdom: always brightening, never dimming."
    },
    "19": {
      "L": "The way of the wicked is as deep darkness; they do not know at what they stumble.",
      "M": "The way of the wicked is like deep darkness; they do not know what makes them fall.",
      "T": "The wicked walk in darkness so complete they do not even know what trips them. They fall, and they cannot say why. The darkness they chose has hidden their own obstacles from them."
    },
    "20": {
      "L": "My son, attend to my words; incline your ear to my sayings.",
      "M": "My son, pay attention to my words; turn your ear toward my teaching.",
      "T": "My son — stop. Come back to what I am saying. Lean in and listen."
    },
    "21": {
      "L": "Let them not depart from your eyes; keep them in the midst of your heart.",
      "M": "Do not lose sight of them; hold them at the center of your heart.",
      "T": "Keep these words always in view. Let them sit at the core of your inner life, where they can shape everything else."
    },
    "22": {
      "L": "For they are life to those who find them, and healing to all their flesh.",
      "M": "For they are life to those who discover them and health to their whole body.",
      "T": "These words are not merely advice — they are life itself. Find them and you find health, body and soul together."
    },
    "23": {
      "L": "Guard your heart with all diligence, for from it flow the springs of life.",
      "M": "Guard your heart above all else, for it is the source from which life flows.",
      "T": "Above everything else: guard your heart. The Hebrew heart is not just emotion — it is your will, your mind, the center of everything you are and do. Everything you are flows from it, the way a spring feeds a river. What the heart is, the life becomes."
    },
    "24": {
      "L": "Put away from you a crooked mouth, and keep devious lips far from you.",
      "M": "Rid yourself of corrupt speech; keep dishonest talk far from your lips.",
      "T": "Watch your words. Remove crooked speech from your life — twisted words, half-truths, language designed to deceive. Distance yourself from all of it."
    },
    "25": {
      "L": "Let your eyes look straight ahead, and let your gaze be fixed directly before you.",
      "M": "Let your eyes look forward, with your gaze fixed straight ahead.",
      "T": "Eyes forward. Keep your attention on the road in front of you — not scanning for the wrong things, not drifting toward what you should not be looking at."
    },
    "26": {
      "L": "Make level the path of your feet, and let all your ways be established.",
      "M": "Carefully consider the path you walk, and make all your ways steady.",
      "T": "Think before you step. Examine the road your feet are on and make sure it is solid — each step deliberate, each choice measured. Do not just wander; know where you are going."
    },
    "27": {
      "L": "Do not turn to the right hand or to the left; remove your foot from evil.",
      "M": "Do not swerve to the right or the left; keep your feet away from evil.",
      "T": "Do not drift — not right, not left. The road is straight; stay on it, and keep your feet well away from every form of evil."
    }
  },
  "5": {
    "1": {
      "L": "My son, give heed to my wisdom; incline your ear to my understanding,",
      "M": "My son, pay attention to my wisdom; turn your ear toward my understanding,",
      "T": "My son — what I am about to say requires your full attention. Lean in and listen carefully."
    },
    "2": {
      "L": "That you may preserve discretion and your lips may guard knowledge.",
      "M": "So that you will hold on to discernment and your lips will guard knowledge.",
      "T": "The goal is that discernment becomes truly yours — that what comes out of your mouth reflects what you actually know, not merely what you feel in the moment."
    },
    "3": {
      "L": "For the lips of a forbidden woman drip honey, and her speech is smoother than oil;",
      "M": "For the lips of the immoral woman drip honey, and her words are smoother than oil;",
      "T": "The woman who will destroy you speaks sweetly. Her words are honey at first — smooth as oil, easy to receive, impossible to resist."
    },
    "4": {
      "L": "But her end is bitter as wormwood, sharp as a two-edged sword.",
      "M": "But in the end she is as bitter as wormwood, as sharp as a two-edged sword.",
      "T": "But follow that sweetness and you will reach the end of it: bitter as poison, sharp as a blade cutting through you from both sides."
    },
    "5": {
      "L": "Her feet go down to death; her steps lay hold of Sheol.",
      "M": "Her feet go down to death; her steps lead straight to Sheol.",
      "T": "Watch her feet: they move toward death. Every step she takes is another step toward the realm of the dead. She is walking you there, and she calls it love."
    },
    "6": {
      "L": "She gives no thought to the path of life; her ways are unstable and she does not know it.",
      "M": "She does not consider the path of life; her ways wander and she does not realize it.",
      "T": "She has no idea where she is going, and she does not care. The path of life is not something she has ever considered. Her course shifts and wanders — and she brings you with her into the uncertainty."
    },
    "7": {
      "L": "And now, O sons, listen to me; do not depart from the words of my mouth.",
      "M": "So now, my sons, listen to me; do not turn away from what I am telling you.",
      "T": "I am speaking to you now, while there is still time to hear it. Do not turn away."
    },
    "8": {
      "L": "Keep your way far from her, and do not go near the door of her house,",
      "M": "Keep your road far from her; do not go near the door of her house,",
      "T": "Put real distance between yourself and her — not merely resistance in the moment, but a habitual, structural distance. Do not go near her door."
    },
    "9": {
      "L": "Lest you give your honor to others and your years to the merciless,",
      "M": "Or you will surrender your dignity to others and your prime years to those who are ruthless,",
      "T": "Follow her and you will hand over the best of yourself — your reputation, the years when you had the most to give — and they will belong to someone merciless who did not earn them."
    },
    "10": {
      "L": "And strangers be filled with your wealth, and your labors go to the house of a foreigner,",
      "M": "And strangers will consume your prosperity, and your hard work will end up in a foreigner's house,",
      "T": "What you built, what you earned, what you worked for — strangers will possess it. The fruit of your labor will fill another man's house."
    },
    "11": {
      "L": "And you groan at the last, when your flesh and your body are consumed,",
      "M": "And at the end you will groan when your body is wasted and your health is gone,",
      "T": "At the end of this road you will mourn — not quietly, but deeply — when your body has paid the price of every choice you made."
    },
    "12": {
      "L": "And say: 'How I hated discipline, and my heart despised correction!",
      "M": "And you will say: 'How I hated correction, and how my heart despised being rebuked!",
      "T": "And these are the words you will say: 'Why did I hate instruction? Why did everything in me resist correction?'"
    },
    "13": {
      "L": "I did not listen to the voice of my teachers, nor incline my ear to my instructors.",
      "M": "I would not heed the voice of my teachers or turn my ear toward those who instructed me.",
      "T": "I had teachers and I ignored them. I had people who tried to correct me and I turned away from every one of them. I had every opportunity to learn."
    },
    "14": {
      "L": "I was almost in utter ruin in the midst of the assembly and congregation.'",
      "M": "I was on the verge of complete ruin in the sight of the whole community.'",
      "T": "I came this close to total ruin — and it would have happened in public, in front of everyone, with nowhere to hide and no way to recover face."
    },
    "15": {
      "L": "Drink water from your own cistern, and running water from your own well.",
      "M": "Drink water from your own cistern and fresh water from your own well.",
      "T": "The positive counsel is this: drink from your own source. The intimacy and pleasure and life of marriage belong inside the covenant you made — not scattered to strangers."
    },
    "16": {
      "L": "Should your springs overflow in the streets, your streams of water in the public squares?",
      "M": "Should your springs be scattered in the streets, your streams of water in the public squares?",
      "T": "What belongs to your home should stay in your home. Would you really scatter the life of your household into the street for anyone to drink? Of course not."
    },
    "17": {
      "L": "Let them be yours alone, and not for strangers with you.",
      "M": "Let them be yours alone, not shared with strangers.",
      "T": "This belongs to you and to your wife — no one else. What is inside your home is not public property. Guard it."
    },
    "18": {
      "L": "Let your fountain be blessed, and rejoice in the wife of your youth.",
      "M": "May your source of life be blessed, and may you find joy with the wife of your youth.",
      "T": "The spring of your life — let it be blessed. Find your joy where it belongs: with the woman you married when you were young. She is still there."
    },
    "19": {
      "L": "A loving deer and a graceful doe — let her breasts satisfy you at all times; may you always be intoxicated with her love.",
      "M": "A loving deer, a graceful doe — may her love satisfy you completely at all times; may you always be captivated by her love.",
      "T": "She is your deer, your doe — beautiful, graceful, yours. Let her be all the satisfaction you need, now and always. Be captured by her love — there is enough there to last a lifetime, and it will not destroy you."
    },
    "20": {
      "L": "Why should you be intoxicated, my son, with a forbidden woman, or embrace the bosom of an outsider?",
      "M": "Why, my son, would you be captivated by an immoral woman or hold close a stranger?",
      "T": "Then why — why would you go looking elsewhere? Why let yourself be captured by a woman who is not yours? Everything you need is already in your own house."
    },
    "21": {
      "L": "For the ways of a man are before the eyes of the LORD, and he watches over all his paths.",
      "M": "For a man's ways are in plain sight before the LORD, and he examines every path he takes.",
      "T": "Nothing you do is hidden. The LORD sees every road you walk — every step, every detour, every decision made in the dark. He is not unaware, and he is not indifferent."
    },
    "22": {
      "L": "The iniquities of the wicked ensnare him, and he is held fast by the cords of his sin.",
      "M": "The wicked man is ensnared by his own iniquities and held fast by the ropes of his own sin.",
      "T": "Sin does not need outside punishment to do its work. A man's own wrongdoing catches him — the cords of his own choices wrap around him, tighter and tighter, until he cannot get free."
    },
    "23": {
      "L": "He dies for lack of instruction, and in the greatness of his folly he goes astray.",
      "M": "He dies for lack of discipline and is led astray by his immense foolishness.",
      "T": "In the end he dies not from bad luck but from refusing to be taught. His folly was not small — it was vast, all-consuming — and it drove him off course until there was no coming back."
    }
  },
  "6": {
    "1": {
      "L": "My son, if you have given your pledge for a neighbor, if you have struck your hand for a stranger,",
      "M": "My son, if you have become surety for your neighbor, if you have given your hand in a pledge for a stranger,",
      "T": "My son, if you have pledged your financial security for someone else — locked yourself into a guarantee with a stranger —"
    },
    "2": {
      "L": "You are caught by the words of your mouth, trapped by the words of your mouth.",
      "M": "You are snared by your own words; you are trapped by what you have said.",
      "T": "Your own words have become a trap. What came out of your mouth has shut around you like a snare — and it was your own hand that set it."
    },
    "3": {
      "L": "Do this now, my son, and deliver yourself, for you have come into your neighbor's hand: go, humble yourself and press your neighbor hard.",
      "M": "Do this at once, my son, and free yourself, since you have fallen into your neighbor's hand: go, humble yourself, and urgently plead with your neighbor.",
      "T": "Here is what you must do, and do it now: go to your neighbor, lay aside your pride entirely, and press him to release you. You are in his hands — humility is the only way out, and delay makes everything worse."
    },
    "4": {
      "L": "Give no sleep to your eyes, nor slumber to your eyelids.",
      "M": "Do not let your eyes sleep or your eyelids slumber.",
      "T": "Do not wait, do not sleep, do not rest — not until you have handled this. Tonight, if possible."
    },
    "5": {
      "L": "Deliver yourself like a gazelle from the hand of the hunter, like a bird from the hand of the fowler.",
      "M": "Save yourself like a gazelle escaping from the hunter's hand, like a bird from the hand of the trapper.",
      "T": "Act with the urgency of prey that has just sensed the hunter. A gazelle does not slow down to reconsider — it runs. A trapped bird does not negotiate — it escapes. Be like them."
    },
    "6": {
      "L": "Go to the ant, O sluggard; consider her ways and be wise.",
      "M": "Go to the ant, you sluggard; observe her ways and become wise.",
      "T": "You have no excuse — not even ignorance. Go look at the ant. Study what she does. Then be ashamed that something so small has more wisdom in it than you."
    },
    "7": {
      "L": "She has no commander, no officer, and no ruler,",
      "M": "With no commander, no overseer, and no master above her,",
      "T": "No one tells her what to do. No supervisor, no foreman, no authority watching over her shoulder —"
    },
    "8": {
      "L": "Yet she prepares her food in summer and gathers her provisions at harvest.",
      "M": "She stores her provisions in summer and gathers her food at harvest time.",
      "T": "And yet she works. She plans ahead. Summer is for preparation; harvest is for gathering. She does this not because someone made her, but because it is wise — and wisdom is all the motivation she needs."
    },
    "9": {
      "L": "How long will you lie there, O sluggard? When will you rise from your sleep?",
      "M": "How long will you lie there, you sluggard? When will you get up from your sleep?",
      "T": "How long? The ant has already been working for hours. When exactly do you intend to get up?"
    },
    "10": {
      "L": "A little sleep, a little slumber, a little folding of the hands to rest —",
      "M": "'A little sleep, a little slumber, a little folding of the hands to rest' —",
      "T": "The lazy person's inner voice: 'Just a little more sleep. Just a bit more rest. Just a moment more with my hands folded.' It always sounds reasonable. It never stops sounding reasonable."
    },
    "11": {
      "L": "And poverty will come upon you like a prowler, and want like an armed man.",
      "M": "And poverty will come on you like a thief and scarcity like an armed man.",
      "T": "But 'a little more' adds up, and then poverty arrives — not gently, not gradually, but the way a robber arrives. Suddenly, decisively, with force. By the time you see it coming it is already there."
    },
    "12": {
      "L": "A worthless man, a man of evil, goes about with a crooked mouth,",
      "M": "A scoundrel, a wicked man, goes about with corrupt speech;",
      "T": "There is a type worth recognizing — the scoundrel, the man whose very being bends toward destruction. His mouth is the first sign: crooked words, calculated deception, nothing said straight."
    },
    "13": {
      "L": "He winks with his eyes, signals with his feet, and points with his fingers;",
      "M": "He communicates with his eyes, shuffles his feet, and gestures with his fingers;",
      "T": "He signals what he really means without saying it — winks, gestures, a private language of innuendo. Nothing he communicates is honest. He has replaced language with theater."
    },
    "14": {
      "L": "With perverseness in his heart, he devises evil continually; he sows discord.",
      "M": "With a corrupt mind he constantly plots evil and stirs up conflict.",
      "T": "His heart is a workshop of harm. He plans it deliberately and continuously — and the end product is always the same: division, conflict, broken relationships. That is what he is for."
    },
    "15": {
      "L": "Therefore calamity will come upon him suddenly; in an instant he will be broken beyond healing.",
      "M": "Therefore disaster will strike him suddenly; in an instant he will be shattered beyond recovery.",
      "T": "The man who plants division will himself be destroyed — suddenly, totally, without warning. What he did to others will be done to him, and there will be no healing it."
    },
    "16": {
      "L": "There are six things the LORD hates, seven that are an abomination to his soul:",
      "M": "There are six things the LORD hates, and seven that are detestable to him:",
      "T": "Here is the LORD's own catalogue of what he finds intolerable — six things he hates, and one more that he cannot stomach at all. The graduated list is itself a warning: the final item is the worst."
    },
    "17": {
      "L": "Haughty eyes, a lying tongue, and hands that shed innocent blood,",
      "M": "Proud eyes, a lying tongue, and hands that kill the innocent,",
      "T": "Eyes that look down on everyone; a tongue built for deception; hands stained with innocent blood —"
    },
    "18": {
      "L": "A heart that devises wicked schemes, feet that hurry toward evil,",
      "M": "A mind that plots wicked plans and feet that run swiftly toward evil,",
      "T": "A mind that works overtime designing harm; feet that do not walk toward evil — they run, as if evil were a destination worth rushing to —"
    },
    "19": {
      "L": "A false witness who pours out lies, and one who sows discord among brothers.",
      "M": "A false witness who spreads lies, and a person who stirs up conflict among brothers.",
      "T": "A witness who lies and destroys someone with false testimony; and the one who takes a community of brothers — people who were bound together — and plants discord in the middle of it until they tear apart. This last one is what the LORD finds most intolerable of all."
    },
    "20": {
      "L": "My son, keep your father's commandment and do not forsake your mother's teaching.",
      "M": "My son, keep your father's command and do not abandon your mother's instruction.",
      "T": "My son, everything your father and mother taught you — keep it. The instruction came from two directions and it agrees: hold on to it."
    },
    "21": {
      "L": "Bind them on your heart continually; tie them about your neck.",
      "M": "Bind them to your heart at all times; fasten them around your neck.",
      "T": "These words belong on you, not filed away somewhere. Let them sit at the center of who you are; wear them where they are visible — they are not separate from your life, they are part of it."
    },
    "22": {
      "L": "When you walk, they will guide you; when you sleep, they will watch over you; when you awake, they will speak to you.",
      "M": "When you travel, they will guide you; when you sleep, they will guard you; and when you wake, they will speak to you.",
      "T": "These words become your companion across the whole of every day: traveling with you on the road, standing watch while you sleep, speaking first when you open your eyes in the morning. You are never without them."
    },
    "23": {
      "L": "For the commandment is a lamp and the teaching is a light, and the reproofs of instruction are the way of life,",
      "M": "For the command is a lamp and the teaching is a light, and the corrections of discipline are the pathway to life,",
      "T": "Here is why you must keep them: the commandment is a lamp in a dark place — and the teaching is the light itself. And every correction and rebuke you ever received? They were the pathway to life. The stinging word that felt like an attack was pointing you toward living."
    },
    "24": {
      "L": "Keeping you from the evil woman, from the smooth tongue of the adulterous woman.",
      "M": "To protect you from the immoral woman and from the flattering tongue of the adulteress.",
      "T": "All this wisdom, all this instruction — it is armor against a specific threat: the woman who will ruin you, whose tongue has been sharpened precisely to bring you down."
    },
    "25": {
      "L": "Do not desire her beauty in your heart, and do not let her capture you with her glancing eyes.",
      "M": "Do not desire her beauty in your heart, and do not be taken captive by her alluring eyes.",
      "T": "It begins in the heart, before any action. Do not let desire for her take root there. And do not let her eyes hold you — the attraction she uses is a weapon, designed to catch."
    },
    "26": {
      "L": "For a prostitute's price is only a loaf of bread, but a married woman hunts for a man's precious life.",
      "M": "For a prostitute reduces a man to a loaf of bread, but an adulteress preys on his very life.",
      "T": "The scale of the danger matters. What a prostitute costs you is money — you lose little more than a piece of bread. But the adulteress hunts something far more valuable: your life itself, the most precious thing about you. She will take it and not look back."
    },
    "27": {
      "L": "Can a man carry fire in his bosom and his clothes not be burned?",
      "M": "Can a man carry fire against his chest without his clothes catching fire?",
      "T": "The question answers itself: can you hold fire against your skin and not burn? Of course not."
    },
    "28": {
      "L": "Or can a man walk on hot coals and his feet not be scorched?",
      "M": "Can a person walk on hot coals without scorching his feet?",
      "T": "Can you walk across burning coals and not feel them? The answer is obvious — and so is what it means for you."
    },
    "29": {
      "L": "So is he who goes in to his neighbor's wife; none who touches her will go unpunished.",
      "M": "So it is with the man who sleeps with his neighbor's wife; no one who touches her will escape punishment.",
      "T": "The man who goes to another man's wife is doing exactly this — holding fire, walking on coals. No one who does it comes away unburned. Not one."
    },
    "30": {
      "L": "Men do not despise a thief who steals to satisfy himself when he is hungry.",
      "M": "People do not despise a thief who steals because he is starving.",
      "T": "Even for theft there is a kind of human understanding — a hungry man who steals to eat is pitiable. People can see the desperation behind it."
    },
    "31": {
      "L": "Yet if he is caught, he must repay sevenfold; he shall give all the wealth of his house.",
      "M": "But if he is caught, he must repay seven times over, giving up everything in his house.",
      "T": "But that understanding does not cancel the debt: caught, he still owes sevenfold — everything he has, his whole household's wealth. Sympathy and consequence are not the same thing."
    },
    "32": {
      "L": "He who commits adultery with a woman lacks sense; he who does it destroys himself.",
      "M": "But a man who commits adultery has no sense; whoever does it destroys his own life.",
      "T": "Adultery is not just wrong — it is stupid in the deepest sense. The adulterous man lacks the basic judgment to see what he is doing to himself. He is the agent of his own destruction, and no one forced him."
    },
    "33": {
      "L": "He will get wounds and dishonor, and his disgrace will not be wiped away.",
      "M": "He will suffer wounds and dishonor, and his shame will never be erased.",
      "T": "What he receives in return is wounds — physical, social, permanent. The shame that attaches to him will not come off. There is no reputation rehabilitation for this."
    },
    "34": {
      "L": "For jealousy makes a husband furious, and he will show no mercy when he takes revenge.",
      "M": "For jealousy enrages a husband, and he will show no mercy when he takes his revenge.",
      "T": "You are not just dealing with the woman — you are dealing with her husband, whose jealousy is a furnace. He will not be reasoned with, not be calmed down, not be bought off. When he comes for you, he will not hold back."
    },
    "35": {
      "L": "He will accept no ransom; he will refuse a bribe, however great it may be.",
      "M": "He will accept no compensation; he will refuse every bribe, no matter how large.",
      "T": "Money is no solution here. You cannot pay your way out. No ransom, no gift, no sum of money will satisfy him. This is the man you have made your enemy — and he will not rest."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'proverbs')
        merge_tier(existing, PROVERBS, tier_key)
        save(tier_dir, 'proverbs', existing)
    print('Proverbs 4–6 written.')

if __name__ == '__main__':
    main()
