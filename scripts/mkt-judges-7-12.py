"""
MKT Judges chapters 7–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-judges-7-12.py

Covers: Gideon's 300 and the rout of Midian (ch. 7); the capture of Zebah and Zalmunna,
the golden ephod, and Gideon's death (ch. 8); Abimelech's brutal reign, Jotham's fable,
and God's justice at Thebez (ch. 9); the minor judges Tola and Jair, Israel's spiral of
apostasy, and the beginning of the Ammonite crisis (ch. 10); Jephthah's rise, his
diplomatic exchange with Ammon, his tragic vow, and his daughter (ch. 11); the Ephraim
conflict and "shibboleth," plus the minor judges Ibzan, Elon, and Abdon (ch. 12).

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) L/M; "the LORD" T — consistent with all
  prior OT scripts (Joshua, Deuteronomy, etc.)
- H430 (אֱלֹהִים): "God" all tiers when divine singular; "gods" when plural/pagan
- H7307 (רוּחַ): "spirit" / "Spirit" context-dependent — in 9:23 "an evil spirit" (God
  uses a disruptive spirit as instrument of justice); in 11:29 "the Spirit of the LORD"
  (capitalized — divine empowerment of Jephthah before battle); T surfaces the theological
  distinction between demonic instrumentality and prophetic anointing
- H2617 (חֶסֶד): in 8:35 "kindness" L; "faithful kindness" M; "steadfast loyal love" T —
  the Israelites' failure to show חֶסֶד to Gideon's family is a covenant-loyalty failure,
  not mere gratitude; T names this explicitly
- H5315 (נֶפֶשׁ): in 9:17 "life" — Gideon risked his life (physical survival), not the
  immaterial soul; in 10:16 "soul" L; "heart" M; "aching heart" T — the LORD's soul/heart
  being "grieved" for Israel's misery is a profound anthropopathism; T honors this
- H1368 (גִּבּוֹר): in 11:1 "mighty man" L; "warrior" M; "champion of valor" T
- H5087/H5088 (נָדַר/נֶדֶר): "vow" all tiers — Jephthah's vow is one of the most disputed
  passages in Judges; T notes the ambiguity of "whatsoever comes out" (Hebrew יֵצֵא can be
  person or animal) and that "I will offer it up as a burnt offering" may be either literal
  sacrifice or a votive dedication; the text never resolves this; T preserves the tension
- H5930 (עֹלָה): "burnt offering" all tiers
- H4910 (מָשַׁל): "rule" L; "rule" M; "govern/reign" T — in 8:22-23 Gideon refuses hereditary
  kingship; the LORD alone is king; T draws out the theocratic principle
- H646 (אֵפוֹד): "ephod" all tiers — Gideon's golden ephod in 8:27 became a cult object,
  a substitute for legitimate sanctuary access; T notes the irony: Gideon who tore down
  Baal's altar now constructs a snare for Israel
- H2181 (זָנָה): "whored / went whoring" L; "committed spiritual adultery / turned to"
  M (using "played the harlot" for devotional contexts); "chased after" with explicit note
  about covenant infidelity T
- H1168 (בַּעַל/בְּעָלִים): "Baals" / "Baal" per context — the local manifestations of the
  storm-fertility deity; Baal-berith in 9:4 is the "Baal of the Covenant," a Canaanite
  deity worshipped at Shechem; T notes the bitter irony of a covenant-god funding a
  covenant-breaking fratricide
- H2764 / H1175 (חֵרֶם/חֶרֶם): not a major issue in chs. 7-12, but Abimelech's razing of
  Shechem and salting (9:45) echoes herem language; T notes this
- H7645 (שִׁבֹּלֶת/סִבֹּלֶת): "Shibboleth" / "Sibboleth" in 12:6 — kept as transliterations;
  the Gileadites exploited phonological dialect difference (shin vs. sin/samekh) to identify
  Ephraimite fugitives; T explains the mechanism
- H2428 (חַיִל): "valor / army / force" — context-dependent throughout; Jephthah in 11:1 is
  a "mighty man of valor" (גִּבּוֹר חַיִל); the Ammonite army is "their host" (חַיִל)
- H7218 (רֹאשׁ): "head" L; "head / leader / captain" M/T — in 11:8-11 the elders make
  Jephthah "head and commander" (רֹאשׁ וְקָצִין); T surfaces the patron-client negotiation
- Jotham's fable (9:8-15): in T tier, rendered with poetic cadence and line structure
  to honor the fable's literary genre; this is the earliest fable in world literature
  recorded in prose; T foregrounds its political bite
- Ch. 10:16 note: "his soul was grieved/shortened for Israel's misery" — the Hebrew
  קָצְרָה נַפְשׁוֹ (his soul shortened/was distressed) is a vivid idiom; T renders as
  "he could bear their misery no longer" to capture both emotional and covenantal weight
- Ch. 11:29 note: "the Spirit of the LORD came upon Jephthah" uses H7307 + H3068 together,
  which is the standard formula for prophetic/military anointing (cf. Gideon in 6:34,
  Samson in 13:25); T distinguishes this from the "evil spirit" in 9:23
- Ch. 11:39 note: "and she knew no man" — confirms Jephthah's daughter died a virgin; the
  ambiguity of the vow resolution is intentional; the text chooses silence over resolution
- Ch. 12:6 note: the "shibboleth" test killed 42,000 Ephraimites — a staggering fratricide;
  T notes the tribal war here echoes the Ephraim complaint in ch. 8, but Jephthah (unlike
  Gideon) met insult with force; the contrast reveals character
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

JUDGES = {
  "7": {
    "1": {
      "L": "Then Jerubbaal, who is Gideon, rose early, and all the people that were with him, and they encamped beside the spring of Harod; and the host of Midian was north of them, by the hill of Moreh, in the valley.",
      "M": "Then Jerubbaal (that is, Gideon) and all the people with him rose early and encamped beside the spring of Harod, with the camp of Midian north of them by the hill of Moreh in the valley.",
      "T": "Jerubbaal—the man they called Gideon—rose at dawn with all his men and made camp beside the spring of Harod. The Midianite horde lay to the north, at the foot of the hill of Moreh, down in the valley below."
    },
    "2": {
      "L": "And the LORD said unto Gideon, The people that are with thee are too many for me to give the Midianites into their hands, lest Israel boast themselves against me, saying, Mine own hand hath saved me.",
      "M": "The LORD said to Gideon, “The people with you are too many for me to give Midian into their hands, lest Israel boast against me, saying, 'My own hand has saved me.'”",
      "T": "The LORD said to Gideon, “You have too many men. If I hand Midian over to them now, Israel will take the credit and say, 'We won this by our own strength'—and I will not share my glory with human pride.”"
    },
    "3": {
      "L": "Now therefore proclaim thou in the ears of the people, saying, Whosoever is fearful and afraid, let him return and depart early from mount Gilead. And there returned of the people twenty and two thousand; and there remained ten thousand.",
      "M": "Now therefore proclaim to the people, 'Whoever is fearful and trembling, let him turn back and depart from Mount Gilead.'“ And twenty-two thousand of the people turned back, and ten thousand remained.",
      "T": "So Gideon made the announcement: “If any man here is frightened or anxious, he may go home from Mount Gilead right now.” Twenty-two thousand walked away. Only ten thousand remained."
    },
    "4": {
      "L": "And the LORD said unto Gideon, The people are yet too many; bring them down unto the water, and I will try them for thee there: and it shall be, that of whom I say unto thee, This shall go with thee, the same shall go with thee; and of whomsoever I say unto thee, This shall not go with thee, the same shall not go.",
      "M": "The LORD said to Gideon, “The people are still too many. Bring them down to the water, and I will test them for you there. Of whoever I say to you, 'This one shall go with you,' he shall go with you; and whoever I say, 'This one shall not go with you,' he shall not go.”",
      "T": "Still the LORD said, “There are too many. Bring them down to the water and I will winnow them there. I will tell you who goes and who turns back.”"
    },
    "5": {
      "L": "So he brought down the people unto the water: and the LORD said unto Gideon, Every one that lappeth of the water with his tongue, as a dog lappeth, him shalt thou set by himself; likewise every one that boweth down upon his knees to drink.",
      "M": "So he brought the people down to the water. And the LORD said to Gideon, “Set apart everyone who laps the water with his tongue like a dog from everyone who kneels down to drink.”",
      "T": "Gideon brought the men to the water. The LORD said: “Separate those who lap up water with their tongues like a dog from those who kneel down to drink.”"
    },
    "6": {
      "L": "And the number of them that lapped, putting their hand to their mouth, was three hundred men: but all the rest of the people bowed down upon their knees to drink water.",
      "M": "The number of those who lapped, cupping water to their mouths with their hands, was three hundred men; but all the rest of the people knelt down to drink.",
      "T": "Three hundred men lapped water by scooping it up to their mouths with their hands. All the rest knelt down to drink."
    },
    "7": {
      "L": "And the LORD said unto Gideon, By the three hundred men that lapped will I save you, and deliver the Midianites into thine hand: and let all the other people go every man unto his place.",
      "M": "The LORD said to Gideon, “With the three hundred men who lapped I will save you and give the Midianites into your hand. Let all the other people go, each to his place.”",
      "T": "The LORD said to Gideon, “These three hundred who lapped—with them I will deliver you, and I will give Midian into your hands. Send all the others home.”"
    },
    "8": {
      "L": "So the people took victuals in their hand, and their trumpets: and he sent all the rest of Israel every man unto his tent, and retained those three hundred men: and the host of Midian was beneath him in the valley.",
      "M": "So the three hundred men took the people's provisions and their trumpets in their hands. And Gideon sent all the rest of Israel each to his tent, but kept the three hundred men. The camp of Midian was below him in the valley.",
      "T": "The three hundred men took the food and the trumpets of those who left. Gideon dismissed the rest of Israel to their tents and kept only his three hundred. Down in the valley the Midianite camp spread out before them."
    },
    "9": {
      "L": "And it came to pass the same night, that the LORD said unto him, Arise, get thee down unto the host; for I have delivered it into thine hand.",
      "M": "That same night the LORD said to him, “Arise, go down against the camp, for I have given it into your hand.”",
      "T": "That night the LORD spoke again: “Get up and go down to the camp. I have given it into your hand.”"
    },
    "10": {
      "L": "But if thou fear to go down, go thou with Phurah thy servant down to the host:",
      "M": "But if you are afraid to go down, go down with Purah your servant to the camp,",
      "T": "But if fear holds you back, take Purah your servant and go down to the camp together."
    },
    "11": {
      "L": "And thou shalt hear what they say; and afterward shall thine hands be strengthened to go down unto the host. Then went he down with Phurah his servant unto the outside of the armed men that were in the host.",
      "M": "And you shall hear what they say, and afterward your hands will be strengthened to go down against the camp.“ So he went down with Purah his servant to the outposts of the armed men in the camp.",
      "T": "Listen to what they are saying, and it will give you the courage you need.“ So Gideon slipped down with Purah to the edge of the enemy camp, where the sentinels stood."
    },
    "12": {
      "L": "And the Midianites and the Amalekites and all the children of the east lay along in the valley like grasshoppers for multitude; and their camels were without number, as the sand by the sea side for multitude.",
      "M": "And the Midianites and the Amalekites and all the people of the East lay along the valley like locusts in abundance, and their camels were without number, as numerous as the sand on the seashore.",
      "T": "The Midianites, Amalekites, and all the eastern peoples blanketed the valley like a swarm of locusts. Their camels were beyond counting—as many as grains of sand on the shore."
    },
    "13": {
      "L": "And when Gideon was come, behold, there was a man that told a dream unto his fellow, and said, Behold, I dreamed a dream, and, lo, a cake of barley bread tumbled into the host of Midian, and came unto a tent, and smote it that it fell, and overturned it, that the tent lay along.",
      "M": "When Gideon arrived, a man was telling his companion a dream: “Behold, I dreamed a dream, and a loaf of barley bread came tumbling into the camp of Midian and struck a tent so that it fell and was turned upside down, so that the tent collapsed.”",
      "T": "As Gideon arrived, he heard one soldier telling another about a dream: “I dreamed that a loaf of barley bread went rolling down into our camp. It struck a tent and the whole thing collapsed flat.”"
    },
    "14": {
      "L": "And his fellow answered and said, This is nothing else save the sword of Gideon the son of Joash, a man of Israel: for into his hand hath God delivered Midian, and all the host.",
      "M": "And his companion answered, “This is nothing other than the sword of Gideon the son of Joash, a man of Israel. God has given into his hand Midian and all the camp.”",
      "T": "His companion answered, “That can only mean one thing—the sword of Gideon son of Joash, the Israelite. God has handed Midian and this whole army over to him.”"
    },
    "15": {
      "L": "And it was so, when Gideon heard the telling of the dream, and the interpretation thereof, that he worshipped, and returned into the host of Israel, and said, Arise; for the LORD hath delivered into your hand the host of Midian.",
      "M": "When Gideon heard the telling of the dream and its interpretation, he worshiped. And he returned to the camp of Israel and said, “Arise, for the LORD has given the host of Midian into your hand.”",
      "T": "The moment Gideon heard the dream and its meaning, he bowed and worshiped. Then he hurried back to the Israelite camp and called out, “On your feet! The LORD has given the Midianite army into our hands!”"
    },
    "16": {
      "L": "And he divided the three hundred men into three companies, and he put a trumpet in every man's hand, with empty pitchers, and lamps within the pitchers.",
      "M": "And he divided the three hundred men into three companies and put a trumpet in every man's hand, along with empty jars, with torches inside the jars.",
      "T": "He split his three hundred men into three groups, giving each man a trumpet and an empty clay jar with a torch hidden inside."
    },
    "17": {
      "L": "And he said unto them, Look on me, and do likewise: and, behold, when I come to the outside of the camp, it shall be that, as I do, so shall ye do.",
      "M": "And he said to them, “Watch me and do likewise. When I come to the outskirts of the camp, do as I do.”",
      "T": "He told them, “Watch me and follow my lead exactly. When I reach the edge of the camp, do whatever I do.”"
    },
    "18": {
      "L": "When I blow with a trumpet, I and all that are with me, then blow ye the trumpets also on every side of all the camp, and say, The sword of the LORD, and of Gideon.",
      "M": "When I and all who are with me blow the trumpet, you also blow the trumpets all around the camp and shout, 'For the LORD and for Gideon!'",
      "T": "The moment I blow my trumpet—and all my men blow theirs—you blow yours from every side of the camp and shout: 'The sword of the LORD and of Gideon!'"
    },
    "19": {
      "L": "So Gideon, and the hundred men that were with him, came unto the outside of the camp in the beginning of the middle watch; and they had but newly set the watch: and they blew the trumpets, and brake the pitchers that were in their hands.",
      "M": "So Gideon and the hundred men who were with him came to the outskirts of the camp at the beginning of the middle watch, when the guards had just been posted. They blew the trumpets and smashed the jars they had in their hands.",
      "T": "Gideon and his hundred men reached the edge of the camp at the start of the middle watch—just when the sentries had been changed. All at once they blew their trumpets and shattered the jars."
    },
    "20": {
      "L": "And the three companies blew the trumpets, and brake the pitchers, and held the lamps in their left hands, and the trumpets in their right hands to blow withal: and they cried, The sword of the LORD, and of Gideon.",
      "M": "The three companies blew the trumpets and broke the jars. They held the torches in their left hands and the trumpets in their right hands to blow, and they cried out, “A sword for the LORD and for Gideon!”",
      "T": "All three groups blew their trumpets and smashed their jars simultaneously. Torches blazed in their left hands, trumpets roared from their right, and they all cried out: “The sword of the LORD and of Gideon!”"
    },
    "21": {
      "L": "And they stood every man in his place round about the camp: and all the host ran, and cried, and fled.",
      "M": "Every man stood in his place around the camp, and all the host ran; they cried out and fled.",
      "T": "Every man held his position all around the camp. Inside, panic broke out—the Midianites screamed and fled in every direction."
    },
    "22": {
      "L": "And the three hundred blew the trumpets, and the LORD set every man's sword against his fellow, even throughout all the host: and the host fled to Bethshittah in Zererath, and to the border of Abelmeholah, unto Tabbath.",
      "M": "When the three hundred trumpets blew, the LORD set every man's sword against his fellow throughout all the camp. And the army fled to Beth-shittah toward Zererah, as far as the border of Abel-meholah, by Tabbath.",
      "T": "As the three hundred trumpets rang out, the LORD turned the Midianite soldiers against each other—swords flashing in their own camp. The survivors fled all the way to Beth-shittah and Zererah, on to the border of Abel-meholah near Tabbath."
    },
    "23": {
      "L": "And the men of Israel gathered themselves together out of Naphtali, and out of Asher, and out of all Manasseh, and pursued after the Midianites.",
      "M": "And the men of Israel were called out from Naphtali, and from Asher, and from all Manasseh, and they pursued the Midianites.",
      "T": "Warriors from Naphtali, Asher, and all Manasseh rallied and joined the pursuit of the fleeing Midianites."
    },
    "24": {
      "L": "And Gideon sent messengers throughout all mount Ephraim, saying, Come down against the Midianites, and take before them the waters unto Bethbarah and Jordan. Then all the men of Ephraim gathered themselves together, and took the waters unto Bethbarah and Jordan.",
      "M": "Gideon also sent messengers throughout all the hill country of Ephraim, saying, “Come down against the Midianites and hold the waters against them as far as Beth-barah and the Jordan.” So all the men of Ephraim were called out and they seized the waters as far as Beth-barah and the Jordan.",
      "T": "Gideon sent messengers throughout the Ephraimite highlands: “Come down! Cut off the Midianites at the fords—hold the waters of Beth-barah and the Jordan against them!” The men of Ephraim mustered and seized those crossing points."
    },
    "25": {
      "L": "And they took two princes of the Midianites, Oreb and Zeeb; and they slew Oreb upon the rock Oreb, and Zeeb they slew at the winepress of Zeeb, and pursued Midian, and brought the heads of Oreb and Zeeb to Gideon on the other side Jordan.",
      "M": "They captured the two princes of Midian, Oreb and Zeeb. They killed Oreb at the rock of Oreb and Zeeb at the winepress of Zeeb, and they pursued Midian. And they brought the heads of Oreb and Zeeb to Gideon beyond the Jordan.",
      "T": "They captured the two Midianite warlords, Oreb and Zeeb—killing Oreb at the rock that now bears his name, and Zeeb at the winepress that bears his. They pressed on after the Midianite army and brought the heads of Oreb and Zeeb to Gideon across the Jordan."
    }
  },
  "8": {
    "1": {
      "L": "And the men of Ephraim said unto him, Why hast thou served us thus, that thou calledst us not, when thou wentest to fight with the Midianites? And they did chide with him sharply.",
      "M": "And the men of Ephraim said to him, “What is this that you have done to us, not to call us when you went to fight against Midian?” And they accused him fiercely.",
      "T": "The men of Ephraim confronted Gideon angrily: “Why didn't you call us when you went to fight Midian? What kind of slight is this?” They were furious."
    },
    "2": {
      "L": "And he said unto them, What have I done now in comparison of you? Is not the gleaning of the grapes of Ephraim better than the vintage of Abiezer?",
      "M": "He said to them, “What have I accomplished in comparison with you? Is not the gleaning of the grapes of Ephraim better than the full vintage of Abiezer?”",
      "T": "Gideon answered them gently: “What have I done compared to you? Even the leftover grapes of Ephraim are better than the entire harvest of Abiezer.”"
    },
    "3": {
      "L": "God hath delivered into your hands the princes of Midian, Oreb and Zeeb: and what was I able to do in comparison of you? Then their anger was abated toward him, when he had said that.",
      "M": "God has given into your hands the princes of Midian, Oreb and Zeeb. What was I able to do compared to you?“ Their anger toward him subsided when he said this.",
      "T": "God gave you the Midianite princes—Oreb and Zeeb! What I did is nothing beside that.“ At these words their anger cooled."
    },
    "4": {
      "L": "And Gideon came to Jordan, and passed over, he and the three hundred men that were with him, faint, yet pursuing them.",
      "M": "And Gideon came to the Jordan and crossed over, he and the three hundred men with him, exhausted yet still pursuing.",
      "T": "Gideon reached the Jordan and crossed it with his three hundred men—every one of them spent and hungry, but still pressing forward."
    },
    "5": {
      "L": "And he said unto the men of Succoth, Give, I pray you, loaves of bread unto the people that follow me; for they be faint, and I am pursuing after Zebah and Zalmunna, kings of Midian.",
      "M": "And he said to the men of Succoth, “Please give loaves of bread to the people who follow me, for they are exhausted, and I am pursuing Zebah and Zalmunna, the kings of Midian.”",
      "T": "He asked the people of Succoth, “Give my men some bread—they are exhausted. I am still chasing Zebah and Zalmunna, the kings of Midian.”"
    },
    "6": {
      "L": "And the princes of Succoth said, Are the hands of Zebah and Zalmunna now in thine hand, that we should give bread unto thine army?",
      "M": "But the officials of Succoth said, “Are the hands of Zebah and Zalmunna already in your hand, that we should give bread to your army?”",
      "T": "The leaders of Succoth refused: “Have you already caught Zebah and Zalmunna? Why should we feed an army that hasn't won yet?”"
    },
    "7": {
      "L": "And Gideon said, Therefore when the LORD hath delivered Zebah and Zalmunna into mine hand, then I will tear your flesh with the thorns of the wilderness and with briers.",
      "M": "And Gideon said, “Very well. When the LORD has given Zebah and Zalmunna into my hand, I will flail your flesh with the thorns of the wilderness and with briers.”",
      "T": "Gideon replied, “So be it. When the LORD delivers Zebah and Zalmunna into my hand, I will come back and thresh your flesh with desert thorns and briers.”"
    },
    "8": {
      "L": "And he went up thence to Penuel, and spake unto them likewise: and the men of Penuel answered him as the men of Succoth had answered him.",
      "M": "From there he went up to Penuel and spoke to them in the same way, and the men of Penuel answered him just as the men of Succoth had.",
      "T": "He went on to Penuel and made the same request. The people of Penuel gave him the same cold refusal as Succoth."
    },
    "9": {
      "L": "And he spake also unto the men of Penuel, saying, When I come again in peace, I will break down this tower.",
      "M": "And he also said to the men of Penuel, “When I return in peace, I will break down this tower.”",
      "T": "To the men of Penuel he said, “When I come back victorious, I will pull this tower down.”"
    },
    "10": {
      "L": "Now Zebah and Zalmunna were in Karkor, and their hosts with them, about fifteen thousand men, all that were left of all the hosts of the children of the east: for there fell an hundred and twenty thousand men that drew sword.",
      "M": "Now Zebah and Zalmunna were at Karkor with their forces, about fifteen thousand men—all who were left of the entire army of the people of the East—for one hundred and twenty thousand soldiers who drew the sword had fallen.",
      "T": "Zebah and Zalmunna had regrouped at Karkor with about fifteen thousand men—the remnant of the eastern armies. One hundred and twenty thousand had already fallen in battle."
    },
    "11": {
      "L": "And Gideon went up by the way of them that dwelt in tents on the east of Nobah and Jogbehah, and smote the host: for the host was secure.",
      "M": "And Gideon went up by the route of the tent-dwellers east of Nobah and Jogbehah, and attacked the army, for the army was off guard.",
      "T": "Gideon came at them by the nomads' road east of Nobah and Jogbehah and struck the army when they were least expecting it."
    },
    "12": {
      "L": "And when Zebah and Zalmunna fled, he pursued after them, and took the two kings of Midian, Zebah and Zalmunna, and discomfited all the host.",
      "M": "When Zebah and Zalmunna fled, he pursued them and captured the two kings of Midian, Zebah and Zalmunna, throwing the whole army into a panic.",
      "T": "Zebah and Zalmunna tried to flee, but Gideon ran them down and captured both kings. The entire army was thrown into chaos."
    },
    "13": {
      "L": "And Gideon the son of Joash returned from battle before the sun was up.",
      "M": "And Gideon the son of Joash returned from battle by the ascent of Heres.",
      "T": "Then Gideon son of Joash made his way back from battle by the pass of Heres."
    },
    "14": {
      "L": "And caught a young man of the men of Succoth, and enquired of him: and he described unto him the princes of Succoth, and the elders thereof, even threescore and seventeen men.",
      "M": "And he captured a young man of Succoth and questioned him. The young man wrote down for him the officials and elders of Succoth, seventy-seven men.",
      "T": "He seized a young man from Succoth and interrogated him. The young man wrote out the names of Succoth's leaders and elders—seventy-seven in all."
    },
    "15": {
      "L": "And he came unto the men of Succoth, and said, Behold Zebah and Zalmunna, with whom ye did upbraid me, saying, Are the hands of Zebah and Zalmunna now in thine hand, that we should give bread unto thy men that are weary?",
      "M": "And he came to the men of Succoth and said, “Behold Zebah and Zalmunna, about whom you taunted me, saying, 'Are the hands of Zebah and Zalmunna already in your hand, that we should give bread to your weary men?'”",
      "T": "Gideon returned to the men of Succoth and said, “Here they are—Zebah and Zalmunna. You mocked me: 'Have you actually caught them yet? Why should we feed your exhausted men?' Well?”"
    },
    "16": {
      "L": "And he took the elders of the city, and thorns of the wilderness and briers, and with them he taught the men of Succoth.",
      "M": "And he took the elders of the city and the thorns of the wilderness and briers, and with them he taught the men of Succoth a lesson.",
      "T": "He seized the elders of the city and, using desert thorns and briers, he gave the men of Succoth the punishment he had promised."
    },
    "17": {
      "L": "And he beat down the tower of Penuel, and slew the men of the city.",
      "M": "And he tore down the tower of Penuel and killed the men of the city.",
      "T": "Then he marched to Penuel, pulled down their tower, and put the men of the city to death."
    },
    "18": {
      "L": "Then said he unto Zebah and Zalmunna, What manner of men were they whom ye slew at Tabor? And they answered, As thou art, so were they; each one resembled the children of a king.",
      "M": "Then he said to Zebah and Zalmunna, “What kind of men were those you killed at Tabor?” They answered, “They were like you—every one of them had the bearing of a king's son.”",
      "T": "Then Gideon turned to the two captured kings: “Describe the men you killed at Tabor.” They said, “They looked exactly like you—each one carried himself like a king's son.”"
    },
    "19": {
      "L": "And he said, They were my brethren, even the sons of my mother: as the LORD liveth, if ye had saved them alive, I would not slay you.",
      "M": "And he said, “They were my brothers, the sons of my own mother. As the LORD lives, if you had let them live, I would not kill you.”",
      "T": "He said quietly, “Those were my brothers—my own mother's sons. I swear by the LORD's life: if you had spared them, I would have spared you.”"
    },
    "20": {
      "L": "And he said unto Jether his firstborn, Up, and slay them. But the youth drew not his sword: for he feared, because he was yet a youth.",
      "M": "And he said to Jether his firstborn, “Rise and kill them!” But the young man did not draw his sword, for he was afraid, because he was still a youth.",
      "T": "He turned to his eldest son, Jether: “Kill them.” But Jether could not move—he was still just a boy and fear gripped him."
    },
    "21": {
      "L": "Then Zebah and Zalmunna said, Rise thou, and fall upon us: for as the man is, so is his strength. And Gideon arose, and slew Zebah and Zalmunna, and took away the ornaments that were on their camels' necks.",
      "M": "Then Zebah and Zalmunna said, “Rise yourself and fall upon us, for as the man is, so is his strength.” So Gideon arose and killed Zebah and Zalmunna, and he took the crescent ornaments that were on their camels' necks.",
      "T": "So the two kings taunted Gideon: “Do it yourself. A man's strength matches his manhood.” Gideon stepped forward and killed them, then stripped the golden crescent ornaments from their camels' necks."
    },
    "22": {
      "L": "Then the men of Israel said unto Gideon, Rule thou over us, both thou, and thy son, and thy son's son also: for thou hast delivered us from the hand of Midian.",
      "M": "Then the men of Israel said to Gideon, “Rule over us—you and your son and your grandson also—for you have saved us from the hand of Midian.”",
      "T": "The men of Israel came to Gideon: “Be our king—you and your sons after you. You have rescued us from Midian's grip.”"
    },
    "23": {
      "L": "And Gideon said unto them, I will not rule over you, neither shall my son rule over you: the LORD shall rule over you.",
      "M": "But Gideon said to them, “I will not rule over you, and my son will not rule over you; the LORD will rule over you.”",
      "T": "Gideon refused: “I will not be your king, and neither will any of my sons. The LORD is your king.”"
    },
    "24": {
      "L": "And Gideon said unto them, I would desire a request of you, that ye would give me every man the earrings of his prey. (For they had golden earrings, because they were Ishmaelites.)",
      "M": "And Gideon said to them, “Let me make one request of you: give me each man an earring from his plunder.” (For they had golden earrings, because they were Ishmaelites.)",
      "T": "But he did ask one thing: “Let every man give me a gold earring from his plunder.” (The Midianites, being Ishmaelites, wore gold earrings.)"
    },
    "25": {
      "L": "And they answered, We will willingly give them. And they spread a garment, and did cast therein every man the earrings of his prey.",
      "M": "And they answered, “We will gladly give them.” And they spread out a garment, and each man threw the earrings of his plunder into it.",
      "T": "They agreed eagerly. They spread out a cloak and each man threw in the gold earrings he had taken."
    },
    "26": {
      "L": "And the weight of the golden earrings that he requested was a thousand and seven hundred shekels of gold; beside ornaments, and collars, and purple raiment that was on the kings of Midian, and beside the chains that were about their camels' necks.",
      "M": "The weight of the golden earrings that he requested was seventeen hundred shekels of gold, besides the crescent ornaments and pendants and the purple garments worn by the kings of Midian, and besides the collars that were around their camels' necks.",
      "T": "The gold earrings alone weighed seventeen hundred shekels—not counting the crescent ornaments, the pendants, the royal purple robes worn by the kings of Midian, or the golden chains around their camels' necks."
    },
    "27": {
      "L": "And Gideon made an ephod thereof, and put it in his city, even in Ophrah: and all Israel went a whoring after it there; which thing became a snare unto Gideon, and to his house.",
      "M": "And Gideon made an ephod from it and placed it in his city, in Ophrah. And all Israel committed spiritual adultery after it there, and it became a snare to Gideon and to his family.",
      "T": "With the gold Gideon made an ephod and set it up in his hometown of Ophrah. All Israel began venerating it there as a cult object—and it became a snare that trapped Gideon himself and his whole household. The man who tore down Baal's altar had built a new idol."
    },
    "28": {
      "L": "Thus was Midian subdued before the children of Israel, so that they lifted up their heads no more. And the country was in quietness forty years in the days of Gideon.",
      "M": "So Midian was subdued before the people of Israel, and they raised their heads no more. And the land had rest forty years in the days of Gideon.",
      "T": "So Midian was broken before Israel and never recovered. The land enjoyed forty years of peace throughout Gideon's lifetime."
    },
    "29": {
      "L": "And Jerubbaal the son of Joash went and dwelt in his own house.",
      "M": "And Jerubbaal the son of Joash went and lived in his own house.",
      "T": "Jerubbaal son of Joash retired to his own home."
    },
    "30": {
      "L": "And Gideon had threescore and ten sons of his body begotten: for he had many wives.",
      "M": "Now Gideon had seventy sons, his own offspring, for he had many wives.",
      "T": "Gideon had fathered seventy sons by his many wives."
    },
    "31": {
      "L": "And his concubine that was in Shechem, she also bare him a son, whose name he called Abimelech.",
      "M": "And his concubine who was in Shechem also bore him a son, whom he named Abimelech.",
      "T": "His concubine in Shechem bore him another son, whom he named Abimelech—a name that would cast a long shadow."
    },
    "32": {
      "L": "And Gideon the son of Joash died in a good old age, and was buried in the sepulchre of Joash his father, in Ophrah of the Abiezrites.",
      "M": "And Gideon the son of Joash died at a good old age and was buried in the tomb of his father Joash, at Ophrah of the Abiezrites.",
      "T": "Gideon son of Joash died at a ripe old age and was buried in the family tomb at Ophrah, in the territory of the Abiezrites."
    },
    "33": {
      "L": "And it came to pass, as soon as Gideon was dead, that the children of Israel turned again, and went a whoring after Baalim, and made Baalberith their god.",
      "M": "As soon as Gideon died, the people of Israel turned again and committed spiritual adultery after the Baals, making Baal-berith their god.",
      "T": "No sooner was Gideon in the grave than Israel turned back to the Baals, making Baal-berith—the Canaanite god of covenants—their deity."
    },
    "34": {
      "L": "And the children of Israel remembered not the LORD their God, who had delivered them out of the hands of all their enemies on every side:",
      "M": "And the people of Israel did not remember the LORD their God, who had delivered them from the hand of all their enemies on every side,",
      "T": "They forgot the LORD their God—the one who had rescued them from every enemy surrounding them."
    },
    "35": {
      "L": "Neither shewed they kindness to the house of Jerubbaal, namely, Gideon, according to all the goodness which he had shewed unto Israel.",
      "M": "and they did not show faithful kindness to the family of Jerubbaal—that is, Gideon—in return for all the good that he had done for Israel.",
      "T": "Nor did they show any steadfast loyal love to Gideon's family—no gratitude for all the good he had done for Israel."
    }
  },
  "9": {
    "1": {
      "L": "And Abimelech the son of Jerubbaal went to Shechem unto his mother's brethren, and communed with them, and with all the family of the house of his mother's father, saying,",
      "M": "Abimelech the son of Jerubbaal went to Shechem to his mother's relatives and spoke with them and with the whole clan of his mother's family, saying,",
      "T": "Abimelech son of Jerubbaal went to Shechem, where his mother's family lived, and met with all her relatives, saying to them:"
    },
    "2": {
      "L": "Speak, I pray you, in the ears of all the men of Shechem, Whether is better for you, either that all the sons of Jerubbaal, which are threescore and ten persons, reign over you, or that one reign over you? remember also that I am your bone and your flesh.",
      "M": "“Please speak in the hearing of all the men of Shechem: which is better for you—that all seventy sons of Jerubbaal rule over you, or that one man rule over you? And remember, I am your own flesh and blood.”",
      "T": "“Say this to all the citizens of Shechem: 'Is it better to be ruled by seventy of Gideon's sons, or by one man? And remember—my mother is one of you. I am your blood.”"
    },
    "3": {
      "L": "And his mother's brethren spake of him all these words in the ears of all the men of Shechem: and their hearts inclined to follow Abimelech; for they said, He is our brother.",
      "M": "And his mother's relatives spoke all these words on his behalf in the hearing of all the men of Shechem, and their hearts inclined to follow Abimelech, for they said, “He is our brother.”",
      "T": "His mother's family passed the message along to all the leaders of Shechem, and the people's loyalties shifted toward Abimelech. “He is one of us,” they said."
    },
    "4": {
      "L": "And they gave him threescore and ten pieces of silver out of the house of Baalberith, wherewith Abimelech hired vain and light persons, which followed him.",
      "M": "And they gave him seventy pieces of silver from the house of Baal-berith, with which Abimelech hired worthless and reckless men, who followed him.",
      "T": "From the treasury of Baal-berith—the god of covenants—they gave him seventy pieces of silver. With that money, Abimelech hired a band of desperate, reckless men as his followers. Covenant funds bought a covenant-breaker's army."
    },
    "5": {
      "L": "And he went unto his father's house at Ophrah, and slew his brethren the sons of Jerubbaal, being threescore and ten persons, upon one stone: notwithstanding yet Jotham the youngest son of Jerubbaal was left; for he hid himself.",
      "M": "And he went to his father's house at Ophrah and killed his brothers, the sons of Jerubbaal—seventy men—on one stone. But Jotham the youngest son of Jerubbaal escaped, for he had hidden himself.",
      "T": "Then he went to his father's home at Ophrah and murdered seventy of his brothers—Gideon's sons—one by one on a single stone. Only the youngest, Jotham, survived, because he had hidden himself."
    },
    "6": {
      "L": "And all the men of Shechem gathered together, and all the house of Millo, and went, and made Abimelech king, by the plain of the pillar that was in Shechem.",
      "M": "And all the men of Shechem and all Beth-millo gathered together and went and made Abimelech king, by the oak of the pillar at Shechem.",
      "T": "Then all the citizens of Shechem and the people of Beth-millo assembled and crowned Abimelech king beside the great oak at the sacred pillar in Shechem."
    },
    "7": {
      "L": "And when they told it to Jotham, he went and stood in the top of mount Gerizim, and lifted up his voice, and cried, and said unto them, Hearken unto me, ye men of Shechem, that God may hearken unto you.",
      "M": "When this was told to Jotham, he went and stood on the top of Mount Gerizim and called out in a loud voice and said to them, “Listen to me, you men of Shechem, that God may listen to you.”",
      "T": "When Jotham heard what had been done, he climbed to the summit of Mount Gerizim and cried out in a loud voice: “Listen to me, men of Shechem—if you want God to hear you, hear me first!”"
    },
    "8": {
      "L": "The trees went forth on a time to anoint a king over them; and they said unto the olive tree, Reign thou over us.",
      "M": "The trees once went out to anoint a king over themselves, and they said to the olive tree, 'Reign over us.'",
      "T": "Once upon a time the trees decided to anoint a king.\nThey went to the olive tree first: 'Come, be our king.'"
    },
    "9": {
      "L": "But the olive tree said unto them, Should I leave my fatness, wherewith by me they honour God and man, and go to be promoted over the trees?",
      "M": "But the olive tree said to them, 'Shall I leave my rich oil by which God and men are honored, and go to sway over the trees?'",
      "T": "But the olive tree said:\n'Should I give up my oil—the oil that honors gods and mortals alike—\njust to go and lord it over the trees?'"
    },
    "10": {
      "L": "And the trees said to the fig tree, Come thou, and reign over us.",
      "M": "And the trees said to the fig tree, 'You come and reign over us.'",
      "T": "So the trees turned to the fig tree: 'Come, you be our king.'"
    },
    "11": {
      "L": "But the fig tree said unto them, Should I forsake my sweetness, and my good fruit, and go to be promoted over the trees?",
      "M": "But the fig tree said to them, 'Shall I give up my sweetness and my good fruit, and go to sway over the trees?'",
      "T": "But the fig tree said:\n'Should I abandon my sweetness and my good fruit\nto go and rule over the trees?'"
    },
    "12": {
      "L": "Then said the trees unto the vine, Come thou, and reign over us.",
      "M": "Then the trees said to the vine, 'You come and reign over us.'",
      "T": "Then the trees went to the vine: 'Come, you rule over us.'"
    },
    "13": {
      "L": "And the vine said unto them, Should I leave my wine, which cheereth God and man, and go to be promoted over the trees?",
      "M": "And the vine said to them, 'Shall I give up my wine that cheers God and men, and go to sway over the trees?'",
      "T": "But the vine said:\n'Should I leave my wine—the wine that gladdens both gods and mortals—\nto go swaying over the other trees?'"
    },
    "14": {
      "L": "Then said all the trees unto the bramble, Come thou, and reign over us.",
      "M": "Then all the trees said to the bramble, 'You come and reign over us.'",
      "T": "At last all the trees turned to the thornbush: 'Come then—you be our king.'"
    },
    "15": {
      "L": "And the bramble said unto the trees, If in truth ye anoint me king over you, then come and put your trust in my shadow: and if not, let fire come out of the bramble, and devour the cedars of Lebanon.",
      "M": "And the bramble said to the trees, 'If you truly anoint me king over you, then come and take refuge in my shade; but if not, let fire come out of the bramble and devour the cedars of Lebanon.'",
      "T": "And the thornbush replied:\n'If you really mean to anoint me your king, then come shelter under my shade!\nBut if you're not in earnest—let fire burst from this thornbush and consume the cedars of Lebanon.'"
    },
    "16": {
      "L": "Now therefore, if ye have done truly and sincerely, in that ye have made Abimelech king, and if ye have dealt well with Jerubbaal and his house, and have done unto him according to the deserving of his hands;",
      "M": "Now therefore, if you acted in good faith and sincerity when you made Abimelech king, and if you have dealt well with Jerubbaal and his house and treated him according to what his deeds deserved—",
      "T": "Now hear me out: if you acted in genuine good faith when you made Abimelech king—if you have dealt honorably with the family of Jerubbaal and given him what his service deserved—"
    },
    "17": {
      "L": "(For my father fought for you, and adventured his life far, and delivered you out of the hand of Midian:",
      "M": "(for my father fought for you and risked his life to the full and delivered you from the hand of Midian,",
      "T": "(my father fought for you and threw his life into the balance, and he delivered you from Midian's hand—"
    },
    "18": {
      "L": "And ye are risen up against my father's house this day, and have slain his sons, threescore and ten persons, upon one stone, and have made Abimelech, the son of his maidservant, king over the men of Shechem, because he is your brother;)",
      "M": "yet you have risen up against my father's house today and have killed his sons, seventy men, on one stone, and have made Abimelech, the son of his female servant, king over the men of Shechem, because he is your relative)",
      "T": "yet today you have risen up against his family, butchered seventy of his sons on a single stone, and crowned a slave-woman's son king over Shechem—simply because he shares your blood)"
    },
    "19": {
      "L": "If ye then have dealt truly and sincerely with Jerubbaal and with his house this day, then rejoice ye in Abimelech, and let him also rejoice in you:",
      "M": "—if you have in fact acted in good faith and sincerity with Jerubbaal and his house this day, then rejoice in Abimelech, and let him also rejoice in you.",
      "T": "—then, if your conscience is clear, enjoy your king and let him enjoy you."
    },
    "20": {
      "L": "But if not, let fire come out from Abimelech, and devour the men of Shechem, and the house of Millo; and let fire come out from the men of Shechem, and from the house of Millo, and devour Abimelech.",
      "M": "But if not, let fire come out from Abimelech and devour the men of Shechem and Beth-millo; and let fire come out from the men of Shechem and from Beth-millo and devour Abimelech.",
      "T": "But if not—if your conscience knows better—then let fire blaze out from Abimelech and burn up Shechem and Beth-millo, and let fire burst from Shechem and Beth-millo and consume Abimelech."
    },
    "21": {
      "L": "And Jotham ran away, and fled, and went to Beer, and dwelt there, for fear of Abimelech his brother.",
      "M": "And Jotham ran away and fled to Beer, and he lived there for fear of Abimelech his brother.",
      "T": "Then Jotham fled and ran for his life to Beer, where he stayed in hiding, afraid of his brother Abimelech."
    },
    "22": {
      "L": "When Abimelech had reigned three years over Israel,",
      "M": "When Abimelech had ruled over Israel for three years,",
      "T": "Three years into Abimelech's reign over Israel,"
    },
    "23": {
      "L": "Then God sent an evil spirit between Abimelech and the men of Shechem; and the men of Shechem dealt treacherously with Abimelech:",
      "M": "God sent an evil spirit between Abimelech and the men of Shechem, and the men of Shechem dealt treacherously with Abimelech.",
      "T": "God sent an evil spirit to sow discord between Abimelech and the people of Shechem. The Shechemites began to act in bad faith against him."
    },
    "24": {
      "L": "That the cruelty done to the threescore and ten sons of Jerubbaal might come, and their blood be laid upon Abimelech their brother, which slew them; and upon the men of Shechem, which aided him in the killing of his brethren.",
      "M": "This was so that the violence done to the seventy sons of Jerubbaal might come to account, and their blood be charged to Abimelech their brother who killed them, and to the men of Shechem who aided him in killing his brothers.",
      "T": "God's purpose: that the blood of Gideon's seventy sons would be avenged—the guilt falling on Abimelech who killed them, and on the men of Shechem who made it possible."
    },
    "25": {
      "L": "And the men of Shechem set liers in wait for him in the top of the mountains, and they robbed all that came along that way by them: and it was told Abimelech.",
      "M": "And the men of Shechem put men in ambush against him on the mountaintops, and they robbed all who passed by them along that way. And it was reported to Abimelech.",
      "T": "The men of Shechem planted ambushes on the hilltops and began raiding every caravan that passed. Word reached Abimelech."
    },
    "26": {
      "L": "And Gaal the son of Ebed came with his brethren, and went over to Shechem: and the men of Shechem put their confidence in him.",
      "M": "And Gaal the son of Ebed moved into Shechem with his relatives, and the men of Shechem transferred their loyalty to him.",
      "T": "Then Gaal son of Ebed arrived in Shechem with his clan, and the Shechemites shifted their allegiance to him."
    },
    "27": {
      "L": "And they went out into the fields, and gathered their vineyards, and trode the grapes, and made merry, and went into the house of their god, and did eat and drink, and cursed Abimelech.",
      "M": "And they went out into the fields and gathered the grapes from their vineyards and trod them and held a festival. Then they went into the house of their god and ate and drank and cursed Abimelech.",
      "T": "During the harvest festival they went to their vineyards, pressed the grapes, held a celebration, went into the temple of their god—and over the wine began cursing Abimelech."
    },
    "28": {
      "L": "And Gaal the son of Ebed said, Who is Abimelech, and who is Shechem, that we should serve him? is not he the son of Jerubbaal? and Zebul his officer? serve the men of Hamor the father of Shechem: for why should we serve him?",
      "M": "And Gaal the son of Ebed said, “Who is Abimelech, and who is Shechem, that we should serve him? Is he not the son of Jerubbaal, and is not Zebul his deputy? Serve the men of Hamor the father of Shechem—but why should we serve him?”",
      "T": "Gaal son of Ebed called out: “Who is this Abimelech, and why does Shechem bow to him? He is just the son of Jerubbaal—a mercenary king—and Zebul is nothing but his flunkey! We are the true sons of Shechem, the sons of Hamor! Why should we serve this man?”"
    },
    "29": {
      "L": "And would to God this people were under my hand! then would I remove Abimelech. And he said to Abimelech, Increase thine army, and come out.",
      "M": "Would that this people were under my command! Then I would remove Abimelech. I would say to Abimelech, 'Increase your army and come out!'",
      "T": "If only this people were under my command—I would get rid of Abimelech! I would tell him: 'Bring all your men and come out and fight!'"
    },
    "30": {
      "L": "And when Zebul the ruler of the city heard the words of Gaal the son of Ebed, his anger was kindled.",
      "M": "When Zebul the governor of the city heard the words of Gaal the son of Ebed, his anger blazed.",
      "T": "Zebul, Abimelech's governor in the city, heard what Gaal had said and his anger flared."
    },
    "31": {
      "L": "And he sent messengers unto Abimelech privily, saying, Behold, Gaal the son of Ebed and his brethren be come to Shechem; and, behold, they fortify the city against thee.",
      "M": "And he sent messengers to Abimelech secretly, saying, “Behold, Gaal the son of Ebed and his relatives have come to Shechem, and they are stirring up the city against you.",
      "T": "He sent secret word to Abimelech: “Gaal son of Ebed has come to Shechem with his clan and is turning the whole city against you."
    },
    "32": {
      "L": "Now therefore up by night, thou and the people that is with thee, and lie in wait in the field:",
      "M": "Now therefore, set out by night, you and the people who are with you, and set an ambush in the field.",
      "T": "March tonight under cover of darkness—you and your men—and set an ambush in the fields."
    },
    "33": {
      "L": "And it shall be, that in the morning, as soon as the sun is up, thou shalt rise early, and set upon the city: and, behold, when he and the people that is with him come out against thee, then mayest thou do to them as thou shalt find occasion.",
      "M": "Then in the morning, as soon as the sun rises, rise early and rush upon the city. When he and the people with him come out against you, you may do to them whatever your hand finds to do.",
      "T": "At first light, attack the city. When Gaal and his men come out to meet you, do what needs to be done.“"
    },
    "34": {
      "L": "And Abimelech rose up, and all the people that were with him, by night, and they laid wait against Shechem in four companies.",
      "M": "So Abimelech and all the people with him rose by night and set an ambush against Shechem in four companies.",
      "T": "Abimelech moved that night with all his men, and they surrounded Shechem in four assault groups."
    },
    "35": {
      "L": "And Gaal the son of Ebed went out, and stood in the entering of the gate of the city: and Abimelech rose up, and the people that were with him, from lying in wait.",
      "M": "And Gaal the son of Ebed went out and stood at the entrance of the city gate, and Abimelech and the people with him rose from the ambush.",
      "T": "Gaal son of Ebed went out and took his position at the city gate—just as Abimelech and his forces rose from their hiding places."
    },
    "36": {
      "L": "And when Gaal saw the people, he said to Zebul, Behold, there come people down from the top of the mountains. And Zebul said unto him, Thou seest the shadow of the mountains as if they were men.",
      "M": "When Gaal saw the people, he said to Zebul, “Look, people are coming down from the mountaintops!” But Zebul said to him, “You are just seeing the shadow of the mountains—they look like men.”",
      "T": "Gaal looked up and said to Zebul, “Look—people are coming down from the hilltops!” Zebul said, “You're just seeing shadows on the hillside.”"
    },
    "37": {
      "L": "And Gaal spake again and said, See there come people down by the middle of the land, and another company come along by the plain of Meonenim.",
      "M": "Gaal spoke again and said, “Look, people are coming down from the center of the land, and one company is coming by way of the Diviners' Oak.”",
      "T": "Gaal looked again: “No—there's a column coming down from the center of the land, and another coming by the Diviners' Oak.”"
    },
    "38": {
      "L": "Then said Zebul unto him, Where is now thy mouth, wherewith thou saidst, Who is Abimelech, that we should serve him? is not this the people that thou hast despised? go out, I pray now, and fight with them.",
      "M": "Then Zebul said to him, “Where is your big talk now—when you said, 'Who is Abimelech, that we should serve him?' Is not this the very people you despised? Go out now and fight them!”",
      "T": "Then Zebul turned on him: “Now where are all your brave words? 'Who is Abimelech that we should serve him?' Well? There is the people you sneered at. Go out and fight them!”"
    },
    "39": {
      "L": "And Gaal went out before the men of Shechem, and fought with Abimelech.",
      "M": "And Gaal went out at the head of the men of Shechem and fought with Abimelech.",
      "T": "So Gaal led the Shechemites out to face Abimelech."
    },
    "40": {
      "L": "And Abimelech chased him, and he fled before him, and many were overthrown and wounded, even unto the entering of the gate.",
      "M": "And Abimelech chased him, and he fled before him, and many fell wounded all the way to the entrance of the gate.",
      "T": "Abimelech drove him back—Gaal fled, and his men fell wounded in heaps all the way to the city gate."
    },
    "41": {
      "L": "And Abimelech dwelt at Arumah: and Zebul thrust out Gaal and his brethren, that they should not dwell in Shechem.",
      "M": "And Abimelech took up residence at Arumah, and Zebul drove out Gaal and his relatives so that they could not remain in Shechem.",
      "T": "Abimelech pulled back to Arumah; Zebul expelled Gaal and his clan from Shechem permanently."
    },
    "42": {
      "L": "And it came to pass on the morrow, that the people went out into the field; and they told Abimelech.",
      "M": "The next day the people of Shechem went out into the field, and it was reported to Abimelech.",
      "T": "The next day the Shechemites went out to work their fields. Word came to Abimelech."
    },
    "43": {
      "L": "And he took the people, and divided them into three companies, and laid wait in the field, and looked, and, behold, the people were come forth out of the city; and he rose up against them, and smote them.",
      "M": "He took his men and divided them into three companies and set ambushes in the fields. He watched and saw the people coming out of the city, so he rose against them and struck them down.",
      "T": "He split his troops into three groups, set an ambush in the fields, and watched. When the Shechemites came out, he fell on them."
    },
    "44": {
      "L": "And Abimelech, and the company that was with him, rushed forward, and stood in the entering of the gate of the city: and the two other companies ran upon all the men that were in the fields, and slew them.",
      "M": "And Abimelech and the company with him rushed forward and stood at the entrance of the city gate, while the two other companies rushed on all who were in the fields and cut them down.",
      "T": "Abimelech's group charged the gate and held it, while the other two companies swept through the fields, killing everyone they found."
    },
    "45": {
      "L": "And Abimelech fought against the city all that day; and he took the city, and slew the people that was therein, and beat down the city, and sowed it with salt.",
      "M": "And Abimelech fought against the city all that day. He captured it and killed the people who were in it, and he razed the city and sowed it with salt.",
      "T": "Abimelech fought until the city fell. He killed its people, tore down every building, and salted the ruins—a cursing ritual, consecrating the ground to desolation."
    },
    "46": {
      "L": "And when all the men of the tower of Shechem heard that, they entered into an hold of the house of the god Berith.",
      "M": "When all the men of the Tower of Shechem heard of it, they entered the stronghold of the house of El-berith.",
      "T": "When the people of the Tower of Shechem heard what had happened, they retreated into the fortified temple of El-berith."
    },
    "47": {
      "L": "And it was told Abimelech, that all the men of the tower of Shechem were gathered together.",
      "M": "And it was reported to Abimelech that all the men of the Tower of Shechem had gathered together.",
      "T": "Abimelech was told that they had all taken refuge there."
    },
    "48": {
      "L": "And Abimelech gat him up to mount Zalmon, he and all the people that were with him; and Abimelech took an axe in his hand, and cut down a bough from the trees, and took it, and laid it upon his shoulder, and said unto the people that were with him, What ye have seen me do, make haste, and do as I have done.",
      "M": "And Abimelech went up to Mount Zalmon, he and all the people with him. Abimelech took an axe in his hand and cut down a bundle of brushwood and carried it up on his shoulder. And he said to the people with him, “What you have seen me do, hurry and do the same.”",
      "T": "Abimelech led his men up Mount Zalmon. He took an axe, cut a great bundle of brushwood, hoisted it onto his shoulder, and ordered his men: “Quickly—do exactly what I've done.”"
    },
    "49": {
      "L": "And all the people likewise cut down every man his bough, and followed Abimelech, and put them to the hold, and set the hold on fire upon them; so that all the men of the tower of Shechem died also, about a thousand men and women.",
      "M": "So every one of the people cut down his bundle and followed Abimelech and piled the branches against the stronghold and set it on fire over the people inside. So all the people of the Tower of Shechem died also, about one thousand men and women.",
      "T": "Every soldier cut his bundle and they piled the wood against the stronghold and set it ablaze. About a thousand men and women died in the fire—the entire population of the Tower of Shechem. Jotham's curse had begun its work."
    },
    "50": {
      "L": "Then went Abimelech to Thebez, and encamped against Thebez, and took it.",
      "M": "Then Abimelech went to Thebez and encamped against Thebez and captured it.",
      "T": "From there Abimelech marched to Thebez, besieged it, and took the town."
    },
    "51": {
      "L": "But there was a strong tower within the city, and thither fled all the men and women, and all they of the city, and shut it to them, and gat them up to the top of the tower.",
      "M": "But there was a strong tower within the city, and all the men and women and all the city leaders fled to it, shut themselves in, and climbed up to the roof.",
      "T": "But inside the town stood a strong tower. The whole population—men, women, and leaders alike—took refuge in it, locked the door, and climbed to the roof."
    },
    "52": {
      "L": "And Abimelech came unto the tower, and fought against it, and went hard unto the door of the tower to burn it with fire.",
      "M": "And Abimelech came to the tower and fought against it, and he approached the door of the tower to set it on fire.",
      "T": "Abimelech pressed his attack on the tower, approaching the door to burn it down."
    },
    "53": {
      "L": "And a certain woman cast a piece of a millstone upon Abimelech's head, and all to brake his skull.",
      "M": "But a woman dropped an upper millstone on Abimelech's head and cracked his skull.",
      "T": "Then a woman dropped the upper stone of a handmill from the roof onto Abimelech's head and shattered his skull."
    },
    "54": {
      "L": "Then he called hastily unto the young man his armourbearer, and said unto him, Draw thy sword, and slay me, that men say not of me, A woman slew him. And his young man thrust him through, and he died.",
      "M": "He quickly called to his armor-bearer and said, “Draw your sword and run me through, lest they say of me, 'A woman killed him.'” So his young man thrust him through, and he died.",
      "T": "He gasped to his armor-bearer, “Draw your sword and finish me—don't let them say a woman killed me.” So the young man drove his sword through him, and he died. He got what he demanded, though not what he deserved."
    },
    "55": {
      "L": "And when the men of Israel saw that Abimelech was dead, they departed every man unto his place.",
      "M": "And when the men of Israel saw that Abimelech was dead, they all went home to their own places.",
      "T": "When Israel saw that Abimelech was dead, they all went home."
    },
    "56": {
      "L": "Thus God rendered the wickedness of Abimelech, which he did unto his father, in slaying his seventy brethren:",
      "M": "Thus God repaid Abimelech for the evil he had done to his father by killing his seventy brothers.",
      "T": "So God settled the account of Abimelech for murdering his seventy brothers."
    },
    "57": {
      "L": "And all the evil of the men of Shechem did God render upon their heads: and upon them came the curse of Jotham the son of Jerubbaal.",
      "M": "And all the evil of the men of Shechem God also brought back on their own heads, and upon them came the curse of Jotham the son of Jerubbaal.",
      "T": "And the men of Shechem received their own reckoning. Jotham's curse from the top of Mount Gerizim had come to pass, word for word."
    }
  },
  "10": {
    "1": {
      "L": "And after Abimelech there arose to defend Israel Tola the son of Puah, the son of Dodo, a man of Issachar; and he dwelt in Shamir in mount Ephraim.",
      "M": "After Abimelech, Tola the son of Puah, son of Dodo, a man of Issachar, arose to save Israel. He lived in Shamir in the hill country of Ephraim.",
      "T": "After Abimelech, Tola son of Puah son of Dodo—a man of Issachar—arose to deliver Israel. He made his home in Shamir in the Ephraimite highlands."
    },
    "2": {
      "L": "And he judged Israel twenty and three years, and died, and was buried in Shamir.",
      "M": "He judged Israel twenty-three years, and then he died and was buried in Shamir.",
      "T": "He governed Israel for twenty-three years, then died and was buried in Shamir."
    },
    "3": {
      "L": "And after him arose Jair, a Gileadite, and judged Israel twenty and two years.",
      "M": "After him arose Jair the Gileadite, and he judged Israel twenty-two years.",
      "T": "After him came Jair the Gileadite, who governed Israel for twenty-two years."
    },
    "4": {
      "L": "And he had thirty sons that rode on thirty ass colts, and they had thirty cities, which are called Havothjair unto this day, which are in the land of Gilead.",
      "M": "He had thirty sons who rode on thirty donkeys, and they had thirty cities in the land of Gilead, which are called Havvoth-jair to this day.",
      "T": "He had thirty sons who each rode a donkey and governed thirty towns in Gilead—a cluster of settlements still called Havvoth-jair to this day."
    },
    "5": {
      "L": "And Jair died, and was buried in Camon.",
      "M": "And Jair died and was buried in Kamon.",
      "T": "Jair died and was buried at Kamon."
    },
    "6": {
      "L": "And the children of Israel did evil again in the sight of the LORD, and served Baalim, and Ashtaroth, and the gods of Syria, and the gods of Zidon, and the gods of Moab, and the gods of the children of Ammon, and the gods of the Philistines, and forsook the LORD, and served not him.",
      "M": "And the people of Israel again did what was evil in the sight of the LORD. They served the Baals and the Ashtoreths, the gods of Syria, the gods of Sidon, the gods of Moab, the gods of the Ammonites, and the gods of the Philistines. They forsook the LORD and did not serve him.",
      "T": "Once again Israel did what was evil in the LORD's sight. They served the Baals and the Ashtoreths—and on top of that, the gods of Syria, Sidon, Moab, Ammon, and Philistia. They abandoned the LORD entirely and stopped serving him."
    },
    "7": {
      "L": "And the anger of the LORD was hot against Israel, and he sold them into the hands of the Philistines, and into the hands of the children of Ammon.",
      "M": "And the anger of the LORD was kindled against Israel, and he sold them into the hands of the Philistines and into the hands of the Ammonites.",
      "T": "The LORD's anger blazed against Israel and he sold them—delivered them as property—into the hands of the Philistines and the Ammonites."
    },
    "8": {
      "L": "And that year they vexed and oppressed the children of Israel: eighteen years, all the children of Israel that were on the other side Jordan in the land of the Amorites, which is in Gilead.",
      "M": "And that year they shattered and crushed the people of Israel, eighteen years, all the people of Israel who were beyond the Jordan in the land of the Amorites in Gilead.",
      "T": "That year they crushed and ground down Israel for eighteen long years—particularly those living east of the Jordan in the former Amorite territory of Gilead."
    },
    "9": {
      "L": "Moreover the children of Ammon passed over Jordan to fight also against Judah, and against Benjamin, and against the house of Ephraim; so that Israel was sore distressed.",
      "M": "And the Ammonites also crossed the Jordan to fight against Judah and Benjamin and the house of Ephraim, so that Israel was severely distressed.",
      "T": "The Ammonites even crossed the Jordan to wage war against Judah, Benjamin, and Ephraim. Israel was in utter distress."
    },
    "10": {
      "L": "And the children of Israel cried unto the LORD, saying, We have sinned against thee, both because we have forsaken our God, and also served Baalim.",
      "M": "And the people of Israel cried out to the LORD, saying, “We have sinned against you, because we have forsaken our God and have served the Baals.”",
      "T": "Israel cried out to the LORD: “We have sinned against you. We abandoned our God and served the Baals.”"
    },
    "11": {
      "L": "And the LORD said unto the children of Israel, Did not I deliver you from the Egyptians, and from the Amorites, from the children of Ammon, and from the Philistines?",
      "M": "And the LORD said to the people of Israel, “Did I not save you from the Egyptians and from the Amorites, from the Ammonites and from the Philistines?",
      "T": "The LORD answered: “Was it not I who rescued you from Egypt? From the Amorites? From the Ammonites and the Philistines?"
    },
    "12": {
      "L": "The Zidonians also, and the Amalekites, and the Maonites, did oppress you; and ye cried to me, and I delivered you out of their hand.",
      "M": "And the Sidonians and the Amalekites and the Maonites oppressed you, and you cried out to me, and I delivered you from their hand.",
      "T": "The Sidonians, the Amalekites, the Maonites—they all oppressed you, and every time you cried out I delivered you."
    },
    "13": {
      "L": "Yet ye have forsaken me, and served other gods: wherefore I will deliver you no more.",
      "M": "Yet you have forsaken me and served other gods; therefore I will save you no more.",
      "T": "Yet you have abandoned me and gone after other gods. I will not rescue you again."
    },
    "14": {
      "L": "Go and cry unto the gods which ye have chosen; let them deliver you in the time of your tribulation.",
      "M": "Go and cry out to the gods you have chosen. Let them save you in the time of your distress.",
      "T": "Go and cry to the gods you chose. Let them deliver you in your hour of need.“"
    },
    "15": {
      "L": "And the children of Israel said unto the LORD, We have sinned: do thou unto us whatsoever seemeth good unto thee; deliver us only, we pray thee, this day.",
      "M": "And the people of Israel said to the LORD, “We have sinned. Do to us whatever seems good to you. Only please deliver us today.”",
      "T": "Israel said to the LORD, “We have sinned. Do with us whatever you think right. Only please—save us today.”"
    },
    "16": {
      "L": "And they put away the strange gods from among them, and served the LORD: and his soul was grieved for the misery of Israel.",
      "M": "So they put away the foreign gods from among themselves and served the LORD, and he could no longer bear the misery of Israel.",
      "T": "They removed every foreign god from their midst and began serving the LORD again—and he could bear their suffering no longer. His aching heart gave way."
    },
    "17": {
      "L": "Then the children of Ammon were gathered together, and encamped in Gilead. And the children of Israel assembled themselves together, and encamped in Mizpeh.",
      "M": "Then the Ammonites were called to arms and camped in Gilead. And the people of Israel gathered and camped at Mizpah.",
      "T": "The Ammonites mobilized and camped in Gilead. Israel gathered and made camp at Mizpah."
    },
    "18": {
      "L": "And the people and princes of Gilead said one to another, What man is he that will begin to fight against the children of Ammon? he shall be head over all the inhabitants of Gilead.",
      "M": "And the people and leaders of Gilead said to one another, “Who is the man who will begin the fight against the Ammonites? He shall be head over all the inhabitants of Gilead.”",
      "T": "The leaders of Gilead said among themselves, “Which man will step forward and lead the attack against Ammon? Whoever does it shall be ruler over all of Gilead.”"
    }
  },
  "11": {
    "1": {
      "L": "Now Jephthah the Gileadite was a mighty man of valour, and he was the son of an harlot: and Gilead begat Jephthah.",
      "M": "Now Jephthah the Gileadite was a mighty warrior, but he was the son of a prostitute. Gilead was his father.",
      "T": "Jephthah the Gileadite was a champion of valor—but he was born of a prostitute. Gilead was his father."
    },
    "2": {
      "L": "And Gilead's wife bare him sons; and his wife's sons grew up, and they thrust out Jephthah, and said unto him, Thou shalt not inherit in our father's house; for thou art the son of a strange woman.",
      "M": "And Gilead's wife bore him sons. When the wife's sons grew up, they drove Jephthah out and said to him, “You shall not have an inheritance in our father's house, for you are the son of another woman.”",
      "T": "Gilead's legitimate wife also bore him sons. When they grew up, they drove Jephthah out: “You get nothing from our father's estate—you're the son of another woman.”"
    },
    "3": {
      "L": "Then Jephthah fled from his brethren, and dwelt in the land of Tob: and there were gathered vain men to Jephthah, and went out with him.",
      "M": "Then Jephthah fled from his brothers and settled in the land of Tob. And worthless fellows gathered around Jephthah and went out raiding with him.",
      "T": "So Jephthah ran away to the land of Tob. There he attracted a band of desperate men around him and they lived by raiding."
    },
    "4": {
      "L": "And it came to pass in process of time, that the children of Ammon made war against Israel.",
      "M": "After some time the Ammonites made war against Israel.",
      "T": "In the course of time, the Ammonites launched a war against Israel."
    },
    "5": {
      "L": "And it was so, that when the children of Ammon made war against Israel, the elders of Gilead went to fetch Jephthah out of the land of Tob:",
      "M": "And when the Ammonites made war against Israel, the elders of Gilead went to bring Jephthah back from the land of Tob.",
      "T": "When the Ammonites attacked, the elders of Gilead went to Tob to bring Jephthah back."
    },
    "6": {
      "L": "And they said unto Jephthah, Come, and be our captain, that we may fight with the children of Ammon.",
      "M": "And they said to Jephthah, “Come, be our commander so that we can fight against the Ammonites.”",
      "T": "They said to him, “Come back. Lead us against the Ammonites.”"
    },
    "7": {
      "L": "And Jephthah said unto the elders of Gilead, Did not ye hate me, and expel me out of my father's house? and why are ye come unto me now when ye are in distress?",
      "M": "But Jephthah said to the elders of Gilead, “Did you not hate me and drive me out of my father's house? Why have you come to me now when you are in trouble?”",
      "T": "Jephthah said to them, “Didn't you hate me and throw me out of my father's house? Now that you're in trouble, you come to me?”"
    },
    "8": {
      "L": "And the elders of Gilead said unto Jephthah, Therefore we turn again to thee now, that thou mayest go with us, and fight against the children of Ammon, and be our head over all the inhabitants of Gilead.",
      "M": "And the elders of Gilead said to Jephthah, “That is why we have turned to you now—so that you will go with us and fight against the Ammonites, and be our head over all the inhabitants of Gilead.”",
      "T": "The elders said, “Precisely why we have come. Lead us against Ammon, and you will be ruler over all of Gilead.”"
    },
    "9": {
      "L": "And Jephthah said unto the elders of Gilead, If ye bring me home again to fight against the children of Ammon, and the LORD deliver them before me, shall I be your head?",
      "M": "And Jephthah said to the elders of Gilead, “If you bring me back to fight against the Ammonites, and the LORD gives them over to me, I will be your head.”",
      "T": "Jephthah said, “If you bring me home to fight Ammon—and the LORD delivers them to me—then I will be your ruler.”"
    },
    "10": {
      "L": "And the elders of Gilead said unto Jephthah, The LORD be witness between us, if we do not so according to thy words.",
      "M": "And the elders of Gilead said to Jephthah, “The LORD will be witness between us—we will surely do as you say.”",
      "T": "The elders replied, “The LORD himself is our witness. We will do exactly as you say.”"
    },
    "11": {
      "L": "Then Jephthah went with the elders of Gilead, and the people made him head and captain over them: and Jephthah uttered all his words before the LORD in Mizpeh.",
      "M": "So Jephthah went with the elders of Gilead, and the people made him their head and commander. And Jephthah stated all his terms before the LORD at Mizpah.",
      "T": "Jephthah went with the elders, and the people appointed him head and commander. He laid out all the terms before the LORD at Mizpah—making the agreement a covenant before God."
    },
    "12": {
      "L": "And Jephthah sent messengers unto the king of the children of Ammon, saying, What hast thou to do with me, that thou art come against me to fight in my land?",
      "M": "And Jephthah sent messengers to the king of the Ammonites, saying, “What do you have against me, that you have come to fight against me in my land?”",
      "T": "Jephthah opened diplomatic talks, sending a message to the Ammonite king: “What grievance do you have with us that you have invaded our land?”"
    },
    "13": {
      "L": "And the king of the children of Ammon answered unto the messengers of Jephthah, Because Israel took away my land, when they came up from Egypt, from Arnon even unto Jabbok, and unto Jordan: now therefore restore those lands again peaceably.",
      "M": "And the king of the Ammonites answered the messengers of Jephthah, “Because Israel took away my land when they came up from Egypt, from the Arnon as far as the Jabbok and the Jordan. Now therefore return them peaceably.”",
      "T": "The Ammonite king replied: “When Israel came up from Egypt, they seized our land—from the Arnon all the way to the Jabbok and the Jordan. Give it back, peaceably.”"
    },
    "14": {
      "L": "And Jephthah sent messengers again unto the king of the children of Ammon:",
      "M": "And Jephthah sent messengers again to the king of the Ammonites",
      "T": "Jephthah sent back his own message:"
    },
    "15": {
      "L": "And said unto him, Thus saith Jephthah, Israel did not take away the land of Moab, nor the land of the children of Ammon:",
      "M": "and said to him, “Thus says Jephthah: Israel did not take the land of Moab or the land of the Ammonites.",
      "T": "“Jephthah says this: Israel took neither Moabite nor Ammonite land."
    },
    "16": {
      "L": "But when Israel came up from Egypt, and walked through the wilderness unto the Red sea, and came to Kadesh;",
      "M": "When Israel came up from Egypt, they went through the wilderness to the Red Sea and came to Kadesh.",
      "T": "When Israel left Egypt, they passed through the wilderness to the Red Sea and arrived at Kadesh."
    },
    "17": {
      "L": "Then Israel sent messengers unto the king of Edom, saying, Let me, I pray thee, pass through thy land: but the king of Edom would not hearken thereto. And in like manner they sent unto the king of Moab: but he would not consent: and Israel abode in Kadesh.",
      "M": "Then Israel sent messengers to the king of Edom, saying, 'Please let us pass through your land,' but the king of Edom would not listen. They also sent to the king of Moab, but he would not consent. So Israel remained at Kadesh.",
      "T": "Israel asked Edom for passage—refused. They asked Moab—also refused. So Israel stayed at Kadesh."
    },
    "18": {
      "L": "Then they went along through the wilderness, and compassed the land of Edom, and the land of Moab, and came by the east side of the land of Moab, and pitched on the other side of Arnon, but came not within the border of Moab: for Arnon was the border of Moab.",
      "M": "Then they journeyed through the wilderness and went around the land of Edom and the land of Moab, and came along the eastern side of the land of Moab, and camped on the other side of the Arnon, but did not enter the territory of Moab, for the Arnon was the boundary of Moab.",
      "T": "So Israel went the long way around, skirting Edom and Moab, coming up along Moab's east side, and camping beyond the Arnon River—never setting foot inside Moab's territory, because the Arnon was Moab's border."
    },
    "19": {
      "L": "And Israel sent messengers unto Sihon king of the Amorites, the king of Heshbon; and Israel said unto him, Let us pass, we pray thee, through thy land into my place.",
      "M": "And Israel sent messengers to Sihon king of the Amorites, the king of Heshbon, and Israel said to him, 'Please let us pass through your land to our place.'",
      "T": "Then Israel sent messengers to Sihon king of the Amorites in Heshbon: 'Let us pass through your land to reach our destination.'"
    },
    "20": {
      "L": "But Sihon trusted not Israel to pass through his coast: but Sihon gathered all his people together, and pitched in Jahaz, and fought against Israel.",
      "M": "But Sihon did not trust Israel to pass through his territory. So Sihon gathered all his people together and camped at Jahaz and fought against Israel.",
      "T": "But Sihon refused to trust Israel with passage through his land. He mustered his entire army, camped at Jahaz, and attacked Israel."
    },
    "21": {
      "L": "And the LORD God of Israel delivered Sihon and all his people into the hand of Israel, and they smote them: so Israel possessed all the land of the Amorites, the inhabitants of that country.",
      "M": "And the LORD, the God of Israel, gave Sihon and all his people into the hand of Israel, and they struck them down. So Israel took possession of all the land of the Amorites, the inhabitants of that country.",
      "T": "The LORD, the God of Israel, handed Sihon and his whole army over to Israel. Israel defeated them and occupied all the Amorite territory."
    },
    "22": {
      "L": "And they possessed all the coasts of the Amorites, from Arnon even unto Jabbok, and from the wilderness even unto Jordan.",
      "M": "And they possessed all the territory of the Amorites from the Arnon to the Jabbok and from the wilderness to the Jordan.",
      "T": "The whole region from the Arnon to the Jabbok, from the desert to the Jordan—they occupied it all."
    },
    "23": {
      "L": "So now the LORD God of Israel hath dispossessed the Amorites from before his people Israel, and shouldest thou possess it?",
      "M": "So now the LORD, the God of Israel, has dispossessed the Amorites from before his people Israel, and are you going to take it?",
      "T": "The LORD, the God of Israel, drove out the Amorites—so now you want to take their land from us?"
    },
    "24": {
      "L": "Wilt not thou possess that which Chemosh thy god giveth thee to possess? So whomsoever the LORD our God shall drive out from before us, them will we possess.",
      "M": "Do you not possess what Chemosh your god gives you? And whatever the LORD our God has taken for us, we will possess.",
      "T": "You hold what your god Chemosh gives you. We hold what the LORD our God has given us—and that is the principle that settles this."
    },
    "25": {
      "L": "And now art thou any thing better than Balak the son of Zippor, king of Moab? did he ever strive against Israel, or did he ever fight against them,",
      "M": "And are you any better than Balak the son of Zippor, king of Moab? Did he ever strive with Israel? Did he ever go to war with them?",
      "T": "Are you any greater than Balak son of Zippor, king of Moab? Did he wage war against Israel? Did he challenge us in court?"
    },
    "26": {
      "L": "While Israel dwelt in Heshbon and her towns, and in Aroer and her towns, and in all the cities that be along by the coasts of Arnon, three hundred years? why therefore did ye not recover them within that time?",
      "M": "For three hundred years Israel lived in Heshbon and its villages, in Aroer and its villages, and in all the towns along the Arnon. Why did you not take them back during all that time?",
      "T": "Israel has held Heshbon and Aroer and all the towns along the Arnon for three hundred years. If this land were really yours, why didn't you reclaim it in three centuries?"
    },
    "27": {
      "L": "Wherefore I have not sinned against thee, but thou doest me wrong to war against me: the LORD the Judge be judge this day between the children of Israel and the children of Ammon.",
      "M": "I have not sinned against you, but you are doing me wrong by making war on me. The LORD, the Judge, decide today between the people of Israel and the people of Ammon.",
      "T": "I have done you no wrong. You are the one committing injustice by attacking us. Let the LORD, who is the Judge, render his verdict today between Israel and Ammon.“"
    },
    "28": {
      "L": "Howbeit the king of the children of Ammon hearkened not unto the words of Jephthah which he sent him.",
      "M": "But the king of the Ammonites did not listen to the words that Jephthah sent him.",
      "T": "The Ammonite king ignored every word of it."
    },
    "29": {
      "L": "Then the Spirit of the LORD came upon Jephthah, and he passed over Gilead, and Manasseh, and passed over Mizpeh of Gilead, and from Mizpeh of Gilead he passed over unto the children of Ammon.",
      "M": "Then the Spirit of the LORD came upon Jephthah, and he passed through Gilead and Manasseh and through Mizpah of Gilead, and from Mizpah of Gilead he crossed over to the Ammonites.",
      "T": "Then the Spirit of the LORD came upon Jephthah. He swept through Gilead and Manasseh, through Mizpah of Gilead, and crossed over to face the Ammonites."
    },
    "30": {
      "L": "And Jephthah vowed a vow unto the LORD, and said, If thou shalt without fail deliver the children of Ammon into mine hands,",
      "M": "And Jephthah made a vow to the LORD and said, “If you will indeed give the Ammonites into my hand,",
      "T": "Before the battle, Jephthah made a vow to the LORD: “If you truly deliver the Ammonites into my hands,"
    },
    "31": {
      "L": "Then it shall be, that whatsoever cometh forth of the doors of my house to meet me, when I return in peace from the children of Ammon, shall surely be the LORD'S, and I will offer it up for a burnt offering.",
      "M": "then whatever comes out of the door of my house to meet me when I return in peace from the Ammonites shall belong to the LORD, and I will offer it up as a burnt offering.",
      "T": "then whatever comes through my front door to greet me when I return victorious from Ammon—it will be the LORD's, and I will offer it as a burnt offering.“ The words were rash, and the text holds its breath."
    },
    "32": {
      "L": "So Jephthah passed over unto the children of Ammon to fight against them; and the LORD delivered them into his hands.",
      "M": "So Jephthah crossed over to the Ammonites to fight against them, and the LORD gave them into his hand.",
      "T": "Jephthah crossed to engage the Ammonites—and the LORD gave them into his hands."
    },
    "33": {
      "L": "And he smote them from Aroer, even till thou come to Minnith, even twenty cities, and unto the plain of the vineyards, with a very great slaughter. Thus the children of Ammon were subdued before the children of Israel.",
      "M": "He struck them from Aroer to the approach of Minnith, twenty cities, and as far as Abel-keramim, with a very great blow. So the Ammonites were subdued before the people of Israel.",
      "T": "He devastated them from Aroer to Minnith—twenty towns—all the way to Abel-keramim, a crushing defeat. Ammon was broken before Israel."
    },
    "34": {
      "L": "And Jephthah came to Mizpeh unto his house, and, behold, his daughter came out to meet him with timbrels and with dances: and she was his only child; beside her he had neither son nor daughter.",
      "M": "Then Jephthah came to his home at Mizpah, and behold, his daughter came out to meet him with tambourines and dancing. She was his only child; he had no son or daughter besides her.",
      "T": "Jephthah came home to Mizpah—and his daughter came out dancing to meet him, tambourine in hand. She was his one and only child. He had no other."
    },
    "35": {
      "L": "And it came to pass, when he saw her, that he rent his clothes, and said, Alas, my daughter! thou hast brought me very low, and thou art one of them that trouble me: for I have opened my mouth unto the LORD, and I cannot go back.",
      "M": "When he saw her, he tore his clothes and said, “Alas, my daughter! You have brought me very low and you have become the cause of my ruin. I have opened my mouth to the LORD, and I cannot take it back.”",
      "T": "When he saw her, he tore his robes in grief and cried out, “Oh, my daughter—you have broken me! You are the one who has ruined me. I made a vow to the LORD and I cannot take it back.”"
    },
    "36": {
      "L": "And she said unto him, My father, if thou hast opened thy mouth unto the LORD, do to me according to that which hath proceeded out of thy mouth; forasmuch as the LORD hath taken vengeance for thee of thine enemies, even of the children of Ammon.",
      "M": "And she said to him, “My father, you have opened your mouth to the LORD; do to me according to what has gone out of your mouth, now that the LORD has avenged you on your enemies, the Ammonites.”",
      "T": "She said to him, “Father, you gave your word to the LORD. Do what you vowed—because the LORD has vindicated you against your enemies, the Ammonites.”"
    },
    "37": {
      "L": "And she said unto her father, Let this thing be done for me: let me alone two months, that I may go up and down upon the mountains, and bewail my virginity, I and my fellows.",
      "M": "And she said to her father, “Let this one thing be done for me: leave me alone for two months, that I may go and wander on the mountains and weep over my virginity, I and my companions.”",
      "T": "But she made one request: “Give me two months. Let me go to the mountains with my companions and mourn that I will die a virgin.”"
    },
    "38": {
      "L": "And he said, Go. And he sent her away for two months: and she went with her companions, and bewailed her virginity upon the mountains.",
      "M": "And he said, “Go.” And he sent her away for two months, and she went with her companions and wept over her virginity on the mountains.",
      "T": "He said, “Go.” He sent her away for two months, and she went into the mountains with her friends and mourned that she would never know a husband."
    },
    "39": {
      "L": "And it came to pass at the end of two months, that she returned unto her father, who did with her according to his vow which he had vowed: and she knew no man. And it was a custom in Israel,",
      "M": "And at the end of two months, she returned to her father, who did with her according to his vow that he had made. She had never known a man. And it became a custom in Israel",
      "T": "At the end of two months she came home to her father, and he fulfilled his vow. She had never known a man. And from this, a tradition arose in Israel—"
    },
    "40": {
      "L": "That the daughters of Israel went yearly to lament the daughter of Jephthah the Gileadite four days in a year.",
      "M": "that the daughters of Israel went year by year to lament the daughter of Jephthah the Gileadite, four days each year.",
      "T": "—the daughters of Israel would go out every year for four days to commemorate the daughter of Jephthah the Gileadite."
    }
  },
  "12": {
    "1": {
      "L": "And the men of Ephraim gathered themselves together, and went northward, and said unto Jephthah, Wherefore passedst thou over to fight against the children of Ammon, and didst not call us to go with thee? we will burn thine house upon thee with fire.",
      "M": "The men of Ephraim were called to arms and crossed to the north. And they said to Jephthah, “Why did you cross over to fight against the Ammonites without calling us to go with you? We will burn your house down over you with fire!”",
      "T": "The Ephraimites mobilized and came north, confronting Jephthah: “You fought Ammon without us? We'll burn your house down over your head!”"
    },
    "2": {
      "L": "And Jephthah said unto them, I and my people were at great strife with the children of Ammon; and when I called you, ye delivered me not out of their hands.",
      "M": "And Jephthah said to them, “I and my people were in great conflict with the Ammonites, and when I called you, you did not deliver me from their hand.",
      "T": "Jephthah answered: “My people and I were in a desperate fight with Ammon. I called on you—you never came."
    },
    "3": {
      "L": "And when I saw that ye delivered me not, I put my life in my hands, and passed over against the children of Ammon, and the LORD delivered them into my hand: wherefore then are ye come up unto me this day, to fight against me?",
      "M": "When I saw that you would not save me, I took my life in my own hands and crossed over against the Ammonites, and the LORD gave them into my hand. So why have you come up against me today to fight me?“",
      "T": "When I saw no help was coming, I risked my life and crossed over, and the LORD handed them to me. So why are you here now, to make war against me?“"
    },
    "4": {
      "L": "Then Jephthah gathered together all the men of Gilead, and fought with Ephraim: and the men of Gilead smote Ephraim, because they said, Ye Gileadites are fugitives of Ephraim among the Ephraimites, and among the Manassites.",
      "M": "Then Jephthah gathered all the men of Gilead and fought with Ephraim. And the men of Gilead struck Ephraim, because the Ephraimites had said, “You Gileadites are fugitives of Ephraim in the midst of Ephraim and Manasseh.”",
      "T": "Jephthah—unlike Gideon before him—chose force over diplomacy. He gathered the Gileadites and attacked Ephraim. The Ephraimites had heaped insult on injury, calling the Gileadites nothing but Ephraimite deserters; now they paid for it."
    },
    "5": {
      "L": "And the Gileadites took the passages of Jordan before the Ephraimites: and it was so, that when those Ephraimites which were escaped said, Let me go over; that the men of Gilead said unto him, Art thou an Ephraimite? If he said, Nay;",
      "M": "And the Gileadites seized the fords of the Jordan ahead of the Ephraimites. And whenever an Ephraimite fugitive said, “Let me cross over,” the men of Gilead would ask him, “Are you an Ephraimite?” If he said, “No,”",
      "T": "The Gileadites seized the Jordan fords before the fleeing Ephraimites could reach them. When a fugitive arrived and asked to cross, they would ask: “Are you an Ephraimite?” If he said no—"
    },
    "6": {
      "L": "Then said they unto him, Say now Shibboleth: and he said Sibboleth: for he could not frame to pronounce it right. Then they took him, and slew him at the passages of Jordan: and there fell at that time of the Ephraimites forty and two thousand.",
      "M": "they would say to him, “Then say 'Shibboleth.'” And he would say “Sibboleth,” for he could not pronounce it correctly. Then they would seize him and kill him at the fords of the Jordan. And there fell at that time forty-two thousand of the Ephraimites.",
      "T": "they told him, “Say 'Shibboleth.'” But the Ephraimite dialect could not produce the 'sh' sound—they said 'Sibboleth.' The difference was a death sentence. Forty-two thousand Ephraimites were killed at the Jordan fords. A shared language had become a weapon."
    },
    "7": {
      "L": "And Jephthah judged Israel six years. Then died Jephthah the Gileadite, and was buried in one of the cities of Gilead.",
      "M": "Jephthah judged Israel for six years. Then Jephthah the Gileadite died and was buried in one of the cities of Gilead.",
      "T": "Jephthah governed Israel for six years. Then he died and was buried in a town of Gilead."
    },
    "8": {
      "L": "And after him Ibzan of Bethlehem judged Israel.",
      "M": "After him Ibzan of Bethlehem judged Israel.",
      "T": "After him, Ibzan of Bethlehem governed Israel."
    },
    "9": {
      "L": "And he had thirty sons, and thirty daughters, whom he sent abroad, and took in thirty daughters from abroad for his sons. And he judged Israel seven years.",
      "M": "He had thirty sons, and thirty daughters he gave in marriage outside his clan, and thirty daughters he brought in from outside for his sons. He judged Israel seven years.",
      "T": "He had thirty sons and thirty daughters. He arranged marriages for all of them—his daughters out and other clans' daughters in for his sons—weaving a wide network of alliances. He governed Israel seven years."
    },
    "10": {
      "L": "Then died Ibzan, and was buried at Bethlehem.",
      "M": "Then Ibzan died and was buried in Bethlehem.",
      "T": "Then Ibzan died and was buried in Bethlehem."
    },
    "11": {
      "L": "And after him Elon, a Zebulonite, judged Israel; and he judged Israel ten years.",
      "M": "After him Elon the Zebulunite judged Israel, and he judged Israel ten years.",
      "T": "After him, Elon the Zebulunite governed Israel for ten years."
    },
    "12": {
      "L": "And Elon the Zebulonite died, and was buried in Aijalon in the country of Zebulun.",
      "M": "And Elon the Zebulunite died and was buried in Aijalon in the land of Zebulun.",
      "T": "Elon the Zebulunite died and was buried at Aijalon in the territory of Zebulun."
    },
    "13": {
      "L": "And after him Abdon the son of Hillel, a Pirathonite, judged Israel.",
      "M": "After him Abdon the son of Hillel the Pirathonite judged Israel.",
      "T": "After him, Abdon son of Hillel the Pirathonite governed Israel."
    },
    "14": {
      "L": "And he had forty sons and thirty nephews, that rode on threescore and ten ass colts: and he judged Israel eight years.",
      "M": "He had forty sons and thirty grandsons who rode on seventy donkeys. He judged Israel eight years.",
      "T": "He had forty sons and thirty grandsons—seventy young men riding donkeys. He governed Israel eight years."
    },
    "15": {
      "L": "And Abdon the son of Hillel the Pirathonite died, and was buried in Pirathon in the land of Ephraim, in the mount of the Amalekites.",
      "M": "And Abdon the son of Hillel the Pirathonite died and was buried at Pirathon in the land of Ephraim, in the hill country of the Amalekites.",
      "T": "Abdon son of Hillel the Pirathonite died and was buried at Pirathon in Ephraim, in the hill country of the Amalekites."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'judges')
        merge_tier(existing, JUDGES, tier_key)
        save(tier_dir, 'judges', existing)
    print('Judges 7–12 written.')

if __name__ == '__main__':
    main()
