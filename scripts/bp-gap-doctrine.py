import json, os, pathlib

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def load_article(slug):
    p = pathlib.Path(OUT_DIR) / f'{slug}.json'
    return json.loads(p.read_text()) if p.exists() else None

def save_article(slug, data):
    p = pathlib.Path(OUT_DIR) / f'{slug}.json'
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False))

def merge_article(slug, data):
    if load_article(slug) is not None: return False
    save_article(slug, data); return True

ARTICLES = {
"angel-a-spirit": {
  "term": "Angel (A Spirit)",
  "category": "concepts",
  "intro": "<p>Angels (Hebrew <em>malak</em>; Greek <em>angelos</em>, \"messenger\") are personal spiritual beings who serve as God's heavenly court, messengers, and agents of his purposes throughout the biblical narrative. As spirits they are not bound by physical limitation (Heb. 1:14: \"ministering spirits sent to serve those who will inherit salvation\"), yet they frequently appear in human form to communicate divine revelation or accomplish specific missions. The OT records angels ministering at decisive moments — announcing the birth of Samson (Judg. 13), standing at the burning bush, delivering the law at Sinai (Gal. 3:19), and protecting God's people (Ps. 91:11–12; Dan. 6). In the NT, angels announce Jesus' conception (Matt. 1:20), birth (Luke 2:10), resurrection (Matt. 28:2–7), and ascension (Acts 1:10–11), and minister to Jesus in Gethsemane (Luke 22:43). Paul affirms their existence while warning against their worship (Col. 2:18). The book of Revelation depicts angels as active instruments of eschatological judgment. As created spiritual beings they are distinct from the divine, subordinate to Christ (Heb. 1:4–14), and do not marry or die (Matt. 22:30; Luke 20:36).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "angel-a-spirit"},
  "key_refs": ["Matthew 1:20", "Hebrews 1:14", "Psalms 91:11", "Revelation 5:11"]
},
"obedience": {
  "term": "Obedience",
  "category": "concepts",
  "intro": "<p>Obedience in Scripture denotes the willing, responsive submission to God's revealed will as the proper expression of covenant loyalty and faith. Under the Mosaic covenant, obedience was the condition of blessing: \"If you will indeed obey my voice and keep my covenant, you shall be my treasured possession\" (Ex. 19:5). The prophets diagnosed Israel's covenant failures as fundamentally a problem of disobedience (Isa. 1:19–20; Jer. 7:23). The NT deepens the concept: Jesus himself became the obedient Son, learning obedience through suffering (Heb. 5:8) and becoming \"obedient to death, even death on a cross\" (Phil. 2:8), reversing Adam's disobedience (Rom. 5:19). Paul's gospel aims at \"the obedience of faith\" among all nations (Rom. 1:5; 16:26). John equates love for God with obedience to his commands: \"Whoever keeps his word, in him truly the love of God is perfected\" (1 John 2:5). James insists that obedience — doing the word, not merely hearing — is the mark of genuine faith (Jas. 1:22–25). Obedience is thus both the evidence of saving faith and the ongoing life of the believer in relationship with God.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "obedience"},
  "key_refs": ["Exodus 19:5", "Philippians 2:8", "Romans 5:19", "1 John 2:5"]
},
"judgment": {
  "term": "Judgment",
  "category": "concepts",
  "intro": "<p>Judgment (Hebrew <em>mishpat</em>; Greek <em>krisis</em>, <em>krima</em>) is a fundamental attribute of God expressed throughout both Testaments as his righteous governance of the moral order of creation. God is the judge of all the earth (Gen. 18:25; Ps. 96:13) who renders impartial verdicts based on truth (Rom. 2:2). Temporal judgments in the OT — the Flood, the destruction of Sodom, the fall of Jerusalem — are presented as specific acts of divine justice within history. The NT intensifies the eschatological dimension: God has appointed a day on which he will judge the world in righteousness through Jesus Christ (Acts 17:31; John 5:22, 27). Every person will give account before the judgment seat (Rom. 14:10; 2 Cor. 5:10), and the dead will be judged according to their works as recorded in the books (Rev. 20:12). The ground of escape from condemnation is the atoning work of Christ, which removes the penalty of sin for those who believe (John 3:18; 5:24; Rom. 8:1). Scripture consistently portrays God's judgment as both an act of justice against sin and a vindication of the righteous — aspects that converge at the cross and at the last day.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "judgment"},
  "key_refs": ["Acts 17:31", "Romans 14:10", "2 Corinthians 5:10", "Revelation 20:12"]
},
"grace-of-god": {
  "term": "Grace of God",
  "category": "concepts",
  "intro": "<p>The grace of God (<em>charis</em>) is his free, unmerited, sovereign favor extended to sinners who deserve only wrath. While the OT expresses God's gracious character through the covenant name Yahweh — \"gracious and merciful, slow to anger and abounding in steadfast love\" (Ex. 34:6; Ps. 103:8) — the NT declares that the grace inaugurated in Israel's history has been fully revealed and poured out through Jesus Christ: \"For the law was given through Moses; grace and truth came through Jesus Christ\" (John 1:17). Paul places grace at the center of his soteriology: salvation is \"by grace... through faith, and that not of yourselves, it is the gift of God\" (Eph. 2:8). Grace does not merely forgive past sins but also enables ongoing sanctification — Paul attributes his apostolic labor to \"the grace of God that is with me\" (1 Cor. 15:10) and teaches that grace undergirds the Christian's entire life from beginning to end (2 Tim. 2:1; Tit. 2:11–12). The throne of God is called a \"throne of grace\" to which believers may approach with confidence in time of need (Heb. 4:16).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "grace-of-god"},
  "key_refs": ["John 1:17", "Ephesians 2:8", "Romans 5:20", "Hebrews 4:16"]
},
"angel-holy-trinity": {
  "term": "Angel (Holy Trinity)",
  "category": "concepts",
  "intro": "<p>Several biblical passages describe a divine angel — the \"Angel of the LORD\" or \"Angel of God\" — who speaks and acts with full divine authority, accepting worship, and is identified with God himself rather than being merely a created messenger. This figure appears to Hagar (Gen. 16:7–13), to Abraham at Moriah (Gen. 22:11–18), to Moses in the burning bush (Ex. 3:2–6), and to Gideon (Judg. 6:11–24). In each case the angel and the LORD are used interchangeably within the same passage. Patristic interpreters commonly identified this Angel of the LORD as a pre-incarnate theophany of the Son of God, which they called a <em>Christophany</em>. This interpretation is supported by John 1:18 (\"No one has seen God at any time; the only-begotten God... has made him known\") and by the NT identification of the exodus cloud-pillar guide with Christ (1 Cor. 10:4). Whether one reads these appearances as Christophanies or as created angels speaking on behalf of God, the passages establish a category of divine self-disclosure through angelic mediation that points toward the fuller revelation of God in the incarnate Son.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "angel-holy-trinity"},
  "key_refs": ["Exodus 3:2", "Judges 6:22", "Genesis 22:11", "1 Corinthians 10:4"]
},
"church-and-state": {
  "term": "Church and State",
  "category": "concepts",
  "intro": "<p>The relationship between religious and civil authority is a recurring theme in Scripture, addressed most directly in the NT but anticipated throughout the OT. In Israel, the theocratic ideal blended religious and civil governance under God's law, though the monarchy introduced ongoing tension between prophetic and royal authority — most sharply in Elijah's confrontation with Ahab (1 Kgs. 18) and Jeremiah's conflict with Zedekiah. Jesus articulated the foundational NT principle: \"Render to Caesar the things that are Caesar's, and to God the things that are God's\" (Matt. 22:21; Mark 12:17; Luke 20:25) — affirming the legitimacy of civil government while insisting on a distinct divine claim. Paul teaches that governing authorities are \"God's servant\" for the public good and that Christians owe taxes, respect, and honor (Rom. 13:1–7; 1 Tim. 2:1–2; Tit. 3:1; 1 Pet. 2:13–17). The limit of civil obedience is reached when the state commands disobedience to God: Peter and the apostles declared \"we must obey God rather than men\" (Acts 5:29), an echo of the Hebrew midwives, Daniel, and the three young men in Babylon who refused royal decrees that violated divine commands.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "church-and-state"},
  "key_refs": ["Matthew 22:21", "Romans 13:1", "Acts 5:29", "1 Peter 2:13"]
},
"hypocrisy": {
  "term": "Hypocrisy",
  "category": "concepts",
  "intro": "<p>Hypocrisy (Greek <em>hypokrisis</em>, originally \"playing a theatrical role\") in biblical usage denotes a gap between outward religious performance and inward reality — the pretense of piety without genuine devotion to God. The OT condemns it in Israel's formal worship divorced from justice and righteousness (Isa. 1:10–17; Amos 5:21–24; Mic. 6:6–8). Jesus reserved his most severe rebukes for the religious hypocrisy he observed in some scribes and Pharisees, delivering seven \"woes\" against them in Matthew 23: they honored God with their lips while their hearts were far from him (Matt. 15:7–9; Isa. 29:13), they performed religious acts for public approval (Matt. 6:2, 5, 16), they made proselytes who were worse than themselves (Matt. 23:15), and they meticulously tithed spices while neglecting justice, mercy, and faithfulness (Matt. 23:23). Paul warns against those who have \"a form of godliness\" but deny its power (2 Tim. 3:5) and against the hypocrisy that disrupts Christian community, as when Peter withdrew from Gentile table fellowship under social pressure (Gal. 2:11–14). The remedy is genuine repentance and the sincere love that comes from a pure heart (1 Tim. 1:5; 1 Pet. 1:22).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "hypocrisy"},
  "key_refs": ["Matthew 23:13", "Isaiah 29:13", "Matthew 6:2", "Galatians 2:13"]
},
"israel-prophecies-concerning": {
  "term": "Israel, Prophecies Concerning",
  "category": "concepts",
  "intro": "<p>The prophetic literature of the OT contains extensive oracles concerning Israel's future — both judgment for covenant unfaithfulness and ultimate restoration to the promised land and to God. The exile to Babylon was foretold (Deut. 28:64–68; 1 Kgs. 14:15; Isa. 39:6–7; Jer. 25:11–12) and its 70-year duration predicted by Jeremiah (Jer. 25:12; 29:10), fulfilled in 586–516 B.C. The prophets also foresaw a future restoration surpassing the Exodus: regathering from all nations (Isa. 11:11–12; Jer. 23:3; Ezek. 37:21), national renewal through a new covenant (Jer. 31:31–34), and blessing flowing to all nations through Israel (Isa. 60; 66:18–23; Zech. 8:23). The NT interprets these prophecies as fulfilled progressively: in Christ (Matt. 2:15; Luke 24:44), in the church composed of Jew and Gentile (Eph. 2:14–16; Gal. 3:28–29), and in a future redemption of ethnic Israel (Rom. 11:25–27). The interpretation of these prophecies is one of the most debated areas of NT hermeneutics, dividing premillennial, amillennial, and postmillennial schools.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "israel-prophecies-concerning"},
  "key_refs": ["Jeremiah 31:31", "Romans 11:26", "Isaiah 11:11", "Ezekiel 37:21"]
},
"kingdom-of-heaven": {
  "term": "Kingdom of Heaven",
  "category": "concepts",
  "intro": "<p>The Kingdom of Heaven (Matthew's preferred term; other Gospels say \"Kingdom of God\") was the central subject of Jesus' teaching — the sovereign reign of God that he announced had arrived in his own person and ministry (Mark 1:15; Luke 11:20) while awaiting its consummation at his return. Jesus described the kingdom through a rich series of parables: it begins small and grows irresistibly (the mustard seed and leaven, Matt. 13:31–33), it contains a mixture of genuine and false members until the final harvest (the wheat and tares, Matt. 13:24–30), it is of surpassing value worth any sacrifice to obtain (the treasure and pearl, Matt. 13:44–46), and its coming is unexpected like a thief (Matt. 24:44; 25:1–13). Entry requires new birth (John 3:3–5), repentance and faith (Mark 1:15), and becoming like a child (Matt. 18:3). The kingdom is already present in the Spirit's power (1 Cor. 4:20; Rom. 14:17) but not yet fully revealed — it will be consummated when Christ returns, delivers the kingdom to the Father, and God becomes \"all in all\" (1 Cor. 15:24–28; Rev. 11:15).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "kingdom-of-heaven"},
  "key_refs": ["Matthew 13:24", "Mark 1:15", "Luke 11:20", "1 Corinthians 15:24"]
},
"pride": {
  "term": "Pride",
  "category": "concepts",
  "intro": "<p>Pride (Hebrew <em>ga'avan</em>, <em>geva</em>; Greek <em>hyperephania</em>, <em>alazoneia</em>) denotes the vice of arrogant self-exaltation that sets itself above God and others, and is consistently identified in Scripture as the foundational human sin. It entered the world through the temptation to be \"like God\" (Gen. 3:5), and is associated with the fall of the adversary himself (Isa. 14:13–14; Ezek. 28:17). Proverbs states the principle plainly: \"Pride goes before destruction, and a haughty spirit before a fall\" (Prov. 16:18), and \"God opposes the proud but gives grace to the humble\" (Prov. 3:34; Jas. 4:6; 1 Pet. 5:5). The OT records the downfall of proud kings — Pharaoh, Nebuchadnezzar (Dan. 4:30–37), Herod Agrippa (Acts 12:21–23) — as paradigms of divine judgment on human arrogance. Jesus declared \"every one who exalts himself will be humbled, and everyone who humbles himself will be exalted\" (Matt. 23:12; Luke 14:11; 18:14). Paul lists pride among the vices of the unregenerate (Rom. 1:30; 2 Tim. 3:2) and roots it in a disordered self-assessment that ignores the grace from which all gifts come (1 Cor. 4:7).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "pride"},
  "key_refs": ["Proverbs 16:18", "James 4:6", "Matthew 23:12", "Daniel 4:37"]
},
"thankfulness": {
  "term": "Thankfulness",
  "category": "concepts",
  "intro": "<p>Thankfulness (Hebrew <em>todah</em>; Greek <em>eucharistia</em>) is both a commanded duty and a natural response of the redeemed to God's goodness throughout Scripture. The Psalms are saturated with calls to thanksgiving (Ps. 100:4; 107:1; 136:1–26), and the practice of offering a \"sacrifice of thanksgiving\" (<em>todah</em>) was a central element of Israel's worship (Lev. 7:12; Ps. 50:14, 23). Jesus himself gave thanks at meals (Matt. 26:27; John 6:11; 11:41), modeling a posture of dependence and gratitude. Paul establishes thankfulness as the marker of a healthy spiritual life: \"In everything give thanks, for this is the will of God in Christ Jesus for you\" (1 Thess. 5:18), and the absence of thanksgiving is among the first symptoms of human rebellion against God (Rom. 1:21). The Eucharist (from <em>eucharistia</em>) is itself the great act of Christian thanksgiving. Colossians exhorts Christians to let thankfulness permeate every dimension of life — speech, song, and work — all done \"in the name of the Lord Jesus, giving thanks to God the Father through him\" (Col. 3:17).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "thankfulness"},
  "key_refs": ["Psalms 100:4", "1 Thessalonians 5:18", "Colossians 3:17", "Romans 1:21"]
},
"zeal-religious": {
  "term": "Zeal, Religious",
  "category": "concepts",
  "intro": "<p>Religious zeal (Hebrew <em>qin'ah</em>; Greek <em>zelos</em>) denotes fervent devotion to God and his cause — an intensity of commitment that Scripture presents as both a virtue when rightly directed and a danger when divorced from knowledge or rooted in selfish motivation. God himself is described as a \"jealous [zealous] God\" (Ex. 20:5; 34:14; Deut. 5:9), whose zeal for his own name drives both judgment and redemption (Isa. 9:7; 37:32; Ezek. 36:5). The godly expression of zeal is illustrated by Phinehas (Num. 25:11–13), Elijah's cry \"I have been very jealous for the LORD\" (1 Kgs. 19:10, 14), and Jesus' consuming zeal for the temple (John 2:17; Ps. 69:9). Paul describes his pre-conversion zeal for Judaism as genuine but misdirected — a \"zeal for God, but not according to knowledge\" (Rom. 10:2; Phil. 3:6) — and celebrates the transforming work of the Spirit that produces a zeal now governed by truth and love (Gal. 4:18; Tit. 2:14). Peter urges believers to \"be zealous for good works\" (Tit. 2:14) and to \"be zealous to be found without spot or blemish\" at Christ's return (2 Pet. 3:14).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "zeal-religious"},
  "key_refs": ["Numbers 25:11", "John 2:17", "Romans 10:2", "Titus 2:14"]
},
"eternal-punishment": {
  "term": "Eternal Punishment",
  "category": "concepts",
  "intro": "<p>The doctrine of eternal punishment holds that the consequences of final divine judgment for the impenitent are unending — a teaching grounded primarily in the explicit teachings of Jesus and the book of Revelation. Jesus warns of \"eternal fire\" (Matt. 18:8; 25:41), \"eternal punishment\" (Matt. 25:46), and Gehenna \"where their worm does not die and the fire is not quenched\" (Mark 9:43–48, citing Isa. 66:24). The contrasting parallel structure of Matthew 25:46 — \"these will go away into eternal punishment, but the righteous into eternal life\" — uses the same Greek adjective (<em>aionios</em>) for both destinies, making the duration of punishment equal to that of life. Revelation describes the final state of those whose names are not in the book of life as the \"lake of fire,\" called \"the second death\" (Rev. 20:14–15). Paul refers to \"everlasting destruction\" and being shut out from the presence of God (2 Thess. 1:9). Three main interpretations have been defended in church history: eternal conscious torment (the majority historic position), annihilationism (the wicked are destroyed after judgment), and universalism (all are eventually restored). The first remains the most widely attested in the NT text.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "eternal-punishment"},
  "key_refs": ["Matthew 25:46", "Mark 9:44", "Revelation 20:15", "2 Thessalonians 1:9"]
},
"fight-of-faith": {
  "term": "Fight of Faith",
  "category": "concepts",
  "intro": "<p>The metaphor of the Christian life as a fight or struggle of faith is prominent in the NT, portraying the believer as an athlete or soldier contending against spiritual opposition. Paul charges Timothy: \"Fight the good fight of the faith; take hold of the eternal life to which you were called\" (1 Tim. 6:12), and at life's end declares: \"I have fought the good fight, I have finished the race, I have kept the faith\" (2 Tim. 4:7). The Epistle to the Hebrews describes OT saints who \"through faith conquered kingdoms, enforced justice... became mighty in war\" (Heb. 11:33–34) and calls believers to run with endurance the race set before them, fixing their eyes on Jesus (Heb. 12:1–2). Paul's extended metaphor of the full armor of God (Eph. 6:10–18) defines the fight as fundamentally spiritual — \"not against flesh and blood\" but against spiritual powers — and prescribes truth, righteousness, faith, salvation, the word of God, and prayer as the believer's weapons. Jude exhorts his readers to \"contend earnestly for the faith that was once for all delivered to the saints\" (Jude 3), extending the fight metaphor to the doctrinal realm.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "fight-of-faith"},
  "key_refs": ["1 Timothy 6:12", "2 Timothy 4:7", "Ephesians 6:12", "Jude 3"]
},
"kingdom-of-satan": {
  "term": "Kingdom of Satan",
  "category": "concepts",
  "intro": "<p>Satan's kingdom (also called his \"domain,\" \"power of darkness,\" or \"world\") denotes the organized dominion of evil that Christ came to destroy. Jesus acknowledged Satan as a real power with a structured kingdom: \"If Satan casts out Satan, he is divided against himself. How then will his kingdom stand?\" (Matt. 12:26). He called Satan \"the ruler of this world\" (John 12:31; 14:30; 16:11), and Paul calls him \"the god of this age\" (2 Cor. 4:4) and \"the prince of the power of the air\" (Eph. 2:2). The scope of his dominion — the whole world \"lies in the power of the evil one\" (1 John 5:19) — is precisely what makes Christ's conquest decisive: the Son of God was manifested \"to destroy the works of the devil\" (1 John 3:8), and by his death and resurrection Christ disarmed and triumphed over spiritual powers (Col. 2:15). Satan's kingdom is thus a defeated kingdom awaiting final destruction: at the last day he will be cast into the lake of fire (Rev. 20:10), and the kingdoms of this world will become the kingdom of God and of his Christ (Rev. 11:15).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "kingdom-of-satan"},
  "key_refs": ["Matthew 12:26", "John 12:31", "1 John 5:19", "Revelation 20:10"]
},
"plan-of-salvation": {
  "term": "Plan of Salvation",
  "category": "concepts",
  "intro": "<p>The plan of salvation (also called the divine economy, counsel, or purpose of redemption) refers to God's sovereign, eternal design to redeem fallen humanity through Jesus Christ — a plan conceived before creation (Eph. 1:4–5; 2 Tim. 1:9; 1 Pet. 1:20; Rev. 13:8) and progressively disclosed through redemptive history. Paul describes it as a \"mystery\" hidden for ages and now revealed: \"to bring all things in heaven and on earth together under one head, even Christ\" (Eph. 1:10). The plan encompasses election (Eph. 1:4), the giving of the law as a guardian until Christ (Gal. 3:23–25), the incarnation (John 1:14), the atonement (Rom. 3:25–26; 1 Pet. 1:18–20), justification by faith (Rom. 3:21–26; 5:1), regeneration (John 3:3–8; Tit. 3:5), sanctification (1 Thess. 4:3; 2 Thess. 2:13), and final glorification (Rom. 8:30). The OT foreshadowed it through types and prophecies (1 Cor. 10:6; Heb. 8–10), and the NT declares its fulfillment in Christ. The unity of OT and NT rests on the conviction that one God has been executing one coherent plan of salvation across both covenants.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "plan-of-salvation"},
  "key_refs": ["Ephesians 1:4", "Romans 8:30", "1 Peter 1:20", "Titus 3:5"]
},
"reconciliation": {
  "term": "Reconciliation",
  "category": "concepts",
  "intro": "<p>Reconciliation (Greek <em>katallage</em>, <em>katallass&#333;</em>) is the NT's term for the restoration of the broken relationship between God and humanity through Christ's atoning work. The word carries the idea of a change from enmity to peace: \"God was in Christ reconciling the world to himself, not counting their trespasses against them\" (2 Cor. 5:19). Paul develops the concept most fully in Romans 5:10–11 and 2 Corinthians 5:18–21: the initiative lies entirely with God (he reconciles; we are reconciled), the means is the death of his Son, and the result is peace and access to God (Rom. 5:1–2). The ministry of reconciliation is then entrusted to the apostles and the church: \"We are ambassadors for Christ, God making his appeal through us: 'Be reconciled to God'\" (2 Cor. 5:20). Colossians extends the scope of reconciliation cosmically: through Christ God reconciles \"all things, whether things on earth or things in heaven, by making peace through his blood, shed on the cross\" (Col. 1:20). The horizontal dimension — reconciliation between alienated people — is grounded in and flows from this vertical reconciliation with God (Matt. 5:23–24; Eph. 2:14–16).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "reconciliation"},
  "key_refs": ["Romans 5:10", "2 Corinthians 5:18", "Colossians 1:20", "Ephesians 2:16"]
},
"wrath": {
  "term": "Wrath",
  "category": "concepts",
  "intro": "<p>The wrath of God (<em>orge theou</em>) is his settled, holy opposition to all that contradicts his righteous character — not an emotional outburst but the inevitable, consistent reaction of moral perfection against moral evil. Scripture consistently affirms divine wrath as a reality integral to God's justice: \"God is a righteous judge, and a God who feels indignation every day\" (Ps. 7:11). The OT narrates specific acts of divine wrath — against Egypt (Ex. 15:7), against Israel in the wilderness (Num. 11:1; Ps. 78:31), and against the nations (Isa. 13:9; Nah. 1:2). Paul's systematic exposition begins: \"The wrath of God is being revealed from heaven against all the godlessness and wickedness of people\" (Rom. 1:18), and traces it as the judicial consequence of humanity's suppression of truth. The NT also speaks of \"wrath to come\" (Matt. 3:7; 1 Thess. 1:10) — the final outpouring of divine judgment at the last day (Rev. 6:17; 11:18; 19:15). Christ's atoning death is precisely the place where God's wrath against sin is fully satisfied (Rom. 3:25; 1 Thess. 5:9; 1 John 2:2), rescuing believers from the wrath to come and bringing them into peace with God (Rom. 5:1, 9–10).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "wrath"},
  "key_refs": ["Romans 1:18", "Romans 3:25", "1 Thessalonians 1:10", "Revelation 19:15"]
},
"afflictions-and-adversities": {
  "term": "Afflictions and Adversities",
  "category": "concepts",
  "intro": "<p>Affliction and adversity are universal experiences addressed throughout Scripture with remarkable pastoral depth and theological richness. The OT records the suffering of the righteous — Job, the persecuted psalmists, Jeremiah — and affirms that God's people are not immune from hardship, while insisting that God uses affliction for discipline, testing, and purification (Ps. 119:71; Heb. 12:5–11; Deut. 8:2–3). The great Psalms of lament (Pss. 22, 44, 88) model honest, persistent prayer in the midst of unexplained suffering without abandoning faith in God. The NT introduces a distinctive theology of suffering shaped by the cross: believers share in Christ's sufferings (Phil. 3:10; Col. 1:24), the Holy Spirit helps in weakness (Rom. 8:26), and present afflictions work \"an eternal weight of glory\" disproportionate in magnitude to the suffering itself (2 Cor. 4:17). James opens his epistle by calling trials a cause for joy because they produce tested character and endurance (Jas. 1:2–4). Paul learned contentment in all circumstances through the strength Christ provides (Phil. 4:11–13), and the promise stands that God works all things together for the good of those who love him (Rom. 8:28).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "afflictions-and-adversities"},
  "key_refs": ["Romans 8:28", "2 Corinthians 4:17", "James 1:2", "Psalms 119:71"]
},
"jesus-the-christ": {
  "term": "Jesus, the Christ",
  "category": "people",
  "intro": "<p>Jesus of Nazareth, identified throughout the NT as the Christ (Greek <em>Christos</em>, \"Anointed One\"; Hebrew <em>Mashiach</em>, Messiah), is the central figure of the Christian faith — the eternal Son of God incarnate as a human being for the salvation of the world. Born of the virgin Mary in Bethlehem (Matt. 1:18–25; Luke 2:1–20) in fulfillment of OT prophecy (Isa. 7:14; Mic. 5:2), he grew up in Nazareth, was baptized by John, and conducted a three-year public ministry of teaching, healing, and calling disciples. His teaching — supremely in the Sermon on the Mount (Matt. 5–7) and through parables — proclaimed the arrival of the kingdom of God. He was crucified under Pontius Pilate, buried, and rose bodily from the dead on the third day (1 Cor. 15:3–8), appearing to his disciples over forty days before his ascension. The NT identifies him as the fulfillment of the law and the prophets (Matt. 5:17; Luke 24:44), the atoning sacrifice for sin (Rom. 3:25; Heb. 9:26; 1 John 2:2), the great high priest (Heb. 4:14–16), and the coming king who will return to judge the living and the dead (Acts 10:42; Rev. 19:11–16). Faith in him is the sole ground of justification (John 14:6; Acts 4:12; Rom. 10:9).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "jesus-the-christ"},
  "key_refs": ["Matthew 1:1", "John 1:14", "Romans 3:25", "1 Corinthians 15:3"]
},
"minister-christian": {
  "term": "Minister, Christian",
  "category": "concepts",
  "intro": "<p>The Christian minister (Greek <em>diakonos</em>, \"servant\"; <em>leitourgos</em>, \"one who performs public service\") serves as an authorized representative and servant of Christ and his church. Jesus defined the paradigm: \"Whoever would be great among you must be your servant, and whoever would be first among you must be slave of all\" (Mark 10:43–44; Matt. 20:26–28), rooting ministry in self-giving service rather than hierarchical authority. The NT distinguishes various ministry roles — apostles, prophets, evangelists, pastors, teachers (Eph. 4:11) — all given to equip the saints for the work of ministry and the building up of the body (Eph. 4:12). Paul describes his own apostolic ministry as the proclamation of Christ crucified (1 Cor. 1:23; 2:2), a \"ministry of reconciliation\" (2 Cor. 5:18), and a stewardship of the gospel (1 Cor. 9:17; Col. 1:25). Qualifications for overseers and deacons are detailed in 1 Timothy 3 and Titus 1, emphasizing character, household management, and doctrinal soundness. The Reformation recovered the priesthood of all believers (1 Pet. 2:5, 9), while affirming the distinctive calling of ordained ministry for word, sacrament, and oversight.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "minister-christian"},
  "key_refs": ["Mark 10:43", "Ephesians 4:11", "2 Corinthians 5:18", "1 Timothy 3:1"]
},
"quotations-and-allusions": {
  "term": "Quotations and Allusions",
  "category": "concepts",
  "intro": "<p>The New Testament's use of the Old Testament through direct quotation and allusion is pervasive — scholars count over 350 direct OT quotations in the NT and several thousand allusions or echoes. These citations demonstrate the NT writers' conviction that the OT scriptures find their fulfillment in the person and work of Jesus Christ (Matt. 5:17; Luke 24:44–47). Matthew's Gospel is structured around five clusters of fulfillment citations (Matt. 1:23; 2:6, 15, 18, 23; etc.) introduced by the formula \"this was to fulfill what was spoken by the prophet.\" Paul's letters cite the OT extensively as doctrinal proof (Rom. 1–4; Gal. 3–4), primarily from the Septuagint (LXX). The Epistle to the Hebrews is built almost entirely on sustained OT exegesis. John employs pervasive allusion rather than direct citation, weaving OT imagery into the narrative structure of the Gospel. The NT quotation methods — including typology, pesher-style fulfillment, and analogical application — reflect the hermeneutical practices of Second Temple Judaism while recentering all scriptural interpretation on Christ.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "quotations-and-allusions"},
  "key_refs": ["Matthew 1:23", "Luke 24:44", "Romans 15:4", "2 Timothy 3:16"]
},
"righteous": {
  "term": "Righteous",
  "category": "concepts",
  "intro": "<p>Righteousness (Hebrew <em>tsaddiq</em>; Greek <em>dikaios</em>) in Scripture denotes conformity to the divine moral standard — both an attribute of God and a status declared of those who stand rightly before him. God is described throughout the OT as the righteous judge (Ps. 7:9; 9:8; 96:13) whose every act is consistent with his perfect character. Human righteousness in the OT is expressed through obedience to the covenant stipulations (Deut. 6:25) and through ethical conduct toward others (Ezek. 18:5–9). The NT introduces the doctrine of imputed righteousness: God justifies the ungodly not by requiring their own righteousness but by crediting to them the righteousness of Christ (Rom. 3:21–26; 4:5–8; 2 Cor. 5:21; Phil. 3:9). Those declared righteous through faith are then called to live righteous lives in the power of the Spirit (Rom. 6:18; Tit. 2:12). The eschatological future is described as \"a new heaven and a new earth in which righteousness dwells\" (2 Pet. 3:13), and the righteous will \"shine like the sun in the kingdom of their Father\" (Matt. 13:43; Dan. 12:3).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "righteous"},
  "key_refs": ["Romans 3:22", "2 Corinthians 5:21", "Philippians 3:9", "Matthew 13:43"]
},
"wicked-people": {
  "term": "Wicked (People)",
  "category": "concepts",
  "intro": "<p>The wicked (<em>rasha</em> in Hebrew; <em>poneros</em>, <em>adikos</em> in Greek) are those who live in deliberate opposition to God and his moral order — a category treated at length in the wisdom literature, the psalms, and the prophets. Psalm 1 contrasts the righteous and the wicked with stark economy: the wicked are like chaff driven away by the wind, while the righteous are like a tree planted by streams of water. The book of Proverbs repeatedly traces the trajectory of the wicked toward destruction (Prov. 11:21; 13:21; 24:20), while the prophets lament the apparent prosperity of the wicked as a test of faith (Jer. 12:1; Hab. 1:13; Ps. 73:3–17). The NT adds the eschatological verdict: at the final judgment the wicked will be separated from the righteous (Matt. 25:31–46), thrown into the \"fiery furnace\" (Matt. 13:42, 50), and will not inherit the kingdom of God (1 Cor. 6:9–10; Gal. 5:19–21). The distinction between the righteous and the wicked is not ultimately a moral achievement but a matter of standing before God — those in Christ having been declared righteous by grace, the wicked remaining under condemnation by choice and unbelief (John 3:18–19).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "wicked-people"},
  "key_refs": ["Psalms 1:4", "Matthew 25:46", "1 Corinthians 6:9", "Proverbs 11:21"]
},
"armies": {
  "term": "Armies",
  "category": "concepts",
  "intro": "<p>Armies in the biblical world were the organized military forces of nations, tribes, and kingdoms, regulated in Israel by specific divine instructions. The LORD of Hosts (<em>Yahweh Sabaoth</em>) is the supreme commander of the heavenly armies and the God who determines the outcome of earthly warfare (1 Sam. 17:45; Ps. 46:7). Israel's military organization in the wilderness was based on a census of fighting men (Num. 1:2–3; 26:2) with each tribe forming its own regiment. The law regulated warfare: cities were to be offered terms of peace before siege (Deut. 20:10–12), fruit trees were not to be cut down (Deut. 20:19–20), and certain men were exempt from service (Deut. 20:5–8). Israel was repeatedly warned that military success depended on trust in God rather than superior numbers (Judg. 7:2–8; Ps. 33:16–17; Isa. 31:1). The NT employs military metaphor extensively — the armor of God (Eph. 6:10–18), soldiers of Christ (2 Tim. 2:3–4), and the heavenly armies at the return of Christ (Rev. 19:14) — while shifting the primary battle to the spiritual realm.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "armies"},
  "key_refs": ["Numbers 1:3", "1 Samuel 17:45", "Ephesians 6:11", "Revelation 19:14"]
},
"backsliders": {
  "term": "Backsliders",
  "category": "concepts",
  "intro": "<p>Backsliding (Hebrew <em>meshuvah</em>, \"turning back\"; Greek <em>apostasia</em>) refers to the pattern of spiritual decline, unfaithfulness, and departure from God that recurs throughout Israel's history and is addressed repeatedly in the wisdom and prophetic literature. The verb <em>shuv</em> (turn/return) underlies both the diagnosis (\"they have turned away\") and the cure (\"return to the LORD\"). The prophets frequently deploy the image of Israel as an unfaithful spouse or wayward child who has abandoned her first love (Jer. 2:13–19; 3:22; Hos. 11:1–7; 14:4). Proverbs 14:14 states: \"The backslider in heart will be filled with the fruit of his ways.\" The NT addresses the danger of spiritual regression: Hebrews warns against \"drifting away\" (Heb. 2:1), \"falling away\" (Heb. 6:6), and \"shrinking back to destruction\" (Heb. 10:39), and calls believers to hold fast their confession (Heb. 4:14; 10:23). Jesus' letters to the seven churches rebuke those who have \"abandoned the love you had at first\" (Rev. 2:4). Restoration for the backslider is a consistent divine promise: \"Return, faithless Israel... I will not look on you in anger, for I am merciful\" (Jer. 3:12).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "backsliders"},
  "key_refs": ["Jeremiah 3:12", "Hosea 14:4", "Hebrews 10:38", "Revelation 2:4"]
},
"commandments": {
  "term": "Commandments",
  "category": "concepts",
  "intro": "<p>The commandments (Hebrew <em>mitzvot</em>; Greek <em>entolai</em>) are the divine instructions given to govern the covenant relationship between God and his people. The Decalogue (\"Ten Commandments\") given at Sinai (Ex. 20:1–17; Deut. 5:6–21) forms the core of the Mosaic covenant stipulations — covering duties toward God (no other gods, no idols, no misuse of the divine name, the Sabbath) and toward other people (honor of parents, and prohibitions of murder, adultery, theft, false witness, and covetousness). The full Mosaic law expanded these into 613 commandments in Jewish tradition, governing worship, diet, civil life, and social ethics. Jesus affirmed the abiding authority of the commandments (Matt. 5:17–19) while deepening them to address heart motivations rather than external compliance alone (Matt. 5:21–48), and distilled them into two: love God with all the heart, and love the neighbor as oneself (Matt. 22:37–40; Deut. 6:5; Lev. 19:18). Paul argues that love fulfills the entire law (Rom. 13:8–10; Gal. 5:14). In the NT, obedience to Christ's commands is the mark of genuine love for him (John 14:15, 21; 1 John 5:3) and the evidence of abiding in him (1 John 2:3–5).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"nave": "commandments"},
  "key_refs": ["Exodus 20:1", "Matthew 22:37", "Romans 13:10", "John 14:15"]
},
}

wrote = skipped = 0
for slug, data in ARTICLES.items():
    article = {
        "id": slug,
        "term": data["term"],
        "category": data["category"],
        "intro": data["intro"],
        "hitchcock_meaning": data.get("hitchcock_meaning"),
        "source_ids": data.get("source_ids", {}),
        "key_refs": data.get("key_refs", []),
        "sections": []
    }
    if merge_article(slug, article):
        wrote += 1
    else:
        skipped += 1

print(f"BP gap-doctrine: Angel (A Spirit) -> Commandments: wrote {wrote}, skipped {skipped} existing.")
