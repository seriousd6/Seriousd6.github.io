"""
MKT 1 Samuel chapters 7–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1samuel-7-12.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M); "the LORD" or "LORD" in T — small-caps convention maintained;
  name's covenantal weight surfaced in T through context rather than "Yahweh" spelling.
- H430 (אֱלֹהִים): "God" throughout — all occurrences in these chapters refer unambiguously
  to the God of Israel; no plural ambiguity to resolve.
- H7307 (רוּחַ): "Spirit" (capitalized) in 10:6, 11:6 — divine charismatic empowerment context;
  Greek pneuma/Hebrew ruach ambiguity resolved by context: these are the classic nagid-anointing
  and judge-empowerment patterns.
- H5057 (נגיד): L "captain", M "ruler", T "designated leader/prince" — the nagid word signals
  appointment to shepherd Israel on God's behalf, distinct from the popular demand for מלך (melek).
  Samuel anoints Saul as nagid in 10:1; the distinction matters theologically.
- H4428 (מלך): "king" throughout all tiers — the people's demand and the institution established.
- H4941 (משפט): "manner" (L) / "practice" or "rights and duties" (M/T) — in ch 8 refers to the
  king's operating style (warning); in ch 10:25 refers to the covenant document setting kingship terms.
- H8668 (תשועה): "salvation" (L), "deliverance/victory" (M/T) — 11:13 is Saul's magnanimous
  declaration after the Jabesh-gilead victory; T renders the honor-shame valence.
- H6666 (צדקות): "righteous acts" (L), "righteous deeds" (M), "saving acts / covenant faithfulness" (T)
  — 12:7 is Samuel's appeal to God's track record; the plural "righteousnesses" refers to specific
  historical deliverances, not a general quality.
- H8034 (שֵׁם): "name" (L/M), but in 12:22 T surfaces "for the sake of his own great name" — God's
  honor-investment in Israel is the ground for his faithfulness, not Israel's merit.
- Ebenezer (7:12): translated "Stone of Help" in T to surface the meaning; kept "Ebenezer" as proper
  noun in L/M.
- Water-pouring rite (7:6): T notes this as a rite of contrition; no parallel elsewhere in OT makes
  its meaning explicit, but context (fasting + confession) confirms penitential register.
- Saul hiding in baggage (10:22): T preserves the ambiguity — fear, humility, or divine providence?
  The narrative does not resolve it.
- "Sons of Belial" (10:27): rendered "worthless men" (L), "certain worthless men" (M), "men of no
  worth" (T) — beliyyaʿal is a compound idiom meaning uselessness/worthlessness; not a proper
  theological title here.
- Aspect notes: narrative waw-consecutive imperfects throughout rendered as past tense in English.
  The Spirit verbs in 10:6, 10:10, 11:6 use tsalach (H6743) — "come powerfully upon" in M/T,
  not the lighter "come upon."
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

SAMUEL = {
  "7": {
    "1": {
      "L": "And the men of Kirjath-jearim came and fetched up the ark of the LORD and brought it into the house of Abinadab on the hill; and they sanctified Eleazar his son to keep the ark of the LORD.",
      "M": "The men of Kiriath-jearim came and brought up the ark of the LORD and took it into the house of Abinadab on the hill, consecrating his son Eleazar to guard the ark of the LORD.",
      "T": "So the men of Kiriath-jearim came and carried the ark of the LORD up to the house of Abinadab on the hill, setting apart his son Eleazar to serve as its guardian."
    },
    "2": {
      "L": "And it came to pass from the day the ark abode in Kirjath-jearim the time was long—it was twenty years—and all the house of Israel lamented after the LORD.",
      "M": "From the day the ark remained in Kiriath-jearim a long time passed—twenty years—and all the house of Israel mourned and yearned after the LORD.",
      "T": "Twenty years passed while the ark sat at Kiriath-jearim, and during all that time the whole house of Israel ached for the LORD, their grief turning into longing."
    },
    "3": {
      "L": "And Samuel spake unto all the house of Israel, saying, If ye do return unto the LORD with all your hearts, then put away the foreign gods and the Ashtaroth from among you, and set your hearts toward the LORD and serve him only; and he will deliver you out of the hand of the Philistines.",
      "M": "Samuel said to all the house of Israel, 'If you are returning to the LORD with all your hearts, then remove the foreign gods and the Ashtaroth from among you, direct your hearts to the LORD, and serve him alone—he will rescue you from the hand of the Philistines.'",
      "T": "Samuel addressed the whole house of Israel: 'If your return to the LORD is wholehearted, then act on it—strip out the foreign gods and the Ashtaroth, fix your loyalty on the LORD alone and serve no other. Do this, and he will deliver you from Philistia's grip.'"
    },
    "4": {
      "L": "Then the children of Israel put away the Baalim and the Ashtaroth, and served the LORD only.",
      "M": "So the Israelites put away the Baals and the Ashtaroth and served the LORD alone.",
      "T": "The people of Israel cleared out the Baals and the Ashtaroth and gave their worship to the LORD and to none other."
    },
    "5": {
      "L": "And Samuel said, Gather all Israel to Mizpah, and I will pray for you to the LORD.",
      "M": "Samuel said, 'Assemble all Israel at Mizpah, and I will intercede for you before the LORD.'",
      "T": "Samuel called for a national assembly: 'Gather all Israel at Mizpah, and I will stand before the LORD and plead on your behalf.'"
    },
    "6": {
      "L": "And they gathered together to Mizpah and drew water and poured it out before the LORD and fasted on that day, and said there, We have sinned against the LORD. And Samuel judged the children of Israel in Mizpah.",
      "M": "They assembled at Mizpah, drew water and poured it out before the LORD, fasted that day, and declared there, 'We have sinned against the LORD.' And Samuel judged the Israelites at Mizpah.",
      "T": "They gathered at Mizpah and performed the rite of water-pouring before the LORD—an act of contrition—fasting through the day and confessing, 'We have sinned against the LORD.' There Samuel presided over Israel as judge."
    },
    "7": {
      "L": "And when the Philistines heard that the children of Israel were gathered together to Mizpah, the lords of the Philistines went up against Israel; and the children of Israel heard and were afraid of the Philistines.",
      "M": "When the Philistine lords heard that the Israelites had assembled at Mizpah, they marched up against Israel. The Israelites, hearing this, were afraid of the Philistines.",
      "T": "Word reached the Philistine lords that Israel had assembled at Mizpah, and they seized the moment to advance against Israel. The Israelites, learning of the attack, were terrified."
    },
    "8": {
      "L": "And the children of Israel said to Samuel, Do not cease to cry to the LORD our God for us, that he may save us from the hand of the Philistines.",
      "M": "The Israelites said to Samuel, 'Do not stop crying out to the LORD our God for us, so that he may save us from the hand of the Philistines.'",
      "T": "The people turned to Samuel in their fear: 'Don't stop interceding for us before the LORD our God—we need him to rescue us from the Philistines.'"
    },
    "9": {
      "L": "And Samuel took a suckling lamb and offered it as a whole burnt offering unto the LORD; and Samuel cried to the LORD for Israel, and the LORD heard him.",
      "M": "Samuel took a nursing lamb and offered it as a whole burnt offering to the LORD, and cried out to the LORD on Israel's behalf—and the LORD answered him.",
      "T": "Samuel offered a nursing lamb as a whole burnt offering to the LORD, crying out to him on Israel's behalf. The LORD responded to his intercession."
    },
    "10": {
      "L": "And as Samuel was offering the burnt offering, the Philistines drew near to battle against Israel; but the LORD thundered with a great thundering upon the Philistines that day and threw them into confusion, and they were struck down before Israel.",
      "M": "As Samuel was offering the burnt offering, the Philistines advanced to attack Israel. But the LORD thundered with a great thunder against the Philistines that day, throwing them into panic, and they were routed before Israel.",
      "T": "Just as Samuel was presenting the burnt offering, the Philistines closed in for battle. Then the LORD unleashed his thunder against them—the sky itself became their enemy—and they fell into chaos and were cut down before Israel."
    },
    "11": {
      "L": "And the men of Israel went out from Mizpah and pursued the Philistines and struck them down as far as below Beth-car.",
      "M": "The men of Israel marched out from Mizpah, pursued the Philistines, and struck them down all the way to below Beth-car.",
      "T": "Israel's men poured out of Mizpah in pursuit and kept striking down Philistines all the way to the pass of Beth-car."
    },
    "12": {
      "L": "Then Samuel took a single stone and set it between Mizpah and Shen, and called its name Ebenezer, saying, Until now the LORD has helped us.",
      "M": "Samuel took a stone and set it up between Mizpah and Shen, naming it Ebenezer, saying, 'To this point the LORD has helped us.'",
      "T": "Samuel planted a standing stone between Mizpah and Shen as a permanent memorial, naming it Ebenezer—Stone of Help—proclaiming: 'Up to this very day the LORD has been our help.'"
    },
    "13": {
      "L": "So the Philistines were subdued and did not come again into the territory of Israel. And the hand of the LORD was against the Philistines all the days of Samuel.",
      "M": "The Philistines were brought low and did not again enter Israelite territory. The hand of the LORD was against the Philistines throughout Samuel's lifetime.",
      "T": "The Philistines were humbled and ceased to threaten Israel's borders. The LORD's restraining hand kept them at bay for as long as Samuel lived."
    },
    "14": {
      "L": "And the cities which the Philistines had taken from Israel were restored to Israel, from Ekron to Gath; and their territories did Israel recover from the hand of the Philistines. And there was peace between Israel and the Amorites.",
      "M": "The towns the Philistines had seized from Israel were restored, from Ekron to Gath, and Israel recovered their surrounding territories from Philistine control. There was also peace between Israel and the Amorites.",
      "T": "The towns seized by the Philistines were returned to Israel—from Ekron in the north to Gath in the south—and the surrounding regions were freed from Philistine control. Peace also settled between Israel and the Amorites."
    },
    "15": {
      "L": "And Samuel judged Israel all the days of his life.",
      "M": "Samuel judged Israel throughout his lifetime.",
      "T": "Samuel served as Israel's judge for the rest of his days."
    },
    "16": {
      "L": "And he went year by year in circuit to Bethel and Gilgal and Mizpah, and he judged Israel in all those places.",
      "M": "Each year he made a circuit to Bethel, Gilgal, and Mizpah, judging Israel at each of those sites.",
      "T": "Year after year Samuel made his rounds—Bethel, Gilgal, Mizpah—dispensing justice at each sacred center throughout the land."
    },
    "17": {
      "L": "And his return was to Ramah, for there was his house; and there he judged Israel; and there he built an altar to the LORD.",
      "M": "His home base was Ramah, where he lived, judged Israel, and built an altar to the LORD.",
      "T": "Ramah was his home, the hub of his ministry—there he gave judgment, and there he built an altar to the LORD, anchoring the nation's worship in the place where he lived."
    }
  },
  "8": {
    "1": {
      "L": "And it came to pass when Samuel was old, he made his sons judges over Israel.",
      "M": "When Samuel grew old, he appointed his sons as judges over Israel.",
      "T": "As Samuel aged, he installed his sons as judges in his place over Israel."
    },
    "2": {
      "L": "The name of his firstborn was Joel, and the name of his second, Abijah; they were judges in Beersheba.",
      "M": "His firstborn was named Joel and his second son Abijah; they served as judges at Beersheba.",
      "T": "His eldest was Joel, his second Abijah—both stationed as judges at Beersheba in the far south."
    },
    "3": {
      "L": "But his sons did not walk in his ways; they turned aside after dishonest gain, took bribes, and perverted justice.",
      "M": "But his sons did not follow his example—they turned to greed, accepted bribes, and twisted justice.",
      "T": "Unlike their father, Samuel's sons were corrupt: they pursued profit, took bribes, and bent justice to serve the highest bidder."
    },
    "4": {
      "L": "Then all the elders of Israel gathered together and came to Samuel at Ramah,",
      "M": "All the elders of Israel assembled and came to Samuel at Ramah,",
      "T": "The elders of Israel convened and traveled in delegation to Samuel at Ramah."
    },
    "5": {
      "L": "and said to him, Behold, you are old, and your sons do not walk in your ways; now make us a king to judge us, like all the nations.",
      "M": "They said to him, 'You are old, and your sons do not follow your ways. Appoint a king for us to rule us, as all the other nations have.'",
      "T": "They confronted Samuel directly: 'You are old, your sons have disgraced your name, and we need a new arrangement. Give us a king to govern us—the same as every other nation has.'"
    },
    "6": {
      "L": "But the thing was evil in Samuel's eyes when they said, Give us a king to judge us; and Samuel prayed to the LORD.",
      "M": "The request displeased Samuel when they said, 'Give us a king to judge us.' Samuel prayed to the LORD.",
      "T": "Samuel was deeply troubled by the demand for a king. He took his grievance to the LORD in prayer."
    },
    "7": {
      "L": "And the LORD said to Samuel, Hearken to the voice of the people in all that they say to you; for they have not rejected you, but they have rejected me from reigning over them.",
      "M": "The LORD said to Samuel, 'Listen to the voice of the people in everything they say to you; for they have not rejected you, but they have rejected me from reigning over them.'",
      "T": "The LORD addressed Samuel's pain: 'Do what the people are asking. Their rejection is not of you—it is of me. They have refused my kingship over them.'"
    },
    "8": {
      "L": "According to all the works which they have done from the day I brought them up out of Egypt even to this day—forsaking me and serving other gods—so they do also to you.",
      "M": "This is consistent with everything they have done since the day I brought them up out of Egypt to this day—forsaking me and serving other gods. Now they are doing the same to you.",
      "T": "This is simply the same old pattern: from the day I brought them out of Egypt to this very day, they have abandoned me and run after other gods. Now they are abandoning my direct rule—and in doing so, they are slighting you as well."
    },
    "9": {
      "L": "Now therefore hearken to their voice; yet solemnly warn them, and declare to them the manner of the king who shall reign over them.",
      "M": "So comply with their request; but first solemnly warn them and describe to them the practice of the king who will reign over them.",
      "T": "Give them what they want—but make sure they understand the cost. Lay out plainly what a king will do to them."
    },
    "10": {
      "L": "And Samuel told all the words of the LORD to the people who asked a king of him.",
      "M": "Samuel reported all the LORD's words to the people who had asked him for a king.",
      "T": "Samuel laid out everything the LORD had told him before the people who were demanding a king."
    },
    "11": {
      "L": "He said, This will be the manner of the king who will reign over you: he will take your sons and appoint them for himself—for his chariots and his horsemen—and some will run before his chariots.",
      "M": "He said, 'This is what the king who reigns over you will do: he will take your sons and assign them to his chariot corps and cavalry, with some running before his chariots.'",
      "T": "Samuel spelled it out: 'Here is what your king will actually do. He will conscript your sons—pressed into service for his chariot force, his cavalry, runners clearing the royal road.'"
    },
    "12": {
      "L": "He will appoint for himself commanders of thousands and commanders of fifties, and will set them to plow his ground and reap his harvest, and to make his weapons of war and equipment for his chariots.",
      "M": "He will appoint commanders over thousands and fifties, and will put your sons to work plowing his fields, harvesting his crops, and making his weapons and chariot equipment.",
      "T": "He will organize them into military units—officers over thousands and over fifties—and draft others into agricultural labor: plowing his estates, harvesting his crops, fashioning his weapons and war equipment."
    },
    "13": {
      "L": "He will take your daughters to be perfumers and cooks and bakers.",
      "M": "He will take your daughters to serve as perfumers, cooks, and bakers.",
      "T": "Your daughters will not escape either—conscripted as perfumers, cooks, and bakers for the royal household."
    },
    "14": {
      "L": "He will take your fields and your vineyards and your olive orchards—the best of them—and give them to his servants.",
      "M": "He will seize your best fields, vineyards, and olive groves and hand them over to his officials.",
      "T": "The best of your fields, vineyards, and orchards—he will confiscate them and redistribute them to his own men."
    },
    "15": {
      "L": "He will take a tenth of your grain and your vineyards and give it to his officers and servants.",
      "M": "He will tithe your grain and your vineyards, distributing the proceeds among his officers and staff.",
      "T": "A royal tithe on your crops and your wine—taken and handed to the bureaucrats who serve him."
    },
    "16": {
      "L": "He will take your male servants and your female servants and your best young men and your donkeys, and put them to his labor.",
      "M": "He will take your male and female servants, your finest young men, and your donkeys, and put them all to work for himself.",
      "T": "Your servants—male and female—your most capable young men and your work animals: all pressed into the king's service."
    },
    "17": {
      "L": "He will take a tenth of your flocks, and you yourselves will be his servants.",
      "M": "He will take a tenth of your flocks, and you will become his subjects.",
      "T": "He will tithe your flocks—and in the end, you yourselves will be his slaves."
    },
    "18": {
      "L": "And you will cry out in that day on account of your king whom you have chosen for yourselves; and the LORD will not hear you in that day.",
      "M": "In that day you will cry out because of the king you have chosen for yourselves, but the LORD will not answer you.",
      "T": "That day will come—the day you cry out under your king's oppression. You chose him; and on that day, the LORD will not answer your cries."
    },
    "19": {
      "L": "But the people refused to listen to the voice of Samuel and said, No, but there shall be a king over us,",
      "M": "But the people refused to listen to Samuel and said, 'No! We will have a king over us—'",
      "T": "The people would not be dissuaded. 'No,' they said flatly. 'We want a king.'"
    },
    "20": {
      "L": "that we also may be like all the nations, and that our king may judge us and go out before us and fight our battles.",
      "M": "'—so that we may be like all the other nations, with our king to rule us, lead us out, and fight our battles.'",
      "T": "'We want to be like every other nation. Our king will govern us, lead us into battle, and fight for us.' They refused to see that this was already the LORD's role."
    },
    "21": {
      "L": "And Samuel heard all the words of the people and repeated them in the ears of the LORD.",
      "M": "Samuel listened to all the people's words and then brought them before the LORD.",
      "T": "Samuel took everything the people had said and laid it all before the LORD."
    },
    "22": {
      "L": "And the LORD said to Samuel, Hearken to their voice and make them a king. And Samuel said to the men of Israel, Go every man to his city.",
      "M": "The LORD told Samuel, 'Listen to their voice and give them a king.' Then Samuel said to the men of Israel, 'Each of you, return to your town.'",
      "T": "The LORD gave his final word: 'Grant their request. Give them a king.' Samuel then dismissed the assembly: 'Go home, each to his own town.'"
    }
  },
  "9": {
    "1": {
      "L": "Now there was a man of Benjamin whose name was Kish, son of Abiel, son of Zeror, son of Bechorath, son of Aphiah, a Benjaminite, a mighty man of valor.",
      "M": "There was a Benjaminite named Kish son of Abiel son of Zeror son of Bechorath son of Aphiah—a Benjaminite and a man of great standing.",
      "T": "In the tribe of Benjamin there was a man named Kish—son of Abiel, of the lineage of Zeror, Bechorath, and Aphiah—a man of standing and substance."
    },
    "2": {
      "L": "He had a son named Saul, a handsome young man; among all the children of Israel there was no one more handsome than he—from his shoulders upward he was taller than all the people.",
      "M": "He had a son named Saul, a fine-looking young man—no one among the Israelites was more handsome; from his shoulders up he stood taller than all the people.",
      "T": "His son was named Saul—a striking young man, the most impressive figure in all Israel. He stood head and shoulders above everyone else, exactly the kind of man that honor culture prized."
    },
    "3": {
      "L": "Now the donkeys of Kish, Saul's father, were lost. And Kish said to Saul his son, Take with you one of the servants and go seek the donkeys.",
      "M": "The donkeys of Kish, Saul's father, had gone astray. Kish told his son Saul, 'Take one of the servants and go look for the donkeys.'",
      "T": "Kish's donkeys had wandered off—a significant loss for a household. Kish sent Saul out: 'Take one of the servants and find them.'"
    },
    "4": {
      "L": "He passed through the hill country of Ephraim and through the land of Shalisha, but they did not find them; they passed through the land of Shalim, and they were not there; and he passed through the land of the Benjaminites, but they did not find them.",
      "M": "He traveled through the hill country of Ephraim and through the region of Shalisha, but they did not find the donkeys. They went through Shalim—not there either. They crossed the land of Benjamin—still nothing.",
      "T": "Saul searched systematically—through Ephraim's highlands, through Shalisha, through Shalim—widening his search, but the donkeys were nowhere to be found. Even in his own tribal territory of Benjamin, nothing."
    },
    "5": {
      "L": "When they came to the land of Zuph, Saul said to his servant with him, Come, let us return, lest my father stop caring about the donkeys and start worrying about us.",
      "M": "When they reached the land of Zuph, Saul said to his servant, 'Let's go back, or my father will stop worrying about the donkeys and start worrying about us.'",
      "T": "When they reached Zuph, Saul was ready to turn back. 'We've gone too far,' he said to his servant. 'My father has probably forgotten the donkeys by now and is worried sick about us.'"
    },
    "6": {
      "L": "He said to him, Behold, in this city there is a man of God, and he is a man of honor; all that he says comes surely to pass. Now let us go there; perhaps he can tell us about our journey on which we have set out.",
      "M": "The servant replied, 'Look, in this town there is a man of God—a man of distinction whose every word proves true. Let's go there; perhaps he can tell us which way we should go.'",
      "T": "The servant had a better idea: 'There's a man of God in this town—highly regarded, and everything he says comes true. Let's consult him. He may be able to point us in the right direction.'"
    },
    "7": {
      "L": "Then said Saul to his servant, But behold, if we go, what shall we bring the man? For the bread is gone from our packs, and there is no present to bring to the man of God. What do we have?",
      "M": "Saul replied to his servant, 'But if we go, what can we bring the man? Our food is gone, and we have no gift to offer the man of God. What do we have?'",
      "T": "Saul thought of the protocol: 'We can't approach a man of honor empty-handed. Our provisions are finished—we have nothing worthy to offer him. What can we bring?'"
    },
    "8": {
      "L": "The servant answered Saul again and said, Behold, I have with me the fourth part of a shekel of silver; that I will give to the man of God, and he will tell us our way.",
      "M": "The servant replied, 'I happen to have a quarter shekel of silver with me. I'll give that to the man of God and he can tell us which way to go.'",
      "T": "The servant checked his purse: 'I have a quarter-shekel of silver. That will do as an honorarium—enough to present to the man of God in exchange for guidance.'"
    },
    "9": {
      "L": "(Formerly in Israel, when a man went to inquire of God, he said, Come, let us go to the seer; for the one now called a prophet was formerly called a seer.)",
      "M": "(In former times in Israel, anyone seeking to inquire of God would say, 'Come, let us go to the seer,' since the one now called a prophet was then called a seer.)",
      "T": "(A note for the reader: in earlier times in Israel, such a person was called a 'seer'—the term 'prophet' came later. When Saul's servant said 'man of God,' he meant what an older Israelite would have called a seer.)"
    },
    "10": {
      "L": "Then Saul said to his servant, Well said; come, let us go. So they went to the city where the man of God was.",
      "M": "Saul replied, 'Good idea—let's go.' So they headed for the town where the man of God lived.",
      "T": "'Perfect,' said Saul. 'Let's go.' They set off for the town where the man of God resided."
    },
    "11": {
      "L": "As they went up the ascent to the city, they met young women going out to draw water, and said to them, Is the seer here?",
      "M": "As they climbed the approach to the town, they met some young women going out to draw water and asked them, 'Is the seer here?'",
      "T": "On the road up to the town they met a group of young women heading to the well and asked them, 'Is the seer in town?'"
    },
    "12": {
      "L": "They answered them and said, He is; behold, he is ahead of you. Hurry now, for he has come to the city today because the people have a sacrifice at the high place today.",
      "M": "They replied, 'He is—in fact, he's right ahead of you. Hurry, because he came to town today for a sacrifice the people are holding at the high place.'",
      "T": "The women answered eagerly: 'Yes, he's here—just ahead of you, in fact. Hurry, or you'll miss him. He came in today for a public sacrifice at the worship site on the hill.'"
    },
    "13": {
      "L": "As soon as you enter the city you will find him, before he goes up to the high place to eat; for the people will not eat until he comes, because he blesses the sacrifice; and afterward, those invited eat. Now go up, for you will find him about this time.",
      "M": "When you enter the town you'll find him right away, before he goes up to the high place to eat. The people won't eat until he arrives, because he pronounces the blessing over the sacrifice; only then do the guests eat. Go now—you'll find him at this very hour.",
      "T": "'The moment you enter town you'll see him—he hasn't gone up to the feast yet. The whole gathering waits for him to arrive and pronounce the blessing before anyone can eat. Go now, and you'll catch him in time.'"
    },
    "14": {
      "L": "They went up into the city; and as they entered the city, behold, Samuel came out toward them on his way up to the high place.",
      "M": "They went into the town, and as they entered, Samuel was coming out toward them on his way up to the high place.",
      "T": "They entered the town—and at that very moment, Samuel was coming out right toward them, heading up to the high place."
    },
    "15": {
      "L": "Now the LORD had revealed to Samuel in his ear one day before Saul came, saying,",
      "M": "The LORD had disclosed to Samuel the day before Saul arrived, saying,",
      "T": "The narrator steps back: the day before, the LORD had spoken privately into Samuel's ear—"
    },
    "16": {
      "L": "Tomorrow about this time I will send you a man from the land of Benjamin, and you shall anoint him as captain over my people Israel; and he shall save my people from the hand of the Philistines. For I have seen my people, for their cry has come to me.",
      "M": "'Tomorrow about this time I will send you a man from Benjamin—anoint him as ruler over my people Israel, to save them from the hand of the Philistines. I have seen the suffering of my people and their cry has come up to me.'",
      "T": "'Tomorrow at this time I am sending you a Benjaminite—anoint him as the designated leader of my people Israel. He will rescue them from Philistia. I have heard my people's cry and I have seen their distress.'"
    },
    "17": {
      "L": "When Samuel saw Saul, the LORD told him, Behold, this is the man of whom I spoke to you. He it is who shall restrain my people.",
      "M": "When Samuel saw Saul, the LORD said to him, 'Here is the man I told you about—he will govern my people.'",
      "T": "The moment Samuel laid eyes on Saul, the LORD spoke: 'That is the man I told you about. He will be the one to govern my people.'"
    },
    "18": {
      "L": "Then Saul drew near to Samuel in the gateway and said, Tell me, I pray you, where is the seer's house?",
      "M": "Saul approached Samuel at the gate and said, 'Excuse me—could you tell me where the seer's house is?'",
      "T": "Saul stepped up to Samuel at the town gate—not knowing who he was speaking to—and asked, 'Pardon me, where does the seer live?'"
    },
    "19": {
      "L": "Samuel answered Saul and said, I am the seer. Go up before me to the high place, for you shall eat with me today; and tomorrow I will send you on your way and will tell you all that is in your heart.",
      "M": "Samuel replied, 'I am the seer. Come up ahead of me to the high place—you will dine with me today, and tomorrow I will send you on your way and tell you everything that is on your mind.'",
      "T": "'I am the seer,' Samuel answered, before Saul could say more. 'Come with me to the high place—you will be my guest at the feast today. Tomorrow I'll send you home, and before you go I will answer everything that weighs on you.'"
    },
    "20": {
      "L": "And as for your donkeys that were lost three days ago, do not set your mind on them, for they are found. And on whom is all the desire of Israel? Is it not on you and on all your father's house?",
      "M": "As for the donkeys you lost three days ago—don't worry about them; they have been found. And as for whom all Israel desires—is it not you, and your whole family?",
      "T": "'And your missing donkeys—three days of searching is over: they've been found. Don't give them another thought.' He paused. 'Tell me—do you have any idea who it is that all Israel longs for? It is you. You and your whole family.'"
    },
    "21": {
      "L": "And Saul answered and said, Am I not a Benjaminite, of the smallest of the tribes of Israel? And my family the least of all the families of the tribe of Benjamin? Why then do you speak to me like this?",
      "M": "Saul answered, 'But I'm a Benjaminite—from the smallest tribe in Israel! My family is the least of all Benjamin's clans. Why do you speak to me like this?'",
      "T": "Saul was flustered. 'My tribe is Benjamin—the smallest in Israel. My clan is the least of all Benjamin's families. You must be speaking to the wrong man.'"
    },
    "22": {
      "L": "Samuel took Saul and his servant and brought them into the hall and gave them a place at the head of those who were invited, who were about thirty men.",
      "M": "Samuel brought Saul and his servant into the banquet hall and seated them at the head of the table among the roughly thirty invited guests.",
      "T": "Samuel himself escorted Saul and his servant into the banquet hall and seated them in the place of honor—ahead of the thirty or so assembled guests."
    },
    "23": {
      "L": "Samuel said to the cook, Bring the portion that I gave you, of which I said to you, Set it aside.",
      "M": "Samuel instructed the cook, 'Bring out the portion I gave you—the one I told you to set aside.'",
      "T": "Samuel turned to the cook: 'Bring the portion I reserved—the one I asked you to set aside.'"
    },
    "24": {
      "L": "The cook lifted up the shoulder and what was on it and set it before Saul. And Samuel said, See, what was kept! Set it before you and eat, for it was kept for you until this appointed time, since I said I had invited the people. So Saul ate with Samuel that day.",
      "M": "The cook lifted up the thigh portion and what was on it and placed it before Saul. Samuel said, 'Look—this has been reserved for you. Eat it, for it was set aside for you until this moment, from the time I invited the guests.' So Saul ate with Samuel that day.",
      "T": "The cook produced a choice cut—the shoulder—with all the trimmings, and set it before Saul. Samuel explained: 'This has been held for you. From the moment I called the gathering, I set this portion aside—for you, for today.' Saul dined with Samuel, honored guest of the prophet."
    },
    "25": {
      "L": "When they came down from the high place into the city, Samuel spoke with Saul on the roof.",
      "M": "When they came down from the high place to the town, Samuel talked with Saul on the roof of the house.",
      "T": "After the feast, when they had come down from the high place into the town, Samuel drew Saul aside for a private conversation on the rooftop—the customary place for intimate, confidential talk."
    },
    "26": {
      "L": "And they rose early; and it came to pass about the break of day that Samuel called to Saul on the roof, saying, Arise, that I may send you on your way. And Saul arose, and both of them went outside, he and Samuel.",
      "M": "They rose early, and at dawn Samuel called up to Saul on the roof, 'Up—I'll send you on your way.' Saul got up and the two of them went out together.",
      "T": "They slept, and at the first light of dawn Samuel called up to Saul on the roof: 'Rise—it's time for you to go.' Saul rose, and the two went out into the early morning together."
    },
    "27": {
      "L": "And as they were going down to the edge of the city, Samuel said to Saul, Tell the servant to pass on ahead of us—and he passed on—but you stand still now, that I may make you hear the word of God.",
      "M": "As they reached the edge of town, Samuel told Saul, 'Send the servant on ahead of us'—and he did—'but you stay here a moment, so I can make the word of God known to you.'",
      "T": "As they reached the outskirts of town, Samuel stopped Saul: 'Send your servant ahead.' The servant went on. 'You stay back with me,' Samuel said. 'I have a word from God to give you.'"
    }
  },
  "10": {
    "1": {
      "L": "Then Samuel took a flask of oil and poured it upon his head and kissed him and said, Is it not that the LORD has anointed you captain over his inheritance?",
      "M": "Samuel took a flask of oil, poured it over his head, and kissed him, saying, 'The LORD has anointed you ruler over his inheritance!'",
      "T": "Samuel poured the flask of oil over Saul's head, kissed him, and declared: 'See what this means—the LORD himself has anointed you as the designated leader of his inheritance, his people.'"
    },
    "2": {
      "L": "When you depart from me today, you will find two men by Rachel's tomb in the border of Benjamin at Zelzah; they will say to you, The donkeys you went to seek are found; your father has given up on the donkeys and now is anxious for you, saying, What shall I do about my son?",
      "M": "When you leave me today, you will meet two men near Rachel's tomb in Benjaminite territory at Zelzah. They will tell you, 'The donkeys you were looking for have been found, but now your father has stopped thinking about the donkeys and is worried about you, asking, \"What's become of my son?\"'",
      "T": "Samuel gave him three signs to confirm the anointing. 'First: when you leave me today, near Rachel's tomb in Benjamin at Zelzah you will meet two men who will tell you the donkeys are found—but that your father has stopped worrying about donkeys and started worrying about you, saying, \"What has happened to my son?\"'"
    },
    "3": {
      "L": "And you shall go on from there and come to the oak of Tabor; and three men going up to God at Bethel will meet you there, one carrying three kids, another carrying three loaves of bread, and another carrying a skin of wine.",
      "M": "From there you will go on to the oak of Tabor, where you will meet three men on their way up to God at Bethel—one carrying three young goats, another three loaves of bread, and another a skin of wine.",
      "T": "'Second sign: at the oak of Tabor you will meet three men going up to Bethel to worship God—one with three young goats, one with three loaves of bread, one with a wineskin.'"
    },
    "4": {
      "L": "They will greet you and give you two loaves of bread, which you shall take from their hands.",
      "M": "They will greet you and offer you two of their loaves of bread, which you must take from them.",
      "T": "'They will greet you and press two of their loaves into your hands—accept them.'"
    },
    "5": {
      "L": "After that you shall come to Gibeah-elohim, where there is a garrison of the Philistines; and when you enter the city there, you will meet a band of prophets coming down from the high place with harp, tambourine, flute, and lyre before them, and they will be prophesying.",
      "M": "After that you will come to Gibeah-elohim, where the Philistine garrison is. As you enter the town, you will meet a group of prophets coming down from the high place playing harp, tambourine, flute, and lyre—all prophesying.",
      "T": "'Third sign: at Gibeah of God—in the shadow of a Philistine garrison—you will encounter a band of prophets descending from the worship site, all playing instruments and prophesying in ecstatic worship.'"
    },
    "6": {
      "L": "And the Spirit of the LORD will come upon you, and you shall prophesy with them and be turned into another man.",
      "M": "The Spirit of the LORD will come powerfully upon you, and you will prophesy with them and be changed into a different person.",
      "T": "'And then the Spirit of the LORD will sweep over you—you will prophesy with them, and you will be transformed. You will not be the same man who left home this morning.'"
    },
    "7": {
      "L": "And when these signs meet you, do whatever your hand finds to do, for God is with you.",
      "M": "Once these signs have occurred, act as the situation demands—for God is with you.",
      "T": "'When these three signs have happened, trust your judgment and act decisively—because God will be with you.'"
    },
    "8": {
      "L": "Then you shall go down before me to Gilgal, and behold, I will come down to you to offer burnt offerings and sacrifice peace offerings; seven days you shall wait, until I come to you and show you what you are to do.",
      "M": "Then go down to Gilgal ahead of me. I will come down to you there to offer burnt offerings and peace offerings. Wait seven days until I arrive—I will tell you what to do next.",
      "T": "'Go down to Gilgal ahead of me. I will follow to offer burnt and peace offerings. Wait the full seven days for me to come—I will tell you then what your next step must be.' This instruction would become a fateful test."
    },
    "9": {
      "L": "When he turned from Samuel to go, God gave him another heart; and all those signs came to pass that day.",
      "M": "As Saul turned to leave Samuel, God gave him a new heart, and all the signs came to pass that day.",
      "T": "The moment Saul turned to leave Samuel, God transformed him from within—a new heart. And each of the three signs came to pass exactly as Samuel had described, all in one day."
    },
    "10": {
      "L": "When they came there to the hill, a band of prophets met him; and the Spirit of God came upon him, and he prophesied among them.",
      "M": "When they arrived at the hill, a group of prophets came to meet him. The Spirit of God came powerfully upon him, and he prophesied among them.",
      "T": "At the hill, the band of prophets met them just as foretold, and the Spirit of God rushed over Saul—and he prophesied in their midst."
    },
    "11": {
      "L": "And when all who knew him beforetime saw that he prophesied among the prophets, the people said to one another, What has happened to the son of Kish? Is Saul also among the prophets?",
      "M": "When everyone who had known him before saw that he was prophesying with the prophets, people said to one another, 'What has come over the son of Kish? Is Saul also among the prophets?'",
      "T": "The bystanders who knew Saul were astonished. 'What has gotten into the son of Kish?' they said to each other. 'Since when is Saul a prophet?' The question became a proverb."
    },
    "12": {
      "L": "And a man from that place answered and said, And who is their father? Therefore it became a proverb: Is Saul also among the prophets?",
      "M": "Someone from that place answered, 'And who is their father?' That is how the saying originated: 'Is Saul also among the prophets?'",
      "T": "Someone in the crowd cut through the amazement with a pointed question: 'Who is anyone's father among the prophets?' Prophetic gifting is not inherited—it is given. And so the saying was coined: 'Is Saul also among the prophets?'"
    },
    "13": {
      "L": "And when he had finished prophesying, he came to the high place.",
      "M": "When he had finished prophesying, he went to the high place.",
      "T": "When the prophetic episode was over, Saul made his way to the worship site."
    },
    "14": {
      "L": "Saul's uncle said to him and to his servant, Where did you go? He said, To seek the donkeys; and when we saw they were nowhere to be found, we went to Samuel.",
      "M": "Saul's uncle asked him and his servant, 'Where did you go?' He replied, 'Looking for the donkeys. When we couldn't find them, we went to Samuel.'",
      "T": "Saul's uncle met him and asked, 'Where have you been?' Saul kept it simple: 'We went looking for the donkeys. When we couldn't find them, we went to see Samuel.'"
    },
    "15": {
      "L": "Saul's uncle said, Tell me, I pray you, what Samuel said to you.",
      "M": "His uncle pressed him, 'Tell me what Samuel said to you.'",
      "T": "The uncle pressed further: 'Tell me—what exactly did Samuel say?'"
    },
    "16": {
      "L": "Saul said to his uncle, He told us plainly that the donkeys were found. But the matter of the kingdom, of which Samuel had spoken, he did not tell him.",
      "M": "Saul replied, 'He told us clearly that the donkeys had been found.' But the matter of the kingship that Samuel had spoken of, Saul said nothing.",
      "T": "Saul answered calmly: 'He told us the donkeys were found.' The kingship—Samuel's private words about that—he kept entirely to himself."
    },
    "17": {
      "L": "And Samuel called the people together before the LORD at Mizpah;",
      "M": "Samuel summoned the people before the LORD at Mizpah.",
      "T": "Samuel convened a national assembly before the LORD at Mizpah."
    },
    "18": {
      "L": "and said to the children of Israel, Thus says the LORD, the God of Israel: I brought up Israel from Egypt and delivered you from the hand of the Egyptians and from the hand of all the kingdoms that were pressing hard upon you.",
      "M": "He said to the Israelites, 'This is what the LORD, the God of Israel, says: I brought Israel up out of Egypt and rescued you from the power of Egypt and all the kingdoms that were oppressing you.'",
      "T": "He addressed the assembly: 'Hear the word of the LORD, the God of Israel: I am the one who brought you up out of Egypt and delivered you from every empire and every adversary that ground you down.'"
    },
    "19": {
      "L": "But today you have rejected your God who saves you from all your troubles and your distresses, and you have said to him, No, but set a king over us. Now therefore present yourselves before the LORD by your tribes and by your thousands.",
      "M": "But today you have rejected your God—the one who has saved you from every calamity and distress—and have said to him, 'No, put a king over us.' Now, then, present yourselves before the LORD by tribes and by thousands.",
      "T": "'And today—today—you have rejected the very God who has saved you in every crisis, every disaster. You have told him, \"We don't want you; give us a king.\" Very well. Come forward before the LORD, tribe by tribe, clan by clan.'"
    },
    "20": {
      "L": "And when Samuel had brought all the tribes of Israel near, the tribe of Benjamin was taken by lot.",
      "M": "Samuel brought all the tribes of Israel forward, and the tribe of Benjamin was chosen by lot.",
      "T": "Samuel began the selection. Tribe by tribe came forward—and the lot fell on Benjamin."
    },
    "21": {
      "L": "He brought the tribe of Benjamin near by their clans, and the clan of Matri was taken; and Saul the son of Kish was taken. But when they sought him, he could not be found.",
      "M": "He brought Benjamin forward by clans, and the clan of Matri was chosen; then Saul son of Kish was chosen. But when they looked for him, he was nowhere to be found.",
      "T": "Within Benjamin, the clan of Matri was selected—and from that clan, Saul son of Kish. But when they went to present him, Saul was nowhere to be found."
    },
    "22": {
      "L": "Therefore they inquired further of the LORD, Has the man come here yet? And the LORD said, Behold, he has hidden himself among the baggage.",
      "M": "They consulted the LORD further, asking, 'Has the man arrived yet?' The LORD replied, 'He has hidden himself among the luggage.'",
      "T": "They turned to the LORD: 'Has he even come?' The LORD answered: 'He is hiding among the baggage.'"
    },
    "23": {
      "L": "And they ran and brought him from there; and when he stood among the people, he was taller than any of the people from his shoulders upward.",
      "M": "They ran and brought him out; when he stood among the people, he was a head taller than everyone else.",
      "T": "They pulled him out from among the equipment and brought him before the crowd. He stood a head above every person there—unmistakably the most imposing figure in the assembly."
    },
    "24": {
      "L": "And Samuel said to all the people, Do you see the one whom the LORD has chosen? There is none like him among all the people. And all the people shouted and said, Long live the king!",
      "M": "Samuel said to all the people, 'Do you see who the LORD has chosen? There is no one like him in all the people.' The people all shouted, 'Long live the king!'",
      "T": "Samuel presented him: 'Look at the man the LORD has chosen—there is none like him in all Israel!' The crowd erupted: 'Long live the king!'"
    },
    "25": {
      "L": "Then Samuel told the people the manner of the kingdom and wrote it in a book and laid it before the LORD. And Samuel sent all the people away, each to his house.",
      "M": "Samuel then explained to the people the rights and duties of the kingship, wrote them in a document, and deposited it before the LORD. He dismissed all the people, each to their own home.",
      "T": "Samuel then set out the terms of the kingship—the rights and limits of the institution—recorded them in writing, and placed the document before the LORD as a covenant text. He dismissed the assembly, each person to their home."
    },
    "26": {
      "L": "Saul also went to his home at Gibeah, and with him went the band of men whose hearts God had touched.",
      "M": "Saul went to his home at Gibeah, accompanied by men whose hearts God had moved.",
      "T": "Saul returned home to Gibeah, and a company of men followed him—men whose hearts God had stirred to loyalty."
    },
    "27": {
      "L": "But the worthless men said, How can this man deliver us? And they despised him and brought him no tribute. But he kept silent.",
      "M": "But certain worthless men said, 'How is this man going to save us?' They despised him and brought him no gift. But Saul said nothing.",
      "T": "But some men of no worth sneered: 'How is this one going to save us?' They withheld the customary gifts of homage. Saul heard it all and said nothing—a sign of remarkable self-control."
    }
  },
  "11": {
    "1": {
      "L": "Then Nahash the Ammonite came up and camped against Jabesh-gilead; and all the men of Jabesh said to Nahash, Make a covenant with us and we will serve you.",
      "M": "Nahash the Ammonite came up and besieged Jabesh-gilead. The men of Jabesh said to him, 'Make a treaty with us and we will serve you.'",
      "T": "Nahash the Ammonite led his army up and encircled Jabesh-gilead. Caught off guard, the men of the town proposed surrender: 'Make a pact with us and we will submit to you.'"
    },
    "2": {
      "L": "And Nahash the Ammonite answered them, On this condition will I make a covenant with you: that I thrust out all your right eyes, and so bring disgrace on all Israel.",
      "M": "Nahash replied, 'I will make terms on one condition: I will gouge out the right eye of every one of you, and thereby shame all Israel.'",
      "T": "Nahash named his terms with deliberate brutality: 'Here is my one condition—I will blind every right eye among you, and through you I will brand all Israel with permanent shame.' He intended it as a humiliation of the whole nation."
    },
    "3": {
      "L": "And the elders of Jabesh said to him, Give us seven days' respite, that we may send messengers through all the territory of Israel; and if there is no one to save us, we will come out to you.",
      "M": "The elders of Jabesh said, 'Grant us a seven-day delay to send messengers throughout Israel; if no one comes to rescue us, we will surrender to you.'",
      "T": "The elders of Jabesh bought time: 'Give us seven days to send throughout Israel. If no one comes to our rescue, we will hand ourselves over.' Nahash agreed—probably confident that no one would answer."
    },
    "4": {
      "L": "When the messengers came to Gibeah of Saul and reported the news to the people, all the people lifted up their voices and wept.",
      "M": "The messengers came to Gibeah of Saul and reported the news to the people. The entire town raised their voices and wept.",
      "T": "The messengers reached Gibeah—Saul's own town—and read out the desperate situation of Jabesh-gilead. The people broke down weeping."
    },
    "5": {
      "L": "And behold, Saul was coming in from the field behind the oxen; and Saul said, What is wrong with the people that they weep? They told him the news of the men of Jabesh.",
      "M": "Just then Saul was coming in from the field behind his oxen. 'What is wrong with the people?' he asked. 'Why are they weeping?' They told him what the men of Jabesh faced.",
      "T": "Saul was out plowing when he returned—still the farmer, not yet the king in practice. Seeing the weeping, he asked what had happened. They told him Jabesh-gilead's ultimatum."
    },
    "6": {
      "L": "And the Spirit of God came upon Saul when he heard those words, and his anger burned fiercely.",
      "M": "The Spirit of God came powerfully upon Saul when he heard those words, and he burned with fury.",
      "T": "When Saul heard the news, the Spirit of God came upon him—and his anger blazed. This was not personal rage; this was the righteous wrath of a man seized by divine commission."
    },
    "7": {
      "L": "He took a yoke of oxen and cut them in pieces and sent them throughout all the territory of Israel by the hand of messengers, saying, Whoever does not come out after Saul and Samuel, so shall it be done to his oxen. And the fear of the LORD fell upon the people, and they came out as one man.",
      "M": "He took a yoke of oxen, cut them in pieces, and sent the pieces throughout Israel by messenger, declaring, 'This is what will be done to the oxen of any man who does not march out with Saul and Samuel.' The terror of the LORD fell on the people and they turned out as one.",
      "T": "Saul slaughtered his own oxen—the tools of his livelihood—cut them up, and sent the pieces to every corner of Israel with this ultimatum: 'March out with Saul and Samuel, or this is what will happen to your livestock.' It was a coercive call-up in the ancient manner. The LORD's dread fell on the nation, and the people rallied as one."
    },
    "8": {
      "L": "When he mustered them at Bezek, the men of Israel were three hundred thousand, and the men of Judah thirty thousand.",
      "M": "He mustered them at Bezek: three hundred thousand Israelites and thirty thousand from Judah.",
      "T": "At Bezek, Saul took the muster: three hundred thousand from Israel, thirty thousand from Judah—a massive national response."
    },
    "9": {
      "L": "They said to the messengers who had come, Thus shall you say to the men of Jabesh-gilead: Tomorrow, when the sun is hot, you will have deliverance. The messengers came and told the men of Jabesh, and they rejoiced.",
      "M": "They told the messengers, 'Say this to the men of Jabesh-gilead: By tomorrow at noon you will be rescued.' When the messengers returned and told them, the men of Jabesh were overjoyed.",
      "T": "The messengers were sent back to Jabesh with word: 'By tomorrow when the sun is high—help is coming.' They brought the news back to the besieged town, and the people were flooded with relief."
    },
    "10": {
      "L": "Then the men of Jabesh said to Nahash, Tomorrow we will come out to you, and you shall do to us whatever seems good to you.",
      "M": "So the men of Jabesh told Nahash, 'Tomorrow we will come out to you, and you may do with us whatever you see fit.'",
      "T": "The men of Jabesh played along with Nahash: 'Come back tomorrow, and we will surrender on whatever terms you choose.' They were buying the night—and an army was on its way."
    },
    "11": {
      "L": "And on the next day Saul put the people in three companies; they came into the midst of the camp in the morning watch and struck down Ammonites until the heat of the day. The survivors were scattered—not even two of them were left together.",
      "M": "The next morning Saul divided the force into three columns. They attacked the Ammonite camp in the last watch of the night and struck them down until the heat of the day. The survivors were so scattered that no two were left together.",
      "T": "Before dawn, Saul divided his army into three strike forces and launched a surprise assault on the Ammonite camp in the darkest watch of the night. They fought through the morning until the heat of the day, and the Ammonites were utterly broken—survivors scattered, unable to regroup, not two men standing together."
    },
    "12": {
      "L": "Then the people said to Samuel, Who said, Shall Saul reign over us? Bring the men that we may put them to death.",
      "M": "The people said to Samuel, 'Who said, \"Shall Saul reign over us?\" Hand those men over—we'll put them to death.'",
      "T": "Flush with victory, the crowd turned to Samuel with blood in their eyes: 'Who were those men who said Saul couldn't save us? Bring them here—we'll execute them.'"
    },
    "13": {
      "L": "But Saul said, Not a man shall be put to death this day, for today the LORD has wrought salvation in Israel.",
      "M": "But Saul said, 'No one shall be put to death today, for today the LORD has given Israel victory.'",
      "T": "Saul stopped it. 'No one dies today,' he declared. 'This is a day of victory—the LORD has rescued Israel. We will not stain it with vengeance.'"
    },
    "14": {
      "L": "Then Samuel said to the people, Come, let us go to Gilgal and renew the kingdom there.",
      "M": "Samuel said to the people, 'Let us go to Gilgal and reaffirm the kingship there.'",
      "T": "Samuel seized the moment: 'Come—all of us to Gilgal. We will solemnly renew the covenant of the kingdom there.'"
    },
    "15": {
      "L": "And all the people went to Gilgal, and there they made Saul king before the LORD in Gilgal; and there they sacrificed peace offerings before the LORD; and there Saul and all the men of Israel rejoiced greatly.",
      "M": "All the people went to Gilgal, where they crowned Saul king before the LORD. They offered peace offerings before the LORD, and Saul and all the Israelites rejoiced greatly.",
      "T": "The whole nation went to Gilgal. There, before the LORD, Saul was publicly acclaimed and established as king. Peace offerings were sacrificed in celebration. Saul and all Israel rejoiced—a great, jubilant renewal of the covenant between king, people, and God."
    }
  },
  "12": {
    "1": {
      "L": "And Samuel said to all Israel, Behold, I have listened to your voice in all that you said to me and have made a king over you.",
      "M": "Samuel addressed all Israel: 'I have listened to you in everything you asked of me and have set a king over you.'",
      "T": "With the kingdom established, Samuel stood before all Israel to make his farewell as governor. 'I have done what you asked,' he said. 'I have listened to you and given you a king.'"
    },
    "2": {
      "L": "And now, behold, the king walks before you; and I am old and gray; and behold, my sons are among you. I have walked before you from my youth to this day.",
      "M": "See, the king now leads you—and I am old and gray. My sons are here with you. I have served before you from my youth until this day.",
      "T": "'Look: the king now walks before you. I am old and white-haired; my sons are here among you. From my youth until today I have served before you—and before your God.'"
    },
    "3": {
      "L": "Here I am; testify against me before the LORD and before his anointed. Whose ox have I taken? Or whose donkey? Whom have I defrauded? Whom have I oppressed? Or from whose hand have I taken a bribe to blind my eyes? I will restore it to you.",
      "M": "Here I stand. Testify against me before the LORD and before his anointed. Have I taken anyone's ox or donkey? Have I defrauded or oppressed anyone? Have I taken a bribe to turn a blind eye? If so, I will make it right.",
      "T": "'I stand before you and before the LORD and his anointed. Make your case against me. Have I taken your ox, your donkey? Have I defrauded anyone? Crushed anyone? Taken money to pervert justice? Name it—and I will restore it.' It was the formal declaration of a judge who had finished his term of office."
    },
    "4": {
      "L": "And they said, You have not defrauded us or oppressed us, nor have you taken anything from anyone's hand.",
      "M": "They replied, 'You have not defrauded us, oppressed us, or taken anything from anyone.'",
      "T": "The people's verdict was unanimous: 'You have defrauded no one, oppressed no one, taken nothing from anyone.'"
    },
    "5": {
      "L": "He said to them, The LORD is witness against you, and his anointed is witness this day, that you have found nothing in my hand. And they said, He is witness.",
      "M": "He said to them, 'The LORD and his anointed are witnesses today that you have found nothing in my hands.' They answered, 'He is witness.'",
      "T": "Samuel pressed the point for the record: 'Then the LORD is your witness—and his anointed stands here too—that my hands are clean.' 'He is witness,' they affirmed."
    },
    "6": {
      "L": "And Samuel said to the people, It is the LORD who appointed Moses and Aaron, and who brought your fathers up out of the land of Egypt.",
      "M": "Samuel said to the people, 'It is the LORD who appointed Moses and Aaron and brought your ancestors up out of Egypt.'",
      "T": "Samuel then began his covenant history speech—the final argument of a faithful judge. 'The LORD himself raised up Moses and Aaron and led your ancestors out of Egypt.'"
    },
    "7": {
      "L": "Now therefore stand still, that I may plead with you before the LORD concerning all the righteous acts of the LORD that he performed for you and for your fathers.",
      "M": "Now take your stand, so I may lay before you before the LORD all the LORD's righteous deeds on your behalf and your ancestors' behalf.",
      "T": "'Stand still and hear me out. Before the LORD, I will rehearse for you his saving acts—everything the LORD has done for you and your fathers, his record of covenant faithfulness.'"
    },
    "8": {
      "L": "When Jacob came into Egypt, and your fathers cried to the LORD, the LORD sent Moses and Aaron, who brought your fathers out of Egypt and made them dwell in this place.",
      "M": "When Jacob went to Egypt and your ancestors cried out to the LORD, the LORD sent Moses and Aaron, who brought them out of Egypt and settled them in this land.",
      "T": "'When Jacob's family went down to Egypt and your ancestors groaned under slavery and cried to the LORD—he answered by sending Moses and Aaron. They brought your forebears out of Egypt and planted them in this land.'"
    },
    "9": {
      "L": "But when they forgot the LORD their God, he sold them into the hand of Sisera, commander of the army of Hazor, and into the hand of the Philistines, and into the hand of the king of Moab, and these fought against them.",
      "M": "But when they forgot the LORD their God, he handed them over to Sisera commander of Hazor's army, to the Philistines, and to the king of Moab, and these nations fought against them.",
      "T": "'But they forgot the LORD their God—and he handed them over to their enemies. Sisera and his iron chariots from Hazor. The Philistines. The king of Moab. Each time they abandoned God, they were given into oppressor hands.'"
    },
    "10": {
      "L": "And they cried to the LORD and said, We have sinned, because we have forsaken the LORD and have served the Baals and the Ashtaroth; but now deliver us from the hand of our enemies, and we will serve you.",
      "M": "They cried out to the LORD and confessed, 'We have sinned—we forsook the LORD and served the Baals and the Ashtaroth. Deliver us now from our enemies and we will serve you.'",
      "T": "'And each time they cried out in confession: \"We have sinned. We abandoned you and ran after Baal and Ashtaroth. Rescue us from our enemies, and we will be yours.\"'"
    },
    "11": {
      "L": "And the LORD sent Jerubbaal and Bedan and Jephthah and Samuel and delivered you from the hand of your enemies on every side, and you dwelt in safety.",
      "M": "The LORD sent Jerubbaal, Bedan, Jephthah, and Samuel, and rescued you from your enemies all around—and you lived in safety.",
      "T": "'And every time, the LORD answered—sending Jerubbaal, Bedan, Jephthah, and Samuel—judges who broke the power of every surrounding enemy. Under their leadership you lived in security.'"
    },
    "12": {
      "L": "But when you saw that Nahash the king of the Ammonites came against you, you said to me, No, but a king shall reign over us—when the LORD your God was your king.",
      "M": "But when you saw Nahash king of Ammon advancing against you, you said to me, 'No—we want a king to rule us!'—even though the LORD your God was your king.",
      "T": "'And then came Nahash the Ammonite—and instead of crying to your King, you came to me and said, \"Give us a human king.\" You said this even while the LORD your God was reigning over you as king.'"
    },
    "13": {
      "L": "And now, behold the king you have chosen and desired; and behold, the LORD has set a king over you.",
      "M": "Now here is the king you chose and asked for. The LORD has set a king over you.",
      "T": "'Here he is—the king you asked for, the king you wanted. The LORD has given you what you demanded. Now live with the choice.'"
    },
    "14": {
      "L": "If you will fear the LORD and serve him and listen to his voice and not rebel against the LORD's command, then both you and the king who reigns over you will continue following the LORD your God.",
      "M": "If you fear the LORD and serve him and obey his voice and do not rebel against his command, then both you and the king who rules you will follow the LORD your God—",
      "T": "'The institution is not the decisive thing. What matters is this: if you and your king truly fear the LORD—serve him, obey his voice, refuse to rebel against his word—then the kingdom will stand, and the LORD will be with you both.'"
    },
    "15": {
      "L": "But if you will not listen to the voice of the LORD, but rebel against the LORD's command, then the hand of the LORD will be against you, as it was against your fathers.",
      "M": "—but if you will not obey the LORD and instead rebel against his command, the hand of the LORD will be against you, as it was against your ancestors.",
      "T": "'—but if you disobey, if you rebel against his command, his hand will turn against you just as it did against your fathers before you.'"
    },
    "16": {
      "L": "Now therefore stand and see this great thing that the LORD will do before your eyes.",
      "M": "Now then, stand still and see the great thing the LORD is about to do before your eyes.",
      "T": "'Now stand here and watch. The LORD is about to demonstrate something in front of your eyes—a sign to seal everything I have said.'"
    },
    "17": {
      "L": "Is it not wheat harvest today? I will call to the LORD, and he will send thunder and rain, that you may see and know that your wickedness is great, which you have done before the LORD in asking a king for yourselves.",
      "M": "Isn't this the wheat harvest? I will call on the LORD, and he will send thunder and rain—so that you will understand how great your wickedness was before the LORD in asking for a king.",
      "T": "'It is wheat harvest—cloudless sky, no rain, no thunder. In a moment I will call on the LORD, and he will send thunder and rain. Then perhaps you will understand how seriously you sinned against him when you demanded a king.'"
    },
    "18": {
      "L": "So Samuel called to the LORD, and the LORD sent thunder and rain that day; and all the people greatly feared the LORD and Samuel.",
      "M": "Samuel called on the LORD, and the LORD sent thunder and rain that day. All the people stood in deep awe of the LORD and of Samuel.",
      "T": "Samuel prayed—and the sky broke open with thunder and rain in the middle of harvest. The people trembled with fear, dreading both the LORD and his prophet."
    },
    "19": {
      "L": "And all the people said to Samuel, Pray for your servants to the LORD your God, that we may not die; for we have added to all our sins this evil of asking a king for ourselves.",
      "M": "All the people said to Samuel, 'Pray to the LORD your God for us—your servants—so we won't die! We have added to all our sins this evil of asking for a king.'",
      "T": "The people collapsed before Samuel: 'Intercede for us—beg the LORD your God that we don't die! We have heaped guilt upon guilt. Asking for a king was sin on top of all our other sins.'"
    },
    "20": {
      "L": "And Samuel said to the people, Do not fear. You have done all this wickedness; yet do not turn aside from following the LORD, but serve the LORD with all your heart.",
      "M": "Samuel replied, 'Do not be afraid. You have committed all this wrong, but do not turn away from the LORD—serve him with your whole heart.'",
      "T": "Samuel's response was neither condemnation nor dismissal. 'Do not be afraid. Yes, you have sinned—deeply. But the answer is not to spiral further down. Turn back. Serve the LORD with your whole heart from this day forward.'"
    },
    "21": {
      "L": "And do not turn aside, for then you would go after empty things that cannot profit or deliver, for they are empty.",
      "M": "Do not turn away to pursue empty idols that cannot help or save—they are worthless.",
      "T": "'Don't be drawn off after emptiness—after gods that cannot act, cannot rescue, cannot save. They are nothing. They will leave you with nothing.'"
    },
    "22": {
      "L": "For the LORD will not forsake his people, for his great name's sake; for it has pleased the LORD to make you his people.",
      "M": "For the LORD will not abandon his people, because of his great name—it pleased him to make you his own.",
      "T": "'Here is your anchor: the LORD will not abandon his people. Not because of your merit—but because of his own great name, and because he himself chose you. He staked his reputation on Israel. That does not change.'"
    },
    "23": {
      "L": "Moreover, as for me, far be it from me that I should sin against the LORD by ceasing to pray for you; but I will instruct you in the good and the right way.",
      "M": "As for me, far be it from me to sin against the LORD by stopping my prayers for you. I will teach you the good and right way.",
      "T": "'And as for me—I will not stop praying for you. To do so would be sin against the LORD. And I will keep teaching you the good and straight path. That is my calling now.'"
    },
    "24": {
      "L": "Only fear the LORD and serve him in truth with all your heart; for consider what great things he has done for you.",
      "M": "Only fear the LORD and serve him faithfully with all your heart—consider the great things he has done for you.",
      "T": "'One thing is necessary: fear the LORD. Serve him faithfully, with undivided loyalty. And when you are tempted to forget—remember what great things he has done for you. Let the record of his saving acts be your anchor.'"
    },
    "25": {
      "L": "But if you do wickedly, both you and your king shall be consumed.",
      "M": "But if you persist in doing evil, both you and your king will be swept away.",
      "T": "'But hear this well: if you choose the path of evil—you and your king together will be swept away. The covenant has two edges. Choose life.'"
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1samuel')
        merge_tier(existing, SAMUEL, tier_key)
        save(tier_dir, '1samuel', existing)
    print('1 Samuel 7–12 written.')

if __name__ == '__main__':
    main()
