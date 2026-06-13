#!/usr/bin/env python3
"""
MKT Echo Layer — 2 Kings chapters 10, 15, 21 (fill: missed by prior scripts)
Run: python3 scripts/zc-echo-2kings-fill-10-15-21.py

Echo type: OT → NT direction.

Key connections:
- 10:10 reliability of God's word → Matt 5:18; Luke 21:33
- 15:29 Galilee/Naphtali taken by Assyria → Matt 4:15-16 (fulfills Isa 9:1-2)
- 21:16 Manasseh's innocent blood → Matt 23:35; Luke 11:50-51
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

TWO_KINGS_ECHOES = {
    "10": {
        "10": [
            {
                "type": "allusion",
                "target": "Luke 21:33",
                "note": "2 Kings 10:10 — &#x201C;Know then that there shall fall to the earth nothing of the word of the LORD which the LORD spoke concerning the house of Ahab&#x201D; — asserts the absolute reliability of divine speech. Every judgment Elijah announced against Ahab&#x2019;s house has been fulfilled to the letter; not one word missed its mark. Jesus&#x2019;s promise in Luke 21:33 — &#x201C;Heaven and earth will pass away, but my words will not pass away&#x201D; — stands in the same tradition of asserting the indestructibility of God&#x2019;s word. What Jehu&#x2019;s purge demonstrated about the prophetic word against Ahab, the resurrection and parousia will demonstrate about Christ&#x2019;s words of judgment and promise: none will fall to the ground."
            },
            {
                "type": "allusion",
                "target": "Matt 5:18",
                "note": "The affirmation in 2 Kings 10:10 that &#x201C;not a word of the LORD will fall to the ground&#x201D; is the OT pattern for Jesus&#x2019;s words in Matthew 5:18: &#x201C;For truly, I say to you, until heaven and earth pass away, not an iota, not a dot, will pass from the Law until all is accomplished.&#x201D; Both texts assert the exhaustive reliability of divine speech — in 2 Kings 10 as a backward look at prophetic fulfillment in history, in Matthew 5 as a forward look at the Law&#x2019;s completion in Jesus. The same God whose words about Ahab&#x2019;s house did not fail is the one whose law finds its telos in Christ."
            }
        ],
        "28": [
            {
                "type": "allusion",
                "target": "Rom 11:4",
                "note": "2 Kings 10:28 records that &#x201C;Jehu wiped out Baal from Israel.&#x201D; This purge fulfills the promise given to Elijah at Horeb (1 Kings 19:14-18), where God disclosed that seven thousand in Israel had not bowed to Baal. Jehu&#x2019;s action is the divine instrument by which that remnant-promise advances. Paul in Romans 11:4 cites the &#x201C;seven thousand who have not bowed the knee to Baal&#x201D; (1 Kings 19:18) as the OT paradigm for the believing Jewish remnant within Israel in his own day. The pattern 2 Kings 10:28 embodies — God preserving a faithful remnant through judgment — is the same pattern Paul sees at work in the partial hardening of Israel and the preservation of Jewish believers in the age of the gospel."
            }
        ]
    },
    "15": {
        "29": [
            {
                "type": "allusion",
                "target": "Matt 4:15-16",
                "note": "2 Kings 15:29 records the Assyrian campaign of Tiglath-Pileser III: &#x201C;He captured...Hazor, Gilead, and Galilee, all the land of Naphtali, and he carried the people captive to Assyria.&#x201D; This dispossession of Galilee and Naphtali is the historical event that Isaiah 9:1-2 addresses: &#x201C;But there will be no gloom for her who was in anguish. In the former time he brought into contempt the land of Zebulun and the land of Naphtali, but in the latter time he has made glorious the way of the sea, the land beyond the Jordan, Galilee of the nations. The people who walked in darkness have seen a great light.&#x201D; Matthew 4:15-16 quotes Isaiah 9:1-2 directly to frame the beginning of Jesus&#x2019;s Galilean ministry: the very territory reduced to darkness by Tiglath-Pileser&#x2019;s conquest becomes the region of the dawning light of Christ. The historical note in 2 Kings 15:29 supplies the wound that Isaiah promises healing for and that Matthew declares healed."
            }
        ],
        "5": [
            {
                "type": "allusion",
                "target": "Luke 17:12-14",
                "note": "2 Kings 15:5 records that the LORD struck King Azariah (Uzziah) with leprosy, so that &#x201C;he was a leprous man to the day of his death, and dwelt in a separate house.&#x201D; The isolation of a leprous king — cut off from the temple, from royal duties, from community — is the condition that Jesus&#x2019;s healing of ten lepers in Luke 17:12-14 reverses. The lepers who &#x201C;stood at a distance&#x201D; and cried for mercy enact the same mandatory separation that Uzziah endured. Jesus&#x2019;s instruction to &#x201C;show yourselves to the priests&#x201D; inverts the trajectory: where Uzziah was exiled from priestly access by his leprosy, the healed lepers are sent back into the priestly system as testimony to cleansing. The king who could not be healed stands behind the diseased subjects whom the King heals."
            }
        ]
    },
    "21": {
        "16": [
            {
                "type": "allusion",
                "target": "Matt 23:35",
                "note": "2 Kings 21:16 records that &#x201C;Manasseh shed very much innocent blood, till he had filled Jerusalem from end to end.&#x201D; This is one of the starkest indictments in the Hebrew Bible — a king whose violence saturated the city. Jesus in Matthew 23:35 pronounces judgment on Jerusalem for &#x201C;all the righteous blood shed on earth, from the blood of righteous Abel to the blood of Zechariah.&#x201D; Manasseh&#x2019;s reign stands as one of the defining chapters in this history of innocent blood — Jewish tradition identifies him as responsible for the death of Isaiah (cf. Lives of the Prophets). The accumulation of innocent blood that Jesus names as the basis for the judgment of 70 AD is precisely the accumulation that 2 Kings 21:16 exemplifies. Manasseh&#x2019;s blood-guilt is part of what fills the measure that Jesus declares full."
            },
            {
                "type": "allusion",
                "target": "Luke 11:50-51",
                "note": "Luke 11:50-51 parallels Matthew 23:35: &#x201C;so that the blood of all the prophets, shed from the foundation of the world, may be charged against this generation, from the blood of Abel to the blood of Zechariah.&#x201D; The Deuteronomic tradition that culminates in 2 Kings 21:16 — kings who shed the blood of prophets and the innocent — is the OT base on which Jesus&#x2019;s indictment rests. Manasseh&#x2019;s filling Jerusalem with blood is the historical specification of the pattern Luke&#x2019;s Jesus identifies as reaching its eschatological moment of accountability in the generation that rejected the Son."
            }
        ],
        "6": [
            {
                "type": "allusion",
                "target": "Gal 5:19-21",
                "note": "2 Kings 21:6 catalogs Manasseh&#x2019;s religious crimes: making his son pass through fire, practicing soothsaying, divining omens, dealing with mediums and necromancers. The list of forbidden practices mirrors what Paul in Galatians 5:19-21 calls &#x201C;works of the flesh&#x201D; — including idolatry and sorcery (pharmakeia) — whose practitioners &#x201C;will not inherit the kingdom of God.&#x201D; Manasseh embodies what Galatians 5 warns against: a life organized around occult power and idolatrous practice rather than the Spirit. The Deuteronomic code that branded these practices as abominations (Deut 18:10-12) is the same Torah Paul assumes when he names sorcery among the works of the flesh that exclude from the kingdom."
            }
        ]
    }
}

def main():
    existing = load_echo('2kings')
    merge_echo(existing, TWO_KINGS_ECHOES)
    save_echo('2kings', existing)
    print('2 Kings echo fill (chs 10, 15, 21) written.')

if __name__ == '__main__':
    main()
