"""
MKT Ruth chapters 1–4 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ruth-1-4.py

Ruth is a masterpiece of Hebrew short story: four tightly structured chapters that move
from emptiness to fullness, from death to life, from outsider to insider. The book is
deliberately set "in the days of the judges" (1:1) — placing covenant faithfulness against
the backdrop of Israel's covenantal failure. Ruth the Moabitess becomes the counter-narrative
to Judges: where Israel proves unfaithful, a foreign woman embodies חֶסֶד.

Key theological arc: The word חֶסֶד (H2617) is the hinge of the entire book — it appears
in 1:8 (Naomi prays it for her daughters-in-law), 2:20 (Naomi sees Boaz's חֶסֶד as the
LORD's חֶסֶד to the living and dead), and 3:10 (Boaz praises Ruth's latter חֶסֶד as greater
than the first). Every human act of loyalty in this book is simultaneously a disclosure of
the LORD's own loyal love. T tier surfaces this theological movement throughout.

Translation decisions:

- H3068 (יהוה): "LORD" L/M (small-caps convention); "the LORD" T — consistent with all
  prior OT scripts (Joshua, Deuteronomy, Judges, etc.)

- H430 (אֱלֹהִים): "God" when divine; "gods" (lowercase) when referring to Moabite deities
  in 1:15 — context makes clear these are foreign gods, not the God of Israel

- H7706 (שַׁדַּי): "Almighty" all tiers in 1:20-21 — Naomi uses the name אֵל שַׁדַּי when
  lamenting God's dealing with her; T preserves the force of the divine name

- H2617 (חֶסֶד): "kindness" L; "faithful kindness" M; "steadfast loyal love" T — the
  covenant-loyalty word that is the book's theological center; three occurrences total
  (1:8; 2:20; 3:10); T always draws out the covenantal dimension

- H1350 (גֹּאֵל / go'el), H1353 (גְּאֻלָּה): "kinsman-redeemer" all tiers — the legal
  institution of family redemption that structures chapters 2–4; the go'el had both the
  right and obligation to restore alienated family property and widows within the clan;
  T surfaces this legal-theological institution and its Christological trajectory

- H4494 / H4496 (מָנוֹחַ / מְנוּחָה): "rest" all tiers — Naomi seeks "rest" (1:9; 3:1)
  for her daughters-in-law, specifically a settled home and marriage security; the word
  resonates with Deuteronomy's "rest in the land"; T surfaces this covenant resonance

- H3671 (כָּנָף): "wing(s)" and "skirt/garment" — the SAME Hebrew word occurs in 2:12
  ("under whose wings you have come to take refuge," referring to God) and 3:9 (Ruth asks
  Boaz to "spread your skirt over your servant," i.e., claim her as wife); this deliberate
  echo is one of the book's finest literary touches; T makes the connection explicit

- H2428 (חַיִל): "mighty man of wealth" L (2:1); "woman of noble character" L (3:11) —
  the same Hebrew word applies to both Boaz (אִישׁ גִּבּוֹר חַיִל, 2:1) and Ruth (אֵשֶׁת
  חַיִל, 3:11; cf. Prov 31:10). M: "man of standing" (2:1) / "woman of noble character"
  (3:11). T: explicitly notes the echo and calls both "people of valor"

- H5315 (נֶפֶשׁ): "life" in 4:15 (מֵשִׁיב נֶפֶשׁ = restorer of life) — physical sustaining
  of embodied life, not the immaterial soul

- H4125 / H4124 (מוֹאָבִיָּה / מוֹאָב): Ruth is called "the Moabitess" repeatedly and
  deliberately. Deut 23:3 excluded Moabites from the assembly to the tenth generation.
  T notes this tension: the book is making a deliberate theological point about the
  scope of covenant inclusion

- H5275 (נַעַל): "shoe/sandal" in 4:7-8 — the sandal-exchange custom sealed legal
  transfers; T explains the ancient practice

- H8543 (תְּמוֹל): in context of "not heretofore" (2:11) — the KJV "heretofore" rendering

- OT intertextuality notes:
  * 4:11-12: The blessing invokes Rachel, Leah, and Tamar — all women whose stories
    involved irregular paths to the covenant line; T draws the connection
  * 4:17-22: The genealogy closes the book by revealing that this Moabite woman's
    faithfulness ran directly to the throne of David — and through David to the Messiah;
    T makes this explicit in v17 and the genealogy's final verse
  * The "gleaning" law invoked by Ruth (2:2) echoes Lev 19:9-10 / Deut 24:19-22 —
    the social-justice provisions of Torah that made space for the vulnerable; T notes this

- Structural note: The book divides naturally into four acts corresponding to the four
  chapters: (1) Emptying — Naomi's loss; (2) Providence — Ruth meets Boaz;
  (3) Night encounter — Ruth claims Boaz as go'el; (4) Gate — legal redemption and
  restoration. Each chapter has its own vocabulary cluster; the translation honors this
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

RUTH = {
  "1": {
    "1": {
      "L": "And it came to pass in the days when the judges ruled, there was a famine in the land; and a certain man of Bethlehem-judah went to sojourn in the country of Moab, he and his wife and his two sons.",
      "M": "In the days when the judges ruled Israel, there was a famine in the land, and a man from Bethlehem in Judah set out to live as a resident alien in the country of Moab — he, his wife, and his two sons.",
      "T": "It was the era of the judges — when Israel's covenantal failure ran deep and cyclical. A famine struck the land. A man from Bethlehem in Judah packed up his household and went to live as a foreigner in Moab: he, his wife, and his two sons."
    },
    "2": {
      "L": "And the name of the man was Elimelech, and the name of his wife Naomi, and the name of his two sons Mahlon and Chilion, Ephrathites of Bethlehem-judah; and they came into the country of Moab and remained there.",
      "M": "The man's name was Elimelech, his wife's name was Naomi, and his two sons were Mahlon and Chilion — Ephrathites from Bethlehem in Judah. They came to Moab and settled there.",
      "T": "The man was Elimelech — 'My God is King.' His wife was Naomi — 'Pleasant.' Their sons were Mahlon and Chilion. Ephrathites, from Bethlehem in Judah. They crossed the Jordan into Moab and made it their home."
    },
    "3": {
      "L": "And Elimelech, Naomi's husband, died; and she was left, she and her two sons.",
      "M": "Then Elimelech, Naomi's husband, died, and she was left with her two sons.",
      "T": "Elimelech died. Naomi was left in a foreign land with her sons."
    },
    "4": {
      "L": "And they took to themselves wives of the women of Moab; the name of the one was Orpah, and the name of the other Ruth; and they dwelt there about ten years.",
      "M": "The sons took Moabite women as wives — the name of the one was Orpah and the name of the other Ruth — and they lived there about ten years.",
      "T": "The two sons married Moabite women. One was named Orpah; the other Ruth. They put down roots in Moab, living there for some ten years."
    },
    "5": {
      "L": "And both Mahlon and Chilion died also; and the woman was left of her two sons and her husband.",
      "M": "Then both Mahlon and Chilion also died, and Naomi was left without her two sons and her husband.",
      "T": "Then both Mahlon and Chilion died as well. Naomi stood bereft — no husband, no sons, a widow in a foreign country."
    },
    "6": {
      "L": "Then she arose with her daughters-in-law to return from the country of Moab; for she had heard in the country of Moab how that the LORD had visited his people in giving them bread.",
      "M": "Then she arose with her daughters-in-law to return from Moab, for she had heard in Moab that the LORD had visited his people by giving them food.",
      "T": "Word reached her in Moab: the LORD had visited his people — the famine was over, bread had returned to Bethlehem. The LORD had not forgotten Israel. Naomi rose and began the journey back, her two daughters-in-law with her."
    },
    "7": {
      "L": "Wherefore she went forth out of the place where she was, and her two daughters-in-law with her; and they went on the way to return to the land of Judah.",
      "M": "So she set out from the place where she had been living, her two daughters-in-law with her, and they walked along the road toward the land of Judah.",
      "T": "She left the place that had taken her husband and sons. The three women walked out together on the road toward Judah."
    },
    "8": {
      "L": "And Naomi said to her two daughters-in-law, Go, return each to her mother's house; the LORD deal kindly with you, as ye have dealt with the dead and with me.",
      "M": "Then Naomi said to her two daughters-in-law, 'Go — return each of you to your mother's house. May the LORD deal with you in faithful kindness, as you have dealt with the dead and with me.'",
      "T": "'Go back,' Naomi told them — 'each of you to your own mother's house. You have shown steadfast loyal love to the dead men and to me. May the LORD return that love to you in kind.'"
    },
    "9": {
      "L": "The LORD grant you that ye may find rest, each of you in the house of her husband; then she kissed them; and they lifted up their voice and wept.",
      "M": "May the LORD grant each of you rest in the house of a new husband.' Then she kissed them, and they wept aloud.",
      "T": "'May the LORD give each of you rest — a household, a husband, a settled life.' She kissed them. All three of them wept."
    },
    "10": {
      "L": "And they said unto her, Surely we will return with thee unto thy people.",
      "M": "But they said to her, 'No — we will return with you to your people.'",
      "T": "'We are coming with you,' they insisted. 'To your people — wherever you go.'"
    },
    "11": {
      "L": "And Naomi said, Turn again, my daughters; why will ye go with me? Are there yet any more sons in my womb, that they may be your husbands?",
      "M": "But Naomi said, 'Turn back, my daughters. Why would you come with me? Do I still have sons in my womb who could become your husbands?'",
      "T": "Naomi pressed them: 'Go back, both of you. What future would you have by coming with me? I have no more sons to give you.'"
    },
    "12": {
      "L": "Turn again, my daughters, go your way; for I am too old to have a husband; if I should say, I have hope, if I should have also a husband to night, and should also bear sons;",
      "M": "Go back, my daughters — I am too old to remarry. Even if I said I had hope, even if tonight I had a husband and bore sons —",
      "T": "'Go back. I am too old for another marriage. And even if I were not — even if I were to wed tonight and have sons —'"
    },
    "13": {
      "L": "Would ye tarry for them till they were grown? would ye stay for them from having husbands? nay, my daughters; for it grieveth me much for your sakes that the hand of the LORD is gone out against me.",
      "M": "Would you wait until they were grown? Would you withhold yourselves from husbands for their sake? No, my daughters — it grieves me deeply for your sakes that the hand of the LORD has gone out against me.",
      "T": "'— would you wait years for them to grow? Would you hold back your lives for their sake? No. This is too bitter for me, my daughters. The LORD himself has lifted his hand against me — I cannot give you a future.'"
    },
    "14": {
      "L": "And they lifted up their voice and wept again; and Orpah kissed her mother-in-law; but Ruth clave unto her.",
      "M": "They wept aloud again. Orpah kissed her mother-in-law farewell, but Ruth clung to her.",
      "T": "Again they broke into weeping. Orpah kissed Naomi and turned back — that was the last they saw of her. But Ruth would not let go."
    },
    "15": {
      "L": "And she said, Behold, thy sister-in-law is gone back unto her people, and unto her gods; return thou after thy sister-in-law.",
      "M": "Then Naomi said, 'Look — your sister-in-law has gone back to her people and to her gods. Go back after her.'",
      "T": "'Your sister-in-law made the sensible choice,' Naomi said. 'She has gone home — to her people, to her gods. Follow her.'"
    },
    "16": {
      "L": "And Ruth said, Intreat me not to leave thee, or to return from following after thee; for whither thou goest, I will go; and where thou lodgest, I will lodge; thy people shall be my people, and thy God my God.",
      "M": "But Ruth said, 'Do not urge me to leave you or to turn back from following you. For where you go, I will go, and where you stay, I will stay. Your people will be my people, and your God will be my God.'",
      "T": "Ruth refused to be moved. 'Stop urging me to leave you,' she said. 'Where you go, I go. Where you stay, I stay. Your people are my people. Your God is my God.'"
    },
    "17": {
      "L": "Where thou diest, will I die, and there will I be buried; the LORD do so to me, and more also, if ought but death part thee and me.",
      "M": "Where you die, I will die, and there I will be buried. May the LORD do so to me and more also if anything but death separates you and me.'",
      "T": "'Where you die, I will die. That is where I will be buried. I call the LORD himself to witness: nothing but death will separate us — and if I break this oath, let him deal with me as he sees fit.'"
    },
    "18": {
      "L": "When she saw that she was stedfastly minded to go with her, she left off speaking unto her.",
      "M": "When Naomi saw that Ruth was determined to go with her, she stopped urging her.",
      "T": "Naomi recognized a settled, unbreakable resolve. She stopped arguing."
    },
    "19": {
      "L": "So they two went until they came to Bethlehem; and it came to pass when they were come to Bethlehem, that all the city was moved about them, and they said, Is this Naomi?",
      "M": "So the two of them walked on until they came to Bethlehem. When they arrived in Bethlehem, the whole town was stirred up over them, and the women said, 'Can this be Naomi?'",
      "T": "The two women walked the entire road together and arrived at last in Bethlehem. The town stirred. Word ran through the women: 'Is this Naomi? Is it really her — after all these years?'"
    },
    "20": {
      "L": "And she said unto them, Call me not Naomi; call me Mara; for the Almighty hath dealt very bitterly with me.",
      "M": "She said to them, 'Do not call me Naomi — call me Mara, for the Almighty has dealt very bitterly with me.'",
      "T": "'Do not call me Naomi — the name that means Pleasant,' she told them. 'Call me Mara — Bitter — because Almighty God has filled my life with bitterness.'"
    },
    "21": {
      "L": "I went out full, and the LORD hath brought me home again empty; why then call ye me Naomi, seeing the LORD hath testified against me, and the Almighty hath afflicted me?",
      "M": "I went out full, and the LORD has brought me back empty. Why call me Naomi when the LORD has spoken against me and the Almighty has afflicted me?'",
      "T": "'I left here with a husband and sons. I return with nothing. The LORD led me out full and has brought me home empty. Why give me a name that means pleasant when God himself has become my adversary — when the Almighty has shattered what I had?'"
    },
    "22": {
      "L": "So Naomi returned, and Ruth the Moabitess her daughter-in-law with her, who returned out of the country of Moab; and they came to Bethlehem in the beginning of barley harvest.",
      "M": "So Naomi came back, and with her Ruth the Moabitess, her daughter-in-law, who had returned with her from Moab. They arrived in Bethlehem at the beginning of the barley harvest.",
      "T": "That was how Naomi came home — empty, bitter, but not alone. Ruth the Moabitess walked beside her. They arrived in Bethlehem just as the barley harvest was beginning: an ending that held, if they could see it, the seed of everything that was to come."
    }
  },
  "2": {
    "1": {
      "L": "And Naomi had a kinsman of her husband's, a mighty man of wealth, of the family of Elimelech; and his name was Boaz.",
      "M": "Now Naomi had a kinsman on her husband's side, a man of standing from the family of Elimelech, whose name was Boaz.",
      "T": "There was a man — a connection through Elimelech's bloodline. His name was Boaz: a man of standing, of substance, of valor. One of Naomi's late husband's family."
    },
    "2": {
      "L": "And Ruth the Moabitess said unto Naomi, Let me now go to the field, and glean ears of corn after him in whose sight I shall find grace. And she said unto her, Go, my daughter.",
      "M": "Ruth the Moabitess said to Naomi, 'Let me go to the fields and glean grain behind whoever will allow me to.' Naomi said to her, 'Go, my daughter.'",
      "T": "Ruth came to Naomi with a plan. 'Let me go out to the fields,' she said, 'and glean grain after the harvesters — wherever I can find someone willing to let me.' 'Go ahead, my daughter,' said Naomi."
    },
    "3": {
      "L": "And she went, and came, and gleaned in the field after the reapers; and her hap was to light on a part of the field belonging unto Boaz, who was of the kindred of Elimelech.",
      "M": "So she went out, came to the fields, and gleaned after the reapers. As it happened, she came upon the portion of the field belonging to Boaz, who was from Elimelech's family.",
      "T": "She went. And as providence arranged — the Hebrew has the idiom 'her chance chanced upon her' — she ended up gleaning in the very portion of the field that belonged to Boaz, Elimelech's kinsman."
    },
    "4": {
      "L": "And, behold, Boaz came from Bethlehem, and said unto the reapers, The LORD be with you; and they answered him, The LORD bless thee.",
      "M": "Just then Boaz arrived from Bethlehem and greeted the reapers: 'The LORD be with you.' They answered him, 'The LORD bless you.'",
      "T": "At that moment Boaz himself arrived from Bethlehem. His first words to his workers were a blessing: 'The LORD be with you.' They blessed him back: 'The LORD bless you.' The exchange reveals the man."
    },
    "5": {
      "L": "Then said Boaz unto his servant that was set over the reapers, Whose damsel is this?",
      "M": "Boaz asked his servant who was in charge of the reapers, 'Whose young woman is this?'",
      "T": "Boaz noticed Ruth. He turned to the foreman over his reapers: 'Who is that young woman?'"
    },
    "6": {
      "L": "And the servant that was set over the reapers answered and said, It is the Moabitish damsel that came back with Naomi out of the country of Moab.",
      "M": "The foreman answered, 'She is the Moabite young woman who came back with Naomi from Moab.'",
      "T": "'She is the Moabite woman,' the foreman said — 'the one who came back with Naomi from Moab.'"
    },
    "7": {
      "L": "And she said, I pray you, let me glean and gather after the reapers among the sheaves; so she came, and hath continued even from the morning until now, that she tarried a little in the house.",
      "M": "She asked, 'Please let me glean and gather among the sheaves after the reapers.' She came and has been on her feet since early morning, with only a brief rest in the shelter.",
      "T": "'She asked permission very respectfully — may she please glean after the reapers. She has been working hard since early morning and has barely rested. She asked; she works; she waits.'"
    },
    "8": {
      "L": "Then said Boaz unto Ruth, Hearest thou not, my daughter? Go not to glean in another field, neither go from hence, but abide here fast by my maidens.",
      "M": "Then Boaz said to Ruth, 'Listen carefully, my daughter. Do not go to glean in another field — stay right here. Keep close to my young women.'",
      "T": "Boaz went directly to Ruth. 'Listen,' he said. 'Don't go to anyone else's field. Don't leave this one. Stay here, close to my women workers.'"
    },
    "9": {
      "L": "Let thine eyes be on the field that they do reap, and go thou after them; have I not charged the young men that they shall not touch thee? and when thou art athirst, go unto the vessels, and drink of that which the young men have drawn.",
      "M": "Watch the field where they are reaping and follow along after them. I have told the young men not to bother you. When you are thirsty, go to the water jars and drink from what the men have drawn.",
      "T": "'Keep your eyes on the section where they're reaping and follow their line. I have told my men not to lay a hand on you. And when you're thirsty, help yourself from the jars — the men have drawn water for everyone.'"
    },
    "10": {
      "L": "Then she fell on her face, and bowed herself to the ground, and said unto him, Why have I found grace in thine eyes, that thou shouldest take knowledge of me, seeing I am a stranger?",
      "M": "She fell with her face to the ground and bowed, and said to him, 'Why have I found favor in your eyes, that you would take notice of me, when I am a foreigner?'",
      "T": "Ruth prostrated herself before him. 'Why are you showing me this kindness?' she asked. 'I am a foreigner. You owe me nothing. Why do you even notice me?'"
    },
    "11": {
      "L": "And Boaz answered and said unto her, It hath fully been shewed me, all that thou hast done unto thy mother in law since the death of thine husband; and how thou hast left thy father and thy mother, and the land of thy nativity, and art come unto a people which thou knewest not heretofore.",
      "M": "Boaz answered her, 'Everything you have done for your mother-in-law since your husband's death has been fully reported to me — how you left your father and mother and your homeland and came to a people you had never known before.'",
      "T": "Boaz looked at her steadily. 'Everything you have done has been told to me,' he said — 'your faithfulness to Naomi after her husband died, how you left your own father and mother, your land, everything familiar, and came to live among people you had never met before.'"
    },
    "12": {
      "L": "The LORD recompense thy work, and a full reward be given thee of the LORD God of Israel, under whose wings thou art come to trust.",
      "M": "May the LORD repay you for what you have done. May you receive a full reward from the LORD, the God of Israel, under whose wings you have come to take refuge.'",
      "T": "'May the LORD repay you in full for it,' he said. 'You have come to shelter under the wings of the God of Israel. He does not neglect those who run to him for refuge.'"
    },
    "13": {
      "L": "Then she said, Let me find favour in thy sight, my lord; for that thou hast comforted me, and for that thou hast spoken friendly unto the heart of thine handmaid, though I be not like unto one of thine handmaidens.",
      "M": "She said, 'May I continue to find favor in your sight, my lord — for you have comforted me and spoken kindly to your servant, though I am not even like one of your own servant women.'",
      "T": "'You have given me more than I deserve,' Ruth said. 'You have comforted me. You spoke to my heart — to me, a woman who does not even rank as one of your own servants.'"
    },
    "14": {
      "L": "And Boaz said unto her, At mealtime come thou hither, and eat of the bread, and dip thy morsel in the vinegar; and she sat beside the reapers, and he reached her parched corn, and she did eat, and was sufficed, and left.",
      "M": "At mealtime Boaz said to her, 'Come over here and eat some bread, and dip your morsel in the wine vinegar.' So she sat beside the reapers, and he handed her some roasted grain. She ate until she was satisfied and had some left over.",
      "T": "When the meal break came, Boaz called to her: 'Come, eat with us. Dip your bread in the vinegar.' She sat down beside the reapers — not apart, not outside. He handed her roasted grain himself. She ate until full and had food left over."
    },
    "15": {
      "L": "And when she was risen up to glean, Boaz commanded his young men, saying, Let her glean even among the sheaves, and reproach her not.",
      "M": "When she rose to glean again, Boaz commanded his young men, saying, 'Let her glean even among the sheaves, and do not rebuke her.'",
      "T": "When she went back to work, Boaz gave quiet orders to his men: 'Let her glean right among the bound sheaves — don't shame her or push her away.'"
    },
    "16": {
      "L": "And let fall also some of the handfuls of purpose for her, and leave them, that she may glean them, and rebuke her not.",
      "M": "And pull out some stalks from the bundles and drop them deliberately for her to glean, and do not rebuke her.'",
      "T": "'Better yet — pull handfuls out of the sheaves on purpose and drop them in her path. And say nothing. Let her think it is her own gleaning.'"
    },
    "17": {
      "L": "So she gleaned in the field until even, and beat out that she had gleaned; and it was about an ephah of barley.",
      "M": "So she gleaned in the field until evening. When she beat out what she had gleaned, it came to about an ephah of barley.",
      "T": "She worked from morning until evening. When she beat out the grain at dusk, it measured about an ephah of barley — an extraordinary amount for a single day's gleaning from a foreign woman with no claim on the field."
    },
    "18": {
      "L": "And she took it up, and went into the city; and her mother in law saw what she had gleaned; and she brought forth, and gave to her that she had reserved after she was sufficed.",
      "M": "She took it up and went into the town. Her mother-in-law saw what she had gleaned. Ruth also brought out and gave her the food she had saved from her meal.",
      "T": "She carried the grain back into town. Naomi's eyes went wide when she saw the pile. Ruth also took out the food she had saved from lunch — still had some. She gave it to Naomi."
    },
    "19": {
      "L": "And her mother in law said unto her, Where hast thou gleaned to day? and where wroughtest thou? blessed be he that did take knowledge of thee; and she shewed her mother in law with whom she had wrought, and said, The man's name with whom I wrought to day is Boaz.",
      "M": "Her mother-in-law asked her, 'Where did you glean today? Where did you work? Blessed be the man who took notice of you!' She told her mother-in-law with whom she had worked, and said, 'The man's name with whom I worked today is Boaz.'",
      "T": "'Where did you glean all this?' Naomi asked. 'Where did you work? Blessed be whoever showed you such kindness!' Ruth told her everything — and then she said the name: 'The man I worked with today is Boaz.'"
    },
    "20": {
      "L": "And Naomi said unto her daughter in law, Blessed be he of the LORD, who hath not left off his kindness to the living and to the dead; and Naomi said unto her, The man is near of kin unto us, one of our next kinsmen.",
      "M": "Then Naomi said to her daughter-in-law, 'Blessed be he of the LORD, who has not abandoned his faithful kindness to the living and to the dead.' And Naomi said to her, 'The man is closely related to us — he is one of our kinsman-redeemers.'",
      "T": "Naomi's face changed. 'Blessed be he by the LORD!' she said. 'The LORD has not abandoned his steadfast loyal love to us — to the living and to the dead alike.' Then her voice dropped: 'That man is one of our kinsman-redeemers. He has the right — and the duty — to redeem what was lost.'"
    },
    "21": {
      "L": "And Ruth the Moabitess said, He said unto me also, Thou shalt keep fast by my young men, until they have ended all my harvest.",
      "M": "Ruth the Moabitess added, 'He also told me to keep close to his workers until they have finished the entire harvest.'",
      "T": "Ruth told her more: 'And he told me to stay with his workers — all the way through to the end of harvest.'"
    },
    "22": {
      "L": "And Naomi said unto Ruth her daughter in law, It is good, my daughter, that thou go out with his maidens, that they meet thee not in any other field.",
      "M": "Naomi said to Ruth her daughter-in-law, 'It is good, my daughter, that you go out with his young women. In someone else's field you could come to harm.'",
      "T": "'Good — do exactly as he says,' Naomi told her. 'Stay with his women workers. In another man's field you would have no protection.'"
    },
    "23": {
      "L": "So she kept fast by the maidens of Boaz to glean unto the end of barley harvest and of wheat harvest; and dwelt with her mother in law.",
      "M": "So Ruth stayed close to the young women of Boaz and gleaned through the end of the barley harvest and the wheat harvest. And she lived with her mother-in-law.",
      "T": "Ruth stayed with Boaz's women workers all the way through the barley harvest and then the wheat harvest — weeks of steady labor. And every evening she came home to Naomi."
    }
  },
  "3": {
    "1": {
      "L": "Then Naomi her mother in law said unto her, My daughter, shall I not seek rest for thee, that it may be well with thee?",
      "M": "Then Naomi her mother-in-law said to her, 'My daughter, shall I not seek a settled resting place for you, where things will go well for you?'",
      "T": "When the harvest was done, Naomi came to Ruth with a plan. 'My daughter,' she said, 'shouldn't I be seeking a settled home for you — a place of rest, a life that is finally secure?'"
    },
    "2": {
      "L": "And now is not Boaz of our kindred, with whose maidens thou wast? Behold, he winnoweth barley to night in the threshingfloor.",
      "M": "Now Boaz — our kinsman — with whose young women you worked: tonight he will be winnowing barley at the threshing floor.",
      "T": "'Boaz — the man whose field you worked in all through harvest. He is our kinsman-redeemer. Tonight he is at the threshing floor, winnowing barley.'"
    },
    "3": {
      "L": "Wash thyself therefore, and anoint thee, and put thy raiment upon thee, and get thee down to the floor; but make not thyself known unto the man, until he shall have done eating and drinking.",
      "M": "Wash yourself, put on fragrant oil, dress yourself in your best garment, and go down to the threshing floor. But do not make yourself known to the man until he has finished eating and drinking.",
      "T": "'Here is what I want you to do: bathe, put on fragrance, dress well. Go down to the threshing floor. But do not let him know you are there until he has eaten and drunk his fill.'"
    },
    "4": {
      "L": "And it shall be, when he lieth down, that thou shalt mark the place where he shall lie, and thou shalt go in, and uncover his feet, and lay thee down; and he will tell thee what thou shalt do.",
      "M": "When he lies down, take note of the place where he lies. Then go, uncover his feet, and lie down. He will tell you what to do.",
      "T": "'When he settles to sleep, take careful note of where he lies. Then go to him quietly, uncover his feet, and lie down. He is a man of integrity — he will tell you what to do next.'"
    },
    "5": {
      "L": "And she said unto her, All that thou sayest unto me I will do.",
      "M": "Ruth said to her, 'I will do everything you say.'",
      "T": "'Whatever you say,' Ruth told her. 'I will do it.'"
    },
    "6": {
      "L": "And she went down unto the floor, and did according to all that her mother in law bade her.",
      "M": "So she went down to the threshing floor and did everything her mother-in-law had instructed.",
      "T": "Ruth went down to the threshing floor and followed Naomi's instructions exactly."
    },
    "7": {
      "L": "And when Boaz had eaten and drunk, and his heart was merry, he went to lie down at the end of the heap of corn; and she came softly, and uncovered his feet, and laid herself down.",
      "M": "When Boaz had eaten and drunk and his heart was glad, he went and lay down at the far end of the grain pile. Then Ruth came quietly, uncovered his feet, and lay down.",
      "T": "Boaz ate well and drank well. His heart was content. He lay down at the far edge of the grain pile to sleep. Ruth moved through the dark as quietly as she could. She uncovered his feet and lay down."
    },
    "8": {
      "L": "And it came to pass at midnight, that the man was afraid, and turned himself; and, behold, a woman lay at his feet.",
      "M": "At midnight the man startled, turned himself, and there — a woman was lying at his feet.",
      "T": "In the deep of the night, something woke Boaz. He turned over — and found a woman lying at his feet in the darkness."
    },
    "9": {
      "L": "And he said, Who art thou? And she answered, I am Ruth thine handmaid; spread therefore thy skirt over thine handmaid; for thou art a near kinsman.",
      "M": "He said, 'Who are you?' She answered, 'I am Ruth, your servant. Spread your garment over your servant, for you are a kinsman-redeemer.'",
      "T": "'Who are you?' he said. 'I am Ruth, your servant,' she answered. 'Spread your garment over me — you are a kinsman-redeemer.' It was a marriage claim, spoken in the legal language of family redemption. The same Hebrew word — wing — that Boaz had used of God's sheltering wings in 2:12 is the word Ruth now uses for the garment of protection she is asking Boaz to extend over her."
    },
    "10": {
      "L": "And he said, Blessed be thou of the LORD, my daughter; for thou hast shewed more kindness in the latter end than at the beginning, inasmuch as thou followedst not young men, whether poor or rich.",
      "M": "He said, 'Blessed be you of the LORD, my daughter. This latter act of faithful kindness is greater than the first. You have not gone after young men, whether poor or rich.'",
      "T": "'You are blessed of the LORD, my daughter,' he said. 'This last act of steadfast loyal love surpasses even the first — your loyalty to Naomi when you came from Moab. You did not chase after young men, poor or rich. You chose the path of covenant faithfulness, not the path of convenience.'"
    },
    "11": {
      "L": "And now, my daughter, fear not; I will do to thee all that thou requirest; for all the city of my people doth know that thou art a virtuous woman.",
      "M": "And now, my daughter, do not be afraid. I will do for you everything you have asked, for all my people in the city know that you are a woman of noble character.",
      "T": "'Do not be afraid,' he said. 'I will do everything you are asking. The whole city knows what you are: a woman of valor — the same word the town uses for a great warrior, a champion. You have earned that name here in Bethlehem.'"
    },
    "12": {
      "L": "And now it is true that I am thy near kinsman; howbeit there is a kinsman that is nearer than I.",
      "M": "And now it is true that I am a kinsman-redeemer. However, there is a kinsman-redeemer closer in line than I.",
      "T": "'I am indeed your kinsman-redeemer. But there is a complication: there is one more closely related to you than I — he stands ahead of me in the order of obligation.'"
    },
    "13": {
      "L": "Tarry this night, and it shall be in the morning, that if he will perform unto thee the part of a kinsman, well; let him do the kinsman's part; but if he will not do the part of a kinsman to thee, then will I do the part of a kinsman to thee, as the LORD liveth; lie down until the morning.",
      "M": "Stay here tonight. In the morning, if he is willing to act as kinsman-redeemer for you, good — let him do so. But if he is not willing, then as the LORD lives, I will act as your kinsman-redeemer. Now lie down until morning.'",
      "T": "'Stay the night. In the morning I will go to the gate. If he chooses to redeem you, let him — he has the right. But if he passes, then as the LORD lives, I will redeem you myself. Now lie down until morning.'"
    },
    "14": {
      "L": "And she lay at his feet until the morning; and she rose up before one could know another; and he said, Let it not be known that a woman came into the floor.",
      "M": "So she lay at his feet until morning. She rose before anyone could recognize another, for he said, 'It must not be known that a woman came to the threshing floor.'",
      "T": "She lay quietly at his feet until the last watch of the night. She rose in the dark, before dawn could show faces, because Boaz had told her: 'No one must know a woman came here tonight.' Both their reputations mattered."
    },
    "15": {
      "L": "Also he said, Bring the vail that thou hast upon thee, and hold it; and when she held it, he measured six measures of barley, and laid it on her; and she went into the city.",
      "M": "He also said, 'Bring the cloak you are wearing and hold it out.' She held it out, and he measured six measures of barley into it and placed it on her. Then she went into the town.",
      "T": "'Hold out your shawl.' She held it open, and he filled it with six measures of barley — a generous load, enough to carry, a visible token that she came from him. He sent her back before daylight."
    },
    "16": {
      "L": "And when she came to her mother in law, she said, Who art thou, my daughter? and she told her all that the man had done to her.",
      "M": "When she came to her mother-in-law, Naomi asked, 'How did things go, my daughter?' And Ruth told her everything the man had done for her.",
      "T": "Back home, Naomi was waiting. 'How did it go, my daughter?' Ruth told her everything — every word, every act, nothing held back."
    },
    "17": {
      "L": "And she said, These six measures of barley gave he me; for he said to me, Go not empty unto thy mother in law.",
      "M": "She added, 'And he gave me these six measures of barley, with the instruction not to go back to my mother-in-law empty-handed.'",
      "T": "'And this grain he sent for you,' Ruth said. 'He told me: do not go back to your mother-in-law empty-handed.' The echo of Naomi's own word from 1:21 was not lost on either of them."
    },
    "18": {
      "L": "Then said she, Sit still, my daughter, until thou know how the matter will fall; for the man will not be in rest, until he have finished the thing this day.",
      "M": "Then Naomi said, 'Stay still, my daughter, until you know how the matter will turn out. The man will not rest until he has settled this today.'",
      "T": "'Now we wait,' Naomi said. 'Sit still and let it unfold. That man will not let the sun set without resolving this — he will settle it today.'"
    }
  },
  "4": {
    "1": {
      "L": "Then went Boaz up to the gate, and sat him down there; and, behold, the kinsman of whom Boaz spake came by; unto whom he said, Ho, such a one! turn aside, sit down here. And he turned aside, and sat down.",
      "M": "Boaz went up to the town gate and sat down there. Just then the kinsman Boaz had mentioned came by. Boaz said, 'Turn aside here, friend — sit down.' He turned aside and sat down.",
      "T": "At first light, Boaz was already at the gate — the ancient courtroom and public square of every Israelite town. And as if providence had arranged the timing, the very man he was looking for came by. 'You there!' Boaz called to him. 'Come here, sit down.' The man sat."
    },
    "2": {
      "L": "And he took ten men of the elders of the city, and said, Sit ye down here; and they sat down.",
      "M": "Then Boaz took ten of the elders of the town and said, 'Sit down here.' They sat down.",
      "T": "Boaz called ten of the town's elders to sit as formal witnesses. They sat. The legal proceeding was convened."
    },
    "3": {
      "L": "And he said unto the kinsman, Naomi, that is come again out of the country of Moab, selleth a parcel of land, which was our brother Elimelech's.",
      "M": "He said to the kinsman, 'Naomi, who has returned from Moab, is selling the piece of land that belonged to our relative Elimelech.'",
      "T": "'Naomi has come back from Moab,' Boaz said to the man. 'She is putting up for sale the field that belonged to Elimelech — our kinsman.'"
    },
    "4": {
      "L": "And I thought to advertise thee, saying, Buy it before the inhabitants, and before the elders of my people; if thou wilt redeem it, redeem it; but if thou wilt not redeem it, then tell me, that I may know; for there is none to redeem it beside thee; and I am after thee. And he said, I will redeem it.",
      "M": "I thought I should inform you of it, saying: Buy it before those sitting here and before the elders of my people. If you will redeem it, do so. But if you will not, tell me, so I may know — for there is no one before you, and I come after you.' The kinsman said, 'I will redeem it.'",
      "T": "'I am required to give you first right of refusal — before these witnesses, before these elders. If you will redeem the field, say so now. If not, tell me, and I am next in line.' The man said, 'I will redeem it.'"
    },
    "5": {
      "L": "Then said Boaz, What day thou buyest the field of the hand of Naomi, thou must buy it also of Ruth the Moabitess, the wife of the dead, to raise up the name of the dead upon his inheritance.",
      "M": "Then Boaz said, 'On the day you acquire the field from Naomi, you also acquire Ruth the Moabitess, the widow of the dead man, to perpetuate the name of the dead on his inheritance.'",
      "T": "Then Boaz played his card. 'The day you buy the field from Naomi, you also take Ruth the Moabitess — the dead man's widow — as your wife, so that his name and line continue in Israel.'"
    },
    "6": {
      "L": "And the kinsman said, I cannot redeem it for myself, lest I mar mine own inheritance; redeem thou my right to thyself; for I cannot redeem it.",
      "M": "The kinsman said, 'I cannot redeem it for myself, or I would risk damaging my own inheritance. Take my right of redemption yourself, for I am unable to redeem it.'",
      "T": "The man's calculation changed visibly. 'I cannot do it,' he said. 'Taking on a wife and her potential heirs would complicate my own estate. Take the right of redemption — I pass.'"
    },
    "7": {
      "L": "Now this was the manner in former time in Israel concerning redeeming and concerning changing, for to confirm all things; a man plucked off his shoe, and gave it to his neighbour; and this was a testimony in Israel.",
      "M": "Now in earlier times in Israel, this was the custom for redeeming and exchanging: to confirm any transaction, a man removed his sandal and gave it to the other party. This was the manner of attestation in Israel.",
      "T": "In those days in Israel, a legal transfer was sealed not with ink but with a sandal. When a man stepped back from a right of redemption, he removed his shoe and handed it to the other party. That sandal was Israel's witnessed deed of transfer."
    },
    "8": {
      "L": "Therefore the kinsman said unto Boaz, Buy it for thee; so he drew off his shoe.",
      "M": "So the kinsman said to Boaz, 'Buy it for yourself.' And he drew off his sandal.",
      "T": "The man said to Boaz, 'It is yours.' He took off his sandal and handed it over."
    },
    "9": {
      "L": "And Boaz said unto the elders, and unto all the people, Ye are witnesses this day, that I have bought all that was Elimelech's, and all that was Chilion's and Mahlon's, of the hand of Naomi.",
      "M": "Then Boaz said to the elders and all the people, 'You are witnesses today that I have purchased from Naomi everything that belonged to Elimelech and to Chilion and Mahlon.'",
      "T": "Boaz turned to face the ten elders and the whole gathered crowd. 'You are all witnesses,' he declared. 'I have today purchased from Naomi the entire estate of Elimelech, Chilion, and Mahlon.'"
    },
    "10": {
      "L": "Moreover Ruth the Moabitess, the wife of Mahlon, have I purchased to be my wife, to raise up the name of the dead upon his inheritance, that the name of the dead be not cut off from among his brethren, and from the gate of his place; ye are witnesses this day.",
      "M": "Moreover, I have also acquired Ruth the Moabitess, Mahlon's widow, as my wife, to preserve the name of the deceased on his inheritance, so that his name will not be cut off from his brothers and from the gate of his hometown. You are witnesses today.'",
      "T": "'And more than that: I have taken Ruth the Moabitess — Mahlon's widow — as my wife, so that the dead man's name will endure in Israel, so that his line will not be erased from this community and from this gate. You are all witnesses today. It is done.'"
    },
    "11": {
      "L": "And all the people that were in the gate, and the elders, said, We are witnesses; the LORD make the woman that is come into thine house like Rachel and like Leah, which two did build the house of Israel; and do thou worthily in Ephratah, and be famous in Bethlehem.",
      "M": "All the people who were at the gate and the elders said, 'We are witnesses. May the LORD make this woman who is entering your house like Rachel and Leah, who together built the house of Israel. And may you be powerful in Ephrathah and famous in Bethlehem.'",
      "T": "The people spoke with one voice: 'We are witnesses.' Then the blessing came: 'May the LORD make this woman who enters your home like Rachel and Leah — the two mothers who built the whole house of Israel. May you prosper in Ephrathah and your name ring out in Bethlehem.'"
    },
    "12": {
      "L": "And let thy house be like the house of Pharez, whom Tamar bare unto Judah, of the seed which the LORD shall give thee of this young woman.",
      "M": "And may your house be like the house of Perez, whom Tamar bore to Judah — from the offspring the LORD gives you through this young woman.'",
      "T": "'May your household be like the house of Perez — born of Tamar's bold, covenant-driven faithfulness to the line of Judah. May the LORD give you sons through this woman worthy of that lineage.' The crowd was invoking women who had stood outside the expected path and yet carried the covenant forward."
    },
    "13": {
      "L": "So Boaz took Ruth, and she was his wife; and when he went in unto her, the LORD gave her conception, and she bare a son.",
      "M": "So Boaz took Ruth, and she became his wife. When he went in to her, the LORD enabled her to conceive, and she bore a son.",
      "T": "Boaz married Ruth. The LORD opened her womb — she had been barren through the years in Moab — and she bore a son. After so much emptiness, there was life."
    },
    "14": {
      "L": "And the women said unto Naomi, Blessed be the LORD, which hath not left thee this day without a kinsman, that his name may be famous in Israel.",
      "M": "The women said to Naomi, 'Blessed be the LORD, who has not left you this day without a kinsman-redeemer. May his name be renowned in Israel.'",
      "T": "The women of Bethlehem came to Naomi. 'Blessed be the LORD,' they said, 'who has not abandoned you without a kinsman-redeemer. May this child's name become great in Israel.'"
    },
    "15": {
      "L": "And he shall be unto thee a restorer of life, and a nourisher of thine old age; for thy daughter in law, which loveth thee, which is better to thee than seven sons, hath born him.",
      "M": "He will restore your life and sustain you in your old age, for your daughter-in-law who loves you has borne him — she who is better to you than seven sons.'",
      "T": "'He will restore your life, Naomi — nourish you through old age. And he was born of the daughter-in-law who loves you, who is worth more to you than seven sons.' What began with bitterness has ended with abundance beyond measure."
    },
    "16": {
      "L": "And Naomi took the child, and laid it in her bosom, and became nurse unto it.",
      "M": "Naomi took the child and laid him against her chest and became his nurse.",
      "T": "Naomi took the baby into her arms, held him against her heart, and became his nurse and foster mother. The woman who had named herself Mara — Bitter — was full again."
    },
    "17": {
      "L": "And the women her neighbours gave it a name, saying, There is a son born to Naomi; and they called his name Obed; he is the father of Jesse, the father of David.",
      "M": "The neighboring women gave him his name, saying, 'A son has been born to Naomi.' They named him Obed. He was the father of Jesse, the father of David.",
      "T": "The women neighbors named the child, calling out to the street: 'A son has been born to Naomi!' They named him Obed — 'Servant.' And here the book reveals what it has been building toward: Obed became the father of Jesse. Jesse became the father of David. The Moabite woman's faithfulness ran in a straight line to the throne of Israel."
    },
    "18": {
      "L": "Now these are the generations of Pharez; Pharez begat Hezron,",
      "M": "Now these are the generations of Perez: Perez fathered Hezron,",
      "T": "And this is the covenant line from Perez to David — the genealogy that proves Ruth belongs to the story of redemption:"
    },
    "19": {
      "L": "And Hezron begat Ram, and Ram begat Amminadab,",
      "M": "Hezron fathered Ram, Ram fathered Amminadab,",
      "T": "Perez fathered Hezron, Hezron fathered Ram, Ram fathered Amminadab,"
    },
    "20": {
      "L": "And Amminadab begat Nahshon, and Nahshon begat Salmon,",
      "M": "Amminadab fathered Nahshon, Nahshon fathered Salmon,",
      "T": "Amminadab fathered Nahshon, Nahshon fathered Salmon,"
    },
    "21": {
      "L": "And Salmon begat Boaz, and Boaz begat Obed,",
      "M": "Salmon fathered Boaz, Boaz fathered Obed,",
      "T": "Salmon fathered Boaz, Boaz fathered Obed,"
    },
    "22": {
      "L": "And Obed begat Jesse, and Jesse begat David.",
      "M": "Obed fathered Jesse, and Jesse fathered David.",
      "T": "Obed fathered Jesse, Jesse fathered David. The foreign woman who said 'your God is my God' became the great-grandmother of Israel's greatest king."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ruth')
        merge_tier(existing, RUTH, tier_key)
        save(tier_dir, 'ruth', existing)
    print('Ruth 1–4 written.')

if __name__ == '__main__':
    main()
