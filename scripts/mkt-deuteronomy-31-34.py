"""
MKT Deuteronomy chapters 31–34 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-deuteronomy-31-34.py

Covers: Moses's final charge to Joshua and all Israel (ch. 31); commission of Joshua at the
tent of meeting; the song commanded as a witness; writing and placement of the law beside the
ark; the Song of Moses (ch. 32, extended Hebrew poetry — the fullest theological statement in
Deuteronomy); the blessing of the twelve tribes (ch. 33, poetry); the death and burial of
Moses (ch. 34).

Translation decisions:
- H3068 (יהוה): "LORD" in L/M (small-caps convention); "the LORD" in T — matches all prior
  Deuteronomy scripts
- H430 (אֱלֹהִים): "God" in all tiers
- H6697 (צוּר, Rock): capitalized as a divine epithet throughout ch. 32 — "the Rock"; the
  contrast between Israel's Rock (the LORD) and the enemy's "rock" (lowercase) is theologically
  significant and preserved
- H3441 (יְשֻׁרוּן, Jeshurun): poetic name for Israel meaning "the Upright One"; retained as
  "Jeshurun" in L/M with brief gloss in T on first occurrence; appears in 32:15, 33:5, 33:26
- H7307 (רוּחַ) in 34:9: "spirit of wisdom" — lowercase, since it refers to a divinely
  granted quality conferred on Joshua, not a direct reference to the divine Spirit as such;
  consistent with the context (Moses laying on hands)
- H1285 (בְּרִית): "covenant" throughout
- H4191 (מוּת): "died/die" — straightforward; ch. 34:5 notes "according to the word/mouth
  of the LORD" — translated "according to the word of the LORD" (פִּי יהוה = lit. "mouth of
  the LORD"), which T glosses as "in obedience to the LORD's own word"
- H5771 (עָוֺן) / H4784 (מָרָה): "rebellion/rebellious" — matching prior scripts; 31:27
  carries both the stiff-neck and rebellion vocabulary; T surfaces the moral weight
- Ch. 32 (Song of Moses): highly structured Hebrew poetry with 52 verses. L preserves
  parallelism and source word order. M renders as natural English prose. T uses \n line breaks
  to honour the bicolon structure, gives interpretive cadence, and surfaces the theological arc:
  theophany → Israel's privilege → Israel's apostasy → God's judgment → God's vindication.
- Ch. 33 (Blessing of Moses): tribal blessings in poetry. T uses \n line breaks for the
  poetic structure of each blessing. L/M preserve the blessing formula per tribe.
- Ch. 34 (Death of Moses): prose narrative. T carries the theological weight of the ending:
  Moses is irreplaceable, but the story continues; no marked grave means no shrine cult.
- H5012 (נָבִיא): "prophet" in 34:10 — the closing verdict of the Torah on Moses is that
  no prophet has since arisen like him; T unpacks what "face to face" meant vs. normal
  prophetic vision
- OT echo: 31:6 parallels Josh 1:9; T notes the continuity without anachronism. 31:23
  parallels God's direct commissioning of Joshua (distinct from Moses's commissioning in 31:7).
- 32:35 ("vengeance is mine"): Paul cites this in Rom 12:19; T notes the NT trajectory
  without anachronism, phrasing it as the theological claim that divine retribution is
  not Israel's to dispense privately.
- 32:43: the LXX and DSS preserve additional lines ("bow down to him, all gods") not in MT;
  L/M follow MT; T notes the fuller witness of the tradition.
- Poetic refrains in ch. 32 ("purge the evil," etc.) do not appear here; the refrain of
  ch. 32 is the LORD's own name / the Rock epithet — preserved verbatim.
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

DEUTERONOMY = {
  "31": {
    "1": {
      "L": "And Moses went and spoke these words to all Israel.",
      "M": "Moses went and spoke these words to all Israel.",
      "T": "Moses turned to the whole assembly of Israel and delivered his final words."
    },
    "2": {
      "L": "And he said to them, 'I am a hundred and twenty years old today. I can no longer go out or come in. The LORD has said to me, \"You shall not cross this Jordan.\"'",
      "M": "He said to them, 'I am a hundred and twenty years old today. I am no longer able to lead you out and bring you in. The LORD has told me I will not cross the Jordan.'",
      "T": "'I am one hundred and twenty years old,' Moses said to them. 'My time for leading is over — the LORD himself has told me I will not cross the Jordan. My journey ends here.'"
    },
    "3": {
      "L": "The LORD your God himself goes over before you. He will destroy these nations before you, and you shall dispossess them. Joshua goes over before you, as the LORD has spoken.",
      "M": "The LORD your God himself will cross over before you. He will destroy these nations before you so that you can take their land. Joshua will lead you across, as the LORD has said.",
      "T": "The LORD your God goes before you — he will clear the nations from the land so you can possess it. Joshua will lead you across, as the LORD has promised. You will not be left without a leader, and you will not be left without God."
    },
    "4": {
      "L": "And the LORD will do to them as he did to Sihon and Og, the kings of the Amorites, and to their land, whom he destroyed.",
      "M": "The LORD will deal with them just as he dealt with Sihon and Og, the Amorite kings, and their land, which he destroyed.",
      "T": "What the LORD did to Sihon and Og — those powerful Amorite kings — he will do again. The pattern is established: he goes before his people and eliminates the opposition."
    },
    "5": {
      "L": "And the LORD will give them up before you, and you shall do to them according to all the commandment which I have commanded you.",
      "M": "The LORD will hand them over to you, and you must deal with them according to all the commands I have given you.",
      "T": "The LORD will hand them over — and you must treat them exactly as I have commanded. The victories will be his; the obedience must be yours."
    },
    "6": {
      "L": "Be strong and courageous. Do not fear or be in dread of them, for the LORD your God is he who goes with you. He will not leave you or forsake you.",
      "M": "Be strong and courageous. Do not be afraid or terrified by them — the LORD your God goes with you. He will never leave you or abandon you.",
      "T": "Be strong — be courageous. There is no room for fear, because the LORD your God is the one going with you into every battle. He will not let you go; he will not walk away. You are not alone."
    },
    "7": {
      "L": "And Moses called Joshua and said to him in the sight of all Israel, 'Be strong and courageous, for you shall go with this people into the land that the LORD has sworn to their fathers to give them, and you shall put them in possession of it.'",
      "M": "Moses summoned Joshua and said to him before all Israel, 'Be strong and courageous, for you are the one who will lead this people into the land the LORD swore to give their ancestors — you will be the one who takes them in to possess it.'",
      "T": "Moses called Joshua before the whole assembly. 'Be strong and courageous,' he said. 'You are the one who will carry this people across and into the land the LORD swore to give their fathers. This call is yours now.'"
    },
    "8": {
      "L": "And the LORD is he who goes before you. He will be with you; he will not leave you or forsake you. Do not fear and do not be dismayed.",
      "M": "The LORD himself goes before you. He will be with you; he will never leave you or abandon you. Do not be afraid or discouraged.",
      "T": "The LORD himself walks ahead of you. He will be at your side — he will never desert you, never abandon you. So do not be afraid. Do not be undone by what lies ahead."
    },
    "9": {
      "L": "And Moses wrote this law and gave it to the priests, the sons of Levi, who carried the ark of the covenant of the LORD, and to all the elders of Israel.",
      "M": "Moses wrote down this law and handed it over to the Levitical priests who carried the ark of the covenant of the LORD, and to all the elders of Israel.",
      "T": "Moses committed the law to writing and placed it in the hands of those responsible for its custody — the Levitical priests who bore the ark of the covenant, and the elders of Israel. The word would not be left to memory alone."
    },
    "10": {
      "L": "And Moses commanded them, 'At the end of every seven years, at the appointed time in the year of release, at the Feast of Booths,'",
      "M": "Moses commanded them: 'At the end of every seven years, during the Festival of Booths in the year of debt cancellation,'",
      "T": "'Every seven years,' Moses commanded, 'when the year of release comes and the Festival of Booths arrives —'"
    },
    "11": {
      "L": "'when all Israel comes to appear before the LORD your God at the place which he shall choose, you shall read this law before all Israel in their hearing.'",
      "M": "'when all Israel comes to appear before the LORD your God at the place he chooses, you must read this law aloud before all Israel in their hearing.'",
      "T": "'— when all Israel gathers before the LORD at his chosen place, this law must be read aloud to the entire assembly. Everyone hears it; no one is exempt from knowing what the covenant demands.'"
    },
    "12": {
      "L": "'Assemble the people — men, women, and children, and the sojourner who is within your towns — that they may hear and learn to fear the LORD your God and be careful to do all the words of this law,'",
      "M": "'Gather the entire people — men, women, children, and the foreigners living in your towns — so they can hear, learn to fear the LORD your God, and carefully follow all the words of this law.'",
      "T": "'Bring everyone: men, women, children, the immigrant in your midst. No one stays home. Every person must hear, every person must learn what it means to fear the LORD and to keep his covenant. The law belongs to the whole community.'"
    },
    "13": {
      "L": "'and that their children who have not known it may hear and learn to fear the LORD your God as long as you live in the land that you are going over the Jordan to possess.'",
      "M": "'The children who do not yet know the law must hear it and learn to fear the LORD your God throughout all the time you live in the land you are about to cross the Jordan to possess.'",
      "T": "'And this is for the children especially — those too young to have known the covenant. Each generation must hear and learn. The fear of the LORD does not pass by inheritance; it must be taught, heard, and received afresh by every generation that enters the land.'"
    },
    "14": {
      "L": "And the LORD said to Moses, 'Behold, the days approach when you must die. Call Joshua and present yourselves in the tent of meeting, that I may commission him.' And Moses and Joshua went and presented themselves in the tent of meeting.",
      "M": "The LORD said to Moses, 'The time of your death is drawing near. Call Joshua and come to the tent of meeting so I can commission him.' Moses and Joshua went and stood at the tent of meeting.",
      "T": "Then the LORD spoke to Moses directly: 'Your death is near. Bring Joshua — come to the tent of meeting, and I will formally commission him.' Moses and Joshua obeyed and stood together at the entrance of the tent."
    },
    "15": {
      "L": "And the LORD appeared in the tent in a pillar of cloud. And the pillar of cloud stood over the entrance of the tent.",
      "M": "The LORD appeared at the tent in a pillar of cloud, which stood at the entrance of the tent.",
      "T": "The LORD came — the pillar of cloud descended and stood at the entrance of the tent. There was no mistaking the presence: God himself was commissioning Joshua."
    },
    "16": {
      "L": "And the LORD said to Moses, 'Behold, you are about to lie down with your fathers. Then this people will rise and go after the foreign gods of the land among whom they go to be among them, and will forsake me and break my covenant that I have made with them.'",
      "M": "The LORD said to Moses, 'You are about to die and join your ancestors. After that, this people will rise up and chase after the foreign gods of the land they are entering; they will abandon me and break the covenant I made with them.'",
      "T": "'You are about to die,' the LORD told Moses — no softening, no comfort withheld. 'And after you are gone, this people will turn. They will chase the gods of Canaan, they will abandon me, they will shatter the covenant. I see it already.'"
    },
    "17": {
      "L": "'Then my anger will be kindled against them in that day, and I will forsake them and hide my face from them, and they will be devoured. And many evils and troubles will come upon them, so that they will say in that day, \"Have not these evils come upon us because our God is not among us?\"'",
      "M": "'My anger will blaze against them that day, and I will abandon them and hide my face from them, and they will be consumed. Many disasters and troubles will overwhelm them, and they will ask, \"Have all these evils come upon us because our God is no longer with us?\"'",
      "T": "'My anger will ignite against them — I will withdraw, hide my face, and let them be consumed by what they chose. Disaster after disaster will fall on them. And they will ask the right question too late: \"Has God abandoned us?\" — not understanding that they abandoned him first.'"
    },
    "18": {
      "L": "'And I will surely hide my face in that day on account of all the evil they have done, for they have turned to other gods.'",
      "M": "'I will certainly conceal my face that day because of all the evil they have done — they have turned to other gods.'",
      "T": "'I will turn my face away — not arbitrarily, but in direct response to what they chose. They turned their faces to other gods; I will turn mine. The hiding of my face is the consequence of their faithlessness, not its cause.'"
    },
    "19": {
      "L": "'Now therefore write this song and teach it to the people of Israel. Put it in their mouths, that this song may be a witness for me against the people of Israel.'",
      "M": "'Now write down this song and teach it to the Israelites. Put it in their mouths, so that this song will serve as a witness for me against them.'",
      "T": "'Write this song. Teach it to Israel; make it part of them, put it on their lips. It will remain in their mouths long after they have broken faith — and when the catastrophe comes, the song itself will testify: they knew what was coming, and they chose it anyway.'"
    },
    "20": {
      "L": "'For when I have brought them into the land flowing with milk and honey which I swore to their fathers, and they have eaten their fill and grown fat, they will turn to other gods and serve them and despise me and break my covenant.'",
      "M": "'When I bring them into the land of milk and honey I swore to give their ancestors, and they eat until they are full and become prosperous, they will turn to other gods and serve them, and they will reject me and break my covenant.'",
      "T": "'Prosperity is the danger. When the land yields its abundance — milk, honey, grain, oil — they will eat until they are satisfied, grow fat and comfortable, and then turn away from the God who gave it all to them. Fullness breeds forgetfulness. This is Israel's recurring temptation.'"
    },
    "21": {
      "L": "'And when many evils and troubles have come upon them, this song shall confront them as a witness, for it will not be forgotten from the mouths of their offspring. For I know their inclination which they carry out today, before I have brought them into the land that I swore to give.'",
      "M": "'When disasters and troubles overwhelm them, this song will testify against them — it will not disappear from the mouths of their descendants. I know what they are already planning to do, even now, before they have entered the land I promised.'",
      "T": "'When the disasters come — and they will — this song will still be on their lips, passed from parents to children to grandchildren. It will be the witness that proves they were warned. And I know already what they will do. Even as we stand here, their hearts are bent toward unfaithfulness. The song will not let them pretend otherwise.'"
    },
    "22": {
      "L": "And Moses wrote this song the same day and taught it to the people of Israel.",
      "M": "Moses wrote down this song that very day and taught it to the Israelites.",
      "T": "That same day, Moses wrote the song and taught it to all Israel. The word was given; now it was entrusted to the people."
    },
    "23": {
      "L": "And the LORD commissioned Joshua the son of Nun and said, 'Be strong and courageous, for you shall bring the people of Israel into the land that I swore to give them. I will be with you.'",
      "M": "The LORD then commissioned Joshua son of Nun, saying, 'Be strong and courageous, for you will bring the Israelites into the land I swore to give them. I will be with you.'",
      "T": "Then the LORD himself spoke directly to Joshua: 'Be strong — be courageous. You are the one who will bring Israel into the land I promised them under oath. And I will be with you.' The commission came not from Moses alone; it came from God."
    },
    "24": {
      "L": "And when Moses had finished writing the words of this law in a book to the very end,",
      "M": "When Moses had finished writing out the entire law in a book,",
      "T": "When Moses had written every word of this law to its final line —"
    },
    "25": {
      "L": "Moses commanded the Levites who carried the ark of the covenant of the LORD,",
      "M": "Moses gave a command to the Levites who carried the ark of the covenant of the LORD:",
      "T": "— he turned to the Levites who bore the ark of the covenant and gave them one final charge:"
    },
    "26": {
      "L": "'Take this book of the law and put it beside the ark of the covenant of the LORD your God, that it may be there for a witness against you.'",
      "M": "'Take this scroll of the law and place it beside the ark of the covenant of the LORD your God. It will remain there as a witness against you.'",
      "T": "'Place this book — the entire written law — alongside the ark of the covenant. Not inside it, but beside it. It will be there as a standing witness, testifying to what Israel was taught and what Israel agreed to. It outlasts every generation.'"
    },
    "27": {
      "L": "'For I know your rebellion and your stiff neck. Behold, even today while I am still alive among you, you have been rebellious against the LORD. How much more after my death!'",
      "M": "'I know how rebellious and stubborn you are. Even today, while I am still with you, you have been defiant toward the LORD. How much worse will it be after I am gone?'",
      "T": "'I know you. I have led you for forty years and I know what you are capable of. Even now — while I still stand here breathing — you resist the LORD. What will happen after I am buried? I shudder to think of it.'"
    },
    "28": {
      "L": "'Assemble before me all the elders of your tribes and your officers, that I may speak these words in their ears and call heaven and earth to witness against them.'",
      "M": "'Gather all the elders of your tribes and your officials so I can speak these words in their hearing and call heaven and earth to testify against them.'",
      "T": "'Bring me every elder, every officer — I will speak the truth to them directly, and I will call heaven and earth as my witnesses. What I am about to say will be on record before the cosmos.'"
    },
    "29": {
      "L": "'For I know that after my death you will surely act corruptly and turn aside from the way that I have commanded you. And evil will befall you in the latter days, because you will do what is evil in the sight of the LORD, provoking him to anger through the work of your hands.'",
      "M": "'I know that after my death you will become deeply corrupt and turn away from everything I have commanded. Disaster will come upon you in the days ahead, because you will do what is evil in the LORD's sight, provoking him to anger through what your hands make.'",
      "T": "'After I am gone, you will corrupt yourselves. You will leave the path I laid out. And the disasters that come on you in the latter days will not be arbitrary — they will be the direct consequence of what you chose to do with your hands: the idols you shaped, the gods you served. You will provoke the LORD to anger, and you will live with the result.'"
    },
    "30": {
      "L": "And Moses spoke in the ears of all the assembly of Israel the words of this song until they were finished:",
      "M": "Moses then recited the words of this song in the hearing of the entire assembly of Israel, from beginning to end:",
      "T": "And Moses stood before the whole assembly of Israel and spoke every word of this song — the full witness — to the very end:"
    }
  },
  "32": {
    "1": {
      "L": "Give ear, O heavens, and I will speak; and let the earth hear the words of my mouth.",
      "M": "Listen, O heavens, and I will speak; let the earth hear what I say.",
      "T": "Give ear, O heavens — I will speak;\nlet the earth hear the words of my mouth."
    },
    "2": {
      "L": "May my teaching drop as the rain, my speech distill as the dew, as gentle rain upon the tender grass, and as showers upon the herb.",
      "M": "Let my teaching fall like rain and my speech settle like dew, like gentle showers on new grass, like rainfall on tender plants.",
      "T": "May my teaching fall like rain,\nmy words descend like dew —\nlike soft showers on fresh grass,\nlike rainfall on young green things."
    },
    "3": {
      "L": "For I will proclaim the name of the LORD; ascribe greatness to our God!",
      "M": "I will proclaim the name of the LORD; give glory to our God!",
      "T": "For I proclaim the name of the LORD —\nascribe greatness to our God!"
    },
    "4": {
      "L": "The Rock — his work is perfect, for all his ways are justice. A God of faithfulness and without iniquity, just and upright is he.",
      "M": "The Rock — his work is flawless, and all his ways are just. A faithful God, without fault — he is righteous and upright.",
      "T": "The Rock —\nhis work is perfect, flawless;\nall his ways are justice.\nA God of faithfulness, never unjust —\nhe is righteous and straight."
    },
    "5": {
      "L": "They have acted corruptly toward him; their blemish makes them not his children — a perverse and crooked generation.",
      "M": "They have corrupted themselves — they are not his children because of their blemish; they are a perverse and crooked generation.",
      "T": "They corrupted themselves against him —\nnot his children, these, their moral stain disqualifies them;\na generation twisted and bent."
    },
    "6": {
      "L": "Do you thus repay the LORD, O foolish and unwise people? Is he not your father who created you — who made you and established you?",
      "M": "Is this how you repay the LORD, O foolish and senseless people? Is he not your father who made you — who formed you and gave you your place?",
      "T": "Is this your return on all he gave you —\nyou foolish, witless people?\nIs he not your father who made you,\nwho established you and set you in the world?"
    },
    "7": {
      "L": "Remember the days of old; consider the years of many generations; ask your father and he will show you, your elders and they will tell you.",
      "M": "Remember the ancient days; think back across many generations. Ask your father — he will tell you; ask the elders — they will explain.",
      "T": "Look back across time —\nthink through the long years, generation by generation.\nAsk your father; he will tell you;\nconsult the elders; they will explain."
    },
    "8": {
      "L": "When the Most High gave to the nations their inheritance, when he divided the children of Adam, he set the bounds of the peoples according to the number of the sons of Israel.",
      "M": "When the Most High apportioned the nations their inheritance and divided the human race, he fixed the boundaries of every people according to the number of Israel's sons.",
      "T": "When the Most High parceled out the nations —\ndividing all of humanity —\nhe fixed the boundaries of every people\naccording to the number of Israel's sons."
    },
    "9": {
      "L": "For the LORD's portion is his people; Jacob is the lot of his inheritance.",
      "M": "But the LORD's own portion is his people; Jacob is what he has claimed as his inheritance.",
      "T": "But the LORD's own allotment is his people —\nJacob is the portion he keeps for himself."
    },
    "10": {
      "L": "He found him in a desert land, in the howling wilderness waste. He encircled him, he cared for him, he kept him as the apple of his eye.",
      "M": "He found his people in a barren wasteland, in the howling desert. He surrounded them, looked after them, guarded them like the apple of his eye.",
      "T": "He found him in a desert —\nin the howling emptiness of a barren waste —\nhe surrounded him, tended him,\nguarded him as the very pupil of his eye."
    },
    "11": {
      "L": "Like an eagle that stirs up its nest, that hovers over its young, that spreads out its wings, catches them, and bears them on its pinions —",
      "M": "Like an eagle that rouses its young from the nest, hovers over them, spreads its wings to catch them, and carries them on its feathers —",
      "T": "Like an eagle rousing its nestlings,\nhovering over its young —\nwings spread wide to catch them,\nlifting them and bearing them up —"
    },
    "12": {
      "L": "the LORD alone led him, and there was no foreign god with him.",
      "M": "the LORD alone was his guide — no foreign god was with him.",
      "T": "the LORD alone was his guide.\nNo alien god walked with him."
    },
    "13": {
      "L": "He made him ride on the high places of the land and he ate the produce of the field. He suckled him with honey from the rock and oil from the flinty rock,",
      "M": "He set him on the heights of the land and fed him with the produce of the fields. He gave him honey from the rock and oil from the hardest stone,",
      "T": "He set him on the high places of the land,\nfed him the yield of the fields —\nhoney drawn from solid rock,\noil pressed from flint itself —"
    },
    "14": {
      "L": "curds from the herd and milk from the flock, with the fat of lambs, rams of Bashan and goats, with the finest of the wheat — and you drank the blood of the grape as foaming wine.",
      "M": "along with curds from cattle and milk from the flock, the fat of choice lambs and Bashan rams and goats, the finest wheat — and you drank rich red wine from the grape.",
      "T": "curds and milk from herd and flock,\nfat of the choicest lambs and bulls of Bashan,\nthe finest wheat —\nand you drank rich wine, red as blood from the grape."
    },
    "15": {
      "L": "But Jeshurun grew fat and kicked. You grew fat, you grew thick, you became covered with fat. Then he forsook God who made him and scoffed at the Rock of his salvation.",
      "M": "But Jeshurun became fat and rebellious — you grew fat, sleek, and bloated. Then Israel abandoned the God who made them and mocked the Rock of their salvation.",
      "T": "But Jeshurun — Israel, the so-called Upright One —\ngrew fat and kicked against its God.\nYou grew heavy and smooth and self-satisfied;\nthen you abandoned the God who made you\nand mocked the Rock who had rescued you."
    },
    "16": {
      "L": "They provoked him to jealousy with strange gods; with abominations they provoked him to anger.",
      "M": "They made him jealous with foreign gods; with detestable practices they provoked his anger.",
      "T": "They stirred his jealousy with alien gods;\nwith their abominations they lit the fuse of his wrath."
    },
    "17": {
      "L": "They sacrificed to demons, not to God — to gods they had not known, to new gods that came up recently, whom your fathers had not feared.",
      "M": "They offered sacrifices to demons — not to God — to gods they had never known, to newly arrived gods your ancestors did not fear.",
      "T": "They sacrificed to demons — not to God —\nto gods no one had ever known,\nupstarts newly arrived from nowhere,\nwhom your fathers never dreamed of fearing."
    },
    "18": {
      "L": "You were unmindful of the Rock who bore you, and you forgot the God who gave you birth.",
      "M": "You neglected the Rock who fathered you; you forgot the God who gave you life.",
      "T": "You forgot the Rock who bore you;\nyou pushed from memory the God who gave you birth."
    },
    "19": {
      "L": "The LORD saw and spurned them, because of the provocation of his sons and daughters.",
      "M": "When the LORD saw this he was filled with contempt for them, provoked by his sons and daughters.",
      "T": "The LORD saw it —\nand the sight of his own sons and daughters provoking him filled him with revulsion."
    },
    "20": {
      "L": "And he said, 'I will hide my face from them; I will see what their end will be — for they are a perverse generation, children in whom there is no faithfulness.'",
      "M": "He said, 'I will hide my face from them and wait to see what becomes of them — they are a crooked generation, children with no loyalty at all.'",
      "T": "'I will turn my face away,' he said,\n'and watch to see where this leads.\nA perverse generation, these —\nchildren in whom there is not a shred of faithfulness.'"
    },
    "21": {
      "L": "They have made me jealous with what is not God; they have provoked me with their vanities. So I will make them jealous with those who are not a people; I will provoke them to anger with a foolish nation.",
      "M": "They provoked my jealousy with something that is not God; they angered me with worthless idols. So I will provoke their jealousy with a nation that is not a people; I will make them angry with a foolish nation.",
      "T": "They made me jealous with a non-god;\nthey provoked me with their hollow idols.\nSo I will make them jealous with a non-people —\nI will provoke them with a nation they would never dignify."
    },
    "22": {
      "L": "For a fire is kindled by my anger and it burns to the depths of Sheol, and devours the earth with its increase, and sets on fire the foundations of the mountains.",
      "M": "A fire is ignited by my anger that burns down to the depths of the realm of the dead, consuming the earth and its harvest, and setting the roots of the mountains ablaze.",
      "T": "For a fire has been lit by my anger —\nit burns all the way down to Sheol's lowest depths,\nit devours the earth and everything it yields,\nit sets the roots of the mountains alight."
    },
    "23": {
      "L": "I will heap evils upon them; I will spend my arrows on them.",
      "M": "I will pile disaster upon them and exhaust my arrows against them.",
      "T": "I will heap calamity upon calamity;\nI will empty my quiver against them."
    },
    "24": {
      "L": "Wasted by hunger, devoured by plague and poisonous pestilence; the teeth of beasts I will send against them, with the venom of things that crawl in the dust.",
      "M": "Ravaged by famine, consumed by burning fever and bitter pestilence — I will set wild beasts on them along with crawling things that bite with poison from the dust.",
      "T": "Starved to wasting, burned by disease,\nbitten by bitter plague —\nI will loose wild animals with tearing teeth\nand the venom of creatures that crawl in the dust."
    },
    "25": {
      "L": "Outside the sword shall bereave, and inside terror — for the young man and the young woman alike, the nursing infant with the gray-haired elder.",
      "M": "The sword will cut them down outside; inside the city, terror — for young and old alike, the nursing infant and the elderly.",
      "T": "Outside: the sword cuts down youth and maiden alike.\nInside: terror for every soul —\nthe infant at the breast,\nthe man whose hair has gone white."
    },
    "26": {
      "L": "I said, 'I will cut them to pieces; I will wipe out the memory of them from among men,'",
      "M": "I said to myself, 'I will scatter them to the four winds; I will erase their memory from the face of the earth —'",
      "T": "'I had it in my mind to scatter them to the corners of the earth,\nto erase their very memory from among the nations —'"
    },
    "27": {
      "L": "had I not feared the taunting of the enemy, lest their adversaries misconstrue, lest they say, 'Our hand is high, and the LORD has not done all this.'",
      "M": "had I not feared the taunting of the enemy — that their foes would misread it and claim, 'Our own power did this; the LORD had no part in it.'",
      "T": "'— but I held back, because I feared the enemy's boast:\nif I destroyed Israel, her enemies would misread the meaning.\nThey would say, \"We did this ourselves —\nthe LORD had nothing to do with it.\"\nI would not give them that.'"
    },
    "28": {
      "L": "For they are a nation void of counsel, and there is no understanding in them.",
      "M": "This enemy nation is without sense; there is no understanding in them.",
      "T": "They are a nation with no wisdom —\nno insight lives in them."
    },
    "29": {
      "L": "If only they were wise, they would understand this; they would discern what their end will be!",
      "M": "If they had any wisdom, they would grasp this; they would understand what lies ahead.",
      "T": "If only they were wise —\nif they could see past the moment —\nthey would grasp what their end will be."
    },
    "30": {
      "L": "How should one have chased a thousand, and two have put ten thousand to flight, unless their Rock had sold them, and the LORD had given them up?",
      "M": "How else could one man rout a thousand, or two men put ten thousand to flight, unless their Rock had surrendered them and the LORD had handed them over?",
      "T": "How could one man chase a thousand,\nand two put ten thousand to flight —\nunless their Rock had let them go,\nunless the LORD himself had handed them over?"
    },
    "31": {
      "L": "For their rock is not as our Rock — our enemies are judges in this.",
      "M": "Their rock is nothing like our Rock — even our enemies can see that.",
      "T": "Their god is not like our God —\neven the enemy concedes it, in the end."
    },
    "32": {
      "L": "For their vine comes from the vine of Sodom and from the fields of Gomorrah. Their grapes are grapes of poison; their clusters are bitter.",
      "M": "Their vine springs from the vine of Sodom, from the fields of Gomorrah — their grapes are poisonous, their clusters filled with bitterness.",
      "T": "Their vine is rooted in Sodom,\nnourished by the fields of Gomorrah —\ntheir grapes are grapes of poison;\nevery cluster is bitter to the core."
    },
    "33": {
      "L": "Their wine is the venom of serpents and the cruel poison of asps.",
      "M": "Their wine is snake venom — the deadly poison of cobras.",
      "T": "Their wine is serpent's venom —\nthe fatal poison of the asp."
    },
    "34": {
      "L": "Is not this laid up in store with me, sealed up in my treasuries?",
      "M": "Is not this stored up by me — sealed in my storehouses?",
      "T": "Is not all of this stored up with me,\nsealed away in my treasury?"
    },
    "35": {
      "L": "Vengeance is mine, and recompense, for the time their foot shall slip; for the day of their calamity is at hand, and what is coming upon them makes haste.",
      "M": "Vengeance belongs to me — I will repay. In due time their foot will slip; their day of disaster is coming, and doom approaches fast.",
      "T": "Vengeance is mine — I will repay;\ntheir foot will slip at the moment I choose.\nThe day of their calamity is near,\nand what is coming rushes toward them.\n(Paul will cite this verse in Romans 12 as the ground for refusing private revenge: divine retribution is God's to dispense, not Israel's — and not ours.)"
    },
    "36": {
      "L": "For the LORD will vindicate his people and have compassion on his servants, when he sees that their power is gone and there is none remaining, bond or free.",
      "M": "The LORD will vindicate his people and have compassion on his servants when he sees their strength is spent and none remain, whether slave or free.",
      "T": "For the LORD will judge on behalf of his people;\nhe will have compassion on his servants\nwhen he sees that their strength has given out,\nthat nothing remains — slave or free."
    },
    "37": {
      "L": "And he will say, 'Where are their gods, the rock in which they took refuge,'",
      "M": "Then he will say, 'Where are their gods — the rock they depended on for safety?'",
      "T": "'Where are their gods now?' he will say —\n'the rock they ran to for refuge?'"
    },
    "38": {
      "L": "'who ate the fat of their sacrifices and drank the wine of their drink offerings? Let them rise up and help you; let them be your protection!'",
      "M": "'The gods who ate the fat of their sacrifices and drank the wine of their offerings — let them rise up now and rescue you! Let them be your shield!'",
      "T": "'The gods that feasted on your fat offerings\nand drank your libations —\nlet them stand up now and save you.\nLet them be your shelter.'"
    },
    "39": {
      "L": "'See now that I, even I, am he, and there is no god beside me. I kill and I make alive; I wound and I heal; and there is none who can deliver from my hand.'",
      "M": "'See now that I alone am God — there is no other god beside me. I put to death and I bring to life; I wound and I heal; no one can escape my hand.'",
      "T": "'Look at this and understand:\nI am he — the only one.\nNo god exists beside me.\nI kill, and I give life;\nI wound, and I heal.\nNo one escapes my hand.'"
    },
    "40": {
      "L": "For I lift my hand to heaven and swear: 'As I live forever,'",
      "M": "For I raise my hand toward heaven and declare: 'I live forever —'",
      "T": "I raise my hand to heaven and take this oath:\n'As surely as I live forever —'"
    },
    "41": {
      "L": "'if I sharpen my glittering sword and my hand takes hold of judgment, I will take vengeance on my adversaries and repay those who hate me.'",
      "M": "'I will sharpen my flashing sword; my hand will grip the instrument of judgment; I will repay my enemies and punish those who hate me.'",
      "T": "'I will sharpen my flashing sword;\nmy hand will seize the instrument of judgment;\nI will repay my enemies in full\nand reward those who hate me.'"
    },
    "42": {
      "L": "'I will make my arrows drunk with blood, while my sword shall devour flesh — with the blood of the slain and the captives, from the heads of the long-haired enemy.'",
      "M": "'My arrows will be drunk with blood as my sword devours flesh — the blood of the slain and the captives, from the heads of the enemy's warriors.'",
      "T": "'My arrows will be drunk with blood;\nmy sword will eat its fill of flesh —\nthe blood of the dead, the blood of the captured,\nfrom the heads of the enemy's princes.'"
    },
    "43": {
      "L": "Rejoice with him, O heavens; bow down to him, all gods. For he avenges the blood of his children and takes vengeance on his adversaries; he repays those who hate him and makes atonement for his land, for his people.",
      "M": "Rejoice, O heavens, with his people, and bow before him, all divine beings. For he avenges the blood of his servants; he takes vengeance on his adversaries and makes atonement for his land and his people.",
      "T": "Rejoice, O heavens, with his people!\nBow down to him, all the divine council!\nFor he avenges his servants' blood;\nhe takes vengeance on his enemies\nand cleanses the land of his people.\n(The LXX and Dead Sea Scrolls preserve fuller lines here — \"bow down to him, all gods\" — not in the MT; the additional witness strengthens the cosmic scope of this climax.)"
    },
    "44": {
      "L": "And Moses came and spoke all the words of this song in the ears of the people, he and Hoshea the son of Nun.",
      "M": "Moses came and recited all the words of this song to the people, together with Hoshea son of Nun.",
      "T": "Moses and Hoshea son of Nun stood before the people and spoke every word of the song in their hearing."
    },
    "45": {
      "L": "And when Moses had finished speaking all these words to all Israel,",
      "M": "When Moses finished reciting all these words to all Israel,",
      "T": "When Moses had finished speaking every word to all Israel —"
    },
    "46": {
      "L": "he said to them, 'Set your heart to all the words that I am warning you with today, that you may command your children to be careful to do all the words of this law.'",
      "M": "he said to them, 'Take these warnings to heart — all the words I am charging you with today — and pass them on to your children so that they carefully obey every word of this law.'",
      "T": "he said: 'Take these words to heart — every warning I have spoken today. Teach them to your children; make sure they know what fidelity to the covenant looks like. This is not a burden handed off to the next generation; it is life, handed on.'"
    },
    "47": {
      "L": "'For it is not an empty word for you, but it is your life, and by this word you shall live long in the land that you go over the Jordan to possess.'",
      "M": "'This is not a trivial thing — it is your very life. And by keeping it, you will live for many years in the land you are crossing the Jordan to take.'",
      "T": "'This is not an abstraction. This is your life. The length of your days in the land depends on it. Hold onto the law and it holds you in the land.'"
    },
    "48": {
      "L": "And the LORD spoke to Moses that very day,",
      "M": "That same day the LORD said to Moses,",
      "T": "That same day the LORD spoke to Moses:"
    },
    "49": {
      "L": "'Go up to this mountain of the Abarim, Mount Nebo, which is in the land of Moab opposite Jericho, and see the land of Canaan, which I am giving to the people of Israel for a possession.'",
      "M": "'Climb to the top of the Abarim range, to Mount Nebo in Moab, across from Jericho, and look out over the land of Canaan that I am giving to the Israelites as their possession.'",
      "T": "'Climb to Mount Nebo — the peak of the Abarim range — in the land of Moab across from Jericho. Look out over the land of Canaan that I am giving to Israel. You will see it. Then you will die.'"
    },
    "50": {
      "L": "'And die on the mountain that you go up to, and be gathered to your people, as Aaron your brother died on Mount Hor and was gathered to his people.'",
      "M": "'There on the mountain you climb, you will die and be joined to your ancestors, just as your brother Aaron died on Mount Hor and was joined to his.'",
      "T": "'Die on that mountain. Be gathered to your people — as Aaron your brother died on Mount Hor and was gathered to his. The same end awaits every servant of God, however great.'"
    },
    "51": {
      "L": "'because you broke faith with me in the midst of the people of Israel at the waters of Meribah-kadesh in the wilderness of Zin, and because you did not uphold my holiness in the midst of the people of Israel.'",
      "M": "'Because you were unfaithful to me in the presence of Israel at the waters of Meribah-kadesh in the wilderness of Zin, and failed to uphold my holiness before the people of Israel.'",
      "T": "'Because at the waters of Meribah-kadesh, in the wilderness of Zin, you broke faith with me before the eyes of Israel — you did not honor me as holy before the people. That moment has its consequence.'"
    },
    "52": {
      "L": "'For you shall see the land before you, but you shall not go there, into the land that I am giving to the people of Israel.'",
      "M": "'You will see the land ahead of you, but you will not enter it — the land I am giving to Israel.'",
      "T": "'You will see it — the whole land spread before you. But you will not cross over. This is your boundary, Moses. The land belongs to the generation that follows you.'"
    }
  },
  "33": {
    "1": {
      "L": "And this is the blessing with which Moses the man of God blessed the children of Israel before his death.",
      "M": "This is the blessing with which Moses, the man of God, blessed the people of Israel before he died.",
      "T": "This is Moses's final act — not a law, not a warning, but a blessing. Before he died, the man of God spoke one last word over every tribe of Israel."
    },
    "2": {
      "L": "He said, 'The LORD came from Sinai and dawned from Seir upon us; he shone forth from Mount Paran; he came from the ten thousands of holy ones — from his right hand went a fiery law for them.'",
      "M": "He said, 'The LORD came from Sinai; he rose over us from Seir; he shone forth from Mount Paran; he arrived with ten thousands of holy ones — from his right hand blazing fire went out to them.'",
      "T": "The LORD came from Sinai;\nhe rose like the dawn from Seir;\nhe blazed forth from Mount Paran.\nHe came with ten thousands of his holy ones —\nfire streaming from his right hand."
    },
    "3": {
      "L": "Yes, he loved his people; all his holy ones were in his hand; they bowed down at your feet, each receiving your words.",
      "M": "He loves his people — all his holy ones are in his care. They bow at his feet and receive his instructions.",
      "T": "He loves his people deeply —\nall his holy ones rest in his hand.\nThey bow at his feet;\nthey receive his words."
    },
    "4": {
      "L": "Moses commanded us a law, as an inheritance for the assembly of Jacob.",
      "M": "Moses gave us the law — an inheritance for the assembly of Jacob.",
      "T": "Moses gave us the law —\nan inheritance for the whole assembly of Jacob."
    },
    "5": {
      "L": "And he was king in Jeshurun when the heads of the people were gathered, the tribes of Israel together.",
      "M": "The LORD became king over Jeshurun when the leaders of the people assembled, when all the tribes of Israel came together.",
      "T": "The LORD became king over Jeshurun —\nwhen the leaders assembled,\nwhen all the tribes of Israel gathered as one."
    },
    "6": {
      "L": "Let Reuben live, and not die, but let his men be few.",
      "M": "Let Reuben live and not die, though his numbers remain small.",
      "T": "Let Reuben live — not perish —\nthough his numbers stay small."
    },
    "7": {
      "L": "And this is for Judah. He said, 'Hear, O LORD, the voice of Judah and bring him in to his people. His hands contend for him and you shall be a help against his adversaries.'",
      "M": "And of Judah he said, 'Hear, O LORD, the voice of Judah, and bring him back to his people. His hands fight for him; be his help against his enemies.'",
      "T": "'Hear Judah's cry, O LORD —\nbring him home to his people.\nHis hands fight alone;\nbe the strength that breaks his enemies.'"
    },
    "8": {
      "L": "And of Levi he said, 'Give to Levi your Thummim, and your Urim to your favored one, whom you tested at Massah, with whom you strove at the waters of Meribah.'",
      "M": "And of Levi he said, 'Grant your Thummim to Levi and your Urim to your faithful servant, whom you tested at Massah and with whom you contended at the waters of Meribah.'",
      "T": "'To Levi belongs the Thummim;\nto your devoted one, the Urim —\nthe one tested at Massah,\nchallenged at the waters of Meribah.'"
    },
    "9": {
      "L": "'who said of his father and mother, \"I regard them not,\" and who did not acknowledge his brothers or know his children. For he kept your word and guarded your covenant.'",
      "M": "'He put loyalty to God above family ties, not acknowledging his father and mother, not favoring his brothers or his own children. He obeyed your word and kept your covenant.'",
      "T": "'He said to father and mother, \"I do not know you\";\nhe would not acknowledge his brothers\nor favor his own children.\nHe chose your word over every human bond;\nhe kept your covenant without flinching.'"
    },
    "10": {
      "L": "'They shall teach Jacob your ordinances and Israel your law; they shall put incense before you and whole burnt offerings on your altar.'",
      "M": "'They will teach Jacob your decrees and Israel your law; they will offer incense before you and present burnt offerings on your altar.'",
      "T": "'They will teach Jacob your rulings\nand Israel your law.\nThey will offer incense before you;\nthey will lay burnt offerings on your altar.'"
    },
    "11": {
      "L": "'Bless, O LORD, his substance and accept the work of his hands. Strike through the loins of those who rise against him, of those who hate him, that they rise no more.'",
      "M": "'Bless his resources, LORD, and take pleasure in what he does. Shatter the strength of his enemies, those who hate him, so they cannot stand again.'",
      "T": "'Bless what Levi has, O LORD;\ntake pleasure in all he does.\nBreak the strength of those who oppose him —\nlet those who hate him never rise again.'"
    },
    "12": {
      "L": "Of Benjamin he said, 'The beloved of the LORD shall dwell in safety. The Most High encircles him all the day long, and he dwells between his shoulders.'",
      "M": "Of Benjamin he said, 'The beloved of the LORD rests in safety. The Most High shelters him all day long and dwells between his shoulders.'",
      "T": "'Benjamin — beloved of the LORD —\nsleeps in safety.\nThe Most High encircles him all day;\nhe makes his home between Benjamin's shoulders.'"
    },
    "13": {
      "L": "And of Joseph he said, 'Blessed by the LORD be his land, with the best gifts of heaven above and of the deep that crouches beneath,'",
      "M": "Of Joseph he said, 'May the LORD bless his land with the finest gifts of heaven above and of the deep waters beneath,'",
      "T": "'May the LORD bless Joseph's land\nwith the finest heaven bestows from above\nand the riches the deep yields from below.'"
    },
    "14": {
      "L": "'with the finest of the produce of the sun and the finest of the yield of the moons,'",
      "M": "'with the best crops grown under the sun, and the finest harvests brought by each season,'",
      "T": "'The choicest gifts of sunshine,\nthe best that each season brings —'"
    },
    "15": {
      "L": "'with the best of the ancient mountains and the abundance of the everlasting hills,'",
      "M": "'with the richest produce of the age-old mountains and the abundance of the everlasting hills,'",
      "T": "'the riches of the ancient hills,\nthe abundance of the everlasting heights —'"
    },
    "16": {
      "L": "'with the best of the earth and its fullness, and the favor of him who dwelt in the bush. Let these rest on the head of Joseph and on the crown of the head of the one separated from his brothers.'",
      "M": "'with the best of the land and its fullness, and the goodwill of him who appeared in the burning bush. May all this rest on Joseph's head — the crown of the prince among his brothers.'",
      "T": "'all the richness of the earth and its fullness —\nand the blessing of him who appeared in the burning bush.\nLet all this rest on Joseph's head,\non the brow of the one set apart among his brothers.'"
    },
    "17": {
      "L": "'The firstborn of his bull has majesty, and his horns are the horns of a wild ox. With them he shall gore the peoples, all of them, to the ends of the earth. These are the ten thousands of Ephraim and the thousands of Manasseh.'",
      "M": "'His firstborn bull has majesty — his horns are like the horns of a wild ox. With them he will drive the nations to the ends of the earth. These are the ten thousands of Ephraim and the thousands of Manasseh.'",
      "T": "'His firstborn is like a bull in its prime —\nwild-ox horns crown him.\nWith them he will gore the nations\nto the very ends of the earth:\nEphraim's ten thousands,\nManasseh's thousands.'"
    },
    "18": {
      "L": "And of Zebulun he said, 'Rejoice, Zebulun, in your going out, and Issachar, in your tents.'",
      "M": "Of Zebulun he said, 'Rejoice, Zebulun, in your ventures abroad, and Issachar, in your tents.'",
      "T": "'Rejoice, Zebulun, as you go out to sea;\nand Issachar, rejoice in your tents at home.'"
    },
    "19": {
      "L": "'They shall call peoples to the mountain; there they shall offer sacrifices of righteousness. For they shall suck the abundance of the seas and the hidden treasures of the sand.'",
      "M": "'They will summon nations to their mountain and offer sacrifices there that are right. They will draw from the abundance of the seas and the hidden riches buried in the sand.'",
      "T": "'They summon the nations to their mountain;\nthere they offer righteous sacrifices.\nThey tap the riches of the sea\nand the hidden treasures buried in the shore.'"
    },
    "20": {
      "L": "And of Gad he said, 'Blessed be he who enlarges Gad! Gad crouches like a lion; he tears off arm and scalp.'",
      "M": "Of Gad he said, 'Blessed is he who gives Gad room to grow! He crouches like a lion, tearing arm and scalp.'",
      "T": "'Blessed be the one who expands Gad's territory!\nGad crouches like a lion;\nhe tears arm and scalp apart.'"
    },
    "21": {
      "L": "'He chose the first part for himself, for there a commander's portion was reserved; and he came with the leaders of the people; he carried out the righteous acts of the LORD and his judgments with Israel.'",
      "M": "'He secured the best territory for himself, where a leader's portion was set aside. He marched with the heads of the people and carried out the LORD's righteous decrees and his judgments for Israel.'",
      "T": "'He chose the choicest portion for himself —\na commander's share was reserved there.\nHe marched with Israel's leaders\nand executed the LORD's justice among his people.'"
    },
    "22": {
      "L": "And of Dan he said, 'Dan is a lion's cub; he leaps from Bashan.'",
      "M": "Of Dan he said, 'Dan is a lion's cub that springs out of Bashan.'",
      "T": "'Dan is a lion's cub —\nhe leaps from the heights of Bashan.'"
    },
    "23": {
      "L": "And of Naphtali he said, 'O Naphtali, satisfied with favor and full of the blessing of the LORD, take possession of the west and the south.'",
      "M": "Of Naphtali he said, 'Naphtali — overflowing with favor, full of the LORD's blessing — take possession of the sea and the south.'",
      "T": "'Naphtali — fed full with favor,\nbrimming with the LORD's blessing:\nown the sea-country and the south.'"
    },
    "24": {
      "L": "And of Asher he said, 'Most blessed of sons be Asher; let him be the favored of his brothers and let him dip his foot in oil.'",
      "M": "Of Asher he said, 'Most blessed among sons is Asher; may he be the favorite of his brothers and may he dip his feet in olive oil.'",
      "T": "'Most blessed of the sons is Asher —\nfavored by his brothers,\nstanding in oil up to his feet.'"
    },
    "25": {
      "L": "'Your locks shall be iron and bronze; as your days, so shall your strength be.'",
      "M": "'Your bolts shall be iron and bronze; may your strength match the length of your days.'",
      "T": "'Your fastening is iron and bronze;\nand whatever the days bring,\nyour strength shall match them.'"
    },
    "26": {
      "L": "'There is none like God, O Jeshurun, who rides through the heavens as your help and in his excellency through the skies.'",
      "M": "'There is no one like the God of Jeshurun, who rides through the heavens to help you, through the skies in his majesty.'",
      "T": "'None is like the God of Jeshurun —\nhe rides through the heavens to your aid,\nthrough the skies in his splendor.'"
    },
    "27": {
      "L": "'The eternal God is your dwelling place and underneath are the everlasting arms. And he drove out the enemy before you and said, \"Destroy!\"'",
      "M": "'The eternal God is your refuge, and underneath are his everlasting arms. He drives out the enemy before you and commands, \"Destroy!\"'",
      "T": "'The God who has always been is where you live —\nand underneath you are everlasting arms.\nHe drives the enemy before you\nand says, \"Destroy them.\"'"
    },
    "28": {
      "L": "'So Israel dwelt in safety and alone — the fountain of Jacob — in a land of grain and wine, whose heavens drop dew.'",
      "M": "'Israel has lived in safety, Jacob alone in a land of grain and new wine, under a sky that drips with dew.'",
      "T": "'So Israel lives in safety —\nJacob alone in a land of grain and wine,\nunder skies that send down dew.'"
    },
    "29": {
      "L": "'Happy are you, O Israel! Who is like you, a people saved by the LORD, the shield of your help and the sword of your triumph! Your enemies shall come cringing to you, and you shall tread upon their high places.'",
      "M": "'What happiness is yours, O Israel! Who is like you — a people saved by the LORD, the shield who helps you, the sword of your victory! Your enemies will cower before you, and you will march over their high places.'",
      "T": "'How blessed you are, O Israel —\nunmatched among the nations!\nSaved by the LORD,\nshielded by him, avenged by him.\nYour enemies will cringe before you;\nyou will march across their heights.'"
    }
  },
  "34": {
    "1": {
      "L": "And Moses went up from the plains of Moab to Mount Nebo, to the top of Pisgah, which is opposite Jericho. And the LORD showed him all the land — Gilead as far as Dan,",
      "M": "Moses climbed from the plains of Moab to the top of Pisgah on Mount Nebo, which faces Jericho. And the LORD showed him the whole land — Gilead all the way to Dan,",
      "T": "Moses climbed from the plains of Moab to the summit of Pisgah, to Mount Nebo, looking out over Jericho. And the LORD showed him everything — the whole land spread before him: Gilead reaching to Dan,"
    },
    "2": {
      "L": "all Naphtali, the land of Ephraim and Manasseh, all the land of Judah as far as the western sea,",
      "M": "all of Naphtali, Ephraim, and Manasseh, all of Judah as far as the Mediterranean Sea,",
      "T": "all of Naphtali, the territories of Ephraim and Manasseh, all of Judah stretching to the western sea —"
    },
    "3": {
      "L": "the Negeb, and the Plain — the valley of Jericho, the city of palm trees — as far as Zoar.",
      "M": "the Negeb, the Jordan Valley, the city of palms at Jericho, all the way to Zoar.",
      "T": "the Negeb, the Jordan lowlands, Jericho — the city of palms — as far south as Zoar."
    },
    "4": {
      "L": "And the LORD said to him, 'This is the land of which I swore to Abraham, to Isaac, and to Jacob, saying, \"I will give it to your offspring.\" I have let you see it with your eyes, but you shall not cross over there.'",
      "M": "The LORD said to him, 'This is the land I promised to Abraham, Isaac, and Jacob, saying, \"I will give it to your descendants.\" I have let you see it with your own eyes, but you will not cross into it.'",
      "T": "'This is it,' the LORD said. 'The land I swore to Abraham, to Isaac, to Jacob — \"I will give it to your offspring.\" I have let you see every inch of it with your own eyes. But this is where your journey ends. You will not cross over.'"
    },
    "5": {
      "L": "And Moses the servant of the LORD died there in the land of Moab, according to the word of the LORD.",
      "M": "So Moses the servant of the LORD died there in the land of Moab, just as the LORD had said.",
      "T": "And so Moses died — there, in the land of Moab, in obedience to the LORD's own word. The servant of God had reached the boundary the LORD set for him, and he went no further."
    },
    "6": {
      "L": "And he buried him in the valley in the land of Moab opposite Beth-peor; but no one knows his burial place to this day.",
      "M": "The LORD buried him in a valley in Moab, across from Beth-peor. No one has ever found the location of his grave, to this day.",
      "T": "God himself buried Moses in a valley in Moab, across from Beth-peor. And to this day, no one knows where the grave is. There is no shrine, no monument — the greatest prophet who ever lived has no marked tomb. His legacy is not a location; it is a people and a law."
    },
    "7": {
      "L": "Moses was a hundred and twenty years old when he died. His eye was undimmed and his natural vigor had not diminished.",
      "M": "Moses was a hundred and twenty years old when he died, yet his eyesight was still sharp and his strength had not faded.",
      "T": "Moses was one hundred and twenty years old at his death, yet his eyes were still clear and his strength unbroken. He did not die worn out — he died at the boundary God set, no earlier."
    },
    "8": {
      "L": "And the people of Israel wept for Moses in the plains of Moab thirty days. Then the days of weeping and mourning for Moses were ended.",
      "M": "The Israelites mourned for Moses in the plains of Moab for thirty days, until their weeping and mourning came to an end.",
      "T": "Israel mourned Moses in the plains of Moab for thirty days — the full period of formal grieving. Then the mourning was over. Israel wept for Moses as they had wept for Aaron. He was irreplaceable, and they knew it."
    },
    "9": {
      "L": "And Joshua the son of Nun was full of the spirit of wisdom, for Moses had laid his hands on him. So the people of Israel obeyed him and did as the LORD had commanded Moses.",
      "M": "Joshua son of Nun was filled with the spirit of wisdom because Moses had laid his hands on him. So the Israelites listened to Joshua and did what the LORD had commanded through Moses.",
      "T": "Joshua son of Nun was filled with the spirit of wisdom — Moses had laid his hands on him in commissioning. Israel recognized the transfer of authority and obeyed Joshua as they had obeyed Moses, doing what the LORD had commanded. The mission continued."
    },
    "10": {
      "L": "And there has not arisen since a prophet in Israel like Moses, whom the LORD knew face to face,",
      "M": "No prophet has arisen in Israel since who was like Moses — one whom the LORD knew face to face.",
      "T": "There has never been another prophet in Israel like Moses — not in the generations since his death. The LORD knew him face to face: direct speech, not vision or dream, not mystery and symbol, but open conversation between God and the one he chose."
    },
    "11": {
      "L": "for all the signs and wonders which the LORD sent him to do in the land of Egypt — to Pharaoh and to all his servants and to all his land —",
      "M": "No one else performed all the signs and wonders the LORD sent him to do in Egypt — against Pharaoh, his officials, and his whole land —",
      "T": "No one else performed those signs and wonders in Egypt — what the LORD sent Moses to do before Pharaoh, before his whole court, before the entire land of Egypt."
    },
    "12": {
      "L": "and for all the mighty hand and all the great terror which Moses did in the sight of all Israel.",
      "M": "or the mighty power and awesome deeds that Moses displayed before all Israel.",
      "T": "No one else displayed that mighty hand — the awesome deeds of power and terror — performed in full view of all Israel. Moses stands alone in the story of God's people. And now the story moves on."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'deuteronomy')
        merge_tier(existing, DEUTERONOMY, tier_key)
        save(tier_dir, 'deuteronomy', existing)
    print('Deuteronomy 31–34 written.')

if __name__ == '__main__':
    main()
