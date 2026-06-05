"""
MKT Echo Layer — John chapters 1–2
Run: python3 scripts/zc-echo-john-1-2.py

Source data used:
- data/interlinear/john.json
- data/translation/glossary-greek.json (G3056 λόγος; G3439 μονογενής; G4151 πνεῦμα)
- data/translation/draft/mediating/john.json (MKT text verified per verse)
- data/parallels/john.json (absorbed: 1:1→Gen 1:1, 1:11→Isa 53:3, 1:23→Isa 40:3,
                            1:29→Gen 22:8, 1:51→Gen 28:12, 2:17→Ps 69:9)

Key decisions in this range:
- Existing echoes/john.json already covers 1:1,3,4,5,9,11,12,14,17,18,23,29,32,34,45,51
  and 2:1,11,13,17,19 — merge_echo will not overwrite those entries.
- Gen 22:8 (Aqedah) added to 1:29 as a second type entry; existing Exod 12:3 and Isa 53:7
  entries in 1:29 are not overwritten.
- 1:47 "no deceit" (δόλος) is a deliberate LXX verbal echo: Gen 27:35 uses δόλῳ for Jacob's
  deception; classified allusion.
- 2:5 "do whatever he tells you" — Gen 41:55 Joseph typology is classified allusion (not type),
  since the structural parallel is secondary to the verbal echo.
- Zech 14:21 placed at 2:14 (discovery of traders) rather than 2:16 so that each action-verse
  has its own echo; Isa 56:7 at 2:16 matches the verbal "house of prayer" rebuke.
- Echo type for 2:21 is shadow (Ezek 37:26-27 eschatological sanctuary), not fulfillment, since
  John presents this as the disciples' post-hoc interpretation (v22), not an explicit prophecy cite.
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
  "1": {
    "2": [
      {
        "type": "theme",
        "target": "Prov 8:22-23",
        "note": "Personified Wisdom speaks: 'The LORD brought me forth as the first of his works, before his deeds of old; I was formed long ages ago, at the very beginning.' The Prologue's insistence that the Word was with God 'in the beginning' draws on the Wisdom tradition's portrait of a divine figure present before creation — the closest OT parallel to Logos Christology, and one the Evangelist's first-century audience would have heard immediately."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Mal 3:1",
        "note": "Malachi's 'See, I will send my messenger who will prepare the way before me' is activated by the Evangelist's precise framing: John is not self-appointed but 'sent from God' (ἀπεσταλμένος παρὰ θεοῦ). The word 'sent' positions John within the prophetic commissioning framework Malachi announced, where God himself dispatches the herald before his own arrival at the temple."
      }
    ],
    "7": [
      {
        "type": "theme",
        "target": "Isa 43:10",
        "note": "God declares to Israel: 'You are my witnesses, and my servant whom I have chosen, so that you may know and believe me.' The witness-bearing role (martyria) is a significant OT category — God calls his people to testify before the nations to his saving acts. John the Baptist's function as witness draws on this framework; the Evangelist's repeated emphasis on testimony throughout the Gospel activates the same OT witness vocation."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Mal 4:5",
        "note": "Malachi's promise to send Elijah 'before that great and dreadful day of the LORD comes' generates the question the crowd will ask in v21: is John this Elijah? The Evangelist's clarification that John was not the Light but a witness to it forestalls any identification of John with the messianic-Elijah expectation. The shadow of Malachi's Elijah prophecy frames these opening scenes throughout."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Isa 1:3",
        "note": "Isaiah's lament: 'The ox knows its master, the donkey its owner's manger, but Israel does not know, my people do not understand.' The Prologue echoes the same tragic irony — the world's maker is not recognized by the world he made. The rejection is not a surprise but the continuation of an ancient pattern of Israel's failure to recognize the God who owned them."
      }
    ],
    "13": [
      {
        "type": "shadow",
        "target": "Ezek 36:26-27",
        "note": "God promises: 'I will give you a new heart and put a new spirit in you... I will put my Spirit in you.' Ezekiel's new-covenant pledge of a divinely-wrought transformation — not achieved by human effort or natural descent — is the OT shadow of John's 'born of God.' Both texts emphasize the unilateral divine act; John's birth-from-above language (echoed in 3:3-8) develops what Ezekiel announced prophetically."
      }
    ],
    "15": [
      {
        "type": "theme",
        "target": "Mic 5:2",
        "note": "Micah declares of the coming Ruler: 'his origins are from of old, from ancient times' (מִקֶּדֶם מִימֵי עוֹלָם). John the Baptist's testimony that Christ 'existed before me' despite coming 'after me' presupposes eternal pre-existence precisely of this kind. The Baptist's paradox — chronologically later, ontologically prior — is the experiential form of what Micah encoded in prophetic language."
      }
    ],
    "16": [
      {
        "type": "theme",
        "target": "Ps 36:8-9",
        "note": "'They feast on the abundance of your house; you give them drink from your river of delights. For with you is the fountain of life.' John's 'from his fullness we have all received, grace upon grace' draws on the Psalter's image of God as inexhaustible source. Christ is now this fountain; the 'living water' language later in the Gospel (4:14; 7:37-38) develops the same image of drawing indefinitely from the divine source."
      }
    ],
    "19": [
      {
        "type": "theme",
        "target": "Deut 18:20-22",
        "note": "Deuteronomy mandates that the community test prophetic claims — if a prophet speaks what the LORD did not command, he has spoken presumptuously (Deut 18:20-22). The Sanhedrin's official delegation to John follows the OT obligation to discern true from false prophecy. The irony is that a legitimate procedure is being applied to the genuine forerunner — the mechanism designed to identify authentic messengers is now interrogating one."
      }
    ],
    "20": [
      {
        "type": "theme",
        "target": "Ps 2:2",
        "note": "Psalm 2 speaks of the LORD and his anointed (מְשִׁיחוֹ = mashiach = Christos). The interrogators' question 'Are you the Messiah?' draws directly on this royal-messianic tradition. John's explicit denial clears the ground — the true Anointed One of Psalm 2, to whom the nations are promised as an inheritance, is already present but not yet publicly identified."
      }
    ],
    "21": [
      {
        "type": "allusion",
        "target": "Mal 4:5",
        "note": "The question 'Are you Elijah?' comes directly from Malachi's promise that Elijah would return before the great and dreadful day of the LORD — a live expectation in Second Temple Judaism attested in Ben Sira and Qumran texts. The Baptist denies the literal identification; yet Luke 1:17 presents him as coming in the spirit and power of Elijah. Both registers are active in John's Gospel — the letter denied, the function acknowledged."
      },
      {
        "type": "allusion",
        "target": "Deut 18:15",
        "note": "'The LORD your God will raise up for you a prophet like me from among you — you must listen to him.' 'Are you the Prophet?' invokes this Mosaic figure — a distinct messianic expectation in Second Temple Judaism, separate from both Elijah and the Messiah. The crowd will identify Jesus as this Prophet in 6:14 after the feeding miracle; here John denies occupying the role."
      }
    ],
    "22": [
      {
        "type": "theme",
        "target": "Jer 23:21",
        "note": "'I did not send these prophets, yet they have run with their message; I did not speak to them, yet they have prophesied.' The demand 'What do you say about yourself?' is the form of prophetic authorization-testing. Jeremiah's critique of unauthorized prophets is the framework the interrogators operate within; the OT distinction between sent-by-God and self-appointed is precisely what they are investigating."
      }
    ],
    "24": [
      {
        "type": "theme",
        "target": "Deut 17:9-11",
        "note": "Deuteronomy gives the Levitical priests the authority to 'give you the verdict' in difficult cases — establishing the priestly-legal gatekeeping function in Israel. The Pharisees among the delegation represent the heirs of this interpretive authority. Their role as adjudicators of prophetic claims is structurally legitimate within the covenant; the Evangelist's irony is that they are using a correct procedure to reach a wrong conclusion."
      }
    ],
    "25": [
      {
        "type": "shadow",
        "target": "Ezek 36:25",
        "note": "God promises: 'I will sprinkle clean water on you, and you will be clean; I will cleanse you from all your impurities.' The Pharisees' question assumes baptism is a messianic or prophetic act of purification — they are right. Ezekiel's promise of a divinely-enacted water-cleansing as the prelude to Spirit renewal is exactly the tradition John's baptism inhabits. The questioners understand the symbolic claim; what they cannot accept is its fulfillment."
      }
    ],
    "26": [
      {
        "type": "shadow",
        "target": "Isa 44:3",
        "note": "'I will pour water on the thirsty land, and streams on the dry ground; I will pour out my Spirit on your offspring.' The contrast between John's water baptism and the unrecognized One's Spirit baptism activates the OT stream linking water and Spirit as paired gifts of the new age. Isaiah (44:3), Ezekiel (36:25-27), and Joel (2:28) all converge on this promise; the 'one you do not know' is the one who will make it real."
      }
    ],
    "27": [
      {
        "type": "allusion",
        "target": "Josh 5:15",
        "note": "Before Jericho the commander of the LORD's army says: 'Take off your sandals, for the place where you are standing is holy.' Sandal-removal marks encounters with the divine in the OT — Moses at the burning bush (Exod 3:5), Joshua before the heavenly commander. John's declaration that he is unworthy to unfasten even the sandal strap of the coming one uses this sacred-space language: being near this person is standing on holy ground."
      }
    ],
    "28": [
      {
        "type": "allusion",
        "target": "2 Kgs 2:6-8",
        "note": "Elijah's final journey crossed the Jordan — he struck the water with his rolled cloak and they passed over on dry ground before his translation to heaven. John baptizes at the Jordan in this same region, standing at the geographic site of Elijah's departure. The location signals the hinge moment: the great prophet's era ends at the Jordan; the greater one now arrives at the same threshold."
      }
    ],
    "29": [
      {
        "type": "type",
        "target": "Gen 22:8",
        "note": "Abraham's word to Isaac — 'God himself will provide the lamb' (יִרְאֶה-לּוֹ הַשֶּׂה) — is fulfilled structurally in the Aqedah: a substitute is given at the last moment to avert a death. The binding of Isaac, where God provides the ram in the son's place, prefigures with precision the Lamb God provides to take away the world's sin. The Aqedah is the type; the Passover lamb reinforces it; John the Baptist names the antitype."
      }
    ],
    "30": [
      {
        "type": "theme",
        "target": "Prov 8:22-23",
        "note": "Wisdom: 'I was brought forth before the hills, before the mountains were settled in place.' John's reiteration that the one who comes after him 'existed before me' is the Prologue's pre-existence claim in personal testimony form. The Wisdom tradition's portrait of a divine figure present before all created things — the craftsman beside God at creation — is the OT anticipation the Logos Christology claims to fulfill."
      }
    ],
    "31": [
      {
        "type": "allusion",
        "target": "Isa 40:5",
        "note": "'And the glory of the LORD will be revealed, and all people will see it together.' John states his mission as the revelation of the Messiah to Israel — precisely what Isaiah 40 announces for the day after the herald prepares the way. John's water baptism is the preparatory clearing; the manifestation of Christ at the Jordan is the specific revelation Isaiah envisioned when the divine herald completes his work."
      }
    ],
    "33": [
      {
        "type": "shadow",
        "target": "Joel 2:28-29",
        "note": "'I will pour out my Spirit on all people... even on my servants, both men and women, I will pour out my Spirit.' John identifies the coming one as he who will baptize with the Holy Spirit — the total, universal outpouring Joel announced as the end-time act of God. Pentecost (Acts 2:17) will be Peter's explicit connection of this verse to Joel's prophecy; here it is John the Baptist who first names the one who will fulfil it."
      }
    ],
    "35": [
      {
        "type": "theme",
        "target": "1 Kgs 19:19-21",
        "note": "Elisha was ploughing when Elijah threw his cloak over him; Elisha immediately left his oxen to follow the prophet. The movement of John's disciples toward Jesus echoes the Elijah-Elisha prophetic succession: the forerunner's role is complete when those he has prepared begin following the greater one. The sequence of days in vv29, 35, 43 reinforces the structured handoff."
      }
    ],
    "36": [
      {
        "type": "allusion",
        "target": "Isa 53:7",
        "note": "The repeated proclamation 'Lamb of God' constitutes a second witness (Deut 19:15). Where v29 activates the Passover-lamb type, this second cry invites the Isaiah 53 register: the Suffering Servant led 'like a lamb to the slaughter,' silent before his shearers, whose vicarious suffering removes iniquity. John's double proclamation condenses both the Passover type and the Servant portrait."
      }
    ],
    "37": [
      {
        "type": "theme",
        "target": "Josh 1:16",
        "note": "'Whatever you have commanded us we will do, and wherever you send us we will go.' The disciples' immediate response — hearing and following — enacts the covenant obedience the OT sought. The verbal connection between Joshua (Yehoshua) and Jesus (Iēsous) makes the resonance deliberate: those who hear the greater Joshua and follow are entering the rest the OT prefigured."
      }
    ],
    "38": [
      {
        "type": "allusion",
        "target": "Prov 9:4-5",
        "note": "Wisdom calls: 'Come... eat my food and drink the wine I have mixed.' The disciples' 'Rabbi, where are you staying?' is the opening move of discipleship — asking where the teacher dwells is entry into Wisdom's household. Jesus' 'Come and you will see' (v39) enacts the paradigmatic Wisdom invitation: the house is wherever the Teacher is; learning begins by accepting the summons."
      }
    ],
    "39": [
      {
        "type": "theme",
        "target": "Ps 27:4",
        "note": "'One thing I ask from the LORD... that I may dwell in the house of the LORD all the days of my life.' The disciples spending that day with Jesus anticipates John's developed theology of abiding (ménō, used 40 times in the Gospel). The Psalmist's longing to dwell permanently in the divine presence is now enacted literally: the disciples come, see, and stay — the simplest form of the abiding Christ will later command."
      }
    ],
    "40": [
      {
        "type": "theme",
        "target": "Gen 12:1",
        "note": "'Go from your country, your people and your father's household to the land I will show you.' Andrew's departure from John's circle to follow Jesus echoes the OT pattern of responding to a divine call before the full destination is known. The faith structure that runs from Abraham through every Hebrew call narrative — trust the call without a complete map — is enacted in the disciples' first steps."
      }
    ],
    "41": [
      {
        "type": "allusion",
        "target": "Ps 2:2",
        "note": "Andrew's announcement 'We have found the Messiah (Χριστόν)' uses the Greek equivalent of מָשִׁיחַ from Ps 2:2 — the LORD's anointed Davidic king before whom the nations rage. The Evangelist's parenthetical translation note (Christ = Anointed) signals to Greek readers the full weight of the Hebrew covenant category Andrew has just invoked."
      }
    ],
    "42": [
      {
        "type": "allusion",
        "target": "Gen 17:5",
        "note": "'No longer will you be called Abram; your name will be Abraham, for I have made you a father of many nations.' Divine name-changing in the OT marks a fundamental identity transformation: Abram to Abraham, Jacob to Israel (Gen 32:28). Jesus' renaming of Simon as Cephas/Peter is the same sovereign act — the Lord who knows who each person will become redefines them by the name of what they will be."
      }
    ],
    "43": [
      {
        "type": "allusion",
        "target": "1 Kgs 19:19",
        "note": "Elijah's call of Elisha — throwing his cloak over him while he ploughed — is the paradigmatic OT prophetic call narrative: a single act by the prophet immediately reorients the called person's life. Jesus' terse 'Follow me' is the distilled form of this commissioning: Elijah used a symbolic gesture; Jesus uses a word. The pattern is the same; the authority has intensified."
      }
    ],
    "44": [
      {
        "type": "theme",
        "target": "Isa 9:1-2",
        "note": "'In the future he will honor Galilee of the Gentiles — the people walking in darkness have seen a great light.' Bethsaida lies in Galilee, the region Isaiah specifically designated as the first to receive the light of the coming deliverance. The disciples' Galilean origin situates them geographically in Isaiah's designated territory; Matthew 4:15-16 makes the fulfillment explicit, but John's notices build the same pattern."
      }
    ],
    "46": [
      {
        "type": "allusion",
        "target": "Isa 53:2",
        "note": "The Servant 'grew up like a tender shoot, like a root out of dry ground; he had no beauty or majesty to attract us to him.' Nathanael's contempt — 'Can anything good come from Nazareth?' — echoes the Servant's profile exactly: the obscure provincial origin, lacking the appearance of greatness. God's Servant comes from the kind of place that elicits Nathanael's question; that is the form in which God chose to send him."
      }
    ],
    "47": [
      {
        "type": "allusion",
        "target": "Gen 27:35",
        "note": "In the LXX of Gen 27:35, Isaac says Jacob came 'with deceit (δόλῳ).' Jesus calls Nathanael 'a true Israelite in whom there is no deceit (δόλος).' The word choice is precise: the name Israel came to the father of deceit; Jesus sees in Nathanael the guileless character the name should have always signified. The encounter in v51 will give this true Israelite the very vision Jacob had at Bethel."
      }
    ],
    "48": [
      {
        "type": "allusion",
        "target": "Zech 3:10",
        "note": "'Each of you will invite his neighbor to sit under his vine and fig tree,' says the LORD — a sign of the messianic era of peace and covenant restoration. Nathanael sitting or meditating under the fig tree carries this eschatological resonance; Jesus' supernatural knowledge of him in that intimate space signals the arrival of the era Zechariah promised, present now in the one who knows what no one was there to witness."
      }
    ],
    "49": [
      {
        "type": "allusion",
        "target": "2 Sam 7:14",
        "note": "The Davidic covenant: 'I will be his father, and he will be my son.' Nathanael's twin acclamation — 'Son of God' and 'King of Israel' — maps onto the two poles of this covenant. Divine sonship and Davidic kingship are inseparable in 2 Samuel 7 and Psalm 2; Nathanael confesses in one breath what the entire OT royal-messianic trajectory converges toward."
      }
    ],
    "50": [
      {
        "type": "theme",
        "target": "Isa 64:4",
        "note": "'Since ancient times no one has heard, no ear has perceived, no eye has seen any God besides you, who acts on behalf of those who wait for him.' Jesus' promise that Nathanael will see 'greater things' sets the visual theology for the whole Gospel. The OT horizon is Isaiah's promise that what God will do for those who wait on him exceeds all prior witness; what Nathanael is about to see enters that trajectory."
      }
    ]
  },
  "2": {
    "2": [
      {
        "type": "theme",
        "target": "Isa 62:5",
        "note": "'As a bridegroom rejoices over his bride, so will your God rejoice over you.' Jesus and his disciples attending a wedding places the Cana sign within the OT's dominant metaphor for God's covenant relationship with Israel. The divine-marriage motif runs through Isaiah, Hosea (2:16-20), and Ezekiel (16:8-14); John's opening sign at a wedding sits within this symbolic field and anticipates the marriage supper of the Lamb (Rev 19:9)."
      }
    ],
    "3": [
      {
        "type": "theme",
        "target": "Amos 9:13-14",
        "note": "Amos promises that in the restoration era 'new wine will drip from the mountains and flow from all the hills.' The depletion of wine at the wedding is not merely social embarrassment — it represents the exhausted state of the old order. Amos's eschatological wine-abundance makes the 'no wine' theologically resonant: the messianic sign will replace the old order's emptiness with the new age's overflow."
      }
    ],
    "4": [
      {
        "type": "theme",
        "target": "Hab 2:3",
        "note": "'For the revelation awaits an appointed time; it speaks of the end and will not prove false. Though it linger, wait for it; it will certainly come.' Jesus' 'my hour has not yet come' introduces the central Johannine category of the divinely appointed hour — recurring through the Gospel (7:30; 8:20; 12:23; 13:1). The OT background is prophetic expectation of a fixed divine time (Hab 2:3; Dan 8:19); Jesus operates within this timetable, not outside it."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Gen 41:55",
        "note": "Pharaoh's instruction to the famine-stricken Egyptians — 'Go to Joseph and do what he tells you' — is structurally parallel to Mary's 'Do whatever he tells you.' Joseph was the providential figure through whom life came to Egypt in a time of depletion; Jesus at Cana is the greater provider who gives abundance where the old supply has run out."
      }
    ],
    "6": [
      {
        "type": "theme",
        "target": "Lev 11:33",
        "note": "Levitical purity law held that clay vessels could contract impurity and must be broken, while stone vessels could not contract impurity. Stone water jars were therefore preferred for water used in purification rites. That the vessels of Jewish ritual cleansing become the vessels of messianic abundance is John's sign-theology in concentrated form: the water of Levitical purification gives way to the wine of the new-covenant celebration."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "1 Kgs 18:33-35",
        "note": "Before the Carmel contest Elijah ordered the stone jars filled with water three times until the water ran into the trench — a complete, unambiguous filling before the divine act descended. The servants at Cana filling the jars to the brim before the transformation echoes Elijah's protocol: the ordinary substance is used fully, forestalling any charge of manipulation, before the miraculous act overrides it."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Gen 24:19-20",
        "note": "At the well outside Nahor, Rebekah drew water for Abraham's servant and his camels — a repeated act of drawing that preceded the covenant marriage she secured. The servants drawing from the stone jars and bringing it to the master of the banquet echo this drawing-at-a-well pattern embedded in a wedding context: both scenes pivot on the act of drawing provision that enables the celebration."
      }
    ],
    "9": [
      {
        "type": "theme",
        "target": "Ps 78:24-25",
        "note": "'He rained down manna for the people to eat... mortals ate the bread of angels.' The master of the banquet receives the miraculous provision without knowing its source, while the servants who drew the water know. Israel received manna without initially understanding it (Exod 16:14-15: 'What is it?'). Hidden divine provision that confounds the official while the servants recognize it is a recurring OT pattern."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Isa 25:6",
        "note": "Isaiah's vision of the eschatological banquet: 'a feast of rich food for all peoples, a banquet of aged wine — the best of meats and the finest of wines.' The master's observation 'you have saved the best till now' is the sign's theological punchline, activating this OT pattern of eschatological abundance surpassing all prior celebration. Messianic feast does not deplete but reserves the best; the old order's logic is reversed."
      }
    ],
    "12": [
      {
        "type": "theme",
        "target": "Isa 9:1-2",
        "note": "'In the future he will honor Galilee of the Gentiles — the people walking in darkness have seen a great light.' Capernaum on the Sea of Galilee is briefly noted as the resting place before the Jerusalem Passover. The movement into Galilee continues to fulfill the Isaiah 9:1-2 pattern — the region Isaiah designated for the first light of messianic salvation is exactly where Jesus is staying between signs."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Zech 14:21",
        "note": "Zechariah's vision of the eschatological temple ends: 'There will no longer be a trader (Canaanite) in the house of the LORD Almighty on that day.' The presence of cattle-dealers, dove-sellers, and money-changers in the courts is exactly what Zechariah promised to end. Jesus' temple action is not primarily a moral protest against dishonest commerce; it is an eschatological act fulfilling Zechariah's specific declaration."
      }
    ],
    "15": [
      {
        "type": "allusion",
        "target": "Mal 3:2-3",
        "note": "'But who can endure the day of his coming? Who can stand when he appears? For he will be like a refiner's fire... He will purify the Levites.' Malachi's vision of the Lord arriving at the temple as purifying judgment is enacted here. The whip of cords, the scattered coins, and the overturned tables are the refiner's fire in action — the sudden purifying arrival Malachi promised, too powerful for the commercial enterprise to withstand."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "Isa 56:7",
        "note": "'My house will be called a house of prayer for all nations.' Jesus' rebuke — 'stop making my Father's house a marketplace' — is rooted in this text (cited explicitly in the Synoptic cleansing accounts). The market system in the court of the Gentiles is precisely the obstacle to the universal-access house of prayer Isaiah envisioned; the 'market' displaces the 'prayer' that was always the Father's intention."
      }
    ],
    "18": [
      {
        "type": "theme",
        "target": "Exod 4:1-9",
        "note": "God gives Moses authenticating signs so that Israel will believe he was sent: the staff-to-serpent, the leprous hand, the water-to-blood. The authorities' demand for a sign to prove Jesus' authority is the standard OT framework for prophetic validation — a structurally legitimate request within the covenant. The irony is that the sign Jesus will give (resurrection in three days) is the one they will refuse to receive."
      }
    ],
    "20": [
      {
        "type": "theme",
        "target": "1 Kgs 6:37-38",
        "note": "Solomon's temple was laid in the fourth year and completed in the eleventh — seven years of concentrated national effort and divine design. The authorities invoke Herod's long reconstruction (begun ~19 BCE) to make Jesus' three-day claim absurd. The human investment in the stone temple is real and immense. What the authorities cannot see is that Jesus is not speaking of stone and cedar."
      }
    ],
    "21": [
      {
        "type": "shadow",
        "target": "Ezek 37:26-27",
        "note": "God promises: 'I will put my sanctuary among them forever... I will be their God, and they will be my people.' Ezekiel's vision of the eschatological divine dwelling permanently among the people is the OT trajectory the body-as-temple claim fulfills. The temple as the meeting point of God and humanity — its function since Eden and Sinai — is now permanently and personally embodied in the risen Christ (cf. John 1:14)."
      }
    ],
    "22": [
      {
        "type": "allusion",
        "target": "Ps 16:10",
        "note": "'You will not abandon me to the realm of the dead, nor will you let your faithful one see decay.' When the disciples 'believed the scripture' after the resurrection, the primary scriptural anchor was this psalm (Acts 2:27-31; Acts 13:35 both cite Ps 16:10 as the resurrection proof-text). The temple/body saying is verified by a scripture the disciples had always possessed but now understood differently."
      }
    ],
    "23": [
      {
        "type": "theme",
        "target": "Exod 4:30-31",
        "note": "Aaron performed the LORD's signs before the people 'and they believed.' The pattern of signs producing belief follows the Exodus template. John carefully records the crowd's belief-response, but the following verses complicate it — Jesus knows this belief is sign-dependent and shallow, just as Israel's sign-induced belief in the wilderness repeatedly proved fragile under pressure (Ps 78:32-37)."
      }
    ],
    "24": [
      {
        "type": "theme",
        "target": "Jer 17:9-10",
        "note": "'The heart is deceitful above all things and beyond cure. Who can understand it? I the LORD search the heart and examine the mind.' Jesus' refusal to entrust himself to the believing crowds draws on the OT's realism about human nature. Only the LORD searches hearts (Ps 139:1-4; 1 Sam 16:7); Jesus sharing this divine knowledge is John's understated presentation of identity."
      }
    ],
    "25": [
      {
        "type": "theme",
        "target": "1 Sam 16:7",
        "note": "'The LORD does not look at the things people look at. People look at the outward appearance, but the LORD looks at the heart.' John's summary — Jesus needed no human testimony because he knew what was in each person — is the divine prerogative God claims throughout the OT. Sharing this knowledge marks Jesus as the one who sees as God sees; the chapter closes on this identification."
      }
    ]
  }
}


def main():
    existing = load_echo('john')
    merge_echo(existing, JOHN_ECHOES)
    save_echo('john', existing)
    print('John 1–2 echoes written.')

if __name__ == '__main__':
    main()
