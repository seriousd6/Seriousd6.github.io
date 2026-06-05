"""
Numbers — all four layers.
Key NT uses: bronze serpent (21), water from rock (20), wilderness wandering as warning,
Balaam's star oracle (24), Phinehas's zeal, priestly blessing (6:24-26).
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

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
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

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

ECHO = {
  "6": {
    "24": [
      {"type": "allusion", "target": "2 Cor 13:14", "note": "The LORD bless you and keep you; the LORD make his face shine on you and be gracious to you; the LORD lift up his countenance upon you and give you peace — the Aaronic blessing (Num 6:24-26) is the OT's most direct benediction of divine favor; Paul's trinitarian benediction in 2 Cor 13:14 echoes its structure and is its new covenant fulfillment"}
    ]
  },
  "14": {
    "29": [
      {"type": "allusion", "target": "Heb 3:17", "note": "Your dead bodies shall fall in this wilderness — the wilderness generation's judgment (their corpses fell in the desert) is Hebrews' central warning about unbelief: with whom was God provoked for forty years? Was it not with those who sinned, whose bodies fell in the wilderness? (Heb 3:17)"},
      {"type": "allusion", "target": "1 Cor 10:5", "note": "God was not pleased with most of them, for they were overthrown in the wilderness — Paul cites the wilderness generation's fate as a warning to the Corinthians; the judgment on the unbelieving exodus generation is the type of what awaits persistent unbelief"}
    ]
  },
  "21": {
    "8": [
      {"type": "fulfillment", "target": "John 3:14-15", "note": "Make a fiery serpent and set it on a pole and everyone who is bitten, when he sees it, shall live — Jesus explicitly cites the bronze serpent as a type of his own crucifixion: as Moses lifted up the serpent in the wilderness, so must the Son of Man be lifted up, that whoever believes in him may have eternal life (John 3:14-15); looking to the lifted serpent = believing in the lifted Christ"}
    ]
  },
  "24": {
    "17": [
      {"type": "fulfillment", "target": "Rev 22:16", "note": "A star shall come out of Jacob — Balaam's messianic oracle (the star from Jacob) is applied to Christ in Revelation: I am the root and the descendant of David, the bright morning star; Num 24:17 was a significant messianic proof-text in Second Temple Judaism (the Dead Sea Scrolls use it messianically)"}
    ]
  },
  "25": {
    "11": [
      {"type": "allusion", "target": "Rom 10:2", "note": "Phinehas son of Eleazar has turned back my wrath by being jealous with my jealousy — Phinehas's zeal for YHWH's honor (executing the Israelite and Midianite woman in their sin) is cited as the model of passionate covenant faithfulness; Paul's description of Israel's zeal for God echoes the Phinehas tradition"}
    ]
  }
}

ORIGINAL = {
  "6": {
    "24": "<p><strong>yevarechecha YHWH veyishmerecha yaer YHWH panav eleicha vichuneka yissa YHWH panav eleicha veyasem lecha shalom</strong>: The Aaronic Blessing (Birkat Kohanim) is the oldest liturgical text in continuous use — fragments of it were found on silver amulets from the 7th century BCE (the Ketef Hinnom scrolls, the oldest biblical text discovered). Its three-part structure increases in length: 3 words, 5 words, 7 words, with a crescendo toward <em>shalom</em> (peace/wholeness/well-being). The divine name YHWH appears three times — early Christian interpreters saw this as a Trinitarian hint. The blessing has been recited in Jewish synagogues for over 2,500 years and by Christian ministers at service benedictions, making it one of the most-spoken texts in human history.</p>"
  },
  "21": {
    "8": "<p><strong>veasa lecha saraf veshim oto al nes vehaya kol hanashuch veraah oto vachai</strong>: 'Make a fiery serpent and set it on a pole, and everyone who is bitten, when he sees it, shall live.' The serpent-on-a-pole raises a question: is this a violation of the second commandment (no graven images)? The text suggests: (1) it is the looking in faith, not the object itself, that saves; (2) YHWH appointed the image for a specific purpose as a means of grace. The Greek translation (<em>ophis chalkous</em>, bronze serpent) uses the same word Paul uses in 2 Cor 5:21: God made him who knew no sin to be <em>sin</em> (Gk. <em>hamartia</em>) for us — Christ becomes the thing that kills (sin/the serpent) in order to be the means of salvation for all who look to him.</p>"
  }
}

CONTEXT = {
  "1": {
    "1": "<p>Numbers takes its English name from the two censuses (chs. 1 and 26); the Hebrew title is <em>Bemidbar</em> (In the Wilderness), which better captures the book's geographical and theological content. It narrates the wilderness journey from Sinai to the plains of Moab — a journey that should have taken months but became 40 years because of the generation's unbelief at Kadesh-barnea (chs. 13-14). The book is structured around the failure of the first generation (which dies in the wilderness) and the formation of the second generation (which enters Canaan). The typological theme of wilderness-as-testing-ground is developed extensively in the NT: Israel's forty years in the wilderness corresponds to Jesus's forty days of testing (Matt 4:1-11), and Paul makes the wilderness generation's failures into warnings for the church (1 Cor 10:1-13).</p>"
  },
  "21": {
    "4": "<p>The bronze serpent incident (Num 21:4-9) occurs during one of the wilderness generation's recurring cycles of complaint-judgment-intercession-deliverance. The people speak against God and against Moses; YHWH sends fiery serpents as judgment; the people confess sin and Moses intercedes; YHWH provides the bronze serpent as a means of healing. The serpent-image was preserved in Israel and later became an object of idolatry: Hezekiah destroyed it during his reforms (2 Kings 18:4: he broke in pieces the bronze serpent that Moses had made, for until those days the people of Israel had burned incense to it). The thing appointed as a healing sign became an idol — illustrating the tendency of every divine gift to be worshiped rather than used. Jesus redeems the image by applying it to himself in John 3:14.</p>"
  }
}

CHRIST = {
  "6": {
    "24": "<p>A direct revelation: 'The LORD bless you and keep you; the LORD make his face shine on you and be gracious to you; the LORD lift up his countenance upon you and give you peace.' The Aaronic blessing is Israel's definitive statement of what divine favor looks like: not an absence of difficulty but the direct presence and face of YHWH turned toward his people in grace. In Christ, the Aaronic blessing receives its ultimate fulfillment: the Father's face shines in the face of Christ (2 Cor 4:6: the light of the knowledge of the glory of God in the face of Jesus Christ); the divine peace (<em>shalom</em>) that the blessing promised is the peace Christ gives (John 14:27: Peace I leave with you; my peace I give to you); the benedictions of Christian worship (2 Cor 13:14; Jude 24-25; Rev 1:4-5) are the new covenant form of the ancient priestly blessing.</p>"
  },
  "21": {
    "8": "<p>A type: 'Set it on a pole, and everyone who is bitten, when he sees it, shall live.' Jesus explicitly applies the bronze serpent typology to himself (John 3:14-15), making it the Bible's own explanation of why Christ must be 'lifted up' on the cross. The structural parallel: Israel was under God's judgment for sin (serpent bites = death sentence) → Moses interceded → YHWH appointed an external means of salvation (look to the serpent) → those who looked in faith lived. The antitype: humanity is under God's judgment for sin → Christ intercedes → the Father appoints the cross as the external means of salvation → those who look in faith to the crucified Christ live forever. The bronze serpent is Numbers' most explicit Christological type, made explicit not by later Christian interpretation but by Jesus himself.</p>"
  }
}

def main():
    e = load_echo('numbers')
    merge_echo(e, ECHO)
    save_echo('numbers', e)

    c = load_comm('mkt-original', 'numbers')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', 'numbers', c)

    c = load_comm('mkt-context', 'numbers')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', 'numbers', c)

    c = load_comm('mkt-christ', 'numbers')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', 'numbers', c)

    print('numbers: all 4 layers written')

if __name__ == '__main__':
    main()
