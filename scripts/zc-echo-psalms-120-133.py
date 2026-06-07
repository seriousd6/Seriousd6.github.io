"""
Echo data — Psalms chapters 120–133 (gap-fill: chs 120–129, 131, 133 missing; 130, 132 already present)
Run: python3 scripts/zc-echo-psalms-120-133.py

These are the Songs of Ascents (Ps 120–134), sung by pilgrims ascending to Jerusalem
for the three annual feasts (Passover, Weeks, Booths). They form a liturgical unit
expressing longing for God's house, trust in the LORD's protection, and hope for
Jerusalem's restoration.

Key connections:
- Ps 121:4: "He who watches over Israel will neither slumber nor sleep" → Heb 7:25
  (Christ always lives to intercede — the eternal watchkeeper).
- Ps 122:1: "I rejoiced with those who said to me, 'Let us go to the house of the LORD'"
  → John 2:17 / Heb 10:25.
- Ps 122:6: "Pray for the peace of Jerusalem" → Heb 12:22 / Rev 21:2 (heavenly Jerusalem).
- Ps 124:8: "Our help is in the name of the LORD" → Acts 4:12 (salvation in no other name).
- Ps 125:1: "Those who trust in the LORD are like Mount Zion which cannot be shaken"
  → Heb 12:28 (a kingdom that cannot be shaken).
- Ps 126:5-6: "Those who sow in tears will reap with songs of joy" → John 16:20
  (your grief will turn to joy).
- Ps 127:1: "Unless the LORD builds the house, the builders labor in vain" →
  1 Cor 3:11 (no one can lay a foundation other than the one already laid — Christ).
- Ps 129:4: "The LORD is righteous; he has cut me free from the cords of the wicked"
  → Col 1:13 (rescued us from the dominion of darkness).
- Ps 131:2: "Like a weaned child with its mother; like a weaned child I am content"
  → Matt 18:3 (become like little children) / Phil 4:11 (I have learned contentment).
- Ps 133:1: "How good and pleasant it is when God's people live together in unity"
  → John 17:21 (that they all may be one, as you, Father, are in me).
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

# INTENT: Echo data for Songs of Ascents (Ps 120–133), targeting 12 missing chapters.
#   The Songs of Ascents were pilgrimage psalms; their themes of ascending to God's house,
#   divine protection, unity, and restoration find NT fulfillment in Christ as the true
#   temple (John 2:19-21), the eternal keeper (Heb 7:25), and the foundation of God's
#   household (1 Cor 3:11). The unity prayer of Ps 133 finds its highest form in Jesus'
#   high-priestly prayer (John 17:21).
# CHANGE? If data/echoes/psalms.json structure changes, update load_echo/save_echo
#   per Z_COMMENTARY_SCRIPT_GUIDE.md.
# VERIFY: python3 -c "import json; d=json.load(open('data/echoes/psalms.json')); print([len(d.get(str(c),{})) for c in range(120,134)])" should show non-zero for all 14.

PSALMS_ECHOES = {
  "120": {
    "7": [
      {
        "type": "allusion",
        "target": "Matt 10:34",
        "note": "I am for peace; but when I speak, they are for war — 'Do not suppose that I have come to bring peace to the earth. I did not come to bring peace, but a sword' (Matt 10:34). The Psalmist's experience of being for peace and encountering only war is the condition Christ acknowledges for his followers. He himself is the Prince of Peace (Isa 9:6) whose coming provokes hostility in those committed to violence — Psalm 120:7's lament is the pilgrimage condition of those who follow the way of peace in a world that chooses war."
      }
    ]
  },
  "121": {
    "4": [
      {
        "type": "allusion",
        "target": "Heb 7:25",
        "note": "He who watches over Israel will neither slumber nor sleep — 'therefore he is able to save completely those who come to God through him, because he always lives to intercede for them' (Heb 7:25). The unwearying divine watchkeeper of Psalm 121:4 is fulfilled in Christ's perpetual intercession — he is the keeper who never sleeps because he is the one who passed through death and lives permanently on the other side. His intercession is not periodic prayer but constant watchfulness: 'always lives' (Heb 7:25) is the NT form of 'will neither slumber nor sleep.'"
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "John 10:9",
        "note": "The LORD will watch over your coming and going both now and forevermore — 'I am the gate; whoever enters through me will be saved. They will come in and go out, and find pasture' (John 10:9). The LORD's guardianship of going out and coming in (Ps 121:8) — a comprehensive Hebraic idiom for all of life's movement — is enacted by Christ as the gate. Those who enter through him find protection in their going out and coming in, and the 'forevermore' of the Psalm is the 'I am' of John — the eternal guardian."
      }
    ]
  },
  "122": {
    "1": [
      {
        "type": "allusion",
        "target": "John 2:17",
        "note": "I rejoiced with those who said to me, 'Let us go to the house of the LORD' — 'his disciples remembered that it is written: \"Zeal for your house will consume me\"' (John 2:17). The pilgrimage joy of ascending to the LORD's house (Ps 122:1) and the consuming zeal for God's house (Ps 69:9, cited at the Temple cleansing) both point to Christ's passion for the place of divine presence. The pilgrim song of going to the house of the LORD reaches its fullest expression in Christ, who is himself that house (John 2:19-21: 'Destroy this temple, and I will raise it again in three days')."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Heb 12:22",
        "note": "Pray for the peace of Jerusalem — 'but you have come to Mount Zion, to the city of the living God, the heavenly Jerusalem. You have come to thousands upon thousands of angels in joyful assembly' (Heb 12:22). The prayer for Jerusalem's peace (Ps 122:6) finds its NT horizon in the heavenly Jerusalem of Hebrews — the city that is already the dwelling of the living God, accessible through Christ the mediator (Heb 12:24). Rev 21:2: the new Jerusalem coming down from heaven, in which God will dwell permanently with his people. The peace prayed for in the earthly city is the peace that the new Jerusalem will permanently embody."
      }
    ]
  },
  "123": {
    "2": [
      {
        "type": "allusion",
        "target": "John 15:5",
        "note": "As the eyes of slaves look to the hand of their master, as the eyes of a female slave look to the hand of her mistress, so our eyes look to the LORD our God, till he shows us his mercy — 'I am the vine; you are the branches. If you remain in me and I in you, you will bear much fruit; apart from me you can do nothing' (John 15:5). The posture of Psalm 123:2 — eyes fixed on the master, waiting on his provision, doing nothing apart from his direction — is the posture Jesus describes for abiding in him. Complete dependency on the master's hand is the form of life that connects to Christ."
      }
    ]
  },
  "124": {
    "8": [
      {
        "type": "allusion",
        "target": "Acts 4:12",
        "note": "Our help is in the name of the LORD, the Maker of heaven and earth — 'salvation is found in no one else, for there is no other name under heaven given to mankind by which we must be saved' (Acts 4:12). The exclusive help and deliverance found in the LORD's name (Ps 124:8) is what Peter declares located in the name of Jesus — the name above every name (Phil 2:9). The Psalm's declaration that the Maker of heaven and earth is Israel's helper finds its NT concentration in the risen Christ, through whom alone the help of the Maker reaches those who call."
      }
    ]
  },
  "125": {
    "1": [
      {
        "type": "allusion",
        "target": "Heb 12:28",
        "note": "Those who trust in the LORD are like Mount Zion, which cannot be shaken, which endures forever — 'therefore, since we are receiving a kingdom that cannot be shaken, let us be thankful, and so worship God acceptably with reverence and awe' (Heb 12:28). The unshakeable stability of those who trust in the LORD (Ps 125:1) is the kingdom that Hebrews declares believers are receiving through Christ. The shakeability of all earthly structures (Heb 12:26-27: God will shake earth and heaven) contrasts with the unshakeable kingdom — the Psalm's image of the unmovable mountain is the image of what Christ's kingdom is."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Matt 7:14",
        "note": "But those who turn to crooked ways the LORD will banish with the evildoers — 'but small is the gate and narrow the road that leads to life, and only a few find it' (Matt 7:14). Psalm 125:5's distinction between those who trust in the LORD and those who turn to crooked ways parallels Christ's narrow-road/broad-road teaching. The final result — the LORD banishes those who choose crooked paths — is the same end that awaits those who take the broad road: exclusion from the peace that ends the Psalm (v5b: 'Peace be on Israel')."
      }
    ]
  },
  "126": {
    "5": [
      {
        "type": "allusion",
        "target": "John 16:20",
        "note": "Those who sow in tears will reap with songs of joy — 'very truly I tell you, you will weep and mourn while the world rejoices. You will grieve, but your grief will turn to joy' (John 16:20). The harvest pattern of Psalm 126:5-6 — sorrow at sowing, joy at reaping — is the eschatological rhythm Jesus applies to the disciples in the passion discourse. The tears of going out bearing seed are the grief of Holy Saturday; the songs of reaping are the joy of resurrection morning. The Psalm's pattern becomes the template for discipleship: suffering before glory, cross before crown."
      }
    ]
  },
  "127": {
    "1": [
      {
        "type": "allusion",
        "target": "1 Cor 3:11",
        "note": "Unless the LORD builds the house, the builders labor in vain. Unless the LORD watches over the city, the guards stand watch in vain — 'for no one can lay any foundation other than the one already laid, which is Jesus Christ' (1 Cor 3:11). Paul's building metaphor (1 Cor 3:9-11) applies Psalm 127:1's principle directly: the builders labor in vain unless God builds, and God has already laid the foundation — Christ himself. The Psalm's wisdom about futile human construction without divine agency becomes Paul's theology of the church: only the building whose foundation and builder is Christ will stand."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "Matt 11:28",
        "note": "In vain you rise early and stay up late, toiling for food to eat — for he grants sleep to those he loves — 'come to me, all you who are weary and burdened, and I will give you rest' (Matt 11:28). The anxious, sleepless toiling that Psalm 127:2 declares futile is the burden Christ invites the weary to lay down. God's gift of sleep to his beloved (the one who trusts and rests rather than anxiously striving) is the rest Christ offers — the yoke that is easy, the burden that is light. The LORD who gives sleep is the Christ who gives rest."
      }
    ]
  },
  "128": {
    "5": [
      {
        "type": "allusion",
        "target": "Gal 4:26",
        "note": "May the LORD bless you from Zion; may you see the prosperity of Jerusalem all the days of your life — 'but the Jerusalem that is above is free, and she is our mother' (Gal 4:26). The blessing from Zion and the prosperity of Jerusalem that Psalm 128:5 envisions as the ideal for the God-fearer are the blessings that Paul, in Galatians 4, locates in the heavenly Jerusalem — the mother-city of all who are born of the Spirit. The pilgrimage Psalm's vision of a blessed life connected to Jerusalem is fulfilled in the believer's connection to the Jerusalem above, from which all covenant blessings flow through Christ."
      }
    ]
  },
  "129": {
    "4": [
      {
        "type": "allusion",
        "target": "Col 1:13",
        "note": "The LORD is righteous; he has cut me free from the cords of the wicked — 'for he has rescued us from the dominion of darkness and brought us into the kingdom of the Son he loves, in whom we have redemption, the forgiveness of sins' (Col 1:13-14). The divine liberation from the cords of the wicked (Ps 129:4) is the image that captures the NT doctrine of rescue from spiritual bondage. Israel's experience of being cut free from oppressors becomes the template for the rescue Paul describes: from the dominion of darkness, its cords cut by the cross, into the kingdom of God's Son."
      }
    ]
  },
  "131": {
    "2": [
      {
        "type": "allusion",
        "target": "Matt 18:3",
        "note": "I have calmed and quieted my soul; like a weaned child with its mother, like a weaned child I am content — 'truly I tell you, unless you change and become like little children, you will never enter the kingdom of heaven' (Matt 18:3). The posture of Psalm 131:2 — the calmed, quieted soul that has ceased grasping and is content to rest in God's presence like a child — is the posture Jesus identifies as the condition for kingdom entry. Phil 4:11: 'I have learned, in whatever state I am, to be content.' The soul's quiet resting, not its striving, is the image of kingdom life."
      }
    ]
  },
  "133": {
    "1": [
      {
        "type": "allusion",
        "target": "John 17:21",
        "note": "How good and pleasant it is when God's people live together in unity — 'that all of them may be one, Father, just as you are in me and I am in you. May they also be in us so that the world may believe that you have sent me' (John 17:21). The beauty of brotherly unity that Psalm 133:1 celebrates reaches its theological depth in Jesus' high-priestly prayer: the unity of God's people is patterned on the unity of the Father and Son, and it is the apologetic demonstration that the Father sent the Son. The Psalm's aesthetic and liturgical delight in unity becomes, in John 17, a Trinitarian reality and a missiological imperative."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "John 10:10",
        "note": "There the LORD bestows his blessing, even life forevermore — 'I have come that they may have life, and have it to the full' (John 10:10). The blessing at Zion's completion — life forevermore (Ps 133:3) — is the life Christ declares he came to give. The unity blessed by God in Psalm 133 produces life in its fullest form; the community gathered under Christ experiences what Zion was always meant to provide. The dew of Hermon descending on Zion is the image of divine overflow — life abundant beyond what was asked or expected."
      }
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    for ch in range(120, 134):
        entries = len(existing.get(str(ch), {}))
        print(f"  ch{ch}: {entries} verses with entries")
    print("Psalms 120-133 echoes complete.")

if __name__ == '__main__':
    main()
