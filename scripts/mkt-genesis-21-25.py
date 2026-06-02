"""
MKT Genesis chapters 21–25 — three-tier translation written directly to draft JSON files.

Covers:
  21 — Birth of Isaac; Hagar and Ishmael sent away; treaty with Abimelech at Beer-sheba
  22 — The Akedah: God tests Abraham; the binding and release of Isaac
  23 — Death of Sarah; Abraham purchases Machpelah from the Hittites
  24 — Abraham's servant finds Rebekah for Isaac (longest chapter: 67 verses)
  25 — Abraham's death; Ishmael's line; birth of Jacob and Esau; Esau sells his birthright

Contested-term decisions embedded here (all glossary entries remain "draft"):
  H3068 יהוה — L/M: "LORD", T: "the LORD" (personal name noted in Akedah T-tier commentary)
  H430  אֱלֹהִים — L/M/T: "God" (theologically singular throughout these chapters)
  H2617 חֶסֶד — L/M: "steadfast love", T: "faithful love" / "loyal love" (ch 24 prayer passages)
  H5315 נֶפֶשׁ — rendered contextually: "life" for animate self, not Greek immaterial soul
  H1285 בְּרִית — "covenant" throughout; ch 21 highlights oath-bond structure
  H4397 מַלְאַךְ — "angel" (T), "messenger" (L) in ch 21/22

Run: python3 scripts/mkt-genesis-21-25.py
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

# ── Translation data ───────────────────────────────────────────────────────────

GENESIS = {

# ══════════════════════════════════════════════════════════════════════════════
# Chapter 21 — Isaac's birth; Hagar expelled; covenant with Abimelech
# ══════════════════════════════════════════════════════════════════════════════
"21": {
  "1": {
    "L": "And the LORD visited Sarah as he had said, and the LORD did to Sarah as he had spoken.",
    "M": "Now the LORD was gracious to Sarah as he had said, and the LORD did for Sarah what he had promised.",
    "T": "The LORD kept his word to Sarah—exactly what he had promised, he now fulfilled."
  },
  "2": {
    "L": "And Sarah conceived and bore Abraham a son in his old age, at the appointed time of which God had spoken to him.",
    "M": "Sarah became pregnant and bore a son to Abraham in his old age, at the very time God had promised him.",
    "T": "Sarah conceived and gave birth to a son for Abraham in his old age—at the precise time God had said."
  },
  "3": {
    "L": "And Abraham called the name of his son who was born to him, whom Sarah bore him, Isaac.",
    "M": "Abraham gave the name Isaac to the son Sarah bore him.",
    "T": "Abraham named the boy Isaac—'He Laughs'—the son Sarah had borne him."
  },
  "4": {
    "L": "And Abraham circumcised his son Isaac when he was eight days old, as God had commanded him.",
    "M": "When his son Isaac was eight days old, Abraham circumcised him, as God had commanded him.",
    "T": "Abraham circumcised Isaac when the boy was eight days old, just as God had commanded."
  },
  "5": {
    "L": "And Abraham was a hundred years old when his son Isaac was born to him.",
    "M": "Abraham was a hundred years old when his son Isaac was born to him.",
    "T": "Abraham was one hundred years old when Isaac was born."
  },
  "6": {
    "L": "And Sarah said, 'God has made laughter for me; everyone who hears will laugh over me.'",
    "M": "Sarah said, 'God has brought me laughter, and everyone who hears about this will laugh with me.'",
    "T": "Sarah said, 'God has given me reason to laugh! Everyone who hears this will laugh with me.'"
  },
  "7": {
    "L": "And she said, 'Who would have said to Abraham that Sarah would nurse children? Yet I have borne him a son in his old age.'",
    "M": "She also said, 'Who would have said to Abraham that Sarah would nurse children? Yet I have borne him a son in his old age.'",
    "T": "'Who could have imagined telling Abraham that Sarah would nurse a child? Yet I have given him a son in his old age!'"
  },
  "8": {
    "L": "And the child grew and was weaned. And Abraham made a great feast on the day that Isaac was weaned.",
    "M": "The child grew and was weaned, and on the day Isaac was weaned Abraham held a great feast.",
    "T": "The child grew and was weaned, and Abraham threw a great celebration the day Isaac was weaned."
  },
  "9": {
    "L": "But Sarah saw the son of Hagar the Egyptian, whom she had borne to Abraham, laughing.",
    "M": "But Sarah saw that the son whom Hagar the Egyptian had borne to Abraham was mocking.",
    "T": "But Sarah watched Ishmael—the son Hagar the Egyptian had borne to Abraham—laughing and mocking."
  },
  "10": {
    "L": "So she said to Abraham, 'Cast out this slave woman with her son, for the son of this slave woman shall not be heir with my son Isaac.'",
    "M": "She said to Abraham, 'Get rid of that slave woman and her son, for that woman's son will never share in the inheritance with my son Isaac.'",
    "T": "She said to Abraham, 'Drive out this slave woman and her son! The son of a slave must not share the inheritance with my son Isaac.'"
  },
  "11": {
    "L": "And the thing was very displeasing to Abraham on account of his son.",
    "M": "The matter distressed Abraham greatly because it concerned his son.",
    "T": "This was deeply distressing to Abraham—Ishmael was his son."
  },
  "12": {
    "L": "But God said to Abraham, 'Be not displeased on account of the boy and on account of your slave woman. Whatever Sarah says to you, do as she tells you, for through Isaac shall your offspring be named.'",
    "M": "But God said to him, 'Do not be so distressed about the boy and your slave woman. Listen to whatever Sarah tells you, because it is through Isaac that your offspring will be reckoned.'",
    "T": "But God said to Abraham, 'Do not be troubled about the boy or your slave woman. Do what Sarah says—it is through Isaac that your descendants will carry your name.'"
  },
  "13": {
    "L": "'And I will make a nation of the son of the slave woman also, because he is your offspring.'",
    "M": "'I will make the son of the slave woman into a nation also, because he is your offspring.'",
    "T": "'I will also make a great nation from the slave woman's son, because he too is your child.'"
  },
  "14": {
    "L": "So Abraham rose early in the morning and took bread and a skin of water and gave it to Hagar, putting it on her shoulder, along with the child, and sent her away. And she departed and wandered in the wilderness of Beersheba.",
    "M": "Early the next morning Abraham took some food and a skin of water and gave them to Hagar. He set them on her shoulders and then sent her off with the boy. She went on her way and wandered in the Desert of Beersheba.",
    "T": "Early the next morning Abraham packed bread and a waterskin for Hagar, placed them on her shoulders, handed her the boy, and sent them away. She wandered off into the wilderness of Beersheba."
  },
  "15": {
    "L": "When the water in the skin was gone, she put the child under one of the bushes.",
    "M": "When the water in the skin was gone, she put the boy under one of the bushes.",
    "T": "When the water was used up, she pushed the boy into the shade of a shrub"
  },
  "16": {
    "L": "Then she went and sat down opposite him a good way off, about the distance of a bowshot, for she said, 'Let me not look on the death of the child.' And as she sat opposite him, she lifted up her voice and wept.",
    "M": "Then she went off and sat down about a bowshot away, for she thought, 'I cannot watch the boy die.' And as she sat there, she began to sob.",
    "T": "and walked away—about a bowshot's distance—and sat down, because she could not bear to watch him die. She sat there and wept aloud."
  },
  "17": {
    "L": "And God heard the voice of the boy, and the angel of God called to Hagar from heaven and said to her, 'What troubles you, Hagar? Fear not, for God has heard the voice of the boy where he is.'",
    "M": "God heard the boy crying, and the angel of God called to Hagar from heaven and said, 'What is the matter, Hagar? Do not be afraid; God has heard the boy crying as he lies there.'",
    "T": "God heard the boy's crying, and the messenger of God called to Hagar from heaven: 'What is wrong, Hagar? Do not be afraid—God has heard the boy crying where he lies.'"
  },
  "18": {
    "L": "'Arise, lift up the boy, and hold him fast with your hand, for I will make him into a great nation.'",
    "M": "'Lift the boy up and take him by the hand, for I will make him into a great nation.'",
    "T": "'Get up, take the boy by the hand—I will make him into a great nation.'"
  },
  "19": {
    "L": "Then God opened her eyes, and she saw a well of water. And she went and filled the skin with water and gave the boy a drink.",
    "M": "Then God opened her eyes and she saw a well of water. So she went and filled the skin with water and gave the boy a drink.",
    "T": "Then God opened her eyes and she saw a spring of water. She filled the waterskin and gave the boy a drink."
  },
  "20": {
    "L": "And God was with the boy, and he grew up. He lived in the wilderness and became an expert with the bow.",
    "M": "God was with the boy as he grew up. He lived in the desert and became an archer.",
    "T": "God was with Ishmael as he grew up. He settled in the wilderness and became a skilled archer."
  },
  "21": {
    "L": "He lived in the wilderness of Paran, and his mother took a wife for him from the land of Egypt.",
    "M": "While he was living in the Desert of Paran, his mother got a wife for him from Egypt.",
    "T": "He settled in the wilderness of Paran, and his mother arranged for him to marry a woman from Egypt."
  },
  "22": {
    "L": "At that time Abimelech and Phicol the commander of his army said to Abraham, 'God is with you in all that you do.'",
    "M": "At that time Abimelek and Phicol the commander of his forces said to Abraham, 'God is with you in everything you do.'",
    "T": "Around that time Abimelech and his military commander Phicol came to Abraham and said, 'God is clearly with you in everything you do.'"
  },
  "23": {
    "L": "'Now therefore swear to me here by God that you will not deal falsely with me or with my descendants or with my posterity, but as I have dealt kindly with you, you will deal with me and with the land where you have sojourned.'",
    "M": "'Now swear to me here before God that you will not deal falsely with me or my children or my descendants. Show to me and the country where you now reside as a foreigner the same kindness I have shown to you.'",
    "T": "'So swear to me before God right now that you will not deceive me or my children or my descendants. Show me the same loyalty I have shown you during your time in my land.'"
  },
  "24": {
    "L": "And Abraham said, 'I will swear.'",
    "M": "Abraham said, 'I swear it.'",
    "T": "Abraham said, 'I swear it.'"
  },
  "25": {
    "L": "When Abraham reproved Abimelech about a well of water that Abimelech's servants had seized,",
    "M": "Then Abraham complained to Abimelek about a well of water that Abimelek's servants had seized.",
    "T": "Then Abraham brought up a grievance—a well that Abimelech's servants had taken by force."
  },
  "26": {
    "L": "Abimelech said, 'I do not know who has done this thing; you did not tell me, and I have not heard of it until today.'",
    "M": "But Abimelek said, 'I don't know who did this. You did not tell me, and I heard about it only today.'",
    "T": "Abimelech replied, 'I have no idea who did that. You never told me, and I only learned of it today.'"
  },
  "27": {
    "L": "So Abraham took sheep and oxen and gave them to Abimelech, and the two men made a covenant.",
    "M": "So Abraham brought sheep and cattle and gave them to Abimelek, and the two men made a treaty.",
    "T": "Abraham brought sheep and cattle and gave them to Abimelech, and the two men made a covenant together."
  },
  "28": {
    "L": "Abraham set seven ewe lambs of the flock apart.",
    "M": "Abraham set apart seven ewe lambs from the flock,",
    "T": "Then Abraham separated seven young ewes from the flock,"
  },
  "29": {
    "L": "And Abimelech said to Abraham, 'What is the meaning of these seven ewe lambs that you have set apart?'",
    "M": "and Abimelek asked Abraham, 'What is the meaning of these seven ewe lambs you have set apart by themselves?'",
    "T": "and Abimelech asked him, 'What are these seven ewes you have set aside?'"
  },
  "30": {
    "L": "He said, 'These seven ewe lambs you will take from my hand, that this may be a witness for me that I dug this well.'",
    "M": "He replied, 'Accept these seven lambs from my hand as a witness that I dug this well.'",
    "T": "He answered, 'Accept these seven ewes as my witness that I dug this well.'"
  },
  "31": {
    "L": "Therefore that place was called Beersheba, because there both of them swore an oath.",
    "M": "So that place was called Beersheba, because the two men swore an oath there.",
    "T": "That place was named Beersheba — 'Well of the Oath' — because both men swore an oath there."
  },
  "32": {
    "L": "So they made a covenant at Beersheba. Then Abimelech and Phicol the commander of his army rose up and returned to the land of the Philistines.",
    "M": "After the covenant had been made at Beersheba, Abimelek and Phicol the commander of his forces returned to the land of the Philistines.",
    "T": "The covenant was sealed at Beersheba. Then Abimelech and his commander Phicol returned to the land of the Philistines."
  },
  "33": {
    "L": "Abraham planted a tamarisk tree in Beersheba and called there on the name of the LORD, the Everlasting God.",
    "M": "Abraham planted a tamarisk tree in Beersheba, and there he called on the name of the LORD, the Eternal God.",
    "T": "Abraham planted a tamarisk tree at Beersheba and there called on the name of the LORD, El Olam — the God of Eternity."
  },
  "34": {
    "L": "And Abraham sojourned many days in the land of the Philistines.",
    "M": "And Abraham stayed in the land of the Philistines for a long time.",
    "T": "Abraham lived as a resident alien in the Philistines' land for many years."
  }
},

# ══════════════════════════════════════════════════════════════════════════════
# Chapter 22 — The Akedah: the binding of Isaac
# ══════════════════════════════════════════════════════════════════════════════
"22": {
  "1": {
    "L": "After these things God tested Abraham and said to him, 'Abraham!' And he said, 'Here I am.'",
    "M": "Some time later God tested Abraham. He said to him, 'Abraham!' 'Here I am,' he replied.",
    "T": "After all this, God put Abraham to the test. He called, 'Abraham!' Abraham answered, 'Here I am.'"
  },
  "2": {
    "L": "'Take your son, your only son Isaac, whom you love, and go to the land of Moriah, and offer him there as a burnt offering on one of the mountains of which I shall tell you.'",
    "M": "'Take your son, your only son, whom you love—Isaac—and go to the region of Moriah. Sacrifice him there as a burnt offering on a mountain I will show you.'",
    "T": "'Take your son—your only son, Isaac, the one you love—and go to the land of Moriah. Offer him there as a burnt offering on one of the mountains I will point out to you.'"
  },
  "3": {
    "L": "So Abraham rose early in the morning, saddled his donkey, and took two of his young men with him, and his son Isaac. And he cut the wood for the burnt offering and arose and went to the place of which God had told him.",
    "M": "Early the next morning Abraham got up and loaded his donkey. He took with him two of his servants and his son Isaac. When he had cut enough wood for the burnt offering, he set out for the place God had told him about.",
    "T": "Abraham rose early the next morning, saddled his donkey, and set off with two servants and his son Isaac. He had cut the wood for the offering beforehand. They headed for the place God had told him."
  },
  "4": {
    "L": "On the third day Abraham lifted up his eyes and saw the place from afar.",
    "M": "On the third day Abraham looked up and saw the place in the distance.",
    "T": "On the third day Abraham looked up and could see the place in the distance."
  },
  "5": {
    "L": "Then Abraham said to his young men, 'Stay here with the donkey; I and the boy will go over there and worship and come again to you.'",
    "M": "He said to his servants, 'Stay here with the donkey while I and the boy go over there. We will worship and then we will come back to you.'",
    "T": "He told his servants, 'Stay here with the donkey. The boy and I will go on ahead, worship, and then come back to you.'"
  },
  "6": {
    "L": "And Abraham took the wood of the burnt offering and laid it on Isaac his son. And he took in his hand the fire and the knife. So they went both of them together.",
    "M": "Abraham took the wood for the burnt offering and placed it on his son Isaac, and he himself carried the fire and the knife. As the two of them went on together,",
    "T": "Abraham loaded the firewood on Isaac's shoulders, while he himself carried the flame and the knife. The two of them walked on together."
  },
  "7": {
    "L": "And Isaac said to his father Abraham, 'My father!' And he said, 'Here I am, my son.' He said, 'Behold, the fire and the wood, but where is the lamb for a burnt offering?'",
    "M": "Isaac spoke up and said to his father Abraham, 'Father?' 'Yes, my son?' Abraham replied. 'The fire and wood are here,' Isaac said, 'but where is the lamb for the burnt offering?'",
    "T": "Isaac spoke up: 'Father?' 'Yes, my son?' 'We have the fire and the wood,' said Isaac, 'but where is the lamb for the offering?'"
  },
  "8": {
    "L": "Abraham said, 'God will provide for himself the lamb for a burnt offering, my son.' So they went both of them together.",
    "M": "Abraham answered, 'God himself will provide the lamb for the burnt offering, my son.' And the two of them went on together.",
    "T": "Abraham answered, 'God himself will see to the lamb for the offering, my son.' And the two of them walked on together."
  },
  "9": {
    "L": "When they came to the place of which God had told him, Abraham built the altar there and laid the wood in order and bound Isaac his son and laid him on the altar, on top of the wood.",
    "M": "When they reached the place God had told him about, Abraham built an altar there and arranged the wood on it. He bound his son Isaac and laid him on the altar, on top of the wood.",
    "T": "They came to the place God had shown him. Abraham built the altar, arranged the wood, then bound his son Isaac and laid him on the altar on top of the wood."
  },
  "10": {
    "L": "Then Abraham reached out his hand and took the knife to slaughter his son.",
    "M": "Then he reached out his hand and took the knife to slay his son.",
    "T": "Abraham reached out and took the knife to slay his son."
  },
  "11": {
    "L": "But the angel of the LORD called to him from heaven and said, 'Abraham, Abraham!' And he said, 'Here I am.'",
    "M": "But the angel of the LORD called out to him from heaven, 'Abraham! Abraham!' 'Here I am,' he replied.",
    "T": "But the messenger of the LORD called out from heaven: 'Abraham! Abraham!' He said, 'Here I am.'"
  },
  "12": {
    "L": "'Do not lay your hand on the boy or do anything to him, for now I know that you fear God, seeing you have not withheld your son, your only son, from me.'",
    "M": "'Do not do anything to him. Now I know that you fear God, because you have not withheld from me your son, your only son.'",
    "T": "'Do not touch the boy—do nothing to him. Now I know that you truly fear God, because you did not hold back your son, your only son, from me.'"
  },
  "13": {
    "L": "And Abraham lifted up his eyes and looked, and behold, behind him was a ram, caught in a thicket by his horns. And Abraham went and took the ram and offered it up as a burnt offering instead of his son.",
    "M": "Abraham looked up and there in a thicket he saw a ram caught by its horns. He went over and took the ram and sacrificed it as a burnt offering instead of his son.",
    "T": "Abraham looked up and saw a ram caught by its horns in a thicket. He went and took it and offered it as a burnt offering in place of his son."
  },
  "14": {
    "L": "So Abraham called the name of that place, 'The LORD will provide'; as it is said to this day, 'On the mount of the LORD it shall be provided.'",
    "M": "So Abraham called that place 'The LORD Will Provide.' And to this day it is said, 'On the mountain of the LORD it will be provided.'",
    "T": "Abraham named that place 'Yahweh-Yireh' — 'The LORD Provides.' And to this day people say, 'On the mountain of the LORD it will be seen to.'"
  },
  "15": {
    "L": "And the angel of the LORD called to Abraham a second time from heaven",
    "M": "The angel of the LORD called to Abraham from heaven a second time",
    "T": "The messenger of the LORD called to Abraham from heaven a second time"
  },
  "16": {
    "L": "and said, 'By myself I have sworn, declares the LORD, because you have done this thing and have not withheld your son, your only son,'",
    "M": "and said, 'I swear by myself, declares the LORD, that because you have done this and have not withheld your son, your only son,'",
    "T": "and said, 'I swear by myself — this is the LORD's own oath — because you have done this and have not held back your son, your only son:'"
  },
  "17": {
    "L": "'I will surely bless you, and I will surely multiply your offspring as the stars of heaven and as the sand that is on the seashore. And your offspring shall possess the gate of his enemies,'",
    "M": "'I will surely bless you and make your descendants as numerous as the stars in the sky and as the sand on the seashore. Your descendants will take possession of the cities of their enemies,'",
    "T": "'I will bless you greatly and multiply your descendants like the stars of the sky and the sand on the seashore. Your descendants will conquer the cities of their enemies,'"
  },
  "18": {
    "L": "'and in your offspring shall all the nations of the earth be blessed, because you have obeyed my voice.'",
    "M": "'and through your offspring all nations on earth will be blessed, because you have obeyed me.'",
    "T": "'and through your descendants all nations of the earth will be blessed — because you obeyed me.'"
  },
  "19": {
    "L": "So Abraham returned to his young men, and they arose and went together to Beersheba. And Abraham lived at Beersheba.",
    "M": "Then Abraham returned to his servants, and they set off together for Beersheba. And Abraham stayed in Beersheba.",
    "T": "Abraham rejoined his servants, and they set off together for Beersheba. Abraham settled at Beersheba."
  },
  "20": {
    "L": "Now after these things it was told to Abraham, 'Behold, Milcah also has borne children to your brother Nahor:'",
    "M": "Some time later Abraham was told, 'Milcah is also a mother; she has borne sons to your brother Nahor:'",
    "T": "After these events, word came to Abraham: 'Milcah has also borne children to your brother Nahor:'"
  },
  "21": {
    "L": "Uz his firstborn, Buz his brother, Kemuel the father of Aram,",
    "M": "Uz the firstborn, Buz his brother, Kemuel the father of Aram,",
    "T": "Uz the firstborn, then his brother Buz, and Kemuel the father of Aram,"
  },
  "22": {
    "L": "Chesed, Hazo, Pildash, Jidlaph, and Bethuel.",
    "M": "Kesed, Hazo, Pildash, Jidlaph and Bethuel.",
    "T": "Chesed, Hazo, Pildash, Jidlaph, and Bethuel."
  },
  "23": {
    "L": "Bethuel fathered Rebekah. These eight Milcah bore to Nahor, Abraham's brother.",
    "M": "Bethuel became the father of Rebekah. Milcah bore these eight sons to Abraham's brother Nahor.",
    "T": "Bethuel became the father of Rebekah. These eight Milcah bore to Nahor, Abraham's brother."
  },
  "24": {
    "L": "Moreover, his concubine, whose name was Reumah, bore Tebah, Gaham, Tahash, and Maacah.",
    "M": "His concubine, whose name was Reumah, also had sons: Tebah, Gaham, Tahash and Maakah.",
    "T": "His concubine Reumah also bore sons: Tebah, Gaham, Tahash, and Maacah."
  }
},

# ══════════════════════════════════════════════════════════════════════════════
# Chapter 23 — Death of Sarah; purchase of the cave of Machpelah
# ══════════════════════════════════════════════════════════════════════════════
"23": {
  "1": {
    "L": "Sarah lived 127 years; these were the years of the life of Sarah.",
    "M": "Sarah lived to be a hundred and twenty-seven years old.",
    "T": "Sarah lived to be one hundred and twenty-seven years old."
  },
  "2": {
    "L": "And Sarah died at Kiriath-arba, that is, Hebron, in the land of Canaan, and Abraham went in to mourn for Sarah and to weep for her.",
    "M": "She died at Kiriath Arba (that is, Hebron) in the land of Canaan, and Abraham went to mourn for Sarah and to weep over her.",
    "T": "She died at Kiriath-arba, that is Hebron, in the land of Canaan. Abraham came to mourn for Sarah and to weep over her."
  },
  "3": {
    "L": "And Abraham rose up from before his dead and said to the Hittites,",
    "M": "Then Abraham rose from beside his dead wife and spoke to the Hittites.",
    "T": "Then Abraham rose from beside his dead wife and spoke to the Hittites:"
  },
  "4": {
    "L": "'I am a sojourner and foreigner among you; give me property among you for a burying place, that I may bury my dead out of my sight.'",
    "M": "'I am a foreigner and stranger among you. Sell me some property for a burial site here so I can bury my dead.'",
    "T": "'I am a resident alien among you. Sell me a burial plot so I can bury my dead and lay her to rest.'"
  },
  "5": {
    "L": "The Hittites answered Abraham,",
    "M": "The Hittites replied to Abraham,",
    "T": "The Hittites answered Abraham:"
  },
  "6": {
    "L": "'Hear us, my lord; you are a prince of God among us. Bury your dead in the choicest of our tombs. None of us will withhold from you his tomb to hinder you from burying your dead.'",
    "M": "'Sir, listen to us. You are a mighty prince among us. Bury your dead in the choicest of our tombs. None of us will refuse you his tomb for burying your dead.'",
    "T": "'Listen to us, my lord. You are a mighty prince in our midst. Bury your dead in our finest tomb — none of us would refuse you.'"
  },
  "7": {
    "L": "Abraham rose and bowed to the Hittites, the people of the land.",
    "M": "Then Abraham rose and bowed down before the people of the land, the Hittites.",
    "T": "Abraham rose and bowed respectfully before the people of the land, the Hittites."
  },
  "8": {
    "L": "He said to them, 'If you are willing that I should bury my dead out of my sight, hear me and entreat for me Ephron the son of Zohar,'",
    "M": "He said to them, 'If you are willing to let me bury my dead, then listen to me and intercede with Ephron son of Zohar on my behalf'",
    "T": "'If it is your wish that I bury my dead here, hear me out and approach Ephron son of Zohar on my behalf.'"
  },
  "9": {
    "L": "'that he may give me the cave of Machpelah, which he owns; it is at the end of his field. For the full price let him give it to me in your presence as property for a burying place.'",
    "M": "'so he will sell me the cave of Machpelah, which belongs to him and is at the end of his field. Ask him to sell it to me for the full price as a burial site, in your presence.'",
    "T": "'Ask him to sell me the cave of Machpelah at the edge of his field — at full market price, in front of you all, as a permanent burial place.'"
  },
  "10": {
    "L": "Now Ephron was sitting among the Hittites, and Ephron the Hittite answered Abraham in the hearing of the Hittites, of all who went in at the gate of his city,",
    "M": "Ephron the Hittite was sitting among his people and he replied to Abraham in the hearing of all the Hittites who had come to the gate of his city.",
    "T": "Ephron the Hittite was sitting among his people. He spoke to Abraham in the hearing of all the Hittites who had gathered at the city gate:"
  },
  "11": {
    "L": "'No, my lord, hear me: I give you the field, and I give you the cave that is in it. In the sight of the sons of my people I give it to you. Bury your dead.'",
    "M": "'No, my lord,' he said. 'Listen to me; I give you the field, and I give you the cave that is in it. I give it to you in the presence of my people. Bury your dead.'",
    "T": "'No, my lord — hear me out. I give you the field and the cave in it. I give it to you freely, in front of my people. Bury your dead.'"
  },
  "12": {
    "L": "Then Abraham bowed down before the people of the land.",
    "M": "Again Abraham bowed down before the people of the land",
    "T": "Abraham bowed low before the people of the land"
  },
  "13": {
    "L": "And he said to Ephron in the hearing of the people of the land, 'But if you will, hear me: I give the price of the field. Accept it from me, that I may bury my dead there.'",
    "M": "and he said to Ephron in their hearing, 'Listen to me, if you will. I will pay the price of the field. Accept it from me so I can bury my dead there.'",
    "T": "and spoke to Ephron before everyone: 'Please hear me — let me pay the full price. Accept the money so I can bury my dead there.'"
  },
  "14": {
    "L": "Ephron answered Abraham,",
    "M": "Ephron answered Abraham,",
    "T": "Ephron replied to Abraham:"
  },
  "15": {
    "L": "'My lord, listen to me: a piece of land worth four hundred shekels of silver, what is that between you and me? Bury your dead.'",
    "M": "'Listen to me, my lord; the land is worth four hundred shekels of silver, but what is that between you and me? Bury your dead.'",
    "T": "'My lord, what is four hundred shekels of silver between friends? Bury your dead.'"
  },
  "16": {
    "L": "Abraham listened to Ephron, and Abraham weighed out for Ephron the silver that he had named in the hearing of the Hittites, four hundred shekels of silver, according to the weights current among the merchants.",
    "M": "Abraham agreed to Ephron's terms and weighed out for him the price he had named in the hearing of the Hittites: four hundred shekels of silver, according to the weight current among the merchants.",
    "T": "Abraham accepted the terms and counted out four hundred shekels of silver in front of the Hittites — the standard commercial weight — and paid Ephron."
  },
  "17": {
    "L": "So the field of Ephron in Machpelah, which was to the east of Mamre, the field with the cave that was in it and all the trees that were in the field, throughout its whole area, was made over",
    "M": "So Ephron's field in Machpelah near Mamre — both the field and the cave in it, and all the trees within the borders of the field — was deeded",
    "T": "Thus the field of Ephron at Machpelah, east of Mamre — the field, the cave in it, and all the trees within the borders —"
  },
  "18": {
    "L": "to Abraham as a possession in the sight of the Hittites, before all who went in at the gate of his city.",
    "M": "to Abraham as his property, in the presence of all the Hittites who had come to the gate of the city.",
    "T": "passed into Abraham's possession before all the Hittites at the city gate."
  },
  "19": {
    "L": "After this, Abraham buried Sarah his wife in the cave of the field of Machpelah east of Mamre, that is, Hebron, in the land of Canaan.",
    "M": "Afterward Abraham buried his wife Sarah in the cave in the field of Machpelah near Mamre (which is at Hebron) in the land of Canaan.",
    "T": "Then Abraham buried his wife Sarah in the cave of Machpelah east of Mamre, that is Hebron, in the land of Canaan."
  },
  "20": {
    "L": "The field and the cave that is in it were made over to Abraham as property for a burying place by the Hittites.",
    "M": "So the field and the cave in it were deeded to Abraham by the Hittites as a burial site.",
    "T": "The field and cave became Abraham's permanent property for burial, formally transferred by the Hittites."
  }
},

# ══════════════════════════════════════════════════════════════════════════════
# Chapter 24 — Abraham's servant finds Rebekah for Isaac (67 verses)
# H2617 חֶסֶד: "steadfast love" (L), "faithful love" (T) in vv. 12, 14, 27, 49
# ══════════════════════════════════════════════════════════════════════════════
"24": {
  "1": {
    "L": "Now Abraham was old, well advanced in years. And the LORD had blessed Abraham in all things.",
    "M": "Abraham was now very old, and the LORD had blessed him in every way.",
    "T": "Abraham was very old by now, and the LORD had blessed him in every way."
  },
  "2": {
    "L": "And Abraham said to his servant, the oldest of his household, who had charge of all that he had, 'Put your hand under my thigh,'",
    "M": "He said to the senior servant in his household, the one in charge of all that he had, 'Put your hand under my thigh.'",
    "T": "He called the oldest servant of his household — the one who managed everything he owned — and said, 'Place your hand under my thigh.'"
  },
  "3": {
    "L": "'that I may make you swear by the LORD, the God of heaven and God of the earth, that you will not take a wife for my son from the daughters of the Canaanites, among whom I dwell,'",
    "M": "'I want you to swear by the LORD, the God of heaven and the God of earth, that you will not get a wife for my son from the daughters of the Canaanites, among whom I am living,'",
    "T": "'I want you to swear by the LORD, God of heaven and earth, that you will not take a wife for my son from the daughters of the Canaanites among whom I live,'"
  },
  "4": {
    "L": "'but will go to my country and to my kindred, and take a wife for my son Isaac.'",
    "M": "'but will go to my country and my own relatives and get a wife for my son Isaac.'",
    "T": "'but will go back to my homeland, to my own family, and find a wife for my son Isaac.'"
  },
  "5": {
    "L": "The servant said to him, 'Perhaps the woman may not be willing to follow me to this land. Must I then take your son back to the land from which you came?'",
    "M": "The servant asked him, 'What if the woman is unwilling to come back with me to this land? Shall I then take your son back to the country you came from?'",
    "T": "The servant asked, 'What if the woman refuses to come back with me to this land? Should I take your son back to the country you came from?'"
  },
  "6": {
    "L": "Abraham said to him, 'See to it that you do not take my son back there.'",
    "M": "Abraham replied, 'Make sure that you do not take my son back there.'",
    "T": "Abraham said, 'Whatever you do, do not take my son back there.'"
  },
  "7": {
    "L": "'The LORD, the God of heaven, who took me from my father's house and from the land of my kindred, and who spoke to me and swore to me, \"To your offspring I will give this land,\" he will send his angel before you, and you shall take a wife for my son from there.'",
    "M": "'The LORD, the God of heaven, who brought me out of my father's household and my native land and who spoke to me and promised me on oath, \"To your offspring I will give this land\" — he will send his angel before you so that you can get a wife for my son from there.'",
    "T": "'The LORD, God of heaven, who brought me from my father's household and my homeland, who spoke to me and swore on oath, \"I will give this land to your descendants\" — he will send his messenger ahead of you, and you will find a wife for my son there.'"
  },
  "8": {
    "L": "'If the woman is not willing to follow you, then you will be free from this oath of mine; only you must not take my son back there.'",
    "M": "'If the woman is unwilling to come back with you, then you will be released from this oath of mine. Only do not take my son back there.'",
    "T": "'If she refuses to come with you, you are released from this oath. Only do not take my son back there.'"
  },
  "9": {
    "L": "So the servant put his hand under the thigh of Abraham his master and swore to him concerning this matter.",
    "M": "So the servant put his hand under the thigh of his master Abraham and swore an oath to him concerning this matter.",
    "T": "The servant placed his hand under Abraham's thigh and swore to carry out this mission."
  },
  "10": {
    "L": "Then the servant took ten of his master's camels and departed, taking all sorts of choice gifts from his master; and he arose and went to Mesopotamia to the city of Nahor.",
    "M": "Then the servant left, taking ten of his master's camels loaded with all kinds of good things from his master. He set out for Aram Naharaim and made his way to the town of Nahor.",
    "T": "The servant took ten of his master's camels loaded with fine gifts and set out for Aram-naharaim, making his way to the city of Nahor."
  },
  "11": {
    "L": "And he made the camels kneel down outside the city by the well of water at the time of evening, the time when women go out to draw water.",
    "M": "He had the camels kneel down near the well outside the town; it was toward evening, the time the women come out to draw water.",
    "T": "He made the camels kneel by the well at the edge of town. It was evening — the time when women come out to draw water."
  },
  "12": {
    "L": "And he said, 'O LORD, God of my master Abraham, please grant me success today and show steadfast love to my master Abraham.'",
    "M": "Then he prayed, 'LORD, God of my master Abraham, make me successful today, and show kindness to my master Abraham.'",
    "T": "He prayed: 'O LORD, God of my master Abraham — grant me success today. Show faithful love to my master Abraham.'"
  },
  "13": {
    "L": "'Behold, I am standing by the spring of water, and the daughters of the men of the city are coming out to draw water.'",
    "M": "'See, I am standing beside this spring, and the daughters of the townspeople are coming out to draw water.'",
    "T": "'Here I stand at this spring as the young women of the town are coming out to draw water.'"
  },
  "14": {
    "L": "'Let the young woman to whom I shall say, \"Please let down your jar that I may drink,\" and who shall say, \"Drink, and I will water your camels also\" — let her be the one you have appointed for your servant Isaac. By this I shall know that you have shown steadfast love to my master.'",
    "M": "'May it be that when I say to a young woman, \"Please let down your jar that I may have a drink,\" and she says, \"Drink, and I\'ll water your camels too\" — let her be the one you have chosen for your servant Isaac. By this I will know that you have shown kindness to my master.'",
    "T": "'Let this be the sign: the young woman I ask for a drink, who also offers to water my camels — let her be the one you have chosen for Isaac. By this I will know you have shown faithful love to my master.'"
  },
  "15": {
    "L": "Before he had finished speaking, behold, Rebekah, who was born to Bethuel the son of Milcah, the wife of Nahor, Abraham's brother, came out with her water jar on her shoulder.",
    "M": "Before he had finished praying, Rebekah came out with her jar on her shoulder. She was the daughter of Bethuel son of Milcah, who was the wife of Abraham's brother Nahor.",
    "T": "Before he had even finished praying, Rebekah came out with her water jar on her shoulder — the daughter of Bethuel, son of Milcah and Nahor, Abraham's brother."
  },
  "16": {
    "L": "The young woman was very attractive in appearance, a virgin, whom no man had known. She went down to the spring and filled her jar and came up.",
    "M": "The woman was very beautiful, a virgin; no man had ever slept with her. She went down to the spring, filled her jar and came back up.",
    "T": "She was beautiful — a young woman, a virgin, whom no man had known. She went down to the spring, filled her jar, and came up."
  },
  "17": {
    "L": "Then the servant ran to meet her and said, 'Please give me a little water to drink from your jar.'",
    "M": "The servant hurried to meet her and said, 'Please give me a little water from your jar.'",
    "T": "The servant hurried to meet her. 'Please,' he said, 'give me a sip of water from your jar.'"
  },
  "18": {
    "L": "She said, 'Drink, my lord.' And she quickly let down her jar upon her hand and gave him a drink.",
    "M": "'Drink, my lord,' she said, and quickly lowered the jar to her hands and gave him a drink.",
    "T": "'Drink, my lord,' she said, and quickly lowered the jar to her hands and let him drink."
  },
  "19": {
    "L": "When she had finished giving him a drink, she said, 'I will draw water for your camels also, until they have finished drinking.'",
    "M": "After she had given him a drink, she said, 'I'll draw water for your camels too, until they have had enough to drink.'",
    "T": "When he had finished, she said, 'I will draw water for your camels too, until they have all drunk their fill.'"
  },
  "20": {
    "L": "So she quickly emptied her jar into the trough and ran again to the well to draw water, and she drew for all his camels.",
    "M": "So she quickly emptied her jar into the trough, ran back to the well to draw more water, and drew enough for all his camels.",
    "T": "She quickly poured her jar into the watering trough, ran back to the well, and kept drawing until all ten camels had drunk their fill."
  },
  "21": {
    "L": "The man gazed at her in silence to learn whether the LORD had prospered his journey or not.",
    "M": "Without saying a word, the man watched her closely to learn whether or not the LORD had made his journey successful.",
    "T": "The man watched in silence, wanting to know whether the LORD had made his journey a success."
  },
  "22": {
    "L": "When the camels had finished drinking, the man took a gold ring weighing a half shekel, and two bracelets for her arms weighing ten gold shekels,",
    "M": "When the camels had finished drinking, the man took out a gold nose ring weighing a beka and two gold bracelets weighing ten shekels.",
    "T": "When the camels had finished drinking, the man took out a gold nose ring weighing half a shekel and two gold bracelets weighing ten shekels."
  },
  "23": {
    "L": "and said, 'Whose daughter are you? Tell me: is there room in your father's house for us to spend the night?'",
    "M": "Then he asked, 'Whose daughter are you? Please tell me, is there room in your father's house for us to spend the night?'",
    "T": "He asked, 'Whose daughter are you? Is there room at your father's house for us to spend the night?'"
  },
  "24": {
    "L": "She said to him, 'I am the daughter of Bethuel the son of Milcah, whom she bore to Nahor.'",
    "M": "She answered him, 'I am the daughter of Bethuel, the son that Milcah bore to Nahor.'",
    "T": "She answered, 'I am the daughter of Bethuel — the son Milcah bore to Nahor.'"
  },
  "25": {
    "L": "She added, 'We have plenty of both straw and fodder, and room to spend the night.'",
    "M": "She also said to him, 'We have plenty of straw and fodder, as well as room for you to spend the night.'",
    "T": "'We have plenty of straw and feed,' she added, 'and there is room for you to stay the night.'"
  },
  "26": {
    "L": "The man bowed his head and worshiped the LORD",
    "M": "Then the man bowed down and worshiped the LORD,",
    "T": "Then the man bowed his head and worshiped the LORD,"
  },
  "27": {
    "L": "and said, 'Blessed be the LORD, the God of my master Abraham, who has not forsaken his steadfast love and his faithfulness toward my master. As for me, the LORD has led me in the way to the house of my master's kinsmen.'",
    "M": "saying, 'Praise be to the LORD, the God of my master Abraham, who has not abandoned his kindness and faithfulness to my master. As for me, the LORD has led me on the journey to the house of my master's relatives.'",
    "T": "and said, 'Blessed be the LORD, God of my master Abraham — he has not withheld his faithful love and his faithfulness from my master. The LORD has guided me on this very road to the house of my master's own family.'"
  },
  "28": {
    "L": "The young woman ran and told her mother's household about these things.",
    "M": "The young woman ran and told her mother's household about these things.",
    "T": "The young woman ran home and told everyone in her mother's household."
  },
  "29": {
    "L": "Rebekah had a brother whose name was Laban. Laban ran out toward the man, to the spring.",
    "M": "Now Rebekah had a brother named Laban, and he hurried out to the man at the spring.",
    "T": "Rebekah had a brother named Laban. He ran out to meet the man at the spring."
  },
  "30": {
    "L": "As soon as he saw the ring and the bracelets on his sister's arms, and heard the words of Rebekah his sister, 'Thus the man spoke to me,' he went to the man. And behold, he was standing by the camels at the spring.",
    "M": "As soon as he had seen the nose ring, and the bracelets on his sister's arms, and had heard Rebekah tell what the man said to her, he went out to the man and found him standing by the camels near the spring.",
    "T": "When he saw the ring and bracelets on his sister's arms and heard what she reported the man had said, he hurried to the well — there the man still stood by his camels."
  },
  "31": {
    "L": "He said, 'Come in, O blessed of the LORD. Why do you stand outside? For I have prepared the house and a place for the camels.'",
    "M": "'Come, you who are blessed by the LORD,' he said. 'Why are you standing out here? I have prepared the house and a place for the camels.'",
    "T": "He said, 'Come in, you who are blessed by the LORD! Why are you standing outside? I have prepared the house and a place for the camels.'"
  },
  "32": {
    "L": "So the man came to the house and unharnessed the camels. And straw and fodder were given for the camels, and there was water to wash his feet and the feet of the men who were with him.",
    "M": "So the man went to the house, and the camels were unloaded. Straw and fodder were brought for the camels, and water for him and his men to wash their feet.",
    "T": "The man came into the house. The camels were unloaded; straw and feed were brought for them. Then water was brought for the servant and his men to wash their feet."
  },
  "33": {
    "L": "Then food was set before him to eat. But he said, 'I will not eat until I have said what I have to say.' He said, 'Speak on.'",
    "M": "Then food was placed before him, but he said, 'I will not eat until I have told you what I have to say.' 'Then tell us,' Laban said.",
    "T": "Food was placed before him, but he said, 'I will not eat until I have told my business.' 'Then speak,' said Laban."
  },
  "34": {
    "L": "So he said, 'I am Abraham's servant.'",
    "M": "So he said, 'I am Abraham's servant.'",
    "T": "He said, 'I am Abraham's servant.'"
  },
  "35": {
    "L": "'The LORD has greatly blessed my master, and he has become great. He has given him flocks and herds, silver and gold, male servants and female servants, camels and donkeys.'",
    "M": "'The LORD has blessed my master abundantly, and he has become wealthy. He has given him sheep and cattle, silver and gold, male and female servants, and camels and donkeys.'",
    "T": "'The LORD has richly blessed my master, and he has become very wealthy. He has given him flocks and herds, silver and gold, servants and maids, camels and donkeys.'"
  },
  "36": {
    "L": "'And Sarah my master's wife bore a son to my master when she was old, and to him he has given all that he has.'",
    "M": "'My master's wife Sarah has borne him a son in her old age, and he has given him everything he owns.'",
    "T": "'My master's wife Sarah bore him a son in her old age, and he has given everything he owns to this son.'"
  },
  "37": {
    "L": "'My master made me swear, saying, \"You shall not take a wife for my son from the daughters of the Canaanites, in whose land I dwell,\"'",
    "M": "'My master made me take an oath, saying, \"Do not get a wife for my son from the daughters of the Canaanites, in whose land I live,\"'",
    "T": "'My master had me swear: \"Do not take a wife for my son from the Canaanites in whose land I live.\""
  },
  "38": {
    "L": "'but you shall go to my father's house and to my clan and take a wife for my son.'",
    "M": "'\"But go to my father's family and to my own clan, and get a wife for my son.\"'",
    "T": "'\"Instead, go to my father's household and my own clan and find a wife for my son.\"'"
  },
  "39": {
    "L": "'I said to my master, \"Perhaps the woman will not follow me.\"'",
    "M": "'Then I asked my master, \"What if the woman will not come back with me?\"'",
    "T": "'I asked my master, \"What if the woman refuses to come back with me?\"'"
  },
  "40": {
    "L": "'But he said to me, \"The LORD, before whom I have walked, will send his angel with you and prosper your way. You shall take a wife for my son from my clan and from my father's house.\"'",
    "M": "'He replied, \"The LORD, before whom I have walked faithfully, will send his angel with you and make your journey a success, so that you can get a wife for my son from my own clan and from my father's family.\"'",
    "T": "'He said, \"The LORD, before whom I have walked, will send his messenger with you and make your journey successful. You will find a wife for my son from my own clan and my father's family.\"'"
  },
  "41": {
    "L": "'Then you will be free from my oath, when you come to my clan. And if they will not give her to you, you will be free from my oath.'",
    "M": "'\"And if you go to my clan and they refuse to give her to you — you will be released from my oath.\"'",
    "T": "'\"If you go to my family and they will not give her to you, then you are released from this oath.\"'"
  },
  "42": {
    "L": "'I came today to the spring and said, \"O LORD, the God of my master Abraham, if now you are prospering the way that I go,\"'",
    "M": "'When I came to the spring today, I said, \"LORD, God of my master Abraham, if you will, please grant success to the journey on which I have come.\"'",
    "T": "'When I arrived at the spring today I prayed: \"O LORD, God of my master Abraham — if you are indeed making this journey successful for me —\"'"
  },
  "43": {
    "L": "'\"behold, I am standing by the spring of water. Let the virgin who comes out to draw water, to whom I shall say, 'Please give me a little water from your jar to drink,'\"’",
    "M": "'\"See, I am standing beside this spring. If a young woman comes out to draw water and I say to her, 'Please let me drink a little water from your jar,'\"'",
    "T": "'\"Here I stand at this spring. When a young woman comes to draw water and I ask, 'Let me drink from your jar,'\"'"
  },
  "44": {
    "L": "'\"and she says to me, 'Drink, and I will draw for your camels also,' let her be the woman whom the LORD has appointed for my master's son.\"'",
    "M": "'\"and if she says, 'Drink, and I\'ll draw water for your camels too,' let her be the one the LORD has chosen for my master's son.\"'",
    "T": "'\"and she says, 'Drink, and I will water your camels too' — then she is the woman the LORD has chosen for my master's son.\"'"
  },
  "45": {
    "L": "'Before I had finished speaking in my heart, behold, Rebekah came out with her water jar on her shoulder, and she went down to the spring and drew water. I said to her, \"Please let me drink.\"'",
    "M": "'Before I finished praying in my heart, Rebekah came out, with her jar on her shoulder. She went down to the spring and drew water, and I said to her, \"Please let me have a drink.\"'",
    "T": "'Before I had even finished praying silently, Rebekah came out with her jar on her shoulder, went down to the spring, and drew water. I said, \"Please let me drink.\"'"
  },
  "46": {
    "L": "'She quickly let down her jar from her shoulder and said, \"Drink, and I will give your camels drink also.\" So I drank, and she gave the camels drink also.'",
    "M": "'She quickly lowered her jar from her shoulder and said, \"Drink, and I\'ll water your camels too.\" So I drank, and she watered the camels also.'",
    "T": "'She quickly lowered her jar and said, \"Drink — I will water your camels too.\" So I drank, and she watered the camels as well.'"
  },
  "47": {
    "L": "'Then I asked her, \"Whose daughter are you?\" She said, \"The daughter of Bethuel, Nahor's son, whom Milcah bore to him.\" So I put the ring on her nose and the bracelets on her arms.'",
    "M": "'I asked her, \"Whose daughter are you?\" She said, \"The daughter of Bethuel son of Nahor, whom Milcah bore to him.\" Then I put the ring in her nose and the bracelets on her arms,'",
    "T": "'I asked her whose daughter she was. She said, \"The daughter of Bethuel, the son Milcah bore to Nahor.\" I put the ring in her nose and the bracelets on her arms.'"
  },
  "48": {
    "L": "'and I bowed my head and worshiped the LORD and blessed the LORD, the God of my master Abraham, who had led me by the right way to take the daughter of my master's kinsman for his son.'",
    "M": "'and I bowed down and worshiped the LORD. I praised the LORD, the God of my master Abraham, who had led me on the right road to get the granddaughter of my master's brother for his son.'",
    "T": "'Then I bowed and worshiped the LORD, blessing him — God of my master Abraham — who had led me straight to the daughter of my master's kinsman for his son.'"
  },
  "49": {
    "L": "'Now then, if you are going to show steadfast love and faithfulness to my master, tell me; and if not, tell me, that I may turn to the right hand or to the left.'",
    "M": "'Now if you will show kindness and faithfulness to my master, tell me; and if not, tell me, so I may know which way to turn.'",
    "T": "'So now — will you show faithful love and faithfulness to my master? Tell me yes or no, so I know which way to turn.'"
  },
  "50": {
    "L": "Then Laban and Bethuel answered and said, 'The thing has come from the LORD; we cannot speak to you bad or good.'",
    "M": "Laban and Bethuel answered, 'This is from the LORD; we can say nothing to you one way or the other.'",
    "T": "Laban and Bethuel answered, 'This has come from the LORD. We cannot say yes or no to you.'"
  },
  "51": {
    "L": "'Behold, Rebekah is before you; take her and go, and let her be the wife of your master's son, as the LORD has spoken.'",
    "M": "'Here is Rebekah; take her and go, and let her become the wife of your master's son, as the LORD has directed.'",
    "T": "'Rebekah is here before you — take her and go. Let her become your master's son's wife, as the LORD has spoken.'"
  },
  "52": {
    "L": "When Abraham's servant heard their words, he bowed himself to the earth before the LORD.",
    "M": "When Abraham's servant heard what they said, he bowed down to the ground before the LORD.",
    "T": "When Abraham's servant heard their answer, he prostrated himself before the LORD."
  },
  "53": {
    "L": "And the servant brought out jewelry of silver and of gold, and garments, and gave them to Rebekah. He also gave to her brother and to her mother costly ornaments.",
    "M": "Then the servant brought out gold and silver jewelry and articles of clothing and gave them to Rebekah; he also gave costly gifts to her brother and to her mother.",
    "T": "The servant brought out silver and gold jewelry and fine clothing and gave them to Rebekah. He also gave costly gifts to her brother and mother."
  },
  "54": {
    "L": "And he and the men who were with him ate and drank, and they spent the night there. When they arose in the morning, he said, 'Send me away to my master.'",
    "M": "Then he and the men who were with him ate and drank and spent the night there. When they got up the next morning, he said, 'Send me on my way to my master.'",
    "T": "He and his men ate and drank and spent the night. In the morning he got up and said, 'Let me go back to my master.'"
  },
  "55": {
    "L": "Her brother and her mother said, 'Let the young woman remain with us a while, at least ten days; after that she may go.'",
    "M": "But her brother and her mother replied, 'Let the young woman remain with us ten days or so; then you may go.'",
    "T": "Her brother and mother said, 'Let the girl stay with us for ten days or so — then you can go.'"
  },
  "56": {
    "L": "But he said to them, 'Do not delay me, since the LORD has prospered my way. Send me away that I may go to my master.'",
    "M": "But he said to them, 'Do not detain me, now that the LORD has granted success to my journey. Send me on my way so I may go to my master.'",
    "T": "He replied, 'Do not delay me — the LORD has made my journey a success. Send me off so I can return to my master.'"
  },
  "57": {
    "L": "They said, 'Let us call the young woman and ask her.'",
    "M": "Then they said, 'Let's call the young woman and ask her about it.'",
    "T": "They said, 'Let's call Rebekah and ask her.'"
  },
  "58": {
    "L": "And they called Rebekah and said to her, 'Will you go with this man?' She said, 'I will go.'",
    "M": "So they called Rebekah and asked her, 'Will you go with this man?' 'I will go,' she said.",
    "T": "They called Rebekah and asked, 'Will you go with this man?' She said, 'I will go.'"
  },
  "59": {
    "L": "So they sent away Rebekah their sister and her nurse, and Abraham's servant and his men.",
    "M": "So they sent their sister Rebekah on her way, along with her nurse and Abraham's servant and his men.",
    "T": "So they sent their sister Rebekah off with her nurse, along with Abraham's servant and his men."
  },
  "60": {
    "L": "And they blessed Rebekah and said to her, 'Our sister, may you become thousands of ten thousands, and may your offspring possess the gate of those who hate him!'",
    "M": "And they blessed Rebekah and said to her, 'Our sister, may you increase to thousands upon thousands; may your offspring possess the cities of their enemies.'",
    "T": "They blessed Rebekah and said, 'Our sister, may you become the mother of thousands upon thousands! May your descendants take possession of the cities of their enemies!'"
  },
  "61": {
    "L": "Then Rebekah and her young women arose and rode on the camels and followed the man. Thus the servant took Rebekah and went his way.",
    "M": "Then Rebekah and her attendants got ready and mounted the camels and went back with the man. So the servant took Rebekah and left.",
    "T": "Then Rebekah and her attendants mounted the camels and followed the man. The servant took Rebekah and set out."
  },
  "62": {
    "L": "Now Isaac had returned from Beer-lahai-roi and was dwelling in the Negeb.",
    "M": "Now Isaac had come from Beer Lahai Roi, for he was living in the Negev.",
    "T": "Isaac had been coming from Beer-lahai-roi and was living in the Negev."
  },
  "63": {
    "L": "And Isaac went out to meditate in the field toward evening. And he lifted up his eyes and saw, and behold, there were camels coming.",
    "M": "He went out to the field one evening to meditate, and as he looked up, he saw camels approaching.",
    "T": "One evening Isaac went out to walk in the fields. He looked up and saw camels approaching."
  },
  "64": {
    "L": "And Rebekah lifted up her eyes, and when she saw Isaac, she dismounted from the camel",
    "M": "Rebekah also looked up and saw Isaac. She got down from her camel",
    "T": "Rebekah looked up and saw Isaac. She got down from her camel"
  },
  "65": {
    "L": "and said to the servant, 'Who is that man, walking in the field to meet us?' The servant said, 'It is my master.' So she took her veil and covered herself.",
    "M": "and asked the servant, 'Who is that man in the field coming to meet us?' 'He is my master,' the servant answered. So she took her veil and covered herself.",
    "T": "and asked the servant, 'Who is that man walking in the field to meet us?' The servant said, 'That is my master.' So she covered herself with her veil."
  },
  "66": {
    "L": "And the servant told Isaac all the things that he had done.",
    "M": "Then the servant told Isaac all he had done.",
    "T": "Then the servant told Isaac everything that had happened."
  },
  "67": {
    "L": "Then Isaac brought her into the tent of Sarah his mother and took Rebekah, and she became his wife, and he loved her. So Isaac was comforted after his mother's death.",
    "M": "Isaac brought her into the tent of his mother Sarah, and he married Rebekah. So she became his wife, and he loved her; and Isaac was comforted after his mother's death.",
    "T": "Isaac brought Rebekah into his mother Sarah's tent, and she became his wife. He loved her. So Isaac was comforted after losing his mother."
  }
},

# ══════════════════════════════════════════════════════════════════════════════
# Chapter 25 — Abraham's death; Ishmael's line; birth and early years of
#              Jacob and Esau; Esau sells his birthright
# ══════════════════════════════════════════════════════════════════════════════
"25": {
  "1": {
    "L": "Abraham took another wife, and her name was Keturah.",
    "M": "Abraham had taken another wife, whose name was Keturah.",
    "T": "Abraham took another wife, named Keturah."
  },
  "2": {
    "L": "She bore him Zimran, Jokshan, Medan, Midian, Ishbak, and Shuah.",
    "M": "She bore him Zimran, Jokshan, Medan, Midian, Ishbak and Shuah.",
    "T": "She bore him Zimran, Jokshan, Medan, Midian, Ishbak, and Shuah."
  },
  "3": {
    "L": "Jokshan fathered Sheba and Dedan. The sons of Dedan were Asshurim, Letushim, and Leummim.",
    "M": "Jokshan was the father of Sheba and Dedan; the descendants of Dedan were the Ashurites, the Letushites and the Leummites.",
    "T": "Jokshan fathered Sheba and Dedan. The descendants of Dedan were the Ashurites, Letushites, and Leummites."
  },
  "4": {
    "L": "The sons of Midian were Ephah, Epher, Hanoch, Abida, and Eldaah. All these were the children of Keturah.",
    "M": "The sons of Midian were Ephah, Epher, Hanok, Abida and Eldaah. All these were descendants of Keturah.",
    "T": "The sons of Midian were Ephah, Epher, Hanoch, Abida, and Eldaah. All these were Keturah's descendants."
  },
  "5": {
    "L": "Abraham gave all he had to Isaac.",
    "M": "Abraham left everything he owned to Isaac.",
    "T": "Abraham gave everything he owned to Isaac."
  },
  "6": {
    "L": "But to the sons of his concubines Abraham gave gifts, and while he was still living he sent them away from his son Isaac, eastward to the east country.",
    "M": "But while he was still living, he gave gifts to the sons of his concubines and sent them away from his son Isaac to the land of the east.",
    "T": "While he was still alive, Abraham gave gifts to the sons of his concubines and sent them away from his son Isaac, eastward to the east."
  },
  "7": {
    "L": "These are the days of the years of Abraham's life, 175 years.",
    "M": "Abraham lived a hundred and seventy-five years.",
    "T": "Abraham lived to be one hundred and seventy-five years old."
  },
  "8": {
    "L": "Abraham breathed his last and died in a good old age, an old man and full of years, and was gathered to his people.",
    "M": "Then Abraham breathed his last and died at a good old age, an old man and full of years; and he was gathered to his people.",
    "T": "Then Abraham breathed his last and died — old, full of years, satisfied with life — and was gathered to his people."
  },
  "9": {
    "L": "Isaac and Ishmael his sons buried him in the cave of Machpelah, in the field of Ephron the son of Zohar the Hittite, east of Mamre,",
    "M": "His sons Isaac and Ishmael buried him in the cave of Machpelah near Mamre, in the field of Ephron son of Zohar the Hittite,",
    "T": "His sons Isaac and Ishmael buried him in the cave of Machpelah near Mamre, in the field of Ephron son of Zohar the Hittite —"
  },
  "10": {
    "L": "the field that Abraham purchased from the Hittites. There Abraham was buried, with Sarah his wife.",
    "M": "the field Abraham had bought from the Hittites. There Abraham was buried with his wife Sarah.",
    "T": "the field Abraham had purchased from the Hittites. There Abraham was buried, together with his wife Sarah."
  },
  "11": {
    "L": "After the death of Abraham, God blessed Isaac his son. And Isaac settled at Beer-lahai-roi.",
    "M": "After Abraham's death, God blessed his son Isaac, who then lived near Beer Lahai Roi.",
    "T": "After Abraham died, God blessed his son Isaac, who settled near Beer-lahai-roi."
  },
  "12": {
    "L": "These are the generations of Ishmael, Abraham's son, whom Hagar the Egyptian, Sarah's servant, bore to Abraham.",
    "M": "This is the account of the family line of Abraham's son Ishmael, whom Sarah's slave, Hagar the Egyptian, bore to Abraham.",
    "T": "This is the family record of Ishmael, Abraham's son, whom Hagar the Egyptian — Sarah's slave — bore to Abraham."
  },
  "13": {
    "L": "These are the names of the sons of Ishmael, named in the order of their birth: Nebaioth, the firstborn of Ishmael; and Kedar, Adbeel, Mibsam,",
    "M": "These are the names of the sons of Ishmael, listed in the order of their birth: Nebaioth the firstborn of Ishmael, Kedar, Adbeel, Mibsam,",
    "T": "These are the names of Ishmael's sons in birth order: Nebaioth the firstborn, then Kedar, Adbeel, Mibsam,"
  },
  "14": {
    "L": "Mishma, Dumah, Massa,",
    "M": "Mishma, Dumah, Massa,",
    "T": "Mishma, Dumah, Massa,"
  },
  "15": {
    "L": "Hadad, Tema, Jetur, Naphish, and Kedemah.",
    "M": "Hadad, Tema, Jetur, Naphish and Kedemah.",
    "T": "Hadad, Tema, Jetur, Naphish, and Kedemah."
  },
  "16": {
    "L": "These are the sons of Ishmael and these are their names, by their villages and by their encampments, twelve princes according to their tribes.",
    "M": "These were the sons of Ishmael, and these are the names of the twelve tribal rulers according to their settlements and camps.",
    "T": "These were Ishmael's sons — twelve princes, each the head of a settlement or encampment, according to their clans."
  },
  "17": {
    "L": "These are the years of the life of Ishmael: 137 years. He breathed his last and died, and was gathered to his people.",
    "M": "Ishmael lived a hundred and thirty-seven years. He breathed his last and died, and he was gathered to his people.",
    "T": "Ishmael lived one hundred and thirty-seven years. He breathed his last and died, and was gathered to his people."
  },
  "18": {
    "L": "They settled from Havilah to Shur, which is opposite Egypt in the direction of Assyria. He settled over against all his kinsmen.",
    "M": "His descendants settled in the area from Havilah to Shur, near the eastern border of Egypt, as you go toward Ashur. And they lived in hostility toward all the tribes related to them.",
    "T": "His descendants settled from Havilah to Shur, east of Egypt on the way to Assyria — living at odds with all their relatives, just as had been foretold."
  },
  "19": {
    "L": "These are the generations of Isaac, Abraham's son: Abraham fathered Isaac,",
    "M": "This is the account of the family line of Abraham's son Isaac. Abraham became the father of Isaac,",
    "T": "This is the family record of Isaac, Abraham's son. Abraham was Isaac's father;"
  },
  "20": {
    "L": "and Isaac was forty years old when he took Rebekah, the daughter of Bethuel the Aramean of Paddan-aram, the sister of Laban the Aramean, to be his wife.",
    "M": "and Isaac was forty years old when he married Rebekah daughter of Bethuel the Aramean from Paddan Aram and sister of Laban the Aramean.",
    "T": "Isaac was forty years old when he married Rebekah, daughter of Bethuel the Aramean from Paddan-aram and sister of Laban the Aramean."
  },
  "21": {
    "L": "And Isaac prayed to the LORD for his wife, because she was barren. And the LORD granted his prayer, and Rebekah his wife conceived.",
    "M": "Isaac prayed to the LORD on behalf of his wife, because she was childless. The LORD answered his prayer, and his wife Rebekah became pregnant.",
    "T": "Isaac prayed to the LORD for his wife, because she was barren. The LORD answered his prayer, and Rebekah became pregnant."
  },
  "22": {
    "L": "The children struggled together within her, and she said, 'If it is thus, why is this happening to me?' So she went to inquire of the LORD.",
    "M": "The babies jostled each other within her, and she said, 'Why is this happening to me?' So she went to inquire of the LORD.",
    "T": "But the babies struggled inside her, and she said, 'If it is like this, why is this happening to me?' She went to seek the LORD's word."
  },
  "23": {
    "L": "And the LORD said to her, 'Two nations are in your womb, and two peoples from within you shall be divided; the one shall be stronger than the other, the older shall serve the younger.'",
    "M": "The LORD said to her, 'Two nations are in your womb, and two peoples from within you will be separated; one people will be stronger than the other, and the older will serve the younger.'",
    "T": "The LORD said to her, 'Two nations are in your womb. Two peoples will be separated from within you. One will be stronger than the other — and the older will serve the younger.'"
  },
  "24": {
    "L": "When her days to give birth were completed, behold, there were twins in her womb.",
    "M": "When the time came for her to give birth, there were twin boys in her womb.",
    "T": "When her time came to give birth, there were twins in her womb."
  },
  "25": {
    "L": "The first came out red, all his body like a hairy cloak, so they called his name Esau.",
    "M": "The first to come out was red, and his whole body was like a hairy garment; so they named him Esau.",
    "T": "The first one came out reddish, his whole body like a hairy garment, so they named him Esau."
  },
  "26": {
    "L": "Afterward his brother came out with his hand holding Esau's heel, so his name was called Jacob. Isaac was sixty years old when she bore them.",
    "M": "After this, his brother came out, with his hand grasping Esau's heel; so he was named Jacob. Isaac was sixty years old when Rebekah gave birth to them.",
    "T": "Then his brother came out grasping Esau's heel, so he was named Jacob — 'He Grasps the Heel.' Isaac was sixty years old when they were born."
  },
  "27": {
    "L": "When the boys grew up, Esau was a skillful hunter, a man of the field, while Jacob was a quiet man, dwelling in tents.",
    "M": "The boys grew up, and Esau became a skillful hunter, a man of the open country, while Jacob was content to stay at home among the tents.",
    "T": "The boys grew up. Esau became a skilled hunter, a man of the open country. Jacob was a quiet, settled man who stayed near the tents."
  },
  "28": {
    "L": "Isaac loved Esau because he ate of his game, but Rebekah loved Jacob.",
    "M": "Isaac, who had a taste for wild game, loved Esau, but Rebekah loved Jacob.",
    "T": "Isaac loved Esau — wild game was his weakness. But Rebekah loved Jacob."
  },
  "29": {
    "L": "Once when Jacob was cooking stew, Esau came in from the field, and he was exhausted.",
    "M": "Once when Jacob was cooking some stew, Esau came in from the open country, famished.",
    "T": "One day Jacob was boiling a stew when Esau came in from the field, completely exhausted."
  },
  "30": {
    "L": "And Esau said to Jacob, 'Let me eat some of that red stew, for I am exhausted!' Therefore his name was called Edom.",
    "M": "He said to Jacob, 'Quick, let me have some of that red stew! I'm famished!' That is why he was also called Edom.",
    "T": "Esau said, 'Quick! Let me eat some of that red stew — I am utterly starving!' That is why he was also called Edom, 'Red One.'"
  },
  "31": {
    "L": "Jacob said, 'Sell me your birthright now.'",
    "M": "Jacob replied, 'First sell me your birthright.'",
    "T": "Jacob said, 'Sell me your birthright first.'"
  },
  "32": {
    "L": "Esau said, 'I am about to die; of what use is a birthright to me?'",
    "M": "Esau said, 'Look, I am about to die. What good is the birthright to me?'",
    "T": "Esau said, 'I am about to die! What good is a birthright to me now?'"
  },
  "33": {
    "L": "Jacob said, 'Swear to me now.' So he swore to him and sold his birthright to Jacob.",
    "M": "But Jacob said, 'Swear to me first.' So he swore an oath to him, selling his birthright to Jacob.",
    "T": "Jacob said, 'Swear to me right now.' So Esau swore an oath, selling his birthright to Jacob."
  },
  "34": {
    "L": "Then Jacob gave Esau bread and lentil stew, and he ate and drank and rose and went his way. Thus Esau despised his birthright.",
    "M": "Then Jacob gave Esau some bread and some lentil stew. He ate and drank, and then got up and left. So Esau despised his birthright.",
    "T": "Then Jacob gave Esau bread and lentil stew. He ate, drank, got up, and left. Esau had despised his birthright."
  }
}

}  # end GENESIS dict

# ── Write to draft files ───────────────────────────────────────────────────────

if __name__ == '__main__':
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'genesis')
        merge_tier(existing, GENESIS, tier_key)
        save(tier_dir, 'genesis', existing)

    # Verse count summary
    total = sum(len(v) for v in GENESIS.values())
    print(f'\nDone. Chapters: {sorted(GENESIS.keys())}')
    print(f'Total verses written: {total}')
    for ch, verses in sorted(GENESIS.items()):
        print(f'  Ch {ch}: {len(verses)} verses')
