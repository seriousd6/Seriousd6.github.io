"""
Echo Layer — 2 Samuel chapters 22–23
Run: python3 scripts/zc-echo-2samuel-22-23.py

Chapter 22 is nearly identical to Psalm 18 (David's song of deliverance).
The Psalm 18 parallel absorbed from parallels/2samuel.json as a type entry (v1).

Key echo connections:
- 22:1  — the song = Ps 18; whole-chapter type
- 22:5-7 — waves of death / cords of Sheol → death-descent-rescue pattern → Acts 2:24
- 22:10 — YHWH parting heavens and coming down → Isa 64:1; John 1:14
- 22:17 — drawn from many waters → 1 Pet 3:21 (baptism/salvation through water)
- 22:20 — rescued 'because he delighted in me' → Isa 42:1; Matt 3:17
- 22:28 — humble/proud reversal → Luke 1:51-52; Jas 4:6
- 22:29 — 'you are my lamp, O LORD' → John 8:12; Rev 21:23
- 22:50 — 'I will praise you among the nations' → Rom 15:9 (Paul cites as Christ's voice)
- 22:51 — steadfast love to anointed / descendants forever → Davidic covenant, Gal 3:16
- 23:1  — 'man raised to prominence, anointed of God' → messianic title vocabulary
- 23:2  — Spirit of YHWH speaks through David → Acts 2:30-31; 1 Pet 1:10-11
- 23:3-4 — just ruler like morning light → Mal 4:2; Rev 22:16; Luke 1:78-79
- 23:5  — everlasting covenant → Heb 13:20; Jer 31:31
- 23:39 — Uriah the Hittite last in the list → Matt 1:6 (preserved in genealogy)
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

SAMUEL_ECHOES = {
  "22": {
    "1": [
      {
        "type": "parallel",
        "target": "Ps 18:1-50",
        "note": "2 Samuel 22 and Psalm 18 are near-identical texts — David's song of deliverance preserved in two canonical locations. Minor variants between them (MT 2 Sam vs. MT Ps 18) reflect the transmission history of liturgical poetry. The placement of this poem at the end of the narrative books gives it a summarizing theological weight: the whole of David's reign is framed by YHWH's rescue of his anointed. That the psalm enters the Psalter as Ps 18 means it is available for every worshipper to pray as their own — the king's testimony becomes the congregation's speech. The NT cites Ps 18 at multiple points, reading it as the voice of Christ who was delivered from death."
      }
    ],
    "5": [
      {
        "type": "theme",
        "target": "Acts 2:24",
        "note": "The waves of death (<em>misbrê māwet</em>) engulfing David and the cords of Sheol (<em>ḥeblê šĕʾôl</em>) surrounding him describe a death-confrontation from which YHWH delivers the anointed one. Peter's Pentecost sermon cites the same death-descent-rescue structure in Ps 16:10 (= the same psalm tradition) to argue that Christ's resurrection was impossible to prevent: 'God raised him up, loosing the pangs of death, because it was not possible for him to be held by it' (Acts 2:24). David's experience of the death-assault from which YHWH rescues him is the typological matrix for the death and resurrection of the Anointed."
      }
    ],
    "10": [
      {
        "type": "type",
        "target": "John 1:14",
        "note": "YHWH's response to David's distress (v7) is described as a cosmic theophany: 'He parted the heavens and came down (<em>wayyēṭ šāmayim wayyērăd</em>).' The divine descent motif — YHWH coming down through the heavens to rescue his anointed — is the typological structure that the Incarnation fulfills. Isaiah 64:1 picks up this exact language in a prayer: 'Oh that you would tear open the heavens and come down!' John 1:14 answers: 'the Word became flesh and tabernacled among us.' The descent of YHWH through the skies to rescue David becomes the framework for understanding God's ultimate descent to rescue humanity."
      }
    ],
    "17": [
      {
        "type": "theme",
        "target": "1 Pet 3:21",
        "note": "YHWH 'reached down from on high and took me; he drew me out of many waters' (<em>yimšēnî mimmayim rabbîm</em>) — the image of rescue from the deep waters of death. The 'many waters' (<em>mayim rabbîm</em>) in ancient Near Eastern cosmology represent chaotic destruction and death. 1 Peter 3:21 uses Noah's rescue through water as a type of baptism: 'and this water symbolizes baptism that now saves you also — not the removal of dirt from the body, but the pledge of a clear conscience toward God. It saves you by the resurrection of Jesus Christ.' David's rescue from death-waters is part of the water-salvation typological chain (Exodus, Noah, baptism) that points to Christ's death and resurrection as the ultimate deliverance from the waters of death."
      }
    ],
    "20": [
      {
        "type": "fulfillment",
        "target": "Matt 3:17",
        "note": "YHWH rescues David 'because he delighted in me' (<em>kî ḥāpēṣ bî</em>) — divine favor as the basis of rescue. Psalm 18:19 repeats the same phrase. Isaiah 42:1 applies the delight-formula to the Servant: 'my chosen one in whom my soul delights.' Matthew 3:17 completes this trajectory at the baptism of Jesus: 'This is my beloved Son, with whom I am well pleased.' The divine delight in the anointed one that grounds David's rescue from death becomes the declaration over the Son at the opening of his public ministry — and ultimately the basis of his resurrection ('He was declared to be the Son of God in power... by his resurrection,' Rom 1:4)."
      }
    ],
    "28": [
      {
        "type": "theme",
        "target": "Luke 1:51",
        "note": "The summary theological principle of YHWH's dealings: 'You deliver a humble people, but your eyes are on the proud to bring them low' — the reversal pattern that governs the whole of salvation history. Luke 1:51-52 (Mary's Magnificat) states the same theology in response to the Incarnation: 'He has shown strength with his arm; he has scattered the proud in the thoughts of their hearts; he has brought down the mighty from their thrones and exalted those of humble estate.' James 4:6 cites the Proverb 3:34 form ('God opposes the proud but gives grace to the humble') as governing the Christian life. David's psalm formulates the structural law of divine government that Mary announces is being enacted in the birth of Christ."
      }
    ],
    "29": [
      {
        "type": "type",
        "target": "John 8:12",
        "note": "'For you are my lamp, O LORD, and the LORD lights up my darkness' — YHWH as personal light in the darkness of David's distress. The lamp-of-YHWH theology is developed across the OT: the <em>nēr</em> of God burns in the temple; the Davidic line is called 'a lamp for David' in the succession narratives (1 Kgs 11:36; 15:4). Jesus announces: 'I am the light of the world; whoever follows me will not walk in darkness but will have the light of life' (John 8:12). Revelation 21:23 identifies the Lamb as the lamp of the New Jerusalem: 'the city has no need of sun or moon to shine on it, for the glory of God gives it light, and its lamp is the Lamb.' What David experiences as divine illumination in crisis, the NT declares to be personal and eschatological — Christ as the light who permanently dispels darkness."
      }
    ],
    "50": [
      {
        "type": "fulfillment",
        "target": "Rom 15:9",
        "note": "'Therefore I will praise you, O LORD, among the nations (<em>baggôyim</em>), and sing praises to your name' — David's vow to praise YHWH before the nations. Paul cites this verse in Romans 15:9 as a proof-text for the Gentile mission: 'And in order that the Gentiles might glorify God for his mercy. As it is written: &ldquo;Therefore I will praise you among the Gentiles and sing to your name.&rdquo;' Paul reads the verse as the voice of Christ himself speaking — David's resolve to praise YHWH among the nations becomes Christ's declaration that his mission extends to all peoples. The Gentile mission is not a Plan B but was encoded in the Davidic covenant: the anointed one's praise was always to resound among the nations."
      }
    ],
    "51": [
      {
        "type": "fulfillment",
        "target": "Gal 3:16",
        "note": "The closing verse of the poem: YHWH 'shows steadfast love to his anointed — to David and his descendants (<em>wəlzarʿô</em>) forever' — the covenantal promise that the Davidic line will permanently possess divine <em>ḥesed</em>. Galatians 3:16 applies the same 'seed' (<em>zera</em>) / 'offspring' logic to the Abrahamic promise: 'Now the promises were made to Abraham and to his offspring. It does not say &ldquo;and to offsprings,&rdquo; referring to many, but referring to one, &ldquo;and to your offspring,&rdquo; who is Christ.' The same exegetical move applies here: the promise of eternal <em>ḥesed</em> to David&rsquo;s seed finds its fulfillment not in the biological descendants of David collectively (who eventually fail) but in the one descendant who endures forever — Christ, who sits on David's throne and whose covenant God keeps with perfect faithfulness."
      }
    ]
  },
  "23": {
    "1": [
      {
        "type": "type",
        "target": "Acts 2:30",
        "note": "David's oracle uses a cluster of messianic title-vocabulary: 'the declaration of the man God raised to prominence (<em>hāʾîš huqqam ʿal</em>)' and 'the anointed of the God of Jacob (<em>mĕšîaḥ ʾĕlōhê yaʿăqōḇ</em>).' The 'raised to prominence' phrase anticipates the resurrection-exaltation language that Peter applies to Jesus: 'Being therefore a prophet, and knowing that God had sworn with an oath to him that he would set one of his descendants on his throne, he foresaw and spoke about the resurrection of the Christ' (Acts 2:30). The title <em>māšîaḥ</em> — anointed — applied to David in his last oracle becomes the technical term for the promised heir whose anointing and exaltation exceeds David's. The oracle is in effect David introducing the Christ by introducing himself as the type."
      }
    ],
    "2": [
      {
        "type": "theme",
        "target": "1 Pet 1:11",
        "note": "'The Spirit of the LORD speaks through me; his word is on my tongue' — David claims direct prophetic inspiration: what he speaks is YHWH's own speech. 1 Peter 1:10-11 generalizes this to all the prophets: 'the prophets... inquired carefully, inquiring what person or time the Spirit of Christ in them was indicating when he predicted the sufferings of Christ and the subsequent glories.' The Spirit at work in David's last words is the Spirit of Christ — the same Spirit who would inhabit the Messiah (Isa 11:2; 61:1) is the one speaking through David here. Acts 2:30-31 makes the connection explicit: David was a prophet and spoke about Christ's resurrection. David's claim that the Spirit speaks through him becomes the apostolic framework for all OT messianic interpretation."
      }
    ],
    "3": [
      {
        "type": "fulfillment",
        "target": "Mal 4:2",
        "note": "The just ruler who 'rules in the fear of God' is 'like the light of morning, like sunrise on a cloudless day (<em>kəʾôr bōqer yizraḥ šemeš</em>), like the gleam of rain on green grass after showers' — light imagery as the defining characteristic of the ideal Davidic ruler. Malachi 4:2 develops this solar imagery into a messianic promise: 'But for you who fear my name, the sun of righteousness (<em>šemeš ṣĕdāqāh</em>) will rise with healing in its wings.' Luke 1:78-79 quotes the same dawn-imagery of the Messiah: 'the sunrise from on high will visit us, to give light to those who sit in darkness and in the shadow of death.' Revelation 22:16 has Jesus identify himself: 'I am the bright morning star.' The light-of-morning that characterizes the ideal ruler becomes the identity of the Messiah himself."
      }
    ],
    "5": [
      {
        "type": "fulfillment",
        "target": "Heb 13:20",
        "note": "David's concluding declaration: 'he has made with me an everlasting covenant (<em>bĕrît ʿôlām</em>), ordered and secured in every way.' The Davidic covenant's eternal character is the ground of David's confidence. Hebrews 13:20 applies the identical language to the new covenant ratified in Christ's death and resurrection: 'the God of peace who brought again from the dead our Lord Jesus, the great shepherd of the sheep, by the blood of the eternal covenant.' The blood of the eternal covenant is the fulfillment of the everlasting covenant God made with David — the same divine commitment to the Davidic king, now expressed through the sacrificial death of the Davidic heir. The covenant that David received in promise David's son ratifies in blood."
      }
    ],
    "39": [
      {
        "type": "theme",
        "target": "Matt 1:6",
        "note": "Uriah the Hittite appears last in the list of David's thirty-seven mighty men — the man whose murder David arranged, placed at the conclusion of the honor roll. The narrator does not comment; the name stands as a permanent indictment in the historical record. Matthew 1:6 preserves the same uncomfortable fact in the genealogy of Christ: 'David was the father of Solomon by the wife of Uriah.' Matthew names the woman by her marital connection to Uriah, not by her own name — keeping Uriah's claim in the genealogical record. The faithful warrior who died because his king coveted his wife is remembered in both the historical narrative and the messianic genealogy as a testimony to grace: the covenant continues through the very line tainted by the crime, and the victim&rsquo;s name stands permanently in the record as a witness to both human sin and divine faithfulness."
      }
    ]
  }
}

def main():
    existing = load_echo('2samuel')
    merge_echo(existing, SAMUEL_ECHOES)
    save_echo('2samuel', existing)
    print('2 Samuel 22-23 echoes written.')

if __name__ == '__main__':
    main()
