"""
echo | Numbers | chapters 14–15
Run: python3 scripts/zc-echo-numbers-14-15-fill.py

Ch 14: already has entries (v1, v29) — merge_echo skips existing.
Ch 15: supplemental offering laws for the land; one-law-for-all;
        unwitting sin provisions (Heb 9:7 / Rom 3:25 type);
        high-handed sin and Heb 10:26; tzitzit (fringe) and healing
        of the woman who touched the fringe of Jesus's garment (Matt 9:20).
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
  "15": {
    "15": [
      {"type": "allusion", "target": "Eph 2:14", "note": "One statute shall be both for you and for the stranger who sojourns with you — the supplemental offering laws for when Israel enters the land apply equally to native Israelite and resident Gentile: one law, one community, one access. Paul's proclamation in Eph 2:14-16 that Christ 'has broken down in his flesh the dividing wall of hostility' and created 'one new man in place of two' is the fulfillment of this one-law principle; what the Mosaic legislation stated as a legal principle in Numbers 15 is enacted ontologically in the cross."}
    ],
    "22": [
      {"type": "allusion", "target": "Heb 9:7", "note": "If you sin unintentionally and do not observe all these commandments that YHWH has spoken to Moses — the communal unwitting-sin provision (vv.22-26) requires a bull burnt offering and goat sin offering for unintentional community violations. Hebrews 9:7 cites this structure: 'into the second tent only the high priest goes, and only once a year, and not without blood, which he offers for himself and for the unintentional sins of the people.' The communal unwitting-sin sacrifice of Num 15 is the type of Yom Kippur's scope, which is itself the type of Christ's once-for-all atonement covering what was done 'in ignorance' (Acts 3:17; 1 Tim 1:13)."}
    ],
    "30": [
      {"type": "allusion", "target": "Heb 10:26", "note": "But the person who does anything with a high hand (<em>beyad ramah</em>), whether he is native or sojourner, reviles YHWH, and that person shall be cut off from among his people — high-handed sin (<em>beyad ramah</em>, literally with a raised/defiant hand) has no sacrificial remedy in the Levitical system; it results in karet. Hebrews 10:26 applies this principle to apostasy: 'For if we go on sinning deliberately after receiving the knowledge of the truth, there no longer remains a sacrifice for sins, but a fearful expectation of judgment.' The high-handed/presumptuous sin category of Num 15:30-31 is the background for the severe apostasy warning of Hebrews."}
    ],
    "38": [
      {"type": "fulfillment", "target": "Matt 9:20", "note": "Speak to the people of Israel and tell them to make tassels (<em>tzitzit</em>) on the corners of their garments — the tzitzit are the visible sign of covenant identity, worn to remember YHWH's commandments. The woman with a twelve-year hemorrhage 'came up behind him and touched the fringe (<em>kraspedon</em>) of his garment' (Matt 9:20; cf. 14:36). The same Greek word (<em>kraspedon</em>) translates the Hebrew <em>tzitzit</em> (fringe/tassel) in the LXX. The woman reaches for the tassel of the Torah-keeper par excellence — the one who is himself the embodiment of the commandments — and is healed by the touch. The tzitzit whose function was to remind Israel of the commandments becomes, in Christ, the healing fringe of the one who fulfilled them all."},
      {"type": "allusion", "target": "Num 15:40", "note": "The blue cord (<em>ptil tekhelet</em>) in the tzitzit was meant to prompt remembrance of the commandments and thus holiness. The number of threads, knots, and their numerical value (613, according to later tradition) encoded the entire Torah in the fringe. That the healing woman touches the specific corner-tassel suggests that in Jesus, the entire Torah-embodiment is present in a single touch — 'the one who fulfills all righteousness' (Matt 3:15) heals through the very emblem of covenant obligation that he perfectly keeps."}
    ],
    "41": [
      {"type": "allusion", "target": "Rev 1:8", "note": "I am YHWH your God who brought you out of the land of Egypt to be your God — the tzitzit commandment closes with the foundational exodus-identity formula: the same God who redeemed from Egypt is the one whose commandments the fringes recall. The Revelation's opening vision identifies the risen Christ with precisely this formula: 'I am the Alpha and the Omega, says the Lord God, who is and who was and who is to come, the Almighty' (Rev 1:8) — the eternal I AM who brought Israel out of Egypt is the crucified and risen Lord Jesus whose identity encompasses the entire sweep of the covenant name."}
    ]
  }
}

def main():
    e = load_echo('numbers')
    merge_echo(e, ECHO)
    save_echo('numbers', e)
    print('Numbers 14-15 echo written.')

if __name__ == '__main__':
    main()
