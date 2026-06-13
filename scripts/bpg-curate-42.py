"""
BPG Curation — Batch C42: exquisite → fire-lake-of (gaps 4099–4198)
Gaps reviewed: 100 (score-5 isbe-scholarly E–F entries)

Score-5 ISBE entries continue as overwhelmingly lexical/archaic KJV terms and
minor compound forms. Notable stubs: fall-the (THE FALL — Gen 3 doctrine of
original sin, central to soteriology) and fire-lake-of (Lake of Fire — Rev 20,
eschatological judgment). Five redirects to Easton canonical articles.
2 stub-needed; 5 redirects; 93 names-only.

Script: scripts/bpg-curate-42.py
Run: python3 scripts/bpg-curate-42.py  (from project root)
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
    "exquisite":              {"status": "names-only"},   # KJV "exquisite torment"; lexical
    "extinct":                {"status": "names-only"},   # KJV "quenched"; lexical
    "extortion":              {"status": "names-only"},   # Ezek 22:12; Luke 11:39; covered under "Oppression"
    "extreme;-extremity":     {"status": "names-only"},   # lexical
    "eyelid":                 {"status": "names-only"},   # Job 16:16; Jer 9:18; anatomical/lexical
    "eyepaint":               {"status": "names-only"},   # 2 Kings 9:30 (Jezebel); cosmetic/cultural
    "eyes-blinding-of-the":   {"status": "names-only"},   # 2 Kings 25:7; Gen 19:11; cultural practice
    "eyes-covering-of-the":   {"status": "names-only"},   # Gen 20:16; cultural custom
    "eyes-diseases-of-the":   {"status": "names-only"},   # medical; cultural
    "eyes-tender":            {"status": "names-only"},   # Leah "tender eyes" (Gen 29:17); lexical
    "eyesalve":               {"status": "names-only"},   # Rev 3:18; brief; covered under Laodicea
    "eyeservice":             {"status": "names-only"},   # KJV Eph 6:6; Col 3:22; lexical
    "ezar":                   {"status": "names-only"},   # variant of Ezer; Horite clan (Gen 36:21 variant)
    "ezechias;-ezecias":      {"status": "names-only"},   # Greek form of Hezekiah; disambiguation
    "ezerias":                {"status": "names-only"},   # apocryphal name (1 Esd 9:34)
    "ezias":                  {"status": "names-only"},   # apocryphal/variant name
    "eznite":                 {"status": "names-only"},   # demonym; Adino the Eznite (2 Sam 23:8 variant)
    "ezora":                  {"status": "names-only"},   # apocryphal family (1 Esd 9:34)
    # ISBE treats Ezra-Nehemiah as one book; redirect to canonical Easton article on Ezra
    "ezra-nehemiah":          {"status": "redirect-only", "redirect_to": "ezra"},
    "ezril":                  {"status": "names-only"},   # apocryphal name (1 Esd 9:34)
    "fact":                   {"status": "names-only"},   # lexical
    "fade":                   {"status": "names-only"},   # lexical; "fadeth away" (Isa 40:7; Jas 1:11)
    "fail":                   {"status": "names-only"},   # lexical
    "fain":                   {"status": "names-only"},   # KJV "gladly/eagerly" (Luke 15:16); lexical
    "faint":                  {"status": "names-only"},   # lexical
    "fair":                   {"status": "names-only"},   # lexical
    "faithful-sayings":       {"status": "names-only"},   # "faithful saying" formula (1 Tim 1:15; Tit 3:8); brief
    "faithful;-faithfulness": {"status": "names-only"},   # covered under "Faith" and "Faithfulness" in Easton
    "faithless":              {"status": "names-only"},   # KJV "faithless generation" (Matt 17:17); lexical
    "falcon":                 {"status": "names-only"},   # bird (Job 28:7 KJV); natural history
    "fall":                   {"status": "names-only"},   # lexical verb; covered under "Fall, The"
    # The Fall (Gen 3): Adam and Eve's disobedience; "through one man sin entered the world" (Rom 5:12);
    # "in Adam all die" (1 Cor 15:22); cursed ground, enmity between seed (Gen 3:15); foundational for
    # hamartiology, soteriology, and the need for redemption; not in Easton as its own article
    "fall-the":               {"status": "stub-needed"},
    "falling-stars":          {"status": "names-only"},   # eschatological sign (Matt 24:29; Rev 6:13); brief
    "fallow":                 {"status": "names-only"},   # agricultural term (Jer 4:3; Hos 10:12); lexical
    "false-prophets":         {"status": "names-only"},   # covered under "Prophets, False" in Easton
    "false-swearing;-false-witness": {"status": "names-only"},  # covered under "Perjury" and "Testimony" in Easton
    "false-christs":          {"status": "names-only"},   # Matt 24:24; Mark 13:22; covered under eschatology
    "falsehood":              {"status": "names-only"},   # covered under "Lying" in Easton
    "fame":                   {"status": "names-only"},   # lexical
    "familiar":               {"status": "names-only"},   # "familiar spirit" KJV; covered under "Divination" in Easton
    "family":                 {"status": "names-only"},   # general; covered under "House" and "Marriage" in Easton
    "family-relationships":   {"status": "names-only"},   # general; too broad at score-5
    "famish":                 {"status": "names-only"},   # KJV "starve" (Gen 41:55; Isa 5:13); lexical
    "fan-fanner":             {"status": "names-only"},   # winnowing fan (Ruth 3:2; Jer 51:2); cultural/agricultural
    "fancy":                  {"status": "names-only"},   # lexical
    "far-house":              {"status": "names-only"},   # uncertain ISBE term; probably textual variant
    "far;-farther":           {"status": "names-only"},   # lexical
    "fare":                   {"status": "names-only"},   # lexical
    "farewell":               {"status": "names-only"},   # lexical
    "fashion":                {"status": "names-only"},   # lexical
    # Easton has a "Fasting" article; redirect to canonical
    "fast;-fasting":          {"status": "redirect-only", "redirect_to": "fasting"},
    # ISBE compound article combining both; redirect to Easton "Feasts"
    "fasts-and-feasts":       {"status": "redirect-only", "redirect_to": "feasts"},
    "fat-vat":                {"status": "names-only"},   # KJV wine/oil vat (Joel 2:24); agricultural/cultural
    "fathers-house-fathers-house": {"status": "names-only"},  # "beth-ab"; covered under "House" in Easton
    "father-god-the":         {"status": "names-only"},   # covered under "God" and "Trinity" in Easton
    "father-in-law":          {"status": "names-only"},   # kinship term; lexical
    "fatherless":             {"status": "names-only"},   # orphan care; covered under "Orphan" in Easton
    "fathers-brother":        {"status": "names-only"},   # kinship term; lexical
    "fatling;-fatted":        {"status": "names-only"},   # "fatted calf" (Luke 15:23); "fatlings" (2 Sam 6:13); lexical
    "fatness":                {"status": "names-only"},   # lexical
    "fauchion":               {"status": "names-only"},   # KJV variant of "falchion" (curved sword); lexical
    "fault":                  {"status": "names-only"},   # lexical
    "favor":                  {"status": "names-only"},   # lexical
    "fawn":                   {"status": "names-only"},   # young deer; natural history; lexical
    "fear":                   {"status": "names-only"},   # "fear of the LORD"; covered under "Fear" in Easton
    # ISBE alternate compound article; redirect to Easton "Feasts"
    "feasts-and-fasts":       {"status": "redirect-only", "redirect_to": "feasts"},
    "feasts-seasons-for":     {"status": "names-only"},   # ISBE sub-entry; covered under "Feasts" in Easton
    "feathers":               {"status": "names-only"},   # natural history; "wings like a dove" (Ps 55:6); lexical
    "feeble-knees":           {"status": "names-only"},   # Isa 35:3; Heb 12:12; idiom/lexical
    "feeble-minded":          {"status": "names-only"},   # KJV 1 Thess 5:14 ("encourage the fainthearted"); lexical
    "feeling":                {"status": "names-only"},   # lexical
    "feet-washing-of":        {"status": "names-only"},   # John 13:1-17; covered under "Washing" in Easton
    "feign":                  {"status": "names-only"},   # lexical; "feigned madness" (1 Sam 21:13)
    # Roman governor (Acts 23-24); Easton has "Felix" article; redirect
    "felix;-antonius":        {"status": "redirect-only", "redirect_to": "felix"},
    "felloes":                {"status": "names-only"},   # KJV "felloe/felly" of wheel (1 Kings 7:33); lexical
    "fellow":                 {"status": "names-only"},   # lexical
    "female":                 {"status": "names-only"},   # lexical
    "ferry-boat":             {"status": "names-only"},   # 2 Sam 19:18; cultural/transport
    "fervent":                {"status": "names-only"},   # lexical; "fervent in spirit" (Rom 12:11)
    "festival":               {"status": "names-only"},   # general; covered under "Feasts" in Easton
    "fetch":                  {"status": "names-only"},   # lexical
    "fetter":                 {"status": "names-only"},   # chains/shackles; cultural/lexical
    "fiery-heat":             {"status": "names-only"},   # lexical
    "fiery-serpent":          {"status": "names-only"},   # Num 21:6-9; covered under "Serpent" in Easton
    "fight":                  {"status": "names-only"},   # lexical
    "figure":                 {"status": "names-only"},   # lexical
    "file":                   {"status": "names-only"},   # 1 Sam 13:21 KJV; tool; lexical
    "fillet":                 {"status": "names-only"},   # Exod 27:10-11 tabernacle term; architectural/cultural
    "filth;-filthiness;-filthy": {"status": "names-only"},  # lexical/moral; covered under "Purity" in Easton
    "fin":                    {"status": "names-only"},   # dietary law (Lev 11:9-10); brief
    "fine":                   {"status": "names-only"},   # lexical
    "finer;-fining":          {"status": "names-only"},   # refining metal (Prov 17:3; 25:4); brief cultural
    "fines":                  {"status": "names-only"},   # legal penalties; cultural
    "finger-1":               {"status": "names-only"},   # anatomical; lexical
    "finger-2":               {"status": "names-only"},   # "finger of God" (Exod 8:19; Luke 11:20); brief
    "finish":                 {"status": "names-only"},   # lexical
    "finisher":               {"status": "names-only"},   # "author and finisher of our faith" (Heb 12:2 KJV)
    "fir;-fir-tree":          {"status": "names-only"},   # botanical (1 Kings 5:8; Ps 104:17); natural history
    "fire-baptism":           {"status": "names-only"},   # "baptism of fire" (Matt 3:11; Luke 3:16); covered under "Baptism"
    # "Lake of fire" (Rev 19:20; 20:10,14-15); eschatological place of final judgment; distinct from Gehenna;
    # "second death" (Rev 20:14); eternal punishment debate; not covered in Easton as a named article
    "fire-lake-of":           {"status": "stub-needed"},
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
    print(f'BPG Curation C42: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
