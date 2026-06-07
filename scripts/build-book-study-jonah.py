"""
Book Study Data — Jonah
book_id: jonah
lang: hebrew

Run: python3 scripts/build-book-study-jonah.py

Notes:
- Author group: Minor — peaks are generic; vocabulary selected from Jonah's narrative
- Jonah is the only Minor Prophet that is entirely narrative (no direct oracles)
- Key codes already used: H7451 ra (evil), H5162 nacham (relent), H2015 haphak (overturn),
  H6965 qum (arise), H7307 ruach (spirit/wind), H2617 hesed, H7355 racham, H7585 sheol
- H4487 manah (appoint) is the key sovereignty verb — all nature is "appointed" by YHWH
- H2347 chus (pity) is the climactic verb of the unanswered final question (4:11)
- H7021 qiqayon (gourd): unique to Jonah; the plant that is the book's final object lesson
- H8415 tehom (the deep): the primordial abyss — Jonah's descent goes to the bottom of creation
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
    "bookId": "jonah",

    "key_vocabulary": [
        {
            "code": "H1272",
            "lemma": "בָּרַח",
            "translit": "bāraḥ",
            "gloss": "flee",
            "significance": "בָּרַח (bāraḥ, &lsquo;to bolt — to flee suddenly, to escape; used of rapid, frightened departure&rsquo;) is the verb of Jonah&rsquo;s commission-flight: Jonah 1:3: &ldquo;But Jonah rose to flee (livrōaḥ) to Tarshish from the presence of the LORD.&rdquo; Jonah 1:10: &ldquo;he was fleeing (bōrēaḥ) from the presence of the LORD.&rdquo; The bāraḥ is theologically impossible, and Jonah knows it — he tells the sailors in 1:9 that he fears &ldquo;the LORD, the God of heaven, who made the sea and the dry land.&rdquo; A prophet who worships the God of the sea and the dry land is fleeing on the sea from the God who made it. The very ship and the very sea he uses to escape are in YHWH&rsquo;s hands. The bāraḥ also echoes Adam hiding from the presence of YHWH after the fall (Gen 3:8 — &ldquo;the man and his wife hid themselves from the presence of the LORD God&rdquo;). Jonah&rsquo;s flight is not atheistic disbelief but a prophet&rsquo;s covenantal refusal — he knows God, knows what God will do, and flees anyway. This makes the bāraḥ more culpable than ordinary ignorance. The NT&rsquo;s &ldquo;where shall I go from your Spirit? Or where shall I flee (brach, in Hebrew OT sense) from your presence?&rdquo; (Ps 139:7) is the theological answer to Jonah&rsquo;s bāraḥ — a question that already knows its answer."
        },
        {
            "code": "H3220",
            "lemma": "יָם",
            "translit": "yām",
            "gloss": "sea",
            "significance": "יָם (yām, &lsquo;a sea — the large body of water; by extension, the west; the primordial ocean&rsquo;) is the setting and instrument of YHWH&rsquo;s pursuit of Jonah through chapters 1–2. Jonah 1:4: &ldquo;the LORD hurled a great wind upon the sea (yām), and there was a mighty tempest on the sea.&rdquo; Jonah 1:11-12,15: the sailors ask what to do to quiet the sea (yām); Jonah tells them to throw him in; they do, and &ldquo;the sea ceased from its raging.&rdquo; The yām in Jonah is not chaos but YHWH&rsquo;s obedient instrument: the Creator who made the sea (1:9) commands it as a weapon and a conveyor. The irony is that Jonah — a prophet of YHWH — flees by yām from the God who rules the yām, while the pagan sailors aboard his ship end up fearing the LORD and making vows to him (1:16). The sea converts the Gentiles; the prophet is heading in the opposite direction. Jonah 2:3: &ldquo;you cast me into the deep, into the heart of the seas (yāmmîm).&rdquo; In the prayer, the yām becomes the domain of death from which YHWH rescues Jonah. The NT&rsquo;s Jesus sleeping through a storm at sea (Matt 8:24-26) and stilling it at a word — &ldquo;what sort of man is this, that even the winds and the sea obey him?&rdquo; — places Jesus where YHWH is in Jonah: sovereign over the yām that terrified the sailors."
        },
        {
            "code": "H591",
            "lemma": "אֳנִיָּה",
            "translit": "ʾŏniyyāh",
            "gloss": "ship",
            "significance": "אֳנִיָּה (ʾŏniyyāh, &lsquo;a ship — the large ocean-going vessel&rsquo;) is the vehicle of Jonah&rsquo;s attempted flight: Jonah 1:3: &ldquo;he found a ship (ʾŏniyyāh) going to Tarshish; so he paid the fare and went down into it.&rdquo; Jonah 1:4: &ldquo;the ship threatened to break up.&rdquo; The ʾŏniyyāh functions as the anti-fish: a human-made vessel for human flight, contrasted with YHWH&rsquo;s appointed creature (the dāg) for divine purposes. The sailors aboard the ʾŏniyyāh are Gentiles who end up doing everything right — they pray, they resist throwing Jonah in, they ask YHWH&rsquo;s forgiveness before doing so, and they make vows to YHWH afterward (1:14-16). The ʾŏniyyāh&rsquo;s pagan crew is one of Jonah&rsquo;s sustained ironies: the people with no covenant with YHWH respond to him with more reverence than the covenant prophet. Jonah is asleep in the hold (1:5) while the captain pleads with him to pray — the sailor telling the prophet to pray to his God is an inversion of every prophetic expectation. The ʾŏniyyāh&rsquo;s crew&rsquo;s conversion (1:16: &ldquo;the men feared the LORD exceedingly, and they offered a sacrifice to the LORD and made vows&rdquo;) is the first Gentile conversion in the narrative — and it happens despite Jonah, not because of him."
        },
        {
            "code": "H1709",
            "lemma": "דָּג",
            "translit": "dāg",
            "gloss": "fish",
            "significance": "דָּג (dāg, &lsquo;a fish — often used collectively for fish; from the verb dāgāh, to multiply&rsquo;) is the book&rsquo;s most famous element: Jonah 1:17: &ldquo;And the LORD appointed a great fish (dāg gādôl) to swallow Jonah.&rdquo; The dāg is not Jonah&rsquo;s punishment but his <em>rescue</em> — without the fish, Jonah drowns. The dāg saves him from the consequences of his own flight by means of an experience that feels like death. Jonah 2:1 describes what it produces: Jonah prays. The fish is the instrument of compelled prayer; the sea and the darkness force the prophet back to YHWH. The dāg is also YHWH&rsquo;s creature, given a specific commission: to swallow, contain, and disgorge. Jonah 2:10: &ldquo;And the LORD spoke to the fish, and it vomited Jonah out upon the dry land.&rdquo; YHWH speaks to the fish and is obeyed; Jonah has been less obedient than the fish throughout. Jesus explicitly cites the dāg in Matthew 12:40: &ldquo;just as Jonah was three days and three nights in the belly of the great fish, so will the Son of Man be three days and three nights in the heart of the earth.&rdquo; The dāg&rsquo;s belly becomes the OT type for the tomb: descent-into-death followed by vomiting-out-onto-dry-land is the shape of resurrection. The dāg is not a side issue but the book&rsquo;s structural center: Jonah goes down (1:3,5,17) until the dāg brings him up."
        },
        {
            "code": "H990",
            "lemma": "בֶּטֶן",
            "translit": "bɛṭɛn",
            "gloss": "belly",
            "significance": "בֶּטֶן (bɛṭɛn, &lsquo;the belly — especially the womb; also the bosom or body of anything hollow&rsquo;) appears twice in Jonah 2 at the theological core of the chapter: Jonah 1:17 (MT 2:1): &ldquo;Jonah was in the belly (bɛṭɛn) of the fish three days and three nights.&rdquo; Jonah 2:2: &ldquo;out of the belly (mibɛṭɛn) of Sheol I cried, and you heard my voice.&rdquo; The double use of bɛṭɛn equates the fish&rsquo;s belly with the belly of Sheol (the realm of the dead): the fish is not a temporary aquarium but a death-chamber, a grave that has swallowed Jonah whole. The prayer of Jonah 2 is spoken from inside death — it is a resurrection-prayer prayed before the resurrection: &ldquo;Yet I shall again look upon your holy temple&rdquo; (2:4). The bɛṭɛn-Sheol equation is the theological basis for Jesus&rsquo;s citation of the sign of Jonah: three days in the bɛṭɛn of the fish = three days in &ldquo;the heart of the earth.&rdquo; The bɛṭɛn is also the womb: the same word for the place of death is the word for the place of birth. Jonah&rsquo;s emergence from the bɛṭɛn is birth-language as much as resurrection-language — the recommissioned prophet vomited onto dry land is beginning again."
        },
        {
            "code": "H8415",
            "lemma": "תְּהוֹם",
            "translit": "tĕhôm",
            "gloss": "the deep",
            "significance": "תְּהוֹם (tĕhôm, &lsquo;an abyss — the surging mass of subterranean and oceanic water; the deep; specifically the primordial ocean&rsquo;) appears in Jonah 2:5: &ldquo;The waters closed in over me to take my life; the deep (tĕhôm) surrounded me; weeds were wrapped about my head.&rdquo; In the OT, tĕhôm is the word used for the primordial deep of Genesis 1:2 (&ldquo;darkness was over the face of the deep&rdquo;), for the waters of the flood (Gen 7:11: &ldquo;all the fountains of the great deep burst forth&rdquo;), and for the cosmic waters that YHWH controls (Ps 33:7: &ldquo;he gathers the waters of the sea as a heap; he puts the deeps in storehouses&rdquo;). Jonah&rsquo;s descent goes to the tĕhôm — the bottom of the created order, the place of primordial chaos before the Word separated water from land. To be in the tĕhôm is to be in the realm where creation itself is undone. Jonah 2:6: &ldquo;I went down to the land whose bars closed upon me forever; yet you brought up my life from the pit, O LORD my God.&rdquo; The ascent from tĕhôm is YHWH&rsquo;s creative act: the same God who called order from chaos in Genesis 1 calls Jonah out of the tĕhôm. The NT&rsquo;s &ldquo;the abyss&rdquo; (<em>abyssos</em> — the Greek equivalent of tĕhôm) in Revelation 9:1-2 and 20:3 carries this Joeline theology: the deep is YHWH&rsquo;s domain, not an autonomous power."
        },
        {
            "code": "H6862",
            "lemma": "צַר",
            "translit": "ṣar",
            "gloss": "distress",
            "significance": "צַר (ṣar, &lsquo;narrow, tight; used figuratively of difficulty and distress; the constricted place&rsquo;) opens Jonah&rsquo;s prayer: Jonah 2:2: &ldquo;I called out to the LORD, out of my distress (miṣṣārātî), and he answered me; out of the belly of Sheol I cried, and you heard my voice.&rdquo; The ṣar is the combination of physical constriction (the fish&rsquo;s belly — literally narrow and enclosed) and spiritual crisis — the prophet at the bottom of the sea with seaweed wrapped around his head, utterly without resource. The ṣar is what produces the prayer: throughout chapters 1–2, Jonah has been silent while everyone around him prays (the sailors in 1:5; the captain in 1:6). Only in the absolute ṣar of the fish&rsquo;s belly does Jonah call out to YHWH. The word ṣar appears in many of the psalms of lament that Jonah&rsquo;s prayer echoes (Ps 18:6; 107:6; 120:1) — it is the vocabulary of the one who has nowhere else to turn. The NT&rsquo;s &ldquo;in my distress (<em>thlipsis</em>) I called upon the Lord&rdquo; (2 Cor 1:4-5) and &ldquo;out of my anguish I cried to the Lord&rdquo; (various psalms) continue the ṣar-theology: distress is not the opposite of prayer but its occasion, the narrow place that turns the face toward God."
        },
        {
            "code": "H4487",
            "lemma": "מָנָה",
            "translit": "mānāh",
            "gloss": "appoint",
            "significance": "מָנָה (mānāh, &lsquo;properly, to weigh out; by implication, to allot or appoint; to number&rsquo;) is YHWH&rsquo;s sovereignty verb across all four chapters of Jonah. The formula <em>way-mānneh YHWH</em> (&ldquo;and the LORD appointed&rdquo;) recurs four times: Jonah 1:17: &ldquo;And the LORD appointed (way-mānneh) a great fish to swallow Jonah.&rdquo; Jonah 4:6: &ldquo;Now the LORD God appointed (way-mānneh) a plant and made it come up over Jonah.&rdquo; Jonah 4:7: &ldquo;But when dawn came up the next day, God appointed (way-mānneh) a worm.&rdquo; Jonah 4:8: &ldquo;When the sun rose, God appointed (way-mānneh) a scorching east wind.&rdquo; The verb mānāh implies a careful weighing-out — not a casual assignment but a measured allotment suited exactly to its purpose. YHWH appoints the fish as Jonah&rsquo;s rescuer-and-classroom; the plant as temporary comfort; the worm as the plant&rsquo;s destruction; the east wind as Jonah&rsquo;s exposure. Each appointment is calibrated for the lesson Jonah needs to learn. The mānāh-pattern shows a God who governs not only the grand movements of history but the small operations of worms and plants, using every creature as an instrument of instruction. Daniel 5:26 uses the same word in a different register: &ldquo;Mene, Mene — God has numbered (mĕnāh) your kingdom and brought it to an end.&rdquo;"
        },
        {
            "code": "H7107",
            "lemma": "קָצַף",
            "translit": "qāṣap",
            "gloss": "rage",
            "significance": "קָצַף (qāṣap, &lsquo;to crack off, i.e. to burst out in rage; to be wrathful&rsquo;) is Jonah&rsquo;s emotional signature in chapter 4. Jonah 4:1: &ldquo;But it displeased Jonah exceedingly (wayyēraʿ el-Yônāh rāʿāh gĕdôlāh), and he was angry (wayyiḥar lô).&rdquo; Jonah 4:4: &ldquo;And the LORD said, &lsquo;Do you do well to be angry?&rsquo;&rdquo; Jonah 4:9: &ldquo;&lsquo;Do you do well to be angry (haheiteiv chara) for the plant?&rsquo; And he said, &lsquo;Yes, I do well to be angry, angry enough to die.&rsquo;&rdquo; The qāṣap running through ch. 4 is the book&rsquo;s most revealing psychological portrait: Jonah&rsquo;s anger at God&rsquo;s mercy is displaced onto the withered plant. YHWH asks twice whether Jonah&rsquo;s anger is justified (4:4,9) and receives no answer to the first, and a defiant &ldquo;yes&rdquo; to the second. The irony is exquisite: Jonah confesses in 4:2 that he <em>knew</em> God was gracious, which was precisely why he fled — he wanted Nineveh destroyed and knew YHWH might spare it. His qāṣap is the anger of a man who is right about God&rsquo;s character and enraged by it. The NT&rsquo;s older brother in the prodigal son parable (Luke 15:28: &ldquo;he was angry and refused to go in&rdquo;) is a direct Jonah-echo — the one who has been faithful and served is angry that the Father shows mercy to the returning wastrel."
        },
        {
            "code": "H7021",
            "lemma": "קִיקָיוֹן",
            "translit": "qîqāyôn",
            "gloss": "plant",
            "significance": "קִיקָיוֹן (qîqāyôn, &lsquo;the gourd or castor-oil plant — likely the Ricinus communis, which grows extremely quickly and provides dense shade&rsquo;) appears only in Jonah 4:6-10 — four times, and nowhere else in the Hebrew Bible. Jonah 4:6: &ldquo;Now the LORD God appointed a plant (qîqāyôn) and made it come up over Jonah, that it might be a shade over his head, to save him from his discomfort. So Jonah was exceedingly glad because of the plant.&rdquo; The qîqāyôn is YHWH&rsquo;s final visual aid — a plant that grows overnight, provides shade for one day, is eaten by a worm the next morning, and withers in the heat. Jonah is &ldquo;exceedingly glad&rdquo; about the plant and &ldquo;exceedingly angry&rdquo; when it dies. YHWH&rsquo;s question then turns on the disproportion: Jonah grieves over a plant he neither planted nor grew, which lasted one night. &ldquo;Should not I pity Nineveh... in which there are more than 120,000 persons?&rdquo; The qîqāyôn is a love-object Jonah did nothing to earn and has no covenant claim on — and he grieves its loss passionately. This is exactly Jonah&rsquo;s description of YHWH&rsquo;s relationship to Nineveh. The absurdity of the comparison is the book&rsquo;s final argument. Luther called the qîqāyôn the book&rsquo;s &ldquo;little sermon&rdquo; — and it may be the most economical theological argument in Scripture."
        },
        {
            "code": "H8438",
            "lemma": "תּוֹלָע",
            "translit": "tôlāʿ",
            "gloss": "worm",
            "significance": "תּוֹלָע (tôlāʿ, &lsquo;the worm — specifically the crimson-grub used to make scarlet dye; by extension, any worm&rsquo;) is appointed by God in Jonah 4:7: &ldquo;But when dawn came up the next day, God appointed (way-mānneh) a worm (tôlāʿat) that attacked the plant, so that it withered.&rdquo; The tôlāʿ receives the same mānāh-commission as the great fish — YHWH appoints both the vast (a sea creature large enough to swallow a man) and the minute (a single worm) with equal sovereignty. The worm is the instrument of Jonah&rsquo;s exposure and the occasion of his grief: its tiny action removes the qîqāyôn and leaves Jonah under the sun with the east wind — miserable enough to want to die (4:8). The tôlāʿ&rsquo;s smallness is part of the theology: YHWH&rsquo;s governance reaches to the smallest creature. The same word appears in Job 25:6 (&ldquo;how much less man, who is a maggot, and the son of man, who is a worm!&rdquo;) and in Psalm 22:6 (&ldquo;I am a worm, and not a man&rdquo; — applied by Jesus to himself on the cross). The worm that eats Jonah&rsquo;s shade is a small precursor of the worm that eats the arrogant dead (Isa 14:11; 66:24 — &ldquo;their worm shall not die&rdquo;). Here, however, the worm serves life rather than judgment: it strips Jonah&rsquo;s comfort to make him teachable."
        },
        {
            "code": "H2347",
            "lemma": "חוּס",
            "translit": "ḥûs",
            "gloss": "pity",
            "significance": "חוּס (ḥûs, &lsquo;properly, to cover; figuratively, to compassionate, to pity, to spare&rsquo;) appears in the book&rsquo;s climactic and deliberately unanswered question: Jonah 4:10-11: &ldquo;And the LORD said, &lsquo;You pity (ḥasthā) the plant, for which you did not labor, nor did you make it grow, which came into being in a night and perished in a night. And should not I pity (ʾāḥûs) Nineveh, that great city, in which there are more than 120,000 persons who do not know their right hand from their left, and also much cattle?&rsquo;&rdquo; YHWH uses Jonah&rsquo;s own ḥûs for the plant as the premise for the rhetorical question about Nineveh: the same impulse to pity that Jonah feels toward the plant is what YHWH feels toward Nineveh — but Jonah&rsquo;s ḥûs is for a plant that cost him nothing and existed one day, while YHWH&rsquo;s ḥûs is for 120,000 people he made. The book ends with the question. Jonah never answers. The reader must answer. The only possible answer is &ldquo;yes, of course you should pity Nineveh&rdquo; — which means acknowledging that God&rsquo;s compassion for Israel&rsquo;s enemy is right. The ḥûs-question is the most pointed challenge to ethnic and national exceptionalism in the OT. The NT&rsquo;s &ldquo;love your enemies and pray for those who persecute you&rdquo; (Matt 5:44) is the explicit command that Jonah&rsquo;s ḥûs-question implies."
        }
    ],

    "language_notes": (
        "<p>Jonah is the <strong>only book among the prophets that is entirely narrative</strong> — no first-person oracles, no poetry in the divine voice (though Jonah&rsquo;s prayer in ch. 2 is poetry). This gives Jonah its peculiar ironic texture: the reader sees the prophet from the outside, in the third person, as a character who behaves badly. The narrative voice is controlled and understated — Jonah 1:3 reports the flight in a few flat sentences; the irony is left entirely to the structure. The book is built on a deliberate verbal pattern: &ldquo;arise (qum) and go (lek) to Nineveh&rdquo; appears in 1:2 and is refused, then repeated in 3:2 and obeyed. The structural parallel between the two movements (chs. 1–2 and chs. 3–4) is the book&rsquo;s primary literary device: commission → response → consequence → YHWH&rsquo;s response. In chs. 1–2, Jonah flees, suffers, prays, is rescued. In chs. 3–4, Jonah obeys, Nineveh repents, God relents, Jonah rages. The second movement is the more devastating because Jonah does everything right externally and everything wrong internally.</p>"
        "<p>The <strong>prayer of Jonah 2</strong> is a psalm constructed from phrases drawn from the existing Psalter — an anthology of lament and praise vocabulary assembled in extremis. Scholars identify echoes of Psalms 18, 31, 42, 69, 107, 116, and 120 throughout the eight verses. This is not plagiarism but liturgical memory: Jonah, at the bottom of the ocean, prays in the language the community has shaped for exactly this kind of extremity. The prayer is striking for what it does not say: it does not confess Jonah&rsquo;s sin or acknowledge that his situation is his own fault. It is pure lament-and-praise — the prayer of a man who has been saved from drowning, offered <em>before</em> the fish has vomited him out. The faith that says &ldquo;yet I shall again look upon your holy temple&rdquo; (2:4) while inside the belly of a fish three days dead is the prayer&rsquo;s central act. The Hebrew of 2:9 (&ldquo;salvation belongs to the LORD&rdquo; — liYHWH hayyĕšûʿāh) is the theological summary of the entire book in four Hebrew words.</p>"
        "<p>Jonah&rsquo;s <strong>ironic register</strong> depends entirely on the Hebrew&rsquo;s understatement. The word &ldquo;great&rdquo; (gādôl) appears fourteen times in the book&rsquo;s four chapters — great city, great wind, great storm, great fish, great evil, great anger, great joy, great plant. The repetition is comic and theological: YHWH&rsquo;s great instruments and great opponents are set against Jonah, who responds to them all with the same narrow provinciality. The book&rsquo;s most devastating irony is concentrated in 4:1: &ldquo;But it was exceedingly evil (ra&rsquo;ah gĕdôlāh) to Jonah, and it burned to him.&rdquo; The &ldquo;great evil (ra&rsquo;ah)&rdquo; of Nineveh that prompted the divine mission (1:2) is echoed in the &ldquo;great evil (ra&rsquo;ah)&rdquo; that God&rsquo;s mercy provokes in Jonah (4:1). The same word for the Ninevites&rsquo; sin describes Jonah&rsquo;s rage at their forgiveness — a pun that makes the prophet&rsquo;s self-righteousness legible as its own kind of ra&rsquo;ah.</p>"
    ),

    "reception": (
        "<p><strong>Jesus and the sign of Jonah:</strong> Jesus explicitly identifies the &ldquo;sign of Jonah&rdquo; as the only sign he will give his generation (Matt 12:38-41; Luke 11:29-32). Matthew 12:40 cites the three days and three nights in the fish&rsquo;s belly as the type of the Son of Man&rsquo;s three days in the earth — making Jonah the OT&rsquo;s most direct prefiguration of the death and resurrection. Jesus also contrasts the Ninevites&rsquo; repentance at Jonah&rsquo;s preaching with his generation&rsquo;s refusal: &ldquo;something greater than Jonah is here&rdquo; (Matt 12:41) — the comparison is not flattering to the generation that receives more than Nineveh did and repents less. Paul&rsquo;s &ldquo;buried with him in baptism... raised with him through faith&rdquo; (Col 2:12) participates in the same Jonah-death-and-resurrection structure Jesus identifies.</p>"
        "<p><strong>Patristic and early church:</strong> The early church used Jonah extensively as a type of resurrection — he appears in the Roman catacombs more than any other OT figure, depicted being vomited from the fish as a symbol of resurrection hope. Tertullian, Origen, and Jerome all wrote extensively on the Jonah-typology. Augustine treated the book&rsquo;s final question as a theological statement about the universality of divine mercy, connecting it to Paul&rsquo;s &ldquo;God has consigned all to disobedience, that he may have mercy on all&rdquo; (Rom 11:32). The book was read in synagogue on Yom Kippur as the haftarah — the afternoon prophetic reading — because of its themes of repentance, divine mercy, and the possibility of YHWH relenting from judgment even at the last moment.</p>"
        "<p><strong>Modern:</strong> The fish narrative has drawn disproportionate interpretive attention — debates about whether the story is literal, allegorical, or parabolic have sometimes obscured the book&rsquo;s theological center in ch. 4. The 20th century saw the rise of what scholars call the &ldquo;mission reading&rdquo; of Jonah — Leslie Allen, Phyllis Trible, and others reading the book as a critique of post-exilic Jewish exclusivism and a call to the Gentile mission. The book&rsquo;s ending — with YHWH&rsquo;s unanswered question — was recognized as a deliberate literary device by Jack Sasson (AB commentary, 1990) and others: the reader completes the dialogue that Jonah refuses to complete.</p>"
    ),

    "reading_guide": (
        "<p><strong>The fish is not the point.</strong> Read Jonah in one sitting — it takes twelve minutes — and note where the narrative energy actually concentrates: it is overwhelmingly in chapter 4, Jonah&rsquo;s conversation with YHWH about the gourd. The fish gets three verses in chapter 1 and one verse in chapter 2. The qîqāyôn&rsquo;s theological work takes eleven verses in chapter 4. The book&rsquo;s climax is not the great fish but the small worm that eats the plant that exposes Jonah to the question he cannot answer.</p>"
        "<p><strong>Read chapter 1 for the irony of the Gentiles.</strong> The pagan sailors do everything right: they pray to their gods, they try to row rather than throw Jonah in, they ask YHWH&rsquo;s forgiveness before complying, and they worship YHWH after the sea calms. The prophet of YHWH is asleep, is thrown overboard, and disappears into a fish. The book&rsquo;s mission theology begins here: YHWH is already present and working among the Gentiles before the prophet arrives. Jonah&rsquo;s mission is not to bring God to Nineveh — it is to catch up with what God is already doing.</p>"
        "<p><strong>Sit with the unanswered question at 4:11.</strong> The book ends mid-conversation: YHWH asks whether he should not pity Nineveh, and Jonah&rsquo;s silence is the last word of the text. This is not a narrative failure but the book&rsquo;s most powerful move: the reader is required to answer for Jonah. The only possible answer — &ldquo;of course you should pity Nineveh&rdquo; — is an act of moral self-implication. Answering the question means accepting that God&rsquo;s mercy extends to people we regard as enemies. Jonah could not do this. Whether we can is the book&rsquo;s enduring question.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('jonah')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('jonah', merged)

main()
