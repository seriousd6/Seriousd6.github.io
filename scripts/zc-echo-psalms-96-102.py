"""
Echo data — Psalms chapters 96–102 (gap-fill: chs 96–101 missing; 102 already present)
Run: python3 scripts/zc-echo-psalms-96-102.py

Key connections across the Enthronement Psalms (93–100) and surrounding psalms:
- Ps 96:1: "Sing a new song" → Rev 5:9 (new song to the Lamb who was slain).
- Ps 96:13 / 98:9: "Coming to judge the earth with righteousness" → Acts 17:31
  (God has set a day; the appointed judge is the risen Christ).
- Ps 97:7: "All gods bow down before him" → Phil 2:10-11 (every knee bows to Christ).
- Ps 97:9: "Raised far above all gods" → Eph 1:20-21 (Christ raised far above all rule).
- Ps 98:1: "His right hand and holy arm have gained him the victory" → Acts 2:33
  (Christ exalted to God's right hand); Luke 2:30-32 (Simeon's song: salvation seen).
- Ps 98:2-3: "Salvation shown to the nations, all ends of the earth have seen" →
  Luke 2:30-32 / Isa 52:10 (light for the Gentiles, fulfilled in Christ).
- Ps 99:6-8: God answered Moses, Aaron, Samuel when they called → Heb 7:25
  (Christ always lives to intercede — the pattern of divine response fulfilled).
- Ps 100:3: "We are his people, the flock he tends" → John 10:14/16 (Good Shepherd
  who knows his flock and gathers others not yet of this pen).
- Ps 101:2: "Walk with a blameless heart" → Heb 4:15 (Christ tempted in every way
  yet without sin — the blameless heart David vowed, Christ enacted).
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

# INTENT: Echo data for Psalms 96–101 — the enthronement cluster declaring the LORD
#   reigns and coming to judge, with each key theme finding NT fulfillment: the new
#   song (Ps 96 → Rev 5:9), every knee bowing (Ps 97:7 → Phil 2:10), victory by the
#   right arm (Ps 98:1 → Acts 2:33), the Good Shepherd's flock (Ps 100:3 → John 10),
#   and the blameless king (Ps 101:2 → Heb 4:15).
# CHANGE? If data/echoes/psalms.json structure changes, update load_echo/save_echo
#   per Z_COMMENTARY_SCRIPT_GUIDE.md.
# VERIFY: python3 -c "import json; d=json.load(open('data/echoes/psalms.json')); print([len(d.get(str(c),{})) for c in range(96,103)])" should show non-zero for all.

PSALMS_ECHOES = {
  "96": {
    "1": [
      {
        "type": "fulfillment",
        "target": "Rev 5:9",
        "note": "Sing a new song to the LORD; let all the earth sing to the LORD! — 'And they sang a new song: \"You are worthy to take the scroll and to open its seals, because you were slain, and with your blood you purchased for God persons from every tribe and language and people and nation\"' (Rev 5:9). The new song of Psalm 96:1 — sung by all the earth — is the song Revelation discloses as the song of the slain-and-risen Lamb. The newness is the redemption: what makes this song new in the NT is that the one who has come to judge (v.13) has first come to save."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Rev 11:15",
        "note": "Declare among the nations: 'The LORD reigns!' — 'The kingdom of the world has become the kingdom of our Lord and of his Messiah, and he will reign for ever and ever' (Rev 11:15). The proclamation to the nations that the LORD reigns (Ps 96:10) is the announcement Revelation makes at the seventh trumpet — the moment when the kingdom of this world becomes fully the kingdom of Christ. The Psalm's missionary call to declare divine reign is fulfilled in the eschatological declaration that Christ's reign is universal and permanent."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Acts 17:31",
        "note": "He is coming to judge the earth; he will judge the world in righteousness and the peoples in his faithfulness — 'for he has set a day when he will judge the world with justice by the man he has appointed. He has given proof of this to everyone by raising him from the dead' (Acts 17:31). The coming judge of Psalm 96:13 who judges with righteousness is the risen Christ whom God has appointed. The Psalm's anticipation of the righteous judge arriving is the NT's announcement that the judge has already been revealed — he is the risen Jesus."
      }
    ]
  },
  "97": {
    "7": [
      {
        "type": "fulfillment",
        "target": "Phil 2:10",
        "note": "All who worship carved images are put to shame — those who boast in worthless idols. All gods bow down before him — 'that at the name of Jesus every knee should bow, in heaven and on earth and under the earth, and every tongue acknowledge that Jesus Christ is Lord, to the glory of God the Father' (Phil 2:10-11). The bowing of all gods before the LORD (Ps 97:7) is fulfilled in the universal bowing before the name of Jesus. Paul's hymn presents the exalted Christ as the one before whom the cosmic powers — including all that the nations worshipped — must bow."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Eph 1:21",
        "note": "You, LORD, are most high over all the earth; you are raised far above all gods — 'far above all rule and authority, power and dominion, and every name that is invoked, not only in the present age but also in the one to come' (Eph 1:21). Paul applies the language of Psalm 97:9 — raised far above all — to the resurrection-ascension of Christ. The exaltation of the LORD above all gods in the Psalm is the exaltation of Christ that Ephesians describes. Christ occupies the position the Psalm ascribes to the Most High."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "John 8:12",
        "note": "Light is sown for the righteous and gladness for the upright in heart — 'I am the light of the world. Whoever follows me will never walk in darkness, but will have the light of life' (John 8:12). The sown light for the righteous (Ps 97:11) is the light Christ claims to be and to give. The light planted like seed that grows and illuminates the righteous is the light-of-the-world that Christ embodies — his coming is the sowing of light that Psalm 97:11 promises."
      }
    ]
  },
  "98": {
    "1": [
      {
        "type": "allusion",
        "target": "Acts 2:33",
        "note": "His own right hand and his holy arm have gained him the victory — 'Exalted to the right hand of God, he has received from the Father the promised Holy Spirit and has poured out what you now see and hear' (Acts 2:33). The victory won by the LORD's right hand and holy arm (Ps 98:1) is applied by Peter to the resurrection and ascension of Christ — the victory gained is the defeat of death, and the victorious right hand is the position Christ now occupies. Luke 1:51: 'he has performed mighty deeds with his arm.'"
      }
    ],
    "2": [
      {
        "type": "fulfillment",
        "target": "Luke 2:30",
        "note": "The LORD has made his salvation known and has displayed his righteousness before the nations. All the ends of the earth have witnessed the salvation of our God — 'my eyes have seen your salvation, which you have prepared in the sight of all nations: a light for revelation to the Gentiles and the glory of your people Israel' (Luke 2:30-32). Simeon's song in the Temple applies Psalm 98:2-3 directly to the infant Christ: the salvation displayed before all nations, seen to the ends of the earth, is the child in his arms. The Psalm's global salvation-display becomes the announcement that God's salvation has arrived in person."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Rev 19:11",
        "note": "He will rule the world with righteousness and the peoples with fairness — 'I saw heaven standing open and there before me was a white horse, whose rider is called Faithful and True. With justice he judges and wages war' (Rev 19:11). The righteous and fair world-ruler of Psalm 98:9 is the rider on the white horse — the returning Christ who judges with justice. Psalm 98's anticipation of the coming righteous judge becomes Revelation's vision of the Christ who comes in justice."
      }
    ]
  },
  "99": {
    "1": [
      {
        "type": "allusion",
        "target": "Rev 4:8",
        "note": "The LORD reigns; let the peoples tremble! He is enthroned above the cherubim — 'each of the four living creatures had six wings and was covered with eyes all around, even under its wings. Day and night they never stop saying: \"Holy, holy, holy is the Lord God Almighty, who was, and is, and is to come\"' (Rev 4:8). The divine enthronement above the cherubim in Psalm 99:1 is the throne that Revelation reveals — the same throne from which the Lamb opens the seals. The trembling of peoples before the enthroned LORD becomes the worship of the heavenly throne-room where the Lamb shares the throne (Rev 5:6-7)."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Heb 7:25",
        "note": "Moses and Aaron were among his priests; Samuel was among those who called on his name. They called out to the LORD, and he answered them — 'therefore he is able to save completely those who come to God through him, because he always lives to intercede for them' (Heb 7:25). The pattern of divine response to intercessory prayer (Moses, Aaron, Samuel praying and God answering) reaches its fulfillment in Christ as the eternal intercessor. Unlike Moses and Aaron who ministered for a time, Christ always lives to intercede — the answered prayer of Psalm 99:6 becomes the permanent intercession of the eternal high priest."
      }
    ]
  },
  "100": {
    "3": [
      {
        "type": "allusion",
        "target": "John 10:14",
        "note": "He made us, and we belong to him; we are his people, the flock he tends — 'I am the good shepherd; I know my sheep and my sheep know me — just as the Father knows me and I know the Father — and I lay down my life for the sheep. I have other sheep that are not of this sheep pen' (John 10:14-16). The flock that belongs to the LORD, his people whom he tends (Ps 100:3), is the flock that Christ claims as the Good Shepherd. His disclosure that he has 'other sheep not of this pen' expands the flock of Psalm 100 to include Gentile believers — all the earth (v.1) becoming his flock."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Heb 13:8",
        "note": "For the LORD is good; his steadfast love endures forever, and his faithfulness reaches to every generation — 'Jesus Christ is the same yesterday and today and forever' (Heb 13:8). The eternal faithfulness of the LORD that Psalm 100:5 celebrates — enduring forever, reaching every generation — is the constancy that Hebrews attributes to Christ personally. The hesed and emet (steadfast love and faithfulness) that the Psalm declares permanent are the character of the Son who, as Heb 1:3 states, 'sustains all things by his powerful word' — always and without change."
      }
    ]
  },
  "101": {
    "2": [
      {
        "type": "allusion",
        "target": "Heb 4:15",
        "note": "I will conduct myself with wisdom and integrity... I will walk with a blameless heart within my own house — 'we do not have a high priest who is unable to empathize with our weaknesses, but we have one who has been tempted in every way, just as we are — yet he did not sin' (Heb 4:15). The blameless heart that David vows in Psalm 101:2 — the kingly integrity he commits to — is the holiness Christ enacts perfectly and permanently. David aspires to walk blamelessly within his own house; Christ, as the greater son of David, walks in perfect integrity through the house of human nature, qualifying him to be both king and priest for those who cannot achieve what David vowed."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Rev 21:27",
        "note": "Each morning I will silence all the wicked in the land, cutting off every evildoer from the city of the LORD — 'nothing impure will ever enter it, nor will anyone who does what is shameful or deceitful, but only those whose names are written in the Lamb's book of life' (Rev 21:27). The king's promise to purge every evildoer from the city of the LORD (Ps 101:8) is fulfilled eschatologically in the new Jerusalem — the city from which nothing impure is excluded. The royal justice that Psalm 101:8 envisions is enacted by the Lamb whose city is forever purged of all wickedness."
      }
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    for ch in ['96', '97', '98', '99', '100', '101', '102']:
        entries = len(existing.get(ch, {}))
        print(f"  ch{ch}: {entries} verses with entries")
    print("Psalms 96–102 echoes complete.")

if __name__ == '__main__':
    main()
