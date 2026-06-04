"""
MKT Acts chapters 16–21 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-acts-16-21.py

Building on Acts 1–15 key-term decisions:
- G2424 (Ἰησοῦς): "Jesus" throughout
- G5547 (Χριστός): "Christ" (L/M/T)
- G2962 (κύριος): "Lord" throughout
- G4151 ἅγιον (Holy Spirit): "Holy Spirit" throughout
- G1577 (ἐκκλησία): "church" throughout
- G80 (ἀδελφοί): L: "brothers"; M/T: "brothers and sisters"
- G932 (βασιλεία): "kingdom" throughout
- G3056 (λόγος): "word" (of God / of the Lord)
- G386 (ἀνάστασις): "resurrection" throughout
- G1484 (ἔθνη): "Gentiles" (when contrasted with Jews) / "nations" (geographic)
- G2453 (Ἰουδαῖος): "Jew/Jewish" throughout

New terms in Acts 16-21:
- G3490 (ναύκληρος): "shipowner" / "captain" (ch 27 only — not yet here)
- Ch 16: Lydia's household — G4211 (πορφυρόπωλις): "dealer in purple cloth" — keep
- G4151 μαντεία (spirit of divination, 16:16): "spirit of divination" (L/M/T)
  — the slave girl with πνεῦμα πύθωνα ("Python spirit"); L: "spirit of divination";
  M/T: "spirit by which she predicted the future"
- G4066 (περίχωρος): "surrounding region"
- Areopagus (17:19,22,34): G697 (Ἄρειος Πάγος) — L: "Areopagus"; M: "Areopagus";
  T: "Mars Hill" — keep Greek in L/M, English equivalent in T
- G57 (ἄγνωστος θεός 17:23): "UNKNOWN GOD" — the Athenian altar inscription; render
  in capitals in L to indicate it is an inscription; M/T: "Unknown God" (caps)
- G2236 (ἥδιστα): "most gladly"
- G2871 (κοπή): not here
- G200 (ἀκρίς): not here
- G3056 (λόγος) in philosophical context (17:18): some thought Paul was preaching
  about "Jesus and the Resurrection" as two deities; note this in commentary
- G2316 (θεός) in Athens (17:23-31): Paul argues from natural theology to the
  God who raised Christ; the "unknown God" is the God who created all things
- Corinthian context (ch 18): Priscilla (G4252 Πρίσκιλλα) and Aquila (G207 Ἀκύλας)
  — proper names kept; tent-making (G4635 σκηνοποιός): "tentmaker" (L/M/T)
- Apollos (G625 Ἀπολλώς, 18:24): "eloquent" (G3052 λόγιος); "fervent in spirit"
  (G2204 ζέω τῷ πνεύματι): L: "fervent in the Spirit"; M: "fervent in spirit";
  T: "passionate in spirit" — both human spirit and Spirit possible; L capitalizes
- G3783 (ὀφείλημα): not here; G3784 (ὀφείλω): "owed/must"
- Ephesian disciples (19:1-7): twelve who had only John's baptism; they receive
  the Holy Spirit — important sacramental/pneumatological passage
- G1228 (διάβολος): not prominent here
- G2897 (κραιπάλη): not here
- Diana/Artemis riot (19:23-41): G735 (Ἄρτεμις) = Artemis of Ephesus;
  L/M: "Artemis"; T: "Artemis" — do not use "Diana" (Latin; English follows Greek NT)
- G3565 (νύμφη): not here
- Farewell discourse (20:17-38): Paul's speech to the Ephesian elders at Miletus —
  one of the most theologically rich passages in Acts; pastoral vocabulary important:
  G4166 (ποιμήν) / G1984 (ἐπισκοπή): "oversee/shepherding the flock"; G4264 (προβάτιον):
  not here but G4168 (ποίμνιον): "flock" (20:28,29) — render with pastoral force
- G18 (ἀγαθός) / G2570 (καλός): both "good" unless context demands
- G4102 (πίστις): "faith" throughout
- G1343 (δικαιοσύνη): "righteousness" throughout
- G1344 (δικαιόω): not prominent in Acts
- G2309 (θέλω): "will/want"
- G4151 (πνεῦμα) in 20:22-23: "bound in the Spirit" (L) vs "compelled by the Spirit" (M/T)
- G3956 (πᾶς): "all/every" as context requires
- G0 (blood, 20:26,28): "blood" — "the blood of God" (20:28) is theologically significant;
  do not soften: L/M: "with his own blood"; T: "at the cost of his own blood" —
  refers to Christ, not God the Father; note in commentary
- G141 (αἱρετικός): not here
- G741 (ἀρτύω): not here
- Ch 21: Paul's journey to Jerusalem; James and the elders; Agabus's prophecy
- G435 (ἀνήρ): "man/men" as context requires — sometimes vocative "brothers" in group
- G5330 (Φαρισαῖος): "Pharisee" in ch 23 references (not yet)
- G3614 (οἰκία) / G3624 (οἶκος): "house/household" — context sensitive
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
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]

ACTS_16_21 = {
 "16": {
  "1": {
   "L": "And he came also to Derbe and to Lystra. And behold, a certain disciple was there named Timothy, the son of a Jewish woman who was a believer, but his father was a Greek.",
   "M": "Paul came to Derbe and then to Lystra, where a disciple named Timothy lived, whose mother was Jewish and a believer but whose father was a Greek.",
   "T": "Paul arrived at Derbe and then Lystra, where he found a disciple named Timothy. His mother was a Jewish believer, but his father was Greek."
  },
  "2": {
   "L": "He was well spoken of by the brothers in Lystra and Iconium.",
   "M": "The believers at Lystra and Iconium spoke well of him.",
   "T": "The brothers and sisters in Lystra and Iconium spoke highly of him."
  },
  "3": {
   "L": "Paul wanted to have him go with him, and he took and circumcised him because of the Jews who were in those places, for they all knew that his father was a Greek.",
   "M": "Paul wanted to take him along on the journey, so he circumcised him because of the Jews who lived in that area, for they all knew that his father was a Greek.",
   "T": "Paul wanted to take Timothy along, so he circumcised him—out of consideration for the Jewish people in that region, who all knew his father was Greek."
  },
  "4": {
   "L": "And as they were passing through the cities, they were delivering the decrees to keep that had been decided upon by the apostles and elders in Jerusalem.",
   "M": "As they travelled from town to town, they delivered the decisions reached by the apostles and elders in Jerusalem for the people to obey.",
   "T": "As they went from town to town, they delivered the decisions made by the apostles and elders in Jerusalem for everyone to follow."
  },
  "5": {
   "L": "So the churches were being strengthened in the faith and were increasing in number daily.",
   "M": "So the churches were strengthened in the faith and grew daily in numbers.",
   "T": "The churches were strengthened in their faith and grew in numbers every day."
  },
  "6": {
   "L": "And they passed through the Phrygian and Galatian region, having been forbidden by the Holy Spirit to speak the word in Asia.",
   "M": "Paul and his companions travelled throughout the region of Phrygia and Galatia, having been kept by the Holy Spirit from preaching the word in the province of Asia.",
   "T": "They traveled through the region of Phrygia and Galatia, because the Holy Spirit had prevented them from preaching in the province of Asia."
  },
  "7": {
   "L": "And when they had come to Mysia, they attempted to go into Bithynia, but the Spirit of Jesus did not allow them.",
   "M": "When they came to the border of Mysia, they tried to enter Bithynia, but the Spirit of Jesus would not allow them to.",
   "T": "When they reached the border of Mysia, they tried to enter Bithynia—but the Spirit of Jesus would not let them."
  },
  "8": {
   "L": "And passing by Mysia, they came down to Troas.",
   "M": "So they passed by Mysia and went down to Troas.",
   "T": "So they bypassed Mysia and went down to Troas."
  },
  "9": {
   "L": "And a vision appeared to Paul during the night: a certain man of Macedonia was standing and urging him, saying: Come over to Macedonia and help us.",
   "M": "During the night Paul had a vision of a man of Macedonia standing and begging him, Come over to Macedonia and help us.",
   "T": "That night Paul had a vision: a man from Macedonia was standing there, pleading with him: Come over to Macedonia and help us!"
  },
  "10": {
   "L": "And when he had seen the vision, immediately we sought to go out to Macedonia, concluding that God had called us to proclaim the gospel to them.",
   "M": "After Paul had seen the vision, we got ready at once to leave for Macedonia, concluding that God had called us to preach the gospel to them.",
   "T": "As soon as Paul saw the vision, we immediately made plans to leave for Macedonia—certain that God had called us to bring the good news to those people."
  },
  "11": {
   "L": "Setting sail therefore from Troas, we ran a straight course to Samothrace, and the following day to Neapolis,",
   "M": "From Troas we put out to sea and sailed straight for Samothrace, and the next day we went on to Neapolis.",
   "T": "We set sail from Troas and ran a straight course to Samothrace, and the next day on to Neapolis."
  },
  "12": {
   "L": "and from there to Philippi, which is the leading city of the district of Macedonia and a Roman colony. And we were staying in that city for some days.",
   "M": "From there we travelled to Philippi, a Roman colony and the leading city of that district of Macedonia. And we stayed there several days.",
   "T": "From there we went to Philippi—a leading city of that region of Macedonia and a Roman colony. We stayed there for several days."
  },
  "13": {
   "L": "And on the Sabbath day we went outside the gate to the riverside, where we supposed there was a place of prayer, and sitting down we spoke to the women who had gathered.",
   "M": "On the Sabbath we went outside the city gate to the river, where we expected to find a place of prayer. We sat down and began to speak to the women who had gathered there.",
   "T": "On the Sabbath we went outside the city gate to the riverside, where we expected to find a place of prayer. We sat down and began talking with the women who had gathered."
  },
  "14": {
   "L": "And a certain woman named Lydia, a dealer in purple cloth from the city of Thyatira, a worshiper of God, was listening; and the Lord opened her heart to pay attention to what was spoken by Paul.",
   "M": "One of those listening was a woman from the city of Thyatira named Lydia, a dealer in purple cloth. She was a worshipper of God. The Lord opened her heart to respond to Paul's message.",
   "T": "One of the women listening was Lydia—a dealer in purple cloth from the city of Thyatira who worshiped God. The Lord opened her heart, and she responded to what Paul was saying."
  },
  "15": {
   "L": "And when she and her household were baptized, she urged us, saying: If you have judged me to be faithful to the Lord, come into my house and stay. And she prevailed upon us.",
   "M": "When she and the members of her household were baptised, she invited us to her home. If you consider me a believer in the Lord, she said, come and stay at my house. And she persuaded us.",
   "T": "When she and her household were baptized, she invited us home. She said: If you consider me a believer in the Lord, come and stay at my house. And she convinced us."
  },
  "16": {
   "L": "And it came to pass, as we were going to the place of prayer, that a certain slave girl having a spirit of divination met us, who was bringing much profit to her owners by fortune-telling.",
   "M": "Once when we were going to the place of prayer, we were met by a female slave who had a spirit by which she predicted the future. She earned a great deal of money for her owners by fortune-telling.",
   "T": "One day on our way to the place of prayer, we encountered a slave girl who had a spirit of divination. She made a lot of money for her owners through fortune-telling."
  },
  "17": {
   "L": "She followed Paul and us and cried out, saying: These men are servants of the Most High God, who proclaim to you the way of salvation.",
   "M": "She followed Paul and the rest of us, shouting: These men are servants of the Most High God, who are telling you the way to be saved.",
   "T": "She kept following Paul and the rest of us, shouting: These men are servants of the Most High God—they are telling you how to be saved!"
  },
  "18": {
   "L": "And she did this for many days. But Paul, greatly annoyed, turned and said to the spirit: I command you in the name of Jesus Christ to come out of her! And it came out that very hour.",
   "M": "She kept this up for many days. Finally Paul became so annoyed that he turned around and said to the spirit: In the name of Jesus Christ I command you to come out of her! At that moment the spirit left her.",
   "T": "She kept this up for many days. Paul finally became so exasperated that he turned to the spirit and said: In the name of Jesus Christ, I order you to come out of her! And at that moment the spirit left."
  },
  "19": {
   "L": "But when her owners saw that their hope of gain had gone out, they seized Paul and Silas and dragged them into the marketplace before the rulers.",
   "M": "When her owners realised that their hope of making money was gone, they seized Paul and Silas and dragged them into the market-place to face the authorities.",
   "T": "When her owners saw that their source of income was gone, they grabbed Paul and Silas and hauled them into the marketplace to face the authorities."
  },
  "20": {
   "L": "And bringing them before the magistrates, they said: These men are disturbing our city, being Jews,",
   "M": "They brought them before the magistrates and said: These men are Jews, and are throwing our city into an uproar",
   "T": "They brought them before the magistrates and accused them: These men are Jews and are stirring up trouble in our city!"
  },
  "21": {
   "L": "and they are proclaiming customs which it is not lawful for us to receive or practice, being Romans.",
   "M": "by advocating customs unlawful for us Romans to accept or practise.",
   "T": "They are promoting customs that we Romans are not allowed to accept or practice."
  },
  "22": {
   "L": "And the crowd rose up together against them, and the magistrates tore their garments off them and commanded them to be beaten with rods.",
   "M": "The crowd joined in the attack against Paul and Silas, and the magistrates ordered them to be stripped and beaten with rods.",
   "T": "The crowd joined in the attack. The magistrates ordered Paul and Silas to be stripped and beaten with rods."
  },
  "23": {
   "L": "And after laying many stripes on them, they threw them into prison, commanding the jailer to guard them securely,",
   "M": "After they had been severely flogged, they were thrown into prison, and the jailer was commanded to guard them carefully.",
   "T": "After a severe beating, they were thrown into prison. The jailer was ordered to guard them carefully."
  },
  "24": {
   "L": "who having received such a command, threw them into the inner prison and fastened their feet in the stocks.",
   "M": "When he received these orders, he put them in the inner cell and fastened their feet in the stocks.",
   "T": "Following these orders, the jailer put them in the inner cell and clamped their feet in the stocks."
  },
  "25": {
   "L": "And about midnight Paul and Silas were praying and singing hymns to God, and the prisoners were listening to them.",
   "M": "About midnight Paul and Silas were praying and singing hymns to God, and the other prisoners were listening to them.",
   "T": "Around midnight, Paul and Silas were praying and singing hymns to God—and the other prisoners were listening."
  },
  "26": {
   "L": "And suddenly there was a great earthquake, so that the foundations of the prison were shaken; and immediately all the doors were opened, and everyone's bonds were loosed.",
   "M": "Suddenly there was such a violent earthquake that the foundations of the prison were shaken. At once all the prison doors flew open, and everyone's chains came loose.",
   "T": "Suddenly a massive earthquake shook the foundations of the prison. All the doors flew open at once, and everyone's chains fell off."
  },
  "27": {
   "L": "And the jailer was awakened from sleep, and seeing the prison doors open, he drew his sword and was about to kill himself, supposing that the prisoners had escaped.",
   "M": "The jailer woke up, and when he saw the prison doors open, he drew his sword and was about to kill himself because he thought the prisoners had escaped.",
   "T": "The jailer woke up and saw the prison doors wide open. He drew his sword and was about to kill himself, thinking the prisoners had all escaped."
  },
  "28": {
   "L": "But Paul cried out with a loud voice, saying: Do not harm yourself, for we are all here.",
   "M": "But Paul shouted: Don't harm yourself! We are all here!",
   "T": "But Paul shouted: Don't do it—we're all still here!"
  },
  "29": {
   "L": "And calling for lights, he rushed in, and trembling with fear, he fell down before Paul and Silas.",
   "M": "The jailer called for lights, rushed in and fell trembling before Paul and Silas.",
   "T": "The jailer called for lights, rushed in, and fell trembling before Paul and Silas."
  },
  "30": {
   "L": "And bringing them out he said: Sirs, what must I do to be saved?",
   "M": "He then brought them out and asked: Sirs, what must I do to be saved?",
   "T": "He brought them out and asked: Sirs, what must I do to be saved?"
  },
  "31": {
   "L": "And they said: Believe in the Lord Jesus, and you will be saved, you and your household.",
   "M": "They replied: Believe in the Lord Jesus, and you will be saved—you and your household.",
   "T": "They answered: Believe in the Lord Jesus—and you will be saved, along with your whole household."
  },
  "32": {
   "L": "And they spoke the word of the Lord to him together with all those in his house.",
   "M": "Then they spoke the word of the Lord to him and to all the others in his house.",
   "T": "Then they shared the word of the Lord with him and everyone else in his household."
  },
  "33": {
   "L": "And he took them in that hour of the night and washed their wounds; and he was baptized at once, he and all his family.",
   "M": "At that hour of the night the jailer took them and washed their wounds; then immediately he and all his household were baptised.",
   "T": "Right then in the middle of the night, the jailer cleaned their wounds. And he and his entire household were baptized."
  },
  "34": {
   "L": "And bringing them up into his house, he set food before them and rejoiced greatly, having believed in God with his whole household.",
   "M": "The jailer brought them into his house and set a meal before them; he was filled with joy because he had come to believe in God—he and his whole household.",
   "T": "He brought them into his home and set a meal before them. He and his whole household were overjoyed—they had come to faith in God."
  },
  "35": {
   "L": "Now when it was day, the magistrates sent the constables, saying: Release those men.",
   "M": "When it was daylight, the magistrates sent their officers to the jailer with the order: Release those men.",
   "T": "When morning came, the magistrates sent their officers with the order: Release those men."
  },
  "36": {
   "L": "And the jailer reported these words to Paul: The magistrates have sent to release you. So go out now and go in peace.",
   "M": "The jailer told Paul: The magistrates have ordered that you and Silas be released. Now you can leave. Go in peace.",
   "T": "The jailer passed the message to Paul: The magistrates have ordered your release. You're free to go—go in peace."
  },
  "37": {
   "L": "But Paul said to them: They have beaten us publicly without a trial, men who are Romans, and have thrown us into prison; and now are they throwing us out secretly? No indeed; but let them come themselves and lead us out.",
   "M": "But Paul said to the officers: They beat us publicly without a trial, even though we are Roman citizens, and threw us into prison. And now do they want to get rid of us quietly? No! Let them come themselves and escort us out.",
   "T": "But Paul said: They beat us publicly without a trial—and we are Roman citizens! They threw us in prison, and now they want to slip us out quietly? Absolutely not. Let them come here themselves and escort us out."
  },
  "38": {
   "L": "And the constables reported these words to the magistrates; and they were afraid when they heard that they were Romans.",
   "M": "The officers reported this to the magistrates, and when they heard that Paul and Silas were Roman citizens, they were alarmed.",
   "T": "The officers reported this to the magistrates, who were alarmed to learn that Paul and Silas were Roman citizens."
  },
  "39": {
   "L": "And coming, they appealed to them and bringing them out they were asking them to leave the city.",
   "M": "They came to appease them and escorted them from the prison, requesting them to leave the city.",
   "T": "The magistrates came to apologize. They escorted Paul and Silas out of prison and asked them to leave the city."
  },
  "40": {
   "L": "And going out of the prison, they went to Lydia's house, and when they saw the brothers they encouraged them and departed.",
   "M": "After Paul and Silas came out of the prison, they went to Lydia's house, where they met with the brothers and sisters and encouraged them. Then they left.",
   "T": "When they left the prison, they went to Lydia's house, where they met with the brothers and sisters, encouraged them, and then departed."
  }
 },
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
  }
 },
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
  }
 },
 "19": {
  "1": {
   "L": "And it came to pass while Apollos was in Corinth, that Paul, having passed through the upper regions, came to Ephesus and found some disciples.",
   "M": "While Apollos was at Corinth, Paul took the road through the interior and arrived at Ephesus. There he found some disciples",
   "T": "While Apollos was in Corinth, Paul traveled through the interior regions and arrived at Ephesus. There he found some disciples"
  },
  "2": {
   "L": "And he said to them: Did you receive the Holy Spirit when you believed? And they said to him: We have not even heard whether the Holy Spirit has been given.",
   "M": "and asked them: Did you receive the Holy Spirit when you believed? They answered: No, we have not even heard that there is a Holy Spirit.",
   "T": "and asked them: Did you receive the Holy Spirit when you believed? They answered: We haven't even heard that there is a Holy Spirit."
  },
  "3": {
   "L": "And he said: Into what then were you baptized? And they said: Into John's baptism.",
   "M": "So Paul asked: Then what baptism did you receive? John's baptism, they replied.",
   "T": "He asked: Then what baptism did you receive? They said: John's baptism."
  },
  "4": {
   "L": "And Paul said: John baptized with a baptism of repentance, telling the people to believe in the one coming after him, that is, Jesus.",
   "M": "Paul said: John's baptism was a baptism of repentance. He told the people to believe in the one coming after him, that is, in Jesus.",
   "T": "Paul explained: John's baptism called people to turn from sin. He told them to believe in the one who was coming after him—that is, Jesus."
  },
  "5": {
   "L": "And hearing this, they were baptized in the name of the Lord Jesus.",
   "M": "On hearing this, they were baptised in the name of the Lord Jesus.",
   "T": "When they heard this, they were baptized in the name of the Lord Jesus."
  },
  "6": {
   "L": "And when Paul laid his hands on them, the Holy Spirit came upon them, and they were speaking in tongues and prophesying.",
   "M": "When Paul placed his hands on them, the Holy Spirit came on them, and they spoke in tongues and prophesied.",
   "T": "When Paul laid his hands on them, the Holy Spirit came on them, and they spoke in tongues and prophesied."
  },
  "7": {
   "L": "There were about twelve men in all.",
   "M": "There were about twelve men in all.",
   "T": "There were about twelve of them in all."
  },
  "8": {
   "L": "And entering the synagogue, he was speaking boldly for three months, reasoning and persuading concerning the kingdom of God.",
   "M": "Paul entered the synagogue and spoke boldly there for three months, arguing persuasively about the kingdom of God.",
   "T": "Paul went to the synagogue and spoke boldly for three months, debating and persuading people about the kingdom of God."
  },
  "9": {
   "L": "But when some became hardened and were disobedient, speaking evil of the Way before the congregation, withdrawing from them, he took the disciples with him and was reasoning daily in the school of Tyrannus.",
   "M": "But some of them became obstinate; they refused to believe and publicly maligned the Way. So Paul left them. He took the disciples with him and had discussions daily in the lecture hall of Tyrannus.",
   "T": "But some of them grew hardened and refused to believe, publicly slandering the Way. So Paul withdrew from them, taking the disciples with him, and debated daily in the lecture hall of Tyrannus."
  },
  "10": {
   "L": "And this continued for two years, so that all those dwelling in Asia heard the word of the Lord, both Jews and Greeks.",
   "M": "This went on for two years, so that all the Jews and Greeks who lived in the province of Asia heard the word of the Lord.",
   "T": "This continued for two years, until everyone in the province of Asia—both Jews and Greeks—had heard the word of the Lord."
  },
  "11": {
   "L": "And God was performing extraordinary miracles through the hands of Paul,",
   "M": "God did extraordinary miracles through Paul,",
   "T": "God did extraordinary miracles through Paul—"
  },
  "12": {
   "L": "so that even handkerchiefs or aprons that had touched his skin were carried to the sick, and the diseases left them, and the evil spirits went out.",
   "M": "so that even handkerchiefs and aprons that had touched him were taken to those who were ill, and their illnesses were cured and the evil spirits left them.",
   "T": "so that even cloths and handkerchiefs that had touched him were brought to the sick, and they were healed and evil spirits drove out."
  },
  "13": {
   "L": "But some of the itinerant Jewish exorcists also attempted to invoke the name of the Lord Jesus over those who had evil spirits, saying: I adjure you by Jesus whom Paul preaches.",
   "M": "Some Jews who went around driving out evil spirits tried to invoke the name of the Lord Jesus over those who were demon-possessed. They would say: In the name of the Jesus whom Paul preaches, I command you to come out.",
   "T": "Some traveling Jewish exorcists tried using the name of the Lord Jesus against those who had evil spirits. They would say: I command you by the Jesus that Paul preaches!"
  },
  "14": {
   "L": "And there were seven sons of Sceva, a Jewish high priest, who were doing this.",
   "M": "Seven sons of Sceva, a Jewish chief priest, were doing this.",
   "T": "Seven sons of a Jewish chief priest named Sceva were doing this."
  },
  "15": {
   "L": "But answering, the evil spirit said to them: Jesus I know, and Paul I am acquainted with; but who are you?",
   "M": "One day the evil spirit answered them: Jesus I know, and Paul I know about, but who are you?",
   "T": "One day the evil spirit answered: Jesus I know—and I know about Paul. But who are you?"
  },
  "16": {
   "L": "And the man in whom was the evil spirit leaped on them, and overcoming them all, was so strong against them that they fled out of that house naked and wounded.",
   "M": "Then the man who had the evil spirit jumped on them and overpowered them all. He gave them such a beating that they ran out of the house naked and bleeding.",
   "T": "Then the man controlled by the evil spirit leaped on them and overpowered them all—giving them such a beating that they ran out of the house naked and bleeding."
  },
  "17": {
   "L": "And this became known to all those dwelling in Ephesus, both Jews and Greeks; and fear fell upon them all, and the name of the Lord Jesus was held in high honor.",
   "M": "When this became known to the Jews and Greeks living in Ephesus, they were all seized with fear, and the name of the Lord Jesus was held in high honour.",
   "T": "News of this spread quickly throughout Ephesus—both Jews and Greeks heard about it. Everyone was filled with awe, and the name of the Lord Jesus was held in great honor."
  },
  "18": {
   "L": "And many of those who had believed were coming, confessing and disclosing their practices.",
   "M": "Many of those who believed now came and openly confessed what they had done.",
   "T": "Many of the believers came forward, openly confessing the practices they had been involved in."
  },
  "19": {
   "L": "And a good number of those who practiced magic brought their books together and burned them in front of all; and they counted up the value of them and found it fifty thousand pieces of silver.",
   "M": "A number who had practised sorcery brought their scrolls together and burned them publicly. When they calculated the value of the scrolls, the total came to fifty thousand drachmas.",
   "T": "A large number who had practiced sorcery brought their scrolls together and burned them in public. When they calculated the value, it came to fifty thousand silver coins."
  },
  "20": {
   "L": "So the word of the Lord was growing mightily and prevailing.",
   "M": "In this way the word of the Lord spread widely and grew in power.",
   "T": "In this way the word of the Lord kept spreading with powerful effect."
  },
  "21": {
   "L": "Now when these things were completed, Paul resolved in the Spirit to pass through Macedonia and Achaia and go to Jerusalem, saying: After I have been there, I must also see Rome.",
   "M": "After all this had happened, Paul decided to go to Jerusalem, passing through Macedonia and Achaia. After I have been there, he said, I must visit Rome also.",
   "T": "After all this, Paul felt compelled by the Spirit to travel through Macedonia and Achaia and go to Jerusalem. He said: After I've been there, I must also see Rome."
  },
  "22": {
   "L": "And sending into Macedonia two of his helpers, Timothy and Erastus, he himself stayed in Asia for a time.",
   "M": "He sent two of his helpers, Timothy and Erastus, to Macedonia, while he stayed in the province of Asia a little longer.",
   "T": "He sent Timothy and Erastus ahead to Macedonia, while he stayed in the province of Asia a while longer."
  },
  "23": {
   "L": "And at that time there arose no small stir concerning the Way.",
   "M": "About that time there arose a great disturbance about the Way.",
   "T": "About that time, a serious disturbance broke out over the Way."
  },
  "24": {
   "L": "For a man named Demetrius, a silversmith who made silver shrines of Artemis, was providing no small profit for the craftsmen.",
   "M": "A silversmith named Demetrius, who made silver shrines of Artemis, brought in a lot of business for the craftsmen there.",
   "T": "A silversmith named Demetrius made silver miniature shrines of Artemis and kept the craftsmen busy with plenty of work."
  },
  "25": {
   "L": "He gathered these together, along with the workers in similar trades, and said: Men, you know that our prosperity comes from this trade.",
   "M": "He called them together, along with the workers in related trades, and said: You know, my friends, that we receive a good income from this business.",
   "T": "He called together the craftsmen and workers in related trades and said: Men, you know that our prosperity depends on this business."
  },
  "26": {
   "L": "And you see and hear that not only in Ephesus but in almost all of Asia this Paul has persuaded and turned away a large number of people, saying that gods made with hands are no gods.",
   "M": "And you see and hear how this fellow Paul has convinced and led astray large numbers of people here in Ephesus and in practically the whole province of Asia. He says that gods made by human hands are no gods at all.",
   "T": "You can see and hear for yourselves that this man Paul has convinced and turned away a huge number of people—not just in Ephesus but throughout almost all of Asia—claiming that gods made by human hands aren't real gods."
  },
  "27": {
   "L": "And not only is there a danger that this trade of ours may fall into disrepute, but also that the temple of the great goddess Artemis be regarded as nothing, and she whom all Asia and the world worships will be stripped of her majesty.",
   "M": "There is danger not only that our trade will lose its good name, but also that the temple of the great goddess Artemis will be discredited; and the goddess herself, who is worshipped throughout the province of Asia and the world, will be robbed of her divine majesty.",
   "T": "There's danger that not only our business will fall apart, but also that the temple of the great goddess Artemis will be brought into contempt—and Artemis herself, worshiped throughout all of Asia and the world, will be stripped of her greatness."
  },
  "28": {
   "L": "And when they heard this and were filled with rage, they were crying out: Great is Artemis of the Ephesians!",
   "M": "When they heard this, they were furious and began shouting: Great is Artemis of the Ephesians!",
   "T": "When they heard this, they erupted in fury and began shouting: Great is Artemis of the Ephesians!"
  },
  "29": {
   "L": "And the city was filled with the confusion; and they rushed together into the theater, dragging with them Gaius and Aristarchus, Macedonians, Paul's traveling companions.",
   "M": "Soon the whole city was in an uproar. The people seized Gaius and Aristarchus, Paul's travelling companions from Macedonia, and all rushed into the theatre together.",
   "T": "The whole city erupted into chaos. The crowd seized Gaius and Aristarchus, Paul's traveling companions from Macedonia, and swept them into the theater."
  },
  "30": {
   "L": "But Paul wanting to go in to the assembly, the disciples would not let him.",
   "M": "Paul wanted to appear before the crowd, but the disciples would not let him.",
   "T": "Paul wanted to go in to face the crowd, but the disciples wouldn't let him."
  },
  "31": {
   "L": "And some of the Asiarchs also, being his friends, sent to him urging him not to venture into the theater.",
   "M": "Even some of the officials of the province, friends of Paul, sent him a message begging him not to venture into the theatre.",
   "T": "Even some of the provincial officials who were Paul's friends sent him a warning, urging him not to go into the theater."
  },
  "32": {
   "L": "Some therefore were crying out one thing and some another; for the assembly was in confusion, and the majority did not know why they had come together.",
   "M": "The assembly was in confusion: some were shouting one thing, some another. Most of the people did not even know why they were there.",
   "T": "The crowd was in complete confusion—different people shouting different things. Most didn't even know why they were there."
  },
  "33": {
   "L": "And some of the crowd prompted Alexander, the Jews having put him forward; and Alexander, waving his hand, wanted to make a defense to the people.",
   "M": "The Jews in the crowd pushed Alexander to the front, and they shouted instructions to him. He motioned for silence in order to make a defence before the people.",
   "T": "The Jewish community pushed Alexander forward to address the crowd. He motioned for quiet and tried to make a defense on their behalf."
  },
  "34": {
   "L": "But when they recognized that he was a Jew, one voice was raised by all for about two hours: Great is Artemis of the Ephesians!",
   "M": "But when they realised he was a Jew, they all shouted in unison for about two hours: Great is Artemis of the Ephesians!",
   "T": "But when the crowd recognized he was Jewish, they all shouted together for about two hours: Great is Artemis of the Ephesians!"
  },
  "35": {
   "L": "And the city clerk, quieting the crowd, said: Men of Ephesus, what person is there who does not know that the city of the Ephesians is the temple keeper of the great Artemis and of the image that fell down from Zeus?",
   "M": "The city clerk quietened the crowd and said: Fellow Ephesians, doesn't all the world know that the city of Ephesus is the guardian of the temple of the great Artemis and of her image, which fell from heaven?",
   "T": "The city clerk quieted the crowd and said: People of Ephesus! Who doesn't know that the city of Ephesus is the guardian of the temple of the great Artemis and of the sacred image that fell from heaven?"
  },
  "36": {
   "L": "These things being undeniable, you must be quiet and do nothing rash.",
   "M": "Therefore, since these facts are undeniable, you ought to calm down and not do anything rash.",
   "T": "Since this is undeniable, you should calm down and not do anything foolish."
  },
  "37": {
   "L": "For you have brought these men here who are neither temple robbers nor blasphemers of our goddess.",
   "M": "You have brought these men here, though they have neither robbed temples nor blasphemed our goddess.",
   "T": "You've brought these men here, but they haven't robbed the temple or insulted our goddess."
  },
  "38": {
   "L": "If therefore Demetrius and the craftsmen with him have a complaint against anyone, the courts are open and there are proconsuls; let them bring charges against one another.",
   "M": "If, then, Demetrius and his fellow craftsmen have a grievance against anybody, the courts are open and there are proconsuls. They can press charges.",
   "T": "If Demetrius and his fellow craftsmen have a grievance against anyone, the courts are in session and there are governors—let them file formal charges."
  },
  "39": {
   "L": "But if you seek anything further, it will be decided in the regular assembly.",
   "M": "If there is anything further you want to bring up, it must be settled in a legal assembly.",
   "T": "If you have other matters to raise, they should be settled in a lawful assembly."
  },
  "40": {
   "L": "For indeed we are in danger of being charged with rioting about today's events, there being no cause by which we can account for this disorderly gathering.",
   "M": "As it is, we are in danger of being charged with rioting because of what happened today. In that case we would not be able to account for this commotion, since there is no reason for it.",
   "T": "As it is, we are in danger of being charged with rioting over today's events. We have no good reason to explain this uproar."
  },
  "41": {
   "L": "And having said these things, he dismissed the assembly.",
   "M": "After he had said this, he dismissed the assembly.",
   "T": "After saying this, he dismissed the crowd."
  }
 },
 "20": {
  "1": {
   "L": "And after the uproar ceased, Paul sent for the disciples and, encouraging them, said farewell and departed to go to Macedonia.",
   "M": "When the uproar had ended, Paul sent for the disciples and, after encouraging them, said goodbye and set out for Macedonia.",
   "T": "When the uproar ended, Paul called the disciples together, encouraged them, said goodbye, and set out for Macedonia."
  },
  "2": {
   "L": "And having gone through those regions and encouraged them with much speech, he came to Greece.",
   "M": "He travelled through that area, speaking many words of encouragement to the people, and finally arrived in Greece,",
   "T": "He traveled through those regions, offering many words of encouragement to the believers, and finally arrived in Greece."
  },
  "3": {
   "L": "And spending three months there, when a plot was made against him by the Jews as he was about to set sail for Syria, he resolved to return through Macedonia.",
   "M": "where he stayed three months. Because some Jews had plotted against him just as he was about to sail for Syria, he decided to go back through Macedonia.",
   "T": "He stayed there three months. When a Jewish plot was discovered against him just as he was about to sail for Syria, he decided to return through Macedonia instead."
  },
  "4": {
   "L": "And he was accompanied by Sopater son of Pyrrhus from Berea; and Aristarchus and Secundus from the Thessalonians; and Gaius from Derbe, and Timothy; and Tychicus and Trophimus from Asia.",
   "M": "He was accompanied by Sopater son of Pyrrhus from Berea, Aristarchus and Secundus from Thessalonica, Gaius from Derbe, Timothy also, and Tychicus and Trophimus from the province of Asia.",
   "T": "He was accompanied by Sopater son of Pyrrhus from Berea; Aristarchus and Secundus from Thessalonica; Gaius from Derbe; Timothy; and Tychicus and Trophimus from the province of Asia."
  },
  "5": {
   "L": "These, going on ahead, were waiting for us at Troas.",
   "M": "These men went on ahead and waited for us at Troas.",
   "T": "These men went on ahead and waited for us at Troas."
  },
  "6": {
   "L": "But we sailed from Philippi after the days of Unleavened Bread, and in five days we came to them in Troas, where we stayed for seven days.",
   "M": "But we sailed from Philippi after the Festival of Unleavened Bread, and five days later joined the others at Troas, where we stayed seven days.",
   "T": "We sailed from Philippi after the Festival of Unleavened Bread and joined them at Troas five days later, where we stayed for a week."
  },
  "7": {
   "L": "And on the first day of the week, when we were gathered together to break bread, Paul talked with them, intending to depart on the next day; and he continued talking until midnight.",
   "M": "On the first day of the week we came together to break bread. Paul spoke to the people and, because he intended to leave the next day, kept on talking until midnight.",
   "T": "On the first day of the week we gathered together to break bread. Paul talked with the people and, since he planned to leave the next day, kept on speaking until midnight."
  },
  "8": {
   "L": "And there were many lamps in the upper room where we were gathered.",
   "M": "There were many lamps in the upstairs room where we were meeting.",
   "T": "The upstairs room where we were meeting was bright with many lamps."
  },
  "9": {
   "L": "And a young man named Eutychus, seated in the window, was sinking into a deep sleep; and as Paul continued talking, overcome by sleep, he fell from the third floor and was picked up dead.",
   "M": "Seated in a window was a young man named Eutychus, who was sinking into a deep sleep as Paul talked on and on. When he was sound asleep, he fell to the ground from the third storey and was picked up dead.",
   "T": "A young man named Eutychus was sitting in the window. As Paul talked on and on, Eutychus grew deeply asleep—and fell from the third story. When they picked him up, he was dead."
  },
  "10": {
   "L": "But Paul went down and fell upon him, and embracing him said: Do not be troubled, for his soul is in him.",
   "M": "Paul went down, threw himself on the young man and put his arms around him. Don't be alarmed, he said, he's alive!",
   "T": "Paul went down, threw himself over the young man, and put his arms around him. Don't panic—he's alive! he said."
  },
  "11": {
   "L": "And when he had gone back up and had broken the bread and eaten, he talked for a long time, until dawn, and so departed.",
   "M": "Then he went upstairs again and broke bread and ate. After talking until daylight, he left.",
   "T": "Paul went back upstairs, broke bread, and ate. He kept talking until dawn, then departed."
  },
  "12": {
   "L": "And they brought the boy away alive and were greatly comforted.",
   "M": "The people took the young man home alive and were greatly comforted.",
   "T": "The people took the young man home alive—and were enormously relieved."
  },
  "13": {
   "L": "But going ahead to the ship, we set sail to Assos, intending there to take Paul aboard, for so had he arranged, intending himself to go by land.",
   "M": "We went on ahead to the ship and sailed for Assos, where we were going to take Paul aboard. He had made this arrangement because he was going there on foot.",
   "T": "We went on ahead to the ship and sailed for Assos, planning to pick up Paul there—he had made arrangements to travel there by land."
  },
  "14": {
   "L": "And when he met us at Assos, we took him on board and came to Mitylene.",
   "M": "When he met us at Assos, we took him aboard and went on to Mitylene.",
   "T": "When he met us at Assos, we took him on board and went on to Mitylene."
  },
  "15": {
   "L": "And from there we sailed and arrived the following day opposite Chios; and the next day we crossed over to Samos; and the day following we came to Miletus.",
   "M": "The next day we set sail from there and arrived off Chios. The day after that we crossed over to Samos, and on the following day we arrived at Miletus.",
   "T": "The next day we arrived off Chios, the day after that we crossed to Samos, and the following day we arrived at Miletus."
  },
  "16": {
   "L": "For Paul had decided to sail past Ephesus, so that he might not spend time in Asia; for he was hurrying, if it were possible for him, to be in Jerusalem on the day of Pentecost.",
   "M": "Paul had decided to sail past Ephesus to avoid spending time in the province of Asia, for he was in a hurry to reach Jerusalem, if possible, by the day of Pentecost.",
   "T": "Paul had decided to bypass Ephesus to avoid spending time in the province of Asia—he was hurrying to reach Jerusalem, if at all possible, by the day of Pentecost."
  },
  "17": {
   "L": "And from Miletus, sending to Ephesus, he called to him the elders of the church.",
   "M": "From Miletus, Paul sent to Ephesus for the elders of the church.",
   "T": "From Miletus, Paul sent word to Ephesus for the elders of the church to meet him."
  },
  "18": {
   "L": "And when they came to him, he said to them: You yourselves know how I was with you the whole time from the first day I set foot in Asia,",
   "M": "When they arrived, he said to them: You know how I lived the whole time I was with you, from the first day I came into the province of Asia.",
   "T": "When they arrived, he said: You know how I lived among you the entire time from the first day I set foot in Asia."
  },
  "19": {
   "L": "serving the Lord with all humility and with tears and with trials that came upon me through the plots of the Jews,",
   "M": "I served the Lord with great humility and with tears and in the midst of severe testing by the plots of my Jewish opponents.",
   "T": "I served the Lord with deep humility—often in tears—and endured the trials that came from the plots of the Jewish leaders."
  },
  "20": {
   "L": "how I did not shrink back from declaring to you anything that was profitable, and teaching you publicly and from house to house,",
   "M": "You know that I have not hesitated to preach anything that would be helpful to you but have taught you publicly and from house to house.",
   "T": "I never held back anything that would help you. I taught you publicly and went from house to house."
  },
  "21": {
   "L": "testifying both to Jews and to Greeks of repentance toward God and faith toward our Lord Jesus Christ.",
   "M": "I have declared to both Jews and Greeks that they must turn to God in repentance and have faith in our Lord Jesus.",
   "T": "I declared to both Jews and Greeks that they must turn to God in repentance and trust in our Lord Jesus."
  },
  "22": {
   "L": "And now behold, I am going to Jerusalem, bound in the Spirit, not knowing what will happen to me there,",
   "M": "And now, compelled by the Spirit, I am going to Jerusalem, not knowing what will happen to me there.",
   "T": "And now, compelled by the Spirit, I am going to Jerusalem—not knowing what will happen to me there."
  },
  "23": {
   "L": "except that the Holy Spirit testifies to me in every city, saying that chains and afflictions are waiting for me.",
   "M": "I only know that in every city the Holy Spirit warns me that prison and hardships are facing me.",
   "T": "Only this: in every city the Holy Spirit warns me that chains and hardships are waiting for me."
  },
  "24": {
   "L": "But I do not count my life of any value to myself, if only I may finish my course and the ministry that I received from the Lord Jesus to testify to the gospel of the grace of God.",
   "M": "However, I consider my life worth nothing to me; my only aim is to finish the race and complete the task the Lord Jesus has given me—the task of testifying to the good news of God's grace.",
   "T": "But I don't place any value on my own life—my only goal is to finish the course and complete the mission the Lord Jesus gave me: to testify to the good news of God's grace."
  },
  "25": {
   "L": "And now behold, I know that all of you, among whom I went about proclaiming the kingdom, will see my face no longer.",
   "M": "Now I know that none of you among whom I have gone about preaching the kingdom will ever see me again.",
   "T": "I know that none of you to whom I have gone proclaiming the kingdom will ever see me again."
  },
  "26": {
   "L": "Therefore I testify to you on this day that I am innocent of the blood of all.",
   "M": "Therefore, I declare to you today that I am innocent of the blood of any of you.",
   "T": "So I declare to you today that I am innocent of the blood of all of you."
  },
  "27": {
   "L": "For I did not shrink back from declaring to you the whole counsel of God.",
   "M": "For I have not hesitated to proclaim to you the whole will of God.",
   "T": "I never held back from declaring to you the whole purpose of God."
  },
  "28": {
   "L": "Take heed to yourselves and to all the flock in which the Holy Spirit has appointed you overseers, to shepherd the church of God, which he obtained with his own blood.",
   "M": "Keep watch over yourselves and all the flock of which the Holy Spirit has made you overseers. Be shepherds of the church of God, which he bought with his own blood.",
   "T": "Guard yourselves and the entire flock over which the Holy Spirit has appointed you as overseers. Shepherd God's church—which he purchased at the cost of his own blood."
  },
  "29": {
   "L": "I know that after my departure savage wolves will come in among you, not sparing the flock.",
   "M": "I know that after I leave, savage wolves will come in among you and will not spare the flock.",
   "T": "I know that after I leave, savage wolves will come in among you and will not spare the flock."
  },
  "30": {
   "L": "And from among your own selves men will arise, speaking perverse things, to draw away the disciples after themselves.",
   "M": "Even from your own number men will arise and distort the truth in order to draw away disciples after them.",
   "T": "Even from within your own group, men will rise up and distort the truth to draw disciples after themselves."
  },
  "31": {
   "L": "Therefore be watchful, remembering that night and day for three years I did not cease to admonish each one with tears.",
   "M": "So be on your guard! Remember that for three years I never stopped warning each of you night and day with tears.",
   "T": "So stay alert! Remember that for three years, night and day, I kept warning each of you with tears."
  },
  "32": {
   "L": "And now I commend you to God and to the word of his grace, which is able to build up and to give the inheritance among all those who are sanctified.",
   "M": "Now I commit you to God and to the word of his grace, which can build you up and give you an inheritance among all those who are sanctified.",
   "T": "Now I entrust you to God and to the message of his grace—which is able to build you up and give you an inheritance among all who are set apart for him."
  },
  "33": {
   "L": "I coveted no one's silver or gold or clothing.",
   "M": "I have not coveted anyone's silver or gold or clothing.",
   "T": "I never wanted anyone's silver, gold, or clothing."
  },
  "34": {
   "L": "You yourselves know that these hands served my own needs and those who were with me.",
   "M": "You yourselves know that these hands of mine have supplied my own needs and the needs of my companions.",
   "T": "You know that these hands of mine worked to provide for my own needs and the needs of those who were with me."
  },
  "35": {
   "L": "In everything I showed you that by laboring thus you must help the weak, and remember the words of the Lord Jesus, how he himself said: It is more blessed to give than to receive.",
   "M": "In everything I did, I showed you that by this kind of hard work we must help the weak, remembering the words the Lord Jesus himself said: It is more blessed to give than to receive.",
   "T": "I showed you by example that by this kind of hard work we must help those who are weak. We should remember the words of the Lord Jesus himself: It is more blessed to give than to receive."
  },
  "36": {
   "L": "And when he had said these things, he knelt down and prayed with all of them.",
   "M": "When Paul had finished speaking, he knelt down with all of them and prayed.",
   "T": "When Paul had finished speaking, he knelt down and prayed with all of them."
  },
  "37": {
   "L": "And there was much weeping by all, and they fell on Paul's neck and kissed him,",
   "M": "They all wept as they embraced him and kissed him.",
   "T": "Everyone wept as they embraced Paul and kissed him."
  },
  "38": {
   "L": "grieving most of all over the word that he had spoken, that they were about to see his face no longer. And they accompanied him to the ship.",
   "M": "What grieved them most was his statement that they would never see his face again. Then they accompanied him to the ship.",
   "T": "What broke their hearts most was his saying that they would never see him again. They walked him down to the ship."
  }
 },
 "21": {
  "1": {
   "L": "And when it came to pass that we had parted from them and set sail, we ran a straight course to Cos, and the next day to Rhodes, and from there to Patara.",
   "M": "After we had torn ourselves away from them, we put out to sea and sailed straight to Kos. The next day we went to Rhodes and from there to Patara.",
   "T": "After tearing ourselves away from them, we set sail and went straight to Cos. The next day we reached Rhodes, and from there went on to Patara."
  },
  "2": {
   "L": "And finding a ship crossing to Phoenicia, we went aboard and set sail.",
   "M": "We found a ship crossing over to Phoenicia, went on board and set sail.",
   "T": "We found a ship making the crossing to Phoenicia, went aboard, and set sail."
  },
  "3": {
   "L": "When we had come in sight of Cyprus and left it on the left hand, we sailed to Syria and landed at Tyre; for there the ship was to unload its cargo.",
   "M": "After sighting Cyprus and passing to the south of it, we sailed on to Syria. We landed at Tyre, where our ship was to unload its cargo.",
   "T": "When Cyprus came into view, we left it to the south and sailed on to Syria, landing at Tyre, where the ship was to unload its cargo."
  },
  "4": {
   "L": "And finding the disciples, we stayed there seven days. And they were telling Paul through the Spirit not to set foot in Jerusalem.",
   "M": "We sought out the disciples there and stayed with them seven days. Through the Spirit they urged Paul not to go on to Jerusalem.",
   "T": "We found the believers there and stayed with them for a week. Through the Spirit, they kept urging Paul not to go to Jerusalem."
  },
  "5": {
   "L": "And when it came to pass that our days were completed, we departed and traveled on; and they all accompanied us, with wives and children, till we were outside the city; and kneeling down on the beach, we prayed",
   "M": "When it was time to leave, we left and continued on our way. All of them, including wives and children, accompanied us out of the city, and there on the beach we knelt to pray.",
   "T": "When the week was over, we set out. The whole community—wives and children included—walked us out of the city. On the beach we all knelt down and prayed."
  },
  "6": {
   "L": "and said farewell to one another; and we went on board the ship, and they returned home.",
   "M": "After saying goodbye to each other, we went aboard the ship, and they returned home.",
   "T": "We said our goodbyes, boarded the ship, and they went back home."
  },
  "7": {
   "L": "And completing the voyage from Tyre, we arrived at Ptolemais, and we greeted the brothers and stayed with them for one day.",
   "M": "We continued our voyage from Tyre and landed at Ptolemais, where we greeted the brothers and sisters and stayed with them for a day.",
   "T": "Continuing from Tyre, we arrived at Ptolemais, where we greeted the brothers and sisters and spent a day with them."
  },
  "8": {
   "L": "And the next day we departed and came to Caesarea, and entering the house of Philip the evangelist, who was one of the seven, we stayed with him.",
   "M": "Leaving the next day, we reached Caesarea and stayed at the house of Philip the evangelist, one of the Seven.",
   "T": "The next day we went to Caesarea and stayed at the home of Philip the evangelist, who was one of the Seven."
  },
  "9": {
   "L": "Now this man had four daughters, virgins, who were prophesying.",
   "M": "He had four unmarried daughters who prophesied.",
   "T": "He had four unmarried daughters who had the gift of prophecy."
  },
  "10": {
   "L": "And while we were staying there for several days, a certain prophet named Agabus came down from Judea.",
   "M": "After we had been there a number of days, a prophet named Agabus came down from Judea.",
   "T": "While we were staying there a few days, a prophet named Agabus arrived from Judea."
  },
  "11": {
   "L": "And coming to us, he took Paul's belt and binding his own feet and hands, said: Thus says the Holy Spirit: In this way the Jews in Jerusalem will bind the man whose belt this is and will deliver him into the hands of the Gentiles.",
   "M": "Coming over to us, he took Paul's belt, tied his own hands and feet with it and said: The Holy Spirit says, In this way the Jewish leaders in Jerusalem will bind the owner of this belt and will hand him over to the Gentiles.",
   "T": "He came up to Paul, took his belt, and used it to tie his own hands and feet. Then he said: This is what the Holy Spirit says—the Jewish leaders in Jerusalem will bind the man who owns this belt and hand him over to the Gentiles."
  },
  "12": {
   "L": "When we heard these things, both we and the local people urged him not to go up to Jerusalem.",
   "M": "When we heard this, we and the people there pleaded with Paul not to go up to Jerusalem.",
   "T": "When we heard this, we and the local people all begged Paul not to go to Jerusalem."
  },
  "13": {
   "L": "Then Paul answered: What are you doing, weeping and breaking my heart? For I am ready not only to be bound, but even to die in Jerusalem for the name of the Lord Jesus.",
   "M": "Then Paul answered: Why are you weeping and breaking my heart? I am ready not only to be bound, but also to die in Jerusalem for the name of the Lord Jesus.",
   "T": "Paul answered: Why are you crying and breaking my heart? I am ready not only to be bound but even to die in Jerusalem for the name of the Lord Jesus."
  },
  "14": {
   "L": "And when he would not be persuaded, we were silent, saying: Let the will of the Lord be done.",
   "M": "When he would not be dissuaded, we gave up and said: The Lord's will be done.",
   "T": "When he couldn't be talked out of it, we stopped trying and said: Let the Lord's will be done."
  },
  "15": {
   "L": "And after these days we made our preparations and went up to Jerusalem.",
   "M": "After this, we started on our way up to Jerusalem.",
   "T": "After this we packed our things and set out for Jerusalem."
  },
  "16": {
   "L": "And some of the disciples from Caesarea also came with us, bringing Mnason of Cyprus, an early disciple, with whom we were to lodge.",
   "M": "Some of the disciples from Caesarea accompanied us and brought us to the home of Mnason, where we were to stay. He was a man from Cyprus and one of the early disciples.",
   "T": "Some of the disciples from Caesarea came with us and took us to the home of Mnason of Cyprus, an early disciple, where we were to stay."
  },
  "17": {
   "L": "And when we arrived in Jerusalem, the brothers received us gladly.",
   "M": "When we arrived at Jerusalem, the brothers and sisters received us warmly.",
   "T": "When we arrived in Jerusalem, the believers welcomed us warmly."
  },
  "18": {
   "L": "And the next day Paul went in with us to James, and all the elders were present.",
   "M": "The next day Paul and the rest of us went to see James, and all the elders were present.",
   "T": "The following day Paul and the rest of us went to meet with James, and all the elders were there."
  },
  "19": {
   "L": "And greeting them, he was relating one by one what God had done among the Gentiles through his ministry.",
   "M": "Paul greeted them and reported in detail what God had done among the Gentiles through his ministry.",
   "T": "After greeting them, Paul gave a detailed account of everything God had done among the Gentiles through his ministry."
  },
  "20": {
   "L": "And when they heard it, they glorified God. And they said to him: You see, brother, how many tens of thousands there are among the Jews who have believed, and they are all zealous for the Law.",
   "M": "When they heard this, they praised God. Then they said to Paul: You see, brother, how many thousands of Jews have believed, and all of them are zealous for the law.",
   "T": "When they heard it, they praised God. Then they told Paul: You can see, brother, how many tens of thousands of Jewish people have believed—and they are all deeply committed to the law."
  },
  "21": {
   "L": "And they have been told about you, that you teach all the Jews who are among the Gentiles to forsake Moses, telling them not to circumcise their children nor to walk according to the customs.",
   "M": "They have been informed that you teach all the Jews who live among the Gentiles to turn away from Moses, telling them not to circumcise their children or live according to our customs.",
   "T": "They have been told that you teach all the Jews living among the Gentiles to abandon Moses—telling them not to circumcise their children or follow our ancestral customs."
  },
  "22": {
   "L": "What then is to be done? They will certainly hear that you have come.",
   "M": "What shall we do? They will certainly hear that you have come,",
   "T": "What should we do? They will certainly hear that you've arrived."
  },
  "23": {
   "L": "Therefore do this that we tell you: We have four men who have a vow upon themselves.",
   "M": "so do what we tell you. There are four men with us who have made a vow.",
   "T": "So here's what we want you to do: We have four men who have taken a vow."
  },
  "24": {
   "L": "Take these men and purify yourself along with them, and pay their expenses so that they may shave their heads. And all will know that there is nothing to the things they have been told about you, but that you yourself also walk in an orderly manner, keeping the Law.",
   "M": "Take these men, join in their purification rites and pay their expenses, so that they can have their heads shaved. Then everyone will know there is no truth in these reports about you, but that you yourself are living in obedience to the law.",
   "T": "Join in their purification rites and pay for their expenses so they can have their heads shaved. Then everyone will know that what they've heard about you isn't true—that you yourself live in obedience to the law."
  },
  "25": {
   "L": "But concerning the Gentiles who have believed, we sent a letter with our decision that they should abstain from what has been sacrificed to idols and from blood and from what has been strangled and from sexual immorality.",
   "M": "As for the Gentile believers, we have written to them our decision that they should abstain from food sacrificed to idols, from blood, from the meat of strangled animals and from sexual immorality.",
   "T": "As for the Gentile believers, we have already written to them with our ruling: they must abstain from food sacrificed to idols, from blood, from the meat of strangled animals, and from sexual immorality."
  },
  "26": {
   "L": "Then Paul took the men, and the next day, having purified himself together with them, he went into the temple, declaring the completion of the days of purification until the offering was presented for each one of them.",
   "M": "The next day Paul took the men and purified himself along with them. Then he went to the temple to give notice of the date when the days of purification would end and the offering would be made for each of them.",
   "T": "The next day Paul took the men and underwent purification with them. Then he went to the temple to give notice of when the purification days would end and the offering would be made for each of them."
  },
  "27": {
   "L": "And when the seven days were about to be completed, the Jews from Asia, seeing him in the temple, stirred up all the crowd and laid hands on him,",
   "M": "When the seven days were nearly over, some Jews from the province of Asia saw Paul at the temple. They stirred up the whole crowd and seized him,",
   "T": "When the seven days were nearly over, some Jewish people from the province of Asia spotted Paul in the temple. They stirred up the whole crowd and grabbed him,"
  },
  "28": {
   "L": "crying out: Men of Israel, help! This is the man who teaches everyone everywhere against the people and the Law and this place; and furthermore, he has even brought Greeks into the temple and has defiled this holy place.",
   "M": "shouting: Fellow Israelites, help us! This is the man who teaches everyone everywhere against our people and our law and this place. And besides, he has brought Greeks into the temple and defiled this holy place.",
   "T": "shouting: People of Israel, help! This is the man who teaches everyone everywhere against our people, our law, and this place. And now he's even brought Greeks into the temple and defiled this holy ground!"
  },
  "29": {
   "L": "For they had previously seen Trophimus the Ephesian in the city with him, whom they supposed Paul had brought into the temple.",
   "M": "They had previously seen Trophimus the Ephesian in the city with Paul and assumed that Paul had brought him into the temple.",
   "T": "They had seen Trophimus the Ephesian with Paul in the city and assumed Paul had brought him into the temple."
  },
  "30": {
   "L": "And the whole city was stirred up, and the people ran together; and they seized Paul and dragged him out of the temple, and immediately the doors were shut.",
   "M": "The whole city was aroused, and the people came running from all directions. Seizing Paul, they dragged him from the temple, and immediately the gates were shut.",
   "T": "The whole city was in an uproar. People came running from every direction. They seized Paul and dragged him out of the temple, and the gates were immediately shut behind him."
  },
  "31": {
   "L": "And as they were seeking to kill him, a report came up to the commander of the cohort that all Jerusalem was in confusion.",
   "M": "While they were trying to kill him, news reached the commander of the Roman troops that the whole city of Jerusalem was in an uproar.",
   "T": "While they were trying to kill him, word reached the commander of the Roman troops that all Jerusalem was in chaos."
  },
  "32": {
   "L": "He immediately took soldiers and centurions and ran down to them. And when they saw the commander and the soldiers, they stopped beating Paul.",
   "M": "He at once took some officers and soldiers and ran down to the crowd. When the rioters saw the commander and his soldiers, they stopped beating Paul.",
   "T": "He immediately took soldiers and officers and rushed down to the crowd. When the mob saw the commander with his soldiers, they stopped beating Paul."
  },
  "33": {
   "L": "Then the commander came near and took hold of him and ordered him to be bound with two chains; and he was asking who he was and what he had done.",
   "M": "The commander came up and arrested him and ordered him to be bound with two chains. Then he asked who he was and what he had done.",
   "T": "The commander came up, arrested Paul, and ordered him chained with two chains. He then asked who Paul was and what he had done."
  },
  "34": {
   "L": "And some in the crowd were shouting one thing and some another; and when he could not find out the truth because of the uproar, he ordered him to be brought into the barracks.",
   "M": "Some in the crowd shouted one thing and some another, and since the commander could not get at the truth because of the uproar, he ordered that Paul be taken into the barracks.",
   "T": "Different people in the crowd shouted different things. Unable to get at the truth through the uproar, the commander ordered Paul taken into the barracks."
  },
  "35": {
   "L": "And when he came to the steps, it happened that he was carried by the soldiers because of the violence of the crowd,",
   "M": "When Paul reached the steps, the violence of the mob was so great he had to be carried by the soldiers.",
   "T": "When Paul reached the steps, the mob was so violent that the soldiers had to carry him."
  },
  "36": {
   "L": "for the multitude of the people followed, crying out: Away with him!",
   "M": "The crowd that followed kept shouting: Get rid of him!",
   "T": "The crowd surged behind them, shouting: Away with him!"
  },
  "37": {
   "L": "And as he was about to be brought into the barracks, Paul said to the commander: Am I permitted to say something to you? And he said: You know Greek?",
   "M": "As the soldiers were about to take Paul into the barracks, he asked the commander: May I say something to you? Do you speak Greek? the commander replied.",
   "T": "As the soldiers were about to take him inside, Paul asked the commander: May I say something to you? The commander said: Do you speak Greek?"
  },
  "38": {
   "L": "Were you not then the Egyptian who before these days stirred up a revolt and led four thousand men of the Assassins out into the wilderness?",
   "M": "Aren't you the Egyptian who started a revolt and led four thousand terrorists out into the wilderness some time ago?",
   "T": "Aren't you the Egyptian who started that revolt not long ago and led four thousand assassins out into the desert?"
  },
  "39": {
   "L": "But Paul said: I am a Jew from Tarsus in Cilicia, a citizen of no insignificant city. I beg you, permit me to speak to the people.",
   "M": "Paul answered: I am a Jew, from Tarsus in Cilicia, a citizen of no ordinary city. Please let me speak to the people.",
   "T": "Paul answered: I am a Jew—a citizen of Tarsus in Cilicia, no insignificant city. Please allow me to speak to the people."
  },
  "40": {
   "L": "And when he had given him permission, Paul, standing on the steps, motioned to the people with his hand. And when a great silence fell, he spoke to them in the Hebrew dialect, saying:",
   "M": "After receiving the commander's permission, Paul stood on the steps and motioned to the crowd. When they were all silent, he said to them in Aramaic:",
   "T": "After receiving permission, Paul stood on the steps and motioned to the crowd. When silence fell, he addressed them in Aramaic:"
  }
 }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'acts')
        merge_tier(existing, ACTS_16_21, tier_key)
        save(tier_dir, 'acts', existing)
    print('Acts 16–21 written.')

if __name__ == '__main__':
    main()
