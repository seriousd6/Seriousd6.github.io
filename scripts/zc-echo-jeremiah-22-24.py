"""
MKT Echo Commentary — Jeremiah chapters 22–24
Run: python3 scripts/zc-echo-jeremiah-22-24.py

Key echo anchors:
- Jer 22:3   social justice triad (foreigner, fatherless, widow) → Matt 25:31-46;
  Luke 4:18; Jas 1:27 — this triad runs from Deut through the prophets into Christ's
  explicit criteria for the final judgment
- Jer 22:5   "this house will become a ruin" → Matt 23:38 (Jesus departs the temple
  declaring "your house is left to you desolate" — same desolation oracle)
- Jer 22:16  "to know me" = defending the poor → John 17:3; 1 John 2:3-4 — knowing
  God defined by obedience-as-love, not by mystical experience
- Jer 22:30  Coniah/Jeconiah "childless" regarding the throne → Matt 1:11-12 / Luke
  3:27 — the Matthean legal line passes through the cursed Jeconiah while Luke's
  biological line bypasses it through Nathan; Christ fulfills the Davidic promise
  without carrying the curse
- Jer 23:5-6 the righteous Branch / YHWH-Tzidkenu → 1 Cor 1:30; 2 Cor 5:21 —
  the most explicitly messianic text in Jeremiah; NT identifies Christ as the Branch
  who is righteousness for his people
- Jer 23:29  "my word like fire, like a hammer" → Heb 4:12; Rev 19:15 — the word's
  power is personified in Christ, the living Word
- Jer 24:7   "a heart to know me" / covenant formula → Heb 8:10; 2 Cor 4:6 —
  anticipates the new covenant promise of Jer 31 already in ch24
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    """Merge echo entries; deduplicate by (type, target) within each verse."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))

JEREMIAH_ECHO = {
  "22": {
    "3": [
      {"type": "theme", "target": "Matt 25:31-46", "note": "The triad of justice — foreigner, fatherless, widow — that YHWH commands Judah's king to protect reappears in Jesus's criteria for the final judgment: feeding the hungry, welcoming the stranger, caring for the sick. The prophetic social-justice demand is fulfilled in Christ's identification with 'the least of these.'"},
      {"type": "allusion", "target": "Luke 4:18", "note": "Jesus's inaugural sermon in Nazareth — good news to the poor, freedom for the oppressed, release for the captive — is the announcement of the messianic reign that Jeremiah's justice command pointed toward; the king who 'does what is just and right' is now identified as the anointed one himself."},
      {"type": "allusion", "target": "Jas 1:27", "note": "Pure religion is looking after orphans and widows in their distress — James echoes the prophetic justice triad of Jer 22:3 (and Deut 10:18; Isa 1:17); the covenant obligation runs from Moses through the prophets into the practical ethics of the new covenant community."}
    ],
    "5": [
      {"type": "allusion", "target": "Matt 23:38", "note": "This house will become a ruin — Jesus departs the Jerusalem temple saying 'your house is left to you desolate,' applying the same palace/house desolation oracle to the second temple that Jeremiah applied to the first; the pattern of covenant house abandoned because of unfaithfulness repeats in the rejection of Messiah."}
    ],
    "16": [
      {"type": "allusion", "target": "John 17:3", "note": "Is that not what it means to know me? — knowing YHWH is defined by defending the cause of the poor; Jesus defines eternal life as knowing the Father and the Son he sent (John 17:3), and John's first letter extends this: those who do not love their brothers and sisters do not know God (1 John 4:8); knowing God as relational obedience, not theoretical assent."},
      {"type": "allusion", "target": "1 John 4:8", "note": "Knowing YHWH = doing justice — Jer 22:16 makes knowledge of God practical and ethical; John's formulation that 'whoever does not love does not know God' is the NT compression of the same principle; the one who perfectly knows the Father is the one who perfectly embodied this justice (Matt 12:17-21)."}
    ],
    "29": [
      {"type": "allusion", "target": "Matt 1:11-12", "note": "Record this man as childless — no descendant of his will sit on David's throne; yet Matthew's genealogy of Jesus (Matt 1:11-12) passes through Jeconiah/Coniah, carrying the royal legal lineage to Christ while Luke's genealogy (3:27) bypasses Jeconiah through Nathan's line; both lines converge in Jesus who is legally Davidic through Joseph and biologically Davidic through Mary, fulfilling the throne-promise without activating the throne-curse on his descendants."}
    ]
  },
  "23": {
    "1": [
      {"type": "allusion", "target": "John 10:11-16", "note": "Woe to the shepherds who destroy and scatter the sheep — Jeremiah's oracle against faithless leaders introduces the true-shepherd promise of vv3-4; Jesus explicitly identifies himself as the good shepherd who gathers what the bad shepherds scattered and lays down his life for the sheep; John 10 is the NT fulfillment of the Jeremiah/Ezekiel shepherd sequence."},
      {"type": "allusion", "target": "Ezek 34:2-10", "note": "The shepherd oracle of Jer 23:1-4 is closely parallel to and anticipates Ezekiel 34's extended shepherds oracle; both condemn the same faithless leaders and both promise YHWH's direct intervention to gather and care for the flock — a promise fulfilled in Christ, the one shepherd (John 10:16)."}
    ],
    "5": [
      {"type": "fulfillment", "target": "Matt 2:23", "note": "I will raise up for David a righteous Branch (Hebrew tsemach, 'branch' or 'shoot') — the Messianic title 'Branch' appears also in Isa 4:2; Zech 3:8; 6:12; the early church connected Jesus the Nazarene (from Nazareth) with the tsemach/netzer Branch tradition; Matthew's 'he shall be called a Nazarene' (Matt 2:23) likely invokes this prophetic tradition."},
      {"type": "fulfillment", "target": "Luke 1:32-33", "note": "The righteous Branch who will reign wisely and do justice and righteousness — the Davidic king who reigns with wisdom and justice is the figure Gabriel announces to Mary: 'the Lord God will give him the throne of his father David, and he will reign over Jacob's descendants forever'; Luke 1:32-33 is the explicit NT fulfillment of the Branch-king promise."}
    ],
    "6": [
      {"type": "fulfillment", "target": "1 Cor 1:30", "note": "YHWH Tsidkenu — 'The LORD Our Righteousness' is the name given to the coming messianic king; Paul's identification of Christ as the one 'who has become for us wisdom from God — that is, our righteousness, holiness, and redemption' (1 Cor 1:30) is the NT claim that Jesus is YHWH Tsidkenu; the Messianic name of Jer 23:6 is applied to Christ himself."},
      {"type": "fulfillment", "target": "2 Cor 5:21", "note": "The LORD Our Righteousness — God made Christ who had no sin to be sin for us, so that in him we might become the righteousness of God (2 Cor 5:21); Paul's exchange formula is the fulfillment of the Jeremiah promise: the Branch king provides righteousness not merely by reigning rightly but by being made sin so that his people receive his righteousness."}
    ],
    "18": [
      {"type": "allusion", "target": "Rev 5:1-5", "note": "Who has stood in the LORD's council to see and hear his word? — Jeremiah's diagnostic of the false prophets: they had not stood in YHWH's council; Revelation presents Christ as the only one found worthy to stand before the throne and open the sealed scroll (Rev 5:5, 9); he alone has stood in the divine council and has authority to speak and enact YHWH's purposes."}
    ],
    "23": [
      {"type": "allusion", "target": "Acts 17:28", "note": "Am I only a God nearby, and not a God far away? — YHWH's declaration of omnipresence (heaven and earth full of him, v24) is the OT ground for Paul's Areopagus proclamation: 'in him we live and move and have our being' (Acts 17:28); the God who fills heaven and earth is the same in whom all creaturely existence subsists."}
    ],
    "29": [
      {"type": "allusion", "target": "Heb 4:12", "note": "Is not my word like fire, like a hammer that shatters rock? — the active, powerful, penetrating word of God described in Jeremiah is the foundation for Hebrews' description of the word of God as alive and active, sharper than a double-edged sword, piercing even to the division of soul and spirit; Heb 4:12-13 extends the fire-and-hammer imagery to its full personified form in the living word."},
      {"type": "allusion", "target": "Rev 19:15", "note": "The word like fire — in Revelation, from the mouth of the rider on the white horse (Christ) comes a sharp sword with which he strikes down nations; Rev 19:15 is the eschatological enactment of Jer 23:29: the word-as-weapon that Jeremiah described is now wielded by the incarnate Word himself in his final advent."}
    ]
  },
  "24": {
    "7": [
      {"type": "fulfillment", "target": "Heb 8:10", "note": "I will give them a heart to know me, that I am the LORD. They will be my people and I will be their God, for they will return to me with all their heart — this is the new covenant formula that Jer 31:31-34 will state explicitly; Heb 8:10-12 quotes Jer 31 as the charter of the new covenant, but ch24 already anticipates it: the transformed heart and restored covenant relationship that Jesus seals with his blood."},
      {"type": "allusion", "target": "2 Cor 4:6", "note": "A heart to know me — God who said let light shine out of darkness has made his light shine in our hearts to give us the knowledge of the glory of God in the face of Christ (2 Cor 4:6); the heart-knowledge of YHWH that Jer 24:7 promises as the fruit of discipline is given in Christ, the face of God now visible."},
      {"type": "allusion", "target": "Ezek 36:26", "note": "A heart to know me — Jer 24:7 anticipates the new heart promise that Ezekiel will develop: I will give you a new heart and put a new spirit in you; I will remove from you your heart of stone and give you a heart of flesh (Ezek 36:26); both prophets point to the same Spirit-worked inner transformation that the new covenant delivers."}
    ]
  }
}


def main():
    existing = load_echo('jeremiah')
    merge_echo(existing, JEREMIAH_ECHO)
    save_echo('jeremiah', existing)
    print('Jeremiah 22–24 echo written.')


if __name__ == '__main__':
    main()
