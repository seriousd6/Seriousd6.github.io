"""
MKT Acts chapters 22–28 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-acts-22-28.py

Building on Acts 1–21 key-term decisions:
- G2424 (Ἰησοῦς): "Jesus" throughout
- G5547 (Χριστός): "Christ" (L/M/T)
- G2962 (κύριος): "Lord" throughout
- G4151 ἅγιον: "Holy Spirit" throughout
- G1577 (ἐκκλησία): "church" throughout
- G80 (ἀδελφοί): L: "brothers"; M/T: "brothers and sisters"
- G386 (ἀνάστασις): "resurrection" throughout

New context in Acts 22-28:
- Paul's defense speeches (22-26): formal apologetic rhetoric; key terms from Greek
  legal/philosophical vocabulary
- G1340 (διϊσχυρίζομαι): "insist/maintain"
- G627 (ἀπολογία): "defense" — Paul's formal defense speeches; L/M: "defense";
  T: "defense" or "account of himself"
- G2919 (κρίνω): "judge/judged" throughout
- G1844 (ἐξορκίζω): not used here
- G1849 (ἐξουσία): "authority" throughout
- G5458 (φωστήρ): not here
- The Pharisees and resurrection (23:6-10): Paul's strategic use of the
  Pharisee/Sadducee division; G5330 (Φαρισαῖος): "Pharisee"; G4523 (Σαδδουκαῖος):
  "Sadducee" — proper names, no translation needed
- G1680 (ἐλπίς): "hope" — "hope of the resurrection" is a key phrase in chs 23-26
- G4886 (σύνδεσμος): not here
- G1223+G5124 (διὰ τοῦτο): "for this reason / therefore"
- Festus (G5347 Φῆστος): Roman governor; "Festus" throughout
- Agrippa (G67 Ἀγρίππας): King Agrippa II; "Agrippa" throughout
- Bernice (G959 Βερνίκη): Agrippa's sister; "Bernice" throughout
- G235 (ἀλλά): "but" adversative throughout
- The shipwreck (ch 27): nautical vocabulary — render with appropriate color:
  G5152 (τοπάζιον): not here; G2478 (ἰσχυρός): "strong/severe"
  G4973 (σφραγίς): not here
  G1545 (ἔκβασις): not here
  G2830 (κλύδων): "rough seas"
  G2945 (κύκλῳ): "around"
  Casting lots (27:38): βολίζω (taking soundings); G3731 (ὁρμή): "impulse"
  G29 (ἀγγαρεύω): not here
- G5014 (ταπείνωσις): not here
- Centurion Julius (G2456 Ἰούλιος): "Julius" throughout
- Malta (G3194 Μελίτη): "Malta" (L/M/T) — not "Melita"
- Viper (G2191 ἔχιδνα) in ch 28: "viper" / "snake"
- Publius (G4196 Πόπλιος): "Publius" throughout
- The Roman Jews (ch 28): Paul's final encounter with Jewish leaders in Rome;
  careful to show that Acts ends with the gospel going to the Gentiles
- G1484 (ἔθνη): "Gentiles" in the Isaiah quotation (28:28)
- G4991 (σωτηρία): "salvation" — the last word of Acts thematically
- G3954 (παρρησία): "boldly" (L) / "boldly" (M) / "with complete freedom" (T) —
  the final adverb of Acts 28:31; T tries to capture what ἀκωλύτως (unhindered) adds
- The Isaiah quotation (28:26-27): from Isa 6:9-10 LXX; match the OT translation
  decisions; render "hearing they will not understand" etc. faithfully
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

ACTS_22_28 = {
 "22": {
  "1": {
   "L": "Brothers and fathers, hear my defense which I now make to you.",
   "M": "Brothers and fathers, listen now to my defence.",
   "T": "Brothers and fathers, listen to the defense I want to make before you."
  },
  "2": {
   "L": "And when they heard that he was speaking to them in the Hebrew dialect, they became even more quiet. And he said:",
   "M": "When they heard him speak to them in Aramaic, they became very quiet. Then Paul said:",
   "T": "When they heard him speaking in Aramaic, they became very quiet. Paul continued:"
  },
  "3": {
   "L": "I am a Jew, born in Tarsus of Cilicia, but brought up in this city, educated at the feet of Gamaliel according to the strict manner of the ancestral law, being zealous for God just as all of you are today.",
   "M": "I am a Jew, born in Tarsus of Cilicia, but brought up in this city. I studied under Gamaliel and was thoroughly trained in the law of our ancestors. I was just as zealous for God as any of you are today.",
   "T": "I am a Jew—born in Tarsus of Cilicia, but raised here in Jerusalem. I was educated under Gamaliel in the strictest interpretation of our ancestral law, and I was just as zealous for God as all of you are today."
  },
  "4": {
   "L": "I persecuted this Way to the death, binding and delivering into prisons both men and women,",
   "M": "I persecuted the followers of this Way to their death, arresting both men and women and throwing them into prison,",
   "T": "I hunted down the followers of this Way and had them killed—arresting both men and women and throwing them in prison."
  },
  "5": {
   "L": "as also the high priest and all the council of elders can testify; from whom I also received letters to the brothers and traveled to Damascus to bring those who were there too, bound, to Jerusalem to be punished.",
   "M": "as the high priest and all the Council can themselves testify. I even obtained letters from them to their associates in Damascus, and went there to bring these people as prisoners to Jerusalem to be punished.",
   "T": "The high priest and the whole council of elders can verify this. I even got letters from them authorizing me to travel to Damascus and bring the followers of the Way back to Jerusalem as prisoners."
  },
  "6": {
   "L": "And it came to pass that as I was traveling and drawing near to Damascus, about noon, suddenly a great light from heaven flashed around me.",
   "M": "About noon as I came near Damascus, suddenly a bright light from heaven flashed around me.",
   "T": "Around midday, as I was on the road approaching Damascus, a brilliant light from heaven suddenly blazed around me."
  },
  "7": {
   "L": "And I fell to the ground and heard a voice saying to me: Saul, Saul, why are you persecuting me?",
   "M": "I fell to the ground and heard a voice say to me: Saul! Saul! Why do you persecute me?",
   "T": "I fell to the ground and heard a voice say: Saul! Saul! Why are you persecuting me?"
  },
  "8": {
   "L": "And I answered: Who are you, Lord? And he said to me: I am Jesus the Nazarene, whom you are persecuting.",
   "M": "Who are you, Lord? I asked. I am Jesus of Nazareth, whom you are persecuting, he replied.",
   "T": "I asked: Who are you, Lord? He answered: I am Jesus of Nazareth—the one you are persecuting."
  },
  "9": {
   "L": "And those who were with me saw the light, but they did not hear the voice of the one who was speaking to me.",
   "M": "My companions saw the light, but they did not understand the voice of him who was speaking to me.",
   "T": "My companions saw the light but didn't hear the voice of the one speaking to me."
  },
  "10": {
   "L": "And I said: What shall I do, Lord? And the Lord said to me: Rise and go into Damascus, and there it will be told you all things that are appointed for you to do.",
   "M": "What shall I do, Lord? I asked. Get up, the Lord said, and go into Damascus. There you will be told all that you have been assigned to do.",
   "T": "I asked: What should I do, Lord? He said: Get up and go into Damascus. There you will be told everything you have been assigned to do."
  },
  "11": {
   "L": "And as I could not see because of the brilliance of that light, being led by the hand by those who were with me, I came into Damascus.",
   "M": "My companions led me by the hand into Damascus, because the brilliance of the light had blinded me.",
   "T": "I couldn't see because of the brilliance of that light, so my companions led me by the hand into Damascus."
  },
  "12": {
   "L": "And a certain Ananias, a devout man according to the Law, well spoken of by all the Jews living there,",
   "M": "A man named Ananias came to see me. He was a devout observer of the law and highly respected by all the Jews living there.",
   "T": "A man named Ananias came to me—a devout man who kept the law and was highly regarded by all the Jewish community there."
  },
  "13": {
   "L": "came to me and standing over me said: Brother Saul, receive your sight. And I, in that very hour, received my sight and looked at him.",
   "M": "He stood beside me and said: Brother Saul, receive your sight! And at that very moment I was able to see him.",
   "T": "He stood beside me and said: Brother Saul, receive your sight! And at that very moment I could see again."
  },
  "14": {
   "L": "And he said: The God of our ancestors has appointed you to know his will and to see the Righteous One and to hear a voice from his mouth,",
   "M": "Then he said: The God of our ancestors has chosen you to know his will and to see the Righteous One and to hear words from his mouth.",
   "T": "Then he said: The God of our ancestors has chosen you to know his will, to see the Righteous One, and to hear words from his own mouth."
  },
  "15": {
   "L": "because you will be a witness for him to all men of what you have seen and heard.",
   "M": "You will be his witness to all people of what you have seen and heard.",
   "T": "You will be his witness to all people of everything you have seen and heard."
  },
  "16": {
   "L": "And now why do you delay? Rise and be baptized and wash away your sins, calling on his name.",
   "M": "And now what are you waiting for? Get up, be baptised and wash your sins away, calling on his name.",
   "T": "And now—why are you waiting? Get up, be baptized, and wash your sins away, calling on his name."
  },
  "17": {
   "L": "And it came to pass when I returned to Jerusalem and was praying in the temple, I fell into a trance",
   "M": "When I returned to Jerusalem and was praying at the temple, I fell into a trance",
   "T": "After I returned to Jerusalem and was praying in the temple, I fell into a trance."
  },
  "18": {
   "L": "and saw him saying to me: Hurry and get out of Jerusalem quickly, because they will not accept your testimony about me.",
   "M": "and saw the Lord speaking to me. Quick! he said. Leave Jerusalem immediately, because the people here will not accept your testimony about me.",
   "T": "I saw the Lord speaking to me. He said: Hurry—get out of Jerusalem immediately. The people here won't accept your testimony about me."
  },
  "19": {
   "L": "And I said: Lord, they themselves know that I was imprisoning and beating in every synagogue those who believed in you,",
   "M": "Lord, I replied, these people know that I went from one synagogue to another to imprison and beat those who believe in you.",
   "T": "Lord, I said, they know I went from one synagogue to another, imprisoning and beating those who believed in you."
  },
  "20": {
   "L": "and when the blood of Stephen your witness was shed, I also was standing by and approving, and guarding the cloaks of those who were killing him.",
   "M": "And when the blood of your martyr Stephen was shed, I stood there giving my approval and guarding the clothes of those who were killing him.",
   "T": "And when Stephen—your witness—was being killed, I was standing there, giving my approval and watching over the cloaks of those who were killing him."
  },
  "21": {
   "L": "And he said to me: Go, for I will send you far away to the Gentiles.",
   "M": "Then the Lord said to me: Go; I will send you far away to the Gentiles.",
   "T": "But the Lord said to me: Go—I am sending you far away to the Gentiles."
  },
  "22": {
   "L": "And they were listening to him up to this word, and they lifted up their voice, saying: Rid the earth of such a man; it is not fitting for him to live.",
   "M": "The crowd listened to Paul until he said this. Then they raised their voices and shouted: Rid the earth of him! He's not fit to live!",
   "T": "The crowd listened until he said this. Then they erupted: Rid the earth of this man! He doesn't deserve to live!"
  },
  "23": {
   "L": "And as they were shouting and throwing off their cloaks and flinging dust into the air,",
   "M": "As they were shouting and throwing off their cloaks and flinging dust into the air,",
   "T": "They were shouting, tearing off their cloaks, and throwing dust into the air."
  },
  "24": {
   "L": "the commander ordered him to be brought into the barracks, saying that he should be examined by flogging to find out why they were shouting against him like this.",
   "M": "the commander ordered that Paul be taken into the barracks. He directed that he be flogged and interrogated in order to find out why the people were shouting at him like this.",
   "T": "The commander ordered Paul taken into the barracks and interrogated under flogging—to find out why the crowd was in such an uproar over him."
  },
  "25": {
   "L": "But when they had stretched him out with the thongs, Paul said to the centurion standing by: Is it lawful for you to flog a man who is a Roman and uncondemned?",
   "M": "As they stretched him out to flog him, Paul said to the centurion standing there: Is it legal for you to flog a Roman citizen who hasn't even been found guilty?",
   "T": "But as they tied him up to be flogged, Paul said to the centurion standing there: Is it legal to flog a Roman citizen before he has been tried?"
  },
  "26": {
   "L": "And when the centurion heard this, he went to the commander and reported, saying: What are you about to do? For this man is a Roman.",
   "M": "When the centurion heard this, he went to the commander and reported it. What are you going to do? he said. This man is a Roman citizen.",
   "T": "The centurion heard this and went to the commander. He said: Do you know what you're doing? This man is a Roman citizen!"
  },
  "27": {
   "L": "Then the commander came and said to him: Tell me, are you a Roman? And he said: Yes.",
   "M": "The commander went to Paul and asked: Tell me, are you a Roman citizen? Yes, I am, he answered.",
   "T": "The commander came and asked Paul: Are you really a Roman citizen? I am, Paul said."
  },
  "28": {
   "L": "The commander answered: I acquired this citizenship with a large sum of money. And Paul said: But I was born a citizen.",
   "M": "Then the commander said: I had to pay a lot of money for my citizenship. Paul replied: But I was born a citizen.",
   "T": "The commander replied: I paid a lot of money for my citizenship. Paul said: But I was born a citizen."
  },
  "29": {
   "L": "So those who were about to examine him immediately withdrew from him; and the commander also was afraid when he realized that he was a Roman and that he had bound him.",
   "M": "Those who were about to interrogate him withdrew immediately. The commander himself was alarmed when he realised that he had put Paul, a Roman citizen, in chains.",
   "T": "Those who were about to interrogate him withdrew immediately. The commander was alarmed to realize that he had put a Roman citizen in chains."
  },
  "30": {
   "L": "And the next day, desiring to know the true reason why he was accused by the Jews, he released him and ordered the chief priests and all the council to come together; and bringing Paul down, he set him before them.",
   "M": "The commander wanted to find out exactly why Paul was being accused by the Jews. So the next day he released him and ordered the chief priests and all the members of the Sanhedrin to assemble. Then he brought Paul and had him stand before them.",
   "T": "The next day the commander wanted to know exactly what the Jewish charges against Paul were. So he released him and ordered the chief priests and the whole Sanhedrin to assemble. Then he brought Paul in and had him stand before them."
  }
 },
 "23": {
  "1": {
   "L": "And looking intently at the council, Paul said: Brothers, I have lived my life before God in all good conscience up to this day.",
   "M": "Paul looked straight at the Sanhedrin and said: My brothers, I have fulfilled my duty to God in all good conscience to this day.",
   "T": "Paul looked the Sanhedrin straight in the eye and said: Brothers, I have lived my entire life before God with a completely clear conscience—right up to this day."
  },
  "2": {
   "L": "And the high priest Ananias commanded those standing near him to strike him on the mouth.",
   "M": "At this the high priest Ananias ordered those standing near Paul to strike him on the mouth.",
   "T": "At this, the high priest Ananias ordered those standing near Paul to slap him across the mouth."
  },
  "3": {
   "L": "Then Paul said to him: God is going to strike you, you whitewashed wall! And you are sitting to judge me according to the Law, and command me to be struck in violation of the Law?",
   "M": "Then Paul said to him: God will strike you, you whitewashed wall! You sit there to judge me according to the law, yet you yourself violate the law by commanding that I be struck!",
   "T": "Paul shot back: God will strike you, you whitewashed wall! You sit there judging me according to the law—then break the law yourself by ordering me to be struck!"
  },
  "4": {
   "L": "And those standing nearby said: Do you revile God's high priest?",
   "M": "Those who were standing near Paul said: How dare you insult God's high priest!",
   "T": "Those standing near him said: How dare you insult God's high priest!"
  },
  "5": {
   "L": "And Paul said: I did not know, brothers, that he was the high priest; for it is written: You shall not speak evil of a ruler of your people.",
   "M": "Paul replied: Brothers, I did not realise that he was the high priest; for it is written: Do not speak evil about the ruler of your people.",
   "T": "Paul said: Brothers, I didn't realize he was the high priest. For Scripture says: Do not speak evil about the ruler of your people."
  },
  "6": {
   "L": "But Paul, knowing that one part of them were Sadducees and the other Pharisees, called out in the council: Brothers, I am a Pharisee, a son of Pharisees; it is regarding the hope of the resurrection of the dead that I am on trial.",
   "M": "Then Paul, knowing that some of them were Sadducees and the others Pharisees, called out in the Sanhedrin: My brothers, I am a Pharisee, descended from Pharisees. I stand on trial because of the hope of the resurrection of the dead.",
   "T": "Then Paul, realizing that some members were Sadducees and others Pharisees, called out to the council: Brothers, I am a Pharisee—the son of a Pharisee! I am on trial because of my hope in the resurrection of the dead!"
  },
  "7": {
   "L": "When he said this, a dispute broke out between the Pharisees and Sadducees; and the assembly was divided.",
   "M": "When he said this, a dispute broke out between the Pharisees and the Sadducees, and the assembly was divided.",
   "T": "When he said this, a fierce argument broke out between the Pharisees and the Sadducees—the assembly was split."
  },
  "8": {
   "L": "For the Sadducees say there is no resurrection, nor angel, nor spirit; but the Pharisees acknowledge them all.",
   "M": "The Sadducees say that there is no resurrection, and that there are neither angels nor spirits, but the Pharisees acknowledge them all.",
   "T": "The Sadducees deny the resurrection, angels, and any kind of spirit; but the Pharisees believe in all three."
  },
  "9": {
   "L": "And there was a great uproar; and some of the scribes of the Pharisee party stood up and contended fiercely: We find nothing wrong with this man. But what if a spirit or an angel spoke to him?",
   "M": "There was a great uproar, and some of the teachers of the law who were Pharisees stood up and argued vigorously: We find nothing wrong with this man. What if a spirit or an angel has spoken to him?",
   "T": "A great shouting match erupted. Some of the Pharisee teachers stood up and argued strongly: We find nothing wrong with this man! What if a spirit or an angel really did speak to him?"
  },
  "10": {
   "L": "And when the dispute became very violent, the commander, afraid that Paul would be torn to pieces by them, ordered the troops to go down and take him away from among them by force, and to bring him into the barracks.",
   "M": "The dispute became so violent that the commander was afraid Paul would be torn to pieces by them. He ordered the troops to go down and take him away from them by force and bring him into the barracks.",
   "T": "The argument became so violent that the commander feared Paul would be torn apart. He ordered the troops to go down and take Paul away by force and bring him back to the barracks."
  },
  "11": {
   "L": "And the following night the Lord stood beside him and said: Take courage, for as you have testified to the things about me in Jerusalem, so you must also testify in Rome.",
   "M": "The following night the Lord stood near Paul and said: Take courage! As you have testified about me in Jerusalem, so you must also testify in Rome.",
   "T": "That night the Lord stood near Paul and said: Take courage! Just as you have testified about me here in Jerusalem, so you must also testify in Rome."
  },
  "12": {
   "L": "And when day came, the Jews formed a conspiracy and bound themselves by an oath, saying that they would neither eat nor drink until they had killed Paul.",
   "M": "The next morning some Jews formed a conspiracy and bound themselves with an oath not to eat or drink until they had killed Paul.",
   "T": "The next morning some Jewish men formed a conspiracy and bound themselves by an oath not to eat or drink until they had killed Paul."
  },
  "13": {
   "L": "There were more than forty who formed this conspiracy.",
   "M": "More than forty men were involved in this plot.",
   "T": "More than forty men joined this conspiracy."
  },
  "14": {
   "L": "They went to the chief priests and elders and said: We have bound ourselves by an oath to taste nothing until we have killed Paul.",
   "M": "They went to the chief priests and elders and said: We have taken a solemn oath not to eat anything until we have killed Paul.",
   "T": "They went to the chief priests and elders and said: We have sworn an oath not to eat anything until we have killed Paul."
  },
  "15": {
   "L": "Now therefore you with the council notify the commander to bring him down to you, as if you were going to investigate his case more thoroughly; and we, before he comes near, are ready to kill him.",
   "M": "Now then, you and the Sanhedrin petition the commander to bring him before you on the pretext of wanting more accurate information about his case. We are ready to kill him before he gets here.",
   "T": "So here's the plan: you and the Sanhedrin ask the commander to bring Paul before you on the pretense of investigating his case more carefully. We'll be ready to kill him before he arrives."
  },
  "16": {
   "L": "But the son of Paul's sister heard about the ambush, and going in he entered the barracks and told Paul.",
   "M": "But when the son of Paul's sister heard of this plot, he went into the barracks and told Paul.",
   "T": "But Paul's nephew heard about the ambush. He went to the barracks and told Paul."
  },
  "17": {
   "L": "And Paul called one of the centurions and said: Take this young man to the commander, for he has something to tell him.",
   "M": "Then Paul called one of the centurions and said: Take this young man to the commander; he has something to tell him.",
   "T": "Paul called one of the centurions and said: Take this young man to the commander—he has something important to tell him."
  },
  "18": {
   "L": "So he took him and brought him to the commander and said: Paul the prisoner called me and asked me to bring this young man to you, as he has something to say to you.",
   "M": "So the centurion took him to the commander and said: Paul, the prisoner, sent for me and asked me to bring this young man to you because he has something to tell you.",
   "T": "The centurion took him to the commander and said: Paul the prisoner sent for me and asked me to bring this young man to you. He has something to tell you."
  },
  "19": {
   "L": "The commander took him by the hand and drawing him aside privately asked: What is it that you have to report to me?",
   "M": "The commander took the young man by the hand, drew him aside and asked: What is it you want to tell me?",
   "T": "The commander took the young man aside privately and asked: What is it you want to tell me?"
  },
  "20": {
   "L": "And he said: The Jews have agreed to ask you to bring Paul down to the council tomorrow, as if they were going to inquire more carefully about him.",
   "M": "He said: The Jews have agreed to ask you to bring Paul before the Sanhedrin tomorrow on the pretext of wanting more accurate information about him.",
   "T": "He said: The Jewish leaders have agreed to ask you to bring Paul to the Sanhedrin tomorrow, under the pretense of getting more information about him."
  },
  "21": {
   "L": "So do not be persuaded by them, for more than forty of their men are lying in wait for him, who have bound themselves by an oath neither to eat nor to drink until they have killed him; and now they are ready, waiting for the promise from you.",
   "M": "Don't give in to them, because more than forty of them are waiting in ambush for him. They have taken an oath not to eat or drink until they have killed him. They are ready now, waiting for your consent.",
   "T": "Don't let them talk you into it. More than forty men are waiting in ambush—they have sworn not to eat or drink until they have killed him. They're ready right now, waiting for your word."
  },
  "22": {
   "L": "So the commander dismissed the young man, instructing him: Tell no one that you have revealed this to me.",
   "M": "The commander dismissed the young man with this warning: Don't tell anyone that you have reported this to me.",
   "T": "The commander dismissed the young man with a warning: Don't tell anyone you reported this to me."
  },
  "23": {
   "L": "And summoning two of the centurions, he said: Get ready two hundred soldiers, seventy horsemen, and two hundred spearmen to go to Caesarea at the third hour of the night.",
   "M": "Then he called two of his centurions and ordered them: Get ready a detachment of two hundred soldiers, seventy horsemen and two hundred spearmen to go to Caesarea at nine tonight.",
   "T": "He called two of his centurions and ordered: Prepare two hundred soldiers, seventy cavalry, and two hundred spearmen to march to Caesarea tonight at nine."
  },
  "24": {
   "L": "And provide mounts for Paul to ride, so that he may be brought safely to Felix the governor.",
   "M": "Provide horses for Paul so that he may be taken safely to Governor Felix.",
   "T": "Provide horses for Paul to ride, and get him safely to Governor Felix."
  },
  "25": {
   "L": "And he wrote a letter having this form:",
   "M": "He wrote a letter as follows:",
   "T": "He also wrote a letter that went like this:"
  },
  "26": {
   "L": "Claudius Lysias to the most excellent Governor Felix, greetings.",
   "M": "Claudius Lysias, To His Excellency, Governor Felix: Greetings.",
   "T": "Claudius Lysias, to the Most Excellent Governor Felix. Greetings."
  },
  "27": {
   "L": "This man was seized by the Jews and was about to be killed by them when I came upon them with the soldiers and rescued him, having learned that he was a Roman citizen.",
   "M": "This man was seized by the Jews and they were about to kill him, but I came with my troops and rescued him, for I had learned that he is a Roman citizen.",
   "T": "This man was seized by the Jewish people and they were about to kill him. I arrived with my troops and rescued him—I had found out he was a Roman citizen."
  },
  "28": {
   "L": "And wanting to know the charge for which they were accusing him, I brought him down to their council.",
   "M": "I wanted to know why they were accusing him, so I brought him to their Sanhedrin.",
   "T": "I wanted to know what charge they were bringing against him, so I brought him before their Sanhedrin."
  },
  "29": {
   "L": "I found that he was accused in connection with disputes about their law, but that there was no accusation worthy of death or imprisonment.",
   "M": "I found that the accusation had to do with questions about their law, but there was no charge against him that deserved death or imprisonment.",
   "T": "I found that the charge had to do with disputes about their religious law—nothing that deserved death or imprisonment."
  },
  "30": {
   "L": "And when it was reported to me that there would be a plot against the man, I immediately sent him to you, charging his accusers also to state before you what they have against him.",
   "M": "When I was informed of a plot to be carried out against the man, I sent him to you at once. I also ordered his accusers to present to you their case against him.",
   "T": "When I was told about a plot against him, I sent him to you immediately. I also instructed his accusers to present their charges against him before you."
  },
  "31": {
   "L": "So the soldiers, carrying out their orders, took Paul and brought him by night to Antipatris.",
   "M": "So the soldiers, carrying out their orders, took Paul with them during the night and brought him as far as Antipatris.",
   "T": "The soldiers followed their orders and took Paul during the night, bringing him as far as Antipatris."
  },
  "32": {
   "L": "And the next day, leaving the cavalry to go on with him, they returned to the barracks.",
   "M": "The next day they let the cavalry go on with him, while they returned to the barracks.",
   "T": "The next day they let the cavalry escort continue with Paul while they returned to the barracks."
  },
  "33": {
   "L": "When they came to Caesarea and delivered the letter to the governor, they also presented Paul to him.",
   "M": "When the cavalry arrived in Caesarea, they delivered the letter to the governor and handed Paul over to him.",
   "T": "When they arrived in Caesarea, they delivered the letter to the governor and turned Paul over to him."
  },
  "34": {
   "L": "And having read the letter and asked what province he was from, and learning that he was from Cilicia,",
   "M": "The governor read the letter and asked what province he was from. Learning that he was from Cilicia,",
   "T": "The governor read the letter and asked what province Paul was from. When he learned he was from Cilicia,"
  },
  "35": {
   "L": "he said: I will hear your case when your accusers arrive also. And he ordered him to be kept under guard in Herod's palace.",
   "M": "he said, I will hear your case when your accusers get here too. Then he ordered that Paul be kept under guard in Herod's palace.",
   "T": "he said: I will hear your case when your accusers arrive. He then ordered Paul to be kept under guard in Herod's palace."
  }
 },
 "24": {
  "1": {
   "L": "And after five days the high priest Ananias came down with some elders and a certain orator named Tertullus, and they brought their charges against Paul before the governor.",
   "M": "Five days later the high priest Ananias went down to Caesarea with some of the elders and a lawyer named Tertullus, and they brought their charges against Paul before the governor.",
   "T": "Five days later the high priest Ananias came down to Caesarea with some elders and a lawyer named Tertullus. They presented their case against Paul to the governor."
  },
  "2": {
   "L": "When Paul had been summoned, Tertullus began to accuse him, saying: Since we have achieved much peace through you, and since by your foresight reforms are being made for this nation,",
   "M": "When Paul was called in, Tertullus presented his case before Felix: We have enjoyed a long period of peace under you, and your foresight has brought about reforms in this nation.",
   "T": "When Paul was brought in, Tertullus stated the case: We have enjoyed long peace under your leadership, and your foresight has brought many reforms to our nation."
  },
  "3": {
   "L": "we acknowledge this in every way and everywhere, most excellent Felix, with all gratitude.",
   "M": "Everywhere and in every way, most excellent Felix, we acknowledge this with profound gratitude.",
   "T": "Everywhere and in every way, Most Excellent Felix, we are deeply grateful."
  },
  "4": {
   "L": "But not to delay you further, I beg you to hear us briefly in your kindness.",
   "M": "But in order not to weary you further, I would request that you be kind enough to hear us briefly.",
   "T": "But so as not to take up too much of your time, I ask that you hear us briefly with your usual courtesy."
  },
  "5": {
   "L": "For we have found this man to be a plague and one who stirs up riots among all the Jews throughout the world, and a ringleader of the sect of the Nazarenes.",
   "M": "We have found this man to be a troublemaker, stirring up riots among the Jews all over the world. He is a ringleader of the Nazarene sect",
   "T": "We have found this man to be a troublemaker who stirs up riots among Jews throughout the world. He is a ringleader of the Nazarene sect."
  },
  "6": {
   "L": "He even tried to desecrate the temple, and we arrested him.",
   "M": "and even tried to desecrate the temple; so we seized him.",
   "T": "He even tried to desecrate the temple—so we arrested him."
  },
  "8": {
   "L": "By examining him yourself you will be able to learn from him about all these things of which we accuse him.",
   "M": "By examining him yourself you will be able to learn the truth about all these charges we are bringing against him.",
   "T": "If you examine him yourself, you will be able to find out all these things for which we accuse him."
  },
  "9": {
   "L": "And the Jews also joined in the charge, asserting that all these things were so.",
   "M": "The other Jews joined in the accusation, asserting that these things were true.",
   "T": "The other Jewish leaders joined in the accusation, insisting these things were all true."
  },
  "10": {
   "L": "And when the governor had motioned to him to speak, Paul answered: Knowing that you have been a judge over this nation for many years, I cheerfully make my defense.",
   "M": "When the governor motioned for him to speak, Paul replied: I know that for a number of years you have been a judge over this nation; so I gladly make my defence.",
   "T": "When the governor nodded for Paul to speak, Paul replied: I know you have been a judge over this nation for many years, so I gladly make my defense."
  },
  "11": {
   "L": "As you can verify, it is not more than twelve days since I went up to Jerusalem to worship.",
   "M": "You can easily verify that no more than twelve days ago I went up to Jerusalem to worship.",
   "T": "You can easily verify that it was no more than twelve days ago that I went up to Jerusalem to worship."
  },
  "12": {
   "L": "And they did not find me disputing with anyone or stirring up a crowd in the temple or in the synagogues or throughout the city.",
   "M": "My accusers did not find me arguing with anyone at the temple, or stirring up a crowd in the synagogues or anywhere else in the city.",
   "T": "My accusers did not find me arguing with anyone or stirring up any crowd—not in the temple, the synagogues, or anywhere in the city."
  },
  "13": {
   "L": "Neither can they prove to you the things of which they now accuse me.",
   "M": "And they cannot prove to you the charges they are now making against me.",
   "T": "They cannot prove to you a single one of the charges they are bringing against me."
  },
  "14": {
   "L": "But I admit this to you, that according to the Way which they call a sect, so I worship the God of our fathers, believing all things that are according to the Law and written in the Prophets,",
   "M": "However, I admit that I worship the God of our ancestors as a follower of the Way, which they call a sect. I believe everything that is in accordance with the Law and that is written in the Prophets,",
   "T": "I will admit this: I worship the God of our ancestors according to the Way—which they call a sect. I believe everything the Law teaches and everything written in the Prophets."
  },
  "15": {
   "L": "having a hope in God, which these men themselves also accept, that there will be a resurrection of both the righteous and the unrighteous.",
   "M": "and I have the same hope in God as these men themselves have, that there will be a resurrection of both the righteous and the wicked.",
   "T": "I share the same hope in God as these men themselves have—that there will be a resurrection of both the righteous and the unrighteous."
  },
  "16": {
   "L": "In this I also exercise myself to always have a clear conscience toward God and toward men.",
   "M": "So I strive always to keep my conscience clear before God and man.",
   "T": "So I make it my constant goal to maintain a clear conscience before God and everyone."
  },
  "17": {
   "L": "And after several years I came to bring alms to my nation and to present offerings,",
   "M": "After an absence of several years, I came to Jerusalem to bring my people gifts for the poor and to present offerings.",
   "T": "After being away for several years, I came to Jerusalem to bring contributions for the poor of my people and to present offerings."
  },
  "18": {
   "L": "in connection with which they found me purified in the temple, without any crowd or uproar—but some Jews from Asia—",
   "M": "I was ceremonially clean when they found me in the temple courts doing this. There was no crowd with me, nor was I involved in any disturbance.",
   "T": "It was while I was doing this that they found me ceremonially clean in the temple—no crowd, no disturbance."
  },
  "19": {
   "L": "who ought to be present before you and to make accusation, if they have anything against me.",
   "M": "But there are some Jews from the province of Asia, who ought to be here before you and bring charges if they have anything against me.",
   "T": "But there were some Jews from the province of Asia who should be here before you to bring their charges—if they have any case against me."
  },
  "20": {
   "L": "Or else let these men themselves say what wrongdoing they found when I stood before the council,",
   "M": "Or these who are here should state what crime they found in me when I stood before the Sanhedrin—",
   "T": "Otherwise, let these men who are here say what crime they found when I stood before the Sanhedrin—"
  },
  "21": {
   "L": "unless it is this one thing that I called out as I stood among them: It is about the resurrection of the dead that I am on trial before you today.",
   "M": "unless it was this one thing I shouted as I stood before them: It is concerning the resurrection of the dead that I am on trial before you today.",
   "T": "unless it is this one statement I shouted out as I stood among them: It is about the resurrection of the dead that I am on trial before you today!"
  },
  "22": {
   "L": "But Felix, having a rather accurate knowledge of the Way, adjourned the hearing, saying: When Lysias the commander comes down, I will decide your case.",
   "M": "Then Felix, who was well acquainted with the Way, adjourned the proceedings. When Lysias the commander comes, he said, I will decide your case.",
   "T": "Then Felix, who had a fairly accurate understanding of the Way, adjourned the proceedings. He said: When Commander Lysias comes, I will decide your case."
  },
  "23": {
   "L": "And he ordered the centurion to keep him in custody and to give him some liberty, and not to prevent his own people from ministering to his needs.",
   "M": "He ordered the centurion to keep Paul under guard but to give him some freedom and permit his friends to take care of his needs.",
   "T": "He ordered the centurion to keep Paul in custody but give him some freedom and allow his friends to take care of his needs."
  },
  "24": {
   "L": "And after some days, Felix arrived with his wife Drusilla, who was Jewish, and he sent for Paul and heard him speak about faith in Christ Jesus.",
   "M": "Several days later Felix came with his wife Drusilla, who was Jewish. He sent for Paul and listened to him as he spoke about faith in Christ Jesus.",
   "T": "Some days later Felix arrived with his wife Drusilla, who was Jewish. He sent for Paul and listened to him speak about faith in Christ Jesus."
  },
  "25": {
   "L": "And as he was reasoning about righteousness and self-control and the coming judgment, Felix became frightened and said: Go away for now, and when I have an opportunity I will summon you.",
   "M": "As Paul talked about righteousness, self-control and the judgment to come, Felix was afraid and said: That's enough for now! You may leave. When I find it convenient, I will send for you.",
   "T": "But when Paul began discussing righteousness, self-control, and the coming judgment, Felix became frightened and said: That's enough for now! You can go. When the time is right, I'll send for you again."
  },
  "26": {
   "L": "At the same time he was hoping that money would be given to him by Paul; therefore he also sent for him more often and conversed with him.",
   "M": "At the same time he was hoping that Paul would offer him a bribe, so he sent for him frequently and talked with him.",
   "T": "At the same time Felix was hoping Paul would offer him a bribe. So he kept sending for him and talking with him."
  },
  "27": {
   "L": "But after two years, Porcius Festus succeeded Felix; and wanting to do the Jews a favor, Felix left Paul bound.",
   "M": "When two years had passed, Felix was succeeded by Porcius Festus, but because Felix wanted to grant a favour to the Jews, he left Paul in prison.",
   "T": "After two years, Porcius Festus succeeded Felix. Wanting to leave the Jewish leaders satisfied, Felix left Paul in prison."
  }
 },
 "25": {
  "1": {
   "L": "Therefore Festus, having come into the province, after three days went up to Jerusalem from Caesarea.",
   "M": "Three days after arriving in the province, Festus went up from Caesarea to Jerusalem,",
   "T": "Three days after arriving in the province, Festus went up from Caesarea to Jerusalem."
  },
  "2": {
   "L": "And the chief priests and the leading men of the Jews brought charges against Paul to him, and they were urging him,",
   "M": "where the chief priests and the Jewish leaders appeared before him and presented the charges against Paul.",
   "T": "There the chief priests and the Jewish leaders brought their charges against Paul before him."
  },
  "3": {
   "L": "requesting a favor against Paul, that he summon him to Jerusalem—while planning an ambush to kill him along the way.",
   "M": "They requested Festus, as a favour to them, to have Paul transferred to Jerusalem, for they were preparing an ambush to kill him along the way.",
   "T": "They asked Festus to do them a favor—transfer Paul to Jerusalem. They were planning an ambush to kill him along the way."
  },
  "4": {
   "L": "Festus answered that Paul was being kept in Caesarea and that he himself was about to depart there shortly.",
   "M": "Festus answered: Paul is being held at Caesarea, and I myself am going there soon.",
   "T": "Festus answered: Paul is being kept in Caesarea, and I myself am going there shortly."
  },
  "5": {
   "L": "Therefore, he said, let those among you who have authority go down with me, and if there is something wrong with this man, let them accuse him.",
   "M": "Let some of your leaders come with me, and if the man has done anything wrong, they can press charges against him there.",
   "T": "So let your capable leaders come down with me, and if this man has done anything wrong, they can press charges there."
  },
  "6": {
   "L": "And having stayed among them no more than eight or ten days, he went down to Caesarea; and the next day he sat on the tribunal and ordered Paul to be brought.",
   "M": "After spending eight or ten days with them, Festus went down to Caesarea. The next day he convened the court and ordered that Paul be brought before him.",
   "T": "After spending eight or ten days with them, Festus went down to Caesarea. The next day he convened court and ordered Paul brought in."
  },
  "7": {
   "L": "And when he appeared, the Jews who had come down from Jerusalem stood around him, bringing many and serious charges against him, which they could not prove.",
   "M": "When Paul came in, the Jews who had come down from Jerusalem stood round him. They brought many serious charges against him, but they could not prove them.",
   "T": "When Paul appeared, the Jews who had come down from Jerusalem surrounded him, bringing many serious charges—none of which they could prove."
  },
  "8": {
   "L": "Paul argued in his own defense: I have not sinned against the law of the Jews, or against the temple, or against Caesar.",
   "M": "Then Paul made his defence: I have done nothing wrong against the Jewish law or against the temple or against Caesar.",
   "T": "Paul made his defense: I have done nothing wrong against the Jewish law, the temple, or Caesar."
  },
  "9": {
   "L": "But Festus, wishing to do the Jews a favor, answered Paul and said: Are you willing to go up to Jerusalem, and there to be judged before me on these charges?",
   "M": "Festus, wishing to do the Jews a favour, said to Paul: Are you willing to go up to Jerusalem and stand trial before me there on these charges?",
   "T": "Festus, wanting to curry favor with the Jews, said to Paul: Are you willing to go up to Jerusalem and stand trial before me there on these charges?"
  },
  "10": {
   "L": "But Paul said: I am standing before Caesar's tribunal, where I ought to be tried. I have done no wrong to the Jews, as you yourself know very well.",
   "M": "Paul answered: I am now standing before Caesar's court, where I ought to be tried. I have not done any wrong to the Jews, as you yourself know very well.",
   "T": "Paul answered: I am standing right now before Caesar's court—this is where I should be tried. I have done no wrong to the Jews, as you yourself know very well."
  },
  "11": {
   "L": "If then I am in the wrong and have committed anything worthy of death, I am not trying to escape death; but if there is nothing to the things of which they accuse me, no one can hand me over to them. I appeal to Caesar.",
   "M": "If, however, I am guilty of doing anything deserving death, I do not refuse to die. But if the charges brought against me by these Jews are not true, no one has the right to hand me over to them. I appeal to Caesar!",
   "T": "If I am guilty of something that deserves death, I am not trying to escape death. But if there is no truth in what these people are accusing me of, no one has the right to hand me over to them. I appeal to Caesar!"
  },
  "12": {
   "L": "Then Festus, having conferred with the council, replied: You have appealed to Caesar; to Caesar you shall go.",
   "M": "After Festus had conferred with his council, he declared: You have appealed to Caesar. To Caesar you will go!",
   "T": "After consulting with his advisers, Festus declared: You have appealed to Caesar—to Caesar you will go!"
  },
  "13": {
   "L": "Now when some days had passed, King Agrippa and Bernice arrived in Caesarea and paid their respects to Festus.",
   "M": "A few days later King Agrippa and Bernice arrived at Caesarea to pay their respects to Festus.",
   "T": "A few days later King Agrippa and Bernice arrived in Caesarea to greet Festus."
  },
  "14": {
   "L": "And as they were spending many days there, Festus laid Paul's case before the king, saying: There is a certain man left as a prisoner by Felix,",
   "M": "Since they were spending several days there, Festus discussed Paul's case with the king. He said: There is a man here whom Felix left as a prisoner.",
   "T": "Since they were staying there several days, Festus brought up Paul's case with the king. He said: There is a man here that Felix left as a prisoner."
  },
  "15": {
   "L": "about whom, when I was in Jerusalem, the chief priests and elders of the Jews brought charges and asked for a verdict against him.",
   "M": "When I went to Jerusalem, the chief priests and the elders of the Jews brought charges against him and asked that he be condemned.",
   "T": "When I was in Jerusalem, the chief priests and Jewish elders brought charges against him and asked that he be condemned."
  },
  "16": {
   "L": "I replied to them that it is not the Roman custom to hand over any man before the accused has met his accusers face to face and has had the opportunity to defend himself against the charge.",
   "M": "I told them that it is not the Roman custom to hand over anyone before they have faced their accusers and have had an opportunity to defend themselves against the charges.",
   "T": "I told them that it is not the Roman custom to hand over someone before the accused has faced the accusers and had the opportunity to defend himself against the charges."
  },
  "17": {
   "L": "When they came here, therefore, I made no delay, but the next day sat on the tribunal and ordered the man to be brought in.",
   "M": "When they came here, I did not delay the case, but convened the court the next day and ordered the man to be brought in.",
   "T": "When they came here, I didn't delay—the very next day I convened the court and ordered the man brought in."
  },
  "18": {
   "L": "When the accusers stood up, they did not charge him with any of the crimes I was expecting,",
   "M": "When his accusers got up to speak, they did not charge him with any of the crimes I had expected.",
   "T": "When his accusers stood up, the charges they brought were not at all what I had expected."
  },
  "19": {
   "L": "but they had certain disputes against him about their own religion and about a certain dead man named Jesus, whom Paul asserted was alive.",
   "M": "Instead, they had some points of dispute with him about their own religion and about a dead man named Jesus who Paul claimed was alive.",
   "T": "Instead, they had some disagreement with him about their own religion—and about a man named Jesus, who had died, but whom Paul insisted was still alive."
  },
  "20": {
   "L": "And being uncertain how to investigate such matters, I asked him whether he wished to go to Jerusalem and be tried there on these charges.",
   "M": "I was at a loss how to investigate such matters; so I asked if he would be willing to go to Jerusalem and stand trial there on these charges.",
   "T": "I had no idea how to investigate such matters, so I asked if he was willing to go to Jerusalem and stand trial there."
  },
  "21": {
   "L": "But when Paul had appealed to be kept under guard for the decision of his Imperial Majesty, I ordered him to be kept under guard until I send him up to Caesar.",
   "M": "But when Paul made his appeal to be held over for the Emperor's decision, I ordered him held until I could send him to Caesar.",
   "T": "But Paul appealed to have his case kept for the Emperor's decision, so I ordered him held until I could send him to Caesar."
  },
  "22": {
   "L": "And Agrippa said to Festus: I myself would like to hear the man. Tomorrow, he said, you shall hear him.",
   "M": "Then Agrippa said to Festus: I would like to hear this man myself. He replied: Tomorrow you will hear him.",
   "T": "Agrippa said to Festus: I'd like to hear this man myself. Tomorrow, Festus replied, you will hear him."
  },
  "23": {
   "L": "And the next day, when Agrippa and Bernice came with great pomp, and entered the audience hall with the commanders and the prominent men of the city, and Paul was brought in at the command of Festus,",
   "M": "The next day Agrippa and Bernice came with great pomp and entered the audience room with the high-ranking military officers and the prominent men of the city. At the command of Festus, Paul was brought in.",
   "T": "The next day Agrippa and Bernice arrived in great ceremony and entered the audience hall with the senior military officers and prominent citizens. At Festus's command, Paul was brought in."
  },
  "24": {
   "L": "Festus said: King Agrippa, and all men who are present with us, you see this man about whom all the multitude of the Jews petitioned me, both in Jerusalem and here, shouting that he ought not to live any longer.",
   "M": "Festus said: King Agrippa, and all who are present with us, you see this man! The whole Jewish community has petitioned me about him in Jerusalem and here in Caesarea, shouting that he ought not to live any longer.",
   "T": "Festus said: King Agrippa, and everyone present with us—you see this man. The entire Jewish community has petitioned me about him, both in Jerusalem and here, crying out that he should no longer be alive."
  },
  "25": {
   "L": "But I found that he had done nothing deserving death. And as he himself has appealed to the Emperor, I decided to send him.",
   "M": "I found he had done nothing deserving of death, but because he made his appeal to the Emperor I decided to send him to Rome.",
   "T": "I found that he has done nothing deserving death. But since he appealed to the Emperor, I decided to send him."
  },
  "26": {
   "L": "Yet I have no definite charge to write to my lord about him. Therefore I have brought him before all of you, and especially before you, King Agrippa, so that after this examination I may have something to write.",
   "M": "But I have nothing definite to write to His Majesty about him. Therefore I have brought him before all of you, and especially before you, King Agrippa, so that as a result of this investigation I may have something to write.",
   "T": "But I have nothing definite to write to His Majesty about him. So I have brought him before all of you—especially you, King Agrippa—so that after this hearing I will have something concrete to write."
  },
  "27": {
   "L": "For it seems unreasonable to me to send a prisoner and not indicate the charges against him.",
   "M": "For I think it is unreasonable to send a prisoner without specifying the charges against him.",
   "T": "For it seems absurd to send a prisoner without stating the charges against him."
  }
 },
 "26": {
  "1": {
   "L": "And Agrippa said to Paul: You are permitted to speak for yourself. Then Paul stretched out his hand and made his defense:",
   "M": "Then Agrippa said to Paul: You have permission to speak for yourself. So Paul motioned with his hand and began his defence:",
   "T": "Agrippa said to Paul: You have permission to speak for yourself. Paul motioned with his hand and began his defense:"
  },
  "2": {
   "L": "I consider myself fortunate that it is before you, King Agrippa, that I am to make my defense today against all the accusations brought against me by the Jews,",
   "M": "King Agrippa, I consider myself fortunate to stand before you today as I make my defence against all the accusations of the Jews,",
   "T": "King Agrippa, I count myself fortunate to stand before you today and make my defense against all the accusations the Jewish leaders bring against me."
  },
  "3": {
   "L": "especially because you are an expert in all the customs and controversies of the Jews. Therefore I beg you to listen to me patiently.",
   "M": "and especially so because you are well acquainted with all the Jewish customs and controversies. Therefore, I beg you to listen to me patiently.",
   "T": "Especially because you are well acquainted with all the Jewish customs and controversies. I ask you to listen to me patiently."
  },
  "4": {
   "L": "My manner of life from youth, from the beginning, spent among my own people and in Jerusalem, is known to all the Jews.",
   "M": "The Jewish people all know the way I have lived ever since I was a child, from the beginning of my life in my own country, and also in Jerusalem.",
   "T": "All the Jewish people know how I have lived from my earliest youth—how I lived among my own people and in Jerusalem."
  },
  "5": {
   "L": "They have known about me for a long time, if they are willing to testify, that according to the strictest party of our religion I have lived as a Pharisee.",
   "M": "They have known me for a long time and can testify, if they are willing, that I conformed to the strictest sect of our religion, living as a Pharisee.",
   "T": "They have known me for a long time and could testify—if they chose to—that I lived as a Pharisee, the strictest movement in our religion."
  },
  "6": {
   "L": "And now I am standing on trial because of the hope of the promise made by God to our fathers,",
   "M": "And now it is because of my hope in what God has promised our ancestors that I am on trial today.",
   "T": "And now I stand on trial because of my hope in the promise God made to our ancestors."
  },
  "7": {
   "L": "to which our twelve tribes hope to attain, as they earnestly worship night and day. It is concerning this hope, O King, that I am accused by the Jews.",
   "M": "This is the promise our twelve tribes are hoping to see fulfilled as they earnestly serve God day and night. King Agrippa, it is because of this hope that these Jews are accusing me.",
   "T": "This is the promise our twelve tribes are hoping to see fulfilled as they earnestly serve God night and day. King Agrippa, it is precisely because of this hope that the Jewish leaders are accusing me."
  },
  "8": {
   "L": "Why is it judged incredible among you that God raises the dead?",
   "M": "Why should any of you consider it incredible that God raises the dead?",
   "T": "Why does any of you find it incredible that God raises the dead?"
  },
  "9": {
   "L": "I myself was convinced that I ought to do many things against the name of Jesus the Nazarene.",
   "M": "I too was convinced that I ought to do all that was possible to oppose the name of Jesus of Nazareth.",
   "T": "I myself once believed it was my duty to do everything possible to oppose the name of Jesus of Nazareth."
  },
  "10": {
   "L": "And I did so in Jerusalem. I not only locked up many of the saints in prison with the authority I received from the chief priests, but when they were put to death I cast my vote against them.",
   "M": "And that is just what I did in Jerusalem. On the authority of the chief priests I put many of the Lord's people in prison, and when they were put to death, I cast my vote against them.",
   "T": "And that is what I did in Jerusalem. With the authority from the chief priests, I locked up many of God's people in prison. When they were put to death, I voted for it."
  },
  "11": {
   "L": "And punishing them often in all the synagogues, I was trying to force them to blaspheme; and being furiously enraged at them, I was persecuting them even to foreign cities.",
   "M": "Many a time I went from one synagogue to another to have them punished, and I tried to force them to blaspheme. I was so obsessed with persecuting them that I even hunted them down in foreign cities.",
   "T": "I had them punished again and again in every synagogue, trying to force them to blaspheme. I was so consumed with rage against them that I hunted them down even in cities outside Judea."
  },
  "12": {
   "L": "In connection with this, while traveling to Damascus with the authority and commission of the chief priests,",
   "M": "On one of these journeys I was going to Damascus with the authority and commission of the chief priests.",
   "T": "On one of these journeys I was traveling to Damascus with the authority and commission of the chief priests."
  },
  "13": {
   "L": "at midday, O King, I saw on the road a light from heaven, brighter than the sun, shining around me and those who were traveling with me.",
   "M": "About noon, King Agrippa, as I was on the road, I saw a light from heaven, brighter than the sun, blazing around me and my companions.",
   "T": "Around midday, King Agrippa, I saw a light from heaven, brighter than the sun—blazing around me and my companions on the road."
  },
  "14": {
   "L": "And when we had all fallen to the ground, I heard a voice saying to me in the Hebrew dialect: Saul, Saul, why are you persecuting me? It is hard for you to kick against the goads.",
   "M": "We all fell to the ground, and I heard a voice saying to me in Aramaic: Saul, Saul, why do you persecute me? It is hard for you to kick against the goads.",
   "T": "We all fell to the ground. I heard a voice say to me in Aramaic: Saul! Saul! Why are you persecuting me? It is hard for you to fight against your own conscience."
  },
  "15": {
   "L": "And I said: Who are you, Lord? And the Lord said: I am Jesus whom you are persecuting.",
   "M": "Then I asked: Who are you, Lord? I am Jesus, whom you are persecuting, the Lord replied.",
   "T": "I asked: Who are you, Lord? The Lord answered: I am Jesus—the one you are persecuting."
  },
  "16": {
   "L": "But rise and stand on your feet; for I have appeared to you for this purpose: to appoint you as a servant and witness both of what you have seen and of what I will show you,",
   "M": "Now get up and stand on your feet. I have appeared to you to appoint you as a servant and as a witness of what you have seen and will see of me.",
   "T": "But get up and stand on your feet. I have appeared to you to appoint you as my servant and witness—of what you have already seen and of what I will show you in the future."
  },
  "17": {
   "L": "rescuing you from the people and from the Gentiles, to whom I am sending you,",
   "M": "I will rescue you from your own people and from the Gentiles. I am sending you to them",
   "T": "I will rescue you from your own people and from the Gentiles, to whom I am now sending you—"
  },
  "18": {
   "L": "to open their eyes, so that they may turn from darkness to light and from the authority of Satan to God, that they may receive forgiveness of sins and a place among those who are sanctified by faith in me.",
   "M": "to open their eyes and turn them from darkness to light, and from the power of Satan to God, so that they may receive forgiveness of sins and a place among those who are sanctified by faith in me.",
   "T": "to open their eyes and turn them from darkness to light and from the power of Satan to God, so they may receive forgiveness of sins and a place among those who are set apart by faith in me."
  },
  "19": {
   "L": "Therefore, King Agrippa, I was not disobedient to the heavenly vision,",
   "M": "So then, King Agrippa, I was not disobedient to the vision from heaven.",
   "T": "So then, King Agrippa, I did not disobey the heavenly vision."
  },
  "20": {
   "L": "but declared first to those in Damascus, then in Jerusalem and throughout all the region of Judea, and to the Gentiles, that they should repent and turn to God, and perform deeds worthy of their repentance.",
   "M": "First to those in Damascus, then to those in Jerusalem and in all Judea, and then to the Gentiles, I preached that they should repent and turn to God and demonstrate their repentance by their deeds.",
   "T": "First to those in Damascus, then in Jerusalem and throughout all Judea, and then to the Gentiles—I proclaimed that they should turn to God in repentance and prove their repentance by how they live."
  },
  "21": {
   "L": "It was for this reason that the Jews seized me in the temple and tried to kill me.",
   "M": "That is why some Jews seized me in the temple courts and tried to kill me.",
   "T": "This is why the Jewish leaders seized me in the temple and tried to kill me."
  },
  "22": {
   "L": "But having obtained help from God, I have stood to this day testifying both to small and great, saying nothing except what the prophets and Moses said would take place,",
   "M": "But God has helped me to this very day; so I stand here and testify to small and great alike. I am saying nothing beyond what the prophets and Moses said would happen—",
   "T": "But God has helped me to this very day. I stand here testifying to small and great alike—saying nothing beyond what Moses and the prophets said would happen:"
  },
  "23": {
   "L": "that the Christ would suffer and that, as the first to rise from the dead, he would proclaim light to both our people and to the Gentiles.",
   "M": "that the Messiah would suffer and, as the first to rise from the dead, would bring the message of light to his own people and to the Gentiles.",
   "T": "that the Messiah would suffer and, as the first to rise from the dead, would bring the light of salvation to his own people and to the Gentiles."
  },
  "24": {
   "L": "And as he was saying these things in his defense, Festus said with a loud voice: Paul, you are out of your mind! Your great learning is driving you to madness.",
   "M": "At this point Festus interrupted Paul's defence. You are out of your mind, Paul! he shouted. Your great learning is driving you insane.",
   "T": "At this point, Festus burst out: You are out of your mind, Paul! All your learning has driven you mad!"
  },
  "25": {
   "L": "But Paul said: I am not out of my mind, most excellent Festus, but I am uttering words of truth and reason.",
   "M": "I am not insane, most excellent Festus, Paul replied. What I am saying is true and reasonable.",
   "T": "Paul said: I am not out of my mind, Most Excellent Festus. What I am saying is true and reasonable."
  },
  "26": {
   "L": "For the king knows about these things, and I speak freely to him. For I am convinced that nothing of these things is hidden from him; for this has not been done in a corner.",
   "M": "The king is familiar with these things, and I can speak freely to him. I am convinced that none of this has escaped his notice, because it was not done in a corner.",
   "T": "The king understands these things, and I can speak freely to him. I'm convinced none of this has escaped his notice—these things did not happen in some corner."
  },
  "27": {
   "L": "King Agrippa, do you believe the prophets? I know that you believe.",
   "M": "King Agrippa, do you believe the prophets? I know you do.",
   "T": "King Agrippa, do you believe the prophets? I know you do."
  },
  "28": {
   "L": "And Agrippa said to Paul: In a short time would you persuade me to be a Christian?",
   "M": "Then Agrippa said to Paul: Do you think that in such a short time you can persuade me to be a Christian?",
   "T": "Agrippa said to Paul: Do you actually think you can make me a Christian in such a short time?"
  },
  "29": {
   "L": "And Paul said: Whether short or long, I would to God that not only you but also all who hear me today would become such as I am—except for these chains.",
   "M": "Paul replied: Short time or long—I pray to God that not only you but all who are listening to me today may become what I am, except for these chains.",
   "T": "Paul said: Whether it takes a short time or a long one, I pray to God that not only you but everyone here listening to me today might become what I am—except for these chains."
  },
  "30": {
   "L": "And the king rose, and the governor and Bernice and those who were sitting with them.",
   "M": "The king rose, and with him the governor and Bernice and those sitting with them.",
   "T": "The king rose, and with him the governor and Bernice and all who were seated with them."
  },
  "31": {
   "L": "And as they were going aside, they were saying to one another: This man is doing nothing worthy of death or imprisonment.",
   "M": "After they left the room, they began saying to one another: This man is not doing anything that deserves death or imprisonment.",
   "T": "As they walked away, they said to one another: This man is not doing anything that deserves death or imprisonment."
  },
  "32": {
   "L": "And Agrippa said to Festus: This man could have been set free if he had not appealed to Caesar.",
   "M": "Agrippa said to Festus: This man could have been set free if he had not appealed to Caesar.",
   "T": "Agrippa said to Festus: This man could have been freed if he hadn't appealed to Caesar."
  }
 },
 "27": {
  "1": {
   "L": "And when it was decided that we should sail to Italy, they delivered Paul and some other prisoners to a centurion named Julius, of the Augustan Cohort.",
   "M": "When it was decided that we would sail for Italy, Paul and some other prisoners were handed over to a centurion named Julius, who belonged to the Imperial Regiment.",
   "T": "When it was decided that we would sail for Italy, Paul and some other prisoners were handed over to a centurion named Julius, of the Imperial Regiment."
  },
  "2": {
   "L": "And embarking in a ship of Adramyttium that was about to sail to the ports along the coast of Asia, we put out to sea, with Aristarchus, a Macedonian from Thessalonica, being with us.",
   "M": "We boarded a ship from Adramyttium about to sail for ports along the coasts of the province of Asia, and we put out to sea. Aristarchus, a Macedonian from Thessalonica, was with us.",
   "T": "We boarded a ship from Adramyttium that was heading for ports along the coast of Asia. We set sail, and Aristarchus—a Macedonian from Thessalonica—was with us."
  },
  "3": {
   "L": "And the next day we put in at Sidon; and Julius treated Paul kindly and allowed him to go to his friends to receive their care.",
   "M": "The next day we landed at Sidon; and Julius, in kindness to Paul, allowed him to go to his friends so they might provide for his needs.",
   "T": "The next day we landed at Sidon. Julius treated Paul kindly and allowed him to visit friends who could care for him."
  },
  "4": {
   "L": "And putting out to sea from there, we sailed under the shelter of Cyprus because the winds were contrary.",
   "M": "From there we put out to sea again and passed to the lee of Cyprus because the winds were against us.",
   "T": "Setting out again, we sailed in the shelter of Cyprus because the winds were against us."
  },
  "5": {
   "L": "And when we had sailed across the open sea along the coast of Cilicia and Pamphylia, we came down to Myra in Lycia.",
   "M": "When we had sailed across the open sea off the coast of Cilicia and Pamphylia, we landed at Myra in Lycia.",
   "T": "After sailing across the open sea off the coasts of Cilicia and Pamphylia, we arrived at Myra in Lycia."
  },
  "6": {
   "L": "And there the centurion found an Alexandrian ship sailing to Italy, and he put us aboard it.",
   "M": "There the centurion found an Alexandrian ship sailing for Italy and put us on board.",
   "T": "There the centurion found an Alexandrian ship bound for Italy and put us aboard."
  },
  "7": {
   "L": "And sailing slowly for many days and with difficulty arriving off Cnidus, the wind not allowing us to proceed, we sailed under the shelter of Crete off Salmone,",
   "M": "We made slow headway for many days and had difficulty arriving off Cnidus. When the wind did not allow us to hold our course, we sailed to the lee of Crete, opposite Salmone.",
   "T": "We made slow headway for many days and had difficulty reaching Cnidus. When the wind kept us from going further, we sailed in the shelter of Crete, past Cape Salmone."
  },
  "8": {
   "L": "and with difficulty sailing past it, we came to a place called Fair Havens, near which was the city of Lasea.",
   "M": "We moved along the coast with difficulty and came to a place called Fair Havens, near the town of Lasea.",
   "T": "We struggled along the coast and came to a place called Fair Havens, near the city of Lasea."
  },
  "9": {
   "L": "And much time had passed, and the voyage was now dangerous, since even the fast was already past; and Paul warned them,",
   "M": "Much time had been lost, and sailing had already become dangerous because by now it was after the Day of Atonement. So Paul warned them,",
   "T": "We had lost so much time that sailing had become dangerous—the Day of Atonement was already past. Paul warned them,"
  },
  "10": {
   "L": "saying to them: Men, I perceive that the voyage is going to result in disaster and great loss, not only of the cargo and the ship, but also of our lives.",
   "M": "Men, I can see that our voyage is going to be disastrous and bring great loss to ship and cargo, and to our own lives also.",
   "T": "Men, I can see that this voyage is going to end in disaster and great loss—not only to the ship and cargo, but to our own lives as well."
  },
  "11": {
   "L": "But the centurion was more persuaded by the pilot and the shipowner than by what was said by Paul.",
   "M": "But the centurion, instead of listening to what Paul said, followed the advice of the pilot and of the owner of the ship.",
   "T": "But the centurion trusted the pilot and the ship's owner more than Paul's warning."
  },
  "12": {
   "L": "Since the harbor was not suitable to winter in, the majority made a plan to put out to sea from there as well, if somehow they could reach Phoenix, a harbor of Crete facing both southwest and northwest, and winter there.",
   "M": "Since the harbour was unsuitable to winter in, the majority decided that we should sail on, hoping to reach Phoenix and winter there. This was a harbour in Crete, facing both south-west and north-west.",
   "T": "Since Fair Havens was not suitable for wintering, the majority voted to sail on and try to reach Phoenix—a harbor in Crete facing southwest and northwest—and winter there."
  },
  "13": {
   "L": "And when a gentle south wind blew, thinking they had obtained their purpose, they weighed anchor and were sailing along the coast of Crete.",
   "M": "When a gentle south wind began to blow, they saw their opportunity; so they weighed anchor and sailed along the shore of Crete.",
   "T": "When a gentle south wind began to blow, they thought they had their chance. They weighed anchor and sailed along the shore of Crete."
  },
  "14": {
   "L": "But before long, a violent wind, called the Northeaster, rushed down from it.",
   "M": "Before very long, a wind of hurricane force, called the Northeaster, swept down from the island.",
   "T": "But before long, a hurricane-force wind—called the Northeaster—swept down from the island."
  },
  "15": {
   "L": "And when the ship was caught and could not face the wind, we gave way to it and were driven along.",
   "M": "The ship was caught by the storm and could not head into the wind; so we gave way to it and were driven along.",
   "T": "The ship was caught by the storm and couldn't head into it. So we gave up and let ourselves be driven."
  },
  "16": {
   "L": "And running under the shelter of a small island called Cauda, we were barely able to secure the ship's boat.",
   "M": "As we passed to the lee of a small island called Cauda, we were hardly able to make the lifeboat secure,",
   "T": "We ran in the shelter of a small island called Cauda, where we barely managed to haul in the lifeboat."
  },
  "17": {
   "L": "After hoisting it, they used ropes to undergird the ship; and fearing that they would run aground on the Syrtis, they let down the anchor and were thus driven along.",
   "M": "so the men hoisted it aboard. Then they passed ropes under the ship itself to hold it together. Fearing that they would run aground on the sandbars of Syrtis, they lowered the sea anchor and let the ship be driven along.",
   "T": "They hoisted it on deck. Then they ran ropes under the hull to hold the ship together. Afraid of running aground on the sandbars of Syrtis, they lowered the sea anchor and let the ship drift."
  },
  "18": {
   "L": "And as we were being violently storm-tossed, the next day they began throwing the cargo overboard.",
   "M": "We took such a violent battering from the storm that the next day they began to throw the cargo overboard.",
   "T": "We were tossed so violently by the storm that the next day they began throwing the cargo overboard."
  },
  "19": {
   "L": "And on the third day they threw the ship's tackle overboard with their own hands.",
   "M": "On the third day, they threw the ship's tackle overboard with their own hands.",
   "T": "On the third day they threw the ship's equipment overboard with their own hands."
  },
  "20": {
   "L": "And when neither sun nor stars appeared for many days, and no small storm was pressing down upon us, all hope of our being saved was finally abandoned.",
   "M": "When neither sun nor stars appeared for many days and the storm continued raging, we finally gave up all hope of being saved.",
   "T": "When neither sun nor stars appeared for many days and the violent storm kept raging, we finally gave up all hope of surviving."
  },
  "21": {
   "L": "And after a long abstinence from food, then Paul stood up in their midst and said: Men, you should have heeded me and not set sail from Crete and incurred this damage and loss.",
   "M": "After the men had gone a long time without food, Paul stood up before them and said: Men, you should have taken my advice not to sail from Crete; then you would have spared yourselves this damage and loss.",
   "T": "After no one had eaten for a long time, Paul stood up among them and said: Men, you should have listened to me and not sailed from Crete—you would have avoided all this damage and loss."
  },
  "22": {
   "L": "But now I urge you to take heart, for there will be no loss of life among you, but only of the ship.",
   "M": "But now I urge you to keep up your courage, because not one of you will be lost; only the ship will be destroyed.",
   "T": "But now I urge you to keep your courage. Not one of you will lose your life—only the ship will be lost."
  },
  "23": {
   "L": "For this very night an angel of the God to whom I belong and whom I worship stood before me,",
   "M": "Last night an angel of the God to whom I belong and whom I serve stood beside me",
   "T": "Last night an angel of the God I belong to and serve stood beside me"
  },
  "24": {
   "L": "saying: Do not be afraid, Paul; you must stand before Caesar; and behold, God has granted you all those who sail with you.",
   "M": "and said: Do not be afraid, Paul. You must stand trial before Caesar; and God has graciously given you the lives of all who sail with you.",
   "T": "and said: Don't be afraid, Paul. You must stand before Caesar. And God has graciously given you the lives of everyone sailing with you."
  },
  "25": {
   "L": "Therefore take heart, men, for I believe God that it will be just as I have been told.",
   "M": "So keep up your courage, men, for I have faith in God that it will happen just as he told me.",
   "T": "So take heart, men—I trust God that it will happen exactly as he told me."
  },
  "26": {
   "L": "But we must run aground on some island.",
   "M": "Nevertheless, we must run aground on some island.",
   "T": "But we will run aground on some island."
  },
  "27": {
   "L": "When the fourteenth night had come, as we were being driven across the Adriatic Sea, about midnight the sailors began to suspect that they were approaching some land.",
   "M": "On the fourteenth night we were still being driven across the Adriatic Sea, when about midnight the sailors sensed they were approaching land.",
   "T": "On the fourteenth night we were still being driven across the Adriatic. About midnight the sailors sensed they were approaching land."
  },
  "28": {
   "L": "And taking soundings, they found twenty fathoms; and a little further on, taking soundings again, they found fifteen fathoms.",
   "M": "They took soundings and found that the water was twenty metres deep. A short time later they took soundings again and found it was fifteen metres deep.",
   "T": "They took soundings and found the water was about forty meters deep. A little farther on they took soundings again and found it was about thirty meters."
  },
  "29": {
   "L": "And fearing that we might run aground on rocky ground, they threw out four anchors from the stern and were praying for daylight to come.",
   "M": "Fearing that we would be dashed against the rocks, they dropped four anchors from the stern and prayed for daylight.",
   "T": "Afraid of being dashed against rocks, they dropped four anchors from the stern and prayed for daylight."
  },
  "30": {
   "L": "And the sailors were seeking to flee from the ship and had let down the ship's boat into the sea, pretending they were going to lay out anchors from the prow.",
   "M": "In an attempt to escape from the ship, the sailors let the lifeboat down into the sea, pretending they were going to lower some anchors from the bow.",
   "T": "Trying to escape, some sailors lowered the lifeboat into the sea, pretending they were going to drop anchors from the bow."
  },
  "31": {
   "L": "Paul said to the centurion and the soldiers: Unless these men remain in the ship, you cannot be saved.",
   "M": "Then Paul said to the centurion and the soldiers: Unless these men stay with the ship, you cannot be saved.",
   "T": "Paul said to the centurion and the soldiers: Unless these men stay on the ship, you cannot be saved."
  },
  "32": {
   "L": "Then the soldiers cut away the ropes of the ship's boat and let it fall away.",
   "M": "So the soldiers cut the ropes that held the lifeboat and let it drift away.",
   "T": "So the soldiers cut the ropes of the lifeboat and let it fall away."
  },
  "33": {
   "L": "And just before daybreak, Paul urged all of them to take some food, saying: Today is the fourteenth day you have been watching and going without food, having eaten nothing.",
   "M": "Just before dawn Paul urged them all to eat. For the last fourteen days, he said, you have been in constant suspense and have gone without food—you haven't eaten anything.",
   "T": "Just before dawn, Paul urged everyone to eat. He said: For fourteen days you have been in suspense, going without food. Now I urge you to eat something."
  },
  "34": {
   "L": "Therefore I urge you to take some food, for this is for your survival; for not a hair will fall from the head of any of you.",
   "M": "Now I urge you to take some food. You need it to survive. Not one of you will lose a single hair from his head.",
   "T": "You need it to survive—not one of you will lose a single hair from your head."
  },
  "35": {
   "L": "And saying these things and taking bread, he gave thanks to God before all; and breaking it, he began to eat.",
   "M": "After he said this, he took some bread and gave thanks to God in front of them all. Then he broke it and began to eat.",
   "T": "After saying this, he took some bread, gave thanks to God in front of everyone, broke it, and began to eat."
  },
  "36": {
   "L": "And they all took heart and ate some food themselves.",
   "M": "They were all encouraged and ate some food themselves.",
   "T": "Everyone was encouraged—and they all ate."
  },
  "37": {
   "L": "In all we were two hundred and seventy-six persons in the ship.",
   "M": "Altogether there were 276 of us on board.",
   "T": "In all, there were 276 people on the ship."
  },
  "38": {
   "L": "And having eaten their fill, they lightened the ship by throwing the grain into the sea.",
   "M": "When they had eaten as much as they wanted, they lightened the ship by throwing the grain into the sea.",
   "T": "When they had eaten enough, they lightened the ship by throwing the grain into the sea."
  },
  "39": {
   "L": "And when day came, they did not recognize the land; but they noticed a bay with a beach, and they resolved, if they were able, to run the ship aground on it.",
   "M": "When daylight came, they did not recognise the land, but they saw a bay with a sandy beach, where they decided to run the ship aground if they could.",
   "T": "When daylight came, they didn't recognize the land. But they saw a bay with a beach and decided to try to run the ship aground there."
  },
  "40": {
   "L": "And casting off the anchors, they left them in the sea; at the same time they untied the ropes of the steering oars; and hoisting the foresail to the wind, they made for the beach.",
   "M": "Cutting loose the anchors, they left them in the sea and at the same time untied the ropes that held the rudders. Then they hoisted the foresail to the wind and made for the beach.",
   "T": "They cut the anchors and left them in the sea. They loosened the ropes that held the rudders, raised the foresail to catch the wind, and headed for the beach."
  },
  "41": {
   "L": "But striking a reef where two seas met, they ran the vessel aground, and the prow stuck and remained immovable, but the stern was being broken up by the violence of the waves.",
   "M": "But the ship struck a sandbar and ran aground. The bow stuck fast and would not move, and the stern was broken to pieces by the pounding of the waves.",
   "T": "But the ship hit a sandbar and ran aground. The bow stuck fast and couldn't move, while the stern was broken to pieces by the pounding waves."
  },
  "42": {
   "L": "And the soldiers' plan was to kill the prisoners, lest any of them should swim away and escape.",
   "M": "The soldiers planned to kill the prisoners to prevent any of them from swimming away and escaping.",
   "T": "The soldiers planned to kill the prisoners to prevent any from swimming away and escaping."
  },
  "43": {
   "L": "But the centurion, wanting to save Paul, stopped them from carrying out their plan. He ordered those who could swim to jump overboard first and get to land.",
   "M": "But the centurion wanted to spare Paul's life and kept them from carrying out their plan. He ordered those who could swim to jump overboard first and get to land.",
   "T": "But the centurion, wanting to save Paul, stopped them. He ordered those who could swim to jump in first and get to land."
  },
  "44": {
   "L": "And the rest should follow, some on planks and some on other pieces from the ship. And so it came about that all escaped safely to the land.",
   "M": "The rest were to get there on planks or on other pieces of the ship. In this way everyone reached land safely.",
   "T": "The others were to follow, some on planks and some on wreckage from the ship. And so everyone made it safely to land."
  }
 },
 "28": {
  "1": {
   "L": "And when we had reached safety, we then learned that the island was called Malta.",
   "M": "Once safely on shore, we found out that the island was called Malta.",
   "T": "Once we were safely ashore, we learned the island was called Malta."
  },
  "2": {
   "L": "And the native people showed us unusual kindness, for they kindled a fire and welcomed us all, because of the rain that had begun to fall and because of the cold.",
   "M": "The islanders showed us unusual kindness. They built a fire and welcomed us all because it was raining and cold.",
   "T": "The islanders showed us remarkable kindness. They built a fire and welcomed all of us—it was raining and cold."
  },
  "3": {
   "L": "But when Paul had gathered a bundle of sticks and laid them on the fire, a viper came out because of the heat and fastened onto his hand.",
   "M": "Paul gathered a pile of brushwood and, as he put it on the fire, a viper, driven out by the heat, fastened itself on his hand.",
   "T": "Paul gathered a bundle of brushwood. As he put it on the fire, the heat drove out a viper that latched onto his hand."
  },
  "4": {
   "L": "When the native people saw the creature hanging from his hand, they said to one another: Surely this man is a murderer; though he escaped from the sea, Justice has not allowed him to live.",
   "M": "When the islanders saw the snake hanging from his hand, they said to each other: This man must be a murderer; for though he escaped from the sea, the goddess Justice has not allowed him to live.",
   "T": "When the islanders saw the snake hanging from his hand, they said to each other: This man must be a murderer. Even though he escaped the sea, Justice won't let him live."
  },
  "5": {
   "L": "But he shook off the creature into the fire and suffered no harm.",
   "M": "But Paul shook the snake off into the fire and suffered no ill effects.",
   "T": "But Paul shook the snake off into the fire and was completely unharmed."
  },
  "6": {
   "L": "They were expecting him to swell up or suddenly fall down dead. But after they had waited a long time and saw nothing unusual happen to him, they changed their minds and said he was a god.",
   "M": "The people expected him to swell up or suddenly fall dead; but after waiting a long time and seeing nothing unusual happen to him, they changed their minds and said he was a god.",
   "T": "The people expected him to swell up or suddenly drop dead. But after waiting a long time and seeing nothing unusual happen, they changed their minds and said he was a god."
  },
  "7": {
   "L": "Now in that neighborhood were lands belonging to the leading man of the island, named Publius, who welcomed us and entertained us hospitably for three days.",
   "M": "There was an estate nearby that belonged to Publius, the chief official of the island. He welcomed us to his home and showed us generous hospitality for three days.",
   "T": "The nearby estate belonged to Publius, the chief official of the island. He welcomed us and generously hosted us for three days."
  },
  "8": {
   "L": "And it happened that the father of Publius was lying sick with fever and dysentery. Paul visited him and after praying and laying his hands on him, he healed him.",
   "M": "His father was sick in bed, suffering from fever and dysentery. Paul went in to see him and, after prayer, placed his hands on him and healed him.",
   "T": "His father was in bed, sick with fever and dysentery. Paul went to him, prayed, placed his hands on him, and healed him."
  },
  "9": {
   "L": "And when this happened, the rest of the sick people on the island also came and were healed.",
   "M": "When this had happened, the rest of those on the island who had diseases came and were cured.",
   "T": "When this became known, the rest of the sick people on the island came to Paul and were healed."
  },
  "10": {
   "L": "They also honored us with many honors; and when we were about to sail, they supplied us with what we needed.",
   "M": "They honoured us in many ways; and when we were ready to sail, they furnished us with the supplies we needed.",
   "T": "They honored us in many ways. When we were ready to sail, they provided everything we needed."
  },
  "11": {
   "L": "And after three months we set sail in a ship that had wintered at the island—an Alexandrian ship with the Twin Brothers as its figurehead.",
   "M": "After three months we put out to sea in a ship that had wintered in the island—it was an Alexandrian ship with the figurehead of the twin gods Castor and Pollux.",
   "T": "After three months we sailed in an Alexandrian ship that had wintered there—its figurehead was the twin gods Castor and Pollux."
  },
  "12": {
   "L": "And putting in at Syracuse, we stayed there three days.",
   "M": "We put in at Syracuse and stayed there three days.",
   "T": "We put in at Syracuse and stayed three days."
  },
  "13": {
   "L": "And from there we sailed around and came to Rhegium; and after one day a south wind sprang up and on the second day we came to Puteoli.",
   "M": "From there we set sail and arrived at Rhegium. The next day the south wind came up, and on the following day we reached Puteoli.",
   "T": "From there we sailed around and reached Rhegium. A south wind came up the next day, and the day after we arrived at Puteoli."
  },
  "14": {
   "L": "There we found brothers and were invited to stay with them for seven days. And so we came to Rome.",
   "M": "There we found some brothers and sisters who invited us to spend a week with them. And so we came to Rome.",
   "T": "There we found believers who invited us to spend a week with them. And so we came to Rome."
  },
  "15": {
   "L": "And from there the brothers, when they heard about us, came to meet us as far as the Forum of Appius and Three Inns. On seeing them, Paul gave thanks to God and took courage.",
   "M": "The brothers and sisters there had heard that we were coming, and they travelled as far as the Forum of Appius and the Three Taverns to meet us. At the sight of these people Paul thanked God and was encouraged.",
   "T": "The brothers and sisters there had heard we were coming and traveled as far as the Forum of Appius and Three Taverns to meet us. When Paul saw them, he thanked God and took courage."
  },
  "16": {
   "L": "And when we came into Rome, Paul was allowed to stay by himself with the soldier who guarded him.",
   "M": "When we got to Rome, Paul was allowed to live by himself, with a soldier to guard him.",
   "T": "When we arrived in Rome, Paul was allowed to live by himself, with a soldier assigned to guard him."
  },
  "17": {
   "L": "And it came to pass after three days that Paul called together the leaders of the Jews. And when they had gathered, he said to them: Brothers, I did nothing against the people or the customs of our fathers; yet from Jerusalem I was delivered as a prisoner into the hands of the Romans.",
   "M": "Three days later he called together the local Jewish leaders. When they had assembled, Paul said to them: My brothers, although I have done nothing against our people or against the customs of our ancestors, I was arrested in Jerusalem and handed over to the Romans.",
   "T": "Three days after arriving, Paul called together the Jewish leaders of Rome. When they gathered, he said: Brothers, I have done nothing against our people or the customs of our ancestors. Yet I was arrested in Jerusalem and handed over to the Romans."
  },
  "18": {
   "L": "And when they had examined me, they wanted to release me because there was no ground for putting me to death.",
   "M": "They examined me and wanted to release me, because I was not guilty of any crime deserving death.",
   "T": "After examining me, they wanted to release me—I was not guilty of anything deserving death."
  },
  "19": {
   "L": "But when the Jews objected, I was compelled to appeal to Caesar—not that I had any charge to bring against my nation.",
   "M": "When the Jews objected, I was compelled to make an appeal to Caesar. I certainly did not intend to bring any charge against my own people.",
   "T": "But when the Jewish leaders objected, I was forced to appeal to Caesar—not because I had any charge to bring against my own nation."
  },
  "20": {
   "L": "For this reason therefore I have asked to see you and speak with you, since it is because of the hope of Israel that I am bound with this chain.",
   "M": "For this reason I have asked to see you and talk with you. It is because of the hope of Israel that I am bound with this chain.",
   "T": "That is why I asked to see you and talk with you. I am bound with this chain because of the hope of Israel."
  },
  "21": {
   "L": "And they said to him: We have not received any letters about you from Judea, and none of the brothers who came here has reported or spoken anything evil about you.",
   "M": "They replied: We have not received any letters from Judea concerning you, and none of our people who have come from there has reported or said anything bad about you.",
   "T": "They said: We have not received any letters from Judea about you, and none of the brothers who have come from there has reported or said anything bad about you."
  },
  "22": {
   "L": "But we want to hear from you what you think, for we know that this sect is spoken against everywhere.",
   "M": "But we want to hear what your views are, for we know that people everywhere are talking against this sect.",
   "T": "But we'd like to hear directly from you what you believe. We do know that this sect is spoken against everywhere."
  },
  "23": {
   "L": "And having set a day for him, they came to him at his lodging in greater numbers. He explained to them by solemnly testifying about the kingdom of God and by persuading them about Jesus from both the Law of Moses and the Prophets, from morning until evening.",
   "M": "They arranged to meet Paul on a certain day, and came in even larger numbers to the place where he was staying. He witnessed to them from morning till evening, explaining about the kingdom of God, and from the Law of Moses and from the Prophets he tried to persuade them about Jesus.",
   "T": "They set a day to meet with him, and a large crowd came to where Paul was staying. From morning until evening he explained everything—testifying about the kingdom of God and persuading them about Jesus from both Moses and the Prophets."
  },
  "24": {
   "L": "And some were persuaded by what he said, but others did not believe.",
   "M": "Some were convinced by what he said, but others would not believe.",
   "T": "Some were convinced by what he said, but others refused to believe."
  },
  "25": {
   "L": "And disagreeing with one another, they were departing, after Paul had made one statement: The Holy Spirit rightly spoke through Isaiah the prophet to your fathers,",
   "M": "They disagreed among themselves and began to leave after Paul had made this final statement: The Holy Spirit spoke the truth to your ancestors when he said through Isaiah the prophet:",
   "T": "They disagreed with one another and began to leave. But Paul had a final word: The Holy Spirit was right when he spoke to your ancestors through Isaiah the prophet:"
  },
  "26": {
   "L": "saying: Go to this people and say: You will indeed hear but never understand, and you will indeed see but never perceive.",
   "M": "Go to this people and say: You will be ever hearing but never understanding; you will be ever seeing but never perceiving.",
   "T": "Go to this people and say: You will hear and hear but never understand. You will look and look but never see."
  },
  "27": {
   "L": "For the heart of this people has become dull, and with their ears they can barely hear, and they have closed their eyes; lest they should perceive with their eyes and hear with their ears and understand with their heart and turn, and I would heal them.",
   "M": "For this people's heart has become calloused; they hardly hear with their ears, and they have closed their eyes. Otherwise they might see with their eyes, hear with their ears, understand with their hearts and turn, and I would heal them.",
   "T": "For the hearts of this people have grown callous—their ears are hard of hearing and their eyes are closed. Otherwise they might see with their eyes, hear with their ears, understand with their hearts—and turn to me, and I would heal them."
  },
  "28": {
   "L": "Therefore let it be known to you that this salvation of God has been sent to the Gentiles; they will also listen.",
   "M": "Therefore I want you to know that God's salvation has been sent to the Gentiles, and they will listen!",
   "T": "Therefore I want you to know that God's salvation has been sent to the Gentiles—and they will listen!"
  },
  "30": {
   "L": "And he stayed two whole years in his own rented dwelling and was receiving all who were coming to him,",
   "M": "For two whole years Paul stayed there in his own rented house and welcomed all who came to see him.",
   "T": "For two whole years Paul stayed in his own rented house and welcomed everyone who came to visit him."
  },
  "31": {
   "L": "proclaiming the kingdom of God and teaching the things about the Lord Jesus Christ with all boldness, without hindrance.",
   "M": "He proclaimed the kingdom of God and taught about the Lord Jesus Christ—with all boldness and without hindrance!",
   "T": "He proclaimed the kingdom of God and taught about the Lord Jesus Christ with complete freedom—and no one stopped him."
  }
 }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'acts')
        merge_tier(existing, ACTS_22_28, tier_key)
        save(tier_dir, 'acts', existing)
    print('Acts 22–28 written.')

if __name__ == '__main__':
    main()
