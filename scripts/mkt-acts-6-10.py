"""
MKT Acts chapters 6–10 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-acts-6-10.py

Translation decisions:
- Stephen's speech (ch. 7) tracks LXX closely in L tier; OT quotes rendered from source.
- Isaiah 53 quote (ch. 8) rendered with attention to Hebrew and LXX registers.
- πνεῦμα: capitalised as Spirit in Holy Spirit references; lowercase for human spirit (ch. 7:59).
- ἐκκλησία: "assembly" (L), "church" (M), "community" (T).
- Cornelius episode (ch. 10): honour-shame social dynamics preserved; "God-fearer" retained.
- Peter's sermon (10:34-43) carefully handles aorist 'was anointed', 'went about', 'we ate and drank'.
- Δικαιοσύνη (righteousness) in 10:35 rendered fully — it is covenantal uprightness, not mere morality.
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
  # ── CHAPTER 6 ──────────────────────────────────────────────────────────────
  "6": {
    "1": {
      "L": "Now in those days, when the number of the disciples was multiplying, there arose a murmuring of the Hellenists against the Hebrews, because their widows were being neglected in the daily distribution.",
      "M": "In those days when the number of disciples was increasing, the Hellenistic Jews among them complained against the Hebraic Jews because their widows were being overlooked in the daily distribution of food.",
      "T": "As the number of disciples was growing rapidly, tension surfaced: the Greek-speaking Jewish believers were complaining that their widows were being overlooked in the daily food distribution, while the Aramaic-speaking believers were not."
    },
    "2": {
      "L": "And the twelve summoned the full number of the disciples and said, 'It is not pleasing for us to leave the word of God to serve tables.'",
      "M": "So the Twelve gathered all the disciples together and said, 'It would not be right for us to neglect the ministry of the word of God in order to wait on tables.'",
      "T": "The twelve apostles called the whole community together and said, 'It is not right for us to set aside the proclamation of God's word to manage food distribution.'"
    },
    "3": {
      "L": "'Therefore, brothers, select from among yourselves seven men of good report, full of the Spirit and of wisdom, whom we will appoint over this need.'",
      "M": "'Brothers and sisters, choose seven men from among you who are known to be full of the Spirit and wisdom. We will turn this responsibility over to them'",
      "T": "'So, brothers and sisters, choose seven men from among you—people of good character, full of the Holy Spirit and sound judgment. We will put them in charge of this work.'"
    },
    "4": {
      "L": "'But we will devote ourselves continually to prayer and to the ministry of the word.'",
      "M": "'and will give our attention to prayer and the ministry of the word.'",
      "T": "'This will free us to give ourselves fully to prayer and to proclaiming the word.'"
    },
    "5": {
      "L": "And the proposal pleased the whole multitude; and they chose Stephen, a man full of faith and the Holy Spirit, and Philip, and Prochorus, and Nicanor, and Timon, and Parmenas, and Nicolas, a proselyte from Antioch,",
      "M": "This proposal pleased the whole group. They chose Stephen, a man full of faith and of the Holy Spirit; also Philip, Procorus, Nicanor, Timon, Parmenas, and Nicolas from Antioch, a convert to Judaism.",
      "T": "This pleased everyone. They chose Stephen, a man brimming with faith and the Holy Spirit, along with Philip, Prochorus, Nicanor, Timon, Parmenas, and Nicolas, a Gentile convert from Antioch."
    },
    "6": {
      "L": "whom they placed before the apostles; and having prayed, they laid their hands on them.",
      "M": "They presented these men to the apostles, who prayed and laid their hands on them.",
      "T": "These seven were brought before the apostles, who prayed over them and laid their hands on them."
    },
    "7": {
      "L": "And the word of God was increasing, and the number of disciples was multiplying greatly in Jerusalem; and a great company of the priests were becoming obedient to the faith.",
      "M": "So the word of God spread. The number of disciples in Jerusalem increased rapidly, and a large number of priests became obedient to the faith.",
      "T": "The word of God kept spreading and growing. The number of disciples in Jerusalem multiplied dramatically, and a great many priests came to embrace the faith."
    },
    "8": {
      "L": "And Stephen, full of grace and power, was doing great wonders and signs among the people.",
      "M": "Now Stephen, a man full of God's grace and power, performed great wonders and signs among the people.",
      "T": "Stephen, filled with God's grace and power, was performing remarkable miracles and signs among the people."
    },
    "9": {
      "L": "But some rose up from the synagogue called the Synagogue of the Freedmen (and some of Cyrenians and Alexandrians, and of those from Cilicia and Asia), and they disputed with Stephen.",
      "M": "Opposition arose, however, from members of the Synagogue of the Freedmen (as it was called)—Jews of Cyrene and Alexandria as well as the provinces of Cilicia and Asia—who began to argue with Stephen.",
      "T": "But some men from the Synagogue of the Freedmen—people from Cyrene, Alexandria, Cilicia, and the province of Asia—started arguing with Stephen."
    },
    "10": {
      "L": "And they were not able to withstand the wisdom and the Spirit with which he was speaking.",
      "M": "But they could not stand up against the wisdom the Spirit gave him as he spoke.",
      "T": "They were no match for him: the wisdom and the Spirit behind his words were overwhelming."
    },
    "11": {
      "L": "Then they secretly persuaded men to say, 'We have heard him speaking blasphemous words against Moses and against God.'",
      "M": "Then they secretly persuaded some men to say, 'We have heard Stephen speak blasphemous words against Moses and against God.'",
      "T": "Unable to defeat him in debate, they secretly put men up to say, 'We heard him blaspheme Moses and God.'"
    },
    "12": {
      "L": "And they stirred up the people and the elders and the scribes; and coming upon him, they seized him and brought him to the council.",
      "M": "So they stirred up the people and the elders and the teachers of the law. They seized Stephen and brought him before the Sanhedrin.",
      "T": "They incited the crowd, the elders, and the religious scholars. Stephen was grabbed, arrested, and dragged before the council."
    },
    "13": {
      "L": "And they put forward false witnesses who said, 'This man does not cease speaking words against this holy place and the law;'",
      "M": "They produced false witnesses, who testified, 'This fellow never stops speaking against this holy place and against the law.'",
      "T": "They brought in false witnesses who declared, 'This man constantly says things against the temple and the law.'"
    },
    "14": {
      "L": "'for we have heard him say that Jesus the Nazarene will destroy this place and will change the customs which Moses delivered to us.'",
      "M": "'For we have heard him say that this Jesus of Nazareth will destroy this place and change the customs Moses handed down to us.'",
      "T": "'We heard him say that Jesus of Nazareth will demolish this place and change the customs that Moses passed on to us.'"
    },
    "15": {
      "L": "And gazing at him, all who were sitting in the council saw his face, as if it were the face of an angel.",
      "M": "All who were sitting in the Sanhedrin looked intently at Stephen, and they saw that his face was like the face of an angel.",
      "T": "Every member of the council fixed their eyes on Stephen, and they saw something startling: his face looked like the face of an angel."
    }
  },

  # ── CHAPTER 7 ──────────────────────────────────────────────────────────────
  "7": {
    "1": {
      "L": "And the high priest said, 'Are these things so?'",
      "M": "Then the high priest asked Stephen, 'Are these charges true?'",
      "T": "The high priest asked Stephen, 'Is this true?'"
    },
    "2": {
      "L": "And he said, 'Brothers and fathers, hear me. The God of glory appeared to our father Abraham while he was in Mesopotamia, before he lived in Charran,'",
      "M": "To this he replied: 'Brothers and fathers, listen to me! The God of glory appeared to our father Abraham while he was still in Mesopotamia, before he lived in Harran.'",
      "T": "Stephen answered: 'Brothers and fathers, hear me out. The God of glory appeared to our ancestor Abraham while he was still in Mesopotamia, long before he ever settled in Haran.'"
    },
    "3": {
      "L": "'and said to him, 'Leave your country and your kindred, and come into the land which I will show you.''",
      "M": "''Leave your country and your people,' God said, 'and go to the land I will show you.''",
      "T": "'God told him, 'Leave your homeland and your family, and travel to the land I will show you.''"
    },
    "4": {
      "L": "'Then having departed from the land of the Chaldaeans, he lived in Charran; and from there, after his father died, God removed him into this land in which you now dwell.'",
      "M": "'So he left the land of the Chaldeans and settled in Harran. After the death of his father, God sent him to this land where you are now living.'",
      "T": "'So Abraham left the Chaldeans behind and settled in Haran. After his father died, God moved him to this very land where you now live.'"
    },
    "5": {
      "L": "'And he gave him no inheritance in it, not even a foot's length, and yet promised to give it to him as a possession, and to his offspring after him, when he did not yet have a child.'",
      "M": "'He gave him no inheritance here, not even enough ground to set his foot on. But God promised him that he and his descendants after him would possess the land, even though at that time Abraham had no child.'",
      "T": "'God gave Abraham no land here—not even a foot of it. Yet he promised that one day this land would belong to Abraham and his descendants, even though at the time Abraham had no children at all.'"
    },
    "6": {
      "L": "'And God spoke in this way, that his offspring would be strangers in a foreign land, and would be enslaved and mistreated four hundred years.'",
      "M": "'God spoke to him in this way: 'Your descendants will be strangers in a country not their own, and they will be enslaved and mistreated four hundred years.''",
      "T": "'God told him this: 'Your descendants will be foreigners in a strange land, where they will be enslaved and oppressed for four hundred years.''"
    },
    "7": {
      "L": "''And the nation that they serve I will judge,' said God, 'and after that they will come out and worship me in this place.''",
      "M": "''But I will punish the nation they serve as slaves,' God said, 'and afterwards they will come out of that country and worship me in this place.''",
      "T": "''But I will judge the nation that enslaves them,' said God. 'After that they will come out and worship me here in this land.''"
    },
    "8": {
      "L": "'And he gave him the covenant of circumcision. And thus Abraham fathered Isaac, and circumcised him on the eighth day; and Isaac fathered Jacob, and Jacob the twelve patriarchs.'",
      "M": "'Then he gave Abraham the covenant of circumcision. And Abraham became the father of Isaac and circumcised him eight days after his birth. Later Isaac became the father of Jacob, and Jacob became the father of the twelve patriarchs.'",
      "T": "'Then God gave Abraham the covenant of circumcision. Abraham became the father of Isaac and circumcised him on the eighth day. Isaac became the father of Jacob, and Jacob the father of the twelve patriarchs.'"
    },
    "9": {
      "L": "'And the patriarchs, moved with jealousy, sold Joseph into Egypt; and God was with him,'",
      "M": "'Because the patriarchs were jealous of Joseph, they sold him as a slave into Egypt. But God was with him'",
      "T": "'The patriarchs were jealous of Joseph and sold him into slavery in Egypt. But God was with him'"
    },
    "10": {
      "L": "'and delivered him out of all his afflictions, and gave him favour and wisdom in the sight of Pharaoh king of Egypt; and he appointed him governor over Egypt and all his house.'",
      "M": "'and rescued him from all his troubles. He gave Joseph wisdom and enabled him to gain the goodwill of Pharaoh king of Egypt; so Pharaoh made him ruler over Egypt and all his palace.'",
      "T": "'and rescued him from every hardship. He gave Joseph wisdom and the favour of Pharaoh king of Egypt, who appointed him governor over Egypt and his entire household.'"
    },
    "11": {
      "L": "'Then a famine came over all Egypt and Canaan, and great affliction; and our fathers were finding no sustenance.'",
      "M": "'Then a famine struck all Egypt and Canaan, bringing great suffering, and our ancestors could not find food.'",
      "T": "'Then a severe famine hit both Egypt and Canaan, causing great hardship. Our ancestors could find nothing to eat.'"
    },
    "12": {
      "L": "'But Jacob, having heard that there was grain in Egypt, sent out our fathers the first time.'",
      "M": "'When Jacob heard that there was grain in Egypt, he sent our forefathers on their first visit.'",
      "T": "'When Jacob heard there was grain in Egypt, he sent our ancestors on their first trip there.'"
    },
    "13": {
      "L": "'And at the second time Joseph was made known to his brothers, and Joseph's family was revealed to Pharaoh.'",
      "M": "'On their second visit, Joseph told his brothers who he was, and Pharaoh learned about Joseph's family.'",
      "T": "'On their second visit, Joseph revealed himself to his brothers, and his family became known to Pharaoh.'"
    },
    "14": {
      "L": "'And Joseph, sending word, called his father Jacob to him, and all his kindred, seventy-five souls in all.'",
      "M": "'After this, Joseph sent for his father Jacob and his whole family, seventy-five in all.'",
      "T": "'Joseph then sent for his father Jacob and the whole family—seventy-five people in all.'"
    },
    "15": {
      "L": "'And Jacob went down into Egypt, and he died, he and our fathers,'",
      "M": "'Then Jacob went down to Egypt, where he and our ancestors died.'",
      "T": "'Jacob went down to Egypt, and there he died, along with all our ancestors.'"
    },
    "16": {
      "L": "'and they were carried over to Shechem and laid in the tomb that Abraham had bought for a sum of money from the sons of Hamor in Shechem.'",
      "M": "'Their bodies were brought back to Shechem and placed in the tomb that Abraham had bought from the sons of Hamor at Shechem for a certain sum of money.'",
      "T": "'Their remains were brought back to Shechem and placed in the tomb that Abraham had purchased from the sons of Hamor at Shechem.'"
    },
    "17": {
      "L": "'But as the time of the promise was drawing near which God had sworn to Abraham, the people grew and multiplied in Egypt,'",
      "M": "'As the time drew near for God to fulfil his promise to Abraham, the number of our people in Egypt had greatly increased.'",
      "T": "'As the time approached for God to fulfill the promise he had made to Abraham, the population of our people in Egypt had grown enormous.'"
    },
    "18": {
      "L": "'until another king arose who did not know Joseph.'",
      "M": "'Then 'a new king, to whom Joseph meant nothing, came to power in Egypt.''",
      "T": "'Then a new king came to power in Egypt who had never heard of Joseph.'"
    },
    "19": {
      "L": "'This one, having dealt craftily with our race, mistreated our fathers so that they were compelled to expose their infants, that they might not survive.'",
      "M": "'He dealt treacherously with our people and oppressed our ancestors by forcing them to throw out their newborn babies so that they would die.'",
      "T": "'He exploited our people with cunning cruelty, forcing our ancestors to abandon their newborn babies so they would die.'"
    },
    "20": {
      "L": "'At this time Moses was born, and he was beautiful to God; and he was nourished three months in his father's house.'",
      "M": "'At that time Moses was born, and he was no ordinary child. For three months he was cared for in his parents' house.'",
      "T": "'It was at that time that Moses was born—a child beautiful to God. He was cared for in his father's home for three months.'"
    },
    "21": {
      "L": "'And when he had been exposed, Pharaoh's daughter took him up and nourished him as her own son.'",
      "M": "'When he was placed outside, Pharaoh's daughter took him and brought him up as her own son.'",
      "T": "'When he was abandoned, Pharaoh's daughter found him and raised him as her own son.'"
    },
    "22": {
      "L": "'And Moses was educated in all the wisdom of the Egyptians, and he was mighty in his words and deeds.'",
      "M": "'Moses was educated in all the wisdom of the Egyptians and was powerful in speech and action.'",
      "T": "'Moses was trained in all the learning of Egypt and became powerful in both speech and action.'"
    },
    "23": {
      "L": "'But when forty years had passed, it arose in his heart to visit his brothers, the children of Israel.'",
      "M": "'When Moses was forty years old, he decided to visit his own people, the Israelites.'",
      "T": "'When Moses turned forty, he felt compelled to visit his own people, the Israelites.'"
    },
    "24": {
      "L": "'And seeing one of them being wronged, he defended him and avenged him who was oppressed, striking down the Egyptian.'",
      "M": "'He saw one of them being mistreated by an Egyptian, so he went to his defence and avenged him by killing the Egyptian.'",
      "T": "'He saw an Israelite being mistreated and stepped in to defend him, striking down the Egyptian oppressor.'"
    },
    "25": {
      "L": "'He supposed that his brothers would understand that God was giving them deliverance by his hand; but they did not understand.'",
      "M": "'Moses thought that his own people would realise that God was using him to rescue them, but they did not.',",
      "T": "'Moses assumed his own people would understand that God was using him to rescue them—but they didn't see it that way.'"
    },
    "26": {
      "L": "'And on the following day he appeared to some who were fighting and tried to reconcile them to peace, saying, 'Men, you are brothers; why do you wrong one another?''",
      "M": "'The next day Moses came upon two Israelites who were fighting. He tried to reconcile them by saying, 'Men, you are brothers; why do you want to hurt each other?''",
      "T": "'The following day he came across two Israelites fighting and tried to make peace between them: 'Friends, you are brothers—why are you hurting each other?''"
    },
    "27": {
      "L": "'But the one who was wronging his neighbour pushed him away, saying, 'Who made you a ruler and a judge over us?''",
      "M": "'But the man who was mistreating the other pushed Moses aside and said, 'Who made you ruler and judge over us?''",
      "T": "'But the man doing the wrong shoved Moses away: 'Who put you in charge as our ruler and judge?''"
    },
    "28": {
      "L": "'Are you wanting to kill me as you killed the Egyptian yesterday?",
      "M": "'Are you thinking of killing me as you killed the Egyptian yesterday?",
      "T": "'Do you plan to kill me like you killed that Egyptian yesterday?"
    },
    "29": {
      "L": "'When Moses heard this, he fled, and became an exile in the land of Midian, where he fathered two sons.'",
      "M": "'When Moses heard this, he fled to Midian, where he settled as a foreigner and had two sons.'",
      "T": "'Hearing this, Moses fled and lived as a foreigner in Midian, where he had two sons.'"
    },
    "30": {
      "L": "'And after forty years had passed, an angel appeared to him in the wilderness of Mount Sinai, in a flame of fire in a bush.'",
      "M": "'After forty years had passed, an angel appeared to Moses in the flames of a burning bush in the desert near Mount Sinai.'",
      "T": "'Forty years later, an angel appeared to him in the Sinai wilderness—in a flame of fire blazing from inside a bush.'"
    },
    "31": {
      "L": "'When Moses saw it, he marvelled at the sight; and as he drew near to observe, the voice of the Lord came to him:'",
      "M": "'When he saw this, he was amazed at the sight. As he went over to get a closer look, he heard the Lord's voice.'",
      "T": "'Moses stared in amazement. As he approached to look more closely, he heard the voice of the Lord:'"
    },
    "32": {
      "L": "'I am the God of your fathers, the God of Abraham and of Isaac and of Jacob.' And Moses trembled and dared not look.",
      "M": "'I am the God of your fathers, the God of Abraham, Isaac and Jacob.' Moses trembled with fear and did not dare to look.",
      "T": "'I am the God of your ancestors—Abraham, Isaac, and Jacob.' Moses shook with fear and could not bring himself to look."
    },
    "33": {
      "L": "'The Lord said to him, 'Remove the sandals from your feet, for the place where you are standing is holy ground.''",
      "M": "'Then the Lord said to him, 'Take off your sandals, for the place where you are standing is holy ground.''",
      "T": "'The Lord said to him, 'Take off your sandals—the ground where you stand is holy.''"
    },
    "34": {
      "L": "'I have surely seen the affliction of my people who are in Egypt, and I have heard their groaning, and I have come down to deliver them. And now come, I will send you to Egypt.",
      "M": "'I have indeed seen the oppression of my people in Egypt. I have heard their groaning and have come down to set them free. Now come, I will send you back to Egypt.",
      "T": "'I have seen the suffering of my people in Egypt. I have heard their cries. I have come down to rescue them. So now—go! I am sending you to Egypt."
    },
    "35": {
      "L": "'This Moses, whom they rejected saying, 'Who made you a ruler and a judge?'—this man God sent as both ruler and deliverer, with the hand of the angel who appeared to him in the bush.'",
      "M": "'This is the same Moses they had rejected with the words, 'Who made you ruler and judge?' He was sent to be their ruler and deliverer by God himself, through the angel who appeared to him in the bush.'",
      "T": "'The very man they had rejected—'Who put you in charge?'—that man God sent as both their ruler and their deliverer, through the angel who appeared in the burning bush.'"
    },
    "36": {
      "L": "'He led them out, performing wonders and signs in the land of Egypt, and in the Red Sea, and in the wilderness for forty years.'",
      "M": "'He led them out of Egypt and performed wonders and signs in Egypt, at the Red Sea and for forty years in the wilderness.'",
      "T": "'He led them out, performing signs and wonders in Egypt, at the Red Sea, and across forty years in the wilderness.'"
    },
    "37": {
      "L": "'This is the Moses who said to the children of Israel, 'God will raise up a prophet for you from your brothers, like me.''",
      "M": "'This is the Moses who told the Israelites, 'God will raise up for you a prophet like me from your own people.''",
      "T": "'This is the Moses who told the Israelites, 'God will raise up a prophet like me from among your own people.''"
    },
    "38": {
      "L": "'This is the one who was in the assembly in the wilderness with the angel who was speaking to him on Mount Sinai, and with our fathers; who received living oracles to give to us.'",
      "M": "'He was in the assembly in the wilderness, with the angel who spoke to him on Mount Sinai, and with our ancestors; and he received living words to pass on to us.'",
      "T": "'He was the mediator in the desert assembly—standing between the angel who spoke at Sinai and our ancestors—and he received the living words of God to hand on to us.'"
    },
    "39": {
      "L": "'Our fathers were unwilling to obey him, but thrust him aside, and in their hearts turned back to Egypt,'",
      "M": "'But our ancestors refused to obey him. Instead, they rejected him and in their hearts turned back to Egypt.'",
      "T": "'But our ancestors refused to submit to him. They pushed him aside and in their hearts longed to return to Egypt.'"
    },
    "40": {
      "L": "'saying to Aaron, 'Make gods for us who will go before us; for this Moses who led us out of the land of Egypt, we do not know what has become of him.''",
      "M": "'They told Aaron, 'Make us gods who will go before us. As for this fellow Moses who led us out of Egypt—we don't know what has happened to him!''",
      "T": "'They said to Aaron, 'Make us gods to lead us, because this Moses who brought us out of Egypt—we have no idea what happened to him.''"
    },
    "41": {
      "L": "'And they made a calf in those days, and brought a sacrifice to the idol, and were rejoicing in the works of their hands.'",
      "M": "'That was the time they made an idol in the form of a calf. They brought sacrifices to it and revelled in what their own hands had made.'",
      "T": "'That was when they fashioned a golden calf, offered sacrifices to it, and threw a celebration over the thing their own hands had made.'"
    },
    "42": {
      "L": "'But God turned and gave them up to worship the host of heaven; as it is written in the book of the prophets: 'Did you offer slain beasts and sacrifices to me for forty years in the wilderness, O house of Israel?''",
      "M": "'But God turned away from them and gave them over to the worship of the sun, moon and stars. This agrees with what is written in the book of the prophets: 'Did you bring me sacrifices and offerings forty years in the wilderness, people of Israel?''",
      "T": "'So God turned from them and abandoned them to worship the stars of heaven. This is what the prophets record: 'People of Israel, was it really me you were offering sacrifices to during those forty years in the wilderness?''"
    },
    "43": {
      "L": "'You also took up the tabernacle of Moloch and the star of the god Rephan, the figures which you made to worship them; and I will carry you away beyond Babylon.",
      "M": "'You have taken up the tabernacle of Molek and the star of your god Rephan, the idols you made to worship. Therefore I will send you into exile beyond Babylon.",
      "T": "'You carried around Molech's shrine and the star-idol of Rephan—images you made and worshipped. So I will send you into exile beyond Babylon."
    },
    "44": {
      "L": "'Our fathers had the tabernacle of witness in the wilderness, as he who spoke to Moses had commanded him to make it according to the pattern which he had seen.'",
      "M": "'Our ancestors had the tabernacle of the covenant law with them in the wilderness. It had been made as God directed Moses, according to the pattern he had seen.'",
      "T": "'Our ancestors had the sacred tent—the tabernacle of witness—in the desert. God told Moses to build it according to the exact pattern he had seen.'"
    },
    "45": {
      "L": "'And having received it in turn, our fathers brought it in with Joshua at the dispossession of the nations which God drove out before the face of our fathers—until the days of David.'",
      "M": "'After receiving the tabernacle, our ancestors under Joshua brought it with them when they took the land from the nations God drove out before them. It remained in the land until the time of David,'",
      "T": "'Passing it from generation to generation, our ancestors brought the tabernacle into the promised land with Joshua, as God drove out the nations before them. It remained there until the time of David—'"
    },
    "46": {
      "L": "'who found favour in the sight of God and asked to find a tabernacle for the God of Jacob.'",
      "M": "'who enjoyed God's favour and asked that he might provide a dwelling place for the God of Jacob.'",
      "T": "'—who received God's favour and longed to build a permanent home for the God of Jacob.'"
    },
    "47": {
      "L": "'But it was Solomon who built a house for him.'",
      "M": "'But it was Solomon who built a house for him.'",
      "T": "'But in the end it was Solomon who built him a house.'"
    },
    "48": {
      "L": "'Yet the Most High does not dwell in houses made with hands; as the prophet says:'",
      "M": "'However, the Most High does not live in houses made by human hands. As the prophet says:'",
      "T": "'And yet—the Most High does not live in buildings made by human hands. As the prophet declared:'"
    },
    "49": {
      "L": "'Heaven is my throne, and the earth is the footstool of my feet. What sort of house will you build me? says the Lord, or what is the place of my rest?",
      "M": "'Heaven is my throne, and the earth is my footstool. What kind of house will you build for me? says the Lord. Or where will my resting place be?",
      "T": "'Heaven is my throne, and the earth is my footstool. What kind of house could you possibly build for me? says the Lord. Where would I even rest?"
    },
    "50": {
      "L": "'Has not my hand made all these things?",
      "M": "'Has not my hand made all these things?",
      "T": "'Didn't my own hand make all of this?"
    },
    "51": {
      "L": "'You stiff-necked and uncircumcised in heart and ears! You always resist the Holy Spirit; as your fathers did, so also do you.'",
      "M": "'You stiff-necked people! Your hearts and ears are still uncircumcised. You are just like your ancestors: you always resist the Holy Spirit!'",
      "T": "'Stubborn and hard-hearted, with ears that refuse to listen—you are no different from your ancestors! You keep on resisting the Holy Spirit, generation after generation.'"
    },
    "52": {
      "L": "'Which of the prophets did your fathers not persecute? And they killed those who foretold the coming of the Righteous One, of whom you have now become betrayers and murderers;'",
      "M": "'Was there ever a prophet your ancestors did not persecute? They even killed those who predicted the coming of the Righteous One. And now you have betrayed and murdered him—'",
      "T": "'Was there ever a prophet your ancestors did not persecute? They murdered every one who announced the coming of the Righteous One. And now you have become his betrayers—and his murderers.'"
    },
    "53": {
      "L": "'you who received the law as ordained by angels, and did not keep it.'",
      "M": "'you who have received the law that was given through angels but have not obeyed it.'",
      "T": "'You received the law that came through angels—the very law you haven't kept.'"
    },
    "54": {
      "L": "Now when they heard these things, they were cut to the heart, and they gnashed their teeth at him.",
      "M": "When the members of the Sanhedrin heard this, they were furious and gnashed their teeth at him.",
      "T": "These words hit like a blade. The council members were in a rage, grinding their teeth at him."
    },
    "55": {
      "L": "But being full of the Holy Spirit, he gazed intently into heaven and saw the glory of God, and Jesus standing at the right hand of God,",
      "M": "But Stephen, full of the Holy Spirit, looked up to heaven and saw the glory of God, and Jesus standing at the right hand of God.",
      "T": "But Stephen, filled with the Holy Spirit, looked up into heaven and saw the glory of God—and Jesus standing at God's right hand."
    },
    "56": {
      "L": "and he said, 'Behold, I see the heavens opened, and the Son of Man standing at the right hand of God.'",
      "M": "'Look,' he said, 'I see heaven open and the Son of Man standing at the right hand of God.'",
      "T": "'Look!' he said. 'The heavens are open, and I can see the Son of Man standing at the right hand of God!'"
    },
    "57": {
      "L": "At this they cried out with a loud voice and covered their ears and rushed together upon him.",
      "M": "At this they covered their ears and, yelling at the top of their voices, they all rushed at him,",
      "T": "At that the crowd erupted. They covered their ears, roared with one voice, and rushed at him together."
    },
    "58": {
      "L": "And having driven him out of the city, they stoned him; and the witnesses laid down their garments at the feet of a young man called Saul.",
      "M": "dragged him out of the city and began to stone him. Meanwhile, the witnesses laid their coats at the feet of a young man named Saul.",
      "T": "They dragged him outside the city walls and began hurling stones at him. The witnesses who threw the first stones laid their cloaks at the feet of a young man named Saul."
    },
    "59": {
      "L": "And they stoned Stephen as he called upon the Lord and said, 'Lord Jesus, receive my spirit.'",
      "M": "While they were stoning him, Stephen prayed, 'Lord Jesus, receive my spirit.'",
      "T": "As the stones rained down, Stephen called out, 'Lord Jesus, receive my spirit!'"
    },
    "60": {
      "L": "And falling on his knees, he cried out with a loud voice, 'Lord, do not hold this sin against them.' And having said this, he fell asleep.",
      "M": "Then he fell on his knees and cried out, 'Lord, do not hold this sin against them.' When he had said this, he fell asleep.",
      "T": "He dropped to his knees and cried with a loud voice, 'Lord, don't hold this sin against them!' With those words, he died."
    }
  },

  # ── CHAPTER 8 ──────────────────────────────────────────────────────────────
  "8": {
    "1": {
      "L": "And Saul was approving of his execution. And there arose on that day a great persecution against the assembly which was in Jerusalem; and they were all scattered throughout the regions of Judaea and Samaria, except the apostles.",
      "M": "And Saul approved of their killing him. On that day a great persecution broke out against the church in Jerusalem, and all except the apostles were scattered throughout Judea and Samaria.",
      "T": "Saul was right there, giving his approval to Stephen's death. That same day a wave of violent persecution broke out against the community in Jerusalem. Everyone scattered throughout Judea and Samaria—everyone, that is, except the apostles."
    },
    "2": {
      "L": "And devout men buried Stephen and made great lamentation over him.",
      "M": "Godly men buried Stephen and mourned deeply for him.",
      "T": "Some devout men buried Stephen and mourned deeply for him."
    },
    "3": {
      "L": "But Saul was ravaging the assembly, entering house by house; and dragging off men and women, he was committing them to prison.",
      "M": "But Saul began to destroy the church. Going from house to house, he dragged off both men and women and put them in prison.",
      "T": "Saul, meanwhile, was systematically destroying the community. He went from house to house, dragging out both men and women and throwing them into prison."
    },
    "4": {
      "L": "So then those who were scattered went through the lands, preaching the word.",
      "M": "Those who had been scattered preached the word wherever they went.",
      "T": "But those who had been scattered went everywhere, and everywhere they went they proclaimed the message."
    },
    "5": {
      "L": "And Philip, going down to the city of Samaria, proclaimed to them the Christ.",
      "M": "Philip went down to a city in Samaria and proclaimed the Messiah there.",
      "T": "Philip went down to a city in Samaria and announced the Messiah to the people there."
    },
    "6": {
      "L": "And the crowds with one accord were paying attention to what was being said by Philip, when they heard and saw the signs which he was performing.",
      "M": "When the crowds heard Philip and saw the signs he performed, they all paid close attention to what he said.",
      "T": "Hearing Philip's message and seeing the miraculous signs he was doing, the crowds gave him their undivided attention."
    },
    "7": {
      "L": "For from many who had unclean spirits, they were coming out, crying with a loud voice; and many who were paralysed and lame were healed.",
      "M": "For with shrieks, impure spirits came out of many, and many who were paralysed or lame were healed.",
      "T": "Unclean spirits came out of many people with loud cries. Many who were paralyzed or lame were healed."
    },
    "8": {
      "L": "And there was great joy in that city.",
      "M": "So there was great joy in that city.",
      "T": "The whole city was filled with joy."
    },
    "9": {
      "L": "Now there was a certain man named Simon who had previously been practicing magic in the city and astonishing the people of Samaria, claiming himself to be someone great.",
      "M": "Now for some time a man named Simon had practised sorcery in the city and amazed all the people of Samaria. He boasted that he was someone great,",
      "T": "There was a man named Simon who had been working as a magician in that city, dazzling the Samaritans and boasting of his own greatness."
    },
    "10": {
      "L": "To whom they were all paying attention, from the least to the greatest, saying, 'This man is the power of God which is called great.'",
      "M": "and all the people, both high and low, gave him their attention and exclaimed, 'This man is rightly called the Great Power of God.'",
      "T": "Everyone—from the least to the greatest—followed him and said, 'This man is what they call the Great Power of God.'"
    },
    "11": {
      "L": "And they were paying attention to him, because he had for a long time astonished them with his magic arts.",
      "M": "They followed him because he had amazed them for a long time with his sorcery.",
      "T": "They had followed him for years because he had amazed them with his magical arts."
    },
    "12": {
      "L": "But when they believed Philip, who was preaching the good news about the kingdom of God and the name of Jesus Christ, both men and women were being baptized.",
      "M": "But when they believed Philip as he proclaimed the good news of the kingdom of God and the name of Jesus Christ, they were baptised, both men and women.",
      "T": "But when they believed Philip's message about the reign of God and the name of Jesus the Messiah, they were baptized—men and women alike."
    },
    "13": {
      "L": "And Simon himself also believed; and being baptized, he continued with Philip; and seeing signs and great miracles being done, he was amazed.",
      "M": "Simon himself believed and was baptised. And he followed Philip everywhere, astonished by the great signs and miracles he saw.",
      "T": "Even Simon himself believed and was baptized. He attached himself to Philip, and was completely astounded watching the signs and great miracles happening before his eyes."
    },
    "14": {
      "L": "Now the apostles in Jerusalem, having heard that Samaria had received the word of God, sent to them Peter and John,",
      "M": "When the apostles in Jerusalem heard that Samaria had accepted the word of God, they sent Peter and John to Samaria.",
      "T": "When the apostles in Jerusalem heard that Samaria had received God's word, they sent Peter and John to them."
    },
    "15": {
      "L": "who, having gone down, prayed for them that they might receive the Holy Spirit.",
      "M": "When they arrived, they prayed for the new believers there that they might receive the Holy Spirit,",
      "T": "Peter and John arrived and prayed for these new believers to receive the Holy Spirit,"
    },
    "16": {
      "L": "For he had not yet fallen on any of them; they had only been baptized in the name of the Lord Jesus.",
      "M": "because the Holy Spirit had not yet come on any of them; they had simply been baptised in the name of the Lord Jesus.",
      "T": "because the Spirit had not yet come upon any of them—they had only been baptized in the name of the Lord Jesus."
    },
    "17": {
      "L": "Then they laid their hands on them, and they received the Holy Spirit.",
      "M": "Then Peter and John placed their hands on them, and they received the Holy Spirit.",
      "T": "Peter and John laid their hands on them, and they received the Holy Spirit."
    },
    "18": {
      "L": "Now when Simon saw that through the laying on of the apostles' hands the Holy Spirit was given, he offered them money,",
      "M": "When Simon saw that the Spirit was given at the laying on of the apostles' hands, he offered them money",
      "T": "Simon watched and saw that the Spirit was given through the laying on of the apostles' hands. He pulled out money"
    },
    "19": {
      "L": "saying, 'Give me also this authority, that on whomever I lay my hands, he may receive the Holy Spirit.'",
      "M": "and said, 'Give me also this ability so that everyone on whom I lay my hands may receive the Holy Spirit.'",
      "T": "and said, 'Give me this power too—so that anyone I lay my hands on will receive the Holy Spirit.'"
    },
    "20": {
      "L": "But Peter said to him, 'May your silver perish with you, because you supposed to obtain the gift of God with money!'",
      "M": "Peter answered: 'May your money perish with you, because you thought you could buy the gift of God with money!'",
      "T": "Peter said to him, 'Your money can go to ruin with you—do you really think God's gift can be bought?'"
    },
    "21": {
      "L": "'You have no part nor lot in this matter, for your heart is not right before God.'",
      "M": "'You have no part or share in this ministry, because your heart is not right before God.'",
      "T": "'You have no share in this whatsoever. Your heart is crooked before God.'"
    },
    "22": {
      "L": "'Repent therefore of this wickedness of yours, and pray to the Lord if perhaps the intent of your heart may be forgiven you.'",
      "M": "'Repent of this wickedness and pray to the Lord in the hope that he may forgive you for having such a thought in your heart.'",
      "T": "'Turn back from this evil and pray to God. Perhaps he will forgive you for thinking this way.'"
    },
    "23": {
      "L": "'For I see that you are in the gall of bitterness and the bond of iniquity.'",
      "M": "'For I see that you are full of bitterness and captive to sin.'",
      "T": "'I can see you are poisoned by bitterness and chained up in sin.'"
    },
    "24": {
      "L": "Then Simon answered and said, 'Pray to the Lord for me, that none of the things which you have spoken may come upon me.'",
      "M": "Then Simon answered, 'Pray to the Lord for me so that nothing you have said may happen to me.'",
      "T": "Simon replied, 'Pray to the Lord for me that nothing you have said will happen to me!'"
    },
    "25": {
      "L": "So when they had testified and spoken the word of the Lord, they returned to Jerusalem; and they were proclaiming the good news in many villages of the Samaritans.",
      "M": "After they had further proclaimed the word of the Lord and testified about Jesus, Peter and John returned to Jerusalem, preaching the gospel in many Samaritan villages.",
      "T": "Peter and John proclaimed the word of the Lord throughout the region and then headed back to Jerusalem, announcing the good news in many Samaritan villages along the way."
    },
    "26": {
      "L": "But an angel of the Lord spoke to Philip, saying, 'Arise and go toward the south, on the road that goes down from Jerusalem to Gaza.' (This is desert.)",
      "M": "Now an angel of the Lord said to Philip, 'Go south to the road—the desert road—that goes down from Jerusalem to Gaza.'",
      "T": "An angel of the Lord spoke to Philip: 'Get up and head south, to the road that runs from Jerusalem down to Gaza—the desert road.'"
    },
    "27": {
      "L": "And he arose and went. And behold, a man of Ethiopia, a eunuch of great authority under Candace, queen of the Ethiopians, who was over all her treasury, who had come to Jerusalem to worship,",
      "M": "So he started out, and on his way he met an Ethiopian eunuch, an important official in charge of all the treasury of the Kandake (which means 'queen of the Ethiopians'). This man had gone to Jerusalem to worship,",
      "T": "Philip set off immediately. On the road he encountered an Ethiopian man—a court official, treasurer to Candace, queen of Ethiopia—who had made the journey to Jerusalem to worship."
    },
    "28": {
      "L": "was returning and was sitting in his chariot, and was reading the prophet Isaiah.",
      "M": "and on his way home was sitting in his chariot reading the Book of Isaiah the prophet.",
      "T": "He was now on his way home, sitting in his chariot, reading aloud from the prophet Isaiah."
    },
    "29": {
      "L": "And the Spirit said to Philip, 'Go near and join this chariot.'",
      "M": "The Spirit told Philip, 'Go to that chariot and stay near it.'",
      "T": "The Spirit said to Philip, 'Go up and walk alongside that chariot.'"
    },
    "30": {
      "L": "And Philip ran to him, and heard him reading Isaiah the prophet, and said, 'Do you understand what you are reading?'",
      "M": "Then Philip ran up to the chariot and heard the man reading Isaiah the prophet. 'Do you understand what you are reading?' Philip asked.",
      "T": "Philip ran up alongside and heard him reading Isaiah the prophet. 'Do you understand what you're reading?' he asked."
    },
    "31": {
      "L": "And he said, 'How can I, unless someone guides me?' And he invited Philip to come up and sit with him.",
      "M": "'How can I,' he said, 'unless someone explains it to me?' So he invited Philip to come up and sit with him.",
      "T": "'How could I,' the man replied, 'unless someone guides me?' He invited Philip to climb up and sit with him."
    },
    "32": {
      "L": "Now the passage of scripture which he was reading was this: 'Like a sheep he was led to the slaughter; and as a lamb before its shearer is silent, so he did not open his mouth.'",
      "M": "This is the passage of Scripture the eunuch was reading: 'He was led like a sheep to the slaughter, and as a lamb before its shearer is silent, so he did not open his mouth.'",
      "T": "The passage he was reading was this: 'Like a sheep he was led away to slaughter; like a lamb silent before the shearer, he did not open his mouth.'"
    },
    "33": {
      "L": "'In his humiliation his judgment was taken away. Who will describe his generation? For his life is taken from the earth.'",
      "M": "'In his humiliation he was deprived of justice. Who can speak of his descendants? For his life was taken from the earth.'",
      "T": "'In his humiliation, justice was denied him. Who can describe his generation? For his life was swept away from the earth.'"
    },
    "34": {
      "L": "And the eunuch answered Philip and said, 'I beg you, of whom does the prophet say this? Of himself, or of someone else?'",
      "M": "The eunuch asked Philip, 'Tell me, please, who is the prophet talking about, himself or someone else?'",
      "T": "The official turned to Philip and asked, 'Please tell me—who is the prophet speaking about? Himself, or someone else?'"
    },
    "35": {
      "L": "And Philip opened his mouth, and beginning from this scripture, he proclaimed the good news to him about Jesus.",
      "M": "Then Philip began with that very passage of Scripture and told him the good news about Jesus.",
      "T": "Philip opened his mouth, started right there in that scripture, and told him the good news about Jesus."
    },
    "36": {
      "L": "And as they went along the road, they came to some water; and the eunuch said, 'See, here is water! What prevents me from being baptized?'",
      "M": "As they travelled along the road, they came to some water and the eunuch said, 'Look, here is water! What can stand in the way of my being baptised?'",
      "T": "As they travelled on, they came to a body of water. The official said, 'Look—water! What is there to stop me from being baptized?'"
    },
    "37": {
      "L": "And Philip said, 'If you believe with all your heart, you may.' And he answered and said, 'I believe that Jesus Christ is the Son of God.'",
      "M": "Philip said, 'If you believe with all your heart, you may.' The eunuch answered, 'I believe that Jesus Christ is the Son of God.'",
      "T": "Philip said, 'If you believe with your whole heart, you may.' He answered, 'I believe that Jesus the Messiah is the Son of God.'"
    },
    "38": {
      "L": "And he commanded the chariot to stop; and they both went down into the water, both Philip and the eunuch; and he baptized him.",
      "M": "And he gave orders to stop the chariot. Then both Philip and the eunuch went down into the water and Philip baptised him.",
      "T": "He ordered the chariot to halt. Both Philip and the official went down into the water, and Philip baptized him."
    },
    "39": {
      "L": "And when they came up out of the water, the Spirit of the Lord caught Philip away; and the eunuch saw him no more, and he went on his way rejoicing.",
      "M": "When they came up out of the water, the Spirit of the Lord suddenly took Philip away, and the eunuch did not see him again, but went on his way rejoicing.",
      "T": "When they came up out of the water, the Spirit of the Lord suddenly swept Philip away. The official never saw him again but continued on his way full of joy."
    },
    "40": {
      "L": "But Philip was found at Azotus; and passing through he preached the good news to all the cities, until he came to Caesarea.",
      "M": "Philip, however, appeared at Azotus and travelled about, preaching the gospel in all the towns until he reached Caesarea.",
      "T": "Philip turned up at Azotus, and from there he went through all the towns proclaiming the good news until he reached Caesarea."
    }
  },

  # ── CHAPTER 9 ──────────────────────────────────────────────────────────────
  "9": {
    "1": {
      "L": "But Saul, still breathing threats and slaughter against the disciples of the Lord, went to the high priest",
      "M": "Meanwhile, Saul was still breathing out murderous threats against the Lord's disciples. He went to the high priest",
      "T": "Meanwhile Saul was still fuming with murderous threats against the Lord's disciples. He went to the high priest"
    },
    "2": {
      "L": "and asked from him letters to Damascus to the synagogues, that if he found any who were of the Way, whether men or women, he might bring them bound to Jerusalem.",
      "M": "and asked him for letters to the synagogues in Damascus, so that if he found any there who belonged to the Way, whether men or women, he might take them as prisoners to Jerusalem.",
      "T": "and requested letters to the synagogues in Damascus, authorizing him to arrest anyone who followed the Way—men or women—and bring them back to Jerusalem as prisoners."
    },
    "3": {
      "L": "And as he journeyed, it came to pass that he was drawing near to Damascus; and suddenly a light from heaven shone around him,",
      "M": "As he neared Damascus on his journey, suddenly a light from heaven flashed around him.",
      "T": "As he approached Damascus, suddenly a brilliant light from heaven blazed around him."
    },
    "4": {
      "L": "and falling to the ground, he heard a voice saying to him, 'Saul, Saul, why are you persecuting me?'",
      "M": "He fell to the ground and heard a voice say to him, 'Saul, Saul, why do you persecute me?'",
      "T": "He fell to the ground, and a voice called out: 'Saul, Saul—why are you persecuting me?'"
    },
    "5": {
      "L": "And he said, 'Who are you, Lord?' And he said, 'I am Jesus, whom you are persecuting; but rise and enter the city, and it shall be told you what you must do.'",
      "M": "'Who are you, Lord?' Saul asked. 'I am Jesus, whom you are persecuting,' he replied. 'Now get up and go into the city, and you will be told what you must do.'",
      "T": "'Who are you, Lord?' Saul asked. 'I am Jesus—the one you are persecuting,' came the reply. 'Now get up and go into the city. You will be told what you must do.'"
    },
    "6": {
      "L": "And the men who were travelling with him stood speechless, hearing a voice but seeing no one.",
      "M": "The men travelling with Saul stood there speechless; they heard the sound but did not see anyone.",
      "T": "The men traveling with Saul stood frozen, hearing the voice but unable to see anyone."
    },
    "7": {
      "L": "And Saul arose from the ground; and when his eyes were opened, he saw nothing; and leading him by the hand, they brought him into Damascus.",
      "M": "Saul got up from the ground, but when he opened his eyes he could see nothing. So they led him by the hand into Damascus.",
      "T": "Saul got up from the ground. When he opened his eyes he could see nothing. They took him by the hand and led him into Damascus."
    },
    "8": {
      "L": "And he was three days without sight, and neither ate nor drank.",
      "M": "For three days he was blind, and did not eat or drink anything.",
      "T": "For three days he sat in complete darkness, eating and drinking nothing."
    },
    "9": {
      "L": "Now there was a certain disciple in Damascus named Ananias; and the Lord said to him in a vision, 'Ananias.' And he said, 'Behold, I am here, Lord.'",
      "M": "In Damascus there was a disciple named Ananias. The Lord called to him in a vision, 'Ananias!' 'Yes, Lord,' he answered.",
      "T": "In Damascus there was a disciple named Ananias. The Lord appeared to him in a vision: 'Ananias!' 'Here I am, Lord,' he said."
    },
    "10": {
      "L": "And the Lord said to him, 'Arise and go to the street called Straight, and inquire in the house of Judas for one named Saul, a Tarsian; for behold, he is praying,'",
      "M": "'Go to the house of Judas on Straight Street and ask for a man from Tarsus named Saul, for he is praying.'",
      "T": "'Go to Straight Street and look for a man from Tarsus named Saul at the house of Judas. He is praying right now.'"
    },
    "11": {
      "L": "'and in a vision he has seen a man named Ananias coming in and laying his hands on him, that he might recover his sight.'",
      "M": "'In a vision he has seen a man named Ananias come and place his hands on him to restore his sight.'",
      "T": "'In a vision he has already seen you—a man named Ananias—coming in and placing your hands on him to restore his sight.'"
    },
    "12": {
      "L": "But Ananias answered, 'Lord, I have heard from many concerning this man, how much evil he has done to your saints in Jerusalem;'",
      "M": "'Lord,' Ananias answered, 'I have heard many reports about this man and all the harm he has done to your holy people in Jerusalem.'",
      "T": "'Lord,' Ananias replied, 'I've heard plenty about this man—how much suffering he has caused your people in Jerusalem.'"
    },
    "13": {
      "L": "'and here he has authority from the chief priests to bind all who call on your name.'",
      "M": "'And he has come here with authority from the chief priests to arrest all who call on your name.'",
      "T": "'He's here with authority from the chief priests to arrest everyone who calls on your name.'"
    },
    "14": {
      "L": "But the Lord said to him, 'Go, for he is a chosen vessel to me, to bear my name before the Gentiles and kings and the children of Israel;'",
      "M": "But the Lord said to Ananias, 'Go! This man is my chosen instrument to proclaim my name to the Gentiles and their kings and to the people of Israel.'",
      "T": "'Go,' the Lord said. 'He is my chosen instrument—I have selected him to carry my name to the Gentiles, to their kings, and to the people of Israel.'"
    },
    "15": {
      "L": "'for I will show him how great things he must suffer for my name's sake.'",
      "M": "'I will show him how much he must suffer for my name.'",
      "T": "'And I will show him how much he must suffer for the sake of my name.'"
    },
    "16": {
      "L": "And Ananias departed and entered the house; and laying his hands on him said, 'Brother Saul, the Lord has sent me—Jesus, who appeared to you on the road by which you were coming—that you may recover your sight and be filled with the Holy Spirit.'",
      "M": "Then Ananias went to the house and entered it. Placing his hands on Saul, he said, 'Brother Saul, the Lord—Jesus, who appeared to you on the road as you were coming here—has sent me so that you may see again and be filled with the Holy Spirit.'",
      "T": "Ananias went to the house, walked in, and placed his hands on Saul. 'Brother Saul,' he said, 'the Lord Jesus—who appeared to you on the road—has sent me so that you can see again and be filled with the Holy Spirit.'"
    },
    "17": {
      "L": "And immediately there fell from his eyes something like scales, and he recovered his sight; and rising up, he was baptized.",
      "M": "Immediately, something like scales fell from Saul's eyes, and he could see again. He got up and was baptised,",
      "T": "Immediately something like scales fell from his eyes and his sight came back. He stood up and was baptized."
    },
    "18": {
      "L": "and taking food, he was strengthened. And he was with the disciples who were in Damascus certain days.",
      "M": "and after taking some food, he regained his strength. Saul spent several days with the disciples in Damascus.",
      "T": "He ate something and his strength returned. He stayed in Damascus for several days with the disciples."
    },
    "19": {
      "L": "And immediately in the synagogues he proclaimed Jesus, that he is the Son of God.",
      "M": "At once he began to preach in the synagogues that Jesus is the Son of God.",
      "T": "Without delay he began announcing in the synagogues that Jesus is the Son of God."
    },
    "20": {
      "L": "And all who heard him were amazed, and said, 'Is this not the one who in Jerusalem was ravaging those who call on this name? And has he not come here for the purpose that he might bring them bound to the chief priests?'",
      "M": "All those who heard him were astonished and asked, 'Isn't he the man who raised havoc in Jerusalem among those who call on this name? And hasn't he come here to take them as prisoners to the chief priests?'",
      "T": "Everyone who heard him was stunned. 'Isn't this the man who was terrorizing believers in Jerusalem and came here specifically to arrest people and take them to the chief priests?'"
    },
    "21": {
      "L": "But Saul increased all the more in strength, and confounded the Jews who dwelt at Damascus, proving that this is the Christ.",
      "M": "Yet Saul grew more and more powerful and baffled the Jews living in Damascus by proving that Jesus is the Messiah.",
      "T": "Yet Saul grew stronger and stronger in his proclamation, leaving the Jewish community in Damascus completely confounded as he demonstrated that Jesus is the Messiah."
    },
    "22": {
      "L": "And when many days had passed, the Jews conspired together to kill him;",
      "M": "After many days had gone by, there was a conspiracy among the Jews to kill him,",
      "T": "Some time later the Jewish leaders in Damascus plotted together to kill him."
    },
    "23": {
      "L": "but their plot became known to Saul. And they were watching the gates also day and night to kill him;",
      "M": "but Saul learned of their plan. Day and night they kept close watch on the city gates in order to kill him.",
      "T": "But Saul found out about the conspiracy. They had the city gates watched day and night to catch him."
    },
    "24": {
      "L": "but his disciples took him by night and let him down through the wall, lowering him in a basket.",
      "M": "But his followers took him by night and lowered him in a basket through an opening in the wall.",
      "T": "But his disciples helped him escape by night, lowering him in a basket through an opening in the city wall."
    },
    "25": {
      "L": "And Saul, having come to Jerusalem, tried to join himself to the disciples; and they were all afraid of him, not believing that he was a disciple.",
      "M": "When he came to Jerusalem, he tried to join the disciples, but they were all afraid of him, not believing that he really was a disciple.",
      "T": "When Saul arrived in Jerusalem and tried to join the disciples, they were all afraid of him. They couldn't believe he had truly become a disciple."
    },
    "26": {
      "L": "But Barnabas, having taken him, brought him to the apostles, and told them how on the road he had seen the Lord, and that he had spoken to him; and how in Damascus he had spoken boldly in the name of Jesus.",
      "M": "But Barnabas took him and brought him to the apostles. He told them how Saul on his journey had seen the Lord and that the Lord had spoken to him, and how in Damascus he had preached fearlessly in the name of Jesus.",
      "T": "Barnabas came alongside Saul, brought him to the apostles, and told the whole story: how Saul had seen the Lord on the road, how the Lord had spoken to him, and how boldly he had proclaimed Jesus in Damascus."
    },
    "27": {
      "L": "And he was with them moving in and out in Jerusalem, speaking boldly in the name of the Lord.",
      "M": "So Saul stayed with them and moved about freely in Jerusalem, speaking boldly in the name of the Lord.",
      "T": "From then on Saul moved freely among them in Jerusalem, speaking with boldness in the name of the Lord."
    },
    "28": {
      "L": "And he spoke and disputed against the Hellenists; but they were seeking to kill him.",
      "M": "He talked and debated with the Hellenistic Jews, but they tried to kill him.",
      "T": "He engaged in vigorous debate with the Greek-speaking Jewish community, who responded by plotting to kill him."
    },
    "29": {
      "L": "And when the brothers knew it, they brought him down to Caesarea and sent him off to Tarsus.",
      "M": "When the believers learned of this, they took him down to Caesarea and sent him off to Tarsus.",
      "T": "When the community found out, they brought him down to Caesarea and put him on a boat to Tarsus."
    },
    "30": {
      "L": "So the assembly throughout all Judaea and Galilee and Samaria had peace, being built up; and walking in the fear of the Lord and in the comfort of the Holy Spirit, it was multiplied.",
      "M": "Then the church throughout Judea, Galilee and Samaria enjoyed a time of peace and was strengthened. Living in the fear of the Lord and encouraged by the Holy Spirit, it increased in numbers.",
      "T": "During this time the community throughout Judea, Galilee, and Samaria enjoyed peace and grew strong. Living in reverence of the Lord and in the encouragement of the Holy Spirit, their numbers kept increasing."
    },
    "31": {
      "L": "Now it came to pass, as Peter was passing through all those regions, that he also came down to the saints who dwelt at Lydda.",
      "M": "As Peter travelled about the country, he went to visit the Lord's people who lived in Lydda.",
      "T": "As Peter was traveling through the region, he visited the Lord's people living at Lydda."
    },
    "32": {
      "L": "And he found there a certain man named Aeneas, who had been lying on a mat for eight years, who was paralysed.",
      "M": "There he found a man named Aeneas, who was paralysed and had been bedridden for eight years.",
      "T": "There he found a man named Aeneas who had been paralyzed and bedridden for eight years."
    },
    "33": {
      "L": "And Peter said to him, 'Aeneas, Jesus Christ heals you; rise up and make your bed.' And immediately he arose.",
      "M": "'Aeneas,' Peter said to him, 'Jesus Christ heals you. Get up and roll up your mat.' Immediately Aeneas got up.",
      "T": "Peter said to him, 'Aeneas, Jesus the Messiah heals you. Get up and make your bed.' And he got up immediately."
    },
    "34": {
      "L": "And all who dwelt at Lydda and Sharon saw him, and they turned to the Lord.",
      "M": "All those who lived in Lydda and Sharon saw him and turned to the Lord.",
      "T": "When the people of Lydda and Sharon saw what had happened, they turned to the Lord."
    },
    "35": {
      "L": "Now there was at Joppa a certain disciple named Tabitha, which translated means Dorcas. She was full of good works and almsdeeds which she was continually doing.",
      "M": "In Joppa there was a disciple named Tabitha (in Greek her name is Dorcas); she was always doing good and helping the poor.",
      "T": "In the town of Joppa there was a disciple named Tabitha—her Greek name was Dorcas—who was constantly doing good and helping those in need."
    },
    "36": {
      "L": "And it came to pass in those days, that she fell sick and died; and when they had washed her, they laid her in an upper room.",
      "M": "About that time she became ill and died, and her body was washed and placed in an upstairs room.",
      "T": "Around this time she became ill and died. After washing her body, they laid her in an upper room."
    },
    "37": {
      "L": "Now Lydda was near Joppa; and when the disciples heard that Peter was there, they sent two men to him, entreating him, 'Do not delay to come through to us.'",
      "M": "Lydda was near Joppa; so when the disciples heard that Peter was in Lydda, they sent two men to him and urged him, 'Please come at once!'",
      "T": "Lydda was close to Joppa. When the disciples heard that Peter was there, they sent two men urging him, 'Please come to us right away!'"
    },
    "38": {
      "L": "And Peter arose and went with them. When he arrived, they led him to the upper room; and all the widows stood beside him weeping, and showing him the tunics and garments which Dorcas had made while she was with them.",
      "M": "Peter went with them, and when he arrived he was taken upstairs to the room. All the widows stood around him, crying and showing him the robes and other clothing that Dorcas had made while she was still with them.",
      "T": "Peter set off with them immediately. When he arrived, he was brought upstairs to the room. All the widows gathered around him in tears, holding up the tunics and cloaks that Dorcas had made for them."
    },
    "39": {
      "L": "But Peter, sending them all out, knelt down and prayed; and turning to the body, he said, 'Tabitha, arise.' And she opened her eyes; and seeing Peter, she sat up.",
      "M": "Peter sent them all out of the room; then he got down on his knees and prayed. Turning towards the dead woman, he said, 'Tabitha, get up.' She opened her eyes and seeing Peter she sat up.",
      "T": "Peter sent everyone out of the room. He got down on his knees and prayed. Then, turning to her body, he said, 'Tabitha, get up.' She opened her eyes, saw Peter, and sat up."
    },
    "40": {
      "L": "And giving her his hand, he raised her up; and calling the saints and widows, he presented her alive.",
      "M": "He took her by the hand and helped her to her feet. Then he called for the believers, especially the widows, and presented her to them alive.",
      "T": "He took her hand and helped her to her feet. Then he called in the believers and the widows and presented Tabitha alive."
    },
    "41": {
      "L": "And it became known throughout all Joppa, and many believed on the Lord.",
      "M": "This became known all over Joppa, and many people believed in the Lord.",
      "T": "News of this spread through all of Joppa, and many came to believe in the Lord."
    },
    "42": {
      "L": "And he remained many days in Joppa with a certain Simon, a tanner.",
      "M": "Peter stayed in Joppa for some time with a tanner named Simon.",
      "T": "Peter stayed on in Joppa for some time at the home of a man named Simon, a tanner."
    }
  },

  # ── CHAPTER 10 ─────────────────────────────────────────────────────────────
  "10": {
    "1": {
      "L": "Now there was a certain man in Caesarea named Cornelius, a centurion of the cohort called the Italian Cohort,",
      "M": "At Caesarea there was a man named Cornelius, a centurion in what was known as the Italian Regiment.",
      "T": "There was a man in Caesarea named Cornelius, a centurion in the regiment known as the Italian Cohort."
    },
    "2": {
      "L": "a devout man who feared God with all his household, who gave many alms to the people, and prayed to God always.",
      "M": "He and all his family were devout and God-fearing; he gave generously to those in need and prayed to God regularly.",
      "T": "He was a devout man who feared God, and so was his entire household. He gave generously to the poor and prayed to God continually."
    },
    "3": {
      "L": "He saw clearly in a vision, about the ninth hour of the day, an angel of God coming in to him and saying to him, 'Cornelius.'",
      "M": "One day at about three in the afternoon he had a vision. He distinctly saw an angel of God, who came to him and said, 'Cornelius!'",
      "T": "One afternoon around three o'clock he had a clear vision: an angel of God came to him and called his name—'Cornelius!'"
    },
    "4": {
      "L": "And he, gazing intently on him, and becoming afraid, said, 'What is it, Lord?' And he said to him, 'Your prayers and your alms have gone up for a memorial before God.'",
      "M": "Cornelius stared at him in fear. 'What is it, Lord?' he asked. The angel answered, 'Your prayers and gifts to the poor have come up as a memorial offering before God.'",
      "T": "Cornelius stared at him, filled with fear. 'What is it, Lord?' he asked. The angel said, 'Your prayers and your generosity to the poor have risen as a memorial offering into the very presence of God.'"
    },
    "5": {
      "L": "'And now send men to Joppa, and fetch one Simon, who is surnamed Peter;'",
      "M": "'Now send men to Joppa to bring back a man named Simon who is called Peter.'",
      "T": "'Now send men to Joppa to bring back a man named Simon—the one they call Peter.'"
    },
    "6": {
      "L": "'he is lodging with a certain Simon a tanner, whose house is by the sea.'",
      "M": "'He is staying with Simon the tanner, whose house is by the sea.'",
      "T": "'He is staying with Simon the tanner, whose house is right by the sea.'"
    },
    "7": {
      "L": "And when the angel who spoke to him had departed, he called two of his household servants and a devout soldier, one of those who waited on him,",
      "M": "When the angel who spoke to him had gone, Cornelius called two of his servants and a devout soldier who was one of his attendants.",
      "T": "When the angel had gone, Cornelius called two of his household servants and a devout soldier from his personal staff."
    },
    "8": {
      "L": "and having explained everything to them, he sent them to Joppa.",
      "M": "He told them everything that had happened and sent them to Joppa.",
      "T": "He explained everything to them and sent them to Joppa."
    },
    "9": {
      "L": "Now on the next day, as they were on their way and approaching the city, Peter went up on the rooftop to pray about the sixth hour.",
      "M": "About noon the following day as they were on their journey and approaching the city, Peter went up on the roof to pray.",
      "T": "The next day, as they were traveling and approaching the city, Peter went up to the roof to pray around midday."
    },
    "10": {
      "L": "And he became hungry and desired to eat; but while they were preparing, a trance fell on him,",
      "M": "He became hungry and wanted something to eat, and while the meal was being prepared, he fell into a trance.",
      "T": "He became hungry and wanted something to eat. While a meal was being prepared, he fell into a trance."
    },
    "11": {
      "L": "and he beholds heaven opened, and a certain vessel descending, as it were a great sheet, let down by four corners to the earth,",
      "M": "He saw heaven opened and something like a large sheet being let down to earth by its four corners.",
      "T": "He saw heaven opened, and something like a great sheet came down, lowered by its four corners toward the earth."
    },
    "12": {
      "L": "in which were all the four-footed beasts and creeping things of the earth and birds of heaven.",
      "M": "It contained all kinds of four-footed animals, as well as reptiles and birds.",
      "T": "In it were all kinds of four-footed animals and reptiles and birds of every sort."
    },
    "13": {
      "L": "And a voice came to him, 'Rise, Peter; kill and eat.'",
      "M": "Then a voice told him, 'Get up, Peter. Kill and eat.'",
      "T": "A voice said to him, 'Get up, Peter. Kill and eat!'"
    },
    "14": {
      "L": "'Surely not, Lord; for I have never eaten anything that is common and unclean.'",
      "M": "'Surely not, Lord!' Peter replied. 'I have never eaten anything impure or unclean.'",
      "T": "'Certainly not, Lord!' Peter said. 'I have never eaten anything ritually impure or unclean.'"
    },
    "15": {
      "L": "And a voice spoke to him again a second time, 'What God has cleansed, do not call common.'",
      "M": "The voice spoke to him a second time, 'Do not call anything impure that God has made clean.'",
      "T": "The voice spoke again: 'Do not call unclean what God has declared clean.'"
    },
    "16": {
      "L": "And this happened three times, and the vessel was immediately taken up into heaven.",
      "M": "This happened three times, and immediately the sheet was taken back to heaven.",
      "T": "This happened three times, and then the sheet was suddenly drawn back up into heaven."
    },
    "17": {
      "L": "Now while Peter was greatly perplexed within himself as to what the vision which he had seen might mean, behold, the men who had been sent by Cornelius, having found out Simon's house, stood at the gate",
      "M": "While Peter was wondering about the meaning of the vision, the men sent by Cornelius found out where Simon's house was and stopped at the gate.",
      "T": "While Peter was still puzzling over what the vision meant, the men Cornelius had sent arrived at Simon's gate."
    },
    "18": {
      "L": "and called out, asking whether Simon who is surnamed Peter was lodging there.",
      "M": "They called out, asking if Simon who was known as Peter was staying there.",
      "T": "They called out, asking whether Simon—the one they called Peter—was lodging there."
    },
    "19": {
      "L": "And while Peter was pondering the vision, the Spirit said to him, 'Behold, three men are seeking you;'",
      "M": "While Peter was still thinking about the vision, the Spirit said to him, 'Simon, three men are looking for you.'",
      "T": "As Peter was still turning the vision over in his mind, the Spirit said, 'Peter, three men are here looking for you.'"
    },
    "20": {
      "L": "'but arise, go down, and accompany them without hesitation, because I have sent them.'",
      "M": "'So get up and go downstairs. Do not hesitate to go with them, for I have sent them.'",
      "T": "'Get up, go downstairs, and go with them without any misgiving. I have sent them.'"
    },
    "21": {
      "L": "And Peter, going down to the men, said, 'Behold, I am the one you are seeking; what is the reason for which you have come?'",
      "M": "Peter went down and said to the men, 'I'm the one you're looking for. Why have you come?'",
      "T": "Peter went down and said to them, 'I'm the one you're looking for. What is this about?'"
    },
    "22": {
      "L": "And they said, 'Cornelius, a centurion, a righteous man and one who fears God, well spoken of by all the nation of the Jews, was directed by a holy angel to send for you to come to his house and to hear words from you.'",
      "M": "They replied, 'We have come from Cornelius the centurion. He is a righteous and God-fearing man, who is respected by all the Jewish people. A holy angel told him to ask you to come to his house so that he could hear what you have to say.'",
      "T": "'We come from Cornelius the centurion,' they said. 'He is a righteous man who fears God and is held in high regard by all the Jewish people. A holy angel instructed him to send for you and to invite you to his home to hear what you have to say.'"
    },
    "23": {
      "L": "Then calling them in, he lodged them. And on the next day he arose and went with them, and certain of the brothers from Joppa accompanied him.",
      "M": "Then Peter invited the men into the house to be his guests. The next day Peter started out with them, and some of the believers from Joppa went along.",
      "T": "Peter invited the men inside and gave them a place to stay. The next morning he set out with them, and several believers from Joppa went along."
    },
    "24": {
      "L": "And on the following day they entered Caesarea. And Cornelius was waiting for them, having called together his relatives and close friends.",
      "M": "The following day he arrived in Caesarea. Cornelius was expecting them and had called together his relatives and close friends.",
      "T": "The day after that they arrived in Caesarea. Cornelius had been expecting them and had gathered together his relatives and close friends."
    },
    "25": {
      "L": "And when Peter entered, Cornelius met him, falling at his feet, worshipped.",
      "M": "As Peter entered the house, Cornelius met him and fell at his feet in reverence.",
      "T": "As Peter entered the house, Cornelius came to meet him and fell down at his feet in worship."
    },
    "26": {
      "L": "But Peter raised him up, saying, 'Stand up; I myself am also a man.'",
      "M": "But Peter made him get up. 'Stand up,' he said, 'I am only a man myself.'",
      "T": "Peter pulled him to his feet. 'Get up,' he said. 'I'm just a human being like you.'"
    },
    "27": {
      "L": "And conversing with him, he went in and found many who had come together.",
      "M": "While talking with him, Peter went inside and found a large gathering of people.",
      "T": "Talking with Cornelius as he went in, Peter found a large crowd assembled."
    },
    "28": {
      "L": "And he said to them, 'You yourselves know how it is unlawful for a Jewish man to join himself to or come near a foreigner; and to me God has shown that I should call no man common or unclean.'",
      "M": "He said to them: 'You are well aware that it is against our law for a Jew to associate with or visit a Gentile. But God has shown me that I should not call anyone impure or unclean.'",
      "T": "'You all know,' Peter said, 'that it is not permitted for a Jew to associate with or enter the home of a Gentile. But God has shown me that I must not regard any person as impure or unclean.'"
    },
    "29": {
      "L": "'Therefore also I came without objection when I was sent for. I ask therefore for what reason you have sent for me.'",
      "M": "'So when I was sent for, I came without raising any objection. May I ask why you sent for me?'",
      "T": "'That is why I came without any hesitation when you sent for me. Now tell me—why did you send for me?'"
    },
    "30": {
      "L": "And Cornelius said, 'Four days ago until this hour, I was fasting and praying at the ninth hour in my house; and behold, a man stood before me in bright clothing,'",
      "M": "Cornelius answered: 'Three days ago I was in my house praying at this hour, at three in the afternoon. Suddenly a man in shining clothes stood before me'",
      "T": "Cornelius answered: 'Four days ago at this very hour—three in the afternoon—I was praying in my home when a man in gleaming clothing suddenly appeared before me.'"
    },
    "31": {
      "L": "'and he said, 'Cornelius, your prayer has been heard and your alms have been remembered before God.''",
      "M": "'and said, 'Cornelius, God has heard your prayer and remembered your gifts to the poor.''",
      "T": "'He said, 'Cornelius, your prayer has been heard and your generosity to the poor has been remembered before God.''"
    },
    "32": {
      "L": "'Send therefore to Joppa, and call Simon who is surnamed Peter; he is lodging in the house of Simon, a tanner, by the sea.'",
      "M": "''Send to Joppa for Simon who is called Peter. He is a guest in the home of Simon the tanner, who lives by the sea.''",
      "T": "''Send to Joppa and bring back Simon called Peter. He is staying in the home of Simon the tanner, right by the sea.''"
    },
    "33": {
      "L": "'At once therefore I sent to you; and you have done well in coming. Now therefore we are all here before God to hear all that you have been commanded by the Lord.'",
      "M": "'So I sent for you immediately, and it was good of you to come. Now we are all here in the presence of God to listen to everything the Lord has commanded you to tell us.'",
      "T": "'So I sent for you right away, and you have been good enough to come. Now here we all are—gathered in the presence of God—ready to hear everything the Lord has directed you to tell us.'"
    },
    "34": {
      "L": "And Peter opened his mouth and said, 'Of a truth I perceive that God is no respecter of persons,",
      "M": "Then Peter began to speak: 'I now realise how true it is that God does not show favouritism",
      "T": "Peter spoke up: 'I am beginning to grasp it fully now—God shows absolutely no partiality among people.'"
    },
    "35": {
      "L": "'but in every nation he who fears him and works righteousness is acceptable to him.'",
      "M": "'but accepts from every nation the one who fears him and does what is right.'",
      "T": "'In every nation, whoever fears him and does what is right is welcome before him.'"
    },
    "36": {
      "L": "'The word which he sent to the children of Israel, preaching the good news of peace through Jesus Christ—he is Lord of all—'",
      "M": "'You know the message God sent to the people of Israel, announcing the good news of peace through Jesus Christ, who is Lord of all.'",
      "T": "'You know the message God sent to the people of Israel—the good news of peace through Jesus the Messiah. He is Lord over everyone.'"
    },
    "37": {
      "L": "'the word which was proclaimed throughout all Judaea, and beginning from Galilee, after the baptism which John preached,'",
      "M": "'You know what has happened throughout the province of Judea, beginning in Galilee after the baptism that John preached—'",
      "T": "'You know what took place throughout Judea, beginning in Galilee after John proclaimed his baptism—'"
    },
    "38": {
      "L": "'how God anointed Jesus of Nazareth with the Holy Spirit and with power, who went about doing good and healing all who were oppressed by the devil, because God was with him.'",
      "M": "'how God anointed Jesus of Nazareth with the Holy Spirit and power, and how he went around doing good and healing all who were under the power of the devil, because God was with him.'",
      "T": "'—how God anointed Jesus of Nazareth with the Holy Spirit and with power, and how he went about doing good and setting free all who were oppressed by the devil, because God was with him.'"
    },
    "39": {
      "L": "'And we are witnesses of all things which he did, both in the country of the Jews and in Jerusalem; whom also they killed, hanging him on a tree.'",
      "M": "'We are witnesses of everything he did in the country of the Jews and in Jerusalem. They killed him by hanging him on a cross,'",
      "T": "'We are witnesses of everything he did in Judea and in Jerusalem. They put him to death by nailing him to a cross.'"
    },
    "40": {
      "L": "'God raised him up on the third day, and gave him to be made manifest,'",
      "M": "'but God raised him from the dead on the third day and caused him to be seen.'",
      "T": "'But God raised him from the dead on the third day and caused him to appear openly.'"
    },
    "41": {
      "L": "'not to all the people, but to witnesses who had been chosen before by God, even to us, who ate and drank with him after he rose from the dead.'",
      "M": "'He was not seen by all the people, but by witnesses whom God had already chosen—by us who ate and drank with him after he rose from the dead.'",
      "T": "'Not to all the people, but to witnesses God had chosen in advance—to us, who ate and drank with him after he rose from the dead.'"
    },
    "42": {
      "L": "'And he commanded us to preach to the people and to testify that he is the one ordained by God to be the Judge of the living and the dead.'",
      "M": "'He commanded us to preach to the people and to testify that he is the one whom God appointed as judge of the living and the dead.'",
      "T": "'He commanded us to proclaim to the people and to bear witness that he is the one God has appointed as judge over both the living and the dead.'"
    },
    "43": {
      "L": "'To him all the prophets bear witness, that through his name everyone who believes in him will receive remission of sins.'",
      "M": "'All the prophets testify about him that everyone who believes in him receives forgiveness of sins through his name.'",
      "T": "'Every one of the prophets testifies about him: that everyone who trusts in him receives the forgiveness of sins through his name.'"
    },
    "44": {
      "L": "While Peter was yet speaking these words, the Holy Spirit fell on all who heard the word.",
      "M": "While Peter was still speaking these words, the Holy Spirit came on all who heard the message.",
      "T": "Peter was still mid-sentence when the Holy Spirit fell on everyone who was listening to the message."
    },
    "45": {
      "L": "And the believers of the circumcision, as many as came with Peter, were astonished, because the gift of the Holy Spirit was poured out also on the Gentiles;",
      "M": "The circumcised believers who had come with Peter were astonished that the gift of the Holy Spirit had been poured out even on Gentiles.",
      "T": "The Jewish believers who had come with Peter were completely astonished: the gift of the Holy Spirit had been poured out even on the Gentiles."
    },
    "46": {
      "L": "for they heard them speaking with tongues and magnifying God. Then Peter answered,",
      "M": "For they heard them speaking in tongues and praising God. Then Peter said,",
      "T": "They could hear them speaking in tongues and declaring the greatness of God. Peter turned to the Jewish believers:"
    },
    "47": {
      "L": "'Can anyone forbid water, that these should not be baptized who have received the Holy Spirit as well as we?'",
      "M": "'Surely no one can stand in the way of their being baptised with water. They have received the Holy Spirit just as we have.'",
      "T": "'Can anyone refuse water for baptizing these people? They have received the Holy Spirit exactly as we did!'"
    },
    "48": {
      "L": "And he commanded them to be baptized in the name of Jesus Christ. Then they asked him to remain some days.",
      "M": "So he ordered that they be baptised in the name of Jesus Christ. Then they asked Peter to stay with them for a few days.",
      "T": "He directed that they be baptized in the name of Jesus the Messiah. Then they asked him to stay on with them for several days."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'acts')
        merge_tier(existing, ACTS, tier_key)
        save(tier_dir, 'acts', existing)
    print('Acts 6–10 written.')

if __name__ == '__main__':
    main()
