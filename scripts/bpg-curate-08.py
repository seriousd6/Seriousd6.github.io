"""
BPG Curation — Batch C08: bethezel → genealogy (gaps 701–800)
Gaps reviewed: 100 (all score-25 smith-scholarly entries, B–G range)

Smith-scholarly entries are richer than pure names: many are cultural,
institutional, or theological topics that warrant Biblepedia articles.
Key stubs include: Brazen Serpent, Cities of Refuge, Pillar of Cloud,
Cornerstone, Eli-eli-lama-sabachthani, Exodus, Cities of Refuge,
Caphtorim (Philistine origin), and 11 Greek-form redirects.

Script: scripts/bpg-curate-08.py
Run: python3 scripts/bpg-curate-08.py  (from project root)
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
    # ── B names (smith-scholarly) ────────────────────────────────────────────
    "bethezel":       {"status": "names-only"},   # village in Micah 1:11; single mention
    "bethlomon":      {"status": "names-only"},   # Greek form of Bethlehem in apocrypha
    "bethrehob":      {"status": "names-only"},   # Aramean state (2 Sam 10:6)
    "bethshittah":    {"status": "names-only"},   # place in Gideon's pursuit (Judg 7:22)
    "bethul":         {"status": "names-only"},   # Simeon town (Josh 19:4)
    "bimhal":         {"status": "names-only"},   # Asher's son (1 Chr 7:33)
    # Smith article on birds of the Bible; zoological/cultural significance
    "birds":          {"status": "stub-needed"},
    # Passover element (Exod 12:8; Num 9:11); typological of suffering in Egypt
    "bitter-herbs":   {"status": "stub-needed"},
    "biztha":         {"status": "names-only"},   # Persian eunuch (Esth 1:10)
    # Both literal (miracles) and spiritual (John 9); rich biblical metaphor
    "blindness":      {"status": "stub-needed"},
    # Greek form of Boaz used in NT genealogies (Matt 1:5; Luke 3:32)
    "booz":           {"status": "redirect-only", "redirect_to": "boaz"},
    "boscath":        {"status": "names-only"},   # Josiah's mother's hometown (2 Kgs 22:1)
    "bozkath":        {"status": "names-only"},   # same as Boscath; variant spelling
    # Bronze serpent on a pole (Num 21:8-9); typology for Christ's crucifixion (John 3:14)
    "brazen-serpent": {"status": "stub-needed"},
    "brick":          {"status": "names-only"},   # construction material; Egyptian bondage context
    "bull-bullock":   {"status": "names-only"},   # sacrificial animal; general reference entry
    "bushel":         {"status": "names-only"},   # KJV unit of measure (Matt 5:15)
    "caldron":        {"status": "names-only"},   # cooking/prophetic vessel (Jer 1:13)
    "canopy":         {"status": "names-only"},   # chuppah/wedding canopy; general reference
    # Alternative name for Song of Solomon
    "canticles":      {"status": "redirect-only", "redirect_to": "song-of-solomon"},
    # Origin of Philistines (Gen 10:14; Deut 2:23; Amos 9:7); significant ethnic history
    "caphtor-caphtorim": {"status": "stub-needed"},
    "caria":          {"status": "names-only"},   # Asia Minor region (1 Macc 15:23; apocryphal)
    "carving":        {"status": "names-only"},   # craft in ancient Israel; archaeological topic
    # Small island near Crete where Paul's ship found shelter (Acts 27:16)
    "cauda":          {"status": "stub-needed"},
    "celosyria":      {"status": "names-only"},   # Coele-Syria; historical region, not key theme
    "chapman":        {"status": "names-only"},   # KJV term for merchant (2 Chr 9:14)
    "chase":          {"status": "names-only"},   # KJV term for hunting; general reference
    # David's elite bodyguard unit alongside Pelethites; likely Cretan mercenaries (2 Sam 8:18)
    "cherethites":    {"status": "stub-needed"},
    # Wadi where Elijah hid and ravens fed him daily (1 Kgs 17:3-7)
    "cherith-the-brook": {"status": "stub-needed"},
    "chrysolite":     {"status": "names-only"},   # gemstone in temple/heavenly imagery
    "ciccar":         {"status": "names-only"},   # Hebrew for "circle/plain" of Jordan; lexical
    # Variant for Sea of Chinnereth (Galilee) (Num 34:11; Josh 12:3)
    "cinneroth":      {"status": "redirect-only", "redirect_to": "cinnereth"},
    # Six designated cities of asylum for unintentional killers (Num 35; Deut 19; Josh 20)
    "cities-of-refuge": {"status": "stub-needed"},
    "citims":         {"status": "names-only"},   # Kittim variant; island peoples (Gen 10:4)
    "citron":         {"status": "names-only"},   # tree from Lev 23:40 LXX; botanical reference
    # Roman tribune who rescued Paul from Jerusalem mob and sent him to Caesarea (Acts 21:31-23:26)
    "claudius-lysias": {"status": "stub-needed"},
    # Theophanic column guiding Israel by day (Exod 13:21-22; 14:19; Num 9:15-23)
    "cloud-pillar-of": {"status": "stub-needed"},
    "coast":          {"status": "names-only"},   # KJV for "region/border" — translation note
    "cock":           {"status": "names-only"},   # rooster; Peter's denial context (Matt 26:74)
    "commerce":       {"status": "names-only"},   # trade in ancient Israel; cultural reference
    "cononiah":       {"status": "names-only"},   # Levite in Hezekiah's reforms (2 Chr 31:12)
    "cooking":        {"status": "names-only"},   # food preparation; cultural reference
    # Greek form of Korah (Jude 11); rebel Levite
    "core":           {"status": "redirect-only", "redirect_to": "korah"},
    # Christ as cornerstone (Ps 118:22; Isa 28:16; Eph 2:20; 1 Pet 2:6-7)
    "cornerstone":    {"status": "stub-needed"},
    "cotton":         {"status": "names-only"},   # textile; Hebrew byssus/linen translation issue
    "creditor":       {"status": "names-only"},   # debt laws; general reference
    "crisping-pins":  {"status": "names-only"},   # KJV "handbags/satchels" (Isa 3:22)
    "cushi":          {"status": "names-only"},   # two figures: Ethiopian messenger (2 Sam 18:21)
    # Forbidden pagan mourning rite (Lev 19:28; Deut 14:1); marks Israel's boundary with paganism
    "cuttings-[in-the-flesh]": {"status": "stub-needed"},

    # ── D names (smith-scholarly) ────────────────────────────────────────────
    "dara":           {"status": "names-only"},   # son of Zerah (1 Chr 2:6)
    "dates":          {"status": "names-only"},   # date palms in the Bible; botanical
    "deer":           {"status": "names-only"},   # clean animal; general reference
    # Psalms of Ascent (Ps 120-134); pilgrimage psalms used for Temple festivals
    "degrees-songs-of": {"status": "stub-needed"},
    # Roman silver coin; daily wage (Matt 20:2); appears in tribute question (Matt 22:19)
    "denarius":       {"status": "stub-needed"},
    "dinaites":       {"status": "names-only"},   # foreign colonists in Samaria (Ezra 4:9)
    "dositheus":      {"status": "names-only"},   # name in 2 Maccabees; apocryphal
    # Variant of Dothan (2 Kgs 6:13)
    "dothaim":        {"status": "redirect-only", "redirect_to": "dothan"},

    # ── E names (smith-scholarly) ────────────────────────────────────────────
    # Mount Ebal: site of covenant curses ceremony (Deut 27:13; Josh 8:30-35)
    "ebal-mount":     {"status": "stub-needed"},
    # Wisdom of Ben Sira; important deuterocanonical text for biblical scholarship
    "ecclesiasticus": {"status": "stub-needed"},
    # Education in ancient Israel: Torah instruction, scribal schools, rabbi-disciple model
    "education":      {"status": "stub-needed"},
    "ehi":            {"status": "names-only"},   # son of Benjamin (Gen 46:21)
    # Port city on Red Sea used by Solomon's fleet and Uzziah (1 Kgs 9:26; 2 Chr 26:2)
    "elath-eloth":    {"status": "stub-needed"},
    "eleasah":        {"status": "names-only"},   # two minor OT figures (1 Chr 2:39; 8:37)
    "eleloheisrael":  {"status": "names-only"},   # Jacob's altar name (Gen 33:20)
    # Jesus's cry of dereliction (Matt 27:46; Mark 15:34); quotes Ps 22:1; key Passion text
    "eli-eli-lama-sabachthani": {"status": "stub-needed"},
    "elihoenai":      {"status": "names-only"},   # returned-exile leader (Ezra 8:4)
    # Greek form of Elisha (Luke 4:27)
    "eliseus":        {"status": "redirect-only", "redirect_to": "elisha"},
    "elizaphan":      {"status": "names-only"},   # Levite leader (Num 3:30; 2 Chr 29:13)
    "elmadam":        {"status": "names-only"},   # NT genealogy (Luke 3:28)
    # Another form of Elath (2 Chr 8:17)
    "eloth":          {"status": "redirect-only", "redirect_to": "elath"},
    "emerods":        {"status": "names-only"},   # KJV "tumors" (1 Sam 5:6); medical/translation
    "en":             {"status": "names-only"},   # Hebrew prefix meaning "spring"; lexical note
    "encampment":     {"status": "names-only"},   # Israelite camp arrangement (Num 2)
    "engine":         {"status": "names-only"},   # KJV siege weapon (2 Chr 26:15)
    "ephai":          {"status": "names-only"},   # Netophathite captain (Jer 40:8)
    "ephraimite":     {"status": "names-only"},   # demonym for tribe of Ephraim
    "ephrain":        {"status": "names-only"},   # town taken by Abijah (2 Chr 13:19)
    "eshton":         {"status": "names-only"},   # Judah descendant (1 Chr 4:11)
    "esril":          {"status": "names-only"},   # 2 Esdras figure; apocryphal
    # NT woman at Philippi who quarreled with Syntyche (Phil 4:2); significant for women in church
    "euodia":         {"status": "stub-needed"},
    # Jewish and early Christian practice of exclusion (John 9:22; 12:42; 1 Cor 5:2)
    "excommunication": {"status": "stub-needed"},
    # The defining event of the OT: Israel's deliverance from Egypt
    "exodus-the":     {"status": "stub-needed"},
    "ezbai":          {"status": "names-only"},   # father of David's warrior Naarai (1 Chr 11:37)

    # ── F–G names (smith-scholarly) ──────────────────────────────────────────
    "floor":          {"status": "names-only"},   # threshing floor; general reference
    "fly-flies":      {"status": "names-only"},   # plague insect; Beelzebub etymology
    "footman":        {"status": "names-only"},   # foot soldier; KJV military term
    "fowl":           {"status": "names-only"},   # birds/poultry; general reference
    "fullers-field-the": {"status": "names-only"}, # Isaiah 7:3 landmark; single location
    # Variant of Geba (Josh 18:24)
    "gaba":           {"status": "redirect-only", "redirect_to": "geba"},
    # Gabbatha/Stone Pavement (John 19:13): the place where Pilate judged Jesus
    "gabatha":        {"status": "stub-needed"},
    "gadi":           {"status": "names-only"},   # father of King Menahem (2 Kgs 15:14)
    "gaham":          {"status": "names-only"},   # Nahor's son (Gen 22:24)
    # Greek form of Gilead
    "galaad":         {"status": "redirect-only", "redirect_to": "gilead"},
    "galley":         {"status": "names-only"},   # large ship (Isa 33:21)
    "garden":         {"status": "names-only"},   # gardens in the Bible; general reference
    "garment":        {"status": "names-only"},   # clothing in biblical times; general
    # Variant of Geshem the Arabian who opposed Nehemiah (Neh 6:6)
    "gashmu":         {"status": "redirect-only", "redirect_to": "geshem"},
    # Greek form of Gideon (Heb 11:32)
    "gedeon":         {"status": "redirect-only", "redirect_to": "gideon"},
    "gederoth":       {"status": "names-only"},   # Judah town captured by Philistines (2 Chr 28:18)
    # Biblical genealogies: purpose, types (Matt 1; Luke 3); use in Jewish and NT context
    "genealogy":      {"status": "stub-needed"},
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
    print(f'BPG Curation C08: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
