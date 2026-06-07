"""
Book Study Data — Daniel
book_id: daniel
lang: hebrew

Run: python3 scripts/build-book-study-daniel.py

Notes:
- Author group: Major in author-freq-hebrew.json; peaks are generic, so vocabulary
  selected from Daniel's specific theological and linguistic features
- Daniel is bilingual: Hebrew (1:1–2:4a, 8–12) and Aramaic (2:4b–7:28)
- Most vocabulary here is Aramaic (H-codes in Strong's cover both Hebrew and Aramaic)
- All translit fields blank in glossary — supplied manually
- H7328 rāz (mystery) appears 9× in Daniel and nowhere else in OT; the most
  distinctive Daniel-specific lexeme in the entire Hebrew Bible
- H5012 nava (prophesy) and H995 biyn (understand) already used — bînāh (H998)
  and śĕkal (H7920) are available and cover Daniel's wisdom theme
- Many obvious Daniel codes already used: H2377 (vision), H3519 (glory),
  H2534 (wrath), H7307 (spirit), H6726 (Zion), H894 (Babel)
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
    "bookId": "daniel",

    "key_vocabulary": [
        {
            "code": "H7328",
            "lemma": "רָז",
            "translit": "rāz",
            "gloss": "mystery",
            "significance": "רָז (rāz, &lsquo;to attenuate, hide; a mystery&rsquo;) is the word that defines Daniel&rsquo;s entire prophetic enterprise — and it appears nowhere else in the Hebrew Bible except Daniel. The Aramaic rāz (a Persian loanword) occurs nine times in Daniel 2–4. Daniel 2:27-28: &ldquo;No wise men, enchanters, magicians, or astrologers can show to the king the mystery (rāzāʾ) that the king has asked, but there is a God in heaven who reveals mysteries (gāleh razin), and he has made known to King Nebuchadnezzar what will be in the latter days.&rdquo; The rāz is not merely a hidden piece of information — it is a divinely withheld revelation about the arc of history, specifically the succession of world empires and the coming of God&rsquo;s everlasting kingdom. Daniel&rsquo;s claim is that human wisdom (the Babylonian wise men) cannot access it by any technique; only God who governs history can reveal what history means. The NT&rsquo;s <em>mystērion</em> in Paul (Rom 16:25-26; Eph 3:3-6; Col 1:26-27) develops directly from the Daniel rāz-tradition: &ldquo;the mystery hidden for ages and generations but now revealed to his saints&rdquo; (Col 1:26). In Paul, the rāz is the inclusion of the Gentiles in the body of Christ — the eschatological secret that Daniel&rsquo;s four-kingdom sequence pointed toward without spelling out."
        },
        {
            "code": "H2493",
            "lemma": "חֵלֶם",
            "translit": "ḥēlem",
            "gloss": "dream",
            "significance": "חֵלֶם (ḥēlem, &lsquo;a dream&rsquo;) is the vehicle of divine revelation in Daniel&rsquo;s Aramaic chapters — given not to the prophet but to the Gentile kings. Daniel 2:1: &ldquo;Nebuchadnezzar had dreams (ḥelmoh).&rdquo; Daniel 4:5: &ldquo;I saw a dream that made me afraid; as I lay in bed the fantasies and the visions of my head alarmed me.&rdquo; The ḥēlem-dreams of chapters 2 and 4 are both given to Nebuchadnezzar and both require Daniel&rsquo;s interpretive gift (pĕšar). The king cannot interpret his own dream — this is Daniel&rsquo;s theological point: God gives the rāz (mystery) in visionary form to those who hold power over history, but the meaning requires a representative of the God who controls history. The Hebrew equivalent ḥălôm (H2472) appears in Genesis (Joseph&rsquo;s dreams), Deuteronomy (warnings about false dreamers), and the Psalms. Daniel&rsquo;s use of the Aramaic ḥēlem signals that these dreams are given to Gentile kings about Gentile empires — an expansion of the dream-vehicle beyond Israel to the nations that hold Israel captive. The NT&rsquo;s Magi (Matt 2:12) and Joseph (Matt 2:13, 19, 22) receive warning dreams, and the Joel 2:28 promise (Acts 2:17: &ldquo;your old men shall dream dreams&rdquo;) fulfills in the Pentecost outpouring of the Spirit."
        },
        {
            "code": "H4437",
            "lemma": "מַלְכוּ",
            "translit": "malkû",
            "gloss": "kingdom",
            "significance": "מַלְכוּ (malkû, Aramaic: &lsquo;dominion, kingdom&rsquo;) is Daniel&rsquo;s central theological noun — the word for the divine kingdom that supersedes all human ones. Daniel 2:44: &ldquo;And in the days of those kings the God of heaven will set up a kingdom (malkûtāʾ) that shall never be destroyed... it shall break in pieces all these kingdoms and bring them to an end, and it shall stand forever.&rdquo; Daniel 4:3: &ldquo;His kingdom (malkûtēh) is an everlasting kingdom.&rdquo; Daniel 7:14: the son of man receives &ldquo;a kingdom (malkû), that all peoples, nations, and languages should serve him; his dominion is an everlasting dominion, which shall not pass away, and his kingdom one that shall not be destroyed.&rdquo; The contrast throughout Daniel is between human kingdoms — represented by metals in Nebuchadnezzar&rsquo;s statue (ch. 2) and by beasts (ch. 7) — and the divine malkû that is eternal. Human malkû is large but temporary; divine malkû is small at first (the stone &ldquo;cut without hands&rdquo; — 2:34) but grows to fill the whole earth (2:35). Jesus&rsquo;s announcement &ldquo;the kingdom of God is at hand&rdquo; (Mark 1:15 — <em>hē basileia tou theou</em>) is the Greek equivalent of Aramaic <em>malkûtēh dĕ-ʾElāhāʾ</em> — the declaration that the Daniel-promised divine malkû has begun arriving in his person."
        },
        {
            "code": "H6591",
            "lemma": "פְּשַׁר",
            "translit": "pĕšar",
            "gloss": "interpretation",
            "significance": "פְּשַׁר (pĕšar, &lsquo;an interpretation&rsquo;) is Daniel&rsquo;s divinely given gift — the ability to decode the rāz-mysteries given in dream and vision form. Daniel 2:4-7: the Chaldeans demand both the dream and its interpretation (pĕšrāʾ) — a double demand the king makes deliberately to verify that the interpretation is genuine. Daniel 5:16: Belshazzar offers rewards to whoever can read and show the interpretation of the handwriting on the wall. Daniel&rsquo;s pĕšar is not analysis or exegesis in the modern sense — it is apocalyptic decoding: the correspondence between heavenly vision and earthly historical reality. The same word (pĕšar) became the technical term for a specific Dead Sea Scroll genre: the <em>pesher</em> commentaries (Pesher Habakkuk, Pesher Nahum) that interpret prophetic texts as direct references to the Qumran community&rsquo;s contemporary history. This use of pĕšar (fulfillment-in-our-time interpretation) is the direct background for NT interpretive formulas: &ldquo;this is that which was spoken by the prophet Joel&rdquo; (Acts 2:16) and Matthew&rsquo;s fulfillment citations (&ldquo;this was to fulfill what was spoken by the prophet&rdquo; — Matt 1:22). In both cases, a prior word&rsquo;s hidden referent is decoded in the light of present events — the Daniel pĕšar method applied to Jesus."
        },
        {
            "code": "H2372",
            "lemma": "חָזָה",
            "translit": "ḥāzāh",
            "gloss": "behold",
            "significance": "חָזָה (ḥāzāh, &lsquo;to gaze at, perceive; to have a vision&rsquo;) is the primary visionary verb of Daniel 7–12, used to introduce each of the great visions. Daniel 7:2: &ldquo;I saw (ḥāzeʾ hāwêt) in my vision by night.&rdquo; Daniel 7:13: &ldquo;I saw (ḥāzeʾ hāwêt) in the night visions, and behold, with the clouds of heaven there came one like a son of man.&rdquo; The Aramaic ḥāzāh is cognate with Hebrew ḥāzāh (same code), which appears in prophetic titles: Amos &ldquo;saw&rdquo; (Amos 1:1) and Micah &ldquo;saw&rdquo; (Mic 1:1). In Daniel, ḥāzāh functions as an evidential marker of authentic prophetic reception — Daniel did not reason to these conclusions by analysis; he saw them in vision. The combination of ḥāzāh (vision) with pĕšar (interpretation) constitutes Daniel&rsquo;s epistemological framework: divine truth is given in visionary form and decoded by divinely granted interpretation. Neither is available by human wisdom. The NT&rsquo;s &ldquo;revelation&rdquo; (apokalypsis — the unveiling of what was hidden) is the Greek equivalent of Daniel&rsquo;s ḥāzāh-experience; John&rsquo;s &ldquo;I was in the Spirit&rdquo; (Rev 1:10) and &ldquo;I saw&rdquo; (Rev 5:1) repeat the Danielic ḥāzāh posture."
        },
        {
            "code": "H998",
            "lemma": "בִּינָה",
            "translit": "bînāh",
            "gloss": "understanding",
            "significance": "בִּינָה (bînāh, &lsquo;understanding, discernment&rsquo;) is Daniel&rsquo;s characteristic wisdom gift in the Hebrew sections of the book. Daniel 1:20: &ldquo;in every matter of wisdom and understanding (bînāh) the king inquired of them, he found them ten times better than all the magicians and enchanters in his realm.&rdquo; Daniel 9:22: the angel Gabriel comes &ldquo;to give you insight and understanding (lĕhaskîl bînāh).&rdquo; Daniel 10:1: Daniel &ldquo;understood the word and had understanding (bînāh) of the vision.&rdquo; Bînāh is not mere intellectual capacity — it is the divinely granted discernment to see through the surface of events to their theological meaning. It appears in Isaiah 11:2 as one of the Spirit&rsquo;s gifts to the Davidic Branch, and in Proverbs 2:3 as the goal of wisdom education. Daniel&rsquo;s bînāh operates precisely at the intersection where ordinary wisdom fails: Nebuchadnezzar&rsquo;s wise men have technical skill but no bînāh for the rāz. Daniel&rsquo;s bînāh is simultaneously a personal gift and a communal function — in 12:10, those with bînāh will understand what the wicked cannot. Ephesians 1:17-18 (&ldquo;the spirit of wisdom and of revelation in the knowledge of him, having the eyes of your hearts enlightened&rdquo;) is Paul&rsquo;s pneumatological equivalent of Daniel&rsquo;s bînāh — understanding given from above, not achieved from below."
        },
        {
            "code": "H5943",
            "lemma": "עִלַּי",
            "translit": "ʿillay",
            "gloss": "Most High",
            "significance": "עִלַּי (ʿillay, Aramaic: &lsquo;supreme, the Most High&rsquo;) is Daniel&rsquo;s preferred title for God in the Aramaic chapters — and one of its most theologically pointed choices. Daniel 4:2: &ldquo;It has seemed good to me to show the signs and wonders that the Most High God (ʾElāhāʾ ʿilyāʾ) has done for me.&rdquo; Daniel 7:18: &ldquo;But the saints of the Most High (qaddîšê ʿelyônîn) shall receive the kingdom and possess the kingdom forever.&rdquo; Daniel 7:25: &ldquo;He shall speak words against the Most High (ʿillay) and shall wear out the saints of the Most High (qaddîšê ʿelyônîn).&rdquo; The title ʿillay / ʿelyôn emphasizes God&rsquo;s transcendence above all earthly power structures. In Daniel&rsquo;s setting — the courts of Babylon and Persia, where kings claim divinity — the insistence that the ʿillay rules over all kingdoms is a direct challenge to imperial theology. Nebuchadnezzar&rsquo;s great doxology in 4:34-35 is his forced acknowledgment of the ʿillay: &ldquo;I blessed the Most High and praised and honored him who lives forever, for his dominion is an everlasting dominion.&rdquo; The NT&rsquo;s &ldquo;Son of the Most High&rdquo; (Luke 1:32 — <em>hyios hypsistou</em>) places Jesus in the Daniel-ʿillay tradition as the one who inherits the everlasting kingdom promised to the ʿillay&rsquo;s saints."
        },
        {
            "code": "H1247",
            "lemma": "בַּר",
            "translit": "bar",
            "gloss": "son",
            "significance": "בַּר (bar, Aramaic: &lsquo;a son, grandson; the heir&rsquo;) is the Aramaic word in Daniel 7:13&rsquo;s most consequential phrase: <strong>bar enash</strong> (&ldquo;son of man&rdquo; — literally, &ldquo;son of a human being&rdquo;). Daniel 7:13: &ldquo;I saw in the night visions, and behold, with the clouds of heaven there came one like a <em>bar enash</em>, and he came to the Ancient of Days and was presented before him.&rdquo; In context, &ldquo;one like a bar enash&rdquo; means &ldquo;one with a human appearance&rdquo; — in contrast to the four beasts (a lion, a bear, a leopard, a monster) that represented the pagan empires. The human-figured one receives from the Ancient of Days the eternal malkû that the beast-empires had temporarily held. The irony is pointed: the beast-empires appear powerful and terrifying, while the human-figured one appears merely creaturely — yet it is the creaturely-looking figure who receives eternal dominion. Jesus adopted &ldquo;Son of Man&rdquo; (Aramaic bar enash, Greek <em>huios tou anthrōpou</em>) as his primary self-designation, explicitly citing Daniel 7:13 at his trial (Mark 14:62: &ldquo;you will see the Son of Man seated at the right hand of Power and coming with the clouds of heaven&rdquo;). Jesus identifies himself as the one who receives the Ancient of Days&rsquo; eternal kingdom — not someday but in the present moment of his exaltation."
        },
        {
            "code": "H5957",
            "lemma": "עָלַם",
            "translit": "ʿālam",
            "gloss": "everlasting",
            "significance": "עָלַם (ʿālam, Aramaic: &lsquo;remote time — past or future indefinitely; adverb, forever&rsquo;) is the qualifier that distinguishes the divine kingdom from all human kingdoms in Daniel. Daniel 2:44: the God of heaven will set up a kingdom &ldquo;that shall never be destroyed... it shall stand forever (leʿālam).&rdquo; Daniel 4:3: &ldquo;his kingdom is an everlasting kingdom (malkût ʿālam), and his dominion endures from generation to generation.&rdquo; Daniel 7:14: the son of man receives &ldquo;an everlasting dominion (šolṭān ʿālam), which shall not pass away.&rdquo; Daniel 7:27: &ldquo;his kingdom shall be an everlasting kingdom (malkût ʿālam), and all dominions shall serve and obey him.&rdquo; The repetition of ʿālam as the kingdom&rsquo;s defining attribute is deliberate: human empires are defined by conquest and duration, but all eventually fall; God&rsquo;s kingdom is defined by ʿālam-permanence. The four metals of Nebuchadnezzar&rsquo;s statue degrade from gold to iron-clay precisely to show that human power declines over time — only the malkû that is ʿālam endures. The NT&rsquo;s <em>aiōnios</em> (eternal) in &ldquo;eternal life&rdquo; (John 3:16) and &ldquo;eternal kingdom&rdquo; (2 Pet 1:11) is the Greek equivalent of Daniel&rsquo;s ʿālam-malkû — the kingdom that does not fall because it does not depend on human succession."
        },
        {
            "code": "H7920",
            "lemma": "שְׂכַל",
            "translit": "śĕkal",
            "gloss": "make wise",
            "significance": "שְׂכַל (śĕkal, &lsquo;to be circumspect, intelligent; causatively to make wise, give understanding&rsquo;) appears at Daniel&rsquo;s climactic eschatological promise. Daniel 12:3: &ldquo;And those who are wise (<em>hammaśkilîm</em>) shall shine like the brightness of the sky above; and those who turn many to righteousness, like the stars forever and ever.&rdquo; Daniel 1:4 introduces Daniel and his friends as men &ldquo;endowed with insight&rdquo; (meśkilîm). Daniel 12:10: &ldquo;the wise (<em>maśkilîm</em>) shall understand.&rdquo; The śĕkal-root names a specific eschatological vocation: the maśkilîm are not merely intelligent — they are the ones who make others wise in understanding God&rsquo;s action in history, who remain faithful under imperial pressure and teach the same faithfulness. Their reward (Dan 12:3) is stellar glory — the most vivid positive eschatology in the OT outside of the resurrection promise two verses earlier (12:2). The same root appears as the verb in Isaiah 52:13 (&ldquo;Behold, my servant shall act wisely [yaśkîl]&rdquo;) — the Servant of YHWH acts with the same insight that characterizes Daniel&rsquo;s faithful community. The Dead Sea Scrolls community called their leader the <em>Maskil</em> (the one who gives wisdom), using the same śĕkal-form as their self-understanding as Daniel&rsquo;s maśkilîm."
        },
        {
            "code": "H3046",
            "lemma": "יְדַע",
            "translit": "yĕdaʿ",
            "gloss": "know",
            "significance": "יְדַע (yĕdaʿ, Aramaic: &lsquo;to know, ascertain by seeing&rsquo;) is Daniel&rsquo;s Aramaic parallel to Hebrew yādaʿ (already used) and appears in the characteristic &ldquo;so that you/they may know&rdquo; formula that structures the court narratives. Daniel 3:18: Shadrach, Meshach, and Abednego tell Nebuchadnezzar: &ldquo;Be it known (yĕdîaʿ lehewēʾ) to you, O king, that we will not serve your gods.&rdquo; Daniel 3:29: after the furnace, Nebuchadnezzar decrees that all nations should know (lĕhôdaʿûtkôn) that no god can rescue like the God of Israel. Daniel 4:25: Nebuchadnezzar will &ldquo;know (tindaʿ) that the Most High rules the kingdom of men.&rdquo; Daniel 6:26: Darius commands that men tremble before the living God — &ldquo;for he is the living God, enduring forever.&rdquo; The yĕdaʿ of Daniel parallels Ezekiel&rsquo;s Hebrew recognition formula (veyādĕʿû kî anî YHWH) but operates in a Gentile key: Nebuchadnezzar, Darius, and the surrounding nations are brought to the knowledge of the ʿillay through the demonstrated protection and vindication of Daniel and his friends. This cross-cultural knowing — the Gentile emperor acknowledging the God of Israel — is Daniel&rsquo;s most direct anticipation of the Gentile mission."
        },
        {
            "code": "H2376",
            "lemma": "חֵזֵו",
            "translit": "ḥezû",
            "gloss": "vision",
            "significance": "חֵזֵו (ḥezû, Aramaic: &lsquo;a sight, vision&rsquo;) is the Aramaic term for the visual content of Daniel&rsquo;s dream-revelations — specifically in the phrase &ldquo;visions of my/your head&rdquo; (ḥezyônê rēʾšāk / rēʾšî). Daniel 2:28: &ldquo;Your dream and the visions of your head (ḥezyônê rēʾšāk) as you lay in bed are these.&rdquo; Daniel 4:5: &ldquo;the visions of my head (ḥezyônê rēʾšî) alarmed me.&rdquo; Daniel 7:1: &ldquo;Daniel saw a dream and visions of his head (ḥezyônê rēʾšēh) as he lay in his bed.&rdquo; The phrase &ldquo;visions of the head&rdquo; is unique to Daniel in the OT — it locates the visionary experience precisely in the mind of the dreamer during sleep, distinguishing it from waking vision (ḥāzōn) and from direct verbal revelation (davar). This phenomenological precision matters: Daniel&rsquo;s apocalyptic claims are grounded in specific dated experiences, not literary compositions. Each of the great visions is anchored to a specific year of a specific king&rsquo;s reign (Dan 7:1 — &ldquo;in the first year of Belshazzar&rdquo;; Dan 8:1 — &ldquo;in the third year of the reign of King Belshazzar&rdquo;; Dan 9:1; Dan 10:1). The ḥezû-grammar of historically anchored night vision becomes the template for John&rsquo;s &ldquo;I was in the Spirit on the Lord&rsquo;s day&rdquo; (Rev 1:10) — a similarly anchored, specific-occasion claim of visionary reception."
        }
    ],

    "language_notes": (
        "<p>Daniel is the only Hebrew Bible book with <strong>two languages</strong> in a theologically structured arrangement. The book opens in Hebrew (1:1–2:4a), shifts to Aramaic when the Chaldean counselors speak to Nebuchadnezzar (2:4b), continues in Aramaic through chapter 7, then returns to Hebrew for chapters 8–12. The Aramaic section (2:4b–7:28) forms a literary <strong>chiastic ring</strong>: chapter 2 (statue, four kingdoms) ↔ chapter 7 (four beasts, son of man); chapter 3 (fiery furnace) ↔ chapter 6 (lions&rsquo; den); chapter 4 (Nebuchadnezzar humbled) ↔ chapter 5 (Belshazzar judged). The language choice is theological: Aramaic was the international diplomatic language of the ancient Near East — the lingua franca of the empire. By writing chapters 2–7 in Aramaic, Daniel addresses the Gentile nations in their own language, making claims about God&rsquo;s sovereignty that are not limited to Israel. The Hebrew sections (1 and 8–12) address Israel directly, in the covenant language. The book&rsquo;s structure embodies its message: God&rsquo;s kingdom concerns both Israel and the nations.</p>"
        "<p>The Aramaic of Daniel 2–7 is <strong>Official Aramaic</strong> (also called Imperial Aramaic) — the administrative language of the Persian Empire, preserved in Ezra, the Elephantine papyri, and diplomatic correspondence from the 5th–6th centuries BC. It contains loanwords from Persian (<em>rāz</em> — mystery; <em>paṯbag</em> — food), Babylonian/Akkadian (<em>kaśdāʾê</em> — Chaldeans), and Greek (names of musical instruments in Dan 3:5). The apocalyptic vocabulary of Daniel&rsquo;s Aramaic section is distinctive: <em>rāz</em> (mystery), <em>pĕšar</em> (interpretation), <em>malkû</em> (kingdom), and <em>ʿālam</em> (forever) are the four load-bearing theological nouns. Taken together, they express Daniel&rsquo;s theological claim: history contains hidden mysteries (<em>rāz</em>) about which kingdom will endure forever (<em>ʿālam</em>), and those mysteries require divine interpretation (<em>pĕšar</em>) to know that only God&rsquo;s kingdom (<em>malkû</em>) will ultimately stand.</p>"
        "<p>The phrase <strong>bar enash</strong> (&ldquo;son of man&rdquo;) in Daniel 7:13 is grammatically a simile, not a title: &ldquo;one <em>like</em> a son of man&rdquo; (kĕbar enash) — someone who appeared human, in contrast to the four beasts. In Aramaic, bar enash simply means &ldquo;a human being,&rdquo; just as Hebrew ben adam means &ldquo;mortal.&rdquo; The theological weight comes from context: this human-figured one receives from the Ancient of Days the eternal dominion that the beast-empires had temporarily held. The figure is simultaneously humble-appearing (human, not bestial) and supremely powerful (receives universal, eternal dominion). When Jesus adopts &ldquo;Son of Man&rdquo; as his primary self-designation — particularly in sayings about authority (Matt 9:6), suffering (Mark 8:31), and coming (Mark 14:62) — he takes Daniel&rsquo;s simile and transforms it into a Christological title, claiming to be the one who receives what Daniel 7 promises. The NT&rsquo;s &ldquo;Son of Man&rdquo; idiom is impossible to understand without reading it against this Aramaic Daniel background.</p>"
        "<p>The Hebrew of Daniel 8–12 introduces a distinct vocabulary set for the later visions. Chapter 9 contains the most theologically compressed Hebrew in Daniel: the prayer of confession (9:4-19) is saturated with covenant vocabulary (<em>ḥăṭāʾ</em> sin, <em>rāšaʿ</em> wickedness, <em>ṣedeq</em> righteousness, <em>ḥesed</em> steadfast love) before moving to the seventy-weeks oracle (9:24-27), which has been the most debated passage in OT scholarship for two millennia. Chapter 12:2 contains the clearest OT statement of bodily resurrection: &ldquo;Many of those who sleep in the dust of the earth shall awake, some to everlasting life (ḥayyê ʿôlam), and some to shame and everlasting contempt.&rdquo; Both Hebrew ʿôlam (forever) and Aramaic ʿālam appear in Daniel, covering both language sections with the same theological weight: the eternal destiny of the resurrected is expressed in the same ʿālam-vocabulary as the eternal kingdom.</p>"
    ),

    "reception": (
        "<p><strong>Jewish tradition:</strong> Daniel is placed in the third division of the Hebrew Bible (the Writings, Kĕtûvîm) rather than the Prophets — a canonical anomaly that Jewish interpreters explained by noting Daniel served in a royal court rather than functioning as a classic preaching prophet. The Dead Sea Scrolls community at Qumran had multiple copies of Daniel and treated it as authoritative, developing the <em>pesher</em> interpretive method directly from Daniel&rsquo;s pĕšar-tradition. Josephus called Daniel &ldquo;one of the greatest of the prophets&rdquo; (Antiquities 10.11.7), noting that Daniel not only predicted future events but specified when they would occur. The seventy-weeks oracle (Dan 9:24-27) has generated more interpretive literature than almost any OT passage — Josephus applied it to the Roman destruction of Jerusalem (AD 70), while others applied it to the Maccabean crisis.</p>"
        "<p><strong>Patristic debate:</strong> The third-century pagan philosopher Porphyry wrote a systematic attack on Daniel, arguing that it was composed in the Maccabean period (164–165 BC) and was therefore vaticinium ex eventu (prophecy after the fact) rather than genuine prediction. Jerome wrote his massive <em>Commentary on Daniel</em> specifically to refute Porphyry, arguing for sixth-century composition and genuine predictive prophecy. Jerome&rsquo;s identification of the four kingdoms (Babylon, Media-Persia, Greece, Rome) and his reading of the &ldquo;little horn&rdquo; as the Antichrist became the standard patristic interpretation. The early church used Daniel 7:13 as its primary proof-text for Jesus&rsquo;s divine authority — at his trial before the Sanhedrin, Jesus&rsquo;s citation of Daniel 7:13 was understood immediately as a claim to divine sonship, triggering the accusation of blasphemy.</p>"
        "<p><strong>Modern scholarship:</strong> The authorship question remains the defining debate in Daniel studies. The critical consensus (since H. H. Rowley&rsquo;s <em>Darius the Mede and the Four World Empires</em>, 1935) argues for Maccabean-era composition of chapters 7–12. Conservative scholars (E. J. Young, <em>The Prophecy of Daniel</em>, 1949; John Goldingay, <em>Daniel</em>, WBC, 1989; Tremper Longman III) defend an earlier date, citing Jesus&rsquo;s authentication of Daniel&rsquo;s authorship (Matt 24:15: &ldquo;the abomination of desolation spoken of by the prophet Daniel — let the reader understand&rdquo;) as decisive evidence. Stephen Miller&rsquo;s NAC commentary (1994) and Ernest Lucas&rsquo;s AOTC commentary (2002) represent opposite positions on the date while both engaging seriously with the Hebrew and Aramaic evidence.</p>"
    ),

    "reading_guide": (
        "<p><strong>Read chapters 1–6 as the theological foundation before engaging the visions.</strong> The court narratives establish what Daniel&rsquo;s God is like through demonstration rather than declaration: the food test (ch. 1), the furnace (ch. 3), and the lions&rsquo; den (ch. 6) show God protecting faithful covenant people in a pagan court. This is the experiential ground for the abstract claims of chapters 7–12: God controls kingdoms because he has been shown to control furnaces. Read the court narratives not as children&rsquo;s stories but as resistance theology — a diaspora survival manual for how to maintain covenant faithfulness while serving inside an empire that demands compromise.</p>"
        "<p><strong>Chapter 7 is the interpretive key to the entire book.</strong> Return to it multiple times: first when you reach it, then again after chapters 8–12, then alongside Matthew 24 and Revelation 13. Chapter 7 synthesizes Daniel 2&rsquo;s four-kingdom sequence (metals → statue → stone) into visionary form (beasts → Ancient of Days → son of man) and adds the crucial element of Daniel 2: the transfer of eternal dominion to the human-figured one. The &ldquo;bar enash&rdquo; who receives the kingdom in 7:13-14 is the answer to every beast that precedes him. Jesus&rsquo;s use of this figure as his primary self-title means that Daniel 7 is the single most important OT passage for understanding the NT&rsquo;s Christology.</p>"
        "<p><strong>Approach chapters 8–12 with interpretive patience.</strong> These chapters have generated more scholarly disagreement than almost any other OT section, with their chronological symbols read as referring variously to the Maccabean crisis, the Roman Empire, or the end of history. The book tells Daniel to &ldquo;seal up the book until the time of the end&rdquo; (12:4). Read them for their theological core — God will vindicate his people, the wise will shine, the resurrection is coming — and hold the chronological questions lightly.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('daniel')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('daniel', merged)

main()
