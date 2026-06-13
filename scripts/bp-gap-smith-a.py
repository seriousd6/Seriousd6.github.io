#!/usr/bin/env python3
"""BP gap-smith-a: Smith Bible Dictionary A–H scholarly entries (35 articles, score 25)"""
import json, os

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def load_article(slug):
    fp = os.path.join(OUT_DIR, f'{slug}.json')
    if os.path.exists(fp):
        with open(fp) as f:
            return json.load(f)
    return None

def save_article(slug, data):
    fp = os.path.join(OUT_DIR, f'{slug}.json')
    with open(fp, 'w') as f:
        json.dump(data, f, indent=2)

def merge_article(slug, data):
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True

ARTICLES = {
    "abomination-of-desolation": {
        "id": "abomination-of-desolation",
        "term": "Abomination of Desolation",
        "category": "events",
        "intro": "<p>The abomination of desolation is a phrase drawn from Daniel 9:27; 11:31; and 12:11, cited by Jesus in Matthew 24:15 and Mark 13:14 as a signal for those in Judea to flee to the mountains: <em>when you see the abomination of desolation spoken of by the prophet Daniel, standing in the holy place.</em> In Daniel the phrase (<em>shiqquts meshomem</em>) denotes a sacrilegious act or object that renders the sanctuary desolate — the setting up of an idol or pagan altar in the temple. The Maccabean period gave the prophecy a partial fulfillment when Antiochus IV Epiphanes erected an altar to Zeus in the Jerusalem temple in 167 BC and sacrificed swine upon it (1 Maccabees 1:54, 59).</p><p>Jesus's citation points toward a further fulfillment in the Roman destruction of Jerusalem in 70 AD. The phrase <em>let the reader understand</em> (Matthew 24:15; Mark 13:14) indicates that the reference was intentionally cryptic — requiring discernment to identify the specific historical event when it arrived. Scholars have identified the Roman siege standards planted in the temple precincts, or Caligula's attempted installation of his statue in the temple (38–40 AD), as fulfillments. Many interpreters also see an eschatological dimension pointing to a future apostasy or desecration at the end of the age, particularly in light of 2 Thessalonians 2:3–4 and Revelation 13.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "abomination-of-desolation", "isbe": "abomination-of-desolation"},
        "key_refs": ["Daniel 9:27", "Matthew 24:15", "Mark 13:14", "Daniel 11:31"]
    },
    "akeldama": {
        "id": "akeldama",
        "term": "Akeldama",
        "category": "places",
        "intro": "<p>Akeldama (Aramaic <em>Ḥaql Dema</em>, meaning <em>field of blood</em>) was the name given to the potter's field purchased with the thirty pieces of silver returned by Judas Iscariot after his betrayal of Jesus (Acts 1:18–19; Matthew 27:3–10). The two accounts differ in detail: Matthew states that the chief priests purchased the field with the returned money to use as a burial place for foreigners; Acts says Judas himself purchased the field and died there with a gruesome fall. Both agree that the field was renamed the Field of Blood and that this fulfilled a prophetic word — Matthew citing Zechariah 11:12–13 via Jeremiah 32:6–9.</p><p>The traditional site is the southeast slope of the Hinnom Valley, at the junction of the Hinnom and Kidron valleys south of Jerusalem — an area associated with the potters' trade and with earlier religious history as the Valley of Hinnom (Gehenna). A large building over an ancient charnel house at the site was used as a burial ground through medieval times. The cave-tomb beneath it has been excavated and is believed by some archaeologists to preserve the location of the original purchase.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "akeldama", "isbe": "akeldama"},
        "key_refs": ["Acts 1:19", "Matthew 27:8", "Matthew 27:3", "Zechariah 11:12"]
    },
    "baruch-book-of": {
        "id": "baruch-book-of",
        "term": "Baruch, Book of",
        "category": "concepts",
        "intro": "<p>The Book of Baruch is one of the deuterocanonical books of the Old Testament — included in the Septuagint and the Roman Catholic and Eastern Orthodox Old Testaments but excluded from the Protestant and Jewish canons and classified as Apocrypha. It is attributed to Baruch son of Neriah, the secretary and companion of the prophet Jeremiah. The book as it stands is a composite work, comprising a prose confession and prayer on behalf of the Babylonian exiles (1:1–3:8), a wisdom poem praising the Law as the embodiment of divine Wisdom (3:9–4:4), and a poetic exhortation of encouragement to the exilic community (4:5–5:9).</p><p>The book claims to have been read to Jehoiachin and the exiles in Babylon (1:1–4), but critical scholars generally date it to the second century BC or later on the basis of its literary dependencies on other biblical texts. The deuterocanonical status of Baruch was held in little esteem among the Jews even in antiquity, and Jerome did not include it in his Vulgate translation of the canonical books, though it was later appended to Jeremiah in the Latin tradition. The Letter of Jeremiah (sometimes printed as chapter 6 of Baruch) is a separate composition mocking idolatry.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "baruch-book-of", "isbe": "baruch-book-of"},
        "key_refs": []
    },
    "birds": {
        "id": "birds",
        "term": "Birds",
        "category": "concepts",
        "intro": "<p>Birds appear throughout the Bible in natural history, ritual law, figurative language, and theological symbolism. The Mosaic law distinguished between clean and unclean birds (Leviticus 11:13–19; Deuteronomy 14:11–20), prohibiting eagles, vultures, ravens, ostriches, owls, hawks, pelicans, storks, herons, and other birds of prey. Doves and pigeons were permitted and were the sacrifice option for the poor who could not afford a lamb (Leviticus 5:7; 12:8; Luke 2:24). Two birds were used in the cleansing ritual for leprosy (Leviticus 14:4–7). The general avifauna of Palestine is rich, lying on major migratory flyways between Africa, Asia, and Europe.</p><p>Biblically significant birds include the dove (symbol of peace and the Holy Spirit, Genesis 8:8–12; Matthew 3:16), the raven (which fed Elijah, 1 Kings 17:4–6), the eagle (symbol of God's sustaining care and swift judgment, Exodus 19:4; Isaiah 40:31), the sparrow and swallow (images of God's providential care of the humble, Psalm 84:3; Matthew 10:29–31), and the cock (whose crowing marked Peter's denial, Matthew 26:74). Solomon's wisdom encompassed speaking of birds (1 Kings 4:33). The Psalms and prophets use bird imagery extensively for the instincts of migration and nesting (Jeremiah 8:7; Proverbs 27:8).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "birds", "isbe": "birds"},
        "key_refs": ["Leviticus 11:13", "Matthew 10:29", "Matthew 3:16", "Jeremiah 8:7"]
    },
    "bitter-herbs": {
        "id": "bitter-herbs",
        "term": "Bitter Herbs",
        "category": "concepts",
        "intro": "<p>Bitter herbs were one of the three prescribed elements of the Passover meal, alongside the roasted lamb and unleavened bread (Exodus 12:8; Numbers 9:11). The Hebrew term <em>merorim</em> simply means bitters or bitter things. The purpose of the bitter herbs was to recall the bitterness of the Israelites' slavery in Egypt (Exodus 1:14), making the Passover meal a liturgical re-enactment of the exodus experience. The Mishnah (Pesachim 2:6) identifies five plants that may be used: lettuce, chicory, pepperwort, snakeroot, and dandelion.</p><p>Botanically, the plants most likely used in biblical times were wild lettuces, chicory, bitter cresses, hawkweeds, and sow-thistles — all of which grow abundantly in the Sinai peninsula, Palestine, and Egypt. These plants are bitter to the taste in their raw state, particularly in spring. In modern Jewish Passover observance the bitter herbs (<em>maror</em>) remain one of the symbolic foods of the Seder plate. The ritual use of bitter herbs connects the act of eating with historical memory, embodying in bodily experience the suffering from which the LORD delivered Israel.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "bitter-herbs", "isbe": "bitter-herbs"},
        "key_refs": ["Exodus 12:8", "Numbers 9:11", "Exodus 1:14"]
    },
    "blindness": {
        "id": "blindness",
        "term": "Blindness",
        "category": "concepts",
        "intro": "<p>Blindness was extremely common in the ancient Near East and appears frequently in biblical narrative, law, poetry, and prophecy. The primary physical causes included trachoma (a bacterial eye infection spread by flies), ophthalmia, vitamin A deficiency, trauma, and the effects of intense desert sunlight. Mosaic law protected the blind: <em>you shall not curse the deaf or put a stumbling block before the blind</em> (Leviticus 19:14); the blind were not to be turned aside from the right way (Deuteronomy 27:18). Blind animals were prohibited as sacrifices (Leviticus 22:22; Malachi 1:8), and physical defects including blindness disqualified priests from temple service (Leviticus 21:18).</p><p>Blind beggars appear throughout the Gospels as recipients of healing: Bartimaeus at Jericho (Mark 10:46–52), the man born blind in John 9, and the blind men of Galilee (Matthew 9:27–31). These healings fulfilled Isaiah's messianic prophecy that the eyes of the blind would be opened (Isaiah 35:5; 42:7; 61:1–2; Luke 4:18). Spiritual blindness — the inability to perceive God's truth — is a major metaphor in both Testaments (Isaiah 6:10; John 9:39–41; 2 Corinthians 4:4; Revelation 3:17). Paul was struck blind on the road to Damascus as a prelude to his conversion (Acts 9:8–9).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "blindness", "isbe": "blindness"},
        "key_refs": ["Leviticus 19:14", "John 9:1", "Isaiah 35:5", "Mark 10:46"]
    },
    "brazen-serpent": {
        "id": "brazen-serpent",
        "term": "Brazen Serpent",
        "category": "events",
        "intro": "<p>The brazen serpent (also bronze serpent or Nehushtan) was a bronze image made by Moses at God's command during the wilderness period, following a plague of fiery serpents sent against Israel as punishment for complaining against God and Moses (Numbers 21:5–9). God instructed Moses: <em>Make a fiery serpent and set it on a pole, and everyone who is bitten, when he sees it, shall live.</em> Moses made a serpent of bronze (<em>nechash nechoshet</em> — a wordplay in Hebrew), set it on a pole, and anyone who looked at it after being bitten lived. This act of looking in faith at the elevated serpent became the paradigmatic Old Testament type of the atonement.</p><p>Jesus explicitly drew on this event in John 3:14–15: <em>as Moses lifted up the serpent in the wilderness, so must the Son of Man be lifted up, that whoever believes in him may have eternal life.</em> The physical serpent preserved in Israel after the wilderness period became an object of idolatrous veneration; Hezekiah destroyed it as part of his religious reformation, calling it Nehushtan (meaning <em>a piece of bronze</em>) — a name that demythologized it and stripped it of divine status (2 Kings 18:4). The ISBE notes that the incident illustrates the principle that divine healing comes through a specific God-ordained means, requiring active faith.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "brazen-serpent", "isbe": "brazen-serpent"},
        "key_refs": ["Numbers 21:9", "John 3:14", "2 Kings 18:4"]
    },
    "caphtor-caphtorim": {
        "id": "caphtor-caphtorim",
        "term": "Caphtor, Caphtorim",
        "category": "places",
        "intro": "<p>Caphtor was the region identified as the original homeland of the Philistines before they settled on the coast of Canaan (Deuteronomy 2:23; Jeremiah 47:4; Amos 9:7). Amos 9:7 places Caphtor in a parallel with Egypt and Kush as the origins of Israel's neighbors: <em>Did I not bring Israel up from the land of Egypt, and the Philistines from Caphtor?</em> The Caphtorim are also listed in the Table of Nations as descendants of Mizraim (Egypt) who dispossessed the Avvim and settled in Gaza (Genesis 10:14; Deuteronomy 2:23). The Caphtorim likely correspond to the Keftiu of Egyptian records, widely identified with Crete or the Aegean — consistent with the broader scholarly identification of the Philistines as part of the Sea Peoples movement from the Aegean world who settled the Levantine coast around 1200 BC.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "caphtor-caphtorim", "isbe": "caphtor-caphtorim"},
        "key_refs": ["Deuteronomy 2:23", "Jeremiah 47:4", "Amos 9:7", "Genesis 10:14"]
    },
    "cauda": {
        "id": "cauda",
        "term": "Cauda",
        "category": "places",
        "intro": "<p>Cauda (also spelled Clauda in some manuscripts; modern Gavdos) was a small island south of Crete, mentioned in Acts 27:16 in Paul's account of his voyage to Rome. The ship on which Paul traveled was caught in the violent northeastern storm called <em>Euroclydon</em> or Euraquilo; while running before the storm they managed to pass under the lee of the island of Cauda, where they barely secured the ship's boat, undergirded the hull with cables, and took in the sea anchor. Cauda provided a brief shelter that allowed the sailors to take emergency precautions before the storm drove the ship across the Adriatic Sea toward Malta. The island is identified with modern Gavdos, the southernmost island of Europe, about 25 miles south of Crete's western tip.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "cauda", "isbe": "cauda"},
        "key_refs": ["Acts 27:16"]
    },
    "cherethites": {
        "id": "cherethites",
        "term": "Cherethites",
        "category": "people",
        "intro": "<p>The Cherethites and Pelethites together formed the personal bodyguard of King David (2 Samuel 8:18; 15:18; 20:7, 23; 1 Kings 1:38, 44; 1 Chronicles 18:17). Commanded by Benaiah son of Jehoiada, they served as the king's most trusted military escort, carrying out executions and accompanying the royal processions. They remained loyal to David during Absalom's rebellion (2 Samuel 15:18) and played a decisive role in ensuring Solomon's succession by escorting him to Gihon to be anointed (1 Kings 1:38).</p><p>The name Cherethites is linked to Crete (Hebrew <em>Kerethi</em>), and Smith suggests they were Cretan mercenaries — perhaps connected to the Caphtorim/Philistines and part of the Sea Peoples tradition. Ezekiel 25:16 and Zephaniah 2:5 use Cherethites as a name for the Philistine coastal inhabitants. The combination of foreign mercenaries in David's bodyguard (including also Ittai the Gittite's regiment) reflects the cosmopolitan military culture of his court — loyal fighters bound personally to the king rather than to tribal or national affiliations.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "cherethites", "isbe": "cherethites"},
        "key_refs": ["2 Samuel 8:18", "1 Kings 1:38", "Ezekiel 25:16"]
    },
    "cherith-the-brook": {
        "id": "cherith-the-brook",
        "term": "Cherith, The Brook",
        "category": "places",
        "intro": "<p>The brook Cherith (Hebrew <em>kerith</em>, meaning <em>cutting</em> or <em>ravine</em>) was the torrent-stream or wadi where Elijah hid himself at God's command during the first part of the three-and-a-half-year drought in the reign of Ahab (1 Kings 17:3–7). God directed Elijah: <em>Turn eastward and hide yourself by the brook Cherith, which is east of the Jordan.</em> There Elijah drank from the brook and was fed by ravens that brought him bread and meat morning and evening — a miraculous provision that sustained him during his withdrawal from public life. When the brook dried up because there was no rain in the land, God directed him to Zarephath.</p><p>The location of Cherith has been debated: the phrase <em>east of the Jordan</em> suggests a wadi in Transjordan, possibly Wadi Qelt or one of the wadis of Gilead. The feeding by ravens has been noted as the fulfillment of God's general promise to feed those who seek first his kingdom (Matthew 6:26) and as a particular sign of divine provision in a land suffering judgment for Ahab's Baalism.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "cherith-the-brook", "isbe": "cherith-the-brook"},
        "key_refs": ["1 Kings 17:3", "1 Kings 17:6", "1 Kings 17:7"]
    },
    "cities-of-refuge": {
        "id": "cities-of-refuge",
        "term": "Cities of Refuge",
        "category": "concepts",
        "intro": "<p>The cities of refuge were six Levitical cities designated under the Mosaic law as places of asylum for a person who had killed another unintentionally — the involuntary homicide who would otherwise be subject to vengeance by the <em>go'el ha-dam</em> (avenger of blood, a near kinsman) (Numbers 35:6–34; Deuteronomy 19:1–13; Joshua 20:1–9). Three were on each side of the Jordan: Kedesh in Naphtali, Shechem in Ephraim, and Kiriath-arba (Hebron) in Judah west of the Jordan; and Bezer in Reuben, Ramoth-gilead in Gad, and Golan in Manasseh east of the Jordan (Joshua 20:7–8).</p><p>The legal process required the person to flee to the city, stand at the gate, and state their case. If the elders admitted them, the avenger of blood could not harm them within the city. The case was tried and if the killing was found to be accidental, the person must remain in the city of refuge until the death of the high priest, after which they could return home safely. If they left before the high priest's death, the avenger could kill them without guilt. The cities symbolized God's provision of mercy within a justice system that took human life seriously, and the typological connection between the high priest's death and the release of the fugitive is widely noted in relation to Christ's atoning death.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "cities-of-refuge", "isbe": "cities-of-refuge"},
        "key_refs": ["Numbers 35:11", "Joshua 20:7", "Deuteronomy 19:3", "Numbers 35:28"]
    },
    "claudius-lysias": {
        "id": "claudius-lysias",
        "term": "Claudius Lysias",
        "category": "people",
        "intro": "<p>Claudius Lysias was the Roman military tribune (commander of a cohort of approximately 1,000 soldiers) in Jerusalem who rescued Paul from the Jewish mob in the temple courts (Acts 21:31–40; 22:24; 23:10, 26). When the crowd tried to beat Paul to death, Lysias arrested him, intending to examine him by flogging until Paul revealed his Roman citizenship — at which point the tribune became alarmed, recognizing that he had bound a Roman citizen (Acts 22:25–29). He later transferred Paul secretly to Caesarea Maritima under heavy escort to protect him from a plot to ambush and kill him (Acts 23:12–33), writing a letter to the governor Felix that diplomatically recast events to show Lysias in a favorable light (Acts 23:26–30). His Greek name with a Roman praenomen reflects the common practice of provincial freedmen adopting Roman names upon purchasing citizenship.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "claudius-lysias", "isbe": "claudius-lysias"},
        "key_refs": ["Acts 21:31", "Acts 22:28", "Acts 23:26"]
    },
    "cloud-pillar-of": {
        "id": "cloud-pillar-of",
        "term": "Cloud, Pillar of",
        "category": "concepts",
        "intro": "<p>The pillar of cloud by day and the pillar of fire by night was the visible manifestation of God's presence that guided and protected Israel throughout the wilderness journey from Egypt to Canaan (Exodus 13:21–22; 14:19–20; 40:34–38; Numbers 9:15–23). The cloud preceded the camp as they marched and rested on the tabernacle when they camped. It served multiple functions: directional guidance (lifting when Israel should move, resting when they should stop), protective cover (coming between the Israelite and Egyptian camps at the Red Sea, Exodus 14:19–20), and revelatory presence (God is said to have spoken to Moses out of or in the pillar, Numbers 12:5; Deuteronomy 31:15).</p><p>The cloud covered the tabernacle from its dedication onward (Exodus 40:34–38); when it lifted, Israel set out, and when it settled, they camped — even for extended periods (Numbers 9:19–22). This cloud was the Shekinah — the tangible dwelling of God among his people. The New Testament connects this tradition to the Spirit's presence (1 Corinthians 10:1–2) and to the Transfiguration's overshadowing cloud (Matthew 17:5), and Jesus's return is described as coming in clouds with great power and glory (Mark 13:26; Revelation 1:7).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "cloud-pillar-of", "isbe": "cloud-pillar-of"},
        "key_refs": ["Exodus 13:21", "Numbers 9:17", "1 Corinthians 10:1", "Revelation 1:7"]
    },
    "cornerstone": {
        "id": "cornerstone",
        "term": "Cornerstone",
        "category": "concepts",
        "intro": "<p>The cornerstone (or foundation stone) was the key structural element placed at the corner of a building to bind together the two courses of masonry and establish the building's alignment. In ancient construction the cornerstone was carefully selected, set first, and determined the position of the entire structure. The metaphor is used in Scripture both for human leaders — Isaiah 19:13 calls the princes of Egypt its <em>cornerstone</em> — and supremely for the LORD and his anointed servant.</p><p>Isaiah 28:16 contains the pivotal text: <em>Behold, I am the one who has laid as a foundation in Zion a stone, a tested stone, a precious cornerstone, of a sure foundation.</em> This is applied to Christ in the New Testament as the stone rejected by the builders but made the cornerstone by God (Psalm 118:22; Matthew 21:42; Acts 4:11; Ephesians 2:20; 1 Peter 2:6–7). Paul describes the church as built on the foundation of apostles and prophets, <em>Christ Jesus himself being the cornerstone</em> (Ephesians 2:20). The image was also used negatively: Isaiah 8:14 and Romans 9:33 describe the Messiah as a stone of stumbling and a rock of offense to those who do not believe.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "cornerstone", "isbe": "corner-stone"},
        "key_refs": ["Isaiah 28:16", "Psalm 118:22", "Ephesians 2:20", "1 Peter 2:6"]
    },
    "cuttings-[in-the-flesh]": {
        "id": "cuttings-[in-the-flesh]",
        "term": "Cuttings in the Flesh",
        "category": "concepts",
        "intro": "<p>Cuttings in the flesh were a mourning and religious practice widespread in the ancient Near East, in which worshippers lacerated their bodies as an act of mourning for the dead or propitiation of deities. The Israelites were explicitly prohibited from this practice in two Mosaic texts: Leviticus 19:28 forbids making cuts on the body for the dead or tattooing, and Deuteronomy 14:1 prohibits cutting oneself or shaving the forehead for the dead. These prohibitions set Israel apart from the surrounding Canaanite and Mesopotamian religious cultures.</p><p>The most dramatic biblical example of pagan self-laceration is 1 Kings 18:28, where the prophets of Baal cut themselves with swords and lances until blood gushed out during their contest with Elijah on Mount Carmel — an ecstatic practice meant to attract the god's attention. Jeremiah 16:6 describes the practice at funerals as something that would happen among those who abandoned God. The prohibition in Leviticus 21:5 extends specifically to priests. The underlying principle appears to be that the body is God's property, that mourning has legitimate forms that do not involve self-harm, and that manipulative attempts to compel divine response through suffering are foreign to the Israelite covenant relationship.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "cuttings-in-the-flesh", "isbe": "cuttings-in-the-flesh"},
        "key_refs": ["Leviticus 19:28", "Deuteronomy 14:1", "1 Kings 18:28", "Jeremiah 16:6"]
    },
    "degrees-songs-of": {
        "id": "degrees-songs-of",
        "term": "Degrees, Songs of",
        "category": "concepts",
        "intro": "<p>The Songs of Degrees (or Songs of Ascents, Hebrew <em>shir ha-ma'alot</em>) is the title given to Psalms 120–134, a collection of fifteen psalms distinguished by this superscription. Four are attributed to David, one to Solomon, and the remaining ten are anonymous. The Hebrew word <em>ma'alot</em> means <em>steps</em> or <em>ascents</em>, and three major interpretations have been proposed for the title: (1.) They were sung by pilgrims ascending to Jerusalem for the three annual feasts (Passover, Weeks, Tabernacles) — a connection supported by the pilgrim themes of several psalms (e.g., 122, 125, 126, 132). (2.) They were chanted by the Levites on the fifteen steps leading from the Court of the Women to the Court of Israel in the temple, one psalm per step. (3.) The title refers to a literary device of graduated or step-like parallelism in the psalms' poetry.</p><p>The first and third interpretations are not mutually exclusive, and the pilgrim-song explanation has the most ancient support (Mishnah Middot 2:5). These psalms include some of the most beloved in the Psalter: Psalm 121 (<em>I lift up my eyes to the hills</em>), Psalm 127 (<em>unless the LORD builds the house</em>), Psalm 130 (<em>out of the depths I cry to you</em>), and Psalm 133 (<em>how good and pleasant it is when brothers dwell in unity</em>).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "degrees-songs-of", "isbe": "degrees-songs-of"},
        "key_refs": ["Psalm 120:1", "Psalm 121:1", "Psalm 130:1", "Psalm 133:1"]
    },
    "denarius": {
        "id": "denarius",
        "term": "Denarius",
        "category": "concepts",
        "intro": "<p>The denarius (plural <em>denarii</em>; Authorized Version <em>penny</em>) was the principal silver coin of the Roman Empire in the New Testament period, equivalent in value to approximately a day's wage for a laborer. Its name derived from its original worth of ten bronze <em>asses</em>, later increased to sixteen. The coin bore the image and inscription of the reigning emperor on its obverse face.</p><p>The denarius appears in several of Jesus's parables and encounters. In the parable of the workers in the vineyard, a denarius is the agreed daily wage (Matthew 20:2, 9, 13). In the parable of the unforgiving servant, a debt of 100 denarii (about three months' wages) is contrasted with the servant's own enormous unpaid debt (Matthew 18:28). When the Pharisees and Herodians tried to trap Jesus with the tribute question, he asked for a denarius — observing that it bore Caesar's image and inscription — and gave the famous reply: <em>Render to Caesar the things that are Caesar's, and to God the things that are God's</em> (Matthew 22:19–21). The ointment poured on Jesus was said to be worth 300 denarii (about a year's wages, Mark 14:5; John 12:5).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "denarius", "isbe": "denarius"},
        "key_refs": ["Matthew 20:2", "Matthew 22:19", "Mark 14:5", "Matthew 18:28"]
    },
    "ebal-mount": {
        "id": "ebal-mount",
        "term": "Ebal, Mount",
        "category": "places",
        "intro": "<p>Mount Ebal is one of the two mountains flanking the city of Shechem in the central hill country of Canaan, the northern of the pair (with Mount Gerizim to the south, Deuteronomy 11:29; 27:12–13). Ebal was the mountain designated for the pronouncing of curses: Moses commanded that after Israel crossed the Jordan, the tribes of Reuben, Gad, Asher, Zebulun, Dan, and Naphtali should stand on Ebal to proclaim the curses for disobedience, while Simeon, Levi, Judah, Issachar, Joseph, and Benjamin stood on Gerizim to proclaim the blessings (Deuteronomy 27:12–13). Joshua carried out this ceremony after the conquest of Ai, building an altar on Mount Ebal of uncut stones, offering burnt offerings and peace offerings, and writing the law of Moses on plastered stones (Joshua 8:30–35).</p><p>Mount Ebal rises to approximately 3,080 feet (938 meters) above sea level, making it the highest peak in the central Samarian highlands. The covenant renewal ceremony at these mountains — with blessings and curses dividing the assembled nation — gave physical and geographical expression to the two-ways structure of Mosaic theology that pervades Deuteronomy.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "ebal-mount", "isbe": "ebal-mount"},
        "key_refs": ["Deuteronomy 11:29", "Deuteronomy 27:13", "Joshua 8:30"]
    },
    "ecclesiasticus": {
        "id": "ecclesiasticus",
        "term": "Ecclesiasticus",
        "category": "concepts",
        "intro": "<p>Ecclesiasticus is the name given in the Latin Vulgate tradition to the deuterocanonical book more fully titled <em>The Wisdom of Jesus son of Sirach</em>, or simply Ben Sira. It is one of the longest and most substantial of the deuterocanonical books, included in the Septuagint and in the Roman Catholic and Eastern Orthodox canons but excluded from the Protestant and Jewish biblical canons (where it is classified as Apocrypha). The book was written in Hebrew by a Jerusalem scribe named Joshua (Jesus) ben Eleazar ben Sira around 180 BC, and translated into Greek by his grandson around 132 BC, with the grandson's preface surviving as an introduction to the Greek text.</p><p>Ecclesiasticus is a wisdom book in the tradition of Proverbs, covering practical ethics, social conduct, prayer, the praise of famous ancestors of Israel (chapters 44–50, the famous <em>Let us now praise famous men</em>), and theological reflection on wisdom as the Law of Moses. The Hebrew text was partially lost and partially recovered in the Cairo Geniza (1896–1900) and at Masada (1964). The name <em>Ecclesiasticus</em> — meaning <em>the church book</em> — reflects its widespread use in early Christian catechesis and liturgy.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "ecclesiasticus", "isbe": "ecclesiasticus"},
        "key_refs": []
    },
    "education": {
        "id": "education",
        "term": "Education",
        "category": "concepts",
        "intro": "<p>Education in ancient Israel was primarily religious and moral rather than academic in the modern sense. The foundational texts are Deuteronomy 6:6–9 and 11:18–21, which commanded parents to teach the commandments diligently to their children — talking about them when sitting, walking, lying down, and rising up, and binding them as signs on hands and foreheads. The household was the primary educational unit; the father's role as teacher of the Law was central (Proverbs 1:8; 4:1–4; Ephesians 6:4). Wisdom literature (Proverbs, Ecclesiastes) is largely structured as parental instruction to sons.</p><p>Formal instruction in the Law was provided by the priests and Levites (Deuteronomy 31:9–13; 2 Chronicles 17:7–9) and by professional scribes and sages in the Second Temple period. Synagogues became centers of Torah education from the post-exilic period onward, with reading and exposition of the Scriptures as their primary function. Jewish boys were traditionally taught a trade alongside Torah study — Rabbi Jehuda's maxim that teaching a son no trade was equivalent to teaching him to be a thief reflects the integration of vocational and moral formation (Mishnah Kiddushin 4:14). In the New Testament, Jesus is called <em>rabbi</em> (teacher) and the disciples (<em>mathetes</em>) were literally learners, with the teacher-disciple model of Jewish education as its background.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "education", "isbe": "education"},
        "key_refs": ["Deuteronomy 6:7", "Proverbs 1:8", "Ephesians 6:4", "2 Chronicles 17:9"]
    },
    "elath-eloth": {
        "id": "elath-eloth",
        "term": "Elath, Eloth",
        "category": "places",
        "intro": "<p>Elath (also Eloth; modern Aqaba/Eilat) was a port city at the northern end of the Gulf of Aqaba (the eastern arm of the Red Sea), situated in the territory of Edom and strategically important for access to maritime trade routes to Arabia and East Africa. It is first mentioned in the account of Israel's wilderness wanderings (Deuteronomy 2:8) and came under Israelite control in the time of David. Solomon used the nearby port of Ezion-geber for his Red Sea fleet (1 Kings 9:26–28).</p><p>Control of Elath changed hands several times between Israel and Edom. Azariah (Uzziah) of Judah restored Elath to Judah (2 Kings 14:22; 2 Chronicles 26:2), but Rezin of Syria took it back and restored it to Edom/Syria in the reign of Ahaz (2 Kings 16:6). In the Roman period the site became the port of Aila, connecting the Nabataean trade network to the Red Sea. The modern Israeli city of Eilat and the Jordanian city of Aqaba now occupy the ancient site.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "elath-eloth", "isbe": "elath-eloth"},
        "key_refs": ["Deuteronomy 2:8", "1 Kings 9:26", "2 Kings 14:22", "2 Kings 16:6"]
    },
    "eli-eli-lama-sabachthani": {
        "id": "eli-eli-lama-sabachthani",
        "term": "Eli, Eli, Lama Sabachthani",
        "category": "events",
        "intro": "<p><em>Eli, Eli, lama sabachthani</em> (Matthew 27:46) or <em>Eloi, Eloi, lema sabachthani</em> (Mark 15:34) — <em>My God, my God, why have you forsaken me?</em> — are the words Jesus cried out from the cross in the ninth hour (3 PM), the fourth of the seven words from the cross recorded in the Gospels. The Hebrew form in Matthew and the Aramaic in Mark represent the opening verse of Psalm 22, the great psalm of the righteous sufferer that moves from abandonment to vindication. The entire psalm is remarkably predictive of the crucifixion scene (22:7–8, 16–18), and Jesus's quotation of its opening signals his identification with the psalm's suffering yet ultimately trusting voice.</p><p>The theological weight of these words is immense. They represent the darkest moment of the incarnation — the Son's experience of the Father's withdrawal in the bearing of human sin (2 Corinthians 5:21; Galatians 3:13). Bystanders misheard the cry as a call to Elijah. The words are simultaneously a cry of genuine desolation and an act of trust, since to pray Psalm 22 is to affirm that God <em>has not despised or scorned the suffering of the afflicted one</em> (Psalm 22:24). Luther called this the <em>theology of the cross</em> — God present in his hiddenness.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "eli-eli-lama-sabachthani", "isbe": "eli-eli-lama-sabachthani"},
        "key_refs": ["Matthew 27:46", "Mark 15:34", "Psalm 22:1", "Psalm 22:24"]
    },
    "euodia": {
        "id": "euodia",
        "term": "Euodia",
        "category": "people",
        "intro": "<p>Euodia (also spelled Euodias in older translations) was a woman in the church at Philippi who, together with Syntyche, was personally appealed to by Paul in Philippians 4:2–3: <em>I urge Euodia and I urge Syntyche to agree in the Lord.</em> Both women are commended as having <em>labored side by side with</em> Paul <em>in the gospel</em> along with Clement and other co-workers — indicating they held significant positions of ministry and service in the Philippian congregation. The appeal to a third party to <em>help these women</em> suggests a personal conflict between Euodia and Syntyche that was visible enough to warrant public address in the letter. Their names both carry positive meanings (Euodia = <em>prosperous journey</em> or <em>fragrant</em>; Syntyche = <em>fortunate</em>), and their ministry prominence reflects the role of women in the Philippian church, which from its founding had included Lydia as a leading figure (Acts 16:14–15).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "euodia", "isbe": "euodia"},
        "key_refs": ["Philippians 4:2", "Philippians 4:3"]
    },
    "excommunication": {
        "id": "excommunication",
        "term": "Excommunication",
        "category": "concepts",
        "intro": "<p>Excommunication in biblical contexts refers to formal exclusion from religious community, practiced in both Jewish and Christian settings. Jewish excommunication existed in three graduated forms: (1.) <em>niddui</em> — temporary exclusion for thirty days with certain restrictions on social contact; (2.) <em>cherem</em> — formal banning, stricter and more permanent; and (3.) <em>shammatha</em> — the most severe curse-like exclusion. The Mishnah lists twenty-four offenses punishable by excommunication. Jesus anticipates a form of this in Matthew 18:17 (<em>let him be to you as a Gentile and a tax collector</em>) and the Johannine community was familiar with being <em>put out of the synagogue</em> (aposynagogos, John 9:22; 12:42; 16:2).</p><p>In the New Testament, Paul exercises a form of excommunication in 1 Corinthians 5, commanding the church to deliver the incestuous man to Satan <em>for the destruction of the flesh, so that his spirit may be saved in the day of the Lord.</em> The goal is both the purity of the community and the restoration of the offender. 2 Thessalonians 3:14 instructs the church to have nothing to do with the disobedient, and 2 John 10 addresses refusing hospitality to false teachers. The purpose throughout is always the health of the body and the hope of the offender's repentance.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "excommunication", "isbe": "excommunication"},
        "key_refs": ["Matthew 18:17", "1 Corinthians 5:5", "John 9:22", "2 Thessalonians 3:14"]
    },
    "exodus-the": {
        "id": "exodus-the",
        "term": "Exodus, The",
        "category": "events",
        "intro": "<p>The Exodus was the foundational event of Israel's national history — the departure of the Israelite people from their enslavement in Egypt under the leadership of Moses, and their journey toward the promised land of Canaan. The narrative is contained in Exodus 1–18 and is the dominant paradigm of divine redemption in the Old Testament. God declared to Pharaoh through Moses: <em>Let my people go</em> (Exodus 5:1), and after ten plagues culminating in the death of Egypt's firstborn, Pharaoh expelled the Israelites. Israel departed on the night of the Passover, approximately 600,000 men plus women and children (Exodus 12:37), passed through the Red Sea, and received the Law at Sinai.</p><p>The date of the Exodus is debated: the traditional chronology, based on 1 Kings 6:1 (480 years before Solomon's fourth year), places it around 1446 BC in the reign of Amenhotep II; a later date around 1270–1250 BC in the reign of Ramesses II is favored by many archaeologists based on Egyptian evidence. The Exodus defines God's identity in the Old Testament: the Decalogue begins <em>I am the LORD your God, who brought you out of Egypt, out of the house of slavery</em> (Exodus 20:2). The New Testament presents Christ's death and resurrection as the ultimate Exodus — the liberation of humanity from the slavery of sin and death (Luke 9:31; 1 Corinthians 5:7; 10:1–4).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "exodus-the", "isbe": "exodus-the"},
        "key_refs": ["Exodus 12:51", "Exodus 20:2", "1 Kings 6:1", "1 Corinthians 10:1"]
    },
    "gabatha": {
        "id": "gabatha",
        "term": "Gabatha",
        "category": "people",
        "intro": "<p>Gabatha appears in the additions to the book of Esther (Esther 12:1 in the Septuagint; Apocrypha) as the name of one of the two eunuchs — along with Tharra — who conspired against King Artaxerxes (Ahasuerus) and were exposed by Mordecai. This corresponds to the Bigthana/Bigthan and Teresh conspiracy of the Hebrew text of Esther 2:21–23, where Mordecai overheard the plot, reported it to Esther who told the king, and the conspirators were hanged on the gallows — an act that was recorded in the chronicles of the king and later rewarded when Ahasuerus honored Mordecai (Esther 6:1–3). The expanded Greek text of Esther provides additional names and details not in the Hebrew original. Gabatha is thus the Greek name for one of the plotters whose exposure secured Mordecai's future standing.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "gabatha", "isbe": "gabatha"},
        "key_refs": ["Esther 2:21", "Esther 6:2"]
    },
    "genealogy": {
        "id": "genealogy",
        "term": "Genealogy",
        "category": "concepts",
        "intro": "<p>Genealogy in the biblical world served functions far broader than modern family history — it established tribal identity, inheritance rights, priestly eligibility, royal legitimacy, and covenantal continuity. The Hebrew term <em>toledot</em> (generations, genealogy) structures the entire book of Genesis as a series of generational narratives (<em>these are the generations of</em>…). Biblical genealogies include the linear type (a–b–c chain, often schematic) and the segmented type (branching, showing multiple descendants). Both are selective rather than exhaustive, often telescoping generations for thematic or numerical purposes.</p><p>Genealogies are particularly important for: establishing Levitical and priestly descent (crucial for temple service and post-exilic identification, Ezra 2:62; Nehemiah 7:64); royal legitimacy (the line of David through Jesse, Ruth 4:18–22; Matthew 1:1–17); and the two genealogies of Jesus in Matthew 1 and Luke 3, which trace his Davidic lineage to establish messianic credentials — Matthew tracing from Abraham through the royal line to Joseph, Luke tracing back through Nathan to Adam. The divergence between the two genealogies has been explained by levirate marriage, different branches of the Davidic family, or one tracing Mary's line.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "genealogy", "isbe": "genealogy"},
        "key_refs": ["Genesis 5:1", "Matthew 1:1", "Luke 3:23", "Ezra 2:62"]
    },
    "gleaning": {
        "id": "gleaning",
        "term": "Gleaning",
        "category": "concepts",
        "intro": "<p>Gleaning was the Mosaic provision by which the poor, the sojourner, the fatherless, and the widow were entitled to gather the portions of harvest left behind by the primary reapers. Three distinct gleaning laws are given: for grain fields (Leviticus 19:9–10; Deuteronomy 24:19), for vineyards (Leviticus 19:10; Deuteronomy 24:21), and for olive groves (Deuteronomy 24:20). In each case the farmer was prohibited from reaping the corners of the field, from going back over what had already been reaped, or from gathering fallen fruit — these were to be left for the vulnerable of society. The law did not require payment or charity; it required access to the means of productive labor.</p><p>The book of Ruth provides the most extended illustration of the gleaning laws in practice. Ruth the Moabitess gleaned in Boaz's field in Bethlehem, and Boaz instructed his workers to leave extra grain for her to gather and not to reproach her (Ruth 2:2–17). This narrative demonstrates both the social safety net the gleaning laws provided and the spirit of generosity that could go beyond the law's minimum requirements. The gleaning laws reflect a theology of land as God's gift to all Israel (Leviticus 25:23), not a private possession to be hoarded.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "gleaning", "isbe": "gleaning"},
        "key_refs": ["Leviticus 19:9", "Deuteronomy 24:19", "Ruth 2:2", "Ruth 2:17"]
    },
    "handicraft": {
        "id": "handicraft",
        "term": "Handicraft",
        "category": "concepts",
        "intro": "<p>Handicraft and skilled trades were practiced widely in ancient Israel and the surrounding cultures, and the biblical text reflects a society in which artisanal skill was valued both economically and spiritually. The Tabernacle and temple were built by craftsmen described as filled with divine <em>wisdom, understanding, and knowledge in every kind of craft</em> (Exodus 31:3; 35:31–35). The craftsmen Bezalel and Oholiab were specifically gifted by God for work in gold, silver, bronze, stonecutting, woodworking, weaving, and embroidery. Iron- and bronze-smithing, pottery, carpentry, tentmaking, and weaving are all attested in biblical texts.</p><p>Jewish tradition required fathers to teach their sons a trade — a practice reflected in Paul's tentmaking (Acts 18:3) and Jesus's identity as a carpenter or craftsman (<em>tekton</em>, Mark 6:3; Matthew 13:55). The Talmudic saying attributed to Rabbi Jehuda — that one who teaches his son no trade is as one who teaches him to be a thief — expresses the moral seriousness attached to productive labor. Revelation 18:22 mourns the fall of Babylon by cataloguing its lost craftsmen: <em>no craftsman of any craft will be found in you any more.</em></p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "handicraft", "isbe": "handicraft"},
        "key_refs": ["Exodus 31:3", "Acts 18:3", "Mark 6:3", "Revelation 18:22"]
    },
    "heliopolis": {
        "id": "heliopolis",
        "term": "Heliopolis",
        "category": "places",
        "intro": "<p>Heliopolis (Greek <em>city of the sun</em>) was the name given by Greek writers to the ancient Egyptian city known in the Hebrew Bible as <em>On</em> (Genesis 41:45, 50; 46:20) and in later prophetic texts as <em>Aven</em> (Ezekiel 30:17) and <em>Beth-shemesh</em> (House of the Sun, Jeremiah 43:13). It was the center of Egyptian sun worship — the city of the sun god Ra/Atum — and one of the most important religious and intellectual cities of ancient Egypt. Potiphera, the priest of On whose daughter Asenath became Joseph's wife, served the sun-god cult of this city (Genesis 41:45).</p><p>Jeremiah prophesied that Nebuchadnezzar would break the obelisks of Beth-shemesh (the sun-pillars of Heliopolis) and burn the temples of the Egyptian gods (Jeremiah 43:13). Ezekiel 30:17 names Aven (On) among the cities that would fall in the judgment on Egypt. The site of ancient Heliopolis is in modern-day northeastern Cairo; only a single obelisk of Sesostris I now stands at the site, but ancient sources describe it as one of the most monument-filled cities in Egypt. Isaiah 19:18 may allude to Heliopolis as <em>the City of Destruction</em> (or <em>the City of the Sun</em> in some manuscripts).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "heliopolis", "isbe": "heliopolis"},
        "key_refs": ["Genesis 41:45", "Jeremiah 43:13", "Ezekiel 30:17"]
    },
    "hin": {
        "id": "hin",
        "term": "Hin",
        "category": "concepts",
        "intro": "<p>The hin was a Hebrew liquid measure, equal to one-sixth of a bath or approximately 3.7–4 liters (about one US gallon) by modern estimates, though ancient weights and measures are subject to varying calculations. It was subdivided into thirds, halves, and sixths in priestly contexts (Exodus 29:40; Numbers 15:4–10). The hin appears primarily in connection with the Tabernacle and temple service: the prescribed oil for the lampstand (Exodus 30:24), the drink offerings that accompanied sacrifices (a quarter-hin for a lamb, a third-hin for a ram, a half-hin for a bull, Numbers 15:4–10), and the daily meal offering (Exodus 29:40).</p><p>The hin also appears in Ezekiel's vision of the restored worship in proportioned food and drink allocations (Ezekiel 4:11; 45:24; 46:5, 7, 11, 14). The name is likely borrowed from the Egyptian <em>hnw</em>, a standard Egyptian measure, reflecting the Mosaic system's Egyptian background. Like other biblical weights and measures, the actual value of the hin has been debated, with estimates ranging from approximately 3.5 to 6.5 liters depending on which period and textual tradition is followed.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "hin", "isbe": "hin"},
        "key_refs": ["Exodus 29:40", "Numbers 15:4", "Ezekiel 45:24"]
    },
    "hippopotamus": {
        "id": "hippopotamus",
        "term": "Hippopotamus",
        "category": "concepts",
        "intro": "<p>The hippopotamus is widely identified by modern scholars as the animal described under the name Behemoth in Job 40:15–24, where God challenges Job with a description of a magnificent creature: <em>Behold, Behemoth, which I made as I made you; he eats grass like an ox. Behold, his strength in his loins, and his power in the muscles of his belly.</em> The description of the creature's tail like a cedar, its strength in its belly muscles, its dwelling in reeds and swamps, its ability to drink up a river, and its imperviousness to hunters all match the hippopotamus (<em>Hippopotamus amphibius</em>), which was common in the Nile and known throughout the ancient Near East.</p><p>Alternative identifications include the elephant (which better fits the <em>cedar</em> tail, though elephants eat branches not grass) and a mythological creature representing primordial chaos. Smith's commentary identifies Behemoth as a description of the actual hippopotamus, consistent with the parallel divine speech about Leviathan (Job 41), which most likely describes the Nile crocodile. Both creatures — Behemoth and Leviathan — are used to overwhelm Job with the scale of God's creative power and wisdom, pointing to the frailty of human understanding before the Creator.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "hippopotamus", "isbe": "hippopotamus"},
        "key_refs": ["Job 40:15", "Job 40:23", "Job 40:19"]
    },
    "holofernes": {
        "id": "holofernes",
        "term": "Holofernes",
        "category": "people",
        "intro": "<p>Holofernes (also spelled Olofernes) was the Assyrian general of Nebuchadnezzar described in the deuterocanonical Book of Judith as commanding the army that invaded the western lands, besieged the Israelite city of Bethulia, and was killed by the Jewish widow Judith. According to the narrative, Judith gained access to Holofernes's camp under the pretense of providing intelligence against her own people, was entertained at his banquet, and when he had drunk himself to sleep, beheaded him with his own sword and carried his head back to Bethulia — a deed that routed the Assyrian army. The story has been compared to the earlier accounts of Jael and Sisera (Judges 4:17–22) and celebrates a woman as God's instrument for national deliverance.</p><p>Holofernes appears only in the Book of Judith and has no corroborated historical identification, adding to the scholarly consensus that the book is a theological narrative rather than historical chronicle. The name may be a Graecized form of a Persian or Old Iranian name. The story's canonical status varies: Judith is deuterocanonical in Catholic and Orthodox traditions but is not in the Protestant or Jewish biblical canons.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "holofernes", "isbe": "holofernes"},
        "key_refs": []
    },
    "hymenaeus": {
        "id": "hymenaeus",
        "term": "Hymenaeus",
        "category": "people",
        "intro": "<p>Hymenaeus was a member of the early Christian community whom Paul publicly named and delivered to Satan along with Alexander for having rejected faith and a good conscience and shipwrecked their faith (1 Timothy 1:20). Paul's use of <em>delivered to Satan</em> parallels his instruction regarding the incestuous man in Corinth (1 Corinthians 5:5) — an act of ecclesiastical discipline that removed the person from the protective sphere of the church community, in the hope of eventual correction. Hymenaeus reappears in 2 Timothy 2:17–18 alongside Philetus, as someone whose teaching is spreading <em>like gangrene</em> — specifically the heresy that <em>the resurrection has already happened,</em> an over-realized eschatology that Paul says was upsetting the faith of some. The two epistles together present Hymenaeus as a teacher who began within the Pauline community and became a significant theological threat to it.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"smith": "hymenaeus", "isbe": "hymenaeus"},
        "key_refs": ["1 Timothy 1:20", "2 Timothy 2:17", "2 Timothy 2:18"]
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
    print(f'BP gap-smith-a: Smith A–H scholarly entries: wrote {written}, skipped {skipped} existing.')

if __name__ == '__main__':
    main()
