"""
Book Study Data — Exodus
book_id: exodus
lang: hebrew

Run: python3 scripts/build-book-study-exodus.py

Notes:
- Author group: Moses (peak in author-freq-hebrew.json)
- 12 vocab entries; Hebrew translit fields are blank in glossary — supplied manually
- H3068 (YHWH): peak=Minor in freq data (Minor Prophets use YHWH most densely per word),
  but Moses-rate=31.50 and the name's formal revelation is Exodus 3:14 — included as essential
- H1818 (dam): lit gloss '-guiltiness' is misleading; using 'blood' (the word's primary meaning)
- H5647 (abad): lit='keep in bondage'; using 'serve' (the word's core meaning before
  and after the Exodus — same root for slavery and worship)
- H4908 (mishkan): lit='dwelleth'; using 'tabernacle/dwelling place'
- H3548 (kohen): lit='chief ruler'; using 'priest'
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
    "bookId": "exodus",

    "key_vocabulary": [
        {
            "code": "H3068",
            "lemma": "יְהֹוָה",
            "translit": "YHWH",
            "gloss": "LORD",
            "significance": "יְהוָה (YHWH — the Tetragrammaton, usually rendered &lsquo;LORD&rsquo; in English translations) is the personal name of Israel&rsquo;s God, formally revealed to Moses at the burning bush in Exodus 3:14-15. When Moses asks God&rsquo;s name, God responds &lsquo;I AM WHO I AM&rsquo; (אֶהְיֶה אֲשֶׁר אֶהְיֶה, ehyeh asher ehyeh) and then says &lsquo;YHWH, the God of your fathers&rsquo; — linking the eternal self-existence of &lsquo;I AM&rsquo; to the covenant faithfulness toward Abraham, Isaac, and Jacob. The name probably derives from the verb הָיָה (hayah, &lsquo;to be&rsquo;) in the causative sense — YHWH as &lsquo;the one who causes to be&rsquo; or &lsquo;the one who is what he is.&rsquo; Jewish tradition considered the name too holy to pronounce, substituting Adonai (&lsquo;Lord&rsquo;) when reading aloud — hence the hybrid &lsquo;Jehovah&rsquo; which combines YHWH&rsquo;s consonants with Adonai&rsquo;s vowels. Jesus&rsquo;s seven &lsquo;I am&rsquo; statements in John&rsquo;s Gospel explicitly echo this Sinai self-revelation."
        },
        {
            "code": "H6453",
            "lemma": "פֶּסַח",
            "translit": "pesaḥ",
            "gloss": "Passover",
            "significance": "פֶּסַח (pesah, &lsquo;Passover, the Passover offering&rsquo;) derives from the verb pasah (to pass over, spare, exempt) and names the central act of Israel&rsquo;s redemption: when YHWH &lsquo;passed over&rsquo; the houses marked with blood (12:13, 23, 27), he spared the firstborn of Israel while the firstborn of Egypt died. The word appears first in 12:11 and immediately becomes the name of Israel&rsquo;s defining annual festival (12:21, 27, 43, 48; 13:6-10). The Passover lamb must be without blemish (12:5), killed at twilight (12:6), its blood applied to the doorposts (12:7), and consumed entirely within the night (12:10). Paul identifies Christ as &lsquo;our Passover lamb&rsquo; (τὸ πάσχα ἡμῶν, 1 Cor 5:7), and John structures his Gospel so that Jesus dies precisely when the Passover lambs are slaughtered in the temple (John 19:14). The word travels from Hebrew pesah into Greek as πάσχα and into English as &lsquo;Paschal&rsquo; — as in &lsquo;Paschal mystery.&rsquo;"
        },
        {
            "code": "H1818",
            "lemma": "דָּם",
            "translit": "dām",
            "gloss": "blood",
            "significance": "דָּם (dam, &lsquo;blood&rsquo;) is the pivotal material of the Exodus narrative at two levels. At the macro level, the Passover formula &lsquo;when I see the blood (הַדָּם), I will pass over you&rsquo; (12:13) makes blood the dividing mark between judgment and protection — not Israel&rsquo;s goodness but the blood of the substitute. At the covenant level, the blood of the covenant is central to the Sinai ratification: Moses takes the blood of the burnt offerings, throws half against the altar, reads the Book of the Covenant, and throws the remaining half on the people, saying &lsquo;this is the blood of the covenant that YHWH has made with you in accordance with all these words&rsquo; (24:8). This blood-covenant ceremony is the explicit background for Jesus&rsquo;s words at the Last Supper: &lsquo;this is my blood of the covenant, which is poured out for many for the forgiveness of sins&rsquo; (Matt 26:28). The Epistle to the Hebrews expounds the entire Exodus blood ritual as pointing to Christ&rsquo;s own blood."
        },
        {
            "code": "H5647",
            "lemma": "עָבַד",
            "translit": "ʿābad",
            "gloss": "serve",
            "significance": "עָבַד (abad, &lsquo;to serve, work, till; to worship&rsquo;) is one of Exodus&rsquo;s most theologically dense words because the same verb covers both the slavery Israel endures and the worship they are redeemed for. In 1:13-14, Israel &lsquo;worked (יַּעֲבִדוּ) in crushing bondage&rsquo; for Pharaoh. In 3:12, when Moses asks what he will tell Israel, God says: &lsquo;when you have brought the people out of Egypt, you shall serve (תַּעַבְדוּן) God on this mountain.&rsquo; The same verb serves both slavery and worship, and the substitution is the entire Exodus: Israel is freed from serving Pharaoh in order to serve YHWH. The noun עֲבוֹדָה (avodah, &lsquo;work/service/worship&rsquo;) carries both meanings simultaneously in Hebrew. Moses&rsquo;s repeated demand to Pharaoh — &lsquo;let my people go, so they may serve (וְיַעַבְדֻנִי) me in the wilderness&rsquo; (8:1, 20; 9:1, 13; 10:3) — is not merely a request for freedom but a transfer of ownership: Israel belongs to YHWH, not to Pharaoh, and will serve him, not Egypt."
        },
        {
            "code": "H3519",
            "lemma": "כָּבוֹד",
            "translit": "kābôd",
            "gloss": "glory",
            "significance": "כָּבוֹד (kabod, &lsquo;glory, weight, honor, splendor&rsquo;) in Exodus is the visible manifestation of God&rsquo;s presence — heavy, luminous, overwhelming. The root means &lsquo;to be heavy&rsquo;: God&rsquo;s glory is that which has ultimate weight and reality. The glory appears as a cloud and fire leading Israel through the wilderness (13:21-22), settles on Sinai (24:16-17), fills the tabernacle when it is completed (40:34-35) — so powerfully that Moses cannot enter. Moses&rsquo;s request &lsquo;show me your glory (כְּבֹדֶךָ)&rsquo; (33:18) is the most intimate prayer in Exodus; God responds by making all his goodness pass before Moses while he is hidden in the rock (33:19-23). The book&rsquo;s final image — glory filling the tabernacle, cloud covering it, Moses unable to enter — is the consummation of all 40 chapters: God has come to dwell among his people in visible, heavy, overwhelming presence. The NT picks up this language for Christ: &lsquo;we have seen his glory&rsquo; (John 1:14) and for the eschatological temple (Rev 21:23)."
        },
        {
            "code": "H6944",
            "lemma": "קֹדֶשׁ",
            "translit": "qōdeš",
            "gloss": "holiness",
            "significance": "קֹדֶשׁ (qodesh, &lsquo;holiness, sacredness, what is set apart for God&rsquo;) peaks in the Moses author group and pervades Exodus as the character of God that demands a corresponding character in his people. The burning bush is &lsquo;holy ground&rsquo; (3:5). Sinai is the &lsquo;holy mountain&rsquo; with strict boundaries (19:23). The tabernacle is structured around graduated holiness: the outer court, the holy place, the most holy place (the Holy of Holies, קֹדֶשׁ הַקֳּדָשִׁים). The priests wear garments inscribed &lsquo;holy to YHWH&rsquo; (28:36). And the goal stated at Sinai: &lsquo;you shall be to me a kingdom of priests and a holy nation&rsquo; (19:6). Holiness in Exodus is not primarily moral purity (though it includes it) but relational status: the people are set apart — consecrated — as belonging to YHWH. This sets the entire sacrificial and purity system of Leviticus: before Israel can approach the holy God, the holiness problem created by sin must be addressed through blood, atonement, and consecration."
        },
        {
            "code": "H3722",
            "lemma": "כָּפַר",
            "translit": "kāpar",
            "gloss": "atone",
            "significance": "כָּפַר (kapar, &lsquo;to cover, atone, make propitiation&rsquo;) peaks in the Moses author group and is the theological verb of the tabernacle&rsquo;s entire sacrificial system. The root meaning is &lsquo;to cover&rsquo; — the related noun כַּפֹּרֶת (kapporet) names the lid of the ark of the covenant: the &lsquo;atonement cover&rsquo; or &lsquo;mercy seat,&rsquo; rendered ἱλαστήριον in the Septuagint (the same word Paul uses in Romans 3:25 for Christ as the &lsquo;propitiation&rsquo;). On the Day of Atonement (Lev 16), the high priest sprinkled blood on the kapporet to cover Israel&rsquo;s sins before the presence of YHWH. In Exodus, the word appears repeatedly in the tabernacle instructions: &lsquo;and Aaron shall make atonement (כִּפֶּר) on its horns once a year with the blood of the sin offering&rsquo; (30:10). The atonement system addresses the central problem of a holy God dwelling among a sinful people: without covering, the proximity of holiness and sin is fatal. The NT reads Christ&rsquo;s death as the definitive kapar — covering sins not with animal blood but with his own (Heb 9:11-14)."
        },
        {
            "code": "H4908",
            "lemma": "מִשְׁכָּן",
            "translit": "miškān",
            "gloss": "tabernacle",
            "significance": "מִשְׁכָּן (mishkan, &lsquo;tabernacle, dwelling place&rsquo;) peaks in the Moses author group and names the portable sanctuary God commands Israel to build so that he may dwell among them (25:8). The word derives from שָׁכַן (shakan, &lsquo;to dwell, reside permanently&rsquo;), and God&rsquo;s stated purpose is explicit: &lsquo;let them make me a sanctuary, that I may dwell (שָׁכַנְתִּי) in their midst&rsquo; (25:8). The mishkan is not a temple for occasional visits but God&rsquo;s permanent address within the covenant community. Architecturally, the tabernacle mirrors Sinai (the mountain of God&rsquo;s presence) as a portable version: the outer court corresponds to the foot of the mountain, the holy place to the mountain itself, the most holy place to the summit where God spoke to Moses. In John 1:14, the Incarnation is described with the same root: &lsquo;the Word became flesh and dwelt (ἐσκήνωσεν — &lsquo;tabernacled&rsquo;) among us&rsquo; — a deliberate echo of Exodus&rsquo;s mishkan. God&rsquo;s goal of dwelling with his people, inaugurated at the tabernacle, reaches its fulfillment in Christ and its consummation in the new Jerusalem where &lsquo;the tabernacle (σκηνή) of God is with man&rsquo; (Rev 21:3)."
        },
        {
            "code": "H3548",
            "lemma": "כֹּהֵן",
            "translit": "kōhēn",
            "gloss": "priest",
            "significance": "כֹּהֵן (kohen, &lsquo;priest, officiating minister&rsquo;) peaks in the Moses author group and in Exodus designates the mediatorial office that Aaron and his sons occupy at the center of the tabernacle system. The priest is the boundary-crosser: he enters the presence of a holy God on behalf of an unholy people, offering sacrifice, burning incense, and maintaining the instruments of the sanctuary. The priestly vestments (ch. 28) — the ephod, the breastplate with the names of the twelve tribes, the golden plate inscribed &lsquo;holy to YHWH&rsquo; — visually embody the priest&rsquo;s mediatorial role: he bears the names of Israel before God and bears the holiness of God before Israel. The Epistle to the Hebrews reads the Aaronic priesthood as a shadow pointing to the perfect High Priest who has passed through the heavenly tabernacle once and for all with his own blood (Heb 9:11-12). Exodus 19:6 (&lsquo;a kingdom of priests and a holy nation&rsquo;) anticipates a day when the entire people holds the priestly function — applied to the church in 1 Peter 2:9 and to the redeemed in Revelation 1:6; 5:10."
        },
        {
            "code": "H6440",
            "lemma": "פָּנִים",
            "translit": "pānîm",
            "gloss": "face",
            "significance": "פָּנִים (panim, &lsquo;face, presence, the front of someone or something&rsquo;) peaks in the Moses author group and is the word for the most intimate dimension of divine encounter in Exodus. The phrase פָּנִים אֶל פָּנִים (panim el panim, &lsquo;face to face&rsquo;) describes the unique quality of Moses&rsquo;s relationship with God: &lsquo;YHWH used to speak to Moses face to face, as a man speaks to his friend&rsquo; (33:11). Yet in the same context God declares: &lsquo;you cannot see my face (פָּנַי), for man shall not see me and live&rsquo; (33:20). Moses is instead shown God&rsquo;s back as God&rsquo;s glory passes by. This paradox — Moses speaks face to face with God, yet cannot see God&rsquo;s face — defines the tension of the old covenant: intimate relationship yet mediated, direct access yet bounded. The &lsquo;bread of the Presence&rsquo; in the tabernacle (25:30) is literally &lsquo;bread of the face&rsquo; (לֶחֶם הַפָּנִים) — the loaves placed perpetually before God&rsquo;s face. Moses&rsquo;s face itself shines after his encounters with God (34:29-35) — glory reflected from the divine face. The NT declares that the glory Moses glimpsed is now fully visible in Christ: &lsquo;the light of the knowledge of the glory of God in the face of Jesus Christ&rsquo; (2 Cor 4:6)."
        },
        {
            "code": "H2077",
            "lemma": "זֶבַח",
            "translit": "zebaḥ",
            "gloss": "sacrifice",
            "significance": "זֶבַח (zevaḥ, &lsquo;slaughter, sacrifice — a sacrifice involving the slaughter of an animal&rsquo;) peaks in the Moses author group and is the primary word for Israel&rsquo;s sacrificial practice in Exodus. The zevaḥ involves the killing of an animal, the manipulation of its blood, and a sacred meal shared among offerers, priests, and sometimes YHWH (whose portion goes up as smoke). In Exodus, Moses repeatedly demands that Israel be released to &lsquo;sacrifice (וְנִזְבְּחָה) to YHWH our God in the wilderness&rsquo; (3:18; 5:3, 8, 17). The Passover itself is a zevaḥ (12:27): &lsquo;it is the sacrifice (זֶבַח) of YHWH&rsquo;s Passover.&rsquo; The word roots the whole sacrificial system in the visceral reality of slaughter: atonement and worship cost something; the sanctuary is not an aesthetic space but a slaughterhouse hallowed by divine presence. The contrast with pure incense or grain offerings kept before the worshipper the fundamental logic of substitution: something dies so that the worshipper may live in God&rsquo;s presence."
        },
        {
            "code": "H5337",
            "lemma": "נָצַל",
            "translit": "nāṣal",
            "gloss": "deliver",
            "significance": "נָצַל (natsal, &lsquo;to snatch away, rescue, deliver from danger&rsquo;) names the decisive action of God in the Exodus. At the burning bush, YHWH declares his intent: &lsquo;I have come down to deliver (לְהַצִּילוֹ) them out of the hand of the Egyptians&rsquo; (3:8). The word describes sudden, decisive rescue — the snatching of something from the grip of a stronger power. After the crossing of the Red Sea, Israel recognizes what has happened: &lsquo;YHWH saved (וַיּוֹשַׁע) Israel that day from the hand of the Egyptians&rsquo; (14:30). The Exodus becomes the paradigmatic act of divine rescue in all subsequent OT theology: every prayer for deliverance, every cry of the psalmists, every prophetic promise of restoration echoes the Exodus as the model for what God does when he acts. The NT reads the death and resurrection of Christ as the new Exodus — the natsal that rescues not from Egyptian slavery but from the slavery of sin and death (Luke 9:31, where Jesus&rsquo;s departure — &lsquo;exodus&rsquo; — is the word used for his death in Jerusalem)."
        }
    ],

    "language_notes": (
        "<p>Exodus introduces what becomes the most theologically loaded word in the Hebrew Bible: <strong>יְהוָה (YHWH)</strong>, the divine personal name revealed formally at the burning bush (3:14-15). The name&rsquo;s etymology is debated — it is most likely related to the verb הָיָה (hayah, &lsquo;to be, to exist, to cause to be&rsquo;) — but the text itself interprets it: אֶהְיֶה אֲשֶׁר אֶהְיֶה, usually rendered &lsquo;I AM WHO I AM&rsquo; but equally &lsquo;I WILL BE WHAT I WILL BE&rsquo; (the Hebrew imperfect tense is both present and future). The name announces not merely God&rsquo;s self-existence but his commitment to remain who he is in covenant faithfulness. In 6:2-3, YHWH says explicitly: &lsquo;I appeared to Abraham, to Isaac, and to Jacob as El Shaddai, but by my name YHWH I did not make myself known to them.&rsquo; The Exodus is the moment the divine name is unveiled — and with it, the full personal character of God as redeemer.</p>"
        "<p>One of Exodus&rsquo;s most linguistically precise theological moves is its use of <strong>עָבַד (abad)</strong> — the same verb — for both Israel&rsquo;s slavery under Pharaoh and their worship of YHWH. &lsquo;The Israelites were made to work (יַּעֲבִדוּ) as slaves&rsquo; (1:13); &lsquo;let my people go, that they may serve (וְיַעַבְדֻנִי) me&rsquo; (8:1). The Hebrew text makes the substitution unavoidable: the people will serve — the only question is whose service they are in. The redemption is not from service to freedom but from one master to another. This linguistic precision grounds the NT&rsquo;s theology of freedom: &lsquo;you are slaves of the one you obey&rsquo; (Rom 6:16); freed from sin to become &lsquo;slaves of righteousness&rsquo; (Rom 6:18). The Exodus liberates for worship, not from it.</p>"
        "<p>The <strong>Song of the Sea</strong> (Exodus 15:1-21) is one of the oldest pieces of Hebrew poetry in the Bible and exhibits archaic features distinct from later biblical poetry. The tricolon structure (three-part parallel lines) appears more frequently here than in later two-part parallelism. Archaic verb forms (&lsquo;Yah&rsquo; as a shortened divine name, v. 2) and lexical items (&lsquo;Yahweh is a man of war,&rsquo; v. 3, using אִישׁ מִלְחָמָה) reflect a very early date. The poem celebrates not the departure from Egypt but the defeat of the Egyptians in the sea — the focus is God&rsquo;s military triumph, establishing YHWH as the divine warrior. The poem&rsquo;s structure anticipates the destination: it closes with the temple where God will reign forever (15:17-18), collapsing the Sinai journey and the Jerusalem temple into a single expectation. Miriam&rsquo;s antiphon in 15:21 (&lsquo;sing to YHWH, for he has triumphed gloriously&rsquo;) is probably the oldest form of the song.</p>"
        "<p>The tabernacle instructions (chs. 25-31) and their execution (chs. 35-40) exhibit a <strong>deliberate verbal repetition</strong> in which the construction account mirrors the command account almost word for word. This is not literary laziness but theological emphasis: the people do precisely what God commanded, without addition or subtraction. The phrase &lsquo;just as YHWH commanded Moses&rsquo; (כַּאֲשֶׁר צִוָּה יְהוָה אֶת מֹשֶׁה) appears ten times in chapter 40 alone — matching the ten commandments and echoing the seven-fold refrain of creation (&lsquo;and it was so&rsquo;; &lsquo;it was good&rsquo;). The tabernacle&rsquo;s completion is narrated as a second creation: the people, materials, skilled workers, and God&rsquo;s presence come together to make a world within the world — a holy space where heaven and earth overlap.</p>"
    ),

    "reception": (
        "<p><strong>Patristic:</strong> The Exodus narrative was read by the early church as a comprehensive type of Christian redemption. Origen&rsquo;s <em>Homilies on Exodus</em> (c. 240) set the pattern: the Passover lamb = Christ; the Red Sea crossing = baptism; the wilderness journey = the Christian life; the promised land = eternal rest. This typological reading was not considered allegory but historical fulfillment — the Exodus literally happened as a pattern designed to foreshadow the greater redemption. The Ten Commandments received extensive commentary: Augustine grouped them as three toward God and seven toward neighbor (influencing the Western catechetical tradition); the Orthodox East grouped them as four toward God and six toward neighbor. Both traditions saw the Decalogue as the permanent moral law distinct from the ceremonial and civil laws that were fulfilled in Christ.</p>"
        "<p><strong>Reformation:</strong> Luther and Calvin both treated the Sinai covenant with care but differently. Luther distinguished law and gospel sharply: the Sinai law reveals sin and drives to Christ; it does not provide a means of salvation. Calvin saw the Mosaic law as three uses — a mirror of sin, a curb on society, and a guide for the regenerate. The tabernacle received renewed attention: Calvin argued against elaborate church art and decoration partly because the elaborate tabernacle instructions were given for Israel&rsquo;s infant state and were fulfilled in Christ, the true temple. The Passover&rsquo;s relation to the Lord&rsquo;s Supper was hotly debated: Catholic, Lutheran, Reformed, and Zwinglian traditions all appealed to Exodus 12 in their eucharistic controversies.</p>"
        "<p><strong>Modern:</strong> Two questions dominate contemporary Exodus scholarship. The first is <em>historicity</em>: no direct Egyptian records of the Exodus exist (as expected — no empire records its defeats), but various lines of evidence (Semitic names in Egypt, Habiru groups, the plagues&rsquo; correspondence to the Nile ecology, the Merneptah Stele&rsquo;s reference to &lsquo;Israel&rsquo; as a people in Canaan by 1208 BC) establish the plausibility of a 15th- or 13th-century date. The second is <em>the plagues as polemic against Egyptian deities</em>: each plague targets a major Egyptian deity (the Nile = Hapi; frogs = Heqet; cattle = Apis; the firstborn of Pharaoh = who himself was considered divine), making the ten plagues a systematic demonstration that YHWH&rsquo;s power exceeds every Egyptian god. This reading enriches the theological claim: the Exodus is not merely Israel&rsquo;s liberation but a cosmic reckoning of who the true God is.</p>"
    ),

    "reading_guide": (
        "<p>Exodus divides naturally into two halves with very different literary textures. Chapters 1-18 are narrative — dramatic, story-driven, moving at pace: the birth and calling of Moses, the confrontations with Pharaoh, the plagues, the Passover night, the crossing of the sea, the wilderness journey. Chapters 19-40 are legal and ritual — detailed, measured, structured: the Sinai theophany, the Decalogue, the covenant code, the tabernacle instructions. Do not read the second half as a less interesting appendix; it is the destination. The redemption of chapters 1-18 has a purpose, stated in 25:8: <em>&lsquo;let them make me a sanctuary, that I may dwell in their midst.&rsquo;</em> The goal of the Exodus is not freedom in the abstract but the presence of God.</p>"
        "<p>Watch the <strong>hardening of Pharaoh&rsquo;s heart</strong> carefully — it is more complex than it first appears. In some passages Pharaoh hardens his own heart (8:15, 32; 9:34); in others YHWH hardens it (4:21; 7:3; 9:12; 10:1, 20, 27; 11:10; 14:4, 8). The two are not contradictions but the inside and outside of the same event: Pharaoh&rsquo;s freely chosen hardening is simultaneously God&rsquo;s judicial hardening in judgment. Paul uses this very passage in Romans 9:17-18 to ground divine sovereignty in election, while the narrative itself never removes Pharaoh&rsquo;s responsibility for his refusals. The hardening serves a theological purpose explicitly stated: &lsquo;so that I may multiply my signs and wonders in Egypt&rsquo; (7:3) — the prolonged confrontation demonstrates YHWH&rsquo;s supremacy over all Egyptian gods decisively rather than summarily.</p>"
        "<p>The Decalogue (20:1-17) opens with a statement that is often overlooked: &lsquo;<em>I am YHWH your God, who brought you out of the land of Egypt, out of the house of slavery.&rsquo;</em> This is not a commandment — it is the gospel that precedes all the commandments. The Ten Words are not the way Israel earns its relationship with God; they describe the life of a people already redeemed, already in covenant. Obedience is the grateful response to grace, not the precondition for it. Common misreadings to avoid: treating the tabernacle instructions as irrelevant ritual detail (they are the architecture of God&rsquo;s dwelling — read them as the blueprint of his home); reading Moses as a solitary hero rather than a mediator who repeatedly intercedes for the people he leads (33:12-17; 34:9); and assuming the &lsquo;I AM&rsquo; of 3:14 is only a philosophical claim about God&rsquo;s existence rather than a covenantal promise — &lsquo;I will be with you&rsquo; (3:12).</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('exodus')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('exodus', merged)

main()
