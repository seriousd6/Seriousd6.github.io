"""
MKT Exodus chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-exodus-1-6.py

Covers: Israel's oppression in Egypt, Moses' birth and early life, the burning bush
and divine name revelation, Moses' commissioning, initial confrontation with Pharaoh,
Pharaoh's backlash against Israel, and God's covenant renewal speech (the YHWH disclosure).

Translation decisions:
- H3068 (יהוה): "the LORD" throughout in L/M; in T at 3:15 and 6:2–3 I use "Yahweh" because
  these are the formal name-disclosure moments where the hidden significance is explicitly being
  unveiled — otherwise T also uses "the LORD" to maintain register consistency.
- H430 (אֱלֹהִים): "God" throughout. At 4:16 "as God to him" is kept literal (L/M/T) because
  the meaning is not a divine claim but an authority-mediation role.
- H5315 (נֶפֶשׁ) at 1:5: "persons" in M (embodied self, not immaterial soul), "souls" in L
  (word-for-word), "descendants" in T (communicates the seventy living people).
- H1285 (בְּרִית) at 2:24, 6:4–5: "covenant" — formal, oath-bound relationship.
- H1961 (אֶהְיֶה) at 3:14: "I AM WHO I AM" — L/M follow the traditional translation;
  T adds "and I will be what I will be" in parenthetical apposition, capturing the imperfective
  aspect of the verb (ongoing self-existence and future dynamic presence).
- H6547 (פַּרְעֹה): "Pharaoh" — a title-name, not translated.
- H6189/H8193 at 6:12, 30 (ערל שפתים): L "uncircumcised lips" preserves the idiom;
  M "faltering lips" gives natural English; T "faltering and inarticulate" brings out the
  rhetorical incompetence Moses fears.
- H7706 (שַׁדַּי) at 6:3: "God Almighty" in L/M; "El Shaddai" in T since Moses is explicitly
  explaining a prior name, and El Shaddai is the technical OT patriarchal designation.
- H6531 (פֶּרֶךְ) at 1:13, 14: "with rigor/ruthlessly/brutally" — the Hebrew denotes crushing
  severity; T moves toward the visceral reality.
- Hardening of Pharaoh's heart (4:21, H2388 חָזַק): L "will harden," M "will harden,"
  T names both the divine act and the Pharaonic agency: "I myself will harden." The paradox
  (God hardens, Pharaoh also hardens himself in later chapters) is not resolved in 4:21 — it is
  simply stated. T does not over-explain.
- 6:3 exegetical note: The claim that YHWH was not known "by my name YHWH" to the patriarchs
  is not a contradiction of Genesis (where YHWH appears frequently) but a claim about the full
  covenant significance and enacted power of that name, now to be demonstrated through the Exodus.
  T surfaces this in "its full significance."
- Genealogy (6:14–27): Kept functional and clear. T compresses formal language slightly while
  retaining all names and family relationships. The genealogy's purpose is to authenticate Moses
  and Aaron as legitimate Levitical descendants.
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

EXODUS = {
  "1": {
    "1": {
      "L": "Now these are the names of the sons of Israel who came into Egypt with Jacob, each man with his household.",
      "M": "These are the names of the sons of Israel who came to Egypt with Jacob, each man with his family.",
      "T": "These are the names of Jacob's sons who entered Egypt—each man arriving with his own household."
    },
    "2": {
      "L": "Reuben, Simeon, Levi, and Judah;",
      "M": "Reuben, Simeon, Levi, and Judah;",
      "T": "Reuben, Simeon, Levi, and Judah;"
    },
    "3": {
      "L": "Issachar, Zebulun, and Benjamin;",
      "M": "Issachar, Zebulun, and Benjamin;",
      "T": "Issachar, Zebulun, and Benjamin;"
    },
    "4": {
      "L": "Dan and Naphtali, Gad and Asher.",
      "M": "Dan and Naphtali, Gad and Asher.",
      "T": "Dan and Naphtali, Gad and Asher."
    },
    "5": {
      "L": "All the souls coming from the loins of Jacob were seventy souls; but Joseph was already in Egypt.",
      "M": "The total number of Jacob's direct descendants was seventy persons; Joseph was already in Egypt.",
      "T": "Seventy of Jacob's own descendants made the journey—but Joseph was already in Egypt."
    },
    "6": {
      "L": "Then Joseph died, and all his brothers, and all that generation.",
      "M": "Joseph died, and all his brothers, and all that generation.",
      "T": "Joseph died. His brothers died. That whole generation passed away."
    },
    "7": {
      "L": "But the children of Israel were fruitful and increased abundantly, and multiplied and grew exceedingly mighty, so that the land was filled with them.",
      "M": "But the Israelites were fruitful and increased rapidly in number; they multiplied and grew exceedingly strong, so that the land was filled with them.",
      "T": "But the Israelites were fruitful and swarmed, multiplying with extraordinary vigor until the whole land of Egypt was teeming with them."
    },
    "8": {
      "L": "Now there arose a new king over Egypt who did not know Joseph.",
      "M": "Then a new king, who did not know about Joseph, came to power in Egypt.",
      "T": "Then a new king came to power in Egypt—one who knew nothing of Joseph."
    },
    "9": {
      "L": "And he said to his people, 'Behold, the people of the children of Israel are too many and too mighty for us.'",
      "M": "He said to his people, 'Look, the Israelite people are more numerous and stronger than we are.'",
      "T": "'Look,' he said to his people, 'these Israelites are becoming too numerous and too powerful for us.'"
    },
    "10": {
      "L": "'Come, let us deal wisely with them, lest they multiply, and if war befalls us, they join our enemies and fight against us and go up from the land.'",
      "M": "'Come, we must deal shrewdly with them, or they will multiply further, and if war breaks out, they may join our enemies and fight against us, and then leave the country.'",
      "T": "'We have to act shrewdly—if we let them keep multiplying, the day war comes they will side with our enemies, fight against us, and walk out of the country.'"
    },
    "11": {
      "L": "Therefore they set over them forced-labor overseers to afflict them with their burdens. They built storage cities for Pharaoh—Pithom and Raamses.",
      "M": "So they put slave masters over them to oppress them with forced labor, and they built Pithom and Rameses as store cities for Pharaoh.",
      "T": "The Egyptians put slave masters over them to crush them under forced labor. With that labor they built the storage cities of Pithom and Rameses for Pharaoh."
    },
    "12": {
      "L": "But the more they were afflicted, the more they multiplied and spread out, so that the Egyptians were in dread because of the children of Israel.",
      "M": "But the more they were oppressed, the more they multiplied and spread. So the Egyptians dreaded the Israelites.",
      "T": "But the harder they oppressed them, the more the Israelites multiplied and spread—until the Egyptians were filled with dread at the sight of them."
    },
    "13": {
      "L": "And the Egyptians made the children of Israel serve with rigor.",
      "M": "The Egyptians worked the Israelites ruthlessly.",
      "T": "The Egyptians drove the Israelites into brutal forced labor."
    },
    "14": {
      "L": "They made their lives bitter with hard labor in mortar and brick and in all kinds of labor in the field. In all their labor they made them serve with rigor.",
      "M": "They made their lives bitter with harsh labor—in brick and mortar and all kinds of fieldwork. All their labor was forced upon them ruthlessly.",
      "T": "Life became bitter—endless toil in mortar and brick, backbreaking fieldwork of every kind. Every form of their labor was grinding and merciless."
    },
    "15": {
      "L": "Then the king of Egypt spoke to the Hebrew midwives, of whom the name of the one was Shiphrah and the name of the other was Puah,",
      "M": "The king of Egypt commanded the Hebrew midwives, whose names were Shiphrah and Puah:",
      "T": "The king of Egypt gave orders to the Hebrew midwives—Shiphrah and Puah were their names—"
    },
    "16": {
      "L": "and said, 'When you serve as midwife to the Hebrew women and see them on the birthstool, if it is a son, you shall kill him; but if it is a daughter, she shall live.'",
      "M": "commanding them, 'When you are helping the Hebrew women during childbirth, if it is a boy, kill him; but if it is a girl, let her live.'",
      "T": "with this command: 'When you assist the Hebrew women in childbirth, if the child is a boy, kill him on the spot. If it is a girl, let her live.'"
    },
    "17": {
      "L": "But the midwives feared God and did not do as the king of Egypt commanded them; they let the male children live.",
      "M": "The midwives, however, feared God and did not do what the king of Egypt told them to do; they let the boys live.",
      "T": "But the midwives feared God. They refused to obey the king's command and kept the boys alive."
    },
    "18": {
      "L": "So the king of Egypt called the midwives and said to them, 'Why have you done this and let the male children live?'",
      "M": "Then the king of Egypt summoned the midwives and asked them, 'Why have you done this? Why have you let the boys live?'",
      "T": "Pharaoh summoned the midwives. 'Why have you done this?' he demanded. 'Why have you let the boys live?'"
    },
    "19": {
      "L": "The midwives said to Pharaoh, 'Because the Hebrew women are not like the Egyptian women; for they are vigorous and give birth before the midwife comes to them.'",
      "M": "The midwives answered Pharaoh, 'Hebrew women are not like Egyptian women; they are vigorous and give birth before the midwives arrive.'",
      "T": "The midwives told Pharaoh, 'Hebrew women are not like Egyptian women—they are strong and give birth before we can even get there.'"
    },
    "20": {
      "L": "So God dealt well with the midwives. And the people multiplied and grew very mighty.",
      "M": "So God was kind to the midwives and the people increased and became even more numerous.",
      "T": "God rewarded the midwives. The Israelite people kept multiplying and grew mightier still."
    },
    "21": {
      "L": "And because the midwives feared God, he made households for them.",
      "M": "And because the midwives feared God, he gave them families of their own.",
      "T": "Because the midwives feared God, he established families for them."
    },
    "22": {
      "L": "Then Pharaoh commanded all his people, 'Every son that is born you shall cast into the Nile, but every daughter you shall let live.'",
      "M": "Then Pharaoh gave this order to all his people: 'Every Hebrew boy that is born you must throw into the Nile, but let every girl live.'",
      "T": "Pharaoh issued an order to all his people: 'Every Hebrew boy who is born must be thrown into the Nile. Every girl you may let live.'"
    }
  },
  "2": {
    "1": {
      "L": "Now a man from the house of Levi went and took to wife a daughter of Levi.",
      "M": "A man from the tribe of Levi married a Levite woman.",
      "T": "A man of the tribe of Levi took a woman of his own tribe as his wife."
    },
    "2": {
      "L": "The woman conceived and bore a son. When she saw that he was a good child, she hid him three months.",
      "M": "She conceived and gave birth to a son. When she saw that he was a fine child, she hid him for three months.",
      "T": "She conceived and gave birth to a son. When she saw what a beautiful child he was, she hid him for three months."
    },
    "3": {
      "L": "When she could no longer hide him, she took for him an ark of papyrus and daubed it with tar and pitch. She put the child in it and placed it among the reeds along the bank of the Nile.",
      "M": "But when she could hide him no longer, she got a papyrus basket for him and coated it with tar and pitch. She placed the child in it and set it among the reeds along the bank of the Nile.",
      "T": "When she could no longer hide him, she wove a basket of papyrus reeds, sealed it with tar and pitch, laid the baby inside, and set it floating among the reeds at the river's edge."
    },
    "4": {
      "L": "And his sister stood at a distance to know what would be done to him.",
      "M": "His sister stood at a distance to see what would happen to him.",
      "T": "His sister took up a position some distance away to watch what would happen to him."
    },
    "5": {
      "L": "Now the daughter of Pharaoh came down to bathe at the Nile, and her maidens walked along by the riverside. She saw the ark among the reeds and sent her maidservant to fetch it.",
      "M": "Then Pharaoh's daughter went down to the Nile to bathe, and her attendants were walking along the riverbank. She saw the basket among the reeds and sent her female servant to get it.",
      "T": "Pharaoh's daughter came down to bathe in the Nile while her attendants walked along the bank. She spotted the basket among the reeds and sent her servant girl to fetch it."
    },
    "6": {
      "L": "When she opened it, she saw the child, and behold, the baby was crying. She had compassion on him and said, 'This is one of the Hebrews' children.'",
      "M": "She opened it and saw the baby. He was crying, and she felt sorry for him. 'This is one of the Hebrew babies,' she said.",
      "T": "She opened it and found the baby—he was crying. Her heart went out to him. 'This must be one of the Hebrew children,' she said."
    },
    "7": {
      "L": "Then his sister said to Pharaoh's daughter, 'Shall I go and call a nursing woman from the Hebrews to nurse the child for you?'",
      "M": "His sister asked Pharaoh's daughter, 'Shall I go and get one of the Hebrew women to nurse the baby for you?'",
      "T": "The baby's sister stepped forward and said to Pharaoh's daughter, 'Shall I go and find a Hebrew woman to nurse the baby for you?'"
    },
    "8": {
      "L": "And Pharaoh's daughter said to her, 'Go.' So the maiden went and called the child's mother.",
      "M": "Pharaoh's daughter told her, 'Yes, go.' So the girl went and got the baby's mother.",
      "T": "'Go,' said Pharaoh's daughter. The girl went and brought the child's own mother."
    },
    "9": {
      "L": "And Pharaoh's daughter said to her, 'Take this child away and nurse him for me, and I will give you your wages.' So the woman took the child and nursed him.",
      "M": "Pharaoh's daughter said to her, 'Take this baby and nurse him for me, and I will pay you.' So the woman took the baby and nursed him.",
      "T": "Pharaoh's daughter said to her, 'Take this baby and nurse him for me. I will pay you.' So the woman took her own child and nursed him."
    },
    "10": {
      "L": "When the child grew up, she brought him to Pharaoh's daughter, and he became her son. She named him Moses, saying, 'Because I drew him out of the water.'",
      "M": "When the child grew older, she took him to Pharaoh's daughter and he became her son. She named him Moses, saying, 'I drew him out of the water.'",
      "T": "The child grew, and she brought him to Pharaoh's daughter, who adopted him as her own son. She named him Moses—'Because,' she said, 'I drew him out of the water.'"
    },
    "11": {
      "L": "One day, when Moses had grown up, he went out to his people and looked on their burdens, and he saw an Egyptian striking a Hebrew, one of his brothers.",
      "M": "Years later, when Moses had grown up, he went out to where his own people were and watched them at their hard labor. He saw an Egyptian beating a Hebrew, one of his own people.",
      "T": "When Moses was grown, he went out to his own people and watched them struggling under their burdens. He saw an Egyptian beating a Hebrew—one of his own kinsmen."
    },
    "12": {
      "L": "He looked this way and that, and seeing no one, he struck down the Egyptian and hid him in the sand.",
      "M": "Looking around and seeing no one, he killed the Egyptian and hid him in the sand.",
      "T": "Moses glanced both ways; seeing no one, he killed the Egyptian and buried the body in the sand."
    },
    "13": {
      "L": "When he went out the next day, behold, two Hebrew men were struggling together. And he said to the one who was in the wrong, 'Why do you strike your fellow?'",
      "M": "The next day he went out and saw two Hebrews fighting. He asked the one who was in the wrong, 'Why are you hitting your fellow Hebrew?'",
      "T": "The next day he went out again and found two Hebrews brawling. He turned to the one who had started it: 'Why are you hitting your own countryman?'"
    },
    "14": {
      "L": "He said, 'Who made you a prince and judge over us? Do you intend to kill me as you killed the Egyptian?' And Moses was afraid, and thought, 'Surely the thing is known.'",
      "M": "The man asked, 'Who made you ruler and judge over us? Are you thinking of killing me as you killed the Egyptian?' Then Moses was afraid and thought, 'What I did must have become known.'",
      "T": "'Who appointed you as our ruler and judge?' the man shot back. 'Are you planning to kill me the way you killed that Egyptian?' Moses was gripped with fear. The matter had gotten out."
    },
    "15": {
      "L": "When Pharaoh heard of this, he sought to kill Moses. But Moses fled from the face of Pharaoh and stayed in the land of Midian. And he sat down by a well.",
      "M": "When Pharaoh heard about this, he tried to kill Moses, but Moses fled from Pharaoh and went to live in Midian, where he sat down beside a well.",
      "T": "When Pharaoh heard what had happened, he sought to kill Moses. Moses fled from Pharaoh and settled in Midian. There he sat down by a well."
    },
    "16": {
      "L": "Now the priest of Midian had seven daughters. They came and drew water, filling the troughs to water their father's flock.",
      "M": "Now a priest of Midian had seven daughters, and they came to draw water and fill the troughs to water their father's flock.",
      "T": "The priest of Midian had seven daughters. They came to the well, drew water, and filled the troughs to water their father's flocks."
    },
    "17": {
      "L": "The shepherds came and drove them away, but Moses stood up and saved them and watered their flock.",
      "M": "Some shepherds came along and drove the women away, but Moses got up and came to their rescue and watered their flock.",
      "T": "Shepherds came and drove them off, but Moses stood up, intervened on their behalf, and watered the flocks himself."
    },
    "18": {
      "L": "When they came home to Reuel their father, he said, 'How is it that you have come home so quickly today?'",
      "M": "When they came home to their father Reuel, he asked them, 'Why have you returned so early today?'",
      "T": "When they returned to their father Reuel, he asked, 'Why are you back so early today?'"
    },
    "19": {
      "L": "They said, 'An Egyptian man delivered us out of the hand of the shepherds and even drew water for us and watered the flock.'",
      "M": "They answered, 'An Egyptian rescued us from the shepherds. He even drew water for us and watered the flock.'",
      "T": "'An Egyptian man rescued us from the shepherds,' they told him. 'He even drew water for us and watered the flocks.'"
    },
    "20": {
      "L": "And he said to his daughters, 'Then where is he? Why have you left the man? Call him, that he may eat bread.'",
      "M": "Reuel said to his daughters, 'And where is he? Why did you leave him? Invite him to have something to eat.'",
      "T": "'Where is he?' Reuel asked his daughters. 'Why did you leave him there? Invite him in for a meal.'"
    },
    "21": {
      "L": "And Moses was content to dwell with the man, and he gave Moses his daughter Zipporah.",
      "M": "Moses agreed to stay with the man, who gave his daughter Zipporah to Moses in marriage.",
      "T": "Moses was content to settle with him, and Reuel gave his daughter Zipporah to Moses as his wife."
    },
    "22": {
      "L": "She bore a son, and he called his name Gershom, for he said, 'I have been a sojourner in a foreign land.'",
      "M": "Zipporah gave birth to a son, and Moses named him Gershom, saying, 'I have become a foreigner in a foreign land.'",
      "T": "She bore a son, and Moses named him Gershom—'Sojourner there'—for he said, 'I have been a stranger in a foreign land.'"
    },
    "23": {
      "L": "During those many days the king of Egypt died, and the children of Israel groaned because of their slavery and cried out. Their cry for rescue from slavery rose up to God.",
      "M": "During that long period, the king of Egypt died. The Israelites groaned in their slavery and cried out, and their cry for help because of their slavery went up to God.",
      "T": "A long time passed. The king of Egypt died. The Israelites were still groaning under their bondage; they cried out, and their cry from slavery ascended to God."
    },
    "24": {
      "L": "And God heard their groaning, and God remembered his covenant with Abraham, with Isaac, and with Jacob.",
      "M": "God heard their groaning and he remembered his covenant with Abraham, with Isaac and with Jacob.",
      "T": "God heard their groaning. God remembered the covenant he had made with Abraham, Isaac, and Jacob."
    },
    "25": {
      "L": "God saw the children of Israel, and God knew.",
      "M": "So God looked on the Israelites and was concerned about them.",
      "T": "God saw the Israelites. God took notice."
    }
  },
  "3": {
    "1": {
      "L": "Now Moses was keeping the flock of his father-in-law Jethro, the priest of Midian. He led the flock to the far side of the desert and came to Horeb, the mountain of God.",
      "M": "Now Moses was tending the flock of Jethro his father-in-law, the priest of Midian. He led the flock to the far side of the wilderness and came to Horeb, the mountain of God.",
      "T": "Moses was tending the flock of his father-in-law Jethro, priest of Midian, when he led the sheep to the far side of the desert and came to Horeb—the mountain of God."
    },
    "2": {
      "L": "And the angel of the LORD appeared to him in a flame of fire out of the midst of a bush. He looked, and behold, the bush was burning with fire, yet the bush was not consumed.",
      "M": "There the angel of the LORD appeared to him in flames of fire from within a bush. Moses saw that though the bush was on fire it did not burn up.",
      "T": "There the angel of the LORD appeared to him—a flame of fire blazing from the heart of a thornbush. Moses looked: the bush was burning, yet the bush was not being consumed."
    },
    "3": {
      "L": "Moses said, 'I will turn aside and see this great sight—why the bush is not burned.'",
      "M": "So Moses thought, 'I will go over and see this strange sight—why the bush does not burn up.'",
      "T": "Moses said to himself, 'Let me step aside and look at this remarkable sight—why isn't the bush burning up?'"
    },
    "4": {
      "L": "When the LORD saw that he turned aside to see, God called to him out of the bush, 'Moses, Moses!' And he said, 'Here I am.'",
      "M": "When the LORD saw that he had gone over to look, God called to him from within the bush, 'Moses! Moses!' And Moses said, 'Here I am.'",
      "T": "When the LORD saw that Moses had turned aside to look, God called to him from the heart of the bush: 'Moses! Moses!' 'Here I am,' Moses answered."
    },
    "5": {
      "L": "Then he said, 'Do not come near! Take off your sandals from your feet, for the place where you are standing is holy ground.'",
      "M": "'Do not come any closer,' God said. 'Take off your sandals, for the place where you are standing is holy ground.'",
      "T": "'Come no closer,' God said. 'Take off your sandals—the ground where you stand is holy ground.'"
    },
    "6": {
      "L": "He said also, 'I am the God of your father—the God of Abraham, the God of Isaac, and the God of Jacob.' And Moses hid his face, for he was afraid to look at God.",
      "M": "Then he said, 'I am the God of your father, the God of Abraham, the God of Isaac and the God of Jacob.' At this, Moses hid his face, because he was afraid to look at God.",
      "T": "Then he said, 'I am the God of your father—the God of Abraham, the God of Isaac, the God of Jacob.' Moses covered his face, afraid to look at God."
    },
    "7": {
      "L": "Then the LORD said, 'I have surely seen the affliction of my people who are in Egypt and have heard their cry because of their taskmasters. I know their sorrows.'",
      "M": "The LORD said, 'I have indeed seen the misery of my people in Egypt. I have heard them crying out because of their slave drivers, and I am concerned about their suffering.'",
      "T": "'I have seen the suffering of my people in Egypt,' the LORD said. 'I have heard their cry under the taskmasters. I know what they are enduring.'"
    },
    "8": {
      "L": "'So I have come down to deliver them from the hand of the Egyptians and to bring them up from that land to a good and broad land, a land flowing with milk and honey—to the place of the Canaanites, the Hittites, the Amorites, the Perizzites, the Hivites, and the Jebusites.'",
      "M": "'So I have come down to rescue them from the hand of the Egyptians and to bring them up out of that land into a good and spacious land, a land flowing with milk and honey—the home of the Canaanites, Hittites, Amorites, Perizzites, Hivites, and Jebusites.'",
      "T": "'So I have come down to rescue them from Egypt's grip, to bring them up out of that land into a good and wide land—a land overflowing with milk and honey—the territory now occupied by the Canaanites, Hittites, Amorites, Perizzites, Hivites, and Jebusites.'"
    },
    "9": {
      "L": "'And now, behold, the cry of the children of Israel has come to me, and I have also seen the oppression with which the Egyptians oppress them.'",
      "M": "'And now the cry of the Israelites has reached me, and I have seen the way the Egyptians are oppressing them.'",
      "T": "'The cry of the Israelites has reached me—I have seen how the Egyptians are crushing them.'"
    },
    "10": {
      "L": "'Come now, therefore, and I will send you to Pharaoh, that you may bring my people, the children of Israel, out of Egypt.'",
      "M": "'So now, go. I am sending you to Pharaoh to bring my people the Israelites out of Egypt.'",
      "T": "'So go—I am sending you to Pharaoh. Bring my people, the Israelites, out of Egypt.'"
    },
    "11": {
      "L": "But Moses said to God, 'Who am I that I should go to Pharaoh and bring the children of Israel out of Egypt?'",
      "M": "But Moses said to God, 'Who am I that I should go to Pharaoh and bring the Israelites out of Egypt?'",
      "T": "But Moses said to God, 'Who am I to go to Pharaoh? Who am I to lead the Israelites out of Egypt?'"
    },
    "12": {
      "L": "He said, 'But I will be with you, and this shall be the sign for you, that I have sent you: when you have brought the people out of Egypt, you shall serve God on this mountain.'",
      "M": "And God said, 'I will be with you. And this will be the sign to you that it is I who have sent you: When you have brought the people out of Egypt, you will worship God on this mountain.'",
      "T": "'I will be with you,' God said. 'And this is how you will know I sent you: when you have brought the people out of Egypt, you will worship God right here on this mountain.'"
    },
    "13": {
      "L": "Then Moses said to God, 'If I come to the children of Israel and say to them, \"The God of your fathers has sent me to you,\" and they ask me, \"What is his name?\" what shall I say to them?'",
      "M": "Moses said to God, 'Suppose I go to the Israelites and say to them, \"The God of your fathers has sent me to you,\" and they ask me, \"What is his name?\" Then what shall I tell them?'",
      "T": "Moses said to God, 'Suppose I go to the Israelites and tell them, \"The God of your fathers has sent me.\" And they ask, \"What is his name?\"—what do I say?'"
    },
    "14": {
      "L": "God said to Moses, 'I AM WHO I AM.' He said, 'Say this to the children of Israel: \"I AM has sent me to you.\"'",
      "M": "God said to Moses, 'I AM WHO I AM.' And he said, 'Say this to the Israelites: \"I AM has sent me to you.\"'",
      "T": "God said to Moses, 'I AM WHO I AM—and I will be what I will be.' Then he said, 'Tell the Israelites: \"I AM has sent me to you.\"'"
    },
    "15": {
      "L": "God also said to Moses, 'Say this to the children of Israel: \"The LORD, the God of your fathers—the God of Abraham, the God of Isaac, and the God of Jacob—has sent me to you.\" This is my name forever, and thus I am to be remembered throughout all generations.'",
      "M": "God also said to Moses, 'Say to the Israelites, \"The LORD, the God of your fathers—the God of Abraham, the God of Isaac and the God of Jacob—has sent me to you.\" This is my name forever, the name you shall call me from generation to generation.'",
      "T": "God said further, 'Tell the Israelites: \"Yahweh—the God of your fathers, the God of Abraham, Isaac, and Jacob—has sent me to you.\" This is my name forever. This is how I am to be remembered in every generation.'"
    },
    "16": {
      "L": "'Go and gather the elders of Israel and say to them, \"The LORD, the God of your fathers—the God of Abraham, of Isaac, and of Jacob—has appeared to me, saying, I have surely visited you and seen what has been done to you in Egypt.\"'",
      "M": "'Go, assemble the elders of Israel and say to them, \"The LORD, the God of your fathers—the God of Abraham, Isaac, and Jacob—appeared to me and said: I have watched over you and have seen what has been done to you in Egypt.\"'",
      "T": "'Go and assemble the elders of Israel. Tell them: \"The LORD—the God of your fathers, Abraham's God, Isaac's God, Jacob's God—has appeared to me. He says: I have seen what Egypt has done to you, and I have come.\"'"
    },
    "17": {
      "L": "'And I have said I will bring you up from the affliction of Egypt to the land of the Canaanites, the Hittites, the Amorites, the Perizzites, the Hivites, and the Jebusites—a land flowing with milk and honey.'",
      "M": "'And I have promised to bring you up out of your misery in Egypt into the land of the Canaanites, Hittites, Amorites, Perizzites, Hivites and Jebusites—a land flowing with milk and honey.'",
      "T": "'I have promised to bring you up from Egypt's misery into the land of the Canaanites, Hittites, Amorites, Perizzites, Hivites, and Jebusites—a land flowing with milk and honey.'"
    },
    "18": {
      "L": "'And they shall listen to your voice. And you and the elders of Israel shall go to the king of Egypt and say to him, \"The LORD, the God of the Hebrews, has met with us. And now, please let us go a three-day journey into the wilderness, that we may sacrifice to the LORD our God.\"'",
      "M": "'The elders of Israel will listen to you. Then you and the elders are to go to the king of Egypt and say to him, \"The LORD, the God of the Hebrews, has met with us. Let us take a three-day journey into the wilderness to offer sacrifices to the LORD our God.\"'",
      "T": "'The elders will listen to you. Then you and the elders are to go to Pharaoh and say: \"The LORD, the God of the Hebrews, has appeared to us. Please let us go three days' journey into the desert to offer sacrifice to the LORD our God.\"'"
    },
    "19": {
      "L": "'And I know that the king of Egypt will not let you go unless compelled by a mighty hand.'",
      "M": "'But I know that the king of Egypt will not let you go unless a mighty hand compels him.'",
      "T": "'I know Pharaoh well—he will not let you go unless forced by a mighty hand.'"
    },
    "20": {
      "L": "'So I will stretch out my hand and strike Egypt with all the wonders that I will do in it. After that he will let you go.'",
      "M": "'So I will stretch out my hand and strike the Egyptians with all the wonders that I will perform among them. After that, he will let you go.'",
      "T": "'I will stretch out my hand and strike Egypt with wonder after wonder. After that, Pharaoh will release you.'"
    },
    "21": {
      "L": "'And I will give this people favor in the eyes of the Egyptians. It shall be, when you go, that you shall not go empty-handed.'",
      "M": "'And I will make the Egyptians favorably disposed toward this people, so that when you leave you will not go empty-handed.'",
      "T": "'I will cause the Egyptians to look favorably on my people, so that when you leave, you will not go out empty-handed.'"
    },
    "22": {
      "L": "'But each woman shall ask of her neighbor and of the woman who sojourns in her house, for articles of silver and gold and for clothing. You shall put them on your sons and on your daughters. Thus you shall plunder Egypt.'",
      "M": "'Every woman is to ask her neighbor and any woman living in her house for articles of silver and gold and for clothing, which you will put on your sons and daughters. And so you will plunder the Egyptians.'",
      "T": "'Every Israelite woman is to ask her Egyptian neighbor for jewelry of silver and gold and for fine clothing. You will dress your sons and daughters in them—and strip Egypt clean.'"
    }
  },
  "4": {
    "1": {
      "L": "Then Moses answered and said, 'But behold, they will not believe me or listen to my voice, for they will say, \"The LORD did not appear to you.\"'",
      "M": "Moses answered, 'What if they do not believe me or listen to me and say, \"The LORD did not appear to you\"?'",
      "T": "Moses objected: 'But what if they don't believe me—if they refuse to listen and say, \"The LORD never appeared to you\"?'"
    },
    "2": {
      "L": "The LORD said to him, 'What is that in your hand?' He said, 'A staff.'",
      "M": "Then the LORD asked him, 'What is that in your hand?' 'A staff,' he replied.",
      "T": "'What is that in your hand?' the LORD asked. 'A staff,' Moses said."
    },
    "3": {
      "L": "And he said, 'Throw it on the ground.' So he threw it on the ground, and it became a serpent, and Moses fled from it.",
      "M": "'Throw it on the ground,' the LORD said. Moses threw it on the ground and it became a snake, and he ran from it.",
      "T": "'Throw it on the ground,' the LORD said. Moses threw it down, and it became a snake. Moses ran from it."
    },
    "4": {
      "L": "And the LORD said to Moses, 'Put out your hand and take it by the tail.' So he put out his hand and caught it, and it became a staff in his hand.",
      "M": "Then the LORD said to him, 'Reach out your hand and take it by the tail.' So Moses reached out and took hold of the snake and it turned back into a staff in his hand.",
      "T": "'Reach out and take it by the tail,' the LORD told him. Moses reached out and grabbed it, and it became a staff in his hand again."
    },
    "5": {
      "L": "'—so that they may believe that the LORD, the God of their fathers, the God of Abraham, the God of Isaac, and the God of Jacob, has appeared to you.'",
      "M": "'This is so that they may believe that the LORD, the God of their fathers—the God of Abraham, the God of Isaac and the God of Jacob—has appeared to you.'",
      "T": "'That will convince them that the LORD has appeared to you—the God of their fathers, Abraham's God, Isaac's God, Jacob's God.'"
    },
    "6": {
      "L": "Again, the LORD said to him, 'Put your hand inside your cloak.' And he put his hand inside his cloak, and when he took it out, behold, his hand was leprous like snow.",
      "M": "Then the LORD said, 'Put your hand inside your cloak.' So Moses put his hand into his cloak, and when he took it out, the skin was leprous—white as snow.",
      "T": "Then the LORD said, 'Now put your hand inside your cloak.' He did—and when he withdrew it, the hand was covered with disease, white as snow."
    },
    "7": {
      "L": "Then God said, 'Put your hand back inside your cloak.' So he put his hand back inside his cloak, and when he took it out, behold, it was restored like the rest of his flesh.",
      "M": "'Now put it back into your cloak,' he said. So Moses put his hand back into his cloak, and when he took it out, it was restored, like the rest of his skin.",
      "T": "'Put it back,' the LORD said. He did—and when he withdrew it again, the hand was fully restored, like the rest of his skin."
    },
    "8": {
      "L": "'If they will not believe you or listen to the voice of the first sign, they may believe the voice of the second sign.'",
      "M": "'If they do not believe you or pay attention to the first sign, they may believe the second.'",
      "T": "'If they are not convinced by the first sign, the second should convince them.'"
    },
    "9": {
      "L": "'And if they will not believe even these two signs or listen to your voice, you shall take some water from the Nile and pour it on the dry ground. And the water that you shall take from the Nile will become blood on the dry ground.'",
      "M": "'But if they do not believe these two signs or listen to you, take some water from the Nile and pour it on the dry ground. The water you take from the river will become blood on the ground.'",
      "T": "'If they still refuse to believe after both signs, here is what you do: take water from the Nile and pour it on dry ground. The Nile water will become blood the moment it hits the earth.'"
    },
    "10": {
      "L": "But Moses said to the LORD, 'O Lord, I am not a man of words—not in the past and not since you have spoken to your servant—for I am slow of speech and slow of tongue.'",
      "M": "Moses said to the LORD, 'Pardon your servant, Lord. I have never been eloquent, neither in the past nor since you have spoken to your servant. I am slow of speech and tongue.'",
      "T": "'My Lord,' Moses said, 'I have never been a man of words—not before and not now that you have spoken to me. I am slow and inarticulate.'"
    },
    "11": {
      "L": "Then the LORD said to him, 'Who made man's mouth? Who makes him mute, or deaf, or seeing, or blind? Is it not I, the LORD?'",
      "M": "The LORD said to him, 'Who gave human beings their mouths? Who makes them deaf or mute? Who gives them sight or makes them blind? Is it not I, the LORD?'",
      "T": "'Who made the human mouth?' the LORD replied. 'Who makes someone deaf or mute, sighted or blind? Is it not I, the LORD?'"
    },
    "12": {
      "L": "'Now therefore go, and I will be with your mouth and teach you what you shall speak.'",
      "M": "'Now go; I will help you speak and will teach you what to say.'",
      "T": "'Now go—I will be with your mouth and teach you what to say.'"
    },
    "13": {
      "L": "But he said, 'Oh, my Lord, please send by the hand of whomever else you will send.'",
      "M": "But Moses said, 'Pardon your servant, Lord. Please send someone else.'",
      "T": "'Please, my Lord,' Moses said. 'Send someone else.'"
    },
    "14": {
      "L": "Then the anger of the LORD was kindled against Moses, and he said, 'Is there not Aaron your brother, the Levite? I know that he can speak well. Moreover, behold, he is coming out to meet you, and when he sees you, he will be glad in his heart.'",
      "M": "Then the LORD's anger burned against Moses and he said, 'What about your brother Aaron the Levite? I know he can speak well. He is already on his way to meet you, and he will be glad to see you.'",
      "T": "The LORD's anger flared at Moses. 'Your brother Aaron the Levite—he can certainly speak. And right now he is on his way to meet you, and when he sees you, his heart will be glad.'"
    },
    "15": {
      "L": "'You shall speak to him and put the words in his mouth, and I will be with your mouth and with his mouth and will teach you both what to do.'",
      "M": "'You are to speak to him and put words in his mouth; I will help both of you speak and will teach you what to do.'",
      "T": "'You will speak to him and put the words in his mouth. I will be with both your mouths and teach you what to do.'"
    },
    "16": {
      "L": "'He will speak for you to the people, and he will be a mouth for you, and you will be as God to him.'",
      "M": "'He will speak to the people for you, and it will be as if he were your mouth and as if you were God to him.'",
      "T": "'He will be your mouthpiece to the people, the way you speak for God to him.'"
    },
    "17": {
      "L": "'And you shall take in your hand this staff, with which you shall do the signs.'",
      "M": "'But take this staff in your hand so you can perform the signs with it.'",
      "T": "'Take this staff in your hand—it is the instrument you will use to perform the signs.'"
    },
    "18": {
      "L": "Moses went back to Jethro his father-in-law and said to him, 'Please let me go back to my brothers in Egypt to see whether they are still alive.' And Jethro said to Moses, 'Go in peace.'",
      "M": "Then Moses went back to Jethro his father-in-law and said to him, 'Let me return to my own people in Egypt to see if any of them are still alive.' Jethro said, 'Go, and I wish you well.'",
      "T": "Moses went back to his father-in-law Jethro. 'Let me return to my kinsmen in Egypt,' he said, 'and see if they are still alive.' Jethro said, 'Go with my blessing.'"
    },
    "19": {
      "L": "And the LORD said to Moses in Midian, 'Go, return to Egypt, for all the men who were seeking your life are dead.'",
      "M": "Now the LORD had said to Moses in Midian, 'Go back to Egypt, for all those who wanted to kill you are dead.'",
      "T": "The LORD had told Moses in Midian, 'Go back to Egypt—all those who wanted you dead are gone.'"
    },
    "20": {
      "L": "So Moses took his wife and his sons and set them on a donkey, and went back to the land of Egypt. And Moses took the staff of God in his hand.",
      "M": "So Moses took his wife and sons, put them on a donkey and started back to Egypt. And he took the staff of God in his hand.",
      "T": "Moses loaded his wife and sons on a donkey and headed back to Egypt, with the staff of God in his hand."
    },
    "21": {
      "L": "And the LORD said to Moses, 'When you go back to Egypt, see that you do before Pharaoh all the miracles that I have put in your power. But I will harden his heart so that he will not let the people go.'",
      "M": "The LORD said to Moses, 'When you return to Egypt, see that you perform before Pharaoh all the wonders I have given you the power to do. But I will harden his heart so that he will not let the people go.'",
      "T": "'When you arrive in Egypt,' the LORD told Moses, 'perform all the wonders I have given you before Pharaoh. But I myself will harden his heart so that he will not let the people go.'"
    },
    "22": {
      "L": "'Then you shall say to Pharaoh, \"Thus says the LORD: Israel is my son, my firstborn.\"'",
      "M": "'Then say to Pharaoh, \"This is what the LORD says: Israel is my firstborn son.\"'",
      "T": "'Then tell Pharaoh: \"This is what the LORD says: Israel is my son, my firstborn.\"'"
    },
    "23": {
      "L": "'And I say to you, \"Let my son go, that he may serve me.\" If you refuse to let him go, behold, I will kill your son, your firstborn.'",
      "M": "'And I told you, \"Let my son go, so he may worship me.\" But you refused to let him go; so I will kill your firstborn son.'",
      "T": "'I am saying to you: Let my son go, so he can worship me. If you refuse to let him go, I will put your firstborn son to death.'"
    },
    "24": {
      "L": "At a lodging place on the way, the LORD met him and sought to kill him.",
      "M": "At a lodging place on the way, the LORD met Moses and was about to kill him.",
      "T": "On the road, at the lodging place, the LORD confronted Moses and was about to kill him."
    },
    "25": {
      "L": "Then Zipporah took a flint and cut off her son's foreskin and touched his feet with it and said, 'Surely you are a bridegroom of blood to me.'",
      "M": "But Zipporah took a flint knife, cut off her son's foreskin and touched Moses' feet with it. 'Surely you are a bridegroom of blood to me,' she said.",
      "T": "Zipporah grabbed a sharp stone, cut off her son's foreskin, and threw it at Moses' feet. 'You are a bridegroom of blood to me!' she cried."
    },
    "26": {
      "L": "So he let him go. It was then that she said, 'A bridegroom of blood,' because of the circumcision.",
      "M": "So the LORD let him alone. (At that time she said 'bridegroom of blood,' referring to circumcision.)",
      "T": "Then God let him go. Zipporah's words—'a bridegroom of blood'—referred to the circumcision."
    },
    "27": {
      "L": "The LORD said to Aaron, 'Go into the wilderness to meet Moses.' So he went and met him at the mountain of God and kissed him.",
      "M": "The LORD said to Aaron, 'Go into the wilderness to meet Moses.' So he met Moses at the mountain of God and kissed him.",
      "T": "The LORD told Aaron, 'Go into the desert to meet Moses.' Aaron went and met him at the mountain of God. They embraced."
    },
    "28": {
      "L": "And Moses told Aaron all the words of the LORD with which he had sent him to speak, and all the signs that he had commanded him to do.",
      "M": "Moses told Aaron everything the LORD had said when he sent him, and also about all the signs he had commanded him to perform.",
      "T": "Moses told Aaron everything the LORD had said when he sent him, and all the signs he had commissioned him to perform."
    },
    "29": {
      "L": "Then Moses and Aaron went and gathered together all the elders of the children of Israel.",
      "M": "Moses and Aaron brought together all the elders of the Israelites,",
      "T": "Moses and Aaron assembled all the elders of Israel."
    },
    "30": {
      "L": "And Aaron spoke all the words that the LORD had spoken to Moses and did the signs in the sight of the people.",
      "M": "and Aaron told them everything the LORD had said to Moses. He also performed the signs before the people,",
      "T": "Aaron spoke everything the LORD had told Moses, then performed the signs before the people."
    },
    "31": {
      "L": "And the people believed. And when they heard that the LORD had visited the children of Israel and that he had seen their affliction, they bowed their heads and worshipped.",
      "M": "and they believed. And when they heard that the LORD was concerned about them and had seen their misery, they bowed down and worshipped.",
      "T": "The people believed. When they heard that the LORD had taken notice of them and had seen their suffering, they bowed their heads and worshipped."
    }
  },
  "5": {
    "1": {
      "L": "Afterward Moses and Aaron went and said to Pharaoh, 'Thus says the LORD, the God of Israel: \"Let my people go, that they may hold a feast to me in the wilderness.\"'",
      "M": "Afterward Moses and Aaron went to Pharaoh and said, 'This is what the LORD, the God of Israel, says: \"Let my people go, so that they may hold a festival to me in the wilderness.\"'",
      "T": "Moses and Aaron went to Pharaoh and said, 'This is what the LORD, the God of Israel, declares: \"Let my people go, so they can celebrate a festival to me in the desert.\"'"
    },
    "2": {
      "L": "But Pharaoh said, 'Who is the LORD, that I should obey his voice and let Israel go? I do not know the LORD, and moreover I will not let Israel go.'",
      "M": "Pharaoh said, 'Who is the LORD, that I should obey him and let Israel go? I do not know the LORD and I will not let Israel go.'",
      "T": "Pharaoh said, 'Who is this LORD that I should obey him and let Israel go? I don't know this LORD, and I will not let Israel go.'"
    },
    "3": {
      "L": "Then they said, 'The God of the Hebrews has met with us. Please let us go a three-day journey into the desert and sacrifice to the LORD our God, or he will strike us with pestilence or with the sword.'",
      "M": "Then they said, 'The God of the Hebrews has met with us. Now let us take a three-day journey into the wilderness to offer sacrifices to the LORD our God, or he may strike us with plagues or with the sword.'",
      "T": "'The God of the Hebrews has appeared to us,' they said. 'Please let us take a three-day journey into the desert and offer sacrifice to the LORD our God—otherwise he may strike us with plague or the sword.'"
    },
    "4": {
      "L": "But the king of Egypt said to them, 'Moses and Aaron, why do you take the people away from their work? Get back to your burdens.'",
      "M": "But the king of Egypt said, 'Moses and Aaron, why are you taking the people away from their labor? Get back to your work!'",
      "T": "The king of Egypt said, 'Moses and Aaron, why are you pulling the people away from their work? Get back to your labor!'"
    },
    "5": {
      "L": "Pharaoh said, 'Behold, the people of the land are now many, and you make them rest from their burdens!'",
      "M": "Pharaoh said, 'Look, the people of the land are now numerous, and you are stopping them from working.'",
      "T": "Pharaoh said, 'There are so many of these people—and you are giving them excuses to stop working!'"
    },
    "6": {
      "L": "The same day Pharaoh commanded the taskmasters of the people and their foremen,",
      "M": "That same day Pharaoh gave this order to the slave drivers and overseers in charge of the people:",
      "T": "That very day Pharaoh issued orders to the slave drivers and foremen:"
    },
    "7": {
      "L": "'You shall no longer give the people straw to make brick as in the past. Let them go and gather straw for themselves.'",
      "M": "'You are no longer to supply the people with straw for making bricks; let them go and gather their own straw.'",
      "T": "'Stop supplying the people with straw for making bricks. Make them go find their own.'"
    },
    "8": {
      "L": "'But demand of them the same quota of bricks as before. Do not reduce it, for they are idle. That is why they cry, \"Let us go and offer sacrifice to our God.\"'",
      "M": "'But require them to make the same number of bricks as before; don't reduce the quota. They are lazy; that is why they are crying out, \"Let us go and sacrifice to our God.\"'",
      "T": "'But require the same quota of bricks as before—not one less. They are lazy, which is why they keep saying, \"Let us go and offer sacrifice to our God.\"'"
    },
    "9": {
      "L": "'Let heavier work be laid on the men that they may labor at it and pay no attention to lying words.'",
      "M": "'Make the work harder for the people so that they keep working and pay no attention to lies.'",
      "T": "'Pile on the work—keep them so busy they don't have time to listen to Moses' empty words.'"
    },
    "10": {
      "L": "So the taskmasters and the foremen of the people went out and said to the people, 'Thus says Pharaoh, \"I will not give you straw.\"'",
      "M": "The slave drivers and the overseers went out and said to the people, 'This is what Pharaoh says: \"I will not give you any more straw.\"'",
      "T": "The slave drivers and foremen went out to the people and announced, 'Pharaoh's orders: no more straw.'"
    },
    "11": {
      "L": "'Go and find straw for yourselves wherever you can, for none of your work will be reduced.'",
      "M": "'Go get your own straw wherever you can find it, but your work will not be reduced at all.'",
      "T": "'Go and find straw wherever you can—but your quota is not going down by one brick.'"
    },
    "12": {
      "L": "So the people were scattered throughout all the land of Egypt to gather stubble for straw.",
      "M": "So the people scattered all over Egypt to gather stubble to use for straw.",
      "T": "The people scattered across Egypt, picking up stubble to use in place of straw."
    },
    "13": {
      "L": "The taskmasters were urgent, saying, 'Complete your work, your daily task, each day, as when there was straw.'",
      "M": "The slave drivers kept pressing them, saying, 'Complete the work required of you for each day, just as when you had straw.'",
      "T": "The slave drivers pressed them relentlessly: 'Meet your daily quota—same as when straw was provided.'"
    },
    "14": {
      "L": "And the foremen of the children of Israel, whom Pharaoh's taskmasters had set over them, were beaten and asked, 'Why have you not fulfilled your task of making bricks as before?'",
      "M": "Then Israelite overseers appointed by Pharaoh's slave drivers were beaten and were asked, 'Why didn't you meet your quota of bricks yesterday and today, as before?'",
      "T": "The Israelite foremen whom Pharaoh's slave drivers had appointed were beaten. 'Why haven't you met your brick quota, the same as before?' they were demanded."
    },
    "15": {
      "L": "Then the foremen of the children of Israel came and cried to Pharaoh, 'Why do you treat your servants like this?'",
      "M": "Then the Israelite overseers went and appealed to Pharaoh: 'Why have you treated your servants this way?'",
      "T": "The Israelite foremen went to Pharaoh and cried out, 'Why are you treating your servants this way?'"
    },
    "16": {
      "L": "'No straw is given to your servants, yet they say to us, \"Make bricks!\" And behold, your servants are beaten; but the fault is in your own people.'",
      "M": "'Your servants are given no straw, yet we are told, \"Make bricks!\" Your servants are being beaten, but the fault lies with your own people.'",
      "T": "'No straw has been given to us, yet they demand: \"Make bricks!\" Your servants are being beaten, and the blame lies squarely with your own officials.'"
    },
    "17": {
      "L": "He said, 'You are idle, you are idle! That is why you say, \"Let us go and sacrifice to the LORD.\"'",
      "M": "Pharaoh said, 'Lazy, that's what you are—lazy! That is why you keep saying, \"Let us go and sacrifice to the LORD.\"'",
      "T": "Pharaoh said, 'Idle! You are idle! That is why you keep whining, \"Let us go and offer sacrifice to the LORD.\"'"
    },
    "18": {
      "L": "'Go now and work. No straw will be given you, but you must deliver the same number of bricks.'",
      "M": "'Now get to work. You will not be given any straw, yet you must produce your full quota of bricks.'",
      "T": "'Get back to work. No straw, same quota—that's final.'"
    },
    "19": {
      "L": "The foremen of the children of Israel saw that they were in trouble when they heard, 'You shall not reduce your daily number of bricks.'",
      "M": "The Israelite overseers realized they were in serious trouble when they were told, 'You are not to reduce the number of bricks required of you for each day.'",
      "T": "The Israelite foremen understood the trouble they were in when they were told, 'You will not reduce the daily brick quota by even one.'"
    },
    "20": {
      "L": "When they came out from Pharaoh, they met Moses and Aaron, who were standing there waiting for them.",
      "M": "When they left Pharaoh, they found Moses and Aaron waiting to meet them,",
      "T": "Coming out from Pharaoh's presence, they ran into Moses and Aaron who were waiting for them."
    },
    "21": {
      "L": "And they said to them, 'The LORD look on you and judge, because you have made us stink in the eyes of Pharaoh and in the eyes of his servants, and have put a sword in their hand to kill us.'",
      "M": "'May the LORD look on you and judge you! You have made us obnoxious to Pharaoh and his officials and have put a sword in their hand to kill us.'",
      "T": "'May the LORD see what you have done and judge you for it! You have made us repugnant to Pharaoh and his officials—you have put a sword in their hands to kill us.'"
    },
    "22": {
      "L": "Then Moses turned to the LORD and said, 'O Lord, why have you done evil to this people? Why did you ever send me?'",
      "M": "Moses returned to the LORD and said, 'Why, Lord, why have you brought trouble on this people? Is this why you sent me?'",
      "T": "Moses went back to the LORD. 'My Lord,' he said, 'why have you brought disaster on this people? Is this what you sent me for?'"
    },
    "23": {
      "L": "'For since I came to Pharaoh to speak in your name, he has done evil to this people, and you have not delivered your people at all.'",
      "M": "'Ever since I went to Pharaoh to speak in your name, he has brought trouble on this people, and you have not rescued your people at all.'",
      "T": "'Since I first went to Pharaoh to speak in your name, he has only made things worse for these people—and you have done nothing to rescue them.'"
    }
  },
  "6": {
    "1": {
      "L": "Then the LORD said to Moses, 'Now you shall see what I will do to Pharaoh. For with a strong hand he will let them go, and with a strong hand he will drive them out of his land.'",
      "M": "Then the LORD said to Moses, 'Now you will see what I will do to Pharaoh: Because of my mighty hand he will let them go; because of my mighty hand he will drive them out of his country.'",
      "T": "The LORD said to Moses, 'Now you will see what I am going to do to Pharaoh. My strong hand will compel him—not merely let them go, but drive them out.'"
    },
    "2": {
      "L": "God spoke to Moses and said to him, 'I am the LORD.'",
      "M": "God also said to Moses, 'I am the LORD.'",
      "T": "God spoke to Moses and said, 'I am Yahweh—the LORD.'"
    },
    "3": {
      "L": "'I appeared to Abraham, to Isaac, and to Jacob, as God Almighty, but by my name the LORD I did not make myself known to them.'",
      "M": "'I appeared to Abraham, to Isaac and to Jacob as God Almighty, but by my name the LORD I did not make myself fully known to them.'",
      "T": "'I appeared to Abraham, Isaac, and Jacob as God Almighty—El Shaddai—but my personal name, Yahweh, I did not reveal to them in its full significance.'"
    },
    "4": {
      "L": "'I also established my covenant with them to give them the land of Canaan, the land in which they sojourned.'",
      "M": "'I also established my covenant with them to give them the land of Canaan, where they resided as foreigners.'",
      "T": "'I also made a covenant with them to give them the land of Canaan—the land where they had lived as aliens.'"
    },
    "5": {
      "L": "'Moreover, I have heard the groaning of the children of Israel whom the Egyptians keep in bondage, and I have remembered my covenant.'",
      "M": "'Moreover, I have heard the groaning of the Israelites, whom the Egyptians are enslaving, and I have remembered my covenant.'",
      "T": "'I have heard the Israelites groaning under Egypt's boot—and I have remembered my covenant.'"
    },
    "6": {
      "L": "'Say therefore to the children of Israel: I am the LORD, and I will bring you out from under the burdens of the Egyptians and I will rid you of their bondage, and I will redeem you with an outstretched arm and with great acts of judgment.'",
      "M": "'Therefore, say to the Israelites: \"I am the LORD, and I will bring you out from under the yoke of the Egyptians. I will free you from being slaves to them, and I will redeem you with an outstretched arm and with mighty acts of judgment.\"'",
      "T": "'So tell the Israelites: \"I am the LORD. I will bring you out from under Egypt's burdens. I will free you from their slavery. I will redeem you with an outstretched arm and mighty acts of judgment.\"'"
    },
    "7": {
      "L": "'I will take you as my own people and I will be your God. Then you will know that I am the LORD your God, who brought you out from under the burdens of the Egyptians.'",
      "M": "'I will take you as my own people, and I will be your God. Then you will know that I am the LORD your God, who brought you out from under the yoke of the Egyptians.'",
      "T": "'I will claim you as my people, and I will be your God. Then you will know that I—the LORD—am your God, the one who brought you out from under Egypt's burdens.'"
    },
    "8": {
      "L": "'And I will bring you into the land that I swore to give to Abraham, to Isaac, and to Jacob. I will give it to you as a possession. I am the LORD.'",
      "M": "'And I will bring you to the land I swore with uplifted hand to give to Abraham, to Isaac and to Jacob. I will give it to you as a possession. I am the LORD.'",
      "T": "'I will bring you into the land I promised with a raised hand to give to Abraham, Isaac, and Jacob. It will be your inheritance. I am the LORD.'"
    },
    "9": {
      "L": "Moses spoke thus to the children of Israel, but they did not listen to Moses, because of their broken spirit and their cruel bondage.",
      "M": "Moses reported this to the Israelites, but they did not listen to him because of their discouragement and harsh labor.",
      "T": "Moses told this to the Israelites, but they could not take it in. Their spirit was crushed, broken by years of brutal slavery."
    },
    "10": {
      "L": "Then the LORD spoke to Moses, saying,",
      "M": "Then the LORD said to Moses,",
      "T": "The LORD spoke to Moses:"
    },
    "11": {
      "L": "'Go in and tell Pharaoh king of Egypt to let the children of Israel go out of his land.'",
      "M": "'Go, tell Pharaoh king of Egypt to let the Israelites go out of his country.'",
      "T": "'Go! Tell Pharaoh king of Egypt to release the Israelites from his land.'"
    },
    "12": {
      "L": "But Moses spoke before the LORD, saying, 'Behold, the children of Israel have not listened to me. How then shall Pharaoh listen to me, for I am of uncircumcised lips?'",
      "M": "But Moses said to the LORD, 'If the Israelites will not listen to me, why would Pharaoh listen to me, since I speak with faltering lips?'",
      "T": "Moses appealed to the LORD: 'If the Israelites won't listen to me, why would Pharaoh? I'm no speaker—my lips are faltering.'"
    },
    "13": {
      "L": "But the LORD spoke to Moses and Aaron and gave them a charge concerning the children of Israel and concerning Pharaoh king of Egypt, to bring the children of Israel out of the land of Egypt.",
      "M": "The LORD spoke to Moses and Aaron about the Israelites and Pharaoh king of Egypt, and he commanded them to bring the Israelites out of Egypt.",
      "T": "But the LORD spoke to Moses and Aaron and commissioned them to bring the Israelites out of Egypt—dealing with both the Israelites and Pharaoh king of Egypt."
    },
    "14": {
      "L": "These are the heads of their fathers' houses: the sons of Reuben, the firstborn of Israel: Hanoch, Pallu, Hezron, and Carmi; these are the clans of Reuben.",
      "M": "These were the heads of their families: The sons of Reuben the firstborn son of Israel were Hanoch and Pallu, Hezron and Carmi. These were the clans of Reuben.",
      "T": "These are the heads of the ancestral houses. Reuben, Israel's firstborn, had four sons: Hanoch, Pallu, Hezron, and Carmi—these are the clans of Reuben."
    },
    "15": {
      "L": "The sons of Simeon: Jemuel, Jamin, Ohad, Jachin, Zohar, and Shaul, the son of a Canaanite woman; these are the clans of Simeon.",
      "M": "The sons of Simeon were Jemuel, Jamin, Ohad, Jachin, Zohar and Shaul the son of a Canaanite woman. These were the clans of Simeon.",
      "T": "Simeon's sons: Jemuel, Jamin, Ohad, Jachin, Zohar, and Shaul the son of a Canaanite woman—these are the clans of Simeon."
    },
    "16": {
      "L": "These are the names of the sons of Levi according to their generations: Gershon, Kohath, and Merari. The years of the life of Levi were 137.",
      "M": "These were the names of the sons of Levi according to their records: Gershon, Kohath and Merari. Levi lived 137 years.",
      "T": "The sons of Levi, in family sequence: Gershon, Kohath, and Merari. Levi lived 137 years."
    },
    "17": {
      "L": "The sons of Gershon: Libni and Shimei, according to their clans.",
      "M": "The sons of Gershon, by clans, were Libni and Shimei.",
      "T": "Gershon's sons: Libni and Shimei, according to their clans."
    },
    "18": {
      "L": "The sons of Kohath: Amram, Izhar, Hebron, and Uzziel. The years of the life of Kohath were 133.",
      "M": "The sons of Kohath were Amram, Izhar, Hebron and Uzziel. Kohath lived 133 years.",
      "T": "Kohath's sons: Amram, Izhar, Hebron, and Uzziel. Kohath lived 133 years."
    },
    "19": {
      "L": "The sons of Merari: Mahli and Mushi. These are the clans of Levi according to their generations.",
      "M": "The sons of Merari were Mahli and Mushi. These were the Levite clans according to their records.",
      "T": "Merari's sons: Mahli and Mushi. These are the clans of Levi in sequence of descent."
    },
    "20": {
      "L": "Amram took as his wife Jochebed his father's sister, and she bore him Aaron and Moses. The years of the life of Amram were 137.",
      "M": "Amram married his father's sister Jochebed, who bore him Aaron and Moses. Amram lived 137 years.",
      "T": "Amram married Jochebed, his father's sister. She bore him Aaron and Moses. Amram lived 137 years."
    },
    "21": {
      "L": "The sons of Izhar: Korah, Nepheg, and Zichri.",
      "M": "The sons of Izhar were Korah, Nepheg and Zichri.",
      "T": "Izhar's sons: Korah, Nepheg, and Zichri."
    },
    "22": {
      "L": "The sons of Uzziel: Mishael, Elzaphan, and Sithri.",
      "M": "The sons of Uzziel were Mishael, Elzaphan and Sithri.",
      "T": "Uzziel's sons: Mishael, Elzaphan, and Sithri."
    },
    "23": {
      "L": "Aaron took as his wife Elisheba, the daughter of Amminadab and the sister of Nahshon, and she bore him Nadab, Abihu, Eleazar, and Ithamar.",
      "M": "Aaron married Elisheba, daughter of Amminadab and sister of Nahshon, and she bore him Nadab and Abihu, Eleazar and Ithamar.",
      "T": "Aaron married Elisheba—daughter of Amminadab, sister of Nahshon—and she bore him Nadab, Abihu, Eleazar, and Ithamar."
    },
    "24": {
      "L": "The sons of Korah: Assir, Elkanah, and Abiasaph; these are the clans of the Korahites.",
      "M": "The sons of Korah were Assir, Elkanah and Abiasaph. These were the Korah clans.",
      "T": "Korah's sons: Assir, Elkanah, and Abiasaph—these are the clans of the Korahites."
    },
    "25": {
      "L": "Eleazar the son of Aaron took as his wife one of the daughters of Putiel, and she bore him Phinehas. These are the heads of the fathers' clans of the Levites according to their clans.",
      "M": "Eleazar son of Aaron married one of the daughters of Putiel, and she bore him Phinehas. These were the heads of the Levite families, clan by clan.",
      "T": "Aaron's son Eleazar married a daughter of Putiel, and she bore him Phinehas. These are the heads of the Levite ancestral clans."
    },
    "26": {
      "L": "These are the Aaron and Moses to whom the LORD said, 'Bring out the children of Israel from the land of Egypt by their hosts.'",
      "M": "It was this same Aaron and Moses to whom the LORD said, 'Bring the Israelites out of Egypt by their divisions.'",
      "T": "These were the Aaron and Moses to whom the LORD said, 'Bring the Israelites out of Egypt, division by division.'"
    },
    "27": {
      "L": "It was they who spoke to Pharaoh king of Egypt about bringing out the children of Israel from Egypt—this Moses and this Aaron.",
      "M": "They were the ones who spoke to Pharaoh king of Egypt about bringing the Israelites out of Egypt—this same Moses and Aaron.",
      "T": "They were the ones who confronted Pharaoh king of Egypt and demanded the release of the Israelites—this same Moses and Aaron."
    },
    "28": {
      "L": "On the day the LORD spoke to Moses in the land of Egypt,",
      "M": "On the day the LORD spoke to Moses in Egypt,",
      "T": "On the day the LORD spoke to Moses in the land of Egypt,"
    },
    "29": {
      "L": "the LORD said to Moses, 'I am the LORD; tell Pharaoh king of Egypt everything that I tell you.'",
      "M": "he said to him, 'I am the LORD. Tell Pharaoh king of Egypt everything I tell you.'",
      "T": "the LORD said to Moses, 'I am the LORD. Speak to Pharaoh king of Egypt everything I say to you.'"
    },
    "30": {
      "L": "But Moses said before the LORD, 'Behold, I am of uncircumcised lips. How will Pharaoh listen to me?'",
      "M": "But Moses said to the LORD, 'Since I speak with faltering lips, why would Pharaoh listen to me?'",
      "T": "But Moses said to the LORD, 'My lips are faltering and inarticulate—how will Pharaoh take me seriously?'"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'exodus')
        merge_tier(existing, EXODUS, tier_key)
        save(tier_dir, 'exodus', existing)
    print('Exodus 1–6 written.')

if __name__ == '__main__':
    main()
