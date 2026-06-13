"""
BP Article Synthesis — w: Wafers → Writing
Covers Easton entries: Wafers through Writing (63 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Category logic applied:
  - people:   Hitchcock match + no major place signals in brief
  - places:   brief/title contains 'city', 'town', 'sea of', 'river', 'mount', 'valley', etc.
  - concepts: no Hitchcock match, no place signals
  - names:    Hitchcock-only (no Easton/Smith entry exists)
  - events:   title is clearly an event (battle, feast, exile, flood, etc.)

Script: scripts/bp-w.py
Run: python3 scripts/bp-w.py
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
    "wafers": {
        "id": "wafers",
        "term": "Wafers",
        "category": "concepts",
        "intro": "<p>Wafers (Hebrew <em>raqiq</em>) were thin, unleavened cakes used in a number of Mosaic offerings and rituals. They appear in the account of the manna, which the Israelites described as tasting like \"wafers made with honey\" (Exodus 16:31). In the Levitical system, unleavened wafers anointed or spread with oil were prescribed as a meat offering (Leviticus 2:4) and as an accompaniment to certain peace offerings and the consecration of the Nazirite's vow (Numbers 6:15, 19). They also featured in the ordination ceremony of Aaron and his sons (Exodus 29:2, 23; Leviticus 8:26). The wafer's thinness and unleavened character made it suitable for these uses — the absence of leaven signifying purity and the absence of corruption. The same Hebrew term underlies the Passover unleavened bread, connecting all these ritual uses to the theme of purity before God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wafers"},
        "key_refs": ["Exodus 16:31", "Exodus 29:2", "Leviticus 2:4", "Numbers 6:15"]
    },
    "wages": {
        "id": "wages",
        "term": "Wages",
        "category": "concepts",
        "intro": "<p>Wages in Scripture are governed by two principles: prompt payment and just compensation. The Mosaic law required that a hired worker be paid before sundown on the day he worked: \"Thou shalt not oppress a hired servant that is poor and needy... At his day thou shalt give him his hire, neither shall the sun go down upon it\" (Leviticus 19:13; Deuteronomy 24:14–15). To withhold wages was a form of oppression denounced by the prophets (Jeremiah 22:13; Malachi 3:5) and by James, who declares that the cries of cheated laborers have reached the ears of the Lord (James 5:4). The only specific wage-rate cited in the New Testament is the denarius per day paid to vineyard workers in Jesus's parable (Matthew 20:2), which represents the standard daily wage of the period. Paul uses the concept theologically in Romans 6:23: \"The wages of sin is death; but the gift of God is eternal life through Jesus Christ our Lord\" — contrasting earned penalty with freely given grace.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wages", "smith": "wages", "isbe": "wages"},
        "key_refs": ["Leviticus 19:13", "Deuteronomy 24:15", "Matthew 20:2", "Romans 6:23"]
    },
    "wagon": {
        "id": "wagon",
        "term": "Wagon",
        "category": "concepts",
        "intro": "<p>Wagons (Hebrew <em>aghalah</em>, from the root meaning \"to roll\") were wheeled carts drawn by oxen and used for transporting goods and people. The word is translated both \"wagon\" and \"cart\" in the King James Bible. In Genesis 45:19, 21, 27, Pharaoh sends wagons to bring Jacob and his household down to Egypt at Joseph's invitation. Numbers 7:3–8 records that the leaders of Israel brought six covered wagons and twelve oxen as offerings at the dedication of the tabernacle; these were assigned to the Gershonites and Merarites for transporting the tabernacle components, while the Kohathites bore the holy vessels on their shoulders. The Philistines used a wagon (1 Samuel 6:7–14) to return the ark of the LORD, pulled by milk cows. David's ill-fated attempt to transport the ark on a new cart (2 Samuel 6:3–7) resulted in the death of Uzzah and a change to the proper Levitical method of carrying it on poles.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wagon", "smith": "wagon"},
        "key_refs": ["Genesis 45:19", "Numbers 7:3", "1 Samuel 6:7", "2 Samuel 6:3"]
    },
    "wailing-place-jews": {
        "id": "wailing-place-jews",
        "term": "Wailing-place, Jews'",
        "category": "places",
        "intro": "<p>The Jews' Wailing Place (now known as the Western Wall or Kotel) is a section of the western retaining wall of the temple mount in Jerusalem, constructed by Herod the Great as part of his expansion of the temple precinct. After the destruction of the temple by the Romans in AD 70, the site became the holiest accessible location for Jewish prayer and mourning, as the temple itself was gone and the mount under foreign control for most of subsequent history. Jewish pilgrims gathered here on the anniversary of the temple's destruction (the ninth of Av) and on other occasions to lament the desolation — hence the name given by Western travellers. The laments of Psalm 79 (\"O God, the heathen are come into thine inheritance\") and the book of Lamentations were recited here. The wall is approximately 485 meters long in total, with the exposed prayer plaza section roughly 57 meters wide; it is the most visited Jewish site in the world.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wailing-place-jews"},
        "key_refs": ["Psalms 79:1", "Isaiah 64:9", "Lamentations 1:4"]
    },
    "wall": {
        "id": "wall",
        "term": "Wall",
        "category": "concepts",
        "intro": "<p>Walls in biblical times served defensive, social, and symbolic purposes. Fortified city walls distinguished urban settlements from open villages (Leviticus 25:29; Numbers 13:28; Deuteronomy 3:5) and were the primary defense against military assault. Ancient Israelite cities were protected by massive walls — archaeological evidence at Hazor, Megiddo, and Gezer reveals Solomonic-era walls several metres thick. The conquest of Jericho, where the walls \"fell down flat\" at the trumpet blast (Joshua 6:20), demonstrated that divine power supersedes human fortification. Nehemiah's rebuilding of Jerusalem's walls (Nehemiah 1–6) is the most extended wall-construction narrative in Scripture. Walls also figure metaphorically: God promises to be \"a wall of fire\" around Jerusalem (Zechariah 2:5), and Paul declares in Ephesians 2:14 that Christ has broken down \"the middle wall of partition\" — the dividing wall in the temple that excluded Gentiles from the inner courts — as a metaphor for the reconciliation of Jew and Gentile in one body.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wall", "isbe": "wall"},
        "key_refs": ["Joshua 6:20", "Nehemiah 4:6", "Zechariah 2:5", "Ephesians 2:14"]
    },
    "wandering": {
        "id": "wandering",
        "term": "Wandering",
        "category": "events",
        "intro": "<p>The Wandering of Israel in the Wilderness refers to the forty-year period between the Exodus from Egypt and the entry into Canaan, during which the Israelites traversed the Sinai peninsula and surrounding regions. The proximate cause was God's judgment on the generation that refused to enter Canaan after the report of the twelve spies (Numbers 13–14): because they believed the ten fearful spies over Caleb and Joshua and wept in unbelief, God declared that all adults twenty years and older at the time of the census would die in the wilderness (Numbers 14:26–35). The itinerary of the wilderness period is recorded in Numbers 33, listing forty-two stopping points. Deuteronomy's retrospective frames the wandering as both judgment and discipline: \"thou shalt remember all the way which the LORD thy God led thee these forty years in the wilderness, to humble thee, and to prove thee\" (Deuteronomy 8:2). The New Testament uses the wilderness generation typologically as a warning against unbelief (1 Corinthians 10:1–11; Hebrews 3:7–4:11).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wandering"},
        "key_refs": ["Numbers 14:33", "Numbers 33:1", "Deuteronomy 8:2", "Hebrews 3:17"]
    },
    "war": {
        "id": "war",
        "term": "War",
        "category": "concepts",
        "intro": "<p>War in the Old Testament is a pervasive reality both historical and theological. Israel took possession of Canaan through military conquest ordered by God (Deuteronomy 7:1–2; Joshua 1:2–9), and subsequent Israelite history involved continuous warfare with surrounding nations. The Mosaic law regulated warfare: declarations were required before siege (Deuteronomy 20:10–12), fruit trees were protected (Deuteronomy 20:19–20), and certain categories of persons were exempt from service (Deuteronomy 20:5–8). Israel's military victories and defeats were theologically interpreted as reflecting the nation's covenant faithfulness or disobedience — a theology most explicitly stated in the covenant blessings and curses of Deuteronomy 28. The New Testament reinterprets the warfare motif: while earthly warfare is not condemned, the primary conflict is spiritual. Paul describes the Christian life with military metaphors — armour of God (Ephesians 6:11–17), good soldier (2 Timothy 2:3–4) — while insisting that \"the weapons of our warfare are not carnal, but mighty through God\" (2 Corinthians 10:4).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "war", "smith": "war"},
        "key_refs": ["Deuteronomy 20:1", "Ephesians 6:11", "2 Corinthians 10:4", "2 Timothy 2:3"]
    },
    "ward": {
        "id": "ward",
        "term": "Ward",
        "category": "concepts",
        "intro": "<p>Ward in the King James Bible translates several distinct Hebrew and Greek terms, all denoting confinement or watchful custody. As a prison or place of detention, it appears in Genesis 40:3–4, where Pharaoh puts his chief butler and baker \"in ward\" in the house of the captain of the guard — the same place where Joseph was imprisoned. In Isaiah 21:8, the word means a watch-post or station: the watchman cries that he stands continually on his ward (his post). In Nehemiah 13:30, it refers to the assigned watches (guard duties) of the priests and Levites. The concept of ward thus spans confinement imposed on prisoners and the vigilant duty of watchmen — two meanings united by the idea of close attention and boundary-keeping.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ward", "isbe": "ward"},
        "key_refs": ["Genesis 40:3", "Isaiah 21:8", "Nehemiah 13:30"]
    },
    "wars-of-the-lord-the-book-of-the": {
        "id": "wars-of-the-lord-the-book-of-the",
        "term": "Wars of the Lord, The Book of the",
        "category": "concepts",
        "intro": "<p>The Book of the Wars of the LORD is an ancient document cited once in the Old Testament (Numbers 21:14–15) in a brief poetic fragment about the borders of Arnon. The citation — \"Wherefore it is said in the book of the wars of the LORD, What he did in the Red Sea, and in the brooks of Arnon\" — is our only evidence that such a book existed. It was apparently a collection of songs or accounts celebrating Israel's military victories under divine leadership during the wilderness period and conquest of Transjordan. Like the Book of Jasher (referenced in Joshua 10:13 and 2 Samuel 1:18) and the book mentioned in Numbers 21:27, it represents a class of early Israelite literary sources that did not enter the canonical collection but were known to the biblical authors. Nothing further is known of its contents, date, or authors. The existence of such collections suggests a rich tradition of military poetry celebrating divine warfare in early Israel, of which the Song of Moses (Exodus 15) and the Song of Deborah (Judges 5) are canonical examples.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wars-of-the-lord-the-book-of-the"},
        "key_refs": ["Numbers 21:14", "Joshua 10:13", "2 Samuel 1:18"]
    },
    "washing": {
        "id": "washing",
        "term": "Washing",
        "category": "concepts",
        "intro": "<p>Washing in the ancient Near East served both hygienic and ceremonial purposes, and the Mosaic law developed an extensive system of ritual washing to mark transitions between states of purity and impurity. Priests were required to wash their hands and feet before ministering at the altar (Exodus 30:19–21). Levitical washings were prescribed for contact with corpses, certain diseases, bodily emissions, and other sources of impurity (Leviticus 11–15; Numbers 19). By the first century AD, the Pharisees had elaborated these laws into a detailed oral tradition governing handwashing before meals — a \"tradition of the elders\" that Jesus challenged not as hygiene but as a substitute for genuine heart-purity (Mark 7:1–9; Matthew 15:1–9). Pilate's washing of his hands in Matthew 27:24 appropriated the OT gesture of disavowal (Deuteronomy 21:6–7) but could not remove guilt. John 13:1–17, where Jesus washes the disciples' feet, uses the washing motif to illustrate servanthood and the spiritual cleansing that comes through him.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "washing"},
        "key_refs": ["Exodus 30:19", "Mark 7:3", "Matthew 27:24", "John 13:8"]
    },
    "watches": {
        "id": "watches",
        "term": "Watches",
        "category": "concepts",
        "intro": "<p>Watches were the divisions of the night assigned to sentinels on guard duty. The Hebrews originally divided the night into three watches — the beginning, the middle, and the morning watch (Judges 7:19; Exodus 14:24; Lamentations 2:19) — each corresponding to roughly four hours. After contact with the Romans, four watches came into use, as reflected in the New Testament: the evening watch, midnight, cockcrow, and morning (Mark 13:35; Matthew 14:25). Watchmen were stationed on city walls (2 Samuel 18:24; 2 Kings 9:17–20) and in watchtowers in vineyards and fields (Isaiah 21:8; Matthew 21:33) to give warning of approaching enemies or travellers. Metaphorically, the psalmists and prophets use the night watch as an image of eager expectation: \"My soul waiteth for the Lord more than they that watch for the morning\" (Psalm 130:6). Jesus's parables of the watching servants (Luke 12:37–38; Mark 13:34–37) use the watch system to call disciples to vigilance in expectation of his return.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "watches"},
        "key_refs": ["Judges 7:19", "2 Samuel 18:24", "Mark 13:35", "Psalms 130:6"]
    },
    "watchings": {
        "id": "watchings",
        "term": "Watchings",
        "category": "concepts",
        "intro": "<p>Watchings (Greek <em>agrupniai</em>, literally \"sleeplessnesses\") appears in Paul's list of hardships endured in apostolic ministry in 2 Corinthians 6:5 and 11:27 — catalogues of suffering that include beatings, imprisonments, stonings, shipwreck, perils of travel, and both hunger and watchings. The term denotes involuntary sleeplessness arising from the demands and dangers of mission: nights spent working to avoid being a burden (1 Thessalonians 2:9; 2 Thessalonians 3:8), nights of prayer (Luke 6:12), and nights of anxiety and danger when rest was impossible. Paul's inclusion of watchings in a formal list of apostolic credentials reflects his understanding that physical suffering and deprivation are marks of genuine ministry rather than evidence of failure — a perspective that challenged Corinthian Christians who prized comfort and eloquence in their spiritual leaders.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "watchings"},
        "key_refs": ["2 Corinthians 6:5", "2 Corinthians 11:27"]
    },
    "water-of-jealousy": {
        "id": "water-of-jealousy",
        "term": "Water of jealousy",
        "category": "concepts",
        "intro": "<p>The water of jealousy (Hebrew <em>mey hama'arim</em>, \"bitter waters that bring the curse\") was a ritual ordeal administered to a wife suspected of adultery when there was no witness to confirm or deny the charge (Numbers 5:11–31). The priest mixed dust from the tabernacle floor with holy water in an earthen vessel, wrote out the curse on a scroll, washed the ink into the water, and gave the woman the bitter water to drink after she had sworn an oath of innocence. If she were guilty, the text states the water would cause her abdomen to swell and her thigh to fall, bringing the curse upon her; if innocent, she would be free and would conceive children. The rite operated as a divine judgment in the absence of human evidence, placing the outcome entirely in God's hands. It is unique in the Mosaic law as a trial by ordeal and represents one of the few cases in Israelite law where a matter could not be resolved by witnesses alone.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "water-of-jealousy", "smith": "water-of-jealousy"},
        "key_refs": ["Numbers 5:11", "Numbers 5:18", "Numbers 5:27"]
    },
    "water-of-purification": {
        "id": "water-of-purification",
        "term": "Water of purification",
        "category": "concepts",
        "intro": "<p>The water of purification refers to lustral water used in various Levitical ceremonies of ritual cleansing. In Numbers 8:7, God instructs Moses to cleanse the Levites before their consecration to tabernacle service: \"sprinkle water of purifying upon them.\" More broadly, Levitical law prescribed washings with water for purification from numerous sources of uncleanness, including contact with a corpse, the completion of a period of skin disease, bodily discharge, and contact with carcasses of unclean animals (Leviticus 11–15). The most elaborate purification water was the water of separation prepared with the ashes of a red heifer (Numbers 19), which could remove the impurity of death. Zechariah 13:1 prophesies a future \"fountain opened to the house of David and to the inhabitants of Jerusalem for sin and for uncleanness,\" which the New Testament understands as fulfilled in the cleansing work of Christ (1 John 1:7; Hebrews 9:13–14).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "water-of-purification"},
        "key_refs": ["Numbers 8:7", "Leviticus 15:13", "Zechariah 13:1", "Hebrews 9:13"]
    },
    "water-of-separation": {
        "id": "water-of-separation",
        "term": "Water of separation",
        "category": "concepts",
        "intro": "<p>The water of separation (Hebrew <em>mey niddah</em>, \"water of impurity\" or \"water for the removal of sin\") was a specially prepared mixture of spring water and the ashes of a red heifer, used to cleanse persons and objects defiled by contact with a human corpse — the most severe form of ritual impurity under the Mosaic law (Numbers 19). A perfect red heifer without defect, never yoked, was slaughtered and burned entirely, along with cedar wood, hyssop, and scarlet thread; the ashes were preserved and mixed with running water as needed. A clean person sprinkled the mixture on the defiled person with a hyssop branch on the third and seventh days of impurity, after which the defiled person washed and was clean by evening. The paradox of the rite — that the person who prepared it became unclean while the unclean person became clean — was noted by ancient rabbis and Christian commentators alike. The author of Hebrews contrasts the limited efficacy of this purification with the blood of Christ, which \"purge[s] your conscience from dead works to serve the living God\" (Hebrews 9:13–14).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "water-of-separation", "smith": "water-of-separation"},
        "key_refs": ["Numbers 19:9", "Numbers 19:17", "Hebrews 9:13"]
    },
    "waterspouts": {
        "id": "waterspouts",
        "term": "Waterspouts",
        "category": "concepts",
        "intro": "<p>Waterspouts (Hebrew <em>tsinnor</em>) appears in Psalm 42:7: \"Deep calleth unto deep at the noise of thy waterspouts: all thy waves and thy billows are gone over me.\" The Revised Version margin renders <em>tsinnor</em> as \"cataracts,\" and most modern translations follow this sense: the roaring of waterfalls or floodgates of heaven. The psalmist, apparently in exile north of the Jordan near the headwaters of the river and the roar of the waters from Mount Hermon (mentioned in verse 6), uses the overwhelming sound and force of cascading water as an image for the floods of divine affliction that have submerged him. The same Hebrew word may be connected to David's capture of Jerusalem through the water shaft or conduit (<em>tsinnor</em>) mentioned in 2 Samuel 5:8, though that usage is debated. The verse's powerful image of \"deep calling to deep\" became a locus classicus in Christian mystical and devotional writing for describing the soul's experience of overwhelming suffering and divine encounter.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "waterspouts"},
        "key_refs": ["Psalms 42:7"]
    },
    "wave-offerings": {
        "id": "wave-offerings",
        "term": "Wave offerings",
        "category": "concepts",
        "intro": "<p>Wave offerings (Hebrew <em>tenufah</em>) were portions of sacrifices presented to God by a distinctive gesture of waving — moving the offering horizontally back and forth before the LORD — before they were given to the officiating priest. The rite is prescribed in Exodus 29:24–27 for the breast of the ram of ordination, and it became the standard treatment for the breast of all peace offerings (Leviticus 7:30–34). The right shoulder (thigh) was the \"heave offering\" (<em>terumah</em>, lifted up vertically); the breast was the wave offering. Both portions were assigned to Aaron and his sons as their priestly portion. Wave offerings were also prescribed for the two lambs at Pentecost (Leviticus 23:20) and for offerings connected with the Nazirite vow (Numbers 6:20). The waving gesture was understood as symbolically presenting the offering to God and receiving it back as a portion — a liturgical enactment of gift and return.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wave-offerings"},
        "key_refs": ["Exodus 29:24", "Leviticus 7:30", "Leviticus 23:20", "Numbers 6:20"]
    },
    "wax": {
        "id": "wax",
        "term": "Wax",
        "category": "concepts",
        "intro": "<p>Wax in Scripture refers to the product of bees' combs melted down, and it appears primarily in poetic and metaphorical contexts. The image of wax melting before fire is used three times in the Psalms to convey dissolution or terror before God: \"They are like wax; they melt away before God\" (Psalm 68:2); \"the mountains melted like wax at the presence of the LORD\" (Psalm 97:5); and in Psalm 22:14, the suffering Servant says \"my heart is like wax; it is melted in the midst of my bowels\" — a vivid description of extreme anguish. Micah 1:4 similarly pictures the mountains melting like wax before the fire at God's coming in judgment. The consistent use of wax as an image of instantaneous, irreversible dissolution under heat makes it a powerful figure for both human frailty before God's holiness and for the destructive force of divine judgment on natural obstacles.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wax", "isbe": "wax"},
        "key_refs": ["Psalms 22:14", "Psalms 68:2", "Psalms 97:5", "Micah 1:4"]
    },
    "wean": {
        "id": "wean",
        "term": "Wean",
        "category": "concepts",
        "intro": "<p>Weaning in the ancient Hebrew world was a significant milestone, typically occurring later than modern practice — at two or three years of age, and in some accounts possibly as late as five. The extended nursing period meant that weaning was a cause for celebration: Genesis 21:8 records that Abraham \"made a great feast the same day that Isaac was weaned.\" Hannah delayed bringing Samuel to the tabernacle until after his weaning, waiting until she could fulfil her vow to dedicate him permanently to the LORD's service (1 Samuel 1:22–24). The weaned child is used metaphorically in Psalm 131:2 by the psalmist to describe a state of quieted contentment before God: \"as a child that is weaned of his mother: my soul is even as a weaned child\" — no longer crying for what it cannot have, but resting in the present relationship. Song of Solomon 8:1 uses the imagery of nursing mothers in a comparison.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wean", "isbe": "wean"},
        "key_refs": ["Genesis 21:8", "1 Samuel 1:23", "Psalms 131:2"]
    },
    "weasel": {
        "id": "weasel",
        "term": "Weasel",
        "category": "concepts",
        "intro": "<p>The weasel (Hebrew <em>holedh</em>) appears once in the Old Testament in the list of unclean creeping things that defile by contact (Leviticus 11:29). Most modern lexicographers accept the identification as a weasel or mole-rat — a small carnivorous mammal common to the Middle East — though some earlier translators rendered the word as \"mole.\" Whatever the precise species, the <em>holedh</em> is grouped with the mouse, the great lizard, the gecko, the sand lizard, and other small animals among the creatures \"that creep upon the earth\" whose carcasses conveyed ritual impurity. Anyone who touched such a carcass was unclean until evening; any vessel, food, or water the carcass fell into was similarly defiled (Leviticus 11:31–38). The dietary and purity laws served to distinguish Israel from surrounding nations and to maintain the symbolic holiness of the covenant community.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "weasel", "smith": "weasel", "isbe": "weasel"},
        "key_refs": ["Leviticus 11:29"]
    },
    "weaving-weavers": {
        "id": "weaving-weavers",
        "term": "Weaving, weavers",
        "category": "concepts",
        "intro": "<p>Weaving was one of the most ancient and economically significant crafts in the biblical world. Egypt was particularly famed for its fine linen weaving (Isaiah 19:9), and the skilled weavers among the Israelites contributed their expertise to the construction of the tabernacle: Exodus 35:35 lists \"the weaver\" alongside the embroiderer and the designer among the craftsmen filled with divine wisdom for tabernacle work. The specific weaving of the tabernacle curtains (Exodus 26:1–6) and the high priest's garments (Exodus 28:6–8) required exceptional skill. Weaving is used metaphorically in Job 7:6 — \"my days are swifter than a weaver's shuttle\" — as an image of the speed and transience of life. The craft employed both horizontal looms (for ordinary cloth) and vertical looms (for fine tapestry). The Phoenicians (Ezekiel 27:7) and Egyptians were renowned as exporters of woven textiles throughout the Mediterranean world.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "weaving-weavers"},
        "key_refs": ["Exodus 35:35", "Isaiah 19:9", "Job 7:6", "Ezekiel 27:7"]
    },
    "week": {
        "id": "week",
        "term": "Week",
        "category": "concepts",
        "intro": "<p>The week, a unit of seven days, is embedded in the creation narrative of Genesis 1–2, where God works for six days and rests on the seventh — establishing the pattern that underlies the sabbath commandment (Exodus 20:8–11; Deuteronomy 5:12–15). The seven-day week is not derived from astronomical cycles (unlike the day, month, and year) but from this divine pattern, making it unique among ancient time divisions. In Hebrew, the days were numbered rather than named (first day, second day, etc.), with the seventh called the Sabbath (<em>shabbat</em>, \"rest\"). Weeks also structured the religious calendar: seven weeks of seven days (a week of weeks) separated Passover from Pentecost (Leviticus 23:15–16); seven sabbatical years led to the Jubilee (Leviticus 25:8); and Daniel's prophecy of \"seventy weeks\" (Daniel 9:24–27) uses the week unit for calculating messianic timing. In the New Testament, the first day of the week became the Lord's Day, the primary day of Christian assembly, in commemoration of the resurrection (John 20:19; Acts 20:7; Revelation 1:10).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "week", "smith": "week", "isbe": "week"},
        "key_refs": ["Genesis 2:2", "Exodus 20:11", "Leviticus 23:15", "Daniel 9:24"]
    },
    "weeks-feast-of": {
        "id": "weeks-feast-of",
        "term": "Weeks, Feast of",
        "category": "events",
        "intro": "<p>The Feast of Weeks (Hebrew <em>chag shavu'ot</em>) was the second of the three great annual pilgrimage festivals of Israel, celebrated fifty days after the Passover Sabbath — hence its Greek name <em>Pentecost</em> (\"fiftieth\"). The law in Leviticus 23:15–21 and Deuteronomy 16:9–12 required counting seven complete weeks from the day after the Passover Sabbath, then on the fiftieth day presenting a new grain offering from the first wheat harvest, including two leavened loaves as a wave offering — uniquely leavened, unlike most offerings. The festival was a joyful celebration of the completed wheat harvest, and Deuteronomy emphasized the inclusion of servants, Levites, strangers, orphans, and widows in the celebration. The Feast of Weeks acquired new significance in the New Testament: it was on the day of Pentecost that the Holy Spirit descended on the assembled disciples in Jerusalem, the promised gift of the risen Christ (Acts 2:1–4), an event the church has understood as the spiritual harvest corresponding to the physical harvest celebrated that day.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "weeks-feast-of", "isbe": "weeks-feast-of"},
        "key_refs": ["Leviticus 23:16", "Deuteronomy 16:9", "Acts 2:1"]
    },
    "weights": {
        "id": "weights",
        "term": "Weights",
        "category": "concepts",
        "intro": "<p>Hebrew weights were based on the shekel as the standard unit, with subdivisions and multiples used in trade and in the Mosaic law. The gerah was the smallest unit (one-twentieth of a shekel; Exodus 30:13); the shekel equalled twenty gerahs; the maneh (mina) equalled fifty shekels; and the talent equalled sixty minas or three thousand shekels. A \"shekel of the sanctuary\" (Exodus 30:13, 24; 38:24–26) was used for official temple calculations. Actual weights were typically made of stone — the \"stones\" mentioned in Leviticus 19:36 and Deuteronomy 25:13–15 refer to stone weight-standards. The Bible repeatedly condemns the use of falsified weights: Leviticus 19:35–36, Proverbs 11:1, 16:11, 20:23, and Micah 6:11 all denounce \"divers weights\" (a heavy stone for buying, a light one for selling) as an abomination to the LORD — a form of economic fraud violating covenant justice. Archaeological finds of inscribed stone weights from Iron Age Israel confirm the system described in Scripture.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "weights"},
        "key_refs": ["Leviticus 19:36", "Deuteronomy 25:15", "Proverbs 11:1", "Micah 6:11"]
    },
    "well": {
        "id": "well",
        "term": "Well",
        "category": "concepts",
        "intro": "<p>A well (Hebrew <em>beer</em>) was a dug shaft reaching groundwater, distinct from a spring (<em>'ain</em>) which was a natural outflow. Wells were critical to life in the semi-arid landscape of Canaan and the surrounding regions, and control of water rights was a source of frequent conflict. Abraham and Abimelech quarrelled over wells at Beersheba (Genesis 21:25–31), and the naming of Beersheba (\"well of the oath\") reflects the solemnity of these agreements. Isaac's servants dug a series of wells in the Philistine territory that generated repeated disputes (Genesis 26:15–22). The well was a customary meeting place and, in patriarchal narrative, the setting for betrothal encounters: Abraham's servant met Rebekah at a well (Genesis 24:11–20), Jacob met Rachel at a well (Genesis 29:2–12), and Moses met Zipporah and her sisters at a well in Midian (Exodus 2:15–17). Jesus's conversation with the Samaritan woman at Jacob's Well (John 4:6–26) gives the setting deep symbolic resonance: he offers \"living water\" springing up to eternal life, transcending the physical well.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "well", "smith": "well", "isbe": "well"},
        "key_refs": ["Genesis 21:25", "Genesis 26:20", "John 4:11", "John 4:14"]
    },
    "westward": {
        "id": "westward",
        "term": "Westward",
        "category": "concepts",
        "intro": "<p>In biblical Hebrew, westward is expressed as <em>yammah</em>, meaning \"seaward\" — toward the sea, since the Mediterranean lay to the west of Israel. This spatial orientation was built into the Hebrew vocabulary: <em>yam</em> means both \"sea\" and \"west.\" Deuteronomy 3:27 uses the term when God tells Moses to look north, south, east, and west (<em>yammah</em>) from Mount Pisgah to behold the promised land he would not enter. The directional terms of biblical Hebrew thus reflect the geographical setting of the authors, who oriented themselves with the east (sunrise) as the primary direction — hence the east is \"before\" (<em>qedem</em>), the west is \"behind\" (<em>achar</em> or <em>yam</em>), the south is \"right hand\" (<em>yamin</em>), and the north is \"left hand\" (<em>smol</em>). This geographical vocabulary shaped the symbolic associations of directions in prophetic and poetic literature.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "westward"},
        "key_refs": ["Deuteronomy 3:27"]
    },
    "whale": {
        "id": "whale",
        "term": "Whale",
        "category": "concepts",
        "intro": "<p>The word \"whale\" in the King James Bible translates several distinct Hebrew terms, none of which necessarily refers to the cetacean mammal as the term is used in modern English. The Hebrew <em>tan</em> (plural <em>tannin</em>) appears in Job 7:12 (\"Am I a sea, or a whale, that thou settest a watch over me?\"), Ezekiel 29:3 (God addresses Pharaoh as \"the great dragon that lieth in the midst of his rivers\"), and Jeremiah 51:34. In Genesis 1:21 the KJV renders <em>tannin</em> as \"great whales\" (the great sea creatures of creation). The great fish (<em>dag gadol</em>) that swallowed Jonah is specifically called a large fish in Hebrew (Jonah 1:17), though the Septuagint and Matthew 12:40 use <em>ketos</em> (a large sea creature or sea monster). The cumulative biblical picture is of powerful and terrifying creatures of the deep that serve as instruments of divine sovereignty — whether as symbols of chaos subdued by God in creation or as agents of his providential purposes.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "whale", "smith": "whale", "isbe": "whale"},
        "key_refs": ["Job 7:12", "Jonah 1:17", "Matthew 12:40", "Genesis 1:21"]
    },
    "wheat": {
        "id": "wheat",
        "term": "Wheat",
        "category": "concepts",
        "intro": "<p>Wheat (Hebrew <em>hittah</em>) was one of the primary grain crops of ancient Palestine and the ancient Near East, cultivated since at least the tenth millennium BC. It appears throughout Scripture as a staple food and a measure of prosperity: God's blessing on Israel included \"the finest of the wheat\" (Psalm 81:16; 147:14; Deuteronomy 32:14). Egypt's seven years of plenty in Joseph's era were characterized by abundant wheat harvests (Genesis 41:5–7). The annual wheat harvest in early summer was the occasion for the Feast of Weeks (Pentecost). Wheat appears frequently in Jesus's parables: the parable of the tares (Matthew 13:24–30) involves wheat growing alongside weeds, with the harvest as the image of final judgment; John 12:24 uses the grain of wheat falling into the ground to die as a figure for Christ's death and resurrection; Luke 22:31 records Jesus telling Peter that Satan has desired to sift him \"as wheat.\" The separation of wheat from chaff at threshing became a classic image of divine judgment (Matthew 3:12).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wheat", "smith": "wheat", "isbe": "wheat"},
        "key_refs": ["Psalms 81:16", "Matthew 13:25", "John 12:24", "Matthew 3:12"]
    },
    "wheel": {
        "id": "wheel",
        "term": "Wheel",
        "category": "concepts",
        "intro": "<p>Wheels appear in Scripture in both practical and visionary contexts. The practical wheel (<em>galgal</em>, also meaning \"rolling thing\") was used in threshing instruments (Isaiah 28:28), in wheels of wagons (Ezekiel 23:24; Nahum 3:2), and in the ten wheeled bronze bases of the temple (1 Kings 7:30–33). Psalm 83:13 uses the wheel or tumbleweed metaphorically: \"O my God, make them like a wheel; as the stubble before the wind.\" The most theologically significant wheels are in Ezekiel's inaugural vision, where four enormous wheels (Hebrew <em>ofan</em>) accompany the four living creatures bearing the divine throne-chariot: they are described as \"a wheel in the middle of a wheel\" with rims full of eyes (Ezekiel 1:15–21; 10:9–17), moving in concert with the Spirit without turning. This image of omnidirectional divine movement has generated extensive discussion in Jewish mysticism (Merkabah tradition) and Christian theology about the divine omnipresence and sovereignty.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wheel", "isbe": "wheel"},
        "key_refs": ["Psalms 83:13", "Ezekiel 1:16", "1 Kings 7:30"]
    },
    "white": {
        "id": "white",
        "term": "White",
        "category": "concepts",
        "intro": "<p>White is consistently used in Scripture as a symbol of purity, holiness, victory, and divine glory. In Levitical contexts, the purified leper presented himself with a white garment to signify cleansing; white garments for the Levites and priests (2 Chronicles 5:12) expressed consecration to God's service. Isaiah 1:18 offers God's invitation to covenant renewal: \"though your sins be as scarlet, they shall be as white as snow; though they be red like crimson, they shall be as wool.\" In the Apocalypse, white garments are given to the redeemed (Revelation 3:4–5; 7:9, 14) and the armies of heaven are clothed in fine white linen (Revelation 19:14). The transfigured Christ's garments became \"white as snow\" or \"white as the light\" (Matthew 17:2; Mark 9:3). In Daniel 7:9, the Ancient of Days wears garments white as snow. The consistent association of white with the divine presence and with the eschatological state of the redeemed makes it the dominant colour of apocalyptic vision.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "white", "isbe": "white"},
        "key_refs": ["Isaiah 1:18", "Revelation 7:9", "Matthew 17:2", "Daniel 7:9"]
    },
    "widows": {
        "id": "widows",
        "term": "Widows",
        "category": "concepts",
        "intro": "<p>The care of widows is one of the most persistent ethical demands of both Testaments, placed alongside care for orphans and strangers as a test of genuine covenant faithfulness. The Mosaic law forbade oppressing widows (Exodus 22:22–24) and directed that a portion of the tithe be set aside for them (Deuteronomy 14:29; 26:12–13). The prophets repeatedly charge Israel with neglecting widows as evidence of covenant breach (Isaiah 1:17, 23; Jeremiah 7:6; Ezekiel 22:7; Zechariah 7:10). Job defends his righteousness by citing his care for widows (Job 29:13; 31:16). In the New Testament, James defines pure religion as \"to visit the fatherless and widows in their affliction\" (James 1:27). The early church immediately faced the challenge of providing for widows (Acts 6:1–6), leading to the appointment of the first deacons. Paul gives specific instructions about the enrollment of widows for formal church support (1 Timothy 5:3–16), and Luke's Gospel gives particular attention to widows as exemplars of faith (Luke 2:36–38; 18:1–8; 21:1–4).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "widows"},
        "key_refs": ["Exodus 22:22", "Deuteronomy 14:29", "James 1:27", "1 Timothy 5:3"]
    },
    "wife": {
        "id": "wife",
        "term": "Wife",
        "category": "concepts",
        "intro": "<p>The institution of marriage and the role of wife is established at creation: after God created Eve from Adam's rib, he presented her to the man, and \"therefore shall a man leave his father and his mother, and shall cleave unto his wife: and they shall be one flesh\" (Genesis 2:24). Jesus cites this text in his teaching on divorce (Matthew 19:4–6; Mark 10:6–9), grounding marriage in the one-flesh union of creation and opposing easy divorce. The Old Testament ideal of a faithful wife is celebrated in Proverbs 31:10–31 (the <em>eshet chayil</em>, woman of valour) and in the Song of Solomon's poetry of mutual love. The New Testament develops the husband-wife relationship as an analogy of Christ and the church (Ephesians 5:22–33), with the wife's submission to her husband paralleled by the church's submission to Christ, and the husband's love for his wife paralleled by Christ's self-giving love for the church. Polygamy, practiced by the patriarchs and Israelite kings, is never explicitly commanded in Scripture and is implicitly critiqued by the creation pattern of one man and one woman.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wife", "smith": "wife", "isbe": "wife"},
        "key_refs": ["Genesis 2:24", "Matthew 19:5", "Ephesians 5:22", "Proverbs 31:10"]
    },
    "wilderness": {
        "id": "wilderness",
        "term": "Wilderness",
        "category": "concepts",
        "intro": "<p>Wilderness in the Old Testament most often translates the Hebrew <em>midhbar</em>, denoting not a barren sandy desert but a largely uninhabited pastoral region used for grazing — the semi-arid steppe land beyond the cultivated zones. The same word is used for areas where flocks grazed (Psalm 65:12; Joel 1:19–20) and where the voice cried \"prepare ye the way of the LORD\" (Isaiah 40:3). The Sinai wilderness became the defining location of Israel's foundational encounter with God — Sinai, the giving of the law, the tabernacle — making the wilderness both a place of divine meeting and of testing. Elijah fled to the wilderness (1 Kings 19:4) and was fed there; John the Baptist appeared in the wilderness of Judea (Matthew 3:1); Jesus was led by the Spirit into the wilderness to be tempted (Matthew 4:1; Mark 1:12–13). The wilderness thus carries a dual theological significance in Scripture: it is the place of stripping away human resources and the place of intimate divine encounter.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wilderness", "isbe": "wilderness"},
        "key_refs": ["Isaiah 40:3", "Matthew 3:1", "Matthew 4:1", "Deuteronomy 8:2"]
    },
    "willows": {
        "id": "willows",
        "term": "Willows",
        "category": "concepts",
        "intro": "<p>Willows (Hebrew <em>'arabim</em>) appear several times in Scripture in connection with water and with mourning. The word <em>'arabah</em> (related to the same root) also means the Jordan valley and dry steppe, suggesting these trees were associated with watercourses in otherwise dry terrain. Leviticus 23:40 prescribes the use of willows, along with palm branches and boughs of leafy trees, in the celebration of the Feast of Tabernacles. Job 40:22 places the behemoth under the willow trees beside brooks. Isaiah 44:3–4 promises spiritual refreshment on Israel using the image of willows growing by water. The most poignant use is Psalm 137:1–2: \"By the rivers of Babylon, there we sat down, yea, we wept, when we remembered Zion. We hanged our harps upon the willows in the midst thereof\" — where the willow becomes the symbol of exile's mournful silence. The species is probably the weeping willow or the poplar (<em>Salix acmophylla</em> or related), common in Mesopotamian river landscapes.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "willows", "smith": "willows", "isbe": "willows"},
        "key_refs": ["Psalms 137:1", "Leviticus 23:40", "Isaiah 44:4", "Job 40:22"]
    },
    "wimple": {
        "id": "wimple",
        "term": "Wimple",
        "category": "concepts",
        "intro": "<p>Wimple (Hebrew <em>mitpachot</em>) appears in Isaiah 3:22 in the KJV's rendering of a list of women's clothing items that God will take away from the daughters of Zion as a judgment. Modern translations render the word as \"shawls\" (RSV, NIV, ESV) or \"cloaks\" — a large outer wrap or veil worn by women. The same Hebrew root appears in Ruth 3:15 where Boaz tells Ruth to hold out her shawl (<em>mitpachot</em>) and he fills it with six measures of barley for her to carry home. The word thus describes a substantial outer garment used both as clothing and as a carrying vessel. Isaiah 3:18–24 is a remarkable catalogue of the elaborate feminine ornamentation of the Judean upper class — anklets, headbands, crescents, pendants, bracelets, scarves, and many other items — whose removal is promised as a sign of coming humiliation and desolation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wimple", "smith": "wimple", "isbe": "wimple"},
        "key_refs": ["Isaiah 3:22", "Ruth 3:15"]
    },
    "window": {
        "id": "window",
        "term": "Window",
        "category": "concepts",
        "intro": "<p>Windows in ancient Palestinian houses were typically small, high openings designed for ventilation and light while providing security and privacy. They might be closed with latticed screens, wooden shutters, or simple coverings. Several biblical windows are notable: Rahab hung a scarlet cord from her window as a sign for the Israelite spies, and her house built into the city wall had a window that allowed them to escape by rope (Joshua 2:15, 18, 21). Michal let David down through a window to escape from Saul's men (1 Samuel 19:12). Ahaziah fell through \"a lattice in his upper chamber\" (2 Kings 1:2). At Troas, Eutychus fell asleep in a window and fell from the third floor while Paul was preaching (Acts 20:9). Paul himself was let down from a window in Damascus in a basket to escape the governor's soldiers (2 Corinthians 11:33). The upper windows of Solomon's temple admitted light to the inner rooms (1 Kings 6:4). Windows also appear metaphorically: Malachi 3:10 promises God will \"open the windows of heaven\" with blessing for those who bring the full tithe.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "window", "smith": "window", "isbe": "window"},
        "key_refs": ["Joshua 2:15", "2 Kings 1:2", "Acts 20:9", "Malachi 3:10"]
    },
    "winds": {
        "id": "winds",
        "term": "Winds",
        "category": "concepts",
        "intro": "<p>Winds in Scripture are recognized as instruments of divine sovereignty and as natural forces with theological significance. The four winds — north, south, east, and west — represent completeness and universality: Jeremiah 49:36 speaks of the four winds of the four quarters of heaven as agents of God's judgment on Elam; Ezekiel 37:9 calls on the four winds to breathe upon the valley of dry bones, bringing life; Daniel 8:8 and Zechariah 2:6 use the four winds to indicate dispersion in all directions. The east wind (<em>qadim</em> or <em>ruach qadim</em>) is consistently associated in Scripture with destructive force: it blasted the seven thin ears of Pharaoh's dream (Genesis 41:6), dried up Jonah's gourd (Jonah 4:8), and is used by God as an instrument of judgment (Exodus 10:13; Hosea 13:15). The south wind brought warmth (Job 37:17; Luke 12:55); the north wind brought cold (Proverbs 25:23). In Acts 27:14, the violent northeastern wind Euroclydon (Euroquilo) drove Paul's ship toward Malta.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "winds", "smith": "winds"},
        "key_refs": ["Jeremiah 49:36", "Ezekiel 37:9", "John 3:8", "Acts 27:14"]
    },
    "wine": {
        "id": "wine",
        "term": "Wine",
        "category": "concepts",
        "intro": "<p>Wine (Hebrew <em>yayin</em>, the most common term; also <em>tirosh</em>, new wine; Greek <em>oinos</em>) was a staple beverage and a significant feature of both daily life and religious observance in biblical times. Its production was part of the agricultural cycle blessed by God: \"corn, wine, and oil\" appear as the triad of divine provision throughout the Old Testament (Deuteronomy 7:13; Hosea 2:8). Wine was used in the Levitical offerings (Numbers 15:5–10), and Jesus's first miracle was turning water into wine at Cana (John 2:1–11). Paul instructs Timothy to take a little wine for his stomach (1 Timothy 5:23). At the same time, Scripture consistently warns against drunkenness: Noah's drunkenness led to dishonour (Genesis 9:21), Lot's daughters used wine to deceive him (Genesis 19:32–35), and Proverbs 20:1 declares \"Wine is a mocker; strong drink is raging.\" The Nazirite vow required abstinence from wine. Jesus instituted the Lord's Supper using the cup of wine as the symbol of his blood of the new covenant (Matthew 26:27–29; 1 Corinthians 11:25–26).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wine", "smith": "wine"},
        "key_refs": ["Deuteronomy 7:13", "John 2:3", "Matthew 26:27", "Proverbs 20:1"]
    },
    "wine-press": {
        "id": "wine-press",
        "term": "Wine-press",
        "category": "concepts",
        "intro": "<p>The wine-press (Hebrew <em>gath</em> for the upper trough; Greek <em>lenos</em>) consisted of two connected receptacles cut from rock or built of stone: an upper vat where grapes were trodden by foot, and a lower vat (<em>yeqeb</em>) into which the juice flowed through a channel. Grape-treading was communal, seasonal labor performed with singing and shouting (Isaiah 16:10; Jeremiah 25:30). Jesus's parable of the tenants describes a landowner who \"digged a wine-press\" in his vineyard (Matthew 21:33; Mark 12:1). The wine-press becomes in Scripture a powerful image of divine judgment: in Isaiah 63:2–3, God describes treading the wine-press of his wrath alone; in Revelation 14:19–20 and 19:15, the great wine-press of God's wrath is trodden outside the city, producing a flood of blood. Joel 3:13 calls for the nations to be sent to the wine-press as the great judgment approaches. The treading of grapes, with its images of crushing and flowing blood-red liquid, made the wine-press a natural figure for the execution of divine judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wine-press"},
        "key_refs": ["Isaiah 63:3", "Matthew 21:33", "Revelation 14:19", "Joel 3:13"]
    },
    "winefat": {
        "id": "winefat",
        "term": "Winefat",
        "category": "concepts",
        "intro": "<p>Winefat (Greek <em>hupolenion</em>, \"under the press\") refers to the lower receptacle of the wine-press, set below the treading floor to receive the juice that flows from the crushed grapes. The word occurs only once in the New Testament at Mark 12:1, in Jesus's parable of the wicked tenants: \"A man planted a vineyard and set a hedge around it, and dug a place for the winefat, and built a tower, and let it out to husbandmen.\" Matthew 21:33 provides a parallel with slightly different vocabulary. The detail of digging a winefat was a significant investment by the owner — indicating careful preparation and legitimate expectation of fruit — which heightens the injustice of the tenants who refused to render the owner his due. The parable uses the vineyard's complete equipment (hedge, tower, wine-press, winefat) to depict a well-established covenantal arrangement, making the tenants' rejection all the more inexcusable.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "winefat"},
        "key_refs": ["Mark 12:1", "Matthew 21:33"]
    },
    "winnow": {
        "id": "winnow",
        "term": "Winnow",
        "category": "concepts",
        "intro": "<p>Winnowing was the process of separating grain from chaff after threshing, accomplished by tossing the mixture into the air with a wooden fan or fork so that wind carried away the lighter chaff while the heavier grain fell back to the threshing floor. Biblical references to winnowing include Ruth 3:2, where Boaz is winnowing barley at the threshing floor, providing the setting for Ruth's approach. Isaiah 30:24 promises that the oxen and donkeys that work the ground will eat clean fodder \"which hath been winnowed with the shovel and with the fan.\" Jeremiah uses the image to describe divine judgment on Babylon (Jeremiah 51:2) and false prophets (Jeremiah 23:28). John the Baptist's prophecy of the coming Messiah employs the winnowing fork as the central image: the one who comes after him will thoroughly purge his threshing floor, gathering the wheat into his barn but burning the chaff with unquenchable fire (Matthew 3:12; Luke 3:17) — judgment that separates the genuine from the counterfeit.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "winnow"},
        "key_refs": ["Ruth 3:2", "Isaiah 30:24", "Matthew 3:12", "Jeremiah 51:2"]
    },
    "wise-men": {
        "id": "wise-men",
        "term": "Wise men",
        "category": "concepts",
        "intro": "<p>Wise men in Scripture appear in two distinct senses. In the Old Testament, particularly in Daniel 2:12, \"wise men\" (<em>chakamin</em>) designates the class of royal counsellors and diviners at the Babylonian court — a profession that included astrologers, Chaldeans, soothsayers, and enchanters whose esoteric knowledge was employed in interpreting omens and advising the king. When Nebuchadnezzar demanded that they tell him his dream without being told what it was, they failed, and Daniel alone succeeded through divine revelation. In the New Testament, the Magi (Greek <em>magoi</em>, translated \"wise men\" in Matthew 2:1–12) were Gentile scholars from the east — likely Mesopotamia or Persia — who observed a star signifying the birth of the King of the Jews and came to worship him. The number of Magi is not given in Matthew (the tradition of three derives from the number of gifts). Their coming fulfilled prophetic types of Gentiles bringing tribute to Israel's king (Isaiah 60:3, 6; Psalm 72:10–11).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wise-men", "smith": "wise-men", "isbe": "wise-men"},
        "key_refs": ["Daniel 2:12", "Matthew 2:1", "Matthew 2:11", "Isaiah 60:3"]
    },
    "wise-wisdom": {
        "id": "wise-wisdom",
        "term": "Wise, wisdom",
        "category": "concepts",
        "intro": "<p>Wisdom in biblical thought is fundamentally a moral and relational quality rather than merely an intellectual one. Proverbs 1:7 and 9:10 declare that \"the fear of the LORD is the beginning of wisdom\" — locating wisdom's source in covenant relationship with God rather than in human cleverness or learning. To be \"foolish\" in the biblical sense is to act as if God does not exist or does not matter (Psalm 14:1). The wisdom literature (Proverbs, Ecclesiastes, Job, Psalms, Song of Solomon) explores practical wisdom in every domain of life — speech, work, relationships, wealth, suffering, pleasure. \"Wisdom\" also became a personification in Proverbs 8–9, where Wisdom speaks in the first person as God's co-worker in creation — a passage that influenced New Testament Christology. In the New Testament, Christ is called the wisdom of God (1 Corinthians 1:24, 30), and the contrast between worldly wisdom and divine wisdom is a major theme of 1 Corinthians 1–3. James 1:5 promises that God will give wisdom liberally to those who ask in faith.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wise-wisdom"},
        "key_refs": ["Proverbs 1:7", "Proverbs 8:22", "1 Corinthians 1:24", "James 1:5"]
    },
    "witch": {
        "id": "witch",
        "term": "Witch",
        "category": "concepts",
        "intro": "<p>Witch in the Old Testament translates the Hebrew <em>mekhashshepheh</em> (feminine) or <em>mekhashsheph</em> (masculine), from the root <em>kashaph</em>, meaning to practice sorcery or use magical arts. The Mosaic law pronounced the death penalty on anyone who practiced sorcery: \"Thou shalt not suffer a witch to live\" (Exodus 22:18). Deuteronomy 18:10 lists similar prohibitions: \"There shall not be found among you... one who practices witchcraft.\" The broader context makes clear that such practices were associated with the religions of Canaan and represented a form of seeking guidance and power from sources other than the LORD. Saul's desperate consultation of the medium of Endor (1 Samuel 28:7–25) — condemned as a witch-like consultation — illustrates the trajectory of one who has turned from God. The prohibition of witchcraft was grounded not merely in social harm but in theological principle: all hidden knowledge and occult power belongs to God, and seeking it through other channels is a rejection of his sovereignty and a form of idolatry.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "witch"},
        "key_refs": ["Exodus 22:18", "Deuteronomy 18:10", "1 Samuel 28:7"]
    },
    "witchcraft": {
        "id": "witchcraft",
        "term": "Witchcraft",
        "category": "concepts",
        "intro": "<p>Witchcraft in Scripture denotes the practice of divination, sorcery, and occult arts in general — the attempt to access supernatural knowledge or power through means other than direct approach to the LORD. Samuel equates Saul's disobedience with witchcraft: \"Rebellion is as the sin of witchcraft, and stubbornness is as iniquity and idolatry\" (1 Samuel 15:23), indicating that witchcraft's core sin is the rejection of God's authority in favour of one's own will. Jezebel's influence over Israel is characterised as witchcraft (2 Kings 9:22). Manasseh's apostasy included witchcraft (2 Chronicles 33:6). Micah prophesies that God will cut off witchcraft from the land (Micah 5:12) as part of the purification of the messianic age. In the New Testament, the Greek <em>pharmakeia</em> (from which \"pharmacy\" derives) — usually translated \"sorcery\" or \"witchcraft\" — appears in Galatians 5:20 as a work of the flesh and in Revelation 9:21; 18:23; 21:8; 22:15 as a characteristic sin of the unredeemed. The term's root in drug-use suggests that ancient sorcery often involved the use of substances to induce altered states.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "witchcraft"},
        "key_refs": ["1 Samuel 15:23", "2 Kings 9:22", "Galatians 5:20", "Micah 5:12"]
    },
    "witness": {
        "id": "witness",
        "term": "Witness",
        "category": "concepts",
        "intro": "<p>Witness in Scripture encompasses both the legal requirement of testimony and the theological concept of bearing testimony to God's truth. Mosaic law required at least two witnesses for any capital charge (Deuteronomy 17:6; 19:15) — a safeguard against false accusation that the New Testament extends to church discipline (Matthew 18:16; 2 Corinthians 13:1). The false witness was to receive the punishment he sought for the accused (Deuteronomy 19:16–21). The bearing of false witness is explicitly prohibited in the Decalogue (Exodus 20:16; Deuteronomy 5:20) as a sin against both neighbour and truth. In the prophets and Psalms, God himself is invoked as witness between parties (Genesis 31:50; Malachi 2:14). In the New Testament, the concept expands: Jesus calls his disciples to be his witnesses throughout the world (Acts 1:8), the word <em>martus</em> (witness) becoming the root of \"martyr\" as faithful testimony to Christ led to death. The Holy Spirit is called a witness to Christ (John 15:26), and God is called as witness by Paul (Romans 1:9; 2 Corinthians 1:23).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "witness", "smith": "witness", "isbe": "witness"},
        "key_refs": ["Deuteronomy 19:15", "Exodus 20:16", "Acts 1:8", "John 15:26"]
    },
    "witness-of-the-spirit": {
        "id": "witness-of-the-spirit",
        "term": "Witness of the Spirit",
        "category": "concepts",
        "intro": "<p>The witness of the Spirit refers to the inward testimony of the Holy Spirit that believers are the children of God, described in Romans 8:16: \"The Spirit himself bears witness with our spirit that we are children of God.\" Paul's statement indicates a dual testimony — the believer's own spirit and the Holy Spirit bearing concurrent witness — producing the inner assurance of adoption. This is closely connected to the preceding verse (Romans 8:15), where Paul describes crying out \"Abba, Father\" by the Spirit of adoption, identifying the Trinitarian ground of this assurance: the Spirit of God's Son cries the Son's own word for God in the heart of the adopted child. The same reality underlies Galatians 4:6: \"God sent the Spirit of his Son into our hearts, crying, 'Abba! Father!'\" The witness of the Spirit became a central concept in Reformed and Puritan theology of assurance, and played a prominent role in John Wesley's doctrine of assurance of salvation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "witness-of-the-spirit", "isbe": "witness-of-the-spirit"},
        "key_refs": ["Romans 8:16", "Romans 8:15", "Galatians 4:6", "1 John 5:10"]
    },
    "wizard": {
        "id": "wizard",
        "term": "Wizard",
        "category": "concepts",
        "intro": "<p>A wizard (Hebrew <em>yid'oni</em>, \"a knowing one,\" from <em>yada'</em>, \"to know\") was a person who claimed to possess secret knowledge through contact with a familiar spirit — a spirit of the dead or a demonic being who provided information about hidden or future things. The Mosaic law prohibited seeking wizards (Leviticus 19:31; 20:6) and decreed death for anyone who possessed a familiar spirit or was a wizard (Leviticus 20:27). Wizards are frequently paired with mediums (<em>'ovot</em>) in the law and the historical books, representing two related forms of divination through contact with the spirit world. Saul expelled wizards and mediums from Israel early in his reign (1 Samuel 28:3) but later consulted the medium of Endor in desperation — a final apostasy. Isaiah's condemnation of the people for consulting \"wizards that peep and that mutter\" (Isaiah 8:19) uses the imagery of faint spirit-sounds to expose the futility and debasement of seeking the dead rather than the living God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wizard", "smith": "wizard", "isbe": "wizard"},
        "key_refs": ["Leviticus 19:31", "Leviticus 20:27", "1 Samuel 28:3", "Isaiah 8:19"]
    },
    "wolf": {
        "id": "wolf",
        "term": "Wolf",
        "category": "concepts",
        "intro": "<p>The wolf (Hebrew <em>ze'ev</em>; Greek <em>lukos</em>) was the dominant large predator of ancient Palestine, preying on sheep and goats and thus a constant threat to shepherding communities. Its characteristics — nocturnal habit, ravenous hunger, and pack behaviour — made it a powerful symbol of treachery, violence, and dangerous leadership. The dying blessing of Jacob calls Benjamin \"a wolf that raveneth\" (Genesis 49:27). Zephaniah 3:3 describes the princes of Jerusalem as \"evening wolves\" who leave no bone till morning. Ezekiel 22:27 applies the same image to the corrupt officials of Israel. Jesus employs the wolf as the archetypal image of false teachers and those who prey on the flock: \"Beware of false prophets, which come to you in sheep's clothing, but inwardly they are ravening wolves\" (Matthew 7:15), and warns that he sends his disciples \"as sheep in the midst of wolves\" (Matthew 10:16). The eschatological reversal of the wolf's nature — \"The wolf also shall dwell with the lamb\" (Isaiah 11:6; 65:25) — pictures the transformation of the age of redemption.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wolf", "smith": "wolf", "isbe": "wolf"},
        "key_refs": ["Genesis 49:27", "Matthew 7:15", "Isaiah 11:6", "John 10:12"]
    },
    "woman": {
        "id": "woman",
        "term": "Woman",
        "category": "concepts",
        "intro": "<p>Woman in Scripture is presented from creation as the equal partner and counterpart of man: made from Adam's rib (Genesis 2:21–23), named <em>ishshah</em> (woman) because she was taken from <em>ish</em> (man), and designed as his \"help meet\" — a corresponding helper (Genesis 2:18). The fall narrative records the serpent's approach through Eve and the resulting judgment, which includes pain in childbearing and the marring of the relationship between man and woman (Genesis 3:16). Nevertheless, women occupy prominent roles throughout the biblical narrative: Deborah as judge and prophetess (Judges 4–5), Hannah as a model of faithful prayer (1 Samuel 1–2), Esther as deliverer of her people, and the prophets' imagery of faithful Israel as a woman. In the New Testament, women were among Jesus's most faithful disciples and the first witnesses to the resurrection. Paul affirms that in Christ \"there is neither male nor female\" as a statement of equal standing in salvation (Galatians 3:28), while maintaining ordered roles in marriage and corporate worship (1 Corinthians 11; Ephesians 5).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "woman", "isbe": "woman"},
        "key_refs": ["Genesis 2:22", "Genesis 2:23", "Galatians 3:28", "Judges 4:4"]
    },
    "wood": {
        "id": "wood",
        "term": "Wood",
        "category": "concepts",
        "intro": "<p>Wood (<em>ets</em> in Hebrew, used for both the material and the living tree) was a foundational building and fuel material throughout the biblical world. Lebanon's cedar forests supplied the premium timber for Solomon's temple (1 Kings 5:6–10; 2 Chronicles 2:8) and his palace (1 Kings 7:2–3). Acacia (<em>shittim</em>) wood from the Sinai was the primary material for the tabernacle's structural elements, the ark of the covenant, and the furniture (Exodus 25–27). The tabernacle also required abundant wood for its altar's burnt offerings. Isaiah uses wood-cutting as an extended illustration of idolatry's absurdity: a man cuts down a tree, uses half for fuel and warmth, and fashions the other half into an idol to worship (Isaiah 44:14–17). Paul uses building materials including wood in his image of the quality of ministry work in 1 Corinthians 3:12–15: gold, silver, and precious stones survive the fire of judgment; wood, hay, and stubble do not.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wood", "smith": "wood", "isbe": "wood"},
        "key_refs": ["1 Kings 5:6", "Exodus 25:5", "Isaiah 44:14", "1 Corinthians 3:12"]
    },
    "wood-offering": {
        "id": "wood-offering",
        "term": "Wood-offering",
        "category": "concepts",
        "intro": "<p>The wood-offering was a contribution of wood by the people and priests to maintain the perpetual fire on the altar of burnt offering in the temple, prescribed in Leviticus 6:12–13: \"The fire upon the altar shall be burning in it; it shall not be put out.\" During the period of Nehemiah's reforms, when normal temple revenues had been disrupted, a specific lot was cast among the people to determine which families would provide wood at appointed times (Nehemiah 10:34; 13:31). This arrangement appears to have developed into a formal system of wood donations by various families on designated days. The Mishnah (tractate Taanit 4:5) lists nine days on which different families brought wood. The wood-offering illustrates the entire community's share in maintaining the temple worship — not only the priests and Levites but all Israel had a role in sustaining the continual fire that symbolised God's ongoing acceptance of Israel's worship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wood-offering"},
        "key_refs": ["Nehemiah 10:34", "Nehemiah 13:31", "Leviticus 6:13"]
    },
    "wool": {
        "id": "wool",
        "term": "Wool",
        "category": "concepts",
        "intro": "<p>Wool (Hebrew <em>tsemer</em>) was the primary textile fibre of ancient Israel, obtained by shearing sheep and used to make clothing, blankets, and trade goods. Sheep-shearing was an occasion for celebration (1 Samuel 25:2–4; 2 Samuel 13:23). The Levitical law prohibited mixing wool and linen in the same garment (Deuteronomy 22:11; Leviticus 19:19) — a prohibition whose rationale is debated but may be connected to priestly garments or the boundary-keeping symbolism of the law. Naaman offered among his gifts of gratitude to Elisha ten changes of clothing — costly items in the ancient world (2 Kings 5:5). Proverbs 31:13 credits the capable wife with seeking wool and flax and working willingly with her hands. Isaiah 1:18 uses snow-white wool as a metaphor for the completeness of divine cleansing: \"though your sins be as scarlet, they shall be as white as snow; though they be red like crimson, they shall be as wool.\" The vision of the Ancient of Days in Daniel 7:9 describes his garment as white as snow and the hair of his head as pure wool.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wool", "smith": "wool", "isbe": "wool"},
        "key_refs": ["Leviticus 19:19", "Deuteronomy 22:11", "Isaiah 1:18", "Daniel 7:9"]
    },
    "word-of-god": {
        "id": "word-of-god",
        "term": "Word of God",
        "category": "concepts",
        "intro": "<p>The Word of God in Scripture designates both the spoken divine address to humanity and the written record of that address — ultimately understood as one coherent testimony. Hebrews 4:12 describes the written Word as \"living and active, sharper than any two-edged sword, piercing to the division of soul and of spirit, of joints and of marrow, and discerning the thoughts and intentions of the heart.\" 2 Timothy 3:16–17 grounds the Scripture's authority in inspiration: \"All Scripture is breathed out by God and profitable for teaching, for reproof, for correction, and for training in righteousness.\" John 17:17 identifies the word with sanctifying truth: \"Thy word is truth.\" Psalm 119 is entirely devoted to celebrating the many dimensions of God's revealed word — its reliability, life-giving character, and function as a lamp and light. In the prophetic tradition, the \"word of the LORD\" that came to the prophets was experienced as a powerful, external address that compelled proclamation (Jeremiah 20:9; Amos 3:8). Peter affirms that no prophecy came from human will but from the Holy Spirit carrying along the human authors (2 Peter 1:21).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "word-of-god"},
        "key_refs": ["Hebrews 4:12", "2 Timothy 3:16", "John 17:17", "Psalms 119:105"]
    },
    "word-the": {
        "id": "word-the",
        "term": "Word, The",
        "category": "concepts",
        "intro": "<p>The Word (<em>ho Logos</em>) is one of the titles of the Lord Jesus Christ, used exclusively in the Johannine writings. John's Gospel opens with the theological declaration: \"In the beginning was the Word, and the Word was with God, and the Word was God\" (John 1:1). The prologue (John 1:1–18) grounds the incarnation in the eternal divine Logos: the one who was in the beginning with God, through whom all things were made, became flesh and dwelt among us (John 1:14). The title also appears in 1 John 1:1, where the author bears witness to \"the Word of life\" that he has heard, seen, and touched — anchoring the Logos theology in concrete historical testimony. Revelation 19:13 uses the title for the rider on the white horse at the final judgment: \"his name is called The Word of God.\" The use of <em>Logos</em> had deep resonance in both Jewish (where the Word was God's creative and revelatory agent) and Greek philosophical (where the Logos was the rational principle of the universe) contexts, making it a bridge concept for the proclamation of Christ.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "word-the"},
        "key_refs": ["John 1:1", "John 1:14", "1 John 1:1", "Revelation 19:13"]
    },
    "works-covenant-of": {
        "id": "works-covenant-of",
        "term": "Works, Covenant of",
        "category": "concepts",
        "intro": "<p>The Covenant of Works is a theological term used in Reformed covenant theology to describe the arrangement established by God with Adam in the Garden of Eden before the fall — a conditional covenant in which life and continued blessing were contingent on Adam's obedience. The term is not found in Scripture but is derived from the structure of Genesis 2–3: God placed Adam in the garden with abundant provision, gave him a specific command (Genesis 2:16–17), and attached the sanction of death to disobedience. The parallel between Adam and Christ in Romans 5:12–21 and 1 Corinthians 15:45–49, where Paul calls Adam \"a type of the one who was to come\" and contrasts the disobedience of the first Adam with the obedience of the second, provides the New Testament basis for seeing Adam's probationary role in covenantal terms. The Covenant of Works is contrasted with the Covenant of Grace — the post-fall divine arrangement to save through the promised Seed of the woman (Genesis 3:15) — which is fulfilled in Christ, who perfectly satisfied the demands the first Adam failed to meet.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "works-covenant-of"},
        "key_refs": ["Genesis 2:17", "Romans 5:12", "Romans 5:19", "1 Corinthians 15:45"]
    },
    "works-good": {
        "id": "works-good",
        "term": "Works, Good",
        "category": "concepts",
        "intro": "<p>Good works in Scripture are the fruit of salvation, not its ground. Paul's foundational statement in Ephesians 2:8–10 resolves the apparent tension: \"For by grace you have been saved through faith. And this is not your own doing; it is the gift of God, not a result of works, so that no one may boast. For we are his workmanship, created in Christ Jesus for good works, which God prepared beforehand, that we should walk in them.\" Salvation is entirely by grace through faith; good works are the prepared pathway that flows from it. James 2:17–18 makes the complementary point: faith without works is dead, and genuine faith is demonstrated by works — not earning salvation but evidencing it. Jesus declares that the light of believers' good works should shine before others so that they may glorify the Father (Matthew 5:16). Paul writes to Titus that Christ gave himself to purify a people \"zealous for good works\" (Titus 2:14), and the pastoral epistles repeatedly emphasise readiness for good works as a mark of genuine godliness (1 Timothy 6:18; 2 Timothy 3:17; Titus 3:1).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "works-good"},
        "key_refs": ["Ephesians 2:8", "Ephesians 2:10", "James 2:18", "Matthew 5:16"]
    },
    "worm": {
        "id": "worm",
        "term": "Worm",
        "category": "concepts",
        "intro": "<p>Worm in the Bible translates several Hebrew terms covering different creatures and carrying different connotations. The <em>sas</em> (Isaiah 51:8) is the clothes-moth caterpillar that destroys garments. The <em>rimmah</em> (Exodus 16:20, 24; Job 25:6) is the maggot or putrefying worm, a symbol of decay and death — the manna that was kept overnight bred worms and stank (Exodus 16:20), and Job uses the worm as the ultimate image of human insignificance and mortality (Job 25:6). The Psalmist's famous self-description in Psalm 22:6, \"I am a worm, and no man; a reproach of men, and despised of the people,\" combines the worm's associations of lowliness and vulnerability with the context of extreme suffering and public shame — language the New Testament understands as prophetic of Christ on the cross. In the teaching of Jesus, Gehenna is described as a place where \"their worm dieth not, and the fire is not quenched\" (Mark 9:44–48, citing Isaiah 66:24), using the image of worms feeding on the perpetually burning refuse of the city as an image of unending divine judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "worm", "smith": "worm"},
        "key_refs": ["Psalms 22:6", "Job 25:6", "Isaiah 51:8", "Mark 9:44"]
    },
    "wormwood": {
        "id": "wormwood",
        "term": "Wormwood",
        "category": "concepts",
        "intro": "<p>Wormwood (Hebrew <em>la'anah</em>; Greek <em>apsinthos</em>) is the <em>Artemisia absinthium</em> of botanists, an intensely bitter plant used to produce absinthe and noted throughout the ancient world for its bitterness. In Scripture it consistently serves as an image of bitter consequence, judgment, and moral corruption. Deuteronomy 29:18 warns against the root of bitterness that bears gall and wormwood — the idolater whose influence poisons the community. Proverbs 5:4 describes the adulteress: \"her end is bitter as wormwood.\" Amos 5:7 pronounces woe on those who \"turn judgment to wormwood\" — making justice bitter rather than sweet. Jeremiah uses wormwood as an image of God's judgment on unfaithful Israel (Jeremiah 9:15; 23:15). In Revelation 8:11, one of the seven trumpets is named Wormwood: when a great star falls into rivers and springs of water, a third of the waters become bitter \"as wormwood\" and many people die — a judgment on corrupted life-sources mirroring the bitter waters of Marah (Exodus 15:23–25).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wormwood", "smith": "wormwood", "isbe": "wormwood"},
        "key_refs": ["Deuteronomy 29:18", "Proverbs 5:4", "Amos 5:7", "Revelation 8:11"]
    },
    "worship": {
        "id": "worship",
        "term": "Worship",
        "category": "concepts",
        "intro": "<p>Worship in Scripture denotes the honour, reverence, and devotion rendered to God — an honour that is his alone and that it is idolatry to render to any creature. The Hebrew <em>shachah</em> (to bow down, prostrate oneself) and the Greek <em>proskuneo</em> (to kiss the hand toward, bow in homage) are the primary words, both capturing the posture of submission before divine greatness. The Shema (Deuteronomy 6:4–5) and the first two commandments (Exodus 20:3–6) establish exclusive worship of the LORD as the foundation of covenant life. The prophets condemn Israel's worship of idols as both spiritual adultery and rational absurdity (Isaiah 44:9–20; Jeremiah 10:1–16). In Acts 10:25–26, Peter refuses Cornelius's prostration, and in Revelation 22:8–9, the angel refuses John's worship, directing him to worship God alone. Jesus declares that true worshippers will worship \"in spirit and truth\" (John 4:23–24) — not tied to a location or external rite but rooted in authentic encounter with the God who is Spirit. Christian worship centres on the Trinitarian God revealed in Christ and mediated by the Spirit.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "worship", "isbe": "worship"},
        "key_refs": ["Exodus 20:3", "John 4:23", "Acts 10:25", "Revelation 22:9"]
    },
    "worshipper": {
        "id": "worshipper",
        "term": "Worshipper",
        "category": "concepts",
        "intro": "<p>Worshipper in the New Testament most distinctively appears in Acts 19:35, where the Greek <em>neokoros</em> (literally \"temple-sweeper\" or \"temple-warden\") is applied to the city of Ephesus: the city clerk calms the riotous crowd by reminding them that \"the city of the Ephesians is a worshipper [neokoros] of the great goddess Diana\" — meaning that Ephesus held the officially recognized status as guardian city of the Artemis temple, one of the Seven Wonders of the ancient world. The title <em>neokoros</em> was a formal civic honour awarded by Rome to cities that hosted an imperial cult temple, and Ephesus held it multiple times over. The speech of the city clerk in Acts 19:35–41 is a masterpiece of civic pragmatism, using the city's prestigious status to argue against the riot on grounds of Roman order rather than theology. The episode illuminates the civic and economic stakes of Paul's mission: the gospel's success in Ephesus threatened not merely a religious tradition but the city's identity and economic base.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "worshipper", "smith": "worshipper", "isbe": "worshipper"},
        "key_refs": ["Acts 19:35"]
    },
    "wrestle": {
        "id": "wrestle",
        "term": "Wrestle",
        "category": "concepts",
        "intro": "<p>Wrestling in Scripture carries both literal and metaphorical significance. The most theologically loaded instance is Jacob's nocturnal wrestling with the mysterious man at the ford of Jabbok (Genesis 32:22–32) — an encounter identified as divine (Genesis 32:30; Hosea 12:3–4) in which Jacob prevailed by clinging and would not let go until he received a blessing, and received both the blessing and a new name (Israel, \"he who strives with God\"). The episode established Jacob as the ancestor of a people defined by their striving with God, a pattern that shapes Israel's prayer life in the Psalms and prophets. Ephesians 6:12 uses the wrestling metaphor for spiritual conflict: \"For we do not wrestle against flesh and blood, but against the rulers, against the authorities, against the cosmic powers over this present darkness.\" Paul uses the athlete's vocabulary of intense bodily struggle to convey the seriousness and totality of the Christian's engagement with spiritual opposition, resolved not by human strength but by the full armour of God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "wrestle"},
        "key_refs": ["Genesis 32:24", "Genesis 32:28", "Ephesians 6:12", "Hosea 12:3"]
    },
    "writing": {
        "id": "writing",
        "term": "Writing",
        "category": "concepts",
        "intro": "<p>Writing in the biblical world is attested from the earliest periods of Israelite history and presupposed as a known art throughout the Old Testament. Exodus 17:14 — \"Write this for a memorial in a book\" — is the first command to write in the Pentateuch, followed quickly by God himself writing the Ten Commandments on stone tablets (Exodus 31:18; 32:15–16). The ancient Hebrew script (Proto-Sinaitic/Phoenician) was a consonantal alphabet of approximately 22 letters, a dramatic simplification from the hundreds of Sumerian cuneiform or Egyptian hieroglyphic signs, making literacy more widely accessible. Writing materials included stone tablets (Exodus 24:12), clay (Ezekiel 4:1), wooden tablets (Isaiah 30:8; Habakkuk 2:2), papyrus (imported from Egypt), and leather/vellum. Ink made from charcoal or lampblack was used with a reed pen (Jeremiah 36:18; 3 John 13). The New Testament was written on papyrus and later vellum in Greek, the Mediterranean world's common language. The entire biblical canon was produced through the writing of divinely inspired human authors over roughly fifteen hundred years.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "writing", "smith": "writing", "isbe": "writing"},
        "key_refs": ["Exodus 17:14", "Exodus 31:18", "Jeremiah 36:18", "2 Timothy 3:16"]
    },
}


def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP w: Wafers → Writing: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
