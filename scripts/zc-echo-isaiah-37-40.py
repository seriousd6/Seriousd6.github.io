"""
echo | Isaiah | 37-40 | python3 scripts/zc-echo-isaiah-37-40.py

Ch 40 already complete (v3 → John's baptism, v6 → 1 Pet 1:24-25, v13 → Rom 11:34).
This script adds chs 37, 38, 39.

Key echo decisions:
- Isa 37:16 (you alone are LORD of all kingdoms) → Rev 4:11: sovereignty confession
- Isa 37:19 (idols are not gods) → 1 Cor 8:4: Paul's explicit echo of this OT logic
- Isa 37:36 (angel strikes 185,000) → Rev 19:11-21: type of eschatological military defeat
- Isa 38:10 (gates of Sheol) → Rev 1:18: Christ holds the keys of Death and Hades
- Isa 38:17 (sins cast behind God's back) → Col 2:14: debt cancelled; record nailed to cross
- Isa 38:18-19 (dead cannot praise God) → 1 Cor 15:55-57: resurrection breaks Sheol's silence
- Isa 39:6-7 (exile to Babylon announced) → Luke 21:24 / Acts 7:43: Babylon exile as type
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
    "37": {
        "16": [
            {"type": "allusion", "target": "Rev 4:11", "note": "O LORD of hosts, God of Israel, you alone are the God of all kingdoms of the earth; you have made heaven and earth — Hezekiah's prayer of absolute monotheism and Creator-sovereignty echoes in Rev 4:11 (Worthy are you, our Lord and God, to receive glory and honor and power, for you created all things); the throne-room doxology in Revelation is the eschatological fulfillment of the sovereignty claim Hezekiah made in prayer."},
            {"type": "allusion", "target": "Acts 17:24", "note": "The God who made the world and everything in it, being Lord of heaven and earth — Paul's Areopagus speech echoes Hezekiah's confession (Isa 37:16) that the LORD made heaven and earth; the monotheistic Creator-claim is both the ground of Hezekiah's prayer and the premise of Paul's proclamation to the nations."}
        ],
        "19": [
            {"type": "allusion", "target": "1 Cor 8:4", "note": "An idol is nothing at all in the world, and there is no God but one — Paul's declaration directly reflects the OT logic of Isa 37:19 (the gods of the nations are no gods; they are the work of human hands, wood and stone); Hezekiah's prayer articulates the axiomatic distinction between the living God and manufactured idols that Paul applies to meat offered to idols."}
        ],
        "31": [
            {"type": "allusion", "target": "John 15:5", "note": "The surviving remnant of the house of Judah shall again take root downward and bear fruit upward — the organic metaphor of the remnant rooted and fruitful anticipates Jesus's vine-and-branches teaching (John 15:5); the fruitbearing comes from remaining attached to the living source, just as Judah's survival comes from being rooted in the LORD."}
        ],
        "36": [
            {"type": "type", "target": "Rev 19:11-21", "note": "The angel of the LORD went out and struck down 185,000 in the Assyrian camp — a single divine agent annihilating an entire army overnight is the most dramatic type in the OT of the eschatological defeat of God's enemies; Rev 19:11-21 depicts the rider on the white horse striking down the nations, the final antitype of this event."}
        ]
    },
    "38": {
        "10": [
            {"type": "allusion", "target": "Rev 1:18", "note": "I said in the middle of my days I must depart; I am consigned to the gates of Sheol for the rest of my years — Hezekiah's descent to the gates of death is the OT personal prototype of the mortal crisis Christ entered through crucifixion; but where Hezekiah merely approached the gates, Christ descended into death and rose with the keys of Death and Hades (Rev 1:18), so no one who trusts him need pass through those gates permanently."}
        ],
        "11": [
            {"type": "allusion", "target": "Ps 116:9", "note": "I shall look on the LORD no more in the land of the living — Hezekiah's lament that death separates from the covenant community of worship anticipates Ps 116:9 (I will walk before the LORD in the land of the living) and the resurrection hope; the NT answers Hezekiah's despair by declaring that in Christ there is no final separation from the presence of God."}
        ],
        "17": [
            {"type": "allusion", "target": "Col 2:14", "note": "You have cast all my sins behind your back — the complete, backward-casting forgiveness Hezekiah received anticipates the complete cancellation of the debt record that Col 2:14 describes: God has forgiven our trespasses, canceling the record of debt that stood against us by nailing it to the cross; both texts describe divine forgiveness as a definitive, irreversible act."},
            {"type": "allusion", "target": "Heb 9:22", "note": "Without the shedding of blood there is no forgiveness — the forgiveness Hezekiah experienced (you have cast all my sins behind your back, v17) required a ground; Heb 9:22 locates that ground in blood-atonement, which in the OT was the sacrificial system and in the NT is the blood of Christ; Hezekiah's forgiveness was a promissory note drawn on Christ's sacrifice."}
        ],
        "18": [
            {"type": "allusion", "target": "1 Cor 15:55", "note": "Sheol does not thank you; death does not praise you; those who go down to the pit do not hope for your faithfulness — this lament (that the dead cannot praise God) is the precise problem that Christ's resurrection answers; 1 Cor 15:55 (O death, where is your victory?) is the triumphant reversal of Hezekiah's canticle, enabled by the resurrection of Christ."},
            {"type": "allusion", "target": "Rev 5:9-14", "note": "The dead cannot praise God — the silence of Sheol in Isa 38:18 is shattered by the endless praise of the Lamb in Rev 5:9-14; every creature in heaven, on earth, and under the earth joins the new song, the eschatological answer to Hezekiah's lament that death ends worship."}
        ],
        "20": [
            {"type": "allusion", "target": "Rev 15:3", "note": "The LORD will save me, and we will sing my songs with stringed instruments all the days of our lives at the house of the LORD — Hezekiah's vow to sing praise in the temple all his days is the prototype of the eternal praise in the heavenly sanctuary; Rev 15:3 depicts the victorious singing the song of Moses and the Lamb in the temple of God — the ultimate fulfillment of this vow."}
        ]
    },
    "39": {
        "6": [
            {"type": "type", "target": "Luke 21:24", "note": "Behold, the days are coming when all that is in your house shall be carried to Babylon — Isaiah's announcement to Hezekiah that the Babylonian exile will come follows the same prophetic pattern Jesus applies to Jerusalem's destruction by Rome (Luke 21:24: Jerusalem will be trampled underfoot by the Gentiles); both events are divine judgment following Israel's unfaithfulness, and both are announced by a prophet to a generation that will not personally suffer them."},
            {"type": "allusion", "target": "Acts 7:43", "note": "I will send you into exile beyond Babylon — Stephen's speech (Acts 7:43) cites the Babylon exile as the culmination of Israel's long pattern of rejecting God's word; Isa 39:6 is the prophetic announcement of that exile, and both texts use Babylon as the place of divine judgment for covenant unfaithfulness."}
        ],
        "7": [
            {"type": "type", "target": "Matt 1:11-12", "note": "Some of your own sons who will come from you shall be taken away and shall be eunuchs in the palace of the king of Babylon — the deportation of Judah's sons to Babylon is the historical event that Matt 1:11-12 marks as a turning point in Jesus's genealogy (the deportation to Babylon); Christ enters the genealogy at the point of the exile, making him the one who comes out of the depths of Israel's judgment to bring restoration."}
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
