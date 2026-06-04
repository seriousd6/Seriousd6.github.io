"""
MKT 1 Kings chapters 19–21 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1kings-19-21.py

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L/M throughout; "the LORD" in T.
  Consistent with mkt-1kings-1-6.py convention.
- H430 (אֱלֹהִים): "God" in all tiers.
- H6635 (צְבָאוֹת): "hosts" — "LORD of hosts" in all tiers (19:10,14).
- H5315 (נֶפֶשׁ): rendered "life" throughout this range (Jezebel's threat, Elijah's request,
  Benhadad's servants' plea). The sense is bodily survival, not the Greek immaterial soul.
  19:4: "take my life" (Elijah's despair request); 19:10,14: "seek my life" (Elijah's lament).
- H7307 (רוּחַ): two distinct senses in this range — must not be collapsed:
  - 19:11: "wind" (physical storm that tore mountains — unambiguously meteorological)
  - 21:5: "spirit" (Ahab's inner disposition/mood — "why is your spirit so troubled?")
  L preserves context-appropriate rendering; M/T same.
- H4397 (מַלְאָךְ): "angel" in 19:5,7 (divine messenger); "messenger" in 20:2,5 (human envoy).
  Context determines; document in T where theologically significant.
- H7307 ch19v12 — qol demamah daqah (קוֹל דְּמָמָה דַקָּה):
  Literally "voice/sound + stillness/silence + thin/fine/gentle." A unique construction.
  L: "a sound of thin, still silence" — preserving the Hebrew's unusual combination.
  M: "a still, small voice" — the traditional rendering (KJV), still accurate and powerful.
  T: draws out the theological significance: God's self-revelation was not in spectacular
  natural phenomena but in a gentle, intimate whisper. The key point of the theophany.
  The double repetition of Elijah's lament (v10 and v14 are verbatim in Hebrew): intentional.
  Elijah is stuck in his depression; God's second question and identical answer show
  Elijah has not moved. T notes this in v14.
- H2617 (חֶסֶד): 20:31 — the servants of Ben-hadad say the kings of Israel are "men of chesed."
  This is political mercy/covenant loyalty invoked as diplomatic hope.
  L: "men of kindness"; M: "men of steadfast mercy"; T: "men of covenant mercy."
  Consistent with established hesed decisions in mkt-1kings-1-6.py (slight variation in
  20:31 because context is diplomatic, not devotional).
- H2764 (חֵרֶם): 20:42 — holy war devotion formula: "the man I had devoted to destruction."
  This is the same term as in Joshua's conquest (herem). Ahab's release of Ben-hadad
  was a theological crime — he reversed what God had consecrated to destruction.
  L: "devoted to destruction"; M: "set apart for destruction"; T: "consecrated to destruction
  by the LORD" — T notes the holy war register.
- H1285 (בְּרִית): "covenant" in all tiers (20:34 — Ahab's treaty with Ben-hadad).
- H5159 (נַחֲלָה): 21:3,4 — "inheritance" (ancestral land). Israelite law (Lev 25; Num 36)
  prohibited permanent sale of ancestral land. Naboth's refusal was legally/covenantally
  correct; Jezebel's killing him to seize his land violated both law and covenant.
  L: "inheritance of my fathers"; M: "ancestral inheritance"; T: "the covenant land of my
  fathers" — T surfaces the legal/theological significance.
- H1100 (בְּלִיַּעַל): 21:10,13 — "sons of Belial/worthless men" — men of no-account used as
  false witnesses. L: "sons of Belial"; M: "worthless men"; T: "men of no account."
- H3754 (כֶּרֶם): "vineyard" all tiers in ch 21.
- Aspect: waw-consecutive imperfects = narrative past throughout. Perfect verbs for
  state descriptions (Ahab's sullen mood). God's speech in 19:15-18 uses imperfects
  for divine commissioning — future-oriented in English.
- OT echoes:
  - 19:8: "forty days and forty nights to Horeb" echoes Moses (Exod 24:18; Deut 9:9,18).
    Elijah stands in the Mosaic tradition; the Horeb theophany deliberately recalls Sinai.
    T notes this explicitly.
  - 19:11-13: The Horeb theophany reverses the Sinai pattern — fire, wind, earthquake
    accompanied God's descent in Exod 19. Here God is emphatically NOT in those things.
    T surfaces this as theological inversion.
  - 19:18: "seven thousand who have not bowed to Baal" — God's hidden remnant. Paul
    cites this in Rom 11:4 ("I have kept for myself seven thousand"). T notes this.
  - 20:13,28: "you shall know that I am the LORD" — Exodus recognition formula (Exod 7:5
    etc.). The battle victories are acts of self-identification; T notes the Exodus echo.
  - 21:3: Naboth's refusal echoes Lev 25:23 ("the land is mine; you are only tenants").
    T connects this explicitly.
  - 21:19: "In the place where dogs licked the blood of Naboth..." The fulfillment in
    22:38 (dogs lick Ahab's blood in Samaria) and 2 Kgs 9:36 (Jezebel) shows the
    Deuteronomistic theodicy of exact retribution.
- Ch 21:27-29 repentance note: Ahab's genuine self-humbling produces a remarkable
  divine response — delay of judgment to the next generation. T brings out the grace.
  This is one of the few bright moments in Ahab's narrative.
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

KINGS = {
  "19": {
    "1": {
      "L": "And Ahab told Jezebel all that Elijah had done, and all that he had killed all the prophets with the sword.",
      "M": "Ahab told Jezebel everything Elijah had done and how he had killed all the prophets with the sword.",
      "T": "Ahab reported to Jezebel everything Elijah had done—including how he had put all the prophets to death with the sword."
    },
    "2": {
      "L": "Then Jezebel sent a messenger to Elijah saying, 'So let the gods do to me and more also, if I do not make your life as the life of one of them by this time tomorrow.'",
      "M": "Jezebel sent a messenger to Elijah, saying, 'May the gods deal with me, however severely, if by tomorrow at this time I have not made your life like the life of one of them.'",
      "T": "Jezebel sent a messenger to Elijah: 'May the gods do so to me and more besides if by this time tomorrow your life is not like the life of one of those prophets.'"
    },
    "3": {
      "L": "When he saw that, he arose and went for his life, and came to Beersheba, which belongs to Judah, and left his servant there.",
      "M": "When Elijah saw this, he arose and fled for his life. He came to Beersheba in Judah and left his servant there.",
      "T": "Elijah saw the threat and fled for his life. He came to Beersheba in Judah and left his servant there."
    },
    "4": {
      "L": "But he himself went a day's journey into the wilderness and came and sat down under a juniper tree. And he requested for himself to die, saying, 'It is enough; now, O LORD, take my life, for I am not better than my fathers.'",
      "M": "He himself went a day's journey into the wilderness and sat down under a juniper tree. He asked that he might die, saying, 'It is enough! Now, LORD, take my life, for I am no better than my ancestors.'",
      "T": "He went on alone into the wilderness—a full day's journey—and collapsed under a juniper tree. He asked God to let him die. 'Enough,' he said. 'LORD, take my life. I am no better than my fathers.'"
    },
    "5": {
      "L": "And he lay and slept under the juniper tree. And behold, an angel touched him and said to him, 'Arise and eat.'",
      "M": "He lay down and slept under the juniper tree. Then an angel touched him and said, 'Arise and eat.'",
      "T": "He lay down and fell asleep under the juniper tree. Then an angel touched him and said: 'Get up and eat.'"
    },
    "6": {
      "L": "And he looked, and there at his head was a cake baked on coals and a cruse of water. And he ate and drank and lay down again.",
      "M": "He looked, and there at his head was a cake baked on coals and a jar of water. He ate and drank and lay down again.",
      "T": "He looked up and there beside him was bread baked on hot coals and a jar of water. He ate and drank, then lay back down."
    },
    "7": {
      "L": "And the angel of the LORD came again a second time and touched him and said, 'Arise and eat, for the journey is too great for you.'",
      "M": "The angel of the LORD came back a second time, touched him, and said, 'Arise and eat, for the journey is too far for you.'",
      "T": "The angel of the LORD came a second time, touched him, and said: 'Get up and eat—the journey ahead is too long for you.'"
    },
    "8": {
      "L": "And he arose and ate and drank, and went in the strength of that food forty days and forty nights to Horeb, the mount of God.",
      "M": "He arose and ate and drank, and in the strength of that food he traveled forty days and forty nights until he reached Horeb, the mountain of God.",
      "T": "He got up, ate and drank, and on the strength of that food traveled forty days and forty nights to Horeb, the mountain of God—the very mountain where Moses had met the LORD."
    },
    "9": {
      "L": "There he came to a cave and lodged there. And behold, the word of the LORD came to him, and he said to him, 'What are you doing here, Elijah?'",
      "M": "There he came to a cave and spent the night. The word of the LORD came to him: 'What are you doing here, Elijah?'",
      "T": "He found a cave there and spent the night in it. Then the word of the LORD came to him: 'What are you doing here, Elijah?'"
    },
    "10": {
      "L": "He said, 'I have been very zealous for the LORD, the God of hosts. For the people of Israel have forsaken your covenant, thrown down your altars, and killed your prophets with the sword, and I, even I only, am left, and they seek my life, to take it away.'",
      "M": "He answered, 'I have been utterly zealous for the LORD, the God of hosts. The people of Israel have abandoned your covenant, torn down your altars, and killed your prophets with the sword. I alone am left, and they are trying to take my life.'",
      "T": "'I have been consumed with zeal for the LORD, the God of hosts. The people of Israel have abandoned your covenant, demolished your altars, and put your prophets to death. I am the only one left—and now they are hunting me down.'"
    },
    "11": {
      "L": "He said, 'Go out and stand on the mount before the LORD.' And behold, the LORD passed by, and a great and strong wind tore the mountains and broke the rocks in pieces before the LORD, but the LORD was not in the wind. And after the wind an earthquake, but the LORD was not in the earthquake.",
      "M": "He said, 'Go out and stand on the mountain before the LORD.' Then the LORD passed by. A great and powerful wind tore the mountains apart and shattered the rocks before the LORD—but the LORD was not in the wind. After the wind there was an earthquake—but the LORD was not in the earthquake.",
      "T": "The LORD said: 'Go out and stand on the mountain before the LORD.' Then the LORD himself passed by. A great and powerful wind went ahead, tearing mountains apart and shattering rocks—but the LORD was not in the wind. After the wind, an earthquake—but the LORD was not in the earthquake."
    },
    "12": {
      "L": "And after the earthquake a fire, but the LORD was not in the fire. And after the fire a sound of thin, still silence.",
      "M": "After the earthquake there was a fire—but the LORD was not in the fire. And after the fire a still, small voice.",
      "T": "After the earthquake, fire—but the LORD was not in the fire. And after the fire: a gentle whisper, a voice in utter stillness."
    },
    "13": {
      "L": "And when Elijah heard it, he wrapped his face in his mantle and went out and stood at the entrance of the cave. And behold, there came a voice to him and said, 'What are you doing here, Elijah?'",
      "M": "When Elijah heard it, he wrapped his face in his cloak and went out and stood at the entrance of the cave. A voice came to him: 'What are you doing here, Elijah?'",
      "T": "When Elijah heard it, he wrapped his face in his cloak—covering himself before the presence of God—and went out and stood at the entrance of the cave. The voice came: 'What are you doing here, Elijah?'"
    },
    "14": {
      "L": "He said, 'I have been very zealous for the LORD, the God of hosts. For the people of Israel have forsaken your covenant, thrown down your altars, and killed your prophets with the sword, and I, even I only, am left, and they seek my life, to take it away.'",
      "M": "He answered, 'I have been utterly zealous for the LORD, the God of hosts. The people of Israel have abandoned your covenant, torn down your altars, and killed your prophets with the sword. I alone am left, and they are trying to take my life.'",
      "T": "'I have been consumed with zeal for the LORD, the God of hosts. Israel has abandoned your covenant, torn down your altars, and killed your prophets. I alone am left—and they want my life.' Elijah repeats the same words, unchanged. The vision has not broken through his despair."
    },
    "15": {
      "L": "And the LORD said to him, 'Go, return on your way to the wilderness of Damascus. And when you arrive, you shall anoint Hazael to be king over Syria.'",
      "M": "The LORD said to him, 'Go back the way you came, to the wilderness of Damascus. When you get there, anoint Hazael as king over Aram.'",
      "T": "The LORD said: 'Go back the way you came—to the wilderness of Damascus. When you arrive, anoint Hazael as king over Aram.'"
    },
    "16": {
      "L": "'And Jehu the son of Nimshi you shall anoint to be king over Israel, and Elisha the son of Shaphat of Abel-meholah you shall anoint to be prophet in your place.'",
      "M": "'You shall also anoint Jehu son of Nimshi as king over Israel, and Elisha son of Shaphat from Abel-meholah as prophet in your place.'",
      "T": "'Anoint Jehu son of Nimshi king over Israel, and anoint Elisha son of Shaphat of Abel-meholah as prophet in your place.'"
    },
    "17": {
      "L": "'And the one who escapes from the sword of Hazael shall Jehu kill, and the one who escapes from the sword of Jehu shall Elisha kill.'",
      "M": "'Whoever escapes the sword of Hazael, Jehu will kill. And whoever escapes the sword of Jehu, Elisha will kill.'",
      "T": "'Whoever escapes Hazael's sword, Jehu will cut down. Whoever escapes Jehu's sword, Elisha will finish.'"
    },
    "18": {
      "L": "'Yet I have left to myself seven thousand in Israel, all the knees that have not bowed to Baal, and every mouth that has not kissed him.'",
      "M": "'Yet I have kept seven thousand in Israel—every knee that has not bowed to Baal and every mouth that has not kissed him.'",
      "T": "'But I have kept for myself seven thousand in Israel—every knee that has not bent to Baal, every mouth that has not kissed him. You are not as alone as you think.'"
    },
    "19": {
      "L": "So he departed from there and found Elisha the son of Shaphat, who was plowing with twelve yoke of oxen before him, he being with the twelfth. Elijah passed by him and cast his mantle on him.",
      "M": "So Elijah went from there and found Elisha son of Shaphat plowing with twelve yoke of oxen; he himself was with the twelfth pair. Elijah passed by him and threw his cloak over him.",
      "T": "Elijah left and found Elisha son of Shaphat plowing with twelve yoke of oxen. Elisha was driving the last yoke. Elijah passed by and threw his cloak over him—an unmistakable act of calling."
    },
    "20": {
      "L": "And he left the oxen and ran after Elijah and said, 'Let me kiss my father and my mother, and then I will follow you.' He said, 'Go back again, for what have I done to you?'",
      "M": "Elisha left the oxen and ran after Elijah and said, 'Let me kiss my father and mother goodbye, and then I will follow you.' He said, 'Go back—what have I done to you?'",
      "T": "Elisha left the oxen and ran after Elijah. 'Let me kiss my father and mother goodbye,' he said, 'and then I will follow you.' Elijah said: 'Go back—what have I done to hold you back?'"
    },
    "21": {
      "L": "And he returned from following him and took a yoke of oxen and slaughtered them, and boiled their flesh with the instruments of the oxen, and gave it to the people, and they ate. Then he arose and went after Elijah and ministered to him.",
      "M": "Elisha turned back from following Elijah, took a yoke of oxen, slaughtered them, and boiled their flesh using the wooden plowing gear as fuel. He gave the food to the people and they ate. Then he arose and followed Elijah and served him.",
      "T": "Elisha turned back, slaughtered his oxen, and boiled the meat on a fire of the plowing gear—burning his livelihood as he cooked it. He fed the people, then arose and followed Elijah, serving him from that day forward."
    }
  },
  "20": {
    "1": {
      "L": "And Ben-hadad king of Syria gathered all his army, and there were thirty-two kings with him, and horses and chariots. And he went up and besieged Samaria and made war against it.",
      "M": "Ben-hadad king of Aram gathered all his army—thirty-two kings with him, along with horses and chariots—and went up and besieged Samaria and attacked it.",
      "T": "Ben-hadad king of Aram mustered his whole army—thirty-two vassal kings, cavalry and chariots—and marched up to besiege Samaria."
    },
    "2": {
      "L": "And he sent messengers into the city to Ahab king of Israel and said to him, 'Thus says Ben-hadad:'",
      "M": "He sent messengers into the city to Ahab king of Israel with this message from Ben-hadad:",
      "T": "He sent messengers into the city to Ahab king of Israel. Ben-hadad's message was this:"
    },
    "3": {
      "L": "'Your silver and your gold are mine; your best wives and your children are also mine.'",
      "M": "'Your silver and gold belong to me, and your best wives and children also belong to me.'",
      "T": "'Your silver and gold are mine. Your wives and your best children are mine.'"
    },
    "4": {
      "L": "And the king of Israel answered, 'As you say, my lord the king; I am yours, and all that I have.'",
      "M": "The king of Israel answered, 'Just as you say, my lord the king—I and all I have are yours.'",
      "T": "Ahab king of Israel answered: 'As you say, my lord the king. I and everything I have are yours.'"
    },
    "5": {
      "L": "And the messengers came again and said, 'Thus says Ben-hadad: Although I sent to you, saying, Your silver and your gold, your wives and your children, you shall deliver to me,'",
      "M": "The messengers came back and said, 'Thus says Ben-hadad: I sent to you saying, Deliver to me your silver and gold, your wives and your children—'",
      "T": "The messengers came again: 'Ben-hadad says this: I sent word demanding your silver, gold, wives, and children—'"
    },
    "6": {
      "L": "'yet I will send my servants to you tomorrow about this time, and they shall search your house and the houses of your servants, and lay hands on whatever is pleasing in your eyes and take it away.'",
      "M": "'—but tomorrow at this time I will send my servants to search your palace and your servants' houses, and they will seize whatever pleases them and carry it off.'",
      "T": "'—but tomorrow about this time I will send my men through your palace and your servants' houses to take whatever they want.'"
    },
    "7": {
      "L": "Then the king of Israel called all the elders of the land and said, 'Mark and see how this man is seeking mischief, for he sent to me for my wives and my children and my silver and my gold, and I did not refuse him.'",
      "M": "The king of Israel called all the elders of the land and said, 'See clearly how this man is bent on trouble. He sent to me for my wives and children and silver and gold, and I did not refuse him.'",
      "T": "Ahab summoned all the elders of the land and said: 'See how this man is looking for a fight. He demanded my wives, my children, my silver and gold—and I agreed to all of it.'"
    },
    "8": {
      "L": "And all the elders and all the people said to him, 'Do not listen or consent.'",
      "M": "All the elders and all the people said, 'Do not listen to him or agree.'",
      "T": "All the elders and all the people said: 'Do not listen. Do not give in.'"
    },
    "9": {
      "L": "So he said to the messengers of Ben-hadad, 'Tell my lord the king: All that you sent for to your servant at the first I will do, but this thing I cannot do.' And the messengers departed and brought him word again.",
      "M": "So he told Ben-hadad's messengers, 'Tell my lord the king: Everything you first demanded of your servant I will do, but this last thing I cannot agree to.' The messengers left and brought back word.",
      "T": "Ahab told Ben-hadad's messengers: 'Tell my lord the king: Your first demands I will meet—but this further demand I cannot fulfill.' The messengers went and brought the reply."
    },
    "10": {
      "L": "And Ben-hadad sent to him and said, 'The gods do so to me and more also, if the dust of Samaria shall suffice for handfuls for all the people who follow me.'",
      "M": "Ben-hadad sent back and said, 'May the gods deal with me severely if the dust of Samaria is enough to provide a handful for each of the troops who follow me.'",
      "T": "Ben-hadad sent back his answer: 'May the gods deal with me in the harshest terms if there is enough dust in Samaria to give every one of my soldiers a fistful.'"
    },
    "11": {
      "L": "And the king of Israel answered, 'Tell him: Let not him who straps on his armor boast like him who takes it off.'",
      "M": "The king of Israel answered, 'Tell him: Let not the one who straps on his armor boast like one who takes it off.'",
      "T": "Ahab sent back: 'Tell him—a man strapping on his armor should not boast like a man who has taken it off after the fight.'"
    },
    "12": {
      "L": "And when Ben-hadad heard this message, as he was drinking with the kings in the pavilions, he said to his servants, 'Set yourselves in array.' And they set themselves in array against the city.",
      "M": "When Ben-hadad heard this message—he and the kings were drinking in the field shelters—he said to his servants, 'Take your positions.' They took their positions against the city.",
      "T": "Ben-hadad was drinking with the allied kings in the field encampments when this reply arrived. He said: 'Take your positions.' They moved into battle formation against the city."
    },
    "13": {
      "L": "And behold, a prophet came near to Ahab king of Israel and said, 'Thus says the LORD: Have you seen all this great multitude? Behold, I will give it into your hand today, and you shall know that I am the LORD.'",
      "M": "Then a prophet came to Ahab king of Israel and said, 'Thus says the LORD: Do you see this vast army? I will hand it over to you today, and you will know that I am the LORD.'",
      "T": "Then a prophet approached Ahab king of Israel and said: 'The LORD says this: Do you see this vast army? I am handing it over to you today—and you will know that I am the LORD.'"
    },
    "14": {
      "L": "And Ahab said, 'By whom?' He said, 'Thus says the LORD: By the young men of the district governors.' Then he said, 'Who shall begin the battle?' He answered, 'You shall.'",
      "M": "Ahab asked, 'By whom?' He said, 'Thus says the LORD: By the young officers of the district governors.' Then Ahab asked, 'Who should open the battle?' He replied, 'You shall.'",
      "T": "'Through whom?' Ahab asked. 'Through the young officers of the district governors,' the prophet said. 'Who will strike first?' 'You will,' he answered."
    },
    "15": {
      "L": "Then he mustered the young men of the district governors, and there were two hundred and thirty-two. After them he mustered all the people of Israel, seven thousand.",
      "M": "He mustered the young officers of the district governors—there were two hundred and thirty-two of them. After them he mustered all the fighting men of Israel—seven thousand.",
      "T": "Ahab counted the young officers of the district governors: two hundred and thirty-two men. Then he counted all the fighting men of Israel: seven thousand."
    },
    "16": {
      "L": "And they went out at noon, while Ben-hadad was drinking himself drunk in the pavilions, he and the thirty-two kings who helped him.",
      "M": "They went out at noon, while Ben-hadad was drinking himself drunk in the field shelters—he and the thirty-two kings who had come to help him.",
      "T": "They marched out at midday. Ben-hadad was drinking himself drunk in the field encampments—he and the thirty-two allied kings with him."
    },
    "17": {
      "L": "And the young men of the district governors went out first. And Ben-hadad sent out spies, and they told him, 'Men have come out from Samaria.'",
      "M": "The young officers of the district governors went out first. Ben-hadad sent scouts, who reported, 'Men are coming out of Samaria.'",
      "T": "The young officers led the way out of the city. Ben-hadad's scouts reported: 'Men are coming out of Samaria.'"
    },
    "18": {
      "L": "He said, 'If they have come out for peace, take them alive. If they have come out for war, take them alive.'",
      "M": "He said, 'Whether they have come out for peace or for war, take them alive.'",
      "T": "He said: 'Whether they come in peace or for battle—take them alive.'"
    },
    "19": {
      "L": "So these young men of the district governors came out of the city, and the army which followed them.",
      "M": "So the young officers of the district governors came out of the city, with the rest of the army behind them.",
      "T": "The young officers came out of the city first, with the main army following behind them."
    },
    "20": {
      "L": "And each one struck down his man. The Syrians fled, and Israel pursued them. But Ben-hadad king of Syria escaped on a horse with horsemen.",
      "M": "Each man struck down his opponent. The Arameans fled, and Israel pursued them. But Ben-hadad king of Aram escaped on horseback with some cavalry.",
      "T": "Each Israelite cut down his man. The Arameans broke and fled; Israel gave chase. Ben-hadad king of Aram escaped on horseback with a cavalry escort."
    },
    "21": {
      "L": "And the king of Israel went out and struck the horses and chariots, and struck Syria with a great blow.",
      "M": "The king of Israel went out and captured the horses and chariots, and inflicted a great defeat on Aram.",
      "T": "Ahab king of Israel went out and seized the horses and chariots. The Arameans suffered a devastating defeat."
    },
    "22": {
      "L": "Then the prophet came near to the king of Israel and said to him, 'Go, strengthen yourself and consider well what you must do, for in the spring the king of Syria will come up against you.'",
      "M": "The prophet came to the king of Israel and said, 'Go, strengthen yourself. Take note of what you need to do, for at the turn of the year the king of Aram will attack you again.'",
      "T": "The prophet came to Ahab and said: 'Strengthen yourself and take careful stock of your situation—because at the spring campaign season, the king of Aram will come against you again.'"
    },
    "23": {
      "L": "And the servants of the king of Syria said to him, 'Their gods are gods of the hills; therefore they were stronger than we. But let us fight against them in the plain, and surely we shall be stronger than they.'",
      "M": "Meanwhile the servants of the king of Aram said to him, 'Their gods are gods of the hills; that is why they were stronger than we. But if we fight them in the plain, we will certainly be stronger than they.'",
      "T": "Ben-hadad's officers advised him: 'Their gods are gods of the hills—that's why they beat us. Fight them on level ground and we will surely overpower them.'"
    },
    "24": {
      "L": "'And do this: remove the kings, each from his post, and put governors in their places.'",
      "M": "'Do this: remove each king from his command and replace them with professional officers.'",
      "T": "'Also do this: dismiss the vassal kings from their posts and put trained military commanders in their place.'"
    },
    "25": {
      "L": "'And muster an army like the army you have lost—horse for horse and chariot for chariot. Then we will fight against them in the plain, and surely we shall be stronger than they.' And he listened to their voice and did so.",
      "M": "'Raise an army to replace the one you lost—horse for horse, chariot for chariot. Then we will fight them in the plain, and surely we will be stronger.' He listened to them and did so.",
      "T": "'Rebuild your army to match what you lost—horse for horse, chariot for chariot. Fight them on the plain, and victory is certain.' He took their advice and acted on it."
    },
    "26": {
      "L": "And it came to pass at the turn of the year, that Ben-hadad mustered the Syrians and went up to Aphek to fight against Israel.",
      "M": "In the spring Ben-hadad mustered the Arameans and went up to Aphek to fight Israel.",
      "T": "When spring came, Ben-hadad mustered the Aramean forces and marched up to Aphek to fight against Israel."
    },
    "27": {
      "L": "And the people of Israel were mustered and were provisioned and went against them. And the people of Israel encamped before them like two little flocks of goats, but the Syrians filled the country.",
      "M": "The people of Israel were also mustered and supplied, and they marched out to meet them. The Israelites camped opposite them looking like two small flocks of goats, while the Arameans covered the land.",
      "T": "Israel was also mustered and supplied and marched out to meet them. The Israelites camped across from the Arameans like two small flocks of goats—while the Arameans spread across the whole countryside."
    },
    "28": {
      "L": "And a man of God came near and said to the king of Israel, 'Thus says the LORD: Because the Syrians have said, The LORD is a god of the hills but he is not a god of the valleys, therefore I will give all this great multitude into your hand, and you shall know that I am the LORD.'",
      "M": "A man of God came to the king of Israel and said, 'Thus says the LORD: Because the Arameans have said, The LORD is a god of the hills but not of the valleys, I will hand all this vast army over to you, and you will know that I am the LORD.'",
      "T": "A man of God came to Ahab king of Israel and said: 'The LORD says this: Because the Arameans have claimed that the LORD is only a god of the hills and not of the valleys—I will hand all this vast army over to you. And you will know that I am the LORD.'"
    },
    "29": {
      "L": "And they encamped opposite each other seven days. Then on the seventh day the battle was joined. And the people of Israel struck down of the Syrians a hundred thousand foot soldiers in one day.",
      "M": "The two armies camped across from each other for seven days. On the seventh day the battle was joined. The Israelites cut down a hundred thousand Aramean foot soldiers in a single day.",
      "T": "The two armies faced each other for seven days. On the seventh day the battle erupted. Israel cut down a hundred thousand Aramean foot soldiers in a single day."
    },
    "30": {
      "L": "But the rest fled into the city of Aphek, and the wall fell on twenty-seven thousand men who were left. Ben-hadad also fled and came into the city and went from chamber to inner chamber.",
      "M": "The survivors fled into the city of Aphek, and the city wall collapsed on twenty-seven thousand of the remaining men. Ben-hadad also fled into the city and hid himself in an inner room.",
      "T": "The survivors fled into Aphek, and the city wall collapsed on twenty-seven thousand more. Ben-hadad himself fled into the city and hid in an inner room."
    },
    "31": {
      "L": "His servants said to him, 'Behold, we have heard that the kings of the house of Israel are kings of kindness. Let us put sackcloth on our bodies and ropes on our heads and go out to the king of Israel. Perhaps he will spare your life.'",
      "M": "His servants said to him, 'We have heard that the kings of the house of Israel are kings of steadfast mercy. Let us put on sackcloth and put ropes on our heads and go out to the king of Israel. Perhaps he will spare your life.'",
      "T": "His servants said to him: 'We have heard that the kings of Israel are men of covenant mercy. Let us put on sackcloth and ropes and go out to the king of Israel. Perhaps he will let you live.'"
    },
    "32": {
      "L": "So they put sackcloth on their bodies and ropes on their heads and came to the king of Israel and said, 'Your servant Ben-hadad says, Please let me live.' And he said, 'Is he still alive? He is my brother.'",
      "M": "They put on sackcloth and ropes and came to the king of Israel and said, 'Your servant Ben-hadad says, Please spare my life.' He replied, 'Is he still alive? He is my brother.'",
      "T": "They put on sackcloth and ropes and came to Ahab king of Israel. 'Your servant Ben-hadad says: Please let me live.' Ahab replied: 'Is he still alive? He is my brother.'"
    },
    "33": {
      "L": "Now the men were watching for a sign, and they quickly caught it from him and said, 'Yes, your brother Ben-hadad.' Then he said, 'Go, bring him.' So Ben-hadad came out to him, and he caused him to come up into the chariot.",
      "M": "The men were looking for a favorable sign from him, and they quickly caught his words and said, 'Yes—your brother Ben-hadad.' He said, 'Go, bring him.' So Ben-hadad came out to him, and Ahab had him come up into the chariot.",
      "T": "The men seized on the word—they were watching for any encouragement—and said: 'Yes, your brother Ben-hadad.' 'Go, bring him,' said Ahab. Ben-hadad came out, and Ahab brought him up into the chariot."
    },
    "34": {
      "L": "And Ben-hadad said to him, 'The cities which my father took from your father I will restore, and you may establish bazaars for yourself in Damascus, as my father made in Samaria.' And Ahab said, 'I will send you away with this covenant.' So he made a covenant with him and sent him away.",
      "M": "Ben-hadad said to him, 'I will return the cities my father took from your father, and you may set up your own trading quarters in Damascus, as my father did in Samaria.' Ahab replied, 'I will release you with this treaty.' He made a covenant with him and let him go.",
      "T": "Ben-hadad said: 'The cities my father seized from your father I will restore. And you may establish your own trading district in Damascus, just as my father had in Samaria.' Ahab said: 'I release you on these terms.' He made a covenant with Ben-hadad and sent him away."
    },
    "35": {
      "L": "And a certain man of the sons of the prophets said to his companion at the word of the LORD, 'Strike me.' But the man refused to strike him.",
      "M": "A certain man from the company of the prophets said to his companion by the word of the LORD, 'Strike me.' But the man refused to strike him.",
      "T": "One of the sons of the prophets, acting on the LORD's command, said to his companion: 'Strike me.' But the man refused."
    },
    "36": {
      "L": "Then he said to him, 'Because you have not obeyed the voice of the LORD, as soon as you depart from me, a lion shall strike you down.' And as soon as he had departed from him, a lion met him and struck him down.",
      "M": "He said to him, 'Because you have not obeyed the voice of the LORD, as soon as you leave me a lion will kill you.' And when he departed from him, a lion met him and killed him.",
      "T": "The prophet said: 'Because you did not obey the word of the LORD, a lion will kill you when you leave me.' As soon as the man went away, a lion came and killed him."
    },
    "37": {
      "L": "Then he found another man and said, 'Strike me.' And the man struck him, wounding him.",
      "M": "He found another man and said, 'Strike me.' That man struck him and wounded him.",
      "T": "He found another man and said: 'Strike me.' That man struck him and drew blood."
    },
    "38": {
      "L": "So the prophet departed and waited for the king along the road, disguising himself with a bandage over his eyes.",
      "M": "So the prophet went and waited for the king along the road, disguising himself with a bandage over his eyes.",
      "T": "The prophet went and waited along the road for the king to pass, disguising himself with a cloth bandaged over his eyes."
    },
    "39": {
      "L": "And as the king passed by, he cried to the king and said, 'Your servant went out in the midst of the battle, and behold, a soldier turned and brought a man to me and said, Guard this man; if by any means he be missing, your life shall be for his life, or else you shall pay a talent of silver.'",
      "M": "As the king passed, the prophet cried out to him and said, 'Your servant was in the thick of the battle when a soldier turned and brought a man to me and said, Guard this man. If he goes missing, your life will be forfeit for his, or you will pay a talent of silver.'",
      "T": "As the king passed by, the prophet called out: 'Your servant was in the thick of the battle when a soldier brought a captive to me and said: Guard this man. If he escapes, your life is forfeit—or you pay a talent of silver.'"
    },
    "40": {
      "L": "And while your servant was busy here and there, he was gone.' The king of Israel said to him, 'So shall your judgment be; you yourself have decided it.'",
      "M": "'But while I was occupied here and there, he got away.' The king of Israel said to him, 'Your sentence is decided—you have passed judgment on yourself.'",
      "T": "'But while I was occupied with this and that, he was gone.' Ahab said: 'You have judged your own case—that is your sentence.'"
    },
    "41": {
      "L": "Then he quickly took the bandage away from his eyes, and the king of Israel recognized him as one of the prophets.",
      "M": "He quickly removed the bandage from his eyes, and the king of Israel recognized him as one of the prophets.",
      "T": "He quickly pulled the bandage from his eyes. Ahab recognized him as one of the prophets."
    },
    "42": {
      "L": "And he said to him, 'Thus says the LORD: Because you have let go out of your hand the man whom I had devoted to destruction, therefore your life shall be for his life, and your people for his people.'",
      "M": "He said to him, 'Thus says the LORD: Because you have released the man whom I had set apart for destruction, your life will be required for his life, and your people for his people.'",
      "T": "He said: 'The LORD says this: Because you have let go the man I had consecrated to destruction, your life will pay for his and your people for his people.'"
    },
    "43": {
      "L": "And the king of Israel went to his house vexed and sullen, and came to Samaria.",
      "M": "The king of Israel went home to Samaria resentful and angry.",
      "T": "Ahab king of Israel went home sullen and resentful, and returned to Samaria."
    }
  },
  "21": {
    "1": {
      "L": "And after these things, Naboth the Jezreelite had a vineyard which was in Jezreel, beside the palace of Ahab king of Samaria.",
      "M": "After this, Naboth the Jezreelite owned a vineyard in Jezreel, adjacent to the palace of Ahab king of Samaria.",
      "T": "After these events, there was a man named Naboth the Jezreelite whose vineyard lay right beside the palace of Ahab king of Samaria in Jezreel."
    },
    "2": {
      "L": "And Ahab spoke to Naboth saying, 'Give me your vineyard that I may have it for a garden of herbs, for it is near my house. And I will give you for it a better vineyard than it, or if it seems good to you, I will give you its worth in money.'",
      "M": "Ahab said to Naboth, 'Give me your vineyard so I can use it as a vegetable garden, since it is right next to my palace. I will give you a better vineyard for it, or if you prefer, I will pay you its value in silver.'",
      "T": "Ahab spoke to Naboth: 'Let me have your vineyard for a kitchen garden—it is right next to my house. I will give you a better vineyard in exchange, or if you prefer, I will pay you its fair price in silver.'"
    },
    "3": {
      "L": "But Naboth said to Ahab, 'The LORD forbid that I should give the inheritance of my fathers to you.'",
      "M": "But Naboth said to Ahab, 'The LORD forbid that I should give you my ancestral inheritance.'",
      "T": "But Naboth said to Ahab: 'The LORD forbid that I should give you the covenant land of my fathers. This ground is not mine to sell.'"
    },
    "4": {
      "L": "And Ahab came into his house vexed and sullen because of the word that Naboth the Jezreelite had spoken to him, for he had said, 'I will not give you the inheritance of my fathers.' He lay down on his bed and turned away his face and would eat no food.",
      "M": "Ahab went home resentful and sullen because of what Naboth the Jezreelite had said—'I will not give you my ancestral inheritance.' He lay down on his bed, turned his face to the wall, and refused to eat.",
      "T": "Ahab went home sullen and resentful over Naboth's answer: 'I will not give you my ancestral inheritance.' He lay down on his bed, turned his face away, and refused to eat."
    },
    "5": {
      "L": "But Jezebel his wife came to him and said to him, 'Why is your spirit so troubled that you eat no food?'",
      "M": "His wife Jezebel came to him and said, 'Why are you so troubled in spirit that you will not eat?'",
      "T": "Jezebel his wife came to him and said: 'Why are you so downcast? Why won't you eat?'"
    },
    "6": {
      "L": "And he said to her, 'Because I spoke to Naboth the Jezreelite and said to him, Give me your vineyard for money; or else, if it pleases you, I will give you another vineyard in its place. But he answered, I will not give you my vineyard.'",
      "M": "He told her, 'I spoke to Naboth the Jezreelite and said, Sell me your vineyard, or if you prefer, I will give you another vineyard in its place. But he said, I will not give you my vineyard.'",
      "T": "He told her: 'I asked Naboth the Jezreelite to give me his vineyard—either for payment or in exchange for another. He said: I will not give you my vineyard.'"
    },
    "7": {
      "L": "And Jezebel his wife said to him, 'Do you now govern Israel? Arise, eat bread and let your heart be merry. I will give you the vineyard of Naboth the Jezreelite.'",
      "M": "His wife Jezebel said to him, 'Do you not now govern Israel? Get up, eat, and be glad. I will give you the vineyard of Naboth the Jezreelite.'",
      "T": "Jezebel said: 'Is this how you govern Israel? Get up and eat—cheer up. I will get you the vineyard of Naboth the Jezreelite.'"
    },
    "8": {
      "L": "So she wrote letters in Ahab's name and sealed them with his seal, and sent the letters to the elders and to the leaders who lived with Naboth in his city.",
      "M": "She wrote letters in Ahab's name, sealed them with his seal, and sent them to the elders and nobles who lived in Naboth's city.",
      "T": "She wrote letters in Ahab's name, sealed them with his royal seal, and sent them to the elders and leading men of Naboth's city."
    },
    "9": {
      "L": "And she wrote in the letters, 'Proclaim a fast, and set Naboth at the head of the people.'",
      "M": "In the letters she wrote, 'Proclaim a fast and seat Naboth in the prominent position among the people.'",
      "T": "The letters said: 'Call a public fast. Seat Naboth in a place of honor before the people.'"
    },
    "10": {
      "L": "'And set two men, sons of Belial, before him, and let them bear witness against him, saying, You have cursed God and the king. Then take him out and stone him to death.'",
      "M": "'Place two worthless men opposite him to testify against him, saying, You have cursed God and the king. Then take him out and stone him to death.'",
      "T": "'Then seat two men of no account across from him. Have them testify: He cursed God and the king. Then take him out and stone him to death.'"
    },
    "11": {
      "L": "And the men of his city, the elders and the leaders who lived in his city, did as Jezebel had sent word to them, just as it was written in the letters which she had sent to them.",
      "M": "The men of the city—the elders and nobles who lived there—did exactly as Jezebel had instructed in the letters she sent them.",
      "T": "The men of the city—the elders and leading citizens—carried out Jezebel's orders to the letter."
    },
    "12": {
      "L": "They proclaimed a fast and set Naboth at the head of the people.",
      "M": "They proclaimed a fast and seated Naboth in the place of honor.",
      "T": "They called a public fast and gave Naboth the seat of honor."
    },
    "13": {
      "L": "And two men, sons of Belial, came in and sat before him. And the men of Belial witnessed against Naboth in the presence of the people, saying, 'Naboth has cursed God and the king.' So they carried him outside the city and stoned him with stones, and he died.",
      "M": "Two worthless men came in and sat opposite Naboth. They testified against him before the people, saying, 'Naboth has cursed God and the king.' So they took him outside the city and stoned him to death.",
      "T": "Two men of no account came in and sat across from Naboth. In front of all the people they gave their false testimony: 'Naboth cursed God and the king.' They dragged him outside the city and stoned him to death."
    },
    "14": {
      "L": "Then they sent to Jezebel saying, 'Naboth has been stoned; he is dead.'",
      "M": "Then they sent word to Jezebel: 'Naboth has been stoned to death.'",
      "T": "Word was sent back to Jezebel: 'Naboth has been stoned. He is dead.'"
    },
    "15": {
      "L": "As soon as Jezebel heard that Naboth had been stoned and was dead, Jezebel said to Ahab, 'Arise, take possession of the vineyard of Naboth the Jezreelite, which he refused to give you for money, for Naboth is not alive, but dead.'",
      "M": "As soon as Jezebel heard that Naboth had been stoned and was dead, she said to Ahab, 'Get up and take possession of the vineyard of Naboth the Jezreelite that he refused to sell you—for Naboth is dead, not alive.'",
      "T": "The moment Jezebel heard that Naboth was stoned and dead, she said to Ahab: 'Get up and take possession of the vineyard Naboth refused to sell you. He is dead. The vineyard is yours.'"
    },
    "16": {
      "L": "And as soon as Ahab heard that Naboth was dead, Ahab arose to go down to the vineyard of Naboth the Jezreelite to take possession of it.",
      "M": "As soon as Ahab heard that Naboth was dead, he arose and went down to the vineyard of Naboth the Jezreelite to take possession of it.",
      "T": "The moment Ahab heard Naboth was dead, he got up and went down to take possession of the vineyard."
    },
    "17": {
      "L": "Then the word of the LORD came to Elijah the Tishbite, saying,",
      "M": "Then the word of the LORD came to Elijah the Tishbite:",
      "T": "Then the word of the LORD came to Elijah the Tishbite:"
    },
    "18": {
      "L": "'Arise, go down to meet Ahab king of Israel, who is in Samaria. Behold, he is in the vineyard of Naboth, where he has gone down to take possession of it.'",
      "M": "'Go down to meet Ahab king of Israel, who is in Samaria. He is in Naboth's vineyard, where he has gone to take possession of it.'",
      "T": "'Go down to meet Ahab king of Israel who is in Samaria. He is in Naboth's vineyard—he has gone down to seize it.'"
    },
    "19": {
      "L": "'And you shall say to him, Thus says the LORD: Have you killed and also taken possession? And you shall say to him, Thus says the LORD: In the place where dogs licked up the blood of Naboth shall dogs lick your blood, even yours.'",
      "M": "'Say to him: Thus says the LORD: Have you murdered and then seized? And say to him: Thus says the LORD: In the very place where dogs licked up the blood of Naboth, dogs will lick your blood too.'",
      "T": "'Say to him: The LORD says this: You have murdered and now you seize. And say: The LORD says this: In the very place where dogs lapped up Naboth's blood, dogs will lap up your blood—your blood, Ahab.'"
    },
    "20": {
      "L": "Ahab said to Elijah, 'Have you found me, O my enemy?' He answered, 'I have found you, because you have sold yourself to do what is evil in the sight of the LORD.'",
      "M": "Ahab said to Elijah, 'Have you found me, my enemy?' He answered, 'I have found you—because you have sold yourself to do evil in the sight of the LORD.'",
      "T": "Ahab said to Elijah: 'So you have found me—my enemy?' Elijah answered: 'I have found you. Because you have sold yourself like a slave to do what is evil in the eyes of the LORD.'"
    },
    "21": {
      "L": "'Behold, I will bring evil upon you. I will utterly sweep you away and will cut off from Ahab every male, bond or free, in Israel.'",
      "M": "'I am about to bring disaster on you. I will sweep you away completely and cut off from Ahab every male, slave or free, in Israel.'",
      "T": "'I am bringing disaster on you. I will consume you utterly—I will cut off from Ahab every male, slave or free, in all of Israel.'"
    },
    "22": {
      "L": "'And I will make your house like the house of Jeroboam the son of Nebat, and like the house of Baasha the son of Ahijah, for the provocation with which you have provoked me to anger and have caused Israel to sin.'",
      "M": "'I will make your house like the house of Jeroboam son of Nebat and like the house of Baasha son of Ahijah, because of the way you have provoked me to anger and led Israel into sin.'",
      "T": "'I will make your dynasty like Jeroboam son of Nebat's—like Baasha son of Ahijah's—because you have provoked my anger and led Israel into sin.'"
    },
    "23": {
      "L": "'And of Jezebel the LORD also spoke, saying, The dogs shall eat Jezebel within the walls of Jezreel.'",
      "M": "'And concerning Jezebel the LORD also said: The dogs shall eat Jezebel in the plot of ground at Jezreel.'",
      "T": "'And of Jezebel the LORD has spoken: The dogs will devour Jezebel in the field of Jezreel.'"
    },
    "24": {
      "L": "'Anyone belonging to Ahab who dies in the city the dogs shall eat, and anyone of his who dies in the open country the birds of the heavens shall eat.'",
      "M": "'Anyone of Ahab's house who dies in the city the dogs will eat, and anyone who dies in the open country the birds of the air will eat.'",
      "T": "'Those of Ahab's house who die in the city—dogs will devour them. Those who die in the countryside—the birds of the sky will consume them.'"
    },
    "25": {
      "L": "(Indeed there was none like Ahab, who sold himself to do what was evil in the sight of the LORD, whom Jezebel his wife incited.)",
      "M": "(There was no one like Ahab who sold himself to do evil in the sight of the LORD, stirred up by Jezebel his wife.)",
      "T": "(No one sold himself to do evil in the LORD's sight like Ahab—and Jezebel his wife was the one who drove him to it.)"
    },
    "26": {
      "L": "He did very abominably in following idols, according to all that the Amorites had done, whom the LORD cast out before the people of Israel.",
      "M": "He acted very abominably by following after idols, just as the Amorites had done—those whom the LORD had driven out before Israel.",
      "T": "He was utterly detestable in his idol worship, following the Amorites' path—the very people the LORD had driven out before Israel."
    },
    "27": {
      "L": "And when Ahab heard those words, he tore his clothes and put sackcloth on his flesh and fasted and lay in sackcloth and went about dejectedly.",
      "M": "When Ahab heard those words, he tore his clothes, put on sackcloth next to his skin, fasted, lay in sackcloth, and went about in mourning.",
      "T": "When Ahab heard these words, he tore his clothes. He put on sackcloth directly against his skin, fasted, and walked around in mourning—genuinely shaken."
    },
    "28": {
      "L": "And the word of the LORD came to Elijah the Tishbite, saying,",
      "M": "Then the word of the LORD came to Elijah the Tishbite:",
      "T": "Then the word of the LORD came to Elijah the Tishbite:"
    },
    "29": {
      "L": "'Have you seen how Ahab has humbled himself before me? Because he has humbled himself before me, I will not bring the evil in his days; but in his son's days I will bring the evil upon his house.'",
      "M": "'Have you noticed how Ahab has humbled himself before me? Because he has humbled himself before me, I will not bring the disaster in his lifetime; but in his son's day I will bring disaster on his house.'",
      "T": "'Do you see how Ahab has humbled himself before me? Because he has done this—because he has genuinely humbled himself—I will not bring the disaster in his days. In his son's days I will bring it on his house.'"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1kings')
        merge_tier(existing, KINGS, tier_key)
        save(tier_dir, '1kings', existing)
    print('1 Kings 19–21 written.')

if __name__ == '__main__':
    main()
