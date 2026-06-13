"""
BPG Curation — Batch C43: fire-strange → frock (gaps 4199–4298)
Gaps reviewed: 100 (score-5 isbe-scholarly F entries — fire compounds, first/firstborn,
fishing terms, fold, foreknowledge, forest, forgiveness, fort, freedom, friend range)

Numerals (five, forty, four, fourscore, etc.) and lexical verbs (flee, follow, forbid,
forfeit, forego, etc.) are names-only. Significant redirects to canonical Easton articles:
first-begotten/firstborn/firstling → first-born; fishing compounds → fisher/fish-hooks/
fishing-the-art-of; forgiveness → forgiveness-of-sin; foreknowledge → foreknowledge-of-god;
fortification compound → fenced-cities; freedom compounds → freedom.
0 stub-needed; 14 redirects; 86 names-only.

Script: scripts/bpg-curate-43.py
Run: python3 scripts/bpg-curate-43.py  (from project root)
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
    "fire-strange":              {"status": "names-only"},   # Lev 10:1; Num 3:4; Nadab/Abihu; covered under fire
    "fire-unquenchable":         {"status": "names-only"},   # Matt 3:12; Mark 9:43-48; eschatological; covered under fire
    "fires":                     {"status": "names-only"},   # plural/lexical; names-only
    "first":                     {"status": "names-only"},   # lexical
    # Rev 1:5; Heb 1:6 KJV "firstbegotten"; Greek prototokos; Easton has first-born.json
    "first-begotten":            {"status": "redirect-only", "redirect_to": "first-born"},
    # ISBE combined article on the firstborn institution; Easton has first-born.json
    "firstborn;-firstling":      {"status": "redirect-only", "redirect_to": "first-born"},
    # Deut 12:6; Exod 34:19; animal firstlings offered to God; Easton has first-born.json
    "firstling":                 {"status": "redirect-only", "redirect_to": "first-born"},
    "fish-gate":                 {"status": "names-only"},   # Neh 3:3; 12:39; Jerusalem gate; minor place
    "fishers-coat":              {"status": "names-only"},   # John 21:7 KJV "fisher's coat"; lexical/cultural
    # ISBE compound; Matt 4:18-19; Easton has fisher.json
    "fisher;-fisherman":         {"status": "redirect-only", "redirect_to": "fisher"},
    # Job 41:1; Amos 4:2; Hab 1:15; Easton has fish-hooks.json
    "fishhook":                  {"status": "redirect-only", "redirect_to": "fish-hooks"},
    # Matt 4:18-22; John 21; Easton has fishing-the-art-of.json
    "fishing":                   {"status": "redirect-only", "redirect_to": "fishing-the-art-of"},
    "fit-fitly":                 {"status": "names-only"},   # Eph 4:16 "fitly joined"; lexical
    "five":                      {"status": "names-only"},   # numeral; lexical
    "flake":                     {"status": "names-only"},   # Job 41:23 KJV; lexical
    "flame":                     {"status": "names-only"},   # lexical; general fire term; covered under fire
    "flat-nose":                 {"status": "names-only"},   # Lev 21:18 KJV priestly disqualification; medical/cultural
    "flaying":                   {"status": "names-only"},   # Mic 3:3; cultural/judicial practice
    "flee":                      {"status": "names-only"},   # lexical; "flee temptation" (1 Cor 6:18; 1 Tim 6:11)
    "flesh-and-blood":           {"status": "names-only"},   # Matt 16:17; 1 Cor 15:50; idiom; covered under flesh
    "flesh-pot":                 {"status": "names-only"},   # Exod 16:3; cooking vessel; cultural; covered under flesh
    # Exod 8:21-31; Eccl 10:1; Ps 78:45; Easton has fly.json
    "flies":                     {"status": "redirect-only", "redirect_to": "fly"},
    "float-flote":               {"status": "names-only"},   # 1 Kgs 5:9; 2 Chr 2:16 KJV "raft"; nautical/cultural
    "flock":                     {"status": "names-only"},   # general; covered under fold/shepherd in Easton
    "flote-float":               {"status": "names-only"},   # variant of float-flote; same raft reference
    "flourish":                  {"status": "names-only"},   # Ps 72:7; 92:12; lexical/poetic
    "flue;-net":                 {"status": "names-only"},   # Isa 19:8 KJV fishing net; covered under fishing
    "flux":                      {"status": "names-only"},   # Acts 28:8 KJV "dysentery"; medical/lexical
    "foal":                      {"status": "names-only"},   # Gen 49:11; Zech 9:9; Matt 21:5; covered under ass/donkey
    # Num 32:16; 1 Sam 24:3; Ps 50:9; Easton has fold.json
    "fold;-folding":             {"status": "redirect-only", "redirect_to": "fold"},
    "folk":                      {"status": "names-only"},   # KJV collective "people"; lexical
    "follow":                    {"status": "names-only"},   # lexical; discipleship term
    "follower":                  {"status": "names-only"},   # Eph 5:1; 1 Pet 3:13; lexical
    "folly":                     {"status": "names-only"},   # Prov 9:13; 2 Sam 13:12; lexical; covered under wisdom
    "fool;-folly":               {"status": "names-only"},   # ISBE combined; Ps 14:1; Prov 10:18; covered under wisdom
    "foolery":                   {"status": "names-only"},   # KJV variant; lexical
    "foot":                      {"status": "names-only"},   # anatomical; lexical; washing of feet covered elsewhere
    "for":                       {"status": "names-only"},   # lexical/grammatical
    "foray":                     {"status": "names-only"},   # KJV military raid term; lexical
    "forbear":                   {"status": "names-only"},   # lexical; "forbear not" (Ezek 2:5); 2 Chr 35:21
    "forbearance":               {"status": "names-only"},   # Rom 3:25; 2 Pet 3:9; covered under patience/longsuffering
    "forbid":                    {"status": "names-only"},   # lexical; "God forbid" (Rom 3:4 KJV)
    "forecast":                  {"status": "names-only"},   # Dan 11:24-25 KJV "devise plans"; lexical
    "forefather":                {"status": "names-only"},   # lexical; 2 Tim 1:3; patriarchal term
    "forefront":                 {"status": "names-only"},   # 2 Sam 11:15; Ezek 40:19; lexical
    "forego":                    {"status": "names-only"},   # lexical
    "foreign-divinities":        {"status": "names-only"},   # covered under idols/idolatry in Easton
    # Acts 2:23; Rom 8:29-30; 1 Pet 1:2; Easton has foreknowledge-of-god.json
    "foreknow;-foreknowledge":   {"status": "redirect-only", "redirect_to": "foreknowledge-of-god"},
    "foreordain;-forordination": {"status": "names-only"},   # Rom 8:29-30; Eph 1:5,11; covered under foreknowledge/predestination
    "forepart":                  {"status": "names-only"},   # Exod 28:27; Acts 27:41 KJV; lexical
    "foresail":                  {"status": "names-only"},   # Acts 27:40; nautical/cultural
    "foreship":                  {"status": "names-only"},   # Acts 27:30 KJV; nautical/cultural
    "foreskin":                  {"status": "names-only"},   # Gen 17:14; Exod 4:25; covered under circumcision
    # 2 Sam 18:6-8 battle site; Easton has forest.json
    "forest-of-ephraim":         {"status": "redirect-only", "redirect_to": "forest"},
    "foretell;-foretold":        {"status": "names-only"},   # lexical; covered under prophecy
    "forfeit":                   {"status": "names-only"},   # lexical; Ezra 10:8; 1 Chr 26:27
    "forge;-forger":             {"status": "names-only"},   # Isa 54:16; 1 Sam 13:19; cultural metalworking
    "forget;-forgetful":         {"status": "names-only"},   # ISBE compound; Jas 1:25; lexical
    # Matt 26:28; Acts 10:43; Luke 24:47; Easton has forgiveness-of-sin.json
    "forgiveness":               {"status": "redirect-only", "redirect_to": "forgiveness-of-sin"},
    "forgo":                     {"status": "names-only"},   # lexical
    "fork":                      {"status": "names-only"},   # 1 Sam 13:21; agricultural tool; cultural
    "form":                      {"status": "names-only"},   # lexical; Phil 2:6 "form of God"
    "former":                    {"status": "names-only"},   # lexical; "former rain" (Deut 11:14) covered elsewhere
    "forswear":                  {"status": "names-only"},   # Matt 5:33 KJV "swear falsely"; lexical
    "forth":                     {"status": "names-only"},   # lexical
    # ISBE major compound; Easton has fenced-cities.json for fortified city system
    "fortification;-fort;-fortified-cities;-fortress": {"status": "redirect-only", "redirect_to": "fenced-cities"},
    "fortune":                   {"status": "names-only"},   # Isa 65:11 "Gad" (Fortune) deity; covered under Gad/idolatry
    "forty":                     {"status": "names-only"},   # numeral; "forty years in wilderness" etc.; lexical
    "forum":                     {"status": "names-only"},   # Acts 28:15 "Forum of Appius"; Roman place; minor
    "forward;-forwardness":      {"status": "names-only"},   # ISBE compound; 2 Cor 9:2 KJV "forwardness"; lexical
    "foul":                      {"status": "names-only"},   # lexical; ritual uncleanness; covered under clean/unclean
    "foundation":                {"status": "names-only"},   # Heb 6:1; Matt 7:24-27; lexical; covered under several topics
    "founder":                   {"status": "names-only"},   # Jer 6:29; 10:9,14; metalworking craftsman; cultural
    "fountain-gate":             {"status": "names-only"},   # Neh 2:14; 3:15; 12:37; Jerusalem gate; minor place
    "four":                      {"status": "names-only"},   # numeral; lexical
    "four-hundred":              {"status": "names-only"},   # numeral; lexical
    "four-thousand":             {"status": "names-only"},   # numeral; lexical
    "fourfold":                  {"status": "names-only"},   # Luke 19:8 Zacchaeus; lexical
    "fourscore":                 {"status": "names-only"},   # KJV "eighty"; numeral; lexical
    "foursquare":                {"status": "names-only"},   # Rev 21:16; Exod 27:1; lexical; covered under New Jerusalem
    "fourteen":                  {"status": "names-only"},   # numeral; lexical
    "fourth-part":               {"status": "names-only"},   # numeral; lexical
    "fowl-fatted":               {"status": "names-only"},   # 1 Kgs 4:23 royal provisions; cultural
    "fragment":                  {"status": "names-only"},   # John 6:12 feeding miracle; lexical
    "frame":                     {"status": "names-only"},   # lexical
    "frankly":                   {"status": "names-only"},   # Luke 7:42 KJV "freely forgave"; lexical
    "fray":                      {"status": "names-only"},   # Deut 28:26; Jer 7:33 KJV "frighten"; lexical
    "freckled-spot":             {"status": "names-only"},   # Lev 13:39 KJV; dermatological/priestly diagnosis; medical
    # ISBE combined; Gal 5:1; John 8:32; Easton has freedom.json
    "free;-freedom":             {"status": "redirect-only", "redirect_to": "freedom"},
    # ISBE combined; 1 Cor 7:22; Easton has freedom.json (covers freedman concept)
    "freedman;-freeman":         {"status": "redirect-only", "redirect_to": "freedom"},
    "freely":                    {"status": "names-only"},   # lexical; "freely ye have received" (Matt 10:8)
    "freewoman":                 {"status": "names-only"},   # Gal 4:22-31 Sarah allegory; covered under Hagar/Sarah
    "frequent":                  {"status": "names-only"},   # 2 Cor 11:23 KJV "in stripes above measure"; lexical
    "fresh":                     {"status": "names-only"},   # lexical
    "fret-fretting":             {"status": "names-only"},   # Ps 37:1,7-8 "fret not"; Lev 13:51 "fretting leprosy"; lexical
    "fried":                     {"status": "names-only"},   # Lev 7:12 fried grain offerings; dietary/cultic
    "friend;-friendship":        {"status": "names-only"},   # ISBE combined; Prov 17:17; John 15:13-15; lexical
    "friends;-chief-friends":    {"status": "names-only"},   # ISBE compound; Esth 6:13; Prov 19:4; lexical
    "fringes":                   {"status": "names-only"},   # Num 15:38-40; Deut 22:12; Matt 9:20; covered under frontlets
    "frock":                     {"status": "names-only"},   # KJV archaic garment term; lexical
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
    print(f'BPG Curation C43: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
