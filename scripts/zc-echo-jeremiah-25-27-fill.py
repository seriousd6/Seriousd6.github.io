"""
MKT Echo Layer — Jeremiah chapters 25–27
Run: python3 scripts/zc-echo-jeremiah-25-27-fill.py

Key echo decisions:
- 25:11-12 seventy years → Dan 9:2 (Daniel reads Jeremiah and prays); the
  foundational apocalyptic time-cycle that underlies Daniel's vision and NT eschatology
- 25:15-16 cup of wrath → Matt 26:39 (Gethsemane) is the primary NT echo: the cup
  Jesus asks to be removed is precisely the cup of divine wrath Jeremiah describes
- 26:8-15 'this man deserves to die' → Jesus's trial (Mark 14:58,64): the Sanhedrin
  charges against Jesus for predicting temple destruction repeat the exact pattern of
  the priests' charge against Jeremiah; a direct structural parallel
- 27:2 the yoke → Matt 11:29-30: Jesus's invitation to take his easy yoke deliberately
  contrasts with the heavy yoke of Babylonian subjection Jeremiah announces
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
    """Merge echo entries; deduplicate by (type, target) within each verse."""
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

JER_ECHOES = {
  "25": {
    "11": [
      {
        "type": "fulfillment",
        "target": "Dan 9:2",
        "note": "Daniel 9:2 explicitly states that Daniel read Jeremiah's seventy-year prophecy and prayed in response, triggering the angel Gabriel's revelation of the seventy-weeks schema (Dan 9:24-27). The Jeremian seventy years thus launches the entire Danielic eschatological framework that the NT, Revelation, and Jesus's Olivet Discourse build upon."
      }
    ],
    "15": [
      {
        "type": "allusion",
        "target": "Matt 26:39",
        "note": "The cup of the wine of wrath that YHWH commands Jeremiah to give all nations to drink is the background for Jesus's Gethsemane prayer: 'if it is possible, let this cup pass from me.' Jesus is asking to be spared the very cup of divine wrath that Jer 25 describes — the cup he ultimately drinks on behalf of those who deserved it, absorbing the judgment the nations and Israel were under."
      },
      {
        "type": "allusion",
        "target": "Rev 14:10",
        "note": "Revelation's cup of God's fury — poured full strength into the cup of his wrath (Rev 14:10; 16:19) — is drawn directly from Jer 25:15-28's vision of the wrath-cup passed to the nations. John's apocalyptic imagery recasts the Jeremian historical judgment as an eschatological reality enacted at the end of the age."
      }
    ],
    "29": [
      {
        "type": "allusion",
        "target": "1 Pet 4:17",
        "note": "Jeremiah's logic — judgment begins with Jerusalem, the city bearing YHWH's name, before spreading to the nations — is exactly Peter's argument in 1 Pet 4:17: 'it is time for judgment to begin with God's household; and if it begins with us, what will the outcome be for those who do not obey the gospel?' Both texts ground universal judgment in the prior judgment of God's own people."
      }
    ],
    "30": [
      {
        "type": "allusion",
        "target": "John 5:25",
        "note": "YHWH's roaring voice from on high (Jer 25:30; cf. Amos 1:2; Joel 3:16) anticipates Jesus's claim in John 5:25: 'a time is coming and has now come when the dead will hear the voice of the Son of God, and those who hear will live.' The divine roaring that in Jeremiah signals eschatological judgment becomes, in Jesus, the life-giving summons of resurrection."
      }
    ]
  },
  "26": {
    "8": [
      {
        "type": "type",
        "target": "Mark 14:64",
        "note": "The priests and prophets' verdict 'this man deserves to die' for predicting the temple's destruction (Jer 26:8-11) is the precise structural type of the Sanhedrin's verdict against Jesus: 'they all condemned him as worthy of death' (Mark 14:64), following the accusation that he said 'I will destroy this temple' (Mark 14:58). Jeremiah is the most direct prophetic type of Jesus's trial among all OT figures."
      }
    ],
    "15": [
      {
        "type": "allusion",
        "target": "Matt 23:35",
        "note": "Jeremiah's warning 'if you put me to death, you will bring the guilt of innocent blood upon yourselves' (Jer 26:15) is the foundation for Jesus's blood-guilt pronouncement in Matt 23:35-36: 'on you will come all the righteous blood shed on earth.' Both texts announce that unjust execution of YHWH's messenger makes the executors liable for covenant blood-guilt."
      }
    ]
  },
  "27": {
    "2": [
      {
        "type": "allusion",
        "target": "Matt 11:29",
        "note": "The wooden yoke with crossbars and straps that Jeremiah wears to symbolize Babylonian subjugation is the same yoke-image Jesus inverts in Matt 11:29-30: 'take my yoke upon you and learn from me ... my yoke is easy and my burden is light.' The contrast between Babylon's crushing yoke of judgment and Christ's gentle yoke of covenant is deliberate: Jesus offers what the prophets could only promise would come after the exile's end."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Rev 22:15",
        "note": "The catalog of false spiritual authorities — prophets, diviners, dreamers, fortune-tellers, sorcerers — who give false peace assurances (Jer 27:9-10) are excluded from the covenant community, as Revelation's exclusion lists confirm: 'outside are the sorcerers ... and everyone who loves and practices falsehood' (Rev 22:15). The covenant community's boundary against false spiritual mediation runs from Jeremiah through Revelation."
      }
    ],
    "22": [
      {
        "type": "theme",
        "target": "Rev 11:2",
        "note": "YHWH's promise that the temple vessels taken to Babylon will be retrieved 'until the day when I attend to them' grounds the prophetic expectation of temple restoration that undergirds Revelation's new-temple imagery. The 42-month trampling of the holy city (Rev 11:2) and the eventual new Jerusalem (Rev 21:2) are the eschatological fulfillment of the same divine attendance-to-them that Jeremiah promises."
      }
    ]
  }
}

def main():
    existing = load_echo('jeremiah')
    merge_echo(existing, JER_ECHOES)
    save_echo('jeremiah', existing)

    out = json.loads((ROOT / 'data/echoes/jeremiah.json').read_text())
    for ch in range(25, 28):
        ck = str(ch)
        entries = out.get(ck, {})
        status = 'done' if entries else 'MISSING'
        count = sum(len(v) for v in entries.values())
        print(f'  ch {ch}: {status} ({count} echo entries across {len(entries)} verses)')

if __name__ == '__main__':
    main()
