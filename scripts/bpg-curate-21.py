"""
BPG Curation — Batch C21: shemitic-languages → troop-band (gaps 1999–2098)
Gaps reviewed: 100 (score-10 entries, S–T range)

Heavy on Shimite/Shunite tribal demonyms (names-only), Smith combined variants
of Sinai and Timnah, and NT epistle article variants. Redirects thin out here
because fewer Easton articles exist for S–T names.

Key stubs: Siloam (Pool; John 9 miracle), Tabernacles Feast (Sukkot),
Ten Commandments (Decalogue; Exod 20), Thessalonians First Epistle.

Script: scripts/bpg-curate-21.py
Run: python3 scripts/bpg-curate-21.py  (from project root)
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
    # ── S entries ─────────────────────────────────────────────────────────────
    "shemitic-languages":  {"status": "names-only"},   # variant of "Semitic languages"; general reference
    "shephathiah":         {"status": "names-only"},   # multiple figures (1 Chr 3:3; Neh 11:4)
    # Nave concept (31 verses); Easton has shewbread.json (Exod 25:30; Lev 24:5-9)
    "shewbread-showbread": {"status": "redirect-only", "redirect_to": "shewbread"},
    "shihor-of-egypt":     {"status": "names-only"},   # Nile branch (Josh 13:3); general
    "shillemites-the":     {"status": "names-only"},   # Shallum's family (Num 26:49)
    "shiloni":             {"status": "names-only"},   # variant of Shilonite (Neh 11:5)
    "shilonite-the":       {"status": "names-only"},   # epithet for Ahijah the prophet
    "shilonites-the":      {"status": "names-only"},   # plural demonym; covered under shiloh
    "shimi":               {"status": "names-only"},   # variant of Shimei; multiple figures
    "shimites-the":        {"status": "names-only"},   # Shimei's clan (Num 3:21)
    "shimronites-the":     {"status": "names-only"},   # Shimron's family (Num 26:24)
    "shimshai-or-shimshai": {"status": "names-only"},  # scribe (Ezra 4:8); Smith combined
    "ship":                {"status": "names-only"},   # general reference; NT voyages
    "shiphmite-the":       {"status": "names-only"},   # 1 Chr 27:27 epithet; obscure
    "shiramoth":           {"status": "names-only"},   # Levite musician (1 Chr 15:18 variant)
    "shittah-tree-shittim": {"status": "names-only"},  # acacia wood (Exod 25:5); tabernacle
    "shoco":               {"status": "names-only"},   # Judah city variant of Socoh (1 Chr 4:18)
    "shuhamites-the":      {"status": "names-only"},   # Shuham's family (Num 26:42)
    "shulamite-the":       {"status": "names-only"},   # Song 6:13; bride in Song of Songs
    "shumathites-the":     {"status": "names-only"},   # Caleb descendants (1 Chr 2:53)
    # The Shunammite woman who hosted Elisha (2 Kgs 4:8-37); Easton has shunammite.json
    "shunammite-the":      {"status": "redirect-only", "redirect_to": "shunammite"},
    "shunites-the":        {"status": "names-only"},   # Shuni's family (Num 26:15)
    "shupham":             {"status": "names-only"},   # Benjamin's son (Num 26:39 variant)
    "shuphamites-the":     {"status": "names-only"},   # Shupham's family (Num 26:39)
    # Smith combined; Easton has shushan.json (Persian capital; Esther; Neh 1:1)
    "shushan-or-susa":     {"status": "redirect-only", "redirect_to": "shushan"},
    "shuthalhites-the":    {"status": "names-only"},   # Shuthelah's family (Num 26:35)
    "siaha":               {"status": "names-only"},   # temple servant family (Ezra 2:44 variant)
    "sihimma":             {"status": "names-only"},   # Smith entry; unclear figure
    # Pool of Siloam (John 9:7-11; Jesus heals blind man); Tower of Siloam (Luke 13:4); no Easton article
    "siloam":              {"status": "stub-needed"},
    "siloam-tower-in":     {"status": "names-only"},   # Luke 13:4; single reference; covered under siloam stub
    "silverlings":         {"status": "names-only"},   # KJV "silverlings" = pieces of silver (Isa 7:23)
    # Smith "Mount" variant; Easton has sinai.json
    "sina-mount":          {"status": "redirect-only", "redirect_to": "sinai"},
    # Smith combined; Easton has sinai.json (Exod 19-34; giving of the law)
    "sinai-or-sinai":      {"status": "redirect-only", "redirect_to": "sinai"},
    "sincerity":           {"status": "names-only"},   # 29 Nave verses; virtue; general
    "sirach":              {"status": "names-only"},   # Ben Sirach; apocryphal author
    "slothfulness":        {"status": "names-only"},   # 24 Nave verses; sin; general
    "sochoh":              {"status": "names-only"},   # Judah city variant of Socoh
    "soldiers":            {"status": "names-only"},   # 41 Nave verses; general military reference
    "solomons-song":       {"status": "names-only"},   # canonical book; no Easton song-of-songs.json
    "son":                 {"status": "names-only"},   # general relationship reference
    "sparta":              {"status": "names-only"},   # 1 Macc 12:2; apocryphal context
    "spear":               {"status": "names-only"},   # weapon; general reference
    "spearmen":            {"status": "names-only"},   # Acts 23:23; general military
    "star-of-the-wise-men": {"status": "names-only"},  # Matt 2:2; covered under magi stub
    "stocks":              {"status": "names-only"},   # imprisonment device (Acts 16:24); general
    "stoicism":            {"status": "names-only"},   # 22 Nave verses; philosophical school; general
    "stones":              {"status": "names-only"},   # general reference
    "strangers":           {"status": "names-only"},   # 36 Nave verses; sojourner concept; general
    "stumbling":           {"status": "names-only"},   # 21 Nave verses; stumbling block articles exist
    "suretyship":          {"status": "names-only"},   # guarantor (Prov 11:15); general
    "sweat-bloody":        {"status": "names-only"},   # Luke 22:44; Gethsemane; single reference
    "syrtis-the":          {"status": "names-only"},   # Acts 27:17 quicksands; single reference

    # ── T entries ─────────────────────────────────────────────────────────────
    "tabelel":             {"status": "names-only"},   # Isa 7:6; Rezin's ally; minor figure
    # Sukkot/Feast of Booths (Lev 23:34; Neh 8:14-18; Zech 14:16); no Easton tabernacles.json
    "tabernacles-the-feast-of": {"status": "stub-needed"},
    "tabor-the-plain-of":  {"status": "names-only"},   # 1 Sam 10:3; single reference
    "tache":               {"status": "names-only"},   # KJV "clasp" for tabernacle curtains (Exod 26:6)
    "tachmonite-the":      {"status": "names-only"},   # Josheb-basshebeth's epithet (2 Sam 23:8)
    "tact":                {"status": "names-only"},   # 24 Nave verses; virtue; general
    "tahanites-the":       {"status": "names-only"},   # Tahan's family (Num 26:35)
    "tahpanhes-tehaphnehes-tahapanes": {"status": "names-only"},  # Egyptian city (Jer 43:7); no Easton article
    "tappush":             {"status": "names-only"},   # Manasseh city / Caleb descendant (1 Chr 2:43)
    "tarpelites-the":      {"status": "names-only"},   # Ezra 4:9; Assyrian deportee group
    "tax":                 {"status": "names-only"},   # 34 Nave verses; Roman taxation; general
    "tekoa-or-tekoah":     {"status": "names-only"},   # Amos's hometown; no Easton tekoa.json
    "tekoite-the":         {"status": "names-only"},   # epithet (Neh 3:5); from Tekoa
    "telasear":            {"status": "names-only"},   # 2 Kgs 19:12 Assyrian city; single reference
    "telharsa-or-telharesha": {"status": "names-only"}, # Babylonian place (Ezra 2:59); Smith combined
    "temani":              {"status": "names-only"},   # Edomite clan (Gen 36:34 variant)
    "temperance":          {"status": "names-only"},   # 21 Nave verses; covered under self-control
    # The Decalogue (Exod 20:1-17; Deut 5:6-21); foundational OT law; no Easton article
    "ten-commandments":    {"status": "stub-needed"},
    # Smith variant; Easton has new-testament.json (Heb 9:15; canonical NT)
    "testament-new":       {"status": "redirect-only", "redirect_to": "new-testament"},
    "testament-old":       {"status": "names-only"},   # no Easton old-testament.json; covered under stub planned
    "thank-offering-or-peace-offering": {"status": "names-only"},  # no Easton peace-offering.json; general
    # Canonical NT epistle; no Easton thessalonians.json; key eschatology text (1 Thess 4:13-18)
    "thessalonians-first-epistle-to-the": {"status": "stub-needed"},
    "thessalonians-second-epistle-to-the": {"status": "names-only"},  # companion epistle; no separate Easton article
    "thorns":              {"status": "names-only"},   # crown of thorns; general reference
    "three-taverns":       {"status": "names-only"},   # Acts 28:15 waystation; single reference
    "thresholds-the":      {"status": "names-only"},   # temple thresholds; general
    "thuhash":             {"status": "names-only"},   # Nahor's son (Gen 22:24 variant)
    # Smith "Sea of" variant; Easton has tiberias.json (Sea of Galilee; John 6:1)
    "tiberias-the-sea-of": {"status": "redirect-only", "redirect_to": "tiberias"},
    "tikvath":             {"status": "names-only"},   # Huldah's father-in-law (2 Kgs 22:14 variant)
    "timbrel-tabret":      {"status": "names-only"},   # musical instrument (Exod 15:20); general
    # Smith combined; Easton has timnah.json (Samson's wife's city; Judg 14)
    "timna-or-timnah":     {"status": "redirect-only", "redirect_to": "timnah"},
    # Timnath-serah / Timnathah; Easton has timnah.json
    "timnathah":           {"status": "redirect-only", "redirect_to": "timnah"},
    "timnite-the":         {"status": "names-only"},   # Samson's father-in-law epithet (Judg 15:6)
    # Smith epistle variant; Easton has timothy.json (Paul's companion; 1–2 Tim)
    "timothy-epistles-of-paul-to": {"status": "redirect-only", "redirect_to": "timothy"},
    "tirathites-the":      {"status": "names-only"},   # scribal family (1 Chr 2:55)
    "tire":                {"status": "names-only"},   # KJV ornament/headdress (Ezek 24:17)
    "tirhakah-or-tirhakah": {"status": "names-only"},  # Ethiopian pharaoh (2 Kgs 19:9); Smith combined
    "tirhanah":            {"status": "names-only"},   # Caleb's son (1 Chr 2:48)
    "tirras":              {"status": "names-only"},   # Japheth's son variant Tiras (Gen 10:2)
    # Smith "the" variant; Easton has tishbite.json (Elijah's epithet; 1 Kgs 17:1)
    "tishbite-the":        {"status": "redirect-only", "redirect_to": "tishbite"},
    # Smith combined; Easton has tithe.json (Lev 27:30; Mal 3:10; Matt 23:23)
    "tithe-or-tenth":      {"status": "redirect-only", "redirect_to": "tithe"},
    # Nave concept (29 verses); Easton has tithe.json
    "tithes":              {"status": "redirect-only", "redirect_to": "tithe"},
    "tizite-the":          {"status": "names-only"},   # 1 Chr 11:45 epithet; Joha's
    # Easton has tolaites.json (Tola's family; Num 26:23)
    "tolaites-the":        {"status": "redirect-only", "redirect_to": "tolaites"},
    "tou-or-toi":          {"status": "names-only"},   # Hamath's king (2 Sam 8:9); Smith combined
    "treasure-houses":     {"status": "names-only"},   # 38 Nave verses; general
    "treasurecities":      {"status": "names-only"},   # store cities (Exod 1:11; 1 Kgs 9:19)
    "troop-band":          {"status": "names-only"},   # military unit; general reference
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
    print(f'BPG Curation C21: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
