"""
Echo Layer — Ezekiel chapters 18–20
Run: python3 scripts/zc-echo-ezekiel-18-20-fill.py

Major echo clusters:
- Ch 18: Individual moral responsibility — 18:4/20 → Rom 2:6; 6:23; Paul's
  appropriation of Lev 18:5 in Gal 3:12; 18:23/32 → 2 Pet 3:9; 1 Tim 2:4;
  John 3:16; 18:30-31 → Ezek 36:26-27; Acts 2:38; new heart/spirit typology
- Ch 19: Lament for princes — vine/lion imagery; 19:9 silenced royal voice →
  contrast with Rev 5:5 (Lion who has conquered); 19:10-14 vine burned → John 15
- Ch 20: Pattern of rebellion / new exodus — 20:11 → Gal 3:12; Rom 10:5 (Lev 18:5
  citation); 20:12 sabbath sign → Heb 4:9; Col 2:16-17; 20:33-37 shepherd's rod
  → John 10:16; Heb 13:20; 20:40-41 holy mountain pleasing aroma → Rev 14:1;
  Rom 12:1; 1 Pet 2:9-12
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echoes(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echoes(book, data):
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

EZK_ECHOES = {
  "18": {
    "2": [
      {"type": "allusion-source", "target": "Jer 31:29-30", "note": "The sour grapes proverb — 'the fathers ate sour grapes and the children's teeth are set on edge' — is also explicitly contested in Jeremiah 31:29-30, where YHWH announces that each person will die for their own iniquity. Both passages prepare for the new covenant era of individual accountability."}
    ],
    "4": [
      {"type": "allusion-source", "target": "Rom 6:23", "note": "Every soul belongs to YHWH; the soul who sins will die — the foundational principle Paul builds on: the wages of sin is death, but the gift of God is eternal life through Christ Jesus our Lord. Paul's gospel is the answer to the problem Ezekiel 18:4 poses."},
      {"type": "allusion", "target": "Rom 5:12", "note": "Ezekiel insists on individual accountability (the child does not die for the parent's sin); Paul's Adam/Christ typology operates at the representative/covenantal level rather than the individual-moral — both are grappling with the transmission of sin and its consequences across generations."}
    ],
    "20": [
      {"type": "allusion-source", "target": "Rom 2:6", "note": "The righteousness of the righteous belongs to him and the wickedness of the wicked falls on him — Paul cites Psalm 62:12 to make the same point: God will render to each one according to his works, and his own conduct determines his standing."},
      {"type": "allusion", "target": "Gal 6:5", "note": "Each person bears their own load — Paul's principle of individual accountability in Galatians echoes the Ezekielian framework: personal moral responsibility, not inherited or transferred, is the basis of judgment."}
    ],
    "23": [
      {"type": "allusion-source", "target": "2 Pet 3:9", "note": "Do I have any pleasure in the death of the wicked? — 2 Peter quotes the heart of this passage: the Lord is not slow concerning his promise, but patient toward you, not willing that any should perish but that all should come to repentance. YHWH's desire in Ezekiel 18:23 becomes the NT basis for mission patience."},
      {"type": "allusion", "target": "1 Tim 2:4", "note": "God desires all people to be saved and to come to the knowledge of the truth — the same divine will for universal life that Ezekiel 18:23 establishes for the OT is reaffirmed by Paul as the basis for intercession for all people."}
    ],
    "31": [
      {"type": "allusion-source", "target": "Ezek 36:26", "note": "Make yourselves a new heart and a new spirit — Ezekiel commands what only God can give. The resolution to the command of 18:31 is YHWH's promise in 36:26-27: I will give you a new heart and put a new spirit within you. The command reveals the need; the promise supplies the gift through Christ."},
      {"type": "allusion", "target": "Acts 2:38", "note": "Repent and turn from all your transgressions — Peter's Pentecost call to repentance echoes Ezekiel's repeated call: repent and turn; a new heart requires a turning that the Spirit accomplishes in the new covenant."}
    ],
    "32": [
      {"type": "allusion-source", "target": "John 3:16-17", "note": "I have no pleasure in the death of anyone; turn and live — this becomes John 3:16 and 3:17: God so loved the world that he gave his only Son, that whoever believes will not perish but have eternal life; God did not send his Son to condemn the world but to save it. The divine will-to-life of Ezekiel 18:32 is fulfilled in the Incarnation."}
    ]
  },
  "19": {
    "1": [
      {"type": "allusion", "target": "Rev 18:9-10", "note": "Raise a lament for the princes of Israel — the dirge form (qinah meter) for fallen rulers anticipates Revelation's lament over Babylon, where kings who committed adultery with her weep and mourn when they see her smoke rising."}
    ],
    "9": [
      {"type": "allusion", "target": "Rev 5:5", "note": "The lion cub whose roaring voice is silenced, caged and taken to Babylon — the silenced royal lion is the darkened form of what Revelation restores: the Lion of the tribe of Judah, the Root of David, has prevailed. The royal lion silenced in judgment and exile is finally the Lion who conquers death."}
    ],
    "14": [
      {"type": "allusion-source", "target": "John 15:6", "note": "The vine with no strong branch left, fire spreading from within to consume the fruit — Jesus's allegory of the true vine warns of exactly this: branches that do not remain in him are cut off, thrown out, wither, gathered, and burned. The fire of Ezekiel 19:14 is the judgment imagery Jesus uses for those who fail to bear fruit."}
    ]
  },
  "20": {
    "5": [
      {"type": "allusion-source", "target": "Acts 13:17", "note": "YHWH's election of Israel in Egypt — the beginning of the covenantal history Ezekiel rehearses — is recited by Paul in his synagogue sermon at Pisidian Antioch: the God of Israel chose our fathers and made the people great during their stay in Egypt. The same history of grace-and-rebellion becomes the context for announcing the Messiah."}
    ],
    "9": [
      {"type": "allusion-source", "target": "Rom 3:25-26", "note": "YHWH acting 'for the sake of my name' — restraining deserved judgment to protect his reputation among the nations — is the OT ground of what Paul calls the divine forbearance: God passed over former sins in the patience of God, to demonstrate his righteousness at the present time. The delay of judgment for the sake of the divine name is finally explained at the cross."}
    ],
    "11": [
      {"type": "allusion-source", "target": "Gal 3:12", "note": "The statutes by which the one who does them will live (citing Lev 18:5) — Paul quotes this formula in Galatians 3:12 to contrast law and faith: the law is not of faith, but the one who does them will live by them. Paul uses Ezekiel/Leviticus's conditional 'do and live' to show that Christ's 'trust and live' operates on different logic."},
      {"type": "allusion", "target": "Rom 10:5", "note": "Moses writes that the person who does the righteousness that is based on the law will live by it — Paul cites Lev 18:5 (which Ezekiel 20:11 also invokes) to contrast with the righteousness of faith. The divine life-by-doing formula is the basis against which Christ's fulfillment stands out."}
    ],
    "12": [
      {"type": "allusion-source", "target": "Col 2:16-17", "note": "The sabbaths given as a sign between YHWH and Israel are fulfilled-and-surpassed in Christ: Paul tells the Colossians that no one should judge them in matters of sabbath, for these are a shadow of things to come — but the body that casts the shadow belongs to Christ."},
      {"type": "allusion", "target": "Heb 4:9-11", "note": "The sabbath as covenant sign points toward the eschatological rest: there remains a sabbath rest for the people of God, for whoever enters God's rest also rests from his own works as God did from his. Ezekiel's sabbath-sign theology becomes the template for Hebrews' theology of rest in Christ."}
    ],
    "34": [
      {"type": "allusion-source", "target": "Matt 24:31", "note": "The gathering from all the nations where they have been scattered — with mighty hand and outstretched arm — becomes the great gathering of the elect that Jesus announces: he will send his angels with a loud trumpet call and gather his elect from the four winds. The new exodus gathering of Ezekiel 20 is the template for the eschatological ingathering."}
    ],
    "37": [
      {"type": "allusion-source", "target": "John 10:16", "note": "I will cause you to pass under the shepherd's rod and bring you into the bond of the covenant — the shepherd's rod that inspects and brings in the flock is fulfilled in the Good Shepherd: I have other sheep that are not of this fold; I must bring them also, and they will listen to my voice; then there will be one flock, one shepherd."},
      {"type": "allusion", "target": "Heb 13:20", "note": "The covenant sealed by the shepherd's authority is the covenant of peace in which Jesus is the great shepherd: may the God of peace, who brought back from the dead our Lord Jesus, the great Shepherd of the sheep, by the blood of the eternal covenant, equip you with everything good."}
    ],
    "40": [
      {"type": "allusion-source", "target": "Rev 14:1", "note": "On my holy mountain, the high mountain of Israel, all the house of Israel will serve me and there I will accept them — Revelation 14:1 places the 144,000 on Mount Zion with the Lamb, having his name and the Father's name on their foreheads. The holy mountain worship of Ezekiel 20 is fulfilled in the eschatological Zion assembly."}
    ],
    "41": [
      {"type": "allusion-source", "target": "Rom 12:1", "note": "I will accept you as a pleasing aroma when I gather you from the nations — Paul calls believers to present their bodies as a living sacrifice, holy and pleasing to God, which is their true worship. The 'pleasing aroma' of gathered Israel becomes the NT's metaphor for consecrated bodily worship."},
      {"type": "allusion", "target": "1 Pet 2:9", "note": "I will show my holiness through you before the nations — Peter applies this Israel-commission to the church: you are a chosen people, a royal priesthood, a holy nation, a people for his own possession, that you may declare the praises of him who called you out of darkness. The mission to the nations through a holy people is continuous from Ezekiel to the NT church."}
    ]
  }
}

def main():
    existing = load_echoes('ezekiel')
    merge_echo(existing, EZK_ECHOES)
    save_echoes('ezekiel', existing)

    out = json.loads((ROOT / 'data/echoes/ezekiel.json').read_text())
    for ch in [18, 19, 20]:
        ck = str(ch)
        count = sum(len(v) for v in out.get(ck, {}).values())
        status = 'done' if out.get(ck) else 'MISSING'
        print(f'ch {ch}: {status} ({len(out.get(ck, {}))} verse-keys, {count} entries total)')

if __name__ == '__main__':
    main()
