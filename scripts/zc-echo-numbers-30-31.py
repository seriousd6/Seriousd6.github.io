"""
Echo — Numbers chapters 30–31
Run: python3 scripts/zc-echo-numbers-30-31.py

Key echoes in this range:
- Num 30:2  → Matt 5:33-37; Jas 5:12 (vow-keeping / Christ's call to simple yes/no integrity)
- Num 30:15 → Heb 7:22; Isa 53:12 (bearing another's iniquity / Christ as guarantor)
- Num 31:3  → Rev 19:2; Rom 12:19 (YHWH's vengeance on Midian / divine justice)
- Num 31:8  → Jude 11; Rev 2:14 (Balaam killed / NT references to Balaam's way)
- Num 31:16 → Rev 2:14 (Balaam's counsel to Midian / false teaching pattern)
- Num 31:21-23 → 1 Cor 3:13; Zech 13:9; Mal 3:2 (metal through fire / testing/refining)
- Num 31:24 → Heb 9:13-14; 1 Pet 1:18-19 (purification after defilement)
- Num 31:50 → Acts 10:4; Rev 8:4 (memorial offering before YHWH)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

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

NUMBERS_ECHOES = {
  "30": {
    "2": [
      {"type": "allusion", "target": "Matt 5:33", "note": "Num 30:2 commands that a man who vows a vow to YHWH must not break his word — he shall do all that proceeds from his mouth. Jesus cites this principle in Matt 5:33-37 and transforms it: rather than requiring oath-fulfillment, he calls his people to a integrity so deep that oaths become unnecessary ('Let what you say be simply Yes or No')."},
      {"type": "allusion", "target": "Jas 5:12",  "note": "James 5:12 echoes Jesus's teaching directly: 'do not swear, either by heaven or by earth or by any other oath, but let your yes be yes and your no be no' — applying the vow-law of Num 30:2 at the level of character rather than mere compliance with oath-keeping rules."}
    ],
    "5": [
      {"type": "theme",    "target": "Heb 7:22",  "note": "When a father disallows a daughter's vow, the vow is nullified — he intervenes to relieve her of the obligation. Heb 7:22 presents Jesus as the 'guarantor' (surety) of a better covenant, standing between his people and the full weight of their covenant obligations, absorbing what they cannot fulfill."}
    ],
    "13": [
      {"type": "theme",    "target": "Eph 5:25",  "note": "A husband may confirm or nullify his wife's vow (Num 30:13-15), bearing the weight of covenant obligations for his household. Ephesians 5:25 presents this authority-as-sacrifice principle in Christ: 'husbands, love your wives, as Christ loved the church and gave himself up for her' — headship defined by self-giving, not self-interest."}
    ],
    "15": [
      {"type": "shadow",   "target": "Isa 53:12", "note": "If a husband says nothing to his wife (approving her vow) but then later annuls it, he bears her iniquity (Num 30:15) — the guilt of her unfulfilled obligation transfers to him. Isaiah 53:12 describes the Servant: 'he bore the sin of many, and makes intercession for the transgressors' — Christ bears the iniquity of his people's unfulfilled covenant obligations."}
    ]
  },
  "31": {
    "2": [
      {"type": "allusion", "target": "Rev 19:2",  "note": "YHWH commands vengeance on Midian for what they did to Israel (Num 31:2-3). Revelation 19:2 declares that God 'has avenged on her the blood of his servants' — the holy war pattern of divine vengeance on those who corrupted YHWH's people finds eschatological fulfillment in Christ's final judgment."},
      {"type": "allusion", "target": "Rom 12:19", "note": "The command to execute YHWH's vengeance (Num 31:2-3) reflects the principle Paul cites in Rom 12:19: 'Vengeance is mine, I will repay, says the Lord' (Deut 32:35). Individual believers are called not to avenge themselves, precisely because YHWH reserves this prerogative — as Numbers 31 demonstrates."}
    ],
    "3": [
      {"type": "shadow",   "target": "Eph 6:12",  "note": "Israel arms for war against Midian 'to execute YHWH's vengeance on Midian' (Num 31:3). Eph 6:12 reframes this for the new covenant community: 'we do not wrestle against flesh and blood, but against the rulers, against the authorities, against the cosmic powers over this present darkness' — holy war is spiritualized but not abandoned."}
    ],
    "6": [
      {"type": "allusion", "target": "Rev 8:6",   "note": "Phinehas goes to war with the holy vessels and the trumpets for the alarm in his hand (Num 31:6). The trumpets that signal both sacred assembly and divine judgment (Num 10:1-10) reappear as the seven trumpets of Rev 8:6 that announce YHWH's final judgments on the enemies of his people."}
    ],
    "8": [
      {"type": "allusion", "target": "Rev 2:14",  "note": "Balaam son of Beor is killed in the Midianite war (Num 31:8). The NT consistently treats Balaam as a type of false teaching motivated by greed. Rev 2:14 warns the church at Pergamum against 'the teaching of Balaam, who taught Balak to put a stumbling block before the sons of Israel.'"},
      {"type": "allusion", "target": "Jude 11",   "note": "Jude 11 invokes Balaam as one of three OT types of apostasy: 'they abandoned themselves for the sake of gain to Balaam's error.' Balaam's death in Num 31:8 is the conclusion of a story that begins in Num 22-24 and becomes a recurring NT symbol of religious compromise for financial reward."}
    ],
    "16": [
      {"type": "allusion", "target": "Rev 2:14",  "note": "Balaam's counsel to Balak — teaching Midianite women to cause Israel to sin at Peor (Num 31:16) — becomes the paradigmatic NT example of false teaching that leads God's people into idolatry and sexual immorality. Rev 2:14 explicitly cites 'the teaching of Balaam' as the pattern of corruption infiltrating the church."}
    ],
    "19": [
      {"type": "type",     "target": "Heb 9:13",  "note": "Soldiers who killed or touched the dead must purify themselves on the third and seventh days with the water of impurity (Num 31:19-20). Heb 9:13-14: 'the blood of goats and bulls, and the sprinkling of defiled persons with the ashes of a heifer, sanctify for the purification of the flesh — how much more will the blood of Christ... purify our conscience from dead works to serve the living God.'"}
    ],
    "21": [
      {"type": "type",     "target": "1 Cor 3:13", "note": "Metals (gold, silver, bronze, iron, tin, lead) must pass through fire to be purified; non-metals pass through water (Num 31:21-23). 1 Cor 3:13: 'each one's work will become manifest, for the Day will disclose it, because it will be revealed by fire, and the fire will test what sort of work each one has done' — the metals-through-fire purification is a type of final judgment."},
      {"type": "allusion", "target": "Zech 13:9",  "note": "The military metal-purification by fire in Num 31:22-23 anticipates Zechariah's covenant-refining oracle: 'And I will put this third into the fire, and refine them as one refines silver, and test them as gold is tested. They will call on my name, and I will answer them' — fire as the instrument of both purification and covenantal testing."},
      {"type": "allusion", "target": "Mal 3:2",    "note": "The fire that purifies metals after battle (Num 31:21-23) foreshadows Malachi's messenger who comes 'like a refiner's fire' (Mal 3:2-3), sitting 'as a refiner and purifier of silver' to purify the sons of Levi. The battle-purification law seeds the prophetic purification imagery."}
    ],
    "23": [
      {"type": "theme",    "target": "1 Pet 1:7",  "note": "What cannot endure fire is purified through water (Num 31:23). 1 Pet 1:7: the testing of faith is 'more precious than gold that perishes though it is tested by fire' — Peter extends the metals-through-fire purification to the spiritual testing of faith, using the same metallurgical framework."}
    ],
    "24": [
      {"type": "allusion", "target": "Heb 9:13",  "note": "Washing garments on the seventh day renders the soldiers clean (Num 31:24). The Levitical purification sequence (death-contact → multiple-day quarantine → water-washing → clean) is the structural framework that Hebrews 9 presents as fulfilled and surpassed by Christ's blood."}
    ],
    "48": [
      {"type": "theme",    "target": "Luke 17:18", "note": "The commanders of thousands and hundreds report to Moses that not one soldier was lost in the battle (Num 31:49) — a miraculous preservation that prompts their thanksgiving offering. The only leper who returned to give thanks (Luke 17:18) reflects the same logic: remarkable preservation calling for explicit gratitude before YHWH."}
    ],
    "50": [
      {"type": "allusion", "target": "Acts 10:4",  "note": "The military officers bring gold as an offering to YHWH 'to make atonement for ourselves before YHWH' (Num 31:50). Acts 10:4: the angel tells Cornelius that his prayers and alms have 'ascended as a memorial before God' — the same concept of offerings and prayers rising to YHWH's presence as a memorial, now applied to a Gentile centurion."},
      {"type": "allusion", "target": "Rev 8:4",    "note": "The gold brought into the tent of meeting 'as a memorial for the people of Israel before YHWH' (Num 31:54) structurally parallels Rev 8:4: 'the smoke of the incense, with the prayers of the saints, rose before God from the hand of the angel' — the memorial-before-YHWH concept finds its eschatological form in the heavenly altar."}
    ],
    "54": [
      {"type": "allusion", "target": "Heb 7:25",  "note": "The gold offering brought before YHWH as a memorial (Num 31:54) reflects the principle of continued priestly intercession keeping Israel in YHWH's remembrance. Heb 7:25: Christ 'always lives to make intercession' for his people — the permanent, living memorial that surpasses the gold brought into the tabernacle."}
    ]
  }
}

def main():
    existing = load_echo('numbers')
    merge_echo(existing, NUMBERS_ECHOES)
    save_echo('numbers', existing)
    for ch in ['30', '31']:
        count = len(existing.get(ch, {}))
        print(f'ch {ch}: {count} verses with echo entries')
    print('Numbers 30-31 echoes written.')

if __name__ == '__main__':
    main()
