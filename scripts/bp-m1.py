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
  'maachah': {
    'id': 'maachah', 'term': 'Maachah', 'category': 'people',
    'intro': '<p>Maachah (meaning: <em>pressed down; worn; fastened</em>) is the name of several persons and a small Aramean kingdom in the Old Testament. As a kingdom, Aram-Maachah was a small state northeast of Bashan near Mount Hermon whose forces joined the Ammonite coalition against David and were defeated by Joab. As a personal name it was borne by a wife of Nahor, Abraham\'s brother; a concubine of Caleb; the mother of Absalom (daughter of Talmai, king of Geshur); the favorite wife of Rehoboam and mother of Abijam; and several men including the father of Achish of Gath and the father of one of David\'s mighty men.</p>',
    'sections': [], 'hitchcock_meaning': 'pressed down; worn; fastened', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Joshua 13:13', '2 Samuel 10:6', '1 Chronicles 19:7']
  },
  'maaleh-acrabbim': {
    'id': 'maaleh-acrabbim', 'term': 'Maaleh-acrabbim', 'category': 'places',
    'intro': '<p>Maaleh-acrabbim, meaning "Ascent of Akrabbim" or "Scorpion Pass," was a steep mountain pass forming part of the southern boundary of Canaan as described in Numbers 34:4 and the territory of Judah in Joshua 15:3. It lay south of the Dead Sea at the northern edge of the Wilderness of Zin, and the name may reflect the abundance of scorpions in the region. The pass is identified with the modern Naqb es-Safa, a significant route between the Negev and the Arabah south of the Dead Sea.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Numbers 34:4', 'Joshua 15:3']
  },
  'maarath': {
    'id': 'maarath', 'term': 'Maarath', 'category': 'places',
    'intro': '<p>Maarath (meaning: <em>den; making empty; watching</em>) was a town in the hill country of Judah, listed in the tribal allotments of Joshua 15:59 alongside Bethlehem and Peor. Its precise location is uncertain, but it lay in the highlands southwest of Jerusalem. The town is mentioned only once and does not appear in later biblical narratives, making its identification dependent entirely on the boundary and city lists of Joshua.</p>',
    'sections': [], 'hitchcock_meaning': 'den; making empty; watching', 'source_ids': ['easton'],
    'key_refs': ['Joshua 15:59']
  },
  'maaseiah': {
    'id': 'maaseiah', 'term': 'Maaseiah', 'category': 'people',
    'intro': '<p>Maaseiah (meaning: <em>the work of the Lord</em>) is one of the most common names in the Old Testament, shared by at least twenty different individuals. Among the most notable: a Levite musician appointed by David for the ark processional; an army officer who helped Jehoiada the priest install Joash as king; a son of Ahaz king of Judah who was killed by Zichri; a priest who stood beside Ezra during the public reading of the law; and several priests and laymen who had married foreign women and separated from them during Ezra\'s reform. The name\'s frequency reflects its meaning — a testimony to the Lord\'s work in a person\'s life.</p>',
    'sections': [], 'hitchcock_meaning': 'the work of the Lord', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Chronicles 15:18', '2 Chronicles 23:1', '2 Chronicles 28:7', 'Nehemiah 8:4']
  },
  'maasiai': {
    'id': 'maasiai', 'term': 'Maasiai', 'category': 'people',
    'intro': '<p>Maasiai (meaning: <em>the defense, or strength, or trust of the Lord</em>) was a priest of the house of Immer who settled in Jerusalem after the return from Babylon. He is listed in the genealogy of priests who took up residence in the holy city during the restoration period recorded in 1 Chronicles 9:12. The name is a variant of Maaseiah and reflects the same theological meaning — trust in the Lord\'s strength and protection.</p>',
    'sections': [], 'hitchcock_meaning': 'the defense, or strength, or trust of the Lord', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Chronicles 9:12']
  },
  'maath': {
    'id': 'maath', 'term': 'Maath', 'category': 'people',
    'intro': '<p>Maath (meaning: <em>wiping away; breaking; fearing; smiting</em>) was an ancestor of Jesus Christ listed in Luke\'s genealogy between Mattathias and Naggai, in the line from David through Nathan rather than Solomon. Luke 3:26 is the only biblical reference to this name. As with many figures in Luke\'s genealogy, nothing further is recorded about Maath in Scripture.</p>',
    'sections': [], 'hitchcock_meaning': 'wiping away; breaking; fearing; smiting', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Luke 3:26']
  },
  'maaziah': {
    'id': 'maaziah', 'term': 'Maaziah', 'category': 'people',
    'intro': '<p>Maaziah is the name of two men in the post-exilic period. The first was the head of the twenty-fourth and last division of priests organized by David for the temple service; his family served in the final rotation of the twenty-four priestly courses. The second Maaziah was a priest who set his seal to the covenant of reform under Nehemiah, pledging to observe the law of God and separate the community from foreign entanglements. Both are mentioned exclusively in the restoration-era texts of Chronicles and Nehemiah.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Chronicles 24:18', 'Nehemiah 10:8']
  },
  'maccabees': {
    'id': 'maccabees', 'term': 'Maccabees', 'category': 'people',
    'intro': '<p>The Maccabees were a Jewish priestly family who led the successful revolt against the Seleucid king Antiochus IV Epiphanes (175–164 B.C.) after he desecrated the Jerusalem temple and attempted to suppress Jewish religious practice. The name derives either from the Aramaic for "hammer" (applied to Judas the first great leader) or from a Hebrew acronym. After Judas Maccabeus recaptured and rededicated the temple in 164 B.C. — the event commemorated in Hanukkah — his brothers Simon and Jonathan continued the struggle, eventually establishing the Hasmonean dynasty that ruled Judea until the Roman conquest under Pompey in 63 B.C.</p><p>Though the Maccabean revolt is not narrated in the canonical Hebrew Bible, the intertestamental period it defined shaped the political and religious landscape of the New Testament world.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Daniel 11:32', 'Hebrews 11:34']
  },
  'maccabees-books-of-the': {
    'id': 'maccabees-books-of-the', 'term': 'Maccabees, Books of the', 'category': 'concepts',
    'intro': '<p>The Books of the Maccabees are four works describing the Maccabean revolt and the Hasmonean period. First Maccabees (in the Deuterocanon/Apocrypha) is a historical account of the revolt from approximately 175–134 B.C., considered reliable by many historians. Second Maccabees covers a shorter period with greater theological and miraculous emphasis, introducing the doctrine of resurrection and prayers for the dead. Third and Fourth Maccabees, found in some traditions, address the persecution of Jews in Egypt and the philosophy of reason mastering passion respectively.</p><p>First and Second Maccabees are included in the Catholic and Eastern Orthodox Old Testament canons but are regarded as apocryphal by Protestant traditions. They provide crucial background for understanding the Judaism Jesus encountered.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['1 Maccabees 1:1', '2 Maccabees 7:9']
  },
  'macedonia': {
    'id': 'macedonia', 'term': 'Macedonia', 'category': 'places',
    'intro': '<p>Macedonia (meaning: <em>burning; adoration</em>) was a kingdom and Roman province in the northern Aegean region corresponding to modern northern Greece, home to Philippi, Thessalonica, and Berea. Paul\'s mission to Macedonia began with a vision of a Macedonian man pleading for him to "come over and help us," which the apostle understood as a divine call directing the gospel into Europe. The Macedonian churches — notably at Philippi and Thessalonica — became models of generosity, contributing abundantly to Paul\'s collection for Jerusalem despite their own poverty.</p><p>Paul traveled through Macedonia several times, and his letters to the Philippians and Thessalonians address Macedonian congregations. The Macedonian Christians\' eagerness and the churches\' faithfulness made them a source of encouragement to Paul throughout his ministry.</p>',
    'sections': [], 'hitchcock_meaning': 'burning; adoration', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Acts 16:9', 'Romans 15:26', '2 Corinthians 8:1', '2 Corinthians 9:2']
  },
  'machaerus': {
    'id': 'machaerus', 'term': 'Machaerus', 'category': 'places',
    'intro': '<p>Machaerus was a Herodian fortress-palace built by Herod the Great on a rocky promontory east of the Dead Sea in the territory of Perea, overlooking the Arnon gorge. Josephus identifies it as the place where John the Baptist was imprisoned and executed at the command of Herod Antipas, after John rebuked Herod\'s marriage to Herodias. The fortress combined military strength with palatial luxury, and its remote location east of the Jordan made it a secure prison for political and religious prisoners. Archaeological excavations have confirmed the site at modern Mukawir in Jordan.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Mark 6:14', 'Matthew 14:3', 'Luke 3:19']
  },
  'machbanai': {
    'id': 'machbanai', 'term': 'Machbanai', 'category': 'people',
    'intro': '<p>Machbanai was a Gadite warrior who came to David at Ziklag while David was restricted in his movements because of Saul, joining the growing band of mighty men who supported David\'s cause. He is listed eleventh among the Gadite captains who crossed the Jordan in the first month when it was at flood stage and joined David\'s forces. Beyond this mention in 1 Chronicles 12:13, nothing further is recorded about him.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Chronicles 12:13']
  },
  'machir': {
    'id': 'machir', 'term': 'Machir', 'category': 'people',
    'intro': '<p>Machir (meaning: <em>selling; knowing</em>) was the firstborn son of Manasseh by his Aramean concubine, and the father of Gilead, from whom the territory of Gilead took its name. Machir was a man of war and the Machirites received the territories of Gilead and Bashan east of the Jordan as their tribal allotment. A second Machir, the son of Ammiel from Lo-debar, showed kindness to Mephibosheth, Jonathan\'s lame son, and later brought supplies to David at Mahanaim during Absalom\'s revolt.</p>',
    'sections': [], 'hitchcock_meaning': 'selling; knowing', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Joshua 17:1', 'Numbers 26:29', '2 Samuel 9:4', '2 Samuel 17:27']
  },
  'machpelah': {
    'id': 'machpelah', 'term': 'Machpelah', 'category': 'places',
    'intro': '<p>Machpelah (meaning: <em>double</em>) was the field and cave near Hebron purchased by Abraham from Ephron the Hittite as a burial place for Sarah. The transaction is recorded in meticulous detail in Genesis 23, making it Israel\'s first legally acquired foothold in Canaan. The cave became the patriarchal tomb: Abraham himself, Isaac and Rebekah, Jacob and Leah were all buried there. Only Rachel, who died on the road to Bethlehem, was buried elsewhere.</p><p>The site is identified with the Cave of Machpelah beneath the great Herodian enclosure in Hebron — the Ibrahimi Mosque/Cave of the Patriarchs — one of the most ancient and contested holy sites in the Middle East, venerated by Jews, Christians, and Muslims.</p>',
    'sections': [], 'hitchcock_meaning': 'double', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 23:19', 'Genesis 25:9', 'Genesis 49:31', 'Genesis 50:13']
  },
  'madai': {
    'id': 'madai', 'term': 'Madai', 'category': 'people',
    'intro': '<p>Madai (meaning: <em>a measure; judging; a garment</em>) was the third son of Japheth in the Table of Nations in Genesis 10:2, and is the ancestor of the Medes (<em>Madai</em> in Hebrew). The Medes were an Indo-European people who settled in the mountainous region south of the Caspian Sea corresponding to modern northwestern Iran. They conquered Assyria in alliance with Babylon, and later merged with the Persians to form the Medo-Persian empire — the dominant world power from 550 B.C. through Alexander\'s conquest, appearing prominently in the books of Ezra, Daniel, and Esther.</p>',
    'sections': [], 'hitchcock_meaning': 'a measure; judging; a garment', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 10:2', '1 Chronicles 1:5', 'Daniel 5:28']
  },
  'madmannah': {
    'id': 'madmannah', 'term': 'Madmannah', 'category': 'places',
    'intro': '<p>Madmannah (meaning: <em>measure of a gift; preparation of a garment</em>) was a town in the southern Negev of Judah, listed in the tribal allotments of Joshua 15:31. It also appears in 1 Chronicles 2:49 as a descendant name in the genealogy of Judah, where it likely refers to the town itself treated as the "daughter" (settlement) of its founder Shaaph. The site is tentatively identified with Umm Demnah south of Beersheba.</p>',
    'sections': [], 'hitchcock_meaning': 'measure of a gift; preparation of a garment', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Joshua 15:31', '1 Chronicles 2:49']
  },
  'madmen': {
    'id': 'madmen', 'term': 'Madmen', 'category': 'places',
    'intro': '<p>Madmen was a town of Moab against which Jeremiah pronounced a brief oracle of judgment: "Even you, O Madmen, shall be brought to silence" (Jeremiah 48:2). The name may be related to the Hebrew word for "dung heap." Its precise location in Moab is uncertain, and the town appears only in this single prophetic reference. Some scholars have proposed identifying it with Dimon mentioned in Isaiah 15:9 or with Khirbet Dimneh in the Moabite plateau.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Jeremiah 48:2']
  },
  'madmenah': {
    'id': 'madmenah', 'term': 'Madmenah', 'category': 'places',
    'intro': '<p>Madmenah was a town north of Jerusalem mentioned in Isaiah 10:31 in the prophet\'s vivid description of the Assyrian army\'s advance southward toward the capital city — a poetic march through a series of Benjamite towns culminating in the threat against Jerusalem itself. The town was apparently close enough to Jerusalem that its inhabitants were among those who would flee in panic before the Assyrian advance. It does not appear elsewhere in Scripture and its precise site is unknown.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Isaiah 10:31']
  },
  'madness': {
    'id': 'madness', 'term': 'Madness', 'category': 'concepts',
    'intro': '<p>Madness in Scripture covers a range from literal mental disorder to figurative folly and divine judgment. Deuteronomy 28:28 lists madness among the curses God would send on Israel for covenant unfaithfulness. David feigned madness before Achish of Gath to protect his life. Nebuchadnezzar was struck with a form of madness that caused him to live like an animal for seven years until his reason was restored as a sign of divine sovereignty. In the New Testament, Jesus\'s opponents accused him of having a demon and being mad (John 10:20), and Festus dismissed Paul\'s learning as madness. Qoheleth also observes madness as part of his survey of human experience under the sun.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Deuteronomy 28:34', 'John 10:20', 'Ecclesiastes 1:17', 'Daniel 4:33']
  },
  'madon': {
    'id': 'madon', 'term': 'Madon', 'category': 'places',
    'intro': '<p>Madon (meaning: <em>a chiding; a garment; his measure</em>) was a Canaanite royal city whose king Jobab joined the northern coalition assembled by Jabin of Hazor against Joshua\'s forces. The coalition was defeated at the waters of Merom, and the king of Madon appears in the list of thirty-one Canaanite kings conquered by Joshua. The site is unidentified with certainty but was likely located in Galilee near Hazor.</p>',
    'sections': [], 'hitchcock_meaning': 'a chiding; a garment; his measure', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Joshua 11:1', 'Joshua 12:19']
  },
  'magdala': {
    'id': 'magdala', 'term': 'Magdala', 'category': 'places',
    'intro': '<p>Magdala (meaning: <em>tower; greatness</em>) was a prosperous town on the western shore of the Sea of Galilee, about three miles north of Tiberias, known in the first century for its fish-salting industry and boat-building. It is the hometown of Mary Magdalene, who derived her surname from the town. Jesus visited the region of Magdala (called Magadan in some manuscripts) after feeding the four thousand, and was met by Pharisees and Sadducees demanding a sign. Archaeological excavations at Migdal have uncovered a first-century synagogue and Roman-period remains confirming the site\'s significance in Jesus\'s Galilean ministry.</p>',
    'sections': [], 'hitchcock_meaning': 'tower; greatness', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Matthew 15:39', 'Mark 8:10']
  },
  'magdalene': {
    'id': 'magdalene', 'term': 'Magdalene', 'category': 'people',
    'intro': '<p>Magdalene is the surname of Mary of Magdala, one of the most prominent women in the Gospel accounts. She appears to have been delivered by Jesus from seven demons and afterward traveled with him and the Twelve, supporting the ministry from her own resources. She was present at the crucifixion when most of the disciples had fled, was among those who observed Jesus\'s burial, and on the morning of the resurrection was the first or among the first to arrive at the tomb. In John\'s account she is the first to see the risen Jesus and was commissioned by him to carry the news to the disciples — making her what tradition has called "apostle to the apostles."</p>',
    'sections': [], 'hitchcock_meaning': 'a person from Magdala', 'source_ids': ['easton'],
    'key_refs': ['Luke 8:2', 'Mark 16:9', 'John 20:1', 'Matthew 27:56']
  },
  'magic': {
    'id': 'magic', 'term': 'Magic', 'category': 'concepts',
    'intro': '<p>Magic in the ancient world encompassed practices intended to influence supernatural powers or divine will through ritual, incantation, or divination — including astrology, omens, and consultation of spirits. The Mosaic law strictly prohibited all such practices, listing them alongside witchcraft, sorcery, and necromancy as abominations that brought divine judgment on the Canaanite nations. The prohibition rested on the conviction that all knowledge of the future and all power over circumstances belongs to the Lord alone, and that seeking it through occult means amounts to idolatry.</p><p>In the New Testament the magicians Bar-Jesus (Elymas) and Simon Magus are encountered and rebuked by the apostles, and the Ephesian converts publicly burned their magic books at considerable cost as a sign of genuine repentance. Revelation\'s list of those excluded from the holy city includes sorcerers.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Deuteronomy 18:10', 'Acts 13:6', 'Acts 19:19', 'Revelation 21:8']
  },
  'magicians': {
    'id': 'magicians', 'term': 'Magicians', 'category': 'concepts',
    'intro': '<p>Magicians in Scripture designate professional practitioners of the occult arts — typically the court specialists in dream interpretation, divination, and ritual magic employed by the pharaohs of Egypt and the kings of Babylon. Pharaoh\'s magicians replicated the first two plagues (blood and frogs) through their secret arts but failed at the third (lice or gnats), declaring it "the finger of God." Nebuchadnezzar\'s magicians, enchanters, sorcerers, and astrologers were unable to reveal and interpret his dream, opening the way for Daniel\'s divine revelation. The magicians\' failure in both accounts underscores the supremacy of Israel\'s God over all human occult knowledge.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Exodus 7:11', 'Exodus 8:18', 'Daniel 2:2', 'Daniel 2:10']
  },
  'magistrate': {
    'id': 'magistrate', 'term': 'Magistrate', 'category': 'concepts',
    'intro': '<p>Magistrates in Scripture refer to civil authorities charged with administering justice — from the appointed judges Moses established in the wilderness to the Roman praetors who beat Paul and Silas at Philippi. The Old Testament emphasizes the obligation of magistrates to judge fairly, without partiality or bribery, upholding the rights of the poor and vulnerable. Jesus instructs his hearers to settle disputes with adversaries before reaching the magistrate (Luke 12:58), reflecting the authority of Roman judicial officials. Paul teaches in Romans 13 that governing magistrates are God\'s servants for good and that believers should submit to them, paying taxes and rendering honor; Titus is similarly told to remind Christians to be subject to rulers and authorities.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Luke 12:58', 'Acts 16:20', 'Romans 13:1', 'Titus 3:1']
  },
  'magog': {
    'id': 'magog', 'term': 'Magog', 'category': 'people',
    'intro': '<p>Magog (meaning: <em>covering; roof; dissolving</em>) was the second son of Japheth in the Table of Nations (Genesis 10:2), and the name used by Ezekiel and Revelation for the land or peoples associated with the apocalyptic enemy of God\'s people. In Ezekiel 38–39, "Gog of the land of Magog" is the leader of a northern coalition that attacks Israel in the latter days and is destroyed by God\'s direct intervention. Most ancient interpreters associated Magog with Scythian or northern barbarian peoples; Josephus identified the Magogites with the Scythians. Revelation 20:8 uses Gog and Magog as symbols for the nations gathered for the final battle against the saints after the millennium.</p>',
    'sections': [], 'hitchcock_meaning': 'covering; roof; dissolving', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 10:2', 'Ezekiel 38:2', 'Revelation 20:8']
  },
  'magor-missabib': {
    'id': 'magor-missabib', 'term': 'Magor-missabib', 'category': 'concepts',
    'intro': '<p>Magor-missabib (meaning: <em>fear on every side</em>) was the symbolic name Jeremiah gave to Pashhur the priest after Pashhur had Jeremiah beaten and put in stocks for his prophecy against Jerusalem. The name, drawn from a phrase Jeremiah himself used in his laments, declared that Pashhur would become a terror to himself and all his friends — that they would fall by the sword of their enemies and he would witness it, before going into Babylon as a captive. The symbolic naming was a prophetic act of judgment, making Pashhur\'s very name a living oracle of doom against those who opposed God\'s word.</p>',
    'sections': [], 'hitchcock_meaning': 'fear on every side', 'source_ids': ['easton'],
    'key_refs': ['Jeremiah 20:3', 'Jeremiah 20:4']
  },
  'mahalaleel': {
    'id': 'mahalaleel', 'term': 'Mahalaleel', 'category': 'people',
    'intro': '<p>Mahalaleel was a pre-flood patriarch, the son of Cainan and father of Jared in the Sethite genealogy of Genesis 5:12–17, and an ancestor of Noah. He lived 895 years according to the Genesis record. Luke\'s genealogy of Jesus includes him in the line from Adam through Seth to Jesus, spelling the name Maleleel in the Greek. A man of the same name also appears in Nehemiah 11:4 as a Judahite ancestor of those who settled in Jerusalem after the exile, though he is a different individual.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 5:12', 'Luke 3:37']
  },
  'mahalath': {
    'id': 'mahalath', 'term': 'Mahalath', 'category': 'people',
    'intro': '<p>Mahalath is the name of two women in the Old Testament. The first was a daughter of Ishmael and granddaughter of Abraham, whom Esau took as a wife (also called Basemath in Genesis 36:3) when he recognized that Canaanite wives displeased his father. The second was a granddaughter of David, daughter of Jerimoth, whom Rehoboam took as one of his wives. The name may also appear in the headings of Psalms 53 and 88 as a musical notation, though in that context it likely denotes a tune or mode of performance rather than a person.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 28:9', '2 Chronicles 11:18']
  },
  'mahalath-leannoth-maschil': {
    'id': 'mahalath-leannoth-maschil', 'term': 'Mahalath Leannoth Maschil', 'category': 'concepts',
    'intro': '<p>Mahalath Leannoth Maschil is the complex musical heading of Psalm 88, combining three terms whose precise meaning in performance context is debated. <em>Mahalath</em> likely indicates a tune or mode; <em>leannoth</em> may mean "for singing" or "for affliction" or indicate antiphonal performance; <em>maschil</em> denotes an instructive or skillfully composed psalm. Together they mark Psalm 88 as a didactic lament of a particular musical character. The psalm itself is one of the darkest in the psalter, ending without any resolution of its anguish — a feature that may be reflected in the "affliction" element of the heading.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Psalms 88:1']
  },
  'mahalath-maschil': {
    'id': 'mahalath-maschil', 'term': 'Mahalath Maschil', 'category': 'concepts',
    'intro': '<p>Mahalath Maschil is the musical heading of Psalm 53, marking it as a <em>maschil</em> (a didactic or skillful composition) set to a tune or in a mode called <em>mahalath</em>. Psalm 53 is closely parallel to Psalm 14, describing the universal moral corruption of humanity ("The fool says in his heart, \'There is no God\'") and God\'s judgment on the evildoers. The use of the divine name <em>Elohim</em> rather than the personal name <em>YHWH</em> (Yahweh) throughout Psalm 53 versus Psalm 14 has led scholars to identify them as variant versions for use in different liturgical settings.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Psalms 53:1']
  },
  'mahanaim': {
    'id': 'mahanaim', 'term': 'Mahanaim', 'category': 'places',
    'intro': '<p>Mahanaim (meaning: <em>tents; two fields; two armies</em>) was a site in Gilead east of the Jordan where Jacob, returning from Haran, met the angels of God and named the place "Two Camps." The name reflects Jacob\'s vision of the divine host alongside his own company. The town later became important in Israelite history: it was the seat of Ish-bosheth\'s brief rival kingdom after Saul\'s death; David took refuge there during Absalom\'s revolt; and the city was given to the Levites as a place of refuge. Its exact location on the Jabbok River is debated but generally placed at modern Tulul ed-Dahab.</p>',
    'sections': [], 'hitchcock_meaning': 'tents; two fields; two armies', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 32:2', 'Joshua 13:26', '2 Samuel 2:8', '2 Samuel 17:24']
  },
  'mahaneh-dan': {
    'id': 'mahaneh-dan', 'term': 'Mahaneh-dan', 'category': 'places',
    'intro': '<p>Mahaneh-dan (meaning "camp of Dan") was a campsite between Zorah and Eshtaol in the tribal territory of Dan where the Spirit of the Lord first began to stir Samson. The same name was used for a location west of Kiriath-jearim where the six hundred Danite warriors who were seeking territory in the north encamped before their march to Laish. The name preserves memory of the Danite military encampments in the region before the tribe secured a permanent settlement.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Judges 13:25', 'Judges 18:12']
  },
  'mahath': {
    'id': 'mahath', 'term': 'Mahath', 'category': 'people',
    'intro': '<p>Mahath (meaning: <em>same as Maath — wiping away; dissolution</em>) is the name of two Kohathite Levites. The first was an ancestor of Heman the singer, listed in the genealogy of the Levitical musicians appointed by David for temple worship in 1 Chronicles 6. The second Mahath was a Levite who served in Hezekiah\'s temple reform, assisting in the purification of the temple and the distribution of the holy offerings contributed by the people during the revival of worship.</p>',
    'sections': [], 'hitchcock_meaning': 'same as Maath', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Chronicles 6:35', '2 Chronicles 29:12']
  },
  'mahazioth': {
    'id': 'mahazioth', 'term': 'Mahazioth', 'category': 'people',
    'intro': '<p>Mahazioth (meaning: <em>seeing a sign; seeing a letter</em>) was a son of Heman the king\'s seer, appointed by David among the twenty-four courses of temple musicians to prophesy with lyres, harps, and cymbals. He is listed in 1 Chronicles 25:4 among Heman\'s sons whose names form an acrostic prayer, and his course, the twenty-third, is identified in 1 Chronicles 25:30 as the lot that fell to him and his sons and brothers — twelve in his division.</p>',
    'sections': [], 'hitchcock_meaning': 'seeing a sign; seeing a letter', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Chronicles 25:4', '1 Chronicles 25:30']
  },
  'maher-shalal-hash-baz': {
    'id': 'maher-shalal-hash-baz', 'term': 'Maher-shalal-hash-baz', 'category': 'people',
    'intro': '<p>Maher-shalal-hash-baz (meaning: <em>making speed to the spoil; he hastens to the prey</em>) was the son of the prophet Isaiah and a prophetess, whose birth and naming were commanded by God as a living sign. The name was first written on a tablet with witnesses before the child\'s conception, then given at birth to signal that before the child could say "my father" or "my mother," the wealth of Damascus and the spoil of Samaria would be carried away by the king of Assyria. This oracle, directed against the Syro-Ephraimite alliance threatening Judah under Ahaz, was fulfilled by the Assyrian campaigns of Tiglath-pileser III.</p>',
    'sections': [], 'hitchcock_meaning': 'making speed to the spoil; he hastens to the prey', 'source_ids': ['easton'],
    'key_refs': ['Isaiah 8:1', 'Isaiah 8:3', 'Isaiah 8:4']
  },
  'mahlah': {
    'id': 'mahlah', 'term': 'Mahlah', 'category': 'people',
    'intro': '<p>Mahlah (meaning: <em>same as Mahali — sickness; a harp; forgiveness</em>) was the eldest of the five daughters of Zelophehad of the tribe of Manasseh, who had died in the wilderness without sons. The daughters — Mahlah, Noah, Hoglah, Milcah, and Tirzah — came before Moses and the leaders to petition for their father\'s inheritance, arguing that his name should not be lost because he had no son. God ruled in their favor, establishing a legal precedent that daughters could inherit in the absence of sons, subject to marrying within their tribe to prevent the inheritance from passing to another tribe.</p>',
    'sections': [], 'hitchcock_meaning': 'Mahli, Mahlon, same as Mahali', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Numbers 27:1', 'Numbers 36:11', 'Joshua 17:3']
  },
  'mahlon': {
    'id': 'mahlon', 'term': 'Mahlon', 'category': 'people',
    'intro': '<p>Mahlon was the elder son of Elimelech and Naomi of Bethlehem who emigrated to Moab during a famine and there took Ruth the Moabitess as his wife. He died in Moab without children, and his death, along with that of his father and brother Chilion, left Naomi and her daughters-in-law as widows. Ruth\'s loyalty to Naomi and her subsequent marriage to Boaz was understood in part as a fulfillment of the levirate principle: Boaz acquired Ruth "to raise up the name of the dead on his inheritance, that the name of the dead may not be cut off from among his brothers" — referring specifically to Mahlon.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Ruth 1:2', 'Ruth 4:10']
  },
  'mahol': {
    'id': 'mahol', 'term': 'Mahol', 'category': 'people',
    'intro': '<p>Mahol was the father of four men — Heman, Calcol, Darda, and Ethan — who were renowned for their wisdom but whose wisdom was surpassed by Solomon\'s. The text in 1 Kings 4:31 identifies them as "the sons of Mahol," implying membership in a guild or class of wise men; some scholars suggest "sons of Mahol" may mean "sons of the dance" — members of a musical or cultic dancing guild rather than literal sons of a man named Mahol. The same names appear in 1 Chronicles 2 as descendants of Judah, though the relationship between the two passages is debated.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Kings 4:31', '1 Chronicles 2:6']
  },
  'mail-coat-of': {
    'id': 'mail-coat-of', 'term': 'Mail, Coat of', 'category': 'concepts',
    'intro': '<p>The coat of mail was a type of defensive armor consisting of overlapping metal scales or plates sewn onto a leather or fabric backing, resembling fish scales. Goliath wore a coat of mail of bronze weighing five thousand shekels (approximately 125 pounds) when he challenged Israel — its enormous weight underscoring his formidable appearance and the apparent impossibility of David\'s victory. The Hebrew term <em>shiryon kaskassim</em> specifically describes this scale-armor construction. Coats of mail are also mentioned in the equipment of Solomon\'s guard and the armies of Nehemiah\'s time when rebuilding Jerusalem\'s walls.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['1 Samuel 17:5', '1 Samuel 17:38', 'Nehemiah 4:16']
  },
  'main-sail': {
    'id': 'main-sail', 'term': 'Main-sail', 'category': 'concepts',
    'intro': '<p>The main-sail (or foresail) appears in Acts 27:40 in the account of Paul\'s shipwreck near Malta: when the ship was driven ashore, the sailors hoisted the foresail to the wind to drive the vessel toward the beach. The Greek term <em>artemon</em>, translated "foresail" in modern versions and "mainsail" in the Authorized Version, referred to a small sail rigged at the bow of the ship, used for maneuvering in harbors and shallow waters rather than open-sea sailing. The precise rigging of ancient Mediterranean merchant vessels of the first century helps to clarify the nautical details of this passage.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Acts 27:40']
  },
  'makheloth': {
    'id': 'makheloth', 'term': 'Makheloth', 'category': 'places',
    'intro': '<p>Makheloth (meaning: <em>assemblies; congregations</em>) was one of the wilderness campsites of Israel on the journey from Egypt to Canaan, listed in the itinerary of Numbers 33:25–26 between Haradah and Tahath. Its precise location is unknown as most of the wilderness stations cannot be identified with certainty. The name may reflect a gathering or assembly that took place at the campsite, preserving a memory of a significant communal event during the wilderness wandering.</p>',
    'sections': [], 'hitchcock_meaning': 'assemblies; congregations', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Numbers 33:25', 'Numbers 33:26']
  },
  'makkedah': {
    'id': 'makkedah', 'term': 'Makkedah', 'category': 'places',
    'intro': '<p>Makkedah (meaning: <em>worshiping; burning; raised; crookedness</em>) was a Canaanite royal city in the Shephelah of Judah where the five Amorite kings who fled from Joshua\'s forces hid in a cave. Joshua sealed the cave and then defeated the enemy armies before returning to execute the kings — pulling them from the cave and hanging them on five trees until evening before burying them in the same cave. Makkedah is listed among the cities conquered by Joshua and was later assigned to the tribe of Judah.</p>',
    'sections': [], 'hitchcock_meaning': 'worshiping; burning; raised; crookedness', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Joshua 10:10', 'Joshua 10:16', 'Joshua 12:16']
  },
  'maktesh': {
    'id': 'maktesh', 'term': 'Maktesh', 'category': 'places',
    'intro': '<p>Maktesh (Hebrew: <em>mortar</em>) was a district or quarter of Jerusalem mentioned in Zephaniah 1:11 in a prophecy of judgment: "Wail, O inhabitants of the Maktesh, for all the traders are no more; all who weigh out silver are cut off." The name likely describes a hollow or valley in Jerusalem used as a commercial center where merchants and money-changers conducted business, possibly the Tyropoeon Valley between the western hill and the temple mount. It appears only once in Scripture and is not identified with certainty.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Zephaniah 1:11']
  },
  'malachi': {
    'id': 'malachi', 'term': 'Malachi', 'category': 'people',
    'intro': '<p>Malachi (meaning: <em>my messenger; my angel</em>) was the last of the Old Testament writing prophets, whose book closes the Hebrew canon and points forward to a coming messenger who will prepare the Lord\'s way. Almost nothing personal is known about him beyond his name, which some have suggested may be a title rather than a personal name — though most scholars treat it as a proper name. He prophesied in Jerusalem probably during the governorship of Nehemiah or shortly after, addressing the same problems of priestly negligence, mixed marriages, divorce, and neglect of tithes that Nehemiah\'s memoirs describe.</p><p>His final oracle predicts the sending of Elijah before the great and terrible Day of the Lord — a prophecy the New Testament applies to John the Baptist.</p>',
    'sections': [], 'hitchcock_meaning': 'my messenger; my angel', 'source_ids': ['easton'],
    'key_refs': ['Malachi 3:1', 'Malachi 4:5', 'Matthew 11:10', 'Matthew 17:12']
  },
  'malachi-prophecies-of': {
    'id': 'malachi-prophecies-of', 'term': 'Malachi, Prophecies of', 'category': 'concepts',
    'intro': '<p>The Book of Malachi is structured around six disputations in which the prophet quotes objections from the people and priests and answers them with divine rebuttal. Its themes include the corruption of the priesthood (offering blind and lame animals), the epidemic of divorce and marriage to foreign women, the withholding of tithes, and the people\'s complaint that it does not profit to serve God. Against this spiritual complacency Malachi announces the coming of a refining messenger, the Elijah who will prepare the Lord\'s way, and the great Day of the Lord on which the righteous will shine and the wicked will be burned.</p><p>Malachi is the most frequently quoted minor prophet in the New Testament\'s identification of John the Baptist as the forerunner, and its closing chapters shaped the eschatological expectations of Second Temple Judaism.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Malachi 1:1', 'Malachi 3:1', 'Matthew 11:10', 'Mark 1:2']
  },
  'malcam': {
    'id': 'malcam', 'term': 'Malcam', 'category': 'concepts',
    'intro': '<p>Malcam (also Milcom or Molech) was the chief deity of the Ammonites, mentioned in Scripture in contexts of condemnation. When David captured the Ammonite city of Rabbah, he took from Malcam\'s head a crown of gold weighing a talent and set it on his own head. The prophets Jeremiah and Zephaniah condemn those who swear by Malcam alongside the Lord. The worship of Molech (the same deity under a slightly different form) involved child sacrifice and was among the most abhorrent practices forbidden by the Mosaic law.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['2 Samuel 12:30', 'Jeremiah 49:1', 'Zephaniah 1:5', '1 Kings 11:5']
  },
  'malchi-shua': {
    'id': 'malchi-shua', 'term': 'Malchi-shua', 'category': 'people',
    'intro': '<p>Malchi-shua was the third son of King Saul, listed in 1 Chronicles 8:33 among Saul\'s sons by Jonathan, Ishvi, and Malchi-shua. He was killed alongside his father Saul and his brothers Jonathan and Abinadab by the Philistines at the battle of Gilboa on Mount Gilboa, ending the male line of Saul\'s house capable of military leadership. His death in battle at his father\'s side is recorded in 1 Samuel 31:2 and 1 Chronicles 10:2.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['1 Chronicles 8:33', '1 Samuel 31:2']
  },
  'malchiah': {
    'id': 'malchiah', 'term': 'Malchiah', 'category': 'people',
    'intro': '<p>Malchiah (meaning: <em>the Lord my king, or my counselor</em>) is a name shared by at least ten persons in the Old Testament, most associated with the priestly and Levitical service. Among the most notable: the head of the fifth course of priests in David\'s temple organization; a priest who repaired a section of Jerusalem\'s walls under Nehemiah; the son of Hammelech in whose cistern Jeremiah was imprisoned by Zedekiah\'s officials; and several priests and laymen who had taken foreign wives during the exile. The name\'s frequency in the priestly class reflects its theological meaning acknowledging God\'s kingship.</p>',
    'sections': [], 'hitchcock_meaning': 'the Lord my king, or my counselor', 'source_ids': ['easton'],
    'key_refs': ['1 Chronicles 24:9', 'Jeremiah 38:6', 'Nehemiah 3:14']
  },
  'malchus': {
    'id': 'malchus', 'term': 'Malchus', 'category': 'people',
    'intro': '<p>Malchus (meaning: <em>my king, kingdom, or counselor</em>) was the servant of the high priest Caiaphas whose right ear was cut off by Peter with a sword in the Garden of Gethsemane at the moment of Jesus\'s arrest. Only John\'s Gospel names the servant and his assailant. Jesus immediately rebuked Peter, touched Malchus\'s ear and healed it — the last healing miracle recorded before the crucifixion — and declared that he could call on twelve legions of angels but chose to drink the cup his Father had given him. The healing of Malchus stands as a vivid emblem of Jesus\'s nonviolent submission to his Father\'s will.</p>',
    'sections': [], 'hitchcock_meaning': 'my king, kingdom, or counselor', 'source_ids': ['easton', 'smith'],
    'key_refs': ['John 18:10', 'Matthew 26:51', 'Luke 22:51']
  },
  'mallothi': {
    'id': 'mallothi', 'term': 'Mallothi', 'category': 'people',
    'intro': '<p>Mallothi (meaning: <em>fullness; circumcision</em>) was a son of Heman, the king\'s seer, appointed by David among the twenty-four courses of Levitical musicians for prophesying and temple worship. He is listed in 1 Chronicles 25:4 among the sons of Heman whose names form an acrostic poem of praise, and his division, the nineteenth, is identified in 1 Chronicles 25:26 as falling to him and his sons and brothers — twelve in his assigned rotation.</p>',
    'sections': [], 'hitchcock_meaning': 'fullness; circumcision', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Chronicles 25:4', '1 Chronicles 25:26']
  },
  'mallows': {
    'id': 'mallows', 'term': 'Mallows', 'category': 'concepts',
    'intro': '<p>The mallows of Job 30:4 — described as gathered for food by those Job likens to the most despised outcasts of society — likely refers to the saltbush or orache plant (<em>Atriplex halimus</em>), which grows in arid and saline conditions near the Dead Sea region. The Hebrew word <em>mallooach</em> is related to the word for salt, reflecting the saltmarsh habitat of the plant. Though not highly nutritious, its leaves could be eaten in extremity and the plant was used medicinally. The reference underscores the wretchedness of those who gather it as a staple food.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Job 30:4']
  },
  'malluch': {
    'id': 'malluch', 'term': 'Malluch', 'category': 'people',
    'intro': '<p>Malluch (meaning: <em>reigning; counseling</em>) is the name of six men in the Old Testament, all associated with the priestly or Levitical service in the post-exilic period. Among them: a Merarite Levite in the genealogy of the temple singers; a priest who returned from Babylon with Zerubbabel and whose family is listed in Nehemiah 12:2; two priests who had married foreign wives and were required to send them away in Ezra\'s reform; and a priestly leader who set his seal to the covenant of Nehemiah.</p>',
    'sections': [], 'hitchcock_meaning': 'reigning; counseling', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Chronicles 6:44', 'Nehemiah 12:2', 'Ezra 10:29']
  },
  'mammon': {
    'id': 'mammon', 'term': 'Mammon', 'category': 'concepts',
    'intro': '<p>Mammon is an Aramaic word (meaning: <em>riches; wealth</em>) used by Jesus in his Sermon on the Mount and in Luke 16 to personify material wealth as a spiritual rival to God. "No one can serve two masters... You cannot serve God and mammon" (Matthew 6:24) presents money not merely as a neutral tool but as a potential lord that competes with God for the allegiance of the heart. In Luke 16 Jesus uses the parable of the dishonest manager to urge his followers to use "unrighteous mammon" (worldly wealth) to make friends who will welcome them into eternal dwellings — teaching stewardship of earthly resources in light of eternal priorities.</p>',
    'sections': [], 'hitchcock_meaning': 'riches', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Matthew 6:24', 'Luke 16:9', 'Luke 16:13']
  },
  'mamre': {
    'id': 'mamre', 'term': 'Mamre', 'category': 'places',
    'intro': '<p>Mamre (meaning: <em>rebellious; bitter; set with trees</em>) was both a personal name and a place name in the patriarchal narratives. Mamre the Amorite was an ally of Abraham who helped pursue the four kings after the rescue of Lot. The "oaks of Mamre" or the "plain of Mamre" near Hebron was Abraham\'s primary residence in Canaan, where he camped, built an altar, and received the three divine visitors who announced Isaac\'s birth and revealed the coming destruction of Sodom. The proximity of Mamre to Machpelah places it in the region of modern Hebron, and a site called Ramet el-Khalil south of Hebron has been identified with ancient Mamre.</p>',
    'sections': [], 'hitchcock_meaning': 'rebellious; bitter; set with trees', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 14:13', 'Genesis 14:24', 'Genesis 18:1', 'Genesis 23:17']
  },
  'man': {
    'id': 'man', 'term': 'Man', 'category': 'concepts',
    'intro': '<p>The biblical doctrine of man (theological anthropology) presents human beings as uniquely created in the image and likeness of God — <em>imago Dei</em> — set apart from the rest of creation as rational, moral, relational, and spiritual beings capable of communion with their Creator. Genesis 1:26–27 establishes both male and female as image-bearers with dominion over creation. The fall in Genesis 3 introduced radical corruption of that image: the mind, will, and affections of fallen humanity are directed away from God rather than toward him.</p><p>The New Testament presents Christ as the true and perfect image of God and the Second Adam who restores what the first Adam lost. Paul\'s anthropology distinguishes the outer and inner man, the natural and spiritual, and the dying and renewed dimensions of human existence in light of the resurrection.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 1:26', 'Genesis 1:27', 'Romans 5:12', '1 Corinthians 15:45']
  },
  'man-of-sin': {
    'id': 'man-of-sin', 'term': 'Man of sin', 'category': 'concepts',
    'intro': '<p>The "man of sin" (or "man of lawlessness" in most modern translations) is a figure described by Paul in 2 Thessalonians 2:3–12 who will appear before the Day of the Lord, exalting himself above every so-called god and object of worship and proclaiming himself to be God while sitting in the temple of God. He operates with satanic power and deceptive signs, and is described as already being restrained by a force that will be removed before his full manifestation. His coming results in his destruction by Christ at his appearing.</p><p>Interpreters have identified the man of sin with Roman emperors, the papacy, a future individual Antichrist, or a corporate symbol of anti-Christian power; the passage\'s language draws heavily on Daniel\'s vision of the "abomination of desolation."</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['2 Thessalonians 2:3', '2 Thessalonians 2:4', '2 Thessalonians 2:8']
  },
  'manaen': {
    'id': 'manaen', 'term': 'Manaen', 'category': 'people',
    'intro': '<p>Manaen (meaning: <em>a comforter; a leader</em>) was a prophet and teacher in the church at Antioch, listed in Acts 13:1 among those from whom the Holy Spirit directed the setting apart of Barnabas and Saul for their first missionary journey. He is described as a "foster brother" or "member of the court" (Greek <em>syntrophos</em>) of Herod the tetrarch — meaning he was raised with Herod Antipas at the Roman court, likely as a companion of similar age. His presence among the Antiochene leadership illustrates the social breadth of the early church, which included people connected to the highest levels of Herodian society.</p>',
    'sections': [], 'hitchcock_meaning': 'a comforter; a leader', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Acts 13:1']
  },
  'manasseh': {
    'id': 'manasseh', 'term': 'Manasseh', 'category': 'people',
    'intro': '<p>Manasseh (meaning: <em>forgetfulness; he that is forgotten</em>) is the name of two major figures and a tribal name in the Old Testament. The first was the elder son of Joseph and Asenath, born in Egypt and adopted by Jacob, whose tribe received a large allotment in both Cisjordan and Transjordan. The second and more theologically significant Manasseh was king of Judah for fifty-five years (the longest reign in Judah\'s history), notorious for reintroducing Baal worship, Asherah poles, child sacrifice in the Valley of Hinnom, and occult practices that Hezekiah his father had abolished.</p><p>The books of Kings credit Manasseh\'s sin as the primary cause of the Babylonian exile, yet 2 Chronicles records his capture by Assyria, repentance in humility, and restoration — presenting a more complex portrait of a man whose wickedness was eventually followed by genuine, if inadequate, reform.</p>',
    'sections': [], 'hitchcock_meaning': 'forgetfulness; he that is forgotten', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 41:51', '2 Kings 21:1', '2 Chronicles 33:11', '2 Chronicles 33:12']
  },
  'mandrakes': {
    'id': 'mandrakes', 'term': 'Mandrakes', 'category': 'concepts',
    'intro': '<p>Mandrakes (<em>Mandragora officinarum</em>) are a plant of the nightshade family whose forked roots vaguely resemble a human form and whose fruits have a pleasant odor. In Genesis 30, Reuben found mandrakes during the wheat harvest and brought them to his mother Leah; Rachel bargained for them from Leah, believing they had fertility-enhancing properties — a belief widespread in the ancient Near East. The Song of Solomon 7:13 mentions mandrakes\' fragrance as part of the beloved\'s garden of love. Whether mandrakes actually influenced the subsequent births of Jacob\'s children is left ambiguous by the text, which attributes the conceptions to God\'s direct action.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 30:14', 'Song of Solomon 7:13']
  },
  'maneh': {
    'id': 'maneh', 'term': 'Maneh', 'category': 'concepts',
    'intro': '<p>The maneh (or mina) was a unit of weight in the ancient Near East equivalent to sixty shekels, and as such was the standard intermediate unit in the shekel-maneh-talent system. Ezekiel\'s reformed system in Ezekiel 45:12 defines the maneh as twenty gerahs times three — sixty shekels total. The maneh appears in the accounts of Solomon\'s gold stores (1 Kings 10:17), the Ezra-Nehemiah period contributions to the temple treasury, and in the parable of the minas (pounds) in Luke 19, where the word is the Greek form of the same underlying monetary unit representing a substantial sum.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Ezekiel 45:12', '1 Kings 10:17', 'Nehemiah 7:71']
  },
  'manger': {
    'id': 'manger', 'term': 'Manger', 'category': 'concepts',
    'intro': '<p>The manger was a feeding trough for animals, made of wood or hewn from stone, used in stables and cave-stalls throughout ancient Palestine. Luke\'s Gospel records that Mary wrapped Jesus in swaddling cloths and laid him in a manger because there was no room for them in the inn — a detail that places the birth of the Messiah in humble, even animal-shared, surroundings. The manger became the sign given to the shepherds by the angel, uniquely identifying the newborn king. Isaiah\'s image of the ox knowing its owner\'s manger (Isaiah 1:3) may lie behind Luke\'s emphasis, presenting Jesus as the one whom even the animals recognize while Israel does not.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Luke 2:7', 'Luke 2:12', 'Luke 2:16']
  },
  'manna': {
    'id': 'manna', 'term': 'Manna', 'category': 'concepts',
    'intro': '<p>Manna was the miraculous food God provided for Israel throughout their forty years in the wilderness, appearing each morning as a fine, flake-like substance on the ground that the Israelites ground or beat and baked into cakes tasting like wafers made with honey. The name derives from the Hebrew <em>man hu?</em> — "What is it?" — spoken when Israel first encountered it. A double portion fell on the sixth day to allow rest on the Sabbath, and it ceased when Israel entered Canaan and ate the produce of the land.</p><p>Jesus employed manna as a christological type in John 6, identifying himself as "the bread of life" and "the true bread from heaven" — the greater manna that gives not merely physical life for a generation but eternal life to all who believe. Revelation promises "hidden manna" to the overcomer.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Exodus 16:15', 'Numbers 11:7', 'John 6:31', 'John 6:35']
  },
  'manoah': {
    'id': 'manoah', 'term': 'Manoah', 'category': 'people',
    'intro': '<p>Manoah (meaning: <em>rest; a present</em>) was a man of the tribe of Dan from Zorah, the father of Samson. He and his barren wife received the announcement of Samson\'s coming birth from the angel of the Lord, who appeared twice and gave instructions for a Nazirite consecration from birth. When Manoah offered a burnt offering and the flame ascended, the angel ascended in the flame — at which point Manoah feared he would die for having seen God, though his wife reassured him. His reverence and earnest desire to receive instruction for raising the promised child stand in marked contrast to the tragic outcome of Samson\'s life.</p>',
    'sections': [], 'hitchcock_meaning': 'rest; a present', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Judges 13:1', 'Judges 13:8', 'Judges 13:20']
  },
  'manslayer': {
    'id': 'manslayer', 'term': 'Manslayer', 'category': 'concepts',
    'intro': '<p>A manslayer in Mosaic law was one who had killed a person unintentionally — without premeditation or malice — in contrast to a murderer who killed with intent. The Mosaic law distinguished carefully between these categories: the deliberate murderer was to be executed with no possibility of sanctuary, while the accidental manslayer was permitted to flee to one of six designated cities of refuge where he could live in safety from the avenger of blood until the death of the current high priest, after which he could return home. The system thus provided both protection for the innocent and a form of accountability, since the manslayer could not return to his property until the high priest\'s death.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Numbers 35:6', 'Numbers 35:12', 'Deuteronomy 19:4', 'Joshua 20:3']
  },
  'mantle': {
    'id': 'mantle', 'term': 'Mantle', 'category': 'concepts',
    'intro': '<p>The mantle in Scripture refers to a large outer cloak or robe, often of a distinctive character that marked its wearer\'s identity and office. Elijah\'s hairy or sheepskin mantle was his prophetic trademark and became the most famous mantle in the Bible: he used it to part the Jordan, threw it over Elisha as a call to prophetic succession, and when it fell from the ascending Elijah, Elisha took it up and used it to repeat the parting of the Jordan — a double portion of Elijah\'s spirit confirmed in a double of his signature action. The torn mantle of Ahijah the Shilonite symbolized the division of Solomon\'s kingdom, and Samuel\'s mantle torn by Saul signified the tearing of the kingdom from him.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Kings 19:13', '1 Kings 19:19', '2 Kings 2:8', '2 Kings 2:13']
  },
  'maoch': {
    'id': 'maoch', 'term': 'Maoch', 'category': 'people',
    'intro': '<p>Maoch was the father of Achish, king of Gath, at whose court David took refuge with his six hundred men while fleeing Saul. When Achish is referred to in 1 Kings 2:39, his father is called Maachah rather than Maoch — likely variant forms of the same name or a scribal variation. Achish is presented as treating David with relative fairness, and David lodged in his territory for over a year, though the Philistine lords refused to allow David to fight alongside them against Saul at Jezreel.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Samuel 27:2', '1 Kings 2:39']
  },
  'maon': {
    'id': 'maon', 'term': 'Maon', 'category': 'places',
    'intro': '<p>Maon (meaning: <em>house; place of sin</em>) was a town in the hill country of Judah, listed in Joshua 15:55 among the settlements of the tribe of Judah in the southern highlands. It gave its name to the Wilderness of Maon, where David hid from Saul and where Nabal the Carmelite kept his flocks — Nabal is described as "a man of Maon whose business was in Carmel." The town is identified with Tell Main about eight miles south of Hebron. The wilderness surrounding it provided the rocky terrain where Saul nearly caught David before being called away by news of a Philistine raid.</p>',
    'sections': [], 'hitchcock_meaning': 'house; place of sin', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Joshua 15:55', '1 Samuel 23:24', '1 Samuel 25:2']
  },
  'mara': {
    'id': 'mara', 'term': 'Mara', 'category': 'concepts',
    'intro': '<p>Mara (meaning: <em>bitter; bitterness</em>) is the name Naomi gave herself when she returned from Moab to Bethlehem bereft of her husband and two sons. "Do not call me Naomi," she said; "call me Mara, for the Almighty has dealt very bitterly with me" (Ruth 1:20). The name-change is a profound act of grief, expressing Naomi\'s sense that her life had been emptied of its former fullness and sweetness. It stands as a biblical affirmation that honest lament — naming loss as loss and bitterness as bitterness — is a legitimate expression of faith, one that the book of Ruth answers with the restoration of family and hope through Ruth and Boaz.</p>',
    'sections': [], 'hitchcock_meaning': 'bitter; bitterness', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Ruth 1:20']
  },
  'marah': {
    'id': 'marah', 'term': 'Marah', 'category': 'places',
    'intro': '<p>Marah (meaning: <em>bitter</em>) was the first water source reached by Israel after crossing the Red Sea on their journey through the Sinai wilderness. The water was undrinkable due to its bitterness, causing the people to murmur against Moses. God showed Moses a piece of wood (or tree) which, when cast into the water, made it sweet — a miracle that was followed by a declaration of God\'s healing covenant: "I am the Lord, your healer." The site is generally identified somewhere in the Sinai peninsula near the eastern shore of the Gulf of Suez, though the precise location is debated.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Exodus 15:23', 'Exodus 15:25', 'Numbers 33:8']
  },
  'maralah': {
    'id': 'maralah', 'term': 'Maralah', 'category': 'places',
    'intro': '<p>Maralah (meaning: <em>sleep; a sacrifice of myrrh; ascension</em>) was a town on the border of the tribal territory of Zebulun, mentioned in Joshua 19:11 as part of the southern boundary description of Zebulun\'s allotment. It lay near the Kishon River in the region of the Jezreel Valley. Its precise identification is uncertain, and it appears only in this one boundary text, making it one of many minor geographical markers in the tribal allotment lists of Joshua.</p>',
    'sections': [], 'hitchcock_meaning': 'sleep; a sacrifice of myrrh; ascension', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Joshua 19:11']
  },
  'maranatha': {
    'id': 'maranatha', 'term': 'Maranatha', 'category': 'concepts',
    'intro': '<p>Maranatha is an Aramaic phrase preserved untranslated in 1 Corinthians 16:22, capable of being read as either a statement ("Our Lord has come" — <em>maran atha</em>) or a prayer ("Our Lord, come!" — <em>marana tha</em>). The prayer interpretation is generally preferred and was the cry of the early church\'s eschatological longing. The phrase also appears in the Didache (a first or second century Christian document) as a liturgical acclamation in the eucharistic setting. Revelation\'s final prayer "Come, Lord Jesus" (Marana tha in Aramaic) echoes the same eschatological petition, marking it as one of the oldest prayers of the church.</p>',
    'sections': [], 'hitchcock_meaning': 'the Lord is coming', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Corinthians 16:22', 'Philippians 4:5', 'Revelation 22:20']
  },
  'marble': {
    'id': 'marble', 'term': 'Marble', 'category': 'concepts',
    'intro': '<p>Marble appears in Scripture as a material associated with royal luxury and architectural grandeur. The palace of the Persian king Ahasuerus at Susa had a pavement of porphyry, marble, mother-of-pearl, and precious stones (Esther 1:6). David prepared marble for the temple in large quantities (1 Chronicles 29:2), and Revelation\'s lament over Babylon includes marble among the luxury commodities whose merchants will no longer find buyers when the great city falls (Revelation 18:12). The word translated marble sometimes refers to alabaster or other white stone, as Israel\'s marble quarries were limited compared to those of Greece or Rome.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Esther 1:6', '1 Chronicles 29:2', 'Revelation 18:12']
  },
  'marcheshvan': {
    'id': 'marcheshvan', 'term': 'Marcheshvan', 'category': 'concepts',
    'intro': '<p>Marcheshvan (also Bul) is the eighth month of the Hebrew civil calendar, corresponding to October–November in the modern calendar. It is mentioned in 1 Kings 6:38 as the month Bul, in which Solomon completed the building of the temple after seven years of construction. In the later period Marcheshvan became its standard name, derived from the Babylonian month name. It was a month of plowing and sowing in the agricultural cycle of ancient Israel, occurring after the early rains had softened the ground following the summer dry season.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Kings 6:38']
  },
  'marcus': {
    'id': 'marcus', 'term': 'Marcus', 'category': 'people',
    'intro': '<p>Marcus is the Latin form of Mark, identified in Colossians 4:10 as a cousin of Barnabas who sends greetings from Rome alongside Paul during Paul\'s imprisonment. He is almost certainly the same as John Mark, the young man whose departure from the first missionary journey caused a sharp disagreement between Paul and Barnabas (Acts 15:37–39), and whose subsequent rehabilitation in Paul\'s estimation is evidenced by Paul\'s warm endorsement in Colossians and Philemon and his request for Mark in 2 Timothy 4:11. Peter also mentions Marcus as a son in 1 Peter 5:13, reflecting the close relationship between Mark and both senior apostles that positioned him as the traditional author of the second Gospel.</p>',
    'sections': [], 'hitchcock_meaning': 'polite; shining', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Colossians 4:10', '1 Peter 5:13', '2 Timothy 4:11']
  },
}

def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f"BP m1: Maachah → Marcus: wrote {written}, skipped {skipped} existing.")

main()
