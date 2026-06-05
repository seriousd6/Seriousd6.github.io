"""
MKT Echo Layer — Ephesians chapters 1–4
Run: python3 scripts/zc-echo-ephesians-1-4.py

Source data used:
- data/interlinear/ephesians.json
- data/translation/draft/mediating/ephesians.json (MKT text)
- data/parallels/ephesians.json (absorbed: 4:8 → Ps 68:18; 4:26 → Ps 4:4)

Key decisions in this range:
- Ps 110:1 at 1:20 classified type (not fulfillment): Paul applies it typologically
  in a doxological context, not in the direct citation form found in Heb 1:13.
- Ps 8:6 at 1:22 classified fulfillment: Paul applies the Psalm explicitly to Christ
  (same explicit move in 1 Cor 15:27), reading the "son of man" as the Son of Man.
- Isa 57:19 at 2:14/2:17 classified allusion: Paul echoes the language without a
  citation formula; the verbal overlap (near/far, peace) is deliberate.
- Isa 28:16 at 2:20 classified allusion; Ps 118:22 classified type — NT authors
  explicitly present Christ as the stone the builders rejected (Matt 21:42; 1 Pet 2:6-8),
  which qualifies as type though Paul himself does not cite either Psalm here.
- Gen 12:3 at 3:6 classified fulfillment: Paul presents the Gentile inclusion as the
  promised blessing of Abraham arriving (Gal 3:8 makes the fulfillment logic explicit).
- Deut 6:4 at 4:4-6 classified theme: Paul does not quote the Shema but structures the
  seven-fold unity formula on the same monotheistic logic. The connection is conceptual.
- Parallels absorbed: 4:8 (Ps 68:18, prophecy-source → quote with note added);
  4:26 (Ps 4:4, quotation → quote with note added).
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


EPHESIANS_ECHOES = {
  "1": {
    "4": [
      {
        "type": "type",
        "target": "Deut 7:6",
        "note": "Israel's election as a holy people — chosen out of all peoples, set apart, to be holy — is the structural antecedent to Paul's claim that believers were chosen in Christ before the foundation of the world. The divine pattern of election-unto-holiness transfers from the national to the eschatological people of God."
      },
      {
        "type": "allusion",
        "target": "Isa 43:10",
        "note": "God's address to Israel — 'you are my witnesses, my chosen servant' — carries the same combination of election and holy purpose; Paul universalises this calling in Christ, who is the chosen Servant par excellence and in whom all are now chosen."
      }
    ],
    "5": [
      {
        "type": "type",
        "target": "Exod 4:22",
        "note": "Israel's designation as God's firstborn son (Exod 4:22) established adoption language for the covenant people; Paul uses the same adoption frame (huiothesia) but grounds it in Christ, the Son, through whom all who are in him receive the status Israel bore by covenant. The type moves from national to personal and eschatological."
      },
      {
        "type": "allusion",
        "target": "Hos 11:1",
        "note": "Hosea's 'out of Egypt I called my son' pictures divine adoption as the origin of the covenant relationship; Paul's predestination-to-adoption language draws on this prior Sonship vocabulary, which Matthew later applies directly to Jesus (Matt 2:15) as the true Son Israel failed to be."
      }
    ],
    "7": [
      {
        "type": "type",
        "target": "Exod 6:6",
        "note": "God's promise to redeem Israel from Egypt with an outstretched arm (ga'al / lutrōsis) is the foundational OT type of redemption; Paul uses the same redemption vocabulary (apolytrōsis) but locates its fulfilment in Christ's blood, presenting the cross as the definitive exodus the Sinai deliverance foreshadowed."
      },
      {
        "type": "shadow",
        "target": "Lev 17:11",
        "note": "The Levitical principle that life is in the blood, and that blood makes atonement, undergirds Paul's phrase 'redemption through his blood' — the Mosaic sacrificial system embedded in Israel's worship the logic that redemption costs life, a cost the blood of Christ finally bears without repetition."
      }
    ],
    "10": [
      {
        "type": "shadow",
        "target": "Isa 9:6",
        "note": "The Isaianic vision of a prince of endless peace whose dominion grows without end — gathering all authority under the governance of a Davidic figure — provides the prophetic vocabulary for Paul's anakephalaiōsasthai, the summing-up of all things in Christ when the fullness of times arrives."
      },
      {
        "type": "theme",
        "target": "Isa 11:9",
        "note": "The vision of a renewed creation where nothing is left outside God's harmonious order ('the earth will be full of the knowledge of the LORD') supplies the cosmic scope Paul has in mind when he speaks of 'all things in heaven and on earth' being united under one head."
      }
    ],
    "13": [
      {
        "type": "fulfillment",
        "target": "Ezek 36:27",
        "note": "Ezekiel's new-covenant promise — 'I will put my Spirit within you' — finds its NT fulfilment in Paul's description of the Holy Spirit as the seal of those who believe; the Spirit given at Pentecost is the promised indwelling that Ezekiel set in the future as the mark of the restored people of God."
      },
      {
        "type": "allusion",
        "target": "Ezek 9:4",
        "note": "The sealing of the faithful in Jerusalem before judgment (Ezek 9:4) is an OT prototype of protective divine marking; Paul's sealing language for the believer draws on this image of God distinguishing and protecting his own, now realised through the indwelling Spirit."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "Ps 16:5",
        "note": "The Psalmist's confession that the LORD is his portion and inheritance (chelqi / klēronomiā) is echoed in Paul's 'riches of his glorious inheritance in the saints' — the individual certainty of the Psalm becomes the corporate inheritance of the new covenant people, and its fullness is found in Christ."
      }
    ],
    "20": [
      {
        "type": "type",
        "target": "Ps 110:1",
        "note": "The royal oracle — 'Sit at my right hand until I make your enemies a footstool' — is the OT's most-cited messianic text; Paul applies it to Christ's post-resurrection exaltation, presenting the seating at God's right hand as the fulfilment of the Davidic enthronement that Psalm 110 anticipates."
      }
    ],
    "22": [
      {
        "type": "fulfillment",
        "target": "Ps 8:6",
        "note": "The Psalm's declaration that God 'put everything under his feet' — referring to the Adamic dominion over creation — is explicitly applied to Christ in 1 Cor 15:27; Paul's use here does the same: Christ is the Son of Man who receives the universal dominion Adam forfeited, and the church as his body participates in that headship."
      }
    ]
  },
  "2": {
    "1": [
      {
        "type": "allusion",
        "target": "Ezek 37:3",
        "note": "The valley of dry bones — dead Israel waiting for the breath of God to give life — is the prophetic background for Paul's 'dead in your trespasses and sins'; Ezekiel's vision of national spiritual death and divine resurrection becomes in Paul the diagnosis and cure of every individual before God's quickening grace."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "Exod 34:6",
        "note": "The self-disclosure of God to Moses — 'abounding in steadfast love (hesed) and faithfulness' — is the foundational OT characterisation of God's mercy; Paul's 'rich in mercy' (ploúsios en elei) intentionally echoes this defining attribute, presenting the gospel as the demonstration of the character God revealed at Sinai."
      },
      {
        "type": "theme",
        "target": "Ps 86:15",
        "note": "The Psalm restates the Sinai self-disclosure: 'you, Lord, are full of compassion and gracious, slow to anger, abounding in love and faithfulness'; Paul's description of God as 'rich in mercy' in the context of rescuing the dead belongs to this sustained OT witness that divine abundance expresses itself in saving mercy."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "Gen 17:4",
        "note": "The Abrahamic covenant promised that Gentile nations would share in blessing through Abraham's offspring; Paul's description of Gentiles as formerly 'excluded from the covenants of the promise' names the Abrahamic, Mosaic, and Davidic covenants as the heritage from which they were estranged — a status that 2:13 then declares overcome in Christ."
      },
      {
        "type": "allusion",
        "target": "Jer 31:31",
        "note": "Jeremiah's new covenant, made with both Israel and Judah, does not explicitly include Gentiles — which is part of what made the Gentile inclusion a 'mystery'; Paul implies that the Gentiles' former exclusion from covenant promise is now resolved precisely because the new covenant is inaugurated in Christ's blood (Luke 22:20)."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Isa 57:19",
        "note": "Isaiah's oracle — 'Peace, peace to the far and to the near' — speaks of God healing those who were estranged from him; Paul identifies Christ himself as that peace, using the near/far polarity Isaiah employed to describe the reconciliation of Gentile (far) and Jew (near) through the cross."
      }
    ],
    "17": [
      {
        "type": "quote",
        "target": "Isa 57:19",
        "note": "Paul quotes or closely alludes to Isa 57:19 ('peace to the far and peace to the near') in describing Christ's proclamation — the same verse he drew on in 2:14. The verbal parallel (far/near, peace/eirēnē) is close enough to be deliberate, and it presents the incarnate Christ as the fulfilment of the peace God promised to the estranged."
      },
      {
        "type": "allusion",
        "target": "Isa 52:7",
        "note": "The herald whose feet are beautiful, who announces peace and brings good news (euangelizomenos eirēnēn) — Paul applies this same evangelistic vocabulary to Christ personally; the messenger who announces salvation is now identified with the salvation he announces."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Isa 28:16",
        "note": "God's promise to lay a tested, precious cornerstone in Zion — a foundation stone that will not make its trusters ashamed — is the prophetic text behind Paul's description of Christ as the chief cornerstone (akrogōniaios); the church built on apostles and prophets with Christ as cornerstone is the fulfilment of the Zion-foundation oracle."
      },
      {
        "type": "type",
        "target": "Ps 118:22",
        "note": "The rejected stone that becomes the chief cornerstone — cited by Jesus himself as a type of his rejection and vindication (Matt 21:42) and by Peter as explicitly fulfilled in Christ (1 Pet 2:7) — underlies Paul's use of cornerstone language; the stone the builders rejected is now the cornerstone of the new temple, the church."
      }
    ],
    "21": [
      {
        "type": "shadow",
        "target": "1 Kgs 6:14",
        "note": "Solomon's temple — God's dwelling among his people, the culmination of the Tabernacle trajectory — is the OT shadow that Paul's 'holy temple in the Lord' resolves; the church as living temple (a building of persons, not stones) is the fulfilment of the divine dwelling that the Solomonic structure anticipated and that Ezekiel projected into the future (Ezek 40-48)."
      }
    ]
  },
  "3": {
    "5": [
      {
        "type": "allusion",
        "target": "Dan 2:28",
        "note": "In Daniel, God 'reveals mysteries' (Aramaic: rāz) to Nebuchadnezzar through his prophet, demonstrating that divine purposes hidden to human wisdom are disclosed to God's servants; Paul uses the same 'mystery-now-revealed' structure, but the revelation belongs to the era of the Spirit and fulfils the trajectory Daniel opened."
      },
      {
        "type": "allusion",
        "target": "Amos 3:7",
        "note": "Amos declared that 'the Sovereign LORD does nothing without revealing his plan to his servants the prophets'; Paul's claim that the mystery is now revealed to God's holy apostles and prophets operates within this prophetic framework — but the scale of what is revealed (Gentile co-inclusion) exceeds anything the OT prophets disclosed in full."
      }
    ],
    "6": [
      {
        "type": "fulfillment",
        "target": "Gen 12:3",
        "note": "The Abrahamic promise that all nations would be blessed through his offspring (explicitly developed in Gen 18:18; 22:18) finds its fulfilment in Paul's declaration that the Gentiles are co-heirs and co-members in the one body through the gospel; Paul's argument in Gal 3:8 makes this connection explicit, reading Gen 12:3 as the gospel announced in advance."
      },
      {
        "type": "fulfillment",
        "target": "Isa 49:6",
        "note": "The Servant's commission to be 'a light for the Gentiles, that my salvation may reach to the ends of the earth' supplies the prophetic basis for Paul's own commission to preach to the Gentiles; the mystery Paul administers (3:1-9) is the actualization of Isaiah's Servant mission in the church's universal proclamation."
      }
    ],
    "10": [
      {
        "type": "theme",
        "target": "Prov 8:22",
        "note": "Proverbs' depiction of divine Wisdom as God's companion in creation, present before the world was made, shapes Paul's language about the 'manifold wisdom of God' now being displayed through the church — the multi-faceted wisdom that ordered creation is the same wisdom that planned and now executes the reconciliation of all things in Christ."
      }
    ],
    "15": [
      {
        "type": "theme",
        "target": "Gen 5:2",
        "note": "God's naming of Adam — and through Adam the naming/calling of every human family — provides the background for Paul's statement that every family in heaven and earth derives its name from the Father; divine fatherhood and the naming of families traces back to the creation narrative, which Paul presents as finding its ultimate reference in the Father revealed in Christ."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "Ps 1:3",
        "note": "The blessed man who is 'like a tree planted by streams of water' — rooted, fruitful, and stable — supplies the imagery Paul uses for believers being 'rooted and established in love'; the Psalm's metaphor of stability through groundedness in Torah becomes in Paul a stability through groundedness in Christ's love."
      },
      {
        "type": "allusion",
        "target": "Jer 17:7",
        "note": "Jeremiah's image of the one who trusts in the LORD as a tree with roots reaching to the stream — flourishing even in drought — parallels Paul's 'rooted and grounded'; both use botanical rootedness to describe the stability that comes from being anchored in divine relationship rather than in human resources."
      }
    ]
  },
  "4": {
    "4": [
      {
        "type": "theme",
        "target": "Deut 6:4",
        "note": "The Shema — 'Hear, O Israel: The LORD our God, the LORD is one' — is the monotheistic bedrock of Jewish identity; Paul's seven-fold unity formula ('one body, one Spirit, one hope, one Lord, one faith, one baptism, one God and Father') is structured on the same unity-logic, extending the Shema's monotheism into a Trinitarian framework without abandoning its confession."
      }
    ],
    "8": [
      {
        "type": "quote",
        "target": "Ps 68:18",
        "note": "Paul cites Ps 68:18 directly ('When he ascended on high, he led captives in his train and gave gifts to his people'), a psalm of divine warrior triumph likely associated with the ark procession or Davidic conquest; Paul applies the ascent to Christ's resurrection/ascension and reinterprets 'receiving gifts' as 'giving gifts' — possibly reading a Targum tradition or applying the logic that what the conquering king receives is distributed to his people."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Ps 139:8",
        "note": "The Psalmist's recognition that God is present both in the heights of heaven and in the depths of Sheol frames Paul's interpretation of Ps 68:18 — the Christ who ascended must also have descended, filling the full vertical range of existence that the Psalm maps as God's domain; Christ's descent-and-ascent enacts what the Psalm says only God can span."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "Jer 2:5",
        "note": "Jeremiah's indictment of Israel for 'walking after emptiness and becoming empty' (hebel, vanity) — the same futility that idol worship produces — is echoed in Paul's description of Gentile existence as 'the vanity of their minds' (mataiótēs); both diagnose a blindness that comes from being cut off from the living God."
      },
      {
        "type": "allusion",
        "target": "Isa 44:18",
        "note": "Isaiah's portrait of the idol-worshipper as one whose 'eyes are plastered over' so he cannot see — with a 'deluded heart' that leads him astray — is the OT background for Paul's 'darkened in their understanding' and 'ignorance'; Paul presents Gentile spiritual blindness as a form of the idolatry Isaiah exposed."
      }
    ],
    "24": [
      {
        "type": "fulfillment",
        "target": "Gen 1:26",
        "note": "The image of God (tselem elohim) in which Adam was created — the original righteousness and holiness that humanity bore before the fall — is precisely what Paul says the new self is 'created to be like'; the new creation in Christ is not a novel category but the restoration of what humanity was made to be at the beginning."
      }
    ],
    "25": [
      {
        "type": "quote",
        "target": "Zech 8:16",
        "note": "Paul's 'put off falsehood and speak truth to your neighbor' closely echoes Zech 8:16 ('speak the truth to each other'), Zechariah's instruction for the renewed community; Paul draws on this text as the community ethics of the new-covenant assembly, replacing the old man's patterns with prophetic norms for the restored people."
      }
    ],
    "26": [
      {
        "type": "quote",
        "target": "Ps 4:4",
        "note": "Paul directly cites or echoes Ps 4:4 ('In your anger do not sin; when you are on your beds, search your hearts and be silent'); the Psalm's counsel to let righteous anger rest without spiraling into sin becomes Paul's instruction for community conflict — anger that does not find resolution before nightfall gives ground to the devil."
      }
    ],
    "30": [
      {
        "type": "allusion",
        "target": "Isa 63:10",
        "note": "Isaiah describes Israel's wilderness rebellion as grieving God's Holy Spirit — 'they rebelled and grieved his Holy Spirit, so he turned and became their enemy'; Paul issues the same warning to believers, applying Isa 63:10 directly: the Spirit who seals and indwells can be grieved by the very behaviours Paul is cataloguing (anger, falsehood, corrupt speech)."
      }
    ]
  }
}


def main():
    existing = load_echo('ephesians')
    merge_echo(existing, EPHESIANS_ECHOES)
    save_echo('ephesians', existing)
    print('Ephesians 1–4 echoes written.')

if __name__ == '__main__':
    main()
