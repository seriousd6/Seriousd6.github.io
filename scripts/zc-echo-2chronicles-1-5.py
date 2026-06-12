"""
MKT Echo Layer — 2 Chronicles chapters 1–5
Run: python3 scripts/zc-echo-2chronicles-1-5.py

Source data used:
- data/interlinear/2chronicles.json
- data/parallels/2chronicles.json (absorbed: ch1 v1 → 1 Kgs 3; ch3 v1 → 1 Kgs 6; ch5 v2 → 1 Kgs 8)
- data/translation/draft/mediating/2chronicles.json

Key decisions:
- Ch1 parallels 1 Kgs 3 (Solomon's dream at Gibeon): absorbed as allusion; also echoes
  Matt 12:42 (greater than Solomon) and Jas 1:5 (ask wisdom generously)
- Ch2: Huram's collaboration and temple planning; 2:4 incense/feasts → Col 2:16-17 (shadows);
  2:6 heaven-cannot-contain → Acts 7:48 / John 1:14
- Ch3 parallels 1 Kgs 6: Mount Moriah at v1 is the Aqedah site (Gen 22:2) — temple built
  where Abraham's sacrifice was; v14 curtain → Matt 27:51
- Ch4: molten sea → Rev 4:6 (glassy sea); bronze altar → Heb 13:10; lampstands → Rev 1:12
- Ch5: glory-cloud theophany at v13-14 is primary echo focus; ark's placement → Heb 9:4-5;
  the refrain 'his steadfast love endures forever' → Rev 15:3-4
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
  "1": {
    "1": [
      {
        "type": "allusion",
        "target": "1 Kgs 3:4-15",
        "note": "The Chronicler parallels the Gibeon theophany of 1 Kings 3, omitting the dream-frame but preserving Solomon's request for wisdom and YHWH's grant. The Chronicler's account substitutes 'knowledge and wisdom' for 1 Kings' 'discerning heart' — the two accounts are complementary rather than contradictory."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "John 16:24",
        "note": "God's night-time offer to Solomon — 'Ask what you want me to give you' — is the OT prototype of the prayer-promise Jesus extends in John 16:24: 'Ask, and you will receive, that your joy may be full.' The unconditional divine offer to provide what is asked establishes a pattern that the new covenant makes universally available in Christ's name."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Jas 1:5",
        "note": "Solomon's request for 'wisdom and knowledge' to govern God's people is the OT's paradigmatic prayer for wisdom. James 1:5 — 'If any of you lacks wisdom, let him ask God, who gives generously to all without reproach, and it will be given him' — is the NT universalization of Solomon's prayer: what was uniquely granted to Israel's king is made available to every believer through the God who gives generously."
      }
    ],
    "12": [
      {
        "type": "theme",
        "target": "Eph 3:20",
        "note": "Because Solomon asked for wisdom rather than wealth, YHWH grants both wisdom and riches beyond anything asked or imagined: 'riches, wealth, and honor such as no king has had before you.' The pattern of God giving beyond what is requested finds its NT expression in Eph 3:20: 'him who is able to do far more abundantly than all that we ask or think.' Solomon's unexpected surplus is a temporal sign of the divine abundance fully revealed in Christ."
      }
    ]
  },
  "2": {
    "1": [
      {
        "type": "allusion",
        "target": "John 14:2",
        "note": "Solomon builds both a house for YHWH's name and a palace for himself. In John 14:2 Jesus announces: 'In my Father's house are many rooms; I go to prepare a place for you.' The Solomonic building project anticipates Christ's work of preparing a dwelling in the Father's house — though what Solomon built was stone and cedar, Christ prepares a permanent spiritual dwelling in the Father's presence itself."
      }
    ],
    "4": [
      {
        "type": "shadow",
        "target": "Col 2:16-17",
        "note": "Solomon's enumeration of the temple's purposes — burnt offerings, incense, Sabbaths, new moons, appointed feasts — is the calendar of the Mosaic worship system. Paul's declaration in Col 2:16-17 that 'these are a shadow of the things to come, but the substance belongs to Christ' applies precisely to this list: the temple's entire ritual schedule of offerings and festivals is a shadow-complex pointing to the one who is its substance."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Acts 7:48",
        "note": "Solomon's own rhetorical question — 'Who is able to build him a house, since heaven and the highest heaven cannot contain him? Who am I to build him a house, except to offer sacrifice before him?' — anticipates Stephen's argument in Acts 7:48-49 that the Most High does not dwell in houses made by hands. Solomon himself acknowledged the temple's inadequacy as a divine dwelling even as he built it."
      },
      {
        "type": "allusion",
        "target": "John 1:14",
        "note": "The theological problem Solomon identifies — heaven cannot contain God, yet he is building a house for him — is resolved not by a better building but by the incarnation. John 1:14 ('the Word became flesh and tabernacled among us') announces that God has made himself containable in a human body. What the Jerusalem temple could only inadequately approximate, the body of Christ perfectly achieves."
      }
    ]
  },
  "3": {
    "1": [
      {
        "type": "allusion",
        "target": "Gen 22:2",
        "note": "The temple is built on Mount Moriah — the same mountain where God commanded Abraham to offer Isaac (Gen 22:2). The Chronicler explicitly identifies this connection, making the temple's site the place where YHWH's provision was first declared ('the LORD will provide,' Gen 22:14). The temple built where the ram was substituted for Isaac anticipates the greater sacrifice where no substitute was provided but God himself gave his Son (Rom 8:32)."
      }
    ],
    "14": [
      {
        "type": "shadow",
        "target": "Matt 27:51",
        "note": "The curtain separating the Holy Place from the Most Holy Place, made of blue, purple, and crimson yarn and fine linen, is the veil torn in two from top to bottom at Christ's death (Matt 27:51). The tearing of the veil is the Solomonic sanctuary's most dramatic eschatological moment: the barrier to the divine presence is abolished when the one who is himself the divine presence dies outside the city gates. Access to the Most Holy Place is permanently opened through Christ's body (Heb 10:19-20)."
      }
    ],
    "15": [
      {
        "type": "theme",
        "target": "Rev 3:12",
        "note": "The two bronze pillars Jachin ('He will establish') and Boaz ('In him is strength') standing before the temple entrance carry names that read as covenant promises. In Rev 3:12 the risen Christ promises the faithful: 'The one who conquers, I will make him a pillar in the temple of my God.' The Solomonic pillars of establishment and strength become in Revelation the image of those who participate permanently in the eschatological temple through their union with Christ."
      }
    ]
  },
  "4": {
    "1": [
      {
        "type": "type",
        "target": "Heb 13:10",
        "note": "The great bronze altar for burnt offerings — the place where sacrifices were consumed — is the type behind Heb 13:10: 'We have an altar from which those who serve the tent have no right to eat.' The new-covenant altar is not a bronze structure but Christ himself, whose sacrifice is the source of spiritual sustenance. The Solomonic altar type gives Hebrews its sacrificial imagery for Christ's atoning work."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "Rev 4:6",
        "note": "The molten sea — a massive bronze basin resting on twelve oxen — prefigures the glassy sea before the heavenly throne in Rev 4:6. The temple's sea represented the cosmic waters ordered under divine sovereignty (cf. Gen 1:2, 6-8); the heavenly sea of glass in Revelation represents the same divine mastery over chaos in the eschatological throne room. The Solomonic sea is the earthly sanctuary's version of what John sees in the heavenly vision."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Heb 9:10",
        "note": "The ten basins for washing — used by the priests for purification of the burnt offerings — belong to the category of 'regulations for the body' and 'various washings' that Heb 9:10 describes as 'imposed until the time of reformation.' These ablution rituals were not arbitrary but pointed to the purification that Christ accomplishes: 'he entered once for all into the holy places... by means of his own blood' (Heb 9:12), providing the cleansing the temple washings could only symbolize."
      }
    ],
    "19": [
      {
        "type": "allusion",
        "target": "Rev 1:12-13",
        "note": "The golden lampstands placed in front of the inner sanctuary — five on the south and five on the north — connect to the vision of Revelation 1:12-13, where the risen Christ stands 'in the midst of seven golden lampstands.' The Solomonic lampstands illuminate the earthly sanctuary; the seven lampstands in Revelation represent the churches in which Christ is present and from which his light shines. The continuity of lampstand imagery from Solomon's temple to John's vision is deliberate."
      }
    ]
  },
  "5": {
    "2": [
      {
        "type": "allusion",
        "target": "1 Kgs 8:1-21",
        "note": "The Chronicler's account of the ark's transfer to the completed temple parallels 1 Kings 8:1-21 closely. Solomon's assembling of all Israel's leaders — the whole congregation — at the transfer of the ark echoes the covenantal assembly language of Sinai and anticipates the eschatological gathering. Paul applies this gathering-language to the new covenant: God's purpose is 'to unite all things in him' (Eph 1:10), the gathering that the Solomonic assembly imperfectly prefigures."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "Heb 9:7",
        "note": "The priests bringing the ark of the covenant into the inner sanctuary — the Most Holy Place — enacts the principle Hebrews describes for the high priest: 'into the second section only the high priest goes, and he but once a year, not without taking blood' (Heb 9:7). The ark's permanent installation in the Most Holy Place corresponds to Christ's single entry 'by means of his own blood' into the heavenly holy place (Heb 9:12) — both are once-for-all entries that establish permanent access rather than repeated ritual."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Heb 9:4",
        "note": "The carrying poles of the ark were so long that their tips were visible from the Holy Place but not from outside — they could be seen 'to this day.' Hebrews 9:4-5 describes the same sanctuary furniture in its theological significance: the ark, the mercy seat, the cherubim. The Chronicler's precise detail about the visible poles confirms the historical reality of the sanctuary whose theological significance Hebrews develops in full."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Heb 9:4",
        "note": "The ark contained only the two stone tablets of the Ten Commandments — 'nothing in the ark except the two tablets of stone.' Hebrews 9:4 mentions 'the tablets of the covenant' as contents of the ark alongside the golden urn of manna and Aaron's staff. The Chronicler's note that the jar of manna and Aaron's rod were no longer present (cf. Exod 16:33-34; Num 17:10) may reflect their loss before the temple period; the tablets alone endured as the covenant foundation."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Ps 118:1",
        "note": "The Levitical choir's refrain — 'For he is good; his steadfast love endures forever' — is the foundational doxology of Israel's liturgy (Ps 106:1; 107:1; 118:1; 136). The glory cloud descends precisely as this declaration of covenant faithfulness is sung. In Rev 15:3-4 the redeemed sing 'the song of Moses and the Lamb,' celebrating the same divine goodness and faithfulness in the new exodus. The refrain sung at the temple's dedication is still the substance of heavenly worship."
      },
      {
        "type": "fulfillment",
        "target": "Rev 15:3",
        "note": "The musicians and singers joining as 'one voice' to praise and give thanks as the glory filled the temple is the high point of the entire temple-building narrative. Revelation 15:3 shows the eschatological fulfillment: the redeemed standing on the glassy sea singing the song of God's greatness and holiness. The unity of voice at Solomon's dedication anticipates the unity of the redeemed multitude before the heavenly sanctuary — worship that the earthly temple could only temporarily and partially achieve."
      }
    ],
    "14": [
      {
        "type": "shadow",
        "target": "John 1:14",
        "note": "The divine glory filling the temple so completely that the priests could not stand to serve — the <em>shekinah</em> overwhelming the entire structure — is the OT's most intense theophany of divine presence in the sanctuary. John 1:14 declares that this glory found personal, incarnate expression in Jesus: 'we have seen his glory, glory as of the only Son from the Father, full of grace and truth.' The glory that filled Solomon's temple tabernacled in human flesh; the temporary, localized shekinah became permanent, personal divine presence in Christ."
      }
    ]
  }
}

def main():
    existing = load_echo('2chronicles')
    merge_echo(existing, CHRON2_ECHOES)
    save_echo('2chronicles', existing)
    print('2 Chronicles 1–5 echoes written.')

if __name__ == '__main__':
    main()
