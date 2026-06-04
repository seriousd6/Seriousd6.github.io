"""
MKT Jeremiah chapters 7–9 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-7-9.py

These chapters contain the Temple Sermon (ch. 7), the stork-and-migratory-bird oracle and
"balm in Gilead" lament (ch. 8), and the extended lament over universal treachery culminating
in the famous boasting passage (ch. 9).

Translation decisions (carried forward from mkt-jeremiah-4-6.py unless noted):
- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where personal-name force is
  significant — especially oracle-introduction formulas, direct-address, and divine-declaration
  ("Yahweh declares it") closings.
- H430 (אֱלֹהִים): "God" in all tiers throughout.
- H6635 (צְבָאוֹת): "LORD of hosts" in L/M; "Yahweh of Armies" in T — the military-divine
  register of these judgment oracles warrants the stronger rendering.
- H1697 (דָּבָר): "word" in all tiers — the prophetic-word formula is theologically load-bearing.
- H7965 (שָׁלוֹם): 8:11 (the peace-peace refrain, parallel to 6:14) — L/M: "Peace, peace";
  T: "All is well, all is well" — captures the false-optimism register per 4-6 decision.
- H7307 (רוּחַ): No clear divine-Spirit occurrence in these chapters; where it appears it is
  atmospheric. Rendered "wind" / "spirit" by context.
- H5315 (נֶפֶשׁ): 9:9 "shall not my soul be avenged" — divine self / desire for justice; T:
  "Shall I not exact justice." 8:18 "my sorrow is beyond healing / my heart is faint within me"
  — embodied inner experience; not metaphysical soul.
- H2617 (חֶסֶד): 9:24 — "steadfast love" (L), "steadfast love" (M), "covenant faithfulness" (T).
  This is the only occurrence in the range; the T rendering makes explicit the covenant dimension
  that is implicit in the Hebrew.
- H4941 (מִשְׁפָּט): 9:24 — "justice" in all tiers; here it is the comprehensive judicial-social
  sense of righteous ordering, not merely legal verdict.
- H8267 (שֶׁקֶר): "deceptive words / falsehood / lie" — the key term of ch. 7 (vv. 4, 8, 28)
  and ch. 9 (vv. 3, 5). Rendered "deceptive words" in v4 (phrase context), "lie/falsehood"
  elsewhere. T renders "the lie" in 7:4 to make the force of the warning explicit.
- H1964 (הֵיכָל): "temple/house" — the triple formula in 7:4 "temple of the LORD, temple of
  the LORD, temple of the LORD" is rendered verbatim in all tiers; it is the formula itself that
  Jeremiah mocks. KJV's "The temple of the LORD" is retained.
- H8612 (תֹּפֶת / Topheth): proper noun retained unchanged; note added to T regarding the
  cultic child-sacrifice site in Ben Hinnom / Gehenna.
- H4446 (מַלְכֶּת) / H8064 (שָׁמַיִם): 7:18 "queen of heaven" — the Akkadian Ishtar / Astarte
  cult; "queen of heaven" retained in all tiers as the standard English rendering.
- H7451 (רָעָה): "evil" for moral wickedness; "disaster/calamity" for divine judgment-event.
- H4878 (מְשׁוּבָה): "apostasy/backsliding" — 8:5 "perpetual apostasy"; T "habitual turning."
- H4997 + H4798 (נְאֻם יְהוָה): "declares the LORD" in L/M; "Yahweh declares" or "Yahweh
  declares it" in T when the phrase closes a statement of divine intent.
- 7:22-23 — Exegetical note: "I did not speak to your fathers… concerning burnt offerings"
  is Deuteronomic rhetoric emphasizing the primacy of covenant obedience over ritual. It does
  not mean Moses gave no sacrificial laws but that the foundational command was voice-obedience.
  T surfaces this rhetorical priority without flattening the force of the statement.
- 9:23-24 — Quoted by Paul in 1 Cor 1:31 and 2 Cor 10:17 ("let him who boasts, boast in the
  LORD"). T makes the contrast between the three broken boasts (wisdom / strength / riches) and
  the one true boast (knowing Yahweh's חֶסֶד, מִשְׁפָּט, צְדָקָה) structurally explicit.
- 9:25-26 — "Circumcised with the uncircumcised" / "uncircumcised in heart": anticipates Jer
  31:33 (new covenant, law written on the heart), Deut 30:6, and Paul's contrast in Rom 2:28-29.
  T makes the heart-circumcision dimension explicit since it is the climactic point of the passage.

OT echo and NT resonance notes:
- 7:11 "den of robbers" — quoted verbatim by Jesus in the Temple Cleansing (Matt 21:13; Mark
  11:17; Luke 19:46). This is one of the highest-frequency OT quotations in the Gospel narratives.
  T preserves "hideout for criminals" to keep the violence of the image.
- 7:12 — Shiloh's destruction is the historical warning: the ark's capture (1 Sam 4) and the
  abandonment of Shiloh by Yahweh. The sanctuary was no more permanent than the people's
  faithfulness. Ps 78:60 recalls it.
- 7:18 — Queen of heaven (Akkadian Ishtar/Astarte) cult — attested at Elephantine and across the
  ancient Near East. Jer 44 returns to this practice among the Egyptian diaspora.
- 7:31 — Topheth / Ben Hinnom = Gehenna in later Jewish and NT usage (Matt 5:22 etc.). The
  child-sacrifice site becomes the eschatological image of divine judgment.
- 8:7 — The migrating birds as metaphor for instinctive covenant knowledge: stork (H2624 חֲסִידָה
  "loyal/kind one") knows its season; my people do not know Yahweh's מִשְׁפָּטִים. The name of the
  stork itself (from חֶסֶד) may be an implied irony — the loyal bird knows loyalty; Israel does not.
- 8:11 — Parallel to 6:14; the "peace, peace" refrain becomes a recurring indictment of false
  prophecy throughout Jeremiah. NT echo: 1 Thess 5:3.
- 8:22 — "Balm in Gilead" — Gilead was famous for its aromatic resin used medicinally (Gen
  37:25; 43:11). The rhetorical question implies the answer is yes — balm exists, physicians
  exist — but healing has not come because the patient refuses treatment. T presses this.
- 9:1 — The MT numbers this as the last verse of ch. 8 (8:23 in LXX-order), but English
  Bibles follow the chapter division here. The verse marks the transition from communal oracle
  to prophetic lament (qinah). T preserves the lament register.
- 9:23-24 — The triad wisdom/strength/riches is the ancient Near Eastern catalogue of human
  resources. Yahweh's counter-triad חֶסֶד / מִשְׁפָּט / צְדָקָה (steadfast love / justice /
  righteousness) is his self-description as creator-covenant God. The passage is foundational
  for OT ethics. Paul cites it twice.

Structural notes:
  Ch. 7 — The Temple Sermon: condition and warning (vv. 1-15), intercession forbidden (vv. 16-20),
    sacrifice vs. obedience (vv. 21-28), lamentation commanded (v. 29), Topheth oracle (vv. 30-34).
  Ch. 8 — Judgment continued: desecration of graves (vv. 1-3), failure to return (vv. 4-7),
    false wisdom (vv. 8-12), communal lament (vv. 13-17), cry from afar (vv. 18-22).
  Ch. 9 — Treachery and lament: Jeremiah's wish to flee (vv. 1-6), refiner's fire (vv. 7-9),
    desolation lament (vv. 10-16), mourning women (vv. 17-22), the true boast (vv. 23-24),
    circumcision of the heart (vv. 25-26).

Aspect notes:
  7:13 "rising up early and speaking" — participial construction emphasizing habitual, repeated
    action. T: "again and again."
  8:6 "every one turns to his own course" — Qal participle: ongoing habitual action, not past.
  9:3 "they proceed from evil to evil" — Qal perfect with iterative sense; T: "they lurch."
  9:8 "he layeth his wait" — Qal participle: ongoing ambush posture, not single act.
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
            if v not in existing[ch]:
                existing[ch][v] = tiers[tier_key]

JEREMIAH = {
  "7": {
    "1": {
      "L": "The word that came to Jeremiah from the LORD, saying:",
      "M": "This is the word that came to Jeremiah from the LORD:",
      "T": "This is the word that came from Yahweh to Jeremiah:"
    },
    "2": {
      "L": "Stand in the gate of the LORD's house and proclaim there this word, and say: Hear the word of the LORD, all you of Judah who enter these gates to worship the LORD.",
      "M": "Stand at the gate of the LORD's house and proclaim this word there, and say: Hear the word of the LORD, all you of Judah who come through these gates to worship the LORD.",
      "T": "Take your stand at the gate of Yahweh's house and declare this word there: 'Hear the word of Yahweh, all you of Judah who pass through these gates to worship him.'"
    },
    "3": {
      "L": "Thus says the LORD of hosts, the God of Israel: Amend your ways and your deeds, and I will let you dwell in this place.",
      "M": "This is what the LORD of hosts, the God of Israel, says: Reform your ways and your actions, and I will let you live in this place.",
      "T": "Yahweh of Armies, the God of Israel, says this: Truly reform your ways and your deeds — and I will let you dwell in this land."
    },
    "4": {
      "L": "Do not trust in these deceptive words: 'The temple of the LORD, the temple of the LORD, the temple of the LORD are these.'",
      "M": "Do not trust in these deceptive words: 'This is the temple of the LORD, the temple of the LORD, the temple of the LORD!'",
      "T": "Stop trusting the lie — 'The temple of Yahweh! The temple of Yahweh! The temple of Yahweh!' — as if the building itself guaranteed your safety."
    },
    "5": {
      "L": "For if you truly amend your ways and your deeds, if you truly execute justice between a man and his neighbor,",
      "M": "For if you truly reform your ways and your actions, if you truly administer justice between one person and another,",
      "T": "Only if you truly reform your conduct — if you genuinely practice justice between one person and another —"
    },
    "6": {
      "L": "if you do not oppress the sojourner, the fatherless, or the widow, and do not shed innocent blood in this place, and if you do not go after other gods to your own harm,",
      "M": "if you do not exploit the foreigner, the fatherless, or the widow, or shed innocent blood in this place, and if you do not follow other gods to your own ruin —",
      "T": "if you stop exploiting the immigrant, the orphan, and the widow — stop shedding innocent blood in this place — stop chasing other gods to your own destruction —"
    },
    "7": {
      "L": "then I will let you dwell in this place, in the land that I gave to your fathers forever and ever.",
      "M": "then I will let you live in this place, in the land I gave your ancestors for ever and ever.",
      "T": "then I will let you remain in this land — the land I gave your ancestors as an everlasting possession."
    },
    "8": {
      "L": "Behold, you are trusting in deceptive words to no avail.",
      "M": "But look — you are trusting in deceptive words that can do you no good.",
      "T": "But the truth is this: you are placing your trust in a lie — words that accomplish nothing."
    },
    "9": {
      "L": "Will you steal, murder, commit adultery, swear falsely, make offerings to Baal, and walk after other gods that you have not known,",
      "M": "You steal, murder, commit adultery, swear falsely, sacrifice to Baal, and follow other gods you have never known —",
      "T": "You steal, you murder, you commit adultery, you swear false oaths, you burn offerings to Baal, you run after gods you have never even known —"
    },
    "10": {
      "L": "and then come and stand before me in this house that is called by my name, and say, 'We are delivered!' — only to go on doing all these abominations?",
      "M": "and then come and stand before me in this house that bears my name, and say, 'We are safe!' — and then go on doing all these detestable things?",
      "T": "and then walk in here and stand before me in this house that bears my name, crying, 'We are safe now!' — and then turn right back to all these very abominations?"
    },
    "11": {
      "L": "Has this house, which is called by my name, become a den of robbers in your eyes? Behold, I myself have seen it, declares the LORD.",
      "M": "Has this house, which bears my name, become a den of robbers in your eyes? I myself have seen it! declares the LORD.",
      "T": "Has this house — the house that bears my name — become a criminals' hideout in your eyes? Hear me: I have seen it with my own eyes. Yahweh declares it."
    },
    "12": {
      "L": "But go now to my place that was in Shiloh, where I caused my name to dwell at first, and see what I did to it because of the evil of my people Israel.",
      "M": "Go now to my place that was in Shiloh, where I first caused my name to dwell, and see what I did to it because of the wickedness of my people Israel.",
      "T": "Go to Shiloh — to the place where I first made my name dwell — and see with your own eyes what I did to it because of the evil of my people Israel."
    },
    "13": {
      "L": "And now, because you have done all these things, declares the LORD, and when I spoke to you, rising up early and speaking, you did not listen, and when I called you, you did not answer,",
      "M": "And now, since you have done all these things — declares the LORD — and though I spoke to you again and again you did not listen, and when I called you, you would not answer —",
      "T": "Now you have done all these things — Yahweh declares. I rose early and spoke, again and again. I called out to you. You would not listen. You would not answer."
    },
    "14": {
      "L": "therefore I will do to the house that is called by my name, and in which you trust, and to the place that I gave to you and to your fathers, as I did to Shiloh.",
      "M": "therefore I will do to this house that bears my name, and in which you trust, and to this place that I gave to you and your ancestors, exactly as I did to Shiloh.",
      "T": "So I will do to this house — the house that carries my name, the house you have trusted as your guarantee — what I did to Shiloh. I gave this place to you and your ancestors; I can take it back."
    },
    "15": {
      "L": "And I will cast you out of my sight, as I cast out all your kinsmen, all the offspring of Ephraim.",
      "M": "And I will drive you out of my presence, just as I drove out all your kinsmen — the entire offspring of Ephraim.",
      "T": "I will hurl you out of my sight, the same way I expelled all your northern kin — every last descendant of Ephraim."
    },
    "16": {
      "L": "As for you, do not pray for this people, or lift up a cry or prayer on their behalf, and do not intercede with me, for I will not hear you.",
      "M": "As for you, do not pray for this people, do not lift up a cry or prayer on their behalf, and do not press me with intercession — for I will not listen to you.",
      "T": "And you, Jeremiah — do not pray for this people. Do not raise a cry or a plea on their behalf. Do not intercede with me. I will not listen."
    },
    "17": {
      "L": "Do you not see what they are doing in the cities of Judah and in the streets of Jerusalem?",
      "M": "Do you not see what they are doing in the towns of Judah and in the streets of Jerusalem?",
      "T": "Don't you see it — what they are doing throughout Judah's towns and in every street of Jerusalem?"
    },
    "18": {
      "L": "The children gather wood, the fathers kindle fire, and the women knead dough, to make cakes for the queen of heaven; and they pour out drink offerings to other gods, to provoke me to anger.",
      "M": "The children gather wood, the fathers light the fire, and the women knead the dough to make cakes for the queen of heaven. And they pour out drink offerings to other gods to provoke me to anger.",
      "T": "Children gather the fuel, fathers light the fire, women knead the dough — all to bake offerings for the queen of heaven. And they pour out libations to foreign gods, as if they want to goad me into fury."
    },
    "19": {
      "L": "Is it I they are provoking? declares the LORD. Is it not themselves, to their own shame?",
      "M": "But is it really me they are provoking? declares the LORD. Is it not themselves they are provoking, bringing shame on themselves?",
      "T": "Is it me they are provoking? — Yahweh asks. No — they are provoking themselves, heaping shame upon their own heads."
    },
    "20": {
      "L": "Therefore thus says the Lord GOD: Behold, my anger and my wrath will be poured out on this place, on man and beast, on the trees of the field and the fruit of the ground; it will burn and not be quenched.",
      "M": "Therefore this is what the Lord GOD says: My anger and my wrath are about to be poured out on this place — on human and animal, on the trees of the field and the crops of the ground — and it will burn and will not be quenched.",
      "T": "Therefore this is what the Lord GOD declares: My anger and my fury are about to be poured out on this place — on human and animal alike, on the trees of the field and the produce of the land. It will burn, and no one will quench it."
    },
    "21": {
      "L": "Thus says the LORD of hosts, the God of Israel: Add your burnt offerings to your sacrifices and eat the flesh.",
      "M": "This is what the LORD of hosts, the God of Israel, says: Go ahead — add your burnt offerings to your other sacrifices and eat the meat yourselves.",
      "T": "Yahweh of Armies, the God of Israel, says this: Pile your burnt offerings onto your peace offerings and eat all the meat yourselves."
    },
    "22": {
      "L": "For in the day that I brought them out of the land of Egypt, I did not speak to your fathers or command them concerning burnt offerings and sacrifices.",
      "M": "For on the day I brought your ancestors out of Egypt, I did not speak with them or give them commands about burnt offerings and sacrifices.",
      "T": "Because on the day I brought your ancestors out of Egypt, burnt offerings were not my primary word to them. That ritual was not the foundational command."
    },
    "23": {
      "L": "But this command I gave them: 'Obey my voice, and I will be your God, and you shall be my people. Walk in all the way that I command you, that it may be well with you.'",
      "M": "Rather, I gave them this command: 'Obey me, and I will be your God, and you will be my people. Walk in all the ways I command you, so that it may go well with you.'",
      "T": "This was my foundational command: 'Listen to my voice. I will be your God; you will be my people. Walk in every way I have shown you — and it will go well with you.'"
    },
    "24": {
      "L": "But they did not listen or incline their ear, but walked in their own counsels and the stubbornness of their evil hearts, and went backward and not forward.",
      "M": "But they did not listen or pay attention; they followed their own plans, the stubbornness of their evil hearts. They turned their backs and went backward, not forward.",
      "T": "But they would not listen. They refused to pay attention. They followed the schemes of their own corrupt hearts — walking backward, away from me, not toward me."
    },
    "25": {
      "L": "From the day that your fathers came out of the land of Egypt to this day, I have sent all my servants the prophets to them, day by day, rising early and sending.",
      "M": "From the day your ancestors came out of Egypt until this very day, I have persistently sent all my servants the prophets to you — day after day, rising early to send them.",
      "T": "From the day your ancestors left Egypt until this very day, I have sent my servants the prophets — day after day, rising early to send them. And I have never stopped."
    },
    "26": {
      "L": "Yet they did not listen to me or incline their ear, but stiffened their neck; they did worse than their fathers.",
      "M": "Yet they did not listen to me or pay attention; they were stubborn and stiff-necked. They behaved even worse than their ancestors.",
      "T": "Still they would not listen. Still they refused to pay attention — making their necks rigid against me. And with each generation they grew worse than those before them."
    },
    "27": {
      "L": "You shall speak all these words to them, but they will not listen to you; you shall also call to them, but they will not answer you.",
      "M": "You will speak all these words to them, but they will not listen. You will call to them, but they will not respond.",
      "T": "Speak all these words to them — they will not hear you. Call out to them — they will not answer. This is the mission Yahweh has given you."
    },
    "28": {
      "L": "And you shall say to them: 'This is the nation that did not obey the voice of the LORD their God and did not accept discipline; truth has perished; it is cut off from their lips.'",
      "M": "You shall say to them: 'This is the nation that did not obey the LORD their God and refused to accept correction. Truth has vanished; it has disappeared from their lips.'",
      "T": "Then announce the verdict: 'This is a nation that would not obey Yahweh their God, would not accept correction. Truth has perished — it has been cut out of their mouths entirely.'"
    },
    "29": {
      "L": "Cut off your hair and cast it away; raise a lamentation on the bare heights, for the LORD has rejected and forsaken the generation of his wrath.",
      "M": "Shave off your hair and throw it away; raise a dirge on the hilltops, for the LORD has rejected and abandoned this generation under his wrath.",
      "T": "Shave your head and cast the hair to the wind. Lift a funeral wail on the bare hilltops — for Yahweh has rejected and abandoned this generation on whom his wrath has fallen."
    },
    "30": {
      "L": "For the sons of Judah have done evil in my sight, declares the LORD; they have set their abominations in the house that is called by my name, to defile it.",
      "M": "For the people of Judah have done evil in my sight, declares the LORD; they have installed their detestable idols in the house that bears my name, defiling it.",
      "T": "The people of Judah have done what is evil in my sight — Yahweh declares. They placed their vile idols in the very house that bears my name, polluting it to the core."
    },
    "31": {
      "L": "And they have built the high places of Topheth, which is in the Valley of the Son of Hinnom, to burn their sons and their daughters in the fire, which I did not command, nor did it come into my mind.",
      "M": "They have built the shrines of Topheth in the Valley of Ben Hinnom to burn their sons and daughters in the fire — something I never commanded, and something that never even entered my mind.",
      "T": "They built the high places of Topheth in the Valley of Ben Hinnom and burned their sons and daughters in the fire — something I never commanded, something that never even crossed my mind."
    },
    "32": {
      "L": "Therefore, behold, the days are coming, declares the LORD, when it will no more be called Topheth, or the Valley of the Son of Hinnom, but the Valley of Slaughter; for they will bury in Topheth, because there is no room elsewhere.",
      "M": "Therefore, the days are coming, declares the LORD, when this place will no longer be called Topheth or the Valley of Ben Hinnom, but the Valley of Slaughter — for they will bury the dead in Topheth until there is no room left.",
      "T": "Therefore, days are coming — Yahweh declares — when it will no longer be called Topheth, or the Valley of Ben Hinnom. It will be called the Valley of Slaughter. They will bury the bodies in Topheth until there is no more room."
    },
    "33": {
      "L": "And the dead bodies of this people will be food for the birds of the air and for the beasts of the earth; and none shall frighten them away.",
      "M": "The corpses of this people will become food for the birds of the sky and the wild animals of the earth, and no one will drive them away.",
      "T": "The bodies of this people will lie as carrion for the birds of the sky and the wild animals of the earth — and no one will be left to drive them off."
    },
    "34": {
      "L": "And I will silence in the cities of Judah and in the streets of Jerusalem the voice of mirth and the voice of gladness, the voice of the bridegroom and the voice of the bride; for the land shall become a waste.",
      "M": "I will bring to an end the sounds of joy and gladness, the voices of the bridegroom and the bride, in the cities of Judah and the streets of Jerusalem — for the land will become a wasteland.",
      "T": "I will silence every sound of joy and celebration from the cities of Judah and the streets of Jerusalem — the laughter of revelers, the songs of bridegroom and bride. The land will become a desolation."
    }
  },
  "8": {
    "1": {
      "L": "At that time, declares the LORD, they will bring out from their graves the bones of the kings of Judah, the bones of its princes, the bones of the priests, the bones of the prophets, and the bones of the inhabitants of Jerusalem.",
      "M": "At that time, declares the LORD, the bones of the kings of Judah, the bones of its officials, the bones of the priests, the bones of the prophets, and the bones of Jerusalem's inhabitants will be brought out of their graves.",
      "T": "At that time — Yahweh declares — they will drag the bones out of their graves: the bones of Judah's kings, their officials, the priests, the prophets, and the ordinary citizens of Jerusalem."
    },
    "2": {
      "L": "And they will spread them before the sun and the moon and all the host of heaven, which they have loved and which they have served and after which they have walked and which they have sought and which they have worshipped; they will not be gathered or buried; they will be as dung on the surface of the ground.",
      "M": "They will be exposed before the sun, the moon, and all the host of heaven — which this people loved, served, followed, consulted, and worshipped. The bones will not be gathered for burial; they will lie like dung spread on the ground.",
      "T": "Those bones will be spread out like dung before the sun, the moon, and all the starry host — the very gods they loved, served, followed, consulted, and worshipped. No one will gather them for burial. They will lie like refuse on the open ground."
    },
    "3": {
      "L": "Death shall be preferred to life by all the remnant that remains of this evil family, in all the places where I have driven them, declares the LORD of hosts.",
      "M": "And all the survivors of this evil family who remain in all the places where I have driven them will prefer death to life, declares the LORD of hosts.",
      "T": "Every survivor of this wicked family — scattered to every place where I have driven them — will choose death over life. Yahweh of Armies declares it."
    },
    "4": {
      "L": "Moreover you shall say to them: Thus says the LORD: When men fall, do they not rise again? When one turns away, does he not return?",
      "M": "Furthermore, say to them: This is what the LORD says: When people fall, don't they get back up? When someone turns away, don't they come back?",
      "T": "Say this to them: Here is what Yahweh says: When a man falls down, doesn't he get up? When someone wanders off the path, doesn't he turn back?"
    },
    "5": {
      "L": "Why then has this people, Jerusalem, turned away in perpetual apostasy? They hold fast to deceit; they refuse to return.",
      "M": "Then why has this people — Jerusalem — turned away in perpetual backsliding? They cling to deception and refuse to come back.",
      "T": "Then why has this people — Jerusalem — turned away in endless, habitual apostasy? They grip their delusion tight; they will not turn back."
    },
    "6": {
      "L": "I have paid attention and listened, but they did not speak aright; no one repents of his evil, saying, 'What have I done?' Everyone turns to his own course, like a horse that rushes headlong into battle.",
      "M": "I listened carefully, but they did not speak what is right. No one repents of his wickedness and asks, 'What have I done?' Each one charges ahead on his own course, like a horse plunging headlong into battle.",
      "T": "I listened carefully — but no one spoke honestly. No one stopped and asked, 'What have I done?' Everyone plunges ahead on their own course, like a warhorse charging into battle with no thought of turning."
    },
    "7": {
      "L": "Even the stork in the heavens knows her appointed times; the turtledove, the swallow, and the crane keep the time of their coming; but my people do not know the requirements of the LORD.",
      "M": "Even the stork in the sky knows when to migrate; the turtledove, the swallow, and the crane observe the season of their return — but my people do not know the requirements of the LORD.",
      "T": "Even the stork knows its season; the dove, the swallow, the crane — all observe their migration times by instinct. But my own people don't even know what Yahweh requires of them."
    },
    "8": {
      "L": "How do you say, 'We are wise, and the law of the LORD is with us'? But behold, the lying pen of the scribes has made it into a lie.",
      "M": "How can you claim, 'We are wise, and we have the law of the LORD'? But in fact the lying pen of the scribes has turned it into a lie.",
      "T": "You say, 'We are wise — we have Yahweh's law.' But look what the scribes' deceptive pens have done with it: they have turned the law itself into a lie."
    },
    "9": {
      "L": "The wise men shall be put to shame; they shall be dismayed and caught. Behold, they have rejected the word of the LORD, so what wisdom is in them?",
      "M": "The wise will be disgraced; they will be terrified and caught. They have rejected the word of the LORD — so what wisdom is left in them?",
      "T": "The wise will be shamed; they will be caught out and trapped. They threw away the word of Yahweh — so where is their wisdom now? It has come to nothing."
    },
    "10": {
      "L": "Therefore I will give their wives to others and their fields to conquerors, because from the least to the greatest everyone is greedy for unjust gain; from prophet to priest, everyone deals falsely.",
      "M": "Therefore I will give their wives to other men and their fields to new owners, because from the least to the greatest all are consumed by greed; from prophet to priest, all deal dishonestly.",
      "T": "So I will hand their wives over to others, their fields to new masters — because every one of them, from least to greatest, is driven by greed. Prophet and priest alike — every last one of them is a liar."
    },
    "11": {
      "L": "They have healed the wound of the daughter of my people lightly, saying, 'Peace, peace,' when there is no peace.",
      "M": "They dress the wound of my people as though it were minor, saying, 'Peace, peace,' when there is no peace.",
      "T": "They treat my people's gaping wound as if it were a scratch. 'All is well, all is well!' — but nothing is well."
    },
    "12": {
      "L": "Were they ashamed when they committed abomination? No, they were not at all ashamed; they did not know how to blush. Therefore they shall fall among the fallen; when I punish them, they shall be overthrown, says the LORD.",
      "M": "Were they ashamed when they committed these detestable acts? No, they felt no shame at all; they did not even know how to blush. So they will fall among the fallen; when the time of punishment comes, they will be brought down, says the LORD.",
      "T": "Did they feel any shame when they did these vile things? Not at all — they had forgotten how to blush. So they will fall with the fallen; when the hour of reckoning arrives, they will go down with the rest. Yahweh says it."
    },
    "13": {
      "L": "When I would gather them, declares the LORD, there are no grapes on the vine, no figs on the fig tree; even the leaves are withered, and what I gave them has passed from them.",
      "M": "I will take away their harvest, declares the LORD: no grapes on the vine, no figs on the fig tree, even the leaves will wither. What I gave them will be stripped away.",
      "T": "I will strip away what I gave them — Yahweh declares. No grapes left on the vine, no figs on the fig tree, even the leaves withered and gone. Everything I bestowed on them — taken back."
    },
    "14": {
      "L": "Why do we sit still? Gather together; let us go into the fortified cities and perish there, for the LORD our God has doomed us to perish and has given us poisoned water to drink, because we have sinned against the LORD.",
      "M": "Why are we sitting here? Come, let us flee to the fortified cities and die there — for the LORD our God has condemned us and has given us poisoned water to drink, because we have sinned against the LORD.",
      "T": "Why are we sitting still? Gather together and flee to the fortified cities — let us at least die there! For Yahweh our God has sentenced us, given us poison to drink. This is what our sin against Yahweh has brought."
    },
    "15": {
      "L": "We hoped for peace, but no good came; for a time of healing, but behold, terror.",
      "M": "We hoped for peace, but no good has come; we waited for a time of healing, but instead there is only terror.",
      "T": "We waited for peace — nothing came. We hoped for healing — and terror arrived in its place."
    },
    "16": {
      "L": "The snorting of their horses is heard from Dan; at the sound of the neighing of their stallions the whole land quakes. They have come and devoured the land and everything in it, the city and those who dwell in it.",
      "M": "From Dan the snorting of their warhorses is heard; the whole land shakes at the sound of their stallions' neighing. They have come to devour the land and all that fills it — every city and all its inhabitants.",
      "T": "From Dan comes the snorting of their warhorses; the neighing of their stallions makes the whole land tremble. They are coming to devour the land — everything in it — every city and every person."
    },
    "17": {
      "L": "For behold, I am sending among you serpents, adders that cannot be charmed, and they shall bite you, declares the LORD.",
      "M": "For I am about to send poisonous snakes among you — vipers that cannot be charmed — and they will bite you, declares the LORD.",
      "T": "For I am sending venomous snakes among you — serpents no charmer can control — and they will bite you. Yahweh declares it."
    },
    "18": {
      "L": "My grief is beyond healing; my heart is sick within me.",
      "M": "My sorrow is beyond healing; my heart is faint within me.",
      "T": "My sorrow is past all mending — my heart collapses within me."
    },
    "19": {
      "L": "Behold, the cry of the daughter of my people from a far country: 'Is the LORD not in Zion? Is her King not in her?' 'Why have they provoked me to anger with their carved images and with their foreign idols?'",
      "M": "Listen — the cry of my people from a distant land: 'Is the LORD not in Zion? Is her King no longer there?' — But: 'Why have they provoked me with their carved idols and worthless foreign gods?'",
      "T": "I hear it — the anguished cry of my people rising from a far country: 'Has Yahweh abandoned Zion? Is her King no longer there?' But the divine answer breaks in: 'Why did they provoke me with their carved images, their worthless foreign gods?'"
    },
    "20": {
      "L": "The harvest is past, the summer is ended, and we are not saved.",
      "M": "The harvest is over, the summer has ended — and we are still not saved.",
      "T": "The harvest has come and gone; summer has ended — and still we are not saved."
    },
    "21": {
      "L": "For the wound of the daughter of my people I am wounded; I mourn, and dismay has taken hold of me.",
      "M": "I am broken over the brokenness of my people; I mourn, and horror has gripped me.",
      "T": "My people are shattered — and I am shattered with them. Grief overwhelms me; horror has seized me by the heart."
    },
    "22": {
      "L": "Is there no balm in Gilead? Is there no physician there? Why then has the health of the daughter of my people not been restored?",
      "M": "Is there no balm in Gilead? Is there no physician there? Then why has the wound of my people not been healed?",
      "T": "Is there no healing resin in Gilead? Is there no physician there? The medicine exists — the healer exists — then why, why has my people's wound not healed?"
    }
  },
  "9": {
    "1": {
      "L": "Oh that my head were waters, and my eyes a fountain of tears, that I might weep day and night for the slain of the daughter of my people!",
      "M": "Oh that my head were a spring of water and my eyes a fountain of tears, so that I could weep day and night for the slain of my dear people!",
      "T": "If only my head were a spring and my eyes an endless fountain of tears — I would weep day and night for the fallen of my people."
    },
    "2": {
      "L": "Oh that I had in the desert a travelers' lodging place, that I might leave my people and go away from them! For they are all adulterers, a company of treacherous men.",
      "M": "Oh that I had a lodging place for travelers in the wilderness, so that I could leave my people and go away from them! For they are all adulterers, a gathering of traitors.",
      "T": "If only I could find a desert way-station — I would abandon my people and flee from them. They are all covenant-breakers, a congregation of betrayers."
    },
    "3": {
      "L": "They bend their tongue like their bow of falsehood; they have grown strong in the land; for they proceed from evil to evil, and they do not know me, declares the LORD.",
      "M": "They have bent their tongue like a bow to shoot falsehood; they have grown powerful in the land but not by truth. They go from one evil to the next, and they do not know me, declares the LORD.",
      "T": "They string their tongue like a bow, aimed with lies. Falsehood, not faithfulness, has grown dominant in this land. They lurch from one evil to the next — and still will not know me. Yahweh declares it."
    },
    "4": {
      "L": "Let everyone beware of his neighbor, and put no trust in any brother; for every brother is a deceiver, and every neighbor goes about as a slanderer.",
      "M": "Beware of your neighbors; put no trust in any relative — for every brother is a schemer, and every neighbor goes around spreading slander.",
      "T": "Don't trust your neighbor; don't rely on any kinsman — for every brother is out to trip you up, and every neighbor makes a living by slander."
    },
    "5": {
      "L": "Everyone deceives his neighbor, and no one speaks the truth; they have taught their tongue to speak lies; they weary themselves committing iniquity.",
      "M": "Everyone deceives his neighbor, and no one tells the truth. They have trained their tongue to lie; they exhaust themselves committing sin.",
      "T": "They deceive one another; no one speaks the truth. They have trained their tongues for lying — wearing themselves out in the practice of sin."
    },
    "6": {
      "L": "Your dwelling is in the midst of deceit; through deceit they refuse to know me, declares the LORD.",
      "M": "You live in the midst of deception; through their deceit they refuse to know me, declares the LORD.",
      "T": "You dwell inside a world of deception; through deception they have chosen not to know me. Yahweh declares it."
    },
    "7": {
      "L": "Therefore thus says the LORD of hosts: Behold, I will smelt them and test them, for what else can I do because of the daughter of my people?",
      "M": "Therefore this is what the LORD of hosts says: I will refine them and test them — for what else can I do with my sinful people?",
      "T": "Therefore Yahweh of Armies says this: I will put them through the refiner's fire and test them. What else can I do with my people?"
    },
    "8": {
      "L": "Their tongue is a deadly arrow; it speaks deceit. With his mouth each speaks peace to his neighbor, but in his heart he sets an ambush.",
      "M": "Their tongue is a lethal arrow that shoots out deceit. With their mouths they speak peace to their neighbors, but in their hearts they are planning an ambush.",
      "T": "Their tongue is a deadly arrow shot with deception. They speak peace to your face — but inside they are already setting the trap."
    },
    "9": {
      "L": "Shall I not punish them for these things? declares the LORD; and shall I not avenge myself on a nation such as this?",
      "M": "Should I not punish them for all this? declares the LORD. Should I not take vengeance on such a nation as this?",
      "T": "Shall I not call them to account for this? — Yahweh demands. Shall I not exact justice from a nation that behaves this way?"
    },
    "10": {
      "L": "I will take up weeping and wailing for the mountains, and a lamentation for the pastures of the wilderness, for they are laid waste so that no one passes through, and the lowing of cattle is not heard; both the birds of the air and the beasts have fled and are gone.",
      "M": "I will take up weeping and wailing for the mountains and lamentation for the wilderness pastures, for they have been laid waste so that no one passes through — no cattle low, the birds of the air and the wild animals have all fled and disappeared.",
      "T": "I lift up weeping and wailing for the mountains, a funeral lament for the wilderness pastures — they are scorched and empty. No one passes through; no cattle low; the birds have taken flight and the wild animals have fled. Nothing remains."
    },
    "11": {
      "L": "And I will make Jerusalem a heap of ruins, a lair of jackals; I will make the cities of Judah a desolation, without inhabitant.",
      "M": "I will make Jerusalem a heap of rubble, a haunt of jackals; I will make the cities of Judah a wasteland, with no one living in them.",
      "T": "I will turn Jerusalem into a rubble heap, a den for jackals. The cities of Judah I will make a wasteland, emptied of every living soul."
    },
    "12": {
      "L": "Who is the man so wise that he can understand this? And to whom has the mouth of the LORD spoken, that he may declare it? Why is the land ruined and laid waste like a wilderness, so that no one passes through?",
      "M": "Who is wise enough to understand this? Who has received the word from the LORD and can explain it? Why has the land been ruined and laid waste like a desert that no one crosses?",
      "T": "Who is wise enough to grasp this? Who has heard from Yahweh and can interpret it for others? Why has the land been devastated, turned into a desert that no one dares cross?"
    },
    "13": {
      "L": "And the LORD says: Because they have forsaken my law that I set before them, and have not obeyed my voice or walked in accord with it,",
      "M": "The LORD answered: Because they have abandoned my law that I placed before them, and have not obeyed my voice or followed it —",
      "T": "Yahweh answers: Because they abandoned my law — the instruction I set before them. They would not listen to my voice; they would not live by it."
    },
    "14": {
      "L": "but have stubbornly followed their own hearts and have gone after the Baals, as their fathers taught them —",
      "M": "Instead they followed the stubbornness of their own hearts and went after the Baals, just as their ancestors had taught them.",
      "T": "Instead they followed the stubbornness of their own hearts, pursuing the Baals — exactly as their fathers had taught them."
    },
    "15": {
      "L": "therefore thus says the LORD of hosts, the God of Israel: Behold, I will feed this people with wormwood and give them poisonous water to drink.",
      "M": "Therefore this is what the LORD of hosts, the God of Israel, says: I will feed this people with wormwood and give them poisoned water to drink.",
      "T": "Therefore Yahweh of Armies, the God of Israel, says this: I am about to feed this people on bitter wormwood and make them drink toxic water."
    },
    "16": {
      "L": "I will scatter them among the nations whom neither they nor their fathers have known; and I will send the sword after them until I have consumed them.",
      "M": "I will scatter them among nations that neither they nor their ancestors have known; and I will pursue them with the sword until I have consumed them.",
      "T": "I will scatter them among nations they have never known — not they nor their ancestors. And I will send the sword chasing after them until I have consumed every last one."
    },
    "17": {
      "L": "Thus says the LORD of hosts: Consider, and call for the mourning women to come; send for the skillful women to come;",
      "M": "This is what the LORD of hosts says: Consider this carefully; summon the professional mourning women to come; send for the most skilled among them to come.",
      "T": "Yahweh of Armies says: Think hard about this — and send for the mourning women. Call for the most skilled among them."
    },
    "18": {
      "L": "let them make haste and raise a wailing over us, that our eyes may run down with tears and our eyelids flow with water.",
      "M": "Let them come quickly and raise a lament over us, so that our eyes may stream with tears and our eyelids overflow with weeping.",
      "T": "Let them come quickly and lift up the funeral wail over us — so that our eyes run with tears and our eyelids pour down with weeping."
    },
    "19": {
      "L": "For a voice of wailing is heard from Zion: 'How we are ruined! We are greatly ashamed, because we have left the land, because they have thrown down our dwellings.'",
      "M": "For a cry of wailing is heard from Zion: 'We are devastated! We are utterly disgraced — because we have had to leave the land, because our homes have been torn down.'",
      "T": "For the sound of wailing is already rising from Zion: 'We are ruined! We are utterly shamed — because we were driven from the land, because our homes have been reduced to rubble.'"
    },
    "20": {
      "L": "Yet hear the word of the LORD, O women, and let your ear receive the word of his mouth; teach to your daughters a lament, and each to her neighbor a dirge.",
      "M": "Now, women, hear the word of the LORD; receive the word from his mouth. Teach your daughters to mourn; teach one another this dirge.",
      "T": "Women — hear the word of Yahweh! Let the word from his mouth reach your ears. Teach your daughters this lament; teach one another this song of mourning."
    },
    "21": {
      "L": "For death has come up through our windows; it has entered our palaces, cutting off children from the streets and young men from the public squares.",
      "M": "For death has climbed through our windows and entered our palaces, cutting down children in the streets and young men in the public squares.",
      "T": "For death has climbed through our windows; it has entered our palaces — cutting down children in the streets, young men in the open squares."
    },
    "22": {
      "L": "Speak thus, declares the LORD: 'The corpses of men shall fall like dung on the open field, like sheaves after the harvester, with none to gather them.'",
      "M": "This is what the LORD declares: 'Human corpses will fall like manure on the open field, like grain stalks left behind by the reaper, with no one to gather them up.'",
      "T": "This is what Yahweh declares: 'Bodies will fall like dung across the open field — like the cut stalks a reaper leaves behind, with no one to come and collect them.'"
    },
    "23": {
      "L": "Thus says the LORD: 'Let not the wise man boast in his wisdom, let not the mighty man boast in his might, let not the rich man boast in his riches,",
      "M": "This is what the LORD says: 'Let not the wise boast in their wisdom, nor the mighty in their strength, nor the rich in their wealth,",
      "T": "This is what Yahweh says: 'Don't let the wise crow about their wisdom. Don't let the strong crow about their strength. Don't let the wealthy crow about their riches."
    },
    "24": {
      "L": "but let him who boasts boast in this, that he understands and knows me, that I am the LORD who practices steadfast love, justice, and righteousness in the earth. For in these things I delight, declares the LORD.'",
      "M": "but let him who boasts boast in this: that he understands and knows me — that I am the LORD who exercises steadfast love, justice, and righteousness in the earth. For these are what I delight in, declares the LORD.'",
      "T": "If anyone wants to boast, let them boast in this alone: that they know me and understand who I am — Yahweh, who acts with covenant faithfulness, justice, and righteousness throughout the earth. These are what I delight in. Yahweh declares it.'"
    },
    "25": {
      "L": "Behold, the days are coming, declares the LORD, when I will punish all who are circumcised merely in the flesh —",
      "M": "The days are coming, declares the LORD, when I will punish all who are only outwardly circumcised —",
      "T": "The days are coming — Yahweh declares — when I will call to account all who are circumcised in body only:"
    },
    "26": {
      "L": "Egypt, Judah, Edom, the sons of Ammon, Moab, and all who dwell in the desert who cut the corners of their hair; for all these nations are uncircumcised, and all the house of Israel is uncircumcised in heart.",
      "M": "Egypt, Judah, Edom, Ammon, Moab, and all who live in the wilderness and clip the hair at their temples — for all these nations are physically uncircumcised, and all the house of Israel is uncircumcised in heart.",
      "T": "Egypt, Judah, Edom, Ammon, Moab, and all the desert peoples who shave the edges of their hair — these nations are uncircumcised in body, but all the house of Israel is uncircumcised in heart. The outer sign means nothing without the inner reality."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 7–9 written.')

if __name__ == '__main__':
    main()
