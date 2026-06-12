"""
Echo layer — Proverbs 31
Run: python3 scripts/zc-echo-proverbs-31-31.py

Two sections:
- vv1-9: King Lemuel's mother's teaching — justice for the afflicted, wine for the perishing;
  key echoes: wine-for-the-perishing (→ Matt 27:34 gall/vinegar at crucifixion),
  opening the mouth for the mute (→ Isa 35:6 / Matt 9:32-33),
  righteous judgment for the poor (→ Isa 11:4 / John 5:30)
- vv10-31: Eshet Chayil (Woman of Valor) — the acrostic ideal-wife poem;
  key echoes: the bride of Christ (→ Rev 19:7-9; Eph 5:25-27),
  wisdom-speech (→ Col 3:16), fear-of-YHWH conclusion (→ 1 Pet 3:3-4),
  works-follow (→ Rev 14:13; Heb 6:10)
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
  "31": {
    "6": [
      {
        "type": "shadow",
        "target": "Matt 27:34",
        "note": "The command to give wine to the one who is perishing casts light on the wine-mixed-with-gall offered to Christ at the crucifixion (Matt 27:34; cf. Ps 69:21). The irony is complete: the one who came to give living water to the perishing (John 4:14) is himself offered bitter drink as he bears the condition of the perishing. He refuses the numbing gall but accepts the vinegar (John 19:28-30) to fulfill his mission to the end."
      }
    ],
    "8": [
      {
        "type": "shadow",
        "target": "Isa 35:5",
        "note": "The command to &#8220;open your mouth for the mute&#8221; is fulfilled in Christ's Messianic signs: Isaiah promises that in the day of salvation &#8220;the tongue of the mute will shout for joy&#8221; (Isa 35:6), and the Gospels record Jesus healing the mute as a sign of the kingdom's arrival (Matt 9:32-33; Mark 7:32-37). The royal advocate for the voiceless anticipated by Proverbs 31 is realized in Jesus."
      }
    ],
    "9": [
      {
        "type": "shadow",
        "target": "Isa 11:4",
        "note": "The ideal king judges righteously and defends the poor and needy — the exact terms of Isaiah's Messianic Branch: &#8220;he will judge the poor with righteousness and decide with fairness for the afflicted of the earth&#8221; (Isa 11:4). Jesus claims this authority: &#8220;I can do nothing on my own. As I hear, I judge, and my judgment is just&#8221; (John 5:30). The mother's instruction to King Lemuel names the justice that Christ embodies."
      }
    ],
    "10": [
      {
        "type": "shadow",
        "target": "Eph 5:25",
        "note": "&#8220;An excellent wife — who can find her?&#8221; — the rhetorical question about a rare prize. In Ephesians Paul uses the husband-wife relationship as the primary analogy for Christ and the church (Eph 5:25-27): Christ as the husband who loves, cherishes, and presents the church to himself &#8220;in splendor, without spot or wrinkle.&#8221; The Eshet Chayil passage is the OT archetype that Paul's church-as-bride language fulfills."
      }
    ],
    "20": [
      {
        "type": "shadow",
        "target": "Matt 25:35",
        "note": "The woman of valor who &#8220;opens her hand to the poor and extends her hands to the needy&#8221; embodies the righteousness that Christ identifies with himself in the sheep-and-goats parable: &#8220;whatever you did for one of the least of these brothers and sisters of mine, you did for me&#8221; (Matt 25:35,40). The Eshet Chayil's generosity is the pattern for kingdom citizenship."
      }
    ],
    "22": [
      {
        "type": "shadow",
        "target": "Rev 19:8",
        "note": "The woman of valor clothed in &#8220;fine linen and purple&#8221; anticipates the bridal imagery of Revelation: &#8220;Fine linen, bright and clean, was given her to wear&#8221; and the linen is glossed as &#8220;the righteous acts of God's holy people&#8221; (Rev 19:8). The Eshet Chayil's honorable dress is the type of the church's eschatological clothing — righteousness that is both imputed and lived."
      }
    ],
    "26": [
      {
        "type": "allusion",
        "target": "Col 3:16",
        "note": "&#8220;She opens her mouth with wisdom, and faithful instruction (<em>tôrat ḥeseḏ</em>) is on her tongue.&#8221; Paul's command &#8220;let the word of Christ dwell in you richly, teaching and admonishing one another in all wisdom&#8221; (Col 3:16) is the NT form of the same ideal — wisdom-speech that builds up. The woman of valor as teacher of Torah is the OT prototype for the Spirit-equipped teacher of the new covenant."
      }
    ],
    "30": [
      {
        "type": "allusion",
        "target": "1 Pet 3:3",
        "note": "The Eshet Chayil's climax contrasts outward beauty with the fear of YHWH: &#8220;charm is deceptive and beauty is fleeting, but a woman who fears the LORD is to be praised.&#8221; Peter applies this reversal directly: outward adornment is not what counts; rather &#8220;the hidden person of the heart with the imperishable beauty of a gentle and quiet spirit&#8221; is precious in God's sight (1 Pet 3:3-4). Peter's instruction draws on this exact Proverbs contrast."
      }
    ],
    "31": [
      {
        "type": "allusion",
        "target": "Rev 14:13",
        "note": "&#8220;Give her the fruit of her hands, and let her works praise her in the gates&#8221; — the divine vindication of faithful labor. Revelation 14:13 pronounces the same blessing eschatologically: &#8220;Blessed are the dead who die in the Lord... their deeds will follow them.&#8221; The works that praise the woman of valor in Proverbs&#8217; gates are the deeds that follow the saints into eternity. Heb 6:10 echoes the same assurance: &#8220;God is not unjust; he will not forget your work.&#8221;"
      }
    ]
  }
}

def main():
    existing = load_echo('proverbs')
    merge_echo(existing, PROVERBS_ECHOES)
    save_echo('proverbs', existing)
    v_count = sum(len(vv) for vv in PROVERBS_ECHOES.values())
    print(f'proverbs echoes ch31: {v_count} verses written')

if __name__ == '__main__':
    main()
