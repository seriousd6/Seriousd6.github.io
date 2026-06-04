"""
MKT 2 Chronicles chapters 19–21 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2chronicles-19-21.py

Content:
- Ch 19: Jehu son of Hanani rebukes Jehoshaphat for allying with Ahab; Jehoshaphat's judicial reform
         — appointment of judges across Judah and a supreme court in Jerusalem
- Ch 20: Moab, Ammon, and Meunites invade; Jehoshaphat's great prayer; Jahaziel's prophecy;
         the singing army; God sets ambush and enemies destroy each other; Valley of Berachah;
         Jehoshaphat's reign summary; ill-fated Tarshish alliance with Ahaziah
- Ch 21: Jehoram's reign — murders brothers, marries Ahab's daughter, walks in Ahab's ways;
         Edom and Libnah revolt; Elijah's letter of judgment; Philistine-Arabian raid; bowel
         disease; ignominious death and burial

Translation decisions (carrying forward from mkt-2chronicles-13-18.py):
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T. Consistent throughout OT scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H2617 (חֶסֶד): "steadfast love" in L/M; "covenant loyalty" in T.
  At 20:21 the refrain is "for his steadfast love endures forever" — the Psalm 136 / Hallel refrain.
  L/M preserve "steadfast love"; T expands to "his covenant loyalty never ends."
- H1285 (בְּרִית): "covenant" throughout. At 21:7 the Davidic covenant is the theological anchor
  that prevents Jehoram's line from being cut off — "lamp" language (H5216, nir) signals dynastic
  continuation; T explains the lamp-as-dynasty image explicitly.
- H7307 (רוּחַ): "Spirit" (capitalized) at 20:14 where the divine Spirit falls on Jahaziel.
  Prophetic agency, not wind. Consistent with prior 2 Chronicles scripts (15:1, Azariah).
- H8172 (שָׁעַן, rely/lean): Jehoshaphat's prayer in 20:12 — "our eyes are on you" — is the
  posture of total reliance, the same theological stance the Chronicler calls shaan elsewhere.
  T surfaces this explicitly as the contrast with Asa in ch. 16.

New decisions for chs 19–21:
- H539 (אָמַן, believe/trust) at 20:20: "Believe in the LORD your God and you will be established;
  believe his prophets, and you will succeed." The verb hiphil form הַאֲמִינוּ is the same root as
  Isaiah 7:9 ("if you are not firm in faith / im lo ta'aminu, ki lo te'amenu"). The Chronicler
  is echoing Isaiah's word to Ahaz deliberately. Jehoshaphat shows the faith Ahaz refused.
  L: "Believe in the LORD"; M: "Trust in the LORD"; T: names the Isaiah echo explicitly.
- 20:21 "his steadfast love endures forever" (H2617 + H5769 le'olam): the refrain of Psalm 136,
  the Great Hallel. The army's march into battle singing this refrain makes it the most theologically
  rich battle scene in Chronicles. T preserves the liturgical force of the phrase.
- 20:17 "stand firm, hold your position, and see the salvation of the LORD" echoes Exodus 14:13
  (Moses at the Red Sea: "stand firm and see the salvation of the LORD"). Jehoshaphat's battle
  is another Exodus. T notes the echo.
- H5216 (נִיר, nir, "lamp") at 21:7: the promise to give David a "lamp" — a successor, a dynastic
  heir. Same image as 1 Kgs 11:36, 15:4; 2 Kgs 8:19. The lamp is not physical light but the
  continuing flame of the dynasty. T makes the metaphor explicit.
- 21:7 H14 (abah, "was willing") negative: "the LORD was not willing to destroy" — divine
  restraint in the face of human wickedness, grounded in covenant not merit. T names this.
- 21:12 Elijah's letter: unique to Chronicles; absent from 2 Kings 8. The letter arrives posthumously
  if chronology is aligned (Elijah was already translated before Jehoram's full eight years).
  The Chronicler may be using a previously uncited prophetic collection, or anachronistic citation
  of the greatest northern prophet as witness against the worst southern king. T notes the anomaly.
- 21:19 "no fire in his honor": the royal cremation of aromatics was a mark of honor (cf. 16:14,
  Asa's great fire). Jehoram was denied it. The absence is the verdict.
- Aspect notes:
  - Ch 19: Jehoshaphat's judicial speeches use imperative and cohortative — commands to judges
    about how to exercise their office. L preserves the imperatival force; T surfaces the
    covenant-court theology behind each instruction.
  - Ch 20: The prayer (vv. 6-12) moves from hymnic praise (v. 6) to historical recital (vv. 7-9)
    to specific petition (vv. 10-12). L preserves the rhetorical structure; M reads as flowing
    prayer; T connects each movement to its theological logic.
  - Ch 20: "they began to sing and praise" (v. 22) — the Hebrew perfect (waw-consecutive) marks
    the exact moment God acted: as they began. The singing is the act of faith that triggers
    the divine intervention.
  - Ch 21: waw-consecutive narrative past throughout — the chronicle of a reign moving steadily
    toward judgment. T gives the narrative a retrospective weight the bare events lack.
- OT intertextuality:
  - 19:6-7: Jehoshaphat's charge to judges echoes Deut 1:16-17 (Moses's instructions to judges)
    and Deut 16:18-20. The judicial reform is a return to Mosaic covenant structure.
  - 19:9 "fear of the LORD, faithfulness, whole heart" — the triad of covenant loyalty that
    runs from Deut 6:4-5 through Joshua's farewell to David's charge to Solomon (1 Chr 28:9).
  - 20:6-12: Jehoshaphat's prayer is a masterwork of covenant theology. "In your hand are power
    and might, so that none is able to withstand you" (v. 6) echoes 1 Chr 29:12 (David's prayer).
    The reference to Abraham "your friend" (v. 7) echoes Isa 41:8. The temple-as-prayer-house
    (vv. 8-9) echoes Solomon's dedication prayer (2 Chr 6:28-30). T surfaces each echo.
  - 20:17 echoes Exod 14:13 ("stand firm, see the salvation of the LORD") and also Moses's song
    (Exod 15). The Exodus pattern: God fights, Israel watches, God saves.
  - 20:20 echoes Isa 7:9 (the Ahaz episode, same root): the faith of Jehoshaphat sets against
    the unbelief of Ahaz the king who was also offered a sign and refused it.
  - 20:21 "his steadfast love endures forever" — Psalm 136 refrain, sung 26 times in that psalm.
    Sung here in battle, it recapitulates Israel's entire history of redemption.
  - 21:7 "lamp" echoes 1 Kgs 11:36, 15:4; 2 Kgs 8:19 — the dynasty promise to David as a lamp
    in Jerusalem. The same image reappears in Psalm 132:17 ("I have prepared a lamp for my anointed").
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
  "19": {
    "1": {
      "L": "And Jehoshaphat king of Judah returned to his house in Jerusalem in peace.",
      "M": "Jehoshaphat king of Judah returned safely to his palace in Jerusalem.",
      "T": "He came home — which was more than Ahab did. The battle of Ramoth-gilead had killed the king of Israel; the king of Judah rode home alive. The Chronicler noted it without comment, though the contrast was not lost on anyone who had heard Micaiah's prophecy."
    },
    "2": {
      "L": "And Jehu the son of Hanani the seer went out to meet him and said to King Jehoshaphat, 'Should you help the wicked and love those who hate the LORD? Because of this, wrath has come upon you from before the LORD.'",
      "M": "Jehu son of Hanani the seer went out to meet him and said to King Jehoshaphat: 'Is it right for you to help the wicked and love those who hate the LORD? Because of this, the wrath of the LORD has come upon you.'",
      "T": "The son of the prophet Asa had imprisoned now confronted the son of Asa — the family line of rebuke continuing. Hanani the seer had been thrown in prison for telling Asa the truth about the Syrian alliance; his son Jehu now stood before Asa's son Jehoshaphat with the same unpleasant assignment. The rebuke is pointed: you helped the wicked, you loved those who hate the LORD. The wicked was Ahab; those who hated the LORD were the Baal-worshippers of the northern court. Jehoshaphat's alliance marriage and his joint military campaign had aligned Judah's faithful king with Israel's most faithless one. The LORD's wrath had already come — the battle at Ramoth-gilead, the near-death in the chariot charge, the failure of the Tarshish ships. The consequences of the alliance were already being felt."
    },
    "3": {
      "L": "Nevertheless, there are good things found in you, for you removed the Asherim from the land and have set your heart to seek God.",
      "M": "But there is some good in you, for you removed the Asherah poles from the land and have been determined to seek God.",
      "T": "The rebuke was not the final word. Jehu balanced judgment with honest acknowledgment: there is good in you. The Asherim removed, the heart directed toward God — these were real. The Chronicler's theology of individual assessment is careful: Jehoshaphat's failure in the Ahab alliance does not erase his faithfulness in the reform and the teaching mission. The wrath is real; the goodness is also real. God deals with the whole person, not a caricature."
    },
    "4": {
      "L": "Jehoshaphat lived at Jerusalem. And he went out again among the people, from Beersheba to the hill country of Ephraim, and brought them back to the LORD, the God of their fathers.",
      "M": "Jehoshaphat continued to live in Jerusalem, and he went out again among the people from Beersheba to the hill country of Ephraim and turned them back to the LORD, the God of their ancestors.",
      "T": "The response to rebuke: immediate, energetic, renewed. From Beersheba in the far south to the hill country of Ephraim in the north — the full extent of territory Judah controlled, including the captured border region. Jehoshaphat went out personally, not through administrators, to bring the people back to the LORD their God. The personal tour, the direct engagement with people in their own cities — this was a king who understood that covenant faithfulness was not administered from a throne room but modeled in person across the whole land."
    },
    "5": {
      "L": "He appointed judges in the land in all the fortified cities of Judah, city by city.",
      "M": "He appointed judges throughout the land, in every fortified city of Judah, city by city.",
      "T": "The judicial reform: a network of courts planted in every fortified city across Judah. This was a reorganization of the entire legal infrastructure of the kingdom, grounding it in the Mosaic covenant structure of Deuteronomy 16:18-20. Jehoshaphat was not merely appointing officials; he was rebuilding the covenant community's capacity for justice. A people who could not get fair judgment in their own cities could not flourish; the courts were as important as the army."
    },
    "6": {
      "L": "He said to the judges, 'Consider what you do, for you judge not for man but for the LORD. He is with you in giving judgment.'",
      "M": "He said to the judges, 'Be careful what you do, because you are not judging for human beings but for the LORD, who is with you when you give judgment.'",
      "T": "The charge to judges is grounded in theology, not merely in civic duty. You are not judging for man — for the litigants, for the powerful, for the patron who appointed you — but for the LORD. Every case brought before you comes ultimately before God, who is present in the court. This echoes Moses's instruction in Deuteronomy 1:17: 'For the judgment is God's.' The magistrate's bench is a place of divine representation; its occupant bears the weight of that accountability."
    },
    "7": {
      "L": "'Now then, let the fear of the LORD be upon you. Be careful what you do, for with the LORD our God there is no injustice or partiality or taking of bribes.'",
      "M": "'Now, let the fear of the LORD be on you. Act carefully, for the LORD our God does not tolerate injustice, partiality, or bribery.'",
      "T": "Three specific corruptions of justice named and prohibited: injustice (legal wrongdoing), partiality (deciding according to the identity of the litigant rather than the merits of the case), and bribery (deciding according to payment). God practices none of these, and the judges who represent him must practice none either. The fear of the LORD — that reverential awe before the one who will judge the judges — is not the beginning of paralysis but the beginning of integrity. A judge who fears the LORD will not accept a bribe; the fear is stronger than the inducement."
    },
    "8": {
      "L": "Moreover, in Jerusalem, Jehoshaphat appointed some of the Levites and priests and heads of the fathers' houses of Israel, for the judgment of the LORD and for disputes. Then they returned to Jerusalem.",
      "M": "In Jerusalem Jehoshaphat also appointed Levites, priests, and heads of Israelite clans to adjudicate cases involving the LORD's law and to resolve civil disputes. They were based in Jerusalem.",
      "T": "Above the network of local courts, Jehoshaphat established a supreme court in Jerusalem — the capital as both the religious and legal center of the kingdom. Levites, priests, and tribal heads sat together: a court that combined expertise in Torah (the Levites and priests knew the law), tribal representation (the heads of fathers' houses knew their communities), and royal authority (Jerusalem, the king's city). The court handled two distinct categories: matters of the LORD — religious law, ceremonial disputes, the law of the sanctuary — and civil matters, the disputes between Israelites over property, violence, and contracts."
    },
    "9": {
      "L": "And he charged them: 'Thus you shall do in the fear of the LORD, in faithfulness, and with a whole heart.'",
      "M": "He gave them this charge: 'You must carry out your duties in the fear of the LORD, with integrity, and wholeheartedly.'",
      "T": "Three words for the disposition of a just judge: fear of the LORD (accountability to God, not to power), faithfulness (emunah — reliability, truthfulness, the opposite of capriciousness), and a whole heart (undivided loyalty, no hidden agenda, no divided interest between God's justice and personal advantage). The same triad appears in the Shema's logic and in David's charge to Solomon (1 Chr 28:9). The covenant community's most dangerous internal failure is always a corrupted judiciary; Jehoshaphat addressed it at the source."
    },
    "10": {
      "L": "'Whenever a case comes to you from your brothers who live in their cities, concerning bloodshed, law or commandment, statutes or rules, you shall warn them, so that they may not incur guilt before the LORD and wrath may not come upon you and your brothers. Thus you shall do, and you will not incur guilt.'",
      "M": "'Whenever your fellow Israelites in their towns bring a case to you — whether involving bloodshed, law, commandment, statutes, or ordinances — you must instruct them so that they do not become guilty before the LORD and his wrath does not fall on you and your colleagues. Do this and you will not be guilty.'",
      "T": "The jurisdiction of the Jerusalem court was defined: any case referred up from the local courts, covering the full range of legal disputes. But the responsibility of the judges went beyond deciding cases: they were to warn — to instruct the litigants so they understood the law and did not sin in ignorance. The judge's role was educative as well as adjudicative; the goal was not merely a verdict but the formation of a community that understood its covenant obligations. Failure to warn was itself a form of guilt that would bring judgment on the judges themselves."
    },
    "11": {
      "L": "'And behold, Amariah the chief priest is over you in all matters of the LORD; and Zebadiah the son of Ishmael, the ruler of the house of Judah, is over you in all the king's matters. The Levites shall serve you as officers. Deal courageously, and may the LORD be with the good!'",
      "M": "'Amariah the chief priest will have final authority over all religious matters, and Zebadiah son of Ishmael, the leader of the tribe of Judah, will oversee all civil affairs. The Levites will assist you as clerks. Act with courage, and may the LORD be with those who do right.'",
      "T": "The supreme court was bicameral in structure: Amariah the high priest presided over cases touching the law of the LORD — the worship, the sanctuary, the priestly code; Zebadiah the son of Ishmael presided over the king's civil matters — property, crime, civic order. The Levites supported both as trained legal officers. The last word is a blessing that is also a warning: may the LORD be with the good — implying, and not with those who corrupt the good. Jehoshaphat closed his charge to the judiciary with a prayer, acknowledging that the courts could only be as just as the God who stood behind them allowed them to be."
    }
  },
  "20": {
    "1": {
      "L": "After this the Moabites and the Ammonites, and with them some of the Meunites, came against Jehoshaphat for battle.",
      "M": "After this, the Moabites and Ammonites, along with some Meunites, came to make war against Jehoshaphat.",
      "T": "A coalition assembled from the east and south: Moab, Ammon, and the Meunites — peoples from the region of Edom and the Arabah. The timing is notable: Jehoshaphat had just completed his judicial reform, had gone out personally to bring the people back to the LORD, had built the most comprehensive judicial structure in Judah's history. The test came immediately after the faithfulness. This pattern runs throughout Chronicles: the faithful king is tested precisely because his faithfulness is real."
    },
    "2": {
      "L": "Some men came and told Jehoshaphat, 'A great multitude is coming against you from beyond the sea, from Edom; and behold, they are in Hazazon-tamar,' that is, En-gedi.",
      "M": "Messengers came and reported to Jehoshaphat: 'A vast army is marching against you from the other side of the Dead Sea, from the region of Edom. They are already at Hazazon-tamar' — that is, En-gedi.",
      "T": "The intelligence report placed the enemy already at En-gedi — the oasis on the western shore of the Dead Sea, less than forty miles from Jerusalem. The phrase 'from beyond the sea, from Edom' is geographically puzzling (Edom is south and east, not across the Dead Sea) and may indicate the army had swept around the southern end of the sea and was now approaching from the west side. Regardless, they were close, they were many, and they were already in position. The crisis was immediate."
    },
    "3": {
      "L": "Then Jehoshaphat was afraid and set his face to seek the LORD, and he proclaimed a fast throughout all Judah.",
      "M": "Jehoshaphat was alarmed and turned to seek the LORD; he proclaimed a fast for all Judah.",
      "T": "Jehoshaphat was afraid — the text does not suppress this. Fear is the honest response to an overwhelming coalition within a day's march. But the fear ran in the right direction: it drove him to seek the LORD, not to send tribute or seek alliance. He proclaimed a national fast — the formal acknowledgment that the situation exceeded human capacity, that the nation was throwing itself before God. The fast was not performance; it was the covenant people's way of saying we have nothing but you."
    },
    "4": {
      "L": "And Judah gathered together to seek help from the LORD; from all the cities of Judah they came to seek the LORD.",
      "M": "Judah assembled to seek help from the LORD, and people came from every town in Judah to seek him.",
      "T": "The national gathering: from every city in Judah, the people streamed to Jerusalem. Not summoned by military conscription but drawn by the fast proclamation — they came to seek the LORD. The judicial reform had given them courts in their cities; now the crisis brought them to the one place that mattered more than any court: the house of the LORD in Jerusalem. The city that Jehoshaphat had equipped with justice was now receiving the people who needed a justice no human court could deliver."
    },
    "5": {
      "L": "And Jehoshaphat stood in the assembly of Judah and Jerusalem, in the house of the LORD, before the new court,",
      "M": "Jehoshaphat stood before the congregation of Judah and Jerusalem in the house of the LORD, in front of the new courtyard,",
      "T": "The scene is deliberately parallel to Solomon's dedication prayer (2 Chr 6:12-13): a king of the Davidic line standing before the assembled people in the house of the LORD, about to pray. The 'new court' was the outer court of the temple complex. Jehoshaphat stood where Solomon had stood; his prayer would echo Solomon's; the God who had answered Solomon was about to answer him."
    },
    "6": {
      "L": "and said, 'O LORD, God of our fathers, are you not God in heaven? You rule over all the kingdoms of the nations. In your hand are power and might, so that none is able to withstand you.'",
      "M": "'LORD, God of our ancestors, you are God in heaven, ruling over all the kingdoms of the nations. Power and might are in your hand, and no one can stand against you.'",
      "T": "The prayer opens with praise — not petition but proclamation. Jehoshaphat declares who God is before he asks anything: God in heaven (sovereign over all geography), ruler over all the kingdoms of the nations (sovereign over all political authority), power and might in his hand (sovereign over all military force). None is able to withstand you: the statement that makes the entire prayer possible. If this is true — if no coalition of Moab and Ammon and Meunites can stand against the God being invoked — then the prayer is not desperate; it is confident. Jehoshaphat prays from a theology that has just named the battlefield's real power structure."
    },
    "7": {
      "L": "'Did you not, our God, drive out the inhabitants of this land before your people Israel, and give it forever to the descendants of Abraham your friend?'",
      "M": "'Our God, you drove out the inhabitants of this land before your people Israel and gave it forever to the descendants of Abraham your friend.'",
      "T": "The historical argument: what God has done before, he can do again. The Canaanites were driven out — a people more deeply entrenched in the land than any Moabite coalition. And the land was given forever to the descendants of Abraham your friend. The word 'friend' (ohev) for Abraham is one of the most intimate designations in the Old Testament — it appears in Isaiah 41:8 and will reappear in James 2:23. Jehoshaphat is praying on the basis of the most ancient of God's covenants, established with his friend Abraham before any king or temple or army existed. The land is ours not because we took it but because you gave it to your friend."
    },
    "8": {
      "L": "'And they have lived in it and have built for you in it a sanctuary for your name, saying,'",
      "M": "'They have lived in it and have built in it a sanctuary for your name, saying,'",
      "T": "The argument moves from the land grant to the temple — Solomon's prayer made in the house God promised to inhabit. The sanctuary was not Israel's achievement but Israel's response to God's invitation; they built it for his name, the place where the Name would dwell and hear prayer. What follows (v. 9) is almost a quotation from Solomon's dedicatory prayer in 2 Chronicles 6."
    },
    "9": {
      "L": "'\"If disaster comes upon us, the sword, judgment, or pestilence, or famine, we will stand before this house and before you — for your name is in this house — and cry out to you in our affliction, and you will hear and save.\"'",
      "M": "'\"When calamity strikes us — sword, judgment, plague, or famine — we will stand before this house and before you, for your name is in this house. We will cry to you in our distress, and you will hear and deliver us.\"'",
      "T": "Jehoshaphat quotes back to God the promise Solomon extracted from God at the temple's dedication. Solomon had prayed: 'If your people come and pray toward this house, then hear in heaven.' God had responded: 'My eyes will be open and my ears attentive to prayer from this place' (2 Chr 7:15). Jehoshaphat is now doing exactly what God promised he would hear: standing before the house, naming the disaster, crying out. He is not arguing; he is taking God at his word. The prayer is the activation of a promise already made. 'You will hear and save' — not 'we hope' but 'you will.' The covenant is the basis of the confidence."
    },
    "10": {
      "L": "'And now behold, the men of Ammon and Moab and Mount Seir, whom you would not let Israel invade when they came from the land of Egypt, and whom they avoided and did not destroy —'",
      "M": "'And now here are the men of Ammon, Moab, and Mount Seir — nations you would not let Israel invade when they came out of Egypt, so Israel turned away from them and did not destroy them —'",
      "T": "The irony of the petition is sharpened by history: God had specifically commanded Israel not to attack Moab or Ammon during the wilderness journey (Deut 2:9, 19), because they were descendants of Lot. Israel had honored that command; they had gone around these peoples rather than through them. And now those same peoples, spared by Israel's obedience to God's instruction, were the ones attacking. The implicit question — the question underlying the whole verse — is: we obeyed you regarding them; will you now protect us from them? The history of mercy is being turned into a prayer."
    },
    "11": {
      "L": "'behold, they reward us by coming to drive us out of your possession, which you have given us to inherit.'",
      "M": "'now see how they repay us by coming to drive us out of your land, which you gave us as an inheritance.'",
      "T": "The ingratitude named: this land is yours — given to us, held as inheritance from you. The enemies are not attacking a political rival; they are coming to expel God's people from God's land. Jehoshaphat frames the invasion not as a military challenge but as an offense against the divine landlord. This is not Judah's problem; it is God's problem. The land they are trying to seize belongs to the God who is being asked to defend it."
    },
    "12": {
      "L": "'O our God, will you not execute judgment on them? For we are powerless against this great horde that is coming against us. We do not know what to do, but our eyes are on you.'",
      "M": "'Our God, will you not judge them? We are powerless against this vast army attacking us. We don't know what to do, but our eyes are fixed on you.'",
      "T": "The climax of the prayer — and one of the most honest prayers in all of Scripture. 'We do not know what to do.' No military strategy, no diplomatic gambit, no plan. The admission is total: we are out of options. This is Asa's prayer at Mareshah in reverse key — there Asa prayed 'we have no strength, only you'; here Jehoshaphat prays 'we have no wisdom, only you.' The reliance is identical. 'But our eyes are on you' — the whole direction of the nation's attention turned from the threat to the one who holds threats in his hand. This is what the Chronicler means by shaan — resting your weight on God. The prayer does not ask for victory; it asks for judgment, for God to be God in this situation, for the eyes to be answered by the action of the one they see."
    },
    "13": {
      "L": "Meanwhile all Judah stood before the LORD, with their little ones, their wives, and their children.",
      "M": "All the people of Judah stood before the LORD, along with their little ones, their wives, and their children.",
      "T": "The entire community present: not the army, not the officials, not the religious professionals — all Judah, including the most vulnerable. Little ones, wives, children — the people who would suffer most if the coalition won, standing before the LORD in the prayer that was the only thing standing between them and destruction. The image is more powerful than any battle formation: a whole people, helpless and exposed, placing themselves before God."
    },
    "14": {
      "L": "And the Spirit of the LORD came upon Jahaziel the son of Zechariah, son of Benaiah, son of Jeiel, son of Mattaniah, a Levite of the sons of Asaph, in the midst of the assembly.",
      "M": "Then the Spirit of the LORD came on Jahaziel son of Zechariah, son of Benaiah, son of Jeiel, son of Mattaniah — a Levite of the line of Asaph — in the middle of the assembly.",
      "T": "The Spirit of the LORD — not the spirit of wisdom or the spirit of skill, but the prophetic Spirit that comes upon a person to speak God's word in a crisis. Jahaziel was a Levite of Asaph's line — the guild of temple singers established by David (1 Chr 25:1). The Asaphites were not primarily prophets but musicians; the Spirit was not limited to the prophetic guild. As with Azariah in chapter 15, the Spirit chose an unexpected vessel at an unexpected moment. The full genealogy is given — four generations — because this moment is being marked as historically significant, and the man who spoke the word deserves to be remembered by name."
    },
    "15": {
      "L": "And he said, 'Listen, all Judah and inhabitants of Jerusalem and King Jehoshaphat! Thus says the LORD to you: Do not be afraid and do not be dismayed at this great horde, for the battle is not yours but God's.'",
      "M": "'Listen, all Judah, people of Jerusalem, and King Jehoshaphat! This is what the LORD says to you: Do not be afraid or discouraged because of this vast army. The battle is not yours — it belongs to God.'",
      "T": "The word from God comes through the unexpected prophet — and it begins with the universal formula of divine reassurance: do not be afraid. The same words God had spoken through Moses at the Red Sea ('do not be afraid; stand firm and see the salvation of the LORD'), through the angel to Joshua ('do not be afraid'), through every prophet who ever delivered a word of deliverance to a surrounded and terrified people. Then the radical reframing: the battle is not yours. You came to fight; you brought an army; you have commanders and positions and weapons. None of it is relevant. This battle belongs to God. Your role is not to win but to watch."
    },
    "16": {
      "L": "'Tomorrow go down against them. Behold, they will come up by the ascent of Ziz. You will find them at the end of the valley, east of the wilderness of Jeruel.'",
      "M": "'Tomorrow march down against them. They will be coming up by the pass of Ziz, and you will find them at the end of the valley that faces the wilderness of Jeruel.'",
      "T": "The tactical intelligence was specific: the pass of Ziz, the valley east of Jeruel. God knew exactly where the enemy would be, because God had already decided what would happen to them. The 'go down against them' is not a battle order but a witness order — go where you can see what I am about to do. The geography was given so that Judah would know that when they found the enemy in that valley, it was not luck but the word of God proved true."
    },
    "17": {
      "L": "'You will not need to fight in this battle. Stand firm, hold your position, and see the salvation of the LORD on your behalf, O Judah and Jerusalem. Do not be afraid and do not be dismayed. Tomorrow go out against them, and the LORD will be with you.'",
      "M": "'You will not need to fight in this battle. Take your positions, stand firm, and watch the LORD save you. Judah and Jerusalem, do not be afraid or lose heart. Tomorrow march out against them, and the LORD will be with you.'",
      "T": "'You will not need to fight' — the complete suspension of military effort. Stand firm: Moses's word at the Red Sea (Exod 14:13), handed down through the centuries to this moment in the Judean wilderness. Hold your position: literally, station yourselves, take your places as an audience, not as combatants. See the salvation of the LORD: the Exodus language intact, the same God, the same promise, a new generation of the same people surrounded by a new version of the same impossible situation. The pattern from Sinai to Zemaraim to Mareshah now appears again: God fights, Israel watches, Israel receives a salvation it could not manufacture. Then the reassurance is repeated — do not be afraid, do not be dismayed — because the human heart forgets even words just spoken, and God is patient with the repetition that faith needs."
    },
    "18": {
      "L": "Then Jehoshaphat bowed his head with his face to the ground, and all Judah and the inhabitants of Jerusalem fell down before the LORD, worshipping the LORD.",
      "M": "Jehoshaphat bowed down with his face to the ground, and all Judah and the people of Jerusalem fell facedown before the LORD in worship.",
      "T": "The response to the oracle: prostration, not celebration. Before they had won a single engagement, before they had taken a single step toward the valley of Jeruel, they fell on their faces before the LORD. This was not victory worship but faith worship — the adoration of a people who had heard a word from God and chose to receive it as true before the evidence was visible. The facedown posture was the body's language for what Jehoshaphat's prayer had already declared: we have nothing but you, and that is enough."
    },
    "19": {
      "L": "And the Levites, of the Kohathites and the Korahites, stood up to praise the LORD, the God of Israel, with a very loud voice.",
      "M": "The Levites of the Kohathite and Korahite clans stood up and praised the LORD, the God of Israel, with a very loud voice.",
      "T": "While the rest of the assembly lay facedown, the Levites stood to sing. The Kohathites and Korahites — the two main branches of the Levitical choir, the descendants of those David had appointed as singers for the house of the LORD — lifted their voices. The very loud voice is not a detail about volume; it is a statement about conviction. The Levites sang as though they already believed what Jahaziel had said, which is the only kind of faith that matters. The prayer had moved to worship before the battle had moved a step."
    },
    "20": {
      "L": "And they rose early in the morning and went out into the wilderness of Tekoa. And as they went out, Jehoshaphat stood and said, 'Hear me, Judah and inhabitants of Jerusalem! Believe in the LORD your God, and you will be established; believe his prophets, and you will succeed.'",
      "M": "'Listen to me, Judah and people of Jerusalem! Trust in the LORD your God, and you will stand firm. Trust in his prophets, and you will succeed.'",
      "T": "The march began at dawn, into the wilderness toward Tekoa — the home territory of Amos, the wilderness terrain south and east of Bethlehem. Before the army moved, Jehoshaphat called for attention. His battle speech was a single theological sentence: believe in the LORD your God and you will be established; believe his prophets and you will succeed. The verb hiphil of aman — the same root Isaiah 7:9 used when God said to Ahaz, 'if you are not firm in faith, you will not be firm at all.' Ahaz had refused to believe and lost his kingdom to the Assyrian shadow; Jehoshaphat chose to believe and was about to see the LORD fight for him. The echo was not accidental; the Chronicler placed the same root word in Jehoshaphat's mouth to mark the contrast. Where Ahaz failed, Jehoshaphat walked forward."
    },
    "21": {
      "L": "And when he had taken counsel with the people, he appointed those who were to sing to the LORD and praise him in holy attire, as they went before the army, and say, 'Give thanks to the LORD, for his steadfast love endures forever.'",
      "M": "After consulting with the people, he appointed singers to walk before the army and praise the LORD in holy robes, singing: 'Give thanks to the LORD, for his steadfast love endures forever.'",
      "T": "The battle formation of the Judean army: singers at the front, warriors behind. The singers were clothed in the holy attire of the Levitical choir — the vestments of the temple, worn in the wilderness. And what they sang was not a battle hymn but the refrain of Psalm 136: 'Give thanks to the LORD, for his steadfast love endures forever.' That phrase — ki le'olam chasdo — appears twenty-six times in Psalm 136, once after every rehearsal of God's mighty acts from creation through the Exodus and the conquest. The army marched into battle reciting Israel's entire history of salvation, condensed into a single repeated phrase. The steadfast love that brought Israel out of Egypt, that divided the Red Sea, that drove out the Canaanites, that endures forever — that same covenant loyalty was being invoked now, in the Judean wilderness, as the troops walked toward the valley. This was not strategy; it was theology in motion."
    },
    "22": {
      "L": "And when they began to sing and praise, the LORD set an ambush against the men of Ammon, Moab, and Mount Seir, who had come against Judah, so that they were routed.",
      "M": "As they began to sing and praise, the LORD set an ambush against the men of Ammon, Moab, and Mount Seir who were invading Judah, and they were defeated.",
      "T": "As they began — the moment of the music was the moment of the intervention. Not after the battle, not while Judah fought bravely — as they began to sing. The LORD set an ambush: not Judah's army, not a human tactical maneuver, but a divine military action in the unseen world that produced a visible result in the valley. The coalition that had assembled to destroy Judah destroyed itself. The singing was the act of faith; the ambush was God's response to that faith. The sequence is theologically precise: the people trusted, walked forward in trust, sang the refrain of God's enduring covenant loyalty — and God proved the refrain true."
    },
    "23": {
      "L": "For the men of Ammon and Moab rose against the inhabitants of Mount Seir, devoting them to destruction, and when they had made an end of the inhabitants of Seir, they all helped to destroy one another.",
      "M": "The men of Ammon and Moab turned against the people of Mount Seir and completely destroyed them. After finishing off the Seirites, they turned on each other.",
      "T": "The mechanism of the ambush: the coalition fractured. Ammon and Moab turned against their Seirite allies — perhaps an old tribal enmity, perhaps a dispute over spoil, perhaps the direct work of God sowing confusion in the enemy camp as he had sowed confusion in Midian in Gideon's time (Judg 7:22) and in Philistia in Saul's time (1 Sam 14:20). When the Seirites were gone, the Ammonites and Moabites finished the work by destroying each other. God's ambush was not an independent army; it was the enemy's own violence turned inward. The coalition that came to destroy Judah was itself the instrument of its own destruction."
    },
    "24": {
      "L": "When Judah came to the watchtower of the wilderness, they looked toward the horde, and behold, there were dead bodies lying on the ground; none had escaped.",
      "M": "When the men of Judah reached the watchtower overlooking the wilderness, they looked toward the enemy horde — and there were dead bodies covering the ground. None had survived.",
      "T": "Judah arrived at the overlook and found what God had promised: a battle already finished before they had struck a blow. 'None had escaped' — the totality of the destruction matching the totality of the threat. The army that had been coming against Judah in overwhelming force lay dead on the ground of the valley where Jahaziel had said they would find the enemy. The prophecy was exact; the fulfillment was exact. Judah had walked forward singing; God had fought."
    },
    "25": {
      "L": "When Jehoshaphat and his people came to take the spoil, they found among them, in great quantities, goods, clothing, and precious things, which they took for themselves until they could carry no more. They were three days in taking the spoil, it was so much.",
      "M": "When Jehoshaphat and his army came to collect the plunder, they found enormous quantities of goods, clothing, and precious items — more than they could carry away. It took three days to gather all the spoil, there was so much.",
      "T": "Three days to collect the spoil from a battle Judah did not fight. The valley floor was covered with the equipment, weapons, goods, and wealth of three armies that had come to plunder Judah and instead lay dead. The irony is the Chronicler's theological commentary: they came to take what was ours; instead, what was theirs became ours. The army that marched out singing about God's steadfast love came home three days later loaded with the wealth of those who had despised that love. God had not merely protected Judah; he had prospered them at their enemies' expense."
    },
    "26": {
      "L": "On the fourth day they assembled in the Valley of Berachah, for there they blessed the LORD. Therefore the name of that place has been called the Valley of Berachah to this day.",
      "M": "On the fourth day they gathered in the Valley of Berachah, where they gave thanks and blessed the LORD. That is why it has been called the Valley of Berachah — the Valley of Blessing — to this day.",
      "T": "The Valley of Berachah — the Valley of Blessing. A toponym carved into the landscape by a single act of corporate worship. The people who had gathered in Jerusalem to fast and pray now gathered in the valley where God had fought for them, to bless the one who had done it. The naming was an act of theological memory: future generations passing through that valley would carry the name, and the name would carry the story. Geography as catechism. The valley would remember what the people had done there even if the people forgot."
    },
    "27": {
      "L": "Then all the men of Judah and Jerusalem, with Jehoshaphat at their head, returned to Jerusalem with joy, for the LORD had made them rejoice over their enemies.",
      "M": "Then all the men of Judah and Jerusalem, with Jehoshaphat leading them, returned joyfully to Jerusalem, because the LORD had given them cause to rejoice over their enemies.",
      "T": "The return is the inverse of the departure: they had gone out in fear and faith; they came back in joy and triumph. Jehoshaphat at their head — the king who had stood before the assembly and prayed the prayer of helplessness now led the triumphal procession. The joy was not theirs; the LORD had given it to them. The grammatical structure is exact: 'the LORD had made them rejoice.' They did not generate the joy; they received it from the God who had given them the victory they had not earned."
    },
    "28": {
      "L": "They came to Jerusalem with harps and lyres and trumpets, to the house of the LORD.",
      "M": "They entered Jerusalem with lyres, harps, and trumpets and went to the house of the LORD.",
      "T": "The army processed into the city with the instruments of the Levitical choir — lyres, harps, and trumpets — and went directly to the temple. The first destination of the returning victors was not the palace but the house of the LORD. The journey had begun in the house of the LORD with prayer; it ended in the house of the LORD with music. The inclusio was liturgical: God's house as both the starting point of faith and the destination of gratitude."
    },
    "29": {
      "L": "And the fear of God came upon all the kingdoms of the countries when they heard that the LORD had fought against the enemies of Israel.",
      "M": "The terror of God fell on all the surrounding kingdoms when they heard that the LORD had fought against the enemies of Israel.",
      "T": "The news spread — as it had spread after Jericho, after Mareshah, after every instance when God fought for his people — and the surrounding kingdoms felt it. The fear of God is not merely political respect or military caution; it is the visceral recognition that something supernatural is at work in Israel's affairs. Nations that might have exploited Judah's crisis held back; nations that might have tested the new peace kept their distance. The God who had fought against the coalition was clearly willing to fight again. The valley of dead bodies was the most effective diplomatic message Jehoshaphat ever sent."
    },
    "30": {
      "L": "So the realm of Jehoshaphat was quiet, for his God gave him rest on every side.",
      "M": "Jehoshaphat's kingdom was at peace, for his God gave him rest on every side.",
      "T": "Rest — the covenant blessing that follows faithfulness, given here with a precision the Chronicler always marks: his God gave him rest. Not political skill, not military strength, not diplomacy — his God. The rest was the fruit of the relationship, not the product of human management. Jehoshaphat's kingdom was quiet because the God who had just destroyed three armies at once was pleased with the king who had prayed the prayer of total dependence and sent the army out singing."
    },
    "31": {
      "L": "Jehoshaphat reigned over Judah. He was thirty-five years old when he began to reign, and he reigned twenty-five years in Jerusalem. His mother's name was Azubah the daughter of Shilhi.",
      "M": "Jehoshaphat reigned over Judah. He was thirty-five years old when he became king and reigned twenty-five years in Jerusalem. His mother's name was Azubah daughter of Shilhi.",
      "T": "The reign summary placed here — not at the end of the chapter — serves as the transition from the narrative of the great victory to the assessment of the reign as a whole. Twenty-five years on the throne, beginning at thirty-five. His mother Azubah daughter of Shilhi: the woman whose name anchored the royal genealogy. The Chronicler's care with these details is the care of a historian who knew that names and years would outlast the stories they anchored."
    },
    "32": {
      "L": "He walked in the way of his father Asa and did not turn aside from it, doing what was right in the sight of the LORD.",
      "M": "He followed the example of his father Asa and did not deviate from it, doing what was right in the LORD's eyes.",
      "T": "The theological verdict: he walked in Asa's way — the early Asa, the Asa of the covenant renewal, the Asa of Mareshah, not the Asa of the Syrian alliance and the imprisoned prophet. The Chronicler is careful: Asa's way includes the good and the bad; Jehoshaphat followed the good portion of it. He did not turn aside — a phrase that echoes the royal theology of Deuteronomy, where the ideal king does not turn aside from the Torah to the right or the left."
    },
    "33": {
      "L": "The high places, however, were not taken away; the people had not yet set their hearts upon the God of their fathers.",
      "M": "The high places, however, were not removed, and the people still had not fully committed their hearts to the God of their ancestors.",
      "T": "The qualification no Chronicler could omit. Jehoshaphat had removed some high places (17:6), had sent the teaching mission, had built the judicial network — and still the high places remained, and still the people's hearts were not wholly given to God. Reform runs ahead of transformation; the external structures of worship can be cleared before the internal structures of the heart follow. The Chronicler saw this gap not as Jehoshaphat's failure alone but as the persistent condition of a people who kept reverting to the familiar. The reform was real; its incompleteness was also real."
    },
    "34": {
      "L": "Now the rest of the acts of Jehoshaphat, from first to last, are written in the chronicles of Jehu the son of Hanani, which is recorded in the Book of the Kings of Israel.",
      "M": "The rest of Jehoshaphat's acts, from beginning to end, are recorded in the account of Jehu son of Hanani, which is included in the Book of the Kings of Israel.",
      "T": "The prophetic archive cited: Jehu son of Hanani — the same Jehu who had rebuked Jehoshaphat at the beginning of this chapter (19:2). The prophet who challenged the king in person was also the historian who preserved the king's full record for posterity. The rebuke and the chronicle came from the same person: someone who both loved truth enough to say the hard thing and cared about memory enough to record the full life. Jehu's account was incorporated into the larger royal history — the Book of the Kings of Israel (meaning all Israel, north and south, the full covenant community)."
    },
    "35": {
      "L": "After this Jehoshaphat king of Judah joined with Ahaziah king of Israel, who acted wickedly.",
      "M": "Later, Jehoshaphat king of Judah entered into a partnership with Ahaziah king of Israel, who was a wicked man.",
      "T": "After all of it — after the great prayer, the singing army, the valley of dead enemies, the Valley of Blessing, the peace — he did it again. Joined with Ahaziah, Ahab's son, the heir of the family whose wickedness had been the problem in chapters 18 and 19. The pattern was stubborn: Jehoshaphat's most persistent weakness was the Ahab alliance. The marriage alliance with Ahab had been one lapse; the joint battle at Ramoth-gilead was another; now, after the judgment of the Meunite coalition and the unambiguous vindication of faith over alliance, he entered another commercial partnership with the northern house. The Chronicler places this error here, immediately after the peace summary, as the shadow that fell on the last years of an otherwise faithful reign."
    },
    "36": {
      "L": "He joined him in building ships to go to Tarshish, and they built the ships in Ezion-geber.",
      "M": "He partnered with Ahaziah to build a fleet of ships to sail to Tarshish. They built the ships at Ezion-geber.",
      "T": "Ezion-geber — the port at the head of the Gulf of Aqaba, the same port Solomon had used for his Ophir trade (2 Chr 8:17-18). Tarshish was the distant western trade destination — likely a port in Spain or Sardinia, the edge of the known world. The commercial ambition was Solomonic in scale; the partnership was disastrous in character. Solomon had built a fleet; Jehoshaphat would build a fleet. But Solomon had not built it in alliance with a king the Chronicler describes as wicked."
    },
    "37": {
      "L": "Then Eliezer the son of Dodavahu of Mareshah prophesied against Jehoshaphat, saying, 'Because you have joined with Ahaziah, the LORD will destroy your works.' And the ships were wrecked and were not able to go to Tarshish.",
      "M": "Eliezer son of Dodavahu from Mareshah prophesied against Jehoshaphat: 'Because you have allied with Ahaziah, the LORD will shatter your works.' The ships were wrecked and could not sail to Tarshish.",
      "T": "Another prophet from Mareshah — the city that had seen Asa's great victory over Zerah the Cushite (2 Chr 14:10), the city that embodied the principle that God fights for those who rely on him. Eliezer's prophecy was immediate and specific: because of the alliance, the works will be destroyed. The ships were wrecked — the Hebrew word prits carries the sense of shattering, breaking apart. The commercial venture that was meant to bring wealth ended in splinters. The judgment was proportionate: the alliance produced nothing. This closing episode frames Jehoshaphat's reign with the same theological message as its opening: the alliance with the house of Ahab costs more than it could ever be worth."
    }
  },
  "21": {
    "1": {
      "L": "Jehoshaphat slept with his fathers and was buried with his fathers in the city of David. And Jehoram his son reigned in his place.",
      "M": "Jehoshaphat rested with his ancestors and was buried with them in the city of David. His son Jehoram succeeded him as king.",
      "T": "Jehoshaphat's death is recorded without ceremony — 'slept with his fathers,' the standard royal obituary — and the transition to Jehoram is immediate. The twenty-five years that had contained the teaching mission, the great prayer, the singing army, the Valley of Blessing were over. What followed would be as dark as those years had been bright. The king who had not fully removed the high places was succeeded by the king who built new ones."
    },
    "2": {
      "L": "He had brothers, the sons of Jehoshaphat: Azariah, Jehiel, Zechariah, Azariah, Michael, and Shephatiah; all these were the sons of Jehoshaphat king of Israel.",
      "M": "Jehoshaphat's sons were: Azariah, Jehiel, Zechariah, Azariah, Michael, and Shephatiah — all sons of Jehoshaphat king of Judah.",
      "T": "Six brothers — all named, all sons of the faithful Jehoshaphat who had prayed and sung his way through the Meunite invasion. Their names carried covenant themes: Azariah ('the LORD has helped'), Jehiel ('God lives'), Zechariah ('the LORD remembers'), Michael ('who is like God'). The family bore the names of covenant theology. What followed would make those names a terrible irony."
    },
    "3": {
      "L": "Their father gave them great gifts of silver, gold, and precious things, with fortified cities in Judah, but he gave the kingdom to Jehoram, because he was the firstborn.",
      "M": "Their father gave them generous gifts of silver, gold, and valuables, along with fortified cities in Judah. But he gave the kingship to Jehoram, since he was the firstborn.",
      "T": "Jehoshaphat's wisdom in the succession: the six younger sons received substantial provision — wealth, cities, security — to prevent the bitter rivalry that had destabilized other dynasties. The kingdom went to the firstborn by covenant right. The provision for the brothers was meant to make the succession peaceful; Jehoram would make it murderous."
    },
    "4": {
      "L": "When Jehoram had ascended the throne of his father and had secured his position, he killed all his brothers with the sword, and also some of the princes of Israel.",
      "M": "Once Jehoram had established himself as king over his father's kingdom, he put all his brothers to the sword, along with some of the Israelite leaders.",
      "T": "The first act of Jehoram's reign: the murder of his brothers. The six sons Jehoshaphat had generously provided for, the young men bearing the names of covenant theology, were killed by the oldest because they were potential threats to the throne. The logic of political self-preservation — ancient, brutal, familiar in the ancient Near East — overrode every obligation of family and covenant. With the princes of Israel — probably officials, perhaps supporters of the brothers — Jehoram eliminated every rival and every witness. A reign that would be defined by murder began with murder."
    },
    "5": {
      "L": "Jehoram was thirty-two years old when he became king, and he reigned eight years in Jerusalem.",
      "M": "Jehoram was thirty-two years old when he began to reign, and he reigned eight years in Jerusalem.",
      "T": "Eight years — eight years that would destroy what decades of Asa and Jehoshaphat had built. The Chronicler gives the age and the duration with the same formula used for every king; the brevity is not mercy but proportion. Eight years was what this king earned."
    },
    "6": {
      "L": "He walked in the way of the kings of Israel, as the house of Ahab had done, for the daughter of Ahab was his wife. And he did what was evil in the sight of the LORD.",
      "M": "He followed the example of the kings of Israel — just as the house of Ahab had done — because his wife was Ahab's daughter. He did what was evil in the LORD's sight.",
      "T": "The Ahab alliance had now come home in the most literal way: Ahab's daughter was Jehoram's wife — Athaliah, whose destructive presence in Jerusalem would eventually produce a coup and a massacre of Davidic heirs (2 Chr 22:10). Jehoshaphat had made the marriage alliance; Jehoram bore its consequence. The daughter of Ahab walked in Ahab's ways, and Jehoram walked with her. The evil in the LORD's sight is stated without euphemism: this was not a failure of education or judgment but a deliberate choice to follow the Omride dynasty's pattern of religious corruption."
    },
    "7": {
      "L": "Yet the LORD was not willing to destroy the house of David, because of the covenant that he had made with David, and since he had promised to give a lamp to him and to his sons forever.",
      "M": "Yet the LORD was not willing to destroy the house of David, because of the covenant he had made with David, having promised to give him and his descendants a lasting dynasty.",
      "T": "The theological anchor that held against everything Jehoram was doing: the Davidic covenant. God had sworn — sworn to David — that the dynasty would not be extinguished. The lamp (nir) — the image of a flame passed from father to son, an unbroken line of succession that represented the continuity of the house — had been promised to David and to his sons forever. Jehoram was everything a Davidic king should not be; his murder of his brothers had nearly extinguished that lamp himself. But the God who made the covenant was not limited by the failures of the kings who inherited it. The lamp would burn despite Jehoram, as it had burned despite Rehoboam and Abijah and the worst chapters of Asa's final years. The covenant was older and more durable than any single king's wickedness."
    },
    "8": {
      "L": "In his days Edom revolted from the rule of Judah and set up a king of their own.",
      "M": "During his reign, Edom rebelled against Judah's authority and crowned their own king.",
      "T": "The first consequence of Jehoram's wickedness visible in the political world: Edom revolted. Judah had controlled Edom since the time of David; Jehoshaphat had maintained that control and used the port at Ezion-geber (on Edomite territory) for his Tarshish fleet. Jehoram's kingdom shrank on the first test. The Chronicler's causality is consistent: unfaithfulness costs the king territory and security. What faithfulness had maintained, unfaithfulness began to lose."
    },
    "9": {
      "L": "Then Jehoram crossed over with his commanders and all his chariots. And he rose up by night and struck the Edomites who had surrounded him and the commanders of the chariots.",
      "M": "Jehoram crossed over with his commanders and all his chariots. He got up at night and broke through when the Edomites surrounded him and his chariot commanders.",
      "T": "A military engagement that was only a partial success: Jehoram broke out of encirclement, which means the Edomites had successfully surrounded the Judean force — an embarrassment for a king claiming David's military inheritance. He escaped; he did not conquer. The Edomite revolt was not suppressed; Judah's king managed only to extricate himself from a trap. The parallel account in 2 Kings 8:20-22 records the same event with the same ambiguous outcome: Jehoram struck the Edomites around him, but Edom remained in revolt."
    },
    "10": {
      "L": "So Edom revolted from the rule of Judah to this day. At that time Libnah also revolted from his rule, because he had forsaken the LORD, the God of his fathers.",
      "M": "So Edom has remained independent of Judah to this day. At the same time Libnah also rebelled against Jehoram, because he had abandoned the LORD, the God of his ancestors.",
      "T": "Edom independent to this day — the Chronicler writing from a point in time when Edom's freedom from Judah was still the known reality, a permanent wound in Judah's territory that traced back to Jehoram's reign. And Libnah — the Judean city in the Shephelah lowlands, near Philistine territory — also revolted. Two revolts in the same passage; two pieces of Judah's inheritance slipping away. The Chronicler names the cause: he had forsaken the LORD, the God of his fathers. The political fragmentation was the visible consequence of spiritual abandonment. Jehoshaphat had built the realm through faithfulness; Jehoram was dismantling it through unfaithfulness, piece by piece."
    },
    "11": {
      "L": "Moreover, he made high places in the hill country of Judah and led the inhabitants of Jerusalem into whoredom and made Judah go astray.",
      "M": "He also built high places throughout the hill country of Judah, seduced the people of Jerusalem into spiritual prostitution, and led Judah astray.",
      "T": "The internal corruption now matched the external losses. Jehoram built new high places — not merely failing to remove the ones Asa and Jehoshaphat had left standing, but constructing new ones for the Baal and Asherah worship he had brought in with Athaliah. The language of whoredom (zanah) is the prophetic word for covenant unfaithfulness expressed in idolatry: Israel was married to the LORD; worshipping other gods was adultery. Jehoram actively seduced his people into this betrayal, 'compelling' the inhabitants of Jerusalem toward the shrines. The king who should have maintained the covenant became the instrument of its violation."
    },
    "12": {
      "L": "And a letter came to him from Elijah the prophet, saying: 'Thus says the LORD, the God of David your father, \"Because you have not walked in the ways of your father Jehoshaphat or in the ways of Asa king of Judah,\"'",
      "M": "Then Elijah the prophet sent him a letter: 'This is what the LORD, the God of your father David, says: \"You have not followed the example of your father Jehoshaphat or of Asa king of Judah.\"'",
      "T": "A letter from Elijah — one of the most anomalous details in Chronicles, absent from the parallel account in Kings. Elijah was the prophet of the northern kingdom, the man who had stood against Ahab and Jezebel on Mount Carmel and in Naboth's vineyard; he had been translated to heaven before Jehoram's reign was fully established. The Chronicler either had access to a prophetic archive that preserved an earlier communication from Elijah, or the letter represents a posthumous prophetic word preserved among his disciples and delivered when its time came. What matters theologically is the message: the greatest prophet of the northern kingdom was being invoked against the southern king who had married into the northern apostasy. Elijah's witness crossed the border and outlasted his translation."
    },
    "13": {
      "L": "'\"but have walked in the way of the kings of Israel and have enticed Judah and the inhabitants of Jerusalem into whoredom, as the house of Ahab led Israel into whoredom, and also you have killed your brothers, of your father's house, who were better than you,\"'",
      "M": "'\"Instead, you have followed the pattern of the kings of Israel and have seduced Judah and Jerusalem into spiritual prostitution, just as the house of Ahab corrupted Israel. You have also murdered your brothers, your own family, who were better men than you.\"'",
      "T": "The indictment is precise and comprehensive: walked in the way of the kings of Israel — the Jeroboam line, the Ahab house, the worship-system-built-on-golden-calves. Led Judah into whoredom — the same verb as verse 11, the covenant-unfaithfulness that expressed itself in Baal worship. As Ahab led Israel — the comparison made explicit: Jehoram had done to Judah what Ahab and Jezebel had done to Israel, making him not merely a bad king but the southern mirror of the worst northern king. And then, the charge that is most damning in terms of covenant and covenant community: you killed your brothers who were better than you. The men bearing names like 'the LORD has helped' and 'the LORD remembers' were murdered by their brother because they might threaten his power. The prophetic verdict on this is not merely political but theological: better than you."
    },
    "14": {
      "L": "'\"behold, the LORD will bring a great plague on your people, your children, your wives, and all your possessions.\"'",
      "M": "'\"Now the LORD will strike your people, your children, your wives, and everything you own with a devastating blow.\"'",
      "T": "The judgment announced: not immediately on Jehoram himself but on everything around him — his people, his children, his wives, his possessions. The ripple effect of royal wickedness: the king's sin was not private; his whole household and kingdom bore the consequences. This was the covenant theology of Numbers 14:18 applied to a king who had broken every covenant obligation he inherited."
    },
    "15": {
      "L": "'\"and you yourself will have a severe sickness with a disease of your bowels, until your bowels come out because of the disease, day by day.\"'",
      "M": "'\"You yourself will suffer a severe bowel disease that will grow worse day by day until your intestines come out.\"'",
      "T": "The personal judgment was specific and public: a disease of the bowels, progressive and fatal, ending in the physical collapse described in verse 19. Ancient commentators noted the symbolic fitness — a king who had 'disemboweled' his dynasty by murdering his brothers died by the failure of his own bowels. The Chronicler does not draw the connection explicitly, but its weight is visible. Elijah's letter was a prophecy; its fulfillment would be exact, as the fulfillment of Micaiah's prophecy about Ahab had been exact."
    },
    "16": {
      "L": "And the LORD stirred up against Jehoram the spirit of the Philistines and of the Arabians who are near the Ethiopians.",
      "M": "The LORD stirred up against Jehoram the hostility of the Philistines and the Arabians who bordered the Cushites.",
      "T": "God stirred up — the same verb used in 1 Chronicles 5:26 when God stirred up the Assyrians against the northern tribes, and in Ezra 1:1 when God stirred up Cyrus to send Israel home. Divine sovereignty working through human political motives: the Philistines and Arabians had their own reasons to attack Judah, but God was the primary cause of their mobilization. The coalition that assembled against Jehoshaphat in chapter 20 had come from the east; this new coalition came from the west and south. Jehoram was surrounded by enemies, all of them instruments of the judgment Elijah had predicted."
    },
    "17": {
      "L": "And they came up against Judah and invaded it and carried away all the possessions found in the king's house, and also his sons and his wives, so that no son was left to him except Jehoahaz, his youngest son.",
      "M": "They invaded Judah, broke through its defenses, and carried off everything in the royal palace, including Jehoram's sons and wives. Only Jehoahaz, his youngest son, was left.",
      "T": "The raid was devastating: the royal household stripped, the royal sons taken, the royal wives carried off. Only the youngest remained. The dynasty Jehoram had tried to secure by murdering his brothers was now reduced to a single son — the youngest, the most vulnerable, spared by accident rather than by any protection the king could provide. The man who had killed his siblings to eliminate threats to his dynasty now had a single heir remaining because God had taken the others. The irony was not lost on the Chronicler, who recorded it without comment because the commentary was unnecessary."
    },
    "18": {
      "L": "And after all this the LORD struck him in his bowels with an incurable disease.",
      "M": "After all this, the LORD afflicted Jehoram with an incurable disease of the bowels.",
      "T": "Elijah's letter delivered. The incurable disease — the word 'incurable' (ein marpeh) carried both medical and theological weight: this was not a disease that physicians could treat or that would respond to seeking help from any human source. The same LORD who had given Asa the option of seeking him (and Asa had chosen physicians instead) now gave Jehoram a disease that made the choice moot: there was nothing to seek except God, and God had already rendered the verdict."
    },
    "19": {
      "L": "In the course of time, at the end of two years, his bowels came out because of the disease, and he died in great agony. His people made no fire in his honor, like the fires made for his fathers.",
      "M": "After two years of this, his bowels came out because of his illness, and he died in severe pain. His people did not honor him with a burning of spices, as they had done for his ancestors.",
      "T": "Two years of progressive suffering — exactly as Elijah's letter had promised, 'day by day.' The death was as public and undignified as the life had been faithless. And then the final verdict from the community: no fire. The burning of aromatic spices at a royal death was a mark of honor, the community's public acknowledgment that a faithful king had served his people. Asa had received a 'very great fire' (16:14). Jehoshaphat presumably received the same. Jehoram received nothing. The silence of the bonfire was the people's verdict on the king who had murdered his brothers, imported Baal worship, watched the kingdom shrink, and died of a disease predicted by a dead prophet. The people would not honor what they could not respect."
    },
    "20": {
      "L": "He was thirty-two years old when he began to reign, and he reigned eight years in Jerusalem. And he departed with no one's regret. They buried him in the city of David, but not in the tombs of the kings.",
      "M": "He was thirty-two years old when he became king and reigned eight years in Jerusalem. He passed away, to no one's regret. They buried him in the city of David, but not in the royal tombs.",
      "T": "The most damning two-word epitaph in all of Chronicles: 'to no one's regret.' The Hebrew reads literally 'he walked away without desire' — no one wanted him to stay, no one mourned his departure, no one felt the loss that a beloved king's death produces in a people who have been well served. He was buried in the city of David — the royal city, the city of the covenant — but not in the tombs of the kings. Excluded from the burial ground of his ancestors by the consensus of those who knew what his reign had been. Thirty-two years old when he became king; forty when he died; eight years of damage that would take Jehoshaphat's faithful son and grandson to begin to repair. The valley of Berachah, the Valley of Blessing, was just a chapter earlier. Between a singing army and an unmourned burial, eight years of a king who chose the house of Ahab over the covenant of his fathers."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2chronicles')
        merge_tier(existing, CHRONICLES2, tier_key)
        save(tier_dir, '2chronicles', existing)
    print('2 Chronicles 19–21 written.')

if __name__ == '__main__':
    main()
