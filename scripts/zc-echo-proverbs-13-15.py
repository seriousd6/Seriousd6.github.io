"""
echo — Proverbs 13–15
Run: python3 scripts/zc-echo-proverbs-13-15.py
Key echoes: hope/tree of life (Rev 22:2; Rom 8:24), fountain of life (John 7:38; 4:14),
  discipline from love (Heb 12:6), way to death (John 14:6), poor man = Maker (Matt 25:40),
  omniscient eyes (Heb 4:13), sacrifice vs. prayer (Heb 10:4-10), Sheol (Rev 1:18).
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

PROVERBS_ECHOES = {
  "13": {
    "12": [
      {
        "type": "allusion",
        "target": "Rom 8:24",
        "note": "Hope deferred makes the heart sick, but a desire fulfilled is a tree of life — the OT wisdom tradition knew that longing unfulfilled is a form of suffering; Paul's description of hope as 'not seen' (Rom 8:24-25) and the groaning of creation awaiting adoption is the new covenant statement of the same condition: the saints of both testaments lived with deferred hope (Heb 11:39-40: these all died not having received the promises). Christ is the fulfillment that turns deferred hope into present joy."
      },
      {
        "type": "allusion",
        "target": "Rev 22:2",
        "note": "A desire fulfilled is a tree of life — the tree of life, lost in Eden (Gen 3:22-24), reappears in Proverbs as an image of fulfilled longing and flourishing; Revelation 22:2 restores it to the center of the new creation city: 'the tree of life with its twelve kinds of fruit, yielding its fruit each month.' The fulfilled desire of Proverbs 13:12 is the eschatological abundance of Christ's restored kingdom."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "John 7:38",
        "note": "The teaching of the wise is a fountain of life, that one may turn away from the snares of death — Wisdom's instruction figured as living water; Jesus at the Feast of Tabernacles: 'Whoever believes in me, as the Scripture has said, out of his heart will flow rivers of living water' (John 7:38). The fountain that gives life and averts death in Proverbs becomes the Spirit whom Christ pours out — the fountainhead is no longer a wise teacher's words but Christ himself."
      }
    ],
    "24": [
      {
        "type": "allusion",
        "target": "Heb 12:6",
        "note": "Whoever spares the rod hates his son, but he who loves him is diligent to discipline him — the equation of loving discipline with parental love; Hebrews 12:6 quotes Proverbs 3:11-12 (the parallel passage) to ground God's discipline of believers as fatherly love: 'the Lord disciplines the one he loves.' Both Proverbs 13:24 and Hebrews 12 make the same argument: the presence of discipline is evidence of love, and the Son of God himself 'learned obedience through what he suffered' (Heb 5:8)."
      }
    ]
  },
  "14": {
    "12": [
      {
        "type": "allusion",
        "target": "John 14:6",
        "note": "There is a way that seems right to a man, but its end is the way to death — Proverbs' warning about human self-direction; Jesus's claim 'I am the way, the truth, and the life; no one comes to the Father except through me' (John 14:6) is the direct answer: the only alternative to the way-that-seems-right-but-leads-to-death is the one who is himself the Way. The wide way of Matthew 7:13 is Proverbs 14:12 made concrete."
      }
    ],
    "27": [
      {
        "type": "allusion",
        "target": "John 4:14",
        "note": "The fear of the LORD is a fountain of life, that one may turn away from the snares of death — the same image as Proverbs 13:14 but rooted explicitly in the fear of YHWH; Jesus to the Samaritan woman: 'the water that I will give him will become in him a spring of water welling up to eternal life' (John 4:14). The fountain-of-life that is the fear of YHWH in Proverbs becomes a personal spring that Christ gives — the gift is now a person, and 'turning away from the snares of death' is eternal life."
      }
    ],
    "31": [
      {
        "type": "allusion",
        "target": "Matt 25:40",
        "note": "Whoever oppresses a poor man insults his Maker, but he who is generous to the needy honors him — the Creator-dignity of every human being grounds the ethics of generosity; Jesus makes this explicit in the judgment scene: 'whatever you did to one of the least of these brothers of mine, you did to me' (Matt 25:40). The connection between treatment of the poor and treatment of God that Proverbs establishes becomes, in Christ, a literal identification: the Son of Man is the poor man."
      }
    ]
  },
  "15": {
    "3": [
      {
        "type": "allusion",
        "target": "Heb 4:13",
        "note": "The eyes of the LORD are in every place, keeping watch on the evil and the good — divine omniscience as a moral constant in Proverbs; Hebrews 4:13 intensifies this: 'no creature is hidden from his sight, but all are naked and exposed to the eyes of him to whom we must give account.' The Proverbs verse grounds ethics in divine observation; Hebrews focuses it eschatologically on the account we give to Christ the judge."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Heb 10:8",
        "note": "The sacrifice of the wicked is an abomination to the LORD, but the prayer of the upright is his delight — the primacy of heart-posture over ritual; Hebrews 10:8 quotes the Psalter's parallel: 'sacrifices and offerings you have not desired.' Christ's self-offering replaces the inadequate sacrificial system entirely; the prayer of the upright that Proverbs celebrates becomes, in the new covenant, intercession offered through Christ (Heb 10:19-22: we draw near with a true heart in full assurance of faith)."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Rev 1:18",
        "note": "Sheol and Abaddon lie open before the LORD; how much more the hearts of the children of man! — even the realm of the dead is transparent to God's gaze; the risen Christ extends this: 'I have the keys of Death and Hades' (Rev 1:18). What Proverbs describes as divine omniscience over the underworld, Revelation presents as Christ's active authority — he not only sees Sheol, he holds its keys."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "Matt 16:26",
        "note": "Better is a little with the fear of the LORD than great treasure and trouble with it — the wisdom tradition's persistent valuation of God-relationship above material wealth; Jesus makes this absolute: 'what will it profit a man if he gains the whole world and forfeits his soul?' (Matt 16:26). Proverbs 15:16 says little + fear of the LORD > great treasure; Jesus says the entire world is not worth the soul — the principle is the same, the stakes are raised to eternity."
      }
    ]
  }
}

def main():
    existing = load_echo('proverbs')
    merge_echo(existing, PROVERBS_ECHOES)
    save_echo('proverbs', existing)
    print('proverbs echo: wrote ch13-15 entries (10 verse connections)')

if __name__ == '__main__':
    main()
