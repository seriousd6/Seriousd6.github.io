"""
MKT Echo Layer — Galatians chapters 4–6
Run: python3 scripts/zc-echo-galatians-4-6.py

Source data used:
- data/interlinear/galatians.json
- data/parallels/galatians.json (absorbed — all ch 4–5 entries)
- data/translation/draft/mediating/galatians.json (MKT text)

Key decisions in this range:
- Parallels absorbed: 4:4 Gen 3:15 → type; 4:21 Gen 21:1-21 → allusion (placed at 4:22
  where Paul introduces the two sons, and 4:24 for the covenant framing); 4:27 Isa 54:1
  → fulfillment (Paul introduces it with "it is written" as Scripture-claim); 4:30 Gen
  21:10 → quote; 5:14 Lev 19:18 → quote.
- Isa 54:1 classified fulfillment: Paul frames this as Scripture speaking to the present
  reality of the Gentile mission ("she who was desolate has more children than she who
  has a husband"), not merely prophetic anticipation.
- 4:4 also carries allusion to Isa 7:14 (Emmanuel born of a woman in the fullness of
  time), though Paul's primary point is subordination to the law, not virginal conception.
- 5:16/5:25 echoes of Ezek 36:27 and 37:14 classified as shadow: the new covenant
  Spirit-in-you theme is background architecture, not verbal quotation.
- 6:15 "new creation" classified allusion to Isa 65:17: Paul's kainē ktisis draws on
  prophetic new-creation vocabulary even without explicit citation.
- Galatians 6 has few OT quotations; echoes are mostly theme/shadow/allusion to
  Wisdom tradition (sowing/reaping) and prophetic promises.
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


GALATIANS_ECHOES = {
  "4": {
    "4": [
      {
        "type": "type",
        "target": "Gen 3:15",
        "note": "The proto-evangelion's promised seed of the woman arrives precisely in the fullness of time; Christ's birth 'of a woman' enacts the reversal of Eden's curse, born under the very law that condemns humanity in order to bear that condemnation."
      },
      {
        "type": "allusion",
        "target": "Isa 7:14",
        "note": "The Emmanuel sign — a child born of a woman as the definitive divine intervention at the appointed moment — provides background register for Paul's 'sent his Son, born of a woman' even though Paul's accent falls on subordination to law rather than virginal conception."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Exod 4:22",
        "note": "God declares Israel his firstborn son at the Exodus; Paul's huiothesia (adoption to sonship) draws on this corporate-sonship tradition, now extended through Christ to Gentiles who receive the full standing Israel was called to embody."
      },
      {
        "type": "shadow",
        "target": "Hos 11:1",
        "note": "Hosea's 'out of Egypt I called my son' established Israel's identity as the son God redeemed; redemption of those under the law that we might receive adoption recapitulates and universalizes this son-calling pattern through the one true Son."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Isa 63:16",
        "note": "Isaiah's prayer 'you are our Father, our Redeemer from of old' establishes the 'Abba, Father' address as covenantal petition, not merely familial warmth; Paul's use of the Aramaic 'Abba' in a Greek letter signals a liturgical cry rooted in Israel's relationship with the God who redeems."
      },
      {
        "type": "allusion",
        "target": "Ps 2:7",
        "note": "The royal decree 'you are my Son' is the paradigm for the divine father–son bond; the Spirit's cry of 'Abba' in believers' hearts enacts their participation in the Sonship the Psalm ascribes to the anointed king."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Jer 2:11",
        "note": "Jeremiah's indictment — 'my people have exchanged their glorious God for worthless idols' — frames Paul's account of the Galatians' pre-conversion service to 'those who by nature are not gods'; both texts locate idolatry as the defining feature of life outside covenant knowledge."
      }
    ],
    "22": [
      {
        "type": "allusion",
        "target": "Gen 16:15",
        "note": "The birth of Ishmael to Hagar establishes the 'slave woman's son born according to the flesh' that Paul's allegory requires; the Genesis narrative itself presents this birth as the human attempt to secure the promise by natural means rather than waiting for divine provision."
      },
      {
        "type": "allusion",
        "target": "Gen 21:2",
        "note": "Isaac's birth 'at the time God had promised' is the pivot of the Sarah narrative — born not by ordinary human agency but by divine faithfulness to an impossible promise; Paul's contrast between 'born of the flesh' and 'born through promise' maps directly onto this distinction."
      }
    ],
    "24": [
      {
        "type": "allusion",
        "target": "Exod 19:1",
        "note": "The Sinai covenant, ratified in fire and fear at the mountain, is the covenant of bondage in Paul's allegory; Hagar's association with 'Mount Sinai in Arabia' identifies the law-covenant with the very geography of slavery and terror rather than inheritance and promise."
      },
      {
        "type": "allusion",
        "target": "Gen 21:9",
        "note": "Paul's 'two covenants' allegory depends on the Genesis narrative as its load-bearing structure; the allegorization is not arbitrary — it draws on the typological potential the Genesis narrative itself establishes by contrasting two mothers, two births, and two destinies."
      }
    ],
    "25": [
      {
        "type": "allusion",
        "target": "Isa 52:1",
        "note": "Isaiah's call to 'wake up, wake up, put on your strength, O Zion' addresses Jerusalem in captivity; Paul identifies 'the present city of Jerusalem' as remaining in that captivity, awaiting the liberation that the Jerusalem above already enjoys — the eschatological reversal Isaiah announces."
      }
    ],
    "26": [
      {
        "type": "shadow",
        "target": "Isa 54:11",
        "note": "The heavenly Jerusalem 'which is free and is our mother' draws on Isaiah's vision of Zion rebuilt with precious stones and her children taught by the LORD; Paul's 'Jerusalem above' is the eschatological city Isaiah projects, present now as the community of those born of promise."
      }
    ],
    "27": [
      {
        "type": "fulfillment",
        "target": "Isa 54:1",
        "note": "Paul cites this explicitly as Scripture ('it is written'), claiming Isaiah's promise to barren Zion is fulfilled in the explosive growth of the Gentile mission; the desolate woman (Sarah, or Zion abandoned during exile) now has more children than the woman with a husband — the law-observant community that expected to be the sole heir."
      }
    ],
    "28": [
      {
        "type": "allusion",
        "target": "Gen 18:10",
        "note": "The divine promise 'I will surely return to you, and Sarah your wife will have a son' is the original word of promise that makes Isaac possible; Paul's 'children of promise, like Isaac' reaches back to this specific divine speech-act as the prototype of all promise-births."
      }
    ],
    "29": [
      {
        "type": "allusion",
        "target": "Gen 21:9",
        "note": "The Genesis text describes Ishmael 'mocking' (LXX: paizonta) at Isaac's weaning feast; Jewish interpretive tradition, including Philo, amplified this as outright persecution — and Paul reads it as a structural pattern still operative: those born of the flesh oppose those born of the Spirit."
      }
    ],
    "30": [
      {
        "type": "quote",
        "target": "Gen 21:10",
        "note": "Paul quotes Sarah's demand to Abraham verbatim as a word of Scripture that settles the question: the slave woman's son has no share in the inheritance alongside the free woman's son — the Genesis narrative itself excludes the Hagar-covenant from the eschatological inheritance."
      }
    ]
  },
  "5": {
    "1": [
      {
        "type": "allusion",
        "target": "Isa 61:1",
        "note": "The Servant's commission 'to proclaim freedom for the captives' is the prophetic backdrop for Christ's liberating work; Paul's 'it is for freedom that Christ has set us free' activates this register, identifying Jesus as the Servant whose announcement of release is now accomplished reality."
      },
      {
        "type": "shadow",
        "target": "Lev 25:10",
        "note": "The Year of Jubilee proclaimed liberty throughout the land and required the return of all who had sold themselves into bondage; as a structural shadow it anticipates the eschatological liberty Christ announces — freedom not merely from economic servitude but from the bondage of the law-covenant itself."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "Deut 27:26",
        "note": "Already quoted at Gal 3:10, the curse on everyone who does not uphold the entire law resurfaces here: Paul's warning that circumcision makes one 'obligated to obey the whole law' is the direct application of Deuteronomy's totality-clause — entry into the law-system means accepting its complete terms, including its curse."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Hab 2:4",
        "note": "The foundational text for Paul's gospel in Galatians — 'the righteous shall live by faith' (cited at Gal 3:11) — underlies 5:5 as well; eagerly awaiting righteousness 'by faith through the Spirit' is the lived practice of Habakkuk's principle, now empowered by the Spirit promised to those who believe."
      }
    ],
    "9": [
      {
        "type": "shadow",
        "target": "Exod 12:15",
        "note": "The Passover regulation requiring the removal of all leaven from the household made leaven the dominant metaphor for corrupting influence in Jewish moral tradition; Paul's proverbial 'a little yeast works through the whole batch' (also 1 Cor 5:6) draws on this cultural weight — false teaching, like leaven, cannot be contained."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Isa 8:14",
        "note": "Isaiah's 'stone that causes people to stumble and a rock that makes them fall' (also cited in Rom 9:33; 1 Pet 2:8) is the OT basis for the 'offense of the cross'; the cross functions as the skandalon Isaiah predicted — a divine provision that becomes a sticking point for those expecting a different kind of deliverance."
      }
    ],
    "14": [
      {
        "type": "quote",
        "target": "Lev 19:18",
        "note": "Paul quotes the Holiness Code's summary command verbatim: 'Love your neighbor as yourself'; his claim that this single commandment fulfills the entire law follows Jesus's own teaching (Matt 22:39-40) and reflects a Jewish tradition of seeking the law's center — but Paul's point is that the Spirit's love fulfills what circumcision never could."
      }
    ],
    "16": [
      {
        "type": "shadow",
        "target": "Ezek 36:27",
        "note": "Ezekiel's new-covenant promise — 'I will put my Spirit in you and move you to follow my decrees' — is the prophetic architecture behind Paul's 'walk by the Spirit'; the Spirit does not merely enable obedience but constitutes the new-covenant mechanism by which the law's righteous requirement is met from within rather than imposed from without."
      }
    ],
    "22": [
      {
        "type": "shadow",
        "target": "Isa 32:15",
        "note": "Isaiah's vision of the Spirit poured out from on high producing justice, righteousness, peace, and quietness provides the prophetic canvas for the fruit of the Spirit; Paul's list is not an arbitrary virtue catalogue but names the character of the Isaianic new-creation community constituted by the Spirit's arrival."
      }
    ],
    "24": [
      {
        "type": "shadow",
        "target": "Deut 30:6",
        "note": "Moses's promise that God will circumcise the hearts of his people 'so that you may love him with all your heart and soul' anticipates the mortification of the flesh that Paul describes; the internal transformation Moses envisioned — heart-circumcision rather than flesh-circumcision — is what Paul identifies as crucifying the flesh with its passions."
      }
    ],
    "25": [
      {
        "type": "shadow",
        "target": "Ezek 37:14",
        "note": "In the dry-bones vision God promises 'I will put my Spirit in you and you will live'; Paul's 'if we live by the Spirit, let us also walk by the Spirit' enacts this promise — the life the Spirit gives is not merely spiritual existence but a specific manner of conduct aligned with the Spirit's own character."
      }
    ]
  },
  "6": {
    "2": [
      {
        "type": "allusion",
        "target": "Lev 19:18",
        "note": "Bearing one another's burdens as fulfillment of 'the law of Christ' echoes the love-your-neighbor command just cited (5:14); the law of Christ is not a new law-code but the Levitical love-command now internalized and empowered by the Spirit working through the community."
      },
      {
        "type": "shadow",
        "target": "Deut 15:7",
        "note": "Deuteronomy's instruction to open the hand generously to brothers in need establishes communal burden-sharing as a covenantal obligation, not optional charity; Paul's 'law of Christ' recovers this mutuality within the eschatological community where all are debtors to the same grace."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "Hos 8:7",
        "note": "Hosea's 'they sow the wind and reap the whirlwind' established the sowing-reaping principle in Israel's prophetic tradition as a statement about moral causality under divine governance; Paul draws on this idiom to warn that sowing to the flesh is not merely unwise but carries built-in consequence — corruption — by the same logic."
      },
      {
        "type": "allusion",
        "target": "Prov 22:8",
        "note": "Proverbs' 'whoever sows injustice reaps calamity' (LXX: 'whoever sows evil reaps trouble') belongs to the Wisdom tradition's consistent insistence that moral choices have real-world outcomes; Paul's formulation 'God cannot be mocked' frames this not as natural law but as divine governance ensuring the harvest matches the seed."
      }
    ],
    "9": [
      {
        "type": "shadow",
        "target": "Isa 40:31",
        "note": "Isaiah's promise that those who hope in the LORD will 'run and not grow weary' provides the eschatological register for Paul's exhortation not to become weary in doing good; the harvest metaphor implies that the reaping season is certain — the prophetic vision of renewal underlies the call to endure until 'the proper time.'"
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Jer 9:23",
        "note": "Jeremiah's 'let the one who boasts boast in this: that they understand and know me' (cited by Paul in 1 Cor 1:31) shapes the contrast in Gal 6:14 between boasting in circumcision — visible, bodily, self-achieved — and boasting in the cross, which is boasting in what God has done at the cost of what the boaster formerly prized."
      }
    ],
    "15": [
      {
        "type": "allusion",
        "target": "Isa 65:17",
        "note": "Isaiah's 'I am creating new heavens and a new earth' is the prophetic source for Paul's kainē ktisis (new creation); Paul narrows the cosmic scope to the individual and community transformed in Christ, but the vocabulary signals that this personal renewal participates in the eschatological new-creation Isaiah announced."
      },
      {
        "type": "allusion",
        "target": "Isa 43:19",
        "note": "God's declaration 'I am doing a new thing — now it springs up' frames new creation as divine initiative breaking into history; Paul's 'what counts is the new creation' positions the gospel not as a refined version of the old order but as the emergence of what Isaiah's new-thing language pointed toward."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "Num 6:24",
        "note": "The Aaronic blessing 'the LORD bless you and keep you... give you peace' is the covenantal benediction Paul echoes with 'peace and mercy to all who follow this rule'; by extending the blessing to 'the Israel of God' Paul claims that those who walk by the new-creation rule now receive the priestly blessing Israel was given at Sinai."
      },
      {
        "type": "allusion",
        "target": "Ps 125:5",
        "note": "The psalm's closing 'peace be on Israel' is a liturgical formula Paul consciously redeploies; identifying the recipients as 'the Israel of God' — those defined by the new creation, not circumcision — he applies Israel's peace-benediction to the covenant community reconstituted around Christ."
      }
    ]
  }
}


def main():
    existing = load_echo('galatians')
    merge_echo(existing, GALATIANS_ECHOES)
    save_echo('galatians', existing)
    print('Galatians 4–6 echoes written.')

if __name__ == '__main__':
    main()
