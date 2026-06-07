"""
Book Study Data — Leviticus
book_id: leviticus
lang: hebrew

Run: python3 scripts/build-book-study-leviticus.py

Notes:
- Author group: Moses (peak in author-freq-hebrew.json)
- 12 vocab entries; Hebrew translit fields blank in glossary — supplied manually
- Covers all five sacrifice types: olah, hattat, asham, shelamin, minhah
- H5799 Azazel: Moses-rate=0.00 in freq data (only 4 occurrences in Lev 16)
  but theologically central to the Day of Atonement — included
- H2403 hattat gloss 'punishment of sin' expanded to 'sin/purification offering'
  to reflect Milgrom's scholarship on dual function (sin removal + sanctuary purification)
- H2930 is the verb (to be/make unclean); H2931 is the adjective (unclean) — using verb
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
    "bookId": "leviticus",

    "key_vocabulary": [
        {
            "code": "H7133",
            "lemma": "קׇרְבָּן",
            "translit": "qorbān",
            "gloss": "offering",
            "significance": "קׇרְבָּן (qorban, &lsquo;that which is brought near, an offering&rsquo;) derives from the verb קָרַב (qarav, &lsquo;to draw near, approach&rsquo;). An offering is not primarily a gift or a payment but an act of approach: the worshipper brings an animal or grain &lsquo;near&rsquo; to God as the mechanism of proximity with the holy. Leviticus opens at 1:2 with &lsquo;when anyone of you brings (יַקְרִיב) an offering (קׇרְבָּן) to YHWH&rsquo; — the verb and noun share the same root, encoding the logic of the whole sacrificial system in the opening sentence: drawing near is what offerings are for. The word is preserved intact in the NT in Jesus&rsquo;s critique of the &lsquo;Corban&rsquo; practice (Κορβᾶν, Mark 7:11): property declared qorban was exempt from being used for parents&rsquo; needs, turning the approach-mechanism into a legal shield against family obligation. The Aramaic form traveled through the centuries unchanged because the concept of sacred approach was too central to abandon."
        },
        {
            "code": "H5930",
            "lemma": "עֹלָה",
            "translit": "ʿōlāh",
            "gloss": "burnt offering",
            "significance": "עֹלָה (olah, &lsquo;burnt offering&rsquo;) literally means &lsquo;that which ascends&rsquo; — the root עָלָה (alah) means &lsquo;to go up.&rsquo; The burnt offering is wholly consumed on the altar; nothing is returned to the worshipper. Unlike the peace offering (shared among God, priests, and worshippers) or the sin offering (portions eaten by priests), the olah gives everything back to God in smoke. This total consumption makes it the sacrifice of total dedication — the full surrender of what the worshipper has brought. Leviticus opens with the olah (chs. 1-2) because it is the foundational act of approach: before fellowship (shelamin) or forgiveness (hattat), there is surrender. The olah was also the tamid — the &lsquo;perpetual offering&rsquo; of a lamb at dawn and dusk every day in the tabernacle, sustaining God&rsquo;s presence in the community without interruption. Paul&rsquo;s appeal to &lsquo;present your bodies as a living sacrifice, holy and acceptable to God&rsquo; (Rom 12:1) explicitly echoes the olah&rsquo;s logic: the Christian&rsquo;s entire life is a perpetual, wholly surrendered burnt offering."
        },
        {
            "code": "H2403",
            "lemma": "חַטָּאָה",
            "translit": "ḥaṭṭāʾāh",
            "gloss": "sin offering",
            "significance": "חַטָּאָה (hattat, &lsquo;sin offering&rsquo; or more precisely &lsquo;purification offering&rsquo;) comes from the same root as &lsquo;sin&rsquo; (חֵטְא, heta, &lsquo;to miss the mark&rsquo;) but functions in Leviticus as both a moral and a ritual purifier. Modern scholars (notably Jacob Milgrom) have established that the hattat&rsquo;s primary function is purification of the sanctuary — the blood is not primarily applied to the sinner but to the altar, the incense altar, or the inner veil, depending on severity: common person (outer altar, 4:25, 30), priest or congregation (inner sanctuary, 4:6-7, 16-18), on the Day of Atonement (the ark&rsquo;s cover, 16:15-16). The logic: Israel&rsquo;s sins and impurities contaminate the sanctuary; if the contamination is not removed, God&rsquo;s presence cannot remain. The hattat cleanses the divine dwelling by application of the purifying blood. Isaiah 53:10 uses the cognate asham (guilt offering) for the Servant&rsquo;s death, but Hebrews 13:11-12 explicitly reads Christ&rsquo;s death outside the camp as fulfilling the hattat: &lsquo;the bodies of those animals whose blood is brought into the holy places by the high priest as a sacrifice for sin are burned outside the camp. So Jesus also suffered outside the gate.&rsquo;"
        },
        {
            "code": "H817",
            "lemma": "אָשָׁם",
            "translit": "ʾāšām",
            "gloss": "guilt offering",
            "significance": "אָשָׁם (asham, &lsquo;guilt offering, reparation offering&rsquo;) addresses a specific offense category: the misappropriation of what belongs to YHWH — sacred things used without authorization, false oaths using the divine name, and unintentional violations of consecrated property. Crucially, the asham requires not only an animal sacrifice but monetary restitution: the wrongdoer must repay the principal plus twenty percent to the party wronged (Lev 6:4-5). The asham thus has two components: the relational repair of reparation and the sacrificial repair of atonement. Isaiah 53:10 uses asham as the interpretive lens for the Servant&rsquo;s death: &lsquo;when his soul makes an offering for guilt (אָשָׁם), he shall see his offspring.&rsquo; The Servant&rsquo;s death is a reparation offering — a payment that restores not merely forgiveness but the full restitution of what sin has taken from God. The NT echoes this when Paul writes that Christ &lsquo;redeems us from the curse of the law&rsquo; (Gal 3:13) — not merely pardoning the debt but paying it in full."
        },
        {
            "code": "H8002",
            "lemma": "שֶׁלֶם",
            "translit": "šelem",
            "gloss": "peace offering",
            "significance": "שֶׁלֶם (shelem, usually plural שְׁלָמִים, shelamin — &lsquo;peace offerings, fellowship offerings&rsquo;) derives from the root שָׁלֵם (shalem, &lsquo;to be complete, whole, at peace&rsquo;). The shelamin are the most relational of the five offerings: the fat portions are burned on the altar (for God), a portion goes to the officiating priests, and the remainder is eaten by the worshipper and household in the presence of God — a communal meal of restored shalom. This structure makes the shelamin the covenant meal: the Sinai covenant is ratified with shelamin (Exod 24:5); the dedication of the Jerusalem temple includes shelamin on a massive scale (1 Kgs 8:63-64). The fellowship meal in God&rsquo;s presence is the goal of the entire sacrificial system — the hattat removes the barrier (sin), the olah surrenders all to God, and the shelamin celebrates the restored relationship in a shared table. The Lord&rsquo;s Supper echoes the shelamin&rsquo;s logic: Christ is the sacrifice, the minister distributes, the congregation eats together in God&rsquo;s presence — the meal of peace in the new covenant."
        },
        {
            "code": "H4503",
            "lemma": "מִנְחָה",
            "translit": "minḥāh",
            "gloss": "grain offering",
            "significance": "מִנְחָה (minhah, &lsquo;grain offering, tribute, gift&rsquo;) is the only bloodless offering in the Levitical system, consisting of fine flour with oil and salt (and sometimes frankincense), sometimes baked or fried. The word&rsquo;s background is tributary — in Genesis, Jacob sends minhah as a diplomatic gift to Esau (32:13-21) and Joseph&rsquo;s brothers bring minhah to the Egyptian ruler (43:11-25). The same word describes the offering of flour and oil to YHWH, framing it as tribute presented to the great King. The required salt in every minhah (2:13) carries a specific covenant meaning: &lsquo;you shall not omit the salt of the covenant of your God from your grain offering&rsquo; — salt preserved food and symbolized covenant permanence; the minhah is a covenant meal. Leaven and honey are excluded (2:11) because both cause fermentation and instability, the opposite of the covenant&rsquo;s durability. The minhah almost always accompanies animal sacrifices, completing the picture of a full meal: flesh and grain, blood and bread, together constituting a comprehensive presentation to God."
        },
        {
            "code": "H2889",
            "lemma": "טָהוֹר",
            "translit": "ṭāhôr",
            "gloss": "clean",
            "significance": "טָהוֹר (tahor, &lsquo;clean, pure, fit for approaching God&rsquo;) is the positive pole of Leviticus&rsquo;s central classification system. Being tahor is not primarily a hygiene category but a status — the condition of being ritually and relationally fit to approach the holy God in the sanctuary. The clean/unclean distinction in chapters 11-15 classifies animals (permitted vs. forbidden for food), bodily conditions (skin diseases, discharges, childbirth), and objects that can transmit or receive impurity. The organizing principle draws on creation order: animals that &lsquo;fit&rsquo; their domain (fish with fins and scales in water; birds that fly without swarming) are tahor; animals that blur categorical boundaries are not. The distinction is not arbitrary but teaches that the ordered creation has structure, and approach to the Creator requires living within that structure intentionally. &lsquo;Clean&rsquo; is the state of one who has gone through the required purification — washing, waiting period, and sometimes sacrifice — to be restored to worship eligibility after becoming tamé."
        },
        {
            "code": "H2930",
            "lemma": "טָמֵא",
            "translit": "ṭāmēʾ",
            "gloss": "be unclean",
            "significance": "טָמֵא (tame, &lsquo;to be or become impure, be/make defiled, be unfit for worship&rsquo;) is the negative pole of Leviticus&rsquo;s purity system and appears more frequently here than in any other biblical book. The key insight of modern scholarship on Levitical impurity (especially Mary Douglas and Jacob Milgrom) is that tame is a status, not a moral failing — a person can become tamé through entirely non-moral events such as childbirth, contact with a corpse, or certain skin conditions. What tahor persons and objects share is fullness of life in God&rsquo;s ordered world; what tamé conditions share is proximity to death, loss, boundary-crossing, or dis-order. Crucially, impurity spreads through contact (11:24-25, 27-28, etc.) and accumulates in the sanctuary (16:16) — if not periodically removed by the sacrificial system, the contamination of Israel&rsquo;s community would drive God&rsquo;s presence from the tabernacle. Jesus&rsquo;s practice reverses the contagion logic: when he touches lepers and the dead (Mark 1:41; 5:41), they become clean rather than him becoming tamé. His touch is more powerful than defilement."
        },
        {
            "code": "H5799",
            "lemma": "עֲזָאזֵל",
            "translit": "ʿazāzēl",
            "gloss": "Azazel",
            "significance": "עֲזָאזֵל (Azazel) appears only in Leviticus 16 (vv. 8, 10, 26) and its meaning remains debated: (1) &lsquo;goat that goes away&rsquo; (the etymology behind the English &lsquo;scapegoat&rsquo;, from ez = goat + azal = go away); (2) a demon or fallen angel inhabiting the wilderness (so the Talmud and 1 Enoch); (3) a topographical name for the rugged cliff from which the goat was later cast in rabbinic practice. Whatever the etymology, the ritual logic is clear: on the Day of Atonement, Aaron lays both hands on the live goat and confesses &lsquo;all the iniquities of the children of Israel, and all their transgressions, all their sins&rsquo; over it. The goat then &lsquo;carries (נָשָׂא) all their iniquities into a remote land&rsquo; (16:22), taking the sins away from the community into the wilderness — the realm outside the ordered, covenanted world. The two goats of Yom Kippur together make the complete picture: one goat is slaughtered (atonement — the blood addresses the sanctuary&rsquo;s defilement); one goat carries the sins away (removal — the guilt is transferred and expelled). Christ embodies both: his blood atones and his completed work removes sin &lsquo;as far as the east is from the west&rsquo; (Ps 103:12)."
        },
        {
            "code": "H3104",
            "lemma": "יוֹבֵל",
            "translit": "yôbēl",
            "gloss": "jubilee",
            "significance": "יוֹבֵל (yobel, also the word for &lsquo;ram&rsquo;s horn / trumpet blast&rsquo;) names the fiftieth year — the super-sabbath declared after seven cycles of seven sabbath years (Lev 25:8-55). In the jubilee year: all Israelite slaves go free and return to their families; all sold land returns to the original family that received it in the original allotment; and debt-slavery relationships are dissolved. The theological foundation is explicit: &lsquo;the land shall not be sold in perpetuity, for the land is mine. For you are strangers and sojourners with me&rsquo; (25:23); &lsquo;for the Israelites are slaves to me — they are my servants whom I brought out of Egypt&rsquo; (25:55). Neither land nor persons are ultimately owned by human beings; they belong to YHWH, and the jubilee periodically restores that ownership. The jubilee is the covenant&rsquo;s built-in economic reset, preventing permanent concentration of land and wealth. Jesus opens his Nazareth sermon with Isaiah 61:1-2 — a text saturated with jubilee language — and declares: &lsquo;today this Scripture is fulfilled in your hearing&rsquo; (Luke 4:21), announcing himself as the one who inaugurates the ultimate jubilee of release, restoration, and freedom."
        },
        {
            "code": "H1350",
            "lemma": "גָּאַל",
            "translit": "gāʾal",
            "gloss": "redeem",
            "significance": "גָּאַל (gaal, &lsquo;to act as kinsman-redeemer, to redeem, to buy back&rsquo;) names the legal and relational responsibility of the next-of-kin (goel) to restore what a poorer family member has had to forfeit. In Leviticus 25, the gaal system is the primary mechanism for the jubilee&rsquo;s goals: if an Israelite must sell land due to poverty, the nearest relative has the right and duty to buy it back (25:25-28); if an Israelite must sell himself into slavery, a relative may redeem him at a calculated price (25:47-55). The word describes not voluntary charity but kinship obligation — the goel acts because of blood relationship, not sentiment. The concept becomes one of the OT&rsquo;s richest theological metaphors: YHWH is Israel&rsquo;s goel — their blood-relative redeemer who buys them back from Egypt (Exod 6:6; 15:13) and promises to buy them back from exile (Isa 43:1; 44:6, 24; 48:20). The book of Ruth structures the entire narrative around Boaz as goel — the kinsman-redeemer who pays the price to restore what Naomi&rsquo;s family had lost — making Boaz one of the OT&rsquo;s most developed types of Christ, the one who became our kin in the Incarnation in order to redeem us."
        },
        {
            "code": "H6942",
            "lemma": "קָדַשׁ",
            "translit": "qādaš",
            "gloss": "sanctify",
            "significance": "קָדַשׁ (qadash, &lsquo;to be holy, to sanctify, to consecrate, to set apart as belonging to God&rsquo;) is the verbal form of the holiness concept that drives the entire second half of Leviticus. The Holiness Code (chs. 17-26) hinges on 19:2: &lsquo;You shall be holy (קְדֹשִׁים תִּהְיוּ), for I YHWH your God am holy.&rsquo; The command is grounded entirely in God&rsquo;s own character — not in a social norm, a pragmatic benefit, or an arbitrary rule, but in the imitation of who God is. The verb appears in three stems that distinguish three agents: in the Piel (causative), YHWH sanctifies Israel (&lsquo;I am YHWH who sanctifies you,&rsquo; 20:8; 21:8, 15, 23; 22:9, 16, 32) — God&rsquo;s action is prior; in the Hitpael (reflexive), Israel sanctifies itself (11:44) — human response is required; in the Qal (simple), persons and things simply are holy by status. The layered grammar encodes the Holiness Code&rsquo;s logic: God acts first to consecrate Israel, and Israel is then called to live into that consecration. The NT transfers this logic to Christ: he &lsquo;became for us...sanctification&rsquo; (1 Cor 1:30), and believers are being &lsquo;sanctified&rsquo; through the one offering by which &lsquo;he has perfected for all time those who are being sanctified&rsquo; (Heb 10:14)."
        }
    ],

    "language_notes": (
        "<p>Leviticus is primarily legal-ritual discourse — almost the entire book is <em>divine speech</em> addressed to Moses (occasionally Aaron) at the tent of meeting. The recurring frame &lsquo;YHWH spoke to Moses, saying&rsquo; (וַיְדַבֵּר יְהוָה אֶל מֹשֶׁה לֵּאמֹר) appears over 30 times, making Leviticus the most explicitly divine-speech book in the Pentateuch. This is not incidental: the book claims that the entire sacrificial and purity system derives from God&rsquo;s own instructions, not from priestly invention or cultural borrowing. The legal-speech genre also explains the repetitions — the same regulations sometimes appear twice from different angles (instructions for the priest first, then for the lay person), reflecting the structured pedagogy of oral legal tradition.</p>"
        "<p>The five Hebrew names for the five main offerings encode the theological logic of each. <strong>עֹלָה</strong> (olah, &lsquo;that which goes up&rsquo;) — wholly consumed, ascending to God. <strong>מִנְחָה</strong> (minhah, &lsquo;tribute/gift&rsquo;) — the bloodless tribute of grain and oil. <strong>שְׁלָמִים</strong> (shelamin, &lsquo;what is at peace/whole&rsquo;) — the communal fellowship meal. <strong>חַטָּאָה</strong> (hattat, &lsquo;sin offering / purification offering&rsquo;) — the blood-based purification of sanctuary and person. <strong>אָשָׁם</strong> (asham, &lsquo;guilt offering / reparation offering&rsquo;) — the sacrifice that accompanies financial restitution for misappropriation. Each name is a compressed theology; reading them is the first step to understanding the system&rsquo;s logic.</p>"
        "<p>The clean/unclean vocabulary in chapters 11-15 forms one of the most systematic <strong>classification taxonomies</strong> in the Hebrew Bible. The key antonym pair — <strong>טָהוֹר</strong> (tahor, clean) and <strong>טָמֵא</strong> (tamé, unclean) — governs every category: animals are tahor or tamé for eating (11:1-47); skin conditions are tahor or tamé for sanctuary approach (13-14); bodily discharges are tahor or tamé (15). The anthropologist Mary Douglas argued that the system classifies creation according to the &lsquo;integrity of categories&rsquo; — what is tahor is what &lsquo;fits&rsquo; its created domain without anomaly. Jacob Milgrom refined this: the tamé conditions cluster around death, loss of bodily integrity, and the blurring of life&rsquo;s boundaries — making the purity system a symbolic assertion that the God of life requires his people to embody life-fullness. The system is not hygiene but symbolic theology enacted in the body.</p>"
        "<p>The <strong>Day of Atonement</strong> ritual of Leviticus 16 is the most elaborate single-chapter ritual text in the entire OT and exhibits a careful chiastic structure: preparations (16:1-5) → entry and sin offerings for Aaron (16:6-10) → entry into the holy of holies (16:11-19) → the Azazel goat ritual (16:20-22) → exit and further purification (16:23-28) → the permanent institution of Yom Kippur (16:29-34). The chapter&rsquo;s central image is the high priest alone, in simple linen garments rather than his ornamented vestments, entering the most holy place once a year with blood — a single human being crossing the ultimate boundary between the holy and the defiled on behalf of the entire community. The Epistle to the Hebrews reads this as the supreme OT type of Christ&rsquo;s once-for-all entry into the heavenly sanctuary with his own blood (Heb 9:7, 12, 24-26).</p>"
        "<p>The <strong>Holiness Code</strong> (chs. 17-26) has a distinctive rhetorical style marked by the divine self-identification formula: &lsquo;<em>אֲנִי יְהוָה</em>&rsquo; (&lsquo;I am YHWH&rsquo;) — appearing approximately 48 times as the ground for every command. The formula does not mean &lsquo;obey because I said so&rsquo; but &lsquo;align yourself with who I actually am.&rsquo; The commands of the Holiness Code derive their authority from the character of God, not from social convention or pragmatic benefit. The code extends holiness from the tabernacle outward to all of life: the family (18-20), the calendar of feasts (23), economic relations (25), and the land itself (26). The theological claim is that Israel&rsquo;s entire way of life — not only worship but agriculture, sexuality, commerce, and law — is to reflect the holiness of the God who lives among them.</p>"
    ),

    "reception": (
        "<p><strong>NT and patristic:</strong> The Epistle to the Hebrews is the NT&rsquo;s systematic commentary on Leviticus, reading the sacrificial system as a shadow (σκιά) of the reality found in Christ (Heb 10:1). The high priest&rsquo;s annual entry into the holy of holies points to Christ&rsquo;s once-for-all entry into the heavenly sanctuary (Heb 9:12, 24-26); the blood of bulls and goats that &lsquo;cannot take away sins&rsquo; (Heb 10:4) points to the blood of Christ that perfects those who draw near (Heb 10:14). Early Christian interpreters read every detail of the Levitical system as prefiguring Christ: Origen&rsquo;s <em>Homilies on Leviticus</em> provided the most extensive allegorical reading, treating the five types of offerings as aspects of Christ&rsquo;s one sacrifice. The patristic consensus was that the ceremonial laws of Leviticus were &lsquo;typological&rsquo; — literally historical, but designed to point forward to their fulfillment in Christ — and therefore obsolete as practices while permanently instructive as theology.</p>"
        "<p><strong>Reformation:</strong> The reformers inherited the medieval distinction between the ceremonial law (fulfilled in Christ and therefore no longer binding), the civil law (applicable to Israel as a theocratic nation but not directly to the church), and the moral law (permanently binding, summarized in the Ten Commandments and the love command). Luther and Calvin both applied this framework to Leviticus: the sacrificial system and purity codes are ceremonial — fulfilled in Christ — while the Holiness Code&rsquo;s ethical commands (&lsquo;love your neighbor as yourself,&rsquo; 19:18, quoted by Jesus and Paul) retain their force as moral law. This framework was useful but sometimes too schematic: recent scholarship has questioned whether the categories map cleanly onto Leviticus&rsquo;s own logic.</p>"
        "<p><strong>Modern scholarship:</strong> Three developments have reshaped Leviticus interpretation. First, <em>the Milgrom school</em> (Jacob Milgrom&rsquo;s three-volume Anchor Bible Leviticus commentary, 1991-2001) established the &lsquo;purification offering&rsquo; as a better translation than &lsquo;sin offering&rsquo; for hattat, clarifying the sanctuary-purification logic of the entire sacrificial system. Second, <em>Mary Douglas&rsquo;s Purity and Danger</em> (1966) transformed the reading of the clean/unclean system from irrational taboo to coherent symbolic theology organized around category integrity — changing how both scholars and pastors read chapters 11-15. Third, <em>liberation theology&rsquo;s reading of the jubilee</em> (Lev 25) has brought renewed attention to the economic and social justice dimensions of Leviticus, arguing that the debt-release and land-restoration provisions are not merely ceremonial curiosities but permanent moral principles about wealth distribution and human dignity.</p>"
    ),

    "reading_guide": (
        "<p>Read Leviticus as the answer to the question Exodus ends with: the glory fills the tabernacle and Moses cannot enter (Exod 40:35). How do sinful people live with a holy God present among them? Every regulation — the offerings, the purity rules, the Holiness Code — exists to answer that question. Without it, Leviticus feels like an arbitrary list; with it, every rule becomes an act of mercy. God is not imposing bureaucracy: he is teaching his people how to approach him without being destroyed.</p>"
        "<p>Read <strong>Leviticus 16 alongside Hebrews 9-10</strong>. The Day of Atonement is the book&rsquo;s theological climax. The high priest once a year, in linen, alone, with blood, through the veil, to the ark — Hebrews unpacks each element: &lsquo;once a year&rsquo; (limited, imperfect) vs. &lsquo;once for all&rsquo; (definitive, complete); animal blood vs. his own blood; earthly sanctuary vs. heavenly. The typological reading is not imposed on Leviticus — it is what Leviticus was structured to generate. The goal is the throne of grace &lsquo;accessible always to all&rsquo; (Heb 4:16; 10:19-22) — the answer to Moses standing outside the tent.</p>"
        "<p>The Holiness Code (chs. 17-26) is not a morality checklist but a vision of life shaped by God&rsquo;s character in every domain. Chapter 19 is its heart: care for the poor (19:9-10), love of neighbor (19:18), honest commerce (19:35-36), and justice for foreigners (19:33-34) — all grounded in &lsquo;I am YHWH.&rsquo; The ethical and ritual commands spring from the same root. Common misreading to avoid: treating the purity system as arbitrary hygiene. The tahor/tamé distinction is symbolic theology — it teaches that ordered approach to the God of life requires the whole person&rsquo;s intentional preparation.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('leviticus')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('leviticus', merged)

main()
