"""
BPG Curation — Batch C22: trouble → abiron (gaps 2099–2198)
Gaps reviewed: 100 (final score-10 S–Z + score-8 concept + score-5 isbe-scholarly A entries)

Notable stubs: Trouble, Trumpet, Unclean Meats, Veil, Ancient Versions (Bible),
Authorized Version, Vulgate, Walking (spiritual), Wilderness Wandering,
Witchcraft, Women (in Scripture), Sabbatical Year, Zechariah (book), Festus,
Aaron's Rod.
15 stub-needed; 22 redirects; 63 names-only.

Script: scripts/bpg-curate-22.py
Run: python3 scripts/bpg-curate-22.py  (from project root)
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
    # ── Score-10 T–Z entries ──────────────────────────────────────────────────
    # "In this world you will have trouble. But take heart! I have overcome the world" (John 16:33);
    # "Cast all your anxiety on him" (1 Pet 5:7); Ps 34:19; Job as paradigm case
    "trouble":              {"status": "stub-needed"},
    # Silver trumpets (Num 10:1-10); shofar at Sinai (Exod 19:16); Feast of Trumpets (Lev 23:24);
    # Jericho walls (Josh 6); "last trumpet" at resurrection (1 Cor 15:52; 1 Thess 4:16)
    "trumpet":              {"status": "stub-needed"},
    "uncharitableness":     {"status": "names-only"},   # "do not judge" (Matt 7:1); covered under charity
    # Lev 11 clean/unclean food laws; Peter's vision (Acts 10:9-16); Mark 7:14-23 "nothing outside…
    # makes a person unclean"; Rom 14:14; Col 2:16; NT fulfillment and ongoing debate
    "unclean-meats":        {"status": "stub-needed"},
    # Smith compound for Urbanus in Rom 16:9; redirect to canonical
    "urbane-or-urbane":     {"status": "redirect-only", "redirect_to": "urbanus"},
    # Greek NT form of Uriah used in Matt 1:6 "wife of Urias"; redirect to canonical Uriah
    "urias":                {"status": "redirect-only", "redirect_to": "uriah"},
    "ut":                   {"status": "names-only"},   # likely variant of Uz (Job 1:1); minor
    "uthii":                {"status": "names-only"},   # possibly Uthai variant (1 Chr 9:4); minor figure
    # Smith compound for Uzzah who touched the ark and died (2 Sam 6:6-7); "God's anger burned against Uzzah"
    "uzza-or-uzzah":        {"status": "redirect-only", "redirect_to": "uzzah"},
    "uzza-the-garden-of":   {"status": "names-only"},   # burial garden of Manasseh and Amon (2 Kgs 21:18,26)
    "uzzielites-the":       {"status": "names-only"},   # Levitical clan of Uzziel (Num 3:27; 1 Chr 26:23)
    # "Moses put a veil over his face" (Exod 34:33-35); torn temple veil at crucifixion (Matt 27:51);
    # 2 Cor 3:12-18 "unveiled faces"; 1 Cor 11:5-6 head covering; access to God's presence
    "veil":                 {"status": "stub-needed"},
    # Architectural element in the Tabernacle and Temple; covered under the "veil" article
    "veil-of-the-tabernacle-and-temple": {"status": "redirect-only", "redirect_to": "veil"},
    # LXX (Septuagint), Peshitta (Syriac), Vulgate (Latin), Coptic versions;
    # textual criticism background; transmission of Hebrew scriptures into Greek world
    "versions-ancient-of-the-old-and-new-testaments": {"status": "stub-needed"},
    # The Authorized (King James) Version of 1611; translation history; "Authorized" designation;
    # influence on English literature and worship; textual basis (Textus Receptus)
    "versions-authorized":  {"status": "stub-needed"},
    "vineyards-plain-of-the": {"status": "names-only"},  # Jordan Valley location (Judg 11:33)
    # Jerome's Latin translation (382-405 AD); became standard Catholic Bible; Council of Trent;
    # Vulgate errors vs. Erasmus's Greek NT; influence on medieval theology
    "vulgate-the":          {"status": "stub-needed"},
    # "Walk in the Spirit" (Gal 5:16); "walk worthy of the calling" (Eph 4:1);
    # "Enoch walked with God" (Gen 5:22,24); "walk in the light" (1 John 1:7); Hebrew halakha
    "walking":              {"status": "stub-needed"},
    "walls":                {"status": "names-only"},   # Jericho, Nehemiah; general reference
    # Israel's 40 years in the wilderness (Num 14:33-34); faithlessness caused delay;
    # 1 Cor 10:1-11 "these things happened as examples for us"; cloud and fire; manna; water from rock
    "wandering-in-the-wilderness": {"status": "stub-needed"},
    "washing-the-hands-and-feet": {"status": "names-only"},  # Pilate/foot-washing; covered separately
    "watches-of-night":     {"status": "names-only"},   # Roman night divisions (Mark 13:35); cultural detail
    # Smith place variant; redirect to the event article
    "wilderness-of-the-wandering": {"status": "redirect-only", "redirect_to": "wandering-in-the-wilderness"},
    "wills":                {"status": "names-only"},   # Heb 9:16-17; too brief a topic
    # ISBE/Smith combined title for Sirach; redirect to the article already stub-needed in C18
    "wisdom-of-jesus-son-of-sirach": {"status": "redirect-only", "redirect_to": "jesus-the-son-of-sirach"},
    # Smith compound title; redirect to article marked stub-needed in C11
    "wisdom-the-of-solomon": {"status": "redirect-only", "redirect_to": "solomon-wisdom-of"},
    # Witch of Endor (1 Sam 28:7-25); condemned (Lev 19:31; Deut 18:10-12);
    # "witchcraft" as work of the flesh (Gal 5:20); Simon Magus (Acts 8:9-24)
    "witch-witchcrafts":    {"status": "stub-needed"},
    # Women in Scripture: disciples of Jesus (Luke 8:1-3); women at tomb (first witnesses);
    # Phoebe (Rom 16:1-2); Priscilla (Acts 18:26); Junia (Rom 16:7); Deborah; Esther; Ruth;
    # "male and female he created them" (Gen 1:27); NT women in ministry debate
    "women":                {"status": "stub-needed"},
    "words":                {"status": "names-only"},   # too broad; "Word" as Logos covered under "logos"
    # Smith variant form; redirect to jubilee article already stub-needed in C18
    "year-of-jubilee":      {"status": "redirect-only", "redirect_to": "jubilee-the-year-of"},
    # Sabbatical year: land rest every 7th year (Lev 25:1-7; Exod 23:10-11);
    # debts cancelled (Deut 15:1-11); release of Hebrew slaves (Deut 15:12-18); Shemitah
    "year-sabbatical":      {"status": "stub-needed"},
    "young-men":            {"status": "names-only"},   # general reference; too broad for single article

    # ── Score-10 Z entries ─────────────────────────────────────────────────────
    "zaavan-or-zavan":      {"status": "names-only"},   # Edomite chief (Gen 36:27; 1 Chr 1:42)
    "zabadeans":            {"status": "names-only"},   # Arab tribe (1 Macc 12:31); apocryphal
    "zalmon-mount":         {"status": "names-only"},   # mountain near Shechem (Judg 9:48)
    # KJV "Zara" in Matt 1:3 = Zerah, Judah's twin (Gen 38:30); Smith compound; redirect to canonical
    "zara-or-zarah":        {"status": "redirect-only", "redirect_to": "zerah"},
    # Smith variant form of Zerah; redirect to canonical
    "zarah-or-zerah":       {"status": "redirect-only", "redirect_to": "zerah"},
    "zareathites-the":      {"status": "names-only"},   # Kenite clan (1 Chr 2:53)
    "zared-the-valley-of":  {"status": "names-only"},   # Zered brook (Num 21:12; Deut 2:13-14)
    "zaretan-or-zarthan":   {"status": "names-only"},   # Jordan Valley location (Josh 3:16; 1 Kgs 4:12)
    "zarhites-the":         {"status": "names-only"},   # clan of Zerah (Num 26:13,20; Josh 7:17)
    "zebulunites-the":      {"status": "names-only"},   # tribe of Zebulun demonym
    # Smith compound for Zechariah; concept-no-article signals Nave entries;
    # redirect to canonical prophet article
    "zechariah-zecharias":  {"status": "redirect-only", "redirect_to": "zechariah"},
    # Book of Zechariah: post-exilic prophet (520 BC); messianic prophecies quoted 40+ times in NT;
    # Zech 9:9 (triumphal entry); 11:12-13 (30 silver coins); 12:10 ("they will look on me whom they pierced");
    # night visions; "not by might nor by power, but by my Spirit" (Zech 4:6)
    "zechariah-the-book-of": {"status": "stub-needed"},
    "zelok":                {"status": "names-only"},   # obscure; not clearly identified in canonical texts
    "zemarite-the":         {"status": "names-only"},   # Canaanite people group (Gen 10:18)
    "zephi":                {"status": "names-only"},   # Edomite chief (1 Chr 1:36 = Zepho)
    # Smith compound for Sidon; redirect to canonical
    "zidon-or-sidon":       {"status": "redirect-only", "redirect_to": "sidon"},
    "zidonians":            {"status": "names-only"},   # demonym for Sidon; covered under Sidon
    "ziphim-the":           {"status": "names-only"},   # people of Ziph who betrayed David's location (1 Sam 23:19)
    "ziphran":              {"status": "names-only"},   # boundary marker (Num 34:9)
    # Smith compound for Zipporah (Moses' wife, Exod 2:21; 4:25); redirect to canonical
    "zipporah-or-zipporah": {"status": "redirect-only", "redirect_to": "zipporah"},
    # Smith compound for Zobah (Aramean kingdom; David fought Hadadezer, 2 Sam 8:3-12)
    "zoba-or-zobah":        {"status": "redirect-only", "redirect_to": "zobah"},
    "zorathites-the":       {"status": "names-only"},   # Kenite clan (1 Chr 2:53)
    "zorites-the":          {"status": "names-only"},   # Kenite clan (1 Chr 2:54)
    "zuzim-the":            {"status": "names-only"},   # ancient people group (Gen 14:5 = Zamzummim)

    # ── Score-8 concept-no-article ─────────────────────────────────────────────
    # KJV form of Abijah; redirect to canonical
    "abiah":                {"status": "redirect-only", "redirect_to": "abijah"},
    "apharsathchites":      {"status": "names-only"},   # Samaritan settlers in Ezra 4:9 (KJV)
    "baale":                {"status": "names-only"},   # Baalah = Kiriath-jearim variant (Josh 15:9-10)
    "berothai":             {"status": "names-only"},   # Aramean city (2 Sam 8:8 = Berothah)
    "beth-shan":            {"status": "names-only"},   # where Philistines hung Saul's body (1 Sam 31:10)
    # Variant spelling of Caesar; redirect to canonical
    "cesar":                {"status": "redirect-only", "redirect_to": "caesar"},
    "cuth":                 {"status": "names-only"},   # people relocated to Samaria (2 Kgs 17:24,30)
    # Greek form of Aeneas (Acts 9:32-35); Peter healed Aeneas at Lydda; redirect to canonical
    "eneas":                {"status": "redirect-only", "redirect_to": "aeneas"},
    # Porcius Festus (Acts 24:27-26:32); Paul's appeal to Caesar; "Festus said, 'Paul, you are out
    # of your mind'" (Acts 26:24); diplomatic handling of Paul's case; transition from Felix
    "festus":               {"status": "stub-needed"},
    "habaiah":              {"status": "names-only"},   # priestly family barred from ministry (Ezra 2:61)
    "kenizzites":           {"status": "names-only"},   # Kenizzite people (Gen 15:19); Caleb was a Kenizzite
    "malcham":              {"status": "names-only"},   # Ammonite deity = Milcom (Zeph 1:5 KJV) or Benjaminite
    "nethinims":            {"status": "names-only"},   # KJV form of Nethinim (temple servants); Ezra 2:43-58
    "ramath":               {"status": "names-only"},   # several OT places named Ramath (Judg 10:17; 1 Sam 30:27)
    "salah":                {"status": "names-only"},   # ancestor of Abram (Gen 10:24; Luke 3:35 = Shelah)
    "sardites":             {"status": "names-only"},   # clan of Sered (Num 26:26 variant)
    "shalisha":             {"status": "names-only"},   # land Saul searched (1 Sam 9:4)
    "tel-harsa":            {"status": "names-only"},   # Babylonian exile settlement (Ezra 2:59)
    "zuzims":               {"status": "names-only"},   # variant of Zuzim/Zamzummim (Gen 14:5)

    # ── Score-5 isbe-scholarly (A entries) ────────────────────────────────────
    "aalar":                {"status": "names-only"},   # obscure ISBE entry; not in canonical texts
    # Aaron's rod that budded (Num 17:1-11) confirmed Levitical priesthood; swallowed Egyptian rods
    # (Exod 7:12); kept in ark as memorial (Heb 9:4); sign of divine appointment
    "aarons-rod":           {"status": "stub-needed"},
    "ab-1":                 {"status": "names-only"},   # Hebrew month Av (5th month); ISBE lexical entry
    "ab-2":                 {"status": "names-only"},   # Hebrew prefix "father"; lexical
    # ISBE form of Habakkuk; redirect to canonical article
    "abacuc":               {"status": "redirect-only", "redirect_to": "habakkuk"},
    # ISBE form of Obadiah; redirect to canonical article
    "abadias":              {"status": "redirect-only", "redirect_to": "obadiah"},
    "abagarus":             {"status": "names-only"},   # legendary King of Edessa; apocryphal Jesus correspondence
    # Abana/Abanah river in Damascus (2 Kgs 5:12 "Are not Abana and Pharpar…better than all the waters
    # of Israel?"); Naaman's objection; redirect to canonical spelling
    "abanah":               {"status": "redirect-only", "redirect_to": "abana"},
    "abase":                {"status": "names-only"},   # KJV "abase" = humble; Phil 4:12; lexical
    "abate":                {"status": "names-only"},   # KJV "abate" = decrease (Gen 8:8); lexical
    # Latin/Greek form of Obadiah; redirect to canonical article
    "abdias":               {"status": "redirect-only", "redirect_to": "obadiah"},
    "abdon-1":              {"status": "names-only"},   # minor judge (Judg 12:13-15)
    "abdon-2":              {"status": "names-only"},   # Benjaminite and other figures (1 Chr 8:23 etc.)
    "abel-1":               {"status": "names-only"},   # ISBE disambiguation; Abel the person covered in Easton
    "abel-2":               {"status": "names-only"},   # Abel the place (2 Sam 20:14-18); various "Abel" cities
    "abel-beth-maacah":     {"status": "names-only"},   # Abel-beth-maacah city (2 Sam 20:14-15; 2 Kgs 15:29)
    "abgar;-abgarus;-abagarus": {"status": "names-only"},  # ISBE compound; extrabiblical king; apocryphal
    "abhor":                {"status": "names-only"},   # KJV "abhor" (Amos 5:21; Rom 12:9); lexical entry
    "abi-1":                {"status": "names-only"},   # mother of Hezekiah (2 Kgs 18:2 = Abijah)
    "abi-2":                {"status": "names-only"},   # Hebrew name prefix "my father"; lexical
    # ISBE compound for Abijah; redirect to canonical spelling
    "abia;-abiah":          {"status": "redirect-only", "redirect_to": "abijah"},
    "abide":                {"status": "names-only"},   # KJV "abide/remain" (John 15:4-10); lexical
    "abigail;-abigal":      {"status": "names-only"},   # ISBE disambiguation; Abigail covered in Easton
    "ability":              {"status": "names-only"},   # "to each according to his ability" (Matt 25:15); lexical
    "abiron":               {"status": "names-only"},   # ISBE form of Abiram (Num 16 variant)
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
    print(f'BPG Curation C22: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
