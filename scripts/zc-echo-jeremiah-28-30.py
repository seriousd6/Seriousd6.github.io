"""
Echo layer -- Jeremiah chapters 28-30
Run: python3 scripts/zc-echo-jeremiah-28-30.py

Key NT connections:
- 28:9:  true prophet test (word must come true) -- 1 John 4:1; Matt 7:15-16
- 28:15-17: false prophet dies the same year -- Acts 5:1-11 (Ananias pattern)
- 29:7:  seek the shalom of the city of exile -- 1 Pet 2:12-17 (live well among pagans)
- 29:11: plans for welfare and a future -- Rom 8:28; Eph 2:10
- 29:13: seek me with all your heart and find me -- Matt 7:7-8; John 6:37
- 29:14: I will let myself be found / gather from all nations -- John 11:52; Eph 1:10
- 30:8-9: David their king whom I will raise up -- Acts 2:30-36; 2 Tim 2:8
- 30:17: I will heal your wounds -- Isa 53:5; 1 Pet 2:24
- 30:21: their leader will approach me -- Heb 7:25; John 14:6
- 30:22: you will be my people and I will be your God -- Rev 21:3; 2 Cor 6:16
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f"  wrote {p.relative_to(ROOT)}")

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e["type"], e["target"]) for e in existing[ch][v]}
                for e in entries:
                    if (e["type"], e["target"]) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e["type"], e["target"]))

JEREMIAH_ECHOES = {
  "28": {
    "9": [
      {"type": "allusion", "target": "1 John 4:1", "note": "Only when the prophet's word comes true will it be known that the LORD has truly sent him -- the OT test for true prophecy (Deut 18:22; Jer 28:9) becomes the NT test for spirits and prophetic claims: test the spirits to see whether they are from God (1 John 4:1); the empirical test of fulfilled prediction is the same criterion that validates Jesus's prophetic authority (every major prediction came true, supremely the resurrection)"},
      {"type": "allusion", "target": "Matt 7:15", "note": "Beware of false prophets -- Jesus's warning in Matt 7:15-16 (watch out for false prophets; you will recognize them by their fruit) applies the prophetic test criterion Jeremiah demonstrates: the standard of fulfilled word and observable fruit distinguishes the sent prophet from the self-appointed one"}
    ],
    "15": [
      {"type": "allusion", "target": "Gal 1:8", "note": "The LORD has not sent you, and you have made this people trust in a lie -- Paul's anathema in Gal 1:8-9 (even if we or an angel from heaven should preach a gospel contrary to the one we preached, let him be accursed) stands in the prophetic tradition of Jeremiah's test: the prophet who speaks without divine commission is cursed, not commissioned; the NT equivalent is the false gospel condemned by its deviation from apostolic truth"}
    ],
    "17": [
      {"type": "allusion", "target": "Acts 5:5", "note": "The prophet Hananiah died that same year in the seventh month -- the sudden death of the false prophet who deceived the covenant community echoes the sudden deaths of Ananias and Sapphira (Acts 5:1-11: immediately he fell down and breathed his last); both events demonstrate that YHWH treats deliberate deception of the covenant community as a capital offense requiring immediate judgment as a warning to the community"}
    ]
  },
  "29": {
    "7": [
      {"type": "allusion", "target": "1 Pet 2:12", "note": "Seek the welfare (shalom) of the city where I have sent you into exile, and pray to the LORD on its behalf -- this is the posture Peter calls the church to: live such good lives among the pagans that though they accuse you of doing wrong they may see your good deeds and glorify God (1 Pet 2:12); also Rom 13:1-7 (be subject to governing authorities); the exilic engagement with the surrounding society is the NT church's posture as strangers and exiles (1 Pet 2:11) who work for the city's flourishing"},
    ],
    "11": [
      {"type": "allusion", "target": "Rom 8:28", "note": "I know the plans I have for you, declares the LORD, plans for welfare and not for harm, to give you a future and a hope -- Paul's confidence in Rom 8:28 (all things work together for good for those who love God, who are called according to his purpose) is the NT form of the Jeremianic assurance: YHWH's purposive planning for his people's welfare is the ground of covenant confidence in both testaments"},
      {"type": "allusion", "target": "Eph 2:10", "note": "Plans for welfare... to give you a future and a hope -- Eph 2:10 specifies the NT form of YHWH's plans: created in Christ Jesus for good works which God prepared in advance for us to do; the purposive planning of Jer 29:11 is Christologically specific in Ephesians -- the future and hope are in Christ, and the plans are the works God prepared before creation"}
    ],
    "13": [
      {"type": "allusion", "target": "Matt 7:7", "note": "You will seek me and find me when you search for me with all your heart -- Jesus's promise in Matt 7:7-8 (ask and it will be given to you; seek and you will find; the one who seeks finds) directly corresponds to Jeremiah's promise; the wholeheartedness Jeremiah requires is the context in which Jesus makes seeking-and-finding an unfailing promise"},
      {"type": "allusion", "target": "John 6:37", "note": "You will seek me and find me -- whoever comes to me I will never cast out (John 6:37); Jesus's guarantee of reception for seekers is the NT personalization of Jeremiah's promise: YHWH who allowed himself to be found by the exiles is Christ who receives all who come to him without exception"}
    ],
    "14": [
      {"type": "allusion", "target": "John 11:52", "note": "I will gather you from all the nations and all the places where I have driven you -- the re-gathering from worldwide exile is fulfilled by Christ who dies not only for the Jewish nation but also to gather into one the children of God who are scattered abroad (John 11:52); the Jeremianic re-gathering promise is the foundation for the universal gathering mission of Christ's death"},
      {"type": "allusion", "target": "Eph 1:10", "note": "I will restore your fortunes and gather you -- God's plan to sum up all things in Christ, things in heaven and on earth (Eph 1:10), is the eschatological fulfillment of the Jeremianic gathering promise; the gathering of exiles to Jerusalem becomes the gathering of all things to Christ as the cosmic center"}
    ]
  },
  "30": {
    "7": [
      {"type": "allusion", "target": "Matt 24:21", "note": "How terrible that day will be! There has never been another like it. A time of anguish for Jacob -- but he will be saved out of it -- the unparalleled tribulation that precedes salvation in Jer 30:7 is the OT template for Jesus's eschatological discourse: for then there will be great tribulation, such as has not been from the beginning of the world... and if those days had not been cut short, no human being would be saved, but for the sake of the elect those days will be cut short (Matt 24:21-22); salvation through-not-from the tribulation"}
    ],
    "8": [
      {"type": "allusion", "target": "Matt 11:29", "note": "On that day I will break the yoke from your neck and snap your bonds -- the breaking of the covenant yoke of judgment is the act Christ performs when he says take my yoke upon you, for my yoke is easy and my burden is light (Matt 11:28-30); the heavy yoke of Babylonian bondage is broken by YHWH; the heavy yoke of sin and death is broken by Christ who replaces it with his easy yoke"}
    ],
    "9": [
      {"type": "fulfillment", "target": "Acts 2:30", "note": "They will serve the LORD their God and David their king, whom I will raise up for them -- the raised Davidic king is the resurrected Christ: Peter declares at Pentecost that God had sworn an oath to David that he would place one of his descendants on his throne; foreseeing this, David spoke of the resurrection of the Messiah (Acts 2:30-31); the raising up of the Davidic king that Jeremiah promises is accomplished in the resurrection"},
      {"type": "fulfillment", "target": "2 Tim 2:8", "note": "David their king, whom I will raise up for them -- Paul's gospel-summary in 2 Tim 2:8: remember Jesus Christ, raised from the dead, descended from David, as preached in my gospel; the resurrection of the Davidic king is the center of the Pauline gospel, completing Jeremiah's promise of the raised Davidic ruler"}
    ],
    "10": [
      {"type": "allusion", "target": "Rom 8:35", "note": "Do not be afraid, my servant Jacob; do not be dismayed, O Israel -- I am with you to save you -- Paul's rhetorical climax in Rom 8:35-39 (who shall separate us from the love of Christ?) echoes the covenant assurance of Jeremiah: nothing in creation can separate the covenant people from their God's saving purpose; the YHWH who promises to be with Jacob is the Father of whom Paul says neither death nor life nor angels nor principalities can separate us from his love in Christ"}
    ],
    "17": [
      {"type": "fulfillment", "target": "1 Pet 2:24", "note": "I will restore your health and heal your wounds -- the divine healing of the incurable wound (Jer 30:12-17) is fulfilled in Christ's atoning work: he bore our sins in his body on the tree, so that we might die to sins and live for righteousness; by his wounds you have been healed (1 Pet 2:24, quoting Isa 53:5); the incurable wound that YHWH promises to heal becomes the healed wound in Christ's substitutionary suffering"}
    ],
    "21": [
      {"type": "allusion", "target": "Heb 7:25", "note": "Their leader will come from among them, and their governor will emerge from their own midst; I will bring him near and he will approach me -- the covenant leader who is drawn near to YHWH for his people is the type of Christ as high priest who draws near to the Father permanently: he always lives to make intercession for those who draw near to God through him (Heb 7:25); also John 14:6 (no one comes to the Father except through me) -- Christ is the one who approaches the Father as the people's representative"}
    ],
    "22": [
      {"type": "fulfillment", "target": "Rev 21:3", "note": "You will be my people and I will be your God -- the covenant formula that appears throughout the OT (Exod 6:7; Lev 26:12; Jer 7:23; 11:4; 30:22; Ezek 36:28; 37:27) reaches its final fulfillment in Rev 21:3: I heard a loud voice from the throne saying, Behold the dwelling place of God is with man; he will dwell with them and they will be his people and God himself will be with them; this culmination is the final answer to the exilic promise of Jer 30:22"},
      {"type": "allusion", "target": "2 Cor 6:16", "note": "I will be your God and you will be my people -- Paul cites this covenant formula in 2 Cor 6:16 as the ground for the church's separation from idolatry: I will make my dwelling among them and walk among them, and I will be their God and they shall be my people; the covenant identity of the OT is applied directly to the NT church as the community of the new covenant in Christ"}
    ]
  }
}

def main():
    existing = load_echo("jeremiah")
    merge_echo(existing, JEREMIAH_ECHOES)
    save_echo("jeremiah", existing)
    print("Jeremiah 28-30 echoes written.")

if __name__ == "__main__":
    main()
