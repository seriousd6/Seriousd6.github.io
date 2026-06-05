"""
MKT Echo Layer — Romans chapters 11–14
Run: python3 scripts/zc-echo-romans-11-14.py

Source data used:
- data/translation/draft/mediating/romans.json (MKT text for ch11-14)
- data/parallels/romans.json (absorbed: 11:3 1 Kgs 19:10; 11:4 1 Kgs 19:18;
  11:8 Isa 29:10; 11:9-10 Ps 69:22-23; 11:26 Isa 59:20-21; 11:34 Isa 40:13;
  12:19 Deut 32:35; 12:20 Prov 25:21-22; 13:9 Exod 20:13-17;
  14:11 Isa 45:23)

Key decisions in this range:
- 11:8 Isa 29:10 — Paul's composite quote includes Deut 29:4 (spirit of stupor)
  and Isa 29:10 (eyes shut, ears closed); classified as quote for both sources
- 11:26 "all Israel will be saved" — Isa 59:20-21 is the backing prophecy;
  also alludes to Isa 27:9 (when I take away their sin) for v27
- 11:33-36 doxology — draws on Isa 40:13, Job 41:11, Ps 36:9; each classified
  as the appropriate type (quote for 11:34 since Paul cites it explicitly;
  allusion for Job 41:11 since the wording is close but not exact)
- 12:14 "bless those who persecute you" — the reversal of the OT curse tradition
  is itself the echo: contrast with Ps 109:28, fulfillment of Prov 25:21-22
- 13:1-7 governing authorities — OT background in Prov 8:15-16 (kings rule through Wisdom),
  Dan 2:21 (God changes times and seasons, sets up and deposes kings)
- 14:11 Isa 45:23 — Paul uses this for universal divine judgment; applies the Isaianic
  every-knee-bows to the future divine judgment seat (in Phil 2:10 Paul applies the same
  text to Christ's exaltation); classified as quote (absorbed from parallels)
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

ROMANS_ECHOES = {
  "11": {
    "1": [
      {"type": "theme", "target": "1 Sam 12:22", "note": "Samuel declares that the LORD will not reject his people for the sake of his great name — Paul's 'Did God reject his people? By no means!' stands in the tradition of the OT assurance that divine rejection of the covenant people is incompatible with God's own faithfulness to his name; Paul's own Israelite identity is an argument from lived experience."},
      {"type": "allusion", "target": "Ps 94:14", "note": "The LORD will not reject his people; he will never forsake his inheritance — the psalm's assurance against divine abandonment is the OT counterpart to Paul's argument that apparent Israel-rejection is partial and temporary, not the total abandonment that Ps 94:14 denies."}
    ],
    "2": [
      {"type": "allusion", "target": "1 Kgs 19:10", "note": "Elijah's complaint begins the Elijah-remnant section Paul introduces in v3 — the verse anticipates the Elijah passage Paul will cite; God did not reject his people is the answer to Elijah's despair, confirmed by the 7,000 reserved of v4."}
    ],
    "3": [
      {"type": "quote", "target": "1 Kgs 19:10", "note": "Elijah's complaint — they have killed your prophets and torn down your altars; I am the only one left — is cited to frame the present situation of Israel: as in Elijah's day, apparent near-total apostasy conceals a hidden remnant; Paul reads the Elijah moment as a type of the present condition of Jewish unbelief."}
    ],
    "4": [
      {"type": "quote", "target": "1 Kgs 19:18", "note": "God's answer to Elijah — I have reserved for myself seven thousand who have not bowed the knee to Baal — establishes the remnant-principle that Paul applies to the present: God's sovereign reservation of a remnant operates invisibly, preventing the prophet (or apostle) from seeing the full picture of divine faithfulness."}
    ],
    "5": [
      {"type": "allusion", "target": "Isa 10:20-22", "note": "The remnant of Israel will no longer rely on what struck them but will lean on the LORD in truth — Isaiah's remnant theology (which Paul has already cited in 9:27-28) continues here: the remnant chosen by grace is the Isaianic remnant that leans on God rather than human achievement, now defined by grace rather than ethnic selection."}
    ],
    "6": [
      {"type": "theme", "target": "Deut 7:6-8", "note": "God chose Israel not because of their numbers or merit but because he loved them and kept his oath — the Deuteronomic grounding of election in grace rather than merit is the OT basis for Paul's insistence that if the remnant is by grace, works cannot be the criterion; the Deuteronomic love-choice already excluded merit as the basis of divine selection."}
    ],
    "7": [
      {"type": "allusion", "target": "Isa 6:9-10", "note": "God telling Isaiah to make the people's heart calloused, their ears dull, their eyes closed — the hardening of the majority of Israel that Paul describes in the elect versus the rest is anticipated in Isaiah's own commission, where he was told the effect of his preaching would be hardening rather than repentance."}
    ],
    "8": [
      {"type": "quote", "target": "Isa 29:10", "note": "God brought on Israel a deep sleep, closing their eyes and covering their heads — Paul combines Deut 29:4 (God has not given them a heart to perceive or eyes to see or ears to hear) and Isa 29:10 into a single oracle of judicial hardening; the composite forms Paul's scriptural proof that the spiritual stupor of majority Israel is itself a divine action anticipated in the prophetic corpus."},
      {"type": "quote", "target": "Deut 29:4", "note": "Moses's testimony that God had not yet given Israel eyes to see or ears to hear — combined with Isa 29:10 in Paul's citation, this verse establishes the Mosaic precedent for divinely administered spiritual dullness; the hardening of Israel is not a Pauline explanation of embarrassing historical data but the fulfillment of multiple OT predictions."}
    ],
    "9": [
      {"type": "quote", "target": "Ps 69:22-23", "note": "David's imprecatory prayer — may their table become a snare and a trap, a stumbling block and a retribution — is applied to the majority of Israel who have stumbled over Christ; Psalm 69 is one of the most extensively Christologically applied psalms in the NT (Ps 69:4 = John 15:25; Ps 69:9 = John 2:17; Ps 69:21 = John 19:29), and here Paul applies the imprecatory section to Israel's hardening."}
    ],
    "10": [
      {"type": "quote", "target": "Ps 69:23", "note": "The continuation of the same psalm — may their backs be bent forever — concludes Paul's citation; the bowed-back image of perpetual servitude is applied to Israel's present condition of spiritual submission to the works-righteousness system that cannot justify."}
    ],
    "11": [
      {"type": "allusion", "target": "Deut 32:21", "note": "God provoking Israel to jealousy through a non-nation — Paul has already cited this (10:19); here he develops its logic: Israel's stumbling was purposive, resulting in salvation going to the Gentiles, which in turn will make Israel jealous; the Song of Moses's provocation-to-jealousy motif is the hermeneutical key to Paul's understanding of the Jew-Gentile dynamic in redemptive history."}
    ],
    "12": [
      {"type": "theme", "target": "Isa 27:6", "note": "Jacob will take root and Israel will bud and blossom and fill the world with fruit — Paul's 'if their transgression means riches for the world, and their loss means riches for the Gentiles, how much greater riches will their fullness bring' anticipates the a-fortiori logic using the Isaianic vine-image of Israel filling the world with abundance when restored."}
    ],
    "13": [
      {"type": "allusion", "target": "Isa 49:6", "note": "The Servant as a light to the Gentiles so that salvation reaches the ends of the earth — Paul's taking pride in his ministry as apostle to the Gentiles is grounded in the Isaianic Servant's commission; Paul sees himself as the agent through whom the Servant's Gentile mission is being executed."}
    ],
    "14": [
      {"type": "allusion", "target": "Deut 32:21", "note": "I will make them envious by a non-nation — Paul's explicit strategy of provoking Israel to envy through his Gentile ministry is the pastoral application of Moses's song; the apostle to the Gentiles is simultaneously working toward the redemption of his own people by the indirect route of the Mosaic jealousy-provocation."}
    ],
    "15": [
      {"type": "allusion", "target": "Ezek 37:1-14", "note": "The vision of the valley of dry bones — 'life from the dead' — Paul's 'if their rejection brought reconciliation to the world, what will their acceptance be but life from the dead?' uses the Ezekielian resurrection imagery for Israel's future restoration; the final gathering of Israel is the eschatological resurrection that triggers the completion of new-creation life."}
    ],
    "16": [
      {"type": "type", "target": "Num 15:19-21", "note": "The firstfruits dough offering that consecrates the whole batch — Paul's 'if the part of the dough offered as firstfruits is holy, then the whole batch is holy' applies the Levitical principle of firstfruits-consecration to argue that the patriarchs (and the believing remnant) as firstfruits sanctify and anticipate the consecration of all Israel."}
    ],
    "17": [
      {"type": "allusion", "target": "Ps 52:8", "note": "The psalmist as a green olive tree in the house of God — Paul's olive-tree image for Israel and the Gentile wild-olive shoot inhabits the OT's consistent use of the olive tree as a symbol of covenant blessing and divine presence; the psalmist's identity with a flourishing olive tree is the positive image whose disruption Paul describes in the broken-off branches."}
    ],
    "18": [
      {"type": "allusion", "target": "Jer 11:16", "note": "The LORD called Israel a thriving olive tree, but announced that its branches would be burned — Jeremiah's prior use of the olive tree for Israel as both flourishing and subject to covenant judgment is the background for Paul's grafting-in language; the same tree can shed branches through covenant faithlessness."}
    ],
    "19": [
      {"type": "theme", "target": "Deut 7:6", "note": "Israel chosen from all peoples to be his treasured possession — the Gentile believer who reasons that branches were broken off so they could be grafted in is implicitly claiming Israel's election-status for themselves; Paul's warning in v20 will correct the arrogance that assumes Gentile inclusion displaces Jewish election."}
    ],
    "20": [
      {"type": "allusion", "target": "Prov 16:18", "note": "Pride goes before destruction, a haughty spirit before a fall — Paul's 'do not be arrogant but be afraid' draws on the wisdom tradition's consistent warning that the pride of the secure is the precondition for their fall; the Gentile believer who boasts over broken-off branches stands in the position Proverbs repeatedly warns against."}
    ],
    "21": [
      {"type": "allusion", "target": "Ezek 17:9-10", "note": "The parable of the vine transplanted — Ezekiel's allegory of a vine torn up when it forsakes its planting ground is the OT background for Paul's warning that God did not spare the natural branches; the same God who cut the vine in Ezekiel's parable will not spare the wild-olive Gentile who becomes arrogant."}
    ],
    "22": [
      {"type": "allusion", "target": "Isa 40:11", "note": "The gentleness of the divine shepherd — Paul's 'consider the kindness and sternness of God' names both qualities that Isaiah's portraits of God combine; kindness (chrestotes) toward those who receive him and severity (apotomia) toward those who fall away are both true of the same God."}
    ],
    "23": [
      {"type": "allusion", "target": "Ezek 37:11-14", "note": "God able to make the dry bones live again — Paul's 'God is able to graft them in again' appeals to the divine omnipotence that makes Israel's future restoration not merely wishful but guaranteed by the power of the God who raises the dead; Ezekiel's resurrection-of-Israel vision is the OT ground for this claim."}
    ],
    "24": [
      {"type": "theme", "target": "Isa 11:11-12", "note": "God gathering Israel a second time from the four quarters of the earth — the re-grafting of the natural branches is the Pauline metaphor for the Isaianic second gathering; what is contrary to nature (v24) from a horticultural standpoint is entirely consistent with God's covenant purposes announced in the prophets."}
    ],
    "25": [
      {"type": "allusion", "target": "Isa 6:9-11", "note": "The hardening of Israel until the cities lie ruined — Paul's mystery that hardening has come to part of Israel until the fullness of the Gentiles comes in echoes Isaiah's own commission to preach until the land is utterly desolate (until the stump remains, Isa 6:13); the hardening has a temporal limit in Isaiah just as in Paul."}
    ],
    "26": [
      {"type": "quote", "target": "Isa 59:20-21", "note": "The deliverer will come to Zion, to those in Jacob who repent of their sins — Paul's 'the deliverer will come from Zion; he will turn godlessness away from Jacob' (adapting the LXX) reads the Isaianic Zion-deliverer as the returning Christ whose parousia will precipitate Israel's final salvation; the modification from 'to Zion' to 'from Zion' reflects the post-resurrection, post-ascension location of the deliverer."},
      {"type": "allusion", "target": "Isa 27:9", "note": "Jacob's guilt will be atoned for when all the altar stones are to be like chalk — Paul's 'and this is my covenant with them when I take away their sins' (v27) draws on Isa 27:9's promise of Israel's final atonement; the eschatological removal of sin is the content of the new covenant applied to Israel's ultimate salvation."}
    ],
    "27": [
      {"type": "allusion", "target": "Jer 31:33-34", "note": "The new covenant promise — I will forgive their wickedness and remember their sin no more — is the content of the covenant Paul describes as Israel's ultimate portion; the final salvation of all Israel is the realization of Jeremiah's new covenant, which included Israel's full forgiveness as its climactic element."}
    ],
    "28": [
      {"type": "theme", "target": "Deut 7:9", "note": "The faithful God keeping his covenant love to a thousand generations of those who love him — Paul's 'as far as election is concerned, they are loved on account of the patriarchs' grounds the irrevocability of Israel's election in the Deuteronomic divine faithfulness to the covenant made with the patriarchs; the thousands-of-generations promise cannot be annulled by Israel's current unbelief."}
    ],
    "29": [
      {"type": "allusion", "target": "Num 23:19", "note": "God is not a man that he should change his mind; has he promised and not fulfilled? — Paul's 'God's gifts and his call are irrevocable' (ametameletos) is the NT form of Numbers 23:19's declaration of divine consistency; what God has committed to the patriarchs through his call and gifts cannot be revoked by human unfaithfulness."}
    ],
    "30": [
      {"type": "theme", "target": "Hos 1:6-2:1", "note": "Lo-Ruhamah (not loved) and Lo-Ammi (not my people) reversed in Hosea to Ruhamah (loved) and Ammi (my people) — Paul's chiastic structure (formerly disobedient → now received mercy; now disobedient → will receive mercy) mirrors Hosea's reversal pattern; mercy following disobedience is the structural principle of both Hosea's covenant theology and Paul's argument."}
    ],
    "31": [
      {"type": "allusion", "target": "Zech 12:10", "note": "God pouring out a spirit of grace and supplication on the house of David so they will look on the one they have pierced — the future receptivity of Israel that Paul anticipates ('so they too may now receive mercy') connects to Zechariah's vision of Israel's grief-unto-repentance when they recognize the pierced one; Zechariah's prophecy is one OT anchor for Paul's expectation."}
    ],
    "32": [
      {"type": "allusion", "target": "Gen 3:22", "note": "God declaring that humanity had become like one of us knowing good and evil — the Adamic condition (bound over to disobedience, knowing good but choosing evil) is the universal situation Paul summarizes; God's binding all in disobedience so that he may have mercy on all is the reversal of the Adamic fall through the mercy that operates at the same universal scope as the fall."}
    ],
    "33": [
      {"type": "theme", "target": "Job 11:7-9", "note": "Can you fathom the mysteries of God? They are higher than the heavens and deeper than Sheol — the doxological wonder at divine inscrutableness with which Paul closes the argument of ch9-11 inhabits the wisdom tradition of Job; the depths and heights of God's wisdom that Job's friends gesticulate toward are now displayed in the mystery of election, hardening, and universal mercy."}
    ],
    "34": [
      {"type": "quote", "target": "Isa 40:13", "note": "Who has known the mind of the LORD, or who has been his counselor? — Paul's doxological citation lifts Isaiah 40:13 from its context (God so great that no one guided him in creation) and applies it to the inscrutable wisdom of his redemptive plan; the same God whose mind is unfathomable in creation is equally unfathomable in the election of the remnant and the mercy to all."},
      {"type": "allusion", "target": "Job 15:8", "note": "Eliphaz asks Job: do you limit wisdom to yourself? Have you listened in on God's deliberations? — Paul's 'who has been his counselor' echoes the wisdom-tradition's consistent warning against presuming to have access to the divine council; the rhetorical questions in vv34-35 draw on this theme."}
    ],
    "35": [
      {"type": "allusion", "target": "Job 41:11", "note": "God declaring: who has given to me that I must repay? Everything under heaven belongs to me — Paul's 'who has ever given to God, that God should repay them?' is a near-quotation of Job 41:11; the divine self-sufficiency that God asserts from the whirlwind is the theological ground for understanding mercy as pure grace, not compensation."}
    ],
    "36": [
      {"type": "allusion", "target": "1 Chr 29:14", "note": "David's prayer — 'Everything comes from you, and we have given you only what comes from your hand' — Paul's 'for from him and through him and for him are all things' is the doxological formulation of the same Davidic insight: creation and creature exist within the divine self-giving, not beside or independent of it."}
    ]
  },
  "12": {
    "1": [
      {"type": "allusion", "target": "Ps 51:17", "note": "The sacrifices of God are a broken and contrite heart — Paul's call to 'offer your bodies as a living sacrifice' stands in the prophetic-wisdom tradition that reinterpreted Levitical sacrifice as the offering of the whole person; the living sacrifice Paul calls for fulfills what Ps 51:17 and Isa 1:11-13 pointed toward when they relativized animal sacrifice in favor of the interior offering."},
      {"type": "type", "target": "Lev 1:3", "note": "The whole burnt offering presented before the LORD — Paul's 'living sacrifice, holy and pleasing to God' uses Levitical sacrificial categories (holy, pleasing, offered as worship) but transforms them: the sacrifice is living, continuous, and constituted by the self-presentation of the entire person rather than the death of an animal."}
    ],
    "2": [
      {"type": "allusion", "target": "Ezek 36:26", "note": "God's promise to give his people a new heart and a new spirit, removing the heart of stone — Paul's 'be transformed by the renewing of your mind' is the apostolic exhortation corresponding to the Ezekielian promise; the new-covenant transformation of the inner person is both divine gift (Ezekiel) and ethical summons (Paul), inseparable poles of the same reality."}
    ],
    "3": [
      {"type": "allusion", "target": "Prov 3:7", "note": "Do not be wise in your own eyes; fear the LORD and shun evil — Paul's 'do not think of yourself more highly than you ought, but think with sober judgment' is the Solomonic wisdom applied to the new covenant community; self-knowledge that includes awareness of divine grace-measure echoes the wisdom tradition's consistent critique of self-inflation."}
    ],
    "4": [
      {"type": "type", "target": "1 Cor 12:12", "note": "The body-as-community image Paul develops here draws on OT corporate anthropology — Israel as a single body, members with distinct functions — but Paul's innovation is the 'in Christ' qualifier that makes the body the body of the Messiah, the new-covenant assembly that replaces the tribal assembly of the Sinai covenant."}
    ],
    "5": [
      {"type": "allusion", "target": "Exod 19:5-6", "note": "Israel as a kingdom of priests — Paul's 'in Christ we, though many, form one body' applies the Sinai corporate identity to the new covenant community, which inherits the priestly-national identity of Israel now constituted by union with Christ rather than by Mosaic covenant."}
    ],
    "6": [
      {"type": "theme", "target": "Num 11:25-29", "note": "The Spirit distributed among the seventy elders, each prophesying — Paul's 'we have different gifts, according to the grace given to each of us' stands in the tradition of the distributed Spirit in Numbers 11, where the divine Spirit-endowment for various functions was understood as a single Spirit distributing different capacities to different members of the community."}
    ],
    "7": [
      {"type": "theme", "target": "Ezra 7:10", "note": "Ezra devoted to studying, doing, and teaching the law — the teaching office Paul mentions (if it is teaching, then teach) stands in the OT tradition of the teacher-scribe whose function was to transmit and apply the covenant word; in the new covenant the teacher transmits the apostolic gospel."}
    ],
    "8": [
      {"type": "allusion", "target": "Prov 11:24-25", "note": "One person gives freely, yet gains even more — Paul's 'if it is giving, then give generously' inhabits the Proverbs wisdom about liberality: the one who scatters gains, the one who withholds loses; generosity is the wisdom-posture commended throughout the OT and here named as a Spirit-endowed gift."}
    ],
    "9": [
      {"type": "allusion", "target": "Ps 97:10", "note": "Let those who love the LORD hate evil — Paul's 'love must be sincere; hate what is evil; cling to what is good' begins the ethical catechism of ch12 with the Psalter's consistent linkage of love-for-God and hate-of-evil; the OT does not separate devotion from moral discernment, and neither does Paul."}
    ],
    "10": [
      {"type": "allusion", "target": "Lev 19:18", "note": "Love your neighbor as yourself — Paul's 'be devoted to one another in love; honor one another above yourselves' is the intensification of the Levitical love-command; the Philadelphia (brotherly-love) devotion goes beyond the minimum (love as much as yourself) to the active preferring of others' honor above one's own."}
    ],
    "11": [
      {"type": "theme", "target": "Prov 6:6-11", "note": "The ant who works without being commanded, never lacking because of its diligence — Paul's 'never be lacking in zeal; keep your spiritual fervor' draws on the wisdom tradition's commendation of diligent labor applied here to the spiritual life; sloth in serving the Lord is the new covenant form of the sluggard's failure."}
    ],
    "12": [
      {"type": "allusion", "target": "Ps 130:5-6", "note": "I wait for the LORD more than watchmen wait for the morning — Paul's 'joyful in hope, patient in affliction, faithful in prayer' is the dispositional triad that the Psalter's lament-and-hope tradition produces: the hope that waits, the patience that endures affliction, and the prayer that maintains the relationship during trial."}
    ],
    "13": [
      {"type": "theme", "target": "Deut 15:7-11", "note": "Do not be hardhearted toward your poor brother; open your hand freely — Paul's 'share with the Lord's people who are in need' continues the Deuteronomic open-handedness command, now applied to the new covenant community of the poor."}
    ],
    "14": [
      {"type": "allusion", "target": "Prov 25:21-22", "note": "If your enemy is hungry, give him food; heap burning coals on his head — Paul's 'bless those who persecute you; bless and do not curse' is the NT intensification of the Proverbs principle of active good toward enemies; the curse-tradition of the OT (as in Ps 109) is here replaced by the blessing-posture that Proverbs already points toward."}
    ],
    "15": [
      {"type": "theme", "target": "Job 30:25", "note": "Job weeping for those in trouble — the empathetic co-suffering Paul commends in 'rejoice with those who rejoice; mourn with those who mourn' is the covenant-community practice that the wisdom tradition values; Job's weeping for others' suffering is the OT form of the communal empathy Paul commands."}
    ],
    "16": [
      {"type": "allusion", "target": "Prov 3:7", "note": "Do not be wise in your own eyes — Paul's 'do not be proud; be willing to associate with people of low position; do not be conceited' reprises the wisdom tradition's warning about self-inflation; the willingness to associate with the lowly is the practical outworking of not thinking more highly of oneself than one ought (12:3)."}
    ],
    "17": [
      {"type": "allusion", "target": "Prov 20:22", "note": "Do not say I will pay back this wrong; wait for the LORD and he will avenge — Paul's 'do not repay anyone evil for evil' stands in the Proverbs tradition of leaving vengeance to God; the OT already anticipated the NT prohibition on personal retaliation."}
    ],
    "18": [
      {"type": "allusion", "target": "Ps 34:14", "note": "Turn from evil and do good; seek peace and pursue it — Paul's 'if it is possible, as far as it depends on you, live at peace with everyone' is the apostolic application of the Psalter's peace-pursuit; the qualification (if possible, as far as it depends on you) is Paul's pastoral realism about circumstances where peace is refused by the other party."}
    ],
    "19": [
      {"type": "quote", "target": "Deut 32:35", "note": "From the Song of Moses — 'It is mine to avenge; I will repay, says the Lord' — Paul prohibits personal vengeance on the ground that God has claimed vengeance as his own prerogative; the Mosaic song's assertion of divine eschatological justice is the theological warrant for leaving room for God's wrath rather than taking it into one's own hands."}
    ],
    "20": [
      {"type": "quote", "target": "Prov 25:21-22", "note": "If your enemy is hungry, feed him; if he is thirsty, give him water to drink — in doing this you will heap burning coals on his head — Paul cites the Proverbs passage to ground the active-good-toward-enemies principle; the burning coals is ambiguous (shame that leads to repentance, or the divine judgment that follows unrepentant hostility), but the main point is the counterintuitive power of meeting hostility with concrete acts of goodness."}
    ],
    "21": [
      {"type": "allusion", "target": "Gen 4:7", "note": "Sin crouching at Cain's door, desiring to have him but he must rule over it — Paul's 'do not be overcome by evil, but overcome evil with good' echoes the divine summons to Cain (who failed); the community can succeed where Cain failed by meeting evil with good rather than escalating to greater evil."}
    ]
  },
  "13": {
    "1": [
      {"type": "allusion", "target": "Prov 8:15-16", "note": "By wisdom kings reign and rulers make just laws — Paul's 'there is no authority except that which God has established' grounds civil authority in divine ordering; the Proverbs tradition that wisdom (the divine attribute) is the source and ground of legitimate governance is the OT background for the apostolic teaching on governing authorities."},
      {"type": "allusion", "target": "Dan 2:21", "note": "God sets up kings and deposes them — Paul's divine-appointment of governing authorities echoes Daniel's consistent presentation of God as the sovereign over all political arrangements; the same God who used Nebuchadnezzar and Cyrus as instruments of his purpose has established the authorities Paul's readers must submit to."}
    ],
    "2": [
      {"type": "theme", "target": "Num 16:1-3", "note": "Korah's rebellion against Moses's divinely appointed authority — those who rebel against God's appointed leaders rebel against God himself; Paul's 'whoever rebels against the authority is rebelling against what God has instituted' applies the Mosaic-Korah principle to civil governance."}
    ],
    "3": [
      {"type": "allusion", "target": "Prov 14:35", "note": "A king's favor is toward a wise servant, but his wrath falls on a shameful one — the OT principle that legitimate authority rewards good conduct and punishes bad is the wisdom background for Paul's 'rulers hold no terror for those who do right, but for those who do wrong'; civil governance functions by the same principle of rewarding good and punishing evil that wisdom literature consistently teaches."}
    ],
    "4": [
      {"type": "allusion", "target": "Gen 9:6", "note": "Whoever sheds human blood, by humans shall their blood be shed — the Noahic grounding of capital punishment in the image of God establishes that the sword-bearing authority Paul mentions ('for God's servant is an avenger who carries out God's wrath on the wrongdoer') has OT precedent; civil authority's sword is the institutional form of the Gen 9:6 principle."}
    ],
    "5": [
      {"type": "theme", "target": "Eccl 8:2", "note": "Obey the king's command because you took an oath before God — the wisdom tradition that grounds civil submission in the God-commanded oath is the OT background for Paul's 'it is necessary to submit to the authorities, not only because of possible punishment but also as a matter of conscience'; submission has a conscience-dimension, not merely a fear-of-punishment dimension."}
    ],
    "6": [
      {"type": "allusion", "target": "Ezra 6:8", "note": "The Persian king ordering tax revenues for the rebuilding of the temple — the OT practice of paying taxes to pagan authorities (affirmed by Ezra and the returnees paying tribute to Persia) is the background for Paul's 'this is also why you pay taxes, for the authorities are God's servants'; taxing legitimate authority is itself a divine ordering."}
    ],
    "7": [
      {"type": "allusion", "target": "Prov 3:27", "note": "Do not withhold good from those to whom it is due — Paul's 'give to everyone what you owe them' applies the Proverbs principle of rendering what is due to specific civic obligations: taxes, revenue, respect, honor."}
    ],
    "8": [
      {"type": "allusion", "target": "Lev 19:18", "note": "Love your neighbor as yourself — Paul's 'the one who loves others has fulfilled the law' grounds the love-debt in the Levitical commandment that the entire ethical teaching of the OT pivots on; the debt of love that never fully discharges is the new covenant form of the ongoing obligation Lev 19:18 places on God's people."}
    ],
    "9": [
      {"type": "quote", "target": "Exod 20:13-17", "note": "The Decalogue's second table — do not commit adultery, do not murder, do not steal, do not covet — Paul summarizes the commandments that govern neighbor relations by citing them and then distilling them into the single principle of Lev 19:18; the Sinai commandments are not abrogated but are compressed into the love-command that Jesus identified as their summary."},
      {"type": "quote", "target": "Lev 19:18", "note": "Love your neighbor as yourself — Paul identifies this as the fulfillment of all the neighbor-directed commandments; Lev 19:18 is the summary commandment in the Torah that both Jesus and Paul identify as the principle that encompasses all the social ethics of the Decalogue."}
    ],
    "10": [
      {"type": "allusion", "target": "Ps 112:5", "note": "Good will come to those who are generous and lend freely, who conduct their affairs with justice — the wisdom tradition's portrait of the good person who does no harm to a neighbor is the OT background for Paul's summary 'love does no harm to a neighbor; therefore love is the fulfillment of the law.'"}
    ],
    "11": [
      {"type": "allusion", "target": "Isa 56:1", "note": "Maintain justice and do what is right, for my salvation is close at hand — Paul's 'the hour has already come for you to wake from your slumber; our salvation is nearer now than when we first believed' is the apostolic version of Isaiah's eschatological urgency; the nearness of salvation is the motive for present ethical intensity."}
    ],
    "12": [
      {"type": "allusion", "target": "Isa 60:1-2", "note": "Arise, shine, for your light has come, and the glory of the LORD rises upon you — Paul's 'the night is nearly over; the day is almost here; let us put on the armor of light' inhabits the Isaianic dawn-metaphor for the eschatological era of divine presence; the light-armor of the new day is the ethical posture appropriate to those living in the overlap of the ages."}
    ],
    "13": [
      {"type": "allusion", "target": "Prov 23:20-21", "note": "Do not join those who drink too much wine or gorge themselves on meat, for drunkards and gluttons become poor — Paul's 'not in carousing and drunkenness, not in sexual immorality and debauchery' draws on the wisdom tradition's consistent catalogue of behaviors that belong to the darkness of self-indulgence rather than the light of disciplined life."}
    ],
    "14": [
      {"type": "allusion", "target": "Isa 61:10", "note": "Clothed with garments of salvation, arrayed in a robe of his righteousness — Paul's 'clothe yourselves with the Lord Jesus Christ' is the Christological fulfillment of the Isaianic clothing-image; where Isaiah speaks of being clothed with salvation and righteousness, Paul names the one who is salvation and righteousness as the clothing."}
    ]
  },
  "14": {
    "1": [
      {"type": "theme", "target": "Isa 56:3-8", "note": "God welcoming foreigners and eunuchs who join themselves to the LORD — Paul's 'accept the one whose faith is weak' applies the OT principle of welcoming the marginalized who maintain covenant devotion even if their practice differs from the dominant community norm; the weak-in-faith Roman believers are the new covenant analog of those the majority would exclude."}
    ],
    "2": [
      {"type": "allusion", "target": "Dan 1:8-16", "note": "Daniel and his friends refusing the king's food and thriving on vegetables and water — the pattern of believers choosing a restricted diet for reasons of conscience before God is the OT precedent for the weak-in-faith vegetarian believer Paul describes; Daniel's practice was honorable, even if not binding on all, and he continued in it without condemning others."}
    ],
    "3": [
      {"type": "allusion", "target": "Lev 19:15", "note": "Do not pervert justice; do not show partiality — Paul's 'the one who eats must not treat with contempt the one who does not, and the one who does not eat must not judge the one who does' applies the Levitical principle of impartiality within the community to the table-fellowship disputes of the Roman house-churches."}
    ],
    "4": [
      {"type": "allusion", "target": "Prov 17:2", "note": "A prudent servant will rule over a disgraceful son — Paul's 'who are you to judge someone else's servant? To their own master, servants stand or fall' applies the patron-client wisdom about the household authority structure; judging another person's servant is a presumption of authority that belongs to the master alone."}
    ],
    "5": [
      {"type": "allusion", "target": "Col 2:16-17", "note": "Paul elsewhere notes that food, drink, and festival observances (including Sabbath) are shadows of the reality found in Christ — the dispute about days in 14:5-6 stands in this same framework; one person considers one day more sacred than another on conscience grounds without this being either required or prohibited for all."}
    ],
    "6": [
      {"type": "allusion", "target": "Deut 14:26", "note": "Eat what you desire at the appointed place and rejoice before the LORD — the OT principle that eating before God (with thanksgiving) consecrates the meal is the background for Paul's 'whoever eats meat does so to the Lord, for they give thanks to God'; the thanksgiving that accompanies eating is the covenantal act that makes the meal an act of worship rather than mere consumption."}
    ],
    "7": [
      {"type": "allusion", "target": "Ps 100:3", "note": "Know that the LORD is God; it is he who made us, and we are his — Paul's 'none of us lives for ourselves alone, and none of us dies for ourselves alone' denies the individual autonomy that would ground either the libertarian or the ascetic position; being God's creature means belonging to God, not to oneself, in both life and death."}
    ],
    "8": [
      {"type": "allusion", "target": "Ps 116:15", "note": "Precious in the sight of the LORD is the death of his faithful servants — Paul's 'whether we live or die, we belong to the Lord' is the apostolic form of the psalmist's assurance; the same Lord who values his servants' lives also owns their deaths, so neither state puts the believer outside the Lord's claiming."}
    ],
    "9": [
      {"type": "allusion", "target": "Ps 22:28-29", "note": "Dominion belongs to the LORD and he rules over the nations; all who go down to the dust will kneel before him — Paul's 'Christ died and returned to life so that he might be the Lord of both the dead and the living' applies Psalm 22's declaration of divine lordship over the dead (those who go down to dust) and the living to the risen Christ."}
    ],
    "10": [
      {"type": "allusion", "target": "Eccl 12:14", "note": "God will bring every deed into judgment — Paul's 'we will all stand before God's judgment seat' is the eschatological application of the Ecclesiastes principle that divine judgment covers all; the judgment is individual (each of us will give an account, v12), consistent with the OT's consistent teaching on individual accountability before God."}
    ],
    "11": [
      {"type": "quote", "target": "Isa 45:23", "note": "By myself I have sworn, a word has gone out from my mouth in truth: every knee will bow before me; every tongue will confess — Paul applies this to the universal eschatological accountability before God's judgment seat; in Philippians 2:10-11 Paul applies the same text to Christ's exaltation, showing that the divine name-bowing Isaiah describes is enacted in the universal acknowledgment of Christ as Lord."}
    ],
    "12": [
      {"type": "theme", "target": "Ezek 18:20", "note": "The soul who sins is the one who will die; the child will not share the guilt of the parent — Paul's 'each of us will give an account of ourselves to God' is the NT form of Ezekiel's individualized judgment; the accountability is personal, not transferable, which grounds both the prohibition on judging others (their accountability is theirs) and the urgency of personal moral responsibility."}
    ],
    "13": [
      {"type": "allusion", "target": "Isa 8:14", "note": "The LORD as a stone that causes stumbling — Paul's 'make up your mind not to put any stumbling block or obstacle in the way of a brother or sister' applies the OT stumbling-stone image constructively: what the LORD can be to those who do not receive him, the strong believer can become to the weak through careless use of freedom."}
    ],
    "14": [
      {"type": "allusion", "target": "Gen 1:31", "note": "God saw all that he had made and it was very good — Paul's 'nothing is unclean in itself' stands in the Creational goodness of God's declaration over his own creation; the categories of clean and unclean in the Levitical system were never denials of creation's inherent goodness but covenant-boundary markers that Christ has now reconfigured."}
    ],
    "15": [
      {"type": "allusion", "target": "Lev 19:18", "note": "Love your neighbor as yourself — Paul's 'if your brother or sister is distressed because of what you eat, you are no longer acting in love' applies the love-command to the specific case of the strong believer whose freedom is wounding the weak; the love-obligation reconfigures the exercise of legitimate freedom."}
    ],
    "16": [
      {"type": "theme", "target": "Isa 52:5", "note": "The name of God is blasphemed among the nations because of Israel's behavior — Paul's 'do not let what you know is good be spoken of as evil' applies the prophetic concern about God's reputation to the behavior of the strong believer; the community's internal conflicts that spill into public perception damage the gospel's witness."}
    ],
    "17": [
      {"type": "allusion", "target": "Isa 32:16-17", "note": "The fruit of righteousness will be peace and the effect of righteousness will be quietness and confidence — Paul's 'the kingdom of God is not a matter of eating and drinking, but of righteousness, peace and joy in the Holy Spirit' maps onto Isaiah's eschatological vision of the kingdom as the domain of righteousness-producing-peace; food and drink disputes are beside the point because the kingdom's substance is these deeper realities."}
    ],
    "18": [
      {"type": "theme", "target": "Deut 4:6", "note": "Keeping the commandments as wisdom in the sight of the nations — Paul's 'anyone who serves Christ in this way is pleasing to God and receives human approval' echoes the Deuteronomic concern for the community's testimony among those who observe them; righteous conduct produces both divine pleasure and the respect of onlookers."}
    ],
    "19": [
      {"type": "allusion", "target": "Ps 34:14", "note": "Seek peace and pursue it — Paul's 'let us make every effort to do what leads to peace and to mutual edification' applies the Psalter's peace-pursuit to the specific context of the strong-weak dispute; the effort required to achieve peace in a community of diverse practices is the new covenant form of the Psalter's active pursuit of shalom."}
    ],
    "20": [
      {"type": "allusion", "target": "Gen 1:31", "note": "God declared all things good — Paul's 'all food is clean' grounds the principle in creation theology; the Levitical distinction between clean and unclean food was covenant-boundary legislation, not an ontological claim about certain foods being evil, and Christ has reconfigured that boundary so that all food is what God declared it in Genesis 1."}
    ],
    "21": [
      {"type": "allusion", "target": "1 Cor 8:13", "note": "I will never eat meat again if it causes my brother to fall — Paul's parallel principle in 1 Corinthians frames Romans 14:21 in its broader context; the abstinence principle Paul commends here is the enacted form of the cruciform love that lays down its own rights for the sake of the other's conscience."}
    ],
    "22": [
      {"type": "allusion", "target": "Ps 32:2", "note": "Blessed is the one whose sin the LORD does not count against them — Paul's 'blessed is the one who does not condemn himself by what he approves' inhabits the Psalter's beatitude-tradition; the blessedness of the one whose conscience is clear before God is the subjective dimension of the objective blessedness of justification."}
    ],
    "23": [
      {"type": "allusion", "target": "Hab 2:4", "note": "The righteous will live by his faith — Paul has cited this as his thesis (1:17); here the reverse is stated: what is not from faith is sin; the faith-principle that governs justification (1:17) also governs the practical life of the community — every action must arise from faith to be right before God."}
    ]
  }
}

def main():
    existing = load_echo('romans')
    merge_echo(existing, ROMANS_ECHOES)
    save_echo('romans', existing)
    print('Romans 11–14 echoes written.')

if __name__ == '__main__':
    main()
