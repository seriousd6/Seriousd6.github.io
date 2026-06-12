"""
MKT Echo Layer — 2 Chronicles chapters 9–12
Run: python3 scripts/zc-echo-2chronicles-9-12.py

Ch9: Queen of Sheba's visit (9:1) — Jesus cites it in Matt 12:42 / Luke 11:31
     Solomon's wisdom-fame (9:7) — beatitude-echo (blessed servants of the wise king)
Ch10: Heavy yoke (10:11) — contrast with Christ's easy yoke (Matt 11:30)
Ch12: Humble self-abasement averts judgment (12:6) — Jas 4:10; 1 Pet 5:6
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
  "9": {
    "1": [
      {"type": "fulfillment", "target": "Matt 12:42", "note": "When the queen of Sheba heard the fame of Solomon she came to test him with hard questions — Jesus cites this episode directly: 'the queen of the South will rise up at the judgment with this generation and condemn it, for she came from the ends of the earth to hear the wisdom of Solomon, and behold, something greater than Solomon is here.' The gentile queen who traveled to encounter Solomon's wisdom is the OT type of the nations drawn to the greater Wisdom incarnate in Christ."},
      {"type": "allusion", "target": "Luke 11:31", "note": "Lukan parallel to Matt 12:42 — the queen of the South will rise at the judgment and condemn this generation, for she came from the ends of the earth to hear Solomon's wisdom, and something greater than Solomon is here."}
    ],
    "7": [
      {"type": "allusion", "target": "Luke 12:37", "note": "Happy are your men! Happy are your servants who continually stand before you and hear your wisdom — the beatitude pronounced on Solomon's servants who stand in his presence echoes the Lukan beatitude on servants whom the master finds alert when he returns: 'Blessed are those servants whom the master finds awake when he comes.'"}
    ]
  },
  "10": {
    "11": [
      {"type": "contrast", "target": "Matt 11:30", "note": "My father made your yoke heavy, but I will add to it — Rehoboam's threat to increase the burden of leadership is the direct foil for Christ's invitation: 'Come to me, all who labor and are heavy laden, and I will give you rest. Take my yoke upon you... for my yoke is easy, and my burden is light.' The heavy-yoke ruler of Rehoboam's folly stands in contrast to the easy-yoke King of Matthew 11."}
    ]
  },
  "12": {
    "6": [
      {"type": "allusion", "target": "Jas 4:10", "note": "The princes of Israel and the king humbled themselves and said, 'The LORD is righteous' — the self-humbling of the king and leaders averts divine judgment (v7: 'they have humbled themselves; I will not destroy them'). James 4:10 draws on the same covenantal pattern: 'Humble yourselves before the Lord and he will exalt you.' The Chronicler's narrative consistently demonstrates that humility (anah/kana) before YHWH turns aside deserved judgment — a principle Christ embodies in his own humiliation (Phil 2:8-9: 'he humbled himself... therefore God has highly exalted him')."},
      {"type": "allusion", "target": "1 Pet 5:6", "note": "Humble yourselves, therefore, under the mighty hand of God so that at the proper time he may exalt you — the same covenantal logic as 2 Chr 12:6-7: humility before YHWH's judgment brings mercy and future exaltation."}
    ]
  }
}

def main():
    e = load_echo('2chronicles')
    merge_echo(e, ECHOES)
    save_echo('2chronicles', e)
    count = sum(len(v) for v in ECHOES.values())
    print(f'2chronicles echo: wrote entries for {count} verses across ch 9-12')

if __name__ == '__main__':
    main()
