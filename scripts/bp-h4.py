"""
BP Article Synthesis — h4: Hillel → Hyssop
Covers Easton entries: Hillel through Hyssop (69 entries)

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

Script: scripts/bp-h4.py
Run: python3 scripts/bp-h4.py
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


# ── Article data ──────────────────────────────────────────────────────────────
ARTICLES = {
    "hillel": {
        "id": "hillel",
        "term": "Hillel",
        "category": "people",
        "intro": "<p>Hillel the Pirathonite was the father of Abdon, one of the so-called minor judges of Israel who served after Elon the Zebulunite. Abdon son of Hillel judged Israel for eight years and is remembered for his forty sons and thirty grandsons who rode on seventy donkeys—a detail that conveyed the prosperity and honor of his household. Hillel himself receives mention only as Abdon's father, placing him among the Ephraimite families of Pirathon in the hill country of Ephraim.</p><p>His name, meaning <em>he that praises</em> or <em>praising</em>, was also borne by the great Babylonian rabbi Hillel the Elder (first century BC), whose school became one of the two dominant branches of early rabbinic interpretation. The biblical Hillel is entirely distinct from this later figure but shares a name that became prominent in Jewish tradition. The brief reference in Judges 12:13 places him in the succession of tribal leaders who maintained order in the period before the monarchy.</p>",
        "sections": [],
        "hitchcock_meaning": "he that praises",
        "source_ids": {
            "easton": "hillel",
            "smith": "hillel",
            "isbe": "hillel"
        },
        "key_refs": ["Judges 12:13", "Judges 12:15"]
    },
    "hind": {
        "id": "hind",
        "term": "Hind",
        "category": "concepts",
        "intro": "<p>The hind (Hebrew <em>ʾayālâ</em>, feminine form of <em>ʾayyāl</em>, stag) is the female red deer or related deer species that figured prominently in the poetry and imagery of ancient Israel. In the arid landscape of Palestine, the deer's grace and sure-footedness on mountainous terrain made it a natural metaphor for spiritual vitality. David's thanksgiving psalm declares, <em>He makes my feet like the feet of a deer and sets me secure on the heights</em> (2 Samuel 22:34; Psalm 18:33)—celebrating divine empowerment for difficult terrain.</p><p>The hind appears in the title of Psalm 22 (<em>The Doe of the Dawn</em>), where it likely denotes a musical setting or tune. In the Song of Solomon the beloved's eyes are compared to those of a dove, and her lover leaps over mountains like a gazelle or young stag (2:9, 17). Proverbs 5:19 commends the faithful wife using the image of a loving hind. The hind nursing her young in Lamentations 1:6 and abandoning them in the famine of Lamentations 4:3 serves as a metaphor for Zion's desperate state. The animal's association with freedom, beauty, and agility gave it particular resonance in Hebrew poetry.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hind",
            "smith": "hind",
            "isbe": "hind"
        },
        "key_refs": ["2 Samuel 22:34", "Psalm 18:33", "Psalm 22:1", "Proverbs 5:19"]
    },
    "hinge": {
        "id": "hinge",
        "term": "Hinge",
        "category": "concepts",
        "intro": "<p>The hinge in biblical usage refers to the pivot mechanism on which ancient doors turned. The Hebrew <em>ṣîr</em> describes this turning post rather than the metal hinge plates familiar in modern construction. Ancient Near Eastern doors typically rotated on a vertical wooden or stone post that fit into a socket in the floor threshold and a bracket above, turning with the door's movement rather than being fastened to the door frame at multiple points.</p><p>The hinge appears in two memorable biblical contexts. Proverbs 26:14 uses it for comic effect: <em>As a door turns on its hinges, so does a sluggard on his bed</em>—the sluggard swings back and forth as lazily as a door, going nowhere despite constant motion. The two mentions in 1 Kings 7:50 and Ezekiel 45:19 refer to the door hinges of the temple, made of gold in Solomon's construction. Archaeological evidence from ancient Near Eastern sites confirms the pivot-socket system: stone threshold sockets with worn circular grooves testify to centuries of daily door movement.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hinge",
            "smith": "hinge",
            "isbe": "hinge"
        },
        "key_refs": ["1 Kings 7:50", "Proverbs 26:14"]
    },
    "hinnom": {
        "id": "hinnom",
        "term": "Hinnom",
        "category": "places",
        "intro": "<p>Hinnom (the Valley of the Son of Hinnom, Hebrew <em>gê ben-hinnōm</em>) was a deep, narrow ravine running along the southern and western sides of Jerusalem, separating the hill of Zion from the so-called Hill of Evil Counsel. The name derives from an otherwise unidentified figure called the son (or sons) of Hinnom, perhaps a pre-Israelite landowner. Its topographic position made it a natural boundary and drainage channel for the ancient city.</p><p>The valley became infamous as the site of Molech worship, where apostate Israelites—including at times kings Ahaz and Manasseh—burned their children in fire as offerings. King Josiah defiled the site as part of his religious reforms, making it unfit for continued worship. Its accursed association gave rise to the Greek form <em>Gehenna</em> (contracted from <em>gê hinnōm</em>), which Jesus used as a vivid image of eschatological judgment. In later Jewish and Christian imagination, Gehenna became the designation for the place of final punishment—a theological evolution rooted in the historical horror of what had occurred in this ravine beneath Jerusalem's walls.</p>",
        "sections": [],
        "hitchcock_meaning": "there they are; their riches",
        "source_ids": {
            "easton": "hinnom",
            "smith": "hinnom",
            "isbe": "hinnom-valley-of"
        },
        "key_refs": ["Joshua 15:8", "2 Kings 23:10", "Jeremiah 7:31", "Matthew 5:22"]
    },
    "hiram": {
        "id": "hiram",
        "term": "Hiram",
        "category": "people",
        "intro": "<p>Hiram (also written Huram) was the Phoenician king of Tyre who maintained close diplomatic and commercial ties with both David and Solomon. His name, meaning <em>exaltation of life</em> or <em>noble-born</em>, reflects the prestige of the Tyrian royal house. He sent cedar timber and skilled craftsmen to David for the construction of the royal palace, and he later entered into an extensive treaty with Solomon for the supply of cedar and cypress timber and gold in exchange for grain and oil—a partnership that fueled Solomon's building projects including the Jerusalem temple.</p><p>A second Hiram (also called Huram-abi) was the master craftsman sent by King Hiram to work on the temple furnishings: the son of a Tyrian man and an Israelite woman from the tribe of Naphtali (or Dan in Chronicles), he cast the two bronze pillars Jachin and Boaz, the bronze sea and its twelve oxen, the ten lavers, and all the bronze work of the temple complex. His combined Phoenician-Israelite heritage made him the embodiment of the international character of Solomon's building enterprise. The alliance between Israel and Tyre represented the high-water mark of Solomonic economic and diplomatic power.</p>",
        "sections": [],
        "hitchcock_meaning": "exaltation of life; a destroyer",
        "source_ids": {
            "easton": "hiram",
            "isbe": "hiram"
        },
        "key_refs": ["2 Samuel 5:11", "1 Kings 5:1", "1 Kings 7:13", "1 Kings 9:11"]
    },
    "hireling": {
        "id": "hireling",
        "term": "Hireling",
        "category": "concepts",
        "intro": "<p>A hireling in biblical usage was a wage laborer employed for a limited term, as distinguished from a slave (permanent property) or a bondslave (serving a fixed period to discharge debt). The Hebrew <em>śākîr</em> and Greek <em>misthios</em> designate one hired for pay, with the Mosaic law providing that day laborers must be paid the same day their work is done, before sunset, as they were typically poor and dependent on immediate payment for daily sustenance (Leviticus 19:13; Deuteronomy 24:14–15).</p><p>The hireling's legal protections under the law reflected Israel's memory of their own bondage in Egypt. In the prophets, the metaphor of the hireling whose days are defined and appointed appears in Job 7:1–2 to describe the brevity and toil of human life. Jesus's parable of the prodigal son has the younger son resolve to return as a hireling in his father's house—a deliberate step down from sonship. Most memorably, Jesus contrasts the good shepherd with the hireling (John 10:12–13), who flees when danger comes because he has no personal stake in the flock, making the hireling a figure for self-interested leadership as opposed to genuine pastoral care.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hireling",
            "isbe": "hireling"
        },
        "key_refs": ["Leviticus 19:13", "Deuteronomy 24:14", "Job 7:1", "John 10:12"]
    },
    "hiss": {
        "id": "hiss",
        "term": "Hiss",
        "category": "concepts",
        "intro": "<p>Hissing in the biblical world expressed contempt, scorn, or astonishment at the magnitude of a catastrophe. The Hebrew <em>šāraq</em> denotes a sharp whistling or hissing sound used as a gesture of mockery or shocked amazement, and it appears with striking frequency in the prophetic literature when describing the desolation of cities or nations under divine judgment. When Solomon's temple was destroyed and Jerusalem fell, passersby would hiss at the ruined city as a reflexive expression of horror and contempt.</p><p>The threat that Israel would become a hissing and a byword among the nations appears as one of the curses for covenant unfaithfulness (1 Kings 9:8; Jeremiah 19:8; 25:9; Micah 6:16). Zechariah 10:8 employs the same verb in a redemptive reversal: God will <em>hiss</em> (or whistle) for his scattered people to gather them back from exile, turning the signal of judgment into a shepherd's call for his flock. The dual usage—contemptuous scorn and shepherd's summons—reflects the range of associations the gesture carried in ancient Near Eastern culture.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hiss",
            "isbe": "hissing"
        },
        "key_refs": ["1 Kings 9:8", "Jeremiah 19:8", "Lamentations 2:15", "Zechariah 10:8"]
    },
    "hittites": {
        "id": "hittites",
        "term": "Hittites",
        "category": "people",
        "intro": "<p>The Hittites were one of the pre-Israelite peoples of Canaan and, more broadly, the rulers of a great empire centered in Anatolia (modern Turkey) that reached its height in the late Bronze Age (roughly 1400–1200 BC). In the table of nations (Genesis 10:15), the biblical Hittites are descended from Heth son of Canaan, making them a Semitic Canaanite group distinct from—though historically overlapping with—the Anatolian Hittite empire known from archaeology. Abraham purchased the cave of Machpelah from Ephron the Hittite, and Hittite neighbors appear throughout the patriarchal narratives as landowners and traders.</p><p>In the conquest narratives, Hittites are listed among the peoples Israel was to dispossess from Canaan. Uriah the Hittite, one of David's mighty men and the husband of Bathsheba, represents the integration of Hittite individuals into Israelite society at the highest levels. The great Anatolian Hittite empire, known from Egyptian records and its own cuneiform archives at Hattusa, was a major power that fought Egypt to a standstill at the Battle of Kadesh (c. 1274 BC) and concluded one of history's earliest known peace treaties. Their civilization collapsed around 1200 BC along with much of the Bronze Age eastern Mediterranean world.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hittites",
            "isbe": "hittites"
        },
        "key_refs": ["Genesis 10:15", "Genesis 23:10", "Joshua 3:10", "2 Samuel 11:3"]
    },
    "hivites": {
        "id": "hivites",
        "term": "Hivites",
        "category": "people",
        "intro": "<p>The Hivites were one of the pre-Israelite peoples of Canaan, listed among the nations to be displaced as Israel settled the land. Descended according to the table of nations from Canaan son of Ham (Genesis 10:17), they occupied the central mountain region and northern territories—from Hermon and Lebanon in the north to Gibeon in the south. The name has been interpreted as meaning <em>wicked</em> or <em>life-giver</em>, though the etymology remains uncertain.</p><p>Three significant Hivite encounters shape the biblical narrative. At Shechem, the Hivite prince Hamor (Emmor) negotiated with Jacob's sons for the marriage of Shechem to Dinah, ending catastrophically in the massacre by Simeon and Levi (Genesis 34). The Gibeonites, who deceived Joshua into a peace treaty through their famous ruse of worn-out sandals and moldy bread, were Hivites, and their treaty was honored even at great cost throughout the period of the monarchy. The Hivites of the Lebanon region provided Solomon's labor conscription for temple construction, suggesting a continued Hivite presence in the north well into the monarchic period.</p>",
        "sections": [],
        "hitchcock_meaning": "wicked; wickedness",
        "source_ids": {
            "easton": "hivites",
            "smith": "hivites",
            "isbe": "hivites"
        },
        "key_refs": ["Genesis 10:17", "Genesis 34:2", "Joshua 9:7", "Joshua 11:3"]
    },
    "hizkiah": {
        "id": "hizkiah",
        "term": "Hizkiah",
        "category": "people",
        "intro": "<p>Hizkiah was an ancestor of the prophet Zephaniah, named in the opening verse of Zephaniah's book as part of the unusually detailed genealogy tracing the prophet's lineage back four generations to a Hizkiah. Most commentators have identified this Hizkiah with the famous King Hezekiah of Judah, interpreting the extended genealogy as an effort to establish Zephaniah's royal credentials and explain his access to the court of King Josiah. If this identification is correct, Zephaniah was a great-great-grandson of Hezekiah.</p><p>The name Hizkiah means <em>the strength of the LORD</em>, a form related to the more common Hezekiah (<em>Yah strengthens</em>). The variant spelling in Zephaniah 1:1 distinguishes this reference from the king, though many scholars treat them as the same individual. The pedigree given to Zephaniah—son of Cushi, son of Gedaliah, son of Amariah, son of Hizkiah—is the longest prophetic genealogy in the Hebrew scriptures, suggesting this lineage carried particular significance for the book's original audience.</p>",
        "sections": [],
        "hitchcock_meaning": "the strength of the Lord",
        "source_ids": {
            "easton": "hizkiah",
            "smith": "hizkiah",
            "isbe": "hizkiah"
        },
        "key_refs": ["Zephaniah 1:1"]
    },
    "hizkijah": {
        "id": "hizkijah",
        "term": "Hizkijah",
        "category": "people",
        "intro": "<p>Hizkijah was one of the leaders of the people who set their seal to the solemn covenant renewal under Nehemiah, recorded in Nehemiah 10:17. The covenant, made after Ezra's public reading of the Law and the great day of national repentance in Nehemiah 9, committed the returned exiles to observe the Law of God as given through Moses, including provisions regarding sabbath observance, the sabbatical year, the temple tax, and the support of the Levites and priests.</p><p>The name Hizkijah, meaning <em>the strength of the LORD</em>, is a variant of Hezekiah. The individual named here is distinct from both King Hezekiah and the Hizkiah of Zephaniah's genealogy. He appears only in this sealing list without further narrative context. The covenant document of Nehemiah 10 represents one of the most significant acts of corporate religious commitment in the post-exilic period, and the named signatories—priests, Levites, and lay leaders—stood as witnesses and guarantors of the community's renewed dedication to Torah observance.</p>",
        "sections": [],
        "hitchcock_meaning": "the strength of the Lord",
        "source_ids": {
            "easton": "hizkijah"
        },
        "key_refs": ["Nehemiah 10:17"]
    },
    "hobab": {
        "id": "hobab",
        "term": "Hobab",
        "category": "people",
        "intro": "<p>Hobab was the son of Reuel the Midianite, identified in Numbers 10:29 as the father-in-law of Moses (though the Hebrew <em>ḥōtēn</em> can denote various in-law relationships, and some interpreters render it as brother-in-law). This has generated the question of how to reconcile Hobab son of Reuel with Jethro (<em>yitrô</em>), who is also identified as Moses's father-in-law. The most common harmonization identifies Reuel and Jethro as the same person (with Jethro as a title or alternate name) and Hobab as his son, making Hobab Moses's brother-in-law.</p><p>Moses appealed to Hobab to serve as a guide in the wilderness: <em>You know how we are to encamp in the wilderness, and you will serve as eyes for us</em> (Numbers 10:31). Hobab initially declined, wishing to return to his own land and people, but the ultimate outcome of the appeal is unrecorded—though Judges 1:16 and 4:11 suggest the Kenite descendants of Moses's father-in-law did join Israel, indicating Hobab relented. His name, meaning <em>beloved</em>, reflects the positive regard in which he was held by the Israelite community.</p>",
        "sections": [],
        "hitchcock_meaning": "favored; beloved",
        "source_ids": {
            "easton": "hobab",
            "smith": "hobab",
            "isbe": "hobab"
        },
        "key_refs": ["Numbers 10:29", "Numbers 10:31", "Judges 1:16", "Judges 4:11"]
    },
    "hobah": {
        "id": "hobah",
        "term": "Hobah",
        "category": "places",
        "intro": "<p>Hobah was a location north of Damascus to which Abraham pursued the coalition of four kings after his rescue of Lot from their captivity. Genesis 14:15 records that Abraham divided his forces, attacked the enemy by night, and chased them as far as Hobah, recovering all the spoils and captives. The exact site of Hobah is unknown; it lay to the north or northeast of Damascus, and the name meaning <em>hiding-place</em> or <em>secrecy</em> may suggest a concealed or remote location.</p><p>The pursuit from the battle near Dan (in the north of Canaan) all the way past Damascus to Hobah represents a remarkable military action covering several hundred miles, demonstrating both the geographic range of the Genesis 14 narrative and Abraham's determination to recover his kinsman. This episode is the only military action attributed to Abraham in the patriarchal narratives, and it establishes him as a figure of significant standing among the regional powers of his time. The specific identification of Hobah remains unresolved by archaeology.</p>",
        "sections": [],
        "hitchcock_meaning": "love; friendship; secrecy",
        "source_ids": {
            "easton": "hobah",
            "smith": "hobah",
            "isbe": "hobah"
        },
        "key_refs": ["Genesis 14:15"]
    },
    "hodijah": {
        "id": "hodijah",
        "term": "Hodijah",
        "category": "people",
        "intro": "<p>Hodijah (meaning <em>majesty of Jehovah</em> or <em>Yah is glory</em>) was the name of several individuals in the post-exilic community. The most prominent was a Levite who assisted Ezra in expounding the Law during the great public reading described in Nehemiah 8, standing on a wooden platform before the Water Gate and helping the people understand the text. The same Hodijah (or a closely related individual) also led the congregation in confession and praise during the covenant renewal ceremony of Nehemiah 9.</p><p>The name appears again among those who set their seal to the solemn covenant in Nehemiah 10, where two individuals named Hodijah are listed—one apparently a Levite and one a lay leader. The frequency of the name in this post-exilic period suggests it expressed the community's renewed emphasis on the honor and majesty of God after the trauma of exile. Hodijah represents the cadre of Levitical teachers who made the Torah accessible to the returned community and facilitated the spiritual renewal that Nehemiah's memoir describes.</p>",
        "sections": [],
        "hitchcock_meaning": "majesty of Jehovah",
        "source_ids": {
            "easton": "hodijah",
            "smith": "hodijah"
        },
        "key_refs": ["Nehemiah 8:7", "Nehemiah 9:5", "Nehemiah 10:10"]
    },
    "hoglah": {
        "id": "hoglah",
        "term": "Hoglah",
        "category": "people",
        "intro": "<p>Hoglah was one of the five daughters of Zelophehad of the tribe of Manasseh, who died in the wilderness without male heirs. When his daughters—Mahlah, Noah, Hoglah, Milcah, and Tirzah—petitioned Moses for their father's inheritance, God ruled in their favor, establishing the legal principle that daughters could inherit when there were no sons, provided they married within their own tribe to prevent transfer of tribal land (Numbers 27:1–11; 36:1–12).</p><p>The case of Zelophehad's daughters was landmark in Israelite law, cited explicitly in Numbers as a standing ordinance. Their names appear in three different lists (Numbers 26:33; 27:1; 36:11; Joshua 17:3), indicating the historical memory of the case was carefully preserved. Hoglah's name meaning <em>his festival</em> or <em>partridge</em> reflects the common use of animal or festivity names in ancient Israel. The daughters' inheritance was later confirmed in the tribal land allotments in Joshua, and the case remained the foundational precedent for daughters' inheritance rights in Israelite jurisprudence.</p>",
        "sections": [],
        "hitchcock_meaning": "his festival or dance",
        "source_ids": {
            "easton": "hoglah",
            "smith": "hoglah",
            "isbe": "hoglah"
        },
        "key_refs": ["Numbers 26:33", "Numbers 27:1", "Numbers 36:11", "Joshua 17:3"]
    },
    "hoham": {
        "id": "hoham",
        "term": "Hoham",
        "category": "people",
        "intro": "<p>Hoham king of Hebron was one of five Amorite kings who formed a coalition against Gibeon after the Gibeonites made a peace treaty with Joshua. When Gibeon appealed to Joshua for help, Israel marched overnight from Gilgal and launched a surprise attack, routing the coalition at the battle of Beth-horon. God aided Israel with a great hailstorm that killed more of the enemy than the sword, and it was during this battle that Joshua's famous prayer caused the sun to stand still over Gibeon.</p><p>After the battle, Hoham and the other four kings—Piram of Jarmuth, Japhia of Lachish, Debir of Eglon, and the king of Jerusalem Adoni-zedek—hid in a cave at Makkedah. Joshua sealed the cave entrance until the military operation was complete, then brought the kings out and had his commanders place their feet on their necks as a symbolic act of subjugation before executing them and hanging their bodies on trees. The episode established Israelite dominance over the entire southern hill country in a single campaign. Hoham's name means <em>Jehovah impels</em>.</p>",
        "sections": [],
        "hitchcock_meaning": "Jehovah impels",
        "source_ids": {
            "easton": "hoham",
            "smith": "hoham",
            "isbe": "hoham"
        },
        "key_refs": ["Joshua 10:3", "Joshua 10:22", "Joshua 10:26"]
    },
    "hold": {
        "id": "hold",
        "term": "Hold",
        "category": "concepts",
        "intro": "<p>A hold in the biblical sense was a stronghold, fortress, or refuge—a defensible position used as a hiding place or military base. The Hebrew terms <em>meṣûdâ</em> (stronghold, fastness) and <em>meṣad</em> (fort) are translated as hold or stronghold in many passages. David used a network of such positions during his years as a fugitive from Saul, seeking refuge in the limestone caves and rocky terrain of the Judean wilderness and the hill country of Moab.</p><p>First Samuel 22:4–5 records David leaving his family in the hold of Mizpeh of Moab while the prophet Gad directed him back to Judah, and 1 Samuel 24:22 notes his return to the stronghold after his encounter with Saul at En-gedi. The Philistine holdfast at Gibeah of God (1 Samuel 10:5) and the stronghold of Zion (2 Samuel 5:7) that David captured to make his royal city both illustrate the strategic importance of defensible high ground in Iron Age Palestine. The concept extends metaphorically: God himself is called the stronghold (<em>meṣûdâ</em>) and refuge of his people throughout the Psalms.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hold",
            "isbe": "stronghold"
        },
        "key_refs": ["1 Samuel 22:4", "1 Samuel 24:22", "2 Samuel 5:7", "Psalm 18:2"]
    },
    "holiness": {
        "id": "holiness",
        "term": "Holiness",
        "category": "concepts",
        "intro": "<p>Holiness (Hebrew <em>qōdeš</em>, Greek <em>hagiasmos</em> and <em>hagiosyne</em>) is one of the most fundamental attributes of God and the characteristic quality demanded of his people. In the highest sense, holiness belongs uniquely to God—the cry of the seraphim in Isaiah 6:3 and the song of the living creatures in Revelation 4:8, <em>Holy, holy, holy is the LORD of hosts</em>, establishes divine holiness as the supreme category of God's being. The Hebrew root <em>qds</em> conveys the idea of separation or distinctness: God is wholly other, set apart from all creaturely limitation, moral impurity, and corruption.</p><p>Because Israel was God's covenant people, holiness was not merely an attribute to be admired but a quality to be embodied: <em>Be holy, for I the LORD your God am holy</em> (Leviticus 19:2; 1 Peter 1:16). This imperative pervaded the entire structure of Israelite worship and daily life, touching diet, dress, land use, sexual ethics, and social relations. In the New Testament, holiness is understood as both positional (the believer is declared holy through Christ's atonement) and progressive (the Spirit works sanctification over time). The tension between the perfect holiness imputed by grace and the ongoing pursuit of practical holiness characterizes the New Testament's treatment of the subject.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "holiness",
            "isbe": "holiness"
        },
        "key_refs": ["Leviticus 19:2", "Isaiah 6:3", "1 Peter 1:15", "Hebrews 12:14"]
    },
    "holy-ghost": {
        "id": "holy-ghost",
        "term": "Holy Ghost",
        "category": "concepts",
        "intro": "<p>Holy Ghost is the older English designation for the Holy Spirit (Hebrew <em>rûaḥ haqqōdeš</em>, Greek <em>pneuma hagion</em>), the third person of the Trinity. The King James Version consistently used Ghost where modern versions prefer Spirit, reflecting the Germanic <em>geist</em> (spirit, mind) preserved in the English word ghost. Both terms render the same underlying Hebrew and Greek words without difference in theological meaning. The personality of the Holy Spirit is established in Scripture by the attributes assigned to him: he thinks (Romans 8:27), wills (1 Corinthians 12:11), speaks (Acts 13:2), grieves (Ephesians 4:30), and can be blasphemed (Matthew 12:31)—attributes that belong only to a personal being.</p><p>The Spirit's work spans both Testaments: in the Old Testament, the Spirit empowers leaders, prophets, and craftsmen; in the New, he convicts the world of sin, regenerates the believer, baptizes believers into the body of Christ, indwells and seals them, and distributes spiritual gifts. The Pentecost event in Acts 2 marks the distinctive new covenant gift of the Spirit in fulfillment of Joel's prophecy. Trinitarian theology affirms the Spirit as fully divine, co-equal and co-eternal with the Father and Son, proceeding from the Father (and in Western theology, from the Son—the <em>filioque</em> clause).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "holy-ghost",
            "isbe": "holy-spirit"
        },
        "key_refs": ["John 14:26", "Acts 2:4", "Romans 8:27", "Ephesians 4:30"]
    },
    "holy-of-holies": {
        "id": "holy-of-holies",
        "term": "Holy of Holies",
        "category": "concepts",
        "intro": "<p>The Holy of Holies (Hebrew <em>qōdeš haqqŏdāšîm</em>, Most Holy Place) was the innermost chamber of the tabernacle and later the temple, separated from the outer Holy Place by a heavy veil or curtain. It was a perfect cube—ten cubits in each dimension in the tabernacle, twenty cubits in the temple—and was left in total darkness. No natural light entered, and no one except the high priest was permitted to enter, and he only once a year on the Day of Atonement with blood for the atonement of the nation's sins.</p><p>The ark of the covenant with its golden mercy seat stood within the Holy of Holies, and the cherubim spread their wings over the mercy seat, between which the divine presence (<em>šekînâ</em>) dwelt. The veil separating the Holy Place from the Most Holy Place was torn in two from top to bottom at the moment of Christ's death (Matthew 27:51), an event interpreted by the Epistle to the Hebrews as the opening of direct access to God through Christ's priestly sacrifice. The Holy of Holies is thus both the paradigmatic space of divine dwelling in the old covenant and the type of the heavenly sanctuary where Christ ministers as eternal high priest.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "holy-of-holies",
            "isbe": "holy-of-holies"
        },
        "key_refs": ["Exodus 26:33", "Leviticus 16:2", "Matthew 27:51", "Hebrews 9:3"]
    },
    "holy-place": {
        "id": "holy-place",
        "term": "Holy Place",
        "category": "concepts",
        "intro": "<p>The Holy Place (Hebrew <em>haqqōdeš</em>) was the outer of the two interior divisions of the tabernacle and temple, separated from the courtyard by the entrance screen and from the Holy of Holies by the inner veil. In the tabernacle it measured twenty cubits long by ten cubits wide and ten cubits high; in Solomon's temple the proportions were doubled. It was accessible to the priests in their daily and weekly ministry, but not to ordinary Israelites.</p><p>Three pieces of furniture occupied the Holy Place: the golden lampstand (menorah) on the south side, giving light to the otherwise windowless room; the table of showbread on the north side, bearing twelve loaves renewed every Sabbath; and the golden altar of incense directly in front of the inner veil. The priests maintained the lamps, offered incense morning and evening, and replaced the showbread weekly. These three furnishings are interpreted in Hebrews 9 as types pointing to Christ: the light of the world, the bread of life, and the one mediator whose intercession is the true incense before God.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "holy-place",
            "isbe": "tabernacle"
        },
        "key_refs": ["Exodus 26:33", "Exodus 37:17", "Hebrews 9:2"]
    },
    "homer": {
        "id": "homer",
        "term": "Homer",
        "category": "concepts",
        "intro": "<p>The homer (Hebrew <em>ḥōmer</em>, meaning <em>heap</em> or <em>donkey-load</em>) was the largest standard unit of dry measure in ancient Israel, equivalent to ten ephahs and approximately eight to ten bushels in modern terms (estimates vary from about 55 to 220 liters, with most scholars settling around 220 liters or approximately 6.5 bushels). The homer thus represented the load a donkey could carry, giving it a practical basis in agricultural commerce.</p><p>The homer appears in legal and prophetic contexts. Leviticus 27:16 uses it to calculate land values for votive offerings—one homer of barley seed valued at fifty shekels of silver. Numbers 11:32 describes the immense quail harvest in the wilderness, where the least any individual gathered was ten homers. Hosea 3:2 records the prophet purchasing his estranged wife for fifteen shekels of silver and a homer and a half of barley. Ezekiel's sanctuary measurements (45:11–14) establish the homer as the standard from which the ephah and bath are derived, providing a unified metrology for the restored land. The homer's agricultural grounding made it the natural unit for grain transactions.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "homer",
            "smith": "homer",
            "isbe": "homer"
        },
        "key_refs": ["Leviticus 27:16", "Numbers 11:32", "Hosea 3:2", "Ezekiel 45:11"]
    },
    "honey": {
        "id": "honey",
        "term": "Honey",
        "category": "concepts",
        "intro": "<p>Honey in the biblical world referred both to the honey of wild bees (Hebrew <em>dĕbaš yĕʿārîm</em>, forest honey) and to a thick sweet syrup made from dates or grape must, the latter being the more common product in agricultural contexts. Palestine was proverbially a land flowing with milk and honey, a phrase occurring over twenty times in the Old Testament as a description of Canaan's fertility. Wild bees nested in rock crevices, hollow trees, and animal carcasses; the most dramatic honey incident in the Bible is Samson finding honeybees in the carcass of the lion he had killed, from which he drew his famous riddle.</p><p>Honey was valued as a luxury food and sweetener in a world without refined sugar. Jonathan tasted honey during a battle against the Philistines and was immediately refreshed, an episode that nearly cost him his life due to Saul's rash oath. The Psalms describe God's law as sweeter than honey (Psalm 19:10; 119:103), and Proverbs 24:13 commends honey as good for the soul. However, honey was excluded from grain offerings to God (Leviticus 2:11), possibly because fermented honey was associated with pagan worship. John the Baptist's diet of locusts and wild honey (Matthew 3:4) was a sign of austere wilderness existence.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "honey",
            "smith": "honey",
            "isbe": "honey"
        },
        "key_refs": ["Exodus 3:8", "Judges 14:8", "Psalm 19:10", "Matthew 3:4"]
    },
    "hood": {
        "id": "hood",
        "term": "Hood",
        "category": "concepts",
        "intro": "<p>Hood in biblical usage refers to a head covering or turban worn as an article of dress, rendered by the Hebrew <em>ṣānîph</em> and related terms. In Isaiah 3:23, the term appears in the long list of women's ornaments and garments that would be stripped away in judgment—turbans or head-tires among them. The same root is rendered <em>diadem</em> in Job 29:14, where Job describes his former honor and authority, and it appears as the headgear of the high priest in Zechariah 3:5, where Joshua the high priest is given a clean turban as part of his investiture vision, symbolizing renewed purity and dignity in the priestly office.</p><p>Head coverings in the ancient Near East carried significant social meaning: they could indicate rank, gender roles, mourning, or ceremonial status. The word <em>ṣānîph</em> suggests a winding or wrapping, consistent with the turbans seen in Assyrian and Egyptian reliefs of the period. The stripping of such garments in prophetic judgment oracles (Isaiah 3) contrasted the luxury of Jerusalem's women with the coming desolation, while the bestowing of a turban in Zechariah 3 enacted priestly restoration and divine acceptance.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hood",
            "isbe": "hood"
        },
        "key_refs": ["Isaiah 3:23", "Job 29:14", "Zechariah 3:5"]
    },
    "hoof": {
        "id": "hoof",
        "term": "Hoof",
        "category": "concepts",
        "intro": "<p>The hoof, specifically whether it is cloven (split), was a key criterion in Mosaic dietary law for determining whether a land animal was clean and therefore edible for Israelites. Leviticus 11:3 and Deuteronomy 14:6 established the dual requirement: a clean animal must both have a completely divided hoof and chew its cud. Animals with cloven hooves that did not chew the cud (pigs) or that chewed the cud without cloven hooves (camels, rabbits) were unclean.</p><p>The symbolic significance of the divided hoof has been interpreted variously in rabbinic literature as representing circumspection in one's path, the need for both practical and spiritual discipline, or simply a practical distinction serving public health. In prophetic imagery, the hoof appears as an instrument of power and judgment: Ezekiel 26:11 describes Nebuchadnezzar's horses' hooves treading Tyre's streets, and Micah 4:13 envisions Zion's hooves made of iron to thresh the nations. The requirement to bring all animals—not leaving a single hoof behind—in the Exodus confrontation with Pharaoh (Exodus 10:26) underscored Israel's total dependence on God's complete provision.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hoof",
            "isbe": "hoof"
        },
        "key_refs": ["Exodus 10:26", "Leviticus 11:3", "Deuteronomy 14:6", "Micah 4:13"]
    },
    "hook": {
        "id": "hook",
        "term": "Hook",
        "category": "concepts",
        "intro": "<p>Hooks in the biblical world served both practical and metaphorical functions. The Hebrew vocabulary distinguishes several types: <em>ḥāh</em>, a ring or hook inserted in the nose of animals or prisoners for leading and control (Isaiah 37:29; Ezekiel 29:4; 38:4); <em>wāw</em>, the hooks or pins from which the tabernacle curtains hung (Exodus 26:32, 37); and <em>ṣinnôr</em>, a hook or grappling instrument. The image of God placing a hook in the jaw of an enemy to turn them back was a vivid expression of divine sovereignty over human ambition.</p><p>Isaiah 37:29 records God's threat to Sennacherib: <em>I will put my hook in your nose and my bit in your mouth, and I will turn you back on the way by which you came</em>—the language of animal control applied to an arrogant conqueror. Ezekiel uses the same imagery for Gog (38:4) and Egypt's Pharaoh (29:4), whose power God would control like that of a fish or crocodile on a leash. The pruning hooks of Isaiah 2:4 and Micah 4:3 (swords beaten into pruning hooks) represent the peacetime transformation of military equipment into agricultural tools in the eschatological vision of lasting peace.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hook",
            "isbe": "hook"
        },
        "key_refs": ["Exodus 26:32", "Isaiah 2:4", "Isaiah 37:29", "Ezekiel 38:4"]
    },
    "hope": {
        "id": "hope",
        "term": "Hope",
        "category": "concepts",
        "intro": "<p>Hope is one of the three cardinal Christian virtues alongside faith and love (1 Corinthians 13:13), but it has a distinctive character in biblical theology that sets it apart from mere optimism. Biblical hope (Hebrew <em>tiqwâ</em>, <em>yāḥal</em>; Greek <em>elpis</em>) is not uncertain wishfulness but confident expectation grounded in God's character and promises. The distinction from secular hope lies in its object: not circumstances or human effort, but the living God whose covenant faithfulness guarantees what he has promised.</p><p>In the Old Testament, hope is repeatedly expressed as waiting on the LORD—a patient, active confidence that God will act despite present adversity (Psalm 31:24; Isaiah 40:31). The New Testament deepens this by tying hope specifically to the resurrection: Paul calls Christ's resurrection the basis of the believer's hope (1 Corinthians 15:19–20), and the hope of glory is described as Christ himself dwelling within (Colossians 1:27). Hebrews 6:19 calls this hope an anchor for the soul—fixed not in earthly circumstances but in the heavenly sanctuary where Christ the forerunner has entered. Hope endures because it is not yet seen (Romans 8:24–25), but it is certain because its foundation is the word and oath of God.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hope",
            "isbe": "hope"
        },
        "key_refs": ["Romans 8:24", "1 Corinthians 13:13", "Colossians 1:27", "Hebrews 6:19"]
    },
    "hophni": {
        "id": "hophni",
        "term": "Hophni",
        "category": "people",
        "intro": "<p>Hophni was one of the two sons of Eli the high priest who served as priests at the sanctuary of Shiloh. Together with his brother Phinehas, he was guilty of egregious priestly abuses: seizing the best portions of sacrificial meat before the fat was burned (in direct violation of Mosaic law), threatening worshippers who objected, and lying with the women who served at the entrance to the tent of meeting. Their father Eli rebuked them but failed to remove them, and his leniency was counted as honoring his sons more than God.</p><p>A man of God prophesied the end of Eli's priestly house (1 Samuel 2:34), and the sign given was that both Hophni and Phinehas would die on the same day. The prophecy was fulfilled when the Philistines defeated Israel at Aphek: Eli's sons carried the ark of the covenant into battle—an unauthorized act—and both were killed when the Philistines captured it. Eli himself died upon hearing the news. The deaths of Hophni and Phinehas marked the catastrophic end of the house of Eli and set the stage for Samuel's rise to priestly and prophetic leadership in Israel.</p>",
        "sections": [],
        "hitchcock_meaning": "pugilist; strong",
        "source_ids": {
            "easton": "hophni",
            "smith": "hophni"
        },
        "key_refs": ["1 Samuel 2:34", "1 Samuel 4:4", "1 Samuel 4:11", "1 Samuel 4:17"]
    },
    "hophra": {
        "id": "hophra",
        "term": "Hophra",
        "category": "people",
        "intro": "<p>Hophra (known to Greek historians as Apries) was a Pharaoh of Egypt who reigned approximately 591–570 BC, during the final years of the kingdom of Judah and the early period of the Babylonian exile. He is mentioned by name only in Jeremiah 44:30, where God declares he will give Hophra into the hands of his enemies just as he gave Zedekiah king of Judah into the hands of Nebuchadnezzar—a prophecy that was fulfilled when Hophra was overthrown and killed by Ahmose II.</p><p>During the siege of Jerusalem (588–586 BC), Hophra led an Egyptian army that temporarily relieved the Babylonian pressure on the city, causing Nebuchadnezzar to break off the siege briefly. Jeremiah warned that this Egyptian intervention would fail (Jeremiah 37:5–10), and indeed the Babylonians quickly returned and completed the destruction of Jerusalem. The Jewish refugees who fled to Egypt after Gedaliah's assassination, ignoring Jeremiah's counsel, settled partly under Hophra's protection—an act Jeremiah condemned as faithless reliance on Egypt rather than God. Hophra's downfall, as Jeremiah predicted, came through internal Egyptian conflict.</p>",
        "sections": [],
        "hitchcock_meaning": "cover of the mouth; that sees the house",
        "source_ids": {
            "easton": "hophra",
            "isbe": "hophra"
        },
        "key_refs": ["Jeremiah 37:5", "Jeremiah 44:30"]
    },
    "hor": {
        "id": "hor",
        "term": "Hor",
        "category": "places",
        "intro": "<p>Mount Hor is most prominently the mountain on the border of Edom where Aaron the high priest died and was buried. Numbers 20:22–29 records that God commanded Moses and Aaron to go up to Mount Hor, where Aaron's priestly vestments were transferred to his son Eleazar before Aaron died on the summit at age 123. Israel mourned Aaron for thirty days. The precise identification of Mount Hor remains disputed; the traditional identification with Jebel Harun (Aaron's Mountain) above Petra in modern Jordan is ancient but not universally accepted by scholars.</p><p>A second Mount Hor is mentioned in Numbers 34:7–8 as a landmark on the northern boundary of Canaan, apparently located near the Mediterranean coast in the direction of the entrance to Hamath—a entirely different location from the Edomite Hor. The repetition of the name thus represents two different mountains, the southern one associated with Aaron's death and the northern one serving as a geographic marker for the tribal boundaries. The name Hor may simply mean <em>mountain</em> or <em>hill</em> in a general sense.</p>",
        "sections": [],
        "hitchcock_meaning": "who conceives, or shows; a hill",
        "source_ids": {
            "easton": "hor",
            "smith": "hor",
            "isbe": "hor"
        },
        "key_refs": ["Numbers 20:22", "Numbers 20:28", "Numbers 33:38", "Numbers 34:7"]
    },
    "horeb": {
        "id": "horeb",
        "term": "Horeb",
        "category": "places",
        "intro": "<p>Horeb (meaning <em>desert</em> or <em>dried-up ground</em>) is the name used predominantly in Deuteronomy and the Elijah narratives for the sacred mountain also called Sinai in Exodus and Numbers. The relationship between the two names has been debated: most scholars treat Horeb and Sinai as alternative designations for the same mountain or mountain complex, with Horeb as the broader name for the general area and Sinai as the specific peak, or the names reflecting the usage of different source traditions.</p><p>At Horeb, Moses encountered the burning bush and received his commission (Exodus 3:1); Israel camped there and received the Ten Commandments and the covenant law; and the tabernacle was constructed in its shadow. Elijah fled to Horeb after Jezebel's threat and experienced the still small voice of God there (1 Kings 19:8–12)—a deliberate echo of Moses's experience. Malachi 4:4 commands Israel to remember the law of Moses given at Horeb, the final Old Testament reference to the mountain, which in Christian interpretation became a type of the New Covenant mediated on the true mountain of God. Paul's allegory in Galatians 4 uses Sinai/Horeb as the symbol of the covenant of law contrasted with the covenant of promise.</p>",
        "sections": [],
        "hitchcock_meaning": "desert; solitude; destruction",
        "source_ids": {
            "easton": "horeb",
            "smith": "horeb",
            "isbe": "horeb"
        },
        "key_refs": ["Exodus 3:1", "Deuteronomy 5:2", "1 Kings 19:8", "Malachi 4:4"]
    },
    "horem": {
        "id": "horem",
        "term": "Horem",
        "category": "places",
        "intro": "<p>Horem was one of the fenced (fortified) cities of the tribe of Naphtali, listed in Joshua 19:38 among the cities of Naphtali's allotment in the northern territories of Canaan. The name, meaning <em>an offering dedicated to God</em> or <em>consecrated</em>, reflects the Hebrew root <em>ḥrm</em> related to the concept of holy dedication or sacred destruction. Beyond its appearance in this boundary and city list, Horem receives no further mention in the biblical narrative.</p><p>The tribal allotments of Naphtali placed it in the upper Galilee region, including territory around the Sea of Galilee and the Huleh basin northward toward the Lebanon range. Horem's precise location within this territory is unidentified by archaeology. The list of Naphtali's cities in Joshua 19 is part of the formal territorial division supervised by Eleazar and Joshua at Shiloh, establishing the land grants that were to define tribal identity and inheritance through subsequent generations.</p>",
        "sections": [],
        "hitchcock_meaning": "an offering dedicated to God",
        "source_ids": {
            "easton": "horem",
            "smith": "horem",
            "isbe": "horem"
        },
        "key_refs": ["Joshua 19:38"]
    },
    "horites": {
        "id": "horites",
        "term": "Horites",
        "category": "people",
        "intro": "<p>The Horites (Hebrew <em>ḥōrîm</em>, cave-dwellers) were an ancient people who inhabited the mountainous region of Seir (later Edom) before the descendants of Esau displaced them. Genesis 14:6 mentions them at Mount Seir in the account of the four kings' southern campaign, and Genesis 36:20–30 provides a substantial genealogy of Horite clans—Lotan, Shobal, Zibeon, Anah, Dishon, Ezer, and Dishan—whose chieftains Esau's descendants supplanted, just as Israel would displace the Canaanites west of the Jordan.</p><p>The identification of the biblical Horites with the Hurrians, an important non-Semitic people known from ancient Near Eastern texts (the Mitanni kingdom and Nuzi documents), was once widely accepted but has been questioned in recent scholarship. The Hurrians were a significant power in Mesopotamia and northern Syria during the second millennium BC, but their connection to the cave-dwelling Horites of Mount Seir is linguistically and geographically uncertain. The biblical Horites appear to be a Canaanite/Edomite group, while the Hurrian connection remains a hypothesis requiring caution. Deuteronomy 2:12 and 2:22 use the Horite displacement as a parallel to Israel's own coming displacement of Canaan.</p>",
        "sections": [],
        "hitchcock_meaning": "cave-men",
        "source_ids": {
            "easton": "horites",
            "isbe": "horites"
        },
        "key_refs": ["Genesis 14:6", "Genesis 36:20", "Deuteronomy 2:12"]
    },
    "hormah": {
        "id": "hormah",
        "term": "Hormah",
        "category": "places",
        "intro": "<p>Hormah (meaning <em>devoted to destruction</em> or <em>consecrated to God by a vow of destruction</em>) was a city in the Negev whose name commemorated an act of holy war. Numbers 21:1–3 records that when the Canaanite king of Arad attacked Israel during the wilderness period, Israel vowed to utterly destroy (<em>ḥāram</em>) his cities if God delivered them, and when victory came the place was named Hormah to memorialize the fulfillment of that vow.</p><p>An earlier, less successful encounter also connects to Hormah: Numbers 14:45 and Deuteronomy 1:44 record that when the first generation of Israelites presumptuously attempted to enter Canaan after their faithless response to the spies' report, they were routed by the Amalekites and Canaanites all the way to Hormah—a humiliating reversal that underscored the consequence of disobedience. Hormah was later assigned to Judah and then to Simeon (Joshua 15:30; 19:4), and David distributed spoils to its inhabitants (1 Samuel 30:30). The modern identification is debated between Tel Masos and Tel Halif in the northern Negev.</p>",
        "sections": [],
        "hitchcock_meaning": "devoted or consecrated to God; utter destruction",
        "source_ids": {
            "easton": "hormah",
            "smith": "hormah",
            "isbe": "hormah"
        },
        "key_refs": ["Numbers 14:45", "Numbers 21:3", "Joshua 15:30", "1 Samuel 30:30"]
    },
    "horn": {
        "id": "horn",
        "term": "Horn",
        "category": "concepts",
        "intro": "<p>Horns in the biblical world served as both practical objects and powerful symbols. As physical objects, animal horns were perforated at the tip to make trumpets for signaling in battle and worship (Joshua 6:4–5), and hollow horns served as oil flasks (1 Samuel 16:1). The four corners of the altar of burnt offering and the altar of incense were fashioned as projecting horns (<em>qarnōt</em>), to which worshippers could cling for refuge and to which blood was applied in atoning rituals.</p><p>As a symbol, the horn represented power, strength, and royal dignity—the natural force of a horned animal applied metaphorically to human or divine authority. Hannah's prayer (1 Samuel 2:1) exults that God has exalted her horn; the Psalms repeatedly speak of God exalting or humbling horns of nations and individuals (Psalm 75:4–5, 10; 89:17). Daniel's visions use horns as symbols for kings and kingdoms (Daniel 7–8), a usage continued in Revelation (13:1; 17:3). The messianic horn of David (Psalm 132:17; Luke 1:69) became a title for the anointed deliverer who would restore Israel's strength. The range of horn symbolism—from musical instrument to atoning altar to prophetic imagery—reflects its pervasive importance in Israelite religion and thought.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "horn",
            "smith": "horn",
            "isbe": "horn"
        },
        "key_refs": ["1 Samuel 2:1", "Psalm 75:10", "Daniel 7:8", "Luke 1:69"]
    },
    "hornet": {
        "id": "hornet",
        "term": "Hornet",
        "category": "concepts",
        "intro": "<p>The hornet (Hebrew <em>ṣirʿâ</em>, stinging) appears three times in the Old Testament (Exodus 23:28; Deuteronomy 7:20; Joshua 24:12) as the instrument God promised to send before Israel to drive out the Canaanite peoples. The literal reading—that God would use actual hornets as a plague against Canaan's inhabitants—finds some support in ancient Near Eastern texts where bee or hornet infestations are mentioned as causing population displacement.</p><p>Allegorical interpretations have also been proposed: that the hornet represents terror, fear, or a divine panic that God would send upon the Canaanites to weaken their resistance before Israel's advance. Some modern scholars propose the hornet may be a metaphor for Egypt's military campaigns that weakened the Canaanite city-states before Israel's conquest. Joshua 24:12 specifically credits the hornet (rather than Israel's sword or bow) with driving out the two Amorite kings, emphasizing divine initiative in the conquest. The hornet thus becomes a symbol of God fighting for his people through means beyond ordinary military force.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hornet",
            "smith": "hornet",
            "isbe": "hornet"
        },
        "key_refs": ["Exodus 23:28", "Deuteronomy 7:20", "Joshua 24:12"]
    },
    "horonaim": {
        "id": "horonaim",
        "term": "Horonaim",
        "category": "places",
        "intro": "<p>Horonaim (<em>two caverns</em>) was a city of Moab located in the southern part of the Moabite plateau, south of the Arnon River. Isaiah 15:5 and Jeremiah 48:3, 5, 34 mention Horonaim in prophecies of judgment against Moab, where the fugitives of Moab are described as crying out at its descent—suggesting the city sat at the top of a steep descending pass, with the sound of wailing echoing from its cliffs. It was a place of some size and strategic importance in the southern Moabite territory.</p><p>The Moabite Stone (Mesha Stele, ninth century BC) also mentions Horonaim in the context of Mesha's military operations against Israel, providing extrabiblical confirmation of the site's importance in Moabite territory. The Isaiah and Jeremiah oracles against Moab paint a picture of the city's destruction: its fugitives descend the way of Luhith weeping, and the sound of destruction echoes from Horonaim. The city's location in southern Moab below the main plateau may account for the reference to its <em>descent</em>; it would have been accessible via one of the steep wadis cutting through the plateau's eastern escarpment.</p>",
        "sections": [],
        "hitchcock_meaning": "angers; ragings",
        "source_ids": {
            "easton": "horonaim",
            "smith": "horonaim",
            "isbe": "horonaim"
        },
        "key_refs": ["Isaiah 15:5", "Jeremiah 48:3", "Jeremiah 48:34"]
    },
    "horonite": {
        "id": "horonite",
        "term": "Horonite",
        "category": "concepts",
        "intro": "<p>Horonite was the designation applied to Sanballat, one of the principal opponents of Nehemiah's mission to rebuild the walls of Jerusalem. The term identifies him as a native of Horonaim in Moab or of Beth-horon in the hill country of Ephraim—the latter being the more commonly accepted identification, suggesting he was a Samaritan official with roots in the Beth-horon region that controlled the main pass between the coastal plain and Jerusalem.</p><p>Sanballat the Horonite appears throughout the Nehemiah memoir as a persistent adversary, mocking the rebuilding project, conspiring with Tobiah the Ammonite and Geshem the Arab against Nehemiah, and attempting to lure Nehemiah into a meeting that would compromise the work. Despite his opposition, the wall was completed in fifty-two days. The Elephantine papyri from Egypt (fifth century BC) mention Sanballat's sons as governors of Samaria, providing extrabiblical confirmation of his status as a significant Samaritan official. His designation as a Horonite served to mark his foreign or provincial origin in contrast to the Jerusalem community whose interests he opposed.</p>",
        "sections": [],
        "hitchcock_meaning": "of the valley; of the lord",
        "source_ids": {
            "easton": "horonite",
            "smith": "horonite",
            "isbe": "horonite"
        },
        "key_refs": ["Nehemiah 2:10", "Nehemiah 2:19", "Nehemiah 4:1", "Nehemiah 6:1"]
    },
    "horse": {
        "id": "horse",
        "term": "Horse",
        "category": "concepts",
        "intro": "<p>The horse in the Bible appears almost exclusively in military contexts, standing as the supreme symbol of military power and human self-reliance. In contrast to the donkey (the mount of peace and servitude), the horse was the weapon of war: chariots drawn by horses gave decisive advantage on the flat plains of Megiddo, Jezreel, and the coastal routes. Egypt was the primary supplier of horses to the ancient Near East, and Solomon's famous horse trade with Egypt (1 Kings 10:28–29) represented both his wealth and a potential compromise of the Deuteronomic law warning kings not to multiply horses (Deuteronomy 17:16).</p><p>The prophets repeatedly contrast trust in horses and chariots with trust in God: <em>Some trust in chariots and some in horses, but we trust in the name of the LORD our God</em> (Psalm 20:7). Isaiah 31:1–3 pronounces woe on those who go down to Egypt for help and trust in horses. Job 39:19–25 contains a celebrated description of the war horse as one of God's most magnificent creatures—fearless and exhilarated in battle. Zechariah and Revelation use horses as symbolic figures in apocalyptic visions (Zechariah 1:8; 6:1–8; Revelation 6:1–8), where their colors represent divine purposes of judgment and redemption.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "horse",
            "smith": "horse",
            "isbe": "horse"
        },
        "key_refs": ["Deuteronomy 17:16", "Psalm 20:7", "Job 39:19", "Revelation 6:2"]
    },
    "horse-gate": {
        "id": "horse-gate",
        "term": "Horse-gate",
        "category": "places",
        "intro": "<p>The Horse Gate was one of the gates in the walls of Jerusalem, located on the east side of the city between the Water Gate and the East Gate, apparently near the southeast corner of the temple mount. Nehemiah 3:28 records that the priests repaired the wall above the Horse Gate during the reconstruction project. The gate's name likely derived from its use as the entry point for horses serving the royal stables or the cavalry units quartered in the nearby palace complex.</p><p>The Horse Gate also appears in the dramatic account of Queen Athaliah's execution: when she rushed to the temple upon hearing the coronation shouts for the young king Joash, Jehoiada the priest commanded that she be led out to the Horse Gate to be executed there rather than within the temple precincts (2 Kings 11:16; 2 Chronicles 23:15). The gate's proximity to the palace made it the natural place for this act of royal justice. Jeremiah 31:40 includes the Horse Gate in the boundary description of the future holy city that will never again be plucked up or overthrown.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "horse-gate",
            "isbe": "horse-gate"
        },
        "key_refs": ["2 Kings 11:16", "Nehemiah 3:28", "Jeremiah 31:40"]
    },
    "horse-leech": {
        "id": "horse-leech",
        "term": "Horse-leech",
        "category": "concepts",
        "intro": "<p>The horse-leech (Hebrew <em>ʿalûqâ</em>) appears only once in Scripture, in Proverbs 30:15, as an example of insatiable appetite: <em>The horse-leech has two daughters crying 'Give, give'</em>—the opening of a numerical saying about four things that are never satisfied (the grave, the barren womb, the earth thirsting for water, and fire). The identity of the <em>ʿalûqâ</em> has been debated; while traditionally rendered horse-leech (a large bloodsucking worm that clings to the throats of animals drinking), some scholars have proposed it refers to a vampire-like creature from folklore or simply a generic bloodsucker.</p><p>The Talmud identified the two daughters of the horse-leech with Gehinnom and the evil inclination, or with various allegorical pairs. The precise zoological identification matters less than the rhetorical function: the horse-leech's unceasing demand for blood (<em>give, give</em>) becomes the perfect image for insatiability. The broader Agur poem in Proverbs 30 uses natural observations to explore the limits of human wisdom and the mysteries of creation, and the horse-leech illustrates that some appetites are by nature inexhaustible.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "horse-leech"
        },
        "key_refs": ["Proverbs 30:15"]
    },
    "horseman": {
        "id": "horseman",
        "term": "Horseman",
        "category": "concepts",
        "intro": "<p>Horsemen in the biblical world were cavalry soldiers who rode horses in military operations, distinguished from chariot warriors who were pulled by horses. The Hebrew <em>parāš</em> (horseman, rider) and the more common <em>baʿal parāš</em> (master of a horse) denote mounted military personnel. Egyptian cavalry and chariots pursuing Israel at the Exodus introduced horsemen as a force of oppression in Israel's national memory; their drowning in the Red Sea was a paradigm of divine deliverance over military technology.</p><p>Horses and horsemen multiplied in Israel under the monarchy: Solomon had 12,000 horsemen stationed in chariot cities and in Jerusalem (1 Kings 10:26). The prophets use the image of divine horsemen in apocalyptic visions: Zechariah sees horsemen patrolling the earth at God's direction, and Elijah's translation was accompanied by a chariot of fire and horses of fire (2 Kings 2:11–12), giving rise to Elisha's exclamation <em>My father, my father, the chariots of Israel and its horsemen!</em> The phrase became a way of describing a prophet's worth to Israel—more valuable than military cavalry. In Revelation 9, demonic horsemen form part of the vision of judgment, while Revelation 19 depicts Christ himself as a conquering rider.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "horseman",
            "isbe": "horseman"
        },
        "key_refs": ["Exodus 14:9", "2 Kings 2:12", "Zechariah 1:8", "Revelation 19:14"]
    },
    "hosah": {
        "id": "hosah",
        "term": "Hosah",
        "category": "places",
        "intro": "<p>Hosah was a border town in the territory of Asher (Joshua 19:29), located near the coast of the Mediterranean north of Tyre and south of Zidon. Its placement in the Asherite boundary list suggests it was a coastal or near-coastal settlement in Phoenician-adjacent territory. The town gave its name to a family or district, and its precise modern identification remains uncertain, with proposed sites including Tell Rashidiyeh near Tyre.</p><p>The name Hosah also belonged to a Levite, a son of Merari, who was appointed as a gatekeeper of the ark of the covenant during David's arrangements for worship in Jerusalem (1 Chronicles 16:38; 26:10–11). This Levite Hosah was appointed with Obed-edom to minister before the ark after its installation in the tent David had pitched for it, and he was later assigned to the western gatehouse of the temple in David's organization of the Levitical duties. The shared name between the Asherite town and the Levitical gatekeeper represents coincidental usage of the same Hebrew term meaning <em>trusting</em> or <em>refuge</em>.</p>",
        "sections": [],
        "hitchcock_meaning": "trusting",
        "source_ids": {
            "easton": "hosah",
            "smith": "hosah",
            "isbe": "hosah"
        },
        "key_refs": ["Joshua 19:29", "1 Chronicles 16:38", "1 Chronicles 26:10"]
    },
    "hosanna": {
        "id": "hosanna",
        "term": "Hosanna",
        "category": "concepts",
        "intro": "<p>Hosanna (Hebrew <em>hôšîʿā-nnāʾ</em>, <em>save, we pray</em> or <em>save now</em>) was the acclamation shouted by the crowds at Jesus's triumphal entry into Jerusalem on Palm Sunday. Originally a petition for divine deliverance (Psalm 118:25), it had by the first century become a liturgical shout of joyful praise at the Feast of Tabernacles, when worshippers waved lulab bundles and chanted Psalm 118 as part of the Hallel. The word carried both its original meaning of appeal and its evolved sense of acclamation and blessing.</p><p>The Gospels record the crowd crying <em>Hosanna to the Son of David! Blessed is he who comes in the name of the Lord! Hosanna in the highest!</em>—applying the messianic pilgrim blessing of Psalm 118:26 directly to Jesus and adding the Davidic royal title that identified him as the promised king. The children in the temple continued the acclamation, fulfilling (according to Matthew 21:16) the word of Psalm 8:2. The scene deliberately evoked both the Davidic kingship and the Feast of Tabernacles' eschatological associations, framing Jesus's entry as the arrival of the long-awaited Davidic redeemer. Hosanna subsequently passed into Christian liturgy as a standard acclamation of praise, particularly in Eucharistic worship.</p>",
        "sections": [],
        "hitchcock_meaning": "save I pray thee; keep; preserve",
        "source_ids": {
            "easton": "hosanna",
            "smith": "hosanna",
            "isbe": "hosanna"
        },
        "key_refs": ["Psalm 118:25", "Matthew 21:9", "Matthew 21:15", "Mark 11:10"]
    },
    "hose": {
        "id": "hose",
        "term": "Hose",
        "category": "concepts",
        "intro": "<p>Hose appears in Daniel 3:21 (KJV) as part of the list of garments worn by Shadrach, Meshach, and Abednego when they were thrown into the fiery furnace: <em>bound in their coats, their hosen, and their hats, and their other garments</em>. The Aramaic word rendered <em>hosen</em> or <em>hose</em> (<em>sarbāl</em>) denotes a type of garment—likely a tunic, trousers, or mantle worn as an undergarment. Translations vary considerably: mantle, tunic, trousers, and cloak have all been proposed depending on how the Aramaic is understood.</p><p>The point of the verse is not the precise nature of the garments but their preservation: when the three men emerged from the furnace unharmed, not a hair of their heads was singed and their garments were not affected—not even the smell of fire was on them. The detailed listing of their clothing items before and after the ordeal dramatizes the miraculous completeness of God's protection. The specific term <em>hosen</em> in the KJV reflects the translation conventions of the early seventeenth century; modern versions typically render the underlying Aramaic with more current terminology.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hose"
        },
        "key_refs": ["Daniel 3:21", "Daniel 3:27"]
    },
    "hosea": {
        "id": "hosea",
        "term": "Hosea",
        "category": "people",
        "intro": "<p>Hosea son of Beeri was a prophet of the northern kingdom of Israel who ministered during the eighth century BC, during the reigns of Uzziah, Jotham, Ahaz, and Hezekiah of Judah and the reign of Jeroboam II of Israel. His name, meaning <em>salvation</em>, is cognate with Joshua and Jesus. He was the only writing prophet who was himself a native of the northern kingdom, and his ministry spanned the turbulent final decades before Samaria fell to Assyria in 722 BC.</p><p>Hosea's prophecy is remarkable for its autobiographical character: God commanded him to marry Gomer, a woman who proved unfaithful, and the prophet's anguished marriage became a living parable of God's relationship with faithless Israel. Through the naming of his children—Jezreel (judgment), Lo-ruhamah (not pitied), and Lo-ammi (not my people)—Hosea enacted the divine verdict on a nation that had abandoned its covenant. Yet the book also contains some of the most tender expressions of divine love in the Hebrew scriptures: <em>How can I give you up, Ephraim?</em> (Hosea 11:8). The New Testament cites Hosea in multiple contexts, most notably Matthew 2:15 (<em>out of Egypt I called my son</em>) and 1 Peter 2:10's allusion to Lo-ammi's reversal.</p>",
        "sections": [],
        "hitchcock_meaning": "Hoshea, savior; safety",
        "source_ids": {
            "easton": "hosea",
            "smith": "hosea",
            "isbe": "hosea"
        },
        "key_refs": ["Hosea 1:1", "Hosea 2:19", "Hosea 11:8", "Matthew 2:15"]
    },
    "hosea-prophecies-of": {
        "id": "hosea-prophecies-of",
        "term": "Hosea, Prophecies of",
        "category": "concepts",
        "intro": "<p>The Book of Hosea stands first among the twelve Minor Prophets in the Hebrew canon, a placement sometimes attributed to its length, age, or the theological comprehensiveness of its themes. Covering fourteen chapters, it divides broadly into two sections: chapters 1–3, centered on the autobiographical account of Hosea's marriage to Gomer and its allegorical interpretation as God's relationship with Israel; and chapters 4–14, containing a series of prophetic oracles, laments, and appeals addressed to the northern kingdom in its final decades before Assyrian conquest.</p><p>The theological richness of Hosea's prophecies has made the book one of the most cited in the New Testament. Hosea's central metaphor of Israel as God's unfaithful wife who prostituted herself with the Baals transformed how subsequent scripture speaks of covenant infidelity. His vision of future restoration—the valley of Achor becoming a door of hope, the divorce decree reversed, the divine name <em>my husband</em> replacing <em>my master</em>—anticipates the new covenant language of Jeremiah and Ezekiel. Paul draws on Hosea 2:23 and 1:10 in Romans 9:25–26 to argue for Gentile inclusion in the people of God, extending the reversal of Lo-ammi beyond Israel to encompass all nations.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hosea-prophecies-of",
            "smith": "hosea-prophecies-of"
        },
        "key_refs": ["Hosea 2:14", "Hosea 6:6", "Hosea 11:1", "Romans 9:25"]
    },
    "hoshea": {
        "id": "hoshea",
        "term": "Hoshea",
        "category": "people",
        "intro": "<p>Hoshea (meaning <em>salvation</em>) was a name borne by several biblical figures, most significantly: (1) the original name of Joshua son of Nun, changed by Moses from Hoshea to Joshua (Yahweh is salvation) in Numbers 13:16; and (2) the last king of Israel (the northern kingdom), who reigned approximately 731–722 BC. This last king Hoshea came to power by assassinating Pekah and was himself eventually imprisoned by Shalmaneser V of Assyria after conspiring with Egypt to withhold tribute. Samaria fell after a three-year siege and the population was deported, ending the northern kingdom.</p><p>The biblical verdict on Hoshea is notably milder than on his predecessors: he <em>did evil in the sight of the LORD, yet not as the kings of Israel who were before him</em> (2 Kings 17:2), suggesting some moderation of the Jeroboam cult. However, his faithless reliance on Egypt rather than on God sealed the nation's fate. A third Hoshea was a leader from the tribe of Ephraim in David's administrative organization (1 Chronicles 27:20), and several other individuals bear the name in the postexilic period. The name's identity with Joshua and ultimately with Jesus—all meaning salvation—gave it lasting theological resonance.</p>",
        "sections": [],
        "hitchcock_meaning": "Hoshea, savior; safety",
        "source_ids": {
            "easton": "hoshea",
            "smith": "hoshea",
            "isbe": "hoshea"
        },
        "key_refs": ["Numbers 13:8", "2 Kings 17:1", "2 Kings 17:6"]
    },
    "host": {
        "id": "host",
        "term": "Host",
        "category": "concepts",
        "intro": "<p>Host in the biblical vocabulary carries two distinct meanings. As a term for hospitality, it denotes one who receives and entertains guests—Romans 16:23 greets Gaius as <em>host of the whole church</em>, and Luke 10:35 refers to the innkeeper who cares for the wounded man in the parable of the Good Samaritan as a host. As a military term, host denotes an army or organized body of fighting men: the Israelite tribes marched in ordered hosts, and the Midianite army is called a host in Judges 4.</p><p>The military sense underlies one of the most significant divine titles: the LORD of hosts (<em>YHWH ṣĕbāʾôth</em>), which appears more than 250 times in the Hebrew scriptures. The phrase originally may have referred to the armies of Israel or to the angelic heavenly armies, but it developed into a comprehensive title for God's supreme authority over all created powers—celestial bodies, angelic beings, and earthly armies alike. The title is particularly prominent in the prophetic books (especially Isaiah, Jeremiah, and the twelve Minor Prophets) as an assertion of divine sovereignty in contexts of international upheaval.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "host",
            "isbe": "host"
        },
        "key_refs": ["Romans 16:23", "1 Samuel 17:45", "Isaiah 6:3", "Revelation 19:14"]
    },
    "host-of-heaven": {
        "id": "host-of-heaven",
        "term": "Host of Heaven",
        "category": "concepts",
        "intro": "<p>The host of heaven refers to the sun, moon, stars, and celestial bodies as a category—the cosmic assembly of luminaries that Genesis 2:1 summarizes as completed on the sixth day. The same phrase also designates the angelic beings who serve before God's throne (1 Kings 22:19; 2 Chronicles 18:18), creating a deliberate overlap between the celestial bodies and the heavenly court. This double reference reflects the ancient Near Eastern background in which stars were associated with divine beings.</p><p>The worship of the host of heaven was a persistent temptation for Israel, adopted from surrounding Assyrian, Babylonian, and Canaanite cultures that venerated astral deities. Deuteronomy 4:19 explicitly warns Israel not to worship the sun, moon, or stars that God allotted to the nations. Manasseh's building of altars for the host of heaven in both courts of the temple (2 Kings 21:5) was among his most notorious transgressions, and Josiah's reform included removing the vessels made for Baal, Asherah, and the host of heaven from the temple. The proclamation that God created and controls the host of heaven—rather than being subordinate to it—was a fundamental assertion of Israelite monotheism against the astral religion of the ancient world.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "host-of-heaven",
            "isbe": "host-of-heaven"
        },
        "key_refs": ["Genesis 2:1", "Deuteronomy 4:19", "2 Kings 21:5", "1 Kings 22:19"]
    },
    "hostage": {
        "id": "hostage",
        "term": "Hostage",
        "category": "concepts",
        "intro": "<p>A hostage in the ancient Near East was a person of standing—typically a royal family member or noble's son—given as a security pledge for the faithful performance of a treaty, tribute payment, or surrender agreement. The Hebrew <em>ben-taʿarubot</em> (son of pledges) describes this arrangement. By holding the pledges, the dominant party had leverage to ensure compliance; harm to the hostage would be threatened if the weaker party defected.</p><p>The Bible mentions hostages in two military contexts. When Amaziah of Judah was defeated by Jehoash king of Israel at Beth-shemesh, Jehoash took Amaziah as a prisoner and then took hostages from Jerusalem—presumably members of the royal family or nobles—as security when he returned north after dismantling a section of Jerusalem's wall (2 Kings 14:14; 2 Chronicles 25:24). The institution of hostage-taking reflects the common ancient Near Eastern practice of binding defeated parties to loyal submission through personal guarantees, a practice attested in Egyptian, Assyrian, and Hittite treaty records throughout the second and first millennia BC.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hostage",
            "isbe": "hostage"
        },
        "key_refs": ["2 Kings 14:14", "2 Chronicles 25:24"]
    },
    "hough": {
        "id": "hough",
        "term": "Hough",
        "category": "concepts",
        "intro": "<p>To hough (or hamstring) was to sever the hamstring tendon of the hind legs of captured horses, rendering them permanently lame and useless for military purposes. The Hebrew <em>ʿāqar</em> (to hamstring, to hough) describes this practice. Joshua was commanded by God to hamstring the horses of the coalition kings he defeated at the Waters of Merom (Joshua 11:6, 9), preventing Israel from incorporating enemy chariot forces into their own army—an implicit statement that Israel's military strength was to rest on God rather than on horse-power.</p><p>David later hamstrung the chariot horses he captured from Hadadezer king of Zobah in the north, keeping only enough for a hundred chariots (2 Samuel 8:4; 1 Chronicles 18:4). The deliberate destruction of military assets—particularly animals of such high economic and military value—was an act of theological statement as much as practical policy. The prohibition in Deuteronomy 17:16 against multiplying horses for the king reflected the same concern: dependence on cavalry would shift trust from the LORD to military technology. Houghing captured horses was thus an act of covenantal faith as well as military pragmatism.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hough",
            "isbe": "hough"
        },
        "key_refs": ["Joshua 11:6", "Joshua 11:9", "2 Samuel 8:4"]
    },
    "hour": {
        "id": "hour",
        "term": "Hour",
        "category": "concepts",
        "intro": "<p>The concept of the hour as a subdivided unit of time appears first in the biblical narrative in Daniel 3:6 and 4:19, reflecting the Babylonian division of the day into twelve equal parts. The Hebrew <em>šāʿâ</em> and Chaldee <em>šāʿâh</em> originally conveyed a brief moment or glance of time rather than a precise sixty-minute unit, and the Babylonian twelfth-part system was not part of original Hebrew timekeeping. Before the exile, Israelites reckoned time by watches of the night and by the position of the sun during the day.</p><p>In the New Testament the Greek <em>hōra</em> functions both as the twelfth-part of day or night and as a theologically weighted term for a decisive appointed moment. John's Gospel in particular employs <em>the hour</em> as a recurring motif for the appointed time of Jesus's glorification through death and resurrection: <em>the hour has not yet come</em> (John 2:4; 7:30; 8:20) gives way to <em>the hour has come</em> (John 12:23; 13:1; 17:1), marking the theological turning point of the Gospel. Paul uses the same term eschatologically: <em>knowing the time, that now it is high time to awake out of sleep</em> (Romans 13:11).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hour",
            "smith": "hour",
            "isbe": "hour"
        },
        "key_refs": ["Daniel 4:19", "John 2:4", "John 12:23", "Romans 13:11"]
    },
    "house": {
        "id": "house",
        "term": "House",
        "category": "concepts",
        "intro": "<p>The house in biblical culture encompassed far more than a physical dwelling—it denoted the household, family, lineage, and dynastic continuity associated with a patriarchal line. The Hebrew <em>bayit</em> and Greek <em>oikos</em> serve simultaneously as dwelling-place, family unit, and dynasty (as in <em>the house of David</em>, <em>the house of Israel</em>). Until the sojourn in Egypt, the Hebrews primarily dwelt in tents; their transition to permanent houses in Canaan reflected the shift from nomadic to settled agricultural life.</p><p>Ancient Palestinian houses were typically constructed of stone or mudbrick with flat roofs (used for sleeping, drying flax, and prayer), built around a central courtyard that served as the household's working and social space. The theological significance of the house is immense: God desires to <em>dwell</em> in the midst of his people, and the tabernacle and temple are both called his <em>house</em>. Nathan's oracle to David (2 Samuel 7) is built on a wordplay between David's desire to build God a house (temple) and God's promise to build David a house (dynasty). Ultimately the New Testament describes the church as God's household (<em>oikos</em>, Ephesians 2:19) and believers' bodies as temples of the Holy Spirit (1 Corinthians 6:19).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "house",
            "smith": "house",
            "isbe": "house"
        },
        "key_refs": ["2 Samuel 7:5", "2 Samuel 7:11", "Ephesians 2:19", "1 Timothy 3:15"]
    },
    "hukkok": {
        "id": "hukkok",
        "term": "Hukkok",
        "category": "places",
        "intro": "<p>Hukkok was a border town on the tribal boundary of Naphtali, mentioned in Joshua 19:34 as a landmark point where the territory of Naphtali met the tribal lands of Asher and Zebulun. The name, meaning <em>engraver</em> or <em>decreed</em>, suggests either a craftsman's settlement or a place with some association with legal or written records. It is identified in 1 Chronicles 6:75 as the same location called Helkath, which was assigned to the Levites of the Gershomite clan from the territory of Asher.</p><p>The modern identification is proposed as Yakuk, a village on the northwestern slopes above the Plain of Gennesaret (Sea of Galilee), in the region where the territories of Naphtali, Asher, and Zebulun converged. The area around the northwest shore of the Sea of Galilee was later associated with Jesus's Galilean ministry, and Matthew 4:13–16 quotes Isaiah 9:1–2's reference to the lands of Zebulun and Naphtali as receiving the light of the Messiah—the same region that included Hukkok's territory.</p>",
        "sections": [],
        "hitchcock_meaning": "engraver; scribe; lawyer",
        "source_ids": {
            "easton": "hukkok",
            "smith": "hukkok",
            "isbe": "hukkok"
        },
        "key_refs": ["Joshua 19:34", "1 Chronicles 6:75"]
    },
    "hul": {
        "id": "hul",
        "term": "Hul",
        "category": "people",
        "intro": "<p>Hul was the second son of Aram son of Shem, listed in the table of nations in Genesis 10:23. Through his father Aram, Hul belongs to the Semitic branch of humanity in the post-flood genealogy. His name, meaning <em>circle</em> or <em>pain</em> (alternatively, <em>to turn</em>), follows the pattern of eponymous ancestor names in Genesis 10 that identify the progenitors of peoples and regions rather than historically developed individuals.</p><p>No region or people is specifically identified with Hul by name in other biblical texts, though ancient traditions and some scholars have associated him with the Huleh basin (the marshy lake region north of the Sea of Galilee) or with a territory in northern Mesopotamia. As with many figures in the table of nations, Hul represents a point in the genealogical framework through which Genesis organizes the known world of nations into a family descended from Noah, without providing independent narrative material about the figure himself.</p>",
        "sections": [],
        "hitchcock_meaning": "pain; infirmity",
        "source_ids": {
            "easton": "hul",
            "smith": "hul",
            "isbe": "hul"
        },
        "key_refs": ["Genesis 10:23", "1 Chronicles 1:17"]
    },
    "huldah": {
        "id": "huldah",
        "term": "Huldah",
        "category": "people",
        "intro": "<p>Huldah was a prophetess in Jerusalem during the reign of King Josiah, the wife of Shallum son of Tikvah, keeper of the wardrobe. When the high priest Hilkiah found the book of the Law in the temple during Josiah's restoration project, the king sent a delegation of the highest officials—including Hilkiah, Ahikam, Achbor, Shaphan, and Asaiah—to inquire of the LORD through a prophet. Rather than consulting Jeremiah or Zephaniah (both of whom were active at this time), they went to Huldah.</p><p>Huldah's response was authoritative and specific: she confirmed the authenticity of the book and pronounced that the judgments written in it would indeed fall on Judah because the people had abandoned God, but that because Josiah's heart was tender and he had humbled himself before the LORD, he would be gathered to his fathers in peace before the disaster came. Her oracle set in motion Josiah's sweeping religious reforms and the great Passover celebration of 621 BC. Huldah's central role in one of the most momentous events of late Judean history makes her one of the most significant female prophetic figures in the Old Testament.</p>",
        "sections": [],
        "hitchcock_meaning": "the world",
        "source_ids": {
            "easton": "huldah",
            "smith": "huldah",
            "isbe": "huldah"
        },
        "key_refs": ["2 Kings 22:14", "2 Kings 22:15", "2 Kings 22:20", "2 Chronicles 34:22"]
    },
    "humiliation-of-christ": {
        "id": "humiliation-of-christ",
        "term": "Humiliation of Christ",
        "category": "concepts",
        "intro": "<p>The humiliation of Christ refers to the voluntary condescension of the eternal Son of God in the incarnation and throughout his earthly life and death. The classical theological category of <em>humiliatio</em> is grounded in Philippians 2:5–11, where Paul describes Christ as being in the form of God, yet not regarding equality with God as something to be grasped, but emptying himself (<em>ekenōsen</em>), taking the form of a servant, being made in the likeness of humans, and being obedient to death—even death on a cross. This self-emptying (<em>kenosis</em>) is the doctrinal basis for the theology of humiliation.</p><p>Reformed and Lutheran theologians systematized Christ's humiliation as encompassing: (1) his incarnation and birth in humble circumstances; (2) his subjection to the Law; (3) his sufferings; (4) his death; and (5) his burial and descent to the realm of the dead. Each aspect represented a further stage in the voluntary condescension of one who was by nature Lord of all. The humiliation is inseparable from and is the precondition for the exaltation: the one who descended is the one who ascended above all heavens (Ephesians 4:10), and the name above every name is given precisely to the crucified one (Philippians 2:9–11).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "humiliation-of-christ",
            "isbe": "humiliation-of-christ"
        },
        "key_refs": ["Philippians 2:7", "Galatians 4:4", "Hebrews 2:9", "2 Corinthians 8:9"]
    },
    "humility": {
        "id": "humility",
        "term": "Humility",
        "category": "concepts",
        "intro": "<p>Humility (Hebrew <em>ʿānāwâ</em>, meekness; Greek <em>tapeinophrosynē</em>, lowliness of mind) is a prominent Christian and biblical virtue, denoting a realistic and submissive estimation of oneself before God and others. It is not self-deprecation or false modesty but the accurate recognition of one's creaturely dependence on God and the consequent posture of openness to others. The Greek word <em>tapeinophrosynē</em> was largely a new Christian coinage: in classical Greek, lowliness of mind was a weakness; the gospel elevated it to a virtue modeled by Christ himself.</p><p>Proverbs establishes humility as the precondition for honor: <em>Before honor is humility</em> (15:33; 18:12), and pride goes before destruction (16:18). Jesus pronounced the poor in spirit blessed (Matthew 5:3) and himself meek and lowly in heart (Matthew 11:29), washing his disciples' feet as a practical demonstration. Paul commands believers to regard others as more significant than themselves (Philippians 2:3) and grounds this in Christ's kenotic self-emptying. James 4:6 and 1 Peter 5:5 both cite Proverbs 3:34: <em>God opposes the proud but gives grace to the humble</em>—making humility the foundational orientation for receiving divine grace.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "humility",
            "isbe": "humility"
        },
        "key_refs": ["Proverbs 15:33", "Matthew 11:29", "Philippians 2:3", "James 4:6"]
    },
    "hunting": {
        "id": "hunting",
        "term": "Hunting",
        "category": "concepts",
        "intro": "<p>Hunting in the biblical world encompassed the pursuit and capture of wild game for food, sport, or pest control, using bows, snares, nets, and pits. The first biblical hunter of note is Nimrod, described in Genesis 10:9 as a mighty hunter before the LORD—a phrase that became proverbial in Israel. Esau was a skilled hunter, contrasted with his brother Jacob who was a man of the tents; his father Isaac's fondness for his venison played a role in the deception over the birthright blessing.</p><p>In the Mosaic law, hunting was permitted but circumscribed: any game animal killed in the field must have its blood covered with earth (Leviticus 17:13), acknowledging that life belongs to God even in the taking of wild animals. The Psalms and wisdom literature use the hunter's craft as a metaphor: the wicked set snares for the righteous (Psalm 140:5; 141:9–10), and the foreign woman of Proverbs hunts for the young man's life (Proverbs 6:26). The imagery of hunting as an expression of oppressive power appears in Jeremiah 16:16, where God threatens to send hunters against the exiles, and Ezekiel 13:18–20, where false prophetesses are condemned for hunting souls like birds.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hunting",
            "smith": "hunting",
            "isbe": "hunting"
        },
        "key_refs": ["Genesis 10:9", "Genesis 25:27", "Leviticus 17:13", "Jeremiah 16:16"]
    },
    "hur": {
        "id": "hur",
        "term": "Hur",
        "category": "people",
        "intro": "<p>Hur is a name borne by several notable figures in the Old Testament. The most prominent was the companion of Moses and Aaron at the battle of Rephidim, where Hur helped Aaron hold up Moses's hands so that the staff of God remained raised; when his hands were lowered, Amalek prevailed, but when they were raised, Israel prevailed—and Hur and Aaron supported Moses's arms until sunset and Israel's victory was complete. Hur and Aaron were also left in charge of the people while Moses ascended Sinai for forty days.</p><p>A second Hur was the son of Caleb by his wife Ephrath (Azubah), making him an ancestor of the craftsman Bezalel who constructed the tabernacle furnishings. A third Hur was the husband of Miriam according to Jewish tradition, though this is not stated in the canonical text. A fourth was a king of Midian slain by Israel in the campaign against the Midianites after the incident with Baal-peor (Numbers 31:8). The name's meaning—<em>liberty, whiteness</em> or <em>hole</em>—is variously interpreted, and its frequency reflects its common usage as a personal name in ancient Israel.</p>",
        "sections": [],
        "hitchcock_meaning": "liberty; whiteness; hole",
        "source_ids": {
            "easton": "hur",
            "isbe": "hur"
        },
        "key_refs": ["Exodus 17:10", "Exodus 17:12", "Exodus 24:14", "1 Chronicles 2:19"]
    },
    "hurai": {
        "id": "hurai",
        "term": "Hurai",
        "category": "people",
        "intro": "<p>Hurai of the valleys of Gaash was one of David's thirty mighty men, the elite warriors celebrated in the list of David's heroes in 1 Chronicles 11. His name, meaning <em>linen-worker</em> (some render it as related to freedom or whiteness), and his identification as coming from the valleys of Gaash—the region of hills in Ephraim associated with Joshua's burial place—places him in the territory of the central hill country of Israel.</p><p>The parallel passage in 2 Samuel 23:30 spells the name as Hiddai, suggesting a scribal variant in the transmission of the list. As with most of the thirty, Hurai's inclusion in the catalog of mighty men documents his military prowess and personal loyalty to David during the years of his reign, without providing individual narrative accounts of his specific exploits. The list of David's heroes reflects the composition of a professional warrior elite that formed the backbone of the Davidic military establishment.</p>",
        "sections": [],
        "hitchcock_meaning": "linen-worker",
        "source_ids": {
            "easton": "hurai",
            "isbe": "hurai"
        },
        "key_refs": ["1 Chronicles 11:32", "2 Samuel 23:30"]
    },
    "husband": {
        "id": "husband",
        "term": "Husband",
        "category": "concepts",
        "intro": "<p>The husband in biblical society occupied the central structural role in the household (<em>bayit</em>), the basic social unit of Israelite life. The English word husband derives from <em>house-bond</em> (the one who binds the household together), and this imagery is apt for the biblical conception: the husband was responsible for the economic provision, protection, and spiritual leadership of the household. The Mosaic law gave husbands considerable authority but also placed obligations on them: a man who falsely accused his wife of premarital unchastity was flogged and fined (Deuteronomy 22:18–19); a husband could not arbitrarily dismiss a wife he had taken captive (Deuteronomy 21:14).</p><p>The covenantal relationship of husband and wife became a primary metaphor in the prophets for God's relationship with Israel: God is Israel's husband (Jeremiah 3:14; Hosea 2:16), and Israel's idolatry is consistently described as adultery and prostitution against this relationship. The New Testament extends the metaphor to Christ and the church (Ephesians 5:22–33), with the husband's sacrificial love for his wife grounded in Christ's self-giving love for the church. Paul's household code instruction that husbands love their wives as Christ loved the church radically elevated the husband's responsibility to one of costly self-sacrifice rather than mere authority.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "husband",
            "smith": "husband",
            "isbe": "husband"
        },
        "key_refs": ["Jeremiah 3:14", "Hosea 2:16", "Ephesians 5:25", "1 Peter 3:7"]
    },
    "husbandman": {
        "id": "husbandman",
        "term": "Husbandman",
        "category": "concepts",
        "intro": "<p>A husbandman was one whose livelihood was the cultivation of the ground—a farmer, tiller, or vinedresser. The term reflects the foundational importance of agriculture in Israelite society: the land of Canaan was God's gift to Israel, and its cultivation expressed both dependence on God's provision and faithful stewardship of the covenant inheritance. Agriculture was among the earliest occupations of humanity (Genesis 2:15; 3:19), and Noah is specifically called the first tiller of the ground after the flood (Genesis 9:20).</p><p>The husbandman appears prominently in the parables of Jesus as a metaphor for those responsible for bearing fruit in the kingdom: the parable of the tenants (Matthew 21:33–41; Mark 12:1–9; Luke 20:9–16) depicts the rejected son sent by the vineyard owner to collect its fruit. John 15:1 presents God as the true husbandman who tends the vine (Christ) and prunes its branches (disciples) to produce more fruit. Paul uses the husbandman's expectation of harvest as a basis for the worker's right to share in the fruits of his labor (2 Timothy 2:6), and James points to the farmer's patient waiting for the early and late rains as a model of eschatological patience (James 5:7).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "husbandman",
            "isbe": "agriculture"
        },
        "key_refs": ["Genesis 9:20", "Matthew 21:33", "John 15:1", "James 5:7"]
    },
    "hushai": {
        "id": "hushai",
        "term": "Hushai",
        "category": "people",
        "intro": "<p>Hushai the Archite was David's close friend and counselor, described in 1 Chronicles 27:33 as <em>the king's friend</em>—a formal court title. His most celebrated service to David was during the rebellion of Absalom. When David fled Jerusalem, Hushai came to meet him with his robe torn and earth on his head in mourning. David sent him back to Jerusalem as a counter-spy, instructing him to feign loyalty to Absalom and undermine the advice of Ahithophel, who had joined the rebellion.</p><p>Hushai's finest moment came when Absalom convened his council: Ahithophel gave tactically excellent advice to pursue David immediately with a swift force before David could reorganize. Hushai successfully countered this counsel with advice to gather all Israel and overwhelm David in open battle—a delay that gave David time to prepare and ultimately survive. The narrative comments that God had ordained to defeat the good counsel of Ahithophel in order to bring disaster on Absalom. Ahithophel, seeing that his counsel was not followed, went home and hanged himself. Hushai's intelligence service through Jonathan and Ahimaaz at En-rogel was integral to David's survival of his most serious political crisis.</p>",
        "sections": [],
        "hitchcock_meaning": "their haste; their sensuality; their silence",
        "source_ids": {
            "easton": "hushai",
            "isbe": "hushai"
        },
        "key_refs": ["2 Samuel 15:37", "2 Samuel 16:16", "2 Samuel 17:7", "2 Samuel 17:14"]
    },
    "husk": {
        "id": "husk",
        "term": "Husk",
        "category": "concepts",
        "intro": "<p>Husk in the King James Bible refers to two different Hebrew objects. In Numbers 6:4, the husk (<em>zag</em>) is the outer skin or husk of a grape, which Nazirites were forbidden to eat along with all other grape products during their vow. In 2 Kings 4:42, husk (<em>ṣiqlōn</em>) refers to a sack or bag used to carry grain, part of the firstfruits offering brought to Elisha by a man from Baal-shalishah.</p><p>The most memorable use of the concept in the New Testament, though not using the word husk, is the prodigal son's degradation to feeding pigs and longing to fill himself with the carob pods (<em>keratia</em>) the pigs ate—the nadir of his spiritual and material ruin. The outer husks or coverings of grain, grapes, and pods represented the margins and leavings of agricultural production—the portions eaten by animals or discarded by humans. Their use in contexts of extreme poverty or Nazirite renunciation illustrates how ordinary agricultural waste could carry significant moral or ritual significance in biblical narrative.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "husk",
            "isbe": "husk"
        },
        "key_refs": ["Numbers 6:4", "2 Kings 4:42", "Luke 15:16"]
    },
    "hymn": {
        "id": "hymn",
        "term": "Hymn",
        "category": "concepts",
        "intro": "<p>The hymn in biblical usage denoted a song of praise addressed to God, distinguished in the New Testament from psalms (<em>psalmoi</em>) and spiritual songs (<em>ōdai pneumatikai</em>) in the triad of worship music mentioned in Ephesians 5:19 and Colossians 3:16. The Greek <em>hymnos</em> carried the sense of a formal song of divine praise, and the verb <em>hymneō</em> (to sing a hymn) appears in Matthew 26:30 and Mark 14:26 for the singing of the Hallel psalms (Psalms 113–118) at the conclusion of the Passover meal—the final act of Jesus and his disciples before Gethsemane.</p><p>The New Testament letters preserve what are widely believed to be fragments of early Christian hymns: Philippians 2:6–11 (the kenosis hymn), Colossians 1:15–20 (the cosmic Christ hymn), 1 Timothy 3:16, and the doxologies of Revelation. These suggest that hymn-singing was among the earliest and most characteristic practices of Christian worship. The exhortation to sing with grace in your hearts to the Lord (Colossians 3:16) makes hymn-singing both a communal act and an inward disposition of gratitude, with the sung word of Christ dwelling richly in the congregation.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hymn",
            "smith": "hymn",
            "isbe": "hymn"
        },
        "key_refs": ["Matthew 26:30", "Ephesians 5:19", "Colossians 3:16", "Philippians 2:6"]
    },
    "hypocrite": {
        "id": "hypocrite",
        "term": "Hypocrite",
        "category": "concepts",
        "intro": "<p>Hypocrite (Greek <em>hypokritēs</em>, literally an actor who plays a role beneath a mask) was a term Jesus applied with particular intensity to scribes and Pharisees who performed religious duties for public recognition rather than genuine devotion to God. The word entered biblical vocabulary from Greek theater, where actors wore masks to represent characters—the hypocrite presents a face that is not their own. Jesus's seven woes in Matthew 23 are addressed repeatedly to <em>scribes and Pharisees, hypocrites</em>, cataloging specific failures: they shut the kingdom against others, devour widows' houses while making long prayers, make converts twice as fit for hell, strain out gnats while swallowing camels, clean the outside of the cup while the inside is full of greed.</p><p>The Sermon on the Mount (Matthew 6:2, 5, 16) identifies the hypocrite's motivation as human applause: they give alms with trumpets, pray standing in synagogues to be seen, and disfigure their faces while fasting so that others will notice their devotion. The Hebrew equivalent in Job and the wisdom literature (<em>ḥānēph</em>, profane or godless one) captures the element of insincerity and irreligion beneath a religious exterior. Jesus's teaching consistently locates authenticity in the hiddenness of the heart rather than in public performance.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hypocrite",
            "isbe": "hypocrite"
        },
        "key_refs": ["Matthew 6:2", "Matthew 6:5", "Matthew 23:13", "Luke 12:56"]
    },
    "hyssop": {
        "id": "hyssop",
        "term": "Hyssop",
        "category": "concepts",
        "intro": "<p>Hyssop (Hebrew <em>ʾêzôb</em>, Greek <em>hyssōpos</em>) was a small bushy plant used extensively in Israelite purification rites for its ability to hold and sprinkle liquid. Its first biblical appearance is at the Passover in Egypt, where it was used to apply the lamb's blood to the doorposts and lintel (Exodus 12:22). This initial association with protective blood established hyssop as the instrument of atoning application throughout the Levitical law: it was used in the purification of lepers, the cleansing of houses affected by mold, and the sprinkling of blood in the red heifer ceremony (Numbers 19).</p><p>The plant's identity has been debated—the most likely candidate is the Syrian hyssop (<em>Origanum syriacum</em>), a common bushy herb of Palestinian rock walls that forms natural bunches suitable for use as a sprinkler. Psalm 51:7 uses hyssop as a metaphor for deep inner cleansing: <em>Purge me with hyssop, and I shall be clean</em>. At the crucifixion, a sponge of sour wine was offered to Jesus on a hyssop branch (John 19:29), connecting the Passover sacrifice imagery to the cross. Hebrews 9:19 cites Moses's use of hyssop at Sinai to complete the typological pattern of blood, hyssop, and covenant.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "hyssop",
            "smith": "hyssop",
            "isbe": "hyssop"
        },
        "key_refs": ["Exodus 12:22", "Psalm 51:7", "John 19:29", "Hebrews 9:19"]
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
    print(f'BP h4: Hillel → Hyssop: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
