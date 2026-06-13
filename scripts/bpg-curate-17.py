"""
BPG Curation — Batch C17: friends → intolerance-religious (gaps 1599–1698)
Gaps reviewed: 100 (all score-10 entries, F–I range)

Heavy on Smith tribal/clan demonyms (-ites, -ians, Giblites, Gileadites, etc.) and
"prophecy of X" / "X-or-X" combined variants — most redirect to Easton canonical slugs.
Concept-no-article entries are general virtues/vices (honesty, idleness, injustice) → names-only.

Key stubs: Galatians (epistle), Genealogy of Jesus Christ, High Places (bamot).
Notable skip: high-places6813-priest — garbled composite artifact, not a real entry.
Redirect cluster: Smith "prophecy of" variants (habakkuk-prophecy-of, haggai-prophecy-of),
tribal demonyms (gershonites, gadites, gileadites), and Smith combined forms (X-or-X, X-and-X).

Script: scripts/bpg-curate-17.py
Run: python3 scripts/bpg-curate-17.py  (from project root)
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
    # ── F entries ─────────────────────────────────────────────────────────────
    "friends":             {"status": "names-only"},   # general reference; Jonathan-David etc. covered individually
    "frontlets-or-phylacteries": {"status": "names-only"},  # Smith combined; no Easton phylactery.json
    "frugality":           {"status": "names-only"},   # virtue; 25 Nave verses; general
    # Smith article on burial rites; Easton has funeral.json
    "funerals":            {"status": "redirect-only", "redirect_to": "funeral"},

    # ── G entries ─────────────────────────────────────────────────────────────
    # Smith "tribe of" variant; Easton has gad.json
    "gad-the-tribe-of":    {"status": "redirect-only", "redirect_to": "gad"},
    "gadarenes-girgesenes-gerasenes": {"status": "names-only"},  # Smith combined; no Easton gadarene/gerasa.json
    # Gadites = people of Gad; Easton has gad.json
    "gadites-the":         {"status": "redirect-only", "redirect_to": "gad"},
    # Canonical NT epistle; key text on justification by faith; no Easton article
    "galatians-the-epistle-to-the": {"status": "stub-needed"},
    # Galileans demonym; Easton has galilee.json
    "galileans":           {"status": "redirect-only", "redirect_to": "galilee"},
    "gareb-the-hill":      {"status": "names-only"},   # minor hill near Jerusalem (Jer 31:39)
    "garmite-the":         {"status": "names-only"},   # epithet (1 Chr 4:19); obscure
    # Smith combined variant; Easton has gath-hepher.json (Jonah's hometown, 2 Kgs 14:25)
    "gathhepher-or-gittahhepher": {"status": "redirect-only", "redirect_to": "gath-hepher"},
    # Inhabitants of Gaza; Easton has gaza.json
    "gazathites-the":      {"status": "redirect-only", "redirect_to": "gaza"},
    # Gaza demonym variant; Easton has gaza.json
    "gazites-the":         {"status": "redirect-only", "redirect_to": "gaza"},
    "gederathite-the":     {"status": "names-only"},   # 1 Chr 12:4 epithet; obscure
    "gederite-the":        {"status": "names-only"},   # 1 Chr 27:28 epithet; obscure
    "gems":                {"status": "names-only"},   # precious stones; individual gem articles exist
    # Matt 1:1-17 (through Solomon) and Luke 3:23-38 (through Nathan); two-line genealogy problem
    "genealogy-of-jesus-christ": {"status": "stub-needed"},
    # Sea of Galilee name variant; Easton has gennesaret.json
    "gennesaret-sea-of":   {"status": "redirect-only", "redirect_to": "gennesaret"},
    # Smith variant spelling; Easton has gennesaret.json
    "gennesareth":         {"status": "redirect-only", "redirect_to": "gennesaret"},
    "gerasenes":           {"status": "names-only"},   # Mark 5:1 region; no Easton gerasa.json
    "gerizites":           {"status": "names-only"},   # 1 Sam 27:8 Negev clan; obscure
    # Gershon clan Levites; Easton has gershon.json
    "gershonites-the":     {"status": "redirect-only", "redirect_to": "gershon"},
    "gesham":              {"status": "names-only"},   # Caleb descendant (1 Chr 2:47); minor figure
    # Smith combined variant; Easton has geshur.json (Aramean kingdom; 2 Sam 3:3)
    "geshuri-and-geshurites": {"status": "redirect-only", "redirect_to": "geshur"},
    "gezrites-the":        {"status": "names-only"},   # 1 Sam 27:8 obscure clan
    # Smith place variant; Easton has gibeah.json (Saul's capital, Judg 19-21)
    "gibeath":             {"status": "redirect-only", "redirect_to": "gibeah"},
    # Gibeonites; Easton has gibeon.json (Josh 9; 2 Sam 21)
    "gibeonites-the":      {"status": "redirect-only", "redirect_to": "gibeon"},
    "giblites-the":        {"status": "names-only"},   # people of Gebal (Josh 13:5; 1 Kgs 5:18)
    # Gileadites demonym; Easton has gilead.json
    "gileadites-the":      {"status": "redirect-only", "redirect_to": "gilead"},
    "gilonite-the":        {"status": "names-only"},   # Ahithophel's epithet (2 Sam 15:12)
    "ginnetho":            {"status": "names-only"},   # post-exilic priest (Neh 12:4)
    "ginnethon":           {"status": "names-only"},   # post-exilic priest (Neh 10:6; 12:16 variant)
    # Easton has girgashite.json (Canaanite nation, Gen 10:16)
    "girgashites":         {"status": "redirect-only", "redirect_to": "girgashite"},
    # Smith "the" variant; Easton has girgashite.json
    "girgasite-the":       {"status": "redirect-only", "redirect_to": "girgashite"},
    "gizonites-the":       {"status": "names-only"},   # 1 Chr 11:34 obscure epithet
    "gluttony":            {"status": "names-only"},   # sin; 31 Nave verses; general
    # Smith "scape goat" entry; Easton has scapegoat.json (Lev 16; Azazel)
    "goat-scape":          {"status": "redirect-only", "redirect_to": "scapegoat"},
    "godlessness":         {"status": "names-only"},   # 47 Nave verses; covered under ungodliness articles
    # Grecian = Greek-speaking Jew; Easton has greece.json
    "grecian":             {"status": "redirect-only", "redirect_to": "greece"},
    # Smith combined; Easton has greece.json
    "greece-greeks-grecians": {"status": "redirect-only", "redirect_to": "greece"},
    # Nave "groves" = Asherah poles; Easton has grove.json
    "groves":              {"status": "redirect-only", "redirect_to": "grove"},
    "gunites-the":         {"status": "names-only"},   # Guni's descendants (Num 26:48)

    # ── H entries ─────────────────────────────────────────────────────────────
    "habaiah-or-habajah":  {"status": "names-only"},   # Neh 7:63 priestly family variant
    # Smith combined variant; Easton has habakkuk.json
    "habakkuk-or-habakkuk": {"status": "redirect-only", "redirect_to": "habakkuk"},
    # Smith "prophecy of" variant; Easton has habakkuk.json
    "habakkuk-prophecy-of": {"status": "redirect-only", "redirect_to": "habakkuk"},
    "hachilah-the-hill":   {"status": "names-only"},   # David's hiding place (1 Sam 23:19)
    "haga-bah":            {"status": "names-only"},   # Smith variant of Hagabah (Neh 7:48)
    "hagerite-the":        {"status": "names-only"},   # 1 Chr 27:31 steward epithet
    # Smith "prophecy of" variant; Easton has haggai.json
    "haggai-prophecy-of":  {"status": "redirect-only", "redirect_to": "haggai"},
    "haggites-the":        {"status": "names-only"},   # Haggi's family (Num 26:15)
    "halohesh":            {"status": "names-only"},   # Neh 3:12 wall-builder
    "haltil":              {"status": "names-only"},   # Smith transcription artifact; obscure
    # Hamathite demonym; Easton has hamath.json (city on Orontes)
    "hamathite-the":       {"status": "redirect-only", "redirect_to": "hamath"},
    "hamulites-the":       {"status": "names-only"},   # Hamul's family (Num 26:21)
    "hananiel":            {"status": "names-only"},   # minor biblical figure
    "handkerchief-napkin-apron": {"status": "names-only"},  # Acts 19:12; cloths; general
    "hanging-hangings":    {"status": "names-only"},   # tabernacle curtains (Exod 26); general
    "haphraim":            {"status": "names-only"},   # Issachar town (Josh 19:19)
    "harem":               {"status": "names-only"},   # royal household; general reference
    "harodite-the":        {"status": "names-only"},   # 2 Sam 23:25 epithet
    "harphite":            {"status": "names-only"},   # 1 Chr 12:5 epithet
    "hattuph":             {"status": "names-only"},   # Ezra 2:42 variant; returned exile family
    "hazaradar":           {"status": "names-only"},   # desert boundary (Num 34:4); single reference
    "hazer":               {"status": "names-only"},   # generic "enclosure" place; general
    # Hebronites demonym; Easton has hebron.json
    "hebronites-the":      {"status": "redirect-only", "redirect_to": "hebron"},
    "hege":                {"status": "names-only"},   # eunuch (Esth 2:3); minor figure
    "helhath":             {"status": "names-only"},   # border town (Josh 19:25); variant of Helkath
    "hellenist":           {"status": "names-only"},   # Greek-speaking Jew (Acts 6:1); no Easton article
    "hem-of-garment":      {"status": "names-only"},   # fringes/tassels; general reference
    "hepherites-the":      {"status": "names-only"},   # Hepher's family (Num 26:32)
    "hesed":               {"status": "names-only"},   # son of Ben-hesed (1 Kgs 4:10); minor figure
    # Smith combined variant; Easton has hezron.json
    "hesron-hezron":       {"status": "redirect-only", "redirect_to": "hezron"},
    # Bamot — pagan/syncretistic shrines condemned throughout Kings/Chronicles; 29 Nave verses
    "high-places":         {"status": "stub-needed"},
    # Garbled composite artifact in Smith (high-places + high-priest merged); not a real entry
    "high-places6813-priest": {"status": "skip"},
    "highways":            {"status": "names-only"},   # ancient roads; general reference
    "hills":               {"status": "names-only"},   # general; individual hills have articles
    # Smith combined variant; Easton has hiram.json (Tyre's king; 1 Kgs 5:1)
    "hiram-or-huram":      {"status": "redirect-only", "redirect_to": "hiram"},
    # Smith variant spelling; Easton has hittites.json
    "hittits":             {"status": "redirect-only", "redirect_to": "hittites"},
    # Smith misspelling of Hezekiah; Easton has hezekiah.json
    "hizkljah":            {"status": "redirect-only", "redirect_to": "hezekiah"},
    "hodiah":              {"status": "names-only"},   # Neh 8:7 Levite; minor figure
    "honesty":             {"status": "names-only"},   # virtue; 38 Nave verses; general
    "hook-hooks":          {"status": "names-only"},   # fishing hooks (Ezek 38:4); general
    # Horim = Horites; Easton has horites.json (pre-Edomite cave-dwellers, Gen 14:6)
    "horim":               {"status": "redirect-only", "redirect_to": "horites"},
    "hosham":              {"status": "names-only"},   # obscure; likely Smith transcription issue
    "hospitality":         {"status": "names-only"},   # Christian virtue; general; no distinct Easton article
    "hothan":              {"status": "names-only"},   # 1 Chr 11:44 epithet
    "how-the-prophetic-gift-was-received": {"status": "names-only"},  # Smith article section; not a proper topic
    "huphamites-the":      {"status": "names-only"},   # Hupham's family (Num 26:39)
    "hurai-or-hurai":      {"status": "names-only"},   # Smith combined; 1 Chr 11:32 warrior
    "hurhai":              {"status": "names-only"},   # Smith variant; unclear figure
    # Smith combined variant; Easton has hushai.json (David's friend/spy, 2 Sam 15-17)
    "hushai-or-hushai":    {"status": "redirect-only", "redirect_to": "hushai"},
    "hyaena":              {"status": "names-only"},   # animal (Jer 12:9 LXX); general

    # ── I entries ─────────────────────────────────────────────────────────────
    "iconoclasm":          {"status": "names-only"},   # idol-smashing; 25 Nave verses; general
    "idleness":            {"status": "names-only"},   # sin; 32 Nave verses; general
    "indictments":         {"status": "names-only"},   # legal; 34 Nave verses; general
    "industry":            {"status": "names-only"},   # diligence/work; 40 Nave verses; general
    "injustice":           {"status": "names-only"},   # sin; 37 Nave verses; general
    "ink-inkhorn":         {"status": "names-only"},   # writing instruments (Ezek 9:2); general
    "intolerance-religious": {"status": "names-only"}, # 23 Nave verses; general
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
    print(f'BPG Curation C17: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
