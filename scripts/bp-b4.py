"""
BP Article Synthesis — b4: Blind → By-word
Covers Easton entries: Blind through By-word (70 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Script: scripts/bp-b4.py
Run: python3 scripts/bp-b4.py
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
    "blind": {
        "id": "blind",
        "term": "Blind",
        "category": "concepts",
        "intro": "<p>Blindness in Scripture is treated both as a physical condition and as a powerful spiritual metaphor. Blind beggars appear frequently in the Gospels, often at city gates and roadsides, dependent on charity in a society that had no provision for those unable to work (Matt. 9:27; 20:30; John 5:3). The Mosaic law specifically forbade mistreating the blind and placing stumbling blocks before them (Lev. 19:14; Deut. 27:18), and the prophets included restoration of sight among the signs of the messianic age (Isa. 35:5; 42:7).</p><p>Jesus&#39; healing of the blind is one of the most prominent categories of his miraculous ministry, and the Fourth Gospel develops the healing of the man born blind (John 9) as an extended meditation on spiritual sight and blindness. Paul uses blindness as a metaphor for the spiritual condition of those who do not perceive the gospel (2 Cor. 4:4), and the Laodicean church is rebuked for not recognizing its own spiritual blindness (Rev. 3:17). The consistent biblical movement is from physical blindness toward the deeper blindness of unbelief, overcome by the light of divine revelation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "blind"},
        "key_refs": ["Matthew 9:27", "Matthew 20:30", "Isaiah 35:5", "John 9:1"],
        "sections": []
    },
    "blood": {
        "id": "blood",
        "term": "Blood",
        "category": "concepts",
        "intro": "<p>Blood occupies a uniquely sacred place in biblical theology. The Mosaic law prohibited the consumption of blood on the grounds that &#8220;the life of the flesh is in the blood,&#8221; and God has given it for the altar to make atonement (Lev. 17:11). This prohibition, rooted in the Noahic covenant (Gen. 9:4), applied to Israel and to resident foreigners alike, and was maintained as a minimal requirement for Gentile believers in the Jerusalem decree of Acts 15:20. The priestly rituals of the tabernacle and temple assigned blood the central role in the atoning sacrificial system: blood applied to the altar covered the sin of the offerer.</p><p>In the New Testament, the blood of Christ becomes the supreme fulfillment of all that the sacrificial blood foreshadowed. The Epistle to the Hebrews argues systematically that while animal blood could not truly remove sin (Heb. 10:4), the blood of Jesus&#8212;offered once for all as the perfect high priest and sacrifice&#8212;effects genuine cleansing of conscience and permanent access to God (Heb. 9:12&#8211;14). The Lord&#39;s Supper institutes the cup as a covenant in Christ&#39;s blood (1 Cor. 11:25; Luke 22:20), and the letters of John and Peter ground Christian cleansing and redemption in his blood (1 John 1:7; 1 Pet. 1:19).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "blood", "smith": "blood", "isbe": "blood"},
        "key_refs": ["Leviticus 17:11", "Genesis 9:4", "Hebrews 9:12", "1 John 1:7"],
        "sections": []
    },
    "bloody-sweat": {
        "id": "bloody-sweat",
        "term": "Bloody Sweat",
        "category": "events",
        "intro": "<p>Bloody sweat is the phenomenon described in Luke 22:44, where Jesus in Gethsemane, in a state of extreme agony, prayed more earnestly and &#8220;his sweat became like great drops of blood falling down to the ground.&#8221; The medical term for this rare condition is hematidrosis or hemohidrosis, in which extreme emotional distress causes the rupture of capillaries adjacent to sweat glands, allowing blood to mix with perspiration. The verse is attested in the major manuscript traditions, though it is absent from a small number of witnesses.</p><p>The theological significance of the Gethsemane agony is substantial: it reveals the full humanity of Jesus as he faced the weight of the suffering and divine abandonment that the cross entailed. The bloody sweat underscores that the Passion was not simply physical execution but a profound spiritual ordeal. Hebrews 5:7 alludes to this moment in describing Jesus&#39; &#8220;prayers and supplications, with loud cries and tears, to him who was able to save him from death,&#8221; emphasizing that his priestly sympathy with human weakness was forged in genuine suffering.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bloody-sweat", "isbe": "bloody-sweat"},
        "key_refs": ["Luke 22:44", "Hebrews 5:7"],
        "sections": []
    },
    "blot": {
        "id": "blot",
        "term": "Blot",
        "category": "concepts",
        "intro": "<p>Blot in Scripture carries two primary senses: a moral stain or reproach (Job 31:7; Prov. 9:7), and the divine act of erasure, either of sin in forgiveness or of a person&#39;s name from the book of life in judgment. The Hebrew <em>mum</em> denotes a physical or moral blemish, while the verb &#8220;to blot out&#8221; (<em>machah</em>) is used both for the forgiveness of sin&#8212;&#8220;blot out my transgressions&#8221; (Ps. 51:1, 9)&#8212;and for the removal of a name from God&#39;s record (Ex. 32:32&#8211;33).</p><p>Isaiah 44:22 uses the metaphor of a cloud dispersed: &#8220;I have blotted out your transgressions like a cloud and your sins like mist.&#8221; This positive sense of blotting&#8212;complete removal of the record of sin&#8212;is taken up in Colossians 2:14, where Paul declares that the written record of debt against us has been &#8220;cancelled&#8221; (literally, &#8220;blotted out&#8221;) and nailed to the cross. The contrasting negative use&#8212;having one&#39;s name blotted from the book of life (Rev. 3:5)&#8212;implies the ultimate consequence of apostasy and unbelief.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "blot", "isbe": "blot"},
        "key_refs": ["Psalms 51:1", "Isaiah 44:22", "Colossians 2:14", "Revelation 3:5"],
        "sections": []
    },
    "blue": {
        "id": "blue",
        "term": "Blue",
        "category": "concepts",
        "intro": "<p>Blue was one of the three principal colors used in the tabernacle and priestly vestments, consistently listed alongside purple and scarlet in the Mosaic instructions (Ex. 25:4; 26:1, 31, 36; 28:5&#8211;6). The Hebrew <em>tekhelet</em> designates a shade ranging from sky-blue to violet, produced from a dye derived from a marine creature&#8212;likely the Murex trunculus snail&#8212;making it an expensive and prestigious color. The tekhelet cord was incorporated into the fringes (tzitzit) that Israelites were commanded to wear as a reminder of the commandments (Num. 15:38&#8211;40).</p><p>Blue appears throughout the sacred furnishings: the high priest&#39;s robe was entirely of blue (Ex. 28:31), the ark, table, lampstand, and altars were covered with blue cloth when transported through the wilderness (Num. 4:6&#8211;12), and blue thread was woven into the curtains and veils of the sanctuary. The association of blue with priestly dignity and divine presence made it a color of particular sacred significance in the Israelite cult, distinguishing holy objects and holy persons from common use.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "blue"},
        "key_refs": ["Exodus 25:4", "Exodus 28:31", "Numbers 15:38"],
        "sections": []
    },
    "boanerges": {
        "id": "boanerges",
        "term": "Boanerges",
        "category": "people",
        "intro": "<p>Boanerges, meaning <em>sons of thunder</em>, was the surname given by Jesus to the brothers James and John, sons of Zebedee (Mark 3:17). The Aramaic original (<em>bene reghesh</em>) suggests a stormy, vehement temperament, illustrated most vividly when the brothers asked Jesus for permission to call down fire from heaven on a Samaritan village that refused them hospitality (Luke 9:54). The nickname reflects the impetuous character James and John displayed throughout the Synoptic tradition.</p><p>Despite this characterization, both men underwent profound transformation through their association with Jesus. James became the first apostle martyred, executed by Herod Agrippa around A.D. 44 (Acts 12:2). John, the &#8220;son of thunder,&#8221; became the apostle preeminently associated with love in the Johannine tradition, and his first letter&#8212;written in old age&#8212;is permeated with the theme of love as the defining mark of genuine faith in Christ. The contrast between the nickname and John&#39;s later identity is itself a testament to the transforming power of discipleship.</p>",
        "hitchcock_meaning": "son of thunder",
        "source_ids": {"easton": "boanerges", "smith": "boanerges", "isbe": "boanerges"},
        "key_refs": ["Mark 3:17", "Luke 9:54", "Acts 12:2"],
        "sections": []
    },
    "boar": {
        "id": "boar",
        "term": "Boar",
        "category": "concepts",
        "intro": "<p>The boar (wild pig) appears in Scripture only in Psalm 80:13, where the afflicted nation is compared to a vineyard ravaged: &#8220;The boar from the forest ravages it, and all that move in the field feed on it.&#8221; The Hebrew <em>chazir</em> is elsewhere translated &#8220;swine,&#8221; referring to the domestic and wild pig alike. Wild boars were common in the forests and marshes of ancient Palestine, and their destructive rooting in cultivated fields made them a fitting image for the thorough devastation of an enemy invasion.</p><p>Swine were classified as unclean under the Levitical dietary law (Lev. 11:7; Deut. 14:8), making the boar doubly threatening in the psalm&#39;s imagery&#8212;an unclean beast desecrating what was meant to be holy and fruitful. Proverbs 11:22 uses a gold ring in a swine&#39;s snout as an image of misplaced beauty, and Isaiah 65:4 lists eating swine&#39;s flesh among the abominations of the apostate. The wild boar of Psalm 80 has been interpreted historically as a symbol of specific foreign aggressors, though the metaphorical force is independent of any single historical referent.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "boar", "isbe": "boar"},
        "key_refs": ["Psalms 80:13", "Leviticus 11:7"],
        "sections": []
    },
    "boaz": {
        "id": "boaz",
        "term": "Boaz",
        "category": "people",
        "intro": "<p>Boaz, whose name means <em>in strength</em> or <em>fleetness</em>, was a wealthy Bethlehemite landowner and a kinsman of Elimelech, the husband of Naomi. His story unfolds in the book of Ruth, where he fulfills the role of kinsman-redeemer (<em>go&#39;el</em>) by marrying the widowed Moabite Ruth and redeeming the property of Naomi&#39;s deceased husband. His first act of kindness was permitting Ruth to glean in his fields and instructing his workers to leave extra grain for her, motivated by his knowledge of her loyalty to Naomi and his reverence for Yahweh&#39;s care for the vulnerable.</p><p>Boaz appears in the genealogy of David (Ruth 4:21&#8211;22) and subsequently in the messianic lineage of Jesus Christ (Matt. 1:5). His role as kinsman-redeemer has made him a prominent type of Christ in Christian interpretation: as Boaz redeemed Ruth by paying the required price and taking the foreign widow as his bride, so Christ redeems his people at cost to himself and unites them to himself. One of the two bronze pillars of Solomon&#39;s temple was also called Boaz (1 Kings 7:21; 2 Chr. 3:17).</p>",
        "hitchcock_meaning": "or Booz, in strength",
        "source_ids": {"easton": "boaz", "smith": "boaz", "isbe": "boaz"},
        "key_refs": ["Ruth 4:1", "Ruth 4:21", "Matthew 1:5", "1 Kings 7:21"],
        "sections": []
    },
    "bochim": {
        "id": "bochim",
        "term": "Bochim",
        "category": "places",
        "intro": "<p>Bochim, meaning <em>weepers</em>, was a place west of Jordan, above Gilgal, where the angel of the LORD appeared to the Israelites early in the period of the judges and rebuked them for failing to destroy the Canaanite altars and for making covenants with the inhabitants of the land (Judg. 2:1&#8211;5). The people wept aloud at the divine rebuke&#8212;hence the name&#8212;and offered sacrifices there. The episode stands as a programmatic explanation of the cycle of apostasy and oppression that characterizes the entire book of Judges.</p><p>The precise location of Bochim is uncertain; the Septuagint renders the name as &#8220;the place of weeping&#8221; rather than preserving it as a proper noun, suggesting the name was understood as descriptive rather than a fixed toponym. Some scholars identify it with Bethel. The appearance of the divine messenger at Bochim serves as a hinge point in the narrative of Joshua&#8211;Judges, marking the transition from the conquest era to the darker period of tribal fragmentation and religious compromise that follows.</p>",
        "hitchcock_meaning": "the place of weeping; or of mulberry-trees",
        "source_ids": {"easton": "bochim", "smith": "bochim", "isbe": "bochim"},
        "key_refs": ["Judges 2:1", "Judges 2:5"],
        "sections": []
    },
    "boil": {
        "id": "boil",
        "term": "Boil",
        "category": "concepts",
        "intro": "<p>Boil (rendered &#8220;botch&#8221; in the King James Version of Deut. 28:27, 35) refers to a severe skin ulcer or abscess. The sixth plague of Egypt consisted of boils breaking out on both humans and animals (Exod. 9:9&#8211;11), and the Mosaic covenant threatened boils among the covenant curses for disobedience (Deut. 28:27, 35). The most famous biblical boil is that afflicting Hezekiah during his near-fatal illness, treated on Isaiah&#39;s instruction with a poultice of figs that was applied to the boil, after which the king recovered (2 Kings 20:7; Isa. 38:21).</p><p>Job is afflicted with &#8220;loathsome sores from the sole of his foot to the crown of his head&#8221; (Job 2:7)&#8212;likely a severe skin disease involving painful sores&#8212;which he scrapes with a potsherd. The connection between disease and divine judgment or testing is woven through the biblical accounts of boils, while the healing narratives of Hezekiah and, in the New Testament, of various lepers and the sick, demonstrate God&#39;s power to restore what affliction has broken.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "boil"},
        "key_refs": ["Exodus 9:9", "Deuteronomy 28:27", "2 Kings 20:7", "Job 2:7"],
        "sections": []
    },
    "bolled": {
        "id": "bolled",
        "term": "Bolled",
        "category": "concepts",
        "intro": "<p>Bolled is an archaic English term found only in Exodus 9:31 (King James Version), describing the state of the flax and barley crops at the time of the seventh plague of Egypt: &#8220;the barley was in the ear, and the flax was bolled&#8221;&#8212;that is, the flax had formed its seed pods and was approaching harvest. The Hebrew <em>gibh&#39;ol</em> means &#8220;the calyx of flowers,&#8221; indicating blossoming or budding. Modern translations render it &#8220;in bloom&#8221; or &#8220;in bud.&#8221;</p><p>The agricultural detail is significant for dating the plagues within the Egyptian agricultural year: barley ripens in Egypt around March and flax somewhat earlier, placing the plague of hail in late winter. The wheat and spelt, not yet &#8220;bolled,&#8221; survived the hail and were harvested later. This precision reflects the narrative&#39;s interest in historical plausibility and provides incidental data about Egyptian agricultural practices that modern archaeology has confirmed.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bolled", "isbe": "bolled"},
        "key_refs": ["Exodus 9:31"],
        "sections": []
    },
    "bolster": {
        "id": "bolster",
        "term": "Bolster",
        "category": "concepts",
        "intro": "<p>Bolster is the King James Version rendering of the Hebrew <em>kebir</em> in 1 Samuel 19:13, 16, where Michal placed a household idol (teraphim) in David&#39;s bed with a bolster of goat&#39;s hair at its head to deceive Saul&#39;s messengers into thinking David was still abed. The word describes a cylindrical pillow or head-covering. In 1 Samuel 26, the &#8220;bolster&#8221; (more precisely, the area &#8220;at his head&#8221;) of Saul&#39;s sleeping form marks the location of his spear and water jug, which David took as proof that he had been within reach of the king yet spared his life.</p><p>The item in 1 Samuel 19 is more accurately translated &#8220;a quilt of goat&#39;s hair&#8221; (so the Revised Version marginal reading), used to simulate the head of a sleeping man. The episode is one of several in the David narratives where disguise and deception serve providential ends, and Michal&#39;s stratagem allowed David to escape what would have been his death had Saul&#39;s servants arrived earlier.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bolster", "isbe": "bolster"},
        "key_refs": ["1 Samuel 19:13", "1 Samuel 26:7", "1 Samuel 26:11"],
        "sections": []
    },
    "bond": {
        "id": "bond",
        "term": "Bond",
        "category": "concepts",
        "intro": "<p>Bond in Scripture denotes any binding obligation or restraint. In the legal context of Numbers 30, a bond (<em>issar</em>) is a vow or sworn commitment by which a person binds himself or herself to a course of action; the passage governs the circumstances under which a father or husband may annul a woman&#39;s vow. The word carries a related sense of physical imprisonment or oppression (Ps. 116:16; Isa. 52:2), and the Septuagint and New Testament use &#8220;bond&#8221; for the chains and imprisonment Paul and others endured for the gospel (Phil. 1:7, 13, 14; Col. 4:18).</p><p>Paul&#39;s use of &#8220;bonds&#8221; (Greek <em>desmoi</em>) is notable for its transformation of a shameful circumstance into an occasion for witness: his imprisonment had become known throughout the praetorium and was advancing the gospel rather than hindering it (Phil. 1:12&#8211;13). The theological contrast between the bondage of sin and the freedom of Christ is developed throughout Paul&#39;s letters, culminating in the declaration that in Christ there is neither bond nor free (Gal. 3:28; Col. 3:11).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bond"},
        "key_refs": ["Numbers 30:2", "Psalms 116:16", "Philippians 1:13", "Galatians 3:28"],
        "sections": []
    },
    "bondage": {
        "id": "bondage",
        "term": "Bondage",
        "category": "concepts",
        "intro": "<p>Bondage in Scripture refers primarily to Israel&#39;s servitude in Egypt, described as the defining national trauma from which Yahweh redeemed his people (Ex. 2:23&#8211;25; 5:1&#8211;23). Egypt is repeatedly called the &#8220;house of bondage&#8221; in the Decalogue preamble and throughout Deuteronomy (Ex. 13:3; 20:2; Deut. 5:6; 6:12), grounding Israel&#39;s obligation to serve Yahweh alone in the historical fact of his prior redemption. Post-exilic writers apply the same vocabulary to the Babylonian captivity (Ezra 9:8&#8211;9; Isa. 14:3).</p><p>The New Testament develops bondage as a metaphor for the human condition under sin, the law, and demonic oppression. Paul&#39;s contrast in Galatians and Romans between the spirit of slavery leading to fear and the spirit of adoption leading to freedom (Rom. 8:15; Gal. 4:24&#8211;25) draws on the Exodus typology to describe salvation. Hebrews 2:15 speaks of those &#8220;all their lives held in slavery by their fear of death.&#8221; The movement from bondage to freedom through divine redemption is one of the master narratives of both Testaments.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bondage", "isbe": "bondage"},
        "key_refs": ["Exodus 2:23", "Exodus 13:3", "Romans 8:15", "Galatians 4:24"],
        "sections": []
    },
    "bonnet": {
        "id": "bonnet",
        "term": "Bonnet",
        "category": "concepts",
        "intro": "<p>Bonnet is the King James Version rendering of two Hebrew words designating head-coverings worn by priests and, in a different form, by ordinary Israelites. The priestly bonnet (<em>migba&#39;ah</em>) was a linen turban worn by the ordinary priests (Ex. 39:28; Ezek. 44:18), distinct from the high priest&#39;s mitre (<em>mitsnepheth</em>). Both were part of the elaborate garments prescribed for Aaron and his sons &#8220;for glory and for beauty&#8221; (Ex. 28:40). The Revised Version consistently renders the priestly headgear as &#8220;head-tires&#8221; or &#8220;turbans.&#8221;</p><p>The word <em>peer</em>, also rendered bonnet in Isaiah 3:20, refers to an ornamental headdress worn by women and figures in Isaiah&#39;s catalog of luxury ornaments that will be stripped away in judgment. The same root appears in Isaiah 61:3 and 10, where a &#8220;beautiful headdress&#8221; replaces ashes as a symbol of divine restoration. The range of usage&#8212;from priestly vestments to feminine adornment to the garlands of the redeemed&#8212;illustrates the symbolic weight carried by head-coverings in the biblical world.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bonnet", "isbe": "bonnet"},
        "key_refs": ["Exodus 39:28", "Ezekiel 44:18", "Isaiah 61:3"],
        "sections": []
    },
    "book": {
        "id": "book",
        "term": "Book",
        "category": "concepts",
        "intro": "<p>Book in Scripture translates the Hebrew <em>sepher</em> and Greek <em>biblos</em>/<em>biblion</em>, terms that encompass a range of written documents from scrolls and letters to legal records and sacred texts. The first mention of writing in the Bible is the divine command to Moses to record the defeat of Amalek &#8220;in a book&#8221; (Ex. 17:14), followed by Moses&#39; writing of the covenant law (Ex. 24:7). The centrality of the written word to Israelite religion&#8212;from the book of the law deposited beside the ark to the royal copy of Deuteronomy&#8212;distinguishes Israel among ancient Near Eastern cultures in its emphasis on textual preservation of divine revelation.</p><p>Scripture refers to several celestial or divine books: the Book of Life (Ex. 32:32; Phil. 4:3; Rev. 20:12&#8211;15) in which the names of the redeemed are recorded; the books of judgment opened at the last day (Rev. 20:12); and the book of God&#39;s remembrance (Mal. 3:16). Jeremiah&#39;s purchase of a field and the recording of the transaction in two copies&#8212;sealed and open&#8212;(Jer. 32:10&#8211;14) reflects the legal practice of double-document transactions that archaeology has confirmed from the ancient Near East. The Lamb&#39;s book of Revelation (Rev. 5:1) seals the entire sweep of redemptive history.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "book", "isbe": "book"},
        "key_refs": ["Exodus 17:14", "Philippians 4:3", "Revelation 20:12", "Malachi 3:16"],
        "sections": []
    },
    "booth": {
        "id": "booth",
        "term": "Booth",
        "category": "concepts",
        "intro": "<p>Booth designates a temporary shelter constructed from the branches, leaves, and boughs of trees. The Hebrew <em>sukkah</em> (plural <em>sukkoth</em>) appears in Jacob&#39;s construction of shelters for his cattle at the place thereafter named Succoth (Gen. 33:17), and in the Feast of Booths (Sukkot), during which Israel was commanded to dwell in booths for seven days each autumn to commemorate the wilderness wandering (Lev. 23:42&#8211;43). The feast was one of the three great pilgrimage festivals of the Israelite calendar, associated with the ingathering of the harvest at the end of the agricultural year.</p><p>Booths also appear in military contexts as field shelters (2 Sam. 11:11; 1 Kings 20:12, 16) and in the agricultural setting of watchmen&#39;s huts in vineyards and fields (Isa. 1:8; Job 27:18). The fragility and impermanence of the sukkah gave it theological resonance as a reminder of Israel&#39;s dependence on God during the wilderness years. Zechariah 14:16&#8211;19 envisions the nations streaming to Jerusalem to keep the Feast of Booths in the age to come, giving the feast eschatological dimensions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "booth", "isbe": "booth"},
        "key_refs": ["Genesis 33:17", "Leviticus 23:42", "Leviticus 23:43"],
        "sections": []
    },
    "booty": {
        "id": "booty",
        "term": "Booty",
        "category": "concepts",
        "intro": "<p>Booty designates the spoils of war: captives, livestock, and valuables seized from a defeated enemy. Mosaic law regulated the distribution of booty carefully: in wars against distant nations not subject to the <em>cherem</em> (ban), Israel could take women, children, livestock, and goods as plunder; in wars against the Canaanites, however, all living things were to be devoted to destruction (Deut. 20:14&#8211;17). The spoil taken from Midian (Num. 31:25&#8211;47) provides a detailed example of the division process: half to the warriors, half to the congregation, with a levy for the priests and Levites from each share.</p><p>David established a precedent that those who remained with the supplies shared equally in booty with those who went into battle, a ruling that became a statute in Israel (1 Sam. 30:24&#8211;25). Violations of the cherem ban, as in Achan&#39;s taking of devoted Canaanite goods (Josh. 7), brought catastrophic consequences. The imagery of God distributing the spoils of spiritual victory appears in Psalm 68:12 and Isaiah 53:12, where the Servant is said to divide the booty with the strong after pouring out his soul to death.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "booty", "smith": "booty", "isbe": "booty"},
        "key_refs": ["Deuteronomy 20:14", "Numbers 31:26", "1 Samuel 30:24", "Isaiah 53:12"],
        "sections": []
    },
    "borrow": {
        "id": "borrow",
        "term": "Borrow",
        "category": "concepts",
        "intro": "<p>Borrowing in the Old Testament was regulated by the covenant community&#39;s obligations of mutual care. The law prohibited charging interest on loans to fellow Israelites (Ex. 22:25; Lev. 25:36&#8211;37; Deut. 23:19&#8211;20), and Deuteronomy 15:6 envisioned Israel as a lending rather than borrowing nation, enjoying covenant blessing. Psalm 37:21 identifies the wicked as those who borrow and do not repay, contrasting them with the righteous who are generous and give.</p><p>The most significant biblical &#8220;borrowing&#8221; episode is Israel&#39;s request of the Egyptians for silver, gold, and clothing upon the Exodus (Ex. 12:35&#8211;36). The Hebrew verb (<em>sha&#39;al</em>) more precisely means &#8220;to ask&#8221; rather than &#8220;to borrow with intent to repay,&#8221; and the Revised Version renders it accordingly. This transaction, understood as God&#39;s provision of back-wages from their Egyptian masters after generations of unpaid labor, fulfilled the promise made to Abraham that his descendants would leave their place of affliction with great possessions (Gen. 15:14).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "borrow"},
        "key_refs": ["Exodus 12:35", "Exodus 22:25", "Deuteronomy 15:6", "Psalms 37:21"],
        "sections": []
    },
    "bosom": {
        "id": "bosom",
        "term": "Bosom",
        "category": "concepts",
        "intro": "<p>Bosom in Scripture functions as both a literal and figurative term. Literally, the fold of the garment at the chest served as a pocket for carrying objects in Eastern dress (Prov. 17:23; Isa. 65:6&#8211;7). To &#8220;carry in one&#39;s bosom&#8221; expressed close personal affection and protective care: the image of a shepherd carrying lambs in his bosom (Isa. 40:11) and Moses&#39; complaint about bearing the people &#8220;as a nursing father carries the nursing child&#8221; (Num. 11:12) both draw on this intimacy.</p><p>The phrase &#8220;Abraham&#39;s bosom&#8221; in Luke 16:22&#8211;23 designates the place of comfort where Lazarus rested after death, reclining in the place of honor at Abraham&#39;s side&#8212;a metaphor for the blessed state of the righteous departed drawn from the banquet imagery of guests reclining together. John 1:18 applies the same image to the unique relationship between the eternal Son and the Father: Jesus is &#8220;the only-begotten Son, who is in the bosom of the Father,&#8221; indicating perfect intimacy and mutual knowledge that grounds the Son&#39;s capacity to make the Father known.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bosom", "isbe": "bosom"},
        "key_refs": ["John 1:18", "Luke 16:22", "Isaiah 40:11", "Numbers 11:12"],
        "sections": []
    },
    "bosor": {
        "id": "bosor",
        "term": "Bosor",
        "category": "people",
        "intro": "<p>Bosor is the Chaldee or Aramaic form of the name Beor, used in 2 Peter 2:15 where the apostle describes false teachers as those who &#8220;have followed the way of Balaam, the son of Bosor, who loved gain from wrongdoing.&#8221; Beor (Bosor) was the father of Balaam the prophet-for-hire from Pethor, who was hired by Balak king of Moab to curse Israel during the wilderness period (Num. 22&#8211;24; Deut. 23:4).</p><p>Peter&#39;s use of the Aramaic form Bosor rather than the Hebrew Beor may reflect a Palestinian Aramaic pronunciation current in his day, or it may represent a wordplay on the Hebrew <em>basar</em> (flesh), emphasizing Balaam&#39;s carnal motivation. Jude 11 similarly cites Balaam as an example of greed-driven apostasy, and Revelation 2:14 refers to the &#8220;teaching of Balaam&#8221; as a designation for the compromise of Christian integrity for financial gain&#8212;giving the name Balaam lasting currency as a symbol of mercenary religious influence.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bosor", "smith": "bosor", "isbe": "bosor"},
        "key_refs": ["2 Peter 2:15", "Numbers 22:5", "Jude 1:11", "Revelation 2:14"],
        "sections": []
    },
    "bosses": {
        "id": "bosses",
        "term": "Bosses",
        "category": "concepts",
        "intro": "<p>Bosses refers to the convex projecting knobs or studs on the front of a shield (Job 15:26), used both to deflect blows and as decorative reinforcement. The Hebrew word implies roundness or convexity. In Job 15:26, Eliphaz describes the wicked man as one who runs at God &#8220;with outstretched neck, with his thick-bossed shields&#8221;&#8212;an image of reckless, armor-clad defiance against divine authority. The thick bosses suggest a particularly heavy or reinforced shield, emphasizing the arrogance of the posture rather than its practical military value against an omnipotent God.</p><p>Ancient shields ranged from small round bucklers to large body-length shields, and many were decorated with metal bosses. Egyptian, Assyrian, and Canaanite shields all show examples of such reinforced projections in artistic representations. The poetic use in Job captures the visual image of an adversary approaching in full martial readiness, oblivious to the futility of armed defiance against the Creator.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bosses"},
        "key_refs": ["Job 15:26"],
        "sections": []
    },
    "botch": {
        "id": "botch",
        "term": "Botch",
        "category": "concepts",
        "intro": "<p>Botch is an archaic English word used in Deuteronomy 28:27, 35 (King James Version) for a severe skin disease listed among the covenant curses: &#8220;The LORD will strike you with the boils of Egypt, and with tumors and the scab and the itch, of which you cannot be healed&#8221; (Deut. 28:27). The same Hebrew word is rendered &#8220;boil&#8221; in the account of the sixth Egyptian plague (Ex. 9:9&#8211;11), making the threatened disease explicitly a reversal of the Exodus: the plagues that afflicted Egypt will now afflict a disobedient Israel.</p><p>The Revised Version replaces &#8220;botch&#8221; with &#8220;boil&#8221; throughout, reflecting the word&#39;s obsolescence in modern English. The covenant curse structure of Deuteronomy 28 presents disease not merely as natural misfortune but as a direct consequence of covenant violation, an extension of the principle that blessing flows from obedience and judgment from apostasy. The explicit reference to the &#8220;boils of Egypt&#8221; ties the curse to the memory of the Exodus, warning that God who once struck Egypt&#39;s oppressors is capable of striking his own people if they become similarly defiant.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "botch"},
        "key_refs": ["Deuteronomy 28:27", "Deuteronomy 28:35", "Exodus 9:9"],
        "sections": []
    },
    "bottle": {
        "id": "bottle",
        "term": "Bottle",
        "category": "concepts",
        "intro": "<p>Bottles in the ancient biblical world were most commonly made from the skins of goats or other animals, sewn into watertight containers with the neck of the animal serving as the opening. The Gibeonites carried old, cracked wineskins as evidence of a long journey (Josh. 9:4, 13), and David received a skin of wine from Jesse when sent to Saul (1 Sam. 16:20). Clay vessels also served as bottles for water and other liquids, and the Hebrew <em>baqbuq</em> (probably onomatopoeic for the gurgling sound) designates an earthenware flask (Jer. 19:1, 10).</p><p>Jesus&#39; parable of new wine in old wineskins (Matt. 9:17; Mark 2:22; Luke 5:37&#8211;38) uses the familiar limitation of leather bottles&#8212;which lose elasticity with age and burst under the expansion of fermenting wine&#8212;to illustrate the incompatibility of the new order of the kingdom with the rigid structures of the old. The &#8220;bottle in the smoke&#8221; of Psalm 119:83 describes a parched, shriveled wineskin, an image of exhaustion and affliction. Job 32:19 compares his need to speak to new wineskins about to burst.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bottle", "smith": "bottle", "isbe": "bottle"},
        "key_refs": ["Joshua 9:4", "Matthew 9:17", "Psalms 119:83", "Jeremiah 19:1"],
        "sections": []
    },
    "bow": {
        "id": "bow",
        "term": "Bow",
        "category": "concepts",
        "intro": "<p>The bow was the preeminent long-range weapon of the ancient world and appears throughout the biblical narrative from the patriarchal period onward (Gen. 21:20; 27:3). Composite bows constructed of wood, horn, and sinew were capable of considerable range and penetrating power; the tribe of Benjamin was particularly renowned for its archers, some of whom could shoot with either hand (1 Chr. 8:40; 12:2). Bowing in salutation&#8212;kneeling on one knee with the body inclined forward&#8212;was the standard Eastern mode of showing respect, as illustrated repeatedly in the patriarchal narratives (Gen. 33:3; 43:28).</p><p>The bow carries rich symbolic weight in Scripture. The rainbow is the sign of God&#39;s covenant with Noah (Gen. 9:13&#8211;16). The breaking of a bow symbolizes military defeat and the end of warfare (Ps. 46:9; Hos. 1:5; Jer. 49:35), while the gift of a &#8220;bow of bronze&#8221; in David&#39;s victory psalm (2 Sam. 22:35; Ps. 18:34) signifies divine empowerment for battle. Jonathan&#39;s bow, lamented in David&#39;s elegy, &#8220;turned not back&#8221; in battle (2 Sam. 1:22)&#8212;a tribute to the fallen warrior&#39;s consistent courage.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bow"},
        "key_refs": ["Genesis 21:20", "Genesis 9:13", "Psalms 46:9", "2 Samuel 22:35"],
        "sections": []
    },
    "bowels": {
        "id": "bowels",
        "term": "Bowels",
        "category": "concepts",
        "intro": "<p>Bowels in Scripture function as the seat of deep emotional feeling, particularly compassion and tender affection. The Hebrew <em>me&#39;im</em> and the Greek <em>splagchna</em> (literally &#8220;entrails&#8221;) are used in both testaments to describe the inner emotional center from which compassion flows. Paul appeals to Philemon in terms of &#8220;bowels of mercies&#8221; (Phil. 1:8; Philem. 7, 12, 20 KJV), translated in modern versions as &#8220;heart&#8221; or &#8220;affection.&#8221; The Revised Version consistently renders <em>splagchna</em> as &#8220;tender mercies&#8221; or &#8220;compassion.&#8221;</p><p>The expression &#8220;bowels of mercies&#8221; in Colossians 3:12 is part of a list of virtues to be &#8220;put on&#8221; as the garments of the new humanity in Christ: compassion, kindness, humility, meekness, and patience. The physical metaphor reflects the ancient understanding that strong emotion was felt in the abdomen, a recognition of the embodied nature of human emotional life that the biblical languages preserve. In modern translation this visceral language is often softened, but its original force communicates the depth and physicality of the compassion being described.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bowels", "isbe": "bowels"},
        "key_refs": ["Philippians 1:8", "Colossians 3:12", "Philemon 1:7"],
        "sections": []
    },
    "bowing": {
        "id": "bowing",
        "term": "Bowing",
        "category": "concepts",
        "intro": "<p>Bowing as a gesture of respect, worship, or submission appears throughout Scripture in a variety of social and religious contexts. Abraham bowed to the people of the land when negotiating for Sarah&#39;s burial place (Gen. 23:7); Jacob bowed seven times before Esau as a sign of submission and reconciliation (Gen. 33:3); and Joseph&#39;s brothers bowed before him, unconsciously fulfilling his earlier dreams (Gen. 43:28). The bow was the standard Near Eastern gesture of respect toward superiors, kings, and gods alike.</p><p>The religious prohibition on bowing before idols or foreign gods (Ex. 20:5; 23:24) gave the gesture a deeply theological dimension: bowing was an act of acknowledgment of authority and worth, reserved for God alone in the context of worship. Naaman&#39;s request for permission to bow in the house of Rimmon when accompanying his master (2 Kings 5:18) illustrates the tension between political obligation and religious loyalty. Psalm 95:6 invites Israel to &#8220;bow down and kneel before the LORD our Maker,&#8221; and Philippians 2:10 extends this universal homage eschatologically to every knee bowing at the name of Jesus.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bowing"},
        "key_refs": ["Genesis 23:7", "Genesis 33:3", "Psalms 95:6", "Philippians 2:10"],
        "sections": []
    },
    "bowl": {
        "id": "bowl",
        "term": "Bowl",
        "category": "concepts",
        "intro": "<p>Bowl translates several Hebrew terms in the Old Testament, applied to a range of vessels from the ornamental cups of the tabernacle lampstand to large ceremonial basins. The Hebrew <em>gullah</em> designates the oil reservoirs of the golden lampstand (Ex. 25:31&#8211;34; Zech. 4:2), while <em>mizraq</em> refers to the large basins used to receive and sprinkle sacrificial blood at the altar. The golden bowls (&#8220;vials&#8221;) of Revelation 5:8 contain the prayers of the saints, and the seven bowls of God&#39;s wrath (Rev. 15&#8211;16) are poured out in the final sequence of plagues.</p><p>Amos 6:6 condemns those who &#8220;drink wine in bowls&#8221; as a sign of luxurious indulgence while being indifferent to the ruin of Joseph&#8212;the oversized bowl replacing the modest cup as a symbol of excess. Zechariah 9:15 envisions the victorious people of God &#8220;full like a bowl, drenched like the corners of the altar.&#8221; The bowl&#39;s ritual associations&#8212;with sacrifice, oil, and wine&#8212;gave it a sacramental resonance across the range of biblical contexts in which it appears.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bowl", "isbe": "bowl"},
        "key_refs": ["Exodus 25:31", "Amos 6:6", "Revelation 5:8", "Zechariah 4:2"],
        "sections": []
    },
    "box": {
        "id": "box",
        "term": "Box",
        "category": "concepts",
        "intro": "<p>Box in the King James Version refers to a small flask or vial for holding anointing oil or perfume (Mark 14:3; 2 Kings 9:1; 1 Sam. 10:1). The Greek <em>alabastron</em> in Mark 14:3 designates an alabaster flask, sealed at the neck and typically broken open to release the contents&#8212;hence the woman&#39;s act of breaking the flask before pouring the costly ointment over Jesus&#39; head. This alabaster container was a standard vessel for expensive perfumes in the Greco-Roman world, its impermeable stone preserving the fragrance.</p><p>The Hebrew <em>pakh</em> in 1 Samuel 10:1 and 2 Kings 9:1, 3 designates a small flask or cruse from which the prophet pours oil over the head of the person being anointed king. Samuel anoints Saul with such a flask (1 Sam. 10:1), and the young prophet sent by Elisha uses one to anoint Jehu in the inner chamber (2 Kings 9:1&#8211;6). The act of breaking or pouring from these small containers was thus associated with the most solemn acts of royal anointing and, in the Gospel account, with the woman&#39;s extravagant act of devotion.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "box"},
        "key_refs": ["Mark 14:3", "1 Samuel 10:1", "2 Kings 9:1"],
        "sections": []
    },
    "box-tree": {
        "id": "box-tree",
        "term": "Box-tree",
        "category": "concepts",
        "intro": "<p>Box-tree appears in Isaiah 41:19 and 60:13 (King James Version) as the translation of the Hebrew <em>te&#39;ashshur</em>, one of several trees promised to appear in the transformed wilderness as signs of divine restoration. Modern translations render it variously as &#8220;cypress,&#8221; &#8220;box,&#8221; or &#8220;pine,&#8221; as the precise identification remains uncertain. Ezekiel 27:6 uses the related term for the fine wood used in the oars of Tyrian ships, suggesting a hard, high-quality timber.</p><p>Isaiah 41:19 lists the box-tree alongside the cedar, acacia, myrtle, olive, fir, and pine as trees God will plant in the desert as a visible sign of his power and purpose: &#8220;that they may see and know, may consider and understand together, that the hand of the LORD has done this.&#8221; Isaiah 60:13 envisions the glory of Lebanon&#8212;its cedars, firs, and box-trees&#8212;coming to beautify the sanctuary of the restored Zion. The repeated clustering of these trees in eschatological restoration passages gives the imagery of flourishing woodland a prophetic and theological depth beyond mere botanical description.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "box-tree", "isbe": "box-tree"},
        "key_refs": ["Isaiah 41:19", "Isaiah 60:13", "Ezekiel 27:6"],
        "sections": []
    },
    "bozrah": {
        "id": "bozrah",
        "term": "Bozrah",
        "category": "places",
        "intro": "<p>Bozrah, meaning <em>fortress</em> or <em>sheepfold</em>, designates two distinct locations in the Old Testament. The more prominent is Bozrah of Edom, the ancient capital of the Edomite kingdom, located in the region of modern Jordan. It was the city of Jobab son of Zerah, one of the early Edomite kings (Gen. 36:33). Isaiah, Jeremiah, and Amos all cite Bozrah as the symbol of Edom&#39;s power and the focus of divine judgment against that nation (Isa. 34:6; 63:1; Jer. 49:13; Amos 1:12).</p><p>Isaiah 63:1 contains one of the most vivid prophetic images in Scripture: the divine warrior &#8220;coming from Edom, in crimsoned garments from Bozrah&#8221; after treading the winepress of nations, his garments stained with the blood of divine judgment. Micah 2:12 uses Bozrah as a gathering place for the remnant of Israel, employing the image of sheep in a fold. A second Bozrah, in Moab (Jer. 48:24), was also subject to prophetic judgment. The Edomite Bozrah corresponds to modern Buseirah, excavated by Crystal Bennett in the 1970s.</p>",
        "hitchcock_meaning": "in tribulation or distress",
        "source_ids": {"easton": "bozrah", "smith": "bozrah", "isbe": "bozrah"},
        "key_refs": ["Genesis 36:33", "Isaiah 34:6", "Isaiah 63:1", "Jeremiah 49:13"],
        "sections": []
    },
    "bracelet": {
        "id": "bracelet",
        "term": "Bracelet",
        "category": "concepts",
        "intro": "<p>Bracelets were among the most common ornamental jewelry in the ancient Near East, worn by both men and women on the wrist and arm. In the Old Testament they appear as gifts symbolizing betrothal and social status: Abraham&#39;s servant gave Rebekah a gold bracelet as part of the gifts signaling Isaac&#39;s intention (Gen. 24:22, 30, 47). Women&#39;s bracelets are included among the luxury ornaments Isaiah condemns in his catalog of Judah&#39;s pride (Isa. 3:19), and anklets (<em>&#39;ets&#39;adah</em>) are listed among the spoils brought back from the Midianite war (Num. 31:50).</p><p>The bracelet on Saul&#39;s arm brought to David by the Amalekite claiming to have killed the king (2 Sam. 1:10) was evidently a royal ornament marking his status. In Egyptian and Mesopotamian cultures bracelets carried specific symbolic and votive significance, and the tradition of exchanging bracelets as tokens of covenant or alliance has parallels across the ancient Near East. The lavish bracelets and jewelry described in Ezekiel 16:11 are part of God&#39;s adornment of Jerusalem as his bride&#8212;an image of divine generosity that makes subsequent unfaithfulness all the more culpable.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bracelet", "smith": "bracelet", "isbe": "bracelet"},
        "key_refs": ["Genesis 24:22", "Numbers 31:50", "2 Samuel 1:10", "Ezekiel 16:11"],
        "sections": []
    },
    "bramble": {
        "id": "bramble",
        "term": "Bramble",
        "category": "concepts",
        "intro": "<p>Bramble translates the Hebrew <em>atad</em> in Judges 9:14&#8211;15 and Psalm 58:9, referring to a thorny shrub of the buckthorn family (<em>Rhamnus</em> species) common in Palestine. In Jotham&#39;s fable (Judg. 9:7&#8211;15)&#8212;the oldest fable in the Bible&#8212;the trees seek a king and are rejected by the olive, fig, and vine in succession until they turn to the bramble, which accepts the kingship with a threat: if the trees acted in good faith, let them take shelter in its shade; if not, let fire come out of the bramble and devour the cedars of Lebanon. The fable is a pointed satire on Abimelech&#39;s kingship and the folly of those who chose him.</p><p>The bramble appears elsewhere as a symbol of desolation and wilderness (Isa. 34:13) and of the painful results of wickedness. The contrast between thorns and briers on the one hand and the fruit-bearing vine and fig tree on the other is a recurring biblical motif for distinguishing the life that flourishes under covenant blessing from the barren desolation of judgment (Isa. 5:6; 55:13; Matt. 7:16).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bramble"},
        "key_refs": ["Judges 9:14", "Isaiah 34:13", "Isaiah 55:13"],
        "sections": []
    },
    "branch": {
        "id": "branch",
        "term": "Branch",
        "category": "concepts",
        "intro": "<p>Branch carries both literal and technical messianic significance in the Old Testament. The Hebrew <em>tsemach</em> (&#8220;sprout&#8221; or &#8220;shoot&#8221;) becomes a distinct messianic title in the prophetic literature: Jeremiah promises a &#8220;righteous Branch&#8221; from David&#39;s line who will reign wisely and execute justice (Jer. 23:5; 33:15), Zechariah designates the messianic figure &#8220;the Branch&#8221; who will build the temple of the LORD and bear royal honor (Zech. 3:8; 6:12), and Isaiah&#39;s vision of the restored Davidic shoot from the stump of Jesse (Isa. 11:1&#8211;9) is the foundational text of this imagery.</p><p>Branch also carries figurative weight as a symbol of prosperity (Job 8:16; 15:32) and national strength (Ezek. 17:3, 10; Dan. 11:7). The New Testament develops the vine-and-branches metaphor extensively in John 15:1&#8211;8, where Jesus identifies himself as the true vine and his disciples as branches, with fruitfulness dependent on remaining in him. The corporate dimension&#8212;the branch deriving life from the vine&#8212;becomes a foundational image for understanding the relationship between Christ and the church in Johannine theology.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "branch"},
        "key_refs": ["Jeremiah 23:5", "Zechariah 6:12", "Isaiah 11:1", "John 15:5"],
        "sections": []
    },
    "brass": {
        "id": "brass",
        "term": "Brass",
        "category": "concepts",
        "intro": "<p>Brass in the King James Version consistently mistranslates the Hebrew <em>nechoshet</em> and Greek <em>chalkos</em>, which denote copper or bronze (an alloy of copper and tin) rather than the zinc-based alloy that is modern brass. True brass was not known in antiquity until well into the Christian era. Bronze&#8212;harder and more workable than pure copper&#8212;was the dominant metal of the ancient Near East for weapons, tools, and decorative objects during the Bronze Age. The mountains of Deuteronomy 8:9 from which bronze could be dug refer to the copper deposits of the Arabah and Sinai regions.</p><p>Bronze figures prominently in the tabernacle and temple furnishings: the altar of burnt offering, its utensils, the bronze sea, and the ten lavers in Solomon&#39;s temple were all of cast bronze (Ex. 27:1&#8211;8; 1 Kings 7:13&#8211;46). Armor and weapons of bronze appear throughout the warrior narratives (1 Sam. 17:5&#8211;6; 2 Sam. 22:35). The symbolic use of bronze as a figure for hardness, endurance, or divine power appears in descriptions of the divine warrior (Ezek. 1:7; Rev. 1:15) and in the covenant curses, which threaten that the heavens will become bronze&#8212;withholding rain&#8212;if Israel is disobedient (Deut. 28:23).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "brass", "smith": "brass"},
        "key_refs": ["Deuteronomy 8:9", "Exodus 27:2", "1 Samuel 17:5", "Revelation 1:15"],
        "sections": []
    },
    "bravery": {
        "id": "bravery",
        "term": "Bravery",
        "category": "concepts",
        "intro": "<p>Bravery as used in Isaiah 3:18 (King James Version) is an archaic English term meaning beauty, comeliness, or splendid ornament rather than courage in battle. The Hebrew <em>tiph&#39;arah</em> signifies beauty, glory, or that which is magnificent in appearance. In this context, the passage catalogues the elaborate ornaments and finery that will be stripped from the proud women of Zion in the coming judgment: anklets, headbands, crescents, pendants, bracelets, scarves, headdresses, and &#8220;the bravery of their tinkling ornaments&#8221;&#8212;all the external signs of status and wealth that defined elite Jerusalemite society.</p><p>The broader passage (Isa. 3:16&#8211;4:1) is one of Isaiah&#39;s most detailed social critiques, targeting the arrogance of women who walked with outstretched necks and mincing steps while the poor lacked basic necessities. The judgment&#8212;baldness, sackcloth, and the garments of captivity&#8212;directly inverts the bravery being flaunted. The same word <em>tiph&#39;arah</em> elsewhere describes the glory of God&#39;s restored people (Isa. 62:3) and the beauty of holiness, demonstrating that the object of Isaiah&#39;s critique is misdirected glory rather than beauty itself.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bravery", "isbe": "bravery"},
        "key_refs": ["Isaiah 3:18"],
        "sections": []
    },
    "breach": {
        "id": "breach",
        "term": "Breach",
        "category": "concepts",
        "intro": "<p>Breach in Scripture most commonly refers to a gap broken in a city wall, leaving it vulnerable to enemy attack (1 Kings 11:27; 2 Kings 12:5; Isa. 30:13). The repair of breaches was a matter of urgent civic and defensive concern, and the rebuilding of Jerusalem&#39;s broken walls under Nehemiah is the primary narrative occasion for the term&#39;s use in the post-exilic period. Psalm 60:2 laments a breach God has made in Israel, understood as a defeat requiring divine healing.</p><p>The metaphorical dimensions of &#8220;breach&#8221; prove theologically rich. Isaiah 58:12 and 61:4 envision the restored community as those who repair the ancient ruins and &#8220;raise up the former devastations,&#8221; and Isaiah 30:13 describes unconfessed iniquity as a crack in a high wall, growing silently until it collapses suddenly. The priestly intercessor who &#8220;stands in the breach&#8221; before God on behalf of the people (Ps. 106:23; Ezek. 22:30) becomes a powerful image of prophetic intercession, with Moses the archetypal example. Ezekiel mourns that he could find no such intercessor to stand in the breach for a generation facing judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "breach"},
        "key_refs": ["1 Kings 11:27", "Psalms 106:23", "Isaiah 58:12", "Ezekiel 22:30"],
        "sections": []
    },
    "bread": {
        "id": "bread",
        "term": "Bread",
        "category": "concepts",
        "intro": "<p>Bread was the staple food of ancient Israel and the entire biblical world, made primarily from wheat flour (Ex. 29:2) or, in times of scarcity, from barley, millet, or mixed grains (Judg. 7:13; Ezek. 4:9). Baking was typically women&#39;s work, and the process&#8212;grinding grain, mixing dough, leavening or making unleavened cakes, and baking on a griddle, in a clay oven, or under hot coals&#8212;is described in detail at several points in the narrative (Gen. 18:6; Ruth 2:14; 1 Kings 17:13&#8211;16). The Passover unleavened bread permanently encoded the hurried departure from Egypt in Israel&#39;s annual ritual memory.</p><p>Bread carries profound theological weight throughout both Testaments. The showbread (bread of the Presence) placed weekly before the LORD in the tabernacle signified Israel&#39;s covenantal relationship with God (Ex. 25:30; Lev. 24:5&#8211;9). God provided manna as supernatural bread in the wilderness (Ex. 16), and Jesus declared himself &#8220;the bread of life&#8221; (John 6:35, 48), the true bread from heaven of which the manna was a type. The breaking of bread at the Last Supper instituted the Eucharist (Luke 22:19; 1 Cor. 11:23&#8211;26), and early Christians continued &#8220;breaking bread&#8221; as a central practice of their communal life (Acts 2:42, 46).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bread", "smith": "bread", "isbe": "bread"},
        "key_refs": ["Exodus 16:4", "John 6:35", "Luke 22:19", "Acts 2:42"],
        "sections": []
    },
    "breastplate": {
        "id": "breastplate",
        "term": "Breastplate",
        "category": "concepts",
        "intro": "<p>Breastplate in Scripture refers to two distinct objects: the piece of armor protecting the chest in battle, and the ornate priestly vestment worn by the high priest. The high priest&#39;s breastplate (<em>choshen</em>) was a folded square of the same embroidered fabric as the ephod, set with twelve precious stones in four rows of three, each engraved with the name of one of the twelve tribes (Ex. 28:15&#8211;30; 39:8&#8211;21). Within it were carried the Urim and Thummim, the sacred lots used for discerning God&#39;s will. It was called the &#8220;breastplate of judgment&#8221; and was worn &#8220;over his heart&#8221; when Aaron entered the sanctuary.</p><p>The military breastplate becomes a spiritual metaphor in Isaiah 59:17, where God himself puts on righteousness as a breastplate, and Paul develops this into the full armor of God (Eph. 6:14), identifying the breastplate specifically with righteousness. In 1 Thessalonians 5:8 he describes the breastplate of faith and love, combining Isaian imagery with his characteristic triad of virtues. The protection of the vital organs by a breastplate of moral and spiritual integrity expresses the Pauline conviction that Christian life is a form of warfare requiring active defensive equipment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "breastplate"},
        "key_refs": ["Exodus 28:15", "Ephesians 6:14", "Isaiah 59:17", "1 Thessalonians 5:8"],
        "sections": []
    },
    "breeches": {
        "id": "breeches",
        "term": "Breeches",
        "category": "concepts",
        "intro": "<p>Breeches in the King James Version translates the Hebrew <em>mikhnasayim</em>, designating linen drawers or undergarments worn by the priests from the waist to the thighs (Ex. 28:42; Ezek. 44:17&#8211;18). These were prescribed specifically to cover nakedness when officiating at the altar, a requirement rooted in the prohibition against ascending the altar by steps in such a way as to expose oneself (Ex. 20:26). The priestly undergarments were part of the full vestments required for service at the sanctuary.</p><p>The Revised Version renders the term more accurately as &#8220;linen breeches&#8221; or &#8220;linen undergarments.&#8221; Ezekiel&#39;s vision of the restored temple specifies that the priests shall wear linen breeches and not gird themselves with anything that causes sweat (Ezek. 44:17&#8211;18), maintaining the purity and dignity of sanctuary service. The precise attention to priestly clothing in the legal texts reflects the broader principle that the service of God required not only the right attitude but the right appearance, with every element of dress regulated to express holiness and order in the divine presence.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "breeches", "isbe": "breeches"},
        "key_refs": ["Exodus 28:42", "Ezekiel 44:17"],
        "sections": []
    },
    "bribe": {
        "id": "bribe",
        "term": "Bribe",
        "category": "concepts",
        "intro": "<p>Bribery is consistently condemned in the Old Testament as a corruption of justice that blinds the eyes of the wise and perverts the words of the righteous (Ex. 23:8; Deut. 16:19). The gift that corrupts a judge&#8212;the Hebrew <em>shochad</em>&#8212;undermines the judicial impartiality that Mosaic law regarded as foundational to the covenant community&#39;s social order. Samuel explicitly denied having taken a bribe throughout his life of public service (1 Sam. 12:3), and Amos condemned those who &#8220;afflict the righteous, take a bribe, and turn aside the needy in the gate&#8221; (Amos 5:12) as a central symptom of Israel&#39;s injustice.</p><p>The prophetic literature returns repeatedly to bribery as one of the defining marks of a society in spiritual decline: Isaiah condemns rulers who are &#8220;companions of thieves&#8221; who love bribes and run after gifts (Isa. 1:23), and Micah describes a Jerusalem where judges rule for a bribe and priests teach for a price (Mic. 3:11). Proverbs acknowledges the practical power of a bribe while not endorsing it (Prov. 17:8; 18:16), and Psalm 15:5 identifies the refusal of bribes against the innocent as a mark of the person who shall dwell on God&#39;s holy hill.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bribe"},
        "key_refs": ["Exodus 23:8", "Deuteronomy 16:19", "Amos 5:12", "Psalms 15:5"],
        "sections": []
    },
    "bricks": {
        "id": "bricks",
        "term": "Bricks",
        "category": "concepts",
        "intro": "<p>Brickmaking formed the chief labor imposed on the Israelites during their Egyptian bondage (Ex. 1:13&#8211;14; 5:7&#8211;19). Egyptian bricks were typically made of Nile mud mixed with straw or reed fiber for binding, dried in the sun rather than fired. The famous incident in Exodus 5, where Pharaoh removed the straw supply but maintained the brick quota, has been confirmed by Egyptian sources: both straw-filled and strawless bricks are found at various sites, the latter generally associated with periods of labor crisis.</p><p>Babylon was similarly famous for its fired brick construction (Gen. 11:3), where the Mesopotamian alluvial plain provided abundant clay but no stone. Jeremiah 43:9 records God&#39;s instruction to Jeremiah to hide large stones in mortar at the entrance of Pharaoh&#39;s palace in Tahpanhes, as a sign that Nebuchadnezzar would set his throne over them. Nahum 3:14 sarcastically encourages Nineveh to &#8220;go into the clay and tread the mortar, take hold of the brick mold&#8221; as preparation for the siege that will destroy it&#8212;using the language of construction to anticipate inevitable destruction.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bricks"},
        "key_refs": ["Exodus 1:14", "Exodus 5:7", "Genesis 11:3", "Jeremiah 43:9"],
        "sections": []
    },
    "bride": {
        "id": "bride",
        "term": "Bride",
        "category": "concepts",
        "intro": "<p>Bride is used in Scripture both in the ordinary sense of a woman about to marry or newly married, and as a rich theological metaphor for the community of the redeemed. In ordinary usage, the adornment of a bride with jewels and the joy of a bridegroom over his bride serve as images of divine delight over restored Israel (Isa. 49:18; 61:10; 62:5). The bride of the Song of Solomon, seeking and celebrating her beloved, has been read throughout Jewish and Christian tradition as an allegory of the soul or the community in its relationship to God.</p><p>John the Baptist describes himself as &#8220;the friend of the bridegroom&#8221; who rejoices at hearing the bridegroom&#39;s voice (John 3:29), and Jesus&#39; parables of the wedding banquet and ten virgins (Matt. 22:1&#8211;14; 25:1&#8211;13) develop the marriage metaphor eschatologically. Paul describes the church as a pure virgin presented to Christ (2 Cor. 11:2; Eph. 5:25&#8211;32), and Revelation&#39;s climactic vision is of &#8220;the holy city, new Jerusalem, coming down out of heaven from God, prepared as a bride adorned for her husband&#8221; (Rev. 21:2, 9). The bride metaphor encompasses both the covenant relationship of God and his people and the eschatological consummation toward which all history moves.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bride"},
        "key_refs": ["Revelation 21:2", "Isaiah 61:10", "John 3:29", "Ephesians 5:25"],
        "sections": []
    },
    "bridle": {
        "id": "bridle",
        "term": "Bridle",
        "category": "concepts",
        "intro": "<p>Bridle in Scripture translates several Hebrew words used both literally for the bit and bridle used to control horses and donkeys, and metaphorically for the control of human speech and passion. Psalm 32:9 warns against being like a horse or mule &#8220;which must be curbed with bit and bridle&#8221;&#8212;lacking the understanding to be guided by gentle instruction and requiring forcible restraint. The image of God placing a hook in the nose or a bridle in the mouth of an arrogant king (2 Kings 19:28; Isa. 37:29) expresses divine sovereignty over human aggression, particularly directed at Sennacherib of Assyria.</p><p>The book of James develops the bridle as the primary metaphor for tongue-control: &#8220;If we put bits into the mouths of horses so that they obey us, we guide their whole bodies as well. So also the tongue is a small member, yet it boasts of great things&#8221; (James 3:3). The comparison between the small bit that controls the large horse and the small tongue that directs the whole person became one of the most influential metaphors for self-governance in the biblical tradition. Isaiah 30:28 applies the bridle of divine discipline to the nations.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bridle"},
        "key_refs": ["Psalms 32:9", "2 Kings 19:28", "James 3:3", "Isaiah 30:28"],
        "sections": []
    },
    "brier": {
        "id": "brier",
        "term": "Brier",
        "category": "concepts",
        "intro": "<p>Brier translates several Hebrew terms for thorny or prickly plants and appears throughout the prophetic literature as a symbol of desolation, judgment, and the moral condition of the wicked. Micah 7:4 describes the most upright among the corrupt as a brier hedge. Proverbs 15:19 compares the path of the sluggard to a hedge of thorns in contrast to the smooth highway of the upright. Ezekiel 28:24 promises that Israel will no longer have &#8220;a pricking brier or a painful thorn&#8221; from its neighbors, using the imagery of painful vegetation for hostile surrounding nations.</p><p>Isaiah 55:13 contains the most celebrated brier passage: &#8220;Instead of the thorn shall come up the cypress; instead of the brier shall come up the myrtle&#8221;&#8212;a promise that the transformation of the natural landscape will accompany the new exodus of God&#39;s redeemed people. This same pattern of brier replaced by fruitful vegetation appears in Isaiah 5:6 (as covenant curse) and 7:23&#8211;25 (as consequence of Assyrian invasion), making the presence or absence of briers a barometer of covenant relationship and divine favor in the Isaianic vision of the land.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "brier"},
        "key_refs": ["Isaiah 55:13", "Ezekiel 28:24", "Micah 7:4"],
        "sections": []
    },
    "brigandine": {
        "id": "brigandine",
        "term": "Brigandine",
        "category": "concepts",
        "intro": "<p>Brigandine is an archaic English term used in Jeremiah 46:4 and 51:3 (King James Version) for a type of defensive armor, translated in modern versions as &#8220;coat of mail&#8221; or &#8220;armor.&#8221; A brigandine was historically a body armor made of small iron or steel plates riveted to a fabric or leather backing, sometimes described as a scale coat. The Hebrew <em>siryon</em> denotes the scale armor or coat of mail familiar from ancient Near Eastern warfare.</p><p>Jeremiah 46:4 is part of an oracle against Egypt, urging her soldiers to prepare for battle: &#8220;Harness the horses; mount, O horsemen! Take your stations with your helmets, polish your spears, put on your brigandines!&#8221; The irony is that Egypt&#39;s careful military preparation will not avail against the Babylonian advance that God is orchestrating. Jeremiah 51:3 similarly addresses the archer and soldier of Babylon, but the call to arms there is already futile. The brigandine&#39;s appearance in both oracles against foreign powers underscores that military readiness cannot overcome divine determination.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "brigandine", "smith": "brigandine"},
        "key_refs": ["Jeremiah 46:4", "Jeremiah 51:3"],
        "sections": []
    },
    "brimstone": {
        "id": "brimstone",
        "term": "Brimstone",
        "category": "concepts",
        "intro": "<p>Brimstone (sulfur) is a yellow, flammable mineral found in deposits around the Dead Sea and volcanic regions. Its association with fire and divine judgment pervades the Old Testament: the destruction of Sodom and Gomorrah is described as a rain of fire and brimstone from the LORD out of heaven (Gen. 19:24), and subsequent prophetic literature consistently evokes this event as the paradigm of sudden, total divine judgment (Isa. 34:9; Ezek. 38:22; Amos 4:11). The sulfurous springs and ancient volcanic activity around the Dead Sea region provided a natural basis for the imagery.</p><p>In the New Testament, brimstone is exclusively eschatological: the lake of fire and brimstone in Revelation (Rev. 19:20; 20:10; 21:8) is the ultimate destination of the beast, the false prophet, the devil, and those whose names are not in the book of life. The pairing of fire and brimstone from Genesis to Revelation creates one of the most consistent images of divine wrath in the biblical canon. The torment of Revelation&#39;s lake of fire &#8220;going up forever and ever&#8221; (Rev. 14:11) draws on the Sodom precedent to describe the irreversible and permanent nature of final judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "brimstone", "smith": "brimstone", "isbe": "brimstone"},
        "key_refs": ["Genesis 19:24", "Isaiah 34:9", "Revelation 20:10", "Revelation 21:8"],
        "sections": []
    },
    "brook": {
        "id": "brook",
        "term": "Brook",
        "category": "places",
        "intro": "<p>Brook translates the Hebrew <em>nachal</em>, which in Palestinian geography designates a seasonal watercourse or wadi&#8212;a stream bed that flows with water in the rainy winter season but dries to sand or a trickle in summer. The unreliability of such streams makes them a powerful metaphor in Job 6:15&#8211;20 for treacherous friends whose loyalty disappears when most needed: &#8220;My brothers are treacherous as a torrent-bed, as torrential streams that pass away.&#8221; Several important biblical streams bear this designation, including the Brook Cherith where Elijah was fed by ravens (1 Kings 17:3&#8211;7) and the Brook Besor where some of David&#39;s men remained while others pursued the Amalekites (1 Sam. 30:9&#8211;10).</p><p>The Brook Kidron, running between Jerusalem and the Mount of Olives, appears in significant historical moments: David crossed it weeping during Absalom&#39;s revolt (2 Sam. 15:23), Josiah burned idols there (2 Kings 23:6), and Jesus crossed it on the way to Gethsemane (John 18:1). The &#8220;brook of Eshcol&#8221; yielded the famous cluster of grapes carried back by the Israelite spies (Num. 13:23). The eschatological vision of Ezekiel 47 envisions a life-giving stream flowing from the temple that transforms the landscape, reversing the curse of dryness.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "brook", "isbe": "brook"},
        "key_refs": ["Job 6:15", "1 Kings 17:3", "Numbers 13:23", "John 18:1"],
        "sections": []
    },
    "brother": {
        "id": "brother",
        "term": "Brother",
        "category": "concepts",
        "intro": "<p>Brother in Scripture designates biological siblings (Matt. 1:2), near kinsmen such as nephews and cousins (Gen. 13:8; 14:16), fellow members of the covenant community (Deut. 15:3; 17:15), and members of the same tribe or nation. The broad semantic range of the Hebrew <em>ach</em> reflects a social world in which clan and kinship identity extended well beyond the nuclear family. Jesus&#39; brothers mentioned in the Gospels (Matt. 13:55; Mark 6:3) have been variously identified as biological sons of Mary and Joseph, sons of Joseph by a prior marriage (the Epiphanian view), or cousins (Jerome&#39;s view), without final resolution.</p><p>In the New Testament, &#8220;brother&#8221; becomes the standard designation for fellow believers (Acts 9:17; Rom. 8:29; Heb. 2:11&#8211;12). Jesus&#39; declaration that whoever does the will of God is his brother, sister, and mother (Mark 3:35) redefines kinship around spiritual allegiance rather than biological descent. Paul&#39;s description of Christ as &#8220;the firstborn among many brothers&#8221; (Rom. 8:29) places the resurrected Lord as the elder sibling of a new family constituted by adoption through the Spirit. The ethical obligation flowing from this brotherhood&#8212;including mutual forbearance, financial sharing, and the pursuit of one another&#39;s good&#8212;is a consistent theme of the NT epistles.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "brother", "smith": "brother", "isbe": "brother"},
        "key_refs": ["Romans 8:29", "Mark 3:35", "Hebrews 2:11", "Deuteronomy 15:3"],
        "sections": []
    },
    "bruit": {
        "id": "bruit",
        "term": "Bruit",
        "category": "concepts",
        "intro": "<p>Bruit is an archaic English word meaning a rumor or report, found only in Jeremiah 10:22 (KJV: &#8220;Behold, the noise of the bruit is come, and a great commotion out of the north country&#8221;) and Nahum 3:19 (KJV: &#8220;all that hear the bruit of thee shall clap the hands over thee&#8221;). Modern translations render it as &#8220;rumor,&#8221; &#8220;report,&#8221; or &#8220;news.&#8221; The Hebrew <em>shema&#39;</em> means that which is heard&#8212;a report, tidings, or sound.</p><p>In Jeremiah 10:22 the bruit refers to the report of an advancing army from the north, widely understood as the Babylonian invasion. In Nahum 3:19 the bruit refers to the news of Nineveh&#39;s fall, over which all who hear will clap their hands in relief after centuries of Assyrian brutality. The two uses bracket the prophetic use of the term: in one case a bruit of approaching catastrophe, in the other a bruit of long-awaited judgment on the oppressor. The word itself, long obsolete in English, survives only in these two King James passages.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bruit", "isbe": "bruit"},
        "key_refs": ["Jeremiah 10:22", "Nahum 3:19"],
        "sections": []
    },
    "bucket": {
        "id": "bucket",
        "term": "Bucket",
        "category": "concepts",
        "intro": "<p>Bucket appears in only two biblical passages and in both cases carries figurative rather than literal weight. Isaiah 40:15 declares that the nations are &#8220;like a drop from a bucket&#8221; before God, a striking image of the utter disproportion between the greatest human powers and the sovereign Creator. Numbers 24:7 is part of Balaam&#39;s oracle over Israel: &#8220;Water shall flow from his buckets, and his seed shall be in many waters&#8221;&#8212;an image of abundance and far-reaching influence that several ancient interpreters read as a messianic prophecy.</p><p>The Hebrew <em>deli</em> designates the vessel used to draw water from a well, one of the most basic tools of daily life in an arid land where every drop was precious. The contrast in Isaiah 40:15 between this humble household object and the vast weight of the nations is deliberately deflationary, designed to relativize all human political power before the incomparable majesty of the Creator. The rhetorical move from the cosmic to the domestic and back is characteristic of Deutero-Isaiah&#39;s strategy of reorienting a defeated people toward the sovereignty of their God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bucket", "isbe": "bucket"},
        "key_refs": ["Isaiah 40:15", "Numbers 24:7"],
        "sections": []
    },
    "buckler": {
        "id": "buckler",
        "term": "Buckler",
        "category": "concepts",
        "intro": "<p>Buckler in Scripture designates a small portable shield, distinct from the larger body-length shield used in pitched battle. The Hebrew terms translated buckler (<em>magen</em>, <em>tsinnah</em>) cover a range of protective shields from the small round buckler carried by light troops to the large siege shields. The word appears frequently as a divine epithet: God is called a buckler to those who trust in him (2 Sam. 22:31; Ps. 18:2, 30; Prov. 2:7), and Psalm 91:4 describes his faithfulness as &#8220;a shield and buckler.&#8221;</p><p>In Ezekiel 23:24 the foes of Jerusalem come with bucklers and shields, and 1 Chronicles 5:18 describes the Transjordanian tribes as warriors skilled with bucklers and swords. David hung captured shields in Jerusalem as war trophies (1 Kings 10:16&#8211;17; 2 Chr. 9:15&#8211;16). The consistent metaphorical use of the buckler for divine protection reflects the military realities of the ancient world, where the shield was the primary defensive tool and its quality determined survival in close combat. The theological claim that God himself is the believer&#39;s buckler transfers the warrior&#39;s absolute trust in his shield to the covenant relationship with Yahweh.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "buckler", "isbe": "buckler"},
        "key_refs": ["2 Samuel 22:31", "Psalms 91:4", "Proverbs 2:7"],
        "sections": []
    },
    "building": {
        "id": "building",
        "term": "Building",
        "category": "concepts",
        "intro": "<p>Building in the ancient Israelite world was adapted to the Palestinian landscape and climate. The earliest Israelite settlements after the conquest likely involved taking over existing Canaanite structures, and later periods show a progression from the four-room house typical of Iron Age Israel to the more elaborate public architecture of the monarchy. David&#39;s palace was built by Phoenician craftsmen (2 Sam. 5:11), and Solomon&#39;s temple and palace complex drew on the same expertise and materials&#8212;cedar from Lebanon, hewn stone, and skilled labor that Israel did not itself possess (1 Kings 5:6&#8211;18).</p><p>Building becomes a metaphor for the construction of community and character in both testaments. Paul describes the church as a building whose foundation is Jesus Christ (1 Cor. 3:10&#8211;15) and as &#8220;a holy temple in the Lord&#8221; being built together as a dwelling place for God (Eph. 2:21&#8211;22). Each believer&#39;s work of ministry is described as building on this foundation with materials whose quality will be tested by fire on the last day. The eschatological image of the heavenly city descending as a divine building not made by human hands (Heb. 11:10; Rev. 21:2) completes the metaphorical arc from earthly construction to eternal divine habitation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "building"},
        "key_refs": ["1 Kings 5:6", "1 Corinthians 3:10", "Ephesians 2:21", "Hebrews 11:10"],
        "sections": []
    },
    "bul": {
        "id": "bul",
        "term": "Bul",
        "category": "concepts",
        "intro": "<p>Bul, meaning <em>rain</em> or <em>produce</em>, was the name of the eighth month in the ancient Hebrew calendar, corresponding roughly to October&#8211;November. It is mentioned in 1 Kings 6:38 as the month in which Solomon&#39;s temple was completed, after seven years of construction. The name appears in inscriptions from Gezer and in Phoenician sources, confirming its use in the broader Canaanite cultural sphere. After the Babylonian exile, this month came to be called Marcheshvan (or Cheshvan) in the Babylonian-derived calendar that Israel adopted.</p><p>Bul falls at the beginning of the rainy season in Palestine, when the early rains break the summer drought and the agricultural cycle begins anew with plowing and planting. The completion of the temple in this month may carry symbolic significance: the house of God finished as the rains return, linking divine habitation with the life-giving rhythms of the land. The pre-exilic Hebrew calendar with its agricultural month names (Abib, Ziv, Ethanim, Bul) reflects the deep integration of Israel&#39;s religious life with the cycles of Palestinian farming.</p>",
        "hitchcock_meaning": "old age; perishing",
        "source_ids": {"easton": "bul", "smith": "bul", "isbe": "bul"},
        "key_refs": ["1 Kings 6:38"],
        "sections": []
    },
    "bullock": {
        "id": "bullock",
        "term": "Bullock",
        "category": "concepts",
        "intro": "<p>Bullock translates Hebrew terms for young bulls used extensively in the sacrificial system of ancient Israel. Bulls and bullocks were the most expensive sacrificial animals, required for the most solemn rites: the sin offering for the high priest or the whole congregation (Lev. 4:3&#8211;21), the consecration of priests (Ex. 29:1), and the elaborate sacrifices of the major festivals (Num. 28&#8211;29). A young bull without blemish was the paradigmatic animal of the burnt offering, its full consumption by fire signifying total consecration to God.</p><p>The prophets used bullock imagery to critique the reduction of worship to mere ritual formalism. Isaiah 1:11 voices God&#39;s disgust at the &#8220;abundance of burnt offerings, rams and fat of fed beasts,&#8221; when justice and compassion were absent, and Hosea 14:2 calls Israel to offer &#8220;the bulls of our lips&#8221;&#8212;that is, verbal praise rather than animal sacrifice&#8212;as the appropriate offering of a repentant people. Psalm 69:31 similarly declares that a humble, thankful heart pleases the LORD more than an ox or bullock with horns and hoofs, anticipating the New Testament&#39;s spiritual reinterpretation of sacrifice.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bullock"},
        "key_refs": ["Leviticus 4:3", "Exodus 29:1", "Isaiah 1:11", "Hosea 14:2"],
        "sections": []
    },
    "bulrush": {
        "id": "bulrush",
        "term": "Bulrush",
        "category": "concepts",
        "intro": "<p>Bulrush translates two distinct Hebrew terms in the Old Testament. The first (<em>gome&#39;</em>) is the papyrus plant (<em>Cyperus papyrus</em>), which grew abundantly in the Nile marshes and was used for making boats, baskets, and writing material. The basket in which the infant Moses was placed (Ex. 2:3) is described as made of this material&#8212;literally a &#8220;papyrus ark.&#8221; Isaiah 18:2 describes Egyptian ambassadors traveling &#8220;in vessels of papyrus on the waters.&#8221; The second term (<em>agmon</em>) in Isaiah 58:5 refers to a reed or rush, used in the image of a hypocritical fast that merely bows the head like a bulrush rather than producing genuine repentance.</p><p>Papyrus had ceased to grow in Egypt by medieval times but was reintroduced and is found today only in limited locations. Its importance in the ancient world can hardly be overstated: virtually all writing in the ancient Mediterranean and Near East was done on papyrus or prepared animal skin, and Egypt was the primary producer and exporter of this material throughout the biblical period. The image of the infant Moses hidden in a papyrus basket among the reeds of the Nile connects his birth story to this quintessentially Egyptian plant.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bulrush", "smith": "bulrush"},
        "key_refs": ["Exodus 2:3", "Isaiah 58:5", "Isaiah 18:2"],
        "sections": []
    },
    "bulwarks": {
        "id": "bulwarks",
        "term": "Bulwarks",
        "category": "concepts",
        "intro": "<p>Bulwarks designates the defensive towers, ramparts, and bastions of a fortified city wall. The Hebrew <em>chel</em> and related terms refer to the outer defensive works&#8212;the raised earthworks, towers, and ramparts that protected the city gates and wall stretches. King Uzziah introduced a significant innovation in Judahite military fortification by installing engines of war on the towers and at the corners to shoot arrows and hurl large stones at besiegers (2 Chr. 26:15). Psalm 48:13 invites worshippers to &#8220;walk about Zion, go around her, number her towers, consider well her ramparts, go through her citadels,&#8221; as an act of praise for God&#39;s protection of the city.</p><p>The theological use of bulwarks moves naturally from the military to the metaphorical: Isaiah 26:1 describes the strong city of the redeemed as one where God himself has set up &#8220;salvation as walls and bulwarks.&#8221; This metaphorical transfer&#8212;from stone defensive works to divine protection experienced as equally solid and reliable&#8212;is characteristic of the biblical psalms and prophets, who consistently describe God&#39;s protection in the concrete architectural language of military security.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bulwarks"},
        "key_refs": ["2 Chronicles 26:15", "Psalms 48:13", "Isaiah 26:1", "Zephaniah 1:16"],
        "sections": []
    },
    "bunch": {
        "id": "bunch",
        "term": "Bunch",
        "category": "concepts",
        "intro": "<p>Bunch in the King James Version translates three distinct Hebrew terms for bound clusters or groupings of plants. The &#8220;bunch of hyssop&#8221; in Exodus 12:22 was used to apply the Passover blood to the doorposts and lintel, making hyssop the instrument of apotropaic protection on the night of the exodus. The same connection&#8212;hyssop and blood&#8212;recurs in the purification rites of Leviticus and Numbers, and in Psalm 51:7 (&#8220;purge me with hyssop&#8221;) as a plea for moral cleansing.</p><p>The &#8220;bunch of raisins&#8221; (a cake of pressed raisins, so most modern versions) brought to David by Ziba (2 Sam. 16:1) and carried as provisions by those who came to David at Ziklag (1 Chr. 12:40) reflects the portable, long-lasting food staples of ancient Israelite travel and warfare. The &#8220;bunch of a camel&#8221; in Isaiah 30:6 refers to the hump, as gifts are loaded on animals for an embassy to Egypt. These three quite different uses of the word reflect the breadth of the KJV translators&#39; vocabulary choices where specific Hebrew terms lacked obvious English equivalents.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bunch", "isbe": "bunch"},
        "key_refs": ["Exodus 12:22", "2 Samuel 16:1", "Isaiah 30:6"],
        "sections": []
    },
    "burden": {
        "id": "burden",
        "term": "Burden",
        "category": "concepts",
        "intro": "<p>Burden in Scripture carries both literal and technical prophetic meanings. Literally it designates any load carried by an animal or person (Ex. 23:5), a heavy task or responsibility (Ex. 2:11; 18:22), or an oppressive obligation. Moses&#39; complaint to God about bearing the people &#8220;as a nurse carries a nursing infant&#8221; (Num. 11:11&#8211;12) and Jesus&#39; contrast between the heavy burdens laid on others by the Pharisees and his own &#8220;easy yoke and light burden&#8221; (Matt. 11:28&#8211;30) use the word in this relational and social sense.</p><p>The technical use of &#8220;burden&#8221; (<em>massa&#39;</em>) as a heading for prophetic oracles against foreign nations (Isa. 13:1; 15:1; 17:1; 19:1; Jer. 23:33&#8211;38; Nah. 1:1; Hab. 1:1; Zech. 9:1; Mal. 1:1) reflects the Hebrew term&#39;s double meaning: both &#8220;load&#8221; and &#8220;utterance.&#8221; A prophetic burden is thus both something that weighs on the prophet and a weighty word pronounced against its subject. Jeremiah 23:33&#8211;38 contains an extended wordplay on this ambiguity, where the people&#39;s mocking question &#8220;What is the burden of the LORD?&#8221; draws a sharp divine response.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "burden", "isbe": "burden"},
        "key_refs": ["Exodus 23:5", "Isaiah 13:1", "Matthew 11:30", "Jeremiah 23:33"],
        "sections": []
    },
    "burial": {
        "id": "burial",
        "term": "Burial",
        "category": "concepts",
        "intro": "<p>Burial among the Israelites was regarded as a duty of piety, and denial of burial was considered a great indignity (Eccl. 6:3; Jer. 22:19). The first detailed burial account in Scripture is that of Sarah, for whose sepulcher Abraham negotiated with the sons of Heth, establishing the cave of Machpelah as the patriarchal burial site (Gen. 23). Burial normally followed death within hours in the hot Palestinian climate, and the body was washed, wrapped in linen, and sometimes anointed with spices before being laid in a tomb cut from rock or in a simple grave.</p><p>The family tomb, where generation after generation were &#8220;gathered to their people,&#8221; expressed the continuity of family identity and the hope of belonging to the ancestral community even in death. New Testament burial practice followed similar conventions: Jesus was wrapped in linen with spices and laid in a garden tomb within hours of his crucifixion (John 19:38&#8211;42), and the women&#39;s return to the tomb with further spices on Sunday morning (Mark 16:1&#8211;2; Luke 24:1) reflects the ongoing desire to complete proper burial preparation. Paul&#39;s use of burial imagery in Romans 6:4 and Colossians 2:12 makes the Christian&#39;s baptism a participation in Christ&#39;s death, burial, and resurrection.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "burial", "isbe": "burial"},
        "key_refs": ["Genesis 23:4", "John 19:40", "Romans 6:4", "Mark 16:1"],
        "sections": []
    },
    "burnt-offering": {
        "id": "burnt-offering",
        "term": "Burnt Offering",
        "category": "concepts",
        "intro": "<p>The burnt offering (<em>olah</em>, meaning &#8220;that which ascends&#8221;) was the foundational sacrifice of the Israelite cult, distinguished by the complete consumption of the entire animal on the altar&#8212;nothing was returned to the offerer or reserved for the priests except the hide (Lev. 7:8). This totality expressed the offering&#39;s primary meaning: unreserved dedication to God. Animals acceptable for burnt offerings included bulls, rams, male goats, turtledoves, and pigeons, with the species determined by the offerer&#39;s means (Lev. 1:3&#8211;17). The daily burnt offering&#8212;a lamb morning and evening on the altar of the tabernacle&#8212;was the heartbeat of Israel&#39;s sacrificial calendar (Ex. 29:38&#8211;42; Num. 28:3&#8211;8).</p><p>The foundational burnt offerings of Scripture&#8212;Noah&#39;s after the flood (Gen. 8:20), Abraham&#39;s near-sacrifice of Isaac (Gen. 22:2&#8211;13), and the inauguration of the tabernacle worship (Lev. 9)&#8212;mark key transitions in the covenant narrative. The Epistle to the Hebrews argues that all these offerings pointed forward to the self-offering of Christ, who &#8220;offered himself without blemish to God&#8221; (Heb. 9:14), fulfilling and superseding the entire burnt offering system. Psalm 40:6&#8211;8, quoted in Hebrews 10:5&#8211;7, explicitly subordinates burnt offerings to obedient self-presentation before God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "burnt-offering", "smith": "burnt-offering"},
        "key_refs": ["Leviticus 1:3", "Exodus 29:38", "Genesis 22:2", "Hebrews 9:14"],
        "sections": []
    },
    "bush": {
        "id": "bush",
        "term": "Bush",
        "category": "concepts",
        "intro": "<p>Bush in Scripture refers most significantly to the burning bush in which the LORD appeared to Moses at Horeb&#8212;a bush that burned with fire but was not consumed (Ex. 3:2&#8211;4). The Hebrew <em>seneh</em> appears only in the contexts related to this theophany; Deuteronomy 33:16 alludes to it in the blessing of Joseph as &#8220;the one who dwells in the bush.&#8221; The miraculous character of the vision&#8212;fire present yet without destruction&#8212;signaled divine holiness that was approachable only on God&#39;s own terms, as the command to remove sandals makes clear (Ex. 3:5).</p><p>The bush theophany is the context of God&#39;s self-revelation as &#8220;I AM WHO I AM&#8221; (Ex. 3:14), the disclosure of the divine name Yahweh, and the commission of Moses to deliver Israel from Egypt. Jesus references &#8220;the passage about the bush&#8221; in his argument for the resurrection (Mark 12:26; Luke 20:37), citing God&#39;s self-identification as the God of Abraham, Isaac, and Jacob as evidence that the patriarchs are alive, since God is not the God of the dead but of the living. The burning bush thus becomes a locus for both OT revelation and NT theological argument.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bush"},
        "key_refs": ["Exodus 3:2", "Exodus 3:14", "Mark 12:26", "Deuteronomy 33:16"],
        "sections": []
    },
    "butler": {
        "id": "butler",
        "term": "Butler",
        "category": "concepts",
        "intro": "<p>Butler translates the Hebrew <em>mashkeh</em>, literally &#8220;one who gives to drink,&#8221; designating the chief cupbearer of an ancient Near Eastern royal court (Gen. 40:1&#8211;13; 41:9&#8211;13). The royal cupbearer held a position of great trust and intimacy with the king: he tasted wine before serving it to guard against poisoning, and his constant proximity to the monarch gave him significant political influence. Egyptian sources and Assyrian palace reliefs confirm the importance of this office across the ancient Near East.</p><p>Pharaoh&#39;s butler appears in the Joseph narrative as a fellow prisoner who receives Joseph&#39;s interpretation of his dream, forecasting his restoration to office. When the butler was restored as predicted, he failed to remember Joseph and mention him to Pharaoh for two full years&#8212;a delay that becomes part of the providential pattern the narrator is tracing. Nehemiah served as cupbearer to Artaxerxes I of Persia (Neh. 1:11), a position that gave him access and standing to request royal permission for the Jerusalem rebuilding project. Solomon&#39;s cupbearers impressed the Queen of Sheba alongside his buildings, wisdom, and household arrangements (1 Kings 10:5; 2 Chr. 9:4).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "butler", "smith": "butler", "isbe": "butler"},
        "key_refs": ["Genesis 40:1", "Genesis 41:9", "Nehemiah 1:11", "1 Kings 10:5"],
        "sections": []
    },
    "butter": {
        "id": "butter",
        "term": "Butter",
        "category": "concepts",
        "intro": "<p>Butter in Scripture translates the Hebrew <em>chemah</em>, which more precisely designates curdled milk, leben (a yogurt-like fermented dairy product), or clarified butter&#8212;the product of churning milk in a skin bag, common across the ancient Near East. Abraham served his three divine visitors curd and milk along with a prepared calf (Gen. 18:8), and Jael gave Sisera curdled milk from a skin to drink (Judg. 5:25). Job 29:6 uses the image of his steps being &#8220;washed with butter&#8221; (clarified fat) as a figure for extraordinary prosperity and ease.</p><p>The land flowing with &#8220;milk and honey&#8221; reflects the same pastoral abundance that butter imagery evokes. Isaiah 7:15, 22 promises that in the time of the messianic child, curds and honey will be the available food in a land so depopulated by judgment that it reverts to pasture&#8212;an ambiguous image simultaneously of divine provision and agricultural devastation. Psalm 55:21 uses butter as a metaphor for smooth, deceptive speech: &#8220;His speech was smooth as butter, yet war was in his heart.&#8221; Proverbs 30:33 draws on the physical process of churning: &#8220;Churning milk produces curds, and twisting the nose produces blood, so stirring up anger produces strife.&#8221;</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "butter", "smith": "butter"},
        "key_refs": ["Genesis 18:8", "Judges 5:25", "Job 29:6", "Psalms 55:21"],
        "sections": []
    },
    "buz": {
        "id": "buz",
        "term": "Buz",
        "category": "people",
        "intro": "<p>Buz, whose name means <em>contempt</em> or <em>despised</em>, appears in two contexts in the Old Testament. The first is as the second son of Nahor and Milcah, Abraham&#39;s brother and sister-in-law (Gen. 22:21), making him a nephew of Abraham and a member of the broader Terahite family that gave rise to both the Israelites and the Aramean peoples. A Buzite region in northern Arabia is also associated with the name.</p><p>The more theologically significant appearance of Buz is through his descendant Elihu son of Barachel the Buzite, the fourth and final interlocutor in the book of Job (Job 32:2). Elihu is notably angry with both Job for justifying himself rather than God and with the three friends for failing to answer Job adequately, and his speeches (Job 32&#8211;37) prepare the way for God&#39;s speeches from the whirlwind. Jeremiah 25:23 lists Buz among the nations that will drink the cup of God&#39;s wrath in judgment, placing the region in the orbit of the broader ancient Near East subject to prophetic reckoning.</p>",
        "hitchcock_meaning": "despised; plundered",
        "source_ids": {"easton": "buz", "smith": "buz"},
        "key_refs": ["Genesis 22:21", "Job 32:2", "Jeremiah 25:23"],
        "sections": []
    },
    "buzi": {
        "id": "buzi",
        "term": "Buzi",
        "category": "people",
        "intro": "<p>Buzi, whose name means <em>my contempt</em> or <em>despised of the LORD</em>, is known in Scripture solely as the father of the prophet Ezekiel (Ezek. 1:3). The book of Ezekiel opens with the precise dating and location of the prophet&#39;s inaugural vision: in the thirtieth year, in the fourth month, on the fifth day, while Ezekiel was among the exiles by the river Chebar in Babylonia, the word of the LORD came to Ezekiel son of Buzi the priest.</p><p>The identification of Ezekiel as both son of Buzi and as a priest places him within the Zadokite priestly lineage, which is reflected throughout his prophecy in his intense concern for the temple, its furnishings, its ritual purity, and the detailed vision of the restored sanctuary in chapters 40&#8211;48. Buzi himself receives no further biographical treatment in the text; his significance is entirely genealogical, establishing his son&#39;s priestly credentials and the context of Ezekiel&#39;s call to prophetic ministry in exile.</p>",
        "hitchcock_meaning": "my contempt",
        "source_ids": {"easton": "buzi", "smith": "buzi"},
        "key_refs": ["Ezekiel 1:3"],
        "sections": []
    },
    "by": {
        "id": "by",
        "term": "By",
        "category": "concepts",
        "intro": "<p>By in 1 Corinthians 4:4 (King James Version) is used in the archaic sense of &#8220;against,&#8221; translating the Greek preposition <em>hypo</em> in the reflexive context: &#8220;For I know nothing by myself&#8221; (KJV), meaning &#8220;I am not aware of anything against myself&#8221; (ESV, RSV). This usage&#8212;&#8220;by&#8221; in the sense of &#8220;against&#8221;&#8212;was current in sixteenth and seventeenth century English but is now confined to dialectal use. The Revised Version correctly renders it as &#8220;against.&#8221;</p><p>Paul&#39;s statement in its context is a careful reflection on self-assessment and divine judgment: his clear conscience does not acquit him, since it is the Lord who judges. The passage (1 Cor. 4:1&#8211;5) is a significant text on the limits of introspection and the sufficiency of divine evaluation alone as the final standard. The archaic use of &#8220;by&#8221; in the KJV illustrates more broadly the way in which shifts in the meaning of common English prepositions over four centuries can obscure rather than illuminate the sense of passages that were transparently clear to seventeenth-century readers.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "by"},
        "key_refs": ["1 Corinthians 4:4"],
        "sections": []
    },
    "by-and-by": {
        "id": "by-and-by",
        "term": "By and By",
        "category": "concepts",
        "intro": "<p>By and by is an archaic English phrase used in Matthew 13:21 and Luke 21:9 (King James Version) to translate the Greek <em>eutheos</em> and <em>euthys</em>, meaning &#8220;immediately&#8221; or &#8220;straightway.&#8221; In modern English &#8220;by and by&#8221; means &#8220;eventually&#8221; or &#8220;after some time,&#8221; the precise opposite of its seventeenth-century meaning of &#8220;at once.&#8221; This semantic reversal is one of the more significant instances of a KJV translation that now actively misleads the modern reader.</p><p>In Matthew 13:21, the rocky-ground hearer receives the word with joy but falls away &#8220;by and by&#8221;&#8212;that is, immediately&#8212;when persecution arises. In Luke 21:9, Jesus warns that the end does not come &#8220;by and by&#8221;&#8212;that is, not immediately&#8212;when wars and disturbances occur. The Revised Version renders Matthew 13:21 as &#8220;straightway&#8221; and the RSV and ESV as &#8220;immediately,&#8221; restoring the urgency of the Greek. The shift in meaning of &#8220;by and by&#8221; over four centuries illustrates the necessity of periodic translation revision to maintain accurate communication of the biblical text.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "by-and-by", "isbe": "by-and-by"},
        "key_refs": ["Matthew 13:21", "Luke 21:9"],
        "sections": []
    },
    "by-ways": {
        "id": "by-ways",
        "term": "By-ways",
        "category": "concepts",
        "intro": "<p>By-ways appears in Judges 5:6 and Psalm 125:5 (King James Version) for the winding, crooked, or indirect paths taken to avoid the main roads. In Judges 5:6, the song of Deborah laments that in the days of Shamgar and Jael the highways were abandoned and travelers &#8220;walked through by-ways&#8221;&#8212;indirect routes through wilderness and hill country taken to avoid the Canaanite-controlled roads and the danger of ambush. This picture of a land where normal commerce and travel were impossible captures the insecurity of Israel in the early judges period.</p><p>Psalm 125:5 uses the image spiritually: &#8220;But those who turn aside to their crooked ways (<em>by-ways</em>), the LORD will lead away with evildoers.&#8221; The contrast is between those who trust in the LORD and are as secure as Mount Zion (vv. 1&#8211;2) and those who abandon the straight path for crooked detours that lead to judgment. The physical image of winding, hidden paths becomes a metaphor for moral deviation and spiritual apostasy, consistent with the Psalter&#39;s broader use of the &#8220;way&#8221; metaphor for the path of righteous or unrighteous living.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "by-ways"},
        "key_refs": ["Judges 5:6", "Psalms 125:5"],
        "sections": []
    },
    "by-word": {
        "id": "by-word",
        "term": "By-word",
        "category": "concepts",
        "intro": "<p>By-word in the King James Version translates two Hebrew terms used for a person or people who has become a proverb or object of scornful speech among others. The Hebrew <em>millah</em> (Job 30:9) means a word or speech, and Job laments that he has become &#8220;their song&#8221; and &#8220;their by-word&#8221;&#8212;a figure of ridicule among those who were themselves despised. The more common term <em>mashal</em> (Ps. 44:14; Deut. 28:37; 2 Chr. 7:20) designates a proverb or taunt-song, signifying a person or nation that has become a cautionary example.</p><p>The covenant curses of Deuteronomy 28:37 threaten that Israel will become &#8220;a horror, a proverb, and a by-word among all the peoples&#8221; if it abandons the LORD&#8212;a threat fulfilled in the exilic experience and lamented in Psalm 44:14. Solomon&#39;s prayer of dedication anticipates this possibility (2 Chr. 7:20: &#8220;I will make it a proverb and a by-word among all peoples&#8221;). The by-word thus represents the ultimate public shame of a people whose covenant relationship with God was their defining identity, and whose failure of that relationship became a subject of commentary and contempt among the nations.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "by-word"},
        "key_refs": ["Job 30:9", "Psalms 44:14", "Deuteronomy 28:37", "2 Chronicles 7:20"],
        "sections": []
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
    print(f'BP b4: Blind → By-word: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
