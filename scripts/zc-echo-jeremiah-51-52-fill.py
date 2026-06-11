"""
Echo fill — Jeremiah chapters 51–52
Run: python3 scripts/zc-echo-jeremiah-51-52-fill.py

Ch 51 already has 2 entries (51:7, 51:45) from Phase 2 combined script.
Only ch 52 needs to be written; merge_echo will skip existing entries.

Ch 52 = fall of Jerusalem / Jehoiachin released from prison.
Key theological connections:
- 52:3 (expelled from presence) = Luke 21:20-24; 2 Thess 2:8
- 52:13 (temple burned) = John 2:19-21 (Christ as the new temple); Matt 24:2
- 52:17-20 (sacred furnishings plundered) = Heb 9:1-5 (shadows superseded)
- 52:31-34 (Jehoiachin's honored seat) = Matt 1:11-12 (Davidic line preserved); the
  Davidic-seed-through-exile preserved for the genealogy of Christ
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

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

JER_ECHO_52 = {
  "52": {
    "3": [
      {"type": "allusion", "target": "Luke 21:20-24", "note": "Because of the LORD&apos;s anger that all this happened to Jerusalem and Judah, until he finally expelled them from his presence — the theological summary of the exile: covenantal expulsion from YHWH&apos;s presence; Jesus anticipates the 70 CE recurrence of this expulsion: when you see Jerusalem surrounded by armies, know that its desolation has come... Jerusalem will be trampled underfoot by the Gentiles until the times of the Gentiles are fulfilled (Luke 21:20-24); both destructions are YHWH&apos;s expulsion-judgment on covenant-breaking Jerusalem"}
    ],
    "13": [
      {"type": "allusion", "target": "Matt 24:2", "note": "He set fire to the house of the LORD — the first destruction of the Jerusalem temple (586 BCE); Jesus predicts the second: truly I tell you, not one stone here will be left on another, every one will be thrown down (Matt 24:2); the temple destruction of Jer 52:13 sets the pattern that Jesus applies to the second temple; both destructions are divine judgment on covenant failure"},
      {"type": "fulfillment", "target": "John 2:19-21", "note": "The house of the LORD burned to the ground — the end of the temple as YHWH&apos;s dwelling; Jesus&apos;s response to the temple establishment (destroy this temple and I will raise it in three days, John 2:19-21) declares that he himself is the new temple; the building that Nebuchadrezzar burned becomes the shadow whose substance is Christ&apos;s body"}
    ],
    "17": [
      {"type": "allusion", "target": "Heb 9:1-5", "note": "The Chaldeans smashed the bronze pillars, movable stands, and bronze sea — the destruction of the sacred temple furniture; Hebrews lists these same furnishings (lampstand, table, ark, cherubim — Heb 9:1-5) as the earthly copies of heavenly realities that the Mosaic covenant provided; their destruction by Babylon is the negative demonstration of what Hebrews argues theologically: these were shadows that Christ the true high priest has now superseded with his own body and blood"}
    ],
    "27": [
      {"type": "allusion", "target": "Acts 7:42-43", "note": "So Judah was carried into exile from its own land — the climactic statement of the exile; Stephen&apos;s speech to the Sanhedrin traces the same trajectory: God turned away and gave them up to worship the host of heaven (Acts 7:42, citing Amos 5:25-27); the exile of Jer 52:27 is what Stephen uses to indict Israel&apos;s history of rejecting the Spirit-sent messengers, culminating in their rejection of Jesus"}
    ],
    "31": [
      {"type": "allusion", "target": "Matt 1:11-12", "note": "Evil-merodach king of Babylon released Jehoiachin king of Judah from prison in the thirty-seventh year of his exile — the Davidic king preserved through exile, still alive, given a seat of honor; Matthew&apos;s genealogy includes Jehoiachin (Jechoniah) at precisely this point (Matt 1:11-12): after the deportation to Babylon, Jechoniah was the father of Shealtiel; Jer 52&apos;s ending of the preserved-Davidic-king-in-exile is the genealogical link that makes the Davidic descent of Jesus possible"},
      {"type": "allusion", "target": "Eph 2:6", "note": "Gave him a seat of honor above the other captive kings in Babylon — the exiled Davidic king elevated to a seat of honor; Paul applies a similar language of elevation to Christ and to those in him: God raised us up with Christ and seated us with him in the heavenly realms (Eph 2:6); the exiled-king-raised-to-honor pattern of Jer 52:31-34 is the type of the resurrection-and-exaltation of Christ and his people"}
    ],
    "34": [
      {"type": "allusion", "target": "Phil 4:19", "note": "A regular daily portion was granted him by the king of Babylon, every day until his death — YHWH&apos;s provision for the preserved Davidic line even in exile, through a foreign king; Paul&apos;s confidence that God will supply every need according to his riches in glory in Christ Jesus (Phil 4:19) rests on the same pattern: YHWH provides for his covenant people even in exile, even through unexpected instruments; the daily portion for the exiled king is the type of the Father&apos;s daily provision for his people"}
    ]
  }
}

def main():
    existing = load_echo('jeremiah')
    merge_echo(existing, JER_ECHO_52)
    save_echo('jeremiah', existing)
    print('Jeremiah 52 echoes written.')

if __name__ == '__main__':
    main()
