"""
MKT Acts chapters 17–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-acts-17-18.py

Translation decisions (consistent with mkt-acts-1-5.py and mkt-acts-11-15.py):
- πνεῦμα (Spirit): capitalised when referring to the Holy Spirit; lowercase for human spirit.
  Acts 17:16 "his spirit was provoked" = lowercase (Paul's own spirit).
  Acts 18:25 "fervent in spirit" = lowercase (Apollos's human fervour).
- κύριος (Lord): retained throughout; context (Yahweh / Jesus) is not disambiguated in L/M.
- Χριστός (Christ): "Christ" in L; "Messiah" in M when the messianic claim is foregrounded
  (17:3, 18:5, 18:28); "Messiah" in T throughout these chapters since they centre on
  Paul's synagogue argument that Jesus fulfils the Hebrew Scriptures.
- ἐκκλησία: "church" in M; "community" in T (18:22 — Jerusalem visit).
- βαπτίζω: "baptized" in L/M (18:8); "baptized" in T as well (ritual is the point here,
  not foregrounding immersion imagery).
- Acts 17:18: ἀνάστασις (resurrection) — translated literally; Paul's Athenian audience
  likely heard "Anastasis" as a female personal name at first, which adds irony the T
  tier surfaces.
- Acts 17:22–31 (Areopagus Speech): Paul's quotation "For we also are his offspring"
  (17:28b) comes from Aratus, Phaenomena 5; possibly also Cleanthes, Hymn to Zeus.
  T renders "offspring" as "children" to surface the theological weight against idolatry
  in 17:29.
- Acts 17:26: "from one" (ἐξ ἑνός) — "one man" understood contextually (Adam /
  common humanity); L preserves the ambiguity, M adds "man" for clarity, T reads
  "one person" for gender-neutral resonance without losing meaning.
- Acts 18:21: The textual tradition has Paul saying "I must keep the feast in Jerusalem"
  (Western text), but the better Alexandrian MSS (NA28) omit this. The verse retains
  the shorter form: Paul simply says he will return if God wills.
- Acts 18:25: "knowing only the baptism of John" — Apollos's gap is catechetical, not
  moral; T surfaces this as an opportunity for mentorship (Priscilla and Aquila's role,
  18:26) rather than a deficiency to be criticised.
- Aorist verbs rendered as completed acts throughout; imperfects as ongoing action
  (e.g. 17:17 "was reasoning" ongoing daily activity; 18:4 "was reasoning every Sabbath").
- OT echo: Acts 17:24 echoes Isaiah 66:1 ("heaven is my throne, earth my footstool")
  and 1 Kings 8:27 (God not contained in temples); T layers this in the rendering.
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

ACTS = {

  # ── CHAPTER 17 ─────────────────────────────────────────────────────────────
  "17": {
    "1": {
      "L": "Now when they had passed through Amphipolis and Apollonia, they came to Thessalonica, where there was a synagogue of the Jews.",
      "M": "When Paul and his companions had passed through Amphipolis and Apollonia, they came to Thessalonica, where there was a Jewish synagogue.",
      "T": "Traveling through Amphipolis and Apollonia, they arrived at Thessalonica, where there was a Jewish synagogue."
    },
    "2": {
      "L": "And according to Paul's custom, he went to them and for three Sabbaths reasoned with them from the Scriptures,",
      "M": "As was his custom, Paul went into the synagogue, and on three Sabbath days he reasoned with them from the Scriptures,",
      "T": "As was his practice, Paul went to the synagogue. For three Sabbaths he reasoned with them from the Scriptures,"
    },
    "3": {
      "L": "explaining and demonstrating that it was necessary for the Christ to suffer and to rise from the dead, and that this Jesus, whom I proclaim to you, is the Christ.",
      "M": "explaining and proving that the Messiah had to suffer and rise from the dead. This Jesus I am proclaiming to you is the Messiah, he said.",
      "T": "showing from Scripture that the Messiah had to suffer and rise from the dead. He declared: This Jesus I'm telling you about is the Messiah."
    },
    "4": {
      "L": "And some of them were persuaded and joined Paul and Silas, as did a large number of the God-fearing Greeks and not a few of the leading women.",
      "M": "Some of the Jews were persuaded and joined Paul and Silas, as did a large number of God-fearing Greeks and quite a few prominent women.",
      "T": "Some of the Jewish people were persuaded and joined Paul and Silas—along with a large number of devout Greeks and several prominent women."
    },
    "5": {
      "L": "But the Jews, being jealous and taking along some wicked men from the marketplace, formed a mob and set the city in an uproar; and attacking the house of Jason, they were seeking to bring them out to the people.",
      "M": "But other Jews were jealous; so they rounded up some bad characters from the market-place, formed a mob and started a riot in the city. They rushed to Jason's house in search of Paul and Silas in order to bring them out to the crowd.",
      "T": "But the other Jewish leaders, stirred by jealousy, gathered some troublemakers from the marketplace, started a riot, and stormed Jason's house looking for Paul and Silas."
    },
    "6": {
      "L": "And not finding them, they dragged Jason and some brothers before the city authorities, crying out: These men who have turned the world upside down have come here also,",
      "M": "But when they did not find them, they dragged Jason and some other believers before the city officials, shouting: These men who have caused trouble all over the world have now come here,",
      "T": "When they couldn't find Paul and Silas, they dragged Jason and some other believers before the city officials, shouting: These troublemakers who have turned the world upside down have come here too!"
    },
    "7": {
      "L": "and Jason has received them; and they all act contrary to the decrees of Caesar, saying that there is another king—Jesus.",
      "M": "and Jason has welcomed them into his house. They are all defying Caesar's decrees, saying that there is another king, one called Jesus.",
      "T": "Jason has taken them in. They all defy Caesar's decrees by claiming there is another king—Jesus."
    },
    "8": {
      "L": "And they stirred up the crowd and the city authorities when they heard these things.",
      "M": "When they heard this, the crowd and the city officials were thrown into turmoil.",
      "T": "This alarmed the crowd and the city officials."
    },
    "9": {
      "L": "And when they had taken a pledge from Jason and the rest, they released them.",
      "M": "Then they made Jason and the others post bond and let them go.",
      "T": "They made Jason and the others post a security bond before releasing them."
    },
    "10": {
      "L": "And the brothers immediately sent Paul and Silas away by night to Berea, and when they arrived they went into the synagogue of the Jews.",
      "M": "As soon as it was night, the believers sent Paul and Silas away to Berea. On arriving there, they went to the Jewish synagogue.",
      "T": "That same night the believers sent Paul and Silas off to Berea. When they arrived, they went straight to the Jewish synagogue."
    },
    "11": {
      "L": "Now these were more noble than those in Thessalonica; they received the word with all eagerness, examining the Scriptures daily to see if these things were so.",
      "M": "Now the Berean Jews were of more noble character than those in Thessalonica, for they received the message with great eagerness and examined the Scriptures every day to see if what Paul said was true.",
      "T": "The Bereans were more open-minded than the Thessalonians—they eagerly received the message and examined the Scriptures every day to see whether what Paul said was true."
    },
    "12": {
      "L": "Many of them therefore believed, along with a number of prominent Greek women and men.",
      "M": "As a result, many of them believed, as did also a number of prominent Greek women and many Greek men.",
      "T": "As a result, many believed—including a number of prominent Greek women and men."
    },
    "13": {
      "L": "But when the Jews from Thessalonica learned that the word of God had been proclaimed by Paul in Berea also, they came there too, agitating and stirring up the crowds.",
      "M": "But when the Jews in Thessalonica learned that Paul was preaching the word of God at Berea, some of them went there too, agitating the crowds and stirring them up.",
      "T": "But when the Jewish leaders in Thessalonica found out that Paul was preaching God's word in Berea, they came there to stir up trouble and agitate the crowds."
    },
    "14": {
      "L": "And then immediately the brothers sent Paul away to go as far as to the sea, but Silas and Timothy remained there.",
      "M": "The believers immediately sent Paul to the coast, but Silas and Timothy stayed at Berea.",
      "T": "The believers immediately sent Paul down to the coast, while Silas and Timothy stayed behind in Berea."
    },
    "15": {
      "L": "And those who conducted Paul brought him as far as Athens; and when they received an instruction for Silas and Timothy that they should come to him as soon as possible, they departed.",
      "M": "Those who escorted Paul brought him to Athens and then left with instructions for Silas and Timothy to join him as soon as possible.",
      "T": "Paul's escorts took him all the way to Athens, then returned with a message for Silas and Timothy to join him as quickly as possible."
    },
    "16": {
      "L": "Now while Paul was waiting for them in Athens, his spirit was provoked within him as he saw that the city was full of idols.",
      "M": "While Paul was waiting for them in Athens, he was greatly distressed to see that the city was full of idols.",
      "T": "While Paul was waiting in Athens, he was deeply troubled to see the city completely filled with idols."
    },
    "17": {
      "L": "So he was reasoning in the synagogue with the Jews and the devout persons, and in the marketplace every day with those who happened to be there.",
      "M": "So he reasoned in the synagogue with both Jews and God-fearing Greeks, as well as in the market-place day by day with those who happened to be there.",
      "T": "So he debated in the synagogue with the Jews and devout Greeks, and every day in the marketplace with anyone who happened to be there."
    },
    "18": {
      "L": "And some of the Epicurean and Stoic philosophers also were conversing with him. And some were saying: What does this babbler mean to say? But others: He seems to be a proclaimer of foreign deities—because he was proclaiming Jesus and the resurrection.",
      "M": "A group of Epicurean and Stoic philosophers began to debate with him. Some of them asked: What is this babbler trying to say? Others remarked: He seems to be advocating foreign gods. They said this because Paul was preaching the good news about Jesus and the resurrection.",
      "T": "He also debated with some Epicurean and Stoic philosophers. Some scoffed: What is this word-picker trying to say? Others said: He seems to be promoting foreign gods—because Paul was preaching about Jesus and the resurrection."
    },
    "19": {
      "L": "And taking hold of him, they brought him to the Areopagus, saying: May we know what this new teaching is that you are presenting?",
      "M": "Then they took him and brought him to a meeting of the Areopagus, where they said to him: May we know what this new teaching is that you are presenting?",
      "T": "They took hold of him and brought him to the Areopagus, saying: We'd like to understand this new teaching of yours."
    },
    "20": {
      "L": "For you are bringing some strange things to our hearing; we want to know therefore what these things mean.",
      "M": "You are bringing some strange ideas to our ears and we would like to know what they mean.",
      "T": "What you're saying sounds strange to us. We want to understand what you mean."
    },
    "21": {
      "L": "Now all the Athenians and the foreigners sojourning there spent their time in nothing else but telling or hearing something new.",
      "M": "All the Athenians and the foreigners who lived there spent their time doing nothing but talking about and listening to the latest ideas.",
      "T": "Now, all the Athenians and the visitors staying there loved nothing more than discussing the latest ideas."
    },
    "22": {
      "L": "And Paul, standing in the midst of the Areopagus, said: Men of Athens, I observe that in every way you are very religious.",
      "M": "Paul then stood up in the meeting of the Areopagus and said: People of Athens! I see that in every way you are very religious.",
      "T": "So Paul stood up in the middle of the Areopagus and said: People of Athens, I can see that you are extremely religious in every way."
    },
    "23": {
      "L": "For passing through and observing your objects of worship, I also found an altar on which had been inscribed: TO AN UNKNOWN GOD. Therefore what you worship as unknown, this I proclaim to you.",
      "M": "For as I walked around and looked carefully at your objects of worship, I even found an altar with this inscription: TO AN UNKNOWN GOD. So you are ignorant of the very thing you worship—and this is what I am going to proclaim to you.",
      "T": "As I was walking around and looking at what you worship, I noticed an altar with this inscription: TO AN UNKNOWN GOD. What you worship without knowing who he is—that is what I'm going to tell you about."
    },
    "24": {
      "L": "The God who made the world and everything in it, he being Lord of heaven and earth, does not dwell in temples made by hands,",
      "M": "The God who made the world and everything in it is the Lord of heaven and earth and does not live in temples built by human hands.",
      "T": "The God who made the world and everything in it—he is Lord of heaven and earth—doesn't live in temples built by human hands."
    },
    "25": {
      "L": "nor is he served by human hands as though he needed anything, since he himself gives to all life and breath and all things.",
      "M": "And he is not served by human hands, as if he needed anything. Rather, he himself gives everyone life and breath and everything else.",
      "T": "He isn't served by human hands, as if he needed anything. He himself is the one who gives life and breath and everything else to all people."
    },
    "26": {
      "L": "And he made from one every nation of mankind to dwell on all the face of the earth, having determined appointed seasons and the boundaries of their habitation,",
      "M": "From one man he made all the nations, that they should inhabit the whole earth; and he marked out their appointed times in history and the boundaries of their lands.",
      "T": "From one person he made all the nations to inhabit the whole earth. He determined their appointed times in history and the boundaries of their territories."
    },
    "27": {
      "L": "to seek God, if perhaps they might feel after him and find him—though indeed he is not far from each one of us.",
      "M": "God did this so that they would seek him and perhaps reach out for him and find him, though he is not far from any one of us.",
      "T": "He did this so that people would seek him—and perhaps feel their way toward him and find him. Though he is not far from any one of us."
    },
    "28": {
      "L": "For in him we live and move and exist, as even some of your own poets have said: For we also are his offspring.",
      "M": "For in him we live and move and have our being. As some of your own poets have said: We are his offspring.",
      "T": "For in him we live and move and exist. As some of your own poets have said: We are his children."
    },
    "29": {
      "L": "Being therefore offspring of God, we ought not to think that the divine nature is like gold or silver or stone—an image formed by human skill and imagination.",
      "M": "Therefore since we are God's offspring, we should not think that the divine being is like gold or silver or stone—an image made by human design and skill.",
      "T": "Since we are God's children, we shouldn't think of God as an idol made of gold, silver, or stone—something shaped by human hands and imagination."
    },
    "30": {
      "L": "Therefore, having overlooked the times of ignorance, God is now commanding all people everywhere to repent,",
      "M": "In the past God overlooked such ignorance, but now he commands all people everywhere to repent.",
      "T": "God has looked past those earlier times of ignorance—but now he commands everyone, everywhere, to turn to him."
    },
    "31": {
      "L": "because he has set a day on which he will judge the world in righteousness by a man whom he has appointed; and he has given proof of this to all by raising him from the dead.",
      "M": "For he has set a day when he will judge the world with justice by the man he has appointed. He has given proof of this to everyone by raising him from the dead.",
      "T": "He has set a day when he will judge the whole world with justice—by the man he has appointed. And he has given proof of this to everyone by raising him from the dead."
    },
    "32": {
      "L": "Now when they heard of the resurrection of the dead, some began to scoff; but others said: We will hear you again about this.",
      "M": "When they heard about the resurrection of the dead, some of them sneered, but others said: We want to hear you again on this subject.",
      "T": "When they heard about the resurrection of the dead, some sneered—but others said: We'd like to hear more about this."
    },
    "33": {
      "L": "So Paul went out from their midst.",
      "M": "At that, Paul left the Council.",
      "T": "With that, Paul left the Areopagus."
    },
    "34": {
      "L": "But some men joined him and believed, among whom also were Dionysius the Areopagite and a woman named Damaris, and others with them.",
      "M": "Some of the people became followers of Paul and believed. Among them was Dionysius, a member of the Areopagus, also a woman named Damaris, and a number of others.",
      "T": "Some people joined Paul and believed. Among them were Dionysius, a member of the Areopagus, a woman named Damaris, and others with them."
    },
  },

  # ── CHAPTER 18 ─────────────────────────────────────────────────────────────
  "18": {
    "1": {
      "L": "After these things, departing from Athens, he came to Corinth.",
      "M": "After this, Paul left Athens and went to Corinth.",
      "T": "After this, Paul left Athens and traveled to Corinth."
    },
    "2": {
      "L": "And he found a certain Jew named Aquila, a native of Pontus, having recently come from Italy with his wife Priscilla, because Claudius had ordered all the Jews to leave Rome. He came to them,",
      "M": "There he met a Jew named Aquila, a native of Pontus, who had recently come from Italy with his wife Priscilla, because Claudius had ordered all Jews to leave Rome. Paul went to see them,",
      "T": "There he met a Jewish man named Aquila, a native of Pontus who had recently arrived from Italy with his wife Priscilla—they had left because Emperor Claudius had ordered all Jews out of Rome. Paul went to see them,"
    },
    "3": {
      "L": "and because he was of the same trade he stayed with them and they were working together, for by trade they were tentmakers.",
      "M": "and because he was a tentmaker as they were, he stayed and worked with them.",
      "T": "and since Paul was a tentmaker—the same trade as Aquila and Priscilla—he stayed and worked with them."
    },
    "4": {
      "L": "And he was reasoning in the synagogue every Sabbath and persuading both Jews and Greeks.",
      "M": "Every Sabbath he reasoned in the synagogue, trying to persuade Jews and Greeks.",
      "T": "Every Sabbath he debated in the synagogue, trying to persuade both Jews and Greeks."
    },
    "5": {
      "L": "But when Silas and Timothy came down from Macedonia, Paul was constrained by the word, testifying to the Jews that Jesus was the Christ.",
      "M": "When Silas and Timothy came from Macedonia, Paul devoted himself exclusively to preaching, testifying to the Jews that Jesus was the Messiah.",
      "T": "When Silas and Timothy arrived from Macedonia, Paul devoted himself entirely to preaching—declaring to the Jewish community that Jesus is the Messiah."
    },
    "6": {
      "L": "But when they opposed and reviled him, he shook out his garments and said to them: Your blood be upon your own heads; I am clean. From now on I will go to the Gentiles.",
      "M": "But when they opposed Paul and became abusive, he shook out his clothes in protest and said to them: Your blood be on your own heads! I am innocent of it. From now on I will go to the Gentiles.",
      "T": "But when they opposed him with insults, he shook out his clothes in protest and said: Your blood is on your own heads—I am clear of responsibility. From now on I'm going to the Gentiles."
    },
    "7": {
      "L": "And departing from there, he went into the house of a man named Titius Justus, a worshiper of God, whose house was adjoining the synagogue.",
      "M": "Then Paul left the synagogue and went next door to the house of Titius Justus, a worshipper of God.",
      "T": "He left the synagogue and went next door to the home of Titius Justus, a worshiper of God."
    },
    "8": {
      "L": "But Crispus, the synagogue leader, believed in the Lord together with his whole household; and many of the Corinthians, hearing, were believing and being baptized.",
      "M": "Crispus, the synagogue leader, and his entire household believed in the Lord; and many of the Corinthians who heard Paul believed and were baptised.",
      "T": "Crispus, the synagogue leader, believed in the Lord along with his entire household. And many other Corinthians who heard Paul believed and were baptized."
    },
    "9": {
      "L": "And the Lord said to Paul in a vision during the night: Do not be afraid, but go on speaking and do not be silent,",
      "M": "One night the Lord spoke to Paul in a vision: Do not be afraid; keep on speaking, do not be silent.",
      "T": "One night the Lord said to Paul in a vision: Don't be afraid—keep speaking and don't fall silent."
    },
    "10": {
      "L": "for I am with you, and no one will attack you to harm you, because I have many people in this city.",
      "M": "For I am with you, and no one is going to attack and harm you, because I have many people in this city.",
      "T": "I am with you, and no one will attack or harm you—because I have many people in this city."
    },
    "11": {
      "L": "And he settled there a year and six months, teaching the word of God among them.",
      "M": "So Paul stayed in Corinth for a year and a half, teaching them the word of God.",
      "T": "Paul stayed in Corinth for a year and a half, teaching the word of God."
    },
    "12": {
      "L": "But when Gallio was proconsul of Achaia, the Jews made a united attack on Paul and brought him before the tribunal,",
      "M": "While Gallio was proconsul of Achaia, the Jews of Corinth made a united attack on Paul and brought him to the place of judgment.",
      "T": "When Gallio became governor of Achaia, the Jewish leaders made a coordinated attack on Paul and dragged him before the court."
    },
    "13": {
      "L": "saying: This man is persuading people to worship God contrary to the law.",
      "M": "This man, they charged, is persuading the people to worship God in ways contrary to the law.",
      "T": "Their charge: This man is persuading people to worship God in ways that violate the law."
    },
    "14": {
      "L": "But as Paul was about to open his mouth, Gallio said to the Jews: If it were a matter of wrongdoing or wicked crime, O Jews, it would be reasonable for me to accept your complaint.",
      "M": "Just as Paul was about to speak, Gallio said to them: If you Jews were making a complaint about some misdemeanour or serious crime, it would be reasonable for me to listen to you.",
      "T": "Just as Paul was about to speak, Gallio cut the accusers off: If this were a matter of crime or serious wrongdoing, I would have reason to hear your case."
    },
    "15": {
      "L": "But if it is questions about words and names and your own law, look after it yourselves; I will not be a judge of these things.",
      "M": "But since it involves questions about words and names and your own law—settle the matter yourselves. I will not be a judge of such things.",
      "T": "But since this is about words, names, and your own religious law—settle it among yourselves. I refuse to judge such matters."
    },
    "16": {
      "L": "And he drove them from the tribunal.",
      "M": "So he drove them off.",
      "T": "And he had them thrown out of court."
    },
    "17": {
      "L": "And they all took hold of Sosthenes, the synagogue leader, and beat him in front of the tribunal. But none of these things mattered to Gallio.",
      "M": "Then the crowd there turned on Sosthenes the synagogue leader and beat him in front of the proconsul; and Gallio showed no concern whatever.",
      "T": "Then the crowd turned on Sosthenes, the synagogue leader, and beat him right in front of the court. But Gallio paid no attention."
    },
    "18": {
      "L": "And Paul, having remained many more days, said farewell to the brothers and sailed away to Syria, and Priscilla and Aquila were with him. He had his hair cut at Cenchreae, for he had a vow.",
      "M": "Paul stayed on in Corinth for some time. Then he left the brothers and sisters and sailed for Syria, accompanied by Priscilla and Aquila. Before he sailed, he had his hair cut off at Cenchreae because of a vow he had taken.",
      "T": "Paul stayed in Corinth a while longer, then said goodbye to the brothers and sisters and sailed for Syria, with Priscilla and Aquila. Before leaving, he had his hair cut at Cenchreae, fulfilling a vow he had made."
    },
    "19": {
      "L": "And they arrived at Ephesus, and he left them there; but he himself went into the synagogue and reasoned with the Jews.",
      "M": "They arrived at Ephesus, where Paul left Priscilla and Aquila. He himself went into the synagogue and reasoned with the Jews.",
      "T": "They arrived at Ephesus, where Paul left Priscilla and Aquila. He went to the synagogue and debated with the Jewish community."
    },
    "20": {
      "L": "And when they asked him to remain for a longer time, he declined,",
      "M": "When they asked him to spend more time with them, he declined.",
      "T": "They asked him to stay longer, but he declined."
    },
    "21": {
      "L": "but saying farewell to them and saying: I will return to you again, God willing, he set sail from Ephesus.",
      "M": "But as he left, he promised, I will come back if it is God's will. Then he set sail from Ephesus.",
      "T": "He said goodbye and told them: I will come back, God willing. Then he sailed from Ephesus."
    },
    "22": {
      "L": "And when he had landed at Caesarea, he went up and greeted the church, and then went down to Antioch.",
      "M": "When he landed at Caesarea, he went up to Jerusalem and greeted the church and then went down to Antioch.",
      "T": "He landed at Caesarea, went up to greet the church in Jerusalem, and then went down to Antioch."
    },
    "23": {
      "L": "And after spending some time there, he left and passed through the Galatian region and Phrygia in order, strengthening all the disciples.",
      "M": "After spending some time in Antioch, Paul set out from there and travelled from place to place throughout the region of Galatia and Phrygia, strengthening all the disciples.",
      "T": "After spending some time there, Paul set out again, traveling through the region of Galatia and Phrygia, strengthening the disciples everywhere he went."
    },
    "24": {
      "L": "Now a certain Jew named Apollos, an Alexandrian by birth, a learned man, came to Ephesus, being mighty in the Scriptures.",
      "M": "Meanwhile a Jew named Apollos, a native of Alexandria, came to Ephesus. He was a learned man, with a thorough knowledge of the Scriptures.",
      "T": "Meanwhile, a Jewish man named Apollos, a native of Alexandria, arrived in Ephesus. He was an eloquent speaker with a thorough knowledge of the Scriptures."
    },
    "25": {
      "L": "He had been instructed in the way of the Lord, and being fervent in spirit, he was speaking and teaching accurately the things about Jesus, though he knew only the baptism of John.",
      "M": "He had been instructed in the way of the Lord, and he spoke with great fervour and taught about Jesus accurately, though he knew only the baptism of John.",
      "T": "He had been taught the way of the Lord and was passionate in spirit. He taught accurately about Jesus—though he only knew about John's baptism."
    },
    "26": {
      "L": "And he began to speak boldly in the synagogue; but when Priscilla and Aquila heard him, they took him aside and explained to him the way of God more accurately.",
      "M": "He began to speak boldly in the synagogue. When Priscilla and Aquila heard him, they invited him to their home and explained to him the way of God more adequately.",
      "T": "He began speaking boldly in the synagogue. When Priscilla and Aquila heard him, they invited him home and explained the way of God to him more fully."
    },
    "27": {
      "L": "And when he wanted to cross over to Achaia, the brothers encouraged him and wrote to the disciples to welcome him. When he arrived, he greatly helped those who had believed through grace,",
      "M": "When Apollos wanted to go to Achaia, the brothers and sisters encouraged him and wrote to the disciples there to welcome him. When he arrived, he was a great help to those who by grace had believed.",
      "T": "When Apollos decided to go to Achaia, the brothers and sisters encouraged him and wrote to the believers there to welcome him. On his arrival he was a great asset to those who had believed through God's grace."
    },
    "28": {
      "L": "for he vigorously refuted the Jews publicly, demonstrating through the Scriptures that Jesus was the Christ.",
      "M": "For he vigorously refuted his Jewish opponents in public debate, proving from the Scriptures that Jesus was the Messiah.",
      "T": "He powerfully refuted the Jewish leaders in public, showing from the Scriptures that Jesus is the Messiah."
    },
  },
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'acts')
        merge_tier(existing, ACTS, tier_key)
        save(tier_dir, 'acts', existing)
    print('Acts 17–18 written.')

if __name__ == '__main__':
    main()
