"""
MKT Joshua chapters 7–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-joshua-7-12.py

Covers: The sin of Achan and its consequences (ch. 7); the conquest of Ai with the
ambush strategy and altar on Mount Ebal (ch. 8); the Gibeonite deception and treaty
(ch. 9); the southern campaign including the sun standing still and the five-king
coalition (ch. 10); the northern campaign and defeat of Hazor (ch. 11); the summary
list of 31 kings defeated under Moses and Joshua (ch. 12).

Translation decisions (continuing conventions from mkt-joshua-1-6.py):
- H3068 (יהוה): "LORD" (small caps) L/M; "the LORD" T — consistent with all prior OT scripts
- H430 (אֱלֹהִים): "God" all tiers
- H2617 (חֶסֶד): not prominent in chs 7-12; when it appears, "kindness" L / "faithful
  kindness" M / "steadfast loyal love" T — per ch. 1-6 convention
- H1285 (בְּרִית): "covenant" all tiers
- H2764 / H2763 (חֵרֶם / חָרַם): "devoted thing / devote to destruction" L;
  "devoted to destruction" M; "sacred ban / herem" T — carried forward from ch. 6;
  the concept is holy-war dedication to God, not mere slaughter; T surfaces the
  theological frame while not softening the severity
- H5315 (נֶפֶשׁ): "soul/soul" L; "lives/person" M; "lives/whole selves" T — context
  here is physical persons, not theological soul; translated as "person" in the king-list
  formula "all the souls therein"
- H8451 (תּוֹרָה): "the Book of the Law" L/M; "the Torah" / "the Book of the Torah" T —
  in 8:31-35 the entire Mosaic corpus is in view; T uses "Torah" to signal scope
- H7307 (רוּחַ): not prominent in these chapters
- H2388 + H553 (חָזַק + אָמַץ) in 10:25: "be strong and courageous" all tiers —
  identical to the command in 1:6,7,9; T frames it as assurance flowing from victory
- H2572 (חֲמִשִּׁים): "fifty shekels" weight of Achan's gold — preserved in L/M/T
- H8049 (Achan / עָכָן): name is preserved as proper noun; etymological play with
  H6117 (עָכַר = "trouble/trouble") surfaces in 7:25-26; "Valley of Achor" (H5911)
  means "Valley of Trouble" — T makes this explicit with the parenthetical "Trouble"
- H1553 (Babylonish garment): "goodly Babylonish garment" L; "beautiful Babylonian
  cloak" M; "fine cloak from Babylon" T — the Shinar/Babylon reference marks it as
  forbidden foreign luxury; the desire for it is the genesis of the sin
- Joshua's spear (8:18-26) echoes Moses' staff at Rephidim (Exod 17:8-13) — the
  signal posture connecting leader, divine promise, and battlefield outcome; T notes
  this intertextual echo
- The sun standing still (10:12-13): the citation is from the Book of Jashar (also
  cited in 2 Sam 1:18); Hebrew וַיִּדֹּם (wayyiddom) = "was silent/stood still";
  the phenomenon is the day lengthened so Israel could finish the battle; T preserves
  the poetic register of the cited speech without harmonising it
- Gibeon treaty (ch. 9): Israel "did not ask counsel from the LORD" (9:14) — a key
  theological note; the treaty oath is binding even though obtained by deception;
  the text presents this without resolving the tension; T surfaces the theological
  weight of the binding oath
- H6430 (Philistines) in 11:22: the Anakites left in Gaza/Gath/Ashdod foreshadow
  Goliath and the Philistine giants (cf. 2 Sam 21:15-22); T notes this connection
- H7497 (רְפָאִים / Rephaim) in 12:4: "remnant of the Rephaim" — the ancient giant
  peoples; preserved as Rephaim in all tiers; L uses "remnant of the Rephaim" as
  the interlinear literally presents it
- Ch. 12 king-list format: the formulaic "one" after each king is preserved verbatim
  in L; M uses em-dash format for readability; T uses comma-list for flow while
  retaining the liturgical repetition; the list runs to 31 kings total
- Herem in ch. 7: Achan's violation brings collective liability — this reflects
  the Israelite covenantal solidarity model; one man's sin pollutes the whole camp;
  T surfaces this rather than softening it
- OT intertextuality: 8:30-35 altar on Ebal implements Deut 27:2-8 verbatim;
  T draws the explicit connection
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
  "7": {
    "1": {
      "L": "But the children of Israel committed a trespass regarding the devoted thing, for Achan the son of Carmi, the son of Zabdi, the son of Zerah, of the tribe of Judah, took of the devoted thing. And the anger of the LORD was kindled against the children of Israel.",
      "M": "But the Israelites were unfaithful regarding the devoted things, for Achan son of Carmi, son of Zabdi, son of Zerah, of the tribe of Judah, had taken some of them. So the LORD's anger burned against Israel.",
      "T": "But Israel broke faith over the sacred ban: Achan son of Carmi, son of Zabdi, son of Zerah, of the tribe of Judah, had taken items devoted to destruction. The LORD's anger blazed against Israel."
    },
    "2": {
      "L": "And Joshua sent men from Jericho to Ai, which is beside Beth-aven, on the east side of Bethel, and said to them, 'Go up and view the country.' And the men went up and spied out Ai.",
      "M": "Joshua sent men from Jericho to Ai, which is near Beth-aven to the east of Bethel, with orders: 'Go and spy out the region.' So the men went and scouted Ai.",
      "T": "Joshua sent scouts from Jericho to Ai — the town near Beth-aven, east of Bethel — with orders: 'Go, scout the territory.' The men went and reconnoitered Ai."
    },
    "3": {
      "L": "And they returned to Joshua and said to him, 'Let not all the people go up, but let about two or three thousand men go up and attack Ai. Do not make all the people toil thither, for they are but few.'",
      "M": "When they returned, they told Joshua, 'Not all the army needs to go. Send two or three thousand men to take Ai — don't wear out the whole force, for the people of Ai are few.'",
      "T": "'Not everyone needs to march,' they reported back to Joshua. 'Send two or three thousand — Ai is small. There's no need to exhaust the whole army.'"
    },
    "4": {
      "L": "So about three thousand men went up from the people, and they fled before the men of Ai.",
      "M": "About three thousand men went up, but they were routed by the men of Ai.",
      "T": "About three thousand soldiers went up — and they broke and ran before Ai's men."
    },
    "5": {
      "L": "And the men of Ai struck down about thirty-six of them and chased them from before the gate as far as Shebarim and smote them on the descent. And the hearts of the people melted and became as water.",
      "M": "The men of Ai killed about thirty-six of them and chased them from the city gate down to Shebarim, cutting them down on the slopes. At this the courage of the people melted away.",
      "T": "Ai's defenders cut down about thirty-six Israelites, chasing them from the gate all the way to Shebarim, cutting them down on the descent. The hearts of the people dissolved like water."
    },
    "6": {
      "L": "And Joshua rent his clothes and fell to the earth upon his face before the ark of the LORD until the evening, he and the elders of Israel, and they put dust upon their heads.",
      "M": "Joshua tore his clothes and fell facedown before the ark of the LORD until evening — he and the elders of Israel — putting dust on their heads.",
      "T": "Joshua tore his garments and fell face to the ground before the ark of the LORD and lay there until evening — he and the elders of Israel, with dust heaped on their heads."
    },
    "7": {
      "L": "And Joshua said, 'Alas, O Lord GOD, why hast thou at all brought this people over the Jordan, to deliver us into the hand of the Amorites to destroy us? Would to God we had been content to dwell on the other side of the Jordan!'",
      "M": "Joshua said, 'Alas, Sovereign LORD, why did you ever bring this people across the Jordan? To hand us over to the Amorites and destroy us? If only we had been content to stay on the other side!'",
      "T": "'O Lord GOD — why did you ever lead this people across the Jordan? To hand us over to the Amorites and wipe us out? We should have settled on the other side and never crossed!'"
    },
    "8": {
      "L": "O Lord, what shall I say when Israel has turned their backs before their enemies?",
      "M": "Sovereign LORD, what can I say now that Israel has fled before her enemies?",
      "T": "'What can I say, Lord, when Israel turns its back and runs from its enemies?'"
    },
    "9": {
      "L": "For the Canaanites and all the inhabitants of the land shall hear of it and shall surround us and cut off our name from the earth. And what wilt thou do for thy great name?",
      "M": "When the Canaanites and all the peoples of the land hear of this, they will encircle us and wipe out our name from the earth. And what will you do for your great name?",
      "T": "'The Canaanites and every people in the land will hear of this and close in around us, wiping our name from the earth. And then what becomes of your great name?'"
    },
    "10": {
      "L": "And the LORD said to Joshua, 'Rise up! Wherefore have you fallen upon your face?'",
      "M": "The LORD said to Joshua, 'Stand up! What are you doing down on your face?'",
      "T": "The LORD said to Joshua: 'Get up! Why are you lying face-down like this?'"
    },
    "11": {
      "L": "Israel has sinned and has also transgressed my covenant which I commanded them. For they have even taken of the devoted thing and have also stolen and dissembled, and have put it even among their own stuff.",
      "M": "Israel has sinned; they have violated my covenant that I commanded them. They took some of the devoted things; they stole, they deceived, and they hid it among their own belongings.",
      "T": "'Israel has sinned. They have broken the covenant I commanded — they took from the sacred ban, they stole, they lied, and they buried the plunder among their own things.'"
    },
    "12": {
      "L": "Therefore the children of Israel cannot stand before their enemies; they turn their backs before their enemies, because they have become a devoted thing. I will be with you no more unless you destroy the devoted thing from among you.",
      "M": "That is why the Israelites cannot stand against their enemies — they flee because they themselves have become liable to the ban. I will not be with you any longer unless you destroy what is under the ban from among you.",
      "T": "'That is why Israel cannot face its enemies — it turns and flees, because the camp itself has fallen under the curse of the sacred ban. I will not be with you anymore until you remove that banned thing from your midst.'"
    },
    "13": {
      "L": "Rise up, sanctify the people, and say, 'Sanctify yourselves for tomorrow, for thus says the LORD God of Israel: There is a devoted thing in your midst, O Israel. You cannot stand before your enemies until you take away the devoted thing from among you.'",
      "M": "'Get up and consecrate the people. Say to them: Consecrate yourselves for tomorrow, for this is what the LORD, the God of Israel, says: There are devoted things among you, Israel. You cannot stand against your enemies until you remove them.'",
      "T": "'Rise up. Consecrate the people. Tell them: Prepare yourselves for tomorrow — for the LORD God of Israel says: There is a banned thing in your midst, Israel. You cannot stand before your enemies until you rid yourselves of it.'"
    },
    "14": {
      "L": "In the morning therefore you shall be brought near by your tribes, and it shall be that the tribe which the LORD takes shall come near by families, and the family which the LORD takes shall come near by households, and the household which the LORD takes shall come near man by man.",
      "M": "In the morning you will be presented tribe by tribe. The tribe the LORD identifies will come forward clan by clan; the clan the LORD identifies will come forward household by household; and the household the LORD identifies will come forward man by man.",
      "T": "In the morning you will present yourselves tribe by tribe. The tribe the LORD selects comes forward clan by clan; the clan selected comes forward household by household; the household selected comes forward man by man."
    },
    "15": {
      "L": "And it shall be that he who is taken with the devoted thing shall be burned with fire, he and all that he has, because he has transgressed the covenant of the LORD and because he has done folly in Israel.",
      "M": "Whoever is caught with the devoted things will be burned along with everything he owns, because he violated the LORD's covenant and did a disgraceful thing in Israel.",
      "T": "'Whoever is found holding the banned goods will be burned — he and all he owns — because he violated the LORD's covenant and committed an outrage against Israel.'"
    },
    "16": {
      "L": "So Joshua rose early in the morning and brought Israel near by their tribes, and the tribe of Judah was taken.",
      "M": "Early the next morning Joshua had Israel come forward tribe by tribe, and the tribe of Judah was identified.",
      "T": "Early the next morning Joshua brought all Israel forward tribe by tribe, and the tribe of Judah was singled out."
    },
    "17": {
      "L": "And he brought near the family of Judah and took the family of the Zarhites. And he brought near the family of the Zarhites man by man, and Zabdi was taken.",
      "M": "He brought the clans of Judah forward, and the clan of Zerah was identified. He brought the Zerahite clan forward man by man, and Zabdi was identified.",
      "T": "The clans of Judah came forward, and the Zerahites were singled out. The Zerahites came forward man by man, and Zabdi was singled out."
    },
    "18": {
      "L": "And he brought near his household man by man, and Achan the son of Carmi, the son of Zabdi, the son of Zerah, of the tribe of Judah, was taken.",
      "M": "He brought Zabdi's household forward man by man, and Achan son of Carmi, son of Zabdi, son of Zerah, of the tribe of Judah, was identified.",
      "T": "Zabdi's household came forward man by man — and Achan son of Carmi, son of Zabdi, son of Zerah, of the tribe of Judah, was singled out."
    },
    "19": {
      "L": "And Joshua said to Achan, 'My son, give glory to the LORD God of Israel and give praise to him. Tell me now what you have done; do not hide it from me.'",
      "M": "Joshua said to Achan, 'My son, give glory to the LORD, the God of Israel, and honor him. Tell me what you have done; do not hide it from me.'",
      "T": "Joshua said to Achan: 'My son, give glory and honor to the LORD, the God of Israel. Tell me truthfully what you have done — hide nothing from me.'"
    },
    "20": {
      "L": "And Achan answered Joshua and said, 'Indeed I have sinned against the LORD God of Israel, and thus and thus have I done.'",
      "M": "Achan answered Joshua, 'It is true — I have sinned against the LORD, the God of Israel. This is what I did.'",
      "T": "Achan answered Joshua: 'Yes, it is true. I sinned against the LORD God of Israel. And this is what I did.'"
    },
    "21": {
      "L": "When I saw among the spoils a goodly Babylonish garment and two hundred shekels of silver and a wedge of gold weighing fifty shekels, I coveted them and took them. Behold, they are hid in the earth in the midst of my tent, and the silver under it.",
      "M": "When I saw among the plunder a beautiful Babylonian cloak, two hundred shekels of silver, and a gold bar weighing fifty shekels, I wanted them and took them. They are hidden in the ground inside my tent, with the silver underneath.",
      "T": "'I spotted a fine cloak from Babylon among the plunder — and two hundred shekels of silver and a fifty-shekel gold bar. I wanted them. I took them. They are buried in the ground inside my tent, with the silver at the bottom.'"
    },
    "22": {
      "L": "So Joshua sent messengers and they ran to the tent, and behold, it was hid in his tent with the silver under it.",
      "M": "Joshua sent men, who ran to the tent, and there it was — hidden in his tent, with the silver underneath.",
      "T": "Joshua sent men running to the tent. There it was — buried in Achan's tent, with the silver underneath, exactly as he had said."
    },
    "23": {
      "L": "And they took them from the midst of the tent and brought them to Joshua and to all the children of Israel and laid them out before the LORD.",
      "M": "They took the things from the tent, brought them to Joshua and all the Israelites, and spread them out before the LORD.",
      "T": "They took the stolen goods from inside the tent and brought them to Joshua and all Israel and laid them out before the LORD."
    },
    "24": {
      "L": "Then Joshua and all Israel with him took Achan the son of Zerah, and the silver and the garment and the wedge of gold, and his sons and his daughters and his oxen and his donkeys and his sheep and his tent and all that he had, and they brought them up to the Valley of Achor.",
      "M": "Then Joshua and all Israel took Achan son of Zerah, along with the silver, the cloak, and the gold bar, his sons and daughters, his cattle, donkeys, and sheep, his tent and everything he owned, and brought them to the Valley of Achor.",
      "T": "Joshua and all Israel seized Achan son of Zerah — along with the silver, the cloak, the gold bar, his sons and daughters, his cattle, donkeys, and sheep, his tent and every possession — and brought them all to the Valley of Achor."
    },
    "25": {
      "L": "And Joshua said, 'Why have you troubled us? The LORD will trouble you this day.' And all Israel stoned him with stones, and they burned them with fire and stoned them with stones after.",
      "M": "Joshua said, 'Why have you brought this trouble on us? The LORD will bring trouble on you today.' Then all Israel stoned Achan to death, and after stoning them they burned everything.",
      "T": "Joshua said: 'Why have you brought disaster on us? The LORD will bring disaster on you this very day.' All Israel stoned Achan to death, and afterward they were burned with fire."
    },
    "26": {
      "L": "And they raised over him a great heap of stones which remains to this day. And the LORD turned from the fierceness of his anger. Therefore the name of that place is called the Valley of Achor to this day.",
      "M": "Over Achan they piled a great heap of stones that is still there today. Then the LORD turned from his fierce anger. That is why the place has been called the Valley of Achor to this day.",
      "T": "They heaped a great pile of stones over him, and it stands to this day. Then the LORD's blazing anger subsided. And so that place was named the Valley of Achor — 'Trouble' — a name it carries to this day."
    }
  },
  "8": {
    "1": {
      "L": "And the LORD said to Joshua, 'Fear not, neither be dismayed. Take all the people of war with you and arise, go up to Ai. See, I have given into your hand the king of Ai and his people and his city and his land.'",
      "M": "Then the LORD said to Joshua, 'Do not be afraid or discouraged. Take the whole army with you and go up to Ai. I have given the king of Ai, his people, city, and land into your hands.'",
      "T": "The LORD said to Joshua: 'Do not be afraid; do not be disheartened. Take the whole fighting force and go up to Ai. I am handing over to you its king, its people, its city, and its land.'"
    },
    "2": {
      "L": "And you shall do to Ai and its king as you did to Jericho and its king. Only its spoil and its cattle shall you take for a prey to yourselves. Lay an ambush for the city, behind it.",
      "M": "Do to Ai and its king what you did to Jericho and its king. You may carry off their plunder and livestock for yourselves. Set an ambush behind the city.",
      "T": "'Deal with Ai and its king the same way you dealt with Jericho and its king — but this time, take the livestock and goods for yourselves. Set an ambush behind the city.'"
    },
    "3": {
      "L": "So Joshua and all the people of war arose to go up against Ai. And Joshua chose thirty thousand men, mighty men of valor, and sent them out by night.",
      "M": "So Joshua and the whole army set out to go up against Ai. Joshua chose thirty thousand capable warriors and sent them out under cover of night.",
      "T": "Joshua and the whole army prepared to advance against Ai. Joshua selected thirty thousand of his best warriors and dispatched them under cover of darkness."
    },
    "4": {
      "L": "And he commanded them, 'Behold, you shall lie in ambush against the city, behind the city. Go not very far from the city, but all of you be ready.'",
      "M": "He instructed them, 'Listen — you are to lie in ambush behind the city. Don't go too far from it; all of you be on alert.'",
      "T": "'Here are your orders,' he said. 'You will take position in ambush behind the city. Stay close — do not go far — and keep every man ready.'"
    },
    "5": {
      "L": "'And I and all the people who are with me will approach the city. And when they come out against us as at the first, we shall flee before them.'",
      "M": "'I and all the troops with me will advance on the city. When they come out to attack us as they did before, we will flee from them.'",
      "T": "'I will approach the city with all my troops. When they come out to meet us the same as last time, we will turn and run.'"
    },
    "6": {
      "L": "'For they will come out after us until we have drawn them away from the city, for they will say, \"They flee before us as at the first.\" So we shall flee before them.'",
      "M": "'They will pursue us until we have lured them away from the city, for they will say, \"They are running from us just like before.\" We will keep running from them.'",
      "T": "'They will chase us until we have pulled them clear of the city — they will be thinking, \"Israel is running again, just like last time.\" And we will run.'"
    },
    "7": {
      "L": "'Then you shall rise up from the ambush and take the city, for the LORD your God will deliver it into your hand.'",
      "M": "'Then you will rise from your ambush and take the city, for the LORD your God will hand it over to you.'",
      "T": "'Then you spring from ambush and take the city — the LORD your God is handing it to you.'"
    },
    "8": {
      "L": "'And when you have taken the city, you shall set it on fire. According to the word of the LORD shall you do. See, I have commanded you.'",
      "M": "'Once you have seized it, set it on fire. Do this in accordance with the LORD's command. I have now given you your orders.'",
      "T": "'Once it falls, burn it. This is the LORD's command — and I am passing it on to you as your orders.'"
    },
    "9": {
      "L": "So Joshua sent them forth, and they went to the place of ambush and stayed between Bethel and Ai, on the west side of Ai. But Joshua lodged that night among the people.",
      "M": "Joshua sent them off, and they went to their ambush position and waited between Bethel and Ai, west of Ai. Joshua spent that night with the rest of the people.",
      "T": "Joshua sent the ambush force ahead, and they took position between Bethel and Ai, on the west side of Ai, and waited. Joshua himself spent that night with the main camp."
    },
    "10": {
      "L": "And Joshua rose up early in the morning and mustered the people, and he and the elders of Israel went up before the people against Ai.",
      "M": "Joshua rose early the next morning and reviewed the troops, then he and the elders of Israel led the people up to Ai.",
      "T": "At first light Joshua mustered his forces. He and the elders of Israel led the army up toward Ai."
    },
    "11": {
      "L": "And all the people of war who were with him went up and drew near and came before the city and pitched on the north side of Ai. Now there was a valley between them and Ai.",
      "M": "The whole army that was with him advanced and took up position north of Ai, with a valley between them and the city.",
      "T": "The entire fighting force advanced and took up position on the north side of Ai — a valley lay between them and the city."
    },
    "12": {
      "L": "And he took about five thousand men and set them in ambush between Bethel and Ai, on the west side of the city.",
      "M": "He also positioned about five thousand men in ambush between Bethel and Ai, west of the city.",
      "T": "He also placed about five thousand men in ambush between Bethel and Ai on the city's west side."
    },
    "13": {
      "L": "And when they had set the people, even all the army that was on the north of the city, and their ambush on the west of the city, Joshua went that night into the midst of the valley.",
      "M": "After positioning all the troops — the main force north of the city and the ambush west of it — Joshua spent that night in the middle of the valley.",
      "T": "With the main force to the north and the ambush force to the west, Joshua moved into the valley that night."
    },
    "14": {
      "L": "And it came to pass when the king of Ai saw this that he and all his people, the men of the city, hurried and rose early and went out against Israel to battle, at the appointed place before the plain. But he did not know that there was an ambush against him behind the city.",
      "M": "When the king of Ai saw them, he and all his people quickly moved out to engage Israel in battle at the designated place overlooking the plain. He did not know that ambushers were waiting for him behind the city.",
      "T": "The king of Ai saw them. He and all his people rushed out at daybreak to engage Israel on the plain at the regular battle site — not knowing that a force lay hidden behind the city."
    },
    "15": {
      "L": "And Joshua and all Israel made as if they were beaten before them and fled by the way of the wilderness.",
      "M": "Joshua and all Israel pretended to be beaten before them and fled toward the wilderness.",
      "T": "Joshua and all Israel feigned defeat and fled toward the desert."
    },
    "16": {
      "L": "And all the people in Ai were called together to pursue them, and they pursued Joshua and were drawn away from the city.",
      "M": "All the men in Ai were called out to pursue them; they chased Joshua and were lured away from the city.",
      "T": "Every man in Ai was rallied to give chase. They poured out after Joshua, drawn away from the city."
    },
    "17": {
      "L": "And there was not a man left in Ai or Bethel who did not go out after Israel. They left the city open and pursued Israel.",
      "M": "Not a man was left in Ai or Bethel who had not gone out in pursuit of Israel. They left the city gates open and chased after Israel.",
      "T": "Not one man remained in Ai or Bethel — they all poured out in pursuit of Israel, leaving the city gates wide open and unguarded."
    },
    "18": {
      "L": "And the LORD said to Joshua, 'Stretch out the spear that is in your hand toward Ai, for I will give it into your hand.' And Joshua stretched out the spear in his hand toward the city.",
      "M": "The LORD said to Joshua, 'Point the spear in your hand toward Ai, for I will hand it over to you.' Joshua pointed his spear toward the city.",
      "T": "The LORD said to Joshua: 'Aim the spear in your hand at Ai — I am giving it to you.' Joshua raised his spear toward the city."
    },
    "19": {
      "L": "And the ambush arose quickly out of their place and ran into the city as soon as he stretched out his hand, and they entered the city and took it and made haste to set it on fire.",
      "M": "The ambush rose quickly from their position and rushed into the city the moment Joshua extended his hand. They entered Ai, captured it, and immediately set it on fire.",
      "T": "The moment Joshua's hand shot forward, the ambush force sprang from their position and rushed into the city. They seized Ai and immediately put it to the torch."
    },
    "20": {
      "L": "And when the men of Ai turned back and looked, the smoke of the city ascended to heaven. And they had no power to flee this way or that, for the people who fled to the wilderness turned back against the pursuers.",
      "M": "When the men of Ai looked back and saw the smoke from the city rising toward the sky, they could not escape in any direction. The Israelites who had been fleeing toward the wilderness turned around to face the pursuers.",
      "T": "Ai's soldiers turned and looked — smoke from the city was billowing up to heaven. They had nowhere to run. The Israelites who had fled into the desert wheeled around to face them."
    },
    "21": {
      "L": "And when Joshua and all Israel saw that the ambush had taken the city and that the smoke of the city ascended, they turned back and smote the men of Ai.",
      "M": "When Joshua and all Israel saw that the ambush had captured the city and that smoke was rising from it, they turned back and attacked the men of Ai.",
      "T": "When Joshua and all Israel saw the smoke rising — proof the ambush had taken the city — they turned and cut down Ai's men."
    },
    "22": {
      "L": "And the others issued out of the city against them, so that they were in the midst of Israel, some on this side and some on that. And they smote them until none remained or had escaped.",
      "M": "The men who came out of the city were trapped in the middle, with Israelites on both sides. They struck them down until not one of them was left alive to escape.",
      "T": "The men from the city came out to meet them — and now Ai's army was caught in the middle, Israelites on both sides. They were cut down until not a single man survived."
    },
    "23": {
      "L": "And the king of Ai they took alive and brought him to Joshua.",
      "M": "They captured the king of Ai alive and brought him to Joshua.",
      "T": "The king of Ai they captured alive and brought to Joshua."
    },
    "24": {
      "L": "And it came to pass when Israel had made an end of slaying all the inhabitants of Ai in the field, in the wilderness where they chased them, and they were all fallen by the edge of the sword until they were consumed, that all the Israelites returned to Ai and struck it with the edge of the sword.",
      "M": "When Israel had finished killing all the men of Ai in the open field and in the wilderness where they had chased them — when every last one had fallen by the sword — all Israel returned to Ai and put it to the sword.",
      "T": "Once Israel had finished killing all of Ai's men — cut down in the open fields and in the desert where they had fled, every one falling by the sword — all Israel came back to Ai and put it to the sword."
    },
    "25": {
      "L": "So all who fell that day, both men and women, were twelve thousand — all the people of Ai.",
      "M": "The total killed that day — men and women combined — was twelve thousand, the entire population of Ai.",
      "T": "The dead that day — men and women together — numbered twelve thousand. The entire population of Ai was gone."
    },
    "26": {
      "L": "For Joshua did not draw back his hand that he stretched out with the spear until he had devoted all the inhabitants of Ai to destruction.",
      "M": "Joshua kept his spear pointed at Ai until every inhabitant was devoted to destruction.",
      "T": "Joshua held his spear outstretched toward the city — as Moses had held his staff at Rephidim — until every man and woman of Ai had been devoted to destruction."
    },
    "27": {
      "L": "Only the livestock and the spoil of that city Israel took for a prey to themselves, according to the word of the LORD which he commanded Joshua.",
      "M": "Israel kept the livestock and plunder of that city as their share, as the LORD had commanded Joshua.",
      "T": "Israel took only the livestock and the spoil of the city — their lawful share, as the LORD had directed Joshua."
    },
    "28": {
      "L": "And Joshua burned Ai and made it a heap forever, a desolation to this day.",
      "M": "Joshua burned Ai down, reducing it to a permanent ruin — a desolation that stands to this day.",
      "T": "Joshua burned Ai and left it a permanent rubble-heap — a desolation that stands to this day."
    },
    "29": {
      "L": "And the king of Ai he hanged on a tree until evening. And as the sun went down Joshua commanded that they should take his body down from the tree and cast it at the entering of the gate of the city, and raise thereon a great heap of stones, which remains to this day.",
      "M": "He had the king of Ai hanged on a tree until evening. At sunset Joshua ordered them to take the body down from the tree, throw it at the city gate, and pile a large heap of stones over it, which is there to this day.",
      "T": "The king of Ai was hanged on a tree until sunset. At sundown Joshua ordered the body taken down and thrown at the city gate, and a great heap of stones was piled over it — it remains there to this day."
    },
    "30": {
      "L": "Then Joshua built an altar to the LORD God of Israel on Mount Ebal,",
      "M": "Then Joshua built an altar to the LORD, the God of Israel, on Mount Ebal,",
      "T": "Then Joshua built an altar to the LORD God of Israel on Mount Ebal,"
    },
    "31": {
      "L": "as Moses the servant of the LORD had commanded the children of Israel, as it is written in the Book of the Law of Moses, an altar of whole stones, over which no man has wielded any iron tool. And they offered on it burnt offerings to the LORD and sacrificed peace offerings.",
      "M": "in keeping with what Moses the servant of the LORD had commanded Israel, as written in the Book of the Law of Moses — an altar of uncut stones on which no iron tool had been used. They offered burnt offerings to the LORD on it and sacrificed fellowship offerings.",
      "T": "exactly as Moses the LORD's servant had commanded Israel, as prescribed in the Book of the Torah of Moses: an altar of unworked stone, no iron tool touching it. They offered burnt offerings to the LORD and sacrificed peace offerings — fulfilling Deuteronomy 27 at the moment of first settlement."
    },
    "32": {
      "L": "And he wrote there upon the stones a copy of the law of Moses, which he had written, in the presence of the children of Israel.",
      "M": "There Joshua wrote on the stones a copy of the law of Moses, in the presence of the Israelites.",
      "T": "There Joshua inscribed on the stones a full copy of the Torah of Moses — written out in the sight of all Israel."
    },
    "33": {
      "L": "And all Israel, stranger and native alike, with their elders and officers and judges, stood on either side of the ark before the Levitical priests who carried the ark of the covenant of the LORD, half before Mount Gerizim and half before Mount Ebal, as Moses the servant of the LORD had commanded, to bless the people of Israel.",
      "M": "All Israel — resident aliens included — with their elders, officials, and judges, stood on either side of the ark facing the Levitical priests who carried the ark of the covenant of the LORD. Half stood in front of Mount Gerizim and half before Mount Ebal, as Moses the servant of the LORD had commanded, for the blessing of the people.",
      "T": "All Israel — native-born and foreigner alike — stood in two groups with their elders, officers, and judges, facing the Levitical priests who carried the LORD's ark. Half stood before Mount Gerizim, half before Mount Ebal, exactly as Moses the LORD's servant had prescribed for pronouncing blessing over the people."
    },
    "34": {
      "L": "And afterward he read all the words of the law, the blessings and the cursings, according to all that is written in the Book of the Law.",
      "M": "Then Joshua read all the words of the law — the blessings and the curses — according to all that is written in the Book of the Law.",
      "T": "Afterward Joshua read aloud every word of the Torah — the blessings and the curses — everything written in the Book of the Law."
    },
    "35": {
      "L": "There was not a word of all that Moses had commanded which Joshua did not read before all the assembly of Israel, with the women and the little ones and the strangers that were conversant among them.",
      "M": "Joshua read every single word that Moses had commanded — before the whole assembly of Israel: men, women, children, and the foreigners living among them.",
      "T": "Not a single word of all that Moses had commanded was left out — Joshua read it all before the whole assembly of Israel: men, women, children, and the foreigners dwelling in their midst."
    }
  },
  "9": {
    "1": {
      "L": "And it came to pass when all the kings who were beyond the Jordan, in the hills and in the lowland and on all the coast of the Great Sea toward Lebanon, the Hittite and the Amorite and the Canaanite and the Perizzite and the Hivite and the Jebusite, heard of these things,",
      "M": "When all the kings west of the Jordan — in the hill country, the western foothills, and along the entire Mediterranean coast as far as Lebanon — heard about these events, the Hittites, Amorites, Canaanites, Perizzites, Hivites, and Jebusites",
      "T": "When the news spread to all the kings west of the Jordan — in the highlands, the foothills, and along the entire Mediterranean coast up to Lebanon — all the Hittites, Amorites, Canaanites, Perizzites, Hivites, and Jebusites"
    },
    "2": {
      "L": "they gathered themselves together with one accord to fight against Joshua and Israel.",
      "M": "joined forces with one purpose: to fight against Joshua and Israel.",
      "T": "joined forces with one purpose: to make war on Joshua and Israel."
    },
    "3": {
      "L": "But the inhabitants of Gibeon heard what Joshua had done to Jericho and to Ai,",
      "M": "But the people of Gibeon heard what Joshua had done to Jericho and Ai.",
      "T": "The people of Gibeon took a different course. They heard what Joshua had done to Jericho and Ai,"
    },
    "4": {
      "L": "and they worked craftily and went and made as if they had been ambassadors and took worn-out sacks on their donkeys and worn-out wineskins that were rent and bound up,",
      "M": "and acted with cunning — they set out disguised as envoys, loading their donkeys with worn-out sacks and cracked, patched wineskins.",
      "T": "and came up with a scheme. They disguised themselves as distant ambassadors, loading worn-out sacks on their donkeys and taking cracked, patched wineskins,"
    },
    "5": {
      "L": "and old and clouted shoes upon their feet, and old garments on themselves, and all the bread of their provision was dry and mouldy.",
      "M": "They wore patched, worn-out sandals and old clothing, and all their bread was dry and crumbly.",
      "T": "wearing patched, worn-out sandals and threadbare clothing, with bread that was dry and moldy."
    },
    "6": {
      "L": "And they went to Joshua at the camp at Gilgal and said to him and to the men of Israel, 'We have come from a far country. Now therefore make a covenant with us.'",
      "M": "They went to Joshua at the camp at Gilgal and said to him and the Israelites, 'We have come from a distant country; make a treaty with us.'",
      "T": "They came to Joshua at the camp at Gilgal and said to him and to the men of Israel: 'We have come from a very distant land. Make a treaty with us.'"
    },
    "7": {
      "L": "And the men of Israel said to the Hivites, 'Perhaps you dwell among us. How shall we then make a covenant with you?'",
      "M": "The Israelites said to the Hivites, 'But what if you live near us? How could we make a treaty with you?'",
      "T": "The Israelites said to the Hivites: 'What if you actually live right among us? Then we could make no treaty with you.'"
    },
    "8": {
      "L": "And they said to Joshua, 'We are your servants.' And Joshua said to them, 'Who are you and from where do you come?'",
      "M": "They said to Joshua, 'We are your servants.' Joshua asked them, 'Who are you, and where do you come from?'",
      "T": "'We are your servants,' they said. Joshua asked them: 'Who are you? Where do you come from?'"
    },
    "9": {
      "L": "And they said to him, 'From a very far country your servants have come because of the name of the LORD your God. For we have heard the fame of him and all that he did in Egypt,'",
      "M": "They answered, 'Your servants have come from a very distant country because of the reputation of the LORD your God. We heard the report about him and everything he did in Egypt,'",
      "T": "'Your servants have come from a very distant land, drawn by the fame of the LORD your God. We heard the report of his name and everything he did in Egypt,'"
    },
    "10": {
      "L": "and all that he did to the two kings of the Amorites who were beyond the Jordan, Sihon king of Heshbon and Og king of Bashan who was at Ashtaroth.",
      "M": "and what he did to the two Amorite kings east of the Jordan — Sihon king of Heshbon and Og king of Bashan, who ruled from Ashtaroth.",
      "T": "'and what he did to the two Amorite kings beyond the Jordan — Sihon of Heshbon and Og of Bashan at Ashtaroth.'"
    },
    "11": {
      "L": "And our elders and all the inhabitants of our country spoke to us, saying, 'Take provisions in your hand for the journey and go to meet them and say to them, \"We are your servants. Now therefore make a covenant with us.\"'",
      "M": "Our elders and all who live in our country said to us, 'Take provisions for the journey, go to meet them and say, \"We are your servants; please make a treaty with us.\"'",
      "T": "'So our elders and all our people sent us with this charge: \"Take provisions for the journey, go meet them, and say: We are your servants — make a treaty with us.\"'"
    },
    "12": {
      "L": "'This our bread we took hot out of our houses on the day we set out to go to you. But now, behold, it is dry and crumbly.'",
      "M": "'Look at our bread — it was fresh from our ovens when we left home to come to you. But now, see, it is dry and crumbled.'",
      "T": "'Look at this bread — it was still warm from the oven when we left home to come to you. Look at it now: dry and crumbled.'"
    },
    "13": {
      "L": "'And these wineskins that we filled were new when we filled them, and behold they are torn. And these our garments and our sandals have worn out because of the very long journey.'",
      "M": "'These wineskins were brand new when we filled them, but look — they are cracked. And our clothes and sandals are worn out from the extremely long journey.'",
      "T": "'These wineskins were new when we filled them — look at them now, cracked and burst. Our clothing and sandals are worn through from the sheer length of the journey.'"
    },
    "14": {
      "L": "And the men of Israel took of their provisions and did not ask counsel from the LORD.",
      "M": "The Israelites sampled their provisions but did not consult the LORD.",
      "T": "The men of Israel tasted their provisions — and did not seek the LORD's word."
    },
    "15": {
      "L": "And Joshua made peace with them and made a covenant with them to let them live. And the leaders of the congregation swore an oath to them.",
      "M": "Joshua made a peace treaty with them and agreed to let them live, and the leaders of the assembly confirmed it with an oath.",
      "T": "Joshua made peace with them and concluded a treaty — he would let them live — and the leaders of the assembly swore an oath to them. The oath was binding."
    },
    "16": {
      "L": "And it came to pass at the end of three days after they had made a covenant with them that they heard that they were their neighbors and that they dwelt among them.",
      "M": "Three days after the treaty was made, the Israelites heard that these people lived nearby and were their neighbors.",
      "T": "Three days after the treaty was sealed, the Israelites learned that these men were their neighbors — they lived right in the same region."
    },
    "17": {
      "L": "And the children of Israel journeyed and came unto their cities on the third day. Now their cities were Gibeon and Chephirah and Beeroth and Kirjathjearim.",
      "M": "The Israelites marched out and arrived at their cities on the third day — Gibeon, Chephirah, Beeroth, and Kiriath-jearim.",
      "T": "The Israelites marched and reached these cities on the third day: Gibeon, Chephirah, Beeroth, and Kiriath-jearim."
    },
    "18": {
      "L": "And the children of Israel smote them not because the leaders of the congregation had sworn to them by the LORD God of Israel. And all the congregation murmured against the leaders.",
      "M": "But the Israelites did not attack them, because the leaders of the assembly had sworn a binding oath to them in the name of the LORD, the God of Israel. And the whole assembly grumbled against the leaders.",
      "T": "But Israel held back its sword, because the assembly's leaders had sworn an oath by the LORD God of Israel — the oath was binding even though obtained by deception. The whole community erupted in complaint against the leaders."
    },
    "19": {
      "L": "But all the leaders said to all the congregation, 'We have sworn to them by the LORD God of Israel, and now we cannot touch them.'",
      "M": "But all the leaders told the whole assembly, 'We have given them our oath in the name of the LORD, the God of Israel, and we cannot harm them.'",
      "T": "The leaders answered the whole assembly: 'We gave them a sworn oath in the name of the LORD God of Israel — we cannot lay a hand on them.'"
    },
    "20": {
      "L": "'This we will do to them: we will let them live, lest wrath come upon us because of the oath which we swore to them.'",
      "M": "'We will let them live, so that God's anger does not fall on us because of the oath we gave them.'",
      "T": "'We will let them live. If we break the sworn oath, God's wrath will fall on us — and we cannot have that.'"
    },
    "21": {
      "L": "And the leaders said to them, 'Let them live.' And they became cutters of wood and drawers of water for all the congregation, as the leaders had said to them.",
      "M": "So the leaders said, 'Let them live.' They became woodcutters and water-carriers for the whole community, as the leaders had decreed.",
      "T": "'Let them live,' the leaders ruled. So the Gibeonites became hewers of wood and drawers of water for the whole community — the role the leaders had assigned them."
    },
    "22": {
      "L": "And Joshua called for them and spoke to them, saying, 'Why have you deceived us, saying, \"We are very far from you,\" when you dwell among us?'",
      "M": "Joshua summoned the Gibeonites and said to them, 'Why did you deceive us by saying you were from a distant land when you actually live among us?'",
      "T": "Joshua summoned the Gibeonites and confronted them: 'Why did you deceive us — claiming to come from far away when you live right here among us?'"
    },
    "23": {
      "L": "'Now therefore you are cursed, and none of you shall be freed from being bondmen and cutters of wood and drawers of water for the house of my God.'",
      "M": "'You are therefore cursed: you will never cease to be slaves — woodcutters and water-carriers — for the house of my God.'",
      "T": "'You are therefore cursed — none of your people will ever be free from serving as woodcutters and water-carriers for the house of my God.'"
    },
    "24": {
      "L": "And they answered Joshua and said, 'Because it was certainly told your servants how the LORD your God commanded his servant Moses to give you all the land and to destroy all the inhabitants of the land before you, therefore we were sore afraid for our lives because of you and have done this thing.'",
      "M": "They answered Joshua, 'Your servants were clearly told how the LORD your God commanded his servant Moses to give you all this land and destroy all its inhabitants before you. We feared for our lives because of you — that is why we did this.'",
      "T": "They answered Joshua: 'We were told plainly how the LORD your God commanded his servant Moses to give you this whole land and to destroy all its inhabitants. We feared for our very lives — that is why we did what we did.'"
    },
    "25": {
      "L": "'And now, behold, we are in your hand. Do with us as it seems good and right to you.'",
      "M": "'Now we are in your hands. Do to us whatever you think is good and right.'",
      "T": "'We are in your hands. Do with us whatever seems right and good to you.'"
    },
    "26": {
      "L": "And so he did to them, and delivered them from the hand of the children of Israel so that they did not slay them.",
      "M": "So Joshua did as they asked, and kept the Israelites from killing them.",
      "T": "That is what Joshua did — he rescued them from the Israelites' sword."
    },
    "27": {
      "L": "And Joshua made them that day cutters of wood and drawers of water for the congregation and for the altar of the LORD, in the place that he should choose. And so they are to this day.",
      "M": "That day Joshua made them woodcutters and water-carriers for the community and for the altar of the LORD, at whatever place the LORD would choose. And they continue in that role to this day.",
      "T": "Joshua assigned them that day as woodcutters and water-carriers for the community and for the LORD's altar — serving wherever the LORD would choose. And so it has remained to this day."
    }
  },
  "10": {
    "1": {
      "L": "Now it came to pass when Adonizedek king of Jerusalem heard how Joshua had taken Ai and had devoted it to destruction, doing to Ai and its king as he had done to Jericho and its king, and how the inhabitants of Gibeon had made peace with Israel and were among them,",
      "M": "When Adonizedek king of Jerusalem heard how Joshua had captured and destroyed Ai — dealing with Ai and its king as he had dealt with Jericho and its king — and how the people of Gibeon had made peace with Israel and were living among them,",
      "T": "Adonizedek king of Jerusalem heard that Joshua had captured Ai and devoted it to destruction — treating Ai and its king the same way he had treated Jericho — and that the Gibeonites had made peace with Israel and were living among them."
    },
    "2": {
      "L": "he feared greatly, because Gibeon was a great city, as one of the royal cities, and because it was greater than Ai, and all its men were mighty.",
      "M": "He was deeply alarmed, because Gibeon was a large city, like one of the royal cities, greater than Ai, and all its men were warriors.",
      "T": "This alarmed him greatly. Gibeon was a major city — one of the royal cities — larger than Ai, with an army of skilled warriors."
    },
    "3": {
      "L": "Wherefore Adonizedek king of Jerusalem sent to Hoham king of Hebron and to Piram king of Jarmuth and to Japhia king of Lachish and to Debir king of Eglon, saying,",
      "M": "So Adonizedek king of Jerusalem sent word to Hoham king of Hebron, Piram king of Jarmuth, Japhia king of Lachish, and Debir king of Eglon:",
      "T": "Adonizedek king of Jerusalem sent to Hoham king of Hebron, Piram king of Jarmuth, Japhia king of Lachish, and Debir king of Eglon with this message:"
    },
    "4": {
      "L": "'Come up to me and help me, that we may attack Gibeon, for it has made peace with Joshua and with the children of Israel.'",
      "M": "'Come and help me attack Gibeon, for it has made peace with Joshua and the Israelites.'",
      "T": "'Come up and help me strike Gibeon — they have made peace with Joshua and Israel.'"
    },
    "5": {
      "L": "Therefore the five kings of the Amorites, the king of Jerusalem and the king of Hebron and the king of Jarmuth and the king of Lachish and the king of Eglon, gathered themselves together and went up with all their armies and encamped before Gibeon and made war against it.",
      "M": "So the five Amorite kings — of Jerusalem, Hebron, Jarmuth, Lachish, and Eglon — joined forces, marched up with all their armies, and besieged Gibeon, attacking it.",
      "T": "The five Amorite kings — of Jerusalem, Hebron, Jarmuth, Lachish, and Eglon — united their armies, marched out together, besieged Gibeon, and attacked."
    },
    "6": {
      "L": "And the men of Gibeon sent to Joshua at the camp at Gilgal, saying, 'Slack not your hand from your servants. Come up to us quickly and save us and help us, for all the kings of the Amorites that dwell in the hill country are gathered together against us.'",
      "M": "The Gibeonites sent word to Joshua at the camp at Gilgal: 'Do not abandon your servants! Come up to us quickly — rescue us and help us! All the Amorite kings from the hill country have allied against us.'",
      "T": "The men of Gibeon sent an urgent message to Joshua at Gilgal: 'Do not abandon your servants! Come quickly — rescue us! All the Amorite kings from the highlands have united against us!'"
    },
    "7": {
      "L": "So Joshua went up from Gilgal, he and all the people of war with him, and all the mighty men of valor.",
      "M": "So Joshua marched up from Gilgal with his entire fighting force, including all his best warriors.",
      "T": "Joshua marched up from Gilgal — the whole fighting force with him, every seasoned warrior."
    },
    "8": {
      "L": "And the LORD said to Joshua, 'Fear them not, for I have delivered them into your hand. There shall not a man of them stand before you.'",
      "M": "The LORD said to Joshua, 'Do not be afraid of them; I have given them into your hand. Not one of them will be able to stand against you.'",
      "T": "The LORD said to Joshua: 'Do not be afraid of them — I have handed them to you. Not one man will be able to stand before you.'"
    },
    "9": {
      "L": "Joshua therefore came unto them suddenly and went up from Gilgal all night.",
      "M": "After marching all night from Gilgal, Joshua took them by surprise.",
      "T": "Joshua marched all night from Gilgal and fell on them without warning."
    },
    "10": {
      "L": "And the LORD discomfited them before Israel and slew them with a great slaughter at Gibeon and chased them along the way that goes up to Beth-horon and smote them to Azekah and to Makkedah.",
      "M": "The LORD threw them into panic before Israel. Israel struck them down in a great victory at Gibeon, chased them along the road going up to Beth-horon, and cut them down all the way to Azekah and Makkedah.",
      "T": "The LORD threw them into confusion before Israel. Israel struck them a massive blow at Gibeon and chased them up the pass of Beth-horon, cutting them down all the way to Azekah and Makkedah."
    },
    "11": {
      "L": "And it came to pass as they fled from before Israel, while they were in the going down to Beth-horon, that the LORD cast down great stones from heaven upon them as far as Azekah, and they died. They were more who died with the hailstones than they whom the children of Israel slew with the sword.",
      "M": "While they were fleeing before Israel down the pass of Beth-horon, the LORD rained down huge hailstones on them all the way to Azekah, and they died. More of them were killed by the hailstones than by the Israelites' swords.",
      "T": "As the enemy fled down the Beth-horon pass, the LORD hurled massive hailstones on them from the sky — all the way to Azekah. More died from the hail than were killed by Israelite swords."
    },
    "12": {
      "L": "Then spoke Joshua to the LORD in the day when the LORD delivered up the Amorites before the children of Israel, and he said in the sight of Israel, 'Sun, stand thou still upon Gibeon; and thou, Moon, in the valley of Ajalon.'",
      "M": "On the day the LORD gave the Amorites over to Israel, Joshua prayed to the LORD in the sight of Israel: 'Sun, stand still over Gibeon! Moon, stand still over the Valley of Aijalon!'",
      "T": "That day — the day the LORD handed the Amorites to Israel — Joshua spoke to the LORD in the hearing of all Israel and said: 'Sun, be still over Gibeon! Moon, hold your place in the Valley of Aijalon!'"
    },
    "13": {
      "L": "And the sun stood still and the moon stayed until the nation had avenged itself on its enemies. Is not this written in the Book of Jasher? So the sun stood still in the midst of heaven and did not hasten to go down for about a whole day.",
      "M": "The sun stood still and the moon stopped until the nation avenged itself on its enemies. Is this not written in the Book of Jashar? The sun halted in the middle of the sky and did not hurry to set for about a full day.",
      "T": "The sun was still and the moon held its place until the nation had taken full vengeance on its enemies. This is recorded in the Book of Jashar. The sun stood fixed in the middle of the sky and did not hasten to go down for nearly a full day."
    },
    "14": {
      "L": "And there was no day like that before it or after it, that the LORD hearkened to the voice of a man, for the LORD fought for Israel.",
      "M": "There has never been a day like it before or since — a day when the LORD listened to a human voice — for the LORD fought for Israel.",
      "T": "There has never been a day like it — before or since — when the LORD responded to a human voice like that. For the LORD himself was fighting for Israel."
    },
    "15": {
      "L": "And Joshua and all Israel with him returned to the camp at Gilgal.",
      "M": "Then Joshua and all Israel returned to the camp at Gilgal.",
      "T": "Joshua and all Israel returned to the camp at Gilgal."
    },
    "16": {
      "L": "But these five kings fled and hid themselves in the cave at Makkedah.",
      "M": "The five kings fled and hid in a cave at Makkedah.",
      "T": "The five kings had fled and hidden themselves in a cave at Makkedah."
    },
    "17": {
      "L": "And it was told Joshua, saying, 'The five kings are found hid in a cave at Makkedah.'",
      "M": "Joshua was told, 'The five kings have been found hiding in the cave at Makkedah.'",
      "T": "Word came to Joshua: 'The five kings have been found — hiding in the cave at Makkedah.'"
    },
    "18": {
      "L": "And Joshua said, 'Roll great stones unto the mouth of the cave and set men by it to guard them.'",
      "M": "Joshua said, 'Roll large stones to the entrance of the cave and post guards to watch over them.'",
      "T": "'Roll large stones over the cave mouth,' Joshua ordered, 'and set guards there.'"
    },
    "19": {
      "L": "'But do not stay there yourselves. Pursue after your enemies and smite the hindmost of them. Do not let them enter into their cities, for the LORD your God has delivered them into your hand.'",
      "M": "'But don't you stay there! Pursue your enemies; cut off their retreat and don't let them reach their cities, for the LORD your God has handed them over to you.'",
      "T": "'But the rest of you — keep pursuing! Cut off the retreat. Don't let them get back to their cities. The LORD your God has handed them to you.'"
    },
    "20": {
      "L": "And it came to pass when Joshua and the children of Israel had made an end of slaying them with a very great slaughter, until they were consumed, and the remnant that remained of them had entered into fortified cities,",
      "M": "When Joshua and the Israelites had finished slaughtering them in a tremendous defeat — the survivors having taken refuge in the fortified cities —",
      "T": "When Joshua and the Israelites had finished the slaughter — a crushing blow — and whatever survivors remained had scrambled into their fortified cities,"
    },
    "21": {
      "L": "all the people returned to the camp to Joshua at Makkedah in peace. None moved his tongue against any of the children of Israel.",
      "M": "all the troops returned safely to Joshua at the camp at Makkedah. No one dared to say a word against the Israelites.",
      "T": "the whole army returned in peace to Joshua at Makkedah — not a man dared breathe a threat against Israel."
    },
    "22": {
      "L": "Then Joshua said, 'Open the mouth of the cave and bring out those five kings unto me out of the cave.'",
      "M": "Joshua said, 'Open the mouth of the cave and bring out those five kings to me.'",
      "T": "'Open the cave and bring the five kings out to me,' Joshua ordered."
    },
    "23": {
      "L": "And they did so, and brought forth those five kings unto him out of the cave — the king of Jerusalem, the king of Hebron, the king of Jarmuth, the king of Lachish, and the king of Eglon.",
      "M": "They did so, and brought out the five kings from the cave: the king of Jerusalem, the king of Hebron, the king of Jarmuth, the king of Lachish, and the king of Eglon.",
      "T": "They did so, and the five kings were brought out from the cave: the king of Jerusalem, the king of Hebron, the king of Jarmuth, the king of Lachish, and the king of Eglon."
    },
    "24": {
      "L": "And it came to pass when they brought out those kings to Joshua, that Joshua called for all the men of Israel and said unto the chiefs of the men of war who went with him, 'Come near, put your feet upon the necks of these kings.' And they came near and put their feet upon their necks.",
      "M": "When they had brought the kings out to Joshua, he summoned all the Israelites and said to the commanders of the troops who had come with him, 'Come forward and put your feet on the necks of these kings.' They came forward and placed their feet on their necks.",
      "T": "When the kings were brought out before him, Joshua summoned all Israel and said to his commanding officers: 'Come and put your feet on the necks of these kings.' They came forward and placed their feet on the kings' necks."
    },
    "25": {
      "L": "And Joshua said unto them, 'Fear not nor be dismayed. Be strong and courageous, for thus shall the LORD do to all your enemies against whom you fight.'",
      "M": "Joshua said to them, 'Do not be afraid or discouraged. Be strong and courageous, for this is how the LORD will deal with all the enemies you fight.'",
      "T": "'Do not be afraid; do not lose heart,' Joshua said to them. 'Be strong and full of courage — this is what the LORD will do to every enemy you face.'"
    },
    "26": {
      "L": "And afterward Joshua smote them and slew them and hanged them on five trees. And they were hanging upon the trees until the evening.",
      "M": "Afterward Joshua had the kings killed and their bodies hung on five trees, where they remained until evening.",
      "T": "After that Joshua had them killed and their bodies hung on five trees, where they hung until sunset."
    },
    "27": {
      "L": "And it came to pass at the time of the going down of the sun that Joshua commanded and they took them down from the trees and cast them into the cave wherein they had been hid, and laid great stones in the mouth of the cave, which remain until this very day.",
      "M": "At sunset Joshua ordered them taken down from the trees and thrown into the cave where they had hidden. Large stones were placed at the entrance of the cave, and they remain there to this day.",
      "T": "At sunset Joshua gave the order: the bodies were taken down from the trees and thrown into the cave where the kings had hidden. Large stones were placed over the entrance — and they remain there to this very day."
    },
    "28": {
      "L": "And Joshua took Makkedah on that day and smote it with the edge of the sword and utterly destroyed the king thereof and all the souls that were therein. He left none remaining. And he did to the king of Makkedah as he had done to the king of Jericho.",
      "M": "That same day Joshua took Makkedah, struck it with the sword, and completely destroyed the king and every person in it. He left no survivors, treating the king of Makkedah as he had treated the king of Jericho.",
      "T": "That day Joshua took Makkedah — put it to the sword, and devoted its king and every soul in it to destruction. Not one was left. He dealt with Makkedah's king as he had dealt with Jericho's."
    },
    "29": {
      "L": "Then Joshua and all Israel with him passed from Makkedah to Libnah and fought against Libnah.",
      "M": "Then Joshua and all Israel moved on from Makkedah to Libnah and attacked it.",
      "T": "Joshua and all Israel moved from Makkedah to Libnah and attacked it."
    },
    "30": {
      "L": "And the LORD delivered it also and its king into the hand of Israel. And he smote it with the edge of the sword and all the souls that were therein. He left none remaining in it. And he did to its king as he had done to the king of Jericho.",
      "M": "The LORD also handed Libnah and its king over to Israel. Joshua struck it and all its people with the sword, leaving no survivors. He treated its king as he had treated the king of Jericho.",
      "T": "The LORD gave Libnah and its king into Israel's hand. Joshua put it and every person in it to the sword — not one survivor. He dealt with its king as he had dealt with Jericho's."
    },
    "31": {
      "L": "And Joshua and all Israel with him passed from Libnah to Lachish and encamped against it and fought against it.",
      "M": "Next Joshua and all Israel moved from Libnah to Lachish. They took up positions around it and attacked.",
      "T": "From Libnah, Joshua and all Israel moved to Lachish, laid siege to it, and attacked."
    },
    "32": {
      "L": "And the LORD delivered Lachish into the hand of Israel, and Joshua took it on the second day and smote it with the edge of the sword, and all the souls therein, according to all that he had done to Libnah.",
      "M": "The LORD handed Lachish over to Israel. Joshua captured it on the second day and put every person in it to the sword, just as he had done to Libnah.",
      "T": "The LORD gave Lachish to Israel. Joshua took it on the second day and put every person to the sword, just as he had done to Libnah."
    },
    "33": {
      "L": "Then Horam king of Gezer came up to help Lachish. And Joshua smote him and his people until he had left him none remaining.",
      "M": "King Horam of Gezer came up to help Lachish, but Joshua defeated him and his army, leaving no survivors.",
      "T": "King Horam of Gezer came up to relieve Lachish, but Joshua struck him down along with his whole army — not one survivor."
    },
    "34": {
      "L": "And from Lachish Joshua and all Israel with him passed to Eglon and encamped against it and fought against it.",
      "M": "From Lachish, Joshua and all Israel moved on to Eglon. They surrounded it and attacked.",
      "T": "From Lachish, Joshua and all Israel moved on to Eglon, surrounded it, and attacked."
    },
    "35": {
      "L": "And they took it on that day and smote it with the edge of the sword, and all the souls that were therein he devoted to destruction that day, according to all that he had done to Lachish.",
      "M": "They captured it that same day and put every person in it to the sword, devoting everyone to destruction, just as they had done to Lachish.",
      "T": "They captured Eglon that day, put it to the sword, and devoted every soul in it to destruction — just as they had done to Lachish."
    },
    "36": {
      "L": "And Joshua and all Israel with him went up from Eglon to Hebron and fought against it.",
      "M": "Then Joshua and all Israel moved from Eglon and went up to attack Hebron.",
      "T": "From Eglon, Joshua and all Israel went up to Hebron and attacked it."
    },
    "37": {
      "L": "And they took it and smote it with the edge of the sword, and its king and all its cities and all the souls that were therein. He left none remaining, according to all that he had done to Eglon. He devoted it and all the souls that were therein to destruction.",
      "M": "They captured it, struck the city and its king and all its surrounding towns with the sword, and killed everyone in it — leaving no survivors — just as they had done to Eglon. They devoted everyone to destruction.",
      "T": "They took Hebron — put the city, its king, all its surrounding towns, and every person to the sword. Not one survivor remained, just as at Eglon. Every soul was devoted to destruction."
    },
    "38": {
      "L": "And Joshua and all Israel with him turned back to Debir and fought against it.",
      "M": "Then Joshua and all Israel turned back to Debir and attacked it.",
      "T": "Joshua and all Israel wheeled back to Debir and attacked it."
    },
    "39": {
      "L": "And he took it and its king and all its cities, and they smote them with the edge of the sword and devoted all the souls that were therein to destruction. He left none remaining. As he had done to Hebron and to Libnah and its king, so he did to Debir and to its king.",
      "M": "He captured Debir with its king and surrounding towns, struck everyone with the sword, and devoted all to destruction — leaving no survivors. He treated Debir and its king as he had treated Hebron and Libnah with their kings.",
      "T": "He took Debir and its king and surrounding towns, put everyone to the sword, and devoted all to destruction — not one survivor. He treated Debir and its king just as he had treated Hebron, Libnah, and their kings."
    },
    "40": {
      "L": "So Joshua struck all the land, the hill country and the Negeb and the lowland and the slopes, and all their kings. He left none remaining but devoted to destruction all that breathed, as the LORD God of Israel commanded.",
      "M": "So Joshua subdued the whole region — the hill country, the Negev, the western foothills, and the mountain slopes — along with all their kings. He left no survivors; he devoted all who breathed to destruction, as the LORD God of Israel had commanded.",
      "T": "Joshua thus conquered the entire region — the highlands, the Negev, the western foothills, and the mountain slopes — and all their kings. He left not one alive; everything that breathed was devoted to destruction, as the LORD God of Israel had commanded."
    },
    "41": {
      "L": "And Joshua smote them from Kadesh-barnea even to Gaza, and all the country of Goshen, even to Gibeon.",
      "M": "Joshua struck down all the territory from Kadesh-barnea to Gaza, and all the region of Goshen as far as Gibeon.",
      "T": "Joshua's campaign extended from Kadesh-barnea to Gaza, across all the region of Goshen, up to Gibeon."
    },
    "42": {
      "L": "And Joshua took all these kings and their land at one time, because the LORD God of Israel fought for Israel.",
      "M": "Joshua captured all these kings and their lands in one campaign, because the LORD, the God of Israel, fought for Israel.",
      "T": "All these kings and their lands Joshua took in a single campaign, for the LORD God of Israel was fighting for Israel."
    },
    "43": {
      "L": "Then Joshua and all Israel with him returned to the camp at Gilgal.",
      "M": "Then Joshua and all Israel returned to the camp at Gilgal.",
      "T": "Joshua and all Israel then returned to the camp at Gilgal."
    }
  },
  "11": {
    "1": {
      "L": "And it came to pass when Jabin king of Hazor heard of these things that he sent to Jobab king of Madon and to the king of Shimron and to the king of Achshaph,",
      "M": "When Jabin king of Hazor heard of these events, he sent word to Jobab king of Madon, to the king of Shimron, and to the king of Achshaph,",
      "T": "When Jabin king of Hazor heard the news, he sent word to Jobab king of Madon, and to the kings of Shimron and Achshaph,"
    },
    "2": {
      "L": "and to the kings in the northern hills and in the Arabah south of Chinneroth and in the lowland and in the heights of Dor on the west,",
      "M": "and to the kings in the northern hill country, in the Arabah south of Kinnereth, in the western foothills, and in the heights of Dor on the west,",
      "T": "and to the kings of the northern highlands, the Arabah south of Kinnereth, the western lowlands, and the heights of Dor on the coast,"
    },
    "3": {
      "L": "to the Canaanites on the east and the west, and the Amorites and the Hittites and the Perizzites and the Jebusites in the hill country, and the Hivites under Hermon in the land of Mizpah.",
      "M": "to the Canaanites on the east and west, to the Amorites, Hittites, Perizzites, and Jebusites in the hill country, and to the Hivites below Hermon in the region of Mizpah.",
      "T": "and to the Canaanites east and west, the Amorites, Hittites, Perizzites, and Jebusites in the highlands, and the Hivites below Mount Hermon in the land of Mizpah."
    },
    "4": {
      "L": "And they went out, they and all their armies with them, very many people, as the sand that is on the sea shore in multitude, with very many horses and chariots.",
      "M": "They marched out with all their forces — a huge army, as numerous as the sand on the seashore — with a great many horses and chariots.",
      "T": "They mustered their forces — a vast army, as countless as the sand on the seashore — with horses and chariots in great number."
    },
    "5": {
      "L": "And all these kings met together and came and encamped together at the waters of Merom to fight against Israel.",
      "M": "All these kings joined forces and came to camp together at the Waters of Merom to fight against Israel.",
      "T": "All these kings assembled and marched out together to the Waters of Merom to make war on Israel."
    },
    "6": {
      "L": "And the LORD said to Joshua, 'Be not afraid because of them, for tomorrow about this time will I deliver them up all slain before Israel. You shall hamstring their horses and burn their chariots with fire.'",
      "M": "The LORD said to Joshua, 'Do not be afraid of them, for by this time tomorrow I will hand all of them over, dead, to Israel. You must hamstring their horses and burn their chariots.'",
      "T": "The LORD said to Joshua: 'Do not be afraid of them. By this time tomorrow I will have delivered all of them, slain, to Israel. Hamstring their horses and burn their chariots.'"
    },
    "7": {
      "L": "So Joshua and all his people of war came against them at the waters of Merom suddenly and fell upon them.",
      "M": "Joshua and the whole army made a surprise attack on them at the Waters of Merom.",
      "T": "Joshua and all his fighting men fell on them suddenly at the Waters of Merom."
    },
    "8": {
      "L": "And the LORD delivered them into the hand of Israel, who smote them and chased them to great Sidon and to Misrephoth-maim and to the valley of Mizpah eastward. And they smote them until they left none remaining.",
      "M": "The LORD gave them into Israel's hand. They struck them down and pursued them as far as Greater Sidon and Misrephoth-maim, and eastward as far as the Valley of Mizpah. They struck them down until no survivor was left.",
      "T": "The LORD gave them into Israel's hand. Israel cut them down and chased the survivors as far as Greater Sidon and Misrephoth-maim, and east to the Valley of Mizpah — striking them down until not one remained."
    },
    "9": {
      "L": "And Joshua did to them as the LORD commanded him. He hamstrung their horses and burned their chariots with fire.",
      "M": "Joshua did just as the LORD had told him: he hamstrung their horses and burned their chariots.",
      "T": "Joshua did exactly as the LORD directed: he hamstrung the horses and burned the chariots."
    },
    "10": {
      "L": "And Joshua turned back at that time and took Hazor and smote its king with the sword. For Hazor beforetime was the head of all those kingdoms.",
      "M": "At that time Joshua turned back and captured Hazor, putting its king to the sword — for Hazor had formerly been the leading city among all those kingdoms.",
      "T": "Joshua then turned back and captured Hazor, putting its king to the sword. Hazor had been the dominant power over all those kingdoms."
    },
    "11": {
      "L": "And they smote all the souls that were therein with the edge of the sword, devoting them to destruction. There was not any left to breathe. And he burned Hazor with fire.",
      "M": "They struck everyone in it with the sword, devoting them to destruction — no one who breathed was left. And Joshua burned Hazor.",
      "T": "They put every soul in it to the sword and devoted them to destruction — nothing that breathed was left alive. Then Joshua burned Hazor to the ground."
    },
    "12": {
      "L": "And all the cities of those kings and all their kings Joshua took and smote with the edge of the sword, devoting them to destruction, as Moses the servant of the LORD had commanded.",
      "M": "Joshua captured and struck with the sword all the cities of those kings and all their kings — devoting them to destruction, just as Moses the servant of the LORD had commanded.",
      "T": "Joshua captured all the cities of those kings and all their kings, putting them to the sword and devoting them to destruction, exactly as Moses the LORD's servant had commanded."
    },
    "13": {
      "L": "But as for the cities that stood on their mounds, Israel burned none of them, except Hazor alone. That Joshua burned.",
      "M": "But Israel did not burn the cities built on their mounds — only Hazor did Joshua burn.",
      "T": "Israel did not burn the cities still standing on their ancient mounds — only Hazor, which Joshua burned."
    },
    "14": {
      "L": "And all the spoil of these cities and the livestock the children of Israel took for a prey to themselves. But every man they smote with the edge of the sword until they had destroyed them. They left not any that breathed.",
      "M": "The Israelites kept all the plunder and livestock from these cities for themselves. But every person they struck down with the sword until they had destroyed them all — no one was left who breathed.",
      "T": "Israel took all the spoil and livestock from these cities as their own. But every human being was put to the sword until every last one was destroyed — nothing that breathed was left."
    },
    "15": {
      "L": "As the LORD commanded Moses his servant, so Moses commanded Joshua, and so Joshua did. He left nothing undone of all that the LORD had commanded Moses.",
      "M": "As the LORD had commanded his servant Moses, so Moses had commanded Joshua, and Joshua carried it out — he left nothing undone of all the LORD had commanded Moses.",
      "T": "The LORD commanded Moses; Moses commanded Joshua; Joshua obeyed. He left nothing undone of all that the LORD had commanded Moses."
    },
    "16": {
      "L": "So Joshua took all that land, the hill country and all the Negeb and all the land of Goshen and the lowland and the Arabah and the hill country of Israel and its lowland,",
      "M": "Joshua took all this land: the hill country, all the Negev, all the region of Goshen, the western foothills, the Arabah, and the hill country and foothills of Israel,",
      "T": "Joshua took the whole land: the highlands, all the Negev, all the land of Goshen, the western lowlands, the Arabah, and the highlands and foothills of Israel —"
    },
    "17": {
      "L": "from Mount Halak that goes up to Seir even to Baalgad in the valley of Lebanon under mount Hermon. And all their kings he took and smote and slew them.",
      "M": "from Mount Halak, which runs toward Seir, to Baal-gad in the Lebanon Valley below Mount Hermon. He captured all their kings, struck them down, and put them to death.",
      "T": "from Mount Halak rising toward Seir all the way north to Baal-gad in the Lebanon Valley below Mount Hermon. Every king he captured, he struck down and executed."
    },
    "18": {
      "L": "Joshua made war a long time with all those kings.",
      "M": "Joshua waged war against all these kings for a long time.",
      "T": "The war against all these kings was long."
    },
    "19": {
      "L": "There was not a city that made peace with the children of Israel except the Hivites, the inhabitants of Gibeon. They took all in battle.",
      "M": "Except for the Hivites living in Gibeon, not a single city made peace with the Israelites — they conquered them all in battle.",
      "T": "Not a single city made peace with Israel — except the Hivites of Gibeon. Every other city was taken by force."
    },
    "20": {
      "L": "For it was of the LORD to harden their hearts to come against Israel in battle, that he might devote them to destruction and that they might have no mercy shown them but be destroyed, as the LORD commanded Moses.",
      "M": "It was the LORD who hardened their hearts to wage war against Israel, so that he might put them under the ban and destroy them completely, without mercy, as the LORD had commanded Moses.",
      "T": "For it was the LORD's design that their hearts be hardened to make war on Israel — so they would be devoted to destruction with no mercy shown, exactly as the LORD had commanded Moses. The outcome was never in doubt."
    },
    "21": {
      "L": "And Joshua came at that time and cut off the Anakim from the hill country, from Hebron, from Debir, from Anab, and from all the hill country of Judah and from all the hill country of Israel. Joshua devoted them to destruction with their cities.",
      "M": "At that time Joshua went and destroyed the Anakites from the hill country — from Hebron, Debir, and Anab — and from all the hill country of Judah and Israel. Joshua completely destroyed them and their cities.",
      "T": "At that time Joshua destroyed the Anakites from the highlands — from Hebron, Debir, Anab, and all the highlands of Judah and Israel. Joshua devoted them and their cities to destruction."
    },
    "22": {
      "L": "There was none of the Anakim left in the land of the children of Israel. Only in Gaza, in Gath, and in Ashdod did some remain.",
      "M": "None of the Anakites were left in Israelite territory, though some survived in Gaza, Gath, and Ashdod.",
      "T": "Not one Anakim remained in Israelite territory. Some survived in Gaza, Gath, and Ashdod — and from there their line would eventually produce Goliath and the Philistine giants."
    },
    "23": {
      "L": "So Joshua took all the land, according to all that the LORD said to Moses. And Joshua gave it for an inheritance to Israel according to their divisions by their tribes. And the land had rest from war.",
      "M": "Joshua took the entire land, just as the LORD had told Moses, and he gave it as an inheritance to Israel according to their tribal divisions. Then the land had rest from war.",
      "T": "Joshua took the whole land — exactly as the LORD had spoken to Moses — and gave it to Israel as their inheritance according to their tribal divisions. And the land rested from war."
    }
  },
  "12": {
    "1": {
      "L": "Now these are the kings of the land whom the children of Israel struck and whose land they possessed beyond the Jordan toward the sunrise, from the river Arnon to mount Hermon and all the Arabah on the east:",
      "M": "These are the kings of the land that the Israelites defeated and whose territory they took over east of the Jordan — from the Arnon River to Mount Hermon, including the eastern Arabah:",
      "T": "Here are the kings of the land whom Israel struck down and whose territory they possessed east of the Jordan — from the Arnon River to Mount Hermon, along with all the eastern Arabah:"
    },
    "2": {
      "L": "Sihon king of the Amorites who dwelt in Heshbon, who ruled from Aroer, which is upon the bank of the river Arnon, and from the middle of the river, and from half Gilead even unto the river Jabbok, which is the border of the children of Ammon;",
      "M": "Sihon king of the Amorites, who lived at Heshbon. He ruled from Aroer on the bank of the Arnon River — including the middle of the river — extending as far as the Jabbok River, the border of Ammon, and half of Gilead.",
      "T": "Sihon, Amorite king at Heshbon, whose domain ran from Aroer on the Arnon's bank — and the river's midchannel — across half of Gilead to the Jabbok, the Ammonite border;"
    },
    "3": {
      "L": "and the Arabah to the Sea of Chinneroth on the east and to the sea of the Arabah, even the Salt Sea, on the east, the way to Beth-jeshimoth, and from the south under the slopes of Pisgah;",
      "M": "and the eastern Arabah from the Sea of Kinnereth to the Dead Sea of the Arabah, the road to Beth-jeshimoth, and southward under the slopes of Pisgah.",
      "T": "and the eastern Arabah from the Sea of Kinnereth down to the Dead Sea, along the road to Beth-jeshimoth and south along the slopes of Pisgah;"
    },
    "4": {
      "L": "and the coast of Og king of Bashan, who was of the remnant of the Rephaim, who dwelt at Ashtaroth and at Edrei,",
      "M": "and the territory of Og king of Bashan, one of the last of the Rephaim, who lived at Ashtaroth and Edrei;",
      "T": "and the territory of Og king of Bashan — one of the last survivors of the Rephaim — who ruled from Ashtaroth and Edrei:"
    },
    "5": {
      "L": "and reigned in mount Hermon and in Salcah and in all Bashan unto the border of the Geshurites and the Maachathites and half Gilead, the border of Sihon king of Heshbon.",
      "M": "He ruled over Mount Hermon, Salecah, all of Bashan up to the border of the Geshurites and Maacathites, and half of Gilead to the border of Sihon king of Heshbon.",
      "T": "He ruled over Mount Hermon, Salecah, all of Bashan to the borders of Geshur and Maacah, and half of Gilead to Sihon's border."
    },
    "6": {
      "L": "Them did Moses the servant of the LORD and the children of Israel smite. And Moses the servant of the LORD gave their land for a possession to the Reubenites and the Gadites and the half-tribe of Manasseh.",
      "M": "Moses the servant of the LORD and the Israelites conquered them, and Moses gave their land as a possession to the Reubenites, the Gadites, and the half-tribe of Manasseh.",
      "T": "Moses the LORD's servant and the Israelites defeated them. Moses the LORD's servant gave their land to the Reubenites, Gadites, and the half-tribe of Manasseh as their inheritance."
    },
    "7": {
      "L": "And these are the kings of the country which Joshua and the children of Israel smote on this side of the Jordan on the west, from Baalgad in the valley of Lebanon even to mount Halak that goeth up to Seir. Joshua gave it for a possession to the tribes of Israel according to their divisions,",
      "M": "These are the kings in Canaan that Joshua and the Israelites defeated west of the Jordan — from Baal-gad in the Lebanon Valley to Mount Halak rising toward Seir. Joshua gave their land as an inheritance to the tribes of Israel by their tribal divisions,",
      "T": "And these are the kings west of the Jordan whom Joshua and Israel defeated — from Baal-gad in the Lebanon Valley south to Mount Halak rising toward Seir. Joshua gave their land to the tribes of Israel as their inheritance by tribal divisions:"
    },
    "8": {
      "L": "in the hill country and in the lowland and in the Arabah and in the slopes and in the wilderness and in the Negeb, the Hittite, the Amorite, and the Canaanite, the Perizzite, the Hivite, and the Jebusite:",
      "M": "in the hill country, the western foothills, the Arabah, the mountain slopes, the wilderness, and the Negev — the lands of the Hittites, Amorites, Canaanites, Perizzites, Hivites, and Jebusites:",
      "T": "the highlands, the foothills, the Arabah, the slopes, the desert, and the Negev — formerly the territory of the Hittites, Amorites, Canaanites, Perizzites, Hivites, and Jebusites:"
    },
    "9": {
      "L": "the king of Jericho, one; the king of Ai, which is beside Bethel, one;",
      "M": "the king of Jericho — one; the king of Ai near Bethel — one;",
      "T": "the king of Jericho, one; the king of Ai beside Bethel, one;"
    },
    "10": {
      "L": "the king of Jerusalem, one; the king of Hebron, one;",
      "M": "the king of Jerusalem — one; the king of Hebron — one;",
      "T": "the king of Jerusalem, one; the king of Hebron, one;"
    },
    "11": {
      "L": "the king of Jarmuth, one; the king of Lachish, one;",
      "M": "the king of Jarmuth — one; the king of Lachish — one;",
      "T": "the king of Jarmuth, one; the king of Lachish, one;"
    },
    "12": {
      "L": "the king of Eglon, one; the king of Gezer, one;",
      "M": "the king of Eglon — one; the king of Gezer — one;",
      "T": "the king of Eglon, one; the king of Gezer, one;"
    },
    "13": {
      "L": "the king of Debir, one; the king of Geder, one;",
      "M": "the king of Debir — one; the king of Geder — one;",
      "T": "the king of Debir, one; the king of Geder, one;"
    },
    "14": {
      "L": "the king of Hormah, one; the king of Arad, one;",
      "M": "the king of Hormah — one; the king of Arad — one;",
      "T": "the king of Hormah, one; the king of Arad, one;"
    },
    "15": {
      "L": "the king of Libnah, one; the king of Adullam, one;",
      "M": "the king of Libnah — one; the king of Adullam — one;",
      "T": "the king of Libnah, one; the king of Adullam, one;"
    },
    "16": {
      "L": "the king of Makkedah, one; the king of Bethel, one;",
      "M": "the king of Makkedah — one; the king of Bethel — one;",
      "T": "the king of Makkedah, one; the king of Bethel, one;"
    },
    "17": {
      "L": "the king of Tappuah, one; the king of Hepher, one;",
      "M": "the king of Tappuah — one; the king of Hepher — one;",
      "T": "the king of Tappuah, one; the king of Hepher, one;"
    },
    "18": {
      "L": "the king of Aphek, one; the king of Lasharon, one;",
      "M": "the king of Aphek — one; the king of Lasharon — one;",
      "T": "the king of Aphek, one; the king of Lasharon, one;"
    },
    "19": {
      "L": "the king of Madon, one; the king of Hazor, one;",
      "M": "the king of Madon — one; the king of Hazor — one;",
      "T": "the king of Madon, one; the king of Hazor, one;"
    },
    "20": {
      "L": "the king of Shimron-meron, one; the king of Achshaph, one;",
      "M": "the king of Shimron-meron — one; the king of Achshaph — one;",
      "T": "the king of Shimron-meron, one; the king of Achshaph, one;"
    },
    "21": {
      "L": "the king of Taanach, one; the king of Megiddo, one;",
      "M": "the king of Taanach — one; the king of Megiddo — one;",
      "T": "the king of Taanach, one; the king of Megiddo, one;"
    },
    "22": {
      "L": "the king of Kedesh, one; the king of Jokneam in Carmel, one;",
      "M": "the king of Kedesh — one; the king of Jokneam in Carmel — one;",
      "T": "the king of Kedesh, one; the king of Jokneam in Carmel, one;"
    },
    "23": {
      "L": "the king of Dor in the heights of Dor, one; the king of Goiim in Gilgal, one;",
      "M": "the king of Dor in the region of Dor — one; the king of Goiim in Gilgal — one;",
      "T": "the king of Dor in the heights of Dor, one; the king of Goiim at Gilgal, one;"
    },
    "24": {
      "L": "the king of Tirzah, one — all the kings thirty and one.",
      "M": "the king of Tirzah — one. In all, thirty-one kings.",
      "T": "the king of Tirzah, one. Thirty-one kings in all."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'joshua')
        merge_tier(existing, JOSHUA, tier_key)
        save(tier_dir, 'joshua', existing)
    print('Joshua 7–12 written.')

if __name__ == '__main__':
    main()
