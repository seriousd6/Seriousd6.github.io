"""
echo | zechariah | ch8–13 | completing ch8 and ch10 (ch9, 11-13 already have entries)
run: python3 scripts/zc-echo-zechariah-8-13.py

Key echo decisions:
- ch8:v2: divine jealousy/zeal for Zion → Paul's divine-jealousy for the church (2 Cor 11:2)
- ch8:v3: YHWH returns to dwell in Jerusalem → John 1:14 incarnation (Word tabernacles among us)
- ch8:v8: covenant formula 'my people / their God' → NT new covenant fulfillment texts
- ch8:v13: Israel as blessing to nations → Gal 3:14 (blessing of Abraham to Gentiles in Christ)
- ch8:v22-23: nations streaming to Jerusalem / taking hold of robe of one Jew → Rev 21:24-26
- ch10:v4: cornerstone from Judah → Eph 2:20; Matt 21:42; 1 Pet 2:6-7
- ch10:v3: YHWH tends flock → John 10:11-14 (Good Shepherd)
- ch10:v8-9: ingathering of scattered → John 11:52 (gathering scattered children of God)
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

ZECHARIAH_ECHOES = {
  "8": {
    "2": [
      {
        "type": "allusion",
        "target": "2 Cor 11:2",
        "note": "YHWH declares 'I am burning with jealousy for Zion — great jealousy.' Paul employs the same language for his pastoral care of the church: 'I feel a divine jealousy for you, for I betrothed you to one husband, to present you as a pure virgin to Christ.' The divine jealousy (<em>qin'ah</em>) that Zechariah describes for the earthly Zion becomes the apostolic jealousy for the NT Zion — the church as the bride of Christ."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "John 1:14",
        "note": "YHWH declares 'I have returned to Zion and will live (<em>shakhanti</em>) in Jerusalem' — the Shekinah-dwelling returning after its departure in Ezekiel 10-11. John 1:14 uses the same tabernacle-dwelling language for the incarnation: 'the Word became flesh and dwelt (<em>eskēnōsen</em>, tabernacled) among us.' The return of YHWH's dwelling-presence that Zechariah envisions is fulfilled in the personal presence of the incarnate Son."
      },
      {
        "type": "allusion",
        "target": "Rev 21:3",
        "note": "Jerusalem called 'the faithful city' and YHWH dwelling in it — Rev 21:3 applies the same covenant-presence language to the new Jerusalem: 'Behold, the dwelling place of God is with man; he will dwell with them, and they will be his people.' Zechariah's restoration Jerusalem is the OT type; the new Jerusalem where God himself will be their God is the final fulfillment."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Rev 21:3",
        "note": "The covenant formula 'They will be my people and I will be their God, in faithfulness and righteousness' is the OT's most concise statement of covenant relationship. Rev 21:3-4 applies it to the new creation: 'he will dwell with them, and they will be his people, and God himself will be with them as their God.' The formula first spoken at Sinai (Exod 6:7; Lev 26:12) reaches its final form in the new Jerusalem."
      },
      {
        "type": "allusion",
        "target": "Heb 8:10",
        "note": "The covenant-renewal formula 'I will be their God and they will be my people' is quoted in Heb 8:10 from Jer 31:33 as the content of the new covenant written on the heart. Zechariah 8:8 announces this covenant formula in the restoration context; the Epistle to the Hebrews declares it fulfilled in the new covenant mediated by Christ."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Gal 3:14",
        "note": "'Just as you were a curse among the nations, so I will save you, and you will be a blessing. Do not be afraid.' The reversal from curse to blessing is the covenant pattern Paul applies to the cross: 'so that in Christ Jesus the blessing of Abraham might come to the Gentiles' (Gal 3:14). Israel becomes a blessing to the nations not merely by national restoration but through the Messiah who absorbs the curse (Gal 3:13) and becomes the source of blessing for all nations."
      }
    ],
    "19": [
      {
        "type": "allusion",
        "target": "John 16:20",
        "note": "'The fasts of the fourth, fifth, seventh, and tenth months will become occasions of joy and gladness and cheerful feasts.' The mourning-fasts commemorating Jerusalem's fall (each month marking a stage of the 586 BCE siege) are transformed into feasts. Jesus applies the same mourning-to-joy reversal to his disciples at the Last Supper: 'your sorrow will turn to joy' (John 16:20-22). The grief of Jerusalem's destruction becomes gladness through the one who is resurrection and life."
      }
    ],
    "22": [
      {
        "type": "allusion",
        "target": "Acts 15:17",
        "note": "'Many peoples and powerful nations will come to seek the LORD of Hosts in Jerusalem.' The nations streaming to seek YHWH in Jerusalem is the eschatological vision that James cites at the Jerusalem Council (Acts 15:17, quoting Amos 9:12 LXX) as being fulfilled in the Gentile mission: the nations seeking the Lord flows from the raised Davidic dynasty — Christ. Zechariah 8:22 envisions the same ingathering that the apostolic mission begins to fulfill."
      }
    ],
    "23": [
      {
        "type": "allusion",
        "target": "Rev 21:24",
        "note": "'Ten men from every nation and language will take hold of the robe of one Jew, saying Let us go with you, for we have heard that God is with you.' The nations clinging to the one Jew is read by the church fathers as a prophecy of the nations drawn to Christ — the one Jew in whom God is supremely present (Immanuel). Rev 21:24-26 shows the nations streaming into the new Jerusalem and bringing their glory into it. The one whose robe the nations grasp fulfills Zechariah's 'God is with him': 'they shall call his name Immanuel — God with us' (Matt 1:23)."
      }
    ]
  },
  "10": {
    "3": [
      {
        "type": "allusion",
        "target": "John 10:11",
        "note": "'The LORD of Hosts tends his flock, the house of Judah, and makes them like his majestic horse in battle.' YHWH as the true shepherd over against the false shepherds is the explicit setting for Jesus's Good Shepherd discourse (John 10:11-14: 'I am the good shepherd'). Ezekiel 34:15-16 applies the same pattern — YHWH himself will shepherd his sheep after the failure of human shepherds — which Jesus claims as his own mission."
      }
    ],
    "4": [
      {
        "type": "fulfillment",
        "target": "Matt 21:42",
        "note": "'From Judah will come the cornerstone (<em>pinna</em>).' Jesus quotes Ps 118:22 at the close of the parable of the tenants — 'the stone the builders rejected has become the cornerstone' — which Matt 21:42 applies as the OT's prediction of the rejected-and-vindicated Messiah. Zechariah 10:4 roots the cornerstone in the tribe of Judah, tying the Davidic lineage to the cornerstone identity that Jesus claims."
      },
      {
        "type": "allusion",
        "target": "Eph 2:20",
        "note": "'From Judah will come the cornerstone, from him the tent peg, from him the battle bow, from him every ruler.' Paul describes the church as 'built on the foundation of the apostles and prophets, Christ Jesus himself being the cornerstone' (Eph 2:20). The Zechariah 10:4 portrait of the one from Judah who is cornerstone, tent-peg, battle-bow, and ruler anticipates the NT's multi-faceted portrait of Christ as the source of every covenant function."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Rom 11:26",
        "note": "'I will strengthen the house of Judah and save the house of Joseph... they will be as if I had not rejected them, for I am the LORD their God and I will answer them.' The comprehensive restoration of both houses (Judah and Joseph = the divided kingdom reunited) is the eschatological hope that Paul draws on in Romans 11:25-26: 'all Israel will be saved.' The 'as if I had not rejected them' language anticipates Paul's mystery of Israel's regrafting after the Gentile fullness comes in."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "John 11:52",
        "note": "'I will signal for them and gather them, for I have redeemed them; they will be as numerous as before.' The divine ingathering of scattered Israel is the template for the NT's universal gathering. John 11:52 identifies Jesus's death as 'to gather into one the children of God who are scattered abroad' — the eschatological ingathering that Zechariah anticipates is accomplished through the cross. The 'as numerous as before' points to a fullness exceeding the original, fulfilled in the NT church as the Israel of God drawn from all nations."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Rev 15:2",
        "note": "'He will pass through the sea of distress and strike down the waves; all the depths of the Nile will dry up.' The divine passage through and conquest of the sea — the Exodus pattern — becomes in Revelation the image of those who have 'conquered the beast' standing beside 'what appeared to be a sea of glass mixed with fire' (Rev 15:2). The sea of distress that YHWH passes through on behalf of his people in Zechariah is the type of Christ's passage through death and the final conquest of all that the sea represents."
      }
    ]
  }
}

def main():
    existing = load_echo('zechariah')
    merge_echo(existing, ZECHARIAH_ECHOES)
    save_echo('zechariah', existing)
    print('Zechariah 8–13 echoes written.')

if __name__ == '__main__':
    main()
