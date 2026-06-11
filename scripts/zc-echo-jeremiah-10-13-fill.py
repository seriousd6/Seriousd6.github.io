"""
MKT Echo Layer — Jeremiah chapters 10–13
Run: python3 scripts/zc-echo-jeremiah-10-13-fill.py

Key echo decisions:
- 10:6-7 'who should not fear you, King of the nations' is quoted almost verbatim in
  Rev 15:3-4 (song of Moses and Lamb); 10:10 'true God / living God' echoes John 17:3
- 11:19 'lamb led to slaughter' is one of the key Servant-of-Isaiah passages; the
  echo runs through Isa 53:7 and is directly activated in Acts 8:32
- 12:7 'I have abandoned my house' → Matt 23:38 Jesus's temple-abandonment pronouncement;
  one of the most direct Jeremiah → Jesus structural echoes
- 13:23 'can a leopard change its spots' → Paul's anthropology in Rom 7:18 / John 3:6
  (the impossibility of self-reform without regeneration)
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

JER_ECHOES = {
  "10": {
    "3": [
      {
        "type": "theme",
        "target": "Acts 17:29",
        "note": "Jeremiah's polemic against craftsmen who cut timber and fashion it into a deity anticipates Paul's Areopagus conclusion: 'we should not think the divine being is like gold or silver or stone — an image made by human design and skill.' Both texts argue that any image that required human labor to produce cannot be the Creator."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "Rev 15:4",
        "note": "The song of Moses and the Lamb in Rev 15:3-4 echoes Jer 10:7 almost verbatim: 'who will not fear you, Lord, and bring glory to your name? ... King of the nations.' John's heavenly hymn draws on the Jeremianic anti-idol polemic to frame the eschatological worship of Christ."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "John 17:3",
        "note": "Jeremiah's 'the LORD is the true God ... the living God' is the foundation for Jesus's high-priestly prayer definition: 'this is eternal life: that they know you, the only true God, and Jesus Christ, whom you have sent.' The Jeremian monotheism is fulfilled and specified in the Trinitarian revelation of the Incarnation."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "Col 1:16",
        "note": "Jacob's God is 'the maker of all things' — the same comprehensive creation attribution that Paul applies to Christ in Col 1:16 ('by him all things were created: things in heaven and on earth'). The creator-deity of Jeremiah's anti-idol polemic is identified in the NT with the pre-incarnate Christ."
      }
    ]
  },
  "11": {
    "19": [
      {
        "type": "allusion",
        "target": "Isa 53:7",
        "note": "Jeremiah's self-description as 'a gentle lamb led to slaughter' who did not know the conspiracy against him is one of the prophetic prototypes that Isaiah 53:7 draws on and applies to the Suffering Servant. The NT activates both passages: Acts 8:32-33 quotes Isa 53:7 at the Ethiopian eunuch's conversion, and the lamb-to-slaughter image is applied to Jesus throughout (John 1:29; Rev 5:6)."
      },
      {
        "type": "type",
        "target": "John 1:29",
        "note": "The innocent prophet who is targeted for death because of his faithful proclamation — led like a lamb to slaughter — is structurally the prophetic type that finds fulfillment in Jesus. John the Baptist's acclamation 'behold the Lamb of God who takes away the sin of the world' activates this entire prophetic-lamb trajectory."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Rev 6:10",
        "note": "Jeremiah's appeal 'let me see your vengeance on them, for to you I have committed my cause' resurfaces in the cry of the martyrs under the altar in Rev 6:10: 'How long, Sovereign Lord, holy and true, until you judge the inhabitants of the earth and avenge our blood?' Both are the covenant-loyalty cry of suffering witnesses awaiting divine vindication."
      }
    ]
  },
  "12": {
    "1": [
      {
        "type": "theme",
        "target": "Rev 16:7",
        "note": "Jeremiah's theodicy question — why does the way of the wicked prosper? — is the OT's recurrent challenge that Revelation resolves with the angel's declaration: 'Yes, Lord God Almighty, true and just are your judgments.' The justice that Jeremiah demanded and could not yet see is publicly vindicated in the final judgment."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Heb 12:1",
        "note": "YHWH's challenge to Jeremiah — if you cannot keep pace with foot-soldiers, how will you compete with horses? — reframes spiritual endurance as a graduated escalation. Hebrews 12:1 draws on the same athletic-endurance metaphor: 'let us run with perseverance the race marked out for us, fixing our eyes on Jesus' — the very answer to the escalation challenge Jeremiah faced."
      }
    ],
    "7": [
      {
        "type": "fulfillment",
        "target": "Matt 23:38",
        "note": "YHWH's lament 'I have abandoned my house; I have forsaken my inheritance; I have handed the one I deeply love over to her enemies' is the precise theological background for Jesus's pronouncement over Jerusalem: 'your house is left to you desolate' (Matt 23:38; Luke 13:35). Jesus, standing in the temple, enacts the Jeremianic divine departure — the same abandonment of the sanctuary that preceded 587 BCE is now announced for 70 CE."
      }
    ],
    "14": [
      {
        "type": "theme",
        "target": "Acts 15:17",
        "note": "YHWH's promise to uproot Israel's wicked neighbors but then restore them if they learn Israel's ways parallels the Gentile mission logic that James cites from Amos 9:11-12 at the Jerusalem Council (Acts 15:16-17): the restoration of David's tent so 'that the rest of mankind may seek the Lord, even all the Gentiles who bear my name.' Both texts ground Gentile inclusion in covenant extension."
      }
    ]
  },
  "13": {
    "11": [
      {
        "type": "allusion",
        "target": "John 15:4",
        "note": "YHWH's comparison of Israel's covenant intimacy to a sash clinging to a person's waist — 'so I bound the whole house of Israel ... to myself' — uses the same bonding-intimacy logic that Jesus applies to abiding in the vine: 'remain in me, as I also remain in you' (John 15:4). Both texts treat covenant attachment as organic union; the sash that is separated from YHWH becomes worthless, as does the branch cut from the vine."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "John 12:35",
        "note": "Jeremiah's urgent call 'give honor to the LORD your God before he brings darkness — before your feet stumble on the darkening mountains' uses the identical darkness-and-stumbling metaphor that Jesus inverts into an invitation: 'walk while you have the light, before darkness overtakes you ... whoever walks in the dark does not know where they are going' (John 12:35). Both texts treat the darkness as an eschatological deadline for response."
      }
    ],
    "23": [
      {
        "type": "allusion",
        "target": "Rom 7:18",
        "note": "The rhetorical impossibility of self-transformation in Jer 13:23 — 'can a Cushite change his skin, or a leopard its spots? Neither can you do good' — is the OT foundation for Paul's diagnosis in Rom 7:18: 'I know that nothing good dwells in me, that is, in my sinful nature. For I have the desire to do what is good, but I cannot carry it out.' Both texts establish the necessity of divine transformation rather than moral self-improvement."
      },
      {
        "type": "allusion",
        "target": "John 3:6",
        "note": "The leopard-spots impossibility grounds Jesus's Nicodemus conversation: 'that which is born of flesh is flesh, and that which is born of Spirit is Spirit' (John 3:6). The new birth is the divine answer to the leopard-spots problem — the transformation that is humanly impossible becomes possible through the Spirit's regenerative work."
      }
    ]
  }
}

def main():
    existing = load_echo('jeremiah')
    merge_echo(existing, JER_ECHOES)
    save_echo('jeremiah', existing)

    out = json.loads((ROOT / 'data/echoes/jeremiah.json').read_text())
    for ch in range(10, 14):
        ck = str(ch)
        entries = out.get(ck, {})
        status = 'done' if entries else 'MISSING'
        count = sum(len(v) for v in entries.values())
        print(f'  ch {ch}: {status} ({count} echo entries across {len(entries)} verses)')

if __name__ == '__main__':
    main()
