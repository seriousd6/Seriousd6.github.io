"""
MKT Echo Layer — 2 Chronicles chapters 32–34
Run: python3 scripts/zc-echo-2chronicles-32-34.py

Ch32: Greater with us than with them (32:7) — 1 John 4:4; arm of flesh vs YHWH (32:8) — 2 Cor 10:4
Ch33: Manasseh's repentance restored him (33:12) — Luke 15:20; prodigal-son pattern
Ch34: Josiah tears clothes at the word of the law (34:19) — Heb 4:12
      Huldah's oracle: because your heart was tender (34:27) — 1 Pet 5:5-6
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
  "32": {
    "7": [
      {"type": "allusion", "target": "1 John 4:4", "note": "Be strong and courageous, do not be afraid or dismayed before the king of Assyria and all the horde that is with him, for there is one greater with us than with him — Hezekiah's encouragement to Jerusalem before Sennacherib's siege is the OT form of 1 John 4:4: 'he who is in you is greater than he who is in the world.' The covenant promise of divine presence surpassing the enemy's power is the consistent ground of courage in both testaments."},
      {"type": "allusion", "target": "Matt 28:20", "note": "With us is YHWH our God to help us and to fight our battles — the promise of divine presence in the face of overwhelming opposition. Christ's closing promise in the Great Commission — 'I am with you always, to the end of the age' — is the new covenant form of Hezekiah's assurance that YHWH is with his people against every Sennacherib."}
    ],
    "8": [
      {"type": "allusion", "target": "2 Cor 10:4", "note": "With him is an arm of flesh, but with us is the LORD our God to help us and to fight our battles — the flesh-vs-Spirit contrast embedded in Hezekiah's battle-speech. 2 Corinthians 10:4: 'the weapons of our warfare are not of the flesh but have divine power to destroy strongholds.' Paul's spiritual warfare theology draws on the same covenant insight: physical power (arm of flesh) is inadequate against the real enemy; divine power (with us is YHWH) is the decisive force."}
    ]
  },
  "33": {
    "12": [
      {"type": "allusion", "target": "Luke 15:20", "note": "When Manasseh was in distress, he entreated the favor of YHWH his God and humbled himself greatly before the God of his fathers — Manasseh's repentance is the most extreme case in the OT: the most notorious and prolonged sinner in the Chronicles narrative turned to God from a Babylonian prison. The pattern matches the prodigal son's return: coming to himself in affliction, humbling himself, returning to the father. Luke 15:20: 'while he was still a long way off, his father saw him and felt compassion, and ran and embraced him.' YHWH was moved by Manasseh's prayer and restored him — the compassion-of-the-father toward the returned prodigal."},
      {"type": "allusion", "target": "1 Tim 1:15", "note": "Manasseh who shed innocent blood, built altars to Baal, burned his children in the valley of Hinnom, and practiced witchcraft — yet was restored through repentance. Paul calls himself the 'foremost' sinner and grounds Christ's saving of him in the same principle: 'Christ Jesus came into the world to save sinners, of whom I am the foremost. But I received mercy for this reason: that in me, as the foremost, Jesus Christ might display his perfect patience as an example to those who were to believe in him' (1 Tim 1:15-16). Manasseh's restoration from the worst of sins is the OT exemplar."}
    ]
  },
  "34": {
    "19": [
      {"type": "allusion", "target": "Heb 4:12", "note": "When the king heard the words of the Law, he tore his clothes — Josiah's immediate physical response to hearing the written word of YHWH demonstrates the covenantal power of Scripture to pierce through accumulated cultural accommodation. Hebrews 4:12: 'the word of God is living and active, sharper than any two-edged sword, piercing to the division of soul and of spirit, of joints and of marrow, and discerning the thoughts and intentions of the heart.' Josiah's torn-clothes response is the OT image of exactly this penetration."}
    ],
    "27": [
      {"type": "allusion", "target": "1 Pet 5:6", "note": "Because your heart was tender and you humbled yourself before God when you heard his words... your eyes shall not see all the disaster that I will bring upon this place — Huldah's oracle preserves the covenantal principle that humility before the divine word averts judgment. 1 Peter 5:6: 'Humble yourselves therefore under the mighty hand of God so that at the proper time he may exalt you.' Josiah's humility does not prevent the exile (which was already decreed) but preserves him from seeing it — the covenant principle that humble response to divine revelation receives divine mercy."},
      {"type": "allusion", "target": "Jas 4:10", "note": "Humble yourself before the LORD and he will exalt you — James 4:10 encapsulates the same covenantal logic Huldah delivers to Josiah: humility before the divine word brings divine mercy. The Chronicler consistently illustrates this principle (Rehoboam in ch 12, Manasseh in ch 33, Josiah here); Huldah's oracle is its most explicit prophetic statement."}
    ]
  }
}

def main():
    e = load_echo('2chronicles')
    merge_echo(e, ECHOES)
    save_echo('2chronicles', e)
    count = sum(len(v) for v in ECHOES.values())
    print(f'2chronicles echo: wrote entries for {count} verses across ch 32-34')

if __name__ == '__main__':
    main()
