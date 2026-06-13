"""
BP Article Synthesis — t2: Tetrarch → Tooth
Covers Easton entries: Tetrarch through Tooth (75 entries)

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

Script: scripts/bp-t2.py
Run: python3 scripts/bp-t2.py
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
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True


ARTICLES = {
    "tetrarch": {
        "term": "Tetrarch",
        "category": "concepts",
        "intro": "<p>Tetrarch, literally <em>ruler of a fourth part</em> of a province, was a title used in the Roman imperial system for subordinate regional rulers below the rank of king. In the New Testament it denotes any such client ruler of a territorial division (Matt. 14:1; Luke 3:1). Herod Antipas, who governed Galilee and Perea, and his brother Philip, who ruled the northeastern regions, were both tetrarchs under Roman authority following the division of Herod the Great's kingdom at his death in 4 BC.</p><p>The title carried real administrative and military power despite its lesser prestige. Herod Antipas, the tetrarch most prominent in the Gospels, is responsible for the execution of John the Baptist (Matt. 14:1-12) and plays a brief role in the trial of Jesus (Luke 23:7-12). The NT writers use the term loosely to mean any subordinate regional governor, not strictly one who rules a quarter-share.</p>",
        "hitchcock_meaning": "governor of a fourth part",
        "source_ids": {"easton": "tetrarch", "smith": "tetrarch", "isbe": "tetrarch"},
        "key_refs": ["Matthew 14:1", "Luke 3:1", "Acts 13:1"]
    },
    "thaddaeus": {
        "term": "Thaddaeus",
        "category": "people",
        "intro": "<p>Thaddaeus, one of the twelve apostles, is listed in Mark 3:18 and Matthew 10:3 where he is also called Lebbaeus. He is generally identified with Judas son of James (Luke 6:16; Acts 1:13), making him the apostle Judas who is distinguished from Iscariot. The name Thaddaeus may mean <em>breast</em> or <em>heart</em>, reflecting a term of endearment.</p><p>His only recorded words in the Gospels come at the Last Supper, where he asked Jesus, \"Lord, how is it that you will manifest yourself to us and not to the world?\" (John 14:22), prompting Jesus's teaching on the indwelling of the Spirit. Church tradition assigns him missionary work in Edessa and Persia, but these accounts are largely legendary. He is commemorated with Simon the Zealot in the Western liturgical calendar.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "thaddaeus", "isbe": "thaddaeus"},
        "key_refs": ["Mark 3:18", "Matthew 10:3", "Luke 6:16"]
    },
    "thahash": {
        "term": "Thahash",
        "category": "people",
        "intro": "<p>Thahash, whose name means <em>that makes haste</em> or <em>that keeps silence</em>, was a son of Nahor, Abraham's brother, born to his concubine Reumah (Gen. 22:24). He is mentioned only in the genealogical list connecting Abraham's extended Mesopotamian family.</p><p>His inclusion in the Table of Nations context helps establish the broader family network from which Abraham descended and from which Rebekah, Laban, Rachel, and Leah would later come. No individual narrative is attached to Thahash beyond his genealogical listing.</p>",
        "hitchcock_meaning": "that makes haste; that keeps silence",
        "source_ids": {"easton": "thahash", "isbe": "thahash"},
        "key_refs": ["Genesis 22:24"]
    },
    "tharshish": {
        "term": "Tharshish",
        "category": "places",
        "intro": "<p>Tharshish (Tarshish) was a distant maritime region associated with the great trading ships that sailed long ocean voyages in the ancient world (1 Kings 10:22; 22:48). The <em>ships of Tarshish</em> became a proverbial expression for large merchant vessels capable of extended seafaring, used by Phoenicians and later by Israelite traders under Solomon and Jehoshaphat.</p><p>Its precise location remains debated: the most commonly proposed identifications are Tartessus in southern Spain, Carthage in North Africa, or a region somewhere in the western Mediterranean. The consistent association with silver, iron, tin, and lead (Ezek. 27:12) and with very long voyages argues for a location far to the west of Palestine. Jonah's attempt to flee to Tarshish (Jon. 1:3) is used to illustrate the impossibility of escaping God's presence.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tharshish", "smith": "tharshish"},
        "key_refs": ["1 Kings 10:22", "1 Kings 22:48", "Jonah 1:3", "Ezekiel 27:12"]
    },
    "theatre": {
        "term": "Theatre",
        "category": "concepts",
        "intro": "<p>The theatre is mentioned in Scripture only in Acts 19:29-31, where the silversmiths of Ephesus, inflamed by Demetrius's accusations against Paul, dragged his companions Gaius and Aristarchus into the city's great theatre. Such open-air amphitheatres were standard features of Hellenistic and Roman cities, capable of seating tens of thousands for public assemblies, dramatic performances, and civic meetings.</p><p>The Ephesian theatre, subsequently excavated by archaeologists, could hold approximately twenty-four thousand spectators and remains partially standing today. The assembly that gathered there was chaotic and legally problematic, as the town clerk acknowledged in calming the crowd (Acts 19:35-41). The episode illustrates how public spaces of Greco-Roman civic life became sites of conflict between early Christianity and established economic and religious interests.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "theatre", "smith": "theatre", "isbe": "theatre"},
        "key_refs": ["Acts 19:29", "Acts 19:31"]
    },
    "thebez": {
        "term": "Thebez",
        "category": "places",
        "intro": "<p>Thebez, whose name may mean <em>brightness</em>, was a town approximately eleven miles northeast of Shechem on the road toward Scythopolis, identified with the modern site of Tubas. It is known in Scripture solely from the account of Abimelech's death: having subdued most of Israel, he besieged Thebez, and as he approached the tower gate to set it afire, a woman dropped an upper millstone on his head, fatally crushing his skull (Judg. 9:50-54).</p><p>Abimelech, unwilling to die at the hand of a woman, commanded his armor-bearer to run him through with a sword. The episode became a proverbial example of the danger of advancing too near city walls in siege warfare — Joab references it explicitly when reporting Uriah's death to David (2 Sam. 11:21).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "thebez", "smith": "thebez", "isbe": "thebez"},
        "key_refs": ["Judges 9:50", "2 Samuel 11:21"]
    },
    "theft": {
        "term": "Theft",
        "category": "concepts",
        "intro": "<p>Theft, the unlawful taking of another's property, is strictly prohibited by the eighth commandment (Ex. 20:15). Mosaic law required proportional restitution: fivefold for an ox slaughtered or sold after theft, fourfold for a sheep, and double for other property (Ex. 22:1-4). If the thief could not make restitution, he could be sold into indentured service. Man-stealing — kidnapping another person for sale — carried the death penalty (Ex. 21:16).</p><p>The prophets condemn theft alongside injustice and false dealing as symptoms of covenant unfaithfulness (Jer. 7:9; Hos. 4:2). The New Testament likewise prohibits theft (Eph. 4:28; 1 Cor. 6:10), with Paul's instruction that the former thief must instead labor honestly and give to those in need presenting a positive alternative rooted in transformed character rather than mere prohibition.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "theft", "isbe": "theft"},
        "key_refs": ["Exodus 20:15", "Exodus 22:1", "2 Samuel 12:6", "Ephesians 4:28"]
    },
    "theocracy": {
        "term": "Theocracy",
        "category": "concepts",
        "intro": "<p>Theocracy, a term coined by the Jewish historian Josephus, describes the form of government under which ancient Israel lived: direct rule by God through his law and his appointed representatives. From Sinai until the monarchy, Israel's constitution was the Mosaic covenant, and judges were raised up not as hereditary rulers but as divinely appointed deliverers in times of crisis. The law itself was understood as given by God and administered by priests and elders.</p><p>Samuel's warning when Israel demanded a king (1 Sam. 8:6-20) captures the theological tension: the desire for a human king like other nations was understood as a rejection of God's direct rule. Yet the Davidic covenant subsequently transformed the monarchy into a vehicle for theocratic governance rather than its replacement. The prophets consistently evaluated kings by the standard of covenant faithfulness rather than political success.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "theocracy", "isbe": "theocracy"},
        "key_refs": ["1 Samuel 8:6", "Deuteronomy 17:18"]
    },
    "theophilus": {
        "term": "Theophilus",
        "category": "people",
        "intro": "<p>Theophilus, whose name means <em>friend of God</em> or <em>lover of God</em>, is the person to whom Luke dedicated both his Gospel and the Acts of the Apostles (Luke 1:3; Acts 1:1). Luke addresses him as \"most excellent Theophilus\" in the Gospel, a title of honor suggesting he was a Roman official or person of significant social rank. He appears to have already received some instruction about Christianity (Luke 1:4) and may have been Luke's patron for the literary project.</p><p>Whether Theophilus was a specific individual, a symbolic name for all Christian readers (\"lover of God\"), or a code name for a Roman patron remains debated. The most natural reading treats him as a real named individual. Nothing further is recorded about him in Scripture, but he stands at the receiving end of the most extensive single contribution to the NT canon.</p>",
        "hitchcock_meaning": "friend of God",
        "source_ids": {"easton": "theophilus", "smith": "theophilus", "isbe": "theophilus"},
        "key_refs": ["Luke 1:3", "Acts 1:1"]
    },
    "thessalonians-epistles-to-the": {
        "term": "Thessalonians, Epistles to the",
        "category": "concepts",
        "intro": "<p>The two letters to the Thessalonians are generally considered the earliest surviving Pauline epistles, written from Corinth around AD 50-51, shortly after Paul's founding visit to Thessalonica during his second missionary journey (Acts 18:1-18). The First Epistle commends the young church's faith amid persecution, provides pastoral teaching on sexual ethics and brotherly love, and addresses concern about believers who had died before Christ's return (1 Thess. 4:13-18). It concludes with a vivid description of the parousia.</p><p>The Second Epistle corrects misunderstandings circulating in the church about the day of the Lord — some had apparently concluded it had already come. Paul responds by describing a prior apostasy and the revelation of the \"man of lawlessness\" that must precede the end (2 Thess. 2:1-12). Both letters reflect the eschatological urgency of the earliest church and Paul's concern for the practical holiness of his converts.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "thessalonians-epistles-to-the"},
        "key_refs": ["Acts 18:1", "1 Thessalonians 3:6", "1 Thessalonians 4:13", "2 Thessalonians 2:1"]
    },
    "thessalonica": {
        "term": "Thessalonica",
        "category": "places",
        "intro": "<p>Thessalonica, modern Thessaloniki, was a large and populous city on the Thermaic bay in the Roman province of Macedonia, serving as the capital of one of the four administrative districts of the province. Founded in 315 BC by Cassander and named for his wife, a half-sister of Alexander the Great, it became a prosperous commercial center under Roman rule. The city was governed by magistrates called politarchs — a title confirmed by inscriptions and once doubted by critics of Acts.</p><p>Paul and Silas visited Thessalonica on the second missionary journey, preaching in the synagogue for three Sabbaths and establishing a congregation before Jewish opposition forced their departure (Acts 17:1-9). The church Paul founded there received two of his earliest letters and is commended repeatedly for its faith and missionary influence throughout Macedonia and beyond (1 Thess. 1:7-8).</p>",
        "hitchcock_meaning": "victory against the Thessalonian",
        "source_ids": {"easton": "thessalonica", "smith": "thessalonica", "isbe": "thessalonica"},
        "key_refs": ["Acts 17:1", "1 Thessalonians 1:9", "Acts 17:5", "Philippians 4:16"]
    },
    "theudas": {
        "term": "Theudas",
        "category": "people",
        "intro": "<p>Theudas was a Jewish insurrectionist cited by the Pharisee Gamaliel in his speech before the Sanhedrin (Acts 5:36). Gamaliel argued that if the apostles' movement was merely human in origin, it would collapse as Theudas's revolt had — Theudas had gathered about four hundred followers but was killed, and his movement dissolved. The name may relate to a Greek root meaning <em>flowing</em> or <em>giver</em>.</p><p>The identification of this Theudas is historically complex, as Josephus mentions a Theudas who led a revolt around AD 44-46 — after Gamaliel's speech in Acts (set in the early 30s). The discrepancy has generated extensive discussion: either Josephus and Acts refer to different men, Josephus's chronology is imprecise, or Luke's use of Gamaliel's speech introduces a later detail. The episode illustrates the pattern of failed messianic movements in first-century Judea against which the apostolic mission is implicitly contrasted.</p>",
        "hitchcock_meaning": "flowing with water",
        "source_ids": {"easton": "theudas", "smith": "theudas", "isbe": "theudas"},
        "key_refs": ["Acts 5:36"]
    },
    "thick-clay": {
        "term": "Thick Clay",
        "category": "concepts",
        "intro": "<p>The phrase \"thick clay\" appears in Habakkuk 2:6, though the Revised Version more accurately renders the Hebrew as \"pledges\" — items taken as collateral from debtors. The context is a woe oracle against the Chaldeans (Babylonians), condemned for heaping up wealth through the exploitation of conquered nations. The imagery portrays an oppressor who accumulates pledges — the property of the poor held as debt securities — until the weight of injustice becomes crushing.</p><p>The Hebrew term involved appears to be a wordplay, and the precise rendering has been debated since antiquity. The theological point is clear: the Chaldeans who enriched themselves through oppression and debt-enslavement of their subjects would themselves become plunder. The passage is part of Habakkuk's series of five woe oracles against Babylonian hubris.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "thick-clay"},
        "key_refs": ["Habakkuk 2:6"]
    },
    "thieves-the-two": {
        "term": "Thieves, The Two",
        "category": "concepts",
        "intro": "<p>The two criminals crucified alongside Jesus (Luke 23:32-43) are described as robbers or malefactors in the Gospel accounts. Their contrasting responses to Jesus in Luke's account have become paradigmatic in Christian reflection: one reviled Jesus and demanded a miraculous rescue; the other confessed his own guilt, acknowledged Jesus's innocence and kingship, and received the extraordinary promise \"today you will be with me in paradise\" (Luke 23:43).</p><p>Matthew and Mark record both criminals reviling Jesus (Matt. 27:44; Mark 15:32), while Luke distinguishes them, a detail sometimes explained by a change of heart in one of them during the crucifixion. Christian tradition has named the penitent thief Dismas (or Dimas) and the impenitent thief Gestas, though these names are not scriptural. The episode has been widely read as a demonstration that salvation is available to the repentant until the final moment of life.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "thieves-the-two", "smith": "thieves-the-two"},
        "key_refs": ["Luke 23:32", "Luke 23:43", "Matthew 27:44"]
    },
    "thistle": {
        "term": "Thistle",
        "category": "concepts",
        "intro": "<p>Thistles are among the thorny plants that proliferate in Palestine and appear frequently in biblical metaphor. They are associated in Scripture with the curse upon the ground following the fall: \"thorns also and thistles shall it bring forth to thee\" (Gen. 3:18). Their appearance on neglected land became a symbol of desolation and divine judgment (Hos. 10:8). In Amaziah's confrontation with Jehoash, the parable of a thistle presuming to negotiate with a cedar captures the folly of disproportionate ambition (2 Kings 14:9).</p><p>Several Hebrew and Greek words are translated variously as thistles, thorns, or briers in English, and the distinction is not always maintained consistently. The many thorny plants of Palestine served as natural illustrations of the hardship of cursed ground, the danger of complacency, and the encroachment of spiritual neglect on what had been fruitful.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "thistle", "smith": "thistle"},
        "key_refs": ["Genesis 3:18", "2 Kings 14:9", "Hosea 10:8"]
    },
    "thomas": {
        "term": "Thomas",
        "category": "people",
        "intro": "<p>Thomas, one of the twelve apostles, bore a name meaning <em>twin</em> in Aramaic, rendered <em>Didymus</em> in Greek (John 11:16; 20:24). He is best known for his initial refusal to believe the resurrection without tactile evidence (John 20:24-25), a doubt resolved when Jesus appeared and invited him to touch his wounds, prompting Thomas's confession \"My Lord and my God\" (John 20:28) — among the most direct assertions of Christ's divinity in the Gospels.</p><p>Thomas also appears at the raising of Lazarus, urging his fellow disciples to go with Jesus even if it meant dying (John 11:16), and asking at the Last Supper how the disciples could know the way if they did not know where Jesus was going (John 14:5). This question occasioned Jesus's declaration \"I am the way, the truth, and the life.\" Church tradition assigns Thomas missionary work in India, a claim supported by the ancient Mar Thoma church there.</p>",
        "hitchcock_meaning": "a twin",
        "source_ids": {"easton": "thomas", "smith": "thomas", "isbe": "thomas"},
        "key_refs": ["Matthew 10:3", "John 11:16", "John 20:24", "John 20:28"]
    },
    "thorn": {
        "term": "Thorn",
        "category": "concepts",
        "intro": "<p>Thorns are among the most common plants of the Palestinian landscape and carry deep symbolic weight throughout Scripture. They first appear as part of the curse on the ground following Adam's sin (Gen. 3:18), and their prevalence on uncultivated land made them a natural image for judgment, neglect, and spiritual declension. The burning thornbush of Moses's call (Ex. 3:2) and the thorns of the vineyard in Isaiah's parable (Isa. 5:6) both exploit this imagery.</p><p>In the parable of the sower, thorns represent the cares of the world and the deceitfulness of riches that choke the word and render it unfruitful (Matt. 13:7, 22). The crown of thorns woven by Roman soldiers and placed on Jesus before his crucifixion (Matt. 27:29) is theologically dense, carrying overtones of the curse Jesus bears on behalf of humanity. Paul's \"thorn in the flesh\" (2 Cor. 12:7) uses the same imagery for a persistent personal affliction.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "thorn"},
        "key_refs": ["Genesis 3:18", "Matthew 13:7", "Matthew 27:29", "2 Corinthians 12:7"]
    },
    "thorn-in-the-flesh": {
        "term": "Thorn in the Flesh",
        "category": "concepts",
        "intro": "<p>Paul's \"thorn in the flesh\" is a persistent affliction he describes in 2 Corinthians 12:7-10, given to prevent pride following extraordinary revelations and visions. He prayed three times for its removal; God's response was \"My grace is sufficient for you, for my power is made perfect in weakness.\" Paul came to embrace the thorn as the occasion for experiencing divine strength in human frailty.</p><p>The precise nature of the thorn has been debated since antiquity. Proposals include a chronic eye disease (Gal. 4:15; 6:11), epilepsy, malaria, a speech impediment, severe headaches, or persistent spiritual opposition from an adversary. The description \"a messenger of Satan to buffet me\" introduces a personal-spiritual dimension. Whatever its nature, the passage has become the primary NT text on the theological meaning of unanswered prayer and suffering in the life of faith, and Paul's paradox — \"when I am weak, then I am strong\" — remains one of the most cited statements in Christian pastoral literature.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "thorn-in-the-flesh", "isbe": "thorn-in-the-flesh"},
        "key_refs": ["2 Corinthians 12:7", "2 Corinthians 12:9", "Galatians 4:15"]
    },
    "thousands": {
        "term": "Thousands",
        "category": "concepts",
        "intro": "<p>In Israelite tribal organization, the \"thousand\" (Hebrew <em>eleph</em>) functioned as a subdivision of the tribe used for military mustering, census-taking, and judicial organization. Moses appointed leaders of thousands, hundreds, fifties, and tens to share the burden of judgment (Ex. 18:21). Military units were organized by thousands with their commanders (Num. 31:14; 1 Sam. 8:12).</p><p>The large numbers in the Mosaic census lists (Num. 1; 26) have generated extensive scholarly discussion: some interpreters read <em>eleph</em> as a clan or unit designation rather than a literal count of one thousand, which would reduce the total population figures substantially. The term also appears in the blessings on Israel (Deut. 1:11; Ps. 68:17) and in the prophecy of Bethlehem as \"little among the thousands of Judah\" (Mic. 5:2), where it clearly means a tribal subdivision rather than a precise number.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "thousands"},
        "key_refs": ["Exodus 18:21", "Micah 5:2", "Numbers 1:16"]
    },
    "threshing": {
        "term": "Threshing",
        "category": "concepts",
        "intro": "<p>Threshing was the process of separating grain from its stalks, practiced in Palestine from the earliest agricultural period. After the harvest, sheaves were carried to the threshing floor — typically a flat, exposed rock surface on a hilltop where wind could carry away the chaff. Oxen were driven over the grain to break the stalks (Deut. 25:4), or a heavy threshing sledge studded with iron or sharp stones was pulled across it (Isa. 41:15).</p><p>Threshing-floors were communally significant sites. Boaz's encounter with Ruth occurred at his threshing floor (Ruth 3). David purchased Araunah's threshing floor on Mount Moriah as the site of his altar after the plague, and this site became the location of Solomon's temple (2 Sam. 24:18-25; 2 Chr. 3:1). Prophetic imagery frequently invokes threshing as a metaphor for divine judgment (Isa. 21:10; Jer. 51:33; Matt. 3:12).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "threshing", "smith": "threshing", "isbe": "threshing"},
        "key_refs": ["Deuteronomy 25:4", "Ruth 3:2", "2 Samuel 24:18", "Matthew 3:12"]
    },
    "threshold": {
        "term": "Threshold",
        "category": "concepts",
        "intro": "<p>The threshold, the stone sill of a doorway, carried particular significance in ancient Near Eastern culture as a liminal boundary between the sacred and profane, or between one household and another. The priests of Dagon refused to step on the threshold of the Philistine temple after the idol fell before the ark of God, establishing a threshold-avoidance custom (1 Sam. 5:5). Keepers of the threshold were important temple officials responsible for the gates and contributions (2 Kings 22:4; 25:18).</p><p>In Ezekiel's vision, the threshold of the temple becomes a locus of divine glory and judgment (Ezek. 10:4; 43:8). Zephaniah condemns those who leap over the threshold (Zeph. 1:9), possibly referring to the Philistine superstition or to a practice of Baal worship. The threshold thus functions as a boundary marker with both physical and theological dimensions in biblical texts.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "threshold", "smith": "threshold", "isbe": "threshold"},
        "key_refs": ["1 Samuel 5:5", "2 Kings 22:4", "Ezekiel 10:4", "Zephaniah 1:9"]
    },
    "throne": {
        "term": "Throne",
        "category": "concepts",
        "intro": "<p>The throne (Hebrew <em>kiss'e</em>) was the royal seat symbolizing sovereign authority and the exercise of judgment. The throne of David became the central theological symbol of God's covenant with Israel regarding a perpetual dynastic line: \"I will establish the throne of his kingdom forever\" (2 Sam. 7:13; Ps. 45:6). The ark of the covenant was understood as God's earthly throne between the cherubim.</p><p>In prophetic and apocalyptic literature, the throne of God dominates heavenly visions — Isaiah sees the Lord seated on a high and lofty throne (Isa. 6:1), and John's Revelation opens with a sustained vision of the divine throne surrounded by the four living creatures and twenty-four elders (Rev. 4:2-11). The New Testament announces that Jesus, risen and ascended, has taken his seat at the right hand of the throne of God (Heb. 12:2; Rev. 3:21), fulfilling the Davidic covenant in a cosmic register.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "throne", "smith": "throne", "isbe": "throne"},
        "key_refs": ["2 Samuel 7:13", "Psalms 45:6", "Isaiah 6:1", "Revelation 4:2"]
    },
    "thummim": {
        "term": "Thummim",
        "category": "concepts",
        "intro": "<p>The Thummim, always paired with the Urim, formed part of the sacred priestly equipment used for obtaining divine guidance on important decisions (Ex. 28:30; Lev. 8:8; Deut. 33:8). The name means <em>perfection</em> or <em>truth</em> (LXX renders it \"truth\"; Vulgate \"veritas\"). They were kept in or on the breastplate of the high priest and consulted when Israel needed a divine decision on critical matters.</p><p>The exact nature of the Urim and Thummim remains uncertain: they may have been lots, sacred stones, or inscribed tablets used to obtain binary yes/no answers from God. Their use appears to have declined after the early monarchy and is associated particularly with the period of the judges and early kings. The absence of the Urim in the post-exilic period (Ezra 2:63; Neh. 7:65) marks a significant change in the mode of divine communication, replaced increasingly by prophetic and scriptural interpretation.</p>",
        "hitchcock_meaning": "perfection; truth",
        "source_ids": {"easton": "thummim", "smith": "thummim", "isbe": "thummim"},
        "key_refs": ["Exodus 28:30", "Deuteronomy 33:8", "1 Samuel 28:6", "Ezra 2:63"]
    },
    "thunder": {
        "term": "Thunder",
        "category": "concepts",
        "intro": "<p>Thunder is described throughout Scripture as the voice of God (Job 40:9; Ps. 77:18; 104:7; John 12:29). It accompanied the theophany at Sinai when the law was given (Ex. 19:16) and was deployed as divine judgment against the Philistines at Mizpah during Samuel's time (1 Sam. 7:10). The seven thunders in Revelation 10:3-4 represent divine communications that John was commanded not to write down.</p><p>James and John received from Jesus the surname Boanerges, meaning <em>sons of thunder</em> (Mark 3:17), possibly reflecting their fiery temperament (Luke 9:54). In Israelite religion, thunder's association with divine power contrasted with the Canaanite storm god Baal's claim over rain and thunder, making it a theologically contested domain. The psalms celebrate YHWH's voice in the storm as supreme over all rival claimants (Ps. 29).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "thunder", "smith": "thunder", "isbe": "thunder"},
        "key_refs": ["Job 40:9", "Psalms 77:18", "1 Samuel 7:10", "Mark 3:17"]
    },
    "thyatira": {
        "term": "Thyatira",
        "category": "places",
        "intro": "<p>Thyatira was a city on the borders of Lydia and Mysia in Asia Minor, known today as Ak-hissar (\"white castle\"). It was home to a significant guild-based economy, particularly purple dyeing and bronze-working, and was known for its trade guilds. Lydia, the seller of purple cloth converted by Paul at Philippi, was from Thyatira (Acts 16:14), and her conversion inaugurated the gospel's entry into Europe.</p><p>Thyatira is one of the seven churches addressed in Revelation (Rev. 2:18-29), receiving a letter that commends the congregation for love, faith, service, and patient endurance while rebuking it for tolerating a prophetess called Jezebel who led members into sexual immorality and the eating of food sacrificed to idols. The letter's reference to trade guilds and their associated religious practices suggests the particular temptations faced by Christians in a guild-economy city. Its name may mean <em>a perfume</em> or <em>sacrifice of labor</em>.</p>",
        "hitchcock_meaning": "a perfume; sacrifice of labor",
        "source_ids": {"easton": "thyatira", "smith": "thyatira", "isbe": "thyatira"},
        "key_refs": ["Revelation 1:11", "Revelation 2:18", "Acts 16:14"]
    },
    "thyine-wood": {
        "term": "Thyine Wood",
        "category": "concepts",
        "intro": "<p>Thyine wood is mentioned only in Revelation 18:12 among the luxury goods traded by the merchants of Babylon, listed alongside gold, silver, jewels, and fine linen. It came from the sandarac tree (<em>Tetraclinis articulata</em> or <em>Callitris quadrivalvis</em>), a North African conifer valued in antiquity for its dark, fragrant, beautifully grained timber. Roman writers mention it as among the most expensive luxury cabinet-woods, used for furniture and decorative inlays by wealthy households.</p><p>Its inclusion in Revelation's catalogue of Babylon's luxury trade underscores both the extent of the ancient Roman long-distance luxury market and the moral critique implicit in the passage: the accumulated wealth of the imperial system, built on commerce reaching across continents, is presented as destined for sudden destruction. The list of goods in Revelation 18 ends with \"the souls of men\" (v. 13), placing human trafficking at the culmination of Babylon's trade in luxury.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "thyine-wood", "isbe": "thyine-wood"},
        "key_refs": ["Revelation 18:12"]
    },
    "tiberias": {
        "term": "Tiberias",
        "category": "places",
        "intro": "<p>Tiberias was a city on the western shore of the Sea of Galilee, founded by Herod Antipas around AD 20 and named in honor of the Emperor Tiberius, whose favor Herod sought. It served as Herod's administrative capital in Galilee. The city was built partly over an ancient cemetery, making it ritually unclean for observant Jews initially, though it eventually became an important center of Jewish learning after the destruction of Jerusalem.</p><p>The adjacent lake is called \"the Sea of Tiberias\" in the Gospel of John (6:1; 21:1). Though Jesus conducted extensive ministry around the shores of this lake, no Gospel narrative places him within the city of Tiberias itself. After AD 70, Tiberias became a major center of rabbinic Judaism, where the Jerusalem Talmud was later compiled. Its modern name, Tverya, preserves the ancient name.</p>",
        "hitchcock_meaning": "good vision; the navel",
        "source_ids": {"easton": "tiberias", "smith": "tiberias", "isbe": "tiberias"},
        "key_refs": ["John 6:1", "John 21:1"]
    },
    "tiberias-sea-of": {
        "term": "Tiberias, Sea of",
        "category": "places",
        "intro": "<p>The Sea of Tiberias is one of several names for the inland freshwater lake in northern Israel (John 6:1; 21:1), also known as the Sea of Galilee, the Sea of Gennesaret (Luke 5:1), and in the Old Testament as the Sea of Chinnereth (Num. 34:11; Josh. 12:3). Approximately thirteen miles long and eight miles wide, it lies some 680 feet below sea level and is fed primarily by the Jordan River.</p><p>The lake was the center of Jesus's Galilean ministry. He called his first disciples from among its fishermen (Matt. 4:18-22), calmed a storm on its waters (Matt. 8:23-27), walked on it (Matt. 14:25), and appeared to the disciples beside it after his resurrection (John 21). The fishing villages on its shores — Capernaum, Bethsaida, Magdala — were the primary settings of much of the Gospel narrative outside Jerusalem.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tiberias-sea-of", "isbe": "tiberias-sea-of"},
        "key_refs": ["John 6:1", "John 21:1", "Matthew 4:18", "Luke 5:1"]
    },
    "tiberius-caesar": {
        "term": "Tiberius Caesar",
        "category": "people",
        "intro": "<p>Tiberius Caesar (full name Tiberius Claudius Nero) was the second Roman Emperor, reigning from AD 14 until his death in AD 37. He is the Caesar explicitly named in Luke 3:1 as the emperor during whose reign John the Baptist began his ministry. His fifteenth regnal year (approximately AD 28-29) provides one of the key chronological anchors for the Gospel chronology.</p><p>Tiberius is also the unnamed \"Caesar\" to whom tribute was debated in the famous question posed to Jesus about paying taxes (Matt. 22:17-21; Mark 12:14-17). He governed the empire primarily through trusted subordinates during his later years of semi-retirement on Capri, a period that coincided with the ministry of Jesus and the early church. Pontius Pilate served as prefect of Judea under Tiberius's authority during the crucifixion.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tiberius-caesar"},
        "key_refs": ["Luke 3:1", "Matthew 22:17", "Matthew 22:21"]
    },
    "tibni": {
        "term": "Tibni",
        "category": "people",
        "intro": "<p>Tibni, son of Ginath, was the rival claimant to the throne of Israel who contested Omri's succession after the brief reign and suicide of Zimri (1 Kings 16:21-22). His name means <em>straw</em> or <em>hay</em>. A significant portion of the people supported Tibni while others followed Omri, creating a divided kingdom within the northern state that lasted several years before Tibni died and Omri emerged as sole ruler.</p><p>Scripture records nothing further about Tibni's character, policies, or the nature of his support base. His death (\"then Tibni died, and Omri reigned\") is recorded without elaboration. He represents a period of acute political instability in the northern kingdom following the military coup cycle — Baasha, Elah, Zimri, and then the Tibni-Omri division — that characterized Israel's early decades of monarchy.</p>",
        "hitchcock_meaning": "straw; hay",
        "source_ids": {"easton": "tibni", "smith": "tibni", "isbe": "tibni"},
        "key_refs": ["1 Kings 16:21", "1 Kings 16:22"]
    },
    "tidal": {
        "term": "Tidal",
        "category": "people",
        "intro": "<p>Tidal, styled \"king of nations\" (or \"king of Goiim\"), was one of the four kings who joined the coalition of Chedorlaomer against the five kings of the Sodom plain (Gen. 14:1-9). His name may mean <em>that breaks the yoke</em> or <em>knowledge of elevation</em>. He is generally identified with a Hittite king, possibly Tudhalia, mentioned in Assyrian and Hittite records, making this an early biblical contact with the Hittite world of Asia Minor.</p><p>The battle of Genesis 14, in which this coalition defeated the five Canaanite cities and carried Lot captive, prompted Abraham's rescue mission with his 318 trained men and the subsequent encounter with Melchizedek king of Salem (Gen. 14:14-20). Tidal himself is not mentioned beyond the coalition list; he serves to locate the episode within the broader ancient Near Eastern political landscape of the patriarchal period.</p>",
        "hitchcock_meaning": "that breaks the yoke; knowledge of elevation",
        "source_ids": {"easton": "tidal", "smith": "tidal", "isbe": "tidal"},
        "key_refs": ["Genesis 14:1", "Genesis 14:9"]
    },
    "tiglath-pileser-i": {
        "term": "Tiglath-pileser I",
        "category": "people",
        "intro": "<p>Tiglath-pileser I was the most celebrated monarch of the first Assyrian empire, reigning approximately 1115-1077 BC, though he is not mentioned by name in Scripture. He conducted military campaigns reaching as far as the Mediterranean coast, crossed the Euphrates twenty-eight times, and established Assyrian dominance over much of the ancient Near East during the period corresponding to the later judges of Israel.</p><p>His annals, preserved in cuneiform, document extensive campaigns into Syria, Phoenicia, and the regions bordering Israel. Though not a biblical figure, his reign provides crucial background context for understanding the rise of Assyrian power that would eventually devastate both Israel and Judah under his successors. His later namesake, Tiglath-pileser III, is the Assyrian king directly encountered in the biblical narrative.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tiglath-pileser-i"},
        "key_refs": []
    },
    "tiglath-pileser-iii": {
        "term": "Tiglath-pileser III",
        "category": "people",
        "intro": "<p>Tiglath-pileser III (reigned c. 745-727 BC), also known in Scripture as Pul, was one of the most powerful Assyrian kings and a decisive figure in biblical history. He exacted tribute from Menahem of Israel (2 Kings 15:19-20) and later, at the invitation of Ahaz of Judah, invaded the northern kingdom, capturing Galilean territories and deporting their populations to Assyria (2 Kings 15:29; 1 Chr. 5:26). This was the first wave of the Assyrian exile of Israel.</p><p>His campaigns fundamentally altered the political landscape of the ancient Near East, transforming Assyria into the dominant imperial power of the era. He employed systematic deportation of conquered populations as a policy tool to prevent rebellion — the practice that scattered the northern tribes. Isaiah's early prophecies of Assyrian judgment against both Israel and the surrounding nations are set against the background of Tiglath-pileser's campaigns. He is called Pul in his identity as king of Babylon (2 Kings 15:19; 1 Chr. 5:26).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tiglath-pileser-iii"},
        "key_refs": ["2 Kings 15:29", "2 Kings 16:5", "1 Chronicles 5:26", "2 Chronicles 26:6"]
    },
    "timaeus": {
        "term": "Timaeus",
        "category": "people",
        "intro": "<p>Timaeus was the father of blind Bartimaeus, whose healing by Jesus on the road near Jericho is recorded in Mark 10:46-52. The name is of Greek origin and means <em>defiled</em> or possibly <em>highly prized</em>. Mark is unique among the Gospel writers in preserving the father's name alongside the son's, suggesting Bartimaeus was known in the early Christian community — perhaps indicating he became a disciple or was otherwise remembered by name.</p><p>Bartimaeus's persistence in calling out \"Son of David, have mercy on me\" despite the crowd's attempts to silence him (Mark 10:48) became a celebrated example of faith and determined prayer in NT interpretation. Jesus's response — \"your faith has made you well\" — connects the healing to Bartimaeus's persistent trust rather than to anything in his background. He immediately followed Jesus on the way after his sight was restored.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "timaeus", "smith": "timaeus", "isbe": "timaeus"},
        "key_refs": ["Mark 10:46"]
    },
    "timbrel": {
        "term": "Timbrel",
        "category": "concepts",
        "intro": "<p>The timbrel (Hebrew <em>toph</em>) was a small hand-drum or tambourine, one of the oldest attested musical instruments in the ancient Near East. It consisted of a circular frame, sometimes with small cymbals or jingles attached, over which a membrane of skin was stretched, played by striking with the hand. Its antiquity is reflected in Laban's complaint that Jacob left without allowing him to send them away \"with joy and songs, with tabret and with harp\" (Gen. 31:27).</p><p>The timbrel appears consistently in contexts of joyful celebration, procession, and communal worship. Miriam led the women of Israel in timbrel-playing and dance after the crossing of the Red Sea (Ex. 15:20). Jephthah's daughter came out with timbrels and dancing to greet her father's return (Judg. 11:34). The Psalms call for praise with timbrel (Ps. 81:2; 149:3; 150:4), establishing it as a legitimate instrument of temple worship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "timbrel", "isbe": "timbrel"},
        "key_refs": ["Genesis 31:27", "Exodus 15:20", "Judges 11:34", "Psalms 150:4"]
    },
    "timnah": {
        "term": "Timnah",
        "category": "places",
        "intro": "<p>Timnah (also Timnath) was a town in the Shephelah region of Judah, assigned first to Dan and later recognized in Judah's territory (Josh. 15:10; 19:43). It was later seized by the Philistines (2 Chr. 28:18). The site is identified with Tell Batash in the Sorek valley, where significant archaeological excavations have confirmed occupation from the Late Bronze Age through the Iron Age.</p><p>Timnah is best known in the biblical narrative as the location where Samson took a Philistine wife (Judg. 14:1) and where he encountered the lion whose carcass later harbored a honeycomb — the basis of his famous riddle (Judg. 14:5-18). The name means <em>forbidding</em> or <em>portion</em> in Hitchcock's system. The site's location at the boundary between Israelite and Philistine territory made it a natural setting for the cross-cultural tensions of the Samson narrative.</p>",
        "hitchcock_meaning": "forbidding",
        "source_ids": {"easton": "timnah", "smith": "timnah", "isbe": "timnah"},
        "key_refs": ["Joshua 15:10", "Judges 14:1", "Judges 14:5", "2 Chronicles 28:18"]
    },
    "timnath": {
        "term": "Timnath",
        "category": "places",
        "intro": "<p>Timnath appears in the patriarchal narrative as the place near which Judah's sheepshearers were working when Tamar, disguised as a prostitute, positioned herself on the road to meet him (Gen. 38:12-14). The resulting union produced Perez and Zerah, ancestors of David. The location is also referenced in relation to Samson's Philistine wife (Judg. 14:1) and may overlap with or be near Timnah in the Shephelah.</p><p>The name means <em>image</em>, <em>figure</em>, or <em>enumeration</em> in Hitchcock's system. The multiple uses of similar place names (Timnah, Timnath, Timnath-serah, Timnath-heres) in different narrative contexts have led to some scholarly discussion about whether these represent a single site or distinct locations. The Timnath of Genesis 38 is usually placed in the hill country of Judah.</p>",
        "hitchcock_meaning": "image; figure; enumeration",
        "source_ids": {"easton": "timnath", "smith": "timnath", "isbe": "timnath"},
        "key_refs": ["Genesis 38:12", "Genesis 38:14", "Judges 14:1"]
    },
    "timnath-heres": {
        "term": "Timnath-heres",
        "category": "places",
        "intro": "<p>Timnath-heres, meaning <em>portion of the sun</em>, was the city in the hill country of Ephraim where Joshua was buried (Judg. 2:9). It is identified with Timnath-serah (Josh. 19:50; 24:30), the city Joshua received as his inheritance after the distribution of the land. The site is generally identified with Khirbet Tibnah in the central highlands, approximately seventeen miles southwest of Shechem.</p><p>The slight name variation — Timnath-serah (\"remaining portion\") versus Timnath-heres (\"portion of the sun\") — may reflect different scribal traditions or a later renaming. The location of Joshua's tomb made the site a significant memorial to Israel's greatest military leader after Moses. Josephus describes Joshua's tomb there as still visible in his day.</p>",
        "hitchcock_meaning": "image of the sun",
        "source_ids": {"easton": "timnath-heres", "isbe": "timnath-heres"},
        "key_refs": ["Judges 2:9"]
    },
    "timnath-serah": {
        "term": "Timnath-serah",
        "category": "places",
        "intro": "<p>Timnath-serah, meaning <em>remaining portion</em> or <em>abundant portion</em>, was the city in the hill country of Ephraim granted to Joshua as his personal inheritance after the distribution of the land to the tribes (Josh. 19:50). He built and settled there after the completion of the conquest, and was buried there at his death (Josh. 24:30). The site is identified with Khirbet Tibnah in the central highlands.</p><p>It is called Timnath-heres in Judges 2:9, a slight variation that has been explained as a reversal of the syllables or a difference between scribal traditions. The granting of Timnath-serah to Joshua after all the tribes received their portions reflects his selfless service — he requested his inheritance last among all Israel's leaders. The site's association with his burial gave it enduring memorial significance.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "timnath-serah", "isbe": "timnath-serah"},
        "key_refs": ["Joshua 19:50", "Joshua 24:30"]
    },
    "timnite": {
        "term": "Timnite",
        "category": "people",
        "intro": "<p>Timnite is the designation applied to Samson's Philistine father-in-law, identifying him as a man of Timnah rather than by personal name (Judg. 15:6). After Samson abandoned his Philistine wife following the riddle dispute, his father-in-law gave her to another man. When Samson returned and discovered this, the resulting conflict — Samson's foxes and firebrands burning the Philistine crops, and the Philistines' revenge killing of the Timnite and his daughter — escalated into a cycle of retaliatory violence.</p><p>The Timnite remains an unnamed figure whose decision to give his daughter to another man (Judg. 15:2) set off the violent chain of events that culminated in the burning of the Philistine grain, vineyards, and olive orchards. His fate illustrates the tragic consequences of the cross-cultural tensions that characterized Samson's story.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "timnite", "isbe": "timnite"},
        "key_refs": ["Judges 15:6"]
    },
    "timon": {
        "term": "Timon",
        "category": "people",
        "intro": "<p>Timon was one of the seven men chosen by the Jerusalem congregation to oversee the equitable distribution of food to Hellenistic widows who had been overlooked in the daily distribution (Acts 6:5). His name means <em>honorable</em> or <em>worthy</em>. He is listed third among the seven, all of whom bore Greek names, indicating they were drawn from the Hellenistic Jewish community — the group that had raised the complaint.</p><p>The selection of Timon and his colleagues represented an early form of ecclesiastical administration, with the apostles delegating practical service to free themselves for prayer and the ministry of the word (Acts 6:2-4). Beyond his listing in Acts 6:5, nothing further is recorded of Timon in Scripture. Later Christian tradition associates him with missionary work in various regions, but these accounts are not verifiable.</p>",
        "hitchcock_meaning": "honorable; worthy",
        "source_ids": {"easton": "timon", "smith": "timon", "isbe": "timon"},
        "key_refs": ["Acts 6:5"]
    },
    "timotheus": {
        "term": "Timotheus",
        "category": "people",
        "intro": "<p>Timotheus is the Greek form of the name Timothy, used interchangeably with the anglicized form in Acts and in the epistles. The Revised Version consistently renders it \"Timothy.\" He was the son of a Jewish mother and a Greek father from Lystra (Acts 16:1), converted through Paul's ministry and circumcised by Paul before joining the missionary team. He became one of Paul's most trusted companions and emissaries.</p><p>The name means <em>honoring God</em> or <em>valued of God</em>. Paul sent him as his representative to Thessalonica (1 Thess. 3:2), Corinth (1 Cor. 4:17), and Philippi (Phil. 2:19), and eventually entrusted him with oversight of the church at Ephesus (1 Tim. 1:3). Two of Paul's pastoral epistles are addressed to him. See also <em>Timothy</em>.</p>",
        "hitchcock_meaning": "honor of God; valued of God",
        "source_ids": {"easton": "timotheus", "smith": "timotheus", "isbe": "timotheus"},
        "key_refs": ["Acts 16:1"]
    },
    "timothy": {
        "term": "Timothy",
        "category": "people",
        "intro": "<p>Timothy was Paul's closest and most trusted co-worker in the gospel, a young man of mixed Jewish and Gentile heritage from Lystra in Lycaonia (Acts 16:1-3). His mother Eunice and grandmother Lois were Jewish Christians commended for their sincere faith (2 Tim. 1:5). Paul circumcised him before the second missionary journey to avoid giving offense among the Jewish communities they would visit. He is addressed as \"my true son in the faith\" (1 Tim. 1:2) and \"my beloved son\" (2 Tim. 1:2).</p><p>Timothy accompanied Paul through Macedonia, Achaia, and Asia, and served as his emissary to Thessalonica (1 Thess. 3:2), Corinth (1 Cor. 4:17), and Philippi (Phil. 2:19-23). He was with Paul during imprisonments and is co-sender of several epistles (2 Cor. 1:1; Col. 1:1; 1 Thess. 1:1). Paul left him at Ephesus to address false teaching (1 Tim. 1:3), and two of the pastoral epistles are addressed to him, the second calling him to Rome before Paul's anticipated execution.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "timothy", "smith": "timothy", "isbe": "timothy"},
        "key_refs": ["2 Timothy 1:5", "Acts 16:1", "1 Timothy 1:2", "2 Timothy 3:11"]
    },
    "timothy-first-epistle-to": {
        "term": "Timothy, First Epistle to",
        "category": "concepts",
        "intro": "<p>The First Epistle to Timothy is one of three pastoral epistles addressed to individual church workers rather than congregations. Written by Paul after departing Ephesus for Macedonia (1 Tim. 1:3), it charges Timothy to combat false teachers promoting myths and genealogies (1:4), provides instructions for public worship including the role of men and women (2:1-15), specifies qualifications for overseers and deacons (3:1-13), and addresses the care of widows, elders, and slaves (5:1-6:2).</p><p>Theologically, the letter centers on the importance of sound doctrine (\"healthy teaching\") as the foundation of church life and on the \"trustworthy saying\" that Christ Jesus came into the world to save sinners (1:15). The doxology of 1:17 — \"to the King eternal, immortal, invisible, the only God, be honor and glory for ever\" — is among Paul's most celebrated. The letter reflects the organizational challenges of established congregations in Paul's later period.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "timothy-first-epistle-to"},
        "key_refs": ["1 Timothy 1:2", "1 Timothy 3:1", "1 Timothy 4:7"]
    },
    "timothy-second-epistle-to": {
        "term": "Timothy, Second Epistle to",
        "category": "concepts",
        "intro": "<p>The Second Epistle to Timothy is widely regarded as Paul's final letter, written from Rome during a second imprisonment and in anticipation of his martyrdom (2 Tim. 4:6-8). More personal and urgent than the First Epistle, it calls Timothy to remain steadfast, to rekindle his gift (1:6), to suffer hardship as a good soldier (2:3), and to guard the deposit of faith committed to him (1:14). Paul asks Timothy to come quickly, bringing Mark and Paul's cloak and scrolls (4:11-13).</p><p>The letter contains some of the most celebrated passages in Paul's correspondence: the charge to \"preach the word; be ready in season and out of season\" (4:2), the famous declaration \"I have fought the good fight, I have finished the race, I have kept the faith\" (4:7), and the foundational statement that \"all Scripture is breathed out by God and profitable for teaching\" (3:16). It closes Paul's literary legacy on a note of personal courage and theological confidence.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "timothy-second-epistle-to"},
        "key_refs": ["2 Timothy 4:6", "2 Timothy 4:7", "2 Timothy 3:16", "Philippians 2:22"]
    },
    "tin": {
        "term": "Tin",
        "category": "concepts",
        "intro": "<p>Tin (Hebrew <em>bedil</em>) was one of the metals known to ancient Israel, listed alongside gold, silver, bronze, iron, and lead (Num. 31:22). As a component of bronze — an alloy of copper and tin — it was essential to ancient metallurgy from the Bronze Age onward. Tin was traded over long distances; the Phoenicians were particularly important traders of tin, obtaining it from Britain (the Cassiterides or \"tin islands\") and from Iberian Spain through their Mediterranean commercial networks.</p><p>Ezekiel employs tin in his metallurgical imagery: Israel is compared to a smelting furnace in which tin, lead, and other base metals are mixed with silver (Ezek. 22:18-20), conveying moral corruption. Ezekiel 27:12 mentions Tarshish as a source of tin traded with Tyre. The relative scarcity of tin compared to copper and iron in the ancient Near East gave Phoenician and later Greek traders a strategic commercial advantage.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tin", "smith": "tin", "isbe": "tin"},
        "key_refs": ["Numbers 31:22", "Ezekiel 22:18", "Ezekiel 27:12"]
    },
    "tinkling-ornaments": {
        "term": "Tinkling Ornaments",
        "category": "concepts",
        "intro": "<p>Tinkling ornaments were ankle-rings or anklets, typically of silver or gold, that produced a distinctive sound as the wearer walked (Isa. 3:18). They are listed among the ornaments and finery catalogued in Isaiah 3:18-24 in the prophet's oracle against the proud women of Jerusalem — a detailed inventory that includes headdresses, pendants, bracelets, veils, turbans, armlets, sashes, and perfume boxes.</p><p>The passage situates these ornaments within Isaiah's broader critique of the luxury and complacency of the Jerusalem aristocracy in the eighth century BC, which he read as symptoms of spiritual unfaithfulness and social injustice. The promised replacement — \"sackcloth\" for \"a rich robe,\" \"branding\" for \"beauty\" (Isa. 3:24) — inverts each ornament with a corresponding mark of judgment. Such ankle ornaments were common across the ancient Near East and have been recovered archaeologically from Palestinian sites.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tinkling-ornaments"},
        "key_refs": ["Isaiah 3:18"]
    },
    "tiphsah": {
        "term": "Tiphsah",
        "category": "places",
        "intro": "<p>Tiphsah was a city marking one boundary of Solomon's kingdom at its greatest extent (1 Kings 4:24), identified with the ancient Thapsacus on the Euphrates River in modern Syria. The name means <em>passage</em>, <em>leap</em>, or <em>ford</em>, reflecting its location at an important crossing of the Euphrates. It was one of the major fords on the Euphrates used by armies and caravans moving between Mesopotamia and the Levant.</p><p>The city appears again in a disturbing context: Menahem, king of Israel, attacked Tiphsah and its surrounding territory when it refused to open its gates to him, carrying out atrocities against its population (2 Kings 15:16). The two references thus bracket Tiphsah's biblical role — first as an emblem of Solomon's imperial reach to the Euphrates, then as the scene of a brutal episode in the northern kingdom's decline.</p>",
        "hitchcock_meaning": "passage; leap; step; the passover",
        "source_ids": {"easton": "tiphsah", "smith": "tiphsah", "isbe": "tiphsah"},
        "key_refs": ["1 Kings 4:24", "2 Kings 15:16"]
    },
    "tiras": {
        "term": "Tiras",
        "category": "people",
        "intro": "<p>Tiras was the youngest of the seven sons of Japheth in the Table of Nations (Gen. 10:2; 1 Chr. 1:5), making him a grandson of Noah and an ancestor of the nations descended from the Japhetic line. The Tiras clan or people have been variously identified by ancient and modern commentators as the Tyrsenoi (Tyrrhenians or Etruscans), the Thracians, or a seafaring Aegean people.</p><p>No biblical narrative involves Tiras beyond his listing in the genealogy. His inclusion in the Table of Nations reflects the ancient Israelite understanding that all known peoples descended from Noah's three sons, providing a theological framework for the diversity of nations. The identification of Tiras with the Etruscans or Thracians is suggested by similarity of names but remains speculative, as the Table of Nations reflects ancient Near Eastern geographic knowledge rather than modern ethnography.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tiras", "isbe": "tiras"},
        "key_refs": ["Genesis 10:2", "1 Chronicles 1:5"]
    },
    "tires": {
        "term": "Tires",
        "category": "concepts",
        "intro": "<p>Tires were head-ornaments, turbans, or decorative headdresses (Hebrew <em>pe'er</em>, meaning \"beauty\" or \"ornament of the head\"). In Ezekiel 24:17, God instructs the prophet not to remove his tire (headdress) or cover his lips in mourning upon the death of his wife, as a sign-act to Israel: just as Ezekiel would not openly mourn, so the people would be too stunned by the fall of the temple — \"the desire of your eyes\" — to perform traditional mourning rites (Ezek. 24:23).</p><p>Tires also appear in Isaiah's catalogue of women's finery (Isa. 3:18) and are associated with bridegroom adornment (Isa. 61:10). The word reflects the importance of head-covering as a marker of status, dignity, and festive occasion in ancient Israelite culture. Removing the headdress was a mark of grief or humiliation, making Ezekiel's instruction to keep his tire a deliberately counter-intuitive sign of coming judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tires"},
        "key_refs": ["Ezekiel 24:17", "Ezekiel 24:23", "Isaiah 3:18", "Isaiah 61:10"]
    },
    "tirhakah": {
        "term": "Tirhakah",
        "category": "people",
        "intro": "<p>Tirhakah was the last king of Egypt from the Ethiopian (twenty-fifth) dynasty, who reigned approximately 690-664 BC. His name may mean <em>inquirer</em> or <em>examiner</em>. He appears in Scripture in connection with Sennacherib's campaign against Judah during Hezekiah's reign: news of Tirhakah's approach against Sennacherib's army prompted the Assyrian king to send a threatening letter to Hezekiah urging surrender (2 Kings 19:9; Isa. 37:9).</p><p>Hezekiah's response was to take Sennacherib's letter to the temple and spread it before God in prayer, which occasioned Isaiah's oracle of deliverance and the subsequent destruction of 185,000 Assyrian troops (2 Kings 19:14-35). Tirhakah's historical relationship to Sennacherib's campaign of 701 BC has been debated by scholars, as he may not have been pharaoh at that exact date. Nonetheless, his intervention or threatened intervention shaped one of the most dramatic episodes of the eighth-century prophetic period.</p>",
        "hitchcock_meaning": "inquirer; examiner; dull observer",
        "source_ids": {"easton": "tirhakah", "isbe": "tirhakah"},
        "key_refs": ["2 Kings 19:9", "Isaiah 37:9"]
    },
    "tirshatha": {
        "term": "Tirshatha",
        "category": "concepts",
        "intro": "<p>Tirshatha was a title of Persian origin applied to the governor of Judea under Persian rule, meaning approximately <em>his fear</em> or <em>severity</em> — conveying the governor's authority as the representative of the king. It is applied to Zerubbabel, the leader of the first return from exile (Ezra 2:63; Neh. 7:65, 70), and to Nehemiah, who served as governor during the wall-rebuilding period (Neh. 8:9; 10:1).</p><p>The title designates a high civil dignity below the rank of satrap, representing accountability to the Persian crown rather than full autonomous authority. The Tirshatha had responsibility for civil administration, tax collection, and, in Nehemiah's case, military oversight of the province of Judah. Its use for Zerubbabel underscores the political dimension of the return from exile — the restoration of Judean self-governance within the framework of Persian imperial administration.</p>",
        "hitchcock_meaning": "a governor",
        "source_ids": {"easton": "tirshatha", "smith": "tirshatha", "isbe": "tirshatha"},
        "key_refs": ["Ezra 2:63", "Nehemiah 7:65", "Nehemiah 8:9", "Nehemiah 10:1"]
    },
    "tirza": {
        "term": "Tirza",
        "category": "places",
        "intro": "<p>Tirza (Tirzah) served a dual role in Scripture. As a city, it was an ancient Canaanite royal seat captured by Joshua (Josh. 12:24) that became the capital of the northern kingdom of Israel from Jeroboam I until Omri moved the capital to Samaria (1 Kings 14:17; 15:21; 16:6). Its beauty is celebrated in Song of Solomon 6:4, where the beloved is compared to both Tirzah and Jerusalem. As a name, Tirza was one of the five daughters of Zelophehad of Manasseh who successfully petitioned Moses for their father's inheritance (Num. 27:1).</p><p>The city's location is generally identified with Tell el-Far'ah North, approximately seven miles northeast of Shechem, where excavations have confirmed occupation from Chalcolithic through Iron Age periods. Its function as the northern kingdom's first capital gives it significance in the early history of the divided monarchy. The name means <em>pleasantness</em> or <em>delight</em>.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tirza", "smith": "tirza", "isbe": "tirza"},
        "key_refs": ["Joshua 12:24", "1 Kings 14:17", "1 Kings 16:6", "Song of Solomon 6:4"]
    },
    "tishbite": {
        "term": "Tishbite",
        "category": "people",
        "intro": "<p>Tishbite is the designation of Elijah the prophet, indicating his origin from Tishbe (or Thisbe) in Gilead, east of the Jordan (1 Kings 17:1). The epithet marks him as a foreigner in the Israelite heartland — a man from the Transjordanian highlands who appeared suddenly before King Ahab to pronounce judgment. The name of his hometown is linked in Hitchcock's lexicon with meanings related to <em>captivity</em>.</p><p>As \"Elijah the Tishbite,\" he is one of the most dramatic figures in the Hebrew prophets: the announcer of a three-year drought (1 Kings 17:1), the challenger of the prophets of Baal on Mount Carmel (1 Kings 18), the despairing fugitive who heard the still small voice at Horeb (1 Kings 19:12), and the prophet taken up in a whirlwind without dying (2 Kings 2:11). The NT connects him to John the Baptist and to the spirit of prophetic confrontation with corrupt power.</p>",
        "hitchcock_meaning": "that makes captive",
        "source_ids": {"easton": "tishbite", "isbe": "tishbite"},
        "key_refs": ["1 Kings 17:1", "1 Kings 21:17", "2 Kings 2:11", "Malachi 4:5"]
    },
    "tisri": {
        "term": "Tisri",
        "category": "concepts",
        "intro": "<p>Tisri (Tishri) was the first month of the Jewish civil year and the seventh month of the sacred (ecclesiastical) year, corresponding approximately to September-October. It is also called Ethanim in the older nomenclature (1 Kings 8:2). The dedication of Solomon's temple took place \"in the month Ethanim, which is the seventh month\" (1 Kings 8:2), marking Tisri as a month of supreme religious significance.</p><p>Tisri was the most ceremonially dense month in the Hebrew calendar, containing three major observances: the Feast of Trumpets on the first day (Num. 29:1; Lev. 23:24), the Day of Atonement on the tenth day (Lev. 23:27), and the Feast of Tabernacles beginning on the fifteenth day (Lev. 23:34). The concentration of these major observances in a single month made Tisri the spiritual climax of the Israelite year, centering on repentance, atonement, and joyful celebration of God's provision.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tisri"},
        "key_refs": ["1 Kings 8:2", "Leviticus 23:24", "Leviticus 23:27", "Leviticus 23:34"]
    },
    "tithe": {
        "term": "Tithe",
        "category": "concepts",
        "intro": "<p>A tithe is a tenth part of one's income, produce, or possessions consecrated to God. The practice predates the Mosaic law: Abraham gave tithes to Melchizedek, king of Salem, from the spoils of battle (Gen. 14:20; Heb. 7:6), and Jacob vowed to give God a tenth of all he possessed (Gen. 28:22). The Mosaic law codified tithing on an elaborate basis: a first tithe supported the Levites (Num. 18:21-26), who in turn gave a tithe of their tithe to the priests; a second tithe was consumed at Jerusalem in festival celebration (Deut. 14:22-27); and in the third and sixth years, the tithe was directed to the poor and the resident alien (Deut. 14:28-29).</p><p>The prophets, particularly Malachi, treated the withholding of tithes as a form of robbing God and called for faithful giving as a condition for restored blessing (Mal. 3:8-10). Jesus acknowledged tithing while rebuking the Pharisees for neglecting justice, mercy, and faithfulness (Matt. 23:23). The NT does not codify a tithe percentage but calls for generous, cheerful, proportional giving (2 Cor. 9:6-7).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tithe", "isbe": "tithe"},
        "key_refs": ["Genesis 14:20", "Leviticus 27:30", "Numbers 18:21", "Malachi 3:8"]
    },
    "tittle": {
        "term": "Tittle",
        "category": "concepts",
        "intro": "<p>A tittle is the small stroke, serif, or decorative flourish used to distinguish similar-looking letters in the Hebrew script. In Matthew 5:18, Jesus declares that \"not one jot or one tittle shall pass from the law until all is fulfilled\" — the jot being the smallest Hebrew letter (yod) and the tittle the smallest marking on a letter. The statement is among the strongest affirmations of biblical authority and verbal precision in the Gospels.</p><p>Luke 16:17 records a parallel saying: \"It is easier for heaven and earth to pass away than for one tittle of the law to fail.\" Together these statements establish the permanence and completeness of Scripture down to its minutest written details. The context in Matthew is the Sermon on the Mount, where Jesus goes on to demonstrate that he fulfills the law by deepening rather than abolishing its demands (Matt. 5:21-48).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tittle", "isbe": "tittle"},
        "key_refs": ["Matthew 5:18", "Luke 16:17"]
    },
    "titus": {
        "term": "Titus",
        "category": "people",
        "intro": "<p>Titus was a Gentile Christian and trusted co-worker of Paul, who accompanied Paul and Barnabas to the Jerusalem council (Gal. 2:1-3) where Paul resisted pressure to have him circumcised, establishing him as a test case for Gentile freedom from the law. His name means <em>honorable</em> or <em>pleasing</em>. He served as Paul's emissary to Corinth during a period of intense conflict, successfully mediating the dispute and collecting the offering for Jerusalem (2 Cor. 8:6; 12:18).</p><p>Paul left Titus on Crete to \"set in order what remains and appoint elders in every town\" (Tit. 1:5), suggesting significant organizational responsibility in a newly planted church context. The Epistle to Titus addresses this role. Titus later rejoined Paul, apparently in Rome, and was sent to Dalmatia (2 Tim. 4:10). He is notable as a Gentile believer whose case proved the gospel's sufficiency apart from circumcision.</p>",
        "hitchcock_meaning": "pleasing",
        "source_ids": {"easton": "titus", "smith": "titus", "isbe": "titus"},
        "key_refs": ["Galatians 2:1", "2 Corinthians 8:6", "Titus 1:5", "2 Timothy 4:10"]
    },
    "titus-epistle-to": {
        "term": "Titus, Epistle to",
        "category": "concepts",
        "intro": "<p>The Epistle to Titus is one of the three pastoral epistles, addressed to Titus who had been left by Paul to organize the churches of Crete (Tit. 1:5). Written at approximately the same time as First Timothy, it shares similar concerns for sound doctrine and ordered church life. The letter specifies qualifications for elders (1:6-9), addresses the particular pastoral challenges of Cretan culture (1:10-16), provides instructions for various groups — older men, older women, younger women, young men, and slaves (2:1-10) — and grounds the call to godly living in the grace of God revealed in Christ.</p><p>Theologically, the letter contains one of the most concise statements of salvation by grace: \"But when the goodness and loving kindness of God our Savior appeared, he saved us, not because of works done by us in righteousness, but according to his own mercy\" (Tit. 3:4-5). The phrase \"God our Savior\" applied both to the Father (1:3) and to Jesus Christ (1:4; 3:6) reflects the letter's high Christology.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "titus-epistle-to", "smith": "titus-epistle-to", "isbe": "titus-epistle-to"},
        "key_refs": ["Titus 1:4", "Titus 1:5", "Titus 2:11", "Titus 3:4"]
    },
    "tob-the-land-of": {
        "term": "Tob, the Land of",
        "category": "places",
        "intro": "<p>The land of Tob was a district east of the Jordan River, located approximately thirteen miles southeast of the Sea of Galilee in the region of Gilead. To this region Jephthah fled after being expelled by his half-brothers from his home in Gilead, and there he gathered a band of raiders (Judg. 11:3, 5). When the Ammonites threatened Israel, the elders of Gilead came to Tob to recall Jephthah as their military leader, a negotiation that gave rise to his ill-fated vow (Judg. 11:30-31).</p><p>Tob also appears as a source of Aramean mercenaries hired by the Ammonites in their war against David (2 Sam. 10:6, 8). The region's men for hire suggest it was a semi-independent frontier area with a warrior population not firmly integrated into Israelite territorial control. The name means <em>good</em> in Hebrew, though the events associated with the land involve considerable tragedy.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tob-the-land-of", "isbe": "tob-the-land-of"},
        "key_refs": ["Judges 11:3", "Judges 11:5", "2 Samuel 10:6", "2 Samuel 10:8"]
    },
    "tob-adonijah": {
        "term": "Tob-adonijah",
        "category": "people",
        "intro": "<p>Tob-adonijah was a Levite sent by King Jehoshaphat on a teaching mission throughout Judah in the third year of his reign (2 Chr. 17:8). His name means <em>my good God</em> or <em>the Lord is my good master</em>. He is listed in a company of princes, Levites, and priests dispatched with a copy of the Book of the Law to instruct the people of Judah in the requirements of the covenant.</p><p>This educational initiative represents one of Jehoshaphat's significant religious reforms, aimed at rooting out the idolatry of the previous generation and establishing covenant faithfulness among the people. Tob-adonijah's inclusion in the list of teachers reflects the Levitical mandate to serve as instructors of the law to the broader population (Deut. 33:10; Neh. 8:7-8).</p>",
        "hitchcock_meaning": "my good God; the goodness of the Lord",
        "source_ids": {"easton": "tob-adonijah", "isbe": "tob-adonijah"},
        "key_refs": ["2 Chronicles 17:8"]
    },
    "tobiah": {
        "term": "Tobiah",
        "category": "people",
        "intro": "<p>Tobiah the Ammonite was a powerful official who, alongside Sanballat the Horonite and Geshem the Arab, actively opposed Nehemiah's project to rebuild the walls of Jerusalem (Neh. 2:10, 19). His name means <em>the Lord is good</em>. Despite his Ammonite identification and hostility to the restoration project, Tobiah had extensive family and social connections with prominent Jewish households in Jerusalem through his son's marriage into the family of Shecaniah (Neh. 6:17-18).</p><p>These connections provided him with a network of intelligence inside the city and led Nehemiah to distrust certain leading men who were passing information to Tobiah (Neh. 6:19). After Nehemiah's return to Persia, Tobiah was actually given a room in the temple storerooms by the priest Eliashib — a desecration Nehemiah remedied upon his return by throwing Tobiah's furniture out and purifying the chamber (Neh. 13:4-9). He remains the primary antagonist of the Nehemiah memoir.</p>",
        "hitchcock_meaning": "the Lord is good",
        "source_ids": {"easton": "tobiah", "smith": "tobiah", "isbe": "tobiah"},
        "key_refs": ["Nehemiah 2:10", "Nehemiah 6:17", "Nehemiah 13:4"]
    },
    "tobijah": {
        "term": "Tobijah",
        "category": "people",
        "intro": "<p>Tobijah appears in two distinct biblical contexts. (1.) A Levite sent by Jehoshaphat throughout Judah to teach the law to the people (2 Chr. 17:8), listed alongside Tob-adonijah and other teachers in this educational mission — one of Jehoshaphat's key religious reforms. (2.) A man among those who returned from Babylon, mentioned alongside Heldai, Jedaiah, and Hen as recipients from whose silver and gold crowns were to be made for Joshua the high priest as a messianic sign-act (Zech. 6:10, 14).</p><p>The name means <em>the Lord is good</em>, identical in meaning to Tobiah. The Levite's role illustrates the teaching function central to the Levitical calling; the post-exilic figure illustrates the connection between the returnees and the prophetic hopes associated with Joshua the high priest in Zechariah's night visions.</p>",
        "hitchcock_meaning": "the Lord is good",
        "source_ids": {"easton": "tobijah", "smith": "tobijah", "isbe": "tobijah"},
        "key_refs": ["2 Chronicles 17:8", "Zechariah 6:10"]
    },
    "tochen": {
        "term": "Tochen",
        "category": "places",
        "intro": "<p>Tochen was a town assigned to the tribe of Simeon, located in the Negev region of southern Judah (1 Chr. 4:32). The name means <em>middle</em> or <em>measure</em>. It appears in a list of Simeonite settlements along with Etam, Ain, Rimmon, and Ashan, and has not been securely identified with any modern archaeological site.</p><p>Simeon's tribal territory was embedded within Judah's allotment (Josh. 19:1), and over time many Simeonite towns were absorbed into Judah proper. Tochen's single appearance in a territorial list makes it difficult to reconstruct any historical significance beyond its role as a settlement marker for the Simeonite clan structure in the early Israelite period.</p>",
        "hitchcock_meaning": "middle",
        "source_ids": {"easton": "tochen", "smith": "tochen", "isbe": "tochen"},
        "key_refs": ["1 Chronicles 4:32"]
    },
    "togarmah": {
        "term": "Togarmah",
        "category": "people",
        "intro": "<p>Togarmah was a son of Gomer and grandson of Japheth in the Table of Nations (Gen. 10:3; 1 Chr. 1:6), and also the name of the region or people descended from him. The name means <em>which is all bone</em> in Hitchcock's lexicon. His descendants are identified in Ezekiel as traders supplying horses, war-horses, and mules to Tyre from \"Beth-togarmah of the far north\" (Ezek. 27:14), suggesting a location in eastern Asia Minor or the Caucasus region.</p><p>Togarmah also appears in Ezekiel's prophecy of Gog and Magog as one of the northern nations that will join the coalition against Israel in the last days (Ezek. 38:6). Later Jewish and Christian interpreters identified Togarmah with various peoples including Armenians, Turks, or Phrygians, based on the similarity of the name and the northern geographic orientation. No individual narrative is attached to Togarmah beyond genealogical and prophetic mentions.</p>",
        "hitchcock_meaning": "which is all bone",
        "source_ids": {"easton": "togarmah", "smith": "togarmah", "isbe": "togarmah"},
        "key_refs": ["Genesis 10:3", "Ezekiel 27:14", "Ezekiel 38:6"]
    },
    "tohu": {
        "term": "Tohu",
        "category": "people",
        "intro": "<p>Tohu was an ancestor of Samuel the prophet, appearing in the genealogy given in 1 Samuel 1:1. His name means <em>that lives</em> or <em>that declares</em> in Hitchcock's system. He is the same individual called Nahath in 1 Chronicles 6:26 and Toah in 1 Chronicles 6:34, with the variant spellings reflecting different textual traditions in the parallel genealogical lists.</p><p>His significance lies entirely in his genealogical role as a link in the chain connecting Samuel to the tribe of Levi through the line of Kohath. The apparent discrepancy between his Ephraimite identification in 1 Samuel 1:1 and his Levitical lineage in Chronicles is generally explained by Elkanah's family residing in Ephraim while being of Levitical descent — a common situation given the Levites' dispersal throughout the tribes rather than possession of a single tribal territory.</p>",
        "hitchcock_meaning": "that lives; that declares",
        "source_ids": {"easton": "tohu", "smith": "tohu", "isbe": "tohu"},
        "key_refs": ["1 Samuel 1:1"]
    },
    "toi": {
        "term": "Toi",
        "category": "people",
        "intro": "<p>Toi (also written Tou, 1 Chr. 18:9) was the king of Hamath, the Aramean city-state on the Orontes River in Syria. When David defeated Hadadezer king of Zobah — with whom Toi had long been at war — Toi sent his son Joram (also called Hadoram) to David with congratulations and gifts of silver, gold, and bronze (2 Sam. 8:9-10; 1 Chr. 18:9-10). His name means <em>who wanders</em> or <em>error</em> in Hitchcock's lexicon.</p><p>The diplomatic exchange illustrates the international recognition of David's military dominance and the shifting alliances of the Levantine city-states in the tenth century BC. David consecrated the metals from Toi's gifts to the Lord (2 Sam. 8:11), along with the plunder from his other campaigns. Toi's proactive diplomacy prevented a potentially costly confrontation with the newly dominant Israelite kingdom.</p>",
        "hitchcock_meaning": "who wanders",
        "source_ids": {"easton": "toi", "smith": "toi", "isbe": "toi"},
        "key_refs": ["2 Samuel 8:9", "2 Samuel 8:10", "1 Chronicles 18:9"]
    },
    "tola": {
        "term": "Tola",
        "category": "people",
        "intro": "<p>Tola appears in two distinct biblical contexts. (1.) The eldest son of Issachar (Gen. 46:13; Num. 26:23; 1 Chr. 7:1-2) and the ancestor of the Tolaite clan, one of the principal subdivisions of the tribe of Issachar whose numbers are recorded in both Mosaic census lists. His name means <em>worm</em>, <em>grub</em>, or <em>scarlet</em> in Hitchcock's system, related to the crimson dye-producing worm used in tabernacle furnishings. (2.) A judge of Israel from the tribe of Issachar, son of Puah and grandson of Dodo (Judg. 10:1-2), who delivered Israel after Abimelech and judged for twenty-three years, dwelling at Shamir in Mount Ephraim.</p><p>The minor judge Tola is mentioned only briefly without any military campaign or major narrative. His lengthy judgeship of twenty-three years suggests a period of stability and quiet administration rather than the dramatic deliverances associated with Gideon, Jephthah, or Samson. He was buried at Shamir.</p>",
        "hitchcock_meaning": "worm; grub; scarlet",
        "source_ids": {"easton": "tola", "smith": "tola", "isbe": "tola"},
        "key_refs": ["Genesis 46:13", "Numbers 26:23", "Judges 10:1", "Judges 10:2"]
    },
    "tolad": {
        "term": "Tolad",
        "category": "places",
        "intro": "<p>Tolad was a town of the tribe of Simeon in the southern portion of Judah (1 Chr. 4:29), identified with Eltolad in Joshua 15:30 and 19:4. The name means <em>a generation</em> or <em>birth</em>. Like other Simeonite towns, it was located within Judah's territorial allotment, reflecting Simeon's dispersal among the tribes as foretold in Jacob's blessing (Gen. 49:7).</p><p>Tolad appears only in territorial lists and genealogical registers, with no narrative events attached to it. Its identification with Eltolad allows it to be located in the Negev region, but the exact site has not been archaeologically confirmed. The Simeonite towns of the far south eventually became integrated into Judah, and Tolad/Eltolad likely followed this pattern.</p>",
        "hitchcock_meaning": "a generation",
        "source_ids": {"easton": "tolad", "smith": "tolad", "isbe": "tolad"},
        "key_refs": ["1 Chronicles 4:29"]
    },
    "tolaites": {
        "term": "Tolaites",
        "category": "people",
        "intro": "<p>The Tolaites were the descendants of Tola, the eldest son of Issachar (Num. 26:23; 1 Chr. 7:1-2). They formed one of the four principal clans of the tribe of Issachar recorded in the Mosaic census lists. In the second census at the plains of Moab, the Tolaites are listed with their sub-clans, representing a significant portion of the tribe's counted population.</p><p>The Chronicles genealogy (1 Chr. 7:2) records the Tolaite clan as having 22,600 mighty warriors in the time of David — a number that reflects their continued importance within the tribal structure. The Tolaites represent the ongoing identity of Tola's lineage across the centuries from the patriarchal period through the early monarchy, illustrating the persistence of tribal genealogical organization in Israelite society.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tolaites", "isbe": "tolaites"},
        "key_refs": ["Numbers 26:23", "1 Chronicles 7:1", "1 Chronicles 7:2"]
    },
    "toll": {
        "term": "Toll",
        "category": "concepts",
        "intro": "<p>Toll was one of the revenues levied by the Persian imperial administration on goods and commerce (Ezra 4:13; 7:24). The Persian system distinguished between tribute (Hebrew <em>minda</em>, a land tax), custom (<em>belo</em>, a tax on goods), and toll (<em>halakh</em>, a transit tax on roads and crossings). The opponents of the Jerusalem restoration warned Artaxerxes that if the city were rebuilt, these revenues would cease (Ezra 4:13).</p><p>The exemption of priests, Levites, and temple servants from all three categories of taxation granted by Artaxerxes (Ezra 7:24) was a significant economic privilege illustrating the Persian policy of supporting indigenous religious institutions as a tool of provincial governance. In the NT period, toll collection at road stations and customs posts was a major feature of Roman fiscal administration, and toll-collectors (publicans) are prominent in Gospel narratives as a social category associated with both wealth and religious stigma.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "toll", "isbe": "toll"},
        "key_refs": ["Ezra 4:13", "Ezra 7:24"]
    },
    "tombs": {
        "term": "Tombs",
        "category": "concepts",
        "intro": "<p>The tombs of the Hebrews were generally rock-cut chambers or natural caves sealed with a large rolling or lifting stone (Gen. 29:2-3; Matt. 27:60). Family tombs were highly valued and passed between generations: Abraham's purchase of the Cave of Machpelah as a permanent burial place for Sarah established a pattern of family sepulchre ownership (Gen. 23). The patriarchs, Rachel, and later the kings of Israel had designated burial places considered part of their legacy.</p><p>Royal burials in the \"city of David\" were a mark of honor, and the location of David's tomb remained known to Jerusalem's inhabitants centuries later (Acts 2:29). Tombs were whitewashed annually before Passover to warn travelers of ritual uncleanness from contact with the dead — a practice Jesus used metaphorically to describe the Pharisees' outward righteousness concealing inner corruption (Matt. 23:27). The NT records that Jesus was laid in a new tomb, never previously used, hewn from rock and sealed with a stone (Matt. 27:60; John 19:41).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tombs", "smith": "tombs", "isbe": "tombs"},
        "key_refs": ["Genesis 23:9", "2 Kings 9:28", "Matthew 27:60", "Acts 2:29"]
    },
    "tongues-confusion-of": {
        "term": "Tongues, Confusion of",
        "category": "concepts",
        "intro": "<p>The confusion of tongues at Babel is the divine intervention by which the originally unified human language was fragmented into many languages, dispersing across the earth the peoples who had gathered on the plain of Shinar to build a city and tower \"with its top in the heavens\" (Gen. 11:1-9). God's stated reason was to prevent the unchecked fulfillment of human ambition: \"Nothing that they propose to do will now be impossible for them.\" The word Babel became synonymous with confusion and incomprehensibility.</p><p>The event functions in the biblical narrative as the explanation for the diversity of human languages and the dispersal of nations described in Genesis 10's Table of Nations — the two accounts being complementary rather than contradictory. Christian interpreters from the NT period onward have read Pentecost (Acts 2:1-11), where the disciples spoke in the native languages of diaspora Jews from many nations, as a partial reversal of Babel's linguistic and social fragmentation, anticipating an eschatological unity of all peoples before God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tongues-confusion-of", "smith": "tongues-confusion-of", "isbe": "tongues-confusion-of"},
        "key_refs": ["Genesis 11:1", "Genesis 11:7", "Acts 2:4"]
    },
    "tongues-gift-of": {
        "term": "Tongues, Gift of",
        "category": "concepts",
        "intro": "<p>The gift of tongues was the supernatural ability to speak in languages not previously learned, granted by the Holy Spirit at Pentecost (Acts 2:4) in fulfillment of Jesus's promise (Mark 16:17). At that occasion the disciples spoke in the native languages of diaspora Jews from Parthia, Media, Elam, Mesopotamia, and many other regions (Acts 2:9-11), enabling each to hear the gospel in their own tongue. The same gift appeared among Cornelius's household (Acts 10:46) and the Ephesian disciples (Acts 19:6).</p><p>Paul discusses the gift at length in 1 Corinthians 12-14, distinguishing it from prophecy and ranking it below prophecy in terms of congregational edification. He establishes regulations for its use in worship: no more than three speakers in tongues per meeting, each followed by interpretation; otherwise the tongue-speaker should keep silent (1 Cor. 14:27-28). The nature of the tongues — whether human languages or ecstatic speech — has been debated throughout church history. Paul's reference to \"tongues of angels\" (1 Cor. 13:1) suggests the possibility of both.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tongues-gift-of", "smith": "tongues-gift-of", "isbe": "tongues-gift-of"},
        "key_refs": ["Acts 2:4", "Mark 16:17", "1 Corinthians 14:2", "1 Corinthians 14:27"]
    },
    "tooth": {
        "term": "Tooth",
        "category": "concepts",
        "intro": "<p>The tooth figures most prominently in Scripture through the lex talionis formula \"tooth for tooth\" (Ex. 21:24; Lev. 24:20; Deut. 19:21), which established proportionate justice in Mosaic law. The principle limited revenge to exact equivalence — no more than the injury received — representing a significant moral advance over the unlimited vengeance of ancient tribal custom. The same principle governed injuries to slaves: if a master struck out a servant's tooth, the slave was to be freed (Ex. 21:27).</p><p>Jesus explicitly referenced and reinterpreted the tooth-for-tooth principle in the Sermon on the Mount (Matt. 5:38-39), calling his disciples to non-retaliation as a higher ethic that does not abolish the law's concern for justice but transforms the personal response to injury. \"Gnashing of teeth\" appears in Scripture as a vivid expression of rage (Acts 7:54; Job 16:9) and of the anguish and fury of the condemned (Matt. 8:12; 13:42, 50; 22:13), making the tooth one of the more theologically layered anatomical references in the Bible.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tooth"},
        "key_refs": ["Exodus 21:24", "Leviticus 24:20", "Matthew 5:38", "Matthew 8:12"]
    },
}


def main():
    written = 0
    skipped = 0
    for slug, data in ARTICLES.items():
        article = {
            "id": slug,
            "term": data["term"],
            "category": data["category"],
            "intro": data["intro"],
            "hitchcock_meaning": data["hitchcock_meaning"],
            "source_ids": data["source_ids"],
            "key_refs": data["key_refs"],
            "sections": []
        }
        if merge_article(slug, article):
            written += 1
        else:
            skipped += 1
    print(f'BP t2: Tetrarch → Tooth: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
