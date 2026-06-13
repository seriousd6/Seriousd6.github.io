"""
BP Article Synthesis — l2: Litter → Lystra
Covers Easton entries: Litter through Lystra (41 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Category logic applied:
  - people:   Hitchcock match + no major place signals in brief
  - places:   brief/title contains 'city', 'town', 'province', 'mount', 'valley', etc.
  - concepts: no Hitchcock match, no place signals
  - names:    Hitchcock-only (no Easton/Smith entry)

Script: scripts/bp-l2.py
Run: python3 scripts/bp-l2.py
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
    "litter": {
        "id": "litter",
        "term": "Litter",
        "category": "concepts",
        "intro": "<p>Litter (Hebrew <em>tsab</em>, meaning something lightly and gently borne) denotes a sedan chair or palanquin—an enclosed portable vehicle carried on poles by bearers—used to convey persons of rank in the ancient Near East. Numbers 7:3 uses the term for the wagons (or litters) offered by the princes of Israel as transport for the tabernacle furnishings, though the NRSV and most modern versions translate it as <em>covered wagons</em>. Isaiah 66:20 anticipates the gathering of dispersed Israel to Jerusalem in <em>litters</em> alongside horses, chariots, mules, and swift beasts—a picture of the nations as attendants bringing God's people home in honor.</p><p>The litter or palanquin was a luxury conveyance in the ancient world, contrasted with riding on horseback or walking. The Song of Solomon 3:7–10 describes Solomon's ornate palanquin (<em>appiryon</em>) made of cedar, silver, gold, and purple—probably the same form of vehicle. Such conveyances were common throughout the ancient Near East and are attested in Egyptian and Mesopotamian art as the transport of royalty and high officials.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "litter", "isbe": "litter"},
        "key_refs": ["Numbers 7:3", "Isaiah 66:20"]
    },
    "liver": {
        "id": "liver",
        "term": "Liver",
        "category": "concepts",
        "intro": "<p>Liver (Hebrew <em>kabhed</em>, meaning <em>heavy</em>—as the heaviest of the viscera) plays a significant role in Israelite sacrificial law and in the broader ancient Near Eastern context. In the ritual instructions for burnt offerings and peace offerings, the <em>caul</em> or fatty lobe above the liver, along with the two kidneys, was designated as the portion to be burned on the altar for God (Ex. 29:13, 22; Lev. 3:4, 10, 15; 4:9; 7:4). This practice separated Israel's sacrifice from pagan use of the liver: among Babylonians and other ancient peoples, the liver was the seat of divination (<em>hepatoscopy</em>), with the organ examined for omens before battles and major decisions.</p><p>Ezekiel 21:21 records Nebuchadnezzar at a crossroads consulting three oracles—casting lots, reading livers, and consulting household idols—to determine whether to march against Jerusalem or Rabbah. The biblical prohibition of divination (Deut. 18:10–12) explicitly banned such practices in Israel. The liver's dedication to God in sacrifice thus represented both an act of worship and a deliberate rejection of its pagan divinatory function.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "liver", "isbe": "liver"},
        "key_refs": ["Exodus 29:13", "Leviticus 3:4", "Ezekiel 21:21"]
    },
    "living-creatures": {
        "id": "living-creatures",
        "term": "Living Creatures",
        "category": "concepts",
        "intro": "<p>Living creatures (<em>hayyoth</em> in Hebrew, <em>zoa</em> in Greek) designate the extraordinary celestial beings described in Ezekiel's inaugural vision (Ezek. 1; 10) and in John's vision of the heavenly throne room (Rev. 4–5). In Ezekiel, four living creatures each have four faces—of a man, lion, ox, and eagle—four wings, and gleaming bronze feet; they accompany the divine chariot-throne (<em>merkabah</em>) and are identified later in the book as cherubim (Ezek. 10:15). The prophet Isaiah's seraphim (Isa. 6:2–3) are closely related, similarly crying <em>Holy, holy, holy is the LORD of hosts.</em></p><p>In Revelation 4:6–9, four living creatures surround the throne of God, resembling a lion, an ox, a man, and a flying eagle respectively. They lead the heavenly worship—<em>Holy, holy, holy, is the Lord God Almighty, who was and is and is to come</em>—and participate in the seal and trumpet judgments (Rev. 5–8) and the bowl judgments (Rev. 15:7). Christian tradition from Irenaeus onward identified the four faces with the four Evangelists (Matthew, Mark, Luke, John), though the primary significance of the living creatures is as angelic attendants of the divine throne reflecting God's sovereign majesty over all creation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "living-creatures", "isbe": "living-creatures"},
        "key_refs": ["Revelation 4:6", "Revelation 15:7", "Ezekiel 1:5", "Isaiah 6:3"]
    },
    "lizard": {
        "id": "lizard",
        "term": "Lizard",
        "category": "concepts",
        "intro": "<p>Lizard appears in Scripture in the Mosaic purity laws governing unclean creeping things. Leviticus 11:30 lists the <em>letaah</em> (lizard) as one of the eight unclean reptiles—alongside the gecko, land crocodile, sand lizard, and chameleon—contact with whose carcass rendered a person ceremonially unclean until evening. The Authorized Version uses <em>lizard</em> for the Hebrew <em>letaah</em>, a word derived from a root meaning <em>to hide</em>, appropriate to the lizard's habit of concealing itself.</p><p>The identification of the specific reptiles in Leviticus 11:29–30 is uncertain, as the Hebrew terms do not map neatly onto modern zoological classification. Palestine hosts a diverse lizard fauna, including geckos, agamas, skinks, and monitor lizards, any of which might correspond to the listed terms. The general category of lizards (order Squamata) was included among the <em>swarming things</em> that defiled by touch under the Mosaic law, reflecting the Levitical system's concern with maintaining boundaries between the clean and unclean in daily Israelite life.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lizard", "smith": "lizard", "isbe": "lizard"},
        "key_refs": ["Leviticus 11:30"]
    },
    "lo-ammi": {
        "id": "lo-ammi",
        "term": "Lo-ammi",
        "category": "concepts",
        "intro": "<p>Lo-ammi (Hebrew, meaning <em>not my people</em>) was the symbolical name given by divine command to Hosea's third child by Gomer (Hos. 1:9). The name encapsulated God's declaration of covenantal rupture: <em>for ye are not my people, and I will not be your God.</em> This was the starkest of the three symbolic names Hosea gave his children—all three together (Jezreel, Lo-ruhamah, Lo-ammi) announced judgment upon the northern kingdom of Israel for its spiritual adultery through Baal worship and political instability.</p><p>Lo-ammi's theological significance extends far beyond its immediate context. Hosea 1:10 and 2:23 immediately promise a reversal: <em>In the place where it was said to them, 'You are not my people,' it shall be said to them, 'Children of the living God.'</em> Paul quotes this promise in Romans 9:25–26 and applies it to the calling of the Gentiles—those who were <em>not my people</em> becoming recipients of God's grace in Christ. Peter similarly cites Hosea in 1 Peter 2:10. The Lo-ammi oracle thus becomes in the New Testament one of the foundational prophecies for the inclusion of the nations in the covenant people of God.</p>",
        "hitchcock_meaning": "not my people",
        "source_ids": {"easton": "lo-ammi", "isbe": "lo-ammi"},
        "key_refs": ["Hosea 1:9", "Hosea 2:23", "Romans 9:25", "1 Peter 2:10"]
    },
    "lo-debar": {
        "id": "lo-debar",
        "term": "Lo-debar",
        "category": "places",
        "intro": "<p>Lo-debar (meaning <em>no pasture</em> or <em>without word</em>) was a town in the territory of Gilead in Transjordan, not far from Mahanaim, north of the Jabbok River. It appears twice in the narrative of David's reign. First, it was the location where Mephibosheth, the crippled son of Jonathan, lived in obscurity in the house of Machir son of Ammiel (2 Sam. 9:4–5) until David sent for him to honor his covenant with Jonathan. Second, Machir of Lo-debar was among those who brought provisions—beds, basins, earthen vessels, wheat, barley, flour, parched grain, beans, lentils, honey, curds, and sheep—to David and his followers when they had fled across the Jordan during Absalom's rebellion (2 Sam. 17:27–29).</p><p>Lo-debar illustrates both the geographical scope of the Davidic kingdom's Transjordanian connections and the human drama of loyal subjects during the crisis of Absalom's coup. The name's meaning—<em>no pasture</em>—stands in ironic contrast to the provision its townspeople supplied to a king in exile. It may be identified with Debir (Josh. 13:26).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lo-debar", "isbe": "lo-debar"},
        "key_refs": ["2 Samuel 9:4", "2 Samuel 17:27"]
    },
    "lo-ruhamah": {
        "id": "lo-ruhamah",
        "term": "Lo-ruhamah",
        "category": "concepts",
        "intro": "<p>Lo-ruhamah (Hebrew, meaning <em>not having obtained mercy</em> or <em>not pitied</em>) was the symbolic name given to Hosea's daughter by divine command (Hos. 1:6). The name expressed God's withdrawal of compassion from the northern kingdom of Israel: <em>I will no more have mercy upon the house of Israel; but I will utterly take them away.</em> Together with her brothers Jezreel and Lo-ammi, the three children of Hosea's troubled marriage to Gomer constituted a living prophetic sign to Israel of the consequences of spiritual unfaithfulness.</p><p>Like Lo-ammi, Lo-ruhamah's name is reversed in the subsequent promise of restoration: <em>I will have mercy upon her that had not obtained mercy</em> (Hos. 2:23). Paul quotes this reversal in Romans 9:25–26 alongside Lo-ammi as Old Testament warrant for the unexpected inclusion of Gentiles in the people of God. Peter echoes the same language in 1 Peter 2:10, telling his readers: <em>who once were not a people but now are God's people; who had not received mercy but now have received mercy.</em> The name Lo-ruhamah thus belongs to the prophetic vocabulary of divine grace that the New Testament applies to the new covenant community.</p>",
        "hitchcock_meaning": "not having obtained mercy; not pitied",
        "source_ids": {"easton": "lo-ruhamah", "isbe": "lo-ruhamah"},
        "key_refs": ["Hosea 1:6", "Hosea 2:23", "Romans 9:25", "1 Peter 2:10"]
    },
    "loan": {
        "id": "loan",
        "term": "Loan",
        "category": "concepts",
        "intro": "<p>Loan in the Mosaic law was governed by principles of fraternal generosity rather than commercial profit. Israelites were required to lend freely to their poor neighbors without charging interest (<em>neshek</em>, literally <em>a bite</em>): <em>Thou shalt not lend upon usury to thy brother; usury of money, usury of victuals, usury of any thing that is lent upon usury</em> (Deut. 23:19). Exodus 22:25 extends this: <em>If thou lend money to any of my people that is poor by thee, thou shalt not be to him as an usurer, neither shalt thou lay upon him usury.</em> Interest could be charged to foreigners but not to fellow Israelites, establishing a two-tier system that emphasized covenant solidarity over market principles.</p><p>Loans in ancient Israel were also subject to the sabbatical year: every seventh year all debts between Israelites were to be released, preventing the permanent entrenchment of poverty through debt (Deut. 15:1–11). Moses warns against the temptation to refuse loans as the sabbatical year approached (Deut. 15:9). Jesus directly alludes to this tradition in the Sermon on the Mount, commanding his followers to lend without expecting return (Luke 6:35) and to give to all who ask (Matt. 5:42)—extending the Mosaic principle of fraternal generosity beyond ethnic and religious boundaries.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "loan", "smith": "loan", "isbe": "loan"},
        "key_refs": ["Exodus 22:25", "Deuteronomy 23:19", "Deuteronomy 15:9", "Luke 6:35"]
    },
    "lock": {
        "id": "lock",
        "term": "Lock",
        "category": "concepts",
        "intro": "<p>Locks in the ancient world typically consisted of wooden bars or bolts that secured doors from within. The most common mechanism in Palestine and throughout the Near East was a heavy wooden bar that slid across the door into brackets on the door frame (Isa. 45:2; 1 Kings 4:13; Neh. 3:3, 6, 13). A more sophisticated form—the pin tumbler lock—was also used, in which a bar was fitted with holes that could only be lifted by a corresponding wooden key inserted through a hole in the door from the outside (Song 5:4–5). These keys were often large enough to be carried on the shoulder (Isa. 22:22).</p><p>Isaiah 22:22 uses the imagery of keys and locking to describe the authority entrusted to Eliakim: <em>I will lay the key of the house of David on his shoulder; he shall open, and none shall shut; and he shall shut, and none shall open.</em> Jesus applies the same language to the keys of the kingdom of heaven given to Peter (Matt. 16:19) and to himself as the holder of the key of David in Revelation 3:7, making the lock and key a significant biblical symbol of authority and access.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lock", "smith": "lock", "isbe": "lock"},
        "key_refs": ["Isaiah 45:2", "Isaiah 22:22", "Judges 3:24", "Revelation 3:7"]
    },
    "locust": {
        "id": "locust",
        "term": "Locust",
        "category": "concepts",
        "intro": "<p>Locust is the term applied to various species of migratory grasshoppers (primarily <em>Schistocerca gregaria</em>, the desert locust) capable of forming vast swarms that strip all vegetation from an area in hours. Ten different Hebrew words in Scripture designate locusts or related insects at various stages of development or under different names reflecting their destructive capacity. Locusts are named among the clean foods permitted to Israel (Lev. 11:22), and John the Baptist ate locusts and wild honey in the wilderness (Matt. 3:4; Mark 1:6). The eighth plague of Egypt was a devastating locust swarm that consumed every remaining plant (Ex. 10:12–15).</p><p>In prophetic literature, locusts function as instruments of divine judgment: Joel's famous locust plague (Joel 1:4–7; 2:1–11) becomes a metaphor for an invading army and is associated with the Day of the LORD. Amos 7:1–3 describes a locust swarm in a vision of coming judgment that is averted by prophetic intercession. Revelation 9:3–10 deploys the locust image eschatologically: demonic creatures like locusts rise from the abyss with the power of scorpions to torment humanity for five months—one of the most vivid symbolic deployments of the image in Scripture.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "locust", "smith": "locust", "isbe": "locust"},
        "key_refs": ["Matthew 3:4", "Revelation 9:3", "Joel 1:4", "Exodus 10:12"]
    },
    "lodge": {
        "id": "lodge",
        "term": "Lodge",
        "category": "concepts",
        "intro": "<p>Lodge in Scripture refers to a temporary shelter or watchman's hut set up in a field or vineyard to guard the ripening harvest. Isaiah 1:8 uses the image powerfully in his lament over Judah: <em>the daughter of Zion is left as a cottage in a vineyard, as a lodge in a garden of cucumbers</em>—suggesting the desolation of a harvest shed abandoned after the fruit is gathered, surrounded and alone. The Hebrew <em>melunah</em> refers to such a rudimentary shelter of woven branches or thatch, erected seasonally and then left to decay.</p><p>Isaiah 24:20 uses a related image: <em>the earth shall reel to and fro like a drunkard, and shall be removed like a cottage.</em> The fragility of the temporary lodging serves as a metaphor for the impermanence of earthly existence and security—a theme the Hebrew wisdom tradition frequently employs. In the New Testament, to <em>lodge</em> (Greek <em>katalyo</em> or <em>aulizesthai</em>) simply means to find lodging for the night, as Jesus and his disciples lodged in Bethany during the passion week (Matt. 21:17).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lodge", "isbe": "lodge"},
        "key_refs": ["Isaiah 1:8", "Isaiah 24:20"]
    },
    "log": {
        "id": "log",
        "term": "Log",
        "category": "concepts",
        "intro": "<p>Log was the smallest unit of liquid measure in the Mosaic system, equal to approximately one pint or 0.3 liters (though ancient metrology is uncertain). It is mentioned only in connection with the purification ritual for a healed leper: <em>a log of oil</em> is repeatedly specified in Leviticus 14 as the amount the priest was to use in the elaborate cleansing ceremony—one log of oil brought with two male lambs and one ewe lamb, used for wave offerings, anointing, and sprinkling (Lev. 14:10, 12, 15, 21, 24).</p><p>The log stood in relation to larger liquid measures as follows: 12 logs = 1 hin; 72 logs = 1 bath; 720 logs = 1 kor. The term reflects a system of measurement based on physical containers in common use, likely a clay vessel of a standardized size. The specificity of the log requirement in the leper's purification ritual illustrates the detailed nature of Mosaic purity law, where even the quantity of ceremonial oil was divinely prescribed.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "log", "smith": "log", "isbe": "log"},
        "key_refs": ["Leviticus 14:10", "Leviticus 14:12", "Leviticus 14:15"]
    },
    "lois": {
        "id": "lois",
        "term": "Lois",
        "category": "people",
        "intro": "<p>Lois (Greek, meaning <em>better</em> or <em>more desirable</em>) was the maternal grandmother of Timothy, Paul's most trusted associate and co-worker. She is mentioned once in the New Testament, in 2 Timothy 1:5, where Paul expresses his confidence in Timothy's genuine faith, noting that it <em>dwelt first in thy grandmother Lois, and thy mother Eunice.</em> This is the only biblical reference that explicitly identifies three generations of believing women and traces the transmission of faith from grandmother to mother to son.</p><p>Lois was almost certainly a Jewish woman from Lystra in Lycaonia, the home of Timothy's family (Acts 16:1). Paul's Letter to the Galatians suggests that Timothy's mother Eunice was a believing Jew who had raised Timothy in the Scriptures from childhood (2 Tim. 3:14–15), making Lois the likely source of the Hebrew scriptural tradition in which Timothy was formed. The commendation of Lois by name in Paul's final letter gives her a unique place of honor in New Testament memory as the origin of a family line of faith that helped shape the early church's leadership.</p>",
        "hitchcock_meaning": "better",
        "source_ids": {"easton": "lois", "smith": "lois", "isbe": "lois"},
        "key_refs": ["2 Timothy 1:5"]
    },
    "loop": {
        "id": "loop",
        "term": "Loop",
        "category": "concepts",
        "intro": "<p>Loop refers to a knotted eye or ring of blue cord sewn into the edges of the tabernacle curtains to link them together. Exodus 26:4–10 describes in detail how Moses was to make fifty loops along the edge of each outer curtain panel, with the loops of one set facing the loops of the matching set, so that they could be coupled together using fifty golden clasps (<em>taches</em>) to form the complete covering (Ex. 36:11–17). The precision with which these loops were to be aligned—<em>that the loops may take hold one of another</em>—reflects the extraordinary care given to the structural integrity of the portable sanctuary.</p><p>A separate set of fifty loops on the outermost curtains of goat's hair was joined by fifty bronze clasps (Ex. 26:10–11). The loop-and-clasp system allowed the tabernacle to be assembled and disassembled efficiently as the Israelites traveled through the wilderness, while maintaining structural stability when erected. The technical detail of the tabernacle instructions in Exodus 25–27 illustrates the theological principle that the worship of God was to be conducted with precision, craft, and beauty—not improvised, but ordered according to the divine pattern shown to Moses on the mountain.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "loop", "isbe": "loop"},
        "key_refs": ["Exodus 26:4", "Exodus 26:5", "Exodus 26:10"]
    },
    "lord": {
        "id": "lord",
        "term": "Lord",
        "category": "concepts",
        "intro": "<p>Lord translates several distinct Hebrew and Greek words in Scripture, each with different connotations. The most significant is the Hebrew <em>YHWH</em> (the divine name, traditionally rendered <em>LORD</em> in small capitals), which appears approximately 6,800 times in the Old Testament and was considered so sacred by post-exilic Jews that it was not to be pronounced, <em>Adonai</em> (my Lord) being read in its place. The name encapsulates God's self-existent, covenant-faithful nature, revealed to Moses at the burning bush (Ex. 3:14–15; 6:3). <em>El Shaddai</em> (God Almighty) was the name by which God was known to the patriarchs, while <em>YHWH</em> expressed the specific covenant relationship established at the Exodus.</p><p>The Greek <em>Kyrios</em> (Lord) in the New Testament serves both as a translation of <em>YHWH</em> and as the primary confessional title for Jesus Christ: <em>Jesus is Lord</em> (Rom. 10:9; 1 Cor. 12:3) became the foundational Christian creed. By applying Old Testament <em>Kyrios</em> texts to Jesus—such as Joel 2:32 (<em>whoever calls on the name of the LORD shall be saved</em>) in Romans 10:13—Paul and other New Testament writers implicitly equate Jesus with the covenant God of Israel, making the title <em>Lord</em> a primary vehicle for New Testament Christology.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lord", "smith": "lord", "isbe": "lord"},
        "key_refs": ["Exodus 6:3", "Psalms 83:18", "Romans 10:9", "1 Corinthians 12:3"]
    },
    "lords-day": {
        "id": "lords-day",
        "term": "Lord's Day",
        "category": "concepts",
        "intro": "<p>Lord's Day is the name given in Revelation 1:10 to the day on which John received his vision on Patmos: <em>I was in the Spirit on the Lord's day.</em> This is the only New Testament occurrence of the Greek phrase <em>he kyriake hemera</em>, which early Christian writers consistently used to designate Sunday—the first day of the week, the day of Christ's resurrection. The designation <em>Lord's Day</em> appears in early post-apostolic literature (Didache, Ignatius's Epistle to the Magnesians) as the established Christian day of communal worship, distinguished from the Jewish Sabbath.</p><p>The shift from the seventh-day Sabbath to the first day of the week for Christian corporate worship reflects the resurrection's eschatological significance: the community gathers on the day of the new creation, commemorating Christ's victory over death. The New Testament evidence for Sunday worship includes Acts 20:7 (breaking bread on the first day of the week), 1 Corinthians 16:2 (collecting offerings on the first day), and the multiple accounts of resurrection appearances on Sunday. The phrase <em>Lord's Day</em> thus encapsulates the early church's understanding of weekly worship as an ongoing celebration of the resurrection.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lords-day", "isbe": "lords-day"},
        "key_refs": ["Revelation 1:10", "Acts 20:7", "1 Corinthians 16:2"]
    },
    "lords-prayer": {
        "id": "lords-prayer",
        "term": "Lord's Prayer",
        "category": "concepts",
        "intro": "<p>The Lord's Prayer is the name given to the model prayer Jesus taught his disciples when they asked him to instruct them in prayer (Matt. 6:9–13; Luke 11:1–4). Though it is more properly called the Disciples' Prayer—Jesus himself did not need to pray it—the name has been traditional since the early church. The Matthean version, set within the Sermon on the Mount as a corrective to hypocritical public prayer, is the longer and liturgically dominant form. It consists of an address (<em>Our Father in heaven</em>), three petitions for God's glory (hallowing of the name, coming of the kingdom, doing of the will), and three petitions for human need (daily bread, forgiveness of debts, deliverance from evil).</p><p>The doxology (<em>For thine is the kingdom, the power, and the glory, forever, Amen</em>) found in most traditional uses does not appear in the oldest manuscripts of Matthew and is absent from Luke, but is found in the Didache (c. A.D. 100) and became standard in liturgical use. Jesus's teaching on prayer in John 17 provides the deeper theological context of prayer as communion with the Father—the unceasing intercession that grounds the disciples' own praying.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lords-prayer", "smith": "lords-prayer", "isbe": "lords-prayer"},
        "key_refs": ["Matthew 6:9", "Matthew 6:13", "Luke 11:1", "John 17:1"]
    },
    "lords-supper": {
        "id": "lords-supper",
        "term": "Lord's Supper",
        "category": "concepts",
        "intro": "<p>The Lord's Supper (1 Cor. 11:20) is the sacramental meal of bread and wine instituted by Jesus at the Passover meal the night before his crucifixion (Matt. 26:26–29; Mark 14:22–25; Luke 22:14–20; 1 Cor. 11:23–26). Jesus declared the bread to be his body given for his disciples and the cup to be the new covenant in his blood poured out for the forgiveness of sins, commanding them to repeat the meal in remembrance of him. Paul's account in 1 Corinthians 11:23–26 is the earliest written record, predating the Gospel accounts.</p><p>The rite is also called the <em>breaking of bread</em> (Acts 2:42; 20:7), the <em>communion</em> or <em>cup of the Lord</em> (1 Cor. 10:16–21), and, from the Greek <em>eucharistia</em> (thanksgiving), the Eucharist. It is distinguished from the Jewish Passover by its focus on Christ as the sacrificial lamb, from pagan cultic meals by its exclusivity (<em>you cannot drink the cup of the Lord and the cup of demons</em>, 1 Cor. 10:21), and from common eating by the requirement of self-examination (1 Cor. 11:28). The Corinthian church's abuses of the Supper prompted Paul's extended discussion and the solemn warning about eating and drinking judgment by not discerning the Lord's body (1 Cor. 11:29–30).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lords-supper", "smith": "lords-supper", "isbe": "lords-supper"},
        "key_refs": ["1 Corinthians 11:20", "1 Corinthians 11:26", "Matthew 26:26", "Acts 2:42"]
    },
    "lot": {
        "id": "lot",
        "term": "Lot",
        "category": "concepts",
        "intro": "<p>Lot (Hebrew <em>goral</em>, a small pebble or stone) was the physical object used in casting lots—an ancient method of making decisions by chance that the biblical world understood as a means of divine determination. The lots were typically small stones, sticks, or pottery shards that were shaken together in a vessel or container and then drawn or thrown to yield a binary or multiple outcome. Lots were cast to divide the land of Canaan among the twelve tribes (Num. 26:55; 33:54; Josh. 14–19), to identify Achan's guilt (Josh. 7:14), to select Saul as king (1 Sam. 10:20–21), to divide temple duties among the priests (1 Chr. 24–25), and to determine who would bear Haman's genocide against the Jews (Esth. 3:7—which gave rise to the feast of Purim, from the Akkadian <em>puru</em> meaning lot).</p><p>The theological conviction behind lot-casting is expressed in Proverbs 16:33: <em>The lot is cast into the lap, but its every decision is from the LORD.</em> The last recorded use of lots in Scripture is the apostles' selection of Matthias (Acts 1:26), which immediately precedes Pentecost—suggesting that after the Spirit's coming, direct prophetic guidance superseded the mechanical method of lot-casting in the early church's decision-making.</p>",
        "hitchcock_meaning": "an, wrapt up; hidden; covered; myrrh; rosin",
        "source_ids": {"easton": "lot", "smith": "lot", "isbe": "lot"},
        "key_refs": ["Numbers 33:54", "Proverbs 16:33", "Jonah 1:7", "Acts 1:26"]
    },
    "lotan": {
        "id": "lotan",
        "term": "Lotan",
        "category": "people",
        "intro": "<p>Lotan (meaning <em>covering</em> or <em>enveloping</em>) was the eldest son of Seir the Horite, one of the original inhabitants of Edom before the descendants of Esau dispossessed them (Gen. 36:20, 29; 1 Chr. 1:38–39). Seir the Horite gave his name to the land of Edom (also called Mount Seir), and his sons formed the aristocratic clans of the pre-Edomite Horites. Lotan is listed as the ancestor of two sub-clans in the Horite clan lists: Hori and Hemam (Gen. 36:22), or Hori and Homam (1 Chr. 1:39), the variant suggesting scribal confusion between similar Hebrew letters.</p><p>Lotan's sister was Timna (Gen. 36:22), who became the concubine of Eliphaz the son of Esau and the mother of Amalek—thus connecting the Horite and Edomite lineages through her. The Horites are known from extrabiblical sources as the Hurrians, a significant people group in the ancient Near East during the second millennium B.C., though their exact relationship to the Hurrians of Mesopotamia and Syria is debated by scholars.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lotan", "smith": "lotan", "isbe": "lotan"},
        "key_refs": ["Genesis 36:20", "Genesis 36:22", "Genesis 36:29"]
    },
    "love": {
        "id": "love",
        "term": "Love",
        "category": "concepts",
        "intro": "<p>Love in the Bible encompasses a range of relationships and qualities that different languages distinguish more precisely than English. The Old Testament uses <em>ahavah</em> for love in its emotional, relational, and covenantal dimensions—God's love for Israel (Deut. 7:7–8), Israel's required love for God with all the heart (Deut. 6:4–5), and human love for neighbor (Lev. 19:18). The concept of <em>hesed</em>—steadfast love, lovingkindness, or covenant faithfulness—is the dominant word for God's love toward his people, expressing loyalty that persists through betrayal (Ps. 136). The New Testament Greek distinguishes <em>agape</em> (self-giving love oriented toward the good of the other), <em>philia</em> (affectionate friendship), and <em>eros</em> (romantic love, not appearing in the NT).</p><p>The twin commands to love God with all one's being and to love one's neighbor as oneself (Matt. 22:37–40; Mark 12:29–31; Luke 10:27) summarize the entire Law and Prophets. John's Gospel and Epistles present love as the defining characteristic of God's nature (<em>God is love</em>, 1 John 4:8), of the relationship between the Father and the Son, and of the community shaped by Christ's example. Paul's hymn to love in 1 Corinthians 13 remains the canonical description of the character of divine love expressed through human life.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "love", "isbe": "love"},
        "key_refs": ["John 3:16", "1 Corinthians 13:4", "1 John 4:8", "Matthew 22:37"]
    },
    "lubims": {
        "id": "lubims",
        "term": "Lubims",
        "category": "people",
        "intro": "<p>Lubims (also Lubim or Libyans) designates the inhabitants of Libya, the North African territory west of Egypt along the Mediterranean coast. They appear in two historical accounts involving the Egyptian king Shishak's (Sheshonq I) invasion of Judah in the fifth year of Rehoboam: Shishak's army included Lubims, Sukkiim, and Ethiopians (2 Chr. 12:3). They appear again in the reign of Asa of Judah, when the Ethiopian Zerah led a vast army of Ethiopians and Lubims against Judah and was defeated at Mareshah (2 Chr. 16:8).</p><p>The Lubims/Libyans were a semi-nomadic Berber people of North Africa who from at least the New Kingdom period served as mercenary soldiers in the Egyptian army. Several pharaohs of the Twenty-Second through Twenty-Fourth Dynasties were of Libyan origin (including Shishak himself), reflecting the significant Libyan military presence in Egypt during the first millennium B.C. The Lubims in the biblical texts represent the multi-ethnic composition of Egyptian-allied armies that threatened Judah during the Divided Monarchy period.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lubims", "isbe": "lubims"},
        "key_refs": ["2 Chronicles 12:3", "2 Chronicles 16:8"]
    },
    "lucas": {
        "id": "lucas",
        "term": "Lucas",
        "category": "people",
        "intro": "<p>Lucas is the name used in some New Testament passages (Philem. 24; Col. 4:14) to refer to Luke the Evangelist, the physician and companion of Paul. The variant form <em>Loukas</em> (Lucas) and <em>Loukas</em> (Luke) both appear in the Greek manuscripts, reflecting the same individual. In Colossians 4:14 Paul refers to <em>Luke the beloved physician</em>, and in Philemon 24 to <em>Lucas, my fellow laborer</em>—one of the few companions who remained with Paul during his Roman imprisonment. Second Timothy 4:11 records that near the end of Paul's life, <em>Only Luke is with me,</em> testifying to his exceptional loyalty.</p><p>Luke was a Gentile Christian and the author of the Third Gospel and the Acts of the Apostles, making him the only known Gentile contributor to the New Testament canon. His medical background is reflected in the precision and detail of the healing accounts in his Gospel. The <em>we</em> passages in Acts (16:10–17; 20:5–21:18; 27:1–28:16) indicate he was a traveling companion of Paul on several of his missionary journeys. See also <strong>Luke</strong>.</p>",
        "hitchcock_meaning": "luminous; white",
        "source_ids": {"easton": "lucas", "smith": "lucas", "isbe": "lucas"},
        "key_refs": ["Philemon 1:24", "Colossians 4:14", "2 Timothy 4:11"]
    },
    "lucifer": {
        "id": "lucifer",
        "term": "Lucifer",
        "category": "concepts",
        "intro": "<p>Lucifer (Latin, meaning <em>light-bearer</em> or <em>morning star</em>) is the Latin Vulgate rendering of the Hebrew <em>helel ben-shahar</em> (<em>shining one, son of the dawn</em>) in Isaiah 14:12, a title given to the king of Babylon in a taunt-song celebrating his fall: <em>How are you fallen from heaven, O Lucifer, son of the morning!</em> The imagery draws on ancient Near Eastern mythology of a celestial being whose pride led to its downfall—applied here as a poetic metaphor for Babylon's arrogance and impending destruction.</p><p>Christian exegesis from Origen and Tertullian onward applied the Lucifer passage to the fall of Satan, reading it alongside Ezekiel 28:12–19 (the lament over the king of Tyre as a fallen guardian cherub) to construct a narrative of angelic rebellion before the creation of humanity. Jesus's statement <em>I saw Satan fall like lightning from heaven</em> (Luke 10:18) and Revelation 12:7–9's account of the war in heaven have reinforced this typological reading. The name <em>Lucifer</em> as a proper name for the devil derives entirely from this interpretive tradition rather than from direct biblical usage.</p>",
        "hitchcock_meaning": "bringing light",
        "source_ids": {"easton": "lucifer", "smith": "lucifer", "isbe": "lucifer"},
        "key_refs": ["Isaiah 14:12", "Luke 10:18", "Revelation 12:9"]
    },
    "lucius": {
        "id": "lucius",
        "term": "Lucius",
        "category": "people",
        "intro": "<p>Lucius is the name of two individuals in the New Testament. The first was Lucius of Cyrene, a Christian teacher or prophet at Antioch in Syria, mentioned first in the list of prophets and teachers from whom the Holy Spirit directed the church to set apart Barnabas and Paul for their first missionary journey (Acts 13:1). His Cyrenian origin connects him to the significant North African Jewish diaspora that produced other notable early Christians, including Simon of Cyrene who carried Jesus's cross (Mark 15:21).</p><p>The second was Lucius, a Jewish Christian kinsman (<em>sungenes</em>) of Paul who sent greetings to the Roman church in the closing chapter of Paul's letter (Rom. 16:21). He is listed alongside Timothy, Jason, and Sosipater, suggesting he was among Paul's colleagues in the Corinthian church from which Romans was written. Whether Lucius of Cyrene and this Lucius are the same person is uncertain; some have also proposed identifying one or both with Luke the Evangelist, whose Latin name <em>Lukas</em> is a shortened form of <em>Lucanus</em> related to <em>Lucius</em>, but this identification is speculative.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lucius", "smith": "lucius", "isbe": "lucius"},
        "key_refs": ["Acts 13:1", "Romans 16:21"]
    },
    "lucre": {
        "id": "lucre",
        "term": "Lucre",
        "category": "concepts",
        "intro": "<p>Lucre (from Latin <em>lucrum</em>, meaning <em>gain</em>) appears in the phrase <em>filthy lucre</em> in older translations of the pastoral epistles, designating dishonest or dishonorable financial gain. The Greek <em>aischrokerdeia</em> (shameful gain) and <em>aischrokerde</em> (greedy for gain) are translated as <em>greedy of filthy lucre</em> in 1 Timothy 3:3, 8 and Titus 1:7, 11, 1 Peter 5:2, where they describe a disqualifying vice for overseers, deacons, and elders in the church. The warning reflects a real danger in early church leadership: traveling teachers could exploit hospitality and financial support for personal enrichment.</p><p>The Didache and other early church documents regulated the support of itinerant prophets precisely because of abuses. Paul himself deliberately refused payment from certain congregations (1 Cor. 9:12–15; 2 Cor. 11:7–9) to avoid any appearance of preaching for money, while affirming that ministers of the gospel have a legitimate right to material support (1 Cor. 9:14; 1 Tim. 5:18). The contrast between <em>not given to filthy lucre</em> and <em>sober, just, holy, temperate</em> in Titus 1:8 indicates that financial integrity was a core component of the character expected of church leaders.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lucre", "isbe": "lucre"},
        "key_refs": ["1 Timothy 3:3", "Titus 1:7", "1 Peter 5:2"]
    },
    "lud": {
        "id": "lud",
        "term": "Lud",
        "category": "people",
        "intro": "<p>Lud (Hitchcock: <em>same as Lod</em>) designates two distinct peoples in the Table of Nations. (1.) Lud son of Shem (Gen. 10:22; 1 Chr. 1:17) is usually identified as the ancestor of the Lydians of western Asia Minor—a people who rose to prominence in the first millennium B.C. under kings such as Croesus and whose kingdom centered on Sardis until its conquest by Cyrus the Great in 547 B.C. Isaiah 66:19 groups Lud among the distant nations to whom God will send survivors as heralds of his glory. (2.) Ludim son of Mizraim (Egypt) (Gen. 10:13; 1 Chr. 1:11) represents an African people associated with Egypt, probably the same as the Lubim/Libyans or a related North African group.</p><p>In the prophetic literature, Lud appears as a supplier of skilled archers and warriors: Ezekiel 27:10 lists men of Persia, Lud, and Phut as mercenary soldiers in Tyre's army; Jeremiah 46:9 associates the Ludites with Libya and Ethiopia as allies of Egypt. The two different Lud lineages—Semitic and Hamitic—may represent the same geographic region but different traditions of its ethnic origin.</p>",
        "hitchcock_meaning": "same as Lod",
        "source_ids": {"easton": "lud", "smith": "lud", "isbe": "lud"},
        "key_refs": ["Genesis 10:22", "Isaiah 66:19", "Ezekiel 27:10", "Jeremiah 46:9"]
    },
    "ludim": {
        "id": "ludim",
        "term": "Ludim",
        "category": "people",
        "intro": "<p>Ludim was the first son of Mizraim (Egypt) in the Table of Nations (Gen. 10:13; 1 Chr. 1:11), and thus represented a people descended from Ham through the Egyptian line. They are associated in prophetic texts with the Egyptian military sphere: Jeremiah 46:9 names the Ludim alongside the Ethiopians (Cush) and the Libyans (Phut/Lubim) as African archers who handle and bend the bow in Egypt's army. Ezekiel also links Lud and Phut with Egypt (Ezek. 30:5).</p><p>The Ludim may be identified with the Libyan people known as the <em>Libu</em> in Egyptian sources, or with another North African ethnic group who served as mercenaries in the Egyptian military. Their appearance in Ezekiel's oracle against Egypt (Ezek. 30:5) alongside Ethiopia, Libya, Arabia, and the mixed peoples suggests they inhabited the western or southwestern fringes of the Egyptian sphere of influence. The Ludim should be distinguished from the Semitic Lud, son of Shem, who is the ancestor of the Asian Lydians, though the names are related and the traditions have sometimes been conflated in interpretation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ludim", "smith": "ludim", "isbe": "ludim"},
        "key_refs": ["Genesis 10:13", "Jeremiah 46:9", "Ezekiel 30:5"]
    },
    "luhith": {
        "id": "luhith",
        "term": "Luhith",
        "category": "places",
        "intro": "<p>Luhith (meaning <em>made of boards</em>) was a place in Moab, situated between the cities of Zoar and Horonaim, mentioned in two prophetic laments over Moab's coming desolation. Isaiah 15:5 records: <em>in the way of Luhith they shall go up with weeping; for in the way of Horonaim they shall raise up a cry of destruction.</em> Jeremiah 48:5 echoes almost identically: <em>in the going up of Luhith continual weeping shall go up; for in the going down of Horonaim the enemies have heard a cry of distress.</em></p><p>The <em>ascent of Luhith</em> in both passages suggests a steep road or pass climbing the Moabite plateau, possibly connecting the Jordan valley or Zoar region to the higher ground of Moab. The site has not been definitively identified, though several candidates in the Kerak region of modern Jordan have been proposed. The parallel structure of Isaiah and Jeremiah in describing Moab's flight along this road indicates a specific, well-known route that residents of Moab would have recognized as the path of desperate exile.</p>",
        "hitchcock_meaning": "made of boards",
        "source_ids": {"easton": "luhith", "smith": "luhith", "isbe": "luhith"},
        "key_refs": ["Isaiah 15:5", "Jeremiah 48:5"]
    },
    "luke": {
        "id": "luke",
        "term": "Luke",
        "category": "people",
        "intro": "<p>Luke (Greek <em>Loukas</em>, meaning <em>luminous</em> or <em>white</em>) was a Gentile Christian physician (Col. 4:14) and the author of the Third Gospel and the Acts of the Apostles—together comprising approximately one-quarter of the New Testament. His background as a medical professional is reflected in the precision of his accounts of healings and the completeness of his geographical and historical information. He is commended by Paul as <em>the beloved physician</em> and <em>fellow laborer</em> (Col. 4:14; Philem. 24), remaining with Paul during his final imprisonment in Rome when others had departed (2 Tim. 4:11).</p><p>Luke's two-volume work is dedicated to Theophilus (Luke 1:1–4; Acts 1:1) and is distinctive for its literary quality, its special concern for the marginalized (women, the poor, Samaritans, tax collectors), and its universal scope—tracing the gospel from a manger in Bethlehem to Caesar's household in Rome. The <em>we</em> passages in Acts indicate Luke accompanied Paul on portions of his second and third missionary journeys and the voyage to Rome (Acts 16:10–17; 20:5–21:18; 27:1–28:16). His Gospel is especially valued for the unique material it contains, including the parables of the Good Samaritan, the Prodigal Son, and the Rich Man and Lazarus, as well as the most detailed account of the Nativity.</p>",
        "hitchcock_meaning": "luminous; white",
        "source_ids": {"easton": "luke", "smith": "luke", "isbe": "luke"},
        "key_refs": ["Luke 1:1", "Colossians 4:14", "2 Timothy 4:11", "Acts 16:10"]
    },
    "luke-gospel-according-to": {
        "id": "luke-gospel-according-to",
        "term": "Luke, Gospel according to",
        "category": "concepts",
        "intro": "<p>The Gospel according to Luke is the third of the canonical Gospels and the first volume of a two-part work continued in the Acts of the Apostles. Written by Luke—a physician and companion of Paul (Col. 4:14)—it addresses Theophilus and explicitly claims to be a carefully researched, orderly account based on traditions from eyewitnesses and ministers of the word (Luke 1:1–4), making it unique among the Gospels in its self-conscious literary self-description. Luke draws on the Gospel of Mark, a sayings source (Q), and distinctive traditions (known as L material) not found in the other Gospels.</p><p>Luke's Gospel is distinguished by its scope and theological emphases: it begins with the birth narratives of John the Baptist and Jesus in parallel, includes the most extended travel narrative (9:51–19:27), and concludes uniquely with the Emmaus road appearance and an ascension account (24:50–53). Its concern for universal salvation, the role of the Holy Spirit, prayer, women, and the socially marginalized give it a distinctive character. Key unique passages include the parables of the Good Samaritan (10:25–37), the Prodigal Son (15:11–32), the Rich Man and Lazarus (16:19–31), and the Pharisee and Tax Collector (18:9–14), as well as Mary's Magnificat (1:46–55) and the account of the boy Jesus in the temple (2:41–52).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "luke-gospel-according-to", "isbe": "luke-gospel-according-to"},
        "key_refs": ["Luke 1:1", "Luke 4:18", "Acts 1:1"]
    },
    "lunatic": {
        "id": "lunatic",
        "term": "Lunatic",
        "category": "concepts",
        "intro": "<p>Lunatic (from Latin <em>luna</em>, the moon) was a term used in the Authorized Version (Matt. 4:24; 17:15) to translate the Greek <em>seleniazetai</em> (<em>moonstruck</em>), reflecting the ancient belief that epilepsy and certain mental disturbances were influenced by the phases of the moon. The word <em>seleniazetai</em> derives from <em>selene</em> (moon), and the condition described in Matthew 17:15—<em>for he is a lunatic and sore vexed, for ofttimes he falleth into the fire and oft into the water</em>—closely describes the symptoms of epilepsy.</p><p>Jesus healed this boy immediately after his transfiguration when his disciples had failed to do so. The case is described in detail in all three synoptic Gospels (Matt. 17:14–21; Mark 9:14–29; Luke 9:37–43); Mark's and Luke's accounts identify the condition as caused by an evil spirit. This combination of a disease-like presentation with spiritual causation reflects the New Testament's recognition that some physical afflictions in the Gospel period had demonic origin, without implying that all such conditions do. Jesus rebuked the unclean spirit, and the boy was healed immediately.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lunatic", "isbe": "lunatic"},
        "key_refs": ["Matthew 4:24", "Matthew 17:15", "Mark 9:17"]
    },
    "lust": {
        "id": "lust",
        "term": "Lust",
        "category": "concepts",
        "intro": "<p>Lust in Scripture denotes a strong, disordered desire—particularly of a sexual nature but also of appetite, covetousness, and pride—that draws a person away from God and toward sin. The Greek <em>epithumia</em> (translated <em>lust</em> or <em>desire</em>) in its negative sense describes the inward orientation of the fallen nature: <em>the sinful longing; the inward sin which leads to falling away from God</em> (Rom. 1:24; Gal. 5:16, 24; 1 John 2:16–17). James traces the genesis of sin through a distinct sequence: <em>each person is tempted when they are dragged away by their own evil desire and enticed. Then, after desire has conceived, it gives birth to sin; and sin, when it is full-grown, gives birth to death</em> (Jas. 1:14–15).</p><p>The tenth commandment's prohibition of coveting (Ex. 20:17) targets lust at the level of desire before any outward act, and Jesus intensifies this in the Sermon on the Mount by equating lustful looking with adultery of the heart (Matt. 5:28). Paul's remedy for lust is the mortification of the flesh through the Spirit (Rom. 8:13; Col. 3:5), the renewal of the mind (Rom. 12:2), and the practical disciplines of fleeing youthful passions and pursuing righteousness (2 Tim. 2:22; 1 Cor. 6:18).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lust", "isbe": "lust"},
        "key_refs": ["Romans 1:24", "James 1:14", "Matthew 5:28", "1 John 2:16"]
    },
    "luz": {
        "id": "luz",
        "term": "Luz",
        "category": "places",
        "intro": "<p>Luz (Hebrew, meaning <em>separation</em>, <em>departure</em>, or <em>an almond tree</em>) was the ancient Canaanite name of the city later known as Bethel (<em>house of God</em>). Jacob named it Bethel after his dream of a heavenly ladder there (Gen. 28:11–19), but the Canaanite name Luz persisted in usage (Gen. 35:6; Josh. 16:2; 18:13; Judg. 1:23–26). The city lay in the hill country of Ephraim at the southern border of that tribe's territory, approximately ten miles north of Jerusalem on the main road from Jerusalem to Shechem.</p><p>A second Luz is mentioned in Judges 1:26: when the Israelites captured the original Luz/Bethel, a man who had shown them the entrance was released, and he went and founded a new city in Hittite territory which he also named Luz, the name surviving there <em>unto this day.</em> The original Luz/Bethel became one of the most theologically significant sites in Israel's history—the location of Jacob's theophany, one of the two sanctuaries established by Jeroboam (1 Kings 12:29), and a prophetic center (Amos 3:14; 4:4).</p>",
        "hitchcock_meaning": "separation; departure; an almond",
        "source_ids": {"easton": "luz", "smith": "luz", "isbe": "luz"},
        "key_refs": ["Genesis 28:19", "Genesis 35:6", "Joshua 16:2", "Judges 1:23"]
    },
    "lycaonia": {
        "id": "lycaonia",
        "term": "Lycaonia",
        "category": "places",
        "intro": "<p>Lycaonia (meaning <em>she-wolf</em>) was an inland province of Asia Minor (modern central Turkey), situated on the Anatolian plateau west of Cappadocia and south of Galatia. Its principal cities included Iconium, Lystra, and Derbe—all of which figure prominently in Paul's first and second missionary journeys (Acts 13:51–14:23; 16:1). The region was remote, rugged, and culturally distinct: the Lycaonians spoke their own language (Acts 14:11 specifically notes this when the people of Lystra spoke in <em>the speech of Lycaonia</em> on witnessing Paul and Barnabas's miraculous healing), and the population was regarded by ancient writers as wild and difficult to govern.</p><p>Lycaonia's administrative boundaries shifted frequently under successive imperial rulers—Seleucids, various Hellenistic kingdoms, and finally Rome—and at different periods portions of the region were assigned to the provinces of Galatia, Cappadocia, and Cilicia. The churches Paul founded in Lycaonia (at Iconium, Lystra, Derbe) became important bases for the expansion of Christianity into Asia Minor and form part of the audience of the letter to the Galatians if the South Galatian hypothesis is correct.</p>",
        "hitchcock_meaning": "she-wolf",
        "source_ids": {"easton": "lycaonia", "smith": "lycaonia", "isbe": "lycaonia"},
        "key_refs": ["Acts 14:6", "Acts 14:11", "Acts 16:1"]
    },
    "lycia": {
        "id": "lycia",
        "term": "Lycia",
        "category": "places",
        "intro": "<p>Lycia was a province on the southwestern tip of Asia Minor (modern Turkey), opposite the island of Rhodes, known for its rugged mountainous terrain and a strong tradition of maritime independence. Paul's sea voyage to Rome passed through Myra in Lycia, where the centurion Julius found an Alexandrian grain ship bound for Italy and transferred the prisoners to it (Acts 27:5–6)—a detail that illustrates Lycia's role as a major port of call on ancient Mediterranean shipping routes. Paul also touched at Patara in Lycia during his third missionary journey (Acts 21:1–2).</p><p>Lycia had a distinctive political culture: its cities formed one of the earliest federations in history, the Lycian League, which gave each member city proportional representation based on size—a system later admired by Montesquieu and the American founding generation. The Lycians resisted absorption into successive empires and maintained considerable local autonomy under Rome. The presence of Jewish communities in Lycia is attested by 1 Maccabees 15:23, which lists Lycia among the regions to which Rome sent letters protecting Jewish rights.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lycia", "smith": "lycia", "isbe": "lycia"},
        "key_refs": ["Acts 21:1", "Acts 27:5"]
    },
    "lydda": {
        "id": "lydda",
        "term": "Lydda",
        "category": "places",
        "intro": "<p>Lydda (Greek name; Hebrew <em>Lod</em>; Hitchcock: <em>a standing pool</em>) was a town in the Shephelah district of the tribe of Ephraim (later of Dan), situated on the main road from Joppa to Jerusalem about twenty-five miles northwest of Jerusalem. It appears in the Old Testament as Lod, founded by Benjaminite settlers (1 Chr. 8:12), and was rebuilt after the Babylonian exile (Ezra 2:33; Neh. 7:37; 11:35). In the New Testament, Lydda is the site of one of Peter's notable miracles: during his circuit of the coastal communities, he healed Aeneas, a paralytic who had been bedridden for eight years, telling him, <em>Aeneas, Jesus Christ heals you; rise and make your bed</em> (Acts 9:32–35).</p><p>The healing at Lydda led directly to Peter being summoned to nearby Joppa to raise Dorcas from the dead, and the miracle of Aeneas caused all the inhabitants of Lydda and the plain of Sharon to turn to the Lord (Acts 9:35). Lydda/Lod has remained continuously inhabited; modern Lod contains Ben Gurion International Airport, Israel's main international gateway.</p>",
        "hitchcock_meaning": "a standing pool",
        "source_ids": {"easton": "lydda", "smith": "lydda", "isbe": "lydda"},
        "key_refs": ["Acts 9:32", "Acts 9:35", "1 Chronicles 8:12"]
    },
    "lydia": {
        "id": "lydia",
        "term": "Lydia",
        "category": "people",
        "intro": "<p>Lydia designates both a region of western Asia Minor and, more prominently in the New Testament, a woman who was the first recorded European convert to Christianity. Lydia the region (corresponding to ancient Lydian kingdom centered on Sardis) is mentioned in Ezekiel 30:5 and was the homeland of a people known for their wealth, commercial sophistication, and the invention of coinage. Its last independent king, Croesus, became proverbial for wealth before the kingdom fell to Cyrus the Great in 547 B.C.</p><p>Lydia the woman was a <em>seller of purple</em> from Thyatira, a city in the Lydian region known for its dyeing industry, who was residing in Philippi when Paul arrived there on his second missionary journey (Acts 16:14–15, 40). She was a <em>worshipper of God</em>—a God-fearer attending the Jewish prayer meeting by the river outside the city. When Paul spoke, the Lord opened her heart to receive his message; she and her household were baptized, and she immediately offered her home as a base for the mission. Lydia thus became the nucleus of the Philippian church, one of the most affectionate and generous of Paul's congregations.</p>",
        "hitchcock_meaning": "a standing pool",
        "source_ids": {"easton": "lydia", "smith": "lydia", "isbe": "lydia"},
        "key_refs": ["Acts 16:14", "Acts 16:15", "Acts 16:40", "Ezekiel 30:5"]
    },
    "lysanias": {
        "id": "lysanias",
        "term": "Lysanias",
        "category": "people",
        "intro": "<p>Lysanias (meaning <em>that drives away sorrow</em>) was the tetrarch of Abilene, a small territory on the eastern slope of Anti-Lebanon north of Damascus, at the time when John the Baptist began his ministry (Luke 3:1). Luke's precise synchronization of John's beginning with Roman and Jewish rulers—naming the Emperor Tiberius, Pilate, Herod Antipas, Philip, and Lysanias—establishes a specific historical date for the start of John's and Jesus's public ministry (approximately A.D. 28–29).</p><p>The identification of Lysanias has been a subject of historical scrutiny, since Josephus mentions a Lysanias who was king of Chalcis and was executed in 36 B.C.—too early to be Luke's Lysanias. An inscription discovered at Abila (in the Abilene region) referring to a <em>tetrarch Lysanias</em> in the time of Tiberius confirms that a later figure of the same name held that office, vindicating Luke's accuracy. The inclusion of this otherwise obscure local ruler in Luke's historical synchronism reflects his characteristic care in placing the gospel events within the concrete political realities of their time.</p>",
        "hitchcock_meaning": "that drives away sorrow",
        "source_ids": {"easton": "lysanias", "smith": "lysanias", "isbe": "lysanias"},
        "key_refs": ["Luke 3:1"]
    },
    "lysias-claudius": {
        "id": "lysias-claudius",
        "term": "Lysias, Claudius",
        "category": "people",
        "intro": "<p>Claudius Lysias was the Roman military tribune (chiliarch, commander of a cohort of one thousand men) who commanded the Roman troops garrisoned in the Antonia Fortress adjacent to the Jerusalem temple in the late 50s A.D. He appears in the narrative of Paul's arrest in Acts 21:31–23:30, playing a central role in the events that led to Paul's transfer to Caesarea. When the Jerusalem crowd was about to beat Paul to death, Lysias rushed down with soldiers and centurions and rescued him, having him bound with chains and intending to examine him by flogging until Paul revealed his Roman citizenship—at which point the flogging was immediately halted.</p><p>Lysias wrote a letter to the governor Felix explaining his reasons for sending Paul to Caesarea (Acts 23:26–30), a document Luke summarizes; it reveals that Lysias somewhat embellished his role, claiming to have rescued Paul when he learned he was a Roman citizen, whereas in fact he had already ordered the flogging before learning this. The letter illustrates how Roman bureaucratic communication worked in the provincial system and provides one of the New Testament's most concrete examples of Roman legal procedure protecting a citizen's rights.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "lysias-claudius", "smith": "lysias-claudius", "isbe": "lysias-claudius"},
        "key_refs": ["Acts 21:31", "Acts 22:24", "Acts 23:26"]
    },
    "lystra": {
        "id": "lystra",
        "term": "Lystra",
        "category": "places",
        "intro": "<p>Lystra (meaning <em>that dissolves or disperses</em>) was a town in Lycaonia in Asia Minor, situated in a remote and somewhat wild district about eighteen miles south-southwest of Iconium (modern Konya, Turkey). Paul and Barnabas fled to Lystra and Derbe when driven out of Iconium by Jewish opposition during Paul's first missionary journey (Acts 14:6). At Lystra, Paul healed a man who had been lame from birth; the crowd, speaking the local Lycaonian language, took Paul and Barnabas for the gods Hermes and Zeus in human form and attempted to offer sacrifices to them—an episode that prompted the missionaries' impassioned declaration of the living God as creator.</p><p>The same crowd, incited by Jews from Antioch and Iconium, subsequently stoned Paul and dragged him outside the city, leaving him for dead—one of the most dramatic reversals in Acts. Lystra was also the hometown of Timothy, whose mother Eunice was a Jewish believer and whose father was a Greek (Acts 16:1). Timothy became Paul's most trusted associate and companion. Paul later referred to the persecutions he suffered at Antioch, Iconium, and Lystra in 2 Timothy 3:11 as examples of endurance and divine deliverance.</p>",
        "hitchcock_meaning": "that dissolves or disperses",
        "source_ids": {"easton": "lystra", "smith": "lystra", "isbe": "lystra"},
        "key_refs": ["Acts 14:6", "Acts 14:8", "Acts 16:1", "2 Timothy 3:11"]
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
    print(f'BP l2: Litter → Lystra: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
