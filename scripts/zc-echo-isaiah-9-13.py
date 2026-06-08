"""
Isaiah echo — chapters 9–13
Run: python3 scripts/zc-echo-isaiah-9-13.py

Chs 9, 10, 11, 13 already have echo entries. This script adds ch 12.

Isaiah 12 — the short thanksgiving psalm (6 verses) sung after the judgment/exile:
  Isa 12:2  → Rev 7:10; Rom 10:9-10   "salvation" — the salvation cry of the redeemed
  Isa 12:3  → John 7:37-38; John 4:14  wells of salvation = rivers of living water from Christ
  Isa 12:4  → Acts 2:21 / Rom 10:13   call upon his name / name proclaimed in all the earth
  Isa 12:6  → Rev 21:3; Heb 12:22     Holy One great in your midst = God dwelling with man
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent


def load_echo(book):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    return json.loads(p.read_text()) if p.exists() else {}


def save_echo(book, data):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f"  wrote {p.relative_to(ROOT)}")


def merge_echo(existing, new_data):
    # INTENT: append-only echo merge — never drops existing entries, deduplicates by (type, target)
    # CHANGE? If echo schema changes, update the seen-set key here and in all other echo scripts
    # VERIFY: run twice; second run should show 0 new entries added
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e["type"], e["target"]) for e in existing[ch][v]}
                for e in entries:
                    if (e["type"], e["target"]) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e["type"], e["target"]))


ISA_ECHO = {
  "12": {
    "2": [
      {"type": "allusion", "target": "Rev 7:10", "note": "The great multitude crying 'Salvation belongs to our God' — the eschatological fulfillment of Isa 12:2's 'God is my salvation'; the redeemed from every nation sing the same salvation cry as the restored exiles, now directed to God and the Lamb"},
      {"type": "allusion", "target": "Rom 10:10", "note": "With the heart one believes and is justified, and with the mouth one confesses and is saved — Paul's salvation formula echoes Isa 12:2's personal declaration 'God is my salvation'; the individual confession 'the LORD has become my salvation' is the shape of saving faith"}
    ],
    "3": [
      {"type": "fulfillment", "target": "John 7:38", "note": "Whoever believes in me, as the Scripture has said, out of his heart will flow rivers of living water — Jesus cites Scripture (likely Isa 12:3 / 55:1) to identify himself as the source of the wells of salvation; the water drawn with joy from the wells of salvation is the Spirit flowing from the risen Christ"},
      {"type": "allusion", "target": "John 4:14", "note": "The water that I will give will become a spring of water welling up to eternal life — the Samaritan woman and the well of salvation; Isa 12:3's wells of salvation find their personal embodiment in Christ who gives water the drinker never thirsts for again"}
    ],
    "4": [
      {"type": "fulfillment", "target": "Acts 2:21", "note": "Everyone who calls upon the name of the Lord shall be saved — Peter's Pentecost sermon (citing Joel 2:32) announces the fulfillment of Isa 12:4's 'call upon his name'; the name proclaimed in all the earth is the name of Jesus Christ, the exalted Lord"},
      {"type": "allusion", "target": "Phil 2:10", "note": "At the name of Jesus every knee should bow — the exaltation of the name fulfills Isa 12:4's 'proclaim that his name is exalted'; the name made known among the peoples is specifically the name given to the crucified and risen Christ"}
    ],
    "6": [
      {"type": "allusion", "target": "Rev 21:3", "note": "The dwelling place of God is with man — the Holy One great in Israel's midst in Isa 12:6 finds its eschatological completion in the new creation where God tabernacles permanently with his people; the Holy One who was great in Zion is the Lamb in the midst of the holy city"},
      {"type": "allusion", "target": "Heb 12:22", "note": "You have come to Mount Zion, to the city of the living God, to the heavenly Jerusalem — the inhabitant of Zion who shouts for joy at the Holy One's presence (Isa 12:6) is the church that has already come to the heavenly Zion through Christ"}
    ]
  }
}


if __name__ == "__main__":
    e = load_echo("isaiah")
    before = sum(len(v) for ch in e.values() for v in ch.values())
    merge_echo(e, ISA_ECHO)
    save_echo("isaiah", e)
    after = sum(len(v) for ch in e.values() for v in ch.values())
    print(f"  total echo entries: {before} → {after} (+{after - before})")
    for ch, verses in ISA_ECHO.items():
        for v, entries in verses.items():
            saved = e.get(ch, {}).get(v, [])
            print(f"  ch{ch}:{v} — {len(entries)} written, {len(saved)} in file")
