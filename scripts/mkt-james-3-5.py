"""
MKT James chapters 3–5 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-james-3-5.py

Translation decisions:
- G4678 (σοφία): "wisdom" (L/M/T) — James contrasts two kinds of wisdom explicitly (3:13–17); the
  earthly/demonic counterfeit vs. the pure wisdom from above. Capitalisation not used; context makes
  the distinction clear. T tier spells out the contrast.
- G3056 (λόγος): "word" (L/M/T) — in 3:2 purely contextual ("offend not in word/speech"); no
  Johannine resonance here; M/T use "speech" where it reads more naturally.
- G4151 (πνεῦμα): "spirit" lowercase (L/M), "Spirit" (T 4:5) — Jam 4:5 is textually difficult;
  the referent is debated (human spirit God placed in us vs. the Holy Spirit). L preserves the
  ambiguity with lowercase; T reads it as God's Spirit based on the divine-jealousy framing.
- G2962 (κύριος): "Lord" (L/M/T) — throughout chs 3–5 refers to Christ whose return is awaited
  (5:7–8); small-caps convention not available in plain text; uppercase "Lord" used throughout.
- G1577 (ἐκκλησία): "assembly" (L), "church" (M/T) — choosing "church" for M/T as the term is
  already established in Acts and Epistles contexts; L preserves the assembly sense.
- G1343 (δικαιοσύνη): "righteousness" (L/M), "righteous life / righteousness" (T) — 3:18 "fruit
  of righteousness sown in peace" keeps standard rendering; T unpacks the harvest metaphor.
- G5590 (ψυχή): "soul" (L), "soul/life" (M/T) — 5:20 "save a soul from death"; the whole person
  is in view, not merely an immaterial component; T uses "soul" but acknowledges the embodied sense.
- G4561 (σάρξ): "flesh" (L/M), "body" (T 5:3) — in 5:3 the corroded wealth eating "flesh as fire"
  is a judgment metaphor; T renders it "bodies" for vividness.
- G3114 (μακροθυμέω): "be patient / have long patience" (L), "be patient" (M), "wait patiently /
  patient endurance" (T) — eschatological patience awaiting the Lord; aspect is ongoing.
- Jam 4:5 quotation: the source of this "scripture" is unknown; it does not correspond to a known
  OT verse verbatim. Handled in T with a note-style rendering explaining the allusion.
- Textual note Jam 5:12: matches the tradition behind Matt 5:37 (let your yes be yes); T draws
  out the connection to integrity of speech without a cross-reference note in the text itself.
- Aorist aspect in 5:1–6 (prophetic denunciation of the rich): the aorists ("you have condemned,"
  "you have stored up") are prophetic perfects—treating future judgment as accomplished. T surfaces
  this by using present-perfect English where it captures the rhetorical force.
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
  "3": {
    "1": {
      "L": "Not many of you become teachers, my brothers, knowing that we will receive a greater judgment.",
      "M": "Not many of you should become teachers, my brothers, for you know that we who teach will be judged more strictly.",
      "T": "Think carefully before you take on the teacher's role, brothers—those who stand before others to instruct will face a stricter accounting before God."
    },
    "2": {
      "L": "For in many things we all stumble. If anyone stumbles not in word, this one is a perfect man, able also to bridle the whole body.",
      "M": "For we all stumble in many ways. If anyone does not stumble in what he says, he is a perfect person, able also to control his whole body.",
      "T": "We all make many mistakes. But if someone could perfectly control every word they speak, they would have mastered themselves entirely—the person who never missteps with the tongue can govern their whole being."
    },
    "3": {
      "L": "Behold, we put bits into the mouths of horses so that they obey us, and we guide their whole body.",
      "M": "When we put bits into the mouths of horses to make them obey us, we guide their whole bodies.",
      "T": "Think of it this way: a small metal bit placed in a horse's mouth gives the rider command over the entire animal."
    },
    "4": {
      "L": "Behold also the ships, though they are so great and driven by fierce winds, they are guided by a very small helm whithersoever the pilot desires.",
      "M": "Look also at ships: though they are so large and driven by fierce winds, they are steered by a very small rudder wherever the pilot chooses.",
      "T": "Or consider ocean-going ships—massive hulls battered by gales, yet a tiny rudder turns the whole vessel wherever the helmsman decides to go."
    },
    "5": {
      "L": "So also the tongue is a little member and boasts great things. Behold, how great a forest a small fire sets ablaze!",
      "M": "So also the tongue is a small member, yet it makes great boasts. Consider how great a forest a small fire can set ablaze!",
      "T": "The tongue works the same way: a small limb, yet its claims are enormous. And consider how much a single spark can destroy—an entire forest reduced to ash."
    },
    "6": {
      "L": "And the tongue is a fire, a world of iniquity. The tongue is set among our members, defiling the whole body and setting on fire the course of life, and is itself set on fire by hell.",
      "M": "And the tongue is a fire, a world of unrighteousness. The tongue is placed among our members, defiling the whole body, setting fire to the whole course of life, and is itself set on fire by hell.",
      "T": "The tongue is fire—a whole cosmos of wickedness packed into one small member. It corrupts the entire person; it ignites the whole sweep of human existence; and the flame that burns in it was lit in Gehenna itself."
    },
    "7": {
      "L": "For every kind of beast and bird, of reptile and sea creature, is tamed and has been tamed by humanity.",
      "M": "For every kind of animal—beasts, birds, reptiles, and sea creatures—has been tamed and can be tamed by humanity.",
      "T": "Humanity has subdued every creature on earth: wild beasts, birds of the air, crawling things, and the creatures of the sea."
    },
    "8": {
      "L": "But the tongue no one is able to tame—a restless evil, full of deadly poison.",
      "M": "But no human being can tame the tongue. It is a restless evil, full of deadly poison.",
      "T": "But the tongue? No one can tame it. It is a restless, untameable evil loaded with lethal venom."
    },
    "9": {
      "L": "With it we bless the Lord and Father, and with it we curse men, who have been made in the likeness of God.",
      "M": "With it we bless the Lord and Father, and with it we curse people who have been made in the likeness of God.",
      "T": "We use the very same tongue to bless God our Father and to curse the people he made in his own image."
    },
    "10": {
      "L": "Out of the same mouth come forth blessing and cursing. My brothers, these things ought not to be so.",
      "M": "From the same mouth come blessing and cursing. My brothers, this should not be.",
      "T": "Praise and curses pour from the same mouth. Brothers, this simply must not be."
    },
    "11": {
      "L": "Does a spring from the same opening pour forth fresh and bitter water?",
      "M": "Does a spring pour forth from the same opening both fresh and bitter water?",
      "T": "No spring sends up both sweet and bitter water from the same source."
    },
    "12": {
      "L": "Can a fig tree, my brothers, produce olives, or a vine figs? Neither can salt water yield fresh.",
      "M": "My brothers, can a fig tree bear olives, or a grapevine bear figs? Neither can a salt spring produce fresh water.",
      "T": "A fig tree cannot bear olives, brothers. A vine does not grow figs. And a salt spring cannot give fresh water. The mouth is no different."
    },
    "13": {
      "L": "Who is wise and understanding among you? Let him show by his good conduct his works in meekness of wisdom.",
      "M": "Who among you is wise and understanding? Let him show it by his good way of life, by works done in the humility that comes from wisdom.",
      "T": "Is any of you truly wise? Prove it not by argument but by the quality of your daily life—deeds carried out with the quiet confidence that genuine wisdom produces."
    },
    "14": {
      "L": "But if you have bitter jealousy and selfish ambition in your hearts, do not boast and lie against the truth.",
      "M": "But if you harbor bitter jealousy and selfish ambition in your hearts, do not boast about it and lie against the truth.",
      "T": "But if your heart is eaten up with bitter envy and the drive to get ahead at others' expense, do not pretend to wisdom—you would only be lying against the truth."
    },
    "15": {
      "L": "This wisdom is not that coming down from above, but is earthly, soulish, demonic.",
      "M": "Such wisdom does not come down from above, but is earthly, unspiritual, and demonic.",
      "T": "That kind of 'wisdom' has nothing heavenly about it—it belongs to the earth, to the merely human, to the demonic."
    },
    "16": {
      "L": "For where jealousy and selfish ambition are, there is disorder and every vile practice.",
      "M": "For where jealousy and selfish ambition exist, there is disorder and every kind of evil practice.",
      "T": "Wherever envy and self-seeking ambition take root, chaos follows—and every form of wickedness flourishes alongside them."
    },
    "17": {
      "L": "But the wisdom that is from above is first pure, then peaceable, gentle, reasonable, full of mercy and good fruits, undivided, without hypocrisy.",
      "M": "But the wisdom from above is first pure, then peaceable, gentle, open to reason, full of mercy and good fruits, impartial and sincere.",
      "T": "Wisdom from above is another thing entirely. It is, first of all, pure—and from that purity flows a peaceableness, a gentleness, a willingness to listen and yield, a life overflowing with mercy and tangible good, an evenhandedness toward all people, and a complete absence of pretense."
    },
    "18": {
      "L": "And the fruit of righteousness is sown in peace for those who make peace.",
      "M": "And a harvest of righteousness is sown in peace by those who make peace.",
      "T": "Those who work to make peace are planting seeds—and the harvest that grows from that sowing is a life of righteousness."
    }
  },
  "4": {
    "1": {
      "L": "From where do wars and fightings among you come? Is it not from this—your pleasures that war in your members?",
      "M": "What causes quarrels and conflicts among you? Is it not your passions that are at war within you?",
      "T": "Where do the wars and fights that tear your community apart come from? Look inside—they come from the cravings that wage their own war within each of you."
    },
    "2": {
      "L": "You desire and do not have; you murder and covet and cannot obtain; you fight and make war. You have not because you ask not.",
      "M": "You desire and do not have, so you murder. You covet and cannot obtain, so you fight and quarrel. You do not have because you do not ask God.",
      "T": "You crave what you don't have—and so you trample others. You hunger for more—and when you can't get it, you go to war. You remain empty-handed simply because you never ask God."
    },
    "3": {
      "L": "You ask and do not receive, because you ask wrongly, to spend it on your pleasures.",
      "M": "You ask and do not receive, because you ask wrongly—wanting to spend it on your own pleasures.",
      "T": "And when you do ask, your request is refused—because your motive is self-gratification, not God's purposes."
    },
    "4": {
      "L": "Adulteresses! Do you not know that friendship with the world is enmity with God? Therefore whoever wishes to be a friend of the world makes himself an enemy of God.",
      "M": "You adulterous people! Do you not know that friendship with the world is hostility toward God? Therefore, whoever wants to be a friend of the world makes himself an enemy of God.",
      "T": "You have been unfaithful—like a spouse who runs after a rival. Don't you understand that loving what the world loves means standing against what God loves? Whoever chooses the world as their closest companion has chosen to stand against God."
    },
    "5": {
      "L": "Or do you think that the scripture speaks in vain? 'The Spirit he caused to dwell in us yearns jealously.'",
      "M": "Or do you think Scripture speaks to no purpose? 'The Spirit God made to dwell in us longs jealously.'",
      "T": "Has Scripture been speaking all along to no effect? God himself placed his Spirit within us, and that Spirit guards his claim on us with an intensity we can only call jealousy."
    },
    "6": {
      "L": "But he gives greater grace. Therefore it says, 'God opposes the proud but gives grace to the humble.'",
      "M": "But he gives all the more grace. That is why Scripture says: 'God opposes the proud but shows favor to the humble.'",
      "T": "And yet he gives grace upon grace—grace lavish enough to overcome our divided loyalties. As Scripture puts it: God sets himself against the proud, but pours his favor out on the humble."
    },
    "7": {
      "L": "Submit therefore to God. Resist the devil, and he will flee from you.",
      "M": "Submit yourselves therefore to God. Resist the devil, and he will flee from you.",
      "T": "So bring yourself under God's authority. Take your stand against the devil—and he will run."
    },
    "8": {
      "L": "Draw near to God, and he will draw near to you. Cleanse your hands, you sinners, and purify your hearts, you double-minded.",
      "M": "Draw near to God, and he will draw near to you. Cleanse your hands, you sinners, and purify your hearts, you who are double-minded.",
      "T": "Come close to God, and he will come close to you. Wash the guilt from your hands—you have been living like people who do not know him. Purify your inner life—you have been serving two masters at once."
    },
    "9": {
      "L": "Be wretched and mourn and weep. Let your laughter be turned to mourning and your joy to gloom.",
      "M": "Be wretched and mourn and weep. Let your laughter be turned to mourning and your joy to grief.",
      "T": "Feel the weight of what you have done. Let grief come in. Stop laughing as though nothing is wrong—there is real reason to mourn. Let your lightheartedness become solemnity."
    },
    "10": {
      "L": "Humble yourselves before the Lord, and he will exalt you.",
      "M": "Humble yourselves before the Lord, and he will lift you up.",
      "T": "Lower yourselves before the Lord—and he will raise you up."
    },
    "11": {
      "L": "Do not speak evil of one another, brothers. The one speaking evil of a brother or judging his brother speaks evil of the law and judges the law. But if you judge the law, you are not a doer of the law but a judge.",
      "M": "Do not speak evil against one another, brothers. Whoever speaks evil against a brother or judges his brother speaks evil against the law and judges the law. But if you judge the law, you are not a doer of the law but a judge of it.",
      "T": "Stop tearing each other down with your words, brothers. When you attack another believer or appoint yourself their judge, you are overstepping the law—you place yourself above it rather than under it, trading the doer's place for the judge's seat."
    },
    "12": {
      "L": "There is one Lawgiver and Judge, he who is able to save and to destroy. But who are you to judge your neighbor?",
      "M": "There is only one Lawgiver and Judge—the one who is able to save and destroy. But who are you to judge your neighbor?",
      "T": "There is one Lawgiver, one Judge—the God who alone has both the right and the power to save or condemn. Who do you think you are, appointing yourself to judge the person next to you?"
    },
    "13": {
      "L": "Come now, you who say, 'Today or tomorrow we will go into this city and spend a year there and trade and make a profit.'",
      "M": "Come now, you who say, 'Today or tomorrow we will go to this city and spend a year there doing business and making money.'",
      "T": "Listen to this kind of talk: 'We're heading to such-and-such city for a year—we'll trade, we'll turn a profit.' Sounds reasonable enough."
    },
    "14": {
      "L": "Yet you do not know what your life will be tomorrow. For you are a mist that appears for a little time and then vanishes.",
      "M": "Yet you do not know what tomorrow will bring. What is your life? For you are a mist that appears for a little while and then vanishes.",
      "T": "But you have no idea what tomorrow holds. Your life is a morning mist—visible for a moment, then gone without a trace."
    },
    "15": {
      "L": "Instead you ought to say, 'If the Lord wills, we will live and do this or that.'",
      "M": "Instead you ought to say, 'If the Lord wills, we will live and do this or that.'",
      "T": "What you should be saying is: 'If the Lord wills it, we will live to carry out our plans.'"
    },
    "16": {
      "L": "But now you boast in your arrogance. All such boasting is evil.",
      "M": "But as it is, you boast in your arrogance. All such boasting is evil.",
      "T": "Instead you strut about and brag as though your future were yours to command. That kind of self-congratulation is simply wrong."
    },
    "17": {
      "L": "So the one who knows the right thing to do and does not do it, to him it is sin.",
      "M": "So whoever knows the right thing to do and fails to do it, for that person it is sin.",
      "T": "Knowing the good and refusing to do it—that is its own kind of sin."
    }
  },
  "5": {
    "1": {
      "L": "Come now, you rich, weep and howl for your miseries that are coming upon you.",
      "M": "Come now, you rich people, weep and wail over the miseries that are coming upon you.",
      "T": "Now hear this, you wealthy: weep and howl—the suffering that is coming for you will justify every tear."
    },
    "2": {
      "L": "Your riches have rotted and your garments have become moth-eaten.",
      "M": "Your riches have rotted, and your garments are moth-eaten.",
      "T": "Your wealth has already begun to decay. Your fine clothing has been eaten by moths."
    },
    "3": {
      "L": "Your gold and silver have corroded, and their corrosion will be evidence against you and will eat your flesh like fire. You have stored up treasure in the last days.",
      "M": "Your gold and silver have corroded, and their corrosion will testify against you and devour your flesh like fire. You have stored up treasure in the last days.",
      "T": "Your gold and silver have rusted away—and that rust is its own verdict against you, a fire that will consume your very bodies. This is what you have done in the final days of history: accumulated wealth while others went without."
    },
    "4": {
      "L": "Behold, the wages of the laborers who mowed your fields, which you have kept back by fraud, are crying out, and the cries of the harvesters have entered into the ears of the Lord of hosts.",
      "M": "Behold, the wages you withheld from the workers who harvested your fields are crying out against you, and the cries of the harvesters have reached the ears of the Lord of hosts.",
      "T": "Listen: the wages you withheld from the farm workers who harvested your crops—those unpaid wages are crying out. The workers' own cries have already reached the ears of the Lord of the heavenly armies."
    },
    "5": {
      "L": "You have lived in luxury and self-indulgence on the earth; you have fattened your hearts in a day of slaughter.",
      "M": "You have lived on the earth in luxury and self-indulgence. You have fattened your hearts in a day of slaughter.",
      "T": "You have spent your days on earth in ease and indulgence, fattening yourselves—all while the day of reckoning drew near, as cattle fatten themselves unaware before the slaughter."
    },
    "6": {
      "L": "You have condemned and murdered the righteous one; he does not resist you.",
      "M": "You have condemned and murdered the righteous person, who does not resist you.",
      "T": "You have brought charges against the innocent and put them to death—and they never fought back."
    },
    "7": {
      "L": "Be patient therefore, brothers, until the coming of the Lord. See how the farmer waits for the precious fruit of the earth, being patient over it, until it receives the early and the late rain.",
      "M": "Be patient therefore, brothers, until the coming of the Lord. See how the farmer waits for the precious fruit of the earth, being patient about it, until it receives the early and the late rains.",
      "T": "So wait patiently, brothers—wait for the Lord's return. Think of the farmer: he plants his precious crop and then waits through the long season, trusting that the autumn rains and the spring rains will come in their time."
    },
    "8": {
      "L": "You also be patient. Establish your hearts, for the coming of the Lord is at hand.",
      "M": "You also be patient. Strengthen your hearts, for the coming of the Lord is near.",
      "T": "You must have that same patience. Settle your hearts and hold steady—the Lord's return is close."
    },
    "9": {
      "L": "Do not grumble against one another, brothers, so that you may not be judged. Behold, the Judge is standing at the door.",
      "M": "Do not grumble against one another, brothers, so that you will not be judged. The Judge is standing right at the door.",
      "T": "Stop airing your grievances against each other, brothers—unless you want to face judgment yourselves. The Judge is already standing at the door."
    },
    "10": {
      "L": "As an example of suffering and patience, brothers, take the prophets who spoke in the name of the Lord.",
      "M": "As an example of suffering and patience, brothers, take the prophets who spoke in the name of the Lord.",
      "T": "Look to the prophets, brothers—they spoke God's word and they suffered for it. Let their endurance be your model."
    },
    "11": {
      "L": "Behold, we count those blessed who remained steadfast. You have heard of the steadfastness of Job, and you have seen the outcome of the Lord—that the Lord is compassionate and merciful.",
      "M": "Behold, we count as blessed those who remained steadfast. You have heard of the steadfastness of Job, and you have seen the outcome that the Lord brought about—for the Lord is compassionate and merciful.",
      "T": "We call people blessed who held on through suffering. You know the story of Job's endurance—and you know how it ended. That ending reveals who the Lord is: boundlessly compassionate, overflowing with mercy."
    },
    "12": {
      "L": "But above all, my brothers, do not swear, neither by heaven nor by earth nor by any other oath, but let your 'yes' be yes and your 'no' be no, so that you may not fall under condemnation.",
      "M": "But above all, my brothers, do not swear—not by heaven or by earth or by any other oath. Let your yes mean yes and your no mean no, so that you do not fall under judgment.",
      "T": "Above everything else, brothers: no oaths. Don't swear by heaven, don't swear by earth, don't swear by anything at all. A plain yes should mean yes, and a plain no should mean no—or you will find yourself standing under God's judgment."
    },
    "13": {
      "L": "Is anyone among you suffering? Let him pray. Is anyone cheerful? Let him sing praise.",
      "M": "Is anyone among you suffering? Let him pray. Is anyone cheerful? Let him sing praises.",
      "T": "Are you suffering? Pray. Are you joyful? Sing."
    },
    "14": {
      "L": "Is anyone among you sick? Let him call for the elders of the assembly, and let them pray over him, anointing him with oil in the name of the Lord.",
      "M": "Is anyone among you sick? Let him call for the elders of the church, and let them pray over him, anointing him with oil in the name of the Lord.",
      "T": "Is anyone among you ill? Call the church elders. Let them gather and pray over the sick person, anointing them with oil as they invoke the name of the Lord."
    },
    "15": {
      "L": "And the prayer of faith will save the one who is sick, and the Lord will raise him up. And if he has committed sins, they will be forgiven him.",
      "M": "And the prayer offered in faith will restore the one who is sick. The Lord will raise him up, and if he has sinned, he will be forgiven.",
      "T": "The prayer that trusts God will heal the sick person—the Lord will lift them up. And if sin has burdened them alongside sickness, that too will be forgiven."
    },
    "16": {
      "L": "Therefore confess your sins to one another and pray for one another, that you may be healed. The prayer of a righteous person has great power as it is working.",
      "M": "Therefore confess your sins to one another and pray for one another, so that you may be healed. The prayer of a righteous person is powerful and effective.",
      "T": "So make it a practice: confess your failings to each other, pray for each other. This is how healing comes—not in isolation but in community. And the prayer of someone who is right with God carries extraordinary force."
    },
    "17": {
      "L": "Elijah was a man of like nature with us, and he prayed earnestly that it might not rain, and it did not rain on the earth for three years and six months.",
      "M": "Elijah was a human being just like us, and he prayed earnestly that it would not rain, and it did not rain on the earth for three years and six months.",
      "T": "Elijah was as human as any of us—no more, no less. He prayed with everything he had that rain would stop, and for three and a half years the earth went without."
    },
    "18": {
      "L": "Then he prayed again, and heaven gave rain, and the earth brought forth its fruit.",
      "M": "Then he prayed again, and the sky gave rain, and the earth produced its crop.",
      "T": "He prayed again, and the rains came, and the land yielded its harvest."
    },
    "19": {
      "L": "My brothers, if anyone among you wanders from the truth and someone turns him back,",
      "M": "My brothers, if anyone among you strays from the truth and someone brings him back,",
      "T": "Brothers, if one of your number wanders away from the truth and another person draws them back,"
    },
    "20": {
      "L": "let him know that whoever turns a sinner from the error of his way will save his soul from death and will cover a multitude of sins.",
      "M": "let that person know that whoever turns a sinner back from his wandering path will save a soul from death and cover a multitude of sins.",
      "T": "that person should know what they have accomplished: they have rescued a soul from death and drawn a curtain over a vast catalogue of sins."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'james')
        merge_tier(existing, JAMES, tier_key)
        save(tier_dir, 'james', existing)
    print('James 3–5 written.')

if __name__ == '__main__':
    main()
