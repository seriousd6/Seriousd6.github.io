"""
Echo layer — Proverbs 7–9
Run: python3 scripts/zc-echo-proverbs-7-9.py

Ch7: The Strange Woman narrative — foil to Lady Wisdom; leads the naive to Sheol;
     key echoes: inscribed heart (Jer 31:33), ox-to-slaughter contrast (Isa 53:7),
     road to Sheol reversed (Rev 20:14; John 10:10)
Ch8: Lady Wisdom's pre-existence speech (vv22-31) — most Christologically dense passage
     in Proverbs; NT treats Wisdom as a type of Christ (Col 1:15-17; John 1:1-3; Heb 1:2);
     augments existing v22→John 1:1 entry with broader creation-presence echoes
Ch9: Wisdom's banquet vs. Folly's counterfeit banquet — structurally anticipates the
     Marriage Supper of the Lamb (Rev 19:9); bread-and-wine invitation anticipates
     both the Eucharist and John 6 (bread of life)
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

PROVERBS_ECHOES = {
  "7": {
    "3": [
      {
        "type": "allusion",
        "target": "Jer 31:33",
        "note": "The parental command to inscribe wisdom on the tablet of the heart anticipates YHWH's new covenant promise to write his law on the heart (Jer 31:33; Heb 8:10). The new covenant fulfills what parental instruction can only gesture toward — inward transformation by the Spirit rather than external command."
      }
    ],
    "22": [
      {
        "type": "shadow",
        "target": "Isa 53:7",
        "note": "The naive young man follows the seductive woman 'like an ox heading to slaughter' — unwitting, deceived, destroyed. The contrast with the Servant of Isa 53:7 is pointed: the Servant goes to slaughter willingly, not deceived but obedient, and his death is redemptive rather than self-destructive. The same slaughter image used of two radically different deaths."
      }
    ],
    "27": [
      {
        "type": "shadow",
        "target": "John 10:10",
        "note": "The Strange Woman's house as 'the road to Sheol' is the OT emblem of the thief who comes to kill and destroy (John 10:10). Christ presents himself as the antithesis: 'I came that they may have life and have it abundantly.' The descent into death through Folly is the foil against which Wisdom's (and Christ's) life-giving invitation stands."
      },
      {
        "type": "shadow",
        "target": "Rev 20:14",
        "note": "Sheol as the destination of those seduced by Folly points forward to the second death — death and Hades thrown into the lake of fire (Rev 20:14). Christ's resurrection is the decisive reversal of the Sheol trajectory; his descent into death and return destroys the road the Strange Woman represents."
      }
    ]
  },
  "8": {
    "22": [
      {
        "type": "allusion",
        "target": "Col 1:15",
        "note": "Paul's 'firstborn of all creation' (Col 1:15) and 'before all things' (Col 1:17) draw directly on Wisdom's claim to pre-creation existence in Prov 8:22-23. The NT applies to Christ the personal pre-existence that Proverbs ascribes to Wisdom."
      }
    ],
    "27": [
      {
        "type": "allusion",
        "target": "John 1:3",
        "note": "Wisdom's presence 'when he set the heavens in place' and role as master craftsman (v30) is the OT background for John's 'all things were made through him, and without him nothing was made' (John 1:3). The pre-existent Wisdom who delights in creation becomes the Logos through whom creation was made."
      },
      {
        "type": "allusion",
        "target": "Heb 1:2",
        "note": "Hebrews identifies the Son as the one 'through whom also he created the universe' — applying to Christ exactly the creative role that Wisdom claims in Prov 8:27-30. The &#8220;master craftsman&#8221; beside the Father becomes the Son through whom the Father speaks his creating word."
      }
    ],
    "30": [
      {
        "type": "allusion",
        "target": "Matt 3:17",
        "note": "Wisdom's description as the Father's 'daily delight' (MKT: 'I was his daily delight, rejoicing before him always') provides the OT vocabulary for the Father's declaration at Jesus's baptism: 'This is my beloved Son, in whom I am well pleased' (Matt 3:17; cf. Matt 17:5). The eternal delight of the Father in Wisdom finds its historical expression in the Father's declaration over the Son."
      }
    ],
    "31": [
      {
        "type": "shadow",
        "target": "John 1:14",
        "note": "Wisdom rejoicing 'in the world he had made' and finding 'delight in the children of humanity' shadows the Incarnation — the Word becoming flesh and dwelling among (tabernacling with) humanity (John 1:14). The delight that Wisdom has in humankind from eternity is enacted historically when Wisdom-made-flesh takes up residence among the people she delights in."
      }
    ],
    "35": [
      {
        "type": "allusion",
        "target": "John 14:6",
        "note": "'Whoever finds me finds life' is the Wisdom formula that Jesus applies to himself directly: 'I am the way, the truth, and the life. No one comes to the Father except through me' (John 14:6). Finding Wisdom = finding life; finding Christ = finding life. The identification of Christ with Wisdom makes these claims structurally identical."
      },
      {
        "type": "allusion",
        "target": "John 1:4",
        "note": "John's prologue: 'In him was life, and that life was the light of all mankind' — mapping Life directly onto the Logos/Wisdom figure. Prov 8:35 ('whoever finds me finds life') is the Wisdom antecedent that John's Logos-theology inherits and fulfills."
      }
    ],
    "36": [
      {
        "type": "shadow",
        "target": "John 3:18",
        "note": "'All who hate me embrace death' corresponds to John's statement that those who do not believe in the Son are already condemned, and that people loved darkness rather than light (John 3:18-19). Rejection of Wisdom = embracing death; rejection of Christ = the same trajectory, now named as judgment."
      }
    ]
  },
  "9": {
    "2": [
      {
        "type": "shadow",
        "target": "Matt 22:2",
        "note": "Wisdom slaughtering animals, mixing wine, and setting her table directly prefigures the Parable of the Wedding Banquet (Matt 22:2-14), where the king prepares a feast and sends out messengers to invite guests. Both follow the same invitation pattern: feast prepared → servants sent to call → invitation given to those on the road. The structural parallel identifies Christ as Wisdom's fulfillment."
      },
      {
        "type": "shadow",
        "target": "Luke 14:16",
        "note": "The Parable of the Great Banquet (Luke 14:16-24) is the second-closest parallel: a great feast prepared, servants sent, invitation given to all — the same Wisdom-banquet structure. Christ's parables about divine hospitality draw on this Proverbs 9 archetype."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "John 6:35",
        "note": "Wisdom's invitation 'Come and eat my bread; drink the wine I have mixed' (Prov 9:5) is the OT register behind Jesus's 'I am the bread of life; whoever comes to me shall not hunger, and whoever believes in me shall never thirst' (John 6:35). Jesus identifies himself as the fulfillment of Wisdom's banquet invitation."
      },
      {
        "type": "allusion",
        "target": "Matt 26:26",
        "note": "The bread-and-wine of Wisdom's feast (Prov 9:2,5) provides the Wisdom-of-God backdrop for the Last Supper institution (Matt 26:26-28; 1 Cor 11:23-26). When Christ takes bread and wine as his body and blood, he is claiming to be the host of the Wisdom banquet — the feast that Proverbs 9 describes."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "1 Cor 1:24",
        "note": "The declaration that the fear of YHWH is the beginning of wisdom (Prov 9:10; cf. 1:7) is fulfilled in Paul's identification of Christ as 'the power of God and the wisdom of God' (1 Cor 1:24). The beginning of wisdom is fear of YHWH; the consummation of wisdom is Christ himself — and knowing Christ is the fullest expression of the wisdom that begins in his fear."
      }
    ],
    "18": [
      {
        "type": "contrast",
        "target": "Rev 19:9",
        "note": "Dame Folly's banquet ends with her guests in the depths of Sheol (Prov 9:18); Wisdom's banquet ends with life. The eschatological antithesis is the Marriage Supper of the Lamb (Rev 19:9): 'Blessed are those who are invited to the marriage supper of the Lamb.' The two invitations of Proverbs 9 — Wisdom and Folly — find their ultimate resolution in the contrast between the Lamb's supper and the second death."
      }
    ]
  }
}

def main():
    existing = load_echo('proverbs')
    merge_echo(existing, PROVERBS_ECHOES)
    save_echo('proverbs', existing)
    ch_count = len(PROVERBS_ECHOES)
    v_count = sum(len(vv) for vv in PROVERBS_ECHOES.values())
    print(f'proverbs echoes ch7-9: {v_count} verses across {ch_count} chapters written')

if __name__ == '__main__':
    main()
