"""
BP Article Synthesis — c4: Corinthians, Second Epistle to the → Cyrus
Covers Easton entries: Corinthians, Second Epistle through Cyrus (53 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Script: scripts/bp-c4.py
Run: python3 scripts/bp-c4.py
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
    "corinthians-second-epistle-to-the": {
        "id": "corinthians-second-epistle-to-the",
        "term": "Corinthians, Second Epistle to the",
        "category": "concepts",
        "intro": "<p>Second Corinthians is one of Paul's most personally revealing letters, written shortly after First Corinthians, probably in A.D. 55–56 from Macedonia. Paul composed it following the painful reception of the first letter and a subsequent distressing visit, after Titus brought news that the Corinthian church had largely responded with repentance. The letter contains Paul's most extensive defense of his apostolic ministry against opponents who questioned his credentials, and its central section (chapters 8–9) contains the most theologically developed appeal for generous giving in the New Testament.</p><p>The letter's distinctive contributions include the theology of the new covenant ministry as surpassing the Mosaic covenant in glory (chapters 3–4), the theology of resurrection and the groaning of the present body for the heavenly dwelling (chapter 5), and Paul's paradoxical account of apostolic weakness as the vehicle of divine power (chapters 11–12). The famous catalog of sufferings in 11:23–29 and the vision of the third heaven in 12:1–10 make Second Corinthians the closest thing in the New Testament to a personal spiritual autobiography of the apostle Paul.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "corinthians-second-epistle-to-the", "smith": "corinthians-second-epistle-to-the", "isbe": "corinthians-second-epistle-to-the"},
        "key_refs": ["2 Corinthians 1:8", "2 Corinthians 2:12", "2 Corinthians 7:6", "2 Corinthians 12:9"]
    },
    "cormorant": {
        "id": "cormorant",
        "term": "Cormorant",
        "category": "concepts",
        "intro": "<p>Cormorant translates the Hebrew <em>shalak</em> (plunging or darting down) in Leviticus 11:17 and Deuteronomy 14:17, where it appears in the list of unclean birds. The diving behavior implied by the root word suits the cormorant, a large coastal bird that plunges into water to catch fish. However, the identification is uncertain — the same Hebrew term may refer to another water bird such as the fisher owl or gannet. The Septuagint uses a different identification than the King James translators.</p><p>The cormorant also appears in prophetic contexts as a bird of desolation. Isaiah 34:11 and Zephaniah 2:14 describe desolated cities and ruins inhabited by the cormorant (or pelican in some versions) alongside the owl and bittern — birds of solitary waste places whose presence marks the complete abandonment of what was once a thriving human settlement. Psalm 102:6 uses a similar bird as an image of the psalmist's own desolation and loneliness in affliction.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cormorant", "smith": "cormorant", "isbe": "cormorant"},
        "key_refs": ["Leviticus 11:17", "Isaiah 34:11", "Zephaniah 2:14", "Psalms 102:6"]
    },
    "corn": {
        "id": "corn",
        "term": "Corn",
        "category": "concepts",
        "intro": "<p>Corn in the King James Bible translates several Hebrew and Greek words referring to cultivated grain crops rather than the New World maize. The primary Hebrew term <em>dagan</em> (Genesis 27:28; Numbers 18:27; Deuteronomy 28:51) is a collective term for grain in general — wheat, barley, and millet — which formed the dietary staple of ancient Israel. Other Hebrew terms include <em>bar</em> (threshed grain, Genesis 41:35), <em>shever</em> (grain for purchase, Genesis 42:1), and <em>karmel</em> (fresh grain, Leviticus 23:14).</p><p>Grain production and storage was central to ancient Near Eastern economies, and the biblical narrative returns repeatedly to grain in contexts of blessing, famine, tribute, and provision. Joseph's management of Egyptian grain reserves during the famine (Genesis 41–42) is the most extended biblical treatment. The New Covenant use of grain is primarily symbolic: Jesus describes himself as the grain of wheat that must fall into the earth and die to bear much fruit (John 12:24), and grain provides the substance of the Eucharistic bread instituted at the Last Supper.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "corn", "smith": "corn", "isbe": "corn"},
        "key_refs": ["Genesis 27:28", "Deuteronomy 28:51", "John 12:24"]
    },
    "cornelius": {
        "id": "cornelius",
        "term": "Cornelius",
        "category": "people",
        "intro": "<p>Cornelius (meaning <em>of a horn</em>) was a Roman centurion of the Italian band stationed at Caesarea Maritima, whose conversion is narrated in Acts 10 as a watershed event in the early church's understanding of its Gentile mission. He is described as a devout man who feared God with all his household, gave generously to the Jewish poor, and prayed to God continually. An angel directed him to send for Simon Peter at Joppa, while Peter simultaneously received a vision of a sheet bearing clean and unclean animals and the divine command to eat — a vision he came to understand as signifying that no person should be called common or unclean.</p><p>When Peter arrived at Cornelius's house and began to speak, the Holy Spirit fell on all who heard the word before they were even baptized — a development Peter cited at the Jerusalem Council (Acts 11; 15) as decisive proof that God had granted Gentiles repentance unto life. The conversion of Cornelius effectively opened the door for the Gentile mission that Paul would carry to the ends of the Roman Empire. His household baptism is frequently cited in discussions of household and infant baptism.</p>",
        "hitchcock_meaning": "of a horn",
        "source_ids": {"easton": "cornelius", "smith": "cornelius", "isbe": "cornelius"},
        "key_refs": ["Acts 10:1", "Acts 10:44", "Acts 11:18"]
    },
    "corner": {
        "id": "corner",
        "term": "Corner",
        "category": "concepts",
        "intro": "<p>Corner in Scripture carries both literal architectural meaning and extensive figurative and theological significance. Literally, corners defined the angles of buildings (Job 1:19) and streets (Proverbs 7:8), and the corners of fields were to be left unharvested for the poor and the stranger (Leviticus 19:9; 23:22) — a provision for gleaning that Ruth exercised at Boaz's field. The Israelites were prohibited from cutting the corners of their beards (Leviticus 19:27), likely a practice associated with mourning or pagan rites.</p><p>The most theologically significant use is the <em>cornerstone</em> or <em>head of the corner</em> (Hebrew <em>rosh pinnah</em>). Psalm 118:22 — <em>the stone which the builders rejected is become the head of the corner</em> — is quoted by Jesus as fulfilled in himself (Matthew 21:42; Mark 12:10; Luke 20:17) and cited by Peter before the Sanhedrin (Acts 4:11) and in his first epistle (1 Peter 2:7). Isaiah 28:16 prophesies God's laying of a tested, precious cornerstone in Zion, which Paul and Peter apply to Christ as the foundation of God's new temple composed of living stones.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "corner", "smith": "corner", "isbe": "corner"},
        "key_refs": ["Leviticus 19:9", "Psalms 118:22", "Matthew 21:42", "1 Peter 2:7"]
    },
    "cornet": {
        "id": "cornet",
        "term": "Cornet",
        "category": "concepts",
        "intro": "<p>Cornet translates the Hebrew <em>shophar</em>, the ram's horn used as Israel's primary signaling and ceremonial instrument. The name <em>shophar</em> is related to a root meaning brightness, referring to the clarity and carrying power of its sound. It was the instrument used to signal assembly, to sound the alarm of war, to proclaim the jubilee year, and to accompany worship — its blast at Sinai accompanied the divine presence (Exodus 19:16) and its sound opened the gates of the New Year on the Feast of Trumpets.</p><p>The shophar appears frequently in the Psalms as an instrument of praise (Psalm 98:6; 150:3) and in the prophets as a signal of warning and judgment. Hosea 5:8 calls for the shophar to sound the alarm at Gibeah. In the New Testament, the trumpet image becomes eschatological: the last trump signals the resurrection and transformation of believers (1 Corinthians 15:52), and seven trumpet blasts structure the judgments of Revelation 8–11. Daniel 3:5 and 3:7 list a different term translated cornet in the KJV among the instruments commanded to signal worship of Nebuchadnezzar's gold image.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cornet", "smith": "cornet", "isbe": "cornet"},
        "key_refs": ["1 Chronicles 15:28", "Psalms 98:6", "Hosea 5:8", "Daniel 3:5"]
    },
    "cotes": {
        "id": "cotes",
        "term": "Cotes",
        "category": "concepts",
        "intro": "<p>Cotes (also spelled <em>coates</em>) refers to pens or enclosures for flocks, mentioned in 2 Chronicles 32:28 as part of Hezekiah's preparation of storehouses and provisions during his reign — he provided <em>stalls for all manner of beasts, and cotes for flocks</em>. The term denotes sheltered enclosures or folds where sheep and other livestock were protected at night, equivalent to what is elsewhere called a fold or sheepfold in the biblical text.</p><p>Animal husbandry was central to the Israelite economy, and the maintenance of adequate sheltering for flocks was a practical concern. Hezekiah's construction of cotes reflects the prosperity and careful administration associated with his reign in Chronicles, which portrays him as a model king who accumulated wealth and organized provisions systematically in preparation for the Assyrian threat.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cotes", "isbe": "cotes"},
        "key_refs": ["2 Chronicles 32:28"]
    },
    "cottage": {
        "id": "cottage",
        "term": "Cottage",
        "category": "concepts",
        "intro": "<p>Cottage in the King James Bible translates two different Hebrew words referring to temporary shelters. The first (<em>sukkah</em>) appears in Isaiah 1:8 — <em>the daughter of Zion is left as a cottage in a vineyard, as a lodge in a garden of cucumbers</em> — describing a temporary booth or hut erected in a vineyard or field during harvest season to shelter the watchmen, then abandoned after harvest. Job 27:18 uses the same image: the house of the wicked is like a booth and like a hut the keeper makes.</p><p>The second Hebrew word (<em>melunah</em>, Isaiah 24:20) refers to a hammock or swinging hut, used in the vivid picture of the earth reeling like a drunkard and being moved like a cottage — a temporary dwelling so insubstantial it can be blown away. Zephaniah 2:6 uses a related term for the pastures and meadows of the seacoast. Together these images reflect the temporary and fragile nature of human habitation in contrast to the stability of the divine presence.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cottage", "isbe": "cottage"},
        "key_refs": ["Isaiah 1:8", "Job 27:18", "Isaiah 24:20"]
    },
    "couch": {
        "id": "couch",
        "term": "Couch",
        "category": "concepts",
        "intro": "<p>Couch in Scripture refers to a bed, divan, or reclining seat used for sleep, rest, or at meals. The Hebrew terms rendered couch include <em>mishkab</em> (lying down place, Genesis 49:4; Job 7:13), <em>yatsa</em> and related words. In Genesis 49:4, Jacob's rebuke of Reuben for defiling his father's couch by lying with Bilhah cost Reuben the birthright preeminence — a grave violation of honor reflected in the same language as David's later offense with Bathsheba. Psalm 6:6 uses the image of the psalmist flooding his bed with tears of weeping in distress.</p><p>In the New Testament, the couch (Greek <em>krabattos</em>) is the portable mat or pallet carried by those who were healed by Jesus. The paralytic healed at the pool of Bethesda and the one lowered through the roof in Capernaum were commanded to take up their couch and walk — the carrying of the very implement of their infirmity becoming the demonstration of their healing. The household couch or dining couch also provided the setting for meals at which significant teaching occurred.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "couch", "smith": "couch", "isbe": "couch"},
        "key_refs": ["Genesis 49:4", "Job 7:13", "Psalms 6:6"]
    },
    "coulter": {
        "id": "coulter",
        "term": "Coulter",
        "category": "concepts",
        "intro": "<p>Coulter (also coulter or colter) is an agricultural implement that in modern usage refers to the vertical blade on a plow that cuts the soil ahead of the plowshare. In 1 Samuel 13:20–21, the term appears in the context of Philistine control of ironworking: Israelites had to go down to the Philistines to sharpen their plowshares, mattocks, axes, and coulters — a technological dependence that left Israel militarily disadvantaged, since the Philistines would not allow iron tools that could be converted into weapons to be sharpened by Israelites.</p><p>The same agricultural tool appears symbolically in the famous peace passages of Isaiah 2:4 and Micah 4:3, where nations will beat their swords into plowshares and their spears into pruning hooks — and in the inverted call to war in Joel 3:10, where the nations are summoned to beat plowshares into swords. The coulter and plowshare thus anchor both the agricultural economy of the ancient world and the prophetic vision of peace as the transformation of instruments of war into instruments of cultivation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "coulter", "isbe": "coulter"},
        "key_refs": ["1 Samuel 13:20", "Isaiah 2:4", "Micah 4:3"]
    },
    "council": {
        "id": "council",
        "term": "Council",
        "category": "concepts",
        "intro": "<p>Council in the New Testament primarily refers to the Sanhedrin — the supreme Jewish council of seventy-one members that served as the highest religious and judicial authority in Jerusalem. Jesus warned his disciples that they would be delivered to councils (Matthew 10:17; Mark 13:9), and the Sanhedrin is the body before which Jesus was tried (Matthew 26:59), Stephen was condemned (Acts 6:12), Peter and John were examined (Acts 4:5–15), and Paul gave his defense (Acts 22:30–23:10). The term also appears for lesser local councils that could administer discipline within the Jewish community.</p><p>In the Roman administrative context, Acts 25:12 refers to the governor's council of advisers with whom Festus consulted about Paul's case. The New Testament's repeated references to councils in the context of persecution reflect the actual mechanisms by which the early church was pressured — through the established institutions of both Jewish religious governance and Roman provincial administration. The Sanhedrin's authority was limited by Roman oversight, which is why condemnation there required confirmation from Pilate to carry out a death sentence.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "council", "smith": "council"},
        "key_refs": ["Matthew 5:22", "Matthew 10:17", "Acts 4:5", "Acts 25:12"]
    },
    "counsellor": {
        "id": "counsellor",
        "term": "Counsellor",
        "category": "concepts",
        "intro": "<p>Counsellor in Scripture denotes an adviser — one whose wisdom and judgment are sought by individuals or leaders facing decisions. Proverbs 11:14 notes that in a multitude of counsellors there is safety, and 15:22 observes that plans fail without counsel but succeed with many advisers. Ahithophel, David's chief counsellor, was so renowned that his advice was treated as the oracle of God (2 Samuel 16:23). The wisdom literature consistently values the counsel of the experienced and wise as essential to sound governance and personal decision-making.</p><p>Isaiah 9:6 gives the title <em>Wonderful, Counsellor</em> to the coming messianic king — the one whose counsel would be marked by the Spirit of wisdom and understanding (Isaiah 11:2). In the New Testament, Joseph of Arimathea is described as an honourable counsellor and a member of the Sanhedrin who had not consented to the council's condemnation of Jesus (Mark 15:43; Luke 23:50–51). The Paraclete (Advocate/Helper) of John's Gospel carries the semantic range of the counsellor who guides into truth.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "counsellor"},
        "key_refs": ["Proverbs 11:14", "Isaiah 9:6", "Mark 15:43"]
    },
    "courses": {
        "id": "courses",
        "term": "Courses",
        "category": "concepts",
        "intro": "<p>Courses refers to the rotational divisions David established for the priests and Levites in preparation for the temple service. Unable to build the temple himself, David organized the priestly clans into twenty-four courses or divisions, each responsible for temple service for one week twice annually (1 Chronicles 24:1–18). The Levitical singers and gatekeepers were similarly organized into corresponding courses (1 Chronicles 25–26). The system was activated when Solomon dedicated the temple and continued through the period of the monarchy.</p><p>The course system was restored after the exile (Nehemiah 12:1–26; 13:30) and was still functioning in New Testament times. Luke 1:5 notes that Zechariah, the father of John the Baptist, was a priest of the course of Abijah — the eighth of the twenty-four courses — serving in the temple when the angel Gabriel appeared to him. The course of Abijah's duty in the temple thus provides the chronological anchor for Luke's infancy narrative and for attempts to date the birth of John the Baptist and subsequently of Jesus.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "courses"},
        "key_refs": ["1 Chronicles 24:1", "2 Chronicles 31:2", "Luke 1:5"]
    },
    "court": {
        "id": "court",
        "term": "Court",
        "category": "concepts",
        "intro": "<p>Court in Scripture refers to enclosed areas associated with the tabernacle, the temple, or royal palaces. The tabernacle court was a rectangular enclosure approximately 150 by 75 feet, bounded by curtain-hung posts, containing the altar of burnt offering and the laver (Exodus 27:9–19; 40:8). Solomon's temple had both an inner court (the priests' court, 1 Kings 6:36) and a great outer court (the people's court). Herod's expanded temple complex had multiple courts — including the Court of the Gentiles, the Court of Women, the Court of Israel, and the Court of Priests.</p><p>The metaphor of dwelling in the courts of God's house runs through the Psalms as the supreme expression of spiritual desire: <em>My soul longeth, yea, even fainteth for the courts of the LORD</em> (Psalm 84:2). <em>Better is one day in thy courts than a thousand elsewhere</em> (Psalm 84:10). The royal courts of Persia appear in Esther and Nehemiah, where access to the inner court of the king was regulated by strict protocol. The court of the guard in Jerusalem served as Jeremiah's place of confinement and continued prophetic ministry (Jeremiah 37:21; 38:6–13).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "court", "smith": "court", "isbe": "court"},
        "key_refs": ["Exodus 27:9", "1 Kings 6:36", "Psalms 84:2", "Psalms 84:10"]
    },
    "covenant": {
        "id": "covenant",
        "term": "Covenant",
        "category": "concepts",
        "intro": "<p>Covenant (Hebrew <em>berith</em>; Greek <em>diatheke</em>) is one of the organizing categories of biblical theology, denoting a solemn, binding agreement between parties with defined obligations and consequences. In the Old Testament, covenants were made between humans (Genesis 21:32; Joshua 9:6; 1 Samuel 11:1) and between God and individuals or peoples. The major divine covenants — with Noah (Genesis 9), Abraham (Genesis 15; 17), Moses and Israel (Exodus 19–24; Deuteronomy), the Aaronic priesthood (Numbers 25:12–13), and David (2 Samuel 7; Psalm 89) — form the redemptive-historical backbone of the Old Testament. Each covenant involves divine initiative, promises, obligations, and typically a sign.</p><p>The Old Testament prophets anticipate a <em>new covenant</em> (Jeremiah 31:31–34) that would surpass the Mosaic covenant by writing the law on hearts rather than stone and accomplishing full forgiveness. The New Testament presents Jesus's death as the establishment of this new covenant, ratified by his blood (Luke 22:20; 1 Corinthians 11:25). Hebrews develops the contrast most fully: Christ is the mediator of a better covenant (Hebrews 8:6), the old covenant having been rendered obsolete. The Greek <em>diatheke</em> can also mean <em>will</em> or <em>testament</em>, a double meaning Hebrews 9:15–17 exploits to show that the covenant-will takes effect through the death of the testator.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "covenant", "smith": "covenant"},
        "key_refs": ["Genesis 15:18", "Jeremiah 31:31", "Luke 22:20", "Hebrews 8:6"]
    },
    "covering-of-the-eyes": {
        "id": "covering-of-the-eyes",
        "term": "Covering of the eyes",
        "category": "concepts",
        "intro": "<p>The covering of the eyes appears only in Genesis 20:16, in the context of Abimelech's restoration of Sarah to Abraham after he had taken her, believing her to be Abraham's sister. Abimelech gave Abraham a thousand pieces of silver and told Sarah: <em>Behold, he is to thee a covering of the eyes, unto all that are with thee, and with all other</em>. The precise meaning is disputed. The Revised Version renders it: <em>he is unto thee a covering of the eyes</em>, suggesting that Abraham's authority and wealth would serve as a public vindication that protects Sarah's honor.</p><p>Some interpreters understand the silver as compensation that would enable Sarah to afford a face veil — the physical <em>covering of the eyes</em> — that would protect her from future unwanted attention. Others read the phrase as meaning that the silver would speak publicly on her behalf, covering (vindicating) her in the eyes of others. The passage is unique in the biblical text and its exact social and legal background remains a subject of scholarly discussion.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "covering-of-the-eyes"},
        "key_refs": ["Genesis 20:16"]
    },
    "covetousness": {
        "id": "covetousness",
        "term": "Covetousness",
        "category": "concepts",
        "intro": "<p>Covetousness — a strong, consuming desire for what belongs to another — is forbidden in the tenth commandment (<em>thou shalt not covet</em>, Exodus 20:17; Deuteronomy 5:21), which uniquely among the Decalogue's prohibitions targets an internal disposition rather than an observable action. Paul identifies covetousness as the commandment that made him aware of sin (Romans 7:7) and calls it idolatry (Colossians 3:5; Ephesians 5:5) — because the covetous person effectively places the desired object or wealth in the position God alone should occupy.</p><p>Covetousness drives many of the most consequential sins in Scripture: Achan's theft of the devoted spoil (Joshua 7), Ahab and Jezebel's seizure of Naboth's vineyard (1 Kings 21), Judas's betrayal of Jesus for thirty pieces of silver. The New Testament presents contentment as the antidote: Hebrews 13:5 commands that conduct be free from love of money, content with present circumstances, because God has promised never to leave or forsake. Paul's own testimony — that he had learned contentment in both abundance and want (Philippians 4:11–12) — grounds the command in experienced grace rather than mere willpower.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "covetousness", "isbe": "covetousness"},
        "key_refs": ["Exodus 20:17", "Colossians 3:5", "Hebrews 13:5", "Philippians 4:11"]
    },
    "cow": {
        "id": "cow",
        "term": "Cow",
        "category": "concepts",
        "intro": "<p>Cows and cattle were central to the agricultural and sacrificial life of ancient Israel. The Mosaic law required that a cow and her calf not be killed on the same day (Leviticus 22:28) — a principle of humane restraint in animal husbandry. The prohibition against seething a kid in its mother's milk (Exodus 23:19; Deuteronomy 14:21) reflects a similar concern, and became foundational in the later development of kosher food laws. Seven fat and seven lean cows in Pharaoh's dream (Genesis 41) symbolized the seven years of plenty and seven of famine — one of the most memorable uses of animal symbolism in patriarchal narrative.</p><p>Cows were used both as draft animals for plowing and as sacrificial animals. The red heifer of Numbers 19 — a cow without blemish that had never been yoked — was used in the purification ritual for those defiled by contact with a corpse. Isaiah 7:21 pictures the messianic age of simplicity as a time when a man will keep only one cow and two sheep yet have abundant dairy. Amos 4:1 uses the image of <em>cows of Bashan</em> — the fat, well-fed cattle of the Transjordanian plateau — as a metaphor for the self-indulgent wealthy women of Samaria.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cow", "smith": "cow"},
        "key_refs": ["Leviticus 22:28", "Genesis 41:2", "Numbers 19:2", "Amos 4:1"]
    },
    "crane": {
        "id": "crane",
        "term": "Crane",
        "category": "concepts",
        "intro": "<p>Crane translates the Hebrew <em>agur</em> in Isaiah 38:14 and Jeremiah 8:7, though some scholars identify this as the swallow rather than the crane. In Isaiah 38:14, Hezekiah's lament during his illness employs the image of chattering like a crane or swallow as a picture of desperate, inarticulate prayer — cries that go beyond coherent speech. The chattering of small birds is used to express the extremity of grief and weakness.</p><p>Jeremiah 8:7 uses the crane's migratory instinct as a pointed contrast with Israel's spiritual obtuseness: <em>the stork in the heaven knoweth her appointed times; and the turtle and the crane and the swallow observe the time of their migration: but my people know not the judgment of the LORD.</em> The birds follow their God-given instincts precisely and seasonally, while Israel cannot recognize the times of divine visitation and warning. The migratory regularity of birds becomes a rebuke to human moral and spiritual insensitivity.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "crane", "smith": "crane", "isbe": "crane"},
        "key_refs": ["Isaiah 38:14", "Jeremiah 8:7"]
    },
    "creation": {
        "id": "creation",
        "term": "Creation",
        "category": "concepts",
        "intro": "<p>Creation in biblical theology is the act by which God brought all things into being from nothing — ex nihilo — by the power of his word. Genesis 1–2 provides the foundational account, presenting creation as ordered, purposeful, and declared very good. The repeated pattern of divine speech, creative act, divine evaluation, and named time period structures the narrative as a theological affirmation of God's sovereignty over all that exists. The Psalms celebrate the created order as evidence of the Creator's power and faithfulness (Psalms 8, 19, 104), and Job 38–41 develops creation's incomprehensibility as a ground for humility before God.</p><p>The New Testament attributes the role of agent of creation to Christ: <em>all things were made through him, and without him was not any thing made that was made</em> (John 1:3; see also Colossians 1:16; Hebrews 1:2). The same Christ through whom all things were made becomes the one through whom all things are to be reconciled (Colossians 1:20). Paul's concept of the <em>new creation</em> (2 Corinthians 5:17; Galatians 6:15) applies the creation category to the individual in Christ, while Romans 8:19–22 portrays the entire created order as groaning for the eschatological liberation that will accompany the glory of God's children.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "creation", "smith": "creation", "isbe": "creation"},
        "key_refs": ["Genesis 1:1", "John 1:3", "Colossians 1:16", "Romans 8:19"]
    },
    "creature": {
        "id": "creature",
        "term": "Creature",
        "category": "concepts",
        "intro": "<p>Creature in biblical usage denotes the whole of created existence, or individual members of the created order. In Romans 8:19–22, the creature (<em>ktisis</em>, creation) is personified as groaning and travailing in pain, subjected to futility at Adam's fall, now awaiting the revelation of the sons of God and the liberation that will accompany the resurrection. Paul's cosmic scope here extends the consequences of the fall and the reach of redemption beyond humanity to the entire created order.</p><p>Colossians 1:15 describes Christ as the <em>firstborn of all creation</em> — a title indicating his priority and preeminence over all created things rather than his own createdness (as the following verses make clear: all things were created in him, through him, and for him). Revelation 5:13 portrays every creature in heaven and earth and under the earth and in the sea joining in the worship of the Lamb and the one who sits on the throne. The <em>four living creatures</em> (Ezekiel 1:5–14; Revelation 4:6–8) are a special class of heavenly beings whose form combines features of human, lion, ox, and eagle — representing the fullness of creaturely life in the presence of God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "creature", "isbe": "creature"},
        "key_refs": ["Romans 8:19", "Colossians 1:15", "Revelation 5:13"]
    },
    "crescens": {
        "id": "crescens",
        "term": "Crescens",
        "category": "people",
        "intro": "<p>Crescens (meaning <em>growing</em> or <em>increasing</em>) was a companion of Paul mentioned in 2 Timothy 4:10 as having departed for Galatia. The verse appears in Paul's final and most personal letter, written during his second Roman imprisonment, in which he notes that Demas has forsaken him for love of the present world, Crescens has gone to Galatia, and Titus to Dalmatia — leaving Paul nearly alone except for Luke. Whether Crescens's departure was for missionary purposes or for personal reasons the text does not say, but the context groups him with Titus rather than with the defector Demas, suggesting his departure was mission-related.</p><p>Crescens is otherwise unknown in the New Testament. Some ancient traditions associate him with founding churches in Gaul or Vienna, but these accounts are late and historically uncertain. He is one of the minor figures in Paul's circle who appears only in the intimate personal correspondence of the Pastorals.</p>",
        "hitchcock_meaning": "growing; increasing",
        "source_ids": {"easton": "crescens", "smith": "crescens", "isbe": "crescens"},
        "key_refs": ["2 Timothy 4:10"]
    },
    "crete": {
        "id": "crete",
        "term": "Crete",
        "category": "places",
        "intro": "<p>Crete (now called Candia) is one of the largest islands in the Mediterranean, approximately 156 miles long and 7–35 miles wide, situated south of the Aegean Sea. In the ancient world it was renowned as the legendary birthplace of Zeus and the home of the Minoan civilization, one of the earliest advanced cultures of the Mediterranean. In the New Testament, Cretans are listed among those present at Jerusalem on the day of Pentecost (Acts 2:11), indicating an established Jewish diaspora on the island.</p><p>Paul's ship passed along the southern coast of Crete during the voyage to Rome described in Acts 27, stopping at Fair Havens before the disastrous storm drove the ship to Malta. Titus was left in Crete to organize the churches there and appoint elders in every city (Titus 1:5), and Paul quotes the Cretan philosopher Epimenides against the Cretans themselves: <em>the Cretans are always liars, evil beasts, slow bellies</em> (Titus 1:12) — a self-referential paradox that became famous in logic. The epistle to Titus provides the primary biblical window into the early church community on the island.</p>",
        "hitchcock_meaning": "carnal; fleshly",
        "source_ids": {"easton": "crete", "smith": "crete", "isbe": "crete"},
        "key_refs": ["Acts 2:11", "Acts 27:7", "Titus 1:5", "Titus 1:12"]
    },
    "crimson": {
        "id": "crimson",
        "term": "Crimson",
        "category": "concepts",
        "intro": "<p>Crimson in the Bible refers to a deep red dye derived from the crushed dried bodies of scale insects (<em>Coccus ilicis</em> or <em>Kermes</em>) that lived on certain oak trees in the ancient Mediterranean world. The Hebrew terms include <em>karmil</em> and <em>shani</em> (scarlet). Crimson and scarlet were used extensively in the tabernacle furnishings and the high priest's vestments (Exodus 25–28), prized for their richness and durability. The dye was one of the most valuable commodities in ancient textile trade.</p><p>Isaiah 1:18 uses crimson and scarlet as the paradigmatic image of sin's depth in God's sight — <em>though your sins be as scarlet, they shall be as white as snow; though they be red like crimson, they shall be as wool</em> — with the promise of complete cleansing the theological counterpoint to the seemingly indelible stain. The scarlet thread in Rahab's window (Joshua 2:18–21), the scarlet cord of the Song of Solomon (4:3), and the scarlet robe placed on Jesus at his mocking (Matthew 27:28) all carry the complex associations of crimson in the biblical imagination — from luxury and honor to sin and shame.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "crimson", "isbe": "crimson"},
        "key_refs": ["Isaiah 1:18", "Joshua 2:18", "Matthew 27:28"]
    },
    "crisping-pin": {
        "id": "crisping-pin",
        "term": "Crisping-pin",
        "category": "concepts",
        "intro": "<p>Crisping-pin appears in Isaiah 3:22 in the list of ornaments and accessories of the <em>daughters of Zion</em> that God declares will be removed in judgment. The Hebrew <em>charit</em> (from a root meaning to cut or engrave) is understood variously as a hair-curling iron, a crisping pin for curling hair, or as the Revised Version suggests, a satchel or bag. The same word appears in 2 Kings 5:23 rendered as bags, where Naaman's silver was carried in two bags.</p><p>The identification with a hair-curling implement — a heated implement for curling or crimping hair — is the traditional English reading, reflected in the King James rendering. Isaiah 3:18–23 catalogues an extensive list of ornamental accessories worn by the women of Jerusalem's elite, their removal in Isaiah's oracle representing the stripping away of the trappings of pride and luxury. Whether crisping-pin refers to a hairdressing implement or a purse, it belongs to the world of feminine adornment that the prophet places under divine judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "crisping-pin"},
        "key_refs": ["Isaiah 3:22"]
    },
    "crispus": {
        "id": "crispus",
        "term": "Crispus",
        "category": "people",
        "intro": "<p>Crispus (meaning <em>curled</em>) was the ruler of the Jewish synagogue at Corinth who believed in the Lord after hearing Paul's preaching, along with his entire household (Acts 18:8). His conversion was significant because it represented the conversion of the synagogue's head official — the person responsible for organizing worship and inviting speakers — and his whole household following. Paul mentions that he personally baptized Crispus at Corinth (1 Corinthians 1:14), noting that he baptized very few individuals personally, usually leaving baptism to his associates.</p><p>The public conversion of the synagogue ruler was likely a catalyst for the wider response at Corinth, and it also contributed to the tensions that led some Jews to bring Paul before the proconsul Gallio. Crispus's replacement as synagogue ruler was presumably Sosthenes (Acts 18:17), who was later beaten by the mob before Gallio's seat. A Sosthenes is named as Paul's co-author in the opening of First Corinthians (1:1), possibly the same person who later himself became a believer.</p>",
        "hitchcock_meaning": "curled",
        "source_ids": {"easton": "crispus", "smith": "crispus", "isbe": "crispus"},
        "key_refs": ["Acts 18:8", "1 Corinthians 1:14"]
    },
    "cross": {
        "id": "cross",
        "term": "Cross",
        "category": "concepts",
        "intro": "<p>The cross was in the Greco-Roman world the instrument of capital punishment reserved for slaves and the worst criminals — a means of execution designed to maximize shame, pain, and public humiliation. In the New Testament it becomes the central symbol of Christian faith, the site of Christ's atoning death and the axis around which the entire gospel revolves. Paul makes the cross the deliberate center of his preaching: <em>I determined not to know any thing among you, save Jesus Christ, and him crucified</em> (1 Corinthians 2:2). The message of the cross is <em>foolishness to those who are perishing, but to those who are being saved it is the power of God</em> (1 Corinthians 1:18).</p><p>The New Testament uses the cross as both historical event and theological symbol. Galatians 2:20 and 6:14 describe the believer as crucified with Christ and the world crucified to the believer through the cross. Ephesians 2:16 states that through the cross Christ reconciled both Jews and Gentiles to God in one body, having slain the enmity between them. Hebrews 12:2 presents Jesus who for the joy set before him endured the cross, despising the shame, as the ultimate model for persevering faith. The self-denial Jesus calls disciples to — taking up one's cross daily — extends the cross metaphor from his death to the pattern of his followers' lives.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cross", "smith": "cross", "isbe": "cross"},
        "key_refs": ["1 Corinthians 1:18", "Galatians 6:14", "Ephesians 2:16", "Hebrews 12:2"]
    },
    "crown": {
        "id": "crown",
        "term": "Crown",
        "category": "concepts",
        "intro": "<p>Crown in Scripture refers to several distinct types of headwear or ornaments signifying authority, honor, or holiness. The high priest's crown was the golden plate inscribed <em>Holiness to the LORD</em> fastened to his turban (Exodus 29:6; 39:30). Royal crowns were seized as trophies of war (2 Samuel 12:30; 2 Kings 11:12) and were symbols of dynastic legitimacy and divine favor — Psalm 89:39 describes God casting the king's crown to the ground as a picture of judgment on the Davidic line.</p><p>In the New Testament, the crown (Greek <em>stephanos</em>, the victor's wreath, versus <em>diadema</em>, the royal crown) is the primary image of eternal reward. Paul describes the crown of righteousness awaiting those who love Christ's appearing (2 Timothy 4:8), the incorruptible crown that athletes who discipline themselves will receive (1 Corinthians 9:25), and his own converts as his crown of rejoicing (1 Thessalonians 2:19; Philippians 4:1). James promises the crown of life to those who endure temptation (James 1:12), and Revelation presents crowned elders (4:4) who cast their crowns before the throne in worship, and Christ himself wearing many diadems (19:12).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "crown", "smith": "crown", "isbe": "crown"},
        "key_refs": ["Exodus 29:6", "2 Timothy 4:8", "1 Corinthians 9:25", "Revelation 4:4"]
    },
    "crown-of-thorns": {
        "id": "crown-of-thorns",
        "term": "Crown of thorns",
        "category": "concepts",
        "intro": "<p>The crown of thorns was plaited by Roman soldiers and placed on Jesus's head during his mocking before the crucifixion, recorded in Matthew 27:29, Mark 15:17, and John 19:2. The act was part of a sustained mockery of Jesus's claim to be king of the Jews — the soldiers dressed him in a purple robe, put a reed in his hand as a scepter, and knelt before him crying <em>Hail, King of the Jews!</em> before striking him. The thorns inflicted both pain and humiliation, inverting the royal crown into an instrument of suffering.</p><p>Theological reflection on the crown of thorns has consistently found resonance with the curse of Genesis 3:17–18, where thorns and thistles come from the ground cursed for Adam's sin — the thorns pressed onto the head of the second Adam are read as the bearing of the curse that came through the first. The crown of thorns also stands in ironic contrast with the crowns of glory and life that the New Testament promises to those who suffer with Christ, and with the many crowns Christ wears in Revelation 19:12 as the returning King of kings.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "crown-of-thorns", "smith": "crown-of-thorns", "isbe": "crown-of-thorns"},
        "key_refs": ["Matthew 27:29", "Mark 15:17", "John 19:2"]
    },
    "crucifixion": {
        "id": "crucifixion",
        "term": "Crucifixion",
        "category": "events",
        "intro": "<p>Crucifixion was a form of capital punishment practiced by Persians, Carthaginians, and Romans in which the condemned was bound or nailed to a wooden cross and left to die — typically from a combination of exhaustion, asphyxiation, and shock. It was considered the most shameful form of death in the ancient world, reserved for slaves, rebels, and the lowest criminals. Mosaic law declared that a man hung on a tree was cursed by God (Deuteronomy 21:23), a text Paul cites in Galatians 3:13 to explain how Christ becoming a curse for us accomplished redemption. The Romans adopted crucifixion as an imperial instrument of control and public deterrence, and it was widely practiced throughout the first century Mediterranean.</p><p>The crucifixion of Jesus is the central event of the New Testament and the climax of all four Gospels. It took place outside Jerusalem at Golgotha under the authority of Pontius Pilate, following a night of trials before Jewish and Roman authorities. The Gospels emphasize its fulfillment of prophetic Scripture — especially Psalm 22 and Isaiah 53 — and its voluntary character: Jesus laid down his life of his own accord. Paul's theology of the cross in Romans, Galatians, 2 Corinthians, and Colossians interprets it as the means of atonement, justification, reconciliation, and the defeat of sin and death.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "crucifixion", "smith": "crucifixion", "isbe": "crucifixion"},
        "key_refs": ["Deuteronomy 21:23", "Galatians 3:13", "Luke 23:33", "John 19:18"]
    },
    "cruse": {
        "id": "cruse",
        "term": "Cruse",
        "category": "concepts",
        "intro": "<p>A cruse was a small vessel — a flask or jug — used for carrying water or oil. In 1 Samuel 26:11–16, a cruse of water was placed at Saul's head while he slept, and David took it as proof that he had been within striking distance of the king, demonstrating his restraint and loyalty. Elijah's first post-Carmel experience involves a cruse of water and a cake baked on coals provided by an angel at the juniper tree (1 Kings 19:6), and the miraculous cruse of oil that belonged to the widow of Zarephath did not run dry throughout the years of drought (1 Kings 17:12–16).</p><p>The cruse of oil is also associated with the prophetic acts of anointing: Samuel used a cruse (vial) of oil to anoint Saul as king of Israel in 1 Samuel 10:1. The smallness of the vessel emphasizes the abundance of divine provision — a handful of meal and a small cruse of oil stretched through years of famine, and the oil in the cruse becomes a type of the inexhaustible grace that accompanies God's appointments.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cruse", "smith": "cruse", "isbe": "cruse"},
        "key_refs": ["1 Samuel 26:11", "1 Kings 17:12", "1 Kings 19:6"]
    },
    "crystal": {
        "id": "crystal",
        "term": "Crystal",
        "category": "concepts",
        "intro": "<p>Crystal in Scripture renders Hebrew <em>qerach</em> (ice or rock crystal) and Greek <em>krustallos</em>. Ezekiel 1:22 describes the firmament above the living creatures as the color of crystal, terrible in its brightness — a detail in the visionary throne-chariot (merkabah) that conveys the dazzling transparency and clarity of the divine realm. Job 28:17 mentions crystal alongside gold as something to which wisdom cannot be compared in value.</p><p>In Revelation, crystal appears repeatedly in descriptions of the heavenly realm. The sea of glass before the throne is like crystal (Revelation 4:6), evoking the primordial waters of Genesis 1 stilled and made perfectly transparent before God. The New Jerusalem is described as having walls of jasper and the city itself of pure gold, clear as glass or crystal (Revelation 21:11, 18). The river of the water of life proceeds from the throne of God and the Lamb, bright as crystal (Revelation 22:1). Crystal's primary connotations in apocalyptic vision are transparency, purity, and the refraction of divine light — the heavenly world rendered visible to prophetic sight.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "crystal", "smith": "crystal", "isbe": "crystal"},
        "key_refs": ["Ezekiel 1:22", "Revelation 4:6", "Revelation 21:11", "Revelation 22:1"]
    },
    "cubit": {
        "id": "cubit",
        "term": "Cubit",
        "category": "concepts",
        "intro": "<p>The cubit (Hebrew <em>ammah</em>, literally <em>mother of the arm</em> or forearm) was the most common unit of linear measurement in the ancient Near East, derived from the length of the forearm from the elbow to the tip of the middle finger. The standard Israelite cubit was approximately 18 inches (about 44 cm), though a longer royal or sacred cubit of approximately 20.5 inches is also attested in Egyptian and Babylonian contexts and was likely used in the construction of the temple (Ezekiel 40:5 distinguishes a cubit plus a handbreadth from the ordinary cubit).</p><p>The cubit pervades the measurements of the tabernacle (Exodus 25–27), Solomon's temple (1 Kings 6–7), and Ezekiel's visionary temple (Ezekiel 40–48). Noah's ark was 300 cubits long, 50 wide, and 30 high (Genesis 6:15). Goliath's height was six cubits and a span (1 Samuel 17:4). Jesus's use of cubit in Matthew 6:27 — <em>which of you by taking thought can add one cubit unto his stature?</em> — may refer to either height or the span of life, illustrating the futility of anxious effort to extend what God alone controls.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cubit", "smith": "cubit", "isbe": "cubit"},
        "key_refs": ["Genesis 6:15", "Exodus 25:10", "1 Kings 6:2", "Matthew 6:27"]
    },
    "cuckoo": {
        "id": "cuckoo",
        "term": "Cuckoo",
        "category": "concepts",
        "intro": "<p>Cuckoo is the rendering in the King James Version of the Hebrew <em>shahaph</em> (from a root meaning to be lean or slender) in Leviticus 11:16 and Deuteronomy 14:15, where it is listed among the unclean birds Israel was forbidden to eat. The identification of this Hebrew bird name with the European cuckoo is uncertain — the term may refer to a sea gull, petrel, or some other slim coastal bird. Modern translations often render <em>shahaph</em> as sea gull.</p><p>The exact identification matters little for the theological content of the dietary laws, which the New Testament treats as fulfilled in Christ and abrogated for the believing community through Peter's vision of clean and unclean animals (Acts 10:11–16) and Paul's teaching in Colossians 2:16–17 that food regulations were shadows pointing to Christ. The cuckoo/seagull occupies a minor place in the catalogue of unclean creatures.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cuckoo", "smith": "cuckoo"},
        "key_refs": ["Leviticus 11:16", "Deuteronomy 14:15"]
    },
    "cucumbers": {
        "id": "cucumbers",
        "term": "Cucumbers",
        "category": "concepts",
        "intro": "<p>Cucumbers (Hebrew <em>qishshuim</em>) appear only once in the biblical narrative, in Numbers 11:5, where the Israelites in the wilderness complained: <em>We remember the fish, which we did eat in Egypt freely; the cucumbers, and the melons, and the leeks, and the onions, and the garlic.</em> This catalogue of remembered Egyptian produce stands in ironic contrast to the miraculous manna God was providing daily — the Israelites preferred the remembered pleasures of slavery to the miraculous gift of freedom.</p><p>The cucumber was indeed a staple of the Egyptian diet and was widely cultivated in the Nile delta and the ancient Near East. Isaiah 1:8 references cucumber fields in the image of Jerusalem left like a lodge in a garden of cucumbers — a watchman's hut in a field, implying desolation and isolation. The single narrative appearance in Numbers places cucumber longing among the symptoms of a deeper spiritual problem: ungrateful discontent with divine provision that looks back to bondage with nostalgia.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cucumbers", "smith": "cucumbers"},
        "key_refs": ["Numbers 11:5"]
    },
    "cummin": {
        "id": "cummin",
        "term": "Cummin",
        "category": "concepts",
        "intro": "<p>Cummin (Hebrew <em>kammon</em>, meaning condiment) is the seed of <em>Cuminum cyminum</em>, an umbelliferous annual plant cultivated throughout the ancient Near East for its aromatic seeds used to flavor bread, soups, and meat. Isaiah 28:25–27 provides an agriculturally precise description of its cultivation and harvest: the farmer threshes cummin with a rod rather than a heavy sledge because the delicate seeds would be crushed — an illustration of God's wisdom in measuring appropriate judgment to the situation. The passage is one of the most detailed accounts of ancient farming practice in the prophetic literature.</p><p>In Matthew 23:23 Jesus rebukes the scribes and Pharisees for tithing mint, anise, and cummin while neglecting justice, mercy, and faithfulness — noting that the latter <em>ought ye to have done, and not to leave the other undone.</em> The mention of tithing such small seeds as cummin indicates how scrupulously the Pharisees applied Mosaic law to every agricultural product, even the tiniest. Jesus's point is not that cummin-tithing was wrong but that meticulous attention to small ritual observances must not crowd out the weightier matters of the law.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cummin", "smith": "cummin", "isbe": "cummin"},
        "key_refs": ["Isaiah 28:25", "Isaiah 28:27", "Matthew 23:23"]
    },
    "cup": {
        "id": "cup",
        "term": "Cup",
        "category": "concepts",
        "intro": "<p>The cup in Scripture functions both as a practical vessel and as a pervasive theological metaphor. Physically, cups in the ancient world ranged from simple clay vessels to elaborate golden drinking bowls (1 Kings 10:21; Revelation 17:4). The cup of a cupbearer was the vessel from which the king's wine was served, and the cupbearer's role was one of high trust because of the threat of poisoning. The cup of Nebuchadnezzar's vision (Daniel 5) and the wine cup of God's wrath in Jeremiah 25:15 reflect its use as a vessel of divine judgment.</p><p>The cup as a metaphor for one's appointed portion — whether of blessing or suffering — runs through the Psalms and prophets. Psalm 116:13 lifts the <em>cup of salvation</em> in grateful praise; Psalm 23:5 speaks of the cup running over. In Gethsemane, Jesus prays that the cup might pass from him — the cup being the full weight of divine judgment on human sin he was about to take (Matthew 26:39). The cup of the Lord's Supper (1 Corinthians 10:16; 11:25–28) is the cup of the new covenant in his blood, and its reception in faith is participation in the benefits of that death.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cup", "smith": "cup", "isbe": "cup"},
        "key_refs": ["Psalms 23:5", "Matthew 26:39", "1 Corinthians 10:16", "Revelation 17:4"]
    },
    "cup-bearer": {
        "id": "cup-bearer",
        "term": "Cup-bearer",
        "category": "concepts",
        "intro": "<p>The cup-bearer was an officer of high rank in the royal courts of Egypt, Persia, Assyria, and Israel, responsible for serving the king's wine and tasting it first to guard against poisoning. The position required absolute personal loyalty and unquestioned trustworthiness, placing the cup-bearer in intimate proximity to the king — a position that often led to significant political influence. Pharaoh's chief cup-bearer appears in Genesis 40–41, where his imprisonment alongside Joseph, his dream of the vine with three branches, and Joseph's correct interpretation of it as restoration in three days set in motion the chain of events leading to Joseph's rise to power in Egypt.</p><p>Nehemiah served as cup-bearer to the Persian king Artaxerxes (Nehemiah 1:11), a position that gave him regular access to the king in a context of personal confidence. When the king noticed Nehemiah's sadness and asked the reason, Nehemiah received permission and royal resources to return to Jerusalem and rebuild its walls. Solomon's cup-bearers so impressed the Queen of Sheba that she declared there was no more spirit in her on account of his magnificence (1 Kings 10:5; 2 Chronicles 9:4).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cup-bearer"},
        "key_refs": ["Genesis 40:1", "Nehemiah 1:11", "1 Kings 10:5"]
    },
    "curious-arts": {
        "id": "curious-arts",
        "term": "Curious arts",
        "category": "concepts",
        "intro": "<p>Curious arts refers in Acts 19:19 to magical arts and occult practices — the jugglery and divination practiced by the itinerant enchanters and sorcerers of Ephesus, which was renowned in the ancient world as a center of magical practice. When many of those who practiced the curious arts at Ephesus believed Paul's preaching, they brought their books of magical spells and burned them publicly in a pile — the value of the books was calculated at fifty thousand pieces of silver, indicating the scale and economic significance of the magical trade in the city.</p><p>The burning of the magical books at Ephesus is one of the most dramatic demonstrations of conversion in the book of Acts, illustrating the genuine and costly transformation of those who turned from occult practice to faith in Christ. The Greek term <em>perierga</em> (curious or magical arts) appears only here in the New Testament. The episode stands in contrast to the failed exorcism of the sons of Sceva just before it in Acts 19:13–16, demonstrating that authentic faith produces real change while imitation of Christian power without faith yields disaster.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "curious-arts"},
        "key_refs": ["Acts 19:19"]
    },
    "curse": {
        "id": "curse",
        "term": "Curse",
        "category": "concepts",
        "intro": "<p>Curse in Scripture denotes the pronouncement of harm or exclusion as divine judgment or as a conditional consequence of covenant violation. God's first curses fall on the serpent (Genesis 3:14), on Cain (4:11), and — through Adam's disobedience — on the ground itself (3:17). Noah's curse on Canaan (9:25), Jacob's curse on the anger of Simeon and Levi (49:7), and Joshua's curse on the rebuilder of Jericho (6:26) represent human pronouncements with divine backing. Deuteronomy 27–28 catalogues the covenant curses that would fall on Israel for disobedience — the most extensive curse-list in the Old Testament — and the exile is explicitly interpreted as their fulfillment.</p><p>Paul's theology of redemption from the curse in Galatians 3:10–13 is foundational: Christ became a curse for us — citing Deuteronomy 21:23's stipulation that one hung on a tree is cursed — thereby redeeming those under the law's curse. The final removal of curse is an eschatological promise: Revelation 22:3 declares that in the new Jerusalem there will be <em>no more curse</em> — the reversal of Genesis 3 accomplished through the death of Christ and applied to all creation in the new heaven and earth.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "curse", "isbe": "curse"},
        "key_refs": ["Genesis 3:14", "Deuteronomy 27:15", "Galatians 3:13", "Revelation 22:3"]
    },
    "curtain": {
        "id": "curtain",
        "term": "Curtain",
        "category": "concepts",
        "intro": "<p>Curtains in Scripture primarily refer to the hangings and veil systems of the tabernacle. Ten curtains of fine twined linen embroidered with cherubim in blue, purple, and scarlet formed the inner ceiling of the tabernacle structure (Exodus 26:1–6), held together by golden clasps. A further eleven curtains of goats' hair formed the outer tent (Exodus 26:7–13). The inner curtain or veil (<em>paroketh</em>) separated the Holy Place from the Most Holy Place, restricting access to the ark of the covenant and the divine presence to the high priest alone, once a year on the Day of Atonement (Leviticus 16).</p><p>Isaiah 40:22 uses God stretching out the heavens like a curtain as an image of divine majesty in creation. The theological significance of the inner veil culminates in the Gospels' account of the tearing of the temple curtain from top to bottom at the moment of Jesus's death (Matthew 27:51; Mark 15:38; Luke 23:45). Hebrews interprets this explicitly: access to the true Most Holy Place — God's own presence — has been opened through the body of Christ, the veil he passed through (Hebrews 10:19–20), and the way into the sanctuary now stands permanently open to all who approach through him.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "curtain", "isbe": "curtain"},
        "key_refs": ["Exodus 26:1", "Leviticus 16:2", "Matthew 27:51", "Hebrews 10:19"]
    },
    "cush": {
        "id": "cush",
        "term": "Cush",
        "category": "people",
        "intro": "<p>Cush (meaning <em>black</em>) refers primarily to the eldest son of Ham and grandson of Noah, from whom descended the Cushite peoples of northeast Africa (Genesis 10:6–8; 1 Chronicles 1:8–10). Cush was the father of Nimrod, the first great empire-builder of the post-flood world. The land of Cush, named for this ancestor, corresponds broadly to the region south of Egypt — the area known in antiquity as Ethiopia or Nubia, in modern terms roughly Sudan and northern Ethiopia. The river Gihon in Genesis 2:13 is said to encompass the whole land of Cush, connecting the primordial geography to this region.</p><p>Cush and the Cushites appear throughout the prophetic literature. Isaiah 18, 20, and 45, Ezekiel 29–30, and Psalm 68:31 all address or mention Cush, often as a representative of the distant nations that God will one day bring into his purposes. Ethiopia (Cush) stretching out its hands to God (Psalm 68:31) became in patristic interpretation a prophecy of the Gentile mission and the conversion of the Ethiopian eunuch in Acts 8. The name Cush is also applied to a Benjaminite (Psalm 7 superscription) and may have been used as a personal name.</p>",
        "hitchcock_meaning": "Ethiopians; blackness",
        "source_ids": {"easton": "cush", "smith": "cush"},
        "key_refs": ["Genesis 10:6", "Genesis 10:8", "Psalms 68:31", "Isaiah 18:1"]
    },
    "cushan": {
        "id": "cushan",
        "term": "Cushan",
        "category": "places",
        "intro": "<p>Cushan (likely a poetic or extended form of Cush) appears in Habakkuk 3:7 in the prophet's vision of divine theophany: <em>I saw the tents of Cushan in affliction: and the curtains of the land of Midian did tremble.</em> The name here is linked with Midian in a parallel structure, suggesting a region in or near Arabia or the Sinai peninsula associated with the southern Cushite population rather than the Nile-region Ethiopia. Some scholars identify Cushan with the Cushan-rishathaim of Judges 3:8–10 — the king of Mesopotamia who oppressed Israel before the judge Othniel delivered them.</p><p>The geography of Habakkuk 3 follows the route of the divine warrior coming from the south — from Teman and Mount Paran — through Cushan and Midian, the wilderness regions south and east of Canaan through which God had led Israel in the Exodus. Cushan's trembling in Habakkuk's vision recalls the terror that fell on surrounding peoples at the approach of Israel's God during the conquest period.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cushan", "smith": "cushan", "isbe": "cushan"},
        "key_refs": ["Habakkuk 3:7", "Judges 3:8", "Judges 3:10"]
    },
    "cushite": {
        "id": "cushite",
        "term": "Cushite",
        "category": "people",
        "intro": "<p>Cushite designates a person from the land of Cush — broadly the region of northeast Africa south of Egypt. The most prominent Cushite in the narrative books is the unnamed messenger whom Joab sent to David to announce the death of Absalom (2 Samuel 18:21–32). When Ahimaaz son of Zadok also ran to bring news, the watchman identified both runners, and David's anxious question — <em>Is the young man Absalom safe?</em> — was answered evasively by Ahimaaz and directly by the Cushite: <em>The enemies of my lord the king, and all that rise against thee to do thee hurt, be as that young man is.</em></p><p>Other Cushites in Scripture include Ebed-melech, the Cushite official who rescued Jeremiah from the cistern at great personal risk (Jeremiah 38:7–13) and received a personal promise of divine protection in the coming destruction (Jeremiah 39:15–18). Moses's wife is described as a Cushite in Numbers 12:1, prompting Miriam and Aaron's criticism. The Cushite identity of these individuals across widely different periods reflects the presence of Africans from the Nile region in Israelite and Judahite society throughout the monarchic era.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cushite", "isbe": "cushite"},
        "key_refs": ["2 Samuel 18:32", "Jeremiah 38:7", "Numbers 12:1"]
    },
    "custom": {
        "id": "custom",
        "term": "Custom",
        "category": "concepts",
        "intro": "<p>Custom in the New Testament refers to tax or tribute imposed by the Roman authorities. The <em>telonion</em> or toll-booth where Matthew sat collecting customs (Mark 2:14) was a station for levying tariffs on goods in transit, particularly profitable at Capernaum on the trade route from Damascus to the Mediterranean. The publicans (tax-farmers) who collected customs were despised in Jewish society as collaborators with Roman occupation and as likely extortioners, since they profited by collecting above the official rate.</p><p>Jesus's teaching on paying taxes to Caesar (Matthew 22:17–21; Mark 12:14–17) addressed the question of whether paying the Roman poll tax was lawful — his answer distinguishing what belongs to Caesar from what belongs to God became foundational in Christian reflection on civil obligation. Paul explicitly commands payment of custom and tribute to governing authorities in Romans 13:6–7: <em>render therefore to all their dues: tribute to whom tribute is due; custom to whom custom.</em> The custom system thus appears in the New Testament as a point of contact between the religious life of Jesus's followers and the economic structures of the Roman Empire.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "custom"},
        "key_refs": ["Mark 2:14", "Matthew 22:17", "Romans 13:7"]
    },
    "cuthah": {
        "id": "cuthah",
        "term": "Cuthah",
        "category": "places",
        "intro": "<p>Cuthah (also spelled Cuth) was a Babylonian city or district from which the Assyrian king Shalmaneser transported colonists to settle in Samaria after the deportation of the northern kingdom of Israel in 722 B.C. (2 Kings 17:24, 30). The Cuthites brought with them the worship of their deity Nergal, whom they continued to serve alongside the syncretistic adoption of Israelite religion — the combination that the biblical author condemns as the characteristic religion of the Samaritans. The Cuthites were apparently the most numerous of the transplanted groups, so that <em>Cuthean</em> became in later Jewish usage a standard term for Samaritans.</p><p>Cuthah is identified with the site of Tell Ibrahim, northeast of Babylon in modern Iraq, a significant ancient city with an important temple. The deportation and resettlement policy that brought Cuthites to Samaria was standard Assyrian practice for pacifying conquered territories — removing indigenous populations and replacing them with foreigners who had no ancestral loyalty to the land or its traditions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cuthah", "isbe": "cuthah"},
        "key_refs": ["2 Kings 17:24", "2 Kings 17:30"]
    },
    "cutting": {
        "id": "cutting",
        "term": "Cutting",
        "category": "concepts",
        "intro": "<p>Cutting the flesh was an idolatrous and mourning practice explicitly prohibited in Mosaic law. Deuteronomy 14:1 forbids Israel to cut themselves for the dead, and Leviticus 19:28 prohibits cuttings in the flesh as part of a broader prohibition on practices associated with pagan mourning rites. Leviticus 21:5 extends the prohibition to priests, who were forbidden to make any cuttings in their flesh. These prohibitions set Israel apart from surrounding cultures in which self-laceration was a standard expression of grief or religious ecstasy.</p><p>The most dramatic biblical example is the prophets of Baal on Mount Carmel who, when their prayers went unanswered, <em>cut themselves after their manner with knives and lancets, till the blood gushed out upon them</em> (1 Kings 18:28) — a practice Elijah's mockery highlights as characteristic of false religious frenzy. Jeremiah 41:5 records eighty men coming to Jerusalem with their beards shaved, their clothes torn, and their bodies gashed, bringing offerings — a mourning practice after the destruction of the temple. The New Testament prohibition on willful self-harm is grounded in the same theological conviction: the body as God's possession and temple is not to be treated as an expression of pagan grief or religious coercion.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cutting"},
        "key_refs": ["Deuteronomy 14:1", "Leviticus 19:28", "1 Kings 18:28", "Jeremiah 16:6"]
    },
    "cymbals": {
        "id": "cymbals",
        "term": "Cymbals",
        "category": "concepts",
        "intro": "<p>Cymbals (Hebrew <em>tzeltzelim</em>, from a root meaning to tinkle or clash) were percussion instruments consisting of two circular metal plates struck together to produce sound. They were used in Israel's worship both at the tabernacle and the temple, and appear frequently in the lists of musical instruments employed in processional worship. David used cymbals in the joyful procession of the ark to Jerusalem (2 Samuel 6:5; 1 Chronicles 13:8), and David organized the Levitical musicians — including Heman, Asaph, and Ethan — to play bronze cymbals in the temple service (1 Chronicles 15:16–19, 28).</p><p>Psalm 150:5 calls for praise with loud cymbals and high-sounding cymbals in the concluding doxology of the Psalter — the most expansive call to instrumental praise in Scripture. Paul's use of the clanging cymbal in 1 Corinthians 13:1 — <em>though I speak with the tongues of men and of angels, and have not charity, I am become as sounding brass, or a tinkling cymbal</em> — turns the image of ceremonial praise into a figure of empty spiritual performance: impressive sound without the substance of love. The metaphor becomes one of the most cited illustrations in Pauline theology.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cymbals"},
        "key_refs": ["2 Samuel 6:5", "1 Chronicles 15:16", "Psalms 150:5", "1 Corinthians 13:1"]
    },
    "cypress": {
        "id": "cypress",
        "term": "Cypress",
        "category": "concepts",
        "intro": "<p>Cypress in the Revised Version translates the Hebrew <em>tirzah</em> in Isaiah 44:14, where the word denotes the wood used by an idol-maker to carve a god and to warm himself at a fire. The King James Version renders it <em>holm tree</em>, and the identification with either the cypress or the holm oak (evergreen oak) is uncertain. Both are durable hardwoods available in the ancient Near East and suitable for the woodworking the passage describes.</p><p>Isaiah 44:13–17 is one of the most pointed satires of idolatry in the prophetic literature: the craftsman plants a cedar, a cypress, and an oak; uses part of the wood to warm himself and bake bread; and with the remainder makes a god and falls down before it, saying <em>Deliver me; for thou art my god.</em> The passage highlights the irrational character of idolatry — using the same material for fuel and for worship — as the paradigmatic example of what Hosea calls a deceived heart turning aside from reason and truth.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cypress", "smith": "cypress", "isbe": "cypress"},
        "key_refs": ["Isaiah 44:14"]
    },
    "cyprus": {
        "id": "cyprus",
        "term": "Cyprus",
        "category": "places",
        "intro": "<p>Cyprus is one of the largest islands in the Mediterranean, approximately 148 miles long and 40 miles wide, situated south of Cilicia in the northeastern Mediterranean. In antiquity it was famous for its copper mines — the very word <em>copper</em> derives from the island's name. Numbers 24:24 may allude to Cyprus under the name <em>Chittim</em>, and the island had a significant Jewish diaspora community. Acts 4:36 identifies Barnabas as a Levite <em>of the country of Cyprus</em>, establishing the island's importance in the early church.</p><p>Paul and Barnabas visited Cyprus on the first missionary journey, preaching in the synagogues at Salamis and traveling across the island to Paphos, where the confrontation with the sorcerer Elymas (Bar-jesus) and the conversion of the proconsul Sergius Paulus occurred (Acts 13:4–12). Paul's ship passed Cyprus on his final journey to Jerusalem (Acts 21:3) and during the voyage to Rome (Acts 27:4). After the separation from Paul, Barnabas returned to Cyprus with Mark (Acts 15:39), suggesting a continued church presence on the island meaningful to Barnabas personally.</p>",
        "hitchcock_meaning": "fair; fairness",
        "source_ids": {"easton": "cyprus", "smith": "cyprus", "isbe": "cyprus"},
        "key_refs": ["Acts 4:36", "Acts 13:4", "Acts 21:3"]
    },
    "cyrene": {
        "id": "cyrene",
        "term": "Cyrene",
        "category": "places",
        "intro": "<p>Cyrene was a prominent Greek city in the region of Cyrenaica (modern northeastern Libya), founded as a Greek colony and later a Roman provincial capital known for its philosophical schools and large Jewish population. Acts 2:10 lists Cyrenians among those present at Pentecost, indicating an established diaspora community. The city had its own synagogue in Jerusalem, attended by Cyrenian Jews among others (Acts 6:9), suggesting a community large enough to maintain separate worship facilities.</p><p>Simon of Cyrene — a man from Cyrene who happened to be coming from the country — was compelled by Roman soldiers to carry Jesus's cross when Jesus was unable to continue bearing it on the way to Golgotha (Matthew 27:32; Mark 15:21; Luke 23:26). Mark's identification of Simon as the father of Alexander and Rufus suggests his family was known to Mark's readers, possibly the Rufus greeted by Paul in Romans 16:13. A Cyrenian named Lucius is listed among the prophets and teachers at Antioch who sent out Barnabas and Saul on the first missionary journey (Acts 13:1).</p>",
        "hitchcock_meaning": "a wall; coldness; the floor",
        "source_ids": {"easton": "cyrene", "smith": "cyrene", "isbe": "cyrene"},
        "key_refs": ["Matthew 27:32", "Acts 2:10", "Acts 6:9", "Acts 13:1"]
    },
    "cyrenius": {
        "id": "cyrenius",
        "term": "Cyrenius",
        "category": "people",
        "intro": "<p>Cyrenius is the Greek form of the Roman name Publius Sulpicius Quirinius, a Roman senator and military commander who served as governor of Syria. He is mentioned in Luke 2:2 in connection with the census that brought Joseph and Mary to Bethlehem: <em>This was the first enrolment made when Quirinius was governor of Syria.</em> A well-documented census under Quirinius is dated to A.D. 6–7, which appears to be after Herod the Great's death, creating a chronological difficulty that has generated considerable scholarly discussion.</p><p>Proposed resolutions include the possibility of an earlier census or enrollment during a prior period of Quirinius's administrative influence in Syria, a translation of the Greek that reads the passage as <em>before Quirinius was governor</em>, or other interpretive approaches. Whatever the precise historical reconstruction, Luke's reference to Cyrenius is clearly intended to ground the birth of Jesus in datable Roman imperial history — the same purpose served by the synchronism with Caesar Augustus's decree and the subsequent dating to Tiberius's reign at the beginning of Jesus's ministry (Luke 3:1).</p>",
        "hitchcock_meaning": "who governs",
        "source_ids": {"easton": "cyrenius", "smith": "cyrenius", "isbe": "cyrenius"},
        "key_refs": ["Luke 2:2"]
    },
    "cyrus": {
        "id": "cyrus",
        "term": "Cyrus",
        "category": "people",
        "intro": "<p>Cyrus II (meaning in Old Persian <em>the sun</em> or <em>the shepherd</em>; Hebrew renders it as <em>Ko'resh</em>) was the founder of the Achaemenid Persian Empire and the conqueror of Babylon in 539 B.C. His capture of Babylon — described in Daniel 5:30–31 and corroborated by the Cyrus Cylinder discovered in 1879 — ended the Neo-Babylonian Empire and transferred sovereignty over the ancient Near East to Persia. In his first year, Cyrus issued a decree permitting the Jewish exiles to return to their land and rebuild the temple (Ezra 1:1–4; 2 Chronicles 36:22–23), a policy of religious tolerance consistent with what the Cyrus Cylinder reveals of his general approach to conquered peoples' religions.</p><p>Most remarkably, Isaiah 44:28 and 45:1 name Cyrus by name as the one whom the LORD would call as his shepherd to perform his pleasure and rebuild Jerusalem — prophecies written approximately 150 years before Cyrus's birth. Isaiah 45:1 addresses Cyrus as the LORD's anointed (<em>mashiach</em>), applying to a foreign king the category normally reserved for Israel's kings and priests, because God would use him to accomplish his redemptive purposes for his people. The Ezra narrative presents Cyrus's decree as the direct fulfillment of Jeremiah's prophecy of a seventy-year exile (Jeremiah 25:11; 29:10).</p>",
        "hitchcock_meaning": "as miserable; as heir",
        "source_ids": {"easton": "cyrus", "smith": "cyrus", "isbe": "cyrus"},
        "key_refs": ["Ezra 1:1", "Isaiah 44:28", "Isaiah 45:1", "Daniel 5:30"]
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
    print(f'BP c4: Corinthians, Second Epistle → Cyrus: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
