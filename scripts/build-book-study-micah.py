"""
Book Study Data — Micah
book_id: micah
lang: hebrew

Run: python3 scripts/build-book-study-micah.py

Notes:
- Author group: Minor — peaks are generic function words; vocabulary selected
  from Micah's specific prophetic and economic justice vocabulary
- Key codes already used: H4941 mishpat (justice), H2617 hesed, H6588 pesha,
  H7462 raah (shepherd), H6666 tsedaqah, H5375 nasa, H7453 rea, H6726 tsiyon
- H6800 tsanaʿ (walk humbly) appears only in Micah 6:8 and Prov 11:2 —
  the most Micah-specific word in the OT
- H3976 mozen (scales) + H374 ephah (measure) are the paired instruments
  of economic fraud in Micah 6:10-11
- H2790 charash (plow) in 3:12 is the verse Jeremiah 26:18 quotes verbatim
- H4310 mi (who?) in 7:18 mirrors the prophet's own name: Micah = 'who is like YHWH?'
- Hebrew translit fields blank in glossary; supplied manually
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
    "bookId": "micah",

    "key_vocabulary": [
        {
            "code": "H6800",
            "lemma": "צָנַע",
            "translit": "ṣānaʿ",
            "gloss": "walk humbly",
            "significance": "צָנַע (ṣānaʿ, &lsquo;to be modest, to walk humbly — to move with restraint and lowliness&rsquo;) appears in two places in the entire Hebrew Bible: Micah 6:8 and Proverbs 11:2 (&ldquo;with the humble (ṣĕnûʿîm) is wisdom&rdquo;). This near-uniqueness is itself significant: the word is shaped for the Micah 6:8 context. The full phrase is ṣĕnēaʿ lɛḵɛṯ ʿim-ʾĔlōhɛykā — &ldquo;to walk humbly with your God&rdquo; — and the ṣānaʿ describes not a single act but a sustained gait, a posture maintained across an entire life in covenant relationship. The false prophets of Micah 3:5-11 are the anti-ṣānaʿ: they assert themselves against YHWH&rsquo;s word, calibrate their prophecy to what their patrons want to hear, and rest in the self-serving conviction that YHWH is on their side regardless of what they do. Micah&rsquo;s contrast in 3:8 — &ldquo;I am filled with power, with the Spirit of the LORD&rdquo; — is not arrogance but the opposite: the prophet who has received divine commission and speaks from it, regardless of personal cost. The ṣānaʿ is not self-abasement but right-sizing: the recognition that the covenant partner is God and that the appropriate human posture before the Creator is lowliness. The NT&rsquo;s &ldquo;humble yourselves before the Lord, and he will exalt you&rdquo; (James 4:10) and Jesus&rsquo;s &ldquo;learn from me, for I am gentle and lowly in heart&rdquo; (Matt 11:29) enact the ṣānaʿ-posture — and his insistence in Matthew 23:12 that &ldquo;whoever exalts himself will be humbled, and whoever humbles himself will be exalted&rdquo; is the theological logic of Micah 6:8 applied to the leaders of Israel who failed it."
        },
        {
            "code": "H1497",
            "lemma": "גָּזַל",
            "translit": "gāzal",
            "gloss": "seize",
            "significance": "גָּזַל (gāzal, &lsquo;to pluck off, strip, rob — to take by force&rsquo;) is the verb of Micah&rsquo;s first specific indictment: Micah 2:2: &ldquo;They covet fields and seize (gāzĕlû) them, and houses, and take them away; they oppress a man and his house, a man and his inheritance (naḥălāh).&rdquo; The gāzal is premeditated: 2:1 describes the same people who &ldquo;devise wickedness and work evil on their beds&rdquo; and &ldquo;when the morning dawns, perform it, because it is in the power of their hand.&rdquo; The lie-awake-and-plan-it, then rise-and-execute pattern makes the gāzal a calculated economic crime rather than opportunistic theft. The objects of the seizure are sadeh (fields) and batim (houses) — specifically the agricultural inheritance that the covenant land-tenure system meant to keep within each family permanently (cf. the Jubilee legislation of Lev 25, and Naboth&rsquo;s refusal to sell his vineyard in 1 Kgs 21). The Torah already prohibits gāzal explicitly: Leviticus 19:13 &ldquo;you shall not oppress your neighbor or rob (tigzōl) him.&rdquo; What Micah witnesses is the systemic application of the very practice the Torah forbids: the powerful using legal mechanisms (debt, foreclosure, judicial corruption) to accomplish what is in principle gāzal. The NT&rsquo;s James 5:1-6 &mdash; &ldquo;the wages of the laborers who mowed your fields, which you kept back by fraud, are crying out against you&rdquo; — is the apostolic form of Micah&rsquo;s gāzal-indictment."
        },
        {
            "code": "H2790",
            "lemma": "חָרַשׁ",
            "translit": "ḥāraš",
            "gloss": "plow",
            "significance": "חָרַשׁ (ḥāraš, &lsquo;to scratch, engrave, plow; hence to fabricate or devise&rsquo;) is the verb of Micah&rsquo;s most famous judgment oracle: Micah 3:12: &ldquo;Therefore because of you Zion shall be plowed (tēḥārēš) as a field; Jerusalem shall become a heap of ruins, and the mountain of the house a wooded height.&rdquo; This is not merely &ldquo;the city will be damaged&rdquo; — it is the temple mount itself turned into agricultural land, the sacred geography reversed. The ḥāraš-word has a secondary meaning (to engrave/carve), suggesting the furrows cut deep into Zion&rsquo;s hill, and a third meaning (to be silent/still), suggesting the desolation that follows. The verse&rsquo;s importance extends beyond Micah: it is quoted verbatim in Jeremiah 26:18, where the elders use it as a legal precedent to protect Jeremiah from execution. The argument is: &ldquo;Micah of Moresheth said this in Hezekiah&rsquo;s day, and Hezekiah repented, and YHWH relented — so you cannot kill Jeremiah for saying the same thing.&rdquo; This makes Micah 3:12 one of the most consequential individual verses in the OT: it not only announced judgment on Jerusalem but later saved a prophet&rsquo;s life. The ḥāraš-imagery also reverses the Isaiah 2:4/Micah 4:3 &ldquo;beat swords into plowshares&rdquo; vision: in that oracle, weapons become agricultural tools (the sign of peace); in 3:12, the sacred site becomes farmland (the sign of judgment). The same agricultural transformation serves opposite theological ends depending on which direction history is moving."
        },
        {
            "code": "H2022",
            "lemma": "הַר",
            "translit": "har",
            "gloss": "mountain",
            "significance": "הַר (har, &lsquo;a mountain or range of hills; sometimes figurative of majesty, permanence, or divine presence&rsquo;) is Micah&rsquo;s spatial theology made visible. The book&rsquo;s har-references span the full arc of its judgment-and-hope structure. Micah 1:3-4: &ldquo;the LORD is coming out of his place and will come down and tread upon the high places (bāmôt) of the earth. And the mountains (hārîm) will melt under him.&rdquo; Micah 3:12: &ldquo;the mountain of the house (har-habbayiṯ) a wooded height&rdquo; — the temple mount plowed under. Micah 4:1: &ldquo;the mountain of the house of the LORD shall be established as the highest of the mountains (rōʾš hɛhārîm) and it shall be lifted up above the hills.&rdquo; Micah 6:1: &ldquo;Hear what the LORD says: Arise, plead your case before the mountains (hārîm), and let the hills hear your voice.&rdquo; The har moves through Micah as: the place where YHWH melts false worship (1:3-4), the sacred site corrupted by unjust leadership and thus condemned (3:12), the eschatological destination of all nations after purification (4:1), and the witness-stand in the covenant lawsuit (6:1). The same physical mountain — Zion, the temple mount — appears under divine judgment and divine exaltation in the same book, pages apart. The eschatological har of Micah 4:1-3 appears in nearly identical form in Isaiah 2:2-4, suggesting a shared prophetic tradition about Zion as the universal center of YHWH&rsquo;s kingdom."
        },
        {
            "code": "H1035",
            "lemma": "בֵּית לֶחֶם",
            "translit": "bêṯ-lɛḥɛm",
            "gloss": "Bethlehem",
            "significance": "בֵּית לֶחֶם (bêṯ-lɛḥɛm, &lsquo;house of bread — a town in Judah&rsquo;) appears in Micah 5:2 in one of the OT&rsquo;s most precise messianic oracles: &ldquo;But you, O Bethlehem Ephrathah, who are too little (ṣāʿîr) to be among the clans of Judah, from you shall come forth for me one who is to be ruler in Israel, whose coming forth (mōṣāʾōṯāyw) is from of old (miqqɛḏɛm), from ancient days (mîmê ʿôlām).&rdquo; The oracle&rsquo;s logic is the Davidic pattern of reversal: just as the original David came from the smallest clan and was the youngest son, passed over until Samuel demanded all the sons be brought (1 Sam 16), the ultimate Davidic ruler comes from the town too small to count among the Judean clans. Bethlehem was David&rsquo;s city (1 Sam 17:12) — &ldquo;the city of David&rdquo; — which gave it a royal resonance that made its smallness paradoxical: the most royal city is the most inconspicuous. The phrase &ldquo;whose coming forth is from of old, from ancient days&rdquo; implies an origin that antedates Bethlehem — the ruler whose mōṣāʾôṯ (goings forth, origins) stretch back to eternity. Matthew 2:6 cites this verse as fulfilled in Jesus&rsquo; birth at Bethlehem, and it is this passage that Herod&rsquo;s advisors identify when he asks where the Christ is to be born. The contrast between the city&rsquo;s smallness (ṣāʿîr) and the ruler&rsquo;s cosmic origin is preserved in the NT incarnation theology: &ldquo;though he was rich, yet for your sake he became poor&rdquo; (2 Cor 8:9)."
        },
        {
            "code": "H8267",
            "lemma": "שֶׁקֶר",
            "translit": "šɛqɛr",
            "gloss": "falsehood",
            "significance": "שֶׁקֶר (šɛqɛr, &lsquo;an untruth, deception, a sham — often used adverbially of actions performed deceitfully&rsquo;) appears across both the prophetic and economic dimensions of Micah&rsquo;s indictment. Micah 2:11: &ldquo;If a man should go about and utter wind and lies (bašqɛr), saying, &lsquo;I will preach to you of wine and strong drink,&rsquo; he would be the preacher for this people!&rdquo; This is Micah&rsquo;s bitter sarcasm: the population prefers prophets who prophesy abundance, and a man who promises wine and strong drink will have a following, while the prophet who announces judgment is told to stop prophesying (2:6). Micah 6:12: &ldquo;your rich men are full of violence; your inhabitants speak lies (šɛqɛr), and their tongue is deceitful in their mouth.&rdquo; The šɛqɛr runs through both false prophecy and false commerce: the prophets who speak šɛqɛr (what they know to be untrue) and the merchants who use šɛqɛr (false weights and measures). Both are calibrated to extract maximum benefit from those with no recourse — the false prophet benefits from the spiritual economy the way the false merchant benefits from the material economy. Jeremiah takes up the šɛqɛr-prophets as one of his major themes (Jer 5:31; 14:14; 23:25-26: &ldquo;they are prophesying to you a lying vision, worthless divination, and the deceit of their own minds&rdquo;). Revelation&rsquo;s &ldquo;all liars, their portion will be in the lake that burns with fire and sulfur&rdquo; (21:8) places šɛqɛr at the center of what is excluded from the new creation."
        },
        {
            "code": "H3976",
            "lemma": "מֹאזֵן",
            "translit": "mōʾzēn",
            "gloss": "scales",
            "significance": "מֹאזֵן (mōʾzēn, &lsquo;a pair of scales — used only in the dual in Hebrew, because scales have two pans&rsquo;) appears in Micah 6:11: &ldquo;Shall I acquit the man with wicked scales (mōʾznê rɛšaʿ) and with a bag of deceitful weights (ʾabnê mirzam)?&rdquo; This is the climax of the covenant lawsuit: YHWH does not merely prefer honest commerce — he cannot acquit (niqāh, declare innocent) the one who uses corrupt instruments. The mōʾzēn-question is a judicial verdict: the false scales are a crime against the covenant. The OT&rsquo;s commercial-justice legislation is unambiguous: Leviticus 19:36 &ldquo;you shall have just balances (mōʾznê ṣɛḏɛq), just weights (ʾabnê ṣɛḏɛq)&rdquo;; Deuteronomy 25:13-15 forbids two kinds of weights; Proverbs 11:1 &ldquo;a false balance is an abomination to the LORD, but a just weight is his delight.&rdquo; Micah pairs the mōʾzēn with the ephah (H374) — together, the dishonest scales and the short measure are the two instruments of systematic commercial fraud that the powerful used against the poor in the grain markets of Judah. The economic justice of Micah&rsquo;s lawsuit is not separate from the book&rsquo;s spiritual concern — the false mōʾzēn is the economic expression of the false prophet&rsquo;s spiritual dishonesty. Both systems are calibrated to benefit the powerful at the expense of those without recourse."
        },
        {
            "code": "H374",
            "lemma": "אֵיפָה",
            "translit": "ʾêpāh",
            "gloss": "ephah",
            "significance": "אֵיפָה (ʾêpāh, &lsquo;a dry measure — approximately 22 liters, the standard unit for grain transactions&rsquo;) is one of two instruments of commercial fraud in Micah 6:10: &ldquo;Can I forget any longer the treasures of wickedness in the house of the wicked, and the scant measure (ʾêpat hārāzôn) that is accursed?&rdquo; The &ldquo;scant ephah&rdquo; (ʾêpat hārāzôn — literally &ldquo;the lean, thin measure&rdquo;) was a dishonest container: slightly smaller than the standard but sold as if full. The buyer received less grain than paid for, with no practical way to detect or prove the fraud. Deuteronomy 25:14-15 prohibits this explicitly: &ldquo;You shall not have in your house two kinds of measures, a large and a small. A full and fair measure you shall have.&rdquo; Amos 8:5 identifies the same practice in the northern kingdom: merchants who &ldquo;make the ephah small and the shekel great&rdquo; — shrinking what they sell while expanding what they charge. The ʾêpāh&rsquo;s specific weight is symbolic: the grain economy touched every household in ancient Judah. A scant ʾêpāh at the market was the cumulative mechanism by which the poor were made more poor across every transaction. The curse (ʾārûr) attached to the scant ephah in Micah 6:10 is the covenant curse of Deuteronomy — the same framework that governs the blessings and cursings of the covenant applies to the measuring bowl in the marketplace."
        },
        {
            "code": "H622",
            "lemma": "אָסַף",
            "translit": "ʾāsap",
            "gloss": "gather",
            "significance": "אָסַף (ʾāsap, &lsquo;to gather for any purpose; by extension, to receive, take away, remove, or assemble&rsquo;) is Micah&rsquo;s verb of eschatological reversal. Micah 2:12: &ldquo;I will surely assemble (ʾāsōp ʾăsîpkɛm) all of you, O Jacob; I will gather (qabbēṣ) the remnant of Israel.&rdquo; Micah 4:6: &ldquo;In that day, declares the LORD, I will assemble (ʾăsōpēp) the lame and gather (qabbēṣ) those who have been driven away, and those whom I have afflicted.&rdquo; The ʾāsap is the theological reversal of the Assyrian exile: the same scattered flock that judgment sent out across the nations, YHWH&rsquo;s eschatological act brings back in. The double verb formula — ʾāsap + qabbēṣ — is the standard OT pairing for the end-time ingathering: what judgment dispersed, restoration gathers. Isaiah 56:8 uses the same structure: &ldquo;the Lord GOD, who gathers the outcasts of Israel, declares, &lsquo;I will gather yet others to him besides those already gathered.&rsquo;&rdquo; Micah 4:6 adds a detail missing from the prosperity prophets&rsquo; version: the gathered remnant includes &ldquo;the lame&rdquo; and &ldquo;those whom I have afflicted&rdquo; — the gathering is not of the strong and successful but of the broken survivors. This is the shape of grace in Micah&rsquo;s restoration oracles. The NT&rsquo;s &ldquo;he will send out his angels and gather (episynagein) his elect from the four winds&rdquo; (Matt 24:31) participates in the ʾāsap-imagery."
        },
        {
            "code": "H7626",
            "lemma": "שֵׁבֶט",
            "translit": "šēbɛṭ",
            "gloss": "rod",
            "significance": "שֵׁבֶט (šēbɛṭ, &lsquo;a scion, stick — used for punishing, writing, fighting, ruling, walking; figuratively a clan or tribe&rsquo;) appears in two pivotal Micah passages with opposite valences. Micah 5:1: &ldquo;Now muster your troops, O daughter of troops; siege is laid against us; with a rod (bašbɛṭ) they strike the judge of Israel on the cheek.&rdquo; Here the šēbɛṭ is the weapon of humiliation: striking the judge on the cheek is the ritual insult of royal defeat (cf. Jesus before Pilate and Caiaphas in Matt 26:67; John 18:22). The šēbɛṭ-blow precedes the messianic oracle of 5:2 — the humiliation of Israel&rsquo;s current leadership is the context into which the announcement of the Bethlehem ruler is spoken. Micah 7:14: &ldquo;Shepherd your people with your staff (bĕšibṭɛkā), the flock of your inheritance, who dwell alone in a forest in the midst of a garden land.&rdquo; Here the šēbɛṭ is the shepherd&rsquo;s staff — the instrument of protective leadership. The same word in 5:1 strikes the judge in defeat; in 7:14 it guides the flock in protection. The OT&rsquo;s royal vocabulary includes šēbɛṭ as &ldquo;scepter&rdquo;: Genesis 49:10 (&ldquo;the scepter shall not depart from Judah&rdquo;), Psalm 2:9 (&ldquo;you shall break them with a rod of iron&rdquo;), Numbers 24:17 (&ldquo;a scepter shall rise out of Israel&rdquo;). The šēbɛṭ-movement in Micah — from the weapon of Israel&rsquo;s humiliation (5:1) to the shepherd-king&rsquo;s staff (7:14) — is the same arc as the messianic promise itself: from defeat to restoration under the Bethlehem ruler."
        },
        {
            "code": "H7611",
            "lemma": "שְׁאֵרִית",
            "translit": "šĕʾērîṯ",
            "gloss": "remnant",
            "significance": "שְׁאֵרִית (šĕʾērîṯ, &lsquo;a remainder, residual, surviving portion — the part that is left over after destruction or loss&rsquo;) is the theological hinge between Micah&rsquo;s judgment oracles and his restoration oracles. Micah 2:12: &ldquo;I will surely assemble all of you, O Jacob; I will gather the remnant (šĕʾērîṯ) of Israel.&rdquo; Micah 5:7: &ldquo;the remnant of Jacob (šĕʾērîṯ yaʿăqōb) shall be in the midst of many peoples like dew from the LORD.&rdquo; Micah 5:8: &ldquo;the remnant of Jacob (šĕʾērîṯ yaʿăqōb) shall be among the nations.&rdquo; Micah 7:18: &ldquo;pardoning iniquity and passing over transgression for the remnant of his inheritance (šĕʾērîṯ naḥălāṯô).&rdquo; The šĕʾērîṯ concept is neither optimistic nor pessimistic: it concedes that most of Israel will not survive the coming judgment, while insisting that YHWH preserves a portion through which the covenant promises to Abraham, Moses, and David are fulfilled. The remnant is smaller than Israel but not a replacement for Israel — it is the thread of continuity through catastrophe. Micah&rsquo;s šĕʾērîṯ-theology shapes Isaiah&rsquo;s &ldquo;holy seed is its stump&rdquo; (6:13), Jeremiah&rsquo;s &ldquo;I will gather the remnant of my flock out of all the countries where I have driven them&rdquo; (23:3), and Paul&rsquo;s &ldquo;a remnant chosen by grace&rdquo; (Rom 11:5). The NT applies the šĕʾērîṯ-logic to the first-century followers of Jesus: the faithful remnant within Israel through whom the Gentile ingathering now proceeds."
        },
        {
            "code": "H4310",
            "lemma": "מִי",
            "translit": "mî",
            "gloss": "who?",
            "significance": "מִי (mî, &lsquo;who? — the interrogative pronoun for persons; also used in rhetorical questions expecting no human answer&rsquo;) appears in the book&rsquo;s theological climax and simultaneously its interpretive key: Micah 7:18: &ldquo;Who (mî) is a God like you, pardoning iniquity and passing over transgression for the remnant of his inheritance? He does not retain his anger forever, because he delights in steadfast love (ḥɛsɛḏ).&rdquo; The rhetorical mî-question expects no human answer because no comparable God exists. But the mi-question is not incidental to Micah: the prophet&rsquo;s own name is mîkāyāhû (Micah), which means precisely &ldquo;who is like YHWH?&rdquo; (mî + kāmôkā + yāhû). The book&rsquo;s final question is embedded in the prophet&rsquo;s own identity: seven chapters of indictment, messianic promise, covenant lawsuit, and šĕʾērîṯ-hope converge on the mî-question that Micah&rsquo;s name has been asking from the beginning. The answer the book supplies is: this God is the one who pardons, who does not retain anger forever, who will cast all our sins into the depths of the sea (7:19). Micah 7:18-20 is the most concentrated statement of divine character in the twelve minor prophets — it stands in Micah the way Romans 8:31-39 stands in Paul: a doxological outburst at the end of a long argument, declaring that the case rests on the character of God. The NT&rsquo;s &ldquo;who shall bring any charge against God&rsquo;s elect?&rdquo; (Rom 8:33) is the mî-question in its Pauline form."
        }
    ],

    "language_notes": (
        "<p>Micah is structured as <strong>three alternating cycles of judgment and hope</strong>, each opening with indictment and closing with promise: cycles in chapters 1–2, 3–5, and 6–7. This oscillating structure can disorient readers expecting a narrative arc — Micah moves from announcing Jerusalem&rsquo;s destruction (3:12) to announcing its exaltation (4:1-3) within a few verses, and from the scathing covenant lawsuit of chapter 6 to the doxological conclusion of 7:18-20 within the same movement. The oscillation is not inconsistency but the distinctive shape of prophetic eschatology: judgment and restoration are both real, both YHWH&rsquo;s acts, and the relationship between them is cruciform — the corrupt city is destroyed so that the purified city may be established. Reading any half of Micah without the other half is reading half a theology.</p>"
        "<p>Micah speaks as a <strong>rural voice against the urban elite</strong> — his hometown, Moresheth-Gath, was a small village in the Shephelah of Judah, and his perspective is explicitly that of the rural poor whose agricultural land is being seized (2:1-2) and whose community is being dismantled. This gives Micah&rsquo;s rhetoric an intensity that differs from Isaiah&rsquo;s more courtly register: he uses agricultural metaphors (the plowed field, the threshing ox, the scattered flock) that root his theology in the physical reality of 8th-century Judean farming life. The covenant for Micah is not an abstraction but a system of land tenure, weight and measure, and economic relationship — and it is being systematically violated by people with the legal and social power to do so. The literary effect is that Micah&rsquo;s indictments are strikingly concrete: not &ldquo;the people have sinned&rdquo; but &ldquo;they devise wickedness on their beds and execute it in the morning&rdquo; (2:1), not &ldquo;the leaders are corrupt&rdquo; but &ldquo;you hate the good and love the evil, who tear the skin from off my people and their flesh from off their bones&rdquo; (3:2).</p>"
        "<p>Micah 6:1-8 is formally structured as a <strong>covenant lawsuit</strong> (Hebrew rîb), a legal proceeding in which YHWH calls creation itself as witness. The mountains and hills are summoned to hear YHWH&rsquo;s case against Israel (6:1-2). The rhetorical exchange then proceeds: YHWH rehearses his saving acts (6:3-5); the people offer increasingly extravagant sacrificial proposals (6:6-7, culminating in the absurd &ldquo;ten thousands of rivers of oil&rdquo; and the human sacrifice reference); YHWH responds with the three-fold summary of 6:8. The force of 6:8 depends entirely on its lawsuit context: it is not a free-floating ethical aphorism but a covenant verdict delivered after the people have been shown that no amount of sacrifice substitutes for the covenant relationship itself. &ldquo;He has told you, O man, what is good&rdquo; — the emphasis is on &lsquo;told you,&rsquo; i.e., this is not new information. The answer was given in the Torah; the question is only whether Israel would live it.</p>"
    ),

    "reception": (
        "<p><strong>Micah in Jeremiah&rsquo;s court:</strong> The most historically documented reception of any prophetic text in the OT is the citation of Micah 3:12 in Jeremiah 26:18. When Jeremiah announces judgment on the temple and is seized for execution, the elders of Judah cite Micah as precedent: &ldquo;Micah of Moresheth prophesied in the days of Hezekiah king of Judah, and said to all the people of Judah: &lsquo;Zion shall be plowed as a field.&rsquo;&rdquo; Their argument is that Hezekiah repented in response to Micah&rsquo;s word, and YHWH relented — therefore killing Jeremiah would be wrong. This is extraordinary: a century after Micah&rsquo;s ministry, his words function as a living legal resource that saves another prophet&rsquo;s life. The citation also shows that Micah&rsquo;s judgment-oracle was understood not as inevitable but as conditional — a call to repentance that can be heard or ignored.</p>"
        "<p><strong>Matthew and Luke on Bethlehem:</strong> Micah 5:2 is among the most frequently cited OT texts in the NT nativity accounts. Matthew 2:6 cites it as the answer to Herod&rsquo;s question about where the Christ is to be born, slightly adapting the text to emphasize that Bethlehem will produce &ldquo;a ruler who will shepherd my people Israel.&rdquo; Luke&rsquo;s account confirms the Bethlehem birth without citing Micah directly, while John 7:42 shows that the Bethlehem-Messiah connection was common knowledge in Jesus&rsquo; day (&ldquo;has not the Scripture said that the Christ comes from the offspring of David, and comes from Bethlehem?&rdquo;). Early Christian commentary from Justin Martyr and Origen to Augustine used Micah 5:2&rsquo;s &ldquo;from ancient days&rdquo; as evidence for Christ&rsquo;s pre-existence and divine origin.</p>"
        "<p><strong>Micah 6:8 in modern reception:</strong> &ldquo;Do justice, love kindness, walk humbly with your God&rdquo; has functioned as the OT&rsquo;s most quoted ethical summary in Western Christian and Jewish social ethics — cited in abolitionist literature, social gospel theology (Walter Rauschenbusch regularly invoked it), liberation theology, and contemporary social justice movements. This breadth of appropriation has sometimes separated 6:8 from its covenant-lawsuit context: the verse presupposes that the questioner has been shown that no sacrifice substitutes for covenant faithfulness, which gives it a different weight than as a general ethical maxim. Jesus&rsquo;s citation of &ldquo;you tithe mint and dill and cumin, and have neglected the weightier matters of the law: justice and mercy and faithfulness&rdquo; (Matt 23:23) is a compressed version of the Micah 6 argument.</p>"
    ),

    "reading_guide": (
        "<p><strong>Read the three cycles as one oscillating movement.</strong> Chapters 1–3 indict both Samaria and Jerusalem; chapters 4–5 promise restoration and the Bethlehem ruler; chapters 6–7 re-open the lawsuit and close with doxology. Each cycle moves from the same question (covenant failure) toward the same answer (YHWH&rsquo;s faithfulness). The oscillation is the point: judgment and restoration are not sequential events but simultaneous truths held in tension throughout the book.</p>"
        "<p><strong>Read Micah 6:8 in its lawsuit context.</strong> The verse follows six verses in which the people ask what offerings would be sufficient to satisfy YHWH — escalating from burnt offerings to rivers of oil to firstborn children (6:6-7). The absurdity of the escalation is deliberate: the people are looking for the price that buys them out of covenant obligation. YHWH&rsquo;s response in 6:8 rejects the entire premise: the covenant is not a fee schedule. &ldquo;He has told you, O man, what is good&rdquo; refers to the Torah already given — the lawsuit is about refusal, not ignorance.</p>"
        "<p><strong>Read the ending (7:18-20) as the theological answer to the entire book.</strong> Micah has indicted Israel at length. The covenant lawsuit exposed the gap between what YHWH requires and what Israel has done. The question the book raises is: what happens to a people who have violated their covenant this comprehensively? The answer is: a God who pardons iniquity, who does not retain his anger forever, who will cast all our sins into the depths of the sea (7:19). The doxology answers the lawsuit. The mî-question (&ldquo;who is a God like you?&rdquo;) is the book&rsquo;s final argument: the hope of the šĕʾērîṯ rests not on Israel&rsquo;s performance but on YHWH&rsquo;s character.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('micah')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('micah', merged)

main()
