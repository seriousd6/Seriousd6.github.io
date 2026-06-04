"""
MKT Acts chapters 22–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-acts-22-24.py

Translation decisions (consistent with mkt-acts-11-15.py and mkt-acts-6-10.py):
- πνεῦμα (Spirit): capitalised for Holy Spirit; lowercase for human spirit.
- κύριος (Lord): retained throughout; context clarifies referent.
- Χριστός (Christ): "Christ" L/M; "Messiah" in T when the title is foregrounded
  (e.g. 24:24 where Paul speaks "concerning the faith in Christ Jesus" to Felix who
  is evaluating the movement as such — Anointed King dimension is relevant).
- ἐκκλησία: "assembly" (L), "church" (M), "community" (T).
- ὁδός ("the Way"): retained as "the Way" across all tiers — it is Luke's own term
  for the Jesus movement and carries programmatic force (cf. 9:2, 19:9, 22:4, 24:14).
- βαπτίζω: "baptize" (L/M); "immerse" in T (22:16) where the water rite is explicit.
- ἄφεσις: "forgiveness" across M/T; "remission" only if fully literal context demands.
- δικαιοσύνη (24:25): "righteousness" L/M; "the right way to live" T — in context Paul
  is reasoning through moral categories (righteousness, self-control, judgment) that
  would alarm a corrupt official. Not a forensic justification context.
- Aorist verbs = completed acts (L/M/T consistent); presents = ongoing.
- Roman citizenship (22:25-29): the legal stakes are high — "Roman" = "Roman citizen";
  "uncondemned" preserves the legal terminology of ἀκατάκριτος.
- Paul's speech in 22:1 is addressed to a mixed Jerusalem crowd; the Aramaic/Hebrew
  audience is noted at v2. T tier renders this as direct and personal, not polished.
- Tertullus's speech (24:2-9): flattery is heavy and formulaic — L reproduces the
  rhetoric; T exposes the courtly manipulation underneath. "Sect of the Nazarenes"
  (αἵρεσιν τῶν Ναζωραίων, 24:5) kept as "sect/movement" in L/M, "movement" in T.
- Acts 24:7 is absent from NA28 (Western text addition); the interlinear file includes
  it as v7, so it is translated minimally here with a bracketed note in L.
- Ananias (23:2): this is Ananias son of Nedebaeus, high priest c. AD 47–58, distinct
  from Ananias in ch. 5; no gloss needed but worth noting.
- The letter of Claudius Lysias (23:26-30) is formal Roman epistolary prose;
  L tier maintains the stiff formality; M tidies it; T renders it as a working document.
- OT intertextuality: Paul's citation of Exod 22:28 ("You shall not speak evil of a
  ruler of your people") at 23:5 is rendered close to LXX in L; as living moral
  appeal in T.
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

  # ── CHAPTER 22 ────────────────────────────────────────────────────────────────
  # Paul's defence speech to the Jerusalem crowd; arrest under Roman custody.
  "22": {
    "1": {
      "L": "Men, brothers and fathers, hear my defence which I now make before you.",
      "M": "Brothers and fathers, listen now to my defence.",
      "T": "Friends—brothers and fathers—please hear my case."
    },
    "2": {
      "L": "And when they heard that he was speaking to them in the Hebrew tongue, they kept the more silence. And he says:",
      "M": "When they heard him speak to them in Aramaic, they became even quieter. Then Paul said:",
      "T": "When they heard him speaking in their own Aramaic, the crowd fell into a deeper silence. Paul went on:"
    },
    "3": {
      "L": "I am a Jewish man, born in Tarsus of Cilicia, yet brought up in this city, educated at the feet of Gamaliel, trained according to the strict manner of the law of our fathers, being zealous for God, just as you all are today.",
      "M": "I am a Jew, born in Tarsus in Cilicia, but raised here in Jerusalem. I was educated under Gamaliel and trained thoroughly in the law of our ancestors. I was just as zealous for God as any of you are today.",
      "T": "I am a Jew—born in Tarsus of Cilicia but raised right here in this city. I was trained at Gamaliel's feet in the precise keeping of our ancestral law, burning with zeal for God just as you all are."
    },
    "4": {
      "L": "I persecuted this Way to the death, binding and delivering both men and women to prisons,",
      "M": "I persecuted the followers of this Way to their death, arresting both men and women and throwing them into prison,",
      "T": "I hunted down the followers of the Way to their deaths—men and women alike—arresting them and throwing them in prison."
    },
    "5": {
      "L": "as the high priest also bears witness to me, and all the council of elders; from whom I also received letters to the brothers, and I was travelling to Damascus to bring those who were there bound to Jerusalem to be punished.",
      "M": "as the high priest and the whole council of elders can testify. I received letters from them authorizing me to go to Damascus, where I planned to arrest the followers of the Way and bring them back to Jerusalem to be punished.",
      "T": "The high priest himself and the entire council of elders can confirm it. I received official letters from them and was on my way to Damascus to arrest any followers of the Way I could find and drag them back to Jerusalem for punishment."
    },
    "6": {
      "L": "And it came about to me as I was travelling and drawing near to Damascus, that about midday suddenly a great light from heaven shone around me.",
      "M": "About noon as I was approaching Damascus, suddenly a bright light from heaven flashed around me.",
      "T": "As I was travelling and nearing Damascus—it was around midday—a brilliant light from heaven suddenly blazed all around me."
    },
    "7": {
      "L": "And I fell to the ground and heard a voice saying to me: 'Saul, Saul, why do you persecute me?'",
      "M": "I fell to the ground and heard a voice say to me, 'Saul! Saul! Why do you persecute me?'",
      "T": "I fell face down to the ground and heard a voice calling out, 'Saul! Saul! Why are you persecuting me?'"
    },
    "8": {
      "L": "And I answered: 'Who are you, Lord?' And he said to me: 'I am Jesus of Nazareth whom you are persecuting.'",
      "M": "'Who are you, Lord?' I asked. 'I am Jesus of Nazareth, whom you are persecuting,' he replied.",
      "T": "'Who are you, Lord?' I asked. The voice answered, 'I am Jesus of Nazareth—the very one you are persecuting.'"
    },
    "9": {
      "L": "And those who were with me saw the light, but they did not hear the voice of the one who was speaking to me.",
      "M": "My companions saw the light, but they did not hear the voice of him who was speaking to me.",
      "T": "My companions saw the light, but they could not make out the words of the voice speaking to me."
    },
    "10": {
      "L": "And I said: 'What shall I do, Lord?' And the Lord said to me: 'Rise and go into Damascus, and there you will be told about all the things that have been appointed for you to do.'",
      "M": "'What shall I do, Lord?' I asked. 'Get up,' the Lord said, 'and go into Damascus. There you will be told everything you have been assigned to do.'",
      "T": "'Lord, what should I do?' The Lord told me, 'Get up and go into Damascus. There everything laid out for you will be made clear.'"
    },
    "11": {
      "L": "And since I could not see because of the glory of that light, being led by the hand of those who were with me, I came into Damascus.",
      "M": "My eyes had been blinded by the brilliance of that light, so my companions led me by the hand into Damascus.",
      "T": "The glory of that light had blinded me. My companions led me by the hand all the way into Damascus."
    },
    "12": {
      "L": "And one Ananias, a devout man according to the law, well spoken of by all the Jews who lived there,",
      "M": "A man named Ananias came to see me. He was a devout observer of the law and highly regarded by all the Jewish residents of Damascus.",
      "T": "A man named Ananias came to visit me—a devout man, faithful to the law, and held in high esteem by all the Jews living in Damascus."
    },
    "13": {
      "L": "came to me, and standing beside me said to me: 'Brother Saul, receive your sight.' And I myself looked up at him in that very hour.",
      "M": "He stood beside me and said, 'Brother Saul, receive your sight!' And at that very moment I was able to see him.",
      "T": "He stood beside me and said, 'Brother Saul—receive your sight!' At that instant my sight returned and I could see him."
    },
    "14": {
      "L": "And he said: 'The God of our fathers has appointed you to know his will and to see the Just One and to hear a voice from his own mouth,",
      "M": "'The God of our ancestors has chosen you to know his will and to see the Righteous One and to hear words from his own mouth.'",
      "T": "'The God of our ancestors has chosen you,' he said, 'to know his will, to see the Righteous One, and to hear his own voice directly.'"
    },
    "15": {
      "L": "for you will be a witness for him to all people of what you have seen and heard.",
      "M": "'You will be his witness to all people of what you have seen and heard.'",
      "T": "'You will carry his message as a witness to all humanity—testifying to what you have personally seen and heard.'"
    },
    "16": {
      "L": "And now why do you delay? Rise and be baptized and wash away your sins, calling on his name.",
      "M": "'And now, what are you waiting for? Get up, be baptized and wash your sins away, calling on his name.'",
      "T": "'So what are you waiting for? Get up, be immersed, and have your sins washed away—call on his name now!'"
    },
    "17": {
      "L": "And it came about to me, when I had returned to Jerusalem and was praying in the temple, that I fell into a trance,",
      "M": "'When I returned to Jerusalem and was praying at the temple, I fell into a trance.'",
      "T": "'Later, when I was back in Jerusalem and praying in the temple, I fell into a trance.'"
    },
    "18": {
      "L": "and I saw him saying to me: 'Make haste and get out of Jerusalem quickly, because they will not receive your testimony about me.'",
      "M": "'I saw the Lord speaking to me: \"Leave Jerusalem immediately—they will not accept your testimony about me.\"'",
      "T": "'I saw the Lord speaking to me: \"Go quickly—get out of Jerusalem. They won\'t receive your testimony about me.\"'"
    },
    "19": {
      "L": "And I said: 'Lord, they themselves know that I was imprisoning and beating in every synagogue those who believed on you,",
      "M": "'Lord,' I replied, 'they know very well that I used to go from synagogue to synagogue imprisoning and flogging those who believed in you.'",
      "T": "'But Lord,' I said, 'they know exactly what I used to do—going from synagogue to synagogue, arresting and flogging those who put their faith in you.'"
    },
    "20": {
      "L": "and when the blood of your witness Stephen was shed, I myself also was standing by and giving approval, and guarding the garments of those who were killing him.'",
      "M": "'And when your witness Stephen was killed, I was standing there giving my full approval, watching over the clothes of those who were killing him.'",
      "T": "'And when they shed the blood of Stephen, your witness, I was standing right there—giving my complete approval, holding the cloaks of his killers.'"
    },
    "21": {
      "L": "And he said to me: 'Go, for I will send you far away to the Gentiles.'",
      "M": "'Go,' the Lord said to me, 'for I will send you far away to the Gentiles.'",
      "T": "'\"Go,\" the Lord said, \"for I am sending you far away—to the Gentiles.\"'"
    },
    "22": {
      "L": "And up to this word they gave him audience; and they lifted up their voice and said: 'Away with such a fellow from the earth! For it is not fitting for him to live!'",
      "M": "The crowd listened to Paul until he said this. Then they raised their voices and shouted, 'Rid the earth of him! He's not fit to live!'",
      "T": "The crowd had been listening right up to that one word. Then they erupted: 'Kill him! Take this man off the face of the earth! He doesn't deserve to live!'"
    },
    "23": {
      "L": "And as they were crying out and tearing off their garments and casting dust into the air,",
      "M": "As they were shouting and throwing off their cloaks and flinging dust into the air,",
      "T": "They were screaming, ripping off their cloaks, hurling dust into the air—"
    },
    "24": {
      "L": "the commander commanded him to be brought into the barracks, and said that he should be examined by scourging, so that he might find out why they were shouting against him like this.",
      "M": "the commander ordered Paul to be taken into the barracks. He directed that he be flogged and interrogated in order to find out why the crowd was shouting at him like this.",
      "T": "the commander had Paul hauled into the barracks. He ordered him flogged under interrogation—he wanted to know exactly what had set off the crowd."
    },
    "25": {
      "L": "But as they stretched him out with the straps, Paul said to the centurion who was standing nearby: 'Is it lawful for you to scourge a man who is a Roman citizen and has not been condemned?'",
      "M": "As they stretched Paul out to flog him, he said to the centurion standing there, 'Is it legal for you to flog a Roman citizen who hasn't even been tried?'",
      "T": "They were already strapping Paul down for the flogging when Paul spoke to the centurion standing nearby: 'Is it legal for you to flog a Roman citizen without a trial?'"
    },
    "26": {
      "L": "And hearing this, the centurion went and told the commander, saying: 'See what you are about to do, for this man is a Roman citizen.'",
      "M": "When the centurion heard this, he went to the commander and reported it. 'Watch what you are about to do,' he said. 'This man is a Roman citizen.'",
      "T": "The centurion heard it and went straight to the commander. 'Do you realize what you're about to do? This man is a Roman citizen.'"
    },
    "27": {
      "L": "And the commander came and said to him: 'Tell me, are you a Roman citizen?' And he said: 'Yes.'",
      "M": "The commander came over and asked, 'Tell me—are you a Roman citizen?' 'Yes, I am,' Paul answered.",
      "T": "The commander came himself. 'Are you really a Roman citizen?' he demanded. 'Yes,' Paul said."
    },
    "28": {
      "L": "And the commander answered: 'I acquired this citizenship for a large sum.' And Paul said: 'But I was born a citizen.'",
      "M": "'I had to pay a great deal of money for my citizenship,' the commander said. Paul replied, 'But I was born one.'",
      "T": "'I bought my citizenship—it cost a great deal,' the commander said. 'Mine came by birth,' Paul replied."
    },
    "29": {
      "L": "Therefore those who were about to examine him immediately withdrew from him; and the commander also was afraid, because he realized that Paul was a Roman citizen and that he had bound him.",
      "M": "Those who were about to interrogate him immediately backed off. The commander was also alarmed when he realized that Paul was a Roman citizen and that he had put him in chains.",
      "T": "The men who were about to interrogate Paul stepped back immediately. The commander himself was shaken—he had chained a Roman citizen."
    },
    "30": {
      "L": "But on the next day, desiring to know the truth about why he was being accused by the Jews, he released him and commanded the chief priests and all their council to assemble; and bringing Paul down, he set him before them.",
      "M": "The next day, since the commander wanted to find out exactly why Paul was being accused by the Jewish leaders, he released him from his chains and ordered the chief priests and the entire Sanhedrin to assemble. Then he brought Paul down and set him before them.",
      "T": "The following day the commander decided he needed to know the real charge against Paul. He had the chains removed, summoned the chief priests and the whole Sanhedrin, and brought Paul down to stand before them."
    }
  },

  # ── CHAPTER 23 ────────────────────────────────────────────────────────────────
  # Paul before the Sanhedrin; the conspiracy; the letter; transfer to Caesarea.
  "23": {
    "1": {
      "L": "And Paul, gazing intently at the council, said: 'Brothers, I have lived my life before God in all good conscience up to this day.'",
      "M": "Paul looked straight at the Sanhedrin and said, 'My brothers, I have fulfilled my duty to God in all good conscience to this day.'",
      "T": "Paul looked the Sanhedrin full in the face and spoke: 'My brothers, I have lived before God with a completely clear conscience right up to this very moment.'"
    },
    "2": {
      "L": "And Ananias the high priest commanded those who were standing beside him to strike him on the mouth.",
      "M": "At this, the high priest Ananias ordered those standing near Paul to strike him on the mouth.",
      "T": "At that, the high priest Ananias ordered the men standing beside Paul to strike him across the mouth."
    },
    "3": {
      "L": "Then Paul said to him: 'God is going to strike you, you whitewashed wall! And do you sit to judge me according to the law, and contrary to the law you command me to be struck?'",
      "M": "Then Paul said to him, 'God will strike you, you whitewashed wall! You sit there to judge me according to the law, yet you yourself violate the law by commanding that I be struck?'",
      "T": "Paul fired back: 'God will strike you down, you whitewashed wall! You sit there to judge me by the law—and then break the very law yourself by ordering me struck?'"
    },
    "4": {
      "L": "And those who were standing by said: 'Do you revile the high priest of God?'",
      "M": "Those standing near Paul said, 'How dare you insult God's high priest!'",
      "T": "'How dare you insult God's high priest!' the bystanders objected."
    },
    "5": {
      "L": "And Paul said: 'I did not know, brothers, that he was the high priest; for it is written: \"You shall not speak evil of a ruler of your people.\"'",
      "M": "Paul replied, 'Brothers, I did not realize that he was the high priest; for it is written: \"Do not speak evil about the ruler of your people.\"'",
      "T": "'Brothers, I didn't realize he was the high priest,' Paul said. 'I know the scripture: \"You must not speak evil of the ruler of your people.\"'"
    },
    "6": {
      "L": "But when Paul perceived that one part were Sadducees and the other Pharisees, he cried out in the council: 'Brothers, I am a Pharisee, a son of Pharisees. Concerning the hope and the resurrection of the dead I am being judged.'",
      "M": "Then Paul, knowing that some of them were Sadducees and the others Pharisees, called out in the Sanhedrin: 'My brothers, I am a Pharisee, the son of a Pharisee. I stand on trial because of my hope in the resurrection of the dead.'",
      "T": "Paul saw his moment: half the council were Sadducees, the other half Pharisees. He called out to all of them: 'My brothers, I am a Pharisee—a Pharisee's son! It is the hope of the resurrection that puts me on trial here today!'"
    },
    "7": {
      "L": "And when he said this, a dissension arose between the Pharisees and the Sadducees; and the assembly was divided.",
      "M": "When he said this, a dispute broke out between the Pharisees and the Sadducees, and the assembly was divided.",
      "T": "The moment he said it, an argument erupted between the Pharisees and the Sadducees, and the council split down the middle."
    },
    "8": {
      "L": "(For the Sadducees say there is no resurrection, nor angel, nor spirit; but the Pharisees acknowledge them all.)",
      "M": "(The Sadducees say that there is no resurrection, and that there are neither angels nor spirits, but the Pharisees acknowledge all these things.)",
      "T": "(The Sadducees held that there is no resurrection—no angels, no spirits at all. The Pharisees affirmed all three.)"
    },
    "9": {
      "L": "And there arose a great outcry; and some of the scribes of the Pharisees' party stood up and began to contend, saying: 'We find nothing wrong in this man. What if a spirit or an angel has spoken to him?'",
      "M": "There was a great uproar, and some of the teachers of the law who were Pharisees stood up and argued vigorously. 'We find nothing wrong with this man,' they said. 'What if a spirit or an angel has spoken to him?'",
      "T": "The place erupted. Some of the Pharisee scribes jumped to their feet and argued forcefully: 'We find nothing wrong with this man. What if a spirit or an angel really did speak to him?'"
    },
    "10": {
      "L": "And when the dissension became great, the commander, afraid that Paul would be torn in pieces by them, commanded the soldiers to go down and take him away from among them by force, and to bring him into the barracks.",
      "M": "The dispute became so violent that the commander was afraid Paul would be torn to pieces by them. He ordered the soldiers to go down and take him away by force and bring him into the barracks.",
      "T": "The argument turned violent. The commander, fearing Paul would be literally torn apart, ordered his soldiers to rush down, snatch Paul out of the middle of them, and bring him back to the barracks."
    },
    "11": {
      "L": "And the following night the Lord stood by him and said: 'Take courage; for as you have testified about the things concerning me in Jerusalem, so you must also testify in Rome.'",
      "M": "The following night the Lord stood near Paul and said, 'Take courage! As you have testified about me in Jerusalem, so you must also testify in Rome.'",
      "T": "That night the Lord appeared at Paul's side: 'Be courageous,' he said. 'You have borne witness for me in Jerusalem. You must do the same in Rome.'"
    },
    "12": {
      "L": "And when day came, the Jews formed a conspiracy and bound themselves under a curse, saying neither to eat nor to drink until they had killed Paul.",
      "M": "The next morning some Jews formed a conspiracy and bound themselves with an oath not to eat or drink until they had killed Paul.",
      "T": "At daybreak a group of Jews formed a conspiracy and took a solemn oath—they would neither eat nor drink until Paul was dead."
    },
    "13": {
      "L": "And there were more than forty who had formed this conspiracy.",
      "M": "More than forty men were involved in this plot.",
      "T": "More than forty men bound themselves to this oath."
    },
    "14": {
      "L": "And they went to the chief priests and the elders and said: 'We have bound ourselves under a great curse to taste nothing until we have killed Paul.",
      "M": "They went to the chief priests and elders and said, 'We have taken a solemn oath not to eat anything until we have killed Paul.",
      "T": "They went to the chief priests and elders with their scheme: 'We've sworn a solemn oath—we won't eat a thing until Paul is dead."
    },
    "15": {
      "L": "Now therefore you, with the council, give notice to the commander to bring him down to you, as though you are going to examine his case more carefully; and we are ready to kill him before he comes near.'",
      "M": "'Now then, you and the Sanhedrin petition the commander to bring him to you on the pretext that you want to examine his case more thoroughly. We will be ready to kill him before he gets here.'",
      "T": "'Here's what you do: you and the Sanhedrin petition the commander to bring Paul down to you, claiming you need to look into his case more carefully. We'll be waiting in ambush to kill him before he even arrives.'"
    },
    "16": {
      "L": "But Paul's sister's son heard of their ambush, and he came and entered the barracks and told Paul.",
      "M": "But when Paul's nephew heard about this plot, he went into the barracks and told Paul.",
      "T": "Paul's nephew got wind of the ambush. He went straight to the barracks and told Paul."
    },
    "17": {
      "L": "And Paul, calling one of the centurions, said: 'Take this young man to the commander, for he has something to report to him.'",
      "M": "Paul called one of the centurions and said, 'Take this young man to the commander; he has something to report.'",
      "T": "Paul summoned one of the centurions. 'Take this young man to the commander,' he said. 'He has something important to tell him.'"
    },
    "18": {
      "L": "He therefore took him and brought him to the commander and said: 'The prisoner Paul called me and asked me to bring this young man to you, for he has something to say to you.'",
      "M": "So the centurion took the young man to the commander. 'The prisoner Paul asked me to bring this young man to you,' he said. 'He has something to tell you.'",
      "T": "The centurion took the young man to the commander. 'The prisoner Paul called me over and asked me to bring this young man to you,' he said. 'He has something to report.'"
    },
    "19": {
      "L": "And the commander, taking him by the hand, withdrew privately and asked: 'What is it that you have to report to me?'",
      "M": "The commander took the young man by the hand, drew him aside privately, and asked, 'What is it you want to tell me?'",
      "T": "The commander took the young man by the hand and stepped aside with him privately. 'What is it you have to tell me?' he asked."
    },
    "20": {
      "L": "And he said: 'The Jews have agreed to ask you to bring Paul down to the council tomorrow, as though you were going to inquire more carefully about him.",
      "M": "He said, 'The Jewish leaders have agreed to ask you to bring Paul before the Sanhedrin tomorrow, on the pretext of wanting to examine his case more carefully.",
      "T": "'The Jewish leaders have agreed to ask you to bring Paul before the Sanhedrin tomorrow,' he said, 'under the pretense of examining his case more closely."
    },
    "21": {
      "L": "But do not be persuaded by them; for more than forty of their men are lying in ambush for him, who have bound themselves by an oath neither to eat nor to drink until they have killed him; and now they are ready, waiting for your promise.'",
      "M": "'Don't give in to them, because more than forty of them are waiting to ambush him. They have sworn an oath not to eat or drink until they have killed him. Right now they are armed and waiting for your agreement.'",
      "T": "'Don't comply with their request. More than forty of their men are lying in ambush for him—they've taken a solemn oath not to eat or drink until they've killed him. They're poised and waiting for your word right now.'"
    },
    "22": {
      "L": "The commander therefore dismissed the young man, charging him: 'Tell no one that you have reported these things to me.'",
      "M": "The commander dismissed the young man with a warning: 'Don't tell anyone you have reported this to me.'",
      "T": "The commander sent the young man away with strict orders: 'Don't breathe a word to anyone that you've told me this.'"
    },
    "23": {
      "L": "And calling to him two of the centurions, he said: 'Get ready two hundred soldiers to go as far as Caesarea, and seventy horsemen and two hundred spearmen, at the third hour of the night.'",
      "M": "Then he called two of his centurions and ordered them: 'Get ready a detachment of two hundred soldiers, seventy horsemen and two hundred spearmen to go to Caesarea at nine o'clock tonight.'",
      "T": "He summoned two of his centurions. 'Have two hundred infantry ready to move to Caesarea tonight at nine o'clock—plus seventy cavalry and two hundred spearmen.'"
    },
    "24": {
      "L": "Also provide mounts for Paul to ride, and bring him safely to Felix the governor.",
      "M": "'Provide horses for Paul to ride and take him safely to Governor Felix.'",
      "T": "'Get horses for Paul to ride and bring him safely to Governor Felix.'"
    },
    "25": {
      "L": "And he wrote a letter having this form:",
      "M": "He wrote a letter as follows:",
      "T": "He also sent this letter ahead:"
    },
    "26": {
      "L": "Claudius Lysias, to the most excellent governor Felix: Greetings.",
      "M": "Claudius Lysias, To His Excellency, Governor Felix: Greetings.",
      "T": "From Claudius Lysias — To His Excellency, Governor Felix: Greetings."
    },
    "27": {
      "L": "This man was seized by the Jews and was about to be killed by them, when I came upon them with the soldiers and rescued him, having learned that he was a Roman citizen.",
      "M": "'This man was seized by the Jews and they were about to kill him, but I came with my soldiers and rescued him, for I had learned that he is a Roman citizen.'",
      "T": "'This man was seized by Jews and was about to be killed. I intervened with my troops and got him out — I had found out he is a Roman citizen.'"
    },
    "28": {
      "L": "And wishing to know the charge for which they were accusing him, I brought him down to their council.",
      "M": "'I wanted to know why they were accusing him, so I brought him to their Sanhedrin.'",
      "T": "'Wanting to know the specific charge against him, I brought him before their council.'"
    },
    "29": {
      "L": "I found that he was being accused about questions of their law, but had nothing charged against him worthy of death or of bonds.",
      "M": "'I found that the accusation had to do with disputes about their own law, but there was no charge against him that deserved death or imprisonment.'",
      "T": "'The charges all turned on disputes about their own law. Nothing against him warranted death or even imprisonment.'"
    },
    "30": {
      "L": "And when it was disclosed to me that there would be a plot against the man, I sent him to you at once, also ordering his accusers to state before you what they have against him. Farewell.",
      "M": "'When I was informed of a plot against the man, I sent him to you at once. I have also ordered his accusers to present to you their case against him. Farewell.'",
      "T": "'When I learned of a plot against him, I sent him to you immediately. I have instructed his accusers to lay out their case before you. Farewell.'"
    },
    "31": {
      "L": "So the soldiers, according to what had been ordered them, took Paul and brought him by night to Antipatris.",
      "M": "So the soldiers, carrying out their orders, took Paul with them during the night and brought him as far as Antipatris.",
      "T": "The soldiers followed their orders: they moved Paul out under cover of night and brought him all the way to Antipatris."
    },
    "32": {
      "L": "And on the next day, leaving the horsemen to go on with him, they returned to the barracks.",
      "M": "The next day they let the cavalry continue with Paul while they returned to the barracks.",
      "T": "The next morning they handed Paul over to the cavalry escort and marched back to Jerusalem."
    },
    "33": {
      "L": "When they came to Caesarea and delivered the letter to the governor, they presented Paul before him also.",
      "M": "When the cavalry arrived in Caesarea, they delivered the letter to the governor and handed Paul over to him.",
      "T": "On arriving in Caesarea, they delivered the letter to the governor and presented Paul before him."
    },
    "34": {
      "L": "And when he had read it, and had asked from what province he was, and learned that he was from Cilicia,",
      "M": "The governor read the letter and asked what province Paul was from. On learning that he was from Cilicia,",
      "T": "Felix read the letter and asked what province Paul came from. When he learned it was Cilicia,"
    },
    "35": {
      "L": "he said: 'I will hear your case when your accusers also arrive.' And he commanded him to be kept in Herod's praetorium.",
      "M": "he said, 'I will hear your case when your accusers get here.' And he ordered that Paul be kept under guard in Herod's palace.",
      "T": "he said, 'I will give you a hearing once your accusers arrive,' and ordered Paul held in custody at Herod's palace."
    }
  },

  # ── CHAPTER 24 ────────────────────────────────────────────────────────────────
  # Paul before Felix: Tertullus prosecutes; Paul defends; Felix defers; two years pass.
  "24": {
    "1": {
      "L": "And after five days Ananias the high priest came down with certain elders and an orator named Tertullus, and they informed the governor against Paul.",
      "M": "Five days later the high priest Ananias went down to Caesarea with some of the elders and a lawyer named Tertullus, and they brought their charges against Paul before the governor.",
      "T": "Five days later the high priest Ananias arrived in Caesarea with a delegation of elders and a professional advocate named Tertullus. They formally presented their charges against Paul to the governor."
    },
    "2": {
      "L": "And when he was called, Tertullus began to accuse him, saying: 'Since we enjoy much peace through you, and since improvements have been made for this nation through your foresight, most excellent Felix,'",
      "M": "When Paul was called in, Tertullus presented his case before Felix: 'We have enjoyed a long period of peace under you, and your foresight has brought about reforms in this nation, most excellent Felix.'",
      "T": "Tertullus was called forward and opened his speech: 'Through you, Your Excellency Felix, we have enjoyed prolonged peace, and your wise governance has brought real improvements to this nation.'"
    },
    "3": {
      "L": "'in every way and in every place we receive this with all thankfulness, most excellent Felix.'",
      "M": "'Everywhere and in every way, most excellent Felix, we acknowledge this with profound gratitude.'",
      "T": "'We acknowledge this everywhere and in every way with the deepest gratitude, most excellent Felix.'"
    },
    "4": {
      "L": "'But so as not to detain you further, I beg you to hear us briefly, in your clemency.'",
      "M": "'But I do not want to take up too much of your time. I would ask you in your kindness to hear us briefly.'",
      "T": "'I won't take up any more of your valuable time than necessary. I simply ask you to be so gracious as to hear us out briefly.'"
    },
    "5": {
      "L": "'For we have found this man to be a troublemaker and a stirrer up of riots among all the Jews throughout the inhabited world, and a ringleader of the sect of the Nazarenes.'",
      "M": "'We have found this man to be a troublemaker, stirring up riots among Jews all over the world. He is a ringleader of the Nazarene sect.'",
      "T": "'Here is what we have found: this man is a public menace—a troublemaker who has incited unrest among Jews across the entire empire. He is the ringleader of the Nazarene movement.'"
    },
    "6": {
      "L": "'He even attempted to desecrate the temple, and we seized him.'",
      "M": "'He even tried to desecrate the temple, and so we arrested him.'",
      "T": "'He even attempted to defile the temple itself. That is when we arrested him.'"
    },
    "7": {
      "L": "'But Lysias the commander came and with great force took him out of our hands,'",
      "M": "'But the commander Lysias came and forcibly took him from our custody,'",
      "T": "'But the commander Lysias intervened and removed him from our custody by force—'"
    },
    "8": {
      "L": "'by examining him yourself you will be able to learn of all these things of which we accuse him.'",
      "M": "'By examining him yourself you will be able to find out the truth about all these charges we are bringing against him.'",
      "T": "'—and you can determine the truth of all our charges simply by examining him yourself.'"
    },
    "9": {
      "L": "And the Jews also joined in the attack, asserting that these things were so.",
      "M": "The Jews joined in the accusation, asserting that all this was true.",
      "T": "The Jews who had come supported the case, insisting that every word was accurate."
    },
    "10": {
      "L": "And when the governor had nodded to him to speak, Paul answered: 'Knowing that for many years you have been a judge over this nation, I cheerfully make my defence.'",
      "M": "When the governor motioned for him to speak, Paul replied: 'I know that you have been a judge over this nation for a number of years; so I gladly make my defence.'",
      "T": "Felix nodded to Paul to speak, and Paul replied: 'Knowing that you have served as judge over this people for many years, I make my case with confidence.'"
    },
    "11": {
      "L": "'You are able to know that it is not more than twelve days since I went up to Jerusalem to worship.'",
      "M": "'You can easily verify that no more than twelve days ago I went up to Jerusalem to worship.'",
      "T": "'You can check the facts: I arrived in Jerusalem to worship no more than twelve days ago.'"
    },
    "12": {
      "L": "'And neither in the temple did they find me arguing with anyone or stirring up a crowd, nor in the synagogues nor throughout the city.'",
      "M": "'They did not find me arguing with anyone at the temple, or stirring up a crowd in the synagogues or anywhere else in the city.'",
      "T": "'They did not find me arguing with anyone in the temple, or stirring up a crowd in the synagogues, or anywhere else in the city.'"
    },
    "13": {
      "L": "'Neither can they prove to you the things of which they now accuse me.'",
      "M": "'And they cannot prove to you the charges they are now making against me.'",
      "T": "'And they cannot substantiate a single charge they are making.'"
    },
    "14": {
      "L": "'But this I confess to you: according to the Way, which they call a sect, so I serve the God of our fathers, believing everything that is laid down by the Law or written in the Prophets.'",
      "M": "'However, I admit that I worship the God of our ancestors as a follower of the Way, which they call a sect. I believe everything that is in accordance with the Law and that is written in the Prophets.'",
      "T": "'What I will freely admit is this: I worship the God of our ancestors following the Way—what they call a sect. I believe everything the Law teaches and everything the Prophets have written.'"
    },
    "15": {
      "L": "'Having a hope toward God, which these men themselves also accept, that there is going to be a resurrection of both the just and the unjust.'",
      "M": "'I have the same hope in God that these men themselves hold—that there will be a resurrection of both the righteous and the wicked.'",
      "T": "'And I hold the same hope in God that these very accusers claim to share: that both the righteous and the wicked will be raised from the dead.'"
    },
    "16": {
      "L": "'And in this I myself exercise to have always a conscience without offence toward God and men.'",
      "M": "'So I strive always to keep my conscience clear before God and man.'",
      "T": "'This is precisely why I work hard to maintain a clear conscience before God and before everyone around me—always.'"
    },
    "17": {
      "L": "'And after some years I came to bring alms to my nation and offerings.'",
      "M": "'After an absence of several years, I came to Jerusalem to bring my people gifts for the poor and to present offerings.'",
      "T": "'After several years away, I came to bring relief funds to my own people and to present offerings at the temple.'"
    },
    "18": {
      "L": "'In connection with which some Jews from Asia found me purified in the temple, not with a crowd nor with tumult.'",
      "M": "'It was while doing this that some Jews from Asia found me in the temple courts after I had completed the purification rites. There was no crowd around me and no disturbance.'",
      "T": "'That is when some Jews from the province of Asia found me in the temple—I had just completed the purification rites. There was no crowd with me, no disturbance at all.'"
    },
    "19": {
      "L": "'Who ought themselves to be present before you and to make accusation, if they have anything against me.'",
      "M": "'Those are the ones who should be here pressing charges, if they have anything against me—but they are not here.'",
      "T": "'They are the ones who ought to be standing before you with their charges, if they have any grievance against me—but they are absent.'"
    },
    "20": {
      "L": "'Or let these men themselves say what wrongdoing they found when I stood before the council,'",
      "M": "'Or else let these men here state what crime they found in me when I stood before the Sanhedrin—'",
      "T": "'Otherwise, let these men present say what offence they actually found in me when I stood before the Sanhedrin—'"
    },
    "21": {
      "L": "'other than this one statement which I cried out while standing among them: \"It is concerning the resurrection of the dead that I am being judged before you today.\"'",
      "M": "'other than this one statement I shouted as I stood before them: \"It is concerning the resurrection of the dead that I am on trial before you today.\"'",
      "T": "'—unless it is this single declaration I made as I stood there: \"I am on trial today because of the resurrection of the dead.\"'"
    },
    "22": {
      "L": "But Felix, having more exact knowledge of the Way, adjourned them, saying: 'When Lysias the commander comes down, I will decide your case.'",
      "M": "Then Felix, who was well acquainted with the Way, adjourned the proceedings. 'When Lysias the commander comes,' he said, 'I will decide your case.'",
      "T": "Felix, who knew quite a bit about the Way, adjourned the hearing. 'Once the commander Lysias comes down,' he said, 'I will give my ruling.'"
    },
    "23": {
      "L": "And he commanded the centurion that he should be kept in custody, yet have lenient treatment, and that none of his own people should be prevented from serving him.",
      "M": "He ordered the centurion to keep Paul under guard but to give him some freedom and allow his friends to take care of his needs.",
      "T": "He ordered the centurion to keep Paul in custody but to give him considerable latitude—and to let his friends come and go freely to care for him."
    },
    "24": {
      "L": "And after some days Felix came with Drusilla his wife, who was a Jewess, and he sent for Paul and heard him speak concerning the faith in Christ Jesus.",
      "M": "Several days later Felix came with his wife Drusilla, who was Jewish. He sent for Paul and listened to him as he spoke about faith in Christ Jesus.",
      "T": "A few days later Felix arrived with his wife Drusilla—she was Jewish. He sent for Paul and listened to him speak about trusting in Jesus the Messiah."
    },
    "25": {
      "L": "And as he reasoned about righteousness and self-control and the coming judgment, Felix was frightened and answered: 'Go away for the present; when I have an opportunity I will summon you.'",
      "M": "As Paul talked about righteousness, self-control and the judgment to come, Felix was afraid and said, 'That's enough for now! You may leave. When I find it convenient, I will send for you.'",
      "T": "As Paul reasoned through the right way to live, self-mastery, and the coming day when God will judge everyone, Felix grew genuinely alarmed. 'Enough for now,' he said. 'You may go. I will send for you when the moment is right.'"
    },
    "26": {
      "L": "At the same time also he was hoping that money would be given to him by Paul; therefore he also sent for him more frequently and conversed with him.",
      "M": "At the same time he was hoping that Paul would offer him a bribe, so he sent for him frequently and talked with him.",
      "T": "He was also hoping Paul would offer him money. So he kept sending for Paul regularly and having long conversations with him."
    },
    "27": {
      "L": "But when two years had passed, Felix was succeeded by Porcius Festus; and wishing to do the Jews a favour, Felix left Paul bound.",
      "M": "When two years had passed, Felix was succeeded by Porcius Festus. But because Felix wanted to grant a favour to the Jewish leaders, he left Paul in prison.",
      "T": "Two years passed. Then Felix was replaced by Porcius Festus. As a parting gesture to the Jewish leaders, Felix left Paul a prisoner."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'acts')
        merge_tier(existing, ACTS, tier_key)
        save(tier_dir, 'acts', existing)
    print('Acts 22–24 written.')

if __name__ == '__main__':
    main()
