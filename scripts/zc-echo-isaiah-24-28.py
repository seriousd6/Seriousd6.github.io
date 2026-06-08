"""
echo | Isaiah | 24-28 | python3 scripts/zc-echo-isaiah-24-28.py

Ch 25:8 (1 Cor 15:54 / Rev 21:4) and Ch 28:11,16 (1 Cor 14:21, Rom 9:33, 1 Pet 2:6) already in file.
This script adds the remaining chapters and supplementary verses.

Key echo decisions:
- Isa 24:21-22 (host of heaven imprisoned) → Rev 20:2-3 / Jude 6: cosmic powers bound
- Isa 24:23 (LORD outshines sun/moon) → Rev 21:23: no need of sun in new Jerusalem
- Isa 25:6-7 (messianic feast, veil lifted) → Rev 19:9 / Luke 14:15-24 / 2 Cor 3:16
- Isa 26:19 (your dead shall live) → John 5:28-29 / 1 Thess 4:16: resurrection ground text
- Isa 26:20 (hide for a little while) → Heb 10:37: the coming one will not delay
- Isa 27:9 (covenant removes sins) → Rom 11:27: directly quoted by Paul
- Isa 27:13 (great trumpet gathers) → Matt 24:31 / 1 Thess 4:16: eschatological trumpet
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
    "24": {
        "1": [
            {"type": "allusion", "target": "Rev 6:12-14", "note": "The earth made empty and waste, turned upside down — the cosmic upheaval of Isa 24 (the Little Apocalypse) is the OT prototype for Rev 6's seal judgments; the heavens rolled up and earth shaken share the same apocalyptic grammar."},
            {"type": "allusion", "target": "Matt 24:29", "note": "Immediately after the tribulation, the sun darkened and moon not give its light — Jesus draws on the cosmic-catastrophe imagery of Isa 24 for his eschatological discourse; the darkening of luminaries is the OT apocalyptic language Jesus inherits and reapplies to his own return."}
        ],
        "17": [
            {"type": "allusion", "target": "Luke 21:26", "note": "People fainting with fear and foreboding of what is coming on the world — Jesus's eschatological discourse in Luke 21 uses the same inescapable terror logic of Isa 24:17-18 (pit and snare and net); whoever flees the pit falls into the snare, the inescapability of divine judgment characterizes both passages."}
        ],
        "21": [
            {"type": "allusion", "target": "Rev 20:2-3", "note": "The LORD will punish the host of heaven and the kings of the earth — the binding and imprisonment of cosmic powers in Isa 24:21-22 (shut up in prison for many days) is the OT prototype for Rev 20:2-3's binding of Satan for a thousand years; the pattern of cosmic arrest followed by final visitation is identical."},
            {"type": "allusion", "target": "Jude 6", "note": "Angels who did not keep their own position kept in eternal chains in gloomy darkness until the judgment — the imprisonment of the host of heaven in Isa 24:22 (gathered in a pit and shut up) is the background for Jude's reference to the fallen watchers awaiting their sentence."}
        ],
        "23": [
            {"type": "allusion", "target": "Rev 21:23", "note": "The new Jerusalem has no need of sun or moon because the glory of God gives it light — Rev 21:23 fulfills Isa 24:23, where the LORD reigns on Mount Zion in glory so blazing that moon and sun are abashed; the LORD's direct presence replaces created luminaries in both visions."}
        ]
    },
    "25": {
        "6": [
            {"type": "type", "target": "Rev 19:9", "note": "Blessed are those invited to the wedding feast of the Lamb — the rich messianic banquet on Mount Zion for all peoples in Isa 25:6 is the OT archetype of the marriage supper of the Lamb; the choicest food and well-aged wine point forward to the eschatological feast Christ hosts in the new creation."},
            {"type": "allusion", "target": "Luke 14:15-24", "note": "Blessed is everyone who will eat bread in the kingdom of God — the parable of the great banquet (Luke 14) is Jesus's reinterpretation of the Isa 25:6 feast; the invitation goes out to all peoples, and those who make excuses are shut out while the poor and lame are brought in."}
        ],
        "7": [
            {"type": "allusion", "target": "2 Cor 3:16", "note": "When one turns to the Lord, the veil is removed — the covering cast over all peoples in Isa 25:7 (the veil spread over the nations) is the OT image Paul applies to the reading of Moses without Christ; the shroud that blinds is the type of the veil on the heart removed only by turning to the Lord in the Spirit."}
        ]
    },
    "26": {
        "11": [
            {"type": "allusion", "target": "Heb 10:27", "note": "A fearful expectation of judgment and a fury of fire that will consume the adversaries — the fire consuming God's enemies in Isa 26:11 is the conceptual background for Heb 10:27's warning about what awaits those who willfully reject Christ after receiving the knowledge of the truth."}
        ],
        "19": [
            {"type": "fulfillment", "target": "John 5:28-29", "note": "The hour is coming when all who are in the tombs will hear his voice and come out — Jesus's resurrection declaration draws on Isa 26:19 (your dead shall live; their bodies shall rise); the dew of light as the agent of resurrection points forward to Christ, who is himself the resurrection and the life."},
            {"type": "allusion", "target": "1 Thess 4:16", "note": "The dead in Christ will rise first — the general resurrection motif of Isa 26:19 (awake and sing, you who dwell in the dust) is the OT ground of Paul's resurrection confidence; the awakening from the dust is inaugurated in Christ's resurrection and will be completed at his parousia."}
        ],
        "20": [
            {"type": "allusion", "target": "Heb 10:37", "note": "Yet a little while, and the coming one will come and will not delay — the author of Hebrews directly adapts Isa 26:20 (hide yourself for a little while until the fury has passed) alongside Hab 2:3-4; the sheltering until judgment passes becomes the NT posture of patient faith awaiting the returning Christ."}
        ]
    },
    "27": {
        "9": [
            {"type": "quote", "target": "Rom 11:27", "note": "This will be my covenant with them when I take away their sins — Paul directly quotes Isa 27:9 in his climactic conclusion to the olive-tree discourse (Rom 11:26-27); the removal of Jacob's sin by covenant is Paul's OT scriptural ground for Israel's future salvation through the Deliverer who comes from Zion."}
        ],
        "13": [
            {"type": "allusion", "target": "Matt 24:31", "note": "He will send out his angels with a loud trumpet call, and they will gather his elect from the four winds — the great trumpet of Isa 27:13 gathering dispersed Israel from Assyria and Egypt is the OT prototype for Jesus's eschatological gathering of the elect; the one great trumpet signals the end of exile and the ingathering of God's people."},
            {"type": "allusion", "target": "1 Thess 4:16", "note": "The Lord will descend with a loud command and with the trumpet of God — the gathering trumpet of Isa 27:13 is the eschatological instrument of Christ's parousia; what began as a trumpet call for scattered Israel becomes in Paul the trumpet announcing the resurrection of the dead and the meeting with the Lord."}
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
