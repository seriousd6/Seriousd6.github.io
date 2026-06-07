"""
Book Study Data — 1 Samuel
book_id: 1samuel
lang: hebrew

Run: python3 scripts/build-book-study-1samuel.py

Notes:
- Author group: Historical (Joshua-Esther) in author-freq-hebrew.json
- 12 vocab entries; Hebrew translit fields blank in glossary — supplied manually
- Historical-group peaks are generic; vocab selected for 1 Samuel's specific theology:
  anointing/Messiah, Hannah's prayer, YHWH-sees-the-heart, the shaal etymology of
  Saul's name, Jonathan/David covenant, Saul's rejection, sacrifice vs. obedience,
  David-the-shepherd, kingdom-theology, Hannah's rum/exaltation-song, horn/qeren,
  and Saul's shamar-failure
- H7462 raah (shepherd): different root from H7200 raah (see), same spelling, distinct codes
- H6419 palal: glossary thought-tier says '-ing' (placeholder); using 'pray' as gloss
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
    "bookId": "1samuel",

    "key_vocabulary": [
        {
            "code": "H4886",
            "lemma": "מָשַׁח",
            "translit": "māšaḥ",
            "gloss": "anoint",
            "significance": "מָשַׁח (mashach, &lsquo;to rub with oil, to anoint, to consecrate by anointing&rsquo;) is the act that defines 1 Samuel&rsquo;s entire narrative. In 9:16-10:1, Samuel anoints (mashach) Saul as nagid (designated prince) over Israel — the first anointing of a king in Israel&rsquo;s history. In 16:1-13, after Saul&rsquo;s rejection, Samuel anoints David: &lsquo;Take your horn of oil and go&rsquo; (16:1); &lsquo;then Samuel took the horn of oil and anointed him in the midst of his brothers, and the Spirit of YHWH rushed upon David from that day forward&rsquo; (16:13). The nominal form <em>mashiach</em> (מָשִׁיחַ, &lsquo;anointed one&rsquo;) — translated into Greek as <em>Christos</em> (Christ) — enters the NT from this exact background. Hannah&rsquo;s song anticipates it before any king is anointed: &lsquo;He will give strength to his king and exalt the horn of his anointed (מְשִׁיחוֹ)&rsquo; (2:10) — the first use of <em>mashiach</em> in 1 Samuel is a prophetic prayer, not a historical report. The entire book builds toward the anointing of David (ch. 16) as YHWH&rsquo;s true choice — the outwardly overlooked shepherd who becomes the Messianic archetype. The NT&rsquo;s title &ldquo;Jesus Christ&rdquo; (Ἰησοῦς Χριστός) is &ldquo;Jesus the Anointed One&rdquo; — the one toward whom every mashach in 1 Samuel points."
        },
        {
            "code": "H7161",
            "lemma": "קֶרֶן",
            "translit": "qeren",
            "gloss": "horn",
            "significance": "קֶרֶן (qeren, &lsquo;horn — of an animal; by extension, a flask of oil, a cornet; figuratively, a symbol of power and royal dignity&rsquo;) appears in two key 1 Samuel contexts that interpret each other. Hannah&rsquo;s song opens: &lsquo;My heart rejoices in YHWH; my horn (קַרְנִי) is exalted in YHWH&rsquo; (2:1) and closes: &lsquo;He will give strength to his king and exalt the horn (קֶרֶן) of his anointed&rsquo; (2:10) — the qeren of the Messiah is Hannah&rsquo;s ultimate expectation. And in the anointing narratives, YHWH commands Samuel: &lsquo;Fill your horn (קַרְנְךָ) with oil and go; I will send you to Jesse the Bethlehemite, for I have provided for myself a king among his sons&rsquo; (16:1). The horn of oil used to anoint David (16:13) is the enactment of what Hannah&rsquo;s qeren-of-the-Messiah predicted in chapter 2. In ancient Near Eastern iconography, the horn represents power, strength, and royal authority — an exalted horn (rûm-qeren) means YHWH has elevated someone from weakness to power. Psalm 89:24 applies qeren directly to the Davidic covenant: &lsquo;my faithfulness and my steadfast love shall be with him, and in my name shall his horn be exalted.&rsquo; Luke 1:69, in Zechariah&rsquo;s Benedictus, echoes Hannah: &lsquo;he has raised up a horn of salvation (κέρας σωτηρίας) for us in the house of his servant David.&rsquo;"
        },
        {
            "code": "H6419",
            "lemma": "פָּלַל",
            "translit": "pālal",
            "gloss": "pray",
            "significance": "פָּלַל (palal, &lsquo;to intercede, to pray, to judge officially or mentally — from a root meaning to assess or arbitrate&rsquo;) is the verb of Hannah&rsquo;s prayer that opens the entire book. &lsquo;She was deeply distressed and prayed (וַתִּתְפַּלֵּל) to YHWH and wept bitterly&rsquo; (1:10); &lsquo;as she continued praying (מִתְפַּלֶּלֶת) before YHWH, Eli observed her mouth&rsquo; (1:12). The prayer that bridges the Judges period and the monarchy is a barren woman&rsquo;s desperate intercession. The book establishes its theology of prayer here: genuine palal is not formulas but desperation — Hannah &lsquo;poured out my soul (נַפְשִׁי) before YHWH&rsquo; (1:15), and YHWH &lsquo;remembered her&rsquo; (1:19). The noun <em>tefillah</em> (תְּפִלָּה, prayer) derives from this same root and becomes the standard OT word for prayer, especially in the psalms. The book&rsquo;s prayer-theology carries through: Hannah prays and receives Samuel; Samuel &lsquo;does not cease to pray&rsquo; for Israel (12:23); David&rsquo;s psalms later systematize what Hannah enacts. Luke 18:1-8 (the persistent widow) and Luke 1:13 (&lsquo;your prayer has been heard&rsquo; — said to Zechariah about the prayer for a son) are the NT echoes of Hannah&rsquo;s palal. The NT&rsquo;s παράκλητος (paraklete, one who comes alongside to intercede) carries the palal-spirit into the doctrine of the Holy Spirit."
        },
        {
            "code": "H7311",
            "lemma": "רוּם",
            "translit": "rûm",
            "gloss": "exalt",
            "significance": "רוּם (rum, &lsquo;to be high, to rise, to raise up, to exalt — in a wide range of literal and figurative applications&rsquo;) opens 1 Samuel&rsquo;s theological frame through Hannah&rsquo;s song: &lsquo;My heart rejoices in YHWH; my horn is exalted (רָמָה קַרְנִי) in YHWH...the bows of the mighty are broken, but the feeble bind on strength...He raises up (יָרִים) the poor from the dust; he lifts (יָרִים) the needy from the ash heap, to make them sit with princes and inherit a seat of honor. For the pillars of the earth are YHWH&rsquo;s, and on them he has set the world. He will guard the feet of his faithful ones, but the wicked shall be cut off in darkness...He will give strength to his king and exalt (וְיָרֵם) the horn of his anointed&rsquo; (2:1, 4, 8, 10). Hannah&rsquo;s rum is not self-exaltation — it is the recognition that YHWH reverses human expectations of greatness. The barren woman is now fruitful; the mighty are broken; the humble are raised. This inversion is the book&rsquo;s structural argument: David (the youngest, the smallest, the shepherd) is raised above Saul (the tallest, the most impressive, the obvious choice). Hannah&rsquo;s rum-song is the hermeneutical key for reading the whole book. Mary&rsquo;s Magnificat (Luke 1:46-55) is almost word-for-word Hannah&rsquo;s song: &lsquo;he has brought down the mighty from their thrones and exalted (ὕψωσεν) those of humble estate&rsquo; (Luke 1:52) — Jesus&rsquo;s ministry of exalting the lowly is the ultimate rum of which Hannah sang."
        },
        {
            "code": "H7200",
            "lemma": "רָאָה",
            "translit": "rāʾāh",
            "gloss": "see",
            "significance": "רָאָה (raah, &lsquo;to see, to perceive, to discern, to look at — in numerous literal and figurative applications&rsquo;) carries 1 Samuel&rsquo;s most important theological verse: &lsquo;But YHWH said to Samuel, &ldquo;Do not look on his appearance or on the height of his stature, because I have rejected him. For YHWH sees not as man sees (כִּי לֹא אֲשֶׁר יִרְאֶה הָאָדָם): man looks on the outward appearance (לַמַּרְאֶה הָעֵינַיִם), but YHWH looks on the heart (וַיהוָה יִרְאֶה לַלֵּבָב)&rdquo;&rsquo; (16:7). The contrast is structural: human raah evaluates by external visibility (stature, appearance, impressiveness — everything that made Saul seem kingly); divine raah perceives the invisible heart. The entire Saul-David contrast is a raah-problem: Israel saw in Saul what they wanted to see (8:20 — &lsquo;our king may judge us and go out before us and fight our battles&rsquo;); YHWH saw what they could not. The book&rsquo;s narrative invites readers into YHWH&rsquo;s mode of seeing: to evaluate by heart-reality rather than external appearance. The prophets extend this raah-theology: &lsquo;YHWH does not see as man sees&rsquo; (cf. Isa 11:3: the Messianic branch &lsquo;shall not judge by what his eyes see&rsquo;). Paul develops the same principle in 2 Corinthians: &lsquo;we look not to the things that are seen but to the things that are unseen&rsquo; (4:18) — the Pauline raah-hermeneutic owes much to 1 Samuel 16:7."
        },
        {
            "code": "H7592",
            "lemma": "שָׁאַל",
            "translit": "šāʾal",
            "gloss": "ask",
            "significance": "שָׁאַל (shaal, &lsquo;to ask, to inquire, to request, to demand — with a range from simple petition to formal oracle-inquiry&rsquo;) is etymologically present throughout 1 Samuel. Hannah &lsquo;asked (שָׁאַלְתִּי) him from YHWH&rsquo; (1:20) and explains: &lsquo;I have lent (שְׁאִלְתִּיהוּ) him to YHWH&rsquo; (1:28) — Samuel&rsquo;s name puns on the act of asking. Israel &lsquo;asked&rsquo; for a king: the elders said &lsquo;give us a king (שִׂים לָנוּ מֶלֶךְ)&rsquo; and Samuel &lsquo;heard all the words of the people who said this&rsquo; (8:10) — their asking is the theological crisis. Saul&rsquo;s name (שָׁאוּל, &lsquo;asked for&rsquo;) marks him as the king Israel requested. Saul &lsquo;inquired of YHWH&rsquo; (14:37; 28:6) but YHWH did not answer him. Saul&rsquo;s final act of shaal is the darkest: he &lsquo;inquired of a medium&rsquo; (28:7-8) when YHWH would not answer — the ultimate inversion of the book&rsquo;s opening palal. The shaal-pattern reveals the quality of the asker: who you ask reveals who your god is. Hannah asked YHWH for a son and received Samuel; Israel asked for a king and received Saul; Saul asked the dead for guidance and received a death sentence. James 4:3 (&lsquo;you ask and do not receive, because you ask wrongly&rsquo;) diagnoses the Saul-shaal precisely: the manner, motive, and object of asking determines whether YHWH answers."
        },
        {
            "code": "H7462",
            "lemma": "רָעָה",
            "translit": "rāʿāh",
            "gloss": "shepherd",
            "significance": "רָעָה (raah, &lsquo;to tend a flock, to pasture, to shepherd — note: different root and code from H7200 raah, &ldquo;to see&rdquo;&rsquo;) is David&rsquo;s vocation before he becomes king — and the qualification that most matters. When Jesse&rsquo;s sons are presented to Samuel, David is absent: &lsquo;Jesse answered, &ldquo;There remains yet the youngest, but behold, he is keeping the sheep (רֹעֶה בַּצֹּאן)&rdquo;&rsquo; (16:11). David&rsquo;s first credential before Saul is his experience as a shepherd: &lsquo;Your servant used to keep sheep for his father. And when there came a lion, or a bear, and took a lamb from the flock, I went after him and struck him and delivered it out of his mouth&rsquo; (17:34-35). The pastoral competence is the royal qualification — the one who protects sheep can protect Israel. This shepherd-king connection is not incidental: 2 Samuel 5:2 records YHWH&rsquo;s charge to David, &lsquo;you shall be shepherd (רֹעֶה) of my people Israel.&rsquo; Ezekiel 34&rsquo;s long indictment of the bad shepherds (kings who scatter the flock) ends: &lsquo;I will set up over them one shepherd, my servant David, and he shall feed them&rsquo; (34:23). Jesus&rsquo;s &lsquo;I am the good shepherd&rsquo; (John 10:11-14) is the fulfillment of the raah-king trajectory that begins with David keeping his father&rsquo;s sheep in Bethlehem."
        },
        {
            "code": "H2076",
            "lemma": "זָבַח",
            "translit": "zābaḥ",
            "gloss": "sacrifice",
            "significance": "זָבַח (zabach, &lsquo;to slaughter an animal, usually in sacrifice; to offer a sacrificial meal&rsquo;) gives the book its sharpest proverb. When Saul spares the Amalekite animals &lsquo;to sacrifice (לִזְבֹּחַ) to YHWH your God&rsquo; (15:21), Samuel&rsquo;s response is 1 Samuel&rsquo;s most theologically dense statement: &lsquo;Has YHWH as great delight in burnt offerings and sacrifices (זְבָחִים) as in obeying the voice of YHWH? Behold, to obey is better than sacrifice (מִזָּבַח), and to listen than the fat of rams. For rebellion is as the sin of divination, and presumption is as iniquity and idolatry. Because you have rejected the word of YHWH, he has also rejected you from being king&rsquo; (15:22-23). Samuel does not abolish the sacrificial system — he clarifies its purpose. Sacrifice that substitutes for obedience rather than expressing it is the definition of Saul&rsquo;s failure, and the prophets make this point repeatedly (Isa 1:11-17; Hos 6:6: &lsquo;I desire steadfast love and not sacrifice, the knowledge of God rather than burnt offerings&rsquo;). The exact situation was specific: Saul was commanded to destroy all, yet saved the best animals for a zabach. Samuel&rsquo;s response drives to the structural issue: outward religious performance cannot compensate for disobedience to the specific word of YHWH. Jesus twice quotes Hosea 6:6 (&lsquo;I desire mercy, and not sacrifice,&rsquo; Matt 9:13; 12:7) — the zabach-principle runs from 1 Samuel through Hosea to the NT."
        },
        {
            "code": "H1285",
            "lemma": "בְּרִית",
            "translit": "bərît",
            "gloss": "covenant",
            "significance": "בְּרִית (berit, &lsquo;covenant, binding compact — from a root related to cutting, since covenants were ratified by passing between cut animal halves&rsquo;) appears in the defining relationship of 1 Samuel: Jonathan&rsquo;s covenant with David. &lsquo;Then Jonathan made a covenant (בְּרִית) with David, because he loved him as his own soul. And Jonathan stripped himself of the robe that was on him and gave it to David, and his armor, and even his sword and his bow and his belt&rsquo; (18:3-4). Jonathan&rsquo;s stripping of his royal garments is a transfer of dynastic right — he is making David his covenant heir. The berit is ratified again in 20:8 and 23:18. The covenant has a theological dimension: it is sealed &lsquo;before YHWH&rsquo; (23:18) and binds both men&rsquo;s households across generations (20:15-16: &lsquo;do not cut off your steadfast love from my house forever&rsquo;). Jonathan&rsquo;s covenant with David is the inverse of Saul&rsquo;s covenant-breaking with YHWH: Saul cannot keep his obligations because his heart is not in them; Jonathan makes berit with David because love drives him to give up his own dynastic right. The NT word διαθήκη (diatheke, covenant/testament) is the Greek equivalent of berit, and Paul&rsquo;s treatment of the new covenant (2 Cor 3; Gal 3:15-18) stands in the tradition where Jonathan&rsquo;s human berit images the divine covenant of grace."
        },
        {
            "code": "H4467",
            "lemma": "מַמְלָכָה",
            "translit": "mamlākāh",
            "gloss": "kingdom",
            "significance": "מַמְלָכָה (mamlakah, &lsquo;kingdom, dominion, the estate of royal rule — from the root malak, to reign&rsquo;) is the theology of monarchy itself. Israel&rsquo;s request — &lsquo;give us a king to judge us like all the nations&rsquo; (8:5) — and YHWH&rsquo;s response — &lsquo;they have rejected me from being king over them&rsquo; (8:7) — frame the book&rsquo;s ambivalent view of mamlakah. YHWH grants the request and designs a specific king; yet the human mamlakah is always subordinate to divine sovereignty. Samuel&rsquo;s farewell address (12:12-25) articulates the tension: YHWH was their true king; the human king rules conditionally on covenant faithfulness. The word&rsquo;s most dramatic appearance is in Saul&rsquo;s verdict: &lsquo;YHWH has torn the kingdom of Israel (מַמְלְכוּת יִשְׂרָאֵל) from you this day and has given it to a neighbor of yours who is better than you&rsquo; (15:28) — the mamlakah belongs to YHWH to assign and remove. David&rsquo;s rise shows what mamlakah looks like when it is grounded in a heart after YHWH (13:14). The NT&rsquo;s proclamation &lsquo;the kingdom of God is at hand&rsquo; (Mark 1:15) is the announcement that the true mamlakah — which Israel&rsquo;s compromised kingship could only approximate — has arrived in the Son of David who rules not conditionally but by right of perfect covenant faithfulness."
        },
        {
            "code": "H3988",
            "lemma": "מָאַס",
            "translit": "māʾas",
            "gloss": "reject",
            "significance": "מָאַס (maas, &lsquo;to reject, to spurn, to despise, to dissolve — in the Niphal, to be rejected&rsquo;) is the verdict-word of Saul&rsquo;s story. &lsquo;Because you have rejected (מָאַסְתָּ) the word of YHWH, he has also rejected you (וַיִּמְאָסְךָ) from being king&rsquo; (15:23) — the double use in one verse is the book&rsquo;s structural judgment: the human rejection of YHWH&rsquo;s word is immediately answered by divine rejection of the human king. Samuel repeats it: &lsquo;YHWH has rejected you from being king over Israel&rsquo; (15:26). The maas-dynamic is not arbitrary — it is covenant consequence: Saul was given explicit commands (destroy the Amalekites completely, take no plunder) and explicitly disobeyed (kept the best sheep and Agag). The maas verdict interprets the whole first half of the book: why does a talented, Spirit-touched, tall king fail so completely? Because Saul&rsquo;s rejection of YHWH&rsquo;s word is the antecedent to YHWH&rsquo;s rejection of Saul. Samuel&rsquo;s earlier declaration — &lsquo;Has YHWH as great delight in burnt offerings...as in obeying the voice of YHWH?&rsquo; (15:22) — shows that the maas is not about personal dislike but covenant integrity. The NT&rsquo;s &lsquo;I never knew you; depart from me, you workers of lawlessness&rsquo; (Matt 7:23) echoes the structure of Saul&rsquo;s maas — the severing of a relationship that appeared to exist on only one side."
        },
        {
            "code": "H8104",
            "lemma": "שָׁמַר",
            "translit": "šāmar",
            "gloss": "keep",
            "significance": "שָׁמַר (shamar, &lsquo;to hedge about with thorns as protection, to guard, to keep, to observe, to faithfully attend to — a rich cluster of protective vigilance&rsquo;) appears in Samuel&rsquo;s judgment on Saul: &lsquo;You have done foolishly. You have not kept (שָׁמַרְתָּ) the commandment of YHWH your God, which he commanded you...YHWH would have established your kingdom over Israel forever. But now your kingdom shall not continue&rsquo; (13:13-14). The same diagnostic recurs in 15:11 and frames the structural difference between Saul and David. Shamar is the covenant-fidelity word: the one who keeps what is entrusted to them maintains the relationship; the one who does not loses both the trust and its blessings. Saul&rsquo;s failure is not primarily moral failure in the abstract — it is shamar-failure: he did not guard and attend to what was commanded. David&rsquo;s heart-loyalty, by contrast — imperfect as it is, as 2 Samuel shows — is fundamentally shamar-oriented even in crisis: &lsquo;I have kept (שָׁמַרְתִּי) the ways of YHWH and have not wickedly departed from my God&rsquo; (Ps 18:21, David&rsquo;s psalm). The difference between Saul and David is not sinlessness — both sin terribly — but their posture of shamar toward YHWH&rsquo;s word. Jesus&rsquo;s &lsquo;if you love me, you will keep (τηρήσετε) my commandments&rsquo; (John 14:15) and &lsquo;whoever keeps (τηρήσῃ) my word will never see death&rsquo; (John 8:51) are in the same covenant-fidelity tradition of shamar."
        }
    ],

    "language_notes": (
        "<p>Hannah&rsquo;s song (2:1-10) is not a pious preface — it is the book&rsquo;s <strong>interpretive key</strong>, and 1 Samuel cannot be read rightly without reading it first. The song announces the book&rsquo;s central argument in liturgical form: YHWH reverses human expectations (the barren woman bears; the mighty bow is broken; the poor are raised from the ash heap); YHWH sees by different criteria than humans see (the humble are exalted, the proud are brought low); and the whole movement of history tends toward a single point — &lsquo;he will give strength to his king and exalt the horn of his anointed&rsquo; (2:10). This final line is remarkable: there is no king in Israel when Hannah sings it. The word <em>mashiach</em> (anointed one) is spoken prophetically before Saul or David exists. The song is formally comparable to the Egyptian <em>Amarna hymns</em> and to Ugaritic hymn poetry, but its theological content is radically distinctive: YHWH&rsquo;s sovereignty over birth, death, poverty, and power is unqualified. Mary&rsquo;s Magnificat (Luke 1:46-55) quotes and develops Hannah&rsquo;s song so closely — &lsquo;he has brought down the mighty from their thrones and exalted those of humble estate&rsquo; (1:52) — that Luke clearly intends his readers to hear Mary as a second Hannah, and Jesus as the Messiah whose horn Hannah announced.</p>"
        "<p>1 Samuel&rsquo;s primary <strong>literary technique is contrast</strong>: two characters are consistently set against each other to reveal what faithful kingship requires. The paired contrasts cascade through the book: Hannah/Peninnah (fruitful prayer vs. fruitless provocation); Eli/Samuel (complacent priestly household vs. responsive prophetic calling); Saul/David (outward impressiveness vs. inner heart-orientation); Saul&rsquo;s disobedience/David&rsquo;s restraint (Saul kills what should live; David spares what should die — especially in the two opportunities to kill Saul, chs. 24, 26). The contrast is not moralistic — both Saul and David are complex, flawed figures — but theological: what is the heart-posture that YHWH &lsquo;sees&rsquo; (16:7) as qualifying someone for covenant leadership? The contrast technique forces the reader to evaluate character by inner posture rather than external performance, enacting the very raah-shift (16:7) that is the book&rsquo;s key theological claim.</p>"
        "<p>The book&rsquo;s <strong>Spirit-language</strong> tracks the transfer of divine empowerment from Saul to David with precision. &lsquo;The Spirit of YHWH rushed upon Saul&rsquo; (10:10; 11:6) at his anointing and at his first military victory. But in 16:14, immediately after David&rsquo;s anointing: &lsquo;Now the Spirit of YHWH departed from Saul, and a harmful spirit from YHWH tormented him.&rsquo; In the same verse (16:13), &lsquo;the Spirit of YHWH rushed upon David from that day forward.&rsquo; The Spirit&rsquo;s transfer is the theological event of the book&rsquo;s pivot point. The Hebrew verb for the Spirit &lsquo;rushing&rsquo; upon the judges and upon Saul/David is <em>tsalach</em> (צָלַח, &lsquo;to rush upon, to surge&rsquo;) — the same episodic Spirit-language seen in Judges, now applied to kings. The departure of the Spirit from Saul and its permanent resting on David anticipates the NT distinction between the Spirit&rsquo;s episodic OT visits and his permanent Pentecostal indwelling — with David as the OT prototype of one whom the Spirit permanently inhabits for the royal calling.</p>"
        "<p>The Hebrew name <strong>שְׁמוּאֵל (Samuel)</strong> has two proposed etymologies: &lsquo;his name is El&rsquo; (šem + El) or &lsquo;heard of God&rsquo; (šamu + El, related to the root שָׁמַע, hear). The book itself exploits a third reading: in 1:20 Hannah says &lsquo;I asked him (שְׁאֵלְתִּיו) from YHWH,&rsquo; using the root שָׁאַל (shaal, to ask) — the same root as Saul&rsquo;s name (שָׁאוּל, &lsquo;asked for&rsquo;). This pun is deliberate: both Samuel and Saul are &lsquo;asked for&rsquo; — but Hannah asked YHWH for Samuel, while Israel asked Samuel for Saul. The etymological layering reveals the book&rsquo;s narrative irony: Saul (the &lsquo;asked-for king&rsquo;) is replaced by David (the &lsquo;un-asked-for choice&rsquo; of YHWH), while Samuel (the &lsquo;asked-for prophet&rsquo;) is the instrument of both transitions. Hebrew narrative frequently embeds theological interpretation in personal names, and 1 Samuel makes this technique central to its theology of divine sovereignty and human petition.</p>"
    ),

    "reception": (
        "<p><strong>Hannah&rsquo;s song and the Magnificat:</strong> The most important NT reception of 1 Samuel is Luke&rsquo;s deliberate presentation of Mary&rsquo;s Magnificat (1:46-55) as a second Hannah&rsquo;s song. The parallel is structural: a barren/oppressed woman receives a miraculous son through divine intervention; she sings of God&rsquo;s reversal of the mighty and lowly; her son becomes the pivotal figure in Israel&rsquo;s covenant history. Patristic writers (Origen, Ambrose, Chrysostom) consistently read Hannah as a type of Mary and Samuel as a type of Christ — both set apart from birth, both prophets who bridge eras, both offered back to YHWH at the temple/tabernacle. Augustine&rsquo;s <em>City of God</em> (XVII.4) read Hannah&rsquo;s song as a prophecy of Christ&rsquo;s coming kingdom, interpreting &lsquo;the LORD will judge the ends of the earth&rsquo; (2:10) as an explicit Messianic prophecy.</p>"
        "<p><strong>David as the central OT Christ-type:</strong> In patristic and Reformation exegesis, David is the OT figure most extensively read as a type of Christ — not because he is morally perfect (he is not) but because of his structural role: anointed shepherd-king, opposed by enemies, promised an eternal throne (2 Sam 7), who rules in the Spirit&rsquo;s power. Justin Martyr (<em>Dialogue with Trypho</em>, ch. 100-106) develops David as prophet-king type; Chrysostom&rsquo;s homilies on the psalms (written from David&rsquo;s perspective) treat them as Christ&rsquo;s voice. Calvin&rsquo;s <em>Institutes</em> (II.6.2) makes David the primary exemplar of how the OT covenant was always about the Mediator-King. The modern typological tradition (Clowney, Goldsworthy, Graeme Goldsworthy) sees David as the most developed OT type of the messianic office.</p>"
        "<p><strong>Samuel and the threefold office:</strong> Calvin&rsquo;s doctrine of Christ&rsquo;s threefold office as Prophet, Priest, and King (<em>munus triplex</em>) is partially grounded in Samuel&rsquo;s unique historical role as judge-prophet-priest in one person (ch. 7: he judges Israel; ch. 7: he offers sacrifice; ch. 3: he receives prophetic vision). Justin Martyr and Eusebius noted that Samuel anoints both Saul and David — the act that most clearly prefigures the Messianic anointing. Modern scholarship has examined the Deuteronomistic framing of Samuel (from the perspective of Dtr History), the historical reliability of the ark narratives (chs. 4-6), and the social function of the monarchy transition from tribal confederacy to state-level government.</p>"
    ),

    "reading_guide": (
        "<p>Read Hannah&rsquo;s song (2:1-10) before you read anything else in 1 Samuel — it is the book&rsquo;s theological preface. Every contrast in the narrative (Saul/David, the mighty/the lowly, the rejected/the chosen) is announced there. The genealogy at the end of Ruth (4:17-22) sets the stage; Hannah&rsquo;s song announces the theme; and everything in the book between the opening prayer and the closing defeat of Saul is the working out of what Hannah sang before any king existed.</p>"
        "<p>Read Saul and David in parallel, not in sequence. The book spends fourteen chapters on Saul (8-31) and introduces David in ch. 16 while Saul is still reigning — the two stories run simultaneously. Track what each man does when he is disobeyed, when he is threatened, when he sincerely prays, when he faces God&rsquo;s silence. The key diagnostic scene is 1 Samuel 24 and 26: David twice has Saul&rsquo;s life in his hand and twice refuses to &lsquo;put out my hand against the LORD&rsquo;s anointed.&rsquo; This is what the heart that God sees (16:7) looks like in practice.</p>"
        "<p>The most common misreading of 1 Samuel is to read it as a straightforward celebration of David. David is the right king — but the book is honest about his flaws (18:12 hints at political manipulation; 21:10-15 shows cowardice; 27:1-12 shows compromise). What distinguishes David from Saul is not sinlessness but the direction of his heart when he fails: Saul justifies himself (13:12: &lsquo;so I forced myself and offered the burnt offering&rsquo;; 15:24: &lsquo;I feared the people and obeyed their voice&rsquo;); David will, in 2 Samuel 12, simply say &lsquo;I have sinned against YHWH.&rsquo; That difference is the heart YHWH looks for.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('1samuel')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('1samuel', merged)

main()
