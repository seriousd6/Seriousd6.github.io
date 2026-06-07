"""
Book Study Data — Isaiah
book_id: isaiah
lang: hebrew

Run: python3 scripts/build-book-study-isaiah.py

Notes:
- Author group: Major (Isaiah–Daniel) in author-freq-hebrew.json; peaks include
  many generic proper nouns and function words — vocabulary selected from Isaiah's
  specific theological program
- All Hebrew translit fields blank in glossary — supplied manually
- H6918 qadosh: "Holy One of Israel" appears 26x in Isaiah vs. ~6x in all other OT
  books combined; this is Isaiah's single most distinctive theological contribution
- H5650 eved: The four Servant Songs are Isaiah's greatest literary achievement and
  the most densely Christological passage in the OT; the Servant's identity
  deliberately shifts, requiring the NT to supply the referent
- H7522 ratson: Isaiah 61:2 ("the year of the LORD's favor") is the text Jesus reads
  in the Nazareth synagogue (Luke 4:19), stopping before "the day of vengeance" —
  one of the most theologically significant editorial pauses in the Gospels
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
    "bookId": "isaiah",

    "key_vocabulary": [
        {
            "code": "H6918",
            "lemma": "קָדוֹשׁ",
            "translit": "qādôš",
            "gloss": "holy",
            "significance": "קָדוֹשׁ (qadosh, &lsquo;sacred — set apart, morally transcendent; as noun, God by eminence&rsquo;) is Isaiah&rsquo;s most distinctive theological contribution: &ldquo;the Holy One of Israel&rdquo; (qedosh yisrael) appears 26 times in Isaiah, compared to roughly 6 times in the rest of the OT combined. The seraphim&rsquo;s cry in 6:3 — &ldquo;Holy, holy, holy is the LORD of hosts&rdquo; (qadosh qadosh qadosh YHWH tsvaot) — is the only triple repetition of a divine attribute in the Hebrew Bible; it functions as a superlative of the superlative: not merely holy but transcendently, overwhelmingly holy. Isaiah&rsquo;s inaugural vision of holiness immediately reveals human uncleanness: &ldquo;Woe is me! For I am lost; for I am a man of unclean lips&rdquo; (6:5). This holiness-uncleanness dialectic drives the entire book: Judah sins against the Holy One (1:4: &ldquo;they have despised the Holy One of Israel&rdquo;), judgment falls, and then — unexpectedly — the same Holy One redeems: &ldquo;Fear not, for I am with you...I am your God&rdquo; (41:10). John 12:41 identifies the enthroned figure of Isaiah 6 as Christ: &ldquo;Isaiah said these things because he saw his glory and spoke of him.&rdquo; The trisagion becomes the unceasing worship of Revelation 4:8."
        },
        {
            "code": "H5650",
            "lemma": "עֶבֶד",
            "translit": "ʿɛbɛd",
            "gloss": "servant",
            "significance": "עֶבֶד (eved, &lsquo;a servant&rsquo;) anchors the four Servant Songs that are Isaiah&rsquo;s greatest theological achievement: 42:1-9, 49:1-13, 50:4-11, and 52:13-53:12. The Servant&rsquo;s identity deliberately shifts across the Songs: in 41:8-9 Israel is the servant; in 42:1-9 the Servant has a mission <em>to</em> Israel; by 53 the Servant suffers as a substitute for the people. Isaiah 53:5: &ldquo;He was pierced for our transgressions; he was crushed for our iniquities; upon him was the chastisement that brought us peace, and with his wounds we are healed.&rdquo; The NT applies the Servant Songs to Christ with remarkable consistency: Matthew 8:17 cites 53:4 for Jesus&rsquo; healings; Acts 8:32-35 applies 53:7-8 to Jesus&rsquo; death; 1 Peter 2:24 applies 53:5 to the atonement. Isaiah 52:13-53:12 contains the doctrine of substitutionary atonement more clearly than almost anywhere else in Scripture — the Servant is described as bearing sin (53:6), being numbered with transgressors (53:12), and being exalted after suffering (52:13; 53:12). This is why the early church called Isaiah &ldquo;the fifth gospel.&rdquo;"
        },
        {
            "code": "H6726",
            "lemma": "צִיּוֹן",
            "translit": "ṣiyyôn",
            "gloss": "Zion",
            "significance": "צִיּוֹן (Zion, &lsquo;a permanent capital — a mountain of Jerusalem&rsquo;) carries in Isaiah a concentrated eschatological theology. The word appears ~49 times in Isaiah, more than in any other OT book except Psalms. Isaiah 2:3: &ldquo;For out of Zion shall go forth the law, and the word of the LORD from Jerusalem.&rdquo; Isaiah 28:16: &ldquo;I am laying in Zion a stone, a tested stone, a precious cornerstone...whoever believes will not be in haste.&rdquo; Isaiah 52:7: &ldquo;How beautiful upon the mountains are the feet of him who brings good news, who publishes peace...who says to Zion, &lsquo;Your God reigns.&rsquo;&rdquo; Isaiah 62:11: &ldquo;Say to the daughter of Zion, &lsquo;Behold, your salvation comes.&rsquo;&rdquo; Isaiah&rsquo;s Zion is not merely Jerusalem but the eschatological city of God&rsquo;s dwelling and the destination of the worldwide pilgrimage of nations. The NT picks up this Zion-theology fully: Paul applies Isaiah 28:16 to Christ as the cornerstone (Rom 9:33; 10:11); Hebrews 12:22 says believers have &ldquo;come to Mount Zion, to the city of the living God, the heavenly Jerusalem&rdquo;; Revelation 14:1 places the Lamb on Mount Zion."
        },
        {
            "code": "H136",
            "lemma": "אֲדֹנָי",
            "translit": "ʾădōnāy",
            "gloss": "Lord",
            "significance": "אֲדֹנָי (Adonai, &lsquo;the Lord — used as a proper name of God only&rsquo;) is Isaiah&rsquo;s most frequent reverential address for God, appearing with dramatically higher density in Isaiah than in any other prophetic book. Isaiah 6:1: &ldquo;I saw the Lord (Adonai) sitting upon a throne, high and lifted up&rdquo; — the throne-room vision that commissions Isaiah&rsquo;s entire prophetic career. Isaiah characteristically combines Adonai with YHWH: &ldquo;the Lord GOD&rdquo; (Adonai YHWH) appears repeatedly, emphasizing both the sovereignty of the divine lord and the covenant name. Isaiah 6:8: &ldquo;And I heard the voice of the Lord (Adonai) saying, &lsquo;Whom shall I send, and who will go for us?&rsquo;&rdquo; The Adonai-language situates Isaiah&rsquo;s ministry under the authority of the heavenly sovereign: the prophet speaks only because the divine Lord has spoken first. John 12:41 identifies the Adonai of Isaiah 6 as Christ, whose pre-incarnate glory Isaiah saw — making the Adonai-address to the enthroned God Christologically significant."
        },
        {
            "code": "H7971",
            "lemma": "שָׁלַח",
            "translit": "šālaḥ",
            "gloss": "send",
            "significance": "שָׁלַח (shalach, &lsquo;to send away, for, or out — in a great variety of applications&rsquo;) is Isaiah&rsquo;s word for prophetic commission and for the Servant&rsquo;s mission. Isaiah 6:8: the divine question &ldquo;Whom shall I send (eshla*ch*)?&rdquo; and Isaiah&rsquo;s answer &ldquo;Here I am! Send me&rdquo; — the defining moment of the prophet&rsquo;s call. Isaiah 48:16: &ldquo;the Lord GOD has sent (shalach) me, and his Spirit&rdquo; — the Servant&rsquo;s own claim to divine commission. Isaiah 61:1 (the text Jesus reads in the Nazareth synagogue): &ldquo;The Spirit of the Lord GOD is upon me...he has sent (shalach) me to bind up the brokenhearted, to proclaim liberty to the captives.&rdquo; The shalach-chain runs from God&rsquo;s sending Isaiah, through God&rsquo;s sending the Servant, to Jesus&rsquo; sending his disciples: John 20:21: &ldquo;As the Father has sent (apostellein) me, even so I am sending you.&rdquo; The apostolic mission is the extension of the shalach that Isaiah&rsquo;s call inaugurated."
        },
        {
            "code": "H7522",
            "lemma": "רָצוֹן",
            "translit": "rāṣôn",
            "gloss": "favor",
            "significance": "רָצוֹן (ratson, &lsquo;delight, pleasure, favor — especially as shown&rsquo;) is Isaiah&rsquo;s word for the eschatological favor of God freely extended in restoration. Isaiah 49:8: &ldquo;In a time of favor (ratson) I have answered you; in a day of salvation I have helped you.&rdquo; Isaiah 61:2: &ldquo;to proclaim the year of the LORD&rsquo;s favor (ratson), and the day of vengeance of our God.&rdquo; This last text is the one Jesus reads in the Nazareth synagogue (Luke 4:18-19), stopping in the middle of the verse — after &ldquo;the year of the LORD&rsquo;s favor&rdquo; and before &ldquo;the day of vengeance.&rdquo; Jesus then says: &ldquo;Today this Scripture has been fulfilled in your hearing.&rdquo; The ratson-year has arrived in Jesus&rsquo; first coming; the day of vengeance awaits the second. This editorial pause in the middle of Isaiah 61:2 is one of the most significant in all of Scripture — Jesus&rsquo; selective quotation reveals the two-advent structure of Isaiah&rsquo;s eschatology. Paul applies Isaiah 49:8 directly to the gospel announcement: &ldquo;Behold, now is the favorable time; behold, now is the day of salvation&rdquo; (2 Cor 6:2)."
        },
        {
            "code": "H2377",
            "lemma": "חָזוֹן",
            "translit": "ḥāzôn",
            "gloss": "vision",
            "significance": "חָזוֹן (chazon, &lsquo;a sight mentally — a dream, revelation, or oracle&rsquo;) is the genre-label Isaiah gives his own book. Isaiah 1:1: &ldquo;The vision (chazon) of Isaiah the son of Amoz, which he saw concerning Judah and Jerusalem.&rdquo; The chazon is not a private spiritual experience but a prophetic reception of the divine word intended for public proclamation. It is also the word for the foundational throne-room vision of chapter 6 — the vision that undoes Isaiah and reconstitutes him as a prophet. Isaiah 29:11: &ldquo;The vision (chazon) of all this has become to you like the words of a book that is sealed.&rdquo; The sealed chazon — disclosure that cannot yet be read — is opened when the Lamb opens the seals in Revelation 5-8. Proverbs 29:18 uses chazon in its proverbial form: &ldquo;Where there is no prophetic vision (chazon), the people cast off restraint.&rdquo; The chazon-tradition runs from Moses (Num 12:6) through Isaiah to the NT&rsquo;s apokalypsis: both words (Hebrew chazon, Greek apokalypsis) mean the lifting of the veil."
        },
        {
            "code": "H7665",
            "lemma": "שָׁבַר",
            "translit": "šābar",
            "gloss": "break",
            "significance": "שָׁבַר (shabar, &lsquo;to burst, break — literally or figuratively&rsquo;) appears in Isaiah&rsquo;s judgment oracles and — with theological precision — in the Servant Song. Isaiah 24:19: &ldquo;The earth is utterly broken (shabar), the earth is split apart.&rdquo; Isaiah 1:28: &ldquo;But rebels and sinners shall be broken (shabar) together.&rdquo; But the most important shabar in Isaiah is 42:3 — the negative: &ldquo;a bruised reed he will not break (lo yishbor).&rdquo; Matthew 12:20 quotes this as a prophecy of Jesus&rsquo; gentle ministry. The Servant who does not break bruised reeds is the same one who was himself broken: Isaiah 53:5 says &ldquo;he was crushed (daka) for our iniquities&rdquo; — a parallel verb to shabar. The play between God&rsquo;s breaking of the nations in judgment (Isa 14:25; 24:19) and the Servant&rsquo;s not-breaking of the bruised reed captures the two faces of Isaiah&rsquo;s God: the one who shatters the proud and carefully handles the fragile."
        },
        {
            "code": "H6817",
            "lemma": "צָעַק",
            "translit": "ṣāʿaq",
            "gloss": "cry out",
            "significance": "צָעַק (tsaaq, &lsquo;to shriek, cry aloud — by implication, to proclaim&rsquo;) is Isaiah&rsquo;s word for the distress-cry that ascends from the oppressed and generates prophetic response. Isaiah 19:20: &ldquo;When they cry (yitsaqu) to the LORD because of oppressors, he will send them a savior and defender.&rdquo; Isaiah 5:7 contains one of Isaiah&rsquo;s most devastating wordplays: &ldquo;He looked for <em>mishpat</em> (justice), but behold, <em>mispach</em> (bloodshed); for <em>tsedaqah</em> (righteousness), but behold, <em>tseaqah</em> (outcry).&rdquo; The paronomasia — the near-rhyming of justice/bloodshed and righteousness/outcry — is untranslatable: God looked for one thing and heard another. The tseaqah (cry, the noun form of tsaaq) of the oppressed is the sound that fills the space where justice should be. Isaiah&rsquo;s social justice language runs alongside his Servant-theology: the Servant who &ldquo;will not cry aloud or lift up his voice&rdquo; (42:2) is contrasted with the oppressed who cry out for justice — he absorbs the injustice that generates their cry."
        },
        {
            "code": "H5012",
            "lemma": "נָבָא",
            "translit": "nāvāʾ",
            "gloss": "prophesy",
            "significance": "נָבָא (naba, &lsquo;to prophesy — to speak or sing by inspiration in prediction or simple discourse&rsquo;) describes the prophetic act in which Isaiah claims divine authority. Isaiah 30:10: &ldquo;who say to the seers, &lsquo;Do not see,&rsquo; and to the prophets (hanevim), &lsquo;Do not prophesy (lo tinbau) to us what is right.&rsquo;&rdquo; The naba-act is not human theorizing or religious enthusiasm but the conveying of the divine word under divine compulsion. Isaiah&rsquo;s prophetic self-consciousness is expressed through repeated &ldquo;Thus says the LORD&rdquo; (ko amar YHWH) formulas — the prophetic messenger formula that authorizes the proclamation. The book of Isaiah is notable for its self-referential prophecy: Isaiah prophesies the Babylonian exile while still in the Assyrian period (chs. 39-40), and names Cyrus as the liberator ~150 years before Cyrus lived (44:28; 45:1) — claims that drive both the unity debate and the early church&rsquo;s use of Isaiah as proof of divine omniscience. 2 Peter 1:21 provides the theology of naba: &ldquo;men spoke from God as they were carried along by the Holy Spirit.&rdquo;"
        },
        {
            "code": "H894",
            "lemma": "בָּבֶל",
            "translit": "bābɛl",
            "gloss": "Babylon",
            "significance": "בָּבֶל (Babel/Babylon, &lsquo;Babel — including Babylonia and the Babylonian empire&rsquo;) is the historical-theological referent for Isaiah&rsquo;s central judgment-and-restoration narrative. Chapters 13-14 pronounce judgment on Babylon (the &ldquo;oracle concerning Babylon&rdquo;); chapters 40-55 address the exiles in Babylon and promise a new exodus out of her; chapter 47 is an extended taunt-song over fallen Babylon. Isaiah 47:1: &ldquo;Come down and sit in the dust, O virgin daughter of Babylon.&rdquo; Isaiah 48:20: &ldquo;Go out from Babylon, flee from Chaldea.&rdquo; Babylon in Isaiah is not merely an empire but a theological symbol: the city of human pride (Gen 11:1-9), the antithesis of Zion, the place where idols are worshiped and the people of God are enslaved. Revelation appropriates Isaiah&rsquo;s Babylon-theology wholesale: &ldquo;Fallen, fallen is Babylon the great!&rdquo; (Rev 14:8; 18:2) — the entire Roman imperial system is coded as Babylon, and the new exodus from Babylon (Rev 18:4: &ldquo;Come out of her, my people&rdquo;) quotes Isaiah 48:20. Babylon becomes the Bible&rsquo;s permanent symbol for the world-system in opposition to God."
        },
        {
            "code": "H2534",
            "lemma": "חֵמָה",
            "translit": "ḥēmāh",
            "gloss": "wrath",
            "significance": "חֵמָה (chemah, &lsquo;heat — figuratively, anger, poison; from the fever-image of inflamed emotion&rsquo;) is Isaiah&rsquo;s word for the divine judgment that falls on Israel and the nations. Isaiah 42:25: &ldquo;So he poured on him the heat (chemah) of his anger and the might of battle; it set him on fire all around, but he did not understand.&rdquo; Isaiah 51:17: &ldquo;Rouse yourself, stand up, O Jerusalem, you who have drunk from the hand of the LORD the cup of his wrath (chemah).&rdquo; Isaiah 63:3-6: the divine warrior treads the winepress &ldquo;in my wrath (chemah)...in my anger.&rdquo; But chemah is not the final word: Isaiah 54:8: &ldquo;In overflowing anger (qetsep) for a moment I hid my face from you, but with everlasting love (chesed) I will have compassion on you.&rdquo; The cup of God&rsquo;s chemah that Jerusalem drinks in judgment is the same cup Jesus takes in Gethsemane (Luke 22:42: &ldquo;remove this cup from me&rdquo;) — the cup of divine wrath described most graphically in Isaiah. Revelation 14:10 identifies it as &ldquo;the wine of God&rsquo;s wrath, poured full strength into the cup of his anger.&rdquo;"
        },
        {
            "code": "H6605",
            "lemma": "פָּתַח",
            "translit": "pātaḥ",
            "gloss": "open",
            "significance": "פָּתַח (patach, &lsquo;to open wide — literally or figuratively; specifically, to loosen, begin, carve&rsquo;) appears in Isaiah&rsquo;s most characteristic promises of the messianic age. Isaiah 35:5: &ldquo;Then the eyes of the blind shall be opened (yippatechu), and the ears of the deaf unstopped.&rdquo; Isaiah 42:7: &ldquo;to open (liftoach) the eyes that are blind, to bring out the prisoners from the dungeon, from the prison those who sit in darkness.&rdquo; Isaiah 45:1: &ldquo;to open (liftoach) doors before him that gates may not be closed.&rdquo; Isaiah 60:11: &ldquo;Your gates shall be open (patach) continually.&rdquo; The patach-vocabulary is one of the clearest connections between Isaiah and the NT: Jesus&rsquo; response to John the Baptist&rsquo;s question (&ldquo;Are you the one who is to come?&rdquo;) is a catalogue of patach-fulfillments: &ldquo;the blind receive their sight and the lame walk&rdquo; (Matt 11:5), quoting Isaiah 35:5-6 and 61:1. Every healing of a blind person in the Gospels is an enacted quotation of Isaiah&rsquo;s patach-promise: the age of open eyes has arrived."
        }
    ],

    "language_notes": (
        "<p>Isaiah&rsquo;s most remarkable linguistic feature is <strong>the trisagion of 6:3</strong> — &ldquo;holy, holy, holy&rdquo; (qadosh qadosh qadosh). Hebrew has no grammatical superlative form; it creates the &ldquo;most X&rdquo; meaning through intensification, repetition, or construct chains. A double repetition (&ldquo;holy, holy&rdquo;) would be the superlative; the <em>triple</em> repetition of 6:3 is a superlative of the superlative — an unprecedented intensification in the OT. The linguistic uniqueness of the trisagion signals a theological breakthrough: what the seraphim are declaring about God exceeds the grammatical resources of Hebrew. The same linguistic pressure appears in Isaiah&rsquo;s signature title &ldquo;the Holy One of Israel&rdquo; (qedosh yisrael), where the noun qedosh is used as a divine name — not just an attribute — yoking transcendent holiness to covenant particularity: <em>this</em> Holy One belongs specifically to Israel.</p>"
        "<p>Chapters 40-55 exhibit <strong>the characteristic rhetoric of the comfort oracle</strong> — a genre that Isaiah develops with unusual sophistication. The pivot at 40:1-2 (&ldquo;Comfort, comfort my people, says your God&rdquo;) shifts from the messenger formula (&ldquo;thus says the LORD&rdquo;) to the divine direct address. The doubled imperative &ldquo;comfort, comfort&rdquo; (nachamu nachamu) is a Hebrew intensifier — the doubled verb of urgency that appears in 51:9 (&ldquo;Awake, awake&rdquo;) and 52:1 (&ldquo;Awake, awake&rdquo;) and 52:11 (&ldquo;Depart, depart&rdquo;). This anaphoric doubling is a literary signature of the comfort section: the repeated imperatives create a mounting urgency that something decisive is about to happen. The section also employs the <em>rib</em> (lawsuit/courtroom) form extensively: God calls the nations to a cosmic tribunal (41:1; 43:9; 44:8) to establish his unique claim to foreknowledge and divine authority — a forensic rhetoric without parallel in the other prophets.</p>"
        "<p>The <strong>four Servant Songs</strong> (42:1-9; 49:1-13; 50:4-11; 52:13-53:12) form a literary sub-sequence within chapters 40-53 with their own internal development. Each Song begins with a distinctive introduction: the third-person divine announcement in 42:1 (&ldquo;Behold my servant, whom I uphold&rdquo;); the Servant&rsquo;s first-person self-identification in 49:1 (&ldquo;Listen to me, O coastlands, hear, you peoples from afar&rdquo;); the Servant&rsquo;s first-person account of suffering in 50:4; and the return to third-person divine announcement in 52:13 (&ldquo;Behold, my servant shall act wisely&rdquo;). The shift in 52:13-53:12 to the &lsquo;we&rsquo; voice (&ldquo;who has believed what he heard from us?...we esteemed him stricken&rdquo;) — a communal confession that recognizes, in retrospect, the meaning of the Servant&rsquo;s suffering — is one of the most rhetorically sophisticated moves in the Hebrew prophets. The community that confesses in 53:1-6 is making a theological discovery mid-speech: the one we dismissed is the one who bore our guilt.</p>"
        "<p>Isaiah&rsquo;s <strong>new exodus vocabulary</strong> — concentrated in chapters 40-55 — deliberately recalls the Exodus narrative through specific lexical choices. The &ldquo;way&rdquo; (derek) in the wilderness (40:3), the &ldquo;water&rdquo; (mayim) in the dry place (41:18; 44:3), the &ldquo;miraculous&rdquo; (pele) acts (29:14), the divine leading through the wilderness (48:21) — all reference the specific vocabulary of the Exodus. Isaiah 43:16-17: &ldquo;who makes a way (derek) in the sea, a path in the mighty waters, who brings forth chariot and horse&rdquo; — the Red Sea crossing. Isaiah 43:18-19: &ldquo;Remember not the former things... Behold, I am doing a new thing&rdquo; — the new exodus surpasses the first. This intertextual strategy means that readers who know their Exodus narrative will hear a familiar vocabulary deployed for a new situation: the return from Babylon is a second Exodus, more glorious than the first, anticipating the final eschatological redemption. The NT completes the chain: John 1:23 applies Isaiah 40:3 to John the Baptist; Matthew 3:3 applies it to Jesus&rsquo; ministry; and Revelation applies the new exodus imagery to the final liberation of the people of God.</p>"
    ),

    "reception": (
        "<p><strong>Patristic:</strong> The early church called Isaiah &ldquo;the fifth Gospel&rdquo; — the fullest OT witness to Christ. Justin Martyr (c. 155 AD) built his apologetic for Christianity on Isaiah 53 and the Servant Songs, arguing that the suffering and resurrection of Jesus were prophesied centuries before the events. Irenaeus used Isaiah extensively in <em>Against Heresies</em> to demonstrate the unity of OT and NT against Marcionite dualism. Jerome&rsquo;s commentary on Isaiah (c. 408 AD) remains one of his most extensive; he read the entire book Christologically. Augustine drew on Isaiah&rsquo;s holiness-theology for his doctrine of divine sovereignty and human unworthiness. Origen proposed reading Isaiah in the context of his threefold schema of biblical reading: the literal, moral, and spiritual senses — all three operating simultaneously in Isaiah&rsquo;s dense poetry.</p>"
        "<p><strong>Reformation:</strong> Calvin wrote what many consider his greatest biblical commentary on Isaiah — begun in his lectures and published in 1551. Calvin maintained the Christological reading while insisting on the historical referent: Isaiah addressed Ahaz and Hezekiah, and the text&rsquo;s meaning must be established in its historical context before the fuller fulfillment in Christ is traced. Luther similarly preached Isaiah as a prophetic Gospel, with particular attention to Isaiah 53 as the clearest OT statement of substitutionary atonement. The Reformation&rsquo;s recovery of the literal sense did not reduce Isaiah to historical description — it made the historical particularity the ground for the Christological reading rather than an obstacle to it.</p>"
        "<p><strong>Modern debates:</strong> The critical question of whether chapters 1-39 and 40-66 (or 40-55 and 56-66) are by one or more authors — &ldquo;Deutero-Isaiah&rdquo; and &ldquo;Trito-Isaiah&rdquo; — has dominated modern scholarship since J.C. Döderlein&rsquo;s 1775 argument. The debate turns on whether predictive prophecy (the naming of Cyrus in 44:28; 45:1) is possible. Evangelical scholarship (Alec Motyer, J. Oswalt) defends unity on canonical and linguistic grounds. Brevard Childs&rsquo;s canonical approach argued that regardless of compositional history, the book functions as a theological unity — and the NT&rsquo;s consistent attribution of all 66 chapters to &ldquo;Isaiah the prophet&rdquo; (John 12:38-41) supports reading it as such.</p>"
    ),

    "reading_guide": (
        "<p><strong>Read Isaiah 6 before chapter 1.</strong> The vision of the enthroned, thrice-holy Lord (6:1-13) is the theological foundation for everything else: Isaiah&rsquo;s woe at his own uncleanness, the coal that purges his lips, and the commission to speak to deaf ears establish both the message and the pattern. All of Isaiah&rsquo;s later announcements — judgment on sin, comfort for the exiles, the Servant&rsquo;s suffering — are elaborations of what was given in the throne room. Understanding who God is in chapter 6 determines what the judgment of chapters 1-39 means and what the comfort of chapters 40-66 costs.</p>"
        "<p><strong>Track the four Servant Songs as a connected sequence:</strong> 42:1-9 (the Servant&rsquo;s call and mission), 49:1-13 (the worldwide scope of the mission, even when Israel refuses it), 50:4-11 (the Servant&rsquo;s obedient suffering despite rejection), 52:13-53:12 (vicarious death, burial, and exaltation). Read them in one sitting before working through the chapters around them. Isaiah 53 is the book&rsquo;s Christological pinnacle — the community&rsquo;s retrospective confession that the despised one bore their guilt. The NT quotes it more than any other OT passage except the Psalms.</p>"
        "<p><strong>Don&rsquo;t read chapters 40-66 as a different, gentler book.</strong> The comfort of the second half is grounded in the holiness and judgment of the first half — the same God who condemned Judah for forsaking the Holy One of Israel (1:4) is the God who redeems Zion by justice (1:27). The refrain &ldquo;the Holy One of Israel&rdquo; runs through both halves: 1:4 (accusation) and 41:14 (redemption). The most common misreading of Isaiah is to treat chapters 40-55 as the &ldquo;real&rdquo; Isaiah and chapters 1-39 as uncomfortable background; in fact, the comfort means nothing apart from the severity of the prior judgment.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('isaiah')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('isaiah', merged)

main()
