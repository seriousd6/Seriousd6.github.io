"""
Book Study Data — Zephaniah
book_id: zephaniah
lang: hebrew

Run: python3 scripts/build-book-study-zephaniah.py

Notes:
- Author group: Minor — peaks are generic; vocabulary selected from Zephaniah's
  distinctive Day of the LORD and anawim vocabulary
- Key codes already used: H3117 yom (day), H7451 ra (evil), H7611 sheʾerith,
  H4941 mishpat, H8193 saphah (lip/speech), H2534 chemah (wrath), H6942 qadash
- H6035 anav + H6038 anavah appear together in 2:3 — the anawim-theology pair;
  the noun and adjective form the theological unit that Jesus quotes in Matt 5:5
- H7442 ranan (shout for joy) is used TWICE: 3:14 (community's command to shout)
  and 3:17 (YHWH himself shouts over his people) — this double use is unique
- H7321 ruaʿ: the same word for the Day of the LORD's battle-cry becomes the
  restoration's shout of celebration — a deliberate reversal
- H5678 ʿɛvrah (wrath/overflow) + H7782 shofar (trumpet): the Day of the LORD
  vocabulary in 1:15-16 is Zephaniah's signature and the source of Dies Irae
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
    "bookId": "zephaniah",

    "key_vocabulary": [
        {
            "code": "H5678",
            "lemma": "עֶבְרָה",
            "translit": "ʿɛvrāh",
            "gloss": "wrath",
            "significance": "עֶבְרָה (ʿɛvrāh, &lsquo;an outburst of passion — wrath that overflows its banks; the uncontainable surge of furious anger&rsquo;) is the signature term of Zephaniah&rsquo;s Day of the LORD: Zephaniah 1:15: &ldquo;A day of wrath (ʿɛvrat YHWH) is that day, a day of distress and anguish, a day of ruin and devastation, a day of darkness and gloom, a day of clouds and thick darkness.&rdquo; Also Zephaniah 1:18: &ldquo;Neither their silver nor their gold shall be able to deliver them on the day of the wrath (ʿɛvrāh) of the LORD.&rdquo; The ʿɛvrāh imagery in 1:15-16 became the source of the medieval Latin hymn <em>Dies Irae</em> (&ldquo;Day of Wrath&rdquo;), one of the most influential texts in Western musical history, used in Requiem settings by Mozart, Verdi, Berlioz, and others. The ʿɛvrāh in Zephaniah is not arbitrary rage but the overflow of YHWH&rsquo;s character against all that contradicts his holiness: 1:12 (&ldquo;I will punish the men who are complacent, who say in their hearts, &lsquo;The LORD will not do good, nor will he do ill&rsquo;&rdquo;) identifies the target as practical atheism — those who act as if YHWH is morally inert. The ʿɛvrāh answers that inertia with decisive action. The NT&rsquo;s &ldquo;the wrath (orgē — the Greek equivalent of ʿɛvrāh) of God is revealed from heaven against all ungodliness&rdquo; (Rom 1:18) stands in the same tradition."
        },
        {
            "code": "H7782",
            "lemma": "שׁוֹפָר",
            "translit": "šôpār",
            "gloss": "trumpet",
            "significance": "שׁוֹפָר (šôpār, &lsquo;the ram&rsquo;s horn — the primary instrument of alarm, assembly, and warfare in ancient Israel&rsquo;) appears in the Day of the LORD description of Zephaniah 1:16: &ldquo;a day of trumpet blast (šôpār) and battle cry against the fortified cities and against the lofty battlements.&rdquo; The šôpār in Zephaniah is the instrument of military alarm: not the summoning of worshippers to the temple (which it also did) but the battle signal announcing an overwhelming invasion. The OT&rsquo;s šôpār vocabulary includes the Sinai theophany (&ldquo;the sound of the trumpet grew louder and louder&rdquo; — Exod 19:19), Jericho&rsquo;s walls (Josh 6:4-5), Joel&rsquo;s Day of the LORD summons (Joel 2:1: &ldquo;blow the šôpār in Zion; sound the alarm on my holy mountain&rdquo;), and Ezekiel&rsquo;s watchman who sounds the šôpār (Ezek 33:3-6). In Zephaniah, the šôpār is YHWH&rsquo;s war-signal against all human fortifications: the &ldquo;fortified cities&rdquo; and &ldquo;lofty battlements&rdquo; that human confidence has built. The NT&rsquo;s eschatological šôpār (Matt 24:31: &ldquo;he will send out his angels with a loud trumpet call&rdquo;; 1 Cor 15:52: &ldquo;the last trumpet will sound&rdquo;; Rev 8-9&rsquo;s seven trumpets) continues the šôpār-theology: the final Day of the LORD announced by the great horn."
        },
        {
            "code": "H7494",
            "lemma": "רַעַשׁ",
            "translit": "rɛʿaš",
            "gloss": "quaking",
            "significance": "רַעַשׁ (rɛʿaš, &lsquo;vibration, commotion, quaking — the shaking of the earth, the thunder of battle, the trembling of the land before the divine warrior&rsquo;) contributes to Zephaniah&rsquo;s comprehensive list of the Day of the LORD&rsquo;s terrors: Zephaniah 1:15: &ldquo;a day of distress and anguish (ṣārāh ûmĕṣûqāh), a day of ruin and devastation (šōʾāh ûmĕšōʾāh), a day of darkness and gloom.&rdquo; Zephaniah 1:10: &ldquo;a sound of a cry from the Fish Gate, a wail from the Second Quarter, a loud crash (šeber gadōl) from the hills.&rdquo; The rɛʿaš-vocabulary describes the physical and social disruption of the Day: not merely moral judgment but the shaking of the entire created order. In the OT, rɛʿaš accompanies divine theophanies: YHWH&rsquo;s voice shakes the earth (Ps 68:8); the vision of Ezekiel opens with a great rɛʿaš (Ezek 3:12-13); the theophany to Elijah involves rɛʿaš (1 Kgs 19:11). Zephaniah&rsquo;s use in the Day of the LORD context implies that the final judgment is a theophanic event — the same Creator who established the created order will shake it. Hebrews 12:26-27 quotes Haggai 2:6 about the shaking of heaven and earth, adding: &ldquo;This phrase, &lsquo;Yet once more,&rsquo; indicates the removal of things that are shaken... in order that the things that cannot be shaken may remain.&rdquo;"
        },
        {
            "code": "H6035",
            "lemma": "עָנָו",
            "translit": "ʿānāv",
            "gloss": "humble",
            "significance": "עָנָו (ʿānāv, &lsquo;depressed in mind or circumstances — humble, meek, poor; one who is brought low and so depends on God rather than on social power or status&rsquo;) is Zephaniah&rsquo;s primary term for the covenant remnant. Zephaniah 2:3: &ldquo;Seek the LORD, all you humble (ʿanwê) of the land, who do his just commands.&rdquo; Zephaniah 3:12: &ldquo;I will leave in your midst a people humble and lowly (ʿanî wādal). They shall take refuge in the name of the LORD — those who are left in Israel.&rdquo; The ʿānāv-people are the <em>anawim</em> — the Hebrew concept of the poor and humble who depend entirely on YHWH rather than on military power, social status, or political alliance. The contrast in Zephaniah is with the proud: the city whose &ldquo;rulers within her are roaring lions; her judges are evening wolves that leave nothing till the morning&rdquo; (3:3). These proud and violent rulers will be swept away; the ʿānāv-remnant will be preserved. Psalm 37:11 (&ldquo;the meek shall inherit the land&rdquo;) and Jesus&rsquo;s Beatitude &ldquo;blessed are the meek, for they shall inherit the earth&rdquo; (Matt 5:5) are direct extensions of the ʿānāv-theology Zephaniah voices: the covenant&rsquo;s heirs are the humble poor who trust in YHWH rather than in their own resources."
        },
        {
            "code": "H6038",
            "lemma": "עֲנָוָה",
            "translit": "ʿănāwāh",
            "gloss": "humility",
            "significance": "עֲנָוָה (ʿănāwāh, &lsquo;condescension, modesty — the quality of being humble before God and deferential to others; the noun form of ʿānāv&rsquo;) appears paired with the adjective ʿānāv in Zephaniah 2:3&rsquo;s call to seek YHWH before the Day: &ldquo;Seek the LORD, all you humble (ʿanwê) of the land, who do his just commands; seek righteousness; seek humility (ʿănāwāh).&rdquo; The triple imperative &ldquo;seek — seek — seek&rdquo; structures the verse: seek the LORD, seek righteousness (ṣɛḏɛq), seek humility (ʿănāwāh). The ʿănāwāh is therefore not a means to an end but part of the command itself: humility is not merely the posture that enables seeking but one of the things to be sought. The juxtaposition of ṣɛḏɛq (righteousness — right relationship and right action) with ʿănāwāh (humility before God) is the Zephaniah pairing that Micah 6:8&rsquo;s &ldquo;do justice, love kindness, walk humbly&rdquo; also enacts: the covenant life combines ethical rectitude with the ʿănāwāh-posture before YHWH. The LXX translates ʿănāwāh as <em>praütēs</em> (meekness) — the same word Paul uses in Galatians 5:23 as a fruit of the Spirit and in Ephesians 4:2 as the posture of the new community: &ldquo;with all humility and gentleness (praütētos).&rdquo;"
        },
        {
            "code": "H1322",
            "lemma": "בֹּשֶׁת",
            "translit": "bōšɛṯ",
            "gloss": "shame",
            "significance": "בֹּשֶׁת (bōšɛṯ, &lsquo;shame — the feeling of exposure, of having been shown to be wrong, insufficient, or morally bankrupt; by extension, the thing that causes shame&rsquo;) is one of Zephaniah&rsquo;s key terms for the reversal from judgment to restoration. Zephaniah 3:5: &ldquo;the LORD within her is righteous; he does no injustice... but the unjust knows no shame (bōšɛt).&rdquo; The shamelessness of the unjust (they continue their destruction without the capacity for self-awareness that shame provides) is the diagnosis of Judah&rsquo;s leadership. Zephaniah 3:11: &ldquo;On that day you shall not be put to shame (tēbōšî) because of the deeds by which you have rebelled against me; for then I will remove from your midst your proudly exultant ones.&rdquo; Zephaniah 3:19: &ldquo;I will change their shame (bušpāṯām) into praise and renown in all the earth.&rdquo; The arc is: unjust shamelessness (3:5) → shame of judgment (3:11 — the shame that falls on the guilty) → shame transformed into praise (3:19 — the shame of exile reversed by restoration). Zephaniah&rsquo;s bōšɛṯ-arc maps the full movement of covenant judgment and redemption: the God who judges the shameless will ultimately transform the shame of the judged into glory. The NT&rsquo;s &ldquo;he endured the cross, despising the shame (aischynēs)&rdquo; (Heb 12:2) picks up the same bōšɛṯ-to-glory arc."
        },
        {
            "code": "H5766",
            "lemma": "עֶוֶל",
            "translit": "ʿɛvɛl",
            "gloss": "injustice",
            "significance": "עֶוֶל (ʿɛvɛl, &lsquo;moral evil, injustice — specifically the wrongness of deviation from what is right; the bent or crooked nature of actions that violate the covenant order&rsquo;) appears in the contrast between YHWH&rsquo;s character and Judah&rsquo;s leadership: Zephaniah 3:5: &ldquo;The LORD within her is righteous; he does no injustice (ʿawlāh); morning by morning he shows forth his justice; each dawn he does not fail; but the unjust man knows no shame.&rdquo; Also Zephaniah 3:13: &ldquo;Those who are left in Israel; they shall do no injustice (ʿawlāh) and speak no lies, nor shall there be found in their mouth a deceitful tongue.&rdquo; The ʿɛvɛl in 3:5 is the term that defines what YHWH never does — it is the standard of divine righteousness expressed negatively. The contrast with the unjust leaders (3:3-4 — lions, wolves, treacherous prophets, profane priests) who do practice ʿɛvɛl is sharp: YHWH&rsquo;s character is the standard against which Judah&rsquo;s leadership is measured and found catastrophically short. The restoration promise in 3:13 is that the remnant will be defined by the same ʿɛvɛl-absence that defines YHWH: they will do no injustice and speak no lies. The purified community will reflect the character of YHWH who dwells in their midst (3:17)."
        },
        {
            "code": "H7604",
            "lemma": "שָׁאַר",
            "translit": "šāʾar",
            "gloss": "remain",
            "significance": "שָׁאַר (šāʾar, &lsquo;to swell up, be redundant — i.e. to be left over after removal; to remain as a survivor after loss or destruction&rsquo;) is the remnant-verb of Zephaniah: Zephaniah 3:12: &ldquo;I will leave (wĕhišʾartî) in your midst a people humble and lowly.&rdquo; Also Zephaniah 2:9: &ldquo;the remnant of my people shall plunder them, and the survivors (yitrô) of my nation shall possess them.&rdquo; The šāʾar is not the mass of the covenant people who escape the Day of the LORD intact — it is the deliberately left-over remnant, preserved after the judgment has removed the proud and violent. The hiphil form wĕhišʾartî (&ldquo;I will leave&rdquo;) in 3:12 makes YHWH the agent of the leaving: the remnant is not a self-selecting group but one that YHWH specifically preserves. This is consistent with Zephaniah&rsquo;s ʿānāv-theology: the šāʾar-remnant is identified not by military power or social status but by their ʿănāwāh (humility) before YHWH. The NT uses the same šāʾar-logic: Romans 9:27 cites Isaiah 10:22 (&ldquo;though the number of the sons of Israel be as the sand of the sea, only a remnant will be saved&rdquo;) to describe the principle by which YHWH preserves the covenant promise through judgment."
        },
        {
            "code": "H2717",
            "lemma": "חָרַב",
            "translit": "ḥārav",
            "gloss": "lay waste",
            "significance": "חָרַב (ḥārav, &lsquo;to parch through drought, hence to desolate, destroy — the drying up that leads to complete ruin&rsquo;) describes what the Day of the LORD does to the proud nations in Zephaniah 2: Zephaniah 2:4: &ldquo;Gaza shall be deserted, and Ashkelon shall become a desolation.&rdquo; Zephaniah 2:13-14: &ldquo;And he will stretch out his hand against the north and destroy Assyria, and he will make Nineveh a desolation (šĕmāmāh), dry as the desert (ḥārĕbāh). Herds shall lie down in her midst... the raven shall croak in the window; desolation shall be on the threshold.&rdquo; The ḥārav-desolation of Nineveh is announced here by Zephaniah with the same certainty as by Nahum — but Zephaniah embeds it in a comprehensive indictment of all the nations surrounding Judah: the Philistine cities (2:4-7), Moab and Ammon (2:8-11), Cush (2:12), and Assyria (2:13-15). The ḥārav is not merely political collapse but the stripping away of the prosperity the nations built on violence: the city that &ldquo;lived in security&rdquo; and said &ldquo;I am, and there is no one else&rdquo; (2:15) will become ḥārav — parched, empty, home only to birds. The Book of Revelation&rsquo;s &ldquo;Fallen, fallen is Babylon the great&rdquo; (18:2) updates the same ḥārav-announcement to the ultimate empire."
        },
        {
            "code": "H7442",
            "lemma": "רָנַן",
            "translit": "rānan",
            "gloss": "shout for joy",
            "significance": "רָנַן (rānan, &lsquo;properly, to creak or emit a stridulous sound — hence, to shout usually for joy; the spontaneous cry of exultation that cannot be contained&rsquo;) is used twice in Zephaniah&rsquo;s restoration climax in a way that is unique in the OT: Zephaniah 3:14: &ldquo;Sing aloud (rannî), O daughter of Zion; shout, O Israel!&rdquo; — the community is commanded to rānan. Zephaniah 3:17: &ldquo;he will exult over you with gladness; he will quiet you by his love; <strong>he will exult over you with loud singing (yāgîl ʿālayik bĕrinnāh)</strong>&rdquo; — YHWH himself performs rinnāh (the noun form of rānan) over his people. The double rānan — community shouting over God, God shouting over the community — is the book&rsquo;s most theologically significant literary move. The image of YHWH singing (rannāh) over his people is unprecedented: it reverses the typical prophetic direction (YHWH speaks, people respond) and presents the covenant&rsquo;s consummation as a mutual celebration. The NT participates in the same double-movement: Luke 15&rsquo;s three parables all end with celebration over the found — the shepherd, the woman, the father each rejoice (sugkharēte — &ldquo;rejoice with me&rdquo;) when the lost is recovered. Jesus explicitly connects this to the joy in heaven over one sinner who repents (15:7,10)."
        },
        {
            "code": "H7321",
            "lemma": "רוּעַ",
            "translit": "rûaʿ",
            "gloss": "shout",
            "significance": "רוּעַ (rûaʿ, &lsquo;to mar by breaking — to split the ears with sound; to shout an alarm, battle cry, or shout of triumph&rsquo;) appears in the restoration call of Zephaniah 3:14: &ldquo;Sing aloud, O daughter of Zion; shout (hārîʿî), O Israel! Rejoice and exult with all your heart.&rdquo; The significance of rûaʿ in Zephaniah is the reversal it enacts: the Day of the LORD in 1:16 is characterized by &ldquo;trumpet blast and battle cry (ûtĕrûʿāh — from rûaʿ) against the fortified cities&rdquo;. The tĕrûʿāh (the noun of rûaʿ) is YHWH&rsquo;s battle alarm against the fortifications of human pride. In 3:14, the same root becomes the people&rsquo;s shout of jubilation: the battle cry that sounded against Judah&rsquo;s corrupt establishments is now the people&rsquo;s cry of joy at YHWH&rsquo;s victorious presence among them. The OT&rsquo;s tĕrûʿāh-vocabulary spans alarm and celebration: Leviticus 23:24 (&ldquo;a memorial of tĕrûʿāh&rdquo; — the Feast of Trumpets); Joshua 6:5 (Jericho falls at the tĕrûʿāh); Ezra 3:11-13 (&ldquo;the people shouted (rûaʿ) with a great shout when they praised the LORD&rdquo; at the foundation of the Second Temple). Zephaniah uses the rûaʿ-reversal to show that the Day of the LORD&rsquo;s judgment and the people&rsquo;s restoration are both events in the same story told by the same God."
        },
        {
            "code": "H3956",
            "lemma": "לָשׁוֹן",
            "translit": "lāšôn",
            "gloss": "tongue",
            "significance": "לָשׁוֹן (lāšôn, &lsquo;the tongue — as the instrument of licking, eating, or speech; by extension, language, a people group defined by its language&rsquo;) appears in both the negative diagnosis and the positive restoration of Zephaniah. The negative: Zephaniah 3:13: &ldquo;those who are left in Israel... shall do no injustice and speak no lies, nor shall there be found in their mouth a deceitful tongue (lĕšôn tarmît).&rdquo; The deceitful lāšôn is the remnant&rsquo;s non-characteristic: when YHWH purifies his people, the tongue that has been the instrument of deception will be stilled. The positive reversal: Zephaniah 3:9: &ldquo;I will change the speech (sāpāh — lit. &lsquo;lip/language&rsquo;) of the peoples to a pure speech, that all of them may call upon the name of the LORD and serve him with one accord.&rdquo; The sāpāh bĕrûrāh (&ldquo;pure language&rdquo;) of 3:9 is the reversal of the Babel-confusion (Gen 11:1: &ldquo;the whole earth had one language (sāpāh) and the same words&rdquo;; then 11:7: &ldquo;I will confuse their language (sāpāh)&rdquo;). What Babel separated — a shared language — will be restored in the eschatological gathering of nations. Pentecost (Acts 2:4-11) is the NT&rsquo;s fulfillment: the gift of tongues reverses Babel by enabling each lāšôn-group to hear the gospel in its own language, beginning the gathering that Zephaniah&rsquo;s &ldquo;pure speech&rdquo; anticipates."
        }
    ],

    "language_notes": (
        "<p>Zephaniah is structured as a <strong>concentric expansion and contraction</strong> of the Day of the LORD: beginning with Judah&rsquo;s specific sins (1:4-13), expanding outward to encompass all nations (2:4-15), then narrowing back to Jerusalem&rsquo;s corrupt leadership (3:1-7), then widening again to all the earth (3:8), before contracting to the restored remnant (3:9-13) and ending in intimate celebration (3:14-20). This spiral movement — outward judgment, inward restoration — is the theological logic of the book: YHWH&rsquo;s judgment is universal precisely because his sovereignty is universal, but his restoration is particular, centered in a humble remnant who take refuge in his name. The medieval <em>Dies Irae</em> captures only the outward spiral; the full book requires both spirals to be read together.</p>"
        "<p>The book&rsquo;s most distinctive literary feature is the <strong>reversal of the Day of the LORD&rsquo;s vocabulary in the restoration oracles</strong>. Zephaniah 1:14-16 develops the most concentrated string of Day of the LORD language in the OT: wrath (ʿɛvrāh), distress and anguish, darkness and gloom, trumpet (šôpār) and battle cry (tĕrûʿāh). Then in 3:14-17, the same terms return transformed: the shout (rûaʿ) that was a battle alarm becomes the shout of the restored community; the singing (rinnāh) that was absent becomes YHWH&rsquo;s own voice over his people. Zephaniah 3:17&rsquo;s &ldquo;he will exult over you with loud singing (bĕrinnāh)&rdquo; uses the noun form of the same verb rānan that 3:14 uses for the community&rsquo;s rejoicing — the reversal is complete and symmetrical: YHWH sings over his people exactly what his people sing over YHWH. This mutual joy is the book&rsquo;s theological destination. No other prophetic book ends with YHWH himself performing music; 3:17&rsquo;s rinnāh stands as the OT&rsquo;s most intimate image of divine delight in his covenant people.</p>"
        "<p>Zephaniah&rsquo;s anawim-theology — the <strong>identification of the humble poor as the covenant remnant</strong> — is developed in 2:3 and 3:12-13 with vocabulary that becomes foundational for the Psalter&rsquo;s &ldquo;poor of YHWH&rdquo; tradition and for Jesus&rsquo;s Beatitudes. The word ʿānāv (humble/meek) in Zephaniah describes not merely a psychological state but a socioeconomic and political reality: the ʿānāv-people are those who have no human power to rely on and therefore rely entirely on YHWH. The contrast Zephaniah draws — corrupt leaders who are lions and wolves (3:3) against the humble remnant who speak no lies (3:13) — is the OT&rsquo;s clearest anticipation of the beatitude reversal: the ones who appear weakest in the present order are the ones who receive the covenant promises.</p>"
    ),

    "reception": (
        "<p><strong><em>Dies Irae</em> and Western music:</strong> Zephaniah 1:15-16 became the source of the 13th-century Latin sequence <em>Dies Irae, dies illa</em> (&ldquo;Day of wrath, that day&rdquo;), attributed to Thomas of Celano. This text was used in the Mass for the Dead for centuries and was set to music by Mozart (Requiem, K. 626), Verdi (Messa da Requiem), Berlioz (Grande Messe des Morts), and many others — making Zephaniah arguably the OT&rsquo;s most influential text in Western classical music. The musical tradition drew on Zephaniah&rsquo;s ʿɛvrāh-vocabulary to express the solemnity of divine judgment and the urgency of repentance, though typically without the restoration-arc that follows in chapter 3.</p>"
        "<p><strong>Zephaniah 3:9 and Pentecost:</strong> Early Christian interpreters from Origen onward read Zephaniah 3:9 (&ldquo;I will change the speech of the peoples to a pure speech&rdquo;) as a prophecy of Pentecost. The reversal of Babel — one divided language becoming many unified testimonies to YHWH — was seen as fulfilled in Acts 2, where the Spirit enabled each national group to hear the gospel in its own lāšôn. This reading shaped Christian theology of mission: the gathering of the nations through a common proclamation was understood as the restoration that Zephaniah announced. Paul&rsquo;s &ldquo;there is no distinction between Jew and Greek; for the same Lord is Lord of all&rdquo; (Rom 10:12) stands in the same eschatological horizon as Zephaniah&rsquo;s pure-speech promise.</p>"
        "<p><strong>Zephaniah 3:17 in Christian spirituality:</strong> The image of YHWH singing (rinnāh) over his people has functioned as one of the NT&rsquo;s most beloved images of divine delight. The verse has been widely quoted in contexts of suffering and doubt as an assurance that divine pleasure in the covenant people is not contingent on their performance. Luke 15&rsquo;s three parables of the lost — each ending with a celebration — are typically read in light of Zephaniah 3:17: the Father running and celebrating over the returning prodigal is YHWH doing with flesh and motion what Zephaniah heard as a divine song.</p>"
    ),

    "reading_guide": (
        "<p><strong>Read both spirals, not just the first.</strong> The Day of the LORD imagery in chapter 1 — wrath, darkness, trumpet blast — is only half the book. The same God who announces universal judgment in 1:15-16 is the God who sings with joy over his remnant in 3:17. Reading Zephaniah for the judgment alone is like reading a story that stops before the ending. The ʿɛvrāh of 1:15 and the rinnāh of 3:17 are both necessary to understand YHWH&rsquo;s character: he is the God whose holiness cannot endure injustice and whose love will not stop at its removal.</p>"
        "<p><strong>Read 2:3 as the book&rsquo;s pastoral pivot.</strong> Between the judgment announcement and the nations-oracles, Zephaniah inserts a call to seek: &ldquo;Seek the LORD... seek righteousness; seek humility.&rdquo; This is not an interruption but the point: the Day of the LORD is announced so that the humble will seek YHWH before it arrives, not after. The ʿānāv-people who heed the call of 2:3 are the remnant of 3:12-13. The call to seek (baqĕšû, baqĕšû — the repeated imperative) implies that seeking is available, possible, and urgent. The book is not merely a prediction but an invitation.</p>"
        "<p><strong>Read 3:17 slowly.</strong> &ldquo;The LORD your God is in your midst, a mighty one who will save; he will rejoice over you with gladness; he will quiet you by his love; he will exult over you with loud singing.&rdquo; This is the theological destination of the entire book. The God who announced judgment on Jerusalem (3:1-7) and the nations (2:4-15) takes up residence in the city he purified and sings. Read the first three chapters as the path that leads to this sentence. The rinnāh in 3:17 is the answer to the šôpār in 1:16: the horn of judgment has sounded; the song of restoration is its completion.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('zephaniah')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('zephaniah', merged)

main()
