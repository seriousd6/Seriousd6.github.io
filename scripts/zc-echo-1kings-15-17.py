"""
MKT Echo Layer — 1 Kings chapters 15–17
Run: python3 scripts/zc-echo-1kings-15-17.py

Ch15: David's faithfulness summary 'except in the matter of Uriah' — the Davidic
      exception that only Christ will lack (Heb 4:15)
Ch17: Elijah's drought — Jesus cites it for Gentile-grace theology (Luke 4:25-26);
      flour/oil provision; widow's son raised — Luke 7:11-17 structural parallel
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
  "15": {
    "5": [
      {"type": "contrast", "target": "Heb 4:15", "note": "David did what was right in YHWH's eyes and did not turn aside all the days of his life, except in the matter of Uriah the Hittite — every Davidic king has an 'except'; the regnal summary formula measures faithfulness against this standard and always finds a failure point. Heb 4:15 identifies the one Davidic son with no 'except': 'one who in every respect has been tempted as we are, yet without sin' — the uniqueness of Christ's obedience is visible in contrast to every king who preceded him, each of whom the narrator marks with a qualification"}
    ]
  },
  "17": {
    "1": [
      {"type": "allusion", "target": "Luke 4:25", "note": "Elijah the Tishbite announces a multi-year drought — Jesus cites this drought in the Nazareth synagogue sermon (Luke 4:25: 'in the days of Elijah, when the sky was shut for three years and six months') as a paradigm for grace extending to Gentiles over Israel when Israel rejects the prophet"},
      {"type": "allusion", "target": "Jas 5:17", "note": "James cites the same Elijah drought as the paradigm of effective intercessory prayer: 'Elijah was a man with a nature like ours, and he prayed fervently that it might not rain, and for three years and six months it did not rain' — connecting the prophetic drought to the prayer-theology of the NT community"}
    ],
    "16": [
      {"type": "allusion", "target": "Luke 4:26", "note": "The jar of flour and jug of oil that do not run out for the widow of Zarephath — Jesus explicitly cites this miracle in the Nazareth sermon (Luke 4:26: 'there were many widows in Israel... and Elijah was sent to none of them but only to Zarephath in the land of Sidon, to a woman who was a widow') as the paradigm for prophetic grace bypassing Israel and going to a Gentile; Sidon is explicitly Gentile territory"},
      {"type": "allusion", "target": "John 6:12", "note": "The inexhaustible flour and oil provided for the widow through Elijah anticipates the feeding miracles of Jesus where a small amount of food multiplies without running out — the same pattern of the prophet's word overriding natural scarcity"}
    ],
    "22": [
      {"type": "type", "target": "Luke 7:14", "note": "Elijah prays and the widow's son is revived from death — the structural parallel with Jesus raising the widow's son at Nain (Luke 7:11-17) is exact: a widow, her only son who has died, a prophet who acts, life is restored, the crowd responds with awe. Luke 7:16 quotes the crowd: 'a great prophet has arisen among us' — identifying Jesus in Elijah-prophet terms. The Elijah raising is the OT type; the Nain raising is the messianic fulfillment at a greater level of authority (Elijah prays three times; Jesus speaks one word)"}
    ]
  }
}

def main():
    e = load_echo('1kings')
    merge_echo(e, ECHO)
    save_echo('1kings', e)
    count = sum(len(v) for v in ECHO.values())
    print(f'1kings echo: wrote {count} verse-groups across ch 15-17')

if __name__ == '__main__':
    main()
