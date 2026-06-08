"""
echo | Isaiah | 33-36 | python3 scripts/zc-echo-isaiah-33-36.py

Ch 34:4 (Rev 6:14) already in file — ch 34 is done by echo rules (any entry = done).
This script adds chs 33, 35, 36 plus supplementary ch 34 entries.

Key echo decisions:
- Isa 33:14 (who can dwell with everlasting burning?) → Heb 12:29: consuming fire
- Isa 33:22 (one lawgiver and judge) → Jas 4:12: direct conceptual parallel
- Isa 35:5-6 (blind see, lame walk, deaf hear) → Matt 11:5: DIRECT CITATION by Jesus
  as proof of messianic identity; Jesus quotes Isa 35 as the answer to John's question
- Isa 35:8 (the Way of Holiness) → John 14:6: Jesus as the Way
- Isa 35:10 (everlasting joy, sorrow flees) → Rev 21:4: new creation fulfillment
- Isa 34:8 (day of vengeance for Zion's cause) → Rev 19:2: judgment of Babylon
- Isa 36 (Hezekiah narrative) → limited direct NT echo; key typological connection
  is Hezekiah as type of Christ, not destroyed by the Assyrian (death) who threats
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
    "33": {
        "6": [
            {"type": "allusion", "target": "Col 2:3", "note": "In Christ are hidden all the treasures of wisdom and knowledge — Isa 33:6's promise that wisdom and knowledge shall be the stability of the times, the fear of the LORD his treasure, anticipates Paul's declaration that all such treasure is hidden in Christ; the covenantal stability Israel sought in wisdom is now located in the person of the Son."}
        ],
        "14": [
            {"type": "allusion", "target": "Heb 12:29", "note": "Our God is a consuming fire — Heb 12:29 quotes Deut 4:24 but the rhetorical question of Isa 33:14 (who among us can dwell with the consuming fire? who can live with everlasting burning?) provides the same logic; both passages press toward the same answer: only those whose sins are covered by Christ's blood can stand before the holy fire of God."}
        ],
        "15": [
            {"type": "allusion", "target": "Matt 5:8", "note": "Blessed are the pure in heart, for they shall see God — the righteous man of Isa 33:15-16 (who walks righteously, speaks uprightly, stops his ears from hearing of bloodshed) shall dwell on the heights and see the king in his beauty (v17); Jesus's Beatitude is the new-covenant distillation of the Isaianic portrait of the one who dwells with God."}
        ],
        "17": [
            {"type": "allusion", "target": "Rev 22:4", "note": "They will see his face — the promise that the righteous shall see the king in his beauty (Isa 33:17) is the OT anticipation of Rev 22:4's crowning promise that his servants shall see his face; the vision of the enthroned king that was conditional in Isa 33 is given freely to all the redeemed in the new Jerusalem."}
        ],
        "20": [
            {"type": "allusion", "target": "Heb 11:10", "note": "The city of our appointed feasts — Isa 33:20's vision of Jerusalem as the unmoving tent, the quiet habitation, points forward to Heb 11:10's city with foundations whose designer and builder is God; the earthly Zion that could not be shaken (Isa 33:20 — its stakes will never be pulled up) is fulfilled in the unshakeable heavenly city."},
            {"type": "allusion", "target": "Rev 21:2", "note": "I saw the holy city, the new Jerusalem, coming down out of heaven — the quiet habitation of Isa 33:20, the tabernacle of God with his people where no galley ship can come, is the OT anticipation of the new Jerusalem that descends as the eternal dwelling; both texts describe the permanent, unassailable city of God's presence."}
        ],
        "22": [
            {"type": "allusion", "target": "Jas 4:12", "note": "There is only one lawgiver and judge, he who is able to save and to destroy — James directly echoes Isa 33:22 (the LORD is our judge, the LORD is our lawgiver, the LORD is our king; he will save us); both texts insist on a single divine sovereign who combines legislative, judicial, and saving authority, which is fulfilled in Christ (John 5:22; Acts 5:31)."}
        ],
        "24": [
            {"type": "allusion", "target": "Mark 2:5-10", "note": "No inhabitant will say I am sick; the people who dwell there will be forgiven their iniquity — the eschatological Zion of Isa 33:24 links physical healing with the forgiveness of sin; Jesus's healing of the paralytic (Mark 2:5-10) makes the same connection, claiming authority to forgive sins as the validation of messianic healing power."}
        ]
    },
    "34": {
        "8": [
            {"type": "allusion", "target": "Rev 19:2", "note": "For the LORD has a day of vengeance, a year of recompense for the cause of Zion — Rev 19:2 echoes this pattern in the angel's declaration that God has judged Babylon the great and avenged the blood of his servants; the day of vengeance for Zion's cause (Isa 34) finds its ultimate fulfillment in the judgment of spiritual Babylon."}
        ],
        "10": [
            {"type": "allusion", "target": "Rev 14:11", "note": "The smoke of Edom shall go up forever; from generation to generation it shall lie waste — Rev 14:11 applies the same language of eternal smoke to the judgment of those who worship the beast; Isaiah's oracle against Edom (the type of all enemies of God's people) becomes Revelation's image for final eschatological judgment."},
            {"type": "allusion", "target": "Rev 19:3", "note": "The smoke goes up forever and ever — Rev 19:3 uses this precise language from Isa 34:10 to describe the fall of Babylon; the eternal smoking of Edom is the OT archetype for the finality of divine judgment."}
        ]
    },
    "35": {
        "1": [
            {"type": "allusion", "target": "Rev 22:1-3", "note": "The wilderness and the dry land shall be glad; the desert shall rejoice and blossom like a crocus — the blooming desert of Isa 35 is the OT vision of the new creation that Rev 22 fulfills in the river of life flowing from the throne through a verdant garden-city; what was barren becomes abundantly fruitful through God's direct presence."}
        ],
        "3": [
            {"type": "allusion", "target": "Heb 12:12", "note": "Strengthen the weak hands and make firm the feeble knees — Heb 12:12 directly quotes Isa 35:3, applying it to the endurance of Christians under trial; the exhortation to strengthen what is drooping is fulfilled in the community of believers who run the race set before them by looking to Jesus."}
        ],
        "5": [
            {"type": "citation", "target": "Matt 11:5", "note": "The blind receive their sight and the lame walk, lepers are cleansed and the deaf hear — Jesus directly cites Isa 35:5-6 in his answer to John the Baptist's question (Matt 11:4-5; Luke 7:22): 'Go and tell John what you hear and see.' This is Jesus's definitive self-identification as the fulfillment of Isa 35; the signs of healing are the messianic credentials prophesied here."},
            {"type": "citation", "target": "Luke 7:22", "note": "Jesus answered them: Go and tell John what you have seen and heard — the blind see, the lame walk, lepers are cleansed, the deaf hear, the dead are raised (Luke 7:22) is a direct citation of Isa 35:5-6 expanded with Isa 61:1; Jesus's healing ministry is not just compassion but prophetic sign-fulfillment of Isaiah's messianic portrait."}
        ],
        "6": [
            {"type": "allusion", "target": "John 7:38", "note": "Waters break forth in the wilderness and streams in the desert — the water springing up in the dry land of Isa 35:6-7 is the OT type of the living water Jesus promises: rivers of living water flowing from the believer (John 7:38), which John interprets as the Spirit; both Isaiah and Jesus use water-in-the-desert as the sign of eschatological life."}
        ],
        "8": [
            {"type": "allusion", "target": "John 14:6", "note": "A highway shall be there, and it shall be called the Way of Holiness — the Way of Holiness in Isa 35:8 (on which the unclean shall not pass; it is for those who walk on the way) points directly to Jesus's declaration 'I am the way, and the truth, and the life' (John 14:6); Jesus is himself the Way of Holiness on which God's pilgrim people travel."}
        ],
        "10": [
            {"type": "fulfillment", "target": "Rev 21:4", "note": "The ransomed of the LORD shall return and come to Zion with singing; everlasting joy shall be upon their heads; sorrow and sighing shall flee away — Rev 21:4 directly fulfills Isa 35:10: God will wipe away every tear from their eyes, and death shall be no more, neither shall there be mourning, nor crying, nor pain; what Isa 35 promises for the restored exiles is given in its fullness to the redeemed of every nation in the new creation."}
        ]
    },
    "36": {
        "6": [
            {"type": "allusion", "target": "2 Cor 1:9", "note": "A broken reed is Egypt — the Rabshakeh's taunt that trusting Egypt is like leaning on a broken reed that will pierce the hand anticipates the NT critique of trusting in human strength; Paul's 'not trusting in ourselves but in God who raises the dead' (2 Cor 1:9) is the theological resolution to Hezekiah's predicament."}
        ],
        "15": [
            {"type": "type", "target": "Rom 10:11", "note": "Do not let Hezekiah make you trust in the LORD — the Rabshakeh's mockery of trust in God becomes, by contrast, the very posture the NT requires; Rom 10:11 cites Isa 28:16 (no one who believes in him will be put to shame), and Hezekiah's preserved trust in the LORD that is vindicated in ch 37 is the OT type of saving faith."}
        ],
        "18": [
            {"type": "type", "target": "Rev 17:14", "note": "Has any of the gods of the nations delivered his land out of the hand of the king of Assyria? — the Rabshakeh's boast that no national god could resist Assyria is the OT type of the beast's claim to sovereignty; Rev 17:14's response — the Lamb will conquer them — is the ultimate answer to this taunt, demonstrating that the LORD whom Hezekiah trusted is the King of kings."}
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
