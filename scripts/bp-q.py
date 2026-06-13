"""
BP Article Synthesis — q: Quails → Quotations
Covers Easton entries: Quails through Quotations (10 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Category logic applied:
  - people:   Hitchcock match + no major place signals in brief
  - places:   brief/title contains 'city', 'town', 'sea of', 'river', 'mount', 'valley', etc.
  - concepts: no Hitchcock match, no place signals
  - names:    Hitchcock-only (no Easton/Smith entry exists)
  - events:   title is clearly an event (battle, feast, exile, flood, etc.)

Script: scripts/bp-q.py
Run: python3 scripts/bp-q.py
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
    "quails": {
        "id": "quails",
        "term": "Quails",
        "category": "concepts",
        "intro": "<p>Quails (Hebrew <em>selav</em>) appear in two episodes of miraculous provision in Israel's wilderness wandering. At Sinai, the people complained against Moses and Aaron that they had left the fleshpots of Egypt; that evening God sent quails that covered the camp (Exodus 16:13), giving the people meat alongside the manna he was beginning to provide. The second and more extensive quail miracle occurred at Kibroth-hattaavah when the mixed multitude craved meat: God sent a wind that drove quails from the sea and deposited them to a depth of two cubits for a day's journey around the camp (Numbers 11:31). The people gathered them greedily, but while the flesh was still between their teeth, God's anger burned against them for their craving and a great plague struck (Numbers 11:33) — giving Kibroth-hattaavah its name, <em>graves of craving</em>.</p><p>The quail miracles are commemorated in Psalm 78:27–31 as evidence of God's provision and of Israel's faithless ingratitude: he rained flesh on them \"like dust\" and yet they sinned still more. The Psalmist uses the episode as a typological warning about testing God. The common quail (<em>Coturnix coturnix</em>) migrates seasonally across the Sinai peninsula in vast flocks, making its appearance in the wilderness plausible as a natural phenomenon superintended providentially.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "quails", "smith": "quails", "isbe": "quails"},
        "key_refs": ["Exodus 16:13", "Numbers 11:31", "Psalms 78:27"]
    },
    "quarantania": {
        "id": "quarantania",
        "term": "Quarantania",
        "category": "places",
        "intro": "<p>Quarantania (from Latin <em>quaranta</em>, forty, referring to Christ's forty-day fast) is the traditional name for the mountain near Jericho identified as the site of Jesus's temptation, where the devil took him up and showed him all the kingdoms of the world (Matthew 4:8; Luke 4:5). The mountain, known in Arabic as Jebel Quruntul, rises steeply from the Jordan valley floor to approximately 1,200 feet above the plain, overlooking ancient Jericho. From its summit on a clear day the view extends across the Jordan valley and into Transjordan. A Greek Orthodox monastery carved into the cliff face of the mountain commemorates the forty days of Christ's temptation, and the site has been a pilgrimage destination since the early centuries of Christianity.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "quarantania"},
        "key_refs": ["Matthew 4:8", "Luke 4:5"]
    },
    "quarries": {
        "id": "quarries",
        "term": "Quarries",
        "category": "concepts",
        "intro": "<p>The word \"quarries\" in Judges 3:19, 26 (KJV) represents the Hebrew <em>pesilim</em>, more accurately rendered as <em>carved images</em> or <em>idols</em> in most modern translations — the same word used for graven images forbidden in the Decalogue. In the account of Ehud's assassination of Eglon king of Moab, Ehud turned back from the sculptured stones near Gilgal before delivering his message to the king. The site \"by Gilgal\" likely marked a stone monument or boundary marker of pagan religious significance. The older translation \"quarries\" arose from a misunderstanding of the Hebrew term as referring to stone-cutting sites rather than carved cultic objects.</p><p>In the building of Solomon's temple, actual stone quarrying is prominently featured: Solomon employed 80,000 stone-hewers in the mountains of Lebanon (1 Kings 5:15), and the stones were dressed at the quarry so that \"neither hammer nor axe nor any tool of iron was heard in the house\" during construction (1 Kings 6:7). The precision of ancient quarrying, especially the massive foundation stones of the temple mount, remains a subject of archaeological study.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "quarries", "smith": "quarries"},
        "key_refs": ["Judges 3:19", "1 Kings 5:17", "1 Kings 6:7"]
    },
    "quartus": {
        "id": "quartus",
        "term": "Quartus",
        "category": "people",
        "intro": "<p>Quartus (Latin meaning <em>fourth</em>) was a Christian at Corinth who sent greetings in Paul's letter to the Romans (Romans 16:23), described as \"a brother\" — indicating he was a member of the church known to Paul's Roman recipients. He is mentioned alongside Erastus the city treasurer of Corinth in the closing greetings of Romans, suggesting he was part of the Corinthian congregation. No other details about Quartus are preserved in Scripture. His Latin name suggests he may have been of Roman background, and his place in the greeting list indicates he was sufficiently well-connected to the Roman church to warrant a personal mention.</p>",
        "hitchcock_meaning": "fourth",
        "source_ids": {"easton": "quartus", "smith": "quartus"},
        "key_refs": ["Romans 16:23"]
    },
    "quaternion": {
        "id": "quaternion",
        "term": "Quaternion",
        "category": "concepts",
        "intro": "<p>A quaternion (Greek <em>tetradion</em>, meaning a group of four) was a squad of four Roman soldiers assigned as a guard unit. In Acts 12:4, Herod Agrippa I assigned four quaternions — sixteen soldiers in total — to guard the imprisoned Peter: four soldiers on duty at a time, rotating through four watches of the night. Peter was chained between two soldiers while two more stood watch at the doors (Acts 12:6). This heavily reinforced guard, ordered by a king who had just executed James the brother of John, underscores the miraculous nature of Peter's deliverance by an angel — the escape was humanly impossible against such vigilance. The quaternion reflects standard Roman military guard procedure for high-value prisoners.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "quaternion", "smith": "quaternion"},
        "key_refs": ["Acts 12:4"]
    },
    "queen": {
        "id": "queen",
        "term": "Queen",
        "category": "concepts",
        "intro": "<p>Queens in the Old Testament occupied a variety of roles. The queen consort was the wife of the king, but in Israelite practice the king's mother — the <em>gebirah</em> or queen mother — often held greater influence and formal status than the wives. Maachah (1 Kings 15:13) and Athaliah (2 Kings 11:1–20) illustrate the queen mother's power, and the queen mother held an official seat at court. The Psalms celebrate the queen consort in Psalm 45:9 standing at the king's right hand \"in gold of Ophir.\" In the New Testament, Jesus refers to the \"queen of the south\" — the Queen of Sheba — as a Gentile who came to hear Solomon's wisdom and who will rise in judgment against his unbelieving contemporaries (Matthew 12:42; Luke 11:31).</p><p>Foreign queens appear prominently in Scripture. Jezebel, the Phoenician queen of Ahab, wielded extensive power in Israel and became the archetype of pagan influence in a covenant kingdom (1 Kings 21; Revelation 2:20). Esther, though a queen by marriage in a foreign court, used her position to save her people. Song of Solomon 6:8 mentions sixty queens among those who praised the beloved, using royal imagery for the exalted status of the one whom the king loves above all.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "queen", "smith": "queen", "isbe": "queen"},
        "key_refs": ["Psalms 45:9", "1 Kings 15:13", "Matthew 12:42", "Song of Solomon 6:8"]
    },
    "queen-of-heaven": {
        "id": "queen-of-heaven",
        "term": "Queen of heaven",
        "category": "concepts",
        "intro": "<p>The Queen of Heaven (Hebrew <em>melekheth hashamayim</em>) was a pagan goddess worshipped by the women of Judah, to whom they made cakes, poured out drink offerings, and burned incense — practices Jeremiah condemned as provoking God to anger (Jeremiah 7:18; 44:17–25). The practice appears to have involved the whole household: children gathering wood, fathers kindling fire, and women kneading dough to make cakes \"to the queen of heaven.\" When Jeremiah rebuked these women after Jerusalem's fall, they defended their worship by arguing that the disasters had begun only when they stopped worshipping her (Jeremiah 44:17–18).</p><p>The Queen of Heaven is most commonly identified with the Mesopotamian goddess Ishtar (Astarte or Inanna), the goddess of love, fertility, and war, whose worship was widespread across the ancient Near East. Her cult represents the persistent attraction of the fertility religions that surrounded Israel throughout its history. The episode in Jeremiah reveals the depth of syncretistic practice in Judah immediately before and after the Babylonian conquest, and it stands as a lament over the spiritual blindness that contributed to the exile.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "queen-of-heaven", "smith": "queen-of-heaven", "isbe": "queen-of-heaven"},
        "key_refs": ["Jeremiah 7:18", "Jeremiah 44:17", "Jeremiah 44:25"]
    },
    "quicksands": {
        "id": "quicksands",
        "term": "Quicksands",
        "category": "places",
        "intro": "<p>The Quicksands (Greek <em>Syrtis</em>) were two large, treacherous sandbanks off the North African coast in the Gulf of Sidra (modern Libya), feared by ancient sailors for their shallow, shifting waters. Acts 27:17 records that when the ship carrying Paul from Caesarea to Rome was caught in the storm called Euroclydon (a violent northeastern wind), the sailors feared they would run aground on the Syrtis and took emergency measures — letting down the sea anchor and driving before the wind. The Syrtis Major and Syrtis Minor were legendary hazards in classical antiquity; Virgil, Horace, and other Roman writers used the Syrtis as a proverbial image of extreme danger. Paul's eventual shipwreck occurred at Malta rather than the Syrtis, fulfilling the angel's promise that all aboard would survive (Acts 27:24).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "quicksands", "smith": "quicksands"},
        "key_refs": ["Acts 27:17"]
    },
    "quiver": {
        "id": "quiver",
        "term": "Quiver",
        "category": "concepts",
        "intro": "<p>A quiver (Hebrew <em>ashpah</em> or <em>teli</em>) was a portable case — usually of leather, wood, or reed — used to carry arrows. In biblical usage the quiver appears both literally and metaphorically. As a military item, it was carried by archers in both Israelite and enemy armies (Isaiah 22:6; Jeremiah 5:16). The quiver of the LORD's servant is used as a metaphor in Isaiah 49:2, where the Servant of the LORD says God \"hid me in his quiver\" — suggesting a sharp instrument kept in reserve for the appointed hour.</p><p>The most theologically rich use is in Psalm 127:5: \"Happy is the man that hath his quiver full of them\" — where \"them\" refers to sons, compared in verse 4 to arrows in the hand of a mighty man. Children are described as a heritage from the LORD and a reward, and the man with many sons has strength at the city gate. Job 39:23 pictures the war-horse's quiver rattling against it as it rushes into battle, adding to the vivid description of the animal's fearlessness that forms part of God's answer from the whirlwind.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "quiver", "smith": "quiver"},
        "key_refs": ["Psalms 127:5", "Isaiah 49:2", "Job 39:23", "Jeremiah 5:16"]
    },
    "quotations": {
        "id": "quotations",
        "term": "Quotations",
        "category": "concepts",
        "intro": "<p>Quotations from the Old Testament in the New Testament number in the hundreds — by various counts, from 250 to over 600 direct citations and many more allusions — making the relationship between the two Testaments a defining feature of New Testament theology. The New Testament authors cite the Old Testament in Greek, primarily using the Septuagint (LXX) translation rather than the Hebrew Masoretic text, which accounts for some differences between their citations and the Hebrew original. The citation formulas vary: \"it is written\" (<em>gegraptai</em>), \"the Scripture says,\" \"as the prophet says,\" or \"David says in the Holy Spirit\" all indicate scriptural authority.</p><p>The New Testament's use of the Old Testament follows several hermeneutical patterns: direct fulfillment (a prophecy accomplished in Christ), typological fulfillment (an OT person or event prefigures a NT reality), analogical application (applying an OT principle to a NT situation), and summary allusion (evoking an OT theme without direct citation). Matthew's Gospel is the most concentrated in explicit fulfillment quotations, often introduced by \"that it might be fulfilled which was spoken by the prophet.\" Paul's Epistles make the densest use of OT citations for doctrinal argument, especially Romans, Galatians, and Hebrews. The study of NT quotation patterns is a major field of biblical scholarship, illuminating how the apostolic writers understood Christ as the interpretive key to all of Scripture.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "quotations", "isbe": "quotations"},
        "key_refs": ["Matthew 4:15", "Romans 11:2", "Hebrews 1:5", "1 Peter 2:6"]
    },
}


def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP q: Quails → Quotations: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
