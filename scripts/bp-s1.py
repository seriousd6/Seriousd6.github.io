import json, os, pathlib

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def load_article(slug):
    p = pathlib.Path(OUT_DIR) / f'{slug}.json'
    return json.loads(p.read_text()) if p.exists() else None

def save_article(slug, data):
    p = pathlib.Path(OUT_DIR) / f'{slug}.json'
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False))

def merge_article(slug, data):
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True

ARTICLES = {
    "sabachthani": {
        "id": "sabachthani", "term": "Sabachthani", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sabachthani", "isbe": "sabachthani"},
        "key_refs": ["Matthew 27:46", "Mark 15:34"],
        "intro": "<p>Sabachthani (Aramaic <em>shebaqtani</em>, meaning <em>thou hast forsaken me</em>) is the concluding word of the cry of dereliction that Jesus uttered from the cross: <em>Eli, Eli, lama sabachthani?</em> — \"My God, my God, why have you forsaken me?\" (Matt. 27:46; Mark 15:34). The cry is a direct quotation of the opening verse of Psalm 22, spoken in Aramaic, the common language of first-century Judea. Its utterance at the ninth hour (approximately 3 PM) came after three hours of supernatural darkness over the land. The cry has been the subject of profound theological reflection: it expresses the full weight of Christ's atoning suffering, in which he bore the sin of his people and experienced the withdrawal of the Father's felt presence — the darkness of divine judgment — on their behalf. The fact that Psalm 22 moves from lament to triumphant vindication (Ps. 22:24–31) is understood as pointing toward the resurrection that followed the cross.</p>"
    },
    "sabaoth": {
        "id": "sabaoth", "term": "Sabaoth", "category": "concepts",
        "hitchcock_meaning": "Lord of hosts",
        "source_ids": {"easton": "sabaoth", "isbe": "sabaoth"},
        "key_refs": ["Romans 9:29", "James 5:4", "Isaiah 6:3", "Revelation 4:8"],
        "intro": "<p>Sabaoth is the Greek and Latin transliteration of the Hebrew <em>tseba'ot</em> (hosts or armies), a divine epithet appearing as part of the compound title <em>LORD of Sabaoth</em> — equivalent to \"LORD of hosts\" (<em>Yahweh Tseba'ot</em>). It occurs in the New Testament twice in transliterated form (Rom. 9:29, quoting Isa. 1:9; Jas. 5:4) and underlies the angelic acclamation \"Holy, holy, holy is the LORD of hosts\" in Isaiah 6:3, echoed in Revelation 4:8. The title emphasizes God's sovereign command over all celestial and terrestrial forces: the armies of heaven (angels and stars), the armies of earth (Israel's covenant host), and the unseen powers of the universe. It became one of the most frequent divine titles in the later prophets, particularly Isaiah, Jeremiah, and the post-exilic books, where it asserts God's sovereign power over Assyria, Babylon, and the nations despite Israel's apparent weakness. The Septuagint renders it variously as \"Almighty\" (<em>pantokrator</em>) or \"Lord of hosts\" (<em>kyrios sabaoth</em>).</p>"
    },
    "sabbath": {
        "id": "sabbath", "term": "Sabbath", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sabbath", "smith": "sabbath", "isbe": "sabbath"},
        "key_refs": ["Genesis 2:2", "Exodus 20:8", "Mark 2:27", "Colossians 2:16"],
        "intro": "<p>The Sabbath (Hebrew <em>shabbat</em>, from the verb <em>shabbath</em>, to cease or rest) is the seventh day of the week, set apart as a day of rest and worship by divine command. Its institution is traced to the creation account, where God rested on the seventh day and blessed it (Gen. 2:2–3). The Sabbath commandment is the fourth of the Ten Commandments (Ex. 20:8–11; Deut. 5:12–15), grounded in creation (Exodus) and in the Exodus from Egypt (Deuteronomy), making it both a commemoration of divine creation and a memorial of redemption. No work was to be done — neither by Israelites, servants, animals, nor resident aliens — and the penalty for violation was death (Ex. 35:2). Jesus' ministry generated controversy over Sabbath observance: he healed on the Sabbath and declared himself Lord of it (Mark 2:27–28; John 5:9–18). The early church shifted its principal day of worship to Sunday (the Lord's Day) in commemoration of the resurrection. Paul treats the Sabbath as part of the ceremonial shadow fulfilled in Christ (Col. 2:16; Heb. 4:9–11).</p>"
    },
    "sabbath-days-journey": {
        "id": "sabbath-days-journey", "term": "Sabbath day's journey", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sabbath-days-journey", "isbe": "sabbath-days-journey"},
        "key_refs": ["Acts 1:12", "Exodus 16:29", "Numbers 35:5"],
        "intro": "<p>A Sabbath day's journey was the maximum distance that Jewish tradition permitted a person to walk on the Sabbath without violating the law's prohibition against work. Based on a combination of Exodus 16:29 (\"let no one go out of his place on the seventh day\") and Numbers 35:5 (which set 2,000 cubits as the pastureland around a Levitical city), the rabbis fixed the Sabbath limit at 2,000 cubits — approximately 3,000 feet or just under half a mile. Acts 1:12 uses this measure to describe the distance from the Mount of Olives to Jerusalem: \"a Sabbath day's journey away.\" This measurement had no explicit Mosaic authority but was developed by scribal interpretation to provide a practical rule. It could be extended by an <em>eruv</em> (literally \"mixing\"), a legal device by which depositing food at the 2,000-cubit boundary created a fictive \"home,\" permitting travel an additional 2,000 cubits beyond. Jesus' disciples observed the Sabbath following the crucifixion without attempting to visit the tomb until Sunday (Luke 23:56).</p>"
    },
    "sabbatical-year": {
        "id": "sabbatical-year", "term": "Sabbatical year", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sabbatical-year", "smith": "sabbatical-year", "isbe": "sabbatical-year"},
        "key_refs": ["Leviticus 25:2", "Exodus 23:10", "Deuteronomy 15:1", "Nehemiah 10:31"],
        "intro": "<p>The sabbatical year (Hebrew <em>shemittah</em>, release) was the seventh year of a seven-year agricultural cycle during which, by Mosaic law, the land of Israel was to lie fallow and uncultivated (Lev. 25:2–7; Ex. 23:10–11). Whatever grew of itself during that year — volunteer crops and fruit — was not for the landowner but was to be left for the poor, the stranger, and the animals. Additionally, in the sabbatical year all debts owed by fellow Israelites were to be released or forgiven (Deut. 15:1–3), though debts from foreigners could still be collected. The institution expressed faith in God's provision (Lev. 25:20–22), care for the poor, and the principle that the land ultimately belonged to God. Leviticus 26:34–35 warns that failure to observe the sabbatical years will result in exile, during which the land will receive its missed rests — a connection made explicit by the Chronicler in attributing the length of the Babylonian exile to this neglect (2 Chr. 36:21). Nehemiah's restored community pledged to observe the sabbatical year (Neh. 10:31).</p>"
    },
    "sabeans": {
        "id": "sabeans", "term": "Sabeans", "category": "people",
        "hitchcock_meaning": "captivity; conversion; old age",
        "source_ids": {"easton": "sabeans", "smith": "sabeans"},
        "key_refs": ["Genesis 10:7", "Isaiah 43:3", "Isaiah 45:14", "Psalms 72:10"],
        "intro": "<p>The Sabeans were the inhabitants of Seba (or Sheba), a people descended from Cush through his son Seba (Gen. 10:7). Their relationship to the more famous kingdom of Sheba — the realm of the Queen of Sheba — has been debated: some equate Seba with Sheba (both names deriving from related roots), while others distinguish them as a Cushite (African) people near Ethiopia from the South Arabian Sheba. Isaiah identifies Seba as an African people associated with Egypt and Ethiopia (Isa. 43:3), and describes them as men of stature engaged in commerce (Isa. 45:14). Their conversion to Israel's God and tribute to the Messianic king are prophesied in Psalm 72:10: \"The kings of Sheba and Seba shall offer gifts.\" The Sabeans are mentioned in the book of Job as marauders who carried off Job's oxen and donkeys and slew his servants (Job 1:15), indicating a predatory nomadic tribe, possibly distinct from the more settled trading nation of Sheba.</p>"
    },
    "sabtah": {
        "id": "sabtah", "term": "Sabtah", "category": "people",
        "hitchcock_meaning": "a going about or circuiting; old age",
        "source_ids": {"easton": "sabtah", "smith": "sabtah"},
        "key_refs": ["Genesis 10:7", "1 Chronicles 1:9"],
        "intro": "<p>Sabtah (also spelled Sabta) was the third son of Cush, listed in the Table of Nations as a grandson of Ham and great-grandson of Noah (Gen. 10:7; 1 Chr. 1:9). Like his brothers Seba, Havilah, Raamah, and Sabtecha, he is mentioned as a progenitor of peoples in the post-flood world, though the nation or region bearing his name cannot be identified with certainty in the modern landscape. Some scholars have tentatively associated Sabtah with Sabota, an ancient Hadhramaut city in southern Arabia, or with regions along the east African or Arabian coast. As with most of the Table of Nations entries, the primary significance of Sabtah is genealogical — situating him within the broader Hamitic dispersion that populated Africa and parts of the ancient Near East following the flood.</p>"
    },
    "sabtecha": {
        "id": "sabtecha", "term": "Sabtecha", "category": "people",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sabtecha"},
        "key_refs": ["Genesis 10:7", "1 Chronicles 1:9"],
        "intro": "<p>Sabtecha (also spelled Sabtechah) was the fifth and last son of Cush listed in the Table of Nations (Gen. 10:7; 1 Chr. 1:9), making him a great-grandson of Noah through Ham and Cush. He appears in the most shadowy corner of the Cushite genealogy: unlike his more prominent brothers Seba and Raamah, no ancient region or people-group has been identified with any confidence as the descendants of Sabtecha. Some scholars have proposed a connection with the ancient city of Samydake on the Persian Gulf or with regions of the Arabian peninsula or East Africa, but these suggestions remain speculative. The name appears only in the two parallel genealogical lists and carries no narrative significance beyond its place in the Table of Nations' comprehensive mapping of the post-flood world.</p>"
    },
    "sachar": {
        "id": "sachar", "term": "Sachar", "category": "people",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sachar"},
        "key_refs": ["1 Chronicles 11:35", "2 Samuel 23:33", "1 Chronicles 26:4"],
        "intro": "<p>Sachar (meaning <em>hire</em> or <em>reward</em>) is the name of two men in the Old Testament. The first was the father of Ahiam, one of David's thirty mighty warriors (1 Chr. 11:35); his son is also called \"Ahiam the son of Sharar the Hararite\" in the parallel list of 2 Samuel 23:33, suggesting that Sachar and Sharar may be variant spellings of the same name, or that the two accounts reflect different textual traditions. The second Sachar was a son of Obed-edom the Gittite, one of the Levitical gatekeepers appointed by David to serve at the temple (1 Chr. 26:4). Obed-edom's household was remarkably blessed — the ark of the covenant rested in his house for three months (2 Sam. 6:11–12) — and his eight sons, including Sachar, served as capable men for temple service (1 Chr. 26:6–8).</p>"
    },
    "sackbut": {
        "id": "sackbut", "term": "Sackbut", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sackbut", "smith": "sackbut", "isbe": "sackbut"},
        "key_refs": ["Daniel 3:5", "Daniel 3:7", "Daniel 3:10", "Daniel 3:15"],
        "intro": "<p>The sackbut of the Authorized Version (Aramaic <em>sabkha</em>; Greek <em>sambuke</em>) was one of the instruments in the Babylonian royal orchestra that played at the command to worship Nebuchadnezzar's golden image (Dan. 3:5, 7, 10, 15). Despite the name, it has no connection with the Renaissance sackbut, which was a slide trombone — a wind instrument. The Aramaic <em>sabkha</em> was a stringed instrument similar to a triangular harp or lyre, with strings of different lengths producing a range of pitches. The Greek <em>sambuke</em> was a small four-stringed instrument with a high, shrill tone. Modern translations often render the word as \"trigon\" (a triangular lyre) or \"harp.\" The instrument's appearance in the Babylonian orchestra of Daniel 3 reflects the musical culture of the ancient Near East, where royal ceremonies routinely included ensembles of stringed, wind, and percussion instruments to accompany imperial religious rites.</p>"
    },
    "sackcloth": {
        "id": "sackcloth", "term": "Sackcloth", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sackcloth", "smith": "sackcloth", "isbe": "sackcloth"},
        "key_refs": ["Genesis 37:34", "2 Samuel 3:31", "Matthew 11:21", "Revelation 6:12"],
        "intro": "<p>Sackcloth was a coarse, rough fabric woven from black goat hair, used in the ancient Near East both for making sacks and grain bags and as a garment of mourning, penitence, and lamentation. The practice of wearing sackcloth as a sign of grief is attested from the earliest biblical narrative: Jacob put on sackcloth when he believed Joseph was dead (Gen. 37:34), and David commanded all the people to wear sackcloth to mourn for Abner (2 Sam. 3:31). It was worn directly against the skin, sometimes fastened around the waist as a loincloth, and accompanied by other mourning practices such as placing ashes on the head, fasting, and wailing. It served as a visible public expression of internal grief or repentance: the Ninevites put on sackcloth at Jonah's preaching (Jonah 3:5–8), and Jesus cited the failure of Chorazin and Bethsaida to repent in sackcloth and ashes (Matt. 11:21). In prophetic and apocalyptic texts, sackcloth clothes the sky and the sun as a sign of cosmic mourning (Isa. 50:3; Rev. 6:12).</p>"
    },
    "sacrifice": {
        "id": "sacrifice", "term": "Sacrifice", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sacrifice", "smith": "sacrifice", "isbe": "sacrifice"},
        "key_refs": ["Genesis 3:21", "Hebrews 10:1", "Hebrews 9:26", "Ephesians 5:2"],
        "intro": "<p>Sacrifice in the Bible refers to the offering of something precious — typically an animal or grain — to God as an act of worship, atonement, or consecration. The sacrificial system did not originate with human invention: Scripture presents it as divinely instituted from the beginning. Abel offered firstlings of his flock (Gen. 4:4; Heb. 11:4), and God clothed Adam and Eve with skins (Gen. 3:21), implying an early sacrificial act. The Mosaic law organized sacrifice into distinct types: the burnt offering (total consecration), the peace offering (fellowship), the sin offering (atonement for guilt), and the trespass offering. All sacrifices had to be without blemish, offered at the appointed place, with blood carefully handled — for the life is in the blood (Lev. 17:11). The prophets consistently subordinated ritual sacrifice to obedience and justice (1 Sam. 15:22; Hos. 6:6; Amos 5:21–24). The New Testament presents Christ's death as the final and perfect sacrifice that fulfilled and superseded the entire Levitical system: he offered himself once for all as the Lamb of God (Heb. 9:26; 10:10–14; Eph. 5:2; John 1:29).</p>"
    },
    "sadducees": {
        "id": "sadducees", "term": "Sadducees", "category": "concepts",
        "hitchcock_meaning": "followers of Sadoc, or Zadok",
        "source_ids": {"easton": "sadducees", "smith": "sadducees", "isbe": "sadducees"},
        "key_refs": ["Matthew 3:7", "Matthew 22:23", "Acts 23:6", "Acts 23:8"],
        "intro": "<p>The Sadducees were a Jewish religious and political party that arose probably in the Hasmonean period (second century BC), likely taking their name from Zadok, the high priest under Solomon whose family held the high priesthood for generations. They were the priestly aristocracy, closely associated with the Jerusalem temple and the high priestly families. Theologically, the Sadducees rejected the oral tradition (the traditions of the elders) that the Pharisees esteemed equally with the written Torah, accepting only the Pentateuch as authoritative. They denied the resurrection of the dead, the existence of angels, and the doctrine of divine providence over human affairs (Matt. 22:23; Acts 23:8), holding a more rationalistic and this-worldly perspective. They appear in the New Testament primarily as opponents of Jesus and the early church: they challenged Jesus on the resurrection (Matt. 22:23–33), and the high priestly party that arrested both Jesus and the apostles was Sadducean (Acts 4:1; 5:17). Their power depended on the temple; when Jerusalem fell in AD 70, they ceased to exist as a party.</p>"
    },
    "sadoc": {
        "id": "sadoc", "term": "Sadoc", "category": "people",
        "hitchcock_meaning": "or Zadok, just; righteous",
        "source_ids": {"easton": "sadoc", "smith": "sadoc", "isbe": "sadoc"},
        "key_refs": ["Matthew 1:14"],
        "intro": "<p>Sadoc (the Greek form of the Hebrew name Zadok, meaning <em>just</em> or <em>righteous</em>) appears in the genealogy of Jesus Christ in Matthew's Gospel (Matt. 1:14) as a descendant of Zerubbabel and an ancestor of Achim. He belongs to the post-exilic section of the genealogy, which traces the royal line of David from the return from Babylon through the period of the Second Temple down to Joseph, the legal father of Jesus. Nothing else is recorded of Sadoc in Scripture beyond his place in this genealogical list. His inclusion preserves the historical continuity of David's royal line through the generations between the Babylonian exile and the birth of Christ, fulfilling the promise that the Messiah would be of David's lineage (2 Sam. 7:12–13; Matt. 1:1).</p>"
    },
    "saffron": {
        "id": "saffron", "term": "Saffron", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "saffron", "smith": "saffron", "isbe": "saffron"},
        "key_refs": ["Song of Solomon 4:13", "Song of Solomon 4:14"],
        "intro": "<p>Saffron (Hebrew <em>karkom</em>; Arabic <em>za'faran</em>, meaning <em>yellow</em>) is the stigma of the crocus flower (<em>Crocus sativus</em>), used since antiquity as a spice, dye, and perfume. In Scripture it appears only in the Song of Solomon 4:13–14, listed among the precious spices and aromatic plants of the beloved's garden: \"Your shoots are an orchard of pomegranates with all choicest fruits, henna with nard, nard and saffron.\" Many species of crocus grow wild in Palestine, and the cultivated form was known across the ancient Near East for its vivid yellow color and distinctive fragrance. The pistils and stigmata of the crocus flowers were pressed into cakes for use as food flavoring, medicinal remedies, and yellow dye. Saffron remains one of the most expensive spices in the world by weight. Its appearance in the poem of the Song of Solomon places it among the most luxurious and exotic of the garden's treasures.</p>"
    },
    "saint": {
        "id": "saint", "term": "Saint", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "saint"},
        "key_refs": ["Psalms 16:3", "Romans 1:7", "Philippians 1:1", "Ephesians 2:19"],
        "intro": "<p>Saint (Hebrew <em>qadosh</em>; Greek <em>hagios</em>, literally <em>holy one</em>) in the biblical sense denotes one who has been set apart by God and consecrated to his service — not primarily a category of moral achievement but a designation of relationship and calling. In the Old Testament, the \"saints\" or \"holy ones\" are the covenant people of Israel, those set apart from the nations and consecrated to Yahweh (Ps. 16:3; Dan. 7:18). In the New Testament, the term is applied universally to all believers in Jesus Christ, not merely to a special class of the exceptionally virtuous. Paul addresses his letters to the saints at Rome (Rom. 1:7), Corinth (1 Cor. 1:2), Ephesus (Eph. 1:1), and Philippi (Phil. 1:1), meaning all Christians in those communities. Sainthood is thus the normal status of every person united to Christ by faith, sharing in his holiness through justification and the indwelling Spirit. The later Catholic and Orthodox development of a formal canonization process for recognizing saints post mortem reflects a narrowing of the term not found in the New Testament.</p>"
    },
    "sala": {
        "id": "sala", "term": "Sala", "category": "people",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sala"},
        "key_refs": ["Luke 3:35", "Luke 3:36", "1 Chronicles 1:18"],
        "intro": "<p>Sala (also spelled Salah, Shelah, or Selah in different textual traditions) was a descendant of Arphaxad (or Cainan) and an ancestor of Abraham, appearing in the genealogy from Shem to Abraham (Gen. 10:24; 11:12–15; 1 Chr. 1:18, 24). In Luke's genealogy of Jesus, he is listed between Cainan and Heber (Luke 3:35–36). The name's meaning is uncertain but has been connected with the root for a <em>shoot</em> or <em>sprout</em>. In the Genesis account he lived 433 years, fathering Eber at age thirty and living four hundred years more. He stands in the patriarchal genealogical bridge connecting the Noahic flood generation with the Abrahamic covenant line, one of the ancestors through whom the promise of the Messiah passed down the centuries.</p>"
    },
    "salamis": {
        "id": "salamis", "term": "Salamis", "category": "places",
        "hitchcock_meaning": "shaken; test; beaten",
        "source_ids": {"easton": "salamis", "smith": "salamis", "isbe": "salamis"},
        "key_refs": ["Acts 13:5"],
        "intro": "<p>Salamis was the principal city on the eastern coast of the island of Cyprus (modern Famagusta), situated at the mouth of the Pediaeus River on a broad bay of the eastern Mediterranean. In the first century it was the largest and most commercially significant city on the island, with a substantial Jewish community evidenced by the plural \"synagogues\" mentioned in Acts 13:5. Paul and Barnabas visited Salamis on their first missionary journey after sailing from Seleucia, the port of Antioch in Syria (Acts 13:4–5). Barnabas, himself a native of Cyprus (Acts 4:36), may have had personal connections to the city. The missionaries proclaimed the word in the synagogues, with John Mark accompanying them as an assistant. Salamis was the starting point for the crossing of the entire island westward to Paphos, where they confronted the sorcerer Bar-Jesus and the proconsul Sergius Paulus was converted (Acts 13:6–12).</p>"
    },
    "salathiel": {
        "id": "salathiel", "term": "Salathiel", "category": "people",
        "hitchcock_meaning": "asked or lent of God",
        "source_ids": {"easton": "salathiel", "smith": "salathiel", "isbe": "salathiel"},
        "key_refs": ["Matthew 1:12", "1 Chronicles 3:17", "Luke 3:27"],
        "intro": "<p>Salathiel (also spelled Shealtiel; meaning <em>I have asked of God</em>) is mentioned in the genealogies of Jesus as a link in the royal Davidic line during the period of the Babylonian exile. Matthew places him as the son of Jeconiah (Jehoiachin) and the father of Zerubbabel (Matt. 1:12; 1 Chr. 3:17), while Luke calls him the son of Neri (Luke 3:27). The apparent discrepancy is generally resolved by the hypothesis that Salathiel was the biological son of Neri from the Davidic line through Nathan, but was the legal heir of Jeconiah (who died childless, in fulfillment of Jer. 22:30) through adoption or levirate succession. As the father of Zerubbabel, who led the first return of exiles from Babylon, Salathiel represents the hinge point where the royal line survived the exile and the promise of David's throne was carried into the restoration period (Hag. 1:1; Ezra 3:2).</p>"
    },
    "salcah": {
        "id": "salcah", "term": "Salcah", "category": "places",
        "hitchcock_meaning": "thy basket; thy lifting up",
        "source_ids": {"easton": "salcah"},
        "key_refs": ["Deuteronomy 3:10", "Joshua 12:5", "Joshua 13:11"],
        "intro": "<p>Salcah (also Salchah or Salecah) was a city on the eastern frontier of Bashan, the fertile highland region east and northeast of the Sea of Galilee assigned to the half tribe of Manasseh. It marked the extreme eastern boundary of the territory of Og, king of Bashan, which Moses and the Israelites conquered (Deut. 3:10; Josh. 12:5; 13:11). The site is identified with modern Salkhad (or Sulkhad), a town approximately fifty-six miles east of the Jordan, situated in the Hauran upland with the Jebel Druz range to its east. An ancient basalt fortress stands at the site, and its strategic position on the edge of the desert made it a significant frontier stronghold. The reference in 1 Chronicles 5:11 also places it at the boundary of the Gadite settlements in the Transjordanian territory.</p>"
    },
    "salem": {
        "id": "salem", "term": "Salem", "category": "places",
        "hitchcock_meaning": "complete or perfect peace",
        "source_ids": {"easton": "salem", "smith": "salem"},
        "key_refs": ["Genesis 14:18", "Psalms 76:2", "Hebrews 7:1", "Hebrews 7:2"],
        "intro": "<p>Salem (meaning <em>peace</em>) is the royal city of Melchizedek, the priest-king who met Abraham after the defeat of the four kings and blessed him (Gen. 14:18; Heb. 7:1). It is generally identified with Jerusalem — the name \"Jerusalem\" (<em>Yerushalayim</em>) containing <em>shalem</em> within it, and Psalm 76:2 explicitly equating Salem with Zion: \"In Salem also is his tabernacle, and his dwelling place in Zion.\" The identification is not universally accepted, as some scholars have proposed other sites, but the predominant view links Salem-Jerusalem through the Melchizedek narrative as the ancient city that became David's capital. In the New Testament, the author of Hebrews makes the name theologically significant: Melchizedek is king of Salem, which means king of peace (<em>eirene</em>), interpreting his city's name as a type of Christ's messianic peace (Heb. 7:2).</p>"
    },
    "salim": {
        "id": "salim", "term": "Salim", "category": "places",
        "hitchcock_meaning": "foxes; fists; path",
        "source_ids": {"easton": "salim", "smith": "salim", "isbe": "salim"},
        "key_refs": ["John 3:23"],
        "intro": "<p>Salim was a place near Aenon where John the Baptist was baptizing many people because water was plentiful there (John 3:23). The location is described as being \"in Judea\" by implication (John 3:22) and was distinct from the Bethany beyond Jordan (John 1:28) where John had previously been active. The most favored identification places Salim (and the nearby Aenon) in the Jordan valley at the head of the broad Wadi Far'ah, approximately seven miles south of Scythopolis, where abundant springs match the condition \"because water was plentiful.\" A site called Ainun and Salim is still found in this region. The passage is also significant for the Baptist's final recorded testimony, where he declares himself the \"friend of the bridegroom\" and affirms that Christ must increase while he must decrease (John 3:29–30).</p>"
    },
    "sallai": {
        "id": "sallai", "term": "Sallai", "category": "people",
        "hitchcock_meaning": "Sallu, an exaltation; a basket",
        "source_ids": {"easton": "sallai", "isbe": "sallai"},
        "key_refs": ["Nehemiah 11:8", "Nehemiah 12:20"],
        "intro": "<p>Sallai is the name of two men in the post-exilic community described in Nehemiah. The first was a Benjamite who settled in Jerusalem after the return from exile, listed among the inhabitants of the holy city in Nehemiah 11:8, where 928 Benjamites in total are numbered. The second Sallai was a priest who returned from Babylon with Zerubbabel and was the head of a priestly family in the days of the high priest Joiakim (Neh. 12:20). In the parallel list of Nehemiah 12:7, a variant form of the name appears as \"Sallu.\" Beyond their inclusion in these restoration-era registers, neither man is the subject of any narrative record. They represent the broad community of returned exiles — priests, Levites, and laymen — who rebuilt the religious and civic infrastructure of post-exilic Judah.</p>"
    },
    "sallu": {
        "id": "sallu", "term": "Sallu", "category": "people",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sallu", "isbe": "sallu"},
        "key_refs": ["1 Chronicles 9:7", "Nehemiah 11:7", "Nehemiah 12:7"],
        "intro": "<p>Sallu (meaning <em>weighed</em> or <em>paid</em>) is the name of two men in the post-exilic biblical records. The first was a Benjamite, son of Meshullam, who was among the first to resettle in Jerusalem after the return from Babylon (1 Chr. 9:7; Neh. 11:7). The second Sallu was a priest who returned with Zerubbabel and is listed as the head of a priestly family in the days of Joiakim the high priest (Neh. 12:7). The priestly Sallu corresponds to the \"Sallai\" of Neh. 12:20, the two names being variants of the same individual or family designation. Like many of the names in these post-exilic rosters, Sallu appears solely in genealogical and administrative lists, representing the organized reestablishment of tribal and priestly communities in the land after the Babylonian exile.</p>"
    },
    "salmon": {
        "id": "salmon", "term": "Salmon", "category": "people",
        "hitchcock_meaning": "peaceable; perfect; he that rewards",
        "source_ids": {"easton": "salmon", "smith": "salmon"},
        "key_refs": ["Ruth 4:20", "Matthew 1:4", "Matthew 1:5", "1 Chronicles 2:51"],
        "intro": "<p>Salmon (also Salma) was the son of Nashon, chief of Judah in the wilderness (Num. 2:3), and is notable as the husband of Rahab the Canaanite woman of Jericho and the father of Boaz (Ruth 4:20–21; Matt. 1:4–5; 1 Chr. 2:11). He thus stands at a significant genealogical junction: through his marriage to Rahab and his son Boaz's marriage to Ruth, Salmon is an ancestor of David and through David of Jesus Christ (Matt. 1:5–16). The inclusion of Rahab in Matthew's genealogy is theologically significant, highlighting God's grace in drawing Gentile women of faith into the royal messianic line. The name Salma appears in 1 Chronicles 2:51, 54 in connection with Bethlehem, where Salmon may have settled after entering Canaan with Joshua's generation. A separate Easton entry notes a \"Salmon\" as the hill covered with dark forests south of Shechem (cf. Ps. 68:14), which is a distinct place entirely, also known as Zalmon.</p>"
    },
    "salmone": {
        "id": "salmone", "term": "Salmone", "category": "places",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "salmone", "smith": "salmone", "isbe": "salmone"},
        "key_refs": ["Acts 27:7"],
        "intro": "<p>Salmone was a promontory or cape at the northeastern extremity of the island of Crete, under which Paul's ship struggled to sail during his voyage to Rome as a prisoner (Acts 27:7). Contrary winds had slowed the journey along the southern coast of Asia Minor, and after difficult sailing the ship rounded Cape Salmone and made its way westward along the southern shore of Crete toward Fair Havens (Acts 27:8). The cape is identified with the modern Cape Sidero (or Cape Plaka), the easternmost point of Crete, a bold headland that marked the entrance into the sheltered southern coast. The ship's struggle to sail \"under the lee of Crete\" past Salmone foreshadowed the great storm that would eventually wreck the vessel off Malta (Acts 27:14–44), making this headland a waypoint in one of the New Testament's most dramatic travel narratives.</p>"
    },
    "salome": {
        "id": "salome", "term": "Salome", "category": "people",
        "hitchcock_meaning": "same as Salmon",
        "source_ids": {"easton": "salome", "smith": "salome", "isbe": "salome"},
        "key_refs": ["Matthew 27:56", "Mark 15:40", "Mark 16:1", "John 19:25"],
        "intro": "<p>Salome (a Greek form of the Hebrew Shalom, meaning <em>peaceful</em>) was, in the New Testament, the wife of Zebedee the fisherman and mother of James and John the apostles. She was among the women who followed Jesus from Galilee and ministered to him (Matt. 27:55–56; Mark 15:40–41). She appears to have been the sister of Mary the mother of Jesus (John 19:25 with Mark 15:40), which would make James and John first cousins of Jesus — possibly explaining her bold request that her sons be given places of honor at Jesus' right and left hand in his kingdom (Matt. 20:20–21; cf. 19:28). Salome was present at the crucifixion observing from a distance (Mark 15:40), and on Easter morning she was among the women who brought spices to anoint Jesus' body and received the first announcement of the resurrection (Mark 16:1–8). Her faith and devotion made her part of the innermost circle of Jesus' female followers.</p>"
    },
    "salt": {
        "id": "salt", "term": "Salt", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "salt", "smith": "salt", "isbe": "salt"},
        "key_refs": ["Leviticus 2:13", "Ezra 4:14", "Mark 9:49", "Colossians 4:6"],
        "intro": "<p>Salt held exceptional significance in biblical culture, serving simultaneously as a food preservative, a covenant symbol, a sacrificial requirement, and a metaphor for wisdom and purity. The Mosaic law required that all grain offerings be seasoned with salt, and the use of leaven and honey was forbidden (Lev. 2:13) — salt being the antithesis of corruption. The \"covenant of salt\" (<em>brit melah</em>) was an irrevocable and perpetual agreement: God's covenant with David (2 Chr. 13:5) and the Levitical priesthood (Num. 18:19) were both described in these terms. To eat salt with someone was to share hospitality and enter a binding relationship of mutual loyalty (Ezra 4:14; Acts 1:4 LXX). Salt's destructive power when applied to land is reflected in the sowing of salt over Shechem (Judg. 9:45). Jesus called his disciples \"the salt of the earth\" — agents of preservation and flavor in the world (Matt. 5:13; Mark 9:50). Paul exhorts speech to be \"seasoned with salt\" — gracious and apt (Col. 4:6).</p>"
    },
    "salt-sea": {
        "id": "salt-sea", "term": "Salt Sea", "category": "places",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "salt-sea", "isbe": "salt-sea"},
        "key_refs": ["Genesis 14:3", "Numbers 34:3", "Joshua 3:16", "Deuteronomy 3:17"],
        "intro": "<p>The Salt Sea is one of the biblical designations for what is today called the Dead Sea, the hypersaline terminal lake at the southern end of the Jordan Rift Valley, approximately 50 miles long and 11 miles wide. It lies at approximately 1,412 feet below sea level, making it the lowest exposed body of water on earth. Its high salt concentration — roughly ten times that of ocean water — prevents almost all biological life, hence the name Dead Sea. In the Old Testament it is called the Salt Sea (Gen. 14:3; Num. 34:3, 12; Josh. 3:16; 15:2; Deut. 3:17), the Sea of the Arabah (Deut. 4:49; Josh. 3:16), and the Eastern Sea (Ezek. 47:18; Zech. 14:8). Its southern region, known in antiquity as the Vale of Siddim, was the area of the five cities of the plain including Sodom and Gomorrah (Gen. 14:3). Ezekiel's eschatological vision sees its waters healed and teeming with fish (Ezek. 47:8–10).</p>"
    },
    "salt-the-city-of": {
        "id": "salt-the-city-of", "term": "Salt, The city of", "category": "places",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "salt-the-city-of"},
        "key_refs": ["Joshua 15:62"],
        "intro": "<p>The City of Salt was one of six cities listed in the wilderness district of Judah's southern inheritance (Josh. 15:61–62), situated near the Dead Sea in the barren region of the Judean wilderness. Its precise identification is uncertain, but some scholars locate it at Khirbet Qumran — the site later occupied by the Essene community who produced the Dead Sea Scrolls — or at another site near the northwestern shore of the Dead Sea. The region's name may derive from the extensive salt deposits found in the area around the Dead Sea. The six cities of this southern wilderness district, including the City of Salt, En Gedi, and Nibshan, formed the southernmost tier of Judah's settled territory, occupying the desolate but strategically important region bordering the Negev and the Salt Sea.</p>"
    },
    "salt-valley-of": {
        "id": "salt-valley-of", "term": "Salt, Valley of", "category": "places",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "salt-valley-of", "smith": "salt-valley-of", "isbe": "salt-valley-of"},
        "key_refs": ["2 Samuel 8:13", "2 Kings 14:7", "1 Chronicles 18:12", "2 Chronicles 25:11"],
        "intro": "<p>The Valley of Salt was the site of two notable Israelite military victories. David smote the Syrians (or Edomites — the textual tradition is complex) in the Valley of Salt (2 Sam. 8:13; 1 Chr. 18:12; Ps. 60 title), reportedly killing 18,000 Edomites. Approximately two centuries later, Amaziah king of Judah also defeated Edom there, killing 10,000 in the valley and capturing 10,000 more prisoners whom he threw from the top of a cliff (2 Kings 14:7; 2 Chr. 25:11). The valley is generally identified with the broad depression of the Arabah south of the Dead Sea, the salt flats near the Wadi el-Milh (\"Salt Valley\") between Judah and Edom. The salt marshes of this region would have made the area hostile terrain for a retreating army, contributing to the decisive nature of both victories.</p>"
    },
    "salutation": {
        "id": "salutation", "term": "Salutation", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "salutation", "smith": "salutation", "isbe": "salutation"},
        "key_refs": ["Luke 1:41", "Luke 10:4", "Matthew 5:47", "1 Corinthians 16:21"],
        "intro": "<p>Salutation in biblical culture was a formal greeting ritual of considerable social and religious significance, far more elaborate than modern Western conventions. Eastern greetings involved numerous inquiries after the health and well-being of the person, their family, and household, conducted with bows and sometimes prostration, and could consume substantial time. Jewish salutations typically included the word <em>shalom</em> (peace): \"Peace be to you, and peace be to your house, and peace be to all that you have\" (1 Sam. 25:6). Jesus instructed his disciples not to salute anyone on the road when sent on urgent mission (Luke 10:4), reflecting the time-consuming nature of Eastern greetings. The salutation of Mary by the angel Gabriel (Luke 1:28) and of Elizabeth to Mary (Luke 1:41) are described with this vocabulary. Paul closed his letters with personal salutations by hand as a mark of authenticity (1 Cor. 16:21; Gal. 6:11; Col. 4:18), giving the written greeting an equivalent weight to the personal act.</p>"
    },
    "salvation": {
        "id": "salvation", "term": "Salvation", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "salvation", "isbe": "salvation"},
        "key_refs": ["Exodus 14:13", "Luke 19:10", "Hebrews 2:3", "Ephesians 2:8"],
        "intro": "<p>Salvation in the Bible denotes deliverance from danger, evil, or destruction — ranging from physical rescue to the ultimate spiritual redemption of the soul. In the Old Testament the term is used broadly: of Israel's deliverance from Egypt (Ex. 14:13), military victories (1 Sam. 11:13), and rescue from enemies (Ps. 68:19–20). Its deepest OT application is to God's deliverance from sin and its consequences, anticipated in the prophets through the coming of the Suffering Servant (Isa. 52:10; 53) and a new covenant (Jer. 31:31–34). In the New Testament, salvation is the central category of the gospel: Jesus came to seek and to save the lost (Luke 19:10), and his name itself means <em>Yahweh saves</em> (Matt. 1:21). The New Testament presents salvation as deliverance from the guilt and power of sin (Rom. 6:14; Titus 2:11–14), accomplished through Christ's atoning death (Rom. 5:9–10) and received through faith alone (Eph. 2:8–9). It encompasses justification (past), sanctification (present), and glorification (future) — the full scope of redemption applied by the Holy Spirit to every believer.</p>"
    },
    "samaria": {
        "id": "samaria", "term": "Samaria", "category": "places",
        "hitchcock_meaning": "watch-mountain",
        "source_ids": {"easton": "samaria", "smith": "samaria"},
        "key_refs": ["1 Kings 16:24", "2 Kings 17:24", "John 4:4", "Acts 8:5"],
        "intro": "<p>Samaria was both the capital city of the northern kingdom of Israel and the region surrounding it. The city was founded by Omri, king of Israel (c. 880 BC), who purchased the hill of Shemer for two talents of silver and built upon it, naming it after its former owner (1 Kings 16:24). Situated on an isolated, strategically commanding hill in the central highlands, it served as Israel's capital until the Assyrian conquest of 722 BC under Sargon II, who deported most of the Israelite population and resettled the region with peoples from Babylon, Cuthah, Avva, Hamath, and Sepharvaim (2 Kings 17:24). This mixing of populations and religions produced the Samaritans. The region of Samaria lay between Galilee to the north and Judea to the south, and Jews typically avoided traveling through it due to ethnic and religious tensions. Jesus deliberately passed through Samaria (John 4:4), and his conversation with the Samaritan woman at Jacob's well is one of the longest dialogues recorded in the Gospels. Philip's preaching in Samaria following the Jerusalem persecution marked the gospel's expansion into the second circle of Acts 1:8.</p>"
    },
    "samaritan-pentateuch": {
        "id": "samaritan-pentateuch", "term": "Samaritan Pentateuch", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "samaritan-pentateuch", "smith": "samaritan-pentateuch", "isbe": "samaritan-pentateuch"},
        "key_refs": ["Exodus 12:40", "Galatians 3:17"],
        "intro": "<p>The Samaritan Pentateuch is the text of the first five books of Moses (Torah) as preserved by the Samaritan community, written in an archaic form of the Hebrew script (Paleo-Hebrew). It arose after the schism between Jews and Samaritans, probably in the fifth or fourth century BC, when the Samaritans established their own sanctuary on Mount Gerizim and developed their own textual tradition. The Samaritan Pentateuch accepts only the Pentateuch as canonical, rejecting the rest of the Hebrew Bible. It preserves an important ancient textual tradition that in several passages agrees with the Septuagint against the Masoretic Text, suggesting that all three preserve different streams of an ancient common exemplar. One notable difference concerns Exodus 12:40: where the Masoretic Text says \"the time that the people of Israel lived in Egypt was 430 years,\" the Samaritan Pentateuch and Septuagint add \"and in the land of Canaan,\" aligning with Paul's figure in Galatians 3:17. The Samaritan Pentateuch has been a significant resource in the history of textual criticism.</p>"
    },
    "samaritans": {
        "id": "samaritans", "term": "Samaritans", "category": "people",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "samaritans", "smith": "samaritans", "isbe": "samaritans"},
        "key_refs": ["2 Kings 17:24", "Ezra 4:2", "Luke 17:16", "John 4:9"],
        "intro": "<p>The Samaritans were the mixed population that resulted from the Assyrian resettlement of the former northern kingdom of Israel following Sargon II's deportation of the Israelites in 722 BC. The Assyrians brought colonists from Babylon, Cuthah, Avva, Hamath, and Sepharvaim, who intermingled with the remaining Israelite population and blended their pagan religious practices with the worship of Yahweh (2 Kings 17:24–41). When the Jewish exiles returned from Babylon under Zerubbabel, they rejected the Samaritans' offer to help rebuild the temple, creating a lasting breach (Ezra 4:1–5). The Samaritans built their own temple on Mount Gerizim, which the Hasmonean ruler John Hyrcanus destroyed around 128 BC. By the New Testament era, the animosity was deep-rooted: \"Jews have no dealings with Samaritans\" (John 4:9). Jesus deliberately crossed these boundaries: he spoke with the Samaritan woman (John 4), healed ten lepers including one Samaritan (Luke 17:16), and made a Samaritan the hero of one of his most famous parables (Luke 10:33). Philip's mission to Samaria (Acts 8:5–8) extended the gospel across this ethnic and religious divide.</p>"
    },
    "samgar-nebo": {
        "id": "samgar-nebo", "term": "Samgar-nebo", "category": "people",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "samgar-nebo", "isbe": "samgar-nebo"},
        "key_refs": ["Jeremiah 39:3"],
        "intro": "<p>Samgar-nebo appears in Jeremiah 39:3 as one of the Babylonian princes who entered Jerusalem through the middle gate after Nebuchadnezzar breached the city's walls in 586 BC. The text lists several officials by name: Nergal-sharezer, Samgar-nebo, Sarsechim (Rab-saris), Nergal-sharezer (Rab-mag), and others. Modern scholarship has proposed that \"Samgar-nebo\" may be a title or an epithet rather than a proper name, and that the list as a whole involves scribal difficulties. Some have suggested that Samgar-nebo may be a variant form of a Babylonian court title meaning <em>be gracious, O Nebo</em> or <em>cup-bearer of Nebo</em>, possibly attached to one of the Nergal-sharezer officials in the list. The Babylonian officials' presence at the middle gate symbolized the complete fulfillment of Jeremiah's prophecies of Jerusalem's fall to Nebuchadnezzar (Jer. 21:7; 25:9).</p>"
    },
    "samos": {
        "id": "samos", "term": "Samos", "category": "places",
        "hitchcock_meaning": "full of gravel",
        "source_ids": {"easton": "samos", "smith": "samos", "isbe": "samos"},
        "key_refs": ["Acts 20:15"],
        "intro": "<p>Samos was an Aegean island approximately 27 miles long and 20 miles broad, lying off the coast of Lydia (Asia Minor) about 42 miles southwest of Smyrna and separated from the mainland by a narrow strait. It was famous in antiquity as the birthplace of the mathematician and philosopher Pythagoras and as a center of Hera worship. Paul passed by Samos on his third missionary journey, sailing from Mitylene to Miletus (Acts 20:15), calling in there briefly — whether the ship anchored for the night is unclear from the text. The voyage was pressing: Paul was hurrying to reach Jerusalem by Pentecost and had deliberately bypassed Ephesus to avoid a delay (Acts 20:16). Samos thus appears as a waypoint in Paul's final journey southward through the Aegean islands toward Jerusalem, where he would be arrested and begin his journey to Rome.</p>"
    },
    "samothracia": {
        "id": "samothracia", "term": "Samothracia", "category": "places",
        "hitchcock_meaning": "an island possessed by the Samians and Thracians",
        "source_ids": {"easton": "samothracia", "smith": "samothracia"},
        "key_refs": ["Acts 16:11"],
        "intro": "<p>Samothracia (modern Samothrace) was a mountainous island in the northeastern Aegean Sea, about 32 miles long and 6 miles broad, lying approximately 38 miles from the Thracian coast. Its name reflects its dual heritage from Samian and Thracian settlers. The island's central peak, Mount Fengari, rises to nearly 5,500 feet — the highest point in the Aegean — and was visible from a great distance, making the island an important navigational landmark. Paul passed by Samothracia on his first voyage to Europe following the Macedonian vision, sailing from Troas to Neapolis on the Macedonian coast (Acts 16:11). The ship ran before the wind and made the 150-mile crossing in a single day, stopping overnight at Samothracia before continuing to Neapolis the next day. From Neapolis Paul traveled inland to Philippi, where he would found the first European Christian congregation.</p>"
    },
    "samson": {
        "id": "samson", "term": "Samson", "category": "people",
        "hitchcock_meaning": "his sun; his service; there the second time",
        "source_ids": {"easton": "samson", "smith": "samson", "isbe": "samson"},
        "key_refs": ["Judges 13:5", "Judges 14:6", "Judges 16:30", "Hebrews 11:32"],
        "intro": "<p>Samson, son of Manoah of the tribe of Dan, was the last of the major judges of Israel, whose birth was announced by the angel of the LORD to his previously barren mother (Judg. 13). He was consecrated as a Nazirite from the womb — the first such designation in Scripture — meaning he was to abstain from wine and strong drink and was never to cut his hair, the outward sign of his consecration to God (Judg. 13:5). His superhuman strength, empowered by the Spirit of the LORD, enabled him to kill a lion with his bare hands (Judg. 14:6), slay thirty Philistines, and defeat a thousand enemies with the jawbone of a donkey (Judg. 15:15). His life was tragically marked by entanglement with Philistine women: his marriage to a woman of Timnath and his infatuation with Delilah proved his undoing. Delilah extracted the secret of his strength, had his hair shaved, and delivered him blinded and bound to the Philistines (Judg. 16:17–21). In a final act of faith, he pulled down the pillars of the temple of Dagon, killing more enemies in his death than in his life (Judg. 16:30). He is listed among the heroes of faith in Hebrews 11:32.</p>"
    },
    "samuel": {
        "id": "samuel", "term": "Samuel", "category": "people",
        "hitchcock_meaning": "heard of God; asked of God",
        "source_ids": {"easton": "samuel", "smith": "samuel", "isbe": "samuel"},
        "key_refs": ["1 Samuel 1:20", "1 Samuel 7:15", "1 Samuel 12:3", "Acts 3:24"],
        "intro": "<p>Samuel, whose name means <em>heard of God</em> (or <em>asked of God</em>), was the last of the judges and the first of the prophets in the monarchic era — a transitional figure of immense importance in Israel's history. His birth was the answer to the earnest prayer of his mother Hannah, who consecrated him to the LORD before his birth (1 Sam. 1:11, 20). He was brought to the tabernacle at Shiloh to serve under Eli the priest, and there received the divine call in a night vision (1 Sam. 3). He led Israel's spiritual renewal and military recovery at the battle of Mizpah (1 Sam. 7), where the Philistines were routed after Israel repented. When Israel demanded a king, Samuel anointed Saul (1 Sam. 10) and later David (1 Sam. 16) at divine direction. He judged Israel faithfully all his days (1 Sam. 7:15–17) and closed his public career with an appeal for the nation to serve God in integrity (1 Sam. 12). After his death his spirit was summoned by the witch of Endor at Saul's request (1 Sam. 28:11–19). Peter and subsequent NT writers identify Samuel as the beginning of the prophetic line (Acts 3:24; Heb. 11:32).</p>"
    },
    "samuel-books-of": {
        "id": "samuel-books-of", "term": "Samuel, Books of", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "samuel-books-of", "smith": "samuel-books-of", "isbe": "samuel-books-of"},
        "key_refs": ["1 Samuel 27:6", "1 Chronicles 29:29", "2 Samuel 11:2"],
        "intro": "<p>The Books of Samuel (originally a single book in the Hebrew canon) cover the transition from the period of the judges to the monarchy in Israel, spanning roughly from the birth of Samuel (c. 1105 BC) to the last years of David (c. 970 BC). The LXX divided the single Hebrew scroll into two books, treating them as the first and second books of the kingdoms. The authorship is attributed to Samuel for the earlier sections, while 1 Chronicles 29:29 mentions the chronicles of Nathan the prophet and Gad the seer as additional sources. First Samuel narrates the birth and career of Samuel, the rise and fall of Saul, and David's anointing and years of fugitive life. Second Samuel chronicles David's reign — his military conquests, the Davidic covenant (2 Sam. 7), the crisis of Bathsheba and Uriah, Absalom's rebellion, and the closing years of his rule. Theologically, the books explore the nature of kingship, the costliness of sin even in great leaders, and the faithfulness of God to his covenant promises despite human failure.</p>"
    },
    "sanballat": {
        "id": "sanballat", "term": "Sanballat", "category": "people",
        "hitchcock_meaning": "bramble-bush; enemy in secret",
        "source_ids": {"easton": "sanballat", "smith": "sanballat", "isbe": "sanballat"},
        "key_refs": ["Nehemiah 2:10", "Nehemiah 4:1", "Nehemiah 6:1", "Nehemiah 13:28"],
        "intro": "<p>Sanballat the Horonite was a governor or official of Samaria who became the primary adversary of Nehemiah's mission to rebuild the walls of Jerusalem. When Nehemiah arrived in Judea with the commission of King Artaxerxes (Neh. 2:10), Sanballat and his allies — Tobiah the Ammonite and Geshem the Arab — were displeased that anyone should come to seek the welfare of the children of Israel. They employed a progression of tactics to hinder the rebuilding: mockery and ridicule (Neh. 4:1–3), threats of military intervention (Neh. 4:8), false accusation of rebellion before Artaxerxes (Neh. 2:19), attempted entrapment by inviting Nehemiah to a conference (Neh. 6:1–4), and hiring a false prophet to intimidate him (Neh. 6:10–14). All these efforts failed. Sanballat's family had penetrated the Jerusalem priesthood through the marriage of his daughter to the son of the high priest Joiada, a connection that Nehemiah expelled (Neh. 13:28). The Elephantine papyri from Egypt (c. 407 BC) independently confirm Sanballat's existence and the name of his sons Delaiah and Shelemiah.</p>"
    },
    "sanctification": {
        "id": "sanctification", "term": "Sanctification", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sanctification", "isbe": "sanctification"},
        "key_refs": ["Romans 6:22", "1 Thessalonians 4:3", "Hebrews 10:14", "2 Thessalonians 2:13"],
        "intro": "<p>Sanctification (from Latin <em>sanctificare</em>, to make holy; Greek <em>hagiasmos</em>) is the progressive work of God by which believers are transformed in character and conduct to conform increasingly to the holiness of Christ. It is distinguished from justification (which is an instantaneous forensic declaration) in that sanctification is an ongoing process involving both divine agency and human cooperation. The New Testament presents it as God's will for every believer (1 Thess. 4:3) and the fruit of union with Christ (1 Cor. 1:30; Heb. 10:14). Sanctification involves the mortification of sinful desires and the cultivation of the Spirit's fruit through the means of grace — Scripture, prayer, the sacraments, and the community of the church (John 17:17; Rom. 8:13; 12:1–2). It is worked out in the believer \"with fear and trembling\" because it is God who works both the willing and the doing (Phil. 2:12–13). The final goal is glorification — complete conformity to Christ's image at the resurrection (Rom. 8:29–30; 1 John 3:2).</p>"
    },
    "sanctuary": {
        "id": "sanctuary", "term": "Sanctuary", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sanctuary", "isbe": "sanctuary"},
        "key_refs": ["Exodus 25:8", "Psalms 114:2", "Hebrews 9:1", "Revelation 21:22"],
        "intro": "<p>Sanctuary (Hebrew <em>miqdash</em>, from <em>qadash</em>, to be holy; Greek <em>hagion</em>) denotes a holy place set apart for the presence and worship of God. In the broadest biblical usage it can refer to the Holy Land itself (Ex. 15:17; Ps. 114:2), but more specifically it designates the tabernacle (Ex. 25:8; Lev. 12:4), the Jerusalem temple (1 Chr. 22:19; 2 Chr. 29:21), or the inner holy place within either structure. The essential idea is that the sanctuary is the appointed place where God's presence dwells among his people, requiring reverence, ritual purity, and proper approach through the ordained mediatory system. The tabernacle and temple are explicitly called \"sanctuaries\" to emphasize their character as holy ground, not merely religious buildings. God himself is called a sanctuary for his exiled people (Ezek. 11:16). The New Testament reinterprets the sanctuary concept: Christ's body is the true temple (John 2:21), the church is the dwelling place of the Spirit (Eph. 2:21–22), and the believer's body is a temple of the Holy Spirit (1 Cor. 6:19). The heavenly sanctuary into which Christ entered with his own blood is the antitype of all earthly sanctuaries (Heb. 9:11–12).</p>"
    },
    "sandals": {
        "id": "sandals", "term": "Sandals", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sandals"},
        "key_refs": ["Mark 6:9", "Acts 12:8", "Ezekiel 16:10", "Mark 1:7"],
        "intro": "<p>Sandals in the biblical world were the standard footwear of both the poor and wealthy, consisting of a flat sole made of wood, leather, or palm bark fastened to the foot by straps or thongs tied around the ankle and instep. They are distinguished from shoes (which enclosed the foot) in that they left the top of the foot exposed. Removing sandals was a mark of humility or reverence: Moses was commanded to remove his sandals at the burning bush (Ex. 3:5), and Joshua before the angel of the LORD (Josh. 5:15). The custom of the kinsman-redeemer was confirmed by the removing of a sandal (Ruth 4:7–8). John the Baptist, measuring his own humility before Jesus, declared himself unworthy even to perform the slave's task of unfastening the Messiah's sandal (Mark 1:7; John 1:27). Jesus instructed the Twelve to wear sandals for their journeys (Mark 6:9), and Paul was told to bind on his sandals when the angel freed him from prison (Acts 12:8). The metaphor of having feet \"shod with the readiness of the gospel of peace\" uses sandals as an image of the Christian's preparedness for mission (Eph. 6:15).</p>"
    },
    "sanhedrim": {
        "id": "sanhedrim", "term": "Sanhedrim", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sanhedrim"},
        "key_refs": ["Matthew 5:22", "Matthew 26:59", "Mark 15:1", "Acts 4:15"],
        "intro": "<p>The Sanhedrin (Greek <em>synedrion</em>, a sitting together, or council; rendered \"council\" in the AV) was the supreme judicial and administrative council of the Jewish people during the Second Temple period and beyond. According to Jewish tradition it originated with Moses (Num. 11:16), but in its classical form it was a body of 71 members presided over by the high priest, meeting in the Hall of Hewn Stone near the Jerusalem temple. It had authority over religious law, civil matters within Roman-permitted limits, and could impose capital punishment by stoning (though crucifixion required Roman authorization, as in Jesus' case). Its membership included chief priests, elders, and scribes, representing both Sadducean and Pharisaic factions. The Sanhedrin is frequently encountered in the New Testament: it tried Jesus (Matt. 26:59; Mark 15:1), condemned Stephen to stoning (Acts 6:12–15; 7:57–58), examined Peter and John (Acts 4:5–22), and tried Paul (Acts 22:30–23:10). Its authority was extinguished with the fall of Jerusalem in AD 70.</p>"
    },
    "sansannah": {
        "id": "sansannah", "term": "Sansannah", "category": "places",
        "hitchcock_meaning": "bough or bramble of the enemy",
        "source_ids": {"easton": "sansannah", "smith": "sansannah", "isbe": "sansannah"},
        "key_refs": ["Joshua 15:31", "Joshua 19:5", "1 Chronicles 4:31"],
        "intro": "<p>Sansannah was a town in the southern district of Judah (Josh. 15:31) that was subsequently allocated to the tribe of Simeon within Judah's territory (Josh. 19:5, where it appears as Hazar-susah, \"enclosure of the mare,\" and 1 Chr. 4:31 as Hazar-susim, \"enclosure of horses\"). The variation in names may suggest two distinct traditions preserving different characteristics of the site — one botanical (sansannah, meaning a branch or palm bough) and one relating to equestrian use (horse enclosure). The site lay in the Negev, the semi-arid southern zone of Judah. As with many Simeonite cities, Sansannah was situated within Judah's allotment due to the relatively small size of Simeon's territory, which was scattered among Judah's holdings (Josh. 19:1).</p>"
    },
    "saph": {
        "id": "saph", "term": "Saph", "category": "people",
        "hitchcock_meaning": "rushes; sea-moss",
        "source_ids": {"easton": "saph", "smith": "saph", "isbe": "saph"},
        "key_refs": ["2 Samuel 21:18", "1 Chronicles 20:4"],
        "intro": "<p>Saph (also called Sippai in 1 Chr. 20:4) was one of the last survivors of the Philistine giant clans, descended from the Rephaim. He was slain at Gob (or Gezer, as 1 Chr. 20:4 identifies the location) by Sibbechai the Hushathite, one of David's mighty warriors, during the wars against the Philistines in the later part of David's reign (2 Sam. 21:18). The account in 2 Samuel 21:15–22 records four encounters in which David's champions slew Philistine giants, apparently the last remnants of the ancient race of giant warriors. These victories brought an end to the threat from the giant-clans that had been a source of fear since Israel's first approach to Canaan (Num. 13:33; Deut. 1:28). Saph's death at the hands of Sibbechai is a brief but historically significant note marking the end of one of Israel's most formidable ancient adversaries.</p>"
    },
    "saphir": {
        "id": "saphir", "term": "Saphir", "category": "places",
        "hitchcock_meaning": "delightful",
        "source_ids": {"easton": "saphir", "smith": "saphir", "isbe": "saphir"},
        "key_refs": ["Micah 1:11"],
        "intro": "<p>Saphir (meaning <em>beautiful</em> or <em>delightful</em>) was a town of Judah mentioned once in Micah's lament over the coming Assyrian invasion (Mic. 1:11). The verse contains a wordplay on the town's name: \"Pass on your way, inhabitants of Saphir, in nakedness and shame\" — the town of <em>beauty</em> will be exposed in disgrace. This type of rhetorical wordplay on place-names runs throughout Micah 1:10–15, with each community's fate matching or ironically inverting its name. The site is tentatively identified with es-Suafir (or Sawafir), about five miles southeast of Ashdod on the coastal plain, in the Shephelah region. Saphir's inclusion in Micah's catalog of doomed Philistine and Judean cities places it in the path of the Assyrian advance under Sargon II and Sennacherib.</p>"
    },
    "sapphira": {
        "id": "sapphira", "term": "Sapphira", "category": "people",
        "hitchcock_meaning": "that relates or tells",
        "source_ids": {"easton": "sapphira", "smith": "sapphira", "isbe": "sapphira"},
        "key_refs": ["Acts 5:1", "Acts 5:3", "Acts 5:9", "Acts 5:11"],
        "intro": "<p>Sapphira (meaning <em>beautiful</em> in Aramaic) was the wife of Ananias who, together with her husband, sold a piece of property and brought part of the proceeds to the apostles while pretending to bring the full amount — a deliberate act of deception against the Holy Spirit and the apostolic community (Acts 5:1–11). The sin was not in keeping a portion of the sale but in lying about it, as Peter made clear: the property was theirs to keep or sell as they wished (Acts 5:4). Three hours after Ananias fell dead at Peter's word, Sapphira came in unaware of what had happened, confirmed the lie under questioning, and fell dead at the apostle's announcement of her complicity. The sudden deaths of both husband and wife produced great fear throughout the church and among all who heard. The episode, early in the Jerusalem church's history, served as a dramatic and sobering demonstration that the Holy Spirit's presence in the community was a holy and searching reality, not merely a spiritual concept.</p>"
    },
    "sapphire": {
        "id": "sapphire", "term": "Sapphire", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sapphire", "smith": "sapphire", "isbe": "sapphire"},
        "key_refs": ["Exodus 24:10", "Exodus 28:18", "Ezekiel 1:26", "Revelation 21:19"],
        "intro": "<p>Sapphire (Hebrew <em>sappir</em>; Greek <em>sappheiros</em>) was one of the twelve precious stones in the high priest's breastplate (Ex. 28:18; 39:11) and one of the foundational stones of the new Jerusalem (Rev. 21:19). In modern usage the sapphire is a blue variety of corundum, but the ancient Hebrew <em>sappir</em> most likely referred to lapis lazuli — a deep blue stone with gold flecks, widely used in ancient Mesopotamian and Egyptian decorative art. The vivid sky-blue of lapis lazuli makes it appropriate for the descriptions of God's throne: the elders saw under God's feet something like a pavement of sapphire, like the sky in clarity (Ex. 24:10), and Ezekiel saw the firmament above the living creatures as crystal with a throne above it like sapphire (Ezek. 1:26; 10:1). The sapphire is also listed among the gems adorning the prince of Tyre (Ezek. 28:13) and appears in both Job 28:6 and Isaiah 54:11–12 as a symbol of divine beauty and blessing.</p>"
    },
    "sarah": {
        "id": "sarah", "term": "Sarah", "category": "people",
        "hitchcock_meaning": "lady; princess; princess of the multitude",
        "source_ids": {"easton": "sarah", "smith": "sarah"},
        "key_refs": ["Genesis 17:15", "Genesis 21:2", "Galatians 4:22", "Hebrews 11:11"],
        "intro": "<p>Sarah (meaning <em>princess</em>; earlier name Sarai, <em>my princess</em>), the wife and half-sister of Abraham (Gen. 20:12), was renamed by God at the announcement that she would bear the promised son (Gen. 17:15–16). She was a woman of great beauty, twice imperiled by her husband's deception before foreign kings (Gen. 12:10–20; 20:1–18) in both cases miraculously protected by God's intervention. For decades she remained barren, eventually proposing that Abraham take her handmaid Hagar as a concubine — a decision that produced Ishmael and lasting family strife (Gen. 16). At age ninety she laughed at the divine announcement that she would bear a son (Gen. 18:12), and a year later gave birth to Isaac, the child of promise (Gen. 21:1–7). She died at age 127 at Hebron, the only woman in the Bible whose age at death is recorded, and was buried in the cave of Machpelah that Abraham purchased (Gen. 23). The New Testament holds her up as a model of faith (Heb. 11:11) and of the wifely submission that trusts in God (1 Pet. 3:6), and Paul uses her as the type of the covenant of grace (Gal. 4:22–26).</p>"
    },
    "sarai": {
        "id": "sarai", "term": "Sarai", "category": "people",
        "hitchcock_meaning": "my lady; my princess",
        "source_ids": {"easton": "sarai", "smith": "sarai"},
        "key_refs": ["Genesis 11:29", "Genesis 11:31", "Genesis 17:15"],
        "intro": "<p>Sarai was the original name of Sarah, the wife of Abram (Gen. 11:29). The name means <em>my princess</em> — a personal, possessive form of the word for princess or noblewoman. She accompanied Abram from Ur of the Chaldeans and then from Haran when God called him to leave his country and kindred (Gen. 11:31; 12:1–5). At the time of the covenant of circumcision and the divine promise that she would become the mother of nations, God changed her name from Sarai to Sarah — dropping the possessive suffix, making her name simply <em>princess</em> in a more universal sense befitting the mother of the covenant nation (Gen. 17:15). The change in name, given alongside the new name Abram received (Abraham), marked the transformation of both their identities in relation to the divine promise. Thus Sarai appears in the earliest chapters of her story (Gen. 11–17), while Sarah is the name used from the covenant confirmation onward.</p>"
    },
    "sardine-stone": {
        "id": "sardine-stone", "term": "Sardine stone", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sardine-stone"},
        "key_refs": ["Revelation 4:3", "Exodus 28:17", "Exodus 39:10"],
        "intro": "<p>The sardine stone (also sardius; Hebrew <em>'odhem</em>, from a root meaning <em>red</em>; Greek <em>sardios</em> or <em>sardion</em>) was a blood-red or reddish-brown gem corresponding to what we know today as red carnelian or sard — a variety of chalcedony ranging from dark orange to brownish-red. It was named for Sardis in Lydia, a city famous for producing this stone. The sardine was the first stone in the first row of the high priest's breastplate (Ex. 28:17; 39:10), representing the tribe of Reuben according to most traditional identifications. In the apocalyptic vision of Revelation 4:3, the one seated on the heavenly throne appeared like jasper and a sardine (sardius) stone, the two gems together conveying resplendent divine glory. The sardius is also listed among the precious stones adorning the king of Tyre in Ezekiel 28:13, and it forms one of the twelve foundational stones of the new Jerusalem in Revelation 21:20.</p>"
    },
    "sardis": {
        "id": "sardis", "term": "Sardis", "category": "places",
        "hitchcock_meaning": "prince of joy",
        "source_ids": {"easton": "sardis", "smith": "sardis", "isbe": "sardis"},
        "key_refs": ["Revelation 3:1", "Revelation 3:4"],
        "intro": "<p>Sardis was the ancient capital of the Lydian kingdom and one of the great cities of Asia Minor, situated in the Hermus valley at the foot of Mount Tmolus, about 50 miles east of Smyrna and 30 miles south of Thyatira. In its golden age under King Croesus (sixth century BC), Sardis was one of the wealthiest cities in the world; the nearby Pactolus River deposited electrum (a gold-silver alloy) that funded its legendary riches. The city fell to the Persian Cyrus in 547 BC through a surprise attack that became proverbial for overconfidence. In the New Testament, Sardis was one of the seven churches addressed in Revelation (Rev. 3:1–6). The letter to Sardis contains the most severe assessment of any of the seven churches: \"You have a name that you are alive, and you are dead.\" The church was called to wake up, strengthen what remains, and repent — language that may echo the city's own historical reputation for falling through sleepy overconfidence. The ruins of Sardis, now called Sert-Kalessi, include impressive remains of a temple to Artemis.</p>"
    },
    "sardonyx": {
        "id": "sardonyx", "term": "Sardonyx", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sardonyx", "smith": "sardonyx", "isbe": "sardonyx"},
        "key_refs": ["Revelation 21:20"],
        "intro": "<p>Sardonyx (Greek <em>sardonyx</em>, combining <em>sardion</em> and <em>onyx</em>) is a banded gemstone consisting of layers of sard (reddish-brown chalcedony) and onyx (black or white chalcedony), producing a stone with alternate bands of red/brown and white or black. In classical antiquity it was highly prized for cameo carving, as the contrasting layers allowed craftsmen to carve figures in one layer against a background of another color. It appears in the Bible only in Revelation 21:20 as the fifth of the twelve foundation stones of the new Jerusalem. The precious stones listed in Revelation 21:19–20 collectively evoke the richest materials known to the ancient world, representing the eternal glory and perfection of the city of God. The sardonyx's combination of warm red and bright white also carries symbolic resonance with the blood of Christ and the purity of the saints.</p>"
    },
    "sarepta": {
        "id": "sarepta", "term": "Sarepta", "category": "places",
        "hitchcock_meaning": "a goldsmith's shop",
        "source_ids": {"easton": "sarepta", "smith": "sarepta", "isbe": "sarepta"},
        "key_refs": ["Luke 4:26", "1 Kings 17:9", "1 Kings 17:24"],
        "intro": "<p>Sarepta (also Zarephath; Greek <em>Sarepta</em>) was a Phoenician town on the Mediterranean coast between Tyre and Sidon, approximately eight miles south of Sidon. It is famous as the place where the prophet Elijah was directed during the three-and-a-half-year drought, finding shelter and sustenance with a Gentile widow who shared her last flour and oil with him and was miraculously provided for throughout the famine (1 Kings 17:9–24). Elijah also raised her son from death at Zarephath. Jesus cited this episode in his synagogue sermon at Nazareth (Luke 4:26) to demonstrate that divine grace extended to Gentiles when Israel was faithless: though there were many widows in Israel during Elijah's time, he was sent to none of them but to this foreign woman in Sidon. The episode became a paradigm for the inclusion of Gentiles in God's redemptive purposes. The modern site is the village of Sarafand on the Lebanese coast.</p>"
    },
    "sargon": {
        "id": "sargon", "term": "Sargon", "category": "people",
        "hitchcock_meaning": "who takes away protection",
        "source_ids": {"easton": "sargon", "smith": "sargon", "isbe": "sargon"},
        "key_refs": ["Isaiah 20:1", "2 Kings 17:6", "2 Kings 18:9"],
        "intro": "<p>Sargon II (reigned 722–705 BC) was the Assyrian king who completed the conquest of Samaria and the deportation of the northern kingdom of Israel. His name (<em>Sharru-kinu</em>, meaning <em>the legitimate king</em>) echoes the famous Sargon of Akkad, founder of the first Semitic empire. When his predecessor Shalmaneser V died during the siege of Samaria (2 Kings 17:3–6), Sargon took the throne and completed the city's fall in 722/721 BC, deporting approximately 27,290 Israelites (according to his own annals) and resettling the region with peoples from Babylon, Cuthah, and other subject territories. He is mentioned by name only once in Scripture, in Isaiah 20:1, where he is identified as the Assyrian king who sent his commander against the Philistine city of Ashdod. His great palace at Khorsabad, excavated beginning in 1843, confirmed his biblical identification after centuries of uncertainty about his historicity.</p>"
    },
    "satan": {
        "id": "satan", "term": "Satan", "category": "concepts",
        "hitchcock_meaning": "contrary; adversary; enemy; accuser",
        "source_ids": {"easton": "satan", "smith": "satan", "isbe": "satan"},
        "key_refs": ["Job 1:6", "Matthew 4:1", "Revelation 12:9", "Revelation 20:10"],
        "intro": "<p>Satan (Hebrew <em>satan</em>, adversary or accuser; Greek <em>diabolos</em>, the devil, slanderer) is the primary spiritual opponent of God and humanity in biblical theology. In the Old Testament he appears as a member of the divine council who serves as prosecutor or accuser — most fully developed in Job 1–2, where he challenges the integrity of Job's faith and is permitted to afflict him within limits set by God. By the New Testament, Satan is presented in more developed terms as the personal ruler of a kingdom of darkness (Eph. 6:12; Col. 1:13), \"the prince of this world\" (John 12:31), and \"the god of this age\" (2 Cor. 4:4) who blinds unbelievers. He tempted Jesus in the wilderness (Matt. 4:1–11), entered Judas Iscariot (Luke 22:3), and seeks to devour believers (1 Pet. 5:8). His ultimate doom is sealed: he was defeated by Christ's death and resurrection (John 12:31; Col. 2:15), is bound during Christ's reign, and will be finally cast into the lake of fire at the end of history (Rev. 20:10). He is identified with the ancient serpent of Genesis 3 (Rev. 12:9; 20:2).</p>"
    },
    "satyr": {
        "id": "satyr", "term": "Satyr", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "satyr", "smith": "satyr", "isbe": "satyr"},
        "key_refs": ["Isaiah 13:21", "Isaiah 34:14", "Leviticus 17:7", "2 Chronicles 11:15"],
        "intro": "<p>The satyr in Hebrew (sa'ir, literally <em>hairy one</em> or <em>goat</em>) refers to a class of demonic or supernatural goat-like creatures associated with desolate, wild places. The same Hebrew word is translated \"goat\" (Lev. 4:24), \"devil\" in the sense of an idol in the form of a goat (Lev. 17:7; 2 Chr. 11:15 — where Jeroboam appointed priests to serve the satyrs alongside the golden calves), and \"satyr\" in prophetic poetry. Isaiah uses the image of satyrs dancing in the ruins of Babylon (Isa. 13:21) and Edom (Isa. 34:14) to picture the desolation of divine judgment: where human civilization stood, only wild creatures of the desert — including these half-mythic beings — will remain. The concept reflects the ancient Near Eastern belief that ruins and waste places were haunted by malevolent spirits or creatures. Leviticus 17:7 explicitly prohibited Israel from sacrificing to the satyrs after whom they lusted, condemning what appears to have been an existing practice of goat-demon worship.</p>"
    },
    "saul": {
        "id": "saul", "term": "Saul", "category": "people",
        "hitchcock_meaning": "demanded; lent; ditch; death",
        "source_ids": {"easton": "saul", "smith": "saul", "isbe": "saul"},
        "key_refs": ["1 Samuel 9:2", "1 Samuel 10:24", "1 Samuel 15:23", "1 Samuel 31:4"],
        "intro": "<p>Saul, son of Kish of the tribe of Benjamin, was the first king of Israel, anointed by Samuel at God's direction when the people demanded a king to be like the nations (1 Sam. 8–10). He was physically imposing — head and shoulders above all the people (1 Sam. 9:2) — and his early kingship showed promise: he delivered Jabesh-gilead from the Ammonites (1 Sam. 11) and won notable victories over the Philistines. But his reign was tragically undermined by two acts of disobedience: he presumed to offer sacrifice instead of waiting for Samuel (1 Sam. 13:8–14), and he failed to carry out God's command to utterly destroy the Amalekites, sparing King Agag and the best livestock (1 Sam. 15). Samuel's verdict was definitive: \"Because you have rejected the word of the LORD, he has also rejected you from being king\" (1 Sam. 15:23). An evil spirit replaced the Spirit of the LORD upon him, producing bouts of torment that David's harp-playing temporarily relieved. His increasingly erratic behavior — including multiple attempts to kill David, a massacre of the priests at Nob (1 Sam. 22), and a consultation of the witch of Endor (1 Sam. 28) — marked his decline. He died in the battle of Mount Gilboa, falling on his own sword rather than suffer capture by the Philistines (1 Sam. 31:4).</p>"
    },
    "saviour": {
        "id": "saviour", "term": "Saviour", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "saviour", "isbe": "saviour"},
        "key_refs": ["Isaiah 43:3", "Luke 2:11", "John 4:42", "1 Timothy 4:10"],
        "intro": "<p>Saviour (Hebrew <em>moshia'</em>; Greek <em>soter</em>) designates one who delivers from danger, evil, or destruction. In the Old Testament, God himself is repeatedly called the Saviour of Israel (Isa. 43:3, 11; 45:15, 21; Ps. 106:21), the one who rescued the nation from Egypt and its enemies. Human deliverers — particularly the judges — also bore this title (Judg. 3:9, 15; Neh. 9:27). In the New Testament, <em>Soter</em> is applied both to God the Father (Luke 1:47; 1 Tim. 1:1; Jude 25) and preeminently to Jesus Christ, whose very name means <em>Yahweh saves</em> (Matt. 1:21). The angel at Bethlehem proclaimed him \"a Saviour, who is Christ the Lord\" (Luke 2:11), and the Samaritans confessed him \"the Saviour of the world\" (John 4:42). Paul develops the title in the Pastoral Epistles and Titus, where the appearing of \"our great God and Saviour Jesus Christ\" (Titus 2:13) anticipates the completion of salvation at his second coming. The title encompasses deliverance from sin's guilt (justification), its power (sanctification), and its presence (glorification).</p>"
    },
    "scapegoat": {
        "id": "scapegoat", "term": "Scapegoat", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "scapegoat", "smith": "scapegoat"},
        "key_refs": ["Leviticus 16:8", "Leviticus 16:21", "Leviticus 16:22"],
        "intro": "<p>The scapegoat was one of two male goats selected for the annual Day of Atonement ritual prescribed in Leviticus 16. Aaron cast lots over the two goats: one was offered as a sin offering for the LORD, and the other — designated \"for Azazel\" (Lev. 16:8, RV) — was the scapegoat. The high priest confessed all the iniquities of the Israelites over the live goat, laying his hands on its head and symbolically transferring the nation's sins to it, then sent it away into the wilderness to a desolate land (Lev. 16:20–22). This goat \"bore upon him all their iniquities\" and carried them away so they would no longer be present in the camp. The term \"Azazel\" is variously interpreted as a proper name for a demon inhabiting the desert, a place name (a precipice), or a descriptive word meaning <em>removal</em>. The two goats together dramatized two aspects of atonement: propitiation (the sacrificed goat) and removal of sin (the scapegoat). The English word \"scapegoat\" — meaning one who bears blame for others — derives directly from this text.</p>"
    },
    "scarlet": {
        "id": "scarlet", "term": "Scarlet", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "scarlet", "smith": "scarlet", "isbe": "scarlet"},
        "key_refs": ["Exodus 28:6", "Joshua 2:18", "Isaiah 1:18", "Revelation 17:4"],
        "intro": "<p>Scarlet in the Old Testament (Hebrew <em>shani</em> and <em>tola'at shani</em>, literally <em>crimson of the worm</em>) was a bright red dye obtained from the dried body of the female Coccus ilicis, a scale insect (<em>kermes</em>) living on oak trees in Palestine and the Mediterranean basin. The color was among the earliest and most prized dyes known to the ancient world (Gen. 38:28). Scarlet thread, yarn, and fabric were prescribed ingredients of the tabernacle curtains and hangings (Ex. 26:1, 31, 36) and elements of the high priest's vestments (Ex. 28:6, 8, 15, 33). Rahab's red cord hung from her window served as the signal for Israel's spies (Josh. 2:18), a detail given typological significance in early Christian interpretation as a figure of redemption by blood. Isaiah 1:18 uses scarlet and crimson as images of the depth of sin: \"Though your sins are like scarlet, they shall be as white as snow.\" In Revelation, the great harlot is arrayed in purple and scarlet (Rev. 17:4), evoking wealth and bloodshed.</p>"
    },
    "sceptre": {
        "id": "sceptre", "term": "Sceptre", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sceptre", "smith": "sceptre"},
        "key_refs": ["Genesis 49:10", "Numbers 24:17", "Psalms 45:6", "Hebrews 1:8"],
        "intro": "<p>The sceptre (Hebrew <em>shebet</em>, a staff or rod; Greek <em>skeptron</em>) was the symbol of royal authority in the ancient Near East — a staff or wand held by the ruler as an emblem of sovereign power. In biblical usage, the sceptre is closely connected with the concept of kingship and its transfer. Jacob's blessing prophesied that \"the sceptre shall not depart from Judah\" until Shiloh comes (Gen. 49:10), a messianic prophecy pointing to the perpetual royal line of Judah and its culmination in the Messiah. Balaam's oracle spoke of \"a sceptre\" rising from Israel (Num. 24:17). In the Persian court, Ahasuerus extended his golden sceptre to Esther as a gesture permitting her to approach him without death (Esther 4:11; 5:2–3). Psalm 45:6 — quoted in Hebrews 1:8 and applied to Christ — declares: \"Your throne, O God, is forever and ever; the sceptre of your kingdom is a sceptre of uprightness.\" The sceptre thus becomes a symbol of Christ's eternal and righteous reign.</p>"
    },
    "sceva": {
        "id": "sceva", "term": "Sceva", "category": "people",
        "hitchcock_meaning": "disposed; prepared",
        "source_ids": {"easton": "sceva", "smith": "sceva", "isbe": "sceva"},
        "key_refs": ["Acts 19:13", "Acts 19:14", "Acts 19:16"],
        "intro": "<p>Sceva was a Jew described as a \"chief priest\" at Ephesus whose seven sons attempted to cast out evil spirits by invoking the name of Jesus during Paul's ministry in that city (Acts 19:13–16). The episode is among the most dramatic in Acts: the demon-possessed man attacked all seven sons, overpowered them, and left them fleeing the house naked and wounded. Sceva's title \"chief priest\" (<em>archiereus</em>) is puzzling, as Ephesus had no Jewish high priestly office; it may mean he was the head of one of the twenty-four priestly courses, or that he claimed a priestly dignity to lend authority to his sons' exorcistic activities. The sons' failure with the unauthorized use of Jesus' name stands in sharp contrast to Paul's successful ministry, and the episode caused widespread fear and brought many Ephesian believers to confess and burn their books of magic (Acts 19:17–19). It illustrates that the divine power in Jesus' name cannot be mechanically appropriated without true faith and calling.</p>"
    },
    "schism": {
        "id": "schism", "term": "Schism", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "schism", "isbe": "schism"},
        "key_refs": ["1 Corinthians 12:25", "1 Corinthians 1:10", "John 17:21"],
        "intro": "<p>Schism (Greek <em>schisma</em>, a split or tear) refers to a division or separation within the body of Christ that disrupts the unity of the church. In the New Testament the word appears most explicitly in 1 Corinthians 12:25, where Paul states that God has designed the body so that \"there may be no schism in the body, but that the members may have the same care for one another.\" The word also appears in 1 Corinthians 1:10, where Paul urges the Corinthians to be united in mind and judgment and avoid divisions — addressing the factional partisanship that had developed around different apostolic teachers. Jesus' high-priestly prayer in John 17 establishes unity as central to the church's witness: the world will know Christ was sent from God by the observable love and unity of his followers (John 17:21–23). Theologically, schism is distinguished from heresy (false doctrine) in that it involves breaking fellowship over matters of secondary importance, discipline, or personal loyalty rather than fundamental doctrinal error, though in practice the two frequently occur together.</p>"
    },
    "schoolmaster": {
        "id": "schoolmaster", "term": "Schoolmaster", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "schoolmaster", "isbe": "schoolmaster"},
        "key_refs": ["Galatians 3:24", "Galatians 3:25"],
        "intro": "<p>Schoolmaster is the Authorized Version's rendering of the Greek <em>paidagogos</em> in Galatians 3:24–25 — a term Paul uses to describe the role of the Mosaic law in the history of redemption. The <em>paidagogos</em> in the Greco-Roman world was not a teacher but a slave or trusted servant who was responsible for the supervision, discipline, and safe conduct of a minor child, accompanying him to school, overseeing his behavior, and enforcing rules of conduct. Paul's argument is that the law functioned as this supervising guardian over Israel in its spiritual minority, keeping the people under discipline and revealing sin's seriousness — not to save, but to lead them to Christ, in whom justification by faith became available. The arrival of faith in Christ brought the period under the <em>paidagogos</em> to an end: believers in Christ are no longer under this supervisory guardian but are full adult sons of God through faith (Gal. 3:25–26; 4:1–7). Modern translations render <em>paidagogos</em> as \"guardian,\" \"tutor,\" or \"disciplinarian.\"</p>"
    },
    "schools-of-the-prophets": {
        "id": "schools-of-the-prophets", "term": "Schools of the Prophets", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "schools-of-the-prophets", "isbe": "schools-of-the-prophets"},
        "key_refs": ["1 Samuel 19:18", "2 Kings 2:3", "2 Kings 2:5", "2 Kings 6:1"],
        "intro": "<p>The schools of the prophets were communities of prophetic apprentices or disciples organized in the period of Samuel, Elijah, and Elisha for the purpose of training young men for prophetic and priestly service. The first such gathering appears in 1 Samuel 19:18–24, where a company of prophets at Naioth in Ramah prophesied under Samuel's leadership, drawing in Saul's messengers and eventually Saul himself. By Elijah's time, established companies of \"sons of the prophets\" were located at Bethel, Jericho, and Gilgal (2 Kings 2:3, 5; 4:38; 6:1). Elisha became the dominant leader of these communities after Elijah's translation, performing miracles on their behalf and instructing them. The communities appear to have been residential, as 2 Kings 6:1–2 records the sons of the prophets seeking to build larger quarters at the Jordan. Their activities included communal worship, prophetic utterance, and transmission of the prophetic tradition. They represent an early form of organized religious education and prophetic guilds in ancient Israel.</p>"
    },
    "scorpions": {
        "id": "scorpions", "term": "Scorpions", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "scorpions"},
        "key_refs": ["Deuteronomy 8:15", "Luke 10:19", "Revelation 9:3", "1 Kings 12:11"],
        "intro": "<p>Scorpions (Hebrew <em>'aqrab</em>; Greek <em>skorpios</em>) were common venomous arachnids of the hot, rocky wilderness regions of the ancient Near East, well known to every Israelite and particularly associated with the Sinai wilderness. They are mentioned alongside serpents as characteristic dangers of the desert through which God led Israel (Deut. 8:15). The scorpion's painful sting was proverbial for severe pain, making it an apt image for cruel punishment: Rehoboam's boast that his discipline would be with scorpions rather than whips (1 Kings 12:11, 14) was a threat of intensified harshness. Jesus gave his disciples authority to tread on scorpions and serpents without harm (Luke 10:19), symbolizing power over all spiritual enemies. In the apocalyptic vision of Revelation 9:3–10, demonic locusts are given power like that of scorpions — authorized to torment but not to kill, for five months — one of the most vivid images of spiritual judgment in the New Testament.</p>"
    },
    "scourging": {
        "id": "scourging", "term": "Scourging", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "scourging", "smith": "scourging"},
        "key_refs": ["Deuteronomy 25:3", "2 Corinthians 11:24", "Matthew 27:26", "Hebrews 12:6"],
        "intro": "<p>Scourging was the practice of flogging with a rod, strap, or multi-thonged whip as a judicial punishment. The Mosaic law regulated flogging, limiting it to a maximum of forty stripes for any offense (Deut. 25:3), a number the Jews customarily reduced to thirty-nine as a safeguard against accidental exceeding of the limit (2 Cor. 11:24 — Paul received the thirty-nine stripes five times from Jewish authorities). Roman scourging (<em>verberatio</em> or <em>flagellatio</em>) was far more severe, using a whip of leather thongs weighted with bone or metal fragments (<em>flagrum</em>) that could tear flesh to the bone, and had no legal maximum. Roman scourging frequently preceded crucifixion: Jesus was scourged by Pilate's soldiers (Matt. 27:26; Mark 15:15; John 19:1) as part of the crucifixion proceedings. Roman citizenship offered protection from scourging (Acts 22:25–29). The New Testament also uses scourging metaphorically for divine discipline: God scourges every son he receives, treating them as legitimate children (Heb. 12:6, quoting Prov. 3:12).</p>"
    },
    "scribes": {
        "id": "scribes", "term": "Scribes", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "scribes", "smith": "scribes", "isbe": "scribes"},
        "key_refs": ["Ezra 7:6", "Matthew 23:2", "Mark 1:22", "Matthew 5:20"],
        "intro": "<p>The scribes (Hebrew <em>soferim</em>, writers; Greek <em>grammateis</em>) were a professional class of learned men who began as secretaries and copyists of state documents but evolved into the authoritative interpreters of the Mosaic law. In the pre-exilic period they served as royal secretaries and military officers (2 Sam. 8:17; 2 Kings 12:10). Ezra the scribe represents the transition: he was \"a skilled scribe in the Law of Moses\" (Ezra 7:6) who devoted himself to studying, observing, and teaching the law (Ezra 7:10). In the post-exilic and Second Temple period, the scribes became the professional class responsible for copying and expounding Scripture, developing the oral tradition (Mishnah) that the Pharisees elevated alongside the written law. In the New Testament, scribes are frequently paired with Pharisees (Matt. 5:20; 23:2) as the religious establishment opposing Jesus. His authority astonished the crowds because he taught <em>as one who had authority, not as their scribes</em> (Matt. 7:29; Mark 1:22) — speaking in his own name rather than citing tradition.</p>"
    },
    "scrip": {
        "id": "scrip", "term": "Scrip", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "scrip", "smith": "scrip", "isbe": "scrip"},
        "key_refs": ["1 Samuel 17:40", "Matthew 10:10", "Mark 6:8", "Luke 9:3"],
        "intro": "<p>Scrip was a small bag or wallet, typically made of leather or rough material, carried by travelers, shepherds, and soldiers fastened to the belt or slung over the shoulder. In 1 Samuel 17:40, David put five smooth stones in his shepherd's bag (scrip) when he went to face Goliath. In the New Testament the Greek word <em>pera</em> — rendered scrip in the Authorized Version — refers to a traveler's bag used to carry provisions or personal items. Jesus instructed the Twelve and the Seventy in their missionary charges not to take a scrip, along with staff, bread, money, or extra clothes (Matt. 10:9–10; Mark 6:8; Luke 9:3; 10:4) — a directive to trust entirely in the hospitality and provision of those who received them, symbolizing dependence on God rather than self-sufficiency. In contrast, just before his arrest Jesus told the disciples that those who had a purse or scrip should take it, indicating a change from the earlier conditions of protected itinerant mission (Luke 22:36).</p>"
    },
}


def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        article = {
            "id": slug,
            "term": data["term"],
            "category": data["category"],
            "intro": data["intro"],
            "hitchcock_meaning": data.get("hitchcock_meaning"),
            "source_ids": data.get("source_ids", {}),
            "key_refs": data.get("key_refs", []),
            "sections": []
        }
        if merge_article(slug, article):
            written += 1
        else:
            skipped += 1
    print(f"BP s1: Sabachthani → Scrip: wrote {written}, skipped {skipped} existing.")


if __name__ == "__main__":
    main()
