"""
BPG Curation — Batch C14: shalim → asiarchae
Gaps reviewed: 100 (gaps 1300–1399 by priority score)

Score-15 range (gaps 1300–1311): final isbe-person entries.
Score-10 range (gaps 1312–1399): smith-scholarly entries (many duplicate/combined forms) +
  concept-no-article entries with 20–44 Nave verses.

Notable stub-needed decisions:
  - angel-of-the-lord: major theological concept; Christophany debate; Gen 16:7-13;
    Judg 6:22; Zech 3:1-2; Easton has angel.json but not this distinct concept → stub-needed.

Score-10 concept-no-article entries are mostly too low-count for stubs:
  abstinence-total (21), agency (30), aliens (39), ambassadors (26 → redirect),
  amusements-and-worldly-pleasures (38), ambition (44) — all below meaningful threshold → skip.

46 redirects: many are Smith's combined/variant-form entries ("X-or-Y", "X-=Y")
  pointing to their canonical Easton articles.
10 skips: data artifacts, archaic terms, and concepts below minimum threshold.

Script: scripts/bpg-curate-14.py
Run: python3 scripts/bpg-curate-14.py  (from project root)
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
    # ── Score-15 isbe entries ─────────────────────────────────────────────────
    "shalim":             {"status": "names-only"},   # land Saul passed through (1 Sam 9:4)
    # Waters of Shiloah = Siloam/Silwan spring (Isa 8:6); Easton has siloam-pool-of.json
    "shiloah":            {"status": "redirect-only", "redirect_to": "siloam-pool-of"},
    "shimma":             {"status": "names-only"},   # David's brother (1 Chr 2:13 = Shammah)
    "shitrai":            {"status": "names-only"},   # David's herdsman in Sharon (1 Chr 27:29)
    "sud":                {"status": "names-only"},   # unidentified place (1 Esd 5:23); apocryphal
    "sur":                {"status": "names-only"},   # gate of the temple (2 Kgs 11:6)
    "tarpelites":         {"status": "names-only"},   # people settled in Samaria (Ezra 4:9)
    # Amos's hometown; also wise woman of Tekoa (2 Sam 14:2); Easton has tekoa-tekoah.json
    "tekoa":              {"status": "redirect-only", "redirect_to": "tekoa-tekoah"},
    "urbane":             {"status": "names-only"},   # Roman Christian greeted by Paul (Rom 16:9)
    # Variant of Zerah, son of Judah (Gen 38:30); Easton has zerah.json
    "zarah":              {"status": "redirect-only", "redirect_to": "zerah"},
    # Brook Zered; Israel camped there (Num 21:12; Deut 2:13-14); Easton has zered.json
    "zared":              {"status": "redirect-only", "redirect_to": "zered"},
    # Canaanite city (Gen 10:19; 14:2); Easton has zeboim.json
    "zeboiim":            {"status": "redirect-only", "redirect_to": "zeboim"},

    # ── Score-10 smith-place / smith-scholarly ────────────────────────────────
    # Variant of Ararat; Easton has ararat.json
    "aarat":              {"status": "redirect-only", "redirect_to": "ararat"},
    "ab":                 {"status": "names-only"},   # Hebrew month (July/August); 5th month in sacred calendar
    "abel-stone-of":      {"status": "names-only"},   # large stone near Beth-shemesh (1 Sam 6:18)
    # Smith's combined entry for Abijah variants; Easton has abijah.json
    "abia-abiah-or-abijah": {"status": "redirect-only", "redirect_to": "abijah"},
    "abia-course-of":     {"status": "names-only"},   # priestly division of Abijah (Luke 1:5); Zechariah's division
    "abiaibon":           {"status": "skip"},          # probable data artifact; not a recognized biblical entry
    "abida-or-abidah":    {"status": "names-only"},   # combined form; Abida = son of Midian (Gen 25:4)
    "abiel-or-abiel":     {"status": "names-only"},   # Smith duplicate entry; Abiel = grandfather of Saul (1 Sam 9:1)
    # Smith's combined entry for Abijah/Abijam; Easton has abijah.json
    "abijah-or-abijam":   {"status": "redirect-only", "redirect_to": "abijah"},
    # Variant spelling of Abner; Easton has abner.json
    "abiner":             {"status": "redirect-only", "redirect_to": "abner"},
    # Smith's combined entry for Abishai; Easton has abishai.json
    "abishai-or-abishai": {"status": "redirect-only", "redirect_to": "abishai"},
    # Variant of Abishua; Easton has abishua.json
    "abishua-or-abishua": {"status": "redirect-only", "redirect_to": "abishua"},
    "absaloms-pillar-or-place": {"status": "names-only"},  # Absalom's Monument (2 Sam 18:18)
    # Low Nave count (21); covered under fasting and temperance
    "abstinence-total":   {"status": "skip"},
    # Smith's "Achar = Achan"; 1 Chr 2:7 uses Achar; Easton has achan.json
    "achar-=-achan":      {"status": "redirect-only", "redirect_to": "achan"},
    # Greek form of Ahaz used in Apocrypha; Easton has ahaz.json
    "achaz-=-ahaz":       {"status": "redirect-only", "redirect_to": "ahaz"},
    "achor-valley-of":    {"status": "names-only"},   # Valley of Trouble; Achan stoned (Josh 7:24); Isa 65:10
    "adino-or-adino-the-eznite": {"status": "names-only"},  # David's chief mighty man (2 Sam 23:8)
    "adlai-or-adlai":     {"status": "names-only"},   # Smith duplicate; Adlai = herdsman's father (1 Chr 27:29)
    "adonikam-or-adonikam": {"status": "names-only"}, # post-exile leader (Ezra 2:13; 8:13; Neh 7:18)
    "ador-or-adora":      {"status": "names-only"},   # Maccabean era town (1 Macc 13:20 = Adoraim)
    # Archaic English/Latin form of Egypt; Easton has egypt.json
    "aegypt":             {"status": "redirect-only", "redirect_to": "egypt"},
    "aera":               {"status": "skip"},          # unclear/data artifact; no recognized biblical entry
    # Greek form of Ethiopia; Easton has ethiopia.json
    "aethiopia":          {"status": "redirect-only", "redirect_to": "ethiopia"},
    "age-old":            {"status": "skip"},          # archaic phrase; not a distinct biblical concept
    "agee-or-agee":       {"status": "names-only"},   # father of David's warrior Shammah (2 Sam 23:11)
    # Human agency; generic philosophical term; 30 Nave verses — below threshold
    "agency":             {"status": "skip"},
    # Variant of Ahasuerus (Xerxes I); Easton has ahasuerus.json
    "ahashverosh":        {"status": "redirect-only", "redirect_to": "ahasuerus"},
    # Smith's combined entry for Ahiah/Ahijah; Easton has ahijah.json
    "ahiah-or-ahijah":    {"status": "redirect-only", "redirect_to": "ahijah"},
    "ahlai-or-ahlai":     {"status": "names-only"},   # Smith duplicate; Ahlai = daughter of Sheshan (1 Chr 2:31)
    "aholah-and-aholibah": {"status": "names-only"},  # Ezekiel's allegory for Samaria/Jerusalem (Ezek 23)
    "aholibamah-or-abolibamah": {"status": "names-only"}, # Esau's Hivite wife (Gen 36:2)
    # Valley of Aijalon; Joshua's "Sun, stand still" (Josh 10:12); Easton has ajalon.json
    "aijalon-or-ajalon":  {"status": "redirect-only", "redirect_to": "ajalon"},
    # Alternate transliteration of Aijalon; Easton has ajalon.json
    "aj-alon":            {"status": "redirect-only", "redirect_to": "ajalon"},
    "ajah-=-a-iah":       {"status": "names-only"},   # Aiah; father of Rizpah, Saul's concubine (2 Sam 3:7)
    # Alexander the Great; Smith's entry; Easton has alexander.json and alexander-the-great.json
    "alexander-iii":      {"status": "redirect-only", "redirect_to": "alexander"},
    # Egyptian city; major NT setting (Acts 6:9; 18:24); Easton has alexandria.json
    "alexandria-or-alexandria": {"status": "redirect-only", "redirect_to": "alexandria"},
    # Temple wood (1 Kgs 10:11-12; 2 Chr 9:10-11); Easton has almug.json
    "algum-or-almug-trees": {"status": "redirect-only", "redirect_to": "almug"},
    # Covered under "aliens" (Nave); below meaningful stub threshold (39 verses)
    "aliens":             {"status": "skip"},
    "alliances":          {"status": "names-only"},   # treaties between nations; no standalone theological concept
    # Easton has almond.json
    "almond-tree;-almond": {"status": "redirect-only", "redirect_to": "almond"},
    # Duplicate entry; Easton has almug.json
    "almug-trees":        {"status": "redirect-only", "redirect_to": "almug"},
    # Aromatic plant (Ps 45:8; John 19:39; Num 24:6); Easton has aloes.json
    "aloes-lign-aloes":   {"status": "redirect-only", "redirect_to": "aloes"},
    "alpha":              {"status": "skip"},          # Greek letter; Alpha and Omega discussed under God's titles
    "amadatha":           {"status": "names-only"},   # father of Haman the Agagite (Esth 3:1 = Hammedatha)
    # Smith's entry; Easton has amalekite.json (covers tribe and history)
    "amalekites":         {"status": "redirect-only", "redirect_to": "amalekite"},
    "amalekites-mount-of": {"status": "names-only"},  # Mount of the Amalekites (Judg 12:15)
    "amasai-or-amasai":   {"status": "names-only"},   # Levite who greeted David (1 Chr 12:18)
    "amashai-or-amashai": {"status": "names-only"},   # priest (Neh 11:13)
    # Easton has ambassador.json; ambassadors = 2 Cor 5:20 "ambassadors for Christ"
    "ambassadors":        {"status": "redirect-only", "redirect_to": "ambassador"},
    # Below stub threshold (44 verses); covered under pride and worldliness
    "ambition":           {"status": "skip"},
    "ammonno":            {"status": "names-only"},   # probable variant; unidentified in canonical text
    # Variant of Amminadab; Easton has amminadab.json
    "amninadab":          {"status": "redirect-only", "redirect_to": "amminadab"},
    # Smith's combined entry; Easton has amen.json (the liturgical word; also covers Amon-king)
    "amon-or-amen":       {"status": "redirect-only", "redirect_to": "amen"},
    # Smith's combined entry for Amorite people; Easton has amorites.json
    "amorite-the-amorites": {"status": "redirect-only", "redirect_to": "amorites"},
    # Smith's entry on the Book of Amos; Easton has amos.json (covers man and book)
    "amos-book-of":       {"status": "redirect-only", "redirect_to": "amos"},
    "amulets":            {"status": "names-only"},   # protective charms condemned (Isa 3:20); cultural artifact
    # Below stub threshold (38 verses); covered under worldliness
    "amusements-and-worldly-pleasures": {"status": "skip"},
    # Distinct from general angels: theophanic figure (Gen 16:7; Judg 6:22); pre-incarnate Christ debate
    "angel-of-the-lord":  {"status": "stub-needed"},
    # Smith's entry on angels generally; Easton has angel.json
    "angels":             {"status": "redirect-only", "redirect_to": "angel"},
    "anklet":             {"status": "names-only"},   # ankle ornament condemned by Isaiah (Isa 3:16-23)
    # Paul taken to Antipatris en route to Caesarea (Acts 23:31); Easton has antipatris.json
    "antipatris-or-antipatris": {"status": "redirect-only", "redirect_to": "antipatris"},
    "apes":               {"status": "names-only"},   # imported by Solomon (1 Kgs 10:22; 2 Chr 9:21)
    "apharsathchites-apharsites-apharsacites": {"status": "names-only"}, # peoples in Samaria (Ezra 4:9)
    # Christians met Paul at Forum of Appius (Acts 28:15); Easton has appii-forum.json
    "appius-market-of":   {"status": "redirect-only", "redirect_to": "appii-forum"},
    # Botanical; Song of Songs 2:3; 8:5; Prov 25:11; Easton has apple.json
    "apple-tree-apple":   {"status": "redirect-only", "redirect_to": "apple"},
    # Arabian peoples; Easton has arabia.json
    "arabians":           {"status": "redirect-only", "redirect_to": "arabia"},
    "arbah":              {"status": "names-only"},   # "four" in Kirjath-arba (Josh 14:15; 15:13)
    "arch-of-titus":      {"status": "skip"},          # Roman monument; not a biblical concept
    "archevites":         {"status": "names-only"},   # settlers in Samaria (Ezra 4:9)
    "archite-the":        {"status": "names-only"},   # clan of Hushai, David's friend (2 Sam 15:32)
    # King of Arabia who besieged Paul (2 Cor 11:32); Easton has aretas.json
    "aretas-or-aretas":   {"status": "redirect-only", "redirect_to": "aretas"},
    # Variant of Aram-naharaim; Easton has aram-naharaim.json
    "aramnahataim":       {"status": "redirect-only", "redirect_to": "aram-naharaim"},
    # Moses' basket (Exod 2:3); Easton has ark.json (covers both Noah's ark and Moses' basket)
    "ark-of-moses":       {"status": "redirect-only", "redirect_to": "ark"},
    # Noah's ark; Easton has ark.json
    "ark-noahs":          {"status": "redirect-only", "redirect_to": "ark"},
    "arkite-the":         {"status": "names-only"},   # descendants of Canaan (Gen 10:17)
    # Biblical warfare equipment; Easton has armour.json
    "arms-armor":         {"status": "redirect-only", "redirect_to": "armour"},
    "arpad-or-arphad":    {"status": "names-only"},   # Aramean city (Isa 10:9; Jer 49:23)
    "aruboth":            {"status": "names-only"},   # Solomon's third district (1 Kgs 4:10)
    "arvadite":           {"status": "names-only"},   # people of Arvad/Arwad (Gen 10:18)
    # Sons of Asaph: Levite musicians; Easton has asaph.json
    "asaph-sons-of":      {"status": "redirect-only", "redirect_to": "asaph"},
    # Variant of Ashkenaz; Easton has ashkenaz.json
    "ashchenaz":          {"status": "redirect-only", "redirect_to": "ashkenaz"},
    # Smith's combined entry (Azotus = NT form of Ashdod, Acts 8:40); Easton has ashdod.json
    "ashdod-or-azotus":   {"status": "redirect-only", "redirect_to": "ashdod"},
    # Smith's combined entry; Easton has ashkelon.json
    "ashkelon-askelon":   {"status": "redirect-only", "redirect_to": "ashkelon"},
    "ashurim":            {"status": "names-only"},   # Arab tribe descended from Dedan (Gen 25:3)
    "ashurites-the":      {"status": "names-only"},   # people in Ish-bosheth's territory (2 Sam 2:9)
    "asiarchae":          {"status": "names-only"},   # Asiarchs; officials who befriended Paul (Acts 19:31)
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
    print(f'BPG Curation C14: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
