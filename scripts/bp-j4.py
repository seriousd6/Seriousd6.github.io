"""
BP Article Synthesis — j4: Justice of God → Juttah
Covers Easton entries: Justice of God through Juttah (4 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Category logic applied:
  - people:   Hitchcock match + no major place signals in brief
  - places:   brief/title contains 'city', 'town', 'levitical', 'mount', 'valley', etc.
  - concepts: no Hitchcock match, no place signals

Script: scripts/bp-j4.py
Run: python3 scripts/bp-j4.py
"""

import json, os

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)


def load_article(slug):
    path = os.path.join(OUT_DIR, slug + '.json')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return None


def save_article(slug, data):
    path = os.path.join(OUT_DIR, slug + '.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def merge_article(slug, data):
    # Never overwrite an existing synthesis — idempotent safety
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True


ARTICLES = {
    "justice-of-god": {
        "id": "justice-of-god",
        "term": "Justice of God",
        "category": "concepts",
        "intro": "<p>Justice of God refers to that perfection of the divine nature by which God is infinitely righteous in himself and in all his dealings with his creatures—always acting in perfect conformity with what is right and rendering to every moral being exactly what is due. Scripture grounds God's justice in his very character: <em>righteousness and justice are the foundation of your throne</em> (Ps. 89:14), meaning that all God's acts of governance, judgment, and redemption flow from this essential attribute. God's justice expresses itself in his moral law, which reflects what he himself is, and in the sanctions attached to that law—rewards for obedience and punishment for transgression.</p><p>The justice of God operates alongside and in harmony with his other attributes, particularly his mercy and love. In the New Testament, the cross is the supreme demonstration that God is simultaneously <em>just and the justifier</em> of those who believe (Rom. 3:26): Christ's atoning death satisfies the demands of divine justice while opening the way for the justification of sinners. God's justice also sustains the Christian hope of final retribution—the crown of righteousness awaiting those who love Christ's appearing (2 Tim. 4:8) and the just recompense of those who persecuted his people (2 Thess. 1:6).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "justice-of-god"},
        "key_refs": ["Psalms 89:14", "Romans 3:26", "2 Timothy 4:8", "2 Thessalonians 1:6"]
    },
    "justification": {
        "id": "justification",
        "term": "Justification",
        "category": "concepts",
        "intro": "<p>Justification, in biblical theology, is a forensic or judicial act of God by which a sinner is declared righteous in his sight—not by infused righteousness that makes the person inwardly righteous, but by the imputation of Christ's righteousness credited to the believing sinner's account. As a legal term, it stands in direct opposition to condemnation: God pronounces the ungodly <em>not guilty</em> on the basis of what Christ has done on their behalf. The ground of justification is the obedience and atoning sacrifice of Christ; the instrument by which the individual receives it is faith alone (Rom. 5:1; 3:25–26; 4:6).</p><p>Paul's extended treatment in Romans and Galatians establishes that justification cannot be obtained by works of the law (Rom. 3:20; Gal. 2:16) and that Abraham himself was justified by faith before circumcision and before the Mosaic law existed (Rom. 4:1–11; Gal. 3:6–9). The righteousness credited to the believer is an <em>alien righteousness</em>—not their own but Christ's (2 Cor. 5:21; Phil. 3:9). James's complementary teaching (Jas. 2:21–24) addresses the public vindication or demonstration of faith through works, using <em>justification</em> in its common sense of <em>showing to be right</em>, without contradiction of Paul's forensic usage.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "justification", "isbe": "justification"},
        "key_refs": ["Romans 5:1", "Romans 3:25", "Romans 4:6", "2 Corinthians 5:21"]
    },
    "justus": {
        "id": "justus",
        "term": "Justus",
        "category": "people",
        "intro": "<p>Justus (Latin, meaning <em>just</em> or <em>upright</em>) is the name of three individuals in the New Testament. The first was Joseph Barsabas Justus, nominated alongside Matthias to fill the vacancy among the Twelve created by Judas Iscariot's death; when the lot fell on Matthias, Barsabas Justus disappears from the narrative (Acts 1:23–26). The second was Titius Justus (or Titus Justus), a God-fearing Gentile in Corinth whose house stood next door to the synagogue; after Jewish opposition forced Paul out of the synagogue, the apostle moved his teaching base to Justus's house, and many Corinthians believed and were baptized (Acts 18:7).</p><p>The third was Jesus Justus, a Jewish Christian in Rome who sent greetings to the Colossian church through Paul's letter (Col. 4:11). Paul identifies him, along with Aristarchus and Mark, as one of the few Jewish co-workers who had been <em>a comfort</em> to him during his imprisonment. The three occurrences of the name illustrate the Greco-Roman naming practice of adopting Latin cognomina expressing virtue, common among diaspora Jews and early Christians.</p>",
        "hitchcock_meaning": "just or upright",
        "source_ids": {"easton": "justus", "smith": "justus", "isbe": "justus"},
        "key_refs": ["Acts 1:23", "Acts 18:7", "Colossians 4:11"]
    },
    "juttah": {
        "id": "juttah",
        "term": "Juttah",
        "category": "places",
        "intro": "<p>Juttah (meaning <em>extended</em> or <em>turning away</em>) was a Levitical city in the hill-country of Judah, assigned to the priests among the descendants of Aaron (Josh. 15:55; 21:16). It was situated in the mountainous region south of Hebron, in the same district as Maon, Carmel, and Ziph. Some scholars have proposed identifying Juttah with the <em>city of Judah</em> mentioned in Luke 1:39 as the destination of Mary's visit to Elizabeth after the Annunciation—the city where Zechariah and Elizabeth lived and where John the Baptist was born.</p><p>If the Lukan identification is correct, Juttah would hold significant importance as the birthplace of John the Baptist and the location of the Visitation (Luke 1:39–56), during which Mary uttered the Magnificat. The site is tentatively identified with modern Yatta, a large village about five miles south of Hebron, which has preserved a phonetic echo of the ancient name throughout the centuries. As a priestly city, it was part of the system of forty-eight Levitical towns distributed throughout the tribal territories to ensure priestly presence across the land.</p>",
        "hitchcock_meaning": "turning away",
        "source_ids": {"easton": "juttah", "smith": "juttah"},
        "key_refs": ["Joshua 15:55", "Joshua 21:16", "Luke 1:39"]
    },
}


def main():
    written = 0
    skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP j4: Justice of God → Juttah: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
