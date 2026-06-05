"""
Echo Commentary — Hebrews chapters 10–11
Run: python3 scripts/zc-echo-hebrews-10-11.py

Key decisions:
- Ch10: Ps 40:6-8 citation = fulfillment (text applied to Christ explicitly); Jer 31 re-cited
- Ch10: Hab 2:3-4 = allusion/fulfillment; Deut 32:35-36 judgment = quote
- Ch11: Faith Hall of Fame — individual figures: each is shadow/type; Gen, Exod narratives are types
- Abel (11:4): shadow; Noah (11:7): shadow; Abraham (11:8-19): type; Moses (11:24-28): shadow
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

HEBREWS = {
  "10": {
    "1": [
      {"type": "shadow", "target": "Lev 16:1–34", "note": "The annual Day of Atonement that the law provides is the repeated-sacrifice shadow that Hebrews 10:1 identifies as never able to make perfect those who draw near. The very repetition of the annual ritual is the typological signal of its inadequacy — a perfecting sacrifice would not need repeating."}
    ],
    "5": [
      {"type": "fulfillment", "target": "Ps 40:6–8", "note": "\"Sacrifice and offering you did not desire, but a body you have prepared for me... I said, 'Behold, I have come to do your will, O God'\" — Hebrews 10:5-7 cites Ps 40:6-8 LXX (which reads 'a body you have prepared for me' where MT has 'ears you have dug/opened for me') as the Son's words at his incarnation. The psalm's declaration that God does not want sacrifice but the obedient will of the worshiper becomes the Son's announcement that his body-offering fulfills what the animal sacrifices could not."}
    ],
    "9": [
      {"type": "fulfillment", "target": "Ps 40:7–8", "note": "\"Then I said, 'Behold, I have come to do your will, O God, as it is written of me in the scroll of the book'\" — Hebrews 10:9 draws out the implication: Christ 'does away with the first [sacrifice] in order to establish the second [will-doing].' The will-doing that replaces sacrifice is the eschatological fulfillment of the entire sacrificial system's purpose — obedient offering of the self."}
    ],
    "10": [
      {"type": "fulfillment", "target": "Lev 16:15–16", "note": "The once-for-all offering of Christ ('by that will we have been sanctified through the offering of the body of Jesus Christ once for all') fulfills and abolishes the annual repetition of the Day of Atonement. The Levitical once-per-year becomes the Christological once-for-all."}
    ],
    "12": [
      {"type": "fulfillment", "target": "Ps 110:1", "note": "\"Sit at my right hand\" — Hebrews 10:12-13 returns to Ps 110:1 as the description of Christ's posture after his single offering: 'sat down at the right hand of God, waiting from that time until his enemies should be made a footstool for his feet.' The seated high priest contrasts with the Levitical priests who always stood (10:11, never sat) — there was always more work to do; Christ's session indicates completed atonement."}
    ],
    "16": [
      {"type": "fulfillment", "target": "Jer 31:33", "note": "\"This is the covenant that I will make with them after those days, declares the LORD: I will put my laws on their hearts, and write them on their minds\" — Hebrews 10:16-17 cites Jer 31:33-34 again (already quoted in full at 8:8-12) to apply the new covenant's specific promises to the community's present experience: the internal law and complete forgiveness are the benefits of Christ's completed sacrifice."}
    ],
    "17": [
      {"type": "fulfillment", "target": "Jer 31:34", "note": "\"I will remember their sins and their lawless deeds no more\" — the forgiveness-portion of the Jeremiah 31 citation (Heb 10:17) is the logical consequence drawn in 10:18: 'where there is forgiveness of these, there is no longer any offering for sin.' Complete divine forgetting of sin makes further sacrifice meaningless."}
    ],
    "19": [
      {"type": "fulfillment", "target": "Lev 16:2", "note": "The curtain that separated the Most Holy Place from access — torn at the crucifixion (Matt 27:51) — is the type whose fulfillment Hebrews 10:19-20 describes: believers now have confidence to enter the holy places 'by the blood of Jesus, by the new and living way that he opened for us through the curtain, that is, through his flesh.' The curtain is his flesh; the tearing is his death; the opened way is the resurrection-access to the Father."}
    ],
    "20": [
      {"type": "shadow", "target": "Exod 26:31–33", "note": "\"You shall make a veil of blue and purple and scarlet yarns... it shall separate for you the Holy Place from the Most Holy\" — the woven veil that separated the two rooms of the sanctuary is the shadow of which Christ's flesh is the reality (Heb 10:20). The tearing of the sanctuary veil at the crucifixion (Matt 27:51) enacted the typological fulfillment — Christ's death opening the way into God's presence."}
    ],
    "28": [
      {"type": "quote", "target": "Deut 17:6", "note": "\"Only on the evidence of two witnesses or of three witnesses shall a charge be established\" — Hebrews 10:28 cites the two-or-three-witness principle of Deut 17:6 (used for capital cases in Israel) to frame the comparison: if violation of Moses's law brought death without mercy on two-or-three witnesses, how much worse will be the punishment for trampling the Son of God."}
    ],
    "30": [
      {"type": "quote", "target": "Deut 32:35–36", "note": "\"Vengeance is mine; I will repay\" and \"The LORD will judge his people\" — Hebrews 10:30 cites Deut 32:35-36 (the Song of Moses) to ground the warning against deliberate sin. The divine vengeance promised in the Song of Moses belongs to the judge of all — a terrifying prospect for those who have insulted the Spirit of grace."}
    ],
    "38": [
      {"type": "fulfillment", "target": "Hab 2:3–4", "note": "\"For still the vision awaits its appointed time... the righteous shall live by his faith\" — Hebrews 10:37-38 cites Hab 2:3-4 LXX (with modifications: 'he who is coming will come... my righteous one shall live by faith') as the scriptural statement of the faith-endurance principle that governs the community's posture in waiting for the eschatological fulfillment. The Habakkuk text introduces the faith-definition and examples of chapter 11."}
    ]
  },
  "11": {
    "1": [
      {"type": "theme", "target": "Hab 2:4", "note": "\"The righteous shall live by his faith\" — Hebrews 11:1's definition of faith ('the assurance of things hoped for, the conviction of things not seen') is the direct elaboration of the Habakkuk citation that closed chapter 10. The faith-as-substance-of-hope definition explains what the living-by-faith of the remnant in Habakkuk requires."}
    ],
    "4": [
      {"type": "shadow", "target": "Gen 4:1–10", "note": "Abel's acceptable offering — faith-motivated, received by God — contrasts with Cain's rejected offering. Hebrews 11:4 reads Abel as the first OT exemplar of faith: he offered 'by faith' (not merely by external compliance). Abel's blood cried out (Gen 4:10; Heb 12:24) — the murdered witness whose faith-testimony continues even after death."}
    ],
    "5": [
      {"type": "shadow", "target": "Gen 5:22–24", "note": "\"Enoch walked with God, and he was not, for God took him\" — Hebrews 11:5 reads Enoch's translation (taken without dying) as the reward of faith: he pleased God, and God's response was to receive him before death. The Genesis narrative's brief account becomes a testimony to the possibility of pleasing God by faith."}
    ],
    "7": [
      {"type": "shadow", "target": "Gen 6:9–22", "note": "Noah's construction of the ark — 'in reverent fear' about things not yet seen — is the OT paradigm for faith that acts on divine warning about an unseen future event. Noah condemned the world and became heir of the righteousness of faith: the builder who believed God's word about the flood before there was any flood exemplifies Heb 11:1's faith definition."}
    ],
    "8": [
      {"type": "shadow", "target": "Gen 12:1–4", "note": "\"Go from your country and your kindred and your father's house to the land that I will show you\" — Abraham's obedient departure for an unknown destination is the paradigmatic act of faith. Hebrews 11:8 notes that he 'went out, not knowing where he was going' — the faith that acts without seeing the destination is the structural pattern for the community's own pilgrimage."}
    ],
    "10": [
      {"type": "shadow", "target": "Gen 15:1–21", "note": "Abraham's sojourn in Canaan as a tent-dweller — a stranger in the land of promise — is read by Hebrews 11:10 as evidence that he was looking for something beyond: 'the city that has foundations, whose designer and builder is God.' The tent-dwelling patriarch is not simply waiting for permanent settlement in Canaan but for the eschatological city."}
    ],
    "11": [
      {"type": "shadow", "target": "Gen 17:15–21; 18:9–15", "note": "Sarah's faith to conceive despite her age — 'she considered him faithful who had promised' — is the other side of the Abraham-faith account. The barren woman who conceives by divine promise embodies faith in the God who gives life to the dead and calls into existence things that do not exist (Rom 4:17 — the same pattern)."}
    ],
    "17": [
      {"type": "type", "target": "Gen 22:1–18", "note": "The Aqedah — Abraham's binding of Isaac in obedience to God's command — is the supreme OT type of faith tested to the uttermost. Hebrews 11:17-19 reads the Aqedah as Abraham's implicit belief in resurrection: he offered the one through whom the promise would come, 'figuring that God was able even to raise him from the dead, from which, figuratively speaking, he did receive him back.' Isaac received back = type of resurrection."}
    ],
    "20": [
      {"type": "shadow", "target": "Gen 27:27–40", "note": "Isaac's blessing of Jacob and Esau 'by faith... regarding things to come' — treating the as-yet-unrealized blessings as certain. The patriarch who speaks blessing over future generations embodies the faith that treats unseen future realities as present."}
    ],
    "21": [
      {"type": "shadow", "target": "Gen 48:1–22", "note": "Jacob's blessing of Joseph's sons while leaning on his staff — worshiping as he blesses, aware of his own death — is the faith that acts under death's shadow while maintaining confidence in God's future. The dying patriarch who blesses and worships exemplifies faith as confidence in God's commitment beyond the believer's own life-span."}
    ],
    "22": [
      {"type": "shadow", "target": "Gen 50:24–25", "note": "Joseph's command about his bones — 'he made mention of the exodus of the Israelites and gave directions concerning his burial' — is faith in the Exodus promise before the Exodus occurred. The dying Joseph speaks of a departure from Egypt as certain, commanding that his bones be carried out: faith treats God's promises as already-accomplished facts."}
    ],
    "23": [
      {"type": "shadow", "target": "Exod 2:1–2", "note": "Moses's parents hiding him for three months 'because they saw the child was beautiful, and they were not afraid of the king's edict' — their faith overrode the royal command. The text notes their seeing that he was 'beautiful' (Exod 2:2 — 'she saw that he was a goodly child'); Hebrews reads their action as faith-motivated resistance to the lethal royal decree."}
    ],
    "24": [
      {"type": "shadow", "target": "Exod 2:11–15", "note": "Moses's refusal of Egyptian identity — 'when he was grown up, he refused to be called the son of Pharaoh's daughter, choosing rather to be mistreated with the people of God than to enjoy the fleeting pleasures of sin' — is read as faith-motivated choice. The Genesis-to-Exodus transition in Moses is the OT pattern for faith as voluntary embrace of suffering identification over comfortable status."}
    ],
    "26": [
      {"type": "shadow", "target": "Ps 89:50–51", "note": "\"Remember, O Lord, how your servants are mocked... how your enemies mock, O LORD, how they mock the footsteps of your anointed\" — the reproach of the Messiah that Moses bore ('the reproach of Christ') is grounded in the Psalter's pattern of those who share in the anointed one's suffering-honor. Moses's Egyptian reproach is read as participation in the messianic reproach."}
    ],
    "28": [
      {"type": "shadow", "target": "Exod 12:1–30", "note": "Moses's keeping of the Passover 'by faith' — not seeing the destroyer's threat directly but trusting God's word about the blood-sign — is the paradigmatic act of Passover faith. The destroyer passing over the blood-marked houses is the event that Moses trusted before it occurred; the Passover lamb becomes the NT type for Christ (1 Cor 5:7)."}
    ],
    "29": [
      {"type": "shadow", "target": "Exod 14:21–31", "note": "The crossing of the Red Sea 'by faith' — Israel passing through what the Egyptians attempted and drowned in — is the OT pattern of faith in divine deliverance through impossible terrain. The sea-crossing marks the transition from slavery to pilgrimage; Paul reads it as baptismal in 1 Cor 10:1-2."}
    ],
    "30": [
      {"type": "shadow", "target": "Josh 6:1–20", "note": "The walls of Jericho falling after Israel circled them for seven days 'by faith' — not by military assault but by obedient ritual action — is the OT pattern of faith that accomplishes what human force cannot. The Jericho pattern (obedient action without visible mechanism of effectiveness) exemplifies faith as acting on divine instruction without visible causality."}
    ],
    "31": [
      {"type": "shadow", "target": "Josh 2:1–21", "note": "Rahab the prostitute not perishing with the disobedient because she had given friendly welcome to the spies — her faith-act of receiving the spies and her scarlet cord are the paradigm of faith across ethnic-religious boundary. The Gentile prostitute who hides the Israelite scouts is saved while Jericho perishes: faith transcends ethnic and moral categorization."}
    ],
    "35": [
      {"type": "shadow", "target": "1 Kgs 17:17–24; 2 Kgs 4:18–37", "note": "Women receiving back their dead by resurrection — Elijah raising the Zarephath widow's son (1 Kgs 17:21-22) and Elisha raising the Shunammite's son (2 Kgs 4:34-35) — are the OT examples behind Heb 11:35a. These miraculous restorations are the OT shadow of the resurrection that Heb 11:35b contrasts with the martyrs who refused release: those who died for a better resurrection."},
      {"type": "shadow", "target": "2 Macc 7:1–41", "note": "The Maccabean martyrs who refused release so that they might 'rise again to a better life' (2 Macc 7:14) are the background for Heb 11:35b's 'tortured, refusing to accept release, so that they might rise again to a better life.' The Maccabean period's martyrdom-for-resurrection hope is the OT/Second Temple background for the martyrs' faith."}
    ],
    "37": [
      {"type": "shadow", "target": "1 Kgs 19:10", "note": "\"I, even I only, am left, and they seek my life\" — the prophetic martyrdom tradition (Elijah fleeing; the hidden 7,000; Jeremiah's imprisonment; Isaiah's tradition of being sawn in two) is the OT background for Heb 11:37's list of prophetic sufferings: stoned, sawn in two, killed with the sword, wandering in deserts and mountains."}
    ],
    "39": [
      {"type": "theme", "target": "Gen 49:10", "note": "\"The scepter shall not depart from Judah... until tribute comes to him; and to him shall be the obedience of the peoples\" — the OT cloud of witnesses looked forward to a fulfillment they did not receive apart from the new covenant community. The eschatological 'something better' (Heb 11:40) that God provided for the community is what all the OT figures were waiting for — without which they would not be made perfect."}
    ]
  }
}

def main():
    existing = load_echo('hebrews')
    merge_echo(existing, HEBREWS)
    save_echo('hebrews', existing)
    total = sum(len(vlist) for ch in existing.values() for vlist in ch.values())
    print(f'Hebrews echoes: {len(existing)} chapters, {total} total connections.')

if __name__ == '__main__':
    main()
