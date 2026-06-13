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
  'laban': {
    'id': 'laban', 'term': 'Laban', 'category': 'people',
    'intro': '<p>Laban (meaning: <em>white; shining; gentle; brittle</em>) was the son of Bethuel, grandson of Nahor (Abraham\'s brother), and thus a nephew of Abraham\'s family. He lived at Haran in Paddan-aram and is first mentioned in connection with the negotiation of Rebekah\'s marriage to Isaac. He reappears as the father of Leah and Rachel, and the central figure in Jacob\'s twenty years of service in Aram, during which Laban changed Jacob\'s wages ten times and attempted to retain him by trickery, though God overruled in Jacob\'s favor.</p><p>Laban and Jacob eventually made a covenant at Mizpah — the boundary pillar between their households — and parted in peace. A second place named Laban appears in the wilderness itinerary of Deuteronomy 1:1, but has no connection to the patriarch.</p>',
    'sections': [], 'hitchcock_meaning': 'white; shining; gentle; brittle', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Genesis 24:29', 'Genesis 29:16', 'Genesis 31:44']
  },
  'lachish': {
    'id': 'lachish', 'term': 'Lachish', 'category': 'places',
    'intro': '<p>Lachish (meaning: <em>who walks, or exists, of himself</em>) was one of the most important fortified cities of the Shephelah, the lowland foothills of Judah, located about thirty miles southwest of Jerusalem. Its Canaanite king Japhia joined the coalition against Joshua and was defeated at the battle of Gibeon; Joshua then besieged and took the city in two days. Rehoboam later fortified it as one of Judah\'s key defensive cities.</p><p>Lachish achieved particular historical prominence when Sennacherib of Assyria besieged it during his campaign against Hezekiah — an event depicted in the famous Lachish reliefs now in the British Museum. The city was later besieged again by Nebuchadnezzar prior to the fall of Jerusalem, and the Lachish Letters, ink inscriptions on pottery sherds found there, provide vivid evidence of that final period.</p>',
    'sections': [], 'hitchcock_meaning': 'who walks, or exists, of himself', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Joshua 10:3', 'Joshua 10:31', '2 Chronicles 11:9', '2 Kings 18:14']
  },
  'ladder': {
    'id': 'ladder', 'term': 'Ladder', 'category': 'concepts',
    'intro': '<p>The ladder of Scripture appears most memorably in Jacob\'s vision at Bethel, where he saw a ladder (or stairway) set on the earth with its top reaching to heaven, and the angels of God ascending and descending on it, with God standing above it and renewing the Abrahamic covenant. This vision assured Jacob of divine presence and protection as he fled to Haran. Jesus alludes to the image in John 1:51, declaring that the disciples will see heaven opened and angels ascending and descending on the Son of Man — presenting himself as the true ladder connecting earth and heaven, the mediator between God and humanity.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Genesis 28:12', 'John 1:51']
  },
  'laish': {
    'id': 'laish', 'term': 'Laish', 'category': 'places',
    'intro': '<p>Laish (meaning: <em>a lion</em>) was a Phoenician city in the far north of Canaan, noted for its peaceful and prosperous inhabitants who lived in security after the manner of the Sidonians. The tribe of Dan, unable to secure their allotted territory in the south, sent spies who reported Laish as a vulnerable conquest. The Danites subsequently attacked and captured it, renaming it Dan — the city that became the northernmost point of Israel (hence the phrase "from Dan to Beersheba"). Laish is also the name of the father of Palti (or Paltiel), to whom Saul gave Michal after separating her from David.</p>',
    'sections': [], 'hitchcock_meaning': 'a lion', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Judges 18:7', 'Judges 18:29', 'Joshua 19:47']
  },
  'lama': {
    'id': 'lama', 'term': 'Lama', 'category': 'concepts',
    'intro': '<p>Lama is the Aramaic word meaning "why" or "for what reason," appearing in the cry of desolation from the cross: "Eli, Eli, lama sabachthani" (Matthew 27:46; Mark 15:34) — "My God, my God, why have you forsaken me?" The cry is a verbatim quotation of Psalm 22:1, and it stands as the only instance in the Gospels where Jesus addresses God without using "Father." Theologians have discussed the cry at length as a window into the nature of Christ\'s atoning suffering, the depth of his identification with human dereliction, and the continuity of his human consciousness with the lament psalmody of Israel.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Matthew 27:46', 'Psalms 22:1']
  },
  'lamb': {
    'id': 'lamb', 'term': 'Lamb', 'category': 'concepts',
    'intro': '<p>The lamb occupied a central place in Israel\'s sacrificial system, serving as the required offering for the daily burnt offering (morning and evening), the Passover, various festival sacrifices, and a range of sin and peace offerings. The requirements of an unblemished, year-old male established the standard against which Israel\'s offering was measured. In the New Testament the lamb becomes a key christological image: John the Baptist identifies Jesus as "the Lamb of God who takes away the sin of the world," and the book of Revelation depicts the risen Christ as a Lamb bearing the marks of slaughter, who is worshipped alongside the Father as worthy to receive all glory.</p><p>The continuity between the Passover lamb of Exodus and the sacrificed Christ is drawn explicitly in 1 Corinthians 5:7 and 1 Peter 1:19.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Exodus 12:5', 'John 1:29', 'Revelation 5:6', '1 Peter 1:19']
  },
  'lamech': {
    'id': 'lamech', 'term': 'Lamech', 'category': 'people',
    'intro': '<p>Lamech (meaning: <em>poor; made low</em>) is the name of two men in early Genesis, from entirely separate genealogies. The first was a descendant of Cain and the first polygamist recorded in Scripture, who composed the "Song of the Sword" boasting of violence and seventy-sevenfold vengeance — a dark counterpart to God\'s sevenfold mark on Cain. The second Lamech was a descendant of Seth and the father of Noah, who named his son Noah saying "this one will bring us relief from the painful toil of our hands caused by the ground that the Lord has cursed."</p>',
    'sections': [], 'hitchcock_meaning': 'poor; made low', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Genesis 4:18', 'Genesis 5:25', 'Luke 3:36']
  },
  'lamentation': {
    'id': 'lamentation', 'term': 'Lamentation', 'category': 'concepts',
    'intro': '<p>Lamentation in Scripture is the formal expression of grief, typically over death, disaster, or divine judgment, and appears in a recognized literary genre of funeral songs and dirges. David\'s lament over Saul and Jonathan in 2 Samuel 1:17–27 and his dirge over Abner in 2 Samuel 3:33–34 are among the finest examples, as is Amos\'s lamentation over fallen Israel. Ezekiel composed a series of laments against Tyre and Egypt. The most sustained biblical lamentation is the book of Lamentations, attributed to Jeremiah, which mourns the destruction of Jerusalem.</p><p>Lament is treated in Scripture as an appropriate and even necessary response to suffering, and the psalms of lament — comprising nearly a third of the psalter — give the believing community language for honest complaint to God in the midst of affliction.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['2 Samuel 1:17', 'Amos 8:10', 'Ezekiel 27:2']
  },
  'lamentations-book-of': {
    'id': 'lamentations-book-of', 'term': 'Lamentations, Book of', 'category': 'concepts',
    'intro': '<p>The Book of Lamentations consists of five poetic dirges over the destruction of Jerusalem by the Babylonians in 586 B.C. The first four chapters are acrostic poems in Hebrew, each verse or section beginning with a successive letter of the alphabet — a formal structure that may suggest the completeness of Zion\'s grief. The fifth chapter is a communal prayer of sixty-six lines without the acrostic form. Tradition assigns authorship to Jeremiah, who is known to have composed laments and who witnessed the catastrophe, though the book does not name him.</p><p>The book\'s theology holds in tension the conviction that Jerusalem\'s fall was divine judgment for sin with the persistent cry for mercy, reaching its center in the declaration that the steadfast love of the Lord never ceases and his mercies are new every morning — one of the most beloved affirmations of hope in all of Scripture.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Lamentations 3:22', 'Lamentations 3:23', '2 Samuel 1:19']
  },
  'lamp': {
    'id': 'lamp', 'term': 'Lamp', 'category': 'concepts',
    'intro': '<p>The lamp of biblical times was typically a shallow clay dish or saucer filled with olive oil and fitted with a wick, though later forms included closed pinched-nose lamps and elaborate multi-branched lampstands of beaten gold. The golden lampstand (menorah) in the tabernacle and temple was the most sacred, kept burning continually before the Lord as a perpetual light before the veil. Lamps appear throughout Scripture as images of guidance, life, testimony, and divine presence: the word of God is "a lamp to my feet and a light to my path," and the Lord is said to be the lamp of those he loves.</p><p>In the New Testament, lamps figure prominently in the parable of the ten virgins and in Jesus\'s teaching on being the light of the world and letting one\'s light shine before men.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Exodus 25:37', '1 Kings 7:49', 'Psalms 119:105', 'Matthew 25:1']
  },
  'landmark': {
    'id': 'landmark', 'term': 'Landmark', 'category': 'concepts',
    'intro': '<p>Landmarks in ancient Israel were boundary stones or markers, often large unhewn boulders, set to delineate the borders of a family\'s inherited tribal allotment. Their removal was explicitly forbidden by Mosaic law as an act of theft against the family and against God\'s covenant arrangement of the land, and the book of Deuteronomy pronounces a curse on whoever moves a neighbor\'s boundary stone. Proverbs echoes the prohibition, extending it to the ancient boundaries established by ancestors. The practical importance of these markers in a largely pre-literate society, where land rights depended on physical markers rather than written deeds, made their protection a matter of social justice.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Deuteronomy 19:14', 'Deuteronomy 27:17', 'Proverbs 22:28', 'Job 24:2']
  },
  'laodicea': {
    'id': 'laodicea', 'term': 'Laodicea', 'category': 'places',
    'intro': '<p>Laodicea (meaning: <em>just people</em>) was a prosperous city in the Lycus River valley of Phrygia in Asia Minor, about forty miles east of Ephesus. Founded by the Seleucid king Antiochus II and named for his wife Laodice, it became wealthy through banking, textile manufacturing, and a renowned medical school known for its eye salve. Paul mentions it alongside Colossae and Hierapolis, and a letter carried by Epaphras ministered to the Laodicean church.</p><p>The church at Laodicea received the most severe of the seven letters in Revelation 3, rebuked for being "lukewarm" — neither hot nor cold — and for complacency born of wealth, contrasted sharply with Christ\'s offer of true gold, white garments, and eye salve. Its location between hot springs at Hierapolis and cold springs at Colossae may inform the "hot/cold" imagery.</p>',
    'sections': [], 'hitchcock_meaning': 'just people', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Revelation 3:14', 'Colossians 2:1', 'Colossians 4:15', 'Revelation 1:11']
  },
  'laodicea-epistle-from': {
    'id': 'laodicea-epistle-from', 'term': 'Laodicea, Epistle from', 'category': 'concepts',
    'intro': '<p>The "epistle from Laodicea" is mentioned in Colossians 4:16, where Paul instructs the Colossians to exchange letters with the Laodicean church — that they should read the letter from Laodicea, and ensure their letter is also read there. This has prompted long debate about the identity of the Laodicean letter: some identify it with Paul\'s letter to the Ephesians (which may have circulated as a general letter), others with a lost Pauline epistle, and others with the spurious apocryphal "Epistle to the Laodiceans" that appears in some Latin manuscripts but is generally regarded as a forgery of uncertain date.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Colossians 4:16']
  },
  'lapidoth': {
    'id': 'lapidoth', 'term': 'Lapidoth', 'category': 'people',
    'intro': '<p>Lapidoth (meaning: <em>enlightened; lamps</em>) was the husband of Deborah the prophetess and judge of Israel. He is mentioned only once in Scripture, in Judges 4:4, which identifies Deborah as "wife of Lapidoth." Nothing further is recorded about him, and the text\'s focus falls entirely on Deborah\'s role as prophetess, judge, and military leader who summoned Barak and accompanied Israel\'s army to battle against Jabin\'s general Sisera. Some scholars have proposed that "woman of Lapidoth" could be rendered "fiery woman" or "woman of torches," treating the phrase as a description of Deborah rather than a reference to her husband, though the traditional reading is a personal name.</p>',
    'sections': [], 'hitchcock_meaning': 'enlightened; lamps', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Judges 4:4']
  },
  'lapping': {
    'id': 'lapping', 'term': 'Lapping', 'category': 'concepts',
    'intro': '<p>Lapping refers to the manner of drinking water used by Gideon\'s soldiers at the spring of Harod, where God directed Gideon to reduce his army from 32,000 to 300 by observing how the men drank from the stream. Those who lapped the water with their tongues like dogs, keeping their heads up and weapons ready, were selected; those who knelt down to drink were sent home. The distinction preserved a vigilant, battle-ready attitude even at a moment of rest, and the selection of just three hundred men ensured that Israel could not claim credit for the coming victory over the Midianites.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Judges 7:5', 'Judges 7:6', 'Judges 7:7']
  },
  'lapwing': {
    'id': 'lapwing', 'term': 'Lapwing', 'category': 'concepts',
    'intro': '<p>The lapwing is listed among the unclean birds in the Mosaic dietary laws of Leviticus 11:19 and Deuteronomy 14:18. The identification of the Hebrew term <em>dukiphath</em> with the lapwing (a crested plover common in Palestine) follows the Septuagint and Vulgate translations and most standard English versions. The lapwing is a migratory bird well known in the region, and its inclusion in the list of prohibited birds places it alongside hoopoes and other species associated with carrion or impurity in ancient Near Eastern thought, though the precise criterion for uncleanness among birds is not stated in the text.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Leviticus 11:19', 'Deuteronomy 14:18']
  },
  'lasaea': {
    'id': 'lasaea', 'term': 'Lasaea', 'category': 'places',
    'intro': '<p>Lasaea was a city on the southern coast of Crete, mentioned in Acts 27:8 as lying "near" the harbor of Fair Havens where Paul\'s ship anchored during his voyage to Rome. The site has been identified with a small ruined harbor east of Fair Havens, and ancient remains confirm a settlement there in the first century. Lasaea\'s proximity to Fair Havens is the only significance it holds in the biblical narrative; the crew\'s debate over whether to winter at the nearby port of Phenice rather than at Fair Havens led directly to the storm and shipwreck of Acts 27.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Acts 27:8']
  },
  'lasha': {
    'id': 'lasha', 'term': 'Lasha', 'category': 'places',
    'intro': '<p>Lasha was a place mentioned in Genesis 10:19 as one of the boundary markers of Canaanite territory: "from Sidon in the direction of Gerar as far as Gaza, and in the direction of Sodom, Gomorrah, Admah, and Zeboiim as far as Lasha." Its precise location is uncertain, though ancient tradition often identified it with Callirrhoe, the hot springs east of the Dead Sea, or with Laish/Dan in the north. The reference serves to define the extent of Canaan\'s original territory as known in the Table of Nations.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Genesis 10:19']
  },
  'latchet': {
    'id': 'latchet', 'term': 'Latchet', 'category': 'concepts',
    'intro': '<p>A latchet was the thong or strap used to fasten a sandal to the foot. It appears in Scripture most memorably in the Baptist\'s declaration of humility: John the Baptist said he was not worthy to untie (or carry) the sandal latchet of the one coming after him — a task considered too menial even for a disciple\'s service to his teacher, being assigned only to slaves in Jewish custom. Isaiah\'s prophecy uses the same image of sandal straps as a measure of minimum strength, and Jesus alludes to the tradition in his comparison of himself to John.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Mark 1:7', 'Luke 3:16', 'Isaiah 5:27']
  },
  'latin': {
    'id': 'latin', 'term': 'Latin', 'category': 'concepts',
    'intro': '<p>Latin was the official administrative language of the Roman Empire and appears in Scripture in the trilingual inscription on the cross, which Pilate had written in Hebrew, Greek, and Latin (John 19:20) — the three languages representing the religious, intellectual, and political powers of the ancient world. Several Latin loanwords appear in the Greek New Testament, reflecting Roman administrative terminology: <em>centurion</em>, <em>denarius</em>, <em>legion</em>, <em>praetorium</em>, and others. The use of Latin in the inscription underscored the public and universal nature of the proclamation "Jesus of Nazareth, King of the Jews."</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['John 19:20']
  },
  'lattice': {
    'id': 'lattice', 'term': 'Lattice', 'category': 'concepts',
    'intro': '<p>A lattice in biblical contexts refers to an open framework of crossed strips — typically of wood — used in windows or balconies to allow light and air while providing a degree of concealment for those within. Sisera\'s mother and her attendants are pictured looking through a lattice window for his return from battle, and the beloved in Song of Solomon 2:9 sees her lover peering through the lattice. The lattice window through which King Ahaziah of Israel fell, sustaining fatal injuries, prompting his inquiry of Baal-zebub of Ekron, is the other prominent biblical reference.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Judges 5:28', '2 Kings 1:2', 'Song of Solomon 2:9']
  },
  'laver': {
    'id': 'laver', 'term': 'Laver', 'category': 'concepts',
    'intro': '<p>The laver was a large bronze basin of water positioned between the altar of burnt offering and the entrance to the tabernacle (and later the temple), in which the priests washed their hands and feet before entering the sanctuary or approaching the altar. Its function was ritual purification — not moral cleansing per se but the maintenance of the holiness required for priestly service. The laver of the tabernacle was made from the bronze mirrors donated by the women who served at the tent entrance.</p><p>In Solomon\'s temple the single laver was replaced by a great bronze sea (a massive basin resting on twelve oxen) and ten smaller lavers on wheeled stands. The New Testament builds on the imagery of the laver in references to the washing of regeneration and the cleansing of the church by the water of the word.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Exodus 30:18', 'Exodus 38:8', '1 Kings 7:23', '2 Chronicles 4:6']
  },
  'law': {
    'id': 'law', 'term': 'Law', 'category': 'concepts',
    'intro': '<p>Law in Scripture carries a range of meanings. At its broadest, it translates the Hebrew <em>torah</em>, which means instruction or teaching, encompassing all divine guidance and revelation from God. More narrowly, the Law refers to the Mosaic covenant code given at Sinai — the commandments, statutes, and ordinances governing Israel\'s religious and civil life as recorded in the Pentateuch. Paul distinguishes a law of nature written on the hearts of the Gentiles from the specific Mosaic legislation given to Israel, and argues throughout Romans and Galatians that the law, while holy and good, cannot justify — its purpose being to reveal sin and act as a custodian leading to Christ.</p><p>Jesus declared he came not to abolish the Law but to fulfill it, and the New Testament presents his death and resurrection as the fulfillment of the Law\'s sacrificial typology and the inauguration of a new covenant in which the law is written on the heart.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Romans 2:14', 'Romans 2:15', 'Matthew 5:17', 'Hebrews 7:9']
  },
  'law-of-moses': {
    'id': 'law-of-moses', 'term': 'Law of Moses', 'category': 'concepts',
    'intro': '<p>The Law of Moses refers to the body of legislation given through Moses at Sinai and recorded in Exodus, Leviticus, Numbers, and Deuteronomy, governing Israel\'s worship, morality, civil administration, and covenant relationship with God. It encompasses the Ten Commandments, the detailed cultic and ceremonial regulations for the priesthood and sacrificial system, the civil and criminal codes, and the covenant stipulations that bound Israel to exclusive loyalty to the Lord. The Law of Moses was the foundational document of Israel\'s national life: the standard for kings (2 Kings 23:25), the basis for temple service (Ezra 3:2), and the text publicly read at covenant renewals.</p><p>In the New Testament the Law of Moses is held in honor as the scripture of Israel while being fulfilled and in some respects superseded by Christ, whose new covenant establishes righteous standing not by legal observance but by faith.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Kings 2:3', 'Deuteronomy 4:8', 'Ezra 3:2', 'Luke 24:44']
  },
  'lawyer': {
    'id': 'lawyer', 'term': 'Lawyer', 'category': 'concepts',
    'intro': '<p>Lawyers in the New Testament context were not legal practitioners in the modern sense but interpreters and teachers of the Mosaic law — essentially synonymous with the scribes. They were experts in the written Torah and the tradition of its interpretation who advised courts, ruled on questions of legal application, and taught in synagogues. A lawyer tested Jesus with the question about the greatest commandment (Matthew 22:35), and the parable of the Good Samaritan was prompted by a lawyer\'s question about eternal life in Luke 10:25. Jesus rebuked lawyers in Luke 11 for loading others with legal burdens they would not lift themselves.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Matthew 22:35', 'Luke 10:25', 'Luke 11:46']
  },
  'lazarus': {
    'id': 'lazarus', 'term': 'Lazarus', 'category': 'people',
    'intro': '<p>Lazarus (meaning: <em>assistance of God</em> — Greek form of Hebrew Eleazar) is the name of two New Testament figures. The most prominent was the brother of Mary and Martha at Bethany whom Jesus raised from the dead after four days in the tomb — the greatest of John\'s seven signs and the event that precipitated the Sanhedrin\'s final decision to arrest Jesus. Lazarus appears again at the supper in Bethany where Mary anointed Jesus, and he became a target of the chief priests\' hostility because of the testimony his resurrection created.</p><p>The second Lazarus is the poor man of Jesus\'s parable in Luke 16, who lay at the gate of a rich man longing for crumbs. After both die, Lazarus rests in Abraham\'s bosom while the rich man suffers in Hades — the only parable in which a character is given a proper name.</p>',
    'sections': [], 'hitchcock_meaning': 'assistance of God', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['John 11:1', 'John 11:43', 'Luke 16:20']
  },
  'leaf': {
    'id': 'leaf', 'term': 'Leaf', 'category': 'concepts',
    'intro': '<p>Leaves in Scripture carry both literal and figurative significance. The olive leaf brought to Noah by the dove signaled the receding of the flood waters. Leaves are used as images of prosperity (a blessed man is like a tree planted by streams, whose leaf does not wither) and of futility or judgment (like a leaf driven by the wind in affliction, or the withered fig tree Jesus cursed as a sign of Israel\'s unfruitful religion). The tree of life in Revelation 22 bears leaves for the healing of the nations, reversing the curse of Eden and completing the symbolism of the leaf as an image of restoration and life.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Genesis 8:11', 'Psalms 1:3', 'Matthew 21:19', 'Revelation 22:2']
  },
  'league': {
    'id': 'league', 'term': 'League', 'category': 'concepts',
    'intro': '<p>A league in Scripture refers to a formal treaty or covenant of alliance between parties, most often between Israel and neighboring peoples or nations. The Mosaic law explicitly forbade Israel from making leagues with the Canaanite inhabitants of the land, for fear that such alliances would draw Israel into idolatry. The Gibeonite deception in Joshua 9 resulted in a league that Israel maintained even centuries later, at cost of life during Saul\'s reign. Later kings of Israel and Judah frequently made leagues with Egypt, Assyria, or Syria, which the prophets condemned as failures of trust in the Lord.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Exodus 23:32', 'Joshua 9:15', '2 Samuel 5:3']
  },
  'leah': {
    'id': 'leah', 'term': 'Leah', 'category': 'people',
    'intro': '<p>Leah (meaning: <em>weary; tired</em>) was the elder daughter of Laban of Haran and the first wife of Jacob, given to him by Laban\'s deception in place of her younger sister Rachel, for whom Jacob had served seven years. Though unloved compared to Rachel, Leah was the more fruitful: she bore Jacob six sons — Reuben, Simeon, Levi, Judah, Issachar, and Zebulun — and a daughter, Dinah. From Judah came the royal line of David and ultimately the Messiah; from Levi came the priestly tribe and Aaron. Scripture notes that God saw Leah\'s unloved condition and opened her womb as a divine act of compassion.</p><p>Leah was buried in the cave of Machpelah at Hebron alongside Abraham, Sarah, Isaac, and Rebekah — a dignity that underscores her place in the covenant family.</p>',
    'sections': [], 'hitchcock_meaning': 'weary; tired', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Genesis 29:16', 'Genesis 29:23', 'Genesis 49:31']
  },
  'leannoth': {
    'id': 'leannoth', 'term': 'Leannoth', 'category': 'concepts',
    'intro': '<p>Leannoth is a term in the heading of Psalm 88, typically rendered "Mahalath Leannoth" — understood as a musical notation indicating either the name of a tune to which the psalm was sung or a direction regarding its performance style. The word may derive from a Hebrew root meaning "to afflict" or "to answer (in singing)," suggesting an antiphonal or responsive mode of performance. Psalm 88 is one of the darkest psalms in the psalter, ending without resolution in the darkness, and the musical notation of grief matches its tone of unrelieved lament.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Psalms 88:1']
  },
  'leasing': {
    'id': 'leasing', 'term': 'Leasing', 'category': 'concepts',
    'intro': '<p>Leasing is an archaic English word meaning lying or falsehood, used in the Authorized Version of Psalms 4:2 and 5:6 to translate the Hebrew <em>kazab</em> (vanity, falsehood, lie). The psalmist laments those who "love leasing" — who seek after lies and delusions — and Psalm 5:6 declares that God destroys those who speak leasing. The word fell out of common English usage by the eighteenth century, but in the KJV context it consistently means deliberate deception or the telling of lies, reflecting the Old Testament\'s strong condemnation of falsehood as an offense against the God of truth.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Psalms 4:2', 'Psalms 5:6']
  },
  'leather': {
    'id': 'leather', 'term': 'Leather', 'category': 'concepts',
    'intro': '<p>Leather was a common material in the ancient Near East, produced from the hides of cattle, goats, and sheep by tanning and used for a wide range of practical items including sandals, girdles, water bottles, and writing surfaces (scroll material). Elijah and John the Baptist are both described as wearing leather girdles — a mark of prophetic austerity. Numbers 31:20 records the purification of leather goods captured in war. The tent coverings of the tabernacle included skins of rams dyed red and skins of sea cows (or badgers), providing weather-resistant outer layers for the portable sanctuary.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['2 Kings 1:8', 'Matthew 3:4', 'Numbers 31:20']
  },
  'leaven': {
    'id': 'leaven', 'term': 'Leaven', 'category': 'concepts',
    'intro': '<p>Leaven (yeast or sourdough starter) was excluded from all Israelite grain offerings and from the Passover observance, during which all leaven was removed from Israelite homes for seven days in commemoration of the hasty departure from Egypt. In the Mosaic law leaven represents that which corrupts and spreads through a whole mass, and its exclusion from sacrificial contexts signals the purity required in approaching God.</p><p>In the New Testament Jesus uses leaven in two contrasting ways: negatively, as the "leaven of the Pharisees and Sadducees" representing corrupt teaching that permeates; and positively, in the parable of the kingdom, where the woman mixes leaven into three measures of flour until it is all leavened — suggesting the quiet, pervasive growth of the kingdom. Paul employs the negative sense in 1 Corinthians, urging the church to purge the old leaven of malice and wickedness.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Exodus 12:15', 'Leviticus 2:11', 'Matthew 13:33', '1 Corinthians 5:7']
  },
  'lebanon': {
    'id': 'lebanon', 'term': 'Lebanon', 'category': 'places',
    'intro': '<p>Lebanon (meaning: <em>white; incense</em>) refers to the mountain range running parallel to the Mediterranean coast in what is now modern Lebanon, famous in antiquity for its towering cedars — the most prized timber in the ancient Near East. The "white" of the name reflects the snow that caps the peaks for much of the year. Solomon\'s temple was built largely of Lebanese cedar, transported by Phoenician craftsmen from Tyre as part of his alliance with Hiram, and the cedar became a recurring symbol of grandeur, majesty, and human pride in the prophets.</p><p>Lebanon appears frequently in the Song of Solomon as a landscape of beauty and fragrance, and in the prophetic literature its cedars are a symbol both of earthly glory and of God\'s judgment on the proud. Its northern range, Mount Hermon, was likely the site of the transfiguration.</p>',
    'sections': [], 'hitchcock_meaning': 'white, incense', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['1 Kings 8:65', '2 Kings 14:9', 'Song of Solomon 4:8', 'Numbers 34:8']
  },
  'lebbaeus': {
    'id': 'lebbaeus', 'term': 'Lebbaeus', 'category': 'people',
    'intro': '<p>Lebbaeus is a name appearing in some manuscripts of Matthew 10:3 for the apostle identified elsewhere as Thaddaeus and in Luke\'s lists as "Judas the son of James" (or Judas not Iscariot). The variation in manuscripts — some reading "Lebbaeus," others "Thaddaeus," and still others "Lebbaeus who was called Thaddaeus" — suggests these may be a surname, a nickname, or a scribal harmonization. Both names have been interpreted as meaning "heart" or "breast" in their respective Aramaic and Hebrew roots, suggesting a warm or courageous character. This apostle is otherwise nearly unknown in the canonical Gospels, appearing only in the lists and in John 14:22.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Matthew 10:3', 'Luke 6:16', 'John 14:22']
  },
  'lebonah': {
    'id': 'lebonah', 'term': 'Lebonah', 'category': 'places',
    'intro': '<p>Lebonah (meaning: <em>frankincense</em>, related to the same root as Lebanon) was a town near Shiloh in the hill country of Ephraim, mentioned in Judges 21:19 in connection with the annual festival at Shiloh during which the Benjamites abducted wives from among the dancing daughters of the city. The town is identified with the modern village of el-Lubban, located about three miles north of Shiloh on the road to Shechem, and its proximity to the sanctuary at Shiloh explains its role in the narrative of the tribal assembly.</p>',
    'sections': [], 'hitchcock_meaning': 'same as Labana', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Judges 21:19']
  },
  'leek': {
    'id': 'leek', 'term': 'Leek', 'category': 'concepts',
    'intro': '<p>Leeks are mentioned once in Scripture, in the complaint of the Israelites in the wilderness who recalled the produce of Egypt: "We remember the fish we ate in Egypt that cost nothing, the cucumbers, the melons, the leeks, the onions, and the garlic" (Numbers 11:5). The Hebrew word <em>hasir</em> corresponds to the leek (<em>Allium porrum</em>), a bulbous vegetable widely cultivated in ancient Egypt and still common in the region. The nostalgia for Egyptian food in the context of manna reflects the spiritual danger of preferring past comforts to present divine provision — a recurring motif in the wilderness narrative.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Numbers 11:5']
  },
  'lees': {
    'id': 'lees', 'term': 'Lees', 'category': 'concepts',
    'intro': '<p>Lees are the sediment or dregs that settle to the bottom of a wine vat after fermentation. Wine "settled on its lees" was considered full-flavored and rich — Isaiah uses the image positively in his vision of the messianic banquet where God will provide wine well aged on its lees for all peoples. But the prophets also use the image negatively: Zephaniah rebukes those who are complacently "settled on their lees" — stagnant, secure, and indifferent to God — and Jeremiah employs the metaphor of Moab undisturbed on its lees to describe a nation that has not been tested or refined by exile.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Isaiah 25:6', 'Zephaniah 1:12', 'Jeremiah 48:11']
  },
  'left-hand': {
    'id': 'left-hand', 'term': 'Left hand', 'category': 'concepts',
    'intro': '<p>In biblical usage the left hand generally carries connotations of inferiority, weakness, or the inauspicious, in contrast to the favored right hand. God\'s right hand is the symbol of strength, salvation, and honor; the right side is the place of honor at a throne. However, Scripture also uses left-hand navigation neutrally — "the left hand does not know what the right hand does" reflects secret generosity, not shame. In Job 23:9, the left side refers to a region from which God is absent. The distinction between the right and left in ancient Near Eastern culture ran deep in social custom, and the New Testament\'s parable of the sheep and goats places the condemned on the king\'s left hand.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Job 23:9', 'Genesis 14:15', 'Matthew 25:41']
  },
  'left-handed': {
    'id': 'left-handed', 'term': 'Left-handed', 'category': 'concepts',
    'intro': '<p>Left-handedness appears twice in Scripture in distinctly positive military contexts. Ehud the judge and deliverer of Israel was a left-handed Benjamite who used his ambidexterity to conceal a double-edged sword on his right thigh — opposite the side where guards would check — enabling him to assassinate the Moabite king Eglon. Among the Benjamite warriors listed in 1 Chronicles 12 were seven hundred who were left-handed, each able to sling stones at a hair\'s breadth without missing. These references suggest that left-handedness, while unusual, was recognized and cultivated as a tactical military advantage in Israelite warfare.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Judges 3:15', 'Judges 20:16', '1 Chronicles 12:2']
  },
  'legion': {
    'id': 'legion', 'term': 'Legion', 'category': 'concepts',
    'intro': '<p>A Roman legion was a military unit of approximately six thousand infantry soldiers, supplemented by cavalry and auxiliary troops, constituting the standard large-scale formation of the Roman army. The word appears in two New Testament contexts with different nuances. In the Gerasene demoniac narrative, the unclean spirit identifies itself as "Legion, for we are many" — a name evoking the overwhelming numbers of Roman soldiers and the terrifying magnitude of the man\'s possession. In Gethsemane, Jesus notes that he could call on his Father to send more than twelve legions of angels — a number exceeding the entire military power of Rome — underscoring the voluntariness of his submission to arrest.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Mark 5:9', 'Matthew 26:53']
  },
  'lehi': {
    'id': 'lehi', 'term': 'Lehi', 'category': 'places',
    'intro': '<p>Lehi (meaning: <em>jawbone</em>) was a place in the territory of Judah where Samson performed one of his most celebrated feats, slaying a thousand Philistines with the fresh jawbone of a donkey. After the battle, God miraculously caused water to spring from the hollow of the jawbone in answer to Samson\'s prayer for water, and the site was named En-hakkore ("the spring of the one who called"). The Philistines had gathered at Lehi specifically to seize Samson after he was handed over by the men of Judah, making the site the setting for both his greatest military exploit and a miracle of divine provision.</p>',
    'sections': [], 'hitchcock_meaning': 'jawbone', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Judges 15:9', 'Judges 15:14', 'Judges 15:16']
  },
  'lemuel': {
    'id': 'lemuel', 'term': 'Lemuel', 'category': 'people',
    'intro': '<p>Lemuel (meaning: <em>God with them, or him</em>) is identified in Proverbs 31:1 as a king whose mother taught him wisdom — specifically the counsel recorded in Proverbs 31:1–9 warning against women who destroy kings and against strong drink, and urging justice for the poor and needy. The identity of Lemuel has been debated: some ancient and modern interpreters identify him with Solomon (and his mother as Bathsheba), while others suggest he was a non-Israelite king, perhaps Ishmaelite. The chapter concludes (vv. 10–31) with the famous poem describing the capable wife, though its connection to Lemuel is thematic rather than attributed.</p>',
    'sections': [], 'hitchcock_meaning': 'God with them, or him', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Proverbs 31:1', 'Proverbs 31:4']
  },
  'lentiles': {
    'id': 'lentiles', 'term': 'Lentiles', 'category': 'concepts',
    'intro': '<p>Lentils (Hebrew <em>adashim</em>) are a small legume that formed a staple of the ancient Israelite diet, particularly among the poor. They appear in two memorable biblical episodes: Esau sold his birthright to Jacob for a pot of red lentil stew, in an act of impulsive disregard for his covenant inheritance that the New Testament cites as a warning against godlessness; and lentils were among the provisions brought to David by his supporters at Mahanaim during Absalom\'s revolt. Fields of lentils also appear in accounts of David\'s mighty men. The plant (<em>Lens culinaris</em>) is native to the Near East and was cultivated widely in ancient Canaan and Egypt.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Genesis 25:34', '2 Samuel 23:11', '2 Samuel 17:28']
  },
  'leopard': {
    'id': 'leopard', 'term': 'Leopard', 'category': 'concepts',
    'intro': '<p>The leopard (<em>Panthera pardus</em>) was present in ancient Palestine and Lebanon and appears in Scripture primarily in figurative and prophetic contexts. Isaiah\'s vision of the messianic age includes the remarkable image of the leopard lying down with the young goat, illustrating the radical transformation of the natural order. Jeremiah uses the leopard\'s inability to change its spots as a metaphor for the deeply ingrained sinfulness of Judah. Habakkuk describes Babylonian horses as swifter than leopards, and Daniel\'s third beast — representing Greece — has the form of a leopard with four wings. The Revelation beast from the sea has the body of a leopard, combining the imagery of all Daniel\'s empires.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Isaiah 11:6', 'Jeremiah 13:23', 'Habakkuk 1:8', 'Daniel 7:6']
  },
  'leprosy': {
    'id': 'leprosy', 'term': 'Leprosy', 'category': 'concepts',
    'intro': '<p>Leprosy in the Old Testament (Hebrew <em>tsara\'at</em>) encompassed a range of skin diseases, mold conditions in fabrics and walls, and other forms of ritual impurity, not necessarily equivalent to modern Mycobacterium leprae infection. The Mosaic law in Leviticus 13–14 provided detailed regulations for the diagnosis of leprous conditions by the priest and the ritual procedures for quarantine, examination, and eventual cleansing — including a complex two-bird purification ceremony. The disease produced social and religious exclusion, as the leper was required to live outside the camp and to warn approaching persons.</p><p>Notable biblical lepers include Miriam (struck with leprosy for criticizing Moses), Naaman the Syrian general (cleansed by Elisha), and the ten lepers healed by Jesus. Jesus\'s willingness to touch the leper while healing him was a deliberate act of compassionate boundary-crossing.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Leviticus 13:2', 'Numbers 12:10', 'Luke 17:12', 'Matthew 8:3']
  },
  'letter': {
    'id': 'letter', 'term': 'Letter', 'category': 'concepts',
    'intro': '<p>In its theological use in Paul\'s writings, the "letter" (Greek <em>gramma</em>) is contrasted with the "Spirit" — not as written text versus the spoken word, but as the literal written code of the law in its external, demanding character versus the inner transformative work of the Spirit in the new covenant. "The letter kills, but the Spirit gives life" (2 Corinthians 3:6) articulates the distinction: a legal code that condemns those who fail to keep it versus the life-giving power of the Spirit that enables conformity to God\'s will from within. Paul also uses "letter" to describe the physical mark of circumcision versus the inward circumcision of the heart, advancing the same covenant-of-the-heart theology.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Romans 2:27', '2 Corinthians 3:6', 'Romans 7:6']
  },
  'leummim': {
    'id': 'leummim', 'term': 'Leummim', 'category': 'people',
    'intro': '<p>Leummim (meaning: <em>countries; without water</em>) was a son of Dedan in the genealogy of the sons of Keturah, Abraham\'s wife after Sarah\'s death, and thus a grandson of Jokshan and great-grandson of Abraham. He is listed alongside his brothers Asshurim and Letushim as progenitors of peoples or tribes descended from the southern Arabian branch of Abraham\'s family. The name appears only once in Scripture and the peoples it represents have not been definitively identified with any known ancient group.</p>',
    'sections': [], 'hitchcock_meaning': 'countries; without water', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Genesis 25:3']
  },
  'levi': {
    'id': 'levi', 'term': 'Levi', 'category': 'people',
    'intro': '<p>Levi (meaning: <em>associated with him</em>) was the third son of Jacob and Leah, whose name was given at birth in Leah\'s hope that now her husband would be "joined" (lava) to her. Levi and his brother Simeon avenged the rape of their sister Dinah by slaughtering the men of Shechem, an act of vengeance that Jacob condemned on his deathbed and that resulted in Levi\'s tribe receiving no territorial inheritance in Canaan. Instead, by divine reversal, Levi\'s descendants were set apart as the priestly tribe — the Levites — distributed among the other tribes in forty-eight designated cities, their inheritance being the Lord himself and the tithes of Israel.</p><p>Moses and Aaron were descendants of Levi through Amram and Jochebed, and Levi\'s subsequent role as bearer of Israel\'s priesthood and sanctuary service became one of the defining structures of Old Testament religion.</p>',
    'sections': [], 'hitchcock_meaning': 'associated with him', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 29:34', 'Genesis 34:25', 'Exodus 6:16']
  },
  'leviathan': {
    'id': 'leviathan', 'term': 'Leviathan', 'category': 'concepts',
    'intro': '<p>Leviathan is a great sea creature described in Scripture with imagery that blends the natural and the mythological. In Job 41, God\'s challenge to Job concerning Leviathan is one of the most sustained and vivid descriptions of a creature in the Bible — fire-breathing, armored with scales, lord of the deep, whose breath kindles coals and smoke pours from his nostrils. Scholars debate whether this describes a real animal (the crocodile or a large sea creature) or a cosmic chaos-serpent drawn from ancient Near Eastern mythology, likely combining both.</p><p>Psalm 104 places Leviathan in the sea as a creature God formed to play there, while Isaiah 27:1 prophesies the Day of the Lord when God will punish "Leviathan the fleeing serpent, Leviathan the twisting serpent," and kill the dragon in the sea. This apocalyptic imagery is echoed in Revelation\'s dragon and sea beast.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Job 3:8', 'Psalms 104:26', 'Isaiah 27:1', 'Psalms 74:14']
  },
  'levirate-law': {
    'id': 'levirate-law', 'term': 'Levirate Law', 'category': 'concepts',
    'intro': '<p>The Levirate law (from Latin <em>levir</em>, brother-in-law) required that when a married man died without sons, his brother was obligated to marry the widow and raise up offspring in the dead brother\'s name, so that the family name and inheritance would not be extinguished in Israel. The law is codified in Deuteronomy 25:5–10, which also provided a release mechanism — the "sandal ceremony" — by which a brother could publicly renounce his obligation at cost of social shame. The story of Ruth and Boaz illustrates the operation of the custom, though Boaz was a more distant relative than a brother.</p><p>The Sadducees cited the Levirate law in their trick question to Jesus about the resurrection, presenting the case of a woman successively widowed by seven brothers.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Deuteronomy 25:5', 'Genesis 38:8', 'Ruth 4:10', 'Matthew 22:24']
  },
  'levite': {
    'id': 'levite', 'term': 'Levite', 'category': 'concepts',
    'intro': '<p>The Levites were the descendants of Levi, Jacob\'s third son, set apart by God as the tribe responsible for the service of the tabernacle and temple and the care of Israel\'s worship. The tribe was divided into three clans — Gershon, Kohath, and Merari — each assigned specific duties in transporting and maintaining the sanctuary and its furnishings. The Aaronic priests (a subset of the Kohathites) handled the sacrificial altar and the inner sanctuary, while the broader Levite body served as singers, gatekeepers, treasurers, and teaching assistants throughout Israel\'s cities.</p><p>The Levites received no tribal allotment of land but were sustained by the tithes of Israel and given forty-eight towns distributed among all the tribes. Their role as mediators of instruction and worship made them essential to Israel\'s covenant life, and Nehemiah\'s reforms reinvigorated their neglected service after the exile.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Numbers 3:6', 'Numbers 35:2', 'Joshua 21:41', 'Leviticus 25:32']
  },
  'leviticus': {
    'id': 'leviticus', 'term': 'Leviticus', 'category': 'concepts',
    'intro': '<p>Leviticus, the third book of the Pentateuch, is a manual of holiness and worship for Israel centered on the Mosaic covenant. It records the laws given to Moses at Sinai governing sacrificial offerings (Lev. 1–7), the ordination of the Aaronic priesthood (Lev. 8–10), laws of purity and impurity (Lev. 11–16, including the Day of Atonement), and the Holiness Code (Lev. 17–27) addressing ritual, sexual, social, and festival regulations. Its governing principle is summarized in God\'s repeated command: "Be holy, for I am holy."</p><p>The New Testament, especially the epistle to the Hebrews, interprets Leviticus\'s sacrificial system as a shadow of the greater reality of Christ\'s once-for-all atonement, his eternal high priesthood, and the access to God now available through his blood. Peter quotes the Levitical holiness command in 1 Peter 1:16, applying it to the new covenant community.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Leviticus 11:44', 'Leviticus 17:11', 'Hebrews 9:22', '1 Peter 1:16']
  },
  'levy': {
    'id': 'levy', 'term': 'Levy', 'category': 'concepts',
    'intro': '<p>A levy in the Old Testament refers to a compulsory draft of forced labor imposed by a ruler, corresponding to the Hebrew <em>mas</em>. Solomon imposed a levy of thirty thousand men from Israel who served in relays in Lebanon cutting timber for the temple, in addition to a permanent labor force drawn from the Canaanite peoples remaining in the land. The levy was administered through Adoniram (or Adoram), the official in charge of forced labor under David, Solomon, and Rehoboam. Rehoboam\'s refusal to lighten the levy was the immediate cause of the northern tribes\' revolt and the division of the kingdom.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['1 Kings 4:6', '1 Kings 5:13', '1 Kings 12:18']
  },
  'lewdness': {
    'id': 'lewdness', 'term': 'Lewdness', 'category': 'concepts',
    'intro': '<p>Lewdness in Scripture denotes shameless immorality, particularly sexual licentiousness or outrageous depravity. In the Old Testament the Hebrew term <em>zimmah</em> appears in contexts of cultic prostitution, incest, and sexual crimes condemned by Mosaic law. In the New Testament Greek, <em>aselgeia</em> (often rendered lewdness or licentiousness) describes unbridled sensuality and disregard for moral restraint — appearing in Paul\'s lists of vices and in 2 Peter\'s description of Lot\'s environment in Sodom. In the book of Acts, when the Corinthian Jews dragged Paul before Gallio and accused him, Gallio dismissed the case as involving no wrongdoing or vicious crime (lewdness), refusing to be a judge in matters of Jewish religious dispute.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Acts 18:14', 'Ezekiel 23:27', 'Galatians 5:19']
  },
  'libertine': {
    'id': 'libertine', 'term': 'Libertine', 'category': 'concepts',
    'intro': '<p>Libertines in Acts 6:9 refers to the "Synagogue of the Freedmen" (<em>Libertinon</em>), one of several synagogues in Jerusalem whose members disputed with Stephen. The term designates Jews who were former slaves or descendants of slaves who had obtained their freedom — most likely Jewish captives taken to Rome by Pompey in 63 B.C. who later returned to Jerusalem as freedmen. Their synagogue, along with those of Cyrenians, Alexandrians, Cilicians, and Asians, represented the Diaspora Jewish community in Jerusalem, and their confrontation with Stephen precipitated the crisis that led to his martyrdom.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Acts 6:9']
  },
  'libnah': {
    'id': 'libnah', 'term': 'Libnah', 'category': 'places',
    'intro': '<p>Libnah (meaning: <em>white; whiteness</em>) was a Canaanite royal city captured by Joshua during the southern campaign, subsequently assigned to the tribe of Judah and designated a Levitical city for the priests. It appears in the wilderness itinerary of Numbers as a stopping place of Israel, and in the period of the monarchy it gained importance as a fortified city on Judah\'s southwestern border. Libnah revolted against Jehoram of Judah, and it was near the town that the Assyrian army besieging Lachish received news of Tirhakah of Ethiopia\'s approach, prompting Sennacherib to send a second message to Hezekiah.</p>',
    'sections': [], 'hitchcock_meaning': 'white; whiteness', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Joshua 10:29', 'Joshua 12:15', '2 Kings 19:8', 'Numbers 33:20']
  },
  'libni': {
    'id': 'libni', 'term': 'Libni', 'category': 'people',
    'intro': '<p>Libni (meaning: <em>same as Libnah — white</em>) is the name of two men in the Old Testament. The first was the firstborn son of Gershon and grandson of Levi, from whom the Libnite family of Levites descended; his clan was responsible for portions of the tabernacle transport in the wilderness. The second Libni was a descendant of Merari son of Levi, listed in the genealogy of the singers appointed by David for the temple worship. Both men belong to the broader Levitical genealogies that structured Israel\'s priestly service.</p>',
    'sections': [], 'hitchcock_meaning': 'same as Libnah', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Exodus 6:17', 'Numbers 3:18', 'Numbers 3:21']
  },
  'libya': {
    'id': 'libya', 'term': 'Libya', 'category': 'places',
    'intro': '<p>Libya (meaning: <em>the heart of the sea; fat</em>) refers to the region of North Africa west of Egypt, corresponding to the territory known in Hebrew as Put or Phut. Its inhabitants appear among those present at Pentecost in Acts 2:10. Libya is also mentioned in prophetic contexts alongside Egypt and Ethiopia as a region allied with or conquered by major Near Eastern powers. The ancient Libyan people (the Lehabim and Ludim of the Table of Nations) were regarded as descendants of Ham through Mizraim, placing them in the broader family of Egypt\'s related peoples.</p>',
    'sections': [], 'hitchcock_meaning': 'the heart of the sea; fat', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Acts 2:10', 'Genesis 10:13', 'Ezekiel 30:5']
  },
  'lice': {
    'id': 'lice', 'term': 'Lice', 'category': 'concepts',
    'intro': '<p>Lice constitute the third plague of Egypt in the Exodus narrative, when Aaron stretched out his staff and struck the dust of the ground, which became gnats or lice throughout Egypt, afflicting both people and animals. The Hebrew term <em>kinnim</em> is variously translated as lice, gnats, or mosquitoes in different versions. The Egyptian magicians, who had replicated the first two plagues, were unable to produce this one and declared to Pharaoh, "This is the finger of God" — the first acknowledgment by Pharaoh\'s own court that a power beyond their own was at work. The plague represents God\'s sovereign authority over even the smallest creatures of the natural order.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Exodus 8:16', 'Psalms 105:31']
  },
  'lie': {
    'id': 'lie', 'term': 'Lie', 'category': 'concepts',
    'intro': '<p>Lying and falsehood are among the most consistently condemned sins in both Testaments, rooted in the character of God as the God of truth in whom there is no darkness. The ninth commandment ("You shall not bear false witness") specifically addressed false testimony in legal contexts, but the prophets and wisdom literature extend the prohibition to all deliberate deception. Jesus identifies the devil as "a liar and the father of lies" who does not stand in the truth. The New Testament epistles repeatedly command believers to put away falsehood and speak truth with their neighbors, grounding the command in the unity of the body of Christ. Revelation\'s catalog of those excluded from the holy city includes "everyone who loves and practices falsehood."</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['John 8:44', 'Revelation 21:27', '1 Timothy 1:10', 'Ephesians 4:25']
  },
  'lieutenant': {
    'id': 'lieutenant', 'term': 'Lieutenant', 'category': 'concepts',
    'intro': '<p>Lieutenant in the Authorized Version translates the Aramaic and Hebrew term <em>achashdarpanim</em> or <em>satraps</em> — the provincial governors appointed by the Persian kings to administer the empire\'s vast territories. These officials appear in the books of Esther and Ezra, where they are listed alongside governors and other royal officials as recipients of the king\'s decrees. The word rendered "lieutenant" in Esther 3:12 and elsewhere is more accurately translated "satrap" in modern versions, reflecting the well-documented Persian administrative title for the ruler of a major province.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Esther 3:12', 'Esther 8:9', 'Ezra 8:36']
  },
  'life': {
    'id': 'life', 'term': 'Life', 'category': 'concepts',
    'intro': '<p>Life in Scripture is understood as both a biological reality and a theological gift, with God alone as its ultimate source. The creation account presents God breathing the breath of life into the first human, making him a living soul — a unique act of divine animation. In the Old Testament, life is associated with the presence of God, the keeping of his commandments, and dwelling in the land of promise; death comes as the consequence of sin and separation from the divine source of life.</p><p>In the New Testament, <em>zoe</em> (life) takes on a deeper dimension in Jesus\'s teaching: he declares himself "the resurrection and the life" and "the way, the truth, and the life," and promises that those who believe in him will have eternal life — a present participation in the indestructible life of God that begins now and extends beyond physical death. John 3:16 frames the entire Gospel in terms of God\'s gift of eternal life to those who believe.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Genesis 2:7', 'John 3:16', 'John 11:25', 'Romans 6:4']
  },
  'light': {
    'id': 'light', 'term': 'Light', 'category': 'concepts',
    'intro': '<p>Light is one of Scripture\'s most pervasive theological symbols, established at the very opening of creation when God\'s first recorded act was the calling forth of light from darkness. Throughout the Old Testament God is associated with light: his face shining on Israel, his presence as a pillar of fire, his word as a lamp and light. The prophets envision the eschatological age as one of surpassing brightness, with the nations streaming to Zion\'s light.</p><p>In the New Testament Jesus declares himself "the light of the world" — a claim that identifies him with the divine light of God and with the light promised for the Gentiles in Isaiah 42. The prologue of John\'s Gospel identifies the Logos as the true light enlightening every person who comes into the world. Believers are called to walk as children of light, and Revelation\'s new Jerusalem needs no sun because the Lamb is its lamp and God its light.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Genesis 1:3', 'John 8:12', 'Isaiah 60:1', 'Revelation 21:23']
  },
  'lightning': {
    'id': 'lightning', 'term': 'Lightning', 'category': 'concepts',
    'intro': '<p>Lightning in Scripture is consistently associated with divine power, the divine presence, and judgment. God\'s appearance at Sinai was accompanied by lightning, thunder, and thick cloud. The psalms celebrate God as the one who sends lightning as arrows against his enemies, and Job\'s divine speeches invoke the lightning as an expression of God\'s power over creation that humanity cannot match. In the prophets and in Revelation, lightning accompanies throne-room visions as a mark of awesome divine majesty.</p><p>Jesus uses lightning as a metaphor for the sudden, universal visibility of his return: "as the lightning comes from the east and shines as far as the west, so will be the coming of the Son of Man" — an image that rules out any secret or localized manifestation. He also reported seeing Satan fall like lightning from heaven.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['2 Samuel 22:15', 'Psalms 135:7', 'Matthew 24:27', 'Luke 10:18']
  },
  'lign-aloes': {
    'id': 'lign-aloes', 'term': 'Lign-aloes', 'category': 'concepts',
    'intro': '<p>Lign-aloes (or aloes-wood) is the fragrant heartwood of the <em>Aquilaria</em> tree, a highly prized aromatic used in perfumery, incense, and burial preparations throughout the ancient Near East. In Scripture it appears in Balaam\'s blessing of Israel, compared to spreading tents and fragrant trees; in Psalm 45:8 among the garments of the anointed king; in Proverbs 7:17 as a perfume for the seducer\'s bed; and in John 19:39, where Nicodemus brings a mixture of myrrh and aloes for Jesus\'s burial. The "aloes" of Canticles and John likely refers to aloes-wood rather than the bitter medicinal aloe plant.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Numbers 24:6', 'Psalms 45:8', 'John 19:39']
  },
  'ligure': {
    'id': 'ligure', 'term': 'Ligure', 'category': 'concepts',
    'intro': '<p>Ligure is an archaic term used in the Authorized Version to translate the first stone of the third row of the high priest\'s breastplate (Exodus 28:19; 39:12). The identity of the Hebrew <em>leshem</em> is uncertain — proposed identifications include jacinth, amber, opal, tourmaline, and ligurite (a yellowish-green stone). Modern translations variously render it as jacinth, turquoise, or amber. Like all twelve stones of the breastplate, it bore the name of one of the twelve tribes of Israel, though ancient sources disagree on which tribe each stone represented. The uncertainty reflects the difficulty of matching ancient gemstone vocabulary to modern mineralogical classifications.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Exodus 28:19', 'Exodus 39:12']
  },
  'lily': {
    'id': 'lily', 'term': 'Lily', 'category': 'concepts',
    'intro': '<p>The lily of Scripture encompasses several flowering plants native to Palestine, most likely including the scarlet anemone, white narcissus, and the true lily (<em>Lilium candidum</em>). The Hebrew <em>shoshanah</em> and Greek <em>krinon</em> cover a range of flowers, and identifying the precise species in any given passage is difficult. In the Song of Solomon the beloved is "a lily of the valleys" and her beloved grazes among lilies — the flower becoming an image of beauty, love, and the beloved\'s character. Temple decorations incorporated lily designs on the capitals of Jachin and Boaz. Jesus\'s reference to "the lilies of the field" surpassing Solomon\'s glory teaches freedom from anxiety and trust in divine provision.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Song of Solomon 2:1', 'Matthew 6:28', 'Matthew 6:29', '1 Kings 7:22']
  },
  'lime': {
    'id': 'lime', 'term': 'Lime', 'category': 'concepts',
    'intro': '<p>Lime (calcium oxide, produced by burning limestone) had two distinct applications in Scripture. Deuteronomy 27:2–4 records Moses\'s command to set up large stones coated with lime (plaster) on Mount Ebal and to write the law upon them — a method of inscription also attested in Egyptian and Mesopotamian practice. The prophetic use is darker: Amos 2:1 condemns Moab for burning the bones of the king of Edom to lime — a desecration of the dead by reducing human remains to a powdery ash. Isaiah 33:12 uses the image of bones burned to lime as a picture of divine judgment.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Deuteronomy 27:2', 'Isaiah 33:12', 'Amos 2:1']
  },
  'linen': {
    'id': 'linen', 'term': 'Linen', 'category': 'concepts',
    'intro': '<p>Linen, woven from flax, was the preeminent fabric of the ancient world and occupies a place of high significance in Israelite worship and biblical imagery. The priestly vestments of the tabernacle and temple were made of fine linen, and the high priest wore linen on the Day of Atonement. Egypt was the primary producer of fine linen in the ancient world, and its linen was a mark of wealth and status. In prophetic and apocalyptic literature linen garments signify purity and holiness: the angelic figures in Ezekiel, Daniel, and Revelation are clothed in linen, and Revelation 19 presents the righteous deeds of the saints as the fine linen in which the Bride of Christ is arrayed for the marriage of the Lamb.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Leviticus 13:47', 'Isaiah 19:9', 'Revelation 19:8', 'Luke 23:53']
  },
  'linen-yarn': {
    'id': 'linen-yarn', 'term': 'Linen-yarn', 'category': 'concepts',
    'intro': '<p>Linen yarn appears in 1 Kings 10:28 and 2 Chronicles 1:16 in the context of Solomon\'s horse trade with Egypt and Kue (Cilicia). The Hebrew phrase <em>mikveh</em> was long read as "linen yarn" in the Authorized Version, but modern scholarship has concluded that the term likely refers to Kue (a region in Asia Minor) rather than a textile commodity, and most modern translations render the verse as describing merchants who imported horses from Egypt and Kue at fixed prices. The "linen yarn" reading thus reflects an older misunderstanding of a geographical term.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['1 Kings 10:28', '2 Chronicles 1:16']
  },
  'lines': {
    'id': 'lines', 'term': 'Lines', 'category': 'concepts',
    'intro': '<p>Lines in Psalm 16:6 — "The lines have fallen for me in pleasant places; indeed, I have a beautiful inheritance" — refers to the measuring lines or cords used to mark out a tract of land when dividing an inheritance. The image draws on the practice of parceling tribal allotments in Canaan by measuring cord, and David uses it as a metaphor for the covenant relationship he enjoys with God: his portion, his inheritance, is God himself, and the boundaries drawn for him are beautiful. The image appears in other psalms and in Zechariah\'s vision of a measuring line marking Jerusalem\'s restoration.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Psalms 16:6', 'Zechariah 2:1']
  },
  'lintel': {
    'id': 'lintel', 'term': 'Lintel', 'category': 'concepts',
    'intro': '<p>The lintel is the horizontal beam or stone spanning the top of a doorway, supporting the wall above. At the first Passover, the Israelites were commanded to strike the lintel and two doorposts of their houses with the blood of the Passover lamb, and God declared that when he saw the blood he would pass over that door and not strike its inhabitants. This act of blood-marking the entrance of the home established the doorway as the threshold of protection, a ritual whose theological weight carried forward into the new covenant\'s understanding of Christ\'s blood as the ground of the believer\'s safety from judgment. Amos\'s vision of God standing at the altar commanded that the capitals (or lintel) be struck so that the thresholds shake.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Exodus 12:22', 'Exodus 12:23', 'Amos 9:1']
  },
  'lions': {
    'id': 'lions', 'term': 'Lions', 'category': 'concepts',
    'intro': '<p>The lion (<em>Panthera leo</em>) was once present throughout the ancient Near East, including Palestine, and is the most frequently mentioned wild animal in Scripture. It appears in both literal and figurative contexts. Lions killed prophets who disobeyed God\'s word, threatened travelers, and are most famously the agents of God\'s providential protection in the den of lions narrative of Daniel 6. Figuratively the lion represents power, courage, and royalty: Judah is likened to a lion\'s cub in Jacob\'s blessing; Solomon\'s throne was flanked by lions; and the Messiah is called "the Lion of the tribe of Judah" in Revelation. Peter uses the image of a prowling lion to describe the devil seeking souls to devour.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Amos 3:4', 'Daniel 6:22', '1 Peter 5:8', 'Revelation 5:5']
  },
  'lip': {
    'id': 'lip', 'term': 'Lip', 'category': 'concepts',
    'intro': '<p>In biblical usage lips frequently stand by metonymy for speech, language, and the power of words. "Lip" (<em>saphah</em> in Hebrew) is regularly used to denote language itself — the Tower of Babel narrative describes the original unity of humanity as "one lip" (one language), and Isaiah\'s cleansing vision at the temple involves a seraph touching his lips with a coal to purify them for prophetic speech. The psalms speak of God holding lips back or opening them, and the prophets warn of lips that honor God while the heart is far from him.</p><p>In the New Testament the word and testimony of the believer are grounded in the heart\'s belief and the mouth\'s confession, and the epistle to the Hebrews calls the believer\'s praise "the fruit of lips that acknowledge his name."</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Isaiah 37:29', 'Hebrews 13:15', 'Isaiah 6:7', '1 Kings 7:26']
  },
}

def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f"BP l1: Laban → Lip: wrote {written}, skipped {skipped} existing.")

main()
