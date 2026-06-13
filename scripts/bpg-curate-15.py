"""
BPG Curation — Batch C15: amath → civil-service (gaps 1399–1498)
Gaps reviewed: 100 (score-10 smith-scholarly A–C range)

Dense batch of significant Smith topics: Baptism, Atonement (Day of), Assyria,
Astarte, Balances, Banquets, Bathsheba, Beelzebul, Benjamin (tribe), Booths,
Brethren of Jesus, Bride/Bridegroom, Burial, Caesarea Philippi, Caiaphas,
Canon of Scripture, Captivities, Cherubim, Chronicles (books), Canaanites.
40 stub-needed entries; 10 redirects; 50 names-only.

Script: scripts/bpg-curate-15.py
Run: python3 scripts/bpg-curate-15.py  (from project root)
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
    # Smith compound form for Hamath (already redirected in C14 attempt)
    "amath":            {"status": "redirect-only", "redirect_to": "hamath"},
    "asphar":           {"status": "names-only"},   # pool near which Jonathan camped (1 Macc 9:33)
    # Balaam's talking donkey (Num 22:21-34); Jesus's triumphal entry on donkey (Zech 9:9; Matt 21:1-9)
    "ass-donkey":       {"status": "stub-needed"},
    "assos-or-assus":   {"status": "names-only"},   # Troas-area port (Acts 20:13-14); transit stop only
    # Major OT empire: Israel's exile (722 BC), Sennacherib, Isaiah's oracles (Isa 7-8; 10), Jonah
    "assyria-asshur":   {"status": "stub-needed"},
    # Canaanite goddess = Ashtoreth; "abomination of the Sidonians" (1 Kgs 11:5); Solomon's apostasy
    "astarte":          {"status": "stub-needed"},
    "asuppim-and-house-of": {"status": "names-only"},  # temple storehouses (1 Chr 26:15,17)
    # Yom Kippur: Lev 16; high priest enters Holy of Holies; scapegoat; typology in Hebrews 9
    "atonement-the-day-of": {"status": "stub-needed"},
    "atroth":           {"status": "names-only"},   # Gad city (Num 32:35 variant of Atroth-Shophan)
    "azareel-or-azareel": {"status": "names-only"}, # multiple OT figures; compound Smith form
    "baaseiah-or-basseiah": {"status": "names-only"},  # Levite ancestor (1 Chr 6:40)
    "bachrites-the":    {"status": "names-only"},   # clan of Becher (Num 26:35)
    "badger-skins":     {"status": "names-only"},   # tabernacle covering (Exod 26:14); translation disputed
    "baharumite-the":   {"status": "names-only"},   # epithet for warrior Azmaveth (2 Sam 23:31)
    "balamo":           {"status": "names-only"},   # obscure Smith entry; minimal significance
    # "Dishonest scales are an abomination" (Prov 11:1; Lev 19:36); Dan 5:27; Rev 6:5 famine seal
    "balances":         {"status": "stub-needed"},
    # Esther's banquets; Parable of Great Banquet (Luke 14:16-24); Marriage Supper of the Lamb (Rev 19:9)
    "banquets":         {"status": "stub-needed"},
    # Christian baptism: John's baptism; Jesus's baptism; Great Commission (Matt 28:19); Rom 6:3-4
    "baptism":          {"status": "stub-needed"},
    "barhumite-the":    {"status": "names-only"},   # epithet variant for warrior Azmaveth (2 Sam 23:31)
    # Joseph Barsabbas (Acts 1:23): apostle candidate; Judas Barsabbas (Acts 15:22): council letter carrier
    "barsabbas":        {"status": "stub-needed"},
    # David and Bathsheba (2 Sam 11-12); Solomon's mother; NT genealogy: "Uriah's wife" (Matt 1:6)
    "bathsheba-or-bathsheba": {"status": "stub-needed"},
    "bazlith":          {"status": "names-only"},   # temple servant family (Neh 7:54)
    "bazluth":          {"status": "names-only"},   # temple servant family (Ezra 2:52)
    "bearbel":          {"status": "names-only"},   # Betharbel (Hos 10:14); place of destruction; brief
    # Prince of demons (Matt 12:24-27; Mark 3:22-27; Luke 11:15-19); "Beelzebub" in KJV; house divided
    "beelzebul":        {"status": "stub-needed"},
    # Smith compound form; content covered under "beersheba" in Easton
    "beersheba-or-beersheba": {"status": "redirect-only", "redirect_to": "beersheba"},
    # Blind Bartimaeus (Mark 10:46); Lazarus the beggar (Luke 16:19-31); "poor you will always have"
    "beggar-begging":   {"status": "stub-needed"},
    "belaites-the":     {"status": "names-only"},   # clan of Bela (Num 26:38)
    "bells":            {"status": "names-only"},   # priestly robe bells (Exod 28:33); Zech 14:20
    "benekedem":        {"status": "names-only"},   # "Sons of the East" (Gen 29:1; Judg 6:3); generic
    "benjamin-high-gate-or-gate-of": {"status": "names-only"},  # Jerusalem gate (Jer 37:13)
    "benjamin-the-land-of": {"status": "names-only"},  # territory of Benjamin; covered under Benjamin (patriarch)
    # Tribe of Benjamin: Paul's tribe (Phil 3:5); King Saul; Jonathan; smallest yet fierce (Judg 20)
    "benjamin-the-tribe-of": {"status": "stub-needed"},
    "benon":            {"status": "names-only"},   # obscure Smith entry; minimal biblical significance
    # Smith variant of Berea; redirect to main article
    "beraa":            {"status": "redirect-only", "redirect_to": "berea"},
    "berachah-valley-of": {"status": "names-only"}, # Valley of Praise (2 Chr 20:26); single narrative
    # Job's losses; David's grief for Absalom (2 Sam 18:33); "Blessed are those who mourn" (Matt 5:4)
    "bereavement":      {"status": "stub-needed"},
    "beriites-the":     {"status": "names-only"},   # clan of Beri (Num 26:44)
    # Agrippa II's sister; present at Paul's defense (Acts 25:13,23; 26:30); Josephus's account
    "bernice-or-berenice": {"status": "stub-needed"},
    "berothite-the":    {"status": "names-only"},   # epithet for David's warrior (1 Chr 11:39)
    "bethbaalmaveth":   {"status": "names-only"},   # post-exile settlement (Neh 7:28 variant)
    "bethhogla":        {"status": "names-only"},   # Benjamin border town (Josh 15:6; 18:19-21)
    "bethmaachah":      {"status": "names-only"},   # Abel-beth-maachah; Sheba's last refuge (2 Sam 20:14)
    # Jewish betrothal: legally binding (Deut 22:23-27); Mary and Joseph; distinguished from marriage
    "betrothing":       {"status": "stub-needed"},
    "bezer-in-the-wilderness": {"status": "names-only"},  # city of refuge in Reuben (Deut 4:43; Josh 20:8)
    "bigthan-or-bigthana": {"status": "names-only"},  # conspirator against Ahasuerus (Esth 2:21)
    "bilgai":           {"status": "names-only"},   # covenant signer (Neh 10:8)
    "bilhan":           {"status": "names-only"},   # Edomite chief / Benjaminite (Gen 36:27; 1 Chr 7:10)
    "birzavith":        {"status": "names-only"},   # Asher descendant (1 Chr 7:31)
    "bishopric":        {"status": "names-only"},   # KJV "office of bishop" (Acts 1:20); covered under "bishop"
    # גֹּאֵל הַדָּם (go'el hadam): blood avenger in OT justice; why cities of refuge were needed
    "blood-revenger-of": {"status": "stub-needed"},
    # Paul's theology of boasting (2 Cor 10-12; Gal 6:14); boasting in the cross vs. carnal pride
    "boasting":         {"status": "stub-needed"},
    "bohan-stone-of":   {"status": "names-only"},   # boundary marker stone (Josh 15:6; 18:17)
    # Feast of Booths/Tabernacles (Sukkot); Lev 23:34-43; Neh 8:14-17; pilgrimage feast
    "booths":           {"status": "stub-needed"},
    "bozes":            {"status": "names-only"},   # rocky cliff near Michmash (1 Sam 14:4 variant)
    # James, Joses, Simon, Judas (Matt 13:55; Mark 6:3; Gal 1:19); perpetual virginity debate
    "brethren-of-jesus": {"status": "stub-needed"},
    # Marriage metaphor: God/Israel (Hos 2:19-20); Christ/Church (Eph 5:25-27; Rev 21:2,9)
    "bride-bridegroom": {"status": "stub-needed"},
    # Rock-cut tombs, loculi, ossuaries; anointing bodies; Joseph's tomb; Jesus's burial (John 19:40-42)
    "burial-sepulchres": {"status": "stub-needed"},
    # Peter's great confession (Matt 16:13-20); "You are the Messiah, the Son of the living God"
    "caesarea-philippi": {"status": "stub-needed"},
    # High priest (AD 18-36) who condemned Jesus (Matt 26:57-68; John 11:49-53; 18:13-27)
    "caiaphas-or-caiaphas": {"status": "stub-needed"},
    # Promised Land: geography (Dan to Beersheba); Canaanite inhabitants; patriarchal wanderings
    "canaan-the-land-of": {"status": "stub-needed"},
    "canaanite-the":    {"status": "names-only"},   # Simon the Cananaean (Matt 10:4); demonym only
    # Seven nations (Deut 7:1): Hittites, Girgashites, Amorites, Canaanites, Perizzites, Hivites, Jebusites
    "canaanites-the":   {"status": "stub-needed"},
    "cananaean":        {"status": "names-only"},   # Aramaic for "zealot"; epithet for Simon the apostle
    # Ethiopian queen (Acts 8:27-39); Philip's encounter; early gospel spread to Africa
    "candace-or-candace": {"status": "stub-needed"},
    # OT and NT canon: Hebrew 24-book canon; NT 27 books; Councils of Hippo/Carthage; apocrypha
    "canon-of-scripture-the": {"status": "stub-needed"},
    "caphar":           {"status": "names-only"},   # Hebrew prefix "village"; lexical entry only
    # NT province (Acts 2:9; 1 Pet 1:1); significant early Christian presence
    "cappadocia-cappadocians": {"status": "stub-needed"},
    # Assyrian exile (722 BC) and Babylonian exile (605-586 BC); return under Cyrus (538 BC)
    "captivities-of-the-jews": {"status": "stub-needed"},
    # "Cast all your anxiety on him" (1 Pet 5:7); "be anxious for nothing" (Phil 4:6); Matt 6:25-34
    "care":             {"status": "stub-needed"},
    "catholicity":      {"status": "names-only"},   # universal church attribute; too doctrinal at score-10
    # Eastern port of Corinth; Phoebe's church (Rom 16:1-2); Paul's vow (Acts 18:18)
    "cenchrea-or-cenchrea": {"status": "stub-needed"},
    "chains":           {"status": "names-only"},   # Paul "in chains" (Eph 6:20); general reference
    # Chaldean empire; Babylon; Abram from Ur of the Chaldeans (Gen 11:31); Daniel's court
    "chaldeans-or-chaldees": {"status": "stub-needed"},
    # Same as above; Smith combined form variant
    "chaldees-or-chaldees": {"status": "redirect-only", "redirect_to": "chaldeans"},
    "chalk-stones":     {"status": "names-only"},   # Isa 27:9; brief metaphorical reference
    # Greek form of Canaan (Acts 7:11; 13:19)
    "chanaan":          {"status": "redirect-only", "redirect_to": "canaan"},
    "charashim-the-valley-of": {"status": "names-only"},  # "Valley of craftsmen" (1 Chr 4:14)
    # Forbearance and generosity toward others; 1 Cor 13; love that "covers a multitude of sins"
    "charitableness":   {"status": "stub-needed"},
    # God's discipline of his children (Heb 12:5-11; Prov 3:11-12); "whom the Lord loves he disciplines"
    "chastisement":     {"status": "stub-needed"},
    # "Flee sexual immorality" (1 Cor 6:18); Joseph and Potiphar's wife; purity in NT (1 Thess 4:3-5)
    "chastity":         {"status": "stub-needed"},
    "cheani":           {"status": "names-only"},   # obscure Smith entry; no clear biblical reference
    "chebel":           {"status": "names-only"},   # Hebrew "cord/region"; lexical entry only
    # King of Elam who conquered Sodom (Gen 14:1-17); Abram's daring rescue; first recorded battle
    "chedorlaomer-or-chedorlaomer": {"status": "stub-needed"},
    "chemarim-the":     {"status": "names-only"},   # idolatrous priests (Zeph 1:4; 2 Kgs 23:5)
    "chepharhaammonai": {"status": "names-only"},   # Benjamin border town (Josh 18:24)
    # Smith combines place "Cherub" (Ezra 2:59) with heavenly beings; redirect to theological article
    "cherub-cherubim":  {"status": "redirect-only", "redirect_to": "cherubim"},
    # Heavenly beings: guard Eden (Gen 3:24), over Ark (Exod 25:18-22), Ezekiel's chariot (Ezek 1; 10)
    "cherubim":         {"status": "stub-needed"},
    "chiding":          {"status": "names-only"},   # reproof; too generic at score-10
    # Children in Jesus's ministry (Mark 10:13-16); "train up a child" (Prov 22:6); children's faith
    "children":         {"status": "stub-needed"},
    "chillon":          {"status": "names-only"},   # Ruth's husband who died in Moab (Ruth 1:2-5)
    "chimhan":          {"status": "names-only"},   # Barzillai's son who stayed with David (2 Sam 19:37-40)
    # Smith form for Sea of Chinnereth = Sea of Galilee
    "chinnereth-sea-of": {"status": "redirect-only", "redirect_to": "chinnereth"},
    # Variant of Chinnereth (1 Kgs 15:20; Josh 19:35)
    "chinneroth":       {"status": "redirect-only", "redirect_to": "chinnereth"},
    "chittim-kittim":   {"status": "names-only"},   # island peoples (Gen 10:4); Dan 11:30 "ships of Kittim"
    # 1–2 Chronicles: temple-focused history; Davidic covenant; worship; Chronicler's perspective
    "chronicles-first-and-second-books-of": {"status": "stub-needed"},
    # Variant spelling of chrysoprase gemstone (Rev 21:20)
    "chryoprase":       {"status": "redirect-only", "redirect_to": "chrysoprase"},
    # Another variant of chrysoprase (Rev 21:20)
    "chrysprasus":      {"status": "redirect-only", "redirect_to": "chrysoprase"},
    "cities":           {"status": "names-only"},   # cities in biblical history; too generic
    # Joseph in Egypt, Daniel in Babylon, Nehemiah in Persia; God's people in government service
    "civil-service":    {"status": "stub-needed"},
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
    print(f'BPG Curation C15: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
