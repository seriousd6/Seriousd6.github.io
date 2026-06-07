"""
MKT Echo Layer — Acts chapters 22–24
Run: python3 scripts/zc-echo-acts-22-24.py

Source data used:
- data/interlinear/acts.json
- data/translation/draft/mediating/acts.json (MKT text)
- data/parallels/acts.json (no entries for chs 22–24)
- data/commentary/ellicott/acts.json (philological support)

Key decisions in this range:
- Acts 22 is Paul's first-person defense in Hebrew/Aramaic — OT allusions are
  embedded in his autobiography (Damascus road theophany, Ananias's words, temple
  vision) rather than explicit citations.
- "The Righteous One" (22:14) is the clearest Isa 53:11 allusion in Acts.
- "Calling on his name" (22:16) fulfills Joel 2:32, already cited in Acts 2:21.
- Exod 22:28 is the only explicit OT quote in this range (23:5).
- Dan 12:2 is the primary OT background for 24:15 (resurrection of righteous and wicked).
- Verses without defensible OT connections are omitted per echo selection criteria.
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


ACTS_ECHOES = {
  "22": {
    "3": [
      {"type": "allusion", "target": "Phil 3:5", "note": "Paul's credentials — circumcised on the eighth day, of the tribe of Benjamin, a Hebrew of Hebrews, a Pharisee — are the same autobiography he summarizes elsewhere; but the deeper echo is the Pharisaic zeal pattern: from Saul the zealous persecutor to Paul the apostle, the same zealous disposition is redirected by the encounter with the risen Christ."},
    ],
    "6": [
      {"type": "allusion", "target": "Ezek 1:4", "note": "A bright light from heaven flashed around Paul at noon — the Damascus theophany shares the structural features of the great OT theophanies: divine light, overwhelming brightness, prostration of the recipient. Ezekiel's chariot vision opens with a great cloud with brightness and fire; Paul's encounter on the road is the NT theophanic confrontation that matches that intensity."},
    ],
    "7": [
      {"type": "theme", "target": "Isa 53:4-5", "note": "The risen Christ's question — why do you persecute me? — reveals his identification with his suffering people. As the Servant bore the grief of others, so the exalted Christ experiences the affliction of his members as his own affliction. To strike the church is to strike Christ; the solidarity announced in Matt 25:40 is the same solidarity the Damascus road discloses."},
    ],
    "14": [
      {"type": "allusion", "target": "Isa 53:11", "note": "The God of our ancestors has chosen you to see the Righteous One — Ananias's designation of Jesus as 'the Righteous One' is the clearest echo of Isa 53:11 in Acts ('the righteous one, my servant, will justify many'). The title was already used by Peter in Acts 3:14; its repetition here in Paul's testimony confirms it as a fixed Christological title drawn from the Servant Song."},
    ],
    "15": [
      {"type": "fulfillment", "target": "Isa 43:10", "note": "You are my witnesses, says the LORD — Ananias's commission to Paul ('you will be his witness to all people') fulfills the Servant-community vocation of Isa 43:10. Israel was called to be God's witnesses to the nations; the church in Acts carries that witness-vocation forward through the apostolic testimony to the resurrection."},
    ],
    "16": [
      {"type": "fulfillment", "target": "Joel 2:32", "note": "Get up, be baptized and wash your sins away, calling on his name — 'calling on his name' fulfills the Joel 2:32 promise ('everyone who calls on the name of the LORD will be saved') already cited by Peter in Acts 2:21. Paul's baptism is the personal application of that universal salvation-call; the name of the Lord is now explicitly the name of Jesus."},
    ],
    "18": [
      {"type": "allusion", "target": "Isa 6:9-10", "note": "They will not accept your testimony about me — the Lord's warning to Paul that Jerusalem will not receive his witness echoes Isaiah's commission to preach to a people who hear but do not understand. The same pattern that governed Isaiah's mission governs Paul's: the word goes out faithfully, the official community rejects it, and the mission turns outward to those beyond the established community."},
    ],
    "21": [
      {"type": "fulfillment", "target": "Isa 49:6", "note": "I will send you far away to the Gentiles — the Lord's directive to Paul directly fulfills the Servant's mission of Isa 49:6 ('I will make you a light for the Gentiles, that my salvation may reach to the ends of the earth'). Paul's Gentile mission is not a deviation from Israel's calling but the Servant's outward movement reaching the nations as the OT prophets anticipated."},
      {"type": "fulfillment", "target": "Acts 1:8", "note": "The mission to the Gentiles far away fulfills the geographic arc of Acts 1:8 (to the ends of the earth); the Lord's directive to Paul ratifies that this Gentile outreach is the Spirit's appointed movement, not Paul's personal expansion."},
    ],
  },
  "23": {
    "3": [
      {"type": "allusion", "target": "Ezek 13:10-12", "note": "God will strike you, you whitewashed wall — Ezekiel's condemnation of false prophets as whitewashed walls (walls painted to look solid but about to collapse) is Paul's metaphor for the high priest who sits in the seat of judgment while violating the very law he administers. The image condemns hypocrisy: outward piety concealing corrupt justice."},
    ],
    "5": [
      {"type": "quote", "target": "Exod 22:28", "note": "Do not speak evil about the ruler of your people — Paul quotes Exod 22:28 directly, acknowledging his error in not recognizing the high priest's office. The quotation functions both as retraction and as legal citation: the Mosaic law itself establishes the dignity of office that Paul has momentarily violated in his heat."},
    ],
    "6": [
      {"type": "fulfillment", "target": "Acts 1:22", "note": "Paul's proclamation of resurrection before the Sanhedrin is the apostolic testimony at the center of Acts 1:22's requirement for apostleship (a witness of the resurrection). The resurrection of the dead is both the specific disputed doctrine and the hermeneutical key to the whole OT — if the dead rise, then Jesus is what the apostles claim."},
      {"type": "allusion", "target": "Dan 12:2", "note": "The hope and resurrection of the dead — Paul's appeal to 'the hope and resurrection of the dead' draws on the clearest OT resurrection text (Dan 12:2: many who sleep in the dust will awake), which was the ground of the Pharisees' resurrection belief and the scriptural foundation for the apostolic claim that Jesus's resurrection fulfills that hope."},
    ],
    "11": [
      {"type": "fulfillment", "target": "Isa 49:6", "note": "As you have testified about me in Jerusalem, so you must also testify in Rome — the Lord's night encouragement to Paul confirms that the Rome mission is divinely directed, not accidental. The ends-of-the-earth scope of Isa 49:6 and Acts 1:8 reaches its narrative climax when Paul testifies before Caesar in the imperial capital."},
    ],
    "12": [
      {"type": "allusion", "target": "Ps 37:12", "note": "The wicked plot against the righteous and gnash their teeth — the conspiracy of the forty-plus men who bind themselves with an oath to kill Paul enacts the pattern of Ps 37:12: the wicked plotting against the righteous who trusts in the Lord. The Lord's assurance of the previous night (v.11) is the Psalm's counterweight: the righteous are upheld even as the plots multiply."},
    ],
    "27": [
      {"type": "allusion", "target": "Ps 18:16-17", "note": "He reached down from on high and took hold of me; he drew me out of deep waters — Lysias's rescue of Paul from the mob enacts the psalm-pattern of divine deliverance through human instruments. The commander's letter misrepresents his own motives, but the providential deliverance it describes is genuine: the God who delivers the righteous from those stronger than them uses even a Roman commander as the instrument."},
    ],
  },
  "24": {
    "5": [
      {"type": "allusion", "target": "Amos 7:10", "note": "Tertullus calls Paul a troublemaker who stirs up riots among Jews all over the world — the accusation pattern echoes Amos 7:10, where Amaziah accuses Amos of conspiracy against the king ('the land cannot bear all his words'). The prophetic messenger accused of destabilizing the existing order is the OT precedent for Paul's situation; the real destabilization comes from the gospel, not from social unrest."},
    ],
    "14": [
      {"type": "fulfillment", "target": "Isa 8:20", "note": "I worship the God of our ancestors as a follower of the Way, which they call a sect — Paul's claim to 'believe everything that is in accordance with the Law and the Prophets' is the claim that the Way is not a sect but the fulfillment of Israel's scriptures. Isa 8:20 sets the criterion: 'to the law and to the testimony; if they do not speak according to this word, they have no light.' Paul claims the Way passes this test."},
    ],
    "15": [
      {"type": "fulfillment", "target": "Dan 12:2", "note": "There will be a resurrection of both the righteous and the wicked — Paul explicitly grounds his resurrection hope in what 'these men themselves hold.' Dan 12:2 is the OT text that establishes a bodily resurrection of both righteous and wicked for judgment; Paul claims that Jesus's resurrection is the first installment of that Daniel-promised event, and the church's hope stands on the same ground."},
      {"type": "allusion", "target": "Isa 26:19", "note": "Your dead will live, LORD; their bodies will rise — Isaiah 26:19 is the other primary OT resurrection text, expressing hope in the form of confidence that the Lord will raise the dead. Paul's 'same hope these men hold' draws on this prophetic confidence; the dispute between Paul and his accusers about resurrection is a dispute about whether Isaiah and Daniel have been fulfilled in Christ."},
    ],
    "17": [
      {"type": "allusion", "target": "Isa 61:1-2", "note": "I came to Jerusalem to bring my people gifts for the poor — Paul's description of the collection for the poor in Jerusalem echoes the Isaianic Servant's mission to bring good news to the poor (Isa 61:1-2). The concrete financial act of the collection is the material expression of the gospel-for-the-poor that Jesus announced at Nazareth (Lk 4:18); the Gentile churches' gifts to Jewish believers embody the cross-cultural unity that the Servant's mission creates."},
    ],
    "25": [
      {"type": "allusion", "target": "Dan 7:9-10", "note": "Paul talked about righteousness, self-control and the judgment to come — the topics Paul raises before Felix engage the OT's judicial vision: the Ancient of Days seated in judgment with ten thousand times ten thousand attending (Dan 7:9-10), the books opened, all deeds examined. Felix's fear is the appropriate response to hearing that the judge who evaluated his every act is the risen Christ."},
      {"type": "allusion", "target": "Eccl 12:14", "note": "God will bring every deed into judgment, including every hidden thing — Paul's 'judgment to come' before Felix invokes the Ecclesiastes conclusion (12:14) that God will judge every work, good or evil, however hidden. The message to a corrupt governor who takes bribes (v.26) and grants favor for political gain (v.27) is precisely the judgment-of-hidden-deeds that Ecclesiastes warns about."},
    ],
  }
}


def main():
    existing = load_echo('acts')
    merge_echo(existing, ACTS_ECHOES)
    save_echo('acts', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Acts echoes (22–24 added): {len(existing)} chapters, {total} verses with connections.')

if __name__ == '__main__':
    main()
