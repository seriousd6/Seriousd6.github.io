"""
MKT Echo Data — 2 Kings chapters 12–14
Run: python3 scripts/zc-echo-2kings-12-14.py

Ch12: Joash's temple repair — collection-box at the temple gate; money for repairs only
Ch13: Elisha's death and posthumous resurrection — bones revive a corpse (13:21)
Ch14: Amaziah's half-reformation; Jeroboam II's expansion; Jonah sent (14:25)
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
  "12": {
    "9": [
      {"type": "allusion", "target": "Mark 12:41-44", "note": "Jehoiada the priest places a chest at the temple gate to collect money for repairs — the giving-chest at the temple entrance as the locus of covenant generosity; Jesus sits opposite the treasury and watches people put money in (Mark 12:41), noting the widow's two coins. The temple-treasury observation scene in Mark transposes the temple-repair collection of 2 Kgs 12 into a teaching moment about the nature of true giving versus performative giving."}
    ]
  },
  "13": {
    "21": [
      {"type": "allusion", "target": "Matt 27:52-53", "note": "A dead man thrown into Elisha's tomb revives when his body touches Elisha's bones — the only OT instance of resurrection-power persisting after a prophet's death; the tombs opened and the dead rising at Jesus's death (Matt 27:52-53) is the antitype: not the lingering power of a dead prophet's bones but the firstfruits of the resurrection from the living Lord whose death itself opened the graves. The Elisha-bones miracle is the OT's solitary hint that resurrection power can emanate from a buried body."},
      {"type": "allusion", "target": "Heb 11:35", "note": "Elisha's posthumous bone-contact resurrection is what the author of Hebrews includes in the honor roll of faith: 'Women received back their dead by resurrection' (Heb 11:35) — the Shunammite's son (through the living Elisha) and here a nameless man through Elisha's dead bones, both witnessing that the God of Israel is 'the God who raises the dead' (2 Cor 1:9)."}
    ]
  },
  "14": {
    "25": [
      {"type": "allusion", "target": "Matt 12:41", "note": "Jeroboam II's territory restoration is said to fulfill the word of Jonah son of Amittai the prophet from Gath-hepher — identifying Jonah as a historical figure who prophesied to the northern kingdom before his mission to Nineveh; Jesus cites 'Jonah the prophet' in Matt 12:41 as a sign of judgment against his own generation: 'Something greater than Jonah is here.' Jonah's historical connection to the northern kingdom's king (2 Kgs 14:25) grounds his mission to Nineveh in the same period of Assyrian threat that would eventually destroy that kingdom."}
    ]
  }
}

def main():
    e = load_echo('2kings')
    merge_echo(e, ECHO)
    save_echo('2kings', e)
    count = sum(len(v) for v in ECHO.values())
    print(f'2kings echo: wrote {count} verses across ch 12-14')

if __name__ == '__main__':
    main()
