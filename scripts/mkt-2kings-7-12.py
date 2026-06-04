"""
MKT 2 Kings chapters 7–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2kings-7-12.py

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L/M throughout; "the LORD" in T.
  Consistent with mkt-1kings-19-21.py and all prior OT scripts.
- H430 (אֱלֹהִים): "God" in all tiers. Used as title here, not the divine name.
- H5315 (נֶפֶשׁ): "life" throughout this range for bodily survival contexts (e.g., 9:26
  "blood of Naboth"); not rendered "soul" (Greek immaterial sense). Embodies the whole
  living person, not a separable inner part.
- H1285 (בְּרִית): "covenant" in all tiers (11:17 — Jehoiada's triple covenant renewal:
  LORD/king/people). This is the central constitutional act of Joash's accession; T notes
  its echoes of 2 Sam 7 and Josh 24.
- H2183 (זְנוּת): "whoredoms" in L; "harlotries" in M; T renders as "the systematic
  spiritual adultery of Jezebel" — Jehu's charge against Joram in 9:22 frames the whole
  purge as covenant-infidelity judgment.
- H3785 (כֶּשֶׁף): "witchcrafts" in L/M; "sorceries" in T (9:22). The pairing of
  zenunim/witchcraft frames Jezebel as embodying the comprehensive apostasy of the north.
- H7965 (שָׁלוֹם): "peace" in L/M; T differentiates: ironically in 9:17-19 (the messenger's
  "Is it peace?" as the hollow ritual question of a doomed regime), and theologically in
  9:22 (no peace possible where covenant has been violated).
- H1697 (דָּבָר): "word" in L; "word" in M; T surfaces the force of prophetic word as
  historical causation in 9:26 ("according to the word of the LORD"), 10:10, 10:17.
- H5971 (עַם): "people" throughout. In 11:14,17-20 it occurs 7× in rapid succession —
  the "people of the land" (H5971 H776) are the covenant constituency enacting judgment;
  T notes this.
- H4397 (מַלְאָךְ): "messenger" throughout chapters 7-10 (human context); no divine
  angel appearances in this range.
- H5429 (סְאָה): seah — standard dry measure (~7.3L), roughly 1/3 bushel. L preserves
  "seah/measure"; M uses "seah"; T explains in 7:1 that these are crisis grain prices —
  Elisha announces the end of famine-level scarcity.
- H2617 (חֶסֶד): not prominent in this range. No "hesed" uses in chs 7-12.
- H7307 (רוּחַ): not present in this range's key verses.
- H4397/H8111 geographical note: "Samaria" = capital of northern kingdom; "Jezreel" =
  royal winter residence and site of Naboth's vineyard (1 Kgs 21). Multiple scenes of
  judgment converge on Jezreel — Joram's death, Jezebel's death (9:24-37). T notes
  Jezreel becomes the locus of retributive justice.
- H3772 (כָּרַת בְּרִית) lit. "cut covenant" — the idiom of covenant-making involves
  cutting (of sacrificial animals, echoing Gen 15). L: "made a covenant"; M/T: same but
  T notes the legal-constitutional weight in 11:17.
- Aspect decisions:
  - Wayyiqtol (waw-consec. imperfects) = narrative past throughout — rendered in
    simple English past.
  - Qatal perfects in divine speech (9:7-10; 10:30) = past completed acts or
    pronouncements with present binding force.
  - 10:30: God's promise uses qatal ("your sons... shall sit") — divine commitment
    framed as already accomplished; T surfaces the certainty.
- OT echoes:
  - 7:1: Elisha's grain-price prophecy echoes the covenant curse/blessing structure of
    Deut 28 — the famine was covenant curse; the deliverance is covenant rescue.
  - 9:7: "avenge the blood of my servants the prophets" echoes Elijah's lament (1 Kgs
    19:10,14) and God's promise in 1 Kgs 21:19-24. Jehu is the instrument of that oracle.
  - 9:26: "the blood of Naboth and the blood of his sons" — fulfillment of Elijah's
    precise oracle (1 Kgs 21:19). The Deuteronomistic theodicy of exact retribution.
  - 9:36-37: fulfillment of Elijah's prophecy (1 Kgs 21:23). T notes the precision.
  - 10:10: "nothing of the word of the LORD shall fall to the earth" — this is a
    theological statement about prophetic reliability, not just one oracle. The phrase
    "fall to the earth" for a word not being fulfilled is a Hebrew idiom for failure.
    T surfaces this as the narrator's commentary on the whole purge narrative.
  - 10:17: second explicit fulfillment notice — "according to the word that the LORD
    had spoken to Elijah." T notes the doubled fulfillment notices bracket Jehu's purge.
  - 11:1-3: Athaliah's murder of the royal seed threatens the Davidic covenant of
    2 Sam 7:12-16. God's preservation of Joash is the hidden protection of that promise.
    T notes this explicitly — the lamp (8:19) is almost extinguished.
  - 11:17: triple covenant (LORD/king/people) echoes 2 Sam 5:3 (David's anointing),
    Josh 24:25, and Deut 17:18-20 (the king's covenant duty). T surfaces all three.
  - 12:3: "high places not taken away" is the standard Deuteronomistic critique formula
    for kings who were partially faithful. T notes that Joash's faithfulness is
    conditioned by Jehoiada's living tutelage — contrast with 2 Chron 24:17-22 (implied).
- Jezebel note (9:30-37): her painting of eyes and adorning of hair is not seduction —
  it is the act of a queen going to her death in full royal dignity. T surfaces this
  ambiguity: was she facing death with the pride of a reigning queen, or attempting one
  last act of influence? The text refuses to collapse the dignity. Jehu's command to
  "see to this cursed woman and bury her" (9:34) shows his recognition of her royal status
  even in death. The dogs' consumption is the final prophetic irony.
- Hazael's weeping scene (8:11): "he settled his face in a fixed stare" — unusual Hebrew
  (hiph. of H5975 + H6440 "face"). The man of God cannot look away; the horror of the
  vision forces a prolonged, fixed gaze. T surfaces the moral weight: Elisha sees the
  future atrocities and weeps — this is prophetic grief, not strategic sorrow.
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


KINGS2 = {
  "7": {
    "1": {
      "L": "And Elisha said, Hear the word of the LORD. Thus says the LORD: Tomorrow about this time a seah of fine flour shall be sold for a shekel, and two seahs of barley for a shekel, at the gate of Samaria.",
      "M": "Elisha said, \"Hear the word of the LORD. This is what the LORD says: Tomorrow about this time a seah of fine flour will sell for one shekel and two seahs of barley for one shekel, at the gate of Samaria.\"",
      "T": "Elisha declared: \"Hear the word of the LORD. This is what the LORD says: Tomorrow at this very hour, the grain market at Samaria's gate will turn — a seah of fine flour for one shekel, two seahs of barley for one shekel.\" The famine-curse of the siege was about to break."
    },
    "2": {
      "L": "And the lord on whose hand the king leaned answered the man of God and said, Behold, if the LORD were to make windows in heaven, could this thing be? And he said, Behold, you shall see it with your eyes, but you shall not eat of it.",
      "M": "The officer on whose hand the king was leaning answered the man of God and said, \"Even if the LORD were to make windows in heaven, could this thing happen?\" And Elisha said, \"You will see it with your own eyes, but you will not eat any of it.\"",
      "T": "The royal officer who was the king's support — leaning on his arm — challenged the prophet: \"Even if the LORD opened floodgates in the sky, could prices drop like that?\" Elisha answered without hesitation: \"Your eyes will see it. But you will not taste it.\" Unbelief in the word of God always costs more than it imagines."
    },
    "3": {
      "L": "And there were four leprous men at the entrance of the gate. And they said one to another, Why do we sit here until we die?",
      "M": "Now there were four men with skin disease at the entrance of the city gate. They said to one another, \"Why are we sitting here until we die?\"",
      "T": "Four outcasts — men with a skin disease, barred from the city — were sitting at the gate. They said to one another, \"Why are we just sitting here waiting to die?\""
    },
    "4": {
      "L": "If we say, We will enter the city — and the famine is in the city and we shall die there. And if we sit here, we also die. Now therefore come, let us fall to the camp of the Syrians. If they spare us alive, we shall live; and if they kill us, we shall only die.",
      "M": "\"If we say, 'Let us enter the city,' there is famine in the city and we will die there. And if we stay here, we will die here too. So now, come, let us go over to the Syrian camp. If they spare our lives, we live; if they kill us, we only die.\"",
      "T": "\"Inside the city means starvation — we die either way here or there. But if we surrender to the Syrian camp, the worst that happens is what is already happening. If they let us live, we gain; if they kill us, we simply die sooner than we would have anyway. So let us take the chance.\""
    },
    "5": {
      "L": "So they rose up at twilight to go to the camp of the Syrians. And they came to the outskirts of the Syrian camp, and behold, there was no man there.",
      "M": "So at twilight they set out for the Syrian camp. But when they came to the edge of the Syrian camp, there was no one there.",
      "T": "At dusk the four lepers made their way to the Syrian lines — and found the camp completely deserted."
    },
    "6": {
      "L": "For the Lord had caused the camp of the Syrians to hear the sound of chariots and the sound of horses, the sound of a great army, so that they said to one another, Behold, the king of Israel has hired against us the kings of the Hittites and the kings of the Egyptians to come upon us.",
      "M": "For the Lord had made the Syrian camp hear the sound of chariots, the sound of horses, and the sound of a great army. So they said to one another, \"Look, the king of Israel has hired against us the kings of the Hittites and the kings of Egypt to attack us.\"",
      "T": "The LORD himself had caused the Syrian army to hear a phantom army — the thundering of chariot wheels, the hoofbeat of cavalry, the din of a vast host advancing. They had said to each other, \"The king of Israel has hired the Hittites and the Egyptians to come against us!\" God had done with sound what Israel could not do with soldiers."
    },
    "7": {
      "L": "And they arose and fled in the twilight, and left their tents and their horses and their donkeys, even the camp as it was, and fled for their lives.",
      "M": "So they rose up and fled at twilight. They left behind their tents, their horses, and their donkeys — the camp just as it stood — and fled for their lives.",
      "T": "They had bolted in the dusk, abandoning everything — tents pitched, horses tethered, donkeys tied — the whole camp left exactly as it stood. They ran for their lives."
    },
    "8": {
      "L": "And when these lepers came to the outskirts of the camp, they went into one tent and ate and drank, and carried from it silver and gold and garments, and went and hid them. And they came back and entered another tent and carried from it also and went and hid them.",
      "M": "When the lepers reached the edge of the camp, they went into one tent and ate and drank, and carried off silver, gold, and clothing. They went and hid these things. Then they came back and entered another tent and carried off more from it, and hid those things too.",
      "T": "The four outcasts stumbled into abundance: food, wine, silver, gold, clothing. They ate and drank, then began carrying off valuables and hiding them — tent after tent, hoard after hoard. For a moment, the desperate lived like kings."
    },
    "9": {
      "L": "Then they said one to another, We are not doing right. This day is a day of good news, and we hold our peace. If we wait until the morning light, punishment will come upon us. Now therefore come, let us go and tell the king's household.",
      "M": "Then they said to one another, \"We are not doing right. This day is a day of good news, and we are keeping silent. If we wait until morning light, punishment will overtake us. Come, let us go and report to the king's household.\"",
      "T": "Conscience spoke: \"This isn't right. We're sitting on news that could save a city, and we're saying nothing. If we keep quiet till morning, we will be held to account. Come — let us go and tell the palace.\" Even the excluded knew that good news must be shared."
    },
    "10": {
      "L": "So they came and called out to the gatekeepers of the city and told them, We came to the Syrian camp, and behold, there was no man there and no human sound — only horses tied and donkeys tied, and the tents as they were.",
      "M": "So they went and called to the city gatekeepers and said, \"We went to the Syrian camp, and there was no one there, not a sound — only horses and donkeys tied up and the tents left standing as they were.\"",
      "T": "They ran back and called out to the city gatekeepers: \"We went to the Syrian camp — it is empty. Not a person, not a sound. Just the horses and donkeys still tethered, the tents still standing. They are gone.\""
    },
    "11": {
      "L": "And the gatekeepers called out and they told it to the king's household within.",
      "M": "The gatekeepers called out, and it was reported to the king's palace inside.",
      "T": "The gatekeepers relayed the news inward, and it reached the palace."
    },
    "12": {
      "L": "And the king arose in the night and said to his servants, I will tell you now what the Syrians have done to us. They know that we are hungry. So they have gone out of the camp to hide themselves in the field, thinking, When they come out of the city, we shall catch them alive and get into the city.",
      "M": "The king got up in the night and said to his servants, \"I will tell you what the Syrians have done. They know we are starving, so they have left the camp to hide themselves in the open field, thinking that when we come out of the city they will capture us alive and then enter the city.\"",
      "T": "The king's first instinct was suspicion: he woke his servants in the night and said, \"I know what this is — it is a trap. The Syrians know we are desperate with hunger. They have abandoned the camp to lure us out into the open field, where they will take us alive and walk into the city behind us.\""
    },
    "13": {
      "L": "And one of his servants answered and said, Let some men take five of the horses that remain, which are left in the city — behold, they are like all the multitude of Israel that are left in it; indeed they are like all the multitude of Israel who are already consumed — and let us send and see.",
      "M": "One of his servants replied, \"Let some men take five of the remaining horses that are still in the city — they are no worse off than the rest of Israel who are left here; they are like all who are already perishing — and let us send and see.\"",
      "T": "One of his officials spoke up: \"Let us send a reconnaissance party with five horses — the ones that are still alive here. If they perish, what is lost? They are no worse off than the rest of the city's people, all of whom are dying anyway. At least we will know the truth.\""
    },
    "14": {
      "L": "So they took two chariot horses, and the king sent them after the Syrian army, saying, Go and see.",
      "M": "So they took two chariot horses, and the king sent them out after the Syrian army, saying, \"Go and find out.\"",
      "T": "They prepared two chariot horses and the king sent them out with a simple order: \"Go — and tell us what you find.\""
    },
    "15": {
      "L": "And they followed them as far as the Jordan, and behold, the whole way was full of garments and equipment that the Syrians had thrown away in their haste. And the messengers returned and told the king.",
      "M": "They followed them as far as the Jordan, and behold, the whole road was strewn with garments and weapons that the Syrians had thrown away in their panic. The messengers returned and told the king.",
      "T": "They rode to the Jordan and the whole road was a trail of discarded equipment — cloaks, weapons, everything the Syrians had shed as they ran in blind panic. The riders turned back and brought the king their report."
    },
    "16": {
      "L": "So the people went out and plundered the camp of the Syrians. And a seah of fine flour was sold for a shekel and two seahs of barley for a shekel, according to the word of the LORD.",
      "M": "Then the people went out and plundered the Syrian camp. And a seah of fine flour sold for a shekel and two seahs of barley for a shekel, in accordance with the word of the LORD.",
      "T": "The city poured out and ransacked the abandoned camp. By that same afternoon, exactly as Elisha had said, grain was selling at the gate for the price he named. The word of the LORD had not missed by a single coin."
    },
    "17": {
      "L": "Now the king had appointed the lord on whose hand he leaned to have charge of the gate. And the people trampled him in the gate, and he died, as the man of God had said when the king came down to him.",
      "M": "Now the king had placed the officer on whose hand he had leaned in charge of the gate. The people trampled him in the gateway and he died — just as the man of God had said when the king came down to him.",
      "T": "The king had given the doubting officer charge of the gate — perhaps a position of honor, perhaps simply administration. But the surging crowd trampled him to death in the rush. He saw the abundance he had called impossible. He died in the midst of it, as the prophet had said."
    },
    "18": {
      "L": "For it was as the man of God had spoken to the king, saying, Two seahs of barley for a shekel and a seah of fine flour for a shekel shall be sold tomorrow about this time at the gate of Samaria.",
      "M": "For it happened exactly as the man of God had told the king: \"Two seahs of barley will sell for a shekel and a seah of fine flour for a shekel about this time tomorrow at the gate of Samaria.\"",
      "T": "The narrator repeats the prophecy verbatim for emphasis — the fulfillment matched the word precisely, grain price and timing and location."
    },
    "19": {
      "L": "And that lord had answered the man of God and said, Behold, if the LORD were to make windows in heaven, could such a thing be? And he had said, Behold, you shall see it with your eyes, but you shall not eat of it.",
      "M": "And that officer had answered the man of God, \"Even if the LORD were to make windows in heaven, could that happen?\" And Elisha had answered, \"You will see it with your own eyes, but you will not eat any of it.\"",
      "T": "The narrator also repeats the officer's dismissal word for word — the scoff that sealed his fate. He had mocked the prophet's word. He saw every syllable of it come true. But the second half of the prophecy was also exact: the bread and barley that flooded the market never reached his mouth."
    },
    "20": {
      "L": "And so it fell out to him, for the people trampled him in the gate and he died.",
      "M": "And that is exactly what happened to him — the people trampled him in the gateway and he died.",
      "T": "So it ended. One verse, no elaboration. The word of God stood; the man who doubted it did not."
    }
  },
  "8": {
    "1": {
      "L": "Now Elisha had spoken to the woman whose son he had restored to life, saying, Arise and go, you and your household, and sojourn wherever you can sojourn, for the LORD has called for a famine, and it will come upon the land for seven years.",
      "M": "Now Elisha had said to the woman whose son he had restored to life, \"Get up and go, you and your household, and live wherever you can, for the LORD has decreed a famine that will come upon the land for seven years.\"",
      "T": "The Shunamite woman — whose son Elisha had raised from death (2 Kgs 4) — had been warned beforehand. Elisha had told her: \"Leave. The LORD is bringing a seven-year famine on the land. Take your household and settle wherever you find refuge.\" Providence prepares even before the storm breaks."
    },
    "2": {
      "L": "So the woman arose and did according to the word of the man of God. She went with her household and sojourned in the land of the Philistines for seven years.",
      "M": "So the woman obeyed the word of the man of God. She set out with her household and lived in the land of the Philistines for seven years.",
      "T": "She obeyed — no questions asked, no hesitation recorded. For seven years she lived among the Philistines, far from her ancestral land, trusting the prophet's word."
    },
    "3": {
      "L": "And at the end of the seven years, the woman returned from the land of the Philistines. And she went to the king to appeal for her house and for her land.",
      "M": "At the end of the seven years, the woman returned from the land of the Philistines. She went to the king to appeal for her house and her land.",
      "T": "When the seven years were up, she came home to find her property occupied. She went straight to the king to petition for her house and her land — the inheritance that had been left behind when she obeyed God's word."
    },
    "4": {
      "L": "Now the king was talking with Gehazi the servant of the man of God, saying, Tell me all the great things that Elisha has done.",
      "M": "Now the king had been talking with Gehazi the servant of the man of God, saying, \"Tell me all the great things that Elisha has done.\"",
      "T": "At that very moment the king was in conversation with Gehazi, Elisha's former servant, asking him to recount all the prophet's remarkable deeds. The timing was not coincidence — God was arranging the moment."
    },
    "5": {
      "L": "And while he was telling the king how Elisha had restored the dead to life, behold, the woman whose son he had restored to life was appealing to the king for her house and her land. And Gehazi said, My lord, O king, this is the woman, and this is her son whom Elisha restored to life.",
      "M": "While Gehazi was telling the king how Elisha had brought a dead person back to life, the very woman whose son he had restored walked in to appeal to the king for her house and land. Gehazi said, \"My lord the king, this is the woman herself, and this is her son whom Elisha brought back to life!\"",
      "T": "Just as Gehazi was telling the story of the resurrected child, the woman herself walked through the door, petitioning for her property. Gehazi pointed: \"My lord — this is the woman! And this is her son, the very boy Elisha raised!\" Providence had timed the moment to the minute."
    },
    "6": {
      "L": "When the king asked the woman, she told him. And the king appointed for her a certain officer, saying, Restore all that was hers, together with all the fruit of the field from the day that she left the land until now.",
      "M": "When the king asked the woman, she told him her story. So the king appointed an officer for her, saying, \"Restore all that belongs to her, and all the income from her field from the day she left the country until now.\"",
      "T": "The king heard her out and gave immediate orders: full restoration — the house, the land, and all the harvest income from the seven years she had been gone. Obedience to the prophet's word cost her seven years; obedience to God returned it all plus interest."
    },
    "7": {
      "L": "Now Elisha came to Damascus. And Ben-hadad king of Syria was sick. And when it was told him, The man of God has come here,",
      "M": "Elisha came to Damascus. Ben-hadad king of Syria was ill at the time. When he was told, \"The man of God has come here,\"",
      "T": "The scene shifts: Elisha is in Damascus, deep in enemy territory. The Syrian king Ben-hadad lay sick. Word reached him that the prophet of Israel was in the city."
    },
    "8": {
      "L": "the king said to Hazael, Take a present in your hand and go to meet the man of God, and inquire of the LORD through him, saying, Shall I recover from this sickness?",
      "M": "the king said to Hazael, \"Take a gift and go to meet the man of God. Ask him to inquire of the LORD whether I will recover from this illness.\"",
      "T": "Ben-hadad sent his officer Hazael with a gift and a question: \"Go to the Israelite prophet. Ask him — will I live?\" Even a pagan king knew where true prophetic authority resided."
    },
    "9": {
      "L": "So Hazael went to meet him and took a present with him, even every good thing of Damascus, forty camel loads. He came and stood before him and said, Your son Ben-hadad king of Syria has sent me to you, asking, Shall I recover from this sickness?",
      "M": "So Hazael went to meet Elisha and brought a gift — forty camel loads of every good thing from Damascus. He came and stood before the prophet and said, \"Your son Ben-hadad king of Syria has sent me to ask: Will I recover from this illness?\"",
      "T": "Hazael came with magnificent gifts — forty camels loaded with Damascus's finest. He stood before Elisha with the diplomatic formula: \"Your son Ben-hadad asks...\" — the courtly fiction of equals calling each other son. The real question was: will the king live or die?"
    },
    "10": {
      "L": "Elisha said to him, Go, say to him, You shall certainly recover. However, the LORD has shown me that he shall certainly die.",
      "M": "Elisha answered him, \"Go and tell him, 'You will certainly recover.' But the LORD has shown me that he will in fact die.\"",
      "T": "Elisha's answer was a theological riddle: \"Tell him: you will certainly recover. But the LORD has shown me that he will certainly die.\" The sickness would not kill him — but Hazael would. The answer contained both the truth and the terrible disclosure the prophet was about to make."
    },
    "11": {
      "L": "And he settled his face in a fixed stare until Hazael was ashamed. And the man of God wept.",
      "M": "Elisha fixed his gaze on Hazael and stared at him without flinching, until Hazael was uncomfortable. Then the man of God wept.",
      "T": "Elisha stared at Hazael — not a passing glance but a prolonged, unblinking gaze — until Hazael himself could not hold the prophet's eyes and looked away in shame. Then Elisha wept. He could see what Hazael was, and what he would do. The vision of coming atrocity broke the prophet's heart."
    },
    "12": {
      "L": "And Hazael said, Why does my lord weep? He answered, Because I know the evil that you will do to the people of Israel. Their fortresses you will set on fire, and their young men you will kill with the sword, and you will dash their children to pieces, and rip open their pregnant women.",
      "M": "Hazael asked, \"Why does my lord weep?\" He answered, \"Because I know the evil you will inflict on the people of Israel. You will set their strongholds on fire, kill their young men with the sword, dash their infants to pieces, and rip open their pregnant women.\"",
      "T": "\"Why are you weeping, my lord?\" Hazael asked. Elisha answered with a list of horrors — the atrocities that Hazael would commit against Israel: fortresses burned, young men slaughtered, infants dashed against stones, pregnant women ripped open. These were the standard brutalities of ancient conquest. Elisha named them one by one because he had seen them all."
    },
    "13": {
      "L": "And Hazael said, But what is your servant, who is only a dog, that he should do this great thing? And Elisha answered, The LORD has shown me that you shall be king over Syria.",
      "M": "Hazael said, \"How could your servant, a mere dog, do such a great thing?\" Elisha answered, \"The LORD has shown me that you will be king over Syria.\"",
      "T": "Hazael's protest — \"But what is your servant? Only a dog!\" — was the standard self-deprecating formula of court rhetoric. He was not genuinely horrified at the prospect of power; he was already considering it. Elisha answered the real question beneath the polite denial: \"The LORD has shown me you will be king over Syria.\""
    },
    "14": {
      "L": "Then he departed from Elisha and came to his master, who said to him, What did Elisha say to you? And he answered, He told me that you would certainly recover.",
      "M": "Then Hazael left Elisha and returned to his master, who asked him, \"What did Elisha say to you?\" And Hazael replied, \"He told me that you would certainly recover.\"",
      "T": "Hazael left the prophet and went back to Ben-hadad. The king asked, \"What did the prophet say?\" Hazael told him the first half of Elisha's answer — \"You will certainly recover\" — and withheld the rest. His lie by omission was already the beginning of treachery."
    },
    "15": {
      "L": "But on the next day, he took a thick cloth and dipped it in water and spread it over his face, until he died. And Hazael became king in his place.",
      "M": "But the next day, Hazael took a thick cloth, soaked it in water, and spread it over the king's face until he died. And Hazael became king in his place.",
      "T": "The next morning, Hazael murdered his master — not with a sword but with a wet cloth pressed over the sick man's face until he suffocated. He then seized the throne. The prophet's words were enacted within a day."
    },
    "16": {
      "L": "In the fifth year of Joram son of Ahab king of Israel, when Jehoshaphat was king of Judah, Jehoram son of Jehoshaphat king of Judah began to reign.",
      "M": "In the fifth year of Joram son of Ahab king of Israel, while Jehoshaphat was still king of Judah, Jehoram son of Jehoshaphat began to reign as king of Judah.",
      "T": "The Deuteronomistic historian pivots to Judah: in the fifth year of Ahab's son Joram on Israel's throne, Jehoshaphat's son Jehoram succeeded his father in Jerusalem. The two kingdoms' stories run in parallel, both in decline."
    },
    "17": {
      "L": "He was thirty-two years old when he became king, and he reigned eight years in Jerusalem.",
      "M": "Jehoram was thirty-two years old when he became king, and he reigned eight years in Jerusalem.",
      "T": "Thirty-two years old, eight-year reign — the historian records it with characteristic brevity for a reign without distinction."
    },
    "18": {
      "L": "And he walked in the way of the kings of Israel, as the house of Ahab had done, for the daughter of Ahab was his wife. And he did what was evil in the sight of the LORD.",
      "M": "He walked in the ways of the kings of Israel, as the house of Ahab had done, because the daughter of Ahab was his wife. He did what was evil in the sight of the LORD.",
      "T": "The verdict is stark: he followed the Ahab pattern. His marriage to Ahab's daughter was both a political alliance and a theological infection. The house of Ahab had thoroughly contaminated Judah's royal house."
    },
    "19": {
      "L": "Yet the LORD was not willing to destroy Judah, for the sake of David his servant, since he had promised to give a lamp to him and to his children always.",
      "M": "Yet the LORD was not willing to destroy Judah, for the sake of his servant David, since he had promised to give a lamp to him and to his descendants forever.",
      "T": "Yet Judah survived — not through Jehoram's merit, but through God's own commitment to the covenant with David (2 Sam 7). The image of the lamp is exact: even in deepest apostasy, God preserved a line of light. The dynasty wobbled dangerously, but the promise held it upright."
    },
    "20": {
      "L": "In his days Edom revolted from under the hand of Judah and set up a king over themselves.",
      "M": "In his days Edom revolted from under Judah's rule and installed their own king.",
      "T": "The first symptom of imperial unraveling: Edom — long under Judah's control — threw off the yoke and crowned its own king. The dominion that David had built (2 Sam 8:14) was beginning to erode."
    },
    "21": {
      "L": "And Joram went over to Zair with all his chariots. He arose by night and struck the Edomites who had surrounded him and the commanders of the chariots. But the army fled to their tents.",
      "M": "So Joram marched to Zair with all his chariots. He rose up by night and struck the Edomites who had surrounded him and his chariot commanders, but his army fled to their tents.",
      "T": "Joram led a night assault against the encircling Edomites — broke through, perhaps regrouped — but the army disintegrated and fled. The campaign ended in a draw at best: Joram survived, but Edom was not subdued."
    },
    "22": {
      "L": "So Edom revolted from under the hand of Judah to this day. At the same time Libnah also revolted.",
      "M": "So Edom has been in revolt against Judah to this day. Libnah also revolted at the same time.",
      "T": "Edom's independence was permanent. And even Libnah — a priestly city in the Shephelah, within Judah's own heartland — broke away. The kingdom was fragmenting from within and without."
    },
    "23": {
      "L": "Now the rest of the acts of Joram, and all that he did, are they not written in the Book of the Chronicles of the Kings of Judah?",
      "M": "As for the rest of the acts of Joram and everything he did, are they not recorded in the Book of the Chronicles of the Kings of Judah?",
      "T": "The standard dismissal formula — the historian points to another record for those interested in more. Joram's reign merited no detailed treatment; the damage he inflicted was its own monument."
    },
    "24": {
      "L": "So Joram slept with his fathers and was buried with his fathers in the city of David. And Ahaziah his son reigned in his place.",
      "M": "Joram rested with his ancestors and was buried with them in the city of David. And his son Ahaziah became king in his place.",
      "T": "Joram died and was buried in the city of David — the ancestral honor preserved even for an apostate king, because the dynasty survived through God's faithfulness, not through royal merit. Ahaziah his son took the throne."
    },
    "25": {
      "L": "In the twelfth year of Joram son of Ahab king of Israel, Ahaziah son of Jehoram king of Judah began to reign.",
      "M": "In the twelfth year of Joram son of Ahab king of Israel, Ahaziah son of Jehoram king of Judah began his reign.",
      "T": "A synchronism: Ahaziah of Judah accedes in the twelfth year of Joram of Israel — both Ahab's dynasty and its Judahite tributary were about to end simultaneously."
    },
    "26": {
      "L": "Ahaziah was twenty-two years old when he became king, and he reigned one year in Jerusalem. His mother's name was Athaliah, the granddaughter of Omri king of Israel.",
      "M": "Ahaziah was twenty-two years old when he began to reign, and he reigned one year in Jerusalem. His mother's name was Athaliah, a granddaughter of Omri king of Israel.",
      "T": "One year. Twenty-two years old. His mother was Athaliah — Omri's blood, Ahab's line. The brief notice says everything about why his reign would end so quickly and so violently."
    },
    "27": {
      "L": "He walked in the way of the house of Ahab and did what was evil in the sight of the LORD, as the house of Ahab had done, for he was the son-in-law of the house of Ahab.",
      "M": "He walked in the way of the house of Ahab and did what was evil in the sight of the LORD, as the house of Ahab had done, because he was a son-in-law of the house of Ahab.",
      "T": "The theological verdict matches his grandfather Joram's: he walked in Ahab's pattern. The family connection goes in every direction — his mother was Ahab's daughter, he was married into Ahab's network. The house of Ahab had captured Judah's throne."
    },
    "28": {
      "L": "He went with Joram son of Ahab to war against Hazael king of Syria at Ramoth-gilead. And the Syrians wounded Joram.",
      "M": "He went with Joram son of Ahab to fight against Hazael king of Syria at Ramoth-gilead. And the Syrians wounded Joram.",
      "T": "Ahaziah joined his uncle Joram in a military campaign against Hazael at Ramoth-gilead — the same contested border town that had cost Ahab his life (1 Kgs 22). Hazael's forces wounded Joram. The campaign set in motion the events that would end both dynasties."
    },
    "29": {
      "L": "King Joram returned to Jezreel to be healed of the wounds that the Syrians had given him at Ramah when he fought against Hazael king of Syria. And Ahaziah son of Jehoram king of Judah went down to see Joram son of Ahab in Jezreel, because he was sick.",
      "M": "King Joram returned to Jezreel to recover from the wounds the Syrians had inflicted on him at Ramah when he fought Hazael king of Syria. Ahaziah son of Jehoram king of Judah went down to Jezreel to visit Joram son of Ahab, who was ill.",
      "T": "Joram retreated to Jezreel to recover — the royal winter residence, the site of Naboth's murder, the place where judgment would arrive. Ahaziah came to visit his wounded uncle. Two kings, both of Ahab's line, both in Jezreel. Jehu was already riding."
    }
  },
  "9": {
    "1": {
      "L": "Then Elisha the prophet called one of the sons of the prophets and said to him, Gird up your loins and take this flask of oil in your hand and go to Ramoth-gilead.",
      "M": "Elisha the prophet summoned one of the sons of the prophets and said to him, \"Tuck up your robe and take this flask of oil in your hand and go to Ramoth-gilead.\"",
      "T": "Elisha dispatched a young prophet with a single mission: take a flask of oil to Ramoth-gilead. The urgency — \"tuck up your robe, go quickly\" — signals that this is a divine commission that must be executed without delay."
    },
    "2": {
      "L": "When you arrive there, look for Jehu son of Jehoshaphat son of Nimshi. Go in and make him rise from among his brothers and take him to an inner chamber.",
      "M": "\"When you get there, look for Jehu son of Jehoshaphat son of Nimshi. Go in, have him get up from among his companions, and take him to an inner room.\"",
      "T": "\"Find Jehu son of Jehoshaphat son of Nimshi among the military officers. Get him alone — pull him out from his brothers-in-arms and bring him into a private room. What you are about to do must not be witnessed.\""
    },
    "3": {
      "L": "Then take the flask of oil and pour it on his head and say, Thus says the LORD: I anoint you king over Israel. Then open the door and flee; do not wait.",
      "M": "\"Then take the flask, pour the oil on his head, and say: 'This is what the LORD says: I anoint you king over Israel.' Then open the door and flee without delay.\"",
      "T": "\"Pour the oil on his head and speak the LORD's word: 'I anoint you king over Israel.' Then run. Do not wait to see what happens next. Your work is done the moment the word is spoken.\""
    },
    "4": {
      "L": "So the young man, the young prophet, went to Ramoth-gilead.",
      "M": "So the young prophet went to Ramoth-gilead.",
      "T": "He went — simply, immediately, without recorded hesitation."
    },
    "5": {
      "L": "When he arrived, behold, the commanders of the army were sitting. And he said, I have a word for you, O commander. And Jehu said, For which of us all? And he said, For you, O commander.",
      "M": "When he arrived, the commanders of the army were sitting together. He said, \"I have a message for you, commander.\" Jehu asked, \"For which of us?\" He replied, \"For you, commander.\"",
      "T": "He walked into the officers' meeting. Everyone present outranked him. He announced himself with a prophet's brevity: \"I have a word for you, commander.\" Jehu looked around — \"Which of us?\" — and the young prophet pointed: \"You.\""
    },
    "6": {
      "L": "So he arose and went into the house. And the prophet poured the oil on his head and said to him, Thus says the LORD, the God of Israel: I anoint you king over the people of the LORD, over Israel.",
      "M": "So Jehu got up and went inside. The prophet poured the oil on his head and declared, \"This is what the LORD, the God of Israel, says: I anoint you king over the LORD's people, over Israel.\"",
      "T": "Inside the room, the young prophet poured the oil. The words were the same words Samuel had spoken over David: \"I anoint you king over the people of the LORD.\" This was not a coup — it was a divine appointment. Jehu was being consecrated to a task."
    },
    "7": {
      "L": "You shall strike down the house of Ahab your master, that I may avenge the blood of my servants the prophets and the blood of all the servants of the LORD at the hand of Jezebel.",
      "M": "\"You shall strike down the house of Ahab your master, so that I may avenge on Jezebel the blood of my servants the prophets and the blood of all the servants of the LORD.\"",
      "T": "The commission came with a specific mandate: destroy the house of Ahab — in judgment for Jezebel's systematic murder of the LORD's prophets (1 Kgs 18:4,13; 19:10,14). This was not personal vengeance or political ambition. It was divine retribution for the blood of the servants."
    },
    "8": {
      "L": "For the whole house of Ahab shall perish. I will cut off from Ahab every male, both the slave and the free in Israel.",
      "M": "\"The whole house of Ahab shall perish. I will cut off every male of Ahab's line, slave or free, in Israel.\"",
      "T": "\"The whole dynasty ends.\" The language echoes the oracle against Jeroboam and against Baasha — the same judicial formula (1 Kgs 14:10; 16:11). Ahab's house had replicated their sins and would meet their identical end."
    },
    "9": {
      "L": "I will make the house of Ahab like the house of Jeroboam son of Nebat, and like the house of Baasha son of Ahijah.",
      "M": "\"I will make the house of Ahab like the house of Jeroboam son of Nebat and like the house of Baasha son of Ahijah.\"",
      "T": "The explicit comparison: Ahab's dynasty will be wiped out the way Jeroboam's and Baasha's were. The pattern is now three-fold. Dynasties that led Israel into idolatry do not survive God's patience indefinitely."
    },
    "10": {
      "L": "The dogs shall eat Jezebel in the plot of Jezreel, and there shall be none to bury her. Then he opened the door and fled.",
      "M": "\"The dogs will devour Jezebel in the plot of land at Jezreel, and no one will bury her.\" Then the prophet opened the door and fled.",
      "T": "Jezebel's fate is named last and most precisely: dogs at Jezreel, no burial. The prophet spoke the word — Elijah's word from years before (1 Kgs 21:23) now on Elisha's messenger's lips — and then ran, exactly as instructed."
    },
    "11": {
      "L": "Then Jehu came out to the servants of his lord. And someone said to him, Is all well? Why did this mad fellow come to you? And he said to them, You know the man and his talk.",
      "M": "When Jehu came back out to his master's servants, someone asked him, \"Is everything all right? Why did that crazy fellow come to you?\" He replied, \"You know the type and the kind of thing they say.\"",
      "T": "Back among the officers, someone pressed him: \"What did that madman want?\" The dismissive term — \"this mad fellow\" — is how military men routinely spoke of prophets: religious eccentrics, not serious actors. Jehu deflected: \"You know how that sort talks.\" But he was already calculating."
    },
    "12": {
      "L": "And they said, That is a lie! Tell us. So he said, Thus and so he spoke to me, saying, Thus says the LORD: I anoint you king over Israel.",
      "M": "But they said, \"That is a lie! Tell us the truth.\" So he said, \"This is what he said to me: 'This is what the LORD says: I anoint you king over Israel.'\"",
      "T": "They pressed him — \"Stop hedging, tell us\" — and Jehu told them straight. The military officers heard the prophetic formula and understood immediately what it meant. The old order was over."
    },
    "13": {
      "L": "Then each man hastily took his garment and put it under him on the top of the stairs, and they blew the trumpet and said, Jehu is king.",
      "M": "Each man quickly took his cloak and spread it under Jehu on the top of the steps, and they blew the trumpet and proclaimed, \"Jehu is king!\"",
      "T": "They acted at once — a soldier's coronation, spontaneous and decisive. Cloaks spread on the steps, a trumpet blast, a shout: \"Jehu is king!\" It echoed the moment crowds spread garments before a king (cf. Matt 21:8). The officers had waited for exactly this permission."
    },
    "14": {
      "L": "So Jehu son of Jehoshaphat son of Nimshi conspired against Joram. Now Joram with all Israel had been guarding Ramoth-gilead against Hazael king of Syria.",
      "M": "So Jehu son of Jehoshaphat son of Nimshi formed a conspiracy against Joram. Meanwhile Joram with all Israel had been on guard at Ramoth-gilead against Hazael king of Syria.",
      "T": "The narrator gives us the strategic picture: Joram had been defending Ramoth-gilead — the frontier with Hazael — but was now absent, recovering in Jezreel from battle wounds. The fortress was held, but the king was unguarded. Jehu saw the window."
    },
    "15": {
      "L": "But King Joram had returned to Jezreel to be healed of the wounds that the Syrians had given him when he fought with Hazael king of Syria. And Jehu said, If this is your desire, let no one escape from the city to go and tell it in Jezreel.",
      "M": "King Joram had returned to Jezreel to recover from the wounds the Syrians had given him when he fought Hazael king of Syria. Jehu said, \"If this is what you want, let no one leave the city to carry word to Jezreel.\"",
      "T": "Jehu moved with military ruthlessness: lock down the city immediately. No dispatch riders, no warning to the court. Surprise was everything. The newly crowned king was already thinking like a commander."
    },
    "16": {
      "L": "Then Jehu rode in a chariot and went to Jezreel, for Joram was lying there. And Ahaziah king of Judah had come down to see Joram.",
      "M": "Then Jehu got into his chariot and drove toward Jezreel, for that was where Joram was laid up. And Ahaziah king of Judah had come down to visit Joram.",
      "T": "Jehu rode for Jezreel — not as an emissary but as an executioner. Unknowingly, Ahaziah king of Judah had also come to visit his sick uncle. Both kings were in one place, both about to meet the same instrument of God's judgment."
    },
    "17": {
      "L": "Now the watchman was standing on the tower in Jezreel. He spotted the company of Jehu as he came, and said, I see a company. And Joram said, Take a horseman and send to meet them and let him ask, Is it peace?",
      "M": "The watchman on the tower at Jezreel spotted Jehu's company approaching and reported, \"I see a company.\" Joram said, \"Take a horseman and send him to meet them and ask: Is it well?\"",
      "T": "From the watchtower the sentry reported movement — a company of riders approaching from the direction of Ramoth-gilead. Joram, bedridden and expecting dispatches from the front, sent a horseman with the standard greeting: \"Is all well?\""
    },
    "18": {
      "L": "So a horseman went to meet him and said, Thus says the king, Is it peace? And Jehu said, What have you to do with peace? Fall in behind me. The watchman reported, The messenger came to them but is not coming back.",
      "M": "So a horseman rode out to meet Jehu and said, \"The king asks: Is all well?\" Jehu answered, \"What is peace to you? Get behind me.\" The watchman reported, \"The messenger reached them but is not returning.\"",
      "T": "Jehu's answer dismissed the ritual greeting with contempt: \"What does peace have to do with you? Fall in behind me.\" He absorbed the messenger into his column. From the tower, the watchman watched the rider simply join the approaching group and not turn back. The irreversibility was beginning."
    },
    "19": {
      "L": "Then he sent out a second horseman. He came to them and said, Thus says the king, Is it peace? And Jehu answered, What have you to do with peace? Fall in behind me.",
      "M": "So the king sent out a second horseman. He came to them and said, \"The king asks: Is all well?\" Jehu answered, \"What does peace mean to you? Get behind me.\"",
      "T": "A second messenger — same errand, same contemptuous dismissal. Jehu was not answering questions; he was annexing messengers. The watchtower's reports were running out of explanations."
    },
    "20": {
      "L": "Again the watchman reported, He came to them also and is not coming back. And the driving is like the driving of Jehu son of Nimshi, for he drives furiously.",
      "M": "The watchman reported again, \"He reached them and is not returning either. And the driving looks like the driving of Jehu son of Nimshi — he drives like a madman.\"",
      "T": "The watchman's second report came with an identification: \"The driving — it is Jehu son of Nimshi; he drives like a madman.\" Jehu's reckless speed was apparently legendary. His character had already announced him."
    },
    "21": {
      "L": "And Joram said, Make ready. And his chariot was made ready. Then Joram king of Israel and Ahaziah king of Judah went out, each in his own chariot, and they went to meet Jehu and encountered him at the property of Naboth the Jezreelite.",
      "M": "Joram ordered, \"Harness up!\" His chariot was made ready. And Joram king of Israel and Ahaziah king of Judah rode out, each in his own chariot, to meet Jehu. They encountered him in the plot of Naboth the Jezreelite.",
      "T": "The sick king roused himself and rode out — and the two kings met Jehu at the exact spot where Ahab had stolen Naboth's vineyard. The narrator marks the location precisely. It was not coincidence: the God who promised \"I will repay you in this very plot\" (1 Kgs 21:19) had arranged the geography of judgment."
    },
    "22": {
      "L": "When Joram saw Jehu, he said, Is it peace, Jehu? He answered, What peace can there be, as long as the whoredoms of your mother Jezebel and her many witchcrafts are so great?",
      "M": "When Joram saw Jehu, he asked, \"Is this peace, Jehu?\" He answered, \"What peace can there be while your mother Jezebel's harlotries and her many sorceries continue?\"",
      "T": "\"Is it peace, Jehu?\" — the ritual question for the last time. Jehu's answer tore away the pretense: there was no possibility of peace so long as the covenant violations of Jezebel — her systematic spiritual adultery and her occult practices — remained unreckoned with. Peace without justice is not peace; it is merely deferred judgment."
    },
    "23": {
      "L": "And Joram turned his hands and fled and said to Ahaziah, Treachery, O Ahaziah!",
      "M": "Joram wheeled his chariot around and fled, crying to Ahaziah, \"Treachery, Ahaziah!\"",
      "T": "In an instant, Joram understood. He spun his chariot and fled, shouting the one word that explained everything to Ahaziah: \"Treachery!\" But the understanding came too late."
    },
    "24": {
      "L": "And Jehu drew his bow with full strength, and he shot Joram between the arms, and the arrow came out through his heart, and he collapsed in his chariot.",
      "M": "Jehu drew his bow with full force and shot Joram between the shoulders. The arrow went out through his heart, and he slumped down in his chariot.",
      "T": "Jehu's shot was perfect — between the shoulder blades, through the heart. The king of Israel collapsed in his chariot at the very place his father Ahab had murdered Naboth for his land."
    },
    "25": {
      "L": "Then Jehu said to Bidkar his officer, Take him up and throw him into the plot of ground belonging to Naboth the Jezreelite. For remember, when you and I were riding side by side behind Ahab his father, the LORD uttered this pronouncement against him:",
      "M": "Then Jehu said to Bidkar his officer, \"Pick him up and throw him into the plot of land belonging to Naboth the Jezreelite. Remember how, when you and I were riding together behind Ahab his father, the LORD spoke this pronouncement against him:\"",
      "T": "Jehu turned to his officer Bidkar — who had ridden beside him in Ahab's service — and invoked their shared memory: they had been there, the two of them, when Elijah pronounced the oracle over Ahab. \"You remember. Now we are watching the fulfillment.\" Jehu was not making it up; he was bearing witness."
    },
    "26": {
      "L": "Surely I have seen the blood of Naboth and the blood of his sons, declares the LORD, and I will repay you in this very plot of land, declares the LORD. Now therefore take him up and throw him into the plot of land, according to the word of the LORD.",
      "M": "\"'Surely I saw yesterday the blood of Naboth and the blood of his sons — declares the LORD — and I will repay you on this very plot of ground, declares the LORD.' So now lift him up and throw him into the plot, as the LORD said.\"",
      "T": "The oracle was precise: same plot, same blood. Ahab had taken Naboth's life to take his land; now Ahab's son's blood soaked that same ground. Jehu named it: \"according to the word of the LORD.\" This was judicial execution, not murder."
    },
    "27": {
      "L": "When Ahaziah king of Judah saw this, he fled by the way of the garden house. And Jehu pursued him and said, Shoot him also in the chariot. And they shot him at the ascent of Gur, which is near Ibleam. And he fled to Megiddo and died there.",
      "M": "When Ahaziah king of Judah saw what had happened, he fled toward Beth-haggan. Jehu pursued him, ordering, \"Shoot him too!\" They shot him in his chariot at the ascent of Gur near Ibleam. He fled to Megiddo and died there.",
      "T": "Ahaziah had seen his uncle fall and ran — but Jehu's orders were comprehensive. The king of Judah was struck on the road to Megiddo and died there. Being of Ahab's blood and Ahab's house was enough: the judgment of Ahab's dynasty did not stop at the kingdom border."
    },
    "28": {
      "L": "His servants carried him in a chariot to Jerusalem and buried him in his tomb in the city of David.",
      "M": "His servants brought his body in a chariot to Jerusalem and buried him in his tomb in the city of David.",
      "T": "Ahaziah was given a royal burial in Jerusalem — the honor due David's line. Even the instrument of judgment did not strip him of that. He was interred with his ancestors in the city of David."
    },
    "29": {
      "L": "In the eleventh year of Joram son of Ahab, Ahaziah became king over Judah.",
      "M": "In the eleventh year of Joram son of Ahab, Ahaziah had become king over Judah.",
      "T": "A brief synchronistic note, slightly inconsistent with 8:25 due to different counting methods for co-regencies. The historian preserves both calculations without harmonizing them."
    },
    "30": {
      "L": "When Jehu came to Jezreel, Jezebel heard of it. She painted her eyes with eye paint and adorned her head, and she looked out of the window.",
      "M": "When Jehu arrived at Jezreel, Jezebel heard about it. She put on eye makeup, arranged her hair, and looked down from a window.",
      "T": "Jezebel heard that Jehu was coming. She made up her face and dressed her hair and looked down from her window. She knew what was coming. This was not seduction — it was the act of a queen who would meet her death in full royal dignity. She would not be dragged out weeping; she would face her executioner composed."
    },
    "31": {
      "L": "And as Jehu entered the gate, she said, Is it peace, Zimri, murderer of your master?",
      "M": "As Jehu came through the gate, she called out, \"Is it peace, you Zimri, you murderer of your master?\"",
      "T": "Her last words were a taunt and a curse. \"Zimri\" — the officer who had slain Baasha's son Elah and lasted exactly seven days before his own soldiers turned on him (1 Kgs 16:9-20). She was predicting Jehu's end, and asserting her own dignity by refusing to beg. Whatever she was, she was not afraid."
    },
    "32": {
      "L": "And he lifted up his face to the window and said, Who is on my side? Who? And two or three eunuchs looked out at him.",
      "M": "He looked up to the window and called out, \"Who is on my side? Who?\" Two or three court officials looked down at him.",
      "T": "Jehu called up to the palace attendants — the eunuchs, the court officials — and asked whose side they were on. Two or three looked down. That was enough."
    },
    "33": {
      "L": "He said, Throw her down. So they threw her down, and some of her blood spattered on the wall and on the horses, and he trampled her under foot.",
      "M": "He said, \"Throw her down!\" So they threw her down. Some of her blood splattered on the wall and on the horses, and Jehu trampled her under his chariot.",
      "T": "The palace officials obeyed immediately — they had apparently been waiting for someone to give them permission to end Jezebel's reign. She fell. Her blood marked the wall and the horses. Jehu drove his chariot over her. The queen of Israel and the architect of Baal's cult in the northern kingdom was dead."
    },
    "34": {
      "L": "Then he went in and ate and drank. And he said, See now to this cursed woman and bury her, for she is a king's daughter.",
      "M": "Then Jehu went inside and ate and drank. He said, \"See to that cursed woman and bury her, for she is a king's daughter.\"",
      "T": "Jehu went inside and ate — the normal act, unhurried, the execution complete. Then, with a soldier's rough propriety, he gave an order: \"Bury her. Whatever she was, she was a king's daughter.\" Even in the act of judgment, a remnant of honor. The body deserved burial."
    },
    "35": {
      "L": "But when they went to bury her, they found nothing of her but the skull, the feet, and the palms of her hands.",
      "M": "But when they went to bury her, they found nothing of her except the skull, the feet, and the palms of her hands.",
      "T": "They were too late. The dogs had already come and taken almost everything. Only the skull, the feet, and the hands remained — the parts that dogs do not eat, the prophetic tradition says. Elijah's word from years before was being fulfilled with grotesque precision."
    },
    "36": {
      "L": "They returned and told him. And he said, This is the word of the LORD which he spoke by his servant Elijah the Tishbite: In the plot of Jezreel dogs shall eat the flesh of Jezebel.",
      "M": "They came back and told Jehu. And he said, \"This is the word that the LORD spoke through his servant Elijah the Tishbite: 'In the plot of Jezreel, dogs shall eat the flesh of Jezebel.'\"",
      "T": "Jehu received the news without surprise. He quoted the oracle from memory: Elijah's word spoken over Jezebel at Naboth's vineyard (1 Kgs 21:23). The fulfillment had arrived years after the prophet who spoke it was gone. God's words do not age."
    },
    "37": {
      "L": "And the corpse of Jezebel shall be as dung on the face of the field in the plot of Jezreel, so that no one shall say, This is Jezebel.",
      "M": "\"And the corpse of Jezebel shall be as dung on the surface of the field in the plot of Jezreel, so that no one will be able to say, 'This is Jezebel.'\"",
      "T": "No grave, no marker, no tomb, no epitaph. The woman who had built temples, marshaled prophets, and dominated two kingdoms was reduced to compost on the field of Jezreel. \"So that no one can say, 'This is Jezebel.'\" The ultimate dishonor for a queen: erasure."
    }
  },
  "10": {
    "1": {
      "L": "Now Ahab had seventy sons in Samaria. And Jehu wrote letters and sent them to Samaria, to the rulers of Jezreel, the elders, and the guardians of the children of Ahab, saying,",
      "M": "Now Ahab had seventy sons in Samaria. Jehu wrote letters and sent them to Samaria — to the rulers of Jezreel, the elders, and the guardians of Ahab's sons — saying,",
      "T": "Seventy royal sons in Samaria — a dynasty, a future. Jehu addressed the political class directly: the regional rulers, the city elders, the tutors and guardians of Ahab's heirs."
    },
    "2": {
      "L": "Now as soon as this letter comes to you, since your master's sons are with you, and with you are chariots and horses, a fortified city also, and weapons,",
      "M": "\"As soon as this letter reaches you, since your master's sons are with you and you have chariots and horses, a fortified city, and weapons —\"",
      "T": "Jehu's letter opened by cataloguing their strengths: they had the princes, the armory, the chariots, and a fortified city. He was daring them — or offering them a way out through the dare."
    },
    "3": {
      "L": "select the best and most capable of your master's sons and set him on his father's throne, and fight for your master's house.",
      "M": "\"select the best and most qualified of your master's sons and set him on his father's throne and fight for your master's house.\"",
      "T": "\"Choose your best candidate. Crown him. Fight for him.\" The challenge was explicit: if you are loyal to Ahab's house, now is the moment. Jehu was testing whether they had any resolve at all."
    },
    "4": {
      "L": "But they were exceedingly afraid and said, Behold, two kings could not stand before him. How then can we stand?",
      "M": "But they were utterly terrified and said, \"Look — two kings could not stand up to him. How are we going to stand?\"",
      "T": "The answer was fear: two kings — Joram of Israel and Ahaziah of Judah — had already fallen to Jehu in a single morning. What chance did palace officials have? The courage to resist had evaporated before the letter was finished."
    },
    "5": {
      "L": "So he who was over the household, and he who was over the city, together with the elders and the guardians, sent to Jehu, saying, We are your servants, and we will do whatever you tell us. We will not make any man king. Do what is good in your eyes.",
      "M": "So the palace administrator, the city governor, the elders, and the guardians sent word to Jehu: \"We are your servants and will do whatever you tell us. We will not appoint anyone as king. Do whatever you think best.\"",
      "T": "Immediate capitulation: the entire governing structure of Samaria submitted without a sword being drawn. \"We are your servants. Tell us what to do. We will not crown anyone against your will.\" The dynasty of Ahab had no defenders willing to die for it."
    },
    "6": {
      "L": "Then he wrote them a second letter, saying, If you are on my side and will listen to my voice, take the heads of your master's sons and come to me at Jezreel by tomorrow at this time. Now the king's sons, seventy men, were with the great men of the city who were raising them.",
      "M": "Then he wrote them a second letter: \"If you are on my side and will obey me, take the heads of your master's sons and come to me at Jezreel by this time tomorrow.\" Now the king's seventy sons were with the city's leading men who were responsible for raising them.",
      "T": "The second letter was the real test: if submission was genuine, prove it with action. Seventy heads by tomorrow. The historian notes where the sons were — with the great families of Samaria, their tutors and hosts. Those families would now face the impossible choice Jehu had set them."
    },
    "7": {
      "L": "When the letter came to them, they took the king's sons and slaughtered them, seventy men, and put their heads in baskets and sent them to him at Jezreel.",
      "M": "When the letter arrived, they killed all seventy of the king's sons and put their heads in baskets and sent them to Jehu at Jezreel.",
      "T": "They did it. The great men of Samaria — the tutors and guardians of Ahab's sons — slaughtered their own charges, seventy of them, and sent the heads in baskets. Self-preservation conquered every other loyalty. The dynasty of Ahab died without a single soldier fighting for it."
    },
    "8": {
      "L": "A messenger came and told him, They have brought the heads of the king's sons. And he said, Lay them in two heaps at the entrance of the gate until morning.",
      "M": "A messenger came to tell Jehu, \"They have brought the heads of the king's sons.\" He said, \"Pile them in two heaps at the entrance of the gate and leave them until morning.\"",
      "T": "Jehu staged the display deliberately: two piles of heads at the city gate, visible to all who entered or left Jezreel. The spectacle was meant to be witnessed. Tomorrow he would speak to it publicly."
    },
    "9": {
      "L": "In the morning he went out and stood and said to all the people, You are innocent. It was I who conspired against my master and killed him. But who struck down all these?",
      "M": "In the morning he went out and stood before the people and said, \"You are blameless. I was the one who conspired against my master and killed him. But who killed all these?\"",
      "T": "In the morning Jehu addressed the crowd with what looks like a rhetorical question but was actually a theological declaration. \"I killed Joram — that responsibility is mine. But these seventy? Who killed them?\" The answer he was leading toward: the LORD did, through the willing hands of Samaria's own leaders."
    },
    "10": {
      "L": "Know then that there shall fall to the earth nothing of the word of the LORD which the LORD spoke concerning the house of Ahab. For the LORD has done what he said by his servant Elijah.",
      "M": "\"Know, then, that nothing of the word of the LORD concerning the house of Ahab will fall to the ground. For the LORD has carried out what he declared through his servant Elijah.\"",
      "T": "The narrator's theology surfaces in Jehu's own speech: the seventy heads at the gate were not the result of political calculation or military strength — they were the fulfillment of a word spoken by Elijah years before. \"Nothing of the LORD's word will fall to the ground\" is the narrator's great assertion about prophetic reliability. The events themselves are theological argument."
    },
    "11": {
      "L": "So Jehu struck down all who remained of the house of Ahab in Jezreel, all his great men and his close friends and his priests, until he left him no survivor.",
      "M": "So Jehu killed everyone who remained of the house of Ahab in Jezreel — all his officials, his close associates, and his priests — until he had left not one survivor.",
      "T": "The purge was comprehensive: officials, associates, priests. The entire supporting structure of Ahab's regime — everyone who had enabled the dynasty's apostasy — was included in the judgment. Jehu fulfilled the commission to its last detail in Jezreel."
    },
    "12": {
      "L": "Then he set out and went to Samaria. At Beth-eked of the Shepherds, on the road,",
      "M": "He then set out and traveled toward Samaria. On the road, at Beth-eked of the Shepherds,",
      "T": "On the road to Samaria, Jehu encountered another group — this time unexpectedly, at a way station called Beth-eked of the Shepherds."
    },
    "13": {
      "L": "Jehu met the relatives of Ahaziah king of Judah and said, Who are you? And they answered, We are the relatives of Ahaziah, and we have come down to visit the sons of the king and the sons of the queen mother.",
      "M": "Jehu met the relatives of Ahaziah king of Judah. He asked, \"Who are you?\" And they answered, \"We are relatives of Ahaziah. We have come down to visit the royal princes and the sons of the queen mother.\"",
      "T": "Forty-two relatives of Ahaziah — the king of Judah Jehu had already slain — were traveling north to visit their cousins in Jezreel, unaware that those cousins were already dead. They identified themselves honestly. They did not know they were speaking to the man who had killed their king."
    },
    "14": {
      "L": "He said, Take them alive. And they took them alive and slaughtered them at the pit of Beth-eked, forty-two men, and he left none of them.",
      "M": "Jehu ordered, \"Take them alive.\" They were taken alive and then killed at the pit of Beth-eked — forty-two men. Jehu left none of them.",
      "T": "The order was immediate: all forty-two were killed. Their only offense was blood relationship to Ahaziah. The logic of dynastic purge extended across the border: the house of Ahab had penetrated Judah's royal family through Athaliah, and Jehu was cutting that connection completely."
    },
    "15": {
      "L": "When he departed from there, he met Jehonadab the son of Rechab coming to meet him. He greeted him and said to him, Is your heart true to my heart as my heart is to your heart? And Jehonadab answered, It is. Jehu said, If so, give me your hand. So he gave him his hand, and Jehu took him up into the chariot.",
      "M": "When Jehu left there, he encountered Jehonadab son of Rechab coming to meet him. He greeted him and asked, \"Is your heart with my heart as mine is with yours?\" Jehonadab answered, \"It is.\" Jehu said, \"If so, give me your hand.\" He gave him his hand, and Jehu pulled him up into the chariot.",
      "T": "A striking encounter: Jehonadab son of Rechab — the founder of the austere Rechabite community (Jer 35) — came out to meet Jehu. The Rechabites were famous for their strict fidelity to older ways, rejecting the corruptions of settled Canaanite life. Jehonadab's coming to Jehu was a public endorsement from a respected reformer. Jehu knew the symbolic value of having such a man beside him in his chariot."
    },
    "16": {
      "L": "And he said, Come with me and see my zeal for the LORD. So he had him ride in his chariot.",
      "M": "He said, \"Come with me and see my zeal for the LORD.\" So Jehonadab rode in Jehu's chariot.",
      "T": "\"Come and see my zeal for the LORD.\" The phrase is memorable and slightly ambiguous — was it genuine devotion, or was Jehu performing righteousness for a witness? The narrator preserves the tension. Jehu's zeal was real; his incomplete obedience (v.29-31) shows it was also selective."
    },
    "17": {
      "L": "When he came to Samaria, he struck down all who remained to Ahab in Samaria until he had destroyed them, according to the word that the LORD had spoken to Elijah.",
      "M": "When he arrived in Samaria, he killed all of Ahab's line who were still there, until he had wiped them out — in accordance with the word the LORD had spoken to Elijah.",
      "T": "A second fulfillment notice brackets the purge: as in Jezreel (v.10), so in Samaria. Elijah's oracle was executed to the last. The Deuteronomistic narrator states it twice to ensure the theological point lands: what happened was not politics — it was prophecy fulfilled."
    },
    "18": {
      "L": "Then Jehu gathered all the people and said to them, Ahab served Baal a little, but Jehu will serve him much.",
      "M": "Then Jehu assembled all the people and said to them, \"Ahab served Baal only a little, but Jehu will serve him much more.\"",
      "T": "Jehu's deception was as bold as it was cynical: he called a public assembly and announced that he would be an even more devoted servant of Baal than Ahab. He was deliberately gathering the entire Baal cult in one place under the cover of a grand sacrifice."
    },
    "19": {
      "L": "Now therefore call to me all the prophets of Baal, all his worshipers, and all his priests. Let none be missing, for I have a great sacrifice to offer to Baal. Whoever is missing shall not live. But Jehu was acting with cunning in order to destroy the worshipers of Baal.",
      "M": "\"So now summon all the prophets of Baal, all his worshipers, and all his priests. Let none be absent, for I have a great sacrifice to Baal. Anyone who is missing will not live.\" But Jehu was acting with guile in order to destroy the worshipers of Baal.",
      "T": "The narrator breaks the fourth wall to tell us what Jehu was actually doing: subterfuge in service of destruction. The assembly was a trap. Threatening death for non-attendance guaranteed full turnout. The threat he intended for Baal-worshipers, he framed as a threat against non-attendees."
    },
    "20": {
      "L": "And Jehu commanded, Proclaim a solemn assembly for Baal. So they proclaimed it.",
      "M": "Jehu gave the order: \"Announce a solemn assembly for Baal.\" So they made the proclamation.",
      "T": "The public announcement went out — the full formal language of a sacred convocation. Baal's worshipers would have heard it as an extraordinary act of royal piety."
    },
    "21": {
      "L": "And Jehu sent throughout all Israel. And all the worshipers of Baal came, so that there was not a man left who did not come. They entered the house of Baal, and the house of Baal was filled from one end to the other.",
      "M": "Jehu sent word throughout all Israel, and all the worshipers of Baal came — not one was absent. They went into the house of Baal, and the house of Baal was packed full from end to end.",
      "T": "The turnout was total — every Baal-worshiper in Israel came to what they believed was their great festival. The house was standing room only. Jehu had assembled his targets in one building."
    },
    "22": {
      "L": "He said to the man who was over the wardrobe, Bring out vestments for all the worshipers of Baal. So he brought them out vestments.",
      "M": "He said to the keeper of the wardrobe, \"Bring out vestments for all the worshipers of Baal.\" So he brought out vestments for them.",
      "T": "Jehu added a detail that completed the deception: official cultic garments distributed to every participant. The vestments served two purposes — they sustained the illusion of a genuine festival, and they marked every Baal-worshiper with visible identification."
    },
    "23": {
      "L": "Then Jehu went into the house of Baal with Jehonadab son of Rechab. He said to the worshipers of Baal, Search and see that there is no servant of the LORD here among you, but only the worshipers of Baal.",
      "M": "Then Jehu went into the house of Baal with Jehonadab son of Rechab. He said to the Baal-worshipers, \"Search carefully and make sure there is no servant of the LORD here among you — only worshipers of Baal.\"",
      "T": "Jehu entered with his ally Jehonadab — the reformer's presence lending legitimacy to the ceremony. His instruction to check for infiltrators was also a guarantee to the Baal-worshipers: this gathering was exclusively for them, no informants from Jehu's camp. The irony was complete — Jehu himself was the one playing a role."
    },
    "24": {
      "L": "So they went in to offer sacrifices and burnt offerings. Now Jehu had stationed eighty men on the outside and said, If any of the men I am delivering into your hands escapes, his life shall be for your life.",
      "M": "So they went in to offer sacrifices and burnt offerings. Now Jehu had stationed eighty men outside, with orders: \"If any man I am handing over to you escapes, you will pay for it with your own life.\"",
      "T": "While the ceremony proceeded inside, eighty soldiers were posted around the building with orders backed by lethal consequences for failure. The personal accountability Jehu placed on the guards ensured vigilance. Not one was to leave."
    },
    "25": {
      "L": "As soon as he had finished offering the burnt offering, Jehu commanded the guards and the officers, Go in and strike them down; let none come out. So they struck them down with the edge of the sword. The guards and the officers threw them out and went to the inner room of the house of Baal.",
      "M": "As soon as he had finished presenting the burnt offering, Jehu commanded the guards and the officers: \"Go in and cut them down; let no one get out.\" They struck them down with the sword. The guards and officers threw out the bodies and went into the inner shrine of the house of Baal.",
      "T": "The moment the ceremony concluded — Jehu himself apparently participating in the ritual to the end — the order was given. The soldiers entered and killed everyone inside. Then they moved through the building systematically, into the inner shrine. The house of Baal was cleared."
    },
    "26": {
      "L": "And they brought out the sacred pillars of the house of Baal and burned them.",
      "M": "They brought out the sacred pillar of the house of Baal and burned it.",
      "T": "The cult objects — the sacred standing stone or pillar (massebah) associated with Baal worship — were brought out and destroyed by fire. The physical infrastructure of the cult was dismantled."
    },
    "27": {
      "L": "And they demolished the pillar of Baal, and they demolished the house of Baal, and made it a latrine to this day.",
      "M": "They tore down the pillar of Baal and demolished the house of Baal, turning it into a latrine that remains to this day.",
      "T": "Complete desecration: first demolished, then repurposed as a public latrine. The deliberate choice of the most degrading possible use communicated a theological judgment — the house of Baal deserved not preservation, not neglect, but active dishonor. It stood as a monument to that verdict in the narrator's own day."
    },
    "28": {
      "L": "Thus Jehu wiped out Baal from Israel.",
      "M": "So Jehu eliminated Baal worship from Israel.",
      "T": "One sentence for a significant achievement. Baal's national cult — established by Ahab and Jezebel, protected by royal power, fed by Phoenician imports — was gone. Whatever else may be said of Jehu's methods, this was real and lasting."
    },
    "29": {
      "L": "However, Jehu did not depart from the sins of Jeroboam son of Nebat, who made Israel to sin — that is, the golden calves in Bethel and in Dan.",
      "M": "However, Jehu did not turn away from the sins of Jeroboam son of Nebat, who had led Israel into sin — the golden calves at Bethel and at Dan.",
      "T": "The qualification follows immediately: Baal was destroyed, but the golden calves at Bethel and Dan remained. The calves were not foreign imports — they were Jeroboam's own political-religious invention (1 Kgs 12:28-30), serving as state cult objects for the northern kingdom. Jehu's reform had limits. He purged what threatened him politically; he kept what sustained the kingdom's religious identity."
    },
    "30": {
      "L": "And the LORD said to Jehu, Because you have done well in carrying out what is right in my eyes, and have done to the house of Ahab according to all that was in my heart, your sons of the fourth generation shall sit on the throne of Israel.",
      "M": "The LORD said to Jehu, \"Because you have done well — you carried out what I considered right, and dealt with the house of Ahab exactly as I purposed — your descendants to the fourth generation shall sit on the throne of Israel.\"",
      "T": "God honored Jehu's obedience with a dynasty-promise: four generations on Israel's throne. The qualification in v.31 makes clear this was not unconditional, but the promise was real. God recognizes genuine obedience even in an imperfect servant. Jehu's line would hold the throne longer than any other in the northern kingdom."
    },
    "31": {
      "L": "But Jehu was not careful to walk in the law of the LORD, the God of Israel, with all his heart. He did not depart from the sins of Jeroboam, which he made Israel to sin.",
      "M": "But Jehu was not careful to walk in the law of the LORD, the God of Israel, with all his heart. He did not turn away from the sins of Jeroboam, which he had led Israel to commit.",
      "T": "The narrator insists on the full picture: Jehu's zeal for the LORD was real but partial. He destroyed what God explicitly commissioned him to destroy. He did not pursue the deeper reformation that the law required. The golden calves remained because Jehu's obedience was calculated, not whole-hearted. Partial reform does not transform a nation."
    },
    "32": {
      "L": "In those days the LORD began to trim Israel short. And Hazael defeated them throughout the territory of Israel,",
      "M": "In those days the LORD began to reduce the size of Israel. Hazael struck them throughout the territory of Israel,",
      "T": "The consequence of Jehu's incomplete obedience began to appear in his own lifetime: Hazael — the murderer whom Elisha had wept over (8:11-12) — began cutting into Israel's territory. The verb \"trim short\" is the Hebrew image of a land being whittled down. God was using Israel's enemies as instruments of discipline."
    },
    "33": {
      "L": "from the Jordan eastward — all the land of Gilead, the Gadites, and the Reubenites, and the Manassites, from Aroer which is by the Wadi Arnon, that is Gilead and Bashan.",
      "M": "from the Jordan eastward — all the land of Gilead, the Gadites, the Reubenites, and the Manassites, from Aroer by the Wadi Arnon, that is all of Gilead and Bashan.",
      "T": "Transjordan — all the territory east of the Jordan River — fell to Hazael: the tribal lands of Gad, Reuben, and half-Manasseh, from the Arnon gorge north to Bashan. Israel's territory was being stripped down to its western core. Jehu held the throne; he was losing the land."
    },
    "34": {
      "L": "Now the rest of the acts of Jehu, and all that he did, and all his might, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "M": "As for the rest of Jehu's acts, everything he did, and all his achievements, are they not recorded in the Book of the Chronicles of the Kings of Israel?",
      "T": "The closing formula directs readers to the fuller record. What was accomplished militarily and administratively in twenty-eight years is compressed into a summary. The history that mattered was theological, not political."
    },
    "35": {
      "L": "So Jehu slept with his fathers, and they buried him in Samaria. And Jehoahaz his son reigned in his place.",
      "M": "Jehu rested with his ancestors and was buried in Samaria. His son Jehoahaz became king in his place.",
      "T": "Jehu died and was buried with honor in the capital. His son Jehoahaz succeeded him — the first generation of the four promised in v.30 was already in place."
    },
    "36": {
      "L": "The time that Jehu reigned over Israel in Samaria was twenty-eight years.",
      "M": "Jehu had reigned over Israel in Samaria for twenty-eight years.",
      "T": "Twenty-eight years — the longest reign in the northern kingdom's history to this point, and the dynasty would continue for three more generations after him. The promise of v.30 was being kept."
    }
  },
  "11": {
    "1": {
      "L": "Now when Athaliah the mother of Ahaziah saw that her son was dead, she arose and destroyed all the royal seed.",
      "M": "When Athaliah the mother of Ahaziah saw that her son was dead, she rose up and killed all the royal family.",
      "T": "Athaliah — daughter of Omri, daughter-in-law of Ahab, mother of Ahaziah — moved the moment she heard her son was dead. She killed the entire royal family of Judah. Every grandson, every potential heir — all of them. She was seizing the throne, and she was eliminating every challenge to it. For the first time since David, Judah's royal house was apparently extinct."
    },
    "2": {
      "L": "But Jehosheba, the daughter of King Joram and sister of Ahaziah, took Joash son of Ahaziah and stole him away from among the king's sons who were being slaughtered. She put him and his nurse in a bedroom. Thus they hid him from Athaliah, and he was not put to death.",
      "M": "But Jehosheba, daughter of King Joram and sister of Ahaziah, took Joash son of Ahaziah and smuggled him out from among the king's sons who were being killed. She hid him and his nurse in a bedroom, and thus concealed him from Athaliah, so he was not put to death.",
      "T": "One woman — a princess, the king's daughter and the dead king's sister — hid one infant boy. Jehosheba pulled Joash out of the slaughter room and concealed him with his nurse in a private chamber. The Davidic covenant (2 Sam 7:12-16) survived by a single hidden child in a single bedroom. God's promise to David was protected by a woman's courage and a nurse's silence."
    },
    "3": {
      "L": "And he was with her hidden in the house of the LORD for six years, while Athaliah reigned over the land.",
      "M": "He remained with her hidden in the house of the LORD for six years, while Athaliah ruled the land.",
      "T": "Six years the child lived in the temple complex — hidden in God's own house while a usurper sat on David's throne. The lamp that 8:19 says God promised never to extinguish was burning in secret, tended by priests, within the sanctuary."
    },
    "4": {
      "L": "But in the seventh year, Jehoiada sent and brought the captains of hundreds of the Carites and of the guard, and had them come to him in the house of the LORD. He made a covenant with them and put them under oath in the house of the LORD, and showed them the king's son.",
      "M": "In the seventh year, Jehoiada sent for the commanders of the Carites and the royal guard and had them come to him in the house of the LORD. He made a covenant with them, put them under oath in the house of the LORD, and showed them the king's son.",
      "T": "In the seventh year, Jehoiada the priest acted. He called the commanders of the palace guard and the Carite mercenaries — the professional soldiers who protected the king — into the temple. There, in the LORD's house, he showed them the hidden child and bound them under oath. The covenant he made was the foundation for what followed: a constitutional restoration, not merely a coup."
    },
    "5": {
      "L": "He commanded them, saying, This is what you shall do: One third of you who come on duty on the Sabbath shall guard the king's house,",
      "M": "He gave them these instructions: \"This is what you are to do: A third of you who come on duty on the Sabbath are to guard the royal palace;",
      "T": "Jehoiada's plan was precise: he coordinated both the incoming and outgoing Sabbath guard shifts so that more men than usual were present simultaneously. Normally the Sabbath rotation halved the guard; he arranged to keep all of them. The detail matters — he was not relying on loyalty alone but on overwhelming numbers."
    },
    "6": {
      "L": "one third shall be at the gate of Sur, and one third at the gate behind the guard. And you shall guard the house in shifts.",
      "M": "a third at the Gate of Sur, and a third at the gate behind the guards. So you will guard the house from every side.",
      "T": "Three stations: the palace, the southern gate, the gate behind the guardroom. Every access point covered. The plan closed every escape route from the palace complex."
    },
    "7": {
      "L": "And the two divisions of all of you who go off duty on the Sabbath shall keep watch over the house of the LORD for the king.",
      "M": "The two sections of all of you who go off duty on the Sabbath are to stand guard at the house of the LORD for the king.",
      "T": "Both outgoing shifts — normally dismissed — were retained and stationed in the temple courts. The king's son would be surrounded by a full protective force, not a skeleton guard."
    },
    "8": {
      "L": "You shall surround the king, each with his weapons in his hand. Whoever approaches the ranks shall be put to death. Be with the king as he goes out and as he comes in.",
      "M": "Surround the king on every side, each of you with his weapon in his hand. Put to death anyone who comes within the ranks. Be with the king wherever he goes.\"",
      "T": "The orders were unambiguous: stand in formation, weapons ready, no gaps. Anyone who tried to break through was to be killed on the spot. The king — once revealed — was to be physically surrounded at all times. No detail was left to improvisation."
    },
    "9": {
      "L": "The captains of hundreds did according to all that Jehoiada the priest commanded. Each man brought his men — those who were to come in on the Sabbath and those who were to go out on the Sabbath — and came to Jehoiada the priest.",
      "M": "The commanders of hundreds did everything that Jehoiada the priest ordered. Each brought his men — both those going on duty on the Sabbath and those going off duty — and came to Jehoiada the priest.",
      "T": "Complete obedience from the military commanders. Every officer followed the plan exactly. The combination of Jehoiada's authority, the sanctity of the oath sworn in the temple, and the sight of the hidden legitimate king had unified the guard."
    },
    "10": {
      "L": "And the priest gave to the captains of hundreds the spears and shields that had been King David's, which were in the house of the LORD.",
      "M": "The priest gave to the commanders of hundreds the spears and shields that had belonged to King David, which were kept in the house of the LORD.",
      "T": "Jehoiada armed the officers with David's own weapons — a deeply symbolic act. The restoration of the Davidic king would be accomplished with David's own armory. The weapons had been kept in the temple, presumably as sacred relics or trophies. They were now put back to their original purpose."
    },
    "11": {
      "L": "And the guard stood, every man with his weapons in his hand, from the south side of the house to the north side of the house, around the altar and around the house.",
      "M": "The guards took their positions, each with his weapon in hand, from the south end of the temple to the north end, around both the altar and the temple.",
      "T": "The formation enclosed the entire temple precinct: from the south wall to the north wall, around the altar at the center. The child-king would be crowned in the sight of the whole armed assembly — and no one from outside could interfere."
    },
    "12": {
      "L": "Then he brought out the king's son and put the crown on him and gave him the testimony. They proclaimed him king and anointed him. They clapped their hands and said, Long live the king!",
      "M": "Then Jehoiada brought out the king's son, put the crown on him, and gave him the covenant document. They proclaimed him king and anointed him, and they clapped their hands and shouted, \"Long live the king!\"",
      "T": "The coronation followed the ancient protocol: the crown placed on the child, the covenant document — perhaps the law of the king from Deut 17:18-20 — placed in his hands, the anointing with oil, and the acclamation of the people. The shouted affirmation \"Long live the king!\" was the people's ratification. Joash was perhaps seven or eight years old, and he was king."
    },
    "13": {
      "L": "When Athaliah heard the noise of the guard and of the people, she came to the people at the house of the LORD.",
      "M": "When Athaliah heard the noise of the guard and of the people, she came into the house of the LORD to where the people were.",
      "T": "The sound of celebration from the temple complex reached the palace. Athaliah came to see what was happening. She walked into the trap — or rather, into the scene that ended her reign."
    },
    "14": {
      "L": "And when she looked, behold, the king was standing by the pillar, according to the custom, with the commanders and the trumpeters beside the king, and all the people of the land rejoicing and blowing trumpets. And Athaliah tore her clothes and cried out, Treason! Treason!",
      "M": "When she looked, there was the king standing by the pillar, as was the custom, with the commanders and the trumpeters beside the king, and all the people of the land rejoicing and blowing trumpets. Athaliah tore her clothes and cried out, \"Treason! Treason!\"",
      "T": "Everything was done by protocol: the king stood at the royal pillar in the temple, the place where covenants were made and kings were crowned (23:3). The scene was constitutionally correct — a legitimate coronation. Athaliah's cry of \"Treason!\" was the usurper's accusation against the lawful heir. The irony was lost on no one present."
    },
    "15": {
      "L": "Then Jehoiada the priest commanded the captains of hundreds who were set over the army: Bring her out between the ranks, and anyone who follows her shall be put to death with the sword. For the priest said, Let her not be put to death in the house of the LORD.",
      "M": "Jehoiada the priest ordered the commanders of hundreds who were in charge of the troops: \"Take her out between the ranks, and execute with the sword anyone who follows her.\" For the priest had said, \"She must not be killed in the house of the LORD.\"",
      "T": "Jehoiada was precise even in this: she was to be taken outside the temple precincts before execution. The house of the LORD was not to be polluted with blood — even the blood of an usurper. The law's sanctity governed the manner of judgment."
    },
    "16": {
      "L": "So they laid hands on her, and she went by the way of the horses' entrance to the king's house, and there she was put to death.",
      "M": "So they seized her, and she was brought to the royal palace through the entry of the horses' gate, and there she was put to death.",
      "T": "She was taken out through the horse gate — the service entrance to the palace — and executed there. Athaliah's six-year reign, built on the murder of children and maintained by Baal's patronage, ended at a stable entrance. It was an appropriately unglamorous conclusion."
    },
    "17": {
      "L": "And Jehoiada made a covenant between the LORD and the king and the people, that they should be the LORD's people, and also between the king and the people.",
      "M": "Then Jehoiada made a covenant between the LORD and the king and the people, that they would be the LORD's people, and also a covenant between the king and the people.",
      "T": "Three covenants in a single moment: between the LORD and the king, between the LORD and the people, and between the king and the people. This triple covenant echoed the great constitutional moments of Israel's history — Joshua's covenant at Shechem (Josh 24), David's coronation covenant (2 Sam 5:3), and the Mosaic covenant's renewal pattern throughout Deuteronomy. What had been broken by Athaliah's usurpation was formally restored. The kingdom was re-founded on covenant."
    },
    "18": {
      "L": "Then all the people of the land went to the house of Baal and tore it down. His altars and his images they smashed thoroughly, and they killed Mattan the priest of Baal before the altars. And Jehoiada the priest set guards over the house of the LORD.",
      "M": "Then all the people of the land went to the house of Baal and tore it down. They smashed his altars and his images completely, and they killed Mattan the priest of Baal in front of the altars. Jehoiada the priest posted watchmen over the house of the LORD.",
      "T": "The covenantal reform had an immediate concrete expression: the people themselves demolished the house of Baal in Jerusalem. Athaliah had introduced Baal worship to Judah just as Jezebel had done in the north. Now the people tore it down with their own hands. Mattan the Baal-priest was killed. Jehoiada set guards at the temple to protect it from further encroachment. Covenant renewal was not merely declaratory — it required physical action."
    },
    "19": {
      "L": "And he took the captains, the Carites, the guards, and all the people of the land. And they brought the king down from the house of the LORD, going through the gate of the guards to the king's house. And he took his seat on the throne of the kings.",
      "M": "Then Jehoiada took the commanders of hundreds, the Carites, the guards, and all the people of the land, and they brought the king down from the house of the LORD, marching through the gate of the guards to the royal palace. And the king sat on the royal throne.",
      "T": "The procession moved from the temple to the palace — the same route that ran between the two centers of power in Jerusalem. The child-king was escorted by the full military and civilian establishment and seated on the throne of David. Six years hidden; now publicly enthroned."
    },
    "20": {
      "L": "So all the people of the land rejoiced, and the city was quiet. And they put Athaliah to death with the sword at the king's house.",
      "M": "All the people of the land rejoiced, and the city was calm. They had put Athaliah to death with the sword at the royal palace.",
      "T": "The city's mood: relief and celebration. \"The city was quiet\" — the phrase denotes stability restored after upheaval, the settled peace of legitimate order. The contrast with Athaliah's six years of stolen rule is the narrator's final comment on her reign."
    },
    "21": {
      "L": "Jehoash was seven years old when he began to reign.",
      "M": "Jehoash was seven years old when he became king.",
      "T": "Seven years old. The Davidic line survived in a child who had spent his earliest years in hiding in a bedroom in the temple. The lamp that God promised David (8:19) flickered but did not go out."
    }
  },
  "12": {
    "1": {
      "L": "In the seventh year of Jehu, Jehoash became king, and he reigned forty years in Jerusalem. His mother's name was Zibiah of Beersheba.",
      "M": "In the seventh year of Jehu, Jehoash became king. He reigned forty years in Jerusalem. His mother's name was Zibiah of Beersheba.",
      "T": "The synchronism anchors Joash's accession: year 7 of Jehu's reign in the north. Forty years in Jerusalem — one of the longer reigns in Judah's history. His mother's name, Zibiah of Beersheba, locates her in the deep south of Judah, far from Athaliah's Phoenician influence."
    },
    "2": {
      "L": "And Jehoash did what was right in the sight of the LORD all his days, because Jehoiada the priest instructed him.",
      "M": "Jehoash did what was right in the sight of the LORD all his days, for Jehoiada the priest had instructed him.",
      "T": "The verdict is positive — but the narrator immediately qualifies it: his righteousness was conditioned on Jehoiada's instruction. What happens after Jehoiada dies is implied by this qualification. The king who needed a guide was vulnerable when the guide was gone (the fuller picture in 2 Chron 24:17-22 bears this out)."
    },
    "3": {
      "L": "Nevertheless, the high places were not taken away; the people still sacrificed and burned incense at the high places.",
      "M": "Nevertheless, the high places were not removed; the people continued to sacrifice and burn incense at the high places.",
      "T": "The standard qualification for partially faithful kings: the high places persisted. Baal's temple was destroyed (11:18), but the decentralized worship at local hilltop shrines remained. Centralization of worship at Jerusalem was the Deuteronomistic ideal; Joash did not pursue it."
    },
    "4": {
      "L": "And Jehoash said to the priests, All the money of the dedicated gifts that is brought into the house of the LORD — the money for which each person is assessed — all the money that anyone brings of his own free will to the house of the LORD,",
      "M": "Jehoash told the priests, \"All the money brought as consecrated gifts to the house of the LORD — the census money, personal redemption payments, and whatever anyone voluntarily donates to the house of the LORD —\"",
      "T": "Jehoash initiated a temple repair project, the first significant institutional act of his reign. He enumerated the revenue streams: the census tax (Exod 30:12-16), redemption money, and freewill offerings. All of it was to fund repairs."
    },
    "5": {
      "L": "let the priests take it, each from his acquaintance. And let them repair whatever damage is found in the house.",
      "M": "\"the priests are to accept it from those who bring it, each from his own contacts. And they are to repair whatever damage they find in the house.\"",
      "T": "The initial system delegated collection and repair to individual priests, each responsible for donations from their own patrons and networks. The decentralized approach seemed reasonable — but it did not work."
    },
    "6": {
      "L": "But it was so that in the twenty-third year of King Jehoash, the priests had not repaired the damage of the house.",
      "M": "But by the twenty-third year of King Jehoash's reign, the priests had still not repaired the temple.",
      "T": "Twenty-three years later — nothing done. The priests had apparently collected money and used it for other purposes, or simply failed to organize the work. The temple stood in disrepair for nearly a quarter century under a king who was supposed to be faithful."
    },
    "7": {
      "L": "Therefore King Jehoash summoned Jehoiada the priest and the other priests and said to them, Why are you not repairing the damage of the house? Now therefore take no more money from your donors, but hand it over for the repair of the house.",
      "M": "So King Jehoash summoned Jehoiada the priest and the other priests and said to them, \"Why are you not repairing the damage to the temple? From now on, stop accepting money from your donors and turn it directly over for the repair of the temple.\"",
      "T": "Joash confronted the priests directly: twenty-three years, nothing accomplished. The reform was structural: priests would no longer handle the money at all. They would give up their fundraising role entirely. The conflict between the king and the temple administration was being settled in the king's favor."
    },
    "8": {
      "L": "So the priests agreed that they would not accept any more money from the people, and that they would not repair the damage of the house.",
      "M": "So the priests agreed not to accept any more money from the people and not to be responsible for repairing the temple.",
      "T": "The priests accepted the new arrangement — or rather, they accepted the removal of their responsibility. They were no longer in charge of temple finances. The trade-off: less income, less accountability, less work. They agreed readily enough."
    },
    "9": {
      "L": "Then Jehoiada the priest took a chest and bored a hole in its lid and set it beside the altar on the right side as one enters the house of the LORD. The priests who kept the threshold put into it all the money that was brought into the house of the LORD.",
      "M": "Then Jehoiada the priest took a chest, bored a hole in its lid, and placed it beside the altar on the right side as you enter the house of the LORD. The priests who guarded the entrance deposited into it all the money brought to the house of the LORD.",
      "T": "A locked collection box at the temple entrance — the first recorded example of a dedicated charitable collection mechanism in the Bible. Transparent and public: money dropped in by worshipers, accumulated visibly, accessible only through the locked lid. The design removed discretion from individual priests and created accountability through structure."
    },
    "10": {
      "L": "And whenever they saw that there was much money in the chest, the king's secretary and the high priest came up and tied up in bags and counted the money that was found in the house of the LORD.",
      "M": "Whenever there was a large amount in the chest, the king's secretary and the high priest came and counted the money found in the house of the LORD and tied it up in bags.",
      "T": "The counting process involved both royal oversight (the king's secretary) and priestly oversight (the high priest) — dual accountability. The money was bagged and counted formally, not simply passed from hand to hand. This is the oldest recorded government auditing procedure in the Bible."
    },
    "11": {
      "L": "Then they gave the money that was weighed out into the hands of the workmen who had the oversight of the house of the LORD. And they paid it out to the carpenters and builders who worked on the house of the LORD,",
      "M": "They paid out the counted money to the workers in charge of the house of the LORD, who used it to pay the carpenters and builders working on the house of the LORD,",
      "T": "The money went directly to the construction supervisors, who paid the skilled workers — carpenters, builders, masons. The chain of custody was clear: collection box, formal count, payment to supervisors, payment to workers. Every step was documented."
    },
    "12": {
      "L": "to the masons and the stone cutters, as well as to buy timber and cut stone to repair the damage to the house of the LORD, and for all that was paid out for the house to repair it.",
      "M": "and to the masons and stonecutters, and to purchase timber and cut stone to make the repairs to the house of the LORD — whatever was needed for the repair.",
      "T": "The list of materials and labor covers the full scope: skilled tradesmen, materials sourced and cut, all the costs of a genuine building project. This was not cosmetic repair; it was structural restoration."
    },
    "13": {
      "L": "However, there were not made for the house of the LORD any silver basins, snuffers, bowls, trumpets, or any vessels of gold or silver, from the money that was brought into the house of the LORD.",
      "M": "However, no silver basins, snuffers, bowls, trumpets, or any vessels of gold or silver were made for the house of the LORD from this money.",
      "T": "A careful distinction: the donated money was for structural repair only — walls, floors, roofing. Temple furnishings and liturgical equipment would not be purchased with it. The priority was the building's integrity, not its decoration. The historian records this as evidence of fiscal discipline."
    },
    "14": {
      "L": "It was given to the workmen, and they repaired the house of the LORD with it.",
      "M": "All of it was paid to the workmen, and they used it to repair the house of the LORD.",
      "T": "Every shekel collected went to the workers. No diversion, no overhead, no priestly portion withheld. The temple was repaired."
    },
    "15": {
      "L": "Moreover, they did not ask for an accounting from the men into whose hand they delivered the money to be paid out to the workmen, for they dealt honestly.",
      "M": "They did not require an accounting from the men who received the money to pay the workers, because they dealt honestly.",
      "T": "No audit was required of the supervisors — not because accountability was abandoned, but because their honesty was already established and trusted. The historian records this as unusual enough to note: these men could be trusted with unaudited funds. Integrity in public office was rare enough to be remarkable."
    },
    "16": {
      "L": "The money from the guilt offerings and the money from the sin offerings was not brought into the house of the LORD; it belonged to the priests.",
      "M": "The money from the guilt offerings and the sin offerings was not brought into the house of the LORD; it belonged to the priests.",
      "T": "A clarification of the arrangement: the trespass and sin offering revenue was a separate stream entirely, reserved for the priests as their allocated portion under the law (Lev 5:16; 7:7). This money was not redirected to the building fund. The reform did not deprive the priests of their lawful income — it only removed their control over the general donations."
    },
    "17": {
      "L": "At that time Hazael king of Syria went up and fought against Gath and took it. And when Hazael set his face to go up against Jerusalem,",
      "M": "At that time Hazael king of Syria marched up and attacked Gath and captured it. Then he set his sights on going up against Jerusalem.",
      "T": "The Syrian threat arrived in Joash's own reign. Hazael — the murderer whom Elisha had wept over decades earlier — had been systematically expanding southward. He took Gath, the Philistine city on the coastal plain, and then turned his eyes toward Jerusalem. The shadow of judgment was stretching over Judah."
    },
    "18": {
      "L": "Jehoash king of Judah took all the dedicated gifts that Jehoshaphat and Jehoram and Ahaziah, his ancestors, the kings of Judah, had dedicated, and his own dedicated gifts, and all the gold that was found in the treasuries of the house of the LORD and of the king's house, and sent them to Hazael king of Syria. So he withdrew from Jerusalem.",
      "M": "Jehoash king of Judah took all the consecrated gifts that his predecessors — Jehoshaphat, Jehoram, and Ahaziah, kings of Judah — had dedicated, as well as his own gifts, and all the gold found in the treasuries of the house of the LORD and the royal palace, and sent it all to Hazael king of Syria. And Hazael withdrew from Jerusalem.",
      "T": "Joash bought off Hazael with everything in both the temple and royal treasury — multiple generations of accumulated royal gifts, his own dedicated treasures, all the gold. It worked: Hazael took the bribe and turned away. But the temple Joash had spent years and enormous resources repairing was now stripped of its treasury to pay for survival. The irony is bitter: the faithful king who rebuilt the house of the LORD emptied it to save the city."
    },
    "19": {
      "L": "Now the rest of the acts of Joash, and all that he did, are they not written in the Book of the Chronicles of the Kings of Judah?",
      "M": "As for the rest of the acts of Joash and all that he did, are they not recorded in the Book of the Chronicles of the Kings of Judah?",
      "T": "The standard closing formula. Whatever else Joash did — and his reign had significant administrative achievements — the historian's selective account focuses on the temple repair and the Syrian crisis."
    },
    "20": {
      "L": "His servants arose and made a conspiracy and struck down Joash at the house of Millo, on the road that goes down to Silla.",
      "M": "His servants formed a conspiracy and struck down Joash at Beth-millo, on the road that goes down to Silla.",
      "T": "Joash was assassinated by his own servants — a conspiracy within the palace. The location, Beth-millo, was an administrative complex in Jerusalem. He was killed in transit, on a road — not even in the safety of the palace or the temple. The king who had survived Athaliah's massacre as an infant died at the hands of his own household."
    },
    "21": {
      "L": "For Jozachar son of Shimeath and Jehozabad son of Shomer, his servants, struck him down, and he died. And they buried him with his fathers in the city of David. And Amaziah his son reigned in his place.",
      "M": "It was Jozachar son of Shimeath and Jehozabad son of Shomer, his servants, who struck him down, and he died. He was buried with his ancestors in the city of David, and his son Amaziah became king in his place.",
      "T": "The assassins are named — a rare detail, suggesting the historian drew on formal court records. Joash received burial in the city of David, the ancestral honor — though 2 Chronicles 24:25 records that he was not placed in the royal tombs themselves. His son Amaziah succeeded him, and the Davidic dynasty continued despite everything."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2kings')
        merge_tier(existing, KINGS2, tier_key)
        save(tier_dir, '2kings', existing)
    print('2 Kings 7-12 written.')

if __name__ == '__main__':
    main()
