"""
BPG Curation — Batch C50: jackal → joadanus (gaps 5099–5198)
Gaps reviewed: 100 (score-5 isbe-scholarly J entries)

J-range names, apocryphal figures, and compound ISBE forms. No stubs:
all significant J-range concepts are covered in Easton/Smith. Eleven
redirects for variant spellings and ISBE compound forms (jahweh, jairus
disambiguation, Jebusite variants, joash/jehoram pairs, etc.).
0 stub-needed; 11 redirects; 89 names-only.

Script: scripts/bpg-curate-50.py
Run: python3 scripts/bpg-curate-50.py  (from project root)
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
    "jackal":                 {"status": "names-only"},   # animal (Job 30:29; Isa 34:13); natural history
    "jackals-well":           {"status": "names-only"},   # Neh 2:13; Jerusalem geographic
    "jacob-1":                {"status": "names-only"},   # patriarch; covered extensively in Easton as "Jacob"
    "jacob-2":                {"status": "names-only"},   # ISBE disambiguation; same Easton article
    "jacob-testament-of":     {"status": "names-only"},   # pseudepigraphical; apocryphal; too specialized
    "jacubus":                {"status": "names-only"},   # apocryphal variant name
    "jaddai":                 {"status": "names-only"},   # returned exile (Ezra 10:43); minor name
    "jaddus":                 {"status": "names-only"},   # high priest (Josephus); extrabiblical/intertestamental
    "jahleelites-the":        {"status": "names-only"},   # Zebulun clan (Num 26:26); minor demonym
    # ISBE variant spelling of Yahweh/Jehovah; redirect to canonical Easton "Jehovah"
    "jahweh":                 {"status": "redirect-only", "redirect_to": "jehovah"},
    "jahzeel-and-jahziel":    {"status": "names-only"},   # Naphtali clan (Gen 46:24; Num 26:48); minor names
    "jahzeelites-the":        {"status": "names-only"},   # clan of Jahzeel; minor demonym
    "jahzeiah":               {"status": "names-only"},   # postexilic figure (Ezra 10:15); minor name
    "jailor":                 {"status": "names-only"},   # Acts 16:23-36 Philippian jailer; covered under "Philippi"
    # ISBE disambiguation 1; redirect to canonical Easton "Jairus"
    "jairus-1":               {"status": "redirect-only", "redirect_to": "jairus"},
    # ISBE disambiguation 2; redirect to canonical Easton "Jairus"
    "jairus-2":               {"status": "redirect-only", "redirect_to": "jairus"},
    "jalam":                  {"status": "names-only"},   # Esau's son (Gen 36:5,14,18; 1 Chr 1:35); minor name
    "jambri":                 {"status": "names-only"},   # Maccabean people (1 Macc 9:36-42); apocryphal
    "james-protevangelium-of": {"status": "names-only"},  # extracanonical apocryphal gospel; too specialized
    "jaminites":              {"status": "names-only"},   # Simeon clan (Num 26:12); minor demonym
    "jamnia":                 {"status": "names-only"},   # Jabneh in Maccabees; covered under "Jabneh"
    "jamnites":               {"status": "names-only"},   # demonym for Jamnia; minor
    "janai":                  {"status": "names-only"},   # Gadite (1 Chr 5:12); minor name
    "jangling":               {"status": "names-only"},   # KJV "vain talking" (1 Tim 1:6); lexical
    "janim":                  {"status": "names-only"},   # Judah village (Josh 15:53); minor geographic
    "jannai":                 {"status": "names-only"},   # NT genealogy (Luke 3:24); minor name
    "jannes-and-jambres":     {"status": "names-only"},   # Egyptian magicians (2 Tim 3:8); covered in Easton
    "jannes-and-jambres-book-of": {"status": "names-only"},  # pseudepigraphical; apocryphal; too specialized
    "japheth-1":              {"status": "names-only"},   # Noah's son; covered in Easton as "Japheth"
    "japheth-2":              {"status": "names-only"},   # ISBE disambiguation; same Easton article
    "japhia-1":               {"status": "names-only"},   # Canaan king (Josh 10:3); minor
    "japhia-2":               {"status": "names-only"},   # David's son (2 Sam 5:15; 1 Chr 3:7); minor
    "japhleti":               {"status": "names-only"},   # territorial clan (Josh 16:3); minor geographic
    "jar":                    {"status": "names-only"},   # vessel; lexical/cultural
    "jasaelus;-jasael":       {"status": "names-only"},   # apocryphal name
    "jashar-book-of":         {"status": "names-only"},   # lost book (Josh 10:13; 2 Sam 1:18); ISBE variant spelling
    "jasher-book-of":         {"status": "names-only"},   # lost book referenced in OT; brief; covered in Easton
    "jashubites-the":         {"status": "names-only"},   # Issachar clan (Num 26:24); minor demonym
    "jason-1":                {"status": "names-only"},   # Jason of Thessalonica (Acts 17:5-9); covered in Easton
    "jason-2":                {"status": "names-only"},   # High Priest Jason (2 Macc 4:7); intertestamental
    "jasper;-jaspis":         {"status": "names-only"},   # gemstone (Rev 4:3; 21:11); covered under "Stones, Precious"
    "jasubus":                {"status": "names-only"},   # apocryphal name
    "jatal":                  {"status": "names-only"},   # apocryphal name
    "jathan":                 {"status": "names-only"},   # apocryphal name
    "jathbath":               {"status": "names-only"},   # variant of Jotbath (Num 33:33-34); geographic
    "jaw;-jawbone;-jaw-teeth": {"status": "names-only"},  # Samson's jawbone (Judg 15:15-17); cultural/lexical
    "jealousy-water-of":      {"status": "names-only"},   # Num 5 ordeal; covered under "Ordeal, Trial by" in Easton
    "jearim-mount":           {"status": "names-only"},   # Judah boundary (Josh 15:10); geographic
    "jeatherai;-jeaterai":    {"status": "names-only"},   # Gershomite Levite (1 Chr 6:21); minor name
    # ISBE compound; redirect to canonical Easton "Jebusites"
    "jebus;-jebusi;-jebusite": {"status": "redirect-only", "redirect_to": "jebusites"},
    "jechiliah":              {"status": "names-only"},   # Uzziah's mother (2 Kings 15:2); minor name
    "jechonias":              {"status": "names-only"},   # Greek form of Jeconiah; covered under "Jehoiachin"
    "jeddu":                  {"status": "names-only"},   # apocryphal name
    "jedeus":                 {"status": "names-only"},   # apocryphal name
    "jeeli":                  {"status": "names-only"},   # apocryphal name
    "jeelus":                 {"status": "names-only"},   # apocryphal name
    "jeezerites":             {"status": "names-only"},   # Asherite clan (Num 26:44); minor demonym
    "jehallelel;-jehaleleel": {"status": "names-only"},   # two Judah figures (1 Chr 4:16; 2 Chr 29:12); minor
    "jehezkel;-jehezekel":    {"status": "names-only"},   # priest (1 Chr 24:16); minor name
    "jehiel;-jehieli":        {"status": "names-only"},   # several OT figures; minor names
    "jehoaddah;-jehoadah":    {"status": "names-only"},   # Benjaminite (1 Chr 8:36); minor name
    "jehoaddin":              {"status": "names-only"},   # Amaziah's mother (2 Kings 14:2; 2 Chr 25:1); minor
    # ISBE compound; redirect to canonical Easton "Joash"
    "jehoash;-joash":         {"status": "redirect-only", "redirect_to": "joash"},
    # ISBE compound; redirect to canonical Easton "Jehoram"
    "jehoram;-joram":         {"status": "redirect-only", "redirect_to": "jehoram"},
    "jehoshaphat-1":          {"status": "names-only"},   # King Jehoshaphat; covered in Easton as "Jehoshaphat"
    "jehoshaphat-2":          {"status": "names-only"},   # Valley of Jehoshaphat (Joel 3:2,12); covered under "Jehoshaphat"
    "jehovah-servant-of":     {"status": "names-only"},   # Servant Songs (Isa 42-53); covered under "Servant of Jehovah"
    "jehovah-tsidkenu-tsidkenu": {"status": "names-only"},  # "LORD our Righteousness" (Jer 23:6); covered under "Jehovah"
    "jehuel":                 {"status": "names-only"},   # variant of Jeiel; minor Levite name
    "jekabzel":               {"status": "names-only"},   # postexilic Judah town (Neh 11:25); geographic
    "jekameam":               {"status": "names-only"},   # Levite family (1 Chr 23:19; 24:23); minor name
    "jemimah":                {"status": "names-only"},   # Job's daughter (Job 42:14); minor name
    "jemnaan":                {"status": "names-only"},   # apocryphal place name
    "jeopard;-jeopardy":      {"status": "names-only"},   # KJV "endanger/risk" (1 Chr 11:19; 1 Cor 15:30); lexical
    "jerahmeel;-jerahmeelites": {"status": "names-only"},  # Judah figure and clan (1 Chr 2:9,25-41); minor
    # ISBE variant spelling of Jericho; redirect to canonical Easton "Jericho"
    "jerechu;-jerechus":      {"status": "redirect-only", "redirect_to": "jericho"},
    "jeremiah-1":             {"status": "names-only"},   # the prophet; covered extensively in Easton as "Jeremiah"
    "jeremiah-2":             {"status": "names-only"},   # other figures named Jeremiah; disambiguation
    "jeremiah-epistle-of":    {"status": "names-only"},   # apocryphal letter (= Baruch 6); extracanonical
    # ISBE article on Lamentations; redirect to canonical Easton "Lamentations"
    "jeremiah-the-lamentations-of": {"status": "redirect-only", "redirect_to": "lamentations"},
    "jeremiel":               {"status": "names-only"},   # archangel in 2 Esd 4:36; apocryphal
    "jeremy-the-epistle-of":  {"status": "names-only"},   # ISBE compound; same as jeremiah-epistle-of; apocryphal
    "jerusalem-new":          {"status": "names-only"},   # "New Jerusalem" (Rev 21:2,10); covered under "Jerusalem"
    "jeshua;-jeshuah":        {"status": "names-only"},   # covered under "Jeshua" in Easton (Joshua/Jeshua variants)
    "jesias":                 {"status": "names-only"},   # apocryphal name
    "jesting":                {"status": "names-only"},   # KJV "coarse joking" (Eph 5:4); lexical
    "jesus-christ-the-arrest-and-trial-of": {"status": "names-only"},  # covered under "Jesus Christ" in Easton
    "jesus-justus":           {"status": "names-only"},   # Paul's companion (Col 4:11); minor NT figure
    # ISBE compound; redirect to canonical Easton "Genealogy of Christ"
    "jesus-genealogy-of":     {"status": "redirect-only", "redirect_to": "genealogy"},
    "jew-jewess-jewish":      {"status": "names-only"},   # ethnic term; covered under "Jew" in Easton
    "jews":                   {"status": "names-only"},   # covered under "Jew" in Easton
    "jezelus":                {"status": "names-only"},   # apocryphal name
    "jezerites-the":          {"status": "names-only"},   # Asherite clan (Num 26:44); minor demonym
    # ISBE compound; redirect to canonical Easton "Jezreel"
    "jezreel-vale-of":        {"status": "redirect-only", "redirect_to": "jezreel"},
    "jezreelite":             {"status": "names-only"},   # demonym; covered under "Jezreel"
    "jezrielus":              {"status": "names-only"},   # apocryphal name
    "jimna-jimnah":           {"status": "names-only"},   # Asherite (Gen 46:17; Num 26:44); minor name
    # ISBE variant of Jehoahaz; redirect to canonical Easton "Jehoahaz"
    "joachaz":                {"status": "redirect-only", "redirect_to": "jehoahaz"},
    "joacim":                 {"status": "names-only"},   # Greek form of Jehoiakim; covered under "Jehoiakim"
    "joadanus":               {"status": "names-only"},   # apocryphal name
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
    print(f'BPG Curation C50: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
