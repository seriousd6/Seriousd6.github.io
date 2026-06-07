"""
Book Study Data — Hosea
book_id: hosea
lang: hebrew

Run: python3 scripts/build-book-study-hosea.py

Notes:
- Author group: Minor in author-freq-hebrew.json (shared across the 12 Minor Prophets);
  peaks are mostly generic function words — vocabulary selected from Hosea's specific theology
- All Hebrew translit fields blank in glossary — supplied manually
- Many obvious Hosea codes already used: H2617 hesed, H1847 da'at, H7725 shuv,
  H2181 zanah (harlotry), H1285 brit (covenant), H3045 yada, H7356 rachamim
- H7355 racham (compassion) is distinct from H7356 rachamim (compassions, plural noun)
  and is available; it's the verb form used in Lo-Ruhamah's name
- H1167 ba'al: doubles as the Canaanite deity name AND the Hebrew word for
  owner/husband — Hosea 2:16 exploits this deliberately and untranslatably
- H3384 yarah: root of Torah (instruction/law); priests fail to yarah in Hos 4:6
- Hosea is quoted 6 times in the NT, more than any other Minor Prophet
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
    "bookId": "hosea",

    "key_vocabulary": [
        {
            "code": "H7355",
            "lemma": "רָחַם",
            "translit": "rāḥam",
            "gloss": "have compassion",
            "significance": "רָחַם (rāḥam, &lsquo;to fondle; by implication, to love, especially to compassionate&rsquo;) becomes the theological name of Hosea&rsquo;s second child in its negated form: <strong>Lo-Ruhamah</strong> (לֹא רֻחָמָה — &ldquo;not-pitied, not-shown-compassion&rdquo;). Hosea 1:6: &ldquo;Call her name Lo-Ruhamah, for I will no more have mercy (racham) on the house of Israel, to forgive them at all.&rdquo; The name announces the suspension of divine compassion — the covenant love that defined the relationship is being withheld as judgment. But the book&rsquo;s arc reverses this: Hosea 2:23: &ldquo;I will have mercy (ve-riḥamti) on No Mercy (Lo-Ruhamah).&rdquo; The reversal of Lo-Ruhamah is the reversal of judgment itself. Paul quotes 2:23 in Romans 9:25 (&ldquo;her who was not beloved I will call &lsquo;beloved&rsquo;&rdquo;) and 1:10 in Romans 9:26 to justify the inclusion of Gentiles in the covenant — those who had never been within the covenant at all are now being shown the racham that Israel forfeited. The NT&rsquo;s &ldquo;God is rich in mercy&rdquo; (Eph 2:4 — <em>plousios en eleei</em>) is the Greek equivalent of Hosea&rsquo;s racham-restoration: the Lo-Ruhamah condition reversed at infinite cost."
        },
        {
            "code": "H5971",
            "lemma": "עַם",
            "translit": "ʿam",
            "gloss": "people",
            "significance": "עַם (ʿam, &lsquo;a people as a congregated unit; specifically, a tribe; troops&rsquo;) becomes the theological name of Hosea&rsquo;s third child in negative form: <strong>Lo-Ammi</strong> (לֹא עַמִּי — &ldquo;not my people&rdquo;). Hosea 1:9: &ldquo;Call his name Lo-Ammi, for you are not my people (lo ammi attem), and I am not your God.&rdquo; The Hebrew at the end is extraordinary: &ldquo;I am not your ʾehyeh&rdquo; — YHWH uses the word from Exodus 3:14 (&ldquo;I AM WHO I AM,&rdquo; ʾehyeh ʾašer ʾehyeh) and says: I am not your ʾehyeh. The divine self-disclosure at the burning bush is being reversed — the covenant formula &ldquo;I am the LORD your God&rdquo; is suspended. But Hosea 2:23 reverses it again: &ldquo;I will say to Not My People (Lo-Ammi), &lsquo;You are my people (ammi).&rsquo;&rdquo; Paul applies this double reversal in Romans 9:25-26 to the Gentiles — those who were never ʿam at all are being included in the covenant. The Lo-Ammi → Ammi arc is the OT&rsquo;s most concentrated expression of what the NT calls grace: those outside the covenant formula are declared inside by the God who redefines inclusion on the basis of mercy rather than birth."
        },
        {
            "code": "H1167",
            "lemma": "בַּעַל",
            "translit": "baʿal",
            "gloss": "master",
            "significance": "בַּעַל (baʿal, &lsquo;a master; hence a husband or owner&rsquo;) is the most charged word in Hosea because it carries two meanings simultaneously — and Hosea exploits both deliberately. The word means &ldquo;owner/master/husband&rdquo; in ordinary Hebrew, but <em>Baal</em> is also the name of the Canaanite fertility deity Israel was worshiping. Hosea 2:16-17 exploits this double meaning: &ldquo;And in that day, declares the LORD, you will call me &lsquo;My Husband&rsquo; (ishi) and no longer will you call me &lsquo;My Ba&rsquo;al&rsquo; (ba&rsquo;ali). For I will remove the names of the Ba&rsquo;als from her mouth.&rdquo; The shift from ba&rsquo;ali to ishi (my man/husband — from ish, H376) is more than a name change: ba&rsquo;al implies ownership and power-over; ish implies intimate partnership. Israel has been calling YHWH ba&rsquo;al — treating him as a fertility lord to be manipulated by cult performance — when he wants to be known as ish, a covenant husband to be known intimately. The confusion between YHWH and Baal was not simply idolatry but a category error about what kind of God YHWH is and what kind of relationship he seeks. The NT&rsquo;s bridal covenant (Eph 5:25-32; Rev 19:7-9) fulfills the ishi-promise: the relationship is not legal obligation but intimate covenant love."
        },
        {
            "code": "H6588",
            "lemma": "פֶּשַׁע",
            "translit": "pɛšaʿ",
            "gloss": "transgression",
            "significance": "פֶּשַׁע (pɛšaʿ, &lsquo;a revolt — national, moral, or religious&rsquo;) is the strongest of the Hebrew sin-words — not accidental failure but deliberate rebellion against a known authority. Hosea 7:13: &ldquo;Woe to them, for they have strayed from me! Destruction to them, for they have rebelled (pash&rsquo;u) against me!&rdquo; Hosea 8:1: &ldquo;they have transgressed (pash&rsquo;u) my covenant and rebelled against my law.&rdquo; Hosea 14:9: &ldquo;the ways of the LORD are right, and the upright walk in them, but transgressors (posh&rsquo;im) stumble in them.&rdquo; The word pɛšaʿ carries the legal register of treaty violation — in the ancient Near East, pesha was the word for defection from a suzerain, for breaking the terms of a covenant with a great king. Israel&rsquo;s covenant with YHWH is not merely a religious relationship but a treaty obligation; pesha is treaty-breach. The same word appears in Isaiah 53:5 (&ldquo;he was pierced for our transgressions&rdquo; — mĕpōšāʿênû) — the Servant specifically bears Israel&rsquo;s covenant-rebellion. The atonement addresses not merely moral failure but the legal reality of pesha: deliberate, covenant-violating revolt against the God who redeemed Israel from Egypt."
        },
        {
            "code": "H3384",
            "lemma": "יָרָה",
            "translit": "yārāh",
            "gloss": "teach",
            "significance": "יָרָה (yārāh, &lsquo;properly, to flow as water; to rain; to lay or throw; figuratively, to point out, to teach&rsquo;) is the root from which <strong>Torah</strong> (תּוֹרָה — instruction, law) is derived. The verb means fundamentally &ldquo;to point in a direction, to instruct.&rdquo; Hosea 4:6 is the hinge verse of the book&rsquo;s indictment: &ldquo;My people are destroyed for lack of knowledge (da&rsquo;at); because you have rejected knowledge, I reject you from being a priest to me. And since you have forgotten the Torah (torat) of your God, I also will forget your children.&rdquo; The priests&rsquo; failure in Hosea 4 is specifically a yarah-failure — they have not taught (yorah) the people the knowledge of God. Hosea 4:6 is remarkable: Israel is not destroyed by military power or divine caprice but by <em>lack of instruction</em>. The solution to covenant unfaithfulness is teaching — yarah — which creates da&rsquo;at elohim (knowledge of God). The NT&rsquo;s Great Commission (&ldquo;teaching them to observe all that I have commanded you&rdquo; — Matt 28:20 — <em>didaskontes</em>) places the post-resurrection community in the same yarah-tradition: faithful instruction in God&rsquo;s ways is not supplementary to mission but constitutive of it."
        },
        {
            "code": "H376",
            "lemma": "אִישׁ",
            "translit": "ʾîš",
            "gloss": "husband",
            "significance": "אִישׁ (ʾîš, &lsquo;a man as an individual or a male person&rsquo;) is the word in Hosea 2:16&rsquo;s pivotal promise: &ldquo;you will call me <em>ishi</em> (my husband) and no longer will you call me <em>ba&rsquo;ali</em> (my master).&rdquo; The suffix -<em>i</em> makes ish possessive and intimate: <em>ishi</em> is literally &ldquo;my man&rdquo; — the wife&rsquo;s intimate address to a husband she knows, not a lord she obeys. The contrast between ishi and ba&rsquo;ali is the contrast between covenant relationship and power-over relationship, between knowing and serving. The promise continues in 2:19-20: &ldquo;I will betroth you to me forever; I will betroth you to me in righteousness and in justice, in steadfast love (hesed) and in mercy (rachamim). I will betroth you to me in faithfulness (emunah). And you shall know (yādaʿt) the LORD.&rdquo; The goal of the ishi-relationship is knowing (da&rsquo;at) — the intimate covenant knowledge that is Hosea&rsquo;s central concern. The three-fold betrothal formula in 2:19-20 is what the new-covenant relationship looks like: not legal compliance (ba&rsquo;al-mode) but knowing YHWH as ish. The NT&rsquo;s &ldquo;husband of one wife&rdquo; (1 Tim 3:2) and the church as Christ&rsquo;s bride (Eph 5:25-32; Rev 19:7) develop this Hosean ishi-theology."
        },
        {
            "code": "H2919",
            "lemma": "טַל",
            "translit": "ṭal",
            "gloss": "dew",
            "significance": "טַל (ṭal, &lsquo;dew, as covering vegetation&rsquo;) appears twice in Hosea in opposite senses that together define the book&rsquo;s theological arc. Hosea 6:4 (judgment): &ldquo;Your love (hesed) is like a morning cloud and like the dew (ṭal) that goes away early.&rdquo; The dew describes Israel&rsquo;s love for YHWH — real at dawn, evaporated before mid-morning. Israel&rsquo;s repentance in 6:1-3 (&ldquo;let us return to the LORD&rdquo;) sounded heartfelt, but YHWH evaluates it as ṭal-thin: real for a moment but without substance. Hosea 14:5 (restoration): &ldquo;I will be like the dew (ṭal) to Israel; he shall blossom like the lily; he shall take root like the trees of Lebanon.&rdquo; In the restoration oracle, the dew shifts from characterizing Israel&rsquo;s transient love to characterizing God&rsquo;s faithful, life-giving presence. What Israel&rsquo;s love was supposed to be — the gentle, life-sustaining moisture that covers the land at dawn — God&rsquo;s love will actually be. The ṭal-inversion is Hosea&rsquo;s gospel in concentrated form: the quality Israel promised but could not sustain, God provides from his own inexhaustible faithfulness. The NT&rsquo;s &ldquo;rivers of living water&rdquo; (John 7:38) fulfills the ṭal-promise: the Spirit as the constant life-giving moisture that Israel&rsquo;s love could not sustain."
        },
        {
            "code": "H6168",
            "lemma": "עָרָה",
            "translit": "ʿārāh",
            "gloss": "lay bare",
            "significance": "עָרָה (ʿārāh, &lsquo;to be bare; causatively, to make bare, empty, pour out, demolish&rsquo;) is the verb for the shameful exposure that YHWH threatens against Israel-as-adulterous-wife. Hosea 2:3: &ldquo;lest I strip her naked (ʾaʿarenāh) and expose her as in the day she was born, and make her like a wilderness, and make her like a parched land, and kill her with thirst.&rdquo; The imagery is of a covenant lawsuit: an adulterous wife publicly exposed before the legal assembly, returned to the condition she was in before the marriage — helpless, dependent, naked. The threat of ʿārāh is the activation of covenant curses (Deut 28) applied through the marriage-covenant framework: unfaithfulness means forfeiture of everything the covenant provided. But arah-exposure is also the precondition for restoration in Hosea&rsquo;s logic: the stripping that returns Israel to the wilderness (2:3) leads to the wilderness betrothal (2:14-15: &ldquo;I will allure her and bring her into the wilderness and speak tenderly to her&rdquo;). The desolation created by the ʿārāh is the space in which the new covenant is offered. The NT&rsquo;s &ldquo;nothing is hidden that will not be made manifest&rdquo; (Luke 8:17) and the atonement as &ldquo;covering&rdquo; (Jas 5:20: &ldquo;love covers a multitude of sins&rdquo;) both inhabit the arah-logic: judgment exposes; grace covers."
        },
        {
            "code": "H6050",
            "lemma": "עֲנַן",
            "translit": "ʿānan",
            "gloss": "cloud",
            "significance": "עֲנַן (ʿānan, &lsquo;a cloud as covering the sky; the nimbus or thunder-cloud&rsquo;) appears in Hosea 6:4 as the first term in a two-image comparison of Israel&rsquo;s transient repentance: &ldquo;your love (hesed) is like a morning cloud (ʿănan bōqer), and like the dew that goes away early.&rdquo; The cloud and the dew describe Israel&rsquo;s repentance-speech in 6:1-3 (&ldquo;let us return... he will revive us... he will come to us as the showers&rdquo;): real for a moment, then burned off by the day&rsquo;s heat. The cloud-image is theologically ironic: clouds in the OT are the primary sign of divine presence (the pillar of cloud in Exod 13:21; the cloud of glory filling the tabernacle in Exod 40:34-38; the cloud on Sinai in Exod 19:9). Israel&rsquo;s love is like what a cloud is supposed to be a sign of — the divine presence — but without the substance. It promises what it cannot deliver. Hosea 13:3 presses the image further: &ldquo;Therefore they shall be like the morning mist or like the dew that goes early away, like the chaff that swirls from the threshing floor or like smoke from a window&rdquo; — now Israel itself becomes the vanishing cloud. What was their love metaphor becomes their doom metaphor. The NT&rsquo;s warning against a faith that is enthusiasm without root (Matt 13:20-21 — the seed on rocky ground) inhabits the ʿānan-critique."
        },
        {
            "code": "H669",
            "lemma": "אֶפְרַיִם",
            "translit": "ʾɛfrayim",
            "gloss": "Ephraim",
            "significance": "אֶפְרַיִם (ʾɛfrayim, &lsquo;Ephraim, son of Joseph; the tribe and its territory&rsquo;) becomes in Hosea the standard name for the entire northern kingdom of Israel — appearing approximately 37 times, making Hosea the primary biblical source for this usage. Hosea uses &ldquo;Ephraim&rdquo; instead of &ldquo;Israel&rdquo; when specifying the northern ten tribes whose capital lay in Ephraim&rsquo;s tribal territory. The name carries enormous emotional weight in the book. Hosea 11:3: &ldquo;Yet it was I who taught Ephraim to walk; I took them up by their arms.&rdquo; Hosea 11:8: &ldquo;How can I give you up, Ephraim? How can I hand you over, Israel? How can I make you like Admah? How can I treat you like Zeboiim? My heart recoils within me; my compassion grows warm and tender.&rdquo; This is arguably the most emotionally raw expression of divine grief in the OT — YHWH arguing with himself about whether he can bear to execute the judgment he has announced. Chapter 11 complements the marriage passages of chapters 1–3 by introducing a second metaphor: not husband and wife but father and child. Ephraim is the beloved son who has strayed, and the Father cannot bear to let him go. Jesus&rsquo;s parable of the prodigal son (Luke 15:11-32) inhabits this Hosean father-and-Ephraim dynamic — the father running toward the returning son is YHWH&rsquo;s heart for Ephraim enacted."
        },
        {
            "code": "H3157",
            "lemma": "יִזְרְעֵאל",
            "translit": "yizrĕʿēl",
            "gloss": "Jezreel",
            "significance": "יִזְרְעֵאל (yizrĕʿēl, &lsquo;Jizreel — two places in Palestine and two Israelites&rsquo;) is the name of Hosea&rsquo;s first child, a name that works on multiple levels simultaneously. Hosea 1:4-5: &ldquo;Call his name Jezreel, for in just a little while I will punish the house of Jehu for the blood of Jezreel, and I will put an end to the kingdom of the house of Israel.&rdquo; Jezreel (the valley) was where Jehu massacred Ahab&rsquo;s dynasty (2 Kgs 9–10) — naming the child Jezreel announces that the current dynasty will end as Ahab&rsquo;s did, on the same soil. But the name Jezreel means both &ldquo;God scatters&rdquo; (yizraʿ-el, with the root zara&rsquo; in the &ldquo;scatter&rdquo; sense) and &ldquo;God sows&rdquo; (with the same root in the &ldquo;plant seed&rdquo; sense). Hosea 2:22-23 reclaims the name in reversal: &ldquo;and they shall answer Jezreel; and I will sow her (ûzĕraʿtîha) for myself in the land.&rdquo; The same root that names the judgment (God-scatters) names the restoration (God-sows-new-life). The single name Jezreel holds both curse and blessing — the seed scattered is the seed planted. The NT&rsquo;s death-and-resurrection-as-sowing (John 12:24: &ldquo;unless a grain of wheat falls into the earth and dies, it remains alone&rdquo;; 1 Cor 15:36-44) inhabits this Jezreel-theology: God&rsquo;s scattering is the precondition for God&rsquo;s harvest."
        },
        {
            "code": "H4196",
            "lemma": "מִזְבֵּחַ",
            "translit": "mizbēaḥ",
            "gloss": "altar",
            "significance": "מִזְבֵּחַ (mizbēaḥ, &lsquo;an altar, as the place of slaughter or sacrifice&rsquo; — from zabach, to sacrifice) appears in Hosea as the target of the book&rsquo;s sharpest critique of Israel&rsquo;s religious system. Hosea 8:11: &ldquo;Because Ephraim has multiplied altars for sinning, they have become to him altars for sinning.&rdquo; The altars built to deal with sin have themselves become instruments of further sin — the sacrificial system co-opted into the same covenant-unfaithfulness it was meant to address. Hosea 10:1-2: &ldquo;The more his fruit increased, the more altars he built... now they must bear their guilt. The LORD will break down their altars and destroy their pillars.&rdquo; The proliferation of mizbēaḥ is evidence of false religion: Israel multiplies the means of approach to God while remaining estranged from God. The critique culminates in Hosea 6:6 — &ldquo;I desire steadfast love (hesed) and not sacrifice, the knowledge of God rather than burnt offerings&rdquo; — the verse Jesus quotes twice (Matt 9:13; 12:7) when defending mercy over ritual. The mizbēaḥ-critique is not anti-worship but anti-ritualism: sacrifice without da&rsquo;at and hesed creates the illusion of covenant faithfulness where none exists, which is worse than open unfaithfulness because it deceives the worshiper. The NT&rsquo;s &ldquo;present your bodies as a living sacrifice&rdquo; (Rom 12:1 — <em>thysian zōsan</em>) redefines the mizbēaḥ itself in personal and covenantal terms."
        }
    ],

    "language_notes": (
        "<p>Hosea&rsquo;s prophetic medium is the <strong>marriage allegory</strong> — not as illustration but as lived enactment. The grammar of Hosea&rsquo;s allegory is unusual in that it never explains itself: the book begins in the third person (&ldquo;Go, take to yourself a wife of harlotry&rdquo; — Hos 1:2), shifts to YHWH speaking in the first person about his relationship with Israel (ch. 2), then narrates a third-person account of Hosea purchasing his wife again (ch. 3), then launches into oracles that presuppose the allegory without restating it (chs. 4–14). The reader is expected to hold the marriage frame through all fourteen chapters without prompting. This grammatical structure creates intimacy: YHWH does not say &ldquo;Israel is like an adulterous wife&rdquo; — he speaks as a husband directly addressing his wife. The effect is that the accusation and the longing are personal, not forensic. Hebrew&rsquo;s direct-address second person (&ldquo;you, Israel&rdquo; — not &ldquo;they&rdquo;) keeps the reader uncomfortably inside the accused community. The covenant lawsuit genre (rîb — legal dispute) underlies much of Hosea 4, but Hosea consistently pushes past the legal register toward the personal: the God who sues his covenant people is the same God who cannot bear to give them up (11:8).</p>"
        "<p>The <strong>children&rsquo;s names</strong> in chapters 1–2 function as prophetic speech-acts — words that perform what they name. Jezreel (yizrĕʿēl — God scatters/sows), Lo-Ruhamah (not-pitied), and Lo-Ammi (not my people) are not merely names but oracular announcements embedded in flesh. Each child&rsquo;s birth is a new prophetic word, and each name is a compressed oracle. The Hebrew play between &ldquo;God scatters&rdquo; and &ldquo;God sows&rdquo; (both from zāraʿ) in Jezreel&rsquo;s name, the emotional weight of a child named &ldquo;not-loved,&rdquo; and the covenant-reversing shock of &ldquo;not my people&rdquo; are all carried in the Hebrew phonology in a way translations cannot preserve. Reading these names in Hebrew — hearing the negation particle lōʾ (not) attached to racham and ammi — makes the suspension of covenant love audible. Hosea 2:21-23 reverses each in kind — Jezreel re-seeded, Lo-Ruhamah given racham, Lo-Ammi called ammi: the negation removed, the covenant formula restored.</p>"
        "<p>Hosea 11 contains the most remarkable <strong>expression of divine interiority</strong> in the prophets. Hosea 11:8-9: &ldquo;How can I give you up, Ephraim? How can I hand you over, Israel? How can I make you like Admah? How can I treat you like Zeboiim? My heart recoils within me (nĕhpak libbî); my compassion grows warm and tender (nikmerû niḥûmāy).&rdquo; The Hebrew verbs are extraordinary: <em>nĕhpak</em> (turned over, overturned) suggests a physical revolution within the chest — the heart physically turning. <em>Niḥûmāy</em> (my compassions) comes from nāḥam (to comfort, to have compassion — also the root of &ldquo;Nahum&rdquo;); <em>nikmerû</em> means kindled to the point of glowing — the compassion is not mild but burning. The passage ends: &ldquo;I will not execute my burning anger; I will not again destroy Ephraim; for I am God and not a man, the Holy One in your midst.&rdquo; The restraint of divine judgment is grounded in divine nature (ʾEl anoki — I am God): precisely because YHWH is not human, he does not respond to rejection with retribution alone. The NT&rsquo;s &ldquo;God so loved the world&rdquo; (John 3:16) and the prodigal&rsquo;s father running before the son arrives (Luke 15:20) inhabit this Hosean divine interiority.</p>"
        "<p>Hosea&rsquo;s structural signature is the <strong>judgment-to-hope reversal</strong> — Hebrew&rsquo;s adversative particles pivot abruptly from accusation to promise. The key particle is <em>lāken</em> (therefore) which in the prophets usually introduces judgment but in Hosea often pivots to restoration. Hosea 2:14: &ldquo;<em>lāken</em> (therefore) behold, I will allure her and bring her into the wilderness and speak tenderly to her.&rdquo; The &ldquo;therefore&rdquo; that should introduce punishment introduces courtship instead — YHWH&rsquo;s response to Israel&rsquo;s failure is not simply abandonment but a new wilderness-betrothal. Chapter 14 is Hosea&rsquo;s fullest restoration oracle: God&rsquo;s answer to the book&rsquo;s call for return (14:1-3) unfolds in botanical imagery — &ldquo;I will be like the dew to Israel; he shall blossom like the lily; he shall take root like the trees of Lebanon&rdquo; (14:5). The botanical vocabulary of restoration (bloom, root, branch, fragrance, grain, vine) reverses the agricultural devastation of the judgment oracles — every promised growth is the specific undoing of a threatened destruction.</p>"
    ),

    "reception": (
        "<p><strong>Patristic and early church:</strong> Hosea is the most-quoted Minor Prophet in the NT (quoted six times), and the patristic tradition followed this lead. Matthew 2:15 applies Hosea 11:1 (&ldquo;Out of Egypt I called my son&rdquo;) to Jesus&rsquo;s return from Egypt — establishing a typological method where Israel&rsquo;s historical experience prefigures the Messiah&rsquo;s. Origen read the marriage allegory allegorically as the soul&rsquo;s unfaithfulness and God&rsquo;s pursuing love, producing one of the richest early commentaries on spiritual formation. Jerome wrote a commentary that combined literal-historical exegesis with extended allegorical application. The patristic tradition consistently identified Hosea as the prophet of divine love: Augustine quoted Hosea 6:6 (&ldquo;I desire mercy and not sacrifice&rdquo;) in his reflections on the relationship between charity and liturgical obligation.</p>"
        "<p><strong>Reformation and covenant theology:</strong> Martin Luther regarded Hosea as one of the most important OT books for understanding the gospel — the pattern of law (accusation, judgment) followed by gospel (love, restoration) is enacted in Hosea&rsquo;s marriage more dramatically than anywhere else in Scripture. John Calvin&rsquo;s commentary on Hosea focused on the covenant-framework: the marriage is the covenant, the adultery is covenant-breach, and the redemption of Gomer (ch. 3) is the typological promise of Christ&rsquo;s redemption of his faithless covenant people. The Reformation&rsquo;s emphasis on unilateral divine grace found strong support in Hosea&rsquo;s portrayal of YHWH pursuing a wife who could not and did not respond adequately.</p>"
        "<p><strong>Modern scholarship and interpretation:</strong> The debate about the nature of Hosea&rsquo;s marriage — was Gomer already unfaithful when he married her (Hos 1:2: &ldquo;take a wife of whoredom&rdquo;), or did she become so after marriage, or is the marriage entirely visionary? — has generated substantial critical discussion (Francis Andersen and David Noel Freedman&rsquo;s AB commentary, 1980, provides the fullest treatment). Feminist scholars (Phyllis Trible, Renita Weems) have raised important ethical questions about the metaphor&rsquo;s gender dynamics — the adulterous-wife imagery can be read as victim-blaming. Weems&rsquo;s <em>Battered Love</em> (1995) argues that Hosea&rsquo;s metaphor both illuminates divine love and distorts the human relationship it borrows from. The NT&rsquo;s six quotations from Hosea (Matt 2:15; 9:13; 12:7; Rom 9:25-26; 1 Cor 15:55; 1 Pet 2:10) remain the primary measure of the book&rsquo;s canonical significance.</p>"
    ),

    "reading_guide": (
        "<p><strong>Read chapters 1–3 first, slowly, as the hermeneutical key to everything that follows.</strong> The marriage narrative establishes the metaphor that chapters 4–14 presuppose without re-explaining. Without the marriage frame, chapter 4&rsquo;s accusation reads as social critique; with it, as a betrayed husband describing his wife&rsquo;s behavior — Hosea is not a social critic but a prophet of broken covenant love. Chapter 3&rsquo;s repurchase — buying back what was already covenantally his — is the book&rsquo;s most compressed theological statement.</p>"
        "<p><strong>The emotional register of the book requires slow reading.</strong> Hosea 11:8 (&ldquo;How can I give you up, Ephraim?&rdquo;) is YHWH in grief — divine emotion not resolved into neat formula. Read chapter 11 aloud; the architecture (threat → grief → restraint → mercy) can be felt even in translation through pace and pause. The most common misreading abstracts the theology from the emotional texture — doctrine about covenant rather than the voice of a God who cannot bear to let go.</p>"
        "<p><strong>Track the reversal pattern.</strong> Every accusation in chapters 4–10 has a corresponding restoration — often the next chapter: chapter 9&rsquo;s judgment gives way to chapter 11&rsquo;s parental love; chapter 13&rsquo;s death-oracles (Hos 13:14, quoted by Paul in 1 Cor 15:55 as a victory cry) give way to chapter 14&rsquo;s restoration. Judgment and restoration are not sequential but simultaneous aspects of YHWH&rsquo;s response to failure — the anger and the love coexist, which is why the book can sound contradictory. That contradiction is the book&rsquo;s deepest theological truth.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('hosea')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('hosea', merged)

main()
