"""
MKT Echo — Deuteronomy chapters 18–21
Run: python3 scripts/zc-echo-deuteronomy-18-21.py

Source data used:
- data/interlinear/deuteronomy.json
- data/translation/draft/mediating/deuteronomy.json
- data/parallels/deuteronomy.json (absorbed: ch 18 v15 already present; ch 19 v15 already present; ch 21 v23 already present)

Key decisions in this range:
- Ch 18 v15 has three fulfillment entries already; v18-19 add the complementary "words in his mouth" side of the prophet-like-Moses promise
- Ch 19 cities of refuge (v4): classified as shadow — Heb 6:18 uses "refuge" language but does not quote Deut 19 directly
- Ch 20 warfare laws: no explicit NT citation; theme connections only
- Ch 21 heifer rite (v4, v8): shadow/allusion — the verbal parallel to Matt 27:24 is strong enough for allusion
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

DEUTERONOMY_ECHOES = {
  "18": {
    "18": [
      {"type": "fulfillment", "target": "John 12:49", "note": "I will put my words in his mouth and he shall speak to them all that I command him — Jesus explicitly fulfills this: 'I have not spoken on my own authority, but the Father who sent me has himself given me a commandment — what to say and what to speak'; the prophet-like-Moses receives and transmits the divine word without independent addition."},
      {"type": "fulfillment", "target": "John 7:16", "note": "My teaching is not mine but his who sent me — the criterion of the true prophet (speaking only what YHWH commands) is what Jesus claims for his own teaching; his words are the Father's words, meeting the Deuteronomic test of the genuine prophet."}
    ],
    "19": [
      {"type": "fulfillment", "target": "Acts 3:23", "note": "And it shall be that every soul who does not listen to that prophet shall be destroyed from the people — Peter cites this judgment-clause immediately after quoting Deut 18:15-16 (Acts 3:22-23), making the stakes of rejecting Jesus explicit: this is not merely a social failure but the covenant cut-off that Moses warned of."}
    ]
  },
  "19": {
    "4": [
      {"type": "shadow", "target": "Heb 6:18", "note": "The city of refuge for the manslayer who killed without intent — the institution shadows Christ as refuge: the one who flees to the city is safe from the avenger of blood as long as he stays. Hebrews uses the same 'fled for refuge' language for believers clinging to the hope set before them (Heb 6:18), drawing on this Mosaic institution as the conceptual background for salvation-security in Christ."}
    ],
    "16": [
      {"type": "allusion", "target": "Matt 26:59-61", "note": "If a malicious witness rises against a man to accuse him of wrongdoing — the trial of Jesus directly violates this law: the chief priests sought false testimony against him to put him to death, and false witnesses came forward with contradictory charges (Matt 26:59-61). The law designed to protect the innocent from false accusation is weaponized against the innocent one; the very statute whose violation it describes is what condemns him."}
    ]
  },
  "20": {
    "3": [
      {"type": "theme", "target": "Heb 13:6", "note": "Do not be faint-hearted or afraid; do not be in dread or terror of them — the priest's pre-battle address grounds Israel's fearlessness in YHWH's presence. The NT takes up this covenant-presence logic: Heb 13:5-6 quotes Deut 31:6 and draws the same conclusion — 'the Lord is my helper; I will not fear.' The Deuteronomic assurance of the divine warrior going before Israel is reapplied to the Christian's daily battle."}
    ],
    "4": [
      {"type": "theme", "target": "Rom 8:31", "note": "For the LORD your God is he who goes with you to fight for you against your enemies — the logic of the divine warrior who fights on Israel's behalf is the OT background for Paul's rhetorical climax: 'If God is for us, who can be against us?' The covenant pledge to fight for Israel becomes the Spirit-age guarantee that no spiritual power can separate believers from the love of Christ."}
    ],
    "10": [
      {"type": "theme", "target": "Luke 19:42", "note": "When you draw near to a city to fight against it, first offer it terms of peace — the law requiring a peace-offer before siege-warfare lies behind Jesus's lament over Jerusalem: 'Would that you, even you, had known on this day the things that make for peace!' The divine Warrior has come offering peace; Jerusalem's rejection makes the coming judgment a siege she chose rather than one imposed without warning."}
    ]
  },
  "21": {
    "4": [
      {"type": "allusion", "target": "Matt 27:24", "note": "The elders shall wash their hands over the heifer and declare: our hands did not shed this blood — Pilate's handwashing ('I am innocent of this man's blood') directly echoes this Deuteronomic ritual for declaring corporate innocence over unavenged innocent blood. The irony is total: Pilate performs the absolution-rite over the one whose death is the very atonement the heifer-ritual could only shadow."}
    ],
    "8": [
      {"type": "shadow", "target": "Heb 9:13-14", "note": "Accept atonement for your people Israel and do not place the guilt of innocent blood in the midst of your people — the heifer ritual addresses blood-guilt that cannot be traced to a human killer, requiring a corporate act of atonement. Hebrews draws the contrast: if the blood of bulls can cleanse outward defilement, how much more will the blood of Christ purify the conscience from dead works. The heifer-atonement is the shadow; Christ's blood is the substance."}
    ]
  }
}

def main():
    existing = load_echo('deuteronomy')
    merge_echo(existing, DEUTERONOMY_ECHOES)
    save_echo('deuteronomy', existing)
    print('Deuteronomy 18-21 echoes written.')

if __name__ == '__main__':
    main()
