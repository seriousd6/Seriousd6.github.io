"""
BP Article Synthesis — gap-minor: Score-3 Nave stubs, minor concepts, and low-priority terms
30 entries — Nave-only sources

Script: scripts/bp-gap-minor.py
Run: python3 scripts/bp-gap-minor.py
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
        json.dump(data, f, ensure_ascii=False)


def merge_article(slug, data):
    # Never overwrite an existing synthesis — idempotent safety
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True


ARTICLES = {
    "betrothal": {
        "id": "betrothal",
        "term": "Betrothal",
        "category": "concepts",
        "intro": "<p>Betrothal in biblical culture was a formal pledge of marriage carrying greater legal weight than a modern engagement — it was the first stage of marriage itself, legally binding and dissoluble only by formal separation. Genesis 29:18–30 describes Jacob's betrothal to Rachel through a seven-year labor commitment, a form of bride price. The Mosaic law recognized the betrothed woman's legal standing: <a class=\"ref\" data-ref=\"Deuteronomy 20:7\">Deuteronomy 20:7</a> exempted a betrothed man from military service, and Deuteronomy 22:23–27 treated the violation of a betrothed woman on the same legal footing as adultery. The betrothal period in Second Temple Judaism typically lasted about one year, during which the couple lived apart but were fully bound.</p><p>The New Testament's most theologically significant use of betrothal is Mary's situation at the Annunciation: she was \"betrothed to a man whose name was Joseph\" (<a class=\"ref\" data-ref=\"Matthew 1:18\">Matthew 1:18</a>; <a class=\"ref\" data-ref=\"Luke 1:27\">Luke 1:27</a>), yet Joseph's discovery of her pregnancy led him to consider divorce — reflecting that betrothal was legally equivalent to marriage and required formal dissolution. Paul employs betrothal as an image of the church's covenant relationship with Christ: \"I betrothed you to one husband, to present you as a pure virgin to Christ\" (<a class=\"ref\" data-ref=\"2 Corinthians 11:2\">2 Corinthians 11:2</a>), framing gospel commitment in the strongest possible covenant terms.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "betrothal"},
        "key_refs": ["Genesis 29:18", "Deuteronomy 20:7", "Matthew 1:18", "Luke 1:27"]
    },
    "burning-bush": {
        "id": "burning-bush",
        "term": "Burning Bush",
        "category": "concepts",
        "intro": "<p>The burning bush was the miraculous sign through which God appeared to Moses in the Midian wilderness and commissioned him to lead Israel out of Egypt. While tending his father-in-law's flock near Mount Horeb, Moses saw a bush burning with fire that was not consumed, and turned aside to see it (<a class=\"ref\" data-ref=\"Exodus 3:2\">Exodus 3:2–5</a>). The LORD called from within the bush, instructed Moses to remove his sandals because the ground was holy, and revealed himself as \"the God of Abraham, the God of Isaac, and the God of Jacob\" — then disclosed his intention to deliver Israel, revealed the divine name (Exodus 3:14), and commissioned Moses as his agent.</p><p>The burning bush stands as one of the most theologically concentrated theophanies in Scripture: the fire that does not destroy what God inhabits signifies the holiness that purifies rather than annihilates, and the humble thorn bush chosen as the site of divine disclosure suggests God's freedom to sanctify the ordinary and the despised. Stephen cited the burning bush in his defense before the Sanhedrin as evidence that the God of Moses was not confined to the temple or to the land — he spoke \"in a flame of fire in a bush\" in the Midian wilderness (<a class=\"ref\" data-ref=\"Acts 7:30\">Acts 7:30</a>), making the ground holy wherever his presence rested. Patristic interpreters and Jewish tradition alike have read in the unconsumed bush a symbol of Israel's indestructibility in the fires of affliction and, in Christian reading, a foreshadowing of the incarnation — divine presence dwelling in a vessel it does not consume.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "burning-bush"},
        "key_refs": ["Exodus 3:2", "Exodus 3:14", "Acts 7:30"]
    },
    "eye-for-eye": {
        "id": "eye-for-eye",
        "term": "Eye for Eye",
        "category": "concepts",
        "intro": "<p>The principle of lex talionis — \"eye for eye, tooth for tooth\" — appears in three passages in the Mosaic law: <a class=\"ref\" data-ref=\"Exodus 21:24\">Exodus 21:24</a>, <a class=\"ref\" data-ref=\"Leviticus 24:20\">Leviticus 24:20</a>, and <a class=\"ref\" data-ref=\"Deuteronomy 19:21\">Deuteronomy 19:21</a>. In its original legal context, this was not a sanction for private vengeance but a standard of proportionality establishing that punishment must fit the crime and must not exceed it. In the ancient Near East, wealthy offenders often escaped with monetary fines while the poor suffered bodily punishment for identical crimes; the lex talionis embedded a principle of equal justice across social strata into Israelite law.</p><p>Jesus addresses the lex talionis directly in the Sermon on the Mount: \"You have heard that it was said, 'An eye for an eye and a tooth for a tooth.' But I say to you, Do not resist the one who is evil. But if anyone slaps you on the right cheek, turn to him the other also\" (<a class=\"ref\" data-ref=\"Matthew 5:38\">Matthew 5:38–39</a>). Jesus does not abolish the principle of justice but transcends it, calling his followers to a higher standard of non-retaliation and radical grace that goes beyond what justice requires. The lex talionis thus represents the minimum of justice — a floor — while the New Testament ethic calls believers toward a ceiling of mercy that reflects the character of God, who sends rain on the just and the unjust (<a class=\"ref\" data-ref=\"Matthew 5:45\">Matthew 5:45</a>).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "eye-for-eye"},
        "key_refs": ["Exodus 21:24", "Leviticus 24:20", "Deuteronomy 19:21", "Matthew 5:38"]
    },
    "free-will": {
        "id": "free-will",
        "term": "Free Will",
        "category": "concepts",
        "intro": "<p>The doctrine of free will concerns the capacity of human beings to make genuine moral choices and the compatibility of human freedom with divine sovereignty. Scripture affirms both realities without systematically resolving the tension: God is absolutely sovereign over history and human hearts (<a class=\"ref\" data-ref=\"Romans 8:28\">Romans 8:28–30</a>; <a class=\"ref\" data-ref=\"Ephesians 1:11\">Ephesians 1:11</a>; <a class=\"ref\" data-ref=\"Isaiah 46:10\">Isaiah 46:10</a>), yet human beings are genuinely responsible for their choices and summoned to decide (<a class=\"ref\" data-ref=\"Deuteronomy 30:19\">Deuteronomy 30:19</a>; <a class=\"ref\" data-ref=\"Joshua 24:15\">Joshua 24:15</a>; Acts 17:30). The biblical narrative presents characters who make real decisions with real consequences, while simultaneously presenting those events as the outworking of divine purposes.</p><p>Paul's extended discussion of election and hardening in Romans 9–11 is the most concentrated biblical engagement with this tension, though Paul's purpose there is primarily doxological — marveling at God's wisdom and mercy — rather than metaphysical. The free-will question reaches its sharpest form in the New Testament around the topics of repentance and faith: can fallen human beings freely turn to God, or does genuine turning require prior divine transformation? The classic Protestant positions — Arminianism (emphasizing human freedom to believe) and Calvinism (emphasizing divine election as the basis of faith) — both claim substantial scriptural grounding, and the discussion has defined much of Western Christian theology since Augustine's fifth-century controversy with Pelagius over the extent of human moral capacity after the Fall.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "free-will"},
        "key_refs": ["Deuteronomy 30:19", "Joshua 24:15", "Romans 8:28", "Ephesians 1:11"]
    },
    "golden-rule": {
        "id": "golden-rule",
        "term": "Golden Rule",
        "category": "concepts",
        "intro": "<p>The Golden Rule — \"So whatever you wish that others would do to you, do also to them\" (<a class=\"ref\" data-ref=\"Matthew 7:12\">Matthew 7:12</a>; cf. <a class=\"ref\" data-ref=\"Luke 6:31\">Luke 6:31</a>) — is Jesus' distillation of the whole ethical demand of the Law and the Prophets. The statement appears at the climax of the Sermon on the Mount's teaching on prayer and seeking God, as the capstone of Jesus' instruction on love of neighbor. The formulation is notably positive — what you wish to receive, actively do — rather than the negative form common in other ancient traditions (\"do not do to others what you do not want done to you\"), calling for active generosity rather than mere restraint from harm.</p><p>Jesus grounds the Golden Rule explicitly in Scripture: \"for this is the Law and the Prophets\" (<a class=\"ref\" data-ref=\"Matthew 7:12\">Matthew 7:12</a>), connecting it to the double commandment of love for God and neighbor (Matthew 22:37–40) that he identifies as the summary of the entire Old Testament. Leviticus 19:18 — \"you shall love your neighbor as yourself\" — is the Old Testament root from which the Golden Rule grows. Paul echoes the same principle in Romans 13:10 (\"love is the fulfilling of the law\") and Galatians 5:14 (\"the whole law is fulfilled in one word: 'You shall love your neighbor as yourself'\"). While similar maxims appear in Confucian, Stoic, and rabbinic traditions, the positive formulation and the explicit grounding in God's own love give the biblical Golden Rule its distinctive theological character as a command, not merely a prudential maxim.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "golden-rule"},
        "key_refs": ["Matthew 7:12", "Luke 6:31", "Leviticus 19:18"]
    },
    "i-am-that-i-am": {
        "id": "i-am-that-i-am",
        "term": "I Am That I Am",
        "category": "concepts",
        "intro": "<p>\"I AM THAT I AM\" (Hebrew: <em>Ehyeh asher Ehyeh</em>) is the divine name disclosed to Moses at the burning bush when he asked what he should tell Israel about who had sent him: \"God said to Moses, 'I AM WHO I AM.' And he said, 'Say this to the people of Israel: I AM has sent me to you'\" (<a class=\"ref\" data-ref=\"Exodus 3:14\">Exodus 3:14</a>). The phrase is linguistically related to the divine name YHWH (the Tetragrammaton, rendered LORD in English Bibles) and may be translated \"I AM WHAT I AM,\" \"I WILL BE WHAT I WILL BE,\" or \"I AM THE ONE WHO IS\" — all reflecting God's active, self-existent, and self-defining character as the one who is not derived from or dependent on anything outside himself.</p><p>The divine self-identification as pure being became foundational to theological reflection on God's aseity (self-existence) and immutability. The book of Revelation carries the same declaration into Greek eschatological language: \"grace to you... from him who is and who was and who is to come\" (<a class=\"ref\" data-ref=\"Revelation 1:4\">Revelation 1:4</a>), the divine name become an affirmation of eternal presence across all time. In the Gospel of John, Jesus' seven \"I am\" sayings and the climactic \"Before Abraham was, I am\" (<a class=\"ref\" data-ref=\"John 8:58\">John 8:58</a>) — which provoked the crowd to take up stones for blasphemy — carry deliberate resonance with the burning bush disclosure, presenting Jesus as sharing the divine being expressed in the Tetragrammaton.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "i-am-that-i-am"},
        "key_refs": ["Exodus 3:14", "Revelation 1:4", "John 8:58"]
    },
    "midianites": {
        "id": "midianites",
        "term": "Midianites",
        "category": "people",
        "intro": "<p>The Midianites were a nomadic or semi-nomadic tribal confederation descended from Midian, the fourth son of Abraham by his concubine Keturah (<a class=\"ref\" data-ref=\"Genesis 25:1\">Genesis 25:1–4</a>). They occupied territory east and southeast of Canaan, primarily in the region east of the Gulf of Aqaba and in the Sinai and Negev wilderness. Moses spent forty years among the Midianites after fleeing Egypt, married Zipporah the daughter of Jethro (Reuel), a Midianite priest (<a class=\"ref\" data-ref=\"Exodus 2:21\">Exodus 2:21</a>), and received his call at the burning bush in Midianite territory. Moses' father-in-law later provided the model for Israel's judicial administration (Exodus 18).</p><p>Despite this positive early connection, Midian became one of Israel's persistent adversaries. Midianite women participated in the apostasy at Baal-peor (Numbers 25), leading to a commanded campaign against Midian (Numbers 31). In the period of the judges, the Midianites oppressed Israel for seven years, devastating crops and livestock by annual raids, until Gideon was called by God and defeated them with three hundred men (Judges 6–7). The Midianite princes — Oreb, Zeeb, Zebah, and Zalmunna — were killed, and the victory became proverbial in later Scripture: \"Do to them as you did to Midian\" (<a class=\"ref\" data-ref=\"Psalms 83:9\">Psalm 83:9</a>); \"you have shattered them as on the day of Midian\" (<a class=\"ref\" data-ref=\"Isaiah 9:4\">Isaiah 9:4</a>).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "midianites"},
        "key_refs": ["Genesis 25:1", "Exodus 2:21", "Judges 6:1", "Psalms 83:9"]
    },
    "miscegenation": {
        "id": "miscegenation",
        "term": "Miscegenation",
        "category": "concepts",
        "intro": "<p>The biblical laws concerning intermarriage address a concern that is fundamentally religious rather than ethnic. Deuteronomy 7:3–4 explicitly forbids intermarriage with the seven Canaanite nations with a specific rationale: \"for they would turn away your sons from following me, to serve other gods.\" The same concern drives Abraham's and Isaac's instructions to their sons not to marry Canaanite women (<a class=\"ref\" data-ref=\"Genesis 24:3\">Genesis 24:3</a>; <a class=\"ref\" data-ref=\"Genesis 28:1\">Genesis 28:1</a>) and grounds Ezra's and Nehemiah's reforms requiring the dissolution of marriages to foreign women who worshipped other gods (Ezra 9–10; Nehemiah 13:23–27). The principle is covenant purity, not racial purity.</p><p>This reading is confirmed by the positive treatment of non-Israelite women who embraced Israel's God: Rahab of Jericho and Ruth the Moabite are both integrated into the Israelite community and appear in Jesus' genealogy (<a class=\"ref\" data-ref=\"Matthew 1:5\">Matthew 1:5</a>) without condemnation. Moses married a Cushite woman (<a class=\"ref\" data-ref=\"Numbers 12:1\">Numbers 12:1</a>), and Miriam and Aaron's criticism of this marriage was rebuked by God with Miriam's leprosy — God evidently did not share their concern. Paul's instruction not to be \"unequally yoked with unbelievers\" (<a class=\"ref\" data-ref=\"2 Corinthians 6:14\">2 Corinthians 6:14</a>) applies the same religious principle universally across ethnic lines, affirming that the concern is always about the compatibility of faith and covenant allegiance, not ethnic identity.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "miscegenation"},
        "key_refs": ["Genesis 24:3", "Genesis 28:1", "Deuteronomy 7:3", "Numbers 12:1", "Matthew 1:5"]
    },
    "prophetesses": {
        "id": "prophetesses",
        "term": "Prophetesses",
        "category": "people",
        "intro": "<p>Prophetesses — women who functioned in the prophetic role of receiving and communicating divine revelation — appear throughout Scripture as a recognized category alongside male prophets. Miriam, the sister of Moses, is the first explicitly named prophetess (<a class=\"ref\" data-ref=\"Exodus 15:20\">Exodus 15:20</a>), having led the women of Israel in song and worship after the crossing of the sea. Deborah served simultaneously as judge over Israel and as prophetess who delivered the LORD's word to Barak and accompanied him into battle (<a class=\"ref\" data-ref=\"Judges 4:4\">Judges 4:4</a>). Huldah was the prophetess whom the high priest Hilkiah and King Josiah's officials consulted when the Book of the Law was discovered; her oracle certified the authenticity of the scroll and set the course of Josiah's reform (<a class=\"ref\" data-ref=\"2 Kings 22:14\">2 Kings 22:14</a>).</p><p>In the New Testament, Anna the elderly widow prophesied in the temple at Jesus' presentation (<a class=\"ref\" data-ref=\"Luke 2:36\">Luke 2:36–38</a>), and Philip the evangelist's four daughters prophesied (<a class=\"ref\" data-ref=\"Acts 21:9\">Acts 21:9</a>). Most significantly, Peter at Pentecost cited Joel's prophecy — \"your sons and your daughters shall prophesy... your young men shall see visions\" (<a class=\"ref\" data-ref=\"Joel 2:28\">Joel 2:28</a>; <a class=\"ref\" data-ref=\"Acts 2:17\">Acts 2:17</a>) — as being fulfilled by the outpouring of the Spirit on men and women alike. The eschatological age of the Spirit is thus characterized in part by the extension of prophetic gifting across gender, fulfilling Moses' own wish that \"all the LORD's people were prophets\" (<a class=\"ref\" data-ref=\"Numbers 11:29\">Numbers 11:29</a>).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "prophetesses"},
        "key_refs": ["Exodus 15:20", "Judges 4:4", "2 Kings 22:14", "Joel 2:28", "Acts 2:17"]
    },
    "prosperity": {
        "id": "prosperity",
        "term": "Prosperity",
        "category": "concepts",
        "intro": "<p>Prosperity in Scripture encompasses both the material blessings of earthly life and the deeper flourishing that flows from covenant faithfulness — and the tension between these two senses generates one of the Bible's most persistent theological conversations. The Mosaic covenant explicitly linked obedience to material well-being: \"If you faithfully obey the voice of the LORD your God, blessed shall be the fruit of your womb and the fruit of your ground\" (<a class=\"ref\" data-ref=\"Deuteronomy 28:1\">Deuteronomy 28:1–4</a>). The Psalms associate the righteous person with fruitfulness: \"Blessed is everyone who fears the LORD, who walks in his ways... you shall eat the fruit of the labor of your hands; you shall be blessed\" (<a class=\"ref\" data-ref=\"Psalms 128:1\">Psalm 128:1–2</a>). Proverbs develops the theology of wisdom as the path to flourishing in both material and relational dimensions.</p><p>Yet Scripture equally complicates this picture. Job's suffering and Psalm 73's confession that \"I was envious of the arrogant when I saw the prosperity of the wicked\" testify that the righteous do not always flourish and the wicked often do — at least temporarily. Jesus warned that wealth could be a spiritual obstacle (<a class=\"ref\" data-ref=\"Matthew 19:24\">Matthew 19:24</a>) and that storing up earthly treasure is incompatible with trusting God (<a class=\"ref\" data-ref=\"Matthew 6:19\">Matthew 6:19–21</a>). Paul reframed prosperity entirely: \"I have learned, in whatever situation I am, to be content... I can do all things through him who strengthens me\" (<a class=\"ref\" data-ref=\"Philippians 4:11\">Philippians 4:11–13</a>). The New Testament consistently redirects the category of prosperity toward spiritual riches, generous giving, and the eternal inheritance of God's kingdom.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "prosperity"},
        "key_refs": ["Deuteronomy 28:1", "Psalms 128:1", "Matthew 19:24", "Philippians 4:11"]
    },
    "publicans": {
        "id": "publicans",
        "term": "Publicans",
        "category": "people",
        "intro": "<p>Publicans (Latin <em>publicani</em>; Greek <em>telonai</em>) were the tax collectors of the Roman imperial system in first-century Palestine, among the most despised figures in Jewish society. They were seen as collaborators with the Roman occupiers and as systematic extortionists: Roman tax law permitted collectors to levy amounts above the official rate and pocket the excess, making honest practice exceptional. Jewish tax collectors were considered doubly compromised — serving a Gentile power against their own people and regularly incurring ritual impurity through necessary contact with Gentiles. They were routinely grouped with \"sinners\" in rabbinic literature and in the Gospels as a category of the morally and ceremonially compromised.</p><p>Jesus' attitude toward publicans was one of the most provocative aspects of his ministry. He called Levi (Matthew) the tax collector to discipleship at the customs booth (<a class=\"ref\" data-ref=\"Matthew 9:9\">Matthew 9:9</a>) and then dined with \"many tax collectors and sinners\" at Levi's home, drawing Pharisaic criticism (<a class=\"ref\" data-ref=\"Matthew 9:11\">Matthew 9:11</a>). His parable of the Pharisee and the Tax Collector reversed the expected moral verdict, with the repentant tax collector departing justified (<a class=\"ref\" data-ref=\"Luke 18:13\">Luke 18:13–14</a>). The encounter with Zacchaeus the chief tax collector of Jericho — who climbed a sycamore tree to see Jesus and then pledged fourfold restitution — became the occasion for Jesus' declaration of his mission: \"The Son of Man came to seek and to save the lost\" (<a class=\"ref\" data-ref=\"Luke 19:10\">Luke 19:10</a>).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "publicans"},
        "key_refs": ["Matthew 9:9", "Matthew 9:11", "Luke 18:13", "Luke 19:10"]
    },
    "quickening": {
        "id": "quickening",
        "term": "Quickening",
        "category": "concepts",
        "intro": "<p>Quickening — the making alive of what was dead — is a recurring biblical theme encompassing both physical resurrection and the theological concept of spiritual regeneration. Hebrew and Greek words translated \"quicken,\" \"revive,\" or \"make alive\" (<em>hayah</em>; <em>zoopoieo</em>) appear across a range of contexts. The Psalmist petitions: \"You who have made me see many troubles and calamities will revive me again; from the depths of the earth you will bring me up again\" (<a class=\"ref\" data-ref=\"Psalms 71:20\">Psalm 71:20</a>). The communal lament uses the same language: \"Will you not revive us again, that your people may rejoice in you?\" (<a class=\"ref\" data-ref=\"Psalms 80:18\">Psalm 80:18</a>). Ezekiel's vision of the valley of dry bones (<a class=\"ref\" data-ref=\"Ezekiel 37:1\">Ezekiel 37</a>) is the Old Testament's fullest expression of God's power to quicken — to speak life into death on a corporate scale.</p><p>Paul uses quickening language to describe the foundational work of salvation: God \"gives life to the dead and calls into existence the things that do not exist\" (<a class=\"ref\" data-ref=\"Romans 4:17\">Romans 4:17</a>). The same resurrection power that raised Jesus is active in believers: \"if the Spirit of him who raised Jesus from the dead dwells in you, he who raised Christ Jesus from the dead will also give life to your mortal bodies through his Spirit\" (<a class=\"ref\" data-ref=\"Romans 8:11\">Romans 8:11</a>). Ephesians 2:1–5 provides the most concentrated statement: believers \"were dead in trespasses and sins\" but God \"made us alive together with Christ.\" The quickening of sinners — regeneration by the Holy Spirit — participates in the resurrection of Christ himself, making new birth not merely analogous to resurrection but an anticipation of it.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "quickening"},
        "key_refs": ["Psalms 71:20", "Psalms 80:18", "Romans 4:17", "Romans 8:11", "Ephesians 2:1"]
    },
    "rebekah-rebecca": {
        "id": "rebekah-rebecca",
        "term": "Rebekah",
        "category": "people",
        "intro": "<p>Rebekah (also spelled Rebecca) was the wife of Isaac and the mother of Jacob and Esau, the third of the four matriarchs of Israel. The daughter of Bethuel and sister of Laban, she was discovered by Abraham's servant at the well outside the city of Nahor in Aram-naharaim when he was sent to find a wife for Isaac (<a class=\"ref\" data-ref=\"Genesis 24:15\">Genesis 24:15–67</a>). Her willingness to water ten camels unprompted — the specific sign the servant had prayed for — and her immediate agreement to return with him identified her as God's choice. Isaac brought her into his mother Sarah's tent and \"he loved her\" (Genesis 24:67), one of the Old Testament's rare notes of spousal affection.</p><p>After twenty years of barrenness, Isaac prayed and Rebekah conceived twins who \"struggled together within her\" (<a class=\"ref\" data-ref=\"Genesis 25:22\">Genesis 25:22</a>). The divine oracle — \"The older shall serve the younger\" (Genesis 25:23) — set up the central tension of her family's story. Rebekah's favoritism for Jacob and her decisive role in engineering Jacob's deception of the blind Isaac to secure Esau's blessing (Genesis 27) make her one of Scripture's most complex figures: acting as the human instrument of fulfilling the divine oracle while employing morally troubling means. Paul in <a class=\"ref\" data-ref=\"Romans 9:10\">Romans 9:10–13</a> cites the pre-birth oracle to the twins as a paradigmatic example of divine election — \"though they were not yet born and had done nothing either good or bad\" — operating entirely independent of human merit or foresight, and thus illustrating the freedom and sovereignty of God's purpose.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "rebekah-rebecca"},
        "key_refs": ["Genesis 24:15", "Genesis 25:22", "Romans 9:10"]
    },
    "rebellion": {
        "id": "rebellion",
        "term": "Rebellion",
        "category": "concepts",
        "intro": "<p>Rebellion in Scripture denotes organized defiance against legitimate divine or human authority, treated among the most serious sins in the biblical moral taxonomy. First Samuel 15:23 equates it with the gravest occult offenses: \"Rebellion is as the sin of divination, and presumption is as iniquity and idolatry.\" The biblical narrative is punctuated by paradigmatic rebellions: Korah's organized challenge to Moses and Aaron's priestly authority (Numbers 16), Absalom's armed insurrection against his father David (<a class=\"ref\" data-ref=\"2 Samuel 15:1\">2 Samuel 15–18</a>), Jeroboam's secession from the house of David that permanently split the kingdom (1 Kings 12), and Israel's repeated rejection of the prophetic word as the most persistent form of covenant rebellion.</p><p>The ultimate dimension of rebellion in biblical theology is the orientation of the fallen human will against God as creator and covenant sovereign. Isaiah 1:2 opens with God's indictment: \"Children have I reared and brought up, but they have rebelled against me\" — framing Israel's entire history as prolonged filial disobedience. The New Testament identifies the \"spirit that is now at work in the sons of disobedience\" (<a class=\"ref\" data-ref=\"Ephesians 2:2\">Ephesians 2:2</a>) as the animating power of fallen autonomy, and the coming \"man of lawlessness\" as the eschatological climax of humanity's rebellion against God (<a class=\"ref\" data-ref=\"2 Thessalonians 2:3\">2 Thessalonians 2:3</a>). The antidote to rebellion in both Testaments is the submission of the will to God's covenant authority — \"the obedience of faith\" (<a class=\"ref\" data-ref=\"Romans 1:5\">Romans 1:5</a>) — which Christ himself modeled perfectly as the new and obedient Adam.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "rebellion"},
        "key_refs": ["1 Samuel 15:23", "2 Samuel 15:1", "Ephesians 2:2", "2 Thessalonians 2:3"]
    },
    "refining": {
        "id": "refining",
        "term": "Refining",
        "category": "concepts",
        "intro": "<p>Refining — the purging of impurities from metal through intense heat — is one of Scripture's most sustained and theologically productive metaphors for God's purifying work through trial, judgment, and discipline. In the smelting process, ore is heated until dross rises to the surface and is skimmed away, leaving pure metal. Isaiah 1:25 announces God's judgment on Jerusalem in these terms: \"I will turn my hand against you and will smelt away your dross as with lye and remove all your alloy.\" Malachi 3:2–3 pictures the coming of the Lord as a refiner's fire: \"he will sit as a refiner and purifier of silver, and he will purify the sons of Levi and refine them like gold and silver.\"</p><p>Zechariah 13:9 uses refining to describe the covenant relationship that emerges through judgment: \"I will put this third into the fire and refine them as one refines silver, and test them as gold is tested. They will call upon my name, and I will answer them. I will say, 'They are my people'; and they will say, 'The LORD is my God.'\" Isaiah 48:10 addresses Israel in exile: \"Behold, I have refined you, but not as silver; I have tried you in the furnace of affliction\" — assuring them that even the fires of exile serve a purifying divine purpose. In the New Testament, Peter applies the refining metaphor to the trials of faith: \"the tested genuineness of your faith — more precious than gold that perishes though it is tested by fire — may be found to result in praise and glory and honor at the revelation of Jesus Christ\" (<a class=\"ref\" data-ref=\"1 Peter 1:7\">1 Peter 1:7</a>).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "refining"},
        "key_refs": ["Isaiah 1:25", "Isaiah 48:10", "Malachi 3:2", "Zechariah 13:9", "1 Peter 1:7"]
    },
    "restitution": {
        "id": "restitution",
        "term": "Restitution",
        "category": "concepts",
        "intro": "<p>Restitution — making amends through the return or repayment of what has been wrongfully taken or damaged — is a foundational principle of Mosaic civil law. Exodus 22:1–4 establishes the basic framework: a thief who slaughtered or sold a stolen ox must repay five oxen; if the animal was found alive, two. Leviticus 24:18 establishes reciprocal proportionality — \"whoever kills an animal shall make it good, animal for animal.\" Exodus 21:30–36 addresses injuries and property damage with structured restitution requirements. The underlying principle is that sin against a neighbor creates a debt that must be materially satisfied before the broken relationship can be restored — a legal theology that treats the social fabric as real and its damage as measurable.</p><p>The New Testament's most vivid illustration of restitution is Zacchaeus's spontaneous pledge: \"Behold, Lord, the half of my goods I give to the poor. And if I have defrauded anyone of anything, I restore it fourfold\" (<a class=\"ref\" data-ref=\"Luke 19:8\">Luke 19:8</a>). The fourfold rate reflects Exodus 22:1, applied with extravagant generosity beyond legal requirement, and Jesus treats this pledge as evidence of genuine salvation: \"Today salvation has come to this house\" (<a class=\"ref\" data-ref=\"Luke 19:9\">Luke 19:9</a>). Paul's brief letter to Philemon enacts a logic of restitution: \"If he has wronged you at all, or owes you anything, charge that to my account... I will repay it\" (<a class=\"ref\" data-ref=\"Philemon 1:18\">Philemon 18–19</a>), positioning himself as surety for Onesimus in an enacted parable of substitutionary intercession.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "restitution"},
        "key_refs": ["Exodus 22:1", "Leviticus 24:18", "Luke 19:8", "Philemon 1:18"]
    },
    "sabbatic-year": {
        "id": "sabbatic-year",
        "term": "Sabbatic Year",
        "category": "concepts",
        "intro": "<p>The sabbatic year (Hebrew: <em>shemittah</em>) was the seventh-year agricultural sabbath commanded in the Mosaic law, in which the land of Israel was to rest uncultivated, debts were to be released, and Hebrew slaves were to be freed. <a class=\"ref\" data-ref=\"Leviticus 25:2\">Leviticus 25:2–7</a> mandates a complete year of rest for the land: \"you shall not sow your field or prune your vineyard... it shall be a year of solemn rest for the land.\" Whatever grew of itself could be consumed by landowner, servants, and sojourners alike, but no organized sowing or harvest was permitted. Deuteronomy 15:1–11 adds debt cancellation — at the end of every seven years every creditor must release what a neighbor owed — and the freeing of Hebrew servants after six years of service (<a class=\"ref\" data-ref=\"Exodus 21:2\">Exodus 21:2</a>).</p><p>The sabbatic year institutionalized a radical theology of ownership: the land ultimately belonged to God, and Israel held it in trust as tenants (Leviticus 25:23). This embedded a structural check against permanent poverty and hereditary bondage into Israelite society. The prophets linked Israel's failure to observe the sabbatic year to the duration of the Babylonian exile: <a class=\"ref\" data-ref=\"2 Chronicles 36:21\">2 Chronicles 36:21</a> states that the land \"enjoyed its Sabbaths\" during the seventy years of exile, accumulating the years Israel had withheld from it. Jesus' announcement of \"the acceptable year of the LORD\" in <a class=\"ref\" data-ref=\"Luke 4:19\">Luke 4:19</a> (citing Isaiah 61:2) employs sabbatic-year language to describe the messianic age of release and restoration he was inaugurating — liberation from the deeper bondage of sin, debt, and death.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "sabbatic-year"},
        "key_refs": ["Leviticus 25:2", "Deuteronomy 15:1", "Exodus 21:2", "2 Chronicles 36:21", "Luke 4:19"]
    },
    "sacrifices": {
        "id": "sacrifices",
        "term": "Sacrifices",
        "category": "concepts",
        "intro": "<p>Sacrifice in Scripture encompasses the wide range of offerings through which Israel drew near to God — burnt offerings, grain offerings, peace offerings, sin offerings, and guilt offerings — governed in detail by the Levitical code and performed at the tabernacle and later the temple by the Aaronic priesthood. These offerings expressed several theological functions simultaneously: the acknowledgment of God's sovereignty, the atoning removal of sin's guilt (<a class=\"ref\" data-ref=\"Leviticus 4:1\">Leviticus 4</a>), the expression of gratitude and worship, and the maintenance of covenant fellowship between God and his people. The foundational principle of blood sacrifice is explicit: \"the life of the flesh is in the blood, and I have given it for you on the altar to make atonement for your souls\" (<a class=\"ref\" data-ref=\"Leviticus 17:11\">Leviticus 17:11</a>).</p><p>The prophets and Psalms repeatedly warn against reducing sacrifice to ritual formalism divorced from ethical obedience: \"To do righteousness and justice is more acceptable to the LORD than sacrifice\" (Proverbs 21:3); \"I desire steadfast love and not sacrifice\" (Hosea 6:6, cited twice by Jesus in <a class=\"ref\" data-ref=\"Matthew 9:13\">Matthew 9:13</a> and 12:7). The New Testament interprets the entire Levitical system as foreshadowing the atoning death of Christ — \"the Lamb of God, who takes away the sin of the world\" (<a class=\"ref\" data-ref=\"John 1:29\">John 1:29</a>). Hebrews argues that Jesus' sacrifice was \"once for all\" and permanently superseded the repeating animal offerings (<a class=\"ref\" data-ref=\"Hebrews 9:12\">Hebrews 9–10</a>). Paul translates the sacrificial vocabulary into Christian ethics: \"present your bodies as a living sacrifice, holy and acceptable to God, which is your spiritual worship\" (<a class=\"ref\" data-ref=\"Romans 12:1\">Romans 12:1</a>).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "sacrifices"},
        "key_refs": ["Leviticus 17:11", "Matthew 9:13", "John 1:29", "Romans 12:1", "Hebrews 9:12"]
    },
    "security": {
        "id": "security",
        "term": "Security",
        "category": "concepts",
        "intro": "<p>Security in Scripture is a recurring theme that the Bible consistently redirects from earthly foundations to God alone. The danger of false security — trusting in wealth, military power, political alliances, or the mere possession of religious status — is a persistent target of prophetic critique. Psalm 10:4 characterizes the wicked by their self-sufficient arrogance: in the pride of his face the wicked does not seek God. Isaiah 28:15 indicts Jerusalem for making \"a covenant with death\" — seeking security through alliance with Egypt — which the prophet unmasks as \"a refuge of lies.\" Job 29:18 captures the deceptive confidence of prosperity: \"Then I thought, 'I shall die in my nest, and I shall multiply my days as the sand.'\"</p><p>True security in Scripture flows exclusively from covenant relationship with God: \"The name of the LORD is a strong tower; the righteous man runs into it and is safe\" (<a class=\"ref\" data-ref=\"Proverbs 18:10\">Proverbs 18:10</a>). Paul's declaration in Romans 8:38–39 — \"neither death nor life... nor anything else in all creation, will be able to separate us from the love of God in Christ Jesus our Lord\" (<a class=\"ref\" data-ref=\"Romans 8:38\">Romans 8:38–39</a>) — is the New Testament's fullest statement of genuine security: not the absence of danger or suffering but the assurance that God's love in Christ is indestructible. Hebrews 6:18–19 grounds Christian security in the immutability of God's promise and oath: \"we who have fled for refuge might have strong encouragement to hold fast to the hope set before us... a sure and steadfast anchor of the soul.\"</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "security"},
        "key_refs": ["Proverbs 18:10", "Isaiah 28:15", "Romans 8:38", "Hebrews 6:18"]
    },
    "self-condemnation": {
        "id": "self-condemnation",
        "term": "Self-Condemnation",
        "category": "concepts",
        "intro": "<p>Self-condemnation in Scripture refers to the recognition by one's own conscience of guilt before God — the interior verdict that aligns with divine judgment, often arising unbidden in moments of moral clarity or crisis. The phenomenon appears across the biblical narrative: David's conscience \"struck him\" after he numbered the people and he confessed, \"I have sinned greatly in what I have done\" (<a class=\"ref\" data-ref=\"2 Samuel 24:10\">2 Samuel 24:10</a>). Proverbs 5:12–14 gives voice to the self-condemnation of one who rejected wisdom: \"How I hated discipline, and my heart despised reproof! I did not listen to the voice of my teachers.\" Job's searching self-scrutiny throughout the dialogue reflects a man wrestling with conscience before God: \"If I have sinned, what do I do to you, you watcher of mankind?\" (<a class=\"ref\" data-ref=\"Job 7:20\">Job 7:20</a>).</p><p>In the New Testament self-condemnation appears most starkly in Judas Iscariot's tortured acknowledgment: \"I have sinned by betraying innocent blood\" (<a class=\"ref\" data-ref=\"Matthew 27:4\">Matthew 27:4</a>) — a genuine recognition that led, however, not to repentance but to despair. The prodigal son's return includes precisely the kind of self-condemnation that leads to restoration: \"Father, I have sinned against heaven and before you\" (<a class=\"ref\" data-ref=\"Luke 15:18\">Luke 15:18</a>). John's first letter addresses the condemning conscience with grace: \"whenever our heart condemns us, God is greater than our heart, and he knows everything\" (<a class=\"ref\" data-ref=\"1 John 3:20\">1 John 3:20</a>) — affirming both the reality of conscience's verdict and the greater reality of God's forgiveness in Christ that transcends it.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "self-condemnation"},
        "key_refs": ["2 Samuel 24:10", "Matthew 27:4", "Luke 15:18", "1 John 3:20"]
    },
    "self-exaltation": {
        "id": "self-exaltation",
        "term": "Self-Exaltation",
        "category": "concepts",
        "intro": "<p>Self-exaltation — the pride that elevates oneself above one's proper station before God and others — is uniformly condemned in Scripture as the disposition most fundamentally at odds with covenant humility and the character of God. Proverbs 16:18 states the governing principle: \"Pride goes before destruction, and a haughty spirit before a fall.\" Ezekiel 31:10–14 employs the image of a great cedar of Lebanon — majestic, towering above all trees, a shelter for the nations — brought down by God because \"its heart was proud of its height.\" Isaiah 14 uses the self-exaltation of the king of Babylon as a type of the anti-divine rebellion: \"You said in your heart, 'I will ascend to heaven; above the stars of God I will set my throne on high'\" — met by the divine reversal into Sheol.</p><p>Jesus makes the reversal of self-exaltation a recurring teaching: \"For everyone who exalts himself will be humbled, and he who humbles himself will be exalted\" (<a class=\"ref\" data-ref=\"Luke 14:11\">Luke 14:11</a>; cf. 18:14; <a class=\"ref\" data-ref=\"Matthew 23:12\">Matthew 23:12</a>), enacted narratively in the parable of the Pharisee and the Tax Collector. James 4:6 and <a class=\"ref\" data-ref=\"1 Peter 5:5\">1 Peter 5:5</a> both quote Proverbs 3:34 — \"God opposes the proud but gives grace to the humble\" — as the governing principle of Christian community life. The supreme divine counter-movement to self-exaltation is the incarnation itself: Christ, who was in the form of God, \"did not count equality with God a thing to be grasped, but emptied himself, taking the form of a servant... therefore God has highly exalted him\" (<a class=\"ref\" data-ref=\"Philippians 2:6\">Philippians 2:6–9</a>).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "self-exaltation"},
        "key_refs": ["Proverbs 16:18", "Luke 14:11", "Matthew 23:12", "Philippians 2:6", "1 Peter 5:5"]
    },
    "self-examination": {
        "id": "self-examination",
        "term": "Self-Examination",
        "category": "concepts",
        "intro": "<p>Self-examination in Scripture is the spiritually disciplined practice of honest interior assessment before God — the willingness to search one's own heart for sin, self-deception, and spiritual drifting, rather than projecting blame outward or resting in complacent routine. The Psalms model this practice with directness: \"Examine me, O LORD, and prove me; try my heart and my mind\" (<a class=\"ref\" data-ref=\"Psalms 26:2\">Psalm 26:2</a>). David's petition in Psalm 19:12 — \"Who can discern his errors? Declare me innocent from hidden faults\" — acknowledges the depth of self-opacity that genuine self-examination must confront. \"Search me, O God, and know my heart! Try me and know my thoughts! And see if there be any grievous way in me\" (<a class=\"ref\" data-ref=\"Psalms 139:23\">Psalm 139:23–24</a>) is perhaps the most comprehensive biblical prayer of self-examination.</p><p>The most concentrated New Testament summons to self-examination is Paul's instruction regarding the Lord's Supper: \"Let a person examine himself, then, and so eat of the bread and drink of the cup. For anyone who eats and drinks without discerning the body eats and drinks judgment on himself\" (<a class=\"ref\" data-ref=\"1 Corinthians 11:28\">1 Corinthians 11:28–29</a>). Self-examination is the prerequisite for worthy participation in the covenant meal. Paul similarly urges the Corinthians: \"Examine yourselves, to see whether you are in the faith. Test yourselves\" (<a class=\"ref\" data-ref=\"2 Corinthians 13:5\">2 Corinthians 13:5</a>). Lamentations 3:40 voices the communal dimension: \"Let us test and examine our ways, and return to the LORD\" — the practice of self-examination as the instrument of genuine repentance and covenant renewal, not introspection for its own sake.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "self-examination"},
        "key_refs": ["Psalms 26:2", "Psalms 139:23", "1 Corinthians 11:28", "2 Corinthians 13:5"]
    },
    "seraphim-seraphs": {
        "id": "seraphim-seraphs",
        "term": "Seraphim",
        "category": "concepts",
        "intro": "<p>The seraphim (singular: seraph; Hebrew <em>saraph</em>, \"burning one\") are celestial beings appearing in Isaiah's vision of the heavenly throne room, the only extended description of them in Scripture: \"I saw the Lord sitting upon a throne, high and lifted up... Above him stood the seraphim. Each had six wings: with two he covered his face, and with two he covered his feet, and with two he flew\" (<a class=\"ref\" data-ref=\"Isaiah 6:2\">Isaiah 6:2</a>). Two seraphim called to one another: \"Holy, holy, holy is the LORD of hosts; the whole earth is full of his glory\" — the trisagion that became central to both Jewish and Christian liturgy. One seraph then flew to Isaiah with a burning coal from the altar, touched his lips, and declared his guilt removed and his sin atoned for (<a class=\"ref\" data-ref=\"Isaiah 6:6\">Isaiah 6:6–7</a>), enabling his prophetic commission.</p><p>The seraphim in this singular description are characterized by their burning holiness — their very name — their posture of perpetual worship before God's throne, and the paradox that even they must cover their faces and feet in the divine presence, indicating that the vision of God's full glory exceeds even the capacity of the highest angelic beings. Their proclamation — \"the whole earth is full of his glory\" — establishes the theological vision grounding Isaiah's entire prophetic ministry: God's holiness as the comprehensive reality that fills creation yet exceeds all creaturely comprehension. John's Gospel interprets Isaiah 6:9–10 as a vision of Christ's glory (<a class=\"ref\" data-ref=\"John 12:41\">John 12:41</a>), reading the seraphim's trisagion as a witness to the pre-incarnate Son.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "seraphim-seraphs"},
        "key_refs": ["Isaiah 6:2", "Isaiah 6:6", "John 12:41"]
    },
    "shushan-susa": {
        "id": "shushan-susa",
        "term": "Shushan",
        "category": "places",
        "intro": "<p>Shushan (Persian: Susa) was the ancient capital of Elam and one of the royal residences of the Persian Achaemenid Empire, located in southwestern Iran at the confluence of three rivers (the Kerkheh, Dez, and Shaur). In its Persian heyday Susa served as the winter palace of the Persian kings — Persepolis functioned as the ceremonial capital and Ecbatana as the summer residence. The city's great citadel (<em>apadana</em>), where the king held audience from an elevated throne, provides the historical setting for several major narrative events in the biblical books composed against the Persian backdrop.</p><p>Shushan features prominently in the books of Esther, Nehemiah, and Daniel. The book of Esther unfolds entirely within the palace complex: the deposition of Vashti, the selection of Esther, Haman's plot, and the Jewish triumph all take place in \"Shushan the palace\" (<a class=\"ref\" data-ref=\"Esther 1:2\">Esther 1:2–3</a>; <a class=\"ref\" data-ref=\"Esther 8:15\">8:15</a>). Nehemiah was serving as cupbearer to Artaxerxes I in Shushan when he received the news of Jerusalem's desolation that moved him to pray and act (<a class=\"ref\" data-ref=\"Nehemiah 1:1\">Nehemiah 1:1</a>). Daniel received his vision of the ram and the goat \"in Shushan the citadel\" in the province of Elam (<a class=\"ref\" data-ref=\"Daniel 8:2\">Daniel 8:2</a>). Archaeological excavation of the site since the nineteenth century has uncovered the palace complex described in Esther and cuneiform inscriptions from Darius I, providing substantial corroboration of the Persian court setting of these narratives.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "shushan-susa"},
        "key_refs": ["Esther 1:2", "Esther 8:15", "Nehemiah 1:1", "Daniel 8:2"]
    },
    "sobriety": {
        "id": "sobriety",
        "term": "Sobriety",
        "category": "concepts",
        "intro": "<p>Sobriety in Scripture encompasses both the literal avoidance of intoxication and the broader spiritual quality of clear-headedness, alertness, and self-control in the face of the world's allurements and dangers. The Greek words <em>sophrosyne</em> (temperance, self-control) and <em>nepho</em> (to be sober, watchful) appear repeatedly in the New Testament's ethical teaching as essential virtues for Christian life. The Pastoral Epistles list sobriety among the required qualities for church elders and deacons (<a class=\"ref\" data-ref=\"1 Timothy 3:2\">1 Timothy 3:2</a>, 11; Titus 1:8; 2:2), signaling that sober clarity of judgment is foundational to trusted leadership in the community.</p><p>The eschatological urgency of sobriety is especially prominent in the apostolic letters. \"Be sober-minded; be watchful. Your adversary the devil prowls around like a roaring lion, seeking someone to devour\" (<a class=\"ref\" data-ref=\"1 Peter 5:8\">1 Peter 5:8</a>). The awareness that the return of Christ and the consummation of history are real future events gives sobriety its pressing character: \"let us be sober, having put on the breastplate of faith and love, and for a helmet the hope of salvation\" (<a class=\"ref\" data-ref=\"1 Thessalonians 5:8\">1 Thessalonians 5:8</a>). Titus 2:12 grounds sobriety in the grace of God itself: it is divine grace that \"trains us to renounce ungodliness and worldly passions, and to live self-controlled, upright, and godly lives in the present age.\" Sobriety is thus not mere abstinence but the alert, grace-formed posture of the believer who takes seriously both the perils of the present age and the hope of the age to come.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "sobriety"},
        "key_refs": ["1 Peter 5:8", "1 Thessalonians 5:8", "Titus 2:12", "1 Timothy 3:2"]
    },
    "sower": {
        "id": "sower",
        "term": "Sower",
        "category": "concepts",
        "intro": "<p>The sower is primarily known in the New Testament through the Parable of the Sower — the first and most foundational of Jesus' parables, appearing in all three Synoptic Gospels (<a class=\"ref\" data-ref=\"Matthew 13:3\">Matthew 13:3–8</a>; <a class=\"ref\" data-ref=\"Mark 4:3\">Mark 4:3–20</a>; <a class=\"ref\" data-ref=\"Luke 8:5\">Luke 8:5–8</a>) and provided with Jesus' own detailed allegorical explanation. A sower goes out and broadcasts seed, which falls on four types of ground: the hardened path (eaten by birds), rocky soil (sprouts but withers in the sun), thorny ground (choked), and good soil (yielding thirty-, sixty-, and a hundredfold). Jesus interprets the seed as \"the word of the kingdom\" and the four soils as conditions of the human heart — ranging from complete incomprehension to fruitful reception.</p><p>The agricultural reality behind the parable reflects ancient Palestinian farming practice, in which broadcasting seed before plowing was common, resulting in seed landing on varied terrain. Ecclesiastes 11:4 captures the farmer's necessary confidence: \"Whoever watches the wind will not sow, and whoever looks at the clouds will not reap\" — urging action despite uncertainty about outcome. Isaiah 28:24–29 uses the sower's varied techniques (plowing, harrowing, planting different crops in different rows) to illustrate God's varied and instructive dealings with his people. In the New Testament the sower of the parable is most naturally identified with Jesus himself — and by extension with any bearer of the gospel word — whose proclamation goes out broadly and meets every conceivable response, with the extraordinary final yield testifying to the ultimate fruitfulness of the kingdom despite the apparent waste of so much seed on unresponsive soil.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "sower"},
        "key_refs": ["Matthew 13:3", "Mark 4:3", "Luke 8:5", "Ecclesiastes 11:4"]
    },
    "sprinkling": {
        "id": "sprinkling",
        "term": "Sprinkling",
        "category": "concepts",
        "intro": "<p>Sprinkling in the Old Testament was a ritual act performed with blood, water, or oil as part of purification, consecration, and atonement rites in the Levitical system. Blood was sprinkled on the altar (<a class=\"ref\" data-ref=\"Leviticus 1:5\">Leviticus 1:5</a>), on persons and objects being consecrated, and on the mercy seat in the Most Holy Place on the Day of Atonement (<a class=\"ref\" data-ref=\"Leviticus 16:14\">Leviticus 16:14–15</a>). Water mixed with the ashes of a red heifer was sprinkled on those who had become ritually impure through contact with a corpse (<a class=\"ref\" data-ref=\"Numbers 19:18\">Numbers 19:18–19</a>), effecting ritual cleansing. Moses sprinkled the blood of the covenant sacrifice on the altar and on the people at the ratification of the Sinai covenant: \"Behold the blood of the covenant that the LORD has made with you\" (<a class=\"ref\" data-ref=\"Exodus 24:8\">Exodus 24:8</a>).</p><p>Hebrews makes the most sustained theological use of the sprinkling imagery: \"if the blood of goats and bulls, and the sprinkling of defiled persons with the ashes of a heifer, sanctify for the purification of the flesh, how much more will the blood of Christ... purify our conscience from dead works to serve the living God\" (<a class=\"ref\" data-ref=\"Hebrews 9:13\">Hebrews 9:13–14</a>). Peter addresses believers as those chosen \"for obedience to Jesus Christ and for sprinkling with his blood\" (<a class=\"ref\" data-ref=\"1 Peter 1:2\">1 Peter 1:2</a>). Isaiah's Servant Song anticipates that the Servant \"shall sprinkle many nations\" (<a class=\"ref\" data-ref=\"Isaiah 52:15\">Isaiah 52:15</a>), read in the New Testament as the atonement's reach extending to the Gentile world. Sprinkling thus stands as a ritually concrete image whose full theological significance is disclosed only in the atoning death of Christ.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "sprinkling"},
        "key_refs": ["Leviticus 16:14", "Exodus 24:8", "Hebrews 9:13", "1 Peter 1:2", "Isaiah 52:15"]
    },
    "standard": {
        "id": "standard",
        "term": "Standard",
        "category": "concepts",
        "intro": "<p>A standard or banner (Hebrew: <em>degel</em> for tribal standards; <em>nes</em> for signal poles or national banners) served in the ancient world as a rallying point for troops, a means of military identification, and a signal visible from a great distance. Numbers 1:52 and 2:2 regulate the arrangement of Israel's tribal camps around the tabernacle \"each by his own standard, with the banners of their fathers' houses\" — the twelve tribes organized into four groups of three, each with a distinctive ensign under which they camped and marched in the wilderness. The standard thus organized the covenant community around the central sanctuary, reflecting the theological ordering of Israel's life around God's dwelling.</p><p>The prophetic use of the standard is among the most theologically significant. Isaiah repeatedly speaks of the LORD raising a \"signal\" (<em>nes</em>) for the nations: \"He will raise a signal for the nations and will assemble the banished of Israel, and gather the dispersed of Judah from the four corners of the earth\" (<a class=\"ref\" data-ref=\"Isaiah 11:12\">Isaiah 11:12</a>). Isaiah 49:22 and 62:10 develop the same image of a banner lifted to draw the nations into the eschatological ingathering. Psalm 20:5 uses the raising of banners as an image of covenant victory: \"May we shout for joy over your salvation, and in the name of our God set up our banners.\" Song of Solomon 6:4 and 6:10 — \"awesome as an army with banners\" — use the military standard's impressiveness as a simile for the beauty of the beloved. In Christian interpretation the cross has been widely understood as the ultimate fulfillment of Isaiah's \"signal\" raised for all nations.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "standard"},
        "key_refs": ["Numbers 1:52", "Isaiah 11:12", "Isaiah 49:22", "Psalms 20:5"]
    },
    "substitution": {
        "id": "substitution",
        "term": "Substitution",
        "category": "concepts",
        "intro": "<p>Substitution — the principle that one person or animal may bear penalty, guilt, or responsibility on behalf of another — is woven into the fabric of Levitical ritual and reaches its theological climax in the atoning death of Christ. The Day of Atonement ritual of the scapegoat expressed substitution most vividly: Aaron \"shall lay both his hands on the head of the live goat, and confess over it all the iniquities of the people of Israel... putting them on the head of the goat, and sending it away into the wilderness\" (<a class=\"ref\" data-ref=\"Leviticus 16:21\">Leviticus 16:21–22</a>). The slaughtered goat's blood was brought into the Most Holy Place as a sin offering; the living goat carried the sins into the wilderness. Together they enacted the transfer of guilt from the covenant community to a substitute.</p><p>The burnt offering system assumed substitution at its foundation: <a class=\"ref\" data-ref=\"Leviticus 1:4\">Leviticus 1:4</a> states that the worshiper \"shall lay his hand on the head of the burnt offering, and it shall be accepted for him to make atonement for him.\" The New Testament announces the definitive substitution in the language of Isaiah 53:5–6: \"He was pierced for our transgressions; he was crushed for our iniquities... and the LORD has laid on him the iniquity of us all.\" Paul makes the substitutionary logic explicit in its most concentrated formulation: \"God made him who had no sin to be sin for us, so that in him we might become the righteousness of God\" (<a class=\"ref\" data-ref=\"2 Corinthians 5:21\">2 Corinthians 5:21</a>). The doctrine of penal substitutionary atonement, grounded in these texts, became the organizing center of Protestant soteriology and the subject of much contemporary theological discussion.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "substitution"},
        "key_refs": ["Leviticus 16:21", "Leviticus 1:4", "Isaiah 53:5", "2 Corinthians 5:21"]
    },
    "tongues-the-gift": {
        "id": "tongues-the-gift",
        "term": "Tongues, Gift of",
        "category": "concepts",
        "intro": "<p>The gift of tongues (<em>glossolalia</em>, from Greek <em>glossa</em>, \"tongue\") refers to a supernatural capacity to speak in languages — whether known human languages or what Paul calls \"tongues of angels\" (<a class=\"ref\" data-ref=\"1 Corinthians 13:1\">1 Corinthians 13:1</a>) — granted by the Holy Spirit as one of the spiritual gifts for the edification of the church and the witness to the nations. The gift first appeared dramatically at Pentecost: the disciples \"began to speak in other tongues as the Spirit gave them utterance,\" with each listener in the Jerusalem crowd hearing the proclamation in their own native language (<a class=\"ref\" data-ref=\"Acts 2:4\">Acts 2:4</a>). Luke presents this as a reversal of the Babel scattering: where languages had been divided to disperse humanity, the Spirit now bridges languages to gather a new humanity in Christ.</p><p>Paul's most extensive treatment appears in <a class=\"ref\" data-ref=\"1 Corinthians 12:10\">1 Corinthians 12–14</a>, where he affirms the gift while governing its exercise. Uninterpreted tongues in the gathered assembly are of limited benefit: \"if I come to you speaking in tongues, how will I benefit you unless I bring you some revelation or knowledge or prophecy or teaching?\" (1 Corinthians 14:6). He therefore requires interpretation for congregational use (14:27–28) and prioritizes prophecy as more directly edifying. Paul affirms personal use of tongues — \"I speak in tongues more than all of you\" (14:18) — while insisting that ordered, intelligible worship governs the assembly. The question of whether the gift continues in the post-apostolic church (the cessationist position) or remains available to all believers (the continuationist position) has been a defining division in Protestant Christianity since the Reformation and particularly since the rise of Pentecostalism in the twentieth century.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": None, "smith": None, "isbe": None, "nave": "tongues-the-gift"},
        "key_refs": ["Acts 2:4", "1 Corinthians 12:10", "1 Corinthians 13:1", "1 Corinthians 14:6"]
    },
}


def main():
    written = 0
    skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP {__doc__.split(chr(10))[1].strip()}: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
