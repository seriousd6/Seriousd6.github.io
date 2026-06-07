"""
Book Study Data — Jeremiah
book_id: jeremiah
lang: hebrew

Run: python3 scripts/build-book-study-jeremiah.py

Notes:
- Author group: Major in author-freq-hebrew.json; peaks are mostly generic —
  vocabulary selected from Jeremiah's specific theological program
- All Hebrew translit fields blank in glossary — supplied manually
- H4878 meshuvah: 12 of ~14 OT uses are in Jeremiah; the most distinctive
  Jeremianic word — the vocabulary of apostasy as turning away
- H2319 chadash: pivotal as "new" in the only explicit "new covenant" oracle in
  the OT (31:31); Jesus quotes this at the Last Supper; Hebrews develops it
- H2719 cherev: Jeremiah's triad "sword/famine/pestilence" appears ~14x in this
  book alone, more than in all other OT books combined
- H3335 yatsar (potter/form): Jer 18 potter passage is uniquely Jeremianic; Paul
  applies it in Romans 9:21; recapitulates Gen 2:7 creation vocabulary
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
    "bookId": "jeremiah",

    "key_vocabulary": [
        {
            "code": "H4878",
            "lemma": "מְשׁוּבָה",
            "translit": "mĕšûvāh",
            "gloss": "apostasy",
            "significance": "מְשׁוּבָה (meshuvah, &lsquo;apostasy — derived from shuv (to turn), meaning the act of turning away&rsquo;) is Jeremiah&rsquo;s most characteristic diagnostic word: 12 of approximately 14 OT occurrences are in Jeremiah. Jeremiah 2:19: &ldquo;Your evil will chastise you, and your apostasy (meshuvah) will reprove you. Know and see that it is evil and bitter for you to forsake the LORD your God.&rdquo; Jeremiah 3:6-12 repeats the word five times, alternating between &ldquo;faithless Israel&rdquo; and &ldquo;treacherous Judah.&rdquo; The word&rsquo;s derivation from shuv (to turn/return) is theologically precise: apostasy is the opposite of repentance. Jeremiah&rsquo;s persistent call is for Israel to &ldquo;return (shuv)&rdquo; (3:12-14; 4:1; 15:19), and their failure to do so is their meshuvah — the turning-away that has become the orientation of the nation. The diagnostic is structural: the problem with Judah is not specific sins but a fundamental directional turning away from YHWH. Hebrews 6:6 describes apostasy (apostasia, from the Greek verb meaning &ldquo;to stand away from&rdquo;) in terms that echo Jeremiah: it is not a single sin but a condition of having turned away."
        },
        {
            "code": "H2319",
            "lemma": "חָדָשׁ",
            "translit": "ḥādāš",
            "gloss": "new",
            "significance": "חָדָשׁ (chadash, &lsquo;new — fresh, something innovated or renewed&rsquo;) is the pivotal word in Jeremiah 31:31: &ldquo;Behold, the days are coming, declares the LORD, when I will make a new (chadash) covenant with the house of Israel and the house of Judah.&rdquo; This is the only explicit &ldquo;new covenant&rdquo; in the OT, and the word chadash is its load-bearing term. The same word is used for the &ldquo;new song&rdquo; (shir chadash) of the Psalms — a song that proclaims a new act of God. What makes the new covenant &ldquo;new&rdquo; is not its parties or content (YHWH and Israel; the law as standard) but its mode: &ldquo;I will put my law within them, and I will write it on their hearts&rdquo; (31:33). The old covenant was written on stone tablets; the new is written on the heart. Jesus&rsquo; &ldquo;this cup is the new covenant in my blood&rdquo; (Luke 22:20; 1 Cor 11:25) fulfills this oracle explicitly; he identifies the cup as the instrument of the new covenant&rsquo;s establishment. Hebrews 8-10 builds the entire argument for Christ&rsquo;s high priesthood on Jeremiah 31:31-34, quoting it in full in Hebrews 8 — the longest OT quotation in the NT."
        },
        {
            "code": "H2719",
            "lemma": "חֶרֶב",
            "translit": "ḥɛrɛb",
            "gloss": "sword",
            "significance": "חֶרֶב (cherev, &lsquo;a cutting instrument — a sword or knife; also drought, from a related root meaning to be scorched&rsquo;) anchors Jeremiah&rsquo;s characteristic judgment triad: &ldquo;sword (cherev), famine (raav), and pestilence (dever).&rdquo; This combination appears approximately 14 times in Jeremiah, compared to a handful of times in all other OT books combined. Jeremiah 14:12: &ldquo;I will consume them by the sword, by the famine, and by the pestilence.&rdquo; Jeremiah 24:10: &ldquo;I will send sword, famine, and pestilence upon them.&rdquo; The triad is a precise list of the covenant curses of Deuteronomy 28: military defeat (sword), agricultural failure (famine), and epidemic (pestilence) — the specific consequences YHWH warned would follow covenant violation. Jeremiah&rsquo;s repeated invocation of the triad signals that Deuteronomy&rsquo;s curses are being activated. The NT applies the same triadic judgment to the eschatological wars of Revelation 6:3-8 (&ldquo;sword...famine...pestilence&rdquo;) — the three of the four horsemen, confirming that John&rsquo;s vision of end-time judgment is built on the prophetic vocabulary Jeremiah deployed against Jerusalem."
        },
        {
            "code": "H5003",
            "lemma": "נָאַף",
            "translit": "nāʾaf",
            "gloss": "commit adultery",
            "significance": "נָאַף (naaf, &lsquo;to commit adultery — literally of sexual infidelity; figuratively, to apostatize&rsquo;) is Jeremiah&rsquo;s word for Judah&rsquo;s idolatry understood as covenant infidelity. Jeremiah 3:8-9: &ldquo;She saw that for all the adulteries (naafuv) of that faithless one, Israel... Yet her treacherous sister Judah did not fear, but she too went and played the whore. Because she took her whoredom lightly, she polluted the land, committing adultery (naaf) with stone and tree.&rdquo; Jeremiah 9:2: &ldquo;they are all adulterers (menaafim), a company of treacherous men.&rdquo; The marriage metaphor for the covenant — YHWH as husband, Israel as wife — turns idolatry into the most intimate betrayal: seeking other gods is the covenant infidelity of a spouse pursuing other lovers. Jeremiah 2:2 establishes the baseline: &ldquo;I remember the devotion of your youth, your love as a bride.&rdquo; That early devotion is what the naaf-vocabulary measures the distance from. The NT applies the adultery-metaphor directly: James 4:4 addresses &ldquo;you adulterous people&rdquo; — those who love the world rather than God — using the same marriage-and-betrayal framework."
        },
        {
            "code": "H5594",
            "lemma": "סָפַד",
            "translit": "sāpad",
            "gloss": "lament",
            "significance": "סָפַד (saphad, &lsquo;to tear the hair and beat the breast — the physical gestures of Oriental mourning; to lament and wail&rsquo;) is integral to Jeremiah&rsquo;s distinctive literary contribution: the prophetic confession as a genre. The six confessions of Jeremiah (11:18-12:6; 15:10-21; 17:14-18; 18:18-23; 20:7-18) are unlike anything else in the prophets: the prophet does not merely relay divine messages but pours out his own anguish — his desire for vengeance on his enemies, his complaint that God has deceived him (20:7: &ldquo;O LORD, you have deceived me&rdquo;), his curse of the day he was born (20:14-18). Jeremiah 22:18: &ldquo;They shall not lament (siphdu) for him.&rdquo; Jeremiah 49:3: &ldquo;Wail (siphdu)...&rdquo; The saphad-genre draws on the individual lament psalms but pushes them to unprecedented rawness. The result is the OT&rsquo;s most transparently human prophetic voice — suffering without resolution, faithfulness without reward, speaking without being heard. The NT&rsquo;s &ldquo;Jesus wept&rdquo; (John 11:35) and Gethsemane&rsquo;s &ldquo;My soul is very sorrowful, even to death&rdquo; (Matt 26:38) find their closest OT parallel in Jeremiah&rsquo;s saphad-prayers."
        },
        {
            "code": "H2555",
            "lemma": "חָמָס",
            "translit": "ḥāmās",
            "gloss": "violence",
            "significance": "חָמָס (chamas, &lsquo;violence — by implication, wrong; by extension, unjust gain&rsquo;) is Jeremiah&rsquo;s social justice vocabulary. Jeremiah 6:7: &ldquo;As a well keeps its water fresh, so she keeps her evil fresh; violence (chamas) and destruction are heard within her; sickness and wounds are ever before me.&rdquo; Jeremiah 20:8: &ldquo;For the word of the LORD has become for me a reproach and derision all day long... I am weary of holding it in, and I cannot.&rdquo; Jeremiah cries &ldquo;violence (chamas) and destruction!&rdquo; but receives only mockery. The same word describes the violence that precipitated Noah&rsquo;s flood: Genesis 6:11-13 uses chamas three times for the violence that fills the earth before the judgment. Jeremiah&rsquo;s Jerusalem has returned to pre-flood conditions: chamas saturates the city just as it did the antediluvian world. Ezekiel applies the same term to Sodom (16:49-50: &ldquo;she and her daughters were arrogant, overfed and unconcerned; they did not help the poor and needy&rdquo;). The NT&rsquo;s application: Acts 7:52 invokes the prophets&rsquo; persecution, and Habakkuk&rsquo;s famous chamas-cry (&ldquo;why do you make me look at injustice?&rdquo; Hab 1:3) uses the same word."
        },
        {
            "code": "H3707",
            "lemma": "כַּעַס",
            "translit": "kaʿas",
            "gloss": "provoke",
            "significance": "כַּעַס (kaas, &lsquo;to trouble; by implication, to grieve, rage, be indignant — with the specific sense of provoking another to anger&rsquo;) is Jeremiah&rsquo;s word for the covenantal-relational dynamic of idolatry: Israel&rsquo;s unfaithfulness &ldquo;provokes&rdquo; God. Jeremiah 7:18-19: &ldquo;Is it I whom they provoke (mekaisim)?... Is it not themselves, to their own shame?&rdquo; Jeremiah 25:6-7: &ldquo;Do not go after other gods to serve and worship them, or provoke me to anger (hakaisuni) with the work of your hands... Yet you have not listened to me, declares the LORD, that you might provoke me to anger (le haksicheini) with the work of your hands to your own harm.&rdquo; The kaas-language reveals that idolatry is not merely law-breaking but the active provocation of a relational covenant — YHWH&rsquo;s jealousy (from qana, jealous love) responds to kaas with disciplinary judgment. But the provocation ultimately harms the provoker, not God: &ldquo;to your own shame&rdquo; (7:19). The NT&rsquo;s &ldquo;or do we provoke the Lord to jealousy?&rdquo; (1 Cor 10:22 — using parazēloumen, to provoke to jealous anger) applies the same relational-covenant framework to Christian behavior."
        },
        {
            "code": "H7453",
            "lemma": "רֵעַ",
            "translit": "rēaʿ",
            "gloss": "neighbor",
            "significance": "רֵעַ (rea, &lsquo;an associate, neighbor, companion — more or less close&rsquo;) appears in Jeremiah&rsquo;s devastating diagnosis of the social breakdown that attends covenant collapse. Jeremiah 9:4-5: &ldquo;Let everyone beware of his neighbor (rea) and put no trust in any brother, for every brother is a deceiver, and every neighbor (rea) goes about as a slanderer. Everyone deceives his neighbor (rea), and no one speaks the truth.&rdquo; This is the covenant-failure as experienced in everyday relationships: the rea-relationship (the horizontal neighbor-love commanded in Lev 19:18) has collapsed entirely. Jeremiah documents not just the vertical failure (Israel abandoning YHWH) but the horizontal failure (Israelites betraying each other) as the social consequence. Micah 7:5-6 describes the same collapse: &ldquo;put no trust in a neighbor (rea).&rdquo; Jesus quotes the same tradition in Matthew 10:35-36. The Great Commandment&rsquo;s &ldquo;love your neighbor (plēsion) as yourself&rdquo; (Matt 22:39) is the positive restoration of the rea-relationship that Jeremiah describes as destroyed — and that the new covenant written on the heart would ultimately restore."
        },
        {
            "code": "H2181",
            "lemma": "זָנָה",
            "translit": "zānāh",
            "gloss": "play the harlot",
            "significance": "זָנָה (zanah, &lsquo;to play the harlot — literally of sexual promiscuity; figuratively, the OT&rsquo;s standard metaphor for idolatry&rsquo;) is used extensively in Jeremiah for Judah&rsquo;s covenant infidelity. Jeremiah 2:20: &ldquo;On every high hill and under every green tree you bowed down like a whore (zanah).&rdquo; Jeremiah 3:1-3 uses zanah five times in rapid succession: &ldquo;You have played the whore with many lovers... you have the forehead of a whore; you refuse to be ashamed.&rdquo; The marriage-covenant metaphor (YHWH as husband, established in Jer 2:2) makes idolatry grotesquely equivalent to prostitution. The repetition of zanah in Jer 3:1-3 is deliberate rhetoric: Jeremiah is trying to shock a nation that has become comfortable with syncretism into recognizing what its behavior actually looks like from the perspective of covenant fidelity. Hosea established this metaphor for the northern kingdom; Jeremiah extends it to Judah; Ezekiel 16 and 23 develop it at greatest length. Revelation 17:1-5 applies the zanah-metaphor to Rome: &ldquo;the great prostitute who is seated on many waters...the nations have drunk the wine of the passion of her sexual immorality (porneia).&rdquo;"
        },
        {
            "code": "H6869",
            "lemma": "צָרָה",
            "translit": "ṣārāh",
            "gloss": "distress",
            "significance": "צָרָה (tsarah, &lsquo;tightness — figuratively, trouble, adversity, distress&rsquo;) is the word for the eschatological tribulation that Jeremiah promises will precede the final restoration of Israel. Jeremiah 30:7: &ldquo;Alas! That day is so great there is none like it; it is a time of distress (tsarah) for Jacob; yet he shall be saved out of it.&rdquo; This is the origin of the phrase &ldquo;the time of Jacob&rsquo;s trouble,&rdquo; which has shaped Jewish and Christian eschatology for millennia. The tsarah precedes the restoration: Jeremiah 30:8-11 immediately follows with promises of liberation and new covenant blessing. Daniel 12:1 picks up the language: &ldquo;a time of trouble (tsarah), such as never has been since there was a nation till that time.&rdquo; Jesus&rsquo; &ldquo;great tribulation (thlipsis megas)&rdquo; in Matthew 24:21 (&ldquo;then there will be great tribulation, such as has not been from the beginning of the world until now&rdquo;) applies the tsarah-promise to the events preceding his return. Revelation 7:14 places the sealed multitude as those &ldquo;coming out of the great tribulation&rdquo; — the community that has passed through the tsarah of Jacob and been saved out of it."
        },
        {
            "code": "H4834",
            "lemma": "מָרַץ",
            "translit": "māraṣ",
            "gloss": "grievous",
            "significance": "מָרַץ (marats, &lsquo;to press, be pungent or vehement; to irritate&rsquo;) appears in one of Jeremiah&rsquo;s most penetrating critiques of false prophecy. Jeremiah 6:14 (repeated verbatim in 8:11): &ldquo;They have healed the wound of my people lightly (qalal), saying, &lsquo;Peace, peace,&rsquo; when there is no peace.&rdquo; The related diagnostic is marats — the wound that requires severe, pressing treatment but receives only the lightest salve. False prophets treat a fatal wound as superficial: they apply a bandage where surgery is needed. The word &ldquo;lightly&rdquo; (qalal) measures the insufficiency of the treatment: they do not take the wound seriously enough to apply the painful marats-pressure it needs. This critique of surface-level religious healing runs through Jeremiah&rsquo;s confrontations with the temple establishment, the false prophets (notably Hananiah in ch. 28), and the priests. The NT applies the same diagnostic: 2 Timothy 4:3 describes teachers who &ldquo;heap up for themselves teachers to suit their own passions&rdquo; — the same preference for comfortable prophecy over true diagnosis. Ezekiel 13:10-16 continues the wound-metaphor: false prophets build a flimsy wall and whitewash it."
        },
        {
            "code": "H3289",
            "lemma": "יָעַץ",
            "translit": "yāʿaṣ",
            "gloss": "counsel",
            "significance": "יָעַץ (yaats, &lsquo;to advise, counsel, resolve — to deliberate and come to a decision&rsquo;) appears in Jeremiah&rsquo;s sustained confrontation between the counsel of God and the counsel of false prophets and human wisdom. Jeremiah 18:18: &ldquo;Then they said, &lsquo;Come, let us make plots against Jeremiah, for the law shall not perish from the priest, nor counsel (etsah) from the wise, nor the word from the prophet.&rsquo;&rdquo; Jeremiah 49:20: &ldquo;hear the plan (etsah) of the LORD that he has made against Edom.&rdquo; Jeremiah 32:19: God is &ldquo;great in counsel (etsah) and mighty in deed.&rdquo; The confrontation is structural: the human establishment claims its own counsel (the priest&rsquo;s law, the wise man&rsquo;s advice, the false prophet&rsquo;s word) as the guide for Judah, while Jeremiah declares the etsah YHWH — God&rsquo;s counsel — which comes out differently and is rejected. Isaiah 9:6 uses the same root for the coming Servant-King: &ldquo;Wonderful Counselor (yoets)&rdquo; — the one whose counsel surpasses all human wisdom. The NT applies this to Christ: in whom &ldquo;are hidden all the treasures of wisdom and knowledge&rdquo; (Col 2:3)."
        },
        {
            "code": "H3335",
            "lemma": "יָצַר",
            "translit": "yāṣar",
            "gloss": "form",
            "significance": "יָצַר (yatsar, &lsquo;to mold into a form — especially as a potter; figuratively, to determine or form a resolution&rsquo;) is the centerpiece of Jeremiah 18, where God commands the prophet to watch a potter at work. Jeremiah 18:4-6: &ldquo;The vessel he was making of clay was spoiled in the potter&rsquo;s hand, and he reworked it into another vessel... O house of Israel, can I not do with you as this potter (yotser) has done? declares the LORD. Behold, like the clay in the potter&rsquo;s hand, so are you in my hand.&rdquo; The same verb appears in Genesis 2:7: &ldquo;the LORD God formed (yatsar) man from the dust of the ground.&rdquo; The potter&rsquo;s reworking in Jeremiah 18 recapitulates the original creation: the God who first formed (yatsar) humanity from clay has the authority to reshape (yatsar) the nation according to his purposes. The passage insists on both sovereignty (God can reshape the clay) and contingency (Jer 18:7-10: if the nation repents, God changes his plans). Isaiah 29:16 and 45:9 use the same pottery metaphor for human rebellion against divine sovereignty. Paul applies it in Romans 9:20-21: &ldquo;Has the potter no right over the clay?&rdquo; — defending God&rsquo;s sovereign freedom in election."
        }
    ],

    "language_notes": (
        "<p>Jeremiah&rsquo;s most distinctive literary contribution to the OT is the <strong>prophetic confession as a genre</strong>. The six confessions (11:18-12:6; 15:10-21; 17:14-18; 18:18-23; 20:7-18) are extended lament prayers in which the prophet argues with God — expressing desire for vengeance, complaining that YHWH has deceived him (20:7: &ldquo;O LORD, you have deceived me&rdquo;), and in the most extreme case, cursing the day of his birth (20:14-18: &ldquo;Cursed be the day on which I was born!&rdquo;). This language is unprecedented in the prophets: Isaiah&rsquo;s objection (&ldquo;I am a man of unclean lips&rdquo; — 6:5) is immediately resolved; Jeremiah&rsquo;s anguish runs through the entire book without resolution. The confessions use the vocabulary and form of the individual lament psalms (complaint, address to God, petition, and sometimes a concluding assurance) but push them to a rawness the Psalms do not equal. The literary purpose is double: to document the cost of faithful prophetic ministry, and to establish Jeremiah as a type of the suffering servant — the one who speaks the true word and is rejected for it.</p>"
        "<p>Jeremiah exists in <strong>two significantly different text forms</strong>. The Masoretic Text (MT, Hebrew) and the Septuagint (LXX, Greek) differ by approximately one-eighth in length (LXX is shorter) and by arrangement (the oracles against the nations are in different positions). Several passages in the LXX are shorter than the MT by 2-3 verses; in other places, entire sections appear in a different sequence. The discovery of Jeremiah manuscripts at Qumran (Dead Sea Scrolls) confirmed that both the shorter and longer textual traditions existed in Hebrew antiquity — they are not LXX translator variations but two different editions of the book. Most scholars believe the LXX represents an earlier, shorter edition and the MT a later, expanded edition. The theological significance: Jeremiah may be the OT book with the most transparent editorial history — the book&rsquo;s composition was a process, not a single act.</p>"
        "<p>Jeremiah&rsquo;s <strong>apostasy vocabulary</strong> — centered on meshuvah (H4878, backsliding/turning-away) and its cognates — is built on the root shuv (to turn). This creates one of the great OT wordplay networks: shuv means both &ldquo;to return&rdquo; (repentance) and the base of meshuvah (apostasy). Jeremiah&rsquo;s repeated command &ldquo;return (shuv), O faithless Israel&rdquo; (3:12; 3:14; 3:22) and his diagnosis that Israel will not shuv (5:3; 8:5: &ldquo;they hold fast to deceit; they refuse to shuv&rdquo;) creates a sustained wordplay: the word for repentance and the root of the word for apostasy are the same, differentiated only by direction. This linguistic feature mirrors the theological reality: Israel stands at a turning point, and the same root describes both the path toward God and the path away. The Hebrew preacher can say &ldquo;shuv, or your meshuvah will destroy you&rdquo; — a sentence in which the same root points in opposite directions.</p>"
        "<p>The <strong>new covenant oracle of Jeremiah 31:31-34</strong> is the theological center of the book and the most theologically precise promise in the OT. Its grammar repays close attention. &ldquo;I will make a new covenant (berit chadashah) with the house of Israel and the house of Judah, not like the covenant that I made with their fathers on the day when I took them by the hand to bring them out of the land of Egypt&rdquo; (31:31-32). The covenant formula &ldquo;I will be their God and they shall be my people&rdquo; (31:33) is one of the oldest in the OT (cf. Exod 6:7; Lev 26:12; Jer 7:23; 11:4). But now three differences are specified: (1) the law will be written on the heart rather than on stone; (2) there will be a direct, universal knowledge of God — &ldquo;for they shall all know me, from the least of them to the greatest&rdquo;; (3) forgiveness will be complete and non-repeatable — &ldquo;I will forgive their iniquity, and I will remember their sin no more.&rdquo; These three specifications are precisely what the letter to the Hebrews develops as the achievement of Christ&rsquo;s high priesthood. The Hebrew construction &ldquo;I will remember their sin no more&rdquo; (lo ezkhar-od) uses the qal imperfect — a grammatical statement of ongoing non-remembrance, not just a single act of forgetting.</p>"
    ),

    "reception": (
        "<p><strong>Patristic and Medieval:</strong> The early church read Jeremiah primarily as a prophet of the new covenant and a type of Christ in his suffering. Justin Martyr used Jeremiah 31:31-34 as his strongest proof-text for the replacement of the Torah by the new covenant (an argument that Christians today handle more carefully). Tertullian drew extensively on Jeremiah&rsquo;s confessions and lament prayers in his discussions of Christian endurance under persecution. The &ldquo;weeping prophet&rdquo; tradition — Jeremiah as the paradigm of the one who suffers for speaking truth — was established patristically and persisted through the medieval period. Origen applied Jeremiah&rsquo;s confessions allegorically to the soul&rsquo;s suffering in spiritual warfare. The book&rsquo;s association with Lamentations (often attributed to Jeremiah by the tradition) gave rise to a sustained meditation on faithful grief.</p>"
        "<p><strong>Reformation:</strong> Calvin wrote one of his most extensive commentaries on Jeremiah, delivered as lectures in Geneva (1563). He insisted that the new covenant of Jeremiah 31 is not a replacement of the Abrahamic covenant but its renewal — the same grace, now more fully disclosed. Luther preached the Temple Sermon (ch. 7) as a warning against sacramentalism: the temple did not protect Jerusalem any more than external religious forms protect those who trust in them rather than God. Both reformers saw Jeremiah&rsquo;s confrontation with false prophets as the paradigm of the Reformation&rsquo;s confrontation with Rome — the establishment claiming authority while the true prophet spoke the unpopular word.</p>"
        "<p><strong>Modern debates:</strong> The most significant modern debate concerns the relationship between the &ldquo;Deuteronomistic prose&rdquo; sections of Jeremiah (the prose sermons in chs. 7, 11, 21-22, etc.) and the poetic sections generally taken as Jeremiah&rsquo;s authentic oracles. Some scholars (Mowinckel, Hyatt) attributed the prose to a &ldquo;Deuteronomistic school&rdquo; of editors; others (Holladay, Lundbom) defended them as substantially Jeremianic. The role of Baruch as the book&rsquo;s compiler and preserver has also been scrutinized: Jeremiah 36&rsquo;s account of the scroll burned by Jehoiakim and rewritten from dictation shows that the book was the product of deliberate collection. Contemporary scholarship has also rehabilitated Jeremiah 29:11 (&ldquo;plans for welfare and not for evil&rdquo;) from its frequent misquotation as individual promise to its actual context: a pastoral letter to exiles commanding them to seek the shalom of the city where they had been sent.</p>"
    ),

    "reading_guide": (
        "<p><strong>Don&rsquo;t read Jeremiah chronologically.</strong> The book is not arranged by date — it moves between periods of Josiah, Jehoiakim, Zedekiah, and the aftermath, often without clear transitions. The arrangement is thematic and literary, not historical. Use the headings and chapter introductions as clues to when each oracle was delivered, but don&rsquo;t expect a linear narrative. The book rewards reading by section: chapters 1-25 (oracles of judgment), 26-29 (confrontations with false prophets and the letter to the exiles), 30-33 (the &ldquo;Book of Comfort,&rdquo; including 31:31-34), and 34-52 (the historical narrative of Jerusalem&rsquo;s fall). Read the sections thematically rather than hunting for chronological sequence.</p>"
        "<p><strong>Read the confessions (chapters 11-20) alongside the oracles.</strong> They are not interruptions but the emotional foundation: you cannot understand Jeremiah&rsquo;s urgency without knowing its cost. The most extreme (20:7-18) ends with the most despairing statement in the OT: &ldquo;Cursed be the day on which I was born!&rdquo; Read this alongside chapter 31&rsquo;s new covenant promise — the same prophet who despairs in chapter 20 announces the greatest hope in chapter 31.</p>"
        "<p><strong>Hold the new covenant (chapter 31) as the interpretive center.</strong> Everything preceding it exists to explain why the old covenant failed and why something new was necessary: the heart is deceitful (17:9), law on stone cannot transform the stone-hard heart, the temple cannot save. Jeremiah 31:31-34 answers every preceding diagnosis: law written on the heart, direct knowledge of God, complete forgiveness. The NT&rsquo;s claim that Jesus established this new covenant at the Last Supper means every Christian reader encounters here the promise of their own covenant — grounded in Christ&rsquo;s blood.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('jeremiah')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('jeremiah', merged)

main()
