"""
Echo Layer — Ezekiel chapters 6–10
Run: python3 scripts/zc-echo-ezekiel-6-10-fill.py

Chapters already with entries: 9 (seal/mark → Rev 7:3 already present).
This script adds echo entries for chs 6, 7, 8, 10 (and supplements ch 9).

Major echo clusters:
- Ch 6: "know that I am LORD" fulfillment-formula → Phil 2:10-11; remnant memory → Rom 11:5
- Ch 7: The End oracle → Rev 22:10-13; Day of LORD → 1 Thess 5:2; wealth useless in wrath → Jas 5:1-3
- Ch 8: Spirit transport → Rev 4:2; fire/amber figure → Rev 1:14-15; temple departure begins →
  Matt 23:38; 70 elders with censers (perverted worship) → Rev 8:3-4
- Ch 9: Tav mark on forehead → Rev 7:3; 9:4; 14:1; 2 Cor 1:22; judgment from sanctuary → 1 Pet 4:17;
  Elijah/alone intercession → Rom 11:2-4
- Ch 10: Glory departing temple → Matt 23:38; Luke 13:35; temple veil at crucifixion;
  four living creatures (lion/man/cherub/eagle) → Rev 4:6-7; sapphire throne with coals → Rev 4:2; 8:5
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
  "6": {
    "7": [
      {"type": "fulfillment", "target": "Phil 2:10-11", "note": "The 'know that I am the LORD' recognition formula — YHWH's self-assertion through judgment — finds its NT completion in the universal acknowledgment of Jesus as Lord: every knee bows, every tongue confesses that Jesus Christ is Lord, to the glory of God the Father."},
      {"type": "allusion", "target": "Rev 6:15-17", "note": "The slain falling before idols in judgment parallels the great day of wrath in Revelation where kings and commanders hide from the face of him who sits on the throne."}
    ],
    "9": [
      {"type": "allusion", "target": "Rom 11:5", "note": "The surviving remnant who 'remember' YHWH among the nations is the seed of Paul's remnant-by-grace theology: at the present time there is a remnant chosen by grace."},
      {"type": "allusion", "target": "2 Cor 7:10-11", "note": "The exiles loathing themselves for all the evil they have done corresponds to godly sorrow producing repentance: sorrow that leads to salvation and produces earnestness, indignation, and grief over sin."}
    ],
    "14": [
      {"type": "allusion", "target": "Luke 21:24", "note": "The land made desolate throughout all their settlements: Jesus applies the same desolation-formula to Judea in his Olivet discourse, with Jerusalem trodden down by the Gentiles until the times of the Gentiles are fulfilled."}
    ]
  },
  "7": {
    "2": [
      {"type": "allusion-source", "target": "Rev 7:1", "note": "The 'four corners of the land' formula mirrors Revelation's four angels standing at the four corners of the earth holding back the four winds — the same cosmic-geographic totality language for universal judgment."},
      {"type": "allusion-source", "target": "Rev 22:10-13", "note": "The 'end has come' oracle of Ezekiel 7 echoes throughout Revelation's closing: 'Do not seal the words of prophecy... I am coming soon... I am the Alpha and the Omega, the First and the Last, the Beginning and the End.'"}
    ],
    "5": [
      {"type": "allusion-source", "target": "Rev 8:13", "note": "The singular disaster — 'a disaster, a singular disaster' — foreshadows Revelation's triple woe announced by the eagle flying at midheaven."}
    ],
    "7": [
      {"type": "allusion", "target": "1 Thess 5:2-3", "note": "The day near, the time arrived — the Day of LORD motif Ezekiel establishes pervades NT eschatology: the day of the Lord will come like a thief in the night, and when people say 'peace and safety,' destruction will come."}
    ],
    "17": [
      {"type": "allusion-source", "target": "Rev 6:15-17", "note": "All hands going limp and knees going weak is the physiological terror before divine judgment; Revelation 6:15-17 depicts kings and warriors hiding in caves, asking for rocks to fall on them before the wrath of the Lamb."},
      {"type": "allusion-source", "target": "Heb 12:12", "note": "The weakened hands and tottering knees is quoted in Hebrews: 'Strengthen your feeble arms and weak knees' — the judgment-body-image now applied to perseverance toward the Promised Land of the new covenant."}
    ],
    "19": [
      {"type": "allusion-source", "target": "Jas 5:1-3", "note": "Silver and gold useless in the day of wrath — James quotes exactly this principle: your gold and silver have corroded, their corrosion will testify against you and eat your flesh like fire; you have stored up treasure in the last days."},
      {"type": "allusion", "target": "Rev 18:11-17", "note": "The merchants and wealthy who weep over Babylon's fall in Revelation echo this principle: material wealth cannot survive divine judgment; cargo of gold, silver, jewels becomes worthless in one hour."}
    ],
    "26": [
      {"type": "allusion-source", "target": "Mic 3:6-7", "note": "No vision from the prophet, no law from the priest, no counsel from the elders: Micah 3:6-7 describes the same prophetic silence under judgment — the seers will be ashamed, their eyes covered in darkness."},
      {"type": "allusion", "target": "Rev 16:17", "note": "The cascade of disasters with no guidance — report after report of calamity — corresponds to the seventh bowl: 'It is done!' The divine word ends the time of patient warning and begins the time of finality."}
    ]
  },
  "8": {
    "2": [
      {"type": "allusion-source", "target": "Rev 1:14-15", "note": "The divine figure with fire below and gleaming amber above directly parallels the appearance of the risen Christ in Revelation 1: eyes like blazing fire, feet like bronze glowing in a furnace. Ezekiel's throne-chariot visions are the OT template for John's Christophany."},
      {"type": "allusion-source", "target": "Dan 10:6", "note": "The amber/fire figure in Ezekiel 1 and 8 parallels the divine figure of Daniel 10: face like lightning, eyes like torches of fire, arms and feet like gleaming bronze. The same heavenly figure described by both prophets."}
    ],
    "3": [
      {"type": "allusion-source", "target": "Rev 4:2", "note": "The Spirit lifting Ezekiel 'in visions of God' between heaven and earth anticipates John being 'in the Spirit' when he sees the heavenly throne room in Revelation 4. Both prophets are spirit-transported to see the divine court."},
      {"type": "allusion", "target": "Acts 8:39-40", "note": "The Spirit transporting Ezekiel from Babylon to Jerusalem in vision prefigures Philip being physically transported by the Spirit from Gaza to Azotus — the same divine mobility applied to a new covenant minister."}
    ],
    "6": [
      {"type": "allusion-source", "target": "Matt 23:38", "note": "The abominations 'driving me far from my sanctuary' is the beginning of the Glory's departure from the temple (completed in Ezek 10-11). Jesus's 'your house is left to you desolate' (Matt 23:38) is the NT counterpart: the same departure of divine presence from the Second Temple because of Israel's rejection of the Messiah."},
      {"type": "allusion", "target": "John 2:16-17", "note": "Jesus's temple cleansing — 'do not make my Father's house a den of thieves' — directly engages this Ezekielian pattern: the temple defiled by idolatry provokes divine withdrawal. His disciples remember: 'Zeal for your house will consume me' (Ps 69:9)."}
    ],
    "11": [
      {"type": "allusion", "target": "Rev 8:3-4", "note": "The seventy elders with censers offering perverted incense to idols contrasts with the angel at the heavenly altar offering incense with the prayers of the saints in Revelation 8. The same liturgical form — incense, elders, altar — appears in perversion here and in its proper heavenly form in Revelation."}
    ],
    "16": [
      {"type": "allusion-source", "target": "Rev 21:23", "note": "The twenty-five men with backs to the temple worshiping the sun contrasts with the New Jerusalem having no need of sun or moon, for the glory of God gives it light and the Lamb is its lamp. Sun worship is the inversion of the true light."},
      {"type": "allusion", "target": "John 8:12", "note": "Sun worship in the temple's inner court is the perversion that Jesus confronts: 'I am the light of the world; whoever follows me will not walk in darkness.' The sun worshipers look to the wrong source of light."}
    ]
  },
  "9": {
    "4": [
      {"type": "allusion-source", "target": "Rev 7:3", "note": "The tav (final letter of the Hebrew alphabet, written as a cross in ancient script) marked on the foreheads of those who grieve over Jerusalem's sin is the direct source for the sealing of God's servants on their foreheads in Revelation 7:3 and 9:4."},
      {"type": "allusion-source", "target": "Rev 14:1", "note": "Those sealed with the tav are spared in the slaughter; those with the Lamb's name and the Father's name written on their foreheads stand on Mount Zion in Revelation 14:1 — the same protective-mark theology in its eschatological completion."},
      {"type": "allusion", "target": "2 Cor 1:22", "note": "The sealing of the faithful in Ezekiel 9 finds its NT pneumatological form in Paul: God has put his Spirit in our hearts as a seal and deposit, guaranteeing what is to come — the same protective identification enacted through the Spirit."}
    ],
    "6": [
      {"type": "allusion-source", "target": "1 Pet 4:17", "note": "Begin the slaughter at my sanctuary — 1 Peter quotes this Ezekielian principle directly: 'For it is time for judgment to begin at the household of God; and if it begins with us, what will the outcome be for those who do not obey the gospel of God?'"}
    ],
    "8": [
      {"type": "allusion", "target": "Rom 11:2-4", "note": "Ezekiel crying out 'I alone am left!' when the people are slain mirrors Elijah's 'I alone am left' (1 Kgs 19:10), which Paul cites in Romans 11: the remnant pattern — the prophet who thinks he is the last one standing, but YHWH preserves more than he can see."}
    ]
  },
  "10": {
    "1": [
      {"type": "allusion-source", "target": "Rev 4:2-3", "note": "The sapphire/lapis lazuli throne above the cherubim (as in Ezek 1:26) is the OT template for the heavenly throne in Revelation 4: a throne set in heaven with one seated on it with the appearance of jasper and carnelian, with a rainbow like an emerald. Ezekiel's throne-chariot vision is the direct source."},
      {"type": "allusion-source", "target": "Dan 7:9", "note": "The throne above the cherubim parallels Daniel's Ancient of Days whose throne was fiery flames with wheels of burning fire — both visions describe the same heavenly throne-chariot."}
    ],
    "2": [
      {"type": "allusion-source", "target": "Rev 8:5", "note": "The man in linen scattering burning coals over the city directly foreshadows the angel in Revelation 8:5 who takes fire from the altar and throws it to the earth, with thunder, lightning, and earthquake. The coal-scattering is the enacted judgment-form of the incense-prayers of the saints."}
    ],
    "4": [
      {"type": "allusion-source", "target": "Matt 23:38", "note": "The glory of the LORD moving to the temple threshold — the beginning of the departure sequence (culminating in 11:23) — is the ancient type behind Jesus's announcement that the house is left desolate. The Shekinah's departure from Solomon's temple foreshadows the divine presence's departure from the Second Temple after Israel's rejection of the Messiah."},
      {"type": "allusion", "target": "Luke 13:35", "note": "The departure of the glory that fills the temple with cloud corresponds to Jesus's: 'Look, your house is left to you desolate. You will not see me until you say, Blessed is he who comes in the name of the Lord.' Both the original departure and the NT departure end with a promise of return."}
    ],
    "7": [
      {"type": "allusion", "target": "Matt 27:51", "note": "The coals taken from between the cherubim and the associated departing of glory from the temple find their NT counterpart in the tearing of the temple veil at the crucifixion — the moment when the presence once inhabiting the Most Holy Place departs as Jesus gives up his spirit, and the veil separating the divine presence is removed."}
    ],
    "11": [
      {"type": "allusion-source", "target": "Rev 4:6-8", "note": "The cherubim and wheels moving in any direction without turning, covered with eyes, correspond exactly to the four living creatures of Revelation 4: full of eyes all around and within, able to move in any direction. John's vision of the heavenly throne draws directly on Ezekiel 1 and 10."}
    ],
    "14": [
      {"type": "allusion-source", "target": "Rev 4:7", "note": "The four faces of the cherubim — cherub (ox), man, lion, eagle — are the four living creatures of Revelation 4: the first like a lion, the second like an ox, the third with a face like a man, the fourth like a flying eagle. The same fourfold representation of creation before the divine throne."}
    ],
    "18": [
      {"type": "allusion-source", "target": "Luke 21:6", "note": "The glory of the LORD departing from the temple threshold parallels Jesus's departure announcement: 'As for what you see here — the time will come when not one stone will be left on another; every one of them will be thrown down.' The departure of divine presence precedes the destruction of the building."},
      {"type": "allusion", "target": "Rev 21:3", "note": "The departure of the Shekinah in Ezekiel points forward to its return: Revelation 21:3 — 'the dwelling of God is with humanity; he will dwell with them, and they will be his people, and God himself will be with them' — is the final reversal of the Ezekiel 10-11 departure."}
    ]
  }
}

def main():
    existing = load_echoes('ezekiel')
    merge_echo(existing, EZK_ECHOES)
    save_echoes('ezekiel', existing)

    out = json.loads((ROOT / 'data/echoes/ezekiel.json').read_text())
    for ch in [6, 7, 8, 9, 10]:
        ck = str(ch)
        count = sum(len(v) for v in out.get(ck, {}).values())
        status = 'done' if out.get(ck) else 'MISSING'
        print(f'ch {ch}: {status} ({len(out.get(ck, {}))} verse-keys, {count} entries total)')

if __name__ == '__main__':
    main()
