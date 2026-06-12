"""
MKT Echo Data — 2 Kings chapters 15–17
Run: python3 scripts/zc-echo-2kings-15-17.py

Ch15: Kings succeeding in rapid succession — the unraveling of the northern kingdom;
      Tiglath-pileser's invasions
Ch16: Ahaz's altar replacement — foreign cult replacing YHWH's altar / Heb 13:10
Ch17: Fall of Samaria (722 BCE) — theological explanation of the exile (vv7-23);
      nations settled in Samaria — origin of the Samaritans / John 4 context
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
  "16": {
    "10": [
      {"type": "allusion", "target": "Heb 13:10", "note": "Ahaz sees the Damascus altar and has Uriah the priest build a replica in Jerusalem, replacing the bronze altar with a foreign model — the substitution of an unauthorized altar for the one YHWH ordained; Heb 13:10 addresses the opposite movement: 'We have an altar from which those who serve the tent have no right to eat' — the new-covenant altar (Christ's sacrifice) supersedes and replaces the old. Ahaz replaces the true with a false imitation; Christ replaces the type with the fulfillment."}
    ]
  },
  "17": {
    "7": [
      {"type": "allusion", "target": "Rom 1:21-23", "note": "The theological explanation of the fall of Samaria (vv7-23): Israel 'feared other gods and walked in the customs of the nations whom YHWH drove out... and they went after false idols and became false' (v15) — the structure of idolatry as exchange and corruption; Paul in Rom 1:21-23 describes the same spiral: 'although they knew God, they did not honor him as God... they exchanged the glory of the immortal God for images.' The 2 Kgs 17 explanation of the northern exile is the OT's most concentrated analysis of the idolatry-to-judgment sequence that Paul universalizes in Romans 1."}
    ],
    "24": [
      {"type": "allusion", "target": "John 4:9", "note": "The Assyrian repopulation of Samaria with peoples from Babylon, Cuthah, and other nations (v24) — mixed with the remaining Israelite population — is the historical origin of the Samaritan people and their syncretistic religion (v33: 'they feared YHWH but also served their own gods'); John 4:9 records the Samaritan woman's surprise that a Jewish man would speak with her: 'Jews have no dealings with Samaritans.' The ethnic and religious separation traceable to 2 Kgs 17:24-33 is the background of Jesus's deliberate boundary-crossing in the Samaritan encounter, which ends with Samaritans confessing Jesus as 'the Savior of the world' (John 4:42)."}
    ]
  }
}

def main():
    e = load_echo('2kings')
    merge_echo(e, ECHO)
    save_echo('2kings', e)
    count = sum(len(v) for v in ECHO.values())
    print(f'2kings echo: wrote {count} verses across ch 15-17')

if __name__ == '__main__':
    main()
