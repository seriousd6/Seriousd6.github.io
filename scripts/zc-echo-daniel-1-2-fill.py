"""Echo fill: Daniel 1–2
Type: echo
Book: daniel
Run: python3 scripts/zc-echo-daniel-1-2-fill.py

Fills ch 1 (completely missing) and adds supplemental entries to ch 2 beyond the
existing v.44 seed from the combined script.

Ch 1: Faithful exiles in Babylon — food test, divine favor, superior wisdom.
  Key echoes: Joseph parallel (Acts 7:9-10), undefiled servant (Heb 7:26),
  favor with God and man (Luke 2:52), testing by food (Matt 4:1-11),
  superior wisdom (1 Cor 1:20-25).
Ch 2 additions: mystery revealed (Col 1:26-27), stone cut without hands
  (Matt 21:42-44; 1 Cor 10:4), prayer for raz disclosed (Rev 1:1).
"""
import json, pathlib
ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))

DANIEL_ECHOES = {
    "1": {
        "2": [
            {
                "type": "theme",
                "target": "Rom 13:1",
                "note": "YHWH gave (natan) Jehoiakim into Nebuchadnezzar's hand — divine sovereignty over catastrophic political defeat. All governing authority is given from above; the exile is not accident but divine permission."
            },
            {
                "type": "allusion",
                "target": "John 19:11",
                "note": "The verb natan (gave) runs through the passion narrative: Pilate has no authority unless given from above. The divine giving of Jehoiakim into Babylonian hands casts the shadow of the Father giving the Son into the hands of his enemies."
            }
        ],
        "6": [
            {
                "type": "allusion",
                "target": "Acts 7:9-10",
                "note": "Daniel and the Judean exiles chosen for the Babylonian court echo Joseph sold into Egypt — Acts 7:9-10 reads Joseph as a type of Christ rejected by his brothers but exalted by God to save many. The Daniel-in-Babylon pattern continues the Joseph-in-Egypt typological sequence that culminates in Christ."
            }
        ],
        "8": [
            {
                "type": "allusion",
                "target": "Heb 7:26",
                "note": "Daniel's resolve not to defile himself with the king's food anticipates the holiness of the true high priest — holy, innocent, unstained, separated from sinners. The food-separation is a shadow of the undefiled servant who remained uncorrupted by imperial pressure."
            }
        ],
        "9": [
            {
                "type": "allusion",
                "target": "Luke 2:52",
                "note": "God granted Daniel favor and compassion before the chief official — the same divine bestowal as Jesus who increased in favor with God and man (Luke 2:52). Both the exiled Daniel and the child Jesus in a world hostile to their mission receive divine favor that opens closed doors."
            }
        ],
        "12": [
            {
                "type": "allusion",
                "target": "Matt 4:1-11",
                "note": "The ten-day food test in Babylon — test us, see if we look better — parallels the wilderness temptation of Jesus, which also centered on food (Matt 4:3: command these stones to become bread). Both test whether the faithful servant will compromise covenant identity under imperial and satanic pressure."
            },
            {
                "type": "allusion",
                "target": "Heb 4:15",
                "note": "Daniel and his companions tested in all the same ways as the Babylonian court yet did not defile themselves — the pattern of one tested in all things yet without sin. The Danielic faithful are anticipatory types of the perfectly tested Son."
            }
        ],
        "17": [
            {
                "type": "allusion",
                "target": "Col 2:3",
                "note": "God gave these four young men knowledge and skill in all literature and wisdom, and to Daniel the understanding of visions — in Christ are all treasures of wisdom and knowledge hidden (Col 2:3). Daniel's gift of extraordinary wisdom is a foretaste of the one in whom all divine wisdom dwells bodily."
            },
            {
                "type": "allusion",
                "target": "Rev 1:1",
                "note": "Daniel received the ability to understand visions and dreams (v.17) — establishing the OT vision-interpretation tradition that flows through Daniel's apocalyptic chapters into the Revelation given to Christ and transmitted to John. The gift of understanding heavenly disclosure connects Daniel directly to the Apocalypse."
            }
        ],
        "20": [
            {
                "type": "allusion",
                "target": "1 Cor 1:20",
                "note": "Daniel and friends found ten times wiser than all the magicians and enchanters of Babylon — the wisdom of the covenant community surpassing the wisdom of the world-empire. Paul's argument that the foolishness of God is wiser than men (1 Cor 1:25) draws on this same pattern: divine wisdom in a despised form overturning the intellectual supremacy of the age."
            }
        ]
    },
    "2": {
        "18": [
            {
                "type": "theme",
                "target": "Eph 1:9",
                "note": "Daniel urges his companions to seek mercy concerning the mystery (Aramaic raz) — Paul uses the cognate mystery (musterion) for God's revealed will in Christ (Eph 1:9). The prayer for divine disclosure of hidden heavenly realities is the OT pattern of what God does definitively in the gospel."
            }
        ],
        "28": [
            {
                "type": "allusion",
                "target": "Rev 1:1",
                "note": "There is a God in heaven who reveals mysteries, and he has made known what will be in the latter days — the exact pattern and vocabulary of Revelation: God revealing to his servant what must soon take place. Daniel's raz-disclosure structure is fulfilled in the Revelation of Jesus Christ."
            },
            {
                "type": "allusion",
                "target": "Col 1:26-27",
                "note": "The mystery hidden for ages is now disclosed to his saints — Col 1:26-27 identifies what was hidden as Christ in you, the hope of glory. The raz-revelation pattern of Daniel 2 is the OT framework for the Christological mystery Paul announces as now revealed."
            }
        ],
        "34": [
            {
                "type": "fulfillment",
                "target": "Matt 21:42-44",
                "note": "The stone cut without human hands that struck the statue and grew to fill the earth — Jesus applies this directly to himself at the temple: the stone the builders rejected has become the cornerstone; whoever falls on this stone will be broken (Matt 21:42-44). The kingdom that shatters all earthly empires is Christ's own reign, inaugurated at the resurrection."
            },
            {
                "type": "allusion",
                "target": "1 Cor 10:4",
                "note": "Paul identifies the rock in the wilderness as Christ (1 Cor 10:4). The stone of Daniel 2:34-35 — cut without human hands, of supernatural origin — belongs to the same theological trajectory: the Christ-rock that comes from outside human construction to supersede all human-built empires."
            }
        ]
    }
}

def main():
    existing = load_echo("daniel")
    merge_echo(existing, DANIEL_ECHOES)
    save_echo("daniel", existing)

    # Verify ch 1 and ch 2 now have entries
    for ch in ["1", "2"]:
        count = len(existing.get(ch, {}))
        print(f"  ch {ch}: {count} verse(s) with echo entries")

    print("Daniel 1-2 echoes filled.")

if __name__ == "__main__":
    main()
