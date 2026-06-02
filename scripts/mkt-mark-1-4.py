"""
MKT Mark chapters 1-4 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-mark-1-4.py
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

MARK = {
  "1": {
    "1": {
      "L": "The beginning of the gospel of Jesus Christ, Son of God.",
      "M": "This is the beginning of the good news about Jesus Christ, the Son of God.",
      "T": "Here begins the good news about Jesus the Messiah, God's own Son."
    },
    "2": {
      "L": "As it is written in Isaiah the prophet: 'Behold, I send my messenger before your face, who will prepare your way,'",
      "M": "as it is written in the prophet Isaiah: 'I will send my messenger ahead of you, who will prepare your way—'",
      "T": "just as it was written by the prophet Isaiah: 'I am sending my messenger ahead of you to prepare the way before you—'"
    },
    "3": {
      "L": "'The voice of one crying in the wilderness: Prepare the way of the Lord, make his paths straight.'",
      "M": "'a voice of one calling in the wilderness, \"Prepare the way for the Lord, make straight paths for him.\"'",
      "T": "'a voice crying out in the wilderness: Make the way ready for the Lord! Straighten the paths before him!'"
    },
    "4": {
      "L": "John appeared, baptizing in the wilderness and proclaiming a baptism of repentance for the forgiveness of sins.",
      "M": "And so John the Baptist appeared in the wilderness, preaching a baptism of repentance for the forgiveness of sins.",
      "T": "John came on the scene in the wilderness, proclaiming a baptism of repentance as the way to receive forgiveness for sins."
    },
    "5": {
      "L": "And all the region of Judea and all the people of Jerusalem were going out to him and were being baptized by him in the Jordan River, confessing their sins.",
      "M": "The whole Judean countryside and all the people of Jerusalem went out to him. Confessing their sins, they were baptized by him in the Jordan River.",
      "T": "People came streaming out from all of Judea and from Jerusalem itself. They confessed their sins and were baptized by him in the Jordan River."
    },
    "6": {
      "L": "Now John was clothed with camel's hair and wore a leather belt around his waist and ate locusts and wild honey.",
      "M": "John wore clothing made of camel's hair, with a leather belt around his waist, and he ate locusts and wild honey.",
      "T": "John dressed in camel's hair with a leather belt around his waist, and he lived on locusts and wild honey."
    },
    "7": {
      "L": "And he preached, saying, 'After me comes one who is mightier than I, the strap of whose sandals I am not worthy to stoop down and untie.'",
      "M": "And this was his message: 'After me comes the one more powerful than I, whose sandal strap I am not worthy to stoop down and untie.'",
      "T": "His message was this: 'Someone far more powerful than I is coming after me—someone whose sandal strap I'm not even worthy to stoop down and untie.'"
    },
    "8": {
      "L": "'I baptized you with water, but he will baptize you with the Holy Spirit.'",
      "M": "'I baptize you with water, but he will baptize you with the Holy Spirit.'",
      "T": "'I have baptized you with water, but he will baptize you with the Holy Spirit.'"
    },
    "9": {
      "L": "In those days Jesus came from Nazareth of Galilee and was baptized by John in the Jordan.",
      "M": "At that time Jesus came from Nazareth in Galilee and was baptized by John in the Jordan.",
      "T": "About this time, Jesus came from Nazareth in Galilee and was baptized by John in the Jordan."
    },
    "10": {
      "L": "And immediately coming up out of the water, he saw the heavens torn open and the Spirit descending upon him like a dove.",
      "M": "Just as Jesus was coming up out of the water, he saw heaven being torn open and the Spirit descending on him like a dove.",
      "T": "The moment he came up out of the water, he saw the sky torn open and the Spirit coming down on him like a dove."
    },
    "11": {
      "L": "And a voice came out of the heavens: 'You are my beloved Son; in you I am well pleased.'",
      "M": "And a voice came from heaven: 'You are my Son, whom I love; with you I am well pleased.'",
      "T": "And a voice came from heaven: 'You are my Son, my own beloved—in you I delight.'"
    },
    "12": {
      "L": "And immediately the Spirit drove him out into the wilderness.",
      "M": "At once the Spirit sent him out into the wilderness.",
      "T": "Right away the Spirit drove him out into the wilderness."
    },
    "13": {
      "L": "And he was in the wilderness forty days, being tempted by Satan. And he was with the wild beasts, and the angels were ministering to him.",
      "M": "He was in the wilderness forty days, being tempted by Satan. He was with the wild animals, and angels attended him.",
      "T": "He spent forty days in the wilderness, tested by Satan throughout. He was there with the wild animals, and angels took care of him."
    },
    "14": {
      "L": "Now after John was handed over, Jesus came into Galilee, proclaiming the gospel of God,",
      "M": "After John was put in prison, Jesus went into Galilee, proclaiming the good news of God.",
      "T": "After John was arrested and handed over, Jesus went into Galilee announcing the good news from God:"
    },
    "15": {
      "L": "and saying, 'The time has been fulfilled and the kingdom of God has drawn near; repent and believe in the gospel.'",
      "M": "'The time has come,' he said. 'The kingdom of God has come near. Repent and believe the good news!'",
      "T": "'The time has arrived. God's kingdom is breaking in. Turn from sin and trust the good news!'"
    },
    "16": {
      "L": "And passing along the Sea of Galilee, he saw Simon and Andrew the brother of Simon casting a net into the sea, for they were fishermen.",
      "M": "As Jesus walked beside the Sea of Galilee, he saw Simon and his brother Andrew casting a net into the lake, for they were fishermen.",
      "T": "Walking along the shore of the Sea of Galilee, Jesus saw Simon and his brother Andrew casting their net into the water—they were fishermen."
    },
    "17": {
      "L": "And Jesus said to them, 'Come after me, and I will make you become fishers of men.'",
      "M": "'Come, follow me,' Jesus said, 'and I will send you out to fish for people.'",
      "T": "'Come, follow me,' Jesus said, 'and I will make you fishers of people.'"
    },
    "18": {
      "L": "And immediately they left their nets and followed him.",
      "M": "At once they left their nets and followed him.",
      "T": "Right then, they dropped their nets and followed him."
    },
    "19": {
      "L": "And going on a little farther, he saw James the son of Zebedee and John his brother, who were in the boat mending the nets.",
      "M": "When he had gone a little farther, he saw James son of Zebedee and his brother John in a boat, preparing their nets.",
      "T": "A little farther on he saw James son of Zebedee and his brother John. They were in their boat, mending the nets."
    },
    "20": {
      "L": "And immediately he called them, and leaving their father Zebedee in the boat with the hired servants, they followed him.",
      "M": "Without delay he called them, and they left their father Zebedee in the boat with the hired men and followed him.",
      "T": "He called them on the spot. They left their father Zebedee in the boat with the hired workers and went after Jesus."
    },
    "21": {
      "L": "And they went into Capernaum, and immediately on the Sabbath he entered the synagogue and began teaching.",
      "M": "They went to Capernaum, and when the Sabbath came, Jesus went into the synagogue and began to teach.",
      "T": "They went to Capernaum, and on the very next Sabbath Jesus went into the synagogue and began to teach."
    },
    "22": {
      "L": "And they were astonished at his teaching, for he was teaching them as one having authority, and not as the scribes.",
      "M": "The people were amazed at his teaching, because he taught them as one who had authority, not as the teachers of the law.",
      "T": "The people were stunned by his teaching, because he taught like someone with real authority—not like their usual Bible teachers."
    },
    "23": {
      "L": "And immediately there was in their synagogue a man with an unclean spirit. And he cried out,",
      "M": "Just then a man in their synagogue who was possessed by an impure spirit cried out,",
      "T": "At that moment, a man in the synagogue who was controlled by an evil spirit cried out,"
    },
    "24": {
      "L": "'What have you to do with us, Jesus of Nazareth? Have you come to destroy us? I know who you are—the Holy One of God.'",
      "M": "'What do you want with us, Jesus of Nazareth? Have you come to destroy us? I know who you are—the Holy One of God!'",
      "T": "'What do you want with us, Jesus of Nazareth? Have you come to destroy us? I know who you really are—the Holy One of God!'"
    },
    "25": {
      "L": "But Jesus rebuked him, saying, 'Be silent, and come out of him!'",
      "M": "'Be quiet!' said Jesus sternly. 'Come out of him!'",
      "T": "Jesus cut him off sharply: 'Silence! Come out of him!'"
    },
    "26": {
      "L": "And the unclean spirit, convulsing him and crying out with a loud voice, came out of him.",
      "M": "The impure spirit shook the man violently and came out of him with a shriek.",
      "T": "The evil spirit threw the man into convulsions, let out a loud shriek, and left him."
    },
    "27": {
      "L": "And they were all amazed, so that they discussed among themselves, saying, 'What is this? A new teaching with authority! He commands even the unclean spirits, and they obey him.'",
      "M": "The people were all so amazed that they asked each other, 'What is this? A new teaching—and with authority! He even gives orders to impure spirits and they obey him.'",
      "T": "Everyone was astonished. They kept asking each other, 'What is this? A brand-new kind of teaching—with real authority! He even orders evil spirits around, and they obey!'"
    },
    "28": {
      "L": "And immediately the report of him spread throughout all the surrounding region of Galilee.",
      "M": "News about him spread quickly over the whole region of Galilee.",
      "T": "Word about him spread like fire through every corner of Galilee."
    },
    "29": {
      "L": "And immediately, leaving the synagogue, he entered the house of Simon and Andrew, with James and John.",
      "M": "As soon as they left the synagogue, they went with James and John to the home of Simon and Andrew.",
      "T": "They left the synagogue and went straight to the home of Simon and Andrew, with James and John."
    },
    "30": {
      "L": "Now Simon's mother-in-law lay ill with a fever, and immediately they told him about her.",
      "M": "Simon's mother-in-law was in bed with a fever, and they immediately told Jesus about her.",
      "T": "Simon's mother-in-law was in bed, sick with a fever, and they told Jesus about her right away."
    },
    "31": {
      "L": "And he came and took her by the hand and raised her up, and the fever left her, and she began to serve them.",
      "M": "So he went to her, took her hand and helped her up. The fever left her and she began to wait on them.",
      "T": "He went to her, took her hand, and helped her up. The fever left her immediately, and she began serving them."
    },
    "32": {
      "L": "That evening, when the sun had set, they were bringing to him all who were sick or possessed by demons.",
      "M": "That evening after sunset the people brought to Jesus all the sick and demon-possessed.",
      "T": "At sunset that evening, people brought to Jesus everyone who was sick or controlled by evil spirits."
    },
    "33": {
      "L": "And the whole city was gathered together at the door.",
      "M": "The whole town gathered at the door.",
      "T": "The whole town crowded at the door."
    },
    "34": {
      "L": "And he healed many who were sick with various diseases, and cast out many demons. And he would not permit the demons to speak, because they knew him.",
      "M": "And Jesus healed many who had various diseases. He also drove out many demons, but he would not let the demons speak because they knew who he was.",
      "T": "Jesus healed many people suffering from all kinds of diseases and drove out many evil spirits. But he would not let the demons speak, because they knew who he was."
    },
    "35": {
      "L": "And rising very early in the morning, while it was still dark, he arose and went out to a desolate place, and there he was praying.",
      "M": "Very early in the morning, while it was still dark, Jesus got up, left the house and went off to a solitary place, where he prayed.",
      "T": "Long before daybreak, while it was still completely dark, Jesus got up and slipped away to a remote place to pray."
    },
    "36": {
      "L": "And Simon and those who were with him searched for him,",
      "M": "Simon and his companions went to look for him,",
      "T": "Simon and the others went searching for him."
    },
    "37": {
      "L": "and they found him and said to him, 'Everyone is looking for you.'",
      "M": "and when they found him, they exclaimed: 'Everyone is looking for you!'",
      "T": "When they found him, they said, 'Everyone is searching for you!'"
    },
    "38": {
      "L": "And he said to them, 'Let us go on to the neighboring towns, that I may preach there also, for that is why I came out.'",
      "M": "Jesus replied, 'Let us go somewhere else—to the nearby villages—so I can preach there also. That is why I have come.'",
      "T": "He said to them, 'Let's move on to the neighboring villages so I can proclaim the good news there too. That's what I came out to do.'"
    },
    "39": {
      "L": "And he went throughout all Galilee, preaching in their synagogues and casting out demons.",
      "M": "So he traveled throughout Galilee, preaching in their synagogues and driving out demons.",
      "T": "He traveled all across Galilee, preaching in their synagogues and driving out evil spirits."
    },
    "40": {
      "L": "And a leper came to him, imploring him, and kneeling said to him, 'If you will, you are able to make me clean.'",
      "M": "A man with leprosy came to him and begged him on his knees, 'If you are willing, you can make me clean.'",
      "T": "A man with leprosy came to him, fell on his knees, and begged, 'If you want to, you can make me clean.'"
    },
    "41": {
      "L": "And moved with compassion, he stretched out his hand and touched him and said to him, 'I will; be clean.'",
      "M": "Jesus was moved with compassion. He reached out his hand and touched the man. 'I am willing,' he said. 'Be clean!'",
      "T": "Filled with compassion, Jesus reached out and touched him. 'I want to,' he said. 'Be clean!'"
    },
    "42": {
      "L": "And immediately the leprosy left him, and he was made clean.",
      "M": "Immediately the leprosy left him and he was cleansed.",
      "T": "The leprosy disappeared immediately, and he was completely clean."
    },
    "43": {
      "L": "And sternly warning him, he sent him away immediately,",
      "M": "Jesus sent him away at once with a strong warning:",
      "T": "Jesus gave him strict orders and sent him off immediately:"
    },
    "44": {
      "L": "and said to him, 'See that you say nothing to anyone, but go, show yourself to the priest and offer for your cleansing what Moses commanded, as a testimony to them.'",
      "M": "'See that you don't tell this to anyone. But go, show yourself to the priest and offer the sacrifices that Moses commanded for your cleansing, as a testimony to them.'",
      "T": "'Don't say a word about this to anyone. Go straight to the priest, let him examine you, and offer the sacrifice Moses prescribed for your purification. That will be their official proof.'"
    },
    "45": {
      "L": "But he went out and began to proclaim it freely and to spread the word, so that Jesus could no longer openly enter a town, but was out in desolate places, and they were coming to him from every direction.",
      "M": "Instead he went out and began to talk freely, spreading the news. As a result, Jesus could no longer enter a town openly but stayed outside in lonely places. Yet the people still came to him from everywhere.",
      "T": "Instead the man went out and told everyone what had happened, spreading the story far and wide. As a result, Jesus could no longer enter any town publicly. He stayed out in remote areas—but people kept coming to him from every direction."
    }
  },
  "2": {
    "1": {
      "L": "And when he returned to Capernaum after some days, it was reported that he was in the house.",
      "M": "A few days later, when Jesus again entered Capernaum, the people heard that he had come home.",
      "T": "A few days later Jesus returned to Capernaum, and word spread that he was back in the house."
    },
    "2": {
      "L": "And many were gathered together, so that there was no more room, not even near the door. And he was speaking the word to them.",
      "M": "They gathered in such large numbers that there was no room left, not even outside the door, and he preached the word to them.",
      "T": "So many people crowded in that there wasn't any room left—not even near the doorway. He was teaching the word to them."
    },
    "3": {
      "L": "And they came, bringing to him a paralytic carried by four men.",
      "M": "Some men came, bringing to him a paralyzed man, carried by four of them.",
      "T": "Some men arrived, bringing a paralyzed man carried by four of his friends."
    },
    "4": {
      "L": "And when they were unable to bring him near to Jesus because of the crowd, they removed the roof above him, and having dug through, they let down the mat on which the paralytic was lying.",
      "M": "Since they could not get him to Jesus because of the crowd, they made an opening in the roof above Jesus by digging through it and then lowered the mat the man was lying on.",
      "T": "They couldn't get through the crowd to reach Jesus, so they went up on the roof and dug an opening through it. Then they lowered the paralyzed man on his mat right in front of Jesus."
    },
    "5": {
      "L": "And Jesus, seeing their faith, said to the paralytic, 'Child, your sins are forgiven.'",
      "M": "When Jesus saw their faith, he said to the paralyzed man, 'Son, your sins are forgiven.'",
      "T": "When Jesus saw their faith, he said to the paralyzed man, 'My son, your sins are forgiven.'"
    },
    "6": {
      "L": "Now some of the scribes were sitting there, reasoning in their hearts,",
      "M": "Now some teachers of the law were sitting there, thinking to themselves,",
      "T": "Some Bible teachers were sitting there, inwardly questioning:"
    },
    "7": {
      "L": "'Why does this man speak this way? He is blaspheming! Who is able to forgive sins but God alone?'",
      "M": "'Why does this fellow talk like that? He's blaspheming! Who can forgive sins but God alone?'",
      "T": "'How dare he say such a thing? That's blasphemy! Only God can forgive sins—who does he think he is?'"
    },
    "8": {
      "L": "And immediately Jesus, perceiving in his spirit that they were reasoning this way within themselves, said to them, 'Why do you reason these things in your hearts?'",
      "M": "Immediately Jesus knew in his spirit that this was what they were thinking in their hearts, and he said to them, 'Why are you thinking these things?'",
      "T": "Right away Jesus knew in his spirit what they were thinking, and he said to them, 'Why are you reasoning like this in your hearts?'"
    },
    "9": {
      "L": "'Which is easier, to say to the paralytic, \"Your sins are forgiven,\" or to say, \"Rise and take up your mat and walk\"?'",
      "M": "'Which is easier: to say to this paralyzed man, \"Your sins are forgiven,\" or to say, \"Get up, take your mat and walk\"?'",
      "T": "'Think about it—which is easier: to say \"Your sins are forgiven,\" or to say \"Get up, pick up your mat, and walk\"?'"
    },
    "10": {
      "L": "'But so that you may know that the Son of Man has authority on earth to forgive sins'—he said to the paralytic—",
      "M": "'But I want you to know that the Son of Man has authority on earth to forgive sins.' So he said to the man,",
      "T": "'But I want you to understand that the Son of Man has authority on earth to forgive sins.' Then he turned to the paralyzed man and said,"
    },
    "11": {
      "L": "'I say to you, rise, take up your mat and go to your home.'",
      "M": "'Get up, take your mat and go home.'",
      "T": "'Get up! Pick up your mat and go home!'"
    },
    "12": {
      "L": "And he rose and immediately picked up his mat and went out before them all, so that they were all amazed and glorified God, saying, 'We never saw anything like this!'",
      "M": "He got up, took his mat and walked out in full view of them all. This amazed everyone and they praised God, saying, 'We have never seen anything like this!'",
      "T": "The man stood up, grabbed his mat, and walked out right in front of everyone. They were all stunned and praised God: 'We have never seen anything like this!'"
    },
    "13": {
      "L": "He went out again beside the sea, and all the crowd came to him, and he was teaching them.",
      "M": "Once again Jesus went out beside the lake. A large crowd came to him, and he began to teach them.",
      "T": "Jesus went out again to the lakeshore. A large crowd gathered around him, and he taught them."
    },
    "14": {
      "L": "And as he passed by, he saw Levi the son of Alphaeus sitting at the tax office, and he said to him, 'Follow me.' And rising up he followed him.",
      "M": "As he walked along, he saw Levi son of Alphaeus sitting at the tax collector's booth. 'Follow me,' Jesus told him, and Levi got up and followed him.",
      "T": "Walking along, Jesus saw Levi son of Alphaeus sitting at the tax collector's table. 'Follow me,' Jesus said. Levi stood up and followed him."
    },
    "15": {
      "L": "And as he reclined at table in his house, many tax collectors and sinners were reclining with Jesus and his disciples, for there were many who followed him.",
      "M": "While Jesus was having dinner at Levi's house, many tax collectors and sinners were eating with him and his disciples, for there were many who followed him.",
      "T": "Later Jesus was at dinner in Levi's house. Many tax collectors and notorious sinners were eating with Jesus and his disciples—there were quite a few of them who followed him."
    },
    "16": {
      "L": "And the scribes of the Pharisees, when they saw that he was eating with the sinners and tax collectors, said to his disciples, 'Why does he eat with tax collectors and sinners?'",
      "M": "When the teachers of the law who were Pharisees saw him eating with the sinners and tax collectors, they asked his disciples: 'Why does he eat with tax collectors and sinners?'",
      "T": "The Pharisees' Bible teachers noticed Jesus eating with tax collectors and notorious sinners. They challenged his disciples: 'Why does your teacher eat with people like that?'"
    },
    "17": {
      "L": "And hearing this, Jesus said to them, 'Those who are well have no need of a physician, but those who are sick. I came not to call the righteous, but sinners.'",
      "M": "On hearing this, Jesus said to them, 'It is not the healthy who need a doctor, but the sick. I have not come to call the righteous, but sinners.'",
      "T": "Hearing this, Jesus said, 'Healthy people don't need a doctor—sick people do. I haven't come to invite those who think they're already good; I've come for those who know they are sinners.'"
    },
    "18": {
      "L": "Now John's disciples and the Pharisees were fasting. And they came and said to him, 'Why do John's disciples and the disciples of the Pharisees fast, but your disciples do not fast?'",
      "M": "Now John's disciples and the Pharisees were fasting. Some people came and asked Jesus, 'How is it that John's disciples and the disciples of the Pharisees are fasting, but yours are not?'",
      "T": "At that time John's disciples and the Pharisees' disciples were observing a fast. Some people came to Jesus and asked, 'Why do John's disciples and the Pharisees' disciples fast, but yours don't?'"
    },
    "19": {
      "L": "And Jesus said to them, 'Can the sons of the wedding hall fast while the bridegroom is with them? As long as they have the bridegroom with them, they are not able to fast.'",
      "M": "Jesus answered, 'How can the guests of the bridegroom fast while he is with them? They cannot, so long as they have him with them.'",
      "T": "Jesus answered, 'Can the wedding guests fast while the bridegroom is right there with them? Of course not! As long as the bridegroom is present, there's no room for fasting.'"
    },
    "20": {
      "L": "'But the days will come when the bridegroom is taken away from them, and then they will fast in that day.'",
      "M": "'But the time will come when the bridegroom will be taken from them, and on that day they will fast.'",
      "T": "'But the day is coming when the bridegroom will be torn away from them. Then they will fast.'"
    },
    "21": {
      "L": "'No one sews a patch of unshrunk cloth on an old garment. If he does, the new piece pulls away from the old, making the tear worse.'",
      "M": "'No one sews a patch of unshrunk cloth on an old garment. Otherwise, the new piece will pull away from the old, making the tear worse.'",
      "T": "'No one patches an old coat with new, unshrunk cloth. The patch would shrink and pull away, making the hole worse than before.'"
    },
    "22": {
      "L": "'And no one puts new wine into old wineskins. If he does, the wine will burst the skins—and the wine is destroyed and the skins as well. But new wine is for new wineskins.'",
      "M": "'And no one pours new wine into old wineskins. Otherwise, the wine will burst the skins, and both the wine and the wineskins will be ruined. No, new wine is poured into new wineskins.'",
      "T": "'And no one pours new wine into old wineskins. The pressure would burst the skins, and both the wine and the skins would be lost. New wine goes into new wineskins.'"
    },
    "23": {
      "L": "And it came to pass that he was passing through the grainfields on the Sabbath, and his disciples began to make their way plucking the heads of grain.",
      "M": "One Sabbath Jesus was going through the grainfields, and as his disciples walked along, they began to pick some heads of grain.",
      "T": "One Sabbath Jesus was walking through the grain fields. As they went, his disciples started picking heads of grain."
    },
    "24": {
      "L": "And the Pharisees were saying to him, 'Look, why are they doing what is not lawful on the Sabbath?'",
      "M": "The Pharisees said to him, 'Look, why are they doing what is unlawful on the Sabbath?'",
      "T": "The Pharisees challenged him: 'Look at that! Why are your disciples breaking the Sabbath law?'"
    },
    "25": {
      "L": "And he said to them, 'Have you never read what David did when he was in need and was hungry, he and those with him:'",
      "M": "He answered, 'Have you never read what David did when he and his companions were hungry and in need?'",
      "T": "'Haven't you ever read what David did when he and his companions were starving and desperate?'"
    },
    "26": {
      "L": "'how he entered the house of God, in the time of Abiathar the high priest, and ate the bread of the Presence, which it is not lawful for any but the priests to eat, and also gave it to those who were with him?'",
      "M": "'In the days of Abiathar the high priest, he entered the house of God and ate the consecrated bread, which is lawful only for priests to eat. And he also gave some to his companions.'",
      "T": "'In the days of Abiathar the high priest, David went into the house of God and ate the sacred bread that only priests were allowed to eat—and he shared it with his companions.'"
    },
    "27": {
      "L": "And he said to them, 'The Sabbath was made for man, not man for the Sabbath.'",
      "M": "Then he said to them, 'The Sabbath was made for man, not man for the Sabbath.'",
      "T": "Then he told them, 'The Sabbath was made to serve human beings—not human beings to serve the Sabbath.'"
    },
    "28": {
      "L": "'So the Son of Man is Lord even of the Sabbath.'",
      "M": "'So the Son of Man is Lord even of the Sabbath.'",
      "T": "'That's why the Son of Man is master even of the Sabbath.'"
    }
  },
  "3": {
    "1": {
      "L": "He entered again into the synagogue, and there was a man there with a withered hand.",
      "M": "Another time Jesus went into the synagogue, and a man with a shriveled hand was there.",
      "T": "On another occasion Jesus entered the synagogue, where there was a man with a paralyzed hand."
    },
    "2": {
      "L": "And they were watching him closely to see if he would heal him on the Sabbath, so that they might accuse him.",
      "M": "Some of them were looking for a reason to accuse Jesus, so they watched him closely to see if he would heal him on the Sabbath.",
      "T": "His enemies watched him closely, hoping to catch him healing on the Sabbath so they could bring a charge against him."
    },
    "3": {
      "L": "And he said to the man with the withered hand, 'Stand up here in the middle.'",
      "M": "Jesus said to the man with the shriveled hand, 'Stand up in front of everyone.'",
      "T": "Jesus said to the man with the paralyzed hand, 'Stand up here where everyone can see.'"
    },
    "4": {
      "L": "And he said to them, 'Is it lawful on the Sabbath to do good or to do evil, to save life or to kill?' But they were silent.",
      "M": "Then Jesus asked them, 'Which is lawful on the Sabbath: to do good or to do evil, to save life or to kill?' But they remained silent.",
      "T": "He asked them, 'Is it lawful on the Sabbath to do good or to do evil? To save a life or to destroy one?' No one answered."
    },
    "5": {
      "L": "And looking around at them with anger, grieved at their hardness of heart, he said to the man, 'Stretch out your hand.' He stretched it out, and his hand was restored.",
      "M": "He looked around at them in anger and, deeply distressed at their stubborn hearts, said to the man, 'Stretch out your hand.' He stretched it out, and his hand was completely restored.",
      "T": "He looked around at them with anger, cut to the heart by their stubborn coldness. Then he said to the man, 'Hold out your hand.' He held it out—and his hand was completely healed."
    },
    "6": {
      "L": "The Pharisees went out and immediately began conspiring with the Herodians against him, how to destroy him.",
      "M": "Then the Pharisees went out and began to plot with the Herodians how they might kill Jesus.",
      "T": "The Pharisees immediately left and began plotting with the supporters of Herod on how they might eliminate Jesus."
    },
    "7": {
      "L": "And Jesus withdrew with his disciples to the sea, and a great multitude from Galilee followed,",
      "M": "Jesus withdrew with his disciples to the lake, and a large crowd from Galilee followed.",
      "T": "Jesus withdrew with his disciples to the lake, and a large crowd from Galilee followed him."
    },
    "8": {
      "L": "and from Judea and Jerusalem and Idumea and beyond the Jordan and around Tyre and Sidon. The great multitude, hearing all that he was doing, came to him.",
      "M": "When they heard about all he was doing, people came to him from Judea, Jerusalem, Idumea, and the regions across the Jordan and around Tyre and Sidon.",
      "T": "Word had spread about everything he was doing, and people came to him from Judea, Jerusalem, Idumea, the far side of the Jordan, and the region around Tyre and Sidon."
    },
    "9": {
      "L": "And he told his disciples to have a small boat ready for him because of the crowd, lest they press upon him,",
      "M": "Because of the crowd he told his disciples to have a small boat ready for him, to keep the people from crowding him.",
      "T": "The crowd was so large that he told his disciples to have a boat ready so he wouldn't be crushed."
    },
    "10": {
      "L": "for he had healed many, so that all who had afflictions were pressing against him to touch him.",
      "M": "For he had healed many, so that those with diseases were pushing forward to touch him.",
      "T": "He had healed so many people that those with illnesses kept pushing forward just to touch him."
    },
    "11": {
      "L": "And the unclean spirits, whenever they saw him, fell down before him and cried out, 'You are the Son of God.'",
      "M": "Whenever the impure spirits saw him, they fell down before him and cried out, 'You are the Son of God.'",
      "T": "Whenever the evil spirits saw him, they would fall down in front of him and shout, 'You are the Son of God!'"
    },
    "12": {
      "L": "And he strictly warned them not to make him known.",
      "M": "But he gave them strict orders not to tell others about him.",
      "T": "But he strictly ordered them not to reveal who he was."
    },
    "13": {
      "L": "And he went up on the mountain and called to him those whom he desired, and they came to him.",
      "M": "Jesus went up on a mountainside and called to him those he wanted, and they came to him.",
      "T": "Jesus went up into the hills and called the people he wanted. They came to him,"
    },
    "14": {
      "L": "And he appointed twelve—whom he also named apostles—so that they might be with him and he might send them out to preach",
      "M": "He appointed twelve that they might be with him and that he might send them out to preach",
      "T": "and he appointed twelve—whom he called apostles—to be with him and to be sent out to proclaim the good news,"
    },
    "15": {
      "L": "and to have authority to cast out demons.",
      "M": "and to have authority to drive out demons.",
      "T": "and to have authority to drive out evil spirits."
    },
    "16": {
      "L": "He appointed the twelve: Simon, to whom he gave the name Peter;",
      "M": "These are the twelve he appointed: Simon (to whom he gave the name Peter),",
      "T": "The twelve he appointed were: Simon (whom he named Peter),"
    },
    "17": {
      "L": "James the son of Zebedee and John the brother of James (to whom he gave the name Boanerges, that is, Sons of Thunder);",
      "M": "James son of Zebedee and his brother John (to them he gave the name Boanerges, which means 'sons of thunder'),",
      "T": "James son of Zebedee and his brother John (he gave them the name Boanerges, meaning 'Sons of Thunder'),"
    },
    "18": {
      "L": "Andrew, and Philip, and Bartholomew, and Matthew, and Thomas, and James the son of Alphaeus, and Thaddaeus, and Simon the Zealot,",
      "M": "Andrew, Philip, Bartholomew, Matthew, Thomas, James son of Alphaeus, Thaddaeus, Simon the Zealot,",
      "T": "Andrew, Philip, Bartholomew, Matthew, Thomas, James son of Alphaeus, Thaddaeus, Simon the Zealot,"
    },
    "19": {
      "L": "and Judas Iscariot, who betrayed him.",
      "M": "and Judas Iscariot, who betrayed him.",
      "T": "and Judas Iscariot, who would later betray him."
    },
    "20": {
      "L": "Then he went home, and the crowd gathered again, so that they were not even able to eat.",
      "M": "Then Jesus entered a house, and again a crowd gathered, so that he and his disciples were not even able to eat.",
      "T": "Jesus went home again, and such a crowd gathered that he and his disciples couldn't even find time to eat."
    },
    "21": {
      "L": "And when his own people heard it, they went out to take hold of him, for they were saying, 'He has lost his senses.'",
      "M": "When his family heard about this, they went to take charge of him, for they said, 'He is out of his mind.'",
      "T": "When his family heard what was happening, they went to restrain him. 'He's out of his mind,' they were saying."
    },
    "22": {
      "L": "And the scribes who had come down from Jerusalem were saying, 'He is possessed by Beelzebul,' and 'By the prince of demons he casts out the demons.'",
      "M": "And the teachers of the law who came down from Jerusalem said, 'He is possessed by Beelzebul! By the prince of demons he is driving out demons.'",
      "T": "The Bible teachers who had come down from Jerusalem were claiming, 'He is controlled by Beelzebul! He drives out demons by the ruler of the demons!'"
    },
    "23": {
      "L": "And summoning them, he spoke to them in parables: 'How is Satan able to cast out Satan?'",
      "M": "So Jesus called them over to him and began to speak to them in parables: 'How can Satan drive out Satan?'",
      "T": "Jesus called them over and spoke to them in pictures: 'How can Satan drive out Satan?'"
    },
    "24": {
      "L": "'If a kingdom is divided against itself, that kingdom is not able to stand.'",
      "M": "'If a kingdom is divided against itself, that kingdom cannot stand.'",
      "T": "'If a kingdom turns against itself, it will fall apart.'"
    },
    "25": {
      "L": "'And if a house is divided against itself, that house will not be able to stand.'",
      "M": "'If a house is divided against itself, that house cannot stand.'",
      "T": "'And if a household turns against itself, that household cannot survive.'"
    },
    "26": {
      "L": "'And if Satan has risen up against himself and is divided, he is not able to stand, but has an end.'",
      "M": "'And if Satan opposes himself and is divided, he cannot stand; his end has come.'",
      "T": "'So if Satan rebels against himself and is divided, he cannot survive—his end has come.'"
    },
    "27": {
      "L": "'But no one is able to enter the house of a strong man and plunder his goods, unless he first binds the strong man. Then he will plunder his house.'",
      "M": "'In fact, no one can enter a strong man's house without first tying him up. Then he can plunder the strong man's house.'",
      "T": "'No one can break into a strong man's house and rob him without first tying him up. Only then can the house be plundered.'"
    },
    "28": {
      "L": "'Truly I say to you, all sins will be forgiven the sons of men, and all the blasphemies they speak.'",
      "M": "'Truly I tell you, people can be forgiven all their sins and every slander they utter,'",
      "T": "'I tell you the truth: every sin and every slander will be forgiven the sons and daughters of humanity,'"
    },
    "29": {
      "L": "'but whoever blasphemes against the Holy Spirit never has forgiveness, but is guilty of an eternal sin'—",
      "M": "'but whoever blasphemes against the Holy Spirit will never be forgiven; they are guilty of an eternal sin.'",
      "T": "'but anyone who speaks against the Holy Spirit can never be forgiven. They are guilty of a sin that lasts forever.'"
    },
    "30": {
      "L": "for they were saying, 'He has an unclean spirit.'",
      "M": "He said this because they were saying, 'He has an impure spirit.'",
      "T": "He said this because they were charging him with having an evil spirit."
    },
    "31": {
      "L": "And his mother and his brothers arrived, and standing outside, they sent to him and called him.",
      "M": "Then Jesus' mother and brothers arrived. Standing outside, they sent someone in to call him.",
      "T": "Then Jesus' mother and brothers arrived. They stood outside and sent word in to call him out."
    },
    "32": {
      "L": "And a crowd was sitting around him, and they said to him, 'Behold, your mother and your brothers are outside, seeking you.'",
      "M": "A crowd was sitting around him, and they told him, 'Your mother and brothers are outside looking for you.'",
      "T": "A crowd was sitting around him, and someone said, 'Your mother and brothers are outside asking for you.'"
    },
    "33": {
      "L": "And he answered them, 'Who are my mother and my brothers?'",
      "M": "'Who are my mother and my brothers?' he asked.",
      "T": "'Who are my mother and my brothers?' he asked."
    },
    "34": {
      "L": "And looking around at those who sat about him, he said, 'Here are my mother and my brothers!'",
      "M": "Then he looked at those seated in a circle around him and said, 'Here are my mother and my brothers!'",
      "T": "He looked around at the people sitting in a circle around him and said, 'Here—these are my mother and my brothers!'"
    },
    "35": {
      "L": "'For whoever does the will of God, this one is my brother and sister and mother.'",
      "M": "'Whoever does God's will is my brother and sister and mother.'",
      "T": "'Anyone who does God's will is my brother, my sister, and my mother.'"
    }
  },
  "4": {
    "1": {
      "L": "Again he began to teach beside the sea. And a very large crowd gathered to him, so that he got into a boat and sat in it on the sea, and the whole crowd was beside the sea on the land.",
      "M": "Again Jesus began to teach by the lake. The crowd that gathered around him was so large that he got into a boat and sat in it out on the lake, while all the people were along the shore at the water's edge.",
      "T": "Jesus began teaching again beside the lake. Such an enormous crowd gathered around him that he got into a boat and sat offshore, while all the people stood on the shore at the water's edge."
    },
    "2": {
      "L": "And he was teaching them many things in parables, and in his teaching he said to them:",
      "M": "He taught them many things by parables, and in his teaching said:",
      "T": "He taught them many things in parables. In his teaching he said:"
    },
    "3": {
      "L": "'Listen! Behold, a sower went out to sow.'",
      "M": "'Listen! A farmer went out to sow his seed.'",
      "T": "'Listen carefully! A farmer went out to plant seed.'"
    },
    "4": {
      "L": "'And as he sowed, it came to pass that some seed fell beside the path, and the birds came and devoured it.'",
      "M": "'As he was scattering the seed, some fell along the path, and the birds came and ate it up.'",
      "T": "'As he scattered the seed, some fell on the path, and birds came and ate it up.'"
    },
    "5": {
      "L": "'Other seed fell on rocky ground, where it did not have much soil, and immediately it sprang up, since it had no depth of soil.'",
      "M": "'Some fell on rocky places, where it did not have much soil. It sprang up quickly, because the soil was shallow.'",
      "T": "'Some fell on rocky ground where there was little soil. It sprouted quickly because the soil was thin,'"
    },
    "6": {
      "L": "'And when the sun rose, it was scorched, and since it had no root, it withered away.'",
      "M": "'But when the sun came up, the plants were scorched, and they withered because they had no root.'",
      "T": "'but when the sun came up, the seedlings were scorched and withered because they had no roots.'"
    },
    "7": {
      "L": "'And other seed fell among thorns, and the thorns grew up and choked it, and it yielded no fruit.'",
      "M": "'Other seed fell among thorns, which grew up and choked the plants, so that they did not bear grain.'",
      "T": "'Other seed fell among thorn bushes, and the thorns grew up and choked out the seedlings so they produced nothing.'"
    },
    "8": {
      "L": "'And other seeds fell into good soil and produced grain, growing up and increasing and bearing thirtyfold and sixtyfold and a hundredfold.'",
      "M": "'Still other seed fell on good soil. It came up, grew and produced a crop, some multiplying thirty, some sixty, some a hundred times.'",
      "T": "'But other seed fell into good soil and grew and multiplied, producing thirty, sixty, and even a hundred times what was planted!'"
    },
    "9": {
      "L": "And he said, 'Whoever has ears to hear, let him hear.'",
      "M": "Then Jesus said, 'Whoever has ears to hear, let them hear.'",
      "T": "He added, 'If you have ears to hear—then listen carefully!'"
    },
    "10": {
      "L": "And when he was alone, those around him along with the twelve were asking him about the parables.",
      "M": "When he was alone, the Twelve and the others around him asked him about the parables.",
      "T": "When he was alone, the Twelve and those closest to him asked him about the parables."
    },
    "11": {
      "L": "And he said to them, 'To you has been given the mystery of the kingdom of God, but to those outside everything comes in parables,'",
      "M": "'The secret of the kingdom of God has been given to you,' he told them. 'But to those on the outside everything is said in parables'",
      "T": "He told them, 'You have been granted the mystery of God's kingdom. But for outsiders, everything is spoken in parables—'"
    },
    "12": {
      "L": "'so that seeing they may see and not perceive, and hearing they may hear and not understand, lest they should turn and it be forgiven them.'",
      "M": "'so that, \"they may be ever seeing but never perceiving, and ever hearing but never understanding; otherwise they might turn and be forgiven!\"'",
      "T": "'so that they may look and look but never see, and hear and hear but never understand—otherwise they might turn and be forgiven.'"
    },
    "13": {
      "L": "And he said to them, 'Do you not know this parable? How then will you understand all the parables?'",
      "M": "Then Jesus said to them, 'Don't you understand this parable? How then will you understand any parable?'",
      "T": "He said to them, 'Don't you understand this parable? Then how will you understand any of the parables?'"
    },
    "14": {
      "L": "'The sower sows the word.'",
      "M": "'The farmer sows the word.'",
      "T": "'The farmer sows the message.'"
    },
    "15": {
      "L": "'And these are the ones beside the path where the word is sown: when they hear, immediately Satan comes and takes away the word that has been sown in them.'",
      "M": "'Some people are like seed along the path, where the word is sown. As soon as they hear it, Satan comes and takes away the word that was sown in them.'",
      "T": "'The first group is like seed scattered on the path. The moment they hear the message, Satan swoops in and snatches away what was planted in them.'"
    },
    "16": {
      "L": "'And these likewise are the ones sown on rocky ground: who, when they hear the word, immediately receive it with joy.'",
      "M": "'Others, like seed sown on rocky places, hear the word and at once receive it with joy.'",
      "T": "'The second group is like seed planted on rocky ground. They hear the message and immediately receive it with enthusiasm.'"
    },
    "17": {
      "L": "'And they have no root in themselves, but are temporary; then when affliction or persecution arises because of the word, immediately they stumble.'",
      "M": "'But since they have no root, they last only a short time. When trouble or persecution comes because of the word, they quickly fall away.'",
      "T": "'But having no roots, they don't last. When trouble or persecution comes because of the message, they immediately give up.'"
    },
    "18": {
      "L": "'And others are those sown among the thorns: these are the ones who hear the word,'",
      "M": "'Still others, like seed sown among thorns, hear the word;'",
      "T": "'The third group is like seed thrown among thorn bushes. They hear the message,'"
    },
    "19": {
      "L": "'but the cares of this age and the deceitfulness of riches and the desires for other things enter in and choke the word, and it becomes unfruitful.'",
      "M": "'but the worries of this life, the deceitfulness of wealth and the desires for other things come in and choke the word, making it unfruitful.'",
      "T": "'but the anxieties of this present life, the seductive appeal of wealth, and the craving for everything else crowd in and choke the message, and it never matures.'"
    },
    "20": {
      "L": "'But those sown on the good soil are the ones who hear the word and accept it and bear fruit, thirtyfold and sixtyfold and a hundredfold.'",
      "M": "'Others, like seed sown on good soil, hear the word, accept it, and produce a crop—some thirty, some sixty, some a hundred times what was sown.'",
      "T": "'But those like seed in good soil hear the message, embrace it, and produce a harvest—thirty, sixty, or a hundred times what was planted.'"
    },
    "21": {
      "L": "And he said to them, 'Is a lamp brought in to be put under the basket, or under the bed, and not on the lampstand?'",
      "M": "He said to them, 'Do you bring in a lamp to put it under a bowl or a bed? Instead, don't you put it on its stand?'",
      "T": "'Does anyone light a lamp and then put it under a bucket or under a bed? No—you put it on a stand!'"
    },
    "22": {
      "L": "'For nothing is hidden except to be made manifest; nor is anything concealed but that it should come to light.'",
      "M": "'For whatever is hidden is meant to be disclosed, and whatever is concealed is meant to be brought out into the open.'",
      "T": "'Whatever is hidden is meant to be revealed, and whatever is concealed is destined to come into the open.'"
    },
    "23": {
      "L": "'If anyone has ears to hear, let him hear.'",
      "M": "'If anyone has ears to hear, let them hear.'",
      "T": "'If you have ears to listen—then listen!'"
    },
    "24": {
      "L": "And he said to them, 'Consider carefully what you hear. With the measure you use, it will be measured to you, and more will be added to you.'",
      "M": "'Consider carefully what you hear,' he continued. 'With the measure you use, it will be measured to you—and even more.'",
      "T": "'Be careful what you listen to. The standard you apply will be applied to you—and then some.'"
    },
    "25": {
      "L": "'For to the one who has, it will be given, and from the one who has not, even what he has will be taken away.'",
      "M": "'Whoever has will be given more; whoever does not have, even what they have will be taken from them.'",
      "T": "'Those who respond well will receive even more. But from those who don't, even what they have will be stripped away.'"
    },
    "26": {
      "L": "And he said, 'The kingdom of God is as if a man should scatter seed on the ground.'",
      "M": "He also said, 'This is what the kingdom of God is like. A man scatters seed on the ground.'",
      "T": "He also said, 'God's kingdom is like this: a man scatters seed on the ground.'"
    },
    "27": {
      "L": "'And he sleeps and rises night and day, and the seed sprouts and grows; he does not know how.'",
      "M": "'Night and day, whether he sleeps or gets up, the seed sprouts and grows, though he does not know how.'",
      "T": "'Day and night, whether he sleeps or wakes, the seed quietly sprouts and grows—though he has no idea how.'"
    },
    "28": {
      "L": "'The earth produces of itself: first the blade, then the ear, then the full grain in the ear.'",
      "M": "'All by itself the soil produces grain—first the stalk, then the head, then the full kernel in the head.'",
      "T": "'The soil produces the harvest by itself—first the sprout, then the head of grain, and finally the full, ripe kernel.'"
    },
    "29": {
      "L": "'But when the grain is ripe, immediately he puts in the sickle, because the harvest has come.'",
      "M": "'As soon as the grain is ripe, he puts the sickle to it, because the harvest has come.'",
      "T": "'As soon as the grain is ready, the farmer swings the sickle—harvest time has come!'"
    },
    "30": {
      "L": "And he said, 'How shall we compare the kingdom of God, or by what parable shall we present it?'",
      "M": "Again he said, 'What shall we say the kingdom of God is like, or what parable shall we use to describe it?'",
      "T": "He said, 'What picture can we use for God's kingdom? What story can represent it?'"
    },
    "31": {
      "L": "'It is like a grain of mustard seed, which, when sown upon the ground, is smaller than all the seeds that are on the ground,'",
      "M": "'It is like a mustard seed, which is the smallest of all seeds on earth.'",
      "T": "'It is like a mustard seed—the smallest of all seeds when planted in the ground.'"
    },
    "32": {
      "L": "'yet when it is sown it grows up and becomes the greatest of all garden plants and puts out large branches, so that the birds of the sky are able to nest under its shade.'",
      "M": "'Yet when planted, it grows and becomes the largest of all garden plants, with such big branches that the birds can perch in its shade.'",
      "T": "'But once planted, it grows up and becomes the largest of garden plants, with branches big enough for birds to come and shelter in its shade.'"
    },
    "33": {
      "L": "With many such parables he spoke the word to them, as they were able to hear it.",
      "M": "With many similar parables Jesus spoke the word to them, as much as they could understand.",
      "T": "He spoke the message to them using many parables like these—as much as they were ready to receive."
    },
    "34": {
      "L": "He did not speak to them without a parable, but privately to his own disciples he explained all things.",
      "M": "He did not say anything to them without using a parable. But when he was alone with his own disciples, he explained everything.",
      "T": "He never taught the crowd without parables. But privately, with his own disciples, he explained everything."
    },
    "35": {
      "L": "On that day, when evening had come, he said to them, 'Let us go across to the other side.'",
      "M": "That day when evening came, he said to his disciples, 'Let us go over to the other side.'",
      "T": "As evening came that day, Jesus said to his disciples, 'Let's cross to the other side of the lake.'"
    },
    "36": {
      "L": "And leaving the crowd, they took him along in the boat, just as he was. And other boats were with him.",
      "M": "Leaving the crowd behind, they took him along, just as he was, in the boat. There were also other boats with him.",
      "T": "They left the crowd behind and took Jesus with them in the boat, just as he was. Other boats went along too."
    },
    "37": {
      "L": "And a great windstorm arose, and the waves were breaking into the boat, so that the boat was already filling.",
      "M": "A furious squall came up, and the waves broke over the boat, so that it was nearly swamped.",
      "T": "A violent storm suddenly struck. Waves crashed over the sides of the boat, filling it rapidly."
    },
    "38": {
      "L": "But he was in the stern, asleep on the cushion. And they woke him and said to him, 'Teacher, do you not care that we are perishing?'",
      "M": "Jesus was in the stern, sleeping on a cushion. The disciples woke him and said to him, 'Teacher, don't you care if we drown?'",
      "T": "Jesus was asleep in the stern, his head on a cushion. They shook him awake: 'Teacher! Don't you care that we're about to die?'"
    },
    "39": {
      "L": "And waking up he rebuked the wind and said to the sea, 'Silence! Be still!' And the wind ceased, and there was a great calm.",
      "M": "He got up, rebuked the wind and said to the waves, 'Quiet! Be still!' Then the wind died down and it was completely calm.",
      "T": "He got up, spoke sternly to the wind, and commanded the sea: 'Silence! Calm down!' The wind stopped. A great calm fell."
    },
    "40": {
      "L": "And he said to them, 'Why are you so fearful? Have you still no faith?'",
      "M": "He said to his disciples, 'Why are you so afraid? Do you still have no faith?'",
      "T": "He turned to them: 'Why are you so afraid? Do you still have no faith?'"
    },
    "41": {
      "L": "And they were filled with great fear and were saying to one another, 'Who then is this, that even the wind and the sea obey him?'",
      "M": "They were terrified and asked each other, 'Who is this? Even the wind and the waves obey him!'",
      "T": "They were overwhelmed with awe and kept asking each other, 'Who is this? Even the wind and the sea obey him!'"
    }
  }
}

for tier, key in [('literal','L'), ('mediating','M'), ('thought','T')]:
    data = load(tier, 'mark')
    merge_tier(data, MARK, key)
    save(tier, 'mark', data)

print('\nMark 1–4 written to all three tiers.')
print('Chapters covered:', sorted(MARK.keys(), key=int))
