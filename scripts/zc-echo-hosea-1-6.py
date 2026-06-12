"""
echo | hosea | chapters 1-6 (gap-fill: chs 3, 4, 5 missing)
Run: python3 scripts/zc-echo-hosea-1-6.py

Adds echo entries for Hosea 3-5 only; chs 1, 2, 6 already populated
by the earlier multi-book script. merge_echo skips existing entries.

Key canonical connections:
- 3:5: "David their king ... in the latter days" → Davidic Messiah; Rom 11:26
- 4:6: "destroyed for lack of knowledge" → John 1:10; Col 2:2-3 (contrast)
- 5:15: divine withdrawal until acknowledgment → Matt 23:39 (Jesus' departure/return)
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).parent.parent


def load_echo(book):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def save_echo(book, data):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  wrote {p.relative_to(ROOT)}")


def merge_echo(existing, new_data):
    # INTENT: Adds only absent verse keys; for present keys adds only unseen type+target pairs.
    for ch, verses in new_data.items():
        existing.setdefault(ch, {})
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e["type"], e["target"]) for e in existing[ch][v]}
                for e in entries:
                    if (e["type"], e["target"]) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e["type"], e["target"]))


HOSEA_ECHOES = {
    "3": {
        "5": [
            {
                "type": "allusion",
                "target": "Rom 11:26",
                "note": "Afterward the children of Israel will return and seek the LORD their God and David their king, and they will come trembling to the LORD and to his goodness in the latter days — Paul's conviction that 'all Israel will be saved' (Rom 11:26) draws on this pattern of eschatological return: Israel currently in partial hardening, but the 'latter days' restoration Hosea foresees remains on YHWH's calendar; the Messiah is the 'David their king' they will ultimately seek"
            },
            {
                "type": "type",
                "target": "Luke 1:32",
                "note": "David their king — the Davidic Messiah whom Israel will seek in the latter days; Gabriel announces to Mary that Jesus will receive 'the throne of his father David' (Luke 1:32); the eschatological David of Hosea 3:5, Ezek 34:23-24, and Jer 30:9 is identified with Jesus in the NT's typological reading"
            }
        ]
    },
    "4": {
        "6": [
            {
                "type": "allusion",
                "target": "John 1:10",
                "note": "My people are destroyed for lack of knowledge — the destruction through ignorance of God reaches its apex in John 1:10-11: 'the world did not know him; his own people did not receive him'; the very knowledge of God that Hosea identifies as Israel's saving need arrives in the person of the Logos, and is still rejected; the 'lack of knowledge' is not intellectual but relational — refusing the covenant relationship with YHWH"
            },
            {
                "type": "allusion",
                "target": "Col 2:2-3",
                "note": "My people are destroyed for lack of knowledge — Paul declares that in Christ 'are hidden all the treasures of wisdom and knowledge' (Col 2:2-3); Christ is the answer to Hosea's diagnosis: the people were destroyed for lack of knowledge precisely of the God who would be revealed in Jesus; the remedy to Hosea 4:6 is Colossians 2:3"
            }
        ]
    },
    "5": {
        "14": [
            {
                "type": "allusion",
                "target": "Rev 5:5",
                "note": "I will be like a lion to Ephraim, like a young lion to the house of Judah — the lion imagery for YHWH's devastating judgment in Hosea is taken up and transformed in Revelation 5:5, where Christ is 'the Lion of the tribe of Judah'; the terrifying lion of divine judgment is the same one who, as the Lamb, absorbs judgment rather than merely inflicting it"
            }
        ],
        "15": [
            {
                "type": "allusion",
                "target": "Matt 23:39",
                "note": "I will return to my place until they acknowledge their guilt and seek my face; in their distress they will earnestly seek me — Jesus explicitly enacts this pattern in Matthew 23:39: 'you will not see me again, until you say, Blessed is he who comes in the name of the Lord'; as YHWH withdraws to 'his place' until Israel acknowledges its guilt, so Jesus withdraws from Jerusalem, conditioning his visible return on the acknowledgment he Hosea predicted; the pattern is divine withdrawal → Israel's distress → acknowledgment → eschatological return"
            }
        ]
    }
}


def main():
    existing = load_echo("hosea")
    merge_echo(existing, HOSEA_ECHOES)
    save_echo("hosea", existing)
    print("Hosea 1-6 echo (chs 3-5 gap-fill) written.")


if __name__ == "__main__":
    main()
