"""Zechariah echo layer — NT allusions/fulfillments for chs 1–7.
Existing echo file already covers ch4 (Rev 11:4), ch9, ch11, ch12, ch13.
This script adds one or more entries per chapter for chs 1, 2, 3, 5, 6, 7.
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

ZECH_ECHO = {
  "1": {
    "8": [
      {"type": "allusion", "target": "Rev 6:4", "note": "I saw in the night, and behold, a man riding on a red horse — Zechariah's first vision of a rider on a red horse among the myrtle trees, with the heavenly patrol reporting on the earth; the four horsemen of Revelation (Rev 6:1-8) develop this imagery: the heavenly cavalry now carries the divine judgments into the world; in Zechariah the riders report peace; in Revelation they bring tribulation — the eschatological intensification of the same heavenly-patrol motif"},
      {"type": "allusion", "target": "Rev 19:11", "note": "I saw in the night, and behold, a man riding on a red horse — Zechariah's horseman in the myrtle-tree valley is the prototype of the rider on the white horse in Rev 19:11; both are YHWH's agent surveying and executing his purposes in the earth; the night-vision context in Zechariah (1:7: on the twenty-fourth day of the eleventh month) gives the heavenly patrol a dateable historical setting that Revelation universalizes into the eschatological final campaign"}
    ]
  },
  "2": {
    "10": [
      {"type": "allusion", "target": "John 1:14", "note": "Sing and rejoice, O daughter of Zion, for behold, I come and I will dwell in your midst, declares the LORD — the divine promise of indwelling presence; John 1:14 (the Word became flesh and dwelt/tabernacled among us) is the ultimate fulfillment of YHWH's promise to dwell in the midst of his people; Zechariah's vision is of YHWH returning to Jerusalem after exile; John's vision is of the Word tabernacling in humanity in the incarnation"},
      {"type": "allusion", "target": "Rev 21:3", "note": "Many nations shall join themselves to the LORD in that day, and shall be my people. And I will dwell in your midst — the universal gathering of nations to YHWH's dwelling is Zechariah's eschatological horizon; Revelation fulfills it: I heard a loud voice from the throne saying, Behold, the dwelling place of God is with man; he will dwell with them and they will be his people (Rev 21:3); the promise initiated in Zechariah reaches its final form in the new Jerusalem"}
    ]
  },
  "3": {
    "1": [
      {"type": "allusion", "target": "Rom 8:33", "note": "He showed me Joshua the high priest standing before the angel of the LORD, and Satan standing at his right hand to accuse him — the courtroom scene of Zechariah 3 (Satan accusing, divine advocate rebuking) is the OT pattern for the NT's assurance of justification; Paul applies it: Who shall bring any charge against God's elect? It is God who justifies; who is to condemn? (Rom 8:33-34); the scene in Zechariah ends with filthy garments replaced by pure ones — imputed righteousness that stops the accuser's case"},
      {"type": "allusion", "target": "Jude 9", "note": "The LORD said to Satan, The LORD rebuke you, O Satan! — the divine rebuke of the accuser in Zechariah 3:2 is echoed in Jude 9 (the archangel Michael said to the devil, The Lord rebuke you); the formula is the same; the principle is the same: the accuser is silenced not by the accused's merit but by the Lord's authoritative word"}
    ],
    "8": [
      {"type": "allusion", "target": "Heb 7:26", "note": "Hear now, O Joshua the high priest, you and your friends who sit before you, for they are men who are a sign: behold, I will bring my servant the Branch — Joshua the high priest as a sign pointing forward to the Branch; Hebrews identifies Jesus as the high priest who is holy, innocent, unstained, separated from sinners, exalted above the heavens (Heb 7:26); the Branch of Zechariah combines the Davidic kingship (branch from the stump of Jesse) and the priestly intercession into the single figure of Christ"}
    ]
  },
  "5": {
    "3": [
      {"type": "allusion", "target": "Gal 3:10", "note": "This is the curse that goes out over the face of the whole land — the flying scroll of Zechariah 5 (a massive scroll bearing curses against every thief and every one who swears falsely) represents the covenant curses that hang over the land; Paul applies the curse-principle directly: all who rely on works of the law are under a curse (Gal 3:10, citing Deut 27:26); Christ redeems from this curse by becoming a curse for us (Gal 3:13, citing Deut 21:23)"}
    ]
  },
  "6": {
    "12": [
      {"type": "allusion", "target": "Heb 7:1", "note": "Behold, the man whose name is the Branch: for he shall branch out from his place, and he shall build the temple of the LORD. It is he who shall build the temple of the LORD and shall bear royal honor, and shall sit and rule on his throne. And there shall be a priest on his throne — the Branch of Zechariah 6:12-13 combines the Davidic royal office (throne) with the priestly office; this priest-king combination is the Melchizedek pattern; Hebrews identifies Jesus as the Melchizedek priest-king (Heb 7:1): this Jesus, who has a permanent priesthood, holds his royal-priestly throne forever"},
      {"type": "allusion", "target": "John 2:19", "note": "He shall build the temple of the LORD — the Branch-figure in Zechariah 6:13 is the temple builder par excellence; Jesus reinterprets this: destroy this temple, and in three days I will raise it up — speaking of the temple of his body (John 2:19-21); Christ is the temple builder precisely by being the temple himself; the new temple is not a building but his resurrected body around which the church is built (Eph 2:21-22)"}
    ]
  },
  "7": {
    "9": [
      {"type": "allusion", "target": "Matt 23:23", "note": "Thus says the LORD of hosts: Render true judgments, show kindness and mercy to one another, do not oppress the widow, the fatherless, the sojourner, or the poor — Zechariah's summary of covenant ethics (7:9-10); Jesus uses the same categories as the weightier matters of the law: justice and mercy and faithfulness (Matt 23:23); Zechariah and Jesus agree that the law's substance is ethical, not merely ceremonial, and that neglect of justice and mercy is covenant unfaithfulness even under a veneer of religious observance"},
      {"type": "allusion", "target": "James 1:27", "note": "Do not oppress the widow, the fatherless, the sojourner, or the poor — the prophetic ethical standard of Zechariah 7:10; James gives the NT's most compact equivalent: religion that is pure and undefiled before God the Father is this: to visit orphans and widows in their affliction (James 1:27); the specific categories — widow, orphan, sojourner — are the OT's canonical list of the vulnerable, and the NT carries them forward unchanged"}
    ]
  }
}

def main():
    existing = load_echo('zechariah')
    merge_echo(existing, ZECH_ECHO)
    save_echo('zechariah', existing)
    covered = sorted(existing.keys(), key=int)
    print(f'  zechariah echo: chapters with data = {covered}')

if __name__ == '__main__':
    main()
