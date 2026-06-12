"""Haggai echo layer — NT allusions and fulfillments for chs 1–2.
Ch2 already has v6 (Heb 12:26-27) and v9 (John 2:21) from the seed script.
This script adds ch1 entries so both chapters have echo coverage.
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

HAGGAI_ECHO = {
  "1": {
    "1": [
      {"type": "allusion", "target": "Matt 1:12", "note": "Zerubbabel the governor of Judah is named in Haggai 1:1 as the civil leader of the restoration community; he appears in Jesus's genealogy (Matt 1:12-13; Luke 3:27): the Davidic line, narrowed to a single governor under Persian rule, flows through Zerubbabel to the Christ; Haggai's investment in Zerubbabel (2:23) is investment in the line that would produce the Messiah"}
    ],
    "13": [
      {"type": "allusion", "target": "Matt 28:20", "note": "Then Haggai, the messenger of the LORD, spoke to the people with the LORD's message: I am with you, declares the LORD — the divine promise of presence to the discouraged restoration community; Jesus closes the Great Commission with the same promise: I am with you always, to the end of the age (Matt 28:20); the Emmanuel-presence announced by Haggai is the ground of mission in both testaments"},
      {"type": "allusion", "target": "Heb 13:5", "note": "I am with you, declares the LORD — the divine promise of presence; Hebrews quotes Deut 31:6 but draws the same assurance: I will never leave you nor forsake you; the pattern of YHWH's presence-promise to his discouraged people (Haggai, Joshua, Gideon) is the OT foundation for the NT's absolute assurance of divine accompaniment"}
    ]
  },
  "2": {
    "23": [
      {"type": "allusion", "target": "John 6:27", "note": "On that day, declares the LORD of hosts, I will take you, O Zerubbabel my servant, the son of Shealtiel, and make you like a signet ring, for I have chosen you — the signet ring is the royal seal, the mark of authority delegated from the king; God the Father set his seal on the Son of Man (John 6:27); Zerubbabel as signet-ring is a type of the Davidic king who is the Father's authorized representative, a type fulfilled in Christ who bears the Father's full authority"}
    ]
  }
}

def main():
    existing = load_echo('haggai')
    merge_echo(existing, HAGGAI_ECHO)
    save_echo('haggai', existing)
    # Report coverage
    ch1_entries = sum(len(v) for v in existing.get('1', {}).values())
    ch2_entries = sum(len(v) for v in existing.get('2', {}).values())
    print(f'  haggai echo: ch1={ch1_entries} entries, ch2={ch2_entries} entries')

if __name__ == '__main__':
    main()
