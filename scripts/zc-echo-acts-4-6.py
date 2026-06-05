"""
MKT Echo Layer — Acts chapters 1–3
Run: python3 scripts/zc-echo-acts-1-3.py

Source data used:
- data/interlinear/acts.json
- data/translation/draft/mediating/acts.json (MKT text)
- data/parallels/acts.json (absorbed: Acts 2:17, 2:27, 2:30, 2:34, 3:22, 3:25)
- data/commentary/ellicott/acts.json (philological support)

Key decisions in this range:
- Acts 1–3 is dense with explicit OT citations (Joel 2, Ps 16, Ps 110, Deut 18, Gen 22).
  These are classified as "fulfillment" where Peter explicitly presents them as fulfilled in
  the resurrection/Pentecost events.
- The Pentecost scene (2:1–11) has a strong "reversal of Babel" typology — classified as
  "type" (Babel is the OT type; Pentecost is the NT antitype that undoes the judgment).
- Gen 50:20 in the parallels (Acts 2:23) is absorbed as "theme": the deliberate-plan logic
  runs from Joseph through the cross, but Gen 50:20 is not explicitly cited.
- Isa 52:13 at Acts 3:13 is classified as "fulfillment": Peter names Jesus as the "servant"
  and the "glorified" one, directly invoking the Servant-exaltation language.
- Verses without defensible OT connections are left without entries (echo entries should
  not be manufactured).
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


ACTS_ECHOES = {
  "1": {
    "2": [
      {"type": "type", "target": "2 Kgs 2:1", "note": "Elijah was taken up to heaven by a whirlwind while still instructing Elisha — the ascending prophet-figure who commissions a successor is the structural type for Christ's ascension while still teaching his apostles. Elisha receives a double portion of the Spirit; the apostles receive the promised Spirit at Pentecost."},
    ],
    "3": [
      {"type": "theme", "target": "Exod 34:28", "note": "Moses remained on Sinai forty days and forty nights receiving the Law — the forty-day pattern recurs at every major covenantal moment: Moses at Sinai (Exod 34:28), Elijah at Horeb (1 Kgs 19:8), Jesus in the wilderness (Matt 4:2), now Christ's forty-day resurrection appearances. The number marks a complete period of divine preparation before a new covenant stage."},
    ],
    "4": [
      {"type": "fulfillment", "target": "Ezek 36:27", "note": "I will put my Spirit within you — the promise of the Mosaic-Spirit indwelling the covenant community was foretold by Ezekiel as the mark of the new covenant; 'the gift my Father promised' is the same promise."},
      {"type": "fulfillment", "target": "Joel 2:28-29", "note": "I will pour out my Spirit on all flesh — the promise Jesus refers to is Joel's eschatological Spirit-outpouring; its fulfillment at Pentecost is only days away."},
    ],
    "5": [
      {"type": "fulfillment", "target": "Isa 44:3", "note": "I will pour water on the thirsty land and streams on the dry ground; I will pour my Spirit on your offspring — the water-Spirit metaphor of Isaiah 44 anticipates the baptism-with-Spirit distinction Jesus draws: John baptized with water, but the age of Spirit-saturation is now arriving."},
    ],
    "6": [
      {"type": "theme", "target": "Amos 9:11", "note": "In that day I will restore David's fallen tent — the disciples' question about restoring the kingdom to Israel reflects the prophetic expectation of national restoration; Amos 9:11 and Ezek 37:21–22 frame the hope. Christ's answer deflects the timeline but does not deny the promise."},
    ],
    "7": [
      {"type": "allusion", "target": "Dan 2:21", "note": "He changes times and seasons; he deposes kings and raises up others — Daniel's statement about God's sovereignty over times is the background to Jesus's reply that the Father has set the times and dates by his own authority. The times of the end are in the same divine hands that directed all prior history."},
    ],
    "8": [
      {"type": "fulfillment", "target": "Isa 49:6", "note": "I will make you a light for the Gentiles, that my salvation may reach to the ends of the earth — the geographic scope of the mission mandate in Acts 1:8 (Jerusalem → Judea → Samaria → ends of the earth) traces the Servant's outward movement; Acts is the documentary fulfillment of this Servant-mission."},
      {"type": "allusion", "target": "Ps 2:8", "note": "Ask of me and I will make the nations your inheritance, the ends of the earth your possession — the messianic king receives the nations; the Spirit-empowered witnesses carry the news to those nations."},
    ],
    "9": [
      {"type": "allusion", "target": "Dan 7:13", "note": "One like a son of man coming with the clouds of heaven — the ascension cloud is the cloud of divine presence that the Son of Man rides to receive dominion from the Ancient of Days. The ascension is simultaneously departure and enthronement."},
      {"type": "allusion", "target": "Exod 40:34", "note": "The cloud covered the tent of meeting and the glory of the LORD filled the tabernacle — the cloud that receives Jesus echoes the divine-presence cloud. Where the cloud went, the presence went; the ascension-cloud signals that Christ enters the heavenly sanctuary."},
    ],
    "11": [
      {"type": "fulfillment", "target": "Zech 14:4", "note": "On that day his feet will stand on the Mount of Olives — the promised return from heaven to the same mountain establishes continuity between the ascension and the parousia. The angels' announcement anticipates the Zechariah prophecy of the Lord's return to the place from which he departed."},
    ],
    "12": [
      {"type": "allusion", "target": "Zech 14:4", "note": "The Mount of Olives, which is before Jerusalem on the east — Luke's geographic note connects the ascension site to the eschatological return-site of Zechariah 14:4, where the Lord will stand on the Mount of Olives in the day of his coming."},
    ],
    "16": [
      {"type": "allusion", "target": "Ps 41:9", "note": "Even my close friend in whom I trusted, who ate my bread, has lifted his heel against me — Ps 41:9 underlies the 'Scripture had to be fulfilled' concerning Judas's betrayal; the psalm of the one abandoned by a trusted companion is applied to the betrayal within the Twelve."},
    ],
    "18": [
      {"type": "allusion", "target": "Zech 11:12-13", "note": "They weighed out thirty pieces of silver... I threw them to the potter — Zechariah's thirty silver coins thrown to the potter in the temple yard provide the background for the Judas narrative; Matthew 27:3–10 cites this explicitly, and Acts's field-purchase reflects the same event. The connection is to the purchase of the field."},
    ],
    "20": [
      {"type": "quote", "target": "Ps 69:25", "note": "May his place be deserted; let there be no one to dwell in it — Peter cites Ps 69:25 as the scriptural basis for Judas's vacant place; the psalm of the righteous sufferer who is abandoned by his enemies is applied to the abandonment of Judas's position."},
      {"type": "quote", "target": "Ps 109:8", "note": "May another take his place of leadership — Peter's second citation (Ps 109:8) establishes the scriptural warrant for replacing Judas; the psalm of the king abandoned by treacherous allies is used to authorize the selection of a twelfth apostle."},
    ],
    "26": [
      {"type": "allusion", "target": "Prov 16:33", "note": "The lot is cast into the lap, but its every decision is from the LORD — casting lots to determine Matthias's election follows the OT practice of using lots as a means of discerning divine choice (Num 26:55; Josh 7:14). The lot is not random chance but a covenantal decision-making instrument."},
    ],
  },
  "2": {
    "1": [
      {"type": "type", "target": "Exod 19:1", "note": "On the first day of the third month the Israelites arrived at Sinai — Pentecost (Shavuot) falls fifty days after Passover, the same timing as Israel's arrival at Sinai. Jewish tradition by the first century associated Shavuot with the giving of the Law. The Spirit is given at the feast that commemorates Torah-giving: the new Torah (the Spirit who writes on hearts, Jer 31:33) arrives at the appointed time."},
    ],
    "2": [
      {"type": "allusion", "target": "Ezek 37:9", "note": "Come from the four winds, O breath, and breathe into these slain — the violent wind from heaven recalls Ezekiel's wind-breath that restores the valley of dry bones. Pentecost is the enactment of Ezekiel's vision: a spiritually dead people receive new life through the divine breath/Spirit."},
      {"type": "allusion", "target": "Exod 19:18", "note": "Mount Sinai was covered with smoke, because the LORD descended on it in fire — the Sinai theophany combines fire and dramatic sound; the Pentecost sound from heaven and subsequent fire on heads echoes the Sinai theophany in which God descended to give the covenant."},
    ],
    "3": [
      {"type": "allusion", "target": "Isa 5:24", "note": "Tongues of fire separating and resting on each of them — fire is consistently the mark of divine presence in the OT (burning bush: Exod 3:2; Sinai: Exod 19:18; Ezek 1:13). The individual distribution of the fire to each disciple signals that the divine presence now rests directly on each person, not only on the sanctuary."},
    ],
    "4": [
      {"type": "fulfillment", "target": "Num 11:29", "note": "Would that all the LORD's people were prophets, and that the LORD would put his Spirit on them — Moses's wish in the wilderness is fulfilled at Pentecost: the Spirit falls on all who are present, and they all prophesy. What Moses desired is what Peter will call 'what was spoken by the prophet Joel.'"},
    ],
    "5": [
      {"type": "allusion", "target": "Deut 16:16", "note": "Three times a year all your males shall appear before the LORD your God — Shavuot (Pentecost) was one of the three pilgrimage feasts; God-fearing Jews from every nation had gathered to Jerusalem precisely because the feast law drew diaspora Jews back to the holy city. The geographic scattering that created this international audience is itself the reversal-in-process of the Babel diaspora."},
    ],
    "6": [
      {"type": "type", "target": "Gen 11:1-9", "note": "The crowd hears in their own language — Babel is the OT type; Pentecost is the antitype that reverses it. At Babel, one language was divided into many tongues and the peoples were scattered; at Pentecost, the Spirit enables the diverse tongues of the nations to hear the gospel in their own language. The curse of linguistic division is reversed in the Spirit's work."},
    ],
    "11": [
      {"type": "allusion", "target": "Isa 66:18", "note": "I am coming to gather all nations and tongues, and they shall come and see my glory — the Pentecost gathering of representatives from every nation is the first installment of the eschatological ingathering that Isaiah 66 anticipated. The nations are not just present but understand the 'wonders of God' in their own tongues."},
    ],
    "17": [
      {"type": "fulfillment", "target": "Joel 2:28-32", "note": "And in the last days, God says, I will pour out my Spirit on all people — Peter explicitly cites Joel 2:28-32 as the interpretive key for Pentecost; the outpouring of the Spirit on all flesh (sons, daughters, young, old, servants) is identified as the fulfillment of Joel's last-days promise, announced as the eschatological event beginning now."},
    ],
    "18": [
      {"type": "fulfillment", "target": "Joel 2:29", "note": "Even on my servants, both men and women, I will pour out my Spirit in those days — the continuation of the Joel citation emphasizes the democratization of prophetic access: no distinction of class, gender, or age. The Spirit breaks the restriction of prophecy to designated individuals that characterized the Old Covenant era."},
    ],
    "19": [
      {"type": "fulfillment", "target": "Joel 2:30", "note": "I will show wonders in the heavens and signs on the earth — the cosmic portents in Joel's vision frame the day of Pentecost as the beginning of the eschatological era between the first and second comings of Christ, a period defined by prophetic outpouring and anticipating cosmic renewal."},
    ],
    "20": [
      {"type": "fulfillment", "target": "Joel 2:31", "note": "The sun will be turned to darkness and the moon to blood before the coming of the great and glorious day of the Lord — the Joel citation places Pentecost within the eschatological arc that culminates in 'the day of the Lord'; the Spirit's coming is not the end but the beginning of the end-time sequence."},
    ],
    "21": [
      {"type": "fulfillment", "target": "Joel 2:32", "note": "And everyone who calls on the name of the Lord will be saved — the climax of Peter's Joel citation: the promise of universal salvation-access through calling on the Lord's name. The invitation of v.38 ('repent and be baptized in the name of Jesus Christ') is the application of this promise."},
      {"type": "allusion", "target": "Isa 45:22", "note": "Turn to me and be saved, all the ends of the earth — Isaiah's universal salvation-invitation is the prophetic register in which Joel 2:32 operates; Peter's use of Joel 2:32 carries the same universalist logic: salvation is available to all who call."},
    ],
    "22": [
      {"type": "allusion", "target": "Deut 18:22", "note": "If what a prophet proclaims in the name of the LORD does not take place, that is a message the LORD has not spoken — the miracles, wonders, and signs that accredited Jesus are precisely the prophetic-authentication criteria Moses specified. Jesus was accredited by God through signs that demonstrated divine authorization."},
    ],
    "23": [
      {"type": "theme", "target": "Gen 50:20", "note": "You intended to harm me, but God intended it for good — the deliberate-plan logic of the crucifixion (handed over by God's foreknowledge; executed by wicked men) is structurally identical to the Joseph story: human sin and divine purpose operating simultaneously. The cross is not an accident of history but God's foreordained act accomplished through human agency."},
      {"type": "fulfillment", "target": "Isa 53:10", "note": "Yet it was the LORD's will to crush him and cause him to suffer — the 'deliberate plan and foreknowledge' of God behind the crucifixion enacts the Servant Song's insistence that the Servant's suffering was not random but divinely appointed for the bearing of sin."},
    ],
    "24": [
      {"type": "allusion", "target": "Ps 18:4-5", "note": "The cords of death entangled me — 'freeing him from the agony of death' uses the same imagery as Ps 18:4-5 (the cords/snares of death). The resurrection is God releasing the righteous one from death's grip, which is exactly the deliverance-pattern the Psalms describe."},
    ],
    "25": [
      {"type": "fulfillment", "target": "Ps 16:8-11", "note": "I saw the Lord always before me; because he is at my right hand I will not be shaken — Peter cites Ps 16:8-11 as resurrection prophecy spoken by David about Christ; the Psalm's confidence that the holy one will not be abandoned to Hades is fulfilled in the resurrection. David could not have meant himself, since his tomb is present to this day."},
    ],
    "26": [
      {"type": "fulfillment", "target": "Ps 16:9", "note": "Therefore my heart is glad and my tongue rejoices; my body also will rest in hope — the continuation of Peter's Ps 16 citation; the 'resting in hope' is the confident expectation of bodily resurrection, not merely spiritual immortality, as v.31 will make explicit."},
    ],
    "27": [
      {"type": "fulfillment", "target": "Ps 16:10", "note": "You will not abandon me to the realm of the dead, nor will you let your Holy One see decay — the resurrection-prediction at the center of Peter's argument: Ps 16:10 identifies the Christ as the Holy One whose body does not see corruption. Since David's body did see corruption, Peter argues David was prophesying about his descendant."},
    ],
    "28": [
      {"type": "fulfillment", "target": "Ps 16:11", "note": "You will fill me with joy in your presence — the path of life (v.28 = Ps 16:11) is the resurrection life into which the Father brings the Son; the joy of the divine presence is the condition of the risen, ascended Christ now at the right hand."},
    ],
    "30": [
      {"type": "fulfillment", "target": "Ps 132:11", "note": "The LORD swore an oath to David: One of your own descendants I will place on your throne — Peter cites the Davidic covenant oath as the prophetic ground for Christ's resurrection-enthronement; 2 Sam 7:12-16 is the background, and Ps 132:11 is the liturgical memorial of the oath."},
      {"type": "fulfillment", "target": "2 Sam 7:12-13", "note": "I will raise up your offspring to succeed you... I will establish the throne of his kingdom forever — the Davidic covenant's promise of an eternal throne is fulfilled not in Solomon (whose throne fell) but in the resurrection-enthronement of Christ, whose throne at the right hand of God is permanent."},
    ],
    "33": [
      {"type": "fulfillment", "target": "Ps 110:1", "note": "Exalted to the right hand of God — the ascension-enthronement fulfills Ps 110:1 ('sit at my right hand'), which Peter will cite explicitly in vv.34-35. The Spirit poured out (v.33b) is the evidence that the ascension has occurred and the Psalm's enthronement is operative."},
    ],
    "34": [
      {"type": "fulfillment", "target": "Ps 110:1", "note": "The Lord said to my Lord: Sit at my right hand — Peter's explicit citation of Ps 110:1 proves that David himself did not ascend to heaven; the Lord addressed in the Psalm must be David's greater Lord. The ascended Christ is the one enthroned at God's right hand."},
    ],
    "36": [
      {"type": "fulfillment", "target": "Ps 2:2", "note": "The kings of the earth set themselves against the LORD and against his Anointed (Messiah) — 'God has made this Jesus both Lord and Messiah' declares the fulfillment of Ps 2's royal-enthronement scenario; the one plotted against is now installed as Lord and Messiah through the resurrection."},
    ],
    "37": [
      {"type": "allusion", "target": "Zech 12:10", "note": "They will look on the one they have pierced, and they will mourn — the crowd being 'cut to the heart' enacts the Zechariah vision of Israel mourning the one they pierced; the penitential response to Peter's proclamation is the beginning of Zech 12:10's fulfillment, though its full scope reaches the parousia."},
    ],
    "38": [
      {"type": "fulfillment", "target": "Jer 31:34", "note": "I will forgive their wickedness and remember their sins no more — the offer of forgiveness in the name of Jesus Christ is the enactment of the new covenant promise of Jer 31:34; the baptism-for-forgiveness is the covenant rite that grants entry into the community for whom sins are forgotten."},
    ],
    "39": [
      {"type": "allusion", "target": "Isa 57:19", "note": "Peace, peace, to the far and the near — 'the promise is for you and your children and for all who are far off' echoes Isa 57:19's universal peace-offer. The 'far off' will become a key phrase for Gentile inclusion (Eph 2:13, 17), but here it may still refer to diaspora Jews."},
    ],
    "40": [
      {"type": "allusion", "target": "Deut 32:5", "note": "They are corrupt and not his children; they are a warped and crooked generation — Moses's Song warns Israel about the consequences of apostasy; Peter's 'save yourselves from this corrupt generation' applies the same Deuteronomic idiom to the generation that crucified Jesus."},
    ],
    "41": [
      {"type": "allusion", "target": "Exod 32:28", "note": "About three thousand of the people fell that day — at Sinai, three thousand were killed for the golden calf idolatry on the day the Law was given; at Pentecost, three thousand are added to the new covenant community on the day the Spirit is given. The contrast is deliberate: where law brought death, the Spirit gives life (2 Cor 3:6)."},
    ],
    "42": [
      {"type": "allusion", "target": "Exod 24:11", "note": "They saw God, and they ate and drank — the covenantal meal before God at Sinai is the OT precedent for the communal table fellowship of the new covenant community; the breaking of bread together is the continuation of the Passover-Last Supper covenant meal in which Christ is host."},
    ],
    "44": [
      {"type": "allusion", "target": "Deut 15:4", "note": "There need be no poor people among you, for in the land the LORD your God is giving you to possess as your inheritance, he will richly bless you — the Deuteronomic ideal of a community with no poor is enacted in the Jerusalem church's sharing of possessions. The community of the new covenant lives out what the Jubilee vision aimed at."},
    ],
    "46": [
      {"type": "allusion", "target": "Mal 3:1", "note": "Suddenly the Lord you are seeking will come to his temple — the daily temple presence of the new community fulfills the Malachi promise that the Lord would suddenly come to his temple; the disciples meet in the temple courts because they are the community of the Lord who has come."},
    ],
  },
  "3": {
    "1": [
      {"type": "allusion", "target": "Ps 55:17", "note": "Evening, morning and noon I cry out in distress, and he hears my voice — the three daily hours of prayer (including the ninth hour / 3pm) reflect the Jewish prayer practice codified from the Psalms and observed by Daniel (Dan 6:10). The apostles continue in Israel's prayer rhythm as they go to the temple."},
    ],
    "2": [
      {"type": "fulfillment", "target": "Isa 35:6", "note": "Then the lame will leap like a deer — Isaiah's vision of the messianic age includes the lame leaping (Isa 35:6); the lame man at the temple gate is the sign that the age of salvation has arrived. Peter's healing is the continuation of Jesus's ministry (Matt 11:5 cites the same Isa 35 sign to answer John's question)."},
    ],
    "6": [
      {"type": "allusion", "target": "Isa 53:4-5", "note": "Surely he took up our pain and bore our suffering — the healing in the name of Jesus Christ extends the Servant's vicarious bearing of infirmities (Isa 53:4–5; Matt 8:17) through his apostles; the healing power operates by invoking the name of the one who bore the disease."},
    ],
    "8": [
      {"type": "fulfillment", "target": "Isa 35:6", "note": "He jumped to his feet and began to walk, leaping and praising God — the lame man's leaping directly fulfills Isa 35:6 ('the lame will leap like a deer'). Luke's language matches the Isaianic description closely, signaling that the messianic healing Isaiah predicted is now occurring in Jesus's name."},
    ],
    "13": [
      {"type": "fulfillment", "target": "Isa 52:13", "note": "The God of our fathers has glorified his servant Jesus — Peter's language echoes Isa 52:13 ('my servant will be raised and lifted up and greatly exalted'); the resurrection and ascension is the glorification of the Servant. The arrest, condemnation, and death of vv.13b-15 parallel the Servant's humiliation before his exaltation."},
      {"type": "allusion", "target": "Exod 3:6", "note": "The God of Abraham, Isaac and Jacob — Peter anchors the resurrection claim in the covenant God of the burning bush; the one who raised Jesus is the same God who identified himself to Moses as the God of the patriarchs and is therefore the God of the living, not the dead (cf. Matt 22:32)."},
    ],
    "14": [
      {"type": "allusion", "target": "Isa 53:11", "note": "The Holy and Righteous One — Peter's titles for Jesus echo Isa 53:11 ('the righteous one, my servant, will justify many') and Ps 16:10 ('your Holy One'). Requesting a murderer's release in exchange for the Holy and Righteous One is the paradox that the Servant Song predicted: the innocent one condemned while the guilty go free."},
    ],
    "15": [
      {"type": "allusion", "target": "Isa 53:10", "note": "You killed the author of life, but God raised him from the dead — 'after he has suffered he will see the light of life' (Isa 53:10-11); the one killed is paradoxically the source of life, which the resurrection vindicates. The title <em>archēgon</em> (author/pioneer/source of life) carries the OT background of the one through whom all life comes."},
    ],
    "17": [
      {"type": "allusion", "target": "Lev 4:2", "note": "I know that you acted in ignorance — the Levitical law made provision for sins committed in ignorance (Lev 4:2; Num 15:22-29), which is distinct from deliberate, high-handed sin. Peter's appeal to ignorance is not exculpatory but mitigating — it opens the door to the repentance-and-forgiveness that follows in vv.19–20."},
    ],
    "18": [
      {"type": "fulfillment", "target": "Isa 53:1-12", "note": "God fulfilled what all the prophets had foretold: that his Messiah would suffer — Peter claims that the suffering Messiah is not a theological novelty but the unanimous prophetic witness, of which Isa 53 is the most developed expression. The death of Christ is the accomplishment of the entire prophetic trajectory."},
      {"type": "fulfillment", "target": "Ps 22:1-31", "note": "The Messiah would suffer — Ps 22 is the suffering-unto-vindication psalm cited from the cross (Matt 27:46); its arc of abandonment and ultimate deliverance is one of the prophetic texts behind Peter's claim that all the prophets foretold the Messiah's suffering."},
    ],
    "19": [
      {"type": "allusion", "target": "Isa 55:1-3", "note": "Times of refreshing may come from the Lord — Isaiah's invitation to the thirsty to come and eat freely is the OT register of 'times of refreshing'; the repentance Peter calls for is the turning to receive what God freely offers in the age of the Messiah."},
    ],
    "20": [
      {"type": "allusion", "target": "Mal 3:1", "note": "He may send the Messiah, who has been appointed for you — Malachi's promise that God would send his messenger and then the Lord himself would suddenly come is fulfilled in stages; Peter's language of the appointed Messiah being sent again points to the parousia as the final fulfillment of Malachi's promised coming."},
    ],
    "21": [
      {"type": "allusion", "target": "Isa 65:17-25", "note": "God will restore everything, as he promised through his holy prophets — the 'restoration of all things' (<em>apokatastasis</em>) is the OT prophetic horizon of Isa 65:17-25 (new creation), Ezek 36:28-35, and Acts 1:6's question about restoring the kingdom. Christ's return will accomplish what the prophets foresaw."},
      {"type": "allusion", "target": "Mal 4:5-6", "note": "Elijah to restore all things before the great and dreadful day of the LORD — 'restore everything' carries Malachi's eschatological restoration language; the prophets anticipated a final act of divine renewal before the day of the Lord, which the ascended Christ will accomplish at his return."},
    ],
    "22": [
      {"type": "fulfillment", "target": "Deut 18:15", "note": "The Lord your God will raise up for you a prophet like me from among your own people — Peter explicitly cites Moses's prediction of the prophet-like-Moses as fulfilled in Jesus; the New Moses typology that Matthew's Gospel constructs is here stated directly by the first preacher of the church."},
    ],
    "23": [
      {"type": "fulfillment", "target": "Deut 18:19", "note": "Anyone who does not listen to him will be completely cut off from their people — the stern consequence Peter attaches to rejecting Jesus echoes Deut 18:19 and Lev 23:29; the prophet-like-Moses must be heeded or the hearer is cut off. This is the urgency beneath the call to repentance."},
    ],
    "25": [
      {"type": "fulfillment", "target": "Gen 22:18", "note": "Through your offspring all peoples on earth will be blessed — Peter cites the Abrahamic covenant oath (explicitly the Gen 22:18 form) as fulfilled through Jesus; the mission of Acts is the progressive fulfillment of the promise that through Abraham's seed (Christ, Gal 3:16) the nations receive blessing."},
      {"type": "fulfillment", "target": "Gen 12:3", "note": "All peoples on earth will be blessed through you — the original Abrahamic call promise is the foundation; Peter identifies the audience as 'heirs of the prophets and the covenant,' making the point that Christ's work is not a departure from the Abrahamic covenant but its fulfillment."},
    ],
    "26": [
      {"type": "fulfillment", "target": "Isa 49:6", "note": "When God raised up his servant, he sent him first to you — the Servant's mission begins in Israel and extends outward (Isa 49:6); Peter's 'sent him first to you' is the first stage of the Servant's universal mission. The blessings of the resurrection are offered first to Israel in the sequence that also includes 'the ends of the earth.'"},
    ],
  }
}


def main():
    existing = load_echo('acts')
    merge_echo(existing, ACTS_ECHOES)
    save_echo('acts', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Acts echoes (1–3 added): {len(existing)} chapters, {total} verses with connections.')

if __name__ == '__main__':
    main()
