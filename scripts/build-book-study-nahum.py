"""
Book Study Data — Nahum
book_id: nahum
lang: hebrew

Run: python3 scripts/build-book-study-nahum.py

Notes:
- Author group: Minor — peaks are generic; vocabulary selected from Nahum's
  distinctive divine-warrior and judgment vocabulary
- Key codes already used: H2534 chemah (wrath), H8045 shamad (destroy),
  H7307 ruach (spirit/wind), H6726 tsiyon (Zion), H7725 shuv (return)
- H5358 naqam (avenge): appears THREE times in 1:2 — the only such triple in the OT
- H639 aph (anger): Nahum quotes the Exodus 34 covenant formula ("slow to anger")
  but strips the mercy clauses — a deliberate theological inversion
- H1319 basar (good news): Nah 1:15 = Isa 52:7 = Rom 10:15 — the gospel chain
- H7393 rekev + H5483 sus: the battle description in chs. 2-3 is among the most
  cinematically vivid in the OT; Nahum's sûs is the divine-warrior's weapon reversed
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
    "bookId": "nahum",

    "key_vocabulary": [
        {
            "code": "H7065",
            "lemma": "קָנָא",
            "translit": "qānāʾ",
            "gloss": "jealous",
            "significance": "קָנָא (qānāʾ, &lsquo;to be jealous or zealous — an intensity of exclusive attachment; from the same root as the word for a reddening face&rsquo;) opens Nahum&rsquo;s theological declaration: Nahum 1:2: &ldquo;The LORD is a jealous (qannōʾ) and avenging God.&rdquo; The divine qannōʾ (the intensive adjective form) describes covenantal exclusivity — the same attribute invoked in Exodus 20:5 (&ldquo;for I the LORD your God am a jealous God (El qannāʾ)&rdquo;) and in Exodus 34:14 (&ldquo;for YHWH, whose name is Jealous (qannāʾ), is a jealous God&rdquo;). The divine jealousy in Nahum is not pique but the necessary correlate of covenantal sovereignty: the entire earth belongs to YHWH, and empires that devastate his world are trespassing on territory that is not theirs. Assyria&rsquo;s cruelty is not merely a political crime but a theological one — it is executed against nations and peoples under YHWH&rsquo;s ownership and care. The same qannōʾ that drove YHWH to judge Israel&rsquo;s unfaithfulness (Deut 29:20: &ldquo;the LORD&rsquo;s jealousy (qinʾātô) would smoke against that man&rdquo;) now drives judgment against the empire that has been destroying his world. Paul uses the same relational dynamic in 2 Corinthians 11:2: &ldquo;I am jealous for you with a godly jealousy (zēlō... theou zēlō)&rdquo; — the intense exclusive attachment that refuses to share what is beloved with a destroyer is the same attribute in both Testaments."
        },
        {
            "code": "H5358",
            "lemma": "נָקַם",
            "translit": "nāqam",
            "gloss": "avenge",
            "significance": "נָקַם (nāqam, &lsquo;to avenge, take vengeance, punish — properly to grudge; used of judicial retribution&rsquo;) appears three times in a single verse — Nahum 1:2: &ldquo;The LORD takes vengeance (nōqēm YHWH) and is wrathful; the LORD takes vengeance (nōqēm YHWH) on his adversaries and keeps wrath for his enemies.&rdquo; This triple repetition is unparalleled in the OT as a stylistic device — the verb is hammered three times as if to ensure no one mistakes the announcement for a conditional threat. The theological background is Deuteronomy 32:35,41,43: &ldquo;Vengeance is mine (lî nāqām), and recompense... I will take vengeance (ʾāqōm) on my adversaries... he avenges (nāqam) the blood of his children.&rdquo; The reservation of nāqam to God is the OT&rsquo;s explicit teaching that human vengeance usurps the divine role. The triple nāqam in Nahum 1:2 is therefore both a comfort (judgment will come) and a warning against human impatience: YHWH&rsquo;s slow-to-anger character (1:3) means the nāqam is certain but not instantaneous. The NT&rsquo;s &ldquo;Vengeance is mine, I will repay, says the Lord&rdquo; (Rom 12:19; Heb 10:30) cites Deuteronomy 32:35 but stands in the same theological tradition as Nahum&rsquo;s triple declaration: divine retribution is real, certain, and properly reserved to God rather than executed by humans impatient for it."
        },
        {
            "code": "H2195",
            "lemma": "זַעַם",
            "translit": "zaʿam",
            "gloss": "indignation",
            "significance": "זַעַם (zaʿam, &lsquo;properly, froth at the mouth — figuratively, fury, especially God&rsquo;s displeasure against sin&rsquo;) appears in Nahum 1:6: &ldquo;Who can stand before his indignation (liznāmô)? Who can endure the heat of his anger? His wrath is poured out like fire, and the rocks are broken asunder by him.&rdquo; The zaʿam is not mere displeasure but the full force of divine indignation — the froth-at-the-mouth image suggests overwhelming passion. In the OT, zaʿam is consistently used for God&rsquo;s anger against specific objects of injustice: Isaiah 10:5 (&ldquo;the rod of my anger, the staff of my indignation (zaʿmî)&rdquo; — directed against Assyria itself, in a striking reversal of Nahum); Isaiah 30:27; Daniel 8:19; Zechariah 1:12. Nahum 1:6&rsquo;s rhetorical question — &ldquo;who can stand before his indignation?&rdquo; — expects the answer &ldquo;no one,&rdquo; and the answer is immediately given by the melting mountains and the dissolved rocks. The zaʿam against Nineveh is balanced by the miśgāv of 1:7: the same divine character that unleashes indignation against the oppressor is a refuge for those who trust him. The zaʿam and the ṭôv (goodness) are not contradictions but the single holiness of God directed at its appropriate objects."
        },
        {
            "code": "H639",
            "lemma": "אַף",
            "translit": "ʾap",
            "gloss": "anger",
            "significance": "אַף (ʾap, &lsquo;the nostril — from the snorting of anger; hence, anger itself, wrath&rsquo;) appears in Nahum 1:3 in the covenant formula: &ldquo;The LORD is slow to anger (ʾɛrɛk ʾappayim) and great in power, and the LORD will by no means clear the guilty.&rdquo; The phrase ʾɛrɛk ʾappayim (&ldquo;long of nostril&rdquo; — i.e., the nostrils do not flare quickly with anger) is drawn directly from the covenant formula of Exodus 34:6: &ldquo;The LORD, a God merciful and gracious, slow to anger (ʾɛrɛk ʾappayim), and abounding in steadfast love and faithfulness.&rdquo; Nahum&rsquo;s use is a deliberate quotation with a deliberate omission: the mercy clauses (&ldquo;merciful and gracious... abounding in steadfast love&rdquo;) are stripped away, leaving only &ldquo;slow to anger&rdquo; and adding &ldquo;will by no means clear the guilty.&rdquo; This is not a contradiction of Exodus 34 but its other face: the Exodus formula already contains both mercy (34:6-7a) and judgment (&ldquo;who will by no means clear the guilty,&rdquo; 34:7b). Nahum is invoking the full formula while foregrounding its judgment side, because &ldquo;slow to anger&rdquo; does not mean &ldquo;never angry&rdquo; — it means the ʾap is certain when it finally comes. Jonah 4:2 used the same Exodus formula as his reason for fleeing: YHWH was so gracious he might spare Nineveh. Nahum 1:3 is the same formula a century and a half later, announcing that the patience implied by ʾɛrɛk ʾappayim has now run its full course."
        },
        {
            "code": "H5492",
            "lemma": "סוּפָה",
            "translit": "sûpāh",
            "gloss": "whirlwind",
            "significance": "סוּפָה (sûpāh, &lsquo;a hurricane — from sûp, to sweep away; the violent swirling storm that leaves nothing in its path&rsquo;) appears in Nahum 1:3: &ldquo;His way is in whirlwind (bĕsûpāh) and storm (ûbiśʿārāh), and the clouds are the dust of his feet.&rdquo; The sûpāh is the storm-theophany image of the divine warrior: Psalm 83:15 (&ldquo;as the flame sets the mountains ablaze, so may you pursue them with your tempest (bĕsûpātɛkā)&rdquo;); Isaiah 29:6; Jeremiah 23:19; Job 38:1 (&ldquo;the LORD answered Job out of the whirlwind (sûpāh)&rdquo;). In Nahum, the sûpāh-imagery deliberately subverts the Canaanite theology of the ancient Near East: Baal was the Syro-Palestinian storm-deity, whose control of rain and wind gave Canaan its religious imagination. Assyria&rsquo;s imperial religion implicitly claimed divine backing. Nahum announces that YHWH — not Baal, not Ashur — is the actual storm-lord, whose sûpāh is not mythology but the real force that governs natural catastrophe. The clouds are &ldquo;the dust of his feet&rdquo; — the imagery makes the storm-front the Lord&rsquo;s travel-wake, the meteorological by-product of his approach. In the context of a judgment oracle on Nineveh, the sûpāh becomes the vehicle of YHWH&rsquo;s military arrival: he comes against the city as a hurricane comes against the land."
        },
        {
            "code": "H2895",
            "lemma": "טוֹב",
            "translit": "ṭôv",
            "gloss": "good",
            "significance": "טוֹב (ṭôv, &lsquo;good — in the widest sense; pleasant, beautiful, excellent, morally right; when used of God, the fullness of his beneficial character&rsquo;) appears in Nahum 1:7 — the pastoral pivot of the book: &ldquo;The LORD is good (ṭôv YHWH), a stronghold in the day of trouble; he knows those who take refuge in him.&rdquo; The placement of this verse is architecturally deliberate: it stands between the portrait of YHWH&rsquo;s devastating power (1:3-6 — the storm, the melting mountains, the rocks broken asunder) and the announcement of Nineveh&rsquo;s complete destruction (1:8: &ldquo;with an overwhelming flood he will make a complete end of the adversaries&rdquo;). The ṭôv is not despite the judgment but through it: YHWH&rsquo;s goodness is precisely what explains why he judges evil with absolute thoroughness. A God who tolerates the indefinite crushing of the innocent is not good. The Psalter uses ṭôv YHWH as its repeated doxological refrain (Pss 100:5; 106:1; 107:1; 118:1,29; 136:1: &ldquo;Give thanks to the LORD, for he is good, for his steadfast love endures forever&rdquo;). Nahum places this same ṭôv-declaration within an oracle of judgment, not in spite of the context but because of it: the good news for those who are being destroyed is that YHWH&rsquo;s goodness necessarily includes opposition to everything that destroys them."
        },
        {
            "code": "H4869",
            "lemma": "מִשְׂגָּב",
            "translit": "miśgāv",
            "gloss": "stronghold",
            "significance": "מִשְׂגָּב (miśgāv, &lsquo;a high fort, stronghold, refuge — from śāgav, to be high, inaccessible; a place of safety by elevation&rsquo;) appears in Nahum 1:7: &ldquo;The LORD is good, a stronghold (miśgāv) in the day of trouble; he knows those who take refuge in him.&rdquo; The miśgāv is a specific type of refuge — a high, naturally fortified place that enemies cannot reach. It appears throughout the Psalter as one of the key metaphors for divine protection: Psalm 9:9 (&ldquo;The LORD is a stronghold for the oppressed, a stronghold in times of trouble&rdquo;); Psalm 18:2 (&ldquo;my God, my rock, in whom I take refuge, my shield, and the horn of my salvation, my stronghold (miśgabbî)&rdquo;); Psalm 46:7,11 (&ldquo;The LORD of hosts is with us; the God of Jacob is our fortress (miśgāv) for us&rdquo;). In Nahum, the miśgāv stands in deliberate contrast to Nineveh&rsquo;s physical fortifications — the massive walls and gates that are about to be overwhelmed (2:6: &ldquo;the river gates are opened; the palace melts away&rdquo;). The book&rsquo;s readers, Judeans who had experienced the terror of Assyrian military power, are being told that their actual safety rests not on political alliances or military defense but on YHWH&rsquo;s miśgāv. The ṭôv-miśgāv combination in 1:7 is Nahum&rsquo;s pastoral word to the suffering: the same God who destroys Nineveh is a high place of refuge for those who take shelter in him."
        },
        {
            "code": "H1319",
            "lemma": "בָּשַׂר",
            "translit": "bāśar",
            "gloss": "bring good news",
            "significance": "בָּשַׂר (bāśar, &lsquo;properly, to be fresh and full; hence to announce glad tidings — to bring good news&rsquo;) appears in Nahum 1:15: &ldquo;Behold, upon the mountains, the feet of him who brings good news (mĕbaśśēr), who publishes peace!&rdquo; This verse is the direct source — or parallel tradition — for Isaiah 52:7: &ldquo;How beautiful upon the mountains are the feet of him who brings good news (mĕbaśśēr), who publishes peace, who brings good news of happiness, who publishes salvation, who says to Zion, &lsquo;Your God reigns!&rsquo;&rdquo; Paul quotes Isaiah 52:7 in Romans 10:15 as the description of the gospel preacher: &ldquo;How beautiful are the feet of those who preach the good news (euangelizomenōn)!&rdquo; This creates a direct chain: Nahum 1:15 → Isaiah 52:7 → Romans 10:15 — and behind all three stands the same theological structure: the defeat of the great oppressor is &ldquo;good news.&rdquo; In Nahum, the mĕbaśśēr brings news that Nineveh has fallen. In Isaiah, the mĕbaśśēr brings news that YHWH reigns. In Paul, the euangelizomenoi bring news that Jesus has died and risen, defeating the ultimate enemy. The Greek word εὐαγγέλιον (euangelion — gospel, good news) is the direct translation of the Hebrew bĕśôrāh, the noun of bāśar. The &ldquo;gospel&rdquo; is etymologically the Nahum 1:15 announcement: the tyrant has fallen."
        },
        {
            "code": "H7272",
            "lemma": "רֶגֶל",
            "translit": "rɛgɛl",
            "gloss": "foot",
            "significance": "רֶגֶל (rɛgɛl, &lsquo;the foot as used in walking; by implication, a step; the lower extremity&rsquo;) appears in Nahum 1:15: &ldquo;Behold, upon the mountains, the feet (raglê) of him who brings good news.&rdquo; The rɛgɛl here is the herald&rsquo;s feet visible on the mountain ridges — in the ancient world before telegraph or radio, news traveled by messengers on foot, and the image of a figure cresting a mountain ridge was the first sign that news was coming. The speed and visibility of the rɛgɛl on the mountain communicates urgency: this is not a slow report but urgent news. Isaiah 52:7 preserves the same rɛgɛl image in nearly identical language: &ldquo;How beautiful upon the mountains are the feet (raglê) of him who brings good news.&rdquo; Paul&rsquo;s quotation in Romans 10:15 (&ldquo;How beautiful are the feet (hoi podes) of those who preach the good news&rdquo;) makes the rɛgɛl an image of gospel proclamation across the ancient tradition. The &ldquo;beautiful feet&rdquo; are beautiful not in themselves but because of what they carry: the announcement of the tyrant&rsquo;s fall, the reign of YHWH, and ultimately the resurrection of Jesus. Nahum&rsquo;s rɛgɛl on the mountain is the first canonical instantiation of what becomes one of Scripture&rsquo;s most enduring images of mission and proclamation."
        },
        {
            "code": "H7393",
            "lemma": "רֶכֶב",
            "translit": "rɛḵɛv",
            "gloss": "chariot",
            "significance": "רֶכֶב (rɛḵɛv, &lsquo;a vehicle, specifically a war-chariot; by extension, the team or cavalry; the chariot-force as a unit&rsquo;) is central to Nahum&rsquo;s vivid battle description: Nahum 2:3-4: &ldquo;The chariots (rekev) come with flashing metal on the day of his preparation, and the cypress spears are brandished. The chariots (merkāvôt) race madly through the streets; they rush to and fro through the squares; they gleam like torches; they dart like lightning.&rdquo; The rekev was the ancient world&rsquo;s most powerful military weapon — the equivalent of the tank — and Assyria had built the largest chariot force in the Near East. Reliefs from Nineveh itself (now in the British Museum) show exactly the scenes Nahum describes: chariots at full gallop, warriors in disciplined formation. In Nahum 2, the chariots racing through Nineveh&rsquo;s streets are not Assyrian — they are the attacker&rsquo;s vehicles. The reversal is deliberate: the military technology Nineveh used to terrify the nations is now being driven through Nineveh&rsquo;s own streets. The theological point is that no military power is absolute: the rekev that Nineveh trusted falls before YHWH&rsquo;s rekev. Psalm 20:7: &ldquo;Some trust in chariots (rekev) and some in horses, but we trust in the name of the LORD our God.&rdquo; Nahum demonstrates that the Psalm&rsquo;s confession is not wishful thinking but historical reality."
        },
        {
            "code": "H5483",
            "lemma": "סוּס",
            "translit": "sûs",
            "gloss": "horse",
            "significance": "סוּס (sûs, &lsquo;a horse — probably so called from its swiftness; used extensively in military contexts&rsquo;) appears in Nahum&rsquo;s most concentrated burst of battle imagery: Nahum 3:2-3: &ldquo;the crack of the whip, and rumble of the wheel, galloping horse (sûs) and bounding chariot! Horsemen charging, flashing sword and glittering spear, hosts of slain, heaps of corpses, dead bodies without end — they stumble over the bodies!&rdquo; This passage is remarkable for its sound poetry: the Hebrew onomatopoeia of wheels rumbling, hooves striking, weapons clashing creates an acoustic portrait of a city being overwhelmed. The sûs appears in the OT&rsquo;s most important military contexts: Isaiah 31:1 (&ldquo;Woe to those who go down to Egypt for help and rely on horses (sûsîm), who trust in chariots&rdquo;); Job 39:19-25 (YHWH&rsquo;s speech on the war-horse — &ldquo;Do you give the horse (sûs) his might? Do you clothe his neck with a mane?&rdquo;); Revelation 6:2-8 (the four horsemen — sûs becomes the apocalyptic vehicle of divine judgment). In Nahum, the sûs whose galloping is the signature of Assyrian military supremacy becomes the signature of Nineveh&rsquo;s destruction: the same sound that once announced Assyria&rsquo;s coming against the nations now announces judgment against Nineveh itself."
        },
        {
            "code": "H7617",
            "lemma": "שָׁבָה",
            "translit": "šābāh",
            "gloss": "take captive",
            "significance": "שָׁבָה (šābāh, &lsquo;to transport into captivity — to carry off as prisoners of war&rsquo;) is the verb of Nineveh&rsquo;s reversal: Nahum 3:10: &ldquo;Yet she (Thebes/No-Amon) became an exile (gôlāh), she went into captivity (lašĕvî); her infants were dashed in pieces at the head of every street; for her honored men lots were cast, and all her great men were bound in chains.&rdquo; Nahum uses Thebes&rsquo; fate as the mirror image of Nineveh&rsquo;s coming šābāh: if Thebes, protected by the Nile and its allied nations, could be taken captive, so can Nineveh. The šābāh is specifically the Assyrian empire&rsquo;s signature weapon against its enemies: the Assyrians practiced mass deportation (šābāh) as imperial policy — moving entire populations to prevent nationalism and mix conquered peoples with others. Israel&rsquo;s northern kingdom was destroyed by exactly this šābāh in 722 BC (2 Kgs 17:6: &ldquo;the king of Assyria carried (wayyegl) Israel away to Assyria&rdquo;). Nahum announces the šābāh of the šābāh-ers: the empire that transported others will be transported. This is the OT&rsquo;s consistent framework for divine judgment at the national scale — measure for measure, what Nineveh did to others will be done to Nineveh. Obadiah 15: &ldquo;As you have done, it shall be done to you; your deeds shall return on your own head.&rdquo; The fall of Nineveh in 612 BC was so complete that the city was never rebuilt — the šābāh was total and permanent."
        }
    ],

    "language_notes": (
        "<p>Nahum is the OT&rsquo;s most concentrated <strong>sustained poetic oracle against a foreign nation</strong>, and its poetry is among the most technically sophisticated in the prophetic corpus. Chapter 1 contains a <strong>partial acrostic</strong> (aleph through kaph) — each verse or half-verse beginning with successive letters of the Hebrew alphabet — embedded within the theological hymn of 1:2-8. The acrostic is not complete or perfectly regular, but scholars have identified it as deliberate, suggesting a formalized liturgical context for the opening material. The significance is that Nahum&rsquo;s theology is not spontaneous rage but shaped poetry: the announcement of divine judgment is given the careful structure of a praise psalm. Judgment announced with aesthetic precision is judgment that reflects the ordered character of the Judge.</p>"
        "<p>The structure of chapters 2-3 is <strong>cinematic</strong> in a way unusual for ancient literature. Nahum 2:3-4: &ldquo;the chariots come with flashing metal... the chariots race madly through the streets; they rush to and fro through the squares; they gleam like torches; they dart like lightning.&rdquo; Nahum 3:2-3: &ldquo;the crack of the whip, and rumble of the wheel, galloping horse and bounding chariot! Horsemen charging, flashing sword and glittering spear, hosts of slain, heaps of corpses.&rdquo; The battle description uses <strong>sound poetry</strong> — the Hebrew onomatopoeia of wheels rumbling, whips cracking, and hooves striking creates an acoustic portrait of a siege. Scholars have noted that excavations of ancient Nineveh, including its famous reliefs (now in the British Museum), show exactly the military imagery Nahum describes: the chariots at gallop, the organized chaos of siege warfare. Nahum appears to have had detailed knowledge of Assyrian military practice, which lends the poetry a journalistic specificity entirely absent from generic judgment oracles.</p>"
        "<p>Nahum&rsquo;s most important literary technique is the <strong>inversion of the covenant formula</strong> at 1:3. The Exodus 34:6-7 formula — &ldquo;merciful and gracious, slow to anger, abounding in steadfast love and faithfulness&rdquo; — is the OT&rsquo;s most repeated description of YHWH&rsquo;s character. Nahum cites only one clause (&ldquo;slow to anger&rdquo;) and strips the mercy context entirely, adding instead &ldquo;will by no means clear the guilty.&rdquo; This is not contradiction but selection: Exodus 34:7 itself contains both &ldquo;abounding in steadfast love&rdquo; and &ldquo;who will by no means clear the guilty.&rdquo; Nahum isolates the judgment face of the covenant formula because the point of the book is that YHWH&rsquo;s patience — which is real and was demonstrated at Jonah&rsquo;s mission — has a limit, and the limit has been reached. The same God who spared Nineveh when it repented in Jonah&rsquo;s day now announces its permanent destruction after a century and a half of resumed predation. The covenant formula serves both faces of YHWH&rsquo;s character; which face is relevant depends on which direction history has moved.</p>"
    ),

    "reception": (
        "<p><strong>The Nahum-Isaiah-Paul chain:</strong> Nahum 1:15 (&ldquo;the feet of him who brings good news&rdquo;) is quoted or independently parallel in Isaiah 52:7, which Paul then cites in Romans 10:15 to describe gospel proclamation. This creates one of the longest intertextual chains in Scripture: the announcement of Nineveh&rsquo;s fall in Nahum becomes the eschatological announcement of YHWH&rsquo;s reign in Isaiah, which becomes the announcement of Christ&rsquo;s resurrection in Paul. The Greek word <em>euangelion</em> (gospel) is the direct translation of the Hebrew <em>bĕśôrāh</em> (good news); the word &ldquo;gospel&rdquo; is etymologically the Nahum 1:15 announcement. Early Christian commentators noted this chain: Theodore of Mopsuestia and Jerome both wrote on the Nahum-Isaiah connection.</p>"
        "<p><strong>Nahum at Qumran:</strong> The Nahum Pesher (4QpNah) found among the Dead Sea Scrolls is one of the most significant early Jewish commentaries on a prophetic book. The Qumran community read Nahum&rsquo;s oracle against Nineveh as a commentary on their own contemporary enemies — the Seleucids and the Kittim (Romans). 4QpNah contains the clearest extant reference to crucifixion in pre-Christian Jewish texts, interpreting Nahum 2:13 as a reference to a historical figure who &ldquo;hangs men alive.&rdquo; The Pesher demonstrates that Nahum was actively read as prophetic commentary on current political events, not merely as historical record.</p>"
        "<p><strong>Modern discomfort and theological recovery:</strong> Nahum is among the most difficult books for modern readers who have absorbed a therapeutic or mercy-only understanding of God. The book contains no call to repentance, no offer of conditional escape — it announces Nineveh&rsquo;s total destruction as certain and final. Walter Brueggemann and others have argued that reading Nahum requires recovering the perspective of the victim: for those crushed by Nineveh, the announcement of judgment is not incompatible with love but is love&rsquo;s necessary form. Miroslav Volf (&lsquo;Exclusion and Embrace&rsquo;) makes a parallel argument: a God who cannot say &ldquo;no&rdquo; to ultimate evil is a God who cannot be trusted by those who suffer from it.</p>"
    ),

    "reading_guide": (
        "<p><strong>Read Nahum as Jonah&rsquo;s sequel.</strong> Jonah preached to Nineveh and the city repented — YHWH relented from judgment and Jonah was furious. Nahum, writing roughly 150 years later, announces the judgment Jonah feared: Nineveh has reverted to its characteristic cruelty, and this time there is no conditional escape. The two books are the OT&rsquo;s sustained meditation on the relationship between divine patience and divine justice. Jonah shows that YHWH&rsquo;s mercy is genuinely universal. Nahum shows that YHWH&rsquo;s patience, though long, is not unlimited. Both books are necessary to understand either one.</p>"
        "<p><strong>Read 1:7 as the pastoral center.</strong> The book&rsquo;s most important verse is tucked in the middle of the opening theological hymn: &ldquo;The LORD is good, a stronghold in the day of trouble; he knows those who take refuge in him.&rdquo; This verse answers the question the book implicitly raises: if YHWH is avenging and his indignation is irresistible, what does that mean for people who trust him? The answer is that the same character that makes him dangerous to Nineveh makes him a refuge for those under Nineveh&rsquo;s boot. The divine wrath and the divine goodness are the same holiness directed at different objects.</p>"
        "<p><strong>Read the battle poetry as theology, not gratuitous violence.</strong> The vivid military imagery of chapters 2-3 is not glorification of war but the rhetorical form of prophetic certainty: Nahum describes Nineveh&rsquo;s fall as if watching it happen, to communicate that it is as good as done. The heaps of corpses and the wailing inhabitants are the real consequences of Nineveh&rsquo;s century of predation on others — the description is not sadistic but just. The book ends with a question: &ldquo;For upon whom has not come your unceasing evil?&rdquo; (3:19). For those who suffered under Nineveh, the answer is self-evident — and so is the relief.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('nahum')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('nahum', merged)

main()
