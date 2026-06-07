"""
Echo data — Psalms chapters 55–61
Run: python3 scripts/zc-echo-psalms-55-61.py

Key connections:
- Ps 55:12-14,21: The trusted companion's betrayal with smooth words → Judas
  (Matt 26:47-49; John 13:18). Ps 55:22 → 1 Pet 5:7 (cast your anxiety on him).
- Ps 56:3-4: "What can a mere human being do to me?" → Heb 13:6 (explicit cite);
  v8 tears in wineskin → Rev 21:4; v13 walk in light of the living → John 8:12.
- Ps 57:1: Shadow of wings → Matt 23:37 (Christ gathering children like a hen);
  v5/11 "Be exalted above the heavens" → Phil 2:9; v9 praise among nations → Rom 15:9.
- Ps 58:11: "There is a God who judges the earth" → Rev 16:7 divine judgment vindicated.
- Ps 59:16: Morning-praise pattern → the resurrection morning.
- Ps 60:4: Banner for the peoples → Isa 11:10 / John 3:14 cross lifted up;
  v7 "Judah is my scepter" → Gen 49:10 / Rev 5:5 Lion of Judah.
- Ps 61:2: "Rock that is higher than I" → 1 Cor 10:4 (Christ the Rock);
  v6-7: King whose days are extended forever → Luke 1:33 eternal kingdom.
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

# INTENT: Echo data for Psalms 55–61 covering the betrayal-by-companion (Ps 55 →
#   Judas), the "What can humans do to me?" faith anchor (Ps 56 → Heb 13:6),
#   shelter under divine wings (Ps 57 → Matt 23:37), the divine judge vindicated
#   (Ps 58 → Rev 16:7), the banner lifted for the nations (Ps 60 → John 3:14),
#   and the Rock higher than I (Ps 61 → 1 Cor 10:4).
# CHANGE? If data/echoes/psalms.json structure changes, update load_echo/save_echo
#   per Z_COMMENTARY_SCRIPT_GUIDE.md.
# VERIFY: python3 -c "import json; d=json.load(open('data/echoes/psalms.json')); print([len(d.get(str(c),{})) for c in range(55,62)])" should show non-zero for all.

PSALMS_ECHOES = {
  "55": {
    "13": [
      {
        "type": "fulfillment",
        "target": "John 13:18",
        "note": "But it is you — a person like me, my companion, the one I confided in; we shared deep, sweet conversation together — 'He who shared my bread has turned against me' (John 13:18, citing Ps 41:9, but Psalm 55:13-14 is the fuller expression). The trusted companion who shared covenant fellowship and then betrayed is the type of Judas who ate with Jesus at the Last Supper and then led the arrest party. John 6:70-71: 'Have I not chosen you, the Twelve? Yet one of you is a devil!'"
      }
    ],
    "21": [
      {
        "type": "fulfillment",
        "target": "Matt 26:49",
        "note": "His words were smoother than butter, yet war was in his heart; his speech was softer than oil, but it was all drawn swords — 'Going at once to Jesus, Judas said, \"Greetings, Rabbi!\" and kissed him' (Matt 26:49). The smooth words that conceal betrayal — Psalm 55:21's oil-smooth speech that is really drawn swords — is the prophetic description of Judas's greeting. The kiss of betrayal is the embodiment of 'smoother than butter, yet war in his heart.'"
      }
    ],
    "22": [
      {
        "type": "fulfillment",
        "target": "1 Pet 5:7",
        "note": "Throw your burden onto the LORD, and he will hold you up — 'Cast all your anxiety on him because he cares for you' (1 Pet 5:7). Peter's pastoral command is the NT application of Psalm 55:22 — the Psalm's imperative becomes the apostolic instruction. The one who can receive the thrown burden is identified in 1 Peter as the God who demonstrates his care through Christ's suffering and resurrection (1 Pet 2:21-24)."
      }
    ]
  },
  "56": {
    "3": [
      {
        "type": "allusion",
        "target": "Heb 13:6",
        "note": "When I am afraid, I will put my trust in you — 'The Lord is my helper; I will not be afraid. What can mere mortals do to me?' (Heb 13:6, citing Ps 118:6 but parallel to Ps 56:4). The formula 'trust in God → no fear of humans' is the same in both psalms and finds its NT grounding in Hebrews in the context of contentment and divine sufficiency. Rom 8:31: 'If God is for us, who can be against us?' — the same logical pattern."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Rev 21:4",
        "note": "Store my tears in your wineskin — are they not written in your book? — 'He will wipe every tear from their eyes. There will be no more death or mourning or crying or pain' (Rev 21:4). The tears that God stores and records in Psalm 56:8 will be personally wiped away by God in the new creation. The divine care for every tear — remembering, storing, recording — reaches its fulfillment in the eschatological act of divine comfort."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "John 8:12",
        "note": "You have saved my life from death, so that I may walk before God in the light that belongs to the living — 'I am the light of the world. Whoever follows me will never walk in darkness, but will have the light of life' (John 8:12). The 'light that belongs to the living' (Ps 56:13) is the light Christ embodies and gives — the resurrection light that is the opposite of death's darkness. Walking before God in the light of the living is the walking in the light that John describes in 1 John 1:7."
      }
    ]
  },
  "57": {
    "1": [
      {
        "type": "allusion",
        "target": "Matt 23:37",
        "note": "In the shadow of your wings I will take shelter until the storms of destruction pass — 'Jerusalem, Jerusalem... how often I have longed to gather your children together, as a hen gathers her chicks under her wings, but you were not willing' (Matt 23:37). Jesus applies the divine-wings shelter image of Psalm 57:1 to himself as the one offering refuge. Christ presents himself as the embodiment of the sheltering God — the one under whose wings the Psalmist takes refuge is the one Jesus claims to be."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Phil 2:9",
        "note": "Be exalted above the heavens, O God; let your glory be over all the earth — 'therefore God exalted him to the highest place and gave him the name that is above every name' (Phil 2:9). The prayer for divine exaltation above the heavens and glory over all the earth (Ps 57:5, 11) is fulfilled in the resurrection-exaltation of Christ. The repeated refrain of Psalm 57 becomes the NT's declaration of what has occurred: God has exalted him above the heavens."
      }
    ],
    "9": [
      {
        "type": "fulfillment",
        "target": "Rom 15:9",
        "note": "I will give you thanks, O Lord, among the peoples; I will sing your praise among the nations — Paul quotes the parallel verse in Psalm 18:49 in Romans 15:9 as a prophecy of Christ's Gentile mission: 'Therefore I will praise you among the Gentiles; I will sing the praises of your name.' The Psalm's praise among the nations is fulfilled in Christ who 'has become a servant of the Jews on behalf of God's truth' so that 'the Gentiles might glorify God' (Rom 15:8-9). The nations' worship of YHWH is accomplished through Christ."
      }
    ]
  },
  "58": {
    "3": [
      {
        "type": "allusion",
        "target": "Rom 3:23",
        "note": "The wicked are alienated from the womb; from their very birth they go astray — 'for all have sinned and fall short of the glory of God' (Rom 3:23). Paul's universal indictment of human sinfulness in Romans 3 draws on multiple Psalms (including Ps 14, 36, 140) and the same theological reality that Psalm 58:3 expresses: the radical depravity that begins from birth. Eph 2:3: 'we were by nature children of wrath' — the Psalm's womb-to-grave sinfulness is the OT form of the NT's doctrine of original sin."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Rev 16:7",
        "note": "Then people will say, 'There really is a reward for the righteous; truly there is a God who judges the earth' — 'Yes, Lord God Almighty, true and just are your judgments' (Rev 16:7). The vindication of divine justice that Psalm 58:11 anticipates — the moment when even the world acknowledges that God is truly just — is the affirmation the heavenly altar makes in the bowl-judgment sequence of Revelation. The world's forced acknowledgment of divine justice is the fulfillment of the Psalm's anticipation."
      }
    ]
  },
  "59": {
    "8": [
      {
        "type": "allusion",
        "target": "Ps 2:4",
        "note": "But you, LORD, laugh at them; you scoff at all the nations — 'the One enthroned in heaven laughs; the Lord scoffs at them' (Ps 2:4). The divine laughter at the nations' rage in Psalm 59:8 is the same image as Psalm 2:4 — the enthroned God who is utterly untroubled by human opposition. Acts 4:25-26 quotes Psalm 2 in reference to the opposition against Christ, making the divine laughter the Father's response to the crucifixion's apparent triumph of the nations over the Anointed."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "Mark 1:35",
        "note": "I will sing aloud of your steadfast love in the morning; for you have been my fortress and my place of refuge in my day of distress — 'very early in the morning, while it was still dark, Jesus got up, left the house and went off to a solitary place, where he prayed' (Mark 1:35). The morning-praise pattern of Psalm 59:16 is the pattern Jesus enacts — rising before dawn to meet with the Father. The morning of the resurrection (John 20:1) is the ultimate morning-praise, when God's steadfast love breaks through the night of crucifixion grief."
      }
    ]
  },
  "60": {
    "4": [
      {
        "type": "allusion",
        "target": "Isa 11:10",
        "note": "You have set up a banner for those who fear you, for them to rally to — 'In that day the Root of Jesse will stand as a banner for the peoples; the nations will rally to him' (Isa 11:10). The banner that God sets up in Psalm 60:4 is the messianic banner of Isaiah — the Root of Jesse to whom all nations rally. John 3:14-15: 'as Moses lifted up the snake in the wilderness, so the Son of Man must be lifted up, that everyone who believes may have eternal life in him' — the cross as the lifted banner."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Heb 1:3",
        "note": "Save your dear ones — rescue them by your right hand — 'after he had provided purification for sins, he sat down at the right hand of the Majesty in heaven' (Heb 1:3). The rescue 'by your right hand' (Ps 60:5) is accomplished through the one who sits at the right hand — the risen Christ who intercedes and saves from the position of ultimate divine authority (Heb 7:25; Rom 8:34)."
      }
    ],
    "7": [
      {
        "type": "type",
        "target": "Rev 5:5",
        "note": "Judah is my scepter — 'Weep no more; behold, the Lion of the tribe of Judah, the Root of David, has conquered, so that he can open the scroll and its seven seals' (Rev 5:5). The scepter that belongs to Judah (Ps 60:7; Gen 49:10) is the royal authority that Christ exercises as the Lion-Lamb from the tribe of Judah. Heb 7:14: 'it is clear that our Lord descended from Judah' — the tribal identity that the Psalm declares as carrying the scepter is the tribal identity that Christ bears."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "Rom 16:20",
        "note": "Through God we will do great deeds; he himself will crush our enemies — 'the God of peace will soon crush Satan under your feet' (Rom 16:20). Paul's promise to the Roman church echoes the Psalm's confidence that God will crush the enemies of his people. The enemies of Psalm 60:12 reach their eschatological fulfillment in the defeat of Satan — the crushing accomplished through the cross (Col 2:15) and completed at the end (Rev 20:10)."
      }
    ]
  },
  "61": {
    "2": [
      {
        "type": "allusion",
        "target": "1 Cor 10:4",
        "note": "Lead me to the rock that is higher than I — 'they drank from the spiritual rock that accompanied them, and that rock was Christ' (1 Cor 10:4). The rock that is higher than the Psalmist, to which he prays to be led, is the Christ who is identified as the Rock by Paul. Matt 16:18: 'on this rock I will build my church' — the rock that is higher than Peter's human confession is the Christ on whom the church is built. The 'rock higher than I' is the NT's confession of Christ's transcendence."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "John 14:2",
        "note": "I will dwell in your tent forever; I will take refuge under the shelter of your wings — 'my Father's house has many rooms... I am going there to prepare a place for you' (John 14:2). The permanent dwelling in God's tent (Ps 61:4) is the promise Christ makes real in the eschatological dwelling. Rev 7:15: 'he who sits on the throne will shelter them with his presence.' The Psalm's 'dwell forever' in God's tent becomes the new Jerusalem where 'God's dwelling place is now among the people' (Rev 21:3)."
      }
    ],
    "6": [
      {
        "type": "fulfillment",
        "target": "Luke 1:33",
        "note": "You will extend the king's days; his years shall span many generations. May he dwell before God forever — 'he will reign over Jacob's descendants forever; his kingdom will never end' (Luke 1:33). The prayer for the king whose days are extended forever and who dwells before God forever (Ps 61:6-7) is answered in Christ whose kingdom has no end. Heb 7:24: 'but because Jesus lives forever, he has a permanent priesthood' — the eternal days of Psalm 61:6 fulfilled in the one who 'always lives to intercede' (Heb 7:25)."
      }
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    for ch in ['55','56','57','58','59','60','61']:
        entries = len(existing.get(ch, {}))
        print(f"  ch{ch}: {entries} verses with entries")
    print("Psalms 55–61 echoes complete.")

if __name__ == '__main__':
    main()
