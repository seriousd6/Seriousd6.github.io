"""
BPG Curation — Batch C51: joannes → kenosis (gaps 5099–5198)
Gaps reviewed: 100 (score-5 isbe-scholarly J–K entries — Joel/John/Jonah/Jonathan/Jordan/
Joseph/Joshua/Jubilee/Judah/Judgment compound articles, apocryphal J names,
Kenaz, and K entries through kenosis)

Heavy redirect batch: major biblical figures and books appear as ISBE disambiguation
pairs (joel-1/2, john-1/2, jonathan-1/2, joseph-1/2, joshua-1/2/3) and compound
articles (jordan-valley, jubilee-year/cycle, judah territory/at-jordan, judith-book-of,
jude-the-epistle-of, judgment-day/last, jupiter-and-mercury). All redirect to canonical
Easton articles. Apocryphal entries (josaphias, jonathas, joribus, josabdus, etc.) names-only.
0 stub-needed; 28 redirects; 72 names-only.

Script: scripts/bpg-curate-51.py
Run: python3 scripts/bpg-curate-51.py  (from project root)
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
    "joannes":                   {"status": "names-only"},   # apocryphal/variant form of John; 1 Macc 2:2; names-only
    "joarib":                    {"status": "names-only"},   # variant of Joiarib; 1 Chr 9:10; Neh 11:10; names-only
    "joash-1":                   {"status": "names-only"},   # ISBE disambiguation; 2 Kgs 11-12 king of Judah; names-only
    "joash-2":                   {"status": "names-only"},   # ISBE disambiguation; 2 Kgs 13-14 king of Israel; names-only
    "job-testament-of":          {"status": "names-only"},   # pseudepigraphal; apocryphal; extracanonical
    "jod":                       {"status": "names-only"},   # Hebrew letter (10th); Ps 119:73-80; lexical
    # ISBE disambiguation; Joel son of Pethuel; Easton has joel.json
    "joel-1":                    {"status": "redirect-only", "redirect_to": "joel"},
    # ISBE disambiguation; Joel = Samuel's son (1 Sam 8:2); Easton has joel.json
    "joel-2":                    {"status": "redirect-only", "redirect_to": "joel"},
    "johannes":                  {"status": "names-only"},   # Latin/German form of John; variant; names-only
    "johannine-theology":        {"status": "names-only"},   # ISBE scholarly; score-5 → names-only
    # ISBE disambiguation; John the Apostle; Easton has john.json
    "john-1":                    {"status": "redirect-only", "redirect_to": "john"},
    # ISBE disambiguation; another John; Easton has john.json
    "john-2":                    {"status": "redirect-only", "redirect_to": "john"},
    "john-mark":                 {"status": "names-only"},   # Acts 12:12,25; covered under John or Mark in Easton
    "john-the-epistles-of":      {"status": "names-only"},   # ISBE umbrella; no single Easton slug covers all 3 epistles
    "john-the-revelation-of":    {"status": "names-only"},   # ISBE; no dedicated Easton "revelation" article
    "join":                      {"status": "names-only"},   # lexical
    # ISBE compound; Easton has jonah-book-of.json
    "jonah-the-book-of":         {"status": "redirect-only", "redirect_to": "jonah-book-of"},
    # ISBE disambiguation; Greek form of Jonah; Easton has jonah.json
    "jonas-1":                   {"status": "redirect-only", "redirect_to": "jonah"},
    "jonas-2":                   {"status": "names-only"},   # John 21:15-17 "Simon son of Jonas" = Simon's father; brief
    "jonath-elem-rehokim":       {"status": "names-only"},   # Ps 56 superscription; liturgical/musical; names-only
    # ISBE disambiguation; 1 Sam 14:1; Saul's son; Easton has jonathan.json
    "jonathan-1":                {"status": "redirect-only", "redirect_to": "jonathan"},
    # ISBE disambiguation; other Jonathans; Easton has jonathan.json
    "jonathan-2":                {"status": "redirect-only", "redirect_to": "jonathan"},
    "jonathas":                  {"status": "names-only"},   # Greek/apocryphal form of Jonathan (1 Macc 2:5); names-only
    # ISBE compound; Easton has jordan.json
    "jordan-valley":             {"status": "redirect-only", "redirect_to": "jordan"},
    "joribus":                   {"status": "names-only"},   # 1 Esd 8:43 variant; apocryphal
    "jorkeam":                   {"status": "names-only"},   # 1 Chr 2:44; minor Judah place/person
    "josabdus":                  {"status": "names-only"},   # 1 Esd 9:48 variant; apocryphal
    "josaphias":                 {"status": "names-only"},   # 1 Esd 8:36 variant; apocryphal
    "josedech;-josedek":         {"status": "names-only"},   # ISBE compound; Hag 1:1; Ezra 3:2; Jeshua's father; minor
    # ISBE disambiguation; Gen 30:24; patriarch; Easton has joseph.json
    "joseph-1":                  {"status": "redirect-only", "redirect_to": "joseph"},
    # ISBE disambiguation; Luke 3:23 Jesus' father; Easton has joseph.json
    "joseph-2":                  {"status": "redirect-only", "redirect_to": "joseph"},
    "joseph-barnabas":           {"status": "names-only"},   # Acts 4:36; birth name of Barnabas; covered under Barnabas
    "joseph-barsabbas":          {"status": "names-only"},   # Acts 1:23; not chosen apostle; minor figure
    "joseph-of-arimathaea":      {"status": "names-only"},   # Matt 27:57-60; covered under Arimathea in Easton
    "josephs-dream":             {"status": "names-only"},   # Gen 37:5-11; covered under Joseph/dreams
    # ISBE; Matt 1:16-24; Easton has joseph.json
    "joseph-husband-of-mary":    {"status": "redirect-only", "redirect_to": "joseph"},
    "joseph-prayer-of":          {"status": "names-only"},   # pseudepigraphal; apocryphal; extracanonical
    "joseph-the-carpenter-gospel-of": {"status": "names-only"},  # apocryphal gospel; extracanonical
    "josephus":                  {"status": "names-only"},   # Jewish historian Flavius Josephus; scholarly; score-5
    "josephus;-flavius":         {"status": "names-only"},   # ISBE compound; same as josephus; duplicate entry
    "josheb-basshebeth":         {"status": "names-only"},   # 2 Sam 23:8; David's chief mighty man; names-only
    "joshibiah":                 {"status": "names-only"},   # 1 Chr 4:35; minor Simeonite figure
    # ISBE disambiguation; Num 13:16; military leader; Easton has joshua.json
    "joshua-1":                  {"status": "redirect-only", "redirect_to": "joshua"},
    # ISBE disambiguation; Neh 8:17 reference; Easton has joshua.json
    "joshua-2":                  {"status": "redirect-only", "redirect_to": "joshua"},
    # ISBE disambiguation; 1 Sam 6:14 Bethshemite; Easton has joshua.json
    "joshua-3":                  {"status": "redirect-only", "redirect_to": "joshua"},
    "jotapata":                  {"status": "names-only"},   # Josephus' stronghold; Jewish War; historical
    "jotbathah":                 {"status": "names-only"},   # Num 33:33-34; wilderness camp; minor place
    "joy":                       {"status": "names-only"},   # Gal 5:22; Ps 16:11; no dedicated Easton article
    "jozabdus":                  {"status": "names-only"},   # 1 Esd 9:29 variant; apocryphal
    "jozacar":                   {"status": "names-only"},   # 2 Kgs 12:21; assassin of Joash; minor figure
    # Lev 25; Year of Jubilee; Easton has jubilee.json
    "jubilee-year":              {"status": "redirect-only", "redirect_to": "jubilee"},
    # ISBE; Metonic/Jubilee cycle; Easton has jubilee.json
    "jubilee-cycle-of-the":      {"status": "redirect-only", "redirect_to": "jubilee"},
    "jubilees-book-of":          {"status": "names-only"},   # pseudepigraphal; apocryphal; extracanonical
    # ISBE; Matt 3:1 "wilderness of Judaea"; Easton has judea.json
    "judaea-wilderness-of":      {"status": "redirect-only", "redirect_to": "judea"},
    # ISBE disambiguation; Gen 29:35; Leah's son; Easton has judah.json
    "judah-1":                   {"status": "redirect-only", "redirect_to": "judah"},
    # ISBE disambiguation; Neh 11:9; minor figure; Easton has judah.json
    "judah-2":                   {"status": "redirect-only", "redirect_to": "judah"},
    # ISBE; Josh 19:34; Easton has judah-upon-jordan.json
    "judah-at-upon-the-jordan":  {"status": "redirect-only", "redirect_to": "judah-upon-jordan"},
    # ISBE; tribe territory; Easton has judah.json
    "judah-territory-of":        {"status": "redirect-only", "redirect_to": "judah"},
    "judaism":                   {"status": "names-only"},   # ISBE; Jewish religious system; scholarly; score-5
    "judas-barsabbas":           {"status": "names-only"},   # Acts 15:22; companion at Jerusalem Council; minor figure
    "judas-iscariot-gospel-of":  {"status": "names-only"},   # Gnostic apocryphal gospel; extracanonical
    "judas-of-damascus":         {"status": "names-only"},   # Acts 9:11; Saul's host in Damascus; minor figure
    "judas-of-james":            {"status": "names-only"},   # Luke 6:16; Acts 1:13; apostle; covered under Jude/apostles
    "judas-juda":                {"status": "names-only"},   # ISBE compound; names-only (Judas Iscariot variant)
    "judas-not-iscariot":        {"status": "names-only"},   # John 14:22; same as Judas of James; names-only
    "juddah":                    {"status": "names-only"},   # 1 Esd 9:26 variant; apocryphal
    # ISBE; Easton has jude-epistle-of.json
    "jude-the-epistle-of":       {"status": "redirect-only", "redirect_to": "jude-epistle-of"},
    "judges-period-of":          {"status": "names-only"},   # ISBE; historical period; names-only (≠ judges-book-of.json)
    "judging-judgment":          {"status": "names-only"},   # ISBE compound; general; covered under judgments-of-god.json
    # ISBE; Matt 12:36; Rev 20:11-15; Easton has judgment-the-final.json
    "judgment-day-of":           {"status": "redirect-only", "redirect_to": "judgment-the-final"},
    # ISBE; same concept; Easton has judgment-the-final.json
    "judgment-last":             {"status": "redirect-only", "redirect_to": "judgment-the-final"},
    "judicial-blindness":        {"status": "names-only"},   # John 12:40; Rom 11:8; divine hardening; names-only
    "judicial-courts":           {"status": "names-only"},   # ISBE; covered under judges/courts in Easton
    "judicial-hardening":        {"status": "names-only"},   # same concept as judicial-blindness; names-only
    # ISBE; Easton has judith.json
    "judith-book-of":            {"status": "redirect-only", "redirect_to": "judith"},
    "juel":                      {"status": "names-only"},   # 1 Esd 8:38 variant; apocryphal
    "jugglery":                  {"status": "names-only"},   # Dan 2:2; KJV "magicians"; lexical
    "juice":                     {"status": "names-only"},   # Song 8:2; Isa 65:8; lexical
    "jumping":                   {"status": "names-only"},   # Nah 3:2 KJV; lexical
    "junias;-junla":             {"status": "names-only"},   # ISBE compound; Rom 16:7 Junia; names-only
    # ISBE compound; Acts 14:12; Easton has jupiter.json
    "jupiter-and-mercury":       {"status": "redirect-only", "redirect_to": "jupiter"},
    "jurisdiction":              {"status": "names-only"},   # Luke 23:7; lexical
    "justle":                    {"status": "names-only"},   # KJV archaic "jostle" (Nah 2:4); lexical
    "juttah;-jutah":             {"status": "names-only"},   # ISBE compound; Josh 15:55; 21:16; priestly city; minor
    "kab":                       {"status": "names-only"},   # 2 Kgs 6:25 KJV "cab" = dry measure; lexical
    "kadesh-in-galilee":         {"status": "names-only"},   # Josh 20:7; city of refuge; minor place
    "kadesh-on-the-orontes":     {"status": "names-only"},   # Egyptian-Hittite battle site; historical; names-only
    "kadmonite":                 {"status": "names-only"},   # Gen 15:19; Canaanite tribal name; minor
    "kain-1":                    {"status": "names-only"},   # ISBE disambiguation; Judg 4:11 Kenite; minor
    "kain-2":                    {"status": "names-only"},   # ISBE disambiguation; Josh 15:57 Judah town; minor
    "kamon":                     {"status": "names-only"},   # Judg 10:5; burial site of Jair; minor place
    "kaph":                      {"status": "names-only"},   # Hebrew letter (11th); Ps 119:81-88; lexical
    "kariathiarius":             {"status": "names-only"},   # 1 Esd 5:19 variant of Kirjath-arim; apocryphal
    "karka":                     {"status": "names-only"},   # Josh 15:3; Judah southern boundary; minor place
    "kedesh-1":                  {"status": "names-only"},   # ISBE disambiguation; Josh 15:23 Judah town; minor
    "kedesh-2":                  {"status": "names-only"},   # ISBE disambiguation; Josh 12:22; Naphtali city; minor
    "kedesh-naphtali":           {"status": "names-only"},   # Josh 20:7; city of refuge; no dedicated Easton slug
    "keeper;-keepers":           {"status": "names-only"},   # ISBE compound; Ps 121:5 "keeper of Israel"; lexical
    # ISBE compound; Gen 15:19; 36:11; Easton has kenaz.json
    "kenaz;-kenez":              {"status": "redirect-only", "redirect_to": "kenaz"},
    "kenosis":                   {"status": "names-only"},   # ISBE; Phil 2:7 Christological "emptying"; scholarly; score-5
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
    print(f'BPG Curation C51: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
