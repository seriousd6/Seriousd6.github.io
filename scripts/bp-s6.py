"""
BP Article Synthesis — s6: Sychem → Syrophenician
Covers Easton entries: Sychem through Syrophenician (8 entries)

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

Script: scripts/bp-s6.py
Run: python3 scripts/bp-s6.py
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
    "sychem": {
        "id": "sychem",
        "term": "Sychem",
        "category": "places",
        "intro": "<p>Sychem is the Greek transliteration of Shechem, appearing once in the New Testament in Stephen's speech before the Sanhedrin (Acts 7:16), where he refers to the tomb at Sychem purchased by Abraham from the sons of Emmor. The site corresponds to ancient Shechem in the central highlands of Canaan, located in the valley between Mount Ebal and Mount Gerizim. It was one of the most significant cities in Israelite history — the place where God first appeared to Abram after he entered Canaan (Genesis 12:6), where Joshua renewed the covenant with Israel before his death (Joshua 24), and where the kingdom divided under Rehoboam (1 Kings 12). The Greek form Sychem was used by the Septuagint translators and carried over into the New Testament's citations of earlier Israelite history.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sychem", "smith": "sychem", "isbe": "sychem"},
        "key_refs": ["Acts 7:16", "Genesis 12:6", "Joshua 24:32"]
    },
    "syene": {
        "id": "syene",
        "term": "Syene",
        "category": "places",
        "intro": "<p>Syene (Hebrew <em>Seveneh</em>, meaning \"opening\" or possibly related to trade routes) was a frontier town of Egypt on the southern border with Ethiopia (Cush), situated on the eastern bank of the Nile at the first cataract. It corresponds to modern Aswan, one of Egypt's most southerly cities. Syene is mentioned twice in Ezekiel's prophecies against Egypt: God declares that Egypt shall be laid waste \"from the tower of Syene even unto the border of Ethiopia\" (Ezekiel 29:10; 30:6), using the phrase as a merism expressing the full length of the land from north to south. The region was famed in antiquity for its red granite quarries, from which the Egyptians cut obelisks and colossal statues; the granite is still called <em>Syenite</em> after the ancient city. Syene also marked the point where ancient geographers noted the sun's rays fell directly vertical at the summer solstice, a fact used by Eratosthenes in the third century BC to calculate the circumference of the earth.</p>",
        "hitchcock_meaning": "a bush; enmity",
        "source_ids": {"easton": "syene", "smith": "syene", "isbe": "syene"},
        "key_refs": ["Ezekiel 29:10", "Ezekiel 30:6"]
    },
    "synagogue": {
        "id": "synagogue",
        "term": "Synagogue",
        "category": "concepts",
        "intro": "<p>The synagogue (Greek <em>sunagoge</em>, \"assembly\") was the central institution of Jewish communal worship, Torah study, and legal assembly from the Second Temple period onward. The origins of the synagogue are uncertain but are commonly traced to the Babylonian exile (sixth century BC), when Jews living away from the destroyed temple required a place for prayer and scripture reading. By the first century AD, synagogues were found throughout the Jewish diaspora and in every significant town in Palestine — Jesus regularly taught in them (Luke 4:16–21), and Paul consistently entered local synagogues as his first point of contact in new cities (Acts 13:5, 14; 17:1–2). The word appears in the Old Testament only once (Psalm 74:8, where KJV translates the Hebrew <em>mo'adey-el</em>), though the institution is reflected in Ezekiel's gatherings of elders. The synagogue service centered on the reading and exposition of the Torah, prayer, and the Shema; it was led by a ruler of the synagogue (<em>archisynagogos</em>) and an attendant (<em>chazzan</em>). The early church modeled many of its assembly practices on the synagogue pattern.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "synagogue", "smith": "synagogue", "isbe": "synagogue"},
        "key_refs": ["Psalms 74:8", "Luke 4:16", "Acts 13:14", "Acts 17:2"]
    },
    "syntyche": {
        "id": "syntyche",
        "term": "Syntyche",
        "category": "people",
        "intro": "<p>Syntyche (Greek, meaning \"fortunate\" or \"one who converses\") was a female member of the church at Philippi whom Paul addresses by name in his letter to that congregation (Philippians 4:2–3). Paul appeals to both Syntyche and her fellow church member Euodia to \"be of the same mind in the Lord,\" indicating that a personal dispute between the two women had become serious enough to require apostolic intervention. Paul also calls on a third party — an unnamed \"true yokefellow\" — to help reconcile them. He identifies both women as those who \"labored with me in the gospel,\" placing them among the active co-workers in Paul's missionary work at Philippi. Beyond this passage nothing further is known of Syntyche. The episode illuminates the tensions that could arise within early house churches and Paul's pastoral practice of naming and directly addressing those involved.</p>",
        "hitchcock_meaning": "that speaks or discourses",
        "source_ids": {"easton": "syntyche", "smith": "syntyche", "isbe": "syntyche"},
        "key_refs": ["Philippians 4:2", "Philippians 4:3"]
    },
    "syracuse": {
        "id": "syracuse",
        "term": "Syracuse",
        "category": "places",
        "intro": "<p>Syracuse was the principal city of Sicily, situated on the south-eastern coast of the island, and one of the most celebrated cities of the ancient Greek world. Founded by Corinthian colonists in 734 BC, it grew to become the largest Greek city outside Greece itself, renowned for its wealth, culture, and fortifications. The city appears in the New Testament in Acts 28:12, where Paul's ship from Malta put in at Syracuse and remained three days during his voyage to Rome. The brief stop gave Paul contact with one of the Mediterranean world's great urban centers. Syracuse had successfully resisted the Athenian expedition of 415–413 BC in one of antiquity's most dramatic military reverses, and under Dionysius I and II it had been a major Mediterranean power. By Paul's time it was a prosperous Roman provincial city and served as a regular stopping point on the grain routes between Alexandria and Rome.</p>",
        "hitchcock_meaning": "that draws violently",
        "source_ids": {"easton": "syracuse", "smith": "syracuse", "isbe": "syracuse"},
        "key_refs": ["Acts 28:12"]
    },
    "syria": {
        "id": "syria",
        "term": "Syria",
        "category": "places",
        "intro": "<p>Syria (Hebrew <em>Aram</em>) was the name applied in the Old Testament to the broad region lying north and north-east of Israel, bounded roughly by the Taurus Mountains to the north, the Euphrates to the east, the desert to the south, and Phoenicia to the west. Its principal cities were Damascus, Aleppo (Hamath), and Zobah. The Syrians (Arameans) were frequently in conflict with Israel: David subdued Damascus and Zobah (2 Samuel 8:5–6), but Syria became a persistent thorn in the side of the northern kingdom, particularly under Ben-hadad I, Ben-hadad II, and Hazael, who \"smote them in all the coasts of Israel\" (2 Kings 10:32). The prophet Amos pronounced judgment on Damascus for its atrocities against Gilead (Amos 1:3–5), and Isaiah foretold the fall of Damascus (Isaiah 17). In the New Testament era, Syria was a Roman imperial province with Antioch as its capital — a city that became the base of Paul's missionary journeys and the first place where disciples were called Christians (Acts 11:26). The language of the region, Aramaic, had long since become the common tongue of the Near East and the vernacular spoken by Jesus.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "syria", "smith": "syria"},
        "key_refs": ["Genesis 25:20", "2 Samuel 8:6", "2 Kings 10:32", "Acts 11:26"]
    },
    "syriac": {
        "id": "syriac",
        "term": "Syriac",
        "category": "concepts",
        "intro": "<p>Syriac (more accurately rendered <em>Aramaic</em> in modern translations) refers to the Semitic language spoken across the ancient Near East that appears in several passages of the Old Testament and New Testament. In the Old Testament, Aramaic sections appear in Ezra 4:8–6:18 and 7:12–26, and in Daniel 2:4b–7:28, where the shift from Hebrew to Aramaic mid-narrative has long been noted by scholars. In 2 Kings 18:26, the Assyrian officers and the envoys of Hezekiah negotiate in Aramaic — the lingua franca of diplomacy — rather than in Hebrew, the language of the common people. The phrase \"Aramaic\" or \"Syriac\" in Daniel 2:4 marks the point where the language of the text shifts. In the New Testament, Aramaic words preserved in Greek transliteration include <em>Abba</em> (Father), <em>Maranatha</em> (Come, O Lord), <em>Talitha cumi</em> (little girl, arise), and the cry from the cross, <em>Eli, Eli, lama sabachthani</em> (Matthew 27:46; Mark 15:34). Aramaic was the everyday spoken language of Jewish Palestine in the first century and almost certainly the primary language in which Jesus taught.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "syriac"},
        "key_refs": ["2 Kings 18:26", "Ezra 4:7", "Daniel 2:4", "Matthew 27:46"]
    },
    "syrophenician": {
        "id": "syrophenician",
        "term": "Syrophenician",
        "category": "concepts",
        "intro": "<p>Syrophenician (Greek <em>Surophoinikissa</em>) is a geographic designation meaning a person of Phoenician origin living within the Roman province of Syria — as distinct from a Libyan Phoenician (Carthaginian). The term appears in Mark 7:26 to describe the woman who came to Jesus in the region of Tyre and Sidon seeking healing for her demon-possessed daughter: Mark calls her \"a Greek, a Syrophenician by nation,\" meaning she was a Gentile by religion and Phoenician by ethnicity within the Syrian province. Matthew's parallel account (Matthew 15:21–28) calls her a \"woman of Canaan,\" emphasizing her non-Israelite heritage. The encounter is remarkable for the woman's persistence and faith: when Jesus initially declined her request with the saying about giving the children's bread to dogs, she replied with quick-witted humility that even dogs eat the crumbs from their master's table — drawing from Jesus the declaration that her faith was great, and the immediate healing of her daughter. The episode is one of the clearest NT examples of Gentile faith receiving a blessing promised primarily to Israel.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "syrophenician"},
        "key_refs": ["Mark 7:26", "Matthew 15:21", "Matthew 15:28"]
    },
}


def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP s6: Sychem → Syrophenician: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
