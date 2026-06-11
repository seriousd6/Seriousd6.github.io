"""
Echo — Jeremiah chapters 33–36
Run: python3 scripts/zc-echo-jeremiah-33-36-fill.py

Combined Phase 2 script zc-echo-jeremiah-33-36.py exists but likely has no ch 33-36 echo data.

Key echo decisions:
- 33:3 (call and I will answer) = Matt 7:7-8; Eph 3:20
- 33:8 (cleanse/forgive all iniquity) = 1 John 1:9; Heb 9:26
- 33:11 (voice of bridegroom/bride) = John 3:29; Rev 21:2
- 33:15 (righteous Branch of David) = direct NT citation cluster: Luke 1:32-33; Rom 1:3; Rev 22:16
- 33:17 (no lack of Davidic king) = Acts 2:30-31; Rev 22:16
- 34:14-17 (liberty proclaimed then revoked) = Luke 4:18; Gal 5:13
- 35:14-16 (Rechabite faithfulness contrasting Israel) = Matt 8:10; Heb 4:16
- 36:23-24 (scroll burned) = 1 Pet 1:25 (word endures); Isa 40:8
- 36:28-32 (word reconstituted after destruction) = 1 Pet 1:23-25
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

JER_ECHO_33_36 = {
  "33": {
    "3": [
      {"type": "allusion", "target": "Matt 7:7-8", "note": "Call to me and I will answer you, and I will tell you great and hidden things you have not known — the prayer-and-answer promise of Jer 33:3 is the OT ground for Jesus's ask/seek/knock teaching: ask and it will be given to you, seek and you will find (Matt 7:7-8); the promise that YHWH will reveal hidden things to those who call is the foundation of Christian prayer"},
      {"type": "allusion", "target": "Eph 3:20", "note": "I will tell you great and hidden things that you have not known — Paul&apos;s doxology at the end of his prayer: to him who is able to do far more abundantly than all we ask or think (Eph 3:20); the hidden-things promise of Jer 33:3 is the precursor to the surpassing-all-we-ask-or-think assurance Paul gives to the church"}
    ],
    "8": [
      {"type": "allusion", "target": "1 John 1:9", "note": "I will cleanse them from all the iniquity by which they sinned against me, and I will forgive all the iniquity and rebellion — the dual cleanse-and-forgive promise; John uses the same pairing: if we confess our sins he is faithful and just to forgive us our sins and cleanse us from all unrighteousness (1 John 1:9); Jer 33:8 is the OT promise that 1 John declares fulfilled in Christ"},
      {"type": "fulfillment", "target": "Heb 9:26", "note": "I will forgive all the iniquity and rebellion — the comprehensive forgiveness that YHWH promises for the restored Jerusalem; Hebrews declares the once-for-all mechanism: Christ appeared once for all at the end of the ages to put away sin by the sacrifice of himself (Heb 9:26); the forgiveness Jeremiah announces is what Christ enacts at the cross"}
    ],
    "11": [
      {"type": "allusion", "target": "John 3:29", "note": "The voice of the bridegroom and the voice of the bride, the voice of those who sing as they bring thank offerings — the restoration of joy after desolation signaled by the bridal voice; John the Baptist identifies Jesus as the bridegroom (John 3:29: he who has the bride is the bridegroom; the friend of the bridegroom rejoices greatly at the bridegroom&apos;s voice); the joyful bridal voice of Jer 33:11 is what John hears in Jesus"},
      {"type": "allusion", "target": "Rev 21:2", "note": "The voice of the bridegroom and the voice of the bride — the restored Jerusalem filled with bridal joy; Revelation&apos;s climax is the holy city descending as a bride adorned for her husband (Rev 21:2); the bridal restoration Jeremiah promises for the desolated city is the prototype of the New Jerusalem as bride"}
    ],
    "15": [
      {"type": "fulfillment", "target": "Luke 1:32-33", "note": "In those days I will cause a righteous Branch to spring up for David — the Tsemach Tsaddiq (righteous Branch) promise; Gabriel&apos;s announcement fulfills this directly: the Lord God will give him the throne of his father David, and he will reign over the house of Jacob forever (Luke 1:32-33); the Branch who executes justice and righteousness in the land is the one whose kingdom has no end"},
      {"type": "fulfillment", "target": "Rev 22:16", "note": "A righteous Branch to spring up for David — the Branch of the Davidic line; the risen Christ&apos;s self-identification in Revelation&apos;s closing: I am the Root and the Offspring of David, the bright morning star (Rev 22:16); the Branch prophecy of Jer 33:15 is among the clearest OT anticipations of the Davidic Messiah"}
    ],
    "17": [
      {"type": "fulfillment", "target": "Acts 2:30-31", "note": "There will never fail to be a man from David&apos;s line to sit on the throne of the house of Israel — the eternal Davidic covenant; Peter&apos;s Pentecost sermon cites David&apos;s expectation that one of his descendants would sit on his throne (Acts 2:30-31: foreseeing this, he spoke of the resurrection of the Christ); the never-ending Davidic reign of Jer 33:17 is fulfilled in the risen and enthroned Christ"}
    ],
    "20": [
      {"type": "allusion", "target": "Heb 6:17-18", "note": "If you can break my covenant with the day and my covenant with the night so that day and night no longer come at their appointed time — YHWH grounds the Davidic covenant&apos;s certainty in the unchanging order of creation; Hebrews makes a parallel argument for the certainty of God&apos;s promises: so that by two unchangeable things (his promise and his oath) we who have fled for refuge might have strong encouragement (Heb 6:17-18); creation&apos;s order and the covenant oath together guarantee certainty"}
    ]
  },
  "34": {
    "17": [
      {"type": "allusion", "target": "Gal 5:13", "note": "You have not obeyed me by proclaiming liberty — instead I will proclaim liberty against you: to the sword, plague, and famine — the ironic inversion: those who refused to grant freedom are granted freedom to be destroyed; Paul warns of the same irony in Gal 5:13: you were called to freedom, brothers, but do not use your freedom as an opportunity for the flesh; proclaimed liberty that becomes license brings its own bondage"},
      {"type": "allusion", "target": "Luke 4:18", "note": "You shall proclaim liberty to your neighbors — the sabbatical-year slave release that Judah violated; Jesus&apos;s synagogue sermon (Luke 4:18: he has sent me to proclaim liberty to the captives) applies the jubilee liberty of Lev 25 and Isa 61 to his own mission; where Judah proclaimed and then revoked liberty, Jesus proclaims a liberty that is irrevocable"}
    ]
  },
  "35": {
    "14": [
      {"type": "allusion", "target": "Matt 8:10", "note": "The descendants of Jonadab have kept their father&apos;s command, but this people has not obeyed me — the outsiders&apos; faithfulness used to shame the covenant people; Jesus uses the same pattern of comparison: not even in Israel have I found such faith (Matt 8:10, of the Roman centurion); the Rechabites&apos; faithful obedience to a human father&apos;s command contrasts with Israel&apos;s disobedience to YHWH, as the centurion&apos;s faith contrasts with Israel&apos;s unbelief"}
    ],
    "19": [
      {"type": "allusion", "target": "Heb 4:16", "note": "Jonadab son of Rechab shall never fail to have a man standing before me — the perpetual-standing promise to the faithful Rechabites; the new covenant extends standing before God to all believers through Christ: let us draw near to the throne of grace with confidence, so that we may receive mercy and find grace to help in time of need (Heb 4:16); access to God&apos;s presence, which the Rechabites&apos; promise foreshadows, is available to all in Christ"}
    ]
  },
  "36": {
    "23": [
      {"type": "allusion", "target": "Matt 5:18", "note": "As Jehudi read three or four columns the king would cut the section off with a scribe&apos;s knife and throw it into the fire — the futile destruction of the written word of God; Jesus&apos;s declaration (not one jot or tittle will pass from the Law until all is accomplished, Matt 5:18) asserts the indestructibility of the divine word; Jehoiakim&apos;s burning of the scroll illustrates the exact futility Jesus implies: you cannot destroy it"}
    ],
    "28": [
      {"type": "allusion", "target": "1 Pet 1:23-25", "note": "Take another scroll and write on it all the same words that were in the first scroll that Jehoiakim burned — the word of YHWH reconstituted after its apparent destruction; Peter quotes Isa 40:8 to make this the defining character of the gospel: the living and abiding word of God, the word of the Lord that remains forever (1 Pet 1:23-25); Jer 36&apos;s reconstituted scroll is the narrative demonstration of the word&apos;s indestructibility that Isaiah announces and Peter applies to the gospel"}
    ]
  }
}

def main():
    existing = load_echo('jeremiah')
    merge_echo(existing, JER_ECHO_33_36)
    save_echo('jeremiah', existing)
    print('Jeremiah 33-36 echoes written.')

if __name__ == '__main__':
    main()
