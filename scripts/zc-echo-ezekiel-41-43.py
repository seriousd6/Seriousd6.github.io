"""
echo layer: Ezekiel 41-43
Key echo clusters:
  - ch41 sanctuary measurements → Heb 9:1-5 (earthly sanctuary as copy of heavenly)
  - ch41 wooden altar/table before YHWH → Heb 13:10; Rev 8:3-5
  - ch42 holy chambers / priestly garments → Rev 1:6; 5:10; 1 Pet 2:9
  - ch42 wall separating holy from common → Eph 2:14 (dividing wall broken in Christ)
  - ch43 glory returning from east → Rev 21:11, 23; John 1:14
  - ch43 dwelling of God with man forever → Rev 21:3
  - ch43 new altar / blood consecration → Heb 9:13-14; 10:1-4
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
  "41": {
    "1": [
      {"type": "shadow", "target": "Heb 9:1-5", "note": "He brought me to the nave and measured the jambs — Ezekiel's guided tour through the temple zones (outer court, inner court, nave, Most Holy Place) is the structure Hebrews 9:1-5 uses to argue that the earthly sanctuary was a copy and shadow of the heavenly (Heb 8:5); the precise measurements Ezekiel records establish the architectural seriousness of the earthly temple whose purpose is to mirror heavenly realities now permanently accessible through Christ."},
      {"type": "allusion", "target": "Rev 21:15-17", "note": "The measuring of the temple with a measuring rod — the angelic guide's precise measurements anticipate the angel measuring the New Jerusalem with a measuring rod in Revelation 21:15-17; the act of divine measurement establishes the permanence and reality of the sacred space, and in both visions it signals that the dwelling of God with his people is a precisely architected divine intention."}
    ],
    "4": [
      {"type": "shadow", "target": "Heb 9:3-5", "note": "He measured the innermost room, twenty cubits square — this is the Most Holy Place, location of the divine presence above the mercy seat; Hebrews 9:3-5 cites the Most Holy Place as the type of the heavenly sanctuary into which Christ has entered with his own blood (Heb 9:12), not to perform the annual Yom Kippur ritual but to secure eternal redemption; the inner sanctuary Ezekiel measures is the earthly shadow of where the risen Christ now intercedes."}
    ],
    "22": [
      {"type": "type", "target": "Heb 13:10", "note": "The altar of wood, three cubits high — this wooden altar is designated the table before YHWH; Hebrews 13:10 declares: we have an altar from which those who serve the tent have no right to eat; the altar of the Christian community is Christ himself, both priest and sacrifice, from whom the redeemed feed; the wooden altar in Ezekiel's vision anticipates the cross as the altar on which the true sacrifice was offered."},
      {"type": "allusion", "target": "Rev 8:3-5", "note": "The table before YHWH — the wooden altar in the visionary sanctuary echoes forward to the golden altar before the throne in Revelation 8:3-5, from which the prayers of the saints ascend as incense and from which fire is thrown on the earth; Ezekiel's table before YHWH is transformed in Revelation into the eschatological altar from which both intercession and judgment proceed."}
    ]
  },
  "42": {
    "13": [
      {"type": "shadow", "target": "1 Pet 2:9", "note": "The holy chambers where the priests shall eat the most holy offerings — the priestly privilege of eating holy food in the sanctuary is a type of the NT declaration that all believers constitute a royal priesthood (1 Pet 2:9; Rev 1:6; 5:10); where Ezekiel's vision restricts the eating to consecrated Aaronic priests, the new covenant opens the privileges of the Most Holy Place to all who are in Christ the great High Priest."},
      {"type": "allusion", "target": "Rev 5:10", "note": "The priests shall eat the most holy offerings there — the restricted priestly eating in the earthly temple finds its eschatological reversal: you have made them a kingdom and priests to our God, and they shall reign on the earth (Rev 5:10); the few Aaronic priests who could eat in the holy chambers become all the redeemed who feast at the eschatological table, because Christ has made his people priests by his blood (Rev 1:5-6)."}
    ],
    "20": [
      {"type": "type", "target": "Eph 2:14", "note": "It had a wall all around to make a separation between the holy and the common — the wall enforcing the holy/common boundary is the OT type of the dividing wall of hostility that Christ has broken down; Paul declares in Ephesians 2:14: he himself is our peace, who has made us both one and has broken down in his flesh the dividing wall of hostility, abolishing the law of commandments expressed in ordinances; the architectural barrier Ezekiel measures is dismantled by the cross."}
    ]
  },
  "43": {
    "2": [
      {"type": "type", "target": "John 1:14", "note": "The glory of the God of Israel was coming from the east, and the sound was like the sound of many waters — the return of YHWH's glory to the temple after its departure in Ezekiel 10-11 is the OT pattern that John 1:14 fulfills: the Word became flesh and dwelt (eskēnōsen, tabernacled) among us, and we have seen his glory; the Shekinah glory that departed from Jerusalem at the exile returns permanently not to a building but to a body — the incarnate Son is the new temple in whom the divine glory dwells."},
      {"type": "allusion", "target": "Rev 21:11", "note": "The earth shone with his glory — the return of YHWH's glory to the visionary temple is the type of the divine glory that fills the New Jerusalem in Revelation 21:11: having the glory of God, its radiance like a most rare jewel, like a jasper, clear as crystal; the same divine glory Ezekiel sees entering the temple will permanently illuminate the eschatological city where God dwells with his people."}
    ],
    "4": [
      {"type": "fulfillment", "target": "John 2:19-21", "note": "The glory of YHWH entered the temple by the gate facing east — the dramatic re-entry of the divine glory is the event Jesus declares fulfilled in himself: Destroy this temple, and in three days I will raise it up (John 2:19); John explains: he was speaking about the temple of his body (John 2:21); the return of divine glory to the earthly temple that Ezekiel foresees is accomplished not in the rebuilt Second Temple but in the resurrection body of the Son of God."}
    ],
    "7": [
      {"type": "fulfillment", "target": "Rev 21:3", "note": "This is the place of my throne where I will dwell in the midst of the children of Israel forever — YHWH's declaration of permanent dwelling among his people is cited as fulfilled in Revelation 21:3: Behold, the dwelling place of God is with man. He will dwell with them, and they will be his people, and God himself will be with them as their God; the forever-dwelling Ezekiel announces is realized in the New Jerusalem where no temple building is needed (Rev 21:22) because the Lord God Almighty and the Lamb are its temple."},
      {"type": "allusion", "target": "Rev 22:4", "note": "My holy name shall no more be defiled — the permanent indwelling with the name unspoiled anticipates the New Jerusalem's final blessing: they will see his face, and his name will be on their foreheads (Rev 22:4); what the old temple could only approximate is accomplished permanently in the city where Christ and his people share the same name and unobstructed presence."}
    ],
    "18": [
      {"type": "shadow", "target": "Heb 9:13-14", "note": "These are the ordinances of the altar: offer a bull as a sin offering — the elaborate seven-day blood ritual for consecrating the new altar is the Levitical system at its most detailed; Hebrews 9:13-14 uses this logic to demonstrate Christ's superiority: if the blood of goats and bulls sanctify for the purification of the flesh, how much more will the blood of Christ purify our conscience from dead works to serve the living God; the altar consecration Ezekiel describes establishes what the blood of Christ finally accomplishes."}
    ],
    "27": [
      {"type": "fulfillment", "target": "Heb 10:10-14", "note": "From the eighth day onward the priests shall offer and I will accept you — the altar consecration climaxes on the eighth day (associated with new creation and resurrection) when sacrificial worship resumes and YHWH declares acceptance; Hebrews 10:10-14 fulfills this: we have been sanctified through the offering of the body of Jesus Christ once for all; by a single offering he has perfected for all time those who are being sanctified; the conditional YHWH-acceptance Ezekiel describes becomes the permanent acceptance secured in Christ's once-for-all sacrifice."}
    ]
  }
}

def main():
    existing = load_echo("ezekiel")
    merge_echo(existing, EZEKIEL_ECHOES)
    save_echo("ezekiel", existing)
    print("Ezekiel 41-43 echoes written.")

if __name__ == "__main__":
    main()
