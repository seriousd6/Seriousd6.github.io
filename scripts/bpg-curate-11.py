"""
BPG Curation — Batch C11: proconsul → urim-and-thummim (gaps 1001–1100)
Gaps reviewed: 100 (score-25 smith-scholarly P–U range)

Rich batch with important NT administrative terms, Jewish literature,
deuterocanonical books, and major theological/cultural topics.
Key stubs: Psalms-book-of, Proconsul, Procurator, Punishments, Raphael,
Sin-offering, Sower (parable), Susa, Synagogue-the-Great, Syrophoenician,
Talmud, Targum, Topheth, Tribute-money, Urim-and-Thummim, Uncleanness.
12 redirects: Rahel, Scythopolis, Sibboleth, Symeon, Thamar, Thara, Tharra,
Thebes, Thimnathah, Tilgathpilneser, Twin-brothers, Tyrus.
1 skip: Tormah (textual artifact in Judg 9:31).

Script: scripts/bpg-curate-11.py
Run: python3 scripts/bpg-curate-11.py  (from project root)
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
    # ── P entries ────────────────────────────────────────────────────────────
    # Roman senatorial governor; Sergius Paulus (Acts 13:7), Gallio (Acts 18:12)
    "proconsul":        {"status": "stub-needed"},
    # Roman equestrian governor; Felix (Acts 23:24) and Festus (Acts 24:27) were procurators
    "procurator":       {"status": "stub-needed"},
    "province":         {"status": "names-only"},   # Roman provinces; individual ones have their own articles
    # The Book of Psalms; 150 psalms; five-book structure; Davidic authorship tradition
    "psalms-book-of":   {"status": "stub-needed"},
    # Capital and flogging (Deut 25:2-3); stoning (Lev 24:16); NT crucifixion context
    "punishments":      {"status": "stub-needed"},
    "put":              {"status": "names-only"},   # son of Ham (Gen 10:6); Libya/Punt people
    "pyrrhus":          {"status": "names-only"},   # father of Sopater (Acts 20:4); minor figure

    # ── R entries ────────────────────────────────────────────────────────────
    "rabbith":          {"status": "names-only"},   # Issachar town (Josh 19:20)
    # "Run with endurance the race" (Heb 12:1); athletic metaphor in Paul (1 Cor 9:24-26; Gal 5:7)
    "race":             {"status": "stub-needed"},
    # KJV spelling of Rachel (Gen 31:4 in LXX context); Greek form
    "rahel":            {"status": "redirect-only", "redirect_to": "rachel"},
    "rakem":            {"status": "names-only"},   # Manasseh descendant (1 Chr 7:16)
    # Archangel named in Tobit 12:15; significant in Jewish angelology; identified as healer
    "raphael":          {"status": "stub-needed"},
    "raphon":           {"status": "names-only"},   # city east of Jordan (1 Macc 5:37)
    "rechah":           {"status": "names-only"},   # unidentified Judah town (1 Chr 4:12)
    "rephah":           {"status": "names-only"},   # Ephraim descendant (1 Chr 7:25)
    # Star-god worshipped by Israel in the wilderness (Acts 7:43 quoting Amos 5:26 LXX; "Chiun" in MT)
    "rephan":           {"status": "stub-needed"},
    "resheph":          {"status": "names-only"},   # Ephraim descendant (1 Chr 7:25)
    "rezia":            {"status": "names-only"},   # Asher's son (1 Chr 7:39)
    "roe-roebuck":      {"status": "names-only"},   # clean animal (Deut 12:15); speed metaphor
    "roof":             {"status": "names-only"},   # flat rooftops; Rahab, Peter's vision; general
    "room":             {"status": "names-only"},   # upper room; general reference

    # ── S entries ────────────────────────────────────────────────────────────
    "salt-city-of":     {"status": "names-only"},   # Judah wilderness town (Josh 15:62)
    "salu":             {"status": "names-only"},   # father of Zimri (Num 25:14)
    # The region of Samaria (distinct from Samaria city); Jesus in John 4; Acts 8:1 evangelism
    "samaria-country-of": {"status": "stub-needed"},
    # Island Paul sailed past on second journey (Acts 16:11); Thrace coast
    "samothrace":       {"status": "stub-needed"},
    "sandal":           {"status": "names-only"},   # footwear; "unworthy to unfasten his sandals" idiom
    "saraph":           {"status": "names-only"},   # Judah descendant (1 Chr 4:22)
    "sardine-sardius":  {"status": "names-only"},   # red gemstone in breastplate (Exod 28:17; Rev 4:3)
    "sarothie":         {"status": "names-only"},   # temple servant family (1 Esd 5:34); apocryphal
    "saw":              {"status": "names-only"},   # tool; David's labor sentence (2 Sam 12:31)
    "scorpion":         {"status": "names-only"},   # wilderness danger (Deut 8:15); Rev 9:5; general
    # Hellenistic name for Beth-shean; Decapolis city (1 Macc 5:52; 12:40)
    "scythopolis":      {"status": "redirect-only", "redirect_to": "beth-shan"},
    "sea":              {"status": "names-only"},   # sea in biblical cosmology; too generic
    # Seleucid dynasty kings; Dan 11 prophecies; critical for intertestamental history
    "seleucus":         {"status": "stub-needed"},
    "semein":           {"status": "names-only"},   # NT genealogy (Luke 3:26)
    "senuah":           {"status": "names-only"},   # Benjaminite leaders (Neh 11:9 variant)
    "servant":          {"status": "names-only"},   # too generic; Servant of the Lord covered under "servant-of-the-lord"
    "shaaph":           {"status": "names-only"},   # Caleb's son (1 Chr 2:47,49)
    "shallun":          {"status": "names-only"},   # wall-builder (Neh 3:15)
    "shama":            {"status": "names-only"},   # David's warrior (1 Chr 11:44)
    "shamma":           {"status": "names-only"},   # Asher's son (1 Chr 7:37)
    "sharonite":        {"status": "names-only"},   # epithet for Shitrai (1 Chr 27:29)
    "sharuhen":         {"status": "names-only"},   # Simeon town (Josh 19:6)
    "sheal":            {"status": "names-only"},   # post-exile man with foreign wife (Ezra 10:29)
    "shebah":           {"status": "names-only"},   # Isaac's well (Gen 26:33 = Beersheba etymology)
    "shelomith":        {"status": "names-only"},   # multiple persons: Lev 24:11, Levites, etc.
    "shelomoth":        {"status": "names-only"},   # Levite (1 Chr 23:9; 24:22)
    "shimeam":          {"status": "names-only"},   # Saul's descendant (1 Chr 9:38 variant of Shimeah)
    "shimeath":         {"status": "names-only"},   # Moabite mother of Joash's assassin (2 Kgs 12:21)
    "shuppim":          {"status": "names-only"},   # Benjamin's son (1 Chr 7:12,15)
    # Dialectical variant of Shibboleth tested at the Jordan crossing (Judg 12:6)
    "sibboleth":        {"status": "redirect-only", "redirect_to": "shibboleth"},
    "sibraim":          {"status": "names-only"},   # boundary in Ezekiel's vision (Ezek 47:16)
    "sicyon":           {"status": "names-only"},   # Greek city (1 Macc 15:23)
    "side":             {"status": "names-only"},   # Pamphylian port (1 Macc 15:23); apocryphal
    "sidonians":        {"status": "names-only"},   # people of Sidon; demonym only
    # Prophet/teacher at Antioch (Acts 13:1); surname "Niger" suggests African origin
    "simeon-niger":     {"status": "stub-needed"},
    # חַטָּאת (chattath): sacrifice for unintentional sin (Lev 4-5); typological for Christ
    "sin-offering":     {"status": "stub-needed"},
    # Wisdom of Solomon: deuterocanonical book; personified Wisdom; important for NT Christology
    "solomon-wisdom-of": {"status": "stub-needed"},
    "solomons-servants": {"status": "names-only"},  # returned-exile temple servant family (Ezra 2:55-58)
    "south-ramoth":     {"status": "names-only"},   # Judah town (1 Sam 30:27)
    "sow":              {"status": "names-only"},   # unclean pig (Prov 11:22; 2 Pet 2:22); general
    # Parable of the Sower (Matt 13:1-23; Mark 4:1-20; Luke 8:4-15); most detailed parable interpretation
    "sower-sowing":     {"status": "stub-needed"},
    # Spices in anointing, burial (John 19:40), incense, and trade; key in OT and NT narrative
    "spice-spices":     {"status": "stub-needed"},
    "spinning":         {"status": "names-only"},   # textile craft (Prov 31:19); general cultural
    "standards":        {"status": "names-only"},   # military banners; general reference
    "suchathites":      {"status": "names-only"},   # Kenite family (1 Chr 2:55)
    "sukkiim":          {"status": "names-only"},   # African troops in Shishak's army (2 Chr 12:3)
    # Persian royal capital; Nehemiah served Artaxerxes here; Esther's story; Daniel's vision (Dan 8:2)
    "susa":             {"status": "stub-needed"},
    # "Do not swear at all" (Matt 5:34); OT oath law (Lev 19:12); James 5:12; false oaths
    "swearing":         {"status": "stub-needed"},
    # Greek form of Simeon; Simeon in Acts 15:14 (James's speech); redirect to main article
    "symeon":           {"status": "redirect-only", "redirect_to": "simeon"},
    # Knesset HaGedolah: Jewish council 5th–3rd c. BC; canonized OT and oral law tradition
    "synagogue-the-great": {"status": "stub-needed"},
    # Woman whose daughter Jesus healed (Mark 7:24-30); NT term combining Syrian + Phoenician identity
    "syrophoenician":   {"status": "stub-needed"},

    # ── T entries ────────────────────────────────────────────────────────────
    # Oral Torah compiled into Mishnah + Gemara; essential background for NT and rabbinic Judaism
    "talmud":           {"status": "stub-needed"},
    "taphon":           {"status": "names-only"},   # town in Judah (1 Macc 9:50)
    # Aramaic translations/paraphrases of Hebrew scriptures; important for textual background
    "targum":           {"status": "stub-needed"},
    # Greek form of Tamar used in NT genealogy (Matt 1:3)
    "thamar":           {"status": "redirect-only", "redirect_to": "tamar"},
    # Greek form of Terah (Luke 3:34 KJV)
    "thara":            {"status": "redirect-only", "redirect_to": "terah"},
    # Variant spelling of Thara; same referent
    "tharra":           {"status": "redirect-only", "redirect_to": "terah"},
    # Greek name for No-Amon (Egyptian Thebes); Nahum's comparison (Nah 3:8); Jer 46:25
    "thebes":           {"status": "redirect-only", "redirect_to": "no-amon"},
    # Dan border town (Josh 19:43 variant of Timnah)
    "thimnathah":       {"status": "redirect-only", "redirect_to": "timnah"},
    "tibhath":          {"status": "names-only"},   # city David captured from Hadadezer (1 Chr 18:8)
    # The Tigris River (Heb. Hiddekel); one of four Eden rivers (Gen 2:14); Daniel's vision (Dan 10:4)
    "tigris":           {"status": "stub-needed"},
    # Variant spelling of Tiglath-pileser used in Chronicles (1 Chr 5:6,26; 2 Chr 28:20)
    "tilgathpilneser":  {"status": "redirect-only", "redirect_to": "tiglathpileser"},
    # Gaius Titius Justus: Paul's host in Corinth after synagogue conflict (Acts 18:7)
    "titus-justus":     {"status": "stub-needed"},
    # Book of Tobit: deuterocanonical narrative; Raphael's role; significant for Jewish angelology
    "tobit-book-of":    {"status": "stub-needed"},
    # Rock-cut burial tombs; Jewish burial customs; Jesus's empty tomb narrative
    "tomb":             {"status": "stub-needed"},
    # Valley of Hinnom site where children were sacrificed to Molech (Jer 7:31; 2 Kgs 23:10); Gehenna's origin
    "topheth":          {"status": "stub-needed"},
    # Judg 9:31 KJV: "Tormah" likely a misreading for "privily" or "Arumah"; textual artifact
    "tormah":           {"status": "skip"},
    "tower":            {"status": "names-only"},   # Tower of Siloam, Babel; general reference
    # Ephesian town clerk who quelled riot against Paul (Acts 19:35); Roman civic administrative role
    "town-clerk":       {"status": "stub-needed"},
    "trial":            {"status": "names-only"},   # legal trials; general reference
    # Temple tax pericope (Matt 17:24-27) and Caesar's coin (Matt 22:15-22); key NT fiscal texts
    "tribute-money":    {"status": "stub-needed"},
    "turpentine-tree":  {"status": "names-only"},   # terebinth tree (Isa 6:13 KJV); general botanical
    # Dioscuri (Acts 28:11); same article as "pollux" entry already marked stub-needed
    "twin-brothers":    {"status": "redirect-only", "redirect_to": "pollux"},
    # KJV/Greek form of Tyre (Ezek 26-28; Acts 21:3)
    "tyrus":            {"status": "redirect-only", "redirect_to": "tyre"},

    # ── U entries ────────────────────────────────────────────────────────────
    "uknaz":            {"status": "names-only"},   # Kenaz's son (1 Chr 4:15)
    # Levitical purity laws; ritual uncleanness in Lev 11-15; NT fulfillment in Mark 7:14-23
    "uncleanness":      {"status": "stub-needed"},
    "undergirding":     {"status": "names-only"},   # nautical frapping of hull (Acts 27:17 KJV); technical term
    "urbanus":          {"status": "names-only"},   # greeted in Romans 16:9; generic co-worker mention
    # Sacred lots used by high priest (Exod 28:30; Lev 8:8; Num 27:21); "lights and perfections"
    "urim-and-thummim": {"status": "stub-needed"},
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
    print(f'BPG Curation C11: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
