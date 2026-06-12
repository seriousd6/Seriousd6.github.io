#!/usr/bin/env python3
"""
MKT Echo Layer — Micah chapter 7 (entirely missing)
Run: python3 scripts/zc-echo-micah-7-7-full.py

Echo type: OT → NT direction.

Key connections:
- 7:6 man's enemies are his own household → Matt 10:35-36 (Jesus quotes verbatim)
- 7:8-9 rise from darkness, YHWH my light → John 8:12; Rom 4:25 (vindication)
- 7:18-19 who is a God like you, casting sins into the sea → Heb 8:12; 1 John 1:9
- 7:20 faithfulness to Abraham → Gal 3:29; Heb 6:13-18 (the sworn covenant)
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

MICAH_ECHOES = {
    "7": {
        "6": [
            {
                "type": "quote",
                "target": "Matt 10:35-36",
                "note": "Jesus cites Micah 7:6 directly in the mission discourse: 'For I have come to set a man against his father, and a daughter against her mother, and a daughter-in-law against her mother-in-law. And a person's enemies will be those of his own household' (Matt 10:35-36). The verbal correspondence with Micah 7:6 is direct. Micah laments the social disintegration of the pre-exilic community as a sign of covenant collapse; Jesus takes the same social fracture and declares it the predictable cost of covenant loyalty in an age of division. The household divisions Micah mourns as symptom of Israel's judgment, Jesus frames as the necessary consequence of bringing the sword of decision into the world."
            },
            {
                "type": "quote",
                "target": "Luke 12:53",
                "note": "Luke 12:53 is the parallel to Matthew's citation of Micah 7:6 — 'father against son and son against father, mother against daughter and daughter against mother, mother-in-law against her daughter-in-law and daughter-in-law against mother-in-law.' Luke's formulation makes the citation bidirectional (both generations against each other), emphasizing that the covenant crisis divides households at every level. Micah's diagnosis of social breakdown becomes in Jesus's teaching the expected social topology of the kingdom's arrival: where the word of God comes with full authority, it compels decision and division."
            }
        ],
        "8": [
            {
                "type": "allusion",
                "target": "John 8:12",
                "note": "Micah 7:8 is a declaration of covenant confidence from within darkness: 'Rejoice not over me, O my enemy; when I fall, I shall rise; when I sit in darkness, YHWH will be a light to me.' The one who sits in darkness but trusts in YHWH's light is the paradigm that Jesus fulfills when he declares 'I am the light of the world. Whoever follows me will not walk in darkness, but will have the light of life' (John 8:12). Micah's confidence — that darkness is not the final word for those who wait on YHWH — becomes in Jesus the announcement that the light itself has arrived in person. The darkness Micah endures by faith, the disciples are delivered from by encounter."
            }
        ],
        "18": [
            {
                "type": "allusion",
                "target": "Heb 8:12",
                "note": "Micah 7:18-19 is one of the OT's most concentrated expressions of divine forgiveness: 'Who is a God like you, pardoning iniquity and passing over transgression for the remnant of his inheritance? He does not retain his anger forever, because he delights in steadfast love (<em>hesed</em>). He will again have compassion on us; he will tread our iniquities underfoot. You will cast all our sins into the depths of the sea.' Hebrews 8:12 quotes Jeremiah's new covenant promise — 'I will be merciful toward their iniquities, and I will remember their sins no more' — as the charter of the new covenant in Christ's blood. Both texts articulate the same theological reality: the God who delights in hesed casts sin away permanently, not merely covers it. In Christ, the casting-into-the-sea is accomplished through the cross."
            },
            {
                "type": "allusion",
                "target": "1 John 1:9",
                "note": "Micah's confidence that YHWH will cast all sins into the depths of the sea (7:19) is the OT form of John's new covenant assurance: 'If we confess our sins, he is faithful and just to forgive us our sins and to cleanse us from all unrighteousness' (1 John 1:9). The casting-into-the-sea and the cleansing-from-all-unrighteousness are the same divine act described from different vantage points. Micah speaks from within the covenant community awaiting the fullness of forgiveness; John writes after the cross has accomplished what Micah's doxology anticipated. The God who delights in hesed is the God who demonstrates his faithfulness and justice through the propitiation of the Son (1 John 2:2)."
            }
        ],
        "20": [
            {
                "type": "allusion",
                "target": "Gal 3:29",
                "note": "Micah closes with an appeal to the Abrahamic covenant: 'You will show faithfulness to Jacob and steadfast love to Abraham, as you have sworn to our fathers from the days of old.' Paul's letter to the Galatians makes this covenant the framework for understanding Christ: 'if you are Christ's, then you are Abraham's offspring, heirs according to promise' (Gal 3:29). The sworn faithfulness to Abraham that Micah invokes as the ground of his final confidence is fulfilled in Christ, who is himself the singular seed of Abraham (Gal 3:16) in whom all the promises of God find their Yes and Amen (2 Cor 1:20). The covenant oath that spans from Abraham through Micah reaches its fulfillment in the one who is both the Son of David and the Son of Abraham (Matt 1:1)."
            }
        ]
    }
}

def main():
    existing = load_echo('micah')
    merge_echo(existing, MICAH_ECHOES)
    save_echo('micah', existing)
    print('Micah 7 echoes written.')

if __name__ == '__main__':
    main()
