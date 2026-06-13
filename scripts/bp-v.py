"""
BP Article Synthesis — v: Vagabond → Vulture
17 entries
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
    "vagabond": {
        "id": "vagabond",
        "term": "Vagabond",
        "category": "concepts",
        "intro": "<p>A vagabond in Scripture denotes a wanderer or fugitive driven from home and community, most memorably in <a class=\"ref\" data-ref=\"Genesis 4:12\">Genesis 4:12</a>, where God's sentence on Cain reads, \"You shall be a fugitive and a wanderer on the earth\" (R.V.). The word comes from the Latin <em>vagabundus</em> and is not used as a term of mere social contempt in the biblical text but carries the solemn weight of exile from the divine presence and the security of land and kin. In <a class=\"ref\" data-ref=\"Psalms 109:10\">Psalm 109:10</a> the same fate—children wandering and begging—is invoked as a covenantal curse on the wicked.</p><p>The word appears in the New Testament in <a class=\"ref\" data-ref=\"Acts 19:13\">Acts 19:13</a>, where the KJV describes certain Jewish exorcists as \"vagabond Jews,\" meaning itinerant or traveling practitioners who attempted to invoke the name of Jesus without genuine faith. Cain's curse became a type of spiritual rootlessness in later biblical theology: exile from God's presence is the deepest homelessness, and the gospel reversal of that exile is central to the promise of a new creation where the wandering is ended.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "vagabond", "smith": None, "isbe": "vagabond"},
        "key_refs": ["Genesis 4:12", "Psalms 109:10", "Acts 19:13"]
    },
    "vajezatha": {
        "id": "vajezatha",
        "term": "Vajezatha",
        "category": "people",
        "intro": "<p>Vajezatha was one of the ten sons of Haman the Agagite, the chief minister of the Persian king Ahasuerus (Xerxes I), who had devised a plan to destroy all the Jews in the Persian empire. When the plan was reversed by the intercession of Queen Esther and the king's favor toward Mordecai, Haman was executed and his sons fell with him. Vajezatha and his nine brothers were killed by the Jews of the capital Shushan on the thirteenth of Adar (<a class=\"ref\" data-ref=\"Esther 9:9\">Esther 9:9</a>), and their bodies were publicly hung the following day at Esther's request, ensuring the complete destruction of the house of the enemy.</p><p>The name Vajezatha, meaning \"purity\" or \"worthy of honor\" (Hitchcock: \"sprinkling the chamber\"), is of Persian origin like the names of his brothers. Haman's ten sons are listed together in Esther 9:7–9, and the names were traditionally written in a vertical column in Hebrew scrolls of Esther, signifying their simultaneous downfall. The deaths of Haman's sons fulfilled the ancient judgment on Amalek that Saul had failed to complete, framing the book of Esther as the resolution of a conflict stretching back to <a class=\"ref\" data-ref=\"1 Samuel 15:8\">1 Samuel 15:8</a>.</p>",
        "sections": [],
        "hitchcock_meaning": "sprinkling the chamber",
        "source_ids": {"easton": "vajezatha", "smith": "vajezatha", "isbe": None},
        "key_refs": ["Esther 9:9", "Esther 9:7"]
    },
    "valley": {
        "id": "valley",
        "term": "Valley",
        "category": "concepts",
        "intro": "<p>Several distinct Hebrew words are translated \"valley\" in the Old Testament, reflecting the varied topography of the biblical lands. The term <em>bik'ah</em> denotes a broad plain between mountain ranges (<a class=\"ref\" data-ref=\"Deuteronomy 8:7\">Deuteronomy 8:7</a>); <em>'emek</em> describes a broad open valley ideal for agriculture and armies (the Valley of Jezreel, the Valley of Elah); <em>nahal</em> refers to a wadi or torrent valley, typically dry except in rainy season; and <em>ge'</em> or <em>gai</em> designates a narrow ravine or gorge. Each term carries distinct geographical and narrative associations throughout Scripture.</p><p>Valleys in the Bible function as places of encounter, conflict, and transformation. The Valley of Hinnom south of Jerusalem became the site of pagan child sacrifice and later a symbol of judgment. The Valley of the Shadow of Death in <a class=\"ref\" data-ref=\"Psalms 23:4\">Psalm 23:4</a> evokes mortal danger through which God escorts his people. The Valley of Dry Bones in Ezekiel 37 becomes the setting for Israel's resurrection. Isaiah promises that every valley shall be exalted in the coming age of salvation (<a class=\"ref\" data-ref=\"Isaiah 40:4\">Isaiah 40:4</a>), inverting the landscape as a sign of God making the rough places plain.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "valley", "smith": None, "isbe": "valley"},
        "key_refs": ["Deuteronomy 8:7", "Psalms 23:4", "Isaiah 40:4", "Ezekiel 37:1"]
    },
    "vashti": {
        "id": "vashti",
        "term": "Vashti",
        "category": "people",
        "intro": "<p>Vashti was the queen of the Persian king Ahasuerus (Xerxes I, reigned 486–465 BC) who was deposed from her royal position because she refused to display herself before the king's guests at a great banquet (<a class=\"ref\" data-ref=\"Esther 1:10\">Esther 1:10–12</a>). The feast had lasted seven days, and on the final day the king, \"merry with wine,\" commanded that Vashti be brought before the assembled nobles to display her beauty. Her refusal—the reasons for which the text does not explain—enraged the king and led his counselors to warn that her example would embolden women throughout the empire to defy their husbands.</p><p>As a result, Ahasuerus issued a royal decree deposing Vashti and decreeing that \"every man should be master in his own household\" (<a class=\"ref\" data-ref=\"Esther 1:22\">Esther 1:22</a>). Her removal from the throne opened the way for Esther to be chosen as queen and ultimately to save the Jewish people. Vashti's name, meaning \"beautiful\" or \"best\" in Persian (Hitchcock: \"that drinks; thread\"), has made her a figure of considerable interpretive interest: some traditions censure her disobedience; others read her refusal as an act of courage. Her story sets the stage for the book of Esther's deeper drama of providence at work through unlikely instruments.</p>",
        "sections": [],
        "hitchcock_meaning": "that drinks; thread",
        "source_ids": {"easton": "vashti", "smith": "vashti", "isbe": "vashti"},
        "key_refs": ["Esther 1:10", "Esther 1:12", "Esther 1:19", "Esther 1:22"]
    },
    "vaticanus-codex": {
        "id": "vaticanus-codex",
        "term": "Vaticanus, Codex",
        "category": "concepts",
        "intro": "<p>The Codex Vaticanus (designated <em>B</em> or 03) is widely regarded as the oldest surviving vellum manuscript of the Christian Bible and one of the most important witnesses to the text of Scripture. Dating to the early fourth century AD (circa 300–325), it is written in Greek uncial script on fine vellum and contains most of the Old Testament in the Septuagint (LXX) translation as well as the New Testament, though it lacks portions of Genesis, Psalms, Hebrews, the Pastoral Epistles, Philemon, and Revelation. It has been housed in the Vatican Library in Rome since at least the fifteenth century.</p><p>Together with the Codex Sinaiticus, Vaticanus forms the foundation of modern critical editions of the Greek New Testament and has profoundly shaped modern Bible translations. Because it and Sinaiticus represent an Alexandrian text-type that often differs from the later Byzantine manuscripts underlying the Textus Receptus, their use in modern scholarship has generated ongoing discussion among textual critics and Bible translators. Vaticanus is generally considered a careful and accurate manuscript, and its agreement with other early witnesses—papyri, the Old Latin versions, and early Church Fathers—has given it enormous weight in establishing the earliest recoverable text of the New Testament.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "vaticanus-codex", "smith": None, "isbe": None},
        "key_refs": []
    },
    "veil-vail": {
        "id": "veil-vail",
        "term": "Veil",
        "category": "concepts",
        "intro": "<p>Several distinct objects are called a veil or vail in Scripture. The most theologically significant is the great curtain that separated the Holy Place from the Most Holy Place in the tabernacle and later the temple, woven of blue, purple, and crimson thread and embroidered with cherubim (<a class=\"ref\" data-ref=\"Exodus 26:31\">Exodus 26:31–33</a>). Only the high priest could pass through it, and only on the Day of Atonement. When Jesus died on the cross, this veil was torn from top to bottom (<a class=\"ref\" data-ref=\"Matthew 27:51\">Matthew 27:51</a>), signifying that his atoning death had opened the way into God's presence for all people—the central theme of the Epistle to the Hebrews (<a class=\"ref\" data-ref=\"Hebrews 10:19\">Hebrews 10:19–20</a>).</p><p>A different kind of veil appears in the story of Moses: after speaking with God, his face shone with such reflected glory that he covered it with a veil when addressing the people (<a class=\"ref\" data-ref=\"Exodus 34:33\">Exodus 34:33</a>). Paul interprets this veil in <a class=\"ref\" data-ref=\"2 Corinthians 3:13\">2 Corinthians 3:13–16</a> as a type of the spiritual blindness that prevents Israel from recognizing the glory of the new covenant in Christ—a veil removed only \"when one turns to the Lord.\" Women's veils, described in <a class=\"ref\" data-ref=\"Ruth 3:15\">Ruth 3:15</a> and <a class=\"ref\" data-ref=\"Isaiah 3:22\">Isaiah 3:22</a>, served as everyday garments in the ancient Near East, distinct from the bridal and religious contexts.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "veil-vail", "smith": None, "isbe": None},
        "key_refs": ["Exodus 26:31", "Exodus 34:33", "Matthew 27:51", "2 Corinthians 3:13", "Hebrews 10:19"]
    },
    "version": {
        "id": "version",
        "term": "Version",
        "category": "concepts",
        "intro": "<p>A Bible version is a translation of the Hebrew, Aramaic, and Greek Scriptures into another language. The oldest and most influential ancient version is the Septuagint (LXX), a Greek translation of the Hebrew Old Testament produced by Jewish scholars in Alexandria beginning around 250 BC and widely used by the New Testament writers and the early Church. The Latin Vulgate, translated by Jerome in the late fourth century AD and authorized as the official Bible of the Western Church, shaped European Christianity for over a millennium. Other ancient versions—the Syriac Peshitta, the Coptic, the Ethiopic, the Armenian—are valuable witnesses to early textual traditions and the global spread of the faith.</p><p>The history of English Bible translation begins with John Wycliffe's fourteenth-century rendering from the Latin and accelerates dramatically with William Tyndale's pioneering work from the original Greek and Hebrew in the sixteenth century. The King James Version (1611) achieved a literary and theological authority that endured for centuries. Modern translations—the RSV, NIV, ESV, NASB, and many others—draw on advances in textual criticism, manuscript discovery, and biblical scholarship. Each version involves choices about manuscript traditions, translation philosophy (formal vs. functional equivalence), and literary register, making the study of versions an important discipline for serious students of Scripture.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "version", "smith": None, "isbe": None},
        "key_refs": ["Genesis 3:15", "Matthew 1:23"]
    },
    "villages": {
        "id": "villages",
        "term": "Villages",
        "category": "concepts",
        "intro": "<p>Villages in the ancient biblical world were small, typically unwalled agricultural settlements surrounding a larger walled city that served as the regional center and place of refuge. The Hebrew word rendered \"villages\" in <a class=\"ref\" data-ref=\"Judges 5:7\">Judges 5:7</a> and 5:11 (<em>perazoth</em>) denotes habitations in the open country, distinct from fortified towns (<em>'arim</em>). Deuteronomy distinguishes between cities \"enclosed with high walls, gates, and bars\" and unwalled towns in the open country (<a class=\"ref\" data-ref=\"Deuteronomy 3:5\">Deuteronomy 3:5</a>), and the Jubilee law treated them differently regarding redemption of property (<a class=\"ref\" data-ref=\"Leviticus 25:29\">Leviticus 25:29–31</a>). Villages depended on the nearby walled city for military protection.</p><p>The pattern of villages clustered around a mother city shaped Jesus' ministry in Galilee, where he moved systematically through \"all the cities and villages\" teaching in their synagogues (<a class=\"ref\" data-ref=\"Matthew 9:35\">Matthew 9:35</a>). The phrase \"her daughters\" applied to dependent villages of a major city (e.g., the villages of Gaza, Ashdod) reflects a social and administrative reality throughout the ancient Near East. In the song of Deborah, the reference to village life ceasing during the oppression of Jabin (<a class=\"ref\" data-ref=\"Judges 5:7\">Judges 5:7</a>) illustrates how enemy raids forced people off their farmsteads and into walled refuges, collapsing the open-country economy.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "villages", "smith": None, "isbe": None},
        "key_refs": ["Judges 5:7", "Deuteronomy 3:5", "Leviticus 25:29", "Matthew 9:35"]
    },
    "vine": {
        "id": "vine",
        "term": "Vine",
        "category": "concepts",
        "intro": "<p>The grapevine (<em>Vitis vinifera</em>) was one of the most culturally and theologically significant plants in the ancient Near East. It appears first in Scripture in the account of Noah, who \"planted a vineyard\" after the flood (<a class=\"ref\" data-ref=\"Genesis 9:20\">Genesis 9:20</a>). Palestine was celebrated for its vines: the spies returning from Canaan carried a single cluster of grapes so large that two men bore it on a pole (<a class=\"ref\" data-ref=\"Numbers 13:23\">Numbers 13:23</a>). The vine became a central symbol of Israel's election and calling. In multiple prophetic passages Israel is depicted as a vine or vineyard planted by God—a metaphor of privilege and accountability (<a class=\"ref\" data-ref=\"Isaiah 5:1\">Isaiah 5:1–7</a>; <a class=\"ref\" data-ref=\"Psalms 80:8\">Psalm 80:8</a>; <a class=\"ref\" data-ref=\"Ezekiel 15:2\">Ezekiel 15:2</a>).</p><p>In the New Testament Jesus transforms the metaphor decisively: \"I am the true vine\" (<a class=\"ref\" data-ref=\"John 15:1\">John 15:1</a>), presenting himself as the fulfillment of all that Israel was meant to be. Those who remain in him bear fruit; those who do not are cut away. The fruit of the vine also stands at the center of the Lord's Supper, where Jesus identified the cup with his blood of the new covenant (<a class=\"ref\" data-ref=\"Matthew 26:27\">Matthew 26:27–29</a>) and declared he would not drink of it again until he drank it new in his Father's kingdom—a forward-looking eschatological promise.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "vine", "smith": "vine", "isbe": "vine"},
        "key_refs": ["Genesis 9:20", "Numbers 13:23", "Isaiah 5:1", "John 15:1", "Matthew 26:27"]
    },
    "vine-of-sodom": {
        "id": "vine-of-sodom",
        "term": "Vine of Sodom",
        "category": "concepts",
        "intro": "<p>The vine of Sodom is mentioned once in Scripture, in the Song of Moses in Deuteronomy: \"Their vine is from the vine of Sodom and from the fields of Gomorrah; their grapes are grapes of poison; their clusters are bitter\" (<a class=\"ref\" data-ref=\"Deuteronomy 32:32\">Deuteronomy 32:32</a>). The passage is part of a prophetic indictment of an unfaithful generation whose corruption is as thoroughgoing as that of the cities destroyed by divine judgment. The \"vine of Sodom\" functions as a symbol of moral poison and spiritual deception—outwardly resembling fruit but producing only bitterness and death.</p><p>The plant's botanical identity has been debated, but many scholars identify it with the colocynth (<em>Citrullus colocynthis</em>), a wild gourd that produces round, smooth fruits resembling small watermelons. These fruits appear appealing but contain a powerful bitter cathartic substance toxic in large doses. The \"apple of Sodom\" described by ancient writers (Josephus, Tacitus) may refer to this or to another plant of the region whose fruit turns to ashes or dust when touched. Whatever the botanical referent, the theological point is clear: Sodom's legacy is a harvest of beautiful appearances concealing deadly content, a fitting image for the corrupting influence of idolatry on Israel.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "vine-of-sodom", "smith": "vine-of-sodom", "isbe": None},
        "key_refs": ["Deuteronomy 32:32"]
    },
    "vinegar": {
        "id": "vinegar",
        "term": "Vinegar",
        "category": "concepts",
        "intro": "<p>Vinegar in the Bible refers to sour wine (<em>hometz</em> in Hebrew, <em>oxos</em> in Greek), produced when wine undergoes further fermentation and becomes acidic. It was a common beverage of laborers and soldiers in the ancient world, being inexpensive and thirst-quenching when mixed with water (the Roman <em>posca</em>). Boaz's workers dipped their bread in vinegar (<a class=\"ref\" data-ref=\"Ruth 2:14\">Ruth 2:14</a>), and the Nazirite vow prohibited its consumption along with wine (<a class=\"ref\" data-ref=\"Numbers 6:3\">Numbers 6:3</a>). Proverbs 10:26 uses the sharpness of vinegar on the teeth as a metaphor for the irritation a sluggard causes his employer.</p><p>The theological weight of vinegar concentrates in its association with the suffering of the Messiah. <a class=\"ref\" data-ref=\"Psalms 69:21\">Psalm 69:21</a>—\"They gave me poison for food, and for my thirst they gave me sour wine to drink\"—is cited as a prophetic text fulfilled at the crucifixion. The Gospel accounts record that Jesus was offered vinegar mixed with gall (Matthew 27:34) as an act of mockery or compassion; he tasted it and refused. Shortly before his death he was offered vinegar on a sponge (<a class=\"ref\" data-ref=\"John 19:29\">John 19:29</a>), which he received, enabling him to speak his final words. These scenes stand as direct fulfillments of the Davidic psalm's prophetic complaint.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "vinegar", "smith": "vinegar", "isbe": "vinegar"},
        "key_refs": ["Psalms 69:21", "Ruth 2:14", "Matthew 27:34", "John 19:29"]
    },
    "viol": {
        "id": "viol",
        "term": "Viol",
        "category": "concepts",
        "intro": "<p>The viol (Hebrew <em>nebel</em>) was a stringed musical instrument used in ancient Israel, rendered variously as \"psaltery,\" \"lute,\" or \"harp\" in different Bible translations. The R.V. translates <em>nebel</em> as \"lute\" in <a class=\"ref\" data-ref=\"Isaiah 5:12\">Isaiah 5:12</a> and \"stringed instrument\" elsewhere. The <em>nebel</em> was likely a large harp-like instrument with a resonating box, distinct from the smaller hand-held <em>kinnor</em> (lyre). Both were used in Levitical temple worship, and David organized the Levitical singers to play them in the sanctuary (<a class=\"ref\" data-ref=\"1 Chronicles 25:1\">1 Chronicles 25:1</a>).</p><p>The viol appears in a striking prophetic context in <a class=\"ref\" data-ref=\"Isaiah 5:12\">Isaiah 5:12</a>, where Isaiah condemns those who make music at their feasts—harp, lute, tambourine, flute, and wine—but \"do not regard the deeds of the LORD, or see the work of his hands.\" The abundance of music at banquets was not itself sinful; the failure of spiritual attention was the indictment. Similarly, in <a class=\"ref\" data-ref=\"Amos 6:5\">Amos 6:5</a> the prophet rebukes those who \"sing idle songs to the sound of the harp\" and devise musical instruments \"like David,\" while unconcerned about the ruin of Joseph—a warning that liturgical sophistication cannot substitute for justice and covenant faithfulness.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "viol", "smith": "viol", "isbe": "viol"},
        "key_refs": ["Isaiah 5:12", "Amos 6:5", "1 Chronicles 25:1"]
    },
    "viper": {
        "id": "viper",
        "term": "Viper",
        "category": "concepts",
        "intro": "<p>The viper is a venomous snake occurring in several biblical passages, with two Hebrew words of uncertain botanical identification behind the translations. The word <em>eph'eh</em> (Job 20:16; Isaiah 30:6; 59:5) probably denotes a specific venomous species of the ancient Near East, associated with the wilderness and desolate places. Job 20:16 speaks of the wicked man who \"sucked the poison of cobras; the tongue of a viper will kill him\"—a vivid image of judgment. Isaiah 30:6 describes the dangerous creatures of the Negev, and Isaiah 59:5 portrays the deeds of the wicked as viper's eggs that hatch death.</p><p>In the New Testament the viper becomes a powerful image of spiritual corruption and divine judgment. John the Baptist addressed the Pharisees and Sadducees coming to his baptism as a \"brood of vipers\" (<a class=\"ref\" data-ref=\"Matthew 3:7\">Matthew 3:7</a>), challenging them to produce genuine fruit of repentance. Jesus used the same phrase in <a class=\"ref\" data-ref=\"Matthew 12:34\">Matthew 12:34</a>, linking it to the impossibility of good fruit from an evil heart. The viper appears in a narrative of unexpected grace in <a class=\"ref\" data-ref=\"Acts 28:3\">Acts 28:3–6</a>, where Paul, shipwrecked on Malta, shook off a viper that had fastened on his hand without harm—a sign of apostolic authority recalling <a class=\"ref\" data-ref=\"Mark 16:18\">Mark 16:18</a>.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "viper", "smith": "viper", "isbe": "viper"},
        "key_refs": ["Job 20:16", "Isaiah 30:6", "Matthew 3:7", "Matthew 12:34", "Acts 28:3"]
    },
    "virgin": {
        "id": "virgin",
        "term": "Virgin",
        "category": "concepts",
        "intro": "<p>The word \"virgin\" in Scripture carries both literal and theological significance, centered especially on the great Immanuel prophecy of <a class=\"ref\" data-ref=\"Isaiah 7:14\">Isaiah 7:14</a>: \"Behold, the virgin shall conceive and bear a son, and shall call his name Immanuel.\" The Hebrew word used is <em>almah</em>, meaning a young woman of marriageable age; the Septuagint translators rendered it with the unambiguous Greek <em>parthenos</em> (virgin), and Matthew's Gospel cites both (<a class=\"ref\" data-ref=\"Matthew 1:23\">Matthew 1:23</a>) in applying the prophecy to the birth of Jesus from Mary. The incarnation of the Son of God through a virgin birth is a foundational doctrine of Christian faith, affirming both his true humanity (born of a woman) and his divine identity (no human father).</p><p>The term also carries broader import in biblical ethics and typology. Deuteronomy and the Mosaic law treated a woman's virginity as a matter of family honor and covenant integrity. Paul in <a class=\"ref\" data-ref=\"2 Corinthians 11:2\">2 Corinthians 11:2</a> describes the church as a \"pure virgin\" whom he has betrothed to Christ, and the parable of the ten virgins in <a class=\"ref\" data-ref=\"Matthew 25:1\">Matthew 25:1</a> uses the image of wedding attendants to teach eschatological readiness. The 144,000 in Revelation 14:4 are described as those who \"have not defiled themselves with women, for they are virgins\"—a likely metaphor for those who have remained faithful to Christ rather than committing spiritual adultery with the world.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "virgin", "smith": None, "isbe": None},
        "key_refs": ["Isaiah 7:14", "Matthew 1:23", "Luke 1:31", "2 Corinthians 11:2", "Matthew 25:1"]
    },
    "vision": {
        "id": "vision",
        "term": "Vision",
        "category": "concepts",
        "intro": "<p>A vision in Scripture is a direct mode of divine communication in which God reveals himself or his purposes to a recipient in a waking or trance-like state, distinct from an ordinary dream occurring during sleep. Hebrew terms (<em>hazon</em>, <em>mar'ah</em>, <em>chizzayon</em>) and the Greek <em>horama</em> all describe this mode of revelation, which was granted to patriarchs, prophets, and apostles. The classic distinction appears in <a class=\"ref\" data-ref=\"Numbers 12:6\">Numbers 12:6</a>, where God says he will speak to a prophet \"in a vision\" and \"in a dream,\" while speaking to Moses face to face—making the vision a high but not the highest form of divine communication.</p><p>Visions are pivotal in both Testaments. The prophets Isaiah, Ezekiel, Daniel, and Zechariah received extensive visions forming the core of their books. In the New Testament Zechariah received a vision of Gabriel in the temple (<a class=\"ref\" data-ref=\"Luke 1:22\">Luke 1:22</a>); Paul received visions directing the mission to Macedonia (<a class=\"ref\" data-ref=\"Acts 16:9\">Acts 16:9</a>) and testified before Agrippa of \"the heavenly vision\" that redirected his life (<a class=\"ref\" data-ref=\"Acts 26:19\">Acts 26:19</a>). The book of Revelation is explicitly framed as a visionary experience (<a class=\"ref\" data-ref=\"Revelation 1:10\">Revelation 1:10</a>). The prophet Joel's promise—\"your sons and daughters shall prophesy, your old men shall dream dreams, your young men shall see visions\"—was cited by Peter at Pentecost as a sign of the new covenant age (<a class=\"ref\" data-ref=\"Acts 2:17\">Acts 2:17</a>).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "vision", "smith": None, "isbe": "vision"},
        "key_refs": ["Numbers 12:6", "Luke 1:22", "Acts 16:9", "Acts 26:19", "Acts 2:17", "Revelation 1:10"]
    },
    "vows": {
        "id": "vows",
        "term": "Vows",
        "category": "concepts",
        "intro": "<p>A vow in Scripture is a voluntary promise made to God, binding once spoken and distinct from an oath sworn before witnesses. The Mosaic law governed vows extensively in <a class=\"ref\" data-ref=\"Numbers 30:2\">Numbers 30</a> and <a class=\"ref\" data-ref=\"Deuteronomy 23:21\">Deuteronomy 23:21–23</a>: while no one was compelled to vow, a vow once made must be kept, because breaking faith with God was a serious sin. The principle \"it is better not to vow than to vow and not pay\" is repeated in <a class=\"ref\" data-ref=\"Ecclesiastes 5:5\">Ecclesiastes 5:5</a>. Vows characteristically expressed intense petition or thanksgiving: Jacob vowed at Bethel if God would bring him safely home (<a class=\"ref\" data-ref=\"Genesis 28:20\">Genesis 28:20</a>); Hannah vowed to dedicate her son to the LORD if he opened her womb (<a class=\"ref\" data-ref=\"1 Samuel 1:11\">1 Samuel 1:11</a>).</p><p>The Nazirite vow, described in <a class=\"ref\" data-ref=\"Numbers 6:1\">Numbers 6</a>, was a special dedication involving abstention from wine, from cutting the hair, and from contact with the dead. Samson and Samuel were dedicated Nazirites from birth. The rashness of Jephthah's vow (<a class=\"ref\" data-ref=\"Judges 11:30\">Judges 11:30–31</a>), leading to his daughter's consecration, illustrates the danger of ill-considered promises to God. In the New Testament Jesus taught that simple truthfulness should make oaths unnecessary (<a class=\"ref\" data-ref=\"Matthew 5:33\">Matthew 5:33–37</a>), and Paul observed Nazirite-related customs on his final visit to Jerusalem (<a class=\"ref\" data-ref=\"Acts 21:23\">Acts 21:23</a>), showing continuity with Jewish devotional practice in the early church.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "vows", "smith": "vows", "isbe": None},
        "key_refs": ["Numbers 30:2", "Deuteronomy 23:21", "Genesis 28:20", "1 Samuel 1:11", "Judges 11:30", "Matthew 5:33"]
    },
    "vulture": {
        "id": "vulture",
        "term": "Vulture",
        "category": "concepts",
        "intro": "<p>Several Hebrew words of uncertain ornithological identification are translated \"vulture\" in different Bible versions, pointing to various large birds of prey and scavengers native to the ancient Near East. The Levitical food laws list the vulture among the unclean birds (<a class=\"ref\" data-ref=\"Leviticus 11:14\">Leviticus 11:14</a>; <a class=\"ref\" data-ref=\"Deuteronomy 14:13\">Deuteronomy 14:13</a>). The Hebrew <em>da'ah</em> and <em>ra'ah</em> likely refer to the black kite or related raptor; <em>nesher</em>, often translated \"eagle,\" may sometimes indicate the griffon vulture, which was more commonly seen in the region. Job 28:7 speaks of a hidden path \"that the falcon's eye has not seen,\" and the vulture's keen perception became a byword for sharpness of sight.</p><p>Vultures function in Scripture primarily as agents of judgment—the creatures that consume the unburied dead following military defeat, an ultimate disgrace in the ancient world. Isaiah 34:15 depicts the desolation of Edom as a place given over to wild creatures including the vulture. Jesus alludes to the proverbial gathering of vultures around a corpse in <a class=\"ref\" data-ref=\"Matthew 24:28\">Matthew 24:28</a> (\"Wherever the corpse is, there the vultures will gather\"), using it to warn against false messiahs and to illustrate the unmistakable, public nature of the true coming of the Son of Man. Some interpreters read \"eagles\" (KJV) in this passage, but \"vultures\" fits the imagery of carrion-feeding more naturally.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "vulture", "smith": "vulture", "isbe": "vulture"},
        "key_refs": ["Leviticus 11:14", "Deuteronomy 14:13", "Job 28:7", "Isaiah 34:15", "Matthew 24:28"]
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
