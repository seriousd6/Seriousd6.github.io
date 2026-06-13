"""
BPG Curation — Batch C25: american-revised-version → apply (gaps 2399–2498)
Gaps reviewed: 100 (score-5 isbe-scholarly A entries — mostly lexical, some theology)

Score-5 ISBE entries continue to be overwhelmingly lexical/archaic KJV terms and
minor compound forms. Notable stubs: Angel of Yahweh (pre-incarnate Christ debate),
Anthropology (imago Dei), Anthropomorphism, Antiochus IV Epiphanes (temple desecration),
Apocalyptic Literature, Apostasy, Apostles' Creed.
7 stub-needed; 3 redirects; 90 names-only.

Script: scripts/bpg-curate-25.py
Run: python3 scripts/bpg-curate-25.py  (from project root)
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
    "american-revised-version": {"status": "names-only"},  # ASV 1901; too specialized for biblepedia
    "amiable":              {"status": "names-only"},   # KJV Ps 84:1 "How amiable are your tabernacles"; lexical
    "amiss":                {"status": "names-only"},   # KJV "wrongly/improperly"; lexical
    "ammidioi;-ammidoi":    {"status": "names-only"},   # apocryphal figures (1 Esd 5:20)
    "ammihur":              {"status": "names-only"},   # ISBE variant of Ammihud; minor figure
    # ISBE compound form; redirect to canonical article on Ammon/Ammonites
    "ammon;-ammonites":     {"status": "redirect-only", "redirect_to": "ammon"},
    "amos-1":               {"status": "names-only"},   # ISBE disambiguation; Amos the prophet covered in Easton
    "amos-2":               {"status": "names-only"},   # NT genealogy (Luke 3:25); disambiguation only
    "amulet":               {"status": "names-only"},   # protective charm (Isa 3:20); covered under "magic"
    "anael":                {"status": "names-only"},   # Tobit's uncle (Tobit 1:21); apocryphal
    "ananias-1":            {"status": "names-only"},   # ISBE disambiguation; Ananias (Acts 5) in Easton
    "ananias-2":            {"status": "names-only"},   # ISBE disambiguation; Ananias (Acts 9) in Easton
    "ananiel":              {"status": "names-only"},   # Tobit's grandfather (Tobit 1:1); apocryphal
    "anathothite":          {"status": "names-only"},   # demonym for Anathoth; epithet for warriors
    "ancestors":            {"status": "names-only"},   # general concept; lexical
    "ancient":              {"status": "names-only"},   # lexical adjective
    "ancients":             {"status": "names-only"},   # KJV "elders/ancients"; lexical
    "ancle":                {"status": "names-only"},   # KJV spelling of "ankle" (Ezek 47:3); lexical
    "aner-1":               {"status": "names-only"},   # Amorite ally of Abram (Gen 14:13,24)
    "aner-2":               {"status": "names-only"},   # Levite town in Manasseh (1 Chr 6:70)
    "anetothite":           {"status": "names-only"},   # variant of Anathothite; demonym
    "angel-of-god":         {"status": "names-only"},   # covered under "theophany" and "angel of the Lord"
    # "The Angel of Yahweh" (מַלְאַךְ יְהוָה): OT theophanic appearances at burning bush (Exod 3:2),
    # to Gideon (Judg 6:11-23), to Manoah (Judg 13:3-22); identified with God himself (Gen 16:13);
    # debate: pre-incarnate Christ vs. created being; distinguished from other angels
    "angel-of-yahweh":      {"status": "stub-needed"},
    "angels-of-the-seven-churches": {"status": "names-only"},  # Rev 2-3; covered under Revelation
    "angle":                {"status": "names-only"},   # fishing hook (Isa 19:8; Matt 17:27); lexical
    "angling":              {"status": "names-only"},   # fishing technique; general
    "anglo-saxon-versions": {"status": "names-only"},   # ancient Bible translations; too specialized
    "anguish":              {"status": "names-only"},   # "anguish of soul" (Exod 6:9); general; lexical
    "anise;-dill":          {"status": "names-only"},   # "you tithe mint, anise and cumin" (Matt 23:23); plant
    "ankle":                {"status": "names-only"},   # Ezek 47:3; anatomical reference
    "anklet;-ankle-chain":  {"status": "names-only"},   # Isa 3:18-20 jewelry; cultural
    "annaas":               {"status": "names-only"},   # apocryphal figure (1 Esd 9:32)
    "annis":                {"status": "names-only"},   # variant; unclear
    "annul;-disannul":      {"status": "names-only"},   # KJV "make void"; lexical
    "annus":                {"status": "names-only"},   # minor compound variant
    "annuus":               {"status": "names-only"},   # minor variant
    "anoint;-anointed":     {"status": "names-only"},   # covered under "anointing" in Easton
    "anon":                 {"status": "names-only"},   # KJV "immediately" (Matt 13:20; Mark 1:12); lexical
    "anos":                 {"status": "names-only"},   # apocryphal figure (1 Esd 9:31)
    "answer":               {"status": "names-only"},   # lexical
    "answerable":           {"status": "names-only"},   # KJV; lexical
    "antediluvian-patriarchs": {"status": "names-only"},  # pre-flood patriarchs; covered individually
    "antediluvians":        {"status": "names-only"},   # people before the flood; covered under Noah
    "antelope":             {"status": "names-only"},   # clean animal (Deut 14:5); brief botanical
    "anthedon":             {"status": "names-only"},   # Philistine coastal city (1 Macc 13:13); apocryphal
    "anthothijah":          {"status": "names-only"},   # Benjaminite (1 Chr 8:24)
    # Biblical anthropology: humans created as image of God (imago Dei, Gen 1:26-27);
    # "from dust you came" (Gen 3:19); body, soul, spirit debate (1 Thess 5:23);
    # sin's effect on human nature; essential for theology of salvation and sanctification
    "anthropology":         {"status": "stub-needed"},
    # God described in human terms: "the hand of the LORD" (Exod 9:3); "God saw" (Gen 6:5);
    # "he repented" (Gen 6:6 KJV); "the eyes of the LORD" (Prov 15:3); necessary for finite
    # minds to understand infinite God; Maimonides' response; NT avoids in light of incarnation
    "anthropomorphism":     {"status": "stub-needed"},
    "anti-libanus":         {"status": "names-only"},   # Anti-Lebanon mountain range; geographic
    "antilogemena":         {"status": "names-only"},   # disputed canonical books (ISBE scholarly term)
    "antimony":             {"status": "names-only"},   # mineral; 1 Chr 29:2 KJV; general
    # ISBE place-type entry for Antioch of Syria; redirect to canonical article
    "antioch-in-syria":     {"status": "redirect-only", "redirect_to": "antioch"},
    # Paul's first missionary journey base (Acts 13:14-52); "almost the whole city gathered";
    # also covered under the main Antioch article; redirect
    "antioch-of-pisidia":   {"status": "redirect-only", "redirect_to": "antioch"},
    "antiochians":          {"status": "names-only"},   # demonym; covered under Antioch
    "antiochis":            {"status": "names-only"},   # Seleucid figure; apocryphal
    "antiochus-i":          {"status": "names-only"},   # Seleucid king; mainly intertestamental
    "antiochus-ii":         {"status": "names-only"},   # Seleucid king; mainly apocryphal context
    "antiochus-iii":        {"status": "names-only"},   # "Antiochus the Great"; Dan 11 background; brief
    # Antiochus IV Epiphanes: desecrated Jerusalem temple (168 BC); erected Zeus idol (Dan 11:31);
    # "abomination of desolation" (Dan 11:31; Matt 24:15; Mark 13:14); provoked Maccabean revolt;
    # models NT "man of lawlessness" typology; critical for Daniel and eschatology
    "antiochus-iv;-antiochus-epiphanes": {"status": "stub-needed"},
    "antiochus-v":          {"status": "names-only"},   # Eupator; brief reign; apocryphal
    "antiochus-vi":         {"status": "names-only"},   # child king; Seleucid
    "antiochus-vii":        {"status": "names-only"},   # Sidetes; last major Seleucid; apocryphal
    "antipater":            {"status": "names-only"},   # Herod's Idumean father; extrabiblical Josephus
    "antiquity":            {"status": "names-only"},   # general concept; lexical
    "anus":                 {"status": "names-only"},   # possibly a minor name variant in ISBE; not canonical
    "apace":                {"status": "names-only"},   # KJV "quickly"; lexical
    "apame":                {"status": "names-only"},   # Persian queen (1 Esd 4:29); apocryphal
    "apart":                {"status": "names-only"},   # lexical
    "aphaerema":            {"status": "names-only"},   # Judean district (1 Macc 11:34); apocryphal
    "apharsathchites;-apharsachites": {"status": "names-only"},  # Samaritan settlers (Ezra 4:9); variant
    "apherema":             {"status": "names-only"},   # variant of Aphaerema; apocryphal
    "apherra":              {"status": "names-only"},   # returned exile family variant (1 Esd 5:34)
    "apocalypse-of-baruch": {"status": "names-only"},   # pseudepigraphical; too specialized
    # Daniel, Revelation, 1 Enoch, 4 Ezra, Apocalypse of Peter; characteristics: visions, symbols,
    # cosmic dualism, angelology, eschatological vindication; "revelation of hidden things";
    # essential context for understanding Daniel and Revelation
    "apocalyptic-literature": {"status": "stub-needed"},
    "apocryphal-acts":      {"status": "names-only"},   # extracanonical; too specialized
    "apocryphal-epistles":  {"status": "names-only"},   # extracanonical; too specialized
    "apocryphal-gospels":   {"status": "names-only"},   # individual gospels have varying articles; general
    "apollophanes":         {"status": "names-only"},   # Seleucid figure (2 Macc 10:37); apocryphal
    # "It is impossible… to bring back to repentance those who have fallen away" (Heb 6:4-6);
    # "if we disown him, he will disown us" (2 Tim 2:12); Demas who "loved this world" (2 Tim 4:10);
    # ongoing debate about Calvinist vs Arminian readings of apostasy passages
    "apostasy;-apostate":   {"status": "stub-needed"},
    # Ancient baptismal creed summarizing Christian faith: "I believe in God the Father Almighty…
    # and in Jesus Christ his only Son… born of the Virgin Mary… third day he rose from the dead…
    # I believe in the Holy Spirit, the holy catholic Church, the communion of saints…";
    # not composed by apostles; early 2nd-century origin; foundational for catechesis
    "apostles-creed;-the":  {"status": "stub-needed"},
    "apostles-gospel-of-the-twelve": {"status": "names-only"},  # extracanonical; apocryphal
    "apostolic-age":        {"status": "names-only"},   # period of apostles; covered under Acts/church history
    "apostolic-fathers":    {"status": "names-only"},   # Clement, Ignatius, Polycarp; too specialized at score-5
    "apostolic-fathers-epistles-of": {"status": "names-only"},  # too specialized
    "apostolical-church-ordinances": {"status": "names-only"},  # early church document; extracanonical
    "apostolical-constitutions": {"status": "names-only"},  # early church document
    "apostolical-council":  {"status": "names-only"},   # Jerusalem Council (Acts 15); covered under that article
    "apparently":           {"status": "names-only"},   # lexical
    "apparition":           {"status": "names-only"},   # KJV ghost/vision; lexical
    "appear":               {"status": "names-only"},   # lexical
    "appearance":           {"status": "names-only"},   # lexical
    "appearing":            {"status": "names-only"},   # Christ's appearing/parousia; lexical; covered elsewhere
    "appease":              {"status": "names-only"},   # lexical
    "appertain":            {"status": "names-only"},   # KJV "belong to"; lexical
    "appetite":             {"status": "names-only"},   # "the righteous eat to satisfy their appetite" (Prov 13:25)
    "apphus":               {"status": "names-only"},   # Jonathan Maccabee's surname (1 Macc 2:5); apocryphal
    "apple-of-the-eye":     {"status": "names-only"},   # Ps 17:8; Zech 2:8; idiom; brief
    "apple;-apple-tree":    {"status": "names-only"},   # Song of Solomon; OT botanical; general
    "apples-of-sodom":      {"status": "names-only"},   # plant near Dead Sea; botanical reference
    "apply":                {"status": "names-only"},   # lexical
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
    print(f'BPG Curation C25: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
