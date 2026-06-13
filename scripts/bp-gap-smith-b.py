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
"image": {
  "id": "image",
  "term": "Image",
  "category": "concepts",
  "intro": "<p>\"Image\" in biblical usage refers primarily to representations made for worship — what the Bible calls idols. The Second Commandment forbids the making of any carved image or likeness as an object of worship (<strong>Ex. 20:4–5</strong>; <strong>Deut. 5:8</strong>). The prophets ridiculed idol manufacture, pointing out the absurdity of cutting a tree and using half for firewood and half for a god (<strong>Isa. 44:13–20</strong>; <strong>Jer. 10:3–5</strong>). The Hebrew terms include <em>pesel</em> (carved image), <em>massekah</em> (molten image), and <em>tselem</em> (likeness or statue).</p><p>The \"image of God\" (<em>tselem Elohim</em>) in <strong>Genesis 1:26–27</strong> uses the same root but carries an entirely different meaning — humans are made in the image and likeness of God, giving them inherent dignity and the capacity for moral and relational reflection of the divine character. The NT applies this concept to Christ, who is \"the image of the invisible God\" (<strong>Col. 1:15</strong>), and to believers who are being conformed to that image (<strong>Rom. 8:29</strong>; <strong>2 Cor. 3:18</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Exodus 20:4", "Genesis 1:26", "Colossians 1:15", "Isaiah 44:17"]
},
"inheritance": {
  "id": "inheritance",
  "term": "Inheritance",
  "category": "concepts",
  "intro": "<p>In the Old Testament, inheritance (<em>nahalah</em>) was primarily the ancestral land portion allotted to each tribe and family in Canaan, held in perpetuity as God's gift and never to be permanently alienated (<strong>Num. 27:8–11</strong>; <strong>Lev. 25:23–28</strong>). The laws of inheritance passed property from father to son, with the firstborn receiving a double portion (<strong>Deut. 21:17</strong>). Daughters inherited only when there were no sons (<strong>Num. 27:1–11</strong>). The Jubilee year restored alienated land to its original family every fifty years.</p><p>In the New Testament, inheritance language is transferred to the spiritual realm. Believers are \"heirs of God and co-heirs with Christ\" (<strong>Rom. 8:17</strong>), inheriting eternal life and the kingdom prepared since the foundation of the world (<strong>Matt. 25:34</strong>). The Holy Spirit is the \"guarantee\" (<em>arrabon</em>) of the coming inheritance (<strong>Eph. 1:14</strong>; <strong>1 Pet. 1:4</strong>), and adoption into God's family confers the legal status of heirs alongside the natural Son.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Numbers 27:8", "Romans 8:17", "Ephesians 1:14", "1 Peter 1:4"]
},
"jesurun": {
  "id": "jesurun",
  "term": "Jesurun",
  "category": "concepts",
  "intro": "<p>Jesurun (also spelled Jeshurun; meaning: <em>the upright one</em>) is a poetic name for Israel used four times in Scripture, always with an affectionate or honorific connotation. It appears in <strong>Deuteronomy 32:15</strong> (the Song of Moses), <strong>33:5</strong>, <strong>33:26</strong>, and once in <strong>Isaiah 44:2</strong>. The name comes from the Hebrew root <em>yashar</em>, \"upright\" or \"straight,\" and idealizes Israel as the nation God intended it to be — upright, covenant-faithful, and beloved.</p><p>In Deuteronomy 32:15, the name is used with painful irony: \"Jeshurun grew fat and kicked — you were fat, stout, and sleek; then he forsook God who made him.\" The contrast between the ideal expressed by the name and Israel's actual rebellion heightens the prophetic pathos. Isaiah 44:2 uses it as a tender term of address: \"Fear not, O Jacob my servant, Jeshurun whom I have chosen\" — reassuring the exiles of God's ongoing election and care despite their failure.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Deuteronomy 32:15", "Deuteronomy 33:26", "Isaiah 44:2"]
},
"jesus-christ": {
  "id": "jesus-christ",
  "term": "Jesus Christ",
  "category": "people",
  "intro": "<p>Jesus (Greek form of Joshua, meaning <em>the LORD saves</em>) Christ (meaning <em>the Anointed One</em>, the Greek equivalent of Hebrew <em>Messiah</em>) is the central figure of the New Testament and of Christian faith — the eternal Son of God incarnate, born of the Virgin Mary in Bethlehem during the reign of Herod the Great. His public ministry began at approximately thirty years of age with his baptism by John and lasted roughly three years in Galilee, Judea, and the surrounding regions. He proclaimed the kingdom of God, gathered twelve apostles, taught with unprecedented authority, performed miracles of healing and nature, and welcomed sinners and outcasts.</p><p>He was crucified under Pontius Pilate outside Jerusalem approximately A.D. 30, was buried, and rose bodily from the dead on the third day — an event the apostles regarded as the validation of all his claims (<strong>Rom. 1:4</strong>; <strong>1 Cor. 15:3–8</strong>). He ascended to the Father's right hand and poured out the Holy Spirit at Pentecost. The NT confesses him as both Lord and Christ (<strong>Acts 2:36</strong>), the image of the invisible God (<strong>Col. 1:15</strong>), and the one through whom all things were made (<strong>John 1:1–3</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["John 1:14", "Acts 2:36", "Romans 1:4", "1 Corinthians 15:4"]
},
"jewel": {
  "id": "jewel",
  "term": "Jewel",
  "category": "concepts",
  "intro": "<p>Precious stones appear throughout Scripture as items of great value, symbols of beauty and divine glory, and components of priestly regalia. The high priest's breastplate contained twelve gems, one for each tribe of Israel, set in four rows of three (<strong>Ex. 28:17–20</strong>): sardius, topaz, carbuncle; emerald, sapphire, diamond; jacinth, agate, amethyst; beryl, onyx, and jasper. The precise identification of these Hebrew gem names with modern stones is often uncertain.</p><p>Precious stones appear in the description of the garden of Eden (<strong>Ezek. 28:13</strong>), in descriptions of divine glory (the sapphire throne in <strong>Ezek. 1:26</strong>), and extensively in the New Jerusalem of Revelation (<strong>Rev. 21:18–21</strong>), where the city's foundations are adorned with twelve precious stones corresponding to the apostles. The metaphorical use is also prominent: Proverbs compares a good wife to rubies (<strong>Prov. 31:10</strong>), and Malachi describes the faithful remnant as God's treasured jewels (<strong>Mal. 3:17</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Exodus 28:17", "Revelation 21:19", "Malachi 3:17", "Proverbs 31:10"]
},
"john-the-apostle": {
  "id": "john-the-apostle",
  "term": "John the Apostle",
  "category": "people",
  "intro": "<p>John son of Zebedee, a Galilean fisherman and brother of James, was one of the Twelve and a member of Jesus's innermost circle alongside Peter and James. He is traditionally identified as the \"beloved disciple\" of the Fourth Gospel who reclined at Jesus's side at the Last Supper (<strong>John 13:23</strong>), stood at the cross (<strong>John 19:26</strong>), and outran Peter to the empty tomb (<strong>John 20:4</strong>). Jesus gave him and James the epithet Boanerges — \"sons of thunder\" (<strong>Mark 3:17</strong>) — indicating a vehemence that also showed in their request to call down fire on a Samaritan village (<strong>Luke 9:54</strong>).</p><p>After Pentecost, John was a pillar of the Jerusalem church alongside Peter and James the Lord's brother (<strong>Gal. 2:9</strong>). He is traditionally credited with the Fourth Gospel, three epistles, and Revelation, written during a long ministry at Ephesus that ended with his exile to Patmos under Domitian. He is the only one of the Twelve not to have died a martyr's death, living to extreme old age.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["John 13:23", "Mark 3:17", "Galatians 2:9", "John 19:26"]
},
"judas-maccabaeus": {
  "id": "judas-maccabaeus",
  "term": "Judas Maccabaeus",
  "category": "people",
  "intro": "<p>Judas Maccabaeus (died 160 B.C.) was the third son of Mattathias the priest and the greatest military leader of the Maccabean revolt against the Seleucid king Antiochus IV Epiphanes. When Antiochus desecrated the Jerusalem temple in 167 B.C. by erecting an altar to Zeus and forbidding Jewish practice, Mattathias and his sons led a resistance movement. After his father's death, Judas took command, winning a series of improbable victories against much larger Seleucid forces.</p><p>In 164 B.C. he recaptured Jerusalem, cleansed the temple, and rededicated it — the event commemorated in the Jewish festival of Hanukkah. He is the hero of 1 Maccabees and 2 Maccabees (Apocrypha) and is referenced in <strong>Hebrews 11:34</strong> (in the tradition that identifies him among those who \"became mighty in war\"). He was killed in battle at Elasa in 160 B.C. His brothers Jonathan and Simon continued the dynasty after him.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Hebrews 11:34", "Daniel 11:32"]
},
"judas-of-galilee": {
  "id": "judas-of-galilee",
  "term": "Judas of Galilee",
  "category": "people",
  "intro": "<p>Judas of Galilee (also called a Gaulonite of Gamala by Josephus) led a popular revolt against Rome at the time of the census conducted under Quirinius the governor of Syria in A.D. 6. He taught that submission to the Roman census and taxation was an act of treason against God, the sole king of Israel, and gathered a large following. The revolt was suppressed and Judas himself was killed.</p><p>He is mentioned by Gamaliel in his speech before the Sanhedrin as a cautionary example of a failed messianic movement: \"Judas the Galilean rose up in the days of the census and drew away some of the people after him. He too perished, and all who followed him were scattered\" (<strong>Acts 5:37</strong>). Josephus identifies his followers — the Zealots and Sicarii — as his ideological descendants who continued his anti-Roman ideology up to the Jewish War of A.D. 66–70.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Acts 5:37"]
},
"judas-the-lords-brother": {
  "id": "judas-the-lords-brother",
  "term": "Judas, the Lord's Brother",
  "category": "people",
  "intro": "<p>Judas (also called Jude) is listed among the brothers of Jesus in <strong>Matthew 13:55</strong> and <strong>Mark 6:3</strong>, where the people of Nazareth name \"James, Joseph, Simon, and Judas\" alongside Jesus. He is traditionally identified with Jude the author of the short epistle that bears that name in the NT — who identifies himself only as \"Jude, a servant of Jesus Christ and brother of James\" (Jude 1:1), not claiming apostolic status, which is consistent with the gospel note that Jesus's brothers did not believe in him during his ministry (<strong>John 7:5</strong>).</p><p>Whether this Judas is the same as the apostle \"Judas (not Iscariot)\" of <strong>John 14:22</strong> remains disputed. The epistle of Jude addresses false teaching, appeals to the faith \"once for all delivered to the saints,\" and cites the apocryphal book of 1 Enoch. It was accepted as canonical after some early debate.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Matthew 13:55", "Mark 6:3", "Jude 1:1", "John 7:5"]
},
"leper-leprosy": {
  "id": "leper-leprosy",
  "term": "Leprosy",
  "category": "concepts",
  "intro": "<p>Biblical leprosy (<em>tsara'at</em> in Hebrew; <em>lepra</em> in Greek) was a broad category of skin diseases governed by detailed priestly diagnosis in <strong>Leviticus 13–14</strong>. The characteristic OT form was a white spreading condition covering large surfaces of skin, seen in Miriam (<strong>Num. 12:10</strong>), Naaman (<strong>2 Kings 5:1</strong>), Gehazi (<strong>2 Kings 5:27</strong>), and Moses as a temporary sign (<strong>Ex. 4:6</strong>). The Mosaic law required the leper to be isolated, cry \"Unclean! Unclean!\" and follow an elaborate purification rite after healing. These regulations made leprosy a powerful symbol of sin's defilement.</p><p>Modern scholars recognize that biblical \"leprosy\" encompassed conditions beyond modern Hansen's disease (Mycobacterium leprae), including psoriasis and other skin disorders. In the NT, Jesus healed lepers as a sign of the messianic age (<strong>Matt. 8:2–3</strong>; <strong>Luke 17:12–14</strong>), and his willingness to touch the unclean made these healings also acts of social restoration. He cited his healing of lepers as evidence of his identity to John's disciples (<strong>Matt. 11:5</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Leviticus 13:2", "Matthew 8:3", "Luke 17:14", "Numbers 12:10"]
},
"levites": {
  "id": "levites",
  "term": "Levites",
  "category": "people",
  "intro": "<p>The Levites were the members of the tribe of Levi who were set apart for sanctuary service but were not priests (the priests being restricted to Aaron's line within the tribe). They served as assistants to the Aaronic priests, transporting and caring for the tabernacle's structural elements (<strong>Num. 3–4</strong>), serving as musicians, gatekeepers, and administrators of the temple. The name sometimes extends to the whole tribe including the priests, and sometimes specifically designates the non-priestly Levites in contrast to the priests (<strong>Josh. 3:3</strong>; <strong>Ezek. 44:15</strong>).</p><p>Because the Levites received no tribal land allotment — \"the LORD is their inheritance\" (<strong>Deut. 18:2</strong>) — they were distributed among the other tribes in 48 designated Levitical cities (<strong>Num. 35:1–8</strong>) and supported by tithes from the other tribes. After the exile, the Levites are less numerous in the return lists. In the NT, a Levite appears in the parable of the Good Samaritan (<strong>Luke 10:32</strong>), and Barnabas was a Levite from Cyprus (<strong>Acts 4:36</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Numbers 3:6", "Deuteronomy 18:2", "Luke 10:32", "Acts 4:36"]
},
"libertines": {
  "id": "libertines",
  "term": "Libertines",
  "category": "people",
  "intro": "<p>The Libertines (Greek <em>Libertinoi</em>) were members of a synagogue in Jerusalem who opposed Stephen and brought about his arrest and martyrdom (<strong>Acts 6:9</strong>). The term most likely refers to freedmen — Jews who had been taken captive to Rome at some point (perhaps under Pompey in 63 B.C. or subsequent campaigns) and later freed, or their descendants, who maintained a distinct synagogue in Jerusalem.</p><p>Acts 6:9 mentions the \"Synagogue of the Freedmen (Libertines) and of the Cyrenians and Alexandrians and those from Cilicia and Asia,\" which may represent a single synagogue composed of these diverse diaspora Jewish communities or possibly several synagogues listed together. These Hellenistic Jews stirred up the people against Stephen, produced false witnesses, and dragged him before the Sanhedrin — where his defense speech, the longest in Acts, culminated in his vision of the glorified Christ and his stoning.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Acts 6:9", "Acts 6:12", "Acts 7:58"]
},
"lion": {
  "id": "lion",
  "term": "Lion",
  "category": "concepts",
  "intro": "<p>The lion (<em>aryeh</em> in Hebrew; <em>leon</em> in Greek) was once native to the lands of the Bible, common enough in biblical times that nearly every tribe of Palestine knew it as a real threat. The Bible uses the lion more frequently in metaphor than any other animal. David killed a lion while defending his flocks (<strong>1 Sam. 17:34–36</strong>), and Samson killed one with his bare hands (<strong>Judg. 14:5–6</strong>). Daniel was cast into a den of lions (<strong>Dan. 6</strong>).</p><p>As a metaphor the lion stands for power, courage, and ferocity — both divine and demonic. God and his agents appear in lion-like imagery: \"The LORD will roar from Zion\" (<strong>Amos 1:2</strong>; <strong>Hos. 11:10</strong>). The devil prowls \"like a roaring lion\" seeking someone to devour (<strong>1 Pet. 5:8</strong>). Christ is \"the Lion of the tribe of Judah\" (<strong>Rev. 5:5</strong>) — an image rooted in Jacob's blessing of Judah as a \"lion's cub\" (<strong>Gen. 49:9</strong>). The lion appears in Ezekiel's and John's visions of the four living creatures surrounding the divine throne (<strong>Ezek. 1:10</strong>; <strong>Rev. 4:7</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Revelation 5:5", "1 Peter 5:8", "Genesis 49:9", "Daniel 6:22"]
},
"maccabees-books-of": {
  "id": "maccabees-books-of",
  "term": "Maccabees, Books of",
  "category": "concepts",
  "intro": "<p>The Books of Maccabees are four works bearing the common title \"Maccabees\" found in manuscripts of the Septuagint. The first two were included in the early Latin Bible and Vulgate and were declared canonical by the Council of Trent (1546); they are retained as Apocrypha by Protestant churches. <strong>1 Maccabees</strong> covers the Maccabean revolt from the accession of Antiochus IV Epiphanes (175 B.C.) to the death of Simon Maccabaeus (134 B.C.), written in Hebrew (surviving only in Greek), and is considered historically reliable. <strong>2 Maccabees</strong> covers part of the same period with a more theological and hortatory style, emphasizing providence, martyrdom, and the resurrection of the dead.</p><p><strong>3 Maccabees</strong> (not about the Maccabean revolt) and <strong>4 Maccabees</strong> (a philosophical treatise on reason and passions) are later compositions with narrower circulation. The Maccabean literature provides essential historical background for understanding the intertestamental period, including Hanukkah, the development of resurrection doctrine, and the political context into which Jesus was born.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Daniel 11:32", "Hebrews 11:35"]
},
"meat-offering": {
  "id": "meat-offering",
  "term": "Meat Offering",
  "category": "concepts",
  "intro": "<p>The \"meat offering\" (KJV) is a misleading translation: the Hebrew <em>minchah</em> denotes a grain or cereal offering made of fine flour, with no animal flesh involved. Modern versions render it \"grain offering\" (<strong>Lev. 2:1</strong>). It was offered in several forms: raw fine flour with oil and frankincense, baked loaves, wafers, or fried cakes — always made with salt and without leaven or honey (<strong>Lev. 2:11–13</strong>). A priest burned a \"handful\" (the memorial portion) on the altar; the remainder belonged to the priests as most holy food.</p><p>The grain offering accompanied burnt offerings and peace offerings and could also stand alone as a tribute to God. It represented the dedication of the fruit of human labor — the result of agricultural work — to God. The NT interprets such offerings typologically as foreshadowing the perfect self-offering of Christ and the worship offered by believers as a \"living sacrifice\" (<strong>Rom. 12:1</strong>). Ezekiel's temple vision includes a restored grain offering in the new order (<strong>Ezek. 45:15–17</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Leviticus 2:1", "Leviticus 2:13", "Numbers 15:4", "Romans 12:1"]
},
"metals": {
  "id": "metals",
  "term": "Metals",
  "category": "concepts",
  "intro": "<p>The ancient Hebrews knew and used nearly all metals known to the ancient world. Gold was prized from the earliest times — Havilah's gold is mentioned in <strong>Genesis 2:11–12</strong>, and Abraham was \"very rich in... silver and gold\" (<strong>Gen. 13:2</strong>). Silver served as the standard medium of exchange before coinage (<strong>Gen. 23:16</strong>). Copper (rendered \"brass\" or \"bronze\" in older translations) was used extensively for tools, vessels, and the great bronze objects of the tabernacle and temple — the laver, altar, and sea (<strong>Ex. 27:2</strong>; <strong>1 Kings 7:23</strong>).</p><p>Iron came into widespread use after the Exodus period; the Philistines controlled iron technology during the judges era, giving them a strategic advantage over Israel (<strong>1 Sam. 13:19–22</strong>). Lead was known (<strong>Job 19:24</strong>; <strong>Jer. 6:29</strong>), as were tin and antimony. The processing of metals — smelting, casting, forging — provided the prophets with rich metaphors for divine judgment and purification (<strong>Isa. 1:25</strong>; <strong>Jer. 6:29</strong>; <strong>Ezek. 22:18–22</strong>; <strong>Mal. 3:2–3</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Genesis 2:11", "Exodus 27:2", "1 Samuel 13:19", "Malachi 3:3"]
},
"modin": {
  "id": "modin",
  "term": "Modin",
  "category": "places",
  "intro": "<p>Modin (or Modein) was the hometown of Mattathias and the birthplace of the Maccabean revolt. Located in the Shephelah foothills northwest of Jerusalem, approximately midway between Lydda and Jerusalem, the town features prominently in 1 Maccabees. When Antiochus IV's officers came to Modin to compel the Jews to offer pagan sacrifices, Mattathias killed both a fellow Jew who was about to comply and the royal officer, then fled to the wilderness with his sons — the opening act of the revolt.</p><p>After Judas Maccabaeus died, his brothers were buried at Modin, and Simon built an elaborate family tomb there (<strong>1 Macc. 13:25–30</strong>), described as adorned with carved ships and visible from the sea. The site has been tentatively identified with Khirbet el-Midyeh near the modern Israeli city of Modi'in, though the identification remains debated. Modin is not mentioned in the canonical Old or New Testament.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": []
},
"moneychangers": {
  "id": "moneychangers",
  "term": "Moneychangers",
  "category": "people",
  "intro": "<p>The moneychangers in the Jerusalem temple provided the half-shekel required for the annual temple tax (<strong>Ex. 30:13–15</strong>), exchanging the various foreign currencies carried by diaspora Jews into the Tyrian shekel, which the temple accepted. They set up tables in the Court of the Gentiles, especially in the weeks before Passover when pilgrims from across the known world converged on Jerusalem. A premium (commission) was charged for the exchange.</p><p>Jesus drove the moneychangers out of the temple on at least one occasion — the Synoptics place it during Passion Week (<strong>Matt. 21:12–13</strong>; <strong>Mark 11:15–17</strong>; <strong>Luke 19:45–46</strong>), while John places a similar act at the beginning of his ministry (<strong>John 2:13–17</strong>). Jesus cited Isaiah 56:7 (\"my house shall be called a house of prayer\") and Jeremiah 7:11 (\"den of robbers\") as he overturned the tables and drove them out, denouncing the commercial exploitation of the sacred space.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Matthew 21:12", "John 2:14", "Exodus 30:13", "Mark 11:17"]
},
"mourning": {
  "id": "mourning",
  "term": "Mourning",
  "category": "concepts",
  "intro": "<p>Mourning customs in the ancient Near East were highly ritualized and intensely public. Biblical mourning practices included: tearing garments (<strong>Gen. 37:29</strong>; <strong>Job 1:20</strong>), putting on sackcloth (<strong>2 Sam. 3:31</strong>; <strong>Esth. 4:1</strong>), pouring dust or ashes on the head (<strong>Job 2:12</strong>; <strong>Lam. 2:10</strong>), going barefoot (<strong>2 Sam. 15:30</strong>), fasting (<strong>2 Sam. 1:12</strong>), cutting the hair or beard (in some cultures), wailing and weeping aloud, and hiring professional mourning women (<strong>Jer. 9:17–18</strong>; <strong>Amos 5:16</strong>).</p><p>The Mosaic law regulated mourning to prevent pagan practices such as cutting the body or shaving the head for the dead (<strong>Deut. 14:1</strong>; <strong>Lev. 19:28</strong>). The prophets compared Israel's coming judgment to the mourning of an only son (<strong>Amos 8:10</strong>; <strong>Zech. 12:10</strong>). The Beatitudes pronounce a blessing on those who mourn (<strong>Matt. 5:4</strong>), and Paul distinguishes godly grief that produces repentance from worldly grief that produces death (<strong>2 Cor. 7:10</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Genesis 37:29", "Matthew 5:4", "2 Corinthians 7:10", "Zechariah 12:10"]
},
"nard": {
  "id": "nard",
  "term": "Nard",
  "category": "concepts",
  "intro": "<p>Nard (spikenard; Hebrew <em>nerd</em>; Greek <em>nardos</em>) was a costly fragrant ointment derived from the root and spike of the nard plant (<em>Nardostachys jatamansi</em>), native to the Himalayan region of India. It was imported to the ancient Near East via the spice trade and was among the most expensive aromatics in the ancient world. Its distinctive name \"pure nard\" or \"genuine nard\" (<em>nardos pistikos</em>, <strong>John 12:3</strong>; <strong>Mark 14:3</strong>) distinguished authentic nard from cheaper adulterants.</p><p>Nard appears in the Song of Solomon (<strong>1:12</strong>; <strong>4:13–14</strong>) as a symbol of love and beauty. Its most prominent NT appearance is in the anointing of Jesus at Bethany, where Mary (sister of Martha) broke an alabaster flask of costly pure nard and poured it on Jesus's head (Mark) or feet (John). Judas Iscariot's objection — that the nard could have been sold for 300 denarii (a laborer's annual wage) — highlights the extraordinary value of the gift and Jesus's response that it was a preparation for his burial.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["John 12:3", "Mark 14:3", "Song of Solomon 1:12"]
},
"new-moon": {
  "id": "new-moon",
  "term": "New Moon",
  "category": "concepts",
  "intro": "<p>The first day of each lunar month (the new moon) was observed in Israel as a minor holy day. Special sacrifices were ordained: two young bulls, one ram, seven one-year-old lambs for a burnt offering, plus appropriate grain and drink offerings and a male goat for a sin offering (<strong>Num. 28:11–15</strong>). The trumpets were sounded (<strong>Num. 10:10</strong>; <strong>Ps. 81:3</strong>), and the temple was opened for public worship (<strong>Isa. 66:23</strong>; <strong>Ezek. 46:3</strong>). Commercial activity ceased, as Amos's merchants complained: \"When will the new moon be over, that we may sell grain?\" (<strong>Amos 8:5</strong>).</p><p>New moon celebrations could be occasions for prophets to be consulted (<strong>2 Kings 4:23</strong>) and for family gatherings (<strong>1 Sam. 20:5</strong>). Paul mentions new moons alongside Sabbaths and festivals as elements of the Mosaic calendar that are a \"shadow of things to come\" fulfilled in Christ (<strong>Col. 2:16–17</strong>). The eschatological vision of Isaiah 66:23 portrays all humanity worshipping before God at each new moon and Sabbath.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Numbers 28:11", "Amos 8:5", "Colossians 2:16", "Isaiah 66:23"]
},
"new-year": {
  "id": "new-year",
  "term": "New Year",
  "category": "concepts",
  "intro": "<p>The Jewish New Year (Rosh Hashanah, \"head of the year\") falls on the first of Tishri, the seventh month of the sacred calendar, and is identified in Scripture with the Feast of Trumpets (<strong>Lev. 23:23–25</strong>; <strong>Num. 29:1–6</strong>). The day was marked by complete rest, a sacred assembly, and the blowing of trumpets. The Mosaic legislation does not explicitly call it New Year; that designation developed through Jewish tradition, reflecting the civil calendar reckoning in which Tishri is the first month.</p><p>The tension between a sacred calendar beginning in Nisan (spring, at the Exodus) and a civil year beginning in Tishri (autumn) runs through the OT. By the rabbinic period, Tishri 1 was firmly established as New Year for years (including sabbatical and Jubilee year reckoning) and for the judgment of humanity. The ten days between Rosh Hashanah and Yom Kippur (the Day of Atonement) became the Days of Awe in Jewish tradition — a period of repentance and self-examination before the solemn fast.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Leviticus 23:24", "Numbers 29:1", "Nehemiah 8:2"]
},
"nicolaitans": {
  "id": "nicolaitans",
  "term": "Nicolaitans",
  "category": "people",
  "intro": "<p>The Nicolaitans were a sect condemned by the risen Christ in messages to two of the seven churches of Asia in Revelation — Ephesus, which hated their works (<strong>Rev. 2:6</strong>), and Pergamum, where some held their teaching (<strong>Rev. 2:15</strong>). Their deeds are linked to the \"teaching of Balaam\" — eating food sacrificed to idols and practicing sexual immorality — suggesting they advocated accommodation to pagan culture that the church's Jerusalem decree had explicitly prohibited (<strong>Acts 15:20, 29</strong>).</p><p>Early church fathers (Irenaeus, Clement of Alexandria) attributed the sect's founding to Nicolaus, one of the seven deacons of Acts 6:5, though this attribution is disputed and may reflect a later invention of etymology. The precise nature of their teaching is uncertain; some scholars see them as proto-Gnostics who separated spirit and flesh and thus considered physical conduct morally irrelevant. Their name may be a Greek equivalent of the Hebrew name Balaam (both meaning \"conqueror of the people\"), making the Balaam connection in Revelation a deliberate wordplay.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Revelation 2:6", "Revelation 2:15", "Acts 15:20"]
},
"no-amon": {
  "id": "no-amon",
  "term": "No-Amon",
  "category": "places",
  "intro": "<p>No-Amon (Hebrew <em>No Amon</em>, \"city of Amon\") was the ancient Egyptian capital of Upper Egypt, known to the Greeks as Thebes and located on both banks of the Nile approximately 400 miles south of Cairo. It was one of the greatest cities of antiquity, famed for its massive temples to the god Amon at Karnak and Luxor, and served as Egypt's capital during much of the New Kingdom (c. 1550–1070 B.C.).</p><p>The city is mentioned in the prophet Nahum's taunt against Nineveh: \"Are you better than No-Amon that sat by the Nile?\" (<strong>Nah. 3:8</strong>). Nahum recalls Thebes's destruction by the Assyrian king Ashurbanipal (c. 663 B.C.) as a precedent for Nineveh's coming fall. Jeremiah (<strong>Jer. 46:25</strong>) and Ezekiel (<strong>Ezek. 30:14–16</strong>) also prophesy against No (Thebes) as part of their oracles against Egypt. Elsewhere the city is referred to simply as \"No\" in the Authorized Version.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Nahum 3:8", "Jeremiah 46:25", "Ezekiel 30:14"]
},
"old-testament": {
  "id": "old-testament",
  "term": "Old Testament",
  "category": "concepts",
  "intro": "<p>The Old Testament is the first and larger portion of the Christian Bible, consisting of the Jewish scriptures received from Israel's covenant history. The Hebrew canon comprises 39 books (in the Protestant reckoning) organized into the Law (Torah), the Prophets (Nevi'im), and the Writings (Ketuvim) — together called the <em>Tanakh</em>. The Septuagint (LXX), the Greek translation made from the 3rd century B.C. onward, includes additional books accepted as canonical in Roman Catholic and Eastern Orthodox traditions but classified as Apocrypha or Deuterocanonical in Protestant usage.</p><p>The original text of the OT was written on skins in scroll form, in biblical Hebrew (with some Aramaic sections in Ezra, Daniel, and Jeremiah). The Masoretes standardized the consonantal text and added vowel pointing between A.D. 600–1000, producing the Masoretic Text (MT) that underlies most modern OT translations. The OT functions in Christian theology as the foundation and preparation for the NT: its covenants, prophecies, types, and institutions are fulfilled and reinterpreted in Christ (<strong>Matt. 5:17</strong>; <strong>Luke 24:44</strong>; <strong>2 Cor. 1:20</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Luke 24:44", "Matthew 5:17", "Romans 15:4", "2 Timothy 3:16"]
},
"olives-mount-of": {
  "id": "olives-mount-of",
  "term": "Olives, Mount of",
  "category": "places",
  "intro": "<p>The Mount of Olives is a limestone ridge running roughly north-south approximately 2.6 miles long and 2,684 feet in elevation, rising about 200 feet above the Temple Mount and lying directly to the east of Jerusalem across the Kidron Valley. Its name reflects the olive groves that covered its slopes in antiquity. In the OT it is called \"the mount facing Jerusalem\" (<strong>1 Kings 11:7</strong>; <strong>Ezek. 11:23</strong>) and \"Olivet\" (<strong>2 Sam. 15:30</strong>; <strong>Neh. 8:15</strong>). Zechariah prophesies the Lord's feet will stand on it at the final deliverance (<strong>Zech. 14:4</strong>).</p><p>In the NT the Mount of Olives is intimately connected with Jesus's final week: his triumphal entry descended from it (<strong>Matt. 21:1</strong>), he wept over Jerusalem from it (<strong>Luke 19:41</strong>), the Olivet Discourse was delivered on it (<strong>Matt. 24:3</strong>), he prayed in Gethsemane at its foot (<strong>Matt. 26:36</strong>), and his ascension took place from it (<strong>Acts 1:12</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Zechariah 14:4", "Matthew 24:3", "Acts 1:12", "Luke 19:41"]
},
"paran-elparan": {
  "id": "paran-elparan",
  "term": "Paran",
  "category": "places",
  "intro": "<p>Paran (also El-Paran) was a wilderness region in the northeastern Sinai Peninsula, bounded to the north by the Negeb and to the east by the Arabah. Hagar and Ishmael dwelt in the wilderness of Paran after their expulsion from Abraham's household (<strong>Gen. 21:21</strong>). The Israelites camped in the wilderness of Paran repeatedly during their wilderness wanderings (<strong>Num. 10:12</strong>; <strong>12:16</strong>), and it was from Kadesh in the wilderness of Paran that the twelve spies were sent into Canaan (<strong>Num. 13:3, 26</strong>).</p><p>El-Paran (\"the plain of Paran\" or \"the terebinth of Paran\") is mentioned in <strong>Genesis 14:6</strong> as the southernmost point of the campaign of the four kings against the five. The divine theophany in <strong>Deuteronomy 33:2</strong> and <strong>Habakkuk 3:3</strong> speaks of God coming from Paran — reflecting the tradition of his presence in this southern wilderness region associated with Sinai. Mount Paran in these passages likely refers to the Sinai massif.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Genesis 21:21", "Numbers 13:3", "Deuteronomy 33:2", "Habakkuk 3:3"]
},
"pestilence": {
  "id": "pestilence",
  "term": "Pestilence",
  "category": "concepts",
  "intro": "<p>Pestilence (Hebrew <em>deber</em>; Greek <em>loimos</em>) denotes epidemic disease sent as divine judgment throughout the Bible. It forms part of the standard biblical triad of divine punishments: sword, famine, and pestilence (<strong>Jer. 14:12</strong>; <strong>Ezek. 6:11</strong>; <strong>Rev. 6:8</strong>). The tenth plague on Egypt was a pestilence on livestock (<strong>Ex. 9:3–6</strong>), and God threatened covenant-breaking Israel with it in <strong>Leviticus 26:25</strong> and <strong>Deuteronomy 28:21</strong>.</p><p>David's census brought a three-day pestilence that killed 70,000 Israelites (<strong>2 Sam. 24:13–15</strong>), stopped only when God relented at the threshing floor of Araunah. The prophets use pestilence as a sign of covenant judgment alongside military defeat and famine. In the NT, Jesus predicts pestilences (plagues) among the birth pangs of the end age (<strong>Luke 21:11</strong>), and the four horsemen of Revelation include Death on a pale horse followed by Hades, given power over a quarter of the earth to kill by sword, famine, and pestilence (<strong>Rev. 6:8</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Jeremiah 14:12", "2 Samuel 24:15", "Revelation 6:8", "Luke 21:11"]
},
"pharaohs-daughter": {
  "id": "pharaohs-daughter",
  "term": "Pharaoh's Daughter",
  "category": "people",
  "intro": "<p>Three Egyptian princesses, daughters of Pharaohs, are mentioned in Scripture. (1.) The unnamed daughter of the Pharaoh who oppressed Israel, who discovered the infant Moses in a basket in the Nile, took pity on him, and raised him in the royal court (<strong>Ex. 2:5–10</strong>). She named him Moses (Hebrew <em>Mosheh</em>) from the Egyptian word for \"born of\" or from the Hebrew for \"drawn out.\" Hebrews 11:24 credits Moses with refusing to be called \"the son of Pharaoh's daughter\" when he chose to identify with God's people. (2.) Bithiah (\"daughter of Yahweh\"), wife of Mered of Judah (<strong>1 Chr. 4:18</strong>), likely from the same period. (3.) A wife of Solomon (<strong>1 Kings 3:1</strong>; <strong>7:8</strong>; <strong>9:16, 24</strong>), who received as dowry the city of Gezer, which her father had burned and given to Solomon. This politically advantageous marriage indicates the high status Solomon enjoyed in international diplomacy.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Exodus 2:5", "Hebrews 11:24", "1 Kings 3:1", "1 Chronicles 4:18"]
},
"philip-the-evangelist": {
  "id": "philip-the-evangelist",
  "term": "Philip the Evangelist",
  "category": "people",
  "intro": "<p>Philip the Evangelist was one of the seven men chosen by the Jerusalem church to oversee the distribution of food to widows, thus freeing the apostles for prayer and ministry (<strong>Acts 6:1–5</strong>). He is distinguished from Philip the apostle. When Stephen's martyrdom triggered persecution, Philip fled to Samaria and preached Christ there with great signs and miracles — the first major evangelism outside Jerusalem (<strong>Acts 8:4–8</strong>). His work anticipated the Pentecost of the Samaritans when Peter and John came to pray for the converts.</p><p>An angel then directed Philip to the desert road from Jerusalem to Gaza, where he encountered an Ethiopian eunuch, an official of Queen Candace, reading Isaiah 53. Philip explained the passage as fulfilled in Jesus, baptized the eunuch, and was then caught up by the Spirit to Azotus (<strong>Acts 8:26–40</strong>). He continued preaching through the coastal cities to Caesarea, where he settled. Paul later visited his house in Caesarea; Philip had four unmarried daughters who prophesied (<strong>Acts 21:8–9</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Acts 6:5", "Acts 8:5", "Acts 8:38", "Acts 21:8"]
},
"philosophy": {
  "id": "philosophy",
  "term": "Philosophy",
  "category": "concepts",
  "intro": "<p>Greek philosophy encountered biblical faith at multiple points in the intertestamental and NT periods. The Septuagint translation (3rd–2nd century B.C.) made Jewish scriptures accessible to the Greek world, and Jewish thinkers such as Philo of Alexandria attempted to synthesize Mosaic revelation with Platonic philosophy. The NT itself reflects awareness of Greek philosophical traditions: Paul's Athens sermon at the Areopagus (<strong>Acts 17:22–31</strong>) engaged Stoic and Epicurean philosophers directly, quoting Greek poets (Aratus, Cleanthes) while proclaiming the resurrection — the point at which his audience divided.</p><p>Paul warns the Colossians against \"philosophy and empty deceit, according to human tradition... and not according to Christ\" (<strong>Col. 2:8</strong>), while the prologue of John's Gospel employs the philosophical concept of the Logos (<strong>John 1:1</strong>) to present Christ as the divine Word who orders and sustains all things. The patristic church engaged Greek philosophy extensively, with Justin Martyr, Clement of Alexandria, and Origen using philosophical categories to articulate Christian theology, while others (Tertullian) remained suspicious of Athens's relationship to Jerusalem.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Acts 17:28", "Colossians 2:8", "John 1:1"]
},
"phoebe": {
  "id": "phoebe",
  "term": "Phoebe",
  "category": "people",
  "intro": "<p>Phoebe was a woman of the church at Cenchreae (the eastern port of Corinth) whom Paul commends to the Roman church at the close of his epistle to Rome (<strong>Rom. 16:1–2</strong>). Paul applies two significant terms to her: <em>diakonos</em> (\"servant\" or \"deacon/deaconess\") of the church at Cenchreae, and <em>prostatis</em> (\"patron\" or \"benefactor\") of many, including Paul himself. She is thought to have been the bearer of the letter to Rome, which would have required her to read and explain it to the Roman churches.</p><p>Her dual designation — as a church officer and as a patron of substantial means — makes her one of the most important named women in the NT. The question of whether <em>diakonos</em> here denotes a formal office (deaconess) or informal service is debated. In either case, the commendation Paul issues is remarkable: he asks the Roman church to assist her in whatever she needs, since she has been a helper to many.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Romans 16:1", "Romans 16:2"]
},
"phylactery": {
  "id": "phylactery",
  "term": "Phylactery",
  "category": "concepts",
  "intro": "<p>Phylacteries (Greek <em>phylakteria</em>, \"safeguards\"; Hebrew <em>tefillin</em>) are small leather boxes containing four passages of Scripture — <strong>Exodus 13:1–10</strong>, <strong>13:11–16</strong>, <strong>Deuteronomy 6:4–9</strong>, and <strong>11:13–21</strong> — worn by Jewish men during weekday morning prayers. They are bound by leather straps: one on the forehead between the eyes, and one on the left arm near the heart, in literal obedience to the command of <strong>Deuteronomy 6:8</strong>: \"You shall bind them as a sign on your hand, and they shall be as frontlets between your eyes.\"</p><p>The practice is ancient, attested by finds at Qumran (the Dead Sea Scrolls community). Jesus criticizes those who make their phylacteries broad for public display (<strong>Matt. 23:5</strong>), condemning ostentation rather than the practice itself. The theological purpose is to keep God's law continually before the mind and near the heart — a physical embodiment of the Shema's command to love God with the whole person.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Deuteronomy 6:8", "Matthew 23:5", "Exodus 13:9"]
},
"piece-of-silver": {
  "id": "piece-of-silver",
  "term": "Piece of Silver",
  "category": "concepts",
  "intro": "<p>\"Pieces of silver\" in the OT refers to weighed silver used as currency before the minting of coins. The Hebrew <em>keseph</em> simply means silver; its value was determined by weight rather than denomination. Joseph was sold for twenty pieces of silver (<strong>Gen. 37:28</strong>), and the standard price for a slave was thirty (<strong>Ex. 21:32</strong>; <strong>Zech. 11:12</strong>). In <strong>Zechariah 11:12–13</strong> the thirty pieces of silver paid to the shepherd-prophet were thrown into the house of the LORD — interpreted in Matthew 27:9–10 as fulfilled in Judas's betrayal price.</p><p>After the Persian period, actual silver coins (the Greek <em>drachma</em> and later the <em>stater</em>) circulated in Israel. In the NT, the <em>drachma</em> (a silver coin of roughly a day's wage) appears in the parable of the Lost Coin (<strong>Luke 15:8</strong>), and the <em>stater</em> (worth four drachmas) is the coin found in the fish's mouth for the temple tax (<strong>Matt. 17:27</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Zechariah 11:12", "Matthew 26:15", "Genesis 37:28", "Luke 15:8"]
},
"poetry-hebrew": {
  "id": "poetry-hebrew",
  "term": "Poetry, Hebrew",
  "category": "concepts",
  "intro": "<p>Hebrew poetry differs fundamentally from Greek and English poetry in that its primary structural feature is <em>parallelism</em> — the balancing of thought between lines — rather than rhyme or meter. Robert Lowth (1753) identified three types: <em>synonymous parallelism</em> (the second line restates the first, <strong>Ps. 24:1</strong>), <em>antithetic parallelism</em> (the second line contrasts the first, <strong>Prov. 10:1</strong>), and <em>synthetic</em> or <em>progressive parallelism</em> (the second line develops or completes the first). Later analysis has refined these categories further.</p><p>Hebrew poetry includes three genres: <em>lyrical</em> (the Psalms and much of the Song of Solomon), <em>gnomic or wisdom</em> (Proverbs, Ecclesiastes, Job), and <em>prophetic or elegiac</em> (portions of the prophetic books and the book of Lamentations, which is an acrostic in chapter 1). Much of the prophetic literature was originally delivered in poetic form. The acrostic structure — where successive verses begin with successive letters of the Hebrew alphabet — appears in Psalms 119, Lamentations 1–4, and elsewhere as a mnemonic and artistic device.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Psalms 24:1", "Proverbs 10:1", "Lamentations 1:1"]
},
"pollux": {
  "id": "pollux",
  "term": "Castor and Pollux",
  "category": "concepts",
  "intro": "<p>Castor and Pollux (the Dioscuri, \"sons of Zeus\") were twin demigods of Greek and Roman mythology, patrons of sailors and mariners, believed to appear as the electrical phenomenon of St. Elmo's fire in ship's rigging during storms. Sailors regarded their appearance as a favorable omen. The ship that carried Paul from Malta to Puteoli after his shipwreck bore their figure as its figurehead: \"We set sail in a ship that had wintered in the island, with the twin gods as a figurehead\" (<strong>Acts 28:11</strong>).</p><p>The appearance of this pagan religious symbol in the narrative of Acts is incidental and unremarked — Luke records the vessel's identification mark without comment or critique. Such figureheads were standard on Alexandrian grain ships of the period. The Dioscuri were extremely popular throughout the Roman Empire, with temples in Rome, Corinth, Athens, and many other cities.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Acts 28:11"]
},
"polygamy": {
  "id": "polygamy",
  "term": "Polygamy",
  "category": "concepts",
  "intro": "<p>Polygamy (having multiple wives simultaneously) was practiced by many figures in the Old Testament without explicit divine condemnation in individual cases, yet the cumulative narrative often shows its destructive consequences. Lamech is the first recorded polygamist (<strong>Gen. 4:19</strong>). Abraham took Hagar as a secondary wife at Sarah's urging. Jacob married both Leah and Rachel. Solomon's 700 wives and 300 concubines — many foreign — led to his apostasy (<strong>1 Kings 11:3–4</strong>).</p><p>The Mosaic law regulated rather than abolished polygamy, providing protections for the first wife and her children (<strong>Deut. 21:15–17</strong>; <strong>Ex. 21:10</strong>). The law of the king explicitly warned against multiplying wives (<strong>Deut. 17:17</strong>). The NT assumes monogamy as the Christian norm; Jesus appeals to the creation order of \"one flesh\" from Genesis 2:24 (<strong>Matt. 19:5–6</strong>), and the qualifications for church elders include being \"the husband of one wife\" (<strong>1 Tim. 3:2</strong>; <strong>Tit. 1:6</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Deuteronomy 17:17", "Matthew 19:5", "1 Timothy 3:2", "Genesis 2:24"]
},
"principality": {
  "id": "principality",
  "term": "Principality",
  "category": "concepts",
  "intro": "<p>\"Principalities\" (Greek <em>archai</em>) appears in the NT as one of several terms for categories of spiritual beings, both good and fallen. Paul uses it alongside \"powers\" (<em>exousiai</em>), \"thrones\" (<em>thronoi</em>), and \"dominions\" (<em>kyriotetes</em>) to describe the hierarchical ranks of the angelic and demonic realm. In <strong>Romans 8:38</strong> he declares that neither principalities nor powers can separate believers from the love of God. In <strong>Ephesians 6:12</strong> the Christian's battle is described as against \"the rulers\" (principalities), \"the authorities,\" \"the cosmic powers over this present darkness,\" and \"the spiritual forces of evil in the heavenly places.\"</p><p>The incarnation and resurrection are presented as a cosmic victory: Christ is \"far above all rule and authority and power and dominion\" (<strong>Eph. 1:21</strong>), and the cross disarmed the principalities and powers, making a public spectacle of them (<strong>Col. 2:15</strong>). The church itself is the demonstration to these powers of the manifold wisdom of God (<strong>Eph. 3:10</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Ephesians 6:12", "Romans 8:38", "Colossians 2:15", "Ephesians 1:21"]
},
"proconsul": {
  "id": "proconsul",
  "term": "Proconsul",
  "category": "concepts",
  "intro": "<p>A proconsul (Latin <em>pro consule</em>, \"in place of the consul\") was the governor of a senatorial province — one assigned by lot to the Roman Senate rather than directly by the emperor. Senatorial provinces were generally the more pacified territories, while the emperor retained control of frontier and militarily sensitive provinces through his own legates (propraetors). The proconsul held civilian and military authority within his province and served a term of one year.</p><p>Two proconsuls appear by name in Acts. Sergius Paulus was proconsul of Cyprus when Paul and Barnabas visited, and he believed after the blinding of Elymas the sorcerer (<strong>Acts 13:7–12</strong>). Gallio was proconsul of Achaia (Greece) when the Jews brought Paul before his tribunal in Corinth (<strong>Acts 18:12–17</strong>); he refused to adjudicate what he considered an intra-Jewish religious dispute and dismissed the case. An inscription discovered at Delphi confirms Gallio's proconsulship around A.D. 51–52, providing one of the most important chronological anchors for Pauline chronology.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Acts 13:7", "Acts 18:12"]
},
"procurator": {
  "id": "procurator",
  "term": "Procurator",
  "category": "concepts",
  "intro": "<p>A procurator (Greek <em>hegemon</em>, rendered \"governor\" in the NT) was a Roman official appointed by the emperor to administer an imperial province or sub-province. Judea became a procuratorial province after the removal of Archelaus in A.D. 6 and remained so (except for the brief reign of Herod Agrippa I, A.D. 41–44) until the Jewish War. The procurator held judicial, military, and financial authority, answerable directly to the emperor.</p><p>Four procurators appear in the NT narrative: Pontius Pilate (A.D. 26–36), who condemned Jesus (<strong>Matt. 27:2</strong>); Felix (A.D. 52–59), before whom Paul was held two years in Caesarea (<strong>Acts 24:27</strong>); Festus (A.D. 59–62), who succeeded Felix and before whom Paul appealed to Caesar (<strong>Acts 25:11–12</strong>); and Albinus and Florus (A.D. 62–66) in Josephus but not in Acts. The procurator's headquarters were at Caesarea Maritima, with a Jerusalem praetorium for use during festivals.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Matthew 27:2", "Acts 24:27", "Acts 25:11", "Luke 3:1"]
},
"psalms-book-of": {
  "id": "psalms-book-of",
  "term": "Psalms, Book of",
  "category": "concepts",
  "intro": "<p>The Book of Psalms (Hebrew <em>Tehillim</em>, \"Praises\"; Greek <em>Psalmoi</em>, \"songs to a stringed instrument\") is the hymnbook and prayer book of both the Jewish temple and the Christian church. It comprises 150 poems organized into five books (Pss. 1–41; 42–72; 73–89; 90–106; 107–150), each ending with a doxology — a structure mirroring the five books of Moses. The collection spans at least a millennium of Israelite worship, from the Mosaic period (Psalm 90, attributed to Moses) through the post-exilic restoration.</p><p>Seventy-three psalms are attributed to David in their superscriptions. Asaph, the sons of Korah, Solomon, Ethan, Heman, and Moses are also named as authors. The psalms cover the full range of human experience in relationship to God: praise, lament, thanksgiving, penitence, trust, royal celebration, and wisdom. Christological use of the Psalms pervades the NT: Psalms 2, 16, 22, 69, 110, and 118 are among the most frequently cited OT texts applied to Jesus's identity, passion, and resurrection (<strong>Matt. 22:44</strong>; <strong>Acts 2:25–28</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Acts 2:25", "Matthew 22:44", "Hebrews 1:5", "Psalms 22:1"]
},
"punishments": {
  "id": "punishments",
  "term": "Punishments",
  "category": "concepts",
  "intro": "<p>Biblical punishment law developed from the ancient principle of retaliation (lex talionis) — \"an eye for an eye, tooth for tooth\" (<strong>Ex. 21:24</strong>; <strong>Lev. 24:20</strong>) — which originally functioned to cap retribution rather than mandate it literally. The Mosaic law prescribed capital punishment for a wide range of offenses: murder (<strong>Gen. 9:6</strong>; <strong>Num. 35:16–21</strong>), idolatry, blasphemy, adultery, certain sexual offenses, kidnapping, striking or cursing a parent, and Sabbath violation.</p><p>Methods of execution in the OT included stoning (the standard method for capital crimes in Israel, executed by the community), burning, the sword, and occasionally hanging (displaying the corpse after death). The NT period adds crucifixion (a Roman form), beheading, and imprisonment. Flogging (up to 40 stripes, reduced to 39 by practice, <strong>2 Cor. 11:24</strong>) was administered for offenses not warranting death. Imprisonment appears mainly in the NT period, as a Roman rather than distinctly Israelite institution. The NT affirms civil authorities as God's servants executing justice (<strong>Rom. 13:4</strong>) while looking forward to a final judgment that perfectly vindicates all injustice.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Exodus 21:24", "Romans 13:4", "Deuteronomy 25:3", "2 Corinthians 11:24"]
},
"race": {
  "id": "race",
  "term": "Race",
  "category": "concepts",
  "intro": "<p>The athletic foot-race (<em>stadion</em>) and broader Greek games (the Olympic, Isthmian, Nemean, and Pythian festivals) provided Paul and the author of Hebrews with powerful metaphors for the Christian life. Paul wrote extensively while at Corinth, near the site of the biennial Isthmian Games, and his audience would have recognized athletic imagery immediately. He compares himself and other ministers to racers running for a perishable wreath, then contrasts this with the imperishable crown of Christian victory (<strong>1 Cor. 9:24–27</strong>).</p><p>In <strong>Hebrews 12:1–2</strong>, surrounded by the \"cloud of witnesses\" of faith heroes from chapter 11, believers are urged to \"run with endurance the race that is set before us, looking to Jesus, the founder and perfecter of our faith.\" Paul's final testimony uses the same image: \"I have finished the race, I have kept the faith\" (<strong>2 Tim. 4:7</strong>). The metaphor emphasizes discipline, focus, perseverance, and the necessity of divesting oneself of everything that hinders the run.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["1 Corinthians 9:24", "Hebrews 12:1", "2 Timothy 4:7", "Philippians 3:14"]
},
"raphael": {
  "id": "raphael",
  "term": "Raphael",
  "category": "people",
  "intro": "<p>Raphael (Hebrew: \"God has healed\") is named in Jewish tradition as one of the seven archangels before the throne of God. He appears as a named angel only in the deuterocanonical Book of Tobit, where he accompanies Tobias on his journey to Media disguised as a kinsman, helps him secure his bride Sarah, drives away the demon Asmodeus, and restores Tobit's sight — then reveals his identity: \"I am Raphael, one of the seven angels who stand ready and enter before the glory of the Lord\" (<strong>Tob. 12:15</strong>). He is also identified in some traditions with the angel who troubled the waters at the pool of Bethesda (<strong>John 5:4</strong>, in some manuscripts).</p><p>Raphael is not named in the canonical OT or NT. The tradition of seven archangels is reflected in <strong>Revelation 8:2</strong> (\"the seven angels who stand before God\") and in Jewish intertestamental literature (1 Enoch, 2 Esdras). Only Michael and Gabriel are named in the canonical scriptures.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Revelation 8:2", "Daniel 10:13", "Luke 1:19"]
},
"rephan": {
  "id": "rephan",
  "term": "Rephan",
  "category": "concepts",
  "intro": "<p>Rephan (also Remphan or Chiun) was the name of an astral deity worshipped by Israel in the wilderness, referenced in Stephen's speech: \"Did you bring to me slain beasts and sacrifices during the forty years in the wilderness, O house of Israel? You took up the tent of Moloch and the star of your god Rephan, the images that you made to worship\" (<strong>Acts 7:42–43</strong>), quoting <strong>Amos 5:25–27</strong>. The Septuagint translated the Hebrew <em>Kiyyun</em> (KJV \"Chiun\") of Amos as Rephan.</p><p>The identification of Rephan with a specific deity is uncertain. It is likely a reference to Saturn, venerated in ancient Near Eastern astral religion, or to a specific Mesopotamian or Egyptian star-deity. The Revised Version uses Rephan. The passage indicts Israel for secret idolatry practiced even during the wilderness period, contradicting the idealized view of that era. The divine response was the exile of Israel beyond Babylon.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Acts 7:43", "Amos 5:26"]
},
"samaria-country-of": {
  "id": "samaria-country-of",
  "term": "Samaria",
  "category": "places",
  "intro": "<p>Samaria (as a country or region, distinct from the city of Samaria) originally designated the territory of the northern ten tribes under Jeroboam, extending from the Jordan to the Mediterranean and from Jezreel south to Bethel. After the fall of the northern kingdom to Assyria in 722 B.C. (<strong>2 Kings 17</strong>), the region was repopulated with peoples from Babylon, Cuthah, Avva, Hamath, and Sepharvaim, who mixed with the remaining Israelite population to form the Samaritan people — who worshipped a syncretistic form of Yahwism centered on Mount Gerizim rather than Jerusalem.</p><p>In the NT, Samaria lies between Judea and Galilee. Jesus passed through it, including the encounter at Jacob's well with the Samaritan woman (<strong>John 4</strong>), and used Samaritans in two of his most memorable illustrations: the Good Samaritan (<strong>Luke 10:33</strong>) and the grateful leper (<strong>Luke 17:16</strong>). After Pentecost, Philip preached in Samaria with great response (<strong>Acts 8:5–8</strong>), fulfilling Jesus's commission to witness \"in Jerusalem and in all Judea and Samaria\" (<strong>Acts 1:8</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Acts 1:8", "John 4:9", "2 Kings 17:24", "Acts 8:5"]
},
"samothrace": {
  "id": "samothrace",
  "term": "Samothrace",
  "category": "places",
  "intro": "<p>Samothrace (Revised Version form; KJV \"Samothracia\") was a mountainous island in the northeastern Aegean Sea, lying roughly 38 miles south of the Thracian coast and about midway between Troas and Neapolis. Its highest peak (Mount Fengari) reaches 5,577 feet, making it visible from great distances at sea. The island was famous in antiquity as the site of the mystery religion of the Cabiri, whose initiates included many notable Romans including Philip of Macedon, father of Alexander the Great.</p><p>Paul's ship put in at Samothrace overnight during his second missionary journey, sailing from Troas toward Macedonia after his Macedonian vision (<strong>Acts 16:11</strong>): \"Setting sail from Troas, we made a direct voyage to Samothrace, and the following day to Neapolis.\" The brief mention indicates a favorable wind enabling a fast overnight passage; the normal journey from Troas to Neapolis took 5 days when winds were contrary (Acts 20:6).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Acts 16:11"]
},
"seleucus": {
  "id": "seleucus",
  "term": "Seleucus",
  "category": "people",
  "intro": "<p>Seleucus was the name of five kings of the Seleucid dynasty that ruled Syria and much of the former Persian Empire after Alexander the Great's death (323 B.C.). <strong>Seleucus I Nicator</strong> (312–281 B.C.) founded the dynasty, establishing his capital first at Antioch on the Orontes, the city that would later become the missionary base of Paul's journeys. <strong>Seleucus IV Philopator</strong> (187–175 B.C.) is referenced in the Apocrypha (2 Macc. 3) as having dispatched Heliodorus to plunder the Jerusalem temple treasury — the attempt divinely thwarted.</p><p>The Seleucid dynasty is the \"king of the north\" in Daniel 11's prophecy, and Antiochus IV Epiphanes (175–164 B.C.), whose desecration of the Jerusalem temple prompted the Maccabean revolt, was the brother and successor of Seleucus IV. The Seleucids were eventually pushed out of Judea by the Hasmoneans and later absorbed by Rome when Pompey organized Syria as a Roman province in 64 B.C.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Daniel 11:21", "Daniel 8:23"]
},
"simeon-niger": {
  "id": "simeon-niger",
  "term": "Simeon called Niger",
  "category": "people",
  "intro": "<p>Simeon called Niger (Latin for \"black\") was one of the five prophets and teachers in the church at Antioch named in <strong>Acts 13:1</strong>: \"Now there were in the church at Antioch prophets and teachers: Barnabas, Simeon who was called Niger, Lucius of Cyrene, Manaen a lifelong friend of Herod the tetrarch, and Saul.\" This diverse leadership group included Jewish and Gentile, African and Asian believers. While the Spirit was directing them in worship, he called Barnabas and Saul to be set apart for missionary work.</p><p>The epithet \"Niger\" suggests African origin or dark complexion. Some scholars identify Simeon Niger with Simon of Cyrene who carried Jesus's cross (<strong>Luke 23:26</strong>), noting that Lucius of Cyrene is listed alongside him and that Simon of Cyrene's sons Alexander and Rufus apparently became known figures in the early church (<strong>Mark 15:21</strong>; <strong>Rom. 16:13</strong>). The identification is suggestive but cannot be confirmed.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Acts 13:1", "Luke 23:26", "Mark 15:21"]
},
"solomon-wisdom-of": {
  "id": "solomon-wisdom-of",
  "term": "Wisdom of Solomon",
  "category": "concepts",
  "intro": "<p>The Wisdom of Solomon (also called simply \"Wisdom\") is a deuterocanonical book composed in Greek, probably in Alexandria between 100 B.C. and A.D. 50, though it is attributed to Solomon in the tradition of wisdom literature. It is accepted as canonical by Roman Catholic and Eastern Orthodox churches and classified as Apocrypha in Protestant Bibles. Its three main sections address: the contrast between the destiny of the righteous and the wicked (chapters 1–5); a poem in praise of Wisdom personified as a divine feminine figure (6–9); and a historical survey of Israel's sacred history, particularly the Exodus, interpreted through wisdom's lens (10–19).</p><p>The Wisdom of Solomon influenced NT thought in several ways: its description of Wisdom as the image of God's goodness and the emanation of his glory (<strong>Wis. 7:25–26</strong>) contributed to the background of Christological texts like <strong>Colossians 1:15</strong> and <strong>Hebrews 1:3</strong>. Paul's argument in Romans 1–2 parallels the Wisdom of Solomon's critique of Gentile idolatry in chapters 13–14.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Colossians 1:15", "Hebrews 1:3"]
},
"sower-sowing": {
  "id": "sower-sowing",
  "term": "Sower and Sowing",
  "category": "concepts",
  "intro": "<p>Sowing grain by hand-broadcasting was one of the most fundamental agricultural operations in ancient Israel. The sower carried seed in a fold of his garment or a bag and scattered it over plowed ground. In Palestine, seed was sown in the autumn (October–November) before the early rains, and the grain was harvested in spring (April–May for barley; May–June for wheat). The sower walked through the field broadcasting broadly, which explains the range of soils in Jesus's parable — some seed inevitably fell on the path, on rocky ground, or among thorns.</p><p>The Parable of the Sower (<strong>Matt. 13:3–23</strong>; <strong>Mark 4:3–20</strong>; <strong>Luke 8:5–15</strong>) is one of the foundational parables of the kingdom, which Jesus himself explained: the seed is the word of God, and the various soils represent different hearts. Paul uses sowing and reaping as a metaphor for generosity (<strong>2 Cor. 9:6</strong>; <strong>Gal. 6:7–8</strong>) and for the relationship between the mortal body and the resurrection body (<strong>1 Cor. 15:36–44</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Matthew 13:3", "Galatians 6:7", "1 Corinthians 15:37", "2 Corinthians 9:6"]
},
"spice-spices": {
  "id": "spice-spices",
  "term": "Spices",
  "category": "concepts",
  "intro": "<p>Spices (<em>besamim</em>, <em>nataph</em>, and related terms) were highly valued in the ancient world for perfumery, medicine, embalming, and ritual use. The sacred incense of the tabernacle required four specific spices: stacte, onycha, galbanum, and frankincense (<strong>Ex. 30:34–35</strong>), and the anointing oil blended myrrh, cinnamon, aromatic cane, and cassia (<strong>Ex. 30:23–25</strong>). The Queen of Sheba brought camels laden with spices when she visited Solomon (<strong>1 Kings 10:2</strong>; <strong>2 Chr. 9:1</strong>).</p><p>Spices figure prominently in the Song of Solomon (myrrh, spikenard, cinnamon, calamus, frankincense), reflecting a culture in which fragrance expressed intimacy and honor. At Jesus's burial, Nicodemus brought myrrh and aloes (<strong>John 19:39</strong>), and the women prepared spices to anoint his body (<strong>Luke 23:56</strong>; <strong>24:1</strong>). The wise men's gift of frankincense and myrrh at the nativity is often interpreted symbolically: frankincense for divinity, myrrh for death and burial (<strong>Matt. 2:11</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Exodus 30:23", "John 19:39", "Matthew 2:11", "1 Kings 10:2"]
},
"susa": {
  "id": "susa",
  "term": "Susa",
  "category": "places",
  "intro": "<p>Susa (also Shushan; Hebrew <em>Shushan</em>) was the ancient capital of Elam and later a principal royal residence of the Achaemenid Persian Empire, located on the Shaur River in modern southwestern Iran. It served as one of the three capitals of the empire (alongside Persepolis and Ecbatana). The Persian kings Cyrus, Darius, Xerxes, and Artaxerxes all held court there during winter months.</p><p>Susa is the primary setting for the books of Esther (<strong>Esth. 1:2</strong>) and Nehemiah (<strong>Neh. 1:1</strong>), and the place where Daniel received the vision of <strong>Daniel 8:2</strong>. Excavations at the site (ancient Achaemenid royal precinct, now Shush, Iran) have confirmed the biblical palace description and yielded the famous stele of Hammurabi's law code, now in the Louvre. The decree of Artaxerxes authorizing Nehemiah's mission to rebuild Jerusalem's walls was issued from Susa.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Nehemiah 1:1", "Esther 1:2", "Daniel 8:2"]
},
"swearing": {
  "id": "swearing",
  "term": "Swearing",
  "category": "concepts",
  "intro": "<p>Biblical swearing (oath-taking) involved calling upon God as witness to guarantee the truth of a statement or the binding force of a promise. The OT permitted and even regulated oaths: \"You shall fear the LORD your God, you shall serve him and hold fast to him, and by his name you shall swear\" (<strong>Deut. 10:20</strong>). Oaths were sworn by God's name (<strong>Gen. 21:23</strong>), by God's life (<strong>1 Sam. 14:39</strong>), and by the temple or the king. False swearing (perjury) was strictly condemned as profaning God's name (<strong>Lev. 19:12</strong>; <strong>Zech. 5:3</strong>).</p><p>Jesus's teaching in the Sermon on the Mount raised the standard: \"Do not swear at all... Let what you say be simply 'Yes' or 'No'; anything more than this comes from evil\" (<strong>Matt. 5:34–37</strong>). James echoes this directly (<strong>James 5:12</strong>). Many interpreters understand Jesus to prohibit casual or trivial oath-taking rather than all formal oaths — Paul himself uses oath-like expressions in his letters (<strong>2 Cor. 1:23</strong>; <strong>Gal. 1:20</strong>), and God swore by himself to Abraham (<strong>Heb. 6:13–17</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Matthew 5:34", "Deuteronomy 10:20", "Hebrews 6:13", "James 5:12"]
},
"synagogue-the-great": {
  "id": "synagogue-the-great",
  "term": "Great Synagogue",
  "category": "concepts",
  "intro": "<p>The Great Synagogue (Hebrew <em>Knesset ha-Gedolah</em>) was, according to Jewish tradition, a council of 120 men convened after the return from Babylon to reorganize and preserve Israel's religious life. Tradition names Ezra as its president and credits the body with collecting and editing the scriptures to complete the OT canon, composing key prayers of the synagogue liturgy (including portions of the Amidah), and transmitting the Oral Torah from the prophets to the scribes. The maxim attributed to them in Avot 1:1: \"Be deliberate in judgment, raise up many disciples, and make a fence around the Torah.\"</p><p>Critical scholarship treats the Great Synagogue as a legendary construct rather than a historically verifiable institution, noting that the tradition is not attested before the Mishnah (c. A.D. 200) and that its 120 members likely reflect the 120 signatories of Nehemiah's covenant (<strong>Neh. 10</strong>). Whatever its historical form, the Great Synagogue tradition reflects the real importance of the scribal class in preserving and transmitting Scripture after the exile.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Nehemiah 10:1", "Ezra 7:6"]
},
"syrophoenician": {
  "id": "syrophoenician",
  "term": "Syrophoenician",
  "category": "people",
  "intro": "<p>Syrophoenician (or Syro-Phoenician) is the ethnic descriptor used in <strong>Mark 7:26</strong> for the Gentile woman who came to Jesus near Tyre and begged him to cast a demon out of her daughter. Matthew's parallel (<strong>Matt. 15:22</strong>) calls her a \"Canaanite woman\" — the OT designation for the indigenous inhabitants of the same coastal region. The Syrophoenician label distinguishes Phoenicians living under Syrian Roman administration from the Libyan-Phoenicians (Carthaginians) of North Africa.</p><p>The encounter is one of the most theologically significant Gentile interactions in the Gospels. Jesus initially seems to refuse, saying his mission is to \"the lost sheep of Israel,\" then responds to the woman's persistent wit (\"even the dogs eat the crumbs\") with commendation for her faith and healing of her daughter. The episode foreshadows the full inclusion of the Gentiles in the people of God that Pentecost inaugurates.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Mark 7:26", "Matthew 15:22", "Mark 7:29"]
},
"talmud": {
  "id": "talmud",
  "term": "Talmud",
  "category": "concepts",
  "intro": "<p>The Talmud (Hebrew: <em>doctrine; study</em>) is the vast compilation of Jewish oral law and rabbinic discussion that stands alongside the written Torah as the foundational document of rabbinic Judaism. It exists in two versions: the Jerusalem (Palestinian) Talmud, compiled c. A.D. 400, and the more authoritative Babylonian Talmud, completed c. A.D. 500. Both consist of the Mishnah (codification of the Oral Torah, compiled by Rabbi Judah ha-Nasi c. A.D. 200) surrounded by the Gemara (rabbinic discussion and commentary on the Mishnah).</p><p>The Talmud's origins lie in the Pharisaic belief that alongside the written law God had given Moses an oral law to complete and explain it. Jesus engaged this tradition directly, sometimes affirming it and sometimes challenging it: \"You have a fine way of rejecting the commandment of God in order to establish your tradition\" (<strong>Mark 7:9</strong>; <strong>Matt. 15:3–9</strong>). Paul, trained as a Pharisee \"at the feet of Gamaliel\" (<strong>Acts 22:3</strong>), was familiar with this tradition before his conversion.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Mark 7:9", "Matthew 15:3", "Acts 22:3"]
},
"targum": {
  "id": "targum",
  "term": "Targum",
  "category": "concepts",
  "intro": "<p>A Targum (Aramaic: <em>translation; interpretation</em>) is an Aramaic paraphrase or translation of the Hebrew scriptures, produced because Aramaic became the common language of Palestinian Jews after the Babylonian exile. As Hebrew became increasingly a liturgical language known mainly to scholars, synagogue readers would recite the Hebrew text followed by an oral Aramaic rendering. These oral renderings were eventually written down, producing the Targums.</p><p>The most important Targums are the Targum Onkelos (on the Torah, probably finalized in Babylon, c. 3rd century A.D.) and the Targum Jonathan ben Uzziel (on the Prophets). Palestinian Targums (Targum Neofiti, Targum Pseudo-Jonathan) preserve older, more expansive paraphrasing traditions. The Targums are theologically significant because they often interpret the Hebrew text through a messianic or rabbinic lens and occasionally substitute circumlocutions for direct divine names. They provide evidence for how ancient Jewish communities understood their scripture and are important resources for NT background studies.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Nehemiah 8:8"]
},
"tigris": {
  "id": "tigris",
  "term": "Tigris",
  "category": "places",
  "intro": "<p>The Tigris (Hebrew <em>Hiddekel</em>; Greek <em>Tigris</em>) is one of the two great rivers of Mesopotamia, rising in the mountains of eastern Turkey and flowing approximately 1,150 miles southeast to join the Euphrates before emptying into the Persian Gulf. In the Table of Nations it is listed as one of the four rivers flowing from Eden: \"the third river is the Tigris, which flows east of Assyria\" (<strong>Gen. 2:14</strong>).</p><p>The Tigris formed the eastern boundary of the Assyrian heartland, and major Assyrian cities — Nineveh, Ashur, Calah — lay along its banks. Daniel received his vision of the man clothed in linen while standing on the bank of the great river, which some identify as the Tigris (<strong>Dan. 10:4</strong>). The Greek and Syriac traditions uniformly identify the Hebrew <em>Hiddekel</em> with the Tigris. The river was a commercial artery and military corridor for successive empires from Mesopotamia through the Persian period and remains a major river of modern Iraq.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Genesis 2:14", "Daniel 10:4"]
},
"titus-justus": {
  "id": "titus-justus",
  "term": "Titus Justus",
  "category": "people",
  "intro": "<p>Titus Justus (Revised Version; KJV \"Justus\") was a God-fearer — a Gentile worshipper of the Jewish God who had not converted to Judaism — whose house adjoined the Corinthian synagogue. When the synagogue expelled Paul after his proclamation that Jesus was the Christ, Paul relocated his teaching ministry to the house of Titus Justus (<strong>Acts 18:7</strong>), where he remained for eighteen months building the Corinthian church. The name suggests Roman citizenship (<em>Titus</em> being a Roman praenomen, <em>Justus</em> a cognomen).</p><p>The strategic location of his house — directly adjacent to the synagogue — meant that synagogue attenders could easily observe and access the emerging Christian community. Some scholars have suggested, though without certainty, that he may be identified with the Gaius Paul mentions in <strong>Romans 16:23</strong> (\"Gaius, who is host to me and to the whole church\") or the Titius Justus of some manuscripts, but these identifications remain speculative.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Acts 18:7"]
},
"tobit-book-of": {
  "id": "tobit-book-of",
  "term": "Tobit, Book of",
  "category": "concepts",
  "intro": "<p>The Book of Tobit is a deuterocanonical work accepted as Scripture by Roman Catholic and Eastern Orthodox churches and classified as Apocrypha in Protestant Bibles. It exists in Greek, Latin, Syriac, and Hebrew/Aramaic fragments (discovered at Qumran, confirming its pre-Christian origin). The story is set in Assyria among the Jewish exiles, following Tobit — a righteous Jew blinded by bird droppings — and his son Tobias, whose journey to Media is guided by the angel Raphael in disguise. Tobias marries his kinswoman Sarah, whose seven previous husbands had been killed by the demon Asmodeus; Raphael drives away the demon, and Tobit's sight is restored.</p><p>The book emphasizes almsgiving, prayer, proper burial of the dead, filial piety, and endogamous marriage (marrying within one's people). Its theology of angels, demons, and afterlife reflects the intertestamental period. The literary genre combines elements of wisdom instruction, romance, and apocalyptic, and the book influenced later Jewish and early Christian piety.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": []
},
"tomb": {
  "id": "tomb",
  "term": "Tomb",
  "category": "concepts",
  "intro": "<p>Ancient Israelite burial practice centered on placing the dead in family tombs — natural caves or rock-cut chambers — where successive generations of a family were laid. The phrase \"gathered to his people\" (e.g., <strong>Gen. 25:8</strong>) reflects the practice of collecting bones into the family tomb over time. The cave of Machpelah purchased by Abraham from Ephron the Hittite (<strong>Gen. 23</strong>) became the patriarchal family tomb for Abraham, Sarah, Isaac, Rebekah, Jacob, and Leah.</p><p>Rock-cut tombs with rolling stone doors were common in the Second Temple period, as evidenced by both archaeology and the gospel narratives of Jesus's burial. Joseph of Arimathea's new tomb was such a rock-cut chamber (<strong>John 19:41–42</strong>; <strong>Matt. 27:60</strong>). Jesus's resurrection involved the stone being rolled away and the tomb found empty (<strong>Luke 24:2</strong>). The whitewashing of tombs (<strong>Matt. 23:27</strong>) was a Passover practice to mark them so that priests could avoid corpse-uncleanness. Royal tombs in the City of David are mentioned (<strong>1 Kings 2:10</strong>; <strong>Acts 2:29</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["John 19:41", "Matthew 27:60", "Genesis 23:19", "Acts 2:29"]
},
"topheth": {
  "id": "topheth",
  "term": "Topheth",
  "category": "places",
  "intro": "<p>Topheth (or Tophet; Hebrew meaning \"place of burning\" or possibly from Aramaic <em>toph</em>, \"fireplace\") was a site in the Valley of Hinnom (Ge-Hinnom) southeast of Jerusalem where, in the period of the later monarchy, Israelites sacrificed their children by fire to the god Molech — a practice explicitly condemned by Jeremiah (<strong>Jer. 7:31–32</strong>; <strong>19:6</strong>). Kings Ahaz and Manasseh both \"made their sons pass through fire\" (<strong>2 Kings 16:3</strong>; <strong>21:6</strong>), and the practice was associated with the Valley of the Son of Hinnom.</p><p>King Josiah defiled Topheth as part of his religious reforms, so that no one could make a son or daughter pass through fire to Molech (<strong>2 Kings 23:10</strong>). Jeremiah prophesied it would be renamed \"the Valley of Slaughter\" when the bodies of those judged by God would be too numerous to bury. The valley's ongoing association with fire, filth, and corpses likely contributed to its becoming the name <em>Gehenna</em> (Greek form of Ge-Hinnom) — Jesus's primary term for the place of final judgment.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Jeremiah 7:31", "2 Kings 23:10", "Matthew 5:22"]
},
"town-clerk": {
  "id": "town-clerk",
  "term": "Town Clerk",
  "category": "people",
  "intro": "<p>The town clerk (<em>grammateus</em>, \"secretary\") of Ephesus appears in <strong>Acts 19:35–41</strong> as the city magistrate who calmed the riot in the theater sparked by Demetrius the silversmith's protest against Paul's preaching. His title is literally \"secretary\" in Greek, but at Ephesus this was the most important elected magistrate — the liaison between the city and Roman imperial authority, responsible for proclaiming official decrees and managing public assemblies.</p><p>His speech is remarkably reasonable: he points out that the accusation against Paul and his companions has not been proven, that there are proper legal courts (proconsuls) for legitimate grievances, and that the current unlawful assembly puts the city at risk of Roman intervention. His dismissal of the crowd saved Paul from mob violence. His words also function as an implicit exoneration of Paul in Luke's narrative — a Gentile civic official finding nothing illegal in Christian preaching. The episode illustrates both the volatile nature of Ephesian commerce tied to Artemis worship and Roman tolerance of Christianity when it was not seen as a political threat.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Acts 19:35", "Acts 19:40"]
},
"tribute-money": {
  "id": "tribute-money",
  "term": "Tribute Money",
  "category": "concepts",
  "intro": "<p>Two distinct tribute questions arise in the Gospels. The first concerns the half-shekel temple tax (<em>didrachmon</em>) required of every adult Jewish male annually for the upkeep of the sanctuary (<strong>Ex. 30:13</strong>). When questioned whether Jesus paid this tax, Peter affirmed he did; Jesus then directed Peter to find a <em>stater</em> (four-drachma coin) in a fish's mouth — exactly enough for two (<strong>Matt. 17:24–27</strong>). The second is the Roman poll tax (<em>denarius Caesaris</em>). The Pharisees and Herodians attempted to trap Jesus by asking whether it was lawful to pay tribute to Caesar; his answer — \"Render to Caesar the things that are Caesar's, and to God the things that are God's\" (<strong>Matt. 22:17–21</strong>) — both disarmed the trap and established the foundational Christian principle of dual obligation to civil and divine authority.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Matthew 17:24", "Matthew 22:17", "Exodus 30:13"]
},
"uncleanness": {
  "id": "uncleanness",
  "term": "Uncleanness",
  "category": "concepts",
  "intro": "<p>Ceremonial uncleanness in the Mosaic law was a state of ritual impurity that excluded a person from worship and community participation until appropriate purification was performed. Sources of uncleanness included: contact with a corpse (<strong>Num. 19:11–22</strong>), childbirth (<strong>Lev. 12</strong>), skin diseases (<strong>Lev. 13–14</strong>), bodily discharges (<strong>Lev. 15</strong>), and contact with certain animals or their carcasses (<strong>Lev. 11</strong>). The system distinguished between major uncleanness (requiring days or weeks of waiting plus sacrifice for restoration) and minor uncleanness (resolved by washing and waiting until evening).</p><p>The NT reinterprets cleanness radically: Jesus declared all foods clean (<strong>Mark 7:19</strong>) and touched lepers and the dead without becoming defiled — reversing the direction of contamination through his power to purify. Peter's vision at Joppa (<strong>Acts 10:9–16</strong>) used the clean/unclean food distinction to communicate the inclusion of Gentiles. Paul teaches that nothing is unclean in itself (<strong>Rom. 14:14</strong>) and that the body is a temple of the Holy Spirit, making moral rather than ritual purity the Christian's concern (<strong>1 Cor. 6:19–20</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Leviticus 11:2", "Mark 7:19", "Acts 10:15", "Romans 14:14"]
},
"urim-and-thummim": {
  "id": "urim-and-thummim",
  "term": "Urim and Thummim",
  "category": "concepts",
  "intro": "<p>The Urim and Thummim (Hebrew: <em>lights and perfections</em>) were objects kept in the high priest's breastplate and used to receive divine guidance on specific questions, particularly in matters of national decision (<strong>Ex. 28:30</strong>; <strong>Lev. 8:8</strong>). Their precise nature is unknown — ancient and modern scholars have proposed various theories including lots, gemstones that changed appearance, or oracle-mechanisms. Their function appears to have been binary (yes/no), as when Saul inquired about pursuing the Philistines and received no answer (<strong>1 Sam. 14:37, 41</strong>; <strong>28:6</strong>).</p><p>The Urim is explicitly mentioned as the medium of priestly inquiry in <strong>Numbers 27:21</strong>, where Joshua is to stand before Eleazar the priest who shall inquire for him by the judgment of the Urim. After the First Temple period, the Urim and Thummim apparently ceased functioning; the post-exilic community knew they were needed to settle questions of priestly lineage but had none available (<strong>Ezra 2:63</strong>; <strong>Neh. 7:65</strong>). No reference to them appears in the NT.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Exodus 28:30", "Numbers 27:21", "Ezra 2:63", "1 Samuel 28:6"]
},
"weights-and-measures": {
  "id": "weights-and-measures",
  "term": "Weights and Measures",
  "category": "concepts",
  "intro": "<p>Biblical Israel used both weight-based and volume-based measurement systems. <strong>Weights</strong> (for precious metals and commercial transactions) included: the talent (the largest unit, approximately 75 lbs.), the mina (1/60 of a talent), the shekel (the common unit, approximately 0.4 oz.), the beka (half-shekel), and the gerah (1/20 of a shekel). Weighing was done with a balance scale and stone weights, and the Mosaic law condemned dishonest weights (<strong>Lev. 19:35–36</strong>; <strong>Prov. 11:1</strong>). <strong>Dry measures</strong> included the homer (the largest, approximately 6.5 bushels), the ephah (1/10 homer), the seah (1/3 ephah), the omer (1/10 ephah), and the cab (1/6 ephah). <strong>Liquid measures</strong> included the bath (equal to the ephah), the hin (1/6 bath), and the log (1/12 hin).</p><p>NT measurements reflect the Greco-Roman system: the <em>modios</em> (peck, <strong>Matt. 5:15</strong>), the <em>choinix</em> (quart, <strong>Rev. 6:6</strong>), the <em>metretes</em> (about 10 gallons, <strong>John 2:6</strong>). Roman length measures include the <em>miliario</em> (Roman mile, <strong>Matt. 5:41</strong>) and the <em>stadion</em> (furlong).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Leviticus 19:35", "Proverbs 11:1", "Ezekiel 45:10", "Revelation 6:6"]
},
}

def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f"BP gap-smith-b: Smith I-Z scholarly: wrote {written}, skipped {skipped} existing.")

main()
