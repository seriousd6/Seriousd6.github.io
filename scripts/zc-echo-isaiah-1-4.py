"""
Isaiah echo — chapters 1–4
Run: python3 scripts/zc-echo-isaiah-1-4.py

Selective echo entries for major NT quotations and allusions.
Ch1:9 already present (Rom 9:29 quote). This script adds chs 1 (remaining), 2, 3, 4.

Key connections:
  Isa 1:18  → Rev 7:14 / Heb 9:14   scarlet sins made white by the blood of the Lamb
  Isa 2:2-3 → Heb 12:22 / Rev 21:10  mountain of the LORD established / Zion pilgrimage
  Isa 2:10-11,19,21 → Rev 6:15-17    hiding from the LORD's terror on the great day
  Isa 3:14  → Luke 20:16 / Matt 21:43 vineyard plundered — parable of wicked tenants
  Isa 4:2   → Luke 1:78 / Rev 22:16  the Branch of the LORD — messianic title
  Isa 4:4   → Matt 3:11-12           spirit of burning = baptism with Holy Spirit and fire
  Isa 4:5-6 → Rev 7:15-16            divine shelter / canopy over Zion = God's tabernacling
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
    # VERIFY: run twice; second run output should show 0 new entries added
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
  "1": {
    "18": [
      {"type": "allusion", "target": "Rev 7:14", "note": "Scarlet sins made white as snow — the great multitude who 'washed their robes and made them white in the blood of the Lamb'; Isa 1:18's cleansing promise is fulfilled through the atoning blood of Christ"},
      {"type": "allusion", "target": "Heb 9:14", "note": "The blood of Christ purifies the conscience from dead works; Isa 1:18's offer of cleansing from scarlet/crimson sin is grounded in the high-priestly offering of Christ"}
    ],
    "21": [
      {"type": "allusion", "target": "Rev 17:1", "note": "The faithful city that became a whore — Revelation applies the harlot-city imagery to Babylon/Rome as the anti-Jerusalem; the contrast with the pure bride of Rev 21:2 fulfills Isa 1:26's promise to restore Zion as the faithful city"}
    ],
    "25": [
      {"type": "allusion", "target": "1 Pet 1:7", "note": "God smelting away dross by fire — Peter applies the refiner's fire to the testing of faith more precious than gold; Isa 1:25's purging fire is the eschatological trial that produces proven faith in Christ"},
      {"type": "allusion", "target": "Mal 3:3", "note": "The refiner purifying the sons of Levi — Malachi's messenger refining as silver is the same divine purging as Isa 1:25, applied to the Levitical priesthood and fulfilled in Christ the great High Priest who purifies his people"}
    ]
  },
  "2": {
    "2": [
      {"type": "fulfillment", "target": "Heb 12:22", "note": "You have come to Mount Zion, to the city of the living God — the author of Hebrews announces the eschatological establishment of the mountain of Isa 2:2 as already accessible through Christ; the latter-days mountain-establishment is the new covenant Zion"},
      {"type": "fulfillment", "target": "Rev 21:10", "note": "The great, high mountain and the holy city Jerusalem — John's vision of the New Jerusalem on the great mountain fulfills Isa 2:2's promise that the mountain of the LORD's house would be established as the highest; all nations now flow to it through the Lamb"}
    ],
    "3": [
      {"type": "allusion", "target": "John 4:21", "note": "Worship neither on this mountain nor in Jerusalem — Jesus reframes the Isa 2:3 pilgrimage to Zion; the true worshipers now come to the Father in spirit and truth through Christ rather than to geographic Zion"},
      {"type": "allusion", "target": "Matt 28:19", "note": "Make disciples of all nations — the great commission is the gospel fulfillment of the nations streaming to Zion in Isa 2:3; instead of nations going up to Jerusalem, the disciples go out to all nations with the word of the LORD"}
    ],
    "4": [
      {"type": "allusion", "target": "Rev 21:4", "note": "No more death, mourning, crying, or pain — the swords-into-plowshares peace of Isa 2:4 is the new creation reality of Rev 21; the eschatological end of war achieved through the Lamb's victory"},
      {"type": "allusion", "target": "Acts 17:31", "note": "God has fixed a day to judge the world by the man he has appointed — Isa 2:4's promise that the LORD shall judge between nations is fulfilled by the appointed judge, Jesus Christ, raised from the dead as guarantee of the coming judgment"}
    ],
    "10": [
      {"type": "allusion", "target": "Rev 6:15", "note": "Kings of the earth and the great ones hiding in caves — Rev 6:15-17 is the direct NT echo of Isa 2:10,19,21; those hiding from the LORD's terror in Isa 2 are the exact population of Rev 6 hiding from the face of the Lamb on the great day of wrath"}
    ],
    "19": [
      {"type": "allusion", "target": "Rev 6:16", "note": "Calling on mountains and rocks to fall on them and hide them from the face of him who sits on the throne — a direct allusion to Isa 2:19-21; John identifies the one whose terror drives people to the caves as the Lamb, confirming Christ as the LORD of Isa 2"}
    ]
  },
  "3": {
    "14": [
      {"type": "type", "target": "Luke 20:16", "note": "The parable of the wicked tenants who plundered the vineyard — Isa 3:14 indicts Israel's leaders for devouring the vineyard; Jesus's parable of the wicked tenants (Matt 21:33-43; Luke 20:9-19) applies the same indictment, adding that the owner's Son is killed, and the vineyard given to others"},
      {"type": "allusion", "target": "Matt 21:43", "note": "The kingdom of God will be taken away and given to a people producing its fruits — the transfer of the vineyard from those who plundered it (Isa 3:14) to a faithful nation; Christ fulfills and surpasses the Isa 3 indictment"}
    ]
  },
  "4": {
    "2": [
      {"type": "type", "target": "Luke 1:78", "note": "The sunrise (anatole) shall visit us from on high — Zechariah's canticle uses the same Greek word for 'branch/sprout' (anatole/tsemach) that the LXX uses for Isa 4:2's Branch of the LORD; Christ is the messianic Branch who is beautiful and glorious"},
      {"type": "allusion", "target": "Rev 22:16", "note": "I am the root and the offspring of David, the bright morning star — Christ the Branch who springs from David; Isa 4:2's Branch of the LORD that is glorious for the survivors of Israel is the risen Christ revealed as the radiant source of the new creation"}
    ],
    "4": [
      {"type": "fulfillment", "target": "Matt 3:11", "note": "He will baptize you with the Holy Spirit and fire — John the Baptist explicitly connects his baptism with the spirit of judgment and burning in Isa 4:4; the Lord's cleansing of the daughters of Zion by a spirit of burning is the Pentecost poured out by the risen Christ"},
      {"type": "fulfillment", "target": "Acts 2:3", "note": "Divided tongues as of fire appeared and rested on each of them — the Pentecost fire is the fulfillment of Isa 4:4's spirit of burning; the same purifying fire that Isaiah foresaw for Zion descends on the new covenant community"}
    ],
    "5": [
      {"type": "allusion", "target": "Rev 7:15", "note": "He who sits on the throne will shelter them with his presence — the divine tabernacling over the redeemed echoes Isa 4:5-6's cloud and fire over Mount Zion; the Lamb's canopy replaces the wilderness pillar as the permanent shelter of God's people in the new creation"},
      {"type": "allusion", "target": "John 1:14", "note": "The Word became flesh and tabernacled (eskenosen) among us — the divine cloud-and-fire presence of Isa 4:5 that tabernacled over Zion becomes in John's Gospel the incarnate Word dwelling among his people as God's permanent presence"}
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
