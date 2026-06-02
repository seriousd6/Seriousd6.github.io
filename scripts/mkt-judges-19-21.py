"""
MKT Judges chapters 19–21 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-judges-19-21.py

Covers: The Levite and his concubine — hospitality, gang-rape, and dismemberment at Gibeah
(ch. 19); the inter-tribal war against Benjamin — three-day battle, near-annihilation of
Benjamin (ch. 20); Israel's desperate measures to preserve the Benjamite remnant through
the Jabesh-gilead massacre and the Shiloh abduction (ch. 21).

These chapters function as the darkest anti-climax in Judges, deliberately echoing and
inverting Genesis 19 (Lot/Sodom): both feature a male traveler, a hospitable host, a mob
demanding sexual violation, an offered daughter, and a divine reckoning. But in Gibeah the
concubine is actually handed over, violated to death, and dismembered. The episode implicates
everyone — the Levite who threw her out, the host who offered her, the mob, and the Levite
who coolly ate breakfast beside her corpse. The civil war that follows is massive and
theologically complex: Israel seeks divine guidance yet suffers catastrophic defeat twice
before the third assault succeeds. Ch. 21 resolves the demographic crisis through two further
atrocities (killing Jabesh-gilead, mass abduction at Shiloh), and the book ends on the
same frame-note as 17:6: "no king… everyone did what was right in their own eyes."

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) L/M; "the LORD" T — consistent with all
  prior OT scripts
- H430 (אֱלֹהִים): "God" all tiers when divine; "god/gods" when pagan
- H5039 (נְבָלָה): "folly/outrage" — this is the key word in 19:23-24 and 20:6,10. The same
  term is used for Dinah's rape (Gen 34:7) and Tamar's rape (2 Sam 13:12). It means covenant-
  shattering disgrace, not merely "foolishness." L: "folly/outrageous thing"; M: "outrage";
  T: "outrage" with interpretive weight applied in context
- H1100 (בְּנֵי-בְלִיַּעַל): "sons of Belial" L; "worthless/depraved fellows" M; "lawless men"
  / "predators" T — same term as the Abimelech narrative
- H6370 (פִּילֶגֶשׁ): "concubine" all tiers — she is a secondary wife with covenant status
  but fewer legal protections than a primary wife; L preserves the social reality
- H2181 (זָנָה): in 19:2 "played the whore against him" L; "was unfaithful to him" M;
  "broke faith with him" T — the LXX reads "was angry at him" (ὀργίσθη), but MT זָנָה
  is the standard term for covenant infidelity; T uses covenant language
- H7307 (רוּחַ): not a major term in chs. 19-21
- H2617 (חֶסֶד): absent in these chapters — that absence is the point; the entire catastrophe
  unfolds because no חֶסֶד (covenant loyalty) operates in Israel; T surfaces this in key
  verses (esp. ch. 19's refusal of hospitality)
- H7621 (שְׁבוּעָה): "oath" all tiers — the oath not to give daughters to Benjamin (21:1)
  drives the entire logic of ch. 21; T makes the oath's perverse consequences explicit
- H2764 (חֵרֶם): "devoted to destruction" / "utterly destroy" in 21:11 — the same holy-war
  term used against Canaanites is here applied to Jabesh-gilead (an Israelite city)
- 20:18,23,28 — Israel consults the LORD at Bethel, not Shiloh; the ark was at Bethel at
  this time (cf. 20:27-28 naming Phinehas son of Eleazar); this is pre-monarchic chronology.
  The LORD says "Go up" twice before Israel loses catastrophically — this is theologically
  deliberate: their obedience did not guarantee victory until genuine repentance (fasting,
  weeping, offerings in 20:26). T notes the distinction between divine authorization and
  divine guarantee.
- 19:28 note: the text never explicitly states the concubine was dead before the Levite
  spoke to her ("Get up, let us go"); whether she died from the abuse during the night or
  from her wounds later is intentionally ambiguous. T treats her as dead based on "she did
  not answer" and 19:29's dismemberment without qualification.
- 20:43 note: "trode them down with ease / from Nohah" — the Hebrew is difficult; the town
  Nohah (מְנוּחָה) may be a place name or the adverbial "without respite"; M and T use
  different solutions; L preserves the ambiguity
- 21:22 note: the "legal loophole" argument used here is morally sophistic — the elders
  claim the fathers aren't "giving" their daughters (which the oath prohibited) because the
  Benjamites are seizing them; T exposes this as rationalization without editorializing
- Jotham's-fable style from ch. 9 (line-breaks in T for poetic text) does not apply here;
  these chapters are prose narrative throughout
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
  "19": {
    "1": {
      "L": "And it came to pass in those days, when there was no king in Israel, that there was a certain Levite sojourning on the far side of the hill country of Ephraim, who took to himself a concubine from Bethlehem in Judah.",
      "M": "In those days, when there was no king in Israel, a certain Levite who was living in the remote part of the hill country of Ephraim took a concubine from Bethlehem in Judah.",
      "T": "In those days when Israel had no king, a Levite made his home in the far reaches of the Ephraimite highlands. He had taken a concubine from Bethlehem in Judah."
    },
    "2": {
      "L": "But his concubine played the whore against him, and went away from him unto her father's house to Bethlehem in Judah, and was there four months.",
      "M": "But his concubine was unfaithful to him and left, going back to her father's house at Bethlehem in Judah, where she stayed four months.",
      "T": "But his concubine broke faith with him and left, making her way back to her father's house in Bethlehem, where she remained four months."
    },
    "3": {
      "L": "And her husband arose and went after her to speak to her heart, to bring her back, having his servant with him and a couple of asses; and she brought him into her father's house, and when the father of the young woman saw him, he rejoiced to meet him.",
      "M": "Her husband set out after her to speak tenderly to her and bring her back. He had his servant with him and a pair of donkeys. She brought him into her father's house, and the young woman's father was glad to see him.",
      "T": "Her husband went after her, hoping to win her back with gentle words. He took his servant and two donkeys. She brought him inside her father's house, and her father was genuinely glad to welcome him."
    },
    "4": {
      "L": "And his father-in-law, the young woman's father, held him fast, and he stayed with him three days; so they ate and drank and lodged there.",
      "M": "His father-in-law, the young woman's father, urged him to stay, and he remained three days. They ate and drank and spent the nights there.",
      "T": "His father-in-law pressed him to stay, and the days slipped by — three days of eating and drinking in the house."
    },
    "5": {
      "L": "And it came to pass on the fourth day, when they arose early in the morning, that he rose up to depart; and the young woman's father said unto his son-in-law, Comfort thine heart with a morsel of bread, and afterward thou shalt go thy way.",
      "M": "On the fourth day they rose early and he prepared to leave. But the young woman's father said to his son-in-law, “Sustain yourself with a bite of bread, and after that you may go.”",
      "T": "On the fourth morning he rose early to leave. His father-in-law said, “Have something to eat first — then go.”"
    },
    "6": {
      "L": "So they sat down, and the two of them ate and drank together; and the young woman's father said unto the man, Be content, I pray thee, and tarry all night, and let thine heart be merry.",
      "M": "So they sat down and ate and drank together. Then the young woman's father said, “Please be willing to spend the night and enjoy yourself.”",
      "T": "They sat and ate together. The father pressed again: “Stay the night — rest, enjoy yourself.”"
    },
    "7": {
      "L": "And when the man rose up to depart, his father-in-law urged him; therefore he lodged there again.",
      "M": "When the man rose to leave, his father-in-law urged him, so he spent another night there.",
      "T": "The man got up to go, but his father-in-law kept pressing, and he stayed another night."
    },
    "8": {
      "L": "And he arose early in the morning on the fifth day to depart; and the young woman's father said, Comfort thine heart, I pray thee. And they tarried until the afternoon, and they did eat both of them.",
      "M": "When he rose early on the fifth day to leave, the young woman's father said, “Please strengthen yourself.” So they lingered until afternoon, and the two of them ate.",
      "T": "He rose early on the fifth morning to go. Again his father-in-law said, “Eat something first.” They lingered until the afternoon."
    },
    "9": {
      "L": "And when the man rose up to depart, he and his concubine and his servant, his father-in-law, the young woman's father, said unto him, Behold, now the day draweth toward evening, I pray you tarry all night; behold, the day groweth to an end, lodge here, that thine heart may be merry; and to morrow get thee early on thy way, that thou mayest go home.",
      "M": "When the man rose to go — he and his concubine and his servant — his father-in-law said to him, “Look, the day is wearing on toward evening. Please spend the night. See, the day is nearly gone. Stay the night, enjoy yourself, and tomorrow rise early and go home.”",
      "T": "When the man finally rose to leave — he, his concubine, and his servant — his father-in-law made one last appeal: “The day is nearly spent. Stay one more night. Rise early tomorrow and go home.” Four days of delay had already cost them."
    },
    "10": {
      "L": "But the man would not tarry that night, but he rose up and departed, and came over against Jebus, which is Jerusalem; and there were with him two asses saddled, his concubine also was with him.",
      "M": "But the man would not spend another night. He rose and departed with his two saddled donkeys and his concubine, and they came as far as Jebus, which is Jerusalem.",
      "T": "But this time he refused to stay. He set out with his concubine and his two saddled donkeys and traveled as far as Jebus — the city that is Jerusalem."
    },
    "11": {
      "L": "And when they were by Jebus, the day was far spent; and the servant said unto his master, Come, I pray thee, and let us turn in into this city of the Jebusites, and lodge in it.",
      "M": "When they were near Jebus, the day was nearly gone. The servant said to his master, “Come, let us stop at this Jebusite city and spend the night here.”",
      "T": "As they passed near Jebus the day was almost gone. The servant said, “Let's stop here — spend the night in this city.”"
    },
    "12": {
      "L": "And his master said unto him, We will not turn aside into the city of a foreigner that is not of the children of Israel; we will pass over to Gibeah.",
      "M": "But his master said to him, “We will not stop in a city of foreigners, people who are not Israelites. We will go on to Gibeah.”",
      "T": "His master said, “No — I won't sleep in a foreign city. We push on to Gibeah.” A fatal choice."
    },
    "13": {
      "L": "And he said unto his servant, Come, and let us draw near to one of these places, and we will lodge in Gibeah, or in Ramah.",
      "M": "He said to his servant, “Come, let us reach one of these towns and spend the night — either at Gibeah or at Ramah.”",
      "T": "He told his servant, “We'll stop at one of those Israelite towns — Gibeah or Ramah — and bed down for the night.”"
    },
    "14": {
      "L": "And they passed on and went their way; and the sun went down upon them when they were by Gibeah, which belongeth to Benjamin.",
      "M": "So they passed on and went their way. The sun set on them just as they reached Gibeah, which belongs to Benjamin.",
      "T": "They pressed on, and the sun set as they arrived at Gibeah, a town belonging to Benjamin."
    },
    "15": {
      "L": "And they turned aside thither, to go in and to lodge in Gibeah; and when he went in, he sat him down in a street of the city, for there was no man that took them into his house to lodge.",
      "M": "They turned aside there to spend the night at Gibeah. The man entered and sat down in the town square, for no one would take them in to spend the night.",
      "T": "They turned in to spend the night at Gibeah. The Levite sat in the town square — and no one came out to offer them shelter. Not one person."
    },
    "16": {
      "L": "And behold, there came an old man from his work out of the field at even, who also was of the hill country of Ephraim; and he sojourned in Gibeah, but the men of the place were Benjamites.",
      "M": "As evening came, an old man came in from his work in the fields. He was from the hill country of Ephraim and was living as a resident alien in Gibeah, though the people of the town were Benjamites.",
      "T": "At evening an old man came in from the fields. He was from the Ephraimite highlands — a sojourner in Gibeah, not a native — for the townspeople were Benjamites."
    },
    "17": {
      "L": "And when he lifted up his eyes, he saw a wayfaring man in the street of the city; and the old man said, Whither goest thou? and whence comest thou?",
      "M": "He looked up and saw the traveler in the town square. The old man asked, “Where are you going? Where do you come from?”",
      "T": "He looked up and saw the traveler sitting in the square. “Where are you headed?” he asked. “Where do you come from?”"
    },
    "18": {
      "L": "And he said unto him, We are passing from Bethlehem in Judah to the far sides of the hill country of Ephraim; from thence am I, and I went to Bethlehem in Judah, and I am now going toward the house of the LORD; but there is no man that receiveth me into his house.",
      "M": "He said, “We are traveling from Bethlehem in Judah to the remote part of the hill country of Ephraim. That is where I am from. I went to Bethlehem in Judah and now I am going home. But no one here has taken me in.”",
      "T": "The Levite answered: “We're traveling from Bethlehem back to the far side of the Ephraimite highlands — that's my home. I went down to Bethlehem and now I'm heading back. But not a soul in this town has opened a door to us.”"
    },
    "19": {
      "L": "Yet there is both straw and provender for our asses; and there is bread and wine also for me, and for thy handmaid, and for the young man which is with thy servants; there is no want of any thing.",
      "M": "We have straw and fodder for our donkeys, and we have bread and wine for myself and your female servant and the young man with us — we are not asking for anything.",
      "T": "We have everything we need — fodder for the donkeys, bread and wine for myself, my concubine, and my servant. We ask only for shelter.“"
    },
    "20": {
      "L": "And the old man said, Peace be to thee; howsoever let all thy wants lie upon me; only lodge not in the street.",
      "M": "And the old man said, “Peace to you. I will take care of whatever you need. Only, do not spend the night in the square.”",
      "T": "The old man said, “Peace to you — you are welcome here. Whatever you need is on me. Only, do not sleep in the open square.”"
    },
    "21": {
      "L": "So he brought him into his house, and gave fodder unto the asses; and they washed their feet, and did eat and drink.",
      "M": "He brought them into his house and gave fodder to the donkeys. They washed their feet and ate and drank.",
      "T": "He brought them inside, fed the donkeys, and they washed the road from their feet and sat down to eat and drink."
    },
    "22": {
      "L": "Now as they were making their hearts merry, behold, the men of the city, certain sons of Belial, beset the house round about, and beat at the door, and spake to the master of the house, the old man, saying, Bring forth the man that came into thine house, that we may know him.",
      "M": "While they were enjoying themselves, the men of the city — certain worthless men — surrounded the house and pounded on the door. They said to the master of the house, the old man, “Bring out the man who came into your house so that we may have sexual relations with him.”",
      "T": "While they were still eating and drinking, the house was surrounded. A mob of lawless men from the city hammered on the door and shouted at the old man: “Send out the man who came to your house — we want him.”"
    },
    "23": {
      "L": "And the man, the master of the house, went out unto them, and said unto them, Nay, my brethren, nay, I pray you, do not this folly; seeing that this man is come into mine house, do not this outrageous thing.",
      "M": "And the man, the master of the house, went out to them and said, “No, my brothers, do not act so wickedly. This man has come into my house — do not commit this outrage.”",
      "T": "The old man went out to face them: “No, my brothers — no! Don't do this wicked thing. This man is a guest in my house. You must not commit this outrage.”"
    },
    "24": {
      "L": "Behold, here is my daughter a maiden, and his concubine; them I will bring out now, and humble ye them, and do with them what seemeth good unto you; but unto this man do not so vile a thing.",
      "M": "Behold, here are my virgin daughter and his concubine. I will bring them out. Do with them whatever seems good to you, but to this man do not do this disgraceful thing.",
      "T": "Look — I have a virgin daughter, and this man has a concubine. I will bring them out. Do with them as you will. Only do not do this shameful thing to my male guest."
    },
    "25": {
      "L": "But the men would not hearken to him; so the man took his concubine, and brought her forth unto them outside; and they knew her, and abused her all the night until the morning; and when the day began to spring, they let her go.",
      "M": "But the men would not listen to him. So the man seized his concubine and put her outside to them. They violated her and abused her all through the night until morning. At daybreak they released her.",
      "T": "The men would not listen. So the Levite seized his concubine and threw her out to them. They violated her and brutalized her all night long until dawn, then let her go."
    },
    "26": {
      "L": "Then came the woman in the dawning of the day, and fell down at the door of the man's house where her lord was, till it was light.",
      "M": "At dawn the woman came back and collapsed at the door of the man's house where her lord was, and lay there until daylight.",
      "T": "At the first gray light she dragged herself to the door of the house where her lord was and fell there, her hands on the threshold."
    },
    "27": {
      "L": "And her lord rose up in the morning, and opened the doors of the house, and went out to go on his way; and behold, the woman his concubine was fallen down at the door of the house, with her hands upon the threshold.",
      "M": "Her lord rose in the morning, opened the doors of the house, and went out to continue his journey — and there was his concubine, fallen at the door of the house with her hands on the threshold.",
      "T": "In the morning her lord opened the door to leave — and there she was. His concubine, fallen at the threshold, her hands still reaching toward the door."
    },
    "28": {
      "L": "And he said unto her, Up, and let us be going. But none answered. Then the man put her upon an ass, and the man rose up, and gat him unto his place.",
      "M": "He said to her, “Get up. We are going.” But there was no answer. He loaded her onto the donkey and set out for home.",
      "T": "He said to her, “Get up. We're going.” She did not answer. He lifted her body onto the donkey and rode home."
    },
    "29": {
      "L": "And when he was come into his house, he took a knife, and laid hold on his concubine, and divided her, together with her bones, into twelve pieces, and sent her throughout all the coasts of Israel.",
      "M": "When he arrived home, he took a knife, took hold of his concubine, and cut her into twelve pieces, limb by limb, and sent her throughout all the territory of Israel.",
      "T": "When he reached home, he took a knife and dismembered her — bones and all — into twelve pieces, and sent one piece to each of the twelve territories of Israel."
    },
    "30": {
      "L": "And it was so, that all who saw it said, There was no such deed done nor seen from the day that the children of Israel came up out of the land of Egypt unto this day; consider of it, take advice, and speak.",
      "M": "And everyone who saw it said, “Nothing like this has happened or been seen from the day the people of Israel came up from the land of Egypt until this day. Think about it. Take counsel. Speak.”",
      "T": "Everyone who saw it said the same: “Nothing like this has happened in Israel since the day we came up from Egypt. Look at it. Think. Say something.”"
    }
  },
  "20": {
    "1": {
      "L": "Then all the children of Israel went out, and the congregation was assembled as one man, from Dan even to Beersheba, with the land of Gilead, unto the LORD at Mizpah.",
      "M": "Then all the people of Israel came out as one, and the congregation assembled — from Dan to Beersheba, including the land of Gilead — before the LORD at Mizpah.",
      "T": "All Israel came out as one — from Dan in the far north to Beersheba in the south, and the people of Gilead besides — and assembled before the LORD at Mizpah."
    },
    "2": {
      "L": "And the chief of all the people, even of all the tribes of Israel, presented themselves in the assembly of the people of God, four hundred thousand footmen that drew sword.",
      "M": "The chiefs of all the tribes of Israel took their places in the assembly of the people of God — four hundred thousand foot soldiers who drew the sword.",
      "T": "The commanders of every tribe of Israel took their places in this great assembly before God. Four hundred thousand swords were present."
    },
    "3": {
      "L": "Now the children of Benjamin heard that the children of Israel were gone up to Mizpah. Then said the children of Israel, Tell us, how was this wickedness?",
      "M": "The Benjamites heard that the people of Israel had gone up to Mizpah. And the people of Israel said, “Tell us — how did this evil come about?”",
      "T": "Benjamin heard that all Israel had gathered at Mizpah. The assembly said, “Tell us — how did this atrocity happen?”"
    },
    "4": {
      "L": "And the Levite, the husband of the woman that was slain, answered and said, I came into Gibeah that belongeth to Benjamin, I and my concubine, to lodge.",
      "M": "The Levite, the husband of the murdered woman, answered and said, “I came with my concubine to Gibeah in Benjamin to spend the night.",
      "T": "The Levite — the murdered woman's husband — stood and testified: “My concubine and I came to Gibeah in Benjamin to spend the night."
    },
    "5": {
      "L": "And the men of Gibeah rose against me, and beset the house round about upon me by night, and thought to have slain me; and my concubine have they forced, that she is dead.",
      "M": "The men of Gibeah rose up against me and surrounded the house by night. They intended to kill me. But they seized my concubine and violated her until she died.",
      "T": "The men of Gibeah surrounded the house that night to kill me. They seized my concubine instead and abused her until she died."
    },
    "6": {
      "L": "And I took my concubine, and cut her in pieces, and sent her throughout all the country of the inheritance of Israel; for they have committed lewdness and outrageous folly in Israel.",
      "M": "So I took my concubine and cut her into pieces and sent her throughout all the territory of Israel, because they have committed an outrage and a disgraceful thing in Israel.",
      "T": "I cut her body in pieces and sent it across every part of Israel, because what was done in Gibeah is a covenant-shattering outrage — and all Israel must judge it."
    },
    "7": {
      "L": "Behold, ye are all children of Israel; give here your advice and counsel.",
      "M": "Behold, you are all the people of Israel. Give your verdict and counsel.",
      "T": "You are all Israel. This moment belongs to you — speak, decide, act."
    },
    "8": {
      "L": "And all the people arose as one man, saying, We will not any of us go to his tent, neither will we any of us turn into his house.",
      "M": "All the people rose as one, saying, “Not one of us will go to his tent, nor will any of us return to his house.",
      "T": "Every man rose as one. “None of us goes home. Not one of us returns to his tent.”"
    },
    "9": {
      "L": "But now this shall be the thing which we will do to Gibeah; we will go up against it by lot.",
      "M": "But this is what we will do to Gibeah: we will go up against it by lot.",
      "T": "This is what we do to Gibeah: we march on it, and we decide the order by lot."
    },
    "10": {
      "L": "And we will take ten men of an hundred throughout all the tribes of Israel, and an hundred of a thousand, and a thousand out of ten thousand, to fetch victual for the people, that they may do, when they come to Gibeah of Benjamin, according to all the folly that they have wrought in Israel.",
      "M": "We will take ten men out of every hundred throughout all the tribes of Israel — a hundred from every thousand, a thousand from every ten thousand — to gather supplies for the army, so that when they reach Gibeah in Benjamin they may repay all the outrage that has been committed in Israel.",
      "T": "We will conscript one in ten to supply the army, so that when the rest arrive at Gibeah they can deal with its crime as it deserves."
    },
    "11": {
      "L": "So all the men of Israel were gathered against the city, knit together as one man.",
      "M": "So all the men of Israel gathered against the city, united as one man.",
      "T": "All Israel's fighting men gathered against Gibeah, bound together like a single fist."
    },
    "12": {
      "L": "And the tribes of Israel sent men through all the tribe of Benjamin, saying, What wickedness is this that is done among you?",
      "M": "The tribes of Israel sent men through all the tribe of Benjamin, saying, “What is this evil that has been done among you?",
      "T": "But first the tribes sent envoys through all of Benjamin: “What is this evil that has been done among you?”"
    },
    "13": {
      "L": "Now therefore deliver us the men, the sons of Belial, which are in Gibeah, that we may put them to death, and put away evil from Israel. But the children of Benjamin would not hearken to the voice of their brethren the children of Israel.",
      "M": "Now hand over the worthless men — the lawless men in Gibeah — so that we may put them to death and purge the evil from Israel.“ But the Benjamites would not listen to their brothers the Israelites.",
      "T": "Surrender the guilty men of Gibeah so we can execute them and purge this evil from Israel.“ But Benjamin would not listen to their brothers."
    },
    "14": {
      "L": "But the children of Benjamin gathered themselves together out of the cities unto Gibeah, to go out to battle against the children of Israel.",
      "M": "Instead, the Benjamites rallied from their cities to Gibeah to go to war against the people of Israel.",
      "T": "Instead, Benjamin mustered from every city, converging on Gibeah to make war against the rest of Israel."
    },
    "15": {
      "L": "And the children of Benjamin were numbered at that time out of the cities twenty and six thousand men that drew sword, beside the inhabitants of Gibeah, which were numbered seven hundred chosen men.",
      "M": "The Benjamites were counted at that time — twenty-six thousand swordsmen from their cities, besides seven hundred chosen men from Gibeah.",
      "T": "Benjamin's forces: twenty-six thousand swordsmen from across the tribe, plus seven hundred elite fighters from Gibeah itself."
    },
    "16": {
      "L": "Among all this people there were seven hundred chosen men left-handed; every one could sling stones at an hair breadth, and not miss.",
      "M": "Among all these were seven hundred chosen left-handed men — every one of them able to sling a stone to a hair's breadth without missing.",
      "T": "Among them were seven hundred specialized left-handed slingers, each able to hit a target the width of a hair without missing."
    },
    "17": {
      "L": "And the men of Israel, beside Benjamin, were numbered four hundred thousand men that drew sword; all these were men of war.",
      "M": "The men of Israel, apart from Benjamin, were mustered at four hundred thousand swordsmen — all of them fighting men.",
      "T": "Israel's forces, excluding Benjamin, numbered four hundred thousand swords — every one a trained soldier."
    },
    "18": {
      "L": "And the children of Israel arose, and went up to the house of God, and asked counsel of God, and said, Which of us shall go up first to the battle against the children of Benjamin? And the LORD said, Judah shall go up first.",
      "M": "The people of Israel arose and went up to Bethel and inquired of God. They said, “Which of us shall go up first to battle against the Benjamites?” And the LORD said, “Judah shall go up first.”",
      "T": "Before marching, Israel went to Bethel and sought God's direction: “Who leads the attack against Benjamin?” The LORD answered: “Judah goes first.”"
    },
    "19": {
      "L": "And the children of Israel rose up in the morning, and encamped against Gibeah.",
      "M": "The people of Israel rose up in the morning and encamped against Gibeah.",
      "T": "Israel rose at dawn and deployed against Gibeah."
    },
    "20": {
      "L": "And the men of Israel went out to battle against Benjamin; and the men of Israel put themselves in array to fight against them at Gibeah.",
      "M": "The men of Israel went out to battle against Benjamin and drew up their battle line against them at Gibeah.",
      "T": "Israel marched out and formed up for battle before Gibeah."
    },
    "21": {
      "L": "And the children of Benjamin came forth out of Gibeah, and destroyed down to the ground of the Israelites that day twenty and two thousand men.",
      "M": "The Benjamites came out of Gibeah and cut down twenty-two thousand men of Israel to the ground that day.",
      "T": "Benjamin sallied out of Gibeah and cut down twenty-two thousand Israelites. A shattering defeat — God had said \“go,\” and Israel had still lost."
    },
    "22": {
      "L": "And the people the men of Israel encouraged themselves, and set their battle again in array in the place where they put themselves in array the first day.",
      "M": "But the people, the men of Israel, took courage and formed up their battle line again in the same place as on the first day.",
      "T": "The men of Israel steeled themselves and returned to the same battle position as before."
    },
    "23": {
      "L": "And the children of Israel went up and wept before the LORD until evening, and asked counsel of the LORD, saying, Shall I go up again to battle against the children of Benjamin my brother? And the LORD said, Go up against him.",
      "M": "The people of Israel went up and wept before the LORD until evening. They asked the LORD, “Shall we again go out to battle against our brother Benjamin?” And the LORD said, “Go up against him.”",
      "T": "They went to Bethel and wept before the LORD until evening, then asked: “Do we go back out against our brother Benjamin?” The LORD again said, “Go up against him.” Divine authorization was given — but divine guarantee was not yet."
    },
    "24": {
      "L": "And the children of Israel came near against the children of Benjamin the second day.",
      "M": "The people of Israel advanced against the Benjamites on the second day.",
      "T": "So Israel advanced against Benjamin a second time."
    },
    "25": {
      "L": "And Benjamin went forth against them out of Gibeah the second day, and destroyed down to the ground of the children of Israel again eighteen thousand men; all these drew the sword.",
      "M": "Benjamin came out of Gibeah against them on the second day and struck down eighteen thousand more men of Israel — all of them swordsmen.",
      "T": "Again Benjamin came out of Gibeah and cut down eighteen thousand more Israelite swordsmen. Two days. Forty thousand dead. And still no king."
    },
    "26": {
      "L": "Then all the children of Israel, and all the people, went up, and came to the house of God, and wept, and sat there before the LORD, and fasted that day until even, and offered burnt offerings and peace offerings before the LORD.",
      "M": "Then all the people of Israel, the whole congregation, went up to Bethel and wept. They sat before the LORD and fasted that day until evening, and offered burnt offerings and peace offerings before the LORD.",
      "T": "Now all Israel — the whole nation — went up to Bethel. They wept before the LORD, sat fasting until evening, and offered burnt offerings and fellowship offerings. This time they came not merely for tactical advice but in genuine grief and repentance."
    },
    "27": {
      "L": "And the children of Israel enquired of the LORD, (for the ark of the covenant of God was there in those days,",
      "M": "And the people of Israel inquired of the LORD. (The ark of the covenant of God was there in those days,",
      "T": "(In those days the ark of God's covenant was kept at Bethel — Israel could seek the LORD directly:"
    },
    "28": {
      "L": "And Phinehas, the son of Eleazar, the son of Aaron, stood before it in those days,) saying, Shall I yet again go out to battle against the children of Benjamin my brother, or shall I cease? And the LORD said, Go up; for to morrow I will deliver them into thine hand.",
      "M": "and Phinehas the son of Eleazar, son of Aaron, ministered before it in those days.) They said, “Shall we go out again to battle against our brother Benjamin, or shall we stop?” The LORD said, “Go up, for tomorrow I will give them into your hand.”",
      "T": "Phinehas son of Eleazar son of Aaron ministered before it.) They asked: “Do we attack Benjamin again, or do we stop?” This time the LORD answered with a promise: “Go up. Tomorrow I will hand them over to you.”"
    },
    "29": {
      "L": "And Israel set liers in wait round about Gibeah.",
      "M": "So Israel set ambushes all around Gibeah.",
      "T": "Israel placed hidden forces all around Gibeah."
    },
    "30": {
      "L": "And the children of Israel went up against the children of Benjamin on the third day, and put themselves in array against Gibeah, as at other times.",
      "M": "The people of Israel went up against the Benjamites on the third day and formed up against Gibeah as before.",
      "T": "On the third day Israel marched against Benjamin with the same front as before — but this time the ambush lay waiting."
    },
    "31": {
      "L": "And the children of Benjamin went out against the people, and were drawn away from the city; and they began to smite of the people, and kill, as at other times, in the highways, of which one goeth up to the house of God, and the other to Gibeah in the field, about thirty men of Israel.",
      "M": "The Benjamites went out against the people and were lured away from the city. They began to strike down and kill men as before — about thirty fell in the open roads, one group on the way up toward Bethel and the other toward Gibeah in the field.",
      "T": "Benjamin came out and was drawn away from the city, just as planned. They began killing Israelites as before — about thirty men — along the roads toward Bethel and in the open field."
    },
    "32": {
      "L": "And the children of Benjamin said, They are smitten down before us, as at the first. But the children of Israel said, Let us flee, and draw them from the city unto the highways.",
      "M": "The Benjamites said, “They are falling before us as before.” But the Israelites had said to each other, “Let us flee and draw them away from the city toward the roads.”",
      "T": "Benjamin thought, “We're winning again!” But Israel's retreat was deliberate — they were pulling Benjamin away from the city and onto open ground."
    },
    "33": {
      "L": "And all the men of Israel rose up out of their place, and put themselves in array at Baal-tamar; and the liers in wait of Israel came forth out of their place, even out of the meadows of Gibeah.",
      "M": "All the men of Israel rose from their place and formed up at Baal-tamar, and the Israelite ambush broke out from its position west of Gibeah.",
      "T": "At Baal-tamar Israel wheeled and formed their line — and the hidden ambush erupted from the west side of Gibeah."
    },
    "34": {
      "L": "And there came against Gibeah ten thousand chosen men out of all Israel, and the battle was sore; but they knew not that evil was near upon them.",
      "M": "Ten thousand chosen men from all Israel struck against Gibeah itself, and the battle was fierce. But the Benjamites did not realize that disaster was closing in on them.",
      "T": "Ten thousand picked fighters from all Israel crashed into Gibeah itself. The fighting was savage — and Benjamin still did not understand that the trap had shut."
    },
    "35": {
      "L": "And the LORD smote Benjamin before Israel; and the children of Israel destroyed of the Benjamites that day twenty and five thousand and an hundred men; all these drew the sword.",
      "M": "The LORD struck down Benjamin before Israel. The people of Israel destroyed twenty-five thousand one hundred Benjamite swordsmen that day.",
      "T": "The LORD struck Benjamin down before Israel. Twenty-five thousand one hundred Benjamite swordsmen died that day — the LORD's doing, not Israel's numbers."
    },
    "36": {
      "L": "So the children of Benjamin saw that they were smitten; for the men of Israel gave place to the Benjamites, because they trusted unto the liers in wait which they had set beside Gibeah.",
      "M": "The Benjamites saw that they were beaten, for the men of Israel had given ground before them — relying on the ambush they had set near Gibeah.",
      "T": "Only now did Benjamin see that the battle was lost. Israel's withdrawal on the first two days had been a feint; the real weapon was the ambush behind them."
    },
    "37": {
      "L": "And the liers in wait hasted, and rushed upon Gibeah; and the liers in wait drew themselves along, and smote all the city with the edge of the sword.",
      "M": "The ambushers rushed in to Gibeah, spread out through it, and put all the city to the sword.",
      "T": "The ambush stormed into Gibeah, fanned out through every street, and put everyone in the city to the sword."
    },
    "38": {
      "L": "Now there was an appointed sign between the men of Israel and the liers in wait, that they should make a great flame with smoke rise up out of the city.",
      "M": "The prearranged signal between the men of Israel and the ambush was that they should send up a great column of smoke from the city.",
      "T": "The agreed signal between the main army and the ambush: a great pillar of smoke rising from the burning city."
    },
    "39": {
      "L": "And when the men of Israel retired in the battle, Benjamin began to smite and kill of the men of Israel about thirty persons; for they said, Surely they are smitten down before us, as in the first battle.",
      "M": "When the men of Israel had withdrawn in the battle, Benjamin began killing about thirty of them and said, “They are surely falling before us, just as in the first battle.”",
      "T": "During Israel's deliberate retreat, Benjamin cut down about thirty men and thought: “We're winning again, just like before.”"
    },
    "40": {
      "L": "But when the flame began to arise up out of the city with a pillar of smoke, the Benjamites looked behind them, and behold, the flame of the city ascended up to heaven.",
      "M": "But when the pillar of smoke began to rise from the city, the Benjamites looked back — and the whole city was going up in flames to the sky.",
      "T": "Then the smoke rose — a great column from the city. Benjamin looked back. Gibeah was in flames, the fire reaching toward the sky."
    },
    "41": {
      "L": "And when the men of Israel turned again, the men of Benjamin were amazed; for they saw that evil was come upon them.",
      "M": "The men of Israel turned around, and the Benjamites were terrified, for they saw that disaster had come upon them.",
      "T": "Israel wheeled around. Benjamin was seized with terror — they finally understood that destruction had come."
    },
    "42": {
      "L": "Therefore they turned their backs before the men of Israel unto the way of the wilderness; but the battle overtook them, and them also that came out of the cities they destroyed in the midst of them.",
      "M": "They fled before the men of Israel toward the wilderness, but the battle caught up with them, and those who came out of the cities were struck down in their midst.",
      "T": "They fled toward the desert, but the battle followed them. Those who poured out of the cities ran into the slaughter from the other side."
    },
    "43": {
      "L": "Thus they enclosed the Benjamites round about, and chased them, and trode them down with ease over against Gibeah toward the sunrising.",
      "M": "They surrounded the Benjamites, chased them, and trampled them down toward the east side of Gibeah.",
      "T": "Israel hemmed them in, chased them down, and drove them without mercy to the east of Gibeah."
    },
    "44": {
      "L": "And there fell of Benjamin eighteen thousand men; all these were men of valour.",
      "M": "Eighteen thousand Benjamites fell — all of them fighting men.",
      "T": "Eighteen thousand Benjamites fell — every one a warrior."
    },
    "45": {
      "L": "And they turned and fled toward the wilderness unto the rock of Rimmon; and they gleaned of them in the highways five thousand men; and pursued hard after them unto Gidom, and slew two thousand men of them.",
      "M": "The survivors turned and fled into the wilderness toward the rock of Rimmon. Israel cut down five thousand more along the roads and pursued relentlessly to Gidom, killing two thousand more there.",
      "T": "The survivors turned and fled toward the rock of Rimmon in the desert. Israel cut down five thousand more along the roads, then pressed on to Gidom and killed two thousand more."
    },
    "46": {
      "L": "So that all which fell that day of Benjamin were twenty and five thousand men that drew the sword; all these were men of valour.",
      "M": "So all who fell from Benjamin that day totaled twenty-five thousand swordsmen — all fighting men.",
      "T": "Total Benjamite dead that day: twenty-five thousand swords. A tribe nearly erased."
    },
    "47": {
      "L": "But six hundred men turned and fled to the wilderness unto the rock Rimmon, and abode in the rock Rimmon four months.",
      "M": "But six hundred men fled to the rock of Rimmon in the wilderness and stayed there for four months.",
      "T": "Six hundred men reached the rock of Rimmon in the desert and held out there for four months. These six hundred were all that remained of Benjamin."
    },
    "48": {
      "L": "And the men of Israel turned again upon the children of Benjamin, and smote them with the edge of the sword, as well the men of every city, as the beast, and all that came to hand; also they set on fire all the cities that they came to.",
      "M": "The men of Israel turned back against the Benjamites and put them to the sword — the men of every city, the animals, and everything they found. And they set fire to every city they entered.",
      "T": "Israel swept back through the territory of Benjamin, killing every person in every town — men, women, children, livestock — and burning every city to ash."
    }
  },
  "21": {
    "1": {
      "L": "Now the men of Israel had sworn in Mizpah, saying, There shall not any of us give his daughter unto Benjamin to wife.",
      "M": "Now the men of Israel had taken an oath at Mizpah: “None of us will give his daughter in marriage to a Benjamite.”",
      "T": "At Mizpah the men of Israel had sworn a binding oath: “Not one of us will give his daughter in marriage to Benjamin.” That oath now became the problem."
    },
    "2": {
      "L": "And the people came to the house of God, and abode there till even before God, and lifted up their voices and wept sore;",
      "M": "The people came to Bethel and sat before God until evening, lifting up their voices and weeping bitterly.",
      "T": "The people came to Bethel and sat before God until evening, weeping aloud with bitter grief."
    },
    "3": {
      "L": "And said, O LORD God of Israel, why is this come to pass in Israel, that there should be to day one tribe lacking in Israel?",
      "M": "They said, “O LORD, God of Israel, why has this happened — that today one tribe should be missing from Israel?”",
      "T": "“LORD God of Israel — why has it come to this? Why is one of our own tribes on the edge of extinction?”"
    },
    "4": {
      "L": "And it came to pass on the morrow, that the people rose early, and built there an altar, and offered burnt offerings and peace offerings.",
      "M": "The next morning the people rose early and built an altar there, offering burnt offerings and peace offerings.",
      "T": "The next morning they rose early, built an altar, and offered burnt offerings and fellowship offerings to the LORD."
    },
    "5": {
      "L": "And the children of Israel said, Who is there among all the tribes of Israel that came not up with the congregation unto the LORD? For they had made a great oath concerning him that came not up to the LORD to Mizpah, saying, He shall surely be put to death.",
      "M": "The people of Israel said, “Which of all the tribes of Israel did not come up to the assembly before the LORD?” For there had been a solemn oath that whoever did not come up to the LORD at Mizpah would certainly be put to death.",
      "T": "Then Israel asked: “Which tribe failed to come to the assembly before the LORD?” For there had been a binding oath: any tribe that did not come to Mizpah faced death."
    },
    "6": {
      "L": "And the children of Israel repented them for Benjamin their brother, and said, There is one tribe cut off from Israel this day.",
      "M": "And the people of Israel had compassion for their brother Benjamin and said, “One tribe is cut off from Israel today.”",
      "T": "But the Israelites relented toward their brother Benjamin: “One of our own twelve tribes has been cut off.”"
    },
    "7": {
      "L": "How shall we do for wives for them that remain, seeing we have sworn by the LORD that we will not give them of our daughters to wives?",
      "M": "How shall we provide wives for those who remain, since we have sworn by the LORD that we will not give them any of our daughters as wives?",
      "T": "“How can we find wives for the survivors? We have sworn by the LORD not to give them our daughters.” The oath that seemed righteous now produced its own catastrophe."
    },
    "8": {
      "L": "And they said, What one is there of the tribes of Israel that came not up to Mizpah to the LORD? And, behold, there came none of the inhabitants of Jabeshgilead to the assembly.",
      "M": "They said, “Which tribe of Israel did not come up to Mizpah before the LORD?” And it turned out that no one from Jabesh-gilead had come to the assembly.",
      "T": "They checked: which tribe had not come to Mizpah? The answer: not a single person from Jabesh-gilead had appeared."
    },
    "9": {
      "L": "For the people were numbered, and behold, there were none of the inhabitants of Jabeshgilead there.",
      "M": "For when the people were mustered, not one of the inhabitants of Jabesh-gilead was there.",
      "T": "The census confirmed it — Jabesh-gilead was entirely absent."
    },
    "10": {
      "L": "And the congregation sent thither twelve thousand men of the valiantest, and commanded them, saying, Go and smite the inhabitants of Jabeshgilead with the edge of the sword, with the women and the children.",
      "M": "So the congregation sent twelve thousand of their best warriors there with orders: “Go and put the inhabitants of Jabesh-gilead to the sword — men, women, and children.”",
      "T": "The assembly dispatched twelve thousand warriors to Jabesh-gilead with these orders: “Kill every person — men, women, and children.”"
    },
    "11": {
      "L": "And this is the thing that ye shall do, Ye shall utterly destroy every male, and every woman that hath lain by man.",
      "M": "And this is what you shall do: you shall devote to destruction every male and every woman who has had sexual relations with a man.",
      "T": "The command: devote to destruction every male and every woman who has been with a man. Spare only the virgins."
    },
    "12": {
      "L": "And they found among the inhabitants of Jabeshgilead four hundred young virgins, that had known no man by lying with any male; and they brought them unto the camp to Shiloh, which is in the land of Canaan.",
      "M": "They found among the inhabitants of Jabesh-gilead four hundred young virgins who had not known a man. They brought them to the camp at Shiloh in the land of Canaan.",
      "T": "They found four hundred young women in Jabesh-gilead who had not been with a man. They were brought to the camp at Shiloh in Canaan."
    },
    "13": {
      "L": "And the whole congregation sent some to speak to the children of Benjamin that were in the rock Rimmon, and to call peaceably unto them.",
      "M": "Then the whole congregation sent a message to the Benjamites at the rock of Rimmon, calling to them in peace.",
      "T": "The whole assembly sent messengers to the six hundred Benjamites sheltering at the rock of Rimmon, offering peace terms."
    },
    "14": {
      "L": "And Benjamin came again at that time; and they gave them wives which they had saved alive of the women of Jabeshgilead; and yet so they sufficed them not.",
      "M": "And Benjamin came back at that time. They were given the women they had spared from Jabesh-gilead as wives. But there were not enough for all of them.",
      "T": "Benjamin came back. The Jabesh-gilead women were given to them as wives — four hundred women for six hundred men. Still not enough."
    },
    "15": {
      "L": "And the people repented them for Benjamin, because that the LORD had made a breach in the tribes of Israel.",
      "M": "And the people had compassion for Benjamin, because the LORD had made a gap in the tribes of Israel.",
      "T": "The people grieved for Benjamin — because the LORD himself had torn a gap in Israel's twelve tribes."
    },
    "16": {
      "L": "Then the elders of the congregation said, How shall we do for wives for them that remain, seeing the women are destroyed out of Benjamin?",
      "M": "The elders of the congregation said, “What shall we do for wives for those who are left, since the women of Benjamin have been destroyed?”",
      "T": "The elders asked: “What do we do for the remaining two hundred? All the women of Benjamin are gone.”"
    },
    "17": {
      "L": "And they said, There must be an inheritance for them that be escaped of Benjamin, that a tribe be not destroyed out of Israel.",
      "M": "And they said, “There must be a surviving inheritance for the remnant of Benjamin, so that a tribe may not be wiped out from Israel.”",
      "T": "“The Benjamite survivors must have an inheritance. A tribe of Israel cannot be erased from the earth.”"
    },
    "18": {
      "L": "Howbeit we may not give them wives of our daughters; for the children of Israel have sworn, saying, Cursed be he that giveth a wife to Benjamin.",
      "M": "However, we cannot give them wives from our daughters, for the people of Israel have sworn, 'Cursed is anyone who gives a wife to Benjamin.'",
      "T": "But we can't give them our daughters — the oath stands: 'Cursed is anyone who gives a wife to Benjamin.' The oath had seemed righteous; now it was a trap."
    },
    "19": {
      "L": "Then they said, Behold, there is a feast of the LORD in Shiloh yearly, in a place which is on the north side of Bethel, on the east side of the highway that goeth up from Bethel to Shechem, and on the south of Lebonah.",
      "M": "Then they said, “There is a yearly festival of the LORD at Shiloh, which is north of Bethel, east of the road going up from Bethel to Shechem, and south of Lebonah.”",
      "T": "“There is a yearly festival of the LORD at Shiloh — north of Bethel, east of the Bethel-to-Shechem road, south of Lebonah.”"
    },
    "20": {
      "L": "Therefore they commanded the children of Benjamin, saying, Go and lie in wait in the vineyards;",
      "M": "So they instructed the Benjamites: “Go and hide yourselves in the vineyards,",
      "T": "They told the Benjamite men: “Go and hide in the vineyards.”"
    },
    "21": {
      "L": "And see, and, behold, if the daughters of Shiloh come out to dance in dances, then come ye out of the vineyards, and catch you every man his wife of the daughters of Shiloh, and go to the land of Benjamin.",
      "M": "and watch. When the daughters of Shiloh come out to dance in the dances, come out of the vineyards and each man seize a wife for himself from the daughters of Shiloh, and go back to the land of Benjamin.“",
      "T": "Watch for the daughters of Shiloh when they come out to dance at the festival. Then come out — each man seize a woman from the dancers — and take her back to the land of Benjamin.“"
    },
    "22": {
      "L": "And it shall be, when their fathers or their brethren come unto us to complain, that we will say unto them, Be favourable unto them for our sakes: because we reserved not to each man his wife in the war; for ye did not give unto them at this time, that ye should be guilty.",
      "M": "When their fathers or brothers come to us to complain, we will say to them, 'Be gracious to them for our sake, because we could not provide enough wives from the war. And since you did not give your daughters — they were taken — you are not guilty of violating the oath.'",
      "T": "When their fathers and brothers come to protest, we will tell them: 'Show them grace for our sake — we simply did not have enough women from the war. And since you didn't give your daughters to them but they were seized, technically the oath is unbroken.' It was a legal fiction, and everyone knew it."
    },
    "23": {
      "L": "And the children of Benjamin did so, and took them wives, according to their number, of them that danced, whom they caught; and they went and returned unto their inheritance, and repaired the cities, and dwelt in them.",
      "M": "The Benjamites did so. They took wives for each of them from the dancers they seized. They went back to their territory, rebuilt their cities, and settled in them.",
      "T": "Benjamin did as instructed. Each man seized a wife from the dancing women at Shiloh. They returned to their territory, rebuilt their shattered towns, and settled in."
    },
    "24": {
      "L": "And the children of Israel departed thence at that time, every man to his tribe and to his family, and they went out from thence every man to his inheritance.",
      "M": "At that time the people of Israel also departed from there, each man to his tribe and his family, each going out to his inheritance.",
      "T": "Then all Israel dispersed — each man back to his tribe and his family, each one returning to his inheritance."
    },
    "25": {
      "L": "In those days there was no king in Israel; every man did that which was right in his own eyes.",
      "M": "In those days there was no king in Israel. Everyone did what was right in his own eyes.",
      "T": "In those days Israel had no king — and every person lived by the law of their own heart. This is what that law produces."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'judges')
        merge_tier(existing, JUDGES, tier_key)
        save(tier_dir, 'judges', existing)
    print('Judges 19–21 written.')

if __name__ == '__main__':
    main()
