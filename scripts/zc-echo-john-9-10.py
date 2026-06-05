"""
MKT Echo — John chapters 9–10
Run: python3 scripts/zc-echo-john-9-10.py

Source data used:
- data/interlinear/john.json
- data/translation/draft/mediating/john.json (MKT text for quoting)
- data/parallels/john.json (ch 9 had no entries; ch 10 had 3 — absorbed below)

Key decisions in this range:
- John 9:6 (Gen 2:7): classified `allusion` — the use of clay/spittle to
  restore sight deliberately echoes the creation of the first man from dust;
  the Evangelist frames the healing as a new-creation act, not mere miracle.
- John 9:7 (Isa 8:6 / 2 Kgs 5): Siloam/Shiloah connection classified `allusion`
  — the pool name ('Sent') carries the Evangelist's signature Sent-Father
  theology; the Naaman parallel added as `type` (Gentile healed at prophet's
  word with the same hesitant-obedience structure).
- John 9:24 (Josh 7:19): `quote` would be too strong — the formula 'Give glory
  to God' is a covenantal oath formula present in Joshua's Achan scene; classified
  `allusion` since the Pharisees may be using a stock formula, but the irony
  Johannine readers catch is the echo of forced confession.
- John 9:35 (Dan 7:13): `allusion` — Jesus uses 'Son of Man' as a self-
  designation with clear Daniel background; classified allusion not fulfillment
  since the Evangelist does not explicitly cite Dan 7 here.
- John 10:11 (Ps 23; Ezek 34; Isa 53): all three retained — Psalm 23 is the
  devotional shepherd psalm; Ezek 34 is the prophetic promise that God himself
  will shepherd; Isa 53 provides the 'life laid down for the flock' pattern.
  Together they establish the three registers of the claim.
- John 10:30 (Deut 6:4; Isa 44:6): the Shema provides the ontological shock
  and Deutero-Isaiah the theological framework. Both classified `allusion` —
  Jesus does not cite these texts, but the claim lands against their background.
- John 10:34 (Ps 82:6): `quote` — the only direct citation in these two chapters;
  absorbed from parallels file.
- Parallels absorbed:
    10:11 Ps 23:1 (allusion → shadow) + Ezek 34:11-16 (prophecy-source → type)
    10:16 Ezek 37:24-25 (prophecy-source → type)
    10:34 Ps 82:6 (quotation → quote)
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
  "9": {
    "1": [
      {"type": "fulfillment", "target": "Isa 35:5",
       "note": "Isaiah's messianic sign — 'then the eyes of the blind will be opened' — is enacted in this episode. John 9 is the narrative demonstration that the one Isaiah predicted has arrived; the physical healing is the credential the Servant's mission was to display."},
      {"type": "allusion", "target": "Isa 42:7",
       "note": "The Servant is commissioned to 'open eyes that are blind.' John frames the healing from birth as the Servant's specific mandate fulfilled — not merely a compassionate miracle but an identity disclosure about who Jesus is."}
    ],
    "2": [
      {"type": "theme", "target": "Ezek 18:20",
       "note": "The disciples assume a direct sin-causation model: 'the one who sins is the one who will die; the child will not share the guilt of the parent.' The question reflects a popular application of covenantal retribution theology; Jesus' answer does not contradict Ezekiel but reframes the particular case."},
      {"type": "theme", "target": "Job 4:7",
       "note": "Eliphaz's retributive premise — 'consider now: who, being innocent, has ever perished?' — is the theological assumption embedded in the disciples' question. The book of Job is precisely the refutation of this simplistic calculus, a refutation Jesus endorses."}
    ],
    "3": [
      {"type": "allusion", "target": "Exod 9:16",
       "note": "God tells Moses that Pharaoh's hard case exists 'for this very purpose, that I might show you my power and that my name might be proclaimed in all the earth.' The structural parallel is exact: a seemingly intractable situation (pharaoh's hardness / the man's congenital blindness) is providentially arranged so that God's works may be made manifest."},
      {"type": "theme", "target": "Ps 46:10",
       "note": "'Be still, and know that I am God; I will be exalted among the nations.' The phrase 'works of God might be displayed' points to the same divine-glorification theme: crises that seem opaque to human causation are the theater in which God makes himself known."}
    ],
    "4": [
      {"type": "allusion", "target": "Jer 13:16",
       "note": "'Give glory to the Lord your God before he brings the darkness, before your feet stumble on the darkening hills.' Jeremiah's urgent warning to work while daylight lasts is the OT register Jesus activates: the time for the works of God is bounded; the night of judgment or death closes the window."},
      {"type": "allusion", "target": "Amos 8:9",
       "note": "'I will make the sun go down at noon and darken the earth in broad daylight.' Amos's day-of-the-Lord reversal — unexpected darkness — echoes in Jesus' night-is-coming warning. The urgency is eschatological, not merely biographical."}
    ],
    "5": [
      {"type": "fulfillment", "target": "Isa 42:6",
       "note": "The Servant is appointed as 'a light for the Gentiles' — precisely the role Jesus claims: 'I am the light of the world.' The Evangelist has Jesus speak the Servant's commission in the first person, making the identification explicit."},
      {"type": "allusion", "target": "Ps 27:1",
       "note": "'The Lord is my light and my salvation — whom shall I fear?' The Psalmic identification of the Lord as light is here embodied: the claim 'I am the light' is a divine-presence claim, not merely a metaphor for teaching or moral example."}
    ],
    "6": [
      {"type": "allusion", "target": "Gen 2:7",
       "note": "God forms the first man by taking dust from the ground (אֲדָמָה) and breathing life into him. Jesus takes dust, adds saliva, applies clay to dead eyes — the healing recapitulates the original creation act, presenting Jesus as the one through whom the Creator's power still works to form and restore human faculties."},
      {"type": "allusion", "target": "Isa 45:9",
       "note": "'Woe to those who quarrel with their Maker... Does the clay say to the potter, what are you making?' The potter-and-clay relationship governs the Isaian theology of divine sovereignty in re-creation. Jesus' use of clay invokes this register: the blind man is clay reshaped by the potter's hands."}
    ],
    "7": [
      {"type": "allusion", "target": "Isa 8:6",
       "note": "The name 'Siloam' translates the Hebrew שִׁלֹחַ (Shiloah) — the gently flowing channel whose waters Isaiah uses as a figure for Yahweh's quiet provision (against Assyria's flooding power). The pool named 'Sent' carries the Evangelist's theology of mission: the one whom the Father sent sends the man to the pool whose name encodes that mission."},
      {"type": "type", "target": "2 Kgs 5:14",
       "note": "Naaman the Syrian — afflicted, told by the prophet's messenger to wash in the Jordan, initially resistant, but compliant and healed — is the structural type. Like Naaman, the blind man is given a word of command (Go, wash), obeys without explanation, and returns whole. Both healings prefigure the obedience-of-faith that receives what God's word promises."}
    ],
    "8": [
      {"type": "theme", "target": "Isa 29:18",
       "note": "Isaiah's messianic promise — 'in that day the deaf will hear the words of the scroll, and out of gloom and darkness the eyes of the blind will see' — is visible in the neighbors' bewildered interrogation: is this really the man who sat begging? The recognizable fulfillment of prophecy produces not immediate worship but baffled questioning."}
    ],
    "11": [
      {"type": "allusion", "target": "Isa 43:10",
       "note": "'You are my witnesses, declares the Lord.' The man's report — 'the man they call Jesus made mud, told me to go wash, and I can see' — is the simplest form of the witness commission Isaiah announces: direct personal testimony to what the Lord has done, produced by those who have experienced the salvation themselves."}
    ],
    "14": [
      {"type": "theme", "target": "Exod 20:10",
       "note": "The Sabbath prohibition against work (מְלָאכָה) is the center of the legal controversy: Jesus made mud on the Sabbath, which rabbinic interpretation classified as prohibited kneading. The Evangelist marks the Sabbath detail precisely because it drives the conflict — not despite the law but because the healer exceeds it."}
    ],
    "16": [
      {"type": "theme", "target": "Deut 13:2",
       "note": "The Pharisaic logic — a sign-worker who does not keep the law cannot be from God — applies Deuteronomy's test for false prophets: a prophet who leads Israel away from the commandments is not to be followed, even if his signs come true. Jesus' answer throughout John is that his signs confirm rather than contradict the Father's will."},
      {"type": "allusion", "target": "Exod 31:13",
       "note": "The Sabbath is a sign of the covenant between God and Israel: 'You must observe my Sabbaths. This will be a sign between me and you for the generations to come.' The Pharisees read the Sabbath breach as covenant-sign violation; Jesus reads his healing as the covenant God's own work continuing."}
    ],
    "17": [
      {"type": "allusion", "target": "Deut 18:15",
       "note": "The man's verdict — 'he is a prophet' — applies the Mosaic category for authenticated divine messengers: 'The Lord your God will raise up for you a prophet like me from among you.' The formerly blind man reaches the right category through the right channel (the evidence of the sign) before he knows enough to reach the full truth."}
    ],
    "22": [
      {"type": "theme", "target": "Ezra 10:8",
       "note": "Ezra's post-exilic assembly threatened expulsion from the congregation for those who did not comply with the community's decree. The Johannine ἀποσυνάγωγος (expulsion from the synagogue) is the same coercive mechanism: exclusion from the covenant community as punishment for non-compliance with the leaders' ruling."}
    ],
    "24": [
      {"type": "allusion", "target": "Josh 7:19",
       "note": "'Give glory to God' (δὸς δόξαν τῷ θεῷ) is the precise phrase Joshua uses when pressing Achan to confess: 'Give glory to the Lord, the God of Israel, and give him the praise. Tell me what you have done.' The Pharisees are using a covenantal oath formula — speak the truth before God — while ironically pressuring the man to contradict what God has done through him."}
    ],
    "25": [
      {"type": "theme", "target": "Ps 40:2",
       "note": "'He lifted me out of the slimy pit, out of the mud and mire; he set my feet on a rock.' The blind man's unforgettable testimony — 'I was blind but now I see' — has the structure of the individual lament-turned-praise: a fixed prior state of helplessness, an unexpected divine act, and an irreversible present reality that the sufferer simply reports."}
    ],
    "28": [
      {"type": "allusion", "target": "Deut 34:10",
       "note": "'Since then, no prophet has risen in Israel like Moses, whom the Lord knew face to face.' The Pharisees' claim — 'we are disciples of Moses' — invokes Israel's highest authority, the covenant mediator whom God knew uniquely. The irony the Evangelist highlights: Moses wrote about Jesus (5:46), so discipleship to Moses should lead toward him."}
    ],
    "29": [
      {"type": "allusion", "target": "Num 12:8",
       "note": "'With him I speak face to face, clearly and not in riddles; he sees the form of the Lord.' The Pharisees anchor their certainty about Moses in the Mosaic privilege of direct divine speech. The blind-man episode implicitly answers: the one who healed him speaks with at least the same divine authority — and the Pharisees' refusal to recognize this is the blindness Jesus diagnoses."}
    ],
    "31": [
      {"type": "allusion", "target": "Ps 66:18",
       "note": "'If I had cherished sin in my heart, the Lord would not have listened.' The man's theological argument — 'God does not listen to sinners, but to those who do his will' — draws on a principle the Psalms and Proverbs consistently assert: the moral prerequisites for effective prayer. The man uses Israel's own wisdom to convict the Pharisees."},
      {"type": "allusion", "target": "Prov 15:29",
       "note": "'The Lord is far from the wicked, but he hears the prayer of the righteous.' The man's logic is textbook proverbial wisdom: if Jesus performed this sign, God answered his prayer; if God answered his prayer, Jesus is not the kind of sinner who is cut off from God's hearing."}
    ],
    "32": [
      {"type": "fulfillment", "target": "Isa 29:18",
       "note": "'In that day the deaf will hear... out of gloom and darkness the eyes of the blind will see.' The man's observation that 'nobody has ever heard of opening the eyes of a man born blind' frames the healing as unprecedented precisely because Isaiah's fulfillment is unprecedented — a messianic sign that marks the 'day' Isaiah foresaw."}
    ],
    "34": [
      {"type": "allusion", "target": "Ps 51:5",
       "note": "'Surely I was sinful at birth, sinful from the time my mother conceived me.' The Pharisees weaponize this Psalmic acknowledgment of universal sinfulness — 'you were steeped in sin at birth' — but perversely: they invoke it not as honest self-knowledge but as a cudgel to dismiss his testimony and his healer. The expulsion completes the judicial irony: they who try the innocent cast him out."}
    ],
    "35": [
      {"type": "allusion", "target": "Dan 7:13",
       "note": "Jesus' question — 'Do you believe in the Son of Man?' — activates the Danielic figure: 'one like a son of man, coming with the clouds of heaven, approached the Ancient of Days and was led into his presence... given authority, glory and sovereign power.' The title is a claim about heavenly enthronement and universal dominion, not merely a humble self-designation; the man's worship (v. 38) becomes the appropriate response to the Daniel figure."}
    ],
    "37": [
      {"type": "allusion", "target": "Isa 52:6",
       "note": "'Therefore my people will know my name; therefore in that day they will know that it is I who said, Here I am.' Jesus' self-disclosure — 'you have seen him; he is the one speaking with you' — has the same self-revelation structure as the Isaianic divine name announcement: the one who speaks identifies himself as the one long sought."}
    ],
    "38": [
      {"type": "theme", "target": "Ps 95:6",
       "note": "'Come, let us bow down in worship, let us kneel before the Lord our Maker.' The man's worship (προσεκύνησεν) of Jesus is the fitting response to an encounter with the one who has authority over creation's broken faculties. The Psalm's call to worship the Creator is enacted when the creature restored by Jesus falls before him."}
    ],
    "39": [
      {"type": "allusion", "target": "Isa 6:10",
       "note": "The hardening oracle — 'make the heart of this people calloused; make their ears dull and close their eyes' — is activated by Jesus' judgment statement. Those who see themselves as sighted are given over to the blindness they have chosen; the oracle becomes a description of what encounter with the light produces in those who refuse it."},
      {"type": "allusion", "target": "Isa 29:9",
       "note": "'Stagger, but not from wine; stumble, but not from beer. The Lord has brought over you a deep sleep.' Isaiah's portrait of judicial blindness — not natural impairment but God's response to willful refusal — is the theological register of 10:26 as well as 9:39: those who 'see' and still reject are the ones on whom the judiciary blindness falls."}
    ],
    "41": [
      {"type": "allusion", "target": "Jer 5:21",
       "note": "'Hear this, you foolish and senseless people, who have eyes but do not see, who have ears but do not hear.' Jeremiah's diagnostic applies to the Pharisees exactly: their functional sight coexists with functional blindness — organic faculties present, perception of God's work absent. Jesus confirms that this kind of blindness cannot claim the innocence of the congenital sort."},
      {"type": "allusion", "target": "Deut 29:4",
       "note": "'To this day the Lord has not given you a mind that understands or eyes that see or ears that hear.' Moses acknowledged that physical Exodus-witnesses could still lack the spiritual sight to perceive. The Pharisees are the canonical inheritors of this diagnosis: they have seen the sign and understood nothing."}
    ]
  },

  "10": {
    "1": [
      {"type": "allusion", "target": "Jer 23:1",
       "note": "'Woe to the shepherds who are destroying and scattering the sheep of my pasture!' Jesus' thief-and-robber figure is directed at the Pharisees who have just expelled the healed man (9:34). The unauthorized entry — bypassing the gate — names what Jeremiah named: false leadership that exploits rather than tends."},
      {"type": "allusion", "target": "Ezek 34:2",
       "note": "Ezekiel's oracle against Israel's shepherds who 'slaughter the choice animals' and scatter the flock provides the prophetic background for John 10's binary of legitimate versus illegitimate shepherds. The Pharisees stand in the position Ezekiel condemned; Jesus stands in the position of the one Ezekiel promised."}
    ],
    "2": [
      {"type": "allusion", "target": "Ezek 34:23",
       "note": "'I will place over them one shepherd, my servant David, and he will tend them.' The Evangelist's claim is implicit: the shepherd who enters by the gate is the Davidic shepherd Ezekiel promised — legitimate, sent, and recognized by the flock rather than forcing himself upon it."}
    ],
    "3": [
      {"type": "allusion", "target": "Isa 43:1",
       "note": "'I have summoned you by name; you are mine.' The shepherd calling his own sheep by name mirrors the divine naming that constitutes ownership and covenant protection. The sheep hearing their name is not mere recognition; it is covenantal belonging — being known as one whom the shepherd has claimed."},
      {"type": "theme", "target": "Ps 95:7",
       "note": "'He is our God and we are the people of his pasture, the flock under his care. Today, if only you would hear his voice.' The Psalm's summons — hear his voice today — anticipates the governing theme of the discourse: the sheep-Father relationship depends precisely on this hearing."}
    ],
    "4": [
      {"type": "theme", "target": "Ps 77:20",
       "note": "'You led your people like a flock by the hand of Moses and Aaron.' The image of the shepherd going before the flock — with the sheep following because they know his voice — picks up the Exodus pattern: the Lord leading Israel through wilderness ahead of them, with the flock following the known presence."}
    ],
    "7": [
      {"type": "allusion", "target": "Ps 118:20",
       "note": "'This is the gate of the Lord through which the righteous may enter.' Jesus' 'I am the gate' (ἐγώ εἰμι ἡ θύρα) claims the role the Psalmic gate plays: the single legitimate point of entry into covenant blessing. Access to the Father comes through the one gate; the gate is not a structure but a person."},
      {"type": "allusion", "target": "Gen 28:17",
       "note": "Jacob declares the place of his dream 'the gate of heaven' (שַׁעַר הַשָּׁמָיִם). The image of a gate as the boundary between earth and the divine presence is anchored in the patriarchal narrative; Jesus claims to be that gate — not a place but the relational threshold."}
    ],
    "9": [
      {"type": "allusion", "target": "Ps 23:2",
       "note": "'He makes me lie down in green pastures, he leads me beside quiet waters.' Jesus' promise — 'they will come in and go out and find pasture' — enacts the shepherd psalm's picture of the flock's security and abundance. The sheep who enter through Jesus find what the psalm promises: safe movement and provision."},
      {"type": "fulfillment", "target": "Isa 49:10",
       "note": "'They will neither hunger nor thirst... for he who has compassion on them will guide them and lead them beside springs of water.' The gathering of the scattered sheep who find pasture through the true shepherd fulfills the Servant's mission to gather Israel and lead them to abundance."}
    ],
    "10": [
      {"type": "allusion", "target": "Ezek 34:4",
       "note": "'You have not strengthened the weak or healed the sick... but you have ruled them harshly and brutally.' The thief who 'comes only to steal and kill and destroy' names what Ezekiel's condemned shepherds actually do. Jesus' contrast — he comes for life in abundance — is the fulfillment of Ezekiel's promise that God himself will replace the exploitative shepherds."}
    ],
    "11": [
      {"type": "shadow", "target": "Ps 23:1",
       "note": "The entire psalm — 'The Lord is my shepherd, I lack nothing' — is the devotional background for Jesus' 'I am the good shepherd.' The Psalm's speaker trusts the shepherd through the valley of death; the Shepherd of John 10 enacts that protection by entering the valley himself, laying down his life so that the flock need not fear it."},
      {"type": "type", "target": "Ezek 34:11",
       "note": "'For this is what the Sovereign Lord says: I myself will search for my sheep and look after them.' God's promise to shepherd Israel in person — replacing the false shepherds — is fulfilled when Jesus identifies himself as the shepherd who gives his life. The Ezekiel promise reaches beyond a human king to the Lord himself; Jesus' claim is exactly this."},
      {"type": "allusion", "target": "Isa 53:7",
       "note": "The Servant led as a lamb to slaughter, not opening his mouth — the iconic image of voluntary sacrifice — is the background for 'the good shepherd lays down his life.' The Servant pattern (willing death, for others) is enacted in the Shepherd's self-giving; later, 1 Pet 2:25 makes the identification explicit."}
    ],
    "12": [
      {"type": "allusion", "target": "Zech 13:7",
       "note": "'Strike the shepherd, and the sheep will be scattered.' Zechariah's oracle — which Jesus cites at his arrest (Matt 26:31) — identifies the shepherd's removal as the cause of the flock's scattering. The hireling of John 10:12 enacts the same dynamic: when danger comes, the flock is left exposed. The irony is that Jesus, the true shepherd, will himself be struck (Zech 13:7), but in fulfilling rather than abandoning his role."},
      {"type": "allusion", "target": "Ezek 34:5",
       "note": "'So they were scattered because there was no shepherd, and when they were scattered they became food for all the wild animals.' The wolf that scatters the untended flock is Ezekiel's exact image; John 10:12 imports it directly to describe the inadequacy of any leadership that is merely occupational rather than covenantal."}
    ],
    "14": [
      {"type": "allusion", "target": "Jer 31:34",
       "note": "'No longer will they teach their neighbor, or say to one another, Know the Lord, because they will all know me, from the least of them to the greatest.' The mutual knowing between shepherd and sheep — 'I know my sheep and my sheep know me' — is the pastoral instantiation of the new-covenant knowing Jeremiah promised: not mediated instruction but direct, personal, reciprocal knowledge."},
      {"type": "allusion", "target": "Isa 43:1",
       "note": "'I have summoned you by name; you are mine.' The intimacy of naming and knowing is covenantal possession. Jesus' 'I know my sheep' is the Johannine analogue of God's individual naming in Isaiah — the sheep are not anonymous members of a category but known persons held within the shepherd's care."}
    ],
    "16": [
      {"type": "type", "target": "Ezek 37:24",
       "note": "'My servant David will be king over them, and they will all have one shepherd.' Ezekiel's vision of reunited Israel under the Davidic shepherd — the two sticks (Israel and Judah) becoming one — expands in Jesus' 'one flock, one shepherd' to include Gentiles. The typological pattern is identical: divine gathering of the scattered into a unified flock under one leader."},
      {"type": "fulfillment", "target": "Isa 56:8",
       "note": "'The Sovereign Lord declares — he who gathers the exiles of Israel: I will gather still others to them besides those already gathered.' The 'other sheep not of this sheep pen' are the Gentiles Isaiah's universalism anticipated. Jesus here announces the fulfillment: the gathering of the nations alongside Israel under one shepherd."},
      {"type": "allusion", "target": "Mic 2:12",
       "note": "'I will surely gather all of you, Jacob; I will surely bring together the remnant of Israel... like a flock in its pasture.' Micah's gathering-and-pasturing image uses the same flock/pasture cluster. The 'one flock and one shepherd' formula is the eschatological completion of what Micah foresaw: scattered ones gathered into a unified, tended community."}
    ],
    "17": [
      {"type": "allusion", "target": "Isa 53:10",
       "note": "'Yet it was the Lord's will to crush him and cause him to suffer, and though the Lord makes his life an offering for sin, he will see his offspring and prolong his days.' The Father's love expressed through the Son's death and resurrection — 'I lay it down and I take it up again' — follows the Servant pattern: the death is voluntary and purposive, and the prolonged life follows the offering."}
    ],
    "18": [
      {"type": "allusion", "target": "Ps 40:8",
       "note": "'I desire to do your will, my God; your law is within my heart.' Jesus' authority to lay down his life and take it up is not autonomous will but received command from the Father — the same interior alignment the Psalm describes. The cross is not imposed from outside but embraced from within, in complete harmony with the Father's will."},
      {"type": "allusion", "target": "Isa 53:12",
       "note": "'He poured out his life unto death.' The Servant's self-giving death is not taken but poured out — a willing expenditure. Jesus' insistence that 'no one takes it from me, but I lay it down of my own accord' is the Johannine formulation of the Servant's voluntary self-offering."}
    ],
    "19": [
      {"type": "allusion", "target": "Isa 8:14",
       "note": "'He will be a stone that causes people to stumble and a rock that makes them fall... for both Israel and Judah.' The division Jesus provokes (σχίσμα) fulfills Isaiah's paradox: the Holy One of Israel is simultaneously a sanctuary and a stone of stumbling. The same encounter produces opposite responses — just as Isaiah predicted."}
    ],
    "22": [
      {"type": "theme", "target": "1 Kgs 8:10",
       "note": "The Festival of Dedication (Hanukkah) commemorates the rededication of the temple after Antiochus IV desecrated it (167 BCE), re-enacting Solomon's original dedication when the divine glory filled the house. The setting — Jesus in the temple courts at the festival celebrating divine presence — is loaded: the one who embodies that presence walks among the commemorations of its return."}
    ],
    "24": [
      {"type": "theme", "target": "Dan 9:25",
       "note": "'Know and understand this: from the issuing of the decree to restore and rebuild Jerusalem until the Anointed One, the ruler, comes.' The crowd's demand — 'if you are the Messiah, tell us plainly' — reflects Jewish expectation of an unambiguous messianic declaration. Daniel's 'anointed one' creates the category they are pressing Jesus to fill; Jesus' answer is that the works already testify."}
    ],
    "25": [
      {"type": "theme", "target": "Deut 18:22",
       "note": "'If what a prophet proclaims in the name of the Lord does not take place or come true, that is a message the Lord has not spoken.' The inverse also holds: if the works of Jesus come to pass, they authenticate his mission in the Father's name. Jesus appeals to the Deuteronomic validation criterion — not self-assertion but demonstrated acts."}
    ],
    "26": [
      {"type": "allusion", "target": "Isa 6:9",
       "note": "'Be ever hearing, but never understanding; be ever seeing, but never perceiving.' Jesus' diagnosis — 'you do not believe because you are not my sheep' — is the Johannine equivalent of the Isaiah hardening oracle: inability to hear the shepherd's voice is itself the judicial sign of being outside the flock."}
    ],
    "27": [
      {"type": "theme", "target": "Ps 95:7",
       "note": "'Today, if only you would hear his voice, do not harden your hearts.' The psalm's urgency — hear the voice now, today — is fulfilled in its negative in the leaders' refusal. Jesus' sheep do what the psalm commanded: they hear and follow. The psalm's warning (hardening of heart) is what the questioners demonstrate."}
    ],
    "28": [
      {"type": "allusion", "target": "Isa 43:13",
       "note": "'Yes, and from ancient days I am he. No one can deliver out of my hand. When I act, who can reverse it?' Jesus' 'no one will snatch them out of my hand' transfers to himself the divine attribute Isaiah asserts for the Lord: absolute protection against dispossession. The same hand that cannot be overcome in Isaiah is the hand of the Good Shepherd."},
      {"type": "theme", "target": "Ps 23:6",
       "note": "'Surely your goodness and love will follow me all the days of my life, and I will dwell in the house of the Lord forever.' The eternal life Jesus gives — 'they shall never perish' — enacts the permanence the shepherd psalm promises. The guarantee is not conditional on the sheep's grip but on the shepherd's."}
    ],
    "29": [
      {"type": "allusion", "target": "Deut 33:3",
       "note": "'Surely it is you who love the peoples; all your holy ones are in your hand.' Moses' blessing at his death grounds holy-ones-in-the-divine-hand as an expression of covenant protection. Jesus elevates this: neither his hand nor the Father's hand can be overcome, because both the Son and the Father hold the flock."}
    ],
    "30": [
      {"type": "allusion", "target": "Deut 6:4",
       "note": "'Hear, O Israel: The Lord our God, the Lord is one.' Jesus' claim 'I and the Father are one' is spoken in the context of Hanukkah (the feast celebrating rescue from pagan oppression) to an audience whose entire theological identity rests on the Shema. The declaration does not contradict monotheism — it redefines where unity of divine action is located."},
      {"type": "allusion", "target": "Isa 44:6",
       "note": "'This is what the Lord says — Israel's King and Redeemer, the Lord Almighty: I am the first and I am the last; apart from me there is no God.' Deutero-Isaiah's absolute monotheism — no other God exists — is the background that makes Jesus' Father-Son unity claim both shocking and precise: he claims the relational unity that Yahweh's uniqueness entails."}
    ],
    "31": [
      {"type": "allusion", "target": "Lev 24:16",
       "note": "'Anyone who blasphemes the name of the Lord is to be put to death. The entire assembly must stone them.' The crowd's intent — picking up stones — is the prescribed Levitical response to blasphemy. The charge makes precise legal sense to them: a human claiming divine identity has, in their framework, committed the capital offense."}
    ],
    "34": [
      {"type": "quote", "target": "Ps 82:6",
       "note": "Jesus directly cites the psalm — 'I have said you are gods' — in response to the blasphemy charge. Psalm 82 pictures God addressing human judges who bear his authority: they are called 'gods' (אֱלֹהִים) because they exercise divine judgment. If the lesser instance (appointed human judges) can bear the divine title without blasphemy, the greater instance (the one the Father set apart and sent) must also sustain the claim."}
    ],
    "35": [
      {"type": "theme", "target": "Isa 40:8",
       "note": "'The grass withers and the flowers fall, but the word of our God endures forever.' Jesus' 'scripture cannot be set aside' (broken/λυθῆναι) picks up the Isaianic conviction about the permanent, unoverrideable authority of the divine word. The argument from the unbreakable nature of Scripture is grounded in its source: the God who endures."},
      {"type": "allusion", "target": "Ps 119:89",
       "note": "'Your word, Lord, is eternal; it stands firm in the heavens.' The permanence of God's word is the premise of Jesus' qal va-homer argument: if Scripture cannot be broken, and Scripture calls human judges 'gods,' then the Father's sanctified and sent Son bears the title with greater legitimacy, not less."}
    ],
    "36": [
      {"type": "allusion", "target": "Isa 42:1",
       "note": "'Here is my servant, whom I uphold, my chosen one in whom I delight; I will put my Spirit on him.' The language of being set apart and sent echoes the commissioning of the Servant — divinely chosen, distinguished, appointed for a specific mission. Jesus' claim to be the one 'the Father set apart as his very own' is the Servant-commission language applied in the first person."},
      {"type": "allusion", "target": "Ps 2:7",
       "note": "'You are my Son; today I have become your Father.' The divine sonship claim at the heart of the blasphemy charge is grounded in Psalm 2's royal anointing — the same psalm Jesus' baptism voice echoes. To be set apart as God's Son is not a human pretension but the Davidic covenant's own terminology."}
    ],
    "38": [
      {"type": "theme", "target": "Exod 4:1",
       "note": "'What if they do not believe me or listen to me and say, The Lord did not appear to you?' Moses needed confirming signs; God provided them as evidence of the divine commission. Jesus' appeal — 'believe the works, that you may know the Father is in me' — applies the same evidential logic: the works authenticate the sender and the sent one together."}
    ],
    "41": [
      {"type": "fulfillment", "target": "Mal 3:1",
       "note": "'I will send my messenger, who will prepare the way before me.' The crowd's testimony — 'all that John said about this man was true' — confirms John the Baptist's role as forerunner. The one whose messenger predicted him is now confirmed by the fact that the prediction stands; Malachi's messenger pointed truly."}
    ],
    "42": [
      {"type": "theme", "target": "Isa 53:11",
       "note": "'After he has suffered, he will see the light of life and be satisfied; by his knowledge my righteous servant will justify many.' The 'many believed in Jesus' at the place where John first baptized is the harvest the Servant's mission was to produce: out of the region of testimony and water-purification, faith springs up."}
    ]
  }
}


def main():
    existing = load_echo('john')
    merge_echo(existing, JOHN_ECHOES)
    save_echo('john', existing)
    print('John 9–10 echoes written.')

if __name__ == '__main__':
    main()
