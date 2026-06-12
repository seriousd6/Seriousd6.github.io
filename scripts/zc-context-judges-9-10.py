"""
MKT Context Commentary — Judges chapters 9–10
Run: python3 scripts/zc-context-judges-9-10.py

Chapters covered:
- Ch9: Abimelech's kingship attempt — Israel's first monarchy experiment, Jotham's
  anti-kingship fable, the covenant-curse fulfillment, the millstone death
- Ch10: Tola and Jair minor judges; the fullest apostasy list (seven nations);
  YHWH's covenant confrontation; divine pathos in v16

Historical/ANE context:
- Ch9: The Shechem covenant context (Gen 34, Josh 24); baal-berith as the
  covenant-deity of Shechem; Baal-Berith temple excavated at Tell Balata;
  Abimelech as the prototype for Israel's rejected kingship models;
  the bramble-fable genre in ANE wisdom literature (Jotham's fable =
  earliest political fable in world literature);
  Thebez and the millstone death — women as unexpected agents of divine justice
- Ch10: The seven foreign deities named — their national identifications;
  ANE god lists in treaty contexts; the covenant-lawsuit form (rîb) in v11-14;
  divine pathos in ancient Near Eastern literature (Lament over Sumer);
  the theological development: YHWH does not immediately rescue but first
  confronts Israel's apostasy — a new element in the cycle
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

CONTEXT = {
  "9": {
    "1": "<p>Abimelech's attempt at kingship in ch9 is the book's central political crisis — the dark mirror image of what legitimate monarchy should be. Shechem had been the site of Jacob's covenant with the Hivites (Gen 34), Joshua's covenant renewal ceremony (Josh 24), and was the location of Joseph's bones (Josh 24:32). It was the most important covenant city in the hill country, making Abimelech's choice of Shechem as his base the deliberate co-opting of covenant sacred space for personal power. The Baal-Berith temple (v4 — 'house of Baal-of-the-Covenant') has been identified archaeologically at Tell Balata (Shechem) with a large Middle Bronze Age migdol-temple (fortress-temple, MB IIC stratum) that continued in use into the Iron Age. The excavations of Ernst Sellin (1913) and later G.E. Wright (1956-73) revealed a massive temple complex with two large standing stones (<em>maṣṣēḇôt</em>) flanking the entrance — the Canaanite cult apparatus.</p>",
    "4": "<p>The funding of Abimelech's coup from the Baal-Berith treasury encodes the book's theological argument: the rejection of YHWH's kingship (8:23 — 'YHWH will rule over you') in favor of a human king is simultaneously a religious apostasy. The temple treasury is being used for political revolution — the entanglement of cultic and political power that Deuteronomy's law of the king (Deut 17:14-20) was designed to prevent. The 'worthless and reckless men' (<em>ʾănāšîm rêqîm ûpōḥăzîm</em>) hired as mercenaries represent the standing army that would become characteristic of monarchy — exactly what Samuel warns Israel about in 1 Sam 8:11-12 ('He will take your sons and appoint them to his chariots and to be his horsemen').</p>",
    "7": "<p>Jotham's fable from Mount Gerizim is the earliest political allegory/fable in world literature. Fable literature (where animals or plants speak and act with human agency to make a moral point) is well-attested in ANE wisdom: the Sumerian 'Dispute between the Hoe and the Plow,' the Akkadian 'Dialogue of Pessimism,' and various Egyptian animal fables predate Jotham. But Jotham's fable is distinctive in its political application — it argues directly that kingship sought by the unworthy will destroy those it claims to protect. The genre makes the argument indirectly (via parable) which allows Jotham to escape before the crowd turns on him (v21 — 'he fled and escaped to Beer'). Gerizim as the platform is maximally ironic: the blessing-mountain of Deut 11:29 and Josh 8:33 becomes the site of a curse-pronouncement.</p>",
    "23": "<p>'God sent an evil spirit between Abimelech and the lords of Shechem' — the theological claim is that YHWH works through fractured human relationships to execute covenant justice. The 'evil spirit from God' (<em>rûaḥ rāʿāh mēʾēt hāʾĕlōhîm</em>) parallels the evil spirit that will trouble Saul (1 Sam 16:14) — a divine judicial instrument that removes the 'good spirit' of governance and replaces it with suspicion, treachery, and destruction. Ancient Near Eastern political literature understood divine withdrawal or anger as the explanation for the collapse of kingdoms (the Lament over Sumer and Ur, ca. 2000 BCE, describes Enlil's decision to destroy Ur as divine will being worked through Amorite invaders). The Deuteronomistic Historian uses the same pattern: covenant betrayal → YHWH removes his protection → the natural consequences of ungodly rule destroy the ungodly ruler.</p>",
    "53": "<p>The millstone death of Abimelech at Thebez is the fulfillment of Jotham's curse (v20: 'fire come out from the men of Shechem and consume Abimelech; and fire come out from Abimelech and consume the men of Shechem'). The city of Thebez (<em>ṯēḇēṣ</em>, H8405) is identified with modern Tubas, northeast of Nablus in the central hill country. The detail that a woman's hand delivers the fatal blow from a tower creates the book's second woman-with-domestic-implement victory (Jael: tent peg; anonymous woman: millstone). Both deaths of enemy leaders by women follow YHWH's pattern of reversing human expectations: the mighty general, the aspiring king — both killed by the most unexpected possible agent. This pattern is theologically deliberate: YHWH's deliverances do not come through conventional military heroism.</p>"
  },
  "10": {
    "6": "<p>The seven-nation apostasy list in v6 is the most comprehensive enumeration of foreign gods in Judges, spanning the entire political geography of Israel's neighbors: Baals (Canaanite storm deity), Ashtaroth (Canaanite goddess of fertility and war), gods of Aram (Syrian pantheon, primarily Hadad/Ben-Hadad), gods of Sidon (Phoenician pantheon, primarily Baal and Asherah), gods of Moab (primarily Chemosh — the Mesha Stele confirms Chemosh as Moab's national deity), gods of Ammon (primarily Milcom/Molech), gods of the Philistines (primarily Dagon — confirmed by the Ugaritic texts and the later Temple of Dagon at Ashdod in 1 Sam 5). The geographic span — Syria to the north, Phoenicia to the northwest, Moab and Ammon to the east, Philistia to the west — means Israel has worshiped the gods of every surrounding people simultaneously. This total syncretism is the culmination of the progressive apostasy the book has been documenting.</p>",
    "11": "<p>YHWH's covenant-lawsuit speech in vv11-14 is the most confrontational divine address in Judges. The speech form is the <em>rîḇ</em> (covenant lawsuit) — YHWH speaks as the wronged covenant-lord to the unfaithful vassal. The historical recital in v11-12 is evidence: 'Did I not save you from the Egyptians and from the Amorites, from the sons of Ammon and from the Philistines? The Sidonians also, and Amalek and Maon oppressed you, and you cried out to me, and I saved you from their hand.' The recital of past deliverance makes the current apostasy inexcusable — Israel has received covenant benefits and then abandoned the covenant party who provided them. This is the same pattern as the prophets' lawsuits: 'What more could I have done for my vineyard?' (Isa 5:4).</p>",
    "14": "<p>YHWH's sarcastic dismissal — 'Go and cry out to the gods whom you have chosen; let them save you in the time of your distress' — is unprecedented in Judges. Prior cycles moved directly from Israel's cry to YHWH's compassion and action (2:18 — 'When YHWH raised up judges for them, YHWH was with the judge, and he saved them from the hand of their enemies all the days of the judge, for YHWH was moved to pity by their groaning'). Here the compassion is withheld and replaced by divine sarcasm. This represents a theological development within the book's cycle: YHWH is not a vending machine for salvation but a covenant person whose patience has been exhausted. The episode anticipates the NT teaching that it is possible to 'grieve the Holy Spirit' (Eph 4:30) — divine patience is genuine, not infinite.</p>",
    "16": "<p>'And they put away the foreign gods from among them and served YHWH, and he became impatient over the misery of Israel.' The divine pathos expressed here — YHWH's soul being 'shortened/distressed' (<em>wattiqqṣar napšô</em>) over Israel's <em>ʿāmal</em> (misery/toil) — is one of the OT's most striking expressions of divine inner life. The verb <em>qāṣar</em> with <em>nepeš</em> means to feel constrained, impatient, grieved — the same idiom appears in Num 21:4 where Israel's 'soul was impatient' on the wilderness journey. YHWH's inner emotional response to Israel's suffering is emphasized across the prophets (Isa 63:9 — 'In all their affliction he was afflicted'; Jer 31:20 — 'my heart yearns for him; I will surely have mercy on him'). The ANE comparative literature on divine emotion (the Mesopotamian Laments describe the gods' anguish over destroyed cities) shows that expressing divine pathos was a recognized theological category — but Israel's tradition uniquely roots it in covenant relationship rather than impersonal fate.</p>"
  }
}

def main():
    c = load_comm('mkt-context', 'judges')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', 'judges', c)
    print(f'judges mkt-context: wrote {sum(len(v) for v in CONTEXT.values())} verses across ch 9-10')

if __name__ == '__main__':
    main()
