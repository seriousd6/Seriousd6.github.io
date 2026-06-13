"""
BP Article Synthesis — a6: Azekah → Azur and Azzur
Covers Easton entries: Azekah through Azur and Azzur (6 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Script: scripts/bp-a6.py
Run: python3 scripts/bp-a6.py
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


# ── Article data ──────────────────────────────────────────────────────────────
ARTICLES = {
    "azekah": {
        "id": "azekah",
        "term": "Azekah",
        "category": "places",
        "intro": "<p>Azekah (meaning <em>dug over</em> or <em>strength of walls</em>) was a fortified town in the Shephelah, the low foothills of Judah, near Socoh (Joshua 15:35). It was the scene of Joshua's victory over the five confederated Amorite kings when divine intervention in the form of a violent hailstorm destroyed the fleeing army and, by tradition, the sun stood still over Gibeon (Joshua 10:10–11). The city is also mentioned as one of the last two Judean fortresses holding out against Nebuchadnezzar's final siege of Jerusalem (Jeremiah 34:7) and as a town resettled by returning exiles after the Babylonian captivity (Nehemiah 11:30).</p>",
        "hitchcock_meaning": "strength of walls",
        "source_ids": {"easton": "azekah", "smith": "azekah", "isbe": "azekah"},
        "key_refs": ["Joshua 10:10", "Joshua 15:35", "Jeremiah 34:7", "Nehemiah 11:30"],
        "sections": []
    },
    "azel": {
        "id": "azel",
        "term": "Azel",
        "category": "people",
        "intro": "<p>Azel (meaning <em>noble</em>) was a descendant of King Saul through Jonathan and Meribbaal (Mephibosheth), listed in the Benjaminite genealogy of 1 Chronicles 8:37–38 and 9:43–44. He had six sons whose names are recorded. Azel appears only in these genealogical lists and no narrative is attached to him.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "azel", "smith": "azel"},
        "key_refs": ["1 Chronicles 8:37", "1 Chronicles 8:38", "1 Chronicles 9:43"],
        "sections": []
    },
    "azmaveth": {
        "id": "azmaveth",
        "term": "Azmaveth",
        "category": "people",
        "intro": "<p>Azmaveth (meaning <em>strong as death</em> or <em>a he-goat</em>) is the name of several men and a place in the Old Testament. (1.) A Barhumite, one of David's thirty mighty warriors (2 Samuel 23:31; 1 Chronicles 11:33). (2.) An overseer of the royal treasuries under David (1 Chronicles 27:25). (3.) A descendant of Saul through Jonathan (1 Chronicles 8:36). As a place name, Azmaveth (also called Beth-azmaveth) was a town near Jerusalem whose men returned from exile with Zerubbabel (Ezra 2:24; Nehemiah 12:29).</p>",
        "hitchcock_meaning": "strong death; a he-goat",
        "source_ids": {"easton": "azmaveth", "smith": "azmaveth"},
        "key_refs": ["2 Samuel 23:31", "1 Chronicles 27:25", "Ezra 2:24"],
        "sections": []
    },
    "azotus": {
        "id": "azotus",
        "term": "Azotus",
        "category": "places",
        "intro": "<p>Azotus is the Greek and New Testament form of the Hebrew name Ashdod, one of the five principal Philistine cities on the Mediterranean coastal plain. The sole New Testament reference to the name is Acts 8:40, where Philip the evangelist is found at Azotus after the Spirit caught him away following the baptism of the Ethiopian eunuch—suggesting miraculous transport. From Azotus Philip preached throughout the coastal towns until reaching Caesarea. For the full account of the city see <strong>Ashdod</strong>.</p>",
        "hitchcock_meaning": "the same as Ashdod",
        "source_ids": {"easton": "azotus", "smith": "azotus", "isbe": "azotus"},
        "key_refs": ["Acts 8:40"],
        "sections": []
    },
    "azubah": {
        "id": "azubah",
        "term": "Azubah",
        "category": "people",
        "intro": "<p>Azubah (meaning <em>deserted</em> or <em>forsaken</em>) is the name of two women in the Old Testament. (1.) A wife of Caleb son of Hezron, who bore him several sons (1 Chronicles 2:18–19). She apparently died and Caleb then took Ephrath as his wife. (2.) The daughter of Shilhi and mother of King Jehoshaphat of Judah (1 Kings 22:42; 2 Chronicles 20:31), one of the few queen-mothers named in the Judean royal records.</p>",
        "hitchcock_meaning": "forsaken",
        "source_ids": {"easton": "azubah", "smith": "azubah", "isbe": "azubah"},
        "key_refs": ["1 Chronicles 2:18", "1 Kings 22:42"],
        "sections": []
    },
    "azur-and-azzur": {
        "id": "azur-and-azzur",
        "term": "Azur and Azzur",
        "category": "people",
        "intro": "<p>Azur (or Azzur, meaning <em>helper</em>) is the name of three men in the Old Testament. (1.) The father of Hananiah of Gibeon, a false prophet who opposed Jeremiah by declaring that the Babylonian exile would end within two years—a prophecy Jeremiah refuted and which led to Hananiah's death within the year (Jeremiah 28:1). (2.) The father of Jaazaniah, one of the wicked leaders of Jerusalem whom Ezekiel saw in a vision advising evil counsel (Ezekiel 11:1). (3.) One of the leaders who sealed the renewed covenant with God in the time of Nehemiah (Nehemiah 10:17).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "azur-and-azzur"},
        "key_refs": ["Jeremiah 28:1", "Ezekiel 11:1", "Nehemiah 10:17"],
        "sections": []
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
    print(f'BP a6: Azekah → Azur and Azzur: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
