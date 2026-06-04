"""
MKT 2 Kings chapters 13–15 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2kings-13-15.py

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L/M throughout; "the LORD" in T.
  Carried forward from all prior 2 Kings scripts.
- H430 (אֱלֹהִים): "God" in all tiers (used as title/description, not personal name).
- H2617 (חֶסֶד): "steadfast love" in M; "covenant loyalty" in T where the context
  is Abraham's covenant (13:23). The word combines loyal obligation with active kindness;
  "steadfast love" is the best English approach in M.
- H1285 (בְּרִית): "covenant" in all tiers (13:23 — covenant with Abraham, Isaac, Jacob
  as the ground of God's restraint from destroying Israel).
- H5315 (נֶפֶשׁ): not prominent in this range; rendered "life" or "person" contextually.
- H7307 (רוּחַ): not present in this range.
- H1697 (דָּבָר): "word" in L/M; T surfaces the force of prophetic word as historical
  causation: 14:25 (Jonah's prophecy enacted decades later by Jeroboam II), 15:12
  (Jehu's 4th-generation promise fulfilled). "The word of the LORD does not fall."
- H5030 (נָבִיא): "prophet" throughout. In 14:25 Jonah ben Amittai is called the prophet
  — this is the same Jonah of the canonical book. T notes the connection.
- H5771/H2399 (עָוֹן/חֵטְא): "sin/iniquity" — the repeated Deuteronomistic formula
  "sins of Jeroboam son of Nebat who made Israel to sin" (13:2,11; 14:24; 15:9,18,24,28)
  is rendered woodenly in L to preserve the formula; M smooths; T notes it as the
  Deuteronomistic verdict that frames the whole period.
- H4428 (מֶלֶךְ): "king" throughout.
- H3467 (יָשַׁע): "save/deliverer" — 13:5 "the LORD gave Israel a deliverer" uses the
  root behind "Jesus/Joshua." L: "a savior"; M: "a deliverer"; T: "a rescuer" or notes
  the salvation register explicitly.
- H2416 (חָיָה): "live/revive" — 13:21 "he revived and stood on his feet" — the dead man
  reanimated by touching Elisha's bones. L: "and he came to life"; M: "he revived";
  T: "life surged back into him — he stood." The verb is the same used for Elisha's own
  revival miracles (4:31-37). T notes the irony: dead Elisha still channels resurrection life.
- Elisha's cry 13:14: "My father, my father! The chariots of Israel and its horsemen!"
  This is verbatim the cry Elisha made over Elijah at the translation (2:12). The king
  applies Elisha's own eulogy back to Elisha. L/M preserve the direct quote. T notes
  the inverted echo: Elisha once cried this over Elijah; now Joash cries it over Elisha.
  The phrase "chariots of Israel and its horsemen" means the prophet was worth more to
  Israel's defense than all its military assets.
- 13:19 "five or six times" — Joash's timid three strikes reveals limited faith/zeal.
  The prophet's anger is not arbitrary; the incomplete obedience limits the divine gift.
  T surfaces this: faith that stops short gets a victory that stops short.
- 14:6: citation of Deut 24:16 is verbatim. This is the only explicit law citation in
  1–2 Kings. Amaziah's restraint is presented as Torah-observance, not merely mercy.
  L preserves the quotation markers; M/T make clear this is scripture fulfillment.
- 14:9 (thistle/cedar fable): a wisdom-genre fable. Jehoash's rebuke uses the form of
  an OT mashal. T renders the condescension of the fable with appropriate irony.
- 14:25-27: Jeroboam II is theologically complex — he is evil but used by God to save.
  The Jonah connection (Jonah 1:1) places this before the canonical book of Jonah.
  T notes: God's salvation of Israel under a wicked king is an act of pure mercy,
  not reward. The phrase "there was none to help Israel" (v26) echoes the desolation
  language of Deut 32:36.
- 15:5 "the LORD struck the king so that he was a leper": contrast with 2 Chronicles
  26:16-21 which explains the cause (Uzziah usurping the priestly role). Kings leaves
  the cause unnamed — the divine judgment stands without explanation. L/M follow Kings
  strictly; T notes the ellipsis and its effect.
- 15:12 fulfillment formula: "This was the word of the LORD that he spoke to Jehu..."
  (cf. 10:30) — the fourth-generation promise is now complete. T notes this is the
  longest-running explicit prophetic fulfillment thread in 1–2 Kings.
- 15:16 Menahem's atrocity at Tiphsah: ripping open pregnant women was a recognized
  war atrocity in the ANE (Amos 1:13; Hos 14:1). L/M render plainly; T notes this
  marks Menahem as in the category of foreign oppressors (Hazael, Aram), not just
  a corrupt king — a northern king now perpetrates against his own people what enemy
  kings did to them.
- 15:19 "Pul king of Assyria" = Tiglath-pileser III (an Assyrian king who used
  the Babylonian throne-name "Pul" or "Pulu"). L preserves "Pul"; M uses both names
  in the note (rendered as "Pul" in the text); T: "Tiglath-pileser" with parenthetical.
- 15:29 Tiglath-pileser's deportation: historically 733–732 BCE, the beginning of
  the end for the northern kingdom. This is the first Assyrian deportation of Israelites.
  T surfaces the theological weight: the covenant curses of Deut 28:64-68 are beginning.
- 15:37 Syro-Ephraimite coalition begins: the opening of the crisis that will dominate
  Isa 7–8. This verse is the Kings signal of that threat. T notes the connection.
- Aspect decisions:
  - Wayyiqtol (waw-consec. imperfects) = narrative past throughout; simple English past.
  - Qatal perfects in prophetic fulfillment notices = completed acts (14:25; 15:12).
  - 13:23 "he would not destroy them, nor has he cast them" — the perfect + negative
    in v23b conveys ongoing present result of past decision; T: "nor has he banished
    them from his presence — not yet."
- H5429 (סְאָה) and other measures: not present in this range.
- Geographical notes:
  - "Valley of Salt" (14:7): SW of Dead Sea; traditional site of Edomite defeats.
  - "Selah" / "Joktheel" (14:7): possibly Petra. Amaziah renames it — a rhetorical act
    of symbolic possession.
  - "Beth-shemesh" (14:11): Judean city near the border — humiliating: Judah defeated
    on its own territory.
  - Lebo-hamath (14:25): northern border marker; the Sea of the Arabah = Dead Sea.
  - Tiphsah (15:16): may be Thapsacus on the Euphrates or a local Israelite town.
  - Tiglath-pileser's deportation list (15:29): Ijon, Abel-beth-maacah, Janoah,
    Kedesh, Hazor, Gilead, Galilee, Naphtali — the far north and east of Israel.
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


TWOKINGS = {
  "13": {
    "1": {
      "L": "In the twenty-third year of Joash son of Ahaziah king of Judah, Jehoahaz son of Jehu began to reign over Israel in Samaria, and he reigned seventeen years.",
      "M": "In the twenty-third year of Joash son of Ahaziah, king of Judah, Jehoahaz son of Jehu began to reign over Israel in Samaria; he reigned seventeen years.",
      "T": "When Joash son of Ahaziah had been king of Judah for twenty-three years, Jehoahaz son of Jehu became king over Israel in Samaria — a reign of seventeen years."
    },
    "2": {
      "L": "And he did evil in the sight of the LORD, and walked after the sins of Jeroboam son of Nebat, who made Israel to sin; he did not depart from them.",
      "M": "He did evil in the sight of the LORD, following the sins of Jeroboam son of Nebat, who made Israel to sin; he did not turn from them.",
      "T": "His reign bore the verdict all the northern kings share: evil in the LORD's sight, locked in the founding apostasy of Jeroboam son of Nebat, whose idolatry had set Israel's course. Jehoahaz did not break free of it."
    },
    "3": {
      "L": "And the anger of the LORD was kindled against Israel, and he gave them into the hand of Hazael king of Syria and into the hand of Ben-hadad son of Hazael, all their days.",
      "M": "So the anger of the LORD burned against Israel, and he gave them into the hand of Hazael king of Syria and into the hand of Ben-hadad son of Hazael, continually.",
      "T": "The LORD's anger against Israel caught fire. For the whole reign of Jehoahaz he handed his people to Hazael king of Syria and then to Hazael's son Ben-hadad — a grinding, multi-generational servitude."
    },
    "4": {
      "L": "Then Jehoahaz sought the favor of the LORD, and the LORD listened to him, for he saw the oppression of Israel, how the king of Syria was oppressing them.",
      "M": "Then Jehoahaz sought the favor of the LORD, and the LORD heard him, for he saw the oppression of Israel — how the king of Syria was oppressing them.",
      "T": "At last Jehoahaz turned to appeal to the LORD's favor. And the LORD heard him — not because Jehoahaz had reformed, but because the LORD saw how savagely the king of Syria was grinding down his people. Divine compassion outran human deserving."
    },
    "5": {
      "L": "And the LORD gave Israel a deliverer, so that they escaped from under the hand of the Syrians; and the children of Israel dwelt in their tents as before.",
      "M": "Therefore the LORD gave Israel a deliverer, so that they escaped from under the power of the Syrians; and the people of Israel lived in their homes as before.",
      "T": "So the LORD sent a deliverer — the word echoes the salvation language of the judges — and Israel slipped free of Syria's grip, and people returned to their homes in the peace of ordinary life."
    },
    "6": {
      "L": "Nevertheless they did not depart from the sins of the house of Jeroboam, who made Israel to sin; they walked in them; and there remained also the Asherah in Samaria.",
      "M": "But they did not turn from the sins of the house of Jeroboam, who made Israel to sin; they continued in them — and the Asherah pole remained standing in Samaria.",
      "T": "The rescue changed nothing in Israel's worship. They kept on in the sins of Jeroboam's house. Worse still, the Asherah pole — the symbol of syncretistic Baal religion — stood untouched in Samaria's capital. Deliverance without repentance."
    },
    "7": {
      "L": "For he had left to Jehoahaz an army of not more than fifty horsemen and ten chariots and ten thousand footmen, for the king of Syria had destroyed them and made them like the dust in threshing.",
      "M": "For Hazael had left Jehoahaz no more than fifty cavalry, ten chariots, and ten thousand foot soldiers; the king of Syria had destroyed the rest and reduced them to dust like the chaff on a threshing floor.",
      "T": "The military situation was catastrophic: fifty cavalry, ten chariots, ten thousand infantry — all that remained after Hazael had ground Israel's army to dust. The threshing-floor image is deliberately humiliating: Israel had been crushed to chaff."
    },
    "8": {
      "L": "Now the rest of the acts of Jehoahaz and all that he did, and his might, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "M": "The rest of the acts of Jehoahaz and all that he did, including his military exploits, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "T": "What more there is to say about Jehoahaz — his deeds, his campaigns — the royal annals hold it."
    },
    "9": {
      "L": "So Jehoahaz slept with his fathers, and they buried him in Samaria; and Joash his son reigned in his place.",
      "M": "Jehoahaz rested with his ancestors and was buried in Samaria; and his son Joash reigned in his place.",
      "T": "Jehoahaz died and was buried in Samaria. His son Joash succeeded him."
    },
    "10": {
      "L": "In the thirty-seventh year of Joash king of Judah, Jehoash son of Jehoahaz began to reign over Israel in Samaria, and he reigned sixteen years.",
      "M": "In the thirty-seventh year of Joash king of Judah, Jehoash son of Jehoahaz began to reign over Israel in Samaria; he reigned sixteen years.",
      "T": "Thirty-seven years into the reign of Joash of Judah, Jehoash son of Jehoahaz took the northern throne in Samaria — ruling for sixteen years."
    },
    "11": {
      "L": "And he did evil in the sight of the LORD; he did not depart from all the sins of Jeroboam son of Nebat, who made Israel to sin; he walked in them.",
      "M": "He did evil in the sight of the LORD; he did not turn from all the sins of Jeroboam son of Nebat, who made Israel to sin; he continued in them.",
      "T": "Another northern king, another identical verdict: evil in the LORD's sight, caught in Jeroboam's gravitational pull. Joash walked the same well-worn path of apostasy."
    },
    "12": {
      "L": "Now the rest of the acts of Joash and all that he did, and his might in fighting against Amaziah king of Judah, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "M": "The rest of the acts of Joash and all that he did, including his military prowess in fighting Amaziah king of Judah, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "T": "The fuller record of Joash — his deeds, his striking military victory over Amaziah of Judah — is preserved in the royal annals."
    },
    "13": {
      "L": "So Joash slept with his fathers; and Jeroboam sat upon his throne. And Joash was buried in Samaria with the kings of Israel.",
      "M": "Joash rested with his ancestors, and Jeroboam sat on his throne. Joash was buried in Samaria among the kings of Israel.",
      "T": "Joash died. His son Jeroboam inherited the throne. Joash was laid in the royal burial ground in Samaria."
    },
    "14": {
      "L": "Now Elisha had fallen sick with the sickness of which he would die. And Joash king of Israel came down to him and wept before him and said, 'My father, my father! The chariots of Israel and its horsemen!'",
      "M": "Now Elisha had become ill with the sickness from which he would die. Joash king of Israel came down to him and wept over him, saying, 'My father, my father! The chariots of Israel and its horsemen!'",
      "T": "Elisha's final illness came. And Joash king of Israel went down to him and wept. The words he cried were Elisha's own words — the eulogy Elisha had spoken over Elijah at the translation (2:12): 'My father, my father! The chariots of Israel and its horsemen!' The king was saying: you were worth more to this nation than all our cavalry. Now we are losing you too."
    },
    "15": {
      "L": "And Elisha said to him, 'Take bow and arrows.' And he took bow and arrows.",
      "M": "Elisha said to him, 'Take a bow and arrows.' So he took a bow and arrows.",
      "T": "Even on his deathbed Elisha was acting the prophet's role. 'Take a bow and arrows,' he said. Joash obeyed."
    },
    "16": {
      "L": "And he said to the king of Israel, 'Draw the bow.' And he drew it. And Elisha laid his hands upon the king's hands.",
      "M": "He said to the king of Israel, 'Draw the bow.' And he drew it. Then Elisha placed his hands on the king's hands.",
      "T": "Elisha had the king draw the bow and then laid his own hands over the king's hands — the prophet's power and intention overlaid on the king's action, as if directing the shot from beyond what strength remained in him."
    },
    "17": {
      "L": "And he said, 'Open the window toward the east.' And he opened it. Then Elisha said, 'Shoot.' And he shot. And he said, 'The LORD's arrow of victory, the arrow of victory over Syria! For you shall strike Syria in Aphek until you have made an end of them.'",
      "M": "He said, 'Open the window to the east.' He opened it. Then Elisha said, 'Shoot.' He shot. And Elisha declared, 'The LORD's arrow of victory — victory over Syria! You shall strike Syria at Aphek until you have destroyed them.'",
      "T": "The window opened eastward — toward Syria. The arrow flew. Elisha named it: 'The LORD's arrow of victory over Syria! You will strike Syria at Aphek until you have finished them.' The act was symbolic prophecy made real: the arrow's release was the LORD's commitment to give Joash complete victory."
    },
    "18": {
      "L": "And he said, 'Take the arrows.' And he took them. And he said to the king of Israel, 'Strike the ground.' And he struck three times and stopped.",
      "M": "Then he said, 'Take the arrows.' He took them. He said to the king of Israel, 'Strike the ground.' He struck it three times and then stopped.",
      "T": "Elisha told the king to strike the ground with the arrows. Joash struck three times. Then he stopped — as if three was enough, or he was uncertain, or simply tired. He did not know that the number of strokes would determine the number of victories."
    },
    "19": {
      "L": "Then the man of God was angry with him and said, 'You should have struck five or six times; then you would have struck Syria until you had made an end of it. But now you shall strike Syria only three times.'",
      "M": "Then the man of God was angry with him and said, 'You should have struck five or six times; then you would have struck down Syria completely. But now you will strike Syria only three times.'",
      "T": "The prophet's anger was sharp. 'Five or six strikes, and Syria would have been finished — wiped out. Three strikes, three victories, and then you stop.' The point is not arbitrary ritual but the revelation of Joash's character: his faith was limited, his zeal incomplete. A victory that stops short mirrors an obedience that stops short."
    },
    "20": {
      "L": "So Elisha died and they buried him. Now bands of Moabites used to invade the land in the spring of the year.",
      "M": "Elisha died and was buried. Now bands of Moabites would raid the land each spring.",
      "T": "Elisha died. They buried him. The flat brevity of it. And then the narrator adds, almost incidentally: every spring, Moabite raiders used to sweep into the land — setting the scene for the story that follows."
    },
    "21": {
      "L": "And it happened as they were burying a man, behold, they saw a raiding band; and they threw the man into the grave of Elisha; and as soon as the man touched the bones of Elisha, he revived and stood on his feet.",
      "M": "Once, as they were burying a man, they saw a raiding band approaching, so they threw the body into Elisha's grave. When the man touched Elisha's bones, he came to life and stood on his feet.",
      "T": "One ordinary burial interrupted by raiders: the mourners threw the corpse into the nearest open tomb — Elisha's — and fled. The dead man's body touched the prophet's bones. Life surged back. He stood up. Even in death, Elisha was a channel of resurrection life. The miracle has no explanation and needs none."
    },
    "22": {
      "L": "Now Hazael king of Syria oppressed Israel all the days of Jehoahaz.",
      "M": "Hazael king of Syria had oppressed Israel throughout the reign of Jehoahaz.",
      "T": "Through all the years of Jehoahaz's reign, Hazael of Syria had been Israel's relentless oppressor — the weight the LORD had placed on them for their apostasy."
    },
    "23": {
      "L": "But the LORD was gracious to them and had compassion on them and turned toward them, because of his covenant with Abraham, Isaac, and Jacob, and would not destroy them nor cast them from his presence, as yet.",
      "M": "But the LORD was gracious to them and had compassion on them; he turned to them for the sake of his covenant with Abraham, Isaac, and Jacob, and would not destroy them or banish them from his presence — not yet.",
      "T": "But the LORD's covenant held. Not because Israel deserved rescue — they did not — but because the LORD had bound himself to Abraham, to Isaac, to Jacob. That ancient, unilateral, oath-sealed covenant was the reason Israel still existed. He would not destroy them. He had not yet cast them from his presence. 'Not yet' is the historian's mercy and warning at once."
    },
    "24": {
      "L": "When Hazael king of Syria died, Ben-hadad his son reigned in his place.",
      "M": "When Hazael king of Syria died, his son Ben-hadad reigned in his place.",
      "T": "Hazael died. His son Ben-hadad took the Syrian throne."
    },
    "25": {
      "L": "Then Jehoash son of Jehoahaz took again from the hand of Ben-hadad son of Hazael the cities which he had taken from the hand of Jehoahaz his father in war. Three times Joash struck him and recovered the cities of Israel.",
      "M": "Then Jehoash son of Jehoahaz took back from Ben-hadad son of Hazael the cities that Hazael had seized from Jehoahaz his father in war. Three times Joash struck him and recovered the cities of Israel.",
      "T": "Elisha's dying prophecy was being fulfilled, exactly. Three strikes — three victories. Joash recovered the cities Syria had stripped from his father. Three times, no more. The prophet's word and the king's limited faith had together set the ceiling on Israel's restoration."
    }
  },
  "14": {
    "1": {
      "L": "In the second year of Joash son of Jehoahaz, king of Israel, Amaziah son of Joash king of Judah began to reign.",
      "M": "In the second year of Joash son of Jehoahaz, king of Israel, Amaziah son of Joash began to reign as king of Judah.",
      "T": "Two years into the reign of Joash of Israel, Amaziah son of Joash became king of Judah."
    },
    "2": {
      "L": "He was twenty-five years old when he began to reign, and he reigned twenty-nine years in Jerusalem. His mother's name was Jehoaddan of Jerusalem.",
      "M": "He was twenty-five years old when he became king, and he reigned twenty-nine years in Jerusalem. His mother's name was Jehoaddan of Jerusalem.",
      "T": "Twenty-five years old at his accession, twenty-nine years on the throne in Jerusalem. His mother was Jehoaddan, a Jerusalem woman."
    },
    "3": {
      "L": "And he did what was right in the eyes of the LORD, yet not like David his father; he did in all respects as Joash his father had done.",
      "M": "He did what was right in the sight of the LORD, yet not as David his father had done; in all respects he followed the example of his father Joash.",
      "T": "His reign earned a qualified commendation: right in the LORD's eyes, but measured against his father Joash rather than against David. The Davidic ideal was the standard; Amaziah did not reach it. He was a decent king, not a great one."
    },
    "4": {
      "L": "Only the high places were not taken away; the people still sacrificed and burned incense on the high places.",
      "M": "However, the high places were not removed; the people continued to sacrifice and burn incense on them.",
      "T": "The standard flaw: the high places stood untouched. Israel's worship remained fractured — the temple in Jerusalem and the local shrines elsewhere, the people's devotion split between them."
    },
    "5": {
      "L": "And it came to pass as soon as the kingdom was firm in his hand, he struck down his servants who had slain the king his father.",
      "M": "As soon as the kingdom was firmly in his grip, he executed the servants who had assassinated his father the king.",
      "T": "Once his hold on power was secure, Amaziah moved against the conspirators who had killed his father — a delayed but deliberate act of royal justice."
    },
    "6": {
      "L": "But the children of the murderers he did not put to death, according to what is written in the Book of the Law of Moses, where the LORD commanded, saying, 'Fathers shall not be put to death for children, and children shall not be put to death for fathers; but each man shall be put to death for his own sin.'",
      "M": "But he did not put the sons of the murderers to death, in keeping with what is written in the Book of the Law of Moses, where the LORD commanded: 'Fathers shall not be put to death for the sins of their children, nor children for the sins of their fathers; each person is to die for his own sin.'",
      "T": "But he stopped short of the customary extension of vengeance to the murderers' sons. This is the only explicit legal citation in the books of Kings, and it is remarkable: Amaziah acted in explicit Torah-obedience, quoting Deuteronomy 24:16. The sons lived. Covenant law constrained royal vengeance — and the narrator marks this as righteousness."
    },
    "7": {
      "L": "He struck down ten thousand Edomites in the Valley of Salt and took Sela by storm, and called its name Joktheel unto this day.",
      "M": "He killed ten thousand Edomites in the Valley of Salt and captured Sela in battle, renaming it Joktheel, which is its name to this day.",
      "T": "Amaziah's military record was solid: ten thousand Edomites slain in the Valley of Salt, and the fortress city of Sela taken by assault. He renamed it Joktheel — 'Subdued by God' — a victory monument in a name. The formula 'to this day' signals a tradition the first readers knew well."
    },
    "8": {
      "L": "Then Amaziah sent messengers to Jehoash son of Jehoahaz son of Jehu, king of Israel, saying, 'Come, let us look one another in the face.'",
      "M": "Then Amaziah sent messengers to Jehoash son of Jehoahaz son of Jehu, king of Israel, saying, 'Come, let us meet each other face to face.'",
      "T": "Success against Edom gave Amaziah ambition he could not afford. He sent a challenge to Jehoash king of Israel — the ANE idiom for 'let us fight.' The phrasing 'look each other in the face' means battle, not a summit."
    },
    "9": {
      "L": "And Jehoash king of Israel sent word to Amaziah king of Judah: 'The thistle that was in Lebanon sent word to the cedar that was in Lebanon, saying, Give your daughter to my son for a wife; and there passed by a wild beast that was in Lebanon and trampled down the thistle.'",
      "M": "Jehoash king of Israel sent back to Amaziah king of Judah: 'A thornbush in Lebanon sent this message to the cedar in Lebanon: Give your daughter to my son as a wife. But a wild animal in Lebanon came by and trampled the thornbush.'",
      "T": "Jehoash's reply was a fable — a mashal dripping with contempt. You are the thornbush; I am the cedar. Your message is absurd on its face. Before the matter could even be settled, something larger came along and crushed you. The story tells Amaziah exactly where he stands in the hierarchy of power — and invites him to step back before he is humiliated."
    },
    "10": {
      "L": "You have indeed struck Edom, and your heart has lifted you up. Boast of it and stay at home, for why should you provoke trouble so that you fall — you and Judah with you?",
      "M": "Yes, you have struck Edom, and it has gone to your head. Be satisfied with your glory and stay home. Why stir up trouble that will only bring you down — you and Judah along with you?",
      "T": "The king of Israel delivers the verdict plainly: Edom was your ceiling. You hit it. Now you want to reach higher and you will collapse. Don't drag Judah down with your overreach. The advice is gracious, even if condescending — and Amaziah was too proud to receive it."
    },
    "11": {
      "L": "But Amaziah would not listen. So Jehoash king of Israel went up, and he and Amaziah king of Judah looked one another in the face at Beth-shemesh, which belongs to Judah.",
      "M": "But Amaziah would not listen. So Jehoash king of Israel advanced, and the two kings faced each other in battle at Beth-shemesh, which belongs to Judah.",
      "T": "Amaziah refused the counsel. The battle was joined at Beth-shemesh — Judean territory. The shame of it: Israel did not even have to invade to fight this battle. Judah brought the war to its own backyard."
    },
    "12": {
      "L": "And Judah was put to rout before Israel, and every man fled to his tent.",
      "M": "Judah was routed by Israel, and every man fled to his home.",
      "T": "The rout was complete. Judah's army broke and scattered, every man running for home. Everything Jehoash had predicted came true in a single day."
    },
    "13": {
      "L": "And Jehoash king of Israel captured Amaziah king of Judah, son of Jehoash, son of Ahaziah, at Beth-shemesh, and came to Jerusalem and broke down the wall of Jerusalem from the Gate of Ephraim to the Corner Gate — four hundred cubits.",
      "M": "Jehoash king of Israel captured Amaziah king of Judah, son of Jehoash, son of Ahaziah, at Beth-shemesh; then he came to Jerusalem and broke down the city wall from the Gate of Ephraim to the Corner Gate — a breach of four hundred cubits.",
      "T": "Amaziah was taken prisoner at Beth-shemesh. Jehoash marched on Jerusalem unopposed, breached its northern wall for four hundred cubits — roughly two hundred meters — from the Gate of Ephraim to the Corner Gate. The holy city stood open, defenseless. This was the depth of what Amaziah's pride had bought."
    },
    "14": {
      "L": "And he took all the gold and the silver and all the vessels that were found in the house of the LORD and in the treasuries of the king's house, and hostages also, and returned to Samaria.",
      "M": "He took all the gold and silver and all the vessels found in the house of the LORD and in the royal treasury, along with hostages, and returned to Samaria.",
      "T": "The temple treasury was plundered, the palace treasury emptied. Hostages were taken — insurance against Judah's future resistance. Then Jehoash turned and walked back to Samaria, laden with Judah's wealth and humiliation."
    },
    "15": {
      "L": "Now the rest of the acts of Jehoash that he did, and his might, and how he fought with Amaziah king of Judah, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "M": "The rest of the acts of Jehoash, his military achievements, and how he fought against Amaziah king of Judah — are they not written in the Book of the Chronicles of the Kings of Israel?",
      "T": "The full record of Jehoash's reign — including this victory over Judah — stands in the annals."
    },
    "16": {
      "L": "And Jehoash slept with his fathers and was buried in Samaria with the kings of Israel, and Jeroboam his son reigned in his place.",
      "M": "Jehoash rested with his ancestors and was buried in Samaria with the kings of Israel; his son Jeroboam reigned in his place.",
      "T": "Jehoash died and was buried in Samaria with his royal predecessors. His son Jeroboam — the second and greatest of that name — succeeded him."
    },
    "17": {
      "L": "And Amaziah son of Joash, king of Judah, lived fifteen years after the death of Jehoash son of Jehoahaz, king of Israel.",
      "M": "Amaziah son of Joash, king of Judah, lived fifteen years after the death of Jehoash son of Jehoahaz, king of Israel.",
      "T": "Amaziah outlived Jehoash by fifteen years — though he had been his captive and had watched his city breached. He lived on, diminished."
    },
    "18": {
      "L": "Now the rest of the acts of Amaziah, are they not written in the Book of the Chronicles of the Kings of Judah?",
      "M": "The rest of the acts of Amaziah — are they not written in the Book of the Chronicles of the Kings of Judah?",
      "T": "What more there was of Amaziah's reign is in the Judean royal annals."
    },
    "19": {
      "L": "And they conspired against him in Jerusalem and he fled to Lachish; but they sent after him to Lachish and killed him there.",
      "M": "They made a conspiracy against him in Jerusalem, and he fled to Lachish, but they sent men after him to Lachish and killed him there.",
      "T": "A conspiracy formed against him in Jerusalem — the same city his father had been murdered in, the same pattern repeating. He fled south to Lachish, but the conspirators tracked him down and killed him there."
    },
    "20": {
      "L": "And they brought him on horses, and he was buried at Jerusalem with his fathers in the city of David.",
      "M": "They brought his body back on horseback, and he was buried in Jerusalem with his ancestors in the city of David.",
      "T": "His body was brought home on horseback and laid with the Davidic kings in Jerusalem — the dignity of royal burial even after an undignified end."
    },
    "21": {
      "L": "And all the people of Judah took Azariah, who was sixteen years old, and made him king in place of his father Amaziah.",
      "M": "Then all the people of Judah took Azariah, who was sixteen years old, and made him king in his father Amaziah's place.",
      "T": "The people of Judah did not wait. They took the sixteen-year-old Azariah and crowned him in his father's place — a popular acclamation signaling relief that the dynasty continued."
    },
    "22": {
      "L": "He built Elath and restored it to Judah, after the king slept with his fathers.",
      "M": "He built up Elath and restored it to Judah, after Amaziah rested with his ancestors.",
      "T": "One of Azariah's early achievements: recovering Elath, the Red Sea port — a strategic prize that expanded Judah's trading access. The detail connects to his long, generally prosperous reign."
    },
    "23": {
      "L": "In the fifteenth year of Amaziah son of Joash, king of Judah, Jeroboam son of Joash, king of Israel, began to reign in Samaria, and he reigned forty-one years.",
      "M": "In the fifteenth year of Amaziah son of Joash, king of Judah, Jeroboam son of Joash became king of Israel in Samaria; he reigned forty-one years.",
      "T": "Fifteen years into Amaziah's reign, Jeroboam II came to the northern throne — and reigned forty-one years. The longest northern reign, and the most politically prosperous, though theologically identical to all his predecessors."
    },
    "24": {
      "L": "And he did evil in the sight of the LORD; he did not depart from all the sins of Jeroboam son of Nebat, who made Israel to sin.",
      "M": "He did evil in the sight of the LORD; he did not turn away from all the sins of Jeroboam son of Nebat, who made Israel to sin.",
      "T": "The verdict is predictable and true: evil in the LORD's sight, another generation locked in Jeroboam's founding idolatry. Prosperity did not produce faithfulness; it never does."
    },
    "25": {
      "L": "He restored the border of Israel from Lebo-hamath as far as the Sea of the Arabah, according to the word of the LORD, the God of Israel, which he spoke through his servant Jonah son of Amittai, the prophet, who was from Gath-hepher.",
      "M": "He restored the territorial borders of Israel from Lebo-hamath to the Sea of the Arabah, in fulfillment of the word of the LORD, the God of Israel, spoken through his servant Jonah son of Amittai, the prophet from Gath-hepher.",
      "T": "And yet: Jeroboam II pushed Israel's northern border all the way back to Lebo-hamath and south to the Dead Sea — the full extent of Solomon's territory. He was not doing this in obedience; he was the unwitting instrument of a prophecy. The prophet who delivered that word was Jonah son of Amittai of Gath-hepher — the same Jonah who would later be sent to Nineveh. Here is what he was doing before that: delivering a word of territorial restoration to a faithless king."
    },
    "26": {
      "L": "For the LORD saw that the affliction of Israel was very bitter, for there was none left, bond or free, and there was no helper for Israel.",
      "M": "For the LORD saw how bitterly Israel was suffering; there was no one left, slave or free, and no one to help Israel.",
      "T": "The reason had nothing to do with Jeroboam's merit. The LORD looked at Israel's condition and saw desperate misery — no one left standing, no one to help them. The same compassion that moved him in the time of the judges moved him here. God's mercy preceded any human response to it."
    },
    "27": {
      "L": "And the LORD had not said that he would blot out the name of Israel from under heaven, so he saved them by the hand of Jeroboam son of Joash.",
      "M": "But the LORD had not said he would blot out the name of Israel from under heaven, so he delivered them through Jeroboam son of Joash.",
      "T": "The theological hinge: the LORD had not yet pronounced the final word of erasure. Israel still had a name, and that name was not yet to be wiped out — so the LORD used a wicked king as his rescuing instrument. Salvation through Jeroboam II was grace in spite of Jeroboam II."
    },
    "28": {
      "L": "Now the rest of the acts of Jeroboam and all that he did, and his might, and how he warred and how he recovered Damascus and Hamath for Judah in Israel, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "M": "The rest of the acts of Jeroboam and all that he did, including his military prowess and how he recovered Damascus and Hamath for Israel, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "T": "The fuller record of Jeroboam II — his campaigns, his recovery of Damascus and Hamath — belongs to the annals. The Kings historian's silence on the prosperity itself is eloquent: what God gives through a faithless king is still God's gift, but the king's wickedness remains the verdict."
    },
    "29": {
      "L": "And Jeroboam slept with his fathers, the kings of Israel, and Zachariah his son reigned in his place.",
      "M": "Jeroboam rested with his ancestors, the kings of Israel, and his son Zachariah reigned in his place.",
      "T": "Jeroboam II died — the last of the Jehu dynasty to die in peace. After him the throne of Israel would become a killing field."
    }
  },
  "15": {
    "1": {
      "L": "In the twenty-seventh year of Jeroboam king of Israel, Azariah son of Amaziah, king of Judah, began to reign.",
      "M": "In the twenty-seventh year of Jeroboam king of Israel, Azariah son of Amaziah became king of Judah.",
      "T": "Jeroboam II had been king of Israel for twenty-seven years when Azariah took the throne of Judah — a reign that would outlast most of his contemporaries."
    },
    "2": {
      "L": "He was sixteen years old when he began to reign, and he reigned fifty-two years in Jerusalem; and his mother's name was Jecoliah of Jerusalem.",
      "M": "He was sixteen years old when he became king, and he reigned fifty-two years in Jerusalem. His mother's name was Jecoliah of Jerusalem.",
      "T": "Sixteen years old at his accession, fifty-two years on the throne — the longest reign in Judah's history since Asa. His mother was Jecoliah, a Jerusalem woman."
    },
    "3": {
      "L": "And he did what was right in the eyes of the LORD, according to all that his father Amaziah had done.",
      "M": "He did what was right in the sight of the LORD, just as his father Amaziah had done.",
      "T": "The same qualified approval his father received: right in the LORD's eyes, but measured by Amaziah rather than David."
    },
    "4": {
      "L": "Nevertheless the high places were not taken away; the people still sacrificed and burned incense on the high places.",
      "M": "However, the high places were not removed; the people still sacrificed and burned incense on the high places.",
      "T": "And still the high places stood. The perennial failure of the Davidic kings — they did much right and left this one thing wrong, and the narrator will not let it pass without note."
    },
    "5": {
      "L": "And the LORD struck the king, so that he was a leper to the day of his death, and he lived in a separate house. And Jotham the king's son was over the household, governing the people of the land.",
      "M": "The LORD struck the king with leprosy, and he remained a leper until the day he died, living in a separate house. Jotham the king's son managed the royal household and governed the people of the land.",
      "T": "Then the LORD struck him — leprosy, isolating, permanent, a king who could not rule in his own palace. Kings does not explain why; 2 Chronicles 26 will fill in that detail. Here the divine judgment stands stark and unexplained: the LORD struck the king. Jotham his son served as regent, running the palace and governing the people, while his father lived out his years in a house apart."
    },
    "6": {
      "L": "Now the rest of the acts of Azariah and all that he did, are they not written in the Book of the Chronicles of the Kings of Judah?",
      "M": "The rest of the acts of Azariah and all that he did — are they not written in the Book of the Chronicles of the Kings of Judah?",
      "T": "Azariah's fuller record — his campaigns, his construction, his administration — is in the Judean annals."
    },
    "7": {
      "L": "So Azariah slept with his fathers and they buried him with his fathers in the city of David; and Jotham his son reigned in his place.",
      "M": "Azariah rested with his ancestors and was buried with them in the city of David; his son Jotham reigned in his place.",
      "T": "Azariah died — having spent perhaps the last decade of his life in isolation — and was buried in Jerusalem with the Davidic kings. Jotham, who had long been acting king, formally succeeded him."
    },
    "8": {
      "L": "In the thirty-eighth year of Azariah king of Judah, Zachariah son of Jeroboam reigned over Israel in Samaria six months.",
      "M": "In the thirty-eighth year of Azariah king of Judah, Zachariah son of Jeroboam reigned over Israel in Samaria for six months.",
      "T": "Thirty-eight years into Azariah's reign, Zachariah son of Jeroboam II took the northern throne. He lasted six months — the fourth and last of Jehu's dynasty."
    },
    "9": {
      "L": "And he did evil in the sight of the LORD as his fathers had done; he did not depart from the sins of Jeroboam son of Nebat, who made Israel to sin.",
      "M": "He did evil in the sight of the LORD, as his ancestors had done; he did not turn from the sins of Jeroboam son of Nebat, who had made Israel to sin.",
      "T": "The formula applies: evil, unbroken continuity with Jeroboam's apostasy, no departure. Six months was enough to qualify for the verdict."
    },
    "10": {
      "L": "And Shallum son of Jabesh conspired against him and struck him before the people and killed him and reigned in his place.",
      "M": "Shallum son of Jabesh conspired against him, struck him down publicly, and killed him; then he reigned in his place.",
      "T": "Shallum son of Jabesh assassinated Zachariah in public — conspicuously, before the people — and seized the throne. The dynasty of Jehu ended in a public killing. What had been promised for four generations now closed."
    },
    "11": {
      "L": "Now the rest of the acts of Zachariah, behold, they are written in the Book of the Chronicles of the Kings of Israel.",
      "M": "The rest of the acts of Zachariah are written in the Book of the Chronicles of the Kings of Israel.",
      "T": "What more there was of Zachariah's brief reign is in the annals."
    },
    "12": {
      "L": "This was the word of the LORD which he spoke to Jehu, saying, 'Your sons shall sit upon the throne of Israel to the fourth generation.' And so it came to pass.",
      "M": "This fulfilled the word of the LORD that he had spoken to Jehu: 'Your descendants will sit on the throne of Israel to the fourth generation.' And so it happened.",
      "T": "The narrator pauses to mark the moment: this is the fulfillment of the LORD's specific promise to Jehu at the purge of Ahab's house (2 Kgs 10:30). Four generations: Jehu, Jehoahaz, Jehoash, Jeroboam II, Zachariah. The word of the LORD had run its full course over more than a century, and it had arrived exactly. The longest explicitly tracked prophetic fulfillment thread in 1–2 Kings now closes."
    },
    "13": {
      "L": "Shallum son of Jabesh began to reign in the thirty-ninth year of Uzziah king of Judah, and he reigned a full month in Samaria.",
      "M": "Shallum son of Jabesh became king in the thirty-ninth year of Uzziah king of Judah, and he reigned one month in Samaria.",
      "T": "One month. Shallum had killed to take the throne and kept it for a month."
    },
    "14": {
      "L": "Then Menahem son of Gadi came up from Tirzah and came to Samaria, and struck Shallum son of Jabesh in Samaria and killed him and reigned in his place.",
      "M": "Then Menahem son of Gadi came up from Tirzah to Samaria, struck down Shallum son of Jabesh, killed him, and reigned in his place.",
      "T": "Menahem marched up from Tirzah — the old northern capital — and killed Shallum in Samaria. The throne of Israel was becoming a prize seized by whoever was willing to kill for it."
    },
    "15": {
      "L": "Now the rest of the acts of Shallum and his conspiracy which he made, behold, they are written in the Book of the Chronicles of the Kings of Israel.",
      "M": "The rest of the acts of Shallum and the conspiracy he carried out are written in the Book of the Chronicles of the Kings of Israel.",
      "T": "Shallum's conspiracy and his one-month reign — the annals hold whatever more there was."
    },
    "16": {
      "L": "Then Menahem struck Tiphsah and all who were in it and its territory from Tirzah, because they did not open to him; therefore he struck it and ripped open all the women in it who were with child.",
      "M": "At that time Menahem struck Tiphsah and all who were in it and its surrounding territory, starting from Tirzah, because they refused to open their gates to him; so he attacked it and ripped open all the pregnant women.",
      "T": "The atrocity that marks Menahem's character: when Tiphsah refused to open its gates to him, he sacked it and ripped open every pregnant woman. This was a recognized war crime in the ancient world — Amos condemns it in Aram (Amos 1:13), Hosea applies it to Israel (Hos 14:1). A northern king was now doing to his own people what foreign enemies had done. The brutality that once came from outside now came from within."
    },
    "17": {
      "L": "In the thirty-ninth year of Azariah king of Judah, Menahem son of Gadi began to reign over Israel, and he reigned ten years in Samaria.",
      "M": "In the thirty-ninth year of Azariah king of Judah, Menahem son of Gadi became king over Israel; he reigned ten years in Samaria.",
      "T": "Menahem reigned ten years — long by the standards of Israel's chaotic final decades — by securing his position through tribute to Assyria rather than through loyalty."
    },
    "18": {
      "L": "And he did evil in the sight of the LORD; he did not depart from the sins of Jeroboam son of Nebat, who made Israel to sin, all his days.",
      "M": "He did evil in the sight of the LORD; he did not turn from the sins of Jeroboam son of Nebat, who made Israel to sin, throughout his days.",
      "T": "Ten years of evil — consistent, unrepentant, locked in the same apostasy. The formula is unchanged; the man is unchanged."
    },
    "19": {
      "L": "Pul king of Assyria came against the land, and Menahem gave Pul a thousand talents of silver, that his hand might be with him to confirm the kingdom in his hand.",
      "M": "Pul king of Assyria invaded the land, and Menahem paid Pul a thousand talents of silver to secure his support and strengthen his grip on the kingdom.",
      "T": "Pul — Tiglath-pileser III of Assyria using his Babylonian throne-name — arrived in Israel's territory. Menahem's response was pragmatic and desperate: a thousand talents of silver to buy Assyrian backing for his reign. He stabilized his throne by mortgaging his kingdom to the empire that would eventually swallow it."
    },
    "20": {
      "L": "And Menahem exacted the silver from Israel, from all the men of wealth, fifty shekels of silver from each man; so the king of Assyria turned back and did not stay in the land.",
      "M": "Menahem raised the silver by taxing every wealthy Israelite fifty shekels of silver each; and the king of Assyria withdrew and did not remain in the land.",
      "T": "The tribute was raised by a direct tax on Israel's landed wealthy — fifty shekels per man. Tiglath-pileser took the money and left. For now. The precedent was set: Israel's survival would depend on satisfying Assyrian appetite, and no amount of tribute could do that indefinitely."
    },
    "21": {
      "L": "Now the rest of the acts of Menahem and all that he did, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "M": "The rest of the acts of Menahem and all that he did — are they not written in the Book of the Chronicles of the Kings of Israel?",
      "T": "Menahem's fuller record is in the annals."
    },
    "22": {
      "L": "And Menahem slept with his fathers, and Pekahiah his son reigned in his place.",
      "M": "Menahem rested with his ancestors, and his son Pekahiah reigned in his place.",
      "T": "Menahem died — one of the few kings of this period to die without being assassinated. His son Pekahiah inherited a kingdom deep in Assyrian debt."
    },
    "23": {
      "L": "In the fiftieth year of Azariah king of Judah, Pekahiah son of Menahem began to reign over Israel in Samaria, and he reigned two years.",
      "M": "In the fiftieth year of Azariah king of Judah, Pekahiah son of Menahem became king of Israel in Samaria; he reigned two years.",
      "T": "Two years. Pekahiah son of Menahem ruled in Samaria for two years before his captain killed him."
    },
    "24": {
      "L": "And he did evil in the sight of the LORD; he did not depart from the sins of Jeroboam son of Nebat, who made Israel to sin.",
      "M": "He did evil in the sight of the LORD; he did not turn from the sins of Jeroboam son of Nebat, who had made Israel to sin.",
      "T": "Two years of the same sin, the same verdict. The Jeroboam pattern held to the end."
    },
    "25": {
      "L": "And Pekah son of Remaliah, his captain, conspired against him, with fifty men of the Gileadites, and struck him in Samaria, in the citadel of the king's house, along with Argob and Arieh; and he killed him and reigned in his place.",
      "M": "Pekah son of Remaliah, his military commander, conspired against him with fifty Gileadite warriors and struck him down in Samaria, in the keep of the palace, together with Argob and Arieh; he killed him and reigned in his place.",
      "T": "Pekah, the army commander, organized a coup — fifty Gileadite soldiers, names attached to the act: Argob and Arieh died with the king or in the taking of the palace. Pekahiah was killed in his own citadel. Pekah took the throne. The cycle of violence in the north was accelerating."
    },
    "26": {
      "L": "Now the rest of the acts of Pekahiah and all that he did, behold, they are written in the Book of the Chronicles of the Kings of Israel.",
      "M": "The rest of the acts of Pekahiah and all that he did are written in the Book of the Chronicles of the Kings of Israel.",
      "T": "What more there was of Pekahiah — the annals preserve it."
    },
    "27": {
      "L": "In the fifty-second year of Azariah king of Judah, Pekah son of Remaliah began to reign over Israel in Samaria, and he reigned twenty years.",
      "M": "In the fifty-second year of Azariah king of Judah, Pekah son of Remaliah became king of Israel in Samaria; he reigned twenty years.",
      "T": "Pekah reigned twenty years — long enough to form the Syro-Ephraimite coalition against Judah and to see Tiglath-pileser deport the northern territories. His ambition outlasted his wisdom."
    },
    "28": {
      "L": "And he did evil in the sight of the LORD; he did not depart from the sins of Jeroboam son of Nebat, who made Israel to sin.",
      "M": "He did evil in the sight of the LORD; he did not turn from the sins of Jeroboam son of Nebat, who had made Israel to sin.",
      "T": "The verdict applies again, identically. The details of Pekah's career will differ from his predecessors — alliances, wars, Assyrian pressure — but the theological verdict is the same: unbroken continuity with the founding apostasy."
    },
    "29": {
      "L": "In the days of Pekah king of Israel came Tiglath-pileser king of Assyria and captured Ijon, Abel-beth-maacah, Janoah, Kedesh, Hazor, Gilead, and Galilee, all the land of Naphtali; and he carried them captive to Assyria.",
      "M": "During the reign of Pekah king of Israel, Tiglath-pileser king of Assyria came and captured Ijon, Abel-beth-maacah, Janoah, Kedesh, Hazor, Gilead, and Galilee — all the land of Naphtali — and deported the people to Assyria.",
      "T": "The empire arrived. Tiglath-pileser — no longer 'Pul' now but named as the world conqueror — swept through the north of Israel: Ijon, Abel-beth-maacah, Janoah, Kedesh, Hazor, the whole of Gilead and Galilee, all of Naphtali's territory. The people were deported to Assyria. This was the first mass exile of Israelites — the covenant curse of Deuteronomy 28:64 beginning its slow fulfillment, starting at the edges and moving toward the center."
    },
    "30": {
      "L": "And Hoshea son of Elah made a conspiracy against Pekah son of Remaliah and struck him and killed him, and reigned in his place, in the twentieth year of Jotham son of Uzziah.",
      "M": "Hoshea son of Elah conspired against Pekah son of Remaliah, struck him down, and killed him; he then reigned in his place, in the twentieth year of Jotham son of Uzziah.",
      "T": "One more assassination. Hoshea son of Elah killed Pekah — the last king to die in the standard way — and took the throne. This was Jotham of Judah's twentieth regnal year. The pattern was now inescapable: northern kings killed and were killed."
    },
    "31": {
      "L": "Now the rest of the acts of Pekah and all that he did, behold, they are written in the Book of the Chronicles of the Kings of Israel.",
      "M": "The rest of the acts of Pekah and all that he did are written in the Book of the Chronicles of the Kings of Israel.",
      "T": "The fuller record of Pekah — his wars, his coalition — is in the annals."
    },
    "32": {
      "L": "In the second year of Pekah son of Remaliah, king of Israel, Jotham son of Uzziah, king of Judah, began to reign.",
      "M": "In the second year of Pekah son of Remaliah, king of Israel, Jotham son of Uzziah became king of Judah.",
      "T": "Two years into Pekah's turbulent reign in Israel, Jotham son of Uzziah formally assumed the Judean throne — having long served as regent during his father's leprosy."
    },
    "33": {
      "L": "He was twenty-five years old when he began to reign, and he reigned sixteen years in Jerusalem; and his mother's name was Jerusha the daughter of Zadok.",
      "M": "He was twenty-five years old when he became king, and he reigned sixteen years in Jerusalem. His mother's name was Jerusha daughter of Zadok.",
      "T": "Twenty-five years old, sixteen years of rule in Jerusalem. His mother was Jerusha daughter of Zadok — a priestly connection in his maternal line."
    },
    "34": {
      "L": "And he did what was right in the eyes of the LORD; he did according to all that his father Uzziah had done.",
      "M": "He did what was right in the sight of the LORD, just as his father Uzziah had done.",
      "T": "The same commendation his father received. Jotham walked in Uzziah's steps — the qualified faithfulness of a king who did much right."
    },
    "35": {
      "L": "Only the high places were not taken away; the people still sacrificed and burned incense on the high places. He built the upper gate of the house of the LORD.",
      "M": "However, the high places were not removed; the people still sacrificed and burned incense on the high places. He built the upper gate of the house of the LORD.",
      "T": "The same flaw, the same formula. Yet alongside the persistent failure of the high places, Jotham built the upper gate of the temple — an act of investment in the proper worship center. The two realities coexisted: the king building the temple, the people sacrificing elsewhere."
    },
    "36": {
      "L": "Now the rest of the acts of Jotham and all that he did, are they not written in the Book of the Chronicles of the Kings of Judah?",
      "M": "The rest of the acts of Jotham and all that he did — are they not written in the Book of the Chronicles of the Kings of Judah?",
      "T": "The fuller record of Jotham's reign is in the Judean annals."
    },
    "37": {
      "L": "In those days the LORD began to send Rezin king of Syria and Pekah son of Remaliah against Judah.",
      "M": "In those days the LORD began to send Rezin king of Syria and Pekah son of Remaliah against Judah.",
      "T": "A single sentence that opens one of the most dangerous moments in Judah's history: the LORD himself began sending Rezin of Syria and Pekah of Israel against Judah. The Syro-Ephraimite war — which will fill Isaiah 7–8 with its drama — begins here, quietly, as a divine initiative. Judah's threat came not from nowhere but from the LORD's hand."
    },
    "38": {
      "L": "And Jotham slept with his fathers and was buried with his fathers in the city of David his father; and Ahaz his son reigned in his place.",
      "M": "Jotham rested with his ancestors and was buried with them in the city of David his father; his son Ahaz reigned in his place.",
      "T": "Jotham died and was buried in the royal tombs of Jerusalem. His son Ahaz succeeded him — inheriting the Syro-Ephraimite threat and the crisis Isaiah will meet at the fuller's field."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2kings')
        merge_tier(existing, TWOKINGS, tier_key)
        save(tier_dir, '2kings', existing)
    print('2 Kings 13–15 written.')

if __name__ == '__main__':
    main()
