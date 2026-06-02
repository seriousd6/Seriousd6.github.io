"""
MKT Acts chapters 11–15 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-acts-11-15.py

Translation decisions (consistent with mkt-acts-1-5.py):
- πνεῦμα (Spirit): capitalised when referring to the Holy Spirit; lowercase for human spirit.
- κύριος (Lord): retained for both God and Jesus; context determines referent.
- Χριστός (Christ): "Christ" in L/M; "Anointed One" or "Anointed King" in T when
  the messianic office is in view (e.g. 13:23).
- ἐκκλησία: "assembly" (L), "church" (M), "community" (T).
- μετανοέω / μετάνοια: "repentance/repent" (L/M); "turn back / turning" (T).
- βαπτίζω: "baptize" (L/M); "immerse" (T) where the water ritual is foregrounded.
- ἄφεσις: "forgiveness" across M/T; "remission/release" only in fully literal contexts.
- δικαιόω (13:39): "justify" (L), "set free / justified" (M), "put right with God" (T).
- εὐαγγελίζω: "proclaim the good news / preach the gospel" (L/M); "announce the good
  news" (T).
- ἐθνικοί / ἔθνη: "Gentiles" throughout — no softening to "nations" in narrative prose
  (reserve "nations" for OT citations where LXX ἔθνη is in view, e.g. 13:47 / 15:17).
- Acts 15:34 is a Western-text insertion absent from the best Alexandrian MSS (NA28
  brackets it). The interlinear data includes it as verse 34, so we translate it here
  but keep the rendering minimal and note the textual status in the L tier.
- Aorist verbs rendered as simple completed acts; presents as ongoing states.
- OT quotations (13:33–35, 13:41, 13:47, 15:16–17) preserved close to LXX in L;
  rendered as living speech in T.
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

  # ── CHAPTER 11 ─────────────────────────────────────────────────────────────
  "11": {
    "1": {
      "L": "Now the apostles and the brothers who were throughout Judaea heard that the Gentiles also had received the word of God.",
      "M": "The apostles and the believers throughout Judea heard that the Gentiles had also received the word of God.",
      "T": "Word spread throughout Judea to the apostles and other believers: the Gentiles too had received God's word."
    },
    "2": {
      "L": "And when Peter went up to Jerusalem, those of the circumcision contended with him,",
      "M": "So when Peter went up to Jerusalem, the circumcised believers took issue with him",
      "T": "When Peter arrived in Jerusalem, the Jewish believers confronted him,"
    },
    "3": {
      "L": "saying, 'You went in to uncircumcised men and ate with them!'",
      "M": "and said, 'You went into the house of uncircumcised men and ate with them!'",
      "T": "'You entered the home of uncircumcised people,' they said, 'and sat down to eat with them!'"
    },
    "4": {
      "L": "But Peter, beginning from the start, set it out to them in order, saying:",
      "M": "Starting from the beginning, Peter explained everything to them in order, saying:",
      "T": "Peter took a breath and walked them through the whole story from the start:"
    },
    "5": {
      "L": "'I was in the city of Joppa praying, and in a trance I saw a vision: a certain vessel descending like a great sheet, let down from heaven by four corners; and it came toward me.'",
      "M": "'I was in the city of Joppa praying, and in a trance I saw a vision. I saw something like a large sheet being let down from heaven by its four corners, and it came down toward me.'",
      "T": "'I was in Joppa, praying. I fell into a trance and saw a vision—something like a huge sheet being lowered from heaven by its four corners, coming right down to where I was.'"
    },
    "6": {
      "L": "'When I looked at it closely and observed, I saw the four-footed animals of the earth and the wild beasts and the creeping things and the birds of the sky.'",
      "M": "'I looked into it and saw four-footed animals of the earth, wild beasts, reptiles, and birds.'",
      "T": "'I peered in and saw all kinds of animals—four-footed creatures, wild beasts, reptiles, birds of every kind.'"
    },
    "7": {
      "L": "'And I heard a voice saying to me: \"Rise, Peter; kill and eat.\"'",
      "M": "'Then I heard a voice tell me, \"Get up, Peter. Kill and eat.\"'",
      "T": "'Then a voice spoke to me: \"Get up, Peter. Kill something and eat.\"'"
    },
    "8": {
      "L": "'But I said, \"By no means, Lord; for nothing common or unclean has ever entered into my mouth.\"'",
      "M": "'I replied, \"Surely not, Lord! Nothing impure or unclean has ever entered my mouth.\"'",
      "T": "'I said, \"Absolutely not, Lord! I have never put anything impure or ritually unclean in my mouth.\"'"
    },
    "9": {
      "L": "'But a voice answered a second time from heaven: \"What God has cleansed, do not you call common.\"'",
      "M": "'The voice spoke from heaven a second time: \"Do not call anything impure that God has made clean.\"'",
      "T": "'But the voice from heaven came back a second time: \"Don\'t call something unclean when God has declared it clean.\"'"
    },
    "10": {
      "L": "'This happened three times, and everything was drawn up again into heaven.'",
      "M": "'This happened three times, and then it was all pulled back up into heaven.'",
      "T": "'This happened three times over, and then the whole thing was pulled back up to heaven.'"
    },
    "11": {
      "L": "'And behold, at that very moment three men stood before the house where I was, having been sent to me from Caesarea.'",
      "M": "'Right then three men who had been sent to me from Caesarea stopped at the house where I was staying.'",
      "T": "'At that exact moment—three men sent from Caesarea appeared at the door of the house where I was.'"
    },
    "12": {
      "L": "'And the Spirit told me to go with them, making no distinction. And these six brothers also came with me, and we entered the man's house.'",
      "M": "'The Spirit told me to go with them and not to hesitate. These six brothers also went with me, and we entered the man's house.'",
      "T": "'The Spirit told me to go with them without any hesitation. These six brothers here came along as witnesses, and we went into the man's house.'"
    },
    "13": {
      "L": "'And he told us how he had seen the angel standing in his house and saying: \"Send to Joppa and bring Simon who is called Peter;\"'",
      "M": "'He told us how he had seen an angel appear in his house and say: \"Send to Joppa for Simon who is called Peter.\"'",
      "T": "'Cornelius told us how he had seen an angel standing in his home who said: \"Send someone to Joppa and bring back a man named Simon, who is called Peter.\"'"
    },
    "14": {
      "L": "'who will speak words to you by which you and all your household will be saved.'",
      "M": "'He will bring you a message through which you and all your household will be saved.'",
      "T": "'He will tell you a message through which you and your entire household will be rescued.'"
    },
    "15": {
      "L": "'And as I began to speak, the Holy Spirit fell upon them, just as upon us at the beginning.'",
      "M": "'As I began to speak, the Holy Spirit came on them as he had come on us at the beginning.'",
      "T": "'The moment I began to speak, the Holy Spirit fell on them—exactly as he had fallen on us at Pentecost.'"
    },
    "16": {
      "L": "'And I remembered the word of the Lord, how he said: \"John baptized with water, but you will be baptized with the Holy Spirit.\"'",
      "M": "'Then I remembered what the Lord had said: \"John baptized with water, but you will be baptized with the Holy Spirit.\"'",
      "T": "'This brought back the Lord's own words to me: \"John immersed people in water, but you will be immersed in the Holy Spirit.\"'"
    },
    "17": {
      "L": "'If therefore God gave them the same gift as he also gave to us, having believed on the Lord Jesus Christ, who was I to withstand God?'",
      "M": "'So if God gave them the same gift he gave us when we believed in the Lord Jesus Christ, who was I to think that I could stand in God's way?'",
      "T": "'If God gave them the very same gift he gave us when we put our trust in the Lord Jesus—who was I to get in God's way?'"
    },
    "18": {
      "L": "When they heard these things they were silenced, and they glorified God, saying, 'Then to the Gentiles also God has granted repentance that leads to life.'",
      "M": "When they heard this, they had no further objections and praised God, saying, 'So then, even to Gentiles God has granted repentance that leads to life.'",
      "T": "When they heard this, the room fell silent. Then they began praising God: 'So God has given even the Gentiles the chance to turn and receive life.'"
    },
    "19": {
      "L": "Now those who were scattered by the tribulation that arose over Stephen went as far as Phoenicia and Cyprus and Antioch, speaking the word to no one except to Jews only.",
      "M": "Now those who had been scattered by the persecution that broke out when Stephen was killed travelled as far as Phoenicia, Cyprus and Antioch, spreading the word only among Jews.",
      "T": "The believers scattered by the persecution following Stephen's death made their way to Phoenicia, Cyprus, and Antioch—but they were sharing the message only with fellow Jews."
    },
    "20": {
      "L": "But there were some among them, men of Cyprus and Cyrene, who, when they came to Antioch, spoke to the Hellenists also, proclaiming the Lord Jesus.",
      "M": "Some of them, however, men from Cyprus and Cyrene, went to Antioch and began to speak to Greeks also, telling them the good news about the Lord Jesus.",
      "T": "But some of the believers—men from Cyprus and Cyrene—arrived in Antioch and began sharing the good news about the Lord Jesus with Greek-speaking Gentiles as well."
    },
    "21": {
      "L": "And the hand of the Lord was with them, and a great number, having believed, turned to the Lord.",
      "M": "The Lord's hand was with them, and a great number of people believed and turned to the Lord.",
      "T": "The Lord's power was with them, and large numbers of people came to faith and turned to the Lord."
    },
    "22": {
      "L": "The report about them came to the ears of the assembly in Jerusalem, and they sent out Barnabas to go as far as Antioch.",
      "M": "News of this reached the church in Jerusalem, and they sent Barnabas to Antioch.",
      "T": "Word of this reached the community in Jerusalem, and they sent Barnabas to Antioch to see what was happening."
    },
    "23": {
      "L": "Who, having arrived and having seen the grace of God, rejoiced, and exhorted all with purpose of heart to remain in the Lord.",
      "M": "When he arrived and saw what the grace of God had done, he was glad and encouraged them all to remain true to the Lord with all their hearts.",
      "T": "When Barnabas arrived and saw the grace of God at work, he was overjoyed. He urged them all to hold fast to the Lord with wholehearted commitment."
    },
    "24": {
      "L": "For he was a good man and full of the Holy Spirit and of faith. And a considerable crowd was added to the Lord.",
      "M": "He was a good man, full of the Holy Spirit and faith, and a great number of people were brought to the Lord.",
      "T": "Barnabas was a good man, filled with the Holy Spirit and genuine faith—and through his ministry a great many more people joined the Lord."
    },
    "25": {
      "L": "And he went out to Tarsus to seek Saul,",
      "M": "Then Barnabas went to Tarsus to look for Saul,",
      "T": "Then Barnabas set off for Tarsus to track down Saul,"
    },
    "26": {
      "L": "and having found him, he brought him to Antioch. And it came about that for a whole year they were gathered together with the assembly and taught a considerable crowd; and the disciples were first called Christians in Antioch.",
      "M": "and when he found him, he brought him to Antioch. So for a whole year Barnabas and Saul met with the church and taught great numbers of people. The disciples were first called Christians at Antioch.",
      "T": "and when he found him, brought him back to Antioch. For an entire year the two of them worked and taught alongside the community there, and a great many people were instructed. It was at Antioch that the disciples first received the name 'Christians.'"
    },
    "27": {
      "L": "Now in those days prophets came down from Jerusalem to Antioch.",
      "M": "During this time some prophets came down from Jerusalem to Antioch.",
      "T": "While they were there, a group of prophets came down from Jerusalem to Antioch."
    },
    "28": {
      "L": "And one of them named Agabus stood up and indicated through the Spirit that there was going to be a great famine over all the inhabited world, which also came to pass under Claudius.",
      "M": "One of them, named Agabus, stood up and through the Spirit predicted that a severe famine would spread over the entire Roman world. This happened during the reign of Claudius.",
      "T": "One of them—a man named Agabus—stood up and, guided by the Spirit, predicted that a severe famine was coming across the whole known world. This did come to pass during the reign of Claudius."
    },
    "29": {
      "L": "And each of the disciples, as any had the means, determined to send relief to the brothers dwelling in Judaea.",
      "M": "The disciples, according to their ability, each decided to provide help for the brothers and sisters living in Judea.",
      "T": "Each of the disciples decided to send what they could to help the believers in Judea."
    },
    "30": {
      "L": "Which they also did, sending it to the elders by the hand of Barnabas and Saul.",
      "M": "This they did, sending their gift to the elders by Barnabas and Saul.",
      "T": "They followed through, delivering the relief to the elders through Barnabas and Saul."
    }
  },

  # ── CHAPTER 12 ─────────────────────────────────────────────────────────────
  "12": {
    "1": {
      "L": "Now about that time Herod the king put forth his hands to oppress some of those from the assembly.",
      "M": "It was about this time that King Herod arrested some who belonged to the church, intending to persecute them.",
      "T": "Around that time, King Herod began targeting members of the community for persecution."
    },
    "2": {
      "L": "And he killed James the brother of John with the sword.",
      "M": "He had James, the brother of John, put to death with the sword.",
      "T": "He had James, the brother of John, executed by the sword."
    },
    "3": {
      "L": "And having seen that it pleased the Jews, he proceeded to arrest Peter also. Now it was the days of Unleavened Bread.",
      "M": "When he saw that this met with approval among the Jewish leaders, he proceeded to seize Peter also. This happened during the Festival of Unleavened Bread.",
      "T": "When Herod saw that this pleased the Jewish authorities, he moved to arrest Peter as well. This was during the Festival of Unleavened Bread."
    },
    "4": {
      "L": "Having seized him, he put him in prison, handing him over to four squads of four soldiers each to guard him, intending after the Passover to bring him out to the people.",
      "M": "After arresting him, he put him in prison, handing him over to be guarded by four squads of four soldiers each. Herod intended to bring him out for public trial after the Passover.",
      "T": "He had Peter arrested and thrown into prison, placed under a sixteen-man guard. Herod planned to put him on public trial after Passover."
    },
    "5": {
      "L": "So Peter was kept in the prison, but fervent prayer was being made to God by the assembly for him.",
      "M": "So Peter was kept in prison, but the church was earnestly praying to God for him.",
      "T": "Peter stayed in prison, while the community poured itself into praying fervently to God on his behalf."
    },
    "6": {
      "L": "And when Herod was about to bring him out, that very night Peter was sleeping between two soldiers, bound with two chains; and guards before the door were keeping watch over the prison.",
      "M": "The night before Herod was to bring him to trial, Peter was sleeping between two soldiers, bound with two chains, and sentries stood guard at the entrance.",
      "T": "On the very night before Herod was to put him on trial, Peter was sleeping chained between two guards. More soldiers kept watch at the outer door."
    },
    "7": {
      "L": "And behold, an angel of the Lord stood by him, and a light shone in the cell; and striking Peter on the side, he woke him, saying, 'Rise up quickly.' And his chains fell off from his hands.",
      "M": "Suddenly an angel of the Lord appeared and a light shone in the cell. He struck Peter on the side and woke him up. 'Quick, get up!' he said, and the chains fell off Peter's wrists.",
      "T": "Suddenly an angel of the Lord appeared, and the cell was flooded with light. The angel struck Peter on the side to wake him. 'Get up—quickly!' The chains dropped from Peter's wrists."
    },
    "8": {
      "L": "And the angel said to him, 'Dress yourself and put on your sandals.' And he did so. And he said to him, 'Wrap your outer garment around you and follow me.'",
      "M": "The angel told him, 'Put on your clothes and sandals.' Peter did so. 'Wrap your cloak around you and follow me,' the angel told him.",
      "T": "'Get dressed and put on your sandals,' the angel said. Peter did so. 'Now pull on your cloak and come with me.'"
    },
    "9": {
      "L": "And going out, he followed; and he did not know that what was happening through the angel was real, but thought he was seeing a vision.",
      "M": "Peter followed him out of the prison, but he had no idea that what the angel was doing was really happening; he thought he was seeing a vision.",
      "T": "Peter followed him outside, though he had no idea any of this was actually happening. He thought he was dreaming."
    },
    "10": {
      "L": "Having passed through the first guard and the second, they came to the iron gate that leads into the city; which opened of its own accord to them. And going out, they went down one street, and immediately the angel departed from him.",
      "M": "They passed the first and second guards and came to the iron gate leading to the city. It opened for them by itself, and they went through it. When they had walked the length of one street, the angel suddenly left him.",
      "T": "They moved past the first guard post, then the second, and came to the great iron gate that opened into the city. It swung open on its own. They walked through and went one block down the street. Then the angel was simply gone."
    },
    "11": {
      "L": "And Peter, coming to himself, said, 'Now I know truly that the Lord sent his angel and delivered me from the hand of Herod and from all that the Jewish people expected.'",
      "M": "Then Peter came to himself and said, 'Now I know without a doubt that the Lord has sent his angel and rescued me from Herod's clutches and from everything the Jewish people were hoping would happen.'",
      "T": "Then Peter's head cleared, and he understood. 'Now I know for certain it's real,' he said. 'The Lord sent his angel and rescued me from Herod's grip—from everything the people were hoping would happen to me.'"
    },
    "12": {
      "L": "And having understood this, he came to the house of Mary the mother of John who was also called Mark, where quite a few were gathered together and were praying.",
      "M": "When this had dawned on him, he went to the house of Mary the mother of John, also known as Mark, where many people had gathered and were praying.",
      "T": "He went straight to the house of Mary, the mother of John who went by the name Mark. A large group had gathered there and were deep in prayer."
    },
    "13": {
      "L": "And when he knocked at the door of the gate, a servant girl named Rhoda came to respond.",
      "M": "Peter knocked at the outer entrance, and a servant named Rhoda came to answer the door.",
      "T": "He knocked at the gate, and a servant girl named Rhoda came to answer."
    },
    "14": {
      "L": "And recognising the voice of Peter, from joy she did not open the gate, but running in, she reported that Peter was standing before the gate.",
      "M": "When she recognized Peter's voice, she was so overjoyed she ran back without opening it and exclaimed, 'Peter is at the door!'",
      "T": "When she recognized Peter's voice, she was so overjoyed that instead of opening the gate she ran back inside to announce it: 'Peter is standing at the gate!'"
    },
    "15": {
      "L": "And they said to her, 'You are out of your mind.' But she kept insisting it was so. And they said, 'It is his angel.'",
      "M": "'You're out of your mind,' they told her. When she kept insisting that it was so, they said, 'It must be his angel.'",
      "T": "'You're out of your mind,' they told her. She kept insisting it was true. 'Then it must be his guardian angel,' they said."
    },
    "16": {
      "L": "But Peter continued knocking; and having opened, they saw him and were amazed.",
      "M": "But Peter kept on knocking, and when they opened the door and saw him, they were astonished.",
      "T": "But Peter was still out there knocking. When they finally opened the gate and saw him with their own eyes, they were stunned."
    },
    "17": {
      "L": "But beckoning to them with his hand to be silent, he told them how the Lord had brought him out of the prison. And he said, 'Report these things to James and to the brothers.' And departing, he went to another place.",
      "M": "Peter motioned with his hand for them to be quiet and described how the Lord had brought him out of prison. 'Tell James and the other brothers and sisters about this,' he said, and then he left for another place.",
      "T": "Peter raised his hand to silence them, then described exactly how the Lord had brought him out of prison. 'Tell James and the rest of the brothers about this,' he said. Then he slipped away to another location."
    },
    "18": {
      "L": "Now when day came there was no small stir among the soldiers as to what had become of Peter.",
      "M": "In the morning, there was no small commotion among the soldiers as to what had become of Peter.",
      "T": "At dawn, the prison was in complete uproar. The guards had no idea what had happened to Peter."
    },
    "19": {
      "L": "And when Herod had searched for him and did not find him, he examined the guards and commanded that they be led away. And going down from Judaea to Caesarea, he spent time there.",
      "M": "After Herod had a thorough search made for him and did not find him, he cross-examined the guards and ordered that they be executed. Then Herod went from Judea down to Caesarea and stayed there.",
      "T": "Herod launched a full investigation, found nothing, cross-examined the guards, and ordered their execution. Then he left Judea and went down to Caesarea, where he remained."
    },
    "20": {
      "L": "Now Herod was bitterly hostile toward the people of Tyre and Sidon. And with one accord they came before him, and having won over Blastus the king's chamberlain, they asked for peace, because their region was nourished by the king's country.",
      "M": "He had been quarrelling bitterly with the people of Tyre and Sidon; they now joined together and sought an audience with him. After securing the support of Blastus, a trusted personal servant of the king, they asked for peace, because they depended on the king's territory for their food supply.",
      "T": "Herod had been in a heated dispute with the cities of Tyre and Sidon. Their representatives came to him as a united delegation. They won over Blastus, the king's personal chamberlain, and through him negotiated for peace—they needed it, since their region depended on Herod's territory for food."
    },
    "21": {
      "L": "And on an appointed day, Herod, having put on royal robes, sat upon the throne and made an oration to them.",
      "M": "On the appointed day Herod, wearing his royal robes, sat on his throne and delivered a public address to the people.",
      "T": "On the appointed day, Herod dressed himself in his royal robes, took his seat on the throne, and delivered a formal speech to the crowd."
    },
    "22": {
      "L": "And the people kept calling out, 'The voice of a god, and not of a man!'",
      "M": "The people shouted, 'This is the voice of a god, not of a mortal man!'",
      "T": "The crowd kept shouting, 'The voice of a god, not a man!'"
    },
    "23": {
      "L": "And immediately an angel of the Lord struck him, because he did not give the glory to God; and being eaten by worms, he died.",
      "M": "Immediately, because Herod did not give praise to God, an angel of the Lord struck him down, and he was eaten by worms and died.",
      "T": "At that moment, an angel of the Lord struck him down—because he accepted the glory that belonged to God alone. He was consumed by worms and died."
    },
    "24": {
      "L": "But the word of God grew and multiplied.",
      "M": "But the word of God continued to spread and flourish.",
      "T": "Meanwhile, God's word kept spreading and taking hold everywhere."
    },
    "25": {
      "L": "And Barnabas and Saul returned to Jerusalem, having completed the ministry, taking with them also John who was called Mark.",
      "M": "When Barnabas and Saul had finished their mission, they returned from Jerusalem, taking with them John, also known as Mark.",
      "T": "Barnabas and Saul completed their mission and returned from Jerusalem, bringing with them John, who went by the name Mark."
    }
  },

  # ── CHAPTER 13 ─────────────────────────────────────────────────────────────
  "13": {
    "1": {
      "L": "Now there were in the assembly that was in Antioch certain prophets and teachers: Barnabas and Simeon who was called Niger and Lucius of Cyrene and Manaen who had been brought up with Herod the tetrarch and Saul.",
      "M": "Now in the church at Antioch there were prophets and teachers: Barnabas, Simeon called Niger, Lucius of Cyrene, Manaen (who had been brought up with Herod the tetrarch) and Saul.",
      "T": "The community at Antioch had a remarkable group of prophets and teachers: Barnabas, Simeon who was called Niger, Lucius from Cyrene, Manaen who had grown up alongside Herod the tetrarch, and Saul."
    },
    "2": {
      "L": "While they were ministering to the Lord and fasting, the Holy Spirit said, 'Set apart for me Barnabas and Saul for the work to which I have called them.'",
      "M": "While they were worshipping the Lord and fasting, the Holy Spirit said, 'Set apart for me Barnabas and Saul for the work to which I have called them.'",
      "T": "While they were worshipping the Lord and fasting, the Holy Spirit spoke: 'Commission Barnabas and Saul for the work I have called them to do.'"
    },
    "3": {
      "L": "Then, having fasted and prayed and laid hands on them, they sent them away.",
      "M": "So after they had fasted and prayed, they placed their hands on them and sent them off.",
      "T": "They fasted and prayed, laid their hands on Barnabas and Saul, and sent them on their way."
    },
    "4": {
      "L": "So they, being sent out by the Holy Spirit, went down to Seleucia; and from there they sailed to Cyprus.",
      "M": "The two of them, sent on their way by the Holy Spirit, went down to Seleucia and sailed from there to Cyprus.",
      "T": "Commissioned by the Holy Spirit, they made their way down to Seleucia and from there sailed across to Cyprus."
    },
    "5": {
      "L": "And having come to Salamis, they proclaimed the word of God in the synagogues of the Jews. And they had also John as a helper.",
      "M": "When they arrived at Salamis, they proclaimed the word of God in the Jewish synagogues. John was with them as their helper.",
      "T": "On arriving at Salamis, they began proclaiming God's word in the synagogues. John was with them, assisting in the work."
    },
    "6": {
      "L": "And having gone through the whole island as far as Paphos, they found a certain man—a sorcerer and false prophet, a Jew whose name was Bar-Jesus—",
      "M": "They travelled through the whole island until they came to Paphos. There they met a Jewish sorcerer and false prophet named Bar-Jesus,",
      "T": "They made their way across the whole island to Paphos, where they encountered a Jewish man—a sorcerer and self-styled prophet named Bar-Jesus—"
    },
    "7": {
      "L": "who was with the proconsul Sergius Paulus, an intelligent man. This man, having called for Barnabas and Saul, sought to hear the word of God.",
      "M": "who was an attendant of the proconsul, Sergius Paulus. The proconsul, an intelligent man, sent for Barnabas and Saul because he wanted to hear the word of God.",
      "T": "who had attached himself to the proconsul, Sergius Paulus—a man of real intelligence. Sergius Paulus sent for Barnabas and Saul; he was eager to hear God's word."
    },
    "8": {
      "L": "But Elymas the sorcerer—for so his name is translated—withstood them, seeking to turn the proconsul away from the faith.",
      "M": "But Elymas the sorcerer (for that is what his name means in translation) opposed them and tried to turn the proconsul from the faith.",
      "T": "Elymas—that's what his name means in translation—vigorously opposed them, working to keep the proconsul from coming to faith."
    },
    "9": {
      "L": "But Saul, who is also called Paul, filled with the Holy Spirit, looked intently at him",
      "M": "Then Saul, who was also called Paul, filled with the Holy Spirit, looked straight at Elymas",
      "T": "Saul—who also goes by Paul—filled with the Holy Spirit, fixed his gaze on Elymas"
    },
    "10": {
      "L": "and said, 'O full of all deceit and all wickedness, son of the devil, enemy of all righteousness—will you not stop making crooked the straight paths of the Lord?'",
      "M": "and said, 'You are a child of the devil and an enemy of everything that is right! You are full of all kinds of deceit and trickery. Will you never stop perverting the right ways of the Lord?'",
      "T": "'You child of the devil,' Paul said, 'you enemy of everything right and true—packed full of deception and corruption. Will you never stop twisting the Lord's straight paths into crooked ones?'"
    },
    "11": {
      "L": "'And now, behold, the hand of the Lord is upon you, and you will be blind, not seeing the sun for a time.' Immediately a mist and darkness fell upon him, and going about he sought people to lead him by the hand.",
      "M": "'Now the hand of the Lord is against you. You are going to be blind for a time, not even able to see the light of the sun.' Immediately mist and darkness came over him, and he groped about, seeking someone to lead him by the hand.",
      "T": "'And right now the Lord's hand is against you. You are going to go blind—you won't see the sun for a season.' A dark fog instantly came over him, and he stumbled around trying to find someone to guide him."
    },
    "12": {
      "L": "Then the proconsul, having seen what had happened, believed, being astonished at the teaching of the Lord.",
      "M": "When the proconsul saw what had happened, he believed, for he was amazed at the teaching about the Lord.",
      "T": "When the proconsul saw what had happened, he believed—he was simply astonished at the message about the Lord."
    },
    "13": {
      "L": "Now having set sail from Paphos, Paul and his company came to Perga of Pamphylia; and John departed from them and returned to Jerusalem.",
      "M": "From Paphos, Paul and his companions sailed to Perga in Pamphylia, where John left them to return to Jerusalem.",
      "T": "Paul and his companions sailed from Paphos and came to Perga in Pamphylia. It was there that John left them and returned to Jerusalem."
    },
    "14": {
      "L": "But they, passing through from Perga, came to Antioch of Pisidia, and having entered the synagogue on the day of the sabbath, they sat down.",
      "M": "From Perga they went on to Pisidian Antioch. On the Sabbath they entered the synagogue and sat down.",
      "T": "Travelling on from Perga, they arrived in Pisidian Antioch. On the Sabbath they went into the synagogue and took seats."
    },
    "15": {
      "L": "And after the reading of the Law and the Prophets, the rulers of the synagogue sent to them, saying, 'Brothers, if you have any word of exhortation for the people, speak.'",
      "M": "After the reading from the Law and the Prophets, the leaders of the synagogue sent word to them: 'Brothers, if you have a word of encouragement for the people, please speak.'",
      "T": "After the readings from the Law and the Prophets, the synagogue officials sent a message to them: 'Friends, if any of you has a word of encouragement for the people, please go ahead.'"
    },
    "16": {
      "L": "And Paul, standing up and motioning with his hand, said: 'Men of Israel and you who fear God, listen!'",
      "M": "Standing up, Paul motioned with his hand and said: 'Fellow Israelites and you Gentiles who worship God, listen to me!'",
      "T": "Paul stood up, raised his hand for attention, and spoke: 'People of Israel and all who worship the God of Israel—listen up!'"
    },
    "17": {
      "L": "'The God of this people Israel chose our fathers, and exalted the people when they were sojourners in the land of Egypt, and with an uplifted arm he led them out of it.'",
      "M": "'The God of the people of Israel chose our ancestors; he made the people prosper during their stay in Egypt; with mighty power he led them out of that country;'",
      "T": "'The God of Israel chose our ancestors. He made them flourish while they were strangers in Egypt, and then with an outstretched arm he brought them out.'"
    },
    "18": {
      "L": "'And for a time of about forty years he endured their ways in the wilderness.'",
      "M": "'for about forty years he endured their conduct in the wilderness;'",
      "T": "'He put up with their behaviour in the desert for roughly forty years.'"
    },
    "19": {
      "L": "'And having destroyed seven nations in the land of Canaan, he gave them their land as an inheritance'",
      "M": "'and he overthrew seven nations in Canaan, giving their land to his people as their inheritance.'",
      "T": "'He destroyed seven nations in Canaan and gave the land to his people as their rightful inheritance.'"
    },
    "20": {
      "L": "'—for about four hundred and fifty years. And after these things he gave them judges until Samuel the prophet.'",
      "M": "'All this took about 450 years. After this, God gave them judges until the time of Samuel the prophet.'",
      "T": "'This all took some four hundred and fifty years. After that he gave them judges to lead them, right up until Samuel the prophet.'"
    },
    "21": {
      "L": "'And then they asked for a king, and God gave them Saul son of Kish, a man of the tribe of Benjamin, for forty years.'",
      "M": "'Then the people asked for a king, and he gave them Saul son of Kish, of the tribe of Benjamin, who ruled for forty years.'",
      "T": "'Then the people demanded a king, and God gave them Saul son of Kish, of the tribe of Benjamin—who reigned for forty years.'"
    },
    "22": {
      "L": "'And having removed him, he raised up David for them as king, to whom also he gave testimony, saying: \"I have found David the son of Jesse, a man after my own heart, who will carry out all my will.\"'",
      "M": "'After removing Saul, he made David their king. God testified concerning him: \"I have found David son of Jesse, a man after my own heart; he will do everything I want him to do.\"'",
      "T": "'After removing Saul, he raised up David as their king—and gave him this commendation: \"I have found in David son of Jesse a man who is truly after my own heart; he will carry out everything I want.\"'"
    },
    "23": {
      "L": "'From this man's seed, according to promise, God has brought to Israel a Saviour, Jesus,'",
      "M": "'From the descendants of this man God has brought to Israel the Saviour Jesus, as he promised.'",
      "T": "'From David's descendants, just as God promised, he has brought to Israel a Saviour—Jesus.'"
    },
    "24": {
      "L": "'after John had proclaimed beforehand a baptism of repentance to all the people of Israel before his coming.'",
      "M": "'Before the coming of Jesus, John preached repentance and baptism to all the people of Israel.'",
      "T": "'Before Jesus came, John had already been calling all Israel to turn back to God and be baptized.'"
    },
    "25": {
      "L": "'And as John was completing his course, he said: \"What do you suppose I am? I am not he. But behold, there comes one after me, the sandals of whose feet I am not worthy to untie.\"'",
      "M": "'As John was completing his work, he said: \"Who do you think I am? I am not the one you are looking for. But after me comes one whose sandals I am not worthy to untie.\"'",
      "T": "'As John was finishing his work, he kept saying: \"Do you think I am the one? I am not. But someone is coming after me whose sandals I am not fit to unfasten.\"'"
    },
    "26": {
      "L": "'Brothers, sons of the family of Abraham, and those among you who fear God, to us the word of this salvation has been sent.'",
      "M": "'Fellow children of Abraham and you God-fearing Gentiles, it is to us that this message of salvation has been sent.'",
      "T": "'Friends—children of Abraham's family and all who fear God here—this message of rescue has been sent to us.'"
    },
    "27": {
      "L": "'For those dwelling in Jerusalem and their rulers, not having known him nor the utterances of the prophets that are read every sabbath, fulfilled them by condemning him.'",
      "M": "'The people of Jerusalem and their rulers did not recognise Jesus, yet in condemning him they fulfilled the words of the prophets that are read every Sabbath.'",
      "T": "'The people of Jerusalem and their leaders did not recognise who Jesus was. And yet—by condemning him—they fulfilled the very words of the prophets that are read aloud every Sabbath.'"
    },
    "28": {
      "L": "'And though they found no cause for death, they asked Pilate to have him executed.'",
      "M": "'Though they found no proper grounds for a death sentence, they asked Pilate to have him executed.'",
      "T": "'They found no legitimate grounds to condemn him to death, yet they demanded that Pilate have him executed.'"
    },
    "29": {
      "L": "'And when they had fulfilled all the things written about him, taking him down from the tree, they laid him in a tomb.'",
      "M": "'When they had carried out all that was written about him, they took him down from the cross and laid him in a tomb.'",
      "T": "'When they had done everything that was written about him, they took his body down from the cross and placed it in a tomb.'"
    },
    "30": {
      "L": "'But God raised him from the dead.'",
      "M": "'But God raised him from the dead.'",
      "T": "'But God raised him from the dead.'"
    },
    "31": {
      "L": "'And for many days he appeared to those who had come up with him from Galilee to Jerusalem—who are now his witnesses to the people.'",
      "M": "'For many days he was seen by those who had travelled with him from Galilee to Jerusalem. They are now his witnesses to our people.'",
      "T": "'For many days he appeared to those who had been his companions on the journey from Galilee to Jerusalem. They are now standing as witnesses to our people.'"
    },
    "32": {
      "L": "'And we bring you good news—the promise made to the fathers,'",
      "M": "'We tell you the good news: what God promised our ancestors'",
      "T": "'We are here with good news—the promise God made to our ancestors'"
    },
    "33": {
      "L": "'that God has fulfilled this to us their children, in that he raised Jesus; as also it is written in the second Psalm: \"You are my Son; today I have begotten you.\"'",
      "M": "'he has fulfilled for us, their children, by raising up Jesus. As it is written in the second Psalm: \"You are my son; today I have become your father.\"'",
      "T": "'—God has fulfilled for us their descendants by raising Jesus from the dead. As the second Psalm says: \"You are my Son; today I have given you birth.\"'"
    },
    "34": {
      "L": "'And that he raised him from the dead, no more to return to corruption, he has spoken thus: \"I will give you the holy and faithful mercies of David.\"'",
      "M": "'God raised him from the dead so that he will never be subject to decay. As God has said, \"I will give you the holy and sure blessings promised to David.\"'",
      "T": "'That God raised him never to return to decay—God has said it plainly: \"I will give you the sacred and trustworthy promises I made to David.\"'"
    },
    "35": {
      "L": "'Therefore also in another place he says: \"You will not allow your Holy One to see corruption.\"'",
      "M": "'So it is stated elsewhere: \"You will not let your holy one see decay.\"'",
      "T": "'And another psalm says it directly: \"You will not allow your Faithful One to see the grave\'s corruption.\"'"
    },
    "36": {
      "L": "'For David, having served in his own generation by the will of God, fell asleep and was laid with his fathers and saw corruption;'",
      "M": "'Now when David had served God's purpose in his own generation, he fell asleep; he was buried with his ancestors and his body decayed.'",
      "T": "'David served God's purpose in his own generation, then fell asleep, was buried alongside his ancestors, and his body did decay.'"
    },
    "37": {
      "L": "'but he whom God raised did not see corruption.'",
      "M": "'But the one whom God raised from the dead did not see decay.'",
      "T": "'But the one God raised—he never saw corruption.'"
    },
    "38": {
      "L": "'Therefore let it be known to you, brothers, that through this man forgiveness of sins is proclaimed to you;'",
      "M": "'Therefore, my friends, I want you to know that through Jesus the forgiveness of sins is proclaimed to you.'",
      "T": "'So here is what I want you to know, my friends: through Jesus, forgiveness of sins is being announced to you.'"
    },
    "39": {
      "L": "'and in him everyone who believes is justified from all things from which you could not be justified through the law of Moses.'",
      "M": "'Through him everyone who believes is set free from every sin, a justification you were never able to obtain through the law of Moses.'",
      "T": "'Through him, everyone who trusts in him is put right with God in ways the law of Moses could never accomplish.'"
    },
    "40": {
      "L": "'Watch therefore, so that what is spoken in the prophets does not come upon you:'",
      "M": "'Take care that what the prophets have said does not happen to you:'",
      "T": "'Be careful, then, that what the prophets warned about does not land on you:'"
    },
    "41": {
      "L": "'\"Behold, you scoffers, and wonder and perish; for I am doing a work in your days, a work you will by no means believe, even if someone were to tell it to you.\"'",
      "M": "'\"Look, you scoffers, wonder and perish! For I am going to do something in your days that you would never believe, even if someone told you.\"'",
      "T": "'\"Look at this, you who sneer and mock—and then be swept away. I am doing something in your own time that you would never believe, no matter who told you.\"'"
    },
    "42": {
      "L": "And as they were going out, they kept urging that these words be spoken to them on the following sabbath.",
      "M": "As Paul and Barnabas were leaving the synagogue, the people invited them to speak further about these things on the next Sabbath.",
      "T": "As Paul and Barnabas were leaving, the people pressed them to come back the following Sabbath and say more."
    },
    "43": {
      "L": "And when the synagogue meeting had been dismissed, many of the Jews and devout proselytes followed Paul and Barnabas, who, speaking to them, were persuading them to continue in the grace of God.",
      "M": "When the congregation was dismissed, many of the Jews and devout converts to Judaism followed Paul and Barnabas, who talked with them and urged them to continue in the grace of God.",
      "T": "After the gathering broke up, many Jews and devout converts followed Paul and Barnabas. The two of them spent time with them, encouraging them to hold on to the grace of God."
    },
    "44": {
      "L": "On the following sabbath almost all the city gathered to hear the word of the Lord.",
      "M": "On the next Sabbath almost the whole city gathered to hear the word of the Lord.",
      "T": "The following Sabbath nearly the entire city turned out to hear the word of the Lord."
    },
    "45": {
      "L": "But when the Jews saw the crowds, they were filled with jealousy and contradicted the things spoken by Paul, and were blaspheming.",
      "M": "When the Jewish leaders saw the crowds, they were filled with jealousy. They began to contradict what Paul was saying and heaped abuse on him.",
      "T": "When the Jewish leaders saw the crowds, they burned with jealousy. They began arguing against everything Paul said, hurling insults at him."
    },
    "46": {
      "L": "And Paul and Barnabas, speaking boldly, said, 'It was necessary for the word of God to be spoken first to you. Since you thrust it aside and judge yourselves unworthy of eternal life, behold, we turn to the Gentiles.'",
      "M": "Then Paul and Barnabas answered them boldly: 'We had to speak the word of God to you first. Since you reject it and do not consider yourselves worthy of eternal life, we now turn to the Gentiles.'",
      "T": "Paul and Barnabas gave them a direct answer: 'God's word had to be spoken to you first. But since you push it away and make yourselves judges that you are unworthy of eternal life—we are turning to the Gentiles.'"
    },
    "47": {
      "L": "'For so the Lord has commanded us: \"I have set you as a light for the Gentiles, that you should be for salvation to the ends of the earth.\"'",
      "M": "'For this is what the Lord has commanded us: \"I have made you a light for the Gentiles, that you may bring salvation to the ends of the earth.\"'",
      "T": "'Because that is what the Lord commissioned us to do: \"I have made you a light for the nations, so that you will bring rescue to the very ends of the earth.\"'"
    },
    "48": {
      "L": "And when the Gentiles heard this, they began rejoicing and glorifying the word of the Lord, and as many as had been appointed to eternal life believed.",
      "M": "When the Gentiles heard this, they were glad and honoured the word of the Lord; and all who were appointed for eternal life believed.",
      "T": "The Gentiles were overjoyed when they heard this. They celebrated and gave honour to the Lord's word. And everyone who had been set apart for eternal life came to faith."
    },
    "49": {
      "L": "And the word of the Lord was spreading through all the region.",
      "M": "The word of the Lord spread through the whole region.",
      "T": "God's word spread across the entire region."
    },
    "50": {
      "L": "But the Jews stirred up the devout women of high standing and the prominent men of the city, and raised up persecution against Paul and Barnabas, and expelled them from their borders.",
      "M": "But the Jewish leaders incited the God-fearing women of high standing and the leading men of the city. They stirred up persecution against Paul and Barnabas, and expelled them from their region.",
      "T": "But the Jewish leaders stirred up prominent women who were devout and the leading men of the city. They whipped up a persecution against Paul and Barnabas and drove them out of the area."
    },
    "51": {
      "L": "But they shook off the dust of their feet against them and went to Iconium.",
      "M": "So they shook the dust off their feet as a warning to them and went to Iconium.",
      "T": "Paul and Barnabas shook the dust from their feet in protest and moved on to Iconium."
    },
    "52": {
      "L": "And the disciples were filled with joy and with the Holy Spirit.",
      "M": "And the disciples were filled with joy and with the Holy Spirit.",
      "T": "And the believers they left behind were filled with joy and with the Holy Spirit."
    }
  },

  # ── CHAPTER 14 ─────────────────────────────────────────────────────────────
  "14": {
    "1": {
      "L": "Now it came about at Iconium that they entered together into the synagogue of the Jews, and spoke in such a way that a great multitude both of Jews and of Greeks believed.",
      "M": "At Iconium Paul and Barnabas went as usual into the Jewish synagogue. There they spoke so effectively that a great number of Jews and Greeks believed.",
      "T": "At Iconium, Paul and Barnabas entered the Jewish synagogue as they had done before. Their speaking was so compelling that a great number of both Jews and Greeks came to faith."
    },
    "2": {
      "L": "But the unbelieving Jews stirred up and embittered the souls of the Gentiles against the brothers.",
      "M": "But the Jewish leaders who refused to believe stirred up the other Gentiles and poisoned their minds against the brothers.",
      "T": "But those among the Jews who refused to believe worked to inflame the Gentiles' minds against the believers."
    },
    "3": {
      "L": "Therefore they remained for a considerable time, speaking boldly in the Lord, who was bearing witness to the word of his grace, granting signs and wonders to be done by their hands.",
      "M": "So Paul and Barnabas spent considerable time there, speaking boldly for the Lord, who confirmed the message of his grace by enabling them to perform signs and wonders.",
      "T": "Paul and Barnabas stayed on there for a long time, speaking openly and fearlessly for the Lord. He confirmed the message of his grace by giving them the power to perform signs and wonders."
    },
    "4": {
      "L": "But the multitude of the city was divided: some were with the Jews, and some with the apostles.",
      "M": "The people of the city were divided; some sided with the Jews, others with the apostles.",
      "T": "The city was split. Some took the side of the Jewish leaders; others were with the apostles."
    },
    "5": {
      "L": "Now when an attempt was made by both the Gentiles and the Jews with their rulers to mistreat and stone them,",
      "M": "There was a plot afoot among the Gentiles and Jews, together with their leaders, to ill-treat and stone them.",
      "T": "When a plan was forming among the Gentiles and Jews together—with the approval of their leaders—to assault and stone them,"
    },
    "6": {
      "L": "they became aware of it and fled to the cities of Lycaonia, Lystra and Derbe, and the surrounding region,",
      "M": "Paul and Barnabas found out about it and fled to the Lycaonian cities of Lystra and Derbe and to the surrounding country,",
      "T": "they learned of it and escaped to the Lycaonian cities of Lystra and Derbe and the surrounding countryside."
    },
    "7": {
      "L": "and there they were proclaiming the good news.",
      "M": "where they continued to preach the gospel.",
      "T": "There they kept right on announcing the good news."
    },
    "8": {
      "L": "And at Lystra a certain man was sitting who had no strength in his feet, lame from birth, who had never walked.",
      "M": "In Lystra there sat a man who was lame. He had been that way from birth and had never walked.",
      "T": "In Lystra there was a man who had been unable to walk since birth—he had never taken a single step."
    },
    "9": {
      "L": "This man heard Paul speaking. And Paul, having looked intently at him and having seen that he had faith to be healed,",
      "M": "He listened to Paul as he was speaking. Paul looked directly at him, saw that he had faith to be healed",
      "T": "This man was listening to Paul. Paul looked at him closely and saw that he had the faith needed to be healed."
    },
    "10": {
      "L": "said in a loud voice, 'Stand upright on your feet.' And he sprang up and began to walk.",
      "M": "and called out, 'Stand up on your feet!' At that, the man jumped up and began to walk.",
      "T": "He called out with a clear voice, 'Stand up on your feet!' The man leaped up and started walking."
    },
    "11": {
      "L": "And the crowds, having seen what Paul had done, lifted up their voices, saying in the Lycaonian language, 'The gods have come down to us in the likeness of men!'",
      "M": "When the crowd saw what Paul had done, they shouted in the Lycaonian language, 'The gods have come down to us in human form!'",
      "T": "The crowds saw what Paul had done and began shouting in the Lycaonian language, 'The gods have taken human form and come down to us!'"
    },
    "12": {
      "L": "And they were calling Barnabas Zeus, and Paul Hermes, since he was the one leading in speaking.",
      "M": "Barnabas they called Zeus, and Paul they called Hermes because he was the chief speaker.",
      "T": "They called Barnabas Zeus and Paul Hermes, since Paul was the one doing most of the talking."
    },
    "13": {
      "L": "And the priest of Zeus, whose temple was before the city, bringing oxen and garlands to the gates, wished to offer sacrifice with the crowds.",
      "M": "The priest of Zeus, whose temple was just outside the city, brought bulls and wreaths to the city gates because he and the crowd wanted to offer sacrifices to them.",
      "T": "The priest of the Zeus temple located just outside the city brought bulls and flower wreaths to the city gates, intending to make sacrifices along with the crowds."
    },
    "14": {
      "L": "But when the apostles Barnabas and Paul heard this, tearing their clothes, they rushed out into the crowd, crying out",
      "M": "But when the apostles Barnabas and Paul heard of this, they tore their clothes and rushed out into the crowd, shouting:",
      "T": "When Barnabas and Paul understood what was happening, they tore their clothes and rushed into the crowd, shouting:"
    },
    "15": {
      "L": "and saying, 'Men, why are you doing these things? We also are human beings of the same nature as you, proclaiming to you good news to turn from these worthless things to the living God, who made the heaven and the earth and the sea and all that is in them.'",
      "M": "'Friends, why are you doing this? We too are only human, just like you. We are bringing you good news, telling you to turn from these worthless things to the living God, who made the heavens and the earth and the sea and everything in them.'",
      "T": "'Friends, what are you doing? We are just people—human beings like you! We're here to bring you good news: turn away from these empty things to the living God, the one who made heaven and earth and sea and everything in them.'"
    },
    "16": {
      "L": "'In past generations he allowed all the nations to walk in their own ways.'",
      "M": "'In the past, he let all nations go their own way.'",
      "T": "'In generations past, he allowed all the nations to go their own way.'"
    },
    "17": {
      "L": "'Yet he did not leave himself without witness, doing good and giving you rains from heaven and fruitful seasons, filling your hearts with food and gladness.'",
      "M": "'Yet he has not left himself without testimony: he has shown kindness by giving you rain from heaven and crops in their seasons; he provides you with plenty of food and fills your hearts with joy.'",
      "T": "'And yet he was never without witnesses—he showed his goodness by sending rain from heaven and crops in season, filling your lives with food and your hearts with happiness.'"
    },
    "18": {
      "L": "And saying these things, they could scarcely restrain the crowds from sacrificing to them.",
      "M": "Even with these words, they had difficulty keeping the crowd from sacrificing to them.",
      "T": "Even with these words they could barely stop the crowd from offering sacrifices to them."
    },
    "19": {
      "L": "But Jews came from Antioch and Iconium, and having won over the crowds, they stoned Paul and dragged him outside the city, supposing that he was dead.",
      "M": "Then some Jews came from Antioch and Iconium and won the crowd over. They stoned Paul and dragged him outside the city, thinking he was dead.",
      "T": "Then Jews arrived from Antioch and Iconium. They turned the crowd against Paul, stoned him, and dragged his body outside the city, leaving him for dead."
    },
    "20": {
      "L": "But when the disciples had gathered around him, he rose up and entered into the city. And on the following day he went out with Barnabas to Derbe.",
      "M": "But after the disciples had gathered around him, he got up and went back into the city. The next day he and Barnabas left for Derbe.",
      "T": "But the disciples formed a circle around him, and Paul got up and walked back into the city. The next day he left for Derbe with Barnabas."
    },
    "21": {
      "L": "And having proclaimed the good news to that city and having made quite a few disciples, they returned to Lystra and to Iconium and to Antioch,",
      "M": "They preached the gospel in that city and won a large number of disciples. Then they returned to Lystra, Iconium and Antioch,",
      "T": "They announced the good news in Derbe and made many disciples. Then they turned back—through Lystra, Iconium, and Antioch—"
    },
    "22": {
      "L": "strengthening the souls of the disciples, exhorting them to continue in the faith and saying that through many tribulations we must enter the kingdom of God.",
      "M": "strengthening the disciples and encouraging them to remain true to the faith. 'We must go through many hardships to enter the kingdom of God,' they said.",
      "T": "strengthening the believers, encouraging them to remain firm in the faith. 'The path into God's kingdom runs through many hardships,' they told them."
    },
    "23": {
      "L": "And having appointed elders for them in each assembly, having prayed with fasting, they commended them to the Lord in whom they had believed.",
      "M": "Paul and Barnabas appointed elders for them in each church and, with prayer and fasting, committed them to the Lord, in whom they had put their trust.",
      "T": "They appointed elders in each community, and with prayer and fasting entrusted these believers to the Lord in whom they had placed their faith."
    },
    "24": {
      "L": "And having passed through Pisidia, they came to Pamphylia.",
      "M": "After going through Pisidia, they came into Pamphylia.",
      "T": "Travelling through Pisidia, they arrived in Pamphylia."
    },
    "25": {
      "L": "And having spoken the word in Perga, they went down to Attalia.",
      "M": "When they had preached the word in Perga, they went down to Attalia.",
      "T": "After proclaiming God's word in Perga, they made their way down to Attalia."
    },
    "26": {
      "L": "And from there they sailed to Antioch, from which they had been commended to the grace of God for the work which they had completed.",
      "M": "From Attalia they sailed back to Antioch, where they had been committed to the grace of God for the work they had now completed.",
      "T": "From Attalia they sailed back to Antioch—the very place where they had been sent off into the grace of God for the work they had now finished."
    },
    "27": {
      "L": "And having arrived and having gathered the assembly together, they reported as many things as God had done with them and that he had opened a door of faith to the Gentiles.",
      "M": "On arriving there, they gathered the church together and reported all that God had done through them and how he had opened a door of faith to the Gentiles.",
      "T": "When they arrived, they gathered the whole community and told them everything God had accomplished through them—and how he had opened the door of faith wide to the Gentiles."
    },
    "28": {
      "L": "And they remained there no little time with the disciples.",
      "M": "And they stayed there a long time with the disciples.",
      "T": "They settled in there with the disciples for a considerable time."
    }
  },

  # ── CHAPTER 15 ─────────────────────────────────────────────────────────────
  "15": {
    "1": {
      "L": "And some men came down from Judaea and were teaching the brothers: 'Unless you are circumcised according to the custom of Moses, you cannot be saved.'",
      "M": "Certain people came down from Judea to Antioch and were teaching the believers: 'Unless you are circumcised, according to the custom taught by Moses, you cannot be saved.'",
      "T": "Some men came down from Judea to Antioch and began teaching the believers: 'You cannot be saved unless you are circumcised in accordance with the custom Moses gave us.'"
    },
    "2": {
      "L": "And there being no small dissension and dispute with them from Paul and Barnabas, they arranged that Paul and Barnabas and certain others of them should go up to Jerusalem to the apostles and elders regarding this question.",
      "M": "This brought Paul and Barnabas into sharp dispute and debate with them. So the church decided that Paul and Barnabas and some other believers should go up to Jerusalem and consult the apostles and elders about this question.",
      "T": "This set off a fierce dispute between them and Paul and Barnabas. The community decided to send Paul and Barnabas, along with some others, up to Jerusalem to lay the question before the apostles and elders."
    },
    "3": {
      "L": "So, being sent on their way by the assembly, they were passing through both Phoenicia and Samaria, narrating the conversion of the Gentiles; and they were bringing great joy to all the brothers.",
      "M": "The church sent them on their way, and as they travelled through Phoenicia and Samaria, they told how the Gentiles had been converted. This news made all the believers very glad.",
      "T": "The community sent them off with a proper farewell. As they travelled through Phoenicia and Samaria, they reported the conversion of the Gentiles everywhere they stopped, and it brought deep joy to all the believers."
    },
    "4": {
      "L": "And having arrived in Jerusalem, they were received by the assembly and the apostles and the elders, and they reported all things that God had done with them.",
      "M": "When they came to Jerusalem, they were welcomed by the church and the apostles and elders, to whom they reported everything God had done through them.",
      "T": "When they arrived in Jerusalem, they were warmly welcomed by the community, the apostles, and the elders. They reported everything God had done through them."
    },
    "5": {
      "L": "But some of the sect of the Pharisees who had believed rose up, saying, 'It is necessary to circumcise them and to command them to keep the law of Moses.'",
      "M": "Then some of the believers who belonged to the party of the Pharisees stood up and said, 'The Gentiles must be circumcised and required to keep the law of Moses.'",
      "T": "But some of the believers who had come from the Pharisees stood up and insisted: 'These Gentile converts must be circumcised and made to observe the whole law of Moses.'"
    },
    "6": {
      "L": "And the apostles and the elders were gathered to consider regarding this matter.",
      "M": "The apostles and elders met to consider this question.",
      "T": "The apostles and elders convened to work through this question."
    },
    "7": {
      "L": "And when much debate had taken place, Peter stood up and said to them, 'Brothers, you know that from early days God chose among you that through my mouth the Gentiles should hear the word of the gospel and believe.'",
      "M": "After much discussion, Peter got up and addressed them: 'Brothers, you know that some time ago God made a choice among you that the Gentiles might hear from my lips the message of the gospel and believe.'",
      "T": "After a long and heated debate, Peter rose to speak. 'Friends,' he said, 'you know that some time ago God chose from among us that through my mouth the Gentiles would hear the message of the good news and come to faith.'"
    },
    "8": {
      "L": "'And God, who knows the heart, bore witness to them, giving them the Holy Spirit just as he also did to us;'",
      "M": "'God, who knows the heart, showed that he accepted them by giving the Holy Spirit to them, just as he did to us.'",
      "T": "'God—who sees into every heart—showed that he accepted them by giving them the Holy Spirit, exactly as he had done for us.'"
    },
    "9": {
      "L": "'and he made no distinction between us and them, having cleansed their hearts by faith.'",
      "M": "'He did not discriminate between us and them, for he purified their hearts by faith.'",
      "T": "'He made no distinction whatsoever between us and them—he cleansed their hearts through faith.'"
    },
    "10": {
      "L": "'Now therefore why do you test God by placing a yoke upon the neck of the disciples which neither our fathers nor we were strong enough to bear?'",
      "M": "'Now then, why do you try to test God by putting on the necks of Gentile believers a yoke that neither we nor our ancestors have been able to bear?'",
      "T": "'So why are you testing God by placing on these new believers a burden that neither our ancestors nor we ourselves have ever been able to carry?'"
    },
    "11": {
      "L": "'But through the grace of the Lord Jesus we believe to be saved, in the same way as those also.'",
      "M": "'No! We believe it is through the grace of our Lord Jesus that we are saved, just as they are.'",
      "T": "'We believe it is through the grace of the Lord Jesus that we are saved—and so are they. The same way, no different.'"
    },
    "12": {
      "L": "And all the multitude fell silent, and they were listening to Barnabas and Paul describing all the signs and wonders that God had done through them among the Gentiles.",
      "M": "The whole assembly became silent as they listened to Barnabas and Paul telling about the signs and wonders God had done among the Gentiles through them.",
      "T": "The whole assembly went silent and listened as Barnabas and Paul described the signs and wonders God had done through them among the Gentiles."
    },
    "13": {
      "L": "And after they became silent, James answered, saying, 'Brothers, listen to me.'",
      "M": "When they finished, James spoke up. 'Brothers,' he said, 'listen to me.'",
      "T": "When they had finished, James spoke. 'Friends,' he said, 'hear me out.'"
    },
    "14": {
      "L": "'Simeon has related how God first visited the Gentiles to take from among them a people for his name.'",
      "M": "'Simon has described to us how God first intervened to choose a people for his name from the Gentiles.'",
      "T": "'Simon has just told us how God first moved among the Gentiles—choosing a people from them to bear his name.'"
    },
    "15": {
      "L": "'And with this the words of the prophets agree, as it is written:'",
      "M": "'The words of the prophets are in agreement with this, as it is written:'",
      "T": "'The words of the prophets line up with exactly this—as it is written:'"
    },
    "16": {
      "L": "'\"After these things I will return and I will rebuild the tent of David that has fallen, and I will rebuild its ruins and I will restore it,\"'",
      "M": "'\"After this I will return and rebuild David's fallen tent. Its ruins I will rebuild, and I will restore it,\"'",
      "T": "'\"When that day comes I will return and will rebuild the fallen tent of David. I will rebuild it from its ruins and restore it—\"'"
    },
    "17": {
      "L": "'\"so that the rest of mankind may seek the Lord, even all the Gentiles upon whom my name has been called, says the Lord who does these things.\"'",
      "M": "'\"so that the rest of mankind may seek the Lord, even all the Gentiles who bear my name, says the Lord, who does these things—\"'",
      "T": "'\"—so that all the rest of humanity may seek the Lord—yes, all the Gentiles who are called by my name. This is the word of the Lord, who does what he said he would do.\"'"
    },
    "18": {
      "L": "'Known from eternity are all his works to the Lord.'",
      "M": "'things known from long ago.'",
      "T": "'All of this has been known to God from the beginning of time.'"
    },
    "19": {
      "L": "'Therefore I judge that we should not trouble those from among the Gentiles who are turning to God,'",
      "M": "'It is my judgement, therefore, that we should not make it difficult for the Gentiles who are turning to God.'",
      "T": "'Therefore my ruling is this: we should not put obstacles in the way of Gentiles who are turning to God.'"
    },
    "20": {
      "L": "'but write to them to abstain from things polluted by idols and from sexual immorality and from what is strangled and from blood.'",
      "M": "'Instead we should write to them, telling them to abstain from food polluted by idols, from sexual immorality, from the meat of strangled animals and from blood.'",
      "T": "'Instead, we should write to them asking them to stay away from food offered to idols, from sexual immorality, from meat of strangled animals, and from blood.'"
    },
    "21": {
      "L": "'For Moses from ancient generations has in every city those who proclaim him, being read in the synagogues every sabbath.'",
      "M": "'For the law of Moses has been preached in every city from the earliest times and is read in the synagogues on every Sabbath.'",
      "T": "'Moses has been proclaimed city by city across many generations—his writings are read aloud in the synagogues every Sabbath.'"
    },
    "22": {
      "L": "Then it seemed good to the apostles and the elders, with the whole assembly, to send chosen men from among themselves to Antioch together with Paul and Barnabas: Judas called Barsabbas and Silas, leading men among the brothers.",
      "M": "Then the apostles and elders, with the whole church, decided to choose some of their own men and send them to Antioch with Paul and Barnabas. They chose Judas (called Barsabbas) and Silas, men who were leaders among the believers.",
      "T": "The apostles and elders, together with the whole community, decided to select men from among themselves and send them to Antioch alongside Paul and Barnabas. They chose Judas Barsabbas and Silas, both respected leaders among the believers."
    },
    "23": {
      "L": "writing by their hands: 'The apostles and the elder brothers to the brothers who are from the Gentiles in Antioch and Syria and Cilicia: greetings.'",
      "M": "With them they sent the following letter: The apostles and elders, your brothers, To the Gentile believers in Antioch, Syria and Cilicia: Greetings.",
      "T": "They carried this letter: 'From the apostles and elders, your brothers—to the Gentile believers in Antioch, Syria, and Cilicia. Greetings.'"
    },
    "24": {
      "L": "'Since we have heard that some who went out from us have troubled you with words, unsettling your souls—to whom we gave no instruction—'",
      "M": "'We have heard that some went out from us without our authorisation and disturbed you, unsettling your minds by what they said.'",
      "T": "'We have heard that some people who left us—without any mandate from us—have unsettled you with their words and thrown your minds into confusion.'"
    },
    "25": {
      "L": "'it seemed good to us, having come together with one accord, to send chosen men to you together with our beloved Barnabas and Paul,'",
      "M": "'So we all agreed to choose some men and send them to you with our dear friends Barnabas and Paul—'",
      "T": "'So we met together as one and decided to send chosen delegates to you, along with our dear friends Barnabas and Paul—'"
    },
    "26": {
      "L": "'men who have given up their lives for the name of our Lord Jesus Christ.'",
      "M": "'men who have risked their lives for the name of our Lord Jesus Christ.'",
      "T": "'men who have put their lives on the line for the name of our Lord Jesus the Messiah.'"
    },
    "27": {
      "L": "'Therefore we have sent Judas and Silas, who will themselves also report the same things by word.'",
      "M": "'Therefore we are sending Judas and Silas to confirm by word of mouth what we are writing.'",
      "T": "'We are sending Judas and Silas to give you this same message in person.'"
    },
    "28": {
      "L": "'For it seemed good to the Holy Spirit and to us to place no greater burden upon you than these necessary things:'",
      "M": "'It seemed good to the Holy Spirit and to us not to burden you with anything beyond the following requirements:'",
      "T": "'The Holy Spirit and all of us are in agreement that no burden should be laid on you beyond these essentials:'"
    },
    "29": {
      "L": "'to abstain from things sacrificed to idols and from blood and from things strangled and from sexual immorality. Keeping yourselves free from these, you will do well. Farewell.'",
      "M": "'You are to abstain from food sacrificed to idols, from blood, from the meat of strangled animals and from sexual immorality. You will do well to avoid these things. Farewell.'",
      "T": "'Stay away from food sacrificed to idols, from blood, from meat of strangled animals, and from sexual immorality. Keep clear of these things and you will be doing well. Goodbye and God's blessing.'"
    },
    "30": {
      "L": "So when they were dismissed, they went down to Antioch; and having gathered the multitude together, they delivered the letter.",
      "M": "So the men were sent off and went down to Antioch, where they gathered the church together and delivered the letter.",
      "T": "The delegates were sent off and went to Antioch, gathered the whole community together, and read the letter aloud."
    },
    "31": {
      "L": "And having read it, they rejoiced over the encouragement.",
      "M": "The people read it and were glad for its encouraging message.",
      "T": "The people were overjoyed at the encouragement it brought."
    },
    "32": {
      "L": "And Judas and Silas, both being prophets themselves, with many words exhorted and strengthened the brothers.",
      "M": "Judas and Silas, who were themselves prophets, said much to encourage and strengthen the believers.",
      "T": "Judas and Silas were prophets as well, and they spent a great deal of time encouraging and strengthening the believers with their words."
    },
    "33": {
      "L": "And having spent time there, they were sent off in peace by the brothers to those who had sent them.",
      "M": "After spending some time there, they were sent off by the believers with the blessing of peace to return to those who had sent them.",
      "T": "After staying there for a while, they were sent back with warm farewells from the believers to those who had commissioned them."
    },
    # v34 — Western text insertion (absent from NA28/best Alexandrian mss); included
    # because the interlinear data file has 41 verses in ch 15.
    "34": {
      "L": "But it seemed good to Silas to remain there.",
      "M": "But Silas decided to remain there.",
      "T": "Silas, however, chose to stay on."
    },
    "35": {
      "L": "And Paul and Barnabas remained in Antioch, teaching and proclaiming the word of the Lord, with many others also.",
      "M": "But Paul and Barnabas remained in Antioch, where they and many others taught and preached the word of the Lord.",
      "T": "Paul and Barnabas also stayed in Antioch, teaching and announcing the Lord's word alongside many others."
    },
    "36": {
      "L": "And after some days Paul said to Barnabas, 'Let us now return and visit the brothers in every city in which we proclaimed the word of the Lord, to see how they are.'",
      "M": "Some time later Paul said to Barnabas, 'Let us go back and visit the believers in all the towns where we preached the word of the Lord and see how they are doing.'",
      "T": "Some time later, Paul said to Barnabas, 'Let's go back and check on the believers in all the towns where we proclaimed the Lord's word—see how they're getting on.'"
    },
    "37": {
      "L": "Now Barnabas was determined to take along John called Mark also.",
      "M": "Barnabas wanted to take John, also known as Mark, with them.",
      "T": "Barnabas was set on taking John—the one called Mark—along with them."
    },
    "38": {
      "L": "But Paul thought it best not to take with them the one who had departed from them in Pamphylia and had not gone with them to the work.",
      "M": "But Paul did not think it wise to take him, because he had deserted them in Pamphylia and had not continued with them in the work.",
      "T": "Paul was firmly against it, since Mark had abandoned them in Pamphylia and hadn't seen the work through."
    },
    "39": {
      "L": "And there arose a sharp contention, so that they separated from one another; and Barnabas, taking Mark, sailed away to Cyprus.",
      "M": "They had such a sharp disagreement that they parted company. Barnabas took Mark and sailed for Cyprus,",
      "T": "The disagreement was so heated that they parted ways. Barnabas took Mark and sailed to Cyprus."
    },
    "40": {
      "L": "But Paul chose Silas and departed, being commended by the brothers to the grace of the Lord.",
      "M": "but Paul chose Silas and left, commended by the believers to the grace of the Lord.",
      "T": "Paul chose Silas instead, and the community commended them to the Lord's grace as they set out."
    },
    "41": {
      "L": "And he went through Syria and Cilicia, strengthening the assemblies.",
      "M": "He travelled through Syria and Cilicia, strengthening the churches.",
      "T": "He travelled through Syria and Cilicia, building up and strengthening the communities."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'acts')
        merge_tier(existing, ACTS, tier_key)
        save(tier_dir, 'acts', existing)
    print('Acts 11–15 written.')

if __name__ == '__main__':
    main()
