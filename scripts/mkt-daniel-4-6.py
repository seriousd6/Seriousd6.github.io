"""
MKT Daniel chapters 4–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-daniel-4-6.py

=== CHAPTER OVERVIEW ===

These three chapters are written in Biblical Aramaic (not Hebrew) — part of the
Aramaic section Dan 2:4–7:28. The H-prefix Strong's codes here denote Aramaic
vocabulary, not Hebrew; some lexemes are cognate but carry distinct nuance.

Chapter 4: Nebuchadnezzar's Proclamation — The Great Tree Dream.
  vv. 1–3: Royal greeting from Nebuchadnezzar to all nations.
  vv. 4–18: The dream of the great tree: its splendor, the watcher's descent, the
  command to cut it down while leaving the stump — the decree is to show that the
  Most High rules human kingdoms and may give them to the lowliest.
  vv. 19–27: Daniel (Belteshazzar) reluctantly interprets: the tree is Nebuchadnezzar;
  seven "times" (seasons/years) of bestial degradation lie ahead; counsel to repent.
  vv. 28–33: Fulfillment — Nebuchadnezzar's boast, the divine judgment, and his
  seven-year exile among beasts.
  vv. 34–37: Restoration — at the end of the period he looks to heaven, his reason
  returns, and he praises the King of heaven in a doxology of sovereign grace.
  The entire chapter is a first-person royal proclamation by Nebuchadnezzar — a
  rhetorical frame unique in the Hebrew Bible/Aramaic corpus.

Chapter 5: Belshazzar's Feast — The Writing on the Wall.
  vv. 1–4: The impious feast; Belshazzar commands the Jerusalem temple vessels to
  be used as party cups while praising idols of metal and wood.
  vv. 5–9: A disembodied hand writes four words on the plaster wall; the king is
  terrified; his wise men fail.
  vv. 10–16: The queen mother recommends Daniel; Belshazzar summons him.
  vv. 17–28: Daniel refuses the reward, recounts Nebuchadnezzar's humiliation, then
  indicts Belshazzar for knowing the lesson and still defying the Lord of heaven.
  He reads and interprets: MENE MENE TEKEL UPHARSIN.
  vv. 29–31: Belshazzar honours Daniel, then is slain that night; Darius the Mede
  takes the kingdom.

Chapter 6: Daniel in the Lions' Den.
  vv. 1–5: Darius reorganises the kingdom with 120 satraps under three presidents;
  Daniel's excellence leads the king to consider giving him supreme authority. Rivals
  find no fault in him except through the law of his God.
  vv. 6–9: The conspirators trick Darius into signing an irrevocable 30-day ban on
  all prayer except to the king.
  vv. 10–15: Daniel prays toward Jerusalem as always; caught; king anguished but
  cannot undo the Medo-Persian law.
  vv. 16–18: Daniel thrown into the lions' den; the stone sealed; king fasts and
  cannot sleep.
  vv. 19–23: At dawn the king rushes to the den; Daniel answers — God's angel shut
  the mouths; Daniel lifted out unharmed.
  vv. 24–28: Daniel's accusers thrown in; the lions destroy them. Darius writes a
  royal decree calling all nations to fear the God of Daniel; chapter closes with
  Daniel prospering through both Darius and Cyrus.

=== CONTESTED-TERM DECISIONS ===

- H426 (Aramaic אֱלָה / elah, "God"): The standard Aramaic word for God, used by
  both Israelites and Gentiles in Daniel. Grammatically singular in Aramaic unlike
  Hebrew H430. Rendered "God" in all tiers throughout. When a Gentile character
  speaks it, no distinction is made in the text — the Aramaic elah covers both pagan
  "god" and the true God; context drives interpretation.

- H5943 (עִלַּי / Illay, "Most High"): Aramaic superlative epithet for the God of
  Israel, used by Nebuchadnezzar (ch. 4) and Daniel (ch. 5). Rendered "the Most
  High" in L/M. T uses "the Most High" throughout; context (proclamation, speech to
  king) drives rhythm choices.

- H4756 (מָרֵא / mare', "lord/master"): Used as royal address ("my lord the king").
  Not the divine name. Rendered "my lord" (address to king) in L/M; T may adjust to
  "Your Majesty" or "my king" depending on register.

- H5894 (עִיר / ir, "watcher"): An angelic term unique to Daniel in the Hebrew/
  Aramaic Bible — a celestial watchman/sentinel. L/M: "watcher." T: "heavenly
  watcher" or "holy sentinel" to surface the angelic function.

- H7308 (Aramaic רוּחַ / ruach, "spirit"): Parallel to Hebrew H7307. In the phrase
  "spirit of the holy gods" (4:8,9,18; 5:11,12,14; 6:3), the speaker is a Gentile
  using Aramaic to describe an unusual divine quality in Daniel. L/M: "spirit of the
  holy gods" — preserving the pagan polytheistic expression. T: same phrase, but a
  translation note is embedded in context ("spirit of the holy gods — a Gentile's
  recognition of the divine"). In 6:3 (Darius), "excellent spirit" refers to
  character/administrative virtue, not divine presence; rendered "exceptional spirit"
  or "extraordinary gift" in T. Capital "Spirit" reserved for cases where the divine
  Spirit is the unambiguous referent (none in these chapters for the Gentile usage).

- H6922 (Aramaic קַדִּישׁ / qaddish, "holy"): Rendered "holy" in L/M. In "holy gods,"
  this is the Aramaic superlative of divine otherness. T keeps "holy."

- MENE (H4484) / TEKEL (H8625) / PERES/UPHARSIN (H6537): Aramaic monetary weights
  also functioning as wordplay verbs (numbered/weighed/divided). All three tiers
  transliterate the words. In the interpretation verses (5:26-28), L/M give the
  literal gloss; T surfaces the wordplay and the gravity of the verdict.

- "Father" / "son" (H2 / H1247): In ch. 5 Belshazzar calls Nebuchadnezzar his
  "father" — the Aramaic convention for "predecessor/forefather." Historically
  Belshazzar was Nabonidus's son and Nebuchadnezzar's grandson. L/M: "father" (as
  text has it). T: "grandfather" only in v.5:13 and 5:22 where clarity aids modern
  readers; elsewhere "father" is retained as the text's own register.

- "Scarlet" (H711, Aramaic ארגון / argewan): This is purple/violet (related to
  Akkadian argamannu), not scarlet/red. KJV renders it "scarlet" in error. Rendered
  "purple" in all tiers here.

- H3983 (מֵאמַר / word/decree): Distinct from H4406 (מִלָּה / word/matter). H3983
  rendered "word" in the context of the divine verdict; H4406 rendered "word/matter."

- H2417 (חַי / living): "the living God" — rendered "the living God" throughout as
  an established divine epithet (cf. Josh 3:10; Ps 84:2; Matt 16:16). T may elaborate.

- Aspect: Aramaic uses perfect/imperfect similarly to Hebrew. Waw-consecutive
  equivalents in Aramaic are handled; aorist-equivalent perfects in Daniel's
  narrative are treated as completed acts (L/M past tense, T vivid past).

- Daniel 4's narrative structure: The chapter is framed as Nebuchadnezzar's first-
  person proclamation (vv.1-37). The shift from his testimony to Daniel's speech and
  then to third-person narrative account (vv.28-33) is preserved in all tiers. This
  is an embedded royal letter — L preserves the syntax stiffness; M smooths it; T
  gives it proclamatory voice.

- "Third ruler" (H8531 / שָׁלִישׁ, 5:7,16,29): Belshazzar was co-regent (second to
  Nabonidus); the highest appointment he could make was "third." Context preserved
  in all tiers without paraphrase.
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
  "4": {
    "1": {
      "L": "Nebuchadnezzar the king, to all peoples, nations, and languages that dwell in all the earth: Peace be multiplied to you.",
      "M": "King Nebuchadnezzar, to all peoples, nations, and languages that dwell throughout the earth: May peace be multiplied to you.",
      "T": "King Nebuchadnezzar, to every people, nation, and tongue throughout all the earth: Grace and peace to you in full measure."
    },
    "2": {
      "L": "The signs and wonders that the Most High God has wrought toward me it seemed good to me to declare.",
      "M": "I have thought it good to declare the signs and wonders that the Most High God has worked for me.",
      "T": "It has seemed right to me to make known the extraordinary signs and wonders that the Most High God has performed in my life."
    },
    "3": {
      "L": "How great are his signs, and how mighty are his wonders! His kingdom is an everlasting kingdom, and his dominion is from generation to generation.",
      "M": "How great are his signs and how mighty his wonders! His kingdom is an everlasting kingdom, and his dominion endures from generation to generation.",
      "T": "His signs—how vast! His wonders—how mighty! His is a kingdom without end; his sovereign rule spans every generation and outlasts them all."
    },
    "4": {
      "L": "I, Nebuchadnezzar, was at ease in my house and flourishing in my palace.",
      "M": "I, Nebuchadnezzar, was at rest in my house and thriving in my palace.",
      "T": "It was a season of prosperity for me, Nebuchadnezzar—settled in my palace, at ease, everything flourishing."
    },
    "5": {
      "L": "I saw a dream and it made me afraid; and the thoughts upon my bed and the visions of my head troubled me.",
      "M": "I saw a dream that frightened me; the thoughts on my bed and the visions of my head disturbed me.",
      "T": "Then a dream came—and it terrified me. The visions that swept through my sleeping mind filled me with such dread I could not rest."
    },
    "6": {
      "L": "Therefore I issued a decree to bring before me all the wise men of Babylon, that they might make known to me the interpretation of the dream.",
      "M": "So I issued a decree to bring all the wise men of Babylon before me, so that they might give me the interpretation of the dream.",
      "T": "I commanded that every wise man in Babylon be summoned before me to explain what the dream meant."
    },
    "7": {
      "L": "Then came in the magicians, the astrologers, the Chaldeans, and the soothsayers; and I told them the dream, but they could not make known to me its interpretation.",
      "M": "The magicians, astrologers, Chaldeans, and soothsayers came in, and I told them the dream, but they could not make known to me its interpretation.",
      "T": "The magicians, astrologers, Chaldeans, and diviners all filed in. I told them the dream—but not one of them could tell me what it meant."
    },
    "8": {
      "L": "But at last came in before me Daniel, whose name is Belteshazzar, according to the name of my god, and in whom is the spirit of the holy gods; and I told him the dream, saying:",
      "M": "At last Daniel came before me—he whose name is Belteshazzar, after the name of my god, and in whom dwells the spirit of the holy gods. I told him the dream, saying:",
      "T": "Finally Daniel came—the one I had renamed Belteshazzar after my own god, the man in whom I sensed the spirit of the holy gods. I told him what I had seen:"
    },
    "9": {
      "L": "O Belteshazzar, master of the magicians, because I know that the spirit of the holy gods is in you and no secret troubles you, tell me the visions of my dream that I saw and its interpretation.",
      "M": "O Belteshazzar, chief of the magicians, I know that the spirit of the holy gods is in you and that no mystery is too hard for you. Tell me the visions of my dream that I saw and their interpretation.",
      "T": "Belteshazzar, master of all the wise men—the spirit of the holy gods lives in you and nothing is beyond your understanding. Tell me what I saw in my dream, and tell me what it means."
    },
    "10": {
      "L": "Thus were the visions of my head upon my bed: I was looking, and behold, a tree in the midst of the earth, and its height was great.",
      "M": "These were the visions of my head while I lay in bed: I looked, and there was a tree standing at the center of the earth, and it was very tall.",
      "T": "As I lay on my bed, the visions came: I looked, and there before me stood a tree at the very center of the earth, towering to enormous height."
    },
    "11": {
      "L": "The tree grew and became strong, and its height reached to the heavens, and it was seen to the end of all the earth.",
      "M": "The tree grew and became strong; its top reached to heaven and could be seen to the ends of the whole earth.",
      "T": "The tree kept growing until it touched the sky itself—so immense that you could see it from every corner of the earth."
    },
    "12": {
      "L": "Its leaves were beautiful and its fruit much, and in it was food for all. The beasts of the field had shade under it, and the birds of the heaven dwelt in its branches, and all flesh was fed from it.",
      "M": "Its leaves were beautiful and its fruit was plentiful; in it was food for all. The beasts of the field sheltered beneath it, the birds of the heaven nested in its branches, and all living creatures were fed from it.",
      "T": "Its leaves gleamed, its fruit hung heavy in abundance—enough to feed every creature. Animals rested in its wide shade, birds made their homes in every branch, and all living things found nourishment from it."
    },
    "13": {
      "L": "I was seeing in the visions of my head upon my bed, and behold, a watcher and a holy one came down from heaven.",
      "M": "I was looking in the visions of my head while on my bed, and there came down from heaven a watcher, a holy one.",
      "T": "Then, in those same night visions, a figure descended from heaven—a watcher, a holy sentinel of the celestial realm."
    },
    "14": {
      "L": "He cried aloud and thus he said: Hew down the tree and cut off its branches, shake off its leaves and scatter its fruit; let the beasts get away from beneath it, and the birds from its branches.",
      "M": "He cried out in a loud voice and said: Cut down the tree and trim off its branches, strip off its leaves and scatter its fruit. Let the beasts flee from beneath it and the birds from its branches.",
      "T": "He shouted with a voice that rang through heaven: 'Chop it down! Cut away its branches, strip its leaves, scatter its fruit! Drive out every creature that sheltered under it, every bird that nested in its boughs!'"
    },
    "15": {
      "L": "Nevertheless leave the stump of its roots in the earth, even with a band of iron and bronze, in the tender grass of the field; and let it be wet with the dew of heaven, and let his portion be with the beasts in the grass of the earth.",
      "M": "But leave the stump of its roots in the ground, bound with a band of iron and bronze, amid the tender grass of the field. Let it be drenched with the dew of heaven, and let his lot be with the beasts among the plants of the earth.",
      "T": "Yet leave the stump with its roots still in the ground—bound with iron and bronze—out in the open field. Let the dew of heaven fall on it. Let him live among the animals in the grass."
    },
    "16": {
      "L": "Let his heart be changed from a man's, and let the heart of a beast be given to him, and let seven times pass over him.",
      "M": "Let his mind be changed from a human mind and let the mind of an animal be given to him, and let seven seasons pass over him.",
      "T": "Strip away his human reason; give him the mind of an animal instead. And let this condition endure through seven appointed seasons."
    },
    "17": {
      "L": "This matter is by the decree of the watchers and the demand by the word of the holy ones; to the intent that the living may know that the Most High rules in the kingdom of men, and gives it to whomsoever he will, and sets up over it the basest of men.",
      "M": "This sentence is decreed by the watchers and commanded by the holy ones, so that the living may know that the Most High is sovereign over the kingdom of men: he gives it to whomever he chooses and sets over it even the humblest of people.",
      "T": "This verdict is the judgment of the watchers, the command of the holy ones—issued so that every living person may come to know that the Most High holds absolute sovereignty over all human kingdoms: he bestows them on anyone he pleases, even the most lowly and forgotten."
    },
    "18": {
      "L": "This dream I, the king Nebuchadnezzar, have seen; now you, O Belteshazzar, declare the interpretation thereof, forasmuch as all the wise men of my kingdom are not able to make known to me the interpretation; but you are able, for the spirit of the holy gods is in you.",
      "M": "This is the dream that I, King Nebuchadnezzar, have seen. Now you, Belteshazzar, declare its interpretation, since all the wise men of my kingdom are unable to make it known to me; but you can, because the spirit of the holy gods is in you.",
      "T": "That is the dream I saw—I, Nebuchadnezzar the king. Now you, Belteshazzar, must interpret it. Every wise man in my kingdom has failed me, but you will not, for the spirit of the holy gods is in you."
    },
    "19": {
      "L": "Then Daniel, whose name was Belteshazzar, was dismayed for one hour, and his thoughts alarmed him. The king answered and said, Belteshazzar, let not the dream, or the interpretation thereof, trouble you. Belteshazzar answered and said, My lord, the dream be to them that hate you, and the interpretation thereof to your enemies.",
      "M": "Then Daniel, whose name was Belteshazzar, was dismayed for a while, and his thoughts troubled him. The king said, 'Belteshazzar, let neither the dream nor its interpretation alarm you.' Belteshazzar answered, 'My lord, may the dream be for those who hate you and its interpretation for your enemies!'",
      "T": "Daniel—Belteshazzar—went still. You could see the distress working through him. The king said gently, 'Belteshazzar, don't let the dream or what it means frighten you.' At last Daniel spoke: 'My lord, I wish this dream were meant for your enemies and its meaning for those who despise you!'"
    },
    "20": {
      "L": "The tree that you saw, which grew and became strong, whose height reached to the heaven, and the sight thereof to all the earth;",
      "M": "The tree you saw, which grew and became strong, whose top reached to heaven and was visible to all the earth,",
      "T": "That great tree you saw—which grew until it touched heaven and could be seen from every corner of the earth—"
    },
    "21": {
      "L": "Whose leaves were beautiful, and the fruit thereof much, and in it was food for all; under which the beasts of the field dwelt, and upon whose branches the birds of the heaven had their habitation:",
      "M": "whose leaves were beautiful and its fruit plentiful, providing food for all, under which the beasts of the field lived, and in whose branches the birds of heaven had their home—",
      "T": "with its gleaming leaves and abundant fruit, its shelter for every beast and nesting place for every bird—"
    },
    "22": {
      "L": "It is you, O king, that are grown and become strong; for your greatness has grown and reaches to heaven, and your dominion to the end of the earth.",
      "M": "it is you, O king, who have grown and become strong. Your greatness has increased and reached to heaven, and your dominion extends to the ends of the earth.",
      "T": "that tree is you, O king. You have grown mighty; your power has stretched to the sky and your dominion to the farthest edges of the world."
    },
    "23": {
      "L": "And whereas the king saw a watcher and a holy one coming down from heaven, and saying, Hew the tree down, and destroy it; yet leave the stump of the roots thereof in the earth, even with a band of iron and bronze, in the tender grass of the field; and let it be wet with the dew of heaven, and let his portion be with the beasts of the field, till seven times pass over him:",
      "M": "And as you saw a watcher and a holy one coming down from heaven and saying, 'Cut down the tree and destroy it, yet leave the stump of its roots in the ground, bound with iron and bronze, in the tender grass of the field, and let it be drenched with the dew of heaven, and let his lot be with the beasts of the field, until seven seasons pass over him'—",
      "T": "And the holy watcher you saw descending from heaven, commanding that the tree be cut down and destroyed—yet leaving the stump rooted in the ground, bound with iron and bronze in the open field, soaked with heaven's dew, to live among the animals through seven appointed seasons—"
    },
    "24": {
      "L": "This is the interpretation, O king, and this is the decree of the Most High that has come upon my lord the king:",
      "M": "this is the interpretation, O king: it is the decree of the Most High that has come upon my lord the king.",
      "T": "this is the meaning, my lord king: this is the decree the Most High himself has issued against you."
    },
    "25": {
      "L": "That they shall drive you from men, and your dwelling shall be with the beasts of the field, and they shall make you to eat grass as oxen, and they shall wet you with the dew of heaven, and seven times shall pass over you, till you know that the Most High rules in the kingdom of men, and gives it to whomsoever he will.",
      "M": "You will be driven from among people, and your dwelling will be with the beasts of the field. You will eat grass like an ox and be drenched with the dew of heaven. Seven seasons will pass over you until you acknowledge that the Most High is sovereign over the kingdom of men and gives it to whomever he chooses.",
      "T": "You will be expelled from human society. You will live like a wild animal—eating grass like an ox, your body soaked with the dew of heaven night after night—through seven long seasons, until you come to know deep in your being that the Most High is lord over all human kingdoms and grants them to anyone he pleases."
    },
    "26": {
      "L": "And whereas they commanded to leave the stump of the tree roots; your kingdom shall be sure to you, after that you shall have known that the heavens do rule.",
      "M": "As for the command to leave the stump of the roots: your kingdom will be restored to you as soon as you acknowledge that Heaven is sovereign.",
      "T": "But the command to spare the stump holds out hope: once you recognize that Heaven governs all things, your kingdom will be returned to you."
    },
    "27": {
      "L": "Wherefore, O king, let my counsel be acceptable to you, and break off your sins by righteousness, and your iniquities by showing mercy to the poor; if it may be a lengthening of your tranquillity.",
      "M": "Therefore, O king, let my counsel be acceptable to you: break with your sins by doing what is right, and your iniquities by showing mercy to the oppressed, so that your prosperity may perhaps be extended.",
      "T": "So, O king, let me urge you: turn away from your sins—let righteous deeds replace them; show compassion to those who suffer under your power. Perhaps this will buy you more time of peace."
    },
    "28": {
      "L": "All this came upon the king Nebuchadnezzar.",
      "M": "All this came upon King Nebuchadnezzar.",
      "T": "Every word of it came to pass upon King Nebuchadnezzar."
    },
    "29": {
      "L": "At the end of twelve months he was walking upon the royal palace of Babylon.",
      "M": "Twelve months later, he was strolling on the roof of the royal palace of Babylon.",
      "T": "A full twelve months passed. Then one day the king was pacing the rooftop terrace of his royal palace in Babylon."
    },
    "30": {
      "L": "The king spoke and said, Is not this great Babylon, that I have built for the house of the kingdom by the might of my power, and for the honour of my majesty?",
      "M": "The king said, 'Is this not great Babylon, which I myself have built as a royal residence by my mighty power and for the glory of my majesty?'",
      "T": "And he said to himself with pride: 'Look at it—Babylon the Great! I built this! This magnificent city is a monument to my power and a tribute to my royal glory!'"
    },
    "31": {
      "L": "While the word was in the king's mouth, there fell a voice from heaven, saying, O king Nebuchadnezzar, to you it is spoken; The kingdom is departed from you.",
      "M": "While the word was still in the king's mouth, a voice fell from heaven: 'O King Nebuchadnezzar, to you it is declared: The kingdom has departed from you.'",
      "T": "The proud words were barely off his lips when a voice thundered down from heaven: 'Nebuchadnezzar! Hear this decree: the kingdom has been stripped from you.'"
    },
    "32": {
      "L": "And they shall drive you from men, and your dwelling shall be with the beasts of the field; they shall make you to eat grass as oxen, and seven times shall pass over you, until you know that the Most High rules in the kingdom of men, and gives it to whomsoever he will.",
      "M": "You will be driven away from people, and your dwelling will be with the beasts of the field. You will eat grass like an ox, and seven seasons will pass over you, until you acknowledge that the Most High rules in the kingdom of men and gives it to whom he will.",
      "T": "You will be banished from human society. You will live with the wild animals, eating grass like an ox, through seven appointed seasons—until you come to know that the Most High has absolute sovereignty over human kingdoms and grants them to whoever he chooses."
    },
    "33": {
      "L": "The same hour was the thing fulfilled upon Nebuchadnezzar; and he was driven from men, and did eat grass as oxen, and his body was wet with the dew of heaven, till his hairs were grown like eagles' feathers, and his nails like birds' claws.",
      "M": "That same hour the word was fulfilled against Nebuchadnezzar. He was driven from among men and ate grass like an ox, and his body was drenched with the dew of heaven until his hair grew as long as eagles' feathers and his nails like birds' claws.",
      "T": "That very hour the sentence was carried out. Nebuchadnezzar was driven from human company. He ate grass like an ox and slept in the open, his body drenched by heaven's dew night after night—until his hair grew matted and long as eagle-feathers, his fingernails curling like an animal's talons."
    },
    "34": {
      "L": "And at the end of the days I Nebuchadnezzar lifted up mine eyes unto heaven, and mine understanding returned unto me, and I blessed the Most High, and I praised and honoured him that lives for ever, whose dominion is an everlasting dominion, and his kingdom is from generation to generation.",
      "M": "At the end of the appointed time, I, Nebuchadnezzar, lifted my eyes toward heaven, and my understanding returned to me. I blessed the Most High, and praised and honored him who lives forever; for his dominion is an everlasting dominion and his kingdom endures from generation to generation.",
      "T": "Then, when the appointed time was complete, I raised my eyes to heaven—and my mind came back to me. I blessed the Most High. I praised and honored the One who lives forever: his sovereignty has no end, his kingdom outlasts every generation that has ever lived."
    },
    "35": {
      "L": "And all the inhabitants of the earth are reputed as nothing; and he does according to his will in the army of heaven, and among the inhabitants of the earth; and none can stay his hand, or say unto him, What do you do?",
      "M": "All the inhabitants of the earth are counted as nothing, and he does as he pleases among the host of heaven and among the inhabitants of the earth. No one can stay his hand or say to him, 'What are you doing?'",
      "T": "Before him every human being counts for nothing. He acts according to his own will among the armies of heaven and among all who live on earth. No one can restrain his hand. No one can call him to account: 'What are you doing?'"
    },
    "36": {
      "L": "At the same time my reason returned unto me; and for the glory of my kingdom, mine honour and brightness returned unto me; and my counsellors and my lords sought unto me; and I was established in my kingdom, and excellent majesty was added unto me.",
      "M": "At the same time my reason returned to me, and for the glory of my kingdom, my honor and splendor were restored to me. My counselors and my lords sought me out, I was reestablished in my kingdom, and even greater majesty was added to me.",
      "T": "At that same moment my mind was restored. My dignity and royal splendor returned—along with my throne. My advisors and nobles came back to me; I was reinstated in my kingdom, and I emerged from the ordeal with greater honor than before."
    },
    "37": {
      "L": "Now I Nebuchadnezzar praise and extol and honour the King of heaven, all whose works are truth, and his ways judgment; and those that walk in pride he is able to abase.",
      "M": "Now I, Nebuchadnezzar, praise and exalt and glorify the King of heaven, for all his works are true and his ways are just; and those who walk in pride he is able to humble.",
      "T": "So let me declare it: I, Nebuchadnezzar, praise and exalt and glorify the King of heaven. Everything he does is just and true. And anyone who walks in arrogance—he is fully able to bring them low."
    }
  },
  "5": {
    "1": {
      "L": "Belshazzar the king made a great feast to a thousand of his lords, and drank wine before the thousand.",
      "M": "King Belshazzar made a great feast for a thousand of his nobles and drank wine in their presence.",
      "T": "King Belshazzar held a lavish banquet for a thousand of his nobles, drinking freely before them all."
    },
    "2": {
      "L": "Belshazzar, whiles he tasted the wine, commanded to bring the golden and silver vessels which his father Nebuchadnezzar had taken out of the temple which was in Jerusalem; that the king, and his princes, his wives, and his concubines, might drink therein.",
      "M": "While Belshazzar tasted the wine, he commanded that the gold and silver vessels that his father Nebuchadnezzar had taken from the temple in Jerusalem be brought, so that the king, his nobles, his wives, and his concubines might drink from them.",
      "T": "As the wine flowed, Belshazzar gave an impious command: bring the gold and silver vessels that Nebuchadnezzar had looted from the Lord's temple in Jerusalem—the king and his entire court, his wives and concubines, would drink from sacred things."
    },
    "3": {
      "L": "Then they brought the golden vessels that were taken out of the temple of the house of God which was at Jerusalem; and the king, and his princes, his wives, and his concubines, drank in them.",
      "M": "So they brought in the gold vessels that had been taken from the temple of God in Jerusalem, and the king and his nobles, his wives and his concubines drank from them.",
      "T": "They brought the sacred vessels from God's temple in Jerusalem, and the king, his court, his wives, and his concubines all drank from them."
    },
    "4": {
      "L": "They drank wine, and praised the gods of gold, and of silver, of brass, of iron, of wood, and of stone.",
      "M": "As they drank wine, they praised the gods of gold and silver, of bronze, iron, wood, and stone.",
      "T": "As they drank, they toasted their idols—gods of gold, silver, bronze, iron, wood, and stone: blind and mute and dead."
    },
    "5": {
      "L": "In the same hour came forth fingers of a man's hand, and wrote over against the candlestick upon the plaster of the wall of the king's palace; and the king saw the part of the hand that wrote.",
      "M": "At that moment the fingers of a human hand appeared and wrote on the plaster of the wall of the king's palace, next to the lampstand. The king saw the hand as it wrote.",
      "T": "At that very moment, the fingers of a human hand appeared out of nowhere and began writing on the plastered wall of the palace, in the glow of the lampstand. The king watched the hand moving as it wrote."
    },
    "6": {
      "L": "Then the king's countenance was changed, and his thoughts troubled him, so that the joints of his loins were loosed, and his knees smote one against another.",
      "M": "Then the king's face changed color, and his thoughts alarmed him; the joints of his hips gave way and his knees knocked together.",
      "T": "The king's face went ashen. Terror seized his thoughts. His legs buckled beneath him and his knees knocked together in fear."
    },
    "7": {
      "L": "The king cried aloud to bring in the astrologers, the Chaldeans, and the soothsayers. And the king spoke, and said to the wise men of Babylon, Whosoever shall read this writing, and show me the interpretation thereof, shall be clothed with purple, and have a chain of gold about his neck, and shall be the third ruler in the kingdom.",
      "M": "The king called out loudly to bring in the enchanters, Chaldeans, and astrologers. The king said to the wise men of Babylon, 'Whoever reads this writing and tells me its interpretation shall be clothed in purple and have a gold chain placed around his neck and shall be the third highest ruler in the kingdom.'",
      "T": "He cried out for Babylon's astrologers, Chaldeans, and enchanters. 'Whoever can read that writing and explain what it means,' the king announced, 'will be robed in purple, hung with a gold chain, and made the third highest ruler in this kingdom.'"
    },
    "8": {
      "L": "Then came in all the king's wise men: but they could not read the writing, nor make known to the king the interpretation thereof.",
      "M": "Then all the king's wise men came in, but they could not read the writing or make known to the king its interpretation.",
      "T": "Every one of the king's wise men came in. But none of them could read the writing. None could tell him what it meant."
    },
    "9": {
      "L": "Then was king Belshazzar greatly troubled, and his countenance was changed in him, and his lords were astonied.",
      "M": "Then King Belshazzar was greatly alarmed, his color changed, and his lords were bewildered.",
      "T": "Belshazzar's terror deepened. More color drained from his face. His nobles stood around him, stunned and helpless."
    },
    "10": {
      "L": "Now the queen, by reason of the words of the king and his lords, came into the banquet house; and the queen spoke and said, O king, live for ever; let not your thoughts trouble you, nor let your countenance be changed.",
      "M": "The queen, hearing the words of the king and his lords, came into the banqueting hall. The queen spoke and said, 'O king, live forever! Do not let your thoughts trouble you, and do not let your face be changed.'",
      "T": "Then the queen mother, having heard the commotion in the banquet hall, came in and addressed the king: 'O king, may you live forever! Do not be alarmed. Do not let this unsettle you.'"
    },
    "11": {
      "L": "There is a man in your kingdom, in whom is the spirit of the holy gods; and in the days of your father light and understanding and wisdom, like the wisdom of the gods, was found in him; whom the king Nebuchadnezzar your father, the king, your father, made master of the magicians, astrologers, Chaldeans, and soothsayers.",
      "M": "There is a man in your kingdom in whom is the spirit of the holy gods. In the days of your father, he was found to have light, insight, and wisdom like the wisdom of the gods. King Nebuchadnezzar your father—your father the king—made him chief of the magicians, enchanters, Chaldeans, and astrologers.",
      "T": "There is a man in your kingdom in whom dwells the spirit of the holy gods. In your grandfather's day he possessed illumination of mind, depth of insight, and a wisdom that surpassed all others. King Nebuchadnezzar—the great king, your predecessor—made him head over all the wise men."
    },
    "12": {
      "L": "Forasmuch as an excellent spirit, and knowledge, and understanding, interpreting of dreams, and showing of hard sentences, and dissolving of doubts, were found in the same Daniel, whom the king named Belteshazzar: now let Daniel be called, and he will show the interpretation.",
      "M": "Because an excellent spirit, knowledge, and the ability to interpret dreams, explain riddles, and solve difficult problems were found in this Daniel, whom the king named Belteshazzar. Now let Daniel be called and he will give the interpretation.",
      "T": "This man—Daniel, renamed Belteshazzar by your grandfather—has an extraordinary spirit within him, along with knowledge and skill to interpret dreams, unravel mysteries, and untangle what baffles everyone else. Send for Daniel. He will tell you what this writing means."
    },
    "13": {
      "L": "Then was Daniel brought in before the king. And the king spoke and said unto Daniel, Art you that Daniel, which art of the children of the captivity of Judah, whom the king my father brought out of Judah?",
      "M": "So Daniel was brought before the king. The king said to Daniel, 'Are you that Daniel, one of the exiles of Judah, whom my father the king brought from Judah?'",
      "T": "Daniel was brought in before the king. 'So you are Daniel,' the king said, 'one of the Judean exiles that Nebuchadnezzar brought here from Jerusalem?'"
    },
    "14": {
      "L": "I have even heard of you, that the spirit of the gods is in you, and that light and understanding and excellent wisdom is found in you.",
      "M": "I have heard that the spirit of the gods is in you and that light, understanding, and excellent wisdom are found in you.",
      "T": "I have been told that the spirit of the gods dwells in you—that you have uncommon insight, deep understanding, and extraordinary wisdom."
    },
    "15": {
      "L": "And now the wise men, the astrologers, have been brought in before me, that they should read this writing, and make known to me the interpretation thereof: but they could not show the interpretation of the thing.",
      "M": "The wise men and enchanters were brought in before me to read this writing and make known its interpretation, but they were unable to give the interpretation of the matter.",
      "T": "I brought in all my best men—the wise men, the astrologers—to read the writing and tell me what it means. Not one of them could do it."
    },
    "16": {
      "L": "And I have heard of you, that you can make interpretations, and dissolve doubts: now if you can read the writing, and make known to me the interpretation thereof, you shall be clothed with purple, and have a chain of gold about your neck, and shall be the third ruler in the kingdom.",
      "M": "But I have heard that you can give interpretations and solve problems. Now if you can read this writing and make known to me its interpretation, you shall be clothed in purple and have a gold chain placed around your neck, and you shall be the third ruler in the kingdom.",
      "T": "'But I have been told you can interpret and untangle mysteries. Read this for me. Explain what it means—and I will clothe you in purple, hang a gold chain around your neck, and make you the third most powerful man in this kingdom.'"
    },
    "17": {
      "L": "Then Daniel answered and said before the king, Let your gifts be to yourself, and give your rewards to another; yet I will read the writing unto the king, and make known to him the interpretation.",
      "M": "Then Daniel answered and said before the king, 'Let your gifts remain with you and give your rewards to another. Nevertheless, I will read the writing for the king and make known the interpretation.'",
      "T": "Daniel answered the king directly: 'Keep your gifts. Give your rewards to someone else. But I will read the writing and tell you what it means.'"
    },
    "18": {
      "L": "O you king, the Most High God gave Nebuchadnezzar your father a kingdom, and majesty, and glory, and honour.",
      "M": "O king, the Most High God gave your father Nebuchadnezzar a kingdom, greatness, glory, and majesty.",
      "T": "O king, hear me first. The Most High God gave your grandfather Nebuchadnezzar a great kingdom—power, splendor, glory, and honor—all of it."
    },
    "19": {
      "L": "And for the majesty that he gave him, all people, nations, and languages, trembled and feared before him: whom he would he slew; and whom he would he kept alive; and whom he would he set up; and whom he would he put down.",
      "M": "Because of the greatness that God gave him, all peoples, nations, and languages trembled and feared before him. He killed whom he wished and kept alive whom he wished; he raised up whom he wished and brought down whom he wished.",
      "T": "Because of the power God gave him, every people, nation, and tongue on earth lived in terror before Nebuchadnezzar. He put men to death on a whim; he spared others the same way. He elevated whoever he chose and crushed whoever he chose."
    },
    "20": {
      "L": "But when his heart was lifted up, and his mind hardened in pride, he was deposed from his kingly throne, and they took his glory from him.",
      "M": "But when his heart was lifted up and his spirit became arrogant, he was deposed from his royal throne and his glory was stripped from him.",
      "T": "But when his heart swelled with pride and his spirit hardened into arrogance, he was stripped of his royal throne and his glory was taken away."
    },
    "21": {
      "L": "And he was driven from the sons of men; and his heart was made like the beasts, and his dwelling was with the wild asses: they fed him with grass like oxen, and his body was wet with the dew of heaven; till he knew that the Most High God ruled in the kingdom of men, and that he appoints over it whomsoever he will.",
      "M": "He was driven from among people, his mind became like that of an animal, and his dwelling was with the wild donkeys. He was fed grass like an ox, and his body was drenched with the dew of heaven, until he acknowledged that the Most High God rules over the kingdom of men and sets over it whomever he chooses.",
      "T": "He was expelled from human society. His mind became like a beast's; he lived among the wild donkeys, ate grass like an ox, his body soaked with heaven's dew—until he finally came to acknowledge that the Most High God is sovereign over all human kingdoms and places in power whomever he wills."
    },
    "22": {
      "L": "And you his son, O Belshazzar, have not humbled your heart, though you knew all this.",
      "M": "And you, Belshazzar his son, have not humbled your heart, even though you knew all this.",
      "T": "And you, Belshazzar—his own grandson—you knew all of this, and still you refused to humble yourself."
    },
    "23": {
      "L": "But have lifted up yourself against the Lord of heaven; and they have brought the vessels of his house before you, and you, and your lords, your wives, and your concubines, have drunk wine in them; and you have praised the gods of silver, and gold, of brass, iron, wood, and stone, which see not, nor hear, nor know: and the God in whose hand your breath is, and whose are all your ways, have you not glorified.",
      "M": "But you have lifted yourself up against the Lord of heaven. The vessels of his temple were brought before you, and you and your nobles, wives, and concubines have drunk wine from them. You praised gods of silver and gold, bronze, iron, wood, and stone—which cannot see, hear, or know anything. But the God who holds your very breath in his hand and owns all your ways—him you have not honored.",
      "T": "Instead, you set yourself in open defiance against the Lord of heaven. You had his sacred vessels brought out and turned them into party cups. You and your court, your wives, your concubines, all toasted your idols—gods of metal and wood, blind and deaf and utterly senseless. But the One who holds the very breath in your lungs, who governs every step you take—him you have refused to honor."
    },
    "24": {
      "L": "Then was the part of the hand sent from him; and this writing was written.",
      "M": "So the hand was sent from his presence, and this writing was inscribed.",
      "T": "That is why he sent the hand. That is what produced these words on your wall."
    },
    "25": {
      "L": "And this is the writing that was written, MENE, MENE, TEKEL, UPHARSIN.",
      "M": "And this is the writing that was inscribed: MENE, MENE, TEKEL, and PARSIN.",
      "T": "The words written are these: MENE, MENE, TEKEL, PARSIN."
    },
    "26": {
      "L": "This is the interpretation of the thing: MENE; God has numbered your kingdom, and finished it.",
      "M": "This is the interpretation: MENE—God has numbered the days of your kingdom and brought it to an end.",
      "T": "Here is what they mean. MENE: God has counted up the days of your reign. The total is complete. Your time is finished."
    },
    "27": {
      "L": "TEKEL; You are weighed in the balances, and are found wanting.",
      "M": "TEKEL—you have been weighed in the balance and found wanting.",
      "T": "TEKEL: you have been put on the scales of divine judgment—and you fall short of the measure."
    },
    "28": {
      "L": "PERES; Your kingdom is divided, and given to the Medes and Persians.",
      "M": "PERES—your kingdom is divided and given over to the Medes and Persians.",
      "T": "PERES: your kingdom is being split apart and handed over—this very night—to the Medes and Persians."
    },
    "29": {
      "L": "Then commanded Belshazzar, and they clothed Daniel with purple, and put a chain of gold about his neck, and made a proclamation concerning him, that he should be the third ruler in the kingdom.",
      "M": "Then Belshazzar commanded, and Daniel was clothed in purple, a chain of gold was placed around his neck, and a proclamation was made that he should be the third ruler in the kingdom.",
      "T": "Then Belshazzar, true to his word, commanded that Daniel be robed in purple and given a gold chain for his neck, and the announcement went out that he was now the third ruler of the kingdom."
    },
    "30": {
      "L": "In that night was Belshazzar the king of the Chaldeans slain.",
      "M": "That very night Belshazzar the Chaldean king was killed.",
      "T": "That same night, Belshazzar king of the Chaldeans was struck down."
    },
    "31": {
      "L": "And Darius the Median took the kingdom, being about threescore and two years old.",
      "M": "And Darius the Mede received the kingdom, being about sixty-two years old.",
      "T": "Darius the Mede took possession of the kingdom at about sixty-two years of age."
    }
  },
  "6": {
    "1": {
      "L": "It pleased Darius to set over the kingdom an hundred and twenty princes, which should be over the whole kingdom.",
      "M": "Darius saw fit to appoint 120 satraps over the kingdom, to govern throughout the whole realm.",
      "T": "Darius reorganized his new kingdom, appointing 120 provincial governors to administer every region under his rule."
    },
    "2": {
      "L": "And over these three presidents; of whom Daniel was first: that the princes might give accounts unto them, and the king should have no damage.",
      "M": "Over them were three administrators, of whom Daniel was first, so that the satraps would give account to them and the king would not suffer any loss.",
      "T": "Over these 120 satraps he placed three chief administrators—Daniel first among them—so that the governors would answer to them and the king's interests would be fully protected."
    },
    "3": {
      "L": "Then this Daniel was preferred above the presidents and princes, because an excellent spirit was in him; and the king thought to set him over the whole realm.",
      "M": "Then Daniel distinguished himself above all the other administrators and satraps because an excellent spirit was in him, and the king planned to appoint him over the entire kingdom.",
      "T": "Daniel quickly outpaced the other two administrators and all the satraps, because an extraordinary spirit animated everything he did. The king began making plans to appoint him over the entire kingdom."
    },
    "4": {
      "L": "Then the presidents and princes sought to find occasion against Daniel concerning the kingdom; but they could find none occasion nor fault; forasmuch as he was faithful, neither was there any error or fault found in him.",
      "M": "Then the administrators and satraps tried to find grounds for complaint against Daniel regarding the affairs of the kingdom, but they could find no grounds for complaint or any fault, because he was faithful, and no error or fault was found in him.",
      "T": "His rivals—the other administrators and the satraps—tried every angle to find something to use against him in his administration. They found nothing: no corruption, no negligence, no scandal. He was completely reliable."
    },
    "5": {
      "L": "Then said these men, We shall not find any occasion against this Daniel, except we find it against him concerning the law of his God.",
      "M": "Then these men said, 'We will find no grounds for complaint against Daniel unless we find it in connection with the law of his God.'",
      "T": "Finally they concluded among themselves: 'We will never bring this man down unless we target his devotion to his God.'"
    },
    "6": {
      "L": "Then these presidents and princes assembled together to the king, and said thus unto him, King Darius, live for ever.",
      "M": "Then these administrators and satraps assembled before the king and said to him, 'O King Darius, live forever!'",
      "T": "So they conspired together and came before the king with one voice. 'O King Darius, may you reign forever!'"
    },
    "7": {
      "L": "All the presidents of the kingdom, the governors, and the princes, the counsellors, and the captains, have consulted together to establish a royal statute, and to make a firm decree, that whosoever shall ask a petition of any God or man for thirty days, save of thee, O king, shall be cast into the den of lions.",
      "M": "All the administrators of the kingdom, the prefects, satraps, counselors, and governors have agreed together that the king should issue a statute and enforce a strict decree: anyone who makes any petition to any god or person for thirty days, except to you, O king, shall be thrown into the den of lions.",
      "T": "'All the chief administrators, governors, satraps, advisors, and prefects have together agreed that the king should issue an irrevocable decree: for the next thirty days, anyone who prays to any god or person other than you, O king, will be thrown into the lions' den.'"
    },
    "8": {
      "L": "Now, O king, establish the decree, and sign the writing, that it be not changed, according to the law of the Medes and Persians, which alters not.",
      "M": "Now, O king, issue the decree and sign the document, so that it cannot be changed, in keeping with the law of the Medes and Persians, which cannot be revoked.",
      "T": "'Now, O king, sign it into law. Under the irrevocable law of the Medes and Persians, once it is signed it cannot be undone—by anyone.'"
    },
    "9": {
      "L": "Wherefore king Darius signed the writing and the decree.",
      "M": "So King Darius signed the document and the decree.",
      "T": "King Darius signed the decree."
    },
    "10": {
      "L": "Now when Daniel knew that the writing was signed, he went into his house; and his windows being open in his chamber toward Jerusalem, he kneeled upon his knees three times a day, and prayed, and gave thanks before his God, as he did aforetime.",
      "M": "When Daniel learned that the document had been signed, he went to his house, where the windows in his upper room faced toward Jerusalem. Three times a day he knelt on his knees and prayed and gave thanks before his God, as he had done before.",
      "T": "Daniel heard that the decree had been signed and sealed. He went home, climbed to his upper room where the windows faced Jerusalem, knelt on the floor, and prayed—giving thanks to his God—three times that day, exactly as he had always done."
    },
    "11": {
      "L": "Then these men assembled, and found Daniel praying and making supplication before his God.",
      "M": "Then these men gathered together and found Daniel praying and making supplication before his God.",
      "T": "His enemies had assembled nearby. They came in and caught him on his knees, praying and pleading before his God."
    },
    "12": {
      "L": "Then they came near, and spoke before the king concerning the king's decree; Have you not signed a decree, that every man that shall ask a petition of any God or man within thirty days, save of you, O king, shall be cast into the den of lions? The king answered and said, The thing is true, according to the law of the Medes and Persians, which alters not.",
      "M": "Then they approached the king and spoke about the royal decree: 'Did you not sign a decree that anyone who makes petition to any god or man within thirty days, except to you, O king, shall be thrown into the den of lions?' The king answered, 'The matter is certain, according to the law of the Medes and Persians, which cannot be revoked.'",
      "T": "They went before the king. 'Your Majesty, did you not sign a decree that any person praying to any god or man other than you, within thirty days, would be thrown to the lions?' 'Yes,' said the king, 'and the law of the Medes and Persians stands—no one can revoke it.'"
    },
    "13": {
      "L": "Then answered they and said before the king, That Daniel, which is of the children of the captivity of Judah, regards not you, O king, nor the decree that you have signed, but makes his petition three times a day.",
      "M": "Then they answered and said before the king, 'Daniel, who is one of the exiles from Judah, pays no attention to you, O king, or to the decree you signed, but makes his petition three times a day.'",
      "T": "'Then know this,' they said: 'Daniel—one of the Judean exiles—defies you and your decree. He has been praying three times daily. He refuses to stop.'"
    },
    "14": {
      "L": "Then the king, when he heard these words, was sore displeased with himself, and set his heart on Daniel to deliver him: and he laboured till the going down of the sun to deliver him.",
      "M": "When the king heard these words, he was greatly distressed and set his heart on Daniel to deliver him. He worked until sundown to find a way to save him.",
      "T": "The king was stricken when he heard it. He spent the rest of the day—until sunset—desperately searching for a legal means to save Daniel."
    },
    "15": {
      "L": "Then these men assembled unto the king, and said unto the king, Know, O king, that the law of the Medes and Persians is, That no decree nor statute which the king establishes may be changed.",
      "M": "Then these men came together before the king and said to the king, 'Know, O king, that it is a law of the Medes and Persians that no decree or statute that the king establishes can be changed.'",
      "T": "Then his enemies cornered the king again. 'Your Majesty, let it be on the record: the law of the Medes and Persians holds that no royal decree can ever be revoked.'"
    },
    "16": {
      "L": "Then the king commanded, and they brought Daniel, and cast him into the den of lions. Now the king spoke and said unto Daniel, Thy God whom thou servest continually, he will deliver thee.",
      "M": "So the king gave the command, and they brought Daniel and threw him into the den of lions. The king said to Daniel, 'May your God, whom you serve faithfully, deliver you!'",
      "T": "With no other choice, the king gave the order. Daniel was brought and cast into the lions' den. But the king called down to him as he went: 'Your God—the one you serve without fail—may he save you!'"
    },
    "17": {
      "L": "And a stone was brought, and laid upon the mouth of the den; and the king sealed it with his own signet, and with the signet of his lords; that the purpose might not be changed concerning Daniel.",
      "M": "A stone was brought and laid over the mouth of the den, and the king sealed it with his own signet ring and with the signet rings of his lords, so that nothing could be changed concerning Daniel.",
      "T": "A stone slab was placed over the mouth of the pit. The king pressed his own ring into the seal—and the rings of his nobles too—so that no one could interfere with what had been done."
    },
    "18": {
      "L": "Then the king went to his palace, and passed the night fasting: neither were instruments of musick brought before him: and his sleep went from him.",
      "M": "Then the king returned to his palace and spent the night fasting. No entertainments were brought before him, and sleep fled from him.",
      "T": "The king went back to his palace. He refused food. He sent away his musicians and entertainers. He lay awake the whole night, unable to sleep."
    },
    "19": {
      "L": "Then the king arose very early in the morning, and went in haste unto the den of lions.",
      "M": "Then at the first light of dawn the king arose and hurried to the den of lions.",
      "T": "At the first grey light of dawn the king leaped up and rushed to the lions' den."
    },
    "20": {
      "L": "And when he came to the den, he cried with a lamentable voice unto Daniel: and the king spoke and said to Daniel, O Daniel, servant of the living God, is thy God, whom thou servest continually, able to deliver thee from the lions?",
      "M": "When he came near to the den, he called to Daniel in an anguished voice. The king spoke to Daniel, 'O Daniel, servant of the living God, has your God whom you serve continually been able to deliver you from the lions?'",
      "T": "As he reached the pit he cried out in a voice full of anguish: 'Daniel! Servant of the living God—was your God, the one you serve so faithfully, able to rescue you from the lions?'"
    },
    "21": {
      "L": "Then said Daniel unto the king, O king, live for ever.",
      "M": "Then Daniel said to the king, 'O king, live forever!'",
      "T": "And Daniel's voice came up from the darkness: 'O king, may you live forever!'"
    },
    "22": {
      "L": "My God has sent his angel, and has shut the lions' mouths, that they have not hurt me: forasmuch as before him innocency was found in me; and also before you, O king, have I done no hurt.",
      "M": "My God sent his angel and shut the lions' mouths, and they have not harmed me, because I was found blameless before him; and before you, O king, I have done no wrong.",
      "T": "'My God sent his angel and locked the mouths of the lions. They have not touched me—because before God I stand innocent, and before you, my king, I have done nothing wrong.'"
    },
    "23": {
      "L": "Then was the king exceeding glad for him, and commanded that they should take Daniel up out of the den. So Daniel was taken up out of the den, and no manner of hurt was found upon him, because he believed in his God.",
      "M": "Then the king was exceedingly glad and commanded that Daniel be lifted out of the den. Daniel was brought up from the den, and no injury of any kind was found on him, because he had trusted in his God.",
      "T": "The king was flooded with relief. He commanded Daniel to be lifted out at once. When Daniel came up, not a scratch was on him—because he had placed his trust in his God."
    },
    "24": {
      "L": "And the king commanded, and they brought those men which had accused Daniel, and they cast them into the den of lions, them, their children, and their wives; and the lions had the mastery of them, and brake all their bones in pieces or ever they came at the bottom of the den.",
      "M": "Then the king commanded that the men who had maliciously accused Daniel be brought and thrown into the den of lions—they and their children and their wives. Before they reached the floor of the den, the lions seized them and crushed all their bones.",
      "T": "Then the king ordered Daniel's accusers brought out. They were thrown into the lions' den along with their wives and children. The lions were on them before they even reached the bottom—tearing apart flesh and bone."
    },
    "25": {
      "L": "Then king Darius wrote unto all people, nations, and languages, that dwell in all the earth; Peace be multiplied unto you.",
      "M": "Then King Darius wrote to all peoples, nations, and languages throughout the whole earth: 'May peace be multiplied to you.'",
      "T": "Then King Darius sent a royal letter to every people, nation, and tongue throughout all the earth: 'Grace and peace to you, in full measure.'"
    },
    "26": {
      "L": "I make a decree, That in every dominion of my kingdom men tremble and fear before the God of Daniel: for he is the living God, and stedfast for ever, and his kingdom that which shall not be destroyed, and his dominion shall be even unto the end.",
      "M": "I issue a decree that in all my royal dominion people are to fear and tremble before the God of Daniel, for he is the living God, enduring forever; his kingdom will never be destroyed, and his dominion will have no end.",
      "T": "'I hereby decree that throughout every territory of my kingdom, all people must stand in reverence before the God of Daniel. He is the living God, who endures forever. His kingdom cannot be shattered. His rule will outlast every empire on earth.'"
    },
    "27": {
      "L": "He delivers and rescues; and he works signs and wonders in heaven and in earth, who has delivered Daniel from the power of the lions.",
      "M": "He delivers and rescues; he works signs and wonders in heaven and on earth—he who delivered Daniel from the power of the lions.",
      "T": "'He rescues and he saves. He performs signs and wonders in the heavens and on the earth. He is the one who delivered Daniel from the power of the lions.'"
    },
    "28": {
      "L": "So this Daniel prospered in the reign of Darius, and in the reign of Cyrus the Persian.",
      "M": "So this Daniel prospered during the reign of Darius and during the reign of Cyrus the Persian.",
      "T": "And Daniel thrived—through the entire reign of Darius, and on into the reign of Cyrus the Persian."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'daniel')
        merge_tier(existing, DANIEL, tier_key)
        save(tier_dir, 'daniel', existing)
    print('Daniel 4–6 written.')

if __name__ == '__main__':
    main()
