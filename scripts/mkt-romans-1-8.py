"""
MKT Romans chapters 1-8 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-romans-1-8.py

Key translation decisions:
- G4102 πίστις: "faith" throughout; "faithfulness of Jesus Christ" at 3:22, 26 (subjective genitive)
- G1343 δικαιοσύνη: "righteousness" (L/M); "right standing" in T where forensic sense dominates
- G4561 σάρξ: "flesh" (L always); "sinful nature" only in T for chs 7-8 where the power-of-sin sense is primary
- G3551 νόμος: "the Law" when Torah is in view; "law/principle" for abstract uses (7:21-23, 8:2)
- G2435 ἱλαστήριον (3:25): "propitiation" (L), "atoning sacrifice" (M), "the one who absorbs God's wrath" (T)
- G4151 πνεῦμα: capitalized "Spirit" throughout ch 8 where the divine Spirit is clearly referent
- G166 αἰώνιος: "eternal" (L/M); "the life of the age to come" (T) to preserve eschatological register
- G1515 εἰρήνη: "peace" — the glossary draft read "one", which is a seed error; corrected here
- G266 ἁμαρτία: "sin" — the glossary draft read "offence"; "sin" is the standard rendering
- Romans 7 "I": rhetorical first person; T maintains first person but the voice is recognizably corporate
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
  "1": {
    "1": {
      "L": "Paul, a slave of Christ Jesus, called as an apostle, set apart for the gospel of God—",
      "M": "Paul, a servant of Christ Jesus, called to be an apostle, set apart for the gospel of God—",
      "T": "This letter is from Paul—a slave belonging to Christ Jesus, called by God to be an apostle, set apart to announce the good news of God."
    },
    "2": {
      "L": "which he promised beforehand through his prophets in the Holy Scriptures,",
      "M": "the gospel he promised beforehand through his prophets in the Holy Scriptures—",
      "T": "This good news God promised long ago through his prophets, recorded in the Holy Scriptures."
    },
    "3": {
      "L": "concerning his Son, who was descended from the seed of David according to the flesh,",
      "M": "regarding his Son, who as to his earthly life was a descendant of David,",
      "T": "It is the good news about his Son—who, in his human nature, was born a descendant of David,"
    },
    "4": {
      "L": "who was declared Son of God with power according to the Spirit of holiness by the resurrection from the dead, Jesus Christ our Lord—",
      "M": "and who through the Spirit of holiness was appointed the Son of God in power by his resurrection from the dead: Jesus Christ our Lord.",
      "T": "but who was publicly designated as the Son of God in power—through the Spirit of holiness—by his resurrection from the dead. He is Jesus Christ our Lord."
    },
    "5": {
      "L": "through whom we have received grace and apostleship for the obedience of faith among all the nations, for the sake of his name,",
      "M": "Through him we received grace and apostleship to call all the Gentiles to the obedience that comes from faith for his name's sake.",
      "T": "Through him, God has given us grace and commissioned us as apostles, to bring people of every nation to the obedience that flows from faith—all for the sake of his name."
    },
    "6": {
      "L": "among whom you also are called of Jesus Christ—",
      "M": "And you also are among those Gentiles who are called to belong to Jesus Christ.",
      "T": "You yourselves are among those he has called to belong to Jesus Christ."
    },
    "7": {
      "L": "to all those in Rome who are beloved of God, called as saints: grace to you and peace from God our Father and the Lord Jesus Christ.",
      "M": "To all in Rome who are loved by God and called to be his holy people: Grace and peace to you from God our Father and from the Lord Jesus Christ.",
      "T": "To all of you in Rome who are loved by God and called to live as his holy people: May grace and peace be yours from God our Father and from the Lord Jesus Christ."
    },
    "8": {
      "L": "First, I thank my God through Jesus Christ for all of you, because your faith is proclaimed in all the world.",
      "M": "First, I thank my God through Jesus Christ for all of you, because your faith is being reported all over the world.",
      "T": "First of all, I thank my God through Jesus Christ for every one of you—the whole world is talking about your faith!"
    },
    "9": {
      "L": "For God is my witness, whom I serve with my spirit in the gospel of his Son, that without ceasing I make mention of you",
      "M": "God, whom I serve in my spirit in preaching the gospel of his Son, is my witness how constantly I remember you",
      "T": "God is my witness—the God I serve wholeheartedly in proclaiming the good news about his Son—that I mention you constantly,"
    },
    "10": {
      "L": "always in my prayers, asking if somehow by the will of God I may now at last succeed in coming to you.",
      "M": "in my prayers at all times; and I pray that now at last by God's will the way may be opened for me to come to you.",
      "T": "praying without fail that somehow God's will might allow me to visit you at last."
    },
    "11": {
      "L": "For I long to see you, in order that I may impart some spiritual gift to you, to the end that you may be established—",
      "M": "I long to see you so that I may impart to you some spiritual gift to make you strong—",
      "T": "How I long to see you! I want to share some spiritual gift with you that will strengthen and root you deeper in the faith."
    },
    "12": {
      "L": "that is, to be mutually encouraged among you, each by the faith of the other, both yours and mine.",
      "M": "that is, that you and I may be mutually encouraged by each other's faith.",
      "T": "But really, I'm talking about the encouragement we'll draw from each other—your faith and mine building one another up."
    },
    "13": {
      "L": "I do not want you to be unaware, brothers, that I often planned to come to you—and was prevented until now—in order that I might have some fruit among you also, even as among the rest of the Gentiles.",
      "M": "I do not want you to be unaware, brothers and sisters, that I planned many times to come to you (but have been prevented from doing so until now) in order that I might have a harvest among you, just as I have had among the other Gentiles.",
      "T": "Brothers and sisters, I want you to know that I've intended to visit you many times, though something has always prevented me. I want to see some fruit for the gospel among you, just as I have among the other nations."
    },
    "14": {
      "L": "Both to Greeks and to barbarians, both to the wise and to the foolish, I am a debtor.",
      "M": "I am obligated both to Greeks and non-Greeks, both to the wise and the foolish.",
      "T": "I am under a debt of obligation—to educated Greeks and uneducated foreigners alike, to the sophisticated and the simple."
    },
    "15": {
      "L": "So, as far as it depends on me, I am eager to preach the gospel to you also, those in Rome.",
      "M": "That is why I am so eager to preach the gospel also to you who are in Rome.",
      "T": "That is why I am eager, as far as it lies with me, to announce the good news to you who are there in Rome."
    },
    "16": {
      "L": "For I am not ashamed of the gospel, for it is the power of God for salvation to everyone who believes, to the Jew first and also to the Greek.",
      "M": "For I am not ashamed of the gospel, because it is the power of God that brings salvation to everyone who believes: first to the Jew, then to the Gentile.",
      "T": "I am not ashamed of the good news—not for a moment! It is the very power of God to rescue everyone who trusts in it: the Jew first, and the Gentile as well."
    },
    "17": {
      "L": "For in it the righteousness of God is revealed from faith for faith, as it is written, 'The righteous shall live by faith.'",
      "M": "For in the gospel the righteousness of God is revealed—a righteousness that is by faith from first to last, just as it is written: 'The righteous will live by faith.'",
      "T": "For in the good news a righteousness that comes from God is unveiled—a righteousness that is faith through and through, from start to finish. As the scripture says: 'The one who is righteous will live by faith.'"
    },
    "18": {
      "L": "For the wrath of God is revealed from heaven against all ungodliness and unrighteousness of men, who by their unrighteousness suppress the truth.",
      "M": "The wrath of God is being revealed from heaven against all the godlessness and wickedness of people who suppress the truth by their wickedness,",
      "T": "But God's wrath is also being unveiled from heaven—his settled opposition to all human godlessness and wickedness, of people who smother the truth with their unrighteous lives."
    },
    "19": {
      "L": "because that which is known of God is manifest among them, for God made it manifest to them.",
      "M": "since what may be known about God is plain to them, because God has made it plain to them.",
      "T": "The reason is this: what can be known about God is perfectly clear to them—God himself has made it clear."
    },
    "20": {
      "L": "For his invisible attributes, both his eternal power and divine nature, have been clearly seen from the creation of the world, being understood through the things that are made, so that they are without excuse.",
      "M": "For since the creation of the world God's invisible qualities—his eternal power and divine nature—have been clearly seen, being understood from what has been made, so that people are without excuse.",
      "T": "Ever since the world was created, God's invisible attributes—his eternal power and his divine nature—have been visible to human understanding through the things he made. So people have no excuse."
    },
    "21": {
      "L": "For although they knew God, they did not glorify him as God nor gave thanks, but became futile in their reasoning and their senseless heart was darkened.",
      "M": "For although they knew God, they neither glorified him as God nor gave thanks to him, but their thinking became futile and their foolish hearts were darkened.",
      "T": "For even though they knew God, they refused to honor him as God or give him thanks. Their reasoning became worthless and their uncomprehending hearts were plunged into darkness."
    },
    "22": {
      "L": "Claiming to be wise, they became fools,",
      "M": "Although they claimed to be wise, they became fools",
      "T": "Thinking themselves wise, they made themselves fools."
    },
    "23": {
      "L": "and exchanged the glory of the incorruptible God for the likeness of an image of corruptible man and of birds and of four-footed animals and of creeping things.",
      "M": "and exchanged the glory of the immortal God for images made to look like a mortal human being and birds and animals and reptiles.",
      "T": "They traded the glory of the undying God for carved likenesses of mortal human beings, of birds, of four-legged animals, and of reptiles."
    },
    "24": {
      "L": "Therefore God gave them up in the lusts of their hearts to impurity, to the dishonoring of their bodies among themselves,",
      "M": "Therefore God gave them over in the sinful desires of their hearts to sexual impurity for the degrading of their bodies with one another.",
      "T": "So God let them go—handing them over to the impure cravings of their own hearts, to the mutual degrading of their bodies."
    },
    "25": {
      "L": "who exchanged the truth of God for the lie, and worshiped and served the creature rather than the Creator, who is blessed forever, amen.",
      "M": "They exchanged the truth about God for a lie, and worshiped and served created things rather than the Creator—who is forever praised. Amen.",
      "T": "They swapped the truth of God for a falsehood, and worshiped and served created things rather than the Creator—who is worthy of praise forever. Amen."
    },
    "26": {
      "L": "For this reason God gave them up to dishonorable passions. For their women exchanged the natural use for that which is against nature;",
      "M": "Because of this, God gave them over to shameful lusts. Even their women exchanged natural sexual relations for unnatural ones.",
      "T": "Because of all this, God handed them over to degrading passions. Their women traded natural sexual relations for unnatural ones."
    },
    "27": {
      "L": "and likewise the men, having left the natural use of the woman, burned in their lust for one another, men with men working what is shameless, and receiving in themselves the due penalty of their error.",
      "M": "In the same way the men also abandoned natural relations with women and were inflamed with lust for one another. Men committed shameful acts with other men, and received in themselves the due penalty for their error.",
      "T": "And the men similarly abandoned natural sexual union with women and burned in lust toward one another—men committing shameless acts with men—and in themselves received the fitting consequence of their deviance."
    },
    "28": {
      "L": "And even as they did not approve to acknowledge God, God gave them up to a disapproved mind, to do the things that are not proper,",
      "M": "Furthermore, just as they did not think it worthwhile to retain the knowledge of God, so God gave them over to a depraved mind, so that they do what ought not to be done.",
      "T": "And since they decided it wasn't worth the effort to acknowledge God, God handed them over to a mind that can no longer function properly—to do the things that should never be done."
    },
    "29": {
      "L": "having been filled with all unrighteousness, wickedness, covetousness, malice; full of envy, murder, strife, deceit, maliciousness; whisperers,",
      "M": "They have become filled with every kind of wickedness, evil, greed and depravity. They are full of envy, murder, strife, deceit and malice. They are gossips,",
      "T": "They are filled with every kind of wickedness: corruption, greed, depravity—full of envy, murder, bickering, treachery, spite—and they gossip,"
    },
    "30": {
      "L": "slanderers, God-haters, insolent, proud, boastful, inventors of evil, disobedient to parents,",
      "M": "slanderers, God-haters, insolent, arrogant and boastful; they invent ways of doing evil; they disobey their parents;",
      "T": "they slander, they hate God, they are arrogant and contemptuous and boastful, always finding new ways to do evil, turning their backs on their parents."
    },
    "31": {
      "L": "foolish, faithless, unloving, unmerciful;",
      "M": "they have no understanding, no fidelity, no love, no mercy.",
      "T": "They are stupid, untrustworthy, cold-hearted, and pitiless."
    },
    "32": {
      "L": "who, knowing the righteous decree of God, that those who practice such things are worthy of death, not only do them, but also approve of those who practice them.",
      "M": "Although they know God's righteous decree that those who do such things deserve death, they not only continue to do these very things but also approve of those who practice them.",
      "T": "They know full well God's verdict that those who live like this deserve death—and yet not only do they continue doing these things, they applaud others who do the same."
    }
  },
  "2": {
    "1": {
      "L": "Therefore you are without excuse, O man, every one of you who judges; for in that you judge another, you condemn yourself, for you who judge practice the same things.",
      "M": "You, therefore, have no excuse, you who pass judgment on someone else, for at whatever point you judge another, you are condemning yourself, because you who pass judgment do the same things.",
      "T": "So there is no excuse for you—whoever you are—when you sit in judgment on others. At the very points where you judge others, you condemn yourself, because you do the same things."
    },
    "2": {
      "L": "And we know that the judgment of God is according to truth against those who practice such things.",
      "M": "Now we know that God's judgment against those who do such things is based on truth.",
      "T": "We know that God's judgment on those who do such things is entirely just."
    },
    "3": {
      "L": "And do you think this, O man—you who judge those who practice such things, and yet do them yourself—that you will escape the judgment of God?",
      "M": "So when you, a mere human being, pass judgment on them and yet do the same things, do you think you will escape God's judgment?",
      "T": "Do you really think—you who judge others for doing these things while doing the same yourself—that you will somehow escape God's judgment?"
    },
    "4": {
      "L": "Or do you despise the riches of his kindness and forbearance and patience, not knowing that the kindness of God is meant to lead you to repentance?",
      "M": "Or do you show contempt for the riches of his kindness, forbearance and patience, not realizing that God's kindness is intended to lead you to repentance?",
      "T": "Or do you treat with contempt the wealth of God's kindness, his patience, and his long-suffering—not realizing that God's kindness is designed to draw you toward repentance?"
    },
    "5": {
      "L": "But by your hardness and unrepentant heart you are storing up wrath for yourself on the day of wrath, even the revelation of the righteous judgment of God,",
      "M": "But because of your stubbornness and your unrepentant heart, you are storing up wrath against yourself for the day of God's wrath, when his righteous judgment will be revealed.",
      "T": "But with your hard, unrepentant heart you are stockpiling wrath for yourself—storing it up for the day when God's wrath breaks out and his righteous judgment is made plain."
    },
    "6": {
      "L": "who will render to each one according to his works:",
      "M": "God 'will repay each person according to what they have done.'",
      "T": "God will pay back every person in line with what they have done."
    },
    "7": {
      "L": "to those who by perseverance in good work seek glory and honor and immortality—eternal life;",
      "M": "To those who by persistence in doing good seek glory, honor and immortality, he will give eternal life.",
      "T": "Those who press on doing good, seeking glory and honor and the life of the age to come—to them he will give that life."
    },
    "8": {
      "L": "but to those who are self-seeking and do not obey the truth, but obey unrighteousness—wrath and fury.",
      "M": "But for those who are self-seeking and who reject the truth and follow evil, there will be wrath and anger.",
      "T": "But those who are selfishly ambitious, who reject the truth and follow wickedness—on them wrath and fury will fall."
    },
    "9": {
      "L": "tribulation and distress upon every soul of man who works evil, of the Jew first and also of the Greek;",
      "M": "There will be trouble and distress for every human being who does evil: first for the Jew, then for the Gentile;",
      "T": "Suffering and anguish will come upon every human being who chooses evil—the Jew first, and also the Gentile."
    },
    "10": {
      "L": "but glory and honor and peace to every man who works good, to the Jew first and also to the Greek.",
      "M": "but glory, honor and peace for everyone who does good: first for the Jew, then for the Gentile.",
      "T": "But glory, honor, and peace await everyone who does good—the Jew first, and also the Gentile."
    },
    "11": {
      "L": "For there is no partiality with God.",
      "M": "For God does not show favoritism.",
      "T": "For God shows no partiality."
    },
    "12": {
      "L": "For as many as have sinned without the law will also perish without the law, and as many as have sinned in the law will be judged by the law.",
      "M": "All who sin apart from the law will also perish apart from the law, and all who sin under the law will be judged by the law.",
      "T": "Those who have sinned outside the bounds of the Torah will also perish outside those bounds; and those who have sinned within the Torah's reach will be judged by the Torah."
    },
    "13": {
      "L": "For not the hearers of the law are righteous before God, but the doers of the law will be justified.",
      "M": "For it is not those who hear the law who are righteous in God's sight, but it is those who obey the law who will be declared righteous.",
      "T": "Because it's not the people who hear the Law who stand right before God—it's those who actually do it who will be vindicated."
    },
    "14": {
      "L": "For when Gentiles, who do not have the law, do by nature the things of the law, these, not having the law, are a law to themselves,",
      "M": "Indeed, when Gentiles, who do not have the law, do by nature things required by the law, they are a law for themselves, even though they do not have the law.",
      "T": "When Gentiles—who have no Torah—instinctively do what the Torah requires, they are their own law, even without the Torah."
    },
    "15": {
      "L": "who show the work of the law written in their hearts, their conscience bearing witness therewith, and their thoughts alternately accusing or else defending them,",
      "M": "They show that the requirements of the law are written on their hearts, their consciences also bearing witness, and their thoughts sometimes accusing them and at other times even defending them.",
      "T": "They show that the Torah's demands are written on their hearts: their conscience backs this up—their thoughts either accusing them or coming to their defense."
    },
    "16": {
      "L": "on the day when God will judge the secrets of men, according to my gospel, through Jesus Christ.",
      "M": "This will take place on the day when God judges people's secrets through Jesus Christ, as my gospel declares.",
      "T": "This will all come to light on the day God judges the hidden secrets of human hearts through Jesus Christ—exactly as my gospel declares."
    },
    "17": {
      "L": "But if you call yourself a Jew, and rest upon the law, and boast in God,",
      "M": "Now you, if you call yourself a Jew; if you rely on the law and boast in God;",
      "T": "But suppose you call yourself a Jew—you rely on the Torah and boast about your relationship with God."
    },
    "18": {
      "L": "and know his will, and approve the things that are excellent, being instructed out of the law,",
      "M": "if you know his will and approve of what is superior because you are instructed by the law;",
      "T": "You know his will; you can discern what matters most, because you've been taught by the Torah."
    },
    "19": {
      "L": "and are confident that you yourself are a guide of the blind, a light to those who are in darkness,",
      "M": "if you are convinced that you are a guide for the blind, a light for those who are in the dark,",
      "T": "You're convinced you're a guide for the blind, a light to those living in darkness,"
    },
    "20": {
      "L": "a corrector of the foolish, a teacher of babes, having in the law the form of knowledge and of the truth—",
      "M": "an instructor of the foolish, a teacher of little children, because you have in the law the embodiment of knowledge and truth—",
      "T": "a trainer of the foolish, a teacher of the immature—because you have the Law as the very pattern of knowledge and truth."
    },
    "21": {
      "L": "you, therefore, who teach another, do you not teach yourself? You who preach not to steal, do you steal?",
      "M": "you, then, who teach others, do you not teach yourself? You who preach against stealing, do you steal?",
      "T": "Then why don't you teach yourself what you teach others? You preach, 'Don't steal'—do you steal?"
    },
    "22": {
      "L": "You who say not to commit adultery, do you commit adultery? You who abhor idols, do you rob temples?",
      "M": "You who say that people should not commit adultery, do you commit adultery? You who abhor idols, do you rob temples?",
      "T": "You say, 'Don't commit adultery'—are you faithful yourself? You detest idols—do you rob their temples?"
    },
    "23": {
      "L": "You who boast in the law, through the transgression of the law do you dishonor God?",
      "M": "You who boast in the law, do you dishonor God by breaking the law?",
      "T": "You boast about having the Law—yet by breaking the Law you bring shame on God?"
    },
    "24": {
      "L": "For the name of God is blasphemed among the Gentiles because of you, even as it is written.",
      "M": "As it is written: 'God's name is blasphemed among the Gentiles because of you.'",
      "T": "As the scripture says: 'Because of you, God's name is slandered among the Gentiles.'"
    },
    "25": {
      "L": "For circumcision indeed profits if you practice the law; but if you are a transgressor of the law, your circumcision has become uncircumcision.",
      "M": "Circumcision has value if you observe the law, but if you break the law, you have become as though you had not been circumcised.",
      "T": "Circumcision has value if you keep the Law—but if you break the Law, you might as well be uncircumcised."
    },
    "26": {
      "L": "If therefore the uncircumcision keeps the ordinances of the law, shall not his uncircumcision be reckoned as circumcision?",
      "M": "So then, if those who are not circumcised keep the law's requirements, will they not be regarded as though they were circumcised?",
      "T": "So if an uncircumcised person keeps the Law's requirements, won't God treat that person as if they were circumcised?"
    },
    "27": {
      "L": "And will not the uncircumcision that is by nature, if it fulfills the law, judge you who, through the letter and circumcision, are a transgressor of the law?",
      "M": "The one who is not circumcised physically and yet obeys the law will condemn you who, even though you have the written code and circumcision, are a lawbreaker.",
      "T": "And won't the person who is physically uncircumcised yet keeps the Law stand as a judge against you—who, despite having the written Torah and circumcision, breaks the Law?"
    },
    "28": {
      "L": "For he is not a Jew who is one outwardly; neither is that circumcision which is outward in the flesh.",
      "M": "A person is not a Jew who is one only outwardly, nor is circumcision merely outward and physical.",
      "T": "Because being a Jew isn't a matter of outward markers—and circumcision isn't a matter of what's done to the body."
    },
    "29": {
      "L": "But he is a Jew who is one inwardly; and circumcision is that of the heart, in the Spirit, not in the letter; whose praise is not from men, but from God.",
      "M": "No, a person is a Jew who is one inwardly; and circumcision is circumcision of the heart, by the Spirit, not by the written code. Such a person's praise is not from other people, but from God.",
      "T": "A true Jew is one on the inside—and true circumcision is of the heart, produced by the Spirit, not by the written code. That person's affirmation comes not from other people but from God."
    }
  },
  "3": {
    "1": {
      "L": "What then is the advantage of the Jew? Or what is the profit of circumcision?",
      "M": "What advantage, then, is there in being a Jew, or what value is there in circumcision?",
      "T": "Then what's the point of being a Jew? What advantage does circumcision give?"
    },
    "2": {
      "L": "Much in every way! First of all, that they were entrusted with the oracles of God.",
      "M": "Much in every way! First of all, the Jews have been entrusted with the very words of God.",
      "T": "Enormous—in every respect! Most importantly: the Jews were entrusted with the very words of God."
    },
    "3": {
      "L": "For what if some were faithless? Does their faithlessness nullify the faithfulness of God?",
      "M": "What if some were unfaithful? Will their unfaithfulness nullify God's faithfulness?",
      "T": "But what if some of them proved unfaithful? Does their faithlessness cancel out God's faithfulness?"
    },
    "4": {
      "L": "By no means! Let God be true and every man a liar, as it is written, 'That you might be justified in your words, and prevail when you are judged.'",
      "M": "Not at all! Let God be true, and every human being a liar. As it is written: 'So that you may be proved right when you speak and prevail when you judge.'",
      "T": "Absolutely not! Let God be found true, and every human being a liar. As scripture says: 'So that you are vindicated in your words and triumph when you are put on trial.'"
    },
    "5": {
      "L": "But if our unrighteousness commends the righteousness of God, what shall we say? Is God unrighteous who inflicts wrath? (I speak as a man.)",
      "M": "But if our unrighteousness brings out God's righteousness more clearly, what shall we say? That God is unjust in bringing his wrath on us? (I am using a human argument.)",
      "T": "But if our unrighteous conduct only serves to highlight God's righteousness, is God unjust to punish us? (I'm putting this in human terms.)"
    },
    "6": {
      "L": "By no means! For then how shall God judge the world?",
      "M": "Certainly not! If that were so, how could God judge the world?",
      "T": "Absolutely not! If that were so, how could God judge the world at all?"
    },
    "7": {
      "L": "But if through my lie the truth of God has abounded to his glory, why am I also still judged as a sinner?",
      "M": "Someone might argue, 'If my falsehood enhances God's truthfulness and so increases his glory, why am I still condemned as a sinner?'",
      "T": "But someone might push further: 'If my dishonesty only makes God's truthfulness shine brighter to his glory, why am I still condemned as a sinner?'"
    },
    "8": {
      "L": "And why not say (as we are slanderously reported and as some affirm that we say), 'Let us do evil, that good may come?' Their condemnation is just.",
      "M": "Why not say—as some slanderously claim that we say—'Let us do evil that good may result?' Their condemnation is just!",
      "T": "And why not go all the way and say—as some people maliciously claim we do—'Let's do evil so that good will come from it'? Such people are rightly condemned."
    },
    "9": {
      "L": "What then? Are we better off? Not at all! For we have already charged that both Jews and Greeks are all under sin,",
      "M": "What shall we conclude then? Do we have any advantage? Not at all! For we have already made the charge that Jews and Gentiles alike are all under the power of sin.",
      "T": "Well then—do we Jews have an advantage? Not at all! We have already shown that Jews and Gentiles alike are all under the power of sin."
    },
    "10": {
      "L": "as it is written, 'There is none righteous, not even one;'",
      "M": "As it is written: 'There is no one righteous, not even one;'",
      "T": "As the scripture says: 'There is no one righteous—not even one.'"
    },
    "11": {
      "L": "'There is none that understands, there is none that seeks for God;'",
      "M": "'there is no one who understands; there is no one who seeks God.'",
      "T": "'No one understands; no one is searching for God.'"
    },
    "12": {
      "L": "'All have turned aside, they have together become unprofitable; there is none that does good, no, not even one.'",
      "M": "'All have turned away, they have together become worthless; there is no one who does good, not even one.'",
      "T": "'All have turned away; they have collectively become worthless. Not one does what is good—not a single one.'"
    },
    "13": {
      "L": "'Their throat is an open tomb; with their tongues they have used deceit; the poison of asps is under their lips;'",
      "M": "'Their throats are open graves; their tongues practice deceit. The poison of vipers is on their lips.'",
      "T": "'Their throats are open graves; they deal in deception. The venom of a viper is on their lips.'"
    },
    "14": {
      "L": "'Their mouth is full of cursing and bitterness.'",
      "M": "'Their mouths are full of cursing and bitterness.'",
      "T": "'Their mouths overflow with curses and venom.'"
    },
    "15": {
      "L": "'Their feet are swift to shed blood;'",
      "M": "'Their feet are swift to shed blood;'",
      "T": "'They are quick to commit murder.'"
    },
    "16": {
      "L": "'Destruction and misery are in their ways;'",
      "M": "'Ruin and misery mark their paths,'",
      "T": "'Ruin and anguish follow in their wake.'"
    },
    "17": {
      "L": "'And the way of peace they have not known.'",
      "M": "'and the way of peace they do not know.'",
      "T": "'The path of peace they have never learned.'"
    },
    "18": {
      "L": "'There is no fear of God before their eyes.'",
      "M": "'There is no fear of God before their eyes.'",
      "T": "'They have no reverence for God whatsoever.'"
    },
    "19": {
      "L": "Now we know that whatever the law says, it speaks to those who are in the law, so that every mouth may be stopped and all the world may become accountable to God.",
      "M": "Now we know that whatever the law says, it says to those who are under the law, so that every mouth may be silenced and the whole world held accountable to God.",
      "T": "Now, whatever the Law says, it says to those who live under the Law—so that every mouth may be shut and the entire world stand answerable before God."
    },
    "20": {
      "L": "Because by the works of the law no flesh will be justified before him; for through the law comes the knowledge of sin.",
      "M": "Therefore no one will be declared righteous in God's sight by the works of the law; rather, through the law we become conscious of our sin.",
      "T": "For no human being will be found right in God's sight by doing what the Law commands—the Law's purpose is simply to make us aware that we are sinners."
    },
    "21": {
      "L": "But now, apart from the law, the righteousness of God has been manifested, being witnessed by the law and the prophets;",
      "M": "But now apart from the law the righteousness of God has been made known, to which the Law and the Prophets testify.",
      "T": "But now—apart from the Law entirely—a righteousness that comes from God has been unveiled. The Torah and the Prophets themselves bear witness to it."
    },
    "22": {
      "L": "even the righteousness of God through faith of Jesus Christ unto all those who believe; for there is no distinction.",
      "M": "This righteousness is given through faith in Jesus Christ to all who believe. There is no difference between Jew and Gentile,",
      "T": "This is the righteousness of God—given through the faithfulness of Jesus Christ to all who trust in him. There is no distinction at all:"
    },
    "23": {
      "L": "for all have sinned and fall short of the glory of God,",
      "M": "for all have sinned and fall short of the glory of God,",
      "T": "everyone has sinned and falls far short of the glory God intended for human beings."
    },
    "24": {
      "L": "being justified freely by his grace through the redemption that is in Christ Jesus,",
      "M": "and all are justified freely by his grace through the redemption that came by Christ Jesus.",
      "T": "Yet all are freely declared right with God by his grace, through the release that Christ Jesus accomplished."
    },
    "25": {
      "L": "whom God set forth as a propitiation through faith in his blood, for a demonstration of his righteousness on account of the passing over of former sins,",
      "M": "God presented Christ as a sacrifice of atonement, through the shedding of his blood—to be received by faith. He did this to demonstrate his righteousness, because in his forbearance he had left the sins committed beforehand unpunished—",
      "T": "God put Christ forward as the one who absorbs God's wrath through his sacrificial death—received by faith. God did this to demonstrate his righteousness, because in his patient forbearance he had overlooked sins committed in former times."
    },
    "26": {
      "L": "for the demonstration of his righteousness at the present time, so that he would be just and the justifier of the one who has faith in Jesus.",
      "M": "he did it to demonstrate his righteousness at the present time, so as to be just and the one who justifies those who have faith in Jesus.",
      "T": "He did it to demonstrate his righteousness in the present moment—showing himself to be both utterly just and the very one who declares right those who place their faith in Jesus."
    },
    "27": {
      "L": "Where then is boasting? It is excluded. By what principle? By the law of works? No, but by the law of faith.",
      "M": "Where, then, is boasting? It is excluded. Because of what law? The law that requires works? No, because of the law that requires faith.",
      "T": "So where does boasting fit in? It's been shut out completely. By what principle? The principle of doing good works? No—by the principle of faith."
    },
    "28": {
      "L": "For we hold that a person is justified by faith apart from works of the law.",
      "M": "For we maintain that a person is justified by faith apart from the works of the law.",
      "T": "We conclude, then, that a person is declared right with God through faith—without needing to perform the Law's works."
    },
    "29": {
      "L": "Or is God the God of Jews only? Is he not the God of Gentiles also? Yes, of Gentiles also,",
      "M": "Or is God the God of Jews only? Is he not the God of Gentiles too? Yes, of Gentiles too,",
      "T": "Is God the God of Jews alone? Is he not the God of Gentiles as well? Yes—of Gentiles too!"
    },
    "30": {
      "L": "since God is one—and he will justify the circumcised by faith and the uncircumcised through faith.",
      "M": "since there is only one God, who will justify the circumcised by faith and the uncircumcised through that same faith.",
      "T": "Since God is one, he will vindicate the circumcised through faith and the uncircumcised through that same faith."
    },
    "31": {
      "L": "Do we then nullify the law through faith? By no means! On the contrary, we uphold the law.",
      "M": "Do we, then, nullify the law by this faith? Not at all! Rather, we uphold the law.",
      "T": "Does this mean faith cancels out the Law? Absolutely not—we actually establish the Law."
    }
  },
  "4": {
    "1": {
      "L": "What then shall we say that Abraham, our forefather according to the flesh, has found?",
      "M": "What then shall we say that Abraham, our forefather according to the flesh, discovered in this matter?",
      "T": "What, then, shall we say about Abraham, the forefather of our nation? What did he discover?"
    },
    "2": {
      "L": "For if Abraham was justified by works, he has something to boast about—but not before God.",
      "M": "If, in fact, Abraham was justified by works, he had something to boast about—but not before God.",
      "T": "If Abraham was made right by what he did, he has grounds for boasting. But he has no such grounds before God."
    },
    "3": {
      "L": "For what does the Scripture say? 'Abraham believed God, and it was reckoned to him as righteousness.'",
      "M": "What does Scripture say? 'Abraham believed God, and it was credited to him as righteousness.'",
      "T": "What does the scripture say? 'Abraham trusted God, and it was counted in his favor as righteousness.'"
    },
    "4": {
      "L": "Now to the one who works, wages are not reckoned as grace but as what is owed.",
      "M": "Now to the one who works, wages are not credited as a gift but as an obligation.",
      "T": "When you work a job, your wages aren't a gift—they're what you're owed."
    },
    "5": {
      "L": "But to the one who does not work, but believes on him who justifies the ungodly, his faith is reckoned as righteousness.",
      "M": "However, to the one who does not work but trusts God who justifies the ungodly, their faith is credited as righteousness.",
      "T": "But to the person who doesn't work but simply trusts the God who declares the wicked to be right—that person's faith is counted as righteousness."
    },
    "6": {
      "L": "Just as David also speaks of the blessing of the man to whom God reckons righteousness apart from works:",
      "M": "David says the same thing when he speaks of the blessedness of the one to whom God credits righteousness apart from works:",
      "T": "This is exactly what David means when he speaks of the happiness of the person to whom God credits righteousness without any reference to deeds:"
    },
    "7": {
      "L": "'Blessed are those whose lawless deeds are forgiven, and whose sins are covered.'",
      "M": "'Blessed are those whose transgressions are forgiven, whose sins are covered.'",
      "T": "'How happy are those whose lawless deeds are forgiven, whose sins are buried!'"
    },
    "8": {
      "L": "'Blessed is the man against whom the Lord will never reckon sin.'",
      "M": "'Blessed is the one whose sin the Lord will never count against them.'",
      "T": "'How happy is the person whose sin the Lord will never put on their account!'"
    },
    "9": {
      "L": "Is this blessing then on the circumcised, or on the uncircumcised also? For we say that faith was reckoned to Abraham as righteousness.",
      "M": "Is this blessedness only for the circumcised, or also for the uncircumcised? We have been saying that Abraham's faith was credited to him as righteousness.",
      "T": "Is this happiness only for the circumcised, or for the uncircumcised as well? We've been saying it was Abraham's faith that was credited to him as righteousness."
    },
    "10": {
      "L": "How then was it reckoned? When he was in circumcision or in uncircumcision? Not in circumcision, but in uncircumcision.",
      "M": "Under what circumstances was it credited? Was it after he was circumcised, or before? It was not after, but before!",
      "T": "So when exactly was it credited? After he was circumcised—or before? Not after. Before!"
    },
    "11": {
      "L": "And he received the sign of circumcision, a seal of the righteousness of the faith which he had while still uncircumcised, that he might be the father of all those who believe while uncircumcised, that righteousness might be reckoned to them also;",
      "M": "And he received circumcision as a sign, a seal of the righteousness that he had by faith while he was still uncircumcised. So then, he is the father of all who believe but have not been circumcised, in order that righteousness might be credited to them.",
      "T": "He later received circumcision as an outward sign—a seal confirming the righteousness he had already received by faith before he was circumcised. This makes him the father of all who believe without being circumcised, so that righteousness is credited to them as well."
    },
    "12": {
      "L": "and the father of circumcision to those who are not from circumcision only, but who also follow in the footsteps of the faith that our father Abraham had while uncircumcised.",
      "M": "And he is then also the father of the circumcised who not only are circumcised but who also follow in the footsteps of the faith that our father Abraham had before he was circumcised.",
      "T": "He is also the father of the circumcised—not merely those who are circumcised, but those who walk in the same footsteps of faith that our father Abraham walked before he was circumcised."
    },
    "13": {
      "L": "For the promise to Abraham and to his offspring that he would be heir of the world was not through the law, but through the righteousness of faith.",
      "M": "It was not through the law that Abraham and his offspring received the promise that he would be heir of the world, but through the righteousness that comes by faith.",
      "T": "The promise given to Abraham and his descendants—that he would inherit the world—did not come through the Law but through a righteousness that comes by faith."
    },
    "14": {
      "L": "For if those who are of the law are heirs, faith has been made void and the promise has been abolished.",
      "M": "For if those who depend on the law are heirs, faith means nothing and the promise is worthless,",
      "T": "For if the inheritance belongs to those who keep the Law, then faith is meaningless and the promise is null and void."
    },
    "15": {
      "L": "because the law works out wrath; but where there is no law, neither is there transgression.",
      "M": "because the law brings wrath. And where there is no law there is no transgression.",
      "T": "The Law produces wrath—where there is no Law, there is no violation."
    },
    "16": {
      "L": "For this reason it is by faith, so that it may be according to grace, to the end that the promise may be certain to all the offspring—not to that which is of the law only, but also to that which is of the faith of Abraham, who is the father of us all,",
      "M": "Therefore, the promise comes by faith, so that it may be by grace and may be guaranteed to all Abraham's offspring—not only to those who are of the law but also to those who have the faith of Abraham. He is the father of us all.",
      "T": "This is why the inheritance comes through faith—so that it rests on grace and can be guaranteed to all Abraham's descendants: not only to those who have the Law, but also to those who share Abraham's faith. He is the father of us all."
    },
    "17": {
      "L": "as it is written, 'I have made you the father of many nations'—in the presence of him whom he believed, God who gives life to the dead and calls into existence the things that do not exist.",
      "M": "As it is written: 'I have made you a father of many nations.' He is our father in the sight of God, in whom he believed—the God who gives life to the dead and calls into being things that were not.",
      "T": "As scripture says: 'I have made you the father of many nations.' He stands as our father in the presence of the God he trusted—the God who brings the dead to life and calls non-existent things into existence."
    },
    "18": {
      "L": "Who, against hope, believed in hope, to the end that he might become the father of many nations, according to that which had been spoken, 'So shall your seed be.'",
      "M": "Against all hope, Abraham in hope believed and so became the father of many nations, just as it had been said to him, 'So shall your offspring be.'",
      "T": "Against every human expectation, Abraham kept on hoping—and so he became the father of many nations, exactly as God had told him: 'That is how numerous your descendants will be.'"
    },
    "19": {
      "L": "Without becoming weak in faith, he considered his own body, already as good as dead (he was about a hundred years old), and the deadness of Sarah's womb.",
      "M": "Without weakening in his faith, he faced the fact that his body was as good as dead—since he was about a hundred years old—and that Sarah's womb was also dead.",
      "T": "His faith did not weaken, even when he acknowledged the undeniable facts: his own body was as good as dead (he was about a hundred), and Sarah's womb had long since stopped functioning."
    },
    "20": {
      "L": "He did not waver through unbelief with respect to the promise of God, but was strengthened in faith, giving glory to God,",
      "M": "Yet he did not waver through unbelief regarding the promise of God, but was strengthened in his faith and gave glory to God,",
      "T": "Yet he never wavered in unbelief when it came to God's promise—instead his faith was invigorated, and he gave glory to God,"
    },
    "21": {
      "L": "being fully convinced that what he had promised, he was also able to perform.",
      "M": "being fully persuaded that God had power to do what he had promised.",
      "T": "absolutely convinced that what God had promised, God was able to deliver."
    },
    "22": {
      "L": "Therefore also, 'it was reckoned to him as righteousness.'",
      "M": "This is why 'it was credited to him as righteousness.'",
      "T": "This is why it was credited to him as righteousness."
    },
    "23": {
      "L": "Now it was not written for his sake alone, that it was reckoned to him,",
      "M": "The words 'it was credited to him' were written not for him alone,",
      "T": "But those words—'it was credited to him'—were not written for Abraham alone."
    },
    "24": {
      "L": "but for our sake also, to whom it shall be reckoned, who believe on him who raised Jesus our Lord from the dead,",
      "M": "but also for us, to whom God will credit righteousness—for us who believe in him who raised Jesus our Lord from the dead.",
      "T": "They were written for us as well—for us who trust in the God who raised Jesus our Lord from the dead."
    },
    "25": {
      "L": "who was delivered up for our trespasses, and was raised for our justification.",
      "M": "He was delivered over to death for our sins and was raised to life for our justification.",
      "T": "Jesus was handed over to death for our trespasses, and raised to life to secure our verdict of 'righteous.'"
    }
  },
  "5": {
    "1": {
      "L": "Therefore, being justified by faith, we have peace with God through our Lord Jesus Christ,",
      "M": "Therefore, since we have been justified through faith, we have peace with God through our Lord Jesus Christ,",
      "T": "Now that we have been declared right with God through faith, we have peace with God through our Lord Jesus Christ."
    },
    "2": {
      "L": "through whom we also have had access by faith into this grace in which we stand, and we exult in hope of the glory of God.",
      "M": "through whom we have gained access by faith into this grace in which we now stand. And we boast in the hope of the glory of God.",
      "T": "Through him we have gained access into this state of grace in which we stand. And we celebrate our confident hope of sharing God's glory."
    },
    "3": {
      "L": "And not only this, but we also exult in our tribulations, knowing that tribulation works perseverance;",
      "M": "Not only so, but we also glory in our sufferings, because we know that suffering produces perseverance;",
      "T": "And not only that—we also celebrate our sufferings! Because we know that suffering produces endurance,"
    },
    "4": {
      "L": "and perseverance, proven character; and proven character, hope;",
      "M": "perseverance, character; and character, hope.",
      "T": "and endurance produces tested character, and tested character produces hope."
    },
    "5": {
      "L": "and hope does not disappoint, because the love of God has been poured out within our hearts through the Holy Spirit who was given to us.",
      "M": "And hope does not put us to shame, because God's love has been poured out into our hearts through the Holy Spirit, who has been given to us.",
      "T": "And this hope never humiliates us—because God's love has been poured lavishly into our hearts through the Holy Spirit he has given us."
    },
    "6": {
      "L": "For while we were still weak, at the right time Christ died for the ungodly.",
      "M": "You see, at just the right time, when we were still powerless, Christ died for the ungodly.",
      "T": "Consider this: at exactly the right moment—while we were still helpless—Christ died for the ungodly."
    },
    "7": {
      "L": "For one will scarcely die for a righteous man; though perhaps for the good man someone would dare to die.",
      "M": "Very rarely will anyone die for a righteous person, though for a good person someone might possibly dare to die.",
      "T": "It's a rare thing for someone to die for a decent person—though for a genuinely good person, someone might be willing."
    },
    "8": {
      "L": "But God demonstrates his own love toward us, in that while we were yet sinners, Christ died for us.",
      "M": "But God demonstrates his own love for us in this: while we were still sinners, Christ died for us.",
      "T": "But God makes his love for us plain in this: while we were still sinners—not yet seeking him at all—Christ died for us."
    },
    "9": {
      "L": "Much more then, being now justified by his blood, we shall be saved from the wrath of God through him.",
      "M": "Since we have now been justified by his blood, how much more shall we be saved from God's wrath through him!",
      "T": "Since we have now been declared right by Christ's blood, how much more certain is it that we will be rescued from God's wrath through him!"
    },
    "10": {
      "L": "For if while we were enemies, we were reconciled to God through the death of his Son, much more, having been reconciled, we shall be saved by his life.",
      "M": "For if, while we were God's enemies, we were reconciled to him through the death of his Son, how much more, having been reconciled, shall we be saved through his life!",
      "T": "For if—when we were God's enemies—we were reconciled to him through his Son's death, then how much more certain is it that—now reconciled—we will be saved by his life?"
    },
    "11": {
      "L": "And not only this, but we also exult in God through our Lord Jesus Christ, through whom we have now received the reconciliation.",
      "M": "Not only is this so, but we also boast in God through our Lord Jesus Christ, through whom we have now received reconciliation.",
      "T": "And more than that—we actually celebrate in God himself, through our Lord Jesus Christ, through whom we have now received this full reconciliation."
    },
    "12": {
      "L": "Therefore, just as through one man sin entered into the world, and death through sin, and so death spread to all men, because all sinned—",
      "M": "Therefore, just as sin entered the world through one man, and death through sin, and in this way death came to all people, because all sinned—",
      "T": "Here, then, is the picture: through one human being, sin made its entrance into the world, and death came in through sin. And death spread to every human being, because every human being sinned."
    },
    "13": {
      "L": "for sin was in the world before the law was given, but sin is not charged when there is no law.",
      "M": "To be sure, sin was in the world before the law was given, but sin is not charged against anyone's account where there is no law.",
      "T": "Sin was already in the world before the Torah came—but sin is not put on the books where there is no law."
    },
    "14": {
      "L": "Nevertheless death reigned from Adam until Moses, even over those who had not sinned in the likeness of Adam's transgression, who is a type of him who was to come.",
      "M": "Nevertheless, death reigned from the time of Adam to the time of Moses, even over those who did not sin by breaking a command, as did Adam, who is a pattern of the one to come.",
      "T": "Yet death was king from Adam to Moses—even over people who did not break a specific command as Adam had. Adam was a pattern pointing forward to the one who was to come."
    },
    "15": {
      "L": "But the gracious gift is not like the trespass. For if by the trespass of the one the many died, much more did the grace of God and the gift by the grace of the one man Jesus Christ abound to the many.",
      "M": "But the gift is not like the trespass. For if the many died by the trespass of the one man, how much more did God's grace and the gift that came by the grace of the one man, Jesus Christ, overflow to the many!",
      "T": "But the free gift is nothing like the offence. For if the many died because of one man's offence, how much greater is God's grace—and the gift that overflows through the grace of the one man Jesus Christ—to the many!"
    },
    "16": {
      "L": "And the gift is not like what came through the one who sinned; for on the one hand, the judgment arose from one trespass resulting in condemnation, but on the other hand, the gracious gift arose from many trespasses resulting in justification.",
      "M": "Nor can the gift of God be compared with the result of one man's sin: the judgment followed one sin and brought condemnation, but the gift followed many trespasses and brought justification.",
      "T": "And there is no comparison between the gift and the effect of one man's sin. The judgment from that one sin issued in condemnation; but the gracious gift—following countless offences—issued in justification."
    },
    "17": {
      "L": "For if by the trespass of the one death reigned through the one, much more will those who receive the abundance of grace and of the gift of righteousness reign in life through the one, Jesus Christ.",
      "M": "For if, by the trespass of the one man, death reigned through that one man, how much more will those who receive God's abundant provision of grace and of the gift of righteousness reign in life through the one man, Jesus Christ!",
      "T": "For if death ruled as king through one man's offence, how much more will those who receive the overflow of grace and the gift of right standing reign in life through the one man—Jesus Christ!"
    },
    "18": {
      "L": "So then, as through one trespass there resulted condemnation to all men, even so through one act of righteousness there resulted justification of life to all men.",
      "M": "Consequently, just as one trespass resulted in condemnation for all people, so also one righteous act resulted in justification and life for all people.",
      "T": "In summary: just as one offence brought condemnation to all, so also one act of righteousness brings the gift of life and right standing for all."
    },
    "19": {
      "L": "For as through the one man's disobedience the many were made sinners, even so through the obedience of the one the many will be made righteous.",
      "M": "For just as through the disobedience of the one man the many were made sinners, so also through the obedience of the one man the many will be made righteous.",
      "T": "Just as many were constituted sinners through one man's disobedience, so many will be constituted righteous through one man's obedience."
    },
    "20": {
      "L": "The law came in so that the trespass might increase; but where sin increased, grace abounded all the more,",
      "M": "The law was brought in so that the trespass might increase. But where sin increased, grace increased all the more,",
      "T": "The Law came in alongside to make the offence even clearer—but where sin multiplied, grace multiplied far more."
    },
    "21": {
      "L": "so that, as sin reigned in death, even so grace might reign through righteousness to eternal life through Jesus Christ our Lord.",
      "M": "so that, just as sin reigned in death, so also grace might reign through righteousness to bring eternal life through Jesus Christ our Lord.",
      "T": "So just as sin once reigned by means of death, so now grace reigns through righteousness, bringing the life of the age to come—through Jesus Christ our Lord."
    }
  },
  "6": {
    "1": {
      "L": "What shall we say then? Are we to continue in sin so that grace may abound?",
      "M": "What shall we say, then? Shall we go on sinning so that grace may increase?",
      "T": "So what are we saying? Should we carry on sinning so that grace can keep multiplying?"
    },
    "2": {
      "L": "By no means! We who died to sin, how shall we live in it any longer?",
      "M": "By no means! We are those who have died to sin; how can we live in it any longer?",
      "T": "Absolutely not! We have died to sin—how could we possibly go on living in it?"
    },
    "3": {
      "L": "Or do you not know that all of us who were baptized into Christ Jesus were baptized into his death?",
      "M": "Or don't you know that all of us who were baptized into Christ Jesus were baptized into his death?",
      "T": "Don't you know that all of us who were baptized into Christ Jesus were baptized into his death?"
    },
    "4": {
      "L": "We were buried therefore with him through baptism into death, so that as Christ was raised from the dead through the glory of the Father, we too might walk in newness of life.",
      "M": "We were therefore buried with him through baptism into death in order that, just as Christ was raised from the dead through the glory of the Father, we too may live a new life.",
      "T": "We were buried with him through baptism into death, so that just as Christ was raised from the dead by the Father's glorious power, we too might live a wholly new kind of life."
    },
    "5": {
      "L": "For if we have been united with him in the likeness of his death, we shall certainly also be in the likeness of his resurrection;",
      "M": "For if we have been united with him in a death like his, we will certainly also be united with him in a resurrection like his.",
      "T": "If we have been joined to him in a death like his, we will certainly be joined to him in a resurrection like his."
    },
    "6": {
      "L": "knowing this, that our old man was crucified with him, so that the body of sin might be done away with, so that we would no longer be slaves to sin;",
      "M": "For we know that our old self was crucified with him so that the body ruled by sin might be done away with, that we should no longer be slaves to sin—",
      "T": "We know this: our old self was crucified with Christ so that the sin-dominated body would be rendered powerless—so that we would no longer be slaves serving sin."
    },
    "7": {
      "L": "for he who has died is freed from sin.",
      "M": "because anyone who has died has been set free from sin.",
      "T": "For the person who has died has been legally freed from sin's claim."
    },
    "8": {
      "L": "Now if we died with Christ, we believe that we shall also live with him,",
      "M": "Now if we died with Christ, we believe that we will also live with him.",
      "T": "If we died with Christ, we trust that we will also live with him."
    },
    "9": {
      "L": "knowing that Christ, having been raised from the dead, dies no more; death no longer has mastery over him.",
      "M": "For we know that since Christ was raised from the dead, he cannot die again; death no longer has mastery over him.",
      "T": "We know that Christ, raised from the dead, will never die again—death no longer has any dominion over him."
    },
    "10": {
      "L": "For in that he died, he died to sin once for all; but in that he lives, he lives to God.",
      "M": "The death he died, he died to sin once for all; but the life he lives, he lives to God.",
      "T": "The death he died, he died to sin—definitively, once and for all. The life he now lives, he lives entirely for God."
    },
    "11": {
      "L": "Even so reckon yourselves to be dead indeed to sin, but alive to God in Christ Jesus.",
      "M": "In the same way, count yourselves dead to sin but alive to God in Christ Jesus.",
      "T": "In the same way, you must regard yourselves as dead to sin but alive to God in Christ Jesus."
    },
    "12": {
      "L": "Therefore let not sin reign in your mortal body that you should obey its lusts,",
      "M": "Therefore do not let sin reign in your mortal body so that you obey its evil desires.",
      "T": "So do not let sin rule as king in your mortal body, obeying its cravings."
    },
    "13": {
      "L": "and do not present your members as instruments of unrighteousness to sin, but present yourselves to God as alive from the dead, and your members as instruments of righteousness to God.",
      "M": "Do not offer any part of yourself to sin as an instrument of wickedness, but rather offer yourselves to God as those who have been brought from death to life; and offer every part of yourself to him as an instrument of righteousness.",
      "T": "Stop putting your body's faculties at sin's disposal as tools of wickedness. Instead, offer yourselves to God as people who have come alive from death—and put every part of your body at God's service as a tool of righteousness."
    },
    "14": {
      "L": "For sin shall not have dominion over you, for you are not under law, but under grace.",
      "M": "For sin shall no longer be your master, because you are not under the law, but under grace.",
      "T": "Sin will not be your master—because you are not under Law but under grace."
    },
    "15": {
      "L": "What then? Shall we sin, because we are not under law but under grace? By no means!",
      "M": "What then? Shall we sin because we are not under the law but under grace? By no means!",
      "T": "So what—shall we sin freely since we're not under Law but under grace? Absolutely not!"
    },
    "16": {
      "L": "Do you not know that to whom you present yourselves as slaves for obedience, his slaves you are to whom you obey; whether of sin unto death, or of obedience unto righteousness?",
      "M": "Don't you know that when you offer yourselves to someone as obedient slaves, you are slaves of the one you obey—whether you are slaves to sin, which leads to death, or to obedience, which leads to righteousness?",
      "T": "Don't you realize that when you offer yourselves as slaves in obedience to someone, you become slaves to whoever you obey—whether that's sin, which leads to death, or obedience, which leads to right living?"
    },
    "17": {
      "L": "But thanks be to God, that you were the slaves of sin, but you obeyed from the heart that form of teaching to which you were delivered.",
      "M": "But thanks be to God that, though you used to be slaves to sin, you have come to obey from your heart the pattern of teaching that has now claimed your allegiance.",
      "T": "But thanks be to God! You used to be slaves to sin—yet you wholeheartedly obeyed the pattern of teaching you were handed over to."
    },
    "18": {
      "L": "And being made free from sin, you became enslaved to righteousness.",
      "M": "You have been set free from sin and have become slaves to righteousness.",
      "T": "Set free from sin, you became slaves of righteousness."
    },
    "19": {
      "L": "I speak in human terms because of the weakness of your flesh. For just as you presented your members as slaves to impurity and to lawlessness resulting in lawlessness, so now present your members as slaves to righteousness resulting in sanctification.",
      "M": "I am using an example from everyday life because of your human limitations. Just as you used to offer yourselves as slaves to impurity and to ever-increasing wickedness, so now offer yourselves as slaves to righteousness leading to holiness.",
      "T": "(I'm using the slavery metaphor because your human nature needs it.) Just as you once put your faculties at the service of impurity and lawlessness—spiraling further into lawlessness—now put those same faculties at the service of righteousness, moving toward holiness."
    },
    "20": {
      "L": "For when you were slaves of sin, you were free in regard to righteousness.",
      "M": "When you were slaves to sin, you were free from the control of righteousness.",
      "T": "When you were sin's slaves, you were completely unrestrained by righteousness."
    },
    "21": {
      "L": "What fruit then did you have at that time in the things of which you are now ashamed? For the end of those things is death.",
      "M": "What benefit did you reap at that time from the things you are now ashamed of? Those things result in death!",
      "T": "And what did you gain from those things that you now find shameful? Nothing—except death."
    },
    "22": {
      "L": "But now, having been freed from sin and enslaved to God, you have your fruit resulting in sanctification, and the end is eternal life.",
      "M": "But now that you have been set free from sin and have become slaves of God, the benefit you reap leads to holiness, and the outcome is eternal life.",
      "T": "But now—freed from sin and enslaved to God—the fruit you produce is holiness, and the final outcome is the life of the age to come."
    },
    "23": {
      "L": "For the wages of sin is death, but the free gift of God is eternal life in Christ Jesus our Lord.",
      "M": "For the wages of sin is death, but the gift of God is eternal life in Christ Jesus our Lord.",
      "T": "Sin pays its servants with death—but God's free gift is the life of the age to come, in Christ Jesus our Lord."
    }
  },
  "7": {
    "1": {
      "L": "Or do you not know, brothers (for I am speaking to those who know the law), that the law is binding on a person only as long as he lives?",
      "M": "Do you not know, brothers and sisters—for I am speaking to those who know the law—that the law has authority over someone only as long as that person lives?",
      "T": "Surely you know this—I'm speaking to people who understand the Law—the Law has jurisdiction over a person only as long as they are alive."
    },
    "2": {
      "L": "For the married woman is bound by law to her husband while he lives; but if the husband dies, she is released from the law of the husband.",
      "M": "For example, by law a married woman is bound to her husband as long as he is alive, but if her husband dies, she is released from the law that binds her to him.",
      "T": "Take marriage: a woman is legally bound to her husband while he lives. But if her husband dies, she is released from the law that bound her to him."
    },
    "3": {
      "L": "So then, if while the husband lives she is joined to another man, she will be called an adulteress; but if the husband dies, she is free from that law, so that she is not an adulteress, though she is joined to another man.",
      "M": "So then, if she has sexual relations with another man while her husband is still alive, she is called an adulteress. But if her husband dies, she is released from that law and is not an adulteress if she marries another man.",
      "T": "So if she enters into a relationship with another man while her husband is alive, she is considered an adulteress. But if her husband dies, she is free from that law—she's no adulteress if she marries someone else."
    },
    "4": {
      "L": "Therefore, my brothers, you also were made to die to the law through the body of Christ, so that you might be joined to another—to him who was raised from the dead—so that we might bear fruit for God.",
      "M": "So, my brothers and sisters, you also died to the law through the body of Christ, that you might belong to another, to him who was raised from the dead, in order that we might bear fruit for God.",
      "T": "In the same way, my brothers and sisters, you died to the Law through Christ's body—so that you could be joined to another, to the one who was raised from the dead, and so bear fruit for God."
    },
    "5": {
      "L": "For while we were in the flesh, the sinful passions, which were through the law, were at work in our members to bear fruit for death.",
      "M": "For when we were in the realm of the flesh, the sinful passions aroused by the law were at work in us, so that we bore fruit for death.",
      "T": "When we were living under the power of the flesh, the sinful cravings stirred up by the Law were at work in every part of us—and the fruit we produced was death."
    },
    "6": {
      "L": "But now we have been released from the law, having died to that by which we were held bound, so that we serve in newness of the Spirit, and not in oldness of the letter.",
      "M": "But now, by dying to what once bound us, we have been released from the law so that we serve in the new way of the Spirit, and not in the old way of the written code.",
      "T": "But now we have been released from the Law—dying to what once held us captive—so that we serve in the new way of the Spirit, not in the old way of the written code."
    },
    "7": {
      "L": "What shall we say then? Is the law sin? By no means! Rather, I would not have come to know sin except through the law; for I would not have known about coveting if the law had not said, 'You shall not covet.'",
      "M": "What shall we say, then? Is the law sinful? Certainly not! Nevertheless, I would not have known what sin was had it not been for the law. For I would not have known what coveting really was if the law had not said, 'You shall not covet.'",
      "T": "What should we say, then—is the Law sin? Absolutely not! But I would never have known what sin was except through the Law. I would have had no idea what 'coveting' meant if the Law hadn't said, 'You shall not covet.'"
    },
    "8": {
      "L": "But sin, seizing an opportunity through the commandment, produced in me all manner of covetousness. For apart from the law, sin is dead.",
      "M": "But sin, seizing the opportunity afforded by the commandment, produced in me every kind of coveting. For apart from the law, sin was dead.",
      "T": "But sin grabbed the opportunity through the commandment and produced in me every form of coveting. Apart from Law, sin is a dead thing."
    },
    "9": {
      "L": "And I was once alive apart from the law; but when the commandment came, sin sprang to life, and I died;",
      "M": "Once I was alive apart from the law; but when the commandment came, sin sprang to life and I died.",
      "T": "I was alive once, before the commandment arrived. But when it came, sin sprang to life—and I died."
    },
    "10": {
      "L": "and this commandment which was unto life, this I found to be unto death;",
      "M": "I found that the very commandment that was intended to bring life actually brought death.",
      "T": "The very commandment that was meant to lead to life turned out to bring me death."
    },
    "11": {
      "L": "for sin, finding opportunity through the commandment, deceived me and through it killed me.",
      "M": "For sin, seizing the opportunity afforded by the commandment, deceived me, and through the commandment put me to death.",
      "T": "Because sin, exploiting the commandment as a foothold, deceived me—and used it to kill me."
    },
    "12": {
      "L": "So that the law is holy, and the commandment is holy and righteous and good.",
      "M": "So then, the law is holy, and the commandment is holy, righteous and good.",
      "T": "The Law itself is holy—and the commandment is holy, just, and good."
    },
    "13": {
      "L": "Did then that which is good become death to me? By no means! But sin, in order that it might be shown as sin, through the good worked death in me, so that through the commandment sin might become exceeding sinful.",
      "M": "Did that which is good, then, become death to me? By no means! Nevertheless, in order that sin might be recognized as sin, it used what is good to bring about my death, so that through the commandment sin might become utterly sinful.",
      "T": "Did something good become death for me? Absolutely not! It was sin—in order to be exposed as sin—that used something good to bring about death. Through the commandment, sin's true nature as sin became unmistakably clear."
    },
    "14": {
      "L": "For we know that the law is spiritual, but I am fleshly, sold under sin.",
      "M": "We know that the law is spiritual; but I am unspiritual, sold as a slave to sin.",
      "T": "We know the Law is spiritual—but I am made of flesh and blood, sold into sin's slavery."
    },
    "15": {
      "L": "For what I do, I do not understand; for I am not practicing what I would like to do, but am doing the very thing I hate.",
      "M": "I do not understand what I do. For what I want to do I do not do, but what I hate I do.",
      "T": "I don't even understand my own behavior—I don't do what I want to do, but instead I do the very thing I hate."
    },
    "16": {
      "L": "But if I do the very thing I do not want to do, I agree with the law, that it is good.",
      "M": "And if I do what I do not want to do, I agree that the law is good.",
      "T": "When I do the thing I don't want to do, I'm actually agreeing that the Law is right."
    },
    "17": {
      "L": "So now, it is no longer I who do it, but sin which dwells in me.",
      "M": "As it is, it is no longer I myself who do it, but it is sin living in me.",
      "T": "At that point, it's no longer I who am doing it—it's sin that has taken up residence in me."
    },
    "18": {
      "L": "For I know that in me, that is, in my flesh, nothing good dwells; for the willing is present with me, but the doing of the good is not.",
      "M": "For I know that good itself does not dwell in me, that is, in my sinful nature. For I have the desire to do what is good, but I cannot carry it out.",
      "T": "I know that nothing good lives in me—in my flesh, that is. I can want to do right, but I cannot carry it out."
    },
    "19": {
      "L": "For the good that I will to do, I do not; but the evil which I will not to do, that I practice.",
      "M": "For I do not do the good I want to do, but the evil I do not want to do—this I keep on doing.",
      "T": "I don't do the good I want to do, but I keep doing the evil I don't want to do."
    },
    "20": {
      "L": "But if I do what I do not will, it is no longer I who do it but sin which dwells in me.",
      "M": "Now if I do what I do not want to do, it is no longer I who do it, but it is sin living in me that does it.",
      "T": "If I do what I don't will to do, then it is no longer I who do it—it is the sin that lives in me."
    },
    "21": {
      "L": "I find then the law, that evil is present with me, the one who wills to do good.",
      "M": "So I find this law at work: Although I want to do good, evil is right there with me.",
      "T": "So I discover this principle at work: When I want to do right, evil is always right there with me."
    },
    "22": {
      "L": "For I delight in the law of God after the inward man,",
      "M": "For in my inner being I delight in God's law;",
      "T": "In my inner person I genuinely delight in God's Law—"
    },
    "23": {
      "L": "but I see a different law in my members, warring against the law of my mind, and bringing me into captivity under the law of sin which is in my members.",
      "M": "but I see another law at work in me, waging war against the law of my mind and making me a prisoner of the law of sin at work within me.",
      "T": "but I see a different law operating in my body, fighting against the law of my mind and taking me prisoner under the law of sin that lives in my members."
    },
    "24": {
      "L": "Wretched man that I am! Who will deliver me from this body of death?",
      "M": "What a wretched man I am! Who will rescue me from this body that is subject to death?",
      "T": "What a wretch I am! Who will rescue me from this body that is dragging me toward death?"
    },
    "25": {
      "L": "Thanks be to God through Jesus Christ our Lord! So then, I myself with the mind serve the law of God, but with the flesh the law of sin.",
      "M": "Thanks be to God, who delivers me through Jesus Christ our Lord! So then, I myself in my mind am a slave to God's law, but in my sinful nature a slave to the law of sin.",
      "T": "God be thanked—through Jesus Christ our Lord! So the situation is this: with my mind I am a servant of God's law, but in my flesh I am a servant of sin's law."
    }
  },
  "8": {
    "1": {
      "L": "There is therefore now no condemnation for those who are in Christ Jesus.",
      "M": "Therefore, there is now no condemnation for those who are in Christ Jesus,",
      "T": "So then—there is no condemnation at all for those who are in Christ Jesus."
    },
    "2": {
      "L": "For the law of the Spirit of life in Christ Jesus has set me free from the law of sin and of death.",
      "M": "because through Christ Jesus the law of the Spirit who gives life has set you free from the law of sin and death.",
      "T": "Because the law of the life-giving Spirit—through Christ Jesus—has set you free from the law of sin and death."
    },
    "3": {
      "L": "For what the law was unable to do, in that it was weak through the flesh, God, sending his own Son in the likeness of sinful flesh, and as a sin offering, condemned sin in the flesh;",
      "M": "For what the law was powerless to do because it was weakened by the flesh, God did by sending his own Son in the likeness of sinful flesh to be a sin offering. And so he condemned sin in the flesh,",
      "T": "The Law couldn't do it—it was powerless because of human flesh. But God did what the Law could not: he sent his own Son in the very form of sinful humanity, to deal with sin. And so he condemned sin in the flesh itself—"
    },
    "4": {
      "L": "in order that the righteous requirement of the law might be fulfilled in us, who do not walk according to the flesh but according to the Spirit.",
      "M": "in order that the righteous requirement of the law might be fully met in us, who do not live according to the flesh but according to the Spirit.",
      "T": "—so that the Law's righteous requirement might be fully met in us, who no longer live by the flesh but by the Spirit."
    },
    "5": {
      "L": "For those who are according to the flesh set their minds on the things of the flesh, but those who are according to the Spirit set their minds on the things of the Spirit.",
      "M": "Those who live according to the flesh have their minds set on what the flesh desires; but those who live in accordance with the Spirit have their minds set on what the Spirit desires.",
      "T": "Those who live by the flesh have their minds fixed on what the flesh desires. But those who live by the Spirit have their minds fixed on what the Spirit desires."
    },
    "6": {
      "L": "For the mind of the flesh is death, but the mind of the Spirit is life and peace.",
      "M": "The mind governed by the flesh is death, but the mind governed by the Spirit is life and peace.",
      "T": "To have the mind of the flesh means death. But to have the mind of the Spirit means life and peace."
    },
    "7": {
      "L": "Because the mind of the flesh is enmity against God, for it is not subject to the law of God, for neither is it able to be.",
      "M": "The mind governed by the flesh is hostile to God; it does not submit to God's law, nor can it do so.",
      "T": "The flesh-governed mind is God's enemy—it refuses to submit to God's Law and in fact is incapable of doing so."
    },
    "8": {
      "L": "And those who are in the flesh cannot please God.",
      "M": "Those who are in the realm of the flesh cannot please God.",
      "T": "Those who are controlled by the flesh simply cannot please God."
    },
    "9": {
      "L": "However, you are not in the flesh but in the Spirit, if indeed the Spirit of God dwells in you. But if anyone does not have the Spirit of Christ, he does not belong to him.",
      "M": "You, however, are not in the realm of the flesh but are in the realm of the Spirit, if indeed the Spirit of God lives in you. And if anyone does not have the Spirit of Christ, they do not belong to Christ.",
      "T": "But you are not in the flesh—you are in the Spirit, since the Spirit of God lives in you. And if anyone does not have the Spirit of Christ, that person does not belong to him."
    },
    "10": {
      "L": "But if Christ is in you, the body is dead because of sin, but the spirit is alive because of righteousness.",
      "M": "But if Christ is in you, then even though your body is subject to death because of sin, the Spirit gives life because of righteousness.",
      "T": "But if Christ is in you, then even though your body is subject to death because of sin, your spirit has life because you have been made right."
    },
    "11": {
      "L": "But if the Spirit of him who raised Jesus from the dead dwells in you, he who raised Christ from the dead will also give life to your mortal bodies through his Spirit who dwells in you.",
      "M": "And if the Spirit of him who raised Jesus from the dead is living in you, he who raised Christ from the dead will also give life to your mortal bodies because of his Spirit who lives in you.",
      "T": "And if the Spirit of the one who raised Jesus from the dead lives in you, then the one who raised Christ from the dead will also give life to your mortal bodies—through his Spirit who is living in you."
    },
    "12": {
      "L": "So then, brothers, we are obligated, not to the flesh, to live according to the flesh,",
      "M": "Therefore, brothers and sisters, we have an obligation—but it is not to the flesh, to live according to it.",
      "T": "So then, brothers and sisters, we owe the flesh nothing—we are under no obligation to live by it."
    },
    "13": {
      "L": "for if you live according to the flesh, you must die; but if by the Spirit you put to death the deeds of the body, you will live.",
      "M": "For if you live according to the flesh, you will die; but if by the Spirit you put to death the misdeeds of the body, you will live.",
      "T": "Because if you live by the flesh, you are heading for death. But if by the Spirit you keep putting to death the deeds of the body, you will live."
    },
    "14": {
      "L": "For as many as are led by the Spirit of God, these are the sons of God.",
      "M": "For those who are led by the Spirit of God are the children of God.",
      "T": "For all who are led by God's Spirit are children of God."
    },
    "15": {
      "L": "For you have not received a spirit of slavery leading to fear again, but you have received a spirit of adoption as sons, by which we cry out, 'Abba! Father!'",
      "M": "The Spirit you received does not make you slaves, so that you live in fear again; rather, the Spirit you received brought about your adoption to sonship. And by him we cry, 'Abba, Father.'",
      "T": "For the Spirit you received was not a spirit that enslaves you to fear again—but the Spirit of adoption who makes you children. It is by this Spirit that we cry out, 'Abba! Father!'"
    },
    "16": {
      "L": "The Spirit himself bears witness with our spirit that we are children of God,",
      "M": "The Spirit himself testifies with our spirit that we are God's children.",
      "T": "The Spirit himself joins his voice to ours to confirm that we are God's children."
    },
    "17": {
      "L": "and if children, heirs also—heirs of God and joint heirs with Christ, if indeed we suffer with him so that we may also be glorified with him.",
      "M": "Now if we are children, then we are heirs—heirs of God and co-heirs with Christ, if indeed we share in his sufferings in order that we may also share in his glory.",
      "T": "And if we are children, then we are heirs—heirs of God and co-heirs with Christ. But this also means we share in his sufferings, so that we may share in his glory."
    },
    "18": {
      "L": "For I consider that the sufferings of this present time are not worthy to be compared with the glory that is to be revealed to us.",
      "M": "I consider that our present sufferings are not worth comparing with the glory that will be revealed in us.",
      "T": "I have calculated it: the sufferings of this present time are not even worth comparing to the glory that is coming to light in us."
    },
    "19": {
      "L": "For the earnest expectation of the creation waits for the revealing of the sons of God.",
      "M": "For the creation waits in eager expectation for the children of God to be revealed.",
      "T": "For all of creation stands on tiptoe, eagerly waiting for the children of God to be revealed."
    },
    "20": {
      "L": "For the creation was subjected to futility, not of its own will, but because of him who subjected it, in hope",
      "M": "For the creation was subjected to frustration, not by its own choice, but by the will of the one who subjected it, in hope",
      "T": "For creation was subjected to futility—not willingly, but because God subjected it in hope—"
    },
    "21": {
      "L": "that the creation itself also will be set free from the bondage of corruption into the freedom of the glory of the children of God.",
      "M": "that the creation itself will be liberated from its bondage to decay and brought into the freedom and glory of the children of God.",
      "T": "that creation itself would one day be freed from its slavery to decay and brought into the glorious freedom of God's children."
    },
    "22": {
      "L": "For we know that the whole creation groans and suffers together until now.",
      "M": "We know that the whole creation has been groaning as in the pains of childbirth right up to the present time.",
      "T": "We know that all of creation has been groaning together in labor pains until this very moment."
    },
    "23": {
      "L": "And not only this, but also we ourselves, having the firstfruits of the Spirit, even we ourselves groan within ourselves, waiting eagerly for our adoption as sons—the redemption of our body.",
      "M": "Not only so, but we ourselves, who have the firstfruits of the Spirit, groan inwardly as we wait eagerly for our adoption to sonship, the redemption of our bodies.",
      "T": "And not only creation—we ourselves, who have the Spirit as the firstfruits of the age to come, groan inwardly as we wait eagerly for our full adoption as children of God, the redemption of our bodies."
    },
    "24": {
      "L": "For in hope we were saved. But hope that is seen is not hope; for who hopes for what he already sees?",
      "M": "For in this hope we were saved. But hope that is seen is no hope at all. Who hopes for what they already have?",
      "T": "For it was in hope that we were saved. And hope that is visible is not really hope—who hopes for something they already possess?"
    },
    "25": {
      "L": "But if we hope for what we do not see, through perseverance we wait eagerly for it.",
      "M": "But if we hope for what we do not yet have, we wait for it patiently.",
      "T": "But if we hope for what we don't yet see, we wait with steady endurance."
    },
    "26": {
      "L": "And in the same way the Spirit also helps our weakness; for we do not know how to pray as we ought, but the Spirit himself intercedes for us with groanings too deep for words.",
      "M": "In the same way, the Spirit helps us in our weakness. We do not know what we ought to pray for, but the Spirit himself intercedes for us through wordless groans.",
      "T": "In the same way, the Spirit comes alongside us in our weakness. We don't even know what to pray—but the Spirit himself intercedes for us with groanings beyond words."
    },
    "27": {
      "L": "And he who searches the hearts knows what the mind of the Spirit is, because he intercedes for the saints according to the will of God.",
      "M": "And he who searches our hearts knows the mind of the Spirit, because the Spirit intercedes for God's people in accordance with the will of God.",
      "T": "And the one who searches all hearts knows what the Spirit is saying, because the Spirit intercedes for God's people in perfect alignment with God's will."
    },
    "28": {
      "L": "And we know that to those who love God all things work together for good, to those who are called according to his purpose.",
      "M": "And we know that in all things God works for the good of those who love him, who have been called according to his purpose.",
      "T": "We know this: God works all things together for the good of those who love him—those who are called according to his purpose."
    },
    "29": {
      "L": "For those whom he foreknew he also predestined to be conformed to the image of his Son, in order that he might be the firstborn among many brothers.",
      "M": "For those God foreknew he also predestined to be conformed to the image of his Son, that he might be the firstborn among many brothers and sisters.",
      "T": "For those God knew beforehand, he also determined in advance to be shaped into the image of his Son—so that his Son might be the firstborn among a vast family of brothers and sisters."
    },
    "30": {
      "L": "And those whom he predestined he also called; and those whom he called he also justified; and those whom he justified he also glorified.",
      "M": "And those he predestined, he also called; those he called, he also justified; those he justified, he also glorified.",
      "T": "Those he determined in advance—he also called. Those he called—he also declared right. Those he declared right—he also glorified."
    },
    "31": {
      "L": "What shall we say then to these things? If God is for us, who is against us?",
      "M": "What, then, shall we say in response to these things? If God is for us, who can be against us?",
      "T": "What shall we say in response to all this? If God is on our side, who can possibly stand against us?"
    },
    "32": {
      "L": "He who did not spare his own Son, but delivered him up for us all—how will he not also with him freely give us all things?",
      "M": "He who did not spare his own Son, but gave him up for us all—how will he not also, along with him, graciously give us all things?",
      "T": "He did not hold back his own Son but handed him over for all of us—will he not then, along with him, graciously give us everything?"
    },
    "33": {
      "L": "Who will bring a charge against God's elect? It is God who justifies;",
      "M": "Who will bring any charge against those whom God has chosen? It is God who justifies.",
      "T": "Who can bring an accusation against God's chosen ones? God himself is the one who declares them right."
    },
    "34": {
      "L": "who is the one who condemns? It is Christ Jesus who died—more than that, who was raised—who is at the right hand of God, who also intercedes for us.",
      "M": "Who then is the one who condemns? No one. Christ Jesus who died—more than that, who was raised to life—is at the right hand of God and is also interceding for us.",
      "T": "And who can condemn them? Not Christ Jesus—who died, yes, and more than that, who was raised to life! He is at God's right hand, and he is interceding for us!"
    },
    "35": {
      "L": "Who shall separate us from the love of Christ? Shall tribulation, or distress, or persecution, or famine, or nakedness, or danger, or sword?",
      "M": "Who shall separate us from the love of Christ? Shall trouble or hardship or persecution or famine or nakedness or danger or sword?",
      "T": "Who can separate us from the love of Christ? Can trouble? Hardship? Persecution? Famine? Nakedness? Danger? The sword?"
    },
    "36": {
      "L": "As it is written, 'For your sake we are being killed all the day long; we were regarded as sheep for slaughter.'",
      "M": "As it is written: 'For your sake we face death all day long; we are considered as sheep to be slaughtered.'",
      "T": "As scripture says: 'For your sake we face death all day long—we are treated like sheep destined for the slaughterhouse.'"
    },
    "37": {
      "L": "But in all these things we overwhelmingly conquer through him who loved us.",
      "M": "No, in all these things we are more than conquerors through him who loved us.",
      "T": "No—in all these things we are not merely survivors but overwhelming victors through the one who loved us."
    },
    "38": {
      "L": "For I am persuaded that neither death nor life, nor angels nor principalities, nor things present nor things to come, nor powers,",
      "M": "For I am convinced that neither death nor life, neither angels nor demons, neither the present nor the future, nor any powers,",
      "T": "I am absolutely convinced: neither death nor life, neither angels nor ruling powers, neither the present moment nor anything coming,"
    },
    "39": {
      "L": "nor height nor depth, nor any other created thing, will be able to separate us from the love of God, which is in Christ Jesus our Lord.",
      "M": "neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.",
      "T": "neither height nor depth, nor any other thing in all of creation—nothing will be able to separate us from the love of God that is ours in Christ Jesus our Lord."
    }
  }
}

def main():
    for tier, key in [('literal','L'), ('mediating','M'), ('thought','T')]:
        existing = load(tier, 'romans')
        merge_tier(existing, ROMANS, key)
        save(tier, 'romans', existing)
    print('Done — Romans 1–8 written to all three tiers.')

if __name__ == '__main__':
    main()
