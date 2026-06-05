"""
MKT Echo Layer — Romans chapters 15–16
Run: python3 scripts/zc-echo-romans-15-16.py

Source data used:
- data/interlinear/romans.json
- data/translation/glossary-greek.json
- data/translation/draft/mediating/romans.json
- data/parallels/romans.json (absorbed: 15:3 Ps 69:9; 15:9 Ps 18:49;
  15:10 Deut 32:43; 15:11 Ps 117:1; 15:12 Isa 11:10; 15:21 Isa 52:15;
  16:20 Gen 3:15)
- data/commentary/ellicott/romans.json (philological notes on 15:3, 15:10,
  15:16, 15:20–21, 16:20)
- data/commentary/jfb/romans.json

Key decisions in this range:
- 15:3 Ps 69:9 — Paul quotes LXX; classified quote. In the original Psalm the
  speaker suffers for zeal for God's house; Paul reads the Psalm as messianic
  type (the suffering of Christ bearing what was aimed at the Father).
- 15:9 Ps 18:49 (= 2 Sam 22:50) — Paul's citation follows the Psalms version;
  David sang this among the nations, and Paul reads it as pointing to Christ
  praising God among the Gentiles through his apostolic mission.
- 15:10 Deut 32:43 — Paul follows LXX which explicitly has "Gentiles" in the
  imperative; MT is more ambiguous. Classified quote.
- 15:12 Isa 11:10 — Paul explicitly names Isaiah; the LXX reading diverges from
  MT in ways that make the messianic universalism more explicit. Classified
  fulfillment: Paul presents this as realized in Christ's resurrection-reign.
- 15:21 Isa 52:15 — Paul applies the Servant passage to his own pioneer mission:
  the Servant who startles the nations and silences kings is now active through
  the apostolic proclamation. Classified fulfillment.
- 16:20 Gen 3:15 — the protoevangelium. The crushing of the serpent's head is
  fulfilled in Christ's victory, and the community participates in that victory
  as recipients of the same authority. Classified type (the structural
  correspondence between woman's seed / Satan and Christ / community of faith /
  the powers).
- 15:16 Isa 66:18–20 — the "offering of the Gentiles" language (prosphora) makes
  this a deliberate echo of Isa 66:20 where nations bring God's people as an
  offering to Jerusalem; Paul inverts the direction: Gentiles themselves become
  the sanctified offering, classified allusion.
- Greeting verses (16:1–16, 21–24) — brief thematic echoes; where no verbal or
  structural parallel is defensible, echo is not forced.
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
  "15": {
    "1": [
      {"type": "allusion", "target": "Isa 53:4", "note": "The Servant 'took up our infirmities and carried our sorrows' — Paul's call for the strong to 'bear the infirmities (asthenēmata) of the weak' uses the same structural logic: willingness to take on another's burden as the governing posture of those with capacity, grounded in Christ's own bearing of human weakness."},
      {"type": "theme", "target": "Num 11:12-17", "note": "Moses' complaint that he cannot bear the weight of all the people alone — the burden-bearing motif in Israel's leadership tradition is fulfilled in Christ who bears the whole, and the community is now called to replicate that pattern among themselves in the manner of the seventy elders sharing Moses' load."}
    ],
    "2": [
      {"type": "allusion", "target": "Jer 31:28", "note": "God's new covenant promise to 'build and plant' after the era of judgment — Paul's goal that the strong please the neighbor 'for his good, to build him up' (oikodomē) participates in the Jeremianic new-covenant vocabulary of constructive restoration rather than destructive individualism."}
    ],
    "3": [
      {"type": "quote", "target": "Ps 69:9", "note": "Paul cites the LXX of Ps 69:9: 'The insults of those who insult you have fallen on me.' In the Psalm the speaker suffers because his zeal for God's house makes him the target of those who scorn God; Paul reads Christ as the definitive fulfillment of this pattern — he who pleased not himself bore the reproaches aimed at the Father, making the Psalm a messianic type of vicarious suffering."}
    ],
    "4": [
      {"type": "theme", "target": "Deut 31:19-22", "note": "God commanded Moses to write the Song to serve as a witness and teacher for future generations in Israel — Paul's principle that 'everything written in the past was written to teach us' articulates the same rationale for Scripture: the texts endure beyond their immediate occasion precisely to form patience and hope in later readers."},
      {"type": "theme", "target": "Ps 119:49-50", "note": "'Remember your word to your servant, for you have given me hope. My comfort in my suffering is this: your promise preserves my life' — the psalmist models what Paul describes: the Scripture-generated hope that sustains through suffering; the word does not merely inform but actively produces endurance."}
    ],
    "5": [
      {"type": "theme", "target": "Ps 133:1", "note": "'How good and pleasant it is when God's people live together in unity!' — Paul's benediction that God give the community 'the same mind (to auto phronein) toward one another' prays for what Ps 133 celebrates as a covenantal blessing; the unity Paul seeks is not uniformity but the God-given concord of those who share a single Lord."}
    ],
    "6": [
      {"type": "allusion", "target": "Zeph 3:9", "note": "God's eschatological promise: 'I will purify the lips of the peoples, that all of them may call on the name of the Lord and serve him shoulder to shoulder' — Paul's goal that the community praise 'with one mind and one voice' (en heni stomati) the God and Father of Christ is the realized form of Zephaniah's eschatological liturgical unity, Jew and Gentile worshiping together."}
    ],
    "7": [
      {"type": "allusion", "target": "Gen 12:3", "note": "God's promise to Abraham that 'all peoples on earth will be blessed through you' — Christ's acceptance of both the weak and the strong, Jew and Gentile, is the fulfillment of the Abrahamic promise of universal blessing; 'as Christ accepted you' frames mutual welcome as the embodied form of the gospel's reach to all nations."}
    ],
    "8": [
      {"type": "fulfillment", "target": "Gen 15:1-6", "note": "God's covenant promise to Abraham — children as numerous as the stars — which Paul in ch. 4 identified as the foundation of righteousness by faith. Christ's role as 'servant of the circumcision to confirm the promises made to the patriarchs' means the Abrahamic covenant-chain now reaches its intended destination through Christ's fidelity."},
      {"type": "fulfillment", "target": "2 Sam 7:12-13", "note": "The Davidic covenant's promise of a son who would confirm God's faithfulness — Paul's claim that Christ became a servant to 'confirm the promises made to the patriarchs' includes the Davidic promise; Christ as servant-king is the faithful confirmation of what God pledged to David concerning an enduring royal line."}
    ],
    "9": [
      {"type": "quote", "target": "Ps 18:49", "note": "Paul cites the LXX of Ps 18:49 (= 2 Sam 22:50): 'Therefore I will praise you among the Gentiles; I will sing the praises of your name.' David composed this thanksgiving after deliverance from his enemies; Paul reads Christ as the ultimate speaker of David's words — the risen Son of David glorifying God among the nations through his apostolic mission is the fulfillment of this royal doxology."}
    ],
    "10": [
      {"type": "quote", "target": "Deut 32:43", "note": "Paul quotes from the Song of Moses (Deut 32:43 LXX): 'Rejoice, O Gentiles, with his people.' The Song was Israel's final covenant renewal text, anticipating God's vindication and the Gentiles' call to join Israel's celebration; Paul deploys it as scriptural testimony that Gentile inclusion in the worship of Israel's God was embedded in the founding texts of Israel's covenant life."}
    ],
    "11": [
      {"type": "quote", "target": "Ps 117:1", "note": "Paul quotes the shortest Psalm in its entirety: 'Praise the Lord, all you Gentiles; let all the peoples extol him.' The psalm summons every nation to praise Israel's God precisely because of his covenant faithfulness (hesed) and truth (emet); Paul's citation confirms that universal Gentile praise was not a Pauline novelty but the declared scope of Israel's own doxological tradition."}
    ],
    "12": [
      {"type": "fulfillment", "target": "Isa 11:10", "note": "Paul cites the LXX of Isa 11:10: 'The Root of Jesse will spring up, one who will arise to rule over the nations; in him the Gentiles will hope.' Isaiah's 'Root of Jesse' is the messianic shoot from the apparently dead Davidic line; Paul explicitly names this as Isaiah's prophecy and presents Christ's resurrection-reign as its fulfillment — the risen king now rules over the nations, and the Gentiles' hope in him is the realization of what Isaiah anticipated."}
    ],
    "13": [
      {"type": "theme", "target": "Ps 71:5", "note": "'For you have been my hope, Sovereign Lord, my confidence since my youth' — the psalmist's identification of God himself as the ground and object of hope is the OT foundation for Paul's doxological title 'God of hope'; hope is not a human disposition but a gift of the one who is inherently hope-giving."},
      {"type": "theme", "target": "Isa 11:2", "note": "The Spirit of God resting on the messianic king — Paul's prayer that the community overflow with hope 'by the power of the Holy Spirit' participates in the Isaianic pattern where the messianic era is characterized by Spirit-given abundance; the Spirit's empowerment of hope is the extension of the Spirit's presence in the Root of Jesse to his whole community."}
    ],
    "14": [
      {"type": "allusion", "target": "Jer 31:33-34", "note": "The new covenant promise that 'they will all know me' — Paul's confidence that the Roman believers are 'full of goodness, filled with knowledge' reflects the realized dimension of Jeremiah's new covenant: the community indwelt by God's Spirit possesses the knowledge that the old covenant could not inscribe by law alone; Paul's assurance is simultaneously a new covenant recognition."}
    ],
    "15": [
      {"type": "theme", "target": "Ezek 3:17-21", "note": "God's commission to Ezekiel as a watchman responsible to remind and warn the people — Paul's apologetic reference to writing 'to remind you of them again, because of the grace God gave me' echoes the prophetic pattern of commission-based reminder; the apostolic office carries the same obligation to stir up the memory of God's people that the prophetic office bore."}
    ],
    "16": [
      {"type": "allusion", "target": "Isa 66:18-20", "note": "God gathers the nations and they bring Israel's scattered people 'as an offering (minchah) to the Lord' from all nations to Jerusalem — Paul's description of his 'priestly duty of proclaiming the gospel so that the Gentiles might become an offering (prosphora) acceptable to God, sanctified by the Holy Spirit' directly inverts and fulfills this text: not Israelites brought from Gentile lands, but Gentiles themselves becoming the sanctified offering, the nations now arriving as the gift."},
      {"type": "allusion", "target": "Isa 60:7", "note": "The nations' flocks coming as offerings acceptable on God's altar — the Isaianic vision of eschatological offerings from all nations provides the second stream of the imagery Paul draws on when he describes the Gentiles as a sanctified offering; the priestly language Paul uses maps directly onto the temple-offering context Isaiah anticipated."}
    ],
    "17": [
      {"type": "theme", "target": "Jer 9:23-24", "note": "Jeremiah's prohibition of boasting in wisdom, strength, or riches — 'but let the one who boasts boast in this: that they have the understanding to know me' — Paul's 'I glory in Christ Jesus in my service to God' is the Christological form of Jeremiah's redirected boasting: the only legitimate boast is in what God has done through Christ, not in Paul's own capacity."}
    ],
    "18": [
      {"type": "theme", "target": "Deut 4:34", "note": "Moses asks whether any god has taken a nation for himself through signs and wonders and a mighty hand — Paul's appeal to 'what Christ has accomplished through me in leading the Gentiles to obey God by what I have said and done' echoes the Deuteronomic category of divine action authenticated through signs and wonders; Christ's work through Paul stands in the tradition of theophanic, nation-forming activity."}
    ],
    "19": [
      {"type": "theme", "target": "Isa 2:3", "note": "'The law will go out from Zion, the word of the Lord from Jerusalem' — Paul's description of his mission beginning 'from Jerusalem all the way around to Illyricum' places Jerusalem as the apostolic center from which the gospel radiates, fulfilling the Isaianic picture of Torah-word going out from Zion to the nations, now in the form of apostolic gospel proclamation."},
      {"type": "allusion", "target": "Isa 11:12", "note": "The Root of Jesse 'will raise a banner for the nations and gather the exiles of Israel' — Paul's account of gospel proclamation through signs and wonders as the instrument of Gentile obedience participates in the Isaianic picture of the messianic king gathering the nations; the signs authenticate the messenger of the one who 'will be sought by the nations.'"}
    ],
    "20": [
      {"type": "allusion", "target": "Isa 28:16", "note": "God lays a tested, precious cornerstone in Zion — 'the one who relies on it will never be stricken with panic.' Paul's ambition not to build on another's foundation echoes the imagery of the cornerstone as the unique foundation already laid; Paul does not presume to re-lay what has been established but to build the structure outward into new territory where the foundation has not yet reached."}
    ],
    "21": [
      {"type": "fulfillment", "target": "Isa 52:15", "note": "Paul quotes LXX Isa 52:15: 'Those who were not told about him will see, and those who have not heard will understand.' In Isaiah this follows the Servant's exaltation after suffering, when kings fall silent and nations see what they had not been told. Paul reads his own pioneer mission as the fulfillment of the Servant's proclamation: the unreached peoples who could not know the Servant are now seeing and understanding through apostolic proclamation."}
    ],
    "22": [
      {"type": "theme", "target": "Prov 16:9", "note": "'In their hearts humans plan their course, but the Lord establishes their steps' — Paul's account of being 'often hindered' from coming to Rome reflects the OT theological framework in which divine providence shapes human movement; the hindrance is not personal failure but the same divine ordering of apostolic movement that directed Paul's mission throughout (cf. Acts 16:6-7)."}
    ],
    "23": [
      {"type": "theme", "target": "Ps 84:1-2", "note": "'How lovely is your dwelling place, Lord Almighty! My soul yearns, even faints, for the courts of the Lord' — Paul's 'longing for many years to visit you' uses the same vocabulary of deep desire (epipothia); the apostolic longing for the community mirrors the psalmist's covenant yearning for God's presence, here expressed toward the body of Christ."}
    ],
    "24": [
      {"type": "theme", "target": "Ps 72:8-11", "note": "The Davidic king ruling 'from sea to sea' and to 'the ends of the earth,' with all kings bowing before him — Paul's ambition to reach Spain, the western end of the known world, is shaped by the Psalm's vision of messianic dominion extending to the earth's limits; the apostle goes where the king's gospel must go if the Psalm's scope is to be realized."}
    ],
    "25": [
      {"type": "allusion", "target": "Deut 26:1-11", "note": "The Israelite bringing the first-fruits offering to Jerusalem as a liturgical act of covenant faithfulness — Paul's journey to Jerusalem 'in the service of the Lord's people there' with the Gentile collection mirrors the Deuteronomic first-fruits pattern: the Gentile churches send their offering to the Jerusalem community as an act of covenant solidarity, the collection functioning as a liturgical first-fruits of Gentile participation in Israel's inheritance."}
    ],
    "26": [
      {"type": "theme", "target": "Isa 60:5-6", "note": "Nations streaming to Jerusalem, their wealth and resources flowing in — 'the wealth of the nations will come to you; caravans of camels will cover your land.' The Macedonian and Achaian collection for the poor saints in Jerusalem participates in the Isaianic eschatological pattern of nations bringing their resources to God's people, though Paul's immediate rationale is explicitly covenantal reciprocity (v.27) rather than tribute."}
    ],
    "27": [
      {"type": "allusion", "target": "Lev 19:18", "note": "'Love your neighbor as yourself' — Paul's principle that Gentiles who have 'shared in the Jews' spiritual blessings' are obligated (opheiletai) to share material blessings draws on the Levitical neighbor-love command, now applied across the Jew-Gentile boundary that the gospel has redefined; covenant obligation extends to those who have become one people in Christ."},
      {"type": "theme", "target": "Isa 61:6", "note": "God promises that his people will 'feed on the wealth of nations' and that the nations 'will be named priests of the Lord, ministers of our God' — Paul's principle of Gentile material sharing for Jewish spiritual sharing is the eschatological flip-side of Isaiah's picture of covenant exchange between nations and Israel in the messianic age."}
    ],
    "28": [
      {"type": "theme", "target": "Neh 13:13", "note": "Nehemiah 'putting in charge' trustworthy men to distribute the offering — the careful completion and secure delivery of the collection, which Paul describes as 'sealing this fruit to them,' participates in the tradition of faithful stewardship of communal offerings from distant communities to Jerusalem, a pattern of post-exilic covenant maintenance that Paul's collection extends to the Gentile world."}
    ],
    "29": [
      {"type": "allusion", "target": "Ps 21:3", "note": "'You came to greet him (the king) with rich blessings and placed a crown of pure gold on his head' — the language of 'fulness of blessing' with which Paul expects to come echoes the royal gift-language of the Psalms; the apostle arrives not with empty hands but bearing the covenant abundance that Christ the king has already secured for his people."}
    ],
    "30": [
      {"type": "allusion", "target": "Exod 17:10-13", "note": "Aaron and Hur holding up Moses' arms during the battle with Amalek — Paul's request that the Romans 'join him in his struggle by praying' evokes this precedent of communal support sustaining the leader in a spiritual-physical combat; the apostle's mission depends on the community's intercessory participation just as Israel's battle depended on the uplifted arms of Moses."},
      {"type": "allusion", "target": "Ps 122:6", "note": "'Pray for the peace of Jerusalem; may those who love her be secure' — Paul's prayer-request before going to Jerusalem, seeking safety and a favorable reception, echoes the psalmist's summons to intercede for Jerusalem; the apostle carries forward the same concern for the mother-community's welfare, now under apostolic rather than royal patronage."}
    ],
    "31": [
      {"type": "theme", "target": "Neh 4:1-2", "note": "The returned community in Jerusalem threatened by those who did not want the work completed — Paul's prayer for deliverance from 'unbelievers in Judea' who might obstruct his mission echoes the Nehemiah pattern: the servant of God carrying out God's purpose for Jerusalem faces opposition from those within the land who resist the work."},
      {"type": "theme", "target": "Deut 26:10-11", "note": "The worshiper presenting the first-fruits offering 'before the Lord your God' and rejoicing — Paul's prayer that the collection be 'favorably received' by the Jerusalem saints mirrors the Deuteronomic concern that the offering be acceptable; what Deut 26 describes as a ritual presentational act, Paul now describes as a relational offering carrying the weight of Jew-Gentile solidarity."}
    ],
    "32": [
      {"type": "theme", "target": "Isa 40:31", "note": "'Those who hope in the Lord will renew their strength; they will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint' — Paul's prayer to 'come with joy and be refreshed in your company by God's will' echoes the Isaianic promise of renewal and restoration after labor; the visit to Rome is envisioned as a Spirit-given refreshment in the tradition of covenantal re-energizing."}
    ],
    "33": [
      {"type": "allusion", "target": "Num 6:24-26", "note": "The Aaronic blessing: 'The Lord bless you and keep you; the Lord make his face shine on you and be gracious to you; the Lord turn his face toward you and give you peace (shalom)' — Paul's closing 'the God of peace be with you all' is the apostolic crystallization of the priestly blessing into a covenant benediction, the shalom of Num 6 now named by its giver's character rather than its content."},
      {"type": "theme", "target": "Ps 29:11", "note": "'The Lord gives strength to his people; the Lord blesses his people with peace' — the Psalter's consistent association of the God who blesses with the gift of peace (shalom) is the liturgical background for Paul's concluding epithet; the 'God of peace' is not a novel Pauline formula but the doxological title that Israel's worship had prepared."}
    ]
  },
  "16": {
    "1": [
      {"type": "theme", "target": "Prov 31:10-31", "note": "The 'capable woman' (eshet hayil) who serves, protects, and provides for the community — Phoebe commended as diakonos (deacon/minister) and prostatis (benefactor/patron) inhabits the OT category of the capable woman whose diligent service creates a community of flourishing; the prostatis role Paul names was the form this capacity took in the Greco-Roman world."}
    ],
    "2": [
      {"type": "theme", "target": "Deut 10:18-19", "note": "God's command to welcome the foreigner because 'you were foreigners in Egypt' — Paul's instruction to 'receive her in the Lord in a way worthy of his people' and 'give her any help she may need' applies the Deuteronomic welcome-of-the-stranger ethic within the covenant community; the church at Rome is to embody the same hospitality that covenant Israel was called to practice."}
    ],
    "3": [
      {"type": "theme", "target": "Num 11:16-17", "note": "God gathering seventy elders to share Moses' leadership burden — Paul's greeting of 'co-workers in Christ Jesus' reflects the OT pattern of shared mission where no one leader bears the full weight alone; Prisca and Aquila embody the co-laborer structure that Israel's leadership tradition anticipated in the sharing of Moses' spirit among the elders."}
    ],
    "4": [
      {"type": "theme", "target": "Esth 4:16", "note": "Esther's willingness to risk her life approaching the king — 'if I perish, I perish' — Prisca and Aquila 'risked their own necks' for Paul in the same tradition of covenant loyalty willing to accept death for the community's sake; the willingness to lay down one's life for another's mission is the OT pattern of hesed-driven self-sacrifice."}
    ],
    "5": [
      {"type": "theme", "target": "Exod 12:3-7", "note": "The Passover celebrated by household units ('each man to take a lamb for his family, one for each household') — the house church meeting in Prisca and Aquila's home is the new covenant equivalent of the household-based Passover assembly; the gathered community in a home is the New Exodus form of the original Passover structure."}
    ],
    "6": [
      {"type": "theme", "target": "Prov 31:17", "note": "'She sets about her work vigorously; her arms are strong for her tasks' — Mary who 'worked very hard' for the community is described with the same language of diligent, physically costly labor that Proverbs 31 celebrates; the women who labor in Paul's letters participate in the OT portrait of faithful and costly service as honor."}
    ],
    "7": [
      {"type": "theme", "target": "Ps 22:4-5", "note": "'In you our ancestors put their trust; they trusted and you delivered them' — the description of Andronicus and Junia as 'outstanding among the apostles' who 'were in Christ before I was' honors their seniority in the community of those who trusted; the elders of faith stand in the line of ancestors who anchored trust in God across generations."}
    ],
    "8": [
      {"type": "theme", "target": "Ps 16:3", "note": "'As for the holy people who are in the land, they are the noble ones in whom is all my delight' — Paul's greeting of 'my dear friend Ampliatus in the Lord' mirrors the psalmist's delight in the covenant community; the 'beloved in the Lord' are those whose union with Christ places them within the sphere of divine delight that the psalm celebrates."}
    ],
    "9": [
      {"type": "theme", "target": "Isa 41:6", "note": "'They help each other and say to their companions, Be strong!' — the language of co-workers and helpers in shared mission echoes the OT vision of mutual strengthening in God's service; the co-worker (synergos) relationship that Paul celebrates is the apostolic form of the mutual reinforcement Israel's prophetic tradition calls for."}
    ],
    "10": [
      {"type": "allusion", "target": "Ps 17:3", "note": "'You have tested my heart; you have examined me at night and found nothing wrong; I have resolved that my mouth will not sin' — Apelles 'approved in Christ' (ho dokimos) carries the vocabulary of the tested and vindicated person that Ps 17:3 describes; the 'approved' member of the community has passed the kind of divine examination the psalmist invokes."}
    ],
    "11": [
      {"type": "allusion", "target": "Josh 24:15", "note": "Joshua's declaration: 'As for me and my household, we will serve the Lord' — the greeting of those 'in the household of Narcissus who are in the Lord' reflects the OT household-faith structure where an entire household aligns under a single covenantal allegiance; the pattern of household-level covenant commitment shapes how Paul greets and honors these groups."}
    ],
    "12": [
      {"type": "theme", "target": "Prov 31:27-31", "note": "The capable woman 'who watches over the affairs of her household and does not eat the bread of idleness' — Tryphena, Tryphosa, and Persis who 'work hard in the Lord' are described in terms resonant with the Proverbs 31 portrait; their labor is honored precisely because Proverbs established diligent service as worthy of public praise ('let her works bring her praise at the city gate')."}
    ],
    "13": [
      {"type": "allusion", "target": "Isa 43:10", "note": "'You are my witnesses... and my servant whom I have chosen' — 'Rufus, chosen in the Lord' (ton eklekton en kyriō) carries the election-language that throughout Paul's letter refers to God's sovereign choice; the language reaches back to the OT vocabulary of divine selection (bachar / eklektos) applied first to Israel and the Servant, now distributed to individual members of the covenant community."}
    ],
    "14": [
      {"type": "theme", "target": "Neh 3:1-32", "note": "Nehemiah's list of builders who worked side by side rebuilding Jerusalem's walls — the roster of names in vv.14–15 participates in the OT literary convention of communal lists that honor the members of God's building-work; the names matter because the individuals matter to the covenant community's project of construction."}
    ],
    "15": [
      {"type": "theme", "target": "Neh 12:1-26", "note": "The list of priests, Levites, and community leaders who returned with Zerubbabel and Ezra — the catalog of greeted believers in 16:14–15 is the apostolic equivalent of these covenant-renewal rosters; naming the individuals is itself a covenantal act that recognizes their belonging to God's reconstituted people."}
    ],
    "16": [
      {"type": "allusion", "target": "Ps 133:1-3", "note": "'How good and pleasant it is when God's people live together in unity! ... For there the Lord bestows his blessing, even life forevermore' — Paul's instruction to 'greet one another with a holy kiss' establishes a physical embodiment of the unity Ps 133 describes; the greeting is not a social convention but a covenant act expressing the brotherly dwelling together that the psalm associates with God's blessing."}
    ],
    "17": [
      {"type": "allusion", "target": "Ezek 34:1-6", "note": "God's indictment of shepherds who scatter and harm the flock — Paul's warning about those who 'cause divisions and put obstacles in your way that are contrary to the teaching you have learned' applies the prophetic category of destructive leaders to the Roman situation; those who scatter rather than gather the flock stand under the same divine censure."},
      {"type": "allusion", "target": "Jer 23:1-2", "note": "'Woe to the shepherds who are destroying and scattering the sheep of my pasture!' — the divisive teachers Paul warns against in Rome are the fulfillment of the type of false shepherd the prophets repeatedly condemned; their destruction of unity and their causing of 'offenses' (skandala) maps directly onto Jeremiah's portrait of those who mislead the flock."}
    ],
    "18": [
      {"type": "allusion", "target": "Mic 3:5", "note": "'As for the prophets who lead my people astray, they proclaim peace when they have something to eat, but prepare to wage war against anyone who refuses to feed them' — Paul's 'smooth talk and flattery' (chrestologia kai eulogia) that deceives the naive is the NT form of Micah's 'prophets who lead people astray' by means of persuasive speech that serves self-interest; the appetite-driven teacher was a recognized prophetic category."}
    ],
    "19": [
      {"type": "allusion", "target": "Gen 3:1", "note": "The serpent's craftiness (arum in Hebrew) which deceives the innocent — Paul's command to 'be wise about what is good, and innocent (akeraios, unmixed/pure) about what is evil' is the reversal of Eden's catastrophe: the serpent's wisdom-toward-evil corrupted human innocence; Paul calls for the recovery of simplicity-toward-evil while cultivating knowledge-of-good, the pattern inverted from the Fall."},
      {"type": "allusion", "target": "Prov 3:7", "note": "'Do not be wise in your own eyes; fear the Lord and shun evil' — Paul's command to be wise in what is good and innocent in what is evil echoes the Proverbs pattern of discernment: wisdom is not clever navigation of evil but the right orientation toward good through fear of the Lord, which produces the very simplicity toward evil that Paul commends."}
    ],
    "20": [
      {"type": "type", "target": "Gen 3:15", "note": "The protoevangelium: 'I will put enmity between you and the woman, and between your offspring and hers; he will crush your head, and you will strike his heel.' Paul's promise that 'the God of peace will soon crush Satan under your feet' is the community's participation in this founding type — Christ is the seed who accomplishes the crushing; the Roman believers, as those united to him, share in the authority of his victory over the serpent."},
      {"type": "allusion", "target": "Ps 110:1", "note": "The Lord's declaration to the Davidic king: 'Sit at my right hand until I make your enemies a footstool for your feet' — the 'under your feet' language of v.20 deliberately echoes this royal enthronement psalm that the early church consistently applied to Christ's resurrection-exaltation; the Roman community participates in the footstool-victory that belongs first to the risen king."}
    ],
    "21": [
      {"type": "theme", "target": "Num 11:26-29", "note": "Moses' desire that 'all the Lord's people were prophets and that the Lord would put his Spirit on them' — the community of co-workers and 'fellow Jews' who participate in Paul's apostolic mission embodies the Mosaic vision of a Spirit-distributed ministry not confined to one person; the network of Timothy, Lucius, Jason, and Sosipater is the realized form of shared apostolic labor."}
    ],
    "22": [
      {"type": "theme", "target": "Jer 36:4-6", "note": "Baruch the scribe who wrote Jeremiah's words at his dictation and then read them publicly — Tertius who 'wrote down this letter' stands in the tradition of the prophetic amanuensis; the scribe's role in preserving and transmitting the word of God was established in Israel's prophetic tradition before it was regularized in apostolic correspondence."}
    ],
    "23": [
      {"type": "theme", "target": "Gen 18:1-8", "note": "Abraham's hospitality to the three visitors at Mamre — 'the whole church here enjoys' the hospitality of Gaius; the pattern of radical hospitality extended to all who came, including the wider community, is the patriarchal model that Paul's ecclesial hospitality tradition inherits and formalizes in the house-church context."}
    ],
    "24": [
      {"type": "theme", "target": "Num 6:24-26", "note": "The Aaronic grace-blessing — Paul's repeated grace benedictions (cf. 16:20) draw from the same priestly reservoir as the Aaronic blessing; the 'grace of our Lord Jesus Christ' formula is the Christological specification of the same divine favor that the Aaronic blessing invoked over Israel."}
    ],
    "25": [
      {"type": "allusion", "target": "Dan 2:28-30", "note": "God in Babylon 'reveals deep and hidden things' and 'reveals mysteries' (razin — Daniel 2:28 Aramaic) to make known what will happen — Paul's doxology credits God as the one 'able to establish you according to... the revelation of the mystery hidden for long ages past.' The mystery-disclosure pattern Paul employs is the Daniel framework: what was sealed in the prophets is now the subject of divine unveiling at the appointed time."},
      {"type": "allusion", "target": "Amos 3:7", "note": "'Surely the Sovereign Lord does nothing without revealing his plan to his servants the prophets' — Paul's 'mystery... now revealed through the prophetic writings by the command of the eternal God' affirms the same principle: the prophets were the ordained channel of advance disclosure; the 'prophetic writings' are the medium through which the mystery, hidden then, is now made known."}
    ],
    "26": [
      {"type": "allusion", "target": "Isa 46:10", "note": "God declares: 'I make known the end from the beginning, from ancient times, what is still to come' — Paul's claim that the mystery is 'now revealed' presupposes exactly this Isaianic God who embedded the announcement of the future within the ancient texts; the prophetic writings that now disclose the mystery were vehicles of God's foreknowledge from the beginning."},
      {"type": "allusion", "target": "Isa 52:10", "note": "'The Lord will lay bare his holy arm in the sight of all the nations, and all the ends of the earth will see the salvation of our God' — Paul's doxological conclusion that the mystery is made known 'so that all the Gentiles might come to the obedience that comes from faith' is the realization of Isaiah's promise that God's saving action would be disclosed to all nations; the doxology celebrates the arrival of what the Second Exodus texts anticipated."}
    ],
    "27": [
      {"type": "theme", "target": "Ps 96:7-8", "note": "'Ascribe to the Lord glory and strength; ascribe to the Lord the glory due his name. Bring an offering and come into his courts' — Paul's doxological 'to the only wise God be glory forever through Jesus Christ!' is the apostolic form of the Psalter's summons to ascribe glory to the one God; the 'only' (mono-) reinforces the Shema monotheism that the doxologies of the Psalms celebrate."},
      {"type": "theme", "target": "1 Chr 29:11-13", "note": "David's prayer at the close of his reign: 'Yours, Lord, is the greatness and the power and the glory and the majesty and the splendor... yours is the kingdom... wealth and honor come from you... we give you thanks and praise your glorious name' — Paul's closing doxology ('to the only wise God be glory forever') stands in this tradition of attributing all wisdom, glory, and kingdom to God alone, which the Davidic covenant's conclusion established as the proper response to covenant fulfillment."}
    ]
  }
}

def main():
    existing = load_echo('romans')
    merge_echo(existing, ROMANS_ECHOES)
    save_echo('romans', existing)
    print('Romans 15–16 echoes written.')

if __name__ == '__main__':
    main()
