"""
echo | Leviticus | chapters 22-23
Run: python3 scripts/zc-echo-leviticus-22-23-fill.py

Ch 22: Priestly holiness and acceptable sacrifices — tamim (without defect) requirement
Ch 23: The appointed feasts (mo'adei YHWH) — the entire liturgical calendar as NT types:
  - Sabbath (v3) -> Heb 4:9-10
  - Passover (v5) -> 1 Cor 5:7; John 1:29
  - Firstfruits (v10-11) -> 1 Cor 15:20,23 (Christ the firstfruits of resurrection)
  - Feast of Weeks / Pentecost (v15-16) -> Acts 2:1-4
  - Feast of Trumpets (v24) -> 1 Thess 4:16; 1 Cor 15:52
  - Day of Atonement (v27-28) -> Heb 9:7; Rom 3:25
  - Feast of Tabernacles (v34-36) -> John 7:2,37-39; Col 2:17
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
  "22": {
    "20": [
      {"type": "fulfillment", "target": "1 Pet 1:19", "note": "You shall not offer anything that has a defect, for it will not be accepted for you — the tamim (without defect) standard for sacrificial animals is applied to Christ in 1 Pet 1:18-19: redeemed not with corruptible things but with the precious blood of Christ, a lamb without blemish or defect. Every animal sacrifice's unblemished requirement pointed to the one perfect sacrifice whose perfection is not physical but moral and ontological."},
      {"type": "allusion", "target": "Heb 9:14", "note": "The defect-free offering requirement — Christ offered himself without blemish to God through the eternal Spirit (Heb 9:14); the Levitical tamim requirement is fulfilled in Christ's moral and ontological perfection as the sinless Son who became the one acceptable sacrifice."}
    ],
    "32": [
      {"type": "allusion", "target": "1 Pet 1:15", "note": "I am YHWH who sanctifies you — the divine self-identification formula that grounds the holiness imperative throughout Lev 17-26; Peter draws on this Holiness Code pattern: as he who called you is holy, be holy yourselves in all your conduct (1 Pet 1:15-16, citing Lev 19:2 and 11:44-45), applying the Holiness Code's divine-character-as-ground to the new covenant community."}
    ]
  },
  "23": {
    "3": [
      {"type": "fulfillment", "target": "Heb 4:9", "note": "Six days you shall do your work, but on the seventh day you shall rest — the Sabbath command of Lev 23:3 opens the feast calendar; Hebrews 4:9-10 interprets the Sabbath eschatologically: there remains a Sabbath rest for the people of God, for whoever has entered God's rest has also rested from his works as God did from his. The weekly Sabbath is the sign pointing to the final eschatological rest secured through Christ (Heb 4:3)."},
      {"type": "allusion", "target": "Col 2:16", "note": "Do not let anyone judge you with regard to... a Sabbath — Paul in Col 2:17 states that the appointed feasts, new moons, and Sabbaths are a shadow of the things to come, but the substance belongs to Christ. The Sabbath that opens Lev 23's feast calendar is the first of the shadows that find their substance in Christ's completed work and coming rest."}
    ],
    "5": [
      {"type": "fulfillment", "target": "1 Cor 5:7", "note": "In the first month, on the fourteenth day of the month at twilight is the LORD's Passover — the Passover that heads the feast calendar (Lev 23:5) is the type that Paul identifies as fulfilled in Christ: Christ our Passover lamb has been sacrificed. The feast of the LORD becomes the feast of the Lord Christ whose sacrifice was timed to coincide with the Passover lambs' slaughter (John 19:14)."},
      {"type": "fulfillment", "target": "John 1:29", "note": "The Passover lamb (Lev 23:5) is the type of the Lamb of God who takes away the sin of the world (John 1:29); John's Gospel structures the crucifixion to coincide with the Passover sacrifice, identifying Jesus as the fulfillment of the Passover mo'ed (appointed time)."}
    ],
    "6": [
      {"type": "allusion", "target": "1 Cor 5:8", "note": "On the fifteenth day of the same month is the Feast of Unleavened Bread — seven days of bread without leaven follows the Passover; Paul applies this directly: let us therefore celebrate the festival, not with the old leaven of malice and wickedness, but with the unleavened bread of sincerity and truth. The post-Passover life of the new covenant community is the festival of Unleavened Bread lived in moral purity."}
    ],
    "11": [
      {"type": "fulfillment", "target": "1 Cor 15:20", "note": "He shall wave the sheaf before the LORD on the day after the Sabbath — the Firstfruits offering (omer ha-reshit), waved before YHWH on the Sunday following Passover week, is the type of Christ's resurrection: Christ has been raised from the dead, the firstfruits of those who have fallen asleep (1 Cor 15:20). The exact timing of the firstfruits offering — on the day after the Sabbath — corresponds to the Sunday of Christ's resurrection."},
      {"type": "fulfillment", "target": "1 Cor 15:23", "note": "The firstfruits wave offering points to the resurrection order: each in his own order: Christ the firstfruits, then at his coming those who belong to Christ. The Levitical firstfruits offering is a pledge of the coming harvest; Christ's resurrection is the pledge of the general resurrection harvest at his return."}
    ],
    "15": [
      {"type": "fulfillment", "target": "Acts 2:1", "note": "You shall count fifty days to the day after the seventh Sabbath — the Feast of Weeks (Shavuot) falls fifty days after the firstfruits offering, hence 'Pentecost' (Greek for fiftieth). Acts 2:1-4: when the day of Pentecost arrived they were all together in one place; the outpouring of the Holy Spirit occurs precisely at the feast that celebrates the fifty-day harvest after the firstfruits. Christ's resurrection (firstfruits) is followed fifty days later by the Spirit's outpouring (harvest of souls)."}
    ],
    "16": [
      {"type": "fulfillment", "target": "Acts 2:4", "note": "Count fifty days to the day after the seventh Sabbath; then you shall present a grain offering of new grain to the LORD — the new grain offering of Pentecost corresponds to the new community of the Spirit at Pentecost: the 3,000 who are baptized (Acts 2:41) are the new harvest wave-offering, the first-fruits of the new covenant's harvest of souls. The wave offering of new grain is the type of the Spirit's harvest on the day of Pentecost."}
    ],
    "24": [
      {"type": "allusion", "target": "1 Thess 4:16", "note": "In the seventh month, on the first day of the month, you shall observe a day of solemn rest, a memorial proclaimed with blast of trumpets — the Feast of Trumpets (Yom Teruah) is the feast of the awakening blast; Paul describes the return of Christ with the same trumpet imagery: the Lord himself will descend from heaven with a cry of command, with the voice of an archangel, and with the sound of the trumpet of God (1 Thess 4:16). The annual trumpet blast that opens the seventh month is the type of the eschatological trumpet that inaugurates the resurrection."},
      {"type": "allusion", "target": "1 Cor 15:52", "note": "The Feast of Trumpets' shofar blast points to the last trumpet: in a moment, in the twinkling of an eye, at the last trumpet — for the trumpet will sound, and the dead will be raised imperishable, and we shall be changed (1 Cor 15:52). The mo'ed of trumpets is the annual rehearsal for the final trumpeting that announces the resurrection."}
    ],
    "27": [
      {"type": "fulfillment", "target": "Heb 9:7", "note": "On the tenth day of this seventh month is the Day of Atonement (Yom Kippur) — the annual high-priestly entry into the most holy place with blood; Hebrews 9:7 cites this as the type of Christ's once-for-all entry: into the second tent only the high priest goes, and only once a year, and not without blood; the structure of Lev 23:27-28's annual restriction is the negative image of Christ's permanent, unrepeated access."},
      {"type": "fulfillment", "target": "Rom 3:25", "note": "Afflict yourselves, for it is a Day of Atonement — the communal fast and the high priest's atonement sacrifice (Lev 16) is the context for Paul's declaration that God presented Christ as a hilasterion (mercy seat / propitiation) through faith in his blood. The Day of Atonement's annual atonement is superseded by the cross's once-for-all propitiation."}
    ],
    "34": [
      {"type": "fulfillment", "target": "John 7:2", "note": "On the fifteenth day of this seventh month is the Feast of Booths (Sukkoth) for seven days before the LORD — John 7:2 situates Jesus's teaching in Jerusalem at the feast that is most pregnant with fulfillment: the Feast of Tabernacles. On the last day of the feast, Jesus stood up and cried out: If anyone thirsts, let him come to me and drink (John 7:37) — the water-pouring ceremony of Sukkoth (Simchat Beit HaShoevah) becomes the occasion for Jesus's proclamation of the Spirit."},
      {"type": "fulfillment", "target": "John 7:37", "note": "The Feast of Tabernacles — on the last day of the feast, the greatest day, Jesus stood up and cried out, If anyone thirsts, let him come to me and drink. Whoever believes in me, as the Scripture has said, out of his heart will flow rivers of living water. He said this about the Spirit (John 7:38-39). The feast of dwelling in booths, commemorating YHWH's care for Israel in the wilderness, becomes the occasion for Christ's proclamation that he is the source of the Spirit-water for which the feast's water ceremonies longed."}
    ],
    "36": [
      {"type": "allusion", "target": "Col 2:17", "note": "These are a shadow of the things to come, but the substance belongs to Christ — Paul's programmatic statement about the Levitical feast calendar (Col 2:16-17). The Sabbath, new moon, and feasts that Lev 23 enumerates are all shadows whose substance is Christ. The feast calendar is not arbitrary legislation but a prophetic calendar encoding the shape of the messianic work: death (Passover), purification (Unleavened Bread), resurrection (Firstfruits), Spirit (Pentecost), return (Trumpets), final atonement (Yom Kippur), eternal dwelling (Tabernacles)."}
    ],
    "43": [
      {"type": "allusion", "target": "John 1:14", "note": "So that your generations may know that I made the people of Israel dwell in booths when I brought them out of the land of Egypt — the Feast of Booths commemorates YHWH's tabernacling with Israel in the wilderness; John 1:14 uses the same term: the Word became flesh and eskenosen (tabernacled) among us. The annual commemoration of the wilderness booths is the type of the incarnation — God dwelling with humanity in the temporary, vulnerable form of a booth/tent."},
      {"type": "allusion", "target": "Rev 21:3", "note": "The commemorated wilderness dwelling — YHWH tabernacling with Israel in booths — points to the final tabernacling: Behold, the dwelling place (skene) of God is with man. He will dwell (skenoo) with them (Rev 21:3). The Feast of Tabernacles that commemorates past booth-dwelling is the annual rehearsal of the eschatological dwelling that John's Apocalypse envisions as the goal of all history."}
    ]
  }
}

def main():
    e = load_echo('leviticus')
    merge_echo(e, ECHO)
    save_echo('leviticus', e)
    print('Leviticus 22-23 echo written.')

if __name__ == '__main__':
    main()
