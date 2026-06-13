"""
echo | 2chronicles | ch 11, 19, 27 gap-fill
Adds echo entries for three missing chapters.
Run: python3 scripts/zc-echo-2chronicles-gaps.py
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

CHRONICLES2_ECHOES = {
  "11": {
    "13": [
      {
        "type": "type",
        "target": "Rev 18:4",
        "note": "The priests and Levites from all Israel abandon Jeroboam's false worship and come to Rehoboam in Jerusalem (v13-14) — a type of the call to come out of Babylon: 'Come out of her, my people, so that you will not share in her sins' (Rev 18:4). The faithful remnant separating from apostate institutional religion."
      },
      {
        "type": "allusion",
        "target": "2 Cor 6:17",
        "note": "Those who 'set their hearts on seeking YHWH' (v16) leave the north to worship in Jerusalem — echoing Paul's call to 'come out from them and be separate, says the Lord.' Covenant faithfulness sometimes requires leaving a corrupted religious structure to worship rightly."
      }
    ]
  },
  "19": {
    "6": [
      {
        "type": "allusion",
        "target": "1 Cor 6:2",
        "note": "Jehoshaphat tells the judges: 'Consider carefully what you do, because you are not judging for mere mortals but for the LORD' (v6) — echoed by Paul: 'Do you not know that the Lord's people will judge the world?' (1 Cor 6:2). Human judicial authority is delegated divine authority; those who judge in God's name will themselves be judged by God's standard."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "2 Cor 6:14",
        "note": "Jehu the seer rebukes Jehoshaphat: 'Should you help the wicked and love those who hate the LORD?' (v2) — the same principle Paul articulates in 2 Cor 6:14: 'Do not be yoked together with unbelievers.' Partnering with those who oppose YHWH brings the wrath Jehoshaphat barely escaped at Ramoth-gilead (ch18)."
      }
    ]
  },
  "27": {
    "2": [
      {
        "type": "type",
        "target": "Matt 13:24",
        "note": "Jotham did right in the sight of YHWH, yet 'the people continued their corrupt practices' (v2) — the righteous king's personal faithfulness does not automatically transform the community. This tension between the righteous king and the unresponsive people is the same dynamic as the parable of the wheat and tares (Matt 13:24-30): the king sows good seed, but the field contains both wheat and tares until the harvest."
      }
    ],
    "6": [
      {
        "type": "type",
        "target": "Heb 5:8",
        "note": "Jotham 'grew powerful because he ordered his ways before the LORD his God' (v6) — righteousness expressed through consistent ordered conduct produces genuine growth and authority. This principle finds its supreme expression in Christ, who 'learned obedience through what he suffered' (Heb 5:8) and was therefore perfected as the source of eternal salvation."
      }
    ]
  }
}

def main():
    existing = load_echo('2chronicles')
    merge_echo(existing, CHRONICLES2_ECHOES)
    save_echo('2chronicles', existing)
    for ch in ['11', '19', '27']:
        vv = existing.get(ch, {})
        print(f'  ch{ch}: {len(vv)} verse(s) with echo entries')

if __name__ == '__main__':
    main()
