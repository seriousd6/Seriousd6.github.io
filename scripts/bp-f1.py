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
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True

ARTICLES = {
"fable": {
  "id": "fable", "term": "Fable", "category": "concepts",
  "intro": "<p>Fable, in biblical usage, does not refer to the literary genre of moralizing animal stories but to invented or speculative religious teaching without scriptural grounding. The Greek <em>mythos</em> (translated \"fable\" or \"myth\" in the New Testament) denotes a fictitious narrative or tradition — specifically, the kind of speculative theological discourse that was circulating in certain Jewish and Hellenistic Christian communities of the first century.</p><p>Paul warns Timothy against giving attention to \"endless genealogies\" and \"old wives' fables\" (<a class=\"ref\" data-ref=\"1 Timothy 1:4\">1 Timothy 1:4</a>; <a class=\"ref\" data-ref=\"1 Timothy 4:7\">1 Timothy 4:7</a>; <a class=\"ref\" data-ref=\"2 Timothy 4:4\">2 Timothy 4:4</a>), opposing these to sound doctrine grounded in the apostolic gospel. Titus 1:14 similarly warns against \"Jewish fables\" that distracted from the truth. Peter's contrast is equally pointed: the apostolic witness to Christ was \"not cunningly devised fables\" but eyewitness testimony (<a class=\"ref\" data-ref=\"2 Peter 1:16\">2 Peter 1:16</a>). The New Testament thus uses the term polemically to contrast revealed apostolic truth with human religious invention.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fable", "isbe": "fable"},
  "key_refs": ["1 Timothy 1:4", "1 Timothy 4:7", "2 Timothy 4:4", "2 Peter 1:16"]
},
"face": {
  "id": "face", "term": "Face", "category": "concepts",
  "intro": "<p>Face (<em>panim</em> in Hebrew) carries in Scripture a weight far beyond its literal meaning. In biblical idiom, a person's face represents their very presence, attention, and favor — or the withdrawal thereof. To seek someone's face is to seek their presence; to hide one's face signifies rejection or grief. When God's face shines upon someone it denotes blessing and acceptance, as in the Aaronic benediction (Numbers 6:25); when he hides his face it signals divine displeasure or the experience of abandonment (<a class=\"ref\" data-ref=\"Psalms 44:3\">Psalm 44:3</a>; <a class=\"ref\" data-ref=\"Daniel 9:17\">Daniel 9:17</a>).</p><p>The expression \"face of God\" (<em>pene yhwh</em>) appears throughout the Old Testament as a reverential way of speaking of the divine presence. Adam and Eve hid themselves from the \"face of the Lord God\" after the fall (<a class=\"ref\" data-ref=\"Genesis 3:8\">Genesis 3:8</a>), and Moses was told that no man could see God's face and live (<a class=\"ref\" data-ref=\"Exodus 33:14\">Exodus 33:14-15</a>), yet was granted to see his glory from behind. The New Testament escalates this theme: the disciples saw God's glory in the face of Jesus Christ (2 Corinthians 4:6), and the final beatitude of the redeemed is to see God's face directly (Revelation 22:4).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "face", "isbe": "face"},
  "key_refs": ["Genesis 3:8", "Exodus 33:14", "Psalms 44:3", "Daniel 9:17"]
},
"fair-havens": {
  "id": "fair-havens", "term": "Fair Havens", "category": "places",
  "intro": "<p>Fair Havens is a natural harbour on the southern coast of the island of Crete, situated approximately five miles east of the town of Lasea. It is mentioned once in Scripture, in the account of Paul's voyage to Rome (<a class=\"ref\" data-ref=\"Acts 27:8\">Acts 27:8</a>), when the ship carrying him as a prisoner found temporary shelter there after difficult sailing.</p><p>Though the harbour offered some protection, the ship's officers and owner judged it unsuitable for wintering — it was exposed to certain winds — and overruled Paul's counsel to remain. They pressed on for the port of Phoenix, also in Crete, but were caught by a violent northeaster known as Euroclydon, the storm that eventually wrecked the ship near Malta. Fair Havens thus appears in the narrative as the last point of safety before catastrophe, the place where Paul's warning to stay went unheeded.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fair-havens", "smith": "fair-havens"},
  "key_refs": ["Acts 27:8"]
},
"fairs": {
  "id": "fairs", "term": "Fairs", "category": "concepts",
  "intro": "<p>Fairs (<em>'izabhonim</em> in Hebrew) is an archaic English rendering of a word found seven times in Ezekiel 27 and nowhere else in Scripture. The passage is a lament over Tyre, the great Phoenician commercial city, and the Hebrew word refers to the merchandise or wares exchanged in trade — what modern translations render as \"wares\" or \"merchandise\" rather than \"fairs\" in the sense of a market event (<a class=\"ref\" data-ref=\"Ezekiel 27\">Ezekiel 27</a>).</p><p>Ezekiel 27 is a remarkable economic document, cataloguing Tyre's trading partners across the ancient Near East and Mediterranean world — from Tarshish in the west to Persia in the east, with specific trade goods listed for each region: silver, iron, tin, lead, slaves, horses, ivory, and spices. The theological force of the chapter is the fragility of commercial wealth: the very ships that made Tyre rich become the vessels of her destruction when the east wind shatters them in the heart of the sea.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fairs", "smith": "fairs", "isbe": "fairs"},
  "key_refs": ["Ezekiel 27"]
},
"faith": {
  "id": "faith", "term": "Faith", "category": "concepts",
  "intro": "<p>Faith (<em>pistis</em> in Greek; <em>'emunah</em> in Hebrew) is one of the central categories of biblical theology. In both Testaments, faith denotes a settled trust and confidence in God — his character, his promises, and his acts — that issues in allegiance and obedience. The Old Testament uses <em>'emunah</em> primarily of God's own faithfulness (his reliable steadfastness), while applied to human beings it describes the posture of trusting reliance on God's word, as exemplified in Abraham who \"believed God, and it was counted to him as righteousness\" (Genesis 15:6; Romans 4:3).</p><p>The New Testament deepens and focuses this concept on the person and work of Jesus Christ. Paul's great epistles to Rome and Galatia argue that justification before God comes through faith in Christ alone, not by works of the law (<a class=\"ref\" data-ref=\"Romans 10:14\">Romans 10:14</a>; <a class=\"ref\" data-ref=\"Philippians 1:27\">Philippians 1:27</a>). Hebrews 11 surveys the great cloud of witnesses who lived and died by faith, defining it as \"the substance of things hoped for, the evidence of things not seen.\" John's Gospel characteristically speaks of \"believing into\" (<em>pisteuein eis</em>) Christ — a dynamic trust that involves commitment to a person. Faith is thus inseparable from knowledge of God in Christ (<a class=\"ref\" data-ref=\"John 10:38\">John 10:38</a>; <a class=\"ref\" data-ref=\"1 John 2:3\">1 John 2:3</a>) and is consistently distinguished from mere intellectual assent.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "faith", "isbe": "faith"},
  "key_refs": ["Romans 10:14", "Philippians 1:27", "John 10:38", "1 John 2:3"]
},
"faithful": {
  "id": "faithful", "term": "Faithful", "category": "concepts",
  "intro": "<p>Faithful, as a designation of Christians in the New Testament, means full of faith — actively trusting — rather than simply being trustworthy or reliable. The Greek <em>pistos</em> carries both senses (one who believes and one who can be trusted), but in its application to believers it emphasizes the quality of living trust rather than mere moral reliability. It appears as a standard term for members of the Christian community in Paul's letters: \"the faithful in Christ Jesus\" (Ephesians 1:1), \"the faithful brethren in Christ\" (<a class=\"ref\" data-ref=\"Colossians 1:2\">Colossians 1:2</a>), and \"believers\" (<a class=\"ref\" data-ref=\"Acts 10:45\">Acts 10:45</a>; <a class=\"ref\" data-ref=\"Acts 16:1\">Acts 16:1</a>; <a class=\"ref\" data-ref=\"2 Corinthians 6:15\">2 Corinthians 6:15</a>).</p><p>The term also describes the character that God and Christ exhibit: God is called faithful because he keeps his covenant promises (1 Corinthians 10:13; 1 Thessalonians 5:24), and Christ is \"the faithful witness\" (Revelation 1:5). For human beings, faithfulness — particularly in stewardship and endurance under trial — is consistently commended as the character fitting those who serve a faithful God (<a class=\"ref\" data-ref=\"1 Timothy 4:3\">1 Timothy 4:3</a>).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "faithful"},
  "key_refs": ["Acts 10:45", "Acts 16:1", "2 Corinthians 6:15", "Colossians 1:2"]
},
"fall-of-man": {
  "id": "fall-of-man", "term": "Fall of Man", "category": "events",
  "intro": "<p>The Fall of Man is the theological designation for the primeval event recorded in Genesis 3, when the first human pair — Adam and Eve — disobeyed God's command by eating the fruit of the tree of the knowledge of good and evil at the instigation of the serpent. The expression itself derives from the Apocryphal Book of Wisdom and entered standard theological vocabulary to capture the gravity of this revolt: a catastrophic departure from the original created goodness of humanity.</p><p>The narrative in Genesis 2–3 sets the fall against the backdrop of humanity's creation in God's image, their placement in the garden, and the single prohibition. The consequences that follow — shame, broken relationship with God, expulsion from Eden, the curse on the ground, and mortality — shape all subsequent biblical history. Paul's theology of redemption in <a class=\"ref\" data-ref=\"Romans 1:1\">Romans</a> and elsewhere treats the fall as the definitive event that introduced universal sin and death, making Christ's obedience as the second Adam the necessary counterpart: \"As in Adam all die, so in Christ shall all be made alive\" (1 Corinthians 15:22). John 3:7 ('\"You must be born again\"') presupposes the same broken starting-point.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fall-of-man"},
  "key_refs": ["Genesis 2", "Romans 1:1", "Romans 5:12", "John 3:7"]
},
"fallow-deer": {
  "id": "fallow-deer", "term": "Fallow-deer", "category": "concepts",
  "intro": "<p>Fallow-deer (<em>yahmur</em> in Hebrew, from a root meaning \"to be red\") is listed among the clean animals permitted for food in <a class=\"ref\" data-ref=\"Deuteronomy 14:5\">Deuteronomy 14:5</a> and appears in the list of provisions for Solomon's royal table (<a class=\"ref\" data-ref=\"1 Kings 4:23\">1 Kings 4:23</a>). The precise identification of the Hebrew term has been disputed: the Revised Version renders it \"wild goat\" in Deuteronomy and \"roebucks\" in 1 Kings, reflecting uncertainty about whether the fallow deer (<em>Cervus dama</em>) was native to ancient Palestine.</p><p>Most modern scholars identify <em>yahmur</em> with the roebuck (<em>Capreolus capreolus</em>) or a similar deer species, though the fallow deer was known in the wider Mediterranean world. The entry's significance is primarily for the biblical dietary laws and for the picture of royal abundance in Solomon's court, where such game animals were among the provisions consumed daily. The mention in Deuteronomy establishes its cleanness for Israelite consumption.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fallow-deer", "smith": "fallow-deer"},
  "key_refs": ["Deuteronomy 14:5", "1 Kings 4:23"]
},
"fallow-ground": {
  "id": "fallow-ground", "term": "Fallow Ground", "category": "concepts",
  "intro": "<p>Fallow ground refers to land that has been left unplowed and unseeded — ground that has hardened through neglect and become overgrown with weeds. In Palestinian agriculture, allowing a field to lie fallow for a season was sometimes beneficial, but the prophetic use of the image is consistently negative, representing a spiritual condition of hardness and unpreparedness.</p><p>Both Hosea and Jeremiah employ the image to call Israel to repentance. \"Break up your fallow ground\" (<a class=\"ref\" data-ref=\"Hosea 10:12\">Hosea 10:12</a>; <a class=\"ref\" data-ref=\"Jeremiah 4:3\">Jeremiah 4:3</a>) means essentially: do not sow seed in ground that is spiritually unprepared — break off your evil ways and prepare your hearts to receive the word of God. The metaphor parallels Jesus's parable of the sower, where the condition of the soil determines whether the seed takes root. In both prophets the call to break up fallow ground is accompanied by calls to seek righteousness and return to the Lord.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fallow-ground"},
  "key_refs": ["Hosea 10:12", "Jeremiah 4:3"]
},
"familiar-spirit": {
  "id": "familiar-spirit", "term": "Familiar Spirit", "category": "concepts",
  "intro": "<p>A familiar spirit (<em>'ob</em> in Hebrew) was the supposed spirit of a dead person who could be consulted by a necromancer or medium. The practitioners who claimed to possess such spirits were called in Hebrew <em>ba'al 'ob</em> (\"masters of the ob\") and are consistently condemned in Mosaic law as engaging in a detestable practice of the nations. Leviticus 19:31 and 20:6 forbid Israelites from consulting them; Deuteronomy 18:11 lists communication with familiar spirits among the abominable divination practices that were driving the Canaanites from the land.</p><p>The most extended biblical narrative involving a familiar spirit is Saul's consultation of the woman at Endor (<a class=\"ref\" data-ref=\"Deuteronomy 18:11\">1 Samuel 28</a>), where the king, having expelled all mediums from the land, secretly sought one out on the eve of his final battle. The event underscores the prohibition's gravity: Saul's action was cited as one of the reasons for his death and the transfer of the kingdom (<a class=\"ref\" data-ref=\"2 Kings 21:6\">2 Kings 21:6</a>; <a class=\"ref\" data-ref=\"2 Chronicles 33:6\">2 Chronicles 33:6</a>; 1 Chronicles 10:13). King Manasseh's consulting of familiar spirits is likewise numbered among the sins that provoked God's judgment on Judah.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "familiar-spirit"},
  "key_refs": ["Deuteronomy 18:11", "Leviticus 19:31", "Leviticus 20:6", "2 Kings 21:6"]
},
"famine": {
  "id": "famine", "term": "Famine", "category": "concepts",
  "intro": "<p>Famine (<em>ra'ab</em> in Hebrew) was a recurring feature of life in the ancient Near East and Palestine, resulting from drought, locust invasions, military siege, or crop failure. Scripture records numerous famines that shaped the course of redemptive history. The first recorded famine compelled Abraham to go down to Egypt (<a class=\"ref\" data-ref=\"Genesis 26:1\">Genesis 26:1</a>); a later famine brought Jacob's sons to Egypt for grain, becoming the occasion of Joseph's revelation and the family's settlement in Egypt (<a class=\"ref\" data-ref=\"Genesis 41:1\">Genesis 41:1</a>). During the period of the judges and the kings, famines appear as instruments of divine judgment (<a class=\"ref\" data-ref=\"2 Kings 8:1\">2 Kings 8:1</a>).</p><p>The law of Moses connects the abundance of harvests with covenant faithfulness (Deuteronomy 28:15-24) and famine with covenant violation — a pattern the prophets repeatedly invoke. Amos 8:11 introduces a distinctive form: a famine \"not of bread, nor a thirst for water, but of hearing the words of the LORD,\" spiritual deprivation that is more catastrophic than physical want. In the New Testament, famine appears in Jesus's eschatological discourse (Matthew 24:7) and in the prodigal son's experience (Luke 15:14), where it provides the external crisis that turns his mind homeward.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "famine", "smith": "famine", "isbe": "famine"},
  "key_refs": ["Genesis 26:1", "Genesis 41:1", "2 Kings 8:1", "Amos 8:11"]
},
"fan": {
  "id": "fan", "term": "Fan", "category": "concepts",
  "intro": "<p>Fan (or winnowing shovel) was the agricultural implement used to separate grain from chaff after threshing. The grain was threshed on an open floor — typically a flat rock on a hilltop — and then the threshed mass was tossed into the air with a wooden shovel or fork. The wind carried the lighter chaff away while the heavier grain fell back to the floor (<a class=\"ref\" data-ref=\"Isaiah 30:24\">Isaiah 30:24</a>; <a class=\"ref\" data-ref=\"Jeremiah 15:7\">Jeremiah 15:7</a>).</p><p>The image of winnowing provided a powerful biblical metaphor for divine judgment. God as a divine winnower separates the righteous from the wicked just as grain is separated from chaff. Jeremiah 15:7 uses the image to describe God's judgment on Israel. John the Baptist employed it for Christ: \"His winnowing fan is in his hand, and he will thoroughly purge his floor, and gather his wheat into the garner; but he will burn up the chaff with unquenchable fire\" (<a class=\"ref\" data-ref=\"Matthew 3:12\">Matthew 3:12</a>). This eschatological use of the winnowing image became one of the most vivid pictures of final judgment in the Synoptic Gospels.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fan", "smith": "fan"},
  "key_refs": ["Isaiah 30:24", "Jeremiah 15:7", "Matthew 3:12"]
},
"farm": {
  "id": "farm", "term": "Farm", "category": "concepts",
  "intro": "<p>Farm, in the biblical context, refers to a cultivated field or agricultural holding. Every Hebrew family under the Mosaic system held an allotment of land as an ancestral possession (Numbers 26:33-56), so farming was both an economic necessity and a covenantal feature of Israelite life. The basic farming activities — plowing, sowing, harvesting — appear throughout Scripture as sources of metaphor, illustration, and instruction.</p><p>The one explicit New Testament occurrence in <a class=\"ref\" data-ref=\"Matthew 22:5\">Matthew 22:5</a> is notable: in the parable of the great banquet, one invited guest excuses himself saying he must attend to his farm, and another to his merchandise. Jesus uses the farm — a legitimate and honorable pursuit — as an example of a good thing that becomes an idol when it crowds out the call of the kingdom. The parable of the sower (Matthew 13) similarly uses the imagery of seed, soil, and harvest to describe the reception of the word of God in different hearts.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "farm", "isbe": "farm"},
  "key_refs": ["Matthew 22:5", "Numbers 26:33", "1 Kings 19:19"]
},
"farthing": {
  "id": "farthing", "term": "Farthing", "category": "concepts",
  "intro": "<p>Farthing is the English rendering of two distinct Greek coins in the New Testament. The first is the <em>assarion</em> (Matthew 10:29; Luke 12:6), a small Roman bronze coin equal to one-tenth of a denarius, corresponding roughly to the Roman <em>as</em>. Jesus uses it to illustrate the Father's providential care: \"Are not two sparrows sold for a farthing? and one of them shall not fall to the ground without your Father.\" Luke's version records five sparrows for two farthings, showing that even the extra sparrow thrown in free of charge is known to God.</p><p>The second is the <em>kodrantes</em> (<a class=\"ref\" data-ref=\"Matthew 5:26\">Matthew 5:26</a>; <a class=\"ref\" data-ref=\"Mark 12:42\">Mark 12:42</a>), the quadrans — the smallest Roman copper coin, worth one-quarter of an assarion or one-sixty-fourth of a denarius. Mark identifies the widow's two mites (<em>lepta</em>) as making one farthing/quadrans. Together these coins appear in contexts emphasizing divine valuation of the least and lowest: God's care for the cheapest sparrow, and his commendation of the widow's smallest possible offering.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "farthing", "smith": "farthing"},
  "key_refs": ["Matthew 10:29", "Luke 12:6", "Matthew 5:26", "Mark 12:42"]
},
"fast": {
  "id": "fast", "term": "Fast", "category": "concepts",
  "intro": "<p>Fasting (<em>tsom</em> in Hebrew; <em>nesteia</em> in Greek) is the voluntary abstention from food and sometimes drink as a religious act of humiliation, mourning, petition, or consecration. The Mosaic law mandated only a single annual fast — the Day of Atonement (<a class=\"ref\" data-ref=\"Leviticus 23:26\">Leviticus 23:26-32</a>), referred to in Acts 27:9 simply as \"the fast.\" However, additional fasts arose throughout Israelite history in response to calamity, national crisis, and repentance (Joel 1:14; 2:15; Zechariah 7–8 records four commemorative fasts).</p><p>The prophets challenged fasting that was divorced from justice and genuine repentance (Isaiah 58:3-7; Zechariah 7:5), insisting that God does not desire external religious performance but the broken and contrite heart. Jesus in the Sermon on the Mount assumes his disciples will fast but instructs them to do so without ostentation (Matthew 6:16-18). After the resurrection, fasting appears as a practice associated with prayer in decisive moments of church discernment and mission (<a class=\"ref\" data-ref=\"Acts 27:9\">Acts 13:2-3; 14:23</a>).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fast"},
  "key_refs": ["Leviticus 23:26", "Acts 27:9", "Zechariah 7:1", "Matthew 6:16"]
},
"fat": {
  "id": "fat", "term": "Fat", "category": "concepts",
  "intro": "<p>Fat (<em>heleb</em> in Hebrew) denoted the richest and choicest portion of an animal. In Israelite sacrificial law, the fat of animals sacrificed — specifically the fat covering the entrails, the kidneys, and the liver — was reserved exclusively for God and was never to be eaten: \"All the fat is the LORD's\" (Leviticus 3:16). This prohibition applied to oxen, sheep, and goats offered in sacrifice, though fat from other contexts (e.g., animals that died naturally or were torn) had different regulations.</p><p>The dedication of the fat to God appears already in Abel's offering: he brought the \"fat portions\" (<a class=\"ref\" data-ref=\"Genesis 4:4\">Genesis 4:4</a>) from the firstlings of his flock, which the LORD regarded with favor. The fat's identification with the best and richest portion also gives the term a transferred sense: \"the fat of the land\" (Genesis 45:18) means its finest produce, and \"the fat of wheat\" (<a class=\"ref\" data-ref=\"Psalms 81:16\">Psalm 81:16</a>) signifies its finest grain. The priestly burning of the fat on the altar thus symbolized the dedication of the best to God.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fat", "smith": "fat", "isbe": "fat"},
  "key_refs": ["Genesis 4:4", "Leviticus 3:16", "Psalms 81:16"]
},
"father": {
  "id": "father", "term": "Father", "category": "concepts",
  "intro": "<p>Father is used in Scripture in several distinct senses. In its most immediate sense it denotes a male parent or ancestor, and the term is extended to any forefather or predecessor: Abraham is called \"father\" by his descendants across many generations (<a class=\"ref\" data-ref=\"Matthew 3:9\">Matthew 3:9</a>; <a class=\"ref\" data-ref=\"Deuteronomy 1:11\">Deuteronomy 1:11</a>). As a title of honor and respect, \"father\" was applied to tribal leaders, priests, prophets, royal counselors, and teachers, as when Micah's hired Levite is called \"a father and a priest\" (Judges 17:10).</p><p>Most profoundly, \"Father\" is the supreme biblical name for God in his relationship to his people. In the Old Testament, God is Father of Israel in a corporate, covenantal sense (Deuteronomy 32:6; Hosea 11:1). Jesus radically deepened this: he addressed God as <em>Abba</em> (Father) in prayer and taught his disciples to do the same (Matthew 6:9; Romans 8:15), grounding this intimacy in his own unique divine sonship. The New Testament consistently distinguishes Jesus as Son of God in a way that differs qualitatively from the adopted sonship of believers, yet both relationships derive their meaning from the same Father (<a class=\"ref\" data-ref=\"1 Kings 15:11\">John 20:17</a>).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "father", "smith": "father", "isbe": "father"},
  "key_refs": ["Deuteronomy 1:11", "Matthew 3:9", "Judges 17:10", "John 20:17"]
},
"fathom": {
  "id": "fathom", "term": "Fathom", "category": "concepts",
  "intro": "<p>Fathom (Greek <em>orguia</em>, from a verb meaning \"to stretch\") was a unit of nautical depth measurement equal to six feet — the span of a man's outstretched arms. The term appears once in the New Testament, in the account of Paul's shipwreck, when the sailors sounded the depth of the sea and found \"twenty fathoms\" (approximately 120 feet), and shortly after \"fifteen fathoms\" (<a class=\"ref\" data-ref=\"Acts 27:28\">Acts 27:28</a>), the shallowing confirming their approach to land in darkness.</p><p>The old English word \"fathom\" derives from the Anglo-Saxon <em>faethm</em> (\"bosom\" or the outstretched arms), paralleling the Greek etymology. As a nautical measurement, the fathom remained standard practice for centuries. The detail in Acts 27 reflects Luke's accurate depiction of first-century seamanship and contributes to the recognized historical precision of his account of Paul's voyage to Rome.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fathom", "smith": "fathom"},
  "key_refs": ["Acts 27:28"]
},
"fatling": {
  "id": "fatling", "term": "Fatling", "category": "concepts",
  "intro": "<p>Fatling refers to a young, fattened animal — typically a calf, sheep, or goat — set apart and fed specifically to be slaughtered for sacrifice or feasting. The Hebrew term (<em>meri'</em>) and related words emphasize the animal's specially nourished condition. Fatlings appear in contexts of celebration (<a class=\"ref\" data-ref=\"2 Samuel 6:13\">2 Samuel 6:13</a>), royal feasts, and temple sacrifice.</p><p>The term carries eschatological significance in Isaiah's vision of the coming messianic age, where the wolf and the lamb lie together and \"the fatling\" dwells with the lion (<a class=\"ref\" data-ref=\"Isaiah 11:6\">Isaiah 11:6</a>) — an image of cosmic peace in which the natural order of predation is overturned. Ezekiel 39:18 uses fatlings in an inverted feast of judgment. In Jesus's parable of the prodigal son, the father calls for the \"fatted calf\" to be killed at his son's return (Luke 15:23), and in the parable of the great banquet the king prepares his fatlings (\"oxen and fatlings,\" <a class=\"ref\" data-ref=\"Matthew 22:4\">Matthew 22:4</a>) for the feast. The fatling thus serves as a marker of the highest celebration and most generous hospitality.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fatling"},
  "key_refs": ["2 Samuel 6:13", "Isaiah 11:6", "Matthew 22:4"]
},
"fear-of-the-lord-the": {
  "id": "fear-of-the-lord-the", "term": "Fear of the Lord, The", "category": "concepts",
  "intro": "<p>The fear of the Lord is a central Old Testament concept describing the foundational disposition of true piety toward God. It is not mere terror but a reverential awe that combines recognition of God's holiness and power with love, trust, and devotion. \"The fear of the LORD is the beginning of wisdom\" (<a class=\"ref\" data-ref=\"Proverbs 1:7\">Proverbs 1:7</a>; Psalm 111:10) places it at the foundation of all genuine understanding; Job 28:28 identifies it as the essence of wisdom itself.</p><p>This fear is distinguished in the Old Testament as a covenant disposition: it is conjoined with love and hope (Psalm 147:11), issues in obedience (Deuteronomy 10:12-13), and provides deliverance (Psalm 34:7). The Psalms repeatedly celebrate it as the orientation of the righteous (<a class=\"ref\" data-ref=\"Psalms 19:9\">Psalm 19:9</a> identifies \"the fear of the LORD\" with the law itself — clean, enduring, true). It stands in contrast to the presumption of the wicked (Psalm 36:1). In the New Testament, the concept is subsumed under devotion to God the Father and carries through in phrases such as \"fearing God\" in Acts and the Epistles, where it describes Gentiles drawn to the Jewish synagogue as well as the character of genuine believers (Acts 10:2; 2 Corinthians 7:1).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fear-of-the-lord-the"},
  "key_refs": ["Proverbs 1:7", "Job 28:28", "Psalms 19:9", "Deuteronomy 10:12"]
},
"feast": {
  "id": "feast", "term": "Feast", "category": "concepts",
  "intro": "<p>Feast (<em>mishteh</em>, <em>chag</em> in Hebrew; <em>deipnon</em> in Greek) encompasses both the ordinary social banquet and the great annual religious festivals of Israel. Feasts in their social dimension marked hospitality (<a class=\"ref\" data-ref=\"Genesis 19:3\">Genesis 19:3</a>; <a class=\"ref\" data-ref=\"2 Samuel 3:20\">2 Samuel 3:20</a>), family celebrations (Genesis 21:8; Job 1:4), birthdays (Genesis 40:20), marriage (Judges 14:10), and the conclusion of covenants (Genesis 26:30). They were expressions of joy, abundance, and communal solidarity.</p><p>The religious feasts of Israel — the three great pilgrimage festivals (Passover/Unleavened Bread, Pentecost, Tabernacles) and the Day of Atonement — were divinely instituted occasions for national gathering, sacrifice, and covenant renewal. Jesus attended and taught at these festivals; his final Passover became the Last Supper, the institution of the new covenant. In the New Testament the great feast imagery becomes eschatological: the parable of the great banquet (Luke 14) and the marriage supper of the Lamb (Revelation 19:9) present the consummation of redemption as the ultimate feast — a celebration of divine abundance and intimate fellowship surpassing all earthly feasts.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "feast"},
  "key_refs": ["Genesis 19:3", "2 Samuel 3:20", "Luke 15:23", "Revelation 19:9"]
},
"felix": {
  "id": "felix", "term": "Felix", "category": "people",
  "intro": "<p>Felix (meaning <em>happy</em> or <em>prosperous</em>) was the Roman procurator of Judea who presided over Paul's imprisonment in Caesarea for approximately two years (c. A.D. 57–59). His full name was Marcus Antonius Felix; he was a freedman who rose to the governorship through the influence of his brother Pallas at the court of Emperor Claudius. The Roman historian Tacitus described him as practicing \"every kind of cruelty and lust\" with the authority of a king but the instincts of a slave.</p><p>Paul's hearing before Felix is recorded in <a class=\"ref\" data-ref=\"Acts 24:25\">Acts 24</a>. When Paul reasoned before him about \"righteousness, self-control, and the judgment to come,\" Felix trembled and dismissed him, saying \"Go away for now; when I have an opportunity I will summon you.\" Luke notes that Felix hoped Paul would offer him a bribe, which explains his repeated summonings. When Festus succeeded Felix as procurator, Felix left Paul imprisoned to curry favor with the Jewish leaders — a decision that prolonged Paul's captivity and eventually resulted in his appeal to Caesar.</p>",
  "hitchcock_meaning": "happy, prosperous",
  "source_ids": {"easton": "felix", "smith": "felix"},
  "key_refs": ["Acts 24:25", "Acts 24:27"]
},
"fellowship": {
  "id": "fellowship", "term": "Fellowship", "category": "concepts",
  "intro": "<p>Fellowship (<em>koinonia</em> in Greek; related to <em>koinos</em>, \"common\") is a central New Testament concept denoting the shared life of believers with God and with one another through the Holy Spirit. Its primary dimension is vertical: fellowship with God consists in knowing his will (<a class=\"ref\" data-ref=\"Job 22:21\">Job 22:21</a>), agreement with his purposes (Amos 3:2), mutual love, and participation in the divine life (1 John 1:3 — fellowship \"with the Father and with his Son Jesus Christ\").</p><p>The horizontal dimension — fellowship among believers — flows necessarily from the vertical. Paul's \"the fellowship of the Holy Spirit\" (2 Corinthians 13:14) and the Jerusalem church's devotion to \"the apostles' teaching and the fellowship\" (Acts 2:42) establish <em>koinonia</em> as a constitutive mark of the Christian community. In practical terms, fellowship involved shared prayer, worship, teaching, the Lord's Supper, and economic sharing with those in need (Romans 15:26 uses <em>koinonia</em> for the financial collection for Jerusalem). First John's epistolary argument grounds authentic fellowship in walking in the light, confession of sin, and love of brothers — with no room for fellowship between light and darkness (<a class=\"ref\" data-ref=\"Romans 8\">1 John 1:6-7</a>).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fellowship", "isbe": "fellowship"},
  "key_refs": ["Job 22:21", "John 17:3", "Acts 2:42", "1 John 1:3"]
},
"fence": {
  "id": "fence", "term": "Fence", "category": "concepts",
  "intro": "<p>Fence (<em>gader</em> in Hebrew) refers to the dry-stone walls or thorn-hedge enclosures used throughout ancient Palestine to protect vineyards, gardens, sheepfolds, and cultivated land from animals and intruders. Such walls were typically built without mortar from the stones cleared from the fields themselves. Their partial or complete collapse was common and is used in Scripture as a metaphor for vulnerability and ruin.</p><p>Numbers 22:24 pictures a narrow vineyard path walled on both sides (<a class=\"ref\" data-ref=\"Numbers 22:24\">Numbers 22:24</a>). The Psalms use fence imagery to describe siege conditions — \"Are you all attacking a man as if he were a leaning fence or a tottering wall?\" (<a class=\"ref\" data-ref=\"Psalms 62:3\">Psalm 62:3</a>). Isaiah 5:5 employs the image of God removing the hedge and breaking down the wall of his vineyard as a symbol of judgment on unfaithful Israel (<a class=\"ref\" data-ref=\"Psalms 80:12\">Psalm 80:12</a>). Ecclesiastes 10:8 notes the danger of breaking through a hedge — one who does so \"may be bitten by a snake,\" a proverb about the hazards of undermining established boundaries.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fence", "isbe": "fence"},
  "key_refs": ["Numbers 22:24", "Psalms 62:3", "Psalms 80:12", "Isaiah 5:5"]
},
"fenced-cities": {
  "id": "fenced-cities", "term": "Fenced Cities", "category": "concepts",
  "intro": "<p>Fenced cities (or \"fortified cities\") were walled urban centers that provided refuge and defense for the surrounding population in times of war. In ancient Palestine three types of settlements existed: walled cities, unwalled villages, and villages with towers or castles (1 Chronicles 27:25). A fenced city's defining feature was its surrounding wall of stone, sometimes supplemented by a moat, towers, and gates. Solomon undertook extensive construction of fortified cities throughout his kingdom as part of a regional defense network (1 Kings 9:15-19).</p><p>The fortification of cities was a constant feature of Israelite and Judahite strategy, and the prophets frequently reference them. Jeremiah 31:38-40 envisions Jerusalem's restoration with its walls rebuilt; Nehemiah 3 and 12 describe the rebuilding of Jerusalem's walls under Persian authorization. Militarily, fenced cities could be reduced only by prolonged siege, a fact that shapes the siege warfare accounts throughout Kings and Chronicles. The inability of Judah's fenced cities to withstand Nebuchadnezzar was understood as divine judgment (<a class=\"ref\" data-ref=\"Jeremiah 31:38\">Jeremiah 1:15</a>).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fenced-cities", "smith": "fenced-cities"},
  "key_refs": ["1 Chronicles 27:25", "Jeremiah 31:38", "Nehemiah 3:1"]
},
"ferret": {
  "id": "ferret", "term": "Ferret", "category": "concepts",
  "intro": "<p>Ferret appears in the Authorized Version of Leviticus 11:30 as one of the small unclean creeping things prohibited for consumption by the Mosaic dietary laws. The Hebrew word rendered \"ferret\" (<em>anaqah</em>, meaning a cry or groan) is of uncertain identification. The Revised Version renders it \"gecko,\" following the interpretation that the term refers to a small lizard — specifically the Lacerta gecko or a similar species of the Gekkonidae family, whose distinctive cry gives it its Hebrew name.</p><p>Most modern translations and commentators favor \"gecko\" over \"ferret,\" as the true ferret (<em>Mustela putorius furo</em>) was likely not native to ancient Palestine. The gecko, however, was common throughout the region and was known for the sound it makes. Whatever the precise identification, the prohibition in Leviticus 11 places the animal among the \"creeping things that creep on the ground\" regarded as ceremonially unclean — a category that shaped Israelite purity practice in daily life.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "ferret", "smith": "ferret"},
  "key_refs": ["Leviticus 11:30"]
},
"ferry-boat": {
  "id": "ferry-boat", "term": "Ferry Boat", "category": "concepts",
  "intro": "<p>Ferry boat appears in <a class=\"ref\" data-ref=\"2 Samuel 19:18\">2 Samuel 19:18</a> in the account of David's return to Jerusalem after Absalom's rebellion, when the men of Judah used a crossing vessel to bring the king's household and his followers over the Jordan River. The Hebrew word (<em>abara</em>) describes a kind of flat-bottomed boat or raft used to transport people and goods across the river at the numerous fords of the Jordan.</p><p>Isaiah 18:2 references vessels of papyrus (\"swift messengers\" in \"vessels of bulrushes\") used for river travel, giving a sense of the light reed-bundle boats common in the region. River crossings were strategically significant in biblical history: control of the Jordan fords gave military advantage in several engagements (Judges 3:28; 12:5-6). The ferry boat of 2 Samuel 19 captures an intimate domestic moment — the restoration of the king's household — amid the political drama of David's return to power.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "ferry-boat", "isbe": "ferry-boat"},
  "key_refs": ["2 Samuel 19:18", "Isaiah 18:2"]
},
"festivals-religious": {
  "id": "festivals-religious", "term": "Festivals, Religious", "category": "concepts",
  "intro": "<p>The religious festivals of Israel were divinely instituted occasions for communal worship, sacrifice, and covenant renewal, structured around the agricultural and sacred calendar. Leviticus 23 provides the canonical calendar: the weekly Sabbath, Passover and Unleavened Bread (Nisan 14–21), Firstfruits, the Feast of Weeks/Pentecost (fifty days after Firstfruits), the Feast of Trumpets (Tishri 1), the Day of Atonement (Tishri 10), and the Feast of Tabernacles/Booths (Tishri 15–21). The three pilgrimage festivals — Passover, Weeks, and Tabernacles — required all adult male Israelites to appear before the LORD at the central sanctuary (Deuteronomy 16:16).</p><p>The festivals were multi-layered: they commemorated historical redemptive events (Passover the exodus; Tabernacles the wilderness wandering), aligned with the harvest calendar (Firstfruits, Weeks, Tabernacles), and enacted the sacrificial system's rhythms (daily, monthly, and annual offerings, Numbers 28–29). The New Testament interprets these festivals typologically: Christ is the Passover Lamb (1 Corinthians 5:7), the firstfruits of the resurrection (1 Corinthians 15:20), and Pentecost becomes the occasion of the Spirit's coming (Acts 2). The letter to the Hebrews shows Christ as the fulfillment of the Day of Atonement's high-priestly ritual.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "festivals-religious"},
  "key_refs": ["Leviticus 23", "Numbers 28:1", "1 Corinthians 5:7", "Acts 2:1"]
},
"festus-porcius": {
  "id": "festus-porcius", "term": "Festus, Porcius", "category": "people",
  "intro": "<p>Porcius Festus was the Roman procurator of Judea who succeeded Felix, taking office around A.D. 59–60 (<a class=\"ref\" data-ref=\"Acts 24:27\">Acts 24:27</a>). His tenure was brief — he died in office around A.D. 62 — but historically significant for both Judea and Paul. Shortly after arriving in his province, Festus traveled from Caesarea to Jerusalem, where the Jewish leaders pressed him to have Paul brought there for trial (planning an ambush), but Festus insisted Paul would be heard at Caesarea.</p><p>The climactic hearing of Acts 25–26 unfolds under Festus: Paul's defense before Festus and King Agrippa II ends with Agrippa's famous near-persuasion (Acts 26:28) and his assessment that Paul could have been released had he not appealed to Caesar (<a class=\"ref\" data-ref=\"Acts 25:11\">Acts 25:11</a>). Festus's verdict — \"This man is doing nothing to deserve death or imprisonment\" (<a class=\"ref\" data-ref=\"Acts 25:12\">Acts 25:25</a>) — is one of several such declarations of Paul's innocence in Acts, paralleling the repeated declarations of Jesus's innocence before Pilate. Josephus records Festus as a generally competent administrator who confronted Sicarii and false prophets in Judea.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "festus-porcius", "smith": "festus-porcius", "isbe": "festus-porcius"},
  "key_refs": ["Acts 24:27", "Acts 25:11", "Acts 25:12", "Acts 26:28"]
},
"fever": {
  "id": "fever", "term": "Fever", "category": "concepts",
  "intro": "<p>Fever appears in both the Old and New Testaments as a common affliction and, in the Mosaic law, as one of the covenant curses that would attend Israel's disobedience: \"The LORD will strike you with wasting disease and with fever, inflammation and fiery heat\" (<a class=\"ref\" data-ref=\"Deuteronomy 28:22\">Deuteronomy 28:22</a>). The Hebrew term connotes a burning heat. In the ancient world, fevers were poorly understood, often fatal, and carried theological as well as medical significance.</p><p>The New Testament records several notable fever healings. Jesus healed Peter's mother-in-law of a great fever at Capernaum (<a class=\"ref\" data-ref=\"Matthew 8:14\">Matthew 8:14</a>; Mark 1:30; Luke 4:38-39), rebuking the fever as he would a demon — a detail that points to his authority over disease as part of his kingdom inauguration. The royal official's son whose fever broke \"at the seventh hour\" on Jesus's word (<a class=\"ref\" data-ref=\"John 4:52\">John 4:52</a>) and Paul's healing of Publius's father from fever and dysentery on Malta (<a class=\"ref\" data-ref=\"Acts 28:8\">Acts 28:8</a>) extend this pattern across both Gospels and Acts.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fever", "isbe": "fever"},
  "key_refs": ["Deuteronomy 28:22", "Matthew 8:14", "John 4:52", "Acts 28:8"]
},
"field": {
  "id": "field", "term": "Field", "category": "concepts",
  "intro": "<p>Field (<em>sadeh</em> in Hebrew) denotes cultivated or pastoral land, typically unenclosed, as distinct from the walled city or the enclosed garden. It is one of the most common landscape terms in the Old Testament, appearing in virtually every genre. Fields were the primary site of Israelite agricultural labor — plowing, sowing, and harvest — and of pastoralism, where flocks grazed and shepherds kept watch.</p><p>The field appears throughout Scripture in memorable scenes: Cain killed Abel \"in the field\" (Genesis 4:8); Boaz's field at Bethlehem was where Ruth gleaned (Ruth 2); Naboth's vineyard-field was the occasion of Ahab's injustice (1 Kings 21); and the \"field of blood\" (Aceldama) was purchased with Judas's betrayal money (Acts 1:19). In Jesus's teaching, the field is the world in which the kingdom seed is sown (Matthew 13) and in which hidden treasure awaits discovery (Matthew 13:44). The parable of the prodigal son places his destitution in the field — feeding pigs — as the nadir of his descent.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "field", "smith": "field"},
  "key_refs": ["Genesis 29:2", "Ruth 2:2", "Matthew 13:24", "Matthew 13:44"]
},
"fig": {
  "id": "fig", "term": "Fig", "category": "concepts",
  "intro": "<p>The fig (<em>te'enah</em> in Hebrew; <em>suke</em> in Greek) was one of the most important food plants of ancient Palestine and one of the seven species that characterized the goodness of the Promised Land (Deuteronomy 8:8). Fig trees produced two annual crops — an early crop of large figs in June and a main crop of smaller figs from August through October — and their large leaves, used by Adam and Eve after the fall (<a class=\"ref\" data-ref=\"Genesis 3:7\">Genesis 3:7</a>), are among the first natural details recorded in Scripture.</p><p>\"Each man under his own vine and fig tree\" became the proverbial image of peaceful prosperity in Israel (1 Kings 4:25; Micah 4:4; Zechariah 3:10), and the withering of the fig tree was a sign of judgment (Joel 1:7, 12; Hosea 9:10). Jesus's cursing of the barren fig tree (Matthew 21:18-22; Mark 11:12-25) bracketing the temple cleansing is widely understood as a symbolic enacted judgment on unfruitful Israel, while the fig tree's budding in the Olivet Discourse serves as a sign of the approaching summer of the kingdom (<a class=\"ref\" data-ref=\"Micah 4:4\">Matthew 24:32</a>).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fig"},
  "key_refs": ["Genesis 3:7", "Deuteronomy 8:8", "1 Kings 4:25", "Micah 4:4"]
},
"fillets": {
  "id": "fillets", "term": "Fillets", "category": "concepts",
  "intro": "<p>Fillets (Hebrew <em>hashukum</em>, \"joinings\") refers to the connecting rods or bands used in the construction of the tabernacle court to join the tops of the pillars together and support the linen curtain. They are mentioned in Exodus 27:17, 38:17, and 38:28 in the detailed descriptions of the tabernacle furnishings. According to these passages, the fillets of the pillars in the outer court were made of silver, and the hooks on which the curtains hung were similarly silver.</p><p>The term appears only in these tabernacle specifications and is essentially a technical architectural term for a structural element. The precision with which the tabernacle dimensions, materials, and fittings are described in Exodus 25–40 reflects the divine care for the details of Israel's formal worship — every element of the structure that housed the divine presence was specified by God to Moses on Mount Sinai. The silver fillets thus contributed to the overall effect of the outer court's barrier between the holy and the common.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fillets"},
  "key_refs": ["Exodus 27:17", "Exodus 38:17", "Exodus 38:28"]
},
"finer": {
  "id": "finer", "term": "Finer", "category": "concepts",
  "intro": "<p>Finer (Hebrew <em>tsoreph</em>) denotes a metalworker who refines or purifies precious metals — silver and gold — by melting them and removing impurities. The same Hebrew word is rendered \"founder\" in Judges 17:4 (where Micah's silver is cast into an image) and \"goldsmith\" in Isaiah 41:7. The craft of refining metals was well established in ancient Israel and the surrounding cultures.</p><p>The refiner's process became a significant biblical metaphor for divine purification. Proverbs 25:4 uses the image of removing dross from silver to describe the purification that results when wicked men are removed from a king's presence (<a class=\"ref\" data-ref=\"Proverbs 25:4\">Proverbs 25:4</a>). The fining pot (Proverbs 17:3; 27:21) tests silver as God tests hearts. Malachi 3:2-3 describes the coming of the Lord's messenger in terms of the refiner's fire: \"He will sit as a refiner and purifier of silver; he will purify the Levites and refine them like gold and silver.\" The image consistently represents a painful but productive process of purification that removes what is false and preserves what is genuine.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "finer"},
  "key_refs": ["Proverbs 25:4", "Judges 17:4", "Isaiah 41:7", "Malachi 3:3"]
},
"fining-pot": {
  "id": "fining-pot", "term": "Fining Pot", "category": "concepts",
  "intro": "<p>The fining pot (Hebrew <em>matsreph</em>) is the crucible used by metalworkers to melt and purify silver and gold, burning off dross and impurities at high heat. It appears in two proverbs: \"The fining pot is for silver, and the furnace is for gold, but the LORD tests hearts\" (<a class=\"ref\" data-ref=\"Proverbs 17:3\">Proverbs 17:3</a>); and \"The fining pot is for silver, and the furnace is for gold, and a man is tested by his praise\" (<a class=\"ref\" data-ref=\"Proverbs 27:21\">Proverbs 27:21</a>).</p><p>Both proverbs draw an analogy between the metallurgist's testing process and the way human character is revealed under pressure or scrutiny. Just as the crucible reveals the purity or impurity of metal, trials, adversity, and the response to flattery reveal the true character of a person. The theological point — that the LORD tests hearts as the refiner tests metal — recurs throughout the wisdom literature and prophets (Psalm 66:10; Zechariah 13:9; Isaiah 48:10), establishing divine testing as a purposeful and ultimately purifying process.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fining-pot"},
  "key_refs": ["Proverbs 17:3", "Proverbs 27:21", "Psalm 66:10"]
},
"fir": {
  "id": "fir", "term": "Fir", "category": "concepts",
  "intro": "<p>Fir (Hebrew <em>berosh</em>) is the uniform rendering of the Authorized Version for a tall, stately evergreen tree that featured prominently in Phoenician trade and Israelite construction. The Revised Version and modern scholarship tend to identify <em>berosh</em> with the cypress (<em>Cupressus sempervirens</em>) rather than the fir, though some passages may refer to other conifers. Lebanon's forests of cedar and <em>berosh</em> were among the most valuable timber resources of the ancient world.</p><p>King Hiram of Tyre supplied both cedar and fir/cypress timber to Solomon for the construction of the temple (1 Kings 5:8, 10) and the royal palace. The wood was used for the temple floors, doors, and panels (1 Kings 6:15, 34; 9:11). Its height and stature made the fir a symbol of Assyrian power in Ezekiel 31 and of eschatological restoration in Isaiah 41:19 and 55:13. The instrument on which David played before the ark was made of fir/cypress wood (<a class=\"ref\" data-ref=\"2 Samuel 6:5\">2 Samuel 6:5</a>), suggesting fine craftsmanship.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fir", "smith": "fir"},
  "key_refs": ["2 Samuel 6:5", "1 Kings 5:8", "Isaiah 55:13"]
},
"fire": {
  "id": "fire", "term": "Fire", "category": "concepts",
  "intro": "<p>Fire in Scripture carries multiple theological dimensions simultaneously. As the medium of sacrifice, fire was the means by which offerings ascended to God: Noah's post-flood sacrifice (<a class=\"ref\" data-ref=\"Genesis 8:20\">Genesis 8:20</a>), the altar of burnt offering, and the law's requirement that the altar fire burn continually (Leviticus 6:9) all ground fire in Israel's sacrificial system. Critically, the original fire on the tabernacle altar was kindled by God himself (<a class=\"ref\" data-ref=\"2 Chronicles 7:1\">Leviticus 9:24; 2 Chronicles 7:1</a>) — a divine authorization that made unauthorized \"strange fire\" an act of sacrilege (Leviticus 10:1-2).</p><p>Beyond the sacrificial, fire is the preeminent symbol of God's presence, holiness, and judgment. The burning bush that was not consumed (Exodus 3:2), the pillar of fire in the wilderness, the fire of Sinai (Deuteronomy 4:11-12), and Elijah's contest at Carmel all express God's active presence in fire. Hebrews 12:29 summarizes: \"our God is a consuming fire.\" The New Testament extends fire imagery to the Holy Spirit's coming (Acts 2:3 — tongues of fire), purifying discipline (1 Corinthians 3:13-15), and eschatological judgment (Revelation 20:14).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fire", "smith": "fire", "isbe": "fire"},
  "key_refs": ["Genesis 8:20", "Leviticus 6:9", "2 Chronicles 7:1", "Hebrews 12:29"]
},
"firebrand": {
  "id": "firebrand", "term": "Firebrand", "category": "concepts",
  "intro": "<p>Firebrand is an English term used in the Authorized Version to render several distinct Hebrew words describing burning or charred sticks. In Isaiah 7:4 and Zechariah 3:2, the word (<em>'ud</em>) refers to a smoldering, charred brand — the image in Zechariah 3:2 being particularly striking: Joshua the high priest is described as \"a burning stick snatched from the fire,\" a metaphor for miraculous deliverance from destruction.</p><p>In Judges 15:4, the Hebrew word (<em>lappid</em>, a torch or flame) describes the burning brands that Samson tied to foxes' tails to destroy the Philistines' grain fields — an act of revenge that escalated into broader warfare. In Proverbs 26:18, a reckless man who deceives his neighbor is compared to \"a madman who throws firebrands, arrows, and death\" (<a class=\"ref\" data-ref=\"Proverbs 26:18\">Proverbs 26:18</a>) — a portrait of destructive irresponsibility. The image of Amos 4:11, where Israel is compared to \"a burning stick plucked from the burning,\" echoes Zechariah's language of barely-escaped catastrophe.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "firebrand"},
  "key_refs": ["Isaiah 7:4", "Amos 4:11", "Zechariah 3:2", "Judges 15:4"]
},
"firepan": {
  "id": "firepan", "term": "Firepan", "category": "concepts",
  "intro": "<p>Firepan refers to a vessel used in the tabernacle and temple for carrying burning coals or handling the altar fire. The same Hebrew word (<em>machtah</em>) is rendered in different contexts as \"firepan\" (Exodus 27:3; 38:3), \"snuff-dish\" (Exodus 25:38; 37:23 — for removing burnt lampwick from the golden lampstand), and \"censer\" (Leviticus 10:1; 16:12 — for carrying incense coals before the Lord).</p><p>The firepan was thus a multi-purpose vessel of the sanctuary service. The censers of the tabernacle were made of bronze as part of the altar's equipment (<a class=\"ref\" data-ref=\"Exodus 27:3\">Exodus 27:3</a>; 38:3). The incident of Nadab and Abihu (Leviticus 10:1), who brought \"unauthorized fire\" in their censers before the LORD, underscores the firepan's association with priestly approach to God's holiness. Solomon's temple contained golden firepans among its furnishings (1 Kings 7:50; 2 Kings 25:15).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "firepan", "smith": "firepan"},
  "key_refs": ["Exodus 27:3", "Exodus 25:38", "Leviticus 10:1", "Leviticus 16:12"]
},
"firkin": {
  "id": "firkin", "term": "Firkin", "category": "concepts",
  "intro": "<p>Firkin is an archaic English measure used in the Authorized Version for the Greek <em>metretes</em>, which appears only in <a class=\"ref\" data-ref=\"John 2:6\">John 2:6</a> in the account of the wedding at Cana. The Attic <em>metretes</em> was equivalent to the Hebrew <em>bath</em>, a liquid measure of approximately 8 to 9 gallons. The six stone water jars at Cana each held two or three firkins (metretes), meaning each jar contained roughly 16 to 27 gallons.</p><p>The significance of the measurement in John 2 is in the abundance it implies: the total volume of water transformed into wine was approximately 120 to 180 gallons — an extravagant quantity that exceeds what could be consumed at any ordinary wedding feast. This superabundance is characteristic of Jesus's miracle-signs in John's Gospel, which regularly employ excess as a marker of divine generosity: the twelve baskets of leftover bread, the 153 large fish. The firkin/metretes thus serves to calibrate the miracle's scale.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "firkin", "smith": "firkin"},
  "key_refs": ["John 2:6"]
},
"firmament": {
  "id": "firmament", "term": "Firmament", "category": "concepts",
  "intro": "<p>Firmament (Latin <em>firmamentum</em>, the Vulgate's rendering of the Hebrew <em>raqia'</em>) refers to the expanse or vault of the sky described in the creation account of Genesis 1. The Hebrew <em>raqia'</em> derives from a verb meaning \"to spread out\" or \"to beat flat\" and denotes an expanse — not necessarily a solid dome, despite later interpretive traditions. God created the firmament on the second day to divide the waters above from the waters below (<a class=\"ref\" data-ref=\"Genesis 1:7\">Genesis 1:7</a>), establishing the conditions for a habitable earth.</p><p>The firmament is the space in which the heavenly bodies are set (<a class=\"ref\" data-ref=\"Genesis 1:14\">Genesis 1:14-18</a>) and in which birds fly (Genesis 1:20). The \"windows of heaven\" opened in the flood refer to the reservoirs above the firmament releasing their waters (<a class=\"ref\" data-ref=\"Genesis 7:11\">Genesis 7:11</a>). Psalm 148:4 calls for praise from \"the highest heavens\" and \"the waters above the skies.\" The \"magnificent firmament\" (<em>stereoma</em> in the Septuagint) became associated with God's glory in Ezekiel 1:22-26 and the dazzling brightness of the wise who \"shall shine like the firmament\" (Daniel 12:3).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "firmament", "smith": "firmament", "isbe": "firmament"},
  "key_refs": ["Genesis 1:7", "Genesis 1:14", "Genesis 7:11", "Psalms 148:4"]
},
"first-born": {
  "id": "first-born", "term": "First-born", "category": "concepts",
  "intro": "<p>The first-born son held a position of special privilege and responsibility in ancient Israelite society. By birthright, he received a double portion of the inheritance (<a class=\"ref\" data-ref=\"Deuteronomy 21:17\">Deuteronomy 21:17</a>) and was typically regarded as heir of family leadership. The prominence of the first-born in the patriarchal narratives is striking precisely because God repeatedly overturns the expectation: Ishmael gives way to Isaac, Esau to Jacob (<a class=\"ref\" data-ref=\"Genesis 25:23\">Genesis 25:23</a>), and Manasseh to Ephraim — establishing divine election as transcending natural order.</p><p>The theological weight of the first-born is heightened by the Exodus. God claims all first-born of Israel as his own — sanctified by the Passover in which he struck the first-born of Egypt and spared Israel's (Exodus 13:2, 14-16). The Levites were set apart as substitutes for the first-born of all Israel (Numbers 3:11-13), and all other first-born males required redemption by payment of five shekels (Numbers 18:15-16). The title \"first-born\" is applied theologically to Israel as God's son (Exodus 4:22), to the Davidic king (Psalm 89:27), and supremely in the New Testament to Christ as the first-born over all creation and first-born from the dead (Colossians 1:15, 18; Hebrews 12:23).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "first-born", "smith": "first-born", "isbe": "first-born"},
  "key_refs": ["Deuteronomy 21:17", "Genesis 25:23", "Exodus 13:2", "Colossians 1:15"]
},
"first-born-redemption-of": {
  "id": "first-born-redemption-of", "term": "First-born, Redemption of", "category": "concepts",
  "intro": "<p>The redemption of the first-born was a Mosaic ordinance requiring that all first-born males — both human and animal — be presented to the LORD as belonging to him, following the Passover event in which God struck Egypt's first-born and spared Israel's. First-born clean animals were sacrificed; first-born donkeys (unclean) were redeemed with a lamb or had their necks broken; and all first-born male children were redeemed by payment of five silver shekels to the priests (Numbers 18:15-16; <a class=\"ref\" data-ref=\"Exodus 13:12\">Exodus 13:12</a>; <a class=\"ref\" data-ref=\"Exodus 22:29\">Exodus 22:29</a>).</p><p>The theological rationale was memorial and covenantal: every first-born belonged to God because he had spared Israel's first-born in Egypt. When the Levites were consecrated to full-time priestly service (<a class=\"ref\" data-ref=\"Numbers 3:11\">Numbers 3:11</a>), they were accepted as substitutes for all the first-born of Israel, and the small numerical surplus of Israelite first-born over Levites (273) was resolved by the five-shekel redemption payment. Luke 2:22-24 records that Jesus, as the first-born son of Mary, was presented and redeemed at the temple according to this law — embedding the Son of God within the Mosaic ritual system he would fulfill.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "first-born-redemption-of"},
  "key_refs": ["Numbers 3:11", "Exodus 13:12", "Exodus 22:29", "Numbers 18:15"]
},
"first-born-sanctification-of-the": {
  "id": "first-born-sanctification-of-the", "term": "First-born, Sanctification of the", "category": "concepts",
  "intro": "<p>The sanctification of the first-born is closely related to but distinct from their redemption. All first-born males of both humans and animals were declared holy to the LORD — set apart as his special possession — on the basis of the Passover event. This sanctification established a prior claim that God held over the first-born, a claim that redemption payments acknowledged rather than canceled.</p><p>The principle appears first in God's demand on the first-born of Israel in Egypt (Exodus 11:4-5; 13:2): by striking all first-born of Egypt and passing over Israel's, God demonstrated his ownership of life and his covenantal protection of his people. The first-born thus bore a kind of sacred status — set apart, belonging to God — that the rest of Israel did not share in the same way. Abel's offering of the \"firstlings\" of his flock (<a class=\"ref\" data-ref=\"Genesis 4:4\">Genesis 4:4</a>) is read in this light as an anticipation of the principle, offering to God what was most sacred. The Levites' service as substitutes for the sanctified first-born of all Israel completed the institutionalization of this principle in the Mosaic system.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "first-born-sanctification-of-the"},
  "key_refs": ["Exodus 13:2", "Exodus 22:29", "Numbers 3:45", "Genesis 4:4"]
},
"first-fruits": {
  "id": "first-fruits", "term": "First-fruits", "category": "concepts",
  "intro": "<p>First-fruits (<em>bikkurim</em> in Hebrew) were the initial portion of each crop harvest, presented to God before the rest could be used. The offering of first-fruits expressed acknowledgment that the land and its produce belonged to God — Israel's harvests were gifts from him, not merely the product of human labor. The Mosaic law specified several first-fruit observances: the offering of the first sheaf of barley at Passover season (the \"wave sheaf,\" Leviticus 23:10-11), and the two loaves of wheat bread at Pentecost as the first-fruits of the wheat harvest (Leviticus 23:17).</p><p>Individual Israelites were also required to bring a basket of first-fruits to the sanctuary annually, accompanied by a liturgical confession summarizing Israel's redemptive history (Deuteronomy 26:1-11) — one of the earliest credal formulas in Scripture. First-fruits carried the implicit faith that the rest of the harvest would follow. Paul exploits this logic in <a class=\"ref\" data-ref=\"1 Corinthians 15:20\">1 Corinthians 15:20</a>: Christ's resurrection is the \"first-fruits\" of those who have fallen asleep, guaranteeing that the full harvest of resurrection will follow. The Holy Spirit is also called the \"first-fruits\" (Romans 8:23) — the present experience of the Spirit as the guarantee of full eschatological redemption.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "first-fruits", "isbe": "first-fruits"},
  "key_refs": ["Leviticus 23:10", "Deuteronomy 26:1", "1 Corinthians 15:20", "Romans 8:23"]
},
"fish": {
  "id": "fish", "term": "Fish", "category": "concepts",
  "intro": "<p>Fish (<em>dag</em> in Hebrew, a word connoting great fecundity) were a significant part of the diet and economy of ancient Israel, particularly in regions near the Sea of Galilee, the Jordan River, and the Mediterranean coast. Numbers 11:5 records Israel's longing in the wilderness for the fish they had eaten freely in Egypt. No individual fish species is named in the Old Testament, though Jonah's \"great fish\" (Jonah 2:1) is the most famous single fish in Scripture.</p><p>The abundance of fish in the Sea of Galilee made fishing the primary occupation of several of Jesus's disciples — Peter, Andrew, James, and John were all fishermen. Jesus called them with the promise of making them \"fishers of men\" (<a class=\"ref\" data-ref=\"Matthew 4:19\">Matthew 4:19</a>), and fish appear repeatedly in his ministry: the feeding of five thousand with five loaves and two fish, the miraculous catch, the coin found in the fish's mouth, and the post-resurrection breakfast of fish on the shore (John 21). The Greek word for fish (<em>ichthys</em>) became an early Christian acrostic and symbol, as its letters spelled out \"Jesus Christ, Son of God, Savior.\"</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fish", "smith": "fish", "isbe": "fish"},
  "key_refs": ["Genesis 9:2", "Numbers 11:22", "Jonah 2:1", "Matthew 4:19"]
},
"fish-hooks": {
  "id": "fish-hooks", "term": "Fish-hooks", "category": "concepts",
  "intro": "<p>Fish-hooks are mentioned in several prophetic passages where they appear as instruments of judgment and captivity. Amos 4:2 contains a striking oracle against the wealthy women of Samaria: \"The days are coming when they will take you away with hooks, the last of you with fishhooks\" — a vivid image of exile as being dragged helplessly away like a caught fish. Similarly, Ezekiel 29:4 applies the image to Pharaoh and Egypt, whom God will hook in the jaw and drag out of the Nile.</p><p>The image draws on the common ancient practice of leading captives with hooks through the nose or jaw, documented in Assyrian reliefs and referenced in <a class=\"ref\" data-ref=\"Isaiah 37:29\">Isaiah 37:29</a> (God putting his hook in Sennacherib's nose and turning him back). Job 41:1-2 uses fish-hooks in describing the impossibility of catching Leviathan — the chaos creature that only God can subdue. Jeremiah 16:16 uses fishermen as an image of God's agents sent to bring scattered Israel back, though in a context of judgment rather than restoration.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fish-hooks"},
  "key_refs": ["Amos 4:2", "Isaiah 37:29", "Jeremiah 16:16", "Ezekiel 29:4"]
},
"fish-pools": {
  "id": "fish-pools", "term": "Fish-pools", "category": "concepts",
  "intro": "<p>Fish-pools (or simply \"pools\") appear in the Authorized Version of Song of Solomon 7:4, where the beloved's eyes are compared to \"the fish pools in Heshbon, by the gate of Bath-rabbim.\" The Revised Version renders the term simply as \"pools,\" removing the implication that these reservoirs were specifically stocked with fish, though they may well have been.</p><p>Heshbon, the former capital of the Amorite king Sihon (Numbers 21:25-26), was known in antiquity for its water works. The comparison in the Song likens the beloved's large, calm, reflective eyes to the still, clear pools of this well-watered city. Other reservoirs and pools mentioned in connection with fish include those at Gibeon (<a class=\"ref\" data-ref=\"2 Samuel 2:13\">2 Samuel 2:13</a>), the pool of the king's garden (Nehemiah 3:15-16), and the pools at Jerusalem (Isaiah 7:3; 22:9). Artificial pools were important infrastructure in the water-scarce Palestinian landscape.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fish-pools"},
  "key_refs": ["Song of Solomon 7:4", "2 Samuel 2:13", "Isaiah 22:9"]
},
"fisher": {
  "id": "fisher", "term": "Fisher", "category": "concepts",
  "intro": "<p>Fishers were professional catchers of fish, prominent especially around the Sea of Galilee and along the Mediterranean coast. Several of Jesus's apostles were fishermen by trade before he called them: Peter and Andrew were casting a net into the sea (<a class=\"ref\" data-ref=\"Mark 1:16\">Mark 1:16-17</a>), and James and John were mending their nets in their boat with their father Zebedee when Jesus called them to follow him. Fishing in the Sea of Galilee was a substantial economic industry in the first century.</p><p>Jesus transformed the fisherman's identity into a theological vocation: \"Follow me, and I will make you fishers of men\" (<a class=\"ref\" data-ref=\"Matthew 4:19\">Matthew 4:19</a>; <a class=\"ref\" data-ref=\"Mark 1:17\">Mark 1:17</a>). This metaphor draws on the prophetic use of fishing imagery for gathering scattered people (Jeremiah 16:16; Ezekiel 47:10). The miraculous catch of 153 fish in John 21:1-14 — the post-resurrection appearance where the risen Christ directs the disciples to the catch — functions both as a sign and as a restoration of the fishing commission, now understood in its full missionary dimension.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fisher"},
  "key_refs": ["Luke 5:2", "Matthew 4:19", "Mark 1:17", "John 21:6"]
},
"fishing-the-art-of": {
  "id": "fishing-the-art-of", "term": "Fishing, the Art of", "category": "concepts",
  "intro": "<p>Fishing was practiced extensively in ancient Israel and throughout the ancient Near East, particularly on the Sea of Galilee (also called the Lake of Gennesaret or Tiberias) and along the Mediterranean coast. The techniques employed in biblical times included casting and dragging nets (the draw-net or seine net, Matthew 13:47-48; the cast net, Mark 1:16), line fishing with hooks, and the use of spears or fish-traps. The industry was large enough to support guilds and commercial operations: first-century Galilean fish were salted and exported throughout the Roman Empire from facilities at Magdala (Greek: Tarichaeae, \"salted fish\").</p><p>The gospels set much of Jesus's Galilean ministry in this fishing context. The calling of disciples from their nets (<a class=\"ref\" data-ref=\"Mark 1:16\">Mark 1:16-20</a>), the teaching from Peter's boat, the parable of the dragnet (<a class=\"ref\" data-ref=\"Matthew 13\">Matthew 13:47-50</a>), the miraculous catches, and Peter's finding a coin in a fish's mouth (Matthew 17:27) all draw on the intimate familiarity Jesus and his disciples had with this world. The art of fishing thus provided both the social context and a rich reservoir of parable material for Jesus's Galilean ministry.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fishing-the-art-of"},
  "key_refs": ["Mark 1:16", "Matthew 13:47", "John 21:6", "Luke 5:4"]
},
"fitches": {
  "id": "fitches", "term": "Fitches", "category": "concepts",
  "intro": "<p>Fitches is the Authorized Version's rendering of two distinct Hebrew plants in Isaiah and Ezekiel. In <a class=\"ref\" data-ref=\"Isaiah 28:25\">Isaiah 28:25, 27</a>, the Hebrew <em>qetsah</em> most likely refers to the <em>Nigella sativa</em> (black cumin or fennel flower), a small annual herb of the buttercup family grown across the ancient Near East for its seeds, used as a spice and condiment. Isaiah notes that it is beaten out with a staff rather than threshed with a harder instrument — an illustration of God's wisdom in calibrating judgment to what each crop can bear.</p><p>In Ezekiel 4:9, the Hebrew <em>kussemeth</em> (usually translated \"spelt\" or \"emmer\") was an inferior grain mixed with wheat, barley, and other grains in the prophet's symbolic \"siege bread.\" The passage illustrates Jerusalem's coming scarcity under siege. Both uses of \"fitches\" demonstrate the rich agricultural vocabulary of ancient Palestine and the prophets' precise observation of agricultural practice, which they deployed as a vehicle for theological instruction.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fitches", "smith": "fitches"},
  "key_refs": ["Isaiah 28:25", "Isaiah 28:27", "Ezekiel 4:9"]
},
"flag": {
  "id": "flag", "term": "Flag", "category": "concepts",
  "intro": "<p>Flag in the Authorized Version translates the Hebrew <em>achu</em> (also spelled <em>ahu</em>), an Egyptian loanword referring to aquatic vegetation — specifically reeds, rushes, or sedge grass that grow in marshy ground near water. It appears in Job 8:11 (\"Can the rush grow up without mire? can the flag grow without water?\") and in Genesis 41:2, 18, where it describes the lush reed-grass of the Nile banks in Pharaoh's dream.</p><p>Exodus 2:3, 5 uses the same or similar term (<em>suf</em>) for the reeds among which Moses's basket was hidden on the Nile — the same \"Red Sea\" (<em>yam suf</em>, \"sea of reeds\") that Israel crossed. The flag or papyrus is the Cyperus papyrus, a tall sedge that once grew abundantly in Egyptian and Palestinian marshes. In Job 8:11's botanical metaphor, the impossibility of rushes growing without water parallels the impossibility of the godless prospering without God — the point being that apparent security without a proper foundation cannot endure.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "flag", "smith": "flag"},
  "key_refs": ["Job 8:11", "Genesis 41:2", "Exodus 2:3"]
},
"flagon": {
  "id": "flagon", "term": "Flagon", "category": "concepts",
  "intro": "<p>Flagon in the Authorized Version renders the Hebrew <em>ashishah</em>, which most modern scholars identify not as a liquid container but as a cake of pressed or dried raisins. The Revised Version and most modern translations render it \"raisin cake\" — a concentrated, sweet food used both in ordinary life and in worship contexts. The \"flagons of wine\" of the older translation reflect an error; the substance was a solid cake of compressed raisins rather than a vessel of wine.</p><p>Raisin cakes appear in 2 Samuel 6:19 and 1 Chronicles 16:3 in David's distribution of food to the people after the ark's installation — a joyful communal celebration. Song of Solomon 2:5 uses them as a term of refreshment: \"Sustain me with raisin cakes, refresh me with apples, for I am sick with love.\" Hosea 3:1 warns against those who \"turn to other gods and love the sacred raisin cakes\" — a reference to the use of raisin cakes in pagan Canaanite fertility cult offerings, practices associated with Baal and Asherah worship (<a class=\"ref\" data-ref=\"Hosea 3:1\">Hosea 3:1</a>).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "flagon", "smith": "flagon"},
  "key_refs": ["2 Samuel 6:19", "1 Chronicles 16:3", "Song of Solomon 2:5", "Hosea 3:1"]
},
"flame-of-fire": {
  "id": "flame-of-fire", "term": "Flame of Fire", "category": "concepts",
  "intro": "<p>Flame of fire is the chosen biblical symbol of the holiness and transcendent presence of God. The appearance of God to Moses in the burning bush — a bush aflame but not consumed (<a class=\"ref\" data-ref=\"Exodus 3:2\">Exodus 3:2</a>) — established fire as the medium of divine self-disclosure: the fire was not destructive but holy, the ordinary transformed by the divine presence. This pattern continues throughout the Old Testament: the pillar of fire guiding Israel, the fire on Mount Sinai, and the fire that fell on Elijah's sacrifice at Carmel.</p><p>In the New Testament, the risen and exalted Christ is described in Revelation 2:18 with \"eyes like a flame of fire\" (<a class=\"ref\" data-ref=\"Revelation 2:18\">Revelation 2:18</a>) — a detail from Daniel 10:6 now applied to Christ in his glory, signifying penetrating, holy judgment. Hebrews 12:29, quoting Deuteronomy 4:24, declares \"our God is a consuming fire\" — the flame-character of divine holiness persists from Sinai to the new covenant. Theologians have understood the flame symbol to express the intense, all-consuming operation of God's holiness in relation to sin, and his self-giving, self-disclosing presence in relation to those who draw near to him.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "flame-of-fire"},
  "key_refs": ["Exodus 3:2", "Revelation 2:18", "Hebrews 12:29"]
},
"flax": {
  "id": "flax", "term": "Flax", "category": "concepts",
  "intro": "<p>Flax (<em>pishtah</em> in Hebrew, from a root meaning \"to peel\") was one of the most important fiber and oil plants of the ancient world and a significant crop in Egypt, Canaan, and throughout the Fertile Crescent. The flax plant (<em>Linum usitatissimum</em>) was harvested for its long stem fibers, which were retted (soaked), beaten, and spun into linen — the premier textile of the ancient Near East. Its seeds yielded linseed oil. The mention of flax being in blossom during the seventh Egyptian plague (<a class=\"ref\" data-ref=\"Exodus 9:31\">Exodus 9:31</a>) indicates that it was well established in Egyptian agriculture before the Exodus.</p><p>Rahab hid the Israelite spies under stalks of flax drying on her roof (<a class=\"ref\" data-ref=\"Joshua 2:6\">Joshua 2:6</a>), providing an incidental detail of Palestinian daily life. Flax was used to make the priestly garments, the temple curtains, and fine clothing. The ideal wife of Proverbs 31:13 \"works with flax,\" and Isaiah 42:3 — quoted in Matthew 12:20 — uses \"a dimly burning wick\" (flaxen wick) as an image for those whom the servant of God will not break.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "flax", "smith": "flax"},
  "key_refs": ["Exodus 9:31", "Joshua 2:6", "Isaiah 42:3"]
},
"flea": {
  "id": "flea", "term": "Flea", "category": "concepts",
  "intro": "<p>The flea appears twice in the Old Testament, both times in the mouth of David when addressing Saul during his time as a fugitive. At the cave of Adullam, David asked Saul: \"After whom is the king of Israel come out? after whom dost thou pursue? after a dead dog, after a flea\" (<a class=\"ref\" data-ref=\"1 Samuel 24:14\">1 Samuel 24:14</a>). The second instance echoes this: \"the king of Israel is come out to seek a flea\" (1 Samuel 26:20).</p><p>David's use of the flea as a self-designation is a deliberate expression of self-abasement before the king — the flea being among the smallest and most insignificant of creatures, certainly no worthy quarry for a king and his army. The irony is pointed: Israel's greatest military hero represents himself as a negligible creature to highlight the disproportionate and unjust nature of Saul's pursuit. The flea itself is the common human flea (<em>Pulex irritans</em>), abundant throughout the ancient Near East. Beyond these two references, the term has no further biblical significance.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "flea", "smith": "flea"},
  "key_refs": ["1 Samuel 24:14", "1 Samuel 26:20"]
},
"fleece": {
  "id": "fleece", "term": "Fleece", "category": "concepts",
  "intro": "<p>Fleece refers to the wool coat of a sheep, either while still on the animal or after shearing. The first-shorn fleece of each animal belonged by Mosaic law to the priests: \"The first-fruits of your grain, of your wine and oil, and the first fleece of your sheep, you shall give him\" (<a class=\"ref\" data-ref=\"Deuteronomy 18:4\">Deuteronomy 18:4</a>). Job's famous declaration of social righteousness includes clothing the poor with wool from his own flock (Job 31:20).</p><p>The most theologically memorable use of fleece in Scripture is Gideon's test (<a class=\"ref\" data-ref=\"Judges 6:37\">Judges 6:37-40</a>). Before engaging the Midianite army, Gideon twice asked God for a confirming sign: first that a fleece laid on the threshing floor would be wet with dew while the ground remained dry, then that the fleece would remain dry while the ground was wet. God patiently granted both signs, accommodating Gideon's timidity. The \"fleece\" has since become a common expression for seeking divine confirmation through a specific test — though the episode is generally read as an accommodation to Gideon's weakness rather than a commended practice.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fleece", "isbe": "fleece"},
  "key_refs": ["Deuteronomy 18:4", "Job 31:20", "Judges 6:37"]
},
"flesh": {
  "id": "flesh", "term": "Flesh", "category": "concepts",
  "intro": "<p>Flesh (<em>basar</em> in Hebrew; <em>sarx</em> in Greek) is a richly layered biblical term with at least four distinct usages. In its most basic sense it denotes a part of the body — muscle, tissue — or the whole body of a person or animal (<a class=\"ref\" data-ref=\"Genesis 2:21\">Genesis 2:21</a>; Psalm 102:5). Extended, it describes humanity as a whole in its creaturely, mortal aspect: \"all flesh\" means all living creatures, especially all human beings in their weakness and transience before God (<a class=\"ref\" data-ref=\"Genesis 6:12\">Genesis 6:12</a>; Isaiah 40:6: \"All flesh is grass\"). In a narrower social sense, \"my flesh\" means a close blood relative (Genesis 29:14).</p><p>The New Testament's use of <em>sarx</em> in Paul carries the additional and important sense of the human nature as the site of opposition to God — not the body as such, but the whole human personality oriented away from God, under the power of sin. \"Flesh\" in Romans 7–8, Galatians 5, and Ephesians 2 describes the anti-God principle in fallen human nature — \"the desires of the flesh\" opposing the Spirit. John's Gospel uses \"flesh\" differently: the incarnation is God's Word becoming flesh (<a class=\"ref\" data-ref=\"Genesis 6:12\">John 1:14</a>), taking on the full creaturely, mortal human condition — a use that stands in striking tension with the Pauline negative sense and guards both against docetism and against a purely negative evaluation of embodied humanity.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "flesh", "smith": "flesh", "isbe": "flesh"},
  "key_refs": ["Genesis 2:21", "Genesis 6:12", "Romans 8:5", "John 1:14"]
},
"flesh-hook": {
  "id": "flesh-hook", "term": "Flesh-hook", "category": "concepts",
  "intro": "<p>The flesh-hook was a many-pronged fork used in the sacrificial services of the tabernacle and temple to handle the meat of burnt offerings at the altar. The sons of Eli at Shiloh are reproved in 1 Samuel 2:13-14 for using the flesh-hook illegitimately — plunging it into the boiling pot and taking whatever it brought up as their priest's portion, instead of following the lawful procedure for priestly portions of the sacrifice.</p><p>The flesh-hooks of the tabernacle altar were made of bronze as part of the altar's standard equipment (<a class=\"ref\" data-ref=\"Exodus 27:3\">Exodus 27:3</a>; <a class=\"ref\" data-ref=\"Exodus 38:3\">Exodus 38:3</a>), and their construction was specified along with the other altar vessels: shovels, basins, and firepans. The flesh-hook was used to manage the burning sacrifice on the altar and to lift pieces of meat for proper placement. Leviticus 7:29-36 specifies the lawful priestly portions — breast and right thigh — which the flesh-hook abuse of Eli's sons violated, a sin that foreshadowed the priestly house's downfall.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "flesh-hook", "isbe": "flesh-hook"},
  "key_refs": ["1 Samuel 2:13", "Exodus 27:3", "Exodus 38:3"]
},
"flint": {
  "id": "flint", "term": "Flint", "category": "concepts",
  "intro": "<p>Flint is a hard variety of chert (a form of quartz) found abundantly in the limestone regions of Palestine, the Sinai, and throughout the wilderness territories through which Israel traveled. Its extreme hardness and ability to hold a sharp edge made it the preeminent stone-tool material for cutting instruments before iron became widely available. Flint knives were used for circumcision in the wilderness period: Joshua circumcised the Israelites with \"sharp flint knives\" at Gilgal (Joshua 5:2-3).</p><p>Flint is used in two striking metaphorical expressions. In Isaiah 50:7 — part of the third Servant Song — the Servant declares: \"I have set my face like flint, and I know I will not be put to shame\" (<a class=\"ref\" data-ref=\"Isaiah 50:7\">Isaiah 50:7</a>), describing unwavering determination in the face of suffering and opposition. Ezekiel 3:9 uses the same image when God strengthens the prophet: \"Like the hardest stone, harder than flint, I have made your forehead\" (<a class=\"ref\" data-ref=\"Ezekiel 3:9\">Ezekiel 3:9</a>). Both passages exploit flint's legendary hardness as a metaphor for resolute, divinely-given courage.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "flint", "smith": "flint"},
  "key_refs": ["Isaiah 50:7", "Ezekiel 3:9", "Joshua 5:2"]
},
"flood": {
  "id": "flood", "term": "Flood", "category": "events",
  "intro": "<p>The Flood (or Deluge) is the catastrophic event recorded in Genesis 6–9, in which God sent rising waters to cover the earth as judgment on the pervasive wickedness of the antediluvian world. The narrative describes forty days of rain and the opening of \"the windows of heaven\" and \"the fountains of the great deep\" (Genesis 7:11), resulting in waters that prevailed for 150 days and covered even the highest mountains. Only Noah, his family of eight persons, and the pairs of animals preserved in the ark survived. The ark came to rest on Ararat, and God established the Noahic covenant with the rainbow as its sign (Genesis 9).</p><p>The flood stands as the definitive biblical type of judgment and salvation by water. Peter draws this typological connection explicitly: the flood waters that judged the world also \"saved\" Noah, and this corresponds to baptism, which now saves through resurrection (<a class=\"ref\" data-ref=\"Joshua 24:2\">1 Peter 3:20-21</a>). Jesus uses the days of Noah to characterize the unsuspecting normalcy that will precede the Son of Man's return (Matthew 24:37-39). Hebrews 11:7 commends Noah's faith in building the ark in response to a divine warning about \"things not yet seen.\" The Flood narrative has parallels in Mesopotamian literature (the Atrahasis Epic and Gilgamesh Tablet XI), though the biblical account is theologically distinctive in its ethical-monotheistic framework.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "flood", "smith": "flood", "isbe": "flood"},
  "key_refs": ["Genesis 7:11", "Genesis 9:13", "Matthew 24:37", "1 Peter 3:20"]
},
"flour": {
  "id": "flour", "term": "Flour", "category": "concepts",
  "intro": "<p>Flour (<em>qemach</em> and <em>solet</em> in Hebrew — the latter denoting fine or sifted flour) was a dietary staple throughout the biblical world, produced by grinding grain between millstones. The daily grinding of grain was a household task performed by women (Matthew 24:41) or by slaves. Abraham directed Sarah to prepare \"three seahs of fine flour\" (<a class=\"ref\" data-ref=\"Genesis 18:6\">Genesis 18:6</a>) for the three divine visitors, an expression of the finest hospitality.</p><p>Fine flour played a central role in the Mosaic sacrificial system. The grain offering (<em>minchah</em>) consisted of fine wheat flour, with or without oil, frankincense, salt, and leaven (Leviticus 2). The bread of the Presence in the tabernacle was made from fine flour (Leviticus 24:5). In the economy of Israel, flour served as a medium of trade and provision: Elijah's miraculous jar of flour that did not run out during the famine (1 Kings 17:14-16) and Elisha's purifying of the deadly stew with flour (2 Kings 4:41) are among the notable flour narratives. The vision of Revelation 18:13, lamenting Babylon's fall, includes \"fine flour\" among the luxury commodities the great city will no longer import.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "flour", "smith": "flour"},
  "key_refs": ["Genesis 18:6", "Leviticus 2:1", "1 Kings 17:14", "2 Kings 4:41"]
},
"flowers": {
  "id": "flowers", "term": "Flowers", "category": "concepts",
  "intro": "<p>Flowers, though abundant in ancient Palestine — modern surveys identify some 2,600 plant species in western Syria and Palestine, with hundreds flowering — are mentioned relatively rarely in Scripture by specific name. The most celebrated are the lily (<em>shushan</em>), the rose of Sharon, and the wildflowers of the field. When specific flowers appear in the text, they often carry rich symbolic weight.</p><p>The seasonal appearance of flowers signals renewal and hope: \"The flowers appear on the earth; the time of singing is come\" (<a class=\"ref\" data-ref=\"Song of Solomon 2:12\">Song of Solomon 2:12</a>) heralds the arrival of spring. Conversely, the brevity of flowers serves as the preeminent image of human mortality and transience: \"As for man, his days are as grass: as a flower of the field, so he flourisheth. For the wind passeth over it, and it is gone\" (<a class=\"ref\" data-ref=\"Psalms 103:15\">Psalm 103:15-16</a>; Job 14:2; Isaiah 40:6-8; 1 Peter 1:24). <a class=\"ref\" data-ref=\"Matthew 6:28\">Matthew 6:28-30</a> uses the fleeting beauty of lilies to argue for trust in God's provision — if he so clothes grass that is here today and burned tomorrow, how much more will he care for his own people.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "flowers", "isbe": "flowers"},
  "key_refs": ["Song of Solomon 2:12", "Psalms 103:15", "Job 14:2", "Matthew 6:28"]
},
"flute": {
  "id": "flute", "term": "Flute", "category": "concepts",
  "intro": "<p>Flute (Aramaic <em>mashroki</em>, likely a type of pipe or reed instrument) is mentioned in Daniel 3:5, 7, 10, and 15, as one of the instruments in Nebuchadnezzar's royal orchestra commanded to sound the signal for all nations to prostrate themselves before his golden image. The flute here appears alongside the horn, pipe, lyre, harp, bagpipe, and other instruments in what is evidently a catalogue of the instruments available in the Babylonian court.</p><p>In the New Testament, <em>auletes</em> (flute player; rendered \"minstrel\" in the Authorized Version) appears in <a class=\"ref\" data-ref=\"Matthew 9:23\">Matthew 9:23-24</a>, where professional mourners — including flute players — had already gathered at the house of Jairus before Jesus arrived to raise his daughter. The flute's association with mourning (as well as rejoicing, Matthew 11:17) reflects its dual role in ancient life. The piping at weddings and funerals mentioned in Matthew 11:17 (\"We piped to you, and you did not dance; we sang a dirge, and you did not mourn\") shows the flute's centrality to both celebration and lamentation.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "flute", "smith": "flute"},
  "key_refs": ["Daniel 3:5", "Matthew 9:23", "Matthew 11:17"]
},
"fly": {
  "id": "fly", "term": "Fly", "category": "concepts",
  "intro": "<p>Fly (Hebrew <em>zebub</em>) was a significant pest in the ancient Near East, so troublesome in Syria and Phoenicia that the Canaanites had a god named Baal-zebub (\"lord of flies\") worshipped at Ekron, whose oracle Ahaziah sought in 2 Kings 1:2-16 — an act condemned by Elijah. The influence of this deity's name persisted into the New Testament as Beelzebul, applied to Satan (Matthew 12:24-27).</p><p>The fourth Egyptian plague sent by God through Moses was a plague of flies (or a swarm of insects, <em>'arob</em>) upon Egypt, while Goshen was spared (<a class=\"ref\" data-ref=\"Exodus 8:21\">Exodus 8:21</a>; Psalm 78:45; 105:31) — one of the distinguishing miracles that separated Israel from their Egyptian oppressors. The brevity and fragility of the fly is exploited in Ecclesiastes 10:1: \"Dead flies cause the ointment of the apothecary to send forth a stinking savour\" — a small thing can corrupt something valuable. Isaiah 7:18 employs flies symbolically: the LORD will \"whistle for the fly that is in the uttermost part of the rivers of Egypt\" — summoning the Egyptian armies as irresistible as a swarm of flies.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fly", "isbe": "fly"},
  "key_refs": ["Ecclesiastes 10:1", "Isaiah 7:18", "Exodus 8:21", "Psalms 78:45"]
},
"foam": {
  "id": "foam", "term": "Foam", "category": "concepts",
  "intro": "<p>Foam appears once in the Authorized Version of the Old Testament in Hosea 10:7, where Samaria's king is said to be \"cut off as the foam upon the water\" — an image of insubstantiality and swift disappearance. The Hebrew word (<em>qetseph</em>) is alternatively rendered \"chip\" or \"splinter\" by the LXX and the Revised Version margin, suggesting the image may be of floating wood-splinters rather than water-foam; but the sense in either reading is the same: the king of the northern kingdom will vanish like something that floats momentarily and is gone.</p><p>In the New Testament, foam appears in the description of the epileptic boy whom Jesus healed: the boy would \"foam at the mouth\" (<em>aphrizo</em>) during his seizures, indicating the neurological intensity of his condition (Mark 9:18, 20; Luke 9:39). The Letter of Jude 13 uses \"wild waves of the sea foaming out their shame\" as a metaphor for the character of false teachers — their lives produce nothing of value, only visible but ephemeral display that will be swept away.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "foam", "isbe": "foam"},
  "key_refs": ["Hosea 10:7", "Mark 9:18", "Jude 13"]
},
"fodder": {
  "id": "fodder", "term": "Fodder", "category": "concepts",
  "intro": "<p>Fodder (Hebrew <em>belil</em>, meaning a mixture or medley) refers to feed given to working animals — typically a mixture of grain, straw, chaff, and legumes such as wheat, barley, vetches, and lentils. The Latin <em>farrago</em> (from which the English \"farrage\" derives) describes the same type of mixed animal feed. Job 6:5 uses the donkey's braying and ox's lowing when fodder is available as analogies for the appropriateness of his complaint: \"Does a wild donkey bray when it has grass? Does an ox bellow when it has fodder?\" (<a class=\"ref\" data-ref=\"Job 6:5\">Job 6:5</a>).</p><p>Job 24:6 references those who harvest fodder in another man's field — an image of the destitution of the poor. Isaiah 30:24 describes the future prosperity of the messianic era partly in terms of agricultural abundance: working animals will eat \"salted fodder\" winnowed with a shovel and fork (<a class=\"ref\" data-ref=\"Isaiah 30:24\">Isaiah 30:24</a>). The mention of fodder thus appears consistently in contexts of subsistence, abundance, or its absence, grounding even the animals' feed in the broader covenant blessings and curses of Israel's agricultural life.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fodder", "isbe": "fodder"},
  "key_refs": ["Job 6:5", "Job 24:6", "Isaiah 30:24"]
},
"fold": {
  "id": "fold", "term": "Fold", "category": "concepts",
  "intro": "<p>Fold (Hebrew <em>naveh</em> or <em>gederah</em>) denotes an enclosure where sheep or goats are gathered for rest and protection at night, typically a stone-walled pen or a natural cave or depression used for the same purpose. Sheepfolds are mentioned throughout the Old Testament in pastoral contexts: the Transjordanian tribes built sheepfolds for their flocks when settling east of the Jordan (<a class=\"ref\" data-ref=\"Numbers 32:16\">Numbers 32:16</a>, 24, 36), and David was called from following the ewes to tend Israel (2 Samuel 7:8; Psalm 78:70-71).</p><p>Jesus's extended sheep-and-shepherd discourse in John 10 uses the fold (<em>aule</em>, courtyard) as a primary image: the true shepherd enters by the door, while the thief and robber climbs in another way. \"And there are other sheep I have, which are not of this fold: them also I must bring, and they shall hear my voice; and there shall be one fold, and one shepherd\" (John 10:16) — a statement that eschatological unity of Jew and Gentile in Christ's flock transcends the present boundaries of any single sheepfold. Isaiah 13:20 uses the abandoned fold as a picture of utter desolation.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "fold"},
  "key_refs": ["Numbers 32:16", "2 Samuel 7:8", "Isaiah 13:20", "John 10:16"]
},
"food": {
  "id": "food", "term": "Food", "category": "concepts",
  "intro": "<p>Food in Scripture encompasses both the physical sustenance of human life and a rich theological symbolism. The Creator's original grant to humanity was vegetarian: \"I give you every seed-bearing plant... they will be yours for food\" (<a class=\"ref\" data-ref=\"Genesis 1:29\">Genesis 1:29</a>). After the flood, God extended the grant to include animals: \"Everything that lives and moves will be food for you\" (Genesis 9:2-3), with the sole prohibition of blood. The Mosaic dietary laws then structured what kinds of food were clean or unclean for Israel, embedding distinctions of holiness into daily eating.</p><p>Food carries profound covenant meaning: the Passover meal memorialized redemption; the manna sustained Israel in the wilderness and became a type of the bread from heaven (John 6); and the fellowship meal (the Lord's Supper) is the defining eating event of the new covenant community. Jesus's response to the devil in Matthew 4:4 — \"Man shall not live by bread alone, but by every word that proceeds from the mouth of God\" — sets bodily food in relation to the deeper sustenance that only God provides. Colossians 2:16 and Romans 14 show the early church working through the question of whether Jewish food distinctions still applied in Christ.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "food", "smith": "food"},
  "key_refs": ["Genesis 1:29", "Genesis 9:2", "Deuteronomy 8:3", "John 6:35"]
},
"footstool": {
  "id": "footstool", "term": "Footstool", "category": "concepts",
  "intro": "<p>Footstool, in its literal sense, was a platform or step placed before a throne for the king's feet (2 Chronicles 9:18). In Israelite theology, the footstool became a significant image for God's presence and glory. The ark of the covenant was called God's footstool: David declared his desire to build a house of rest \"for the ark of the covenant of the LORD, for the footstool of our God\" (<a class=\"ref\" data-ref=\"1 Chronicles 28:2\">1 Chronicles 28:2</a>). The Psalms similarly call worshipers to prostrate themselves at God's footstool (Psalm 99:5; 132:7).</p><p>Psalm 110:1 — the most-quoted Old Testament verse in the New Testament — uses the footstool image with royal-messianic force: \"Sit at my right hand, until I make your enemies your footstool\" (<a class=\"ref\" data-ref=\"Psalms 110:1\">Psalm 110:1</a>). Jesus quotes this psalm to challenge the scribes (Matthew 22:44), and Peter applies it to the exalted Christ at Pentecost (Acts 2:35). Hebrews exploits the \"enemies as footstool\" imagery to contrast the incomplete rest of the Levitical priesthood with Christ's single, finished offering after which he \"sat down\" and \"waits for his enemies to be made a footstool for his feet\" (Hebrews 10:13).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "footstool", "isbe": "footstool"},
  "key_refs": ["1 Chronicles 28:2", "Psalms 99:5", "Psalms 110:1", "Hebrews 10:13"]
},
"forces": {
  "id": "forces", "term": "Forces", "category": "concepts",
  "intro": "<p>Forces in the Authorized Version of Isaiah 60:5, 11 translates the Hebrew <em>chayil</em> (or related terms), which in this context denotes not military forces but the wealth, resources, and abundance of the nations. The Revised Version renders the phrase \"the wealth of the nations shall come to you\" (<a class=\"ref\" data-ref=\"Isaiah 60:5\">Isaiah 60:5</a>) — a description of the eschatological pilgrimage of Gentile peoples and their resources to the restored Jerusalem.</p><p>Isaiah 60 as a whole envisions the ingathering of scattered Israel and the nations' voluntary tribute to the LORD's city: camels from Midian and Ephah, gold and frankincense from Sheba, flocks from Kedar and Nebaioth, silver and gold from Tarshish. This vision of the nations' wealth flowing into Zion reverses the pattern of conquest and tribute in which Israel's goods went to foreign powers, and it became a touchstone for New Testament hopes about the Gentile mission: the Magi's gold, frankincense, and myrrh (Matthew 2) are read in the light of this Isaianic expectation.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "forces", "isbe": "forces"},
  "key_refs": ["Isaiah 60:5", "Isaiah 60:11", "Matthew 2:11"]
},
"ford": {
  "id": "ford", "term": "Ford", "category": "places",
  "intro": "<p>A ford is a shallow crossing point in a river where people and animals can wade across. The fords of the Jordan River were numerous — perhaps fifty or more — and appear frequently in biblical narrative as strategic military and geographical features. Control of the Jordan fords gave decisive tactical advantage, as demonstrated when the Ephraimites were cut off at the fords and slaughtered by Jephthah's Gileadites after failing the shibboleth test (<a class=\"ref\" data-ref=\"Judges 12:5\">Judges 12:5-6</a>).</p><p>Ehud escaped across the Jordan fords after assassinating Eglon (<a class=\"ref\" data-ref=\"Judges 3:28\">Judges 3:28</a>); the spies sent by Joshua were sought at the fords (<a class=\"ref\" data-ref=\"Joshua 2:7\">Joshua 2:7</a>); and Jacob crossed the ford of the Jabbok in the night of his wrestling with God (<a class=\"ref\" data-ref=\"Genesis 32:22\">Genesis 32:22</a>). The fords of the Arnon are mentioned in Isaiah 16:2. The strategic importance of river crossings in an era before bridges gave ford control a military significance that repeatedly shaped the outcomes of biblical campaigns.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "ford", "isbe": "ford"},
  "key_refs": ["Joshua 2:7", "Judges 3:28", "Judges 12:5", "Genesis 32:22"]
},
"forehead": {
  "id": "forehead", "term": "Forehead", "category": "concepts",
  "intro": "<p>The forehead held special significance in both pagan and Israelite practice as a visible surface for marking identity, devotion, or status. Oriental custom included marking or coloring the forehead as a sign of dedication to a deity. In Israelite practice, the high priest wore a golden plate on his forehead inscribed \"Holy to the LORD\" (Exodus 28:36-38), and phylacteries (<em>totaphoth</em>) were to be worn \"between your eyes\" (Exodus 13:16; Deuteronomy 6:8) — a forehead marking of devotion to God's word.</p><p>Ezekiel 9:4-6 records a vision in which the righteous in Jerusalem received a mark (Hebrew <em>tav</em>, the last letter of the alphabet, shaped like a cross in ancient script) on their foreheads as a sign of preservation from divine judgment — an image that carries through into Revelation's sealing of the 144,000 (Revelation 7:3) and the mark of God's name on the foreheads of the redeemed (Revelation 22:4), set in sharp contrast to the mark of the beast received on forehead or hand by those who worship him (<a class=\"ref\" data-ref=\"Revelation 13:16\">Revelation 13:16</a>). The forehead thus becomes in the Apocalypse the ultimate site of identity and allegiance.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "forehead", "smith": "forehead"},
  "key_refs": ["Ezekiel 9:4", "Revelation 7:3", "Revelation 13:16", "Revelation 22:4"]
},
"foreigner": {
  "id": "foreigner", "term": "Foreigner", "category": "concepts",
  "intro": "<p>Foreigner (or stranger, alien) in the Old Testament encompassed several distinct categories with different legal standing. The <em>ger</em> (sojourner, resident alien) was a non-Israelite living long-term in the community — protected by Mosaic law, eligible for most religious participation, and required to observe the Sabbath. The <em>nokri</em> (foreigner, outsider) was a temporary visitor or outsider with fewer legal protections. Mosaic law consistently commanded Israel to treat the <em>ger</em> with justice and compassion, grounding the obligation in Israel's own experience as foreigners in Egypt: \"You shall not oppress a sojourner. You know the heart of a sojourner, for you were sojourners in the land of Egypt\" (<a class=\"ref\" data-ref=\"Exodus 22:21\">Exodus 22:21</a>; 23:9; Leviticus 19:33-34).</p><p>The treatment of foreigners was a significant test of Israel's covenant justice, and the prophets frequently reproach Israel for their mistreatment of the stranger alongside widows and orphans. Ruth the Moabitess is the most celebrated foreigner in the Old Testament narrative — her faithful attachment to Naomi and to Israel's God became the occasion of her entry into the messianic line. The New Testament's \"middle wall of partition\" between Jew and Gentile, abolished in Christ (Ephesians 2:14), transforms the category: in Christ there is \"neither Greek nor Jew\" (Colossians 3:11).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "foreigner", "isbe": "foreigner"},
  "key_refs": ["Exodus 22:21", "Exodus 23:9", "Leviticus 19:33", "Ephesians 2:14"]
},
"foreknowledge-of-god": {
  "id": "foreknowledge-of-god", "term": "Foreknowledge of God", "category": "concepts",
  "intro": "<p>The foreknowledge of God refers to his eternal, perfect, and comprehensive knowledge of all future events and persons — not merely an anticipation of what will happen, but an active, purposeful knowing that precedes creation. The biblical texts consistently treat foreknowledge as inseparable from God's sovereign decree: what God foreknows, he foreordains. Key New Testament passages establish this: Christ was \"delivered up according to the definite plan and foreknowledge of God\" (<a class=\"ref\" data-ref=\"Acts 2:23\">Acts 2:23</a>); believers were chosen \"according to the foreknowledge of God the Father\" (<a class=\"ref\" data-ref=\"1 Peter 1:2\">1 Peter 1:2</a>).</p><p>Paul's argument in Romans 8:29-30 links foreknowledge to a chain of divine action: \"Those whom he foreknew he also predestined... called... justified... glorified\" (<a class=\"ref\" data-ref=\"Romans 8:29\">Romans 8:29</a>). Romans 11:2 reinforces the covenantal dimension: God has not rejected his people \"whom he foreknew.\" The theological debate around foreknowledge centers on whether God's prior knowledge of human choices is the basis of election (the Arminian view) or whether foreknowledge and predestination are co-extensive divine acts (the Calvinist view). What is undisputed in Scripture is that God's foreknowledge is perfect, sovereign, and personal — he knows his own by name before the foundation of the world (<a class=\"ref\" data-ref=\"Romans 11:2\">Ephesians 1:4</a>).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "foreknowledge-of-god"},
  "key_refs": ["Acts 2:23", "Romans 8:29", "Romans 11:2", "1 Peter 1:2"]
},
}

def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data): written += 1
        else: skipped += 1
    print(f'BP f1: Fable → Foreknowledge of God: wrote {written}, skipped {skipped} existing.')

if __name__ == '__main__': main()
