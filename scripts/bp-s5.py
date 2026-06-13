#!/usr/bin/env python3
import json, os

OUT_DIR = '../data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def merge_article(slug, data):
    path = os.path.join(OUT_DIR, f'{slug}.json')
    if os.path.exists(path):
        return False
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    return True

ARTICLES = {
"socho": {
  "id": "socho",
  "term": "Socho",
  "category": "places",
  "intro": "<p>Socho (also spelled Socoh, Sochoh, or Shochoh; meaning: <em>a fence</em> or <em>a hedge</em>) was the name of two towns in Judah and one in Ephraim. The most significant was the Shephelah town of Socho in the lowland district (1 Chr. 4:18; 1 Kings 4:10), situated in the Valley of Elah — the setting for the famous confrontation between David and Goliath, where the Philistines camped at Socho opposite the Israelites at Azekah (1 Sam. 17:1). Rehoboam fortified it as part of his defensive network for Judah (2 Chr. 11:7), and the Philistines later captured it during Ahaz's reign (2 Chr. 28:18).</p><p>A second Socho lay in the hill country of Judah (Josh. 15:35, 48), and a third, Socoh, was in the district of Solomon's fifth administrative region in Ephraim (1 Kings 4:10). The repeated occurrence of the name reflects its common descriptive meaning rather than a single settlement.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Samuel 17:1", "1 Chronicles 4:18", "2 Chronicles 11:7"]
},
"sodom": {
  "id": "sodom",
  "term": "Sodom",
  "category": "places",
  "intro": "<p>Sodom (meaning: <em>burning</em> or <em>the walled city</em>) was one of the five cities of the plain (pentapolis) in the vale of Siddim, near the southern end of the Dead Sea. It was notable for its prosperity and natural richness — the region was \"well watered everywhere, like the garden of the LORD\" before its destruction (Gen. 13:10) — and was the city where Abraham's nephew Lot chose to settle. The city's pervasive moral wickedness, especially the sexual violence of its men (Gen. 19), brought catastrophic divine judgment: fire and brimstone rained from heaven, destroying Sodom together with Gomorrah, Admah, and Zeboiim (Gen. 19:24–25).</p><p>Sodom became the supreme Old Testament type of divine punishment for entrenched, unrepentant wickedness. The prophets invoke its destruction as the benchmark of judgment (Isa. 1:9–10; Jer. 23:14; Ezek. 16:46–50), and Jesus himself warns that the day of judgment will be more tolerable for Sodom than for cities that reject the gospel (Matt. 10:15; 11:24). Jude 7 identifies its sin as a warning of eternal fire for those who practice gross immorality and rejection of God.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 13:10", "Genesis 19:24", "Isaiah 1:9", "Matthew 10:15"]
},
"sodoma": {
  "id": "sodoma",
  "term": "Sodoma",
  "category": "places",
  "intro": "<p>Sodoma is the Greek transliteration of the Hebrew place name Sodom, appearing in Paul's quotation of Isaiah 1:9 in Romans 9:29: \"Except the LORD of Sabaoth had left us a seed, we had been as Sodoma, and been made like unto Gomorrha.\" The Revised Version restores the familiar English form \"Sodom\" at this point. Paul uses the reference to underscore that Israel's survival as a people is entirely a matter of divine grace — without God's preserving mercy, the nation would have been as utterly destroyed as Sodom and Gomorrah.</p><p>The use of the Greek form Sodoma here reflects Paul's quotation from the Septuagint rather than from the Hebrew text, a common practice in his epistles and in the broader New Testament.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Romans 9:29", "Isaiah 1:9"]
},
"sodomites": {
  "id": "sodomites",
  "term": "Sodomites",
  "category": "concepts",
  "intro": "<p>The term \"Sodomites\" in the Old Testament translates the Hebrew <em>qadesh</em> (sacred or consecrated one) and denotes male cult prostitutes associated with Canaanite fertility religion rather than inhabitants of Sodom per se. They practiced ritual sexual immorality connected to idol worship, which Israel was strictly forbidden to adopt (Deut. 23:17). The presence of Sodomites in Judah under Rehoboam (1 Kings 14:24) represents the religious apostasy that provoked the prophets, and Asa removed them from the land as part of his reform (1 Kings 15:12), as did Jehoshaphat after him (1 Kings 22:46).</p><p>Paul's description in Romans 1:26–27 of those who \"changed the natural use\" connects the wider pattern of moral inversion to the abandonment of God, using the condemnation of Sodom as the background. The term carried both the literal sense of moral corruption and the cultic sense of false religious devotion, both of which corrupted Israel's covenant faithfulness.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Deuteronomy 23:17", "1 Kings 14:24", "1 Kings 15:12", "Romans 1:26"]
},
"solemn-meeting": {
  "id": "solemn-meeting",
  "term": "Solemn meeting",
  "category": "concepts",
  "intro": "<p>The solemn meeting (Hebrew: <em>atzeret</em>, meaning a solemn assembly or closing festival) was the convocation held on the eighth day following the Feast of Tabernacles (Lev. 23:36; Num. 29:35). It was a day of sacred rest with a distinct offering — one bull, one ram, and seven lambs — differing from the elaborate multiple sacrifices of the preceding seven days, and its character as a closing celebration set it apart from Tabernacles proper. Isaiah uses the term in his critique of Israel's hypocritical worship (Isa. 1:13), declaring that even solemn assemblies had become an abomination when accompanied by injustice.</p><p>The same Hebrew term is applied to the closing assembly on the seventh day of the Feast of Unleavened Bread (Deut. 16:8). The Revised Version renders it \"solemn assembly\" throughout, and the festival structure it describes marks a formal conclusion to Israel's great autumn harvest celebration.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Leviticus 23:36", "Numbers 29:35", "Isaiah 1:13", "Deuteronomy 16:8"]
},
"solomon": {
  "id": "solomon",
  "term": "Solomon",
  "category": "people",
  "intro": "<p>Solomon (meaning: <em>peaceful</em>; Hebrew: <em>Shelomoh</em>) was the son of David and Bathsheba, born in Jerusalem probably around 1035 B.C. and Israel's third king, reigning for forty years (c. 970–931 B.C.). He succeeded David after the abortive coup of his older brother Adonijah and was confirmed as king by the anointing of Zadok the priest and Nathan the prophet (1 Kings 1). At Gibeon the LORD appeared to Solomon in a dream and offered him whatever he would ask; Solomon chose wisdom, and God granted both wisdom and unprecedented wealth and honor (1 Kings 3:5–14).</p><p>Solomon's reign represented the zenith of the united monarchy: he built the Jerusalem temple (the crowning achievement of his reign), extended Israel's borders and trade networks, allied with Egypt through marriage, composed thousands of proverbs and songs, and received tribute from surrounding nations. Yet the proliferation of foreign wives led to idolatry in his old age (1 Kings 11:1–13), and the oppressive taxation and forced labor he imposed planted the seeds of the kingdom's division at his death. In the New Testament Jesus invokes Solomon's glory as exceeded by a field lily (Matt. 6:29) and his wisdom as exceeded by the Son of Man (Matt. 12:42).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Kings 3:12", "1 Kings 6:1", "1 Kings 11:4", "Matthew 12:42"]
},
"solomon-song-of": {
  "id": "solomon-song-of",
  "term": "Solomon, Song of",
  "category": "concepts",
  "intro": "<p>The Song of Solomon (also called Canticles, after the Vulgate's <em>Canticum Canticorum</em>, or the Song of Songs) is the \"song of songs\" — the noblest and most exquisite of its kind — attributed to Solomon (1:1). It celebrates the love between a bride and bridegroom in lyric poetry of great beauty and intensity, moving through courtship, betrothal, longing, reunion, and mutual delight in language drawn from the landscape and flora of the ancient Near East. Its canonical inclusion was debated by rabbis (accepted by Rabbi Akiva as the holiest of all the writings), and it was definitively received as Scripture.</p><p>Interpretations divide between the allegorical (the beloved represents Israel, or the church, and the bridegroom represents God, or Christ) and the literal (a celebration of human romantic love within the covenant of marriage). The New Testament's use of the bridegroom-bride metaphor for Christ and the church (John 3:29; Eph. 5:25–27; Rev. 21:2) provides a theological framework within which the allegorical reading operates, even if the primary genre is erotic poetry celebrating marital love as a divine gift.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Song of Solomon 1:1", "John 3:29", "Ephesians 5:25", "Revelation 21:2"]
},
"solomons-porch": {
  "id": "solomons-porch",
  "term": "Solomon's Porch",
  "category": "places",
  "intro": "<p>Solomon's Porch was a covered colonnade on the eastern side of the Jerusalem temple enclosure, supported by double rows of white marble columns forty feet high. Though the name connects it to the first temple, Josephus states it was a remnant of the original Solomonic structure that Herod incorporated into his rebuilt temple platform. It served as a public gathering place and teaching space where the portico opened onto the Court of the Gentiles.</p><p>All three Synoptic references to Solomon's Porch are in the Gospel of John and Acts: Jesus walked and taught there during the Feast of Dedication (John 10:23); after the healing of the lame man at the Beautiful Gate, Peter and John were seized there and addressed the crowd (Acts 3:11); and the early Jerusalem church regularly gathered in Solomon's Porch (Acts 5:12). Its association with both Jesus's teaching and the earliest apostolic proclamation made it a symbolic center of the transition from temple to church.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["John 10:23", "Acts 3:11", "Acts 5:12"]
},
"son-of-god": {
  "id": "son-of-god",
  "term": "Son of God",
  "category": "concepts",
  "intro": "<p>\"Son of God\" is used in Scripture with a range of meanings reflecting the Hebrew concept of sonship as participation in the character and purpose of God. The plural \"sons of God\" refers to the angelic beings of the divine council (Job 1:6; 38:7) and, in Genesis 6:2–4, to the godly line of Seth (in one interpretation). Israel collectively is called God's son (Ex. 4:22; Hos. 11:1), and the Davidic king is declared God's son at his enthronement (Ps. 2:7; 2 Sam. 7:14).</p><p>In the New Testament the title reaches its fullest meaning in the unique divine Sonship of Jesus Christ — not by adoption or appointment but by eternal nature and being. The confession of Jesus as the Son of God (Matt. 16:16; John 20:31) is the central creedal affirmation of the New Testament church. The Gospel of John distinguishes Jesus's sonship from that of believers: Jesus is the <em>monogenes</em> (only-begotten or unique) Son (John 1:14, 18; 3:16), while believers become sons of God by adoption through him (John 1:12; Gal. 4:5; Rom. 8:15).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Psalms 2:7", "Matthew 16:16", "John 1:14", "Romans 8:15"]
},
"son-of-man": {
  "id": "son-of-man",
  "term": "Son of man",
  "category": "concepts",
  "intro": "<p>\"Son of man\" (<em>ben adam</em> in Hebrew, <em>huios tou anthropou</em> in Greek) carries two primary registers in Scripture. First, it denotes a human being in their weakness and mortality — the Psalmist's meditation on human insignificance before God (Ps. 8:4; 144:3) and God's address to Ezekiel, whom he calls \"son of man\" over ninety times, emphasizing the prophet's creaturely frailty before the divine glory. Second, it is the majestic title of Daniel's vision: \"one like a son of man\" coming on the clouds of heaven to receive from the Ancient of Days an everlasting kingdom over all peoples (Dan. 7:13–14).</p><p>In the Gospels \"Son of Man\" is Jesus's most characteristic self-designation, used exclusively by him (and never applied to him by others except in Acts 7:56). He uses it in three clusters: his earthly authority (Mark 2:10, 28), his suffering and death (Mark 8:31), and his future coming in glory (Mark 8:38; 13:26). The title holds together his full humanity, his identification with the suffering righteous, and his ultimate vindication as cosmic ruler — making it the richest single term Jesus uses for himself.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Daniel 7:13", "Mark 8:31", "Mark 13:26", "Psalms 8:4"]
},
"songs": {
  "id": "songs",
  "term": "Songs",
  "category": "concepts",
  "intro": "<p>Sacred song pervades Scripture from the earliest periods. The Song of Moses after the crossing of the Red Sea (Ex. 15) is the first great hymn of redemption; it is followed by the song at the well (Num. 21:17), Moses's farewell Song of the Law (Deut. 32), Deborah's victory ode (Judg. 5), Hannah's prayer-song (1 Sam. 2), and David's great psalm of deliverance (2 Sam. 22). The Psalter — the Song Book of Israel — collects one hundred and fifty compositions spanning the full range of human experience before God, and was the hymnal of both the temple and the synagogue.</p><p>The New Testament continues this tradition: Mary's Magnificat (Luke 1:46–55), Zechariah's Benedictus (Luke 1:68–79), and the angels' Gloria (Luke 2:14) are all liturgical songs. Revelation presents the church triumphant singing the Song of Moses and the Song of the Lamb (Rev. 15:3), linking the final redemption to the first. Paul instructs believers to address one another in \"psalms and hymns and spiritual songs\" (Eph. 5:19; Col. 3:16), making corporate singing central to Christian worship.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Exodus 15:1", "Psalms 1:1", "Ephesians 5:19", "Revelation 15:3"]
},
"soothsayer": {
  "id": "soothsayer",
  "term": "Soothsayer",
  "category": "concepts",
  "intro": "<p>A soothsayer is one who claims to foretell future events by means other than the Spirit of God — through omens, divination, astrology, or other occult practices. The Hebrew word most often translated \"soothsayer\" or \"diviner\" (<em>qosem</em>) denotes one who casts lots or reads signs to predict the future. Balaam is called a soothsayer or diviner in Joshua 13:22, and the Philistines employed soothsayers in their consultation about the ark (1 Sam. 6:2).</p><p>The Law of Moses strictly prohibited all forms of soothsaying and divination (Deut. 18:10–14), declaring that Israel was not to practice what the nations of Canaan practiced. Isaiah condemns the soothsayers of Judah (Isa. 2:6) and the \"astrologers\" of Babylon (Isa. 47:13). The soothsaying girl at Philippi from whose spirit Paul cast out a divining spirit (Acts 16:16–18) represents the New Testament confrontation of apostolic authority with occult power in the Greco-Roman world.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Joshua 13:22", "Deuteronomy 18:10", "Isaiah 2:6", "Acts 16:16"]
},
"sop": {
  "id": "sop",
  "term": "Sop",
  "category": "concepts",
  "intro": "<p>A sop was a piece of bread used to scoop up broth, sauce, or other food from a shared dish — a common practice at meals in the ancient Near East. In Ruth 2:14 Boaz invites Ruth to eat with his reapers and dip her morsel in the vinegar (a sour wine sauce). The most theologically significant use is at the Last Supper, where Jesus took a piece of unleavened bread, dipped it in the dish of bitter herbs at the Passover table, and gave it to Judas Iscariot, identifying him as the betrayer (John 13:26–27).</p><p>Giving a sop to a guest was a mark of distinction and honor, making the act of handing it to Judas a final, deliberate gesture of grace extended even to the one who would betray him. After receiving the sop, John records, Satan entered into Judas, and Jesus dismissed him with the words \"What thou doest, do quickly.\"</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["John 13:26", "Ruth 2:14"]
},
"sopater": {
  "id": "sopater",
  "term": "Sopater",
  "category": "people",
  "intro": "<p>Sopater (meaning: <em>father who saves</em>) was a Christian from Berea in Macedonia who accompanied Paul on his journey from Greece through Macedonia and Asia at the end of the third missionary journey (Acts 20:4–6). He is likely the same person as Sosipater, greeted by Paul in Romans 16:21 as a kinsman. If so, he was a fellow-Jew and a trusted associate who participated in carrying the collection for the Jerusalem church.</p><p>Sopater's inclusion in the apostolic travel party alongside delegates from Thessalonica, Derbe, Asia Minor, and Ephesus reflects the representative character of the group — one from each major region of Paul's Gentile mission — accompanying the collection as proof of its integrity. His Berean origin recalls the church in that city whose members \"searched the scriptures daily\" (Acts 17:11).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Acts 20:4", "Romans 16:21"]
},
"sorcerer": {
  "id": "sorcerer",
  "term": "Sorcerer",
  "category": "concepts",
  "intro": "<p>A sorcerer (from Latin <em>sortiarius</em>, one who casts lots or tells fortunes) is one who claims supernatural power through occult means — magic, incantation, potions, or spirit-contact. The Hebrew <em>mekhashphim</em> (mutterers or whisperers) denotes those who practice secret arts, including the sorcerers summoned by Pharaoh against Moses (Ex. 7:11) and by Nebuchadnezzar against Daniel (Dan. 2:2). Malachi warns that God will be a swift witness against sorcerers (Mal. 3:5).</p><p>The New Testament records direct apostolic confrontations with sorcery: Simon Magus, who practiced sorcery in Samaria and astonished the people (Acts 8:9), and Elymas Bar-Jesus, the Jewish sorcerer who opposed Paul on Cyprus and was struck blind (Acts 13:8). Sorcery appears in Paul's list of the works of the flesh (Gal. 5:20, Gr. <em>pharmakeia</em>) and is among the sins that exclude from the kingdom in Revelation (Rev. 21:8; 22:15). The new believers at Ephesus publicly burned their books of sorcery valued at fifty thousand pieces of silver (Acts 19:19).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Daniel 2:2", "Acts 13:8", "Galatians 5:20", "Revelation 21:8"]
},
"sorek": {
  "id": "sorek",
  "term": "Sorek",
  "category": "places",
  "intro": "<p>Sorek (meaning: <em>choice vine</em>) was the name of a valley — properly a wadi or torrent-bed — now identified with the Wady Surar, the largest drainage basin of the Judean Shephelah running westward to the Mediterranean near modern Tel Aviv. It drains the western Judean hills, passing through the territories of Dan and the Philistine plain. The valley is famous in biblical narrative as the home of Delilah, the woman with whom Samson fell in love (Judg. 16:4), and it was through this corridor that the Philistines later brought the ark of the covenant back to Israel.</p><p>The name's connection to choice grapes reflects the valley's fertility; Isaiah may allude to it in his parable of the vineyard (Isa. 5:2). The Sorek valley's strategic position as the main route between the coast and Jerusalem made it the scene of repeated military action from the period of the Judges through modern times.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Judges 16:4"]
},
"sosipater": {
  "id": "sosipater",
  "term": "Sosipater",
  "category": "people",
  "intro": "<p>Sosipater (meaning: <em>savior of the father</em>) is greeted by Paul in Romans 16:21 as a kinsman — a fellow-Jew — along with Timothy, Lucius, and Jason. He is almost certainly the same person as Sopater of Berea, who accompanied Paul on his final journey to Jerusalem (Acts 20:4). As a kinsman of Paul and associate of the Pauline mission, Sosipater likely participated in the collection effort for the Jerusalem church and the broader pastoral network Paul maintained across his Gentile churches.</p><p>The name Sosipater is a Greek compound reflecting the common pattern of Greek names with the root <em>soter</em> (savior). His presence in the greeting list of Romans alongside other Jewish Christians in Corinth indicates that the Corinthian church included significant Jewish membership.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Romans 16:21", "Acts 20:4"]
},
"sosthenes": {
  "id": "sosthenes",
  "term": "Sosthenes",
  "category": "people",
  "intro": "<p>Sosthenes (meaning: <em>safe in strength</em> or <em>savior of his nation</em>) appears twice in the New Testament. (1) The chief ruler of the synagogue at Corinth who was seized and beaten by the crowd before the proconsul Gallio when Gallio refused to adjudicate the Jewish complaint against Paul (Acts 18:12–17). Whether his attackers were Jews enraged at his failure or Greeks expressing anti-Jewish sentiment is debated. (2) A Christian named Sosthenes is co-sender of Paul's first letter to Corinth (1 Cor. 1:1), described as \"the brother.\" Many scholars identify these as the same person — the synagogue leader who, after the beating, came to faith and became a co-worker of Paul.</p><p>If the identification is correct, Sosthenes represents a remarkable conversion: the very man whose role as synagogue ruler set the scene for Paul's opposition in Corinth became his associate in the letter to the church founded there.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Acts 18:17", "1 Corinthians 1:1"]
},
"south": {
  "id": "south",
  "term": "South",
  "category": "places",
  "intro": "<p>The Hebrew word for the south in the geographical sense is <em>Negeb</em>, which designates the arid region stretching south of the Judean hills toward the Sinai Peninsula. The Negeb was the caravan corridor through which Abraham and later the patriarchs traveled between Canaan and Egypt (Gen. 12:9; 13:1; 46:1). It comprised a broad triangle of semi-desert, characterized by scattered wells, shallow wadis that flood seasonally, and terrain requiring specialized knowledge to traverse. The land was also known for its copper resources.</p><p>The expression \"going toward the south\" in the patriarchal narratives and in descriptions of military movements often means movement into or through the Negeb. The Negeb also figures in the settlement narratives as part of the inheritance of Judah and Simeon, and in the later monarchy it served as a defensive frontier zone. Modern archaeological work has revealed a dense network of Iron Age and later settlements throughout the Negeb, indicating more sustained habitation than the arid terrain might suggest.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Genesis 12:9", "Genesis 13:1", "Numbers 13:17"]
},
"sovereignty": {
  "id": "sovereignty",
  "term": "Sovereignty",
  "category": "concepts",
  "intro": "<p>The sovereignty of God refers to his absolute right and power to do all things according to his own good pleasure, without dependence on or limitation by any external authority. The concept pervades both Testaments: Daniel's doxology declares that \"the most High ruleth in the kingdom of men, and giveth it to whomsoever he will\" (Dan. 4:25, 35), and Paul's extended treatment in Romans 9–11 grounds God's election of both Israel and the Gentiles in his sovereign mercy — \"I will have mercy on whom I will have mercy\" (Rom. 9:15, quoting Ex. 33:19).</p><p>God's sovereignty encompasses creation (he made all things and sustains them), providence (he governs all events toward his purposes), redemption (election, calling, and justification are all of grace, not human will), and final judgment. Far from undermining human responsibility, the biblical witness presents both as simultaneously true, without resolving the tension philosophically. The doxological response to this doctrine is worship: \"thine is the kingdom, and the power, and the glory\" (Matt. 6:13).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Daniel 4:35", "Romans 9:15", "Ephesians 1:11", "Revelation 4:11"]
},
"spain": {
  "id": "spain",
  "term": "Spain",
  "category": "places",
  "intro": "<p>Spain (Latin: <em>Hispania</em>) is mentioned in Paul's Letter to the Romans as a destination he planned to visit after delivering the collection to Jerusalem, hoping to stop in Rome on the way (Rom. 15:24, 28). The Iberian Peninsula was the western extremity of the Roman Empire and a region of significant Jewish settlement in the first century. Paul's ambition to preach the gospel \"where Christ was not named\" (Rom. 15:20) drove this westward vision beyond Rome itself.</p><p>Whether Paul ever reached Spain is uncertain: the Pastoral Epistles suggest a period of ministry after his first Roman imprisonment, and Clement of Rome (c. A.D. 96) writes that Paul reached \"the extreme limit of the west\" — a phrase many interpret as Spain. No clear documentary evidence confirms a Spanish mission, but the ambition expressed in Romans 15 fits the pattern of Paul's missionary strategy of advancing the gospel along the major Roman roads to the farthest reaches of the empire.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Romans 15:24", "Romans 15:28"]
},
"sparrow": {
  "id": "sparrow",
  "term": "Sparrow",
  "category": "concepts",
  "intro": "<p>The sparrow (Hebrew: <em>tsippor</em>, a general term for small birds; Greek: <em>strouthion</em>) was the most common small bird of Palestine and the cheapest available for sacrifice — two sparrows sold for a farthing (a quarter of an assarion, a very small coin), and five for two farthings (Matt. 10:29; Luke 12:6–7). The leper's cleansing ritual required two living birds (Lev. 14:4–7), and the poor could offer turtledoves or sparrows in place of larger animals.</p><p>Jesus uses the sparrow's low price as the basis for a powerful argument from the lesser to the greater: if not one sparrow falls to the ground without the Father's knowledge, how much more precious are his disciples. The saying establishes the universality of divine providence — extending even to the cheapest, most overlooked creature — as the ground of fearlessness in the face of persecution. The Psalmist's longing for the sparrow's freedom to nest near the altar (Ps. 84:3) uses the bird as a symbol of intimate access to God's dwelling.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Matthew 10:29", "Luke 12:6", "Psalms 84:3", "Leviticus 14:4"]
},
"spicery": {
  "id": "spicery",
  "term": "Spicery",
  "category": "concepts",
  "intro": "<p>Spicery (Hebrew: <em>nechoth</em>) is identified with the gum tragacanth, the dried sap or gum exuded from various species of the astragalus plant, of which some twenty species grew in Palestine and the surrounding region. The tragacanth was used medicinally, as a binding agent, and as an aromatic substance in trade. It is mentioned in the list of goods carried by the Ishmaelite caravan trading from Gilead to Egypt — \"bearing spicery and balm and myrrh\" — to which Joseph was sold by his brothers (Gen. 37:25; 43:11).</p><p>The distinction between spicery and other aromatics (balm, myrrh) suggests that <em>nechoth</em> was a recognizable and commercially valuable commodity in the ancient caravan trade between the Fertile Crescent and Egypt. Jacob sends it as part of the gift to the Egyptian official (Joseph) in an attempt to secure favorable treatment during the famine.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Genesis 37:25", "Genesis 43:11"]
},
"spices": {
  "id": "spices",
  "term": "Spices",
  "category": "concepts",
  "intro": "<p>Spices (Hebrew: <em>besamim</em>, aromatic substances) served three primary functions in biblical life: ritual worship, personal cosmetics and hygiene, and funerary preparation. The sacred anointing oil and the incense burned on the golden altar in the tabernacle and temple required specific aromatic ingredients listed in Exodus 30 — myrrh, cinnamon, calamus, cassia, stacte, onycha, galbanum, and frankincense. These were stored in the temple treasury (1 Chr. 9:29) and required careful priestly oversight.</p><p>Spices also played an important economic role: the Queen of Sheba brought Solomon \"spices in great abundance\" as part of her tribute (1 Kings 10:2), and Hezekiah showed the Babylonian envoys his \"spicehouse\" as evidence of his wealth (2 Kings 20:13). In the burial of the dead, Joseph's body was embalmed with Egyptian methods (Gen. 50:2), while the women prepared aromatic spices to anoint Jesus's body (Luke 23:56; 24:1; John 19:39–40), and Nicodemus brought a hundred pounds of myrrh and aloes for the burial — an extraordinary quantity reflecting royal honor.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Exodus 30:23", "1 Kings 10:2", "Luke 23:56", "John 19:39"]
},
"spider": {
  "id": "spider",
  "term": "Spider",
  "category": "concepts",
  "intro": "<p>The spider appears in Scripture as a wisdom image of structural fragility and self-deceiving confidence. Job's friend Bildad compares the hope of the godless to a spider's web or \"spider's house\" — a trust that will not hold when tested (Job 8:14). Isaiah extends the image: the wicked \"weave the spider's web\" (Isa. 59:5), meaning their schemes and works are insubstantial, incapable of producing what they promise, and potentially dangerous to those who touch them — \"he that eateth of their eggs dieth.\"</p><p>The proverb writer notes that the spider (or gecko, as some translations render it) \"taketh hold with her hands, and is in kings' palaces\" (Prov. 30:28), using the creature's ubiquity and persistence as an image of the small things that nonetheless gain access to great places. Palestine is home to numerous spider species, and the delicacy and impermanence of the web made it a natural metaphor for self-constructed human securities that God can blow away.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Job 8:14", "Isaiah 59:5", "Proverbs 30:28"]
},
"spies": {
  "id": "spies",
  "term": "Spies",
  "category": "events",
  "intro": "<p>The sending of spies or scouts to reconnoiter Canaan before Israel's invasion was commanded by God and executed by Moses at the request of the people (Num. 13:1–2; Deut. 1:22). From Kadesh-barnea Moses selected twelve men — one chief from each tribe — who entered Canaan and surveyed it for forty days, returning with samples of its produce (including the famous cluster of grapes from the Valley of Eshcol) and a report on its inhabitants and fortifications (Num. 13:17–29).</p><p>Ten of the twelve gave a discouraging report, describing the inhabitants as giants before whom \"we were as grasshoppers\" (Num. 13:33), and the people's consequent rebellion condemned the entire adult generation of the Exodus to die in the wilderness (Num. 14). Only Caleb and Joshua, who brought the minority report of faith — \"we are well able to overcome it\" — survived to enter the land. Joshua later sent two spies to Jericho (Josh. 2), where they were sheltered by Rahab, who became a model of faith in the later tradition (Heb. 11:31; James 2:25).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Numbers 13:2", "Numbers 14:6", "Joshua 2:1", "Hebrews 11:31"]
},
"spikenard": {
  "id": "spikenard",
  "term": "Spikenard",
  "category": "concepts",
  "intro": "<p>Spikenard (Hebrew: <em>nerd</em>; Greek: <em>nardos pistike</em>) was a costly aromatic ointment extracted from the root of the Indian plant <em>Nardostachys jatamansi</em>, imported from the Himalayan foothills to the Mediterranean world via trade routes. It was \"very precious\" (Mark 14:3; John 12:3), indicating its great commercial value. It appears in the Song of Solomon as a luxury fragrance associated with the beloved's intimacy (Song 1:12; 4:13–14).</p><p>The most significant New Testament appearances are the anointing accounts: at Bethany, a woman (identified as Mary in John 12) broke an alabaster jar of spikenard worth approximately a year's wages and poured it on Jesus's head or feet. Judas's protest at the \"waste\" prompted Jesus's defense of the act as a preparation for his burial and a memorial that would accompany the gospel proclamation everywhere (Matt. 26:13; Mark 14:9). The gesture's extravagance was the point: the love it expressed exceeded any economic calculation.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Song of Solomon 1:12", "Mark 14:3", "John 12:3", "Matthew 26:13"]
},
"spirit": {
  "id": "spirit",
  "term": "Spirit",
  "category": "concepts",
  "intro": "<p>The biblical terms for spirit — Hebrew <em>ruach</em> and Greek <em>pneuma</em> — both mean primarily <em>wind</em> or <em>breath</em>, the invisible but powerful force of life and movement. <em>Ruach</em> denotes the breath of life given by God that makes humans living beings (Gen. 2:7), the vital principle that departs at death (Eccl. 8:8), the rational immortal soul by which humans reason and will (Prov. 20:27), and the sovereign activity of God himself (Gen. 1:2; Isa. 40:13). The human spirit is that dimension of human being that is oriented toward God and capable of communion with him.</p><p>Spirit also designates non-physical personal beings: angels, demons, and the Holy Spirit. In the New Testament <em>pneuma</em> is frequently the Spirit of God (the Holy Spirit), whose role in regeneration, sanctification, and empowerment is the distinctive mark of the new covenant age. Paul distinguishes the spirit from the flesh (Rom. 8:1–17), soul (1 Thess. 5:23), and body, and presents the life \"according to the Spirit\" as the normative existence of the believer in Christ.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Genesis 2:7", "Ecclesiastes 8:8", "Romans 8:6", "1 Corinthians 2:11"]
},
"spirit-holy": {
  "id": "spirit-holy",
  "term": "Spirit, Holy",
  "category": "concepts",
  "intro": "<p>The Holy Spirit is the third person of the Holy Trinity, fully God and co-equal with the Father and the Son. In the Old Testament the Spirit of God is active in creation (Gen. 1:2), empowers leaders and prophets (Judg. 14:6; 1 Sam. 10:10; Isa. 61:1), and is promised in new covenant abundance: \"I will pour out my Spirit on all flesh\" (Joel 2:28). The Spirit's presence in Israel was selective and often temporary; the prophets anticipate a fuller, permanent dispensation.</p><p>In the New Testament the Holy Spirit descends on Jesus at his baptism (Matt. 3:16–17) and empowers his ministry. Jesus promises the Spirit as the Paraclete (Advocate, Comforter) who will teach, remind, convict, and guide his disciples into all truth (John 14:16–17; 16:7–15). At Pentecost the Spirit is poured out on the entire assembled community (Acts 2:1–4), inaugurating the new covenant age. The Spirit indwells every believer (Rom. 8:9), produces the fruit of Christian character (Gal. 5:22–23), distributes gifts for ministry (1 Cor. 12:4–11), and intercedes for the saints (Rom. 8:26–27).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Joel 2:28", "John 14:16", "Acts 2:4", "Romans 8:9"]
},
"sponge": {
  "id": "sponge",
  "term": "Sponge",
  "category": "concepts",
  "intro": "<p>The sponge appears in Scripture only in the passion narratives of all four Gospels. At the crucifixion, when Jesus said \"I thirst,\" a soldier ran, soaked a sponge in sour wine (vinegar), placed it on a hyssop branch or stick, and held it to Jesus's lips (Matt. 27:48; Mark 15:36; John 19:29). The act fulfilled the Psalmist's lament: \"they gave me also gall for my meat; and in my thirst they gave me vinegar to drink\" (Ps. 69:21).</p><p>Sponges were common in the ancient Mediterranean world, harvested from the seabed by divers along the coasts. Their absorbent quality made them useful for soldiers' canteens and in medical contexts. The gesture of offering the vinegar-soaked sponge at the cross is ambiguous in the Gospel accounts — it may have been a compassionate act to relieve thirst, or a mockers' gesture, or both; the Evangelists present it within the texture of the passion without editorial resolution.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Matthew 27:48", "John 19:29", "Psalms 69:21"]
},
"spouse": {
  "id": "spouse",
  "term": "Spouse",
  "category": "concepts",
  "intro": "<p>The word \"spouse\" in the biblical canon refers exclusively to the wife or bride in the texts where it appears. In the Song of Solomon it occurs repeatedly as the bridegroom's term of address for his beloved (Song 4:8–12; 5:1), and in Hosea 4:13–14 it refers to the wives and daughters of the Israelites who played the harlot. The term carries the connotation of covenantal partnership, since marriage in the biblical world was a formal covenant relationship (Mal. 2:14).</p><p>In the broader biblical theology of marriage, the relationship between husband and wife is used repeatedly as a figure for the covenant between God and Israel (Isa. 54:5; Jer. 3:14; Hos. 2:19–20) and between Christ and the church (Eph. 5:22–33; Rev. 21:2). The faithfulness of a spouse is thus not merely a social or moral norm but a reflection of the covenant faithfulness of God himself.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Song of Solomon 4:8", "Hosea 4:13", "Ephesians 5:25", "Revelation 21:9"]
},
"spring": {
  "id": "spring",
  "term": "Spring",
  "category": "concepts",
  "intro": "<p>The spring (Hebrew: <em>'ayin</em>, literally \"eye,\" the gleaming open source of water) was the vital resource around which settlement in ancient Palestine organized itself. Springs and wells determined the location of towns and encampments throughout the biblical world, and their ownership was worth fighting over (Gen. 21:25–31; 26:15–22). The spring is to be distinguished carefully from the well (<em>beer</em>), which is a dug shaft reaching groundwater; the spring flows naturally from the earth.</p><p>Springs appear throughout biblical narrative: the spring of Harod where Gideon's army camped (Judg. 7:1), the spring of En-gedi where David hid from Saul (1 Sam. 23:29), and the upper and lower springs of the Negeb given to Achsah as her inheritance (Josh. 15:19). Theologically, the spring becomes a figure of divine provision: \"with thee is the fountain of life\" (Ps. 36:9), and the messianic hope envisions \"a fountain opened to the house of David\" (Zech. 13:1) and Jesus offering \"living water\" welling up to eternal life (John 4:14).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Joshua 15:19", "Psalms 36:9", "John 4:14", "Zechariah 13:1"]
},
"stachys": {
  "id": "stachys",
  "term": "Stachys",
  "category": "people",
  "intro": "<p>Stachys (meaning: <em>spike</em> or <em>an ear of grain</em>) was a Christian at Rome whom Paul greets as \"my beloved\" in Romans 16:9 — a term of personal affection indicating close acquaintance. Beyond this single greeting, nothing is known of Stachys in the canonical record. The name is Greek and was found in inscriptions associated with the imperial household, leading some scholars to suggest he may have been a freed slave or servant of Caesar's household.</p><p>Paul's habit of specific personal greetings in Romans 16 reflects the network of personal relationships he had cultivated across the empire, and Stachys's inclusion among those specifically singled out for affectionate address indicates he held a particular place in Paul's circle of trusted friends and co-workers.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Romans 16:9"]
},
"stacte": {
  "id": "stacte",
  "term": "Stacte",
  "category": "concepts",
  "intro": "<p>Stacte (Hebrew: <em>nataph</em>, meaning <em>a drop</em> or <em>to distil</em>) was one of the four aromatic ingredients of the sacred incense burned on the golden altar in the tabernacle (Ex. 30:34). The Revised Version margin suggests it may be opobalsamum — the gum from the balsam tree — while other identifications propose myrrh, storax, or labdanum (the gum of the rock-rose). The Hebrew root's connection to dripping or distilling suggests a resinous substance that seeped naturally from the tree.</p><p>The incense of Exodus 30 was to be made exclusively for the worship of God — any unauthorized production for personal use was punishable by being cut off from the people (Ex. 30:38). Stacte's inclusion in this sacred formula ensured that it, like the other ingredients, was consecrated entirely to the service of God's presence in the tabernacle.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Exodus 30:34"]
},
"star-morning": {
  "id": "star-morning",
  "term": "Star, Morning",
  "category": "concepts",
  "intro": "<p>The morning star — the bright planet Venus, the last and brightest light visible just before the sun rises — is used as a title for Christ in Revelation 22:16: \"I am the root and offspring of David, and the bright and morning star.\" The title condenses several themes: Christ as the light that heralds the coming day of salvation, the one who fulfills the Davidic promise, and the one who overcomes darkness. The promise to the overcomers at Thyatira is that Christ will give them \"the morning star\" (Rev. 2:28), meaning himself.</p><p>Peter speaks of the prophetic word as a light shining in a dark place \"until the day dawn, and the day star arise in your hearts\" (2 Pet. 1:19), using the same image for the internal illumination of faith. In Isaiah 14:12 \"son of the morning\" (<em>helel ben shahar</em>, translated \"Lucifer\" in the KJV) is used of the king of Babylon in a fall from glory — a passage later applied typologically to Satan's pride, making the morning star a title also associated with the fallen adversary, in stark contrast to Christ's possession of it by right.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Revelation 22:16", "Revelation 2:28", "2 Peter 1:19"]
},
"stargazers": {
  "id": "stargazers",
  "term": "Stargazers",
  "category": "concepts",
  "intro": "<p>Stargazers — those who divine the future by observing the heavens — are condemned by Isaiah in his oracle against Babylon (Isa. 47:13). The Babylonians were renowned in antiquity as the world's most sophisticated astronomers and astrologers, and their system of reading celestial signs for political and personal predictions was deeply embedded in Mesopotamian culture. Isaiah taunts them: \"Let now the astrologers, the stargazers, the monthly prognosticators, stand up, and save thee from these things that shall come upon thee\" — the implication being that their elaborate celestial science would be powerless to prevent Babylon's fall.</p><p>This critique reflects the broader biblical polemic against Mesopotamian divination: the God of Israel alone knows and reveals the future (Isa. 41:22–23; 46:10), and all attempts to read that future from stars, livers, or lots are both idolatrous and futile. The Magi of Matthew 2, following a star to Jerusalem, represent a gentile tradition that, at least in one remarkable instance, the God of Israel turned to serve his own revelatory purposes.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Isaiah 47:13", "Isaiah 41:22", "Matthew 2:2"]
},
"stars": {
  "id": "stars",
  "term": "Stars",
  "category": "concepts",
  "intro": "<p>Stars in Scripture are first presented as the handiwork of God's creation (Gen. 1:14–16), appointed to mark times and seasons, to provide light, and to display the glory of their Maker (Ps. 19:1). Their number — known only to God, who calls each by name (Ps. 147:4; Isa. 40:26) — became the image of the promise to Abraham that his descendants would be as innumerable as the stars of heaven (Gen. 15:5; 22:17). The eleven stars of Joseph's dream (Gen. 37:9) symbolized his brothers' future obeisance.</p><p>In prophetic and apocalyptic literature stars carry rich symbolic weight: Amos's mention of Pleiades and Orion (Amos 5:8) emphasizes God's sovereignty over the cosmos. Falling stars signal cosmic upheaval and divine judgment (Isa. 34:4; Rev. 6:13). The seven stars of Revelation 1:16 are the angels of the seven churches — Christ holds them in his right hand. Jude 13 characterizes false teachers as \"wandering stars\" without fixed orbit, reserved for eternal darkness, in contrast to the righteous who will \"shine as the brightness of the firmament\" (Dan. 12:3).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Genesis 1:14", "Genesis 15:5", "Daniel 12:3", "Revelation 1:16"]
},
"stater": {
  "id": "stater",
  "term": "Stater",
  "category": "concepts",
  "intro": "<p>The stater was a Greek silver coin mentioned in Matthew 17:27, where Jesus instructs Peter to cast a hook into the sea, take the first fish, and find a stater in its mouth to pay the temple tax (<em>didrachma</em>) for both of them. The Revised Version renders it \"shekel\" since the stater was equivalent to the Hebrew shekel in value — four Greek drachmas, or two didrachmas, worth approximately two shillings and sixpence in Victorian currency.</p><p>The temple tax of half a shekel (the <em>didrachma</em>) was the annual levy on every adult Jewish male for the upkeep of the sanctuary, based on the Mosaic census tax of Exodus 30:13. The miracle of the coin in the fish's mouth provided the exact amount needed for two people — Peter and Jesus — with nothing to spare and nothing extra, a detail that has struck readers as evidence of the miracle's precise intentionality.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Matthew 17:27", "Exodus 30:13"]
},
"stealing": {
  "id": "stealing",
  "term": "Stealing",
  "category": "concepts",
  "intro": "<p>Stealing — the unauthorized taking of another person's property — is prohibited by the eighth commandment of the Decalogue (Ex. 20:15; Deut. 5:19) and condemned throughout both Testaments. The Mosaic law prescribed restitution rather than imprisonment as the primary remedy: a thief who could not repay could be sold into service for the debt (Ex. 22:1–4), and fivefold restitution was required for stolen oxen, twofold for other animals. Kidnapping for slavery — theft of a person — was a capital offense (Ex. 21:16; Deut. 24:7).</p><p>The prophets regularly list theft among the covenant violations that bring judgment (Jer. 7:9; Hos. 4:2; Zech. 5:3). In the New Testament Paul instructs those who formerly stole to \"steal no more, but rather let him labor\" and give to those in need (Eph. 4:28), grounding the prohibition in the ethic of generosity and honest work. Jesus's image of the thief who comes only to steal, kill, and destroy (John 10:10) contrasts with the Good Shepherd who gives life abundantly.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Exodus 20:15", "Exodus 22:1", "Ephesians 4:28", "John 10:10"]
},
"steel": {
  "id": "steel",
  "term": "Steel",
  "category": "concepts",
  "intro": "<p>\"Steel\" in the Authorized Version of 2 Samuel 22:35, Job 20:24, and Psalm 18:34 renders the Hebrew <em>nechoshet</em>, more accurately translated \"bronze\" or \"brass\" in the Revised Version. The expression \"bow of brass\" (or \"steel\" in the AV) indicates a bow of exceptional hardness and strength — so hard that only a divinely strengthened warrior could bend it. True steel (iron alloyed with carbon to increase hardness) was not widely available in the biblical world, though iron itself was increasingly common from the Iron Age onward.</p><p>Similarly in Jeremiah 15:12 the same word is translated as \"northern iron and steel\" in the AV but rendered \"iron and bronze\" in more modern versions. The poetic context suggests the metaphorical meaning of indestructible, unbreakable strength — a strength that only God can provide to his servant or that his judgment can overcome.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["2 Samuel 22:35", "Psalms 18:34", "Jeremiah 15:12"]
},
"stephanas": {
  "id": "stephanas",
  "term": "Stephanas",
  "category": "people",
  "intro": "<p>Stephanas (meaning: <em>crown</em>) was a leading member of the church at Corinth, whose household was among those Paul had personally baptized — the \"firstfruits of Achaia\" (1 Cor. 1:16; 16:15). His household had devoted themselves to the ministry of the saints, and Paul urges the Corinthians to submit to such men and to recognize all who labor and cooperate with the gospel (1 Cor. 16:15–16). Stephanas, Fortunatus, and Achaicus traveled from Corinth to Paul at Ephesus, refreshing the apostle's spirit and supplying what was lacking from the church's contact with him (1 Cor. 16:17).</p><p>Some have conjectured that Stephanas may have been the \"jailer of Philippi\" mentioned in Acts 16, but the identification lacks textual support. His designation as the firstfruits of Achaia gives him historical significance as one of the very first converts in the Greek mainland.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Corinthians 1:16", "1 Corinthians 16:15", "1 Corinthians 16:17"]
},
"stephen": {
  "id": "stephen",
  "term": "Stephen",
  "category": "people",
  "intro": "<p>Stephen (Greek: <em>Stephanos</em>, meaning <em>crown</em>) was one of the seven men chosen as deacons to oversee the daily distribution to Hellenistic Jewish widows in the Jerusalem church, described as \"a man full of faith and of the Holy Spirit\" (Acts 6:5). He quickly emerged as a powerful apologist and miracle-worker, disputing with members of diaspora synagogues who could not withstand his wisdom. Falsely accused of blasphemy against Moses and the temple, he was brought before the Sanhedrin and delivered the longest speech recorded in Acts — a sweeping review of Israel's history demonstrating that God's presence was never confined to the temple and that Israel had consistently rejected his messengers.</p><p>At the conclusion of his speech Stephen declared his vision of the Son of Man standing at God's right hand, which enraged the council. He was dragged outside Jerusalem and stoned — becoming the first Christian martyr (Acts 7:59–60). Stephen's dying prayer echoed Jesus's own: \"Lord, lay not this sin to their charge.\" Saul of Tarsus, who would become Paul the apostle, witnessed and approved the execution (Acts 7:58; 8:1), making Stephen's death a pivotal moment in both the persecution and the eventual expansion of the church.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Acts 6:5", "Acts 7:55", "Acts 7:59", "Acts 8:1"]
},
"stoics": {
  "id": "stoics",
  "term": "Stoics",
  "category": "concepts",
  "intro": "<p>The Stoics were a school of Greek philosophy founded by Zeno of Citium (c. 334–262 B.C.) who taught in the <em>Stoa Poikile</em> (painted porch) at Athens — hence the name. They are sometimes described as \"the Pharisees of Greek paganism\" for their ethical rigorism, emphasis on duty and virtue, and belief that the wise man lives according to reason and is indifferent to pleasure and pain. They affirmed a single divine reason (<em>logos</em>) pervading all things and the brotherhood of all rational beings under one universal law.</p><p>Paul encountered Stoic philosophers at Athens alongside Epicureans, and both groups brought him to the Areopagus to explain his teaching (Acts 17:18). His speech on the Areopagus deliberately engages Stoic language — the quotation \"for we are also his offspring\" (Acts 17:28) comes from the Stoic poet Aratus — as a point of contact before introducing the distinctively Christian assertions of creation, resurrection, and judgment. The Stoic framework of a divine logos that orders all things provided both preparation for and sharp contrast with the incarnation of the Logos in Jesus Christ.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Acts 17:18", "Acts 17:28"]
},
"stomacher": {
  "id": "stomacher",
  "term": "Stomacher",
  "category": "concepts",
  "intro": "<p>The stomacher (Hebrew: <em>pethigil</em>) is an article of female attire mentioned in Isaiah's catalogue of the luxuries that God will remove from the proud women of Zion as part of his judgment on Jerusalem (Isa. 3:24). The precise nature of the garment is uncertain: some identify it as a richly embroidered sash or girdle worn around the chest or waist, while the Greek Septuagint and Latin Vulgate suggest a fine garment of purple or gold embroidery. In any case it represents the elaborate finery of wealthy women in eighth-century Jerusalem.</p><p>Isaiah contrasts the stomacher with \"a girding of sackcloth\" — the mourning garb that will replace it when judgment comes. The passage (Isa. 3:16–26) is one of the most detailed descriptions of ancient women's clothing and ornamentation in the Old Testament, listing over twenty specific items of adornment, all of which God declares he will take away.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Isaiah 3:24"]
},
"stone": {
  "id": "stone",
  "term": "Stone",
  "category": "concepts",
  "intro": "<p>Stone in the biblical world served as the primary material for construction, memorialization, and the marking of covenantal events. Jacob set up a stone pillar at Bethel to mark his encounter with God (Gen. 28:18), and Joshua erected a great stone at Shechem as a witness to Israel's covenant renewal (Josh. 24:26–27). Samuel set up the stone he called Ebenezer — \"stone of help\" — to commemorate God's deliverance from the Philistines (1 Sam. 7:12). Stones were gathered from fields for cultivation (Isa. 5:2), cut for building (1 Kings 5:17), and used for sealing caves and tombs.</p><p>In biblical theology stone becomes a rich metaphor. Christ is the stone the builders rejected that became the cornerstone (Ps. 118:22; Matt. 21:42), the stone cut without human hands that fills the whole earth (Dan. 2:34–35), and the living stone on which the church is built as living stones (1 Pet. 2:4–8). The New Testament's \"stone\" Christology draws on multiple OT threads — stumbling stone (Isa. 8:14), foundation stone (Isa. 28:16), and cornerstone (Ps. 118:22) — unified in Jesus Christ.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Genesis 28:18", "Psalms 118:22", "Isaiah 28:16", "1 Peter 2:4"]
},
"stones-precious": {
  "id": "stones-precious",
  "term": "Stones, Precious",
  "category": "concepts",
  "intro": "<p>Precious stones are mentioned throughout Scripture as symbols of beauty, wealth, and divine glory. Approximately twenty different gemstones are named in the Bible. Twelve gems, each engraved with the name of one of the tribes of Israel, adorned the high priest's breastplate (Ex. 28:17–20): sardius, topaz, carbuncle, emerald, sapphire, diamond, jacinth, agate, amethyst, beryl, onyx, and jasper. The exact identification of each stone with modern gemological categories is uncertain, as ancient gem nomenclature does not correspond directly to modern classification.</p><p>Precious stones figure in the wisdom literature as images of value surpassing earthly treasure (Prov. 3:15; 8:11; 20:15). In the prophetic literature they adorn the heavenly Jerusalem (Isa. 54:11–12; Ezek. 28:13), and Revelation's vision of the New Jerusalem is built with twelve foundation stones matching the breastplate gems (Rev. 21:19–20), symbolizing the perfection and beauty of the redeemed city of God.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Exodus 28:17", "Proverbs 3:15", "Isaiah 54:11", "Revelation 21:19"]
},
"stoning": {
  "id": "stoning",
  "term": "Stoning",
  "category": "concepts",
  "intro": "<p>Stoning was the prescribed method of capital punishment in the Mosaic law for offenses including idolatry (Deut. 13:10), blasphemy (Lev. 24:14–16), adultery (Deut. 22:21), Sabbath-breaking (Num. 15:35), and disobedience to parents (Deut. 21:21). The procedure typically involved the witnesses to the crime casting the first stones (Deut. 17:7), with the community participating afterward, distributing guilt for the execution across the community rather than concentrating it in an executioner. The condemned was usually first thrown down from an elevation before the stones were cast.</p><p>Notable stonings in the biblical narrative include the execution of Achan and his household for the sin of taking devoted things (Josh. 7:25), the judicial murder of Naboth by Jezebel's arrangement (1 Kings 21), and the martyrdom of Stephen (Acts 7:59). Paul was stoned at Lystra and left for dead (Acts 14:19). Stoning also appears as a metaphor for the rejection of prophets: Jesus laments that Jerusalem \"stonest them that are sent unto thee\" (Matt. 23:37).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Leviticus 24:14", "Deuteronomy 17:7", "Acts 7:59", "Matthew 23:37"]
},
"stork": {
  "id": "stork",
  "term": "Stork",
  "category": "concepts",
  "intro": "<p>The stork (Hebrew: <em>hasidah</em>, meaning <em>kindness</em> or <em>the kind one</em>) was named for its observed affection for its young and its loyalty to its mate — qualities that the Hebrews found admirable enough to encode in the creature's name. Despite this positive association, the stork was listed among the birds forbidden as food (Lev. 11:19; Deut. 14:18), likely because it was a scavenger and a hunter of frogs and fish in marshy ground. White storks are still regular migrants through the Jordan Valley, arriving in great numbers each spring on their passage from Africa to Europe.</p><p>The stork's faithfulness to its migratory schedule is invoked by Jeremiah as a rebuke to Israel: \"the stork in the heaven knoweth her appointed times… but my people know not the judgment of the LORD\" (Jer. 8:7). This use of natural animal instinct to condemn human spiritual dullness is a characteristic rhetorical move of the Hebrew prophets. The Psalmist notes the fir trees as the stork's home (Ps. 104:17), reflecting observation of nesting behavior.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Leviticus 11:19", "Jeremiah 8:7", "Psalms 104:17"]
},
"strain-at": {
  "id": "strain-at",
  "term": "Strain at",
  "category": "concepts",
  "intro": "<p>The phrase \"strain at a gnat\" in Matthew 23:24 (AV) — \"Ye blind guides, which strain at a gnat, and swallow a camel\" — is actually a misprint or mistranslation in the 1611 King James Version. The correct rendering, as the Revised Version restores, is \"strain out a gnat\" (<em>diulizontes</em> = straining or filtering out). The image is of the Pharisees' meticulous practice of filtering wine through cloth to avoid accidentally swallowing an insect, which was ritually unclean — while metaphorically swallowing a camel, the largest of unclean animals.</p><p>Jesus's point is the absurdity of scrupulous attention to minor ritual details (straining out gnats) while ignoring the weightier matters of the law — justice, mercy, and faithfulness (Matt. 23:23). The proverb became proverbial in English speech via the KJV's familiar text, though the correct rendering is \"strain out\" rather than \"strain at.\"</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Matthew 23:24"]
},
"stranger": {
  "id": "stranger",
  "term": "Stranger",
  "category": "concepts",
  "intro": "<p>The Hebrew word most commonly translated \"stranger\" (<em>ger</em>) denotes a foreigner who resides permanently or semi-permanently in Israel — not merely a passing traveler but a recognized resident alien. The Law of Moses extended significant protections to the ger: equality before the courts, the right to glean fields at harvest, access to cities of refuge, participation in the Passover if circumcised, and the instruction to love the stranger as oneself, \"for ye were strangers in the land of Egypt\" (Lev. 19:34; Deut. 10:19). The repeated appeal to Israel's own experience of oppression in Egypt grounds the ethics of hospitality in covenantal memory.</p><p>A second term, <em>nokri</em>, denotes a foreigner who remains culturally separate and is subject to different economic regulations (e.g., interest may be charged, Deut. 23:20). The distinction between resident alien and temporary foreigner shaped Israel's social and legal obligations. In the New Testament both Jesus and Paul extend the category of \"neighbor\" beyond ethnic boundaries, and Ephesians 2:19 declares that Gentile believers are \"no more strangers and foreigners, but fellow citizens with the saints.\"</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Leviticus 19:34", "Deuteronomy 10:19", "Ephesians 2:19"]
},
"straw": {
  "id": "straw",
  "term": "Straw",
  "category": "concepts",
  "intro": "<p>Straw (Hebrew: <em>teben</em>) was the dried stalks of grain after threshing and was essential in ancient brick-making — mixed with clay to bind and prevent cracking as the bricks dried in the sun. The forced labor of the Israelites in Egypt included gathering straw for this purpose, and Pharaoh's cruel order to withhold straw while maintaining the same brick quota intensified their oppression and provides the narrative context for the exodus (Ex. 5:7–18). This detail is consistent with Egyptian construction practice known from archaeological evidence.</p><p>Straw also served as fodder for livestock (Isa. 11:7; 25:10; 65:25; Gen. 24:25, 32), and its combustibility made it a natural metaphor for the worthless and transient. Isaiah's messianic vision of peace envisions the lion eating straw like an ox (Isa. 11:7; 65:25), the reversal of predatory nature, as a sign of universal shalom. Paul's image of building with straw, wood, and stubble on the foundation of Christ (1 Cor. 3:12) uses the material's combustibility to represent works of no lasting value.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Exodus 5:7", "Isaiah 11:7", "1 Corinthians 3:12"]
},
"stream-of-egypt": {
  "id": "stream-of-egypt",
  "term": "Stream of Egypt",
  "category": "places",
  "intro": "<p>The Stream of Egypt (Hebrew: <em>nachal Mitsraim</em>; also \"the river of Egypt\" or \"brook of Egypt\") is the Wady el-'Arish, a broad but usually dry desert wadi running northeast across the Sinai Peninsula to the Mediterranean coast, approximately fifty miles southwest of Gaza. It formed the recognized natural boundary between Canaan and Egypt (Num. 34:5; Josh. 15:4; 1 Kings 8:65) and marked the southwestern limit of the promised land in the covenant with Abraham (Gen. 15:18, where the \"river\" may refer to the Nile or to this wadi).</p><p>Isaiah uses the image in a promise of ingathering: \"In that day the LORD will thresh from the flowing Euphrates to the Wadi of Egypt\" (Isa. 27:12), with the two great rivers defining the full extent of the dispersed people's return. The distinction between this wadi and the Nile is important for geographic precision in the boundary descriptions of Numbers and Joshua.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Numbers 34:5", "Joshua 15:4", "Isaiah 27:12"]
},
"street": {
  "id": "street",
  "term": "Street",
  "category": "concepts",
  "intro": "<p>Streets in the ancient biblical world were rarely the paved, organized thoroughfares of modern imagination; most were narrow, unpaved lanes between houses, used for commerce, communication, and social life. The most famous street in the New Testament is \"the street called Straight\" at Damascus (Acts 9:11), identified with the long east-west colonnade that formed the principal thoroughfare of the Hellenistic-Roman city, still preserved in its general line in modern Damascus. It was there that Saul of Tarsus, struck blind on the road to Damascus, was brought to the house of Judas to wait for Ananias.</p><p>The street was also the venue of public proclamation, mourning, religious display, and commercial transaction. Jesus criticizes those who pray standing on street corners to be seen (Matt. 6:5), while the master in the parable sends servants to the streets and lanes of the city to compel guests for the wedding feast (Luke 14:21). The broad street (plateia) of the heavenly Jerusalem flows with the river of life (Rev. 22:2), where God's servants will walk in eternal day.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Acts 9:11", "Matthew 6:5", "Revelation 22:2"]
},
"stripes": {
  "id": "stripes",
  "term": "Stripes",
  "category": "concepts",
  "intro": "<p>Flogging or stripes (<em>malkot</em> in Hebrew, <em>mastiges</em> in Greek) was a prescribed judicial punishment in the Mosaic law, limited to a maximum of forty blows so that the offender would not be degraded beyond what the law allowed (Deut. 25:1–3). The later rabbinic practice reduced this to thirty-nine (\"forty save one\") as a safeguard against miscounting; Paul twice refers to receiving \"forty stripes save one\" from synagogue authorities (2 Cor. 11:24), indicating this punishment was applied to him five times.</p><p>Roman flogging (<em>flagellatio</em>) was far more severe than Jewish stripes, using a whip with lead or bone tips that could lacerate the flesh to the bone. It was administered to Jesus before the crucifixion (Matt. 27:26; Mark 15:15). Paul also received three Roman beatings with rods (Acts 16:22–23; 2 Cor. 11:25). Isaiah 53:5 — \"by his stripes we are healed\" — became the locus classicus for the substitutionary understanding of Christ's suffering.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Deuteronomy 25:3", "2 Corinthians 11:24", "Isaiah 53:5", "Matthew 27:26"]
},
"subscriptions": {
  "id": "subscriptions",
  "term": "Subscriptions",
  "category": "concepts",
  "intro": "<p>The subscriptions to Paul's epistles — the brief closing notes appended to many letters in the Authorized Version, such as \"Written from Rome\" or \"The first epistle to the Corinthians was written from Philippi\" — are not part of the original inspired text. In their present form they are ascribed to Euthalius, a bishop of the fifth century who annotated manuscripts for liturgical use. Several of these subscriptions are demonstrably incorrect: for example, Galatians is subscribed as written from Rome, whereas the letter gives no clear indication of its origin.</p><p>These additions reflect the later church's interest in reconstructing the circumstances of Paul's letters and providing liturgical context, but they carry no apostolic authority. Modern translations generally omit them or include them only in footnotes, correctly treating the Pauline text as ending at the final verse of each letter.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Romans 16:27", "1 Corinthians 16:24"]
},
"suburbs": {
  "id": "suburbs",
  "term": "Suburbs",
  "category": "concepts",
  "intro": "<p>The suburbs (Hebrew: <em>migrash</em>, meaning pasture land or open ground) designate the immediate open land surrounding Levitical cities — a defined belt of land extending 1,000 cubits from the city wall in each direction (Num. 35:3–5), reserved for the grazing of the Levites' flocks and cattle and for their gardens and fields. The forty-eight Levitical cities scattered throughout Israel's tribal territories each had such suburban pasture lands attached to them, ensuring that the tribe of Levi — which received no contiguous territorial inheritance — could maintain its livestock and agricultural life.</p><p>In 2 Kings 23:11 a different Hebrew word (<em>parvarim</em>) is rendered \"precincts\" or \"suburbs\" in reference to areas adjacent to the temple, likely the outer courts or chambers. The Authorized Version's use of \"suburbs\" reflects the general sense of space immediately outside a town or city boundary.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Numbers 35:3", "Numbers 35:7", "Ezekiel 45:2"]
},
"succoth": {
  "id": "succoth",
  "term": "Succoth",
  "category": "places",
  "intro": "<p>Succoth (meaning: <em>booths</em> or <em>tents</em>) is the name of two distinct places in the Old Testament. (1) The first encampment of the Israelites after leaving Ramesses in Egypt at the beginning of the Exodus (Ex. 12:37; 13:20; Num. 33:5–6). It is identified with Tell el-Maskhutah in the eastern Delta, the civil name of the store city Pithom. (2) A city east of the Jordan in the territory of Gad (Josh. 13:27), identified with Tell Deir 'Alla in the Jordan Valley, where Jacob had earlier built booths for his cattle after his reunion with Esau — giving the site its name (Gen. 33:17). This Transjordanian Succoth was ruled by elders who refused to provision Gideon's army and were punished by him with thorns and briers (Judg. 8:5–16), and it was known for its foundries — the temple bronze was cast in the clay ground near Succoth (1 Kings 7:46; 2 Chr. 4:17).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Exodus 12:37", "Genesis 33:17", "Judges 8:5", "1 Kings 7:46"]
},
"succoth-benoth": {
  "id": "succoth-benoth",
  "term": "Succoth-benoth",
  "category": "concepts",
  "intro": "<p>Succoth-benoth (meaning: <em>booths of daughters</em> or <em>tents of young women</em>) was a deity worshipped by the Babylonian settlers whom the Assyrian king placed in Samaria to replace the deported Israelites (2 Kings 17:30). The name is generally understood as identifying the Babylonian goddess Zir-banit (or Sarpanit), the consort of Marduk, who was the chief deity of Babylon. Worship of this goddess apparently involved ritual booths or tents associated with sacred prostitution.</p><p>The catalogue of foreign gods introduced into Samaria in 2 Kings 17:29–31 illustrates the religious syncretism that characterized the repopulated region, as each national group maintained its own deity while also nominally acknowledging the God of Israel. This mixed worship became the theological basis for the later Jewish disdain for the Samaritans as a people of impure religion.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["2 Kings 17:30"]
},
"sukkiims": {
  "id": "sukkiims",
  "term": "Sukkiims",
  "category": "people",
  "intro": "<p>The Sukkiims (also Sukkites; LXX and Vulgate: Troglodytes, meaning \"cave-dwellers\") were one of the African peoples who composed part of the army of Shishak (Sheshonq I) of Egypt when he invaded Judah in the fifth year of Rehoboam's reign (2 Chr. 12:3). They are mentioned alongside Lubim (Libyans) and Ethiopians as the ethnic components of Shishak's vast force of 1,200 chariots and 60,000 horsemen.</p><p>The Sukkiims are generally identified with nomadic or semi-nomadic people of the African interior or the region along the Red Sea, possibly inhabiting the caves of the hills south of Egypt (hence the Greek rendering \"troglodytes\"). Their single appearance in Scripture provides evidence of the diverse ethnic recruitment of the Libyan pharaohs of Egypt's Twenty-second Dynasty, who drew military manpower from across North Africa.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["2 Chronicles 12:3"]
},
"sun": {
  "id": "sun",
  "term": "Sun",
  "category": "concepts",
  "intro": "<p>The sun (Hebrew: <em>shemesh</em>) is first presented in Scripture as a created luminary appointed by God to govern the day and to mark seasons, days, and years (Gen. 1:14–18) — a deliberate contrast with surrounding cultures where the sun was a major deity. Israel was explicitly forbidden to worship the sun as the nations did (Deut. 4:19; 17:3), though sun-worship repeatedly tempted Israel and was condemned by the prophets (Ezek. 8:16). The sun's sovereignty over the day reflects God's ordering of creation for human flourishing.</p><p>The sun serves as a powerful image in biblical poetry and prophecy: the Lord is \"a sun and shield\" (Ps. 84:11); his face shines like the sun in its strength (Rev. 1:16); and the messianic hope speaks of an age when \"the sun shall no longer be your light by day\" because God himself will be the eternal light (Isa. 60:19–20; Rev. 21:23). Joshua's command for the sun to stand still at Gibeon (Josh. 10:12–13) and Hezekiah's sign of the retreating shadow (2 Kings 20:11) represent God's sovereign authority over his own creation.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 1:14", "Psalms 84:11", "Isaiah 60:19", "Revelation 21:23"]
},
"suph": {
  "id": "suph",
  "term": "Suph",
  "category": "places",
  "intro": "<p>Suph (Deut. 1:1, Revised Version; the Authorized Version renders it as \"Red Sea\") appears in the geographical introduction to Deuteronomy as part of the location formula: \"on this side Jordan, in the wilderness, in the plain over against the Red Sea [Suph], between Paran and Tophel.\" Some scholars identify Suph with Suphah (Num. 21:14, margin) as a specific place name on the desert route, while others take it as an abbreviation for the Sea of Suph — the Red Sea or Gulf of Aqaba.</p><p>The identification is uncertain. If a place name, Suph lies somewhere in the wilderness south or southeast of the Dead Sea. The formula in Deuteronomy 1:1 is a geographical anchor for Moses's farewell addresses, placing the speeches firmly in the Transjordanian wilderness east of the Jordan just before Israel's crossing into Canaan.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Deuteronomy 1:1", "Numbers 21:14"]
},
"suphah": {
  "id": "suphah",
  "term": "Suphah",
  "category": "places",
  "intro": "<p>Suphah appears in Numbers 21:14 (margin; also Revised Version) in a quotation from the ancient \"Book of the Wars of the LORD\" — a now-lost source cited in the wilderness narrative. The text reads: \"Waheb in Suphah, and the wadis of Arnon.\" Suphah is tentatively located near the south-eastern corner of the Dead Sea, possibly at the Ghor es-Safieh, the Jordan delta area where the Zered River enters the Dead Sea from the east.</p><p>The quotation from the Book of the Wars gives Suphah historical depth as a recognized geographical landmark in an older military tradition. Its precise identification remains uncertain, but its association with the conquest-era movements of Israel east of the Dead Sea makes it part of the wilderness itinerary documented in Numbers 33.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Numbers 21:14"]
},
"supper": {
  "id": "supper",
  "term": "Supper",
  "category": "concepts",
  "intro": "<p>Supper was the principal meal of the day in the Jewish world, taken in the early evening after the day's work and heat had subsided (Mark 6:21; John 12:2; 1 Cor. 11:21). Unlike the lighter breakfast or midday meal, supper was the social and family meal around which hospitality and celebration revolved. Great banquets and feasts are consistently described as evening events in both Old and New Testaments.</p><p>The most theologically significant supper in Scripture is the Last Supper — the Passover meal Jesus shared with his disciples on the eve of his crucifixion, during which he instituted the Lord's Supper (Eucharist) as the covenant meal of the new community (Matt. 26:17–30; Mark 14:12–26; Luke 22:7–23; 1 Cor. 11:23–26). The Marriage Supper of the Lamb (Rev. 19:9) is the consummation of all these covenant meals — the great feast of the redeemed with Christ at the end of history.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Mark 6:21", "1 Corinthians 11:23", "Luke 22:20", "Revelation 19:9"]
},
"surety": {
  "id": "surety",
  "term": "Surety",
  "category": "concepts",
  "intro": "<p>A surety is one who becomes legally and financially responsible for another person's obligations — a guarantor who pledges to fulfill a debt or obligation if the primary party fails. Proverbs repeatedly warns against becoming surety for a stranger's debt, as it ensnares the pledger in another person's irresponsibility (Prov. 6:1; 11:15; 17:18; 22:26). Judah's pledge to become surety for Benjamin before Jacob is one of the most moving human gestures in the Joseph narrative (Gen. 43:9; 44:32).</p><p>The most theologically significant use is in Hebrews 7:22, where Jesus is described as \"the surety of a better covenant\" — the one who personally guarantees that all the promises of the new covenant will be fulfilled. Where the Levitical priesthood could only offer imperfect mediation, Christ stands as the eternal guarantee of the covenant's completion, having paid the debt of sin himself and securing the inheritance for all who trust in him.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Hebrews 7:22", "Genesis 43:9", "Proverbs 6:1"]
},
"susanchites": {
  "id": "susanchites",
  "term": "Susanchites",
  "category": "people",
  "intro": "<p>The Susanchites were the inhabitants of Shushan (Susa), the Elamite capital that served as one of the administrative capitals of the Persian Empire. They are named in Ezra 4:9 among the adversaries of the Jews who wrote to the Persian king Artaxerxes opposing the rebuilding of Jerusalem — a letter designed to alarm the king about a potentially rebellious Jewish community. Shushan's prominence as the setting for the Book of Esther (and later Nehemiah's service at the Persian court) gives its inhabitants historical significance in the post-exilic period.</p><p>The mixed population of Samaria that opposed the rebuilding effort included peoples from Babylon, Cuthah, Ava, Hamath, and Shushan (Ezra 4:9–10), reflecting the Assyrian and Babylonian policy of population exchange that had filled the northern territories with diverse ethnic groups after the deportation of Israel.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Ezra 4:9", "Esther 1:2"]
},
"susanna": {
  "id": "susanna",
  "term": "Susanna",
  "category": "people",
  "intro": "<p>Susanna (meaning: <em>lily</em>) was one of the women who followed Jesus from Galilee and ministered to him and the Twelve from their own resources (Luke 8:3). She is named alongside Mary Magdalene and Joanna (the wife of Herod's steward Chuza) in this brief but remarkable notice of women as financial supporters and traveling companions of Jesus's ministry. The reference is the only mention of Susanna in the canonical New Testament.</p><p>These women, who had been healed of evil spirits and infirmities, formed an integral part of the traveling mission of Jesus, and their continued fidelity is confirmed by the role women played at the crucifixion and resurrection (Luke 23:55–56; 24:1–10). Susanna's inclusion in Luke's named list reflects his particular attention to women as participants in the kingdom of God.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Luke 8:3"]
},
"susi": {
  "id": "susi",
  "term": "Susi",
  "category": "people",
  "intro": "<p>Susi was the father of Gaddi, the representative of the tribe of Manasseh among the twelve spies sent by Moses to scout the land of Canaan (Num. 13:11). Beyond this single genealogical reference, nothing is known of Susi. His son Gaddi is one of the ten who returned with a discouraging report about the land's inhabitants, contributing to the people's forty-year delay in entering Canaan.</p><p>The name Susi is linguistically connected to the Hebrew word for horse (<em>sus</em>), possibly suggesting his family's association with horse-rearing or cavalry, though this is speculative. Like many fathers named only in genealogical or tribal lists, Susi's primary significance is the son he contributed to Israel's national history.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Numbers 13:11"]
},
"swallow": {
  "id": "swallow",
  "term": "Swallow",
  "category": "concepts",
  "intro": "<p>The swallow (Hebrew: <em>sis</em> or <em>deror</em>) was a familiar migratory bird of Palestine, returning each spring in large numbers. The swift (which some identify with <em>sis</em>) and the swallow both appear in Scripture as emblems of the seasonal regularity of creation (Jer. 8:7) — their faithful return each spring contrasted with Israel's failure to return to God. Hezekiah, in his illness, likens his moaning to the chattering of the swallow (Isa. 38:14).</p><p>The Psalmist's longing for the swallow's freedom is expressed in Psalm 84:3: \"Yea, the sparrow hath found a house, and the swallow a nest for herself, where she may lay her young, even thine altars, O LORD of hosts, my King and my God\" — the bird's instinctive homing to the sanctuary becoming a figure for the believer's longing to dwell in God's house. The swallow's darting, agile flight also appears in the simile of Proverbs 26:2: \"as the swallow by flying, so the curse causeless shall not come.\"</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Psalms 84:3", "Jeremiah 8:7", "Isaiah 38:14", "Proverbs 26:2"]
},
"swan": {
  "id": "swan",
  "term": "Swan",
  "category": "concepts",
  "intro": "<p>The swan appears in the Authorized Version's list of unclean birds that Israelites were forbidden to eat (Lev. 11:18; Deut. 14:16), translating the Hebrew <em>tinshemeth</em>. The identification is uncertain: the Revised Version renders it \"ibis\" or \"horned owl,\" and most modern translations follow the latter. True swans (Cygnus) do occur as occasional winter visitors to the Jordan River and the Sea of Galilee, but they are rare, which may explain the difficulty in identifying the Hebrew term with certainty.</p><p>If the swan is the correct identification, its inclusion among the unclean birds would be based on dietary rather than moral categories — the Levitical distinction is between creatures of different domains and habits rather than a judgment on the bird's character. The swans' rarity in Palestine may have made the term puzzling to later translators.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Leviticus 11:18", "Deuteronomy 14:16"]
},
"swelling": {
  "id": "swelling",
  "term": "Swelling",
  "category": "concepts",
  "intro": "<p>The \"swelling of Jordan\" (Jer. 12:5; Zech. 11:3; also rendered \"the pride of Jordan\" in the Revised Version) refers not to flood-surge per se but to the dense thicket of tamarisks, willows, poplars, and reeds growing along the Jordan's banks in the lower valley near the Dead Sea. This lush jungle-like vegetation, sometimes twelve to fourteen feet high, was the haunt of lions and other predators and made the river crossing genuinely dangerous. The \"pride\" of Jordan thus denotes this luxuriant, threatening undergrowth.</p><p>Jeremiah uses the image rhetorically: if Jeremiah cannot run with men on foot, how will he contend with horses? If he stumbles in safe land, what will he do in the thicket of Jordan? The comparison moves from the manageable to the overwhelming, using the known danger of the Jordan jungle as a figure for greater trials ahead. Zechariah similarly uses the cedar and the lions in the Jordan's thicket as images of the lament of the proud at the fall of their protectors.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Jeremiah 12:5", "Zechariah 11:3"]
},
"swine": {
  "id": "swine",
  "term": "Swine",
  "category": "concepts",
  "intro": "<p>The swine (Hebrew: <em>hazir</em>) was regarded as the most unclean and most abhorred of animals in Israelite religion. The law classified it as unclean because it has a split hoof but does not chew the cud — failing the second criterion of the two-part test for clean animals (Lev. 11:7; Deut. 14:8). Eating its flesh and touching its carcass rendered a person ritually unclean. The prophets use swine as an image of the utmost degradation and covenant unfaithfulness (Isa. 65:4; 66:3, 17).</p><p>In the New Testament the parable of the Prodigal Son reaches its nadir when the son finds himself feeding swine — the most humiliating possible employment for a Jewish man, far from home and covenant (Luke 15:15–16). The demoniac episode in the Decapolis involves a herd of two thousand swine (Mark 5:11–13), suggesting a Gentile region. Jesus's warning \"do not cast your pearls before swine\" (Matt. 7:6) uses the animal's disregard for what is valuable as a figure for those who are incapable of receiving sacred truth.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Leviticus 11:7", "Luke 15:15", "Mark 5:11", "Matthew 7:6"]
},
"sword": {
  "id": "sword",
  "term": "Sword",
  "category": "concepts",
  "intro": "<p>The sword was the primary close-combat weapon of the biblical world and appears throughout Scripture both as a literal instrument of war and as a pervasive theological metaphor. Hebrew swords were typically double-edged, pointed, worn in a sheath, and suspended from the belt (Ex. 32:27; 1 Sam. 31:4; Ps. 149:6). The development from bronze to iron swords across the biblical period gave the Philistines an early military advantage over Israel that was gradually overcome.</p><p>In biblical theology the sword carries multiple meanings. God's judgment is repeatedly depicted as a sword — \"the LORD's sword is bathed in blood\" (Isa. 34:6); the divinely appointed ruler bears the sword as God's agent of justice (Rom. 13:4). The \"sword of the Spirit, which is the word of God\" (Eph. 6:17) depicts Scripture as the believer's offensive weapon in spiritual warfare. Hebrews 4:12 describes the word of God as sharper than any two-edged sword, penetrating to the division of soul and spirit. The returning Christ is depicted with a sharp sword proceeding from his mouth (Rev. 19:15), exercising the ultimate divine judgment.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Ephesians 6:17", "Hebrews 4:12", "Romans 13:4", "Revelation 19:15"]
},
"sycamine-tree": {
  "id": "sycamine-tree",
  "term": "Sycamine tree",
  "category": "concepts",
  "intro": "<p>The sycamine tree is mentioned once in the New Testament, in Jesus's saying about faith the size of a mustard seed: \"If ye had faith as a grain of mustard seed, ye might say unto this sycamine tree, Be thou plucked up by the root, and be thou planted in the sea; and it should obey you\" (Luke 17:6). The Greek word <em>sykaminos</em> is generally identified with the black mulberry (<em>Morus nigra</em>), a long-lived tree with an extraordinarily deep and tenacious root system — making the uprooting image particularly vivid. Some distinguish it from the sycamore-fig, though both grow in Palestine.</p><p>The mulberry tree was cultivated throughout Palestine and the Mediterranean world for its fruit and for its leaves, which were used to feed silkworms. Its deep roots and long lifespan made it a symbol of stability in the landscape, and the image of faith commanding such a tree underscores the limitless scope of genuine trust in God.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Luke 17:6"]
},
"sycamore": {
  "id": "sycamore",
  "term": "Sycamore",
  "category": "concepts",
  "intro": "<p>The sycamore (more precisely <em>sycomore</em> or sycamore-fig; Hebrew: <em>shikmah</em>; Greek: <em>sykomoros</em>) is <em>Ficus sycomorus</em>, a large fig-bearing tree with mulberry-like leaves that provided both shade and fruit for the poor in ancient Palestine. Its wood was plentiful and valuable enough to be stored in great quantities by the kings of Israel and Judah (1 Kings 10:27; 2 Chr. 1:15), and David appointed a special overseer for the sycamore groves (1 Chr. 27:28). Amos identified himself as a \"dresser of sycamore trees\" before his prophetic call (Amos 7:14), meaning he notched the fruit to accelerate ripening.</p><p>The most famous New Testament sycamore is the tree climbed by the tax collector Zacchaeus of Jericho to see Jesus over the crowd (Luke 19:4). The large, low-branching, easy-to-climb sycamore was ideal for the purpose, and Jesus's invitation to Zacchaeus to come down became the occasion for his salvation and the declaration that \"the Son of Man came to seek and to save that which was lost\" (Luke 19:10).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Luke 19:4", "Amos 7:14", "1 Kings 10:27", "Luke 19:10"]
},
"sychar": {
  "id": "sychar",
  "term": "Sychar",
  "category": "places",
  "intro": "<p>Sychar (possibly meaning: <em>liar</em> or <em>drunkard</em> — a derogatory punning form of Shechem or Samaria in prophetic literature, Isa. 28:1, 7) was the Samaritan town near which Jacob's Well was located, where Jesus's conversation with the Samaritan woman took place (John 4:5). From the time of the Crusaders Sychar was identified with ancient Shechem, but modern scholarship and archaeology generally locate it at the village of Askar on the northern slope of Mount Ebal, about half a mile from Jacob's Well. Others maintain the traditional identification with the site near Tell Balata.</p><p>The theological significance of the location is immense: Jacob had given the ground to Joseph (Gen. 48:22; John 4:5), and the well itself was associated with the patriarch's provision for his flocks. Jesus's offer of \"living water\" (John 4:10–14) at this ancestral well, and his declaration that \"salvation is of the Jews\" yet extends to all who worship in spirit and truth (John 4:22–24), marks the passage as one of the New Testament's most theologically dense encounters.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["John 4:5", "John 4:10", "John 4:22", "Genesis 48:22"]
},
}

def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f"BP s5: Socho → Sychar: wrote {written}, skipped {skipped} existing.")

main()
