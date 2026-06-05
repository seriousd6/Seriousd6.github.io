"""
Echo layer — 1 Corinthians chapters 12-16
Output: data/echoes/1corinthians.json (adds ch12-16)

Ch12-14: Spiritual gifts / body of Christ
Ch15: Resurrection chapter (most extensive OT echo in the epistle)
Ch16: Collection and greetings
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
  "12": {
    "12": [
      {"type": "allusion", "target": "Gen 2:23-24", "note": "One body, many members — Paul's body-of-Christ ecclesiology resonates with the one-flesh unity of Adam and Eve; many distinct persons forming one unified reality through the Spirit"},
      {"type": "allusion", "target": "Exod 30:25-31", "note": "The same Spirit — the anointing oil that consecrated the tabernacle and its vessels was a unified anointing that set apart diverse elements for one holy purpose; the Spirit's unity amid diverse gifts parallels the anointing's unity"}
    ]
  },
  "13": {
    "12": [
      {"type": "allusion", "target": "Num 12:8", "note": "Now we see through a glass dimly, but then face to face — Moses saw YHWH panim el panim (face to face); Paul's eschatological vision of 'face to face' exceeds even the Mosaic face-to-face encounter, making the beatific vision a universal promise for all believers"},
      {"type": "allusion", "target": "Deut 34:10", "note": "No prophet like Moses whom YHWH knew face to face — the ultimate OT intimacy of knowing God becomes Paul's description of eschatological knowing: I shall know fully, even as I have been fully known"}
    ]
  },
  "15": {
    "3": [
      {"type": "fulfillment", "target": "Isa 53:5", "note": "Christ died for our sins according to the Scriptures — Paul's first creedal element cites the Scriptures; Isa 53 (he was wounded for our transgressions) is the primary referent, the Servant's substitutionary death as the fulfillment of the scriptural pattern"},
      {"type": "fulfillment", "target": "Ps 16:10", "note": "He was raised on the third day according to the Scriptures — the second creedal element; Ps 16:10 (you will not let your Holy One see corruption) cited as resurrection prophecy; the third-day specificity may echo Hos 6:2 (after two days he will revive us; on the third day he will raise us)"}
    ],
    "20": [
      {"type": "fulfillment", "target": "Lev 23:10-11", "note": "Christ has been raised as the firstfruits of those who have fallen asleep — the feast of firstfruits (reshit / aparche) was the first sheaf of the harvest waved before YHWH, consecrating the whole harvest. Christ's resurrection is the firstfruits that consecrates and guarantees the general resurrection harvest"},
      {"type": "allusion", "target": "Isa 26:19", "note": "Your dead shall live; their bodies shall rise — one of the clearest OT resurrection promises; Paul's firstfruits language builds on the prophetic expectation of bodily resurrection that Isa 26:19 articulates"}
    ],
    "22": [
      {"type": "allusion", "target": "Gen 2:7", "note": "In Adam all die, so also in Christ shall all be made alive — the Adam-Christ typology is grounded in Gen 2:7 (YHWH formed Adam, breathed life into him); Adam is the death-head of the old humanity, Christ the life-head of the new. The Adam-Christ contrast structures Romans 5 as well"},
      {"type": "type", "target": "Gen 3:19", "note": "Death through Adam — the curse of Gen 3:19 (you are dust and to dust you shall return) is the reality that the Adam-in-Christ reversal overcomes; the firstfruits resurrection is the first reversal of the Adamic curse"}
    ],
    "27": [
      {"type": "fulfillment", "target": "Ps 8:6", "note": "For God has put all things in subjection under his feet — Paul cites Ps 8:6 (you have put all things under his feet) as fulfilled in Christ's resurrection-exaltation; what Ps 8 said about Adam/humanity is now realized in the second Adam who actually rules all things"},
      {"type": "fulfillment", "target": "Ps 110:1", "note": "He must reign until he has put all his enemies under his feet — Ps 110:1 (the LORD says to my Lord: sit at my right hand until I make your enemies your footstool) is the eschatological frame for Christ's present reign between resurrection and parousia"}
    ],
    "45": [
      {"type": "fulfillment", "target": "Gen 2:7", "note": "The first man Adam became a living being (psuche zosa, citing LXX Gen 2:7 exactly) — the last Adam became a life-giving spirit; Paul's contrast is between the LXX-quoted creation of Adam from dust (Genesis) and the eschatological new creation of Christ (pneuma zoopoioun). The citation creates a direct textual bridge between protology and eschatology"},
      {"type": "allusion", "target": "Dan 12:3", "note": "The spiritual body — those who are wise shall shine like the brightness of the heavens; Paul's resurrection-body language (doxa/glory differentials in vv. 41-42) resonates with Daniel's glory-language for the resurrection of the righteous"}
    ],
    "54": [
      {"type": "fulfillment", "target": "Isa 25:8", "note": "Death is swallowed up in victory — Paul quotes Isa 25:8 (he will swallow up death forever) at the climax of the resurrection argument; the eschatological banquet of Isa 25 where YHWH destroys death is now fulfilled in Christ's resurrection and will be completed at the parousia"},
      {"type": "fulfillment", "target": "Hos 13:14", "note": "O death, where is your victory? O death, where is your sting? — Paul adapts Hos 13:14 (where are your plagues, O death? Where is your sting, O Sheol?) as a taunt over conquered death; the LXX rendering allows Paul to quote it as a victory-cry over the defeatt of death through resurrection"}
    ]
  },
  "16": {
    "22": [
      {"type": "allusion", "target": "Deut 27:26", "note": "Let him be accursed (anathema) — the curse-formula echoes the covenant curses of Deuteronomy (Deut 27:26: cursed be everyone who does not confirm the words of this law); Paul's anathema on those who do not love the Lord applies the covenant curse-logic to the new covenant community"},
      {"type": "allusion", "target": "Ps 130:6", "note": "Maranatha (Our Lord, come!) — the Aramaic prayer preserved in Greek transliteration echoes the watchman's longing of Ps 130:6 (my soul waits for the LORD more than watchmen for the morning); it is the earliest attested Christian prayer for the parousia"}
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
