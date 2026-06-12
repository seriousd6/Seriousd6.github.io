"""
MKT Echo Layer — Proverbs chapters 19–21
Run: python3 scripts/zc-echo-proverbs-19-21.py

Ch19: Integrity over wealth (19:1) — Matt 5:3; kindness to poor lends to God (19:17) — Matt 25:40;
      LORD's purpose stands (19:21) — Acts 4:28; slow to anger (19:11) — Jas 1:19
Ch20: None can claim a pure heart (20:9) — Rom 3:10; do not repay evil (20:22) — Rom 12:19;
      spirit as God's lamp (20:27) — 1 Cor 2:10-11; steadfast love upholds the king (20:28) — Luke 1:33
Ch21: King's heart in God's hand (21:1) — Acts 4:27-28; righteousness over sacrifice (21:3) — Matt 9:13;
      wicked substitute for righteous (21:18) — 1 Pet 3:18; victory belongs to God (21:31) — Rev 19:11
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

ECHOES = {
  "19": {
    "1": [
      {"type": "theme", "target": "Matt 5:3", "note": "Better a poor man who walks in integrity than a crooked-tongued fool — the proverb sets moral character above material status. The Sermon's first beatitude ('blessed are the poor in spirit') works the same ground: the one who lacks worldly standing but possesses moral integrity is declared blessed. Both texts resist the assumption that prosperity signals virtue."},
      {"type": "allusion", "target": "Luke 6:20", "note": "The plain-beatitude form ('blessed are you who are poor') is closer to Proverbs' concrete formulation — a real poor person whose integrity surpasses the socially advantaged fool. The proverb contributes to the sapience tradition Luke's beatitudes draw on."}
    ],
    "11": [
      {"type": "allusion", "target": "Jas 1:19", "note": "A man's wisdom makes him slow to anger, and it is his glory to overlook an offense — the sapience tradition James explicitly takes up: 'let every person be quick to hear, slow to speak, slow to anger.' The 'glory' of restraint is not weakness but a mark of wise character."},
      {"type": "theme", "target": "1 Pet 4:8", "note": "Overlooking an offense as glory parallels 'love covers a multitude of sins' (1 Pet 4:8, citing Prov 10:12). Both texts commend the absorptive capacity of the wise person who does not press every grievance — a pattern the NT grounds in God's own forgiveness through Christ."}
    ],
    "17": [
      {"type": "allusion", "target": "Matt 25:40", "note": "Whoever is kind to the poor lends to the LORD, and he will repay him for his deed — the identification of service to the poor with service to God is the precise logic of Matthew 25:40: 'as you did it to one of the least of these my brothers, you did it to me.' The proverb's accounting metaphor (lends, repay) anticipates the eschatological reckoning Christ describes."},
      {"type": "theme", "target": "Luke 6:35", "note": "The divine repayment promised here ('he will repay') finds its eschatological form in Luke 6:35: 'your reward will be great, and you will be sons of the Most High.' Generosity to the poor is conduct that reflects the character of God and receives its return from him."}
    ],
    "21": [
      {"type": "allusion", "target": "Acts 4:28", "note": "Many are the plans in a human heart, but the LORD's purpose is what stands — the Acts 4 prayer quotes Ps 2 and then declares that Herod, Pilate, Gentiles, and Israel did 'whatever your hand and your plan had predestined to take place' (Acts 4:28). The proverb's principle — human plans are many but God's single purpose prevails — is the theological ground on which the early church interpreted the crucifixion."},
      {"type": "theme", "target": "Eph 1:11", "note": "The LORD's purpose standing over all human plans is the principle Paul states as the foundation of election: God 'works all things according to the counsel of his will' (Eph 1:11). The proverb's assertion of divine sovereignty over human planning is the OT sapience form of Pauline predestination."}
    ],
    "22": [
      {"type": "theme", "target": "Heb 13:5", "note": "What is desired in a person is faithful love (chesed) — the premier covenant virtue. The NT's promise of Christ's unfailing presence ('I will never leave you nor forsake you,' Heb 13:5) is the ultimate expression of chesed — the faithful love Proverbs identifies as the most desirable human quality is what God himself provides through Christ."}
    ]
  },
  "20": {
    "9": [
      {"type": "theme", "target": "Rom 3:10", "note": "Who can say, 'I have made my heart pure; I am clean from my sin'? — the rhetorical question expects no answer. Paul's summary of the Psalms and Prophets reaches the same conclusion: 'None is righteous, no, not one' (Rom 3:10). The proverb's wisdom-observation about universal moral incompleteness becomes the biblical-theological premise for the doctrine of universal sinfulness that the gospel addresses."},
      {"type": "allusion", "target": "1 John 1:8", "note": "The proverb's implied 'no one' is echoed in 1 John: 'If we say we have no sin, we deceive ourselves, and the truth is not in us' (1 John 1:8). The self-deception that would answer Proverbs' question affirmatively is precisely what John warns against — the honesty Proverbs requires ('who can say?') is the same honesty that opens the door to Christ's cleansing (1 John 1:9)."}
    ],
    "22": [
      {"type": "allusion", "target": "Rom 12:17-19", "note": "Do not say, 'I will repay evil'; wait on the LORD and he will deliver you — Paul's instructions in Romans 12 draw directly on this: 'Repay no one evil for evil... Beloved, never avenge yourselves, but leave it to the wrath of God, for it is written, Vengeance is mine, I will repay, says the Lord' (Rom 12:17,19). The proverb is the sapience basis for the NT's ethic of non-retaliation grounded in divine justice."},
      {"type": "theme", "target": "Matt 5:39", "note": "Christ's 'do not resist the one who is evil' (Matt 5:39) takes this wisdom-ethic to its radical Christological extreme — not merely waiting for God to act but actively absorbing evil without repayment, as Christ himself did on the cross."}
    ],
    "27": [
      {"type": "allusion", "target": "1 Cor 2:10-11", "note": "The human spirit is the LORD's lamp, searching all the innermost parts — Proverbs pictures God using the human spirit as his instrument of inner examination. Paul extends this: 'the Spirit searches everything, even the depths of God... no one comprehends the thoughts of God except the Spirit of God' (1 Cor 2:10-11). The lamp/Spirit that searches inward is taken up as the Spirit of God himself who searches the divine depths and discloses them."}
    ],
    "28": [
      {"type": "type", "target": "Luke 1:32-33", "note": "Steadfast love (chesed) and faithfulness preserve the king, and his throne is upheld by faithful love — the royal ideal of chesed-upheld kingship. The angel's announcement to Mary applies this directly to Christ: 'he will be great and will be called the Son of the Most High. And the Lord God will give to him the throne of his father David, and he will reign over the house of Jacob forever' (Luke 1:32-33). Christ is the king whose throne is upheld by the chesed he embodies completely."},
      {"type": "allusion", "target": "Heb 1:8", "note": "The throne upheld by faithful love anticipates Hebrews' citation of Ps 45: 'Your throne, O God, is forever and ever' (Heb 1:8). The Davidic king's throne sustained by chesed finds its eternal fulfillment in the Son whose kingship is permanent."}
    ]
  },
  "21": {
    "1": [
      {"type": "allusion", "target": "Acts 4:27-28", "note": "The king's heart is in the hand of the LORD like channels of water, directed wherever he pleases — Acts 4:27-28 applies this principle to the crucifixion itself: 'both Herod and Pontius Pilate, along with the Gentiles and the peoples of Israel, gathered together against your holy servant Jesus... to do whatever your hand and your plan had predestined to take place.' The king whose heart God directs is the Roman prefect; the channel is redirected toward the redemptive purpose God had determined."}
    ],
    "3": [
      {"type": "allusion", "target": "Matt 9:13", "note": "To do righteousness and justice is more acceptable to the LORD than sacrifice — this is the sapience form of the prophetic critique (Hos 6:6; Amos 5:21-24; Mic 6:8). Christ quotes Hosea 6:6 directly in Matthew 9:13 ('I desire mercy, not sacrifice'), placing himself on the side of the prophets and wisdom tradition against ritual formalism. Proverbs confirms the same priority: the moral demand precedes the cultic one."},
      {"type": "theme", "target": "Heb 10:8-9", "note": "Hebrews cites Psalm 40:6-8 to argue that Christ's offering of himself replaces the Levitical sacrifices — 'sacrifices and offerings you have not desired' replaced by 'I have come to do your will.' Proverbs' preference for righteousness over sacrifice is the wisdom-tradition basis for Hebrews' argument that the old sacrificial system was always pointing beyond itself."}
    ],
    "13": [
      {"type": "allusion", "target": "Luke 16:25", "note": "Whoever stops his ears at the cry of the poor will himself cry out and not be heard — the exact retributive logic of the Rich Man and Lazarus: Abraham says to the rich man who ignored the poor man at his gate, 'Child, remember that you in your lifetime received your good things, and Lazarus in like manner bad things' (Luke 16:25). The proverb's warning becomes narrative in Christ's parable."},
      {"type": "theme", "target": "Jas 2:13", "note": "'Judgment is without mercy to one who has shown no mercy' (Jas 2:13) — James's categorical statement is the NT equivalent of the proverb's retributive pattern: the one who closes his ears will not be heard. The reversal of mercy withheld is the shape of judgment both texts describe."}
    ],
    "18": [
      {"type": "type", "target": "1 Pet 3:18", "note": "The wicked are a substitute (kofer, ransom) for the righteous, and the treacherous take the place of the upright — the substitution pattern, where the wicked bear consequences that should fall on the righteous, is inverted in the atonement: 'Christ also suffered once for sins, the righteous for the unrighteous' (1 Pet 3:18). Proverbs describes the normal retributive pattern; the gospel reverses it with the holy one substituting for the guilty."},
      {"type": "allusion", "target": "Isa 43:3", "note": "Isaiah uses the same substitution language in a redemptive direction: 'I give Egypt as your ransom, Cush and Seba in exchange for you' (Isa 43:3). The kofer/substitution concept undergoes its ultimate transformation when Christ himself becomes the ransom (Mark 10:45)."}
    ],
    "21": [
      {"type": "allusion", "target": "Matt 5:6", "note": "Whoever pursues righteousness and steadfast love will find life, righteousness, and honor — the beatitude pattern: those who pursue the right things find life and vindication. Christ's beatitude for those who 'hunger and thirst for righteousness' (Matt 5:6) promises they 'shall be satisfied' — the pursuit and its fulfillment are the same structure Proverbs describes, now grounded in Christ as the source of the righteousness being sought."}
    ],
    "30": [
      {"type": "theme", "target": "1 Cor 1:25", "note": "There is no wisdom, no understanding, no counsel that can stand against the LORD — the comprehensive assertion that all human wisdom-claims are subordinate to God. Paul's argument in 1 Corinthians 1 is the NT expansion: 'the foolishness of God is wiser than men, and the weakness of God is stronger than men' (1 Cor 1:25). The cross is the place where this is demonstrated — the wisdom of the world counseled against it, and it stands as the wisdom of God."}
    ],
    "31": [
      {"type": "allusion", "target": "Rev 19:11", "note": "The horse is made ready for the day of battle, but victory belongs to the LORD — the proverb's final word on military preparedness: equip as you must, but the outcome is not in the horse. The rider on the white horse in Revelation 19:11 ('Faithful and True... in righteousness he judges and makes war') is the embodiment of this principle: the victory that belongs to the LORD is won by the one who is himself the LORD."},
      {"type": "theme", "target": "Ps 20:7", "note": "The proverb distills what Psalm 20:7 states in full: 'Some trust in chariots and some in horses, but we trust in the name of the LORD our God.' The trust in military preparation that Proverbs brackets with divine sovereignty is the same trust the Psalms redirect toward God — and that the NT places in Christ as the one through whom God wins his decisive battle."}
    ]
  }
}

def main():
    e = load_echo('proverbs')
    merge_echo(e, ECHOES)
    save_echo('proverbs', e)
    count = sum(len(v) for v in ECHOES.values())
    print(f'proverbs echo: wrote entries for {count} verses in ch 19-21')

if __name__ == '__main__':
    main()
