"""
MKT Echo Layer — Acts chapters 27–28
Output: data/echoes/acts.json
Run: python3 scripts/zc-echo-acts-27-28.py

Key decisions:
- Acts 28:26 (Isa 6:9-10 citation) already present; merge_echoes skips it.
- Acts 27 (the shipwreck voyage) is saturated with OT exodus/Jonah/Psalm 107 resonance:
  the sea-storm that nearly destroys echoes Jonah 1 and Ps 107:23-32;
  Paul's assurance of divine preservation echoes the angel of Ex 23:20;
  the dawn-eating scene on the last day echoes the Last Supper pattern.
- Acts 28 (Malta, Rome): the snake-bite echo of Ps 91:13 and Num 21; the healing
  of Publius's father echoes Elisha healings; the Rome arrival echoes Isa 40 and 52;
  the Isaiah 6 citation closes Luke-Acts with the same note that opened Isaiah's ministry.
- Echo entries anchor on the verse where the OT resonance is most concentrated.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echoes(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echoes(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echoes(existing, new_data):
    # INTENT: Add new chapter/verse echo entries without overwriting existing ones — safe to re-run.
    # CHANGE? If echo JSON structure changes from {ch:{v:[entries]}}, update this traversal.
    # VERIFY: Re-running should produce identical verse counts (no duplicated entries).
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries

ACTS_ECHOES = {
"27": {
    "9": [
        {
            "type": "allusion",
            "target": "Lev 16:29-31",
            "note": "The reference to 'the Fast' (tēs nēsteias) — Yom Kippur, the Day of Atonement — as the seasonal marker for dangerous Mediterranean sailing situates the voyage in the liturgical calendar of Israel. The Fast of Leviticus 16 is the annual day of national atonement and humbling; Paul's reference to it anchors the pagan sea-voyage within the Jewish covenant calendar that structures sacred time."
        }
    ],
    "14": [
        {
            "type": "typology",
            "target": "Jon 1:4",
            "note": "The great storm (anemos typhonikos — a typhoon-force wind) striking the ship after Paul's warning was ignored directly echoes the storm in Jonah 1:4 ('the LORD hurled a great wind upon the sea, and there was a mighty tempest on the sea'). The reluctant prophet, the sea-storm, the endangered sailors, and the divine purpose behind the storm all parallel — but where Jonah was thrown overboard to save the crew, Paul stays aboard to save them."
        }
    ],
    "20": [
        {
            "type": "allusion",
            "target": "Ps 107:25-27",
            "note": "The crew's despair ('all hope of our being saved was at last abandoned') echoes Psalm 107:27-28 — those who 'go down to the sea in ships... they reeled and staggered like drunken men and were at their wits' end. Then they cried to the LORD in their trouble.' The Psalm's storm-at-sea is the archetypal sea-deliverance pattern that the Acts 27 narrative embodies and extends to a pagan crew."
        }
    ],
    "23": [
        {
            "type": "typology",
            "target": "Exod 23:20",
            "note": "The angel of God who stands by Paul in the night and promises divine preservation ('Do not be afraid, Paul; you must stand before Caesar, and behold, God has granted you all those who sail with you') echoes the angel-of-the-LORD who preceded Israel through the wilderness: 'Behold, I send an angel before you to guard you on the way and to bring you to the place that I have prepared' (Exod 23:20). The divine-protection-through-angel pattern accompanies the mission."
        }
    ],
    "25": [
        {
            "type": "allusion",
            "target": "Dan 3:17-18",
            "note": "Paul's 'take heart, men, for I have faith in God that it will be exactly as I have been told' echoes the confidence-before-catastrophe of Shadrach, Meshach, and Abednego before the furnace: 'If this be so, our God whom we serve is able to deliver us... But if not, be it known to you, O king, that we will not serve your gods' (Dan 3:17-18). Both are declarations of faith-grounded courage in the face of certain human defeat."
        }
    ],
    "33": [
        {
            "type": "typology",
            "target": "Mark 6:41",
            "note": "Paul's dawn-meal before the shipwreck — taking bread, giving thanks before all, breaking it, and beginning to eat — follows the Eucharistic-Last Supper gesture-sequence used in Luke 22:19 and the feeding of the five thousand (Luke 9:16; Mark 6:41): took bread, gave thanks, broke, distributed. The pattern is not coincidental: Luke frames the pre-wreck meal as a communion-shaped act of sustained hope in the middle of a storm."
        }
    ],
    "34": [
        {
            "type": "fulfillment",
            "target": "1 Sam 14:45",
            "note": "'For not a hair is to perish from the head of any of you' (thriks apo tēs kephalēs oudenos apoleitai) is an OT idiom for absolute divine protection: 'not a hair of his head shall fall to the ground' (1 Sam 14:45, of Jonathan; 2 Sam 14:11; Luke 21:18). Paul's guarantee of physical survival uses the covenant-preservation formula — the same words used of those whom God protects from deserved judgment. The word of God's preservation is as certain as his word of judgment."
        }
    ],
    "44": [
        {
            "type": "fulfillment",
            "target": "Ps 107:30",
            "note": "All 276 people escaping safely to land fulfills the pattern of Psalm 107:30 — 'they were glad that the waters were quiet, and he brought them to their desired haven.' The Psalm's sea-deliverance that produces praise is enacted in historical narrative: the storm, the despair, the divine word through the prophet, and the safe arrival. Acts 27 is the Psalm 107 sea-deliverance lived out on a grain ship bound for Rome."
        }
    ]
},
"28": {
    "3": [
        {
            "type": "typology",
            "target": "Ps 91:13",
            "note": "The snake fastening itself to Paul's hand on Malta echoes Psalm 91:13 — 'you will tread on the lion and the adder; the young lion and the serpent you will trample underfoot.' Paul's shaking off the viper without harm is the enacted version of the promise given to those who dwell in the shelter of the Most High. The serpent-and-the-mission motif also echoes Genesis 3:15 (enmity between the seed and the serpent) and Mark 16:18."
        }
    ],
    "5": [
        {
            "type": "typology",
            "target": "Num 21:8-9",
            "note": "Paul suffering no harm from the viper's bite echoes the bronze serpent episode: those bitten by serpents who looked at the bronze serpent lived (Num 21:8-9). Jesus applied this typology to himself (John 3:14-15 — 'as Moses lifted up the serpent in the wilderness, so must the Son of Man be lifted up'). Paul's immunity to the serpent is the apostle participating in the dominion over the serpent that the crucified and risen Christ has established."
        }
    ],
    "8": [
        {
            "type": "typology",
            "target": "2 Kgs 5:11",
            "note": "Paul praying, laying hands on Publius's father, and healing him echoes the Elisha healings — most directly Elisha's healing of Naaman and the Shunammite's son. The pattern (prophet prays, lays on hands or applies physical contact, healing follows) is consistent across 1-2 Kings and Acts. Luke has modeled Paul's healing ministry on the Elijah-Elisha pattern as consistently as Peter's."
        }
    ],
    "15": [
        {
            "type": "allusion",
            "target": "Isa 40:9-10",
            "note": "Brothers from Rome coming to meet Paul on the Appian Way (at the Three Taverns and the Forum of Appius) echoes the herald's cry of Isaiah 40:9-10: 'Go on up to a high mountain, O Zion, herald of good news... say to the cities of Judah, Behold your God!' The coming-to-meet is the reverse-journey of welcome: Paul the herald of good news is welcomed by those who have already received it. Rome receives the gospel's envoy as the ends of the earth receive the word of the LORD."
        }
    ],
    "20": [
        {
            "type": "fulfillment",
            "target": "Isa 52:2",
            "note": "Paul's explanation that 'it is because of the hope of Israel that I am wearing this chain' frames his Roman imprisonment as a fulfillment of the Servant's bound-but-victorious mission. Isaiah 52:2 addresses the 'captive daughter of Zion': 'Loose the bonds from your neck, O captive daughter of Zion.' Paul wears in his own body the bonds that the gospel loosens from those who receive it — his chain is the price of others' liberation."
        }
    ],
    "26": [
        {
            "type": "fulfillment",
            "target": "Isa 6:9-10",
            "note": "Already present."
        }
    ],
    "28": [
        {
            "type": "fulfillment",
            "target": "Isa 49:6",
            "note": "Paul's final declaration — 'this salvation of God has been sent to the Gentiles; they will listen' — closes Acts with the Servant's commission from Isaiah 49:6: 'I will make you a light for the nations, that my salvation may reach to the end of the earth.' Rome is the end of the earth from Jerusalem's perspective; Luke-Acts ends where Isaiah said the salvation would reach. The book of Acts is the fulfillment-narrative of Isaiah's Servant-mission trajectory."
        }
    ],
    "31": [
        {
            "type": "fulfillment",
            "target": "Isa 52:7",
            "note": "Paul 'proclaiming the kingdom of God and teaching about the Lord Jesus Christ with all boldness and without hindrance' as the final image of Acts fulfills Isaiah 52:7 — 'How beautiful are the feet of him who brings good news, who publishes peace, who brings good news of happiness, who publishes salvation, who says to Zion, Your God reigns!' The herald has reached Rome; the kingdom has been proclaimed at the center of the world; Acts ends with the herald's work ongoing and unstoppable."
        }
    ]
}
}

def main():
    existing = load_echoes('acts')
    merge_echoes(existing, ACTS_ECHOES)
    save_echoes('acts', existing)
    for ck in ['27', '28']:
        n = len(existing.get(ck, {}))
        print(f'Acts ch {ck}: {n} echo entries')

if __name__ == '__main__':
    main()
