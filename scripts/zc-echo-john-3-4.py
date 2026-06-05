"""
MKT Echo — John chapters 3–4
Run: python3 scripts/zc-echo-john-3-4.py

Source data used:
- data/interlinear/john.json
- data/translation/draft/mediating/john.json (MKT text for quoting)
- data/parallels/john.json (ch 3 had 4 entries; ch 4 had none — absorbed below)

Key decisions in this range:
- John 3:14 (Num 21:8-9): classified `allusion` — Jesus explicitly draws
  the comparison in the text itself, but it is his own typological statement,
  not a NT claim that "this fulfilled that scripture."
- John 3:16 (Gen 22): classified `type` — the Akedah structural parallel
  (only son / deliberate giving by the father) is a recognized NT echo but
  the Evangelist does not cite it. Supplementary Isa 49:6 added as `theme`
  for the universal scope.
- John 3:28 (Mal 3:1; Isa 40:3): classified `fulfillment` — John the Baptist
  explicitly identifies himself as "sent ahead" of the Messiah, fulfilling
  the prophesied forerunner role.
- John 4:18 (2 Kgs 17:24-33): the "five husbands" as possible allusion to
  the five foreign nations Assyria resettled in Samaria, each bringing their
  own gods while also fearing Yahweh (note is hedged as possible allusion).
- John 4:26 (Isa 52:6; Exod 3:14): the absolute egō eimi claim carries
  the resonance of the divine self-identification formula in Deutero-Isaiah
  and the Sinai name revelation.
- Merge will not overwrite existing entries for vv. 3, 5, 13, 14, 16, 17,
  29, 34, 35, 36 (ch 3) and vv. 5, 6, 10, 14, 20, 22, 25, 44 (ch 4).
  This script adds supplemental entries to those verses and new entries
  for all uncovered verses with genuine OT connections.
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

JOHN_ECHOES = {
  "3": {
    # ── New verse entries ──────────────────────────────────────────────────

    "1": [
      {"type": "theme", "target": "Mic 3:1",
       "note": "Nicodemus as ἄρχων (ruler) of the Jews places him in the tradition of Israel's ruling class whom the prophets repeatedly addressed: 'Hear, you leaders of Jacob, you rulers of Israel.' Those most responsible for knowing the covenant are the first to be confronted with its fulfillment."}
    ],
    "2": [
      {"type": "theme", "target": "Deut 18:15",
       "note": "Nicodemus frames Jesus within the Mosaic category of a prophet validated by wonders: 'no one could do the signs you do if God were not with him.' The same credential — divine authorization confirmed by miracles — was the mark of the prophet like Moses Israel was taught to expect."}
    ],
    "6": [
      {"type": "theme", "target": "Gen 6:3",
       "note": "The antithesis between flesh and Spirit — flesh produces only flesh — echoes the Creator's distinction: 'My Spirit shall not abide in man forever, for he is flesh.' Unaided human nature lacks the capacity to generate spiritual life; that belongs to the Spirit alone."},
      {"type": "allusion", "target": "Ezek 36:26",
       "note": "The contrast between birth from flesh and birth from Spirit parallels Ezekiel's contrast between the old stony heart (the organ of fleshly resistance) and the new heart of flesh animated by God's Spirit — the divine surgery that regeneration requires."}
    ],
    "8": [
      {"type": "allusion", "target": "Gen 1:2",
       "note": "The wind/Spirit analogy exploits the double meaning of πνεῦμα and רוּחַ (both = wind and spirit). The Spirit hovering over the formless deep at creation — sovereign, untraceable, generating life from nothing — is the archetype Jesus invokes for the Spirit's freedom in new birth."},
      {"type": "allusion", "target": "Ezek 37:9",
       "note": "In Ezekiel's vision, the four winds are summoned to breathe life into the slain — the Spirit bringing resurrection from death through sovereign movement that cannot be predicted or controlled. Jesus' analogy of wind points to the same unconstrained, life-giving freedom."}
    ],
    "10": [
      {"type": "theme", "target": "Mal 2:7",
       "note": "'The lips of a priest ought to preserve knowledge... he is the messenger of the Lord Almighty.' As Israel's foremost teacher, Nicodemus bore the covenantal responsibility to know the prophets — including Ezekiel's promise of new birth. His bafflement is not just personal failure; it is institutional failure of the teaching office."}
    ],
    "11": [
      {"type": "theme", "target": "Isa 43:10",
       "note": "'You are my witnesses, declares the Lord.' The witness formula Jesus uses — 'we testify to what we have seen' — resonates with the divine appointment of direct-experience witnesses in Isaiah: those who have seen and heard are commissioned to speak. Jesus speaks as one who has seen heavenly realities directly."}
    ],
    "15": [
      {"type": "allusion", "target": "Num 21:9",
       "note": "The pattern of the bronze serpent — 'when anyone was bitten by a snake and looked at the bronze snake, they lived' — becomes the pattern of salvation: look in faith and live. The condition is the same (humble, directed trust in what God has provided); the scope expands from physical survival to eternal life."}
    ],
    "18": [
      {"type": "theme", "target": "Ps 34:22",
       "note": "The verdict that unbelievers 'stand condemned already' echoes the covenantal framework: those who take refuge in the Lord are not condemned; those who reject him remain under the pre-existing sentence. Condemnation is not an additional punishment brought by Christ's coming but the default state from which he offers rescue."}
    ],
    "19": [
      {"type": "allusion", "target": "Isa 9:2",
       "note": "The arrival of light in the world of darkness — and humanity's preference for darkness — fulfills Isaiah's vision: 'The people walking in darkness have seen a great light; on those living in the land of deep darkness a light has dawned.' John frames Jesus as this light throughout his Gospel; here the rejection of the light is already anticipated."},
      {"type": "theme", "target": "Job 24:13",
       "note": "Job observes that wrongdoers 'rebel against the light, not knowing its ways or staying in its paths.' The moral dynamic Jesus describes — evil deeds producing a preference for concealing darkness — is a pattern Job already diagnosed: it is not ignorance of the light but flight from it."}
    ],
    "20": [
      {"type": "theme", "target": "Ps 52:3",
       "note": "The Psalm's portrait of one who 'loves evil rather than good' provides the scriptural category for those who 'hate the light because their deeds are evil.' The choice against the light is an active moral preference, not merely spiritual blindness."}
    ],
    "21": [
      {"type": "theme", "target": "Ps 15:2",
       "note": "The one who 'lives by the truth and comes into the light' embodies the psalm's portrait of the person who 'walks blamelessly and does what is right.' Actions done in the sight of God are already transparent to his light; coming to the light is the natural movement of a life oriented toward truth."}
    ],
    "25": [
      {"type": "theme", "target": "Num 19:11",
       "note": "The dispute over 'ceremonial washing' (purification) stands against the backdrop of elaborate Mosaic purification rites — especially the water of cleansing in Numbers 19. John the Baptist's water and Jesus' Spirit-baptism both challenge and supersede the OT purity system by offering a purification those rites could only symbolize."}
    ],
    "27": [
      {"type": "theme", "target": "1 Chr 29:14",
       "note": "John's principle — 'a person can receive only what is given them from heaven' — echoes David's prayer: 'Everything comes from you, and we have given you only what comes from your hand.' Sovereignty over gifts, roles, and diminishment belongs to God; John's contentment with his assigned place reflects the same posture."}
    ],
    "28": [
      {"type": "fulfillment", "target": "Mal 3:1",
       "note": "John's self-description — 'I am not the Messiah but am sent ahead of him' — directly fulfills Malachi's prophecy: 'I will send my messenger, who will prepare the way before me.' The Baptist recognizes his own role in the prophetic script and names it explicitly."},
      {"type": "fulfillment", "target": "Isa 40:3",
       "note": "The forerunner's preparatory role fulfills Isaiah's 'voice crying in the wilderness: prepare the way for the Lord.' Jesus himself draws this connection for the crowds (Matt 11:10); John's self-identification in v. 28 carries the same implication."}
    ],
    "30": [
      {"type": "theme", "target": "Isa 40:6",
       "note": "John's willing decrease — 'he must become greater; I must become less' — embodies the prophetic recognition that 'all flesh is like grass... the grass withers and the flowers fall, but the word of our God endures forever.' John identifies himself with the passing moment, and Jesus with the enduring word."}
    ],
    "31": [
      {"type": "allusion", "target": "Prov 30:4",
       "note": "The contrast between the one who comes 'from above' (ἄνωθεν) and the one who is 'from the earth' answers Agur's rhetorical challenge: 'Who has gone up to heaven and come down?' The question was unanswerable in Proverbs; the Evangelist presents the one from above as the answer — the only qualified heavenly witness."}
    ],
    "32": [
      {"type": "allusion", "target": "Isa 53:1",
       "note": "The Evangelist's observation that 'no one accepts his testimony' echoes Isaiah's lament: 'Who has believed our message and to whom has the arm of the Lord been revealed?' The pattern of rejected testimony — God's authorized witness dismissed by those addressed — runs from the Servant's suffering to the Son's rejection."}
    ],
    "33": [
      {"type": "theme", "target": "Num 23:19",
       "note": "'Certified that God is truthful' echoes Balaam's oracle: 'God is not human, that he should lie, nor a human being, that he should change his mind.' Accepting Jesus' testimony is the same act as trusting the God who does not lie — it is a confessional act about God's character."}
    ],

    # ── Supplemental entries for already-covered verses ────────────────────

    "5": [
      # existing: Ezek 36:25-27, Isa 44:3 — add Jer 31:33
      {"type": "allusion", "target": "Jer 31:33",
       "note": "The new birth required for kingdom entry also resonates with Jeremiah's new-covenant promise: 'I will put my law in their minds and write it on their hearts.' Entrance by the Spirit is the mechanism of the interior transformation Jeremiah announced — not geographic or ethnic membership."}
    ],
    "13": [
      # existing: Prov 30:4 — add Deut 30:12
      {"type": "allusion", "target": "Deut 30:12",
       "note": "'It is not in heaven, that you should say, who will go up to heaven for us to get it?' Moses insisted the covenant word was accessible on earth. Jesus fulfills and inverts this: he is the Word who came down, making possible what Moses assured Israel it could not need — a mediator who ascends to retrieve heavenly knowledge."}
    ],
    "16": [
      # existing: Gen 22:1-19, Isa 53:6 — add Isa 49:6 for universal scope
      {"type": "theme", "target": "Isa 49:6",
       "note": "The scope of God's love — 'the world' (κόσμος) — echoes the Servant Songs' universal horizon: 'I will make you a light for the Gentiles, that my salvation may reach to the ends of the earth.' John 3:16 enacts the universalism the Servant mission announced."}
    ],
    "17": [
      # existing: Ezek 33:11 — add Isa 49:6
      {"type": "allusion", "target": "Isa 49:6",
       "note": "The mission to save rather than condemn the world echoes the Servant commissioned to be a light to the nations — the goal is restoration, not judgment. Israel's exclusive categories give way to a saving mission with no boundary."}
    ],
    "29": [
      # existing: Isa 62:5 — add Song 3:11
      {"type": "theme", "target": "Song 3:11",
       "note": "Song of Songs celebrates the wedding day with the image of the crowned bridegroom. John the Baptist's joy at 'hearing the bridegroom's voice' invokes this nuptial register: Israel's God as bridegroom, arriving to claim his bride, fills the Baptist with the joy that completes a long-anticipated covenant celebration."}
    ],
    "34": [
      # existing: Isa 61:1 — add Isa 11:2
      {"type": "allusion", "target": "Isa 11:2",
       "note": "Isaiah's Davidic branch receives the Spirit in full: 'The Spirit of the Lord will rest on him — the Spirit of wisdom and understanding, the Spirit of counsel and of might.' The 'without limit' qualifier in John echoes this cumulative anointing — every dimension of the Spirit rests on the one whom God has sent."}
    ],
    "35": [
      # existing: Ps 2:7-8 — add Gen 37:3
      {"type": "type", "target": "Gen 37:3",
       "note": "The beloved son whom the father honors above all others — Jacob's conspicuous love for Joseph that set him apart and sent him toward a destiny his brothers could not foresee — is a type of the Father's love for the Son and the authority placed in his hands. Joseph's story moves through rejection to universal authority; the Son's does the same."}
    ],
    "36": [
      # existing: Deut 27:26 — add Ps 2:12
      {"type": "theme", "target": "Ps 2:12",
       "note": "'Kiss the son, lest he be angry and your way lead to his destruction.' Psalm 2's warning to kings — that the anointed Son carries both blessing and judgment depending on response — provides the framework for John 3:36's binary: eternal life for the believer, abiding wrath for the one who rejects."}
    ]
  },

  "4": {
    # ── New verse entries ──────────────────────────────────────────────────

    "7": [
      {"type": "allusion", "target": "Gen 24:17",
       "note": "Abraham's servant asks Rebekah at the well for a drink ('Please give me a little water'), initiating the betrothal type-scene that results in her joining the patriarchal household. Jesus' request for water from the Samaritan woman at Jacob's well activates the same narrative pattern — a representative of the Lord seeking a covenant partner at a well."},
      {"type": "allusion", "target": "Exod 2:15",
       "note": "Moses, sitting at a well in a foreign land, encounters women drawing water and acts on their behalf. Jesus, traveling through foreign Samaria, initiates contact at a well in a way that parallels Moses' encounter — an outsider at a well, seeking water, initiating a decisive meeting."}
    ],
    "9": [
      {"type": "theme", "target": "Ezra 4:3",
       "note": "The deep hostility between Jews and Samaritans traces to the post-exilic rejection: when the returned exiles refused Samaritan participation in rebuilding the temple ('You have no part with us'), the rift hardened into centuries of mutual exclusion. The woman's surprise at Jesus' request reflects this entrenched barrier."},
      {"type": "theme", "target": "2 Kgs 17:24",
       "note": "The Samaritans' origins — foreign peoples Assyria settled in the land who developed a syncretistic faith (fearing Yahweh while worshiping other gods) — explain the Jewish contempt for their religious claims. Jesus crosses this boundary deliberately, signaling a new order of covenant access."}
    ],
    "12": [
      {"type": "theme", "target": "Gen 29:10",
       "note": "The woman's challenge — 'are you greater than our father Jacob, who gave us the well?' — invites Johannine comparison. John's Gospel uses such questions to establish Jesus' superiority to the founding figures: Jacob gave a well; Jesus offers water Jacob's well cannot provide."}
    ],
    "13": [
      {"type": "allusion", "target": "Isa 55:2",
       "note": "Jesus' observation that everyone who drinks from the well will thirst again echoes Isaiah's challenge to those who spend resources on what does not satisfy: 'Why spend money on what is not bread, and your labor on what does not satisfy?' The well offers temporary relief; Jesus offers what Isaiah promised — the food and drink that truly satisfy."}
    ],
    "18": [
      {"type": "allusion", "target": "2 Kgs 17:29",
       "note": "Possibly: the 'five husbands' the woman has had may allude to the five nations Assyria resettled in Samaria (2 Kgs 17:24), each of which brought its own god ('each national group made its own gods') while formally worshiping Yahweh. The current 'husband' who is not her husband would then represent the mixed syncretistic religion — an interpretive layer some scholars read in the text, though it functions equally as a direct word of knowledge about the woman's personal history."}
    ],
    "21": [
      {"type": "allusion", "target": "Mal 1:11",
       "note": "'A time is coming' when worship will transcend both Gerizim and Jerusalem echoes Malachi's vision: 'from the rising of the sun to its setting my name will be great among the nations, and in every place incense will be offered to my name.' The geographic restriction of OT worship is about to be superseded by worship as universal as the Spirit."}
    ],
    "23": [
      {"type": "fulfillment", "target": "Jer 31:33",
       "note": "Worship 'in Spirit and in truth' — the interior, location-independent worship the Father seeks — fulfills the new-covenant promise: 'I will put my law in their minds and write it on their hearts.' Such worship does not depend on proximity to a mountain or a temple; it arises from transformation of the inner person."},
      {"type": "allusion", "target": "Isa 29:13",
       "note": "The worship now being superseded is the kind God condemned through Isaiah: 'These people come near to me with their mouth and honor me with their lips, but their hearts are far from me.' Spirit-and-truth worship is the antithesis — hearts brought near, not lips performing a geographic ritual."}
    ],
    "24": [
      {"type": "theme", "target": "Deut 4:15",
       "note": "'You saw no form of any kind the day the Lord spoke to you at Horeb' — Moses grounds Israel's prohibition of images in God's spiritual nature. Jesus draws out the implication: a God who is Spirit cannot be adequately worshiped through external forms bound to a specific location. The Mosaic premise (no form visible) yields the Johannine conclusion (worship in Spirit, not place)."}
    ],
    "26": [
      {"type": "allusion", "target": "Isa 52:6",
       "note": "Jesus' 'I am he' (ἐγώ εἰμι, literally 'I am') carries the resonance of Deutero-Isaiah's divine self-disclosure: 'Therefore my people will know my name; therefore in that day they will know that it is I who foretold it. Yes, it is I.' The Evangelist uses this formula as a coded claim to divine identity throughout the Gospel."},
      {"type": "allusion", "target": "Exod 3:14",
       "note": "The absolute 'I am' picks up the divine name revealed to Moses at Sinai — the God who simply 'is,' underived and unlimited. Jesus' self-disclosure to the Samaritan woman — the first full public 'I am he' in John — grants to an outsider what Israel had received at Horeb."}
    ],
    "29": [
      {"type": "theme", "target": "Ps 139:1",
       "note": "The woman's astonishment that Jesus 'told me everything I ever did' is the human experience of divine omniscience: 'You have searched me, Lord, and you know me... you perceive my thoughts from afar... you are familiar with all my ways.' The Psalm presents this as intimate, searching knowledge; the woman meets it in a person at a well."}
    ],
    "34": [
      {"type": "allusion", "target": "Ps 40:8",
       "note": "Jesus' 'food' — doing the will of the one who sent him — echoes the Servant's interior disposition: 'I desire to do your will, my God; your law is within my heart.' Complete identification with the Father's mission as sustenance rather than obligation."},
      {"type": "allusion", "target": "Deut 8:3",
       "note": "'Man does not live on bread alone but on every word that comes from the mouth of God' — the wilderness teaching Moses gave is here embodied: Jesus himself is sustained by the word/will of the Father, demonstrating that the life he offers is of a different order than physical provision."}
    ],
    "35": [
      {"type": "allusion", "target": "Joel 3:13",
       "note": "Harvest imagery invoked with urgency — 'the fields are ripe for harvest' — echoes Joel's eschatological summons: 'Swing the sickle, for the harvest is ripe.' Jesus applies the final-harvest urgency to the present moment among the Samaritans: the eschatological gathering has begun."}
    ],
    "36": [
      {"type": "theme", "target": "Amos 9:13",
       "note": "'The days are coming when the reaper will be overtaken by the plowman and the planter by the one treading grapes' — the collapse of ordinary agricultural sequence (sower and reaper glad together) is Amos' image of eschatological abundance. Jesus invokes the same temporal collapse: the harvest of the Gentile mission has already begun."}
    ],
    "37": [
      {"type": "theme", "target": "Mic 6:15",
       "note": "The proverb 'one sows and another reaps' echoes the reversal Micah invokes as covenant curse: 'You will plant but not harvest.' Jesus converts the curse-form into a harvest-abundance pattern: in the kingdom's advance, the sower's labor yields fruit for reapers who did not sow — a sign of superabundant provision rather than futile labor."}
    ],
    "39": [
      {"type": "theme", "target": "Isa 66:18",
       "note": "The Samaritans of an entire town believing because of a woman's testimony echoes the eschatological gathering Isaiah envisions: 'I will come to gather all nations and languages, and they will come and see my glory.' The mission extends first to the hated neighbor, anticipating the nations."}
    ],
    "42": [
      {"type": "allusion", "target": "Isa 45:22",
       "note": "The Samaritan confession 'this man really is the Savior of the world' (σωτὴρ τοῦ κόσμου) picks up Isaiah's universal summons: 'Turn to me and be saved, all you ends of the earth; for I am God, and there is no other.' The title exceeds Jewish nationalism; it is the salvation Isaiah announced for all peoples."},
      {"type": "theme", "target": "Isa 49:6",
       "note": "The Servant's mission — 'to bring my salvation to the ends of the earth' — is claimed in the Samaritan confession. The people who were outside the covenant boundary are among the first to confess what Isaiah predicted: the Servant-Messiah as universal Savior, not merely Israel's king."}
    ],
    "46": [
      {"type": "theme", "target": "1 Kgs 17:17",
       "note": "The healing of a dying son at an official's urgent request evokes Elijah's encounter with the widow of Zarephath whose son died: a petitioner comes to God's messenger in desperate urgency over a child's life. Jesus performs as the greater Elijah — with authority that works across the geographic distance separating Capernaum from Cana."}
    ],
    "47": [
      {"type": "theme", "target": "2 Kgs 4:20",
       "note": "The royal official begging the prophet to 'come down before my child dies' mirrors the Shunammite woman's urgent journey to Elisha when her son died. Both encounters disclose the life-giving authority of God's messenger when sought in desperate faith."}
    ],
    "48": [
      {"type": "theme", "target": "Deut 29:3",
       "note": "Jesus' rebuke — 'unless you people see signs and wonders, you will never believe' — echoes Moses' diagnosis of Israel after the Exodus: 'With your own eyes you saw those great trials, those signs and great wonders. But to this day the Lord has not given you a mind that understands.' Signs alone do not produce faith; they expose the prior disposition of the heart."}
    ],
    "50": [
      {"type": "type", "target": "2 Kgs 4:36",
       "note": "Elisha's word to the Shunammite — 'your son is alive' — is the structural precedent for Jesus' 'your son will live.' The word of the prophet of God is sufficient for healing; the miracle is accomplished by declaration, not physical contact. Jesus fulfills what Elisha prefigured, with authority that transcends distance."}
    ],
    "53": [
      {"type": "theme", "target": "Josh 24:15",
       "note": "The official and his whole household believing mirrors the household-faith pattern of Israel's covenant history: 'as for me and my household, we will serve the Lord.' From one head of household to all its members, covenant faith extends through the family structure — a recurring pattern from Joshua through the Acts."}
    ],
    "54": [
      {"type": "type", "target": "2 Kgs 5:14",
       "note": "As Naaman the Syrian — a Gentile — was healed and came to faith through the word of Elisha without the prophet even being present (Elisha sent a messenger rather than appearing), so the royal official (a non-Galilean, likely Herodian court) receives a word-only healing and believes. Both healings of Gentile outsiders prefigure the mission scope that extends beyond Israel."}
    ],

    # ── Supplemental entries for already-covered verses ────────────────────

    "5": [
      # existing: Gen 48:22 — add Gen 33:19
      {"type": "allusion", "target": "Gen 33:19",
       "note": "The plot of ground at Shechem was purchased by Jacob from Hamor's sons (Gen 33:19) and recorded as a patriarchal site before the land grant to Joseph. John's specification of Sychar's location layers two patriarchal claims: the purchased site (Gen 33) and the inherited portion (Gen 48). The encounter with Jesus takes place in sacred geography laden with covenant memory."}
    ],
    "10": [
      # existing: Isa 55:1 — add Jer 2:13, Jer 17:13
      {"type": "allusion", "target": "Jer 2:13",
       "note": "Jesus as the source of 'living water' (ὕδωρ ζῶν) directly inverts Jeremiah's accusation: 'my people have forsaken me, the spring of living water, and have dug their own cisterns, broken cisterns that cannot hold water.' Jacob's well is the cistern; Jesus is the spring Israel was meant to return to."},
      {"type": "allusion", "target": "Jer 17:13",
       "note": "'Lord, those who turn away from you will be written in the dust, because they have forsaken the Lord, the spring of living water.' The woman has literally come to a static cistern (Jacob's well) rather than the true spring — Jesus announces that the living spring has arrived in person."}
    ],
    "14": [
      # existing: Ezek 47:9, Isa 12:3 — add Isa 44:3, Zech 14:8
      {"type": "fulfillment", "target": "Isa 44:3",
       "note": "'I will pour water on the thirsty land and streams on the dry ground; I will pour out my Spirit on your offspring' — the promised water that becomes a spring welling up from within fulfills Isaiah's pairing of water and Spirit. The spring Jesus offers is the indwelling Spirit of the restoration promise."},
      {"type": "allusion", "target": "Zech 14:8",
       "note": "Zechariah's eschatological promise of living water flowing from Jerusalem 'in summer and in winter' — without seasonal interruption — anticipates Jesus' offer of inexhaustible, season-independent living water. The arrival of the Messiah is the arrival of the water Zechariah's Day of the Lord would bring."}
    ],
    "22": [
      # existing: Isa 2:3 — add Ps 147:19
      {"type": "theme", "target": "Ps 147:19",
       "note": "'He has revealed his word to Jacob, his laws and decrees to Israel. He has done this for no other nation.' Jesus affirms the Zion-privilege behind 'salvation is from the Jews' — the covenant heritage is real and specific. The Samaritans rejected the prophets; their worship, however sincere, lacked the fullness of God's self-revelation."}
    ]
  }
}


def main():
    existing = load_echo('john')
    merge_echo(existing, JOHN_ECHOES)
    save_echo('john', existing)
    print('John 3–4 echoes written.')

if __name__ == '__main__':
    main()
