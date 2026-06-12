"""
MKT Echo Layer — 1 Chronicles chapters 11–12
Run: python3 scripts/zc-echo-1chronicles-11-12.py

Source data used:
- data/interlinear/1chronicles.json
- data/parallels/1chronicles.json (absorbed: ch11 vv1-3, 4-9, 10-47)
- data/translation/draft/mediating/1chronicles.json

Key decisions in this range:
- Ch11 parallels (2 Sam 5:1-3, 5:6-10, 23:8-39) absorbed as allusions —
  not "fulfillment" since Chron is retelling history, not claiming prophetic completion
- Water episode (11:17-19): classified as type/shadow of Christ's self-giving —
  the refusal to drink blood-price water and offering to YHWH is structurally
  analogous to Christ's self-sacrifice; not a direct quote but a genuine type
- Amasai's Spirit-oracle (12:18): shadow pointing to Acts 2 gathering to Son of David
- "Sons of Issachar" (12:32): theme rather than fulfillment — the discernment of
  appointed times is taken up in NT kairos language but not directly cited
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

CHRONICLES1_ECHOES = {
  "11": {
    "1": [
      {
        "type": "allusion",
        "target": "2 Sam 5:1-3",
        "note": "The Chronicler reproduces almost verbatim the account of David's anointing at Hebron. The kinship formula 'we are your bone and your flesh' (Gen 2:23 language) signals covenant union — the same idiom Paul applies to the church's union with Christ (Eph 5:30)."
      }
    ],
    "2": [
      {
        "type": "theme",
        "target": "John 10:11",
        "note": "The description of David as the one who 'led out and brought in Israel' is shepherd-king language — the same idiom used in Num 27:17 for the leader who goes out and comes in before the people. Jesus claims this role as the good shepherd who leads the flock (John 10:3-4, 11)."
      }
    ],
    "3": [
      {
        "type": "shadow",
        "target": "Luke 1:32-33",
        "note": "The covenant made with all Israel at Hebron, anointing David king 'according to the word of the LORD by Samuel,' is the founding moment of the Davidic covenant. The angel's promise to Mary that her son will receive 'the throne of his father David' and 'reign over the house of Jacob forever' identifies Jesus as the ultimate heir to this Hebron covenant."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "2 Sam 5:6-10",
        "note": "Parallel account of Jerusalem's capture. The Chronicler edits the story to emphasize Joab's role and omit the taunting 'blind and lame' episode; both accounts establish Jerusalem as the Davidic capital — the city that becomes in Hebrews 12:22 the 'heavenly Jerusalem' to which believers have come."
      }
    ],
    "9": [
      {
        "type": "theme",
        "target": "Matt 1:23",
        "note": "The refrain 'the LORD of hosts was with him' establishes the theological pattern of divine presence with the Davidic king. The Immanuel promise (Isa 7:14; Matt 1:23) is its christological fulfillment — the presence of YHWH with his anointed reaches its permanent expression in the incarnate Son."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "2 Sam 23:8-39",
        "note": "The Mighty Men list closely parallels 2 Samuel 23. The Chronicler frames these warriors as those who 'gave him strong support in his kingdom...to make him king.' They are a typological pointer to those who labor in building Christ's kingdom (cf. Rom 16:3-16, where Paul names co-workers who 'risked their necks')."
      }
    ],
    "17": [
      {
        "type": "type",
        "target": "Heb 9:14",
        "note": "David's longing for water from Bethlehem — and his refusal to drink what his men risked their lives to bring — is one of the OT's purest types of vicarious self-giving. He pours it out as a libation to YHWH, saying 'Far be it from me to drink the blood of these men.' The logic anticipates Christ offering himself through the eternal Spirit (Heb 9:14): life blood offered to God rather than consumed."
      }
    ],
    "19": [
      {
        "type": "shadow",
        "target": "Mark 10:45",
        "note": "David refuses to benefit from what cost others their lives, treating their shed blood as sacred. This shadow finds its deepest fulfillment in the Son of Man who came 'not to be served but to serve, and to give his life as a ransom for many' — the one whose blood, unlike the Bethlehem water, was not poured out as a libation but as the price of others' redemption."
      }
    ],
    "41": [
      {
        "type": "allusion",
        "target": "Matt 1:6",
        "note": "Uriah the Hittite appears near the end of the Mighty Men list — the same man named in Matthew's genealogy as the first husband of Bathsheba ('the wife of Uriah'), through whom Solomon was born in the Davidic-messianic line. His inclusion among David's most loyal warriors heightens the irony of David's later betrayal of him."
      }
    ]
  },
  "12": {
    "1": [
      {
        "type": "theme",
        "target": "Heb 11:38",
        "note": "Warriors come to David at Ziklag 'while he was still keeping himself hidden from Saul' — the anointed king living in exile and hiddenness before his enthronement. The pattern resonates with the Hebrews 11 gallery of faith: those who, like David's men, attached themselves to God's chosen one during the period of his rejection."
      }
    ],
    "18": [
      {
        "type": "shadow",
        "target": "Acts 2:32-33",
        "note": "The Spirit comes upon Amasai and he declares 'We are yours, David; we are with you, son of Jesse!' — a Spirit-inspired confession of allegiance to the Davidic king. The shadow points forward to Pentecost, where the Spirit is poured out by the exalted Son of David and the crowds are drawn to declare Jesus as Lord and Messiah (Acts 2:32-36)."
      },
      {
        "type": "allusion",
        "target": "John 10:16",
        "note": "Amasai's oracle — warriors from multiple tribes united in one cry of allegiance — anticipates 'I have other sheep that are not of this fold; I must bring them also, and they will listen to my voice. So there will be one flock, one shepherd.' The gathering of Israel's tribes to David at Ziklag foreshadows the eschatological gathering of all peoples to Christ."
      }
    ],
    "22": [
      {
        "type": "theme",
        "target": "Rev 19:14",
        "note": "The stream of volunteers reaching David 'day by day' until 'there was a great army, like the army of God' uses language that resonates with the heavenly armies following the Rider on the white horse at the final victory. David's growing host of loyal warriors is a temporal anticipation of the heavenly host that accompanies the Son of David at his return."
      }
    ],
    "32": [
      {
        "type": "theme",
        "target": "Gal 4:4",
        "note": "The sons of Issachar 'understood the times and knew what Israel should do' — wisdom for discerning the appointed moment when the kingdom requires a new direction. Paul's declaration that 'when the fullness of time had come, God sent forth his Son' (Gal 4:4) reflects the same theological category: history has kairos moments that only those with Spirit-given discernment can recognize."
      }
    ],
    "38": [
      {
        "type": "shadow",
        "target": "Rev 7:9",
        "note": "All the tribes of Israel gathering 'with a perfect heart to make David king over all Israel' is a historical type of the eschatological assembly described in Revelation 7:9 — the great multitude from every nation, tribe, people, and language standing before the Lamb. As the tribes came to Hebron to crown David, so all peoples will come to crown the Son of David."
      }
    ],
    "40": [
      {
        "type": "theme",
        "target": "Rev 19:9",
        "note": "The three-day feast at Hebron — 'eating and drinking, for their kinsmen had prepared food for them' — is the festive coronation meal of the Davidic king celebrated by the whole assembly. It anticipates the marriage supper of the Lamb (Rev 19:9), the eschatological feast at the enthronement of the true Son of David."
      }
    ]
  }
}

def main():
    existing = load_echo('1chronicles')
    merge_echo(existing, CHRONICLES1_ECHOES)
    save_echo('1chronicles', existing)
    print('1 Chronicles 11–12 echoes written.')

if __name__ == '__main__':
    main()
