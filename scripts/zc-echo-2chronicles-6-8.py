"""
Echo Layer — 2 Chronicles chapters 6–8
Run: python3 scripts/zc-echo-2chronicles-6-8.py

Ch 6: Solomon's dedicatory prayer — the longest prayer in the OT; key echoes:
  - v18 (will God dwell with humans?) → John 1:14 / Rev 21:3 — the incarnation/new creation answer
  - v30 (you know all human hearts) → Heb 4:13 / Rev 2:23 — the omniscient Christ
  - vv32-33 (prayer for foreigners) → Matt 21:13 / Isa 56:7 — house of prayer for all nations
  - v41 (arise to your resting place) → Heb 4:9-11 / Ps 132:8 — the rest that remains
  - v42 (do not reject your anointed) → Ps 132:10 — messianic anointed

Ch 7: YHWH's answer — v1 (fire from heaven), v14 (already present), v16 (eyes/heart there forever)
  - v1 → Heb 12:29 (consuming fire) / Lev 9:24 (inauguration fire)
  - v16 → John 14:23 / Matt 28:20 (the abiding presence of God)

Ch 8: Solomon's building work concludes
  - v12-13 (burnt offerings on the altar) → Heb 10:11-14 (repeated vs. once-for-all sacrifice)
  - v16 (all work finished / Solomon's house complete) → John 19:30 (tetelestai — the redemptive work complete)
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
  "6": {
    "18": [
      {
        "type": "fulfillment",
        "target": "John 1:14",
        "note": "Solomon's question — 'But will God truly dwell with human beings on the earth? Even the highest heavens cannot contain you' — receives its definitive NT answer in the incarnation: the Word became flesh and tabernacled (ἐσκήνωσεν) among us, the divine presence localized in a human body rather than a house of cedar and stone."
      },
      {
        "type": "fulfillment",
        "target": "Rev 21:3",
        "note": "The temple dedication question ('will God dwell with humans?') reaches its eschatological fulfillment in Revelation's new creation: 'Behold, the dwelling place of God is with man. He will dwell with them, and they will be his people, and God himself will be with them as their God.' What Solomon's temple signified and imperfectly realized, the new Jerusalem completes."
      }
    ],
    "30": [
      {
        "type": "theme",
        "target": "Heb 4:13",
        "note": "Solomon's petition — 'you only know the hearts of all people' — grounds the prayer in YHWH's omniscience. Hebrews applies this same divine knowledge to Christ: 'no creature is hidden from his sight, but all are naked and exposed to the eyes of him to whom we must give account.' The judge who knows all hearts is identified as the risen Christ before whom all must give account."
      },
      {
        "type": "allusion",
        "target": "Rev 2:23",
        "note": "The Chronicler's 'you only know the hearts of all people' is echoed in Christ's letter to Thyatira: 'I am he who searches mind and heart, and I will give to each of you according to your works.' The omniscient God of the temple dedication is the omniscient Christ of the risen church."
      }
    ],
    "32": [
      {
        "type": "allusion",
        "target": "Isa 56:7",
        "note": "Solomon's prayer that the foreigner who comes 'from a distant land because of your great name' should be heard from heaven — 'so that all peoples of the earth may know your name and respect you' — is the OT's clearest anticipation of the universality of Israel's God. Isaiah 56:7 uses identical language: 'my house shall be called a house of prayer for all peoples.' Jesus quotes Isa 56:7 when cleansing the temple (Matt 21:13), citing what Solomon's prayer inaugurated as the goal the temple money-changers were thwarting."
      }
    ],
    "33": [
      {
        "type": "fulfillment",
        "target": "Matt 21:13",
        "note": "The prayer for foreigners — 'grant all that the foreigner asks of you, so that all peoples of the earth may know your name' — finds its NT fulfillment in two directions: Jesus' cleansing of the temple's outer court (the court of the Gentiles) restores the space designated for Gentile prayer (Matt 21:13; quoting Isa 56:7), and Acts 15:14 reports James's declaration that God visited the Gentiles to take a people for his name — exactly the universality Solomon's prayer requested."
      }
    ],
    "41": [
      {
        "type": "allusion",
        "target": "Ps 132:8",
        "note": "Solomon's closing invocation — 'Now arise, LORD God, and come to your resting place — you and the ark of your power' — quotes Psalm 132:8 verbatim. Hebrews 4:1-11 takes up the 'resting place' motif and argues that the rest David and Solomon could not fully provide remains open: 'So then, there remains a Sabbath rest for the people of God... Let us therefore strive to enter that rest.' The temple's resting place is the shadow; Christ's finished work is the substance."
      }
    ],
    "42": [
      {
        "type": "type",
        "target": "Ps 132:10",
        "note": "Solomon's closing petition — 'LORD God, do not reject your anointed one. Remember your steadfast love for your servant David' — is drawn from Psalm 132:10, where 'your anointed one' (<em>mᵉšîḥeḵā</em>) points beyond Solomon to the perpetual Davidic anointed whom YHWH will not reject. The NT's Christos (Christ = Anointed) is the fulfillment: God did not reject his Anointed but raised him from the dead and seated him at his right hand (Acts 2:32-36)."
      }
    ]
  },
  "7": {
    "1": [
      {
        "type": "allusion",
        "target": "Lev 9:24",
        "note": "Fire descending from heaven to consume the inaugural burnt offering mirrors the Mosaic tabernacle dedication (Lev 9:24: 'fire came out from before the LORD and consumed the burnt offering'), confirming that the Solomonic temple is the legitimate successor of Sinai's sanctuary. The same divine acceptance-by-fire pattern recurs at Elijah's Mount Carmel sacrifice (1 Kgs 18:38) — each a demonstration that YHWH alone is God."
      },
      {
        "type": "allusion",
        "target": "Heb 12:29",
        "note": "The fire that consumed the temple's inaugural offering expresses YHWH's holiness — a motif Hebrews applies to the new covenant: 'our God is a consuming fire' (Heb 12:29, quoting Deut 4:24). At Pentecost, the same consuming presence appears as tongues of fire (Acts 2:3), now resting on the new-covenant community rather than a stone sanctuary — the fire from heaven is internalized in Christ's people."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "John 14:23",
        "note": "YHWH's promise — 'my eyes and my heart will always be there' (sc. at the temple) — is the OT's most personal statement of divine abiding presence. Jesus restates this promise in new-covenant terms: 'If anyone loves me, he will keep my word, and my Father will love him, and we will come to him and make our home with him' (John 14:23). What the temple hosted externally, the indwelling Spirit makes internal and personal."
      },
      {
        "type": "allusion",
        "target": "Matt 28:20",
        "note": "YHWH's temple-promise — 'my name may rest here forever... my eyes and my heart will always be there' — is the OT pattern for the risen Christ's commission-promise: 'behold, I am with you always, to the end of the age' (Matt 28:20). The perpetual divine presence promised to the stone temple is now promised by the risen Christ to his gathered community wherever they go."
      }
    ]
  },
  "8": {
    "12": [
      {
        "type": "shadow",
        "target": "Heb 10:11",
        "note": "Solomon's regular burnt offerings 'following the daily schedule... on Sabbaths, new moons, and the three annual appointed feasts' represent the system of repeated sacrifices that Hebrews contrasts with Christ's once-for-all offering: 'every priest stands daily at his service, offering repeatedly the same sacrifices, which can never take away sins. But when Christ had offered for all time a single sacrifice for sins, he sat down at the right hand of God' (Heb 10:11-12). The dailiness of Solomon's altar sacrifices underscores the inadequacy the once-for-all sacrifice resolves."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "John 19:30",
        "note": "Solomon's completion summary — 'all of Solomon's work was carried out from the day the LORD's house was founded to the day it was finished' — uses the completion-of-work formula that John's Gospel applies to Christ's redemptive work: 'It is finished' (<em>tetelestai</em>, John 19:30). Solomon finishes building the earthly temple that death could destroy; Christ finishes the redemptive work that establishes the eternal dwelling of God with humanity, fulfilling what the temple always signified."
      }
    ]
  }
}

def main():
    existing = load_echo('2chronicles')
    merge_echo(existing, CHRON2_ECHOES)
    save_echo('2chronicles', existing)
    n = sum(len(vv) for vv in CHRON2_ECHOES.values())
    print(f'2Chronicles 6-8 echoes written ({n} verses across 3 chapters).')

if __name__ == '__main__':
    main()
