"""
BPG Curation — Batch C57: nabathites → noah-2 (gaps 5804–5903)
Gaps reviewed: 100 (score-5 isbe-scholarly N entries — Nahalal, Nahum, Nathan,
Nathanael, Nebo, Nebuchadnezzar, Necho, Nazirite, Nicanor, Noah disambiguations,
plus New Testament scholarly compounds)

Redirects: nacon→nachon; nahalal/nahallal/nahalol→nahallal; naharai/nahari→naharai;
nahum/book-of→nahum; naked/nakedness→naked; nathan-1/2→nathan;
nathanael-1/2→nathanael; nazirite→nazarite; nebo-1/2/mount→nebo;
nebuchadnezzar/nebuchadrezzar→nebuchadnezzar; nebushazban→nebushasban;
necho/nechoh/neco→necho-ii; necromancy→necromancer;
neginah/neginoth→neginah; nehemias→nehemiah; nemuelites→nemuel;
nephish compounds→naphish; nethanel→nethaneel;
netophathi/netophathites→netophah; nicanor-1/2→nicanor;
nicolaus/nicolas→nicolas; night-hawk→night-hawk;
nimrah/beth-nimrah→nimrah; noah-1/2→noah.
0 stub-needed; 33 redirects; 67 names-only.

Script: scripts/bpg-curate-57.py
Run: python3 scripts/bpg-curate-57.py  (from project root)
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
    "nabathites":                {"status": "names-only"},   # 1 Chr 5:19; Nabataean/Ishmaelite variant; names-only
    # ISBE; 2 Sam 6:6; Easton has nachon.json
    "nacon-the-threshing-floor-of": {"status": "redirect-only", "redirect_to": "nachon"},
    "nadabath":                  {"status": "names-only"},   # 1 Macc 9:37; apocryphal place
    # ISBE; Josh 19:15; 21:35; Easton has nahallal.json
    "nahalal":                   {"status": "redirect-only", "redirect_to": "nahallal"},
    # ISBE compound; Josh 19:15; Judg 1:30; Easton has nahallal.json
    "nahallal;-nahalol":         {"status": "redirect-only", "redirect_to": "nahallal"},
    "nahamani":                  {"status": "names-only"},   # Neh 7:7; minor post-exilic returnee; names-only
    # ISBE compound; 2 Sam 23:37; 1 Chr 11:39; Easton has naharai.json
    "naharai;-nahari":           {"status": "redirect-only", "redirect_to": "naharai"},
    # ISBE compound; Easton has nahum.json and nahum-book-of.json
    "nahum;-the-book-of":        {"status": "redirect-only", "redirect_to": "nahum"},
    "naidus":                    {"status": "names-only"},   # 1 Esd 5:21 variant; apocryphal
    # ISBE compound; Gen 2:25; Rev 3:17; Easton has naked.json
    "naked;-nakedness":          {"status": "redirect-only", "redirect_to": "naked"},
    "name":                      {"status": "names-only"},   # ISBE; theological concept; names-only
    "names-of-god":              {"status": "names-only"},   # ISBE; divine names; significant but no dedicated Easton slug
    "names-proper":              {"status": "names-only"},   # ISBE scholarly; biblical onomastics; names-only
    "nanaea":                    {"status": "names-only"},   # 2 Macc 1:13,15; Seleucid goddess; apocryphal
    "naphath-dor":               {"status": "names-only"},   # Josh 12:23; 1 Kgs 4:11 "heights of Dor"; names-only
    "naphisi":                   {"status": "names-only"},   # 1 Chr 5:19 variant; names-only
    "naphoth-dor":               {"status": "names-only"},   # 1 Kgs 4:11 variant of naphath-dor; names-only
    "naphthar":                  {"status": "names-only"},   # 2 Macc 1:36 "naphtha" substance; apocryphal
    "nasbas":                    {"status": "names-only"},   # 1 Esd 5:31 variant; apocryphal
    "nasi":                      {"status": "names-only"},   # ISBE; Hebrew "prince/leader" = tribal head; names-only
    "nasor":                     {"status": "names-only"},   # 1 Macc 11:67; apocryphal place
    # ISBE disambiguation; 2 Sam 7:2; prophet; Easton has nathan.json
    "nathan-1":                  {"status": "redirect-only", "redirect_to": "nathan"},
    # ISBE disambiguation; 2 Sam 5:14; David's son; Easton has nathan.json
    "nathan-2":                  {"status": "redirect-only", "redirect_to": "nathan"},
    # ISBE disambiguation; John 1:45-49; apostle; Easton has nathanael.json
    "nathanael-1":               {"status": "redirect-only", "redirect_to": "nathanael"},
    # ISBE disambiguation; Ezra 10:22; minor figure; Easton has nathanael.json
    "nathanael-2":               {"status": "redirect-only", "redirect_to": "nathanael"},
    "nathanias":                 {"status": "names-only"},   # 1 Esd 9:34 variant; apocryphal
    "nations":                   {"status": "names-only"},   # general; covered under gentiles in Easton; names-only
    "nativity-of-mary-gospel-of-the": {"status": "names-only"},  # Protoevangelium; apocryphal; extracanonical
    "natural-features":          {"status": "names-only"},   # ISBE scholarly; Palestinian geography; names-only
    "natural-history":           {"status": "names-only"},   # ISBE scholarly; names-only
    "natural-man-the":           {"status": "names-only"},   # ISBE; 1 Cor 2:14; covered under man-natural; names-only
    "natural;-nature":           {"status": "names-only"},   # ISBE compound; Rom 1:26-27; lexical
    "nature":                    {"status": "names-only"},   # lexical
    "naught;-naughty;-naughtiness": {"status": "names-only"},   # ISBE compound; Prov 6:12; KJV; lexical
    "nave-1":                    {"status": "names-only"},   # ISBE disambiguation; 1 Kgs 7:33 "nave" = wheel hub; names-only
    "nave-2":                    {"status": "names-only"},   # ISBE disambiguation; variant form; names-only
    "navel":                     {"status": "names-only"},   # Ezek 38:12 KJV "navel of the earth"; Song 7:2; lexical
    "navy":                      {"status": "names-only"},   # 1 Kgs 9:26; 10:11; lexical
    # ISBE; Num 6:1-21; Easton has nazarite.json
    "nazirite":                  {"status": "redirect-only", "redirect_to": "nazarite"},
    "near-nigh":                 {"status": "names-only"},   # ISBE compound; lexical
    # ISBE disambiguation; Deut 34:1; mount; Easton has nebo.json
    "nebo-1":                    {"status": "redirect-only", "redirect_to": "nebo"},
    # ISBE disambiguation; Isa 46:1; Babylonian deity; Easton has nebo.json
    "nebo-2":                    {"status": "redirect-only", "redirect_to": "nebo"},
    # ISBE; Deut 34:1; Easton has nebo.json
    "nebo-mount":                {"status": "redirect-only", "redirect_to": "nebo"},
    # ISBE compound; 2 Kgs 24:1; Jer 39:5; Easton has nebuchadnezzar.json
    "nebuchadnezzar;-nebuchadrezzar": {"status": "redirect-only", "redirect_to": "nebuchadnezzar"},
    # ISBE; Jer 39:13; Easton has nebushasban.json
    "nebushazban":               {"status": "redirect-only", "redirect_to": "nebushasban"},
    # ISBE compound; 2 Kgs 23:29; 2 Chr 35:20-24; Easton has necho-ii.json
    "necho;-nechoh":             {"status": "redirect-only", "redirect_to": "necho-ii"},
    "necklace":                  {"status": "names-only"},   # Judg 8:26; Isa 3:19; cultural; names-only
    # ISBE; variant of Necho; Easton has necho-ii.json
    "neco":                      {"status": "redirect-only", "redirect_to": "necho-ii"},
    "necodan":                   {"status": "names-only"},   # 1 Esd 5:37 variant; apocryphal
    # ISBE; Deut 18:11; Easton has necromancer.json
    "necromancy":                {"status": "redirect-only", "redirect_to": "necromancer"},
    "needlework":                {"status": "names-only"},   # Exod 26:36; Ps 45:14; embroidery; names-only
    "needy":                     {"status": "names-only"},   # Ps 40:17; Isa 41:17; lexical
    "neesing":                   {"status": "names-only"},   # Job 41:18 KJV archaic "sneezing"; lexical
    "negeb":                     {"status": "names-only"},   # ISBE; southern desert of Canaan; no dedicated Easton slug
    # ISBE compound; psalm superscriptions; Easton has neginah.json
    "neginah;-neginoth":         {"status": "redirect-only", "redirect_to": "neginah"},
    # Greek form of Nehemiah; Easton has nehemiah.json
    "nehemias":                  {"status": "redirect-only", "redirect_to": "nehemiah"},
    "neigh":                     {"status": "names-only"},   # Jer 5:8; 50:11 KJV; lexical
    "neighbor":                  {"status": "names-only"},   # Exod 20:16-17; Lev 19:18; lexical
    "nekodan":                   {"status": "names-only"},   # 1 Esd variant; apocryphal
    # ISBE; Num 26:12; clan of Nemuel; Easton has nemuel.json
    "nemuelites":                {"status": "redirect-only", "redirect_to": "nemuel"},
    "nephea":                    {"status": "names-only"},   # 1 Esd 5:21 variant; apocryphal
    "nephew":                    {"status": "names-only"},   # Judg 12:14; 1 Tim 5:4 KJV "grandson"; lexical
    "nephi":                     {"status": "names-only"},   # 1 Macc 12:37; apocryphal spring; names-only
    "nephis":                    {"status": "names-only"},   # 1 Esd 5:21 variant; apocryphal
    # ISBE compound; Ezra 2:50; Neh 7:52; Easton has naphish.json
    "nephish;-nephisim;-nephishesim;-nephusim": {"status": "redirect-only", "redirect_to": "naphish"},
    "nephthai":                  {"status": "names-only"},   # 2 Macc 1:36 variant of naphthar; apocryphal
    "nephthar;-nephthai":        {"status": "names-only"},   # ISBE compound; apocryphal naphtha substance
    # ISBE compound; variant of nephish; Easton has naphish.json
    "nephushesim;-nephishesim":  {"status": "redirect-only", "redirect_to": "naphish"},
    "nerias":                    {"status": "names-only"},   # Greek form of Neriah; Jer 32:12; names-only
    "nest":                      {"status": "names-only"},   # Deut 22:6; Job 29:18; lexical
    "netaim":                    {"status": "names-only"},   # 1 Chr 4:23 KJV royal potters' settlement; names-only
    # ISBE; Num 1:8; 1 Chr 2:14; Easton has nethaneel.json
    "nethanel":                  {"status": "redirect-only", "redirect_to": "nethaneel"},
    "netophas":                  {"status": "names-only"},   # 1 Esd 5:18 variant; apocryphal
    # ISBE compound; Neh 12:28; Easton has netophah.json
    "netophathi;-netophathites": {"status": "redirect-only", "redirect_to": "netophah"},
    "nettles":                   {"status": "names-only"},   # Job 30:7; Prov 24:31; Zeph 2:9; botanical/names-only
    "network":                   {"status": "names-only"},   # 1 Kgs 7:17-18,20; temple detail; names-only
    "new-birth":                 {"status": "names-only"},   # John 3:3-8; covered under regeneration in Easton
    "new-commandment":           {"status": "names-only"},   # John 13:34; names-only
    "new-covenant":              {"status": "names-only"},   # Jer 31:31-34; Heb 8:8-13; covered under covenant
    "new-earth":                 {"status": "names-only"},   # Rev 21:1; 2 Pet 3:13; eschatological; names-only
    "new-heavens":               {"status": "names-only"},   # Isa 65:17; Rev 21:1; names-only
    "new-jerusalem":             {"status": "names-only"},   # Rev 21:2; eschatological; names-only
    "new-man":                   {"status": "names-only"},   # Eph 4:24; Col 3:10; names-only
    "new-testament-canon":       {"status": "names-only"},   # ISBE scholarly; names-only
    "new-testament-language":    {"status": "names-only"},   # ISBE scholarly; Koine Greek; names-only
    "new-testament-text":        {"status": "names-only"},   # ISBE scholarly; textual criticism; names-only
    "new;-newness":              {"status": "names-only"},   # ISBE compound; lexical
    # ISBE disambiguation; 1 Macc 3:38; Seleucid general; Easton has nicanor.json
    "nicanor-1":                 {"status": "redirect-only", "redirect_to": "nicanor"},
    # ISBE disambiguation; Acts 6:5; deacon at Jerusalem; Easton has nicanor.json
    "nicanor-2":                 {"status": "redirect-only", "redirect_to": "nicanor"},
    "nicodemus-gospel-of":       {"status": "names-only"},   # apocryphal "Acts of Pilate"; extracanonical
    # ISBE compound; Acts 6:5; Rev 2:6,15; Easton has nicolas.json
    "nicolaus;-nicolas":         {"status": "redirect-only", "redirect_to": "nicolas"},
    "nigh":                      {"status": "names-only"},   # KJV archaic "near"; lexical
    # Lev 11:16; Deut 14:15; Easton has night-hawk.json
    "night-hawk":                {"status": "redirect-only", "redirect_to": "night-hawk"},
    "night-monster":             {"status": "names-only"},   # Isa 34:14 "Lilith" KJV; names-only
    "night-watch":               {"status": "names-only"},   # Ps 63:6; Lam 2:19; names-only
    # ISBE compound; Num 32:3; Josh 13:27; Easton has nimrah.json
    "nimrah;-beth-nimrah":       {"status": "redirect-only", "redirect_to": "nimrah"},
    "nineveh-library-of":        {"status": "names-only"},   # ISBE; Ashurbanipal's cuneiform library; names-only
    "niphis":                    {"status": "names-only"},   # 1 Esd 5:21 variant; apocryphal
    # ISBE disambiguation; Gen 5:29; patriarch; Easton has noah.json
    "noah-1":                    {"status": "redirect-only", "redirect_to": "noah"},
    # ISBE disambiguation; Num 27:1; daughter of Zelophehad; Easton has noah.json
    "noah-2":                    {"status": "redirect-only", "redirect_to": "noah"},
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
    print(f'BPG Curation C57: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
