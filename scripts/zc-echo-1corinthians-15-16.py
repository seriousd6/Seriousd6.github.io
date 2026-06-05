"""
MKT Echo Data — 1 Corinthians chapters 15–16
Run: python3 scripts/zc-echo-1corinthians-15-16.py

Source data used:
- data/interlinear/1corinthians.json
- data/translation/draft/mediating/1corinthians.json (MKT text)
- data/parallels/1corinthians.json (prototype echoes absorbed below)
- data/echoes/1corinthians.json (existing echoes for chs 1–14 for consistency)

Key decisions:
- Ch 15 is the densest OT-quotation chapter in the Corinthian correspondence:
  Paul's resurrection argument is built on explicit OT citations and types
  (Ps 110:1, Ps 8:6, Gen 2:7, Isa 25:8, Hos 13:14) — all classified as
  fulfillment or quote, since Paul himself frames them as scriptural proof
- Adam/Christ typology (vv21-22, 45-49): Gen 2:7; Gen 3:19 are the type-texts;
  Christ as last Adam is the antitype who reverses what the first Adam lost
- v20 firstfruits: Lev 23:10-11 — the Passover-season firstfruits offering is the
  type; Christ's resurrection as firstfruits of the dead is the antitype
- Parallels absorption:
    15:27 [quotation] Ps 8:6 -> echo type: quote
    15:45 [quotation] Gen 2:7 -> echo type: quote
    15:54 [prophecy-source] Isa 25:8 -> echo type: fulfillment
    15:55 [prophecy-source + quotation] Hos 13:14 -> echo type: quote (LXX form)
- Ch 16 logistical section: only verses with genuine OT resonance included;
  the Jerusalem collection echoes the OT temple-support pattern; Marana tha (v22)
  echoes the OT longing for YHWH's coming
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


CORINTHIANS_ECHOES = {
  "15": {
    "3": [
      {
        "type": "fulfillment",
        "target": "Isa 53:5",
        "note": "Christ died for our sins 'according to the Scriptures' — Paul's primary scriptural referent is Isa 53, where the Servant bears 'the iniquity of us all' and is 'wounded for our transgressions.' The substitutionary formula ('for our sins') matches precisely the structure of Isa 53:5-6, 10-12, where the Servant's death accomplishes vicarious sin-bearing."
      },
      {
        "type": "allusion",
        "target": "Ps 22:1",
        "note": "The psalmic tradition of the righteous sufferer — especially Ps 22, quoted from the cross (Mark 15:34) — is part of the scriptural pattern Paul invokes. Ps 22 provides the detailed template of the unjust death of God's anointed and ends in vindication, forming the narrative shape that the passion and resurrection fulfill."
      }
    ],
    "4": [
      {
        "type": "fulfillment",
        "target": "Hos 6:2",
        "note": "Raised 'on the third day according to the Scriptures' — Hos 6:2 ('after two days he will revive us; on the third day he will raise us up') was read in early Christianity as a scriptural anticipation of the resurrection pattern. The third-day timing of Christ's resurrection is presented as scriptural fulfillment, not accident."
      },
      {
        "type": "fulfillment",
        "target": "Ps 16:10",
        "note": "David's psalm ('you will not abandon me to the grave, nor will you let your holy one see decay') is applied to Christ's resurrection at Pentecost (Acts 2:27-31) and in Paul's preaching (Acts 13:35). As part of 'the Scriptures' that anticipated the resurrection, Ps 16:10 is a direct fulfillment-text for Paul's summary in v4."
      }
    ],
    "20": [
      {
        "type": "type",
        "target": "Lev 23:10",
        "note": "Christ as 'firstfruits of those who have fallen asleep' applies the Feast of Firstfruits typology to the resurrection. The firstfruits offering (Lev 23:10-11 — the first sheaf of the barley harvest, presented to the LORD at Passover season) is the pledge and preview of the whole harvest; Christ's resurrection is the pledge and preview of the general resurrection. The Passover-season timing of Christ's resurrection matches the firstfruits festival."
      }
    ],
    "21": [
      {
        "type": "type",
        "target": "Gen 2:17",
        "note": "Death came through a man — Adam is the type whose disobedience introduced death into creation (Gen 2:17, 'when you eat of it you will certainly die'; Gen 3:19). The Adam-death is the typological problem; the resurrection-through-a-man (Christ) is its solution. Paul's logic requires the typological parallel: because death entered through one man, the reversal must come through one man."
      }
    ],
    "22": [
      {
        "type": "type",
        "target": "Gen 3:19",
        "note": "The 'in Adam all die' formula summarizes Gen 3 — death is the inheritance of all who share solidarity with Adam by natural descent. The 'in Christ all will be made alive' is the structural counterpart: life as the gift of those in Christ by faith and spiritual solidarity. The Adam/Christ parallel is the most concentrated expression of what the Fall narrative established and the whole OT redemptive history promised to reverse."
      }
    ],
    "25": [
      {
        "type": "quote",
        "target": "Ps 110:1",
        "note": "He must reign 'until he has put all his enemies under his feet' — direct citation of Ps 110:1 LXX ('sit at my right hand until I make your enemies a footstool for your feet'). The Davidic-messianic enthronement psalm is applied to the risen and ascended Christ who reigns in the period between his resurrection and the final consummation. The citation establishes that the present age is Christ's reign, and the resurrection is what makes that reign possible."
      }
    ],
    "26": [
      {
        "type": "fulfillment",
        "target": "Isa 25:8",
        "note": "The last enemy to be destroyed is death — Isa 25:8 ('he will swallow up death forever; the Lord GOD will wipe away tears from all faces') is the OT promise of death's ultimate defeat. Paul identifies the resurrection as the mechanism: death is defeated by the one who passed through it and came out the other side. The full fulfillment will come at the general resurrection (v54 cites Isa 25:8 explicitly)."
      }
    ],
    "27": [
      {
        "type": "quote",
        "target": "Ps 8:6",
        "note": "For he 'has put everything under his feet' — direct quotation of Ps 8:6 LXX ('you made him ruler over the works of your hands; you put everything under his feet'). The psalm about the dignity of humanity-as-son-of-man is applied to Christ as the true human being who receives the dominion that Adam forfeited. Paul and the author of Hebrews (2:6-9) both read Ps 8 as a Christological prophecy through the lens of the Adam/Christ typology."
      }
    ],
    "32": [
      {
        "type": "quote",
        "target": "Isa 22:13",
        "note": "'Let us eat and drink, for tomorrow we die' — verbatim quotation of Isa 22:13, where Isaiah condemns Jerusalem's self-indulgent nihilism in the face of coming judgment. Paul's citation is ironic: without the resurrection, those who deny it are exemplifying the very response that Isaiah condemned in those who refused to take God's word seriously. The resurrection is the premise of any ethics beyond immediate gratification."
      }
    ],
    "45": [
      {
        "type": "quote",
        "target": "Gen 2:7",
        "note": "Direct quotation of Gen 2:7 LXX ('the first man Adam became a living being') as scriptural proof for the natural body preceding the spiritual. Paul adds 'the last Adam, a life-giving Spirit' as his Christological interpretation: where Gen 2:7 provides the Adam-type (a being who receives life), Christ is the antitype who not only possesses life but imparts it to others. The 'last Adam' designation makes Christ the eschatological new humanity."
      }
    ],
    "47": [
      {
        "type": "allusion",
        "target": "Gen 2:7",
        "note": "The first man was 'of the dust of the earth' — allusion to Gen 2:7 ('formed from the dust of the ground') and Gen 3:19 ('for dust you are and to dust you will return'). The earthly, dusty origin of Adam and his descendants is the basis of their mortality and the need for the transformation Paul describes. The second man's heavenly origin (not of dust but of the Spirit) is the basis of the resurrection transformation."
      }
    ],
    "49": [
      {
        "type": "allusion",
        "target": "Gen 1:27",
        "note": "We have borne the image of the earthly man (Adam) and will bear the image of the heavenly man (Christ) — the Gen 1:26-27 image-of-God motif. Adam was made in God's image; Gen 5:3 records that Seth was made in Adam's image, showing the image passes through the fallen line in a corrupted form. Those in Christ will bear the restored image of God that Christ himself is (2 Cor 4:4; Col 1:15; Col 3:10)."
      }
    ],
    "54": [
      {
        "type": "fulfillment",
        "target": "Isa 25:8",
        "note": "Direct fulfillment quotation: 'Death has been swallowed up in victory' — from Isa 25:8 LXX. Paul presents the resurrection body's final transformation as the event that fulfills Isaiah's eschatological promise. The future of Isaiah becomes the accomplished fact of Christ's resurrection (already) and its completion at the last trumpet (not yet). Paul uses 'then will be fulfilled the saying that is written' — his own signal that this is a fulfillment citation."
      }
    ],
    "55": [
      {
        "type": "quote",
        "target": "Hos 13:14",
        "note": "Direct quotation of Hos 13:14 LXX ('Where, O death, are your plagues? Where, O Hades, is your destruction?'). In Hosea's original context, the questions are threats of judgment against Israel; Paul converts them into a victor's taunt against death, now defeated by the resurrection. The LXX form Paul uses reads as a triumphant challenge rather than a divine threat — Paul reads Hosea's judgment-oracle as the death-taunt of the resurrection age."
      }
    ]
  },
  "16": {
    "1": [
      {
        "type": "theme",
        "target": "2 Chr 24:5",
        "note": "The collection for the Jerusalem church echoes the OT pattern of material contributions for the temple community and its personnel (2 Chr 24:5; Neh 10:32-33; Exod 30:12-16). Paul's collection participates in the same theological logic of covenant solidarity through material sharing, fulfilling the prophetic promise that the nations would bring their wealth to support the restored people of God (Isa 60:5-7; 66:20)."
      }
    ],
    "2": [
      {
        "type": "theme",
        "target": "Ps 118:24",
        "note": "The first day of every week — the resurrection day — as the gathering and offering day participates in the eighth-day theology of new creation. The first day (Sunday) is simultaneously the day after the Sabbath (the seventh day of the old creation) and the first day of the new week (the beginning of the resurrection age). Setting aside an offering on this day is worship shaped by the reality of Christ's resurrection."
      }
    ],
    "8": [
      {
        "type": "theme",
        "target": "Lev 23:15",
        "note": "Paul will remain in Ephesus until Pentecost — the Feast of Weeks (Lev 23:15-21, Shavuot), fifty days after Passover. Pentecost had been reinterpreted by the Spirit's outpouring in Acts 2 as the feast of the new covenant's inauguration. Paul's reference to the festival as a calendar marker reflects the early church's continued use of Israel's liturgical calendar as the structure of the Christian year."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Josh 1:6",
        "note": "Be on your guard; stand firm in the faith; be courageous; be strong — the fourfold exhortation echoes God's repeated charge to Joshua (Josh 1:6-9: 'be strong and courageous ... be careful to obey ... do not be afraid'). The Christological context transforms the charge: the courage required is specifically for holding the resurrection faith against those within the congregation who deny it (ch 15), not for military conquest."
      }
    ],
    "22": [
      {
        "type": "allusion",
        "target": "Ps 110:1",
        "note": "Marana tha — 'Come, Lord!' (Aramaic) — is the earliest preserved Christological prayer, drawing on the OT longing for YHWH to come and reign. Ps 110:1 (the Lord enthroned at God's right hand, with enemies being subdued) establishes the messianic-coming framework; the prayer is addressed to the risen Jesus as kyrios, identifying him with the YHWH whose coming was the hope of Israel. The Aramaic form preserved in a Greek letter shows this prayer predates Paul's Greek churches."
      },
      {
        "type": "theme",
        "target": "Isa 64:1",
        "note": "The 'Come, Lord!' prayer participates in the OT eschatological longing for God to intervene decisively — Isaiah's prayer 'Oh that you would rend the heavens and come down!' (Isa 64:1), the Psalms' 'Arise, LORD!' (Ps 7:6; 44:26), the prophetic expectation of YHWH's coming in power (Zech 14:5; Mal 3:1). Paul closes the letter with this prayer: the risen and ascended Christ is the Lord whose coming consummates the whole OT eschatological hope."
      }
    ]
  }
}


def main():
    existing = load_echo('1corinthians')
    merge_echo(existing, CORINTHIANS_ECHOES)
    save_echo('1corinthians', existing)
    ch15 = len(existing.get('15', {}))
    ch16 = len(existing.get('16', {}))
    print(f'1 Corinthians 15-16 echoes written ({ch15} verses in ch 15, {ch16} in ch 16).')

if __name__ == '__main__':
    main()
