"""
Book Study Data — Deuteronomy
book_id: deuteronomy
lang: hebrew

Run: python3 scripts/build-book-study-deuteronomy.py

Notes:
- Author group: Moses (peak in author-freq-hebrew.json)
- 12 vocab entries; Hebrew translit fields blank in glossary — supplied manually
- Focus on Deuteronomy's distinctive vocabulary vs. Genesis-Numbers:
  the love command (ahav), hear/obey (shama), legal triple (mitzvah/mishpat/choq),
  memory (zakar), land (eretz), prophet-like-Moses (navi), herem, fear (yare),
  inheritance (nachalah)
- H8085 shama: peak=Major (Major Prophets highest density) but rate=4.17 in Moses;
  the Shema is so definitively Deuteronomic it must be included
- H157 ahav: peak=Wisdom, Moses-rate=0.69; included because the love command
  is unique to Deuteronomy in the Pentateuch's legal register
- H2763 charam: peak=Historical, Moses-rate=0.24; included because herem warfare
  is institutionally defined in Deuteronomy 7 and is theologically central
"""

import json, os, sys

# ── boilerplate ──────────────────────────────────────────────────────────────

def load_book_study(book_id):
    path = f'data/workshop/book-study/{book_id}.json'
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

def save_book_study(book_id, data):
    os.makedirs('data/workshop/book-study', exist_ok=True)
    path = f'data/workshop/book-study/{book_id}.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'wrote {path} ({len(data.get("key_vocabulary", []))} vocab entries)')

def merge_book_study(existing, new_data):
    """Fill only fields not already present. Safe to re-run."""
    result = dict(existing)
    for key, val in new_data.items():
        if key not in result or not result[key]:
            result[key] = val
    return result

# ── content ──────────────────────────────────────────────────────────────────

BOOK_STUDY = {
    "bookId": "deuteronomy",

    "key_vocabulary": [
        {
            "code": "H8085",
            "lemma": "שָׁמַע",
            "translit": "šāmaʿ",
            "gloss": "hear",
            "significance": "שָׁמַע (shama, &lsquo;to hear, listen, obey&rsquo;) is the word that opens the Shema: <em>שְׁמַע יִשְׂרָאֵל</em> — &lsquo;Hear, O Israel&rsquo; (6:4). The book of Deuteronomy takes its identity from this imperative. In Hebrew, &lsquo;hearing&rsquo; and &lsquo;obeying&rsquo; are the same verb — shama encompasses both the reception of a word and the responsive action it demands. There is no gap between hearing and obeying as there is in English; to genuinely hear is to begin to comply. Deuteronomy&rsquo;s rhetoric is structured around repeated &lsquo;Hear&rsquo; imperatives: &lsquo;Hear, O Israel!&rsquo; (5:1; 6:3, 4; 9:1; 20:3), each introducing a fresh appeal from Moses to a generation on the edge of the land. The Shema itself is not merely a creed about God&rsquo;s unity — it is a loyalty oath: Israel declares YHWH alone as sovereign, which requires total orientation of love and will toward him. Paul draws the line directly: &lsquo;faith comes from hearing (ἀκοή — the LXX translation of shama)&rsquo; (Rom 10:17). The epistemology of both testaments is auditory — the word is spoken, the ear receives it, trust responds."
        },
        {
            "code": "H157",
            "lemma": "אָהַב",
            "translit": "ʾāhab",
            "gloss": "love",
            "significance": "אָהַב (ahav, &lsquo;to love&rsquo;) appears in its most theologically weighted form in Deuteronomy 6:5 — the verse Jesus would call the &lsquo;greatest commandment&rsquo;: &lsquo;You shall love (וְאָהַבְתָּ) YHWH your God with all your heart and with all your soul and with all your strength.&rsquo; Deuteronomy is unique in the Pentateuch in making love the <em>legal</em> foundation of the covenant — not a sentiment that accompanies law but the root from which the entire covenantal structure grows. In Hebrew, ahav covers relational loyalty, volitional commitment, and covenant faithfulness — it is not primarily an emotion but a disposition of the whole self. Deuteronomy also commands love for the neighbor (implicit in chs. 15 and 22) and explicitly for the stranger: &lsquo;Love the stranger (אֶת הַגֵּר), for you were strangers in Egypt&rsquo; (10:19). Jesus identifies the love of God (Deut 6:5) and love of neighbor (Lev 19:18) as the summary of all Torah (Matt 22:37-40). Paul reaches the same conclusion: &lsquo;love is the fulfillment of the law&rsquo; (Rom 13:10). The Greek ἀγαπάω that the NT uses for commanded love is the LXX&rsquo;s regular translation of ahav."
        },
        {
            "code": "H3820",
            "lemma": "לֵב",
            "translit": "lēb",
            "gloss": "heart",
            "significance": "לֵב (lev, &lsquo;heart&rsquo;) in Hebrew is not primarily the seat of emotion but of volition, decision, and moral orientation — what modern usage might call the will or the inner person. The Shema&rsquo;s love command targets the lev first: &lsquo;with all your heart (לְבָבְךָ)&rsquo; (6:5). Throughout Deuteronomy, the heart is the site of covenant faithfulness or failure: &lsquo;do not harden your heart&rsquo; (15:7); &lsquo;lay up these words in your heart&rsquo; (11:18); &lsquo;lest your heart be lifted up and you forget YHWH&rsquo; (8:14). The book&rsquo;s most daring promise concerns the heart directly: &lsquo;YHWH your God will circumcise your heart and the heart of your offspring, so that you will love YHWH your God with all your heart&rsquo; (30:6). External law commands the heart; the eschatological promise is that God will transform it — the surgery that enables what the commandment requires. Jeremiah 31:33 (&lsquo;I will put my law within them, and I will write it on their hearts&rsquo;) and Ezekiel 36:26 (&lsquo;a new heart I will give you&rsquo;) both develop this Deuteronomic promise into the new covenant. Paul reads the fulfillment: &lsquo;you are a letter from Christ...written not with ink but with the Spirit of the living God, not on tablets of stone but on tablets of human hearts&rsquo; (2 Cor 3:3)."
        },
        {
            "code": "H4687",
            "lemma": "מִצְוָה",
            "translit": "miṣwāh",
            "gloss": "commandment",
            "significance": "מִצְוָה (mitzvah, &lsquo;commandment, that which is commanded&rsquo;) is Deuteronomy&rsquo;s umbrella term for YHWH&rsquo;s instruction as a whole. The book frequently uses &lsquo;the commandment&rsquo; (הַמִּצְוָה, ha-mitzvah) in the singular as a collective noun for the entire Torah covenant: &lsquo;be careful to do all the commandment that I command you today&rsquo; (8:1; cf. 15:5; 19:9; 27:1). This singular usage is theologically significant — the many laws are one mitzvah, one covenantal instruction from one God. The rabbis later enumerated 613 individual mitzvot in Torah, but Deuteronomy&rsquo;s singular ha-mitzvah resists atomizing: each law is not an isolated rule but an expression of a single integrated covenant loyalty. Deuteronomy 30:11 insists the mitzvah is not too difficult or too far away — it is near, in the mouth and in the heart, to do it. Jesus answers the lawyer&rsquo;s question &lsquo;which commandment is the greatest?&rsquo; (Matt 22:36) by citing Deuteronomy 6:5 — the greatest mitzvah summarizes and encompasses all others, just as Moses insisted the whole Torah was one covenant address to one people from one God."
        },
        {
            "code": "H4941",
            "lemma": "מִשְׁפָּט",
            "translit": "mišpāṭ",
            "gloss": "ordinance",
            "significance": "מִשְׁפָּט (mishpat, &lsquo;ordinance, judgment, justice, legal decision&rsquo;) designates the case-law component of the covenant — rulings derived from specific precedents and situations. In Deuteronomy&rsquo;s standard legal formula, &lsquo;statutes and ordinances&rsquo; (חֻקִּים וּמִשְׁפָּטִים) appears repeatedly (4:1, 5, 8, 14; 5:1; 6:1; 7:11; etc.) as the comprehensive designation of the covenant&rsquo;s legal content. But mishpat is also the broader concept of <em>justice</em> — the proper ordering of relationships in accordance with right. Deuteronomy is notable for extending mishpat beyond the cult and the community&rsquo;s internal relations: the mishpatim of chapters 15, 22-25 protect the poor, widow, orphan, and stranger from exploitation. The measure of Israel&rsquo;s covenant faithfulness is not only ritual compliance but social justice. The prophets drew precisely this connection: Amos&rsquo;s cry (&lsquo;let mishpat roll down like waters&rsquo;, Amos 5:24) and Micah&rsquo;s summary (&lsquo;to do mishpat, to love kindness, and to walk humbly with your God&rsquo;, Mic 6:8) are applications of Deuteronomy&rsquo;s legal vision to Israel&rsquo;s persistent social failures."
        },
        {
            "code": "H2706",
            "lemma": "חֹק",
            "translit": "ḥōq",
            "gloss": "statute",
            "significance": "חֹק (choq, &lsquo;statute, decree, something engraved&rsquo;) from the root חָקַק (chaqaq, &lsquo;to cut, inscribe, engrave&rsquo;) is law carved into permanence — fixed, non-negotiable divine instruction. Alongside mishpat, the choq (usually plural: chuqqim) forms Deuteronomy&rsquo;s standard formula for the covenant&rsquo;s legal content. The statutes address areas where the rationale is not immediately apparent from human experience — they require trust that the lawgiver&rsquo;s character guarantees their goodness even when the reason is not given. Deuteronomy 4:6-8 makes an astonishing apologetic claim about the chuqqim: &lsquo;What great nation has statutes and ordinances so righteous as all this Torah?&rsquo; — the statutes are themselves evidence of YHWH&rsquo;s wisdom and Israel&rsquo;s privilege as a covenant people. The surrounding nations should look at Israel&rsquo;s life under Torah and recognize a just law from a near God. The NT handles the chuqqim&rsquo;s continuing validity through the fulfillment framework: Paul says Christ &lsquo;canceled the certificate of debt&rsquo; (Col 2:14) while insisting &lsquo;the righteous requirement of the law might be fulfilled in us, who walk not according to the flesh but according to the Spirit&rsquo; (Rom 8:4)."
        },
        {
            "code": "H2142",
            "lemma": "זָכַר",
            "translit": "zākar",
            "gloss": "remember",
            "significance": "זָכַר (zakar, &lsquo;to remember, to call to mind, to recite history so it governs present action&rsquo;) is one of Deuteronomy&rsquo;s most powerful rhetorical tools. The book commands Israel to remember specific historical events as the ground for present obedience: &lsquo;Remember that you were a slave in Egypt and that YHWH your God brought you out&rsquo; (5:15; 15:15; 16:12; 24:18, 22); &lsquo;Remember the days of old, consider the years of many generations&rsquo; (32:7); &lsquo;Remember what Amalek did to you&rsquo; (25:17). Hebrew &lsquo;remembering&rsquo; (zakar) is not merely cognitive recall but liturgical re-enactment: to remember the Exodus is to make it present, to participate in it as a contemporary event. This is why the Passover Seder recites &lsquo;we were slaves in Egypt&rsquo; — not our ancestors, but we. The same logic governs the NT Eucharist: &lsquo;do this in remembrance (ἀνάμνησιν) of me&rsquo; (Luke 22:19; 1 Cor 11:24-25) — the memory is not mere mental recall but a present participation in Christ&rsquo;s death and resurrection. Deuteronomy also warns against forgetting (שָׁכַח, shakach): prosperity is the chief enemy of memory (8:11-17), and forgetting YHWH is the gateway to idolatry."
        },
        {
            "code": "H776",
            "lemma": "אֶרֶץ",
            "translit": "ʾereṣ",
            "gloss": "land",
            "significance": "אֶרֶץ (eretz, &lsquo;land, earth, ground&rsquo;) with its Moses-peak rate of 14.72 is the most prominent noun in the entire Moses corpus after generic verbs — and in Deuteronomy, &lsquo;the land&rsquo; (הָאָרֶץ, ha-aretz) means the Promised Land, the covenantal goal of everything Israel has endured since the Exodus. The phrase &lsquo;the land that YHWH your God is giving you&rsquo; appears as a relentless refrain throughout Deuteronomy (1:25; 3:18; 4:21; 6:10; 8:7; 11:31; etc.): the land is the gift, YHWH is the giver, Israel&rsquo;s faithfulness is the condition for remaining in it. The land is not merely real estate — it is the place where YHWH&rsquo;s name will dwell (12:5, 11, 21), where covenant life can be fully practiced, and where Israel&rsquo;s witness to the nations will be visible. Deuteronomy 28-29 makes the stakes explicit: covenant faithfulness brings flourishing in the land; covenant breach brings exile from it. The prophets parse Israel&rsquo;s history entirely through this Deuteronomic framework. The NT expands the eretz promise eschatologically: &lsquo;the meek shall inherit the earth/land&rsquo; (Matt 5:5 citing Ps 37:11); Jesus is given &lsquo;all the kingdoms of the world and their glory&rsquo; (Matt 4:8); the localized Deuteronomic land promise grows to cosmic scope in the new creation."
        },
        {
            "code": "H5030",
            "lemma": "נָבִיא",
            "translit": "nābîʾ",
            "gloss": "prophet",
            "significance": "נָבִיא (navi, &lsquo;prophet&rsquo;) reaches its most messianic significance in Deuteronomy 18:15-18: Moses promises a coming prophet &lsquo;like me, from among you, from your brothers&rsquo; — YHWH will raise him up, put his words in his mouth, and the prophet will speak everything YHWH commands. The criteria are precise: he will be Israelite (not foreign), YHWH-appointed (not self-claiming), and a bearer of divine words (not his own). Moses&rsquo;s promise implicitly acknowledges his own limitation — the coming prophet will be like Moses but greater, doing what Moses could not finish. Deuteronomy 34:10 assesses the entire subsequent prophetic line: &lsquo;there has not arisen a prophet since in Israel like Moses.&rsquo; The wait continues throughout the OT. The NT answers the wait from multiple directions: Peter cites Deuteronomy 18 directly for Jesus (Acts 3:22-23); Stephen cites it (Acts 7:37); the crowd wonders if Jesus is &lsquo;the Prophet&rsquo; (John 6:14; 7:40); Jesus himself speaks with the authority of YHWH&rsquo;s own voice (Matt 5:21-48: &lsquo;you have heard it said...but I say to you&rsquo;). Hebrews 1:1-2 explicitly marks the transition: the many prophets gave way to the Son."
        },
        {
            "code": "H2763",
            "lemma": "חָרַם",
            "translit": "ḥāram",
            "gloss": "devote to destruction",
            "significance": "חָרַם (charam, &lsquo;to devote to destruction, to put under the ban — the herem&rsquo;) is Deuteronomy&rsquo;s most theologically difficult institution. Chapter 7:1-6 commands Israel to put the seven Canaanite nations under complete herem — no prisoners, no treaties, no intermarriage — and the rationale is given in 7:4: &lsquo;they would turn away your sons from following me.&rsquo; The herem is a theological category, not merely a military one: an enemy city put under herem is &lsquo;devoted&rsquo; (in the sense of being dedicated) to YHWH — removed from ordinary human use and surrendered entirely to divine judgment. The same root gives the word for the &lsquo;most holy&rsquo; portion of the tabernacle furniture — holiness and destruction occupy the same semantic space. The Achan narrative (Josh 7) shows the ban being violated: one family&rsquo;s theft of devoted goods places the entire community under liability. The prophets apply herem metaphorically to Israel itself: Isaiah 43:28 speaks of YHWH &lsquo;devoting Jacob to destruction&rsquo; in the exile. NT interpreters handled the herem through typology — it represents the final divine judgment, not an ongoing ethical mandate — and through the transformation of holy war: the Christian&rsquo;s battle is &lsquo;not against flesh and blood&rsquo; (Eph 6:12)."
        },
        {
            "code": "H3372",
            "lemma": "יָרֵא",
            "translit": "yārēʾ",
            "gloss": "fear",
            "significance": "יָרֵא (yare, &lsquo;to fear, to stand in awe of, to revere&rsquo;) establishes the fundamental posture of Israel toward YHWH. The phrase &lsquo;fear YHWH your God&rsquo; is a Deuteronomic refrain: 4:10; 5:29; 6:2, 13, 24; 8:6; 10:12, 20; 13:4; 14:23; 17:19; 28:58. In Deuteronomy, yare encompasses both reverential awe before divine holiness and practical covenant loyalty: &lsquo;fear YHWH your God, serve him only&rsquo; (6:13) — the fear is not paralyzing terror but the appropriate orientation of a finite creature before an absolute moral sovereign. The word is nearly synonymous with &lsquo;obey&rsquo; in many Deuteronomic contexts. Proverbs 9:10 will declare &lsquo;the fear of YHWH is the beginning of wisdom&rsquo; — Deuteronomy is where the equation is first established. The fear of YHWH is also the community&rsquo;s best deterrent against sin: &lsquo;put away evil from your midst, so that all Israel will hear and fear&rsquo; (17:13; 19:20; 21:21). The NT does not abolish reverence but transfigures its ground: &lsquo;work out your own salvation with fear and trembling, for it is God who works in you&rsquo; (Phil 2:12-13) — the awe is now the response to grace already given, not a condition for earning it."
        },
        {
            "code": "H5159",
            "lemma": "נַחֲלָה",
            "translit": "naḥălāh",
            "gloss": "inheritance",
            "significance": "נַחֲלָה (nachalah, &lsquo;inheritance, allotment, heritage, portion&rsquo;) frames Israel&rsquo;s relationship to the Promised Land in covenantal rather than possessive terms. The land is not conquered — it is inherited: a gift from a father to children who have done nothing to earn it. Deuteronomy uses nachalah in two directions simultaneously: the land is Israel&rsquo;s nachalah from YHWH (12:12; 15:4; 19:14; 25:19), and Israel is YHWH&rsquo;s nachalah — his own treasured portion: &lsquo;YHWH&rsquo;s portion (חֵלֶק) is his people; Jacob is the lot of his inheritance (נַחֲלָה)&rsquo; (32:9). The double ownership is the book&rsquo;s relational logic: YHWH owns the land and gives it to Israel as their inheritance; YHWH owns Israel as his own inheritance from the nations. The Levites receive a deliberate exception — they have no nachalah in land: &lsquo;YHWH is their inheritance&rsquo; (18:2; 10:9). The tribe without land has God himself as their portion, making the Levites a living enacted parable of what the whole nation is called to be. The NT develops nachalah into κληρονομία (klēronomia): believers are &lsquo;heirs of God and co-heirs with Christ&rsquo; (Rom 8:17), and the eternal inheritance is secured through Christ&rsquo;s death as the mediator of a new covenant (Heb 9:15)."
        }
    ],

    "language_notes": (
        "<p>Deuteronomy is one of the most carefully composed prose texts in the Hebrew Bible, structured on the pattern of Late Bronze Age <strong>suzerainty-vassal treaties</strong> (Hittite treaties, ca. 1400-1200 BC). These treaties followed a fixed sequence: preamble identifying the great king → historical prologue surveying the king&rsquo;s benefits → stipulations requiring the vassal&rsquo;s loyalty → deposit and public reading provisions → list of divine witnesses → sanctions (blessings for compliance, curses for breach). Deuteronomy follows this structure almost exactly: chapters 1-4 (historical prologue reviewing YHWH&rsquo;s acts since Egypt) → 5-26 (the stipulations, including the Decalogue and the legal code) → 27-28 (curses and blessings) → 29-30 (covenant renewal) → 31-34 (deposit, succession, death of Moses). This formal observation matters because it means Deuteronomy is not merely a collection of laws — it is a legally structured covenant document, and reading it requires understanding treaty rhetoric.</p>"
        "<p>The book&rsquo;s most famous linguistic feature is the <strong>Shema</strong> (6:4) and its governing verb. <strong>שָׁמַע</strong> (shama) means both &lsquo;hear&rsquo; and &lsquo;obey&rsquo; in Hebrew — there is no second verb for compliance; hearing <em>is</em> the beginning of obedience. The LXX translates shama&rsquo;s object-plus-voice construction sometimes as ἀκούω (I hear) and sometimes as ὑπακούω (I obey underneath, i.e., I submit), revealing the Greek translators&rsquo; sensitivity to the semantic gap. English readers miss this: &lsquo;hear&rsquo; in Hebrew is already a covenantal act, not merely sensory reception. The Shema&rsquo;s opening word (&lsquo;Hear, O Israel!&rsquo;) is thus simultaneously a call to attention, a call to faith, and a call to action — collapsed into a single imperative verb.</p>"
        "<p>Deuteronomy deploys a <strong>triple legal formula</strong> as its standard vocabulary for covenantal instruction: <strong>מִצְוֹת</strong> (mitzvot, commandments), <strong>חֻקִּים</strong> (chuqqim, statutes), and <strong>מִשְׁפָּטִים</strong> (mishpatim, ordinances). These three terms appear together dozens of times (4:1, 5, 8, 14; 5:1, 31; 6:1; 7:11; 8:11; etc.), creating a comprehensive designation for the whole of Torah. The distinction is not merely taxonomic but functional: the mitzvah is the general command; the choq is law carved into permanence without an immediately obvious rationale; the mishpat is case-law generated by specific situations requiring judgment. Modern translations often flatten these into &lsquo;commands and statutes&rsquo; or &lsquo;regulations,&rsquo; losing the legal precision. The triple formula signals that Deuteronomy addresses every kind of law — the categorical, the enacted, and the adjudicated — as a unified covenant whole.</p>"
        "<p>One of Deuteronomy&rsquo;s most distinctive rhetorical features is the insistent use of <strong>הַיּוֹם</strong> (ha-yom, &lsquo;today&rsquo;) — appearing approximately 50 times to create urgency and contemporaneity. Moses does not say &lsquo;at Sinai YHWH commanded these things&rsquo; but &lsquo;YHWH your God commands you <em>today</em>&rsquo; (4:40; 6:6; 8:1, 11; 10:13; 11:26-28; 15:5; etc.). The ha-yom device makes the covenant address not a historical reminiscence but a present summons: every generation that reads or hears Deuteronomy stands at the plains of Moab, on the threshold, required to choose. Deuteronomy 29:14-15 makes this explicit: the covenant is made &lsquo;not only with you who are standing here with us today...but also with those who are not here with us today.&rsquo; The &lsquo;today&rsquo; of the covenant transcends the historical moment of delivery.</p>"
        "<p>Scholars have long noted Deuteronomy&rsquo;s fluctuation between <strong>second-person singular and plural</strong> address — sometimes addressing Israel as a single &lsquo;you&rsquo; (singular: אַתָּה, attah) and sometimes as a collective &lsquo;you all&rsquo; (plural: אַתֶּם, attem). Source critics used this variation as evidence for multiple literary layers, but literary readings have shown that the switch carries rhetorical force: the singular addresses Israel as one covenant person (the corporate &lsquo;you&rsquo; who is YHWH&rsquo;s covenant partner), while the plural addresses the individual members who must each personally choose. The same individual-corporate tension governs the NT: believers are addressed as one body and as individual members simultaneously. The fluctuation is not accidental but a feature of covenant address — the community is both one and many.</p>"
    ),

    "reception": (
        "<p><strong>NT and patristic:</strong> Deuteronomy is the OT book most cited in the NT — over 40 direct quotations and hundreds of allusions. Jesus quotes Deuteronomy three times in his wilderness temptation (Matt 4:4 = Deut 8:3; Matt 4:7 = Deut 6:16; Matt 4:10 = Deut 6:13), demonstrating that he is the faithful Israel where the first generation failed. The patristic period engaged Deuteronomy primarily through its typology of Christ as the prophet like Moses (18:15), its love command (6:5 + Lev 19:18 as the Torah&rsquo;s summary), and the blessings and curses of chapter 28 as explanation of Israel&rsquo;s historical fate. Origen&rsquo;s commentary read Deuteronomy&rsquo;s geographical place-names (the plains of Moab, the Jordan) as spiritual topography for the soul&rsquo;s journey into the promised rest. Chrysostom and Augustine both emphasized the love command as the fulfillment of the legal system — anticipating the Reformation&rsquo;s similar reading.</p>"
        "<p><strong>Reformation:</strong> Luther called Deuteronomy &ldquo;Moses&rsquo;s farewell sermon&rdquo; and read its love command as the clearest expression of what the law demands and what the gospel provides. For Luther, the book simultaneously indicts (you must love with all your heart) and drives to Christ (because you cannot). Calvin&rsquo;s commentary on Deuteronomy is one of his most extensive OT works — he read the covenant structure as providing the permanent framework of law and gospel, with the blessings and curses of chapters 27-28 as the scaffolding on which the prophets built their theology of exile and restoration. The Reformation&rsquo;s recovery of the literal-historical sense — reading Deuteronomy as an actual address to an actual people — opened the book&rsquo;s covenant logic in ways allegorical readings had obscured.</p>"
        "<p><strong>Modern scholarship:</strong> Martin Noth&rsquo;s 1943 hypothesis of a &lsquo;Deuteronomistic History&rsquo; (Deuteronomy through 2 Kings as a single theological narrative edited through the lens of Deuteronomy&rsquo;s covenant theology) transformed OT study for a generation — though its details remain contested, the insight that Deuteronomy provides the theological grammar for reading the Former Prophets endures. The discovery of parallels between Deuteronomy and Hittite suzerainty treaties (Mendenhall, 1954; Kitchen, Craigie) provided external confirmation of the book&rsquo;s ancient setting. Contemporary scholarship has also engaged Deuteronomy&rsquo;s social legislation (chs. 15, 22-25) as anticipating the prophets&rsquo; advocacy for the vulnerable — the book&rsquo;s &lsquo;centralizing theology&rsquo; (one place, one God, one people) is now read alongside its &lsquo;democratizing ethics&rsquo; (every Israelite responsible for every other).</p>"
    ),

    "reading_guide": (
        "<p>The single most important key to Deuteronomy is to recognize it as a <em>sermon</em>, not a law code. Moses is preaching — not dictating statutes but appealing to a generation on the edge of the land, calling them to love the God who has already loved them first. The law comes after the history (chs. 1-4 rehearse what YHWH has done before a single command is given): grace precedes obligation. Every commandment in Deuteronomy is grounded in a prior act of YHWH&rsquo;s faithfulness. &lsquo;You shall love YHWH your God&rsquo; (6:5) is not a cold legal requirement but Moses&rsquo;s pastoral appeal: the God who brought you out of Egypt deserves your whole heart in return.</p>"
        "<p>Read the book in three movements: the historical prologue (chs. 1-4) that establishes <em>why</em> Israel owes YHWH everything; the legal core (chs. 5-26) anchored by the Shema (6:4-9) and radiating outward into every domain of life; and the covenant climax (chs. 27-30) with the staggering blessings, the devastating curses, and then the astonishing promise of 30:6 (&lsquo;YHWH your God will circumcise your heart&rsquo;) — the book ends not with threats but with a promise of inner transformation that Israel alone cannot achieve. Deuteronomy 30:11-14 insists the word is &lsquo;not too hard for you&rsquo;; Paul quotes precisely this passage (Rom 10:6-8) as describing the word of faith in Christ.</p>"
        "<p>Common misreadings: treating Deuteronomy as a second, softer Leviticus (it is structurally different — a sermon, not a priestly manual) and reading the curses of chapter 28 as a prosperity formula (they describe what covenant breach brings historically on a <em>nation</em>, not a rule for individual outcomes). Where to start if reading selectively: 6:1-25 (the Shema and its context), 8:1-20 (prosperity and forgetting), 18:15-22 (the prophet like Moses), 30:1-20 (the promise of return and the circumcised heart).</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('deuteronomy')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('deuteronomy', merged)

main()
