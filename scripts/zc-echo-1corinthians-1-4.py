"""
Echo layer — 1 Corinthians chapters 1–4 (Wisdom/foolishness of the cross; apostolic ministry)
Output: data/echoes/1corinthians.json (creates file, adds chs1-4)

Key OT resonances:
- 1:19 = Isa 29:14 (destroy wisdom of the wise) — explicit citation
- 1:20 = Isa 19:12 + 33:18 (where is the wise man?)
- 1:23 = Isa 8:14 (stumbling stone to Israel)
- 1:24 = Prov 8:22-31 (Wisdom personified)
- 1:27-28 = Gideon / David — YHWH choosing the weak
- 1:31 = Jer 9:24 (boast in the Lord) — explicit citation
- 2:9 = Isa 64:4 (eye has not seen) — explicit or partial citation
- 2:16 = Isa 40:13 (who has known the mind of the Lord?) — explicit citation
- 3:11 = Isa 28:16 (precious tested cornerstone)
- 3:13 = Mal 3:2-3 (refiner's fire at the Day of the Lord)
- 3:16 = Exod 25:8 / Ezek 37:27 (God dwelling in his sanctuary)
- 3:19 = Job 5:13 (catches the wise in their craftiness) — explicit citation
- 3:20 = Ps 94:11 (Lord knows thoughts of the wise are futile) — explicit citation
- 4:13 = Lam 3:45 (scum and refuse of the earth)
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

ECHOES = {
  "1": {
    "19": [
      {"type": "quote", "target": "Isa 29:14", "note": "I will destroy the wisdom of the wise; the intelligence of the intelligent I will frustrate — Paul cites Isa 29:14 directly. In context Isaiah pronounces judgment on Jerusalem's leaders who plan against God in darkness; their sophisticated political wisdom will be nullified. Paul applies the same text to the cross's subversion of Greek rhetorical wisdom and Jewish sign-seeking."}
    ],
    "20": [
      {"type": "allusion", "target": "Isa 19:12", "note": "Where are your wise men? Let them tell you and make known what the LORD Almighty has planned against Egypt — Isaiah's taunt at Egypt's counselors who cannot discern the divine plan; Paul's triple rhetorical question (where is the wise? the teacher of the law? the philosopher?) echoes this prophetic challenge: wisdom that cannot read God's actions in history is not wisdom."},
      {"type": "allusion", "target": "Isa 33:18", "note": "Where is the officer? Where is the one who took the revenue? Where is the one who counted the towers? — Isaiah's eschatological taunt against the Assyrian military bureaucracy; the rhetorical where-is-the-X pattern is the form Paul reuses for the intellectual categories of his own day."}
    ],
    "23": [
      {"type": "allusion", "target": "Isa 8:14", "note": "He will be a holy place; for both Israel and Judah he will be a stone that causes people to stumble and a rock that makes them fall — Isaiah's oracle that YHWH himself would become a stumbling stone (petra skandalou) to Israel recurs in Paul's description of Christ crucified as a stumbling block (skandalon) to Jews. The image of YHWH's own action being the thing that causes his people to stumble anticipates the paradox of the cross."}
    ],
    "24": [
      {"type": "allusion", "target": "Prov 8:22-31", "note": "The LORD brought me forth as the first of his works... I was there when he set the heavens in place... I was filled with delight day after day — Wisdom personified in Prov 8 is present at creation, the agent through whom God works. Paul's identification of Christ as 'the wisdom of God' draws directly on this personified Wisdom tradition, identifying Jesus as the one who was with God in creation and is now the true Wisdom through whom God acts in redemption."}
    ],
    "27": [
      {"type": "type", "target": "Judg 7:2-7", "note": "The LORD said to Gideon: You have too many men... in order that Israel may not boast against me that her own strength saved her — YHWH's deliberate reduction of Gideon's army from 32,000 to 300 is the paradigmatic OT instance of God choosing the weak and few to shame the strong and many, so that the glory of victory belongs entirely to him. Paul's principle in 1:27-29 (God chose the weak to shame the strong so that no one may boast) recapitulates this Gideon-pattern."},
      {"type": "type", "target": "1 Sam 16:7", "note": "Do not consider his appearance or his height... The LORD does not look at the things people look at. People look at the outward appearance, but the LORD looks at the heart — YHWH's choice of David, the youngest son passed over by human assessors, as Israel's king embodies the same reversal-of-human-criteria principle Paul states: God chose what is despised and overlooked by human standards."}
    ],
    "29": [
      {"type": "allusion", "target": "Jer 9:23", "note": "Let not the wise boast of their wisdom or the strong boast of their strength or the rich boast of their riches — Jeremiah's oracle against the three categories of human pride (wisdom, strength, wealth) provides the negative ground for Paul's application: the cross eliminates all grounds for boasting before God because it nullifies the world's three primary currencies of status."}
    ],
    "31": [
      {"type": "quote", "target": "Jer 9:24", "note": "But let the one who boasts boast about this: that they have the understanding to know me, that I am the LORD, who exercises kindness, justice and righteousness on earth — Paul cites Jer 9:24 as the positive ground for the only legitimate boasting: knowing YHWH. Paul's 'boast in the Lord' makes Christ the locus of knowing YHWH, so that boasting in the Lord Christ is the new form of the Jeremianic covenant-knowledge."}
    ]
  },
  "2": {
    "9": [
      {"type": "allusion", "target": "Isa 64:4", "note": "Since ancient times no one has heard, no ear has perceived, no eye has seen any God besides you, who acts on behalf of those who wait for him — Isaiah's prayer of lament and hope applies YHWH's incomparable action to those who wait; Paul applies the same pattern to the hidden wisdom now revealed through the Spirit: what no eye has seen God has prepared for those who love him, disclosed not through human investigation but through divine revelation."},
      {"type": "allusion", "target": "Isa 65:17", "note": "See, I will create new heavens and a new earth. The former things will not be remembered, nor will they come to mind — the new-creation context of the incomprehensible divine action in Isa 64-65 grounds Paul's citation; the Spirit-revealed wisdom is the wisdom of the new creation, incommensurable with the categories of the old age."}
    ],
    "16": [
      {"type": "quote", "target": "Isa 40:13", "note": "Who can fathom the Spirit of the LORD, or instruct the LORD as his counselor? — Paul cites Isa 40:13 (LXX: Who has known the mind of the Lord?) to establish that unspiritual humanity cannot know the mind of God. He then makes the shocking claim that follows: 'But we have the mind of Christ.' The Isaiah context (the incomparability of YHWH in the opening of Deutero-Isaiah) makes the Christological claim explosive: possessing the mind of Christ is possessing the mind of YHWH."}
    ]
  },
  "3": {
    "11": [
      {"type": "allusion", "target": "Isa 28:16", "note": "So this is what the Sovereign LORD says: See, I lay a stone in Zion, a tested stone, a precious cornerstone for a sure foundation — Isaiah's cornerstone oracle (laid in Zion as an unmovable foundation against the chaotic forces) is the background for Paul's claim that no other foundation can be laid than Christ. The Isaianic tested-cornerstone tradition (cited also in Rom 9:33 and 1 Pet 2:6) is applied to Christ as the one foundation whose placement by God is irrevocable."}
    ],
    "13": [
      {"type": "allusion", "target": "Mal 3:2-3", "note": "He is like a refiner's fire or a launderer's soap. He will sit as a refiner and purifier of silver; he will purify the Levites and refine them like gold and silver — Malachi's Day-of-the-Lord refining fire, which tests and purifies what is genuine while consuming what is not, is the OT background for Paul's metaphor of each builder's work being tested by fire on the Day. The fire is eschatological judgment that reveals quality, not merely destroys."}
    ],
    "16": [
      {"type": "allusion", "target": "Exod 25:8", "note": "Have them make a sanctuary for me, and I will dwell among them — the foundational promise of the tabernacle (and temple) is that YHWH's Spirit will dwell among his people in a sacred space. Paul applies this to the community: the church as YHWH's dwelling-place is the eschatological fulfillment of the Sinai tabernacle promise. Destroying the community is destroying the sacred space of the divine presence — with the same consequences as defiling the temple (3:17)."},
      {"type": "allusion", "target": "Ezek 37:27", "note": "My dwelling place will be with them; I will be their God, and they will be my people — Ezekiel's restoration promise that YHWH's sanctuary will be permanently among his people (37:27-28) is enacted in the Spirit-indwelt community. The eschatological temple of Ezekiel's vision is not a building but a people; Paul's claim that the Corinthians are God's temple fulfills this Ezekielian promise."}
    ],
    "19": [
      {"type": "quote", "target": "Job 5:13", "note": "He catches the wise in their craftiness, and the schemes of the wily are swept away — Paul cites Job 5:13 (Eliphaz's speech, ironically) to demonstrate that scripture itself condemns the self-sufficiency of human cleverness before God. The citation is the only direct quotation from Job in the NT; its use here is subtle — Eliphaz was wrong about Job but accidentally right about the general principle."}
    ],
    "20": [
      {"type": "quote", "target": "Ps 94:11", "note": "The LORD knows all human plans; he knows that they are futile — Paul cites Ps 94:11 to confirm that God's knowledge of human reasoning exposes its ultimate futility. In context Ps 94 is a psalm of divine justice against the wicked who think YHWH does not see; the LORD's omniscience here is not neutral observation but the judgment-revealing knowledge that unmasks the pretensions of human wisdom."}
    ]
  },
  "4": {
    "9": [
      {"type": "allusion", "target": "Isa 53:3", "note": "He was despised and rejected by mankind, a man of suffering, and familiar with pain. Like one from whom people hide their faces he was despised, and we held him in low esteem — Paul's description of apostles as the last in a procession, condemned, made a spectacle, is shaped by the Suffering Servant tradition. The apostolic experience of being put on display for death participates in the pattern of the one who was despised and rejected; the servant's vocation becomes the apostolic vocation."}
    ],
    "13": [
      {"type": "allusion", "target": "Lam 3:45", "note": "You have made us scum and refuse among the nations — Jeremiah's lament in Lamentations 3 over Israel's condition in the aftermath of Jerusalem's destruction uses the exact vocabulary Paul applies to the apostles: scum (perikatharmata) and refuse (peripsēma). The apostolic vocation recapitulates the condition of defeated Israel; the messengers of the crucified Messiah are, as expected, treated like the defeated people they represent."}
    ]
  }
}

def main():
    existing = load_echo('1corinthians')
    merge_echo(existing, ECHOES)
    save_echo('1corinthians', existing)
    total = sum(len(v) for v in existing.values())
    print(f'1 Corinthians echo: {len(existing)} chapters, {total} verses with connections.')

if __name__ == '__main__':
    main()
