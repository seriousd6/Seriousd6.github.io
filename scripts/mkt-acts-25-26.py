"""
MKT Acts chapters 25–26 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-acts-25-26.py

Translation decisions (consistent with mkt-acts-1-5.py, 6-10, 11-15, 16-21):
- κύριος: "Lord" throughout
- Χριστός: "Christ" (L/M/T)
- πνεῦμα (Holy Spirit): capitalised when referring to the Holy Spirit
- ἐκκλησία: not prominent in these chapters
- ἀδελφοί: "brothers" (L); "brothers and sisters" (M/T)
- ἔθνη: "Gentiles" when contrasted with Jews; "nations" in OT citation (26:23)
- G4575 (σεβαστός / Σεβαστοῦ): "Augustus" (L/M); "the Emperor" (T) — the honorific
  title for the Roman emperor; Acts uses it for Caesar Augustus / the reigning emperor
- G4592 (σημεῖον): "sign" — not prominent in these chapters
- G3588 ναζωραῖος (26:9): "of Nazareth" — part of proper reference to Jesus
- σκληρόν σοι πρὸς κέντρα λακτίζειν (26:14): Proverbial expression meaning futile
  resistance; L: "hard for you to kick against the goads"; T: illuminates the futility
- G206 (ἄκρος): "most" — not used here
- G386 (ἀνάστασις 26:8,23): "resurrection/raise the dead" — core theological term;
  Paul's entire defense pivots on the resurrection claim
- Paul's conversion (ch 26): third telling (cf. chs 9 and 22); most theological version,
  addressed to a Gentile king — emphasises OT fulfilment and Gentile mission
- Festus's "you are mad" (26:24): G3130 (μανία): "madness"; L: "raving mad";
  M: "out of your mind"; T: "you've lost your mind"
- Paul's appeal to Caesar not undone by Agrippa (26:32): πεπραγματεύσατο not; rather
  the case had been appealed and could not be administratively reversed
- Aorist verbs throughout rendered as completed acts; imperfects as ongoing action
- Divine passive: 26:16 (ὤφθην / "I appeared") — God is agent; passive of vision
- OT intertextuality: 26:22–23 echoes Moses and the prophets; 26:18 echoes Isa 42:7,16
- 26:18 (ἐπιστρέψαι / "turn") and (σκότος → φῶς): light/darkness imagery; from LXX Isa
- 26:23 (πρῶτος ἐξ ἀναστάσεως): "first to rise from the dead" — Christ as firstfruits
  (cf. 1 Cor 15:20); T makes the firstfruits resonance explicit
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

  # ── CHAPTER 25 ─────────────────────────────────────────────────────────────
  "25": {
    "1": {
      "L": "Festus therefore, having come into the province, after three days went up to Jerusalem from Caesarea.",
      "M": "Three days after arriving in the province, Festus went up from Caesarea to Jerusalem,",
      "T": "Three days after taking up his post, Festus travelled up from Caesarea to Jerusalem."
    },
    "2": {
      "L": "And the chief priests and the principal men of the Jews informed him against Paul, and they were urging him,",
      "M": "where the chief priests and the Jewish leaders appeared before him and presented their charges against Paul.",
      "T": "There the chief priests and leading Jewish officials came to him and laid out their case against Paul."
    },
    "3": {
      "L": "asking a favour against him, that he would send for him to Jerusalem—laying an ambush to kill him along the way.",
      "M": "They requested Festus, as a favour to them, to have Paul transferred to Jerusalem, for they were preparing an ambush to kill him on the way.",
      "T": "They asked Festus to do them a favour and transfer Paul to Jerusalem—they were already planning to ambush and kill him on the road."
    },
    "4": {
      "L": "Festus therefore answered that Paul was being kept at Caesarea, and that he himself was about to depart there shortly.",
      "M": "Festus answered that Paul was being held at Caesarea, and that he himself was going back there soon.",
      "T": "Festus replied that Paul was being held in Caesarea and that he himself would be returning there before long."
    },
    "5": {
      "L": "'Let therefore those among you who are able go down with me, and if there is anything wrong in the man, let them accuse him.'",
      "M": "'Let your leaders come with me,' he said, 'and if the man has done anything wrong, they can press charges against him there.'",
      "T": "'So let your leading men come down with me,' he said, 'and if this man has actually done anything wrong, let them bring their accusations in the proper place.'"
    },
    "6": {
      "L": "And having spent among them not more than eight or ten days, he went down to Caesarea; and on the next day, sitting on the judgment seat, he commanded Paul to be brought.",
      "M": "After spending eight or ten days with them, Festus went down to Caesarea. The next day he convened the court and ordered Paul to be brought in.",
      "T": "After eight or ten days in Jerusalem, Festus went back to Caesarea. The very next day he took his seat on the tribunal and ordered Paul to be brought before him."
    },
    "7": {
      "L": "And when he had appeared, the Jews who had come down from Jerusalem stood around him, bringing many and serious charges against him which they were not able to prove,",
      "M": "When Paul arrived, the Jews who had come down from Jerusalem stood around him and brought many serious charges against him, which they could not prove.",
      "T": "When Paul appeared, the Jews who had come down from Jerusalem crowded around him and hurled charge after charge at him—serious accusations, none of which they could substantiate."
    },
    "8": {
      "L": "while Paul said in his defence: 'Neither against the law of the Jews, nor against the temple, nor against Caesar have I sinned at all.'",
      "M": "Then Paul made his defence: 'I have done nothing wrong against the Jewish law or against the temple or against Caesar.'",
      "T": "Paul simply stated his defence: 'I have committed no offence against the Jewish law, against the temple, or against Caesar—none whatsoever.'"
    },
    "9": {
      "L": "But Festus, wishing to do the Jews a favour, answered Paul and said: 'Are you willing to go up to Jerusalem and there be judged before me concerning these things?'",
      "M": "Festus, wanting to grant a favour to the Jews, said to Paul: 'Are you willing to go up to Jerusalem and stand trial before me there on these charges?'",
      "T": "Festus, who wanted to stay on good terms with the Jewish leaders, put the question to Paul: 'Would you be willing to go up to Jerusalem and face trial there before me on these charges?'"
    },
    "10": {
      "L": "But Paul said: 'I am standing before Caesar's judgment seat, where I ought to be judged. To the Jews I have done no wrong, as you yourself know very well.'",
      "M": "Paul answered: 'I am now standing before Caesar's court, where I ought to be tried. I have done nothing wrong to the Jews, as you yourself know very well.'",
      "T": "Paul replied: 'I am standing at the tribunal of Caesar—that is exactly where I ought to be tried. I have done nothing against the Jewish people, as you yourself know perfectly well.'"
    },
    "11": {
      "L": "'For if I am an offender and have done anything worthy of death, I do not refuse to die; but if there is nothing to the charges these men bring against me, no one can hand me over to them. I appeal to Caesar!'",
      "M": "'If I am guilty of doing anything deserving death, I do not refuse to die. But if the charges against me by these men are not true, no one has the right to hand me over to them. I appeal to Caesar!'",
      "T": "'If I have done something that deserves death, I am not trying to escape it. But if there is nothing to any of these accusations—and there is not—then no one has the right to hand me over to please them. I appeal to Caesar!'"
    },
    "12": {
      "L": "Then Festus, having conferred with the council, answered: 'You have appealed to Caesar; to Caesar you shall go.'",
      "M": "After Festus had conferred with his council, he declared: 'You have appealed to Caesar. To Caesar you will go!'",
      "T": "Festus withdrew to consult his advisers, then came back with his answer: 'You have appealed to Caesar. To Caesar you go!'"
    },
    "13": {
      "L": "And after some days had passed, Agrippa the king and Bernice arrived at Caesarea and greeted Festus.",
      "M": "A few days later King Agrippa and Bernice arrived at Caesarea to pay their respects to Festus.",
      "T": "Some days later King Agrippa and Bernice arrived in Caesarea on a state visit to welcome Festus."
    },
    "14": {
      "L": "And as they were spending many days there, Festus laid Paul's case before the king, saying: 'There is a certain man left a prisoner by Felix,'",
      "M": "Since they were spending several days there, Festus discussed Paul's case with the king. He said: 'There is a man here whom Felix left as a prisoner.'",
      "T": "They were there several days, and Festus used the time to lay Paul's situation before the king. 'There's a man here,' he said, 'whom Felix left behind under arrest.'"
    },
    "15": {
      "L": "'about whom, when I was in Jerusalem, the chief priests and the elders of the Jews informed me, asking for a verdict against him.'",
      "M": "'When I went to Jerusalem, the chief priests and the Jewish elders presented their case against him and asked me to condemn him.'",
      "T": "'When I was in Jerusalem, the chief priests and elders of the Jews presented their case against him and demanded I sentence him.'"
    },
    "16": {
      "L": "'I answered them that it is not the custom of the Romans to hand over any man before the accused meets his accusers face to face and has opportunity to make his defence against the charge.'",
      "M": "'I told them that it is not the Roman custom to hand over any man before he has faced his accusers and has had an opportunity to defend himself against the charges.'",
      "T": "'I told them plainly: Romans do not hand a man over for punishment before he has had the chance to face his accusers directly and make his own defence.'"
    },
    "17": {
      "L": "'When therefore they came together here, I made no delay, but on the next day sitting on the judgment seat I commanded the man to be brought.'",
      "M": "'When they came here with me, I did not delay the case, but convened the court the next day and ordered the man to be brought in.'",
      "T": "'So when they came here with me, I wasted no time. The very next day I took my seat on the tribunal and had the man brought in.'"
    },
    "18": {
      "L": "'When his accusers stood up, they brought no charge of such evil things as I supposed,'",
      "M": "'When his accusers got up to speak, they did not charge him with any of the crimes I had expected.'",
      "T": "'When his accusers stood up, the charges they brought were nothing like what I had anticipated.'"
    },
    "19": {
      "L": "'but had certain questions against him about their own religion, and about a certain Jesus who was dead, whom Paul claimed to be alive.'",
      "M": "'Instead, they had some disputes with him about their own religion and about a dead man named Jesus whom Paul claimed was alive.'",
      "T": "'Instead they had arguments with him about their own religion—and about a man named Jesus who had died, whom Paul kept insisting was alive.'"
    },
    "20": {
      "L": "'Being at a loss how to investigate these matters, I asked whether he would be willing to go to Jerusalem and there be judged about these things.'",
      "M": "'I was at a loss how to investigate such matters, so I asked if he would be willing to go to Jerusalem and stand trial there on these charges.'",
      "T": "'Since I had no idea how to handle this kind of dispute, I asked him whether he would be prepared to go to Jerusalem and face trial there on these questions.'"
    },
    "21": {
      "L": "'But when Paul had appealed to be kept for the hearing of the Emperor, I commanded him to be held until I could send him to Caesar.'",
      "M": "'But when Paul made his appeal to be held over for the Emperor's decision, I ordered him held until I could send him to Caesar.'",
      "T": "'But Paul appealed to be kept under custody for the Emperor to decide his case. So I ordered him detained until I could send him to Caesar.'"
    },
    "22": {
      "L": "Agrippa said to Festus: 'I also would like to hear the man myself.' 'Tomorrow,' he said, 'you shall hear him.'",
      "M": "Agrippa said to Festus: 'I would like to hear this man myself.' 'Tomorrow,' said Festus, 'you will hear him.'",
      "T": "Agrippa said, 'I would actually like to hear this man.' Festus replied, 'Tomorrow you will have your chance.'"
    },
    "23": {
      "L": "So on the next day, Agrippa and Bernice having come with great pomp, and having entered into the audience hall with the commanders and the prominent men of the city, at the command of Festus Paul was brought in.",
      "M": "The next day Agrippa and Bernice came with great pomp and entered the audience hall with the high-ranking military officers and the leading men of the city. At the command of Festus, Paul was brought in.",
      "T": "The following day there was a full ceremony. Agrippa and Bernice arrived in state and entered the auditorium with the military commanders and the city's most prominent citizens. On Festus's order, Paul was brought in."
    },
    "24": {
      "L": "And Festus said: 'King Agrippa and all men present with us, you see this man about whom all the Jewish multitude petitioned me, both at Jerusalem and here, crying out that he ought not to live any longer.'",
      "M": "Festus said: 'King Agrippa and all who are present with us, you see this man. The whole Jewish community has petitioned me about him, both in Jerusalem and here in Caesarea, shouting that he ought not to live any longer.'",
      "T": "Festus addressed them: 'King Agrippa and everyone gathered here—you see this man. Every part of the Jewish community, in Jerusalem and here in Caesarea, has been demanding his death, insisting he should not be allowed to live.'"
    },
    "25": {
      "L": "'But I found that he had done nothing deserving death; and as he himself had appealed to the Emperor, I decided to send him.'",
      "M": "'I found he had done nothing deserving death, but because he made his appeal to the Emperor, I decided to send him to Rome.'",
      "T": "'But my own investigation found nothing in him that deserves death. Since he appealed to the Emperor himself, I decided to send him.'"
    },
    "26": {
      "L": "'But I have no certain thing to write to my lord about him; therefore I brought him before you, and especially before you, King Agrippa, so that after the examination I may have something to write.'",
      "M": "'But I have nothing definite to write to His Majesty about him. Therefore I have brought him before all of you, and especially before you, King Agrippa, so that as a result of this investigation I may have something to write.'",
      "T": "'The trouble is, I have nothing solid to put in a letter to the Emperor. So I have brought him before you all—and especially before you, King Agrippa—hoping that this hearing will give me something concrete to report.'"
    },
    "27": {
      "L": "'For it seems to me unreasonable, in sending a prisoner, not to indicate also the charges against him.'",
      "M": "'For it seems absurd to me to send a prisoner without specifying the charges against him.'",
      "T": "'It would be absurd to send a prisoner to Rome without being able to state clearly what he is accused of.'"
    }
  },

  # ── CHAPTER 26 ─────────────────────────────────────────────────────────────
  "26": {
    "1": {
      "L": "And Agrippa said to Paul: 'You are permitted to speak for yourself.' Then Paul stretched out his hand and made his defence:",
      "M": "Then Agrippa said to Paul: 'You have permission to speak for yourself.' So Paul stretched out his hand and began his defence:",
      "T": "Agrippa gave Paul the floor: 'You may speak on your own behalf.' Paul raised his hand and began."
    },
    "2": {
      "L": "'I consider myself fortunate, King Agrippa, that I am to make my defence before you today against all the things of which I am accused by the Jews,'",
      "M": "'King Agrippa, I consider myself fortunate to stand before you today as I make my defence against all the accusations of the Jews,'",
      "T": "'King Agrippa, I count myself fortunate to be standing before you today to answer these charges from the Jewish leaders.'"
    },
    "3": {
      "L": "'especially because you are an expert in all the customs and controversies of the Jews; therefore I beg you to listen to me patiently.'",
      "M": "'especially since you are well acquainted with all the Jewish customs and controversies. I beg you therefore to listen to me patiently.'",
      "T": "'You are a man who knows the Jewish world intimately—every custom, every controversy. I am asking you simply to hear me out.'"
    },
    "4": {
      "L": "'My manner of life from youth, which was lived from the beginning among my own nation and in Jerusalem, all the Jews know,'",
      "M": "'The Jewish people all know the way I have lived since I was young, from the beginning of my life in my own country and later in Jerusalem.'",
      "T": "'Every Jew who knows anything about me knows how I lived from my earliest years—first in my homeland, then in Jerusalem.'"
    },
    "5": {
      "L": "'having known me from the beginning, if they are willing to testify, that according to the strictest sect of our religion I lived as a Pharisee.'",
      "M": "'They have known me for a long time and can testify, if they are willing, that I lived as a Pharisee, according to the strictest sect of our religion.'",
      "T": "'They have known me from the start. If they were willing to be honest, they would confirm that I lived as a Pharisee—following the strictest interpretation of our religion.'"
    },
    "6": {
      "L": "'And now I stand here being judged for the hope of the promise made by God to our fathers,'",
      "M": "'And now it is because of my hope in what God has promised our ancestors that I am on trial today.'",
      "T": "'And here I stand on trial—for nothing other than the hope that comes from God's promise to our ancestors.'"
    },
    "7": {
      "L": "'to which our twelve tribes, earnestly serving night and day, hope to attain; and for this hope I am accused by Jews, O King.'",
      "M": "'This is the promise our twelve tribes are hoping to see fulfilled as they earnestly serve God day and night. It is because of this hope, O King, that these Jews are accusing me.'",
      "T": "'It is the very hope our twelve tribes reach toward as they serve God earnestly, morning and night. And yet, O King, it is because of this hope that the Jews are bringing charges against me.'"
    },
    "8": {
      "L": "'Why is it judged incredible among you if God raises the dead?'",
      "M": "'Why should any of you consider it incredible that God raises the dead?'",
      "T": "'Why is it thought unbelievable that God can raise the dead? Why?'"
    },
    "9": {
      "L": "'I myself indeed thought that I ought to do many things contrary to the name of Jesus of Nazareth,'",
      "M": "'I too was convinced that I ought to do all that was possible to oppose the name of Jesus of Nazareth.'",
      "T": "'I will be honest: I myself once believed it was my duty to fight against the name of Jesus of Nazareth in every way I could.'"
    },
    "10": {
      "L": "'which I also did in Jerusalem; and many of the saints I shut up in prison, having received authority from the chief priests; and when they were being put to death, I cast my vote against them.'",
      "M": "'And that is just what I did in Jerusalem. On the authority of the chief priests I put many of the Lord's people in prison, and when they were put to death, I cast my vote against them.'",
      "T": "'And that is exactly what I did in Jerusalem. With authority from the chief priests, I threw many of God's people in prison. When they were sentenced to death, I voted for it.'"
    },
    "11": {
      "L": "'And in all the synagogues I punished them often and tried to force them to blaspheme; and being exceedingly enraged at them, I persecuted them even to foreign cities.'",
      "M": "'Many a time I went from one synagogue to another to have them punished, and I tried to force them to blaspheme. I was so obsessed with persecuting them that I even hunted them down in foreign cities.'",
      "T": "'Synagogue by synagogue, I had them beaten and tried to force them to deny their faith. My rage drove me even beyond our borders—I was hunting them down in foreign cities.'"
    },
    "12": {
      "L": "'On such a mission I was going to Damascus with the authority and commission of the chief priests,'",
      "M": "'On one of these journeys I was going to Damascus with the authority and commission of the chief priests.'",
      "T": "'That is what I was doing when I set out for Damascus—armed with the authority and orders of the chief priests.'"
    },
    "13": {
      "L": "'O King, at midday on the way I saw a light from heaven, brighter than the sun, shining around me and those who were travelling with me.'",
      "M": "'About noon, O King, as I was on the road, I saw a light from heaven, brighter than the sun, blazing around me and my companions.'",
      "T": "'At midday, O King, a light blazed down from heaven—brighter than the sun itself—surrounding me and everyone travelling with me.'"
    },
    "14": {
      "L": "'And when we had all fallen to the ground, I heard a voice saying to me in the Hebrew language: \"Saul, Saul, why are you persecuting me? It is hard for you to kick against the goads.\"'",
      "M": "'We all fell to the ground, and I heard a voice saying to me in Aramaic: \"Saul, Saul, why do you persecute me? It is hard for you to kick against the goads.\"'",
      "T": "'We all fell to the ground. Then I heard a voice in our own language—Hebrew—speaking directly to me: \"Saul, Saul, why are you persecuting me? You are only hurting yourself by fighting what you cannot stop.\"'"
    },
    "15": {
      "L": "'And I said, \"Who are you, Lord?\" And the Lord said: \"I am Jesus whom you are persecuting.\"'",
      "M": "'\"Who are you, Lord?\" I asked. \"I am Jesus, whom you are persecuting,\" the Lord replied.',",
      "T": "'I asked, \"Who are you, Lord?\" The answer came: \"I am Jesus—the one you are persecuting.\"'"
    },
    "16": {
      "L": "'But rise and stand on your feet; for I have appeared to you for this purpose: to appoint you as a servant and a witness both of the things you have seen of me and of those in which I will appear to you,'",
      "M": "'\"Now get up and stand on your feet. I have appeared to you to appoint you as a servant and as a witness of what you have seen and what I will show you.\"'",
      "T": "'\"Get up and stand. I have appeared to you for a reason: to commission you as my servant and witness—both to what you have seen today and to what I will still reveal to you.\"'"
    },
    "17": {
      "L": "'delivering you from the people and from the Gentiles to whom I am sending you,'",
      "M": "'\"I will rescue you from your own people and from the Gentiles. I am sending you to them\"'",
      "T": "'\"I will keep you safe from your own people and from the Gentiles—the very people I am sending you to.\"'"
    },
    "18": {
      "L": "'to open their eyes, so that they may turn from darkness to light and from the power of Satan to God, that they may receive forgiveness of sins and a share among those who are sanctified by faith in me.'",
      "M": "'\"to open their eyes and turn them from darkness to light, and from the power of Satan to God, so that they may receive forgiveness of sins and a place among those who are sanctified by faith in me.\"'",
      "T": "'\"—to open their eyes, to turn them from darkness toward light, and from the dominion of Satan to the living God. So they may receive forgiveness for all they have done, and a share in the inheritance that belongs to all who are set apart through faith in me.\"'"
    },
    "19": {
      "L": "'Therefore, King Agrippa, I was not disobedient to the heavenly vision,'",
      "M": "'So then, King Agrippa, I was not disobedient to the vision from heaven.'",
      "T": "'And so, King Agrippa, I did not ignore the vision from heaven.'"
    },
    "20": {
      "L": "'but declared first to those in Damascus, and in Jerusalem, and throughout all the country of Judaea, and to the Gentiles, that they should repent and turn to God, performing deeds worthy of repentance.'",
      "M": "'First to those in Damascus, then to those in Jerusalem and in all Judea, and then to the Gentiles also, I preached that they should repent and turn to God and demonstrate their repentance by their deeds.'",
      "T": "'Starting in Damascus, then Jerusalem, then across all of Judea, and then out to the Gentiles—I proclaimed a single message: turn back to God, and let your actions show it is real.'"
    },
    "21": {
      "L": "'For these reasons the Jews seized me in the temple and tried to kill me.'",
      "M": "'That is why some Jews seized me in the temple courts and tried to kill me.'",
      "T": "'That is what the Jewish leaders seized me for in the temple—and that is why they tried to kill me.'"
    },
    "22": {
      "L": "'Having therefore obtained help from God, I stand to this day testifying both to small and great, saying nothing but what the prophets and Moses said would come to pass:'",
      "M": "'But God has helped me to this very day; so I stand here and testify to small and great alike. I am saying nothing beyond what the prophets and Moses said would happen—'",
      "T": "'But God has been my help, and I am still standing. To this day I testify before everyone—important or unimportant—and I say nothing that goes beyond what Moses and the prophets predicted:'"
    },
    "23": {
      "L": "'that the Christ was to suffer, that he, as the first to rise from the dead, would proclaim light both to the people and to the Gentiles.'",
      "M": "'that the Messiah would suffer and, as the first to rise from the dead, would bring the message of light to his own people and to the Gentiles.'",
      "T": "'that the Messiah had to suffer—and that he, as the firstfruits of the resurrection, would be the one to announce the dawn of light to Israel and to all the nations.'"
    },
    "24": {
      "L": "And as he was saying these things in his defence, Festus said with a loud voice: 'Paul, you are out of your mind! Your great learning is driving you to madness!'",
      "M": "At this point Festus interrupted Paul's defence. 'You are out of your mind, Paul!' he shouted. 'Your great learning is driving you insane!'",
      "T": "That was too much for Festus. He cut Paul off mid-sentence and bellowed: 'Paul, you have lost your mind! All that study has pushed you over the edge!'"
    },
    "25": {
      "L": "But Paul said: 'I am not out of my mind, most excellent Festus, but I am speaking words of truth and soberness.'",
      "M": "'I am not insane, most excellent Festus,' Paul replied. 'What I am saying is true and reasonable.'",
      "T": "'I am not out of my mind, most excellent Festus,' Paul replied quietly. 'Everything I am saying is sober truth.'"
    },
    "26": {
      "L": "'For the king knows about these things, and to him I also speak boldly; for I am persuaded that none of these things is hidden from him, for this was not done in a corner.'",
      "M": "'The king is familiar with these things, and to him I can speak freely. I am convinced he already knows about all this. It was not done in a corner.'",
      "T": "'The king understands these things—that is why I am speaking so directly to him. I am quite certain none of this is news to him. It did not happen in a back room somewhere.'"
    },
    "27": {
      "L": "'King Agrippa, do you believe the prophets? I know that you believe.'",
      "M": "'King Agrippa, do you believe the prophets? I know you do.'",
      "T": "'King Agrippa—do you believe the prophets? I know you do.'"
    },
    "28": {
      "L": "And Agrippa said to Paul: 'In a short time you are persuading me to become a Christian!'",
      "M": "Then Agrippa said to Paul: 'Do you think that in such a short time you can persuade me to be a Christian?'",
      "T": "Agrippa's reply was terse: 'You almost have me convinced, Paul—you nearly make me a Christian.'"
    },
    "29": {
      "L": "And Paul said: 'I would pray to God that whether in a short time or in a long time, not only you but also all who hear me this day might become such as I am—except for these chains.'",
      "M": "Paul replied: 'Short time or long—I pray to God that not only you but all who are listening to me today may become what I am, except for these chains.'",
      "T": "Paul said quietly: 'Short time or long, I pray to God that every person in this room—not just you—would come to be exactly what I am. Except, of course, for these chains.'"
    },
    "30": {
      "L": "The king rose, and the governor and Bernice and those sitting with them,",
      "M": "The king rose, and with him the governor and Bernice and those sitting with them.",
      "T": "At that, the king stood up. So did the governor, Bernice, and everyone else in the room."
    },
    "31": {
      "L": "and withdrawing they talked with one another, saying: 'This man is doing nothing deserving death or imprisonment.'",
      "M": "As they were leaving, they said to one another: 'This man is not doing anything that deserves death or imprisonment.'",
      "T": "As they withdrew to a private room, they said to each other: 'This man has done nothing to deserve death or even imprisonment.'"
    },
    "32": {
      "L": "And Agrippa said to Festus: 'This man could have been set free if he had not appealed to Caesar.'",
      "M": "Agrippa said to Festus: 'This man could have been set free if he had not appealed to Caesar.'",
      "T": "Agrippa summed it up to Festus: 'He could have walked free if he hadn't appealed to Caesar.'"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'acts')
        merge_tier(existing, ACTS, tier_key)
        save(tier_dir, 'acts', existing)
    print('Acts 25–26 written.')

if __name__ == '__main__':
    main()
