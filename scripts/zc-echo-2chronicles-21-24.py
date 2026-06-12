"""
Echo Commentary — 2 Chronicles chapters 21–24
Run: python3 scripts/zc-echo-2chronicles-21-24.py

Ch 21: Jehoram's apostasy — Davidic covenant preserved despite king's wickedness (v7);
       Elijah's prophetic letter (vv12-15) echoes the seven letters of Revelation.
Ch 22: Ahaziah and Athaliah — Jehoshabeath hides Joash types preservation of the
       messianic seed; God's judgment on Ahaziah (v7) parallels Acts 12:23.
Ch 23: Jehoiada's coup — coronation with crown and testimony (v11) types Ps 2 / Rev 19;
       covenant renewal (v16) types new covenant; rejoicing people (v13) echo Palm Sunday.
Ch 24: Joash's reign — Moses' temple tax echoes Matt 17:24-27; Zechariah son of Jehoiada
       stoned (v21) is the most direct NT citation in this passage (Matt 23:35; Luke 11:51);
       his dying cry "May the LORD avenge!" echoes Rev 6:10.
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

CHRON2_ECHOES = {
  "21": {
    "7": [
      {
        "type": "allusion",
        "target": "2 Sam 7:12-16",
        "note": "The Chronicler explicitly invokes the Davidic covenant as the reason YHWH refuses to destroy the house of David despite Jehoram's apostasy — the covenant is unconditional and irrevocable, a principle Paul applies directly in Rom 11:29."
      },
      {
        "type": "allusion",
        "target": "Rom 11:29",
        "note": "Paul's declaration that 'the gifts and calling of God are irrevocable' directly extends the logic of 2 Chr 21:7 — the Davidic line is preserved not on the king's merit but on God's covenant faithfulness, which reaches its irreversible culmination in Christ (Acts 2:30)."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "Rev 2:1",
        "note": "Elijah's written letter of prophetic judgment against Jehoram (vv12-15) anticipates the format of the seven letters to the churches in Revelation 2-3 — a prophet's written word carrying divine authority, naming specific sins, and announcing consequences."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "1 Pet 2:4",
        "note": "Jehoram 'departed without being desired' — an epitaph of contempt for the dishonored king. The contrast with Christ is direct: the one 'rejected by men' is 'chosen and precious in God's sight' (1 Pet 2:4), his departure not undesired but mourned and his return awaited."
      }
    ]
  },
  "22": {
    "7": [
      {
        "type": "allusion",
        "target": "Acts 12:23",
        "note": "The Chronicler attributes Ahaziah's death explicitly to God: 'his downfall was God's doing.' The same divine sovereignty over the deaths of the wicked appears in Acts 12:23 (Herod struck down by an angel), reinforcing the pattern that YHWH removes wicked rulers in his own time."
      }
    ],
    "11": [
      {
        "type": "type",
        "target": "Matt 2:13-15",
        "note": "Jehoshabeath hides the infant Joash — the last son of the royal house — in the temple to preserve the Davidic line from Athaliah's massacre. This directly types the flight to Egypt: in both cases a single child of the royal line is hidden from a murderous ruler (Athaliah / Herod) to preserve the messianic promise."
      },
      {
        "type": "allusion",
        "target": "Exod 2:2-3",
        "note": "The hiding of a single child to preserve a divinely promised line recurs: Moses hidden by his mother, Joash hidden by his aunt, Jesus hidden in Egypt. The pattern reveals YHWH's pattern of preserving his purposes through concealment when human power seeks to extinguish them."
      }
    ]
  },
  "23": {
    "3": [
      {
        "type": "allusion",
        "target": "Luke 1:32-33",
        "note": "Jehoiada announces the Davidic covenant as the warrant for Joash's restoration: 'The LORD has spoken concerning the sons of David.' The same covenant warrant governs Gabriel's announcement to Mary — the son of the Most High will receive 'the throne of his father David' and reign forever (Luke 1:32-33)."
      }
    ],
    "11": [
      {
        "type": "type",
        "target": "Ps 2:6-7",
        "note": "The physical coronation of Joash — crown placed on his head, the covenant document (testimony) in his hand, anointed and acclaimed — is the earthly enactment of the royal inauguration Psalm 2 describes for the ultimate Davidic king: 'I have set my King on Zion, my holy hill... You are my Son; today I have begotten you.'"
      },
      {
        "type": "allusion",
        "target": "Rev 19:12",
        "note": "The crowned king standing in the restored temple is a type of the rider on the white horse in Rev 19:12 who 'has a name written that no one knows but himself' and wears 'many diadems' — the ultimate coronation of which every Davidic enthronement is a shadow."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Luke 19:37-38",
        "note": "The people rejoicing and blowing trumpets at the king's installation 'by the pillar at the entrance' echoes the crowd's acclamation at the triumphal entry — both scenes feature the restored Davidic king acclaimed by his people at a key threshold, with instruments and public praise."
      }
    ],
    "16": [
      {
        "type": "type",
        "target": "Jer 31:31-34",
        "note": "Jehoiada makes a covenant 'between himself, all the people, and the king, that they should be the LORD's people.' The three-party covenant formula — priest, people, and king all bound to YHWH — is the structural anticipation of the new covenant in which Christ as priest, his people, and the divine king are similarly united by covenant bond (Jer 31:33: 'I will be their God, and they shall be my people')."
      },
      {
        "type": "allusion",
        "target": "Heb 9:15",
        "note": "This covenant renewal after a period of apostasy and false religion (Athaliah's Baal worship) prefigures the new covenant mediated by Christ that supersedes and cleanses the failure of the old — 'a death has occurred that redeems them from the transgressions committed under the first covenant' (Heb 9:15)."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "Acts 19:27",
        "note": "The people tear down the house of Baal, smash its altars and images, and kill the priest of Baal before the altars. The pattern of covenant renewal followed by the physical destruction of false worship is repeated in Acts 19 where the spread of the gospel directly threatens the worship of Artemis and her silver shrines are economically disrupted."
      }
    ]
  },
  "24": {
    "9": [
      {
        "type": "allusion",
        "target": "Matt 17:24-27",
        "note": "The collection of the 'tax of Moses' (Exod 30:13 — half a shekel per person for the tabernacle/temple) directly underlies the temple-tax episode in Matt 17:24-27, where Jesus pays the two-drachma temple tax through the miracle of the fish — affirming the institution while demonstrating his own sovereign freedom from it as the Son."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Acts 2:17",
        "note": "The Spirit of God 'clothed' (came upon) Zechariah son of Jehoiada, prompting his prophetic rebuke of the apostate people. The same Spirit poured out at Pentecost (Acts 2:17, citing Joel 2:28) clothes and impels the apostolic witness — the same divine empowerment for prophetic speech that Zechariah experienced."
      }
    ],
    "21": [
      {
        "type": "fulfillment",
        "target": "Matt 23:35",
        "note": "Jesus explicitly names 'Zechariah the son of Berechiah' as the last OT martyr, 'whom you murdered between the sanctuary and the altar' (Matt 23:35; Luke 11:51). This is the most direct NT citation of this passage: Jesus identifies the stoning of Zechariah in the temple court as the closing bookend of the entire history of prophetic martyrdom from Abel onward, and charges his contemporaries with responsibility for the whole sequence."
      },
      {
        "type": "allusion",
        "target": "Luke 11:51",
        "note": "Luke's parallel account places Zechariah's blood 'between the altar and the sanctuary' — matching the detail of 2 Chr 24:21 precisely. Jesus's use of this reference in his woes against the scribes and Pharisees turns 2 Chr 24:21 into an indictment: the same pattern of killing God's messengers that characterized Joash's court recurs in first-century Jerusalem."
      }
    ],
    "22": [
      {
        "type": "allusion",
        "target": "Rev 6:10",
        "note": "Zechariah's dying words — 'May the LORD see and avenge!' — are the OT prototype of the martyrs' cry in Rev 6:10: 'O Sovereign Lord, holy and true, how long before you will judge and avenge our blood on those who dwell on the earth?' The blood of the martyred prophet calls for divine justice, a call that reaches its final answer at the last judgment."
      }
    ],
    "25": [
      {
        "type": "allusion",
        "target": "John 1:11",
        "note": "Joash, who owed his throne to the priest Jehoiada, had Jehoiada's son Zechariah killed and was then assassinated by his own servants — killed by the very people his house had depended on. The pattern of abandonment and betrayal by one's own prefigures the deeper reality of John 1:11: 'He came to his own, and his own people did not receive him.'"
      }
    ]
  }
}

def main():
    existing = load_echo('2chronicles')
    merge_echo(existing, CHRON2_ECHOES)
    save_echo('2chronicles', existing)
    ch_count = len(CHRON2_ECHOES)
    v_count = sum(len(vv) for vv in CHRON2_ECHOES.values())
    print(f'2chronicles echoes ch 21-24: wrote {v_count} verses across {ch_count} chapters')

if __name__ == '__main__':
    main()
