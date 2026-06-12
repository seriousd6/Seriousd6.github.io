"""
MKT Echo Data — 2 Kings chapters 1–3
Run: python3 scripts/zc-echo-2kings-1-3.py

Ch1: Elijah calls fire from heaven — Luke 9:54-56 (disciples rebuke / Jesus rebukes them)
Ch2: Elisha's double-portion Spirit request — Acts 2:4 / John 14:12;
     Elisha takes the mantle — Acts 1:8 (Spirit's continuity beyond the individual prophet)
Ch3: Valley filled with water without visible source — John 7:37-39 (rivers of living water)
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

ECHO = {
  "1": {
    "10": [
      {"type": "allusion", "target": "Luke 9:54-56", "note": "Elijah called fire down from heaven twice (vv10, 12) to consume the captain and his fifty — when the disciples James and John ask Jesus 'Lord, do you want us to tell fire to come down from heaven and consume them?' (in imitation of Elijah), Jesus rebukes them: 'You do not know what manner of spirit you are of; for the Son of Man did not come to destroy people's lives but to save them.' Jesus explicitly contrasts his mission with Elijah's fire-calling, marking a decisive shift in the use of prophetic power in the messianic age."}
    ]
  },
  "2": {
    "9": [
      {"type": "allusion", "target": "John 14:12", "note": "Elisha's request for a double portion of Elijah's spirit — asking to be the primary heir and successor of the prophetic power — anticipates Jesus's promise to the disciples: 'whoever believes in me will also do the works that I do; and greater works than these will he do, because I am going to the Father.' The double-portion principle (the heir receives more than the predecessor) is fulfilled in the outpouring of the Spirit at Pentecost, when the power that rested on individual prophets comes upon the entire community."},
      {"type": "allusion", "target": "Acts 2:4", "note": "The Spirit that rested on Elijah is asked for in double measure by Elisha — Elijah's departure and Elisha's reception of the spirit-mantle foreshadows the departure of Jesus and the Spirit's outpouring at Pentecost: 'they were all filled with the Holy Spirit' (Acts 2:4); the prophetic spirit is not lost at the prophet's departure but poured out in greater fullness on the successor community."}
    ],
    "13": [
      {"type": "allusion", "target": "Acts 1:8", "note": "Elisha picks up the mantle of Elijah that had fallen — the prophetic spirit and mission continue through the successor, not lost when the individual prophet departs; Jesus's final words before his ascension ('you will receive power when the Holy Spirit has come upon you, and you will be my witnesses') follow the same pattern: the departing prophet/teacher bestows continuing power and mission on those left behind."}
    ]
  },
  "3": {
    "17": [
      {"type": "allusion", "target": "John 7:38-39", "note": "YHWH's command to make the valley full of trenches, with the promise that the valley would be filled with water without wind or rain — invisible, sourceless provision through obedient preparation — is a type of the Spirit's invisible provision; Jesus at the Feast of Tabernacles: 'Whoever believes in me, as the Scripture has said, out of his heart will flow rivers of living water.' John's narrator explains: 'Now this he said about the Spirit, whom those who believed in him were to receive.' The water that fills the prepared trenches without visible source is the OT form of the Spirit who fills the prepared heart without visible causation."}
    ]
  }
}

def main():
    e = load_echo('2kings')
    merge_echo(e, ECHO)
    save_echo('2kings', e)
    count = sum(len(v) for v in ECHO.values())
    print(f'2kings echo: wrote {count} verses across ch 1-3')

if __name__ == '__main__':
    main()
