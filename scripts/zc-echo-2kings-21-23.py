"""
MKT Echo Data — 2 Kings chapters 21–23
Run: python3 scripts/zc-echo-2kings-21-23.py

Ch21: Manasseh's evil — filling Jerusalem with innocent blood; the sin that made exile
      inevitable (24:3-4); the sin beyond forgiveness (Jer 15:4)
Ch22: Josiah's finding of the Book of the Law — Hilkiah and the scroll
Ch23: Josiah's comprehensive reform — temple cleansing, high places removed, Passover
      celebrated; Josiah as the greatest reformer-king (23:25: no king before or after)
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

ECHO = {
  "22": {
    "8": [
      {"type": "allusion", "target": "Luke 4:17", "note": "Hilkiah the priest finds the Book of the Law in the temple during repairs — the scroll that had been lost or neglected, when read aloud to the king, produces immediate repentance and reform; Luke 4:17 depicts Jesus given the scroll of Isaiah in the synagogue, unrolling it, reading, rolling it up and sitting down: 'Today this Scripture is fulfilled in your hearing.' In both scenes, the reading of a sacred text in a covenant gathering triggers a decisive moment; in Josiah's case, hearing the law produces repentance; in Jesus's case, hearing the fulfillment produces rejection."}
    ]
  },
  "23": {
    "3": [
      {"type": "allusion", "target": "Heb 8:6", "note": "Josiah stands by the pillar and makes a covenant to walk after YHWH with all his heart and soul — the great covenant renewal in the temple; Heb 8:6 contrasts the old covenant mediator (Moses at Sinai) with Jesus: 'he is the mediator of a better covenant, which is enacted on better promises.' Josiah's covenant renewal is the OT's most complete human attempt to restore the Sinai covenant in the period before the exile — it is comprehensive (23:25: no king before or after turned to YHWH as he did) and still insufficient: 'Nevertheless, YHWH did not turn from the burning of his great wrath' (23:26). The reform that surpassed all previous reforms still could not avert the exile, demonstrating the need for the 'better covenant' enacted by the superior mediator."},
      {"type": "allusion", "target": "Matt 22:37", "note": "Josiah's reform is measured by the standard that Jesus names as the first commandment: 'You shall love the Lord your God with all your heart and with all your soul and with all your mind.' The 2 Kgs 23:25 summary of Josiah — 'before him there was no king who turned to YHWH with all his heart and with all his soul and with all his might' — directly echoes the Shema (Deut 6:5); Josiah's total-covenant-commitment is the OT's high-water mark of Shema-obedience. Jesus is the one who perfectly fulfills this commandment, not merely as a reform but as his constitutive identity."}
    ],
    "25": [
      {"type": "allusion", "target": "Heb 7:11", "note": "The narrator's verdict on Josiah — 'before him there was no king like him who turned to YHWH with all his heart and all his soul and all his might, according to all the Law of Moses, nor did any like him arise after him' — is the absolute ceiling of the royal covenant-obedience scale; yet vv26-27 immediately follow: even this superlative obedience could not avert the exile. Heb 7:11 draws the conclusion the exile already implies: 'if perfection had been attainable through the Levitical priesthood (under which the people received the law), what further need would there have been for another priest?' Josiah proves that even the most complete covenant-obedience under the old order was insufficient; the exile demonstrates that human covenant-keeping cannot generate the righteousness the covenant requires."}
    ]
  }
}

def main():
    e = load_echo('2kings')
    merge_echo(e, ECHO)
    save_echo('2kings', e)
    count = sum(len(v) for v in ECHO.values())
    print(f'2kings echo: wrote {count} verses across ch 21-23')

if __name__ == '__main__':
    main()
