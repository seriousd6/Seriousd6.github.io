"""
MKT Daniel chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-daniel-1-3.py

=== LANGUAGE NOTE ===
Daniel 1:1–2:3 is Hebrew. Daniel 2:4b–7:28 is Aramaic (including chs 2–3 here).
The Aramaic section begins when the Chaldeans respond in 2:4; the T tier of 2:4
flags this shift for the reader.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / LORD): Does NOT appear in Daniel 1–3. Daniel uses H136 (אֲדֹנָי /
  Lord) in 1:2 and "God of heaven" (אֱלָהּ שְׁמַיָּא) in the Aramaic sections.
  Rendered "the Lord" in 1:2 (L/M/T). No small-caps LORD needed here.

- H430 (אֱלֹהִים / God): "God" in all tiers. Daniel characteristically uses "God"
  and "God of heaven" rather than the divine personal name — a notable feature of
  the Babylonian context.

- H426 (Aramaic אֱלָהּ / God): "God" in all tiers, consistent with H430 rendering.
  "God of heaven" (אֱלָהּ שְׁמַיָּא) rendered "God of heaven" throughout.

- H5943 (Aramaic עֶלְיוֹן / Most High): "Most High God" in L/M/T (3:26). The
  Aramaic title emphasises God's supremacy over Babylonian deities — crucial in
  context of the furnace narrative.

- H7328 (Aramaic רָז / secret/mystery): "secret" in L (word-for-word);
  "mystery" in M and T. The Aramaic rāz (also a Persian loanword) is the
  central theological term of ch 2 — what human wisdom cannot penetrate but
  God freely discloses to his servants.

- H7307 (רוּחַ / spirit): 1:17 — God gives Daniel "understanding in all visions
  and dreams" (H2377 / H2472, not H7307). In 2:1 and 2:3, the king's spirit
  (H7307) is troubled — lowercase "spirit" (human faculty). In 2:1 the parallel
  term is H8142 (sleep). Lowercase throughout chs 1–3 for H7307.

- H2617 (חֶסֶד / steadfast love): In 1:9, God grants Daniel "favour and
  steadfast love" (H2617) before the chief official. L: "steadfast love";
  M: "compassion" (paired with H7356 / mercy); T surfaces the covenant
  dimension — the same hesed shown to Israel now working quietly in a pagan court.

- H6755 / Aramaic צֶלֶם (image/statue): "image" in L and M throughout ch 3.
  T uses "statue" where the physical object is in focus and "image" where
  the symbolic/theological resonance is foregrounded.

- Musical instruments (ch 3 refrain — H7162, H4953, H7030, H5443, H6460,
  H5481, H2170): L: "horn, pipe, lyre, trigon, harp, bagpipe, and every kind
  of music" (technical, source-faithful). M: same, standard English equivalents.
  T: "the full royal orchestra" in the repeated-refrain verses to avoid monotony
  while naming instruments fully in the decree (3:5, 3:10, 3:15).

- "Son of the gods" (3:25, Aramaic בַּר אֱלָהִין): The plural noun is Nebuchadnezzar's
  pagan idiom for "a divine being." L: "a son of the gods." M: "a divine being."
  T preserves the literal Aramaic phrase and notes the Christological reading
  without imposing it as the only sense.

- Aspect notes: Chapter 1 Hebrew narrative uses waw-consecutive imperfects (past
  narrative sequence). Chapter 2–3 Aramaic also uses past narrative. Aorist-like
  completive aspect rendered with English simple past throughout.
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

DANIEL = {
  "1": {
    "1": {
      "L": "In the third year of the reign of Jehoiakim king of Judah, Nebuchadnezzar king of Babylon came to Jerusalem and besieged it.",
      "M": "In the third year of Jehoiakim king of Judah's reign, Nebuchadnezzar king of Babylon came to Jerusalem and laid siege to it.",
      "T": "Three years into Jehoiakim's reign over Judah, Nebuchadnezzar of Babylon marched on Jerusalem and put the city under siege."
    },
    "2": {
      "L": "And the Lord gave Jehoiakim king of Judah into his hand, with part of the vessels of the house of God; and he carried them to the land of Shinar, to the house of his god, and placed the vessels in the treasury of his god.",
      "M": "The Lord gave Jehoiakim king of Judah into his power, along with part of the vessels of the house of God; he carried them to Babylonia, to the house of his god, and deposited the vessels in the treasury of his god.",
      "T": "The Lord handed Jehoiakim over to him and permitted part of the sacred vessels from God's house to be taken. Nebuchadnezzar carried them to Babylonia as trophies of his god's supposed victory — a misreading of an act that was God's own sovereign decision."
    },
    "3": {
      "L": "Then the king commanded Ashpenaz, his chief eunuch, to bring some of the sons of Israel, both of the royal line and of the nobility,",
      "M": "The king ordered Ashpenaz, his chief official, to bring some of the Israelites — from the royal family and the nobility —",
      "T": "The king instructed his chief official, Ashpenaz, to select young men from the Israelite royal family and aristocracy —"
    },
    "4": {
      "L": "youths without blemish, good in appearance, skilled in all wisdom, knowledgeable and discerning, and fit to stand in the king's palace, and to teach them the literature and language of the Chaldeans.",
      "M": "young men without physical defect, handsome, proficient in every branch of wisdom, well-informed, quick to learn, and qualified to serve in the royal palace — to be taught the literature and language of the Chaldeans.",
      "T": "physically flawless, handsome, broadly educated, intellectually sharp, and capable of court service. They were to be immersed in Babylonian learning and language — assimilation by design."
    },
    "5": {
      "L": "The king assigned them a daily portion of the food the king ate and of the wine he drank. They were to be educated for three years, and at the end of that time they were to stand before the king.",
      "M": "The king assigned them a daily ration from his own food and from the wine he drank. After three years of training, they were to enter the king's service.",
      "T": "The king provided for them from his own table — an honor meant to bind them to Babylonian identity. Three years of education, then an audience with the king himself."
    },
    "6": {
      "L": "Among these were Daniel, Hananiah, Mishael, and Azariah from the sons of Judah.",
      "M": "Among the young men chosen were Daniel, Hananiah, Mishael, and Azariah from the tribe of Judah.",
      "T": "Among those selected were four young men from Judah: Daniel, Hananiah, Mishael, and Azariah."
    },
    "7": {
      "L": "And the chief of the eunuchs gave them names: Daniel he called Belteshazzar, Hananiah he called Shadrach, Mishael he called Meshach, and Azariah he called Abednego.",
      "M": "The chief official assigned them new names: Daniel he called Belteshazzar, Hananiah Shadrach, Mishael Meshach, and Azariah Abednego.",
      "T": "The official replaced their Hebrew names — each of which honoured the God of Israel — with Babylonian names embedding pagan deities. Cultural erasure was systematic: Daniel became Belteshazzar, Hananiah became Shadrach, Mishael became Meshach, Azariah became Abednego."
    },
    "8": {
      "L": "But Daniel resolved in his heart that he would not defile himself with the king's food or with the wine he drank. Therefore he requested the chief of the eunuchs to allow him not to defile himself.",
      "M": "But Daniel was determined not to defile himself with the king's food or the wine he drank; he asked the chief official for permission to avoid this defilement.",
      "T": "Daniel drew a line at the royal table. Whatever the ground — ritual purity, food offered to idols, or simple covenant faithfulness — he would not compromise. He asked the chief official for permission to abstain."
    },
    "9": {
      "L": "And God gave Daniel favour and steadfast love before the chief of the eunuchs.",
      "M": "God granted Daniel favour and compassion in the eyes of the chief official.",
      "T": "God moved the official's heart toward Daniel — giving him both favourable regard and genuine goodwill. The same covenant loyalty God had always shown Israel was now quietly at work inside a Babylonian court."
    },
    "10": {
      "L": "The chief of the eunuchs said to Daniel, 'I fear my lord the king, who appointed your food and your drink; for why should he see your faces looking worse than the youths of your own age? You would endanger my head with the king.'",
      "M": "The chief official said to Daniel, 'I am afraid of my lord the king, who assigned your food and drink. If he sees you looking more haggard than the other young men your age, you will put my life at risk with the king.'",
      "T": "The official understood the request but could not afford it: 'The king personally set your diet. If he sees you looking worse than the others, he will have my head for it. I can't risk that.'"
    },
    "11": {
      "L": "Then Daniel spoke to the steward whom the chief of the eunuchs had assigned over Daniel, Hananiah, Mishael, and Azariah:",
      "M": "So Daniel went to the steward whom the chief official had appointed over Daniel, Hananiah, Mishael, and Azariah,",
      "T": "Daniel went around him, speaking directly to the steward the official had placed over the four of them —"
    },
    "12": {
      "L": "'Please test your servants for ten days; let us be given vegetables to eat and water to drink.'",
      "M": "'Please test your servants for ten days: give us only vegetables to eat and water to drink.'",
      "T": "'Try us for ten days — nothing but vegetables and water. Then judge by what you see.'"
    },
    "13": {
      "L": "'Then let our appearance and the appearance of the youths who eat the king's food be observed by you, and deal with your servants as you see fit.'",
      "M": "'Then compare our appearance with the young men eating the king's food, and treat your servants accordingly.'",
      "T": "'Compare how we look against those eating the royal diet. Decide based on what you observe.'"
    },
    "14": {
      "L": "So he listened to them in this matter and tested them for ten days.",
      "M": "He agreed to their request and tested them for ten days.",
      "T": "The steward agreed and gave them ten days."
    },
    "15": {
      "L": "At the end of ten days it was seen that they were better in appearance and fatter in flesh than all the youths who had been eating the king's food.",
      "M": "At the end of the ten days, they looked healthier and better nourished than all the young men who had been eating the king's food.",
      "T": "Ten days later, Daniel and his friends were visibly healthier and better fed than everyone eating from the royal table."
    },
    "16": {
      "L": "So the steward took away their food and the wine they were to drink, and gave them vegetables.",
      "M": "So the steward removed their assigned food and wine and gave them vegetables instead.",
      "T": "The steward quietly dropped their royal rations and kept them on vegetables from then on."
    },
    "17": {
      "L": "As for these four youths, God gave them learning and skill in all literature and wisdom, and Daniel had understanding in all visions and dreams.",
      "M": "God gave these four young men knowledge and skill in every branch of literature and wisdom; and to Daniel he gave also the ability to interpret visions and dreams.",
      "T": "God gave all four of them an exceptional mind for learning — mastery across every field of Babylonian knowledge. To Daniel he gave an additional gift: the capacity to understand visions and dreams."
    },
    "18": {
      "L": "At the end of the days the king had set for bringing them in, the chief of the eunuchs brought them before Nebuchadnezzar.",
      "M": "At the end of the period the king had set, the chief official presented them before Nebuchadnezzar.",
      "T": "When the three-year programme ended, the chief official brought them before Nebuchadnezzar as commanded."
    },
    "19": {
      "L": "And the king spoke with them, and among them all none was found like Daniel, Hananiah, Mishael, and Azariah. Therefore they stood before the king.",
      "M": "The king spoke with each of them, and none was found equal to Daniel, Hananiah, Mishael, and Azariah; so they entered the king's service.",
      "T": "The king examined them all personally. No one matched Daniel and his three friends. They were appointed to stand in the royal court."
    },
    "20": {
      "L": "And in every matter of wisdom and understanding about which the king inquired of them, he found them ten times better than all the magicians and enchanters in all his kingdom.",
      "M": "In every matter of wisdom and understanding the king put to them, he found them ten times superior to all the magicians and enchanters in his entire realm.",
      "T": "Whenever the king tested them on anything requiring wisdom or discernment, they outperformed the entire court of sorcerers and astrologers by a factor of ten."
    },
    "21": {
      "L": "And Daniel was there until the first year of King Cyrus.",
      "M": "Daniel remained in royal service until the first year of King Cyrus.",
      "T": "Daniel served in that court all the way to the first year of Cyrus — from the opening of Babylonian supremacy to the dawn of Persian rule. A life spanning empires."
    }
  },
  "2": {
    "1": {
      "L": "In the second year of the reign of Nebuchadnezzar, Nebuchadnezzar dreamed dreams; his spirit was troubled and his sleep left him.",
      "M": "In the second year of Nebuchadnezzar's reign, he had disturbing dreams; his spirit was agitated and sleep escaped him.",
      "T": "Two years into his reign, Nebuchadnezzar was tormented by dreams. His mind gave him no peace and sleep abandoned him."
    },
    "2": {
      "L": "Then the king commanded to summon the magicians, the enchanters, the sorcerers, and the Chaldeans, to tell the king his dreams. And they came and stood before the king.",
      "M": "The king ordered the magicians, enchanters, sorcerers, and Chaldeans to be summoned to explain his dreams. They came and stood before him.",
      "T": "He called in the full apparatus of Babylonian divination — magicians, enchanters, sorcerers, Chaldean astrologers — and demanded they explain his dreams. They assembled."
    },
    "3": {
      "L": "And the king said to them, 'I have dreamed a dream, and my spirit is troubled to know the dream.'",
      "M": "The king said to them, 'I have had a dream, and my spirit is troubled; I must know what it means.'",
      "T": "'I have had a dream,' he told them, 'and I am desperate to understand it.'"
    },
    "4": {
      "L": "Then the Chaldeans spoke to the king in Aramaic: 'O king, live forever! Tell your servants the dream, and we will declare the interpretation.'",
      "M": "The Chaldeans responded to the king in Aramaic: 'O king, live forever! Tell us the dream, and we will give you the interpretation.'",
      "T": "[The text of Daniel now shifts to Aramaic and remains in Aramaic through 7:28.] The Chaldeans replied in the imperial tongue: 'Long live the king! Tell us your dream and we will interpret it.'"
    },
    "5": {
      "L": "The king answered and said to the Chaldeans, 'The word from me is gone forth: if you do not make known to me the dream and its interpretation, you will be torn limb from limb and your houses made a dunghill.'",
      "M": "The king replied to the Chaldeans, 'My decree is firm: if you cannot make known to me the dream and its interpretation, you will be torn limb from limb and your houses turned to rubble.'",
      "T": "'My decree is already issued,' the king said. 'If you cannot tell me what I dreamed and explain it, you will be torn apart and your homes demolished.'"
    },
    "6": {
      "L": "'But if you tell me the dream and its interpretation, you will receive from me gifts and rewards and great honour. Therefore tell me the dream and its interpretation.'",
      "M": "'But if you do give me the dream and its interpretation, you will receive gifts, rewards, and great honour from me. So declare the dream and its interpretation.'",
      "T": "'On the other hand, tell me the dream and its meaning and I will lavish gifts and honours on you. The choice is yours.'"
    },
    "7": {
      "L": "They answered a second time and said, 'Let the king tell his servants the dream, and we will declare its interpretation.'",
      "M": "They answered again: 'Let the king tell his servants the dream, and we will give the interpretation.'",
      "T": "They tried once more: 'Just tell us the dream, Your Majesty, and we will interpret it.'"
    },
    "8": {
      "L": "The king answered and said, 'I know with certainty that you are trying to gain time, because you see that the word from me is firm.'",
      "M": "The king replied, 'I know for certain you are stalling for time, because you see my decree stands.'",
      "T": "'I see exactly what you are doing,' the king said. 'You are buying time because you know my order is final.'"
    },
    "9": {
      "L": "'If you do not make the dream known to me, there is but one sentence for you. You have agreed to speak before me lying and corrupt words until the situation changes. Therefore tell me the dream, and I will know that you can declare its interpretation.'",
      "M": "'If you do not make the dream known to me, there is only one verdict for you all. You have conspired to tell me lies and stalling words until circumstances change. Tell me the dream, and then I will know you can interpret it.'",
      "T": "'There is one verdict waiting for you if you fail. You are stalling, hoping things change. Prove you are genuine: tell me the dream first. Then I will believe your interpretation.'"
    },
    "10": {
      "L": "The Chaldeans answered before the king and said, 'There is no man on earth who can declare the king's matter, inasmuch as no great and powerful king has ever asked such a thing of any magician, enchanter, or Chaldean.'",
      "M": "The Chaldeans replied to the king, 'There is not a man on earth who can tell the king what he demands, for no great and powerful king has ever made such a request of any magician, enchanter, or Chaldean.'",
      "T": "The Chaldeans were forced to admit the truth: 'No one on earth can do what the king is asking. No great king has ever demanded this of his advisors. It is simply impossible.'"
    },
    "11": {
      "L": "'And the thing that the king asks is difficult, and no one can declare it to the king except the gods, whose dwelling is not with flesh.'",
      "M": "'What the king demands is too difficult; no one can reveal it except the gods, who do not dwell among mortals.'",
      "T": "'What you are asking lies beyond human capacity. Only the gods could know this — and the gods do not live among us.'"
    },
    "12": {
      "L": "Because of this the king was angry and very furious, and commanded that all the wise men of Babylon be destroyed.",
      "M": "At this, the king became furiously angry and ordered all the wise men of Babylon to be executed.",
      "T": "The king erupted. He ordered every wise man in Babylon put to death."
    },
    "13": {
      "L": "So the decree went out, and the wise men were about to be killed; and they sought Daniel and his companions, to kill them.",
      "M": "The decree was issued and the wise men were being rounded up to be killed; soldiers were sent to find Daniel and his companions as well.",
      "T": "The execution order went into effect. When soldiers came looking for Daniel and his friends, the situation was desperate."
    },
    "14": {
      "L": "Then Daniel answered with prudence and discretion to Arioch, the captain of the king's guard, who had gone out to kill the wise men of Babylon.",
      "M": "Daniel responded with tact and wisdom to Arioch, the commander of the king's guard, who had been dispatched to execute the wise men of Babylon.",
      "T": "Daniel responded to Arioch — the man in charge of the executions — with remarkable composure and good judgment."
    },
    "15": {
      "L": "He asked Arioch, the king's officer, 'Why is the decree so urgent from the king?' Then Arioch made the matter known to Daniel.",
      "M": "He asked Arioch, 'Why is the king's decree so drastic?' And Arioch explained the situation to Daniel.",
      "T": "'Why is the king's order so extreme?' Daniel asked. Arioch told him everything."
    },
    "16": {
      "L": "And Daniel went in and requested the king to give him time, that he might show the king the interpretation.",
      "M": "Daniel went to the king and asked for time, promising that he would bring the king the interpretation.",
      "T": "Daniel went to the king personally and asked for time — promising to deliver the interpretation."
    },
    "17": {
      "L": "Then Daniel went to his house and made the matter known to Hananiah, Mishael, and Azariah, his companions,",
      "M": "Daniel went home and explained the situation to his companions Hananiah, Mishael, and Azariah.",
      "T": "Daniel went straight home and told his three friends everything."
    },
    "18": {
      "L": "and told them to seek mercy from the God of heaven concerning this mystery, so that Daniel and his companions might not be destroyed with the rest of the wise men of Babylon.",
      "M": "He urged them to plead for mercy from the God of heaven about this mystery, so that they and the rest of Babylon's wise men would not be put to death.",
      "T": "He asked them to pray urgently — to call on the God of heaven for mercy about this hidden thing. Their lives, and the lives of everyone in Babylon's court, depended on it."
    },
    "19": {
      "L": "Then the mystery was revealed to Daniel in a vision of the night. Then Daniel blessed the God of heaven.",
      "M": "Then the mystery was revealed to Daniel in a night vision, and Daniel praised the God of heaven.",
      "T": "That night, God revealed the mystery to Daniel in a vision. Daniel's first response was to break into praise."
    },
    "20": {
      "L": "Daniel answered and said: 'Blessed be the name of God forever and ever, for wisdom and might are his.'",
      "M": "Daniel said: 'Blessed be the name of God forever and ever, for wisdom and power belong to him.'",
      "T": "'Blessed be God's name, world without end — for wisdom and power belong to him alone.'"
    },
    "21": {
      "L": "'He changes times and seasons; he removes kings and sets up kings; he gives wisdom to the wise and knowledge to those who have understanding.'",
      "M": "'He changes times and seasons; he removes kings and establishes kings; he gives wisdom to the wise and knowledge to those with discernment.'",
      "T": "'He overturns epochs and reshapes eras. He strips kings from their thrones and raises others to power. He gives the wise deeper wisdom and the discerning sharper sight.'"
    },
    "22": {
      "L": "'He reveals deep and hidden things; he knows what is in the darkness, and the light dwells with him.'",
      "M": "'He uncovers what is deep and hidden; he knows what lies in the darkness, and light itself resides with him.'",
      "T": "'He discloses what has been sealed away in shadow. Darkness holds no secrets from him, for light itself lives in his presence.'"
    },
    "23": {
      "L": "'To you, O God of my fathers, I give thanks and praise, for you have given me wisdom and might, and have now made known to me what we asked of you, for you have made known to us the king's matter.'",
      "M": "'To you, O God of my fathers, I give thanks and praise; you have given me wisdom and strength, and have made known to me what we asked — you have revealed to us the king's concern.'",
      "T": "'God of my ancestors — thank you. You gave me wisdom and the strength to stand in this moment. You answered our prayer and told us what the king needed to know.'"
    },
    "24": {
      "L": "Therefore Daniel went to Arioch, whom the king had appointed to destroy the wise men of Babylon, and said to him, 'Do not destroy the wise men of Babylon; bring me before the king, and I will declare the interpretation to the king.'",
      "M": "Daniel went to Arioch, whom the king had ordered to execute Babylon's wise men, and said, 'Do not kill the wise men of Babylon. Bring me before the king and I will give him the interpretation.'",
      "T": "Daniel went immediately to Arioch. 'Stop the executions,' he said. 'Take me to the king. I have the interpretation.'"
    },
    "25": {
      "L": "Then Arioch brought Daniel before the king in haste and said to him, 'I have found among the exiles of Judah a man who can make known the interpretation to the king.'",
      "M": "Arioch hurried Daniel in to the king and announced, 'I have found a man among the Judean exiles who can give the king the interpretation.'",
      "T": "Arioch rushed Daniel into the royal presence. 'I have found him,' he said — taking credit for a discovery that was entirely God's."
    },
    "26": {
      "L": "The king declared to Daniel, whose name was Belteshazzar, 'Are you able to make known to me the dream that I saw and its interpretation?'",
      "M": "The king asked Daniel, who had been given the name Belteshazzar, 'Can you really tell me the dream I had and explain what it means?'",
      "T": "The king turned to Daniel — the exile renamed Belteshazzar — and asked: 'Can you actually do this? Can you tell me my dream and its meaning?'"
    },
    "27": {
      "L": "Daniel answered before the king and said, 'No wise man, enchanter, magician, or astrologer can declare to the king the mystery that the king has demanded.'",
      "M": "Daniel answered the king, 'No wise man, enchanter, magician, or diviner is able to tell the king the mystery he has demanded.'",
      "T": "'The mystery the king is asking about,' Daniel said, 'lies beyond every form of human wisdom. No sage, no sorcerer, no astrologer has access to it.'"
    },
    "28": {
      "L": "'But there is a God in heaven who reveals mysteries, and he has made known to King Nebuchadnezzar what will be in the latter days. Your dream and the visions of your head as you lay in bed are these:'",
      "M": "'But there is a God in heaven who reveals mysteries, and he has shown King Nebuchadnezzar what will take place in the last days. This is the dream and what you envisioned as you lay in bed:'",
      "T": "'But there is a God in heaven — and he discloses hidden things. He has shown you, Nebuchadnezzar, the shape of what is coming. Let me tell you what you saw as you lay in bed that night.'"
    },
    "29": {
      "L": "'As for you, O king, thoughts came to your mind on your bed about what would be after this, and he who reveals mysteries made known to you what is to be.'",
      "M": "'As you lay in bed, O king, your thoughts turned to what would come after this, and the revealer of mysteries has shown you what is to come.'",
      "T": "'Your mind was wrestling with the future — what comes after your empire? — and God, the revealer of secrets, answered that very question in your sleep.'"
    },
    "30": {
      "L": "'But as for me, this mystery has not been revealed to me because of any wisdom in me more than in any other living person, but so that the interpretation may be made known to the king and that you may know the thoughts of your heart.'",
      "M": "'As for me, this mystery was not revealed to me because I have more wisdom than anyone else, but so that the interpretation could be made known to the king, and so that you might understand the thoughts of your own heart.'",
      "T": "'And I want you to understand, O king: the reason God showed me this was not because I am wiser than anyone else. It was for your sake — so you could receive the interpretation and understand what your own heart was asking.'"
    },
    "31": {
      "L": "'You saw, O king, and behold, a great image. This image, mighty and of exceeding brightness, stood before you, and its form was frightening.'",
      "M": "'You saw, O king, and before you stood a great statue — towering, brilliantly bright, and terrifying in appearance.'",
      "T": "'In your dream you saw an enormous statue standing before you — blazing with light, overpowering in its presence, and terrifying to behold.'"
    },
    "32": {
      "L": "'The head of this image was of fine gold, its chest and arms of silver, its middle and thighs of bronze,'",
      "M": "'The head of the statue was made of pure gold, its chest and arms of silver, its middle and thighs of bronze,'",
      "T": "'The head was pure gold. The chest and arms were silver. The belly and thighs were bronze.'"
    },
    "33": {
      "L": "'its legs of iron, its feet partly of iron and partly of clay.'",
      "M": "'its legs of iron, its feet a mixture of iron and clay.'",
      "T": "'The legs were iron. And the feet — iron mixed with clay, already carrying the seeds of fragility within apparent strength.'"
    },
    "34": {
      "L": "'As you watched, a stone was cut out by no human hand, and it struck the image on its feet of iron and clay, and broke them in pieces.'",
      "M": "'As you watched, a stone was cut from a mountain — not by human hands — and it struck the statue at the feet of iron and clay and shattered them.'",
      "T": "'Then you saw a stone break free from a mountain — no human hands involved. It struck those feet of iron and clay and shattered them.'"
    },
    "35": {
      "L": "'Then the iron, the clay, the bronze, the silver, and the gold, all together were broken in pieces and became like the chaff of the summer threshing floors; and the wind carried them away, so that not a trace of them could be found. But the stone that struck the image became a great mountain and filled the whole earth.'",
      "M": "'The iron, clay, bronze, silver, and gold were all shattered together and became like chaff on a summer threshing floor; the wind swept them away without leaving a trace. But the stone that struck the statue became a great mountain that filled the entire earth.'",
      "T": "'The whole statue — every metal tier — exploded to dust like summer chaff and the wind scattered it, leaving nothing at all. But that stone grew into a mountain that covered the earth.'"
    },
    "36": {
      "L": "'This was the dream. Now we will tell the king its interpretation.'",
      "M": "'That was the dream. Now we will tell the king its interpretation.'",
      "T": "'That is your dream. Now here is what it means.'"
    },
    "37": {
      "L": "'You, O king, the king of kings, to whom the God of heaven has given the kingdom, the power, the might, and the glory,'",
      "M": "'You, O king, king of kings — to whom the God of heaven has given the kingdom, the power, the might, and the glory —'",
      "T": "'You, O king, are king of kings. The God of heaven himself gave you this empire — its dominion, its power, and its glory.'"
    },
    "38": {
      "L": "'and into whose hand he has given, wherever they dwell, the children of man, the beasts of the field, and the birds of the heavens, making you ruler over them all — you are the head of gold.'",
      "M": "'and into whose hand he has given authority over all who live on the earth, the wild beasts, and the birds of the sky — making you ruler over them all. You are that head of gold.'",
      "T": "'He placed under your rule every human being, every creature of the field, every bird of the sky. You have dominion over it all. You are the head of gold.'"
    },
    "39": {
      "L": "'After you shall arise another kingdom inferior to you, and yet a third kingdom of bronze, which shall rule over all the earth.'",
      "M": "'After you, another kingdom will arise, lesser than yours; then a third, a kingdom of bronze, which will extend its rule over all the earth.'",
      "T": "'But after you comes another empire — lesser in glory. And after that a third, symbolised by bronze, that will spread its dominion across the entire earth.'"
    },
    "40": {
      "L": "'And there shall be a fourth kingdom, strong as iron, because iron breaks in pieces and shatters all things. And like iron that crushes, it shall break and shatter all these.'",
      "M": "'Then a fourth kingdom will come, strong as iron — for iron shatters and smashes everything. Like iron, it will crush and demolish all the others.'",
      "T": "'Then a fourth kingdom — brutal as iron. Iron breaks everything. This empire will crush and shatter every rival without mercy.'"
    },
    "41": {
      "L": "'And as you saw the feet and toes, partly of potter's clay and partly of iron, it shall be a divided kingdom, but it shall have some of the strength of iron, just as you saw iron mixed with the muddy clay.'",
      "M": "'As for the feet and toes you saw, partly of potter's clay and partly of iron — it will be a divided kingdom. It will retain some iron strength, but it will be mixed, just as you saw iron combined with soft clay.'",
      "T": "'But those feet — iron mixed with common clay — reveal a divided kingdom. Some of the old iron strength remains, but the foundation is fundamentally compromised.'"
    },
    "42": {
      "L": "'And as the toes of the feet were partly iron and partly clay, so the kingdom shall be partly strong and partly brittle.'",
      "M": "'As the toes were partly iron and partly clay, so the kingdom will be partly strong and partly fragile.'",
      "T": "'Iron strength alongside brittle clay — powerful in some respects, breakable in others.'"
    },
    "43": {
      "L": "'As you saw the iron mixed with muddy clay, so they will mix with one another in marriage, but they will not hold together, just as iron does not mix with clay.'",
      "M": "'Just as you saw the iron mixed with clay, these peoples will seek to unite through intermarriage, but they will not hold together, just as iron and clay do not bond.'",
      "T": "'They will try to hold it together through political marriages and alliances, but the union will not last. Iron and clay do not bond.'"
    },
    "44": {
      "L": "'And in the days of those kings, the God of heaven will set up a kingdom that shall never be destroyed, nor shall the kingdom be left to another people. It shall break in pieces all these kingdoms and bring them to an end, and it shall stand forever,'",
      "M": "'In the time of those kings, the God of heaven will establish a kingdom that will never be destroyed or surrendered to another people. It will shatter all those kingdoms and bring them to an end, and it will endure forever.'",
      "T": "'But in the time of those last kingdoms, the God of heaven will establish a kingdom that cannot be destroyed or transferred. It will grind those kingdoms to dust and stand forever.'"
    },
    "45": {
      "L": "'just as you saw that a stone was cut from a mountain by no human hand, and that it broke in pieces the iron, the bronze, the clay, the silver, and the gold. A great God has made known to the king what shall be after this. The dream is certain, and its interpretation is trustworthy.'",
      "M": "'This corresponds to the stone cut from the mountain without human hands, which broke in pieces the iron, bronze, clay, silver, and gold. The great God has revealed to the king what will come to pass. The dream is certain, and the interpretation reliable.'",
      "T": "'That stone cut without hands — shattering everything in its path — is the kingdom of God himself. The great God has shown you the arc of history from now to the end. This is a certain word. You can trust it.'"
    },
    "46": {
      "L": "Then King Nebuchadnezzar fell upon his face and worshipped Daniel, and commanded that an offering and incense be offered to him.",
      "M": "Then King Nebuchadnezzar fell on his face and paid homage to Daniel, and ordered that offerings and incense be presented to him.",
      "T": "Nebuchadnezzar was so overwhelmed that he fell face-down before Daniel and ordered sacrifices and incense burned in his honour — mistaking the messenger for the source."
    },
    "47": {
      "L": "The king answered Daniel and said, 'Truly, your God is God of gods and Lord of kings, and a revealer of mysteries, for you have been able to reveal this mystery.'",
      "M": "The king said to Daniel, 'Truly, your God is the God of gods and Lord of kings, and a revealer of mysteries, for you were able to reveal this mystery.'",
      "T": "'Your God is the God above all gods, the Lord above all kings, the revealer of what is hidden,' Nebuchadnezzar declared. 'You have proved it.'"
    },
    "48": {
      "L": "Then the king gave Daniel great gifts and many honours, and made him ruler over the whole province of Babylon and chief prefect over all the wise men of Babylon.",
      "M": "The king lavished Daniel with great gifts and many honours, and appointed him ruler over the entire province of Babylon and chief official over all Babylon's wise men.",
      "T": "The king heaped gifts on Daniel and elevated him to the highest positions in the empire — ruler of Babylon's province and chief over all its court sages."
    },
    "49": {
      "L": "Daniel requested the king, and he appointed Shadrach, Meshach, and Abednego over the affairs of the province of Babylon. But Daniel was at the king's court.",
      "M": "At Daniel's request, the king appointed Shadrach, Meshach, and Abednego over the administration of the province of Babylon, while Daniel himself remained at the royal court.",
      "T": "Daniel used his new position to secure appointments for his three friends: Shadrach, Meshach, and Abednego were placed over Babylon's provincial administration. Daniel himself stayed at the centre of power."
    }
  },
  "3": {
    "1": {
      "L": "Nebuchadnezzar the king made an image of gold, its height sixty cubits, its breadth six cubits. He set it up on the plain of Dura, in the province of Babylon.",
      "M": "King Nebuchadnezzar made a golden statue sixty cubits tall and six cubits wide, and erected it on the plain of Dura in the province of Babylon.",
      "T": "Nebuchadnezzar commissioned a colossal golden statue — sixty cubits tall, six cubits wide — and set it up on the plain of Dura. His empire was at its peak; the statue announced it."
    },
    "2": {
      "L": "Then King Nebuchadnezzar sent to assemble the satraps, the prefects, and the governors, the counsellors, the treasurers, the justices, the magistrates, and all the officials of the provinces to come to the dedication of the image that King Nebuchadnezzar had set up.",
      "M": "King Nebuchadnezzar sent word to assemble the satraps, prefects, governors, counsellors, treasurers, judges, magistrates, and all the provincial officials to attend the dedication of the image he had erected.",
      "T": "The king summoned the entire imperial bureaucracy — every rank of official from every province — to the dedication ceremony."
    },
    "3": {
      "L": "Then the satraps, the prefects, and the governors, the counsellors, the treasurers, the justices, the magistrates, and all the officials of the provinces assembled for the dedication of the image that King Nebuchadnezzar had set up. And they stood before the image that Nebuchadnezzar had set up.",
      "M": "The satraps, prefects, governors, counsellors, treasurers, judges, magistrates, and all the provincial officials gathered for the dedication of the image King Nebuchadnezzar had erected, and they stood before the image.",
      "T": "They all came — every tier of imperial authority gathered on the plain — and stood before the gleaming statue."
    },
    "4": {
      "L": "And a herald cried aloud, 'You are commanded, O peoples, nations, and languages:'",
      "M": "Then a herald cried out in a loud voice, 'You are commanded, O peoples, nations, and languages:'",
      "T": "A royal herald shouted the decree across the assembled crowd: 'Hear this — every people, every nation, every tongue:'"
    },
    "5": {
      "L": "'that when you hear the sound of the horn, the pipe, the lyre, the trigon, the harp, the bagpipe, and every kind of music, you are to fall down and worship the golden image that King Nebuchadnezzar has set up.'",
      "M": "'at the sound of the horn, pipe, lyre, trigon, harp, bagpipe, and every kind of music, you must fall down and worship the golden image that King Nebuchadnezzar has erected.'",
      "T": "'The moment the royal orchestra plays, you are to fall face-down and worship the golden statue that King Nebuchadnezzar has erected.'"
    },
    "6": {
      "L": "'And whoever does not fall down and worship shall immediately be cast into a burning fiery furnace.'",
      "M": "'Anyone who does not fall down and worship will immediately be thrown into a burning fiery furnace.'",
      "T": "'Anyone who refuses will be thrown immediately into a furnace of blazing fire.'"
    },
    "7": {
      "L": "Therefore at that time, when all the peoples heard the sound of the horn, the pipe, the lyre, the trigon, the harp, and every kind of music, all the peoples, nations, and languages fell down and worshipped the golden image that King Nebuchadnezzar had set up.",
      "M": "So when all the peoples heard the sound of the horn, pipe, lyre, trigon, harp, and every kind of music, all the peoples, nations, and languages fell down and worshipped the golden image King Nebuchadnezzar had erected.",
      "T": "When the music began, the assembled multitude fell prostrate before the statue. Every nation. Every tongue. Except three."
    },
    "8": {
      "L": "Therefore at that time certain Chaldeans came forward and maliciously accused the Jews.",
      "M": "At that moment certain Chaldeans stepped forward and brought accusations against the Jews.",
      "T": "Immediately, certain Chaldean officials seized the moment and filed formal charges against the Jewish administrators."
    },
    "9": {
      "L": "They declared to King Nebuchadnezzar, 'O king, live forever!'",
      "M": "They said to King Nebuchadnezzar, 'O king, live forever!'",
      "T": "They approached the king with the customary greeting: 'Long live the king!'"
    },
    "10": {
      "L": "'You, O king, have made a decree, that every man who hears the sound of the horn, the pipe, the lyre, the trigon, the harp, the bagpipe, and every kind of music shall fall down and worship the golden image.'",
      "M": "'You, O king, have issued a decree that everyone who hears the horn, pipe, lyre, trigon, harp, bagpipe, and every kind of music must fall down and worship the golden image.'",
      "T": "'Your Majesty himself decreed it: at the sound of the royal orchestra, all must bow to the golden statue.'"
    },
    "11": {
      "L": "'And whoever does not fall down and worship shall be cast into a burning fiery furnace.'",
      "M": "'And anyone who refuses to fall down and worship is to be cast into a burning fiery furnace.'",
      "T": "'The penalty for refusal is the furnace.'"
    },
    "12": {
      "L": "'There are certain Jews, whom you have appointed over the affairs of the province of Babylon: Shadrach, Meshach, and Abednego. These men, O king, pay no attention to you; they do not serve your gods or worship the golden image that you have set up.'",
      "M": "'But there are certain Jewish men, O king, whom you appointed over the province of Babylon — Shadrach, Meshach, and Abednego — who have disregarded your command; they do not serve your gods or worship the golden image you erected.'",
      "T": "'Three of the men you yourself appointed — Shadrach, Meshach, and Abednego — have defied you openly. They will not serve your gods. They would not bow to the statue.'"
    },
    "13": {
      "L": "Then Nebuchadnezzar in furious rage commanded to bring Shadrach, Meshach, and Abednego. Then these men were brought before the king.",
      "M": "In furious rage, Nebuchadnezzar ordered Shadrach, Meshach, and Abednego brought before him, and they were brought to the king.",
      "T": "Nebuchadnezzar erupted. He ordered the three men brought before him at once."
    },
    "14": {
      "L": "Nebuchadnezzar declared to them, 'Is it true, O Shadrach, Meshach, and Abednego, that you do not serve my gods or worship the golden image that I have set up?'",
      "M": "Nebuchadnezzar said to them, 'Is it really true, Shadrach, Meshach, and Abednego — that you refuse to serve my gods and worship the golden image I erected?'",
      "T": "'Is this actually true?' he demanded. 'You — Shadrach, Meshach, Abednego — you refuse to serve my gods? You would not bow to my statue?'"
    },
    "15": {
      "L": "'Now if you are ready, when you hear the sound of the horn, the pipe, the lyre, the trigon, the harp, the bagpipe, and every kind of music, to fall down and worship the image that I have made, well and good. But if you do not worship, you shall immediately be cast into a burning fiery furnace. And who is the god who will deliver you out of my hands?'",
      "M": "'Now if you are ready, when you hear the horn, pipe, lyre, trigon, harp, bagpipe, and every kind of music, to fall down and worship the image I made — very well. But if you do not worship, you will immediately be thrown into a burning fiery furnace. And what god can rescue you from my power?'",
      "T": "'I will give you one more chance: when the orchestra plays, bow down and we will say nothing more. But refuse — and into the furnace you go. And let me ask you: which god is going to rescue you from me?'"
    },
    "16": {
      "L": "Shadrach, Meshach, and Abednego answered and said to the king, 'O Nebuchadnezzar, we have no need to answer you in this matter.'",
      "M": "Shadrach, Meshach, and Abednego replied to the king, 'O Nebuchadnezzar, we have no need to defend ourselves to you in this matter.'",
      "T": "The three answered without hesitation: 'Nebuchadnezzar, we have nothing to explain to you.'"
    },
    "17": {
      "L": "'If this be so, our God whom we serve is able to deliver us from the burning fiery furnace, and he will deliver us out of your hand, O king.'",
      "M": "'If we are thrown in, the God we serve is able to rescue us from the burning fiery furnace, and he will deliver us from your power, O king.'",
      "T": "'If you throw us in, the God we serve can deliver us from that furnace — and he will deliver us from you.'"
    },
    "18": {
      "L": "'But if not, be it known to you, O king, that we will not serve your gods or worship the golden image that you have set up.'",
      "M": "'But even if he does not, know this, O king: we will not serve your gods or worship the golden image you have set up.'",
      "T": "'But even if he chooses not to — know this: we will not serve your gods. We will not bow to your statue. That is final.'"
    },
    "19": {
      "L": "Then Nebuchadnezzar was filled with fury, and the form of his face was changed against Shadrach, Meshach, and Abednego. He ordered the furnace to be heated seven times more than it was customarily heated.",
      "M": "Then Nebuchadnezzar was filled with rage, and his expression changed toward Shadrach, Meshach, and Abednego. He ordered the furnace heated seven times hotter than usual.",
      "T": "Nebuchadnezzar's face contorted with fury. He ordered the furnace heated seven times its normal temperature — pure rage, not rational calculation."
    },
    "20": {
      "L": "And he ordered some of the mighty men of his army to bind Shadrach, Meshach, and Abednego, and to cast them into the burning fiery furnace.",
      "M": "He commanded some of the strongest soldiers in his army to bind Shadrach, Meshach, and Abednego and throw them into the burning fiery furnace.",
      "T": "He ordered his strongest soldiers to bind them and hurl them in."
    },
    "21": {
      "L": "Then these men were bound in their cloaks, their tunics, their hats, and their other garments, and were cast into the burning fiery furnace.",
      "M": "The men were bound fully clothed — wearing their robes, tunics, hats, and other garments — and thrown into the burning fiery furnace.",
      "T": "They were bound as they stood — not even stripped — and thrown into the furnace fully dressed."
    },
    "22": {
      "L": "Because the king's command was urgent and the furnace was very hot, the flame of the fire killed those men who took up Shadrach, Meshach, and Abednego.",
      "M": "Because the king's order was so urgent and the furnace had been heated to extreme temperatures, the flame of fire killed the soldiers who carried the three men to the opening.",
      "T": "The furnace was so ferociously overheated that the soldiers who threw them in were themselves killed by the flames that leapt from the mouth."
    },
    "23": {
      "L": "And these three men, Shadrach, Meshach, and Abednego, fell bound into the burning fiery furnace.",
      "M": "And the three men — Shadrach, Meshach, and Abednego — fell bound into the burning fiery furnace.",
      "T": "The three fell — bound — into the heart of the fire."
    },
    "24": {
      "L": "Then King Nebuchadnezzar was astonished and rose up quickly. He declared to his counsellors, 'Did we not cast three men bound into the fire?' They answered and said to the king, 'True, O king.'",
      "M": "Then King Nebuchadnezzar leaped to his feet in shock. He said to his counsellors, 'Didn't we throw three men, bound, into the fire?' 'Certainly, Your Majesty,' they replied.",
      "T": "Nebuchadnezzar lurched to his feet in alarm. 'Did we not throw three men — bound — into the fire?' 'Yes, of course,' his officials confirmed."
    },
    "25": {
      "L": "He answered and said, 'But I see four men unbound, walking in the midst of the fire, and they are not hurt; and the appearance of the fourth is like a son of the gods.'",
      "M": "He declared, 'Look! I see four men walking freely in the fire, unharmed — and the fourth one has the appearance of a divine being.'",
      "T": "'But I see four men walking freely in the fire — unhurt! And the fourth one —' his appearance is unlike any human. The Aramaic says he looked like 'a son of the gods': Nebuchadnezzar's pagan idiom for a divine being. Christian readers across the centuries have seen the pre-incarnate Christ; the text invites but does not mandate that reading."
    },
    "26": {
      "L": "Then Nebuchadnezzar came near to the door of the burning fiery furnace and declared, 'Shadrach, Meshach, and Abednego, servants of the Most High God, come out! Come here!' Then Shadrach, Meshach, and Abednego came out from the midst of the fire.",
      "M": "Nebuchadnezzar came to the opening of the burning fiery furnace and called, 'Shadrach, Meshach, and Abednego, servants of the Most High God — come out! Come here!' And Shadrach, Meshach, and Abednego walked out of the fire.",
      "T": "The king went to the mouth of the furnace himself. 'Shadrach! Meshach! Abednego! Servants of the Most High God — come out!' And they walked out."
    },
    "27": {
      "L": "And the satraps, the prefects, and the governors and the king's counsellors gathered together and saw that the fire had not had power over the bodies of those men. The hair of their heads was not singed, their cloaks were not harmed, and no smell of fire had come upon them.",
      "M": "The satraps, prefects, governors, and royal counsellors all crowded around and saw that the fire had exercised no power over these men — not a hair of their heads was singed, their clothes were undamaged, and they did not even smell of smoke.",
      "T": "Every official pressed in to examine them. The fire had done absolutely nothing. Not a hair. Not a thread of their clothing. Not even the smell of smoke clung to them."
    },
    "28": {
      "L": "Nebuchadnezzar answered and said, 'Blessed be the God of Shadrach, Meshach, and Abednego, who has sent his angel and delivered his servants who trusted in him, and violated the king's command, and yielded up their bodies rather than serve and worship any god except their own God.'",
      "M": "Nebuchadnezzar declared, 'Blessed be the God of Shadrach, Meshach, and Abednego! He sent his angel and rescued his servants who trusted in him — who defied the royal edict and chose to give up their bodies rather than serve or worship any god but their own.'",
      "T": "'Blessed be the God of Shadrach, Meshach, and Abednego!' the king declared. 'He sent his messenger and delivered his servants who trusted him — men who defied a royal decree and surrendered their lives rather than worship anyone but their own God. They were right.'"
    },
    "29": {
      "L": "'Therefore I make a decree: any people, nation, or language that speaks anything offensive against the God of Shadrach, Meshach, and Abednego shall be torn limb from limb and their houses laid in ruins, because there is no other god who is able to deliver in this way.'",
      "M": "'Therefore I decree: any people, nation, or language that says anything against the God of Shadrach, Meshach, and Abednego is to be torn apart and their house reduced to ruins — for there is no other god who can rescue like this.'",
      "T": "Nebuchadnezzar issued an empire-wide decree: blasphemy against the God of these three was punishable by death and demolition. 'There is no other god,' he said, 'who can rescue like this.'"
    },
    "30": {
      "L": "Then the king promoted Shadrach, Meshach, and Abednego in the province of Babylon.",
      "M": "Then the king promoted Shadrach, Meshach, and Abednego to higher positions in the province of Babylon.",
      "T": "And Shadrach, Meshach, and Abednego were elevated to even higher office in the Babylonian provincial administration."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'daniel')
        merge_tier(existing, DANIEL, tier_key)
        save(tier_dir, 'daniel', existing)
    print('Daniel 1–3 written.')

if __name__ == '__main__':
    main()
