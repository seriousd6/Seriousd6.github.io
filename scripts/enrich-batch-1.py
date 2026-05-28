#!/usr/bin/env python3
"""Enrich books 1-10: Genesis through 2 Samuel."""
import json, os

OUT = os.path.join(os.path.dirname(__file__), '..', 'data', 'books', 'introductions')

ENRICHMENTS = {
  "genesis": {
    "key_people": [
      {"name": "Adam & Eve", "role": "First humans; their rebellion introduces sin, shame, and death into God's good creation"},
      {"name": "Noah", "role": "Righteous man preserved through the flood; receives the covenant of the rainbow, prefiguring new creation"},
      {"name": "Abraham", "role": "Father of the covenant nation; his faith is the defining model of justification by grace through trust in God's word"},
      {"name": "Isaac", "role": "Child of the promise born against all natural hope; his near-sacrifice on Moriah prefigures the substitutionary atonement"},
      {"name": "Jacob", "role": "Patriarch of the twelve tribes; his life of striving and transformation shows that election is by grace, not merit"},
      {"name": "Joseph", "role": "Rejected by his brothers yet sovereignly exalted; the most sustained OT type of Christ's humiliation, suffering, and glory"}
    ],
    "context": "Genesis was written to Israel on the eve of the conquest of Canaan, grounding a newly-formed nation in its identity as God's covenant people. Ancient Near Eastern creation and flood accounts (Enuma Elish, the Gilgamesh Epic) form the cultural backdrop that Genesis directly counters, asserting that one sovereign God — not a pantheon — is the uncreated Creator of all things.",
    "christ_connection": "Genesis anticipates Christ from its opening pages: the protoevangelium promises a seed of the woman who will crush the serpent (3:15), the ram substituted for Isaac on Moriah foreshadows substitutionary atonement (22:13), and Joseph's pattern of rejection, suffering, and exaltation is the closest narrative parallel to the gospel in the entire OT. The scepter prophecy over Judah (49:10) anchors the messianic line that runs from Genesis to Revelation.",
    "key_verses": [
      {"ref": "Genesis 1:1", "note": "The foundational declaration: God alone is the uncreated, sovereign Creator of all that exists"},
      {"ref": "Genesis 3:15", "note": "The protoevangelium — the first messianic promise of the seed who will crush the serpent's head"},
      {"ref": "Genesis 12:1-3", "note": "The Abrahamic covenant: land, seed, and worldwide blessing — the structural backbone of all redemptive history"},
      {"ref": "Genesis 50:20", "note": "Joseph's verdict on his own suffering: the clearest OT statement of God's sovereign providence over evil"}
    ],
    "themes_detail": [
      {"title": "Creation and the Sovereignty of God", "text": "God speaks the cosmos into existence from nothing by his word alone, establishing his absolute sovereignty over all creation. Unlike the myths of surrounding cultures, there is no cosmic battle, no co-eternal matter, and no rival deity — God acts with sovereign freedom and declares his creation 'very good.' This foundational truth shapes every subsequent biblical doctrine: God's ownership of the world, humanity's dignity as image-bearers, and the ground for redemption."},
      {"title": "The Fall and Its Far-Reaching Consequences", "text": "Human rebellion in the garden shatters the original shalom: guilt and shame replace innocence, enmity replaces harmony, and death enters a world made for life. Yet even in judgment, grace appears immediately — God clothes the guilty pair and announces a coming deliverer. Every subsequent human problem, and every subsequent act of redemption, flows from this pivotal rupture."},
      {"title": "Covenant and Election", "text": "God's sovereign choice of Noah, Abraham, Isaac, and Jacob — none of whom merit it — establishes election as the engine of redemptive history. The Abrahamic covenant (chs. 12, 15, 17) is the defining promise: land, seed, and blessing to all nations through this chosen line. Election in Genesis is never an end in itself but always in service of the worldwide blessing God has purposed since Eden."},
      {"title": "Providence and Suffering", "text": "Joseph's story (chs. 37–50) is the Bible's most sustained meditation on divine providence operating through human evil. God does not merely permit the betrayal, the slavery, and the imprisonment — he works through them with perfect precision to preserve life and keep the covenant line alive. This pattern anticipates the cross, where the greatest injustice in history simultaneously accomplished the greatest act of redemption."}
    ]
  },

  "exodus": {
    "key_people": [
      {"name": "Moses", "role": "Deliverer, lawgiver, and mediator of the Sinai covenant; the supreme OT type of the prophet-redeemer"},
      {"name": "Aaron", "role": "Moses' brother and first high priest; his role as mediating priest between God and the people points forward to the Levitical system"},
      {"name": "Miriam", "role": "Prophetess and worship leader; leads Israel in the first recorded song of salvation after the Red Sea crossing"},
      {"name": "Pharaoh", "role": "The hardened king of Egypt whose refusal to release Israel occasions the ten plagues demonstrating YHWH's supremacy"},
      {"name": "Jethro", "role": "Moses' Midianite father-in-law who counsels him on delegation; a Gentile who recognizes the greatness of Israel's God"}
    ],
    "context": "Israel has been enslaved in Egypt for four centuries; the Exodus occurs against the backdrop of the Egyptian New Kingdom (c. 1550–1070 BC), the most powerful empire in the ancient world. God's liberation of a nation of slaves from the greatest superpower on earth establishes the paradigm for redemption that the entire Bible develops — salvation is always by grace, always through blood, and always creates a covenant community.",
    "christ_connection": "Every major element of Exodus is fulfilled in Christ: he is the Passover Lamb whose blood protects from judgment (1 Cor 5:7), the manna from heaven that sustains his people (John 6:35), and the water from the rock in the wilderness (1 Cor 10:4). The tabernacle — God dwelling in the midst of his people — is explicitly echoed in John 1:14, where the Word 'pitched his tent' among us; and Moses as mediator of the old covenant points to Christ as the mediator of the new (Heb 12:24).",
    "key_verses": [
      {"ref": "Exodus 3:14", "note": "God reveals his personal name 'I AM WHO I AM' — the foundation of all biblical theology about God's self-existence and faithfulness"},
      {"ref": "Exodus 12:13", "note": "The Passover: 'when I see the blood, I will pass over you' — the clearest OT statement of substitutionary, propitiatory atonement"},
      {"ref": "Exodus 20:1-3", "note": "The Ten Commandments open with the gospel: redemption precedes obligation; God saves first, then calls to obedience"},
      {"ref": "Exodus 25:8", "note": "God's stated purpose: 'Let them make me a sanctuary, that I may dwell in their midst' — the goal of all redemption is communion"}
    ],
    "themes_detail": [
      {"title": "Redemption by Grace Through Blood", "text": "The Passover (ch. 12) is the interpretive key to the entire book: Israel is not rescued because of merit but because of blood applied in faith. The plagues systematically demolish Egypt's gods (12:12), demonstrating that YHWH alone is sovereign. The pattern — judgment deserved, a substitutionary sacrifice, redemption by grace — becomes the template for every subsequent act of salvation in Scripture."},
      {"title": "The Law as Covenant Charter", "text": "The Ten Commandments and the Book of the Covenant are not the means of salvation but the constitution of a people already redeemed. The Decalogue begins with the indicative of grace ('I am the LORD your God, who brought you out of Egypt') before any imperative is given. Law in Exodus is always covenant law — the response of gratitude from a liberated people, not the ladder by which they climb to God."},
      {"title": "The Tabernacle: God Dwelling with His People", "text": "The final fourteen chapters of Exodus are devoted to the design and construction of the tabernacle, revealing that the ultimate goal of redemption is not merely freedom from bondage but face-to-face communion with God. Every element — the altar, the veil, the ark, the mercy seat — is a lesson in the holiness of God and the necessity of mediation, all fulfilled in Christ who is simultaneously the altar, the priest, and the sacrifice."},
      {"title": "The Revelation of God's Name and Character", "text": "Exodus is the book of the divine name: YHWH, the self-existent, covenant-keeping God who is present with his people. The 'I AM' declaration at the burning bush (3:14), the proclamation of God's character to Moses (34:6–7), and the theophany at Sinai together form the most concentrated revelation of who God is found anywhere in the OT. Jesus' seven 'I AM' statements in John's Gospel are a direct claim to bear this same name."}
    ]
  },

  "leviticus": {
    "key_people": [
      {"name": "Moses", "role": "Recipient of the priestly laws at Sinai; the mediator who relays God's instructions for the sacrificial system"},
      {"name": "Aaron", "role": "The first high priest; consecrated in Leviticus 8–9; his role as the once-yearly Day of Atonement officiant is the book's dramatic climax"},
      {"name": "Nadab and Abihu", "role": "Aaron's sons who offer unauthorized fire before the LORD and die — a stark warning that God's holiness is not negotiable"},
      {"name": "The Levitical Priests", "role": "Ordained mediators who represent the people before God; their entire existence is a lesson that sinners cannot approach a holy God unaided"}
    ],
    "context": "Leviticus is given at Mount Sinai immediately following the construction of the tabernacle in Exodus, addressing the urgent question facing the newly-redeemed nation: how can sinful people live in the presence of a holy God? The book's priestly legislation has parallels in ancient Near Eastern ritual texts but is uniquely grounded in the character and covenant of YHWH, who is both the consuming fire and the merciful redeemer.",
    "christ_connection": "The letter to the Hebrews is the NT commentary on Leviticus, showing that every sacrifice is a shadow pointing to the one perfect offering of Christ (Heb 10:1–14). The Day of Atonement (Lev 16) is the clearest OT preview of propitiation and substitution: the high priest enters the holy of holies once a year with blood that can never finally cleanse — Christ enters the heavenly sanctuary once for all with his own blood, securing eternal redemption (Heb 9:11–14). The holiness code's command 'Be holy, for I am holy' (11:44) finds its answer in Christ who is our holiness (1 Cor 1:30).",
    "key_verses": [
      {"ref": "Leviticus 11:44", "note": "The theological foundation of the entire book: holiness is not optional but is the defining characteristic required of a people who dwell with a holy God"},
      {"ref": "Leviticus 16:30", "note": "The Day of Atonement: 'you shall be clean before the LORD from all your sins' — the annual preview of the final, perfect cleansing Christ would accomplish"},
      {"ref": "Leviticus 17:11", "note": "'The life of the flesh is in the blood' — the theological basis for blood atonement throughout Scripture, fulfilled in Christ's shed blood"},
      {"ref": "Leviticus 19:18", "note": "Love your neighbor as yourself — the moral summary Jesus identifies as the second greatest commandment, showing ethics flows from holiness"}
    ],
    "themes_detail": [
      {"title": "Holiness: The Central Demand of the Covenant", "text": "The word 'holy' (qadosh) appears more in Leviticus than in any other OT book. Holiness is not merely moral purity but separation — being set apart for God, belonging to him, reflecting his character. The laws about food, disease, sexuality, and worship are all applications of a single principle: the covenant God is wholly other, and his people must be visibly distinct from the nations around them. In Christ, this holiness is both imputed (declared holy through his righteousness) and imparted (progressively formed through the Spirit)."},
      {"title": "Sacrifice and Atonement", "text": "The five major offerings (burnt, grain, peace, sin, guilt) each address a different dimension of the broken relationship between God and humanity. At the center of the sacrificial system is the principle of substitution: the animal dies in place of the offerer. But Hebrews makes clear that animal blood can never ultimately satisfy divine justice — the Levitical sacrifices are pedagogical shadows that teach what will finally be accomplished when the true Lamb of God takes away the sin of the world (John 1:29)."},
      {"title": "Clean and Unclean: The Theology of Boundaries", "text": "The purity laws draw visible boundaries between the sacred and the common, the clean and the unclean, as a daily embodied curriculum in holiness. While many specific regulations are not binding under the new covenant (Mark 7:19; Acts 10), they taught Israel that sin contaminates, that uncleanness spreads, and that restoration requires divine initiative. The deeper lesson — that sin excludes from God's presence and only God-provided cleansing restores — is permanently valid."},
      {"title": "The Priestly Mediation System", "text": "The entire apparatus of priests, offerings, and the tabernacle exists because sinners cannot approach a holy God without a mediator. The Levitical priesthood is therefore not an end in itself but a sign pointing forward: Israel's worship was always mediated, always through blood, always requiring someone to stand between the people and the consuming fire. Hebrews 7–10 shows that this entire system is now surpassed by Christ, who is simultaneously the priest, the sacrifice, and the sanctuary."}
    ]
  },

  "numbers": {
    "key_people": [
      {"name": "Moses", "role": "Israel's leader through 40 years of wilderness; even he fails at Meribah (ch. 20), revealing that no merely human leader can bring God's people into rest"},
      {"name": "Aaron and Miriam", "role": "Moses' siblings who rebel against his leadership (ch. 12); Miriam's leprosy illustrates that no one — not even family — is exempt from God's discipline"},
      {"name": "Caleb and Joshua", "role": "The two faithful spies who trust God's promise despite the giants; they alone of their generation enter the land, embodying the life of faith"},
      {"name": "Korah", "role": "Led the great rebellion against Moses and Aaron; his destruction (ch. 16) warns against unauthorized approaches to God and challenges to God-appointed leadership"},
      {"name": "Balaam", "role": "A non-Israelite prophet hired to curse Israel who instead speaks remarkable messianic blessings, demonstrating that God's purposes cannot be thwarted"}
    ],
    "context": "Numbers spans nearly 40 years (c. 1446–1406 BC) of wilderness wandering between Sinai and the plains of Moab. The two census lists (chs. 1 and 26) bracket a generation that perished in the wilderness through unbelief, and the new generation that will inherit the promise. The book's honest account of Israel's repeated failures is simultaneously a record of God's relentless faithfulness.",
    "christ_connection": "The bronze serpent lifted up on a pole in the wilderness — so that all who looked to it in faith would live (21:8–9) — is explicitly cited by Jesus as a type of his own crucifixion: 'as Moses lifted up the serpent in the wilderness, so must the Son of Man be lifted up, that whoever believes in him may have eternal life' (John 3:14–15). Balaam's oracle of 'a star out of Jacob' (24:17) is an early messianic prophecy, and Paul interprets the water from the rock as Christ himself who accompanied and sustained Israel (1 Cor 10:4).",
    "key_verses": [
      {"ref": "Numbers 6:24-26", "note": "The Aaronic blessing — the most beautiful benediction in the OT, expressing God's desire to bless, protect, and give peace to his people"},
      {"ref": "Numbers 14:18", "note": "God's self-description repeated from Exodus: 'slow to anger and abounding in steadfast love' — his patience with Israel despite their rebellion"},
      {"ref": "Numbers 21:8-9", "note": "The bronze serpent: a visual object lesson in salvation by looking to God's provision in faith, fulfilled in Christ lifted up on the cross"},
      {"ref": "Numbers 24:17", "note": "Balaam's messianic oracle: 'a star shall come out of Jacob' — an early prophecy of the coming King who will rule over all nations"}
    ],
    "themes_detail": [
      {"title": "Faithfulness vs. Unbelief", "text": "The book's central tragedy is Kadesh-Barnea (chs. 13–14), where ten spies persuade the nation to refuse entry to the promised land because they fear the inhabitants. God's verdict is unambiguous: this is unbelief, not prudence, and an entire generation will die without inheriting the promise. The contrast between Caleb and Joshua (who 'followed the LORD fully') and the rest of their generation is Numbers' enduring lesson on the life of faith."},
      {"title": "God's Provision and Guidance in the Wilderness", "text": "Despite Israel's continual rebellion, God never withdraws his provision: the cloud and pillar of fire guide them, manna falls every morning, and water is provided from the rock. The wilderness is not a place of abandonment but of sustained, patient grace — God is forming a people through trial and dependence. Numbers invites its readers to trust that the God who provided in the wilderness will provide in every subsequent wilderness experience."},
      {"title": "Rebellion and Its Consequences", "text": "Numbers contains more episodes of rebellion than any other Pentateuchal book: grumbling about food, Miriam and Aaron's challenge to Moses, the spy report, Korah's insurrection, the Baal Peor apostasy. Each episode and its aftermath teaches that the holy God who redeemed Israel will not indefinitely overlook covenant unfaithfulness. Yet even in judgment, Numbers shows a God who provides a way of restoration — the bronze serpent, the interceding high priest, the scapegoat — never abandoning his people entirely."},
      {"title": "The Priestly Blessing and God's Desire to Bless", "text": "The Aaronic blessing (6:24–26) is placed near the beginning of Numbers as a statement of God's ultimate intention for Israel. Despite all the failures that follow, this is God's purpose: to bless, protect, shine upon, be gracious to, and give peace to his people. The blessing given to Israel through Aaron is the template for the blessing given to the whole world through the greater High Priest, Jesus Christ (Eph 1:3)."}
    ]
  },

  "deuteronomy": {
    "key_people": [
      {"name": "Moses", "role": "The preacher of the three great sermons that constitute Deuteronomy; his life ends here, and he dies outside the promised land, showing even the greatest human leader cannot bring God's people to final rest"},
      {"name": "Joshua", "role": "Moses' successor, commissioned in Deuteronomy 31 to lead Israel into Canaan; the one who will do what Moses could not"},
      {"name": "The New Generation of Israel", "role": "Those who did not witness the Exodus are the primary audience; Moses summons them to own the covenant as their own"}
    ],
    "context": "Delivered entirely on the plains of Moab in the final weeks of Moses' life, Deuteronomy is structured according to the ancient Near Eastern suzerainty treaty form — preamble, historical prologue, stipulations, witnesses, blessings and curses — presenting YHWH as the great King renewing his covenant with a new generation. Written for a people who stood at the threshold of the land, it answers: how do we remain in covenant with the God who redeemed us?",
    "christ_connection": "Moses' prophecy of a coming prophet 'like me' from among the people (18:15) is explicitly fulfilled in Jesus according to Peter (Acts 3:22) and Stephen (Acts 7:37). Jesus himself quotes Deuteronomy three times in his wilderness temptation (Matt 4:4, 7, 10), demonstrating that where Israel failed to obey in the wilderness, he succeeded — living out perfect covenant faithfulness as the true Israel. The promise of circumcision of the heart (30:6) is the new covenant's inward transformation by the Spirit (Jer 31; Ezek 36).",
    "key_verses": [
      {"ref": "Deuteronomy 6:4-5", "note": "The Shema — 'Hear, O Israel: The LORD our God, the LORD is one' — the foundational confession of Israel's faith and the summary of the law according to Jesus"},
      {"ref": "Deuteronomy 18:15", "note": "The promise of a prophet like Moses whom God will raise up — the most direct OT anticipation of a messianic prophetic figure"},
      {"ref": "Deuteronomy 30:6", "note": "God promises to circumcise Israel's heart so they will love him — the new covenant promise of inward transformation"},
      {"ref": "Deuteronomy 32:4", "note": "'The Rock, his work is perfect; for all his ways are justice' — the Song of Moses' testimony to God's absolute faithfulness"}
    ],
    "themes_detail": [
      {"title": "The Shema: Love as the Heart of the Law", "text": "Deuteronomy 6:4–5 is the nerve center of the entire book. The demand to love the LORD with heart, soul, and strength is not a burdensome addition to ritual observance but the inner spirit from which all obedience flows. Moses returns to this demand repeatedly, always grounding it in who God is and what he has done. When Jesus identifies this as the greatest commandment (Matt 22:37), he is affirming that Deuteronomy has understood the law's deepest intention all along."},
      {"title": "Covenant Renewal Across Generations", "text": "Moses is urgently aware that the next generation did not experience the Exodus firsthand. Deuteronomy is his effort to make the covenant existentially real for those who only know it secondhand: 'Not with our fathers did the LORD make this covenant, but with us, who are all of us here alive today' (5:3). The pattern — retell the mighty acts of God, apply the covenant demands, warn against apostasy, call for renewed commitment — is the template for every subsequent act of covenant renewal in Scripture."},
      {"title": "Memory, Warning, and the Danger of Prosperity", "text": "Moses' most urgent warning is not about pagan armies but about the spiritual amnesia that prosperity brings: 'Beware lest you forget the LORD your God' (8:11). Deuteronomy is profoundly realistic about the human tendency to attribute God's blessings to one's own effort and to lose the sense of creaturely dependence that sustains covenant faithfulness. The curses of chapters 27–28, culminating in exile, are not threats of abandonment but the just consequences of choosing the path Moses has warned against."},
      {"title": "Moses as Prophet and the Coming Greater Prophet", "text": "Moses is the paradigmatic prophet — he speaks face to face with God and mediates the covenant to the people. But Deuteronomy itself anticipates that Moses is not the final word: a greater prophet will come, one whose words must be heeded upon pain of divine judgment (18:19). Jesus fulfils this by speaking not 'Moses said' but 'I say to you' — not as a transmitter of God's words but as the Word of God himself, the mediator of the better covenant."}
    ]
  },

  "joshua": {
    "key_people": [
      {"name": "Joshua", "role": "Israel's military and spiritual leader who brings the nation into the promised land; his name (Yeshua, 'YHWH saves') identifies him as a type of Christ the ultimate deliverer"},
      {"name": "Rahab", "role": "A Canaanite prostitute who hides the spies in faith and is saved by the scarlet cord; she becomes an ancestor of Jesus and an illustration of justification by faith (Heb 11:31; Jas 2:25)"},
      {"name": "Caleb", "role": "The faithful spy who at age 85 still claims his inheritance with the same boldness he showed 45 years earlier — the portrait of lifelong, undimmed covenant faith"},
      {"name": "Achan", "role": "Takes forbidden plunder from Jericho, bringing defeat on Israel and revealing that one person's disobedience affects the entire community"},
      {"name": "The Priests", "role": "Lead the conquest by carrying the ark into the Jordan and circling Jericho — the conquest is fundamentally an act of worship, not merely military strategy"}
    ],
    "context": "The conquest of Canaan (c. 1406–1380 BC) takes place in the context of the Late Bronze Age, a period of widespread disruption in the ancient Near East. Joshua follows directly from Deuteronomy's commissioning of Joshua as Moses' successor and demonstrates that God's promises — especially the land promise to Abraham — are not empty words but realities he brings to pass through human obedience and faith.",
    "christ_connection": "Joshua's name is the Hebrew equivalent of the Greek 'Jesus' (both mean 'YHWH saves'), making him the most directly named type of Christ in the OT. Just as Joshua led Israel through the Jordan into the promised land of rest, Jesus leads his people through death and resurrection into the greater rest of salvation — a connection Hebrews 4:8–9 makes explicit, noting that if Joshua had given them true rest, God would not have spoken of another day. Rahab's scarlet cord in the window (2:18) echoes the Passover blood on the doorposts, pointing to the blood of Christ as the sign of salvation.",
    "key_verses": [
      {"ref": "Joshua 1:8-9", "note": "God's charge to Joshua: meditate on the law day and night, be strong and courageous — the pattern of the Spirit-empowered, Word-formed life"},
      {"ref": "Joshua 2:18", "note": "Rahab's scarlet cord: a visible sign of salvation by faith in God's promise, echoing the Passover blood"},
      {"ref": "Joshua 21:45", "note": "'Not one word of all the good promises that the LORD had made to the house of Israel had failed' — the verdict on the conquest"},
      {"ref": "Joshua 24:15", "note": "Joshua's challenge at Shechem: 'as for me and my house, we will serve the LORD' — the summons to covenantal decision"}
    ],
    "themes_detail": [
      {"title": "Faith and Obedience as the Path to Inheritance", "text": "Joshua is above all a book about what God accomplishes through a people who trust and obey. The crossing of the Jordan (ch. 3–4), the fall of Jericho (ch. 6), and the victory at Gibeon (ch. 10) are all impossible military feats achieved by following unconventional divine instructions. The lesson is consistent: the promises of God are received through faith expressed in obedience, not through human strategy or strength. Where Israel trusts and obeys, they are victorious; where they act independently or disobey (Achan, the Gibeonite deception), they suffer the consequences."},
      {"title": "The Faithfulness of God to His Promises", "text": "The hinge verse of the entire book is 21:45: 'Not one word of all the good promises that the LORD had made to the house of Israel had failed; all came to pass.' Joshua is the record of God making good on the land promise given to Abraham five centuries earlier. This faithfulness is not abstract — it is demonstrated through specific battles, specific tribal allotments, and specific cities. God's word endures, and Joshua is his exhibit A."},
      {"title": "Holy War and the Justice of God", "text": "The conquest and the command of herem (total destruction) is one of the most difficult sections of the OT for modern readers. The biblical text presents it as the execution of divine judgment on nations whose iniquity had 'reached its full measure' (Gen 15:16). It is not ethnic cleansing but covenant justice — applied not only to Canaanites (Achan the Israelite is also destroyed) but exempting those who align themselves with Israel's God (Rahab, the Gibeonites). The conquest is both the fulfillment of a specific historical promise and a preview of the final judgment."},
      {"title": "Covenant Renewal and the Choice Before Every Generation", "text": "Joshua ends at Shechem (ch. 24) in a solemn covenant renewal ceremony that mirrors the structure of Deuteronomy: recital of God's past acts, call to decision, warning about the costs of apostasy. Joshua's challenge — 'choose this day whom you will serve' — makes clear that covenant membership is not inherited automatically but must be personally embraced. This pattern of the covenant community being summoned to re-own its commitment recurs throughout the OT and reaches its fullest expression in baptism and the Lord's Supper."}
    ]
  },

  "judges": {
    "key_people": [
      {"name": "Deborah", "role": "Prophetess and judge who leads Israel to victory against Canaan; her prominent role when male leadership has failed is the book's implicit commentary on spiritual decline"},
      {"name": "Gideon", "role": "Called from threshing wheat in a winepress, he defeats 135,000 Midianites with 300 men — then makes an ephod that becomes an idol, showing how quickly deliverance turns to apostasy"},
      {"name": "Jephthah", "role": "An outcast judge whose rash vow illustrates the tragic consequences of impetuous speech; included in the Hebrews 11 hall of faith as a genuine believer despite his failures"},
      {"name": "Samson", "role": "The most famous judge: Nazirite from birth, supernaturally strong, personally undisciplined; his final act of destroying the Philistines at the cost of his own life is the book's most dramatic type of Christ"},
      {"name": "Delilah", "role": "Samson's Philistine lover who betrays him for silver — a recurring picture of the allure of the world that draws God's people away from their calling"}
    ],
    "context": "Covering roughly 1380–1050 BC, Judges depicts Israel's life in Canaan under constant pressure from surrounding cultures and peoples. The closing chapters (17–21) are deliberately placed out of chronological order to provide two case studies — an idolatrous priest and a brutal gang rape — that illustrate the depth of Israel's moral collapse. The repeated phrase 'there was no king in Israel; everyone did what was right in his own eyes' (17:6; 21:25) is the book's diagnostic verdict.",
    "christ_connection": "Each judge is a partial, flawed, temporary deliverer — pointing by contrast and analogy to the need for a perfect and permanent King. Samson's death is the most striking type of Christ: he stands between two pillars with arms outstretched, and his death — accepted willingly — destroys more enemies than his life did (16:30). The Spirit who empowers the judges for special service foreshadows the Spirit poured out on Christ at his baptism and through him at Pentecost. The book's desperate cry for a king is answered not in Saul but ultimately in Jesus.",
    "key_verses": [
      {"ref": "Judges 2:16", "note": "God raises up judges to save Israel from their oppressors — the pattern of grace interrupting deserved judgment that structures the whole book"},
      {"ref": "Judges 2:19", "note": "'But whenever the judge died, they turned back and were more corrupt than their fathers' — the tragic escalation of each cycle showing that external deliverers cannot produce lasting change"},
      {"ref": "Judges 21:25", "note": "'Everyone did what was right in his own eyes' — the book's verdict: Israel needs not just a deliverer but a King who rules the heart"}
    ],
    "themes_detail": [
      {"title": "The Cycle of Sin and the Patience of God", "text": "The characteristic sin-oppression-cry-deliverance-rest-sin pattern repeats seven or more times in Judges, and with each cycle the depth of Israel's sin increases while the quality of her leaders deteriorates. This is not literary monotony but theological argument: no external deliverance can break the internal cycle of sin. What Israel needs — and what the book ultimately cries out for — is a new heart, not just a new judge. God's repeated intervention despite Israel's unfaithfulness is an illustration of grace that exhausts natural expectations."},
      {"title": "The Need for a King", "text": "Judges answers one of the most important structural questions in the OT: why did Israel need a monarchy? The answer is not political expediency but theological necessity — a people who repeatedly return to idolatry and moral chaos need a leader who will govern from the inside out, not just deliver them from external enemies. But the book is careful not to idealize kingship; the question it raises is answered fully only when the Son of David arrives who is both King and the source of the inward transformation his people need."},
      {"title": "God's Grace Despite Faithlessness", "text": "The most remarkable theological fact about Judges is that God keeps rescuing a people who keep abandoning him. He raises up Shamgar when no one asked, he commissions Gideon's 300 against all military reason, he uses even the compromised Samson to begin delivering Israel from the Philistines. The judges are not saved because they are faithful; they are faithful because God, in his grace, keeps giving them another chance. This grace is not cheap — the book carefully records the consequences of every sin — but it is inexhaustible."},
      {"title": "Spiritual and Moral Decline Under Syncretism", "text": "The latter chapters of Judges (17–21) are among the darkest in Scripture, depicting Levites who hire themselves out as private idols priests, tribes who massacre other Israelites, and a gang rape echoing the sin of Sodom. The progression is deliberate: by abandoning the exclusive worship of YHWH, Israel progressively loses the moral framework that distinguished her from the Canaanites she was supposed to displace. The application is timeless: syncretism is not merely a theological error but a moral catastrophe."}
    ]
  },

  "ruth": {
    "key_people": [
      {"name": "Ruth", "role": "A Moabite widow who clings to her mother-in-law's God and people; her loyal love is the book's exemplary portrait of covenant faithfulness and becomes the vehicle of God's redemptive purposes"},
      {"name": "Naomi", "role": "Israelite widow who returns from Moab broken and bitter, calling herself 'Mara' (bitter); her restoration through Ruth and Boaz is the book's narrative arc of grace restoring the bereft"},
      {"name": "Boaz", "role": "Wealthy Bethlehemite landowner who acts as kinsman-redeemer; his generosity, initiative, and willingness to pay the full price of redemption make him the most theologically precise OT type of Christ"},
      {"name": "Orpah", "role": "Ruth's sister-in-law who returns to her own people and gods when Naomi releases her — a foil to Ruth's radical commitment, not condemned but not remembered either"}
    ],
    "context": "Set 'in the days when the judges ruled' (c. 1100 BC), Ruth is a deliberate counter-narrative to the chaos and violence of Judges — set in the same period but showing that even in the darkest times, ordinary faithful people live out covenant love. Bethlehem, the story's setting, is not incidental: it is the town of David and later of Jesus, and the genealogy that closes Ruth (4:17–22) reveals that this intimate domestic story is on the main road of redemptive history.",
    "christ_connection": "Boaz is the richest OT type of Christ as redeemer: he is a kinsman (related to those he redeems), he has the resources to redeem, he is both willing and eager to do so, he pays the full price himself, and he acts out of love rather than legal obligation. The Hebrew word gō'ēl (kinsman-redeemer) is used of God himself throughout the prophets, and its fullest human embodiment in Boaz points directly to the one who became flesh (kinsman), possessed the infinite resources of deity, and willingly gave his life to redeem those who had nothing to offer in return.",
    "key_verses": [
      {"ref": "Ruth 1:16-17", "note": "Ruth's declaration of loyalty — 'Your people shall be my people and your God my God' — one of the most beautiful confessions of covenant commitment in Scripture"},
      {"ref": "Ruth 2:12", "note": "Boaz blesses Ruth for taking refuge under the wings of the LORD — the language of the Psalms applied to a Gentile convert"},
      {"ref": "Ruth 3:9", "note": "Ruth's request to Boaz to 'spread his wings' over her is a marriage proposal and simultaneously a plea for the kinsman-redeemer to act on his covenant obligation"},
      {"ref": "Ruth 4:14", "note": "The women's blessing on Naomi: 'Blessed be the LORD, who has not left you without a redeemer today' — the theological verdict on the entire story"}
    ],
    "themes_detail": [
      {"title": "Loyal Love (Hesed): The Heart of the Covenant", "text": "The Hebrew word hesed — covenant loyalty, steadfast love, lovingkindness — occurs three times in Ruth and is the book's theological center of gravity. Ruth shows hesed to Naomi by refusing to return to Moab; Boaz shows hesed to Ruth by going beyond what the law required; and God shows hesed to both by orchestrating their meeting and blessing their union. Hesed is the love that keeps its promises even when released from obligation — the love that characterizes God himself and that he produces in those who belong to him."},
      {"title": "The Kinsman-Redeemer", "text": "The gō'ēl institution was Israel's social safety net: a near relative who could buy back sold property, marry a widow to preserve the family line, and redeem an enslaved kinsman. Boaz fulfils this role for Naomi and Ruth at personal cost (he purchases the land, he marries Ruth, he secures the inheritance). The theological point is that redemption always costs the redeemer — a truth that is only fully revealed when the incarnate Son of God becomes kin to those he redeems through his own flesh and blood."},
      {"title": "Gentiles in the Covenant People", "text": "Ruth is a Moabite — a member of a nation specifically excluded from the assembly of Israel by the law (Deut 23:3). Yet she is welcomed, she receives covenant blessings, she marries an Israelite, and she appears in the genealogy of the Messiah. Her inclusion is not an exception to the covenant but a revelation of its ultimate purpose: the blessing promised to Abraham was always intended to flow to all nations (Gen 12:3). Ruth is a preview of the worldwide church gathered from every nation through the gospel."},
      {"title": "Providence in Ordinary Life", "text": "God's name appears only in blessings and brief allusions in Ruth; there are no miracles, no theophanies, no direct divine speech. Yet the entire story is a carefully constructed demonstration of divine providence operating through ordinary decisions, coincidences, and kindnesses. Ruth 'happened to come to the part of the field belonging to Boaz' (2:3) — a sentence that looks like accident but is the book's wink at the reader. God governs history not only through spectacular interventions but through the quiet ordering of everyday circumstances."}
    ]
  },

  "1samuel": {
    "key_people": [
      {"name": "Hannah", "role": "Barren woman whose fervent prayer and vow result in Samuel's birth; her song of praise (2:1–10) is the direct model for Mary's Magnificat"},
      {"name": "Samuel", "role": "The last judge and first great prophet; he anoints both Saul and David, functioning as prophet, priest, and judge in a prefigurement of Christ's threefold office"},
      {"name": "Saul", "role": "Israel's first king — impressive in appearance but diminishing in character; his disobedience (chs. 13, 15) disqualifies his dynasty and reveals that Israel's need is not merely for a king but for a king after God's own heart"},
      {"name": "David", "role": "The youngest and least expected son of Jesse, anointed by God as the man after his own heart; his defeat of Goliath, his loyal friendship with Jonathan, and his merciful treatment of Saul establish the character of God's chosen king"},
      {"name": "Jonathan", "role": "Saul's son who recognizes David's divine calling and sacrifices his own claim to the throne in covenant friendship — a portrait of self-giving loyalty"}
    ],
    "context": "Covering approximately 1105–1010 BC, 1 Samuel narrates Israel's turbulent transition from loosely organized tribal confederation (under the judges) to a centralized monarchy. The surrounding nations — Philistia in particular — have a technological and military advantage (iron weapons, standing army) that creates genuine pressure for a stronger political structure. Israel's request for a king 'like the nations' (8:5) is both politically understandable and theologically treacherous.",
    "christ_connection": "Samuel's threefold function as prophet, priest, and judge prefigures the one who holds all three offices permanently and perfectly. David is the central OT type of the messianic king: anointed by the Spirit, shepherd of God's people, warrior who defeats God's enemies, and man after God's own heart. The contrast between the outward impressiveness of Saul and the inward character of David — encapsulated in 16:7 ('the LORD looks on the heart') — announces the standard by which Christ, the perfect King, is finally measured.",
    "key_verses": [
      {"ref": "1 Samuel 2:2", "note": "Hannah's song: 'There is none holy like the LORD; there is none besides you' — the theological declaration that frames the entire book"},
      {"ref": "1 Samuel 13:14", "note": "The LORD has sought a man after his own heart — the announcement that David will replace Saul and the key to understanding what God desires in a king"},
      {"ref": "1 Samuel 16:7", "note": "The LORD looks on the heart, not the outward appearance — the principle that overturns human expectations and explains both Saul's rejection and David's anointing"},
      {"ref": "1 Samuel 17:47", "note": "'The battle is the LORD's' — David's declaration before Goliath that defines the theology of holy war throughout the OT"}
    ],
    "themes_detail": [
      {"title": "The Heart vs. the Outward Appearance", "text": "The contrast between Saul and David is established by 16:7 and never abandoned. Saul is everything Israel could want in a king by human standards: tall, handsome, from a prominent family. David is the runt of the litter, forgotten when his brothers are lined up. But the LORD's evaluation inverts human expectation at every turn. This theme is not merely about individual character; it exposes a fundamental truth about human assessment of leaders and the folly of choosing by appearance, status, or popular acclaim."},
      {"title": "The Failure of Saul and the Promise of David", "text": "Saul's two acts of disobedience (chs. 13, 15) are not minor infractions but reveal a pattern: he prioritizes public approval over obedience to God's word, and he believes partial obedience is adequate. Samuel's verdict — 'to obey is better than sacrifice' (15:22) — is one of the OT's clearest statements that formal religious observance cannot substitute for genuine covenant faithfulness. Saul's decline and David's rise are the book's argument that Israel's king must be not merely powerful but obedient."},
      {"title": "Prayer and the Sovereign Initiative of God", "text": "1 Samuel opens with Hannah's prayer (ch. 1–2) and the book is punctuated throughout by prayer as the means by which God's people participate in his purposes. Samuel is himself born as an answer to prayer; the transition of kingship happens only after Samuel intercedes; David repeatedly inquires of the LORD before military action. The book teaches that God accomplishes his purposes in response to the prayers of his people — not because prayer changes his mind, but because he has ordained to act through the intercession of his covenant people."},
      {"title": "The Establishment of Covenant Kingship", "text": "The monarchy in 1 Samuel is a deeply ambivalent development: it is both a rejection of God's direct kingship (8:7) and — paradoxically — part of God's intended plan (see Deut 17:14–20; Gen 49:10). The resolution is that Israel needed not just any king but the right king — one who would rule by God's law, acknowledge God's ultimate sovereignty, and shepherd the people rather than exploit them. Saul's failure clarifies the standard; David's anointing provides the model; and the entire Davidic line points forward to the one King who would fulfil every requirement."}
    ]
  },

  "2samuel": {
    "key_people": [
      {"name": "David", "role": "King of Israel for 40 years; the anointed one (messiah) whose mixed record of triumph and failure makes him both the greatest OT king and a pointer to the need for one greater than David"},
      {"name": "Nathan", "role": "The prophet who delivers both the Davidic covenant (ch. 7) and the devastating confrontation after David's sin (ch. 12); the model of the prophetic office speaking truth to power"},
      {"name": "Bathsheba", "role": "Uriah's wife taken by David in an abuse of royal power; her son Solomon will sit on the covenant throne, showing grace working through and despite human sin"},
      {"name": "Absalom", "role": "David's son who leads a rebellion against his father; his death and David's grief (ch. 18) are among the most humanly poignant scenes in Scripture"},
      {"name": "Mephibosheth", "role": "Jonathan's crippled son whom David restores to the king's table out of covenant loyalty — one of the most beautiful pictures of grace in the OT"}
    ],
    "context": "2 Samuel covers David's 40-year reign (c. 1010–970 BC) and represents the height of Israel's united monarchy. The capture of Jerusalem, the return of the ark, the Davidic covenant, and the expansion of Israel's territory all occur in this book. But the book is structured in two halves: the rise and glory of David's kingdom (chs. 1–10) and the fall that begins with Bathsheba and never fully recovers (chs. 11–24).",
    "christ_connection": "The Davidic covenant (2 Sam 7:12–16) is the pivotal messianic promise of the entire OT: God promises David an eternal house, throne, and kingdom through his offspring. Every subsequent messianic prophecy is essentially a commentary on this promise, and the NT opens by identifying Jesus as 'the son of David' (Matt 1:1) to declare its fulfilment. Peter's Pentecost sermon (Acts 2:30–31) explicitly cites 2 Samuel 7 as the basis for the resurrection — the eternal throne promised to David's son is occupied by the risen Jesus at the right hand of the Father.",
    "key_verses": [
      {"ref": "2 Samuel 7:12-16", "note": "The Davidic covenant: God promises an eternal house, throne, and kingdom through David's offspring — the most important messianic promise in the OT"},
      {"ref": "2 Samuel 12:7", "note": "Nathan's confrontation: 'You are the man' — the moment when the king who judged another's sin is made to see his own; the model of prophetic accountability"},
      {"ref": "2 Samuel 22:2-3", "note": "David's great hymn of thanksgiving: 'The LORD is my rock and my fortress and my deliverer' — his theological reflection on a lifetime of God's faithfulness"}
    ],
    "themes_detail": [
      {"title": "The Davidic Covenant: The Messianic Promise", "text": "Chapter 7 is the theological center of 2 Samuel and arguably of the entire OT. David wants to build a house for God; God instead promises to build a house (dynasty) for David. The threefold promise — house, throne, and kingdom established forever — is the specific promise that all subsequent messianic expectation hangs on. NT writers quote 2 Samuel 7 more than almost any other OT passage, because here God makes explicit what has been implied since Genesis 3:15: the coming deliverer will be a king from the line of David."},
      {"title": "Sin and Its Cascading Consequences", "text": "The second half of 2 Samuel is a sustained meditation on how one act of royal sin — David's adultery with Bathsheba and the murder of Uriah — produces wave after wave of consequences: the death of the child, Amnon's rape of Tamar, Absalom's rebellion, and David's flight from Jerusalem. The book does not moralize about this but shows it unflinchingly. Nathan's prophecy that 'the sword shall never depart from your house' (12:10) is fulfilled in detail, demonstrating that the law of sowing and reaping operates even within the sphere of grace."},
      {"title": "Grace and Restoration After Failure", "text": "Despite the magnitude of David's sin, 2 Samuel also records his genuine repentance (Psalm 51 is the companion text) and God's continued loyalty to the covenant. Mephibosheth's restoration (ch. 9) — a crippled enemy brought to the king's table purely on the basis of covenant loyalty to his father — is an acted parable of grace. David is never presented as perfect, but as a man who, when confronted, does not harden his heart but genuinely turns. This pattern of sin, confrontation, repentance, and restoration is foundational to the theology of forgiveness."},
      {"title": "God's Faithfulness to His Anointed Despite His Failures", "text": "2 Samuel raises the uncomfortable question: if David — the man after God's own heart — can commit adultery and murder, what hope is there for any king or any covenant member? The book's answer is not to excuse David but to point beyond him: the covenant is not based on David's merit but on God's oath. The Davidic promises do not collapse with David's sins; they await a son of David who will keep all that David failed to keep. This is why the OT ends still waiting, and why the NT opens with 'the son of David' who does what David could not."}
    ]
  }
}

written, skipped = [], []
for book_id, extras in ENRICHMENTS.items():
    path = os.path.join(OUT, book_id + '.json')
    if not os.path.exists(path):
        print(f"MISSING: {path}")
        continue
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    data.update(extras)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    written.append(book_id)
    print(f"  enriched: {book_id}")

print(f"\nDone — {len(written)} books updated: {', '.join(written)}")
