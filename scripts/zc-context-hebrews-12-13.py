"""
MKT Context Commentary — Hebrews chapters 12–13
Run: python3 scripts/zc-context-hebrews-12-13.py

Key decisions:
- 12:1 athletic imagery: Greco-Roman athletic contests and their metaphorical use in ancient philosophy
- 12:5-11 divine discipline: Stoic paideia and Jewish disciplinary theology
- 12:18-29 Sinai vs. Zion: the phenomenological contrast between the two covenant theophany events
- 12:22 heavenly Jerusalem: apocalyptic heavenly city traditions
- 13:2 hospitality angels: the Abraham and Lot narratives as cultural background
- 13:5-6 contentment: Stoic/Cynic philosophy on freedom from desire
- 13:13 outside the camp: Jewish purity regulations and social exclusion
- 13:17 leaders: early church governance patterns
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(source, book):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(source, book, data):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

HEBREWS = {
  "12": {
    "1": '<p>The athletic contest metaphor (<em>agōn</em> = race/contest; <em>trechōmen</em> = let us run) was the most widely used metaphor in Hellenistic moral philosophy. The Stoics especially used athletic and military imagery for the philosophical life: Epictetus (Discourses 3.24.31-38) describes the philosopher as a contestant in the arena of life, and the goal of philosophy as winning the crown of virtue. The Cynics used the metaphor of the stripped-down athlete as the model for the philosopher who sets aside all unnecessary burdens. In Jewish contexts, 4 Maccabees (1st century CE) extensively uses the athletic contest as a metaphor for the martyrs\' endurance: the seven brothers are described as athletes whose training in the law prepared them for the ultimate contest (4 Macc 13:13-14; 17:11-16). Hebrews positions Jesus as both the example and the goal of the race — the pioneer and perfecter who has already run and won.</p>',
    "5": '<p>The theology of divine discipline (<em>paideia</em>) as fatherly instruction was developed in both Jewish and Greek traditions. In the Wisdom tradition (Prov 3:11-12, which Hebrews cites; Sir 18:13-14; Wis 11:10), God\'s discipline of the righteous is distinguished from punishment of the wicked: the same difficult events that punish the wicked test and form the righteous. The Stoic philosopher Seneca developed this theology extensively: "God is rough with those he loves" (On Providence 1.5); the suffering of the righteous is their training for virtue, as iron is refined by fire (On Providence 4.16). Philo of Alexandria interprets Abraham\'s trials as God\'s fatherly discipline of his adopted son (On Abraham 170-177). Hebrews situates the community\'s persecution and suffering within this widely shared theology of formative divine discipline.</p>',
    "18": '<p>The contrast between the Sinai theophany and the Zion assembly exploits the phenomenological difference between the two mountain events. Sinai (Exod 19-20) was characterized by sensory terror: fire, darkness, thunder, earthquake, the prohibition against approach, and the mediating distance that even Israel maintained (standing "at a distance," Exod 20:18-21). The rabbis debated why the Torah was given in the wilderness rather than in Israel — the answer being that the Torah belongs to all nations, not to any one territory; and that the wilderness experience of privation prepared the Israelites to receive it. The Sinai events were commemorated in the feast of Shavuot (Pentecost), which in the Second Temple period celebrated both the harvest and the Torah\'s giving. The new covenant Zion assembly (vv22-24) is not in the wilderness but already in the heavenly city — a contrast between journey and arrival, between terror and celebration.</p>',
    "22": '<p>The heavenly Jerusalem had become a developed concept in Jewish apocalyptic by the first century. 4 Ezra 7:26 describes the hidden city that will be revealed: "it shall be that the city which now is invisible shall appear, and the land which now is hidden shall be seen." 2 Baruch 4:2-7 preserves a tradition that the heavenly Jerusalem was shown to Adam before the Fall, to Abraham when God established the covenant, to Moses at Sinai, and is preserved in the divine presence until the end. The Revelation of John (chs. 21-22) describes the same heavenly Jerusalem descending to earth in the eschatological completion. Hebrews uniquely presents the community as having already "come to" (<em>proselelythate</em>, perfect tense) the heavenly city in the present — not merely anticipating it but participating in it through Christ\'s high-priestly ministry in the heavenly sanctuary.</p>',
    "28": '<p>The "unshakeable kingdom" (<em>basileian asaleuton</em>) in contrast to the shakeable creation reflects the eschatological distinction between the present age and the coming age. The Stoic philosophers also discussed cosmic destruction and renewal (<em>ekpyrōsis</em>: the periodic conflagration that destroys and renews the cosmos). Jewish apocalyptic — 4 Ezra 7:30-31, 2 Baruch 32:1-6 — describes the dissolution of the present world-order and the revelation of the eternal. Hebrews\' use of Haggai 2:6 interprets the eschatological shaking as already underway through the Christ-event, and the community as already recipients of the unshakeable kingdom that will survive the cosmic shaking. The "we are receiving" (<em>paralambanontes</em>) is a present tense: the reception is ongoing, not merely future.'
  },
  "13": {
    "2": '<p>Hospitality (<em>philoxenia</em>: love of the stranger) was a cardinal virtue in both Greco-Roman and Jewish culture. The Roman concept of <em>hospitium</em> (guest-friendship) created binding mutual obligations between host and guest that could extend across generations. In Jewish tradition, the obligation to welcome the stranger was grounded in the Exodus experience ("you were strangers in Egypt," Lev 19:34; Deut 10:19) and the covenant obligation to care for the vulnerable (the stranger, the widow, and the orphan appear together repeatedly in Deuteronomy). The Abraham and Lot narratives were celebrated as paradigmatic examples of hospitality (Philo, On Abraham 107-114; Josephus, Antiquities 1.196). In the early church, itinerant teachers, evangelists, and missionaries depended on the hospitality of local communities — the Didache (chs. 11-12) regulates this practice, distinguishing genuine apostles from false teachers who overstay their welcome.</p>',
    "5": '<p>The combination of contentment (<em>autarkeia</em>) with the scriptural promise of divine presence picks up the Stoic-Cynic philosophical tradition of freedom from desire as the foundation of happiness. Epictetus taught that contentment lay in aligning one\'s desires with what is within one\'s control (Discourses 1.1); Diogenes the Cynic embodied radical non-possession as philosophical freedom. Philo described the Essenes\' simple life as philosophical contentment (Hypothetica 11). Paul uses the same <em>autarkeia</em> terminology in Phil 4:11 ("I have learned in whatever state I am to be content"). Hebrews grounds the contentment not in philosophical achievement but in the divine promise: "I will never leave you nor forsake you" — making contentment a theological virtue (trust in God\'s provision) rather than a philosophical one (mastery of desire).</p>',
    "8": '<p>The statement that "Jesus Christ is the same yesterday and today and forever" was relevant against the background of theological novelty. The Hellenistic world was hospitable to new religious movements and new divine figures — there was a market for novel revelation in the first century (cf. Acts 17:21: "the Athenians and the foreigners who lived there spent their time in nothing except telling or hearing something new"). Within the Jewish-Christian community, there may have been teachers who were introducing new theological ideas about Jesus or modifying the received apostolic tradition. The unchangeableness of Jesus Christ is the theological warrant for holding fast to the received teaching rather than following the "strange teachings" (13:9) — doctrinal novelty about Christ is ruled out by Christ\'s own eternal constancy.</p>',
    "13": '<p>The call to go "outside the camp" and bear Jesus\'s reproach draws on the OT structure of purity that defined the camp and distinguished it from the outside. In Leviticus and Numbers, the camp of Israel was the holy space where God dwelt; those with skin diseases, discharges, or corpse-uncleanness were sent outside the camp (Lev 13:46; Num 5:2-3). The scapegoat was sent outside the camp into the wilderness (Lev 16:21-22); the animal carcasses of the sin-offerings were burned outside the camp (Lev 16:27). In first-century Jewish social terms, the "camp" was the synagogue community and its social protection; going "outside the camp" meant voluntary social exclusion from the Jewish community structure — losing the benefits of <em>religio licita</em> status and its protection from Roman requirements of emperor-worship. Hebrews calls the community to accept this social exposure as participation in Christ\'s own outside-the-gate exclusion.</p>',
    "17": '<p>"Obey your leaders and submit to them, for they are keeping watch over your souls, as those who will have to give an account" — the early church governance structure is briefly visible here. The "leaders" (<em>hēgoumenoi</em>) in Hebrews 13:7, 17, 24 (three uses) are distinguished from the apostles and appear to be the local community leaders — elders or overseers in the Pauline language (1 Tim 3:1-7; Titus 1:5-9; Acts 20:17-35). The language of "giving an account" reflects the pastor\'s responsibility as the community\'s shepherd: the Ezekiel 34 image of the shepherd accountable for the flock and the Matthew 25:14-30 image of the steward accountable for the master\'s goods both shape this responsibility. The Didache (chs. 15) instructs communities to elect bishops and deacons who will serve as their prophets and teachers.</p>'
  }
}

def main():
    existing = load_comm('mkt-context', 'hebrews')
    merge_comm(existing, HEBREWS)
    save_comm('mkt-context', 'hebrews', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Hebrews mkt-context: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
