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
"prophets": {
  "id": "prophets",
  "term": "Prophets",
  "category": "people",
  "intro": "<p>The prophets were individuals called and commissioned by God to speak his word to Israel and the nations — not merely to predict the future but to interpret the present in light of God's covenant and character. The Hebrew term <em>nabi</em> (\"one who is called\" or \"one who speaks for\") covers a wide range of figures: Moses is called the greatest prophet (<strong>Deut. 34:10</strong>); Samuel inaugurated the prophetic office as an institution; the writing prophets from Amos and Hosea through Malachi produced the canonical Prophets. In Samuel's time, bands of prophets were organized into prophetic guilds, and the office eventually became distinct from priest and king — the prophet was God's covenant enforcer, calling Israel back from idolatry and injustice.</p><p>The prophetic role was characterized by direct divine commission, the formula \"Thus says the LORD,\" and willingness to confront both rulers and people. The NT identifies John the Baptist as the last of the OT prophets (<strong>Matt. 11:13</strong>) and Christ as the ultimate fulfillment of the Mosaic promise of a prophet like Moses (<strong>Deut. 18:15</strong>; <strong>Acts 3:22</strong>). The early church also recognized a prophetic gift among its members (<strong>1 Cor. 12:28</strong>; <strong>Eph. 4:11</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Deuteronomy 18:15", "1 Kings 17:1", "Acts 3:22", "Matthew 11:13"]
},
"rulers": {
  "id": "rulers",
  "term": "Rulers",
  "category": "concepts",
  "intro": "<p>Scripture addresses the institution of human government throughout both Testaments, presenting rulers as accountable to God as the ultimate sovereign. The OT ideal is the theocratic king who governs in accordance with God's law and leads his people in covenant faithfulness (<strong>Deut. 17:14–20</strong>). Israel's request for a king \"like the nations\" was a rejection of God's direct rule (<strong>1 Sam. 8:7</strong>), yet God accommodated it and worked through the Davidic monarchy to prepare for Christ. Daniel presents world rulers as instruments of God's sovereign purpose over history, however unaware of this they may be (<strong>Dan. 4:25</strong>).</p><p>The NT affirms civil authority as God's servant for good, ordained for the restraint of evil and the encouragement of righteousness (<strong>Rom. 13:1–4</strong>; <strong>1 Pet. 2:13–14</strong>). Obedience to rulers is enjoined with the important limit that \"we must obey God rather than men\" when the two come into conflict (<strong>Acts 5:29</strong>). Revelation portrays earthly kingdoms that set themselves against God as destined for judgment, while Christ is declared \"King of kings and Lord of lords\" (<strong>Rev. 19:16</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Romans 13:1", "Daniel 4:25", "Deuteronomy 17:15", "Revelation 19:16"]
},
"animals": {
  "id": "animals",
  "term": "Animals",
  "category": "concepts",
  "intro": "<p>Animals (Hebrew <em>behemah</em>, <em>chayah</em>; Greek <em>zoa</em>) occupy a significant place in biblical theology as part of God's creation, governed by his care, and integral to Israel's sacrificial worship. God created the animals on the fifth and sixth days, bringing them to Adam to be named — an act signifying human dominion over them (<strong>Gen. 1:24</strong>; <strong>2:19</strong>). After the Flood, God extended his covenant to \"every living creature\" (<strong>Gen. 9:10</strong>) and permits humans to eat animals with restrictions (<strong>Gen. 9:3</strong>; <strong>Lev. 11</strong>).</p><p>The Mosaic law regulated the use of animals extensively: distinguishing clean from unclean, prescribing which could be offered in sacrifice (unblemished cattle, sheep, goats, doves), and providing protections for working animals (<strong>Deut. 25:4</strong>; <strong>Ex. 23:12</strong>). Jesus invoked God's care for sparrows as an argument for his care for people (<strong>Matt. 10:29–31</strong>). Animals also populate biblical imagery extensively — the lion for power and royalty, the lamb for innocence and sacrifice, the dove for peace and the Spirit — culminating in the four living creatures of the divine throne in Ezekiel and Revelation.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Genesis 1:24", "Leviticus 11:2", "Matthew 10:29", "Genesis 9:10"]
},
"apostles": {
  "id": "apostles",
  "term": "Apostles",
  "category": "people",
  "intro": "<p>The apostles (<em>apostoloi</em>, \"those sent out\") were the twelve men chosen by Jesus from among his disciples to be the foundational witnesses of his ministry, death, and resurrection (<strong>Luke 6:13</strong>; <strong>Matt. 10:2–4</strong>; <strong>Mark 3:16–19</strong>). Their commission extended the scope of Jesus's own mission: he sent them first to Israel, then after the resurrection to \"all nations\" (<strong>Matt. 28:19</strong>; <strong>Acts 1:8</strong>). Judas Iscariot's betrayal and subsequent death led to Matthias being chosen to replace him, restoring the Twelve as witnesses of the resurrection (<strong>Acts 1:26</strong>).</p><p>Paul claimed apostolic authority as one \"born out of due time\" on the basis of his Damascus road encounter with the risen Christ (<strong>1 Cor. 15:8–9</strong>; <strong>Gal. 1:1</strong>). The NT uses the term more broadly in some passages (Barnabas, Andronicus, Junia) to denote pioneer missionaries. The apostles are the foundation of the church (with Christ as cornerstone, <strong>Eph. 2:20</strong>), and Revelation 21:14 names the twelve foundations of the New Jerusalem after the twelve apostles of the Lamb.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Luke 6:13", "Matthew 10:2", "Acts 1:26", "Ephesians 2:20"]
},
"character": {
  "id": "character",
  "term": "Character",
  "category": "concepts",
  "intro": "<p>Biblical ethics centers on character — the formation of a person's inner dispositions toward God and neighbor — rather than merely on external rule-keeping. The OT vision of the righteous person integrates heart, will, and action: the blessed man of <strong>Psalm 1</strong> delights in God's law inwardly; the Proverbs describe character virtues (wisdom, diligence, integrity) and vices (foolishness, sloth, pride) as patterns shaping the whole of life. The prophets repeatedly insist that outward ritual without inner transformation is worthless before God (<strong>Isa. 1:10–17</strong>; <strong>Mic. 6:8</strong>).</p><p>Jesus deepens the OT emphasis: the Sermon on the Mount targets the heart behind actions — anger underlies murder, lust underlies adultery, self-promotion underlies piety (<strong>Matt. 5:21–48</strong>). Pauline ethics similarly aims at transformation of the whole person: putting off the old self and putting on the new, created in God's likeness in righteousness and holiness of truth (<strong>Eph. 4:22–24</strong>). The goal of Christian formation is conformity to the image of Christ (<strong>Rom. 8:29</strong>; <strong>2 Cor. 3:18</strong>), a process the NT calls sanctification, worked out by the Spirit from within.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Psalm 1:2", "Micah 6:8", "Matthew 5:8", "Ephesians 4:24"]
},
"citizens": {
  "id": "citizens",
  "term": "Citizens",
  "category": "concepts",
  "intro": "<p>Citizenship in the biblical world carried both rights and obligations. In Israel, belonging to the covenant community conferred membership in the holy nation and involved obligations of obedience to God's law, financial contribution to the sanctuary, and participation in the festivals. The OT law required honoring those in civil authority (<strong>Ex. 22:28</strong>) and praying for the welfare of the city where the exiles were settled (<strong>Jer. 29:7</strong>).</p><p>In the NT, Paul appeals to his Roman citizenship strategically (in Philippi, before the tribune in Jerusalem) to secure his rights and advance the gospel (<strong>Acts 16:37</strong>; <strong>22:25–28</strong>). Yet his deeper citizenship is heavenly: \"Our citizenship (<em>politeuma</em>) is in heaven\" (<strong>Phil. 3:20</strong>), from which Christ the Savior will come. Peter describes believers as \"strangers and exiles\" in this world (<strong>1 Pet. 2:11</strong>), while Ephesians 2:19 declares that Gentile believers are \"no longer strangers and aliens, but fellow citizens with the saints and members of the household of God.\"</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Philippians 3:20", "Ephesians 2:19", "Acts 22:28", "1 Peter 2:11"]
},
"depravity-of-man": {
  "id": "depravity-of-man",
  "term": "Depravity of Man",
  "category": "concepts",
  "intro": "<p>The depravity of man is the biblical teaching that the fall of Adam and Eve corrupted human nature such that every dimension of human existence — mind, will, affections, and conscience — is affected by sin. God's assessment before the Flood: \"every intention of the thoughts of his heart was only evil continually\" (<strong>Gen. 6:5</strong>). After the Flood the same verdict stands: \"the intention of man's heart is evil from his youth\" (<strong>Gen. 8:21</strong>). The prophets reinforce this: the heart is \"deceitful above all things, and desperately sick\" (<strong>Jer. 17:9</strong>).</p><p>Paul's comprehensive indictment of all humanity in <strong>Romans 1–3</strong> culminates in the catena of OT citations: \"None is righteous, no, not one; no one understands; no one seeks for God... there is no fear of God before their eyes\" (<strong>Rom. 3:10–18</strong>). Reformed theology has codified this as \"total depravity\" — not that humans are as wicked as possible, but that sin has affected all parts of the person. The consistent biblical remedy is God's regenerating grace: the new birth by the Spirit (<strong>John 3:3–7</strong>) and the new heart promised by the new covenant (<strong>Ezek. 36:26–27</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Genesis 6:5", "Romans 3:10", "Jeremiah 17:9", "Ezekiel 36:26"]
},
"impenitence": {
  "id": "impenitence",
  "term": "Impenitence",
  "category": "concepts",
  "intro": "<p>Impenitence is the hardening of the heart against God's call to repentance — the persistent refusal to acknowledge sin and turn to God. The Bible presents it as deeply dangerous, accumulating judgment for the day of wrath: \"Because of your hard and impenitent heart you are storing up wrath for yourself on the day of wrath\" (<strong>Rom. 2:5</strong>). Pharaoh's progressive hardening against God's plagues is the OT paradigm: both self-hardening and divine judicial hardening are described (<strong>Ex. 8:15, 32</strong>; <strong>9:12</strong>; <strong>14:4</strong>).</p><p>The prophets repeatedly warn cities and individuals that impenitence forfeits the mercy God extends: \"If you will not repent, I will whet my sword\" (<strong>Ps. 7:12</strong>). Jesus's Galilean ministry warnings are especially sobering: cities that witnessed his miracles and did not repent would face judgment more severe than Sodom (<strong>Matt. 11:20–24</strong>). The unforgivable sin — blasphemy against the Holy Spirit — is related to the settled, final rejection of the Spirit's witness to Christ. Hebrews warns against the hardening that can make repentance impossible (<strong>Heb. 6:4–6</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Romans 2:5", "Exodus 8:15", "Matthew 11:20", "Hebrews 6:6"]
},
"infidelity": {
  "id": "infidelity",
  "term": "Infidelity",
  "category": "concepts",
  "intro": "<p>Infidelity in its biblical sense denotes unbelief toward God — the failure or refusal to trust his word, promises, and revelation. The Hebrew root <em>aman</em> (\"to trust, believe\") provides the positive baseline: Abraham \"believed God, and it was counted to him as righteousness\" (<strong>Gen. 15:6</strong>; <strong>Rom. 4:3</strong>). Infidelity is the opposite — doubting or openly rejecting God's word. Israel in the wilderness repeatedly demonstrated it: they doubted God's power to provide water, food, and victory, despite the evidence of the Exodus (<strong>Num. 14:11</strong>; <strong>Ps. 78:22</strong>).</p><p>The OT also uses the marriage metaphor: Israel's abandonment of God for idols is called infidelity or harlotry (<strong>Hos. 2:2</strong>; <strong>Jer. 3:8</strong>; <strong>Ezek. 16</strong>). In the NT, unbelief (Greek <em>apistia</em>) is presented as the fundamental problem that prevents reception of God's grace: Jesus \"did not do many mighty works\" in Nazareth \"because of their unbelief\" (<strong>Matt. 13:58</strong>). Hebrews warns against \"an evil, unbelieving heart, leading you to fall away from the living God\" (<strong>Heb. 3:12</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Genesis 15:6", "Hebrews 3:12", "Matthew 13:58", "Numbers 14:11"]
},
"judgments": {
  "id": "judgments",
  "term": "Judgments",
  "category": "concepts",
  "intro": "<p>The judgments of God refer to his specific acts of divine punishment within history — distinct from the final eschatological judgment. They include the expulsion from Eden (<strong>Gen. 3:14–24</strong>), the Flood (<strong>Gen. 6–8</strong>), the confusion of languages at Babel (<strong>Gen. 11:1–9</strong>), the destruction of Sodom and Gomorrah (<strong>Gen. 19</strong>), the ten plagues on Egypt (<strong>Ex. 7–12</strong>), the judgments of the wilderness period against faithless Israel, and ultimately the Assyrian and Babylonian exiles (<strong>2 Kings 17</strong>; <strong>25</strong>) which the prophets consistently interpreted as covenant consequences.</p><p>The OT presents these judgments as both punitive and remedial — intended to bring repentance and restore covenant relationship when possible. Amos 4:6–12 lists successive judgments that God sent to bring Israel back to himself, followed by the refrain \"yet you did not return to me.\" The NT frames the cross itself as God's judgment on sin borne by Christ (<strong>Rom. 3:25–26</strong>; <strong>2 Cor. 5:21</strong>), so that those who are in Christ are no longer under condemnation (<strong>Rom. 8:1</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Genesis 3:17", "Amos 4:12", "Romans 3:25", "2 Kings 17:18"]
},
"liberality": {
  "id": "liberality",
  "term": "Liberality",
  "category": "concepts",
  "intro": "<p>Liberality (generosity, open-handedness) is a consistently commended virtue in both Testaments. The Mosaic law institutionalized generosity through tithing, gleaning rights for the poor, the sabbatical release of debts, and the Jubilee return of land (<strong>Lev. 25:35</strong>; <strong>Deut. 15:7–11</strong>). Proverbs holds up the generous man as enriched and blessed: \"One gives freely, yet grows all the richer; another withholds what he should give, and only suffers want\" (<strong>Prov. 11:24</strong>). The psalms celebrate the man who \"has distributed freely, he has given to the poor; his righteousness endures forever\" (<strong>Ps. 112:9</strong>).</p><p>Jesus intensified the call to generosity: sell possessions and give to the poor (<strong>Luke 12:33</strong>), lend without expecting return (<strong>Luke 6:35</strong>), and practice almsgiving secretly rather than for public honor (<strong>Matt. 6:1–4</strong>). Paul's collection for the Jerusalem church (<strong>2 Cor. 8–9</strong>) is the NT's most sustained treatment of generosity, grounded in Christ's own self-giving: \"though he was rich, yet for your sake he became poor\" (<strong>2 Cor. 8:9</strong>). The cheerful giver is beloved of God (<strong>2 Cor. 9:7</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["2 Corinthians 9:7", "Proverbs 11:24", "Deuteronomy 15:10", "Luke 6:35"]
},
"parents": {
  "id": "parents",
  "term": "Parents",
  "category": "concepts",
  "intro": "<p>The biblical teaching on parents encompasses both the obligations of parents toward their children and the duties of children toward their parents. The fifth commandment — \"Honor your father and your mother\" (<strong>Ex. 20:12</strong>; <strong>Deut. 5:16</strong>) — is the foundational text, framed as a positive duty with the promise of long life in the land. It is the first commandment with a promise (<strong>Eph. 6:2</strong>). Striking or cursing a parent was a capital offense in the Mosaic law (<strong>Ex. 21:15, 17</strong>).</p><p>The responsibility of parents to instruct children in the faith is mandated in the Shema context: \"You shall teach them diligently to your children\" (<strong>Deut. 6:7</strong>). Proverbs extensively addresses parental discipline: \"Train up a child in the way he should go\" (<strong>Prov. 22:6</strong>). In the NT, Paul commands fathers not to provoke their children to anger but to raise them in the discipline and instruction of the Lord (<strong>Eph. 6:4</strong>). Jesus himself submitted to his parents (<strong>Luke 2:51</strong>) and condemned the Corban tradition that allowed men to evade parental support (<strong>Mark 7:10–13</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Exodus 20:12", "Deuteronomy 6:7", "Ephesians 6:4", "Proverbs 22:6"]
},
"presumption": {
  "id": "presumption",
  "term": "Presumption",
  "category": "concepts",
  "intro": "<p>Presumption in biblical usage denotes the arrogant overstepping of proper boundaries in relation to God — acting as if one has rights or guarantees one does not possess, or as if God's mercy makes obedience optional. The Mosaic law distinguished between sins committed \"unintentionally\" (for which atonement was available) and sins committed \"with a high hand\" (presumptuously), for which there was no sacrifice — such a person \"reproaches the LORD\" and must be cut off (<strong>Num. 15:30–31</strong>). The psalmist prays to be kept from presumptuous sins that would have great power over him (<strong>Ps. 19:13</strong>).</p><p>Israel's attempt to enter Canaan after the negative spy report — against God's explicit word — is a paradigmatic example: they went up \"presumptuously\" and were defeated (<strong>Num. 14:44</strong>; <strong>Deut. 1:43</strong>). The false prophet who speaks without divine commission also acts presumptuously (<strong>Deut. 18:20</strong>). In the NT, the temptation of Jesus to throw himself from the temple pinnacle — expecting miraculous rescue — is a form of presumption that tests God rather than trusting him (<strong>Matt. 4:6–7</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Numbers 15:30", "Psalms 19:13", "Deuteronomy 18:20", "Matthew 4:7"]
},
"prudence": {
  "id": "prudence",
  "term": "Prudence",
  "category": "concepts",
  "intro": "<p>Prudence (<em>arum</em>, <em>sekel</em> in Hebrew; <em>phronesis</em> in Greek) is the practical wisdom to discern the right course of action in particular circumstances — the application of wisdom to real-life decisions. Proverbs presents it as one of the central virtues: \"The prudent sees danger and hides himself\" (<strong>Prov. 22:3</strong>; <strong>27:12</strong>), contrasted with the simple who blunder ahead. The prudent person weighs words carefully (<strong>Prov. 12:23</strong>), governs appetite (<strong>Prov. 23:1–3</strong>), and acts with forethought.</p><p>The personified Wisdom of Proverbs 8 identifies herself with prudence (<strong>Prov. 8:12</strong>). In the NT, Jesus commends prudence in his disciples: \"Be wise (prudent) as serpents and innocent as doves\" (<strong>Matt. 10:16</strong>). The parable of the wise and foolish builders (<strong>Matt. 7:24–27</strong>) and the ten virgins (<strong>Matt. 25:1–13</strong>) contrast prudent preparation with foolish negligence. Paul's prayer for the Ephesians includes that they receive \"the Spirit of wisdom and of revelation\" (<strong>Eph. 1:17</strong>), and his letter opens by blessing God who has lavished upon us \"all wisdom and insight (prudence)\" in Christ (<strong>Eph. 1:8</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Proverbs 8:12", "Matthew 10:16", "Ephesians 1:8", "Proverbs 22:3"]
},
"reproof": {
  "id": "reproof",
  "term": "Reproof",
  "category": "concepts",
  "intro": "<p>Reproof (rebuke, correction) is presented in Scripture as an act of love and a necessity of faithful community and individual life. Proverbs strongly affirms the value of accepting reproof: \"Whoever loves discipline loves knowledge, but he who hates reproof is stupid\" (<strong>Prov. 12:1</strong>). The one who accepts rebuke gains understanding (<strong>Prov. 15:32</strong>), and a wise person reproves a scoffer at personal risk but reproves a wise man who will love him for it (<strong>Prov. 9:7–8</strong>). The Levitical law required members of the community to \"rebuke your neighbor frankly\" rather than hold a grudge (<strong>Lev. 19:17</strong>).</p><p>Jesus provides the definitive NT pattern for reproof in <strong>Matthew 18:15–17</strong>: private rebuke, then witnesses, then the church — a graduated process aimed at restoration rather than condemnation. Paul commands Timothy to \"reprove, rebuke, and exhort, with complete patience and teaching\" (<strong>2 Tim. 4:2</strong>; <strong>3:16–17</strong>), noting that all Scripture is profitable for reproof and correction. The Holy Spirit convicts (reproves) the world of sin, righteousness, and judgment (<strong>John 16:8</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Proverbs 12:1", "Leviticus 19:17", "Matthew 18:15", "2 Timothy 4:2"]
},
"sanitation": {
  "id": "sanitation",
  "term": "Sanitation",
  "category": "concepts",
  "intro": "<p>The Mosaic law included extensive regulations with public health dimensions, though their primary framing was religious purity rather than germ theory. Laws governing bodily discharges (<strong>Lev. 15</strong>), skin diseases (<strong>Lev. 13–14</strong>), contact with corpses (<strong>Num. 19:11–22</strong>), the handling of unclean foods, and the quarantine of suspected lepers had the practical effect of limiting contagion and maintaining community hygiene. The requirement to bury human waste outside the camp (<strong>Deut. 23:12–14</strong>) is explicitly grounded in God's holy presence among the people.</p><p>The purification rituals — hand-washing, bathing, laundering garments, burning contaminated materials — enforced patterns of cleanliness that distinguished Israel from its neighbors. Many scholars note that the Mosaic sanitation regulations anticipate practices modern medicine independently arrived at: quarantine of infectious disease, avoidance of blood consumption, and separation of the sick from the community. In the NT, Jesus's response to the woman with a flow of blood (<strong>Mark 5:25–34</strong>) and his healing of lepers both show him willing to touch the ceremonially unclean, reversing the normal direction of contamination through his power.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Leviticus 13:4", "Numbers 19:11", "Deuteronomy 23:12", "Leviticus 15:2"]
},
"seekers": {
  "id": "seekers",
  "term": "Seekers",
  "category": "concepts",
  "intro": "<p>\"Seeking God\" (<em>darash</em>, <em>baqash</em> in Hebrew; <em>zeteo</em> in Greek) is a foundational posture of biblical faith — the active orientation of the whole person toward God in prayer, worship, and obedience. The great covenant promise is that those who seek God will find him: \"You will seek me and find me, when you seek me with all your heart\" (<strong>Jer. 29:13</strong>; <strong>Deut. 4:29</strong>). The psalmist's longing — \"As a deer pants for flowing streams, so pants my soul for you, O God\" (<strong>Ps. 42:1</strong>) — expresses the seeker's spirit.</p><p>Seeking God in the OT involves prayer, inquiry at the sanctuary, and walking in his ways. The failure to seek God is a symptom of apostasy: \"The LORD looks down from heaven on the children of man, to see if there are any who understand, who seek after God\" — and finds none among the unrighteous (<strong>Ps. 14:2–3</strong>). Jesus promises that those who ask will receive, seek will find, and knock will have the door opened (<strong>Matt. 7:7–8</strong>). The Athenians unknowingly \"sought God, in the hope that they might feel their way toward him and find him\" (<strong>Acts 17:27</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Jeremiah 29:13", "Psalms 42:1", "Matthew 7:7", "Acts 17:27"]
},
"speaking": {
  "id": "speaking",
  "term": "Speaking",
  "category": "concepts",
  "intro": "<p>The use of speech is a major ethical concern throughout Scripture, reflecting the conviction that words have weight before God and consequence for human relationships. Proverbs contains the most concentrated wisdom on speaking: the tongue has power of life and death (<strong>Prov. 18:21</strong>); the words of a wise person are like a refreshing brook (<strong>Prov. 18:4</strong>); lying lips are an abomination to the LORD but truthful lips are his delight (<strong>Prov. 12:22</strong>). The Ninth Commandment against false witness extends to all dishonest speech.</p><p>James writes the NT's most focused treatment of the tongue: though small, it is a fire capable of setting a great forest ablaze, and no human being can tame it (<strong>James 3:5–8</strong>). Paul urges speech that is \"always gracious, seasoned with salt\" (<strong>Col. 4:6</strong>), instructive in meetings (<strong>1 Cor. 14:26</strong>), and fit for \"building up\" rather than corrupting (<strong>Eph. 4:29</strong>). Jesus holds the highest standard: \"By your words you will be justified, and by your words you will be condemned\" (<strong>Matt. 12:37</strong>), and \"every careless word\" will be given account of on the day of judgment (<strong>Matt. 12:36</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Proverbs 18:21", "James 3:6", "Ephesians 4:29", "Matthew 12:36"]
},
"strife": {
  "id": "strife",
  "term": "Strife",
  "category": "concepts",
  "intro": "<p>Strife (quarreling, contention, discord) is consistently condemned in Scripture as destructive to community and contrary to the peace God intends. Proverbs returns to this theme repeatedly: \"A hot-tempered man stirs up strife, but he who is slow to anger quiets contention\" (<strong>Prov. 15:18</strong>); \"It is an honor for a man to keep aloof from strife\" (<strong>Prov. 20:3</strong>); \"Where there is no wood, a fire goes out; where there is no whisperer, contention ceases\" (<strong>Prov. 26:20</strong>). Quarreling among God's people is a recurring failure in Israel's history and in the early church.</p><p>Paul lists \"strife, jealousy, fits of anger, rivalries, dissensions, divisions\" among the works of the flesh (<strong>Gal. 5:20</strong>). His letter to the Philippians addresses real interpersonal conflict between Euodia and Syntyche (<strong>Phil. 4:2</strong>) and calls the community to \"do nothing from selfish ambition or conceit\" (<strong>Phil. 2:3</strong>). James diagnoses the root of strife: \"What causes quarrels and fights among you? Is it not this, that your passions are at war within you?\" (<strong>James 4:1</strong>). The remedy is humility, gentleness, and the wisdom from above that is \"first pure, then peaceable\" (<strong>James 3:17</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Proverbs 15:18", "Galatians 5:20", "James 4:1", "Philippians 2:3"]
},
"worldliness": {
  "id": "worldliness",
  "term": "Worldliness",
  "category": "concepts",
  "intro": "<p>Worldliness denotes the orientation of one's life around the values, pleasures, and goals of the present age rather than around God and his kingdom. The prophets lampooned Israel's conformity to the surrounding nations in worship and lifestyle. Jesus identifies two masters — God and money — between whom no one can serve both (<strong>Matt. 6:24</strong>), and warns against the deceitfulness of riches and the pleasures of this life that choke the word and make it unfruitful (<strong>Matt. 13:22</strong>; <strong>Luke 8:14</strong>).</p><p>John provides the clearest NT definition: \"Do not love the world or the things in the world... For all that is in the world — the desires of the flesh and the desires of the eyes and pride of life — is not from the Father but is from the world. And the world is passing away along with its desires\" (<strong>1 John 2:15–17</strong>). Paul calls believers not to be \"conformed to this world\" but to be transformed by the renewing of the mind (<strong>Rom. 12:2</strong>). James diagnoses friendship with the world as enmity with God (<strong>James 4:4</strong>). The antidote is the fear of God, eternal perspective, and the love of the Father that displaces love of the world.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["1 John 2:15", "Romans 12:2", "James 4:4", "Matthew 6:24"]
},
"anthropomorphisms": {
  "id": "anthropomorphisms",
  "term": "Anthropomorphisms",
  "category": "concepts",
  "intro": "<p>Anthropomorphisms (from Greek <em>anthropos</em>, human, + <em>morphe</em>, form) are descriptions of God using human physical or emotional characteristics — giving him hands, eyes, ears, a face, a mouth, nostrils, arms, and the emotions of pleasure, grief, anger, and regret. Examples pervade the OT: God \"walked in the garden\" (<strong>Gen. 3:8</strong>), \"the LORD smelled the pleasing aroma\" (<strong>Gen. 8:21</strong>), \"the eyes of the LORD\" roam throughout the earth (<strong>2 Chr. 16:9</strong>), and God \"repented\" of making Saul king (<strong>1 Sam. 15:35</strong>).</p><p>These are not meant as literal physical descriptions of an incorporeal God (\"God is spirit,\" <strong>John 4:24</strong>; \"no one has ever seen God,\" <strong>John 1:18</strong>) but as condescension — God communicating his reality in categories accessible to human understanding. The theological term for this is <em>accommodation</em>. The Psalms and Prophets use anthropomorphism extensively and deliberately: it conveys God's personal engagement with creation and human affairs, his genuine emotional responses (not mere metaphor) to human obedience and rebellion, and his relational character as a God who sees, hears, and acts.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Genesis 3:8", "Genesis 8:21", "John 4:24", "2 Chronicles 16:9"]
},
"apostasy": {
  "id": "apostasy",
  "term": "Apostasy",
  "category": "concepts",
  "intro": "<p>Apostasy (Greek <em>apostasia</em>, \"a standing away from\") denotes a deliberate falling away from the faith — a turning from God after having known him. In the OT, Israel's repeated abandonment of the LORD for foreign gods constitutes national apostasy, threatened with covenant curses (<strong>Deut. 28–30</strong>) and eventually fulfilled in exile. The prophets describe it in terms of marital unfaithfulness (<strong>Hos. 2</strong>; <strong>Jer. 3</strong>) and the forsaking of the fountain of living waters for broken cisterns (<strong>Jer. 2:13</strong>).</p><p>In the NT, Paul warns of a coming apostasy before the day of the Lord (<strong>2 Thess. 2:3</strong>) and describes those who have \"made shipwreck of their faith\" (<strong>1 Tim. 1:19</strong>). Hebrews contains the most severe warnings: those who \"have tasted the heavenly gift\" and then \"fall away\" crucify the Son of God again and cannot be restored to repentance (<strong>Heb. 6:4–6</strong>); and those who \"shrink back\" are distinguished from those who \"have faith and preserve their souls\" (<strong>Heb. 10:39</strong>). The question of whether true believers can apostatize in a final, irrecoverable sense is one of the major disputed points of NT soteriology.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Hebrews 6:4", "2 Thessalonians 2:3", "Jeremiah 2:13", "1 Timothy 1:19"]
},
"benedictions": {
  "id": "benedictions",
  "term": "Benedictions",
  "category": "concepts",
  "intro": "<p>Benedictions are formal pronouncements of blessing — the invocation of God's favor and well-being upon persons or communities. The paradigmatic OT benediction is the Aaronic blessing of <strong>Numbers 6:24–26</strong>, given by the priests over Israel: \"The LORD bless you and keep you; the LORD make his face shine on you and be gracious to you; the LORD turn his face toward you and give you peace.\" God himself promised to bless those on whom his name was thus pronounced. Patriarchal blessings (Isaac's blessing of Jacob and Esau, Jacob's blessing of his sons, <strong>Gen. 27</strong>; <strong>49</strong>) also functioned as solemn benedictions with prophetic force.</p><p>The Psalms conclude with doxological benedictions, and several NT epistles open and close with blessings: \"Grace and peace to you from God our Father and the Lord Jesus Christ\" (Pauline salutations); \"The grace of the Lord Jesus Christ and the love of God and the fellowship of the Holy Spirit be with you all\" (<strong>2 Cor. 13:14</strong>); \"May the God of peace himself sanctify you completely\" (<strong>1 Thess. 5:23</strong>). The Aaronic blessing continues to be used in Christian worship as an authoritative declaration of God's favor over his people.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Numbers 6:24", "2 Corinthians 13:14", "Genesis 49:1", "1 Thessalonians 5:23"]
},
"beneficence": {
  "id": "beneficence",
  "term": "Beneficence",
  "category": "concepts",
  "intro": "<p>Beneficence — active kindness and material generosity toward others — is rooted in Israel's covenant ethic and finds its NT expression in the love commandment and the imitation of God's own generosity. The Mosaic law legislated beneficence toward the poor: gleaning rights, the tithe for the Levite and the poor, the sabbatical release of debts, and the prohibition against charging interest from needy fellow Israelites (<strong>Lev. 25:35–37</strong>; <strong>Deut. 15:7–11</strong>). The motive given is theological: \"Remember that you were a slave in Egypt\" and God redeemed you.</p><p>Jesus distilled the law and prophets into love of God and love of neighbor (<strong>Matt. 22:37–40</strong>), and the parable of the Good Samaritan extended neighbor-love to practical action across social and ethnic lines (<strong>Luke 10:33–37</strong>). James insists that faith without works of beneficence is dead: faith that does not provide food and clothing for a brother or sister in need is no faith at all (<strong>James 2:14–17</strong>). Paul calls the Corinthians to replicate Christ's own self-giving generosity in their collection for the Jerusalem poor (<strong>2 Cor. 8:9</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Deuteronomy 15:10", "Luke 10:37", "James 2:17", "2 Corinthians 8:9"]
},
"conviction": {
  "id": "conviction",
  "term": "Conviction",
  "category": "concepts",
  "intro": "<p>Conviction of sin — the inner persuasion that one has violated God's holiness and stands guilty before him — is presented in Scripture as the essential precondition for repentance and faith. The Psalms record David's experience of conviction: \"When I kept silent, my bones wasted away through my groaning all day long... your hand was heavy upon me; my strength was dried up\" (<strong>Ps. 32:3–4</strong>). The acknowledgment of sin brings relief: \"I acknowledged my sin to you... and you forgave the iniquity of my sin\" (<strong>Ps. 32:5</strong>). Job's encounter with God moves from confident self-defense to prostrate silence (<strong>Job 40:4–5</strong>).</p><p>The NT identifies the Holy Spirit as the agent of conviction: Jesus promises the Spirit will \"convict the world concerning sin and righteousness and judgment\" (<strong>John 16:8</strong>). Peter's Pentecost sermon produced conviction in the hearers: \"they were cut to the heart\" and cried out \"What shall we do?\" (<strong>Acts 2:37</strong>). Paul teaches that the law serves to produce conviction of sin so that sin might be shown to be \"sinful beyond measure\" (<strong>Rom. 7:13</strong>) — making the gospel's remedy both necessary and welcome.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["John 16:8", "Acts 2:37", "Psalms 32:3", "Romans 7:13"]
},
"cowardice": {
  "id": "cowardice",
  "term": "Cowardice",
  "category": "concepts",
  "intro": "<p>Cowardice — the failure of courage in the face of danger, opposition, or persecution — is treated in Scripture as a spiritual failure rather than a mere temperamental weakness. The Mosaic military law released from battle those who were \"afraid and fainthearted,\" lest they discourage others (<strong>Deut. 20:8</strong>). The repeated divine exhortation \"Fear not\" and \"Be strong and courageous\" (<strong>Deut. 31:6</strong>; <strong>Josh. 1:9</strong>) implies that courage must be cultivated and cowardice resisted through trust in God's presence and promise.</p><p>The NT applies this spiritually: Paul urges Timothy, who seems prone to timidity, that \"God gave us a spirit not of fear but of power and love and self-control\" (<strong>2 Tim. 1:7</strong>). The disciple who publicly denies Christ — as Peter did — is a form of cowardice that Jesus warned against (<strong>Matt. 10:33</strong>). Revelation's solemn list of those excluded from the heavenly city begins with \"the cowardly\" (<strong>Rev. 21:8</strong>) — those who, fearing earthly consequences, denied Christ or abandoned faith under pressure. The antidote is faith in the sovereignty of God and love that casts out fear (<strong>1 John 4:18</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Revelation 21:8", "2 Timothy 1:7", "Joshua 1:9", "1 John 4:18"]
},
"disobedience-to-god": {
  "id": "disobedience-to-god",
  "term": "Disobedience to God",
  "category": "concepts",
  "intro": "<p>Disobedience to God — the refusal to heed, obey, or follow his commands — is the defining characteristic of sin throughout Scripture. Its paradigm is Adam and Eve's eating of the forbidden fruit: the single act of disobedience that introduced death, enmity, and labor into human existence (<strong>Gen. 3:6, 17–19</strong>). Paul interprets all of human history through this lens: \"as through one man's disobedience many were constituted sinners, so through one man's obedience many will be constituted righteous\" (<strong>Rom. 5:19</strong>).</p><p>The OT history of Israel is largely a narrative of disobedience and its consequences: the wilderness generation died because of unbelief and refusal to enter Canaan (<strong>Num. 14:22–23</strong>; <strong>Heb. 3:18–19</strong>); the monarchy collapsed under the weight of successive kings who \"did evil in the sight of the LORD\"; exile was the covenantal penalty for persistent disobedience (<strong>Deut. 28:15–68</strong>). Hebrews warns NT believers not to fall into the same pattern: \"Do not harden your hearts as in the rebellion\" (<strong>Heb. 3:8</strong>). The gospel is described as demanding \"the obedience of faith\" (<strong>Rom. 1:5</strong>; <strong>16:26</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Romans 5:19", "Genesis 3:17", "Hebrews 3:18", "Deuteronomy 28:15"]
},
"doubting": {
  "id": "doubting",
  "term": "Doubting",
  "category": "concepts",
  "intro": "<p>Doubt in Scripture covers a range of experiences: the intellectual questioning of God's existence or goodness, the wavering of faith under trial, and the paralysis of indecision. The psalms of lament give the most honest voice to the believer's doubt: \"My God, my God, why have you forsaken me?\" (<strong>Ps. 22:1</strong>); \"Has God forgotten to be gracious?\" (<strong>Ps. 77:9</strong>). These are not merely rhetorical — they reflect genuine spiritual struggle, addressed to God and ultimately resolved through remembrance of his past faithfulness.</p><p>John the Baptist's question from prison — \"Are you the one who is to come, or shall we look for another?\" (<strong>Matt. 11:3</strong>) — represents doubt arising from circumstance rather than unbelief; Jesus responds with evidence. Thomas's refusal to believe without physical evidence (<strong>John 20:25</strong>) becomes faith at the sight of the risen Christ; Jesus pronounces a blessing on those who believe without seeing. James warns against the \"double-minded\" person who doubts in prayer: \"unstable in all his ways\" (<strong>James 1:6–8</strong>). Jude 22 counsels mercy toward those who doubt, recognizing it as a common and often transitional condition of faith.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Matthew 11:3", "John 20:27", "James 1:6", "Psalms 22:1"]
},
"friendship": {
  "id": "friendship",
  "term": "Friendship",
  "category": "concepts",
  "intro": "<p>Biblical friendship is treated as a profound good, grounded in loyalty (<em>chesed</em>), mutual commitment, and truthful speech. Proverbs distinguishes fair-weather companions from the true friend: \"A friend loves at all times, and a brother is born for a time of adversity\" (<strong>Prov. 17:17</strong>), and \"there is a friend who sticks closer than a brother\" (<strong>Prov. 18:24</strong>). Job's lament when his friends fail him — \"To him who is withering away his friend ought to show kindness\" (<strong>Job 6:14</strong>) — and their ultimate failure and divine rebuke show the high standard expected of friendship.</p><p>The most celebrated biblical friendships are David and Jonathan — whose covenant love (\"exceeding the love of women,\" <strong>2 Sam. 1:26</strong>) is held up as a model of faithful friendship — and Ruth and Naomi (<strong>Ruth 1:16–17</strong>). Jesus transforms the concept: he calls his disciples friends rather than servants, grounding this in his self-disclosure and laying down his life for them (<strong>John 15:13–15</strong>). Abraham is called \"friend of God\" (<strong>James 2:23</strong>; <strong>2 Chr. 20:7</strong>), expressing the intimacy of faith that God honors with personal relationship.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Proverbs 17:17", "John 15:13", "2 Samuel 1:26", "James 2:23"]
},
"influence": {
  "id": "influence",
  "term": "Influence",
  "category": "concepts",
  "intro": "<p>The Bible consistently recognizes that human beings shape one another for good or ill, and that association carries spiritual consequence. Solomon's foreign wives influenced him to follow their gods (<strong>1 Kings 11:3–4</strong>), and his consequent apostasy influenced all Israel. Jeroboam \"made Israel to sin\" — a refrain repeated for every northern king who perpetuated his golden calves. The prophets held leaders responsible not only for their own sins but for the sins they induced in the nation.</p><p>The NT addresses influence both positively and negatively. Paul cites the Greek proverb \"Bad company corrupts good morals\" (<strong>1 Cor. 15:33</strong>) and warns against associating with those who call themselves Christians but live in flagrant sin (<strong>1 Cor. 5:11</strong>). The positive vision is \"salt and light\" — believers who flavor and illuminate the world around them by the quality of their lives (<strong>Matt. 5:13–16</strong>). The \"weaker brother\" passages in Romans 14 and 1 Corinthians 8–10 show Paul's careful attention to the influence of the strong on the weak: no right is worth exercising if it causes another to stumble.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["1 Corinthians 15:33", "Matthew 5:13", "Romans 14:13", "1 Kings 11:4"]
},
"instability": {
  "id": "instability",
  "term": "Instability",
  "category": "concepts",
  "intro": "<p>Instability of character — inconsistency, fickleness, and the inability to maintain commitment — is presented in Scripture as a serious spiritual deficiency. Reuben, Jacob's firstborn, forfeited the rights of primogeniture for his \"unstable\" character: \"Unstable as water, you shall not have preeminence, because you went up to your father's bed\" (<strong>Gen. 49:4</strong>). Pharaoh's cycle of relenting and re-hardening during the plagues is a pattern of instability. Israel's pattern of faithfulness in crisis and faithlessness in ease runs through Judges in repeated cycles.</p><p>James defines instability as the double-minded man (<em>dipsychos</em>, \"double-souled\") who wavers in prayer like a wave of the sea: \"that person must not suppose that he will receive anything from the Lord; he is a double-minded man, unstable in all his ways\" (<strong>James 1:7–8</strong>). The antidote is steadfastness (<em>hupomone</em>) — the patient endurance that the testing of faith produces (<strong>James 1:3–4</strong>). Paul prays for believers to be rooted and established in love (<strong>Eph. 3:17</strong>), and commends the Colossians for the steadfastness of their faith (<strong>Col. 2:5</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["James 1:8", "Genesis 49:4", "Colossians 2:5", "Ephesians 3:17"]
},
"penitent": {
  "id": "penitent",
  "term": "Penitent",
  "category": "concepts",
  "intro": "<p>The penitent in Scripture is the person who turns from sin in genuine contrition and returns to God — the opposite of the impenitent. The biblical vocabulary of penitence includes <em>nacham</em> (to feel sorrow, regret), <em>shub</em> (to turn, return), <em>metanoeo</em> (to change the mind), and <em>epistrepho</em> (to turn back). Psalm 51, attributed to David after his sin with Bathsheba, is the paradigmatic penitential prayer: \"The sacrifices of God are a broken spirit; a broken and contrite heart, O God, you will not despise\" (<strong>Ps. 51:17</strong>).</p><p>The penitent's return is met with divine welcome rather than condemnation. Isaiah 55:7: \"Let the wicked forsake his way... let him return to the LORD, who will have compassion on him, and to our God, for he will abundantly pardon.\" Jesus's three parables of Luke 15 — the lost sheep, the lost coin, and the prodigal son — all dramatize the joy of heaven over the return of the penitent. The father's running embrace of the returning son has become the defining NT image of God's response to genuine repentance. Paul distinguishes the \"godly grief\" that produces repentance leading to salvation from worldly sorrow that produces only death (<strong>2 Cor. 7:10</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Psalm 51:17", "Luke 15:20", "Isaiah 55:7", "2 Corinthians 7:10"]
},
"pilate": {
  "id": "pilate",
  "term": "Pilate",
  "category": "people",
  "intro": "<p>Pontius Pilate was the sixth Roman procurator (governor) of Judea, appointed approximately A.D. 26 in the twelfth year of Tiberius. He is the Roman official who presided over the trial and ordered the crucifixion of Jesus. His governance was marked by provocations of Jewish sensibilities — introducing Roman standards bearing the emperor's image into Jerusalem, appropriating temple funds for an aqueduct, and slaughtering Galileans whose blood he \"mingled with their sacrifices\" (<strong>Luke 13:1</strong>).</p><p>All four Gospels narrate the trial before Pilate, which agrees on his finding Jesus innocent of any capital charge and his eventual capitulation to the crowd's demand for crucifixion. John's Gospel elaborates the most extensive dialogue, with Pilate's famous question \"What is truth?\" (<strong>John 18:38</strong>) and his ironic inscription \"King of the Jews\" on the cross (<strong>John 19:19–22</strong>). The Apostles' Creed preserves his name: Jesus \"suffered under Pontius Pilate.\" Josephus and Tacitus both mention him, the latter confirming his execution of Christ (Annals 15.44). He was recalled to Rome c. A.D. 36 after a massacre of Samaritans.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Matthew 27:2", "John 18:38", "Luke 13:1", "John 19:19"]
},
"preaching": {
  "id": "preaching",
  "term": "Preaching",
  "category": "concepts",
  "intro": "<p>Preaching in Scripture denotes the authoritative public proclamation of God's word — the heralding (<em>kerysso</em>) of the gospel rather than merely the explaining (<em>didasko</em>) of doctrine, though the two overlap. The OT prophets are the primary models of preaching: they proclaimed God's word under divine commission, often against hostile audiences, calling for covenant renewal. Ezekiel's commissioning as a watchman (<strong>Ezek. 3:17</strong>) and Jonah's reluctant preaching at Nineveh are paradigmatic cases.</p><p>In the NT, preaching is the central activity of Jesus's ministry: \"He came into Galilee, proclaiming (<em>kerysso</em>) the gospel of God\" (<strong>Mark 1:14</strong>). His sermon at Nazareth (<strong>Luke 4:18–19</strong>) applies Isaiah 61 to his own mission. The apostolic preaching (the <em>kerygma</em>) centered on the death and resurrection of Jesus as fulfillment of the scriptures and the call to repentance and faith (<strong>Acts 2:14–39</strong>). Paul declares it a divine necessity: \"Woe to me if I do not preach the gospel\" (<strong>1 Cor. 9:16</strong>), and the method is primary: faith comes by hearing the word proclaimed (<strong>Rom. 10:14–17</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Romans 10:14", "Mark 1:14", "1 Corinthians 9:16", "Acts 2:14"]
},
"prisoners": {
  "id": "prisoners",
  "term": "Prisoners",
  "category": "concepts",
  "intro": "<p>Imprisonment in the biblical world served different functions than modern incarceration: it was typically used to hold accused persons awaiting trial or sentence rather than as punishment itself. The OT records prisoners being held in cisterns (Joseph, <strong>Gen. 39:20</strong>; Jeremiah, <strong>Jer. 38:6</strong>), guardhouses, and pits. Military prisoners of war were sometimes enslaved, killed, or mutilated. The Mosaic law did not prescribe imprisonment as a standard punishment.</p><p>The NT narrates numerous imprisonments in the apostolic period: John the Baptist (<strong>Matt. 14:3</strong>), Peter (<strong>Acts 12:4</strong>), Paul and Silas at Philippi (<strong>Acts 16:23–24</strong>), and Paul's extended imprisonments in Caesarea and Rome. Paul wrote several letters from prison (Ephesians, Philippians, Colossians, Philemon, 2 Timothy). He interprets his imprisonment as advancing the gospel: \"What has happened to me has really served to advance the gospel\" (<strong>Phil. 1:12</strong>). Jesus's identification with prisoners — \"I was in prison and you visited me\" (<strong>Matt. 25:36</strong>) — makes ministry to prisoners a mark of genuine discipleship.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Matthew 25:36", "Acts 16:24", "Philippians 1:12", "Genesis 39:20"]
},
"reprobacy": {
  "id": "reprobacy",
  "term": "Reprobacy",
  "category": "concepts",
  "intro": "<p>Reprobacy (or reprobation) denotes the condition of being rejected by God — of having one's conscience and moral sensibility so thoroughly corrupted that divine judgment has been rendered irrevocable. The OT portrays the antediluvian world as wholly given to evil (<strong>Gen. 6:5–7</strong>) and Sodom as beyond reforming (<strong>Gen. 18:20</strong>; <strong>19:13</strong>). Pharaoh's progressive hardening represents a reprobate state reached through prolonged resistance. Esau's sale of his birthright and subsequent inability to find repentance (<strong>Heb. 12:17</strong>) serves as a warning.</p><p>Paul's most explicit treatment is in <strong>Romans 1:18–32</strong>: three times God \"gave them up\" to the consequences of their idolatry and moral corruption — to \"a debased (<em>adokimon</em>) mind\" that no longer functions as a reliable guide to good and evil. The logic is judicial: those who suppress the truth in unrighteousness eventually lose the capacity to receive it. This is distinguished from election and reprobation as theological categories in the Calvinist tradition, which grounds the reprobate's condemnation in their own sin while attributing salvation entirely to God's mercy.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Romans 1:28", "Genesis 6:5", "Hebrews 12:17", "2 Timothy 3:8"]
},
"resignation": {
  "id": "resignation",
  "term": "Resignation",
  "category": "concepts",
  "intro": "<p>Resignation in Scripture is the posture of accepting God's will even in suffering — not passive fatalism but active trust that God's purposes are good even when circumstances are painful. Job's initial response to his losses is the paradigm: \"The LORD gave, and the LORD has taken away; blessed be the name of the LORD\" (<strong>Job 1:21</strong>). This resignation is not stoic indifference but faith-based submission to sovereign goodness, maintained even when circumstances suggest otherwise.</p><p>The psalms of lament model resignation through complaint: the psalmist pours out his distress, questions God's seeming absence, and yet ends with renewed trust and praise (<strong>Ps. 46:10</strong>: \"Be still, and know that I am God\"). Jesus's Gethsemane prayer is the NT's supreme example: \"not my will, but yours, be done\" (<strong>Luke 22:42</strong>) — genuine resistance to the cup of suffering resolved into submission to the Father's purpose. Paul's teaching on contentment in all circumstances (<strong>Phil. 4:11–13</strong>) and the acceptance of his thorn in the flesh (<strong>2 Cor. 12:9–10</strong>) exemplify Christian resignation as the doorway to supernatural sufficiency.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Job 1:21", "Luke 22:42", "Philippians 4:11", "2 Corinthians 12:9"]
},
"scoffing": {
  "id": "scoffing",
  "term": "Scoffing",
  "category": "concepts",
  "intro": "<p>Scoffing (mockery, scorning) is the deliberate disparagement of divine things, godly people, or the message of repentance — treated in Scripture as the most hardened form of spiritual resistance. The Psalms begin with the warning not to sit \"in the seat of scoffers\" (<strong>Ps. 1:1</strong>). Proverbs returns repeatedly to the scoffer (<em>luts</em>): he hates reproof (<strong>Prov. 9:7–8</strong>), will not respond to wisdom (<strong>Prov. 13:1</strong>), and stirs up contention (<strong>Prov. 22:10</strong>). Scoffers mocked Israel's returning exiles (<strong>Neh. 2:19</strong>) and jeered Hezekiah's messengers (<strong>2 Chr. 30:10</strong>).</p><p>Peter warns that in the last days scoffers will come following their own lusts and asking \"Where is the promise of his coming?\" (<strong>2 Pet. 3:3–4</strong>). Jude echoes this, citing the apostles' prediction of such mockers (<strong>Jude 18</strong>). The mockers at the cross — \"He saved others; he cannot save himself\" (<strong>Matt. 27:42</strong>) — ironically articulate the theology of substitutionary sacrifice while intending to deny it. Scoffing at divine things represents a particular spiritual danger because it armors the heart against conviction and repentance.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Psalms 1:1", "2 Peter 3:3", "Proverbs 9:7", "Matthew 27:42"]
},
"sorcery": {
  "id": "sorcery",
  "term": "Sorcery",
  "category": "concepts",
  "intro": "<p>Sorcery, witchcraft, and divination encompass the attempts to manipulate supernatural forces or obtain hidden knowledge through means other than God's revealed word. The Mosaic law absolutely prohibited all forms: divination, omens, augury, sorcery, charming, consulting mediums or necromancers (<strong>Deut. 18:9–14</strong>; <strong>Lev. 19:26–31</strong>; <strong>20:6</strong>). The death penalty applied to anyone who practiced as a medium or spiritist (<strong>Lev. 20:27</strong>). The rationale is theological: these practices belong to the nations who are being driven out and represent reliance on anything other than God.</p><p>Despite the prohibitions, sorcery pervaded Israelite history: Saul consulted the witch of Endor in desperation (<strong>1 Sam. 28:7–20</strong>), and Manasseh \"dealt with mediums and necromancers\" among his many abominations (<strong>2 Kings 21:6</strong>). In the NT, Simon Magus practiced sorcery in Samaria (<strong>Acts 8:9–11</strong>), and Elymas the sorcerer opposed Paul in Cyprus (<strong>Acts 13:8</strong>). Revelation includes \"sorcerers\" among those excluded from the heavenly city (<strong>Rev. 22:15</strong>; <strong>21:8</strong>), and the Greek term <em>pharmakeia</em> (sorcery, drug-use for occult purposes) appears in the works of the flesh (<strong>Gal. 5:20</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Deuteronomy 18:9", "Galatians 5:20", "Acts 8:9", "Revelation 22:15"]
},
"thaddeus": {
  "id": "thaddeus",
  "term": "Thaddeus",
  "category": "people",
  "intro": "<p>Thaddeus is listed as one of the twelve apostles in <strong>Matthew 10:3</strong> and <strong>Mark 3:18</strong>. Comparison with Luke's lists (<strong>Luke 6:16</strong>; <strong>Acts 1:13</strong>), which give \"Judas son of James\" in the same position, has led most scholars to identify Thaddeus with Judas son of James — one person known by three names: Judas, Thaddeus, and (according to Matthew) Lebbaeus. The name Thaddeus may derive from an Aramaic root meaning \"breast\" or may be a nickname, and Lebbaeus similarly may mean \"heart.\"</p><p>He appears in John's Gospel as \"Judas (not Iscariot)\" who asks Jesus at the Last Supper why he manifests himself to the disciples and not to the world (<strong>John 14:22</strong>). This brief exchange is the only spoken word attributed to him. He is traditionally identified with Jude the author of the epistle, who names himself \"Jude, a servant of Jesus Christ and brother of James\" — the same James as his father in Luke's list. His subsequent ministry is obscure; tradition places his work in Mesopotamia and Persia.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Matthew 10:3", "Mark 3:18", "John 14:22", "Luke 6:16"]
},
"tryphena": {
  "id": "tryphena",
  "term": "Tryphena and Tryphosa",
  "category": "people",
  "intro": "<p>Tryphena and Tryphosa (meaning: <em>luxurious</em>) are two women greeted by Paul at the close of his epistle to the Romans: \"Greet those workers in the Lord, Tryphena and Tryphosa\" (<strong>Rom. 16:12</strong>). The similarity of their names suggests they were sisters, possibly twins, though they may simply have been fellow workers in the same church community. Their designation as \"workers in the Lord\" places them in the same category of active Christian ministry as others Paul commends in Romans 16 — a chapter remarkable for the number of women it honors as significant contributors to the early church.</p><p>Beyond this single verse nothing is known of them. Their Latin names suggest Roman citizenship or origin. The closing chapter of Romans 16, with its greetings to Priscilla, Mary, Junia, Tryphena, Tryphosa, Persis, and others, provides evidence of the substantial role women played in the establishment of the Roman Christian community before Paul himself had visited the city.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Romans 16:12"]
},
"types": {
  "id": "types",
  "term": "Types",
  "category": "concepts",
  "intro": "<p>Biblical typology is the interpretive framework that identifies OT persons, events, and institutions as divinely designed prefigurations of NT realities — particularly the person and work of Christ. The Greek word <em>typos</em> (\"pattern, impression\") is used in this sense in <strong>Romans 5:14</strong>, where Adam is called \"a type (<em>typos</em>) of the one who was to come\" (Christ). Similarly, the bronze serpent lifted up in the wilderness is a type of Christ lifted up on the cross (<strong>John 3:14</strong>), and the Passover lamb prefigures Christ our Passover (<strong>1 Cor. 5:7</strong>).</p><p>The Letter to the Hebrews is the NT's most sustained typological argument: the Levitical priesthood, tabernacle, and sacrificial system are \"a shadow of the good things to come\" (<strong>Heb. 10:1</strong>), all finding their fulfillment and supersession in Christ the high priest who entered the true heavenly sanctuary with his own blood (<strong>Heb. 9:11–12</strong>). Other prominent types include Melchizedek (prefiguring Christ's royal-priestly office, <strong>Heb. 7</strong>), Noah's ark (prefiguring baptism, <strong>1 Pet. 3:21</strong>), and the manna in the wilderness (prefiguring the bread of life, <strong>John 6:31–35</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Romans 5:14", "1 Corinthians 5:7", "Hebrews 10:1", "John 3:14"]
},
"unselfishness": {
  "id": "unselfishness",
  "term": "Unselfishness",
  "category": "concepts",
  "intro": "<p>Unselfishness — the disposition to seek others' good rather than one's own — is presented in the NT as a direct implication of the gospel and the love commandment. Paul's description of love in <strong>1 Corinthians 13:5</strong> includes that love \"does not insist on its own way.\" His appeal in <strong>Romans 15:1–3</strong> is explicit: \"We who are strong have an obligation to bear with the failings of the weak, and not to please ourselves... For Christ did not please himself.\" The Christ hymn of <strong>Philippians 2:3–8</strong> grounds unselfishness in the incarnation: \"Do nothing from selfish ambition or conceit, but in humility count others more significant than yourselves... Have this mind among yourselves, which is yours in Christ Jesus.\"</p><p>Paul's own apostolic ministry exemplifies this: he foregoes his apostolic right to financial support to avoid putting an obstacle before the gospel (<strong>1 Cor. 9:12</strong>), and he becomes \"all things to all people\" for the sake of their salvation (<strong>1 Cor. 9:22</strong>). Ultimately, Christ's incarnation and cross are the supreme demonstration of unselfishness: \"though he was rich, yet for your sake he became poor\" (<strong>2 Cor. 8:9</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Philippians 2:4", "Romans 15:1", "1 Corinthians 9:22", "2 Corinthians 8:9"]
},
"waiting": {
  "id": "waiting",
  "term": "Waiting",
  "category": "concepts",
  "intro": "<p>Waiting on God is a recurring posture of biblical faith — the patient, expectant trust that God will act in his own time and on his own terms. The Hebrew <em>qawah</em> (\"to wait, hope, expect\") and <em>chakah</em> (\"to wait for, long for\") carry the sense of tense expectation rather than passive inactivity. The classic expression: \"They who wait for the LORD shall renew their strength; they shall mount up with wings like eagles\" (<strong>Isa. 40:31</strong>). The psalmist repeatedly urges waiting: \"Be still before the LORD and wait patiently for him\" (<strong>Ps. 37:7</strong>); \"Wait for the LORD; be strong, and let your heart take courage; wait for the LORD!\" (<strong>Ps. 27:14</strong>).</p><p>Waiting is the appropriate response when God has promised but not yet delivered. Abraham and Sarah waited for a son; Israel waited for deliverance from Egypt and from exile; Simeon and Anna waited for the consolation of Israel (<strong>Luke 2:25, 38</strong>). The NT opens a new dimension of waiting: the Spirit is the \"guarantee\" of the coming inheritance, and believers groan inwardly \"as we wait eagerly for adoption as sons\" and the redemption of bodies (<strong>Rom. 8:23</strong>). The early church's eschatological watchword — \"Come, Lord Jesus\" (<strong>Rev. 22:20</strong>) — is waiting expressed as prayer.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Isaiah 40:31", "Psalms 27:14", "Romans 8:23", "Revelation 22:20"]
},
"watchfulness": {
  "id": "watchfulness",
  "term": "Watchfulness",
  "category": "concepts",
  "intro": "<p>Watchfulness is the posture of alert spiritual attention — being on guard against sin, temptation, apostasy, and false teaching, and remaining ready for the Lord's return. The OT figure of the watchman (<em>tsopheh</em>) stood on the city walls to warn of approaching danger; Ezekiel applies this to the prophet's vocation (<strong>Ezek. 3:17</strong>; <strong>33:6–7</strong>). The Proverbs urge guarding the heart \"with all vigilance\" (<strong>Prov. 4:23</strong>).</p><p>Jesus's eschatological teaching centers on watchfulness: \"Watch therefore, for you know neither the day nor the hour\" (<strong>Matt. 25:13</strong>); \"Stay awake\" (<strong>Mark 13:35–37</strong>). Gethsemane shows disciples who fail to watch even for an hour (<strong>Matt. 26:40–41</strong>). Peter's injunction to \"be sober-minded; be watchful. Your adversary the devil prowls around like a roaring lion, seeking someone to devour\" (<strong>1 Pet. 5:8</strong>) connects watchfulness to spiritual warfare. Paul's farewell to the Ephesian elders is a call to vigilant oversight of the flock against wolves from within and without (<strong>Acts 20:28–31</strong>). The seals of Revelation repeatedly call the churches to hear and watch.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Matthew 25:13", "1 Peter 5:8", "Ezekiel 33:6", "Acts 20:28"]
},
"bride-bridegroom": {
  "id": "bride-bridegroom",
  "term": "Bride and Bridegroom",
  "category": "concepts",
  "intro": "<p>The marriage metaphor — God as husband to Israel, Christ as bridegroom to the church — is one of the most sustained and theologically rich images in Scripture. Hosea's marriage to the unfaithful Gomer dramatizes God's covenant faithfulness to an adulterous Israel (<strong>Hos. 1–3</strong>). Isaiah 62:5 declares: \"As the bridegroom rejoices over the bride, so shall your God rejoice over you.\" Jeremiah uses the sound of bride and bridegroom as a symbol of normalcy whose absence marks judgment (<strong>Jer. 7:34</strong>; <strong>16:9</strong>; <strong>25:10</strong>).</p><p>John the Baptist identifies himself as the \"friend of the bridegroom\" who rejoices at the bridegroom's voice (<strong>John 3:29</strong>). Jesus describes himself as the bridegroom in the parable of the ten virgins (<strong>Matt. 25:1–13</strong>) and teaches that his presence makes fasting inappropriate — the wedding guests do not fast while the bridegroom is with them (<strong>Matt. 9:15</strong>). Paul presents Christian marriage as a sign of Christ's relationship to the church (<strong>Eph. 5:25–32</strong>). The consummation of all things is described as \"the wedding of the Lamb\" and \"the Bride, the wife of the Lamb\" — the new Jerusalem (<strong>Rev. 19:7–9</strong>; <strong>21:2, 9</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Revelation 21:2", "Matthew 25:1", "John 3:29", "Ephesians 5:25"]
},
"canon-of-scripture-the": {
  "id": "canon-of-scripture-the",
  "term": "Canon of Scripture",
  "category": "concepts",
  "intro": "<p>The canon of Scripture is the authoritative collection of books recognized by the church as constituting the written Word of God. The word <em>canon</em> (Greek <em>kanon</em>, \"rule\" or \"straight rod\") was applied to Scripture in the 4th century A.D. to describe the recognized list of books that serve as the normative rule of Christian faith and practice. The OT canon was essentially fixed within Judaism before the NT period — Jesus and the apostles cite books from the Law, Prophets, and Writings as authoritative Scripture, without debating their canonical status.</p><p>The NT canon developed through the 1st–4th centuries. The criteria for canonical recognition included: apostolic authorship or authorization, catholicity (recognition across the church), and doctrinal consistency with the rule of faith. The Council of Carthage (A.D. 397) formally listed the 27 books of the NT as canonical. Protestants follow a 66-book canon (39 OT + 27 NT), while Roman Catholics include 7 additional deuterocanonical books in the OT. The canon is not a human creation but the church's recognition and ratification of what God had already inspired (<strong>2 Tim. 3:16</strong>; <strong>2 Pet. 1:21</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["2 Timothy 3:16", "2 Peter 1:21", "Luke 24:44"]
},
"condescension-of-god": {
  "id": "condescension-of-god",
  "term": "Condescension of God",
  "category": "concepts",
  "intro": "<p>The condescension of God — his gracious stooping to engage with creatures infinitely beneath him — is a recurring theological theme in both Testaments. God is the \"High and Exalted One who lives forever, whose name is Holy,\" who yet dwells with the contrite and lowly in spirit (<strong>Isa. 57:15</strong>). His appearing to Abraham to negotiate over Sodom (<strong>Gen. 18:1–33</strong>), his speaking to Moses \"face to face, as a man speaks with his friend\" (<strong>Ex. 33:11</strong>), and his taking up residence among Israel in the tabernacle and temple are acts of divine accommodation — the infinite condescending to the finite.</p><p>The supreme act of divine condescension is the incarnation: \"The Word became flesh and dwelt among us\" (<strong>John 1:14</strong>). Christ, who was in the form of God, \"did not count equality with God a thing to be grasped, but emptied himself, by taking the form of a servant, being born in the likeness of men\" (<strong>Phil. 2:6–7</strong>). Even the gift of Scripture is an act of condescension — God accommodating infinite revelation to finite human language and cultural forms so that his creatures might know him. This theological principle (accommodation, <em>condescensio</em>) was developed systematically by Calvin.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["John 1:14", "Philippians 2:7", "Isaiah 57:15", "Exodus 33:11"]
},
"judas-jude": {
  "id": "judas-jude",
  "term": "Judas (Jude)",
  "category": "people",
  "intro": "<p>Judas (Greek form; Hebrew <em>Yehudah</em>, \"praise\") is one of the most common names in the NT period. Beyond Judas Iscariot (the betrayer), the NT mentions several others: (1.) Judas son of James (also called Thaddaeus/Lebbaeus), one of the Twelve (<strong>Luke 6:16</strong>; <strong>John 14:22</strong>). (2.) Judas, brother of Jesus (<strong>Matt. 13:55</strong>; <strong>Mark 6:3</strong>), traditionally identified as the author of the epistle of Jude (who calls himself \"brother of James,\" <strong>Jude 1</strong>). (3.) Judas of Galilee, the revolutionary (<strong>Acts 5:37</strong>). (4.) Judas Barsabbas, a leader sent with Paul and Barnabas to Antioch (<strong>Acts 15:22</strong>). (5.) Judas, the man in Damascus at whose house Paul stayed after his conversion (<strong>Acts 9:11</strong>).</p><p>The name's frequency reflects the tribal pride in Judah throughout Second Temple Judaism. The betrayer's infamy has made the name \"Judas\" synonymous with treachery in western languages, though the name itself simply means \"praise\" and was honorably borne by many.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Matthew 10:4", "Luke 6:16", "Jude 1:1", "Acts 5:37"]
},
"ptolemaeus-or-ptolemy": {
  "id": "ptolemaeus-or-ptolemy",
  "term": "Ptolemy",
  "category": "people",
  "intro": "<p>Ptolemy was the dynastic name of the Greek rulers of Egypt from the death of Alexander the Great (323 B.C.) until the Roman conquest (30 B.C.). The dynasty was founded by Ptolemy I Soter (\"Savior\"), one of Alexander's generals. His son Ptolemy II Philadelphus (285–246 B.C.) is credited with sponsoring the Septuagint translation of the Hebrew scriptures into Greek in Alexandria, making the OT accessible to the Hellenistic world. The Ptolemaic dynasty controlled Palestine (the land of Israel) from 301 to 198 B.C., when the Seleucids defeated Ptolemy V at Panion.</p><p>Daniel 11 contains detailed prophecies of the wars between \"the king of the south\" (the Ptolemies) and \"the king of the north\" (the Seleucids), with Palestine as the contested territory between them. The Ptolemies appear in the Books of Maccabees (Apocrypha) as political actors during the Maccabean period. The dynasty ended with Cleopatra VII, who lost to Octavian (Augustus), making Egypt a Roman province.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Daniel 11:5", "Daniel 11:14"]
},
"rich-the": {
  "id": "rich-the",
  "term": "Rich, The",
  "category": "concepts",
  "intro": "<p>Scripture's treatment of wealth is not uniformly negative — Abraham, Job, David, and Solomon were wealthy, and riches are sometimes described as a blessing from God (<strong>Deut. 8:18</strong>; <strong>Prov. 10:22</strong>). However, the OT prophets repeatedly condemn the exploitation of the poor by the rich (<strong>Amos 2:6–7</strong>; <strong>Isa. 5:8</strong>; <strong>Mic. 2:1–2</strong>), and Proverbs warns that riches are precarious and can lead the heart away from God (<strong>Prov. 11:28</strong>; <strong>30:8–9</strong>).</p><p>Jesus's teaching is the sharpest in Scripture: \"It is easier for a camel to go through the eye of a needle than for a rich person to enter the kingdom of God\" (<strong>Matt. 19:24</strong>). The rich young ruler's departure illustrates the danger of wealth as a rival lord. The parable of the rich man and Lazarus (<strong>Luke 16:19–31</strong>) depicts reversal in eternity. Paul does not condemn wealth per se but warns of the love of money as a root of all kinds of evil (<strong>1 Tim. 6:10</strong>) and instructs the rich to be generous, storing up treasure for the age to come (<strong>1 Tim. 6:17–19</strong>). James warns the rich who oppress workers and live in self-indulgence (<strong>James 5:1–6</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Matthew 19:24", "1 Timothy 6:10", "James 5:1", "Luke 16:23"]
},
"scribe-s": {
  "id": "scribe-s",
  "term": "Scribes",
  "category": "people",
  "intro": "<p>Scribes (<em>sopherim</em>) were professional writers and copyists who played an increasingly important role in Jewish religious life from the post-exilic period onward. In the early monarchy they served as royal secretaries and administrators (<strong>2 Sam. 8:17</strong>; <strong>2 Kings 12:10</strong>). After the exile, Ezra is the paradigmatic scribe: \"a scribe skilled in the Law of Moses\" who studied, practiced, and taught the law of the LORD (<strong>Ezra 7:6, 10</strong>). By the Second Temple period, the scribes had become the professional interpreters and teachers of Torah, alongside and sometimes in tension with the priests.</p><p>In the NT the scribes (often paired with Pharisees) are frequent interlocutors with Jesus — questioning, testing, and opposing him. Jesus acknowledged their teaching authority (\"The scribes and the Pharisees sit on Moses's seat,\" <strong>Matt. 23:2</strong>) while sharply criticizing their hypocrisy. He contrasted his own authority with theirs: he taught \"as one having authority, and not as their scribes\" (<strong>Matt. 7:29</strong>). The \"scribe trained for the kingdom of heaven\" in Matthew 13:52 presents an ideal of one who brings out of his treasure \"things new and old.\"</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Ezra 7:6", "Matthew 7:29", "Matthew 23:2", "2 Samuel 8:17"]
},
"veil": {
  "id": "veil",
  "term": "Veil",
  "category": "concepts",
  "intro": "<p>Veils appear in Scripture in two distinct contexts: as items of dress and as a structural feature of the tabernacle and temple. As clothing, veils were worn by women in certain contexts — Rebekah veiled herself when meeting Isaac (<strong>Gen. 24:65</strong>), and the Song of Solomon speaks of the beloved's veil (<strong>Song 4:1</strong>; <strong>6:7</strong>). Smith's dictionary notes that veiling was far less universal in ancient Israel than in post-Koranic Islamic culture; unveiled women were normal in many contexts. Paul addresses head covering in worship in <strong>1 Corinthians 11:2–16</strong>, a passage whose cultural and theological interpretation remains much debated.</p><p>The most theologically significant veil in Scripture is the curtain separating the Holy Place from the Most Holy Place in the tabernacle and temple (<strong>Ex. 26:31–35</strong>). Moses's veil over his shining face (<strong>Ex. 34:33–35</strong>) becomes in Paul's interpretation a symbol of the partial and fading glory of the old covenant, in contrast to the unveiled face of those who behold the glory of the Lord in the gospel (<strong>2 Cor. 3:12–18</strong>). The tearing of the temple veil at the crucifixion (<strong>Matt. 27:51</strong>) signifies the opening of direct access to God through Christ's atoning death (<strong>Heb. 10:19–20</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Matthew 27:51", "Hebrews 10:19", "2 Corinthians 3:14", "Exodus 26:31"]
},
"versions-ancient-of-the-old-and-new-testaments": {
  "id": "versions-ancient-of-the-old-and-new-testaments",
  "term": "Versions, Ancient",
  "category": "concepts",
  "intro": "<p>The ancient versions of Scripture are early translations of the Hebrew OT and Greek NT into other languages, produced to serve communities whose native language differed from the original. They are critical resources for textual criticism, since they sometimes preserve readings earlier than the oldest surviving Hebrew or Greek manuscripts. The principal ancient versions include:</p><p>The <strong>Septuagint</strong> (LXX) — Greek translation of the OT, begun in Alexandria c. 250 B.C., used extensively by the NT writers and early church. The <strong>Targums</strong> — Aramaic paraphrases of the OT. The <strong>Syriac Peshitta</strong> — the OT and NT in Syriac, the primary Bible of eastern Christianity. The <strong>Latin Vulgate</strong> — Jerome's translation (c. A.D. 382–405), which became the standard Bible of the western church for over a millennium. The <strong>Ethiopic</strong>, <strong>Coptic</strong>, <strong>Armenian</strong>, and <strong>Gothic</strong> versions served the churches of their respective regions. Each version reflects the textual tradition available to its translators and the interpretive choices of its era, making them collectively invaluable for reconstructing the history of the biblical text.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["Nehemiah 8:8", "Luke 24:44"]
},
"versions-authorized": {
  "id": "versions-authorized",
  "term": "Authorized Version",
  "category": "concepts",
  "intro": "<p>The Authorized Version (AV), commonly called the King James Version (KJV), is the English translation of the Bible produced in 1611 at the command of King James I of England. It was prepared by a committee of 47 scholars organized into six groups working at Westminster, Oxford, and Cambridge, each assigned specific books of the Bible. The translation built on the foundation of Tyndale's pioneering English NT (1526) and subsequent versions — Coverdale (1535), the Great Bible (1539), the Geneva Bible (1560), and the Bishops' Bible (1568) — refining and synthesizing their work.</p><p>The KJV's text is based on the Greek Textus Receptus for the NT (following Erasmus's critical edition) and the Hebrew Masoretic Text for the OT. Its influence on English literature, language, and culture has been enormous; phrases and rhythms from the KJV have entered the English language at every level. Modern critical scholarship works from earlier and more numerous manuscripts than were available in 1611, and modern translations (RSV, ESV, NIV, NASB) reflect both text-critical advances and the need to render biblical idiom into contemporary English.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["2 Timothy 3:16"]
},
"vulgate-the": {
  "id": "vulgate-the",
  "term": "Vulgate",
  "category": "concepts",
  "intro": "<p>The Vulgate is Jerome's Latin translation of the Bible, produced primarily between A.D. 382 and 405 at the commission of Pope Damasus I. Jerome translated the OT directly from Hebrew (a radical innovation, since earlier Latin versions, the Vetus Latina, were based on the Greek Septuagint) and revised the existing Latin NT using Greek manuscripts. The Vulgate's name (from Latin <em>vulgata editio</em>, \"common edition\") reflects its eventual status as the Bible in common use throughout the medieval western church.</p><p>For over a millennium, the Vulgate was the virtually sole Bible of western Christianity, shaping the theological vocabulary of the Latin West (terms like <em>gratia</em>, <em>paenitentia</em>, <em>sacramentum</em>, <em>fides</em> entered Christian usage through Jerome's translation choices). The Council of Trent (1546) declared it the authentic Latin version for doctrinal use. The Reformers' return to the Greek and Hebrew originals, enabled by Renaissance scholarship, led to new vernacular translations independent of the Vulgate — most notably Luther's German Bible (1534) and the English Authorized Version (1611).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["smith"],
  "key_refs": ["2 Timothy 3:16", "Luke 24:44"]
},
"festus": {
  "id": "festus",
  "term": "Festus",
  "category": "people",
  "intro": "<p>Porcius Festus was the Roman procurator of Judea who succeeded Felix approximately A.D. 59–60 and held office until his death around A.D. 62. He inherited the case of Paul, who had been imprisoned by Felix for two years in Caesarea. When the Jerusalem Jewish leaders pressed Festus to have Paul transferred to Jerusalem (where they planned to kill him), Paul exercised his right as a Roman citizen and appealed his case to Caesar (<strong>Acts 25:11–12</strong>).</p><p>Festus appears as a relatively fair-minded official who acknowledged he found no capital offense in Paul's case but was perplexed by the religious dispute involved. When King Herod Agrippa II and his sister Bernice visited Caesarea, Festus presented Paul's case to them, saying he could find nothing to write to Caesar since the accusations were about \"their own religion and about a certain Jesus, who was dead, but whom Paul asserted to be alive\" (<strong>Acts 25:19</strong>). Paul's defense before Agrippa provoked Festus's declaration: \"Paul, you are out of your mind; your great learning is driving you mad\" (<strong>Acts 26:24</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["nave"],
  "key_refs": ["Acts 24:27", "Acts 25:11", "Acts 25:19", "Acts 26:24"]
},
}

def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f"BP gap-orphans: wrote {written}, skipped {skipped} existing.")

main()
