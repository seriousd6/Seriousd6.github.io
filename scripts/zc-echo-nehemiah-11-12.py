"""
Echo Layer — Nehemiah chapters 11–12
Run: python3 scripts/zc-echo-nehemiah-11-12.py

Ch 11: Repopulation of Jerusalem by lot — one tenth of the people chosen to dwell
  in the holy city; heads of families who volunteered; lists of settlers by tribe.
Ch 12: High-priestly succession (vv1-26); dedication of the wall with two great
  choirs processing in opposite directions and meeting at the temple (vv27-47).

Key echo connections:
- 11:1: Lots cast to assign one-tenth to Jerusalem → Rev 21:27 (only those written
  in the Lamb's book of life enter the holy city)
- 11:2: Men who willingly volunteered to dwell in Jerusalem → Rom 12:1 (present
  your bodies as a living sacrifice)
- 12:10-11: High-priestly succession prevented by death → Heb 7:23-24 (Christ's
  permanent priesthood because he lives forever)
- 12:27: Dedication of Jerusalem's wall → Rev 21:2; Heb 12:22-24
- 12:30: Purification before dedication → Heb 10:22 (hearts sprinkled, bodies washed)
- 12:43: Joy of dedication heard from afar → Zeph 3:14-17; Phil 4:4
- 12:44-47: Systematic provision for priests and Levites → 1 Cor 9:13-14
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

NEH_ECHO_11_12 = {
  "11": {
    "1": [
      {"type": "allusion", "target": "Rev 21:27", "note": "One in ten of the people of Judah is chosen by lot to live in Jerusalem, 'the holy city' (<em>ʿîr haqqōḏeš</em>) — the very name signals that who dwells there matters covenantally; the selection by lot means no one can claim the right to live in the holy city by personal merit or social position; Revelation's vision of the consummated Jerusalem applies the same principle: 'nothing impure will ever enter it, nor will anyone who does what is shameful or deceitful, but only those whose names are written in the Lamb's book of life' (Rev 21:27); belonging to the holy city is by divine election, not human claim"},
      {"type": "allusion", "target": "Eph 2:19", "note": "The repopulation of Jerusalem creates a community of those who are 'fellow citizens' (<em>ʿammê hāʿîr</em>, lit. people of the city) in the holy city — a status that depends on being assigned or choosing to dwell there; Paul's announcement of the Gentiles' inclusion uses the same civic language: 'you are no longer foreigners and strangers, but fellow citizens with God's people and also members of his household' (Eph 2:19); the earthly Jerusalem's population logic — determined by divine allotment, not ethnicity — foreshadows the new Jerusalem's citizenship, which depends entirely on grace"}
    ],
    "2": [
      {"type": "allusion", "target": "Rom 12:1", "note": "Beyond those assigned by lot, some men 'willingly offered themselves' (<em>hiṯnaḏḏᵉḇû</em>, from <em>nāḏaḇ</em>, the root of 'freewill offering') to dwell in Jerusalem — the same voluntary-consecration vocabulary used of those who gave freely for the tabernacle (Exod 35:21-29) and the temple (1 Chr 29:5-9); Paul calls the whole Christian life a 'voluntary offering': 'I urge you, brothers and sisters, in view of God's mercy, to offer your bodies as a living sacrifice' (Rom 12:1); the people who blessed these volunteers for choosing the difficult life in an underpopulated city are the type of the community that honors those who give themselves fully to God's purposes"}
    ],
    "17": [
      {"type": "allusion", "target": "Col 3:16", "note": "Mattaniah, son of Micha, son of Zabdi, son of Asaph, held the role of 'the leader in the thanksgiving prayer' (<em>rōʾš hattᵉhillāh</em>) — the appointed leader who began the prayers of praise in the temple liturgy; his genealogy traces back to Asaph, David's chief worship leader (1 Chr 16:4-5); Paul describes the equivalent function in the new-covenant community: 'let the word of Christ dwell in you richly as you teach and admonish one another with all wisdom through psalms, hymns, and songs from the Spirit, singing to God with gratitude in your hearts' (Col 3:16); the appointed leader of thanksgiving in Nehemiah 11 anticipates the Spirit-led worship of the body of Christ"}
    ],
    "22": [
      {"type": "allusion", "target": "1 Cor 12:28", "note": "Uzzi son of Bani is appointed as 'overseer of the Levites' at Jerusalem, with a specific mandate: 'for the king's command was upon them' regarding 'the duty of the singers, as every day required' — the regular, daily appointment of gifted people for the ordered worship of God in the holy city; Paul describes the same pattern of appointed gifting in the new-covenant community: 'And God has placed in the church first of all apostles, second prophets, third teachers, then miracles, then gifts of healing, of helping, of guidance, and of different kinds of tongues' (1 Cor 12:28); the organized appointment of worship gifts is a consistent feature of the covenant community across both testaments"}
    ],
    "36": [
      {"type": "allusion", "target": "Eph 4:4", "note": "The Levites' divisions are distributed 'in Judah and Benjamin' — not concentrated in Jerusalem but spread throughout the tribes so that priestly service and instruction are available across the whole people; the distribution of the Levites across both tribal territories is the OT pattern of the 'body' that needs every member in its proper place; Paul's vision of the new-covenant community applies the same distribution principle: 'There is one body and one Spirit, just as you were called to one hope when you were called; one Lord, one faith, one baptism; one God and Father of all, who is over all and through all and in all' (Eph 4:4-6); unity in diversity, centered on one Lord but expressed through distributed service"}
    ]
  },
  "12": {
    "10": [
      {"type": "allusion", "target": "Heb 7:23", "note": "The genealogy of the high priests records six generations of succession: Jeshua → Joiakim → Eliashib → Joiada → Jonathan/Johanan → Jaddua — a chain of succession where each priest's ministry ends with his death and another must take his place; the author of Hebrews identifies this continuous succession as the fundamental weakness of the Aaronic priesthood: 'Now there have been many of those priests, since death prevented them from continuing in office; but because Jesus lives forever, he has a permanent priesthood' (Heb 7:23-24); the high-priestly genealogy of Nehemiah 12 is the literary record of the very mortality that makes the Aaronic order provisional and anticipatory of the one priest who holds his office by 'the power of an indestructible life' (Heb 7:16)"}
    ],
    "27": [
      {"type": "type", "target": "Rev 21:2", "note": "The dedication of the wall of Jerusalem — '<em>ḥᵃnukkaṯ ḥômaṯ yᵉrûšālaim</em>' — is a formal consecration ceremony: the Levites are gathered from all their places, the singers are assembled, two great choirs process around the city walls in opposite directions and converge at the temple with sacrifice and great joy; Revelation's climactic vision is of a Jerusalem that comes down 'prepared as a bride beautifully dressed for her husband' (Rev 21:2) — the dedication of Nehemiah 12 is the historical type of the eschatological dedication of the new Jerusalem; the convergence of two choirs at the temple foreshadows the gathering from east and west that Christ announces (Matt 8:11) and Revelation depicts (Rev 7:9-17)"},
      {"type": "allusion", "target": "Heb 12:22", "note": "The people 'come to Jerusalem' from all their places to dedicate the wall — a pilgrimage to the holy city for a liturgical event of consecration; the author of Hebrews uses the same language of 'coming to Jerusalem' to describe what all believers have already received in Christ: 'But you have come to Mount Zion, to the city of the living God, the heavenly Jerusalem. You have come to thousands upon thousands of angels in joyful assembly, to the church of the firstborn, whose names are written in heaven' (Heb 12:22-23); the physical pilgrimage of Nehemiah 12:27 is the earthly anticipation of the spiritual reality that is already present for those in Christ"}
    ],
    "30": [
      {"type": "allusion", "target": "Heb 10:22", "note": "Before the dedication procession, the priests and Levites 'purified themselves and purified the people, the gates, and the wall' — comprehensive ritual purification is the necessary preparation for the consecration of the holy city; the wall dedication cannot proceed without prior cleansing; Hebrews announces the NT fulfillment of this purification pattern: 'having our hearts sprinkled to cleanse us from a guilty conscience and having our bodies washed with pure water, let us draw near to God with a sincere heart and with the full assurance that faith brings' (Heb 10:22); the purification of Nehemiah 12:30 is the type of the definitive cleansing that Christ's blood accomplishes, enabling a dedication and drawing-near that is permanent, not repeated"}
    ],
    "31": [
      {"type": "allusion", "target": "Rev 5:9", "note": "Nehemiah appoints two great companies (<em>tôḏôṯ gᵉḏōlôṯ</em>, 'great thanksgiving choirs') that process in opposite directions around the wall — one going to the right (toward the Dung Gate) and one to the left (toward the Gate of Ephraim), eventually converging at the house of God; this double-choir encirclement of Jerusalem as an act of thanksgiving and dedication is the earthly pattern of the heavenly worship Revelation describes: 'And they sang a new song: You are worthy... because you were slain, and with your blood you purchased for God persons from every tribe and language and people and nation' (Rev 5:9); the procession of thanksgiving around the holy city points to the gathering of all peoples at the heavenly Jerusalem in praise to the Lamb"}
    ],
    "43": [
      {"type": "allusion", "target": "Zeph 3:14", "note": "The dedication ceremony produces such great joy that 'the women and children also rejoiced' and 'the sound of rejoicing in Jerusalem could be heard far away' — the joy of the dedicated holy city becoming audible beyond its borders; Zephaniah had prophesied exactly this: 'Sing, Daughter Zion; shout aloud, Israel! Be glad and rejoice with all your heart, Daughter Jerusalem!... The LORD your God is with you, the Mighty Warrior who saves. He will take great delight in you; in his love he will no longer rebuke you, but will rejoice over you with singing' (Zeph 3:14-17); the joy heard from afar at Nehemiah's dedication is the historical earnest of the eschatological rejoicing that Zephaniah announces — the joy of YHWH himself over his restored city"},
      {"type": "allusion", "target": "Phil 4:4", "note": "The 'great rejoicing' (<em>śimḥāh gᵉḏōlāh</em>) that God himself causes ('for God had given them great joy') is the fruit of covenant faithfulness restored — the wall rebuilt, the community gathered, the word read, the worship ordered; Paul's command to the church at Philippi reflects the same structural reality: 'Rejoice in the Lord always. I will say it again: Rejoice!' (Phil 4:4) — not joy in circumstances but joy that comes from the Lord's presence and acts; Nehemiah 12:43 shows the OT pattern of this God-given joy that exceeds what the situation visibly warrants, heard afar because it is not generated by human effort alone"}
    ],
    "44": [
      {"type": "allusion", "target": "1 Cor 9:13", "note": "On the day of dedication, men are appointed over the 'storerooms for contributions, firstfruits, and tithes... to collect into them from the fields of the towns the portions required by the Torah for the priests and Levites' — the institutional provision for those who serve the sanctuary; Paul draws on this very OT arrangement to establish the principle of support for gospel ministers: 'Don't you know that those who serve in the temple get their food from the temple, and that those who serve at the altar share in what is offered on the altar? In the same way, the Lord has commanded that those who preach the gospel should receive their living from the gospel' (1 Cor 9:13-14); the storeroom system of Nehemiah 12:44 is the OT template that Paul explicitly invokes to argue for the material support of NT ministers"}
    ],
    "45": [
      {"type": "allusion", "target": "Rev 22:3", "note": "The singers and gatekeepers keep 'the service of their God and the service of purification, as commanded by David and his son Solomon' — temple service ordered and sustained according to the Davidic pattern; the gatekeepers and singers serve continuously in their appointed roles; Revelation's description of the new creation promises: 'No longer will there be any curse. The throne of God and of the Lamb will be in the city, and his servants will serve him' (Rev 22:3); the ordered, continuous service of God's house in Nehemiah 12:45 is the earthly anticipation of the eternal service in God's presence that the new creation brings — service that is no longer defined by purification rites because what needed cleansing has been definitively removed"}
    ],
    "46": [
      {"type": "allusion", "target": "Amos 9:11", "note": "The tradition of praise and thanksgiving is traced back to 'the days of David and Asaph of old, there were directors for the singers and for the songs of praise and thanksgiving to God' — the worship of the post-exilic community is explicitly grounded in the Davidic pattern; Amos had promised: 'In that day I will restore David's fallen shelter — I will repair its broken walls and restore its ruins — and will rebuild it as it used to be' (Amos 9:11); the restoration of Davidic worship in Nehemiah 12:46 is the historical fulfillment of Amos's prophecy, though not its eschatological climax — that comes when Christ, the Son of David, establishes the definitive Davidic worship in the new creation (Acts 15:16-17)"}
    ],
    "47": [
      {"type": "allusion", "target": "Gal 6:6", "note": "The whole community of Israel 'set apart the portions for the singers and the gatekeepers' daily — the ongoing, systematic support of those who served in the LORD's house; the Levites in turn 'set apart the holy things for the sons of Aaron'; the pattern of those who receive support sharing what they have with those above them in the service chain; Paul applies the same mutual-support principle to the new-covenant community: 'Nevertheless, the one who receives instruction in the word should share all good things with their instructor' (Gal 6:6); the tithe-chain of Nehemiah 12:47 is the OT background for Paul's instruction about sharing material support with those who teach the word"}
    ]
  }
}

def main():
    e = load_echo('nehemiah')
    before_chs = set(e.keys())
    merge_echo(e, NEH_ECHO_11_12)
    after_chs = set(e.keys())
    new_chs = sorted(after_chs - before_chs, key=int)
    save_echo('nehemiah', e)
    added = sum(len(v) for v in NEH_ECHO_11_12.values())
    print(f'nehemiah echo ch 11-12: added {added} chapter-entries; ch11 and ch12 now complete')
    if new_chs:
        print(f'  new chapters: {new_chs}')

if __name__ == '__main__':
    main()
