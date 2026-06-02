"""
MKT Romans chapters 9-16 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-romans-9-16.py

Key translation decisions (continuing from mkt-romans-1-8.py):
- G4102 πίστις: "faith" / "faithfulness" — maintained from chs 1-8
- G1343 δικαιοσύνη: "righteousness" (L/M); "right standing" / "being made right" in T forensic contexts
- G4561 σάρξ: "flesh" (L always); "sinful nature" only in T where the power sense dominates
- G3551 νόμος: "the Law" when Torah; "law/principle" for abstract uses
- G4151 πνεῦμα: "Spirit" capitalized where divine Spirit is the clear referent
- G166 αἰώνιος: "eternal" (L/M); "the life of the age to come" (T) preserving eschatological register
- G1589 ἐκλογή: "election" (L/M); "God's choosing" (T)
- G4745 στήριγμα / G3549 νόμος τελειόω: 10:4 τέλος as "goal" not mere termination
- 9:5 christological reading: "who is God over all, blessed forever" — not a separate doxology
- 9:22-23 σκεύη: "vessels" (L); "objects" (M/T) — avoids implying rigid mechanical predetermination in M/T
- 11:26 "all Israel will be saved" — kept literal; T adds scope clarification
- 12:1 λογικήν: "reasonable/rational" (L); "true and proper" (M); "the worship that truly makes sense" (T)
- 13:1-7 ἐξουσίαις: governing authorities — not absolutized; T renders with principled submission framing
- 14:17 kingdom of God: "kingdom" (L/M); "reign" (T) — preserving dynamic sense
- 16:1 διάκονος re Phoebe: "servant" (L); "deacon" (M); "minister" (T) — acknowledging her official role
- 16:7 Ἰουνίαν: "Junia" (female name) — "well known among the apostles" (ἐπίσημοι ἐν τοῖς ἀποστόλοις)
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

ROMANS = {
  "9": {
    "1": {
      "L": "I am telling the truth in Christ—I am not lying, my conscience bearing witness with me in the Holy Spirit—",
      "M": "I speak the truth in Christ—I am not lying, my conscience confirms it through the Holy Spirit—",
      "T": "I am telling the truth in Christ—I swear it, my conscience confirms it by the Holy Spirit—"
    },
    "2": {
      "L": "that I have great grief and unceasing anguish in my heart.",
      "M": "I have great sorrow and unceasing anguish in my heart.",
      "T": "there is a deep grief in me, an anguish that never lets up."
    },
    "3": {
      "L": "For I could pray that I myself were accursed, cut off from Christ, for the sake of my brothers, my kinsmen according to the flesh,",
      "M": "For I could wish that I myself were cursed and cut off from Christ for the sake of my people, those of my own race,",
      "T": "I would be willing to be cut off from Christ—to be under God's curse—if it would mean salvation for my own people, my kinsmen by blood."
    },
    "4": {
      "L": "who are Israelites; to whom belong the adoption and the glory and the covenants and the giving of the law and the temple service and the promises,",
      "M": "the people of Israel. Theirs is the adoption to sonship; theirs the divine glory, the covenants, the receiving of the law, the temple worship and the promises.",
      "T": "They are Israelites. They received the adoption as God's children, the visible glory of his presence, the covenants, the giving of the Torah, the forms of worship, and the promises."
    },
    "5": {
      "L": "to whom belong the patriarchs, and from whom is the Christ according to the flesh, who is God over all, blessed forever. Amen.",
      "M": "Theirs are the patriarchs, and from them is traced the human ancestry of the Messiah, who is God over all, forever praised! Amen.",
      "T": "The patriarchs are theirs, and from them came the Messiah himself in his human nature—the one who is God over all, worthy of praise forever. Amen."
    },
    "6": {
      "L": "But it is not as though the word of God has failed. For not all who are from Israel are Israel,",
      "M": "It is not as though God's word had failed. For not all who are descended from Israel are Israel.",
      "T": "But God's word has not failed. The truth is, not everyone descended from Israel is truly Israel."
    },
    "7": {
      "L": "nor because they are Abraham's seed are they all children; but, 'In Isaac shall your seed be called.'",
      "M": "Nor because they are his descendants are they all Abraham's children. On the contrary, 'It is through Isaac that your offspring will be reckoned.'",
      "T": "And not everyone who is Abraham's physical descendant counts as his true child. Instead, God said: 'Through Isaac your descendants will be named.'"
    },
    "8": {
      "L": "That is, it is not the children of the flesh who are children of God, but the children of the promise are reckoned as seed.",
      "M": "In other words, it is not the children by physical descent who are God's children, but it is the children of the promise who are regarded as Abraham's offspring.",
      "T": "In other words, it is not natural-born children who are God's children—it is the children of the promise who are counted as the true offspring."
    },
    "9": {
      "L": "For this is the word of promise: 'About this time I will come, and Sarah will have a son.'",
      "M": "For this was how the promise was stated: 'At the appointed time I will return, and Sarah will have a son.'",
      "T": "For the promise ran like this: 'At the right time I will return, and Sarah will have a son.'"
    },
    "10": {
      "L": "And not only this, but also when Rebekah had conceived by one man, our father Isaac—",
      "M": "Not only that, but Rebekah's children were conceived at the same time by our father Isaac.",
      "T": "And the same principle runs deeper still. Rebekah conceived twin sons by our ancestor Isaac—"
    },
    "11": {
      "L": "for while the children had not yet been born and had not done anything good or bad, in order that God's purpose according to election might stand, not of works but of him who calls,",
      "M": "Yet, before the twins were born or had done anything good or bad—in order that God's purpose in election might stand: not by works but by him who calls—",
      "T": "—but before they were even born, before they had done anything good or bad, God made his choice. This was so that his purpose of election would hold firm—not on the basis of what anyone does, but entirely on the basis of the one who calls."
    },
    "12": {
      "L": "it was said to her, 'The older will serve the younger.'",
      "M": "she was told, 'The older will serve the younger.'",
      "T": "She was told: 'The older will serve the younger.'"
    },
    "13": {
      "L": "Just as it is written, 'Jacob I loved, but Esau I hated.'",
      "M": "Just as it is written: 'Jacob I loved, but Esau I hated.'",
      "T": "As scripture confirms: 'Jacob I loved—Esau I set aside.'"
    },
    "14": {
      "L": "What shall we say then? There is no unrighteousness with God, is there? By no means!",
      "M": "What then shall we say? Is God unjust? Not at all!",
      "T": "What do we make of this? Is God being unfair? Absolutely not!"
    },
    "15": {
      "L": "For he says to Moses, 'I will have mercy on whom I have mercy, and I will have compassion on whom I have compassion.'",
      "M": "For he says to Moses, 'I will have mercy on whom I have mercy, and I will have compassion on whom I have compassion.'",
      "T": "He said to Moses: 'I will show mercy to whomever I choose to show mercy, and I will have compassion on whomever I choose to have compassion.'"
    },
    "16": {
      "L": "So then it does not depend on the one who wills or the one who runs, but on God who has mercy.",
      "M": "It does not, therefore, depend on human desire or effort, but on God's mercy.",
      "T": "So it comes down to this: it is not a matter of human wanting or human striving—it is entirely a matter of God's mercy."
    },
    "17": {
      "L": "For the Scripture says to Pharaoh, 'For this very purpose I raised you up, that I might display my power in you, and that my name might be proclaimed throughout all the earth.'",
      "M": "For Scripture says to Pharaoh: 'I raised you up for this very purpose, that I might display my power in you and that my name might be proclaimed in all the earth.'",
      "T": "For scripture says to Pharaoh: 'I put you on the scene for this very reason—to display my power through you, and to spread my name throughout the whole earth.'"
    },
    "18": {
      "L": "So then he has mercy on whom he wills, and he hardens whom he wills.",
      "M": "Therefore God has mercy on whom he wants to have mercy, and he hardens whom he wants to harden.",
      "T": "So God shows mercy to whomever he chooses—and he allows whomever he chooses to become hard."
    },
    "19": {
      "L": "You will say to me then, 'Why does he still find fault? For who has resisted his will?'",
      "M": "One of you will say to me: 'Then why does God still blame us? For who is able to resist his will?'",
      "T": "Someone will push back: 'Then how can God hold anyone responsible? Who can resist his will?'"
    },
    "20": {
      "L": "On the contrary, who are you, O man, who answers back to God? Will the thing formed say to its molder, 'Why did you make me like this?'",
      "M": "But who are you, a human being, to talk back to God? 'Shall what is formed say to the one who formed it, \"Why did you make me like this?\"'",
      "T": "But really—who do you think you are, answering back to God? Does a pot say to the potter, 'Why did you make me this shape?'"
    },
    "21": {
      "L": "Or does the potter not have authority over the clay, to make from the same lump one vessel for honor and another for dishonor?",
      "M": "Does not the potter have the right to make out of the same lump of clay some pottery for special purposes and some for common use?",
      "T": "The potter has every right over the clay—to make from the same lump one vessel for display and another for everyday use."
    },
    "22": {
      "L": "What if God, desiring to show his wrath and to make his power known, bore with much patience vessels of wrath prepared for destruction,",
      "M": "What if God, although choosing to show his wrath and make his power known, bore with great patience the objects of his wrath—prepared for destruction?",
      "T": "What if God, though fully willing to demonstrate his wrath and make his power plain, patiently endured those marked out for destruction—"
    },
    "23": {
      "L": "in order to make known the riches of his glory upon vessels of mercy, which he prepared beforehand for glory—",
      "M": "What if he did this to make the riches of his glory known to the objects of his mercy, whom he prepared in advance for glory—",
      "T": "—doing so precisely to make the wealth of his glory known to those destined for mercy, whom he prepared in advance for glory?"
    },
    "24": {
      "L": "even us, whom he also called, not from among Jews only but also from among Gentiles?",
      "M": "Even us, whom he also called, not only from the Jews but also from the Gentiles?",
      "T": "And those are us—the ones he called: not only from among the Jews but from among the Gentiles as well."
    },
    "25": {
      "L": "As he also says in Hosea, 'I will call those who were not my people, \"My people,\" and her who was not beloved, \"Beloved.\"'",
      "M": "As he says in Hosea: 'I will call them \"my people\" who are not my people; and I will call her \"my loved one\" who is not my loved one,'",
      "T": "As he says in Hosea: 'The people who were not my people I will call \"my people\"—and the one who was not beloved I will call \"my beloved.\"'"
    },
    "26": {
      "L": "'And it shall be that in the place where it was said to them, \"You are not my people,\" there they shall be called sons of the living God.'",
      "M": "and, 'In the very place where it was said to them, \"You are not my people,\" there they will be called \"children of the living God.\"'",
      "T": "'And in the very place where they were told, \"You are not my people\"—there they will be called children of the living God.'"
    },
    "27": {
      "L": "And Isaiah cries out concerning Israel, 'Though the number of the sons of Israel be as the sand of the sea, only the remnant will be saved;",
      "M": "Isaiah cries out concerning Israel: 'Though the number of the Israelites be like the sand by the sea, only the remnant will be saved.',",
      "T": "And Isaiah shouts it out about Israel: 'Though the number of Israelites be as countless as sand by the sea, only a remnant will be saved—'"
    },
    "28": {
      "L": "for the Lord will carry out his sentence on the earth, fully and without delay.'",
      "M": "for the Lord will carry out his sentence on the earth with speed and finality.'",
      "T": "'—for the Lord will execute his sentence on the earth decisively and without delay.'"
    },
    "29": {
      "L": "And just as Isaiah predicted, 'Unless the Lord of hosts had left us offspring, we would have become like Sodom, and been made like Gomorrah.'",
      "M": "It is just as Isaiah said previously: 'Unless the Lord Almighty had left us descendants, we would have become like Sodom, we would have been like Gomorrah.'",
      "T": "And as Isaiah had said before: 'If the Lord of heavenly armies had not left us a surviving seed, we would have become like Sodom—wiped out like Gomorrah.'"
    },
    "30": {
      "L": "What shall we say then? That Gentiles who did not pursue righteousness have attained it, even a righteousness that is by faith;",
      "M": "What then shall we say? That the Gentiles, who did not pursue righteousness, have obtained it, a righteousness that is by faith;",
      "T": "What do we conclude, then? That Gentiles—who were not even pursuing righteousness—have obtained it, a righteousness that comes through faith."
    },
    "31": {
      "L": "but Israel, pursuing a law of righteousness, did not attain that law.",
      "M": "but the people of Israel, who pursued the law as the way of righteousness, have not attained their goal.",
      "T": "But Israel, striving after a Law that would produce righteousness, never reached it."
    },
    "32": {
      "L": "Why? Because it was not by faith but as if it were by works. They stumbled over the stone of stumbling,",
      "M": "Why not? Because they pursued it not by faith but as if it were by works. They stumbled over the stumbling stone.",
      "T": "Why not? Because they pursued it as if it were a matter of what they did, not of faith. They tripped over the stumbling stone—"
    },
    "33": {
      "L": "just as it is written, 'Behold, I am laying in Zion a stone of stumbling and a rock of offense, and whoever believes in him will not be put to shame.'",
      "M": "As it is written: 'See, I lay in Zion a stone that causes people to stumble and a rock that makes them fall, and the one who believes in him will never be put to shame.'",
      "T": "—exactly as scripture says: 'Look, I am placing in Zion a stone over which people stumble, a rock that makes them fall. But whoever trusts in him will never be put to shame.'"
    }
  },
  "10": {
    "1": {
      "L": "Brothers, the desire of my heart and my prayer to God for them is for their salvation.",
      "M": "Brothers and sisters, my heart's desire and prayer to God for the Israelites is that they may be saved.",
      "T": "Brothers and sisters, the deepest longing of my heart and my constant prayer to God is that they might be saved."
    },
    "2": {
      "L": "For I testify about them that they have a zeal for God, but not according to knowledge.",
      "M": "For I can testify about them that they are zealous for God, but their zeal is not based on knowledge.",
      "T": "I can vouch for this: they burn with zeal for God—but it is a zeal without understanding."
    },
    "3": {
      "L": "For not knowing the righteousness of God and seeking to establish their own, they did not submit to the righteousness of God.",
      "M": "Since they did not know the righteousness of God and sought to establish their own, they did not submit to God's righteousness.",
      "T": "Not knowing the righteousness that comes from God, and trying to establish their own instead, they refused to submit to God's righteousness."
    },
    "4": {
      "L": "For Christ is the end of the law for righteousness to everyone who believes.",
      "M": "Christ is the culmination of the law so that there may be righteousness for everyone who believes.",
      "T": "For Christ is the goal the Law was always pointing toward—so that everyone who trusts in him may be made right with God."
    },
    "5": {
      "L": "For Moses writes of the righteousness that is based on the law, that 'The person who does these things shall live by them.'",
      "M": "Moses writes this about the righteousness that is by the law: 'The person who does these things will live by them.'",
      "T": "Moses writes about the righteousness based on doing the Law: 'The person who does these things will live by them.'"
    },
    "6": {
      "L": "But the righteousness that is by faith says, 'Do not say in your heart, \"Who will ascend into heaven?\"' (that is, to bring Christ down,)",
      "M": "But the righteousness that is by faith says: 'Do not say in your heart, \"Who will ascend into heaven?\"' (that is, to bring Christ down)",
      "T": "But the righteousness that comes from faith says this: 'Don't say to yourself, \"Who will go up into heaven?\"'—meaning, to bring Christ down—"
    },
    "7": {
      "L": "'or \"Who will descend into the abyss?\"' (that is, to bring Christ up from the dead.)",
      "M": "'or \"Who will descend into the deep?\"' (that is, to bring Christ up from the dead).",
      "T": "'—or, \"Who will go down into the deep?\"'—meaning, to bring Christ up from the dead."
    },
    "8": {
      "L": "But what does it say? 'The word is near you, in your mouth and in your heart'—that is, the word of faith that we proclaim—",
      "M": "But what does it say? 'The word is near you; it is in your mouth and in your heart,' that is, the message concerning faith that we proclaim:",
      "T": "No—what does it say? 'The word is right here with you—in your mouth and in your heart.' That is the word of faith we are proclaiming."
    },
    "9": {
      "L": "that if you confess with your mouth that Jesus is Lord and believe in your heart that God raised him from the dead, you will be saved.",
      "M": "If you declare with your mouth, 'Jesus is Lord,' and believe in your heart that God raised him from the dead, you will be saved.",
      "T": "If you confess with your own mouth that Jesus is Lord, and believe in your heart that God raised him from the dead—you will be saved."
    },
    "10": {
      "L": "For with the heart one believes, resulting in righteousness, and with the mouth one confesses, resulting in salvation.",
      "M": "For it is with your heart that you believe and are justified, and it is with your mouth that you profess your faith and are saved.",
      "T": "With the heart a person trusts and is put right with God; with the mouth a person confesses and is saved."
    },
    "11": {
      "L": "For the Scripture says, 'Everyone who believes in him will not be put to shame.'",
      "M": "As Scripture says, 'Anyone who believes in him will never be put to shame.'",
      "T": "As scripture says: 'Everyone who trusts in him will never be put to shame.'"
    },
    "12": {
      "L": "For there is no distinction between Jew and Greek; for the same Lord is Lord of all, abounding in riches for all who call on him;",
      "M": "For there is no difference between Jew and Gentile—the same Lord is Lord of all and richly blesses all who call on him,",
      "T": "There is no difference between Jew and Gentile—the same Lord is Lord of all, pouring out his riches on everyone who calls on him."
    },
    "13": {
      "L": "for 'Everyone who calls on the name of the Lord will be saved.'",
      "M": "for, 'Everyone who calls on the name of the Lord will be saved.'",
      "T": "For: 'Everyone who calls on the name of the Lord will be saved.'"
    },
    "14": {
      "L": "How then are they to call on him in whom they have not believed? And how are they to believe in him whom they have not heard? And how are they to hear without a proclaimer?",
      "M": "How, then, can they call on the one they have not believed in? And how can they believe in the one of whom they have not heard? And how can they hear without someone preaching to them?",
      "T": "But how can people call on someone they have not trusted? And how can they trust someone they have not heard about? And how can they hear if no one is sent to tell them?"
    },
    "15": {
      "L": "And how are they to preach unless they are sent? Just as it is written, 'How beautiful are the feet of those who bring good news!'",
      "M": "And how can anyone preach unless they are sent? As it is written: 'How beautiful are the feet of those who bring good news!'",
      "T": "And how can anyone go and tell unless they are sent? As scripture says: 'How welcome are the footsteps of those who carry good news!'"
    },
    "16": {
      "L": "But they did not all obey the gospel. For Isaiah says, 'Lord, who has believed our report?'",
      "M": "But not all the Israelites accepted the good news. For Isaiah says, 'Lord, who has believed our message?'",
      "T": "But not everyone responded. Isaiah put it plainly: 'Lord, who has believed what we told them?'"
    },
    "17": {
      "L": "So faith comes by hearing, and hearing through the word of Christ.",
      "M": "Consequently, faith comes from hearing the message, and the message is heard through the word about Christ.",
      "T": "So then, faith is born from hearing—and what is heard is the message about Christ."
    },
    "18": {
      "L": "But I say, they have not heard, have they? On the contrary, 'Their voice has gone out into all the earth, and their words to the ends of the world.'",
      "M": "But I ask: Did they not hear? Of course they did: 'Their voice has gone out into all the earth, their words to the ends of the world.'",
      "T": "But did they not hear? Of course they did. As the psalm says: 'Their voice has gone out to all the earth, their words to the very ends of the world.'"
    },
    "19": {
      "L": "But I say, did Israel not know? First Moses says, 'I will provoke you to jealousy by that which is not a nation; by a nation without understanding I will make you angry.'",
      "M": "Again I ask: Did Israel not understand? First, Moses says, 'I will make you envious by those who are not a nation; I will make you angry by a nation that has no understanding.'",
      "T": "Did Israel not understand, then? Consider: Moses was first to say it: 'I will provoke you to jealousy by a people who are not even a nation; I will enrage you by a people who have no understanding.'"
    },
    "20": {
      "L": "And Isaiah is very bold and says, 'I was found by those who did not seek me; I appeared to those who did not ask for me.'",
      "M": "And Isaiah boldly says, 'I was found by those who did not seek me; I revealed myself to those who did not ask for me.'",
      "T": "Then Isaiah goes further and boldly says: 'I was found by those who were not looking for me; I showed myself to those who were not asking.'"
    },
    "21": {
      "L": "But to Israel he says, 'All day long I spread out my hands to a disobedient and contrary people.'",
      "M": "But concerning Israel he says, 'All day long I have held out my hands to a disobedient and obstinate people.'",
      "T": "But about Israel he says: 'All day long I held out my hands to a disobedient and stubborn people.'"
    }
  },
  "11": {
    "1": {
      "L": "I say then, God has not rejected his people, has he? By no means! For I too am an Israelite, from the seed of Abraham, of the tribe of Benjamin.",
      "M": "I ask then: Did God reject his people? By no means! I am an Israelite myself, a descendant of Abraham, from the tribe of Benjamin.",
      "T": "Has God then abandoned his people? Not for a moment! I myself am an Israelite—a descendant of Abraham, from the tribe of Benjamin."
    },
    "2": {
      "L": "God has not rejected his people whom he foreknew. Or do you not know what the Scripture says about Elijah, how he pleads with God against Israel?",
      "M": "God did not reject his people, whom he foreknew. Don't you know what Scripture says in the passage about Elijah—how he appealed to God against Israel?",
      "T": "God has not cast away the people he knew in advance. Don't you recall what the scripture says about Elijah—how he went before God with a complaint against Israel?"
    },
    "3": {
      "L": "'Lord, they have killed your prophets, they have torn down your altars, and I alone am left, and they are seeking my life.'",
      "M": "'Lord, they have killed your prophets and torn down your altars; I am the only one left, and they are trying to kill me.'",
      "T": "'Lord, they have murdered your prophets and demolished your altars. I am the only one left, and now they are trying to kill me.'"
    },
    "4": {
      "L": "But what is the divine response to him? 'I have kept for myself seven thousand men who have not bowed the knee to Baal.'",
      "M": "And what was God's answer to him? 'I have reserved for myself seven thousand who have not bowed the knee to Baal.'",
      "T": "And what did God say in reply? 'I have kept for myself seven thousand people who have never knelt to Baal.'"
    },
    "5": {
      "L": "So then also at the present time there has come to be a remnant according to the gracious election.",
      "M": "So too, at the present time there is a remnant chosen by grace.",
      "T": "In the same way, right now, there is a remnant—chosen by grace."
    },
    "6": {
      "L": "But if by grace, it is no longer by works; otherwise grace would no longer be grace.",
      "M": "And if by grace, then it cannot be based on works; if it were, grace would no longer be grace.",
      "T": "And if it is by grace, then it cannot be on the basis of works—otherwise grace would no longer be grace."
    },
    "7": {
      "L": "What then? What Israel seeks, it has not obtained, but the elect obtained it, and the rest were hardened—",
      "M": "What then? What the people of Israel sought so earnestly they did not obtain. The elect among them did, but the others were hardened,",
      "T": "So what happened? Israel failed to obtain what it was reaching for. The chosen ones received it—the rest were hardened."
    },
    "8": {
      "L": "just as it is written, 'God gave them a spirit of stupor, eyes to see not and ears to hear not, even to this very day.'",
      "M": "as it is written: 'God gave them a spirit of stupor, eyes that could not see and ears that could not hear, to this very day.'",
      "T": "As scripture says: 'God gave them a spirit of deep sleep—eyes that cannot see, ears that cannot hear—right up to this day.'"
    },
    "9": {
      "L": "And David says, 'Let their table become a snare and a trap, and a stumbling block and a retribution to them;",
      "M": "And David says: 'May their table become a snare and a trap, a stumbling block and a retribution for them.",
      "T": "And David says: 'May their very table become a snare and a trap for them—a stumbling block and a punishment.'"
    },
    "10": {
      "L": "let their eyes be darkened so as not to see, and bend their back continually.'",
      "M": "'May their eyes be darkened so they cannot see, and their backs be bent forever.'",
      "T": "'May their eyes be darkened so they cannot see—and keep their backs bent low forever.'"
    },
    "11": {
      "L": "I say then, they have not stumbled so as to fall, have they? By no means! But by their transgression salvation has come to the Gentiles, to make them jealous.",
      "M": "Again I ask: Did they stumble so as to fall beyond recovery? Not at all! Rather, because of their transgression, salvation has come to the Gentiles to make Israel envious.",
      "T": "Did they stumble so as to be permanently lost? Absolutely not! Rather, through their stumbling, salvation has gone out to the Gentiles—to provoke Israel to jealousy."
    },
    "12": {
      "L": "Now if their transgression is riches for the world, and their failure is riches for the Gentiles, how much more their fullness!",
      "M": "But if their transgression means riches for the world, and their loss means riches for the Gentiles, how much greater riches will their full inclusion bring!",
      "T": "If their stumbling has meant wealth for the world—if their failure has meant riches for the Gentiles—imagine what their full restoration will bring!"
    },
    "13": {
      "L": "But I am speaking to you who are Gentiles. Inasmuch then as I am an apostle of Gentiles, I glorify my ministry,",
      "M": "I am talking to you Gentiles. Inasmuch as I am the apostle to the Gentiles, I take pride in my ministry",
      "T": "Now I am addressing you Gentiles directly. As the apostle to the Gentiles, I take pride in this calling—"
    },
    "14": {
      "L": "if somehow I might move my own people to jealousy and save some of them.",
      "M": "in the hope that I may somehow arouse my own people to envy and save some of them.",
      "T": "—in hopes that I can provoke my own people to jealousy and somehow bring some of them to salvation."
    },
    "15": {
      "L": "For if their rejection is the reconciliation of the world, what will their acceptance be but life from the dead?",
      "M": "For if their rejection brought reconciliation to the world, what will their acceptance be but life from the dead?",
      "T": "For if their being set aside has meant the reconciliation of the world—what will their being received back mean? Nothing less than life from the dead!"
    },
    "16": {
      "L": "And if the firstfruit is holy, so is the lump; and if the root is holy, so are the branches.",
      "M": "If the part of the dough offered as firstfruits is holy, then the whole batch is holy; if the root is holy, so are the branches.",
      "T": "If the first piece of dough dedicated to God is holy, the whole batch is holy too. If the root of the tree is holy, so are the branches."
    },
    "17": {
      "L": "But if some of the branches were broken off, and you, being a wild olive tree, were grafted in among them and became partaker with them of the rich root of the olive tree,",
      "M": "If some of the branches have been broken off, and you, though a wild olive shoot, have been grafted in among the others and now share in the nourishing sap from the olive root,",
      "T": "But if some branches were broken off, and you—a shoot from a wild olive tree—were grafted in among the remaining branches to share in the rich sap of the cultivated olive tree,"
    },
    "18": {
      "L": "do not be arrogant toward the branches; but if you are arrogant, remember that it is not you who support the root, but the root that supports you.",
      "M": "do not consider yourself to be superior to those other branches. If you do, consider this: you do not support the root, but the root supports you.",
      "T": "do not look down on those natural branches. If you are tempted to, remember: you do not sustain the root—the root sustains you."
    },
    "19": {
      "L": "You will say then, 'Branches were broken off so that I might be grafted in.'",
      "M": "You will say then, 'Branches were broken off so that I could be grafted in.'",
      "T": "You might say, 'Those branches were removed so I could be grafted in.'"
    },
    "20": {
      "L": "True. By their unbelief they were broken off, and you stand by your faith. Do not be haughty, but fear,",
      "M": "Granted. But they were broken off because of unbelief, and you stand by faith. Do not be arrogant, but tremble.",
      "T": "Fair enough. They were broken off because of unbelief, and you stand in place through faith. So do not be proud—be afraid instead."
    },
    "21": {
      "L": "for if God did not spare the natural branches, he will not spare you either.",
      "M": "For if God did not spare the natural branches, he will not spare you either.",
      "T": "For if God did not hold back from cutting off the natural branches, he will not hold back from cutting you off either."
    },
    "22": {
      "L": "Behold then the kindness and severity of God; to those who fell, severity, but to you, the kindness of God, if you continue in his kindness; otherwise you also will be cut off.",
      "M": "Consider therefore the kindness and sternness of God: sternness to those who fell, but kindness to you, provided that you continue in his kindness. Otherwise, you also will be cut off.",
      "T": "Take a good look at both sides of God: his severe judgment toward those who fell, and his remarkable kindness toward you—provided you remain in that kindness. If you don't, you too will be cut off."
    },
    "23": {
      "L": "And they also, if they do not continue in their unbelief, will be grafted in; for God is able to graft them in again.",
      "M": "And if they do not persist in unbelief, they will be grafted in, for God is able to graft them in again.",
      "T": "And those branches, if they turn from their unbelief, will be grafted back in—because God has the power to graft them in again."
    },
    "24": {
      "L": "For if you were cut out of the olive tree that is wild by nature and were grafted contrary to nature into the cultivated olive tree, how much more will these who are the natural branches be grafted into their own olive tree?",
      "M": "After all, if you were cut out of an olive tree that is wild by nature, and contrary to nature were grafted into a cultivated olive tree, how much more readily will these, the natural branches, be grafted into their own olive tree!",
      "T": "After all—if you were cut from a naturally wild olive tree and grafted, contrary to nature, into the cultivated one—how much easier it will be for the natural branches to be grafted back into their own tree!"
    },
    "25": {
      "L": "For I do not want you to be uninformed, brothers, of this mystery—lest you be wise in your own sight—that a partial hardening has happened to Israel until the fullness of the Gentiles has come in.",
      "M": "I do not want you to be ignorant of this mystery, brothers and sisters, so that you may not be conceited: Israel has experienced a hardening in part until the full number of the Gentiles has come in,",
      "T": "I want you to understand this mystery, brothers and sisters, so that you don't become smug: a partial hardening has settled over Israel—but only until the full number of the Gentiles has come in."
    },
    "26": {
      "L": "and so all Israel will be saved; just as it is written, 'The Deliverer will come from Zion; he will remove ungodliness from Jacob;'",
      "M": "and in this way all Israel will be saved. As it is written: 'The deliverer will come from Zion; he will turn godlessness away from Jacob.'",
      "T": "And in this way, all Israel will be saved. As scripture says: 'The Deliverer will come from Zion—he will drive away all ungodliness from Jacob.'"
    },
    "27": {
      "L": "'And this is my covenant with them, when I take away their sins.'",
      "M": "'And this is my covenant with them when I take away their sins.'",
      "T": "'And this is the covenant I will make with them when I remove their sins.'"
    },
    "28": {
      "L": "Regarding the gospel, they are enemies for your sake; but regarding the election, they are beloved for the sake of the fathers.",
      "M": "As far as the gospel is concerned, they are enemies for your sake; but as far as election is concerned, they are loved on account of the patriarchs,",
      "T": "In terms of the gospel, they are at odds with God—for your benefit. But in terms of God's choosing, they are still loved—for the sake of the patriarchs."
    },
    "29": {
      "L": "for the gifts and the calling of God are irrevocable.",
      "M": "for God's gifts and his call are irrevocable.",
      "T": "Because God never takes back what he gives or withdraws the call he has issued."
    },
    "30": {
      "L": "For just as you once were disobedient to God, but now have been shown mercy because of their disobedience,",
      "M": "Just as you who were at one time disobedient to God have now received mercy as a result of their disobedience,",
      "T": "Just as you once were disobedient to God and have now received mercy through their disobedience—"
    },
    "31": {
      "L": "so also these now have been disobedient, in order that by the mercy shown to you they also may now be shown mercy.",
      "M": "so they too have now become disobedient in order that they too may now receive mercy as a result of God's mercy to you.",
      "T": "—so also they have now been disobedient, so that by the mercy God has shown you they too might now receive mercy."
    },
    "32": {
      "L": "For God has shut up all in disobedience that he might show mercy to all.",
      "M": "For God has bound everyone over to disobedience so that he may have mercy on them all.",
      "T": "For God has confined everyone to disobedience—so that he might show mercy to everyone."
    },
    "33": {
      "L": "O the depth of the riches both of the wisdom and knowledge of God! How unsearchable are his judgments and unfathomable his ways!",
      "M": "Oh, the depth of the riches of the wisdom and knowledge of God! How unsearchable his judgments, and his paths beyond tracing out!",
      "T": "What a depth of wealth and wisdom and knowledge lies in God! How impossible to trace his judgments! How untraceable his paths!"
    },
    "34": {
      "L": "'For who has known the mind of the Lord, or who became his counselor?'",
      "M": "'Who has known the mind of the Lord? Or who has been his counselor?'",
      "T": "'Who has ever understood the mind of the Lord? Who has ever been his advisor?'"
    },
    "35": {
      "L": "'Or who has first given to him that he should be repaid?'",
      "M": "'Who has ever given to God, that God should repay them?'",
      "T": "'Who has ever given God anything, as if he owed them something in return?'"
    },
    "36": {
      "L": "For from him and through him and to him are all things. To him be the glory forever. Amen.",
      "M": "For from him and through him and for him are all things. To him be the glory forever! Amen.",
      "T": "Everything comes from him, exists through him, and returns to him. To him be glory forever! Amen."
    }
  },
  "12": {
    "1": {
      "L": "Therefore I urge you, brothers, by the mercies of God, to present your bodies as a living sacrifice, holy and acceptable to God, which is your reasonable worship.",
      "M": "Therefore, I urge you, brothers and sisters, in view of God's mercy, to offer your bodies as a living sacrifice, holy and pleasing to God—this is your true and proper worship.",
      "T": "In light of all these mercies of God, I urge you, brothers and sisters, to offer your bodies as living sacrifices—holy and pleasing to God. This is the worship that truly makes sense."
    },
    "2": {
      "L": "And do not be conformed to this age, but be transformed by the renewing of your mind, so that you may prove what the will of God is, that which is good and acceptable and perfect.",
      "M": "Do not conform to the pattern of this world, but be transformed by the renewing of your mind. Then you will be able to test and approve what God's will is—his good, pleasing and perfect will.",
      "T": "Stop being shaped by the mold of this present age—instead, let God reshape you from the inside by renewing your thinking. Then you will be able to discern what God's will actually is: what is good, what pleases him, what is complete."
    },
    "3": {
      "L": "For through the grace given to me I say to everyone among you not to think of himself more highly than he ought to think, but to think so as to have sound judgment, as God has allotted to each a measure of faith.",
      "M": "For by the grace given me I say to every one of you: Do not think of yourself more highly than you ought, but rather think of yourself with sober judgment, in accordance with the faith God has distributed to each of you.",
      "T": "By the grace God has given me I say to each of you: don't overestimate yourself. Form a sober, accurate self-assessment—in line with the measure of faith God has given you."
    },
    "4": {
      "L": "For just as we have many members in one body and all the members do not have the same function,",
      "M": "For just as each of us has one body with many members, and these members do not all have the same function,",
      "T": "Just as a single body has many parts—and those parts don't all do the same thing—"
    },
    "5": {
      "L": "so we who are many are one body in Christ, and individually members of one another.",
      "M": "so in Christ we, though many, form one body, and each member belongs to all the others.",
      "T": "—so we, though many, form one body in Christ, and each of us belongs to all the others."
    },
    "6": {
      "L": "Having gifts that differ according to the grace given to us, let us use them: if prophecy, in proportion to our faith;",
      "M": "We have different gifts, according to the grace given to each of us. If your gift is prophesying, then prophesy in accordance with your faith;",
      "T": "We each have different grace-gifts, given according to what God has given us. If your gift is prophecy, use it in proportion to your faith."
    },
    "7": {
      "L": "if service, in the serving; if the one who teaches, in the teaching;",
      "M": "if it is serving, then serve; if it is teaching, then teach;",
      "T": "If it is serving, then serve. If it is teaching, then teach."
    },
    "8": {
      "L": "if the one who exhorts, in the exhortation; the one who gives, with generosity; the one who leads, with diligence; the one who shows mercy, with cheerfulness.",
      "M": "if it is to encourage, then give encouragement; if it is giving, then give generously; if it is to lead, do it diligently; if it is to show mercy, do it cheerfully.",
      "T": "If it is encouraging others, then encourage. If it is giving, give with open-handed generosity. If it is leading, lead with energy. If it is showing kindness, do it with a smile."
    },
    "9": {
      "L": "Let love be without hypocrisy. Abhor what is evil; cling to what is good.",
      "M": "Love must be sincere. Hate what is evil; cling to what is good.",
      "T": "Love must be real—no play-acting. Hate evil with everything in you; hold tightly to what is good."
    },
    "10": {
      "L": "Be devoted to one another in brotherly love; give preference to one another in honor;",
      "M": "Be devoted to one another in love. Honor one another above yourselves.",
      "T": "Love one another with the deep affection of family. Try to outdo each other in showing respect."
    },
    "11": {
      "L": "not lagging in diligence, fervent in spirit, serving the Lord;",
      "M": "Never be lacking in zeal, but keep your spiritual fervor, serving the Lord.",
      "T": "Don't drag your feet in your work—keep your passion burning, serving the Lord."
    },
    "12": {
      "L": "rejoicing in hope, enduring in tribulation, devoted in prayer;",
      "M": "Be joyful in hope, patient in affliction, faithful in prayer.",
      "T": "Be full of joy in hope, steady in suffering, persistent in prayer."
    },
    "13": {
      "L": "contributing to the needs of the saints, pursuing hospitality.",
      "M": "Share with the Lord's people who are in need. Practice hospitality.",
      "T": "Share what you have with God's people who are in need. Make hospitality a habit."
    },
    "14": {
      "L": "Bless those who persecute you; bless and do not curse.",
      "M": "Bless those who persecute you; bless and do not curse.",
      "T": "When people persecute you, bless them—bless, don't curse."
    },
    "15": {
      "L": "Rejoice with those who rejoice, and weep with those who weep.",
      "M": "Rejoice with those who rejoice; mourn with those who mourn.",
      "T": "Celebrate with those who are celebrating; grieve with those who grieve."
    },
    "16": {
      "L": "Be of the same mind toward one another; do not be haughty in mind but associate with the lowly. Do not be wise in your own sight.",
      "M": "Live in harmony with one another. Do not be proud, but be willing to associate with people of low position. Do not be conceited.",
      "T": "Live in harmony with one another. Don't be too proud for humble company—get alongside those of low status. Never become wise in your own estimation."
    },
    "17": {
      "L": "Repay no one evil for evil; take thought for what is honorable in the sight of all people.",
      "M": "Do not repay anyone evil for evil. Be careful to do what is right in the eyes of everyone.",
      "T": "Never pay back evil with evil. Think ahead about what will be seen as honorable by everyone."
    },
    "18": {
      "L": "If possible, as far as it depends on you, be at peace with all people.",
      "M": "If it is possible, as far as it depends on you, live at peace with everyone.",
      "T": "As much as it depends on you, live peaceably with everyone."
    },
    "19": {
      "L": "Beloved, do not avenge yourselves, but give place to wrath; for it is written, 'Vengeance is mine, I will repay, says the Lord.'",
      "M": "Do not take revenge, my dear friends, but leave room for God's wrath, for it is written: 'It is mine to avenge; I will repay,' says the Lord.",
      "T": "Dear friends, never take revenge. Leave room for God's wrath—for it is written: 'Vengeance is mine; I will repay, says the Lord.'"
    },
    "20": {
      "L": "'But if your enemy is hungry, feed him; if he is thirsty, give him a drink; for by doing this you will heap burning coals on his head.'",
      "M": "On the contrary: 'If your enemy is hungry, feed him; if he is thirsty, give him something to drink. In doing this, you will heap burning coals on his head.'",
      "T": "No—instead: 'If your enemy is hungry, feed him. If he is thirsty, give him a drink. Doing this will pile burning coals on his head.'"
    },
    "21": {
      "L": "Do not be overcome by evil, but overcome evil with good.",
      "M": "Do not be overcome by evil, but overcome evil with good.",
      "T": "Don't let evil get the upper hand—get the upper hand over evil by doing good."
    }
  },
  "13": {
    "1": {
      "L": "Every person must be subject to the governing authorities; for there is no authority except from God, and the authorities that exist have been instituted by God.",
      "M": "Let everyone be subject to the governing authorities, for there is no authority except that which God has established. The authorities that exist have been established by God.",
      "T": "Every person should be subject to those in authority over them. There is no authority that does not ultimately come from God—the authorities that exist are placed there by God."
    },
    "2": {
      "L": "Therefore whoever resists the authority has opposed the ordinance of God; and those who have opposed will receive condemnation upon themselves.",
      "M": "Consequently, whoever rebels against the authority is rebelling against what God has instituted, and those who do so will bring judgment on themselves.",
      "T": "So whoever resists the authority is resisting God's ordering of things—and those who resist will bring judgment down on themselves."
    },
    "3": {
      "L": "For rulers are not a cause of fear for the good work, but for the evil. Do you want to have no fear of authority? Do what is good and you will have praise from it;",
      "M": "For rulers hold no terror for those who do right, but for those who do wrong. Do you want to be free from fear of the one in authority? Then do what is right and you will be commended.",
      "T": "Rulers are not a threat to people who do good—only to those who do wrong. Want to live without fear of the authorities? Then do what is right, and you will have their approval."
    },
    "4": {
      "L": "for it is a servant of God to you for your good. But if you do what is evil, be afraid; for it does not bear the sword in vain; for it is a servant of God, an avenger for wrath upon the one who practices evil.",
      "M": "For the one in authority is God's servant for your good. But if you do wrong, be afraid, for rulers do not bear the sword for no reason. They are God's servants, agents of wrath to bring punishment on the wrongdoer.",
      "T": "The authority is God's appointed servant working for your benefit. But if you are doing wrong, be afraid—the sword is not carried for nothing. That authority is God's agent, executing his judgment on the wrongdoer."
    },
    "5": {
      "L": "Therefore it is necessary to be subject, not only because of wrath, but also for the sake of conscience.",
      "M": "Therefore, it is necessary to submit to the authorities, not only because of possible punishment but also as a matter of conscience.",
      "T": "So there are two reasons to submit: to avoid punishment, yes, but also because it is the right thing to do before God."
    },
    "6": {
      "L": "For because of this you also pay taxes; for they are servants of God, devoting themselves to this very thing.",
      "M": "This is also why you pay taxes, for the authorities are God's servants, who give their full time to governing.",
      "T": "This is also why you pay taxes—because the authorities are God's public servants, devoting themselves to this work."
    },
    "7": {
      "L": "Render to all what is due them: tax to whom tax is due; custom to whom custom; fear to whom fear; honor to whom honor.",
      "M": "Give to everyone what you owe them: If you owe taxes, pay taxes; if revenue, then revenue; if respect, then respect; if honor, then honor.",
      "T": "Pay what you owe everyone: taxes to the tax authorities, revenue to those who collect it, respect to those who deserve respect, honor to those who deserve honor."
    },
    "8": {
      "L": "Owe nothing to anyone except to love one another; for the one who loves the other has fulfilled the law.",
      "M": "Let no debt remain outstanding, except the continuing debt to love one another, for whoever loves others has fulfilled the law.",
      "T": "Don't leave any debt unpaid—except the debt of love you owe each other, which you can never fully repay. For the person who loves others has fulfilled the Law."
    },
    "9": {
      "L": "For this, 'You shall not commit adultery, you shall not murder, you shall not steal, you shall not covet,' and if there is any other commandment, it is summed up in this word: 'You shall love your neighbor as yourself.'",
      "M": "The commandments, 'You shall not commit adultery,' 'You shall not murder,' 'You shall not steal,' 'You shall not covet,' and whatever other command there may be, are summed up in this one command: 'Love your neighbor as yourself.'",
      "T": "The commandments—'Don't commit adultery,' 'Don't murder,' 'Don't steal,' 'Don't covet'—and any other commandment you can think of—are all summed up in this one: 'Love your neighbor as yourself.'"
    },
    "10": {
      "L": "Love does no wrong to a neighbor; therefore love is the fulfillment of the law.",
      "M": "Love does no harm to a neighbor. Therefore love is the fulfillment of the law.",
      "T": "Love never wrongs its neighbor. That is why love is the fulfillment of the whole Law."
    },
    "11": {
      "L": "And this, knowing the time, that it is already the hour for you to awaken from sleep; for now our salvation is nearer than when we believed.",
      "M": "And do this, understanding the present time: the hour has already come for you to wake up from your slumber, because our salvation is nearer now than when we first believed.",
      "T": "Do all this aware of the hour—it is already time to wake from sleep! Our final salvation is closer now than when we first believed."
    },
    "12": {
      "L": "The night is almost gone, and the day is near. Let us therefore lay aside the deeds of darkness and put on the armor of light.",
      "M": "The night is nearly over; the day is almost here. So let us put aside the deeds of darkness and put on the armor of light.",
      "T": "The night is nearly over; the day is about to dawn. So let us strip off the deeds that belong to darkness and put on the full armor of light."
    },
    "13": {
      "L": "Let us walk properly as in the day, not in carousing and drunkenness, not in sexual immorality and sensuality, not in strife and jealousy.",
      "M": "Let us behave properly as in the daytime, not in carousing and drunkenness, not in sexual immorality and debauchery, not in dissension and jealousy.",
      "T": "Let us live as people do in the daylight—no wild parties or drunkenness, no sexual immorality or indecency, no quarreling or envy."
    },
    "14": {
      "L": "But put on the Lord Jesus Christ, and make no provision for the flesh in regard to its lusts.",
      "M": "Rather, clothe yourselves with the Lord Jesus Christ, and do not think about how to gratify the desires of the flesh.",
      "T": "Instead, clothe yourselves with the Lord Jesus Christ—and stop making plans to feed the cravings of the flesh."
    }
  },
  "14": {
    "1": {
      "L": "Now receive the one who is weak in faith, but not for the purpose of passing judgment on his opinions.",
      "M": "Accept the one whose faith is weak, without quarreling over disputable matters.",
      "T": "Welcome the person whose faith is still fragile—but not in order to argue about their views."
    },
    "2": {
      "L": "One person has faith to eat all things, but he who is weak eats only vegetables.",
      "M": "One person's faith allows them to eat anything, but another, whose faith is weak, eats only vegetables.",
      "T": "One person's faith lets them eat anything; another, whose faith is weaker, eats only vegetables."
    },
    "3": {
      "L": "Let not the one who eats regard with contempt the one who does not eat, and let not the one who does not eat judge the one who eats, for God has received him.",
      "M": "The one who eats everything must not treat with contempt the one who does not, and the one who does not eat everything must not judge the one who does, for God has accepted them.",
      "T": "The person who eats everything must not look down on the one who doesn't. And the one who abstains must not condemn the one who eats—because God has accepted that person."
    },
    "4": {
      "L": "Who are you to judge the servant of another? To his own master he stands or falls; and he will be made to stand, for the Lord is able to make him stand.",
      "M": "Who are you to judge someone else's servant? To their own master, servants stand or fall. And they will stand, for the Lord is able to make them stand.",
      "T": "Who are you to judge someone else's household servant? Whether they stand or fall is their master's business—and they will stand, because the Lord is able to hold them up."
    },
    "5": {
      "L": "One person judges one day as more important than another; another judges every day alike. Each person must be fully convinced in his own mind.",
      "M": "One person considers one day more sacred than another; another considers every day alike. Each of them should be fully convinced in their own mind.",
      "T": "One person regards one day as more sacred than another; another person considers every day the same. Each should be fully satisfied in their own conviction."
    },
    "6": {
      "L": "He who observes the day observes it to the Lord, and he who eats does so to the Lord, for he gives thanks to God; and he who does not eat abstains to the Lord and gives thanks to God.",
      "M": "Whoever regards one day as special does so to the Lord. Whoever eats meat does so to the Lord, for they give thanks to God; and whoever abstains does so to the Lord and gives thanks to God.",
      "T": "The person who treats a certain day as special does so for the Lord. The person who eats does so for the Lord—giving thanks to God. And the person who abstains also does so for the Lord—and gives thanks to God."
    },
    "7": {
      "L": "For none of us lives to himself and none of us dies to himself.",
      "M": "For none of us lives for ourselves alone, and none of us dies for ourselves alone.",
      "T": "None of us lives for themselves alone, and none of us dies for themselves alone."
    },
    "8": {
      "L": "For if we live, we live to the Lord, and if we die, we die to the Lord; therefore whether we live or die, we are the Lord's.",
      "M": "If we live, we live for the Lord; and if we die, we die for the Lord. So, whether we live or die, we belong to the Lord.",
      "T": "If we live, we live for the Lord. If we die, we die for the Lord. Whether we live or die, we belong to the Lord."
    },
    "9": {
      "L": "For to this end Christ died and came to life again, that he might be Lord of both the dead and the living.",
      "M": "For this very reason, Christ died and returned to life so that he might be the Lord of both the dead and the living.",
      "T": "This is precisely why Christ died and rose again—to become Lord over both the dead and the living."
    },
    "10": {
      "L": "But you, why do you judge your brother? Or you also, why do you regard your brother with contempt? For we will all stand before the judgment seat of God.",
      "M": "You, then, why do you judge your brother or sister? Or why do you treat them with contempt? For we will all stand before God's judgment seat.",
      "T": "So why do you judge your fellow believer? Or why do you look down on them? We will all stand before God's judgment seat."
    },
    "11": {
      "L": "For it is written, 'As I live, says the Lord, every knee will bow to me, and every tongue will give praise to God.'",
      "M": "It is written: 'As surely as I live,' says the Lord, 'every knee will bow before me; every tongue will acknowledge God.'",
      "T": "As scripture says: 'As I live, says the Lord, every knee will bow before me, and every tongue will openly acknowledge God.'"
    },
    "12": {
      "L": "So then each of us will give account of himself to God.",
      "M": "So then, each of us will give an account of ourselves to God.",
      "T": "So each of us will give a personal account to God."
    },
    "13": {
      "L": "Therefore let us no longer judge one another, but rather determine this: not to place a stumbling block or an obstacle in a brother's way.",
      "M": "Therefore let us stop passing judgment on one another. Instead, make up your mind not to put any stumbling block or obstacle in the way of a brother or sister.",
      "T": "So let's stop judging one another. Instead, make this your firm decision: never put a stumbling block in a fellow believer's path."
    },
    "14": {
      "L": "I know and am persuaded in the Lord Jesus that nothing is unclean in itself; but to him who considers anything to be unclean, to that person it is unclean.",
      "M": "I am convinced, being fully persuaded in the Lord Jesus, that nothing is unclean in itself. But if anyone regards something as unclean, then for that person it is unclean.",
      "T": "I am fully convinced in the Lord Jesus that nothing is unclean in itself. But if someone considers a thing unclean, then for that person it is unclean."
    },
    "15": {
      "L": "For if because of food your brother is being hurt, you are no longer walking according to love. Do not destroy with your food the one for whom Christ died.",
      "M": "If your brother or sister is distressed because of what you eat, you are no longer acting in love. Do not by your eating destroy someone for whom Christ died.",
      "T": "If what you eat causes your brother or sister pain, you are no longer walking in love. Do not—over a food choice—destroy someone for whom Christ died."
    },
    "16": {
      "L": "Therefore do not let what you regard as good be spoken of as evil;",
      "M": "Therefore do not let what you know is good be spoken of as evil.",
      "T": "Don't let something you consider good acquire a reputation for evil."
    },
    "17": {
      "L": "for the kingdom of God is not eating and drinking, but righteousness and peace and joy in the Holy Spirit.",
      "M": "For the kingdom of God is not a matter of eating and drinking, but of righteousness, peace and joy in the Holy Spirit,",
      "T": "Because the reign of God is not about what you eat or drink—it is about right living, peace, and joy in the Holy Spirit."
    },
    "18": {
      "L": "for he who serves Christ in this is pleasing to God and approved by men.",
      "M": "because anyone who serves Christ in this way is pleasing to God and receives human approval.",
      "T": "Whoever serves Christ in these things is pleasing to God and respected by people."
    },
    "19": {
      "L": "So then let us pursue the things that make for peace and the things that build up one another.",
      "M": "Let us therefore make every effort to do what leads to peace and to mutual edification.",
      "T": "So let's go after the things that make for peace and build each other up."
    },
    "20": {
      "L": "Do not tear down the work of God for the sake of food. All things indeed are clean, but they are evil for the man who eats with causing offense.",
      "M": "Do not destroy the work of God for the sake of food. All food is clean, but it is wrong for a person to eat anything that causes someone else to stumble.",
      "T": "Don't tear down God's work for the sake of a meal. Everything is clean—but it is wrong to eat in a way that causes someone to stumble."
    },
    "21": {
      "L": "It is good not to eat meat or to drink wine or to do anything by which your brother stumbles.",
      "M": "It is better not to eat meat or drink wine or to do anything else that will cause your brother or sister to fall.",
      "T": "The right thing is to avoid meat or wine or anything else that would cause your brother or sister to fall."
    },
    "22": {
      "L": "The faith which you have, have according to yourself before God. Blessed is the one who does not condemn himself in what he approves.",
      "M": "So whatever you believe about these things keep between yourself and God. Blessed is the one who does not condemn himself by what he approves.",
      "T": "Whatever you believe about these matters, hold it as a private conviction before God. Happy is the person who has no reason to condemn themselves in what they decide."
    },
    "23": {
      "L": "But the one who doubts is condemned if he eats, because it is not from faith; and whatever is not from faith is sin.",
      "M": "But whoever has doubts is condemned if they eat, because their eating is not from faith; and everything that does not come from faith is sin.",
      "T": "But if someone eats while having doubts, they are condemned—because their eating does not flow from faith. And anything that does not flow from faith is sin."
    }
  },
  "15": {
    "1": {
      "L": "Now we who are strong ought to bear the weaknesses of those without strength, and not merely to please ourselves.",
      "M": "We who are strong ought to bear with the failings of the weak and not to please ourselves.",
      "T": "We who are strong have an obligation to carry the weight of the weaknesses of those who are not—and not simply to please ourselves."
    },
    "2": {
      "L": "Each of us is to please his neighbor for his good, to his edification.",
      "M": "Each of us should please our neighbors for their good, to build them up.",
      "T": "Each of us should think about how to please our neighbor—for their benefit, to build them up."
    },
    "3": {
      "L": "For even Christ did not please himself; but as it is written, 'The reproaches of those who reproached you fell on me.'",
      "M": "For even Christ did not please himself but, as it is written: 'The insults of those who insult you have fallen on me.'",
      "T": "Even Christ did not live to please himself. As scripture says: 'The insults people hurled at you fell on me instead.'"
    },
    "4": {
      "L": "For whatever was written in earlier times was written for our instruction, so that through perseverance and the encouragement of the Scriptures we might have hope.",
      "M": "For everything that was written in the past was written to teach us, so that through the endurance taught in the Scriptures and the encouragement they provide we might have hope.",
      "T": "Everything written in earlier times was written for our instruction—so that through the endurance and encouragement that come from the scriptures we might hold on to hope."
    },
    "5": {
      "L": "Now may the God of perseverance and encouragement grant you to be of the same mind with one another according to Christ Jesus,",
      "M": "May the God who gives endurance and encouragement give you the same attitude of mind toward each other that Christ Jesus had,",
      "T": "May the God who gives endurance and encouragement grant you a spirit of unity among yourselves in line with Christ Jesus—"
    },
    "6": {
      "L": "so that with one accord you may with one voice glorify the God and Father of our Lord Jesus Christ.",
      "M": "so that with one mind and one voice you may glorify the God and Father of our Lord Jesus Christ.",
      "T": "—so that with one heart and one voice you may together glorify the God and Father of our Lord Jesus Christ."
    },
    "7": {
      "L": "Therefore, accept one another, just as Christ also accepted us, to the glory of God.",
      "M": "Accept one another, then, just as Christ accepted you, in order to bring praise to God.",
      "T": "So welcome one another just as Christ has welcomed you—all to the glory of God."
    },
    "8": {
      "L": "For I say that Christ has become a servant to the circumcision on behalf of the truth of God, in order to confirm the promises given to the fathers,",
      "M": "For I tell you that Christ has become a servant of the Jews on behalf of God's truth, so that the promises made to the patriarchs might be confirmed",
      "T": "For I tell you this: Christ became a servant to the Jewish people to demonstrate God's faithfulness—to confirm the promises God had made to their ancestors—"
    },
    "9": {
      "L": "and that the Gentiles might glorify God for his mercy; as it is written, 'Therefore I will give praise to you among the Gentiles, and I will sing to your name.'",
      "M": "and, moreover, that the Gentiles might glorify God for his mercy. As it is written: 'Therefore I will praise you among the Gentiles; I will sing the praises of your name.'",
      "T": "—and also so that the Gentiles might glorify God for his mercy. As scripture says: 'Therefore I will praise you among the Gentiles and sing in honor of your name.'"
    },
    "10": {
      "L": "And again he says, 'Rejoice, O Gentiles, with his people.'",
      "M": "Again, it says, 'Rejoice, you Gentiles, with his people.'",
      "T": "And again: 'Rejoice, you Gentiles, together with his people.'"
    },
    "11": {
      "L": "And again, 'Praise the Lord all you Gentiles, and let all the peoples praise him.'",
      "M": "And again, 'Praise the Lord, all you Gentiles; let all the peoples extol him.'",
      "T": "And again: 'Praise the Lord, all you Gentiles—let all peoples join in his praise.'"
    },
    "12": {
      "L": "Again, Isaiah says, 'There will come the root of Jesse, and he who arises to rule over the Gentiles; in him will the Gentiles hope.'",
      "M": "And again, Isaiah says, 'The Root of Jesse will spring up, one who will arise to rule over the nations; in him the Gentiles will hope.'",
      "T": "And Isaiah says: 'The Root of Jesse will appear—the one who rises to rule over the nations. In him the Gentiles will place their hope.'"
    },
    "13": {
      "L": "Now may the God of hope fill you with all joy and peace in believing, so that you may overflow in hope by the power of the Holy Spirit.",
      "M": "May the God of hope fill you with all joy and peace as you trust in him, so that you may overflow with hope by the power of the Holy Spirit.",
      "T": "May the God of hope fill you with complete joy and peace as you trust him—so that you overflow with hope by the power of the Holy Spirit."
    },
    "14": {
      "L": "And I myself also am persuaded about you, my brothers, that you yourselves are full of goodness, filled with all knowledge, and able also to admonish one another.",
      "M": "I myself am convinced, my brothers and sisters, that you yourselves are full of goodness, filled with knowledge and competent to instruct one another.",
      "T": "I am personally convinced about you, brothers and sisters—that you are full of goodness, rich in knowledge, and well able to guide one another."
    },
    "15": {
      "L": "But I have written to you more boldly on some points, by way of reminder, because of the grace given to me by God,",
      "M": "Yet I have written you quite boldly on some points to remind you of them again, because of the grace God gave me",
      "T": "Still, I have written to you with some boldness on certain points—simply to refresh your memory—because of the grace God has given me:"
    },
    "16": {
      "L": "to be a minister of Christ Jesus to the Gentiles, serving as a priest of the gospel of God, so that the offering of the Gentiles may become acceptable, sanctified by the Holy Spirit.",
      "M": "to be a minister of Christ Jesus to the Gentiles. He gave me the priestly duty of proclaiming the gospel of God, so that the Gentiles might become an offering acceptable to God, sanctified by the Holy Spirit.",
      "T": "—to be a minister of Christ Jesus to the Gentiles, carrying out a priestly service of the gospel of God, so that the Gentiles might be presented to God as an acceptable offering, made holy by the Holy Spirit."
    },
    "17": {
      "L": "Therefore in Christ Jesus I have found reason for boasting in things pertaining to God.",
      "M": "Therefore I glory in Christ Jesus in my service to God.",
      "T": "In Christ Jesus I have grounds to boast about what I have done in God's service."
    },
    "18": {
      "L": "For I will not presume to speak of anything except what Christ has accomplished through me, resulting in the obedience of the Gentiles by word and deed,",
      "M": "I will not venture to speak of anything except what Christ has accomplished through me in leading the Gentiles to obey God by what I have said and done—",
      "T": "I will say nothing except what Christ has accomplished through me—bringing the Gentiles to obedience by what I have said and done—"
    },
    "19": {
      "L": "in the power of signs and wonders, in the power of the Spirit of God; so that from Jerusalem and around as far as Illyricum, I have fully preached the gospel of Christ.",
      "M": "by the power of signs and wonders, through the power of the Spirit of God. So from Jerusalem all the way around to Illyricum, I have fully proclaimed the gospel of Christ.",
      "T": "—through the power of signs and miracles, through the power of the Spirit of God. So from Jerusalem all the way round to Illyricum, I have brought the gospel of Christ to its full scope."
    },
    "20": {
      "L": "And so I have aspired to preach the gospel, not where Christ was already named, so that I would not build on another's foundation;",
      "M": "It has always been my ambition to preach the gospel where Christ was not known, so that I would not be building on someone else's foundation.",
      "T": "My ambition has always been to announce the good news where Christ has not yet been named—I have no desire to build on someone else's foundation."
    },
    "21": {
      "L": "but as it is written, 'They who had no news of him will see, and they who have not heard will understand.'",
      "M": "Rather, as it is written: 'Those who were not told about him will see, and those who have not heard will understand.'",
      "T": "As scripture says: 'Those who had never been told about him will see him—and those who never heard will understand.'"
    },
    "22": {
      "L": "For this reason I have also been prevented many times from coming to you.",
      "M": "This is why I have often been hindered from coming to you.",
      "T": "This is why I have been hindered so many times from coming to you."
    },
    "23": {
      "L": "But now, with no further place for me in these regions, and having longed for many years to come to you,",
      "M": "But now that there is no more place for me to work in these regions, and since I have been longing for many years to visit you,",
      "T": "But now I have no more room to work in these regions—and I have been longing to come to you for many years."
    },
    "24": {
      "L": "whenever I go to Spain—for I hope to see you in passing, and to be helped on my way there by you, when I have first enjoyed your company for a while—",
      "M": "I plan to do so when I go to Spain. I hope to see you while passing through and to have you assist me on my journey there, after I have enjoyed your company for a while.",
      "T": "I'm planning to pass through on my way to Spain—I hope to see you as I travel through and, after enjoying your company for a while, to have your help continuing the journey."
    },
    "25": {
      "L": "but now I am going to Jerusalem, serving the saints.",
      "M": "Now, however, I am on my way to Jerusalem in the service of the Lord's people there.",
      "T": "But right now I am heading to Jerusalem in service to God's people there."
    },
    "26": {
      "L": "For Macedonia and Achaia were pleased to make some contribution for the poor among the saints who are in Jerusalem.",
      "M": "For Macedonia and Achaia were pleased to make a contribution for the poor among the Lord's people in Jerusalem.",
      "T": "Macedonia and Achaia have generously decided to make a contribution for the poor among God's people in Jerusalem."
    },
    "27": {
      "L": "Yes, they were pleased to do so, and they are debtors to them. For if the Gentiles have shared in their spiritual things, they are obligated also to minister to them in material things.",
      "M": "They were pleased to do it, and indeed they owe it to them. For if the Gentiles have shared in the Jews' spiritual blessings, they owe it to the Jews to share with them their material blessings.",
      "T": "They were happy to do it—and in truth they owe it. For if the Gentiles have come to share in the spiritual riches of Jerusalem, they in turn ought to give back by sharing their material resources."
    },
    "28": {
      "L": "Therefore, when I have finished this and have put my seal on this fruit of theirs, I will go on by way of you to Spain.",
      "M": "So after I have completed this task and have made sure they have received this contribution, I will go to Spain and visit you on the way.",
      "T": "So once I have finished this task and made sure this gift has been safely delivered, I will head for Spain—and pass through to see you."
    },
    "29": {
      "L": "And I know that when I come to you, I will come in the fullness of the blessing of Christ.",
      "M": "I know that when I come to you, I will come in the full measure of the blessing of Christ.",
      "T": "And I know that when I do come to you, I will arrive in the full blessing of Christ."
    },
    "30": {
      "L": "Now I urge you, brothers, by our Lord Jesus Christ and by the love of the Spirit, to strive together with me in your prayers to God on my behalf,",
      "M": "I urge you, brothers and sisters, by our Lord Jesus Christ and by the love of the Spirit, to join me in my struggle by praying to God for me.",
      "T": "I urge you, brothers and sisters, by our Lord Jesus Christ and by the love the Spirit produces, to fight alongside me in your prayers to God on my behalf."
    },
    "31": {
      "L": "that I may be rescued from those who are disobedient in Judea, and that my service for Jerusalem may prove acceptable to the saints,",
      "M": "Pray that I may be kept safe from the unbelievers in Judea and that the contribution I take to Jerusalem may be favorably received by the Lord's people there,",
      "T": "Pray that I will be kept safe from those who oppose God in Judea—and that the gift I am bringing to Jerusalem will be warmly received by God's people there."
    },
    "32": {
      "L": "so that I may come to you with joy by the will of God and be refreshed together with you.",
      "M": "so that I may come to you with joy, by God's will, and in your company be refreshed.",
      "T": "Then, if God wills, I can come to you with joy and we can be refreshed and encouraged together."
    },
    "33": {
      "L": "Now the God of peace be with you all. Amen.",
      "M": "The God of peace be with you all. Amen.",
      "T": "May the God of peace be with all of you. Amen."
    }
  },
  "16": {
    "1": {
      "L": "I commend to you Phoebe our sister, who is a servant of the church which is at Cenchreae,",
      "M": "I commend to you our sister Phoebe, a deacon of the church in Cenchreae.",
      "T": "I want to introduce to you our sister Phoebe, who serves as a minister of the church at Cenchreae."
    },
    "2": {
      "L": "that you receive her in the Lord in a manner worthy of the saints, and that you assist her in whatever matter she may have need of you; for she herself has also been a helper of many, and of myself as well.",
      "M": "I ask you to receive her in the Lord in a way worthy of his people and to give her any help she may need from you, for she has been the benefactor of many people, including me.",
      "T": "Welcome her in the Lord as befits God's people, and give her whatever help she needs from you—for she has been a patron and supporter to many, including me."
    },
    "3": {
      "L": "Greet Prisca and Aquila, my fellow workers in Christ Jesus,",
      "M": "Greet Priscilla and Aquila, my co-workers in Christ Jesus.",
      "T": "Give my greetings to Prisca and Aquila, my fellow workers in Christ Jesus."
    },
    "4": {
      "L": "who for my life risked their own necks, to whom not only I give thanks, but also all the churches of the Gentiles;",
      "M": "They risked their lives for me. Not only I but all the churches of the Gentiles are grateful to them.",
      "T": "They put their own necks on the line to save my life. Not just I but every Gentile church owes them gratitude."
    },
    "5": {
      "L": "also greet the church that is in their house. Greet Epaenetus, my beloved, who is the first convert to Christ from Asia.",
      "M": "Greet also the church that meets at their house. Greet my dear friend Epaenetus, who was the first convert to Christ in the province of Asia.",
      "T": "Greet also the congregation that meets in their home. Greet my dear Epaenetus—the very first person in the province of Asia to come to Christ."
    },
    "6": {
      "L": "Greet Mary, who has worked hard for you.",
      "M": "Greet Mary, who worked very hard for you.",
      "T": "Greet Mary, who worked extremely hard for your community."
    },
    "7": {
      "L": "Greet Andronicus and Junia, my kinsmen and my fellow prisoners, who are outstanding among the apostles, who also were in Christ before me.",
      "M": "Greet Andronicus and Junia, my fellow Jews who have been in prison with me. They are outstanding among the apostles, and they were in Christ before I was.",
      "T": "Greet Andronicus and Junia, my fellow Jews and fellow prisoners—outstanding in the eyes of the apostles, and believers in Christ before I was."
    },
    "8": {
      "L": "Greet Ampliatus, my beloved in the Lord.",
      "M": "Greet Ampliatus, my dear friend in the Lord.",
      "T": "Greet Ampliatus, whom I dearly love in the Lord."
    },
    "9": {
      "L": "Greet Urbanus, our fellow worker in Christ, and Stachys my beloved.",
      "M": "Greet Urbanus, our co-worker in Christ, and my dear friend Stachys.",
      "T": "Greet Urbanus, our fellow worker in Christ, and my dear Stachys."
    },
    "10": {
      "L": "Greet Apelles, the approved in Christ. Greet those who are of the household of Aristobulus.",
      "M": "Greet Apelles, whose fidelity to Christ has stood the test. Greet those who belong to the household of Aristobulus.",
      "T": "Greet Apelles, who has proved himself in Christ. Greet the household of Aristobulus."
    },
    "11": {
      "L": "Greet Herodion, my kinsman. Greet those of the household of Narcissus who are in the Lord.",
      "M": "Greet Herodion, my fellow Jew. Greet those in the household of Narcissus who are in the Lord.",
      "T": "Greet Herodion, my fellow Jew. Greet those members of the household of Narcissus who belong to the Lord."
    },
    "12": {
      "L": "Greet Tryphaena and Tryphosa, who labor in the Lord. Greet Persis the beloved, who has labored much in the Lord.",
      "M": "Greet Tryphena and Tryphosa, those women who work hard in the Lord. Greet my dear friend Persis, another woman who has worked very hard in the Lord.",
      "T": "Greet Tryphaena and Tryphosa, those hard workers for the Lord. Greet my dear Persis—another woman who has given herself tirelessly to work for the Lord."
    },
    "13": {
      "L": "Greet Rufus, chosen in the Lord, and his mother—and mine.",
      "M": "Greet Rufus, chosen in the Lord, and his mother, who has been a mother to me, too.",
      "T": "Greet Rufus, chosen by the Lord—and his mother, who has been like a mother to me as well."
    },
    "14": {
      "L": "Greet Asyncritus, Phlegon, Hermes, Patrobas, Hermas, and the brothers with them.",
      "M": "Greet Asyncritus, Phlegon, Hermes, Patrobas, Hermas and the other brothers and sisters with them.",
      "T": "Greet Asyncritus, Phlegon, Hermes, Patrobas, and Hermas—and the brothers and sisters who meet with them."
    },
    "15": {
      "L": "Greet Philologus and Julia, Nereus and his sister, and Olympas, and all the saints who are with them.",
      "M": "Greet Philologus, Julia, Nereus and his sister, and Olympas and all the Lord's people who are with them.",
      "T": "Greet Philologus and Julia, Nereus and his sister, and Olympas—and all of God's people who are with them."
    },
    "16": {
      "L": "Greet one another with a holy kiss. All the churches of Christ greet you.",
      "M": "Greet one another with a holy kiss. All the churches of Christ send greetings.",
      "T": "Greet one another with a holy kiss. All the churches of Christ send their greetings."
    },
    "17": {
      "L": "Now I urge you, brothers, to watch out for those who create divisions and stumbling blocks contrary to the teaching you have learned; turn away from them.",
      "M": "I urge you, brothers and sisters, to watch out for those who cause divisions and put obstacles in your way that are contrary to the teaching you have learned. Keep away from them.",
      "T": "I urge you, brothers and sisters, to watch out for those who cause divisions and put people off course—acting against the teaching you received. Stay away from them."
    },
    "18": {
      "L": "For such people do not serve our Lord Christ, but their own belly; and by smooth speech and flattering words they deceive the hearts of the unsuspecting.",
      "M": "For such people are not serving our Lord Christ, but their own appetites. By smooth talk and flattery they deceive the minds of naive people.",
      "T": "People like that are not serving Christ our Lord—they serve their own appetites. With plausible speech and flattery they lead astray the unsuspecting."
    },
    "19": {
      "L": "For the report of your obedience has reached all; therefore I rejoice over you. But I want you to be wise in what is good, and innocent in what is evil.",
      "M": "Everyone has heard about your obedience, so I rejoice because of you; but I want you to be wise about what is good, and innocent about what is evil.",
      "T": "Your obedience is known everywhere—I rejoice over you! But I want you to be wise about what is good, and to remain innocent of what is evil."
    },
    "20": {
      "L": "The God of peace will soon crush Satan under your feet. The grace of our Lord Jesus Christ be with you.",
      "M": "The God of peace will soon crush Satan under your feet. The grace of our Lord Jesus be with you.",
      "T": "The God of peace will soon crush Satan under your feet. May the grace of our Lord Jesus be with you."
    },
    "21": {
      "L": "Timothy my fellow worker greets you, and so do Lucius and Jason and Sosipater, my kinsmen.",
      "M": "Timothy, my co-worker, sends his greetings to you, as do Lucius, Jason and Sosipater, my fellow Jews.",
      "T": "Timothy, my fellow worker, sends his greetings. So do Lucius, Jason, and Sosipater, my fellow Jews."
    },
    "22": {
      "L": "I, Tertius, who wrote this letter, greet you in the Lord.",
      "M": "I, Tertius, who wrote down this letter, greet you in the Lord.",
      "T": "I, Tertius, who took down this letter, greet you in the Lord."
    },
    "23": {
      "L": "Gaius, who is host to me and to the whole church, greets you. Erastus, the city treasurer, greets you, and Quartus, the brother.",
      "M": "Gaius, whose hospitality I and the whole church here enjoy, sends you his greetings. Erastus, who is the city's director of public works, and our brother Quartus send you their greetings.",
      "T": "Gaius, who has opened his home to me and to the whole church, sends his greetings. Erastus, the city treasurer, and our brother Quartus also send their greetings."
    },
    "24": {
      "L": "The grace of our Lord Jesus Christ be with you all. Amen.",
      "M": "May the grace of our Lord Jesus Christ be with all of you. Amen.",
      "T": "May the grace of our Lord Jesus Christ be with all of you. Amen."
    },
    "25": {
      "L": "Now to him who is able to establish you according to my gospel and the preaching of Jesus Christ, according to the revelation of the mystery kept secret for long ages—",
      "M": "Now to him who is able to establish you in accordance with my gospel, the message I proclaim about Jesus Christ, in keeping with the revelation of the mystery hidden for long ages past,",
      "T": "Now to the one who has the power to establish you—in line with the good news I proclaim, the message about Jesus Christ, and in line with the unveiling of the mystery that was kept hidden through the ages—"
    },
    "26": {
      "L": "but now has been manifested, and through the prophetic Scriptures, according to the commandment of the eternal God, has been made known to all the nations, leading to obedience of faith—",
      "M": "but now revealed and made known through the prophetic writings by the command of the eternal God, so that all the Gentiles might come to the obedience that comes from faith—",
      "T": "—but has now been brought to light through the prophetic scriptures, at the command of the eternal God, made known to all nations to bring about the obedience of faith—"
    },
    "27": {
      "L": "to the only wise God, through Jesus Christ, be the glory forever. Amen.",
      "M": "to the only wise God be glory forever through Jesus Christ! Amen.",
      "T": "to the only wise God—through Jesus Christ—be glory forever and ever. Amen."
    }
  }
}

def main():
    for tier, key in [('literal','L'), ('mediating','M'), ('thought','T')]:
        existing = load(tier, 'romans')
        merge_tier(existing, ROMANS, key)
        save(tier, 'romans', existing)
    print('Done — Romans 9–16 written to all three tiers.')

if __name__ == '__main__':
    main()
