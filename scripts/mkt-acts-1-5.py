"""
MKT Acts chapters 1–5 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-acts-1-5.py

Translation decisions:
- πνεῦμα (Spirit): capitalised when referring to the Holy Spirit; lowercase for human spirit.
- κύριος (Lord): retained for both God and Jesus; context determines referent.
- Χριστός (Christ): "Christ" in L/M; "Anointed One" in T when emphasis falls on messianic office.
- ἐκκλησία: "assembly" (L), "church" (M), "community" (T) — avoids anachronistic ecclesiology in L.
- μετανοέω: "repent" (L/M), "turn back" or "change your ways" (T).
- ἄφεσις: "remission/release" (L), "forgiveness" (M/T).
- Joel 2 and Psalm 16/110 quotes preserved close to LXX in L; rendered as living speech in T.
- Aorist verbs rendered as simple completed acts; presents as ongoing states.
- Divine passive marked in L notes where relevant (done implicitly via rendering).
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
  # ── CHAPTER 1 ──────────────────────────────────────────────────────────────
  "1": {
    "1": {
      "L": "The former account I made, O Theophilus, concerning all things that Jesus began both to do and to teach,",
      "M": "In my former book, Theophilus, I wrote about all that Jesus began to do and to teach",
      "T": "In my first book, Theophilus, I told the story of everything Jesus began to do and to teach,"
    },
    "2": {
      "L": "until the day on which, having given commandments through the Holy Spirit to the apostles whom he had chosen, he was taken up.",
      "M": "until the day he was taken up to heaven, after giving instructions through the Holy Spirit to the apostles he had chosen.",
      "T": "right up to the day he was taken up to heaven. Before that, he gave his chosen apostles their commission through the Holy Spirit."
    },
    "3": {
      "L": "To whom also he presented himself alive after his suffering by many convincing proofs, appearing to them through forty days and speaking the things concerning the kingdom of God.",
      "M": "After his suffering, he presented himself to them and gave many convincing proofs that he was alive. He appeared to them over a period of forty days and spoke about the kingdom of God.",
      "T": "After his death he showed himself alive to them again and again over forty days, with unmistakable evidence. During that time he spoke about the reign of God."
    },
    "4": {
      "L": "And gathering together with them, he commanded them not to depart from Jerusalem but to wait for the promise of the Father, which, he said, 'you heard from me;'",
      "M": "On one occasion, while he was eating with them, he gave them this command: 'Do not leave Jerusalem, but wait for the gift my Father promised, which you have heard me speak about.'",
      "T": "While sharing a meal with them he told them, 'Don't leave Jerusalem yet. Stay and wait for what my Father has promised—the gift you heard me speak of.'"
    },
    "5": {
      "L": "for John indeed baptized with water, but you will be baptized with the Holy Spirit not many days from now.",
      "M": "'For John baptized with water, but in a few days you will be baptized with the Holy Spirit.'",
      "T": "'John immersed people in water, but within a few days you will be immersed in the Holy Spirit.'"
    },
    "6": {
      "L": "So then those who had gathered together asked him, saying, 'Lord, are you restoring the kingdom to Israel at this time?'",
      "M": "Then they gathered around him and asked, 'Lord, are you at this time going to restore the kingdom to Israel?'",
      "T": "The apostles were gathered around him and asked, 'Lord, is this the moment you are going to restore the kingdom to Israel?'"
    },
    "7": {
      "L": "And he said to them, 'It is not for you to know the times or the seasons which the Father has placed under his own authority;'",
      "M": "He said to them: 'It is not for you to know the times or dates the Father has set by his own authority.'",
      "T": "'That is not for you to know,' he told them. 'The Father has set those times and seasons by his own authority, and they are not yours to determine.'"
    },
    "8": {
      "L": "but you will receive power when the Holy Spirit has come upon you, and you will be my witnesses in Jerusalem, and in all Judaea and Samaria, and to the uttermost part of the earth.",
      "M": "'But you will receive power when the Holy Spirit comes on you; and you will be my witnesses in Jerusalem, and in all Judea and Samaria, and to the ends of the earth.'",
      "T": "'What you will receive is power—when the Holy Spirit comes upon you. And then you will be my witnesses: first in Jerusalem, then throughout Judea and Samaria, and finally to the very ends of the earth.'"
    },
    "9": {
      "L": "And when he had said these things, while they were watching, he was taken up, and a cloud received him out of their sight.",
      "M": "After he said this, he was taken up before their very eyes, and a cloud hid him from their sight.",
      "T": "When he had finished speaking, he was lifted up before their eyes, and a cloud carried him away out of their sight."
    },
    "10": {
      "L": "And while they were gazing intently into heaven as he went, behold, two men stood by them in white garments,",
      "M": "They were looking intently up into the sky as he was going, when suddenly two men dressed in white stood beside them.",
      "T": "They were still staring up into the sky when two men in dazzling white clothing suddenly appeared beside them."
    },
    "11": {
      "L": "who also said, 'Men of Galilee, why do you stand gazing into heaven? This same Jesus, who has been taken up from you into heaven, will come in the same way as you have seen him go into heaven.'",
      "M": "'Men of Galilee,' they said, 'why do you stand here looking into the sky? This same Jesus, who has been taken from you into heaven, will come back in the same way you have seen him go into heaven.'",
      "T": "'Galileans, why are you standing here staring into the sky?' they asked. 'This very same Jesus who has been taken from you into heaven will come back in exactly the same way you just watched him go.'"
    },
    "12": {
      "L": "Then they returned to Jerusalem from the mount called Olivet, which is near Jerusalem, a sabbath day's journey away.",
      "M": "Then the apostles returned to Jerusalem from the hill called the Mount of Olives, a Sabbath day's walk from the city.",
      "T": "The apostles made their way back to Jerusalem from the Mount of Olives, which is just a short walk from the city."
    },
    "13": {
      "L": "And when they had entered, they went up to the upper room where they were staying: both Peter and John and James and Andrew, Philip and Thomas, Bartholomew and Matthew, James the son of Alphaeus and Simon the Zealot, and Judas the son of James.",
      "M": "When they arrived, they went upstairs to the room where they were staying. Those present were Peter, John, James and Andrew; Philip and Thomas, Bartholomew and Matthew; James son of Alphaeus and Simon the Zealot, and Judas son of James.",
      "T": "Once inside the city, they went up to the upper room where they had been staying. The whole company was there: Peter and John, James and Andrew, Philip and Thomas, Bartholomew and Matthew, James son of Alphaeus and Simon the Zealot, and Judas son of James."
    },
    "14": {
      "L": "These all were continuing with one accord in prayer and supplication, together with the women and Mary the mother of Jesus, and his brothers.",
      "M": "They all joined together constantly in prayer, along with the women and Mary the mother of Jesus, and with his brothers.",
      "T": "All of them were united in heart and devoted themselves to prayer together—the apostles, several women including Mary the mother of Jesus, and his brothers."
    },
    "15": {
      "L": "And in those days Peter stood up in the midst of the brothers—the number of names together was about one hundred and twenty—and said,",
      "M": "In those days Peter stood up among the believers—a group numbering about a hundred and twenty—and said,",
      "T": "During this time, with about a hundred and twenty gathered together, Peter stood up to address them."
    },
    "16": {
      "L": "'Brothers, it was necessary for the scripture to be fulfilled, which the Holy Spirit spoke before through the mouth of David concerning Judas, who became a guide to those who arrested Jesus;'",
      "M": "'Brothers and sisters, the Scripture had to be fulfilled in which the Holy Spirit spoke long ago through David concerning Judas, who served as guide for those who arrested Jesus.'",
      "T": "'Friends,' he began, 'the scripture had to be fulfilled—the one the Holy Spirit spoke through David about Judas, who led those who arrested Jesus.'"
    },
    "17": {
      "L": "for he was counted among us and received his share in this ministry.",
      "M": "He was one of our number and shared in our ministry.",
      "T": "Judas was one of us and had his own part in this work."
    },
    "18": {
      "L": "(This man acquired a field with the reward of his iniquity; and falling headlong, he burst open in the middle and all his bowels gushed out.",
      "M": "(With the payment he received for his wickedness, Judas bought a field; there he fell headlong, his body burst open and all his intestines spilled out.",
      "T": "(With the money he received for his treachery, Judas purchased a field. He fell there face first, and his body split open, spilling out his insides."
    },
    "19": {
      "L": "And it became known to all the inhabitants of Jerusalem; so that field was called in their own language Akeldama, that is, Field of Blood.)",
      "M": "Everyone in Jerusalem heard about this, so they called that field in their language Akeldama, that is, Field of Blood.)",
      "T": "Everyone in Jerusalem heard about it, which is why that field came to be called in Aramaic 'Akeldama'—the Field of Blood.)"
    },
    "20": {
      "L": "'For it is written in the Book of Psalms: 'Let his dwelling become desolate, and let no one dwell in it'; and 'Let another take his office.''",
      "M": "'For,' said Peter, 'it is written in the Book of Psalms: 'May his place be deserted; let there be no one to dwell in it,' and, 'May another take his place of leadership.''",
      "T": "'The Psalms foretold this,' Peter continued. 'One passage reads, 'Let his house stand empty—no one to live in it.' Another says, 'Let someone else take over his office.''"
    },
    "21": {
      "L": "'Therefore, of the men who accompanied us during all the time that the Lord Jesus went in and out among us,'",
      "M": "'Therefore it is necessary to choose one of the men who have been with us the whole time the Lord Jesus was living among us,'",
      "T": "'So we need to choose someone who was with us throughout the Lord Jesus's public ministry—'"
    },
    "22": {
      "L": "'beginning from the baptism of John, until the day that he was taken up from us—one of these must become a witness with us of his resurrection.'",
      "M": "'beginning from John's baptism to the time when Jesus was taken up from us. For one of these must become a witness with us of his resurrection.'",
      "T": "'—from John's baptism all the way to the day Jesus was taken from us. Someone who can join us as a witness to his resurrection.'"
    },
    "23": {
      "L": "And they put forward two: Joseph called Barsabbas, who was surnamed Justus, and Matthias.",
      "M": "So they nominated two men: Joseph called Barsabbas (also known as Justus) and Matthias.",
      "T": "They put forward two names: Joseph Barsabbas (also called Justus) and Matthias."
    },
    "24": {
      "L": "And they prayed and said, 'Lord, you who know the hearts of all, show which one of these two you have chosen,'",
      "M": "Then they prayed, 'Lord, you know everyone's heart. Show us which of these two you have chosen'",
      "T": "Then they prayed together: 'Lord, you see into every heart. Show us which of these two you have already chosen—'"
    },
    "25": {
      "L": "'to take the place in this ministry and apostleship from which Judas fell away to go to his own place.'",
      "M": "'to take over this apostolic ministry, which Judas left to go where he belongs.'",
      "T": "'—to step into the apostolic role that Judas abandoned when he went to his proper end.'"
    },
    "26": {
      "L": "And they cast lots for them, and the lot fell on Matthias, and he was numbered with the eleven apostles.",
      "M": "Then they cast lots, and the lot fell to Matthias; so he was added to the eleven apostles.",
      "T": "They cast lots, and Matthias was chosen. He was enrolled with the eleven apostles."
    }
  },

  # ── CHAPTER 2 ──────────────────────────────────────────────────────────────
  "2": {
    "1": {
      "L": "And when the day of Pentecost was being fulfilled, they were all together in one place.",
      "M": "When the day of Pentecost came, they were all together in one place.",
      "T": "When the day of Pentecost arrived, all the believers were gathered in one place."
    },
    "2": {
      "L": "And suddenly there came from heaven a sound as of a rushing mighty wind, and it filled the whole house where they were sitting.",
      "M": "Suddenly a sound like the blowing of a violent wind came from heaven and filled the whole house where they were sitting.",
      "T": "Without warning a sound like a roaring gale swept down from heaven and filled the entire house where they were sitting."
    },
    "3": {
      "L": "And there appeared to them tongues as of fire, distributing themselves, and it sat upon each one of them.",
      "M": "They saw what seemed to be tongues of fire that separated and came to rest on each of them.",
      "T": "What looked like tongues of fire appeared and spread out, settling on each person in the room."
    },
    "4": {
      "L": "And they were all filled with the Holy Spirit and began to speak with other tongues, as the Spirit was giving them utterance.",
      "M": "All of them were filled with the Holy Spirit and began to speak in other tongues as the Spirit enabled them.",
      "T": "Every one of them was filled with the Holy Spirit and began speaking in languages they had never learned—the Spirit was giving them the words."
    },
    "5": {
      "L": "Now there were dwelling in Jerusalem Jews, devout men, from every nation under heaven.",
      "M": "Now there were staying in Jerusalem God-fearing Jews from every nation under heaven.",
      "T": "Jerusalem was full of devout Jewish pilgrims who had come from every corner of the earth."
    },
    "6": {
      "L": "And when this sound occurred, the multitude came together and were bewildered, because each one heard them speaking in his own language.",
      "M": "When they heard this sound, a crowd came together in bewilderment, because each one heard their own language being spoken.",
      "T": "When the sound broke out, a crowd gathered, completely baffled—each person was hearing their own native language spoken."
    },
    "7": {
      "L": "And they were all amazed and marvelled, saying, 'Behold, are not all these who are speaking Galileans?'",
      "M": "Utterly amazed, they asked: 'Aren't all these who are speaking Galileans?'",
      "T": "They were dumbfounded. 'Aren't all these people Galileans?' they said to each other."
    },
    "8": {
      "L": "'And how do we hear, each of us, in our own language in which we were born?'",
      "M": "'Then how is it that each of us hears them in our native language?'",
      "T": "'Then how is it that every one of us hears them speaking in the very language we grew up with?'"
    },
    "9": {
      "L": "'Parthians and Medes and Elamites and those dwelling in Mesopotamia, both Judaea and Cappadocia, Pontus and Asia,'",
      "M": "'Parthians, Medes and Elamites; residents of Mesopotamia, Judea and Cappadocia, Pontus and Asia,'",
      "T": "'We're here from Parthia, Media, Elam, Mesopotamia, Judea and Cappadocia, Pontus and the province of Asia,'"
    },
    "10": {
      "L": "'both Phrygia and Pamphylia, Egypt and the parts of Libya toward Cyrene, and visitors from Rome, both Jews and proselytes,'",
      "M": "'Phrygia and Pamphylia, Egypt and the parts of Libya near Cyrene; visitors from Rome (both Jews and converts to Judaism);'",
      "T": "'Phrygia and Pamphylia, Egypt and the parts of Libya around Cyrene, visitors from Rome—Jewish and Gentile converts alike—'"
    },
    "11": {
      "L": "'Cretans and Arabians—we hear them speaking in our own tongues the mighty deeds of God.'",
      "M": "'Cretans and Arabs—we hear them declaring the wonders of God in our own tongues!'",
      "T": "'Cretans and Arabs. And all of us are hearing them declare the mighty works of God in our own languages!'"
    },
    "12": {
      "L": "And they were all amazed and greatly perplexed, saying one to another, 'What does this mean?'",
      "M": "Amazed and perplexed, they asked one another, 'What does this mean?'",
      "T": "They were all stunned and confused, asking each other, 'What on earth is happening?'"
    },
    "13": {
      "L": "But others mocking said, 'They are full of new wine.'",
      "M": "Some, however, made fun of them and said, 'They have had too much wine.'",
      "T": "But some in the crowd sneered, 'They've just had too much to drink.'"
    },
    "14": {
      "L": "But Peter, standing up with the eleven, lifted up his voice and declared to them: 'Men of Judaea and all you who dwell in Jerusalem, let this be known to you, and listen to my words.'",
      "M": "Then Peter stood up with the Eleven, raised his voice and addressed the crowd: 'Fellow Jews and all of you who live in Jerusalem, let me explain this to you; listen carefully to what I say.'",
      "T": "Peter stood up with the eleven apostles, raised his voice, and spoke to the crowd: 'Listen, all of you—Jewish people and residents of Jerusalem alike. Let me explain what you are seeing.'"
    },
    "15": {
      "L": "'For these men are not drunk as you suppose, for it is the third hour of the day;'",
      "M": "'These people are not drunk, as you suppose. It's only nine in the morning!'",
      "T": "'These people are not drunk. It is only nine o'clock in the morning!'"
    },
    "16": {
      "L": "'but this is what was spoken through the prophet Joel:'",
      "M": "'No, this is what was spoken by the prophet Joel:'",
      "T": "'What you are seeing is the fulfilment of what the prophet Joel announced:'"
    },
    "17": {
      "L": "'And it shall come to pass in the last days, says God, that I will pour out from my Spirit upon all flesh; and your sons and your daughters shall prophesy, and your young men shall see visions, and your old men shall dream dreams;'",
      "M": "''In the last days, God says, I will pour out my Spirit on all people. Your sons and daughters will prophesy, your young men will see visions, your old men will dream dreams.''",
      "T": "''In the final days,' God says, 'I will pour out my Spirit on every kind of person. Your sons and daughters will speak God's word. Your young men will have visions. Your old men will dream prophetic dreams.''"
    },
    "18": {
      "L": "'Even upon my servants and upon my handmaidens in those days I will pour out from my Spirit, and they shall prophesy;'",
      "M": "''Even on my servants, both men and women, I will pour out my Spirit in those days, and they will prophesy.''",
      "T": "''Yes, even on my servants—men and women both—I will pour out my Spirit in those days, and they will speak my word.''"
    },
    "19": {
      "L": "'And I will give wonders in the heaven above and signs in the earth beneath: blood and fire and vapour of smoke;'",
      "M": "''I will show wonders in the heavens above and signs on the earth below, blood and fire and billows of smoke.''",
      "T": "''I will display wonders in the sky above and signs on the earth below: blood, fire, and columns of smoke.''"
    },
    "20": {
      "L": "'The sun shall be turned into darkness and the moon into blood, before the great and notable day of the Lord comes;'",
      "M": "''The sun will be turned to darkness and the moon to blood before the coming of the great and glorious day of the Lord.''",
      "T": "''The sun will go dark and the moon will turn blood-red before the great and glorious Day of the Lord arrives.''"
    },
    "21": {
      "L": "'And it shall come to pass that everyone who calls on the name of the Lord shall be saved.'",
      "M": "''And everyone who calls on the name of the Lord will be saved.''",
      "T": "''And everyone who calls on the name of the Lord will be rescued.''"
    },
    "22": {
      "L": "'Men of Israel, hear these words: Jesus of Nazareth, a man attested to you by God with mighty deeds and wonders and signs which God did through him in your midst, as you yourselves know—'",
      "M": "'Fellow Israelites, listen to this: Jesus of Nazareth was a man accredited by God to you through miracles, wonders and signs, which God did among you through him, as you yourselves know.'",
      "T": "'People of Israel, hear me out. Jesus of Nazareth was validated before you by God himself—through the miracles, wonders, and signs that God performed through him in your own presence. You saw this with your own eyes.'"
    },
    "23": {
      "L": "'this man, delivered up by the determined counsel and foreknowledge of God, you have taken, and by the hands of lawless men have crucified and killed—'",
      "M": "'This man was handed over to you by God's deliberate plan and foreknowledge; and you, with the help of wicked men, put him to death by nailing him to the cross.'",
      "T": "'This very man was handed over to you according to God's own set plan and foreknowledge—and you had him killed by nailing him to a cross through the hands of godless people.'"
    },
    "24": {
      "L": "'whom God raised up, having loosed the pains of death, because it was not possible for him to be held by it.'",
      "M": "'But God raised him from the dead, freeing him from the agony of death, because it was impossible for death to keep its hold on him.'",
      "T": "'But God raised him from the dead, releasing him from the grip of death—for death simply could not hold him.'"
    },
    "25": {
      "L": "'For David says concerning him: 'I foresaw the Lord always before my face, for he is at my right hand, that I should not be shaken.''",
      "M": "'David said about him: 'I saw the Lord always before me. Because he is at my right hand, I will not be shaken.''",
      "T": "'David spoke of him when he wrote: 'I kept the Lord always in my sight; with him at my right hand I cannot be moved.''"
    },
    "26": {
      "L": "'Therefore my heart was glad and my tongue rejoiced; moreover also my flesh will rest in hope;",
      "M": "''Therefore my heart is glad and my tongue rejoices; my body also will rest in hope,''",
      "T": "''So my heart is full of joy, and my words pour out in praise; my very body rests secure in hope.''"
    },
    "27": {
      "L": "'because you will not abandon my soul to Hades, nor will you give your Holy One to see corruption.",
      "M": "''because you will not abandon me to the realm of the dead, you will not let your holy one see decay.''",
      "T": "''For you will not leave me in the realm of the dead, nor will you let your Faithful One rot in the grave.''"
    },
    "28": {
      "L": "'You have made known to me the ways of life; you will make me full of gladness with your presence.",
      "M": "''You have made known to me the paths of life; you will fill me with joy in your presence.''",
      "T": "''You have shown me the road that leads to life; in your presence there is joy beyond measure.''"
    },
    "29": {
      "L": "'Brothers, I may speak freely to you concerning the patriarch David, that he both died and was buried, and his tomb is with us to this day.'",
      "M": "'Fellow Israelites, I can tell you confidently that the patriarch David died and was buried, and his tomb is here to this day.'",
      "T": "'Friends, I can say this openly: David died, was buried, and his tomb is right here in our city to this day.'"
    },
    "30": {
      "L": "'Therefore, being a prophet and knowing that God had sworn with an oath to him that of the fruit of his loins he would set one upon his throne,'",
      "M": "'But he was a prophet and knew that God had promised him on oath that he would place one of his descendants on his throne.'",
      "T": "'But David was a prophet. He knew that God had sworn an oath to seat one of his own descendants on his throne.'"
    },
    "31": {
      "L": "'seeing this beforehand, he spoke of the resurrection of the Christ: that neither was he abandoned to Hades, nor did his flesh see corruption.'",
      "M": "'Seeing what was to come, he spoke of the resurrection of the Messiah, that he was not abandoned to the realm of the dead, nor did his body see decay.'",
      "T": "'Seeing ahead to that day, David spoke about the resurrection of the Anointed One—he would not be abandoned to the grave, his body would not decay.'"
    },
    "32": {
      "L": "'This Jesus God raised up, of which we all are witnesses.'",
      "M": "'God has raised this Jesus to life, and we are all witnesses of it.'",
      "T": "'God raised this very Jesus from the dead, and every one of us standing here can vouch for it.'"
    },
    "33": {
      "L": "'Therefore, being exalted to the right hand of God, and having received from the Father the promise of the Holy Spirit, he has poured out this which you both see and hear.'",
      "M": "'Exalted to the right hand of God, he has received from the Father the promised Holy Spirit and has poured out what you now see and hear.'",
      "T": "'Now exalted to God's right hand, he received from the Father the promised Holy Spirit and has poured out what you are seeing and hearing right now.'"
    },
    "34": {
      "L": "'For David did not ascend into the heavens; but he himself says: 'The Lord said to my Lord, Sit at my right hand,''",
      "M": "'For David did not ascend to heaven, and yet he said, 'The Lord said to my Lord: Sit at my right hand''",
      "T": "'David himself never ascended to heaven—yet he wrote: 'The Lord said to my Lord: Sit at my right hand.''"
    },
    "35": {
      "L": "'until I make your enemies a footstool for your feet.",
      "M": "''until I make your enemies a footstool for your feet.''",
      "T": "''I will make your enemies a footstool under your feet.''"
    },
    "36": {
      "L": "'Therefore let all the house of Israel know assuredly that God has made both Lord and Christ this Jesus, whom you crucified.'",
      "M": "'Therefore let all Israel be assured of this: God has made this Jesus, whom you crucified, both Lord and Messiah.'",
      "T": "'So let all Israel know beyond any doubt: God has made this man—the one you crucified—both Lord and Anointed King.'"
    },
    "37": {
      "L": "Now when they heard this, they were pierced to the heart, and said to Peter and to the rest of the apostles, 'Brothers, what shall we do?'",
      "M": "When the people heard this, they were cut to the heart and said to Peter and the other apostles, 'Brothers, what shall we do?'",
      "T": "These words hit home. The crowd was cut to the heart and cried out to Peter and the other apostles, 'Brothers, what must we do?'"
    },
    "38": {
      "L": "And Peter said to them, 'Repent, and be baptized, every one of you, in the name of Jesus Christ for the remission of your sins, and you will receive the gift of the Holy Spirit.'",
      "M": "Peter replied, 'Repent and be baptized, every one of you, in the name of Jesus Christ for the forgiveness of your sins. And you will receive the gift of the Holy Spirit.'",
      "T": "'Turn back to God,' Peter answered, 'and be immersed in the name of Jesus the Messiah for the complete forgiveness of your sins. Then you will receive the Holy Spirit as a gift.'"
    },
    "39": {
      "L": "'For the promise is to you and to your children and to all those who are far off, as many as the Lord our God will call.'",
      "M": "'The promise is for you and your children and for all who are far off—for all whom the Lord our God will call.'",
      "T": "'This promise belongs to you and your children, and to all who are far away—as many as the Lord our God will call.'"
    },
    "40": {
      "L": "And with many other words he bore witness and exhorted them, saying, 'Save yourselves from this crooked generation.'",
      "M": "With many other words he warned them; and he pleaded with them, 'Save yourselves from this corrupt generation.'",
      "T": "Peter pressed on with many more arguments, urging them, 'Get out from under this twisted generation—be rescued!'"
    },
    "41": {
      "L": "So those who received his word were baptized, and there were added that day about three thousand souls.",
      "M": "Those who accepted his message were baptized, and about three thousand were added to their number that day.",
      "T": "Those who welcomed his message were baptized, and that single day about three thousand people joined their number."
    },
    "42": {
      "L": "And they were continuing steadfastly in the apostles' teaching and the fellowship, in the breaking of bread and the prayers.",
      "M": "They devoted themselves to the apostles' teaching and to fellowship, to the breaking of bread and to prayer.",
      "T": "These new believers devoted themselves completely to the apostles' teaching, to the shared life of the community, to the breaking of bread, and to prayer."
    },
    "43": {
      "L": "And awe came upon every soul, and many wonders and signs were being done through the apostles.",
      "M": "Everyone was filled with awe at the many wonders and signs performed by the apostles.",
      "T": "A deep sense of reverence settled over everyone. The apostles were performing many miraculous signs and wonders."
    },
    "44": {
      "L": "And all who believed were together and had all things in common;",
      "M": "All the believers were together and had everything in common.",
      "T": "All who believed stayed close to one another and held everything in common."
    },
    "45": {
      "L": "and they were selling their possessions and goods and distributing them to all, as anyone had need.",
      "M": "They sold property and possessions to give to anyone who had need.",
      "T": "They sold their property and belongings and shared the proceeds with anyone who was in need."
    },
    "46": {
      "L": "And day by day, continuing with one accord in the temple, and breaking bread from house to house, they were taking their food with gladness and singleness of heart,",
      "M": "Every day they continued to meet together in the temple courts. They broke bread in their homes and ate together with glad and sincere hearts,",
      "T": "Every single day they gathered together in the temple courts. They shared meals in each other's homes with overflowing joy and generous hearts,"
    },
    "47": {
      "L": "praising God and having favour with all the people. And the Lord was adding daily to their number those who were being saved.",
      "M": "praising God and enjoying the favour of all the people. And the Lord added to their number daily those who were being saved.",
      "T": "praising God and winning the goodwill of everyone around them. Every day the Lord was bringing more and more people into their community to be rescued."
    }
  },

  # ── CHAPTER 3 ──────────────────────────────────────────────────────────────
  "3": {
    "1": {
      "L": "Now Peter and John were going up together to the temple at the hour of prayer, the ninth hour.",
      "M": "One day Peter and John were going up to the temple at the time of prayer—at three in the afternoon.",
      "T": "One afternoon at three o'clock—the hour of prayer—Peter and John were on their way up to the temple."
    },
    "2": {
      "L": "And a man who was lame from his mother's womb was being carried, whom they placed daily at the gate of the temple which is called Beautiful, to ask alms from those entering into the temple.",
      "M": "Now a man who was lame from birth was being carried to the temple gate called Beautiful, where he was put every day to beg from those going into the temple courts.",
      "T": "A man who had been unable to walk since birth was being carried to the temple gate called Beautiful, where he was set down every day to beg from people entering the temple."
    },
    "3": {
      "L": "Seeing Peter and John about to go into the temple, he asked to receive alms.",
      "M": "When he saw Peter and John about to enter, he asked them for money.",
      "T": "When he saw Peter and John about to go in, he held out his hand for a donation."
    },
    "4": {
      "L": "And Peter, with John, fastening his eyes on him, said, 'Look at us.'",
      "M": "Peter looked straight at him, as did John. Then Peter said, 'Look at us!'",
      "T": "Peter fixed his gaze on the man, and John did the same. 'Look at us,' Peter said."
    },
    "5": {
      "L": "And he gave attention to them, expecting to receive something from them.",
      "M": "So the man gave them his attention, expecting to get something from them.",
      "T": "The man looked up eagerly, expecting money."
    },
    "6": {
      "L": "But Peter said, 'Silver and gold I do not have, but what I have I give to you: in the name of Jesus Christ the Nazarene, rise up and walk.'",
      "M": "Then Peter said, 'Silver or gold I do not have, but what I do have I give you. In the name of Jesus Christ of Nazareth, walk.'",
      "T": "'I have no silver or gold,' Peter said, 'but I'll give you what I do have. In the name of Jesus the Messiah of Nazareth—get up and walk.'"
    },
    "7": {
      "L": "And taking him by the right hand, he raised him up; and immediately his feet and his ankles received strength.",
      "M": "Taking him by the right hand, he helped him up, and instantly the man's feet and ankles became strong.",
      "T": "Peter grabbed his right hand and pulled him to his feet. Instantly the man's feet and ankles were made strong."
    },
    "8": {
      "L": "And leaping up, he stood and began to walk, and entered the temple with them, walking and leaping and praising God.",
      "M": "He jumped to his feet and began to walk. Then he went with them into the temple courts, walking and jumping, and praising God.",
      "T": "He sprang up, stood on his feet, and walked—then went into the temple with Peter and John, walking and leaping and praising God at the top of his voice."
    },
    "9": {
      "L": "And all the people saw him walking and praising God.",
      "M": "When all the people saw him walking and praising God,",
      "T": "Everyone in the temple courts saw him walking and heard him praising God."
    },
    "10": {
      "L": "And they recognized him, that he was the one who sat begging for alms at the Beautiful Gate of the temple; and they were filled with wonder and amazement at what had happened to him.",
      "M": "they recognized him as the same man who used to sit begging at the temple gate called Beautiful, and they were filled with wonder and amazement at what had happened to him.",
      "T": "They recognized him as the beggar who sat at the Beautiful Gate every day, and they were absolutely astonished at what had happened."
    },
    "11": {
      "L": "And as he was holding on to Peter and John, all the people ran together to them in the colonnade called Solomon's, greatly wondering.",
      "M": "While the man held on to Peter and John, all the people were astonished and came running to them in the place called Solomon's Colonnade.",
      "T": "The healed man stayed close to Peter and John, and a crowd came running toward them at Solomon's Porch, completely stunned."
    },
    "12": {
      "L": "But Peter, seeing this, answered the people, 'Men of Israel, why do you marvel at this? Or why do you gaze at us, as if by our own power or piety we had made him walk?'",
      "M": "When Peter saw this, he said to them: 'Fellow Israelites, why does this surprise you? Why do you stare at us as if by our own power or godliness we had made this man walk?'",
      "T": "Peter saw the crowd staring and addressed them: 'People of Israel, why are you so surprised? Why are you looking at us as if we healed this man by our own power or personal holiness?'"
    },
    "13": {
      "L": "'The God of Abraham and of Isaac and of Jacob, the God of our fathers, has glorified his servant Jesus, whom you delivered up and denied before the face of Pilate, when he had decided to release him.'",
      "M": "'The God of Abraham, Isaac and Jacob, the God of our fathers, has glorified his servant Jesus. You handed him over to be killed, and you disowned him before Pilate, though he had decided to let him go.'",
      "T": "'The God of Abraham, Isaac, and Jacob—the God of our ancestors—has glorified his servant Jesus. You handed him over to be killed. You rejected him in front of Pilate, even when Pilate was ready to release him.'"
    },
    "14": {
      "L": "'But you denied the Holy and Righteous One and asked for a murderer to be granted to you,",
      "M": "'You disowned the Holy and Righteous One and asked that a murderer be released to you.",
      "T": "'You rejected the Holy and Righteous One and demanded that a murderer be set free in his place.'"
    },
    "15": {
      "L": "'and you killed the Author of life, whom God raised from the dead, of which we are witnesses.'",
      "M": "'You killed the author of life, but God raised him from the dead. We are witnesses of this.'",
      "T": "'You killed the very Source of life. But God raised him from the dead—and we are here to testify to that.'"
    },
    "16": {
      "L": "'And on the basis of faith in his name, his name has made this man strong whom you see and know; and the faith that is through him has given him this complete soundness in the presence of you all.'",
      "M": "'By faith in the name of Jesus, this man whom you see and know was made strong. It is Jesus's name and the faith that comes through him that has completely healed him, as you can all see.'",
      "T": "'And it is through faith in Jesus's name that this man—whom you see and recognise—has been made completely well. The faith that comes through Jesus has restored him to full health right before your eyes.'"
    },
    "17": {
      "L": "'And now, brothers, I know that you acted in ignorance, as did also your rulers.'",
      "M": "'Now, fellow Israelites, I know that you acted in ignorance, as did your leaders.'",
      "T": "'Brothers and sisters, I understand that you and your leaders acted without fully knowing what you were doing.'"
    },
    "18": {
      "L": "'But what God foretold through the mouth of all the prophets, that his Christ would suffer, he has thus fulfilled.'",
      "M": "'But this is how God fulfilled what he had foretold through all the prophets, saying that his Messiah would suffer.'",
      "T": "'But this is exactly how God brought to pass what he had announced through all the prophets—that his Anointed One would suffer.'"
    },
    "19": {
      "L": "'Repent therefore and turn back, that your sins may be blotted out, that times of refreshing may come from the presence of the Lord,'",
      "M": "'Repent, then, and turn to God, so that your sins may be wiped out, that times of refreshing may come from the Lord,'",
      "T": "'So turn back to God, and turn away from your sins, so they can be completely wiped away. Then times of renewal will come from the presence of the Lord.'"
    },
    "20": {
      "L": "'and that he may send the Christ appointed beforehand for you—Jesus—'",
      "M": "'and that he may send the Messiah, who has been appointed for you—even Jesus.'",
      "T": "'He will then send Jesus, the Anointed One who was designated for you long ago.'"
    },
    "21": {
      "L": "'whom heaven must receive until the times of the restoration of all things, which God spoke of through the mouth of his holy prophets from of old.'",
      "M": "'Heaven must receive him until the time comes for God to restore everything, as he promised long ago through his holy prophets.'",
      "T": "'Heaven must hold him until the time when everything is restored to what God always intended—as he has declared through his holy prophets from the very beginning.'"
    },
    "22": {
      "L": "'Moses said: 'The Lord God will raise up for you a prophet like me from your brothers; you shall listen to him in everything he says to you.''",
      "M": "'For Moses said, 'The Lord your God will raise up for you a prophet like me from among your own people; you must listen to everything he tells you.''",
      "T": "'Moses himself said, 'God will raise up for you from your own people a prophet like me. You must obey everything he tells you.''"
    },
    "23": {
      "L": "'And it shall come to pass that every soul that does not hear that prophet shall be utterly destroyed from among the people.'",
      "M": "'Anyone who does not listen to him will be completely cut off from their people.'",
      "T": "'And anyone who refuses to listen to that prophet will be completely cut off from God's people.'"
    },
    "24": {
      "L": "'And indeed all the prophets from Samuel and those who follow, as many as have spoken, also announced these days.'",
      "M": "'Indeed, beginning with Samuel, all the prophets who have spoken have foretold these days.'",
      "T": "'Every prophet from Samuel onward spoke of these days that we are now living through.'"
    },
    "25": {
      "L": "'You are the sons of the prophets and of the covenant which God made with your fathers, saying to Abraham, 'And in your offspring all the families of the earth shall be blessed.''",
      "M": "'And you are heirs of the prophets and of the covenant God made with your fathers. He said to Abraham, 'Through your offspring all peoples on earth will be blessed.''",
      "T": "'You are the heirs of the prophets, and you share in the covenant God made with your ancestors. He told Abraham, 'Through your descendant every family on earth will receive blessing.''"
    },
    "26": {
      "L": "'To you first, God, having raised up his servant, sent him to bless you by turning every one of you from your wicked ways.'",
      "M": "'When God raised up his servant, he sent him first to you to bless you by turning each of you from your wicked ways.'",
      "T": "'God raised up his servant and sent him to you first—to bless you by turning each one of you away from your wickedness.'"
    }
  },

  # ── CHAPTER 4 ──────────────────────────────────────────────────────────────
  "4": {
    "1": {
      "L": "And as they were speaking to the people, the priests and the captain of the temple and the Sadducees came upon them,",
      "M": "The priests and the captain of the temple guard and the Sadducees came up to Peter and John while they were speaking to the people.",
      "T": "While Peter and John were still speaking to the crowd, the temple guards, the chief priests, and the Sadducees arrived."
    },
    "2": {
      "L": "greatly annoyed because they were teaching the people and proclaiming in Jesus the resurrection from the dead.",
      "M": "They were greatly disturbed because the apostles were teaching the people, proclaiming in Jesus the resurrection of the dead.",
      "T": "They were furious that Peter and John were teaching the crowds and announcing the resurrection of the dead—and claiming Jesus as proof of it."
    },
    "3": {
      "L": "And they laid hands on them and put them in custody until the next day, for it was already evening.",
      "M": "They seized Peter and John and, because it was evening, they put them in jail until the next day.",
      "T": "The officials arrested them and, since it was already evening, held them in custody overnight."
    },
    "4": {
      "L": "But many of those who heard the word believed, and the number of the men came to be about five thousand.",
      "M": "But many who heard the message believed; so the number of men who believed grew to about five thousand.",
      "T": "Even so, many who heard the message believed, and the number of men alone reached about five thousand."
    },
    "5": {
      "L": "And it came to pass on the next day that their rulers and elders and scribes were gathered together in Jerusalem,",
      "M": "The next day the rulers, the elders and the teachers of the law met in Jerusalem.",
      "T": "The following day, the ruling council—elders and religious scholars—gathered in Jerusalem."
    },
    "6": {
      "L": "and Annas the high priest was there, and Caiaphas and John and Alexander, and as many as were of the high priestly family.",
      "M": "Annas the high priest was there, and so were Caiaphas, John, Alexander and others of the high priest's family.",
      "T": "Annas the high priest was there, along with Caiaphas, John, Alexander, and all the members of the high-priestly families."
    },
    "7": {
      "L": "And when they had placed them in the midst, they inquired, 'By what power or by what name have you done this?'",
      "M": "They had Peter and John brought before them and began to question them: 'By what power or what name did you do this?'",
      "T": "They placed Peter and John before the assembly and questioned them: 'By whose power or authority did you do this?'"
    },
    "8": {
      "L": "Then Peter, filled with the Holy Spirit, said to them, 'Rulers of the people and elders of Israel,'",
      "M": "Then Peter, filled with the Holy Spirit, said to them: 'Rulers and elders of the people!'",
      "T": "Peter, filled with the Holy Spirit, addressed them: 'Rulers and elders of the people,'"
    },
    "9": {
      "L": "'if we this day are being examined about a good deed done to an impotent man, by what means he has been healed,'",
      "M": "'If we are being called to account today for an act of kindness shown to a man who was lame and are being asked how he was healed,'",
      "T": "'if we are on trial today for a good deed performed on a disabled man—if you want to know how he was healed—'"
    },
    "10": {
      "L": "'let it be known to you all and to all the people of Israel, that in the name of Jesus Christ the Nazarene, whom you crucified, whom God raised from the dead, in this name this man stands before you sound.'",
      "M": "'then know this, you and all the people of Israel: It is by the name of Jesus Christ of Nazareth, whom you crucified but whom God raised from the dead, that this man stands before you healed.'",
      "T": "'then let every one of you know this, and let all Israel know: this man stands before you completely healed through the name of Jesus the Messiah of Nazareth—the one you crucified, the one God raised from the dead.'"
    },
    "11": {
      "L": "'This is the stone which was rejected by you the builders, which has become the head of the corner.'",
      "M": "'Jesus is 'the stone you builders rejected, which has become the cornerstone.''",
      "T": "'He is the stone that you—the builders—threw aside, which has become the very cornerstone.'"
    },
    "12": {
      "L": "'And there is salvation in no other one, for there is no other name under heaven given among men by which we must be saved.'",
      "M": "'Salvation is found in no one else, for there is no other name under heaven given to mankind by which we must be saved.'",
      "T": "'There is rescue in no one else. Across the entire world there is no other name given to human beings by which we can be saved.'"
    },
    "13": {
      "L": "Now seeing the boldness of Peter and John, and perceiving that they were unlearned and untrained men, they marvelled; and they took knowledge of them, that they had been with Jesus.",
      "M": "When they saw the courage of Peter and John and realized that they were unschooled, ordinary men, they were astonished and they took note that these men had been with Jesus.",
      "T": "The council members were astonished at the boldness of Peter and John. These were clearly uneducated, ordinary men—yet they recognized them as those who had been with Jesus."
    },
    "14": {
      "L": "And seeing the man who had been healed standing with them, they had nothing to say against it.",
      "M": "But since they could see the man who had been healed standing there with them, there was nothing they could say.",
      "T": "But the healed man was standing right there beside them, and they had absolutely no argument to make."
    },
    "15": {
      "L": "But having commanded them to go outside the council, they conferred with one another,",
      "M": "So they ordered them to withdraw from the Sanhedrin and then conferred together.",
      "T": "They ordered Peter and John out of the chamber and began discussing among themselves."
    },
    "16": {
      "L": "saying, 'What shall we do to these men? For that a notable miracle has been done through them is evident to all who dwell in Jerusalem, and we cannot deny it.'",
      "M": "'What are we going to do with these men?' they asked. 'Everyone living in Jerusalem knows they have performed a notable sign, and we cannot deny it.'",
      "T": "'What do we do with these men?' they said. 'They have performed an undeniable miracle—everyone in Jerusalem knows it, and we cannot dispute the fact.'"
    },
    "17": {
      "L": "'But that it may spread no further among the people, let us warn them that they speak to no man any more in this name.'",
      "M": "'But to stop this thing from spreading any further among the people, we must warn them to speak no longer to anyone in this name.'",
      "T": "'To stop this spreading further, let us threaten them and forbid them from speaking in that name to anyone ever again.'"
    },
    "18": {
      "L": "And calling them, they commanded them not to speak at all nor to teach in the name of Jesus.",
      "M": "Then they called them in again and commanded them not to speak or teach at all in the name of Jesus.",
      "T": "They brought Peter and John back in and ordered them flatly: no more speaking or teaching in the name of Jesus."
    },
    "19": {
      "L": "But Peter and John answering said to them, 'Whether it is right in the sight of God to listen to you rather than to God, judge for yourselves;'",
      "M": "But Peter and John replied, 'Which is right in God's eyes: to listen to you, or to him? You be the judges!'",
      "T": "Peter and John looked at them and replied, 'You judge for yourselves whether it is right before God to obey you instead of God.'"
    },
    "20": {
      "L": "'for we are not able to stop speaking what we have seen and heard.'",
      "M": "'As for us, we cannot help speaking about what we have seen and heard.'",
      "T": "'As for us, we simply cannot stop talking about what we have seen and heard.'"
    },
    "21": {
      "L": "And when they had further threatened them, they released them, finding no means of punishing them because of the people, for all were glorifying God for what had happened.",
      "M": "After further threats they let them go. They could not decide how to punish them, because all the people were praising God for what had happened.",
      "T": "The council threatened them further and then let them go. They couldn't find any grounds to punish them, because all the people were praising God over what had happened."
    },
    "22": {
      "L": "For the man on whom this miracle of healing was performed was more than forty years old.",
      "M": "For the man who was miraculously healed was over forty years old.",
      "T": "The man who had been healed was over forty years old—he had lived his whole life unable to walk."
    },
    "23": {
      "L": "And being released, they went to their own and reported all that the chief priests and the elders had said to them.",
      "M": "On their release, Peter and John went back to their own people and reported all that the chief priests and the elders had said to them.",
      "T": "Once released, Peter and John returned to the community and reported everything the chief priests and elders had said."
    },
    "24": {
      "L": "And when they heard it, they lifted up their voice with one accord to God and said, 'Sovereign Lord, who made the heaven and the earth and the sea and all things that are in them,'",
      "M": "When they heard this, they raised their voices together in prayer to God. 'Sovereign Lord,' they said, 'you made the heavens and the earth and the sea, and everything in them.'",
      "T": "When the community heard the report, they all lifted their voices to God together: 'Sovereign Lord, you made heaven and earth, the sea, and everything in them.'"
    },
    "25": {
      "L": "'who through the mouth of our father David your servant said by the Holy Spirit: 'Why did the nations rage, and the peoples imagine vain things?''",
      "M": "'You spoke by the Holy Spirit through the mouth of your servant, our father David: 'Why do the nations rage and the peoples plot in vain?''",
      "T": "'Through your servant David you spoke by the Holy Spirit: 'Why do the nations rage? Why do the peoples make their futile plots?''"
    },
    "26": {
      "L": "'The kings of the earth took their stand, and the rulers were gathered together against the Lord and against his Christ.",
      "M": "''The kings of the earth rise up and the rulers band together against the Lord and against his anointed one.''",
      "T": "''The kings of the earth lined up and the rulers joined forces against the Lord and against his Anointed King.''"
    },
    "27": {
      "L": "'For truly in this city there were gathered together against your holy servant Jesus, whom you anointed, both Herod and Pontius Pilate with the Gentiles and the peoples of Israel,'",
      "M": "'Indeed Herod and Pontius Pilate met together with the Gentiles and the people of Israel in this very city to conspire against your holy servant Jesus, whom you anointed.'",
      "T": "'And that is exactly what happened here in this city: Herod and Pontius Pilate joined forces with the Gentiles and the people of Israel, all conspiring against your holy servant Jesus, the one you anointed.'"
    },
    "28": {
      "L": "'to do whatever your hand and your plan had predestined to occur.'",
      "M": "'They did what your power and will had decided beforehand should happen.'",
      "T": "'They did exactly what your power and wisdom had already determined would take place.'"
    },
    "29": {
      "L": "'And now, Lord, look upon their threats and grant to your servants to speak your word with all boldness,'",
      "M": "'Now, Lord, consider their threats and enable your servants to speak your word with great boldness.'",
      "T": "'And now, Lord, take note of their threats. Give your servants the courage to keep speaking your word without fear.'"
    },
    "30": {
      "L": "'while stretching out your hand to heal, and that signs and wonders may be done through the name of your holy servant Jesus.'",
      "M": "'Stretch out your hand to heal and perform signs and wonders through the name of your holy servant Jesus.'",
      "T": "'Stretch out your hand to heal, and let signs and wonders be done through the name of your holy servant Jesus.'"
    },
    "31": {
      "L": "And when they had prayed, the place where they were gathered together was shaken; and they were all filled with the Holy Spirit, and they spoke the word of God with boldness.",
      "M": "After they prayed, the place where they were meeting was shaken. And they were all filled with the Holy Spirit and spoke the word of God boldly.",
      "T": "When they finished praying, the room shook. They were all filled with the Holy Spirit and went on speaking God's word with fearless courage."
    },
    "32": {
      "L": "And the multitude of those who believed were of one heart and soul; and not one of them said that any of the things which he possessed was his own, but they had all things in common.",
      "M": "All the believers were one in heart and mind. No one claimed that any of their possessions was their own, but they shared everything they had.",
      "T": "The whole community of believers was one in heart and mind. No one regarded any of their possessions as their own—everything was shared."
    },
    "33": {
      "L": "And with great power the apostles gave their testimony concerning the resurrection of the Lord Jesus, and great grace was upon them all.",
      "M": "With great power the apostles continued to testify to the resurrection of the Lord Jesus. And God's grace was so powerfully at work in them all",
      "T": "With great power the apostles kept bearing witness to the resurrection of the Lord Jesus, and God's extraordinary grace was evident among all of them."
    },
    "34": {
      "L": "For there was not even one needy person among them; for as many as were owners of lands or houses were selling them, and bringing the proceeds of the things that were sold",
      "M": "that there were no needy persons among them. For from time to time those who owned land or houses sold them, brought the money from the sales",
      "T": "There was not a single person in need among them. Those who owned land or houses would sell them and bring the proceeds"
    },
    "35": {
      "L": "and laying them at the feet of the apostles; and distribution was made to each, according as anyone had need.",
      "M": "and put it at the apostles' feet, and it was distributed to anyone who had need.",
      "T": "and lay the money at the apostles' feet. It was then distributed to everyone according to their need."
    },
    "36": {
      "L": "And Joseph, who was surnamed by the apostles Barnabas (which is, being interpreted, Son of Encouragement), a Levite, a Cypriot by birth,",
      "M": "Joseph, a Levite from Cyprus, whom the apostles called Barnabas (which means 'son of encouragement'),",
      "T": "One example was Joseph, a Levite from Cyprus whom the apostles nicknamed Barnabas—which means 'Son of Encouragement.'"
    },
    "37": {
      "L": "having a field, sold it, and brought the money and laid it at the feet of the apostles.",
      "M": "sold a field he owned and brought the money and put it at the apostles' feet.",
      "T": "He sold a field he owned, brought all the money, and laid it at the apostles' feet."
    }
  },

  # ── CHAPTER 5 ──────────────────────────────────────────────────────────────
  "5": {
    "1": {
      "L": "But a certain man named Ananias, with his wife Sapphira, sold a possession,",
      "M": "Now a man named Ananias, together with his wife Sapphira, also sold a piece of property.",
      "T": "A man named Ananias and his wife Sapphira also sold some property."
    },
    "2": {
      "L": "and kept back a part of the price, his wife also being aware of it, and brought a certain part and laid it at the feet of the apostles.",
      "M": "With his wife's full knowledge he kept back part of the money for himself, but brought the rest and put it at the apostles' feet.",
      "T": "With his wife's full knowledge, he secretly kept back part of the proceeds for himself and brought only a portion, laying it at the apostles' feet as if it were the full amount."
    },
    "3": {
      "L": "But Peter said, 'Ananias, why has Satan filled your heart to lie to the Holy Spirit and to keep back part of the price of the land?'",
      "M": "Then Peter said, 'Ananias, how is it that Satan has so filled your heart that you have lied to the Holy Spirit and have kept for yourself some of the money you received for the land?'",
      "T": "Peter confronted him: 'Ananias, why have you let Satan fill your heart? You have lied to the Holy Spirit by holding back part of the price for yourself.'"
    },
    "4": {
      "L": "'While it remained, was it not your own? And after it was sold, was it not under your own authority? How is it that you have conceived this thing in your heart? You have not lied to men but to God.'",
      "M": "'Didn't it belong to you before it was sold? And after it was sold, wasn't the money at your disposal? What made you think of doing such a thing? You have not lied just to human beings but to God.'",
      "T": "'The land was yours to keep. Once sold, the money was yours to do with as you chose. Why did you plan this in your heart? You haven't deceived us—you have lied to God.'"
    },
    "5": {
      "L": "And hearing these words Ananias fell down and breathed his last. And great fear came upon all those who heard.",
      "M": "When Ananias heard this, he fell down and died. And great fear seized all who heard what had happened.",
      "T": "When Ananias heard those words, he collapsed and died. A deep and shaking fear came over everyone who heard about it."
    },
    "6": {
      "L": "And the young men arose and wrapped him up, and carrying him out, buried him.",
      "M": "Then some young men came forward, wrapped up his body, and carried him out and buried him.",
      "T": "Some of the younger men got up, wrapped his body, carried him out, and buried him."
    },
    "7": {
      "L": "And there was an interval of about three hours, and his wife, not knowing what had happened, came in.",
      "M": "About three hours later his wife came in, not knowing what had happened.",
      "T": "About three hours later, his wife came in, still unaware of what had happened."
    },
    "8": {
      "L": "And Peter answered her, 'Tell me, did you sell the land for so much?' And she said, 'Yes, for so much.'",
      "M": "Peter asked her, 'Tell me, is this the price you and Ananias got for the land?' 'Yes,' she said, 'that is the price.'",
      "T": "Peter asked her, 'Tell me—was that the full price you and Ananias received for the land?' 'Yes,' she said, 'that was the full price.'"
    },
    "9": {
      "L": "But Peter said to her, 'How is it that you agreed together to put the Spirit of the Lord to the test? Behold, the feet of those who buried your husband are at the door, and they will carry you out.'",
      "M": "Peter said to her, 'How could you conspire to test the Spirit of the Lord? Listen! The feet of the men who buried your husband are at the door, and they will carry you out also.'",
      "T": "'How could you and your husband agree to put the Spirit of the Lord to the test?' Peter said. 'Listen—the men who buried your husband are right at the door, and they will carry you out too.'"
    },
    "10": {
      "L": "And immediately she fell at his feet and breathed her last. And the young men came in and found her dead, and carrying her out, they buried her by her husband.",
      "M": "At that moment she fell down at his feet and died. Then the young men came in and, finding her dead, carried her out and buried her beside her husband.",
      "T": "She collapsed at his feet and died. The young men came in, found her dead, and buried her beside her husband."
    },
    "11": {
      "L": "And great fear came upon the whole assembly and upon all those who heard these things.",
      "M": "Great fear seized the whole church and all who heard about these events.",
      "T": "A holy fear gripped the entire community and everyone who heard what had happened."
    },
    "12": {
      "L": "And through the hands of the apostles many signs and wonders were being done among the people; and they were all with one accord in Solomon's Colonnade.",
      "M": "The apostles performed many signs and wonders among the people. And all the believers used to meet together in Solomon's Colonnade.",
      "T": "Through the apostles, many signs and wonders were taking place among the people. The believers all gathered regularly in Solomon's Porch."
    },
    "13": {
      "L": "And of the rest, no one dared to join himself to them, but the people magnified them,",
      "M": "No one else dared join them, even though they were highly regarded by the people.",
      "T": "No outsider dared approach them uninvited, yet the people held them in the highest regard."
    },
    "14": {
      "L": "and more than ever believers were being added to the Lord, multitudes both of men and women,",
      "M": "Nevertheless, more and more men and women believed in the Lord and were added to their number.",
      "T": "And more and more people—men and women alike—kept coming to faith in the Lord and joining their community."
    },
    "15": {
      "L": "so that they even brought the sick out into the streets and laid them on beds and pallets, that at the least the shadow of Peter passing by might fall on some of them.",
      "M": "As a result, people brought the sick into the streets and laid them on beds and mats so that at least Peter's shadow might fall on some of them as he passed by.",
      "T": "People even carried their sick out into the streets and laid them on mats and cots, hoping that even Peter's shadow might fall on some of them as he walked by."
    },
    "16": {
      "L": "And also the multitude from the cities around Jerusalem came together, bringing sick people and those troubled by unclean spirits, and they were being healed, every one.",
      "M": "Crowds gathered also from the towns around Jerusalem, bringing their sick and those tormented by impure spirits, and all of them were healed.",
      "T": "People also streamed in from the towns surrounding Jerusalem, bringing the sick and those tormented by evil spirits. Every single one of them was healed."
    },
    "17": {
      "L": "But the high priest rising up, and all those who were with him, which is the sect of the Sadducees, were filled with jealousy,",
      "M": "Then the high priest and all his associates, who were members of the party of the Sadducees, were filled with jealousy.",
      "T": "The high priest and all his associates—the Sadducees—were filled with burning jealousy."
    },
    "18": {
      "L": "and they laid hands on the apostles and put them in the public prison.",
      "M": "They arrested the apostles and put them in the public jail.",
      "T": "They arrested the apostles and threw them into the public prison."
    },
    "19": {
      "L": "But an angel of the Lord during the night opened the doors of the prison, and bringing them out, said,",
      "M": "But during the night an angel of the Lord opened the doors of the jail and brought them out.",
      "T": "But that night an angel of the Lord opened the prison doors and led them out, saying,"
    },
    "20": {
      "L": "'Go, stand and speak in the temple to the people all the words of this Life.'",
      "M": "'Go, stand in the temple courts,' he said, 'and tell the people all about this new life.'",
      "T": "'Go to the temple and stand there. Proclaim to the people everything about this Life.'"
    },
    "21": {
      "L": "And hearing this, they entered into the temple about daybreak and were teaching. But the high priest and those with him came and called the council together, even all the senate of the children of Israel, and sent to the prison to have them brought.",
      "M": "At daybreak they entered the temple courts, as they had been told, and began to teach the people. When the high priest and his associates arrived, they called together the Sanhedrin—the full assembly of the elders of Israel—and sent to the jail for the apostles.",
      "T": "At dawn they entered the temple and began teaching. Meanwhile the high priest and his associates arrived, convened the full council of Israel's elders, and sent officers to the prison to fetch the apostles."
    },
    "22": {
      "L": "But the officers who went did not find them in the prison; and they returned and reported,",
      "M": "But on arriving at the jail, the officers did not find them there. So they went back and reported,",
      "T": "But the officers arrived at the prison and found no one there. They returned and reported,"
    },
    "23": {
      "L": "saying, 'The prison we found shut with all safety and the guards standing at the doors, but opening it we found no one inside.'",
      "M": "'We found the jail securely locked, with the guards standing at the doors; but when we opened them, we found no one inside.'",
      "T": "'The prison was locked tight, guards were standing at every door—but when we opened it, there was no one inside.'"
    },
    "24": {
      "L": "Now when the captain of the temple and the chief priests heard these words, they were greatly perplexed about them, wondering what this might be.",
      "M": "On hearing this report, the captain of the temple guard and the chief priests were at a loss, wondering what this might lead to.",
      "T": "The temple captain and the chief priests heard this and were completely baffled—where could this lead?"
    },
    "25": {
      "L": "And someone came and reported to them, saying, 'Behold, the men whom you put in prison are standing in the temple and teaching the people.'",
      "M": "Then someone came and said, 'Look! The men you put in jail are standing in the temple courts teaching the people.'",
      "T": "Just then someone arrived with news: 'Look—the men you locked up are standing right there in the temple, teaching the people!'"
    },
    "26": {
      "L": "Then the captain went with the officers and brought them, not with force, for they feared the people, lest they should be stoned.",
      "M": "At that, the captain went with his officers and brought the apostles. They did not use force, because they feared that the people would stone them.",
      "T": "The captain went with his officers and brought the apostles back—but gently, without force, because they were afraid the crowd might stone them."
    },
    "27": {
      "L": "And bringing them, they set them before the council. And the high priest questioned them,",
      "M": "The apostles were brought in and made to appear before the Sanhedrin to be questioned by the high priest.",
      "T": "They brought the apostles in and made them stand before the full council. The high priest opened the questioning:"
    },
    "28": {
      "L": "saying, 'We strictly commanded you not to teach in this name, and behold, you have filled Jerusalem with your doctrine and intend to bring this man's blood upon us.'",
      "M": "'We gave you strict orders not to teach in this name,' he said. 'Yet you have filled Jerusalem with your teaching and are determined to make us guilty of this man's blood.'",
      "T": "'We gave you a clear and firm order not to teach in that name. Yet you have filled Jerusalem with your message and seem intent on making us responsible for this man's death.'"
    },
    "29": {
      "L": "But Peter and the apostles answering said, 'We must obey God rather than men.'",
      "M": "Peter and the other apostles replied: 'We must obey God rather than human beings!'",
      "T": "Peter and the apostles answered together: 'We must obey God rather than any human authority.'"
    },
    "30": {
      "L": "'The God of our fathers raised up Jesus, whom you killed by hanging on a tree.'",
      "M": "'The God of our ancestors raised Jesus from the dead—whom you killed by hanging him on a cross.'",
      "T": "'The God of our ancestors raised up Jesus—the very one you killed by hanging him on a tree.'"
    },
    "31": {
      "L": "'Him God exalted at his right hand as a Prince and a Saviour, to give repentance to Israel and remission of sins.'",
      "M": "'God exalted him to his own right hand as Prince and Saviour that he might bring Israel to repentance and forgive their sins.'",
      "T": "'God has raised him to his own right hand as Ruler and Rescuer—to bring Israel to a change of heart and to grant the forgiveness of sins.'"
    },
    "32": {
      "L": "'And we are witnesses of these things, and so is the Holy Spirit, whom God has given to those who obey him.'",
      "M": "'We are witnesses of these things, and so is the Holy Spirit, whom God has given to those who obey him.'",
      "T": "'We are witnesses to all of this, and so is the Holy Spirit—whom God gives to all who submit to him.'"
    },
    "33": {
      "L": "And hearing this, they were cut to the heart and were wanting to kill them.",
      "M": "When they heard this, they were furious and wanted to put them to death.",
      "T": "These words cut them to the quick. They were furious and wanted to execute the apostles on the spot."
    },
    "34": {
      "L": "But a certain Pharisee in the council named Gamaliel, a teacher of the law, held in honour by all the people, stood up and commanded that the men be put outside for a little while.",
      "M": "But a Pharisee named Gamaliel, a teacher of the law, who was honoured by all the people, stood up in the Sanhedrin and ordered that the men be put outside for a little while.",
      "T": "Then a Pharisee named Gamaliel, a respected teacher of the law, highly esteemed by everyone, stood up in the council. He ordered that the apostles be taken outside for a moment."
    },
    "35": {
      "L": "And he said to them, 'Men of Israel, take care as to what you are about to do to these men.'",
      "M": "Then he addressed the Sanhedrin: 'Men of Israel, consider carefully what you intend to do to these men.'",
      "T": "Then he addressed the council: 'Fellow Israelites, think very carefully about what you are about to do to these men.'"
    },
    "36": {
      "L": "'For before these days Theudas rose up, claiming to be somebody, and a number of men, about four hundred, joined him; who was slain, and all, as many as obeyed him, were scattered and came to nothing.'",
      "M": "'Some time ago Theudas appeared, claiming to be somebody, and about four hundred men rallied to him. He was killed, all his followers were dispersed, and it all came to nothing.'",
      "T": "'Remember Theudas? He came along not long ago claiming to be someone great, and about four hundred people followed him. He was killed, his followers scattered, and the whole movement evaporated.'"
    },
    "37": {
      "L": "'After this man, Judas the Galilean rose up in the days of the census and drew away people after him; he also perished, and all who obeyed him were scattered.'",
      "M": "'After him, Judas the Galilean appeared in the days of the census and led a band of people in revolt. He too was killed, and all his followers were scattered.'",
      "T": "'After him came Judas the Galilean, during the time of the census. He rallied a following behind him, and he too perished. All who followed him were scattered.'"
    },
    "38": {
      "L": "'And now I say to you, keep away from these men and let them be; for if this plan or this work is of men, it will be overthrown;'",
      "M": "'Therefore, in the present case I advise you: Leave these men alone! Let them go! For if their purpose or activity is of human origin, it will fail.'",
      "T": "'So here is my counsel: leave these men alone. Let them go. If this movement is merely human in origin, it will collapse on its own.'"
    },
    "39": {
      "L": "'but if it is of God, you will not be able to overthrow them; lest perhaps you be found even to be fighting against God.'",
      "M": "'But if it is from God, you will not be able to stop these men; you will only find yourselves fighting against God.'",
      "T": "'But if it is from God, you will not be able to stop it—and you may find yourselves at war with God himself.'"
    },
    "40": {
      "L": "And they were persuaded by him; and calling the apostles, having beaten them, they commanded them not to speak in the name of Jesus and released them.",
      "M": "His speech persuaded them. They called the apostles in and had them flogged. Then they ordered them not to speak in the name of Jesus, and let them go.",
      "T": "The council was persuaded. They brought the apostles back in, had them flogged, ordered them not to speak in the name of Jesus, and released them."
    },
    "41": {
      "L": "So they departed from the presence of the council, rejoicing that they were counted worthy to suffer dishonour for the Name.",
      "M": "The apostles left the Sanhedrin, rejoicing because they had been counted worthy of suffering disgrace for the Name.",
      "T": "The apostles walked out of the council chamber rejoicing—glad to have been found worthy of suffering shame for the sake of the Name."
    },
    "42": {
      "L": "And every day in the temple and from house to house they did not cease teaching and proclaiming Jesus as the Christ.",
      "M": "Day after day, in the temple courts and from house to house, they never stopped teaching and proclaiming the good news that Jesus is the Messiah.",
      "T": "Every day, in the temple and in home after home, they kept right on teaching and announcing the good news: Jesus is the Anointed One."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'acts')
        merge_tier(existing, ACTS, tier_key)
        save(tier_dir, 'acts', existing)
    print('Acts 1–5 written.')

if __name__ == '__main__':
    main()
