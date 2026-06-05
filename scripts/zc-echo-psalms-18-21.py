"""
Echo layer — Psalms 18–21 (OT echo: forward direction, OT → NT)
Output: data/echoes/psalms.json (creates entries for Psalms 18–21)

Psalms 18–21 form a royal cluster: Ps 18 (great deliverance psalm = 2 Sam 22),
Ps 19 (creation + Torah), Ps 20 (pre-battle intercession), Ps 21 (post-victory
thanksgiving). All four are Davidic royal psalms interpreted Messianically in the NT.

Key echo zones:
- 18:4-5  → Acts 2:24 — cords of death; impossible for death to hold
- 18:43-44 → Eph 1:20-22 — head of nations; all things under his feet
- 18:49   → Rom 15:9 — I will praise you among the nations (Gentile inclusion text)
- 18:50   → Luke 1:32-33 — steadfast love to David and his descendants forever
- 19:1-4  → Rom 1:20 — creation testifying to God's existence and power
- 19:4    → Rom 10:18 — voice gone out through all the earth (gospel proclamation)
- 19:9    → Rev 16:7; 19:2 — true and just judgments
- 20:6    → Acts 2:36 — YHWH saves his anointed (meshicho / Messiah)
- 21:4    → Acts 2:28 — life forever and ever; resurrection life
- 21:5    → Phil 2:9-11; Rev 5:12 — splendor and majesty after salvation
- 21:8-12 → Rev 19:11-21 — king's right hand destroying enemies

Parallels absorbed (data/parallels/psalms.json):
  18:1 → 2 Sam 22:1-51 (parallel)   [not an OT→NT echo; skipped]
  18:49 → Rom 15:9   (quotation-source)
  19:4  → Rom 10:18  (quotation-source)

Run: python3 scripts/zc-echo-psalms-18-21.py
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

ECHOES = {
  "18": {
    "1": [
      {"type": "allusion", "target": "Matt 12:18", "note": "Matthew applies the Servant title ('my servant whom I have chosen') from Isa 42:1 to Jesus in direct continuity with Ps 18's superscription 'Of David the servant of the LORD.' The 'servant of YHWH' title that David bears in Psalm 18 finds its fullest referent in Jesus, the ultimate Servant of the LORD — both Davidic king and Isaianic Servant"}
    ],
    "4": [
      {"type": "allusion", "target": "Acts 2:24", "note": "'God raised him from the dead, freeing him from the agony of death, because it was impossible for death to keep its hold on him.' Peter's sermon invokes the language of Ps 18:4-5 ('the cords of death entangled me; the torrents of destruction overwhelmed me; the ropes of Sheol coiled around me') to describe what Jesus escaped in resurrection. The psalmist's cry of release from Sheol's grip is fulfilled in Christ's resurrection from death's actual hold"},
      {"type": "allusion", "target": "Rev 1:18", "note": "'I am the Living One; I was dead, and now look, I am alive for ever and ever! And I hold the keys of death and Hades.' The Risen Christ holds the 'keys' of the domain described in Ps 18:4-5 — Sheol and death that once threatened to hold their victim. Christ's resurrection converts the psalmist's escape from death's cords into Christ's permanent authority over death's realm"}
    ],
    "6": [
      {"type": "allusion", "target": "Heb 4:16", "note": "'Let us therefore approach the throne of grace with confidence, so that we may receive mercy and find grace to help us in our time of need.' Hebrews' invitation to approach the heavenly throne takes up the pattern of Ps 18:6 — 'From his temple he heard my voice; my cry came before him, into his ears.' The heavenly sanctuary-access that Ps 18:6 celebrates as YHWH's hearing becomes the basis for Hebrews' invitation to draw near to the throne of Christ in his heavenly sanctuary"}
    ],
    "35": [
      {"type": "allusion", "target": "Matt 11:29", "note": "Ps 18:35 — 'your right hand held me up, and your gentleness (<em>anavah</em>) made me great' — uses the same meekness/gentleness word that Jesus invokes: 'I am gentle (<em>praüs</em>) and humble in heart.' The Davidic king made great through divine gentleness is the prototype of the Messianic King who is identified by his gentleness; royal greatness comes through servant-lowliness"}
    ],
    "43": [
      {"type": "allusion", "target": "Eph 1:20-22", "note": "'He raised Christ from the dead and seated him at his right hand in the heavenly realms, far above all rule and authority... and placed all things under his feet and appointed him to be head over everything for the church.' Paul's exaltation-Christology fulfills Ps 18:43-44 — 'You made me head of the nations; peoples I did not know now serve me.' What David partially experienced as Gentile submission is universally accomplished in Christ's exaltation over all nations"},
      {"type": "allusion", "target": "Phil 2:9-11", "note": "'Therefore God exalted him to the highest place and gave him the name that is above every name, that at the name of Jesus every knee should bow... and every tongue acknowledge that Jesus Christ is Lord.' Phil 2:9-11 universalizes Ps 18:43-45 — 'foreigners submitted to me; as soon as they heard of me they obeyed' — from David's imperial experience to the cosmic submission of all creation to Christ's name"}
    ],
    "49": [
      {"type": "quote", "target": "Rom 15:9", "note": "Paul quotes Ps 18:49 ('Therefore I will praise you among the Gentiles; I will sing the praises of your name') as the first OT proof-text for his argument that Christ has made Gentile worship of Israel's God possible. The psalmist's praise among the nations was partial fulfillment in David's reign; Paul reads it as fully realized in Christ's death-and-resurrection opening the Gentile mission. This is Paul's foundational citation for the entire Gentile-inclusion argument of Romans 15"},
      {"type": "allusion", "target": "Heb 2:12", "note": "Hebrews also draws on the 'I will proclaim your name to my brothers; in the assembly I will praise you' strand of this psalm-family (quoting Ps 22:22 but in the same royal-declaration tradition). Christ as the one who praises the Father 'among the nations' and 'among his brothers' integrates Ps 18:49's royal testimony with the Christological identification of Jesus as the one who offers humanity's worship to God"}
    ],
    "50": [
      {"type": "allusion", "target": "Luke 1:32-33", "note": "'The Lord God will give him the throne of his father David, and he will reign over Jacob's descendants forever; his kingdom will never end.' Gabriel's promise to Mary echoes Ps 18:50 — 'He shows steadfast love to his anointed, to David and to his descendants forever.' The 'forever' of Ps 18:50 is the promise that Gabriel declares fulfilled in Jesus: the covenant-faithfulness to David's line reaches its terminus in the Son of David whose kingdom has no end"},
      {"type": "allusion", "target": "Acts 2:30", "note": "'But he was a prophet and knew that God had promised him on oath that he would place one of his descendants on his throne.' Peter's Pentecost sermon draws on the Davidic-descent promise (Ps 132:11; 2 Sam 7:12) that Ps 18:50 also expresses. The 'steadfast love to David and his descendants forever' was the covenant that made the resurrection of a Davidic descendant both possible and necessary — God could not let the line end in death"}
    ]
  },
  "19": {
    "1": [
      {"type": "allusion", "target": "Rom 1:20", "note": "'For since the creation of the world God's invisible qualities — his eternal power and divine nature — have been clearly seen, being understood from what has been made, so that people are without excuse.' Paul's doctrine of general revelation in Romans 1:20 articulates what Ps 19:1-4 expresses poetically: the creation itself bears witness to the Creator. The heavens 'declare' (<em>sipperim</em>, pour out speech) in Ps 19:1-2; Paul says this declaration renders all humanity accountable"},
      {"type": "allusion", "target": "Heb 1:3", "note": "'The Son is the radiance of God's glory and the exact representation of his being, sustaining all things by his powerful word.' The heavens 'declaring the glory of God' (Ps 19:1) is the creation-context for Hebrews' statement that the Son is the radiance (<em>apaugasma</em>) of that very glory. The creation-speech of Ps 19 is the Son's medium of self-disclosure in Hebrews"}
    ],
    "4": [
      {"type": "quote", "target": "Rom 10:18", "note": "Paul quotes Ps 19:4 in his argument about Israel's accountability for rejecting the gospel: 'But I ask: Did they not hear? Of course they did: Their voice has gone out into all the earth, their words to the ends of the world.' Paul reads the creation's universal proclamation (Ps 19:4) as a type of the gospel's universal reach — just as no part of the earth is beyond creation's testimony, no part of the earth is beyond the gospel's reach. Israel has heard"},
      {"type": "allusion", "target": "Col 1:23", "note": "'This is the gospel that you heard and that has been proclaimed to every creature under heaven.' Paul's claim that the gospel has been universally proclaimed draws on the same Ps 19:4 language of universal proclamation. The creation-voice that has reached all the earth (Ps 19) is now the gospel-voice; both cover the same universal ground"}
    ],
    "7": [
      {"type": "allusion", "target": "2 Tim 3:16-17", "note": "'All Scripture is God-breathed and is useful for teaching, rebuking, correcting and training in righteousness, so that the servant of God may be thoroughly equipped for every good work.' The qualities Paul attributes to Scripture — perfect, trustworthy, making wise — are exactly the qualities Ps 19:7-9 applies to the Torah ('the instruction of the LORD is perfect, reviving the soul; the testimony of the LORD is trustworthy, making wise the simple'). Paul's doctrine of Scripture is the Ps 19 Torah-theology applied to the whole canon"},
      {"type": "allusion", "target": "Jas 1:25", "note": "'But whoever looks intently into the perfect law that gives freedom, and continues in it — not forgetting what they have heard, but doing it — they will be blessed in what they do.' James's 'perfect law that gives freedom' echoes Ps 19:7 ('the instruction of the LORD is perfect, reviving the soul') and 19:11 ('in keeping them there is great reward'). The Torah's perfection celebrated in Ps 19 reappears in James as 'the perfect law that gives freedom' — the Messianically transformed Torah"}
    ],
    "9": [
      {"type": "allusion", "target": "Rev 16:7", "note": "'I heard the altar respond: Yes, Lord God Almighty, true and just are your judgments.' The heavenly worship in Revelation echoes the vocabulary of Ps 19:9 — 'the judgments of the LORD are true and altogether righteous.' The doxological affirmation of divine judgment's truth-and-righteousness that Ps 19 celebrates becomes the eschatological declaration of the heavenly assembly as God's wrath is poured out"},
      {"type": "allusion", "target": "Rev 19:2", "note": "'For true and just are his judgments. He has condemned the great prostitute who corrupted the earth by her adulteries. He has avenged on her the blood of his servants.' The Babylon-judgment doxology in Rev 19:2 uses the same 'true and just' (alēthinai kai dikaiai) language as Ps 19:9. The creation-order righteous judgments of Ps 19 find their eschatological completion in the final judgment of corrupt earthly power"}
    ],
    "10": [
      {"type": "allusion", "target": "Rev 10:9-10", "note": "'I took the little scroll from the angel's hand and ate it. It tasted as sweet as honey in my mouth, but when I had eaten it, my stomach turned sour.' John's scroll-eating echoes Ezek 3:3 primarily, but also Ps 19:10 — 'They are sweeter than honey, than honey from the honeycomb.' The prophetic word that is sweet to taste but bitter in its message of judgment combines both Ezekiel's and the Psalm's honey-sweetness imagery"}
    ]
  },
  "20": {
    "6": [
      {"type": "allusion", "target": "Acts 2:36", "note": "'Therefore let all Israel be assured of this: God has made this Jesus, whom you crucified, both Lord and Messiah.' Peter's Pentecost proclamation that God 'made' (appointed/vindicated) Jesus as Lord and Messiah fulfills the pattern of Ps 20:6 — 'Now I know that the LORD saves his anointed (<em>meshicho</em>); he answers him from his holy heaven with the saving might of his right hand.' The 'anointed' of Ps 20:6 is the Messiah whose salvation is vindicated by God's right-hand power"},
      {"type": "allusion", "target": "Heb 5:7", "note": "'During the days of Jesus's life on earth, he offered up prayers and petitions with fervent cries and tears to the one who could save him from death, and he was heard because of his reverent submission.' Ps 20:1 — 'May the LORD answer you in the day of trouble; may the name of the God of Jacob protect you' — is fulfilled in Gethsemane and the cross: Jesus cried to the one who could save him, and 'he was heard' in the resurrection. Ps 20's royal intercessory prayer finds its ultimate fulfillment in Christ's passion-and-resurrection"}
    ],
    "7": [
      {"type": "allusion", "target": "Phil 3:3", "note": "'For it is we who are the circumcision, we who serve God by his Spirit, who boast in Christ Jesus, and who put no confidence in the flesh.' Paul's contrast — trust in Christ vs. confidence in human resources — echoes Ps 20:7 ('Some trust in chariots and some in horses, but we trust in the name of the LORD our God'). Chariots and horses are the ancient equivalents of human military-political confidence; 'confidence in the flesh' is their Pauline equivalent; Christ replaces 'the name of the LORD' as the ground of trust"},
      {"type": "allusion", "target": "2 Cor 10:17", "note": "'Let the one who boasts boast in the Lord' (citing Jer 9:24). Paul's repeated insistence that all boasting must be in the Lord rather than human resources is the NT application of Ps 20:7's contrast. Ps 20:7's trust-in-the-Lord-not-in-human-military-power is Paul's epistemic principle: no human advantage justifies boasting before God"}
    ]
  },
  "21": {
    "4": [
      {"type": "allusion", "target": "Acts 2:28", "note": "'You have made known to me the paths of life; you will fill me with joy in your presence.' Peter's sermon cites Ps 16:11 ('paths of life') but the argument about life-forever runs from Ps 16 to Ps 21:4 — 'He asked you for life, and you gave it to him — length of days forever and ever.' The resurrection-life promised to David's anointed in Ps 21:4 is Peter's proof that David was speaking prophetically of the resurrection: the psalmist's prayer for 'life forever' was answered in Christ's resurrection"},
      {"type": "allusion", "target": "Rev 1:18", "note": "'I am the Living One; I was dead, and now look, I am alive for ever and ever!' The Risen Christ's self-description as alive 'for ever and ever' directly fulfills Ps 21:4 — 'length of days forever and ever.' What the psalmist prayed for the anointed king, Revelation declares accomplished: Christ lives with the 'forever and ever' life that no subsequent death can interrupt"}
    ],
    "5": [
      {"type": "allusion", "target": "Phil 2:9-11", "note": "God's bestowal of 'splendor and majesty' upon the anointed king in Ps 21:5 ('Through your salvation his glory is great; you have bestowed splendor and majesty upon him') is fulfilled in the exaltation of Christ: God gave him the name above every name. The post-victory royal exaltation of Ps 21 maps onto the post-resurrection exaltation of the crucified Christ — shame transformed into glory through divine vindication"},
      {"type": "allusion", "target": "Rev 5:12", "note": "'Worthy is the Lamb, who was slain, to receive power and wealth and wisdom and strength and honor and glory and praise!' The seven-fold ascription of honor to the Lamb in Rev 5:12 fulfills the pattern of Ps 21:5 — divine bestowal of glory, splendor, and majesty upon the anointed. What Ps 21 prays for the Davidic king, Rev 5 declares accomplished in the slain-and-risen Lamb"}
    ],
    "6": [
      {"type": "allusion", "target": "Rev 21:3-4", "note": "'God's dwelling place is now among the people, and he will dwell with them... He will wipe every tear from their eyes.' Ps 21:6 — 'you fill him with gladness in your presence' — anticipates the eschatological joy of divine presence described in Revelation 21. The king's gladness in YHWH's presence expands into the whole community's gladness in God's presence; the royal-presence joy of Ps 21 becomes the universal presence-joy of the new creation"}
    ],
    "8": [
      {"type": "allusion", "target": "Rev 19:11-16", "note": "'I saw heaven standing open and there before me was a white horse, whose rider is called Faithful and True. With justice he judges and wages war... On his robe and on his thigh he has this name written: KING OF KINGS AND LORD OF LORDS.' The divine warrior of Rev 19 fulfills Ps 21:8-9 — 'Your hand will reach all your enemies; your right hand will seize those who hate you. You will make them like a burning oven in the time of your anger.' The king's eschatological victory over all enemies in Ps 21 is enacted by the returning Christ"},
      {"type": "allusion", "target": "1 Cor 15:25", "note": "'For he must reign until he has put all his enemies under his feet.' Paul's statement about Christ's ongoing and future victory draws on Ps 110:1 primarily but also Ps 21:8-12 — the anointed king's comprehensive destruction of enemies until all opposition is ended. The 'must reign until' is the Ps 21 programme: the anointed king's right hand seizing every enemy until the opposition is completely defeated"}
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, ECHOES)
    save_echo('psalms', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Psalms echo (Ps 18-21): {len(existing)} psalms, {total} verses with connections.')

if __name__ == '__main__':
    main()
