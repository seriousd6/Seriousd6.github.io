"""
echo layer: Ezekiel 23-25
Key echo clusters:
  - ch23 cup of horror → Mark 10:38-39 (cup Jesus must drink); ch23 two-sisters allegory → 2 Cor 11:2; Rev 17
  - ch24 date recorded → Luke 19:44; ch24 uncleansed lewdness → Heb 9:13-14; ch24 mouth opened → Luke 1:64
  - ch25 OAN revenge-motif → Rom 12:19; 2 Thess 1:6-8; ch25 Edom → Rom 9:13; Obad 1
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

EZEKIEL_ECHOES = {
  "23": {
    "4": [
      {"type": "shadow", "target": "2 Cor 11:2", "note": "The two sisters Oholah (Samaria) and Oholibah (Jerusalem) who became YHWH's wives and then committed adultery with the nations is the OT allegory that Paul's betrothal language presupposes: I betrothed you to one husband, to present you as a pure virgin to Christ (2 Cor 11:2); the covenant people who are to remain faithful to their divine husband rather than committing adultery with the world-system is the continuity between Ezekiel's allegory and Paul's pastoral concern."},
      {"type": "shadow", "target": "Rev 17:1-2", "note": "The two adulterous sisters who played the whore with the nations — Egypt, Assyria, Babylon — provide the primary OT template for the great prostitute who sits on many waters, with whom the kings of the earth have committed sexual immorality (Rev 17:1-2); the harlot who commits spiritual adultery with empires in Ezekiel 23 becomes the figure of Babylon in Revelation 17, and the divine judgment announced in both chapters follows the same pattern."}
    ],
    "18": [
      {"type": "allusion", "target": "Eph 4:18", "note": "My soul was alienated from her as my soul had been alienated from her sister — the divine alienation from the covenant people who have persistently defiled themselves anticipates Paul's description of Gentile alienation: they are darkened in their understanding, alienated from the life of God because of the ignorance that is in them (Eph 4:18); in both cases, the alienation is a consequence of spiritual hardening, and in both cases the resolution is the divine initiative of drawing near — accomplished in Christ (Eph 2:13)."}
    ],
    "32": [
      {"type": "type", "target": "Mark 10:38-39", "note": "You shall drink your sister's cup which is deep and wide; you will be filled with drunkenness and sorrow, the cup of horror and desolation — the cup of divine judgment poured out on the unfaithful covenant people is the type Jesus invokes at Gethsemane: Father, let this cup pass from me (Matt 26:39) and when James and John seek glory: can you drink the cup that I drink? (Mark 10:38-39); Jesus's drinking of the covenant-judgment cup on behalf of his people is the christological resolution of the judgment that Ezekiel's sisters face."},
      {"type": "allusion", "target": "Rev 16:19", "note": "The cup of horror and desolation the sisters must drink is the OT template for Revelation's cup of divine wrath: Babylon the great was remembered before God, to make her drain the cup of the wine of the fury of his wrath (Rev 16:19); the cup that passes from Oholibah to the nations is poured out eschatologically on all that opposes God."}
    ],
    "37": [
      {"type": "allusion", "target": "1 Cor 10:20", "note": "They committed adultery, and blood is on their hands; they have committed adultery with their idols and have even offered up their children as food to their idols — Paul draws on the idol-sacrifice connection in 1 Corinthians 10:20 to warn the church: what pagans sacrifice they offer to demons and not to God; I do not want you to be participants with demons; the offering of children to idols in Ezekiel 23 represents the most extreme form of the idolatry that Paul identifies as demonic partnership."}
    ],
    "45": [
      {"type": "allusion", "target": "Rev 18:20", "note": "Righteous men shall judge them with the judgment of adulteresses and with the judgment of women who shed blood — the judicial sentence pronounced on the unfaithful city by righteous men anticipates the heavenly court's verdict in Revelation: Rejoice over her, O heaven, and you saints and apostles and prophets, for God has given judgment for you against her (Rev 18:20); the righteous who execute judgment in Ezekiel's allegory are the saints whose vindication Revelation announces."}
    ]
  },
  "24": {
    "2": [
      {"type": "theme", "target": "Luke 19:44", "note": "Son of man, write down the name of this day, this very day — the LORD commands Ezekiel to record the exact date the king of Babylon began the siege, establishing that YHWH knows and records every moment of historical judgment; Jesus weeps over Jerusalem because they did not recognize the time of their visitation (Luke 19:44), applying the same theological principle: the divine knowledge of the decisive moment is the standard against which human unreadiness is measured."}
    ],
    "6": [
      {"type": "allusion", "target": "Matt 23:35", "note": "Woe to the bloody city, to the pot whose corrosion is in it and whose corrosion has not gone out of it — the blood-stained city whose guilt has been preserved in its very substance echoes Jesus's indictment: upon you may come all the righteous blood shed on earth, from the blood of righteous Abel to the blood of Zechariah (Matt 23:35); the city whose accumulated blood cries out from its stones is the city Jesus mourns and whose judgment he announces."}
    ],
    "13": [
      {"type": "allusion", "target": "Heb 9:13-14", "note": "Your impurity is lewdness; because I would have cleansed you and you were not cleansed, you will not be cleansed from your impurity any more — the divine attempt to cleanse Jerusalem through the Levitical washings and sacrifices that proved insufficient sets up the argument of Hebrews: if the blood of goats and bulls and the sprinkling of defiled persons with the ashes of a heifer sanctify for the purification of the flesh, how much more will the blood of Christ, who through the eternal Spirit offered himself without blemish to God, purify our conscience from dead works (Heb 9:13-14); the uncleanable lewdness of Ezekiel 24 is what the blood of Christ finally addresses."}
    ],
    "16": [
      {"type": "type", "target": "John 11:35", "note": "Son of man, behold, I am about to take the delight of your eyes away from you at a stroke — YHWH's removal of Ezekiel's wife as a sign-act of Jerusalem's coming fall, where the prophet must bear unspeakable personal grief without visible mourning as a sign to the people, anticipates Jesus's grief at Lazarus's tomb: Jesus wept (John 11:35); both the prophet and the Son of God are men of sorrows who enter into the full weight of human death and loss as part of their redemptive mission (Isa 53:3-4)."}
    ],
    "27": [
      {"type": "allusion", "target": "Luke 1:64", "note": "On that day your mouth will be opened to the fugitive, and you shall speak and be no longer mute — Ezekiel's mouth-opening when the promised judgment falls and is confirmed by a fugitive's report is the type of the divine silencing and opening that Zechariah experiences: his mouth was opened and his tongue loosed and he spoke and blessed God (Luke 1:64); in both cases, the opening of the mouth follows the fulfillment of the divine word and becomes the occasion for testimony."}
    ]
  },
  "25": {
    "3": [
      {"type": "theme", "target": "Rev 6:9-11", "note": "Because you said Aha! over my sanctuary when it was profaned, and over the land of Israel when it was made desolate — Ammon's rejoicing over the destruction of YHWH's sanctuary and Israel's dispossession is the form of injustice that the souls under the altar in Revelation cry out against: How long, O Lord, until you judge and avenge our blood on those who dwell on the earth? (Rev 6:10); the divine response to those who rejoice over the suffering of God's people is the thread that runs from Ezekiel's OAN oracles to the eschatological justice of Revelation."},
      {"type": "theme", "target": "Matt 25:40", "note": "Because you said Aha! over my sanctuary and clapped your hands and stamped your feet, rejoicing with all the malice in your heart — the gloating over the fall of God's people is the inverse of what Jesus identifies as treatment of himself: as you did not do it to one of the least of these, you did not do it to me (Matt 25:45); the nations who rejoice in Ammon's fashion over the suffering of YHWH's people are, in the NT's logic, rejoicing over the suffering of Christ."}
    ],
    "12": [
      {"type": "allusion", "target": "Rom 9:13", "note": "Edom acted revengefully against the house of Judah and has grievously offended in taking revenge on them — the ancient enmity of Edom (Esau) against Judah (Jacob) that erupted into active revenge when Jerusalem fell is the historical background for Paul's quotation of Malachi 1:2-3 in Romans 9:13: Jacob I loved but Esau I hated; the persistent hostility of Edom toward Israel in Ezekiel 25 is a late-history chapter in the Esau-Jacob conflict that Paul reads as the pattern of divine election over against human claims."},
      {"type": "allusion", "target": "Obad 1:10", "note": "Edom acted revengefully against the house of Judah — Obadiah 10-15, which is largely contemporaneous with Ezekiel's oracle and covers the same subject (Edom's behavior at Jerusalem's fall), provides the parallel perspective; the two texts together establish the theological-historical background for the NT's use of Edom/Esau as a figure of those who reject the covenant priority even though they shared it by birth."}
    ],
    "14": [
      {"type": "allusion", "target": "Rom 12:19", "note": "I will lay my vengeance upon Edom by the hand of my people Israel — the divine insistence that vengeance against the enemy belongs to YHWH and will be executed by YHWH's agency (not individual retaliation) is the OT ground for Paul's command: Beloved, never avenge yourselves, but leave it to the wrath of God, for it is written, Vengeance is mine, I will repay, says the Lord (Rom 12:19 citing Deut 32:35); the OAN oracles are YHWH's declaration that he will handle what his people are not to handle themselves."}
    ],
    "17": [
      {"type": "allusion", "target": "2 Thess 1:6-8", "note": "I will execute great vengeance on them with wrathful rebukes. Then they will know that I am YHWH, when I lay my vengeance upon them — the vindication of YHWH's people through divine judgment on their oppressors is the OT foundation for Paul's assurance to the persecuted Thessalonian community: God considers it just to repay with affliction those who afflict you... when the Lord Jesus is revealed from heaven with his mighty angels in flaming fire, inflicting vengeance on those who do not know God (2 Thess 1:6-8); the great vengeance of Ezekiel 25 finds its eschatological fulfillment in Christ's return."}
    ]
  }
}

def main():
    existing = load_echo("ezekiel")
    merge_echo(existing, EZEKIEL_ECHOES)
    save_echo("ezekiel", existing)
    print("Ezekiel 23-25 echoes written.")

if __name__ == "__main__":
    main()
