"""
MKT Echo Layer — Psalms chapters 71–74
Run: python3 scripts/zc-echo-psalms-71-74.py

Psalm 71: Psalm of trust in old age; heavy allusion to Ps 31 (cited at the cross);
  v11 echoes cross-mockery (Matt 27:43); v20 resurrection vocabulary.
Psalm 72: The great royal/messianic psalm — v8 dominion from sea to sea, v10 kings
  bringing gifts (Matt 2:11), v17 all nations blessed (Gal 3:8/Gen 22:18).
Psalm 73: Asaph's crisis of faith resolved in the sanctuary; v17 sanctuary typology
  (Heb 9:11); v24 taken to glory (John 14:3); vv25-26 the ultimate devotion.
Psalm 74: Communal lament over temple destruction; v2 the redeemed congregation
  (Acts 20:28); v12 God as King working salvation; v13-14 crushing Leviathan
  (Rev 12:9); v20 the covenant (Heb 13:20).
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
  "71": {
    "1": [
      {
        "type": "allusion",
        "target": "Ps 31:1",
        "note": "Psalm 71 opens with almost the same words as Ps 31:1 ('In you, O LORD, do I take refuge; let me never be put to shame'). Ps 31:5 is the verse Jesus quotes on the cross (Luke 23:46), so Ps 71's opening invokes that same passion-lament register — the righteous sufferer entrusting himself to God."
      }
    ],
    "5": [
      {
        "type": "theme",
        "target": "Heb 2:13",
        "note": "Verse 5 — 'you are my hope, O Lord GOD' — belongs to the psalmic pattern of God-trusting that Heb 2:13 applies to Christ: 'I will put my trust in him.' The Servant's dependence on God, celebrated in the Psalms, is the posture the Son inhabits in the Incarnation."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Ps 22:9",
        "note": "Verse 6 — 'you are he who took me from my mother's womb' — echoes Ps 22:9, which is itself read christologically by the NT. Both psalms present the same pattern: divine faithfulness from birth, sustaining through unjust suffering to ultimate vindication."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Matt 27:43",
        "note": "Verse 11 — 'God has forsaken him; pursue and seize him, for there is none to deliver him' — is the taunt the enemies level at the psalmist. Matt 27:43 quotes this language almost verbatim as the mockery hurled at Christ on the cross, confirming that the NT reads Ps 71 through the passion frame."
      }
    ],
    "20": [
      {
        "type": "shadow",
        "target": "Acts 2:24",
        "note": "Verse 20 — 'you will revive me again; from the depths of the earth you will bring me up again' — uses resurrection vocabulary. Acts 2:24 applies the same language-field to Christ: God raised him up, loosing the pangs of death. The psalmist's hope of revival from 'the depths' becomes the pattern Christ fulfils bodily."
      }
    ],
    "22": [
      {
        "type": "theme",
        "target": "John 6:69",
        "note": "Verse 22 — 'O Holy One of Israel' — is one of the Psalter's uses of the title Isaiah favors for God. In John 6:69 Peter confesses Jesus as 'the Holy One of God,' applying to Christ the divine title the Psalter uses here. The psalm's praise of the Holy One of Israel is taken up in the NT as a title for Jesus."
      }
    ]
  },
  "72": {
    "1": [
      {
        "type": "type",
        "target": "Heb 1:8",
        "note": "Psalm 72 is a royal psalm praying for the ideal king — righteousness, universal dominion, lasting peace. The NT sees this as ultimately fulfilled only in Christ: Heb 1:8 quotes a cognate royal psalm ('Your throne, O God, is forever and ever') and applies it directly to the Son. Ps 72 is the benchmark against which every earthly king falls short and which Christ alone meets."
      }
    ],
    "8": [
      {
        "type": "fulfillment",
        "target": "Rev 11:15",
        "note": "Verse 8 — 'May he have dominion from sea to sea, and from the River to the ends of the earth' — is the prayer most directly answered in Rev 11:15: 'The kingdom of the world has become the kingdom of our Lord and of his Christ, and he shall reign forever and ever.' The OT prayer for the ideal king's universal reign finds its answer in the exaltation of the crucified and risen Christ."
      }
    ],
    "10": [
      {
        "type": "fulfillment",
        "target": "Matt 2:11",
        "note": "Verse 10 — 'May the kings of Sheba and Seba bring gifts' — was read by the early church as fulfilled when the Magi brought gold, frankincense, and myrrh to the infant Jesus (Matt 2:11). The scene deliberately evokes the tribute offered to Solomon and the ideal Davidic king; Matt 2 replays it at the manger."
      }
    ],
    "11": [
      {
        "type": "fulfillment",
        "target": "Phil 2:10",
        "note": "Verse 11 — 'May all kings fall down before him, all nations serve him' — is the eschatological vision Phil 2:10-11 presents as accomplished through the resurrection and exaltation: 'at the name of Jesus every knee should bow... and every tongue confess that Jesus Christ is Lord.' Paul's universal lordship claim answers Ps 72's universal kingship prayer."
      }
    ],
    "12": [
      {
        "type": "theme",
        "target": "Luke 4:18",
        "note": "Verses 12-13 — 'he delivers the needy when he calls, the poor and him who has no helper' — articulate the kingdom-criterion of care for the powerless. Jesus opens his public ministry by quoting Isa 61 (Luke 4:18), which expresses the same program; Ps 72's ideal king is the template Christ claims and embodies."
      }
    ],
    "17": [
      {
        "type": "fulfillment",
        "target": "Gal 3:8",
        "note": "Verse 17 — 'May all nations be blessed in him' — draws on the Abrahamic blessing formula (Gen 12:3; 22:18). Gal 3:8 identifies this promise as the Gospel preached beforehand to Abraham, fulfilled in Christ through whom the blessing reaches all nations. The royal psalm's refrain brings the Abrahamic covenant and the Messiah into one trajectory."
      }
    ],
    "18": [
      {
        "type": "theme",
        "target": "Rev 15:3",
        "note": "Verses 18-19 — the doxological close of Psalter Book II: 'Blessed be the LORD God... who alone does wondrous things.' This pattern of praise to the God who acts in history is taken up in Rev 15:3 ('Great and amazing are your deeds, O Lord God the Almighty!') as the song of those who conquer through the Lamb."
      }
    ]
  },
  "73": {
    "1": [
      {
        "type": "theme",
        "target": "Rom 8:28",
        "note": "Psalm 73 opens with the confession that 'God is good to Israel, to those who are pure in heart' — a thesis Asaph almost abandons when he sees the prosperity of the wicked. This is the same tension Paul resolves in Rom 8:28: 'all things work together for good for those who love God.' The psalmist's journey from crisis to confidence is the pastoral pattern the NT explicates."
      }
    ],
    "17": [
      {
        "type": "shadow",
        "target": "Heb 9:11",
        "note": "Verse 17 — 'until I went into the sanctuary of God; then I discerned their end' — marks the turning point: clarity comes only inside the sanctuary. Heb 9:11 presents Christ as having entered the greater and more perfect tent (the heavenly sanctuary), the ultimate locus where the meaning of suffering and judgment is revealed. Asaph's resolution inside the earthly sanctuary foreshadows the access to God's perspective that Christ opens."
      }
    ],
    "24": [
      {
        "type": "allusion",
        "target": "John 14:3",
        "note": "Verse 24 — 'You guide me with your counsel, and afterward you will receive me to glory' — expresses the hope of being taken to God's presence after death. John 14:3 is Jesus' direct promise of this: 'I will come again and will take you to myself, that where I am you may be also.' The psalmist's hope becomes Christ's explicit pledge to his disciples."
      }
    ],
    "25": [
      {
        "type": "theme",
        "target": "Phil 1:23",
        "note": "Verse 25 — 'Whom have I in heaven but you? And there is nothing on earth that I desire besides you' — is among the strongest expressions of single-minded devotion to God in the Psalter. Phil 1:23 places Paul in the same posture: 'my desire is to depart and be with Christ, for that is far better.' The psalm's language of total devotion becomes the NT language of union with Christ."
      }
    ],
    "26": [
      {
        "type": "theme",
        "target": "2 Cor 12:9",
        "note": "Verse 26 — 'My flesh and my heart may fail, but God is the strength of my heart and my portion forever' — names the dynamic Paul calls weakness made strong through Christ: 2 Cor 12:9 ('My grace is sufficient for you, for my power is made perfect in weakness'). Asaph's confession that God suffices when the self fails is the exact pattern of grace the NT applies to life in Christ."
      }
    ],
    "28": [
      {
        "type": "allusion",
        "target": "Heb 10:22",
        "note": "Verse 28 — 'it is good for me to be near God' — is the Psalter's declaration that closeness to God is the highest good. Heb 10:22 applies this to the new covenant: 'let us draw near with a true heart in full assurance of faith.' What Asaph declares as his personal resolve the NT declares as the birthright of all who approach through Christ's blood and the torn curtain."
      }
    ]
  },
  "74": {
    "2": [
      {
        "type": "allusion",
        "target": "Acts 20:28",
        "note": "Verse 2 — 'Remember your congregation, which you have purchased of old... your heritage, Mount Zion, where you have dwelt' — uses the redemption-purchase language later applied to the church. Acts 20:28 says God obtained the church 'with his own blood,' applying the same costly-acquisition vocabulary to Christ's atoning death. The redeemed assembly moves from Zion to the body of Christ."
      }
    ],
    "12": [
      {
        "type": "theme",
        "target": "John 18:36",
        "note": "Verse 12 — 'God is my King from of old, working salvation in the midst of the earth' — declares that divine kingship and salvation have always operated together at the center of human history. The NT makes this claim about Christ's crucifixion: it is not defeat but the central act of divine kingship. Jesus' words to Pilate in John 18:36 reframe but do not deny the cosmic sovereignty v12 announces."
      }
    ],
    "13": [
      {
        "type": "shadow",
        "target": "Rev 12:9",
        "note": "Verses 13-14 — 'You divided the sea... you crushed the heads of Leviathan' — use the ancient dragon-combat imagery which Rev 12:9 recasts as Satan, 'that ancient serpent,' cast down through Christ's victory. The crushing of Leviathan's heads anticipates the defeat of the serpent at the cross (Gen 3:15; Col 2:15)."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Heb 13:20",
        "note": "Verse 20 — 'Have regard for the covenant' — is the lament's appeal to God's binding self-commitment. Heb 13:20 answers this plea christologically: God has acted through 'the blood of the eternal covenant' in raising Jesus from the dead. The covenant Asaph calls God to remember is the one the resurrection vindicates and seals permanently in Christ."
      }
    ],
    "22": [
      {
        "type": "theme",
        "target": "Rev 19:2",
        "note": "Verse 22 — 'Arise, O God, defend your cause; remember how the foolish mock you all the day' — is the cry for divine vindication against those who blaspheme. Rev 19:2 presents the eschatological answer: God has judged the one 'who corrupted the earth... and has avenged on her the blood of his servants.' The same pattern of patient endurance followed by God's arising to judge runs from Ps 74 through to Revelation's throne-room scenes."
      }
    ]
  }
}


def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    print('Psalms 71-74 echoes written.')

if __name__ == '__main__':
    main()
