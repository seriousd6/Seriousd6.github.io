"""
MKT Echo Commentary — Jeremiah chapters 4–6
Run: python3 scripts/zc-echo-jeremiah-4-6.py

Key echo anchors:
- Jer 4:4  "circumcise your hearts" → Rom 2:29; Col 2:11 (inner circumcision through
  the Spirit; fulfilled in baptism/new birth in Christ)
- Jer 4:23 the un-creation vision (tohu vavohu, no light) → Rev 6:12–14; 2 Pet 3:10
  (eschatological cosmic dissolution mirrors Jeremiah's vision of de-creation)
- Jer 5:1  "see if there is one righteous person" → Rom 3:10–12 (Paul's universal
  indictment in Romans 3 draws directly on this prophetic search that found none)
- Jer 5:21 "eyes but do not see; ears but do not hear" → Mark 8:18; Isa 6:9–10
  (Jesus applies this to the disciples and to unbelieving Israel; Mark 8:18 is the
  only NT verse that quotes Jer 5:21 directly rather than Isa 6)
- Jer 6:14 "peace, peace when there is no peace" → 1 Thess 5:3 (sudden destruction
  when people cry "peace and safety" — the false-peace oracle pattern recapitulated)
- Jer 6:16 "you will find rest for your souls" → Matt 11:29 (Jesus quotes this verse
  directly from the LXX in his "Come to me" invitation; the Jeremiah rest that Israel
  refused is the rest Christ now offers)
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
    """Merge echo entries without duplicating type+target pairs."""
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

JEREMIAH_ECHO = {
  "4": {
    "4": [
      {"type": "fulfillment", "target": "Rom 2:29", "note": "Circumcise yourselves to the LORD and remove the foreskins of your hearts — Paul's argument that true circumcision is inward and of the heart, done by the Spirit, not by the letter, is the direct NT fulfillment of Jeremiah's call; the outer rite pointed to an inner reality that the Spirit now enacts"},
      {"type": "allusion", "target": "Col 2:11", "note": "In Christ you were circumcised with a circumcision not performed by human hands, the putting off of the sinful nature — Paul identifies baptismal union with Christ's death as the fulfillment of heart-circumcision; Jer 4:4's demand is met in Christ's cutting away of the old self"},
      {"type": "allusion", "target": "Deut 30:6", "note": "The LORD your God will circumcise your hearts and the hearts of your descendants — Jeremiah's command in 4:4 is later given as a divine promise in Deut 30:6; the NT's gift of the Spirit is the fulfillment of that promise as the agent who performs the inner circumcision"}
    ],
    "23": [
      {"type": "allusion", "target": "Rev 6:12-14", "note": "I looked at the earth and it was formless and void (tohu vavohu), I looked at the heavens and their light was gone — Jeremiah's vision of de-creation uses the same language as Gen 1:2; Revelation's cosmic dissolution at the sixth seal (sun black, stars fall) is the eschatological recapitulation of Jeremiah's prophetic vision of un-creation under judgment"},
      {"type": "allusion", "target": "2 Pet 3:10", "note": "The heavens will pass away with a roar; the heavenly bodies will be burned up and dissolved — Peter's eschatological picture of cosmic dissolution is the ultimate fulfillment of Jeremiah's de-creation vision; what Jeremiah saw in prophetic terror as the consequence of covenant-breaking, Peter describes as the final cosmic event"}
    ],
    "28": [
      {"type": "allusion", "target": "Matt 24:35", "note": "I have spoken, I have decided, and I will not relent or change my mind — the irreversibility of YHWH's word of judgment; Jesus echoes this: 'Heaven and earth will pass away, but my words will not pass away'; the prophetic certainty of Jeremiah's judgment-word corresponds to the certainty of Jesus's eschatological words"}
    ]
  },
  "5": {
    "1": [
      {"type": "allusion", "target": "Rom 3:10-12", "note": "Go up and down the streets of Jerusalem and see if there is one righteous person — the prophetic search that establishes universal human guilt is the OT foundation of Paul's argument in Rom 3 that 'there is no one righteous, not even one'; the indictment Paul builds from a catena of Psalms and prophets is rooted in this Jeremiah passage"},
      {"type": "allusion", "target": "Rom 3:9", "note": "Both Jews and Greeks are all under sin — Paul's conclusion in Romans 3 ('not one righteous') is drawn precisely from searches like Jeremiah's that found no righteous person in Jerusalem; the city that should have been most righteous exemplifies universal human guilt"}
    ],
    "21": [
      {"type": "allusion", "target": "Mark 8:18", "note": "You have eyes but do not see; you have ears but do not hear — Jesus applies this to the disciples when they fail to understand the feeding miracles: 'Do you have eyes but fail to see, and ears but fail to hear?' Mark 8:18 cites Jer 5:21 specifically (not Isa 6), making this the only NT verse that quotes Jeremiah's version of the blindness indictment directly"},
      {"type": "allusion", "target": "Matt 13:13-15", "note": "The pattern of eyes-that-do-not-see and ears-that-do-not-hear is also behind Jesus's explanation of why he speaks in parables (citing Isa 6:9-10 in Matt 13:13-15); Jer 5:21 is part of the prophetic tradition of spiritual deafness/blindness that Jesus invokes to explain unbelief"}
    ],
    "24": [
      {"type": "allusion", "target": "Rom 1:21", "note": "They do not even say in their hearts, 'Let us now fear the LORD our God, who gives the autumn and spring rains in season' — Jeremiah's description of ingratitude toward the Creator-God who gives rain exactly corresponds to Paul's account of the pagan world: 'although they knew God, they neither glorified him as God nor gave thanks to him'"}
    ]
  },
  "6": {
    "10": [
      {"type": "allusion", "target": "Acts 7:51-53", "note": "Their ears are closed and they cannot listen; the word of the LORD is an offense to them — Stephen's charge against the Sanhedrin: 'You stiff-necked people with uncircumcised hearts and ears! You always resist the Holy Spirit' is the NT re-presentation of Jeremiah's closed-ears indictment; the same resistance that rejected Jeremiah rejected the Messiah"},
      {"type": "allusion", "target": "Rom 11:8", "note": "God gave them a spirit of stupor, eyes that would not see and ears that would not hear — Paul's citation of Deut 29:4 (and Isa 29:10) in Rom 11 stands in the same prophetic tradition as Jer 6:10; the closed ears that rejected Jeremiah's word characterize the partial hardening Paul describes in Romans 11"}
    ],
    "13": [
      {"type": "allusion", "target": "1 Thess 5:3", "note": "They say 'Peace, peace,' when there is no peace — the false-peace prophecy of Jeremiah (6:14; also 8:11) is the direct background for Paul's warning: 'While people are saying peace and safety, destruction will come on them suddenly'; the pattern of false comfort before judgment recurs in NT eschatological warnings"},
      {"type": "allusion", "target": "2 Pet 2:1-3", "note": "From prophet to priest, everyone practices deceit — the pervasive corruption from top to bottom anticipates Peter's warning about false teachers in the church who will secretly introduce destructive heresies; the Jeremiah pattern of leadership corruption is invoked as a warning type for the new covenant community"}
    ],
    "14": [
      {"type": "allusion", "target": "1 Thess 5:3", "note": "Saying 'Peace, peace,' when there is no peace — the false-prophets' cry of peace before judgment is the OT archetype of the false security Paul warns against in 1 Thess 5:3; the sudden destruction that follows false-peace proclamation in Jeremiah's context is transposed to the Day of the Lord in Paul's eschatology"}
    ],
    "16": [
      {"type": "fulfillment", "target": "Matt 11:29", "note": "Ask where the good way is and walk in it, and you will find rest for your souls — Jesus quotes this verse directly from the LXX when he says 'take my yoke upon you and learn from me, and you will find rest for your souls' (Matt 11:29); the rest that Israel refused to walk toward in Jeremiah's day is now personalized in Jesus: he is the good way and the source of soul-rest; this is one of the most direct verbal parallels between Jeremiah and Jesus's words"},
      {"type": "allusion", "target": "John 14:6", "note": "Ask where the good way is and walk in it — Jesus's self-identification as 'the way, the truth, and the life' (John 14:6) is the answer to Jeremiah's call to ask for the good way; the ancient path and the good way Jeremiah pointed to is personified in Christ who is himself the way"}
    ],
    "20": [
      {"type": "allusion", "target": "Heb 10:4-10", "note": "Your burnt offerings are not acceptable; your sacrifices do not please me — Jeremiah's critique of the sacrificial system when disconnected from obedience is deepened in Hebrews: it is impossible for the blood of bulls and goats to take away sins; the sacrifice that God finds acceptable is Christ's once-for-all offering of himself (Heb 10:10)"},
      {"type": "allusion", "target": "Amos 5:21-22", "note": "What good is incense from Sheba... your burnt offerings are not acceptable — Jeremiah's rejection of sacrifices disconnected from justice stands in the same prophetic tradition as Amos 5:21-22 ('I hate your religious feasts'); both feed into the NT understanding that external religious performance without inner transformation is rejected by God"}
    ]
  }
}


def main():
    existing = load_echo('jeremiah')
    merge_echo(existing, JEREMIAH_ECHO)
    save_echo('jeremiah', existing)
    print('Jeremiah 4–6 echo written.')


if __name__ == '__main__':
    main()
