"""
MKT Echo Layer — John chapters 14–16
Run: python3 scripts/zc-echo-john-14-16.py

Source data used:
- data/interlinear/john.json (Strongs tokens, chs 14–16)
- data/translation/draft/mediating/john.json (MKT text for all 91 verses)
- data/translation/glossary-greek.json (G3875 παράκλητος, G4151 πνεῦμα, G225 ἀλήθεια,
  G26 ἀγάπη, G3306 μένω)
- data/parallels/john.json (15:1 and 15:25 absorbed below)
- data/echoes/john.json (chs 1–13 present; chs 14–16 not yet written)
- data/commentary/ellicott/john.json (chs 14–16)

Key decisions in this range:
- 14:6 "I am the way": classified as `type` drawing on Wisdom/Prov 8 tradition rather than
  simple `allusion` — the identification of Jesus with the divine path/life is structural,
  not merely verbal.
- 14:7 / 14:9: Moses's denied request to see God (Exod 33:20-23) is the structural foil.
  Classified `allusion` (John does not cite Exod 33 explicitly, but the intertextual argument
  is strong given the Moses-throughout-John pattern, e.g., 1:17, 5:46, 6:32).
- 14:16 Paraclete: Ezek 36:26-27 and Joel 2:28-29 classified `allusion` not `fulfillment`
  because John does not cite either OT text explicitly; the Spirit-within pattern is
  absorbed from Ezekiel but the terminology differs.
- 14:23 God dwelling with his people: `shadow` for the Eden / Lev 26 pattern — the original
  communion of Gen 3 is the structural origin of this promise; Lev 26:12 makes the trajectory
  explicit; Ezek 37:27 projects it eschatologically.
- 15:1 True Vine: three OT allusions retained from parallels (Ps 80:8; Isa 5:1-7; Ezek 15)
  plus a fourth (Jer 2:21). Isa 5 is the richest — Jesus explicitly replaces what Israel
  failed to be; classified `type` because the vineyard image is structural and deliberately
  evoked, not coincidental.
- 15:25 "hated without reason": `fulfillment` — John 15:25 itself says "to fulfill what is
  written in their Law," making this a self-declared fulfillment of Ps 35:19 / Ps 69:4.
  Both psalms absorbed from parallels.
- 16:2 synagogue expulsion + killing as divine service: Isa 66:5 is classified `allusion`
  (the verbal parallel is not exact but the conceptual frame — persecutors who think they
  serve God — is structurally precise).
- 16:11 "prince of this world condemned": Gen 3:15 is the foundational `type` (protoevangelium;
  the serpent/ruler is crushed); Dan 7 adds the courtroom frame.
- 16:21 birth pangs: Isa 26:17-18, Isa 66:7-9, Mic 4:9-10 are all allusions — the birth-pains-
  then-joy eschatological pattern is a recognizable OT motif the NT inherits throughout.
- 16:32 sheep scattered: `fulfillment` — Zech 13:7 is explicitly cited in Matt 26:31 / Mark
  14:27 for the same event; John does not cite it, but the fulfillment is established by the
  Synoptic tradition for this same night.
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
  "14": {
    "1": [
      {"type": "theme", "target": "Deut 6:4-5", "note": "The Shema commands Israel to love and trust YHWH alone. Jesus places himself alongside the Father as co-object of faith — 'you believe in God; believe also in me' — mapping the singular Shema trust onto a two-person relationship. The Evangelist's Christology emerges here not through argument but through direct command."},
      {"type": "allusion", "target": "Isa 35:4", "note": "'Say to those with fearful hearts, Be strong, do not fear; your God will come.' The comfort formula 'do not let your hearts be troubled' draws on the Isaianic pattern of divine reassurance spoken at the edge of crisis, here transferred from YHWH to Jesus himself as the one who speaks it."}
    ],
    "2": [
      {"type": "shadow", "target": "Ps 23:6", "note": "'I will dwell in the house of the LORD forever.' The Father's house with many rooms is the eschatological fulfillment of the psalmist's longing to dwell permanently in God's presence — what is aspiration in the psalm becomes promised destination in Jesus's word."},
      {"type": "shadow", "target": "Zeph 3:17", "note": "The prophet envisions YHWH dwelling in the midst of his people and rejoicing over them. The Father's house language extends the tabernacle/temple trajectory — the divine-human dwelling first established at Sinai (Exod 40:34-35) now takes a permanent, personal form prepared by the Son."}
    ],
    "3": [
      {"type": "allusion", "target": "Isa 40:10-11", "note": "Isaiah's second-exodus vision: 'The Sovereign LORD comes with power... He tends his flock like a shepherd: he gathers the lambs in his arms.' The departing and returning Lord who gathers his people to himself recapitulates this homecoming pattern; Jesus as shepherd going ahead and returning to gather is the same structure."}
    ],
    "4": [
      {"type": "theme", "target": "Ps 16:11", "note": "The psalmist declares, 'You make known to me the path of life.' Jesus claims the disciples already know this path — because they know him. The movement from 'the LORD makes known the path' to 'I am the path' is the Christological step John has been building toward since 1:18."}
    ],
    "5": [
      {"type": "theme", "target": "Ps 25:4-5", "note": "'Show me your ways, LORD, teach me your paths; guide me in your truth.' Thomas's honest admission — 'we don't know where you are going' — echoes this psalmist's openness about needing divine guidance for the path to God's presence. The answer Jesus gives is not a map but a person."}
    ],
    "6": [
      {"type": "type", "target": "Prov 8:32-35", "note": "Divine Wisdom speaks: 'Blessed are those who listen to me, watching daily at my doors... For those who find me find life.' Jesus's 'I am the way and the truth and the life' inhabits the structural role Proverbs assigns to Wisdom — the one through whom one reaches the Father. John 1:1-18 has already identified Jesus with the divine Word/Wisdom; 14:6 makes the soteriological claim explicit."},
      {"type": "allusion", "target": "Ps 16:11", "note": "'You make known to me the path of life; you will fill me with joy in your presence.' In claiming to be 'the way' and 'the life,' Jesus identifies himself as the living embodiment of what David experienced as a divine gift — the path of life is not a route but a relationship with the Son."}
    ],
    "7": [
      {"type": "allusion", "target": "Exod 33:18-23", "note": "Moses asked God, 'Show me your glory,' and was told no one can see God's face and live — he could only glimpse God's back passing by. Jesus tells the disciples they have already seen the Father through him. What the greatest prophet of Israel was denied is now available through the incarnate Son; the contrast is deliberate in a Gospel that already compared Jesus and Moses (1:17; 6:32)."}
    ],
    "8": [
      {"type": "allusion", "target": "Exod 33:18", "note": "Philip's request — 'show us the Father and that will be enough for us' — verbally echoes Moses's petition, 'Show me your glory.' The Evangelist places Philip in Moses's position. Jesus's answer reframes the request entirely: the Father has already been shown to those who have seen the Son. The glory Moses sought in the cloud is now clothed in flesh."}
    ],
    "9": [
      {"type": "allusion", "target": "Exod 33:20", "note": "God told Moses, 'You cannot see my face, for no one may see me and live.' Jesus's 'anyone who has seen me has seen the Father' directly overturns this Mosaic restriction — not by contradicting it but by fulfilling it through the incarnation. What the Sinai theophany withheld, the Son makes available."},
      {"type": "allusion", "target": "Isa 6:1-5", "note": "Isaiah saw 'the Lord, high and exalted' and cried 'woe to me.' John 12:41 explicitly identifies this vision as seeing Christ's glory. The disciples have seen what Isaiah saw — but without destruction, because the judge has become the savior."}
    ],
    "10": [
      {"type": "allusion", "target": "Deut 18:18", "note": "God told Moses about the future prophet: 'I will put my words in his mouth, and he will tell them everything I command him.' Jesus says 'the words I say to you I do not speak on my own; the Father, living in me, is doing his work' — but Jesus transcends the Deuteronomic prophet model by claiming mutual indwelling rather than mere divine dictation."}
    ],
    "11": [
      {"type": "theme", "target": "Exod 14:31", "note": "Israel believed in the LORD and in Moses when they saw the works at the sea. Jesus invites belief on the basis of works — the same evidentiary logic Moses appealed to, now centered on the Son. The works authenticate the sender just as the Exodus miracles authenticated Moses's commission."}
    ],
    "12": [
      {"type": "allusion", "target": "Isa 61:1-3", "note": "The Spirit of the LORD enables proclamation, healing, and liberation — the Servant's works of the coming age. Jesus's promise that believers will do 'greater works' points toward Spirit-empowered mission after his departure; the Isaianic Servant's agenda is extended through his people by the Spirit Jesus is about to send (16:7)."}
    ],
    "13": [
      {"type": "theme", "target": "Ps 50:15", "note": "'Call on me in the day of trouble; I will deliver you, and you will honor me.' The pattern of petition-in-my-name and I-will-do-it recapitulates the covenantal prayer dynamic of the Psalms — calling on God and receiving answer — now routed through Jesus's name, so that the Father's glory is revealed in the Son."}
    ],
    "14": [
      {"type": "theme", "target": "Ps 37:4", "note": "'Take delight in the LORD, and he will give you the desires of your heart.' The prayer promise of 14:14 is the New Covenant fulfillment of this psalmist pattern — the condition is no longer 'delight in the LORD' abstractly but union with Christ, whose desires and the Father's will are one, so that asking in his name aligns petitioner with the Father's purposes."}
    ],
    "15": [
      {"type": "allusion", "target": "Deut 7:9", "note": "'Know therefore that the LORD your God is God; he is the faithful God, keeping his covenant of love to a thousand generations of those who love him and keep his commandments.' Jesus restructures this Deuteronomic formula around himself: loving Jesus = keeping his commandments = remaining in covenant. The Sinai love-obedience bond is reoriented from Moses's law to Jesus's person."},
      {"type": "allusion", "target": "Exod 20:6", "note": "The second commandment: 'showing love to a thousand generations of those who love me and keep my commandments.' The love-obedience nexus in 14:15 is not a new invention but the restatement of what the Decalogue established as the shape of covenant response, now mediated through Christ."}
    ],
    "16": [
      {"type": "allusion", "target": "Ezek 36:26-27", "note": "God promised, 'I will put a new spirit in you... I will put my Spirit in you and move you to follow my decrees.' The Advocate promised here — another, permanent Paraclete — is the fulfillment of Ezekiel's new-covenant pledge: the Spirit not merely hovering over but dwelling within. The 'with you forever' answers Ezekiel's permanence promise."},
      {"type": "allusion", "target": "Joel 2:28-29", "note": "'I will pour out my Spirit on all people... Even on my servants, both men and women, I will pour out my Spirit in those days.' The Paraclete's arrival fulfills Joel's vision of the democratized Spirit presence. John 14:16 establishes the precondition: the departure of the Son enables the universal indwelling of the Spirit Acts 2 will announce as Joel's fulfillment."}
    ],
    "17": [
      {"type": "allusion", "target": "Ezek 36:27", "note": "The Spirit dwelling within (ἐν ὑμῖν ἔσται) fulfills the Ezekielian promise of interior Spirit presence: not the occasional, external empowerment of specific leaders (as under the old covenant) but permanent indwelling of the covenant community. The contrast between 'beside you' and 'in you' marks the covenantal transition."},
      {"type": "allusion", "target": "Ps 43:3", "note": "'Send me your light and your faithful truth, let them lead me.' The Spirit is called 'the Spirit of truth' — the divine truth that leads to God's holy mountain now given as an interior guide rather than an external path."}
    ],
    "18": [
      {"type": "allusion", "target": "Ps 27:10", "note": "'Though my father and mother forsake me, the LORD will receive me.' The promise 'I will not leave you as orphans; I will come to you' addresses the disciples' imminent abandonment. Jesus positions himself as the LORD who receives the forsaken — the one Ps 27 trusts to be present precisely when human bonds fail."},
      {"type": "allusion", "target": "Isa 49:14-15", "note": "Zion cries 'The LORD has forsaken me'; God responds with the mother-child image: 'Can a mother forget the baby at her breast? Though she may forget, I will not forget you.' Jesus's 'I will not leave you as orphans' inhabits this divine refusal to abandon — the disciples' fear of forsakenness meets the same divine word Zion received."}
    ],
    "19": [
      {"type": "theme", "target": "Isa 26:19", "note": "'Your dead will live, LORD; their bodies will rise — let those who dwell in the dust wake up and shout for joy.' Jesus's 'because I live, you also will live' grounds the disciples' life in his resurrection — the life he will have on the other side of death is the direct source of theirs. Isa 26 projects a resurrection derivative of YHWH's own life; here it is derivative of the Son's."}
    ],
    "20": [
      {"type": "allusion", "target": "Jer 31:33", "note": "'I will put my law in their minds and write it on their hearts. I will be their God, and they will be my people.' The mutual indwelling Jesus describes — 'you will realize that I am in my Father, and you are in me, and I am in you' — is the interior covenant presence Jeremiah's new covenant promised, now accomplished through the Son rather than a written law."},
      {"type": "shadow", "target": "Ezek 37:27", "note": "'My dwelling place will be with them; I will be their God, and they will be my people.' The eschatological cohabitation Ezekiel envisions as a future divine act is compressed into Jesus's present declaration of mutual indwelling — the full restoration of divine-human fellowship that Ezekiel saw as the goal of all God's work with Israel."}
    ],
    "21": [
      {"type": "allusion", "target": "Deut 7:9", "note": "The covenantal love-obedience structure: those who love God and keep his commands receive his covenant faithfulness. Jesus replicates this structure around himself: those who have his commands and keep them love him, and the Father's love follows. The Sinai covenant form is transposed onto the person of the Son."}
    ],
    "22": [
      {"type": "theme", "target": "Deut 29:29", "note": "'The secret things belong to the LORD our God, but the things revealed belong to us and to our children forever.' Judas's question about selective revelation — 'why do you intend to show yourself to us and not to the world?' — touches this Deuteronomic principle of hidden and revealed, now resolved not by divine arbitrariness but by the love-obedience relationship that makes disclosure possible."}
    ],
    "23": [
      {"type": "shadow", "target": "Gen 3:8", "note": "God walked with Adam in the garden in the cool of the day — the original divine-human cohabitation broken at the Fall. Jesus's promise 'we will come to them and make our home with them' restores what Eden represented: the Father and Son dwelling together with the obedient covenant partner. The new-covenant home-making is the redemptive arc of the garden returned."},
      {"type": "allusion", "target": "Lev 26:12", "note": "'I will walk among you and be your God, and you will be my people.' The covenant formula of Leviticus 26 — God dwelling and walking with his people — was conditional on obedience to his decrees. Jesus restates this condition as love expressed through obedience to his word, now fulfilled not by Israel's performance but by the new-covenant indwelling."}
    ],
    "24": [
      {"type": "allusion", "target": "Deut 18:18", "note": "The Mosaic prophet spoke only what God commanded him to say. Jesus says 'these words you hear are not my own; they belong to the Father who sent me' — but he goes beyond the prophet type: Moses received words from outside; Jesus speaks from within a unity with the Father that the Deuteronomic prophet model could not contemplate."}
    ],
    "25": [
      {"type": "theme", "target": "Ps 119:11", "note": "'I have hidden your word in my heart that I might not sin against you.' Jesus speaks while still present; the Spirit will later make these words interior, doing what the psalmist aspired to do manually — storing the divine word within so it guides conduct from the heart."}
    ],
    "26": [
      {"type": "allusion", "target": "Isa 11:2", "note": "'The Spirit of the LORD will rest on him — the Spirit of wisdom and of understanding, the Spirit of counsel and of might, the Spirit of knowledge and fear of the LORD.' The Advocate whom the Father sends teaches 'all things' — comprehensive instruction matching what Isaiah attributed to the Spirit of wisdom and understanding resting on the Messiah, now distributed to his people."},
      {"type": "allusion", "target": "Neh 9:20", "note": "'You gave your good Spirit to instruct them.' The Levites' confession recalls how God gave his Spirit to teach Israel in the wilderness. The Paraclete as teacher of all things and reminder of Jesus's words fulfills what the wilderness Spirit did for Israel — guiding through instruction and memory — now permanently and internally."}
    ],
    "27": [
      {"type": "allusion", "target": "Num 6:24-26", "note": "The Aaronic blessing: 'The LORD bless you and keep you... give you peace.' Jesus's departure-gift of peace is his fulfillment of the priestly benediction — he as the great High Priest bestows what Aaron was commanded to pronounce, and it is 'not as the world gives' because it is the eschatological shalom of God's own presence."},
      {"type": "allusion", "target": "Isa 9:6", "note": "The Servant-King is called 'Prince of Peace.' The peace Jesus bequeaths is not a disposition but a person — the one Isaiah named as its source now fulfills his own title by giving himself as the ground of the disciples' peace in his absence."}
    ],
    "28": [
      {"type": "theme", "target": "Ps 110:1", "note": "'The LORD says to my lord: Sit at my right hand until I make your enemies a footstool for your feet.' Jesus's statement that 'the Father is greater than I' fits within the functional subordination of the seated Messiah who receives authority from the Father — not a denial of ontological equality but the ordering of the one who goes to prepare and return, fulfilling this enthronement trajectory."}
    ],
    "29": [
      {"type": "allusion", "target": "Isa 48:3-5", "note": "'I foretold the former things long ago... so that you could not say, My idol did them.' God's pattern of announcing events before they happen is for the sake of faith — so that when they occur, the hearers recognize divine authorship. Jesus's 'I have told you now before it happens so that when it does happen you will believe' adopts this exact Isaianic rationale."}
    ],
    "30": [
      {"type": "allusion", "target": "Dan 10:13", "note": "'The prince of the Persian kingdom resisted me twenty-one days.' Daniel's angel meets 'princes' — spiritual powers behind earthly kingdoms. Jesus's 'prince of this world' belongs to the same cosmological framework the apocalyptic tradition mapped: a spiritual ruler-power whose domain is 'this world' and whose authority is about to be overthrown."}
    ],
    "31": [
      {"type": "allusion", "target": "Ps 40:8", "note": "'I desire to do your will, my God; your law is within my heart.' The departing Jesus affirms his love for the Father and his exact obedience to the Father's command — the posture Ps 40 describes as the heart's disposition. What the psalmist declared as aspiration, Jesus enacts as historical obedience culminating in the cross."}
    ]
  },
  "15": {
    "1": [
      {"type": "type", "target": "Isa 5:1-7", "note": "The Song of the Vineyard: God planted a choice vine, tended it carefully, and it produced only bad fruit. 'The vineyard of the LORD Almighty is the nation of Israel.' Jesus claims to be 'the true vine' — using the same vineyard imagery Isaiah applied to Israel but asserting that he is what Israel failed to be. The failure of the old vine is resolved not by replanting Israel but by the Son himself becoming the vine."},
      {"type": "allusion", "target": "Ps 80:8-11", "note": "'You transplanted a vine from Egypt; you drove out the nations and planted it.' The psalmist uses this imagery to cry for restoration of what the vine once was. Jesus's 'I am the true vine' answers this lament — the vine from Egypt, failed and in exile, finds its true form in the Son who is the original Israel returning."},
      {"type": "allusion", "target": "Ezek 15:1-8", "note": "Ezekiel uses the vine branch as an image of uselessness — unlike other trees, the vine branch is good for nothing when it bears no fruit, fit only for fire. Jesus's allegory deliberately engages this Ezekielian framework: the branches that do not abide in him meet precisely this fate (15:6), while the true vine produces the fruit the failed branch of Ezek 15 could not."}
    ],
    "2": [
      {"type": "allusion", "target": "Jer 2:21", "note": "'I had planted you like a choice vine of sound and reliable stock. How then did you turn against me into a corrupt, wild vine?' Jeremiah's lament over Israel's degeneration is the background against which the Father's pruning in 15:2 makes sense — the old vine required cutting away, but within the true vine (Jesus), branches that bear fruit are pruned for greater fruitfulness rather than cut off entirely."}
    ],
    "3": [
      {"type": "allusion", "target": "Ps 119:9", "note": "'How can a young person stay on the path of purity? By living according to your word.' The disciples are declared 'already clean because of the word I have spoken to you' — the same mechanism the psalmist identifies: the word of God as the instrument of purification. The word of Jesus performs what the Psalm attributes to the word of God."}
    ],
    "4": [
      {"type": "allusion", "target": "Deut 30:20", "note": "'Love the LORD your God, listen to his voice, and hold fast to him. For the LORD is your life.' Moses's call to 'hold fast' (Hebrew: dāḇaq) to YHWH as the ground of life is the covenant precedent for 'remain in me.' The μένω / abiding Jesus commands is the Greek equivalent of the Deuteronomic cleaving — covenant adhesion as the condition of life."},
      {"type": "allusion", "target": "Ps 91:1", "note": "'Whoever dwells in the shelter of the Most High will rest in the shadow of the Almighty.' The Psalm presents abiding in God as the posture of the one who is protected and fruitful. Jesus takes this spatial metaphor of shelter and makes it organic: dwelling is now dwelling-in-the-vine, a life-union rather than a refuge."}
    ],
    "5": [
      {"type": "allusion", "target": "Hos 14:8", "note": "YHWH to Israel: 'I am like a flourishing juniper; your fruitfulness comes from me.' This divine claim — your fruit comes from my life in you — is the OT ground of Jesus's 'apart from me you can do nothing.' Hosea's metaphor of divine life as the source of Israel's fruitfulness becomes, in John 15, the radical claim that all genuine spiritual productivity is derivative of union with the Son."},
      {"type": "allusion", "target": "Ps 127:1", "note": "'Unless the LORD builds the house, the builders labor in vain.' The principle of absolute divine primacy in any fruitful work is extended in 15:5 to the most basic level: organic union with Christ is the precondition of any spiritual fruit, not effort applied to a divine project."}
    ],
    "6": [
      {"type": "allusion", "target": "Ezek 15:4-6", "note": "Ezekiel's extended vine-branch image: 'It is thrown into the fire for fuel; the fire burns both ends of it, and the middle is charred... I will make the land desolate because they have been unfaithful.' Jesus draws on this Ezekielian precedent — the non-abiding branch is 'thrown away and withers; such branches are picked up, thrown into the fire and burned' — the same fate Ezekiel foresaw for fruitless Israel."}
    ],
    "7": [
      {"type": "theme", "target": "Ps 37:4", "note": "'Delight yourself in the LORD and he will give you the desires of your heart.' The promise 'ask whatever you wish, and it will be done for you' is conditioned on Jesus's words remaining in the abiding disciple. This is the New Covenant form of the Psalm's pattern: desire-aligned-with-God produces granted petitions, because the one whose words remain in you has had their will conformed to the Father's."}
    ],
    "8": [
      {"type": "theme", "target": "Isa 61:3", "note": "'They will be called oaks of righteousness, a planting of the LORD for the display of his splendor.' The fruit-bearing disciples who bring glory to the Father recapitulate Isaiah's 'planting of the LORD' — a community whose fruitfulness is itself a display of divine glory rather than human achievement."}
    ],
    "9": [
      {"type": "allusion", "target": "Jer 31:3", "note": "'I have loved you with an everlasting love; I have drawn you with unfailing kindness.' Jesus's 'as the Father has loved me, so have I loved you' gives the disciples a share in the eternal love that flows between Father and Son — the hesed Jeremiah attributed to YHWH's relationship with Israel is now the measure of Christ's love for his own."}
    ],
    "10": [
      {"type": "allusion", "target": "Deut 7:9", "note": "YHWH keeps his covenant and steadfast love with those who love him and keep his commandments. Jesus reformulates this covenantal logic: keeping his commandments is the evidence of remaining in his love, just as he has kept his Father's commands and remains in the Father's love. The disciple is placed within the same love-obedience economy that governs the Father-Son relationship."}
    ],
    "11": [
      {"type": "theme", "target": "Ps 16:11", "note": "'You will fill me with joy in your presence, with eternal pleasures at your right hand.' The joy Jesus offers as his own joy in the disciples is the fullness Ps 16 locates in God's presence — what David experienced as God's joy-in-presence, Jesus offers as his joy transmitted into those who abide in him."}
    ],
    "12": [
      {"type": "allusion", "target": "Lev 19:18", "note": "'Love your neighbor as yourself.' Jesus reissues the Levitical command but grounds it differently: not 'as yourself' but 'as I have loved you.' The measure of the command shifts from self-regard to the sacrificial love of the Son — a quantitative and qualitative escalation that Lev 19 could not anticipate because it lacked the model Christ provides."}
    ],
    "13": [
      {"type": "allusion", "target": "Isa 53:12", "note": "'He poured out his life unto death, and was numbered with the transgressors. For he bore the sin of many.' The 'greater love' of laying down life for friends is enacted in Jesus's own death, which fulfills the Servant's self-emptying pattern. The principle stated in 15:13 is not abstract ethics but the interpretation of what Jesus is about to do, read against the Servant's specific self-offering."},
      {"type": "type", "target": "Exod 12:3-7", "note": "The Passover lamb was killed on behalf of the household — its death averted judgment and secured the life of those sheltered under its blood. Jesus's laying down his life for his 'friends' fulfills the structural pattern of the Passover substitute: a life given so that those under covenant protection may live."}
    ],
    "14": [
      {"type": "allusion", "target": "Exod 33:11", "note": "'The LORD would speak to Moses face to face, as one speaks to a friend.' The highest privilege in Israel's history — direct, face-to-face speech with God, friend to friend — is what Jesus extends to the disciples. Moses was singular; friendship with God is now the vocation of all who obey the Son."}
    ],
    "15": [
      {"type": "allusion", "target": "Isa 41:8", "note": "'But you, Israel, my servant, Jacob, whom I have chosen, you descendants of Abraham my friend' (LXX: ὃν ἠγάπησα). Abraham's friendship with God is the OT precedent for the disciples' elevation. Jesus grounds this in disclosure: a friend is told the master's business. The disciples inherit Abraham's status as those to whom God reveals his purposes."}
    ],
    "16": [
      {"type": "allusion", "target": "Deut 7:6-7", "note": "'The LORD your God has chosen you out of all the peoples on the face of the earth... The LORD did not set his affection on you because you were more numerous than other peoples... but it was because the LORD loved you.' The disciples' election — 'you did not choose me, but I chose you' — follows this same Deuteronomic logic of uncaused, sovereign love. The Gentile-inclusive mission ('go and bear fruit') is its expansion."},
      {"type": "allusion", "target": "Isa 41:8-9", "note": "'I took you from the ends of the earth... I said, You are my servant; I have chosen you and have not rejected you.' The calling and appointing of the disciples for fruit-bearing mission recapitulates the Servant's calling — selected, appointed for a task, authorized to go in the name of the one who chose them."}
    ],
    "17": [
      {"type": "theme", "target": "Lev 19:18", "note": "The reiteration of the love command ('love each other') signals that Jesus is recasting Lev 19:18 as the foundational social ethic of the new-covenant community. The double repetition (15:12, 15:17) corresponds to the Mosaic practice of repeating covenant obligations at pivotal points in legal instruction."}
    ],
    "18": [
      {"type": "allusion", "target": "Ps 69:4", "note": "'Those who hate me without reason outnumber the hairs of my head... I am forced to restore what I did not steal.' The world's hatred of Jesus was already anticipated in this psalm of the righteous sufferer — which John will quote explicitly in 15:25. Here the pattern is stated prospectively: as the world hated him, so it will hate his disciples."},
      {"type": "allusion", "target": "Isa 49:7", "note": "'He who was despised and abhorred by the nation... Kings will see you and stand up, princes will see and bow down.' The Servant is first despised and then vindicated. Jesus prepares the disciples for the despised-phase: the world's hatred is not a sign of abandonment but of alignment with the Servant's trajectory toward vindication."}
    ],
    "19": [
      {"type": "allusion", "target": "Deut 7:6", "note": "'The LORD your God has chosen you to be a people for his treasured possession, out of all the peoples who are on the face of the earth.' The disciples' removal from the world by Jesus's choosing recapitulates Israel's election from among the nations. As Israel was set apart to be God's own from the midst of the nations, the disciples are set apart from 'the world' to belong to Christ."},
      {"type": "allusion", "target": "Exod 19:5", "note": "'Now if you obey me fully and keep my covenant, then out of all nations you will be my treasured possession.' The new-covenant community of Jesus repeats the Sinai pattern of being chosen-out-of-the-world — the same structural logic that defined Israel now defines those who bear fruit for the Son."}
    ],
    "20": [
      {"type": "theme", "target": "Amos 3:7", "note": "'Surely the Sovereign LORD does nothing without revealing his plan to his servants the prophets.' Jesus has already warned them about persecution; the reference back to 'what I told you' grounds the disciples' experience in the servant-prophet pattern — being warned in advance is the privilege and burden of those who know God's purposes."}
    ],
    "21": [
      {"type": "allusion", "target": "Isa 1:3", "note": "'The ox knows its master, the donkey its owner's manger, but Israel does not know, my people do not understand.' Jesus traces the world's persecution of the disciples to ignorance of the one who sent him — the same diagnostic Isa 1 applies to Israel's rebellion. Not-knowing God is both the cause and the nature of opposition to his messengers."},
      {"type": "allusion", "target": "Jer 4:22", "note": "'My people are fools; they do not know me. They are senseless children; they have no understanding.' The Jeremianic verdict on not-knowing God is the theological category Jesus applies to those who persecute the disciples: their hostility is culpable ignorance, not informed opposition."}
    ],
    "22": [
      {"type": "theme", "target": "Amos 3:2", "note": "'You only have I chosen of all the families of the earth; therefore I will punish you for all your sins.' Greater covenantal privilege entails greater accountability. Jesus's logic — 'if I had not come and spoken to them, they would not be guilty of sin' — follows the Amos principle: knowledge of the divine word creates a level of culpability that ignorance does not carry."}
    ],
    "23": [
      {"type": "theme", "target": "Deut 5:9", "note": "'I, the LORD your God, am a jealous God... showing love to a thousand generations of those who love me.' Hating Jesus = hating the Father because love and hatred of God are a single indivisible response — there is no neutral ground between the Son and the Father. The Deuteronomic unity of God means love or hatred of his representative is love or hatred of him."}
    ],
    "24": [
      {"type": "theme", "target": "Deut 4:32-35", "note": "'Has any god ever tried to take for himself one nation out of another nation, by testings, by signs and wonders...' — the works done among Israel were unparalleled, creating unique culpability. Jesus applies this logic: the works 'no one else did' create a level of inexcusable knowledge that no previous generation possessed, and rejection of them is therefore without precedent."}
    ],
    "25": [
      {"type": "fulfillment", "target": "Ps 35:19", "note": "'Do not let those gloat over me who are my enemies without cause; do not let those who hate me without reason maliciously wink the eye.' John explicitly says the world's hatred fulfills 'what is written in their Law.' Ps 35:19 is one of the two cited texts; the righteous sufferer of the lament psalms is the OT type whose experience the Messiah inhabits in full."},
      {"type": "fulfillment", "target": "Ps 69:4", "note": "'Those who hate me without reason outnumber the hairs of my head.' John's citation 'they hated me without reason' (δωρεάν) matches the LXX of Ps 69:4 verbatim. This psalm — also quoted in John 2:17 (temple zeal) and 19:28-29 (thirst/sour wine) — provides the Evangelist's primary OT grid for reading Jesus's passion as righteous-sufferer fulfillment."}
    ],
    "26": [
      {"type": "allusion", "target": "Ezek 36:26-27", "note": "God promised to put a new spirit within Israel, causing them to follow his decrees. The Paraclete 'who goes out from the Father' fulfills this promise: the interior Spirit presence Ezekiel foresaw now bears testimony to the Son. The going-out-from-the-Father reflects the same divine origin Ezekiel attributed to the new Spirit."},
      {"type": "allusion", "target": "Isa 44:3", "note": "'I will pour water on the thirsty land... I will pour out my Spirit on your offspring.' Isaiah's promise of widespread Spirit outpouring is the OT background for the Paraclete's mission: the Spirit comes not to one leader or prophet but is poured out as testimony to Christ among the disciples and through them to the world."}
    ],
    "27": [
      {"type": "allusion", "target": "Isa 43:10", "note": "'You are my witnesses, declares the LORD, and my servant whom I have chosen, so that you may know and believe me.' The disciples' testimony in 15:27 recapitulates Israel's vocation: YHWH called Israel to bear witness to him among the nations. Now the disciples — who have been 'with him from the beginning' — carry this witness-vocation for the Son into the world."},
      {"type": "allusion", "target": "Isa 44:8", "note": "'You are my witnesses. Is there any God besides me? No, there is no other Rock; I know not one.' Israel's witness was monotheistic testimony. The disciples' testimony to Jesus inherits this form — they testify to the one they have known from the beginning, making their word eyewitness rather than tradition."}
    ]
  },
  "16": {
    "1": [
      {"type": "allusion", "target": "Isa 48:3-5", "note": "'I foretold the former things long ago, my mouth announced them and I made them known... I told you these things long ago... so you could not say, My images brought them about.' Jesus speaks the persecution warnings now precisely so the disciples will not 'fall away' (σκανδαλισθῆτε) when they arrive — the same Isaianic logic of advance disclosure that prevents false attribution and preserves faith."}
    ],
    "2": [
      {"type": "allusion", "target": "Isa 66:5", "note": "'Hear the word of the LORD, you who tremble at his word: Your own people who hate you, and exclude you for my name's sake, have said, Let the LORD be glorified.' Isaiah's vision of communities expelling the faithful and framing it as service to God is precisely the synagogue-expulsion scenario Jesus describes — complete with the religious rationale that makes violence feel like worship."},
      {"type": "allusion", "target": "Num 25:10-13", "note": "Phinehas received a 'covenant of lasting priesthood' for his zeal in killing those who brought sin into Israel — his act was classified as atonement through violence done for God's honor. Jesus's warning that those who kill the disciples will 'think they are offering a service to God' (λατρείαν προσφέρειν) precisely identifies this Phinehas-style zealotry as the frame through which persecutors will interpret their actions."}
    ],
    "3": [
      {"type": "allusion", "target": "Isa 1:3", "note": "'The ox knows its master, the donkey its owner's manger, but Israel does not know, my people do not understand.' Persecutors will do these things 'because they have not known the Father or me' — the same Isaianic diagnosis of not-knowing as the root of violence against God's people. Not-knowing God is both cause and character of opposition to Christ and his own."}
    ],
    "4": [
      {"type": "theme", "target": "Hab 2:3", "note": "'For the revelation awaits an appointed time; it speaks of the end and will not prove false. Though it linger, wait for it; it will certainly come and will not delay.' Jesus's 'when their time comes' (ὅταν ἔλθῃ ἡ ὥρα αὐτῶν) echoes the apocalyptic 'appointed time' of Habakkuk — confidence that even persecution has a divinely delimited hour, not an open-ended catastrophe."}
    ],
    "5": [
      {"type": "allusion", "target": "Isa 55:10-11", "note": "'As the rain and the snow come down from heaven, and do not return to it without watering the earth... so is my word that goes out from my mouth: It will not return to me empty, but will accomplish what I desire.' Jesus coming from the Father and returning to the Father (made explicit in 16:28) embodies this Isaianic word-pattern: the Son going out from God to accomplish his mission and returning having completed it."}
    ],
    "6": [
      {"type": "theme", "target": "Ps 22:14-15", "note": "The psalmist in grief: 'I am poured out like water... my heart has turned to wax; it has melted within me.' The disciples' grief at being told of Jesus's departure mirrors the lament-psalm posture of one whose strength is consumed by coming catastrophe — the Evangelist places the disciples inside the Ps 22 grief that Jesus himself will inhabit on the cross."}
    ],
    "7": [
      {"type": "allusion", "target": "Ezek 36:26-27", "note": "Ezekiel's new-covenant Spirit-indwelling was contingent on the old order passing away. Jesus's 'it is for your good that I am going away' has the same logic: the physical presence of the Son in one body is the limit that must be dissolved for the universal indwelling Spirit presence to be given."},
      {"type": "allusion", "target": "Joel 2:28-29", "note": "'And afterward, I will pour out my Spirit on all people... servants, both men and women.' The Paraclete's sending — conditioned on Jesus going away — is what activates Joel's 'afterward,' which Acts 2 explicitly identifies as the day of Pentecost. John 16:7 is the pre-condition statement that explains why Joel's 'afterward' required the cross and resurrection first."}
    ],
    "8": [
      {"type": "allusion", "target": "Isa 11:4", "note": "'With righteousness he will judge the needy, with justice he will give decisions for the poor of the earth. He will strike the earth with the rod of his mouth.' The Spirit's work of proving the world wrong about sin, righteousness, and judgment is the forensic action Isaiah attributes to the Messiah's mouth — the Spirit carries forward the Messianic verdict into the world's conscience."},
      {"type": "allusion", "target": "Zech 3:1-5", "note": "The scene of Joshua the high priest before the angel with the Accuser opposing him — and the LORD rebuking the Accuser — is the courtroom frame the Paraclete (Advocate) inhabits. The Spirit comes as the divine side's advocate in the cosmic lawsuit over sin, righteousness, and judgment — the same judicial drama Zech 3 depicts."}
    ],
    "9": [
      {"type": "theme", "target": "Isa 53:6", "note": "'We all, like sheep, have gone astray, each of us has turned to our own way.' The Spirit's conviction 'about sin, because people do not believe in me' is the specific application of this universal diagnosis. Unbelief in the Son is the concrete form the general going-astray of Isa 53 takes in the new-covenant era — the Servant's diagnosis given its NT precision."}
    ],
    "10": [
      {"type": "theme", "target": "Ps 17:15", "note": "'As for me, I will be vindicated and will see your face; when I awake, I will be satisfied with seeing your likeness.' Righteousness is established by being received by the Father — Jesus's going to the Father where he can no longer be seen is his vindication. The Spirit convicts of righteousness not by exhibition but by the testimony that the Father has received the Son."}
    ],
    "11": [
      {"type": "type", "target": "Gen 3:15", "note": "'He will crush your head, and you will strike his heel.' The condemnation of 'the prince of this world' fulfills the protoevangelium — the judgment declared in Eden reaches its execution in the cross and resurrection. The ruler of this age is not merely defeated but judicially condemned (κέκριται, perfect tense: the verdict stands); Gen 3:15's promise of crushing is the type of which this judgment is the fulfillment."},
      {"type": "allusion", "target": "Dan 7:11-12", "note": "'Then I continued to watch because of the boastful words the horn was speaking. I kept looking until the beast was slain and its body destroyed.' Daniel's vision of the cosmic powers condemned at the divine court is the apocalyptic backdrop for 'the prince of this world now stands condemned' — the heavenly judgment Daniel saw is what the cross accomplishes."}
    ],
    "12": [
      {"type": "theme", "target": "Deut 29:29", "note": "'The secret things belong to the LORD our God, but the things revealed belong to us and to our children forever.' Jesus's 'I have much more to say to you, more than you can now bear' reflects the Deuteronomic boundary between hidden and revealed. The Spirit of truth will carry forward what the disciples cannot yet receive — revelation is progressive, governed by the bearer's capacity."}
    ],
    "13": [
      {"type": "allusion", "target": "Ps 25:5", "note": "'Guide me in your truth and teach me, for you are God my Savior, and my hope is in you all day long.' The Spirit will 'guide you into all the truth' — the same movement from divine source to human recipient that the psalmist prays for. The Paraclete answers Ps 25's petition with an interior guide rather than an external path."},
      {"type": "allusion", "target": "Neh 9:20", "note": "'You gave your good Spirit to instruct them.' The Levites' historical confession that God's Spirit taught Israel in the wilderness provides the OT precedent for the Paraclete's instructional role. What God did for one generation in the desert, the Spirit now does permanently for all those in union with Christ."}
    ],
    "14": [
      {"type": "theme", "target": "Isa 49:3", "note": "'He said to me, You are my servant, Israel, in whom I will display my splendor.' The Servant is the one in whom God's glory is displayed; now the Spirit glorifies the Son by making his words known to the disciples — the same pattern of glory-through-the-servant flowing from the divine source, now with the Spirit as the agent of transmission."}
    ],
    "15": [
      {"type": "theme", "target": "Dan 7:14", "note": "'He was given authority, glory and sovereign power; all nations and peoples of every language worshiped him.' Jesus's 'all that belongs to the Father is mine' states the comprehensive authority Daniel's throne-scene grants to the Son of Man — everything the Father has passes to the Son, and the Spirit draws from this inexhaustible treasury."}
    ],
    "16": [
      {"type": "allusion", "target": "Isa 26:20", "note": "'Go, my people, enter your rooms and shut the doors behind you; hide yourselves for a little while until his wrath has passed by.' The 'little while' (μικρόν) of 16:16-19 echoes Isaiah's 'little while' of divine concealment before vindication — the temporary hiddenness of the Son in death before his resurrection appearance maps onto this Isaianic pattern of brief hiddenness followed by deliverance."},
      {"type": "allusion", "target": "Hag 2:6", "note": "'This is what the LORD Almighty says: In a little while I will once more shake the heavens and the earth.' The prophetic 'little while' before decisive divine action is a recurring OT temporal marker (cited also in Heb 10:37). Jesus's μικρόν belongs to this tradition of the imminent, eschatologically charged interval before the great reversal."}
    ],
    "17": [
      {"type": "theme", "target": "Eccl 8:17", "note": "'No one can comprehend what goes on under the sun. Despite all their efforts to search it out, no one can discover its meaning.' The disciples' repeated questioning about 'what does he mean?' reflects what Qohelet states theologically: divine purposes at the hinge of the ages exceed immediate human comprehension, not from concealment but from the limits of creaturely understanding."}
    ],
    "18": [
      {"type": "theme", "target": "Isa 55:8-9", "note": "'My thoughts are not your thoughts, neither are your ways my ways... As the heavens are higher than the earth, so are my ways higher than your ways.' The disciples' 'we don't understand' is the experiential form of what Isaiah states as principle: the gap between divine speech and human comprehension is not a failure of communication but a feature of the revelatory situation."}
    ],
    "19": [
      {"type": "theme", "target": "Ps 139:1-4", "note": "'You have searched me, LORD, and you know me... you perceive my thoughts from afar. Before a word is on my tongue you, LORD, know it fully.' Jesus 'saw that they wanted to ask him' — the divine omniscience the psalmist marveled at is embodied in Jesus knowing the unspoken question. The Evangelist consistently presents Jesus as inhabiting YHWH's knowledge of the human heart."}
    ],
    "20": [
      {"type": "allusion", "target": "Isa 61:3", "note": "'To bestow on them a crown of beauty instead of ashes, the oil of gladness instead of mourning, and a garment of praise instead of a spirit of despair.' Jesus's promise 'your grief will turn to joy' recapitulates Isaiah's transformative reversal — mourning-to-joy is the Isaianic pattern for the eschatological vindication of the afflicted, now applied to the disciples' experience of resurrection."},
      {"type": "allusion", "target": "Jer 31:13", "note": "'Then young women will dance and be glad, young men and old as well. I will turn their mourning into gladness; I will give them comfort and joy instead of sorrow.' Jeremiah's new-covenant vision of mourning transformed to joy is the OT precedent for what the resurrection will accomplish — the grief at Jesus's departure reversed by his return."}
    ],
    "21": [
      {"type": "allusion", "target": "Isa 26:17-18", "note": "'As a pregnant woman about to give birth writhes and cries out in her pain, so were we in your presence, LORD.' Isaiah uses childbirth pain as a figure for Israel's suffering before eschatological deliverance. Jesus adopts the same birth-pang image — the disciples' grief is labor pain, not permanent loss; the birth (resurrection) transforms the anguish into joy the woman forgets the pain for."},
      {"type": "allusion", "target": "Mic 4:9-10", "note": "'Why do you now cry aloud — have you no king? Has your ruler perished, that pain seizes you like that of a woman in labor? Writhe in agony, Daughter Zion... You will go to Babylon; there you will be rescued.' Micah's birth-pang imagery for exile-then-redemption is exactly Jesus's schema: the disciples go through anguish (the crucifixion period) and emerge into joy (the resurrection)."}
    ],
    "22": [
      {"type": "allusion", "target": "Isa 35:10", "note": "'And those the LORD has rescued will return. They will enter Zion with singing; everlasting joy will crown their heads. Gladness and joy will overtake them, and sorrow and sighing will flee away.' The joy that no one can take away fulfills Isaiah's vision of permanent joy replacing grief at the eschatological return. The disciples' post-resurrection joy is the personal instantiation of Isa 35's communal promise."},
      {"type": "allusion", "target": "Ps 16:11", "note": "'You will fill me with joy in your presence, with eternal pleasures at your right hand.' The joy of God's presence is the psalmist's ultimate horizon; Jesus promises the same indestructible joy — rooted not in circumstance but in the relationship with the risen Son that the world cannot dissolve."}
    ],
    "23": [
      {"type": "theme", "target": "Dan 9:17-19", "note": "Daniel's prayer appeals 'for the Lord's sake' and 'for your name's sake' — the request is authorized by whose name it invokes. Jesus's transfer of petition-in-my-name from Daniel's appeal-to-God's-name pattern signals that in the new covenant, the Son's name carries the same intercessory authority the divine name carried for Daniel's prayer."}
    ],
    "24": [
      {"type": "theme", "target": "Ps 34:10", "note": "'Those who seek the LORD lack no good thing.' Jesus's invitation — 'ask and you will receive, and your joy will be complete' — is the New Covenant form of this Psalm's promise: those in union with Christ, asking in his name, discover the same principle of divine provision the psalmist attributed to seeking YHWH."}
    ],
    "25": [
      {"type": "allusion", "target": "Num 12:8", "note": "'With Moses I speak face to face, clearly and not in riddles (LXX: οὐ δι᾽ αἰνιγμάτων).' The contrast Moses enjoyed — plain speech instead of riddles — is what Jesus promises for 'that day': speaking plainly about the Father. The disciples will receive the communicative relationship Moses had, without the veiling of figures of speech that has characterized Jesus's teaching under the conditions of his earthly ministry."}
    ],
    "26": [
      {"type": "theme", "target": "Ps 91:15", "note": "'He will call on me, and I will answer him; I will be with him in trouble, I will deliver him and honor him.' The direct access Jesus promises — 'in that day you will ask in my name' — echoes the covenantal call-and-answer dynamic of Ps 91, now enacted through the Son's name as the intercessory channel rather than abstract appeal to the divine presence."}
    ],
    "27": [
      {"type": "allusion", "target": "Deut 7:9", "note": "YHWH keeps covenant love with those who love him and keep his commandments. Jesus states the symmetrical truth: the Father himself loves the disciples because they have loved the Son and believed he came from God. The Deuteronomic love-loyalty relationship between God and the faithful is now mediated through the Son — love for Jesus is the covenantal act that positions the disciple within the Father's own love."}
    ],
    "28": [
      {"type": "type", "target": "Prov 8:22-30", "note": "Wisdom speaks: 'I was formed long ago, at the very beginning... I was constantly at his side... rejoicing always in his presence.' Prov 8's pre-existent Wisdom, proceeding from God and coming into the world, is the closest OT analogy to Jesus's self-description: 'I came from the Father and entered the world; now I am leaving the world and going back to the Father.' John has identified Jesus with this divine Wisdom-Word since 1:1; 16:28 states the complete arc."},
      {"type": "allusion", "target": "Isa 55:10-11", "note": "'As the rain and snow come down from heaven... so is my word that goes out from my mouth: It will not return to me empty, but will accomplish what I desire.' Jesus's journey — from the Father, into the world, back to the Father — is the enacted form of this Isaianic word-cycle: the Son goes out and returns having accomplished the purpose for which he was sent."}
    ],
    "29": [
      {"type": "theme", "target": "Isa 40:5", "note": "'And the glory of the LORD will be revealed, and all people will see it together.' The disciples' moment of clarity — 'now you are speaking clearly and without figures of speech' — is the anticipation of unveiled revelation Isaiah projects as the eschatological disclosure of divine glory. Their comprehension now is a foretaste of the plain, unveiled speech about the Father that will characterize the post-resurrection era."}
    ],
    "30": [
      {"type": "theme", "target": "Ps 139:4", "note": "'Before a word is on my tongue you, LORD, know it fully.' The disciples recognize that Jesus 'does not even need to have anyone ask you questions' — the same omniscience attributed to YHWH in Ps 139. Their confession that Jesus knows all things is the experiential discovery of what the Psalter taught them to attribute to God alone."}
    ],
    "31": [
      {"type": "theme", "target": "Ps 118:8-9", "note": "'It is better to take refuge in the LORD than to trust in humans. It is better to take refuge in the LORD than to trust in princes.' Jesus's question 'Do you now believe?' implies the fragility of their faith — about to be tested by their scattering. The disciples will learn what the Psalm teaches: the LORD alone is trustworthy when human courage collapses."}
    ],
    "32": [
      {"type": "fulfillment", "target": "Zech 13:7", "note": "'Strike the shepherd, and the sheep will be scattered, and I will turn my hand against the little ones.' Matthew 26:31 and Mark 14:27 explicitly cite Zech 13:7 for the disciples' desertion on this same night. John does not cite the text, but the fulfillment is established by the parallel Synoptic accounts of this identical prediction — the scattering Jesus foretells here is the moment Zech 13:7 was written for."},
      {"type": "allusion", "target": "Ps 22:11", "note": "'Do not be far from me, for trouble is near and there is no one to help.' The forsaken righteous sufferer of Ps 22 faces abandonment — 'you will leave me all alone' — which Jesus accepts not with despair but with the confidence that the Father is with him. He enters the psalmist's experience of abandonment while maintaining the psalmist's faith in the God who does not hide his face."}
    ],
    "33": [
      {"type": "allusion", "target": "Dan 7:14", "note": "'He was given authority, glory and sovereign power... His dominion is an everlasting dominion that will not pass away.' 'I have overcome the world' is the personal appropriation of the authority the Son of Man receives in Daniel's throne-room vision. The victory Jesus declares in the present perfect (νενίκηκα) is the enacted fulfillment of Daniel's courtroom award."},
      {"type": "type", "target": "Gen 3:15", "note": "The protoevangelium: 'He will crush your head, and you will strike his heel.' The entire arc of the Farewell Discourse leads to this declaration of victory — 'I have overcome the world' is the fulfillment of Gen 3:15's promise. The cross is the heel-strike; the resurrection is the head-crushing. The disciples' peace is grounded in a victory accomplished at the cosmic level before their trouble begins."},
      {"type": "allusion", "target": "Ps 46:1-2", "note": "'God is our refuge and strength, an ever-present help in trouble. Therefore we will not fear, though the earth give way.' Jesus's offer of 'peace' in the face of 'trouble' (θλίψις) echoes the Psalm's confidence in divine presence as the ground of fearlessness. The peace comes not from the absence of tribulation but from the presence of the overcomer."}
    ]
  }
}


def main():
    existing = load_echo('john')
    merge_echo(existing, JOHN_ECHOES)
    save_echo('john', existing)
    print('John 14–16 echoes written.')

if __name__ == '__main__':
    main()
