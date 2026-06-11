"""
echo layer: Ezekiel 29-32
Egypt oracles (chs 29-30, 32) and Assyrian-cedar oracle (ch 31). Key clusters:
  - ch29 dragon-in-the-Nile → Rev 12-13; messianic horn → Luke 1:69
  - ch30 Day of the LORD, time of the nations → Luke 21:24; Acts 2:20
  - ch31 cosmic tree falls to Sheol → Mark 4:32 (contrast); Phil 2:10 (under the earth)
  - ch32 cosmological darkness at fall → Matt 24:29; Rev 6:12-13; descent to Sheol → 1 Pet 3:19
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

EZEKIEL_ECHOES = {
  "29": {
    "3": [
      {"type": "allusion", "target": "Rev 12:9", "note": "Pharaoh king of Egypt — the great sea creature (tannin/dragon) who says My Nile is my own; I made it for myself — the dragon-ruler who claims self-made sovereignty is the OT prototype of Revelation's great dragon (Rev 12:9; 20:2); Pharaoh in the Nile claiming ownership of creation is the archetype of all satanic self-deification that Revelation symbolizes as the beast and dragon claiming dominion over the world"},
      {"type": "allusion", "target": "Rev 13:1", "note": "The sea creature from the Nile claiming self-made dominion — the beast rising from the sea in Rev 13:1 draws on the Ezekielian tradition of Pharaoh as the great tannin (sea monster) of the Nile; the political power that claims divine self-sufficiency — I made it for myself — is the definitive image of the anti-God empire that Revelation names the beast"}
    ],
    "21": [
      {"type": "fulfillment", "target": "Luke 1:69", "note": "On that day I will cause a horn to sprout for the house of Israel — the messianic horn promise (qeren = horn, symbol of royal power) in the context of Egypt's humiliation is fulfilled in Gabriel's annunciation: God has raised up a horn of salvation for us in the house of his servant David (Luke 1:69); the sprouting horn that arises when the imperial oppressor is brought down is the Davidic Messiah"}
    ]
  },
  "30": {
    "3": [
      {"type": "allusion", "target": "Luke 21:24", "note": "The day of the LORD is near — a day of cloud; it will be the time of the nations (<em>et goyim</em>) — Jesus uses this same phrase in the eschatological discourse: Jerusalem will be trampled underfoot by the Gentiles until the times of the Gentiles (<em>kairoi ethnōn</em>) are fulfilled (Luke 21:24); the 'time of the nations' when God's judgment falls on imperial Egypt becomes the template for the NT's eschatological 'times of the Gentiles'"},
      {"type": "allusion", "target": "Joel 2:31", "note": "The day of the LORD is near — Joel 2:31 (day of the LORD, sun darkened, moon to blood) is quoted at Pentecost in Acts 2:20; Ezekiel's 'day of the LORD' oracle over Egypt is part of the prophetic cluster (Isa 13, Joel 2, Amos 5, Zeph 1) that the NT reads as the eschatological pattern Jesus fulfills and Revelation consummates"}
    ]
  },
  "31": {
    "6": [
      {"type": "allusion", "target": "Mark 4:32", "note": "All the birds of the sky nested in its boughs; under its branches all the beasts of the field gave birth; all great nations dwelt in its shade — the cosmic cedar where all nations find shelter is the same imagery Jesus uses in the parable of the mustard seed: when grown it becomes a tree, so that the birds of the air come and make nests in its branches (Mark 4:32; also Ezek 17:23); the difference is that Assyria's pride-tree falls to Sheol while the Messianic tree is planted by God and stands forever"}
    ],
    "14": [
      {"type": "allusion", "target": "Phil 2:10", "note": "All who drink water are given over to death, to the depths of the earth, among the children of men, with those who go down to the Pit — the universal pattern of descent to Sheol for all great powers prepares the NT's cosmic sovereignty of Christ over the underworld: at the name of Jesus every knee will bow, of those in heaven and on earth and under the earth (Phil 2:10); the fallen cedar's descent to 'the depths of the earth' is what Phil 2:10 addresses as the realm of Christ's completed cosmic authority"}
    ],
    "16": [
      {"type": "allusion", "target": "Eph 4:9", "note": "I cast him down to Sheol with those who go down to the Pit — the descent of the great cedar to the lowest realm below is the pattern Paul reads in Psalm 68 and applies to Christ's descent: what does 'he ascended' mean except that he had also descended into the lower parts of the earth? (Eph 4:9); the cosmic tree brought down to Sheol and the cosmic Lord who descends to Hades and rises inverts the pattern: pride brings the cedar down and it stays down; humility brings Christ down and he rises above all"}
    ]
  },
  "32": {
    "7": [
      {"type": "allusion", "target": "Matt 24:29", "note": "When I blot you out I will cover the heavens and darken their stars; I will cover the sun with a cloud and the moon will not give its light — the cosmological darkness signs accompanying Egypt's fall become the template for the eschatological signs Jesus describes: the sun will be darkened and the moon will not give its light, and the stars will fall from heaven (Matt 24:29; Mark 13:24-25); what happens to Pharaoh's world at the Nile becomes the cosmic pattern for the final Day of the LORD"},
      {"type": "allusion", "target": "Rev 6:12-13", "note": "The sun darkened, moon gives no light, stars covered — at the sixth seal (Rev 6:12-13) the sun becomes black, the moon becomes like blood, and the stars fall from the sky; Ezekiel's Egypt darkness oracle is one of the OT texts that Revelation draws on for the cosmic-catastrophe language of the final judgment; the darkening of Egypt's sky is the prototype of the darkening of the whole cosmos at the Lamb's wrath"}
    ],
    "21": [
      {"type": "allusion", "target": "1 Pet 3:19", "note": "The mightiest warriors will speak to him from the midst of Sheol — the realm below populated by the fallen mighty, the Pit where uncircumcised kings and armies lie; this vision of Sheol as the place where the dead powers reside is the background for 1 Peter 3:19 — Christ, put to death in the flesh but made alive in the Spirit, went and proclaimed to the spirits in prison; Christ's descent to the realm Ezekiel envisions as the gathering place of fallen empires is the cosmic proclamation of his victory over all powers including those under the earth"}
    ],
    "27": [
      {"type": "allusion", "target": "Rev 19:17-18", "note": "The fallen warriors in Sheol with swords under their heads and shields on their bones — Ezekiel's vision of the underworld army with their weapons is the counterpart to Revelation's great supper of God (Rev 19:17-18) where birds eat the flesh of kings and mighty men; both passages use the same fallen-warriors imagery to depict the total defeat of the powers that opposed God; what Ezekiel sees descending to Sheol in Egypt's fall Revelation shows consumed above the earth at Christ's return"}
    ]
  }
}

def main():
    e = load_echo("ezekiel")
    merge_echo(e, EZEKIEL_ECHOES)
    save_echo("ezekiel", e)
    for ch in ["29", "30", "31", "32"]:
        vv = e.get(ch, {})
        print(f"  ch{ch}: {len(vv)} verse(s) with echoes")

if __name__ == "__main__":
    main()
