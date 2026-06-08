"""
Isaiah echo — chapters 14–18
Run: python3 scripts/zc-echo-isaiah-14-18.py

All chapters missing. Selective echo entries for major NT allusions:
  Isa 14:12-15 → Luke 10:18 / Rev 12:9 / 2 Thess 2:4   the fall of the Day Star / Satan's pride
  Isa 14:15    → Rev 20:10                               cast into the pit
  Isa 15:1     → Rev 18:10                               city laid waste overnight — Babylon typology
  Isa 16:5     → Luke 1:32-33 / Acts 15:16               throne of David / tent of David
  Isa 17:12-13 → Rev 17:15 / Rev 19:6                    nations roaring like many waters
  Isa 18:7     → Rev 21:24                               gifts brought to Zion from distant peoples

NT note: chs 15-16 (Moab) and 18 (Cush) are oracles with limited direct NT citation.
Entries are given for chapter completeness; the Lucifer pericope (14:12-15) is the
highest-density NT-cited passage in this range.
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
  "14": {
    "12": [
      {"type": "allusion", "target": "Luke 10:18", "note": "I saw Satan fall like lightning from heaven — Jesus responds to the disciples' report of demonic defeat by citing Isa 14:12 as the paradigm; the fall of the Day Star (Helel/Lucifer) from heaven is the archetype that Christ witnesses in Satan's defeat through his ministry"},
      {"type": "allusion", "target": "Rev 12:9", "note": "The great dragon was thrown down, that ancient serpent called the devil and Satan — the cosmic fall of Isa 14:12 is the heavenly prototype that Revelation depicts eschatologically; the king of Babylon's fall mirrors and typifies the final expulsion of the adversary"}
    ],
    "13": [
      {"type": "allusion", "target": "2 Thess 2:4", "note": "The man of lawlessness who opposes and exalts himself above every god — Paul's description of the anti-Christ echoes the pride of Isa 14:13-14 ('I will ascend above the heights of the clouds; I will make myself like the Most High'); the Babylonian king's hubris is the type of every anti-God power"}
    ],
    "15": [
      {"type": "allusion", "target": "Rev 20:10", "note": "The devil was thrown into the lake of fire — the casting of the Day Star into Sheol/the pit (Isa 14:15) is the OT prototype for the final imprisonment of Satan; the pit of Isa 14 is the lake of fire of Rev 20"}
    ],
    "27": [
      {"type": "allusion", "target": "Rom 8:28", "note": "For those who love God all things work together for good — Paul's confidence in God's purpose echoes Isa 14:24-27's declaration that God's counsel stands and his purpose cannot be thwarted; the unstoppable purpose of God (Isa 14:27) grounds the assurance of Rom 8"}
    ]
  },
  "15": {
    "1": [
      {"type": "type", "target": "Rev 18:10", "note": "Alas, alas, you great city Babylon! For in a single hour your judgment has come — the overnight destruction of Ar of Moab in Isa 15:1 is the OT type of the sudden, catastrophic fall of Babylon in Revelation 18; both depict the swiftness of divine judgment on the proud city-civilization"}
    ]
  },
  "16": {
    "5": [
      {"type": "fulfillment", "target": "Luke 1:32", "note": "The Lord God will give him the throne of his father David — Gabriel's annunciation fulfills Isa 16:5's promise of a throne established in steadfast love in the tent of David; the one who will sit in faithfulness and judge is Jesus Christ"},
      {"type": "allusion", "target": "Acts 15:16", "note": "I will return and rebuild the tent of David that has fallen — James cites Amos 9:11 at the Jerusalem council, but the rebuilt Davidic tent of Isa 16:5 is the same promise; the throne of David is restored in the risen Christ who judges with justice"}
    ]
  },
  "17": {
    "12": [
      {"type": "allusion", "target": "Rev 17:15", "note": "The waters you saw are peoples and multitudes and nations and languages — Revelation explicitly interprets the roaring-waters imagery (already present in Isa 17:12-13) as the hostile nations; the thunder of many peoples in Isa 17 is the prototype of the raging sea of nations in Revelation"},
      {"type": "allusion", "target": "Rev 19:6", "note": "I heard what seemed to be the voice of a great multitude, like the roar of many waters — the redeemed multitude's hallelujah roars like the threatening nations of Isa 17:12-13, but the direction is reversed; the peoples who roared against God now roar his praise in the new creation"}
    ]
  },
  "18": {
    "7": [
      {"type": "type", "target": "Rev 21:24", "note": "The kings of the earth will bring their glory into the New Jerusalem — Isa 18:7's vision of gifts being brought from the people of Cush to Mount Zion is the OT prototype of the eschatological pilgrimage of the nations; what begins as tribute to YHWH's Zion ends as the nations streaming into the heavenly Jerusalem with their glory"}
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
