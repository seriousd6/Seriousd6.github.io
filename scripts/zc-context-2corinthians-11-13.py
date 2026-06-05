"""
mkt-context layer — 2 Corinthians all 13 chapters
Output: data/commentary/mkt-context/2corinthians.json

2 Corinthians is written ca. 54-57 CE after a painful visit and an
intermediate letter (now lost). The 'super-apostles' (11:5; 12:11) are
likely Hellenistic Jewish missionaries with letters of recommendation
who competed with Paul on Greco-Roman rhetorical and wonder-worker grounds.
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
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

CONTEXT = {
  "1": {
    "8": "<p>The affliction Paul suffered in Asia (v. 8: we were so utterly burdened beyond our strength that we despaired of life itself) is unspecified — candidates include: a near-fatal illness (cf. Gal 4:13-14), violent persecution at Ephesus (cf. 1 Cor 15:32 'I fought with beasts'), or the riot of Acts 19. Paul's <em>sentence of death</em> (<em>apokrima tou thanatou</em>) is a judicial term — either the experience felt like a death verdict or he received an actual legal condemnation. Whatever the event, it produced the pneumatological outcome Paul describes: reliance on the God who raises the dead (v. 9), the experiential foundation of 2 Corinthians' theology of resurrection-through-suffering.</p>"
  },
  "3": {
    "1": "<p>Letters of recommendation (<em>systatikaí epistolai</em>, 3:1) were a standard social institution in the ancient Mediterranean world: a prominent person would write a letter attesting to the character, status, and worthiness of a traveling associate. Cicero wrote dozens (Ad Atticum; Ad Familiares); papyri preserve examples from Egyptian commerce. Paul's opponents brought such letters to Corinth, establishing their credentials through social networks Paul lacked or scorned. Paul's counterargument: the Corinthians themselves are his letter of recommendation — written on hearts by the Spirit, readable by everyone. The apostolic community is the authenticating credential for genuine ministry.</p>",

    "7": "<p>The contrast between the 'ministry of death, carved in letters on stone' (<em>diakonia tou thanatou en grammasin entetypōmenē lithois</em>) and the 'ministry of the Spirit' reflects Paul's understanding of Sinai. The Mosaic covenant was glorious — Moses's face shone (Exod 34:29-35); the Israelites could not look at it. But that glory was transient (<em>katargoumene</em>, passing away, v. 7). Paul's argument uses a <em>qal vahomer</em> (lesser to greater) rabbinic form: if the lesser (Mosaic) had glory, the greater (Spirit-ministry) surpasses it immeasurably. This is not anti-Torah polemic (Paul quotes Torah approvingly throughout 2 Corinthians) but a salvation-historical ordering.</p>"
  },
  "5": {
    "10": "<p>The judgment seat of Christ (<em>bema tou Christou</em>, v. 10): the <em>bema</em> was the elevated platform in a Roman city center where the magistrate or proconsul rendered judgments — Gallio sat on the Corinthian <em>bema</em> when Jews dragged Paul before him (Acts 18:12). Paul transforms this civic institution into an eschatological reality: each person will appear before Christ's <em>bema</em> to receive what is due for what was done in the body, whether good or evil. This is not justification-reversal (Paul consistently teaches no condemnation for those in Christ, Rom 8:1) but an accounting of stewardship — the believer's life-work is evaluated by the risen judge.</p>"
  },
  "8": {
    "1": "<p>The collection for the Jerusalem poor (chs. 8-9) was Paul's major trans-community project ca. 52-57 CE, coordinating Gentile churches (Galatia, Macedonia, Achaia, Asia) to send material aid to impoverished believers in Jerusalem. Paul speaks of it in Rom 15:25-27 as a theological act: Gentiles share in Jews' spiritual blessings; it is right to share material resources in return. The political dimension: the collection demonstrates to Jerusalem that Gentile churches are genuine members of the same body, potentially addressing the ongoing Jewish-Gentile tension that produced the Jerusalem Council controversy (Acts 15). Josephus (Ant. 20.51-53) documents chronic food shortage and famine in Judea in this period.</p>"
  },
  "10": {
    "1": "<p>Paul's opponents apparently criticized him for being 'humble when face to face with you, but bold toward you when I am away' (v. 1) — i.e., his letters are severe but his personal presence is weak (<em>asthenes</em>, v. 10) and his speech contemptible (<em>ho logos exouthenemos</em>). This reflects Greco-Roman rhetorical values: a true philosopher-orator should have a physically impressive presence and oratorical power (the Sophistic tradition). Paul's physical weakness, possible speech defect (Gal 4:13-14 hints at illness), and refusal to use the Sophists' professional rhetorical techniques made him vulnerable to dismissal. His defense: the weapons of his warfare are not of the flesh (v. 4) — apostolic authority is not measured by Sophistic standards.</p>"
  },
  "11": {
    "22": "<p>Paul's Israelite identity catalogue (v. 22: Hebrews, Israelites, offspring of Abraham) mirrors the probable claims of the 'super-apostles'. 'Hebrews' (<em>Hebraioi</em>) may indicate Aramaic-speaking Jews of Palestinian origin (cf. Acts 6:1); 'Israelites' emphasizes covenant membership; 'offspring of Abraham' likely points to messianic expectations rooted in the Abrahamic promise. Paul matches their credentials item by item — but his rebuttal is that his list of sufferings (vv. 23-33), not his ethnic credentials, authenticates his apostleship. The most extensive catalogue of apostolic hardship in the NT: five floggings, three beatings, stoning, three shipwrecks, dangers from rivers, robbers, compatriots, Gentiles, wilderness, sea, false brothers.</p>"
  },
  "12": {
    "2": "<p>The man caught up to the third heaven / Paradise (vv. 2-4): Paul's apocalyptic-vision tradition belongs to the well-documented Second Temple Jewish literature of heavenly ascent — 1 Enoch, 2 Enoch, 3 Baruch, T. Levi, and later the Hekhalot literature describe journeys through multiple heavens (three, five, or seven, depending on the source). The rabbinic concept of <em>pardes</em> (paradise) as the garden of God in the highest heaven (b. Hagigah 14b — the four who entered pardes) provides context. Paul's reticence (he cannot tell whether in the body or out of the body, vv. 2-3; he refuses to boast about it, v. 5) is the inverse of the typical apocalyptic visionary who boasts of his heavenly journey.</p>"
  }
}

def main():
    existing = load_comm('mkt-context', '2corinthians')
    merge_comm(existing, CONTEXT)
    save_comm('mkt-context', '2corinthians', existing)
    total = sum(len(v) for v in existing.values())
    print(f'2 Corinthians mkt-context: {len(existing)} chapters, {total} verses.')

if __name__ == '__main__':
    main()
