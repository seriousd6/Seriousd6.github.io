"""
echo layer: Joshua 21–23.
Ch 21 (45 v): Levitical cities — already has v45 entry; adding nothing new.
Ch 22 (34 v): Eastern tribes return, altar controversy resolved as witness altar.
Ch 23 (16 v): Joshua's farewell — divine faithfulness, covenant warning.
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

ECHOES = {
  "22": {
    "5": [
      {"type": "allusion", "target": "Matt 22:37-38", "note": "Phinehas's charge to the eastern tribes: love YHWH your God, walk in all his ways, keep his commandments, cling to him, serve him with all your heart and soul — the full-devotion formula that Jesus distills as the greatest commandment (Matt 22:37-38; cf. Deut 6:5); Joshua's charge is a rehearsal of the Shema applied to covenantal life in the land"},
      {"type": "allusion", "target": "John 14:15", "note": "Obedience as the expression of love: keep his commandments and cling to him — Jesus recasts the same logic: if you love me, keep my commandments (John 14:15); the inseparability of love and obedience in Joshua's charge is the same structure Christ makes explicit in the upper room discourse"}
    ],
    "19": [
      {"type": "allusion", "target": "Heb 10:19-22", "note": "If your land is unclean, cross over to the LORD's land where his tabernacle stands and take a possession among us — the principle that access to YHWH requires being in the land of YHWH's dwelling; Hebrews 10:19-22 transforms this: we now have confidence to enter the Most Holy Place by the blood of Jesus, a new and living way through the veil, so that geographic distance from the sanctuary is abolished in Christ"}
    ],
    "22": [
      {"type": "allusion", "target": "Rev 4:8", "note": "El Elohim YHWH, El Elohim YHWH — the triple-name invocation with which the eastern tribes swear their innocence echoes the triple-holy acclamation of the seraphim and heavenly creatures; the solemn divine-witness oath form is the background for the unceasing Holy, holy, holy of Rev 4:8"},
      {"type": "allusion", "target": "Heb 10:31", "note": "He knows, and let Israel know — calling God as witness to covenant integrity; the same divine omniscience is the ground of the warning in Heb 10:31: it is a fearful thing to fall into the hands of the living God, the covenant judge who knows"}
    ],
    "27": [
      {"type": "allusion", "target": "Rev 11:3", "note": "The altar is a witness between us and you, and between our generations after us, that we do perform the service of YHWH — the altar as ongoing testimony to covenant relationship; the two witnesses of Rev 11:3-4 are described as lampstands and olive trees (Zech 4 imagery) who bear witness to God's truth before the nations; the witness-altar prefigures the church's role as testimony to the covenant"},
      {"type": "allusion", "target": "Rom 1:9", "note": "God is witness between us — the formulaic invocation of God as covenant witness (cf. Gen 31:50; 1 Sam 12:5) is the background for Paul's repeated witness-oath: God is my witness (Rom 1:9; Phil 1:8; 1 Thess 2:5), invoking the same divine omniscience to validate his apostolic integrity"}
    ],
    "34": [
      {"type": "allusion", "target": "John 10:16", "note": "The altar is called Witness, for it is a witness between us that YHWH is God — the naming of the altar as a unifying witness between separated communities; Jesus's promise of one flock, one shepherd (John 10:16) is the fulfillment: the unity of Jewish and Gentile believers in one body, witnessed not by a stone altar but by the Spirit"}
    ]
  },
  "23": {
    "1": [
      {"type": "allusion", "target": "Heb 4:8", "note": "A long time afterward, when YHWH had given rest to Israel from all their surrounding enemies — the land-rest granted through Joshua is what Hebrews cites as inadequate: if Joshua had given them rest, God would not have spoken of another day later on (Heb 4:8); the rest of Canaan points beyond itself to the eschatological Sabbath-rest that remains for the people of God"}
    ],
    "3": [
      {"type": "allusion", "target": "Rom 8:31", "note": "You yourselves have seen all that YHWH your God has done to all these nations for your sake, for it is YHWH your God who has fought for you — the pattern of divine warfare on behalf of his people; Paul's rhetorical question if God is for us, who can be against us? (Rom 8:31) is grounded in this history of YHWH fighting for Israel, now applied to the church through Christ's victory"}
    ],
    "6": [
      {"type": "allusion", "target": "Matt 5:17-18", "note": "Be very strong to keep and to do all that is written in the Book of the Law of Moses — total observance of written Torah as the covenantal obligation; Jesus declares he did not come to abolish the Law or the Prophets but to fulfill them, and that not one jot or tittle will pass until all is accomplished (Matt 5:17-18); the demand for complete Torah-fidelity that Joshua urges is answered not in human obedience but in Christ's perfect fulfillment"}
    ],
    "8": [
      {"type": "allusion", "target": "Rom 8:38-39", "note": "But you shall cling to YHWH your God just as you have done to this day — the verb dabaq (cling/cleave) is the same used in Gen 2:24 (man clings to wife) and Ruth 1:14 (Ruth clung to Naomi); it denotes irreversible attachment. Paul's conviction that nothing can separate us from the love of God (Rom 8:38-39) is the christological fulfillment: the clinging is now guaranteed by the love of Christ who holds his own inseparably"}
    ],
    "10": [
      {"type": "allusion", "target": "Phil 4:13", "note": "One man of you puts to flight a thousand, since it is YHWH your God who fights for you, just as he promised — the arithmetic of divine empowerment that makes one equal to a thousand; Paul's I can do all things through him who strengthens me (Phil 4:13) is the NT form of the same principle: strength for disproportionate effectiveness comes from divine presence, not human capacity"}
    ],
    "11": [
      {"type": "allusion", "target": "1 John 4:19", "note": "Be very careful to love YHWH your God — the urgent summons to love as the foundation of covenant faithfulness; we love because he first loved us (1 John 4:19) answers the question of how this love becomes possible: the enabling love of Christ grounds and produces the love that Joshua commands"}
    ],
    "12": [
      {"type": "allusion", "target": "2 Cor 6:14", "note": "If you turn back and cling to the remnant of these nations remaining among you and make marriages with them — the warning against covenant-mixing through intermarriage; Paul applies the same separation principle to the church: do not be unequally yoked with unbelievers (2 Cor 6:14), drawing on the Deuteronomic prohibition that underlies Joshua's warning"}
    ],
    "13": [
      {"type": "allusion", "target": "1 Cor 15:33", "note": "They shall be a snare and a trap for you, a whip on your sides and thorns in your eyes until you perish from this good land — the nations as instruments of corruption and eventual destruction; Paul's warning bad company corrupts good character (1 Cor 15:33) echoes the same principle: proximity to false teaching and idolatrous practice corrupts covenantal integrity"}
    ],
    "14": [
      {"type": "fulfillment", "target": "2 Cor 1:20", "note": "Not one word has failed of all the good things that YHWH your God promised concerning you; all have come to pass — the total fulfillment of divine promises through the conquest is Joshua's testimony. Paul's all the promises of God find their Yes in him [Christ] (2 Cor 1:20) extends this: if YHWH's land-promises were fulfilled without exception through Joshua, so the new-covenant promises are fulfilled without exception in the one who is greater than Joshua (Heb 4:8)"},
      {"type": "allusion", "target": "Heb 13:8", "note": "All the good things YHWH promised have come to pass — divine promise-faithfulness across time; Jesus Christ is the same yesterday and today and forever (Heb 13:8) is the christological form of this testimony: the God whose promises Joshua declares all fulfilled is the same God who fulfills all promises in his Son"}
    ],
    "15": [
      {"type": "allusion", "target": "Heb 10:28-29", "note": "Just as all the good things that YHWH your God promised have come to pass, so YHWH will bring upon you all the evil things until he destroys you from off this good land — the double-edged character of covenant faithfulness: the same reliability that guarantees blessings guarantees curses for violation. Hebrews 10:28-29 applies this to the new covenant: how much severer punishment will be deserved by the one who tramples the Son of God underfoot; if Israel's covenant curses were real and certain, how much more the new-covenant consequences for those who reject Christ"}
    ],
    "16": [
      {"type": "allusion", "target": "Rev 20:9", "note": "If you transgress the covenant of YHWH your God and go and serve other gods, the anger of YHWH will be kindled against you, and you shall perish quickly from the good land — the final covenant curse: losing the land through divine anger at idolatry. Revelation's great battle ends with fire from heaven consuming the enemies of God's people (Rev 20:9); the temporal land-loss that Joshua warns against finds its eschatological form in the final judgment on all who serve other gods and break covenant with the living God"}
    ]
  }
}

def main():
    e = load_echo('joshua')
    merge_echo(e, ECHOES)
    save_echo('joshua', e)
    print('joshua ch 22-23: echo written')

if __name__ == '__main__':
    main()
