"""
echo | Isaiah | 53-58 | python3 scripts/zc-echo-isaiah-53-58.py

Chs 53-56 already done. This script adds chs 57-58 only.

Key echo decisions:
- Isa 57:15 (high and lofty One dwelling with the contrite) → Luke 1:52 / John 1:14:
  the Magnificat and incarnation as fulfillment of God's dwelling with the humble
- Isa 57:19 ("peace to far and near") → Eph 2:17: DIRECT CITATION by Paul —
  'he came and preached peace to you who were far off and peace to those near'
- Isa 58:6 (loose bonds of wickedness, let oppressed go free) → Luke 4:18:
  Jesus's Nazareth manifesto draws on this alongside Isa 61:1
- Isa 58:11 (spring of water that does not fail) → John 4:14 / John 7:38:
  living water imagery
- Isa 58:14 (I will make you ride on heights) → Heb 4:10-11: Sabbath rest
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
    "57": {
        "15": [
            {"type": "allusion", "target": "Luke 1:52", "note": "He has brought down the mighty from their thrones and exalted those of humble estate — Mary's Magnificat echoes Isa 57:15 (the high and lofty One who inhabits eternity also dwells with the contrite and lowly in spirit); the pattern of God exalting the lowly and dwelling with the humble reaches its climax in the incarnation."},
            {"type": "fulfillment", "target": "John 1:14", "note": "The Word became flesh and tabernacled among us — the high and lofty One who dwells with the lowly and contrite (Isa 57:15) takes his dwelling-with-the-humble to its ultimate expression in the incarnation; the eternal God who inhabits eternity pitches his tent in human flesh."}
        ],
        "19": [
            {"type": "citation", "target": "Eph 2:17", "note": "He came and preached peace to you who were far off and peace to those who were near — Paul directly cites Isa 57:19 in Eph 2:17 as the scriptural basis for Christ's reconciling work; the promise of peace to both the far (Gentiles) and the near (Jews) is fulfilled in Christ who broke down the dividing wall between the two."}
        ],
        "20": [
            {"type": "allusion", "target": "Jude 13", "note": "The wicked are like the tossing sea that cannot be quiet; its waters toss up mire and dirt — Isa 57:20's image of the restless, defiling sea anticipates Jude 13's description of false teachers as wild waves of the sea, casting up the foam of their own shame; the spiritual instability of wickedness is figured in both texts as uncontrollable water."}
        ]
    },
    "58": {
        "6": [
            {"type": "allusion", "target": "Luke 4:18", "note": "To loose the bonds of wickedness, to undo the straps of the yoke, to let the oppressed go free — Jesus's Nazareth manifesto (Luke 4:18) combines Isa 61:1 and Isa 58:6; the liberating ministry Jesus claims as his own draws from both texts; the fast God chooses (Isa 58:6) is social justice, and Jesus embodies it as the one who sets the captive free."}
        ],
        "7": [
            {"type": "allusion", "target": "Matt 25:35-40", "note": "Share your bread with the hungry, bring the homeless poor into your house, cover the naked — the ethical demands of Isa 58:7 are the exact list Jesus uses to describe service to himself in Matt 25:35-40 (I was hungry and you gave me food, I was a stranger and you welcomed me, I was naked and you clothed me); the commands of Isa 58 are fulfilled in service to Christ."}
        ],
        "8": [
            {"type": "allusion", "target": "John 8:12", "note": "Then shall your light break forth like the dawn — the light breaking forth as the reward of righteous practice (Isa 58:8) anticipates Jesus's declaration 'I am the light of the world' (John 8:12) and his command that his disciples let their light shine (Matt 5:16); the dawn-light of Isa 58 is realized in the incarnation and reproduced in the life of those who follow the Light."}
        ],
        "11": [
            {"type": "allusion", "target": "John 4:14", "note": "You shall be like a watered garden, like a spring of water whose waters do not fail — the spring-that-does-not-fail of Isa 58:11 feeds into Jesus's promise to the Samaritan woman (John 4:14: the water that I will give will become a spring of water welling up to eternal life); the covenant promise of unceasing water is fulfilled in the Spirit given through Christ."},
            {"type": "allusion", "target": "John 7:38", "note": "Out of his heart will flow rivers of living water — the never-failing spring of Isa 58:11 (and the wells of salvation in Isa 12:3) lie behind Jesus's Tabernacles declaration; the Spirit as living water makes the believer a spring that never runs dry, the covenant blessing of Isa 58 extended through Christ."}
        ],
        "13": [
            {"type": "allusion", "target": "Mark 2:27-28", "note": "If you turn back your foot from the Sabbath, from doing your pleasure on my holy day — the Sabbath-as-delight in Isa 58:13-14 resonates with Jesus's declaration that the Son of Man is Lord of the Sabbath (Mark 2:27-28); Jesus does not abolish the Sabbath but fulfills its deepest intent as the one who gives true rest."}
        ],
        "14": [
            {"type": "allusion", "target": "Heb 4:10-11", "note": "Then you shall take delight in the LORD, and I will make you ride on the heights of the earth — the Sabbath-rest of Isa 58:13-14 is the OT type of the eschatological rest that Heb 4:10-11 describes: whoever has entered God's rest has ceased from his works just as God did from his; the heights-riding delight of Isa 58 is fulfilled in the rest Christ gives to those who come to him (Matt 11:28-30)."}
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
