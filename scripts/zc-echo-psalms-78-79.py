"""
MKT Echo Layer — Psalms chapters 78–79
Run: python3 scripts/zc-echo-psalms-78-79.py

Psalm 78: Asaph's great historical psalm from Exodus to David. v2 already complete
  (Matt 13:35 fulfillment). Adding: v24-25 manna→John 6:31-32; v15-16 rock water→
  1 Cor 10:4; v52-53 shepherd-flock→John 10:11; v70-72 David chosen→Acts 13:22.
Psalm 79: Lament over temple defilement (likely Babylonian destruction). v1→Luke 21:24
  (Jerusalem trampled); v2→Rev 19:17-18 (birds eating flesh); v9 atonement language→
  Heb 9:22; v11 captives→Luke 4:18; v13 sheep of his pasture→John 10:14/Rev 7:17.
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

PSALMS_ECHOES = {
  "78": {
    "15": [
      {
        "type": "type",
        "target": "1 Cor 10:4",
        "note": "Verses 15-16 — 'He split the rocks in the wilderness and gave them drink abundantly as from the deep' — record the water-from-the-rock miracle that Paul explicitly identifies as a type of Christ: 'the spiritual Rock that followed them, and the Rock was Christ' (1 Cor 10:4). The physical provision in the desert is the shadow; Christ is the reality from which living water flows."
      }
    ],
    "24": [
      {
        "type": "type",
        "target": "John 6:31",
        "note": "Verses 24-25 — 'He rained down manna on them to eat and gave them the grain of heaven. Man ate of the bread of the angels' — are the text Jesus' Capernaum audience quotes back to him (John 6:31: 'our fathers ate the manna in the wilderness'). Jesus' response reframes the manna as a type: 'my Father gives you the true bread from heaven... I am the bread of life' (John 6:32-35). The wilderness provision is the shadow; Christ himself is the sustenance."
      }
    ],
    "52": [
      {
        "type": "shadow",
        "target": "John 10:11",
        "note": "Verse 52 — 'Then he led out his people like sheep and guided them in the wilderness like a flock' — uses the shepherd-flock image for God's Exodus leadership. John 10:11 presents Christ as 'the good shepherd' who lays down his life for the sheep, fulfilling the role Ps 78 attributes to God. The God who shepherded Israel through the wilderness becomes incarnate as the shepherd who dies for the flock."
      }
    ],
    "70": [
      {
        "type": "shadow",
        "target": "Acts 13:22",
        "note": "Verses 70-72 — 'He chose David his servant and took him from the sheepfolds... to shepherd Jacob his people' — narrate God's selection of the shepherd-king David, which Acts 13:22-23 places in the trajectory to Christ: 'Of this man's offspring God has brought to Israel a Savior, Jesus.' David the shepherd-king is the type; Christ is the perfect shepherd-king who guards the sheep with a skill that David's integrity could only approximate."
      }
    ]
  },
  "79": {
    "1": [
      {
        "type": "allusion",
        "target": "Luke 21:24",
        "note": "Verse 1 — 'O God, the nations have come into your inheritance; they have defiled your holy temple; they have laid Jerusalem in ruins' — is the historical lament Jesus applies forward: 'Jerusalem will be trampled underfoot by the Gentiles until the times of the Gentiles are fulfilled' (Luke 21:24). Ps 79's anguish over pagan desecration becomes the template for the AD 70 destruction, which Jesus predicts as the pattern repeating."
      },
      {
        "type": "allusion",
        "target": "Rev 11:2",
        "note": "Verse 1's 'nations into your inheritance... Jerusalem in ruins' also stands behind Rev 11:2: 'the holy city they will trample for forty-two months.' Revelation recasts Ps 79's historical devastation as the eschatological trampling that precedes final vindication, placing the psalm's lament within the larger arc of God's redemptive plan."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "Rev 19:17",
        "note": "Verse 2 — 'they have given the bodies of your servants to the birds of the heavens for food, the flesh of your faithful to the beasts of the earth' — supplies the language Rev 19:17-18 uses for the eschatological judgment: 'Come, gather for the great supper of God, to eat the flesh of kings, the flesh of captains.' The psalmist's anguish over the slain becoming carrion is inverted in Revelation: God's enemies face the same fate that befell his servants."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Heb 9:22",
        "note": "Verse 9 — 'Help us, O God of our salvation... deliver us, and atone for our sins, for your name's sake' — pleads for atonement (Hebrew: <em>kapper</em>, cover/expiate). Heb 9:22 makes the mechanism explicit: 'without the shedding of blood there is no forgiveness of sins.' The psalm's cry for atonement is answered in Christ's blood; the mercy Asaph asks for God's name's sake is enacted through the name of Jesus."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Luke 4:18",
        "note": "Verse 11 — 'Let the groaning of the prisoner come before you; according to your great power, preserve those doomed to die' — is the lament for captives and the condemned. Jesus opens his public ministry by quoting Isa 61:1 (Luke 4:18): 'he has sent me to proclaim liberty to the captives.' Christ's ministry is the enacted answer to every prisoner's groan Ps 79 voices — the deliverance is no longer a prayer but an announcement."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "John 10:14",
        "note": "Verse 13 — 'we your people, the sheep of your pasture, will give thanks to you forever; from generation to generation we will recount your praise' — closes the lament with the shepherd-sheep self-identification of God's people. John 10:14 — 'I am the good shepherd; I know my own and my own know me' — takes up exactly this language: the sheep who give thanks in v13 are the sheep Christ knows and calls by name."
      },
      {
        "type": "allusion",
        "target": "Rev 7:17",
        "note": "The same closing image — 'sheep of your pasture' giving perpetual praise — is fulfilled in Rev 7:17: 'the Lamb in the midst of the throne will be their shepherd, and he will guide them to springs of living water.' The sheep who suffer the lament of Ps 79 and survive to praise in v13 become the great multitude in white robes, guided forever by the Lamb."
      }
    ]
  }
}


def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    print('Psalms 78-79 echoes written.')

if __name__ == '__main__':
    main()
