"""
MKT Echo Layer — John chapters 1–6
Run: python3 scripts/zc-echo-john-1-6.py

Source data used:
- data/interlinear/john.json
- data/translation/draft/mediating/john.json (MKT text)
- data/parallels/john.json (absorbed below)

Key decisions in this range:
- Prologue (1:1–18): Logos echoes Gen 1:1 and Prov 8 Wisdom tradition; classified as
  'shadow' since John builds on the pattern rather than citing either text.
- 1:14 σκηνόω: 'shadow' to Exod 40 tabernacle / Zech 2:10 dwelling; not fulfillment
  because John does not use fulfillment language — he uses it as interpretive frame.
- 1:23: 'fulfillment' because John the Baptist explicitly quotes Isa 40:3 as self-description.
- 1:29: Passover lamb → 'type' (structural anticipation); Isa 53:7 → 'allusion' (verbal
  overlap but John does not cite Isaiah); Gen 22:8 → 'type' (Abraham's "God will provide
  the lamb" foreshadows).
- 2:17: 'fulfillment' because the narrator explicitly says "it is written" and applies Ps 69:9.
- 3:14–15: 'type' — Jesus himself makes the explicit analogy to Num 21:8–9.
- 3:3–5: 'allusion' to Ezek 36:25–27 — verbal and thematic overlap (water, Spirit, new
  birth) but John does not cite Ezekiel.
- 5:28–29: 'allusion' to Dan 12:2 — closest OT parallel to general resurrection language.
- 6:14: 'allusion' to Deut 18:15 — crowd's identification "the Prophet" invokes this text.
- 6:45: 'quote' — Jesus explicitly cites "It is written in the Prophets" before reproducing
  the substance of Isa 54:13.
- 6:31: 'quote' — crowd cites "It is written: He gave them bread from heaven to eat,"
  conflating Exod 16 and Ps 78:24.
- Synoptic parallels (6:1–15 feeding; 6:16–21 walking on water) are NT-to-NT and are NOT
  included here; they belong in the parallels layer which covers intra-canonical parallels.
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
    "1": [
      {
        "type": "shadow",
        "target": "Gen 1:1",
        "note": "The Prologue's opening words mirror Genesis word for word — 'In the beginning.' The echo is not incidental: John frames the Incarnation as a new creation event, the Word present at the first creation now entering it."
      },
      {
        "type": "allusion",
        "target": "Prov 8:22-31",
        "note": "Wisdom's pre-existent presence with God before creation and her role as agent of the creative work (Prov 8:30 — 'craftsman at his side') is the closest OT background to John's Logos theology. John does not cite Proverbs but draws on the same tradition."
      }
    ],
    "3": [
      {
        "type": "shadow",
        "target": "Gen 1:3",
        "note": "God creates by speaking — 'Let there be light' — and John asserts that all things were made through the Word. The creation account establishes the Word's generative role that the Prologue reclaims and applies to Christ."
      }
    ],
    "4": [
      {
        "type": "theme",
        "target": "Gen 2:7",
        "note": "Life and light are the two gifts God brings to his creation — breath of life into the first human, light on the first day. John's identification of the Word as the source of both places Christ at the origin point of what God has always given."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Isa 9:2",
        "note": "Isaiah's oracle — 'The people walking in darkness have seen a great light' — frames the light-darkness conflict that runs through John's Prologue. John activates this register: the light shining in darkness is the arrival Isaiah's people awaited."
      }
    ],
    "9": [
      {
        "type": "theme",
        "target": "Isa 49:6",
        "note": "God's servant is appointed as 'a light for the Gentiles, that my salvation may reach to the ends of the earth.' John's description of the true Light giving light to every person universalizes the Servant's mission, which Jesus later claims explicitly."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Isa 53:3",
        "note": "The Suffering Servant 'was despised and rejected by mankind, a man of suffering.' John's statement that the Word 'came to his own, and his own people did not receive him' activates this register — the pattern of rejection is not a surprise but a fulfillment of the Servant's profile."
      }
    ],
    "12": [
      {
        "type": "theme",
        "target": "Hos 2:23",
        "note": "Hosea's promise — 'I will say to those called Not my people, You are my people' — grounds the transfer of sonship status that John describes. The right to become children of God extends the covenant family language OT prophets projected onto the restored Israel."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Exod 40:34-35",
        "note": "The Greek verb σκηνόω ('made his dwelling') shares the root with σκηνή (tabernacle) and consciously echoes the Shekinah glory filling the Mosaic tabernacle. John presents the Incarnation as the permanent, personal form of what the tabernacle represented — God dwelling among his people."
      },
      {
        "type": "allusion",
        "target": "Zech 2:10",
        "note": "Zechariah's promise — 'I am coming, and I will dwell among you' — uses the same dwelling language. John presents its fulfillment not in the restored temple but in the Word becoming flesh and dwelling with Israel's own people."
      }
    ],
    "17": [
      {
        "type": "theme",
        "target": "Exod 19:1",
        "note": "The Law given through Moses is the definitive OT marker of God's covenant with Israel. John positions grace and truth as the fuller mode of what Moses mediated — not replacement but fulfillment, the substance that the Sinai covenant anticipated."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "Exod 33:20",
        "note": "God tells Moses 'you cannot see my face, for no one may see me and live.' John opens the Prologue's bracket: no one has ever seen God — but the only-begotten God has made him known. The Incarnation resolves the limitation Moses encountered."
      }
    ],
    "23": [
      {
        "type": "fulfillment",
        "target": "Isa 40:3",
        "note": "John the Baptist explicitly identifies himself with this text: 'I am the voice of one calling in the wilderness, Make straight the way of the Lord.' The Isaianic herald prepared to announce the end of exile is now announcing the arriving King."
      }
    ],
    "29": [
      {
        "type": "type",
        "target": "Exod 12:3",
        "note": "The Passover lamb — selected, unblemished, and killed so that its blood wards off judgment from God's people — is the primary structural type. John the Baptist's 'Lamb of God who takes away the sin of the world' directly activates the Passover schema; John 19 will make the correspondence explicit (no bone broken, Passover timing)."
      },
      {
        "type": "allusion",
        "target": "Isa 53:7",
        "note": "The Servant 'was led like a lamb to the slaughter.' John the Baptist's lamb-naming draws on both the Passover type and the Servant Song; the combination — substitutionary death removing sin — maps cleanly onto Isa 53:6's 'the LORD has laid on him the iniquity of us all.'"
      },
      {
        "type": "type",
        "target": "Gen 22:8",
        "note": "Abraham's 'God himself will provide the lamb' is answered here. The binding of Isaac established the pattern — a beloved son not spared, a substitute provided — that John the Baptist's announcement fulfills: God has provided the Lamb."
      }
    ],
    "32": [
      {
        "type": "allusion",
        "target": "Isa 11:2",
        "note": "Isaiah's Branch from Jesse has 'the Spirit of the LORD rest on him.' The Spirit descending and remaining on Jesus at baptism is the anointing that designates him as the Davidic servant-king Isaiah announced."
      },
      {
        "type": "allusion",
        "target": "Isa 42:1",
        "note": "'My servant, whom I uphold, my chosen one in whom I delight; I will put my Spirit on him.' The Father's voice at baptism and the Spirit's descent are the two marks of the Servant's commissioning in Isaiah — both present at the Jordan."
      }
    ],
    "34": [
      {
        "type": "allusion",
        "target": "Ps 2:7",
        "note": "The royal declaration 'You are my Son' — spoken at the Davidic king's enthronement — is the background for 'Son of God' as royal-messianic title. John the Baptist's testimony echoes the coronation formula that the Father ratifies at the baptism."
      }
    ],
    "45": [
      {
        "type": "allusion",
        "target": "Deut 18:15",
        "note": "Philip's claim that 'Moses wrote about him in the Law' most directly invokes Moses' prophecy of the coming prophet like himself — 'You must listen to him.' Philip and Andrew interpret Jesus through this lens; the crowd will reach the same conclusion in John 6:14."
      }
    ],
    "51": [
      {
        "type": "allusion",
        "target": "Gen 28:12",
        "note": "Jacob's dream of a ladder with angels ascending and descending between heaven and earth is directly invoked — Jesus is the point of contact between heaven and earth, replacing Bethel ('house of God') as the site where the divine realm meets the human. The angels now travel on the Son of Man, not a fixed location."
      }
    ]
  },
  "2": {
    "1": [
      {
        "type": "theme",
        "target": "Hos 6:2",
        "note": "The 'third day' carries resurrection resonance in Jewish thought — Hosea's 'on the third day he will restore us' being one strand. John's precise notation may be literary rather than typological, but the third-day marker will become theologically significant in John's narrative (cf. 2:19)."
      }
    ],
    "11": [
      {
        "type": "theme",
        "target": "Exod 4:8",
        "note": "Signs authenticate the messenger from God — God tells Moses the signs will cause Israel to believe. John uses σημεῖα (signs) throughout to describe Jesus' miracles as evidence of divine commissioning; the Cana sign is the first in this authenticating sequence."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Mal 3:1",
        "note": "Malachi prophesies that 'the Lord you are seeking will suddenly come to his temple' and 'he will purify the Levites.' Jesus' arrival at the temple and his expulsion of the traders is the sudden, purifying coming Malachi envisioned — not a gentle reform but a decisive act of ownership."
      }
    ],
    "17": [
      {
        "type": "fulfillment",
        "target": "Ps 69:9",
        "note": "The disciples explicitly recall the text 'Zeal for your house will consume me' (Ps 69:9) as they observe the temple action. John presents the disciples' recollection as interpretive fulfillment — Jesus embodies the psalmist's covenant zeal at the cost of his own life (note: 'consume' carries a double meaning that the cross completes)."
      }
    ],
    "19": [
      {
        "type": "allusion",
        "target": "Amos 9:11",
        "note": "Amos promises God will 'restore David's fallen shelter' — rebuild what has been destroyed. Jesus' claim to rebuild the temple in three days recontextualizes the promise: the destroyed and rebuilt 'temple' is his body, the true dwelling place of God, fulfilling the restoration promise in an unexpected register."
      }
    ]
  },
  "3": {
    "3": [
      {
        "type": "allusion",
        "target": "Ezek 36:25-27",
        "note": "Ezekiel's new covenant promise — 'I will sprinkle clean water on you... I will give you a new heart and put a new spirit in you' — is the primary OT background for Jesus' 'born again' language. The combination of water and Spirit in verses 3–5 directly maps onto Ezekiel's sequence."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Ezek 36:25-27",
        "note": "Jesus elaborates: 'born of water and the Spirit' — both elements in Ezekiel's promised new creation of the inner person. Nicodemus as 'Israel's teacher' (v.10) should have recognized the Ezekiel register."
      },
      {
        "type": "allusion",
        "target": "Isa 44:3",
        "note": "Isaiah's restoration promise — 'I will pour water on the thirsty land... I will pour out my Spirit on your offspring' — pairs the water and Spirit gifts that Jesus now applies to individual new birth."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Prov 30:4",
        "note": "The rhetorical question 'Who has gone up to heaven and come down?' in Proverbs implies no human has divine knowledge from above. Jesus reverses the assumption: the Son of Man has come from heaven and therefore speaks heavenly things with direct authority."
      }
    ],
    "14": [
      {
        "type": "type",
        "target": "Num 21:8-9",
        "note": "Jesus himself makes the typological connection explicit: 'just as Moses lifted up the snake in the wilderness, so the Son of Man must be lifted up.' The bronze serpent — elevated so that anyone who looked on it was saved from death — is the structural anticipation of the crucifixion's saving purpose."
      }
    ],
    "16": [
      {
        "type": "type",
        "target": "Gen 22:1-19",
        "note": "The Akedah — God commanding Abraham to offer his 'one and only son' and then providing a substitute — anticipates the giving of God's one and only Son here. Both scenes involve a beloved only son, an act of giving by the father, and a substitutionary logic that averts death."
      },
      {
        "type": "theme",
        "target": "Isa 53:6",
        "note": "The world's sin laid on one person ('the LORD has laid on him the iniquity of us all') is the Servant framework behind 'whoever believes in him shall not perish.' John 3:16 states the mechanism Isa 53 narrates from the Servant's side."
      }
    ],
    "17": [
      {
        "type": "theme",
        "target": "Ezek 33:11",
        "note": "'I take no pleasure in the death of the wicked, but rather that they turn from their ways and live.' The Father's purpose in sending the Son — not to condemn but to save — matches the character God reveals through Ezekiel: his orientation is always toward life, not judgment."
      }
    ],
    "29": [
      {
        "type": "allusion",
        "target": "Isa 62:5",
        "note": "'As a bridegroom rejoices over his bride, so will your God rejoice over you.' John the Baptist identifies himself as the friend of the bridegroom, rejoicing at the Bridegroom's voice — Jesus is the one whose arrival the prophets celebrated in nuptial language."
      }
    ],
    "34": [
      {
        "type": "allusion",
        "target": "Isa 61:1",
        "note": "Isaiah's anointed herald declares 'the Spirit of the Lord is on me.' The claim that God gives the Spirit 'without limit' to the one he sends identifies Jesus as the Servant-herald fully equipped with the divine Spirit — not a partial endowment but the complete anointing."
      }
    ],
    "35": [
      {
        "type": "theme",
        "target": "Ps 2:7-8",
        "note": "The Davidic enthronement psalm gives the king all nations as inheritance — 'Ask me and I will make the nations your inheritance.' The Father placing 'everything in his hands' recasts this royal grant: the Son's authority is universal, not territorial."
      }
    ],
    "36": [
      {
        "type": "theme",
        "target": "Deut 27:26",
        "note": "The curse on those who do not obey the covenant law — 'God's wrath remains on them' — provides the background for John's language about divine wrath resting on those who reject the Son. The covenantal consequence structure is carried forward into the eschatological moment."
      }
    ]
  },
  "4": {
    "5": [
      {
        "type": "allusion",
        "target": "Gen 48:22",
        "note": "Jacob explicitly gives the plot of land at Shechem to Joseph ('one ridge of land more than your brothers'); Josh 24:32 records Joseph's bones being buried there. The narrative setting locates Jesus at the site of the patriarchal land grant, activating the Jacob-Joseph tradition."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Gen 29:1-10",
        "note": "The well-meeting is a recognized biblical type-scene: Abraham's servant finds Rebekah at a well; Jacob meets Rachel at a well; Moses meets Zipporah at a well. John places Jesus at a well meeting with a woman, invoking the betrothal type-scene — Israel's God pursuing his covenant partner."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Isa 55:1",
        "note": "Isaiah's invitation — 'Come, all you who are thirsty, come to the waters... come, buy and eat without money' — is the prophetic background for Jesus' offer of 'living water' as a gift. The water Jesus offers is the eschatological provision Isaiah announced."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Ezek 47:9",
        "note": "Ezekiel's vision of water flowing from the temple, giving life to everything it touches, is the prophetic template for 'a spring of water welling up to eternal life.' The life-giving water Jesus promises is the new-temple water Ezekiel saw flowing outward."
      },
      {
        "type": "allusion",
        "target": "Isa 12:3",
        "note": "'With joy you will draw water from the wells of salvation' — Isaiah's eschatological promise uses the same well-drawing image Jesus employs. The Samaritan woman drawing water will receive the 'water of salvation' Isaiah's restored Israel was promised."
      }
    ],
    "20": [
      {
        "type": "theme",
        "target": "Deut 12:5-7",
        "note": "Deuteronomy mandates centralized worship at 'the place the LORD your God will choose' — the Jerusalem temple. The Samaritan's question about the rival worship site at Gerizim vs. Jerusalem frames the entire OT debate about where God's name dwells."
      }
    ],
    "22": [
      {
        "type": "theme",
        "target": "Isa 2:3",
        "note": "'For out of Zion shall go the law, and the word of the LORD from Jerusalem.' Jesus affirms the Isaianic framework — 'salvation is from the Jews' — even as he announces the supersession of geographic worship: Jerusalem was the source, but the Spirit-and-truth worshipers are the fulfillment."
      }
    ],
    "25": [
      {
        "type": "allusion",
        "target": "Deut 18:15",
        "note": "The Samaritan woman expects the coming Messiah to 'explain everything to us' — a function Moses ascribed to the prophet-like-Moses who would speak God's words (Deut 18:18: 'I will put my words in his mouth; he will tell them everything I command him'). Jesus immediately claims this role."
      }
    ],
    "44": [
      {
        "type": "theme",
        "target": "Isa 53:3",
        "note": "The Suffering Servant 'was despised... he was despised, and we held him in low esteem.' Jesus' citation of the proverb 'a prophet has no honor in his own country' applies the pattern of the rejected servant to his own reception — or non-reception — among his own people."
      }
    ]
  },
  "5": {
    "17": [
      {
        "type": "allusion",
        "target": "Gen 2:2-3",
        "note": "God 'rested from all his work' on the seventh day — the foundation of the Sabbath command. Jesus' claim 'my Father is always at his work to this very day, and I too am working' directly confronts the Sabbath-as-rest framework: the Father's ongoing creative and sustaining work never ceased, and the Son participates in it."
      }
    ],
    "22": [
      {
        "type": "allusion",
        "target": "Dan 7:13-14",
        "note": "The Ancient of Days gives the Son of Man 'authority, glory and sovereign power; all nations and peoples of every language worshiped him.' Jesus' claim that the Father 'has entrusted all judgment to the Son' recasts the Danielic transfer of authority: the one who receives universal dominion also exercises universal judgment."
      }
    ],
    "23": [
      {
        "type": "theme",
        "target": "Isa 45:23",
        "note": "God declares 'before me every knee will bow; by me every tongue will swear.' Paul applies this to Christ (Phil 2:10–11); Jesus applies its logic here — honoring the Son is honoring the Father, because the Son exercises the Father's authority. To refuse honor to the Son is to refuse it to God."
      }
    ],
    "28": [
      {
        "type": "allusion",
        "target": "Dan 12:2",
        "note": "Daniel's vision — 'Multitudes who sleep in the dust of the earth will awake: some to everlasting life, others to shame and everlasting contempt' — is the direct OT antecedent for Jesus' 'all who are in their graves will hear his voice and come out.' Jesus assumes Daniel's two-destiny resurrection framework."
      }
    ],
    "29": [
      {
        "type": "allusion",
        "target": "Dan 12:2",
        "note": "The two-track resurrection — some to life, some to condemnation — directly maps onto Daniel 12:2's 'some to everlasting life, others to shame and everlasting contempt.' Jesus presents himself as the one who executes both outcomes that Daniel's angel announced."
      }
    ],
    "35": [
      {
        "type": "theme",
        "target": "Ps 132:17",
        "note": "'I have set a lamp for my anointed one' — the royal lamp that represents the Davidic dynasty's continuation. Jesus describes the Baptist as 'a lamp that burned and gave light,' using the royal-lamp imagery to honor John's role as the final preparatory herald before the King arrives."
      }
    ],
    "39": [
      {
        "type": "theme",
        "target": "Deut 31:26",
        "note": "Moses commanded that the Book of the Law be placed beside the ark 'as a witness against you.' Jesus declares that the very Scriptures they study 'testify about me' — reversing the witness: the Torah witnesses not against Israel's failure but toward the one who fulfills the covenant Israel could not keep."
      }
    ],
    "46": [
      {
        "type": "allusion",
        "target": "Deut 18:15",
        "note": "Jesus' claim that Moses 'wrote about me' most directly invokes Deut 18:15 — 'The LORD your God will raise up for you a prophet like me.' Moses himself becomes the accuser of those who reject Jesus, because they claim to follow Moses while rejecting the one Moses pointed toward."
      }
    ]
  },
  "6": {
    "3": [
      {
        "type": "allusion",
        "target": "Exod 19:3",
        "note": "Moses went up the mountain to receive the Law and to mediate between God and Israel. Jesus going up a mountainside and sitting down with disciples before feeding the multitude casts him as the new Moses — the setting anticipates the Bread of Life discourse's reinterpretation of the manna."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "2 Kgs 4:42-44",
        "note": "Elisha feeds a hundred men with twenty barley loaves and has leftovers — 'They ate and had some left over, as the LORD said.' The structural parallel is close: inadequate food, a crowd fed, surplus gathered. Jesus recapitulates and vastly exceeds Elisha's provision, locating himself beyond the prophetic tradition."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Deut 18:15",
        "note": "The crowd's conclusion — 'Surely this is the Prophet who is to come into the world' — is an explicit identification with Moses' promised prophet-like-Moses. They recognize the feeding sign as messianic authentication. Jesus' withdrawal (v.15) corrects their political misreading of the prophetic role."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Exod 3:14",
        "note": "Jesus' self-identification 'It is I' (Greek ἐγώ εἰμί, 'I AM') on the water echoes the divine name revealed to Moses. In the LXX Exod 3:14, God says ἐγώ εἰμί ὁ ὤν. John's consistent use of ἐγώ εἰμί in theophanic contexts signals a claim to divine identity, not merely personal identification."
      }
    ],
    "31": [
      {
        "type": "quote",
        "target": "Exod 16:4",
        "note": "The crowd quotes 'He gave them bread from heaven to eat' — conflating Exod 16:4 ('I will rain down bread from heaven') and Ps 78:24 ('he rained down manna for the people to eat'). Jesus immediately corrects the attribution: it was not Moses but the Father who gave the bread, and now gives the true bread."
      },
      {
        "type": "allusion",
        "target": "Ps 78:24-25",
        "note": "The psalmist celebrates that God 'rained down manna for the people to eat... the bread of angels.' The crowd's citation invokes this thanksgiving tradition; Jesus reframes it: the angels' bread was a temporary sign pointing to the true bread the Father now gives in the Son."
      }
    ],
    "35": [
      {
        "type": "allusion",
        "target": "Isa 55:1-2",
        "note": "Isaiah's eschatological invitation — 'Come, all you who are thirsty, come to the waters... why spend money on what is not bread?' — is the prophetic background for 'I am the bread of life. Whoever comes to me will never go hungry.' Jesus embodies the invitation that Isaiah extended on behalf of God."
      },
      {
        "type": "allusion",
        "target": "Prov 9:5",
        "note": "Wisdom invites: 'Come, eat my food and drink the wine I have mixed; leave your simple ways and you will live.' John's Jesus — identified with the Word and with divine Wisdom in the Prologue — issues precisely this invitation: come, eat, live. The Wisdom feast becomes incarnate."
      }
    ],
    "45": [
      {
        "type": "quote",
        "target": "Isa 54:13",
        "note": "Jesus explicitly cites 'It is written in the Prophets: They will all be taught by God' — reproducing the substance of Isa 54:13 ('all your children will be taught by the LORD'). The Father's drawing (v.44) is the same as the divine teaching Isaiah promised: God instructs those who come to the Son."
      },
      {
        "type": "allusion",
        "target": "Jer 31:33-34",
        "note": "The new covenant promise — 'I will put my law in their minds... they will all know me' — is Jeremiah's version of the same eschatological teaching. Jesus' statement that those 'who have heard the Father and learned from him come to me' fulfills this inner-transformation promise."
      }
    ],
    "51": [
      {
        "type": "allusion",
        "target": "Isa 53:12",
        "note": "The Servant 'poured out his life unto death' and 'bore the sin of many.' Jesus' offer — 'this bread is my flesh, which I will give for the life of the world' — is the same substitutionary giving described in Isa 53: a life voluntarily surrendered so that others receive life."
      }
    ],
    "63": [
      {
        "type": "allusion",
        "target": "Ezek 37:14",
        "note": "'I will put my Spirit in you and you will live' — Ezekiel's dry bones passage climaxes in the Spirit as the source of life. Jesus' statement 'The Spirit gives life; the flesh counts for nothing' adopts this pneumatological framework: the Bread of Life discourse's 'eating' is spiritual, mediated by the Spirit."
      }
    ],
    "69": [
      {
        "type": "theme",
        "target": "Ps 16:10",
        "note": "Peter's confession 'the Holy One of God' applies a divine designation (קָדוֹשׁ — the holy one) to Jesus. Ps 16:10 — 'you will not let your Holy One see decay' — is later applied to Christ's resurrection by both Peter (Acts 2:27) and Paul (Acts 13:35). Peter's title anticipates the Christological argument of Acts."
      }
    ]
  }
}


def main():
    existing = load_echo('john')
    merge_echo(existing, JOHN_ECHOES)
    save_echo('john', existing)
    print('John 1–6 echoes written.')

if __name__ == '__main__':
    main()
