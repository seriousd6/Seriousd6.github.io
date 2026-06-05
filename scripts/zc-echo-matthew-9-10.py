"""
Echo layer — Matthew chapters 9–10 (Miracles + Mission Discourse)
Output: data/echoes/matthew.json (adds ch9-10)

Ch9: Healing series — paralytic, Levi's call, hemorrhage + Jairus, blind men, mute demoniac.
Ch10: Mission discourse — the twelve sent out; echoes of Elijah/Elisha mission, Isaiah Servant,
Exodus commissioning, Deuteronomy on household loyalty.
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

ECHOES = {
  "9": {
    "13": [
      {"type": "quote", "target": "Hos 6:6", "note": "I desire mercy and not sacrifice — Matthew's Jesus quotes Hosea 6:6 twice (9:13 and 12:7); the prophetic prioritization of covenant-love over cultic performance grounds Jesus's table-fellowship with sinners"},
      {"type": "allusion", "target": "1 Sam 15:22", "note": "To obey is better than sacrifice — Samuel's prophetic critique of Saul; the same pattern of prioritizing obedience/mercy over sacrifice runs through the prophetic tradition"}
    ],
    "15": [
      {"type": "allusion", "target": "Isa 54:5-6", "note": "The wedding guests cannot mourn as long as the bridegroom is with them — YHWH as Israel's husband and the coming joy; Jesus as the messianic bridegroom whose presence inaugurates the wedding feast"}
    ],
    "27": [
      {"type": "allusion", "target": "Ps 146:8", "note": "Have mercy on us, Son of David — YHWH opens the eyes of the blind (Ps 146:8); the healing of the blind as the fulfillment of the divine-sight-restoring promise"}
    ],
    "36": [
      {"type": "fulfillment", "target": "Ezek 34:5-6", "note": "Sheep without a shepherd — Ezekiel's indictment of Israel's false shepherds who let the flock scatter; Jesus sees the crowd as the lost sheep that the failed shepherds abandoned, and fulfills the role of the true shepherd YHWH promised"}
    ],
    "37": [
      {"type": "allusion", "target": "Isa 27:12", "note": "The harvest is plentiful but the laborers are few — the threshing/gleaning harvest of the nations (Isa 27:12) that requires workers; Jesus frames the mission as harvest-labor for the approaching kingdom-ingathering"}
    ]
  },
  "10": {
    "6": [
      {"type": "allusion", "target": "Ezek 34:16", "note": "The lost sheep of the house of Israel — YHWH promises to seek the lost, bring back the strayed; Jesus sends the disciples to the same lost flock, enacting the Ezekielian shepherd-mission"}
    ],
    "8": [
      {"type": "type", "target": "2 Kgs 4:43-44", "note": "Heal the sick, raise the dead, cleanse lepers — Elisha's miraculous healings and provisions parallel the works Jesus commissions; the disciples are sent as Elisha-like agents of the prophet-king"},
      {"type": "allusion", "target": "Isa 35:5-6", "note": "The blind see and the lame walk — the Isaianic signs of the messianic age; the works Jesus commissions are the exact signs Isaiah listed as the marks of the LORD coming to save"}
    ],
    "15": [
      {"type": "allusion", "target": "Gen 19:24-25", "note": "More tolerable on the day of judgment for Sodom and Gomorrah than for that town — the paradigmatic judgment of Sodom as the measure of culpability for rejecting divine visitation; Capernaum and Bethsaida are greater than Sodom in responsibility"}
    ],
    "19": [
      {"type": "allusion", "target": "Exod 4:12", "note": "Do not be anxious about how or what you are to speak — I will be with your mouth and teach you what to speak; the commissioning of Moses (speech given by God) is the pattern for the disciples' trust under persecution"}
    ],
    "24": [
      {"type": "allusion", "target": "Num 11:29", "note": "A disciple is not above his teacher — Moses wished all the LORD's people were prophets; the master-disciple relationship orders the prophetic community; the disciple shares the teacher's fate"}
    ],
    "28": [
      {"type": "allusion", "target": "Isa 8:12-13", "note": "Do not fear him who can only kill the body — Isaiah warned: do not fear what they fear; fear YHWH alone. Jesus applies the same prophetic courageous-before-men posture to the disciples under persecution"}
    ],
    "29": [
      {"type": "allusion", "target": "Amos 3:5", "note": "Not one sparrow falls to the ground apart from your Father — the wisdom and sovereignty of YHWH who sees even the smallest thing; the sparrow-sale as the measure of providential attention to the disciples"}
    ],
    "34": [
      {"type": "allusion", "target": "Mic 7:6", "note": "I have not come to bring peace but a sword — Micah's warning that a man's enemies are the men of his own house; Jesus cites the household-division as the effect of his coming"}
    ],
    "35": [
      {"type": "quote", "target": "Mic 7:6", "note": "I have come to set a man against his father — Matthew 10:35-36 is a near-quotation of Mic 7:6; the family-division caused by covenant loyalty to Christ mirrors Micah's description of Israel's moral collapse"}
    ],
    "38": [
      {"type": "allusion", "target": "Gen 22:2", "note": "Take up his cross and follow me — the Aqedah pattern: Abraham took the wood of the burnt offering and laid it on Isaac; the disciple takes his own cross (instrument of execution) and walks to his own death following Jesus"}
    ]
  }
}

def main():
    existing = load_echo('matthew')
    merge_echo(existing, ECHOES)
    save_echo('matthew', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Matthew echo: {len(existing)} chapters, {total} verses with connections.')

if __name__ == '__main__':
    main()
