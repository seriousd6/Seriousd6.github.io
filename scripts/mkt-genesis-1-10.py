"""
MKT Genesis chapters 1-10 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-genesis-1-10.py
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

GENESIS = {
  "1": {
    "1": {
      "L": "In the beginning God created the heavens and the earth.",
      "M": "In the beginning God created the heavens and the earth.",
      "T": "In the beginning, God created everything—the heavens and the earth."
    },
    "2": {
      "L": "And the earth was formless and void, and darkness was over the face of the deep, and the Spirit of God was hovering over the face of the waters.",
      "M": "Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.",
      "T": "The earth was a shapeless, empty void. Darkness covered the face of the primordial deep, while the Spirit of God brooded over the surface of the waters."
    },
    "3": {
      "L": "And God said, 'Let there be light,' and there was light.",
      "M": "And God said, 'Let there be light,' and there was light.",
      "T": "God spoke: 'Let there be light'—and light came into being."
    },
    "4": {
      "L": "And God saw the light, that it was good, and God separated the light from the darkness.",
      "M": "God saw that the light was good, and he separated the light from the darkness.",
      "T": "God looked at the light and saw that it was good. Then he separated the light from the darkness."
    },
    "5": {
      "L": "And God called the light Day, and the darkness he called Night. And there was evening, and there was morning—the first day.",
      "M": "God called the light 'Day,' and the darkness he called 'Night.' And there was evening, and there was morning—the first day.",
      "T": "God named the light 'Day' and the darkness 'Night.' Evening came and morning followed—the first day."
    },
    "6": {
      "L": "And God said, 'Let there be an expanse in the midst of the waters, and let it separate the waters from the waters.'",
      "M": "And God said, 'Let there be an expanse between the waters to separate water from water.'",
      "T": "Then God said, 'Let there be a vast expanse cutting through the waters, dividing the waters above from the waters below.'"
    },
    "7": {
      "L": "And God made the expanse and separated the waters that were under the expanse from the waters that were above the expanse. And it was so.",
      "M": "So God made the expanse and separated the water under the expanse from the water above it. And it was so.",
      "T": "God made this expanse and divided the water beneath it from the water above it. And that is exactly what happened."
    },
    "8": {
      "L": "And God called the expanse Heaven. And there was evening, and there was morning—the second day.",
      "M": "God called the expanse 'Sky.' And there was evening, and there was morning—the second day.",
      "T": "God named the expanse 'Sky.' Evening came and morning followed—the second day."
    },
    "9": {
      "L": "And God said, 'Let the waters under the heavens be gathered together into one place, and let the dry land appear.' And it was so.",
      "M": "And God said, 'Let the water under the sky be gathered to one place, and let dry ground appear.' And it was so.",
      "T": "Then God said, 'Let all the water under the sky gather into one place, so that the dry ground can appear.' And it happened."
    },
    "10": {
      "L": "And God called the dry land Earth, and the gathering of the waters he called Seas. And God saw that it was good.",
      "M": "God called the dry ground 'Land,' and the gathered waters he called 'Seas.' And God saw that it was good.",
      "T": "God named the dry ground 'Land' and the gathered waters 'Seas.' God looked at it and saw that it was good."
    },
    "11": {
      "L": "And God said, 'Let the earth sprout vegetation, plants yielding seed, and fruit trees bearing fruit after their kind with seed in them, upon the earth.' And it was so.",
      "M": "Then God said, 'Let the land produce vegetation: seed-bearing plants and trees on the land that bear fruit with seed in it, according to their various kinds.' And it was so.",
      "T": "God said, 'Let the land burst forth with plant life—seed-bearing plants and fruit trees, each producing according to its own kind, with seed in the fruit.' And it happened."
    },
    "12": {
      "L": "And the earth brought forth vegetation, plants yielding seed after their kind, and trees bearing fruit with seed in them after their kind. And God saw that it was good.",
      "M": "The land produced vegetation: plants bearing seed according to their kinds and trees bearing fruit with seed in it according to their kinds. And God saw that it was good.",
      "T": "The land produced plant life: seed-bearing plants and fruit trees, each reproducing according to its own kind. God saw that it was good."
    },
    "13": {
      "L": "And there was evening, and there was morning—the third day.",
      "M": "And there was evening, and there was morning—the third day.",
      "T": "Evening came and morning followed—the third day."
    },
    "14": {
      "L": "And God said, 'Let there be lights in the expanse of the heavens to separate the day from the night, and let them be for signs and for appointed times, and for days and years,'",
      "M": "And God said, 'Let there be lights in the expanse of the sky to separate the day from the night, and let them serve as signs to mark sacred times, and days and years,'",
      "T": "Then God said, 'Let there be lights in the expanse of the sky to separate day from night. Let them mark the seasons, sacred festivals, days, and years,'"
    },
    "15": {
      "L": "'and let them be for lights in the expanse of the heavens to give light upon the earth.' And it was so.",
      "M": "'and let them be lights in the expanse of the sky to give light on the earth.' And it was so.",
      "T": "'and let them shine down on the earth.' And it happened."
    },
    "16": {
      "L": "And God made the two great lights—the greater light to rule the day and the lesser light to rule the night—and the stars.",
      "M": "God made two great lights—the greater light to govern the day and the lesser light to govern the night. He also made the stars.",
      "T": "God made the two great lights—the larger one to govern the day and the smaller one to govern the night. He made the stars as well."
    },
    "17": {
      "L": "And God set them in the expanse of the heavens to give light upon the earth,",
      "M": "God set them in the expanse of the sky to give light on the earth,",
      "T": "God placed them in the expanse of the sky to shine on the earth,"
    },
    "18": {
      "L": "and to rule over the day and over the night, and to separate the light from the darkness. And God saw that it was good.",
      "M": "to govern the day and the night, and to separate light from darkness. And God saw that it was good.",
      "T": "to govern the day and the night and to divide light from darkness. God saw that it was good."
    },
    "19": {
      "L": "And there was evening, and there was morning—the fourth day.",
      "M": "And there was evening, and there was morning—the fourth day.",
      "T": "Evening came and morning followed—the fourth day."
    },
    "20": {
      "L": "And God said, 'Let the waters swarm with swarms of living creatures, and let birds fly above the earth across the expanse of the heavens.'",
      "M": "And God said, 'Let the water teem with living creatures, and let birds fly above the earth across the expanse of the sky.'",
      "T": "Then God said, 'Let the waters teem with living creatures, and let birds soar above the earth through the open expanse of the sky.'"
    },
    "21": {
      "L": "So God created the great sea creatures and every living creature that moves, with which the waters swarm, after their kind, and every winged bird after its kind. And God saw that it was good.",
      "M": "So God created the great creatures of the sea and every living thing with which the water teems and that moves about in it, according to their kinds, and every winged bird according to its kind. And God saw that it was good.",
      "T": "So God created the massive sea creatures and every kind of living thing that fills the waters, and every kind of winged bird. God saw that it was good."
    },
    "22": {
      "L": "And God blessed them, saying, 'Be fruitful and multiply and fill the waters in the seas, and let birds multiply on the earth.'",
      "M": "God blessed them and said, 'Be fruitful and increase in number and fill the water in the seas, and let the birds increase on the earth.'",
      "T": "God blessed them all and said, 'Multiply and fill the seas, and let the birds multiply across the earth.'"
    },
    "23": {
      "L": "And there was evening, and there was morning—the fifth day.",
      "M": "And there was evening, and there was morning—the fifth day.",
      "T": "Evening came and morning followed—the fifth day."
    },
    "24": {
      "L": "And God said, 'Let the earth bring forth living creatures after their kind—livestock and creeping things and beasts of the earth after their kind.' And it was so.",
      "M": "And God said, 'Let the land produce living creatures according to their kinds: the livestock, the creatures that move along the ground, and the wild animals, each according to its kind.' And it was so.",
      "T": "Then God said, 'Let the land produce living creatures of every kind—livestock, creatures that crawl, and wild animals.' And it happened."
    },
    "25": {
      "L": "And God made the beasts of the earth after their kind, and the livestock after their kind, and everything that creeps upon the ground after its kind. And God saw that it was good.",
      "M": "God made the wild animals according to their kinds, the livestock according to their kinds, and all the creatures that move along the ground according to their kinds. And God saw that it was good.",
      "T": "God made wild animals, livestock, and every creature that crawls—each according to its kind. God saw that it was good."
    },
    "26": {
      "L": "Then God said, 'Let us make man in our image, according to our likeness, and let them have dominion over the fish of the sea and over the birds of the heavens and over the livestock and over all the earth and over every creeping thing that creeps on the earth.'",
      "M": "Then God said, 'Let us make mankind in our image, in our likeness, so that they may rule over the fish in the sea and the birds in the sky, over the livestock and all the wild animals, and over all the creatures that move along the ground.'",
      "T": "Then God said, 'Let us make human beings in our own image, to reflect our likeness—and let them govern the fish of the sea, the birds of the sky, the livestock, the whole earth, and every creature that moves on the ground.'"
    },
    "27": {
      "L": "So God created the man in his own image,\nin the image of God he created him;\nmale and female he created them.",
      "M": "So God created mankind in his own image,\nin the image of God he created them;\nmale and female he created them.",
      "T": "So God created human beings in his own image—\nmade to reflect God's own likeness.\nHe created them male and female."
    },
    "28": {
      "L": "And God blessed them. And God said to them, 'Be fruitful and multiply and fill the earth and subdue it, and have dominion over the fish of the sea and over the birds of the heavens and over every living thing that moves on the earth.'",
      "M": "God blessed them and said to them, 'Be fruitful and increase in number; fill the earth and subdue it. Rule over the fish in the sea and the birds in the sky and over every living creature that moves on the ground.'",
      "T": "God blessed them and said, 'Have many children and fill the earth. Govern it—rule over the fish of the sea, the birds of the sky, and every living creature on the ground.'"
    },
    "29": {
      "L": "And God said, 'Behold, I have given you every plant yielding seed that is on the face of all the earth, and every tree with seed in its fruit. They shall be yours for food.'",
      "M": "Then God said, 'I give you every seed-bearing plant on the face of the whole earth and every tree that has fruit with seed in it. They will be yours for food.'",
      "T": "God said, 'Look—I have given you every seed-bearing plant on the earth and every fruit tree. These are yours to eat.'"
    },
    "30": {
      "L": "'And to every beast of the earth and to every bird of the heavens and to everything that creeps on the earth, everything that has the breath of life, I have given every green plant for food.' And it was so.",
      "M": "'And to all the beasts of the earth and all the birds in the sky and all the creatures that move along the ground—everything that has the breath of life in it—I give every green plant for food.' And it was so.",
      "T": "'And to all the wild animals, all the birds, and everything that crawls on the ground—every living, breathing creature—I give every green plant for food.' And it happened."
    },
    "31": {
      "L": "And God saw all that he had made, and behold, it was very good. And there was evening, and there was morning—the sixth day.",
      "M": "God saw all that he had made, and it was very good. And there was evening, and there was morning—the sixth day.",
      "T": "God looked over everything he had made, and it was all very good indeed. Evening came and morning followed—the sixth day."
    }
  },
  "2": {
    "1": {
      "L": "Thus the heavens and the earth were finished, and all their host.",
      "M": "Thus the heavens and the earth were completed in all their vast array.",
      "T": "So the heavens and the earth and everything in them were completed."
    },
    "2": {
      "L": "And on the seventh day God finished his work that he had done, and he rested on the seventh day from all his work that he had done.",
      "M": "By the seventh day God had finished the work he had been doing; so on the seventh day he rested from all his work.",
      "T": "By the seventh day God had completed all his work. On the seventh day he ceased from all the work he had been doing."
    },
    "3": {
      "L": "So God blessed the seventh day and made it holy, because on it God rested from all his work that he had done in creation.",
      "M": "Then God blessed the seventh day and made it holy, because on it he rested from all the work of creating that he had done.",
      "T": "God blessed the seventh day and set it apart as holy, because on that day he rested from all the work of creation."
    },
    "4": {
      "L": "These are the generations of the heavens and the earth when they were created, in the day that the LORD God made the earth and the heavens.",
      "M": "This is the account of the heavens and the earth when they were created, when the LORD God made the earth and the heavens.",
      "T": "This is the story of the heavens and the earth when they were created. When the LORD God made the earth and the sky,"
    },
    "5": {
      "L": "when no bush of the field was yet in the land and no small plant of the field had yet sprung up—for the LORD God had not yet caused it to rain upon the earth, and there was no man to work the ground,",
      "M": "and no shrub had yet appeared on the earth and no plant had yet sprung up, for the LORD God had not sent rain on the earth and there was no one to work the ground,",
      "T": "no shrub had yet grown in the open country and no grain had yet sprouted, for the LORD God had not yet sent rain, and there was no one to tend the soil."
    },
    "6": {
      "L": "but a mist was going up from the land and was watering the whole face of the ground—",
      "M": "but streams came up from the earth and watered the whole surface of the ground.",
      "T": "Instead, underground springs welled up and watered the entire surface of the ground."
    },
    "7": {
      "L": "then the LORD God formed the man of dust from the ground and breathed into his nostrils the breath of life, and the man became a living soul.",
      "M": "Then the LORD God formed a man from the dust of the ground and breathed into his nostrils the breath of life, and the man became a living being.",
      "T": "The LORD God shaped the man from the dust of the ground, breathed the breath of life into his nostrils, and the man came alive as a living, breathing person."
    },
    "8": {
      "L": "And the LORD God planted a garden in Eden, in the east, and there he put the man whom he had formed.",
      "M": "Now the LORD God had planted a garden in the east, in Eden; and there he put the man he had formed.",
      "T": "The LORD God planted a garden in Eden, in the east, and placed there the man he had formed."
    },
    "9": {
      "L": "And out of the ground the LORD God made to spring up every tree that is pleasant to the sight and good for food. The tree of life was in the midst of the garden, and the tree of the knowledge of good and evil.",
      "M": "The LORD God made all kinds of trees grow out of the ground—trees that were pleasing to the eye and good for food. In the middle of the garden were the tree of life and the tree of the knowledge of good and evil.",
      "T": "The LORD God caused every kind of beautiful, fruit-bearing tree to grow from the ground. In the center of the garden stood the tree of life and the tree of the knowledge of good and evil."
    },
    "10": {
      "L": "A river flowed out of Eden to water the garden, and there it divided and became four rivers.",
      "M": "A river watering the garden flowed from Eden; from there it was separated into four headwaters.",
      "T": "A river flowed out of Eden to water the garden, and downstream it split into four branches."
    },
    "11": {
      "L": "The name of the first is Pishon. It is the one that flows around the whole land of Havilah, where there is gold.",
      "M": "The name of the first is the Pishon; it winds through the entire land of Havilah, where there is gold.",
      "T": "The first river is the Pishon, which flows through the whole land of Havilah, where gold is found."
    },
    "12": {
      "L": "And the gold of that land is good; bdellium and onyx stone are there.",
      "M": "The gold of that land is good; aromatic resin and onyx are also there.",
      "T": "The gold of that land is fine quality; bdellium resin and onyx stone are found there too."
    },
    "13": {
      "L": "The name of the second river is Gihon. It is the one that flows around the whole land of Cush.",
      "M": "The name of the second river is the Gihon; it winds through the entire land of Cush.",
      "T": "The second river is the Gihon, which flows through the whole land of Cush."
    },
    "14": {
      "L": "And the name of the third river is Tigris, which flows east of Assyria. And the fourth river is the Euphrates.",
      "M": "The name of the third river is the Tigris; it runs along the east side of Ashur. And the fourth river is the Euphrates.",
      "T": "The third river is the Tigris, which runs east of Assyria. And the fourth river is the Euphrates."
    },
    "15": {
      "L": "The LORD God took the man and put him in the garden of Eden to work it and keep it.",
      "M": "The LORD God took the man and put him in the Garden of Eden to work it and take care of it.",
      "T": "The LORD God placed the man in the Garden of Eden to cultivate it and watch over it."
    },
    "16": {
      "L": "And the LORD God commanded the man, saying, 'You may surely eat of every tree of the garden,'",
      "M": "And the LORD God commanded the man, 'You are free to eat from any tree in the garden;'",
      "T": "The LORD God gave the man this command: 'You may freely eat the fruit of every tree in the garden,'"
    },
    "17": {
      "L": "'but of the tree of the knowledge of good and evil you shall not eat, for in the day that you eat of it you shall surely die.'",
      "M": "'but you must not eat from the tree of the knowledge of good and evil, for when you eat from it you will certainly die.'",
      "T": "'but you must never eat from the tree of the knowledge of good and evil. The moment you eat from it, you will certainly die.'"
    },
    "18": {
      "L": "Then the LORD God said, 'It is not good that the man should be alone; I will make him a helper fit for him.'",
      "M": "The LORD God said, 'It is not good for the man to be alone. I will make a helper suitable for him.'",
      "T": "Then the LORD God said, 'It is not good for the man to be by himself. I will make a partner who is right for him.'"
    },
    "19": {
      "L": "Now out of the ground the LORD God had formed every beast of the field and every bird of the heavens and brought them to the man to see what he would call them. And whatever the man called every living creature, that was its name.",
      "M": "Now the LORD God had formed out of the ground all the wild animals and all the birds in the sky. He brought them to the man to see what he would name them; and whatever the man called each living creature, that was its name.",
      "T": "The LORD God had formed all the wild animals and birds from the ground, and now he brought them to the man to see what he would call them. Whatever the man named each living creature, that became its name."
    },
    "20": {
      "L": "The man gave names to all livestock and to the birds of the heavens and to every beast of the field. But for Adam there was not found a helper fit for him.",
      "M": "So the man gave names to all the livestock, the birds in the sky and all the wild animals. But for Adam no suitable helper was found.",
      "T": "The man named every livestock animal, every bird, and every wild creature. But none of them was a suitable partner for him."
    },
    "21": {
      "L": "So the LORD God caused a deep sleep to fall upon the man, and while he slept took one of his ribs and closed up its place with flesh.",
      "M": "So the LORD God caused the man to fall into a deep sleep; and while he was sleeping, he took one of the man's ribs and then closed up the place with flesh.",
      "T": "So the LORD God caused a deep sleep to fall on the man. While the man slept, God took one of his ribs and closed up the opening."
    },
    "22": {
      "L": "And the rib that the LORD God had taken from the man he made into a woman and brought her to the man.",
      "M": "Then the LORD God made a woman from the rib he had taken out of the man, and he brought her to the man.",
      "T": "The LORD God shaped the rib he had taken from the man into a woman, and brought her to him."
    },
    "23": {
      "L": "Then the man said,\n'This at last is bone of my bones\nand flesh of my flesh;\nshe shall be called Woman,\nbecause she was taken out of Man.'",
      "M": "The man said,\n'This is now bone of my bones\nand flesh of my flesh;\nshe shall be called Woman,\nfor she was taken out of man.'",
      "T": "The man burst out:\n'At last—this one is bone from my bones\nand flesh from my flesh!\nShe will be called Woman,\nbecause she was taken from man.'"
    },
    "24": {
      "L": "Therefore a man shall leave his father and his mother and hold fast to his wife, and they shall become one flesh.",
      "M": "That is why a man leaves his father and mother and is united to his wife, and they become one flesh.",
      "T": "This is why a man leaves his father and mother and clings to his wife—the two of them becoming one."
    },
    "25": {
      "L": "And the man and his wife were both naked and were not ashamed.",
      "M": "Adam and his wife were both naked, and they felt no shame.",
      "T": "The man and his wife were both naked, and they felt no shame whatsoever."
    }
  },
  "3": {
    "1": {
      "L": "Now the serpent was more crafty than any other beast of the field that the LORD God had made. He said to the woman, 'Did God actually say, \"You shall not eat of any tree in the garden\"?'",
      "M": "Now the serpent was more crafty than any of the wild animals the LORD God had made. He said to the woman, 'Did God really say, \"You must not eat from any tree in the garden\"?'",
      "T": "Now the serpent was more cunning than any wild creature the LORD God had made. He said to the woman, 'Did God really say you must not eat from any tree in the garden?'"
    },
    "2": {
      "L": "And the woman said to the serpent, 'We may eat of the fruit of the trees in the garden,'",
      "M": "The woman said to the serpent, 'We may eat fruit from the trees in the garden,'",
      "T": "The woman answered, 'We can eat from the trees in the garden.'"
    },
    "3": {
      "L": "'but God said, \"You shall not eat of the fruit of the tree that is in the midst of the garden, neither shall you touch it, lest you die.\"'",
      "M": "'but God did say, \"You must not eat fruit from the tree that is in the middle of the garden, and you must not touch it, or you will die.\"'",
      "T": "'But God said we must not eat from the tree in the center of the garden—he even said we must not touch it, or we will die.'"
    },
    "4": {
      "L": "But the serpent said to the woman, 'You will not surely die.'",
      "M": "'You will not certainly die,' the serpent said to the woman.",
      "T": "The serpent said, 'You won't die at all!'"
    },
    "5": {
      "L": "'For God knows that when you eat of it your eyes will be opened, and you will be like God, knowing good and evil.'",
      "M": "'For God knows that when you eat from it your eyes will be opened, and you will be like God, knowing good and evil.'",
      "T": "'God knows that the moment you eat it your eyes will be opened and you will be like God—knowing good and evil for yourself.'"
    },
    "6": {
      "L": "So when the woman saw that the tree was good for food, and that it was a delight to the eyes, and that the tree was to be desired to make one wise, she took of its fruit and ate, and she also gave some to her husband who was with her, and he ate.",
      "M": "When the woman saw that the fruit of the tree was good for food and pleasing to the eye, and also desirable for gaining wisdom, she took some and ate it. She also gave some to her husband, who was with her, and he ate it.",
      "T": "The woman saw that the tree's fruit looked delicious, was beautiful to the eye, and would make her wise. So she took some and ate it. She gave some to her husband, who was right there with her, and he ate it too."
    },
    "7": {
      "L": "Then the eyes of both were opened, and they knew that they were naked. And they sewed fig leaves together and made themselves loincloths.",
      "M": "Then the eyes of both of them were opened, and they realized they were naked; so they sewed fig leaves together and made coverings for themselves.",
      "T": "Immediately their eyes were opened, and they realized they were naked. They sewed fig leaves together and made coverings for themselves."
    },
    "8": {
      "L": "And they heard the sound of the LORD God walking in the garden in the cool of the day, and the man and his wife hid themselves from the presence of the LORD God among the trees of the garden.",
      "M": "Then the man and his wife heard the sound of the LORD God as he was walking in the garden in the cool of the day, and they hid from the LORD God among the trees of the garden.",
      "T": "Then they heard the sound of the LORD God walking through the garden in the evening breeze, and the man and his wife hid among the trees to avoid him."
    },
    "9": {
      "L": "But the LORD God called to the man and said to him, 'Where are you?'",
      "M": "But the LORD God called to the man, 'Where are you?'",
      "T": "But the LORD God called out to the man: 'Where are you?'"
    },
    "10": {
      "L": "And he said, 'I heard the sound of you in the garden, and I was afraid, because I was naked, and I hid myself.'",
      "M": "He answered, 'I heard you in the garden, and I was afraid because I was naked; so I hid.'",
      "T": "The man replied, 'I heard you coming and I was afraid, because I was naked—so I hid.'"
    },
    "11": {
      "L": "He said, 'Who told you that you were naked? Have you eaten of the tree of which I commanded you not to eat?'",
      "M": "And he said, 'Who told you that you were naked? Have you eaten from the tree that I commanded you not to eat from?'",
      "T": "God asked, 'Who told you that you were naked? Did you eat from the tree I commanded you not to eat from?'"
    },
    "12": {
      "L": "The man said, 'The woman whom you gave to be with me, she gave me fruit of the tree, and I ate.'",
      "M": "The man said, 'The woman you put here with me—she gave me some fruit from the tree, and I ate it.'",
      "T": "The man said, 'The woman you gave me—she gave me fruit from the tree, and I ate it.'"
    },
    "13": {
      "L": "Then the LORD God said to the woman, 'What is this you have done?' The woman said, 'The serpent deceived me, and I ate.'",
      "M": "Then the LORD God said to the woman, 'What is this you have done?' The woman said, 'The serpent deceived me, and I ate.'",
      "T": "The LORD God asked the woman, 'What have you done?' She said, 'The serpent tricked me, and I ate.'"
    },
    "14": {
      "L": "The LORD God said to the serpent, 'Because you have done this, cursed are you above all livestock and above all beasts of the field; on your belly you shall go, and dust you shall eat all the days of your life.'",
      "M": "So the LORD God said to the serpent, 'Because you have done this, cursed are you above all livestock and all wild animals! You will crawl on your belly and you will eat dust all the days of your life.'",
      "T": "So the LORD God said to the serpent, 'Because you did this, you are cursed above every animal, wild or domestic. You will crawl on your belly and eat dust for the rest of your life.'"
    },
    "15": {
      "L": "'And I will put enmity between you and the woman, and between your seed and her seed; he will crush your head, and you will strike his heel.'",
      "M": "'And I will put enmity between you and the woman, and between your offspring and hers; he will crush your head, and you will strike his heel.'",
      "T": "'I will make you and the woman enemies of each other, and your offspring and hers will be enemies too. Her offspring will crush your head, even as you strike at his heel.'"
    },
    "16": {
      "L": "To the woman he said, 'I will surely multiply your pain in childbearing; in pain you shall bring forth children. Your desire shall be for your husband, and he shall rule over you.'",
      "M": "To the woman he said, 'I will make your pains in childbearing very severe; with painful labor you will give birth to children. Your desire will be for your husband, and he will rule over you.'",
      "T": "To the woman God said, 'I will greatly increase your pain in childbirth. You will give birth to children in agony. You will long for your husband, and he will dominate you.'"
    },
    "17": {
      "L": "And to Adam he said, 'Because you have listened to the voice of your wife and have eaten of the tree of which I commanded you, \"You shall not eat of it,\" cursed is the ground because of you; in pain you shall eat of it all the days of your life;'",
      "M": "To Adam he said, 'Because you listened to your wife and ate fruit from the tree about which I commanded you, \"You must not eat from it,\" cursed is the ground because of you; through painful toil you will eat food from it all the days of your life.'",
      "T": "To the man God said, 'Because you listened to your wife and ate from the tree I forbade you, the ground is now cursed on your account. You will have to struggle and toil to get food from it for the rest of your life.'"
    },
    "18": {
      "L": "'thorns and thistles it shall bring forth for you; and you shall eat the plants of the field.'",
      "M": "'It will produce thorns and thistles for you, and you will eat the plants of the field.'",
      "T": "'It will sprout thorns and thistles, and you will eat wild plants.'"
    },
    "19": {
      "L": "'By the sweat of your face you shall eat bread, till you return to the ground, for out of it you were taken; for you are dust, and to dust you shall return.'",
      "M": "'By the sweat of your brow you will eat your food until you return to the ground, since from it you were taken; for dust you are and to dust you will return.'",
      "T": "'You will earn your food by the sweat of your face, until you return to the ground—because you were taken from it. You are dust, and to dust you will return.'"
    },
    "20": {
      "L": "The man called his wife's name Eve, because she was the mother of all living.",
      "M": "Adam named his wife Eve, because she would become the mother of all the living.",
      "T": "The man named his wife Eve, because she would be the mother of every living human being."
    },
    "21": {
      "L": "And the LORD God made for Adam and for his wife garments of skins and clothed them.",
      "M": "The LORD God made garments of skin for Adam and his wife and clothed them.",
      "T": "The LORD God made garments from animal skins for the man and his wife, and he clothed them."
    },
    "22": {
      "L": "Then the LORD God said, 'Behold, the man has become like one of us in knowing good and evil. Now, lest he reach out his hand and take also of the tree of life and eat, and live forever—'",
      "M": "And the LORD God said, 'The man has now become like one of us, knowing good and evil. He must not be allowed to reach out his hand and take also from the tree of life and eat, and live forever.'",
      "T": "The LORD God said, 'Now the man has become like one of us, knowing good and evil. We must not let him reach out and eat from the tree of life and live forever.'"
    },
    "23": {
      "L": "therefore the LORD God sent him out from the garden of Eden to work the ground from which he was taken.",
      "M": "So the LORD God banished him from the Garden of Eden to work the ground from which he had been taken.",
      "T": "So the LORD God expelled the man from the Garden of Eden to work the ground he had been made from."
    },
    "24": {
      "L": "He drove out the man, and at the east of the garden of Eden he placed the cherubim and a flaming sword that turned every way to guard the way to the tree of life.",
      "M": "After he drove the man out, he placed on the east side of the Garden of Eden cherubim and a flaming sword flashing back and forth to guard the way to the tree of life.",
      "T": "He drove the man out and stationed mighty cherubim at the east entrance of the garden, along with a flaming sword that flashed in every direction, to guard the way to the tree of life."
    }
  },
  "4": {
    "1": {
      "L": "Now the man knew Eve his wife, and she conceived and bore Cain, saying, 'I have gotten a man with the help of the LORD.'",
      "M": "Adam made love to his wife Eve, and she became pregnant and gave birth to Cain. She said, 'With the help of the LORD I have brought forth a man.'",
      "T": "The man was intimate with his wife Eve, and she conceived and gave birth to Cain. She said, 'I have given birth to a man with the LORD's help.'"
    },
    "2": {
      "L": "And again, she bore his brother Abel. Now Abel was a keeper of sheep, and Cain was a worker of the ground.",
      "M": "Later she gave birth to his brother Abel. Now Abel kept flocks, and Cain worked the soil.",
      "T": "Later she gave birth to his brother Abel. Abel became a shepherd, while Cain worked the ground."
    },
    "3": {
      "L": "In the course of time Cain brought to the LORD an offering of the fruit of the ground,",
      "M": "In the course of time Cain brought some of the fruits of the soil as an offering to the LORD.",
      "T": "When the time came, Cain brought some of the produce of the ground as an offering to the LORD."
    },
    "4": {
      "L": "and Abel also brought of the firstborn of his flock and of their fat portions. And the LORD had regard for Abel and his offering,",
      "M": "And Abel also brought an offering—fat portions from some of the firstborn of his flock. The LORD looked with favor on Abel and his offering,",
      "T": "Abel brought the best portions—the fat and the firstborn—from his flock. The LORD accepted Abel and his offering,"
    },
    "5": {
      "L": "but for Cain and his offering he had no regard. So Cain was very angry, and his face fell.",
      "M": "but on Cain and his offering he did not look with favor. So Cain was very angry, and his face was downcast.",
      "T": "but he did not accept Cain or his offering. Cain became furious, and his face fell."
    },
    "6": {
      "L": "The LORD said to Cain, 'Why are you angry, and why has your face fallen?'",
      "M": "Then the LORD said to Cain, 'Why are you angry? Why is your face downcast?'",
      "T": "The LORD said to Cain, 'Why are you so angry? Why do you look so dejected?'"
    },
    "7": {
      "L": "'If you do well, will you not be accepted? And if you do not do well, sin is crouching at the door. Its desire is for you, but you must rule over it.'",
      "M": "'If you do what is right, will you not be accepted? But if you do not do what is right, sin is crouching at your door; it desires to have you, but you must rule over it.'",
      "T": "'If you do what is right, won't you be accepted? But if you refuse to do right, sin is crouching at your door, ready to pounce. It wants to control you—but you must master it.'"
    },
    "8": {
      "L": "Cain spoke to Abel his brother. And when they were in the field, Cain rose up against his brother Abel and killed him.",
      "M": "Now Cain said to his brother Abel, 'Let's go out to the field.' While they were in the field, Cain attacked his brother Abel and killed him.",
      "T": "One day Cain said to his brother Abel, 'Let's go out to the field.' When they were in the field, Cain attacked his brother and killed him."
    },
    "9": {
      "L": "Then the LORD said to Cain, 'Where is Abel your brother?' He said, 'I do not know; am I my brother's keeper?'",
      "M": "Then the LORD said to Cain, 'Where is your brother Abel?' 'I don't know,' he replied. 'Am I my brother's keeper?'",
      "T": "The LORD asked Cain, 'Where is your brother Abel?' Cain said, 'I don't know. Am I supposed to watch out for my brother?'"
    },
    "10": {
      "L": "And the LORD said, 'What have you done? The voice of your brother's blood is crying to me from the ground.'",
      "M": "The LORD said, 'What have you done? Listen! Your brother's blood cries out to me from the ground.'",
      "T": "The LORD said, 'What have you done? Your brother's blood is crying out to me from the ground!'"
    },
    "11": {
      "L": "'And now you are cursed from the ground, which has opened its mouth to receive your brother's blood from your hand.'",
      "M": "'Now you are under a curse and driven from the ground, which opened its mouth to receive your brother's blood from your hand.'",
      "T": "'Now you are cursed, cut off from the ground that drank your brother's blood from your hand.'"
    },
    "12": {
      "L": "'When you work the ground, it shall no longer yield to you its strength. You shall be a fugitive and a wanderer on the earth.'",
      "M": "'When you work the ground, it will no longer yield its crops for you. You will be a restless wanderer on the earth.'",
      "T": "'When you try to farm the ground, it will refuse to produce for you. You will be a homeless wanderer on the earth.'"
    },
    "13": {
      "L": "Cain said to the LORD, 'My punishment is greater than I can bear.'",
      "M": "Cain said to the LORD, 'My punishment is more than I can bear.'",
      "T": "Cain said to the LORD, 'My punishment is too great for me to endure.'"
    },
    "14": {
      "L": "'Behold, you have driven me today away from the face of the ground, and from your face I shall be hidden. I shall be a fugitive and a wanderer on the earth, and whoever finds me will kill me.'",
      "M": "'Today you are driving me from the land, and I will be hidden from your presence; I will be a restless wanderer on the earth, and whoever finds me will kill me.'",
      "T": "'You are banishing me from the land today, and I will be cut off from your presence. I will be a homeless wanderer, and anyone who finds me will kill me.'"
    },
    "15": {
      "L": "Then the LORD said to him, 'Not so! If anyone kills Cain, vengeance shall be taken on him sevenfold.' And the LORD put a mark on Cain, lest any who found him should attack him.",
      "M": "But the LORD said to him, 'Not so; anyone who kills Cain will suffer vengeance seven times over.' Then the LORD put a mark on Cain so that no one who found him would kill him.",
      "T": "But the LORD said to him, 'No—if anyone kills you, they will suffer sevenfold vengeance.' Then the LORD put a mark on Cain so that no one who found him would kill him."
    },
    "16": {
      "L": "Then Cain went away from the presence of the LORD and settled in the land of Nod, east of Eden.",
      "M": "So Cain went out from the LORD's presence and lived in the land of Nod, east of Eden.",
      "T": "Cain left the presence of the LORD and settled in the land of Nod, east of Eden."
    },
    "17": {
      "L": "Cain knew his wife, and she conceived and bore Enoch. When he built a city, he called the name of the city after the name of his son, Enoch.",
      "M": "Cain made love to his wife, and she became pregnant and gave birth to Enoch. Cain was then building a city, and he named it after his son Enoch.",
      "T": "Cain was intimate with his wife, and she conceived and bore Enoch. Cain built a city and named it after his son Enoch."
    },
    "18": {
      "L": "To Enoch was born Irad, and Irad fathered Mehujael, and Mehujael fathered Methushael, and Methushael fathered Lamech.",
      "M": "To Enoch was born Irad, and Irad was the father of Mehujael, and Mehujael was the father of Methushael, and Methushael was the father of Lamech.",
      "T": "Enoch had a son named Irad, who fathered Mehujael, who fathered Methushael, who fathered Lamech."
    },
    "19": {
      "L": "And Lamech took two wives. The name of the one was Adah, and the name of the other Zillah.",
      "M": "Lamech married two women, one named Adah and the other Zillah.",
      "T": "Lamech married two women: Adah and Zillah."
    },
    "20": {
      "L": "Adah bore Jabal; he was the father of those who dwell in tents and have livestock.",
      "M": "Adah gave birth to Jabal; he was the father of those who live in tents and raise livestock.",
      "T": "Adah gave birth to Jabal, who became the ancestor of those who live in tents and keep livestock."
    },
    "21": {
      "L": "His brother's name was Jubal; he was the father of all those who play the lyre and pipe.",
      "M": "His brother's name was Jubal; he was the father of all who play stringed instruments and pipes.",
      "T": "His brother Jubal became the ancestor of all who play the harp and flute."
    },
    "22": {
      "L": "Zillah also bore Tubal-cain; he was the forger of all instruments of bronze and iron. The sister of Tubal-cain was Naamah.",
      "M": "Zillah also had a son, Tubal-Cain, who forged all kinds of tools out of bronze and iron. Tubal-Cain's sister was Naamah.",
      "T": "Zillah gave birth to Tubal-cain, who crafted all kinds of bronze and iron tools. Tubal-cain's sister was Naamah."
    },
    "23": {
      "L": "Lamech said to his wives:\n'Adah and Zillah, hear my voice;\nyou wives of Lamech, listen to what I say:\nI have killed a man for wounding me,\na young man for striking me.'",
      "M": "Lamech said to his wives,\n'Adah and Zillah, listen to me;\nwives of Lamech, hear my words.\nI have killed a man for wounding me,\na young man for injuring me.'",
      "T": "Lamech sang to his wives:\n'Adah and Zillah, listen to me!\nWives of Lamech, hear what I say!\nI have killed a man who struck me,\na young man who wounded me.'"
    },
    "24": {
      "L": "'If Cain's revenge is sevenfold, then Lamech's is seventy-sevenfold.'",
      "M": "'If Cain is avenged seven times, then Lamech seventy-seven times.'",
      "T": "'If Cain is avenged seven times over, then Lamech will be avenged seventy-seven times!'"
    },
    "25": {
      "L": "And Adam knew his wife again, and she bore a son and called his name Seth, for she said, 'God has appointed for me another offspring instead of Abel, for Cain killed him.'",
      "M": "Adam made love to his wife again, and she gave birth to a son and named him Seth, saying, 'God has granted me another child in place of Abel, since Cain killed him.'",
      "T": "Adam was intimate with his wife again, and she gave birth to a son she named Seth. She said, 'God has given me another child to replace Abel, whom Cain killed.'"
    },
    "26": {
      "L": "To Seth also a son was born, and he called his name Enosh. At that time people began to call upon the name of the LORD.",
      "M": "Seth also had a son, and he named him Enosh. At that time people began to call on the name of the LORD.",
      "T": "Seth also had a son, and named him Enosh. It was at this time that people began calling on the name of the LORD."
    }
  },
  "5": {
    "1": {
      "L": "This is the book of the generations of Adam. When God created man, he made him in the likeness of God.",
      "M": "This is the written account of Adam's family line. When God created mankind, he made them in the likeness of God.",
      "T": "This is the record of Adam's family line. When God created human beings, he made them to reflect his own likeness."
    },
    "2": {
      "L": "Male and female he created them, and he blessed them and named them Man when they were created.",
      "M": "He created them male and female and blessed them. And he named them 'Mankind' when they were created.",
      "T": "He created them male and female, blessed them, and called them 'Humanity' at the time of their creation."
    },
    "3": {
      "L": "When Adam had lived 130 years, he fathered a son in his own likeness, after his image, and named him Seth.",
      "M": "When Adam had lived 130 years, he had a son in his own likeness, in his own image; and he named him Seth.",
      "T": "When Adam was 130 years old, he had a son who resembled him—made in his own image—and he named him Seth."
    },
    "4": {
      "L": "The days of Adam after he fathered Seth were 800 years, and he had other sons and daughters.",
      "M": "After Seth was born, Adam lived 800 years and had other sons and daughters.",
      "T": "After Seth was born, Adam lived another 800 years and had other sons and daughters."
    },
    "5": {
      "L": "Thus all the days that Adam lived were 930 years, and he died.",
      "M": "Altogether, Adam lived a total of 930 years, and then he died.",
      "T": "Adam lived a total of 930 years, and then he died."
    },
    "6": {
      "L": "When Seth had lived 105 years, he fathered Enosh.",
      "M": "When Seth had lived 105 years, he became the father of Enosh.",
      "T": "When Seth was 105 years old, he had a son named Enosh."
    },
    "7": {
      "L": "Seth lived after he fathered Enosh 807 years and had other sons and daughters.",
      "M": "After he became the father of Enosh, Seth lived 807 years and had other sons and daughters.",
      "T": "After Enosh was born, Seth lived another 807 years and had other sons and daughters."
    },
    "8": {
      "L": "Thus all the days of Seth were 912 years, and he died.",
      "M": "Altogether, Seth lived a total of 912 years, and then he died.",
      "T": "Seth lived a total of 912 years, and then he died."
    },
    "9": {
      "L": "When Enosh had lived 90 years, he fathered Kenan.",
      "M": "When Enosh had lived 90 years, he became the father of Kenan.",
      "T": "When Enosh was 90 years old, he had a son named Kenan."
    },
    "10": {
      "L": "Enosh lived after he fathered Kenan 815 years and had other sons and daughters.",
      "M": "After he became the father of Kenan, Enosh lived 815 years and had other sons and daughters.",
      "T": "After Kenan was born, Enosh lived another 815 years and had other sons and daughters."
    },
    "11": {
      "L": "Thus all the days of Enosh were 905 years, and he died.",
      "M": "Altogether, Enosh lived a total of 905 years, and then he died.",
      "T": "Enosh lived a total of 905 years, and then he died."
    },
    "12": {
      "L": "When Kenan had lived 70 years, he fathered Mahalalel.",
      "M": "When Kenan had lived 70 years, he became the father of Mahalalel.",
      "T": "When Kenan was 70 years old, he had a son named Mahalalel."
    },
    "13": {
      "L": "Kenan lived after he fathered Mahalalel 840 years and had other sons and daughters.",
      "M": "After he became the father of Mahalalel, Kenan lived 840 years and had other sons and daughters.",
      "T": "After Mahalalel was born, Kenan lived another 840 years and had other sons and daughters."
    },
    "14": {
      "L": "Thus all the days of Kenan were 910 years, and he died.",
      "M": "Altogether, Kenan lived a total of 910 years, and then he died.",
      "T": "Kenan lived a total of 910 years, and then he died."
    },
    "15": {
      "L": "When Mahalalel had lived 65 years, he fathered Jared.",
      "M": "When Mahalalel had lived 65 years, he became the father of Jared.",
      "T": "When Mahalalel was 65 years old, he had a son named Jared."
    },
    "16": {
      "L": "Mahalalel lived after he fathered Jared 830 years and had other sons and daughters.",
      "M": "After he became the father of Jared, Mahalalel lived 830 years and had other sons and daughters.",
      "T": "After Jared was born, Mahalalel lived another 830 years and had other sons and daughters."
    },
    "17": {
      "L": "Thus all the days of Mahalalel were 895 years, and he died.",
      "M": "Altogether, Mahalalel lived a total of 895 years, and then he died.",
      "T": "Mahalalel lived a total of 895 years, and then he died."
    },
    "18": {
      "L": "When Jared had lived 162 years, he fathered Enoch.",
      "M": "When Jared had lived 162 years, he became the father of Enoch.",
      "T": "When Jared was 162 years old, he had a son named Enoch."
    },
    "19": {
      "L": "Jared lived after he fathered Enoch 800 years and had other sons and daughters.",
      "M": "After he became the father of Enoch, Jared lived 800 years and had other sons and daughters.",
      "T": "After Enoch was born, Jared lived another 800 years and had other sons and daughters."
    },
    "20": {
      "L": "Thus all the days of Jared were 962 years, and he died.",
      "M": "Altogether, Jared lived a total of 962 years, and then he died.",
      "T": "Jared lived a total of 962 years, and then he died."
    },
    "21": {
      "L": "When Enoch had lived 65 years, he fathered Methuselah.",
      "M": "When Enoch had lived 65 years, he became the father of Methuselah.",
      "T": "When Enoch was 65 years old, he had a son named Methuselah."
    },
    "22": {
      "L": "Enoch walked with God after he fathered Methuselah 300 years and had other sons and daughters.",
      "M": "After he became the father of Methuselah, Enoch walked faithfully with God 300 years and had other sons and daughters.",
      "T": "After Methuselah was born, Enoch walked in close fellowship with God for 300 years and had other sons and daughters."
    },
    "23": {
      "L": "Thus all the days of Enoch were 365 years.",
      "M": "Altogether, Enoch lived a total of 365 years.",
      "T": "Enoch lived a total of 365 years."
    },
    "24": {
      "L": "Enoch walked with God, and he was not, for God took him.",
      "M": "Enoch walked faithfully with God; then he was no more, because God took him away.",
      "T": "Enoch walked in close fellowship with God—and then he was gone, because God took him."
    },
    "25": {
      "L": "When Methuselah had lived 187 years, he fathered Lamech.",
      "M": "When Methuselah had lived 187 years, he became the father of Lamech.",
      "T": "When Methuselah was 187 years old, he had a son named Lamech."
    },
    "26": {
      "L": "Methuselah lived after he fathered Lamech 782 years and had other sons and daughters.",
      "M": "After he became the father of Lamech, Methuselah lived 782 years and had other sons and daughters.",
      "T": "After Lamech was born, Methuselah lived another 782 years and had other sons and daughters."
    },
    "27": {
      "L": "Thus all the days of Methuselah were 969 years, and he died.",
      "M": "Altogether, Methuselah lived a total of 969 years, and then he died.",
      "T": "Methuselah lived a total of 969 years, and then he died."
    },
    "28": {
      "L": "When Lamech had lived 182 years, he fathered a son",
      "M": "When Lamech had lived 182 years, he had a son.",
      "T": "When Lamech was 182 years old, he had a son."
    },
    "29": {
      "L": "and called his name Noah, saying, 'Out of the ground that the LORD has cursed this one shall bring us relief from our work and from the painful toil of our hands.'",
      "M": "He named him Noah and said, 'He will comfort us in the labor and painful toil of our hands caused by the ground the LORD has cursed.'",
      "T": "He named him Noah, saying, 'This one will bring us relief from the hard work and painful toil of farming the ground the LORD has cursed.'"
    },
    "30": {
      "L": "Lamech lived after he fathered Noah 595 years and had other sons and daughters.",
      "M": "After Noah was born, Lamech lived 595 years and had other sons and daughters.",
      "T": "After Noah was born, Lamech lived another 595 years and had other sons and daughters."
    },
    "31": {
      "L": "Thus all the days of Lamech were 777 years, and he died.",
      "M": "Altogether, Lamech lived a total of 777 years, and then he died.",
      "T": "Lamech lived a total of 777 years, and then he died."
    },
    "32": {
      "L": "After Noah was 500 years old, Noah fathered Shem, Ham, and Japheth.",
      "M": "After Noah was 500 years old, he became the father of Shem, Ham and Japheth.",
      "T": "After Noah was 500 years old, he had three sons: Shem, Ham, and Japheth."
    }
  },
  "6": {
    "1": {
      "L": "When man began to multiply on the face of the land and daughters were born to them,",
      "M": "When human beings began to increase in number on the earth and daughters were born to them,",
      "T": "As the human population grew and spread across the earth, daughters were born to them."
    },
    "2": {
      "L": "the sons of God saw that the daughters of man were attractive. And they took as their wives any they chose.",
      "M": "the sons of God saw that the daughters of humans were beautiful, and they married any of them they chose.",
      "T": "The divine beings saw how beautiful the human women were and took as wives whichever ones they wanted."
    },
    "3": {
      "L": "Then the LORD said, 'My Spirit shall not abide in man forever, for he is flesh: his days shall be 120 years.'",
      "M": "Then the LORD said, 'My Spirit will not contend with humans forever, for they are mortal; their days will be a hundred and twenty years.'",
      "T": "The LORD said, 'My Spirit will not remain in human beings forever, for they are mortal. Their lifespan will be limited to 120 years.'"
    },
    "4": {
      "L": "The Nephilim were on the earth in those days, and also afterward, when the sons of God came in to the daughters of man and they bore children to them. These were the mighty men who were of old, the men of renown.",
      "M": "The Nephilim were on the earth in those days—and also afterward—when the sons of God went to the daughters of humans and had children by them. They were the heroes of old, men of renown.",
      "T": "The Nephilim—those fearsome giants of legend—lived on the earth in those days, and also afterward, when the divine beings had children by human women. These became the legendary warriors of ancient times, men whose fame spread throughout the world."
    },
    "5": {
      "L": "The LORD saw that the wickedness of man was great in the earth, and that every intention of the thoughts of his heart was only evil continually.",
      "M": "The LORD saw how great the wickedness of the human race had become on the earth, and that every inclination of the thoughts of the human heart was only evil all the time.",
      "T": "The LORD observed how widespread human wickedness had become on the earth—that every thought and impulse of the human heart was nothing but evil, all the time."
    },
    "6": {
      "L": "And the LORD regretted that he had made man on the earth, and it grieved him to his heart.",
      "M": "The LORD regretted that he had made human beings on the earth, and his heart was deeply troubled.",
      "T": "The LORD was grieved that he had made human beings on the earth, and his heart was filled with pain."
    },
    "7": {
      "L": "So the LORD said, 'I will blot out man whom I have created from the face of the land, man and animals and creeping things and birds of the heavens, for I am sorry that I have made them.'",
      "M": "So the LORD said, 'I will wipe from the face of the earth the human race I have created—and with them the animals, the birds and the creatures that move along the ground—for I regret that I have made them.'",
      "T": "So the LORD said, 'I will wipe out the human race I created from the face of the earth—along with every animal, bird, and crawling creature—because I regret making them.'"
    },
    "8": {
      "L": "But Noah found favor in the eyes of the LORD.",
      "M": "But Noah found favor in the eyes of the LORD.",
      "T": "But Noah found grace in the eyes of the LORD."
    },
    "9": {
      "L": "These are the generations of Noah. Noah was a righteous man, blameless in his generation. Noah walked with God.",
      "M": "This is the account of Noah and his family. Noah was a righteous man, blameless among the people of his time, and he walked faithfully with God.",
      "T": "This is the story of Noah and his family. Noah was a righteous man—blameless among the people of his day—and he walked in close fellowship with God."
    },
    "10": {
      "L": "And Noah had three sons, Shem, Ham, and Japheth.",
      "M": "Noah had three sons: Shem, Ham and Japheth.",
      "T": "Noah had three sons: Shem, Ham, and Japheth."
    },
    "11": {
      "L": "Now the earth was corrupt in God's sight, and the earth was filled with violence.",
      "M": "Now the earth was corrupt in God's sight and was full of violence.",
      "T": "The earth had become corrupt in God's sight and was filled with violence."
    },
    "12": {
      "L": "And God saw the earth, and behold, it was corrupt, for all flesh had corrupted their way on the earth.",
      "M": "God saw how corrupt the earth had become, for all the people on earth had corrupted their ways.",
      "T": "God looked at the earth and saw how thoroughly corrupt it was—every creature had corrupted its way of life."
    },
    "13": {
      "L": "And God said to Noah, 'I have determined to make an end of all flesh, for the earth is filled with violence through them. Behold, I will destroy them with the earth.'",
      "M": "So God said to Noah, 'I am going to put an end to all people, for the earth is filled with violence because of them. I am surely going to destroy both them and the earth.'",
      "T": "So God told Noah, 'I have decided to bring an end to all living creatures, for the earth is saturated with violence because of them. I am about to destroy them along with the earth.'"
    },
    "14": {
      "L": "'Make yourself an ark of gopher wood. Make rooms in the ark, and cover it inside and out with pitch.'",
      "M": "'So make yourself an ark of cypress wood; make rooms in it and coat it with pitch inside and out.'",
      "T": "'Build yourself an ark from cypress wood. Make compartments in it and seal it inside and out with tar.'"
    },
    "15": {
      "L": "'This is how you are to make it: the length of the ark 300 cubits, its breadth 50 cubits, and its height 30 cubits.'",
      "M": "'This is how you are to build it: The ark is to be three hundred cubits long, fifty cubits wide and thirty cubits high.'",
      "T": "'Here are the dimensions: 300 cubits long, 50 cubits wide, and 30 cubits high.'"
    },
    "16": {
      "L": "'Make a roof for the ark, and finish it to a cubit above, and set the door of the ark in its side. Make it with lower, second, and third decks.'",
      "M": "'Make a roof for it, leaving below the roof an opening one cubit high all around. Put a door in the side of the ark and make lower, middle and upper decks.'",
      "T": "'Put a roof on it, with an eighteen-inch opening all around just below the roof. Put a door in the side, and build three decks inside—lower, middle, and upper.'"
    },
    "17": {
      "L": "'For behold, I will bring a flood of waters upon the earth to destroy all flesh in which is the breath of life under heaven. Everything that is on the earth shall die.'",
      "M": "'I am going to bring floodwaters on the earth to destroy all life under the heavens, every creature that has the breath of life in it. Everything on earth will perish.'",
      "T": "'I am about to flood the earth to destroy every living creature under the sky—every living thing that breathes. Everything on earth will die.'"
    },
    "18": {
      "L": "'But I will establish my covenant with you, and you shall come into the ark, you, your sons, your wife, and your sons' wives with you.'",
      "M": "'But I will establish my covenant with you, and you will enter the ark—you and your sons and your wife and your sons' wives with you.'",
      "T": "'But I will establish my covenant with you. You, your sons, your wife, and your daughters-in-law will enter the ark together.'"
    },
    "19": {
      "L": "'And of every living thing of all flesh, you shall bring two of every sort into the ark to keep them alive with you. They shall be male and female.'",
      "M": "'You are to bring into the ark two of all living creatures, male and female, to keep them alive with you.'",
      "T": "'Bring two of every living creature into the ark with you—one male and one female—to keep them alive.'"
    },
    "20": {
      "L": "'Of the birds according to their kinds, and of the animals according to their kinds, of every creeping thing of the ground according to its kind, two of every sort shall come in to you to keep them alive.'",
      "M": "'Two of every kind of bird, of every kind of animal and of every kind of creature that moves along the ground will come to you to be kept alive.'",
      "T": "'Two of every kind of bird, animal, and crawling creature will come to you to be kept alive—one male and one female of each.'"
    },
    "21": {
      "L": "'Also take with you every sort of food that is eaten, and store it up. It shall serve as food for you and for them.'",
      "M": "'You are to take every kind of food that is to be eaten and store it away as food for you and for them.'",
      "T": "'Also gather every kind of food and store it up, enough for you and all the animals.'"
    },
    "22": {
      "L": "Noah did this; he did all that God commanded him.",
      "M": "Noah did everything just as God commanded him.",
      "T": "Noah did everything exactly as God commanded him."
    }
  },
  "7": {
    "1": {
      "L": "Then the LORD said to Noah, 'Go into the ark, you and all your household, for I have seen that you are righteous before me in this generation.'",
      "M": "The LORD then said to Noah, 'Go into the ark, you and your whole family, because I have found you righteous in this generation.'",
      "T": "Then the LORD said to Noah, 'Go into the ark—you and your whole family—because you alone are righteous in this generation.'"
    },
    "2": {
      "L": "'Take with you seven pairs of all clean animals, the male and his mate, and a pair of the animals that are not clean, the male and his mate,'",
      "M": "'Take with you seven pairs of every kind of clean animal, a male and its mate, and one pair of every kind of unclean animal, a male and its mate,'",
      "T": "'Take with you seven pairs of every clean animal—a male and its mate—and one pair of every unclean animal—a male and its mate.'"
    },
    "3": {
      "L": "'and seven pairs of the birds of the heavens also, male and female, to keep their offspring alive on the face of all the earth.'",
      "M": "'and also seven pairs of every kind of bird, male and female, to keep their various kinds alive throughout the earth.'",
      "T": "'Also take seven pairs of every kind of bird, male and female, to preserve their offspring throughout the earth.'"
    },
    "4": {
      "L": "'For in seven days I will send rain on the earth forty days and forty nights, and every living thing that I have made I will blot out from the face of the ground.'",
      "M": "'Seven days from now I will send rain on the earth for forty days and forty nights, and I will wipe from the face of the earth every living creature I have made.'",
      "T": "'In seven days I will send rain that will fall for forty days and forty nights, and I will wipe out every living creature I have made from the face of the earth.'"
    },
    "5": {
      "L": "And Noah did all that the LORD had commanded him.",
      "M": "And Noah did all that the LORD commanded him.",
      "T": "Noah did everything the LORD commanded him."
    },
    "6": {
      "L": "Noah was 600 years old when the flood of waters came upon the earth.",
      "M": "Noah was six hundred years old when the floodwaters came on the earth.",
      "T": "Noah was 600 years old when the floodwaters came on the earth."
    },
    "7": {
      "L": "And Noah and his sons and his wife and his sons' wives with him went into the ark to escape the waters of the flood.",
      "M": "And Noah and his sons and his wife and his sons' wives entered the ark to escape the waters of the flood.",
      "T": "Noah and his sons, his wife, and his daughters-in-law entered the ark to escape the floodwaters."
    },
    "8": {
      "L": "Of clean animals, and of animals that are not clean, and of birds, and of everything that creeps on the ground,",
      "M": "Pairs of clean and unclean animals, of birds and of all creatures that move along the ground,",
      "T": "Pairs of clean and unclean animals, of birds and of all creatures that crawl on the ground,"
    },
    "9": {
      "L": "two and two, male and female, went into the ark with Noah, as God had commanded Noah.",
      "M": "male and female, came to Noah and entered the ark, as God had commanded Noah.",
      "T": "male and female, came to Noah and entered the ark, just as God had commanded."
    },
    "10": {
      "L": "And after seven days the waters of the flood came upon the earth.",
      "M": "And after the seven days the floodwaters came on the earth.",
      "T": "Seven days later the floodwaters covered the earth."
    },
    "11": {
      "L": "In the six hundredth year of Noah's life, in the second month, on the seventeenth day of the month, on that day all the fountains of the great deep burst forth, and the windows of the heavens were opened.",
      "M": "In the six hundredth year of Noah's life, on the seventeenth day of the second month—on that day all the springs of the great deep burst forth, and the floodgates of the heavens were opened.",
      "T": "On the seventeenth day of the second month of Noah's six-hundredth year, all the underground springs of the vast deep erupted, and the floodgates of the sky were thrown open."
    },
    "12": {
      "L": "And rain fell upon the earth forty days and forty nights.",
      "M": "And rain fell on the earth forty days and forty nights.",
      "T": "Rain poured down on the earth for forty days and forty nights."
    },
    "13": {
      "L": "On the very same day Noah and his sons, Shem and Ham and Japheth, and Noah's wife and the three wives of his sons with them entered the ark,",
      "M": "On that very day Noah and his sons, Shem, Ham and Japheth, together with his wife and the wives of his three sons, entered the ark.",
      "T": "That same day Noah and his sons—Shem, Ham, and Japheth—entered the ark, along with his wife and his three daughters-in-law."
    },
    "14": {
      "L": "they and every beast, according to its kind, and all the livestock according to their kinds, and every creeping thing that creeps on the earth, according to its kind, and every bird, according to its kind, every winged creature.",
      "M": "They had with them every wild animal according to its kind, all livestock according to their kinds, every creature that moves along the ground according to its kind and every bird according to its kind, everything with wings.",
      "T": "With them were every kind of wild animal, every kind of livestock, every kind of crawling creature, and every kind of bird—everything with wings."
    },
    "15": {
      "L": "They went into the ark with Noah, two and two of all flesh in which there was the breath of life.",
      "M": "Pairs of all creatures that have the breath of life in them came to Noah and entered the ark.",
      "T": "Pairs of every living, breathing creature came to Noah and entered the ark."
    },
    "16": {
      "L": "And those that entered, male and female of all flesh, went in as God had commanded him. And the LORD shut him in.",
      "M": "The animals going in were male and female of every living thing, as God had commanded Noah. Then the LORD shut him in.",
      "T": "They entered the ark male and female, just as God had commanded. Then the LORD himself shut the door behind them."
    },
    "17": {
      "L": "The flood continued forty days on the earth. The waters increased and bore up the ark, and it rose high above the earth.",
      "M": "For forty days the flood kept coming on the earth, and as the waters increased they lifted the ark high above the earth.",
      "T": "The flood lasted forty days. As the waters rose, they lifted the ark up above the earth."
    },
    "18": {
      "L": "The waters prevailed and increased greatly on the earth, and the ark floated on the face of the waters.",
      "M": "The waters rose and increased greatly on the earth, and the ark floated on the surface of the water.",
      "T": "The waters rose higher and higher, and the ark drifted on the surface."
    },
    "19": {
      "L": "And the waters prevailed so mightily on the earth that all the high mountains under the whole heaven were covered.",
      "M": "They rose greatly on the earth, and all the high mountains under the entire heavens were covered.",
      "T": "The waters rose so high that even the tallest mountains under the sky were submerged."
    },
    "20": {
      "L": "The waters prevailed above the mountains, covering them fifteen cubits deep.",
      "M": "The waters rose and covered the mountains to a depth of more than fifteen cubits.",
      "T": "The mountains were covered to a depth of over twenty feet."
    },
    "21": {
      "L": "And all flesh died that moved on the earth, birds, livestock, beasts, all swarming creatures that swarm on the earth, and all mankind.",
      "M": "Every living thing that moved on land perished—birds, livestock, wild animals, all the creatures that swarm over the earth, and all mankind.",
      "T": "Every living creature on land died—birds, livestock, wild animals, every swarming creature, and every human being."
    },
    "22": {
      "L": "Everything on the dry land in whose nostrils was the breath of life died.",
      "M": "Everything on dry land that had the breath of life in its nostrils died.",
      "T": "Every creature on dry land that breathed through its nostrils died."
    },
    "23": {
      "L": "He blotted out every living thing that was on the face of the ground, man and animals and creeping things and birds of the heavens. They were blotted out from the earth. Only Noah was left, and those who were with him in the ark.",
      "M": "Every living thing on the face of the earth was wiped out; people and animals and the creatures that move along the ground and the birds were wiped from the earth. Only Noah was left, and those with him in the ark.",
      "T": "God wiped out every living creature on the face of the earth—people, animals, crawling things, and birds. They were all swept from the earth. Only Noah and those with him in the ark survived."
    },
    "24": {
      "L": "And the waters prevailed on the earth 150 days.",
      "M": "The waters flooded the earth for a hundred and fifty days.",
      "T": "The floodwaters covered the earth for 150 days."
    }
  },
  "8": {
    "1": {
      "L": "But God remembered Noah and all the beasts and all the livestock that were with him in the ark. And God made a wind blow over the earth, and the waters subsided.",
      "M": "But God remembered Noah and all the wild animals and the livestock that were with him in the ark, and he sent a wind over the earth, and the waters receded.",
      "T": "But God remembered Noah and all the animals with him in the ark. He sent a wind to blow across the earth, and the floodwaters began to recede."
    },
    "2": {
      "L": "The fountains of the deep and the windows of the heavens were closed, the rain from the heavens was restrained,",
      "M": "Now the springs of the deep and the floodgates of the heavens had been closed, and the rain had stopped falling from the sky.",
      "T": "The underground springs stopped flowing, the floodgates of the sky were closed, and the rain stopped."
    },
    "3": {
      "L": "and the waters receded from the earth continually. At the end of 150 days the waters had abated,",
      "M": "The water receded steadily from the earth. At the end of the hundred and fifty days the water had gone down,",
      "T": "The water gradually receded from the earth. By the end of 150 days the water level had dropped significantly,"
    },
    "4": {
      "L": "and in the seventh month, on the seventeenth day of the month, the ark came to rest on the mountains of Ararat.",
      "M": "and on the seventeenth day of the seventh month the ark came to rest on the mountains of Ararat.",
      "T": "and on the seventeenth day of the seventh month the ark settled on the mountains of Ararat."
    },
    "5": {
      "L": "And the waters continued to abate until the tenth month; in the tenth month, on the first day of the month, the tops of the mountains were seen.",
      "M": "The waters continued to recede until the tenth month, and on the first day of the tenth month the tops of the mountains became visible.",
      "T": "The waters continued to drop until the tenth month. On the first day of the tenth month, the tops of the mountains appeared."
    },
    "6": {
      "L": "At the end of forty days Noah opened the window of the ark that he had made",
      "M": "After forty days Noah opened a window he had made in the ark",
      "T": "After forty days, Noah opened the window he had built in the ark"
    },
    "7": {
      "L": "and sent forth a raven. It went to and fro until the waters were dried up from the earth.",
      "M": "and sent out a raven, and it kept flying back and forth until the water had dried up from the earth.",
      "T": "and released a raven. It kept flying back and forth until the water had dried up from the earth."
    },
    "8": {
      "L": "Then he sent forth a dove from him, to see if the waters had subsided from the face of the ground.",
      "M": "Then he sent out a dove to see if the water had receded from the surface of the ground.",
      "T": "Then he released a dove to see if the water had gone down from the surface of the ground."
    },
    "9": {
      "L": "But the dove found no place to set her foot, and she returned to him to the ark, for the waters were still on the face of the whole earth. So he put out his hand and took her and brought her into the ark with him.",
      "M": "But the dove could find nowhere to perch because there was water over all the surface of the earth; so it returned to Noah in the ark. He reached out his hand and took the dove and brought it back to himself in the ark.",
      "T": "But the dove found no place to land because water still covered everything. She flew back to the ark, and Noah reached out and brought her inside."
    },
    "10": {
      "L": "He waited another seven days, and again he sent forth the dove out of the ark.",
      "M": "He waited seven more days and again sent out the dove from the ark.",
      "T": "Noah waited seven more days and sent the dove out again."
    },
    "11": {
      "L": "And the dove came back to him in the evening, and behold, in her mouth was a freshly plucked olive leaf. So Noah knew that the waters had subsided from the earth.",
      "M": "When the dove returned to him in the evening, there in its beak was a freshly plucked olive leaf! Then Noah knew that the water had receded from the earth.",
      "T": "That evening the dove returned with a freshly plucked olive leaf in its beak! Noah knew then that the water had gone down."
    },
    "12": {
      "L": "Then he waited another seven days and sent forth the dove, and she did not return to him anymore.",
      "M": "He waited seven more days and sent the dove out again, but this time it did not return to him.",
      "T": "After seven more days he sent the dove out again, and this time it did not come back."
    },
    "13": {
      "L": "In the six hundred and first year, in the first month, the first day of the month, the waters were dried from off the earth. And Noah removed the covering of the ark and looked, and behold, the face of the ground was dry.",
      "M": "By the first day of the first month of Noah's six hundred and first year, the water had dried up from the earth. Noah then removed the covering from the ark and saw that the surface of the ground was dry.",
      "T": "On the first day of the first month of Noah's 601st year, the water had dried up from the earth. Noah removed the covering of the ark and looked out—the ground was dry!"
    },
    "14": {
      "L": "In the second month, on the twenty-seventh day of the month, the earth had dried out.",
      "M": "By the twenty-seventh day of the second month the earth was completely dry.",
      "T": "By the twenty-seventh day of the second month the earth was completely dry."
    },
    "15": {
      "L": "Then God said to Noah,",
      "M": "Then God said to Noah,",
      "T": "Then God spoke to Noah:"
    },
    "16": {
      "L": "'Go out from the ark, you and your wife, and your sons and your sons' wives with you.'",
      "M": "'Come out of the ark, you and your wife and your sons and their wives.'",
      "T": "'Leave the ark—you and your wife, your sons and their wives.'"
    },
    "17": {
      "L": "'Bring out with you every living thing that is with you of all flesh—birds and animals and every creeping thing that creeps on the earth—that they may swarm on the earth, and be fruitful and multiply on the earth.'",
      "M": "'Bring out every kind of living creature that is with you—the birds, the animals, and all the creatures that move along the ground—so they can multiply on the earth and be fruitful and increase in number on it.'",
      "T": "'Take every living creature out with you—the birds, the animals, and everything that crawls—so they can spread across the earth, multiply, and fill it.'"
    },
    "18": {
      "L": "So Noah went out, and his sons and his wife and his sons' wives with him.",
      "M": "So Noah came out, together with his sons and his wife and his sons' wives.",
      "T": "So Noah came out, together with his sons and his wife and his daughters-in-law."
    },
    "19": {
      "L": "Every beast, every creeping thing, and every bird, everything that moves on the earth, went out by families from the ark.",
      "M": "All the animals and all the creatures that move along the ground and all the birds—everything that moves on land—came out of the ark, one kind after another.",
      "T": "Every animal, every crawling creature, and every bird—everything that moves on the earth—came out of the ark, family by family."
    },
    "20": {
      "L": "Then Noah built an altar to the LORD and took some of every clean animal and some of every clean bird and offered burnt offerings on the altar.",
      "M": "Then Noah built an altar to the LORD and, taking some of all the clean animals and clean birds, he sacrificed burnt offerings on it.",
      "T": "Then Noah built an altar to the LORD and sacrificed some of every clean animal and clean bird as burnt offerings on it."
    },
    "21": {
      "L": "And when the LORD smelled the pleasing aroma, the LORD said in his heart, 'I will never again curse the ground because of man, for the intention of man's heart is evil from his youth. Neither will I ever again strike down every living creature as I have done.'",
      "M": "The LORD smelled the pleasing aroma and said in his heart: 'Never again will I curse the ground because of humans, even though every inclination of the human heart is evil from childhood. And never again will I destroy all living creatures, as I have done.'",
      "T": "The LORD was pleased with the aroma and said to himself, 'Never again will I curse the ground because of human beings—even though every impulse of the human heart is bent toward evil from childhood. Never again will I destroy all living things as I have done.'"
    },
    "22": {
      "L": "'While the earth remains, seedtime and harvest, cold and heat, summer and winter, day and night, shall not cease.'",
      "M": "'As long as the earth endures, seedtime and harvest, cold and heat, summer and winter, day and night will never cease.'",
      "T": "'As long as the earth endures, there will always be planting and harvest, cold and heat, summer and winter, day and night—without interruption.'"
    }
  },
  "9": {
    "1": {
      "L": "And God blessed Noah and his sons and said to them, 'Be fruitful and multiply and fill the earth.'",
      "M": "Then God blessed Noah and his sons, saying to them, 'Be fruitful and increase in number and fill the earth.'",
      "T": "God blessed Noah and his sons and said to them, 'Have many children and fill the earth.'"
    },
    "2": {
      "L": "'The fear of you and the dread of you shall be upon every beast of the earth and upon every bird of the heavens, upon everything that creeps on the ground and all the fish of the sea. Into your hand they are delivered.'",
      "M": "'The fear and dread of you will fall on all the beasts of the earth, and on all the birds in the sky, on every creature that moves along the ground, and on all the fish in the sea; they are given into your hands.'",
      "T": "'Every wild animal, every bird, every creature that crawls, and every fish will fear and dread you. They are all placed under your authority.'"
    },
    "3": {
      "L": "'Every moving thing that lives shall be food for you. And as I gave you the green plants, I give you everything.'",
      "M": "'Everything that lives and moves about will be food for you. Just as I gave you the green plants, I now give you everything.'",
      "T": "'Every living creature is now yours to eat. Just as I gave you plants, I now give you everything.'"
    },
    "4": {
      "L": "'But you shall not eat flesh with its life, that is, its blood.'",
      "M": "'But you must not eat meat that has its lifeblood still in it.'",
      "T": "'But you must never eat meat with its lifeblood still in it.'"
    },
    "5": {
      "L": "'And for your lifeblood I will require a reckoning: from every beast I will require it and from man. From his fellow man I will require a reckoning for the life of man.'",
      "M": "'And for your lifeblood I will surely demand an accounting. I will demand an accounting from every animal. And from each human being, too, I will demand an accounting for the life of another human being.'",
      "T": "'I will demand an accounting for your lifeblood. I will hold every animal accountable, and I will hold human beings accountable for the lives of other human beings.'"
    },
    "6": {
      "L": "'Whoever sheds the blood of man, by man shall his blood be shed, for God made man in his own image.'",
      "M": "'Whoever sheds human blood, by humans shall their blood be shed; for in the image of God has God made mankind.'",
      "T": "'Whoever takes a human life shall have their own life taken in return—because God made human beings in his own image.'"
    },
    "7": {
      "L": "'And you, be fruitful and multiply, increase greatly on the earth and multiply in it.'",
      "M": "'As for you, be fruitful and increase in number; multiply on the earth and increase upon it.'",
      "T": "'As for you—have many children, multiply, and spread across the earth.'"
    },
    "8": {
      "L": "Then God said to Noah and to his sons with him,",
      "M": "Then God said to Noah and to his sons with him:",
      "T": "Then God said to Noah and his sons:"
    },
    "9": {
      "L": "'Behold, I establish my covenant with you and your offspring after you,'",
      "M": "'I now establish my covenant with you and with your descendants after you'",
      "T": "'I am establishing my covenant with you and with all your descendants after you—'"
    },
    "10": {
      "L": "'and with every living creature that is with you, the birds, the livestock, and every beast of the earth with you, as many as came out of the ark; it is for every beast of the earth.'",
      "M": "'and with every living creature that was with you—the birds, the livestock and all the wild animals, all those that came out of the ark with you—every living creature on earth.'",
      "T": "'and with every living creature that was with you—the birds, the livestock, all the wild animals—every creature that came out of the ark, every living thing on earth.'"
    },
    "11": {
      "L": "'I establish my covenant with you, that never again shall all flesh be cut off by the waters of the flood, and never again shall there be a flood to destroy the earth.'",
      "M": "'I establish my covenant with you: Never again will all life be destroyed by the waters of a flood; never again will there be a flood to destroy the earth.'",
      "T": "'This is my covenant with you: Never again will all living creatures be wiped out by floodwaters. Never again will a flood destroy the earth.'"
    },
    "12": {
      "L": "And God said, 'This is the sign of the covenant that I make between me and you and every living creature that is with you, for all future generations:'",
      "M": "And God said, 'This is the sign of the covenant I am making between me and you and every living creature with you, a covenant for all generations to come:'",
      "T": "God said, 'This is the sign of the covenant I am making between me and you and every living creature, for all generations to come:'"
    },
    "13": {
      "L": "'I have set my bow in the cloud, and it shall be a sign of the covenant between me and the earth.'",
      "M": "'I have set my rainbow in the clouds, and it will be the sign of the covenant between me and the earth.'",
      "T": "'I have placed my rainbow in the clouds as the sign of my covenant with the earth.'"
    },
    "14": {
      "L": "'When I bring clouds over the earth and the bow is seen in the clouds,'",
      "M": "'Whenever I bring clouds over the earth and the rainbow appears in the clouds,'",
      "T": "'Whenever I bring storm clouds over the earth and the rainbow appears,'"
    },
    "15": {
      "L": "'I will remember my covenant that is between me and you and every living creature of all flesh. And the waters shall never again become a flood to destroy all flesh.'",
      "M": "'I will remember my covenant between me and you and all living creatures of every kind. Never again will the waters become a flood to destroy all life.'",
      "T": "'I will remember my covenant between me and you and every living creature. The waters will never again flood the earth to destroy all life.'"
    },
    "16": {
      "L": "'When the bow is in the clouds, I will see it and remember the everlasting covenant between God and every living creature of all flesh that is on the earth.'",
      "M": "'Whenever the rainbow appears in the clouds, I will see it and remember the everlasting covenant between God and all living creatures of every kind on the earth.'",
      "T": "'When I see the rainbow in the clouds, I will remember the eternal covenant between God and every living creature on the earth.'"
    },
    "17": {
      "L": "God said to Noah, 'This is the sign of the covenant that I have established between me and all flesh that is on the earth.'",
      "M": "So God said to Noah, 'This is the sign of the covenant I have established between me and all life on the earth.'",
      "T": "God told Noah, 'This rainbow is the sign of the covenant I have established between me and every living creature on earth.'"
    },
    "18": {
      "L": "The sons of Noah who went forth from the ark were Shem, Ham, and Japheth. Ham was the father of Canaan.",
      "M": "The sons of Noah who came out of the ark were Shem, Ham and Japheth. Ham was the father of Canaan.",
      "T": "Noah's sons who came out of the ark were Shem, Ham, and Japheth. Ham was the father of Canaan."
    },
    "19": {
      "L": "These three were the sons of Noah, and from these the people of the whole earth were dispersed.",
      "M": "These were the three sons of Noah, and from them came the people who were scattered over the whole earth.",
      "T": "These three were Noah's sons, and from them spread all the people across the whole earth."
    },
    "20": {
      "L": "Noah began to be a man of the soil, and he planted a vineyard.",
      "M": "Noah, a man of the soil, proceeded to plant a vineyard.",
      "T": "Noah, a farmer, planted a vineyard."
    },
    "21": {
      "L": "He drank of the wine and became drunk and lay uncovered in his tent.",
      "M": "When he drank some of its wine, he became drunk and lay uncovered inside his tent.",
      "T": "He drank the wine, became drunk, and lay naked inside his tent."
    },
    "22": {
      "L": "And Ham, the father of Canaan, saw the nakedness of his father and told his two brothers outside.",
      "M": "Ham, the father of Canaan, saw his father naked and told his two brothers outside.",
      "T": "Ham, the father of Canaan, saw his father's nakedness and went outside and told his two brothers."
    },
    "23": {
      "L": "Then Shem and Japheth took a garment, laid it on both their shoulders, and walked backward and covered the nakedness of their father. Their faces were turned backward, and they did not see their father's nakedness.",
      "M": "But Shem and Japheth took a garment and laid it across their shoulders; then they walked in backward and covered their father's naked body. Their faces were turned the other way so that they would not see their father naked.",
      "T": "But Shem and Japheth took a garment and, holding it between them, walked in backward and covered their father's nakedness. They kept their faces turned away so they would not see him."
    },
    "24": {
      "L": "When Noah awoke from his wine and knew what his youngest son had done to him,",
      "M": "When Noah awoke from his wine and found out what his youngest son had done to him,",
      "T": "When Noah sobered up and learned what his youngest son had done to him,"
    },
    "25": {
      "L": "he said, 'Cursed be Canaan; a servant of servants shall he be to his brothers.'",
      "M": "he said, 'Cursed be Canaan! The lowest of slaves will he be to his brothers.'",
      "T": "he said, 'Cursed be Canaan! He will be the lowest of slaves to his brothers.'"
    },
    "26": {
      "L": "He also said, 'Blessed be the LORD, the God of Shem; and let Canaan be his servant.'",
      "M": "He also said, 'Praise be to the LORD, the God of Shem! May Canaan be the slave of Shem.'",
      "T": "'Blessed be the LORD, the God of Shem! May Canaan be Shem's slave.'"
    },
    "27": {
      "L": "'May God enlarge Japheth, and let him dwell in the tents of Shem, and let Canaan be his servant.'",
      "M": "'May God extend Japheth's territory; may Japheth live in the tents of Shem, and may Canaan be the slave of Japheth.'",
      "T": "'May God expand Japheth's territory. May he dwell in the tents of Shem, and may Canaan be his slave.'"
    },
    "28": {
      "L": "After the flood Noah lived 350 years.",
      "M": "After the flood Noah lived 350 years.",
      "T": "After the flood, Noah lived 350 more years."
    },
    "29": {
      "L": "All the days of Noah were 950 years, and he died.",
      "M": "Noah lived a total of 950 years, and then he died.",
      "T": "Noah lived a total of 950 years, and then he died."
    }
  },
  "10": {
    "1": {
      "L": "These are the generations of the sons of Noah, Shem, Ham, and Japheth. Sons were born to them after the flood.",
      "M": "This is the account of Shem, Ham and Japheth, Noah's sons, who themselves had sons after the flood.",
      "T": "This is the family record of Noah's sons—Shem, Ham, and Japheth—and the descendants born to them after the flood."
    },
    "2": {
      "L": "The sons of Japheth: Gomer, Magog, Madai, Javan, Tubal, Meshech, and Tiras.",
      "M": "The sons of Japheth: Gomer, Magog, Madai, Javan, Tubal, Meshek and Tiras.",
      "T": "Japheth's sons: Gomer, Magog, Madai, Javan, Tubal, Meshech, and Tiras."
    },
    "3": {
      "L": "The sons of Gomer: Ashkenaz, Riphath, and Togarmah.",
      "M": "The sons of Gomer: Ashkenaz, Riphath and Togarmah.",
      "T": "Gomer's sons: Ashkenaz, Riphath, and Togarmah."
    },
    "4": {
      "L": "The sons of Javan: Elishah, Tarshish, Kittim, and Dodanim.",
      "M": "The sons of Javan: Elishah, Tarshish, the Kittites and the Rodanites.",
      "T": "Javan's sons: Elishah, Tarshish, Kittim, and Dodanim."
    },
    "5": {
      "L": "From these the coastland peoples of the Gentiles were separated into their lands, every one according to his language, according to their clans, in their nations.",
      "M": "From these the maritime peoples spread out into their territories by their clans within their nations, each with its own language.",
      "T": "From these descendants came the coastal peoples, spread out according to their territories and languages, each nation in its own family line."
    },
    "6": {
      "L": "The sons of Ham: Cush, Egypt, Put, and Canaan.",
      "M": "The sons of Ham: Cush, Egypt, Put and Canaan.",
      "T": "Ham's sons: Cush, Egypt, Put, and Canaan."
    },
    "7": {
      "L": "The sons of Cush: Seba, Havilah, Sabtah, Raamah, and Sabteca. The sons of Raamah: Sheba and Dedan.",
      "M": "The sons of Cush: Seba, Havilah, Sabtah, Raamah and Sabteka. The sons of Raamah: Sheba and Dedan.",
      "T": "Cush's sons: Seba, Havilah, Sabtah, Raamah, and Sabteca. Raamah's sons: Sheba and Dedan."
    },
    "8": {
      "L": "Cush fathered Nimrod; he was the first on earth to be a mighty man.",
      "M": "Cush was the father of Nimrod, who became a mighty warrior on the earth.",
      "T": "Cush was the father of Nimrod, who grew up to be the first great conqueror on earth."
    },
    "9": {
      "L": "He was a mighty hunter before the LORD. Therefore it is said, 'Like Nimrod a mighty hunter before the LORD.'",
      "M": "He was a mighty hunter before the LORD; that is why it is said, 'Like Nimrod, a mighty hunter before the LORD.'",
      "T": "He was a mighty hunter, and his fame spread even before the LORD. That is where the saying comes from: 'Like Nimrod, a mighty hunter before the LORD.'"
    },
    "10": {
      "L": "The beginning of his kingdom was Babel, Erech, Accad, and Calneh, in the land of Shinar.",
      "M": "The first centers of his kingdom were Babylon, Uruk, Akkad and Kalneh, in Shinar.",
      "T": "The first cities of his kingdom were Babylon, Erech, Akkad, and Calneh in the land of Shinar."
    },
    "11": {
      "L": "From that land he went into Assyria and built Nineveh, Rehoboth-Ir, Calah, and Resen between Nineveh and Calah; that is the great city.",
      "M": "From that land he went to Assyria, where he built Nineveh, Rehoboth Ir, Calah",
      "T": "From there he expanded into Assyria and built Nineveh, Rehoboth-Ir, and Calah,"
    },
    "12": {
      "L": "and Resen between Nineveh and Calah; that is the great city.",
      "M": "and Resen, which is between Nineveh and Calah—which is the great city.",
      "T": "and Resen, between Nineveh and Calah—all of which together form the great city."
    },
    "13": {
      "L": "Egypt fathered Ludim, Anamim, Lehabim, Naphtuhim,",
      "M": "Egypt was the father of the Ludites, Anamites, Lehabites, Naphtuhites,",
      "T": "Egypt was the ancestor of the Ludites, Anamites, Lehabites, Naphtuhites,"
    },
    "14": {
      "L": "Pathrusim, Casluhim (from whom the Philistines came), and Caphtorim.",
      "M": "Pathrusites, Kasluhites (from whom the Philistines came) and Caphtorites.",
      "T": "Pathrusites, Casluhites—from whom the Philistines descended—and Caphtorites."
    },
    "15": {
      "L": "Canaan fathered Sidon his firstborn and Heth,",
      "M": "Canaan was the father of Sidon his firstborn, and of the Hittites,",
      "T": "Canaan was the father of Sidon, his firstborn, and the ancestor of the Hittites,"
    },
    "16": {
      "L": "and the Jebusites, the Amorites, the Girgashites,",
      "M": "Jebusites, Amorites, Girgashites,",
      "T": "Jebusites, Amorites, Girgashites,"
    },
    "17": {
      "L": "the Hivites, the Arkites, the Sinites,",
      "M": "Hivites, Arkites, Sinites,",
      "T": "Hivites, Arkites, Sinites,"
    },
    "18": {
      "L": "the Arvadites, the Zemarites, and the Hamathites. Afterward the clans of the Canaanites dispersed.",
      "M": "Arvadites, Zemarites and Hamathites. Later the Canaanite clans scattered",
      "T": "Arvadites, Zemarites, and Hamathites. Afterward the Canaanite clans scattered,"
    },
    "19": {
      "L": "And the territory of the Canaanites extended from Sidon in the direction of Gerar as far as Gaza, and in the direction of Sodom, Gomorrah, Admah, and Zeboiim, as far as Lasha.",
      "M": "and the borders of Canaan reached from Sidon toward Gerar as far as Gaza, and then toward Sodom, Gomorrah, Admah and Zeboyim, as far as Lasha.",
      "T": "and the Canaanite territory stretched from Sidon toward Gerar and Gaza, and then toward Sodom, Gomorrah, Admah, and Zeboiim, as far as Lasha."
    },
    "20": {
      "L": "These are the sons of Ham, by their clans, their languages, their lands, and their nations.",
      "M": "These are the sons of Ham by their clans and languages, in their territories and nations.",
      "T": "These are Ham's descendants, arranged by clan and language, in their territories and nations."
    },
    "21": {
      "L": "To Shem also, the father of all the children of Eber, the elder brother of Japheth, children were born.",
      "M": "Sons were also born to Shem, whose older brother was Japheth; Shem was the ancestor of all the sons of Eber.",
      "T": "Sons were also born to Shem—the elder brother of Japheth and the ancestor of all the descendants of Eber."
    },
    "22": {
      "L": "The sons of Shem: Elam, Asshur, Arpachshad, Lud, and Aram.",
      "M": "The sons of Shem: Elam, Asshur, Arphaxad, Lud and Aram.",
      "T": "Shem's sons: Elam, Asshur, Arphaxad, Lud, and Aram."
    },
    "23": {
      "L": "The sons of Aram: Uz, Hul, Gether, and Mash.",
      "M": "The sons of Aram: Uz, Hul, Gether and Meshek.",
      "T": "Aram's sons: Uz, Hul, Gether, and Mash."
    },
    "24": {
      "L": "Arpachshad fathered Shelah, and Shelah fathered Eber.",
      "M": "Arphaxad was the father of Shelah, and Shelah the father of Eber.",
      "T": "Arphaxad fathered Shelah, and Shelah fathered Eber."
    },
    "25": {
      "L": "To Eber were born two sons: the name of the one was Peleg, for in his days the earth was divided, and his brother's name was Joktan.",
      "M": "Two sons were born to Eber: One was named Peleg, because in his time the earth was divided; his brother was named Joktan.",
      "T": "Eber had two sons: one was named Peleg—because in his time the earth was divided—and his brother was named Joktan."
    },
    "26": {
      "L": "Joktan fathered Almodad, Sheleph, Hazarmaveth, Jerah,",
      "M": "Joktan was the father of Almodad, Sheleph, Hazarmaveth, Jerah,",
      "T": "Joktan was the ancestor of Almodad, Sheleph, Hazarmaveth, Jerah,"
    },
    "27": {
      "L": "Hadoram, Uzal, Diklah,",
      "M": "Hadoram, Uzal, Diklah,",
      "T": "Hadoram, Uzal, Diklah,"
    },
    "28": {
      "L": "Obal, Abimael, Sheba,",
      "M": "Obal, Abimael, Sheba,",
      "T": "Obal, Abimael, Sheba,"
    },
    "29": {
      "L": "Ophir, Havilah, and Jobab; all these were the sons of Joktan.",
      "M": "Ophir, Havilah and Jobab. All these were sons of Joktan.",
      "T": "Ophir, Havilah, and Jobab—all sons of Joktan."
    },
    "30": {
      "L": "The territory in which they lived extended from Mesha in the direction of Sephar to the hill country of the east.",
      "M": "The region where they lived stretched from Mesha toward Sephar, in the eastern hill country.",
      "T": "Their territory stretched from Mesha toward Sephar in the eastern hill country."
    },
    "31": {
      "L": "These are the sons of Shem, by their clans, their languages, their lands, and their nations.",
      "M": "These are the sons of Shem by their clans and languages, in their territories and nations.",
      "T": "These are Shem's descendants, arranged by clan and language, in their territories and nations."
    },
    "32": {
      "L": "These are the clans of the sons of Noah, according to their genealogies, in their nations, and from these the nations spread abroad on the earth after the flood.",
      "M": "These are the clans of Noah's sons, according to their lines of descent, within their nations. From these the nations spread out over the earth after the flood.",
      "T": "These are the family lines of Noah's sons, listed by nation. From these, the nations of the earth spread out after the flood."
    }
  }
}

for tier, key in [('literal','L'), ('mediating','M'), ('thought','T')]:
    data = load(tier, 'genesis')
    merge_tier(data, GENESIS, key)
    save(tier, 'genesis', data)

print('\nGenesis 1–10 written to all three tiers.')
print('Chapters covered:', sorted(GENESIS.keys(), key=int))
