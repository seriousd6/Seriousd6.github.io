"""
MKT Echo — 1 Samuel chapters 22–24
Run: python3 scripts/zc-echo-1samuel-22-24.py

Ch22: Adullam cave (David's 400); Doeg massacres priests of Nob; Abiathar escapes to David (23 verses)
Ch23: Keilah rescue; wilderness pursuit; Jonathan's final visit; Ziphites' betrayal (29 verses)
Ch24: En-gedi cave; David spares Saul; Saul's acknowledgment (22 verses)

Key echo types:
- David's gathering of the distressed/rejected → Jesus gathering the weary (Matt 11:28)
- Doeg's priest massacre → Herod's massacre of innocents (Matt 2:16-18)
- YHWH not giving David into Saul's hand → Acts 2:24 (death could not hold him)
- Jonathan's covenantal pledge → Heb 7:22 (Jesus guarantor of better covenant)
- David's restraint toward the anointed → Phil 2:5-8 (Christ did not exploit equality with God)
- David's appeal to YHWH as judge → 1 Pet 2:23 (entrusted himself to him who judges justly)
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

SAMUEL1_ECHO = {
  "22": {
    "1": [
      {"type": "allusion", "target": "Heb 11:38", "note": "David flees to the cave of Adullam — the anointed king living in caves and desert places, hunted by the established power structure; Heb 11:38 describes the OT faithful as those 'of whom the world was not worthy — wandering about in deserts and mountains, and in dens and caves of the earth'; the Davidic pattern of the hidden, hunted anointed king is fulfilled in Jesus's itinerant ministry without a place to lay his head (Matt 8:20)"}
    ],
    "2": [
      {"type": "allusion", "target": "Matt 11:28", "note": "Everyone who was in distress, and everyone who was in debt, and everyone who was bitter in soul gathered to David — the rejected, indebted, and desperate spontaneously gather to the anointed king in exile; Jesus's 'Come to me, all who labor and are heavy laden, and I will give you rest' (Matt 11:28) is the messianic fulfillment of this pattern: the true anointed king gathers the distressed of Israel around himself"},
      {"type": "allusion", "target": "1 Cor 1:26", "note": "David's 400 are the socially marginal and economically broken — 'not many of you were wise according to worldly standards, not many were powerful, not many were of noble birth' (1 Cor 1:26); God's pattern of gathering the unlikely and weak around his anointed is consistent from David's cave to Paul's churches; the kingdom community is not formed from the socially secure"}
    ],
    "17": [
      {"type": "allusion", "target": "Matt 2:16", "note": "Saul orders his servants to kill the priests of Nob — the massacre of those associated with the Lord's anointed by the threatened political ruler is the pattern fulfilled in Herod's massacre of the innocents (Matt 2:16-18); in both cases a threatened king uses his officials to destroy those connected to the rightful anointed, and in both cases the anointed one escapes while others die in his place"}
    ],
    "19": [
      {"type": "allusion", "target": "Matt 2:18", "note": "Nob, the city of priests, was struck with the edge of the sword — 85 priests killed plus the entire population of Nob; this is the massacre that follows the anointed king's hidden presence; Matthew 2:18 cites Jer 31:15 (Rachel weeping for her children) over Herod's massacre, placing both events in the same theological pattern: the powers of the present age destroy the innocent when threatened by the anointed one"}
    ],
    "20": [
      {"type": "allusion", "target": "Heb 7:25", "note": "Abiathar the son of Ahimelech escaped and fled after David — the one priest who survives the Nob massacre reaches the safety of David's presence and becomes his priest; Hebrews 7:25 applies the same principle to Christ: 'he always lives to make intercession' for those who draw near to God through him; the priest who survives by reaching the anointed king is a type of those who find their only safety in Christ's priestly intercession"}
    ]
  },
  "23": {
    "2": [
      {"type": "allusion", "target": "John 5:30", "note": "David inquired of YHWH — David's repeated consultation of YHWH before military action (vv2, 4, 9-12) is the OT pattern of the anointed one acting only according to the Father's direction; Jesus's 'I can do nothing on my own. As I hear, I judge, and my judgment is just, because I seek not my own will but the will of him who sent me' (John 5:30) is the messianic fulfillment of David's pattern of total dependence on YHWH's guidance before acting"}
    ],
    "14": [
      {"type": "allusion", "target": "Acts 2:24", "note": "God did not give David into Saul's hand — YHWH's sovereign preservation of the anointed king despite relentless, well-resourced pursuit; Acts 2:24 applies the same principle to the resurrection: 'God raised him up, loosing the pangs of death, because it was not possible for him to be held by it'; just as it proved impossible for Saul to eliminate the anointed despite superior power, it proved impossible for death to hold the true Anointed One"}
    ],
    "16": [
      {"type": "allusion", "target": "Heb 7:25", "note": "Jonathan, Saul's son, rose and went to David at Horesh and strengthened his hand in God — Jonathan's visit to the fugitive anointed king in the wilderness, strengthening him and affirming the covenant, is a type of Christ's ongoing intercession; Heb 7:25: 'he always lives to make intercession for them'; Jonathan's covenantal solidarity with David despite every obstacle foreshadows the mediator who never abandons his covenant people"}
    ],
    "17": [
      {"type": "allusion", "target": "Rev 3:21", "note": "Jonathan says to David: 'You shall be king over Israel, and I shall be next to you' — the voluntary relinquishment of inherited kingship so the true anointed king can reign, with the one who yielded sharing in his reign; Rev 3:21 applies this pattern eschatologically: 'The one who conquers, I will grant him to sit with me on my throne, as I also conquered and sat down with my Father on his throne'; Jonathan's position as second to David foreshadows the overcomer's place with Christ"}
    ],
    "18": [
      {"type": "allusion", "target": "Heb 7:22", "note": "And they two made a covenant before YHWH — the third and final covenant between Jonathan and David, made in the wilderness; Jonathan pledges his succession rights to David and David pledges preservation of Jonathan's descendants; Heb 7:22: 'Jesus has become the guarantor of a better covenant'; the covenants Jonathan makes with David on behalf of Israel's future foreshadow the new covenant that Christ mediates as both king and guarantor"}
    ]
  },
  "24": {
    "6": [
      {"type": "allusion", "target": "Phil 2:6", "note": "David said to his men: YHWH forbid that I should do this thing to my lord, YHWH's anointed, to put out my hand against him — David refuses to exploit the opportunity to seize the kingdom when it falls into his hands; Phil 2:6 applies this pattern to Christ: 'though he was in the form of God, did not count equality with God a thing to be grasped'; both David and Christ, when given the opportunity to seize what was rightfully theirs by direct action, chose the path of restraint and submission to the Father's timing"}
    ],
    "11": [
      {"type": "allusion", "target": "1 Pet 2:23", "note": "David declares his innocence to Saul: 'I have not sinned against you, though you seek my life to take it' — the righteous one proclaiming his innocence before his persecutor without retaliating; 1 Pet 2:23: 'When he was reviled, he did not revile in return; when he suffered, he did not threaten, but continued entrusting himself to him who judges justly'; David's appeal to Saul is the OT pattern of the innocent righteous one who refuses to answer violence with violence"}
    ],
    "12": [
      {"type": "allusion", "target": "Rom 12:19", "note": "May YHWH avenge me on you, but my hand shall not be against you — David's explicit commitment to leave vengeance to YHWH rather than taking it himself; Rom 12:19: 'Beloved, never avenge yourselves, but leave it to the wrath of God, for it is written, Vengeance is mine, I will repay, says the Lord'; David's deliberate non-retaliation in En-gedi is the OT's paradigmatic expression of the principle Paul cites in Romans 12"}
    ],
    "15": [
      {"type": "allusion", "target": "Heb 12:23", "note": "YHWH therefore be judge and give sentence between me and you — David appeals to YHWH as the ultimate judge; Heb 12:23 identifies 'God, the judge of all' as the one to whose court believers have come in the new covenant assembly; the appeal to divine judgment as the proper resolution of the conflict between the anointed king and his persecutors is the pattern of the final judgment where Christ's vindication will be made complete"}
    ],
    "17": [
      {"type": "allusion", "target": "Rom 5:8", "note": "Saul said to David: You are more righteous than I, for you have repaid me good, whereas I have repaid you evil — the acknowledgment of a righteous one who returned good for evil; Rom 5:8: 'God shows his love for us in that while we were still sinners, Christ died for us'; David's pattern of returning good for evil from Saul prefigures Christ's supreme act of returning blessing for human rejection and enmity; the confession of the persecutor who recognizes the righteousness of the one he persecuted"}
    ],
    "20": [
      {"type": "allusion", "target": "Acts 2:36", "note": "Saul declares: And now, behold, I know that you shall surely be king, and that the kingdom of Israel shall be established in your hand — the acknowledgment by the incumbent power that the anointed king will triumph; Acts 2:36: 'Let all the house of Israel therefore know for certain that God has made him both Lord and Christ'; Saul's involuntary confession parallels the acknowledgment that every tongue will ultimately give: the kingship of the anointed one is established and will not be overturned"}
    ]
  }
}

def main():
    e = load_echo('1samuel')
    merge_echo(e, SAMUEL1_ECHO)
    save_echo('1samuel', e)
    count = sum(len(v) for v in SAMUEL1_ECHO.values())
    print(f'1samuel echo: wrote {count} chapters (22-24)')

if __name__ == '__main__':
    main()
