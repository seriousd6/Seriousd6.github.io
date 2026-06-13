"""
BPG Curation — Batch C20: pharzites-the → shemidaites-the (gaps 1899–1998)
Gaps reviewed: 100 (score-10 smith-scholarly P–S range + concept-no-article)

Strong batch of NT epistle articles and concept stubs: Philemon, Philippians,
Plagues of Egypt, Purim, Proverbs (book), Revelation, Roman Empire, Ruth (book),
Cities of Refuge, Remorse, Responsibility, Revenge, Revivals, Rich (the), Scribes,
Self-Delusion, Selfishness, Lord of Sabaoth.
21 stub-needed; 16 redirects; 63 names-only.

Script: scripts/bpg-curate-20.py
Run: python3 scripts/bpg-curate-20.py  (from project root)
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
    # ── P entries ─────────────────────────────────────────────────────────────
    "pharzites.-the":       {"status": "names-only"},   # clan of Perez (Num 26:20); corrupted ID with period
    "phaseah":              {"status": "names-only"},   # temple servant family (Ezra 2:49)
    # Paul's letter to Philemon: Onesimus the runaway slave; "no longer as a slave but as a dear brother"
    # (Phlm 16); social implications for slavery; Paul's tactful appeal
    "philemon-the-epistle-of-paul-to": {"status": "stub-needed"},
    # Letter to Philippi: "rejoice in the Lord always" (Phil 4:4); Christ's kenosis (Phil 2:5-11);
    # "I can do all things through him who strengthens me" (Phil 4:13); "press on toward the goal" (Phil 3:14)
    "philippians-epistle-to-the": {"status": "stub-needed"},
    # Smith compound form for Phoenicia; redirect to canonical
    "phoenice-phoenicia":   {"status": "redirect-only", "redirect_to": "phoenicia"},
    # Smith variant spelling of Purim; redirect to main article (marked stub-needed below)
    "phurim":               {"status": "redirect-only", "redirect_to": "purim"},
    "phut-put":             {"status": "names-only"},   # son of Ham (Gen 10:6); African people (Libya/Somalia)
    "phygelus":             {"status": "names-only"},   # deserted Paul in Asia (2 Tim 1:15)
    "pilled":               {"status": "names-only"},   # KJV "peeled" (Gen 30:37-38); translation artifact
    "piltai-or-piltai":     {"status": "names-only"},   # priest (Neh 12:17)
    # "Plague" as divine epidemic judgment overlaps with "pestilence" (marked stub-needed in C10);
    # redirect to avoid duplicate article
    "plague-the":           {"status": "redirect-only", "redirect_to": "pestilence"},
    # Ten Plagues of Egypt (Exod 7-12): blood, frogs, gnats, flies, livestock, boils, hail,
    # locusts, darkness, firstborn; each plague confronts an Egyptian deity; Passover origin
    "plagues-the-ten":      {"status": "stub-needed"},
    "plains":               {"status": "names-only"},   # general geographic; individual plains have articles
    "possession":           {"status": "names-only"},   # too generic; demonic possession covered under "demoniacs"
    "potipherah-or-potipherah": {"status": "names-only"},  # priest of On; Joseph's father-in-law (Gen 41:45)
    # Field bought with Judas's 30 silver coins (Matt 27:3-10; Acts 1:18-19); called Akeldama
    # (Field of Blood in Aramaic); fulfills Zech 11:12-13 and Jer 18:2-3
    "potters-field-the":    {"status": "stub-needed"},
    "praltite-the":         {"status": "names-only"},   # likely "Paltite" epithet for Helez (2 Sam 23:26)
    "presents":             {"status": "names-only"},   # gift-giving; general cultural reference
    "prince-princess":      {"status": "names-only"},   # generic titles; individual princes have articles
    # "Do not boast about tomorrow, for you do not know what a day may bring" (Prov 27:1);
    # Rich Fool (Luke 12:16-21); "now is the acceptable time" (2 Cor 6:2); Jas 4:13-14
    "procrastination":      {"status": "stub-needed"},
    # Book of Proverbs: wisdom literature; "fear of the LORD is beginning of wisdom" (Prov 1:7);
    # Solomonic tradition; practical ethics; virtuous woman (Prov 31); personified Wisdom (Prov 8)
    "proverbs":             {"status": "stub-needed"},
    # Ptolemaic dynasty in Egypt: intertestamental context; Ptolemy I commissioned LXX in Alexandria;
    # Dan 11 "king of the south" wars; Alexander's successor kingdom significant for NT background
    "ptolemaeus-or-ptolemy": {"status": "stub-needed"},
    # Smith variant form of Ptolemaeus; redirect to combined article
    "ptolemee-or-ptolemeus": {"status": "redirect-only", "redirect_to": "ptolemaeus-or-ptolemy"},
    "pua":                  {"status": "names-only"},   # Hebrew midwife (Exod 1:15); Issachar's son (Gen 46:13)
    "puhites-the":          {"status": "names-only"},   # Kenite clan (1 Chr 2:53)
    "punites-the":          {"status": "names-only"},   # clan of Puvah/Puah (Num 26:23)
    # Feast of Purim (Esth 9:20-32): "pur" = lot; Haman's plot to destroy Jews; Mordecai and Esther;
    # deliverance celebrated annually on Adar 14-15; only biblical feast not commanded by Moses
    "purim":                {"status": "stub-needed"},
    "purosh":               {"status": "names-only"},   # variant of Parosh; returned-exile family (Ezra 2:3)

    # ── Q entries ─────────────────────────────────────────────────────────────
    "quicksands-the":       {"status": "names-only"},   # Syrtis sandbars (Acts 27:17 KJV); nautical detail

    # ── R entries ─────────────────────────────────────────────────────────────
    # Smith compound for Rabbah (capital of Ammon); David's siege; Joab; 2 Sam 12:26-31
    "rabbath-of-the-children-of-ammon": {"status": "redirect-only", "redirect_to": "rabbah"},
    "rabbathmoab":          {"status": "names-only"},   # capital of Moab variant; brief
    "rages":                {"status": "names-only"},   # Median city (Tobit 1:14); apocryphal only
    "raguel-or-reuel":      {"status": "names-only"},   # Jethro's alternate name (Exod 2:18); compound form
    # Greek NT spelling of Rahab (Matt 1:5 "Rachab"); redirect to canonical article
    "rahab-or-rachab":      {"status": "redirect-only", "redirect_to": "rahab"},
    "ramathite-the":        {"status": "names-only"},   # epithet for David's official (1 Chr 27:27)
    # Smith compound form for Rameses (city where Israel labored, Exod 1:11; 12:37)
    "rameses-or-raamses":   {"status": "redirect-only", "redirect_to": "rameses"},
    "rams-horns":           {"status": "names-only"},   # shofar; Jericho (Josh 6); covered under "trumpet"
    "rashness":             {"status": "names-only"},   # "slow to speak" (Jas 1:19); general wisdom theme
    "reaia":                {"status": "names-only"},   # temple servant family (Ezra 2:47 variant)
    "reasoning":            {"status": "names-only"},   # "let us reason together" (Isa 1:18); general
    # Greek/NT form of Rebekah used in Paul's argument (Rom 9:10); redirect to canonical
    "rebecca":              {"status": "redirect-only", "redirect_to": "rebekah"},
    # Cities of Refuge: six cities (Num 35:9-34; Deut 4:41-43; 19:1-13; Josh 20);
    # protection for accidental homicide; typologically prefigure Christ as our refuge
    "refuges-cities-of":    {"status": "stub-needed"},
    # "Godly sorrow produces repentance" (2 Cor 7:10); Judas's remorse led to death (Matt 27:3-5)
    # vs Peter's remorse led to restoration; OT examples: Saul, Esau
    "remorse":              {"status": "stub-needed"},
    "rending":              {"status": "names-only"},   # rending garments as mourning (Joel 2:13); cultural
    "rephaim-the-valley-of": {"status": "names-only"},  # valley near Jerusalem; Philistine battles (2 Sam 5:18)
    # "Each of us will give an account to God" (Rom 14:12); Ezek 18 individual accountability;
    # Luke 12:48 "from those given much, much will be required"; stewardship parables
    "responsibility":       {"status": "stub-needed"},
    # Book of Revelation: letters to seven churches; Lamb and scroll (Rev 5); seals, trumpets, bowls;
    # "Behold, I am coming soon" (Rev 22:12); New Jerusalem (Rev 21-22); authorship debates
    "revelation-of-st.-john": {"status": "stub-needed"},
    # "Vengeance is mine, I will repay, says the Lord" (Rom 12:19; Deut 32:35);
    # "do not repay evil with evil" (1 Pet 3:9); turning the other cheek (Matt 5:38-39)
    "revenge":              {"status": "stub-needed"},
    # OT reformations: Hezekiah (2 Chr 29-31), Josiah (2 Kgs 22-23), Ezra-Nehemiah;
    # Pentecost (Acts 2); "Will you not revive us again?" (Ps 85:6); NT awakening themes
    "revivals":             {"status": "stub-needed"},
    "ribai-or-ribai":       {"status": "names-only"},   # father of Ittai (2 Sam 23:29 variant)
    # "Woe to you who are rich" (Luke 6:24); rich young ruler (Matt 19:16-30); camel/needle (Matt 19:24);
    # parable of Rich Man and Lazarus (Luke 16:19-31); James on rich oppressors (Jas 5:1-6)
    "rich-the":             {"status": "stub-needed"},
    "riusah":               {"status": "names-only"},   # wilderness camp (Num 33:21-22 = Rissah)
    # NT political backdrop: Augustus's census; Tiberius during Jesus's ministry; Nero's persecution;
    # Rome in Daniel as the 4th empire; "submit to governing authorities" (Rom 13:1); Paul's citizenship
    "roman-empire":         {"status": "stub-needed"},
    "rubies":               {"status": "names-only"},   # precious stone; wisdom comparisons (Prov 3:15; 31:10)
    # Hosea's daughter name meaning; Lo-Ruhamah ("not pitied") and her restoration as Ruhamah;
    # redirect to the article on Lo-Ruhamah/Hosea's daughter
    "ruhamah-or-ruhamah":   {"status": "redirect-only", "redirect_to": "ruhamah"},
    # Book of Ruth: Ruth's loyalty (Ruth 1:16-17); kinsman-redeemer Boaz; harvest setting;
    # Davidic ancestry (Ruth 4:17-22); NT genealogy (Matt 1:5); model of hesed/loyal love
    "ruth-book-of":         {"status": "stub-needed"},

    # ── S entries ─────────────────────────────────────────────────────────────
    "sabachthani-or-sabachthani": {"status": "names-only"},  # Aramaic cry from cross (Matt 27:46); covered under crucifixion
    # "LORD of hosts" (Yahweh Sabaoth): Isa 1:9; 6:3; quoted in Rom 9:29 and Jas 5:4;
    # divine title emphasizing cosmic sovereignty; also NT "Lord Almighty" (2 Cor 6:18; Rev 4:8)
    "sabaoth-the-lord-of":  {"status": "stub-needed"},
    "sabbathdays-journey":  {"status": "names-only"},   # ~2000 cubits (Acts 1:12); Jewish travel limit
    "sabtecha-or-sabtechah": {"status": "names-only"},  # Cush's son (Gen 10:7); African people group
    "sala-or-salah":        {"status": "names-only"},   # ancestor of Abram (Gen 10:24 = Shelah)
    "salcah-or-salchah":    {"status": "names-only"},   # Bashan boundary town (Deut 3:10; Josh 13:11)
    # Smith compound for Salmon; redirect to canonical (ancestor of Boaz and Rahab; Matt 1:4-5)
    "salma-or-salmon":      {"status": "redirect-only", "redirect_to": "salmon"},
    # Salt Sea = Dead Sea (Num 34:3; Deut 3:17); Smith compound; redirect to main article
    "salt-sea-or-dead-sea": {"status": "redirect-only", "redirect_to": "dead-sea"},
    "salutations":          {"status": "names-only"},   # epistolary greetings; general cultural
    # Greek NT form of Sarah (1 Pet 3:6; Heb 11:11); redirect to canonical article
    "sara":                 {"status": "redirect-only", "redirect_to": "sarah"},
    "sarcasm":              {"status": "names-only"},   # Elijah mocking Baal (1 Kgs 18:27); literary device
    "sardites-the":         {"status": "names-only"},   # clan of Sered (Num 26:26)
    "schools":              {"status": "names-only"},   # schools of the prophets; general
    # "Scribes and Pharisees" (Matt 23); teachers of the law; professional copyists and interpreters;
    # Jesus in debate with scribes; scribe who was not far from kingdom (Mark 12:34)
    "scribe-s":             {"status": "stub-needed"},
    "sea-molten":           {"status": "names-only"},   # cast bronze Sea in temple (1 Kgs 7:23-26); architectural
    # Another form of Dead Sea/Salt Sea; redirect to same article
    "sea-the-salt":         {"status": "redirect-only", "redirect_to": "dead-sea"},
    "secacah-or-secacah":   {"status": "names-only"},   # Judah wilderness town (Josh 15:61)
    # Smith compound for Sela (Edomite rock city) and Selah (Psalm musical notation);
    # redirect to the Sela article (the city is the primary Smith entry)
    "sela-or-selah":        {"status": "redirect-only", "redirect_to": "sela"},
    # Smith compound for Seleucia (port of Syrian Antioch; Acts 13:4); redirect
    "seleucia-or-seleucia": {"status": "redirect-only", "redirect_to": "seleucia"},
    "seleucus-iv":          {"status": "names-only"},   # sent Heliodorus to plunder temple (2 Macc 3); apocryphal
    # "If anyone thinks he is something when he is nothing, he deceives himself" (Gal 6:3);
    # Laodicean church (Rev 3:17); "the heart is deceitful" (Jer 17:9); Prov 14:12
    "self-delusion":        {"status": "stub-needed"},
    # "Do nothing from selfish ambition or vain conceit" (Phil 2:3); "each look not only to his own
    # interests but to the interests of others" (Phil 2:4); Christ as model (Phil 2:5-8)
    "selfishness":          {"status": "stub-needed"},
    "semitic-languages":    {"status": "names-only"},   # linguistic category; too specialized at score-10
    # Smith compound for Sennacherib; redirect to canonical article
    "sennacherib-or-sennacherib": {"status": "redirect-only", "redirect_to": "sennacherib"},
    "sephela":              {"status": "names-only"},   # variant of Shephelah (Judah's lowland district)
    "shaalbim-or-shaalabbin": {"status": "names-only"}, # Dan town (Josh 19:42 variant)
    "shaalbonite-the":      {"status": "names-only"},   # epithet for David's warrior Eliahba (2 Sam 23:32)
    "shaasgaz":             {"status": "names-only"},   # eunuch over second harem (Esth 2:14)
    "shaharaim":            {"status": "names-only"},   # Benjaminite (1 Chr 8:8)
    "shahazimah":           {"status": "names-only"},   # Issachar town (Josh 19:22)
    "shalim-the-land-of":   {"status": "names-only"},   # region Saul passed through (1 Sam 9:4)
    "shalisha-the-land-of": {"status": "names-only"},   # region Saul searched for donkeys (1 Sam 9:4)
    "shallecheth":          {"status": "names-only"},   # western temple gate (1 Chr 26:16)
    "shaveh-kiriathaim":    {"status": "names-only"},   # battlefield where Chedorlaomer defeated Emites (Gen 14:5)
    "shawm":                {"status": "names-only"},   # KJV wind instrument (Ps 98:6 variant); general
    "shearinghouse-the":    {"status": "names-only"},   # Jehu killed Ahaziah's relatives here (2 Kgs 10:12-14)
    "shebuel-or-shebuel":   {"status": "names-only"},   # two Levites (1 Chr 23:16; 25:4 = Shubael)
    "shechaniah":           {"status": "names-only"},   # several OT figures (1 Chr 3:21-22; Ezra 8:3; 10:2)
    "shechemites-the":      {"status": "names-only"},   # clan of Shechem (Num 26:31)
    "sheepgate-the":        {"status": "names-only"},   # Jerusalem gate (Neh 3:1,32); pool of Bethesda nearby
    "sheepmarket-the":      {"status": "names-only"},   # Jerusalem market; brief reference
    "shelanites-the":       {"status": "names-only"},   # clan of Shelah (Num 26:20)
    "shemidah":             {"status": "names-only"},   # variant of Shemida (Num 26:32)
    "shemidaites-the":      {"status": "names-only"},   # clan of Shemida (Num 26:32)
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
    print(f'BPG Curation C20: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
