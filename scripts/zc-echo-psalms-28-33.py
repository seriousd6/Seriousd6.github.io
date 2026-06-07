"""
Echo data — Psalms chapters 28–33 (gap-fill: chs 28, 29, 30, 33 missing; 31, 32 already present)
Run: python3 scripts/zc-echo-psalms-28-33.py

Key connections:
- Ps 28:8: "his anointed one" (meshicho) — direct Messianic title; the Psalm's
  saving fortress is the strength of the Christ. v9 "be their shepherd" → John 10.
- Ps 29:3-4: Voice of the LORD over the waters → Matt 3:16-17 (voice at baptism
  over the Jordan); v9 "Glory!" in the temple → John 12:28 / Rev 4:8.
- Ps 30:3: "you brought my soul up from the realm of the dead" → Acts 2:31 as
  Peter's resurrection proof-text; v5 "weeping by night, joy in the morning" →
  John 16:20-22 / the Easter morning pattern.
- Ps 33:6: "heavens made by the word of the LORD" → John 1:3 / Col 1:16 (the
  pre-incarnate Word as the agent of creation); v3 "new song" → Rev 5:9
  (the Lamb's new song of redemption); v12 "chosen as his own possession" →
  1 Pet 2:9.
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

# INTENT: Echo data for Psalms 28, 29, 30, 33 — covering the Messianic Anointed
#   (Ps 28:8), the divine Voice over the waters at baptism (Ps 29:3), the
#   resurrection from Sheol (Ps 30:3, Peter's proof-text in Acts 2), and the
#   creative Word (Ps 33:6, John 1:3).
# CHANGE? If data/echoes/psalms.json structure changes, update load_echo/save_echo
#   per Z_COMMENTARY_SCRIPT_GUIDE.md.
# VERIFY: python3 -c "import json; d=json.load(open('data/echoes/psalms.json')); print([len(d.get(str(c),{})) for c in range(28,34)])" should show non-zero for 28,29,30,33.

PSALMS_ECHOES = {
  "28": {
    "1": [
      {
        "type": "allusion",
        "target": "1 Cor 10:4",
        "note": "To you, O LORD, I call; my Rock — 1 Cor 10:4 identifies the Rock that accompanied Israel in the wilderness as Christ: 'they drank from the spiritual rock that accompanied them, and that rock was Christ.' The Psalm's address to the LORD as 'my Rock' is prayer addressed to the one who is identified in the NT as the pre-incarnate Son — the rock that David trusts is the Christ who will come."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "Heb 7:25",
        "note": "Hear my cry for mercy as I lift my hands toward your Most Holy Place — the lifting of hands toward the sanctuary is the gesture of priestly intercession. Heb 7:25: 'he always lives to intercede for them' — Jesus as the permanent high priest whose intercession before the Father is the NT fulfillment of the gesture David enacts toward the Holy Place. The hands lifted toward the sanctuary become the hands lifted in eternal priestly intercession."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "Phil 4:13",
        "note": "The LORD is my strength and my shield; my heart trusts in him and I am helped; my heart leaps for joy — Phil 4:13: 'I can do all things through him who strengthens me.' The pattern is identical: trust in God → divine strengthening → resulting joy and thanksgiving. The Christ who strengthens Paul is the LORD who strengthens David."
      }
    ],
    "8": [
      {
        "type": "type",
        "target": "Ps 2:2",
        "note": "He is the saving fortress of his anointed one (meshicho) — the 'anointed one' (Messiah) is explicitly named as the one whose strength is YHWH. Ps 2:2 declares the nations rage 'against the LORD and against his anointed one' — the same term. The pattern of Psalm 28:8 (Anointed's strength entirely derived from YHWH) is the pattern of the Son who says 'the Son can do nothing by himself; he can only do what he sees his Father doing' (John 5:19)."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "John 10:11",
        "note": "Be their shepherd and carry them forever — 'I am the good shepherd. The good shepherd lays down his life for the sheep' (John 10:11). The prayer for God to shepherd and carry his people is answered in Jesus as the Good Shepherd who carries the lost sheep on his shoulders (Luke 15:5) and gently leads those who are weary (Isa 40:11). The petition of Psalm 28:9 is the job description of Christ the Shepherd."
      }
    ]
  },
  "29": {
    "3": [
      {
        "type": "allusion",
        "target": "Matt 3:16",
        "note": "The voice of the LORD is over the waters — the theophanic divine voice thundering over the waters in Psalm 29 is echoed at the baptism: the Spirit descends over the Jordan waters and the Father's voice speaks (Matt 3:16-17: 'a voice from heaven said, \"This is my Son, whom I love; with him I am well pleased.\"'). The divine voice over the waters at creation (Gen 1:2) and in Psalm 29 reaches its climax when the Father speaks over the Jordan at the Son's baptism."
      },
      {
        "type": "allusion",
        "target": "John 1:1",
        "note": "The voice of the LORD — 'In the beginning was the Word (Logos), and the Word was with God, and the Word was God' (John 1:1). The 'voice of the LORD' that thunders seven times through Psalm 29 is the OT expression of the divine Word that John 1 identifies as the pre-incarnate Christ. The creative and theophanic word of YHWH that shakes creation is the Word who becomes flesh."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "Rev 1:15",
        "note": "The voice of the LORD is powerful; the voice of the LORD is majestic — Rev 1:15 describes the risen Christ: 'his voice was like the sound of rushing waters.' The voice of the LORD that Psalm 29 describes as powerful and majestic is the voice that John hears from the risen Christ in the Patmos vision. The cosmic voice of YHWH in the Psalm is the voice of the resurrected Son."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "John 12:28",
        "note": "In his temple all cry, 'Glory!' — the Father's voice speaks glory in John 12:28: 'Father, glorify your name! Then a voice came from heaven: \"I have glorified it, and will glorify it again.\"' The temple-glory cry of Psalm 29 is answered in the Father's declaration of glory through the Son's death and resurrection. Both involve the divine voice producing a glory-response in the worshipping community."
      },
      {
        "type": "allusion",
        "target": "Rev 4:8",
        "note": "In his temple all cry, 'Glory!' — Rev 4:8: the four living creatures 'day and night never stop saying: \"Holy, holy, holy is the Lord God Almighty, who was, and is, and is to come.\"' The heavenly temple worship of Revelation is the eternal form of Psalm 29's temple-chorus. The Lamb who opens the seals (Rev 5:6-7) is the one through whom the glory-cry reaches its fullest expression."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Rev 19:6",
        "note": "The LORD sits enthroned as King forever — 'Hallelujah! For our Lord God Almighty reigns' (Rev 19:6). The eternal kingship of YHWH enthroned over the waters (Ps 29:10) reaches its eschatological expression in Rev 19:6's proclamation of divine reign. Christ's resurrection and ascension are his taking up of the eternal throne the Psalm describes — the throne with the Lamb at its center (Rev 5:6; 7:17)."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "John 14:27",
        "note": "The LORD blesses his people with peace (shalom) — 'Peace I leave with you; my peace I give you. I do not give to you as the world gives' (John 14:27). The shalom-blessing of Psalm 29:11 is the blessing Christ bestows at the last supper and enacts through his resurrection appearances: 'Peace be with you' (John 20:19, 21, 26). The LORD who gives his people strength and peace is identified in John as the risen Christ."
      }
    ]
  },
  "30": {
    "3": [
      {
        "type": "fulfillment",
        "target": "Acts 2:31",
        "note": "LORD, you brought my soul up from the realm of the dead; you restored my life from among those who descend to the pit — Peter cites Psalm 16:10 as the resurrection proof-text in Acts 2:31, but Psalm 30:3 expresses the same theology of divine rescue from Sheol that becomes the template for the resurrection proclamation. Acts 2:24: 'God raised him from the dead, freeing him from the agony of death, because it was impossible for death to keep its hold on him.' The Psalm's movement from Sheol to life is the pattern Christ enacts definitively."
      }
    ],
    "5": [
      {
        "type": "fulfillment",
        "target": "John 16:20",
        "note": "Weeping may remain through the night, but joy arrives with the morning — 'you will weep and mourn while the world rejoices. You will grieve, but your grief will turn to joy' (John 16:20). Jesus applies the Psalm's night-weeping/morning-joy pattern directly to his disciples: the crucifixion is the night of grief; the resurrection is the morning of joy. John 20:1: 'Early on the first day of the week, while it was still dark, Mary Magdalame went to the tomb' — night turning to morning in literal fulfillment."
      },
      {
        "type": "allusion",
        "target": "Rev 21:4",
        "note": "Weeping may remain through the night, but joy arrives with the morning — the eschatological form is Rev 21:4: 'he will wipe every tear from their eyes. There will be no more death or mourning or crying or pain, for the old order of things has passed away.' The night-weeping/morning-joy pattern of Psalm 30:5 is the temporal shadow of which the new creation's permanent, tearless joy is the eternal substance."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Luke 24:5",
        "note": "Can the dust praise you? Can it proclaim your faithfulness? — the argument that death prevents praise is implicitly answered by the resurrection. Luke 24:5: 'Why do you look for the living among the dead? He is not here; he has risen!' The risen Christ proves that the body raised from the grave can praise and proclaim — death does not have the final word. The resurrection is the answer to Psalm 30:9's rhetorical question: yes, through Christ, the raised dust can and will proclaim God's faithfulness."
      }
    ],
    "11": [
      {
        "type": "fulfillment",
        "target": "John 20:20",
        "note": "You have turned my mourning into dancing; you have removed my sackcloth and clothed me with joy — 'he showed them his hands and side. The disciples were overjoyed when they saw the Lord' (John 20:20). The mourning-to-dancing, sackcloth-to-joy transformation of Psalm 30:11 is precisely enacted on Easter evening: the disciples' locked-door grief (John 20:19) turned to joy by the appearance of the risen Christ. The Psalm provides the emotional template for the first Easter appearance."
      }
    ]
  },
  "33": {
    "3": [
      {
        "type": "allusion",
        "target": "Rev 5:9",
        "note": "Sing him a new song — 'they sang a new song: \"You are worthy to take the scroll and to open its seals, because you were slain, and with your blood you purchased for God persons from every tribe and language and people and nation\"' (Rev 5:9). The 'new song' of Psalm 33:3 reaches its eschatological form in the Lamb's song of redemption. The new song commanded by the Psalm is the song that all creation sings only once the slain-and-risen Lamb is revealed."
      }
    ],
    "6": [
      {
        "type": "fulfillment",
        "target": "John 1:3",
        "note": "The heavens were made by the word of the LORD, and all their host by the breath of his mouth — 'through him all things were made; without him nothing was made that has been made' (John 1:3). Psalm 33:6 is the OT foundation for John 1:3's identification of the Logos as the agent of creation. The 'word of the LORD' by which the heavens were made is the personal Word who became flesh (John 1:14). The breath/Spirit pairing in Psalm 33:6 maps onto the Word-and-Spirit creation act of John 1:1-3."
      },
      {
        "type": "fulfillment",
        "target": "Col 1:16",
        "note": "The heavens were made by the word of the LORD — 'for in him all things were created: things in heaven and on earth, visible and invisible, whether thrones or powers or rulers or authorities; all things have been created through him and for him' (Col 1:16). The Psalm's word-of-the-LORD creator is the one Paul identifies as Christ — the pre-incarnate Son through whom all things came into being and are sustained (Col 1:17)."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Mark 4:39",
        "note": "For he spoke, and it came to be; he commanded, and it stood firm — 'he got up, rebuked the wind and said to the waves, \"Quiet! Be still!\" Then the wind died down and it was completely calm' (Mark 4:39). The disciples' question 'Who is this? Even the wind and the waves obey him!' (Mark 4:41) is answered by Psalm 33:9 — this is the one who speaks and it comes to be. Jesus exercises over creation the same creative authority the Psalm attributes to YHWH's spoken word."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Acts 2:23",
        "note": "The counsel of the LORD stands forever, the purposes of his heart through all generations — 'this man was handed over to you by God's deliberate plan and foreknowledge' (Acts 2:23). Peter's Pentecost declaration presents the crucifixion as the execution of God's eternal counsel (Ps 33:11). The cross that looked like human violence was the outworking of the divine plan that stands forever — the Lamb 'slain from the creation of the world' (Rev 13:8) is the counsel of God made flesh."
      }
    ],
    "12": [
      {
        "type": "fulfillment",
        "target": "1 Pet 2:9",
        "note": "Blessed is the nation whose God is the LORD — the people he has chosen as his own possession — 'you are a chosen people, a royal priesthood, a holy nation, God's special possession' (1 Pet 2:9). Peter applies the language of Israel's election directly to the church drawn from all nations. The 'people chosen as his own possession' (Ps 33:12) is the community that Christ gathers 'from every nation, tribe, people and language' (Rev 7:9) — the Psalm's national election language universalized through the Messiah."
      }
    ],
    "22": [
      {
        "type": "allusion",
        "target": "Jude 21",
        "note": "Let your steadfast love, LORD, rest on us, as we have placed our hope in you — 'keep yourselves in God's love as you wait for the mercy of our Lord Jesus Christ to bring you to eternal life' (Jude 21). The Psalm's closing petition (abide in God's hesed + hope) is the posture Jude commands for the church. The steadfast love (hesed) that the Psalm asks to rest on the people is the love that reaches its personal embodiment in Jesus, the one in whom God's faithful love becomes incarnate (John 1:14: 'full of grace and truth')."
      }
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    for ch in ['28','29','30','31','32','33']:
        entries = len(existing.get(ch, {}))
        print(f"  ch{ch}: {entries} verses with entries")
    print("Psalms 28–33 echoes complete.")

if __name__ == '__main__':
    main()
