"""
echo layer: Ezekiel 1-5
Covers missing chapters 3-5 (chs 1-2 already seeded); key NT allusion points:
  - ch3 eat-the-scroll (Rev 10), watchman blood-guilt (Acts 20)
  - ch4 bearing-iniquity type (Heb 9)
  - ch5 Jerusalem-center (Luke 24:47), defiled sanctuary (John 2:19)
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
  "3": {
    "3": [
      {"type": "allusion", "target": "Rev 10:9-10", "note": "Eat this scroll — it was sweet as honey in my mouth: Revelation's seer is commanded to eat a little scroll that is sweet as honey in the mouth but bitter in the stomach (Rev 10:9-10); the direct repetition of the Ezekielian eating-the-scroll vision transfers the prophetic commissioning pattern to John's apocalyptic mission"},
      {"type": "allusion", "target": "Ps 19:10", "note": "The word of God sweeter than honey and the honeycomb (Ps 19:10) — Ezekiel's physical experience of eating the scroll and finding it honey-sweet is the enacted form of the Psalmist's metaphor; the sweetness of divine speech consumed by the prophet is the pattern for all who receive God's word with delight"}
    ],
    "7": [
      {"type": "allusion", "target": "John 12:37-40", "note": "The house of Israel will not listen to you, for they will not listen to me — John 12:37-40 applies Isa 6:10 to explain why the crowds would not believe in Jesus despite seeing his signs; the pattern of prophetic rejection (Ezekiel sent to a hard-headed, stubborn-hearted people) is the pattern Jesus enters and experiences as the final rejected messenger"},
      {"type": "allusion", "target": "Acts 28:25-27", "note": "Hard-headed and stubborn-hearted — Paul's final word to the Roman Jewish community cites Isa 6:9-10 (the same hardening tradition) and concludes: salvation has been sent to the Gentiles and they will listen; the hard-heartedness that makes Ezekiel's mission difficult is the same hardening Paul encounters and which drives the Gentile mission"}
    ],
    "17": [
      {"type": "allusion", "target": "Acts 20:26-27", "note": "I have made you a watchman: give warning from me — Paul's Miletus farewell speech directly echoes the watchman commissioning of Ezekiel 3:17-21: I am innocent of the blood of all of you, for I did not shrink from declaring to you the whole counsel of God (Acts 20:26-27); Paul interprets his apostolic responsibility through Ezekiel's watchman paradigm — the preacher is accountable for delivering the warning"}
    ],
    "18": [
      {"type": "allusion", "target": "Acts 18:6", "note": "I will hold you responsible for his blood — when the Corinthian synagogue rejected Paul's message he shook out his garments and said: your blood be on your own heads; I am innocent (Acts 18:6); the transfer of blood-guilt from the watchman to the unwarned is the direct application of Ezek 3:18 to Paul's apostolic responsibility and his public declaration of innocence"}
    ]
  },
  "4": {
    "4": [
      {"type": "allusion", "target": "Heb 9:28", "note": "Lie on your side and take up the iniquity of the house of Israel upon yourself — Ezekiel's enacted bearing of Israel's iniquity through physical suffering is the prophetic type of Christ's substitutionary bearing: Christ was offered once to bear the sins of many (Heb 9:28); the physical posture of Ezekiel — constrained, bearing the years of guilt in his own body — prefigures the cross where Christ bears the full weight of human covenant failure"},
      {"type": "allusion", "target": "Isa 53:4", "note": "Bear the iniquity of the house of Israel — the prophetic act of bearing (<em>nasa</em>) the iniquity connects directly to the Servant who bears our griefs and carries our sorrows (Isa 53:4); Ezekiel's physical bearing in his body is the OT acted prophecy that the Servant oracle interprets theologically and that Christ fulfills historically"}
    ],
    "14": [
      {"type": "allusion", "target": "Acts 10:14", "note": "I have never defiled myself — Ezekiel protests eating ceremonially impure food in terms Peter later echoes exactly: 'By no means, Lord; for I have never eaten anything that is common or unclean' (Acts 10:14); Peter's Joppa vision repeats Ezekiel's protest word for word before God's declaration that what God has made clean Peter must not call common — the transition from ceremonial purity to Christological cleanness is prepared in Ezekiel's own crisis"}
    ]
  },
  "5": {
    "5": [
      {"type": "allusion", "target": "Luke 24:47", "note": "This is Jerusalem — I placed her in the center of the nations, with countries surrounding her on all sides: the divine placement of Jerusalem as the earth's center, the hub of divine dealings with the nations, is the geographic premise of Luke 24:47 — repentance and forgiveness of sins should be proclaimed in his name to all nations, beginning from Jerusalem; the city at the center of the nations is the launch point of the universal mission"},
      {"type": "allusion", "target": "Rom 9:4-5", "note": "Jerusalem placed in the center of the nations — the uniqueness of Israel's position among the nations (center of divine dealing) is what Paul names in Rom 9:4-5: theirs are the sonship, the glory, the covenants, the law, the temple service, and the promises; Jerusalem's central placement in Ezekiel becomes Paul's grief — the privileges are real, but the rejection of Christ means Jerusalem has forfeited its central role"}
    ],
    "11": [
      {"type": "allusion", "target": "John 2:19-21", "note": "You defiled my sanctuary — therefore I will cut you down: Jesus cites this Ezekielian tradition of sanctuary defilement and judgment when he says destroy this temple and in three days I will raise it up (John 2:19); John explains he was speaking about the temple of his body — the defiled and destroyed sanctuary of ch. 5 is replaced by the indestructible sanctuary of Christ's risen body"},
      {"type": "allusion", "target": "Matt 24:2", "note": "The sanctuary cut down — Jesus's prediction that not one stone of the temple would be left on another (Matt 24:2) is the final fulfillment of the Ezekielian sequence: temple defiled → sanctuary abandoned (Ezek 10-11) → sanctuary destroyed (70 CE); the desolation Ezekiel prophesied in the exile was a type of the definitive desolation Jesus predicted"}
    ],
    "12": [
      {"type": "allusion", "target": "Rev 8:7-12", "note": "A third will die by plague and famine, a third by the sword, a third scattered to the wind — Revelation's trumpet judgments repeatedly use the thirds pattern (a third of the earth burned, a third of the sea, a third of the waters, a third of the lights darkened: Rev 8:7-12); the Ezekielian judgment-in-thirds becomes the structural template for the eschatological judgments of Revelation's trumpet sequence"}
    ]
  }
}

def main():
    e = load_echo("ezekiel")
    merge_echo(e, EZEKIEL_ECHOES)
    save_echo("ezekiel", e)
    # Report chapter coverage
    for ch in ["1", "2", "3", "4", "5"]:
        vv = e.get(ch, {})
        print(f"  ch{ch}: {len(vv)} verse(s) with echoes")

if __name__ == "__main__":
    main()
