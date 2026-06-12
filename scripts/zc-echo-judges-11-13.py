"""
Echo Layer — Judges chapters 11–13
Run: python3 scripts/zc-echo-judges-11-13.py

Key connections:
- Ch11: Jephthah = rejected-then-restored deliverer (Joseph/Moses/Christ pattern); Heb 11:32
- Ch11 v34: Jephthah's daughter = beloved only child; Gen 22 / John 3:16 allusion
- Ch12 v6: Shibboleth test = the revealing-speech principle
- Ch12 vv11-12: Elon the Zebulunite = Isa 9:1 territory (Matt 4:13-16)
- Ch13: Barren woman's annunciation = Sarah/Hannah/Elizabeth/Mary type
- Ch13 v17-18: Angel's name pele' = Isa 9:6 "Wonderful Counselor"
- Ch13 v25: Spirit stirs Samson = Joel 2:28/Acts 2:17 pattern
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

JUDGES_ECHOES = {
  "11": {
    "1": [
      {"type": "type", "target": "Gen 37:28", "note": "Jephthah driven out by his brothers echoes Joseph sold by his brothers — the rejected son who later becomes the deliverer of those who rejected him. The pattern recurs with Moses (Acts 7:27-35) and reaches its fulfillment in Christ: 'He came to his own, and his own people did not receive him' (John 1:11)."},
      {"type": "fulfillment", "target": "Heb 11:32", "note": "Jephthah is listed in the Hall of Faith in Heb 11:32 despite his flawed vow — the NT citation affirms that faith, not moral perfection, is the criterion for covenant inclusion."}
    ],
    "2": [
      {"type": "allusion", "target": "Gen 37:8", "note": "The brothers drive out Jephthah to prevent him sharing the inheritance — exactly the motive behind Joseph's brothers selling him into slavery. The inheritance-exclusion of an outsider son is the recurring crisis that God reverses through the rejected deliverer."}
    ],
    "3": [
      {"type": "allusion", "target": "Acts 7:29", "note": "Jephthah flees and gathers 'worthless fellows' around him in Tob — paralleling Moses fleeing to Midian and later leading a mixed multitude. The rejected deliverer in exile gathering followers precedes the restoration and commission that follows."}
    ],
    "7": [
      {"type": "allusion", "target": "Acts 7:35", "note": "'Did you not hate me and drive me out?' — Jephthah's confrontation of his rejectors echoes Moses: 'This Moses, whom they had rejected with the words, \'Who made you a ruler and judge?\' is the very one God sent to be their ruler and deliverer' (Acts 7:35). The community that rejected the deliverer is forced to appeal to him for rescue."}
    ],
    "11": [
      {"type": "allusion", "target": "Phil 2:9", "note": "The elders who drove Jephthah out now make him 'head and commander over all the inhabitants of Gilead' — the exalted-after-humiliation pattern that Paul applies to Christ: 'Therefore God exalted him to the highest place and gave him the name that is above every name' (Phil 2:9)."}
    ],
    "27": [
      {"type": "allusion", "target": "Rev 19:11", "note": "'The LORD, the Judge, decide today between the people of Israel and the people of Ammon' — the appeal to YHWH as the just judge who adjudicates between peoples prefigures the eschatological judge: 'With justice he judges and wages war' (Rev 19:11). Jephthah's appeal to divine judgment anticipates the final resolution of all conflicts by the divine warrior-judge."}
    ],
    "29": [
      {"type": "allusion", "target": "Acts 2:17", "note": "The Spirit of the LORD came upon Jephthah — the pattern of the Spirit empowering the deliverer for battle. This prophetic Spirit-empowerment (also on Gideon, Samson, Saul, David) points toward the permanent indwelling of the Spirit promised through Joel 2:28-29 and fulfilled at Pentecost: 'In the last days I will pour out my Spirit on all people' (Acts 2:17)."}
    ],
    "30": [
      {"type": "allusion", "target": "Gen 28:20", "note": "Jephthah's conditional vow — 'If you give the Ammonites into my hand, then...' — follows the genre of the conditional vow, first modeled by Jacob at Bethel (Gen 28:20-22). The vow genre reveals both faith (trusting YHWH for the outcome) and the peril of bargaining with YHWH whose gifts are unconditional."}
    ],
    "32": [
      {"type": "fulfillment", "target": "Heb 11:32", "note": "Jephthah crossed over and 'the LORD gave them into his hand' — the victory is YHWH's gift, not the product of the vow. Heb 11:32 cites Jephthah's defeat of the Ammonites as an act of faith, locating the source of victory in trust rather than in the conditional transaction of the vow."}
    ],
    "34": [
      {"type": "allusion", "target": "Gen 22:2", "note": "Jephthah's daughter — his only child — comes out to meet him after the victory, and he has vowed to sacrifice the first to greet him. The only-beloved-child-offered-because-of-a-vow pattern echoes the Akedah: 'Take your son, your only son, whom you love' (Gen 22:2). The difference is decisive: Abraham's ram-substitute prevents Isaac's death; no substitute appears for Jephthah's daughter."}
    ],
    "35": [
      {"type": "allusion", "target": "John 3:16", "note": "'You have become the cause of my ruin' — Jephthah's anguish over his only daughter is a shadow of the Father giving his only Son. The tragic irony that the deliverer's own victory leads to the sacrifice of his beloved child gestures toward the divine logic of redemption: the victory that saves others costs the deliverer his most precious possession."}
    ],
    "36": [
      {"type": "allusion", "target": "Heb 5:8", "note": "The daughter's response — 'Do to me according to what has gone out of your mouth' — echoes Isaac's willing compliance in Gen 22:7-9 and Christ's Gethsemane submission: 'Yet not my will, but yours' (Luke 22:42). The beloved child who submits to the father's vow without resentment is a recurring type of the one who 'learned obedience from what he suffered' (Heb 5:8)."}
    ],
    "39": [
      {"type": "allusion", "target": "Heb 11:32", "note": "Jephthah fulfilled his vow; his daughter 'had never known a man.' The annual four-day lament by the daughters of Israel (v40) memorialized a sacrifice that achieved covenant faithfulness at immense cost. Heb 11:32 includes Jephthah among those who 'through faith conquered kingdoms' — the victory that came through loss is the pattern of faith."}
    ],
    "40": [
      {"type": "allusion", "target": "Zech 12:10", "note": "The daughters of Israel went year by year to lament Jephthah's daughter — an institutionalized annual mourning for an only daughter whose death was connected to covenant victory. This sustained communal mourning for an only child who died has a distant echo in Zech 12:10: 'They will mourn for him as one mourns for an only child, and grieve bitterly for him as one grieves for a firstborn son.'"}
    ]
  },
  "12": {
    "1": [
      {"type": "allusion", "target": "Luke 15:29", "note": "The Ephraimites demand to know why they were not called to share in the victory they did not earn — the elder-brother complaint. 'I've been here all along, and you never gave me...' (Luke 15:29). The sense of entitlement to participation in another's achievement is the recurring failure of those who mistake proximity for faithfulness."}
    ],
    "4": [
      {"type": "allusion", "target": "1 Cor 3:3", "note": "The intertribal civil war that follows the victory over Ammon — Gilead vs. Ephraim — illustrates Paul's warning: 'You are still worldly. For since there is jealousy and quarreling among you, are you not worldly?' (1 Cor 3:3). The tragedy of Israel is that external victories are followed by internal divisions driven by pride and wounded honor."}
    ],
    "6": [
      {"type": "allusion", "target": "Matt 12:37", "note": "The Shibboleth/Sibboleth test — betrayed by dialect — reveals the principle that speech discloses identity: 'For by your words you will be acquitted, and by your words you will be condemned' (Matt 12:37). The Gileadites use a spoken test to distinguish insider from outsider; the NT principle extends this to the words that reveal what the heart is full of (Matt 12:34)."}
    ],
    "7": [
      {"type": "theme", "target": "Heb 11:32", "note": "Jephthah judged Israel six years and died — a brief notice that closes a turbulent story. His inclusion in Heb 11:32 (alongside Gideon, Barak, and Samson) despite the tragedy of his vow confirms the NT principle: 'By faith... they conquered kingdoms, administered justice, and gained what was promised' (Heb 11:33). Faith, not flawlessness, is the criterion."}
    ],
    "11": [
      {"type": "allusion", "target": "Matt 4:15", "note": "Elon the Zebulunite judges Israel — the minor judge from the tribe of Zebulun. Isa 9:1 names Zebulun as the region where the great light would shine (quoted in Matt 4:15-16 as fulfilled in Jesus beginning his ministry in Galilee). The judge from Zebulun keeps the covenant community alive in the territory that will become the theater of the Messiah's ministry."}
    ],
    "14": [
      {"type": "allusion", "target": "Judg 5:10", "note": "Abdon's forty sons and thirty grandsons 'rode on seventy donkeys' — the donkey-riding detail for a judge echoes the celebration of riding 'on white donkeys' in Deborah's song (Judg 5:10), which celebrated peace and prosperity under righteous leadership. The donkey later becomes the vehicle of Christ's royal entry (Matt 21:5, citing Zech 9:9)."}
    ]
  },
  "13": {
    "2": [
      {"type": "type", "target": "Gen 18:1", "note": "A barren woman visited by a divine messenger who announces a miraculous conception — the third annunciation in Judges (cf. also Samson in the larger pattern). This type runs from Sarah (Gen 18:1-15) through Hannah (1 Sam 1) to Elizabeth and Mary (Luke 1:5-38). Each barren woman represents the human impossibility that YHWH overrides to produce his covenant deliverer."}
    ],
    "3": [
      {"type": "type", "target": "Luke 1:31", "note": "The angel's announcement — 'you are barren and have not borne a child, but you shall conceive and bear a son' — follows the annunciation formula that reaches its fullest expression in Luke 1:31: 'You will conceive and give birth to a son, and you are to call him Jesus.' The parallel is structural: barren/unexpected woman + divine messenger + 'you shall conceive and bear a son' + instructions about the child."},
      {"type": "allusion", "target": "Isa 54:1", "note": "The barren woman who will unexpectedly bear a son fulfills the Isaianic promise: 'Sing, barren woman, you who never bore a child; burst into song, shout for joy' (Isa 54:1). Paul applies this verse to the new covenant in Gal 4:27, making the barren-woman-who-bears type a figure for the Gentile church."}
    ],
    "5": [
      {"type": "type", "target": "Luke 1:15", "note": "The Nazirite consecration from the womb — no razor, no wine, set apart to God from before birth — prefigures John the Baptist: 'He is never to take wine or strong drink, and he will be filled with the Holy Spirit even before he is born' (Luke 1:15). Both Samson and John are Nazirite-type figures consecrated from the womb who prepare the way for a greater deliverer."},
      {"type": "allusion", "target": "Num 6:2", "note": "The Nazirite vow requirements (Num 6:2-8) — abstinence from wine, uncut hair, avoidance of the dead — are imposed on Samson from before birth, not by personal choice. The vow marks complete consecration to YHWH's service. Samson's eventual violations of each element (wine at the feast, hair cut by Delilah, contact with corpses) trace the pattern of compromised consecration."}
    ],
    "6": [
      {"type": "allusion", "target": "Dan 10:6", "note": "The woman describes the angel's appearance as 'like the appearance of the angel of God — very awesome.' The language of awesome divine appearance echoes the theophanic descriptions in Daniel 10:6 and Revelation 1:13-16. The same awed, speechless response to overwhelming divine glory characterizes encounters with the angel of the LORD throughout the OT."}
    ],
    "8": [
      {"type": "allusion", "target": "Luke 1:38", "note": "Manoah prays for the divine messenger to return and teach them what to do — a model of seeking divine guidance before undertaking a sacred task. The desire to hear more from the divine messenger before acting reflects the posture of Mary: 'How will this be?' (Luke 1:34). Both parents of covenant deliverers seek clarification before receiving the gift."}
    ],
    "17": [
      {"type": "allusion", "target": "Isa 9:6", "note": "Manoah asks the angel's name. The angel's response — 'Why do you ask my name? It is <em>pele'</em> (beyond understanding / wonderful)' — uses the Hebrew word <em>pele'</em>, the same root as the first element of the Messiah's name in Isa 9:6: 'His name will be called <em>Pele'-yoʿēṣ</em> (Wonderful Counselor).' The angel at Samson's birth carries the divine name-quality that Isaiah assigns to the coming Messiah."}
    ],
    "18": [
      {"type": "allusion", "target": "Gen 32:29", "note": "The refusal to reveal the divine name — 'Why do you ask my name?' — echoes the angel at Peniel who also refuses to give his name when Jacob asks (Gen 32:29). The concealed name at transformative encounters with divine messengers signals the mystery of the divine identity that will be fully revealed only in Christ: 'No one knows the Son except the Father' (Matt 11:27)."}
    ],
    "19": [
      {"type": "type", "target": "Judg 6:21", "note": "The angel works a wonder (<em>maphliʾ</em>, doing wondrously) as the offering is consumed — the same pattern as Gideon's theophany in Judg 6:21, where the angel touches the offering and fire consumes it before the angel disappears. The theophany-at-sacrifice pattern reveals YHWH accepting the offering and vindicating the worshipper before departing — the pattern fulfilled in Christ's once-for-all self-offering."}
    ],
    "20": [
      {"type": "type", "target": "Rev 10:1", "note": "The angel of the LORD ascended in the flame of the altar — the divine presence ascending in fire echoes the column of fire by night (Exod 13:21) and points forward to the glorified Christ: 'his face was like the sun shining in all its brilliance' (Rev 1:16). Fire, glory, and divine ascent are consistently associated with YHWH's presence throughout the OT."}
    ],
    "21": [
      {"type": "allusion", "target": "Luke 24:31", "note": "The angel did not appear again after the theophany — the divine messenger who announced the birth withdraws after the revelation is complete. The pattern of divine appearance-then-withdrawal after a definitive revelation echoes the resurrection appearances: 'their eyes were opened and they recognized him, and he disappeared from their sight' (Luke 24:31)."}
    ],
    "22": [
      {"type": "allusion", "target": "Isa 6:5", "note": "'We are certainly going to die, for we have seen God.' The terror of the divine encounter — the conviction that seeing YHWH means death — is the consistent human response to theophany: Isaiah ('I am a man of unclean lips,' Isa 6:5), Ezekiel (Ezek 1:28), John (Rev 1:17: 'I fell at his feet as though dead'). The creature's instinctive recognition that direct divine encounter should be lethal sets up the grace by which it is survived."}
    ],
    "23": [
      {"type": "allusion", "target": "1 John 4:18", "note": "Manoah's wife reasons from the acceptance of the offering to the assurance of their survival: if YHWH had wanted to kill them, he would not have accepted their offering. This is covenant reasoning from YHWH's past gracious acts to present security — the same logic as 'if God is for us, who can be against us?' (Rom 8:31) and 'there is no fear in love; but perfect love drives out fear' (1 John 4:18)."}
    ],
    "24": [
      {"type": "allusion", "target": "Luke 2:52", "note": "'The woman bore a son and named him Samson. The child grew, and the LORD blessed him.' The brief notice of the miraculous birth, the naming, the growth, and divine blessing precisely parallels the childhood summary for Christ: 'Jesus grew in wisdom and stature, and in favor with God and man' (Luke 2:52) and John the Baptist: 'the child grew and became strong in spirit' (Luke 1:80). The covenant deliverer's blessed growth is a standard formula that frames every new deliverer's beginning."}
    ],
    "25": [
      {"type": "allusion", "target": "Acts 2:17", "note": "The Spirit of the LORD began to stir Samson — the first movements of the empowering Spirit in the consecrated deliverer. The Judges cycle of Spirit-empowerment for deliverance (Othniel 3:10, Gideon 6:34, Jephthah 11:29, Samson 13:25) points toward the permanent, universal Spirit-outpouring promised in Joel 2:28-29 and fulfilled at Pentecost (Acts 2:17-18): from intermittent charismatic empowerment of individual leaders to permanent indwelling of the whole community."}
    ]
  }
}

def main():
    existing = load_echo('judges')
    merge_echo(existing, JUDGES_ECHOES)
    save_echo('judges', existing)
    print('Judges 11-13 echoes written.')

if __name__ == '__main__':
    main()
