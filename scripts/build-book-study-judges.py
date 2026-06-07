"""
Book Study Data — Judges
book_id: judges
lang: hebrew

Run: python3 scripts/build-book-study-judges.py

Notes:
- Author group: Historical (Joshua-Esther) in author-freq-hebrew.json
- 12 vocab entries; Hebrew translit fields blank in glossary — supplied manually
- Historical-group peaks are very generic; vocab selected for theological weight
  in Judges specifically (the Deuteronomistic cycle, judge-deliverer, Spirit-empowerment)
- H5800 azab (forsake) and H7451 ra (evil) have Wisdom peaks but are structurally
  essential to the cycle formula
- H5869 ayin (eye) and H3477 yashar (right) are paired in the key verse 21:25
- H3467 yasha (save): Wisdom peak but is the root of the book's central action
  and of the names Joshua/Jesus
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
    "bookId": "judges",

    "key_vocabulary": [
        {
            "code": "H8199",
            "lemma": "שָׁפַט",
            "translit": "šāpaṭ",
            "gloss": "judge",
            "significance": "שָׁפַט (shapat, &lsquo;to judge, to govern, to decide, to deliver&rsquo;) gives the book its name — the Hebrew title is <em>Shofetim</em> (שֹׁפְטִים, judges). But the shofet in Judges is not primarily a courtroom arbiter: the role encompasses military deliverance, tribal leadership, and covenant adjudication. YHWH &lsquo;raises up&rsquo; (qum) each shofet and empowers them with his Spirit for the specific crisis at hand. The twelve major and minor judges are emphatically not moral exemplars — Gideon makes an ephod that becomes an idol (8:27); Jephthah makes a rash vow (11:30-40); Samson&rsquo;s appetites repeatedly undermine his calling. The deliberate presentation of flawed deliverers is the book&rsquo;s theological argument: Israel does not need better human judges — it needs a king who will lead in covenant faithfulness (21:25), and ultimately a perfect King who never fails. Hebrews 11:32 names several judges (Gideon, Barak, Samson, Jephthah) among the heroes of faith — not for their moral record but for their trust in YHWH&rsquo;s power to save through them despite themselves."
        },
        {
            "code": "H5800",
            "lemma": "עָזַב",
            "translit": "ʿāzab",
            "gloss": "forsake",
            "significance": "עָזַב (azab, &lsquo;to forsake, to abandon, to leave behind&rsquo;) is the cycle&rsquo;s sin-verb. &lsquo;Israel forsook YHWH (עָזְבוּ אֶת יְהוָה)&rsquo; appears at the opening of each new cycle (2:12; 2:13; 10:6, 10) and is the precise term for Israel&rsquo;s covenant failure. The word is relational rather than merely behavioral: Israel does not simply stop performing religious acts — they abandon a person to whom they are covenant-bound. The imagery is marital — YHWH as the faithful husband whom Israel keeps leaving (cf. Hos 2:13). When Israel cries out and YHWH responds, the narrative sometimes records his pointed question: &lsquo;You have forsaken me (עֲזַבְתֶּם אֹתִי) and served other gods; therefore I will save you no more&rsquo; (10:13) — the grace that has responded to eleven previous cycles is not unconditional. The prophets make azab their primary vocabulary for Israel&rsquo;s sin: Isaiah 1:4 (&lsquo;they have forsaken YHWH&rsquo;); Jeremiah 1:16 (&lsquo;they have forsaken me&rsquo;). The NT inverts this: Jesus promises &lsquo;I will never leave (ἐγκαταλείπω, the LXX&rsquo;s azab-equivalent) you or forsake you&rsquo; (Heb 13:5, citing Deut 31:6) — the divine Deliverer does what Israel kept failing to do."
        },
        {
            "code": "H7451",
            "lemma": "רַע",
            "translit": "raʿ",
            "gloss": "evil",
            "significance": "רַע (ra, &lsquo;evil, wicked, bad, harmful&rsquo;) is the cycle&rsquo;s moral evaluator. The formula <em>וַיַּעֲשׂוּ בְנֵי יִשְׂרָאֵל אֶת הָרַע בְּעֵינֵי יְהוָה</em> (&lsquo;the Israelites did what was evil in the eyes of YHWH&rsquo;) triggers each new cycle (2:11; 3:7, 12; 4:1; 6:1; 10:6; 13:1). The Hebrew word ra is semantically unified in a way English &lsquo;evil&rsquo; is not — it covers both moral wickedness and the harmful consequences that wickedness produces. Judges shows this unity concretely: Israel&rsquo;s spiritual ra (apostasy, Baal-worship) produces ra-as-consequence (enemy oppression, degradation, social collapse). The book does not moralize in the abstract — it demonstrates the material social cost of covenant unfaithfulness. The appendices (chs. 17-21) show ra normalized: a Levite&rsquo;s concubine is gang-raped and killed (ch. 19) with explicit Sodom echoes (Gen 19) — the covenant people have become indistinguishable from the nations they were supposed to displace. This is ra reaching its logical terminus."
        },
        {
            "code": "H5869",
            "lemma": "עַיִן",
            "translit": "ʿayin",
            "gloss": "eye",
            "significance": "עַיִן (ayin, &lsquo;eye, sight, the organ of perception and moral evaluation&rsquo;) appears in two contrasting formulas that frame the entire book. The condemnation formula — &lsquo;did evil in the <strong>eyes</strong> (עֵינֵי) of YHWH&rsquo; (2:11; 3:7, 12; 4:1; 6:1; 10:6; 13:1) — positions YHWH&rsquo;s sight as the authoritative moral evaluator. The epitaph formula — &lsquo;everyone did what was right in his own <strong>eyes</strong> (בְּעֵינָיו)&rsquo; (17:6; 21:25) — shows the substitution that has taken place: the human self has replaced YHWH as the moral reference point. The collision between these two phrases is Judges&rsquo; central conflict: whose eyes define what is right? YHWH&rsquo;s assessment or Israel&rsquo;s self-assessment? The book&rsquo;s narrative body (the cycle episodes) answers the question empirically — what looks right to Israel (the Baals who seem to produce rain and crops) turns out to be what is evil in YHWH&rsquo;s eyes. The Proverbs draw the conclusion: &lsquo;There is a way that seems right (יָשָׁר) to a man, but its end is the way to death&rsquo; (Prov 14:12; 16:25)."
        },
        {
            "code": "H3477",
            "lemma": "יָשָׁר",
            "translit": "yāšār",
            "gloss": "right",
            "significance": "יָשָׁר (yashar, &lsquo;right, straight, level, upright&rsquo;) appears in Judges&rsquo; defining epitaph: &lsquo;everyone did what was right (הַיָּשָׁר) in his own eyes&rsquo; (17:6; 21:25). The word itself is not ironic — yashar is the standard positive term for ethical uprightness in Deuteronomy (&lsquo;you shall do what is right [הַיָּשָׁר] and good in YHWH&rsquo;s sight,&rsquo; 6:18) and in Proverbs. Judges&rsquo; bitter irony is that the people are doing what they judge to be genuinely yashar — genuinely right, genuinely straight — but the reference point has shifted from YHWH&rsquo;s standard to their own. The problem is not that Israel abandons all morality but that it privatizes morality — each person becomes their own moral authority. This is the condition of radical autonomy, and Judges traces its social consequences across twenty-one chapters: without an external moral authority (a king who submits to YHWH&rsquo;s Torah), the concept of &lsquo;yashar&rsquo; dissolves into whatever each tribe, household, or individual prefers. The New Testament&rsquo;s claim that there is one who is the Way (ὁδός, hodos — the LXX&rsquo;s yashar-related path) is the antithesis of the Judges condition."
        },
        {
            "code": "H2199",
            "lemma": "זָעַק",
            "translit": "zāʿaq",
            "gloss": "cry out",
            "significance": "זָעַק (zaaq, &lsquo;to cry out, to call for help from distress&rsquo;) is the cycle&rsquo;s turning point. After foreign oppression has ground Israel down, &lsquo;the Israelites cried out (זָעַק) to YHWH&rsquo; (3:9, 15; 4:3; 6:6-7; 10:10; cf. related forms throughout) — and YHWH raises up a deliverer. It is this cry, not repentance or reformation, that consistently triggers divine response. Israel does not turn from the Baals before crying out; they simply cry from pain. YHWH responds anyway — grace extended to the minimum expression of need. This is the pattern Exodus establishes: &lsquo;the people of Israel groaned because of their slavery and cried out for help...God heard their groaning, and God remembered his covenant&rsquo; (Exod 2:23-24). The zaaq is not merit — it is the acknowledgment of helplessness that opens space for divine action. In Judges 10:11-14, YHWH pointedly refuses this pattern for one cycle and demands genuine turning; but he relents when Israel puts away the foreign gods (10:15-16). The psalms liturgize the zaaq: &lsquo;Out of the depths I cry to you, O YHWH&rsquo; (Ps 130:1) — the cry of need is already the beginning of the prayer that God answers."
        },
        {
            "code": "H7307",
            "lemma": "רוּחַ",
            "translit": "rûaḥ",
            "gloss": "spirit",
            "significance": "רוּחַ (ruach, &lsquo;spirit, wind, breath&rsquo;) of YHWH is the empowering force that enables the judges to accomplish their deliverances. &lsquo;The Spirit of YHWH came upon (עָלָה עַל / הָיְתָה עַל) &rsquo; Othniel (3:10), Gideon (6:34 — literally &lsquo;clothed itself with Gideon&rsquo;), Jephthah (11:29), and Samson (13:25; 14:6, 19; 15:14). Each time, the ruach enables what natural human ability cannot: military courage beyond normal capacity, extraordinary physical strength, prophetic boldness. The ruach in Judges is episodic — it comes upon the judges for specific tasks and is not permanent. This episodic character is the OT&rsquo;s standard mode: the Spirit moves and acts for particular purposes, is not universally distributed, and can depart (16:20 — Samson &lsquo;did not know that YHWH had left him&rsquo;). The tragic arc of Samson is precisely the loss of the ruach through covenant violation. The NT marks the eschatological transformation: Jesus promises a Spirit who will &lsquo;abide with you forever&rsquo; (John 14:16), and Pentecost makes permanent what was episodic — the ruach poured out on &lsquo;all flesh&rsquo; (Acts 2:17, citing Joel 2:28) rather than on selected deliverers."
        },
        {
            "code": "H1168",
            "lemma": "בַּעַל",
            "translit": "baʿal",
            "gloss": "Baal",
            "significance": "בַּעַל (Baal, from the root &lsquo;to master, to own, to possess&rsquo;) means &lsquo;lord, master, owner, husband&rsquo; and is both a title and the name of the Canaanite storm and fertility deity. In Judges, &lsquo;the Baals&rsquo; (הַבְּעָלִים, ha-Baalim) is the standard plural for the local manifestations of Baal worship that Israel pursues: &lsquo;they abandoned YHWH and served the Baals and the Ashtoreths&rsquo; (2:12-13; 2:19; 3:7; 8:33; 10:6, 10). Baal worship was the Canaanite fertility religion: the storm god Baal made rain, and rain made crops. For a people transitioning from wilderness (manna-dependence on YHWH) to settled agriculture (harvest-dependence on weather), the temptation was to adopt the local religious technology for agricultural success. The theological problem was covenantal: YHWH had already promised rain in exchange for covenant faithfulness (Deut 28:12) and drought for unfaithfulness (28:23-24). Baal worship was therefore a statement that YHWH&rsquo;s covenant was insufficient for practical life — a practical rejection of sovereignty dressed in agricultural pragmatism. The Elijah-Baal contest on Carmel (1 Kgs 18) is the definitive confrontation; Judges is the pattern of repeated compromise that explains why Elijah was necessary."
        },
        {
            "code": "H3027",
            "lemma": "יָד",
            "translit": "yād",
            "gloss": "hand",
            "significance": "יָד (yad, &lsquo;hand&rsquo;) appears in the two formulas that together describe the cycle&rsquo;s movement. The judgment formula: &lsquo;YHWH delivered them into the hand (בְּיַד) of plunderers&rsquo; (2:14); &lsquo;YHWH sold them into the hand of [enemy king]&rsquo; (3:8; 4:2; 10:7; 13:1). The deliverance formula: &lsquo;YHWH gave [the enemy] into their hand&rsquo; (3:10; 4:7, 14; 7:7; 8:3; 11:32). The yad represents power, agency, and control — to be &lsquo;in the hand of&rsquo; someone is to be subject to their power. The cycle is entirely a matter of which hand holds which: at each cycle&rsquo;s beginning, Israel is in the enemy&rsquo;s hand; at each cycle&rsquo;s end (through YHWH&rsquo;s deliverance), the enemy is in Israel&rsquo;s hand. This is not military notation — it is a theological claim about sovereignty: YHWH transfers power from hand to hand according to covenant faithfulness and his own compassion. Jesus&rsquo;s &lsquo;no one can snatch them out of my hand&rsquo; (John 10:28) and Paul&rsquo;s &lsquo;neither death nor life...will be able to separate us from the love of God in Christ Jesus&rsquo; (Rom 8:38-39) describe the security of being in the hand of the one whose grip cannot be broken."
        },
        {
            "code": "H3467",
            "lemma": "יָשַׁע",
            "translit": "yāšaʿ",
            "gloss": "save",
            "significance": "יָשַׁע (yasha, &lsquo;to save, to deliver, to bring to safety, to give victory&rsquo;) is the root of the names Joshua (יְהוֹשׁוּעַ, &lsquo;YHWH saves&rsquo;) and Jesus (Ἰησοῦς). In Judges, YHWH &lsquo;raised up a deliverer (מוֹשִׁיעַ, moshia — Hiphil participle of yasha) who saved (וַיּוֹשִׁיעֵם) them&rsquo; (3:9, 15). The moshia (savior/deliverer) is the judge&rsquo;s functional title — one who performs yasha for the people. Each judge-moshia is a temporary and partial savior: they save Israel from the immediate oppressor, but the cycle restarts. The repeated moshia-figures accumulate into a promise: if the pattern produces such deliverers, the logic points toward a final, permanent Moshia. Isaiah 45:21-22 draws the line: &lsquo;there is no other God besides me, a righteous God and a Savior (מוֹשִׁיעַ); there is none besides me.&rsquo; The NT names the fulfillment: &lsquo;you shall call his name Jesus (Ἰησοῦς), for he will save (σώσει) his people from their sins&rsquo; (Matt 1:21). The saving-pattern of Judges becomes the vocabulary for the ultimate deliverance."
        },
        {
            "code": "H3581",
            "lemma": "כֹּחַ",
            "translit": "kōaḥ",
            "gloss": "strength",
            "significance": "כֹּחַ (koach, &lsquo;strength, force, power, physical or spiritual capacity&rsquo;) is the narrative linchpin of the Samson cycle. Samson&rsquo;s extraordinary physical koach is repeatedly demonstrated: killing a lion bare-handed (14:6), carrying Gaza&rsquo;s city gates (16:3), pulling down the temple pillars (16:30). But the narrative does not celebrate raw koach — it is a tragedy of koach unmoored from covenant faithfulness. Samson&rsquo;s strength is a gift of the Spirit tied to his Nazirite consecration; when the vow is violated (his hair shaved, 16:17-19), his koach departs. &lsquo;He did not know that YHWH had left him&rsquo; (16:20) — the Spirit&rsquo;s departure is simultaneous with the loss of koach, and Samson cannot tell the difference, which is the tragedy&rsquo;s sharpest edge. A man of extraordinary Spirit-given koach was repeatedly outmaneuvered by his appetites — women, revenge, pride — until his gift was neutralized by his compromises. The pattern extends to every judge: the Spirit gives koach adequate for the task; human weakness undermines the gift. Samson&rsquo;s final koach (16:28-30) comes after his eyes are put out, his pride destroyed, his pretensions ended — only then does he pray and receive strength one last time. Paul&rsquo;s &lsquo;when I am weak, then I am strong&rsquo; (2 Cor 12:10) is the theology that Samson demonstrates negatively and then finally enacts."
        },
        {
            "code": "H5315",
            "lemma": "נֶפֶשׁ",
            "translit": "nepeš",
            "gloss": "soul",
            "significance": "נֶפֶשׁ (nephesh, &lsquo;soul, life, self, throat — the whole living person oriented toward need and desire&rsquo;) reaches its most dramatic expression in Judges in Samson&rsquo;s death: &lsquo;Let me die (תָּמֹת נַפְשִׁי, let my nephesh die) with the Philistines&rsquo; (16:30). Samson&rsquo;s whole self — his embodied life, desires, will, and capacity — is offered in a final act that simultaneously destroys more enemies than his entire life of killing. The nephesh in Hebrew is not a Greek soul that escapes the body at death; it is the integrated, desiring, embodied self — which is why Samson&rsquo;s nephesh can &lsquo;die with the Philistines.&rsquo; The typological resonance noted in the introduction data is precise: Samson stands with arms spread between two pillars, and his voluntary death achieves what his life could not — the structural shape of crucifixion-sacrifice that destroys more through dying than through living. Judges traces the nephesh in each judge: their desires (sexual, vengeful, ambitious) repeatedly subvert their Spirit-given calling. Samson is the most acute case — his nephesh-desires (three women, revenge) are both his greatest vulnerability and the means through which YHWH accomplishes the final deliverance anyway."
        }
    ],

    "language_notes": (
        "<p>Judges is built around a <strong>precise cycle formula</strong> whose Hebrew vocabulary is not varied randomly but locked: (1) <strong>עָזַב</strong> (azab, &lsquo;forsook YHWH&rsquo;) → (2) <strong>הָרַע</strong> (ha-ra, &lsquo;did evil in YHWH&rsquo;s eyes&rsquo;) → (3) <strong>נָתַן בְּיַד</strong> (natan beyad, &lsquo;delivered into the hand of enemy&rsquo;) → (4) <strong>זָעַק</strong> (zaaq, &lsquo;cried out to YHWH&rsquo;) → (5) <strong>הֵקִים</strong> (heqim, &lsquo;raised up a deliverer&rsquo;) → (6) <strong>הוֹשִׁיעַ</strong> (hosia, &lsquo;saved them&rsquo;) → (7) <strong>שָׁקַט</strong> (shaqat, &lsquo;the land had rest&rsquo;). This seven-step formula appears in condensed or expanded form in each major judge cycle (2:11-19; 3:7-11; 3:12-30; 4:1-5:31; 6:1-8:35; 10:6-12:15; 13:1-16:31). The formula is not mere repetition — it is a liturgical rhythm that trains the reader to recognize the pattern as theological argument: the cycle is the shape of Israel&rsquo;s covenant history when YHWH&rsquo;s law is not the ruling standard. Reading Judges&rsquo; individual stories without the cycle formula is like reading individual waves without seeing the tide.</p>"
        "<p>Two contrasting <strong>evaluative formulas</strong> orient the entire book. The condemnation formula &lsquo;did evil in the <em>eyes</em> (עֵינֵי) of YHWH&rsquo; (2:11; 3:7, 12; 4:1; 6:1; 10:6; 13:1) establishes YHWH as the authoritative moral evaluator — what matters is how things look from the divine vantage. The epitaph formula &lsquo;everyone did what was <em>right</em> (יָשָׁר) in his own <em>eyes</em> (עֵינָיו)&rsquo; (17:6; 21:25) shows what happens when YHWH&rsquo;s evaluative eyes are replaced by each person&rsquo;s own. The same word <em>ayin</em> (eye) appears in both formulas, making the contrast structural in the Hebrew: YHWH&rsquo;s ayin vs. each person&rsquo;s ayin. The Proverbs extract the principle: &lsquo;There is a way that seems right (יָשָׁר) to a man, but its end is the way to death&rsquo; (Prov 14:12; 16:25) — exactly the Judges condition articulated as wisdom-warning.</p>"
        "<p>The <strong>Song of Deborah</strong> (Judges 5) is widely regarded as one of the oldest extended texts in the Hebrew Bible, and its archaic language confirms an early date. Distinctive features: the use of archaic verb forms (the qatal where later prose uses wayyiqtol); archaic pronouns (שֶׁ as a relative pronoun rather than the standard אֲשֶׁר); rare vocabulary attested only in early poetry (e.g., פְּרָזוֹן, &lsquo;peasantry/open-country fighters,&rsquo; 5:7, 11); the use of epic repetition (&lsquo;Blessed above women is Jael...blessed above women in the tent,&rsquo; 5:24) that resembles Ugaritic parallel poetry. The Song preserves a warrior-hymn tradition much older than the surrounding prose narrative (ch. 4) that retells the same events. The two chapters together (narrative + poem on the same event) are one of the Hebrew Bible&rsquo;s clearest examples of the deliberate literary pairing of prose and poetry — each mode illuminating what the other cannot.</p>"
        "<p>The <strong>Spirit-language</strong> in Judges uses three related expressions for divine empowerment. The most common is <em>וַתְּהִי עָלָיו רוּחַ יְהוָה</em> (&lsquo;and the Spirit of YHWH was upon him,&rsquo; 3:10; 11:29) — the ruach &lsquo;comes to rest on&rsquo; the judge. A more dramatic form appears for Gideon: <em>וְרוּחַ יְהוָה לָבְשָׁה אֶת גִּדְעוֹן</em> (&lsquo;the Spirit of YHWH clothed itself with Gideon,&rsquo; 6:34) — the Piel of לָבַשׁ (lavash, &lsquo;to clothe/put on&rsquo;) makes the Spirit the subject and Gideon the garment, an image of total enveloping possession. For Samson, the formula is most physical: <em>וַתִּצְלַח עָלָיו רוּחַ יְהוָה</em> (&lsquo;the Spirit of YHWH rushed upon him,&rsquo; 14:6, 19; 15:14) — the verb צָלַח (tsalach) suggests a sudden, powerful surge. The variation in vocabulary tracks the variation in how the Spirit works: Othniel and Jephthah receive the Spirit for leadership; Gideon for transformed identity; Samson for physical power. The NT Pentecost narrative uses similar physical imagery (rushing wind, tongues of fire, Acts 2:1-4) for the permanent coming of the Spirit on all believers.</p>"
    ),

    "reception": (
        "<p><strong>NT and patristic:</strong> The NT&rsquo;s primary reception of Judges is Hebrews 11:32, which lists Gideon, Barak, Samson, and Jephthah as heroes of faith — a selection that would have shocked the original audience, since none of these men is morally exemplary. The point is precisely that faith is the operative category, not moral achievement. Augustine (<em>City of God</em> I.21; XVIII.19) engaged the judges carefully, defending Samson&rsquo;s suicide as unique because divinely authorized — not a precedent for self-destruction but a special case of a man who &lsquo;was compelled by the Spirit who wrought miracles through him.&rsquo; Origen read Samson allegorically as a type of Christ, and several patristic writers noted the Samson-crucifixion parallel: arms extended between the pillars, his death more destructive of enemies than his life. Ambrose wrote extensively on Deborah as a model of prophetic and civic virtue.</p>"
        "<p><strong>Reformation:</strong> Luther read the judges primarily through the lens of divine grace operating through human weakness — precisely the unglamorous kind of grace that works through flawed instruments. The judges were evidence that YHWH can use anyone, regardless of moral standing, when covenant promise drives the action. Calvin&rsquo;s commentary on Judges emphasized the typological function: each judge prefigures Christ, not by moral likeness but by structural role — the deliverer raised up in Israel&rsquo;s darkest moment. The Reformation&rsquo;s recovery of the literal-historical sense gave new grounding to the typological reading: the judges were real people in real history whose patterns genuinely anticipated the pattern of redemption.</p>"
        "<p><strong>Modern scholarship:</strong> Three debates shape contemporary Judges study. First, the <em>Deuteronomistic History</em> framework: Noth&rsquo;s hypothesis that Judges is part of a unified theological history (Deuteronomy through 2 Kings) shaped by Deuteronomic theology has been broadly accepted, though its details are debated. Second, <em>feminist readings</em> of Deborah, Jael, and the Levite&rsquo;s concubine have transformed interpretation: Deborah and Jael have been read as counterexamples to patriarchal norms; the concubine&rsquo;s fate (chs. 19-21) has been read as the book&rsquo;s sharpest moral indictment, with the narrative&rsquo;s silence functioning as accusation. Third, <em>the Samson-Christ typology</em> has been explored with renewed rigor: the structural parallels (Nazirite consecration, Spirit-empowerment, betrayal by intimates, death between the pillars) are now read as more than incidental.</p>"
    ),

    "reading_guide": (
        "<p>Read Judges with the cycle formula as your structural key: apostasy → oppression → crying out → deliverance → rest → repeat. Each judge episode follows this pattern, and tracking it makes the book&rsquo;s argument visible. The judges get progressively worse — Othniel (ch. 3) is completely positive; Gideon (chs. 6-8) is heroic but makes a fatal error; Jephthah (chs. 10-12) makes a rash vow with horrific consequences; Samson (chs. 13-16) is almost entirely self-serving. The downward trajectory is deliberate: the book is arguing that the cycle cannot sustain Israel. The cycle itself is the problem, not a solution.</p>"
        "<p>Read the appendices (chs. 17-21) as the book&rsquo;s diagnostic conclusion rather than as afterthoughts. These chapters — the Micah shrine (17-18) and the Levite&rsquo;s concubine (19-21) — do not follow the cycle format. They show what Israelite life looks like without any deliverer at all, without even the cry to YHWH: idolatry improvised in private homes, civil war, gang rape, tribal genocide. The refrain &lsquo;there was no king in Israel; everyone did what was right in his own eyes&rsquo; (17:6; 21:25) frames the appendices as the explanatory caption: this is what the cycle&rsquo;s terminal condition looks like.</p>"
        "<p>Common misreadings to avoid: (1) reading Samson as a hero — he is a warning; his gifts and his appetites are both spectacular, and the tragedy is that the gifts serve the appetites rather than the covenant; (2) treating the judges as moral models — Hebrews 11 cites them for faith amid failure, not for exemplary character; (3) skipping Deborah&rsquo;s Song (ch. 5) — it is the oldest extended Hebrew poetry in the Bible and the key to how Israel understood its own history as a liturgical event.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('judges')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('judges', merged)

main()
