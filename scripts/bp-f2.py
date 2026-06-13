"""
BP Article Synthesis — f2: Forerunner → Fury
Covers Easton entries: Forerunner through Fury (28 entries)

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

Script: scripts/bp-f2.py
Run: python3 scripts/bp-f2.py
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


# ── Article data ──────────────────────────────────────────────────────────────
ARTICLES = {
    "forerunner": {
        "id": "forerunner",
        "term": "Forerunner",
        "category": "concepts",
        "intro": "<p>A forerunner in biblical usage is one who goes before to prepare the way for someone greater. John the Baptist is the most prominent forerunner in the New Testament, explicitly fulfilling Isaiah 40:3 and Malachi 3:1 in his role of preparing Israel for the ministry of Jesus Christ (Mark 1:2–3; Matthew 11:10). His mission was to call Israel to repentance, to announce the imminent arrival of the kingdom of God, and to direct his disciples to the one who came after him — whom he declared greater than himself.</p><p>Hebrews 6:20 applies the term directly to Christ himself: Jesus has entered the inner sanctuary of heaven \"as a forerunner on our behalf,\" having gone ahead into the holiest place so that believers may follow. The imagery draws on the high-priestly entry into the Most Holy Place on the Day of Atonement, but transforms it: Christ's entry is permanent and his opening of the way is for all who trust in him. The forerunner concept thus works on two levels in Scripture — John preparing the way for Christ, and Christ preparing the way for his people.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "forerunner"},
        "key_refs": ["Mark 1:2", "Mark 1:3", "Hebrews 6:20"]
    },
    "forest": {
        "id": "forest",
        "term": "Forest",
        "category": "concepts",
        "intro": "<p>Forests in ancient Canaan were far more extensive than the largely deforested landscape visible today. The Hebrew <em>ya'ar</em> (dense wood, from the luxuriance of its growth) describes the great primeval forests that covered the highland regions and much of the Galilee and Carmel range. Notable biblical forests include the forest of Lebanon — famous for its cedars, which supplied timber for Solomon's temple and palace — the forest of Ephraim east of the Jordan (2 Samuel 18:6–8, where Absalom died entangled in an oak), and the forests of the southern hill country of Judah.</p><p>Forests in the prophetic literature function as symbols of national pride and self-sufficiency that God will cut down in judgment: Isaiah 10:18–19 describes the Assyrian army as trees of a forest felled by a divine ax, and Isaiah 44:14 satirizes the idol-maker who cuts a cedar from the forest — using half for fuel and carving the remainder into a god. The image of the forest growing over devastated cities (Micah 3:12; Jeremiah 26:18) became a symbol of divine judgment on disobedient Jerusalem. Ecclesiastes 2:6 mentions Solomon's planting of forests as part of his great building projects.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "forest", "smith": "forest"},
        "key_refs": ["Ecclesiastes 2:6", "Isaiah 44:14", "Jeremiah 5:6", "2 Samuel 18:6"]
    },
    "forgiveness-of-sin": {
        "id": "forgiveness-of-sin",
        "term": "Forgiveness of Sin",
        "category": "concepts",
        "intro": "<p>Forgiveness of sin is in biblical theology one of the constituent elements of justification — the act by which God pardons the guilt and removes the legal penalty of a sinner's transgression. In forgiving sin, God does not merely overlook wrongdoing but acts consistently with his justice: in the Old Testament, forgiveness was grounded in the sacrificial system, where animal blood served as a covering (<em>kipper</em>) for sin pending the fuller revelation; in the New Testament, it is grounded in the atoning death of Christ, whose blood provides actual remission rather than anticipatory covering (Romans 3:25–26; Hebrews 10:1–14).</p><p>The New Testament vocabulary of forgiveness uses two primary words: <em>aphiemi</em> (to send away, release, cancel a debt) and <em>charizomai</em> (to bestow as a grace gift). Forgiveness is declared in the apostolic preaching as available through Christ's name (Acts 5:31; 13:38; Luke 24:47) and received by faith and repentance. Psalm 130:4 grounds the possibility of forgiveness in God's character: \"But there is forgiveness with thee, that thou mayest be feared.\" The parable of the Unmerciful Servant (Matthew 18:23–35) teaches that those who receive divine forgiveness are obligated to extend it to others.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "forgiveness-of-sin"},
        "key_refs": ["Acts 5:31", "Acts 13:38", "Psalms 130:4", "1 John 1:9"]
    },
    "fornication": {
        "id": "fornication",
        "term": "Fornication",
        "category": "concepts",
        "intro": "<p>Fornication in Scripture denotes sexual immorality broadly, though the term carries different emphases in the Old and New Testaments. In the Mosaic law, it referred primarily to illicit sexual intercourse outside of marriage, condemned in both the covenant code and the holiness code (Leviticus 19:29; 21:9; Deuteronomy 22:20–21). The law treated fornication seriously as a disruption of family, inheritance, and covenantal holiness. The prophets also used fornication and adultery as extended metaphors for Israel's unfaithfulness to God through idolatry — \"going after other gods\" as a wife breaking the marriage covenant (Hosea 1–3; Jeremiah 3; Ezekiel 16; 23).</p><p>In the New Testament, the Greek <em>porneia</em> (from which derives the English \"pornography\") covers a wide range of sexual immorality including prostitution, premarital sex, adultery, incest, and homosexual acts. Paul lists it among the works of the flesh (Galatians 5:19) and singles it out with particular urgency: unlike other sins committed \"outside the body,\" sexual immorality is a sin against the believer's own body, which is the temple of the Holy Spirit (1 Corinthians 6:18–19). The Jerusalem Council required Gentile converts to abstain from fornication alongside food offered to idols (Acts 15:20, 29). Revelation uses \"fornication\" figuratively for the great city's seduction of the nations into spiritual unfaithfulness (Revelation 17:2; 18:3).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "fornication"},
        "key_refs": ["Leviticus 19:29", "1 Corinthians 6:18", "Galatians 5:19", "Revelation 17:2"]
    },
    "fortunatus": {
        "id": "fortunatus",
        "term": "Fortunatus",
        "category": "people",
        "intro": "<p>Fortunatus (meaning <em>lucky</em> or <em>fortunate</em>, a Latin name common in the Roman world) was a disciple from the church at Corinth who, together with Achaicus and Stephanas, visited Paul at Ephesus during his extended ministry there. Paul mentions them with warm commendation at the close of 1 Corinthians (1 Corinthians 16:17–18): \"For they have refreshed my spirit and yours: therefore acknowledge ye them that are such.\" The visit served to fill the gap created by Paul's absence from Corinth, providing him with news of the congregation's condition and likely carrying either the Corinthians' letter of inquiry (which prompted 1 Corinthians) or the apostle's response back to them.</p><p>Nothing further is recorded about Fortunatus in the New Testament. Whether he was a freed slave (Latin names like \"Fortunatus\" were common among freedmen) or a free-born member of the Corinthian church cannot be determined from the text. His mention alongside Stephanas — the first Corinthian convert and leader of a household that devoted itself to the service of the saints (1 Corinthians 16:15) — suggests he was an active member of the Corinthian Christian community.</p>",
        "hitchcock_meaning": "lucky, fortunate",
        "source_ids": {"easton": "fortunatus", "smith": "fortunatus"},
        "key_refs": ["1 Corinthians 16:17"]
    },
    "fountain": {
        "id": "fountain",
        "term": "Fountain",
        "category": "concepts",
        "intro": "<p>Fountains and natural springs were of critical importance in the ancient Near Eastern world, where water scarcity shaped settlement patterns, agriculture, and military strategy. The Hebrew <em>'ain</em> (literally \"eye\" of the water desert) denotes a natural spring — a living, flowing source of water rising from the ground — as distinct from a cistern or well. Canaan was praised for its abundance of natural water sources: Moses described the promised land as a land of \"brooks of water, of fountains and depths that spring out of valleys and hills\" (Deuteronomy 8:7), a marked contrast to Egypt's dependence on the Nile.</p><p>Fountains in Scripture carry rich symbolic and theological resonances. The \"fountain of living waters\" is a recurring image for God himself (Jeremiah 2:13; 17:13) — and Israel's departure from God for idols is characterized as forsaking this fountain for broken cisterns. Proverbs 13:14 calls wisdom \"a fountain of life.\" Zechariah 13:1 prophesies a future \"fountain opened to the house of David and to the inhabitants of Jerusalem for sin and for uncleanness\" — fulfilled in Christ's atoning work. The river of life flowing from the throne of God in the new Jerusalem (Revelation 22:1) stands as the eschatological fulfillment of the fountain imagery throughout Scripture.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "fountain", "smith": "fountain"},
        "key_refs": ["Deuteronomy 8:7", "Jeremiah 2:13", "Zechariah 13:1", "Revelation 22:1"]
    },
    "fountain-of-the-virgin": {
        "id": "fountain-of-the-virgin",
        "term": "Fountain of the Virgin",
        "category": "places",
        "intro": "<p>The Fountain of the Virgin is the perennial spring that supplies the Pool of Siloam in Jerusalem, located in the Kidron Valley at the southeastern base of the City of David. It is known today as Gihon (Hebrew <em>gushing</em>), the spring whose intermittent outflow gives its name from the way it gushes periodically. The Fountain of the Virgin is one of the few natural water sources in or near Jerusalem, making it strategically vital to the city throughout its history.</p><p>King Hezekiah's famous water tunnel (2 Chronicles 32:30; 2 Kings 20:20), constructed approximately 1,750 feet through solid rock, redirected the spring's waters through the hill into the Pool of Siloam within the city walls in anticipation of the Assyrian siege of 701 BC. This remarkable engineering achievement — confirmed by the discovery of the Siloam Inscription in 1880 — protected Jerusalem's water supply from outside attack. The Pool of Siloam, fed by this spring, was the site where Jesus healed a man born blind by instructing him to wash there (John 9:7, 11).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "fountain-of-the-virgin"},
        "key_refs": ["2 Kings 20:20", "2 Chronicles 32:30", "John 9:7"]
    },
    "fowler": {
        "id": "fowler",
        "term": "Fowler",
        "category": "concepts",
        "intro": "<p>Fowlers — hunters of birds — employed a variety of methods in the ancient world: snares, nets, traps, decoy birds, and lime-covered sticks. Their skill and the secretive nature of their craft made them natural metaphors for those who seek to ensnare the unwary. Psalms 91:3 promises divine protection from \"the snare of the fowler,\" and Psalm 124:7 celebrates escape from it: \"Our soul is escaped as a bird out of the snare of the fowlers; the snare is broken, and we are escaped.\" Proverbs 6:5 urges the person caught in a sinful pledge to free himself \"as a bird from the hand of the fowler.\"</p><p>The prophets use the fowler as a figure for those who entrap the innocent: Hosea 9:8 describes a \"fowler's snare in all his ways,\" characterizing the prophet's opponents. Jeremiah 5:26 applies the image to wicked men who \"set a trap, they catch men\" — exploiting the vulnerable as a fowler catches birds. Ezekiel 17:20 uses the imagery of a net spread for the king of Judah who broke his covenant with Babylon. The metaphor's power lies in the victim's unawareness: the bird does not perceive the snare until it is caught, making the image apt for spiritual deception and moral danger.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "fowler"},
        "key_refs": ["Psalms 91:3", "Psalms 124:7", "Proverbs 6:5", "Jeremiah 5:26"]
    },
    "fox": {
        "id": "fox",
        "term": "Fox",
        "category": "concepts",
        "intro": "<p>The fox (Hebrew <em>shu'al</em>, derived from the animal's habit of digging or burrowing) is the common fox of Palestine, <em>Vulpes tabulae</em>, though the biblical term may sometimes indicate the jackal, which is more gregarious and was more commonly found in large numbers. Samson's famous exploit of catching three hundred foxes (or jackals), tying them in pairs by their tails with torches, and releasing them into the Philistine grain fields (Judges 15:4–5) more likely involved jackals, which could be caught more easily in numbers.</p><p>The fox appears metaphorically in several significant passages: the \"little foxes that spoil the vines\" in Song of Solomon 2:15 represent small, subtle threats to the flourishing relationship. Jesus called Herod Antipas \"that fox\" (Luke 13:32) — a term of contempt for a cunning but ultimately insignificant schemer. Ezekiel 13:4 compares false prophets to foxes in the ruins, scavenging without building or restoring. Lamentations 5:18 mourns that Mount Zion, desolate after the Babylonian destruction, has become the haunt of foxes. The Psalmist uses \"those who are for the fox\" as a figure for the slain who are abandoned (Psalm 63:10).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "fox", "smith": "fox"},
        "key_refs": ["Judges 15:4", "Song of Solomon 2:15", "Luke 13:32", "Ezekiel 13:4"]
    },
    "frankincense": {
        "id": "frankincense",
        "term": "Frankincense",
        "category": "concepts",
        "intro": "<p>Frankincense (Hebrew <em>lebonah</em>; Greek <em>libanos</em>, meaning \"white\") is an aromatic resin obtained by cutting the bark of trees of the genus <em>Boswellia</em>, primarily native to southern Arabia (Yemen and Oman), the Horn of Africa, and India. It was among the most prized luxury trade goods of the ancient world and features prominently in the biblical cult. In the Mosaic system, pure frankincense was added to the grain offering as the portion burned for God (Leviticus 2:1–2) and was placed beside the showbread in the tabernacle (Leviticus 24:7). A special compound incense formula — frankincense combined with other spices — was burned on the golden altar twice daily (Exodus 30:34–38) and was so sacred that reproducing it for personal use was forbidden under penalty of death.</p><p>Frankincense was imported into Israel from Arabia and the East via the great incense roads — a trade that made the Queen of Sheba's visit to Solomon (bringing \"spices, and very much gold, and precious stones\") commercially plausible. Isaiah 60:6 prophesies camels from Midian bringing gold and frankincense to glorify the LORD. In the New Testament, the Magi presented the infant Jesus with gold, frankincense, and myrrh (Matthew 2:11) — gifts of royalty, priesthood, and burial that the church has long read as prophetic of Christ's offices. Revelation 18:13 lists frankincense among the luxury goods of the great trading city whose fall is mourned.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "frankincense", "smith": "frankincense"},
        "key_refs": ["Exodus 30:34", "Leviticus 2:1", "Isaiah 60:6", "Matthew 2:11"]
    },
    "free-will-offering": {
        "id": "free-will-offering",
        "term": "Free-will Offering",
        "category": "concepts",
        "intro": "<p>A free-will offering (<em>nedabah</em> in Hebrew) was a voluntary sacrifice presented to God out of gratitude or devotion, as distinct from the mandatory offerings required by the law for specific occasions, sins, or calendar events. The construction of the tabernacle was largely funded by free-will offerings: Exodus 35:29 records that \"the children of Israel brought a willing offering unto the LORD, every man and woman, whose heart made them willing.\" The people's generosity exceeded what was needed, and Moses had to restrain them from bringing more (Exodus 36:5–7).</p><p>The law regulated even voluntary offerings by specifying that only unblemished animals could be presented (Leviticus 22:23 permitted a slightly imperfect animal for a free-will offering but not for a vow). In the post-exilic period, free-will offerings accompanied the return from Babylon: Ezra 3:5 records that along with the regular appointed sacrifices, the people offered \"every one a free-will offering unto the LORD.\" The New Testament transposes the concept into the sphere of financial generosity: Paul's collection for Jerusalem's poor and the Corinthians' giving are described in terms drawn from free-will offering theology — each should give as he has purposed in his heart, \"not reluctantly or under compulsion, for God loves a cheerful giver\" (2 Corinthians 9:7).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "free-will-offering"},
        "key_refs": ["Exodus 35:29", "Leviticus 22:23", "Ezra 3:5", "2 Corinthians 9:7"]
    },
    "freedom": {
        "id": "freedom",
        "term": "Freedom",
        "category": "concepts",
        "intro": "<p>Freedom in the Old Testament is primarily addressed in the context of the legal provisions governing the release of Hebrew servants and slaves. The Mosaic law limited the duration of voluntary servitude for Hebrews: a Hebrew servant was to serve six years and go free in the seventh (Exodus 21:2), though he could choose permanent bondservice by having his ear pierced at the doorpost. Female servants had different provisions regarding their release (Exodus 21:7–8). The Jubilee year (every fiftieth year) provided for the release of all Israelites who had sold themselves due to debt and the restoration of family land (Leviticus 25:39–41).</p><p>The theological dimension of freedom is grounded in the exodus: because God had redeemed Israel from Egyptian slavery, Israelites were not to be treated as permanent chattels — they were God's servants already (Leviticus 25:55). In the New Testament, freedom becomes a central soteriological theme: Christ's work liberates from the bondage of sin (Romans 6:18, 22), the curse of the law (Galatians 5:1), and the fear of death (Hebrews 2:14–15). Paul's paradox — \"a slave of Christ is a freedman of the Lord; a freedman of the Lord is a slave of Christ\" (1 Corinthians 7:22) — reframes the entire category of freedom in terms of belonging to God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "freedom"},
        "key_refs": ["Exodus 21:2", "Leviticus 25:39", "Romans 6:18", "Galatians 5:1"]
    },
    "frog": {
        "id": "frog",
        "term": "Frog",
        "category": "concepts",
        "intro": "<p>Frogs appear in Scripture primarily in two contexts: the second plague of Egypt and the apocalyptic imagery of Revelation. The Hebrew <em>tsepharde'a</em> (meaning \"marsh-leaper\") refers to the common frog of the Nile Valley, <em>Rana esculenta</em>, which bred in enormous numbers along the river and its marshes. The second plague brought frogs up out of the Nile in such numbers that they covered the land, entered houses, bedrooms, and food storage, and died in heaps — their putrefaction adding to Egypt's distress (Exodus 8:2–14; Psalms 78:45; 105:30). The irony of the plague is often noted: in Egyptian religion, the frog-headed goddess Heqet was associated with fertility and childbirth — the very creatures Egypt venerated became the instrument of divine judgment.</p><p>The book of Revelation (16:13) describes three unclean spirits like frogs coming out of the mouths of the dragon, the beast, and the false prophet — demonic spirits performing signs that go out to the kings of the earth to gather them for the battle of Armageddon. The frog image connects the eschatological scene with the Egyptian plague tradition, depicting the final opposition to God as spiritually defiling and reminiscent of the judgments on God's enemies in the exodus.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "frog", "smith": "frog"},
        "key_refs": ["Exodus 8:2", "Psalms 78:45", "Psalms 105:30", "Revelation 16:13"]
    },
    "frontlets": {
        "id": "frontlets",
        "term": "Frontlets",
        "category": "concepts",
        "intro": "<p>Frontlets (Hebrew <em>totaphoth</em>) appear in three passages of the Mosaic law: Exodus 13:16 and Deuteronomy 6:8 and 11:18. In each case, the command is to bind God's words \"as a sign upon thine hand\" and as \"frontlets between thine eyes.\" In Jewish tradition, the literal interpretation of these commands produced the practice of phylacteries (<em>tefillin</em>) — small leather boxes containing four passages of Scripture (Exodus 13:1–10; 13:11–16; Deuteronomy 6:4–9; 11:13–21), strapped to the forehead and left arm during morning prayers by observant Jewish men.</p><p>Whether Moses intended the command literally or as a vivid metaphor for keeping the law constantly in one's thoughts and actions has been debated. Many scholars read the surrounding context — \"thou shalt teach them diligently unto thy children...when thou sittest in thine house, and when thou walkest by the way\" (Deuteronomy 6:7) — as indicating that the \"frontlets\" command is part of a cluster of metaphorical idioms for comprehensive devotion to the law, not just a prescription for literal objects. Jesus critiques the Pharisees for making their phylacteries \"broad\" for show (Matthew 23:5), indicating that the practice was well-established by the first century but susceptible to ostentation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "frontlets"},
        "key_refs": ["Exodus 13:16", "Deuteronomy 6:8", "Deuteronomy 11:18", "Matthew 23:5"]
    },
    "frost": {
        "id": "frost",
        "term": "Frost",
        "category": "concepts",
        "intro": "<p>Frost (Hebrew <em>kerah</em>, from its smoothness or glassy appearance) occurs in the higher elevations of Palestine during winter, particularly in the hill country of Judah and the Transjordan plateau, where temperatures regularly drop below freezing. Genesis 31:40 records Jacob's complaint of enduring frost by night during his years of service for Laban in the elevated territory of Aram. Jeremiah 36:30 describes the dead body of Jehoiakim lying exposed \"to the frost by night\" as part of a divine curse.</p><p>Job 37:10 attributes the making of ice to God's breath: \"By the breath of God frost is given\" — part of Elihu's poetic catalog of divine meteorological power. Psalm 147:16–17 celebrates the LORD who \"giveth snow like wool\" and \"scattereth the hoarfrost like ashes,\" presenting the cold as an expression of divine sovereignty over creation. In the agricultural calendar, winter frosts could damage olive and fruit harvests; Proverbs 25:13 uses \"the cold of snow in the time of harvest\" (possibly referring to cold water rather than actual snow) as a figure for refreshment. The frost thus served as a reminder of human dependence on God's governance of the seasons.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "frost"},
        "key_refs": ["Genesis 31:40", "Job 37:10", "Psalms 147:16", "Jeremiah 36:30"]
    },
    "fruit": {
        "id": "fruit",
        "term": "Fruit",
        "category": "concepts",
        "intro": "<p>Fruit in Scripture denotes produce broadly — both agricultural crops (grain, grapes, olives, figs, pomegranates) and the offspring of animals and humans (\"the fruit of the womb,\" Psalms 127:3). The agricultural richness of Canaan was captured in the promise of a land of \"milk and honey\" whose fruit was so abundant that the spies carried a single cluster of grapes on a pole between two men (Numbers 13:23). The firstfruits of all harvests were dedicated to the LORD as a tithe and offering, acknowledging God as the source of all abundance (Numbers 18:12; Deuteronomy 14:23).</p><p>In the prophetic and wisdom literature, fruit becomes a standard metaphor for moral and spiritual outcomes. Israel is God's vine whose failure to produce good fruit invites judgment (Isaiah 5:1–7; Hosea 10:1). Proverbs 11:30 states that \"the fruit of the righteous is a tree of life.\" Jesus employs the fruit metaphor extensively: false prophets are known by their fruits (Matthew 7:16–20), the vine and branches parable (John 15:1–8) teaches that abiding in Christ produces lasting fruit, and the Spirit's fruit (Galatians 5:22–23) defines the character of transformed life. The harvest of souls appears in Revelation's imagery of eschatological judgment (Revelation 14:14–20).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "fruit"},
        "key_refs": ["Numbers 18:12", "Isaiah 5:2", "John 15:4", "Galatians 5:22"]
    },
    "frying-pan": {
        "id": "frying-pan",
        "term": "Frying-pan",
        "category": "concepts",
        "intro": "<p>The frying-pan (Hebrew <em>marhesheth</em>, a \"boiler\" or \"deep pan\") was a cooking vessel used in the preparation of grain offerings in the tabernacle and temple ritual. Leviticus 2:7 specifies that the grain offering baked in a frying-pan (or deep pan) was to be made of fine flour with oil, and Leviticus 7:9 confirms that such prepared grain offerings belonged to the priest who offered them. The vessel likely refers to a shallow earthenware or metal pan used for frying rather than the modern deep frying-pan, though the precise form of ancient culinary vessels varies by period and region.</p><p>The inclusion of various methods of grain preparation in Leviticus 2 — the oven (verse 4), the griddle (verse 5), and the frying-pan (verse 7) — indicates that the grain offering could take a variety of forms, with the priestly regulations covering each type. The grain offering (<em>minchah</em>) accompanied animal sacrifices and expressed dedication and covenant loyalty to God independent of animal blood, making it accessible to worshippers of limited means.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "frying-pan"},
        "key_refs": ["Leviticus 2:7", "Leviticus 7:9"]
    },
    "fuel": {
        "id": "fuel",
        "term": "Fuel",
        "category": "concepts",
        "intro": "<p>The fuel used in ancient Palestine included nearly every available combustible material: dry grass and thorns (Matthew 6:30; Psalms 58:9; Ecclesiastes 7:6), dried dung (Ezekiel 4:12, 15), wood, and charcoal. The relative scarcity of timber in many parts of Canaan meant that thorns, briers, and dried vegetation were commonly relied upon for cooking fires — fast-burning fuel that produced quick heat. Ezekiel's instruction to bake his bread over human dung as a sign of Jerusalem's coming defilement was so distressing to the prophet that God granted him cow dung as a substitute — indicating that animal dung fuel, though unpleasant, was a known and tolerable reality of daily life (Ezekiel 4:12–15).</p><p>In the prophetic imagination, fuel becomes a figure for what is consumed in judgment: Ezekiel 15 asks what the vine is good for if it produces no fruit — it cannot even be used as fuel, for the fire consumes it. Isaiah 9:5 describes the boots and garments of the enemy army becoming fuel for fire. The contrast between true worshippers and those who are mere fuel for divine judgment runs through both prophetic and apocalyptic texts (Isaiah 9:18–19; Ezekiel 21:32).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "fuel"},
        "key_refs": ["Ezekiel 4:12", "Matthew 6:30", "Ezekiel 15:4", "Isaiah 9:5"]
    },
    "fugitive": {
        "id": "fugitive",
        "term": "Fugitive",
        "category": "concepts",
        "intro": "<p>The word \"fugitive\" translates several Hebrew terms in the Old Testament. After Cain's murder of Abel, God pronounced that he would be \"a fugitive and a vagabond\" (<em>n'a</em>, a wanderer) in the earth, separated from both God's presence and the society of settled humanity (Genesis 4:12, 14). In Judges 12:4, the Gileadites used \"fugitive\" as a taunt against Ephraim — the Gileadites called the Ephraimites \"fugitives of Ephraim\" before identifying them by the famous password \"Shibboleth\" and killing those who could not pronounce it correctly. In 2 Kings 25:11, the word describes those who fled from Jerusalem at its fall to Babylon.</p><p>Cities of refuge in the Mosaic law (Numbers 35; Deuteronomy 19; Joshua 20) provided an official legal status for those who had accidentally killed someone and needed protection from the avenger of blood — a form of regulated asylum that distinguished the unintentional killer from the deliberate murderer. The fugitive who reached a city of refuge before being overtaken was entitled to a hearing and, if innocent of premeditated murder, to protection within the city until the death of the high priest. This institution reflects a careful legal distinction in Israelite law between manslaughter and murder.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "fugitive"},
        "key_refs": ["Genesis 4:12", "Genesis 4:14", "Judges 12:4", "Numbers 35:11"]
    },
    "fuller": {
        "id": "fuller",
        "term": "Fuller",
        "category": "concepts",
        "intro": "<p>A fuller was a craftsman who cleaned, thickened, and sometimes bleached newly woven cloth by trampling or beating it with the feet or clubs in water mixed with a cleansing agent. The name derives from the Anglo-Saxon <em>fullian</em> (to whiten). In ancient Palestine, the fuller's work required large quantities of water and the use of alkaline substances — alkali, natron, white clay, or the soapwort plant — to remove grease and impurities from raw wool and newly woven fabric. The trade was odorous enough that fullers' workshops were typically located outside city walls, near water sources.</p><p>Fuller's Field (or the Fuller's Field) near Jerusalem, located beside the conduit of the Upper Pool (2 Kings 18:17; Isaiah 7:3; 36:2), was likely the site where fullers stretched cleaned cloth to dry and bleach in the sun. It was at this location that Isaiah met Ahaz during the Syro-Ephraimite crisis, delivering the famous Immanuel prophecy (Isaiah 7:14). Malachi 3:2 describes the coming of the LORD's messenger as \"like a refiner's fire and like fullers' soap,\" using the fuller's purifying work as a metaphor for the purifying judgment that will precede the new covenant era. Mark 9:3 notes that Jesus's garments at the Transfiguration were \"exceeding white; so as no fuller on earth can white them.\"</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "fuller", "smith": "fuller"},
        "key_refs": ["Malachi 3:2", "2 Kings 18:17", "Isaiah 7:3", "Mark 9:3"]
    },
    "fullers-field": {
        "id": "fullers-field",
        "term": "Fuller's Field",
        "category": "places",
        "intro": "<p>Fuller's Field was a location near Jerusalem used by cloth-workers for washing, cleaning, and bleaching fabric. Its position is defined in Scripture by its proximity to the conduit of the Upper Pool, which lay to the north or northwest of the city. The site appears three times in significant prophetic encounters: Isaiah 7:3 records that the LORD told Isaiah to meet King Ahaz at \"the end of the conduit of the upper pool\" at the Fuller's Field — the occasion on which Isaiah delivered the Immanuel prophecy (Isaiah 7:14). The Assyrian Rabshakeh positioned himself at the same location to conduct his psychological warfare address to Jerusalem's defenders (2 Kings 18:17; Isaiah 36:2).</p><p>The choice of the Fuller's Field as a meeting point in both contexts may reflect that it lay on the main northern road approaching the city, making it a natural position for both royal consultations and enemy encampments. The exact identification of the conduit and the Upper Pool has been debated, with candidates including the northern part of the Tyropoeon Valley and the pool northwest of the Damascus Gate. The site's repeated appearance in key narratives underscores its functional importance in the city's topography.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "fullers-field"},
        "key_refs": ["2 Kings 18:17", "Isaiah 36:2", "Isaiah 7:3"]
    },
    "fullers-soap": {
        "id": "fullers-soap",
        "term": "Fuller's Soap",
        "category": "concepts",
        "intro": "<p>Fuller's soap (Hebrew <em>borith mekabbeshim</em>, literally \"alkali of those treading cloth\") was the cleansing agent used by cloth-workers in ancient Israel to remove grease, impurities, and stains from wool and newly woven fabric. It appears to have been derived from the ashes of various plants rich in potassium carbonate or from the soapwort plant (<em>Saponaria officinalis</em>), whose roots produce a natural lathering substance. The substance functioned similarly to modern soap through its alkali content.</p><p>Fuller's soap appears in Scripture primarily in its metaphorical uses. Proverbs 25:20 uses \"vinegar upon nitre\" (alkali) as an image of mismatched contexts. Jeremiah 2:22 acknowledges that even if Judah uses \"nitre\" and \"much soap,\" the stain of her iniquity cannot be removed by her own efforts — only God can cleanse. Malachi 3:2 presents the coming messenger as \"like fullers' soap\" — a powerful purifying agent that the priests and people will need for the refining judgment to come. These passages together present human sin as a stain that human cleansing agents cannot remove, setting the stage for the New Testament's proclamation of cleansing through Christ's blood (1 John 1:7).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "fullers-soap"},
        "key_refs": ["Jeremiah 2:22", "Malachi 3:2", "Proverbs 25:20"]
    },
    "fulness": {
        "id": "fulness",
        "term": "Fulness",
        "category": "concepts",
        "intro": "<p>Fulness (Greek <em>pleroma</em>) is a theologically significant term in the New Testament, used in several distinct but related senses. The \"fulness of time\" (Galatians 4:4; Ephesians 1:10) refers to God's appointed moment — the precise juncture in history, prepared through centuries of covenant history, law, prophecy, and providential circumstance, at which God sent his Son to be born of a woman under the law. The phrase conveys that the incarnation was not improvised but was the culmination of a long divine plan.</p><p>\"Fulness\" is also applied to Christ himself: Colossians 1:19 states that \"it pleased the Father that in him should all fulness dwell,\" and Colossians 2:9 declares that \"in him dwelleth all the fulness of the Godhead bodily\" — affirmations of Christ's complete divine nature against any reduction of him to a lesser being or intermediary. John 1:16 speaks of the \"fulness\" from which believers receive grace upon grace. Ephesians 3:19 prays that believers may be \"filled unto all the fulness of God,\" and Ephesians 1:23 describes the church as \"the fulness of him that filleth all in all\" — participation in Christ's completeness is both the source and the goal of Christian existence.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "fulness"},
        "key_refs": ["Galatians 4:4", "Colossians 2:9", "John 1:16", "Ephesians 1:23"]
    },
    "funeral": {
        "id": "funeral",
        "term": "Funeral",
        "category": "concepts",
        "intro": "<p>Burial was the universal Jewish practice for the disposal of the dead — cremation was foreign to Israelite culture and associated with paganism (though it was used in extreme circumstances, 1 Samuel 31:12). Burial typically took place on the day of death due to the rapid decomposition in the Near Eastern climate, making speed both a practical and religious imperative. The body was washed (Acts 9:37), wrapped in linen (John 11:44; 19:40), and anointed with spices to slow decomposition and honor the dead. The eyes were closed and the jaw bound. Public mourning — wailing, beating the breast, tearing garments, wearing sackcloth — was an expected social expression of grief.</p><p>Burial in family tombs was the norm: the patriarchs were gathered \"to their people\" in ancestral burial places (Genesis 25:8–9; 35:29; 49:29–33). The cave of Machpelah, purchased by Abraham for the burial of Sarah (Genesis 23), became the family tomb of the patriarchs. Professional mourners were hired for elaborate funerals (Matthew 9:23; Jeremiah 9:17). The dead body in Jewish law was a source of levitical impurity, requiring purification for those who came in contact with it (Numbers 19:11–22). Denial of burial was considered a severe dishonor and a divine curse (Deuteronomy 28:26; Jeremiah 22:19).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "funeral"},
        "key_refs": ["Genesis 23:19", "Genesis 25:9", "John 11:44", "Matthew 9:23"]
    },
    "furlong": {
        "id": "furlong",
        "term": "Furlong",
        "category": "concepts",
        "intro": "<p>Furlong in the New Testament translates the Greek <em>stadion</em> (plural <em>stadia</em>), the standard Greek unit of distance equal to approximately 606 feet and 9 inches, or roughly one-eighth of a Roman mile (185 meters). The word derives from the length of the Greek athletic stadium, which was laid out at this standard measurement. Luke 24:13 states that Emmaus was sixty stadia from Jerusalem — approximately seven miles; John 6:19 gives the disciples' distance from shore as twenty-five or thirty stadia; John 11:18 notes that Bethany was fifteen stadia from Jerusalem; and Revelation 14:20 and 21:16 use stadia in apocalyptic measurement.</p><p>The King James Version renders <em>stadion</em> as \"furlong\" — the traditional English unit of one-eighth of a mile — which is a close equivalent (660 feet versus 606 feet). Modern translations typically use \"miles,\" \"stadia,\" or metric equivalents. The unit appears seven times in the New Testament and provides geographically precise details that help locate key events in relation to Jerusalem and other known sites.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "furlong", "smith": "furlong"},
        "key_refs": ["Luke 24:13", "John 6:19", "John 11:18", "Revelation 21:16"]
    },
    "furnace": {
        "id": "furnace",
        "term": "Furnace",
        "category": "concepts",
        "intro": "<p>Furnaces in Scripture served both industrial and symbolic purposes. Industrially, smelting furnaces (Hebrew <em>kur</em>) were used for refining metals — gold, silver, and copper — and the image of purifying metal in a furnace became one of the most powerful metaphors in Scripture for God's refining work on his people: \"I have refined thee, but not with silver; I have chosen thee in the furnace of affliction\" (Isaiah 48:10; Proverbs 17:3; Malachi 3:2–3). Egypt itself is called the \"iron furnace\" in Deuteronomy 4:20 and 1 Kings 8:51, expressing the severity of Israel's bondage.</p><p>The Chaldean furnace (<em>attun</em>) of Daniel 3 was a large industrial furnace with a wide open mouth at the top, into which Shadrach, Meshach, and Abednego were thrown for refusing to worship Nebuchadnezzar's golden image. The narrative of their miraculous preservation — with a fourth figure \"like the Son of God\" walking in the flames with them (Daniel 3:25) — became a touchstone of faith in divine deliverance under persecution. In the New Testament, the furnace of fire appears as an image of eschatological judgment (Matthew 13:42, 50). Genesis 19:28 describes the smoke of Sodom rising like the smoke of a furnace after its destruction.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "furnace", "smith": "furnace"},
        "key_refs": ["Daniel 3:22", "Isaiah 48:10", "Proverbs 17:3", "Matthew 13:42"]
    },
    "furrow": {
        "id": "furrow",
        "term": "Furrow",
        "category": "concepts",
        "intro": "<p>A furrow is the groove or channel cut in the ground by the plough, and it appears in Scripture primarily in agricultural and metaphorical contexts. Psalm 65:10 uses the image of God watering the earth's furrows and softening it with showers, \"blessing the springing thereof\" — a picture of divine provision for the agricultural cycle that Israel depended on for survival. Hosea 10:4 describes judgment and injustice springing up \"as hemlock in the furrows of the field,\" using the agricultural image for the inevitable harvest of covenantal unfaithfulness.</p><p>Hosea 10:10 speaks of the nations gathering against Ephraim to bind them \"in their two furrows\" — a figure possibly drawn from oxen being yoked together for plowing, suggesting subjugation. Job 31:38 invokes the furrows themselves as witnesses against him: \"If my land cry against me, or that the furrows likewise thereof complain\" — an oath of innocence that personifies the earth as a moral witness. The psalms also use the furrow image for human oppression: Psalm 129:3 describes Israel's persecutors as ploughers who made long furrows on her back — an image of prolonged suffering from which the LORD ultimately delivered her.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "furrow"},
        "key_refs": ["Psalms 65:10", "Hosea 10:4", "Psalms 129:3", "Job 31:38"]
    },
    "fury": {
        "id": "fury",
        "term": "Fury",
        "category": "concepts",
        "intro": "<p>Fury as attributed to God in Scripture is a figurative expression for the dispensing of severe afflictive judgments upon sin and unbelief. The Hebrew <em>hemah</em> (wrath, fury, burning anger) and related terms appear frequently in the prophetic literature to describe the intensity of divine response to covenant violation and persistent sin. Isaiah 63:3–6 presents a dramatic image of God treading the winepress of his fury alone, his garments stained with the blood of the nations in an act of redemptive judgment. Leviticus 26:28 warns that if Israel persisted in disobedience, God would walk contrary to them \"in fury\" and chastise them seven times more for their sins.</p><p>The fury of God is consistently presented in Scripture not as irrational passion but as the measured, holy response of perfect righteousness to moral evil — what Paul calls the \"wrath of God revealed from heaven against all ungodliness and unrighteousness of men\" (Romans 1:18). The prophets who most extensively develop the theme — Isaiah, Jeremiah, and Ezekiel — also most clearly present its ultimate purpose as restorative: divine fury consumes what is corrupt to make way for renewal. The New Testament's most concentrated treatment of divine wrath (Romans 1–3; Revelation 14–19) presents Christ's atoning death as the means by which God's righteous fury against sin was satisfied, so that those in Christ are not destined for wrath (1 Thessalonians 5:9).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "fury"},
        "key_refs": ["Leviticus 26:28", "Isaiah 63:3", "Romans 1:18", "1 Thessalonians 5:9"]
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
