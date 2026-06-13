"""
BP Article Synthesis — gap-ethics: Malice → Popular Sins
Covers Phase 2 gap articles: character, virtue, vice, and conduct topics (49 entries)

Sources consulted:
  - data/topical/nave.json (Nave topic verses)
  - data/biblepedia/gaps.json (gap analysis, priority_score)

Category logic applied:
  - concepts: all items here are ethical/moral concepts from Nave

Script: scripts/bp-gap-ethics.py
Run: python3 scripts/bp-gap-ethics.py
"""

import json, os

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)


def load_article(slug):
    path = os.path.join(OUT_DIR, slug + '.json')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return None


def save_article(slug, data):
    path = os.path.join(OUT_DIR, slug + '.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def merge_article(slug, data):
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True


ARTICLES = {
    "malice": {
        "id": "malice",
        "term": "Malice",
        "category": "concepts",
        "intro": "<p>Malice (Hebrew <em>ra</em>; Greek <em>kakia</em>) is the deliberate intention to harm another — the settled disposition of ill-will that seeks to injure, destroy, or corrupt. Scripture treats malice as one of the root sins of a fallen nature: Leviticus forbids the nursing of hatred against a neighbor (Lev. 19:17–18), and the prophets connect malice with violence and oppression (Mic. 2:1; Isa. 32:7). In the NT, Paul lists malice as part of the catalog of pre-conversion vices from which believers are called to be cleansed (Eph. 4:31; Col. 3:8; Tit. 3:3), pairing it with bitterness, anger, and slander. The apostle Peter similarly calls Christians to lay aside \"all malice\" (1 Pet. 2:1). The antidote is not mere restraint but a renewed heart: the command to love enemies (Matt. 5:44) and to overcome evil with good (Rom. 12:21) strikes at malice's root by replacing ill-will with active benevolence. The final judgment will expose and condemn the malicious intentions hidden from human sight (1 Cor. 4:5).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "malice"},
        "key_refs": ["Genesis 3:15", "Leviticus 19:17", "Ephesians 4:31", "Colossians 3:8", "1 Peter 2:1"]
    },
    "self-denial": {
        "id": "self-denial",
        "term": "Self-Denial",
        "category": "concepts",
        "intro": "<p>Self-denial in biblical ethics is the voluntary surrender of personal rights, comforts, or desires for the sake of God's will or another's good — the practical expression of the call to discipleship. Jesus defines it precisely: \"If anyone would come after me, let him deny himself and take up his cross and follow me\" (Matt. 16:24; Mark 8:34; Luke 9:23). The daily cross-bearing Jesus envisions is not ascetic self-punishment but the continual subordination of the self-life to God's kingdom purposes. Abraham's willingness to offer Isaac (Gen. 22:1–12), Moses's identification with the people of God over the treasures of Egypt (Heb. 11:26), and Paul's readiness to be accursed for his kinsmen (Rom. 9:3) illustrate its scope. Paul frames self-denial as mutual: \"Let each of you look not only to his own interests, but also to the interests of others\" (Phil. 2:4), grounding it in the pattern of Christ who emptied himself (Phil. 2:5–8). Far from being a path of loss, Jesus declares it the paradoxical path to life: \"Whoever loses his life for my sake will find it\" (Matt. 16:25).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "self-denial"},
        "key_refs": ["Matthew 16:24", "Mark 8:34", "Philippians 2:4", "Romans 9:3", "Hebrews 11:26"]
    },
    "accusation-false": {
        "id": "accusation-false",
        "term": "Accusation, False",
        "category": "concepts",
        "intro": "<p>False accusation — the bringing of untrue charges against an innocent person — is condemned throughout Scripture as a serious moral and legal offense. The ninth commandment forbids bearing false witness against a neighbor (Ex. 20:16), and Mosaic law imposed severe penalties: if a malicious witness was exposed, he suffered the punishment he sought to bring upon the accused (<em>lex talionis</em>, Deut. 19:16–19). Leviticus prohibits talebearing and joining in a false report (Lev. 19:16; Ex. 23:1). The wisdom literature depicts false accusation as the weapon of the wicked: \"A false witness breathes out lies\" (Prov. 14:5; cf. 19:5, 9). The most devastating instance in Scripture is the trial of Jesus, condemned through suborned false testimony (Matt. 26:59–60; Mark 14:56–57), fulfilling the pattern of the righteous sufferer in the Psalms who was falsely accused (Pss. 27:12; 35:11). The NT exhorts believers to maintain honorable conduct among outsiders, silencing false charges through the quality of their lives (1 Pet. 2:12; 3:16).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "accusation-false"},
        "key_refs": ["Exodus 20:16", "Deuteronomy 19:16", "Psalm 27:12", "Matthew 26:60", "1 Peter 2:12"]
    },
    "ingratitude": {
        "id": "ingratitude",
        "term": "Ingratitude",
        "category": "concepts",
        "intro": "<p>Ingratitude — the failure to acknowledge or return thanks for benefits received — is treated in Scripture as a significant moral failure that reflects spiritual blindness. The OT records Israel's persistent ingratitude toward God despite his mighty acts: forgetting the Exodus, complaining against divine provision in the wilderness (Num. 11:4–6; Ps. 78:10–17), and abandoning him for Baal. The prophets condemn this as the essence of Israel's sin: \"Sons have I reared and brought up, but they have rebelled against me\" (Isa. 1:2). In the Gospels, the cleansing of the ten lepers and the return of only one to give thanks illustrates human ingratitude starkly (Luke 17:17–18). Paul identifies ingratitude as one of the marks of end-time moral collapse: \"ungrateful, unholy\" (2 Tim. 3:2). More fundamentally, Romans 1:21 traces the origin of human idolatry and moral decline to this root: humanity \"did not honor him as God or give thanks to him.\" Gratitude, by contrast, is integral to the Christian life: \"Give thanks in all circumstances\" (1 Thess. 5:18; cf. Phil. 4:6; Col. 3:17).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "ingratitude"},
        "key_refs": ["Romans 1:21", "Luke 17:17", "2 Timothy 3:2", "Deuteronomy 8:12", "Psalm 78:11"]
    },
    "theft-and-thieves": {
        "id": "theft-and-thieves",
        "term": "Theft and Thieves",
        "category": "concepts",
        "intro": "<p>Theft — the wrongful taking of another's property — is forbidden by the eighth commandment (Ex. 20:15; Deut. 5:19) and regulated in detail throughout Mosaic law. The Law required restitution proportional to the goods stolen: a thief who slaughtered or sold a stolen ox must restore five oxen; a sheep, four (Ex. 22:1–4). Stealing persons (kidnapping) carried the death penalty (Ex. 21:16; Deut. 24:7). The prophets condemned economic theft broadly — false weights, fraudulent measures, and oppression of laborers (Amos 8:5; Mic. 6:11; Lev. 19:35–36). The wisdom literature states plainly: \"Do not steal\" (Prov. 22:22–23) and notes that poverty does not justify it (Prov. 6:30–31). In the NT, Jesus lists theft among the vices that defile a person from within (Mark 7:21–22). Paul commands the former thief to labor honestly and share with those in need rather than steal (Eph. 4:28). Jesus himself uses the imagery of a thief's unexpected arrival to urge readiness for his return (Matt. 24:43; Rev. 3:3; 16:15).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "theft-and-thieves"},
        "key_refs": ["Exodus 20:15", "Exodus 22:1", "Ephesians 4:28", "Mark 7:22", "Proverbs 6:30"]
    },
    "vanity": {
        "id": "vanity",
        "term": "Vanity",
        "category": "concepts",
        "intro": "<p>Vanity (Hebrew <em>hebel</em>, \"breath\" or \"vapor\"; Greek <em>mataiotes</em>) designates what is insubstantial, futile, or transient — the characteristic word of Ecclesiastes, which opens and closes with the declaration \"Vanity of vanities, all is vanity\" (Eccl. 1:2; 12:8). The Preacher applies the word to toil, pleasure, wisdom gained apart from God, wealth, and human life itself (Eccl. 2:11; 3:19; 6:12): apart from God, every human achievement evaporates like morning mist. The Psalms characterize humanity's existence in similar terms (Ps. 39:5–6; 62:9; 144:4). In Paul's theology, creation itself was subjected to <em>mataiotes</em> — futility — at the fall, awaiting liberation at the redemption of creation (Rom. 8:20). The NT also condemns the vanity of worldly wisdom that refuses to acknowledge God (1 Cor. 3:20; Eph. 4:17). The opposite of vanity is not achievement but the fear of the Lord and keeping his commandments — Ecclesiastes' concluding word (Eccl. 12:13). In this framework, only what is done in dependence on God and in his service carries lasting weight.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "vanity"},
        "key_refs": ["Ecclesiastes 1:2", "Romans 8:20", "Psalm 39:5", "Ephesians 4:17", "Ecclesiastes 12:13"]
    },
    "boasting": {
        "id": "boasting",
        "term": "Boasting",
        "category": "concepts",
        "intro": "<p>Boasting (Hebrew <em>halal</em>, <em>pa'ar</em>; Greek <em>kauchaomai</em>) in Scripture carries two senses: empty self-glorification condemned as sin, and well-founded exultation in God commended as piety. The prophets forbid boasting in human wisdom, strength, or wealth: \"Let not the wise man boast in his wisdom, let not the mighty man boast in his might, let not the rich man boast in his riches, but let him who boasts boast in this, that he understands and knows me\" (Jer. 9:23–24; 1 Cor. 1:31). Proverbs warns against premature self-praise (Prov. 27:1) and promises that \"Let another praise you and not your own mouth\" (Prov. 27:2). Paul's letters address boasting at length: he forbids boasting in human wisdom or achievement before God (1 Cor. 1:29; 4:7; Gal. 6:14; Eph. 2:9) but fully endorses boasting — glorying — in the cross of Christ (Gal. 6:14), in weaknesses that display divine power (2 Cor. 11:30; 12:9), and in hope and sufferings (Rom. 5:2–3). The Psalms frame legitimate boasting as praise: \"In God we have boasted continually\" (Ps. 44:8).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "boasting"},
        "key_refs": ["Jeremiah 9:23", "Proverbs 27:1", "Galatians 6:14", "2 Corinthians 12:9", "1 Corinthians 1:31"]
    },
    "chastity": {
        "id": "chastity",
        "term": "Chastity",
        "category": "concepts",
        "intro": "<p>Chastity is the moral virtue of sexual purity — faithfulness within marriage and abstinence outside of it — which Scripture presents as integral to covenant holiness. The seventh commandment forbids adultery (Ex. 20:14), and Mosaic law addressed sexual sins with severity, reflecting the principle that the body belongs to God. Job exemplifies voluntary chastity of heart: \"I have made a covenant with my eyes; how then could I gaze at a virgin?\" (Job 31:1). The wisdom of Proverbs devotes extended attention to guarding against sexual temptation (Prov. 2:10–19; 5:3–20; 6:24–35; 7:5–27), urging the son to drink from his own cistern (Prov. 5:15–18). Paul grounds sexual chastity in the body's status as the temple of the Holy Spirit: \"Flee from sexual immorality\" (1 Cor. 6:18–19; 1 Thess. 4:3–5). Hebrews declares marriage honorable and the marriage bed undefiled (Heb. 13:4), while sexual immorality and adultery are matters for God's judgment. The NT consistently presents chastity as both a personal holiness requirement and a witness to the world (Matt. 5:27–28; Eph. 5:3–5; Col. 3:5).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "chastity"},
        "key_refs": ["Exodus 20:14", "Job 31:1", "1 Corinthians 6:18", "1 Thessalonians 4:3", "Hebrews 13:4"]
    },
    "diligence": {
        "id": "diligence",
        "term": "Diligence",
        "category": "concepts",
        "intro": "<p>Diligence — the sustained, earnest application of effort to one's work and duties — is commended throughout Scripture as a virtue integral to faithfulness. Proverbs sets the ant before the sluggard as a model of industrious foresight (Prov. 6:6–11) and repeatedly contrasts the hand of the diligent, which brings wealth and leadership, with the slack hand, which leads to poverty and servitude (Prov. 10:4; 12:24; 13:4). In the NT, Jesus's diligence in his Father's work from boyhood (Luke 2:49) provides the supreme example. Paul urges diligence in Christian service: \"Do not be slothful in zeal, be fervent in spirit, serve the Lord\" (Rom. 12:11); \"Whatever you do, work heartily, as for the Lord\" (Col. 3:23). Peter calls believers to diligent progress in virtue (2 Pet. 1:5, 10) and diligence in being found at peace when Christ returns (2 Pet. 3:14). The writer of Hebrews exhorts against spiritual sluggishness: \"We desire each one of you to show the same earnestness to have the full assurance of hope until the end\" (Heb. 6:11). Diligence in the Christian life thus encompasses labor, virtue, and eschatological readiness.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "diligence"},
        "key_refs": ["Proverbs 6:6", "Proverbs 12:24", "Romans 12:11", "Colossians 3:23", "2 Peter 1:5"]
    },
    "evil-for-good": {
        "id": "evil-for-good",
        "term": "Evil for Good",
        "category": "concepts",
        "intro": "<p>\"Returning evil for good\" — repaying benefactors with harm — is treated in Scripture as a particularly grave moral violation, one that compounds injustice with ingratitude. Proverbs declares: \"If anyone returns evil for good, evil will not depart from his house\" (Prov. 17:13), marking it as a self-destructive vice. The Psalms lament it as the experience of the righteous sufferer: David protests that his accusers are those for whom he fasted and prayed, yet they repay his love with hatred (Ps. 35:12; 109:5). Joseph's brothers preemptively feared he would repay evil for their earlier treachery — a projection that reveals their own evil-for-good mind (Gen. 50:15). In the NT's ethics of enemy love, Jesus transforms the calculus entirely: the command is not merely to resist repaying evil for good but to actively return good for evil (Matt. 5:44; Luke 6:27–28; Rom. 12:17, 21). Paul explicitly states: \"Do not repay anyone evil for evil\" — the governing principle being that evil is to be overcome with good (Rom. 12:17–21). This ethic is grounded in imitating the God who is kind even to the ungrateful and evil (Luke 6:35).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "evil-for-good"},
        "key_refs": ["Proverbs 17:13", "Psalm 35:12", "Romans 12:17", "Matthew 5:44", "Luke 6:35"]
    },
    "faithfulness": {
        "id": "faithfulness",
        "term": "Faithfulness",
        "category": "concepts",
        "intro": "<p>Faithfulness (Hebrew <em>emunah</em>; Greek <em>pistos</em>) is the quality of reliable consistency — the keeping of commitments, the honoring of trust, the constancy of character under pressure. Scripture grounds human faithfulness in God's own faithfulness: \"The LORD is faithful in all his words and kind in all his works\" (Ps. 145:13); \"His mercies never come to an end; they are new every morning; great is your faithfulness\" (Lam. 3:22–23). Human faithfulness is correspondingly rare and precious: \"Many a man proclaims his own steadfast love, but a faithful man who can find?\" (Prov. 20:6). The faithful are the righteous remnant for whom the just shall live (Hab. 2:4; Rom. 1:17). In the NT, faithfulness (pistis) is both the virtue of trusting God and the moral quality of being trustworthy. Jesus commends it in the parable of the talents: \"Well done, good and faithful servant\" (Matt. 25:21, 23). Paul names it among the fruit of the Spirit (Gal. 5:22) and commends faithful servants throughout his letters (1 Cor. 4:2; Col. 1:7; 4:7). The consummation of faithfulness is sharing the Lord's joy in the kingdom (Matt. 25:21).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "faithfulness"},
        "key_refs": ["Lamentations 3:23", "Proverbs 20:6", "Matthew 25:21", "Galatians 5:22", "Habakkuk 2:4"]
    },
    "false-confidence": {
        "id": "false-confidence",
        "term": "False Confidence",
        "category": "concepts",
        "intro": "<p>False confidence — misplaced trust in human strength, wealth, alliances, or ritual observance as a substitute for trust in God — is one of the recurring sins condemned by Israel's prophets. The Psalms contrast it with the true security found in God alone: \"Some trust in chariots and some in horses, but we trust in the name of the LORD our God\" (Ps. 20:7). Jeremiah pronounces a curse on those who trust in man and make flesh their arm while their heart turns from the LORD (Jer. 17:5–6), and a corresponding blessing on those who trust in the LORD (Jer. 17:7–8). Proverbs warns that even one's own understanding can be a source of false confidence: \"Trust in the LORD with all your heart, and do not lean on your own understanding\" (Prov. 3:5). Isaiah exposes Judah's false confidence in the Egyptian alliance (Isa. 30:1–3; 31:1–3) and Hezekiah's initial trust in tribute rather than God during Sennacherib's siege. In the NT, the Pharisee's prayer exemplifies false confidence in religious performance (Luke 18:11–12), and James warns against confidence in commercial planning that ignores divine sovereignty (Jas. 4:13–16). True confidence is confidence in God's faithfulness alone (2 Cor. 1:9).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "false-confidence"},
        "key_refs": ["Psalm 20:7", "Jeremiah 17:5", "Proverbs 3:5", "Isaiah 31:1", "2 Corinthians 1:9"]
    },
    "false-teachers": {
        "id": "false-teachers",
        "term": "False Teachers",
        "category": "concepts",
        "intro": "<p>False teachers are those within or adjacent to the community of God's people who distort divine truth for personal gain, doctrinal error, or moral license. The OT warns extensively against false prophets who declare peace when there is no peace, speaking visions of their own hearts rather than from the LORD (Jer. 23:16–17; Ezek. 13:1–16; Deut. 13:1–5; 18:20–22). The test of the true prophet was fulfillment of prediction and conformity to covenant teaching. Jesus warns of false prophets who come in sheep's clothing but inwardly are ravenous wolves, known by their fruits (Matt. 7:15–20). The apostolic letters address false teachers with particular urgency as the church expanded: Peter predicts they will secretly introduce destructive heresies, denying the Master who bought them (2 Pet. 2:1–3). Paul urges vigilance against those who teach a different gospel or who distort the truth to draw away disciples (Gal. 1:8–9; Acts 20:29–30). John's criterion is Christological: any spirit that does not confess that Jesus Christ has come in the flesh is not from God (1 John 4:2–3). Jude describes false teachers as clouds without rain, wandering stars for whom the gloom of darkness has been reserved (Jude 12–13).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "false-teachers"},
        "key_refs": ["Jeremiah 23:16", "Matthew 7:15", "2 Peter 2:1", "Galatians 1:8", "1 John 4:2"]
    },
    "frugality": {
        "id": "frugality",
        "term": "Frugality",
        "category": "concepts",
        "intro": "<p>Frugality — the prudent, non-wasteful use of resources — is commended in Scripture as a practical virtue consistent with stewardship and contentment, though it is never elevated to an absolute principle that excludes generosity or hospitality. The wisdom literature values careful management of resources: the ant stores its food in summer (Prov. 6:6–8), and the good manager preserves what has been entrusted to him. Elijah's acceptance of the widow of Zarephath's minimal provision and the miraculous multiplication of her oil and meal (1 Kgs. 17:10–16) illustrate divine provision channeled through frugal use of little. In the NT, Jesus's instruction after the feeding of the five thousand — \"Gather up the leftover fragments, that nothing may be lost\" (John 6:12) — reflects this principle at the largest scale. Paul's teaching on contentment provides frugality's spiritual grounding: \"Godliness with contentment is great gain; for we brought nothing into the world, and we cannot take anything out of the world. But if we have food and clothing, with these we will be content\" (1 Tim. 6:6–8). Frugality thus serves as the counterpart to generosity: the person who uses resources wisely is better positioned to give freely (2 Cor. 9:6–8; Prov. 11:24–25).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "frugality"},
        "key_refs": ["Proverbs 6:6", "John 6:12", "1 Timothy 6:6", "Proverbs 11:24", "1 Kings 17:12"]
    },
    "honesty": {
        "id": "honesty",
        "term": "Honesty",
        "category": "concepts",
        "intro": "<p>Honesty — truthfulness in speech and integrity in action — is grounded in the character of God, who cannot lie (Tit. 1:2; Heb. 6:18; Num. 23:19), and is commanded throughout both Testaments. Mosaic law required just weights and honest measures: \"You shall not have in your bag two kinds of weights, a large and a small\" (Deut. 25:13–16; Lev. 19:35–36), for dishonest commercial practice is an abomination to the LORD (Prov. 11:1; 20:10). The ninth commandment, forbidding false witness (Ex. 20:16), extends to all truthfulness in speech. Proverbs develops the contrast between the dishonest merchant who thinks his gain profitable and the LORD who will not overlook it (Prov. 20:17; 21:6). In the Gospels, Jesus commands simple, reliable speech: \"Let your 'yes' be 'yes' and your 'no' be 'no'\" (Matt. 5:37; cf. Jas. 5:12), ruling out all evasive or deceptive language. Paul calls believers to put away falsehood and speak truth with their neighbors, giving a creation-redemption basis: \"we are members of one another\" (Eph. 4:25). The NT vision of the heavenly city excludes everyone who practices falsehood (Rev. 21:27; 22:15).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "honesty"},
        "key_refs": ["Leviticus 19:35", "Deuteronomy 25:13", "Matthew 5:37", "Ephesians 4:25", "Proverbs 11:1"]
    },
    "idleness": {
        "id": "idleness",
        "term": "Idleness",
        "category": "concepts",
        "intro": "<p>Idleness — the refusal or neglect of productive labor — is uniformly condemned in Scripture as a moral failure and a practical path to poverty. Proverbs devotes its sharpest practical wisdom to exposing the sluggard: sent to the ant as a model, he sleeps through the harvest, folds his hands, and wants without working (Prov. 6:6–11; 10:4–5; 12:24; 19:15; 24:30–34). \"Slothfulness casts into a deep sleep, and an idle person will suffer hunger\" (Prov. 19:15); \"One who is slack in his work is a brother to him who destroys\" (Prov. 18:9). In the NT, Paul's ministry model was deliberate: he worked night and day so as not to burden his converts (1 Thess. 2:9; 2 Thess. 3:7–10), establishing the principle: \"If anyone is not willing to work, let him not eat\" (2 Thess. 3:10). He commands the idle to work quietly and earn their own living (2 Thess. 3:12; 1 Tim. 5:13). The creation ordinance that man should \"work and keep\" the garden (Gen. 2:15) frames labor not as punishment but as God's original design, making idleness a departure from the human vocation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "idleness"},
        "key_refs": ["Proverbs 6:6", "Proverbs 10:4", "2 Thessalonians 3:10", "Proverbs 18:9", "1 Timothy 5:13"]
    },
    "injustice": {
        "id": "injustice",
        "term": "Injustice",
        "category": "concepts",
        "intro": "<p>Injustice — the violation of what is due to persons before God and in human society — is among the most consistently condemned sins in Scripture, provoking the sharpest prophetic indictment. God's own character is the foundation: \"For the LORD your God is God of gods and Lord of lords, the great, the mighty, and the awesome God, who is not partial and takes no bribe\" (Deut. 10:17). The Law prohibited perverting justice for the poor or powerful alike (Ex. 23:1–3, 6–7; Lev. 19:15), and mandated protection of the alien, widow, and orphan, who were structurally vulnerable to exploitation. Amos's indictment of Israel centers on economic injustice: selling the righteous for silver and trampling the poor (Amos 2:6–7; 5:10–15; 8:4–6). Isaiah denounces those who \"decree iniquitous decrees\" that rob the poor of their rights (Isa. 10:1–2). Micah's summary of the prophetic demand is justice first: \"Do justice, and to love kindness, and to walk humbly with your God\" (Mic. 6:8). In the NT, James indicts wealthy landowners who defraud workers of wages (Jas. 5:1–6), echoing the prophetic tradition. God's eschatological judgment will finally vindicate the oppressed (Luke 18:7–8; Rev. 18:20).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "injustice"},
        "key_refs": ["Deuteronomy 10:17", "Amos 5:12", "Micah 6:8", "Isaiah 10:1", "James 5:4"]
    },
    "revenge": {
        "id": "revenge",
        "term": "Revenge",
        "category": "concepts",
        "intro": "<p>Revenge — the personal retaliation for injury received — is distinguished in Scripture from legitimate justice administered by lawful authorities, and is prohibited as a private act. The Mosaic law curbed vengeance by channeling it into the covenantal system: \"You shall not take vengeance or bear a grudge against the sons of your own people, but you shall love your neighbor as yourself\" (Lev. 19:18). The institution of cities of refuge (Num. 35:9–28) protected the accidental killer from the avenger of blood, preserving proportionality. Proverbs counsels restraint: \"Do not say, 'I will repay evil'; wait for the LORD, and he will deliver you\" (Prov. 20:22). Paul systematically forbids private revenge and grounds the prohibition in God's prerogative: \"Beloved, never avenge yourselves, but leave it to the wrath of God, for it is written, 'Vengeance is mine, I will repay, says the Lord'\" (Rom. 12:19; Deut. 32:35). The positive command paired with this prohibition is the enemy-love ethic of Jesus (Matt. 5:38–48): returning good for evil, blessing for cursing. Peter grounds the renunciation of revenge in Christ's own example — he did not threaten when he suffered, entrusting himself to the righteous Judge (1 Pet. 2:23).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "revenge"},
        "key_refs": ["Leviticus 19:18", "Romans 12:19", "Proverbs 20:22", "Matthew 5:39", "1 Peter 2:23"]
    },
    "sincerity": {
        "id": "sincerity",
        "term": "Sincerity",
        "category": "concepts",
        "intro": "<p>Sincerity (Greek <em>eilikrineia</em>, from <em>eile</em>, sunlight, + <em>krinein</em>, to judge — what is pure when examined in sunlight) denotes the quality of being genuine, undivided in motive, and free from hidden intentions. In Greek usage the term described pottery or honey tested and certified as pure. Scripture commends it as the disposition God requires: the entire inner life must correspond to the outward expression. Jesus exposes the gap between appearance and reality in the Pharisees' piety (Matt. 6:1–6, 16–18; 23:25–28) and demands heart-purity beneath outward observance. Paul opens 1 Corinthians by urging the church to celebrate the feast of the Christian life \"with the unleavened bread of sincerity and truth\" rather than old leaven of malice and evil (1 Cor. 5:8). He desires love from those who serve not to please men but God who tests the heart (1 Thess. 2:4–5; Eph. 6:5–7). Preaching must be \"in sincerity, as from God\" (2 Cor. 2:17; cf. 1:12). Paul's pastoral vision for his converts is that they be \"sincere and blameless\" at Christ's day (Phil. 1:10; cf. 1 Cor. 5:8). In Scripture, sincerity is not naïve simplicity but the moral integrity in which inner and outer life are transparent to God and each other.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "sincerity"},
        "key_refs": ["1 Corinthians 5:8", "2 Corinthians 1:12", "Philippians 1:10", "Ephesians 6:5", "Matthew 6:1"]
    },
    "slothfulness": {
        "id": "slothfulness",
        "term": "Slothfulness",
        "category": "concepts",
        "intro": "<p>Slothfulness — habitual laziness and reluctance to exert effort — is treated in Proverbs as one of the cardinal practical vices, leading to poverty, frustration, and self-destruction. The sluggard (Hebrew <em>atsel</em>) is held up as a warning: he desires but does not work (Prov. 13:4; 21:25–26), makes excuses to avoid leaving the house (Prov. 22:13; 26:13), turns on his bed like a door on its hinges (Prov. 26:14), and is wiser in his own conceit than seven men who can answer wisely (Prov. 26:16). The result is poverty as a robber (Prov. 6:10–11; 24:33–34) and a harvest lost (Prov. 10:5). In the NT, the context broadens from manual labor to spiritual readiness: the servant who buries his talent rather than trading with it is condemned as \"wicked and slothful\" (Matt. 25:26). The writer of Hebrews charges believers not to be sluggish but to imitate those who through faith and patience inherit the promises (Heb. 6:12). Paul's imperative is direct: \"Do not be slothful in zeal, be fervent in spirit, serve the Lord\" (Rom. 12:11). Slothfulness thus fails both the neighbor and God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "slothfulness"},
        "key_refs": ["Proverbs 6:6", "Proverbs 13:4", "Matthew 25:26", "Hebrews 6:12", "Romans 12:11"]
    },
    "temperance": {
        "id": "temperance",
        "term": "Temperance",
        "category": "concepts",
        "intro": "<p>Temperance (Greek <em>enkrateia</em>, self-control; <em>sophrosyne</em>, sobriety of mind) is the virtue of moderation and self-governance in appetites, passions, and pleasures. In the NT it appears as a fruit of the Spirit (Gal. 5:23) and as a qualification for church leaders (Tit. 1:8; 1 Tim. 3:2). Paul uses the metaphor of an athlete to describe Christian self-mastery: \"Every athlete exercises self-control in all things. They do it to receive a perishable wreath, but we an imperishable. So I do not run aimlessly; I do not box as one beating the air. But I discipline my body and keep it under control, lest after preaching to others I myself should be disqualified\" (1 Cor. 9:25–27). The temperance called for in Scripture is not asceticism — God provides good things to be received with thanksgiving (1 Tim. 4:3–4) — but the avoidance of excess in eating, drinking, and passion. The OT condemns drunkenness (Prov. 20:1; 23:29–35; Isa. 5:11) and the NT exhorts sobriety as the moral counterpart to eschatological readiness (1 Thess. 5:6–8; 1 Pet. 1:13; 5:8). Peter lists self-control as a foundational virtue to be built on faith (2 Pet. 1:6).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "temperance"},
        "key_refs": ["Galatians 5:23", "1 Corinthians 9:25", "2 Peter 1:6", "Proverbs 20:1", "1 Peter 5:8"]
    },
    "advice": {
        "id": "advice",
        "term": "Advice",
        "category": "concepts",
        "intro": "<p>Advice and counsel occupy a prominent place in biblical wisdom ethics, which consistently prizes seeking guidance from multiple wise counselors over relying on one's own judgment. Proverbs makes this the cardinal rule of practical decision-making: \"Without counsel plans fail, but with many advisers they succeed\" (Prov. 15:22; cf. 11:14; 24:6). The wise king Rehoboam's rejection of his elders' counsel in favor of the advice of younger men led to the division of the kingdom (1 Kgs. 12:6–16) — the paradigm case of catastrophic failure to heed good advice. Conversely, Jethro's practical counsel to Moses about delegating judicial responsibility (Ex. 18:14–23) demonstrates wise advice that preserves both the leader and the community. The ultimate source of counsel is God himself: \"For the LORD gives wisdom; from his mouth come knowledge and understanding\" (Prov. 2:6; Isa. 9:6, where the Messiah is called Wonderful Counselor). In the NT, the Spirit's role as the Counselor or Helper (<em>Parakletos</em>, John 14:16, 26) extends this theme: believers are guided into all truth by divine wisdom rather than human speculation alone. Accepting reproof and correction — the hard form of advice — is itself the mark of the wise person (Prov. 12:15; 13:18).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "advice"},
        "key_refs": ["Proverbs 15:22", "Proverbs 11:14", "1 Kings 12:8", "Proverbs 2:6", "John 14:16"]
    },
    "agency-free-moral": {
        "id": "agency-free-moral",
        "term": "Agency, Free Moral",
        "category": "concepts",
        "intro": "<p>Free moral agency is the theological principle that human beings, as created in the image of God, possess genuine freedom to choose between obedience and disobedience, moral good and evil — a freedom that grounds human responsibility before God. Scripture consistently addresses humanity as genuinely responsible for its choices: commands, warnings, invitations, and threats presuppose the capacity to respond. The foundational text is Moses's final charge: \"I have set before you life and death, blessing and curse. Therefore choose life, that you and your offspring may live\" (Deut. 30:19). Joshua similarly poses a genuine alternative: \"Choose this day whom you will serve\" (Josh. 24:15). The prophets' calls to repentance (Isa. 1:16–18; Ezek. 18:30–32) are unintelligible apart from the assumption of genuine moral freedom. Christian theology has historically paired this conviction with the doctrine of total depravity and divine sovereignty: fallen human will is free in the sense of operating without external compulsion yet is bent away from God by sin (Rom. 3:10–12; John 8:34) and requires divine grace to choose rightly (John 6:44; Phil. 2:13). The tension between genuine human freedom and sovereign divine grace is one of the most debated questions in Christian theology, addressed differently in Reformed, Arminian, and Catholic traditions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "agency-free-moral"},
        "key_refs": ["Deuteronomy 30:19", "Joshua 24:15", "Ezekiel 18:30", "Romans 3:11", "Philippians 2:13"]
    },
    "anxiety": {
        "id": "anxiety",
        "term": "Anxiety",
        "category": "concepts",
        "intro": "<p>Anxiety (Hebrew <em>de'agah</em>, care; Greek <em>merimna</em>, anxious care) is the experience of worry, dread, or inner agitation about present or future circumstances. Scripture takes anxiety seriously as a human reality while consistently directing believers toward trust in God as the antidote. Proverbs acknowledges that \"anxiety in a man's heart weighs it down, but a good word makes it glad\" (Prov. 12:25). The Psalms give voice to anxiety in the lament tradition (Pss. 38:18; 94:19; 139:23) before resolving into trust in divine care. Jesus's most extended treatment of anxiety in the Sermon on the Mount (Matt. 6:25–34) forbids anxious worry about material needs — food, drink, clothing — on the basis that the heavenly Father knows and provides. The command \"Do not be anxious\" (<em>me merimnate</em>) is grounded not in denial of need but in the radical security of the kingdom: \"Seek first the kingdom of God and his righteousness, and all these things will be added to you\" (Matt. 6:33). Paul echoes this: \"Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God\" (Phil. 4:6), promising a peace that surpasses understanding. Peter grounds the release of anxiety in divine care: \"Cast all your anxiety on him because he cares for you\" (1 Pet. 5:7).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "anxiety"},
        "key_refs": ["Matthew 6:25", "Philippians 4:6", "1 Peter 5:7", "Proverbs 12:25", "Psalm 94:19"]
    },
    "avarice": {
        "id": "avarice",
        "term": "Avarice",
        "category": "concepts",
        "intro": "<p>Avarice (covetousness, Hebrew <em>betsa</em>; Greek <em>pleonexia</em>) is the insatiable craving for more wealth or possessions — a vice Scripture treats as idolatry and the root of profound social and spiritual harm. The tenth commandment targets the desire itself: \"You shall not covet your neighbor's house... wife... or anything that is your neighbor's\" (Ex. 20:17), recognizing that external sin begins with disordered inner desire. Ecclesiastes diagnoses the avaricious person: \"He who loves money will not be satisfied with money, nor he who loves wealth with his income; this also is vanity\" (Eccl. 5:10). The prophets connect avarice with oppression: Micah denounces those who covet fields and seize them (Mic. 2:2); Ezekiel charges Jerusalem with being consumed by greed (Ezek. 22:13–14). In the NT, Paul identifies covetousness as idolatry (Col. 3:5; Eph. 5:5), because it places created things in the position that God alone should occupy. Jesus warns: \"Take care, and be on your guard against all covetousness, for one's life does not consist in the abundance of his possessions\" (Luke 12:15), following immediately with the parable of the rich fool. The remedy is radical contentment: \"Godliness with contentment is great gain\" (1 Tim. 6:6; Phil. 4:11–12).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "avarice"},
        "key_refs": ["Exodus 20:17", "Luke 12:15", "Colossians 3:5", "Ecclesiastes 5:10", "1 Timothy 6:6"]
    },
    "brotherly-kindness": {
        "id": "brotherly-kindness",
        "term": "Brotherly Kindness",
        "category": "concepts",
        "intro": "<p>Brotherly kindness (Greek <em>philadelphia</em>, lit. \"love of brothers\") is the warm, practical affection that members of the covenant community are to show toward one another, grounded in the shared family bond created by God's redemption. In the NT, the term draws on the OT family and covenant concepts while redefining the family: all who are in Christ are brothers and sisters, regardless of ethnic or social distinctions (Gal. 3:28; Rom. 8:29). Paul commands: \"Love one another with brotherly affection (<em>philadelphia</em>). Outdo one another in showing honor\" (Rom. 12:10). The Thessalonians are commended for their <em>philadelphia</em> but exhorted to abound in it still more (1 Thess. 4:9–10). The writer of Hebrews places it first in practical exhortation: \"Let brotherly love continue\" (Heb. 13:1). Peter calls it the penultimate virtue in the chain of Christian character, to be supplemented by <em>agape</em> — unconditional love that extends even to enemies (2 Pet. 1:7). John grounds the obligation theologically: \"If God so loved us, we also ought to love one another\" (1 John 4:11), making mutual love the visible proof of divine love's reality. The command to love the brotherhood specifically appears in 1 Peter 2:17.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "brotherly-kindness"},
        "key_refs": ["Romans 12:10", "Hebrews 13:1", "2 Peter 1:7", "1 Thessalonians 4:9", "1 Peter 2:17"]
    },
    "cheerfulness": {
        "id": "cheerfulness",
        "term": "Cheerfulness",
        "category": "concepts",
        "intro": "<p>Cheerfulness — the disposition of gladness, lightheartedness, and joyful countenance — is valued in Scripture as both a personal virtue and a social gift, reflecting the goodness of God experienced in life. Proverbs develops the connection between inner attitude and physical wellbeing: \"A cheerful heart is good medicine, but a crushed spirit dries up the bones\" (Prov. 17:22; cf. 15:13; 15:15). The Psalms call for joyful expression in worship: \"Come before his presence with singing\" (Ps. 100:2; cf. Ps. 66:1; 81:1). In the NT, cheerfulness is named as the disposition proper to acts of mercy: \"The one who does acts of mercy, with cheerfulness (<em>hilarotes</em>)\" (Rom. 12:8), suggesting that joyless service defeats its own purpose. Paul grounds Christian cheerfulness not in circumstances but in the Lord's presence: \"Rejoice in the Lord always; again I will say, rejoice\" (Phil. 4:4), written from prison. James frames the proper response to trials as joy (Jas. 1:2), and Peter urges rejoicing even in suffering as participation in Christ's sufferings (1 Pet. 4:13). The ultimate ground of Christian cheerfulness is eschatological: the hope of sharing God's glory (Rom. 5:2) transforms present hardship into occasion for persevering joy.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "cheerfulness"},
        "key_refs": ["Proverbs 17:22", "Romans 12:8", "Philippians 4:4", "James 1:2", "1 Peter 4:13"]
    },
    "choosing": {
        "id": "choosing",
        "term": "Choosing",
        "category": "concepts",
        "intro": "<p>The act of choosing runs throughout Scripture as a fundamental dimension of human moral life and as the distinctive act of divine election. On the human side, Scripture presents genuine choice as both the privilege and the burden of moral agents: Moses charges Israel to choose life or death, blessing or curse (Deut. 30:15–19); Joshua demands a decision about whom to serve (Josh. 24:15); Elijah confronts Israel's vacillation: \"How long will you go limping between two different opinions? If the LORD is God, follow him; but if Baal, then follow him\" (1 Kgs. 18:21). Wisdom calls for the deliberate choice of the fear of the LORD over folly (Prov. 1:29; 3:31). On the divine side, God's choosing is the source of all salvific blessing: he chose Abraham (Neh. 9:7), Israel from among the nations (Deut. 7:6–7), David from among his brothers (1 Sam. 16:8–13), and in the NT, the church in Christ \"before the foundation of the world\" (Eph. 1:4). Jesus chooses his disciples (John 15:16: \"You did not choose me, but I chose you\") and this divine choice grounds their mission and perseverance. The interplay between human responsibility to choose and divine sovereignty in election is a defining tension of biblical soteriology.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "choosing"},
        "key_refs": ["Deuteronomy 30:19", "Joshua 24:15", "1 Kings 18:21", "Ephesians 1:4", "John 15:16"]
    },
    "contention": {
        "id": "contention",
        "term": "Contention",
        "category": "concepts",
        "intro": "<p>Contention — quarreling, strife, and argumentative conflict — is consistently treated in Scripture as a mark of folly and a destroyer of community. Proverbs is especially insistent: \"It is an honor for a man to keep aloof from strife, but every fool will be quarreling\" (Prov. 20:3); \"The beginning of strife is like letting out water, so quit before the quarrel breaks out\" (Prov. 17:14); a quarrelsome wife is compared to the dripping of water on a rainy day (Prov. 19:13; 21:9, 19; 27:15). The contentious person is identified as someone who stirs up division by repeating matters (Prov. 17:9; 26:21). In the NT, Paul lists contentions and quarrels among the works of the flesh (Gal. 5:20; 2 Cor. 12:20) and as characteristic of pre-conversion foolishness (Tit. 3:9). Timothy is warned to avoid foolish controversies that breed quarrels (2 Tim. 2:23–24). James locates the root of conflicts in disordered passions and desires (Jas. 4:1–2). The positive counterpart to contention is the peace of the Spirit (Gal. 5:22), the meekness that receives instruction (Jas. 1:21), and the pursuit of what makes for peace (Rom. 14:19; Heb. 12:14).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "contention"},
        "key_refs": ["Proverbs 20:3", "Proverbs 17:14", "Galatians 5:20", "2 Timothy 2:23", "James 4:1"]
    },
    "cursing": {
        "id": "cursing",
        "term": "Cursing",
        "category": "concepts",
        "intro": "<p>Cursing in Scripture encompasses two distinct phenomena: the pronouncement of divine judgment and penalty upon disobedience, and the sinful human use of speech to invoke harm upon others or to blaspheme God. Divine curses are consequential pronouncements that follow covenant violation — the curse upon the serpent (Gen. 3:14–15), upon Cain (Gen. 4:11), and the covenant curses of Deuteronomy 27–28 that would fall on an disobedient Israel. These are the sovereign declarations of the Judge of all the earth. Human cursing of God or rulers is condemned (Ex. 22:28; Lev. 24:15–16; 2 Sam. 16:5–8), and Shimei's cursing of David is the paradigmatic example. The NT teaching on cursing is particularly striking: Jesus commands blessing those who curse you (Matt. 5:44; Luke 6:28), and Paul echoes the instruction: \"Bless and do not curse\" (Rom. 12:14). James notes the grotesque incongruity of using the same tongue to bless God and curse men made in his image (Jas. 3:9–10). Peter applies the pattern to Christ: \"When he was reviled, he did not revile in return; when he suffered, he did not threaten, but continued entrusting himself to him who judges justly\" (1 Pet. 2:23). The redeemed are released from the curse of the law through Christ, who became a curse for them (Gal. 3:13).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "cursing"},
        "key_refs": ["Genesis 3:14", "Galatians 3:13", "Romans 12:14", "Matthew 5:44", "James 3:9"]
    },
    "discontentment": {
        "id": "discontentment",
        "term": "Discontentment",
        "category": "concepts",
        "intro": "<p>Discontentment — the restless dissatisfaction with one's circumstances, provision, or station — is treated in Scripture as a spiritual failure rooted in distrust of divine goodness and sovereignty. Its most extensive and tragic exhibition is Israel's murmuring in the wilderness: despite miraculous delivery from Egypt, daily manna, water from the rock, and the pillar of fire, Israel constantly grumbled against God and Moses — about water (Ex. 15:24; 17:2–3), food (Ex. 16:2–3; Num. 11:1–6), and the land itself (Num. 14:2–3). Paul cites this as a warning for the church: \"Do not grumble, as some of them did and were destroyed by the Destroyer\" (1 Cor. 10:10). Discontentment with God's provision opens the door to covetousness (Ex. 20:17; Heb. 13:5) and to the social sins of complaining, murmuring, and disputing (Phil. 2:14). The antidote Paul commends is a learned discipline: \"I have learned, in whatever state I am, to be content. I know how to be brought low, and I know how to abound\" (Phil. 4:11–12), grounded in the sufficiency of Christ (Phil. 4:13). Contentment with godliness is, by contrast, great gain (1 Tim. 6:6–8), and the writer of Hebrews commands: \"Keep your life free from love of money, and be content with what you have\" (Heb. 13:5).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "discontentment"},
        "key_refs": ["Philippians 4:11", "1 Corinthians 10:10", "Hebrews 13:5", "Numbers 11:1", "1 Timothy 6:6"]
    },
    "evil-for-evil": {
        "id": "evil-for-evil",
        "term": "Evil for Evil",
        "category": "concepts",
        "intro": "<p>Returning evil for evil — repaying harm with harm, injury with injury — is the natural human response to wrong and the object of one of the NT's most explicit prohibitions. The principle of proportional retaliation (<em>lex talionis</em>: eye for eye, tooth for tooth, Ex. 21:24; Lev. 24:20; Deut. 19:21) was given in Mosaic law to limit disproportionate private vengeance by placing justice in the hands of courts, not individuals. Jesus cites and transcends the formula in the Sermon on the Mount, commanding non-resistance and active love of enemies instead (Matt. 5:38–42). Paul states the prohibition plainly: \"Repay no one evil for evil, but give thought to do what is honorable in the sight of all\" (Rom. 12:17). Peter grounds the renunciation of evil for evil in Christ's example — he did not return curse for curse but entrusted himself to the righteous Judge (1 Pet. 2:23; 3:9). The positive command that accompanies the prohibition transforms the ethics entirely: \"Do not be overcome by evil, but overcome evil with good\" (Rom. 12:21). This is not passivity but a deliberate offensive — meeting harm with love, which alone has power to transform the wrongdoer and display the character of God (Luke 6:35).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "evil-for-evil"},
        "key_refs": ["Romans 12:17", "Romans 12:21", "1 Peter 3:9", "Matthew 5:38", "Luke 6:35"]
    },
    "evil-speaking": {
        "id": "evil-speaking",
        "term": "Evil Speaking",
        "category": "concepts",
        "intro": "<p>Evil speaking (Greek <em>katalalia</em>, <em>blasphemia</em>, <em>katalalos</em>) encompasses slander, malicious gossip, defamation, and harmful speech about others — sins of the tongue that are persistently condemned in both Testaments. The Psalms contrast the wicked whose mouths are full of deceit and whose tongues devise mischief (Ps. 50:19; 52:2–4; 140:3) with the righteous whose speech is truth. Proverbs identifies the slanderer as a destroyer of friendship and community (Prov. 11:13; 16:28; 26:20). Leviticus explicitly forbids going about as a talebearer among the people (Lev. 19:16). In the NT, Paul lists <em>katalalia</em> (evil speaking, slander) among the vices from which the Corinthians have not repented (2 Cor. 12:20) and catalogs it with other sins of disordered speech to be put away (Eph. 4:31; Col. 3:8). Peter calls believers to lay aside all malice, deceit, hypocrisy, envy, and slander (<em>katalaliai</em>) as part of spiritual growth (1 Pet. 2:1). James's extended treatment of the tongue (Jas. 3:1–12) exposes its destructive potential: it is a fire, a world of unrighteousness, capable of defiling the whole body. The remedy is speech seasoned with grace (Col. 4:6), building up rather than tearing down (Eph. 4:29).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "evil-speaking"},
        "key_refs": ["Leviticus 19:16", "Ephesians 4:31", "1 Peter 2:1", "James 3:6", "Colossians 3:8"]
    },
    "false-accusation": {
        "id": "false-accusation",
        "term": "False Accusation",
        "category": "concepts",
        "intro": "<p>False accusation — charging another with offenses they did not commit — is prohibited and condemned throughout Scripture as a violation of truth, justice, and love of neighbor. The ninth commandment specifically addresses it: \"You shall not bear false witness against your neighbor\" (Ex. 20:16), and Mosaic law prescribed rigorous scrutiny of testimony in capital cases (Deut. 19:15–19), requiring the malicious false witness to suffer the very penalty he sought to inflict. The Psalms are filled with laments by the righteous wrongly accused: \"False witnesses have risen against me, and they breathe out violence\" (Ps. 27:12; cf. Pss. 35:11; 109:2–3). Naboth's murder through suborned false testimony (1 Kgs. 21:10–13) is the OT's most notorious judicial murder by false accusation. The trial of Jesus, condemned through coordinated false testimony (Matt. 26:59–61; Mark 14:56–58), repeats this pattern at the highest level. In the NT epistles, Peter encourages believers enduring slanders and false charges to maintain honorable conduct, \"so that when you are spoken against as evildoers, those who slander your good behavior in Christ may be put to shame\" (1 Pet. 3:16; cf. 2:12). The final judgment will vindicate the falsely accused and expose all hidden works of darkness (1 Cor. 4:5).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "false-accusation"},
        "key_refs": ["Exodus 20:16", "Psalm 27:12", "Matthew 26:60", "1 Peter 3:16", "Deuteronomy 19:16"]
    },
    "fraud": {
        "id": "fraud",
        "term": "Fraud",
        "category": "concepts",
        "intro": "<p>Fraud — the obtaining of something through deception, false representation, or dishonest means — is condemned throughout Scripture as a violation of truth, justice, and neighbor love. Mosaic law required just weights and honest measures and prohibited deceptive commercial practices (Lev. 19:35–36; Deut. 25:13–16; Prov. 11:1). The prophets denounced commercial fraud as emblematic of Israel's covenant unfaithfulness: Amos condemns those who make the ephah small and the shekel great, who buy the poor for a pair of sandals (Amos 8:5–6); Hosea accuses Israel of being a merchant in whose hands are false balances (Hos. 12:7); Micah denounces short measures and dishonest scales (Mic. 6:10–11). The wisdom literature identifies fraud as a characteristic of the wicked: \"A man who wrongs his neighbor and then says, 'I was only joking!' is like a madman throwing firebrands\" (Prov. 26:18–19). In the NT, the same Lord who warned against defrauding in trade (Mark 10:19) is the one before whose judgment seat all accounts will be rendered. James condemns the fraudulent withholding of wages from laborers as a crying sin before God: \"The wages you failed to pay the workers who mowed your fields are crying out against you\" (Jas. 5:4). Zacchaeus's fourfold restoration of defrauded amounts is held up as a model of genuine repentance (Luke 19:8).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "fraud"},
        "key_refs": ["Leviticus 19:35", "Amos 8:5", "James 5:4", "Luke 19:8", "Proverbs 11:1"]
    },
    "generosity": {
        "id": "generosity",
        "term": "Generosity",
        "category": "concepts",
        "intro": "<p>Generosity — the free and cheerful giving of resources, time, or service for others' good — flows in Scripture from God's own character as the ultimate giver and reflects the covenant obligation to care for the vulnerable. God's generosity to Israel is the motivating basis for Israel's generosity to the poor: \"You shall open wide your hand to your brother, to the needy and to the poor\" (Deut. 15:11; Lev. 25:35). The law mandated gleaning for the poor, the sabbatical release of debts, and tithing for the Levite, stranger, orphan, and widow (Deut. 14:28–29; 26:12–13). Proverbs frames generosity as both right and self-enriching: \"One gives freely, yet grows all the richer; another withholds what he should give, and only suffers want\" (Prov. 11:24–25; cf. Prov. 22:9). In the NT, Jesus commends the poor widow who gave all she had (Luke 21:2–4) and grounds giving in the divine pattern: \"The measure you give will be the measure you get\" (Luke 6:38). Paul presents the Macedonian churches' generosity in poverty as a model of grace (2 Cor. 8:1–5) and articulates the fundamental principle: \"God loves a cheerful giver\" (2 Cor. 9:7), grounding all Christian giving in Christ's supreme gift: \"He who did not spare his own Son\" (Rom. 8:32).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "generosity"},
        "key_refs": ["Deuteronomy 15:11", "Proverbs 11:24", "2 Corinthians 9:7", "Luke 21:3", "Romans 8:32"]
    },
    "godly": {
        "id": "godly",
        "term": "Godly",
        "category": "concepts",
        "intro": "<p>\"The godly\" (Hebrew <em>hasid</em>, \"faithful one\"; Greek <em>eusebeis</em>) designates in Scripture those who are characterized by devoted loyalty to God — not merely moral rectitude but a relationship of trust, love, and covenant fidelity. The Psalms frequently contrast the godly (<em>hasidim</em>) with the wicked: God preserves the godly (Ps. 4:3; 12:1; 32:6; 37:28; 97:10; 145:17) while the way of the wicked will perish. The godly person is defined not by a fixed ethical checklist but by orientation toward God — \"the LORD is near to all who call on him\" (Ps. 145:18). In the NT epistles, <em>eusebeia</em> (godliness, piety) is a key term for the comprehensive orientation of a Christian life toward God. Paul contrasts the godly life of suffering and witness with empty religiosity (2 Tim. 3:1–5, 12): \"Indeed, all who desire to live a godly life in Christ Jesus will be persecuted\" (2 Tim. 3:12). Peter exhorts believers to pursue godliness as one of the key virtues of Christian growth (2 Pet. 1:6–7) and grounds the moral imperative eschatologically: \"Since all these things are thus to be dissolved, what sort of people ought you to be in lives of holiness and godliness\" (2 Pet. 3:11). Paul summarizes: \"Godliness with contentment is great gain\" (1 Tim. 6:6).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "godly"},
        "key_refs": ["Psalm 4:3", "2 Timothy 3:12", "2 Peter 1:6", "1 Timothy 6:6", "Psalm 145:18"]
    },
    "good-and-evil": {
        "id": "good-and-evil",
        "term": "Good and Evil",
        "category": "concepts",
        "intro": "<p>The distinction between good and evil is foundational to biblical ethics and creation theology. Creation is declared good by God (Gen. 1:4, 10, 12, 18, 21, 25, 31); the fall introduces evil not as a co-eternal principle competing with God but as the corruption of what God made good through the creature's disobedience. The tree of the knowledge of good and evil (Gen. 2:9, 17) stands at the center of the garden as the boundary of human authority — the divine prerogative of determining what is good is not transferred to humanity by right but seized in rebellion. The result is the confusion of good and evil that prophets lament: \"Woe to those who call evil good and good evil\" (Isa. 5:20). Moral discernment — the capacity to distinguish good from evil — is itself a gift: Solomon prays for \"an understanding mind to govern your people, that I may discern between good and evil\" (1 Kgs. 3:9), and Christian maturity involves having \"powers of discernment trained by constant practice to distinguish good from evil\" (Heb. 5:14). The NT's ethical imperatives consistently call for active pursuit of good and avoidance of evil (Rom. 12:9; 1 Thess. 5:21–22; 1 Pet. 3:11), culminating in the final separation at the last judgment (Matt. 25:31–46).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "good-and-evil"},
        "key_refs": ["Genesis 2:9", "Isaiah 5:20", "Hebrews 5:14", "Romans 12:9", "1 Thessalonians 5:21"]
    },
    "good-for-evil": {
        "id": "good-for-evil",
        "term": "Good for Evil",
        "category": "concepts",
        "intro": "<p>Returning good for evil — answering harm with benefit, wrong with blessing — is the radical moral standard set by Jesus and reinforced throughout the NT as the distinctively Christian form of neighbor love. Jesus states it most sharply in the Sermon on the Mount: \"Love your enemies and pray for those who persecute you, so that you may be sons of your Father who is in heaven; for he makes his sun rise on the evil and on the good, and sends rain on the just and on the unjust\" (Matt. 5:44–45; Luke 6:27–28, 35). The motivation is participation in the divine character: God himself practices good toward his enemies. Joseph's treatment of his brothers — providing food and reconciliation rather than retaliation despite their past treachery (Gen. 50:19–21) — is the OT's fullest narrative illustration, rendered explicitly: \"You intended to harm me, but God intended it for good.\" Paul systematizes the principle: \"Repay no one evil for evil... Do not be overcome by evil, but overcome evil with good\" (Rom. 12:17, 21). Peter grounds it in Christ's passion: \"When he was reviled, he did not revile in return; when he suffered, he did not threaten\" (1 Pet. 2:23). Returning good for evil is thus not merely a moral strategy but an imitation of God's own redemptive character.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "good-for-evil"},
        "key_refs": ["Matthew 5:44", "Genesis 50:20", "Romans 12:21", "Luke 6:35", "1 Peter 2:23"]
    },
    "gossip": {
        "id": "gossip",
        "term": "Gossip",
        "category": "concepts",
        "intro": "<p>Gossip (Hebrew <em>nirgan</em>, whisperer; <em>rakil</em>, talebearer; Greek <em>psithurismos</em>, whispering) designates the sharing of damaging or private information about others in an informal, often malicious context. Mosaic law prohibits going about as a slanderer: \"You shall not go around as a slanderer among your people\" (Lev. 19:16). Proverbs consistently condemns the gossip as a destroyer: \"A whisperer separates close friends\" (Prov. 16:28; 17:9); \"The words of a whisperer are like delicious morsels; they go down into the inner parts of the body\" (Prov. 18:8; 26:22), capturing both the appetizing appeal and the destructive effect of gossip. Without a gossip, quarreling ceases (Prov. 26:20). Paul lists gossips and slanderers among those who suppress the truth and whose hearts are darkened (Rom. 1:29–30) and among the sins he fears finding unrepented in Corinth (2 Cor. 12:20). He also warns Timothy that younger widows who are idle learn to be gossips and busybodies (1 Tim. 5:13). James's teaching on the tongue (Jas. 3:5–12) provides the theological basis for condemning gossip: the tongue's destructive capacity is disproportionate to its size, like a small fire that sets a great forest ablaze. The remedy is speech that builds up (Eph. 4:29) and love that covers a multitude of sins (1 Pet. 4:8; Prov. 10:12).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "gossip"},
        "key_refs": ["Leviticus 19:16", "Proverbs 16:28", "Romans 1:29", "2 Corinthians 12:20", "James 3:6"]
    },
    "greed": {
        "id": "greed",
        "term": "Greed",
        "category": "concepts",
        "intro": "<p>Greed (Hebrew <em>betsa</em>, unjust gain; Greek <em>pleonexia</em>, wanting more) is the excessive desire for material wealth or possessions, condemned in Scripture as spiritual idolatry and social destructiveness. The prophets connect it directly with oppression: Micah denounces those who covet fields and violently take them (Mic. 2:2); Ezekiel charges Jerusalem's leaders with shedding blood for dishonest gain (Ezek. 22:12–13); Isaiah pronounces woe on those who add house to house and field to field (Isa. 5:8). The wisdom literature warns: \"A greedy man stirs up strife, but the one who trusts in the LORD will be enriched\" (Prov. 28:25). In the NT, Jesus identifies greed as a deadly spiritual danger: \"Take care, and be on your guard against all covetousness, for one's life does not consist in the abundance of his possessions\" (Luke 12:15). The rich young ruler's departure in grief reveals how greed can block entry into the kingdom (Matt. 19:22). Paul names greed as idolatry (Col. 3:5; Eph. 5:5) — placing money in the position of God — and requires that elders be free from love of money (1 Tim. 3:3; Tit. 1:7). The love of money, rather than money itself, is identified as \"a root of all kinds of evils\" (1 Tim. 6:10).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "greed"},
        "key_refs": ["Luke 12:15", "Colossians 3:5", "1 Timothy 6:10", "Proverbs 28:25", "Micah 2:2"]
    },
    "insincerity": {
        "id": "insincerity",
        "term": "Insincerity",
        "category": "concepts",
        "intro": "<p>Insincerity — the gap between professed and actual motive, between outward expression and inward reality — is one of the moral vices most consistently exposed and condemned by Jesus. The Pharisees provide Scripture's paradigm case: their elaborate public piety — conspicuous fasting, extended public prayers, whitened tombs — concealed inner impurity (Matt. 6:1–7, 16–18; 23:25–28). Jesus condemns this as hypocrisy, and its characteristic marker is performance of religious duty for human recognition rather than divine relationship. Isaiah had already identified Israel's insincere worship: \"This people honors me with their lips, but their heart is far from me\" (Isa. 29:13; cf. Matt. 15:8; Mark 7:6). Paul repeatedly contrasts serving as one who aims to please God, not men: \"For am I now seeking the approval of man, or of God? Or am I trying to please man? If I were still trying to please man, I would not be a servant of Christ\" (Gal. 1:10; cf. 1 Thess. 2:4–5; Eph. 6:5–7). The alternative to insincerity is not perfect moral consistency but genuine transparency before God and others — the \"unleavened bread of sincerity and truth\" (1 Cor. 5:8) that becomes possible through confession and walking in the light (1 John 1:7–9).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "insincerity"},
        "key_refs": ["Isaiah 29:13", "Matthew 23:27", "Galatians 1:10", "1 Corinthians 5:8", "1 John 1:7"]
    },
    "insinuation": {
        "id": "insinuation",
        "term": "Insinuation",
        "category": "concepts",
        "intro": "<p>Insinuation — the art of indirectly planting a damaging suggestion or implication without direct accusation — is a subtle form of slander condemned by the spirit, if not always the letter, of Scripture's commands against bearing false witness and evil speaking. Unlike direct false accusation, insinuation works through implication, tone, and selective presentation of facts. Satan's approach to Eve in Genesis 3 models insinuation: \"Did God actually say...?\" (Gen. 3:1) — a question designed to plant suspicion rather than assert a falsehood directly. The proverb captures its mechanics: \"For lack of wood the fire goes out, and where there is no whisperer, quarreling ceases\" (Prov. 26:20), acknowledging that much social conflict is fed by suggestions rather than direct statements. Absalom's insinuation against David — implying to petitioners that the king would not hear their case, if only there were someone like him in authority — was a calculated program of subversion (2 Sam. 15:3–4). The NT commands direct, honest speech: \"Let your 'yes' be yes and your 'no' be no\" (Jas. 5:12; Matt. 5:37), which rules out the calculated ambiguity insinuation requires. Paul calls believers to speak the truth in love (Eph. 4:15), making transparent communication the standard against which insinuation is measured and found wanting.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "insinuation"},
        "key_refs": ["Genesis 3:1", "Proverbs 26:20", "2 Samuel 15:3", "Ephesians 4:15", "James 5:12"]
    },
    "intemperance": {
        "id": "intemperance",
        "term": "Intemperance",
        "category": "concepts",
        "intro": "<p>Intemperance — the lack of self-regulation in appetites and desires, especially in eating and drinking — is condemned in Scripture as a failure of the self-governance that reflects the image of God and is required by covenant holiness. The OT addresses it primarily through prohibitions on drunkenness: \"Wine is a mocker, strong drink a brawler, and whoever is led astray by it is not wise\" (Prov. 20:1); the extended portrait of the drunkard in Proverbs 23:29–35 catalogs its physical, moral, and social destruction. Isaiah pronounces woe on those who rise early to run after strong drink and stay up late until wine inflames them (Isa. 5:11). The same principles apply to food: Proverbs links gluttony and drunkenness (Prov. 23:20–21), and the charge against the rebellious son includes being a glutton and drunkard (Deut. 21:20). In the NT, Paul requires sobriety of church leaders (1 Tim. 3:2–3; Tit. 1:7–8) and commands all believers: \"Do not get drunk with wine, for that is debauchery, but be filled with the Spirit\" (Eph. 5:18). The positive counterpart to intemperance is <em>enkrateia</em> — self-control, a fruit of the Spirit (Gal. 5:23) and a component of godly character (2 Pet. 1:6; Tit. 2:2). Intemperance ultimately reflects a disordered relationship with created goods — enjoying them outside the limits God set.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "intemperance"},
        "key_refs": ["Proverbs 20:1", "Ephesians 5:18", "Galatians 5:23", "Proverbs 23:29", "Isaiah 5:11"]
    },
    "laziness": {
        "id": "laziness",
        "term": "Laziness",
        "category": "concepts",
        "intro": "<p>Laziness — the habitual avoidance of work, effort, or duty — is treated in Scripture as both a practical vice leading to poverty and a spiritual failing that dishonors the Creator's design for human vocation. Proverbs is the primary biblical source, building a comprehensive portrait of the lazy person (sluggard): he will not plow in season and looks for a harvest that never comes (Prov. 20:4); he buries his hand in the dish and is too lazy to bring it back to his mouth (Prov. 26:15); he finds an implausible excuse for staying home (Prov. 22:13; 26:13). The consequences are clear: \"The sluggard craves and gets nothing, while the diligent are fully supplied\" (Prov. 13:4); poverty arrives like a robber (Prov. 6:9–11; 24:33–34). The ant is held before the lazy person as a rebuke: it stores in summer without being told (Prov. 6:6–8). In the NT, the parable of the talents condemns the servant who buried his talent rather than trading with it as \"wicked and lazy\" (Matt. 25:26). Paul's community discipline was blunt: he refused support to those who were unwilling to work (2 Thess. 3:10), having set a personal example of manual labor to supplement his ministry (Acts 20:34–35; 1 Cor. 4:12). The ground of the work ethic is creation: God placed the human in the garden to work and keep it (Gen. 2:15), making labor intrinsic to human dignity.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "laziness"},
        "key_refs": ["Proverbs 6:6", "Proverbs 13:4", "Matthew 25:26", "2 Thessalonians 3:10", "Genesis 2:15"]
    },
    "modesty": {
        "id": "modesty",
        "term": "Modesty",
        "category": "concepts",
        "intro": "<p>Modesty in Scripture encompasses both restraint in appearance and dress and humility of bearing and self-presentation — a virtue that reflects proper relationship to God and others rather than preoccupation with one's own display. The primary NT text on modest dress is 1 Timothy 2:9–10: Paul urges women to adorn themselves \"in respectable apparel, with modesty and self-control, not with braided hair and gold or pearls or costly attire, but with what is proper for women who profess godliness — with good works.\" Peter's parallel instruction (1 Pet. 3:3–4) contrasts external adornment with the \"hidden person of the heart\" having the imperishable beauty of a gentle and quiet spirit, which is precious in God's sight. Both passages redirect attention from outward display to inward character. Esther's initial refusal of elaborate presentation (Esth. 2:15) and Saul's self-description as a Benjaminite from the least of the tribes (1 Sam. 9:21) illustrate modesty of self-presentation. More broadly, modesty is the opposite of the ostentation condemned by Proverbs and the Prophets — the insistence on honoring others above oneself (Rom. 12:10; Phil. 2:3). Christian modesty thus reflects the mind of Christ who, though in the form of God, did not count equality with God a thing to be grasped (Phil. 2:6).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "modesty"},
        "key_refs": ["1 Timothy 2:9", "1 Peter 3:3", "Philippians 2:3", "Romans 12:10", "Proverbs 11:2"]
    },
    "moral-agency": {
        "id": "moral-agency",
        "term": "Moral Agency",
        "category": "concepts",
        "intro": "<p>Moral agency is the capacity to discern right from wrong and to act on that discernment in a way that carries genuine responsibility before God and others. Scripture consistently presupposes it: divine commands, covenant obligations, warnings, and promises are addressed to persons understood to be capable of genuine response. God's image in humanity (Gen. 1:26–28) grounds this capacity — humans are not mere instinct-driven creatures but beings capable of moral reasoning, choice, and accountability (Gen. 2:16–17; 3:11). Ezekiel's insistence on individual accountability reflects the assumption of genuine moral agency: \"The soul who sins shall die... the righteousness of the righteous shall be upon himself, and the wickedness of the wicked shall be upon himself\" (Ezek. 18:20). The NT deepens the picture: moral agency encompasses not only outward acts but inner dispositions — desire, intention, and motive — that God alone can fully see and judge (1 Cor. 4:5; Heb. 4:12–13; Matt. 5:21–28). Paul's theology holds moral agency in tension with the bondage of sin: \"I do not do what I want, but I do the very thing I hate\" (Rom. 7:15), and with divine enabling grace: \"Work out your own salvation with fear and trembling, for it is God who works in you\" (Phil. 2:12–13). The interplay between genuine human agency and divine sovereignty is one of Christian theology's central tensions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "moral-agency"},
        "key_refs": ["Ezekiel 18:20", "Philippians 2:12", "Romans 7:15", "Genesis 1:26", "Hebrews 4:12"]
    },
    "moral-law": {
        "id": "moral-law",
        "term": "Moral Law",
        "category": "concepts",
        "intro": "<p>The moral law in biblical theology refers to the permanent, universal ethical demands of God — typically identified with the Ten Commandments (Ex. 20:1–17; Deut. 5:6–21) and their summation in the commands to love God and neighbor (Matt. 22:37–40; Deut. 6:4–5; Lev. 19:18) — as distinct from the ceremonial and civil laws of Israel that were fulfilled or superseded in the new covenant. Reformed theology distinguishes these three uses of the law: the first, to reveal sin (Rom. 3:20; 7:7); the second, to restrain civil evil through common grace; and the third, to guide the believer's sanctification (Ps. 119). Paul insists the law is holy, just, and good (Rom. 7:12) even as it cannot justify (Gal. 3:11; Rom. 3:20). The moral law is not abolished by Christ but fulfilled: \"Do not think that I have come to abolish the Law or the Prophets; I have not come to abolish them but to fulfill them\" (Matt. 5:17). Paul's summary of the commandments — \"Love your neighbor as yourself\" (Rom. 13:8–10; Gal. 5:14) — shows that the moral law's substance is carried into the new covenant dispensation. The law written on the heart under the new covenant (Jer. 31:33; Heb. 8:10) is this moral law internalized by the Spirit rather than merely inscribed on tablets.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "moral-law"},
        "key_refs": ["Exodus 20:1", "Matthew 22:37", "Romans 7:12", "Jeremiah 31:33", "Matthew 5:17"]
    },
    "popular-sins": {
        "id": "popular-sins",
        "term": "Popular Sins",
        "category": "concepts",
        "intro": "<p>\"Popular sins\" designates those moral failures that are widespread, socially normalized, or culturally tolerated in a given era — and which Scripture consistently condemns even when the surrounding culture condones or celebrates them. The prophets' characteristic task was to identify and denounce precisely these: the social injustice that enriched the powerful (Amos 5:10–15; Isa. 10:1–2); the idolatry woven into popular religion and culture (Ezek. 8; Jer. 7:9–10); and sexual sins that the surrounding nations practiced as religious ritual (Lev. 18; 20; Deut. 12:31). The principle underlying prophetic condemnation of popular sins is that God's standard does not shift with majority practice: \"You shall not follow a majority to do evil\" (Ex. 23:2). Jesus addresses the same phenomenon in his generation — the legal casuistry that honored the letter while evading the spirit of the law (Matt. 15:3–9; 23:23–24), and the respectable sins of the heart (Matt. 5:21–48). Paul catalogues popular sins of his culture in Romans 1:18–32 — not as curiosities but as evidence of general human accountability. The NT calls for non-conformity to the world's patterns (Rom. 12:2) and a discernment of spirits to distinguish God's will from the spirit of the age (1 John 4:1).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "popular-sins"},
        "key_refs": ["Exodus 23:2", "Romans 12:2", "Amos 5:12", "Matthew 5:27", "1 John 4:1"]
    },
}


def main():
    written = 0
    skipped = 0
    first_term = list(ARTICLES.values())[0]['term']
    last_term = list(ARTICLES.values())[-1]['term']
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP gap-ethics: {first_term} -> {last_term}: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
