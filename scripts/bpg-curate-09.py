"""
BPG Curation — Batch C09: gerzites → lacedaemonians
Gaps reviewed: 100 (gaps 801–900 by priority score)

All priority-25 smith-scholarly entries (0 Nave verses).

Notable stub-needed decisions:
  - gleaning: Levitical poor-law practice (Lev 19; Ruth 2) → stub-needed.
  - heliopolis: ancient Egyptian city = On/Aven (Ezek 30:17) → stub-needed.
  - hippopotamus: Behemoth in Job 40 → stub-needed.
  - holofernes: Apocrypha general in Book of Judith → stub-needed.
  - hymenaeus: false teacher named by Paul (1 Tim 1:20; 2 Tim 2:17) → stub-needed.
  - image: imago Dei + idol-image theology → stub-needed.
  - inheritance: Levitical land laws + spiritual inheritance → stub-needed.
  - jesurun: poetic name for Israel (Deut 32:15; Isa 44:2) → stub-needed.
  - jesus-christ: Smith's entry on the person of Jesus → stub-needed.
  - john-the-apostle: no Easton standalone article → stub-needed.
  - judas-maccabaeus: Maccabean revolt leader → stub-needed.
  - judas-of-galilee: revolutionary (Acts 5:37) → stub-needed.
  - judas-the-lords-brother: brother of Jesus, author of Jude → stub-needed.
  - jewel: precious gems in biblical culture → stub-needed.
  Ten redirects: Greek/variant spellings to canonical Easton articles.

Script: scripts/bpg-curate-09.py
Run: python3 scripts/bpg-curate-09.py  (from project root)
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
    # ── G names / concepts ────────────────────────────────────────────────────
    "gerzites":          {"status": "names-only"},   # tribe near Ziklag associated with Geshurites (1 Sam 27:8)
    "gibea":             {"status": "names-only"},   # son of Sheva, Judah genealogy (1 Chr 2:49)
    "giddalti":          {"status": "names-only"},   # Levite musician (1 Chr 25:4,29)
    "gidom":             {"status": "names-only"},   # place near Gibeah (Judg 20:45)
    "giereagle":         {"status": "skip"},          # KJV bird-species gloss; not a biblical concept
    # Levitical practice of leaving crops for the poor (Lev 19:9-10; Ruth 2); key social-law concept
    "gleaning":          {"status": "stub-needed"},
    "grinding":          {"status": "names-only"},   # grain-milling activity (Matt 24:41); no doctrinal anchor
    "guest":             {"status": "names-only"},   # generic hospitality term; Easton covers hospitality
    "habaziniah":        {"status": "names-only"},   # Rechabite ancestor (Jer 35:3)
    "hagaba":            {"status": "names-only"},   # post-exile temple servant (Neh 7:48)
    "hagarenes-hagarites": {"status": "names-only"}, # tribe defeated by Reuben (1 Chr 5:10,19-20)
    "haggi":             {"status": "names-only"},   # son of Gad (Gen 46:16)
    # Old form of Ai (Gen 12:8 KJV); Easton has ai.json
    "hai":               {"status": "redirect-only", "redirect_to": "ai"},
    "hallohesh":         {"status": "names-only"},   # wall builder and covenant signer (Neh 3:12; 10:24)
    "hamuel":            {"status": "names-only"},   # Simeon descendant (1 Chr 4:26)
    # Smith article on biblical artisan trades; culturally significant background
    "handicraft":        {"status": "stub-needed"},
    "hararite":          {"status": "names-only"},   # descriptor for David's warrior Shammah (2 Sam 23:11)
    # Variant spelling of Armageddon (Rev 16:16); Easton has armageddon.json
    "harmagedon":        {"status": "redirect-only", "redirect_to": "armageddon"},
    "haroeh":            {"status": "names-only"},   # Judah descendant (1 Chr 2:52)
    "harorite":          {"status": "names-only"},   # descriptor for David's warrior (1 Chr 11:27)
    "hassenaah":         {"status": "names-only"},   # family who built the Fish Gate (Neh 3:3)
    "hasshub":           {"status": "names-only"},   # several post-exile figures (Neh 3:11,23; 10:23)
    "haziel":            {"status": "names-only"},   # Levite (1 Chr 23:9)
    # Easton has hebrews-epistle-to.json
    "hebrews-epistle-to-the": {"status": "redirect-only", "redirect_to": "hebrews-epistle-to"},
    "hedge":             {"status": "names-only"},   # thorny fence/barrier; no standalone doctrine
    # Ancient Egyptian city (= On/Aven) where Israelites were held captive; Jer 43:13; Ezek 30:17
    "heliopolis":        {"status": "stub-needed"},
    "hemam":             {"status": "names-only"},   # Horite son = Homam (1 Chr 1:39)
    "hemdan":            {"status": "names-only"},   # Horite chief (Gen 36:26)
    "herald":            {"status": "names-only"},   # royal announcer; no distinct biblical concept
    "hezeki":            {"status": "names-only"},   # Benjamin descendant (1 Chr 8:17)
    "hezronites":        {"status": "names-only"},   # Hezron's clan (Num 26:21)
    # Hebrew liquid measure (~0.6 litre); referenced in sacrificial/temple contexts
    "hin":               {"status": "stub-needed"},
    # The Behemoth of Job 40:15-24; most scholars identify as hippopotamus
    "hippopotamus":      {"status": "stub-needed"},
    "hodevah":           {"status": "names-only"},   # Levite family (Neh 7:43)
    # General Holofernes killed by Judith in the deuterocanonical Book of Judith
    "holofernes":        {"status": "stub-needed"},
    "hukok":             {"status": "names-only"},   # Naphtali/Asher town (Josh 19:34; 1 Chr 6:75)
    "humtah":            {"status": "names-only"},   # Judah hill town (Josh 15:54)
    "huppah":            {"status": "names-only"},   # priestly division (1 Chr 24:13)
    "hushim":            {"status": "names-only"},   # multiple OT figures (Gen 46:23; 1 Chr 8:8,11)
    "husks":             {"status": "names-only"},   # carob pods eaten by the prodigal son (Luke 15:16)
    "hyacinth":          {"status": "names-only"},   # precious stone in priestly/city lists
    # False teacher who rejected conscience and caused shipwreck of faith (1 Tim 1:20; 2 Tim 2:17)
    "hymenaeus":         {"status": "stub-needed"},
    "ibnijah":           {"status": "names-only"},   # Benjaminite (1 Chr 9:8)
    # Imago Dei + idol images + Nebuchadnezzar's statue; fundamental theological concept
    "image":             {"status": "stub-needed"},
    "imna":              {"status": "names-only"},   # Asher descendant (1 Chr 7:35)
    # Mosaic land-law inheritance + NT spiritual inheritance (Gal 3:18; Heb 1:14)
    "inheritance":       {"status": "stub-needed"},
    "instant-instantly": {"status": "skip"},          # archaic KJV word meaning "urgent/persistent"
    "irnahash":          {"status": "names-only"},   # Judah town = Ir-nahash (1 Chr 4:12)
    "iru":               {"status": "names-only"},   # son of Caleb (1 Chr 4:15)
    "ishbah":            {"status": "names-only"},   # father of Eshtemoa (1 Chr 4:17)
    "ishijah":           {"status": "names-only"},   # post-exile man (Ezra 10:31)
    "ismachiah":         {"status": "names-only"},   # Levite overseer under Hezekiah (2 Chr 31:13)
    "isuah":             {"status": "names-only"},   # son of Asher (Gen 46:17)
    "ithnan":            {"status": "names-only"},   # Judah town in the Negev (Josh 15:23)
    "ithra":             {"status": "names-only"},   # father of Amasa, David's nephew (2 Sam 17:25)
    "jahzah":            {"status": "names-only"},   # Reuben Levite town (Josh 13:18)
    "jahziel":           {"status": "names-only"},   # son of Naphtali (Gen 46:24)
    "jairite":           {"status": "names-only"},   # person from Jair (2 Sam 20:26)
    "jarha":             {"status": "names-only"},   # Egyptian servant who married into Israel (1 Chr 2:34)
    "jarimoth":          {"status": "names-only"},   # several minor OT figures
    "jaroah":            {"status": "names-only"},   # Gad descendant (1 Chr 5:14)
    "jashubilehem":      {"status": "names-only"},   # Judah descendant (1 Chr 4:22)
    "jecholiah":         {"status": "names-only"},   # mother of King Uzziah (2 Kgs 15:2)
    # Greek form of Jeconiah/Jehoiachin (Matt 1:11-12); Easton has jehoiachin.json
    "jeconias":          {"status": "redirect-only", "redirect_to": "jehoiachin"},
    "jehoshabeath":      {"status": "names-only"},   # princess who hid Joash; variant of Jehosheba (2 Chr 22:11)
    # Greek form of Jeremiah (Matt 16:14); Easton has jeremiah.json
    "jeremias":          {"status": "redirect-only", "redirect_to": "jeremiah"},
    # KJV form of Jeremiah (Matt 2:17; 27:9); Easton has jeremiah.json
    "jeremy":            {"status": "redirect-only", "redirect_to": "jeremiah"},
    "jeribai":           {"status": "names-only"},   # one of David's warriors (1 Chr 11:46)
    "jeshohaiah":        {"status": "names-only"},   # Simeon prince (1 Chr 4:36)
    "jesuites":          {"status": "names-only"},   # descendants of Jesui/Isui (Num 26:44)
    # Poetic name for Israel meaning "upright one" (Deut 32:15; 33:5,26; Isa 44:2)
    "jesurun":           {"status": "stub-needed"},
    # Smith's scholarly entry on the person of Jesus Christ
    "jesus-christ":      {"status": "stub-needed"},
    "jeuz":              {"status": "names-only"},   # Benjamin descendant (1 Chr 8:10)
    # Biblical precious gems/jewelry; significant in priestly garments, vision texts, wealth narratives
    "jewel":             {"status": "stub-needed"},
    "jewry":             {"status": "skip"},          # archaic KJV word for Judea (Dan 5:13 KJV)
    "jezliah":           {"status": "names-only"},   # Benjamin descendant (1 Chr 8:18)
    "jezreelitess":      {"status": "names-only"},   # woman from Jezreel (1 Sam 27:3)
    "jimnites-the":      {"status": "names-only"},   # descendants of Imnah (Num 26:44)
    "jiphthahel":        {"status": "names-only"},   # valley on Zebulun/Asher border (Josh 19:14,27)
    "joanan":            {"status": "names-only"},   # NT genealogy (Luke 3:27)
    "joda":              {"status": "names-only"},   # NT genealogy (Luke 3:26)
    # Smith's article on John the Apostle; no standalone Easton article
    "john-the-apostle":  {"status": "stub-needed"},
    # Greek/NT form of Jonah (John 1:42; Matt 16:17); Easton has jonah.json
    "jona":              {"status": "redirect-only", "redirect_to": "jonah"},
    "jonam":             {"status": "names-only"},   # NT genealogy (Luke 3:30)
    "jorai":             {"status": "names-only"},   # Gad leader (1 Chr 5:13)
    "josech":            {"status": "names-only"},   # NT genealogy (Luke 3:26)
    # Variant of Jehoshaphat; Easton has jehoshaphat.json
    "joshaphat":         {"status": "redirect-only", "redirect_to": "jehoshaphat"},
    "joshbekashah":      {"status": "names-only"},   # Levite musician (1 Chr 25:4,24)
    # Easton has joshua-the-book-of.json
    "joshua-book-of":    {"status": "redirect-only", "redirect_to": "joshua-the-book-of"},
    # Greek form of Josiah (Matt 1:10-11); Easton has josiah.json
    "josias":            {"status": "redirect-only", "redirect_to": "josiah"},
    "jotbah":            {"status": "names-only"},   # hometown of King Amon's mother (2 Kgs 21:19)
    "jozadak":           {"status": "names-only"},   # father of high priest Jeshua (Ezra 3:2)
    # Easton has judas.json (covers all OT/NT Judases)
    "judas-iscariot":    {"status": "redirect-only", "redirect_to": "judas"},
    # Leader of the Maccabean revolt; 1–2 Maccabees; significant in Second Temple history
    "judas-maccabaeus":  {"status": "stub-needed"},
    # Revolutionary who led tax-revolt; mentioned by Gamaliel (Acts 5:37)
    "judas-of-galilee":  {"status": "stub-needed"},
    # Brother of Jesus; probable author of the Epistle of Jude
    "judas-the-lords-brother": {"status": "stub-needed"},
    "kenezite":          {"status": "names-only"},   # Kenaz descendants; Caleb called a Kenezite
    "kiriathaim":        {"status": "names-only"},   # Moabite city (Num 32:37; Ezek 25:9)
    "kolaiah":           {"status": "names-only"},   # two OT figures (Neh 11:7; Jer 29:21)
    "lacedaemonians":    {"status": "names-only"},   # Spartans who corresponded with Jewish leaders (1 Macc 12)
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
    print(f'BPG Curation C09: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
