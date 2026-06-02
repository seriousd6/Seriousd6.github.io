"""
MKT Joshua chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-joshua-1-6.py

Covers: Joshua's commission and the charge to meditate on the Torah (ch. 1); the spies and
Rahab's confession of faith (ch. 2); the miraculous Jordan crossing with the priests bearing
the ark (ch. 3); the twelve memorial stones at Gilgal (ch. 4); circumcision, Passover, manna
ceases, and the Commander of the LORD's army (ch. 5); the seven-day march and the fall of
Jericho under herem (ch. 6).

Translation decisions:
- H3068 (יהוה): "LORD" (small caps) L/M; "the LORD" T — consistent with all prior OT scripts
- H430 (אֱלֹהִים): "God" all tiers
- H2617 (חֶסֶד): "kindness" L; "faithful kindness" M; "steadfast loyal love" T — Rahab's
  request in 2:12,14 and 6:17,25 carries full covenant-loyalty force; no single word suffices
- H1285 (בְּרִית): "covenant" all tiers
- H5315 (נֶפֶשׁ): "soul" L; "life" M; "life" T — context here is physical safety/survival,
  not theological discussion of the soul; T uses "our lives" or "our whole selves" where apt
- H7307 (רוּחַ) in 5:1: "spirit" L; "courage" M; "resolve" T — the Canaanite kings had no
  spirit/courage left after hearing of the Jordan crossing; ambiguity (breath/spirit/courage)
  is intentional; T surfaces the psychological collapse of enemy resistance
- H2388 + H553 (חָזַק + אָמַץ): "be strong and courageous" all tiers; T adds interpretive
  framing to convey the command's force as divine enablement not mere self-encouragement
- H2764 / H2763 (חֵרֶם / חָרַם): "devoted thing / utterly destroy" L;
  "devoted to destruction" M; "placed under the sacred ban / given over to God" T —
  the herem concept is a holy-war dedication of captured persons/goods to God, not mere
  genocide; T attempts to surface the theological framing while not softening the severity
- H3104 (יוֹבֵל) / H7782 (שׁוֹפָר): both rendered "ram's horn trumpets" L; "rams' horns" M;
  "ram's-horn trumpets / shofars" T — the Jericho horns are specifically jubilee/rams'-horn
  instruments, not standard battle trumpets
- H8451 (תּוֹרָה): "law/Torah" L; "the Law" M; "the Torah" T — in 1:7-8, the whole teaching
  of Moses is in view, not just legal code; T uses "Torah" to signal its comprehensive scope
- H5157 / H5159 (נָחַל / נַחֲלָה): "inherit / inheritance" all tiers
- H4135 (מוּל): "circumcise" all tiers
- H6453 (פֶּסַח): "Passover" all tiers
- H4478 (מָן): "manna" all tiers
- H6944 (קֹדֶשׁ): "holy" all tiers; in 5:15 the ground is "holy" because the LORD is present —
  T notes the echo of Moses at the burning bush (Exod 3:5)
- H7650 (שָׁבַע): "swear/oath" all tiers; Rahab's oath with the spies is a formal treaty
- H7343 (רָחָב): Rahab — proper noun always; her faith-confession in 2:9-11 is one of the
  most significant conversion narratives in the OT; T honours this
- H726 (אֱמוֹרִי) etc.: tribal names rendered as standard English transliterations throughout
- H2146 (זִכָּרוֹן): "memorial / sign" L; "memorial" M/T — the 12 stones in ch. 4 serve
  as a catechetical object: "when your children ask..." pattern echoing Passover instruction
- Ch. 1:8 note: "This Book of the Law shall not depart from your mouth" — meditation (הָגָה,
  murmuring/pondering) is a liturgical-oral practice, not silent reading; T preserves this
- Ch. 2:11 note: Rahab's confession ("the LORD your God, he is God in heaven above and on
  the earth beneath") is structurally identical to the Shema's monotheistic claim;
  T notes she is the first Gentile in Joshua to articulate Israel's core creed
- Ch. 3:15-16 note: Jordan at flood stage — the harvest-time crossing (barley harvest) is when
  the river was most impassable; the miracle is maximal. "Adam" (v.16) is the name of a town
  upstream where the waters piled up — a geographic marker preserved in all tiers
- Ch. 4:9 note: Joshua sets up a second set of 12 stones in the middle of the Jordan itself
  (v.9), separate from the 12 Gilgal stones (v.20) — T distinguishes the two sets
- Ch. 5:2 note: "Circumcise again a second time" — the generation born in the wilderness had
  not been circumcised (vv.4-7); entering the covenant land requires covenant-sign renewal
- Ch. 5:13-15 note: The "Commander of the LORD's army" is a theophanic figure (cf. the Angel
  of the LORD); Joshua's posture of worship (prostration, "my lord") and the holy-ground
  command echo Moses at the burning bush; T draws out this parallel explicitly
- Ch. 6 note: The fall of Jericho is paradigmatic holy war — God fights; Israel obeys the
  ritual; the victory is God's. The herem principle means the conquest is not Israel's plunder
  but God's. Rahab's scarlet cord (H8615 / H8144) echoes the Passover blood — faith marked
  on a house spares its occupants from judgment
- Ch. 6:26 note: Joshua's curse on rebuilding Jericho is fulfilled 500+ years later in
  1 Kings 16:34 (Hiel of Bethel) — T notes the prophetic fulfilment
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

JOSHUA = {
  "1": {
    "1": {
      "L": "And it came to pass after the death of Moses the servant of the LORD, that the LORD spoke to Joshua the son of Nun, the minister of Moses, saying,",
      "M": "After the death of Moses the servant of the LORD, the LORD said to Joshua son of Nun, Moses' aide:",
      "T": "After Moses the servant of the LORD died, the LORD spoke to Joshua son of Nun — Moses' faithful attendant — and said:"
    },
    "2": {
      "L": "Moses my servant is dead. Now therefore arise, cross over this Jordan, you and all this people, to the land which I am giving to them — to the children of Israel.",
      "M": "My servant Moses is dead. Now, you and all this people, get ready to cross the Jordan River into the land I am giving to the Israelites.",
      "T": "My servant Moses has died. Now rise — take all this people across the Jordan into the land I am giving them."
    },
    "3": {
      "L": "Every place that the sole of your foot shall tread upon I have given to you, as I spoke to Moses.",
      "M": "I will give you every place where you set your foot, as I promised Moses.",
      "T": "Every place your foot touches, I have already given to you — just as I declared to Moses."
    },
    "4": {
      "L": "From the wilderness and this Lebanon even to the great river, the river Euphrates — all the land of the Hittites — and to the Great Sea toward the going down of the sun shall be your border.",
      "M": "Your territory will extend from the wilderness and Lebanon in the north to the great Euphrates River in the east, through all the land of the Hittites, and westward to the Mediterranean Sea.",
      "T": "Your domain stretches from the southern wilderness and Mount Lebanon northward to the great Euphrates River — the entire Hittite country — all the way west to the Mediterranean."
    },
    "5": {
      "L": "No man shall be able to stand before you all the days of your life. As I was with Moses, so I will be with you. I will not fail you or forsake you.",
      "M": "No one will be able to stand against you all the days of your life. Just as I was with Moses, so I will be with you; I will never leave you nor forsake you.",
      "T": "No one will ever be able to stand against you all your life. As I was present with Moses, I will be present with you — I will never abandon you or give up on you."
    },
    "6": {
      "L": "Be strong and courageous, for you shall cause this people to inherit the land which I swore to their fathers to give to them.",
      "M": "Be strong and courageous, because you will lead this people to inherit the land I swore to their ancestors to give them.",
      "T": "Be strong and full of courage — it is you who will lead this people into possession of the land the LORD swore to their ancestors."
    },
    "7": {
      "L": "Only be strong and very courageous, to observe and do according to all the law which Moses my servant commanded you. Do not turn from it to the right hand or to the left, that you may prosper wherever you go.",
      "M": "Be strong and very courageous. Be careful to obey all the law that my servant Moses gave you; do not turn from it to the right or to the left, so that you may be successful wherever you go.",
      "T": "Above all, be strong and deeply courageous — careful to live by every word of the Torah my servant Moses gave you. Do not veer from it to the right or the left, so that you may thrive in everything you do."
    },
    "8": {
      "L": "This Book of the Law shall not depart from your mouth, but you shall meditate in it day and night, so that you may observe and do according to all that is written in it. For then you shall make your way prosperous, and then you shall have good success.",
      "M": "Keep this Book of the Law always on your lips; meditate on it day and night, so that you may be careful to do everything written in it. Then you will be prosperous and successful.",
      "T": "Let this Torah never leave your lips — murmur it, turn it over in your mind, day and night, and live by every word written there. That is the path to true prosperity; that is how you will succeed."
    },
    "9": {
      "L": "Have I not commanded you? Be strong and courageous. Do not be afraid; do not be dismayed, for the LORD your God is with you wherever you go.",
      "M": "Have I not commanded you? Be strong and courageous. Do not be terrified; do not be discouraged, for the LORD your God will be with you wherever you go.",
      "T": "I have commanded you: be strong and bold. Do not be afraid; do not lose heart — the LORD your God goes with you every step of the way."
    },
    "10": {
      "L": "Then Joshua commanded the officers of the people, saying,",
      "M": "So Joshua ordered the officers of the people:",
      "T": "Joshua then gave orders to the commanders of the people:"
    },
    "11": {
      "L": "\"Pass through the midst of the camp and command the people, saying, 'Prepare your provisions, for within three days you will cross over this Jordan to go in and possess the land which the LORD your God is giving you to possess.'\"",
      "M": "\"Go through the camp and tell the people: 'Get your supplies ready. Three days from now you will cross the Jordan to take possession of the land the LORD your God is giving you.'\"",
      "T": "\"Move through the camp and say to the people: 'Prepare your provisions — in three days you cross this Jordan and enter the land the LORD your God is giving you to make your own.'\""
    },
    "12": {
      "L": "And to the Reubenites, and to the Gadites, and to the half-tribe of Manasseh, Joshua spoke, saying,",
      "M": "But to the Reubenites, Gadites, and the half-tribe of Manasseh, Joshua said:",
      "T": "Then Joshua addressed the Reubenites, Gadites, and the half-tribe of Manasseh:"
    },
    "13": {
      "L": "\"Remember the word which Moses the servant of the LORD commanded you, saying, 'The LORD your God is giving you rest and has given you this land.'\"",
      "M": "\"Remember what Moses the servant of the LORD commanded you: 'The LORD your God is giving you rest and has granted you this land.'\"",
      "T": "\"Keep in mind what Moses the LORD's servant commanded you: 'The LORD your God is granting you rest and giving you this land.'\""
    },
    "14": {
      "L": "\"Your wives, your little ones, and your cattle shall remain in the land which Moses gave you beyond the Jordan. But all the mighty men of valor among you shall cross over armed before your brothers and help them,\"",
      "M": "\"Your wives, children, and livestock may remain in the land Moses gave you east of the Jordan. But all your fighting men must cross over armed, ahead of your fellow Israelites, to help them,\"",
      "T": "\"Your wives, children, and flocks may stay in the land Moses granted you east of the Jordan. But every warrior among you must cross over fully armed ahead of your brothers and fight alongside them\""
    },
    "15": {
      "L": "\"until the LORD gives rest to your brothers as to you, and they also possess the land which the LORD your God is giving to them. Then you shall return to the land of your possession and possess it, which Moses the servant of the LORD gave you beyond the Jordan toward the sunrise.\"",
      "M": "\"until the LORD gives your brothers rest just as he has given you, and they too have taken possession of the land the LORD your God is giving them. After that you may return to your own land east of the Jordan, which Moses the LORD's servant gave you.\"",
      "T": "\"until the LORD settles your brothers into rest just as he has settled you, and they too take hold of the land the LORD your God is giving them. Then you may return to your territory east of the Jordan — the land Moses the LORD's servant gave you.\""
    },
    "16": {
      "L": "And they answered Joshua, saying, 'All that you have commanded us we will do, and wherever you send us we will go.'",
      "M": "They answered Joshua, 'Whatever you command us, we will do, and wherever you send us, we will go.'",
      "T": "They answered Joshua: 'Every order you give us, we will carry out; wherever you send us, we will go.'"
    },
    "17": {
      "L": "Just as we hearkened to Moses in all things, so we will hearken to you. Only may the LORD your God be with you, as he was with Moses!",
      "M": "We will obey you just as we fully obeyed Moses. May the LORD your God be with you as he was with Moses!",
      "T": "We obeyed Moses in everything, and we will obey you the same way. May the LORD your God be with you as he was with Moses!"
    },
    "18": {
      "L": "Whoever rebels against your commandment and does not hearken to your words in all that you command him shall be put to death. Only be strong and courageous.",
      "M": "Anyone who rebels against your authority and refuses to obey whatever you command will be put to death. Only be strong and courageous.",
      "T": "Any man who defies your command and refuses to follow your word will be put to death. Be strong — be courageous."
    }
  },
  "2": {
    "1": {
      "L": "And Joshua the son of Nun sent secretly two men as spies from Shittim, saying, 'Go, view the land, even Jericho.' And they went and came into the house of a woman who was a prostitute, whose name was Rahab, and they lodged there.",
      "M": "Then Joshua son of Nun secretly sent two spies from Shittim. He said, 'Go, look over the land — especially Jericho.' So they went and entered the house of a prostitute named Rahab and stayed there.",
      "T": "Joshua son of Nun secretly dispatched two spies from Shittim with these orders: 'Scout the land — Jericho especially.' They went in and came to the house of a woman named Rahab, a prostitute, and spent the night there."
    },
    "2": {
      "L": "And it was told to the king of Jericho, saying, 'Behold, men from the children of Israel have come here tonight to search out the country.'",
      "M": "The king of Jericho was told, 'Look — some Israelites have come here tonight to spy out the land.'",
      "T": "Word reached the king of Jericho: 'Israelites have arrived here tonight to scout our country.'"
    },
    "3": {
      "L": "So the king of Jericho sent to Rahab, saying, 'Bring out the men who have come to you, who entered your house, for they have come to search out all the country.'",
      "M": "So the king of Jericho sent this message to Rahab: 'Bring out the men who came to you and entered your house — they have come to spy out the whole country.'",
      "T": "The king of Jericho sent word to Rahab: 'Hand over the men who came to your house — they have come to spy out this whole country.'"
    },
    "4": {
      "L": "But the woman took the two men and hid them, and she said, 'Yes, the men came to me, but I did not know where they were from.'",
      "M": "But the woman had taken the two men and hidden them. She said, 'Yes, the men came to me, but I didn't know where they were from.'",
      "T": "But the woman had already hidden the two men. She told the messengers: 'The men did come to me — but I had no idea where they were from.'"
    },
    "5": {
      "L": "'And it came to pass when the gate was about to be shut at dark that the men went out. I do not know where the men went. Pursue them quickly, for you shall overtake them.'",
      "M": "'At dusk, just when it was time to close the city gate, the men left. I don't know which way they went. Go after them quickly — you may catch them.'",
      "T": "'At dusk, just as the gate was closing, they left. I have no idea which way they went. Go after them now — you may still catch them!'"
    },
    "6": {
      "L": "But she had brought them up to the roof of the house and hidden them with the stalks of flax which she had laid in order upon the roof.",
      "M": "Actually, she had taken them up to the roof and hidden them under the stalks of flax she had laid out there.",
      "T": "In fact, she had already taken them up to the roof and concealed them beneath the stalks of flax she had spread out there to dry."
    },
    "7": {
      "L": "And the men pursued after them on the way to the Jordan, to the fords. And as soon as those who pursued them had gone out, the gate was shut.",
      "M": "So the men set out in pursuit along the road to the Jordan, all the way to the fords. As soon as the pursuers had gone out, the gate was shut.",
      "T": "The search party headed off along the road toward the Jordan as far as the river crossings. The gate was shut behind them the moment they left."
    },
    "8": {
      "L": "And before they lay down, she came up to them upon the roof,",
      "M": "Before the spies lay down for the night, she came up to them on the roof",
      "T": "Before they settled in for the night, Rahab came up to them on the roof"
    },
    "9": {
      "L": "and said to the men, 'I know that the LORD has given you the land, and that your terror has fallen upon us, and that all the inhabitants of the land melt away before you.'",
      "M": "and said to them, 'I know the LORD has given you this land, and that great fear of you has fallen on us, so that all who live in the country are melting in fear because of you.'",
      "T": "and said: 'I know the LORD has given you this land. Your coming has thrown us all into dread — everyone in the country has dissolved in fear before you.'"
    },
    "10": {
      "L": "'For we have heard how the LORD dried up the water of the Red Sea before you when you came out of Egypt, and what you did to the two kings of the Amorites who were on the other side of the Jordan, Sihon and Og, whom you utterly destroyed.'",
      "M": "'We heard how the LORD dried up the Red Sea before you when you came out of Egypt, and what you did to the two Amorite kings east of the Jordan — Sihon and Og — whom you completely destroyed.'",
      "T": "'We heard how the LORD dried up the Red Sea ahead of you when you left Egypt, and what you did to Sihon and Og, the two Amorite kings beyond the Jordan — utterly destroying them.'"
    },
    "11": {
      "L": "'And as soon as we heard it, our hearts melted, and there was no more spirit in any man because of you, for the LORD your God, he is God in the heavens above and on the earth beneath.'",
      "M": "'When we heard it, our courage failed and everyone's spirit sank because of you, for the LORD your God is God in heaven above and on the earth below.'",
      "T": "'The moment we heard it, our hearts collapsed. No one had any resolve left — for the LORD your God is God above in the heavens and below on the earth. There is no other.'"
    },
    "12": {
      "L": "'Now therefore, I pray you, swear to me by the LORD, since I have dealt kindly with you, that you also will deal kindly with my father's house, and give me a true token,'",
      "M": "'Now then, please swear to me by the LORD that, since I have shown you kindness, you will also show faithful kindness to my father's family. Give me a sure sign'",
      "T": "'So now, swear to me by the LORD — since I have shown you loyal love, show that same steadfast loyalty to my family. Give me a reliable pledge'"
    },
    "13": {
      "L": "'that you will save alive my father and my mother, my brothers and my sisters, and all that they have, and deliver our lives from death.'",
      "M": "'that you will spare the lives of my father and mother, my brothers and sisters, and all who belong to them — that you will save us from death.'",
      "T": "'that you will spare my father, my mother, my brothers, my sisters, and all who are theirs — that you will rescue every one of us from death.'"
    },
    "14": {
      "L": "And the men said to her, 'Our life for yours, even to death! If you do not tell this our business, then when the LORD has given us the land we will deal kindly and truly with you.'",
      "M": "The men answered her, 'Our lives for yours! If you don't reveal our mission, we will deal faithfully and kindly with you when the LORD gives us this land.'",
      "T": "The men said to her: 'With our own lives we guarantee yours — we will die before you come to harm. Keep our mission secret, and when the LORD gives us this land, we will treat you with faithful, loyal love.'"
    },
    "15": {
      "L": "Then she let them down by a rope through the window, for her house was on the side of the city wall, and she dwelt within the wall itself.",
      "M": "So she let them down by a rope through the window, for the house she lived in was part of the city wall.",
      "T": "She lowered them by a rope through her window — her house was built into the city wall, and she lived within the wall itself."
    },
    "16": {
      "L": "And she said to them, 'Get you to the mountain, lest the pursuers meet you. Hide yourselves there three days until the pursuers have returned, and afterward you may go your way.'",
      "M": "She told them, 'Go to the hill country so the pursuers won't find you. Hide there for three days until they return, and then go on your way.'",
      "T": "'Head for the hills,' she told them. 'The search party must not find you. Stay hidden three days until they give up and come back — then you can be on your way.'"
    },
    "17": {
      "L": "And the men said to her, 'We will be blameless regarding this your oath which you have made us to swear,'",
      "M": "The men told her, 'We will be free of this oath you have bound us to,",
      "T": "'We will be clear of any guilt under this oath you've made us swear,' the men said,"
    },
    "18": {
      "L": "'unless, when we come into the land, you have bound this line of scarlet thread in the window through which you let us down, and have gathered into your house your father and your mother and your brothers and all your father's household.'",
      "M": "'unless, when we come into the land, you have tied this scarlet cord in the window you let us down from, and have brought your father, mother, brothers, and all your family into your house.'",
      "T": "'only under these conditions: when we come in, tie this scarlet cord in the window you lowered us from, and bring your father, mother, brothers, and every member of your family inside with you.'"
    },
    "19": {
      "L": "'And it shall be that whoever goes out of the doors of your house into the street, his blood shall be on his own head, and we shall be guiltless. But whoever is with you in the house, his blood shall be on our head if any hand is laid upon him.'",
      "M": "'If anyone goes out of your house into the street, their blood will be on their own head — we are not responsible. But if a hand is laid on anyone inside the house with you, their blood will be on our heads.'",
      "T": "'Anyone who steps outside your door into the street — their death is their own responsibility; we are not to blame. But anyone under your roof who is harmed — that blood is on us.'"
    },
    "20": {
      "L": "'And if you tell this our business, then we will be blameless regarding your oath which you have made us to swear.'",
      "M": "'But if you tell anyone about our business, we are released from the oath you have made us swear.'",
      "T": "'If you betray our mission to anyone, we are released from this oath entirely.'"
    },
    "21": {
      "L": "And she said, 'According to your words, so be it.' And she sent them away, and they departed. And she bound the scarlet line in the window.",
      "M": "She agreed, 'Let it be as you say.' And she sent them on their way and they left. Then she tied the scarlet cord in the window.",
      "T": "'Agreed,' she said. 'Let it be exactly as you say.' She sent them off and they went, and she tied the scarlet cord in the window."
    },
    "22": {
      "L": "And they departed and went to the mountain and remained there three days until the pursuers returned. And the pursuers searched all along the way but found nothing.",
      "M": "They left and went into the hill country and stayed there three days until the pursuers had returned. The pursuers searched the whole road but found nothing.",
      "T": "They departed into the hills and stayed three days until the search party came back. The pursuers had combed the whole route and found nothing."
    },
    "23": {
      "L": "So the two men returned and descended from the mountain and crossed over and came to Joshua the son of Nun, and they told him all that had befallen them.",
      "M": "Then the two men started back, came down from the hills, crossed the river, and returned to Joshua son of Nun. They reported everything that had happened to them.",
      "T": "The two men came back down from the hills, crossed the Jordan, and returned to Joshua son of Nun. They told him everything that had happened."
    },
    "24": {
      "L": "And they said to Joshua, 'Truly the LORD has given all the land into our hands, for even all the inhabitants of the country do melt away before us.'",
      "M": "They said to Joshua, 'The LORD has surely given the whole land into our hands; all the people there are melting in fear before us.'",
      "T": "They told Joshua: 'The LORD has truly given the whole land into our hands — every single inhabitant there has melted in fear before us.'"
    }
  },
  "3": {
    "1": {
      "L": "And Joshua rose early in the morning and they removed from Shittim, and he and all the children of Israel came to the Jordan, and lodged there before they passed over.",
      "M": "Early the next morning Joshua and all the Israelites set out from Shittim and arrived at the Jordan, where they camped before crossing.",
      "T": "Early in the morning Joshua led all Israel from Shittim to the banks of the Jordan, and they camped there before making the crossing."
    },
    "2": {
      "L": "And it came to pass after three days that the officers went through the midst of the host,",
      "M": "After three days the officers went throughout the camp",
      "T": "Three days later the commanders moved through the camp"
    },
    "3": {
      "L": "and they commanded the people, saying, 'When you see the ark of the covenant of the LORD your God, and the Levitical priests bearing it, then you shall remove from your place and go after it.'",
      "M": "and gave the people this order: 'When you see the ark of the covenant of the LORD your God carried by the Levitical priests, then move out from your positions and follow it.'",
      "T": "with this command for the people: 'When you see the ark of the covenant of the LORD your God being carried by the Levitical priests, break camp and follow it.'"
    },
    "4": {
      "L": "'Yet there shall be a space between you and it of about two thousand cubits by measure. Come not near to it, that you may know the way by which you must go, for you have not passed this way heretofore.'",
      "M": "'But keep a distance of about two thousand cubits between you and it. Do not go near it, so you will know which way to go, since you have not traveled this road before.'",
      "T": "'Keep a gap of roughly two thousand cubits between you and the ark — do not close that distance — so you can see the route, for this is a road you have never walked before.'"
    },
    "5": {
      "L": "And Joshua said to the people, 'Sanctify yourselves, for tomorrow the LORD will do wonders among you.'",
      "M": "Joshua told the people, 'Consecrate yourselves, for tomorrow the LORD will do amazing things among you.'",
      "T": "Joshua said to the people: 'Set yourselves apart — consecrate yourselves — for tomorrow the LORD will do something extraordinary in your midst.'"
    },
    "6": {
      "L": "And Joshua spoke to the priests, saying, 'Take up the ark of the covenant and cross over before the people.' And they took up the ark of the covenant and went before the people.",
      "M": "Joshua told the priests, 'Lift up the ark of the covenant and cross over ahead of the people.' So they took up the ark of the covenant and went ahead of the people.",
      "T": "Then Joshua said to the priests: 'Lift the ark of the covenant and lead the way across.' The priests took up the ark and moved to the front of the people."
    },
    "7": {
      "L": "And the LORD said to Joshua, 'This day I will begin to magnify you in the sight of all Israel, that they may know that as I was with Moses, so I will be with you.'",
      "M": "The LORD said to Joshua, 'Today I will begin to exalt you in the eyes of all Israel, so they may know that as I was with Moses, so I will be with you.'",
      "T": "The LORD said to Joshua: 'This day I begin to make your name great before all Israel, so that they know — as surely as I was with Moses, I am with you.'"
    },
    "8": {
      "L": "And you shall command the priests who bear the ark of the covenant, saying, 'When you have come to the brink of the waters of the Jordan, you shall stand still in the Jordan.'",
      "M": "Command the priests who carry the ark of the covenant: 'When you reach the edge of the Jordan's waters, stand still in the river.'",
      "T": "Give this charge to the priests who carry the ark of the covenant: 'When your feet touch the edge of the Jordan's water, stand still right there in the river.'"
    },
    "9": {
      "L": "And Joshua said to the children of Israel, 'Come here and hear the words of the LORD your God.'",
      "M": "Joshua said to the Israelites, 'Come close and listen to the words of the LORD your God.'",
      "T": "Joshua called to all Israel: 'Come near — listen to the words of the LORD your God.'"
    },
    "10": {
      "L": "And Joshua said, 'Hereby you shall know that the living God is among you, and that he will without fail drive out from before you the Canaanites, and the Hittites, and the Hivites, and the Perizzites, and the Girgashites, and the Amorites, and the Jebusites.'",
      "M": "He said, 'By this you will know that the living God is among you, and that he will certainly drive out before you the Canaanites, Hittites, Hivites, Perizzites, Girgashites, Amorites, and Jebusites.'",
      "T": "'By what happens today you will know that the living God is in your midst — and that he will drive out from before you the Canaanites, Hittites, Hivites, Perizzites, Girgashites, Amorites, and Jebusites without fail.'"
    },
    "11": {
      "L": "Behold, the ark of the covenant of the Lord of all the earth is crossing over before you into the Jordan.",
      "M": "See, the ark of the covenant of the Lord of all the earth is going ahead of you into the Jordan.",
      "T": "Look — the ark of the covenant of the Lord of all the earth leads the way into the Jordan."
    },
    "12": {
      "L": "Now therefore take for yourselves twelve men out of the tribes of Israel, a man from each tribe.",
      "M": "Now choose twelve men from the tribes of Israel, one from each tribe.",
      "T": "Select twelve men from the tribes of Israel — one from each tribe."
    },
    "13": {
      "L": "And it shall come to pass, as soon as the soles of the feet of the priests who bear the ark of the LORD, the Lord of all the earth, shall rest in the waters of the Jordan, the waters of the Jordan shall be cut off — the waters flowing from above — and they shall stand up in a heap.",
      "M": "And when the priests who carry the ark of the LORD, the Lord of all the earth, plant their feet in the Jordan's waters, the Jordan's current will be cut off and the water coming from upstream will stand up in a heap.",
      "T": "The moment the feet of the priests carrying the ark of the LORD — Lord of all the earth — touch the Jordan's water, the flow will be cut off. The water coming down from upstream will pile up in a single heap."
    },
    "14": {
      "L": "So when the people set out from their tents to cross over the Jordan, and the priests who bore the ark of the covenant were before the people,",
      "M": "So when the people broke camp to cross the Jordan, and the priests carrying the ark of the covenant went ahead of them,",
      "T": "When the people set out from their tents to cross the Jordan, the priests carried the ark of the covenant out in front of them."
    },
    "15": {
      "L": "and as those who bore the ark came to the Jordan, and the feet of the priests bearing the ark were dipped in the brim of the water — for the Jordan overflows all its banks all the time of harvest —",
      "M": "and as the priests who carried the ark reached the Jordan and their feet touched the water's edge — the Jordan being at flood stage throughout the harvest season —",
      "T": "As the priests who carried the ark came to the Jordan and their feet dipped into the edge of the water — the Jordan was at full flood, overflowing all its banks throughout the harvest —"
    },
    "16": {
      "L": "the waters coming down from above stood and rose up in a heap far away at Adam, the city beside Zarethan, and those flowing down toward the Sea of the Arabah, the Salt Sea, failed and were cut off. And the people crossed over opposite Jericho.",
      "M": "the water flowing downstream was completely cut off and piled up in a heap a great distance away, at a town called Adam near Zarethan. The water flowing toward the Dead Sea of the Arabah was cut off completely, and the people crossed over opposite Jericho.",
      "T": "the water flowing downstream was cut off entirely and rose in a great heap far upstream at the town of Adam, near Zarethan. The water flowing toward the Dead Sea drained away completely. The people crossed on dry ground directly opposite Jericho."
    },
    "17": {
      "L": "And the priests who bore the ark of the covenant of the LORD stood firm on dry ground in the midst of the Jordan, and all Israel crossed over on dry ground, until all the nation had crossed over the Jordan completely.",
      "M": "The priests who carried the ark of the covenant of the LORD stood firm on dry ground in the middle of the Jordan while all Israel crossed on dry ground, until the whole nation had finished crossing.",
      "T": "The priests carrying the ark of the covenant stood firm on dry ground in the middle of the Jordan riverbed while all Israel crossed over — every last person — until the whole nation had gone across on dry ground."
    }
  },
  "4": {
    "1": {
      "L": "And it came to pass when all the nation had completely crossed over the Jordan, that the LORD spoke to Joshua, saying,",
      "M": "When the whole nation had finished crossing the Jordan, the LORD said to Joshua:",
      "T": "Once every person had crossed the Jordan, the LORD said to Joshua:"
    },
    "2": {
      "L": "\"Take for yourselves twelve men out of the people, a man from each tribe,\"",
      "M": "\"Choose twelve men from the people, one from each tribe,\"",
      "T": "\"Select twelve men from among the people — one from each tribe —\""
    },
    "3": {
      "L": "\"and command them, saying, 'Take up from here out of the midst of the Jordan, from the place where the priests' feet stood firm, twelve stones, and carry them over with you and leave them in the lodging place where you lodge tonight.'\"",
      "M": "\"and tell them: 'Take twelve stones from the middle of the Jordan — right where the priests stood — carry them over with you and set them down at the place where you camp tonight.'\"",
      "T": "\"and give them this charge: 'Lift out twelve stones from the Jordan riverbed — from the exact place where the priests stood firm — carry them with you, and set them down at tonight's camp.'\""
    },
    "4": {
      "L": "Then Joshua called the twelve men whom he had prepared from the children of Israel, a man from each tribe,",
      "M": "So Joshua called together the twelve men he had appointed from the Israelites, one from each tribe,",
      "T": "Joshua summoned the twelve men he had set aside — one from each tribe of Israel —"
    },
    "5": {
      "L": "and Joshua said to them, 'Cross over before the ark of the LORD your God into the midst of the Jordan, and each of you lift up a stone upon his shoulder, according to the number of the tribes of the children of Israel,'",
      "M": "and said to them, 'Go over ahead of the ark of the LORD your God into the middle of the Jordan. Each of you is to take up a stone on his shoulder, according to the number of the tribes of Israel,'",
      "T": "and said: 'Go back across ahead of the ark of the LORD your God into the middle of the Jordan. Each man, lift a stone onto your shoulder — one for each of the twelve tribes of Israel.'"
    },
    "6": {
      "L": "'so that this may be a sign among you. When your children ask in time to come, saying, \"What do these stones mean to you?\"'",
      "M": "'to serve as a sign among you. In the future, when your children ask, \"What do these stones mean?\"'",
      "T": "'These stones will be a sign among you. In days to come, when your children ask: \"What are these stones for?\"'"
    },
    "7": {
      "L": "'then you shall tell them that the waters of the Jordan were cut off before the ark of the covenant of the LORD. When it crossed over the Jordan, the waters of the Jordan were cut off. And these stones shall be a memorial to the children of Israel forever.'",
      "M": "'tell them that the flow of the Jordan was cut off before the ark of the covenant of the LORD. When the ark crossed the Jordan, the waters were cut off. These stones are to be a memorial to the Israelites forever.'",
      "T": "'answer them: the Jordan's water was cut off before the ark of the covenant of the LORD — when the ark passed over, the water stopped. These stones will be a lasting memorial for Israel in every generation.'"
    },
    "8": {
      "L": "And the children of Israel did so, just as Joshua commanded, and took up twelve stones out of the midst of the Jordan, as the LORD had spoken to Joshua, according to the number of the tribes of the children of Israel, and carried them over with them to the place where they lodged, and laid them down there.",
      "M": "The Israelites did as Joshua commanded. They took twelve stones from the middle of the Jordan, one for each tribe, just as the LORD had told Joshua, carried them to the camp, and set them down there.",
      "T": "The Israelites did exactly as Joshua commanded. They lifted twelve stones from the middle of the Jordan — one for each tribe, as the LORD had directed Joshua — carried them to the camp, and laid them down there."
    },
    "9": {
      "L": "And Joshua set up twelve stones in the midst of the Jordan, in the place where the feet of the priests who bore the ark of the covenant had stood, and they are there to this day.",
      "M": "Joshua also set up twelve stones in the middle of the Jordan at the spot where the priests who carried the ark had stood, and they are there to this day.",
      "T": "Joshua also set up a second set of twelve stones in the middle of the Jordan itself — at the precise place where the feet of the priests who bore the ark had stood. They remain there to this day."
    },
    "10": {
      "L": "For the priests who bore the ark stood in the midst of the Jordan until everything was finished that the LORD had commanded Joshua to speak to the people, according to all that Moses had commanded Joshua. And the people hurried and crossed over.",
      "M": "The priests who carried the ark remained standing in the middle of the Jordan until everything the LORD had commanded Joshua had been carried out, just as Moses had charged Joshua. And the people hurried across.",
      "T": "The priests stood in the middle of the Jordan until every command the LORD had given Joshua was fulfilled — everything Moses had charged Joshua to do. The people crossed quickly."
    },
    "11": {
      "L": "And it came to pass when all the people had completely crossed over, that the ark of the LORD and the priests crossed over in the presence of the people.",
      "M": "When all the people had finished crossing, the ark of the LORD and the priests crossed over in front of the people.",
      "T": "Once all the people had crossed, the ark of the LORD and the priests crossed over before the people to the other side."
    },
    "12": {
      "L": "And the sons of Reuben and the sons of Gad and the half-tribe of Manasseh crossed over armed before the children of Israel, as Moses had spoken to them.",
      "M": "The Reubenites, Gadites, and the half-tribe of Manasseh crossed over armed before the Israelites, as Moses had instructed them.",
      "T": "The Reubenites, Gadites, and the half-tribe of Manasseh crossed over in full battle formation ahead of the Israelites, just as Moses had directed them."
    },
    "13": {
      "L": "About forty thousand armed men crossed over before the LORD for battle, to the plains of Jericho.",
      "M": "About forty thousand soldiers, equipped for battle, crossed before the LORD to the plains of Jericho.",
      "T": "About forty thousand warriors, armed for war, marched before the LORD onto the plains of Jericho."
    },
    "14": {
      "L": "On that day the LORD magnified Joshua in the sight of all Israel, and they feared him as they had feared Moses, all the days of his life.",
      "M": "That day the LORD exalted Joshua in the sight of all Israel, and they held him in awe just as they had revered Moses, all the days of his life.",
      "T": "That day the LORD made Joshua great in the eyes of all Israel, and they stood in awe of him as they had stood in awe of Moses — all his life long."
    },
    "15": {
      "L": "And the LORD spoke to Joshua, saying,",
      "M": "The LORD said to Joshua,",
      "T": "The LORD said to Joshua:"
    },
    "16": {
      "L": "\"Command the priests who bear the ark of the testimony to come up out of the Jordan.\"",
      "M": "\"Command the priests who carry the ark of the testimony to come up out of the Jordan.\"",
      "T": "\"Tell the priests carrying the ark of testimony to come up out of the Jordan.\""
    },
    "17": {
      "L": "So Joshua commanded the priests, saying, \"Come up out of the Jordan.\"",
      "M": "So Joshua commanded the priests, \"Come up out of the Jordan.\"",
      "T": "Joshua gave the command: \"Come up out of the Jordan!\""
    },
    "18": {
      "L": "And it came to pass when the priests who bore the ark of the covenant of the LORD had come up out of the midst of the Jordan, and the soles of the priests' feet were lifted up to the dry land, that the waters of the Jordan returned to their place and flowed over all its banks as before.",
      "M": "As soon as the priests who carried the ark of the covenant of the LORD stepped out of the Jordan and their feet touched dry ground, the waters of the Jordan rushed back to their place and flooded all its banks as before.",
      "T": "The moment the feet of the priests bearing the ark of the covenant came up out of the Jordan and touched dry ground, the Jordan's waters poured back in, overflowing all its banks just as they had before."
    },
    "19": {
      "L": "And the people came up out of the Jordan on the tenth day of the first month and encamped in Gilgal, on the eastern border of Jericho.",
      "M": "The people came up from the Jordan on the tenth day of the first month and camped at Gilgal, on the east border of Jericho.",
      "T": "The people came up from the Jordan on the tenth day of the first month and made camp at Gilgal, on the eastern edge of Jericho's plain."
    },
    "20": {
      "L": "And those twelve stones which they had taken out of the Jordan, Joshua set up in Gilgal.",
      "M": "And Joshua set up at Gilgal the twelve stones they had taken out of the Jordan.",
      "T": "There at Gilgal, Joshua erected the twelve stones they had brought up from the Jordan."
    },
    "21": {
      "L": "And he spoke to the children of Israel, saying, 'When your children ask their fathers in time to come, saying, \"What are these stones?\"'",
      "M": "He told the Israelites, 'In the future when your children ask their fathers, \"What are these stones?\"'",
      "T": "He said to the Israelites: 'In the days to come, when your children ask their fathers, \"What are these stones for?\"'"
    },
    "22": {
      "L": "'then you shall let your children know, saying, \"Israel crossed this Jordan on dry land.\"'",
      "M": "'tell your children: \"Israel crossed the Jordan here on dry ground.\"'",
      "T": "'tell them: \"Here Israel crossed the Jordan on dry ground.\"\'"
    },
    "23": {
      "L": "'For the LORD your God dried up the waters of the Jordan before you until you had crossed over, as the LORD your God did to the Red Sea, which he dried up before us until we had crossed over,'",
      "M": "'For the LORD your God dried up the Jordan before you until you had crossed over, just as the LORD your God did to the Red Sea, which he dried up before us until we crossed over,'",
      "T": "'For the LORD your God dried up the Jordan ahead of you until you had crossed — just as he dried up the Red Sea for us until we crossed over.'"
    },
    "24": {
      "L": "'so that all the peoples of the earth may know the hand of the LORD, that it is mighty, and that you may fear the LORD your God always.'",
      "M": "'so that all the peoples of the earth may know that the LORD's hand is powerful, and so that you may always fear the LORD your God.'",
      "T": "'so that every people on earth would know that the LORD's hand is mighty — and so that you would fear the LORD your God for all time.'"
    }
  },
  "5": {
    "1": {
      "L": "And it came to pass when all the kings of the Amorites who were on the west side of the Jordan, and all the kings of the Canaanites who were by the sea, heard that the LORD had dried up the waters of the Jordan before the children of Israel until we had crossed over, that their heart melted, and there was no spirit left in any of them because of the children of Israel.",
      "M": "Now when all the Amorite kings west of the Jordan and all the Canaanite kings along the coast heard how the LORD had dried up the Jordan before the Israelites until they crossed over, their courage failed and they no longer had any resolve because of the Israelites.",
      "T": "When all the Amorite kings west of the Jordan and all the Canaanite kings along the coast heard how the LORD had dried up the Jordan before the Israelites until they crossed, every last ounce of resolve drained out of them. No one had the will to resist Israel."
    },
    "2": {
      "L": "At that time the LORD said to Joshua, 'Make for yourself flint knives and circumcise the children of Israel the second time.'",
      "M": "At that time the LORD said to Joshua, 'Make flint knives and circumcise the Israelites again.'",
      "T": "At that moment the LORD said to Joshua: 'Make flint knives and circumcise the Israelites — restore the covenant sign.'"
    },
    "3": {
      "L": "So Joshua made himself flint knives and circumcised the children of Israel at the Hill of the Foreskins.",
      "M": "So Joshua made flint knives and circumcised the Israelites at Gibeath-haaraloth.",
      "T": "Joshua made flint knives and circumcised all the Israelite men at Gibeath-haaraloth — the Hill of the Foreskins."
    },
    "4": {
      "L": "And this is the reason why Joshua circumcised them: all the people who came out of Egypt who were males, all the men of war, had died in the wilderness along the way after they came out of Egypt.",
      "M": "This is why Joshua circumcised them: all the men who had come out of Egypt — all the soldiers — had died in the wilderness on the way after leaving Egypt.",
      "T": "Here is why Joshua had to circumcise them: every man who had come out of Egypt — every fighting man of that generation — had died in the wilderness on the journey from Egypt."
    },
    "5": {
      "L": "For all the people who came out of Egypt had been circumcised, but all the people born in the wilderness along the way as they came out of Egypt had not been circumcised.",
      "M": "All the people who had come out of Egypt had been circumcised, but none of the people born in the wilderness during the journey had been circumcised.",
      "T": "Everyone who left Egypt had been circumcised, but the children born during the forty years in the wilderness had not received the covenant sign."
    },
    "6": {
      "L": "For the children of Israel walked forty years in the wilderness until all the nation — the men of war who came out of Egypt — were consumed, because they did not obey the voice of the LORD. The LORD swore that he would not show them the land which he had sworn to their fathers to give us, a land flowing with milk and honey.",
      "M": "The Israelites had moved about in the wilderness for forty years until all the men of fighting age who came out of Egypt had died, since they had not obeyed the LORD. For the LORD had sworn they would not see the land he had solemnly promised their ancestors — a land flowing with milk and honey.",
      "T": "Israel had wandered in the wilderness forty years until the entire generation of soldiers who left Egypt was gone — they had not obeyed the LORD's voice. So the LORD had sworn they would never see the land he had promised to give their ancestors: a land flowing with milk and honey."
    },
    "7": {
      "L": "And he raised up their children in their place, and these Joshua circumcised, for they were uncircumcised because they had not been circumcised along the way.",
      "M": "Their children had taken their place, and Joshua circumcised them, for they had not been circumcised on the journey.",
      "T": "Their sons had taken their place, and it was these Joshua now circumcised — they had gone without the covenant sign all through the journey."
    },
    "8": {
      "L": "And when all the nation had been circumcised, they remained in their places in the camp until they were healed.",
      "M": "After the whole nation had been circumcised, they remained in camp until they had healed.",
      "T": "After every man had been circumcised, they stayed in the camp and recovered until they were whole."
    },
    "9": {
      "L": "Then the LORD said to Joshua, 'Today I have rolled away the reproach of Egypt from you.' And the name of that place has been called Gilgal to this day.",
      "M": "The LORD said to Joshua, 'Today I have rolled away the disgrace of Egypt from you.' So that place has been called Gilgal to this day.",
      "T": "The LORD said to Joshua: 'Today I have rolled away the shame of Egypt from you.' And so that place has been called Gilgal — meaning 'rolled' — to this day."
    },
    "10": {
      "L": "And the children of Israel encamped in Gilgal, and they kept the Passover on the fourteenth day of the month at evening on the plains of Jericho.",
      "M": "The Israelites camped at Gilgal and celebrated the Passover on the evening of the fourteenth day of the month on the plains of Jericho.",
      "T": "Israel camped at Gilgal and kept the Passover — at evening on the fourteenth day of the month — out on the plains of Jericho."
    },
    "11": {
      "L": "And on the day after the Passover, on that very day, they ate of the produce of the land, unleavened cakes and parched grain.",
      "M": "The day after the Passover, that very day, they ate from the produce of the land — unleavened bread and roasted grain.",
      "T": "The morning after the Passover — that same day — they ate from the land's own produce: flat unleavened bread and roasted grain."
    },
    "12": {
      "L": "And the manna ceased on the day after they had eaten of the produce of the land, and there was no longer manna for the children of Israel. They ate of the fruit of the land of Canaan that year.",
      "M": "The manna stopped the day after they ate this food from the land; there was no more manna for the Israelites, and that year they ate the produce of Canaan.",
      "T": "The manna stopped the morning after they ate from the land. There was no more manna for Israel from that day forward. That year they ate what the land of Canaan itself produced."
    },
    "13": {
      "L": "And it came to pass when Joshua was by Jericho, that he lifted up his eyes and looked, and behold, a man stood before him with his drawn sword in his hand. And Joshua went to him and said to him, 'Are you for us or for our adversaries?'",
      "M": "When Joshua was near Jericho, he looked up and saw a man standing in front of him with a drawn sword in his hand. Joshua went up to him and asked, 'Are you for us or for our enemies?'",
      "T": "While Joshua was near Jericho, he looked up and saw a man standing right before him with his sword drawn. Joshua walked toward him and said: 'Whose side are you on — ours or our enemies'?'"
    },
    "14": {
      "L": "And he said, 'No, but as captain of the host of the LORD I have now come.' And Joshua fell on his face to the earth and worshipped, and said to him, 'What does my lord say to his servant?'",
      "M": "He replied, 'Neither — as commander of the LORD's army I have come.' Then Joshua fell facedown to the ground in reverence and asked him, 'What message does my lord have for his servant?'",
      "T": "'Neither,' the man replied. 'I come as Commander of the LORD's army.' Joshua fell face to the ground and bowed in worship, then said: 'What command does my lord have for his servant?'"
    },
    "15": {
      "L": "And the Commander of the LORD's host said to Joshua, 'Take off your sandal from your foot, for the place where you stand is holy.' And Joshua did so.",
      "M": "The Commander of the LORD's army replied, 'Take off your sandal from your foot, for the place where you are standing is holy.' And Joshua did so.",
      "T": "The Commander of the LORD's army said: 'Remove your sandal from your foot — the ground where you stand is holy ground.' Joshua obeyed."
    }
  },
  "6": {
    "1": {
      "L": "Now Jericho was shut up and barred because of the children of Israel. None went out and none came in.",
      "M": "Now Jericho was tightly shut up because of the Israelites — no one went out and no one came in.",
      "T": "Jericho was sealed tight on account of Israel — the gates were barred, no one going in, no one coming out."
    },
    "2": {
      "L": "And the LORD said to Joshua, 'See, I have given Jericho into your hand, with its king and the mighty men of valor.'",
      "M": "Then the LORD said to Joshua, 'See, I have delivered Jericho into your hands, along with its king and its fighting men.'",
      "T": "Then the LORD said to Joshua: 'Look — I have handed Jericho over to you, its king, and all its warriors.'"
    },
    "3": {
      "L": "You shall march around the city, all the men of war, going around the city once. Thus shall you do for six days.",
      "M": "'March around the city once with all the armed men. Do this for six days.'",
      "T": "'Have all the soldiers march around the city — once around, each day. Do this for six days.'"
    },
    "4": {
      "L": "'And seven priests shall bear seven trumpets of rams' horns before the ark. On the seventh day you shall march around the city seven times, and the priests shall blow the trumpets.'",
      "M": "'Have seven priests carry seven rams' horns in front of the ark. On the seventh day march around the city seven times, with the priests blowing the horns.'",
      "T": "'Seven priests are to carry seven rams'-horn trumpets ahead of the ark. On the seventh day march around the city seven times, with the priests sounding the trumpets throughout.'"
    },
    "5": {
      "L": "'And when they make a long blast with the rams' horn, and when you hear the sound of the trumpet, all the people shall shout with a great shout, and the wall of the city shall fall down flat, and the people shall go up, every man straight before him.'",
      "M": "'When you hear the priests sound a long blast on the rams' horns, have the whole army give a loud shout. The wall of the city will collapse, and the people will go up into the city, every man straight in.'",
      "T": "'When the ram's horn gives a long final blast and you hear it, let the whole army shout — a full battle cry. The wall of the city will crumble, and every man will charge straight in.'"
    },
    "6": {
      "L": "So Joshua the son of Nun called the priests and said to them, 'Take up the ark of the covenant, and let seven priests bear seven trumpets of rams' horns before the ark of the LORD.'",
      "M": "So Joshua son of Nun summoned the priests and said to them, 'Lift up the ark of the covenant, and have seven priests carry seven rams' horns in front of the ark of the LORD.'",
      "T": "Joshua son of Nun called for the priests and gave them their orders: 'Lift the ark of the covenant. Let seven priests carry seven rams'-horn trumpets ahead of the LORD's ark.'"
    },
    "7": {
      "L": "And he said to the people, 'Go forward! March around the city, and let the armed force go before the ark of the LORD.'",
      "M": "And he told the army, 'Advance! March around the city, with the armed guard going ahead of the ark of the LORD.'",
      "T": "Then he told the troops: 'Forward! March around the city. The armed vanguard goes ahead of the LORD's ark.'"
    },
    "8": {
      "L": "And it came to pass when Joshua had spoken to the people, that the seven priests bearing seven trumpets of rams' horns before the LORD passed on and blew the trumpets, and the ark of the covenant of the LORD followed them.",
      "M": "When Joshua finished speaking, the seven priests carrying the seven rams' horns marched before the LORD and blew their trumpets, and the ark of the covenant of the LORD followed behind them.",
      "T": "As Joshua gave the word, the seven priests moved forward before the LORD, blowing their seven rams'-horn trumpets, and the ark of the LORD's covenant followed after them."
    },
    "9": {
      "L": "And the armed men went before the priests who blew the trumpets, and the rear guard came after the ark, while the trumpets blew continually.",
      "M": "The armed guard marched ahead of the priests who blew the trumpets, and the rear guard followed the ark, all while the trumpets sounded continuously.",
      "T": "The armed vanguard led the way before the priests blowing the trumpets; the rear guard came after the ark — and the trumpets sounded without stopping."
    },
    "10": {
      "L": "But Joshua commanded the people, 'You shall not shout or make any noise with your voice, nor shall any word proceed out of your mouth, until the day I bid you shout. Then you shall shout.'",
      "M": "But Joshua had commanded the army, 'Do not give a war cry, do not raise your voices, do not say a word until the day I tell you to shout. Then shout!'",
      "T": "Joshua had given this command to the troops: 'No shouting, no noise, not a single word — until I tell you to shout. When I give the command, then shout.'"
    },
    "11": {
      "L": "So he had the ark of the LORD carried around the city, going about it once. And they came into the camp and lodged in the camp.",
      "M": "So Joshua had the ark of the LORD carried around the city, circling it once. Then they returned to camp and spent the night there.",
      "T": "So the ark of the LORD was carried around the city once. Then they returned to camp and spent the night."
    },
    "12": {
      "L": "And Joshua rose early in the morning, and the priests took up the ark of the LORD.",
      "M": "Joshua got up early the next morning and the priests took up the ark of the LORD.",
      "T": "Early the next morning Joshua was up, and the priests lifted the ark of the LORD."
    },
    "13": {
      "L": "And seven priests bearing seven trumpets of rams' horns before the ark of the LORD went on continually and blew the trumpets. And the armed men went before them, and the rear guard came after the ark of the LORD, while the trumpets blew continually.",
      "M": "The seven priests carrying the seven rams' horns marched before the ark of the LORD, continually blowing the horns. The armed guard went ahead of them, and the rear guard followed the ark, while the horns kept sounding.",
      "T": "The seven priests with their seven rams'-horn trumpets marched before the LORD's ark, blowing steadily all the way. The armed troops went ahead; the rear guard followed the ark — and the trumpets never stopped."
    },
    "14": {
      "L": "And on the second day they marched around the city once and returned to the camp. They did this for six days.",
      "M": "On the second day they marched around the city once and returned to camp. They did this for six days.",
      "T": "On the second day they circled the city once and returned to camp. This was the pattern for six days."
    },
    "15": {
      "L": "And it came to pass on the seventh day that they rose early about the dawning of the day and marched around the city seven times in the same manner. It was only on that day that they marched around the city seven times.",
      "M": "On the seventh day they got up at daybreak and marched around the city seven times in the same way — on that day alone they went around the city seven times.",
      "T": "On the seventh day they rose at first light and circled the city seven times in the same way. Only on this day did they circle it seven times."
    },
    "16": {
      "L": "And at the seventh time, when the priests had blown the trumpets, Joshua said to the people, 'Shout! For the LORD has given you the city.'",
      "M": "At the seventh circuit, when the priests sounded the trumpet blast, Joshua commanded the army, 'Shout! The LORD has given you the city!'",
      "T": "At the seventh circuit, as the priests gave the final trumpet blast, Joshua cried out to the army: 'Shout! The LORD has given you this city!'"
    },
    "17": {
      "L": "'The city and all that is in it shall be devoted to the LORD for destruction. Only Rahab the prostitute and all who are with her in her house shall live, because she hid the messengers we sent.'",
      "M": "'The city and everything in it are to be devoted to the LORD for destruction. Only Rahab the prostitute and all who are with her in her house are to be spared, because she hid our spies.'",
      "T": "'The city and all it contains are given over to the LORD — placed under the sacred ban of destruction. Only Rahab the prostitute is to live, and everyone in her house with her, because she hid the men we sent.'"
    },
    "18": {
      "L": "'But as for you, keep yourselves from the devoted things, lest when you have devoted them you take of them and make the camp of Israel a thing for destruction and bring trouble on it.'",
      "M": "'But keep away from the things set apart for destruction, or you will bring destruction on the camp of Israel and cause it trouble. Take none of it for yourselves.'",
      "T": "'Stay away from everything under the ban — not a single item. If you take anything devoted to destruction, you will bring that same destruction down on the camp of Israel and plunge it into disaster.'"
    },
    "19": {
      "L": "'But all the silver and gold and vessels of bronze and iron are holy to the LORD. They shall come into the treasury of the LORD.'",
      "M": "'All the silver and gold and the articles of bronze and iron are sacred to the LORD and must go into his treasury.'",
      "T": "'All the silver, gold, bronze, and iron belong to the LORD — they are holy to him and must go into his treasury.'"
    },
    "20": {
      "L": "So the people shouted when the priests blew the trumpets. And it came to pass when the people heard the sound of the trumpet, that the people shouted with a great shout, and the wall fell down flat, so that the people went up into the city, every man straight before him, and they captured the city.",
      "M": "When the priests sounded the trumpet blast, the people shouted with a great shout, and the wall collapsed. The army charged straight in, and they took the city.",
      "T": "The priests sounded the trumpets, the people gave a great battle cry — and the wall crumbled to the ground. Every soldier charged straight in and they seized the city."
    },
    "21": {
      "L": "Then they devoted all in the city to destruction, both men and women, young and old, oxen, sheep, and donkeys, with the edge of the sword.",
      "M": "They devoted the city to the LORD — they destroyed with the sword every living thing in it: men and women, young and old, cattle, sheep, and donkeys.",
      "T": "They carried out the sacred ban against everything in the city — men and women, young and old, cattle, sheep, and donkeys — all put to the sword."
    },
    "22": {
      "L": "But Joshua said to the two men who had spied out the land, 'Go into the house of the prostitute and bring out from there the woman and all that belong to her, as you swore to her.'",
      "M": "Joshua said to the two men who had spied out the land, 'Go into the house of the prostitute and bring out the woman and everyone who belongs to her, as you swore to her.'",
      "T": "Joshua told the two men who had scouted the land: 'Go to the house of the prostitute and bring out the woman and everyone with her, just as you swore to her.'"
    },
    "23": {
      "L": "So the young men who had been spies went in and brought out Rahab and her father and her mother and her brothers and all that she had, and they brought out all her relatives and left them outside the camp of Israel.",
      "M": "So the young men who had served as spies went in and brought out Rahab, her father, mother, brothers, and all who belonged to her. They brought out the whole family and put them in a place outside the camp of Israel.",
      "T": "The young men who had served as spies went in and brought out Rahab, her father, her mother, her brothers, and all who were hers — her entire household. They placed them safely outside the camp of Israel."
    },
    "24": {
      "L": "And they burned the city with fire and everything in it. Only the silver and the gold and the vessels of bronze and of iron they put into the treasury of the house of the LORD.",
      "M": "Then they burned the whole city and everything in it, but they put the silver, gold, and the articles of bronze and iron into the treasury of the LORD's house.",
      "T": "They burned the city to the ground with everything in it. The silver, gold, bronze, and iron they brought to the treasury of the LORD's house."
    },
    "25": {
      "L": "But Rahab the prostitute and her father's household and all that she had, Joshua saved alive. And she has lived in Israel to this day, because she hid the messengers whom Joshua sent to spy out Jericho.",
      "M": "But Joshua spared Rahab the prostitute, her father's household, and all who belonged to her, because she had hidden the spies Joshua had sent to scout Jericho. She has lived among the Israelites to this day.",
      "T": "Rahab the prostitute, her father's household, and all who belonged to her — Joshua spared them all. She lived among the Israelites from that day forward, because she had hidden the messengers Joshua sent to spy out Jericho."
    },
    "26": {
      "L": "Joshua pronounced this oath at that time, saying, 'Cursed before the LORD be the man who rises up and rebuilds this city Jericho. At the cost of his firstborn son shall he lay its foundation, and at the cost of his youngest son shall he set up its gates.'",
      "M": "At that time Joshua pronounced this solemn oath: 'Cursed before the LORD is the man who undertakes to rebuild this city Jericho. At the cost of his firstborn son he will lay its foundations; at the cost of his youngest son he will set up its gates.'",
      "T": "Joshua then placed this solemn curse on the city: 'Let the man who rebuilds this city Jericho be cursed before the LORD. He will lay its first stone at the cost of his firstborn son, and set up its gates at the cost of his youngest.'"
    },
    "27": {
      "L": "So the LORD was with Joshua, and his fame was in all the land.",
      "M": "So the LORD was with Joshua, and his fame spread throughout the land.",
      "T": "The LORD was with Joshua, and his name became known across the whole land."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'joshua')
        merge_tier(existing, JOSHUA, tier_key)
        save(tier_dir, 'joshua', existing)
    print('Joshua 1–6 written.')

if __name__ == '__main__':
    main()
