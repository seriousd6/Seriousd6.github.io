"""
BPG Curation — Batch C16: clothing → fraternity (gaps 1499–1598)
Gaps reviewed: 100 (all score-10 entries, C–F range)

Score-10 batch: heavy on Smith's combined/variant forms (X-or-Y, X-=-Y, X-the-Y).
Strategy: redirects to Easton where slug confirmed; names-only for minor persons/places/
general references; stub-needed only for core theological concepts regardless of score.

Key stubs: Colossians (epistle), Condescension of God, Ephesians (epistle),
False Teachers.
Redirect cluster: Smith variant forms of canonical slugs (dreams→dream,
enosh→enos, epah→ephah, edom-idumaea→edom, eshcol-the-valley→eshcol, etc.)

Script: scripts/bpg-curate-16.py
Run: python3 scripts/bpg-curate-16.py  (from project root)
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
    # ── C entries ─────────────────────────────────────────────────────────────
    "clothing":            {"status": "names-only"},   # general garment reference; no Easton article
    "clouted":             {"status": "names-only"},   # KJV "clouted sandals" (Josh 9:5); translation artifact
    "college-the":         {"status": "names-only"},   # Huldah's quarter / "second district" (2 Kgs 22:14)
    "colors":              {"status": "names-only"},   # general cultural reference
    # Canonical NT epistle; no Easton article; central text for Christology (Col 1:15-20)
    "colossians-the-epistle-to-the": {"status": "stub-needed"},
    # God's humbling condescension; Ps 113:6; Isa 57:15; foundational for Incarnation theology
    "condescension-of-god": {"status": "stub-needed"},
    "continence":          {"status": "names-only"},   # sexual restraint (1 Cor 7:9); general virtue
    "contingencies":       {"status": "names-only"},   # not a specific biblical term
    "contracts":           {"status": "names-only"},   # legal agreements; general cultural reference
    "converts":            {"status": "names-only"},   # general reference to those turning to God
    "cos-or-coos":         {"status": "names-only"},   # island Paul visited (Acts 21:1); no Easton article
    "create":              {"status": "names-only"},   # Smith article; concept covered under creation
    # Demonym for people of Crete (Titus 1:12)
    "cretes":              {"status": "redirect-only", "redirect_to": "crete"},
    "curiosity":           {"status": "names-only"},   # general trait; not a specific biblical theme
    "cuth-or-cuthah":      {"status": "names-only"},   # Assyrian deportees (2 Kgs 17:24); no Easton article
    "cymbal-cymbals":      {"status": "names-only"},   # musical instruments; general reference

    # ── D entries ─────────────────────────────────────────────────────────────
    "daniel-apocryphal-additions-to": {"status": "names-only"},  # Bel, Susanna, Dragon; apocryphal additions
    # Smith "book of" variant; Easton covers Daniel under daniel.json
    "daniel-the-book-of":  {"status": "redirect-only", "redirect_to": "daniel"},
    # Dan tribe demonym; Easton has dan.json
    "danites-the":         {"status": "redirect-only", "redirect_to": "dan"},
    "dead-people":         {"status": "names-only"},   # general reference
    "deception":           {"status": "names-only"},   # sin; 28 Nave verses; general
    "dedication":          {"status": "names-only"},   # general concept; 22 verses
    "defilement":          {"status": "names-only"},   # purity laws; covered under purification articles
    # Smith combined/variant form; Easton has delilah.json
    "delilah-or-delilah":  {"status": "redirect-only", "redirect_to": "delilah"},
    "demoniacs":           {"status": "names-only"},   # demon-possessed persons; covered under demon/devil
    "despondency":         {"status": "names-only"},   # emotional state; 45 Nave verses; general
    "deuel-or-deuel":      {"status": "names-only"},   # Num 1:14; minor figure; Smith combined form
    # Dibon-gad desert camp (Num 33:45); Easton has dibon.json covering same locale
    "dibongan":            {"status": "redirect-only", "redirect_to": "dibon"},
    "didrachmon":          {"status": "names-only"},   # Greek double drachma; temple tax (Matt 17:24); translation artifact
    "diligence":           {"status": "names-only"},   # 48 Nave verses; virtue; score-10 threshold not met
    "diplomacy":           {"status": "names-only"},   # political skill; 33 Nave verses; general
    "disease":             {"status": "names-only"},   # general medical reference; 45 Nave verses
    "diseases":            {"status": "names-only"},   # Smith scholarly article; general medical reference
    # Jewish Diaspora; Easton has dispersion.json
    "dispersion-the-jews-of-the": {"status": "redirect-only", "redirect_to": "dispersion"},
    "doctrines":           {"status": "names-only"},   # plural form; 46 Nave verses; no distinct Easton article
    "dog-sodomite?":       {"status": "names-only"},   # Deut 23:18 KJV "dog" = male cult prostitute; translation note
    "drachm":              {"status": "names-only"},   # monetary unit; translation artifact
    # Easton has dream.json covering dreams in Scripture
    "dreams":              {"status": "redirect-only", "redirect_to": "dream"},

    # ── E entries ─────────────────────────────────────────────────────────────
    "earthenware":         {"status": "names-only"},   # pottery; general cultural reference
    "earthquakes":         {"status": "names-only"},   # natural disasters; 38 Nave verses; general
    "eclipse-of-the-sun":  {"status": "names-only"},   # astronomical; prophetic context; general
    "edar-tower-of":       {"status": "names-only"},   # tower (Gen 35:21; Mic 4:8); single reference
    # Smith combined variant; Easton has edom.json
    "edom-idumaea-or-idumea": {"status": "redirect-only", "redirect_to": "edom"},
    # Demonym; no separate Easton edomites article; covered under edom.json
    "edomites":            {"status": "redirect-only", "redirect_to": "edom"},
    "egyptian-egyptians":  {"status": "names-only"},   # demonym; general reference
    "elada":               {"status": "names-only"},   # 1 Chr 7:26; minor Ephraim descendant
    # Battle site where Goliath fell; Easton has elah.json
    "elah-the-valley-of":  {"status": "redirect-only", "redirect_to": "elah"},
    # Demonym for people of Elam; Easton has elam.json
    "elamites":            {"status": "redirect-only", "redirect_to": "elam"},
    # Smith combined/variant form; Easton has eleazar.json
    "eleazar-eleazer":     {"status": "redirect-only", "redirect_to": "eleazar"},
    "eliadah":             {"status": "names-only"},   # 1 Kgs 11:23; minor official of Solomon
    # Smith variant spelling; Easton has eliezer.json
    "eliezar":             {"status": "redirect-only", "redirect_to": "eliezer"},
    # Smith combined variant; Easton has elkanah.json
    "elkanah-or-elkonah":  {"status": "redirect-only", "redirect_to": "elkanah"},
    # Smith combined variant; Easton has elnathan.json
    "elnathan-or-elnathan": {"status": "redirect-only", "redirect_to": "elnathan"},
    "elonites-the":        {"status": "names-only"},   # Elon's family (Num 26:26)
    "elteknon":            {"status": "names-only"},   # Judah town variant; minor place
    "embroiderer":         {"status": "names-only"},   # craftsperson; general reference
    # Smith combined variant; Easton has emmaus.json (Emmaus resurrection road, Luke 24:13)
    "emmaus-or-emmaus":    {"status": "redirect-only", "redirect_to": "emmaus"},
    "employee":            {"status": "names-only"},   # general labor concept; 24 Nave verses
    "employer":            {"status": "names-only"},   # general labor concept; 20 Nave verses
    # Smith combined variant; Easton has engedi.json (David's refuge, 1 Sam 24:1)
    "engedi-or-engedi":    {"status": "redirect-only", "redirect_to": "engedi"},
    # Pseudepigraphical text; Easton has enoch.json covering the patriarch
    "enoch-the-book-of":   {"status": "redirect-only", "redirect_to": "enoch"},
    # Enosh = Enos in LXX/KJV; Easton has enos.json
    "enosh":               {"status": "redirect-only", "redirect_to": "enos"},
    # Smith variant of Ephah; Easton has ephah.json
    "epah":                {"status": "redirect-only", "redirect_to": "ephah"},
    # Canonical NT epistle; no Easton article; central text on the church and armor of God
    "ephesians-the-epistle-to-the": {"status": "stub-needed"},
    # Battle site of Absalom's defeat (2 Sam 18:6); Easton has ephraim.json
    "ephraim-the-wood-of": {"status": "redirect-only", "redirect_to": "ephraim"},
    "ephratah-or-ephrath": {"status": "names-only"},   # Bethlehem area; no Easton ephrath.json
    "ephron-mount":        {"status": "names-only"},   # boundary of Judah (Josh 15:9); single reference
    # Philosophical sect (Acts 17:18); Easton has epicureans.json
    "epicureans-the":      {"status": "redirect-only", "redirect_to": "epicureans"},
    "eranites-the":        {"status": "names-only"},   # Eran's family (Num 26:36)
    # Esdras = Ezra in Septuagint; Easton has ezra.json
    "esdras":              {"status": "redirect-only", "redirect_to": "ezra"},
    "esdras-the-second-book-of": {"status": "names-only"},  # 2 Esdras apocryphal text; distinct from Ezra
    # Valley where spies cut the cluster of grapes (Num 13:23); Easton has eshcol.json
    "eshcol-the-valley":   {"status": "redirect-only", "redirect_to": "eshcol"},
    # People of Ashkelon; Easton has ashkelon.json
    "eshkalonites-the":    {"status": "redirect-only", "redirect_to": "ashkelon"},
    "eshtaulites-the":     {"status": "names-only"},   # Eshtaol's inhabitants; minor clan
    "etam-the-rock":       {"status": "names-only"},   # Samson's hiding place (Judg 15:8); single event
    "ethiopian":           {"status": "names-only"},   # demonym; general reference
    # Acts 8:26-40; Philip and the court official; Easton has ethiopian-eunuch.json
    "ethiopian-eunuch-the": {"status": "redirect-only", "redirect_to": "ethiopian-eunuch"},
    "eurcquila":           {"status": "names-only"},   # variant of Euroclydon (Acts 27:14); translation artifact
    "evil-for-good":       {"status": "names-only"},   # rendering evil for good; 22 Nave verses; general
    "eziongaber-or-eziongeber": {"status": "names-only"},  # Red Sea port; no Easton eziongeber.json
    "eznite-the":          {"status": "names-only"},   # epithet for Adino (2 Sam 23:8)
    "ezrahite-the":        {"status": "names-only"},   # epithet for Heman/Ethan (Ps 88:1; 89:1)

    # ── F entries ─────────────────────────────────────────────────────────────
    "faithfulness":        {"status": "names-only"},   # 23 Nave verses; covered broadly under faith
    "fallow-deer":         {"status": "names-only"},   # animal; general reference
    "false-confidence":    {"status": "names-only"},   # presumption/false security; 36 Nave verses; general
    # False prophets and teachers; 2 Pet 2:1; 1 Tim 6:3; Gal 1:6-9; 42 Nave verses
    "false-teachers":      {"status": "stub-needed"},
    "fasts":               {"status": "names-only"},   # Smith article; no Easton fasting.json; general
    "feasts":              {"status": "names-only"},   # Smith article; individual feast articles cover specifics
    "festivals":           {"status": "names-only"},   # general; individual festival articles exist
    "fetters":             {"status": "names-only"},   # chains/bonds; general reference
    # Smith combined form; Easton has fig.json
    "fig-fig-tree":        {"status": "redirect-only", "redirect_to": "fig"},
    "first-fruits":        {"status": "names-only"},   # 26 Nave verses; no Easton firstfruits.json
    "flattery":            {"status": "names-only"},   # sin; 46 Nave verses; general
    "flux-bloody":         {"status": "names-only"},   # KJV dysentery (Acts 28:8); translation artifact
    "fool":                {"status": "names-only"},   # wisdom literature concept; 42 Nave verses; general
    "forgetting-god":      {"status": "names-only"},   # sin; 36 Nave verses; general
    "formalism":           {"status": "names-only"},   # empty religion; 29 Nave verses; general
    "fort":                {"status": "names-only"},   # military structure; 26 Nave verses; general
    "fortifications":      {"status": "names-only"},   # Smith article; general military reference
    "fraternity":          {"status": "names-only"},   # brotherly love; 37 Nave verses; general
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
    print(f'BPG Curation C16: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
