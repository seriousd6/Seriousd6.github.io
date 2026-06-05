"""
Echo layer — 2 Corinthians all 13 chapters
Output: data/echoes/2corinthians.json

2 Corinthians is the most personally revealing of Paul's letters.
Key echo zones: the new exodus theology of ch3 (Exod 34; Jer 31),
the 'servant of the Lord' suffering pattern (Isa 53),
the new creation (Isa 65:17-25), and the triumphal procession (Isa 52:7-10).
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
    "20": [
      {"type": "fulfillment", "target": "Num 23:19", "note": "All God's promises find their Yes in Christ — God is not a man that he should lie; every promise made through the patriarchs and prophets is ratified in the 'Yes' of Christ's faithfulness, fulfilling what the prophets spoke and the Torah promised"}
    ]
  },
  "3": {
    "3": [
      {"type": "fulfillment", "target": "Jer 31:33", "note": "Written not with ink but with the Spirit of the living God, not on tablets of stone but on tablets of human hearts — Paul's new covenant ministry description fulfills Jeremiah's new covenant promise precisely: the law written on hearts rather than stone; the Spirit as the writing-agent replacing Moses's tablets"}
    ],
    "6": [
      {"type": "fulfillment", "target": "Jer 31:31-34", "note": "God has made us ministers of a new covenant (<em>kaines diathekes</em>) — the new covenant that Jeremiah promised, distinguished from the Mosaic covenant by its internality (heart-law), universality, and permanent forgiveness"},
      {"type": "allusion", "target": "Ezek 11:19", "note": "A new spirit I will put within them; I will remove the heart of stone and give them a heart of flesh — Ezekiel's new covenant promise of the Spirit transforming stony hearts into living hearts; Paul's 'tablets of human hearts' echoes Ezek 11:19/36:26"}
    ],
    "13": [
      {"type": "allusion", "target": "Exod 34:33-35", "note": "Moses put a veil over his face — Paul's midrash on the Sinai theophany: the veil Moses wore was to prevent Israel from seeing the fading of the Mosaic covenant's glory; the veil remains on Israel's mind when reading the old covenant, but is removed in Christ"}
    ],
    "18": [
      {"type": "fulfillment", "target": "Exod 34:29-35", "note": "Beholding the glory of the Lord, we are being transformed into the same image from one degree of glory to another — Moses's face shone with reflected glory after encountering YHWH; now believers behold Christ's glory with unveiled faces and are transformed progressively into that same glory; the Mosaic type fulfilled in Christian experience"}
    ]
  },
  "4": {
    "6": [
      {"type": "allusion", "target": "Gen 1:3", "note": "God who said Let light shine out of darkness has shone in our hearts — the creation-light of Gen 1:3 is the type; the new creation-light of the gospel in the face of Christ is the antitype; conversion is a new-creation event"},
      {"type": "allusion", "target": "Isa 9:2", "note": "The people walking in darkness have seen a great light — the Isaianic light-in-darkness oracle; Paul identifies the light of the gospel with the prophetic light that was to dawn in the messianic age"}
    ]
  },
  "5": {
    "17": [
      {"type": "fulfillment", "target": "Isa 65:17", "note": "If anyone is in Christ, he is a new creation; the old has passed away, the new has come — Paul's new creation language directly echoes Isa 65:17 (I am creating new heavens and a new earth; the former things shall not be remembered); the eschatological new creation promised by Isaiah is present already in union with Christ"}
    ],
    "21": [
      {"type": "fulfillment", "target": "Isa 53:6", "note": "For our sake he made him to be sin who knew no sin — the substitutionary exchange (sinless one made sin; sinners made righteous) fulfills the Servant logic of Isa 53:6 where YHWH 'laid on him the iniquity of us all'; the great exchange of 2 Cor 5:21 is Isa 53 compressed into a single sentence"}
    ]
  },
  "6": {
    "2": [
      {"type": "fulfillment", "target": "Isa 49:8", "note": "In a favorable time I listened to you and in a day of salvation I have helped you — Paul quotes Isa 49:8 (LXX) and applies it to the present moment of gospel proclamation: 'Behold, now is the favorable time; now is the day of salvation.' The Isaianic day of YHWH's rescue is declared to have arrived in the gospel age"}
    ],
    "16": [
      {"type": "fulfillment", "target": "Lev 26:11-12", "note": "I will live in them and walk among them, and I will be their God, and they shall be my people — Paul's catena of OT quotations on the temple-community: Lev 26:11-12 (YHWH dwelling with Israel) is the first; the promise of the Shekinah-presence with Israel is fulfilled in the community of believers as the Spirit's temple"},
      {"type": "fulfillment", "target": "Isa 52:11", "note": "Come out from their midst and be separate, says the Lord — the second catena quote: Isa 52:11's call for the priests carrying the temple vessels to be ritually pure on the new exodus from Babylon; Paul applies the call to separation from idolatry to the Christian community"}
    ]
  },
  "8": {
    "9": [
      {"type": "allusion", "target": "Isa 53:2-3", "note": "Though he was rich, yet for your sake he became poor — the self-emptying of the pre-existent Christ echoes the Servant who had no form or majesty (Isa 53:2); the poverty of incarnation and cross parallels the Servant's voluntary humiliation for others' benefit"}
    ]
  },
  "12": {
    "9": [
      {"type": "allusion", "target": "Isa 40:29-31", "note": "My power is made perfect in weakness — YHWH gives power to the faint and increases the strength of the weak; Paul's experience of Christ's power through weakness is the Isaianic pattern of divine strength in human insufficiency reaching its Christological application"}
    ]
  }
}

ECHOES_6_10 = {
  "6": {
    "2": [
      {"type": "allusion", "target": "Isa 61:2", "note": "The 'year of YHWH's favor' that the Servant proclaims (Isa 61:2, cited by Jesus in Luke 4:19) echoes behind Paul's 'time of favor' — the same eschatological window of divine acceptance is now declared open through the apostolic ministry"}
    ],
    "14": [
      {"type": "allusion", "target": "Deut 22:10", "note": "The prohibition against yoking an ox and donkey together is the background image for Paul's 'do not be yoked together with unbelievers' — mismatched yoking violates created distinctions. The Levitical principle extended to any incompatible pairing"},
      {"type": "allusion", "target": "Lev 19:19", "note": "The broader principle behind Deut 22:10 — no mixing of incompatible kinds (mixed livestock, seed, fabric). Paul's catena on incompatible partnerships draws on the Levitical order-theology where categories must be kept distinct; the holiness code's separation logic applies to the covenant community's associations"}
    ],
    "16": [
      {"type": "fulfillment", "target": "Ezek 37:27", "note": "Ezekiel's vision of restored Israel includes 'my dwelling place will be with them; I will be their God, and they will be my people.' Paul's single quotation conflates Lev 26 and Ezek 37, indicating he is citing a known compound formula rather than a single text; both strands converge on the community as the new temple"}
    ],
    "17": [
      {"type": "quote", "target": "Isa 52:11", "note": "Direct quote of the call to the exilic community departing Babylon: 'Come out from them and be separate, says the Lord; touch no unclean thing, and I will receive you.' The departure-from-Babylon text becomes Paul's call to separate from idolatry — the community's separation from the world's patterns recapitulates Israel's exodus from Babylon"},
      {"type": "allusion", "target": "Ezek 20:34", "note": "YHWH's promise to gather Israel 'out from the peoples' (Ezek 20:34, 41) forms part of the same exodus-from-paganism theme — the new covenant community's separation from idolatry recapitulates the Ezekielian promise of re-gathering"}
    ],
    "18": [
      {"type": "quote", "target": "2 Sam 7:14", "note": "The Davidic covenant promise — 'I will be a father to you, and you will be my son' — is expanded by Paul to 'sons and daughters,' applying the royal-adoption language to the entire covenant community. What was the Davidic king's status becomes the status of all who are in Christ"},
      {"type": "allusion", "target": "Jer 31:9", "note": "The new covenant context of Jer 31 includes 'I am a father to Israel' — Paul's catena closes with the sonship language of Jer 31 (the very passage whose 'new covenant' language shapes 2 Cor 3), closing the literary bracket on the OT quotation chain with a direct new-covenant echo"}
    ]
  },
  "7": {
    "1": [
      {"type": "allusion", "target": "Lev 11:44", "note": "The call to 'cleanse ourselves from every defilement of body and spirit' is grounded in the Levitical holiness command — 'be holy, because I am holy' (Lev 11:44; 19:2). Since Paul has just declared the community to be the temple of the living God (6:16), the temple-purity logic of Leviticus now applies: the dwelling place of the Holy One must be kept clean"},
      {"type": "allusion", "target": "Isa 52:11", "note": "Immediately following the 'touch no unclean thing' quote (6:17), Paul's call to cleanse body and spirit carries forward the same Isa 52:11 logic — the departure from Babylon required ritual purification; the new-covenant community's holiness requires active purification, not merely position"}
    ],
    "6": [
      {"type": "allusion", "target": "Isa 49:13", "note": "Paul's 'God who comforts those who are downcast' (ho parakalon tous tapeinous) alludes to Isa 49:13 — 'YHWH has comforted his people and will have compassion on his afflicted ones (tapeinois autou).' The LXX tapeinois matches Paul's tapeinous precisely, identifying God's action through Titus as continuous with the Servant-Song pattern of divine comfort"},
      {"type": "allusion", "target": "Isa 40:1", "note": "The great comfort-oracle of Second Isaiah — 'Comfort, comfort my people, says your God' — stands behind Paul's consolation theology throughout 2 Corinthians (1:3-4 develops it explicitly). Titus arriving with good news is an instance of the Isaian pattern: YHWH's comfort mediated through human messengers to a downcast people"}
    ]
  },
  "8": {
    "9": [
      {"type": "allusion", "target": "Isa 53:12", "note": "Paul's Christological statement — 'through his poverty you might become rich' — echoes the Servant of Isa 53:12 who 'poured out his soul to death.' The exchange pattern (his poverty → our riches) mirrors Isaiah's penal-substitution logic: the Servant's voluntary impoverishment that brings life to many is the structural model for the kenosis Paul describes"}
    ],
    "15": [
      {"type": "quote", "target": "Exod 16:18", "note": "Paul cites the manna-distribution principle verbatim: 'Whoever gathered much had nothing left over, and whoever gathered little had no lack.' The wilderness economy — where YHWH's provision equalised despite varying effort — becomes the model for economic sharing in the collection: the community should practice the eschatological equality the manna prefigured"},
      {"type": "allusion", "target": "Exod 16:4", "note": "The daily-enough provision of manna establishes the principle of sufficiency-not-excess that Paul applies to the collection. The manna narrative tests whether Israel will trust YHWH's daily provision rather than hoard; Paul applies the same test-of-trust logic to the Corinthians' giving"}
    ]
  },
  "9": {
    "6": [
      {"type": "allusion", "target": "Prov 11:24-25", "note": "The sowing/reaping principle draws on Prov 11:24 — 'one gives freely and grows all the richer; another withholds what he should give and only suffers want.' Paul converts the Wisdom observation into an agricultural metaphor, but the underlying principle of counter-intuitive generosity producing increase is identical"},
      {"type": "allusion", "target": "Prov 22:9", "note": "Prov 22:9 — 'Whoever has a bountiful eye will be blessed, for he shares his bread with the poor' — provides a second Proverbs strand for Paul's generosity theology. The 'bountiful eye' (MT: tov ayin) is the antonym of the 'evil eye' of greed; Paul's call to sow bountifully reflects this Wisdom tradition on the generous eye"}
    ],
    "7": [
      {"type": "allusion", "target": "Prov 22:8", "note": "Paul's 'God loves a cheerful giver' (hilaron agapa ho theos) appears to draw on the LXX plus tradition of Prov 22:8, which adds 'God blesses a cheerful and generous man' — a line present in some LXX manuscripts but not the Hebrew MT. Paul's citation reproduces language that circulated in the Greek wisdom tradition attributed to the Proverbs collection"},
      {"type": "allusion", "target": "Exod 25:2", "note": "The freewill-offering principle — 'every man who gives it willingly with his heart' — establishes the non-compulsion standard Paul invokes: giving 'not reluctantly or under compulsion.' The tabernacle collection was paradigmatically voluntary; the Jerusalem collection self-consciously echoes that pattern"}
    ],
    "9": [
      {"type": "quote", "target": "Ps 112:9", "note": "Paul quotes Ps 112:9 verbatim: 'He has scattered, he has given to the poor; his righteousness endures forever.' Ps 112 is the portrait of the blessed man whose generosity and righteousness are permanent; Paul applies the Psalm's description of the generous believer to the pattern of giving he urges, making the collection an enactment of the Psalm's ideal"},
      {"type": "allusion", "target": "Ps 111:3", "note": "Ps 112:9 echoes Ps 111:3 — 'his righteousness endures forever' — where the same phrase describes YHWH himself. Psalms 111-112 form a pair: YHWH's righteousness is mirrored in the righteous person's righteousness. Paul's citation places the generous giver in this mirror-image relationship with the divine character"}
    ],
    "10": [
      {"type": "allusion", "target": "Isa 55:10", "note": "Paul's 'He who supplies seed to the sower and bread for food' directly echoes Isa 55:10 — 'as rain and snow come down from heaven... giving seed to the sower and bread to the eater, so shall my word be.' The Isaian context is YHWH's promise that his word accomplishes its purpose; Paul applies the same agricultural-provision image to God's supply for the generous giver"},
      {"type": "allusion", "target": "Hos 10:12", "note": "Hosea's call to 'sow righteousness for yourselves; reap steadfast love' (Hos 10:12) is a strand behind Paul's sowing/reaping language. The agricultural metaphor for covenant faithfulness producing a harvest of hesed is part of the prophetic tradition Paul invokes when he says God will 'increase the harvest of your righteousness'"}
    ]
  },
  "10": {
    "1": [
      {"type": "allusion", "target": "Zech 9:9", "note": "Paul's appeal by 'the meekness and gentleness of Christ' echoes the messianic king of Zech 9:9 — 'your king comes to you, righteous and having salvation, humble (MT: ani; LXX: praüs = meek).' The meekness Paul attributes to Christ as character is grounded in the prophetic portrait of the gentle, counter-imperial king; his appeal by this meekness positions the apostle in the pattern of his Lord"},
      {"type": "allusion", "target": "Ps 45:4", "note": "The royal psalm's 'in your majesty ride out victoriously in the cause of truth, humility (anavah), and righteousness' connects meekness and kingship with righteous authority. Paul's appeal 'by the meekness of Christ' draws on this tradition that royal authority and gentleness are combined in the ideal king"}
    ],
    "4": [
      {"type": "allusion", "target": "Isa 59:17", "note": "Isaiah's warrior-YHWH 'put on righteousness as a breastplate and a helmet of salvation on his head' (Isa 59:17) is the primary OT source for Paul's weapons/armor language (developed fully in Eph 6:10-17). The divine warrior who dons armor to defeat injustice when no human champion can be found is the model for apostolic spiritual warfare — the weapons have divine power because they are YHWH's own armament"},
      {"type": "allusion", "target": "Isa 49:2", "note": "The Servant declares 'he made my mouth like a sharpened sword, he hid me in the shadow of his hand' — the sword-in-the-mouth as a weapon of the Servant's mission. Paul's weapons that demolish strongholds are the apostolic word, linking his ministry to the Servant's mouth-as-sword"}
    ],
    "5": [
      {"type": "allusion", "target": "Jer 1:10", "note": "Jeremiah was appointed 'to demolish and to uproot, to destroy and to overthrow, to build and to plant' — prophetic commission including both destructive and constructive elements. Paul's 'demolishing arguments and every pretension' echoes Jeremiah's commission; Paul sees his apostolic authority in continuity with the prophetic office of demolishing false structures to make way for truth"},
      {"type": "allusion", "target": "Dan 2:44", "note": "Daniel's stone that 'demolishes' all human kingdoms, filling the whole earth — the eschatological demolition of proud strongholds opposing God's kingdom — provides the apocalyptic frame for Paul's 'demolish every pretension that sets itself up against the knowledge of God.' The divine demolition of proud empires recapitulates in the apostolic ministry"}
    ],
    "17": [
      {"type": "quote", "target": "Jer 9:24", "note": "Paul quotes Jer 9:24 (as in 1 Cor 1:31): 'Let the one who boasts boast in the Lord.' Jeremiah's context: YHWH declares that wisdom, strength, and riches are false grounds for boasting — the only worthy boast is knowing YHWH who practices steadfast love, justice, and righteousness. Paul deploys this against the super-apostles' credentials: all their human commendation collapses before this prophetic standard"},
      {"type": "allusion", "target": "Jer 9:23", "note": "The verse preceding Paul's quote — 'let not the wise man boast in his wisdom, the mighty man in his might, or the rich man in his riches' — is the negative counterpart to v24. Paul's dispute with apostles who boast in letters, commendations, and rhetorical eloquence (10:12) is a direct enactment of the Jeremiah passage: all their boasting falls into YHWH's prohibited categories"}
    ]
  }
}

def main():
    existing = load_echo('2corinthians')
    merge_echo(existing, ECHOES)
    merge_echo(existing, ECHOES_6_10)
    save_echo('2corinthians', existing)
    total = sum(len(v) for v in existing.values())
    print(f'2 Corinthians echo: {len(existing)} chapters, {total} verses with connections.')

if __name__ == '__main__':
    main()
