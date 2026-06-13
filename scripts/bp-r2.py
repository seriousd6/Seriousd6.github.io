"""
BP Article Synthesis — r2: Resurrection of the dead → Rye
Covers Easton entries: Resurrection of the dead through Rye (53 entries)

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

Script: scripts/bp-r2.py
Run: python3 scripts/bp-r2.py
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
    "resurrection-of-the-dead": {
        "id": "resurrection-of-the-dead",
        "term": "Resurrection of the dead",
        "category": "concepts",
        "intro": "<p>The resurrection of the dead is the biblical teaching that at the end of the age the bodies of the dead will be raised to face judgment and to enter their eternal state. The clearest Old Testament statement is Daniel 12:2: \"Many of them that sleep in the dust of the earth shall awake, some to everlasting life, and some to shame and everlasting contempt.\" Job expressed confident hope of bodily resurrection (Job 19:25–27), and Isaiah 26:19 speaks of dead bodies rising. Jesus declared that \"the hour is coming, in the which all that are in the graves shall hear his voice, and shall come forth; they that have done good, unto the resurrection of life; and they that have done evil, unto the resurrection of damnation\" (John 5:28–29).</p><p>The resurrection of Jesus Christ is the foundation and guarantee of the general resurrection: \"But now is Christ risen from the dead, and become the firstfruits of them that slept\" (1 Corinthians 15:20). Paul argues at length in 1 Corinthians 15 that to deny the resurrection of the dead is to deny Christ's resurrection and to make faith empty. The resurrection body is described as transformed — incorruptible, glorious, powerful, and spiritual — suited to the eschatological existence it will inhabit (1 Corinthians 15:42–44). Revelation 20:11–15 depicts the final resurrection and judgment, and Revelation 21–22 portrays the redeemed in their resurrection bodies dwelling in the new creation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "resurrection-of-the-dead", "smith": "resurrection-of-the-dead", "isbe": "resurrection-of-the-dead"},
        "key_refs": ["Daniel 12:2", "John 5:28", "1 Corinthians 15:20", "Revelation 20:12"]
    },
    "reuben": {
        "id": "reuben",
        "term": "Reuben",
        "category": "people",
        "intro": "<p>Reuben (meaning <em>who sees the son</em> or more commonly understood as <em>behold a son</em>, from Leah's cry at his birth: \"the LORD hath looked upon my affliction,\" Genesis 29:32) was the firstborn son of Jacob and Leah, and thus the natural heir to the birthright blessing. He demonstrated moral courage when he saved Joseph from death by persuading his brothers to throw him into a pit rather than kill him, intending to restore him later (Genesis 37:21–22). However, his act of sleeping with his father's concubine Bilhah (Genesis 35:22) disqualified him from the birthright, which passed to Joseph's sons Ephraim and Manasseh, while the tribal leadership went to Judah.</p><p>Jacob's final blessing of Reuben (Genesis 49:3–4) acknowledges him as the firstborn of his strength and excellence, but pronounces that he is \"unstable as water\" and will not excel because he defiled his father's bed. The Tribe of Reuben settled east of the Jordan in the fertile plateau of Transjordan, but eventually diminished in prominence and was absorbed or scattered — largely fulfilling the patriarchal oracle. Reuben's sons are listed in Genesis 46:9, and Numbers 1:20–21 counts 46,500 men of military age in the tribe at the first census.</p>",
        "hitchcock_meaning": "who sees the son; the vision of the son",
        "source_ids": {"easton": "reuben", "smith": "reuben", "isbe": "reuben"},
        "key_refs": ["Genesis 29:32", "Genesis 35:22", "Genesis 37:21", "Genesis 49:3"]
    },
    "reuben-tribe-of": {
        "id": "reuben-tribe-of",
        "term": "Reuben, Tribe of",
        "category": "concepts",
        "intro": "<p>The Tribe of Reuben, descended from Jacob's firstborn, settled on the eastern side of the Jordan in the plateau of Moab, between the Arnon River in the south and the territory of Gad to the north (Numbers 32:1–5; Joshua 13:15–23). Their territory included Heshbon, Dibon, and Medeba. At the first census in the wilderness, Reuben numbered 46,500 men of war (Numbers 1:20–21), but by the second census had declined to 43,730 (Numbers 26:7). Rubenite warriors crossed the Jordan to assist in the conquest of Canaan and then returned to their inheritance (Joshua 22:1–9).</p><p>After the conquest, the Reubenites built an altar at the Jordan — which nearly sparked civil war until they explained it was a memorial rather than a rival sanctuary (Joshua 22:10–34). The Tribe of Reuben faded from prominence in later history: the Song of Deborah reproaches Reuben for failing to join the battle against Sisera (Judges 5:15–16), and the tribe appears infrequently in the subsequent narrative. By the 9th century, their territory had been largely absorbed by Moab, as the Mesha Stele and prophetic references indicate.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "reuben-tribe-of", "smith": "reuben-tribe-of"},
        "key_refs": ["Numbers 1:20", "Joshua 13:15", "Joshua 22:10"]
    },
    "reuel": {
        "id": "reuel",
        "term": "Reuel",
        "category": "people",
        "intro": "<p>Reuel (meaning <em>the shepherd</em> or <em>friend of God</em>) is the name of several biblical individuals, the most significant being the father-in-law of Moses. In Exodus 2:18, Moses's father-in-law is called Reuel — the priest of Midian whose daughter Zipporah Moses married; this same man is later called Jethro (Exodus 3:1), possibly because Jethro was a title or an alternative name. Another Reuel was the second son of Esau and Basemath, daughter of Ishmael, and the father of four chieftains of Edom (Genesis 36:4, 10). A third Reuel was a Gadite leader (Numbers 2:14), and a fourth was a Benjaminite ancestor (1 Chronicles 9:8).</p>",
        "hitchcock_meaning": "the shepherd or friend of God",
        "source_ids": {"easton": "reuel", "smith": "reuel"},
        "key_refs": ["Exodus 2:18", "Genesis 36:4"]
    },
    "revelation": {
        "id": "revelation",
        "term": "Revelation",
        "category": "concepts",
        "intro": "<p>Revelation (Greek <em>apokalypsis</em>, meaning <em>uncovering</em> or <em>disclosure</em>; also from Latin <em>revelatio</em>, <em>unveiling</em>) refers to the act by which God makes himself and his will known to human beings in ways that go beyond natural reason or observation. The biblical doctrine of revelation distinguishes between general revelation — what can be known of God through creation and conscience (Romans 1:19–20; Psalm 19:1–6) — and special revelation, which is God's direct communication through prophets, mighty acts, Scripture, and supremely through the incarnate Son. The author of Hebrews opens with the declaration that God \"at sundry times and in divers manners spake in time past unto the fathers by the prophets, hath in these last days spoken unto us by his Son\" (Hebrews 1:1–2).</p><p>Special revelation is the foundation of Scripture: the prophets received the word of the LORD, and the apostles proclaimed what they had seen and heard of the incarnate Word. The canon of Scripture is regarded as the complete and sufficient deposit of special revelation for the church age. The theological concept of revelation undergirds the entire biblical enterprise: without God's self-disclosure, knowledge of his character, will, and saving purpose would be inaccessible to fallen humanity.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "revelation", "isbe": "revelation"},
        "key_refs": ["Hebrews 1:1", "Romans 1:19", "Galatians 1:12"]
    },
    "revelation-of-christ": {
        "id": "revelation-of-christ",
        "term": "Revelation of Christ",
        "category": "concepts",
        "intro": "<p>The Revelation of Christ (Greek <em>apokalypsis Iesou Christou</em>) refers in New Testament usage both to the initial disclosure of Christ in the incarnation and to his future visible appearing at his second coming. Paul uses the phrase for both: \"the grace of God which was given you by Jesus Christ\" (1 Corinthians 1:4–7) anticipates his readers waiting for \"the coming of our Lord Jesus Christ\" and his revelation. Most distinctively, 2 Thessalonians 1:7 promises that God will give rest to those who suffer \"when the Lord Jesus shall be revealed from heaven with his mighty angels, in flaming fire taking vengeance on them that know not God.\"</p><p>This future appearing — the <em>parousia</em> and <em>apokalypsis</em> — is depicted as unmistakable and universal, contrasting sharply with the hiddenness of Christ's first coming. The entire orientation of the early church was shaped by expectation of this revelation: \"looking for the blessed hope and the glorious appearing of the great God and our Saviour Jesus Christ\" (Titus 2:13).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "revelation-of-christ"},
        "key_refs": ["2 Thessalonians 1:7", "1 Corinthians 1:7", "Titus 2:13"]
    },
    "revelation-book-of": {
        "id": "revelation-book-of",
        "term": "Revelation, Book of",
        "category": "concepts",
        "intro": "<p>The Book of Revelation (also called the Apocalypse of John) is the final book of the New Testament and the only fully apocalyptic book in the Christian canon. It was written by John — most traditionally identified as the apostle John — to seven churches in the Roman province of Asia during a period of persecution, most likely in the reign of Domitian (c. 95 A.D.) or possibly Nero (c. 68 A.D.). The book opens with seven letters to the churches (chapters 2–3), followed by a heavenly throne-room vision (chapter 4), the scroll sealed with seven seals opened by the Lamb (chapters 5–8), the seven trumpet judgments (chapters 8–11), the seven bowl judgments (chapters 15–16), and culminating in the fall of Babylon, the final battle, the millennial reign, the great white throne judgment, and the new creation (chapters 17–22).</p><p>Revelation employs the language, imagery, and literary conventions of Jewish apocalyptic literature (Daniel, Ezekiel, Zechariah) to portray the cosmic conflict between God and evil, the sufferings of the faithful church, and the certain triumph of Christ and his kingdom. Its imagery is deliberately coded and symbolic rather than strictly literal. Four major interpretive frameworks have emerged in church history: preterism (fulfilled in the first century), historicism (unfolding through church history), futurism (primarily yet future), and idealism (depicting timeless spiritual realities). All traditions agree on its central claim: Christ is Lord over history and will vindicate his people.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "revelation-book-of", "smith": "revelation-book-of", "isbe": "revelation-book-of"},
        "key_refs": ["Revelation 1:1", "Revelation 1:19", "Revelation 22:20"]
    },
    "rezeph": {
        "id": "rezeph",
        "term": "Rezeph",
        "category": "places",
        "intro": "<p>Rezeph (meaning <em>pavement</em> or <em>burning coal</em>) was a city in Mesopotamia cited by the Rabshakeh (Sennacherib's representative) in his boastful challenge to Hezekiah, listing cities that Assyria had already destroyed: \"Have the gods of the nations delivered them which my fathers have destroyed; as Gozan, and Haran, and Rezeph, and the children of Eden which were in Thelasar?\" (2 Kings 19:12; Isaiah 37:12). The city was likely Rasappa, a well-known Assyrian provincial capital in northern Syria on the road between the Euphrates and Palmyra, confirming Assyria's extensive conquests west of the Euphrates.</p>",
        "hitchcock_meaning": "pavement; burning coal",
        "source_ids": {"easton": "rezeph", "smith": "rezeph"},
        "key_refs": ["2 Kings 19:12", "Isaiah 37:12"]
    },
    "rezin": {
        "id": "rezin",
        "term": "Rezin",
        "category": "people",
        "intro": "<p>Rezin (meaning <em>good-will</em> or <em>messenger</em>) was the last king of Damascus (Syria), a contemporary of Ahaz of Judah and Pekah of Israel. He allied with Pekah to invade Judah in the Syro-Ephraimite War (c. 734–732 B.C.), pressuring Ahaz to join their anti-Assyrian coalition; when Ahaz refused, they besieged Jerusalem (2 Kings 16:5; Isaiah 7:1). Isaiah delivered his famous Immanuel prophecy in this context (Isaiah 7:14). Rather than trust in God, Ahaz appealed to Tiglath-pileser III of Assyria for help; Tiglath-pileser captured Damascus and killed Rezin (2 Kings 16:9), fulfilling Isaiah's prediction that within sixty-five years Ephraim would be broken (Isaiah 7:8).</p>",
        "hitchcock_meaning": "good-will; messenger",
        "source_ids": {"easton": "rezin", "smith": "rezin", "isbe": "rezin"},
        "key_refs": ["2 Kings 15:37", "2 Kings 16:5", "Isaiah 7:1"]
    },
    "rezon": {
        "id": "rezon",
        "term": "Rezon",
        "category": "people",
        "intro": "<p>Rezon (meaning <em>lean</em>, <em>small</em>, <em>secret</em>, or <em>prince</em>) was a fugitive from Hadadezer king of Zobah who gathered a band of men around him, seized Damascus, and established himself as king there after David's defeat of Hadadezer (1 Kings 11:23–25; 2 Samuel 8:3). He became an adversary of Solomon throughout his reign, joining with Hadad the Edomite as instruments of God's judgment against Solomon's apostasy. Rezon is probably the same as the Hezion who founded the dynasty of Damascus, making him the grandfather or ancestor of Ben-hadad I (1 Kings 15:18).</p>",
        "hitchcock_meaning": "lean; small; secret; prince",
        "source_ids": {"easton": "rezon", "smith": "rezon"},
        "key_refs": ["1 Kings 11:23", "2 Samuel 8:3"]
    },
    "rhegium": {
        "id": "rhegium",
        "term": "Rhegium",
        "category": "places",
        "intro": "<p>Rhegium (meaning <em>rupture</em> or <em>fracture</em>, modern Reggio Calabria) was a Greek colonial city at the southern tip of the Italian peninsula, on the Strait of Messina opposite Sicily. It was a significant port and the natural landing point for ships rounding the toe of Italy heading north. Acts 28:13 records that Paul's ship, carrying him as a prisoner to Rome, put in at Rhegium after leaving Melita (Malta), and after waiting a day for a favorable south wind, sailed on to Puteoli — the main port for Rome's grain trade. Rhegium's position made it a major stopping point on the route between the eastern Mediterranean and Rome.</p>",
        "hitchcock_meaning": "rupture; fracture",
        "source_ids": {"easton": "rhegium", "smith": "rhegium"},
        "key_refs": ["Acts 28:13"]
    },
    "rhesa": {
        "id": "rhesa",
        "term": "Rhesa",
        "category": "people",
        "intro": "<p>Rhesa (meaning <em>will</em> or <em>course</em>) was an ancestor of Jesus in Luke's genealogy, the son of Zerubbabel and father of Joanna, in the descent traced through David (Luke 3:27). He appears only in this genealogical list. His position as son of Zerubbabel the post-exilic governor is noteworthy, as it connects the Lukan lineage through the restoration leader who led the first return from Babylon.</p>",
        "hitchcock_meaning": "will; course",
        "source_ids": {"easton": "rhesa", "smith": "rhesa"},
        "key_refs": ["Luke 3:27"]
    },
    "rhoda": {
        "id": "rhoda",
        "term": "Rhoda",
        "category": "people",
        "intro": "<p>Rhoda (meaning <em>a rose</em>) was a servant girl in the house of Mary the mother of John Mark in Jerusalem, where the early church had gathered to pray for Peter's release from prison (Acts 12:12–16). When Peter knocked at the gate after his miraculous escape, Rhoda recognized his voice and — overcome with joy — left him standing outside while she ran in to announce that Peter was at the door. The assembled believers disbelieved her, suggesting she was seeing his angel, while the persistent Peter continued knocking. The account preserves a vivid, humanizing detail: even in the circle of believers united in earnest prayer, faith was surprised by its own answered prayer.</p>",
        "hitchcock_meaning": "a rose",
        "source_ids": {"easton": "rhoda", "smith": "rhoda"},
        "key_refs": ["Acts 12:12", "Acts 12:14"]
    },
    "rhodes": {
        "id": "rhodes",
        "term": "Rhodes",
        "category": "places",
        "intro": "<p>Rhodes (meaning <em>same as Rhoda</em>, i.e., <em>a rose</em>) was a large Greek island at the southwestern tip of Asia Minor (modern Turkey), famous in antiquity for the Colossus of Rhodes — one of the Seven Wonders of the Ancient World — and as a center of commerce and culture. Acts 21:1 records that Paul's ship passed by Rhodes on his journey from Miletus to Jerusalem, stopping first at Cos and then at Rhodes before sailing to Patara. Rhodes had a significant Jewish community in the intertestamental period and was on the principal sea route between the Aegean and the eastern Mediterranean.</p>",
        "hitchcock_meaning": "same as Rhoda",
        "source_ids": {"easton": "rhodes", "smith": "rhodes"},
        "key_refs": ["Acts 21:1"]
    },
    "riblah": {
        "id": "riblah",
        "term": "Riblah",
        "category": "places",
        "intro": "<p>Riblah was an important city in the land of Hamath (Syria) in the upper Orontes valley, serving repeatedly as a military headquarters for invading powers. Pharaoh Neco imprisoned Jehoahaz there after deposing him and bound him to carry him to Egypt (2 Kings 23:33). Later, after Jerusalem fell to Babylon, Nebuchadnezzar made Riblah his field headquarters: it was there that Zedekiah, the last king of Judah, was brought before Nebuchadnezzar, had his sons killed before his eyes, was blinded, and was carried in chains to Babylon (2 Kings 25:6–7). The chief priests and officers taken at the fall of Jerusalem were also brought to Riblah and executed there (2 Kings 25:20–21). Riblah is identified with modern Ribleh on the eastern bank of the Orontes River.</p>",
        "hitchcock_meaning": "quarrel; greatness to him",
        "source_ids": {"easton": "riblah", "smith": "riblah", "isbe": "riblah"},
        "key_refs": ["2 Kings 23:33", "2 Kings 25:6", "2 Kings 25:20"]
    },
    "riddle": {
        "id": "riddle",
        "term": "Riddle",
        "category": "concepts",
        "intro": "<p>A riddle (Hebrew <em>chidah</em>, meaning a knotty or intricate problem; Greek <em>ainigma</em>) in Scripture refers to a perplexing saying, dark speech, or enigmatic question requiring skill or insight to understand. The most celebrated biblical riddle is Samson's at his wedding feast: \"Out of the eater came forth meat, and out of the strong came forth sweetness\" (Judges 14:12–18) — referring to the honey he had found in the carcass of the lion he had killed, which he framed as a wager that his Philistine companions solved only through his wife's betrayal. The Queen of Sheba came to test Solomon with riddles (1 Kings 10:1), and Ezekiel used the riddle form in his parable of the eagles (Ezekiel 17:2).</p><p>Paul uses the Greek cognate <em>ainigma</em> in his famous description of partial knowledge: \"For now we see through a glass, darkly [literally, <em>in an enigma</em>]; but then face to face\" (1 Corinthians 13:12) — contrasting the indirect, enigmatic knowledge of God available in the present age with the direct knowledge of the age to come. Numbers 12:8 establishes Moses's uniqueness by the standard that God spoke with him \"mouth to mouth, even apparently, and not in dark speeches [<em>chidot</em>].\"</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "riddle", "smith": "riddle"},
        "key_refs": ["Judges 14:12", "Ezekiel 17:2", "1 Corinthians 13:12"]
    },
    "righteousness": {
        "id": "righteousness",
        "term": "Righteousness",
        "category": "concepts",
        "intro": "<p>Righteousness (Hebrew <em>tsedaqah</em> and <em>tsedeq</em>; Greek <em>dikaiosyne</em>) is the quality of being right — conforming to the standard of what is right before God — and is one of the central categories of biblical theology. In the Old Testament, God himself is righteous: his judgments are right (Psalm 119:137), his ways are just (Deuteronomy 32:4), and his righteousness endures forever (Psalm 111:3). Human righteousness consists in conforming to the covenant obligations God has established — loving God, doing justice, keeping his commands (Deuteronomy 6:25; Micah 6:8). The prophets denounce Israel's failure of social righteousness, the perversion of justice against the poor and vulnerable.</p><p>In New Testament theology, the central question becomes how sinful humans can stand righteous before a holy God. Paul's answer in Romans and Galatians is justification by faith: God declares the believer righteous — not on the basis of law-keeping, but on the basis of faith in Christ, who bore the condemnation of sin and whose righteousness is credited (imputed) to believers (Romans 3:21–26; 4:5; 2 Corinthians 5:21). The Sermon on the Mount sets a higher righteousness that exceeds that of the scribes and Pharisees (Matthew 5:20), grounded not merely in external observance but in the transformation of the heart that the new covenant promises (Jeremiah 31:33; Ezekiel 36:26–27).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "righteousness", "isbe": "righteousness"},
        "key_refs": ["Psalms 119:137", "Romans 3:21", "2 Corinthians 5:21", "Matthew 5:20"]
    },
    "rimmon": {
        "id": "rimmon",
        "term": "Rimmon",
        "category": "people",
        "intro": "<p>Rimmon (meaning <em>exalted</em> or <em>pomegranate</em>) is used in several senses in the Old Testament. As a personal name, Rimmon of Beeroth was the father of Baanah and Rechab, the Benjaminite officers who murdered Ish-bosheth, Saul's son (2 Samuel 4:2). As a place name, Rimmon appears as a city in Zebulun (Joshua 19:13), as En-rimmon in the Negeb (Joshua 15:32; Nehemiah 11:29), and as the Rock of Rimmon, a stronghold in Benjamin where six hundred Benjaminites took refuge after the Gibeah disaster (Judges 20:45–47). As a divine name, Rimmon (or Hadad-Rimmon) was the storm deity of Syria, whose temple in Damascus Naaman the Syrian worshipped; Naaman asked Elisha's indulgence for bowing in the house of Rimmon when accompanying his king (2 Kings 5:18).</p>",
        "hitchcock_meaning": "exalted; pomegranate",
        "source_ids": {"easton": "rimmon", "smith": "rimmon"},
        "key_refs": ["2 Samuel 4:2", "2 Kings 5:18", "Judges 20:45"]
    },
    "rimmon-parez": {
        "id": "rimmon-parez",
        "term": "Rimmon-parez",
        "category": "places",
        "intro": "<p>Rimmon-parez (meaning <em>pomegranate of the breach</em> or <em>pomegranate of the pass</em>) was a station in Israel's wilderness journey, listed in Numbers 33:19–20 between Libnah and Rissah. It was one of the encampment sites during the forty years of wilderness wandering between Sinai and Moab. Its precise location in the Sinai peninsula has not been identified. The name may reflect a geographical feature — a split or gap in the terrain near which pomegranate trees grew.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rimmon-parez", "smith": "rimmon-parez"},
        "key_refs": ["Numbers 33:19", "Numbers 33:20"]
    },
    "ring": {
        "id": "ring",
        "term": "Ring",
        "category": "concepts",
        "intro": "<p>Rings in Scripture served as personal ornaments, signet seals, and symbols of authority. The signet ring was particularly significant: a king's ring impressed with his seal authenticated royal decrees, making it the ancient equivalent of an official signature. Pharaoh gave Joseph his signet ring as a sign of authority over Egypt (Genesis 41:42); Ahasuerus gave his ring to Haman and later to Mordecai for sealing royal edicts (Esther 3:10; 8:2). The prodigal son's father put a ring on his returning son's finger as a symbol of restored status in the household (Luke 15:22). The parable of the ten virgins and James's warning against showing favoritism to the man with \"a gold ring\" in the assembly (James 2:2) reflect the social status that rings conveyed.</p><p>Rings also functioned as personal adornment. Isaiah 3:21 lists rings among the ornaments God would remove from Jerusalem's daughters in judgment. Golden rings were part of the donations for the tabernacle (Exodus 35:22), and the rings used to carry the ark of the covenant and the table of showbread were integral structural elements of the sacred furniture (Exodus 25:12–15; 26–27).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ring", "smith": "ring"},
        "key_refs": ["Genesis 41:42", "Esther 3:10", "Luke 15:22", "James 2:2"]
    },
    "riphath": {
        "id": "riphath",
        "term": "Riphath",
        "category": "people",
        "intro": "<p>Riphath (meaning <em>remedy</em>, <em>medicine</em>, <em>release</em>, or <em>pardon</em>) was the second son of Gomer, himself the eldest son of Japheth the son of Noah (Genesis 10:3). He is listed in the table of nations that describes the post-Flood distribution of peoples across the earth. In the parallel list in 1 Chronicles 1:6, he is called Diphath, likely a scribal variant. Josephus identified the Riphatheans with the Paphlagonian people of Asia Minor, though this identification is uncertain. As a figure in the table of nations, Riphath represents one of the clans of the Indo-European peoples who settled north and northwest of the ancient Near East.</p>",
        "hitchcock_meaning": "remedy; medicine; release; pardon",
        "source_ids": {"easton": "riphath", "smith": "riphath"},
        "key_refs": ["Genesis 10:3"]
    },
    "rissah": {
        "id": "rissah",
        "term": "Rissah",
        "category": "places",
        "intro": "<p>Rissah (meaning <em>watering</em>, <em>distillation</em>, or <em>dew</em>) was a station in Israel's wilderness itinerary, listed in Numbers 33:21–22 between Libnah and Kehelathah. It was one of the many encampment sites during the forty years of wandering between Egypt and Canaan. Its precise location in the Sinai peninsula has not been determined. The name may suggest a place where water was found or dew collected, which would make it a significant landmark in an arid landscape.</p>",
        "hitchcock_meaning": "watering; distillation; dew",
        "source_ids": {"easton": "rissah", "smith": "rissah"},
        "key_refs": ["Numbers 33:21", "Numbers 33:22"]
    },
    "rithmah": {
        "id": "rithmah",
        "term": "Rithmah",
        "category": "places",
        "intro": "<p>Rithmah (meaning <em>juniper</em> or <em>noise</em>) was a station in Israel's wilderness journey, listed in Numbers 33:18–19 as the second encampment after Hazeroth. Some identify it with Kadesh-barnea, the major oasis from which the twelve spies were sent to reconnoiter Canaan (Numbers 13:26). The name derives from the juniper or broom tree (<em>rothem</em>), which grows abundantly in the Sinai wilderness and under which Elijah slept in his flight from Jezebel (1 Kings 19:4–5).</p>",
        "hitchcock_meaning": "juniper; noise",
        "source_ids": {"easton": "rithmah", "smith": "rithmah"},
        "key_refs": ["Numbers 33:18", "Numbers 33:19"]
    },
    "river": {
        "id": "river",
        "term": "River",
        "category": "concepts",
        "intro": "<p>Rivers in the biblical world were sources of life, fertility, and boundary-definition. The four rivers of Eden (Genesis 2:10–14) — Pishon, Gihon, Hiddekel (Tigris), and Euphrates — flowed out of the garden to water the earth, establishing the river as a symbol of divine provision and the life-giving presence of God. The Jordan was Israel's boundary and the site of crossing into the Promised Land; the Nile was Egypt's lifeblood; the Euphrates was the boundary of the Promised Land in its fullest extent (Genesis 15:18). The rivers of Assyria and Babylon represented the great world empires.</p><p>Rivers carry rich prophetic and eschatological symbolism. Ezekiel 47 envisions a river flowing from the temple that deepens as it goes and brings life to the Dead Sea. Psalm 65:9 speaks of the river of God that is full of water. Revelation 22:1–2 depicts the river of the water of life, clear as crystal, flowing from the throne of God and the Lamb through the new Jerusalem — the fulfillment of the Eden imagery and the prophetic vision of Ezekiel, bringing healing and life to the new creation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "river", "smith": "river", "isbe": "river"},
        "key_refs": ["Genesis 2:10", "Ezekiel 47:1", "Psalms 65:9", "Revelation 22:1"]
    },
    "river-of-egypt": {
        "id": "river-of-egypt",
        "term": "River of Egypt",
        "category": "places",
        "intro": "<p>The River of Egypt (Hebrew <em>nahal mitsrayim</em> or <em>nahal mitsraim</em>) designated the southwestern boundary of the Promised Land as given to Abraham (Genesis 15:18) and as described in the territory allocated to the tribe of Judah and the larger land of Israel (Numbers 34:5; Joshua 15:4, 47). It is most commonly identified with Wadi el-Arish (the \"brook of Egypt\"), a seasonal streambed that flows northward through the Sinai desert into the Mediterranean near the site of ancient Rhinocolura, approximately forty miles southwest of Gaza. This is distinct from the Nile (Ye'or), though the term is occasionally used for the Nile in other contexts.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "river-of-egypt", "smith": "river-of-egypt"},
        "key_refs": ["Genesis 15:18", "Numbers 34:5", "2 Chronicles 9:26"]
    },
    "river-of-gad": {
        "id": "river-of-gad",
        "term": "River of Gad",
        "category": "places",
        "intro": "<p>The River of Gad is mentioned only in 2 Samuel 24:5 as the starting point for Joab's census of Israel at David's command: \"They passed over Jordan, and pitched in Aroer, on the right side of the city that lieth in the midst of the river of Gad.\" The reference appears to indicate the Arnon River (Wadi Mujib), which formed the boundary between Reuben and Moab east of the Dead Sea. Aroer on the Arnon was the southernmost point of Gad's territory, making the \"river of Gad\" a designation for the Arnon in that region.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "river-of-gad"},
        "key_refs": ["2 Samuel 24:5"]
    },
    "river-of-god": {
        "id": "river-of-god",
        "term": "River of God",
        "category": "concepts",
        "intro": "<p>The River of God (Hebrew <em>nahar elohim</em>) appears in Psalm 65:9 in a hymn celebrating God's providential care for creation: \"Thou visitest the earth, and waterest it: thou greatly enrichest it with the river of God, which is full of water: thou preparest them corn, when thou hast so provided for it.\" The phrase represents the divine abundance that waters the earth and produces its harvests — the invisible channel of God's blessing that sustains all agricultural life. Genesis 2:10 describes a river going out of Eden to water the garden, and Psalm 46:4 speaks of \"a river, the streams whereof shall make glad the city of God.\" These images of the divine river converge in Ezekiel 47 and Revelation 22:1, where the river of God becomes the eschatological source of life and healing.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "river-of-god"},
        "key_refs": ["Psalms 65:9", "Genesis 2:10", "Revelation 22:1"]
    },
    "rivers-of-babylon": {
        "id": "rivers-of-babylon",
        "term": "Rivers of Babylon",
        "category": "places",
        "intro": "<p>The Rivers of Babylon appear in Psalm 137:1, one of Scripture's most poignant laments: \"By the rivers of Babylon, there we sat down, yea, we wept, when we remembered Zion.\" The rivers refer to the network of canals and waterways — branches of the Euphrates and Tigris and the irrigation canals between them — that crisscrossed the Babylonian plain. Exiled Israelites settled along these waterways (Ezekiel 1:1 speaks of Ezekiel among the exiles by the Chebar River), and the rivers of Babylon became the symbol of longing for home, for Jerusalem, and for the presence of God. The Psalm concludes with fierce imprecations against Babylon — a counterpoint to the pathos of the opening verses that has been interpreted theologically as a cry for divine justice rather than personal revenge.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rivers-of-babylon"},
        "key_refs": ["Psalms 137:1"]
    },
    "rivers-of-damascus": {
        "id": "rivers-of-damascus",
        "term": "Rivers of Damascus",
        "category": "places",
        "intro": "<p>The Rivers of Damascus — Abana and Pharpar — are mentioned in 2 Kings 5:12, where Naaman the Syrian commander, instructed by Elisha to wash seven times in the Jordan to be healed of his leprosy, protests indignantly: \"Are not Abana and Pharpar, rivers of Damascus, better than all the waters of Israel? may I not wash in them, and be clean?\" The Abana (modern Nahr Barada) was the principal river flowing through the oasis of Damascus, bringing the snowmelt of Mount Hermon through the city. The Pharpar (possibly modern Nahr el-Awaj) flowed south of Damascus. Both were clear, clean rivers supplying the fertile Damascus oasis. Naaman's servants persuaded him to comply with Elisha's instruction, and his healing exemplified that obedience to God's word matters more than the method's apparent reason.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rivers-of-damascus"},
        "key_refs": ["2 Kings 5:12"]
    },
    "rivers-of-judah": {
        "id": "rivers-of-judah",
        "term": "Rivers of Judah",
        "category": "places",
        "intro": "<p>The Rivers of Judah appear in Joel 3:18 in the eschatological vision of the restoration of Judah following the final judgment on the nations in the Valley of Jehoshaphat: \"and a fountain shall come forth of the house of the LORD, and shall water the valley of Shittim.\" The Judean highlands are relatively dry, with seasonal wadis (watercourses) that run only in winter rains; the prophetic promise of rivers watering Judah represents the transformation of the landscape in the messianic age. Amos 9:13 similarly promises that the mountains shall drip with sweet wine and the hills shall flow with it. Both prophecies reflect the eschatological renewal of creation and the abundant blessing that characterizes the restored covenant community.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rivers-of-judah"},
        "key_refs": ["Joel 3:18"]
    },
    "rizpah": {
        "id": "rizpah",
        "term": "Rizpah",
        "category": "people",
        "intro": "<p>Rizpah (meaning <em>a bed</em>, <em>extension</em>, or <em>a coal</em>) was a concubine of Saul, daughter of Aiah. After Saul's death, Abner's possession of her became the occasion of a political quarrel with Ish-bosheth, Saul's surviving son (2 Samuel 3:7) — in the ancient world, acquiring a former king's concubine implied a claim to royal succession. The more memorable episode involving Rizpah came years later when David surrendered seven of Saul's descendants to the Gibeonites to atone for Saul's massacre of their people (2 Samuel 21:8–9).</p><p>Rizpah then performed one of Scripture's most striking acts of maternal devotion: she spread sackcloth on a rock and kept watch over the exposed bodies of the seven men from the beginning of the barley harvest through the rains — protecting them from birds by day and wild animals by night (2 Samuel 21:10). When David heard of her vigil, he was moved to retrieve the bones of Saul and Jonathan from Jabesh-gilead and bury all of them honorably in the family tomb. Her faithfulness prompted David's act of covenant faithfulness, and the land was thereafter appeased.</p>",
        "hitchcock_meaning": "bed; extension; a coal",
        "source_ids": {"easton": "rizpah", "smith": "rizpah", "isbe": "rizpah"},
        "key_refs": ["2 Samuel 3:7", "2 Samuel 21:10"]
    },
    "road": {
        "id": "road",
        "term": "Road",
        "category": "concepts",
        "intro": "<p>The word \"road\" in the KJV Old Testament appears only once in its modern sense, in 1 Samuel 27:10, where Achish asks David \"whither have ye made a road today?\" — using \"road\" in the older English sense of a raid or foray. In the ancient Near East, roads were not paved highways but beaten paths, trade routes, and military roads that connected cities and regions. The Romans later built an extraordinary network of paved roads throughout the empire — the <em>viae</em> — which facilitated the rapid spread of the gospel in the first century (Acts 28; Romans 15:19). The Old Testament speaks of \"the way\" (Hebrew <em>derek</em>) extensively, both literally and theologically: Israel traveled the way of the wilderness, the king's highway, and the way of Shur; God's ways are above human ways (Isaiah 55:8–9), and the path of righteousness is the way of life (Proverbs 12:28).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "road", "smith": "road"},
        "key_refs": ["1 Samuel 27:10", "Isaiah 40:3", "John 14:6"]
    },
    "robbery": {
        "id": "robbery",
        "term": "Robbery",
        "category": "concepts",
        "intro": "<p>Robbery — the violent seizure of another's property — is consistently condemned in Scripture as a violation of both God's law and human dignity. The eighth commandment (\"Thou shalt not steal,\" Exodus 20:15) extends to violent seizure as well as theft; the Levitical code explicitly prohibits robbery (Leviticus 19:13). The prophets repeatedly cite robbery as evidence of Israel's covenant unfaithfulness: Amos condemns those who store up violence and robbery in their strongholds (Amos 3:10), and Ezekiel lists robbery as among the sins of the violent man who sheds blood (Ezekiel 22:29). The prevalence of robbery in the wilderness reflects the context of the Ishmaelite traders who carried Joseph to Egypt (Genesis 37:25) and the Sabean and Chaldean raiders who plundered Job (Job 1:15–17).</p><p>Isaiah 61:8 grounds God's opposition to robbery in his character: \"For I the LORD love judgment, I hate robbery for burnt offering\" — divine love of justice excludes accepting worship built on exploitation. Proverbs 21:7 declares that the violence of the wicked will destroy them, since they refuse to do justice.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "robbery", "smith": "robbery"},
        "key_refs": ["Leviticus 19:13", "Amos 3:10", "Isaiah 61:8"]
    },
    "rock": {
        "id": "rock",
        "term": "Rock",
        "category": "concepts",
        "intro": "<p>Rock (Hebrew <em>tsur</em> and <em>sela</em>; Greek <em>petra</em>) functions in Scripture both as a geographical reality and as one of the most theologically rich images for God. Limestone and sandstone cliffs, gorges, and outcroppings characterize the landscapes of Canaan, Sinai, and Transjordan, providing both shelter and danger. The rock at Horeb from which Moses struck water for Israel (Exodus 17:6; Numbers 20:11) is interpreted typologically by Paul: \"that Rock was Christ\" (1 Corinthians 10:4), the spiritual drink from which Israel's wilderness generation drank following the presence of God.</p><p>God himself is called the Rock throughout the Old Testament: \"The LORD is my rock, and my fortress, and my deliverer\" (2 Samuel 22:2; Psalm 18:2); \"Who is God save the LORD? or who is a rock save our God?\" (2 Samuel 22:32). The Psalms repeatedly celebrate God as the rock of refuge and salvation (Psalms 31:2; 62:2; 95:1). In the New Testament, Jesus builds his community on the <em>petra</em> (Matthew 16:18) and compares those who hear and obey his words to those who build on rock rather than sand (Matthew 7:24–25). Isaiah's prophecy of the precious cornerstone laid in Zion (Isaiah 28:16) is applied to Christ in 1 Peter 2:6–8.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rock", "smith": "rock", "isbe": "rock"},
        "key_refs": ["2 Samuel 22:2", "Exodus 17:6", "1 Corinthians 10:4", "Matthew 16:18"]
    },
    "roe": {
        "id": "roe",
        "term": "Roe",
        "category": "concepts",
        "intro": "<p>The roe (Hebrew <em>tsevi</em> or <em>tsebi</em>, also rendered gazelle) was a swift, graceful deer-like animal common in the hills of Canaan and celebrated in Scripture for its beauty and speed. It was among the clean animals permitted for food (Deuteronomy 12:15; 14:5) and was listed among the provisions for Solomon's table (1 Kings 4:23). The roe appears most memorably in the Song of Solomon, where the beloved's lover is compared to a roe or young hart leaping upon the mountains (Song of Solomon 2:9, 17; 8:14) — an image of eager, joyful approach. In Proverbs 5:19, a faithful wife is compared to \"a loving hind and pleasant roe.\" The speed of the roe also appears in military imagery: Asahel, Joab's brother, was fleet-footed \"as a wild roe\" (2 Samuel 2:18).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "roe", "smith": "roe"},
        "key_refs": ["Deuteronomy 14:5", "Song of Solomon 2:9", "2 Samuel 2:18"]
    },
    "rogelim": {
        "id": "rogelim",
        "term": "Rogelim",
        "category": "places",
        "intro": "<p>Rogelim (meaning <em>a foot</em> or <em>footman</em>, perhaps referring to fullers' treading cloth) was a city in Gilead east of the Jordan, the home of Barzillai the Gileadite, who provided food and supplies to David and his army when they fled to Mahanaim during Absalom's revolt (2 Samuel 17:27). After Absalom's defeat, Barzillai came from Rogelim to escort the king back over the Jordan, declining David's invitation to come to Jerusalem — saying he was eighty years old and would be a burden — but sending his son Chimham in his place (2 Samuel 19:31–38). Rogelim's precise location has not been identified with certainty.</p>",
        "hitchcock_meaning": "a foot or footman",
        "source_ids": {"easton": "rogelim", "smith": "rogelim"},
        "key_refs": ["2 Samuel 17:27", "2 Samuel 19:31"]
    },
    "roll": {
        "id": "roll",
        "term": "Roll",
        "category": "concepts",
        "intro": "<p>A roll (Hebrew <em>megillah</em>; Greek <em>biblion</em> or <em>tomos</em>) was a scroll — a manuscript written on papyrus, leather, or vellum wound around a central stick and unrolled for reading. Before the codex (book) form became common in the second century A.D., rolls were the standard form for both literary and official documents throughout the ancient Near East and Mediterranean world. Ezra 6:2 records a \"roll\" of official records found at Ecbatana. Jeremiah dictated his prophecies to Baruch, who wrote them on a roll (<em>megillah</em>) that was read publicly and then burned by King Jehoiakim (Jeremiah 36:2–28). Psalm 40:7 speaks of the coming Servant of the LORD: \"in the volume of the book it is written of me\" — applied in Hebrews 10:7 to Christ's coming to do God's will.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "roll", "smith": "roll"},
        "key_refs": ["Ezra 6:2", "Psalms 40:7", "Jeremiah 36:2", "Hebrews 10:7"]
    },
    "romamti-ezer": {
        "id": "romamti-ezer",
        "term": "Romamti-ezer",
        "category": "people",
        "intro": "<p>Romamti-ezer (meaning <em>exaltation of help</em>) was one of the sons of Heman, David's seer, appointed as a Levitical musician for the temple service. His name appears in the list of Heman's fourteen sons (1 Chronicles 25:4), all of whose names together may form a fragmentary liturgical text. He was assigned by lot to lead the twenty-fourth division of the temple musicians (1 Chronicles 25:31), with his sons and brothers — twelve in all — making up the company who served during that appointed week of worship.</p>",
        "hitchcock_meaning": "exaltation of help",
        "source_ids": {"easton": "romamti-ezer", "smith": "romamti-ezer"},
        "key_refs": ["1 Chronicles 25:4", "1 Chronicles 25:31"]
    },
    "romans-epistle-to-the": {
        "id": "romans-epistle-to-the",
        "term": "Romans, Epistle to the",
        "category": "concepts",
        "intro": "<p>The Epistle to the Romans is Paul's longest and most systematically theological letter, addressed to the church in Rome, which Paul had not yet visited when he wrote it (c. 57 A.D.) from Corinth. It is the opening epistle of the Pauline corpus in the New Testament canon. Romans is widely regarded as the fullest exposition of Paul's gospel and of Christian theology in the New Testament: it develops the doctrines of sin (chapters 1–3), justification by faith (chapters 3–5), sanctification and the Spirit (chapters 6–8), God's faithfulness in the election of Israel (chapters 9–11), and the ethical imperatives of the renewed life (chapters 12–15).</p><p>Romans 3:21–26 contains one of the most concentrated statements of atonement theology in the Bible: God set forth Christ as a propitiation to demonstrate his righteousness and to justify those who have faith in Jesus. Chapters 9–11 address the mystery of Israel's partial hardening and the hope of their future restoration. The letter has exercised enormous influence on Christian theology: its rediscovery by Augustine shaped Western theology; Luther's recognition that the righteousness of Romans 1:17 is the righteousness God gives rather than demands ignited the Reformation; and Karl Barth's commentary on Romans reshaped twentieth-century Protestant theology.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "romans-epistle-to-the", "smith": "romans-epistle-to-the", "isbe": "romans-epistle-to-the"},
        "key_refs": ["Romans 1:17", "Romans 3:21", "Romans 8:1", "Romans 11:26"]
    },
    "rome": {
        "id": "rome",
        "term": "Rome",
        "category": "places",
        "intro": "<p>Rome (meaning <em>strength</em> or <em>power</em>) was the capital of the Roman Empire, situated on the Tiber River in central Italy, and the political center of the world in which the New Testament was written. Founded, according to tradition, in 753 B.C., Rome had by the first century A.D. grown into a city of perhaps one million inhabitants, the hub of an empire stretching from Britain to Mesopotamia. For the New Testament church, Rome was both destination and symbol: Paul's burning ambition was to preach the gospel in Rome (Romans 1:15; 15:23–24), and his eventual arrival there — as a prisoner who preached for two years \"with all confidence, no man forbidding him\" (Acts 28:30–31) — represents the fulfillment of the gospel's spread from Jerusalem to the ends of the earth (Acts 1:8).</p><p>A Jewish community had existed in Rome since the second century B.C., and Christians were present there by the early 40s. Claudius had expelled Jews from Rome (Acts 18:2), and Nero's persecution of Christians following the great fire of 64 A.D. provides the context for Peter's and Paul's martyrdoms in Rome. Revelation's Babylon is widely interpreted as a coded reference to Rome — the great city that sat on seven hills, drunk with the blood of the saints (Revelation 17:5–6, 9).</p>",
        "hitchcock_meaning": "strength; power",
        "source_ids": {"easton": "rome", "smith": "rome", "isbe": "rome"},
        "key_refs": ["Acts 28:30", "Romans 1:15", "Revelation 17:9"]
    },
    "rose": {
        "id": "rose",
        "term": "Rose",
        "category": "concepts",
        "intro": "<p>The rose of Scripture (Hebrew <em>chabasseleth</em>) is not certainly identified with the cultivated rose but most likely refers to a bulbous flowering plant of the crocus or narcissus family — possibly the meadow saffron or asphodel — that bloomed in the plains and valleys of Israel. Song of Solomon 2:1 opens with the beloved's self-description: \"I am the rose of Sharon, and the lily of the valleys\" — language of beauty and fragrant delicacy set in the fertile plain of Sharon along the Mediterranean coast. Isaiah 35:1 uses the same word to promise that the wilderness will rejoice and blossom as the rose in the day of messianic restoration. The imagery passed into Christian tradition, where \"the rose of Sharon\" became a devotional title for Christ.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rose", "smith": "rose"},
        "key_refs": ["Song of Solomon 2:1", "Isaiah 35:1"]
    },
    "rosh": {
        "id": "rosh",
        "term": "Rosh",
        "category": "people",
        "intro": "<p>Rosh (meaning <em>the head</em>, <em>top</em>, or <em>beginning</em>) is the name of a son of Benjamin listed among those who went down to Egypt with Jacob (Genesis 46:21). He is not listed among Benjamin's sons in Numbers 26:38–40 or 1 Chronicles 8, suggesting either early death without descendants or a textual variant. Rosh also appears in Ezekiel 38:2–3 and 39:1 in the Hebrew phrase <em>nesi rosh meshech</em> — translated either as \"prince of Rosh, Meshech, and Tubal\" or as \"chief prince of Meshech and Tubal\" (where <em>rosh</em> is an adjective meaning <em>chief</em> rather than a proper name). Whether Rosh in Ezekiel denotes a distinct nation or simply the title \"chief\" is a major question in the interpretation of Ezekiel 38–39.</p>",
        "hitchcock_meaning": "the head; top, or beginning",
        "source_ids": {"easton": "rosh", "smith": "rosh"},
        "key_refs": ["Genesis 46:21", "Ezekiel 38:2"]
    },
    "rosin": {
        "id": "rosin",
        "term": "Rosin",
        "category": "concepts",
        "intro": "<p>Rosin (also resin; Hebrew <em>neophet</em> or possibly <em>tsori</em>) refers to the resinous gum or balm extracted from various trees. In Ezekiel 27:17, Israel and Judah are listed among the trading partners of Tyre, exporting wheat, honey, oil, and \"Pannag, and honey, and oil, and balm\" — the Hebrew <em>tsori</em> often translated as balm or rosin. The balm of Gilead (Jeremiah 8:22) was also a resinous product prized for its medicinal properties. Resin was used in ancient times as a preservative, sealant, incense ingredient, and trade commodity. The precise identification of the Hebrew terms with specific resinous substances remains uncertain.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rosin", "smith": "rosin"},
        "key_refs": ["Ezekiel 27:17"]
    },
    "ruby": {
        "id": "ruby",
        "term": "Ruby",
        "category": "concepts",
        "intro": "<p>Ruby (Hebrew <em>odem</em> or <em>peninim</em>, the precise identification uncertain) was among the precious stones valued in the ancient Near East. The first stone in the high priest's breastplate (Exodus 28:17) was an <em>odem</em>, traditionally translated ruby or carnelian, set in the first row. Lamentations 4:7 compares the Nazarites, whose bodies had been more ruddy than rubies (<em>peninim</em>), in their former purity, with their darkened state in the desolation of the exile. Proverbs 3:15 and 8:11 use rubies as the measure against which wisdom is incomparably greater: \"She is more precious than rubies: and all the things thou canst desire are not to be compared unto her.\" The precise identification of the Hebrew gemstone terms with modern stones remains debated by scholars.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ruby", "smith": "ruby"},
        "key_refs": ["Exodus 28:17", "Proverbs 3:15", "Lamentations 4:7"]
    },
    "rudder-bands": {
        "id": "rudder-bands",
        "term": "Rudder bands",
        "category": "concepts",
        "intro": "<p>Rudder bands (Greek <em>ta zeuktheria ton pederion</em>) appear in Acts 27:40 in the account of Paul's shipwreck off Malta. Ancient Mediterranean ships used steering oars — large paddles mounted at the stern — rather than a single central rudder; in storms, these oars were lashed up out of the water to prevent damage. As the crew attempted to beach the ship at Malta, they \"loosed the rudder bands, and hoised up the mainsail to the wind, and made toward shore.\" Freeing the rudder bands allowed the steering oars to drop back into the water so the helmsmen could guide the ship toward the beach. The technical detail reflects the accuracy of the Acts narrative as an eyewitness account of ancient seamanship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rudder-bands"},
        "key_refs": ["Acts 27:40"]
    },
    "rue": {
        "id": "rue",
        "term": "Rue",
        "category": "concepts",
        "intro": "<p>Rue (Greek <em>peganon</em>) was a strongly scented Mediterranean herb (<em>Ruta graveolens</em>) cultivated in gardens and used medicinally, culinarily, and as a bitter flavoring. In Luke 11:42, Jesus rebukes the Pharisees for tithing mint, rue, and all manner of herbs while passing over judgment and the love of God: \"These ought ye to have done, and not to leave the other undone.\" The Matthean parallel (Matthew 23:23) lists mint, anise, and cummin rather than rue. That Pharisees tithed garden herbs including rue reflects the strict tithing practice that extended even to kitchen herbs, a meticulousness that became a substitute for, rather than an expression of, genuine covenant faithfulness.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rue", "smith": "rue"},
        "key_refs": ["Luke 11:42", "Matthew 23:23"]
    },
    "rufus": {
        "id": "rufus",
        "term": "Rufus",
        "category": "people",
        "intro": "<p>Rufus (Latin meaning <em>red</em>) is mentioned in two New Testament passages. In Mark 15:21, Simon of Cyrene, compelled to carry Jesus's cross, is identified as \"the father of Alexander and Rufus\" — suggesting that Rufus was well known to Mark's Roman audience when the Gospel was written. In Romans 16:13, Paul greets \"Rufus chosen in the Lord, and his mother and mine\" — indicating both that Rufus was an eminent member of the Roman church and that his mother had shown maternal care to Paul. These two references are commonly connected, suggesting that the Rufus whose father carried Christ's cross later became a significant figure in the church at Rome, with Paul having a personal relationship with his family.</p>",
        "hitchcock_meaning": "red",
        "source_ids": {"easton": "rufus", "smith": "rufus"},
        "key_refs": ["Mark 15:21", "Romans 16:13"]
    },
    "ruhamah": {
        "id": "ruhamah",
        "term": "Ruhamah",
        "category": "people",
        "intro": "<p>Ruhamah (meaning <em>having obtained mercy</em> or <em>pitied</em>) is not a personal name of an individual but a symbolic name in Hosea's prophecy. God commanded Hosea to name his daughter Lo-ruhamah (<em>not pitied</em>) as a sign that God would no longer have mercy on Israel (Hosea 1:6). The reversal of this name — Ruhamah — is announced in Hosea 2:23 as the future promise of restoration: \"I will have mercy upon her that had not obtained mercy; and I will say to them which were not my people, Thou art my people.\" Paul applies this oracle directly to the calling of both Jews and Gentiles into the new covenant people of God (Romans 9:25), making Hosea's symbolic naming of his daughter a prophecy of the scope of divine mercy in the gospel age.</p>",
        "hitchcock_meaning": "having obtained mercy",
        "source_ids": {"easton": "ruhamah", "smith": "ruhamah"},
        "key_refs": ["Hosea 1:6", "Hosea 2:23", "Romans 9:25"]
    },
    "rumah": {
        "id": "rumah",
        "term": "Rumah",
        "category": "places",
        "intro": "<p>Rumah (meaning <em>exalted</em>, <em>sublime</em>, or <em>rejected</em>) was the home of Pedaiah, whose daughter Zebudah was the mother of Jehoiakim, the son of Josiah and king of Judah (2 Kings 23:36). It may be identified with Arumah near Shechem, mentioned in Judges 9:41, or possibly with a site in the vicinity of Galilee. The name appears only in the brief genealogical reference to Jehoiakim's maternal family, which was a common practice in the introductions to the reigns of Judean kings.</p>",
        "hitchcock_meaning": "exalted; sublime; rejected",
        "source_ids": {"easton": "rumah", "smith": "rumah"},
        "key_refs": ["2 Kings 23:36", "Judges 9:41"]
    },
    "rush": {
        "id": "rush",
        "term": "Rush",
        "category": "concepts",
        "intro": "<p>Rush (Hebrew <em>gome</em> or <em>agmon</em>) refers to the bulrush and reed plants that grew in marshy areas and along riverbanks throughout the biblical world. Job 8:11 asks rhetorically, \"Can the rush grow up without mire? can the flag grow without water?\" — using the waterside reed as an image of what cannot exist without its proper environment, applied to the impossibility of the godless man prospering without God. Isaiah 9:14 uses the figure of head and tail, palm branch and rush, for the leaders and prophets of Israel. Isaiah 19:15 employs the same contrast for Egypt. In Isaiah 58:5, bowing down the head \"as a bulrush\" describes a merely external, performative fast without genuine humility of heart.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rush", "smith": "rush"},
        "key_refs": ["Job 8:11", "Isaiah 9:14", "Isaiah 58:5"]
    },
    "ruth": {
        "id": "ruth",
        "term": "Ruth",
        "category": "people",
        "intro": "<p>Ruth (meaning <em>friend</em> or <em>companion</em>; the Hitchcock tradition connects it to <em>drunk</em> or <em>satisfied</em>) was a Moabite woman who became one of the most beloved figures in Scripture. After the death of her Israelite husband in Moab, she refused to leave her mother-in-law Naomi when Naomi decided to return to Bethlehem, declaring in one of Scripture's most celebrated speeches of loyalty: \"Whither thou goest, I will go; and where thou lodgest, I will lodge: thy people shall be my people, and thy God my God\" (Ruth 1:16). This declaration of covenant loyalty to Naomi and to Israel's God makes Ruth a model of loving faithfulness (<em>hesed</em>).</p><p>In Bethlehem, Ruth's humble gleaning in the fields of Boaz — Naomi's kinsman-redeemer — led to their marriage, and their son Obed became the grandfather of David. Ruth appears in Matthew's genealogy of Jesus (Matthew 1:5), one of only four women named, each in some way surprising: Ruth the Moabite, by grace and covenant loyalty, became an ancestor of both David and the Messiah. Her story illustrates that God's covenant mercy extends across ethnic boundaries and that the God of Israel receives all who take refuge under his wings (Ruth 2:12).</p>",
        "hitchcock_meaning": "drunk; satisfied",
        "source_ids": {"easton": "ruth", "smith": "ruth", "isbe": "ruth"},
        "key_refs": ["Ruth 1:16", "Ruth 2:12", "Ruth 4:17", "Matthew 1:5"]
    },
    "ruth-the-book-of": {
        "id": "ruth-the-book-of",
        "term": "Ruth The Book of",
        "category": "concepts",
        "intro": "<p>The Book of Ruth is a short narrative in the Hebrew canon placed among the Writings (<em>Ketuvim</em>) and read at the Feast of Weeks (Pentecost); in the Christian Old Testament it appears between Judges and 1 Samuel. It is set in the period of the judges (Ruth 1:1) and recounts the story of Ruth the Moabite widow, her mother-in-law Naomi, and the kinsman-redeemer Boaz. The book is notable for its literary beauty, its portrayal of steadfast covenant love (<em>hesed</em>), and its genealogical conclusion connecting the story to David (Ruth 4:17–22).</p><p>Theologically, Ruth demonstrates God's providential care for the faithful, the extension of covenant mercy to Gentiles who shelter under God's wings, and the institution of the kinsman-redeemer (<em>go'el</em>) — a figure who redeems family property and protects the vulnerable. Boaz as kinsman-redeemer has long been read as a type of Christ, who redeems his people at cost to himself and restores them to their inheritance. The book also challenges the narrow ethnic reading of Israel's covenant by presenting Ruth's loyalty and Boaz's integrity as the means by which God provided the ancestor of his greatest king — and ultimately of the Messiah.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ruth-the-book-of", "smith": "ruth-the-book-of", "isbe": "ruth-the-book-of"},
        "key_refs": ["Ruth 1:1", "Ruth 2:12", "Ruth 4:14", "Matthew 1:5"]
    },
    "rye": {
        "id": "rye",
        "term": "Rye",
        "category": "concepts",
        "intro": "<p>Rye (Hebrew <em>kussemeth</em>) appears in several passages of the Old Testament, usually translated as \"rye\" or \"fitches\" in older versions and as \"spelt\" in most modern translations. Spelt (<em>Triticum spelta</em>) was an ancient hulled wheat cultivated throughout the ancient Near East, hardier and more resistant to poor conditions than common wheat. In Exodus 9:32, the plague of hail destroyed the barley and flax but not the wheat and spelt, because they were late-maturing crops. Isaiah 28:25 mentions spelt as one of the grains the skilled farmer sows in its proper place. Ezekiel 4:9 includes spelt among the mixed grains used to make bread during the symbolic siege of Jerusalem. Spelt was a staple grain of the ancient world, occupying a lower status than wheat in most contexts.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rye", "smith": "rye"},
        "key_refs": ["Exodus 9:32", "Isaiah 28:25", "Ezekiel 4:9"]
    },
}


def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP r2: Resurrection of the dead → Rye: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
