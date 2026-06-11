"""
Echo addendum — Leviticus chapters 20–21
Run: python3 scripts/zc-echo-leviticus-20-21-addendum.py
Adds echo entries for ch20 and ch21 which were missing from the seed script.
ch20: forbidden practices + penalties (Molech, sexual ethics, mediums)
ch21: priestly holiness code (types of Christ as perfect High Priest)
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

ECHO = {
  "20": {
    "7": [
      {"type": "fulfillment", "target": "1 Pet 1:15", "note": "You shall consecrate yourselves therefore and be holy, for I am YHWH your God — the holiness command of Lev 20:7 is part of the Holiness Code pattern that Peter quotes directly in 1 Pet 1:15-16; the NT application is not ceremonial purity but moral conformity to the holy character of God revealed in Christ"}
    ],
    "9": [
      {"type": "allusion", "target": "Matt 15:4", "note": "Anyone who curses his father or his mother shall surely be put to death — Jesus cites this capital penalty in Matt 15:4 (and Mark 7:10) to expose the Pharisees' Corban tradition: by declaring their property dedicated to God they nullified the duty to support aging parents, directly contradicting the Torah command that dishonouring parents was a capital offense; Jesus uses the severity of Lev 20:9 to show the seriousness of the fifth commandment"},
      {"type": "allusion", "target": "Mark 7:10", "note": "Whoever reviles father or mother must surely die — Mark's parallel account of Jesus's Corban controversy; Jesus cites the severity of Lev 20:9 to demonstrate that the Pharisees' tradition nullifies God's word rather than fulfilling it"}
    ],
    "10": [
      {"type": "allusion", "target": "John 8:5", "note": "If a man commits adultery with the wife of his neighbor, both the adulterer and the adulteress shall surely be put to death — the scribes and Pharisees cite the Mosaic adultery penalty (Lev 20:10, Deut 22:22) in their confrontation with Jesus over the woman caught in adultery (John 8:5: Now in the Law Moses commanded us to stone such women; so what do you say?); Jesus's response reframes the entire law's application"}
    ],
    "26": [
      {"type": "fulfillment", "target": "1 Pet 1:16", "note": "You shall be holy to me, for I am holy and have separated you from the peoples to be mine — 1 Peter 1:16 quotes this verse directly (be holy, for I am holy) as the ethical charter of the new covenant community; the call to holiness is grounded in God's own character, not human effort; the NT application extends it from Israel's ethnic-cultic separation to the church's moral-spiritual transformation in Christ"},
      {"type": "allusion", "target": "2 Cor 6:17", "note": "I have separated you from the peoples to be mine — Paul draws on the separation-from-peoples theme of the Holiness Code (Lev 20:24-26) in 2 Cor 6:17 (come out from them and be separate, says the Lord); the NT reapplies Israel's ethno-cultic separation as a moral-spiritual call to the church to be distinct from the world's values"}
    ],
    "27": [
      {"type": "allusion", "target": "Acts 16:16", "note": "A man or a woman who is a medium or a necromancer shall surely be put to death — the death penalty for spiritist consultation (Lev 20:27) underlines the severity of occult practices in the Torah; Acts 16:16-18 shows Paul exorcising a spirit of divination from a slave girl, demonstrating Christ's authority over the powers the Torah forbade and punished; the NT does not repeat the death penalty but maintains the prohibition"}
    ]
  },
  "21": {
    "8": [
      {"type": "allusion", "target": "Heb 7:26", "note": "You shall sanctify him, for he offers the bread of your God... He shall be holy to you, for I YHWH who sanctify you am holy — the priest must be set apart by YHWH's own sanctifying act; Hebrews 7:26 declares Christ to be the fulfillment of all priestly holiness requirements: holy, innocent, unstained, separated from sinners and exalted above the heavens — every attribute the Aaronic priest was required to pursue, Christ possesses intrinsically"}
    ],
    "10": [
      {"type": "allusion", "target": "Heb 4:14", "note": "The priest who is chief among his brothers, on whose head the anointing oil is poured and who has been consecrated to wear the garments, shall not let the hair of his head hang loose nor tear his clothes — the high priest's unique consecration and dignified office is the type of Christ the great high priest; Heb 4:14 opens the high-priestly Christology section: since we have a great high priest who has passed through the heavens, Jesus, the Son of God, let us hold fast our confession"}
    ],
    "17": [
      {"type": "allusion", "target": "Heb 9:14", "note": "None of your offspring throughout their generations who has a blemish may approach to offer the bread of his God — the requirement that priests and their offerings be without physical blemish (Lev 21:17-23) is the type of Christ's perfect, unblemished self-offering; Heb 9:14 draws the explicit connection: how much more will the blood of Christ, who through the eternal Spirit offered himself without blemish to God, purify our conscience from dead works"},
      {"type": "allusion", "target": "1 Pet 1:19", "note": "No man who has a blemish shall draw near to offer — the Levitical requirement of physical perfection in the priest and the sacrifice finds its antitype in Christ as the lamb without blemish or spot (1 Pet 1:19); the imperfect Aaronic priest could not offer a blemished animal; the perfect Christ offered himself, the unblemished one, once for all"}
    ],
    "23": [
      {"type": "allusion", "target": "Heb 7:28", "note": "He shall not go through the veil or approach the altar because he has a blemish, that he may not profane my sanctuaries — imperfect priests are barred from the most sacred ministry; Heb 7:28 contrasts the weakness of imperfect Aaronic priests with Christ: the law appoints men in their weakness as high priests, but the word of the oath, which came later than the law, appoints a Son who has been made perfect forever; Lev 21's exclusions highlight precisely what Christ supersedes"}
    ]
  }
}

e = load_echo('leviticus')
merge_echo(e, ECHO)
save_echo('leviticus', e)
print('Leviticus 20-21 echo entries written.')
