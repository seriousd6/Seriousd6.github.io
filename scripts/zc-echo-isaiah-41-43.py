"""
echo | Isaiah | 41-43 | python3 scripts/zc-echo-isaiah-41-43.py

Ch 42:1 already done (Matt 12:18-21 — Servant Song 1 citation at Jesus's baptism/ministry).
This script adds chs 41, 43, plus supplementary ch 42 entries.

Key echo decisions:
- Isa 41:4 ("I am the first and the last") → Rev 1:8 / Rev 22:13: divine name applied to Christ
- Isa 41:8 (Abraham my friend) → Jas 2:23 / John 15:14: friend of God → friends of Jesus
- Isa 42:6 (light to the Gentiles) → Luke 2:32: Simeon's nunc dimittis DIRECTLY cites this
- Isa 42:7 (open blind eyes, free captives) → Luke 4:18: Jesus's Nazareth manifesto cites this
- Isa 42:10 (new song) → Rev 5:9: the Lamb receives the new song in the heavenly throne room
- Isa 43:10 ("I am he") → John 8:24-58: Jesus's ego eimi statements echo this divine claim
- Isa 43:18-19 (new thing, forget the former) → 2 Cor 5:17 / Rev 21:5: new creation / all things new
- Isa 43:25 (I blot out your transgressions) → Mark 2:7: forgiveness belongs to God alone;
  Jesus's claim to forgive sins is a claim to divine identity
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
    "41": {
        "4": [
            {"type": "fulfillment", "target": "Rev 1:8", "note": "I am the Alpha and the Omega, who is and who was and who is to come, the Almighty — God's self-declaration in Isa 41:4 ('I, the LORD, the first and with the last; I am he') is directly applied to Christ in Rev 1:8 and 22:13; the divine name 'first and last' given to the God who raises up the nations in Isaiah is claimed by the risen Jesus."},
            {"type": "fulfillment", "target": "Rev 22:13", "note": "I am the Alpha and the Omega, the first and the last, the beginning and the end — Jesus explicitly claims the title from Isa 41:4 / 44:6 / 48:12; this is one of Revelation's clearest identifications of Jesus with the LORD of Isaiah."}
        ],
        "8": [
            {"type": "allusion", "target": "Jas 2:23", "note": "Abraham believed God and it was counted to him as righteousness, and he was called a friend of God — James cites Gen 15:6 and applies the title 'friend of God' from Isa 41:8 (Abraham, my friend); both texts ground Abraham's unique standing in faith."},
            {"type": "allusion", "target": "John 15:14", "note": "You are my friends if you do what I command you — Jesus's elevation of the disciples to friends echoes the title God gives Abraham in Isa 41:8; what was unique to Abraham (called my friend) is now extended through Christ to all who abide in him."}
        ],
        "10": [
            {"type": "allusion", "target": "Acts 18:9-10", "note": "Do not be afraid, for I am with you — the LORD's reassurance to Israel in Isa 41:10 is repeated to Paul in a night vision at Corinth (Acts 18:9-10: 'Do not be afraid... for I am with you'); the covenant presence-promise of Isa 41 is extended through Christ to Paul's missionary work among the Gentiles."},
            {"type": "allusion", "target": "Matt 28:20", "note": "I am with you always, to the end of the age — Jesus's parting promise echoes the covenant reassurance formula of Isa 41:10 (I am with you); the presence that Israel received from the LORD is now given by the risen Christ to the church in its mission to all nations."}
        ],
        "14": [
            {"type": "allusion", "target": "Titus 2:14", "note": "Who gave himself for us to redeem us from all lawlessness — the title Redeemer (Isa 41:14: your Redeemer is the Holy One of Israel) is fulfilled in Christ who gives himself as the ransom; the Holy One of Israel who redeems the worm Jacob is the same Holy One who takes human flesh to redeem his people from iniquity."}
        ],
        "18": [
            {"type": "allusion", "target": "John 7:38", "note": "I will open rivers on the bare heights and fountains in the midst of the valleys; I will make the wilderness a pool of water — the water-in-the-desert promise of Isa 41:18 feeds into Jesus's Tabernacles declaration (John 7:38: rivers of living water from the believer); the Spirit is the water that transforms the dry land."}
        ]
    },
    "42": {
        "6": [
            {"type": "citation", "target": "Luke 2:32", "note": "A light for revelation to the Gentiles, and for glory to your people Israel — Simeon's nunc dimittis (Luke 2:32) is a direct citation of Isa 42:6 (I will give you as a covenant for the people, a light for the nations); the infant Jesus is identified as the fulfillment of the Servant's mission to be light for the Gentiles."},
            {"type": "citation", "target": "Acts 13:47", "note": "I have made you a light for the Gentiles, that you may bring salvation to the ends of the earth — Paul and Barnabas directly cite Isa 42:6 (via Isa 49:6) to justify turning to the Gentiles; the Servant's commission to be a light to the nations is the scriptural mandate for the Gentile mission of the church."}
        ],
        "7": [
            {"type": "citation", "target": "Luke 4:18", "note": "He has sent me to proclaim liberty to the captives and recovering of sight to the blind — Jesus's Nazareth manifesto (Luke 4:18) combines Isa 61:1 with Isa 42:7 (to open the eyes that are blind, to bring out the prisoners from the dungeon); Jesus presents himself as the Servant of Isa 42 fulfilling the mission of liberation."}
        ],
        "9": [
            {"type": "allusion", "target": "Rev 21:5", "note": "Behold, the former things have come to pass, and new things I now declare — God's announcement of new things in Isa 42:9 anticipates the eschatological declaration of Rev 21:5 (Behold, I am making all things new); what Isaiah declares as future prophecy is announced as accomplished reality in John's vision of the new creation."}
        ],
        "10": [
            {"type": "allusion", "target": "Rev 5:9", "note": "Sing to the LORD a new song — the call to a new song in Isa 42:10 anticipates the heavenly throne room in Rev 5:9 where the living creatures and elders sing a new song to the Lamb who was slain; the new song prompted by the LORD's triumph becomes the eternal new song of the Lamb's redemption in Revelation."}
        ],
        "16": [
            {"type": "allusion", "target": "John 8:12", "note": "I will turn the darkness before them into light — the divine guide who turns darkness to light for the blind of Isa 42:16 is the figure Jesus identifies himself as in John 8:12 (I am the light of the world; whoever follows me will not walk in darkness but will have the light of life); the Servant of Isa 42 is the light."}
        ]
    },
    "43": {
        "2": [
            {"type": "allusion", "target": "Dan 3:25", "note": "When you pass through the waters, I will be with you; when you walk through fire you shall not be burned — the promise of Isa 43:2 is typologically demonstrated by Shadrach, Meshach, and Abednego in Dan 3:25, where a figure 'like a son of God' accompanies them in the furnace; the presence of God in trial points forward to Christ's presence with his people in suffering."},
            {"type": "allusion", "target": "1 Pet 4:12", "note": "Do not be surprised at the fiery trial when it comes upon you to test you — Peter's encouragement to persecuted Christians draws on the OT pattern of God's people passing through fire and water (Isa 43:2); the promise that God is present in the trial is the ground of endurance under suffering."}
        ],
        "3": [
            {"type": "allusion", "target": "1 Tim 2:6", "note": "I am the LORD your God, the Holy One of Israel, your Savior; I give Egypt as your ransom — the ransom-language of Isa 43:3 anticipates 1 Tim 2:6 (Christ Jesus, who gave himself as a ransom for all); the God who ransomed Israel from Egypt gives his Son as the ransom for the world."}
        ],
        "10": [
            {"type": "allusion", "target": "John 8:24", "note": "Unless you believe that I am he you will die in your sins — Jesus's ego eimi declaration in John 8:24 directly echoes Isa 43:10 ('I am he') and 43:13; the absolute 'I am' without predicate in John 8 is a claim to the divine name of Isa 43, identifying Jesus with the LORD who alone is God and Savior."},
            {"type": "allusion", "target": "John 8:58", "note": "Before Abraham was, I am — Jesus's climactic ego eimi in John 8:58 draws on the timeless divine self-predication of Isa 43:10-13 (you are my witnesses... that I am he; before me no god was formed); the pre-existence claim echoes the LORD's assertion of eternal uniqueness in Isaiah."}
        ],
        "18": [
            {"type": "allusion", "target": "2 Cor 5:17", "note": "Remember not the former things, nor consider the things of old; behold I am doing a new thing — Paul's declaration (if anyone is in Christ, he is a new creation; the old has passed away; behold, the new has come) is the direct fulfillment of Isa 43:18-19; the new thing God promised through the Servant is the new creation inaugurated in Christ's resurrection."},
            {"type": "allusion", "target": "Rev 21:5", "note": "Behold, I am doing a new thing — Rev 21:5 (Behold, I am making all things new) is the eschatological completion of Isa 43:19; what Isa 43 declared as an imminent new act of God is fulfilled in stages: first in the return from exile, then in Christ's resurrection, and finally in the new creation of Rev 21."}
        ],
        "25": [
            {"type": "allusion", "target": "Mark 2:7", "note": "I, I am he who blots out your transgressions for my own sake — when Jesus declares 'your sins are forgiven' (Mark 2:5), the scribes ask 'Who can forgive sins but God alone?' (Mark 2:7); they correctly recall Isa 43:25, where only God says 'I blot out your transgressions'; Jesus's claim to forgive is a claim to the divine prerogative of Isa 43."},
            {"type": "allusion", "target": "Col 2:14", "note": "He who blots out your transgressions — the divine act of erasing sin in Isa 43:25 is accomplished in Christ through the cross; Col 2:14 describes God canceling the record of debt by nailing it to the cross, the definitive enactment of what Isa 43:25 promised: a God who blots out transgression for his own sake."}
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
