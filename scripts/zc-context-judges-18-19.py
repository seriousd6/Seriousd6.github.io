"""
MKT Context Commentary — Judges chapters 18–19
Run: python3 scripts/zc-context-judges-18-19.py

Chapters covered:
- Ch18: Danite migration — the tribe's failed settlement, their northward migration,
  the plundering of Micah's shrine, the conquest of Laish/Dan, the establishment
  of an idolatrous northern cult that will persist until the Assyrian exile
- Ch19: The Levite's concubine — the Gibeah atrocity, the Sodom parallel,
  the 12-piece summons, the moral nadir of the judges period

Historical/ANE context:
- Ch18: Dan's migration is corroborated by the shift from coastal to northern
  Dan in the tribal traditions; Laish/Leshem = Tell Dan, excavated by A. Biran
  (1966-1999); the Dan stele (Tel Dan stele, ca. 841 BCE) mentions the "House
  of David" — same city; the Danite cult at Dan is condemned by the later
  prophets and persists until the Assyrian conquest (722 BCE)
- Ch19: The Gibeah narrative deliberately echoes Gen 19 (Sodom); the question
  of whether this is literary typology or sequential source is debated;
  Benjamin's subsequent near-annihilation (ch20-21) shows covenant consequences;
  the Levite's act (12-piece summons) employs the covenant-animal-cutting idiom;
  hospitality failure in ANE context (xenia obligation);
  the geographical detail (Gibeah = Tell el-Ful, excavated by W.F. Albright)
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
  "18": {
    "1": "<p>Chapter 18 marks the historical beginning of the northern Dan cult — the idolatrous shrine that will anchor Jeroboam's golden calf worship at Dan after the kingdom splits (1 Kgs 12:29-30). The archaeological site of Tell Dan (ancient Laish/Dan, in the far north near the headwaters of the Jordan) was excavated by Avraham Biran from 1966-1999. The excavations revealed a massive Iron Age I destruction layer consistent with a violent conquest, above which Iron Age II cultic installations including a large high-place (<em>bāmāh</em>) were found — consistent with the Danite cult described here and with Jeroboam's later installation. The famous Tel Dan Stele (ca. 841 BCE), discovered in 1993-94, bears the inscription 'House of David' (<em>byt dwd</em>) — the oldest extrabiblical reference to the Davidic dynasty, confirming the city's importance as a northern political center throughout the monarchic period.</p>",
    "7": "<p>Laish is described as dwelling 'in the manner of the Sidonians, quiet and unsuspecting' — a dependency on Phoenician cultural patronage without military protection. The Sidonians (<em>ṣiḏōnîm</em>) were the dominant Phoenician coastal power in this period; Laish's cultural orientation toward Sidon rather than the surrounding Aramean or Israelite powers left it isolated from regional defensive networks. The archaeological record at Tell Dan shows Late Bronze Age Canaanite culture with Phoenician influence, consistent with the text's description. The phrase 'far from Sidon and had no dealings with anyone' (<em>ûmiddāḇār ʾên lāhem ʿim-ʾādām</em>) describes a prosperous but isolated community — exactly the kind of soft target that a landless tribe would identify in a reconnaissance mission.</p>",
    "14": "<p>The Danites' decision to plunder Micah's shrine (an ephod, teraphim, graven image, and molten image) is presented as tactical pragmatism: they want divine authorization and cultic apparatus for their new city. The pattern of stolen cult objects migrating with conquered peoples is well-documented in the ANE — the Ark of the Covenant being captured by the Philistines (1 Sam 4-6) represents the same category of thinking: possess the cult object, possess the deity's presence. The Danites' reasoning is identical to Micah's earlier logic (17:13 — 'now I know YHWH will prosper me, since I have a Levite as priest'): procedural correctness substitutes for covenant faithfulness. The tribe that could not hold its allotment by covenant obedience now attempts to secure prosperity through appropriated sacred objects.</p>",
    "30": "<p>The genealogical revelation that the Danite priest is Jonathan son of Gershom son of Moses is one of the most theologically charged moments in the book. The scribal tradition of inserting a <em>nun</em> into the name to read 'Manasseh' instead of 'Moses' (found in many manuscripts) reflects later discomfort with Moses's direct descendant becoming the founding priest of an idolatrous shrine. The Masoretic text preserves the original reading 'Moses' with a superscript nun — the rabbis used a device called <em>tiqqun sopherim</em> (scribal correction) to protect Moses's honor while preserving the original. That Moses's grandson founded the Danite idol cult within a generation of the Exodus is the book's most devastating single datum: covenant apostasy can penetrate to the founder's own family line. The priesthood continues 'until the day of the exile of the land' — the Assyrian conquest of 722 BCE (2 Kgs 17:5-6), confirming the narrative's historical horizon.</p>",
    "31": "<p>'They set up Micah's carved image for themselves all the days that the house of God was at Shiloh.' The parallel existence of the Danite idolatrous shrine and the legitimate tabernacle at Shiloh is the theological summary of the appendix chapters: while YHWH maintained his covenant presence at Shiloh, apostasy proliferated simultaneously and without challenge. Shiloh (<em>šîlōh</em>) served as the central sanctuary from the Judges period until its destruction, probably by the Philistines after the battle of Eben-ezer (1 Sam 4) around 1050 BCE. Jeremiah later uses Shiloh's destruction as a warning to Jerusalem (Jer 7:12-14; 26:6) — 'Go to my place that was at Shiloh, where I made my name dwell at first, and see what I did to it because of the evil of my people Israel.' The fall of Shiloh is the moment at which Israel's tabernacle-centered covenant worship was permanently disrupted.</p>"
  },
  "19": {
    "1": "<p>Chapter 19 is deliberately constructed as an anti-Sodom narrative, using the Gen 19 account as a literary template to show that an Israelite city has become as morally depraved as the city destroyed by divine fire. The parallels are exact: a visitor lodges in the city square → a righteous resident offers hospitality → the men of the city demand the male guest for sexual violation → the host offers women in the guest's place → the women are violated instead. The literary echo is unmistakable and theologically devastating: Sodom was not a covenant people. Benjamin, descended from Jacob's twelfth son, is Israel. The question the chapter poses is: how is an Israelite city morally worse than Sodom? The answer: because Israel had the covenant, the law, and the tabernacle, and still produced Gibeah.</p>",
    "15": "<p>Gibeah (<em>giḇʿāh</em>) has been identified with Tell el-Ful, excavated by W.F. Albright in 1922-23 and again in 1933. The site revealed a significant Iron Age I fortress-type structure (Albright's 'Fortress I,' ca. 1200-1100 BCE) — consistent with a Benjaminite stronghold of the Judges period. The same site later became Saul's residence as first king (1 Sam 10:26; 15:34). The irony that Saul's hometown is Gibeah of the outrage will haunt the Saul narratives: the first king comes from the city of Benjamin's deepest shame, and his kingship will end in shameful defeat. The failure of hospitality at Gibeah (no one offered lodging, v15) contravenes the fundamental social obligation of the ANE: <em>xenia</em> (Greek) or its Semitic equivalent — the host-guest relationship that protected travelers in a world without public inns or police protection.</p>",
    "22": "<p>The Sodom parallel is made structurally explicit here: men of the city surround the house, demanding the male guest for sexual violation — exactly Gen 19:4-5. The phrase <em>bənê bəliyyaʿal</em> (sons of Belial/worthlessness) is the characterization of those who operate entirely outside covenant norms (1 Sam 2:12 — Eli's sons; 2 Sam 20:1 — Sheba who leads rebellion against David; 1 Kgs 21:10 — the false witnesses against Naboth). Gibeah is not an isolated incident of individual sin but a community-level breakdown where the most fundamental social-moral category (<em>bəliyyaʿal</em> = absolute worthlessness, no positive value remaining) describes the majority of the city's adult males. The demand to 'know' (<em>yāḏaʿ</em>, the sexual euphemism of Gen 4:1 and Gen 19:5) connects Gibeah to the Sodom tradition beyond any doubt.</p>",
    "29": "<p>The 12-piece dismemberment of the concubine and sending to all Israel's territories is the narrative's final act of shock — and it is also a recognized legal-political summons mechanism. The covenant-animal-cutting ceremony (Gen 15:10,17; Jer 34:18) involved cutting an animal in half so the covenant parties passed between the pieces, invoking the same fate on themselves if they violated the covenant. The 12 pieces corresponding to the 12 tribes is a territorial summons that invokes tribal covenant solidarity: what has been done in Benjamin's territory is a covenant violation that demands a response from all 12 parties. The Saul parallel (1 Sam 11:7) is exact — Saul cuts his oxen in 12 pieces and sends them through Israel to summon the tribes to Jabesh-gilead's defense, using the identical gesture. The Levite's act is thus not merely macabre but legally precise: he is invoking the covenant justice mechanisms of Israel's tribal confederation.</p>",
    "30": "<p>'Nothing like this has happened or been seen from the day the children of Israel came up from the land of Egypt until this day.' The historical hyperbole — this is the worst thing since the Exodus — is the narrator's verdict on the entire Judges period. The Exodus framing is deliberate: the book began with a generation that forgot the Exodus (2:10) and ends with an event that surpasses in horror anything that occurred under Egypt's oppression. Israel's self-inflicted moral catastrophe exceeds what her oppressors did to her. The call to 'set your heart to it, take counsel, and speak' is an invitation to covenant response: the tribal assembly will meet at Mizpah (20:1) to decide what to do. Whether Israel can still function as a covenant people in response to this internal atrocity is the question ch20-21 will answer — partially and tragically.</p>"
  }
}

def main():
    c = load_comm('mkt-context', 'judges')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', 'judges', c)
    print(f'judges mkt-context: wrote {sum(len(v) for v in CONTEXT.values())} verses across ch 18-19')

if __name__ == '__main__':
    main()
