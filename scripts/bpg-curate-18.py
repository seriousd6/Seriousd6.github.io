"""
BPG Curation — Batch C18: irony → magic-magicians (gaps 1699–1798)
Gaps reviewed: 100 (score-10 smith-scholarly I–M range + concept-no-article)

Strong batch of NT epistle articles and key theological concepts: Isaiah (book),
James (epistle), 1 John, 2–3 John, Jubilee Year, Judges (book), Kings (books),
Lamentations, Laodiceans, Luke (Gospel), Magi, Magic. Also: Laying on of Hands,
Leaven, Lending, Lord's Day, Lots, Love Feasts, Loyalty, Lukewarmness.
27 stub-needed; 16 redirects; 57 names-only.

Script: scripts/bpg-curate-18.py
Run: python3 scripts/bpg-curate-18.py  (from project root)
"""

import json

GAPS_FILE = 'data/biblepedia/gaps.json'


def load_gaps():
    with open(GAPS_FILE, encoding='utf-8') as f:
        return json.load(f)


def save_gaps(gaps):
    with open(GAPS_FILE, 'w', encoding='utf-8') as f:
        json.dump(gaps, f, ensure_ascii=False, indent=2)


DECISIONS = {
    # ── I entries ─────────────────────────────────────────────────────────────
    "irony":                {"status": "names-only"},   # literary device; no dedicated biblical entry warranted
    # The Book of Isaiah: Servant Songs (Isa 52:13–53:12); Immanuel prophecy (Isa 7:14; Matt 1:23);
    # "righteous shall live by faith" precursor; "all we like sheep" (Isa 53:6); ~400 NT quotations
    "isaiah-book-of":       {"status": "stub-needed"},
    # Smith singular form of Ishmaelites; redirect to Ishmael's descendants article
    "ishmaelite":           {"status": "redirect-only", "redirect_to": "ishmael"},
    # Smith variant spelling of Ishmaelite
    "ishmeelite":           {"status": "redirect-only", "redirect_to": "ishmael"},
    "ishuah":               {"status": "names-only"},   # Asher's son (Gen 46:17; 1 Chr 7:30)
    "ishuai":               {"status": "names-only"},   # variant of Ishuah (1 Chr 7:30)
    "ishui":                {"status": "names-only"},   # variant of Ishuah
    "isle":                 {"status": "names-only"},   # generic geographic; individual islands have articles
    "israelite":            {"status": "names-only"},   # demonym; covered under Israel
    "isshiab":              {"status": "names-only"},   # obscure figure; not clearly identified
    "issue-running":        {"status": "names-only"},   # Lev 15 ritual uncleanness; covered under "uncleanness"
    "izeharites":           {"status": "names-only"},   # Levitical clan of Izhar (Num 3:27; 1 Chr 26:23)

    # ── J entries ─────────────────────────────────────────────────────────────
    "jaalah":               {"status": "names-only"},   # temple servant family (Ezra 2:56)
    # Smith compound; redirect to canonical slug for the city
    "jaazer-or-jazer":      {"status": "redirect-only", "redirect_to": "jazer"},
    "jahaz-also-jahaza-jahazah-and-juhzah": {"status": "names-only"},  # Moabite city; Moses vs Sihon (Num 21:23); place only
    # Redirect shorter forms to the same place article
    "jahaza":               {"status": "redirect-only", "redirect_to": "jahaz"},
    "jahazah":              {"status": "redirect-only", "redirect_to": "jahaz"},
    "jahnziah":             {"status": "names-only"},   # possibly corrupt entry; no clear canonical figure
    "jakamean":             {"status": "names-only"},   # Levite (1 Chr 23:19 variant of Jekameam)
    # Apostle "James son of Alphaeus" (Matt 10:3); "James the younger" (Mark 15:40);
    # possibly the James to whom the risen Christ appeared (1 Cor 15:7); distinct from James of Zebedee
    "james-the-less":       {"status": "stub-needed"},
    # The letter of James; "faith without works is dead" (Jas 2:26); wisdom tradition;
    # "taming the tongue" (Jas 3); trials and patience (Jas 1:2-4); authorship debate (Lord's brother vs apostle)
    "james-the-general-epistle-of": {"status": "stub-needed"},
    "jamnin":               {"status": "names-only"},   # probably Jabneel/Jamnia; minor location
    "janohah":              {"status": "names-only"},   # Ephraim town (2 Kgs 15:29; Josh 16:6-7)
    "japhleli":             {"status": "names-only"},   # "Japhletite" territory boundary (Josh 16:3)
    "jehalelel":            {"status": "names-only"},   # two OT figures (1 Chr 4:16; 2 Chr 29:12)
    "jehieli":              {"status": "names-only"},   # Levite (1 Chr 15:18,20; 26:21)
    # KJV form of Joshua; Greek form of the name; redirect to canonical article
    "jehoshuah":            {"status": "redirect-only", "redirect_to": "joshua"},
    # Greek form of Jephthah used in NT (Heb 11:32 KJV "Jephthae"); redirect to canonical
    "jephthae":             {"status": "redirect-only", "redirect_to": "jephthah"},
    "jerahmeelites":        {"status": "names-only"},   # clan south of Judah (1 Sam 27:10; 30:29)
    # Jerubbaal = Gideon's alternate name given after destroying Baal's altar (Judg 6:32);
    # Smith compound form; redirect to main Gideon article
    "jerubbaal-or-jerubbaal": {"status": "redirect-only", "redirect_to": "gideon"},
    "jerushah":             {"status": "names-only"},   # mother of King Jotham (2 Kgs 15:33; 2 Chr 27:1)
    "jeshuah":              {"status": "names-only"},   # variant of Jeshua; priestly/Levite name
    # Author of Sirach (Ecclesiasticus); deuterocanonical wisdom book; "the fear of the Lord is wisdom"
    # (Sir 1:16); significant for NT wisdom Christology background
    "jesus-the-son-of-sirach": {"status": "stub-needed"},
    "jewish":               {"status": "names-only"},   # adjective/demonym; too generic
    "jimna":                {"status": "names-only"},   # Asher's son (Gen 46:17 = Imnah)
    "jinah":                {"status": "names-only"},   # variant place name; minor location
    "jirjathaim":           {"status": "names-only"},   # two OT places (Gen 14:5; 1 Chr 4:23)
    "joaada":               {"status": "names-only"},   # variant of Jehoiada (Neh 12:10-11)
    # First letter of John; "God is love" (1 John 4:8); three tests of authentic Christianity;
    # "if we confess our sins" (1 John 1:9); "born of God" (1 John 5:1-5); anti-docetist context
    "john-the-first-epistle-general-of": {"status": "stub-needed"},
    # 2 John: "walking in truth and love"; warning against false teachers; 3 John: commending Gaius;
    # condemning Diotrephes; "the elder" as author; hospitality motif from 3 John 5-8
    "john-the-second-and-third-epistles-of": {"status": "stub-needed"},
    "jokdean":              {"status": "names-only"},   # Judah town (Josh 15:56)
    # Smith compound; redirect to canonical slug
    "joppa-or-japho":       {"status": "redirect-only", "redirect_to": "joppa"},
    "jorkoam":              {"status": "names-only"},   # Caleb's descendant (1 Chr 2:44)
    # High priest Jehozadak taken into Babylonian captivity (1 Chr 6:14-15); father of Joshua the priest;
    # Smith compound with equals sign; redirect to canonical
    "josedech-=-jehozadak": {"status": "redirect-only", "redirect_to": "jehozadak"},
    "jotbath-or-jotbathah": {"status": "names-only"},   # wilderness camp (Num 33:33-34; Deut 10:7)
    # Lev 25:8-55: 50th year; release of debt-slaves, land returns to original families;
    # "proclaim liberty throughout the land" (Lev 25:10); cited in Isa 61:1-2; Luke 4:18-19 (Jesus's inaugural sermon)
    "jubilee-the-year-of":  {"status": "stub-needed"},
    # Roman province form of Judah; redirect to canonical
    "judaea-or-judea":      {"status": "redirect-only", "redirect_to": "judah"},
    # Distinguishing the multiple biblical Judases: Iscariot; son of James (Luke 6:16 = Thaddaeus?);
    # Judas Barsabbas (Acts 15:22); Jude the apostle who wrote the epistle; brother of Jesus (Matt 13:55)
    "judas-jude":           {"status": "stub-needed"},
    # Smith variant form; redirect to the combined article
    "jude-or-judas":        {"status": "redirect-only", "redirect_to": "judas-jude"},
    # Book of Judges: period of the judges (c. 1380–1050 BC); cyclical sin-oppression-cry-deliverance;
    # Deborah, Gideon, Samson, Jephthah; "everyone did what was right in his own eyes" (Judg 21:25)
    "judges":               {"status": "stub-needed"},
    # Deuterocanonical; Judith beheads Holofernes (Assyrian general); Maccabean-era composition;
    # models of Jewish resistance; significant for apocryphal literature study
    "judith-the-book-of":   {"status": "stub-needed"},
    # Rom 16:7 "Greet Andronicus and Junia, my relatives and fellow prisoners, outstanding among the apostles";
    # whether Junia is female (early church consensus) vs Junias (male); key witness for women in NT church
    "junias":               {"status": "stub-needed"},

    # ── K entries ─────────────────────────────────────────────────────────────
    # Smith compound for Kadesh and Kadesh-barnea; redirect to canonical
    "kadesh-kadeshbarnea":  {"status": "redirect-only", "redirect_to": "kadesh"},
    "karkaa-or-karkaa":     {"status": "names-only"},   # south Judah border point (Josh 15:3)
    "kefr-kenna":           {"status": "names-only"},   # traditional site of Cana; modern village name
    "keilah-the-garmite":   {"status": "names-only"},   # compound Smith entry; place + epithet
    # The Kenites: Moses' father-in-law Jethro was a Kenite (Judg 1:16); Jael the Kenite killed Sisera
    # with a tent peg (Judg 4:17-22); Heber's clan; "blessed above women" (Judg 5:24); metalworkers
    "kenite-the":           {"status": "stub-needed"},
    # Smith compound; redirect to canonical slug for the valley/wadi
    "kidron-or-kedron":     {"status": "redirect-only", "redirect_to": "kidron"},
    "kings":                {"status": "names-only"},   # too generic; Book of Kings handled below
    # 1–2 Kings: Solomon's glory to Babylonian exile; temple built and destroyed; Elijah and Elisha;
    # Ahab and Jezebel; Hezekiah's reforms; Josiah's discovery of the Law; 586 BC fall of Jerusalem
    "kings-first-and-second-books-of": {"status": "stub-needed"},
    "kiriah":               {"status": "names-only"},   # variant of Kiriath; place name prefix
    # Smith's "Kison" = the Kishon River; Barak defeated Sisera here (Judg 4-5); Elijah killed
    # the prophets of Baal at the Kishon (1 Kgs 18:40); redirect to canonical spelling
    "kison":                {"status": "redirect-only", "redirect_to": "kishon"},
    "kneadingtroughs":      {"status": "names-only"},   # Exod 8:3; bread-making vessels; general
    # "Knowledge of God" (Hos 4:6); "fear of the LORD is beginning of knowledge" (Prov 1:7);
    # "knowledge puffs up, love builds up" (1 Cor 8:1); Gnostic claims about secret knowledge; NT epistemology
    "knowledge":            {"status": "stub-needed"},
    "korahite":             {"status": "names-only"},   # demonym; Korahite psalmists (Ps 42, 44-49)

    # ── L entries ─────────────────────────────────────────────────────────────
    "lachet":               {"status": "names-only"},   # sandal strap (Luke 3:16; John 1:27); single idiom
    "lakes":                {"status": "names-only"},   # general geographic; individual lakes have articles
    "lakum":                {"status": "names-only"},   # Naphtali border town (Josh 19:33)
    "lambs":                {"status": "names-only"},   # sacrificial lambs; covered under "lamb of God"
    # Book of Lamentations: five poems over Jerusalem's fall (586 BC); acrostic structure;
    # "Great is your faithfulness" (Lam 3:23); theology of suffering; liturgical use in Tisha B'Av
    "lamentations-of-jeremiah": {"status": "stub-needed"},
    "lancet":               {"status": "names-only"},   # lance/spear (1 Kgs 18:28 KJV); brief reference
    "language":             {"status": "names-only"},   # general; biblical languages covered elsewhere
    # Letter to Laodicea (Rev 3:14-22): "lukewarm — I will spit you out"; "wretched, pitiful, poor, blind and naked";
    # self-sufficient but spiritually bankrupt; also a lost Pauline letter (Col 4:16)
    "laodiceans":           {"status": "stub-needed"},
    "lasharon":             {"status": "names-only"},   # Canaanite king in Joshuah's conquest list (Josh 12:18)
    "latin-versions":       {"status": "names-only"},   # Vulgate; scholarly; covered under Jerome
    # Ordination (1 Tim 4:14; 2 Tim 1:6); healing (Mark 16:18; Acts 28:8); blessing children
    # (Matt 19:13-15); Spirit given (Acts 8:17-19; 19:6); foundational NT church rite
    "laying-on-of-hands":   {"status": "stub-needed"},
    # "Kingdom of heaven is like leaven" (Matt 13:33); "beware the leaven of the Pharisees"
    # (Matt 16:6; Luke 12:1); Passover unleavened bread (Exod 12:15-20); "a little leaven leavens the whole lump" (1 Cor 5:6-8)
    "leaven-yeast":         {"status": "stub-needed"},
    "lebanah":              {"status": "names-only"},   # temple servant family (Neh 7:48 variant)
    "leech":                {"status": "names-only"},   # Prov 30:15 KJV; single reference
    # OT usury laws: no interest from brothers (Deut 15:8; 23:19-20; Exod 22:25);
    # "lend, expecting nothing in return" (Luke 6:35); parable of servants/talents
    "lending":              {"status": "stub-needed"},
    "lieutenants":          {"status": "names-only"},   # KJV for Persian satraps (Ezra 8:36; Esth 3:12)
    "lign-aloes":           {"status": "names-only"},   # aloe wood (Num 24:6; Ps 45:8 KJV); botanical
    "lish":                 {"status": "names-only"},   # variant of Laish/Dan (Judg 18:29); same place
    "lmri":                 {"status": "names-only"},   # corrupt entry; probably Omri with missing initial
    "loaves":               {"status": "names-only"},   # feeding miracles; general; covered under individual narratives
    "lodge-to":             {"status": "names-only"},   # KJV infinitive entry; covered under hospitality
    "lookingglasses":       {"status": "names-only"},   # Exod 38:8; bronze mirrors; general cultural
    # "On the Lord's Day I was in the Spirit" (Rev 1:10); Sunday as resurrection day;
    # early church shift from Sabbath (Col 2:16-17; Acts 20:7; 1 Cor 16:2; Didache 14)
    "lords-day-the":        {"status": "stub-needed"},
    # Casting lots (Prov 16:33 "the lot is cast but its every decision is from the LORD");
    # Josh 18:6-10; Jonah 1:7; Matthias elected by lot (Acts 1:26); Purim's origin (Heb. pur = lot)
    "lot-the":              {"status": "stub-needed"},
    # Smith entry appears garbled (possibly "lots-feasts-of" = Purim); redirect to Purim
    "lots-feats-of":        {"status": "redirect-only", "redirect_to": "purim"},
    # Agape meal (Jude 12; 1 Cor 11:17-34 context); communal eating preceding the Lord's Supper;
    # abuse at Corinth; "when you come together it is not for the better but for the worse"
    "love-feasts":          {"status": "stub-needed"},
    # Hesed (Hebrew lovingkindness/loyalty); Ruth's loyalty to Naomi (Ruth 1:16-17);
    # "a friend loves at all times" (Prov 17:17); NT faithfulness motif
    "loyalty":              {"status": "stub-needed"},
    # Gospel of Luke; "seeking the lost" theme; parables of Lost Sheep, Coin, Son (Luke 15);
    # Magnificat (Luke 1:46-55); Jesus's ministry to women, Samaritans, sinners; Acts companion volume
    "luke-gospel-of":       {"status": "stub-needed"},
    # "Lukewarm" (Rev 3:15-16): Laodicean letter; "because you are lukewarm, I will spit you out";
    # spiritual half-heartedness; "cannot serve two masters" (Matt 6:24); NT theme of whole-hearted devotion
    "lukewarmness":         {"status": "stub-needed"},
    "lunatics":             {"status": "names-only"},   # KJV for seizure sufferers (Matt 4:24; 17:15); translation note

    # ── M entries ─────────────────────────────────────────────────────────────
    "maadai-or-maadai":     {"status": "names-only"},   # post-exile man with foreign wife (Ezra 10:34)
    "macaerus":             {"status": "names-only"},   # Herodian fortress; John Baptist's imprisonment (Josephus)
    "machirites-the":       {"status": "names-only"},   # clan of Machir (Num 26:29)
    # The wise men of Matt 2:1-12: Babylonian/Zoroastrian astronomers; star of Bethlehem;
    # visit to Bethlehem; three gifts (gold, frankincense, myrrh) named — not three men;
    # Herod's response; "we saw his star" — Gentile witness to the Messiah
    "magi":                 {"status": "stub-needed"},
    # Egyptian magicians vs Moses (Exod 7:11-12); Endor medium (1 Sam 28);
    # Simon Magus (Acts 8:9-24); Bar-Jesus/Elymas (Acts 13:6-11); Ephesian scrolls burned (Acts 19:19);
    # condemned in Deut 18:10-12; Rev 21:8; contrast with genuine prophetic power
    "magic-magicians":      {"status": "stub-needed"},
}


def main():
    gaps = load_gaps()
    idx = {g['id']: g for g in gaps}
    updated = 0
    missing = []
    for gid, decision in DECISIONS.items():
        if gid in idx:
            idx[gid].update(decision)
            updated += 1
        else:
            missing.append(gid)
    if missing:
        print(f'WARNING: {len(missing)} gap ids not found: {missing}')
    save_gaps(list(idx.values()))
    print(f'BPG Curation C18: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
