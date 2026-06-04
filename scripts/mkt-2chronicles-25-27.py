"""
MKT 2 Chronicles chapters 25–27 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2chronicles-25-27.py

Content:
- Ch 25: Amaziah's reign — scrupulous Mosaic obedience (v4), Edomite victory,
         dismissal of Israelite mercenaries, Edomite-god syncretism (v14), prophetic
         rebuke, fatal challenge to Joash king of Israel, military humiliation,
         temple treasury stripped, assassination at Lachish
- Ch 26: Uzziah's fifty-two-year reign — the covenant theorem in operation (v5),
         campaigns against Philistines, Arabians, Meunites; building and agricultural
         expansion; military organization; invention of siege engines; pride in strength
         leading to temple transgression (v16); leprosy in the forehead; exclusion for life;
         Isaiah named as historian of the reign (v22)
- Ch 27: Jotham's sixteen-year reign — faithfulness without entering the temple (v2);
         continued building; Ammonite victory and three-year tribute; covenant theorem
         summary (v6); clean burial; Ahaz succeeds

Translation decisions (carried forward from mkt-2chronicles-22-24.py):
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T. Consistent throughout OT scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H2617 (חֶסֶד): does not occur in these chapters.
- H7307 (רוּחַ): does not occur in these chapters.
- H1285 (בְּרִית): does not occur in these chapters.

New decisions for chs 25–27:
- 25:2 H8003 (shalem = whole/complete): "whole heart" in L/M; T surfaces the diagnostic
  significance of incomplete devotion as a category in Chronicles.
- 25:4: Deut 24:16 is cited explicitly. L/M render the quotation word-for-word; T draws
  out the contrast between this scrupulous Mosaic obedience and the Edomite-god worship
  of v14 — the same man capable of Torah precision becomes an idolater.
- 25:14: Amaziah's syncretism with Edomite gods is the central theological pivot of the
  chapter. T names the theological irony explicitly: these are the gods who just proved
  their worthlessness before his army.
- 25:20 divine governance: "it was of God" — same formula as 22:7. L: "for it came of
  God"; M: "for this was God's doing"; T surfaces the covenantal link between seeking
  false gods and losing the capacity to hear the true God's counsel.
- 26:5 covenant theorem: "as long as he sought the LORD, God made him prosper" — the
  governing theological sentence of the chapter. All three tiers preserve it; T identifies
  it as the Chronicler's explicit causal statement.
- 26:15 "engines invented by cunning men": earliest mention of mechanical siege technology
  in the OT. T notes this and connects "marvellously helped" as divine passive framing
  everything up to that point — and then the hinge phrase "until he grew strong."
- 26:16 H1361 (gabah = lifted up) / H7843 (mashchit = destruction/ruin): "pride to his
  destruction." T connects to Isa 6:1 (same verb gabah — "I saw the LORD, high and
  exalted") — the prophet who recorded Uzziah's reign (v22) used the same word for the
  LORD's exaltation that the Chronicler used for Uzziah's fatal pride.
- 26:22 Isaiah cited as source — the only place in Chronicles where Isaiah is named.
  T draws the connection to Isa 6:1 ("in the year of King Uzziah's death I saw the Lord").
- 27:2 "did not enter the temple" — Jotham's defining characteristic. L/M render it as
  stated; T reads it as the lesson drawn from Uzziah's fate, and notes the irony that
  personal faithfulness did not prevent national corruption.
- 27:6 H3559 (kun = ordered/prepared/established): "prepared his ways" — L: "prepared
  his ways"; M: "ordered his ways steadfastly"; T: the covenant theorem in its cleanest
  form, contrasted with Uzziah whose strength led to pride rather than deeper seeking.
- 27:9 Jotham's clean burial (no disqualifying note) vs. the qualified burials of Joash
  (outside royal tombs) and Uzziah (in burial field, not tombs). T notes the silence as
  the Chronicler's form of commendation.
- Aspect notes:
  - Ch 25: The narrative proceeds in waw-consecutive imperfects throughout. The pivotal
    theological statement at v20 ("it was of God") uses a perfect, marking it as an
    interpretive hinge exactly as at 22:7.
  - Ch 26: The covenant theorem at v5 uses a qal perfect (sought) and a hiphil perfect
    (prospered); the hinge "when he was strong" (v16) uses a qal infinitive construct.
  - Ch 27: The summary at v6 uses a qal imperfect + perfect sequence: "he became mighty
    (imperfect) because he prepared (perfect)."
- OT intertextuality:
  - 25:4: Deut 24:16 — the Mosaic law on individual accountability cited word-for-word.
  - 25:14: The irony echoes the broader OT indictment of idolatry in Pss 115, 135 —
    gods that cannot hear or speak or save cannot be trusted.
  - 25:20: The divine governance formula echoes 22:7 and anticipates the larger
    Chronicler theology of sin binding a person to its consequences.
  - 26:5: The covenant theorem of 15:2 ("seek him and he will be found") in its positive
    form; v16 begins its negative arc.
  - 26:22 / Isa 6:1: The year of Uzziah's death was the year of Isaiah's commissioning.
  - 27:6: The term "prepared his ways" echoes the Proverbs wisdom tradition (Prov 16:9)
    and anticipates the NT "prepare the way" language.
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

CHRONICLES2 = {
  "25": {
    "1": {
      "L": "Amaziah was twenty and five years old when he began to reign, and he reigned twenty and nine years in Jerusalem. And his mother's name was Jehoaddan of Jerusalem.",
      "M": "Amaziah was twenty-five years old when he became king, and he reigned twenty-nine years in Jerusalem. His mother's name was Jehoaddan of Jerusalem.",
      "T": "Amaziah — whose name means 'the LORD is strong' — inherited the throne at twenty-five after his father Joash was assassinated on his sickbed. He would reign nearly thirty years from Jerusalem. His mother was Jehoaddan, a Judean woman from the capital. The regnal formula is the Chronicler's opening frame; everything else he tells us about this king is an interpretation of what happens to a man whose name proclaims one thing about the LORD while his life demonstrates the distance between naming and being."
    },
    "2": {
      "L": "And he did that which was right in the sight of the LORD, but not with a perfect heart.",
      "M": "He did what was right in the sight of the LORD, but not with a fully devoted heart.",
      "T": "The commendation and its qualification arrive in the same sentence. He did what was right — there was genuine obedience, real acts of covenant faithfulness — but not with a whole heart. The Hebrew shalem (whole, complete, at peace) is the word for the completeness of shalom itself. A half-devoted heart is not a second-tier level of faithfulness in Chronicles; it is a diagnostic category. What is not whole will fracture. What is right without being wholehearted will serve the LORD in easy seasons and abandon him when the cost of faithfulness rises."
    },
    "3": {
      "L": "Now it came to pass, when the kingdom was established unto him, that he slew his servants that had killed the king his father.",
      "M": "Once his royal power was established, he put to death the servants who had murdered his father the king.",
      "T": "He waited. The assassins of Joash had lived under Amaziah's rule until his power was secure — a politically reasonable delay. Joash had been killed on his bed by his own servants (24:25-26), and his son inherited a throne that had been reached by conspiracy. Amaziah's first act of royal justice was to execute the conspirators. But before it becomes only a statement about retribution, the Chronicler stops to note how he did it — and what he refrained from doing."
    },
    "4": {
      "L": "But he slew not their children, but did as it is written in the law in the book of Moses, where the LORD commanded, saying, The fathers shall not die for the children, neither shall the children die for the fathers, but every man shall die for his own sin.",
      "M": "He did not put their children to death, but acted according to what is written in the Law, in the Book of Moses, where the LORD commanded: 'Fathers shall not die for their children, nor children for their fathers; each person shall die for their own sin.'",
      "T": "The Chronicler quotes Deuteronomy 24:16 explicitly. Amaziah acted within the limits the Torah set on vengeance: only the guilty, not their families. By ancient Near Eastern standards this was radical; family corporate liability was the norm. To kill only the conspirators and spare their children was a statement of covenantal particularity. The Chronicler places this example of Mosaic precision immediately before the narrative of the Edomite campaign — and immediately before Amaziah's decision to worship Edomite gods after his victory. The contrast is deliberate: the same man capable of scrupulous Torah observance becomes an idolater within a few verses. Principle obedience and wholehearted devotion are not the same thing."
    },
    "5": {
      "L": "Moreover Amaziah gathered Judah together, and made them captains over thousands, and captains over hundreds, according to the houses of their fathers, throughout all Judah and Benjamin: and he numbered them from twenty years old and above, and found them three hundred thousand choice men, able to go forth to war, that could handle spear and shield.",
      "M": "Amaziah mustered Judah and organized them by ancestral houses, appointing commanders of thousands and hundreds over all Judah and Benjamin. He counted all men twenty years and older and found three hundred thousand select troops able for military service, trained to use spear and shield.",
      "T": "A formal military census organized through the covenant structure of ancestral houses — this was Israel's people in arms, not a hired force. Three hundred thousand select troops: a serious and well-organized army. The organization by family units maintained the tribal-covenantal character of the force. But what Amaziah did next suggested he did not trust the three hundred thousand he already had."
    },
    "6": {
      "L": "He hired also an hundred thousand mighty men of valour out of Israel for an hundred talents of silver.",
      "M": "He also hired a hundred thousand soldiers of proven valor from Israel for a hundred talents of silver.",
      "T": "One hundred talents of silver — a massive outlay — to hire Israelite mercenaries. The northern kingdom, which had broken away from the Davidic covenant a century before, was no longer Israel in the way the covenant defined. To supplement Judah's army with troops from a kingdom the LORD had distanced himself from was to mix Judah's force with soldiers from under a different banner. The prophet's next words will make the problem explicit."
    },
    "7": {
      "L": "But there came a man of God to him, saying, O king, let not the army of Israel go with thee; for the LORD is not with Israel, to wit, with all the children of Ephraim.",
      "M": "But a man of God came to him and said, 'O king, do not let the army of Israel march with you, for the LORD is not with Israel — with any of the Ephraimites.'",
      "T": "The man of God arrives before the battle. This is the Chronicler's pattern: before major decisions, a prophetic voice comes. The word is precise and unsparing — the LORD is not with Israel. Not against Israel; simply absent. The northern kingdom's long drift from the covenant had brought it to the place where the LORD's presence could not be assumed. To march with Israel's troops was to enter battle with a divided force: Judah's army trusting the LORD, Israel's men representing a covenant connection that had been severed. The armies could not be aligned."
    },
    "8": {
      "L": "But if thou wilt go, do it, be strong for the battle: God shall make thee fall before the enemy: for God hath power to help, and to cast down.",
      "M": "But if you go through with this, however bravely you fight, God will make you fall before the enemy — for God has the power both to help and to overthrow.",
      "T": "The warning is not about tactics but about covenant logic. God has power to help and power to cast down — both belong to him equally. Military strength does not determine outcomes; divine presence or absence does. To march with Israel's troops despite the warning would be to invite the falling the man of God is trying to prevent. The conditional construction preserves Amaziah's freedom: 'if you go through with this' — he still has a choice."
    },
    "9": {
      "L": "And Amaziah said to the man of God, But what shall we do for the hundred talents which I have given to the army of Israel? And the man of God answered, The LORD is able to give thee much more than this.",
      "M": "Amaziah asked the man of God, 'But what about the hundred talents I already gave to the Israelite troops?' The man of God replied, 'The LORD is able to give you much more than this.'",
      "T": "The question reveals where Amaziah's attention is: not on the covenant implications but on the financial loss. A hundred talents already spent, already gone — this weighs against the prophet's word. The man of God's answer has the sound of a proverb: you are calculating what you might lose by obedience, but God's resources exceed any accounting. The hundred talents are not the real question. Whether Amaziah trusts the LORD enough to absorb a financial loss for covenant faithfulness — that is the real question."
    },
    "10": {
      "L": "Then Amaziah separated them, to wit the army that was come to him out of Ephraim, to go home again: and their anger was greatly kindled against Judah, and they returned home in great anger.",
      "M": "Amaziah then dismissed the Israelite force that had joined him and sent them home. They were furious with Judah and went home in great anger.",
      "T": "He obeyed the prophet's word and paid the financial cost. For this the Chronicler gives him credit; the dismissal was an act of covenant faithfulness even if loss-calculation was part of the motivation. But the dismissal created a problem Amaziah had not anticipated: an army of a hundred thousand armed men, sent home without the battle pay they had come for, in great anger. The Chronicler notes the anger twice, which signals that these dismissed Israelites will reappear. They do, in v13."
    },
    "11": {
      "L": "And Amaziah strengthened himself, and led forth his people, and went to the valley of salt, and smote of the children of Seir ten thousand.",
      "M": "Amaziah then took courage, led his own people to the Valley of Salt, and struck down ten thousand Edomites.",
      "T": "Without the Israelite mercenaries, Amaziah led his Judean force to the Valley of Salt — the arid depression south of the Dead Sea, traditional Judahite fighting ground (cf. 2 Sam 8:13). He won. Ten thousand Edomites fell. The victory was real and substantial, and it came with the LORD's help — the prophet had told him the LORD could give him far more than the lost hundred talents, and the victory at the Valley of Salt was the immediate proof. But the next verses will show what Amaziah did with his victory."
    },
    "12": {
      "L": "And other ten thousand left alive did the children of Judah carry away captive, and brought them unto the top of the rock, and cast them down from the top of the rock, that they all were broken in pieces.",
      "M": "The Judahites also captured ten thousand alive, brought them to the top of the rock, and threw them down so that they were all dashed to pieces.",
      "T": "Ten thousand prisoners of war, brought to a high rock and hurled off. The severity was not unusual by ancient standards, but the Chronicler records it plainly. What matters for his narrative is the sequence: Amaziah won a great victory over Edom, dealt ruthlessly with Edomite prisoners, and then — immediately, in the very next verse — came home carrying Edomite gods. The juxtaposition is the Chronicler's commentary."
    },
    "13": {
      "L": "But the soldiers of the army which Amaziah sent back, that they should not go with him to battle, fell upon the cities of Judah, from Samaria even unto Beth-horon, and smote three thousand of them, and took much spoil.",
      "M": "Meanwhile, the troops Amaziah had dismissed and refused to take into battle raided the cities of Judah from Samaria to Beth-horon, killing three thousand people and carrying off great plunder.",
      "T": "The consequence of v10 arrived. The dismissed Israelite troops — armed, angry, denied their expected battle pay — turned their swords on Judah. They raided from Samaria south through the Beth-horon corridor, killing three thousand Judahites and carrying off much plunder. Amaziah's obedience to the prophet had preserved him from the covenant problem of fighting with Israel's troops; it had not preserved him from the political consequence of provoking a hundred thousand armed men. Obedience is a guarantee of covenant alignment, not of comfort."
    },
    "14": {
      "L": "Now it came to pass, after that Amaziah was come from the slaughter of the Edomites, that he brought the gods of the children of Seir, and set them up to be his gods, and bowed down himself before them, and burned incense unto them.",
      "M": "After Amaziah returned from defeating the Edomites, he brought back the gods of the people of Seir, set them up as his own gods, bowed down before them, and burned incense to them.",
      "T": "The pivot of the entire chapter. Amaziah came home from a victory over Edom and carried the Edomites' gods with him — not as trophies but as objects of worship. He set them up, bowed before them, burned incense. The man who had cited Moses' law about individual accountability, who had scrupulously avoided punishing innocent children for their fathers' guilt, now prostrated himself before the gods of the people he had just conquered. These were the gods who had failed to protect Edom from Amaziah. Their worshipers had just been slaughtered by the ten thousand and thrown from rocks. And Amaziah worshiped them. This is what an unwhole heart looks like in practice: the disciplines of Torah followed from the outside while the inside reaches for whatever offers the next sensation of power or novelty."
    },
    "15": {
      "L": "Wherefore the anger of the LORD was kindled against Amaziah, and he sent unto him a prophet, which said unto him, Why hast thou sought after the gods of the people, which could not deliver their own people out of thine hand?",
      "M": "Therefore the anger of the LORD burned against Amaziah, and he sent a prophet to him who said: 'Why have you sought the gods of this people, who could not deliver their own people from your hand?'",
      "T": "The logic of the prophetic question is unanswerable. These gods could not save their own worshipers from Amaziah's army. They watched while ten thousand of their people were killed and ten thousand more thrown from a cliff. They have proved, conclusively and recently, that they cannot deliver. Why worship something that just demonstrated its own impotence at your expense? The anger of the LORD is not a theological abstraction here; it is the response of a God whose people, who have just experienced his help in battle, have immediately turned to worship the gods of the defeated."
    },
    "16": {
      "L": "And it came to pass, as he talked with him, that the king said unto him, Art thou made of the king's counsel? forbear; why shouldest thou be smitten? Then the prophet forbare, and said, I know that God hath determined to destroy thee, because thou hast done this, and hast not hearkened unto my counsel.",
      "M": "As the prophet was speaking, the king interrupted: 'Did we appoint you a royal adviser? Stop! Why get yourself struck down?' So the prophet stopped, but said first: 'I know that God has determined to destroy you, because you have done this and have not listened to my counsel.'",
      "T": "Amaziah does not answer the unanswerable question about gods that could not save their worshipers. He attacks the prophet's standing: who appointed you my counselor? The threat — 'why should you be struck down?' — is barely veiled. The prophet stops speaking but delivers one final word before he goes: God has already determined this. The verb 'determined' (ya'ats) is deliberate — it is the same word used in v17 when Amaziah 'took counsel' to challenge Joash. Having dismissed divine counsel, Amaziah immediately sought human counsel that would lead him to destruction. The prophet's last word was the truest thing spoken in the chapter."
    },
    "17": {
      "L": "Then Amaziah king of Judah took advice, and sent to Joash the son of Jehoahaz the son of Jehu, king of Israel, saying, Come, let us see one another in the face.",
      "M": "Amaziah king of Judah then consulted his advisers and sent a challenge to Joash son of Jehoahaz son of Jehu, king of Israel: 'Come, let us face each other in battle.'",
      "T": "Having silenced the prophet, Amaziah found different counsel — human counsel, political counsel, the kind that told him what he wanted to hear. He was emboldened by the Edomite victory and apparently intended to assert Judahite dominance over the northern kingdom as well. 'Let us see one another in the face' is the idiom for armed confrontation. The full genealogy of Joash is recorded, reminding the reader that Amaziah was challenging a man from the Jehu dynasty — the same dynasty whose founder had executed judgment on Ahab's house and, in the process, killed Amaziah's own grandfather Ahaziah (22:7-9). The prophet had warned about destruction; Amaziah was planning a war."
    },
    "18": {
      "L": "And Joash king of Israel sent to Amaziah king of Judah, saying, The thistle that was in Lebanon sent to the cedar that was in Lebanon, saying, Give thy daughter to my son to wife: and there passed by a wild beast that was in Lebanon, and trode down the thistle.",
      "M": "Joash king of Israel replied to Amaziah king of Judah: 'A thistle in Lebanon sent a message to a cedar in Lebanon: Give your daughter to my son as a wife. But a wild animal of Lebanon came along and trampled the thistle underfoot.'",
      "T": "Joash answered with a parable, and it is a devastating one. The thistle fancies itself the equal of the cedar and proposes a dynastic marriage; the wild beast does not negotiate or fight back — it simply passes by and treads the thistle underfoot. The application is unmistakable: Amaziah is the thistle. His Edomite victory, real as it was, was a victory over a minor regional power. To challenge Israel, which had been fighting major powers for a generation, was to mistake a small win for great-power status. The parable is also a mercy — Joash is giving Amaziah a clear reading of his situation before the battle makes the lesson more expensive."
    },
    "19": {
      "L": "Thou sayest, Lo, thou hast smitten the Edomites; and thine heart lifteth thee up to boast: abide now at home; why shouldest thou meddle to thine hurt, that thou shouldest fall, even thou, and Judah with thee?",
      "M": "You say, 'I have defeated Edom,' and your pride lifts you up. Stay home! Why stir up trouble that would only bring about your downfall — yours and Judah's with you?",
      "T": "Joash strips the challenge to its psychological core: your heart lifts you up. Pride at the Edomite victory has inflated Amaziah's self-assessment beyond what the victory warrants. Joash is not posturing — he is performing an act of strategic honesty that serves both their interests. Stay home, says the king of Israel, which is itself remarkable. But what Joash said, the man of God had already implied. Amaziah had now received the same warning from two sources and would not hear either one."
    },
    "20": {
      "L": "But Amaziah would not hear; for it came of God, that he might deliver them into the hand of their enemies, because they sought after the gods of Edom.",
      "M": "But Amaziah refused to listen, for this was God's doing — to hand them over to their enemies, because they had sought the gods of Edom.",
      "T": "The Chronicler draws back the curtain. Amaziah's stubbornness was not merely human folly; it was divinely governed, as at 22:7 when Ahaziah's downfall 'came about through God's design.' Amaziah had sought the gods of Edom; those gods had proved their worthlessness; and now the God he had offended would not prevent him from the consequences of his choice. When you commit to hearing one voice, you lose the capacity to hear another. The seeking of false gods and the refusal to hear the true God's counsel are covenantally linked: the one produces the other."
    },
    "21": {
      "L": "So Joash the king of Israel went up; and they saw one another in the face, both he and Amaziah king of Judah, at Beth-shemesh, which belongeth to Judah.",
      "M": "So Joash king of Israel marched out, and he and Amaziah king of Judah met in battle at Beth-shemesh, which belongs to Judah.",
      "T": "Beth-shemesh was in Judah itself — Joash had to cross into Judahite territory to reach the battleground. The battle Amaziah had sought came to him on his own soil. The phrase 'they saw one another in the face' echoes Amaziah's original challenge in v17 — come, let us see one another in the face. He got exactly what he had asked for."
    },
    "22": {
      "L": "And Judah was put to the worse before Israel, and they fled every man to his tent.",
      "M": "Judah was routed before Israel, and every man fled to his own home.",
      "T": "A total defeat. 'Every man to his tent' is the idiom for complete military dissolution — the army did not retreat in formation; it broke and ran, each soldier for himself. The force that Amaziah had organized by ancestral houses, numbered in hundreds of thousands, equipped and deployed — fled before the Israelite army. Joash's parable had been prophetically accurate: the wild beast of Lebanon had come by and trampled the thistle."
    },
    "23": {
      "L": "And Joash the king of Israel took Amaziah king of Judah, the son of Joash, the son of Jehoahaz, at Beth-shemesh, and brought him to Jerusalem, and brake down the wall of Jerusalem from the gate of Ephraim to the corner gate, four hundred cubits.",
      "M": "Joash king of Israel captured Amaziah king of Judah — son of Joash son of Jehoahaz — at Beth-shemesh, brought him to Jerusalem, and broke down the city wall from the Ephraim Gate to the Corner Gate, a stretch of four hundred cubits.",
      "T": "The captured king was brought to his own city as a prisoner, and his city's wall was broken in his sight. Four hundred cubits — roughly 600 feet of demolished fortification, enough to leave Jerusalem militarily vulnerable, enough to humiliate. The Chronicler gives the full genealogy of Amaziah again (son of Joash son of Jehoahaz), echoing Joash's genealogy in v17. Two kings sharing names, their fathers sharing names; now one stood in the ruins of the other's city as conqueror."
    },
    "24": {
      "L": "And he took all the gold and the silver, and all the vessels that were found in the house of God with Obed-edom, and the treasures of the king's house, the hostages also, and returned to Samaria.",
      "M": "He took all the gold and silver, all the vessels found in God's house in the custody of Obed-edom, and the treasures of the palace. He also took hostages and returned to Samaria.",
      "T": "The temple treasury stripped again — an echo of every previous foreign sack, every moment when Judah's covenant unfaithfulness resulted in the despoiling of the LORD's house. Obed-edom appears as the family responsible for the temple treasury — the same name as David's Levitical household that housed the ark (1 Chr 13:13-14) and whose family served the temple from David's time. What Joash's faithful years had restored and what Jehoiada had protected through Athaliah's reign was now stripped again by the fruit of Amaziah's idolatry."
    },
    "25": {
      "L": "And Amaziah the son of Joash king of Judah lived after the death of Joash son of Jehoahaz king of Israel fifteen years.",
      "M": "Amaziah son of Joash king of Judah outlived Joash son of Jehoahaz king of Israel by fifteen years.",
      "T": "Joash king of Israel died before Amaziah, and Amaziah lived fifteen more years in the shadow of his military humiliation. A king who had been captured, whose wall had been torn down, whose temple had been stripped, who had been returned to his throne as a demonstration of Israelite dominance — then reigned another decade and a half. The length of his post-defeat reign is the Chronicler's quiet signal that the mercy of the LORD persisted even toward a king who had worshiped Edomite gods."
    },
    "26": {
      "L": "Now the rest of the acts of Amaziah, first and last, behold, are they not written in the book of the kings of Judah and Israel?",
      "M": "The rest of the acts of Amaziah, from first to last, are recorded in the Book of the Kings of Judah and Israel.",
      "T": "First and last, written in the royal annals. The Chronicler has not told everything; what he has told is the theological skeleton — the half-hearted beginning, the Mosaic obedience, the Edomite victory and its double consequence, the idolatry, the prophetic warning silenced, the fatal challenge to Israel. The full record exists elsewhere; what the Chronicler has selected reveals the shape of a character: capable of obedience, incapable of wholeness."
    },
    "27": {
      "L": "Now after the time that Amaziah did turn away from following the LORD they made a conspiracy against him in Jerusalem; and he fled to Lachish: but they sent to Lachish after him, and slew him there.",
      "M": "From the time Amaziah turned away from following the LORD, a conspiracy formed against him in Jerusalem. He fled to Lachish, but they sent men there after him and killed him.",
      "T": "The conspiracy is explicitly tied to Amaziah's turning from the LORD — 'after the time' makes the causal sequence clear. He turned from following the LORD; therefore the conspiracy formed. As with Joash in chapter 24, the killing was carried out not by a foreign army but by subjects — the covenant people withdrawing their loyalty from a king who had broken covenant. He fled to Lachish, the fortress city in the Shephelah, but the conspirators pursued him there. Distance from Jerusalem was no protection; the sentence found him."
    },
    "28": {
      "L": "And they brought him upon horses, and buried him with his fathers in the city of Judah.",
      "M": "He was carried back on horses and buried with his ancestors in the city of Judah.",
      "T": "Brought home on horses — a dead man's transport. Buried with his ancestors in the city of Judah: neither completely dishonored like Joash who was denied the royal tombs, nor fully honored like the great covenant kings. He was returned to the royal burial ground because his family line warranted it. The half-hearted king received a half-annotated burial. The Chronicler closes the account without flourish, which is itself the verdict."
    }
  },
  "26": {
    "1": {
      "L": "Then all the people of Judah took Uzziah, who was sixteen years old, and made him king in the room of his father Amaziah.",
      "M": "All the people of Judah took Uzziah, who was sixteen years old, and made him king in place of his father Amaziah.",
      "T": "After Amaziah's assassination, the people — not the court, not the army, but the people of Judah — chose the successor. They crowned Uzziah at sixteen. In Chronicles, kings who receive popular acclamation tend to be those around whom the covenant people rally. Uzziah — whose name means 'the LORD is my strength' — succeeded a father whose name also proclaimed the LORD's strength but whose reign demonstrated the distance between the name and the life."
    },
    "2": {
      "L": "He built Eloth, and restored it to Judah, after that the king slept with his fathers.",
      "M": "He built Eloth and restored it to Judah after the king had rested with his ancestors.",
      "T": "One of his first acts was to rebuild Eloth — the port city on the Red Sea's Gulf of Aqaba, briefly a Judean possession under Solomon and lost in subsequent generations. To restore Eloth was to push Judah's reach back toward its Solomonic boundaries. The Chronicler notes it early because it signals the character of the reign: a king who expands and restores, who recovers what was lost, who governs with the golden age as his reference point."
    },
    "3": {
      "L": "Sixteen years old was Uzziah when he began to reign, and he reigned fifty and two years in Jerusalem. His mother's name also was Jecoliah of Jerusalem.",
      "M": "Uzziah was sixteen years old when he became king, and he reigned fifty-two years in Jerusalem. His mother's name was Jecoliah of Jerusalem.",
      "T": "Fifty-two years — one of the longest reigns in Judah's history, rivaled only by Manasseh's fifty-five. His mother Jecoliah was from Jerusalem itself: a capital-city woman, formed in the orbit of the temple, the Davidic house, the covenant traditions. The regnal formula measures what is about to be told: a reign of extraordinary length whose latter portion was defined by leprosy and exclusion, a life that had everything and forfeited the most important thing."
    },
    "4": {
      "L": "And he did that which was right in the sight of the LORD, according to all that his father Amaziah did.",
      "M": "He did what was right in the sight of the LORD, just as his father Amaziah had done.",
      "T": "The commendation uses Amaziah as the benchmark — which is a carefully calibrated praise. Amaziah did right but not with a whole heart (25:2). Uzziah began in the same mode: externally faithful, genuinely obedient, but the qualification of wholeness held in reserve. The next verse will show what distinguished Uzziah's faithful years from Amaziah's: a mentor who provided understanding in the visions of God, and the covenant theorem operating in its clearest form."
    },
    "5": {
      "L": "And he sought God in the days of Zechariah, who had understanding in the visions of God: and as long as he sought the LORD, God made him to prosper.",
      "M": "He sought God during the days of Zechariah, who instructed him in the fear of God. And as long as he sought the LORD, God gave him success.",
      "T": "The theological axis of Uzziah's reign is stated in one sentence: as long as he sought the LORD, God made him to prosper. The causal connection is absolute and the conditionality explicit. Zechariah — not the later prophet Zechariah but an instructor in the court — 'had understanding in the visions of God': prophetic wisdom gave Uzziah access to the mind of the LORD for his decisions. Like Joash guided by Jehoiada, Uzziah's faithfulness was partly anchored in a mentor relationship. The crucial difference is what happened not after the mentor died but after Uzziah grew strong."
    },
    "6": {
      "L": "And he went forth and warred against the Philistines, and brake down the wall of Gath, and the wall of Jabneh, and the wall of Ashdod, and built cities about Ashdod, and among the Philistines.",
      "M": "He went out to war against the Philistines and broke down the walls of Gath, Jabneh, and Ashdod. He also built cities near Ashdod and throughout Philistine territory.",
      "T": "The Philistine coast — the corridor that Israel had never fully controlled since the judges period — fell to Uzziah's campaigns. Three major Philistine cities: Gath, Jabneh, Ashdod. Their walls came down. Judean settlements were planted in formerly Philistine territory. This was the territorial scope of David and Solomon; Uzziah was reaching toward the golden age's boundaries. The military success was the immediate expression of the covenant theorem: as long as he sought the LORD, God made him to prosper — and this is what prosperity looked like."
    },
    "7": {
      "L": "And God helped him against the Philistines, and against the Arabians that dwelt in Gur-baal, and the Mehunims.",
      "M": "God helped him against the Philistines, against the Arabians living in Gur-baal, and against the Meunites.",
      "T": "The Chronicler attributes every victory to God's direct help — not to Uzziah's tactics, numbers, or skill. The Arabians at Gur-baal and the Meunites, who had been a southern threat in Jehoshaphat's time (20:1), both gave way. Multiple fronts, multiple peoples — all yielded. The breadth of the victories underlines that this was divine assistance, not human excellence."
    },
    "8": {
      "L": "And the Ammonites gave gifts to Uzziah: and his name spread abroad even to the entering in of Egypt; for he strengthened himself exceedingly.",
      "M": "The Ammonites brought tribute to Uzziah, and his fame spread as far as the entrance of Egypt, for he grew exceedingly powerful.",
      "T": "From the coast westward to the Egyptian border, from the east where the Ammonites paid tribute — Uzziah's sphere of influence had become Solomonic in extent. 'To the entering of Egypt' echoes 1 Kings 8:65, the description of Solomon's kingdom at its greatest reach. The Chronicler is describing a reign that recaptured something of the golden age, making explicit that this was what seeking the LORD looked like in practice: a king whose fame and power matched the scope of his faithfulness."
    },
    "9": {
      "L": "Moreover Uzziah built towers in Jerusalem at the corner gate, and at the valley gate, and at the turning of the wall, and fortified them.",
      "M": "Uzziah also built towers in Jerusalem — at the Corner Gate, the Valley Gate, and the angle of the wall — and fortified them.",
      "T": "The military infrastructure of Jerusalem itself was strengthened. The Corner Gate was the vulnerable northwest angle; the Valley Gate opened to the Hinnom Valley; the angle of the wall was another exposed point. Uzziah reinforced all three. The same man who broke down the walls of Philistine cities was building up the walls of his own — shaping the landscape of war in both directions simultaneously."
    },
    "10": {
      "L": "Also he built towers in the desert, and digged many wells: for he had much cattle, both in the low country, and in the plains: husbandmen also, and vine dressers in the mountains, and in Carmel: for he loved husbandry.",
      "M": "He also built towers in the wilderness and dug many wells, for he had large herds in the lowlands and on the plains. He had farmers and vinedressers in the hill country and in Carmel, for he loved the soil.",
      "T": "A king who loved the soil: this detail is remarkable in a royal biography. Uzziah's prosperity extended from the military to the agricultural — towers in the desert to protect the herds, wells where there was no water, vineyards in the highlands, crops in the lowlands. The covenant promise of Deuteronomy was agricultural before it was military (Deut 28:11-12); the fruitfulness of the land was both practical wealth and theological confirmation. Wells dug in the desert: every well was a statement that the LORD's provision reached even into the dry places."
    },
    "11": {
      "L": "Moreover Uzziah had a host of fighting men, that went out to war by bands, according to the number of their account by the hand of Jeiel the scribe and Maaseiah the ruler, under the hand of Hananiah, one of the king's captains.",
      "M": "Uzziah maintained an army of fighting men organized in battle units, counted by the records of Jeiel the secretary and Maaseiah the officer, under the authority of Hananiah, one of the king's commanders.",
      "T": "The military organization was formal and accountable: named officers, written records, a clear chain of command with Hananiah at its head. This was not a feudal levy raised in crisis but a standing professional force with administrative infrastructure. The scribe keeping records and the officer maintaining rolls: the army was governed by the same dual-accountability model that Joash had applied to the temple repair fund. Uzziah's administration was orderly because an ordered kingdom tended to be what covenant faithfulness produced."
    },
    "12": {
      "L": "The whole number of the chief of the fathers of the mighty men of valour were two thousand and six hundred.",
      "M": "The total number of clan leaders commanding these valiant troops was two thousand six hundred.",
      "T": "Twenty-six hundred commanders — officers of the ancestral units, the men responsible for the fighting formations beneath them. This was the officer corps, not the total army. The full fighting strength follows in the next verse."
    },
    "13": {
      "L": "And under their hand was an army, three hundred thousand and seven thousand and five hundred, that made war with mighty power, to help the king against the enemy.",
      "M": "Under these commanders was an army of three hundred and seven thousand five hundred, a force of great power to support the king against any enemy.",
      "T": "307,500 soldiers — a force nearly matching the three hundred thousand Amaziah had mustered (25:5), the Chronicler showing continuity in military strength across reigns even as the quality of those reigns differed. The force existed 'to help the king against the enemy': the military organization served the king's covenantal role as protector of the covenant people. As long as the king sought the LORD, the army he commanded was itself an extension of divine provision."
    },
    "14": {
      "L": "And Uzziah prepared for them throughout all the host shields, and spears, and helmets, and habergeons, and bows, and slings to cast stones.",
      "M": "Uzziah equipped the entire army with shields, spears, helmets, body armor, bows, and slings for throwing stones.",
      "T": "The king personally equipped the army: every branch of the force, every form of combat — close-range with spear and shield, protected in formation with helmet and armor, ranged with bow and sling. The care in equipping the troops was part of the same covenantal responsibility that had organized their command structure."
    },
    "15": {
      "L": "And he made in Jerusalem engines, invented by cunning men, to be on the towers and upon the bulwarks, to shoot arrows and great stones withal. And his name spread far abroad; for he was marvellously helped, till he was strong.",
      "M": "In Jerusalem he designed devices — invented by skilled craftsmen — to be mounted on the towers and corners of the wall to shoot arrows and hurl large stones. His fame spread far and wide, for he was wondrously helped until he grew strong.",
      "T": "The engines: specially designed mechanical devices, ballista-like weapons mounted on towers and bulwarks. This is the earliest mention of mechanical siege technology in the Old Testament, and the Chronicler notes with pride that they were invented — products of human ingenuity channeled into the service of Jerusalem's defense. 'Wondrously helped' — the divine passive frames all of this achievement as the work of God in and through a seeking king. Then the sentence ends: until he grew strong. That phrase is the hinge of the chapter. Strength and the seeking of God had walked together; now strength and pride would walk together, and the path would diverge."
    },
    "16": {
      "L": "But when he was strong, his heart was lifted up to his destruction: for he transgressed against the LORD his God, and went into the temple of the LORD to burn incense upon the altar of incense.",
      "M": "But when he became powerful, his heart grew proud to his own ruin. He was unfaithful to the LORD his God and entered the temple of the LORD to burn incense on the incense altar.",
      "T": "The precise moment of transition: when he was strong. The prosperity that had come from seeking the LORD produced strength; the strength, once achieved, produced pride rather than deeper seeking. His heart was lifted up — the verb gabah, the same word Isaiah would later use for the LORD's own exaltation in his call vision (Isa 6:1: 'I saw the Lord, high and lifted up') — but where the LORD's being lifted up is glory, the king's being lifted up is ruin. To his destruction: the Hebrew says 'for corruption' — the word labbeshacho marks the pride as already defined by its end point before it reaches its expression. Uzziah walked into the temple to burn incense: not a sincere act of worship gone wrong, but the conflation of royal power with priestly prerogative. He could do everything else in the kingdom; he wanted to do this too."
    },
    "17": {
      "L": "And Azariah the priest went in after him, and with him fourscore priests of the LORD, that were valiant men:",
      "M": "The priest Azariah went in after him, along with eighty priests of the LORD — courageous men.",
      "T": "Eighty priests followed Azariah to confront the king. That number is significant: this was not one brave priest risking himself; it was a formal corporate resistance by the priestly body. The Chronicler calls them 'valiant men' — the same word used for the fighting soldiers elsewhere. The priests' willingness to confront a powerful king in his pride was itself an act of covenant courage."
    },
    "18": {
      "L": "And they withstood Uzziah the king, and said unto him, It appertaineth not unto thee, Uzziah, to burn incense unto the LORD, but to the priests the sons of Aaron, that are consecrated to burn incense: go out of the sanctuary; for thou hast trespassed; neither shall it be for thine honour from the LORD God.",
      "M": "They confronted King Uzziah and said: 'It is not for you, Uzziah, to burn incense to the LORD — that belongs to the priests, the sons of Aaron, who are consecrated to burn incense. Leave the sanctuary, for you have transgressed. It will not bring you honor from the LORD God.'",
      "T": "The confrontation names the violation precisely: not you, Uzziah — this role belongs to the consecrated priests of Aaron. The distinction between royal and priestly roles was not ceremonial pedantry; it was the covenant's structural protection against the royal-priestly fusion that characterized the pagan cultures around Israel, where the king was also the high priest and sacred power was concentrated in one person. Israel's covenant deliberately separated crown and altar. Uzziah had wielded the scepter brilliantly; he was not authorized to hold the censer. 'It will not bring you honor from the LORD God' — the very thing his pride was seeking, honor and greatness, was the thing that would be denied him by this very act."
    },
    "19": {
      "L": "Then Uzziah was wroth, and had a censer in his hand to burn incense: and while he was wroth with the priests, the leprosy even rose up in his forehead before the priests in the house of the LORD, from beside the incense altar.",
      "M": "Uzziah, holding a censer in his hand, became furious. While he was raging at the priests, leprosy broke out on his forehead right there in the LORD's house, beside the incense altar.",
      "T": "The leprosy broke out in the moment of his fury, before he had acted further — in the house of God, beside the altar he had come to use. He was still holding the censer; his rage was still in his face; the priests were still before him. And suddenly his forehead was marked with the lesions that excluded a man from the community of the LORD's worshipers. The king who had wanted to burn incense in the temple would never enter the temple again. The judgment was perfectly proportioned to the transgression: the man who presumed to enter the holy place was driven permanently from it."
    },
    "20": {
      "L": "And Azariah the chief priest, and all the priests, looked upon him, and, behold, he was leprous in his forehead, and they thrust him out from thence; yea, himself hasted also to go out, because the LORD had smitten him.",
      "M": "Azariah the chief priest and all the priests looked at him — there was the leprosy on his forehead. They hurried to remove him, and he himself rushed out, for the LORD had struck him.",
      "T": "The double urgency: the priests thrusting him out, and Uzziah himself rushing to leave. Both knew in the same instant what had happened — the LORD had struck him. The man of immense military and political power, who had forced his way into the temple in angry pride, could not get out fast enough. The censer was dropped; the fury was gone; what remained was a man with leprosy on his forehead fleeing the house of God that his presumption had profaned."
    },
    "21": {
      "L": "And Uzziah the king was a leper unto the day of his death, and dwelt in a several house, being a leper; for he was cut off from the house of the LORD: and Jotham his son was over the king's house, judging the people of the land.",
      "M": "Uzziah the king remained a leper until his death, living in a separate house, for he was excluded from the LORD's house. His son Jotham was in charge of the royal household, governing the people of the land.",
      "T": "For the remainder of his life — however many years remained of his fifty-two-year reign — Uzziah lived in isolation: separate from the palace, separate from court, and above all cut off from the house of the LORD. The man who had forced his way into the temple to perform priestly duties was excluded from the temple for the rest of his days, unable to enter even as a worshiper, unable to perform the most basic acts of covenant piety. His son Jotham governed in his place. Uzziah was alive but functionally kingless: present in body, absent from the functions that made kingship meaningful. This is what pride to the point of presumption cost — not immediate death, but slow decades of exclusion."
    },
    "22": {
      "L": "Now the rest of the acts of Uzziah, first and last, did Isaiah the prophet, the son of Amoz, write.",
      "M": "The rest of Uzziah's acts, from first to last, were recorded by the prophet Isaiah son of Amoz.",
      "T": "Isaiah — the great eighth-century prophet whose book opens with his call in the year of Uzziah's death (Isa 6:1) — is named here as the historian of Uzziah's reign. This is the only place in Chronicles where Isaiah is cited as a source. The prophet who would write the greatest of the OT's messianic passages was formed as a prophet in the reign of the king whose leprosy ended the golden age. Isaiah's inaugural vision is set explicitly in the year Uzziah died: 'I saw the Lord, high and lifted up' — using the same verb (gabah) the Chronicler uses for Uzziah's lifted-up heart (v16). The contrast is complete: the king who lifted himself up in the temple saw leprosy; the prophet who saw the LORD lifted up in the temple was cleansed and commissioned."
    },
    "23": {
      "L": "So Uzziah slept with his fathers, and they buried him with his fathers in the field of the burial which belonged to the kings; for they said, He is a leper: and Jotham his son reigned in his stead.",
      "M": "Uzziah rested with his ancestors, and they buried him near his ancestors in the burial field belonging to the kings — for they said, 'He is a leper.' His son Jotham became king in his place.",
      "T": "Near the royal tombs, but not in them — the same semi-honored burial given to Joash, who was denied the royal sepulchres for a different covenant failure. Uzziah was buried in the field belonging to the kings, presumably in a separate plot, because his leprosy disqualified him from the main burial chambers. 'He is a leper' — the reason recorded by the Chronicler. After fifty-two years, after campaigns from Philistia to the Egyptian border, after rebuilding Jerusalem's defenses and digging wells in the desert and filling the treasury and equipping the army — the word people said about him was 'he is a leper.' The pride that undid him had become his permanent identification."
    }
  },
  "27": {
    "1": {
      "L": "Jotham was twenty and five years old when he began to reign, and he reigned sixteen years in Jerusalem. His mother's name also was Jerushah, the daughter of Zadok.",
      "M": "Jotham was twenty-five years old when he became king, and he reigned sixteen years in Jerusalem. His mother's name was Jerushah daughter of Zadok.",
      "T": "Jotham — whose name means 'the LORD is perfect' — began his public reign at twenty-five, though he had already been governing in Uzziah's place through the leprosy years. His mother Jerushah was the daughter of Zadok: a priestly family name, connecting the king's mother to the high-priestly line. The son of a leprous king and a woman from the Zadokite family, Jotham had grown up watching both the height of Uzziah's achievement and its collapse into exclusion. His reign would be shaped by what he had observed."
    },
    "2": {
      "L": "And he did that which was right in the sight of the LORD, according to all that his father Uzziah did: howbeit he entered not into the temple of the LORD. And the people did yet corruptly.",
      "M": "He did what was right in the sight of the LORD, just as his father Uzziah had done — except that he did not enter the temple of the LORD. But the people continued to act corruptly.",
      "T": "The defining qualification of Jotham's reign is negative: he did not enter the temple. He had seen his father's leprosy break out in the holy place; he drew the right lesson from it and maintained the boundary his father had violated. He remained within the covenant role assigned to kings, exercising royal authority without grasping at priestly prerogative. But the Chronicler adds a note that cuts the other way: the people continued to act corruptly. Jotham's personal faithfulness did not transform the nation. Covenant faithfulness concentrated in the king without penetrating the people produces a righteous ruler living over a corrupted nation. The covenant always required more than royal obedience alone."
    },
    "3": {
      "L": "He built the high gate of the house of the LORD, and on the wall of Ophel he built much.",
      "M": "He built the Upper Gate of the LORD's house and did extensive work on the wall of Ophel.",
      "T": "Jotham built. His father had built towers, walls, and fortifications; Jotham continued the building program, focusing on the temple's northern gate and the Ophel ridge south of the temple mount. The Upper Gate of the LORD's house was the main northern entrance to the temple complex — the gate through which Uzziah had been expelled in disgrace. To build the very gate that had excluded his father was itself a statement: Jotham honored the temple he would not presume to enter."
    },
    "4": {
      "L": "Moreover he built cities in the mountains of Judah, and in the forests he built castles and towers.",
      "M": "He also built towns in the hill country of Judah and constructed fortresses and towers in the forests.",
      "T": "The building program extended from the capital to the highlands: fortified towns in the mountains, military installations in the forest regions. Jotham secured the interior of the kingdom as well as the capital and the borders. The forests that had been dangerous terrain — places where enemies could mass unseen — were being converted into strategic assets."
    },
    "5": {
      "L": "He fought also with the king of the Ammonites, and prevailed against them. And the children of Ammon gave him the same year an hundred talents of silver, and ten thousand measures of wheat, and ten thousand of barley. So much did the children of Ammon pay unto him, both the second year, and the third.",
      "M": "He also fought against the king of the Ammonites and defeated them. The Ammonites paid him that year one hundred talents of silver, ten thousand cors of wheat, and ten thousand cors of barley — and the same amount in the second and third years as well.",
      "T": "The Ammonite tribute is measured precisely: one hundred talents of silver, ten thousand cors of wheat, ten thousand cors of barley — and this for three consecutive years. The specificity of the Chronicler's accounting is characteristic: when a king's prosperity is real, the numbers are given in detail, because the numbers are the evidence of the covenant theorem in action. Jotham prepared his ways before the LORD (v6), and the LORD gave him Ammonite tribute for three years running. The agricultural quantities and the military tribute belong to the same category: the visible fruitfulness of a king who seeks the LORD."
    },
    "6": {
      "L": "So Jotham became mighty, because he prepared his ways before the LORD his God.",
      "M": "Jotham grew powerful because he ordered his ways steadfastly before the LORD his God.",
      "T": "The theological summary of the reign in one sentence: he became mighty because he ordered his ways before the LORD his God. This is the covenant theorem in its purest form — seeking produces success; ordering your life before the LORD produces the kind of strength that lasts. The verb kun (prepared/ordered/established) carries the idea of setting something firmly in place, making it stable and oriented. Jotham did not merely seek God occasionally; he directed the whole pattern of his living toward the LORD. The result was might — military, political, agricultural — measurable and named. Unlike Uzziah, whose might became the occasion for pride, Jotham's might remained tethered to its source."
    },
    "7": {
      "L": "Now the rest of the acts of Jotham, and all his wars, and his ways, lo, they are written in the book of the kings of Israel and Judah.",
      "M": "The rest of Jotham's acts, including all his wars and his ways, are recorded in the Book of the Kings of Israel and Judah.",
      "T": "Acts, wars, ways: the three categories the Chronicler uses to summarize a king's record. Acts (events, achievements), wars (the military record), ways (the moral and spiritual pattern of a life). All three are written in the royal annals. The Chronicler has selected from those annals the theological skeleton: the right-doing, the refusal to enter the temple, the building and the victory, the people's continuing corruption. The ways of Jotham are preserved in the fuller record; what we have is the essential form of a life that ordered itself before God."
    },
    "8": {
      "L": "He was five and twenty years old when he began to reign, and reigned sixteen years in Jerusalem.",
      "M": "He was twenty-five years old when he became king and reigned sixteen years in Jerusalem.",
      "T": "The accession age and reign length repeated — the standard closing formula for a Judean king. Sixteen years: short relative to his father's fifty-two, but a coherent and honored reign. The repetition of the regnal statistics at the chapter's close gives the sense of a record properly closed, a life properly catalogued."
    },
    "9": {
      "L": "And Jotham slept with his fathers, and they buried him in the city of David: and Ahaz his son reigned in his stead.",
      "M": "Jotham rested with his ancestors and was buried in the city of David. His son Ahaz became king in his place.",
      "T": "Buried in the city of David — without qualification. Not 'buried near his ancestors in the burial field' like Uzziah, not 'buried in the city of David but not in the royal tombs' like Joash. Jotham was buried in the city of his ancestor David, clean and unqualified, which in Chronicles is its own form of commendation. The Chronicler's silence about dishonorable burial details speaks clearly. Ahaz succeeded him: and Ahaz, as the reader of Chronicles knows, would be one of the worst kings in Judah's history. The faithfulness of a father does not guarantee the faithfulness of a son. Jotham's life ordered before the LORD ended with a son who would not order his life before the LORD at all."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2chronicles')
        merge_tier(existing, CHRONICLES2, tier_key)
        save(tier_dir, '2chronicles', existing)
    print('2 Chronicles 25–27 written.')

if __name__ == '__main__':
    main()
