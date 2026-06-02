"""
MKT Genesis chapters 11-20 — three-tier translation.
Run: python3 scripts/mkt-genesis-11-20.py
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
  "11": {
    "1": {
      "L": "Now the whole earth had one language and the same words.",
      "M": "Now the whole world had one language and a common speech.",
      "T": "At that time the whole world spoke a single language with a common vocabulary."
    },
    "2": {
      "L": "And as people migrated from the east, they found a plain in the land of Shinar and settled there.",
      "M": "As people moved eastward, they found a plain in Shinar and settled there.",
      "T": "As people moved eastward, they found a broad plain in the land of Shinar and settled there."
    },
    "3": {
      "L": "And they said to one another, 'Come, let us make bricks, and burn them thoroughly.' And they had brick for stone, and bitumen for mortar.",
      "M": "They said to each other, 'Come, let's make bricks and bake them thoroughly.' They used brick instead of stone, and tar for mortar.",
      "T": "They said to each other, 'Let's make bricks and fire them hard.' They used brick instead of stone and tar as mortar."
    },
    "4": {
      "L": "Then they said, 'Come, let us build ourselves a city and a tower with its top in the heavens, and let us make a name for ourselves, lest we be dispersed over the face of the whole earth.'",
      "M": "Then they said, 'Come, let us build ourselves a city, with a tower that reaches to the heavens, so that we may make a name for ourselves; otherwise we will be scattered over the face of the whole earth.'",
      "T": "Then they said, 'Let's build a city with a tower that reaches to the sky. We'll make a name for ourselves, and it will keep us from being scattered across the earth.'"
    },
    "5": {
      "L": "And the LORD came down to see the city and the tower, which the children of man had built.",
      "M": "But the LORD came down to see the city and the tower the people were building.",
      "T": "But the LORD came down to look at the city and the tower the people were building."
    },
    "6": {
      "L": "And the LORD said, 'Behold, they are one people, and they have all one language, and this is only the beginning of what they will do. And nothing that they propose to do will now be impossible for them.'",
      "M": "The LORD said, 'If as one people speaking the same language they have begun to do this, then nothing they plan to do will be impossible for them.'",
      "T": "The LORD said, 'Look—they are one people with one language. This is just the beginning of what they will be able to do. Soon nothing they set out to do will be beyond them.'"
    },
    "7": {
      "L": "'Come, let us go down and there confuse their language, so that they may not understand one another's speech.'",
      "M": "'Come, let us go down and confuse their language so they will not understand each other.'",
      "T": "'Come, let us go down and scramble their language so they can no longer understand each other.'"
    },
    "8": {
      "L": "So the LORD dispersed them from there over the face of all the earth, and they left off building the city.",
      "M": "So the LORD scattered them from there over all the earth, and they stopped building the city.",
      "T": "So the LORD scattered them across the whole earth, and they stopped building the city."
    },
    "9": {
      "L": "Therefore its name was called Babel, because there the LORD confused the language of all the earth. And from there the LORD dispersed them over the face of all the earth.",
      "M": "That is why it was called Babel—because there the LORD confused the language of the whole world. From there the LORD scattered them over the face of the whole earth.",
      "T": "That is why the city is called Babel—because there the LORD confused the language of the whole earth. From there the LORD scattered them across the face of the earth."
    },
    "10": {
      "L": "These are the generations of Shem. When Shem was 100 years old, he fathered Arpachshad two years after the flood.",
      "M": "This is the account of Shem's family line. Two years after the flood, when Shem was 100 years old, he became the father of Arphaxad.",
      "T": "This is the family record of Shem. Two years after the flood, when Shem was 100 years old, he had a son named Arphaxad."
    },
    "11": {
      "L": "And Shem lived after he fathered Arpachshad 500 years and had other sons and daughters.",
      "M": "And after he became the father of Arphaxad, Shem lived 500 years and had other sons and daughters.",
      "T": "After Arphaxad was born, Shem lived another 500 years and had other sons and daughters."
    },
    "12": {
      "L": "When Arpachshad had lived 35 years, he fathered Shelah.",
      "M": "When Arphaxad had lived 35 years, he became the father of Shelah.",
      "T": "When Arphaxad was 35 years old, he had a son named Shelah."
    },
    "13": {
      "L": "And Arpachshad lived after he fathered Shelah 403 years and had other sons and daughters.",
      "M": "And after he became the father of Shelah, Arphaxad lived 403 years and had other sons and daughters.",
      "T": "After Shelah was born, Arphaxad lived another 403 years and had other sons and daughters."
    },
    "14": {
      "L": "When Shelah had lived 30 years, he fathered Eber.",
      "M": "When Shelah had lived 30 years, he became the father of Eber.",
      "T": "When Shelah was 30 years old, he had a son named Eber."
    },
    "15": {
      "L": "And Shelah lived after he fathered Eber 403 years and had other sons and daughters.",
      "M": "And after he became the father of Eber, Shelah lived 403 years and had other sons and daughters.",
      "T": "After Eber was born, Shelah lived another 403 years and had other sons and daughters."
    },
    "16": {
      "L": "When Eber had lived 34 years, he fathered Peleg.",
      "M": "When Eber had lived 34 years, he became the father of Peleg.",
      "T": "When Eber was 34 years old, he had a son named Peleg."
    },
    "17": {
      "L": "And Eber lived after he fathered Peleg 430 years and had other sons and daughters.",
      "M": "And after he became the father of Peleg, Eber lived 430 years and had other sons and daughters.",
      "T": "After Peleg was born, Eber lived another 430 years and had other sons and daughters."
    },
    "18": {
      "L": "When Peleg had lived 30 years, he fathered Reu.",
      "M": "When Peleg had lived 30 years, he became the father of Reu.",
      "T": "When Peleg was 30 years old, he had a son named Reu."
    },
    "19": {
      "L": "And Peleg lived after he fathered Reu 209 years and had other sons and daughters.",
      "M": "And after he became the father of Reu, Peleg lived 209 years and had other sons and daughters.",
      "T": "After Reu was born, Peleg lived another 209 years and had other sons and daughters."
    },
    "20": {
      "L": "When Reu had lived 32 years, he fathered Serug.",
      "M": "When Reu had lived 32 years, he became the father of Serug.",
      "T": "When Reu was 32 years old, he had a son named Serug."
    },
    "21": {
      "L": "And Reu lived after he fathered Serug 207 years and had other sons and daughters.",
      "M": "And after he became the father of Serug, Reu lived 207 years and had other sons and daughters.",
      "T": "After Serug was born, Reu lived another 207 years and had other sons and daughters."
    },
    "22": {
      "L": "When Serug had lived 30 years, he fathered Nahor.",
      "M": "When Serug had lived 30 years, he became the father of Nahor.",
      "T": "When Serug was 30 years old, he had a son named Nahor."
    },
    "23": {
      "L": "And Serug lived after he fathered Nahor 200 years and had other sons and daughters.",
      "M": "And after he became the father of Nahor, Serug lived 200 years and had other sons and daughters.",
      "T": "After Nahor was born, Serug lived another 200 years and had other sons and daughters."
    },
    "24": {
      "L": "When Nahor had lived 29 years, he fathered Terah.",
      "M": "When Nahor had lived 29 years, he became the father of Terah.",
      "T": "When Nahor was 29 years old, he had a son named Terah."
    },
    "25": {
      "L": "And Nahor lived after he fathered Terah 119 years and had other sons and daughters.",
      "M": "And after he became the father of Terah, Nahor lived 119 years and had other sons and daughters.",
      "T": "After Terah was born, Nahor lived another 119 years and had other sons and daughters."
    },
    "26": {
      "L": "After Terah had lived 70 years, he fathered Abram, Nahor, and Haran.",
      "M": "After Terah had lived 70 years, he became the father of Abram, Nahor and Haran.",
      "T": "After Terah was 70 years old, he had three sons: Abram, Nahor, and Haran."
    },
    "27": {
      "L": "Now these are the generations of Terah. Terah fathered Abram, Nahor, and Haran; and Haran fathered Lot.",
      "M": "This is the account of Terah's family line. Terah became the father of Abram, Nahor and Haran. And Haran became the father of Lot.",
      "T": "This is the family record of Terah. Terah had three sons: Abram, Nahor, and Haran. Haran had a son named Lot."
    },
    "28": {
      "L": "Haran died in the presence of his father Terah in the land of his kindred, in Ur of the Chaldeans.",
      "M": "While his father Terah was still alive, Haran died in Ur of the Chaldeans, in the land of his birth.",
      "T": "Haran died before his father Terah in their homeland of Ur of the Chaldeans."
    },
    "29": {
      "L": "And Abram and Nahor took wives. The name of Abram's wife was Sarai, and the name of Nahor's wife, Milcah, the daughter of Haran the father of Milcah and Iscah.",
      "M": "Abram and Nahor both married. The name of Abram's wife was Sarai, and the name of Nahor's wife was Milcah; she was the daughter of Haran, the father of both Milcah and Iscah.",
      "T": "Abram and Nahor both married. Abram's wife was named Sarai, and Nahor's wife was Milcah, daughter of his brother Haran—who was also the father of Iscah."
    },
    "30": {
      "L": "Now Sarai was barren; she had no child.",
      "M": "Now Sarai was childless because she was not able to conceive.",
      "T": "Sarai was unable to have children; she was barren."
    },
    "31": {
      "L": "Terah took Abram his son and Lot the son of Haran, his grandson, and Sarai his daughter-in-law, his son Abram's wife, and they went forth together from Ur of the Chaldeans to go into the land of Canaan, but when they came to Haran, they settled there.",
      "M": "Terah took his son Abram, his grandson Lot son of Haran, and his daughter-in-law Sarai, the wife of his son Abram, and together they set out from Ur of the Chaldeans to go to Canaan. But when they came to Haran, they settled there.",
      "T": "Terah gathered his son Abram, his grandson Lot (Haran's son), and his daughter-in-law Sarai (Abram's wife), and they left Ur of the Chaldeans together, heading for the land of Canaan. But they stopped at Haran and settled there."
    },
    "32": {
      "L": "The days of Terah were 205 years, and Terah died in Haran.",
      "M": "Terah lived 205 years, and he died in Haran.",
      "T": "Terah lived to be 205 years old and died in Haran."
    }
  },
  "12": {
    "1": {
      "L": "Now the LORD said to Abram, 'Go from your country and your kindred and your father's house to the land that I will show you.'",
      "M": "The LORD had said to Abram, 'Go from your country, your people and your father's household to the land I will show you.'",
      "T": "The LORD said to Abram, 'Leave your homeland, your relatives, and your father's household, and go to the land I will show you.'"
    },
    "2": {
      "L": "'And I will make of you a great nation, and I will bless you and make your name great, so that you will be a blessing.'",
      "M": "'I will make you into a great nation, and I will bless you; I will make your name great, and you will be a blessing.'",
      "T": "'I will make you into a great nation. I will bless you and make your name famous, and you will be a source of blessing to others.'"
    },
    "3": {
      "L": "'I will bless those who bless you, and him who dishonors you I will curse, and in you all the families of the earth shall be blessed.'",
      "M": "'I will bless those who bless you, and whoever curses you I will curse; and all peoples on earth will be blessed through you.'",
      "T": "'I will bless those who treat you well and curse those who treat you with contempt. Through you, every family on earth will be blessed.'"
    },
    "4": {
      "L": "So Abram went, as the LORD had told him, and Lot went with him. Abram was 75 years old when he departed from Haran.",
      "M": "So Abram went, as the LORD had told him; and Lot went with him. Abram was seventy-five years old when he set out from Haran.",
      "T": "So Abram went, just as the LORD had instructed. Lot went with him. Abram was 75 years old when he left Haran."
    },
    "5": {
      "L": "And Abram took Sarai his wife, and Lot his brother's son, and all their possessions that they had gathered, and the people that they had acquired in Haran, and they set out to go to the land of Canaan. When they came to the land of Canaan,",
      "M": "He took his wife Sarai, his nephew Lot, all the possessions they had accumulated and the people they had acquired in Haran, and they set out for the land of Canaan, and they arrived there.",
      "T": "Abram took his wife Sarai, his nephew Lot, all their accumulated possessions, and the people they had gathered in Haran, and they set out for the land of Canaan—and arrived there."
    },
    "6": {
      "L": "Abram passed through the land to the place at Shechem, to the oak of Moreh. At that time the Canaanites were in the land.",
      "M": "Abram traveled through the land as far as the site of the great tree of Moreh at Shechem. At that time the Canaanites were in the land.",
      "T": "Abram traveled through the land as far as the great tree of Moreh at Shechem. The Canaanites were living there at that time."
    },
    "7": {
      "L": "Then the LORD appeared to Abram and said, 'To your offspring I will give this land.' So he built there an altar to the LORD, who had appeared to him.",
      "M": "The LORD appeared to Abram and said, 'To your offspring I will give this land.' So he built an altar there to the LORD, who had appeared to him.",
      "T": "The LORD appeared to Abram and said, 'I will give this land to your descendants.' Abram built an altar there to the LORD, who had appeared to him."
    },
    "8": {
      "L": "From there he moved to the hill country on the east of Bethel and pitched his tent, with Bethel on the west and Ai on the east. And there he built an altar to the LORD and called upon the name of the LORD.",
      "M": "From there he went on toward the hills east of Bethel and pitched his tent, with Bethel on the west and Ai on the east. There he built an altar to the LORD and called on the name of the LORD.",
      "T": "From there he moved on to the hill country east of Bethel and set up his tent, with Bethel to the west and Ai to the east. He built another altar to the LORD there and worshiped him."
    },
    "9": {
      "L": "And Abram journeyed on, still going toward the Negeb.",
      "M": "Then Abram set out and continued toward the Negev.",
      "T": "Then Abram continued his journey southward toward the Negev."
    },
    "10": {
      "L": "Now there was a famine in the land. So Abram went down to Egypt to sojourn there, for the famine was severe in the land.",
      "M": "Now there was a famine in the land, and Abram went down to Egypt to live there for a while because the famine was severe.",
      "T": "A severe famine struck the land, so Abram went down to Egypt to wait it out."
    },
    "11": {
      "L": "When he was about to enter Egypt, he said to Sarai his wife, 'I know that you are a woman beautiful in appearance,'",
      "M": "As he was about to enter Egypt, he said to his wife Sarai, 'I know what a beautiful woman you are.'",
      "T": "Just before entering Egypt, he said to his wife Sarai, 'You are a very beautiful woman.'"
    },
    "12": {
      "L": "'and when the Egyptians see you, they will say, \"This is his wife.\" Then they will kill me, but they will let you live.'",
      "M": "'When the Egyptians see you, they will say, \"This is his wife.\" Then they will kill me but will let you live.'",
      "T": "'When the Egyptians see you, they will say, \"She is his wife,\" and they will kill me to take you. But they will let you live.'"
    },
    "13": {
      "L": "'Say you are my sister, that it may go well with me because of you, and that my life may be spared for your sake.'",
      "M": "'Say you are my sister, so that I will be treated well for your sake and my life will be spared because of you.'",
      "T": "'Please say you are my sister, so things will go well for me and my life will be spared because of you.'"
    },
    "14": {
      "L": "When Abram entered Egypt, the Egyptians saw that the woman was very beautiful.",
      "M": "When Abram came to Egypt, the Egyptians saw that Sarai was a very beautiful woman.",
      "T": "When Abram entered Egypt, the Egyptians noticed that Sarai was very beautiful."
    },
    "15": {
      "L": "And when the princes of Pharaoh saw her, they praised her to Pharaoh. And the woman was taken into Pharaoh's house.",
      "M": "And when Pharaoh's officials saw her, they praised her to Pharaoh, and she was taken into his palace.",
      "T": "Pharaoh's officials saw her and told Pharaoh how beautiful she was, and she was brought into Pharaoh's palace."
    },
    "16": {
      "L": "And for her sake he dealt well with Abram; and he had sheep, oxen, male donkeys, male servants, female servants, female donkeys, and camels.",
      "M": "He treated Abram well for her sake, and Abram acquired sheep and cattle, male and female donkeys, male and female servants, and camels.",
      "T": "Pharaoh treated Abram well on her account, and Abram received sheep, cattle, donkeys, male and female servants, and camels."
    },
    "17": {
      "L": "But the LORD afflicted Pharaoh and his house with great plagues because of Sarai, Abram's wife.",
      "M": "But the LORD inflicted serious diseases on Pharaoh and his household because of Abram's wife Sarai.",
      "T": "But the LORD struck Pharaoh and his household with severe plagues because of Sarai, Abram's wife."
    },
    "18": {
      "L": "So Pharaoh called Abram and said, 'What is this you have done to me? Why did you not tell me that she was your wife?'",
      "M": "So Pharaoh summoned Abram. 'What have you done to me?' he said. 'Why didn't you tell me she was your wife?'",
      "T": "So Pharaoh summoned Abram. 'What have you done to me?' he demanded. 'Why didn't you tell me she was your wife?'"
    },
    "19": {
      "L": "'Why did you say, \"She is my sister,\" so that I took her for my wife? Now then, here is your wife; take her, and go.'",
      "M": "'Why did you say, \"She is my sister,\" so that I took her to be my wife? Now then, here is your wife. Take her and go!'",
      "T": "'Why did you say, \"She is my sister,\" so that I took her as my wife? Here is your wife—take her and leave!'"
    },
    "20": {
      "L": "And Pharaoh gave men orders concerning him, and they sent him away with his wife and all that he had.",
      "M": "Then Pharaoh gave orders about Abram to his men, and they sent him on his way, with his wife and everything he had.",
      "T": "Pharaoh gave orders to have Abram and his wife escorted out of the country, along with everything he owned."
    }
  },
  "13": {
    "1": {
      "L": "So Abram went up from Egypt, he and his wife and all that he had, and Lot with him, into the Negeb.",
      "M": "So Abram went up from Egypt to the Negev, with his wife and everything he had, and Lot went with him.",
      "T": "Abram left Egypt—he and his wife and all he owned, with Lot—and traveled back to the Negev."
    },
    "2": {
      "L": "Now Abram was very rich in livestock, in silver, and in gold.",
      "M": "Abram had become very wealthy in livestock and in silver and gold.",
      "T": "Abram was very wealthy—rich in livestock, silver, and gold."
    },
    "3": {
      "L": "And he journeyed on from the Negeb as far as Bethel to the place where his tent had been at the beginning, between Bethel and Ai,",
      "M": "From the Negev he went from place to place until he came to Bethel, to the place between Bethel and Ai where his tent had been earlier",
      "T": "From the Negev he traveled back, stopping along the way, until he reached Bethel—the very spot between Bethel and Ai where his tent had been before,"
    },
    "4": {
      "L": "to the place where he had made an altar at the first. And there Abram called upon the name of the LORD.",
      "M": "and where he had first built an altar. There Abram called on the name of the LORD.",
      "T": "where he had first built an altar. There Abram called on the name of the LORD."
    },
    "5": {
      "L": "And Lot, who went with Abram, also had flocks and herds and tents.",
      "M": "Now Lot, who was moving about with Abram, also had flocks and herds and tents.",
      "T": "Lot, who was traveling with Abram, also had large flocks and herds and his own tents."
    },
    "6": {
      "L": "And the land could not support both of them dwelling together, for their possessions were so great that they could not dwell together.",
      "M": "But the land could not support them while they stayed together, for their possessions were so great that they were not able to stay together.",
      "T": "The land could not support both of them together—they had so many animals and belongings that there was not enough room."
    },
    "7": {
      "L": "And there was strife between the herdsmen of Abram's livestock and the herdsmen of Lot's livestock. At that time the Canaanites and the Perizzites were dwelling in the land.",
      "M": "And quarreling arose between Abram's herders and Lot's herders. The Canaanites and Perizzites were also living in the land at that time.",
      "T": "Arguments broke out between Abram's herdsmen and Lot's herdsmen. The Canaanites and Perizzites were still living in the land at that time."
    },
    "8": {
      "L": "Then Abram said to Lot, 'Let there be no strife between you and me, and between your herdsmen and my herdsmen, for we are kinsmen.'",
      "M": "So Abram said to Lot, 'Let's not have any quarreling between you and me, or between your herders and mine, for we are close relatives.'",
      "T": "Abram said to Lot, 'Let's not allow any conflict between us or between our herdsmen—we are family.'"
    },
    "9": {
      "L": "'Is not the whole land before you? Separate yourself from me. If you take the left hand, then I will go to the right, or if you take the right hand, then I will go to the left.'",
      "M": "'Is not the whole land before you? Let's part company. If you go to the left, I'll go to the right; if you go to the right, I'll go to the left.'",
      "T": "'The whole land is spread out before us. Let's part ways. If you go left, I'll go right. If you go right, I'll go left.'"
    },
    "10": {
      "L": "And Lot lifted up his eyes and saw that the Jordan Valley was well watered everywhere like the garden of the LORD, like the land of Egypt, in the direction of Zoar. This was before the LORD destroyed Sodom and Gomorrah.",
      "M": "Lot looked around and saw that the whole plain of the Jordan toward Zoar was well watered, like the garden of the LORD, like the land of Egypt. This was before the LORD destroyed Sodom and Gomorrah.",
      "T": "Lot looked out and saw that the whole Jordan valley toward Zoar was lush and well-watered—like the garden of the LORD, like Egypt. This was before the LORD destroyed Sodom and Gomorrah."
    },
    "11": {
      "L": "So Lot chose for himself all the Jordan Valley, and Lot journeyed east. Thus they separated from each other.",
      "M": "So Lot chose for himself the whole plain of the Jordan and set out toward the east. The two men parted company:",
      "T": "So Lot chose the entire Jordan valley for himself and headed east. The two men went their separate ways:"
    },
    "12": {
      "L": "Abram settled in the land of Canaan, while Lot settled among the cities of the valley and moved his tent as far as Sodom.",
      "M": "Abram lived in the land of Canaan, while Lot lived among the cities of the plain and pitched his tents near Sodom.",
      "T": "Abram stayed in the land of Canaan, while Lot settled in the cities of the plain and pitched his tent near Sodom."
    },
    "13": {
      "L": "Now the men of Sodom were wicked, great sinners against the LORD.",
      "M": "Now the people of Sodom were wicked and were sinning greatly against the LORD.",
      "T": "Now the people of Sodom were deeply wicked—flagrant sinners against the LORD."
    },
    "14": {
      "L": "The LORD said to Abram, after Lot had separated from him, 'Lift up your eyes and look from the place where you are, northward and southward and eastward and westward,'",
      "M": "The LORD said to Abram after Lot had parted from him, 'Look around from where you are, to the north and south, to the east and west.'",
      "T": "After Lot had left, the LORD said to Abram, 'Look as far as you can in every direction—north, south, east, and west.'"
    },
    "15": {
      "L": "'for all the land that you see I will give to you and to your offspring forever.'",
      "M": "'All the land that you see I will give to you and your offspring forever.'",
      "T": "'I will give all the land you can see to you and your descendants—forever.'"
    },
    "16": {
      "L": "'I will make your offspring as the dust of the earth, so that if one can count the dust of the earth, your offspring also can be counted.'",
      "M": "'I will make your offspring like the dust of the earth, so that if anyone could count the dust, then your offspring could be counted.'",
      "T": "'I will give you descendants as countless as the dust of the earth—if anyone could count all the dust, they could count your descendants.'"
    },
    "17": {
      "L": "'Arise, walk through the length and the breadth of the land, for I will give it to you.'",
      "M": "'Go, walk through the length and breadth of the land, for I am giving it to you.'",
      "T": "'Now get up and walk the length and breadth of the land, for I am giving all of it to you.'"
    },
    "18": {
      "L": "So Abram moved his tent and came and settled by the oaks of Mamre, which are at Hebron, and there he built an altar to the LORD.",
      "M": "So Abram went to live near the great trees of Mamre at Hebron, where he pitched his tents. There he built an altar to the LORD.",
      "T": "So Abram moved his camp and settled near the great trees of Mamre at Hebron, and built an altar to the LORD there."
    }
  },
  "14": {
    "1": {
      "L": "In the days of Amraphel king of Shinar, Arioch king of Ellasar, Chedorlaomer king of Elam, and Tidal king of Goiim,",
      "M": "At the time of Amraphel king of Shinar, Arioch king of Ellasar, Kedorlaomer king of Elam and Tidal king of Goyim,",
      "T": "In the time of Amraphel king of Shinar, Arioch king of Ellasar, Chedorlaomer king of Elam, and Tidal king of Goiim—"
    },
    "2": {
      "L": "these kings made war with Bera king of Sodom, Birsha king of Gomorrah, Shinab king of Admah, Shemeber king of Zeboiim, and the king of Bela (that is, Zoar).",
      "M": "these kings went to war against Bera king of Sodom, Birsha king of Gomorrah, Shinab king of Admah, Shemeber king of Zeboyim, and the king of Bela (that is, Zoar).",
      "T": "these kings went to war against Bera king of Sodom, Birsha king of Gomorrah, Shinab king of Admah, Shemeber king of Zeboiim, and the king of Bela (that is, Zoar)."
    },
    "3": {
      "L": "All these joined forces in the Valley of Siddim (that is, the Salt Sea).",
      "M": "All these latter kings joined forces in the Valley of Siddim (that is, the Dead Sea Valley).",
      "T": "All five of these kings joined forces in the Valley of Siddim—the region that is now the Dead Sea."
    },
    "4": {
      "L": "Twelve years they had served Chedorlaomer, but in the thirteenth year they rebelled.",
      "M": "For twelve years they had been subject to Kedorlaomer, but in the thirteenth year they rebelled.",
      "T": "For twelve years they had been under Chedorlaomer's rule, but in the thirteenth year they rebelled."
    },
    "5": {
      "L": "In the fourteenth year Chedorlaomer and the kings who were with him came and defeated the Rephaim in Ashteroth-karnaim, the Zuzim in Ham, the Emim in Shaveh-kiriathaim,",
      "M": "In the fourteenth year, Kedorlaomer and the kings allied with him went out and defeated the Rephaites in Ashteroth Karnaim, the Zuzites in Ham, the Emites in Shaveh Kiriathaim,",
      "T": "In the fourteenth year, Chedorlaomer and his allied kings came and defeated the Rephaites at Ashteroth-karnaim, the Zuzites at Ham, the Emites at Shaveh-kiriathaim,"
    },
    "6": {
      "L": "and the Horites in their hill country of Seir as far as El-paran on the border of the wilderness.",
      "M": "and the Horites in the hill country of Seir, as far as El Paran near the desert.",
      "T": "and the Horites in their hill country of Seir, all the way to El-paran on the edge of the wilderness."
    },
    "7": {
      "L": "Then they turned back and came to En-mishpat (that is, Kadesh) and defeated all the country of the Amalekites, and also the Amorites who were dwelling in Hazazon-tamar.",
      "M": "Then they turned back and went to En Mishpat (that is, Kadesh), and they conquered the whole territory of the Amalekites, as well as the Amorites who were living in Hazezon Tamar.",
      "T": "Then they turned back and came to En-mishpat (that is, Kadesh) and crushed the Amalekites throughout their territory, as well as the Amorites living in Hazazon-tamar."
    },
    "8": {
      "L": "Then the king of Sodom, the king of Gomorrah, the king of Admah, the king of Zeboiim, and the king of Bela (that is, Zoar) went out, and they joined battle in the Valley of Siddim",
      "M": "Then the king of Sodom, the king of Gomorrah, the king of Admah, the king of Zeboyim and the king of Bela (that is, Zoar) marched out and drew up their battle lines in the Valley of Siddim",
      "T": "Then the king of Sodom, the king of Gomorrah, the king of Admah, the king of Zeboiim, and the king of Bela (Zoar) came out and drew up their forces in the Valley of Siddim"
    },
    "9": {
      "L": "against Chedorlaomer king of Elam, Tidal king of Goiim, Amraphel king of Shinar, and Arioch king of Ellasar, four kings against five.",
      "M": "against Kedorlaomer king of Elam, Tidal king of Goyim, Amraphel king of Shinar and Arioch king of Ellasar—four kings against five.",
      "T": "to fight Chedorlaomer king of Elam, Tidal king of Goiim, Amraphel king of Shinar, and Arioch king of Ellasar—four kings against five."
    },
    "10": {
      "L": "Now the Valley of Siddim was full of bitumen pits, and as the kings of Sodom and Gomorrah fled, some fell into them, and the rest fled to the hill country.",
      "M": "Now the Valley of Siddim was full of tar pits, and when the kings of Sodom and Gomorrah fled, some of the men fell into them and the rest fled to the hills.",
      "T": "The Valley of Siddim was riddled with tar pits, and as the kings of Sodom and Gomorrah fled, some fell into the pits while the others escaped to the hills."
    },
    "11": {
      "L": "So the enemy took all the possessions of Sodom and Gomorrah, and all their provisions, and went their way.",
      "M": "The four kings seized all the goods of Sodom and Gomorrah and all their food; then they went away.",
      "T": "The four kings seized all the goods and food of Sodom and Gomorrah and marched off."
    },
    "12": {
      "L": "They also took Lot, the son of Abram's brother, who was dwelling in Sodom, and his possessions, and went their way.",
      "M": "They also carried off Abram's nephew Lot and his possessions, since he was living in Sodom.",
      "T": "They also captured Lot, Abram's nephew who lived in Sodom, and took his possessions."
    },
    "13": {
      "L": "Then one who had escaped came and told Abram the Hebrew, who was living by the oaks of Mamre the Amorite, brother of Eshcol and of Aner. These were allies of Abram.",
      "M": "A man who had escaped came and reported this to Abram the Hebrew. Now Abram was living near the great trees of Mamre the Amorite, a brother of Eshkol and Aner, all of whom were allied with Abram.",
      "T": "A survivor escaped and brought the news to Abram the Hebrew, who was living near the great trees of Mamre the Amorite, a brother of Eshcol and Aner—all three were Abram's allies."
    },
    "14": {
      "L": "When Abram heard that his kinsman had been taken captive, he led forth his trained men, born in his house, 318 of them, and went in pursuit as far as Dan.",
      "M": "When Abram heard that his relative had been taken captive, he called out the 318 trained men born in his household and went in pursuit as far as Dan.",
      "T": "When Abram heard that his nephew had been captured, he mobilized 318 trained warriors born in his own household and pursued them all the way to Dan."
    },
    "15": {
      "L": "And he divided his forces against them by night, he and his servants, and defeated them and pursued them to Hobah, north of Damascus.",
      "M": "During the night Abram divided his men to attack them and he routed them, pursuing them as far as Hobah, north of Damascus.",
      "T": "That night he split his men into groups and launched a surprise attack, routing the enemy. He chased them as far as Hobah, north of Damascus."
    },
    "16": {
      "L": "Then he brought back all the possessions, and also brought back his kinsman Lot with his possessions, and the women and the people.",
      "M": "He recovered all the goods and brought back his relative Lot and his possessions, together with the women and the other people.",
      "T": "He recovered all the stolen goods and brought back his nephew Lot, along with the women and the other captives."
    },
    "17": {
      "L": "After his return from the defeat of Chedorlaomer and the kings who were with him, the king of Sodom went out to meet him at the Valley of Shaveh (that is, the King's Valley).",
      "M": "After Abram returned from defeating Kedorlaomer and the kings allied with him, the king of Sodom came out to meet him in the Valley of Shaveh (that is, the King's Valley).",
      "T": "After Abram returned from defeating Chedorlaomer and his allies, the king of Sodom went out to meet him in the Valley of Shaveh—the King's Valley."
    },
    "18": {
      "L": "And Melchizedek king of Salem brought out bread and wine. He was priest of God Most High.",
      "M": "Then Melchizedek king of Salem brought out bread and wine. He was priest of God Most High,",
      "T": "Then Melchizedek, king of Salem, brought out bread and wine. He was a priest of God Most High,"
    },
    "19": {
      "L": "And he blessed him and said, 'Blessed be Abram by God Most High, Possessor of heaven and earth;'",
      "M": "and he blessed Abram, saying, 'Blessed be Abram by God Most High, Creator of heaven and earth.'",
      "T": "and he blessed Abram with these words: 'Blessed be Abram by God Most High, Creator of heaven and earth.'"
    },
    "20": {
      "L": "'and blessed be God Most High, who has delivered your enemies into your hand!' And Abram gave him a tenth of everything.",
      "M": "'And praise be to God Most High, who delivered your enemies into your hand.' Then Abram gave him a tenth of everything.",
      "T": "'And praised be God Most High, who handed your enemies over to you!' Then Abram gave Melchizedek a tenth of everything he had recovered."
    },
    "21": {
      "L": "And the king of Sodom said to Abram, 'Give me the persons, but take the goods for yourself.'",
      "M": "The king of Sodom said to Abram, 'Give me the people and keep the goods for yourself.'",
      "T": "The king of Sodom said to Abram, 'Give me the people—you can keep all the goods for yourself.'"
    },
    "22": {
      "L": "But Abram said to the king of Sodom, 'I have lifted my hand to the LORD, God Most High, Possessor of heaven and earth,'",
      "M": "But Abram said to the king of Sodom, 'With raised hand I have sworn an oath to the LORD, God Most High, Creator of heaven and earth,'",
      "T": "But Abram replied to the king of Sodom, 'I swear with uplifted hand to the LORD, God Most High, Creator of heaven and earth—'"
    },
    "23": {
      "L": "'that I would not take a thread or a sandal strap or anything that is yours, lest you should say, \"I have made Abram rich.\"'",
      "M": "'that I will accept nothing belonging to you, not even a thread or the strap of a sandal, so that you will never be able to say, \"I made Abram rich.\"'",
      "T": "'that I will not take so much as a thread or a sandal strap from anything that belongs to you. I refuse to let you say, \"I made Abram wealthy.\"'"
    },
    "24": {
      "L": "'I will take nothing but what the young men have eaten, and the share of the men who went with me. Let Aner, Eshcol, and Mamre take their share.'",
      "M": "'I will accept nothing but what my men have eaten and the share that belongs to the men who went with me—to Aner, Eshkol and Mamre. Let them have their share.'",
      "T": "'I will only take what my men have already eaten. As for Aner, Eshcol, and Mamre who came with me—let them take their fair share.'"
    }
  },
  "15": {
    "1": {
      "L": "After these things the word of the LORD came to Abram in a vision: 'Fear not, Abram, I am your shield; your reward shall be very great.'",
      "M": "After this, the word of the LORD came to Abram in a vision: 'Do not be afraid, Abram. I am your shield, your very great reward.'",
      "T": "After all this, the word of the LORD came to Abram in a vision: 'Do not be afraid, Abram. I am your shield—your reward will be very great.'"
    },
    "2": {
      "L": "But Abram said, 'O Lord GOD, what will you give me, for I continue childless, and the heir of my house is Eliezer of Damascus?'",
      "M": "But Abram said, 'Sovereign LORD, what can you give me since I remain childless and the one who will inherit my estate is Eliezer of Damascus?'",
      "T": "But Abram said, 'Sovereign LORD, what good are your gifts when I have no children? My heir will be Eliezer of Damascus!'"
    },
    "3": {
      "L": "And Abram said, 'Behold, you have given me no offspring, and a member of my household will be my heir.'",
      "M": "And Abram said, 'You have given me no children; so a servant in my household will be my heir.'",
      "T": "Abram continued, 'You haven't given me any children, so a servant born in my household will inherit everything I have.'"
    },
    "4": {
      "L": "And behold, the word of the LORD came to him: 'This man shall not be your heir; your very own son shall be your heir.'",
      "M": "Then the word of the LORD came to him: 'This man will not be your heir, but a son who is your own flesh and blood will be your heir.'",
      "T": "Then the word of the LORD came to him: 'This man will not be your heir. Your own biological son will be your heir.'"
    },
    "5": {
      "L": "And he brought him outside and said, 'Look toward heaven, and number the stars, if you are able to number them.' Then he said to him, 'So shall your offspring be.'",
      "M": "He took him outside and said, 'Look up at the sky and count the stars—if indeed you can count them.' Then he said to him, 'So shall your offspring be.'",
      "T": "The LORD took him outside and said, 'Look up at the sky and count the stars—if you can.' Then he told him, 'Your descendants will be that numerous.'"
    },
    "6": {
      "L": "And he believed the LORD, and he counted it to him as righteousness.",
      "M": "Abram believed the LORD, and he credited it to him as righteousness.",
      "T": "Abram trusted the LORD, and the LORD counted that trust as righteousness."
    },
    "7": {
      "L": "And he said to him, 'I am the LORD who brought you out from Ur of the Chaldeans to give you this land to possess.'",
      "M": "He also said to him, 'I am the LORD, who brought you out of Ur of the Chaldeans to give you this land to take possession of it.'",
      "T": "Then God said to him, 'I am the LORD, who brought you out of Ur of the Chaldeans to give you this land as your possession.'"
    },
    "8": {
      "L": "But he said, 'O Lord GOD, how am I to know that I shall possess it?'",
      "M": "But Abram said, 'Sovereign LORD, how can I know that I will gain possession of it?'",
      "T": "But Abram asked, 'Sovereign LORD, how can I know that this land will actually be mine?'"
    },
    "9": {
      "L": "He said to him, 'Bring me a heifer three years old, a female goat three years old, a ram three years old, a turtledove, and a young pigeon.'",
      "M": "So the LORD said to him, 'Bring me a heifer, a goat and a ram, each three years old, along with a dove and a young pigeon.'",
      "T": "The LORD told him, 'Bring me a three-year-old cow, a three-year-old goat, and a three-year-old ram, along with a turtledove and a young pigeon.'"
    },
    "10": {
      "L": "And he brought him all these, cut them in half, and laid each half over against the other. But he did not cut the birds in half.",
      "M": "Abram brought all these to him, cut them in two and arranged the halves opposite each other; the birds, however, he did not cut in half.",
      "T": "Abram brought all these animals, split them down the middle, and laid each half across from the other—though he did not cut the birds in two."
    },
    "11": {
      "L": "And when birds of prey came down on the carcasses, Abram drove them away.",
      "M": "Then birds of prey came down on the carcasses, but Abram drove them away.",
      "T": "Vultures swooped down on the carcasses, but Abram drove them away."
    },
    "12": {
      "L": "As the sun was going down, a deep sleep fell on Abram. And behold, dreadful and great darkness fell upon him.",
      "M": "As the sun was setting, Abram fell into a deep sleep, and a thick and dreadful darkness came over him.",
      "T": "As the sun set, Abram fell into a deep sleep, and a thick, terrifying darkness came over him."
    },
    "13": {
      "L": "Then the LORD said to Abram, 'Know for certain that your offspring will be sojourners in a land that is not theirs and will be servants there, and they will be afflicted for four hundred years.'",
      "M": "Then the LORD said to him, 'Know for certain that for four hundred years your descendants will be strangers in a country not their own and that they will be enslaved and mistreated there.'",
      "T": "Then the LORD said to Abram, 'Know this for certain: your descendants will live as foreigners in a land that is not theirs, and they will be enslaved and oppressed for four hundred years.'"
    },
    "14": {
      "L": "'But I will bring judgment on the nation that they serve, and afterward they shall come out with great possessions.'",
      "M": "'But I will punish the nation they serve as slaves, and afterward they will come out with great possessions.'",
      "T": "'But I will punish the nation that enslaves them, and in the end your descendants will leave with great wealth.'"
    },
    "15": {
      "L": "'As for you, you shall go to your fathers in peace; you shall be buried in a good old age.'",
      "M": "'You, however, will go to your ancestors in peace and be buried at a good old age.'",
      "T": "'As for you—you will join your ancestors in peace and be buried at a ripe old age.'"
    },
    "16": {
      "L": "'And they shall come back here in the fourth generation, for the iniquity of the Amorites is not yet complete.'",
      "M": "'In the fourth generation your descendants will come back here, for the sin of the Amorites has not yet reached its full measure.'",
      "T": "'Your descendants will return here in the fourth generation, because the wickedness of the Amorites has not yet reached its full limit.'"
    },
    "17": {
      "L": "When the sun had gone down and it was dark, behold, a smoking fire pot and a flaming torch passed between these pieces.",
      "M": "When the sun had set and darkness had fallen, a smoking firepot with a blazing torch appeared and passed between the pieces.",
      "T": "After the sun had set and darkness had fallen, a smoking firepot and a blazing torch passed between the split carcasses."
    },
    "18": {
      "L": "On that day the LORD made a covenant with Abram, saying, 'To your offspring I give this land, from the river of Egypt to the great river, the river Euphrates,'",
      "M": "On that day the LORD made a covenant with Abram and said, 'To your descendants I give this land, from the Wadi of Egypt to the great river, the Euphrates—'",
      "T": "That very day the LORD made a covenant with Abram: 'I am giving this land to your descendants—from the Brook of Egypt all the way to the great Euphrates River—'"
    },
    "19": {
      "L": "'the land of the Kenites, the Kenizzites, the Kadmonites,'",
      "M": "'the land of the Kenites, Kenizzites, Kadmonites,'",
      "T": "'the land of the Kenites, Kenizzites, Kadmonites,'"
    },
    "20": {
      "L": "'the Hittites, the Perizzites, the Rephaim,'",
      "M": "'Hittites, Perizzites, Rephaites,'",
      "T": "'Hittites, Perizzites, Rephaites,'"
    },
    "21": {
      "L": "'the Amorites, the Canaanites, the Girgashites and the Jebusites.'",
      "M": "'Amorites, Canaanites, Girgashites and Jebusites.'",
      "T": "'Amorites, Canaanites, Girgashites, and Jebusites.'"
    }
  },
  "16": {
    "1": {
      "L": "Now Sarai, Abram's wife, had borne him no children. She had a female Egyptian servant whose name was Hagar.",
      "M": "Now Sarai, Abram's wife, had borne him no children. But she had an Egyptian slave named Hagar.",
      "T": "Sarai, Abram's wife, had given him no children. But she had an Egyptian servant named Hagar."
    },
    "2": {
      "L": "And Sarai said to Abram, 'Behold now, the LORD has prevented me from bearing children. Go in to my servant; it may be that I shall obtain children by her.' And Abram listened to the voice of Sarai.",
      "M": "So she said to Abram, 'The LORD has kept me from having children. Go, sleep with my slave; perhaps I can build a family through her.' Abram agreed to what Sarai said.",
      "T": "Sarai said to Abram, 'The LORD has prevented me from having children. Sleep with my servant—perhaps through her I can build a family.' Abram agreed."
    },
    "3": {
      "L": "So, after Abram had lived ten years in the land of Canaan, Sarai, Abram's wife, took Hagar the Egyptian, her servant, and gave her to Abram her husband as a wife.",
      "M": "So after Abram had been living in Canaan ten years, Sarai his wife took her Egyptian slave Hagar and gave her to her husband Abram to be his wife.",
      "T": "So after Abram had lived in Canaan for ten years, Sarai took her Egyptian servant Hagar and gave her to Abram as a wife."
    },
    "4": {
      "L": "And he went in to Hagar, and she conceived. And when she saw that she had conceived, she looked with contempt on her mistress.",
      "M": "He slept with Hagar, and she conceived. When she knew she was pregnant, she began to despise her mistress.",
      "T": "Abram slept with Hagar, and she became pregnant. When she realized she was pregnant, she began to look down on her mistress."
    },
    "5": {
      "L": "And Sarai said to Abram, 'May the wrong done to me be on you! I gave my servant to your embrace, and when she saw that she had conceived, she looked on me with contempt. May the LORD judge between you and me!'",
      "M": "Then Sarai said to Abram, 'You are responsible for the wrong I am suffering. I put my slave in your arms, and now that she knows she is pregnant, she despises me. May the LORD judge between you and me.'",
      "T": "Sarai said to Abram, 'This is your fault! I gave you my servant, and now that she is pregnant, she treats me with contempt. Let the LORD judge between us!'"
    },
    "6": {
      "L": "But Abram said to Sarai, 'Behold, your servant is in your power; do to her as you please.' Then Sarai dealt harshly with her, and she fled from her.",
      "M": "'Your slave is in your hands,' Abram said. 'Do with her whatever you think best.' Then Sarai mistreated Hagar; so she fled from her.",
      "T": "Abram replied, 'She is your servant—do whatever you think is right.' Then Sarai treated Hagar harshly, and Hagar ran away."
    },
    "7": {
      "L": "The angel of the LORD found her by a spring of water in the wilderness, the spring on the way to Shur.",
      "M": "The angel of the LORD found Hagar near a spring in the desert; it was the spring that is beside the road to Shur.",
      "T": "The angel of the LORD found her by a spring in the desert—the spring along the road to Shur."
    },
    "8": {
      "L": "And he said, 'Hagar, servant of Sarai, where have you come from and where are you going?' She said, 'I am fleeing from my mistress Sarai.'",
      "M": "And he said, 'Hagar, slave of Sarai, where have you come from, and where are you going?' 'I'm running away from my mistress Sarai,' she answered.",
      "T": "The angel asked, 'Hagar, servant of Sarai—where have you come from, and where are you going?' She answered, 'I am running away from my mistress Sarai.'"
    },
    "9": {
      "L": "The angel of the LORD said to her, 'Return to your mistress and submit to her.'",
      "M": "Then the angel of the LORD told her, 'Go back to your mistress and submit to her.'",
      "T": "The angel of the LORD told her, 'Go back to your mistress and submit to her authority.'"
    },
    "10": {
      "L": "The angel of the LORD also said to her, 'I will surely multiply your offspring so that they cannot be numbered for multitude.'",
      "M": "The angel added, 'I will increase your descendants so much that they will be too numerous to count.'",
      "T": "The angel also said, 'I will give you so many descendants they cannot be counted.'"
    },
    "11": {
      "L": "And the angel of the LORD said to her, 'Behold, you are pregnant and shall bear a son. You shall call his name Ishmael, because the LORD has listened to your affliction.'",
      "M": "The angel of the LORD also said to her: 'You are now pregnant and you will give birth to a son. You shall name him Ishmael, for the LORD has heard of your misery.'",
      "T": "The angel of the LORD told her, 'You are pregnant and will have a son. Name him Ishmael—meaning \"God hears\"—because the LORD has heard your cries of distress.'"
    },
    "12": {
      "L": "'He shall be a wild donkey of a man, his hand against everyone and everyone's hand against him, and he shall dwell over against all his kinsmen.'",
      "M": "'He will be a wild donkey of a man; his hand will be against everyone and everyone's hand against him, and he will live in hostility toward all his brothers.'",
      "T": "'He will be a wild and free man—fighting everyone and everyone fighting him—living at odds with all his relatives.'"
    },
    "13": {
      "L": "So she called the name of the LORD who spoke to her, 'You are a God of seeing,' for she said, 'Truly here I have seen him who looks after me.'",
      "M": "She gave this name to the LORD who spoke to her: 'You are the God who sees me,' for she said, 'I have now seen the One who sees me.'",
      "T": "She gave a name to the LORD who had spoken to her: 'You are the God who sees me.' She said, 'I have now seen the One who watches over me.'"
    },
    "14": {
      "L": "Therefore the well was called Beer-lahai-roi; it lies between Kadesh and Bered.",
      "M": "That is why the well was called Beer Lahai Roi; it is still there, between Kadesh and Bered.",
      "T": "That is why the well was named Beer-lahai-roi—the Well of the Living One Who Sees Me. It is still there, between Kadesh and Bered."
    },
    "15": {
      "L": "And Hagar bore Abram a son, and Abram called the name of his son, whom Hagar bore, Ishmael.",
      "M": "So Hagar bore Abram a son, and Abram gave the name Ishmael to the son she had borne.",
      "T": "Hagar gave birth to Abram's son, and Abram named him Ishmael."
    },
    "16": {
      "L": "Abram was 86 years old when Hagar bore Ishmael to Abram.",
      "M": "Abram was eighty-six years old when Hagar bore him Ishmael.",
      "T": "Abram was 86 years old when Ishmael was born."
    }
  },
  "17": {
    "1": {
      "L": "When Abram was 99 years old the LORD appeared to Abram and said to him, 'I am God Almighty; walk before me, and be blameless,'",
      "M": "When Abram was ninety-nine years old, the LORD appeared to him and said, 'I am God Almighty; walk before me faithfully and be blameless.'",
      "T": "When Abram was 99 years old, the LORD appeared to him and said, 'I am God Almighty. Live in my presence and be wholehearted.'"
    },
    "2": {
      "L": "'that I may make my covenant between me and you, and may multiply you greatly.'",
      "M": "'Then I will make my covenant between me and you and will greatly increase your numbers.'",
      "T": "'I will establish my covenant between us and multiply you beyond measure.'"
    },
    "3": {
      "L": "Then Abram fell on his face. And God said to him,",
      "M": "Abram fell facedown, and God said to him,",
      "T": "Abram fell face down, and God continued:"
    },
    "4": {
      "L": "'Behold, my covenant is with you, and you shall be the father of a multitude of nations.'",
      "M": "'As for me, this is my covenant with you: You will be the father of many nations.'",
      "T": "'As for me—this is my covenant with you: You will become the father of many nations.'"
    },
    "5": {
      "L": "'No longer shall your name be called Abram, but your name shall be Abraham, for I have made you the father of a multitude of nations.'",
      "M": "'No longer will you be called Abram; your name will be Abraham, for I have made you a father of many nations.'",
      "T": "'Your name will no longer be Abram. From now on your name is Abraham—because I am making you the father of many nations.'"
    },
    "6": {
      "L": "'I will make you very fruitful, and I will make you into nations, and kings shall come from you.'",
      "M": "'I will make you very fruitful; I will make nations of you, and kings will come from you.'",
      "T": "'I will make you extremely fruitful. Nations will descend from you, and kings will be among your descendants.'"
    },
    "7": {
      "L": "'And I will establish my covenant between me and you and your offspring after you throughout their generations for an everlasting covenant, to be God to you and to your offspring after you.'",
      "M": "'I will establish my covenant as an everlasting covenant between me and you and your descendants after you for the generations to come, to be your God and the God of your descendants after you.'",
      "T": "'I will confirm my covenant between me and you and your descendants throughout all generations—an eternal covenant. I will be your God and the God of your descendants after you.'"
    },
    "8": {
      "L": "'And I will give to you and to your offspring after you the land of your sojournings, all the land of Canaan, for an everlasting possession, and I will be their God.'",
      "M": "'The whole land of Canaan, where you now reside as a foreigner, I will give as an everlasting possession to you and your descendants after you; and I will be their God.'",
      "T": "'The whole land of Canaan—where you now live as a foreigner—I will give to you and your descendants as a permanent possession. And I will be their God.'"
    },
    "9": {
      "L": "And God said to Abraham, 'As for you, you shall keep my covenant, you and your offspring after you throughout their generations.'",
      "M": "Then God said to Abraham, 'As for you, you must keep my covenant, you and your descendants after you for the generations to come.'",
      "T": "God said to Abraham, 'As for your side of the covenant—you and your descendants must keep it, for all generations to come.'"
    },
    "10": {
      "L": "'This is my covenant, which you shall keep, between me and you and your offspring after you: Every male among you shall be circumcised.'",
      "M": "'This is my covenant with you and your descendants after you, the covenant you are to keep: Every male among you shall be circumcised.'",
      "T": "'This is the covenant you will keep between me and you and your descendants: Every male among you must be circumcised.'"
    },
    "11": {
      "L": "'You shall be circumcised in the flesh of your foreskins, and it shall be a sign of the covenant between me and you.'",
      "M": "'You are to undergo circumcision, and it will be the sign of the covenant between me and you.'",
      "T": "'You will circumcise the flesh of your foreskin—this will be the visible sign of the covenant between us.'"
    },
    "12": {
      "L": "'For the generations to come every male among you who is eight days old shall be circumcised, including the one born in your house or bought with your money from any foreigner who is not of your offspring.'",
      "M": "'For the generations to come every male among you who is eight days old must be circumcised, including those born in your household or bought with money from a foreigner—those who are not your offspring.'",
      "T": "'Throughout all your generations, every male child must be circumcised when he is eight days old—whether born in your household or purchased from a foreigner, anyone not of your blood.'"
    },
    "13": {
      "L": "'Both the one born in your house and the one bought with your money shall surely be circumcised. So shall my covenant be in your flesh an everlasting covenant.'",
      "M": "'Whether born in your household or bought with your money, they must be circumcised. My covenant in your flesh is to be an everlasting covenant.'",
      "T": "'Every male in your household—whether born there or bought—must be circumcised. My covenant will be marked in your flesh as a permanent commitment.'"
    },
    "14": {
      "L": "'Any uncircumcised male who is not circumcised in the flesh of his foreskin shall be cut off from his people; he has broken my covenant.'",
      "M": "'Any uncircumcised male, who has not been circumcised in the flesh, will be cut off from his people; he has broken my covenant.'",
      "T": "'Any male who is not circumcised will be cut off from the community—he has broken my covenant.'"
    },
    "15": {
      "L": "And God said to Abraham, 'As for Sarai your wife, you shall not call her name Sarai, but Sarah shall be her name.'",
      "M": "God also said to Abraham, 'As for Sarai your wife, you are no longer to call her Sarai; her name will be Sarah.'",
      "T": "God also said to Abraham, 'As for your wife Sarai—you are to call her Sarah from now on.'"
    },
    "16": {
      "L": "'I will bless her, and moreover, I will give you a son by her. I will bless her, and she shall become nations; kings of peoples shall come from her.'",
      "M": "'I will bless her and will surely give you a son by her. I will bless her so that she will be the mother of nations; kings of peoples will come from her.'",
      "T": "'I will bless her and give you a son through her. I will bless her, and she will become the mother of nations—kings of peoples will come from her.'"
    },
    "17": {
      "L": "Then Abraham fell on his face and laughed and said to himself, 'Shall a child be born to a man who is a hundred years old? Shall Sarah, who is ninety years old, bear a child?'",
      "M": "Abraham fell facedown; he laughed and said to himself, 'Will a son be born to a man a hundred years old? Will Sarah bear a child at the age of ninety?'",
      "T": "Abraham fell face down—and laughed to himself. 'Can a child be born to a hundred-year-old man?' he thought. 'Can Sarah have a child at ninety?'"
    },
    "18": {
      "L": "And Abraham said to God, 'Oh that Ishmael might live before you!'",
      "M": "And Abraham said to God, 'If only Ishmael might live under your blessing!'",
      "T": "Abraham said to God, 'Please—let Ishmael be enough! Let him live under your blessing!'"
    },
    "19": {
      "L": "God said, 'No, but Sarah your wife shall bear you a son, and you shall call his name Isaac. I will establish my covenant with him as an everlasting covenant for his offspring after him.'",
      "M": "Then God said, 'Yes, but your wife Sarah will bear you a son, and you will call him Isaac. I will establish my covenant with him as an everlasting covenant for his descendants after him.'",
      "T": "God said, 'No—Sarah your wife will bear you a son, and you will name him Isaac. I will establish my covenant with him as a permanent covenant for his descendants.'"
    },
    "20": {
      "L": "'As for Ishmael, I have heard you; behold, I have blessed him and will make him fruitful and multiply him greatly. He shall father twelve princes, and I will make him into a great nation.'",
      "M": "'And as for Ishmael, I have heard you: I will surely bless him; I will make him fruitful and will greatly increase his numbers. He will be the father of twelve rulers, and I will make him into a great nation.'",
      "T": "'As for Ishmael—I have heard you. I will bless him, make him fruitful, and multiply him greatly. He will father twelve rulers, and I will make him into a great nation.'"
    },
    "21": {
      "L": "'But I will establish my covenant with Isaac, whom Sarah shall bear to you at this time next year.'",
      "M": "'But my covenant I will establish with Isaac, whom Sarah will bear to you by this time next year.'",
      "T": "'But my covenant I will establish with Isaac, whom Sarah will bear to you at this time next year.'"
    },
    "22": {
      "L": "When he had finished talking with him, God went up from Abraham.",
      "M": "When he had finished speaking with Abraham, God went up from him.",
      "T": "When God had finished speaking with Abraham, he departed."
    },
    "23": {
      "L": "Then Abraham took Ishmael his son and all those born in his house or bought with his money, every male among the men of Abraham's house, and he circumcised the flesh of their foreskins that very day, as God had said to him.",
      "M": "On that very day Abraham took his son Ishmael and all those born in his household or bought with his money, every male in his household, and circumcised them, as God told him.",
      "T": "That very same day, Abraham circumcised his son Ishmael and every male in his household—whether born there or purchased—exactly as God had instructed."
    },
    "24": {
      "L": "Abraham was 99 years old when he was circumcised in the flesh of his foreskin.",
      "M": "Abraham was ninety-nine years old when he was circumcised.",
      "T": "Abraham was 99 years old when he was circumcised."
    },
    "25": {
      "L": "And Ishmael his son was 13 years old when he was circumcised in the flesh of his foreskin.",
      "M": "And his son Ishmael was thirteen when he was circumcised.",
      "T": "His son Ishmael was 13 years old when he was circumcised."
    },
    "26": {
      "L": "That very day Abraham and his son Ishmael were circumcised.",
      "M": "Abraham and his son Ishmael were both circumcised on that same day.",
      "T": "Abraham and his son Ishmael were both circumcised on the same day."
    },
    "27": {
      "L": "And all the men of his house, those born in the house and those bought with money from a foreigner, were circumcised with him.",
      "M": "And every male in Abraham's household, including those born in his household or bought from a foreigner, was circumcised with him.",
      "T": "Every male in Abraham's household—whether born there or purchased from foreigners—was circumcised with him."
    }
  },
  "18": {
    "1": {
      "L": "And the LORD appeared to him by the oaks of Mamre, as he sat at the door of his tent in the heat of the day.",
      "M": "The LORD appeared to Abraham near the great trees of Mamre while he was sitting at the entrance to his tent in the heat of the day.",
      "T": "The LORD appeared to Abraham near the great trees of Mamre while Abraham was sitting at the entrance of his tent during the heat of the day."
    },
    "2": {
      "L": "He lifted up his eyes and looked, and behold, three men were standing in front of him. When he saw them, he ran from the tent door to meet them and bowed himself to the earth",
      "M": "Abraham looked up and saw three men standing nearby. When he saw them, he hurried from the entrance of his tent to meet them and bowed low to the ground.",
      "T": "He looked up and saw three men standing nearby. When he saw them, he ran from the tent entrance to meet them and bowed down to the ground."
    },
    "3": {
      "L": "and said, 'O Lord, if I have found favor in your sight, do not pass by your servant.'",
      "M": "He said, 'If I have found favor in your eyes, my lord, do not pass your servant by.'",
      "T": "He said, 'My lord, if I have found favor with you, please don't pass your servant by.'"
    },
    "4": {
      "L": "'Let a little water be brought, and wash your feet, and rest yourselves under the tree,'",
      "M": "'Let a little water be brought, and then you may all wash your feet and rest under this tree.'",
      "T": "'Let me bring some water so you can wash your feet and rest in the shade of this tree.'"
    },
    "5": {
      "L": "'while I bring a morsel of bread, that you may refresh yourselves, and after that you may pass on—since you have come to your servant.' So they said, 'Do as you have said.'",
      "M": "'Let me get you something to eat, so you can be refreshed and then go on your way—now that you have come to your servant.' 'Very well,' they answered, 'do as you say.'",
      "T": "'Let me bring some food so you can eat and be refreshed before continuing on your way—since you have come to your servant.' They replied, 'Yes, do as you say.'"
    },
    "6": {
      "L": "So Abraham went quickly into the tent to Sarah and said, 'Quick! Three seahs of fine flour! Knead it, and make cakes.'",
      "M": "So Abraham hurried into the tent to Sarah. 'Quick,' he said, 'get three seahs of the finest flour and knead it and bake some bread.'",
      "T": "Abraham hurried into the tent to Sarah. 'Quickly,' he said, 'take three large measures of fine flour, knead it, and bake some bread!'"
    },
    "7": {
      "L": "And Abraham ran to the herd and took a calf, tender and good, and gave it to a young man, who prepared it quickly.",
      "M": "Then he ran to the herd and selected a choice, tender calf and gave it to a servant, who hurried to prepare it.",
      "T": "Then Abraham ran to the herd, selected a tender, choice calf, and gave it to a servant, who quickly prepared it."
    },
    "8": {
      "L": "Then he took curds and milk and the calf that he had prepared, and set it before them. And he stood by them under the tree while they ate.",
      "M": "He then brought some curds and milk and the calf that had been prepared, and set these before them. While they ate, he stood near them under a tree.",
      "T": "He brought curds, milk, and the roasted calf and set the food before them. He stood nearby under the tree while they ate."
    },
    "9": {
      "L": "They said to him, 'Where is Sarah your wife?' And he said, 'She is in the tent.'",
      "M": "'Where is your wife Sarah?' they asked him. 'There, in the tent,' he said.",
      "T": "They asked him, 'Where is your wife Sarah?' He replied, 'She is there in the tent.'"
    },
    "10": {
      "L": "The LORD said, 'I will surely return to you about this time next year, and Sarah your wife shall have a son.' And Sarah was listening at the tent door behind him.",
      "M": "Then one of them said, 'I will surely return to you about this time next year, and Sarah your wife will have a son.' Now Sarah was listening at the entrance to the tent, which was behind him.",
      "T": "Then the LORD said, 'I will certainly return to you at this same time next year, and your wife Sarah will have a son.' Sarah was listening at the tent entrance behind him."
    },
    "11": {
      "L": "Now Abraham and Sarah were old, advanced in years. The way of women had ceased to be with Sarah.",
      "M": "Abraham and Sarah were already very old, and Sarah was past the age of childbearing.",
      "T": "Abraham and Sarah were both very old, and Sarah had long since stopped having her monthly periods."
    },
    "12": {
      "L": "So Sarah laughed to herself, saying, 'After I am worn out, and my lord is old, shall I have pleasure?'",
      "M": "So Sarah laughed to herself as she thought, 'After I am worn out and my lord is old, will I now have this pleasure?'",
      "T": "Sarah laughed silently to herself and thought, 'After I have grown old, and my husband is old, am I going to have a baby?'"
    },
    "13": {
      "L": "The LORD said to Abraham, 'Why did Sarah laugh and say, \"Shall I indeed bear a child, now that I am old?\"'",
      "M": "Then the LORD said to Abraham, 'Why did Sarah laugh and say, \"Will I really have a child, now that I am old?\"'",
      "T": "The LORD said to Abraham, 'Why did Sarah laugh and ask, \"Can I really have a child now that I am old?\"'"
    },
    "14": {
      "L": "'Is anything too hard for the LORD? At the appointed time I will return to you, about this time next year, and Sarah shall have a son.'",
      "M": "'Is anything too hard for the LORD? I will return to you at the appointed time next year, and Sarah will have a son.'",
      "T": "'Is anything too hard for the LORD? I will return to you at the promised time next year, and Sarah will have a son.'"
    },
    "15": {
      "L": "But Sarah denied it, saying, 'I did not laugh,' for she was afraid. He said, 'No, but you did laugh.'",
      "M": "Sarah was afraid, so she lied and said, 'I did not laugh.' But he said, 'Yes, you did laugh.'",
      "T": "Sarah was afraid, so she denied it: 'I didn't laugh.' But he said, 'Yes, you did.'"
    },
    "16": {
      "L": "Then the men set out from there, and they looked down toward Sodom. And Abraham went with them to set them on their way.",
      "M": "When the men got up to leave, they looked down toward Sodom, and Abraham walked along with them to see them on their way.",
      "T": "When the men rose to leave, they looked down toward Sodom. Abraham walked with them to see them off."
    },
    "17": {
      "L": "The LORD said, 'Shall I hide from Abraham what I am about to do,'",
      "M": "Then the LORD said, 'Shall I hide from Abraham what I am about to do?'",
      "T": "The LORD thought, 'Should I hide from Abraham what I am about to do?'"
    },
    "18": {
      "L": "'seeing that Abraham shall surely become a great and mighty nation, and all the nations of the earth shall be blessed in him?'",
      "M": "'Abraham will surely become a great and powerful nation, and all nations on earth will be blessed through him.'",
      "T": "'Abraham will certainly become a great and powerful nation, and all the nations of the earth will be blessed through him.'"
    },
    "19": {
      "L": "'For I have chosen him, that he may command his children and his household after him to keep the way of the LORD by doing righteousness and justice, so that the LORD may bring to Abraham what he has promised him.'",
      "M": "'For I have chosen him, so that he will direct his children and his household after him to keep the way of the LORD by doing what is right and just, so that the LORD will bring about for Abraham what he has promised him.'",
      "T": "'I have singled him out so that he will instruct his children and household after him to follow the way of the LORD—doing what is right and just—so that I can fulfill everything I have promised him.'"
    },
    "20": {
      "L": "Then the LORD said, 'Because the outcry against Sodom and Gomorrah is great and their sin is very grave,'",
      "M": "Then the LORD said, 'The outcry against Sodom and Gomorrah is so great and their sin so grievous'",
      "T": "The LORD continued, 'The outcry against Sodom and Gomorrah is deafening, and their sin is overwhelming.'"
    },
    "21": {
      "L": "'I will go down to see whether they have done altogether according to the outcry that has come to me. And if not, I will know.'",
      "M": "'that I will go down and see if what they have done is as bad as the outcry that has reached me. If not, I will know.'",
      "T": "'I will go down and see for myself whether what they have done matches the outcry that has reached me. If not, I will know.'"
    },
    "22": {
      "L": "So the men turned from there and went toward Sodom, but Abraham still stood before the LORD.",
      "M": "The men turned away and went toward Sodom, but Abraham remained standing before the LORD.",
      "T": "The two men turned and headed toward Sodom, but Abraham remained standing before the LORD."
    },
    "23": {
      "L": "Then Abraham drew near and said, 'Will you indeed sweep away the righteous with the wicked?'",
      "M": "Then Abraham approached him and said: 'Will you sweep away the righteous with the wicked?'",
      "T": "Then Abraham stepped forward and asked, 'Are you really going to destroy the righteous along with the wicked?'"
    },
    "24": {
      "L": "'Suppose there are fifty righteous within the city. Will you then sweep away the place and not spare it for the fifty righteous who are in it?'",
      "M": "'What if there are fifty righteous people in the city? Will you really sweep it away and not spare the place for the sake of the fifty righteous people in it?'",
      "T": "'Suppose there are fifty righteous people in the city—will you still destroy it and not spare it for the sake of those fifty?'"
    },
    "25": {
      "L": "'Far be it from you to do such a thing, to put the righteous to death with the wicked, so that the righteous fare as the wicked! Far be that from you! Shall not the Judge of all the earth do what is just?'",
      "M": "'Far be it from you to do such a thing—to kill the righteous with the wicked, treating the righteous and the wicked alike. Far be it from you! Will not the Judge of all the earth do right?'",
      "T": "'Far be it from you to do such a thing—killing the righteous along with the wicked, treating them both the same way! Far be it from you! Should not the Judge of all the earth act justly?'"
    },
    "26": {
      "L": "And the LORD said, 'If I find at Sodom fifty righteous in the city, I will spare the whole place for their sake.'",
      "M": "The LORD said, 'If I find fifty righteous people in the city of Sodom, I will spare the whole place for their sake.'",
      "T": "The LORD said, 'If I find fifty righteous people in Sodom, I will spare the whole city for their sake.'"
    },
    "27": {
      "L": "Abraham answered and said, 'Behold, I have undertaken to speak to the Lord, I who am but dust and ashes.'",
      "M": "Then Abraham spoke up again: 'Now that I have been so bold as to speak to the Lord, though I am nothing but dust and ashes,'",
      "T": "Abraham responded, 'I am being bold to speak to the Lord—I who am nothing but dust and ashes.'"
    },
    "28": {
      "L": "'Suppose five of the fifty righteous are lacking. Will you destroy the whole city for lack of five?' And he said, 'I will not destroy it if I find forty-five there.'",
      "M": "'what if the number of the righteous is five less than fifty? Will you destroy the whole city for lack of five people?' 'If I find forty-five there,' he said, 'I will not destroy it.'",
      "T": "'What if the fifty are five short? Will you destroy the whole city for lack of five?' He answered, 'If I find forty-five, I will not destroy it.'"
    },
    "29": {
      "L": "Again he spoke to him and said, 'Suppose forty are found there.' He answered, 'For the sake of forty I will not do it.'",
      "M": "Once again he spoke to him, 'What if only forty are found there?' He said, 'For the sake of forty, I will not do it.'",
      "T": "Abraham pressed again: 'What if only forty are found there?' God said, 'For the sake of forty, I will not do it.'"
    },
    "30": {
      "L": "Then he said, 'Oh let not the Lord be angry, and I will speak. Suppose thirty are found there.' He answered, 'I will not do it, if I find thirty there.'",
      "M": "Then Abraham said, 'May the Lord not be angry, but let me speak. What if only thirty can be found there?' He answered, 'I will not do it if I find thirty there.'",
      "T": "Abraham said, 'Please don't be angry, Lord, while I speak again. What if only thirty are found?' He answered, 'I will not do it if I find thirty.'"
    },
    "31": {
      "L": "He said, 'Behold, I have undertaken to speak to the Lord. Suppose twenty are found there.' He answered, 'For the sake of twenty I will not destroy it.'",
      "M": "Abraham said, 'Now that I have been so bold as to speak to the Lord, what if only twenty can be found there?' He said, 'For the sake of twenty, I will not destroy it.'",
      "T": "Abraham said, 'I am being very bold to speak to the Lord—what if only twenty are found?' God said, 'For the sake of twenty, I will not destroy it.'"
    },
    "32": {
      "L": "Then he said, 'Oh let not the Lord be angry, and I will speak again but this once. Suppose ten are found there.' He answered, 'For the sake of ten I will not destroy it.'",
      "M": "Then he said, 'May the Lord not be angry, but let me speak just once more. What if only ten can be found there?' He answered, 'For the sake of ten, I will not destroy it.'",
      "T": "Abraham said, 'Please don't be angry, Lord—let me ask just one more time. What if only ten are found?' He answered, 'For the sake of ten, I will not destroy it.'"
    },
    "33": {
      "L": "And the LORD went his way, when he had finished speaking to Abraham, and Abraham returned to his place.",
      "M": "When the LORD had finished speaking with Abraham, he left, and Abraham returned home.",
      "T": "When the LORD had finished speaking with Abraham, he departed, and Abraham returned home."
    }
  },
  "19": {
    "1": {
      "L": "The two angels came to Sodom in the evening, and Lot was sitting in the gate of Sodom. When Lot saw them, he rose to meet them and bowed himself with his face to the earth",
      "M": "The two angels arrived at Sodom in the evening, and Lot was sitting in the gateway of the city. When he saw them, he got up to meet them and bowed down with his face to the ground.",
      "T": "The two angels arrived at Sodom in the evening, and Lot was sitting at the city gate. When he saw them, he got up to meet them and bowed down with his face to the ground."
    },
    "2": {
      "L": "and said, 'My lords, please turn aside to your servant's house and spend the night and wash your feet. Then you may rise up early and go on your way.' They said, 'No; we will spend the night in the town square.'",
      "M": "He said, 'My lords, please turn aside to your servant's house. You can wash your feet and spend the night and then go on your way early in the morning.' 'No,' they answered, 'we will spend the night in the square.'",
      "T": "He said, 'My lords, please come to my house and spend the night. You can wash your feet and leave early in the morning.' 'No,' they said, 'we will spend the night in the town square.'"
    },
    "3": {
      "L": "But he pressed them strongly; so they turned aside to him and entered his house. And he made them a feast and baked unleavened bread, and they ate.",
      "M": "But he insisted so strongly that they did go with him and entered his house. He prepared a meal for them, baking bread without yeast, and they ate.",
      "T": "But Lot urged them so strongly that they agreed to come with him. He prepared a meal for them and baked bread without yeast, and they ate."
    },
    "4": {
      "L": "But before they lay down, the men of the city, the men of Sodom, both young and old, all the people to the last man, surrounded the house.",
      "M": "Before they had gone to bed, all the men from every part of the city of Sodom—both young and old—surrounded the house.",
      "T": "Before they went to bed, the men of the city—every man from every part of Sodom, young and old—surrounded Lot's house."
    },
    "5": {
      "L": "And they called to Lot, 'Where are the men who came to you tonight? Bring them out to us, that we may know them.'",
      "M": "They called to Lot, 'Where are the men who came to you tonight? Bring them out to us so that we can have sex with them.'",
      "T": "They shouted to Lot, 'Where are the men who came to you tonight? Send them out so we can have relations with them!'"
    },
    "6": {
      "L": "Lot went out to the men at the entrance, shut the door after him,",
      "M": "Lot went outside to meet them and shut the door behind him",
      "T": "Lot went outside to them and shut the door behind him."
    },
    "7": {
      "L": "and said, 'I beg you, my brothers, do not act so wickedly.'",
      "M": "and said, 'No, my friends. Don't do this wicked thing.'",
      "T": "He said, 'Please, friends—don't do such a wicked thing!'"
    },
    "8": {
      "L": "'Behold, I have two daughters who have not known any man. Let me bring them out to you, and do to them as you please. Only do nothing to these men, for they have come under the shelter of my roof.'",
      "M": "'Look, I have two daughters who have never slept with a man. Let me bring them out to you, and you can do what you like with them. But don't do anything to these men, for they have come under the protection of my roof.'",
      "T": "'I have two daughters who have never been with a man. Let me bring them out to you, and you may do with them as you wish. But don't touch these men—they are under my protection.'"
    },
    "9": {
      "L": "'Stand back!' And they said, 'This fellow came to sojourn, and he has become the judge! Now we will deal worse with you than with them.' Then they pressed hard against the man Lot, and drew near to break the door.",
      "M": "'Get out of our way,' they replied. 'This fellow came here as a foreigner, and now he wants to play the judge! We'll treat you worse than them.' They kept bringing pressure on Lot and moved forward to break down the door.",
      "T": "'Get out of our way!' they shouted. 'This outsider came here to live among us, and now he thinks he can tell us what to do! We'll treat you worse than them!' They pressed hard against Lot and moved to break down the door."
    },
    "10": {
      "L": "But the men reached out their hands and brought Lot into the house with them and shut the door.",
      "M": "But the men inside reached out and pulled Lot back into the house and shut the door.",
      "T": "But the men inside reached out, pulled Lot back into the house, and bolted the door."
    },
    "11": {
      "L": "And they struck the men who were at the entrance of the house with blindness, both small and great, so that they wore themselves out groping for the door.",
      "M": "Then they struck the men who were at the door of the house, young and old, with blindness so that they could not find the door.",
      "T": "Then they struck all the men at the entrance with blindness—young and old—so that they exhausted themselves trying to find the door."
    },
    "12": {
      "L": "Then the men said to Lot, 'Have you anyone else here? Sons-in-law, sons, daughters, or anyone you have in the city, bring them out of the place.'",
      "M": "The two men said to Lot, 'Do you have anyone else here—sons-in-law, sons or daughters, or anyone else in the city who belongs to you? Get them out of here,'",
      "T": "The two men asked Lot, 'Do you have anyone else here? Sons-in-law, sons, daughters—anyone in the city who belongs to you? Get them out of here!'"
    },
    "13": {
      "L": "'For we are about to destroy this place, because the outcry against its people has become great before the LORD, and the LORD has sent us to destroy it.'",
      "M": "'because we are going to destroy this place. The outcry to the LORD against its people is so great that he has sent us to destroy it.'",
      "T": "'We are about to destroy this city. The outcry against it has reached the LORD, and he has sent us to destroy it.'"
    },
    "14": {
      "L": "So Lot went out and said to his sons-in-law, who were to marry his daughters, 'Up! Get out of this place, for the LORD is about to destroy the city.' But he seemed to his sons-in-law to be jesting.",
      "M": "So Lot went out and spoke to his sons-in-law, who were pledged to marry his daughters. He said, 'Hurry and get out of this place, because the LORD is about to destroy the city!' But his sons-in-law thought he was joking.",
      "T": "So Lot went out and spoke to his sons-in-law, who were engaged to his daughters. He said, 'Get out of this city! The LORD is going to destroy it!' But they thought he was joking."
    },
    "15": {
      "L": "As morning dawned, the angels urged Lot, saying, 'Up! Take your wife and your two daughters who are here, lest you be swept away in the punishment of the city.'",
      "M": "With the coming of dawn, the angels urged Lot, saying, 'Hurry! Take your wife and your two daughters who are here, or you will be swept away when the city is punished.'",
      "T": "As dawn broke, the angels urged Lot, 'Hurry—take your wife and your two daughters and leave, or you will be swept away with the city when it is punished!'"
    },
    "16": {
      "L": "But he lingered. So the men seized him and his wife and his two daughters by the hand, the LORD being merciful to him, and they brought him out and set him outside the city.",
      "M": "When he hesitated, the men grasped his hand and the hands of his wife and of his two daughters and led them safely out of the city, for the LORD was merciful to them.",
      "T": "But Lot hesitated. So the men grabbed him by the hand—and his wife and two daughters as well—the LORD showing them mercy, and led them out to safety outside the city."
    },
    "17": {
      "L": "And as they brought them out, one said, 'Escape for your life. Do not look back or stop anywhere in the valley. Escape to the hills, lest you be swept away.'",
      "M": "As soon as they had brought them out, one of them said, 'Flee for your lives! Don't look back, and don't stop anywhere in the plain! Flee to the mountains or you will be swept away!'",
      "T": "As soon as they were outside, one of them said, 'Run for your lives! Don't look back—don't stop anywhere on the plain! Flee to the mountains, or you will die!'"
    },
    "18": {
      "L": "And Lot said to them, 'Oh, no, my lords.'",
      "M": "But Lot said to them, 'No, my lords, please!'",
      "T": "But Lot pleaded, 'No, my lords, please!'"
    },
    "19": {
      "L": "'Behold, your servant has found favor in your sight, and you have shown me great kindness in saving my life. But I cannot escape to the hills, lest the disaster overtake me and I die.'",
      "M": "'Your servant has found favor in your eyes, and you have shown great kindness to me in sparing my life. But I can't flee to the mountains; this disaster will overtake me, and I'll die.'",
      "T": "'You have been so gracious to me—saving my life. But I can't make it to the mountains! The disaster will overtake me and I'll die!'"
    },
    "20": {
      "L": "'Behold, this city is near enough to flee to, and it is a little one. Let me escape there—is it not a little one?—and my life will be saved!'",
      "M": "'Look, here is a town near enough to run to, and it is small. Let me flee to it—it is very small, isn't it? Then my life will be spared.'",
      "T": "'Look—that little town is close enough to reach. Let me flee there—it is only a small place. Please let me escape there, and my life will be spared!'"
    },
    "21": {
      "L": "He said to him, 'Behold, I grant you this favor also, that I will not overthrow the city of which you have spoken.'",
      "M": "He said to him, 'Very well, I will grant this request too; I will not overthrow the town you speak of.'",
      "T": "The angel replied, 'Very well, I grant your request. I will not destroy the town you mentioned.'"
    },
    "22": {
      "L": "'Escape there quickly, for I can do nothing until you arrive there.' Therefore the name of the city was called Zoar.",
      "M": "'But flee there quickly, because I cannot do anything until you reach it.' That is why the town was called Zoar.",
      "T": "'But hurry—flee there quickly, because I cannot do anything until you arrive.' That is why the town is called Zoar."
    },
    "23": {
      "L": "The sun had risen on the earth when Lot came to Zoar.",
      "M": "By the time Lot reached Zoar, the sun had risen over the land.",
      "T": "The sun was rising when Lot arrived at Zoar."
    },
    "24": {
      "L": "Then the LORD rained on Sodom and Gomorrah sulfur and fire from the LORD out of heaven.",
      "M": "Then the LORD rained down burning sulfur on Sodom and Gomorrah—from the LORD out of the heavens.",
      "T": "Then the LORD rained down burning sulfur on Sodom and Gomorrah—fire from the LORD out of the sky."
    },
    "25": {
      "L": "And he overthrew those cities, and all the valley, and all the inhabitants of the cities, and what grew on the ground.",
      "M": "Thus he overthrew those cities and the entire plain, destroying all those living in the cities—and also the vegetation in the land.",
      "T": "He destroyed those cities and the whole plain, all the inhabitants of the cities, and everything growing in the ground."
    },
    "26": {
      "L": "But Lot's wife, behind him, looked back, and she became a pillar of salt.",
      "M": "But Lot's wife looked back, and she became a pillar of salt.",
      "T": "But Lot's wife looked back, and she was turned into a pillar of salt."
    },
    "27": {
      "L": "And Abraham went early in the morning to the place where he had stood before the LORD.",
      "M": "Early the next morning Abraham got up and returned to the place where he had stood before the LORD.",
      "T": "Early the next morning, Abraham returned to the place where he had stood before the LORD."
    },
    "28": {
      "L": "And he looked down toward Sodom and Gomorrah and toward all the land of the valley, and he looked and, behold, the smoke of the land went up like the smoke of a furnace.",
      "M": "He looked down toward Sodom and Gomorrah, toward all the land of the plain, and he saw dense smoke rising from the land, like smoke from a furnace.",
      "T": "He looked out over Sodom and Gomorrah and across the whole plain—and saw thick smoke rising like smoke from a great furnace."
    },
    "29": {
      "L": "So it was that, when God destroyed the cities of the valley, God remembered Abraham and sent Lot out of the midst of the overthrow when he overthrew the cities in which Lot had lived.",
      "M": "So when God destroyed the cities of the plain, he remembered Abraham, and he brought Lot out of the catastrophe that overthrew the cities where Lot had lived.",
      "T": "When God destroyed the cities of the plain, he remembered Abraham, and he brought Lot out safely when he overthrew the cities where Lot had been living."
    },
    "30": {
      "L": "Now Lot went up out of Zoar and lived in the hills with his two daughters, for he was afraid to live in Zoar. So he lived in a cave with his two daughters.",
      "M": "Lot and his two daughters left Zoar and settled in the mountains, for he was afraid to stay in Zoar. He and his two daughters lived in a cave.",
      "T": "Lot left Zoar and went to live in the hills with his two daughters—he was afraid to stay in Zoar. He and his daughters lived in a cave."
    },
    "31": {
      "L": "And the firstborn said to the younger, 'Our father is old, and there is not a man on earth to come in to us after the manner of all the earth.'",
      "M": "One day the older daughter said to the younger, 'Our father is old, and there is no man around here to give us children—as is the custom all over the earth.'",
      "T": "One day the older daughter said to the younger, 'Our father is getting old, and there are no men around here to marry us and continue our family line.'"
    },
    "32": {
      "L": "'Come, let us make our father drink wine, and we will lie with him, that we may preserve offspring from our father.'",
      "M": "'Let's get our father to drink wine and then sleep with him and preserve our family line through our father.'",
      "T": "'Let's get our father drunk and sleep with him, so we can have children through him and keep our family going.'"
    },
    "33": {
      "L": "So they made their father drink wine that night. And the firstborn went in and lay with her father. He did not know when she lay down or when she arose.",
      "M": "That night they got their father to drink wine, and the older daughter went in and slept with him. He was not aware of it when she lay down or when she got up.",
      "T": "That night they got their father drunk on wine, and the older daughter went and slept with him. He was not aware of it when she lay down or when she got up."
    },
    "34": {
      "L": "The next day, the firstborn said to the younger, 'Behold, I lay last night with my father. Let us make him drink wine tonight also, and you go in and lie with him, that we may preserve offspring from our father.'",
      "M": "The next day the older daughter said to the younger, 'Last night I slept with my father. Let's get him to drink wine again tonight, and you go in and sleep with him so we can preserve our family line through our father.'",
      "T": "The next day the older said to the younger, 'I slept with Father last night. Let's get him drunk again tonight, and you go in and sleep with him, so we can preserve our family through him.'"
    },
    "35": {
      "L": "So they made their father drink wine that night also, and the younger arose and lay with him. And he did not know when she lay down or when she arose.",
      "M": "So they got their father to drink wine that night also, and the younger daughter went in and slept with him. Again he was not aware of it when she lay down or when she got up.",
      "T": "So they got their father drunk again that night, and the younger daughter slept with him. He was not aware of it when she lay down or when she got up."
    },
    "36": {
      "L": "Thus both the daughters of Lot became pregnant by their father.",
      "M": "So both of Lot's daughters became pregnant by their father.",
      "T": "Both of Lot's daughters became pregnant by their father."
    },
    "37": {
      "L": "The firstborn bore a son and called his name Moab. He is the father of the Moabites to this day.",
      "M": "The older daughter had a son, and she named him Moab; he is the father of the Moabites of today.",
      "T": "The older daughter had a son and named him Moab—he became the ancestor of the Moabites of today."
    },
    "38": {
      "L": "The younger also bore a son and called his name Ben-ammi. He is the father of the Ammonites to this day.",
      "M": "The younger daughter also had a son, and she named him Ben-Ammi; he is the father of the Ammonites of today.",
      "T": "The younger also had a son and named him Ben-ammi—he became the ancestor of the Ammonites of today."
    }
  },
  "20": {
    "1": {
      "L": "From there Abraham journeyed toward the territory of the Negeb and lived between Kadesh and Shur; and he sojourned in Gerar.",
      "M": "Now Abraham moved on from there into the region of the Negev and lived between Kadesh and Shur. For a while he stayed in Gerar,",
      "T": "From there Abraham traveled to the Negev region and settled between Kadesh and Shur. For a time he lived in Gerar,"
    },
    "2": {
      "L": "And Abraham said of Sarah his wife, 'She is my sister.' And Abimelech king of Gerar sent and took Sarah.",
      "M": "and there Abraham said of his wife Sarah, 'She is my sister.' Then Abimelech king of Gerar sent for Sarah and took her.",
      "T": "and there Abraham told people about Sarah his wife, 'She is my sister.' So Abimelech king of Gerar had Sarah brought to him."
    },
    "3": {
      "L": "But God came to Abimelech in a dream by night and said to him, 'Behold, you are a dead man because of the woman whom you have taken, for she is a man's wife.'",
      "M": "But God came to Abimelech in a dream one night and said to him, 'You are as good as dead because of the woman you have taken; she is a married woman.'",
      "T": "But God came to Abimelech in a dream that night and said, 'You are a dead man because of the woman you have taken—she is someone's wife!'"
    },
    "4": {
      "L": "Now Abimelech had not approached her. So he said, 'Lord, will you kill an innocent people?'",
      "M": "Now Abimelech had not gone near her, so he said, 'Lord, will you destroy an innocent nation?'",
      "T": "But Abimelech had not yet touched her, so he said, 'Lord, will you destroy an innocent man?'"
    },
    "5": {
      "L": "'Did he not himself say to me, \"She is my sister\"? And she herself said, \"He is my brother.\" In the integrity of my heart and the innocence of my hands I have done this.'",
      "M": "'Did he not say to me, \"She is my sister,\" and didn't she also say, \"He is my brother\"? I have done this with a clear conscience and clean hands.'",
      "T": "'He told me, \"She is my sister,\" and she herself said, \"He is my brother.\" I did this with a clean conscience and innocent hands.'"
    },
    "6": {
      "L": "Then God said to him in the dream, 'Yes, I know that you have done this in the integrity of your heart, and it was I who kept you from sinning against me. Therefore I did not let you touch her.'",
      "M": "Then God said to him in the dream, 'Yes, I know you did this with a clear conscience, and so I have kept you from sinning against me. That is why I did not let you touch her.'",
      "T": "God said to him in the dream, 'Yes, I know you did this with a clear conscience—that is why I stopped you from sinning against me. I did not let you touch her.'"
    },
    "7": {
      "L": "'Now then, return the man's wife, for he is a prophet, so that he will pray for you, and you shall live. But if you do not return her, know that you shall surely die, you and all who are yours.'",
      "M": "'Now return the man's wife, for he is a prophet, and he will pray for you and you will live. But if you do not return her, you may be sure that you and all who belong to you will die.'",
      "T": "'Now return the man's wife—he is a prophet, and he will pray for you, and you will live. But if you do not return her, know that you will certainly die—you and all your household.'"
    },
    "8": {
      "L": "So Abimelech rose early in the morning and called all his servants and told them all these things. And the men were very much afraid.",
      "M": "Early the next morning Abimelech summoned all his officials and when he told them all that had happened, they were very much afraid.",
      "T": "Early the next morning Abimelech called all his officials together and told them what had happened, and they were terrified."
    },
    "9": {
      "L": "Then Abimelech called Abraham and said to him, 'What have you done to us? And how have I sinned against you, that you have brought on me and my kingdom a great sin? You have done to me things that ought not to be done.'",
      "M": "Then Abimelech called Abraham in and said, 'What have you done to us? How have I wronged you that you have brought such great guilt upon me and my kingdom? You have done things to me that should never be done.'",
      "T": "Then Abimelech summoned Abraham. 'What have you done to us?' he demanded. 'How have I wronged you that you would bring such terrible guilt on me and my kingdom? What you have done to me is inexcusable!'"
    },
    "10": {
      "L": "And Abimelech said to Abraham, 'What did you see, that you did this thing?'",
      "M": "Abimelech also asked Abraham, 'What was your reason for doing this?'",
      "T": "Abimelech also asked, 'What made you do this?'"
    },
    "11": {
      "L": "Abraham said, 'I did it because I thought, \"There is no fear of God at all in this place, and they will kill me because of my wife.\"'",
      "M": "Abraham replied, 'I said to myself, \"There is surely no fear of God in this place, and they will kill me because of my wife.\"'",
      "T": "Abraham replied, 'I thought, \"There is surely no respect for God in this place. They will kill me to get my wife.\"'"
    },
    "12": {
      "L": "'Besides, she is indeed my sister, the daughter of my father though not the daughter of my mother, and she became my wife.'",
      "M": "'Besides, she really is my sister, the daughter of my father though not of my mother; and she became my wife.'",
      "T": "'Besides, she really is my half-sister—we have the same father but different mothers—and she became my wife.'"
    },
    "13": {
      "L": "'And when God caused me to wander from my father's house, I said to her, \"This is the kindness you must do me: at every place to which we come, say of me, \"He is my brother.\"\"'",
      "M": "'And when God had me wander from my father's household, I said to her, \"This is how you can show your love to me: Everywhere we go, say of me, \"He is my brother.\"\"'",
      "T": "'When God sent me traveling far from my father's home, I said to her, \"Do me this favor: wherever we go, say that I am your brother.\"'"
    },
    "14": {
      "L": "Then Abimelech took sheep and oxen, and male servants and female servants, and gave them to Abraham, and returned Sarah his wife to him.",
      "M": "Then Abimelech brought sheep and cattle and male and female slaves and gave them to Abraham, and he returned Sarah his wife to him.",
      "T": "Then Abimelech brought sheep, cattle, and male and female servants, gave them to Abraham, and returned Sarah to him."
    },
    "15": {
      "L": "And Abimelech said, 'Behold, my land is before you; dwell where it pleases you.'",
      "M": "And Abimelech said, 'My land is before you; live wherever you like.'",
      "T": "Abimelech said, 'My land is open to you—settle wherever you please.'"
    },
    "16": {
      "L": "To Sarah he said, 'Behold, I have given your brother a thousand pieces of silver. It is a sign of your innocence in the eyes of all who are with you, and before everyone you are vindicated.'",
      "M": "To Sarah he said, 'I am giving your brother a thousand shekels of silver. This is to cover the offense against you before all who are with you; you are completely vindicated.'",
      "T": "To Sarah he said, 'I am giving your brother a thousand pieces of silver—this is to clear your reputation before everyone with you. You are completely vindicated.'"
    },
    "17": {
      "L": "Then Abraham prayed to God, and God healed Abimelech, and also healed his wife and female servants so that they bore children.",
      "M": "Then Abraham prayed to God, and God healed Abimelech, his wife and his female slaves so they could have children again,",
      "T": "Then Abraham prayed to God, and God healed Abimelech, his wife, and his female servants so that they could have children again."
    },
    "18": {
      "L": "For the LORD had closed all the wombs of the house of Abimelech because of Sarah, Abraham's wife.",
      "M": "for the LORD had kept all the women in Abimelech's household from conceiving because of Abraham's wife Sarah.",
      "T": "For the LORD had closed every womb in Abimelech's household because of Abraham's wife Sarah."
    }
  }
}

for tier, key in [('literal','L'), ('mediating','M'), ('thought','T')]:
    data = load(tier, 'genesis')
    merge_tier(data, GENESIS, key)
    save(tier, 'genesis', data)

print('\nGenesis 11–20 written to all three tiers.')
print('Chapters covered:', sorted(GENESIS.keys(), key=int))
