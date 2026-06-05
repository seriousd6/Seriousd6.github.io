"""
MKT Echo Layer — Galatians chapters 1–3
Run: python3 scripts/zc-echo-galatians-1-3.py

Source data used:
- data/interlinear/galatians.json
- data/parallels/galatians.json (absorbed; conversion notes below)
- data/translation/draft/mediating/galatians.json (MKT text)
- data/translation/notes/galatians.json (token-level glossary data)

Parallels absorption (ch 3 only; chs 1–2 had no parallels entries):
- 3:6  quotation → quote   (Gen 15:6)
- 3:8  prophecy-source → fulfillment  (Gen 12:3; Paul says "Scripture foresaw… announced the gospel in advance")
- 3:10 quotation → quote   (Deut 27:26)
- 3:11 prophecy-source → quote  (Hab 2:4; used as proof text, no explicit fulfillment claim)
- 3:12 prophecy-source → quote  (Lev 18:5; used as antithetical proof text)
- 3:13 quotation → quote   (Deut 21:23)
- 3:16 prophecy-source → fulfillment  (Gen 22:18; Paul explicitly interprets "seed" = Christ)
- 4:4  prophecy-source (Gen 3:15) deferred to zc-echo-galatians-4-6.py
- 4:21–31, 4:27, 4:30, 5:14 also deferred to zc-echo-galatians-4-6.py

Key decisions:
- 1:15 carries unmistakable verbal echoes of both Jer 1:5 and Isa 49:1; classified allusion
  (Paul does not name these texts but the womb/call language is distinctive in both)
- 1:14 Phinehas (Num 25:11-13) as the paradigm of covenantal zeal Paul is invoking —
  classified theme since Paul does not cite it but his Jewish audience would hear it
- 3:13 adds Isa 53:4–5 alongside Deut 21:23 (the curse + the Servant bearing suffering)
- 3:28 "neither male and female" quotes Gen 1:27 language; classified fulfillment since
  Paul's baptismal formula is a deliberate reversal of the creation distinction in Christ
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
  "1": {
    "4": [
      {
        "type": "allusion",
        "target": "Isa 53:10",
        "note": "The Servant 'made his life an offering for sin' (Isa 53:10) and 'poured out his soul to death' (53:12) — Paul's 'gave himself for our sins' draws on the same Servant-giving pattern, now identified with Christ's self-donation."
      },
      {
        "type": "allusion",
        "target": "Isa 53:12",
        "note": "Isaiah's Servant 'bore the sin of many and made intercession for the transgressors'; Paul's description of Christ giving himself 'for our sins' to deliver from the present evil age activates this register."
      }
    ],
    "14": [
      {
        "type": "theme",
        "target": "Num 25:11",
        "note": "Phinehas was the paradigmatic zealot in Jewish memory — his violent action against apostasy 'turned back God's wrath' and earned him a 'covenant of priesthood' (Num 25:13). Paul's self-description as 'extremely zealous for the traditions of my fathers' invokes this tradition; his persecution of the church was the same covenantal zeal misdirected."
      }
    ],
    "15": [
      {
        "type": "allusion",
        "target": "Jer 1:5",
        "note": "God's word to Jeremiah — 'Before I formed you in the womb I knew you, before you were born I set you apart; I appointed you as a prophet to the nations' — is the closest OT parallel to Paul's language. The verbal overlap (set apart / from the womb / called) is not coincidental; Paul is self-consciously standing in the prophetic tradition."
      },
      {
        "type": "allusion",
        "target": "Isa 49:1",
        "note": "The Servant's testimony 'Before I was born the Lord called me; from my mother's womb he has spoken my name' uses the same womb/call structure. Paul draws on both the prophetic call (Jeremiah) and the Servant's mission to the nations (Isaiah 49)."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "Isa 49:6",
        "note": "The Servant's commission to be 'a light for the Gentiles, that my salvation may reach to the ends of the earth' is the OT foundation for Paul's Gentile mission. His phrase 'that I might preach him among the Gentiles' echoes the Servant's mandate without explicit citation."
      }
    ]
  },
  "2": {
    "6": [
      {
        "type": "allusion",
        "target": "Deut 10:17",
        "note": "Moses declares that God 'shows no partiality' — the same language Paul uses when noting that the Jerusalem pillars' reputation 'makes no difference to me; God does not show favoritism.' Paul applies the divine impartiality principle to the apostolic authority question."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "Ps 143:2",
        "note": "The Psalmist's 'no one living is righteous before you' underlies Paul's principle that 'by the works of the law no one will be justified.' Paul does not quote Psalm 143 explicitly here but uses the same logic: the law's standard, honestly applied, condemns; therefore justification must come by another route."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Isa 53:12",
        "note": "Paul's 'the Son of God, who loved me and gave himself for me' echoes the Servant who 'poured out his soul to death' for the transgressors (Isa 53:12). The personal register ('for me') intensifies the Servant language into individual application."
      }
    ]
  },
  "3": {
    "6": [
      {
        "type": "quote",
        "target": "Gen 15:6",
        "note": "Paul quotes the LXX of Genesis 15:6 verbatim: 'Abraham believed God, and it was credited to him as righteousness.' This is the foundational proof that justification by faith predates the law by four centuries — the same exegetical move Paul makes in Romans 4."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "Gen 15:6",
        "note": "Paul's inference that 'those who have faith are children of Abraham' draws out the relational implication of the Genesis 15:6 quotation: if Abraham's standing before God was defined by faith, then faith-sharing people share his family identity, not circumcision-sharers."
      }
    ],
    "8": [
      {
        "type": "fulfillment",
        "target": "Gen 12:3",
        "note": "Paul explicitly claims that Scripture 'announced the gospel in advance to Abraham: All nations will be blessed through you' (Gen 12:3). This is not retrospective allegory — Paul presents the Abrahamic blessing of the nations as the content of the gospel, now fulfilled through Christ."
      },
      {
        "type": "allusion",
        "target": "Gen 22:18",
        "note": "The repeated Abrahamic promise 'in your offspring all the nations of the earth shall be blessed' (Gen 22:18, quoted in 3:16) gives the 3:8 citation its fuller scope — the Gentile blessing is mediated through the singular Seed."
      }
    ],
    "10": [
      {
        "type": "quote",
        "target": "Deut 27:26",
        "note": "Paul quotes the covenant curse formula from the Shechem ceremony: 'Cursed is everyone who does not continue to do everything written in the Book of the Law.' The quote establishes that the law itself places all its adherents under curse — not because keeping it is wrong but because perfect continual observance is the standard no one meets."
      },
      {
        "type": "allusion",
        "target": "Deut 28:15",
        "note": "The extensive covenant curses of Deuteronomy 28 elaborate the Deut 27:26 formula Paul quotes; the specific curses (exile, disease, defeat) fill out what 'under a curse' means for Israel's history — the very catastrophe Paul sees Israel and law-followers trapped within."
      }
    ],
    "11": [
      {
        "type": "quote",
        "target": "Hab 2:4",
        "note": "Paul cites Habakkuk 2:4 as evidence that no one is justified before God by the law: 'The righteous shall live by faith.' The Habakkuk context is God's answer to the prophet's lament — the Chaldean oppressor will fall; the righteous person persists through covenant faithfulness. Paul takes this as a principle: life before God is structured by faith, not law-performance."
      }
    ],
    "12": [
      {
        "type": "quote",
        "target": "Lev 18:5",
        "note": "Paul quotes Leviticus 18:5 — 'The one who does these things will live by them' — as the contrasting principle to faith. The law operates on a 'do-and-live' logic; faith operates on a 'believe-and-receive' logic. Paul presents these as mutually exclusive systems, not complementary ones."
      }
    ],
    "13": [
      {
        "type": "quote",
        "target": "Deut 21:23",
        "note": "Deuteronomy 21:23 — 'Cursed is everyone who is hung on a pole/tree' — was a Jewish stumbling block to Messiah-crucifixion. Paul turns it into the mechanism of redemption: Christ voluntarily entered the curse-position so that the Deuteronomy curse could be exhausted on him rather than on those who broke the law."
      },
      {
        "type": "allusion",
        "target": "Isa 53:4",
        "note": "The Servant 'carried our sorrows; yet we considered him punished by God, stricken and afflicted' (Isa 53:4). Paul's 'Christ redeemed us from the curse of the law by becoming a curse for us' is the same substitutionary logic: the Servant bears the divine judgment that was ours."
      }
    ],
    "14": [
      {
        "type": "fulfillment",
        "target": "Gen 12:3",
        "note": "The purpose clause 'so that the blessing given to Abraham might come to the Gentiles through Christ Jesus' is Paul's explicit identification of Christ's work as the fulfillment of the Abrahamic Gentile-blessing promise — what Genesis 12:3 anticipated, the cross now accomplishes."
      },
      {
        "type": "allusion",
        "target": "Isa 49:6",
        "note": "The Servant's mission to bring God's 'salvation to the ends of the earth' (Isa 49:6) converges here with the Abrahamic blessing of the nations. Paul's argument joins these two OT trajectories — the Abrahamic promise and the Servant's Gentile mission — in the one event of Christ."
      }
    ],
    "16": [
      {
        "type": "fulfillment",
        "target": "Gen 22:18",
        "note": "Paul's exegesis is explicit: the promise 'to your seed' (Gen 22:18) is grammatically singular and refers to Christ. The promise made at the Akedah — after Abraham's test — is the specific form Paul cites; the binding of Isaac and its seed-promise is the text Christ fulfills."
      },
      {
        "type": "allusion",
        "target": "Gen 12:7",
        "note": "The initial land-and-seed promise in Genesis 12:7 ('to your offspring I will give this land') establishes the same grammatically singular 'seed' that Paul exploits in 3:16. His argument rests on the consistent singular across the Abraham cycle."
      }
    ],
    "19": [
      {
        "type": "theme",
        "target": "Exod 19:1",
        "note": "The giving of the law at Sinai is the background for Paul's 'it was added because of transgressions.' Exodus 19 introduces the Sinai covenant as a conditional arrangement (19:5) distinct from the unconditional promise to Abraham — the later, mediated structure Paul is arguing was always temporary."
      }
    ],
    "22": [
      {
        "type": "allusion",
        "target": "Ps 14:1",
        "note": "Psalm 14:1–3 ('there is no one who does good, not even one') provides the universal human diagnosis that underlies Paul's 'Scripture has locked up everything under the control of sin.' The Scripture that imprisons all under sin is the same body of texts that diagnoses universal human failure (Ps 14; Ps 53; Eccl 7:20)."
      }
    ],
    "27": [
      {
        "type": "allusion",
        "target": "Isa 61:10",
        "note": "Isaiah 61:10 — 'he has clothed me with garments of salvation… as a bride adorns herself' — uses the same clothing-with metaphor for restored covenant standing. Paul's 'clothed yourselves with Christ' in baptism draws on this OT image of God providing the garments of new status."
      }
    ],
    "28": [
      {
        "type": "allusion",
        "target": "Gen 1:27",
        "note": "Paul's 'neither male and female' directly echoes Genesis 1:27's 'male and female he created them' — the only Galatians 3:28 pair that uses 'and' rather than 'nor.' This is a deliberate verbal signal: the division of the sexes in creation is not abolished but transcended in Christ, who recapitulates the image of God."
      },
      {
        "type": "allusion",
        "target": "Joel 2:28",
        "note": "Joel 2:28–29 prophesies that the Spirit will be poured out on 'all people — your sons and daughters… even on my servants, both men and women.' The dissolution of social and gender distinctions in Galatians 3:28 corresponds to the Spirit-inclusion Joel foresaw, now realized in baptismal union with Christ."
      }
    ],
    "29": [
      {
        "type": "fulfillment",
        "target": "Gen 17:7",
        "note": "God's covenant with Abraham — 'I will establish my covenant as an everlasting covenant between me and you and your descendants after you' (Gen 17:7) — is the inheritance that Paul claims belongs to all in Christ. The 'heirs according to the promise' language is the fulfillment of this Abrahamic covenant structure."
      }
    ]
  }
}


def main():
    existing = load_echo('galatians')
    merge_echo(existing, GALATIANS_ECHOES)
    save_echo('galatians', existing)
    print('Galatians 1–3 echoes written.')

if __name__ == '__main__':
    main()
