import json, os, pathlib

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def load_article(slug):
    p = pathlib.Path(OUT_DIR) / f'{slug}.json'
    return json.loads(p.read_text()) if p.exists() else None

def save_article(slug, data):
    p = pathlib.Path(OUT_DIR) / f'{slug}.json'
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False))

def merge_article(slug, data):
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True

ARTICLES = {
    "korhites": {
        "term": "Korhites",
        "category": "people",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "korhites"},
        "key_refs": ["Exodus 6:24", "1 Chronicles 12:6", "1 Chronicles 26:1", "2 Chronicles 20:19"],
        "intro": "<p>The Korhites were a Levitical guild descended from Korah, son of Izhar of the tribe of Levi (Ex. 6:24). Though Korah himself perished in the wilderness rebellion against Moses (Num. 16), his sons survived (Num. 26:11) and their descendants became a significant order within the Levitical service. They are mentioned among the Levitical gatekeepers assigned to the south gate and the storehouse (1 Chr. 26:1) and among the warriors who joined David at Ziklag (1 Chr. 12:6). In the reign of Jehoshaphat they led worship before the battle against Moab and Ammon (2 Chr. 20:19). Their most enduring legacy is musical: the heading \"sons of Korah\" is attached to eleven psalms (Ps. 42-49, 84-85, 87-88), indicating the Korhites served as temple singers and custodians of a distinct liturgical tradition. The guild exemplifies the principle that divine judgment on an individual does not necessarily foreclose covenant service for his descendants.</p>"
    },
    "koz": {
        "term": "Koz",
        "category": "people",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "koz", "smith": "koz"},
        "key_refs": ["1 Chronicles 4:8", "Ezra 2:61", "Nehemiah 3:4", "1 Chronicles 24:10"],
        "intro": "<p>Koz (meaning <em>thorn</em>; also spelled Coz or Hakkoz, the form with the Hebrew definite article) is the name of two individuals in the Old Testament. (1.) A descendant of Judah through Aharhel, listed in the genealogy of 1 Chr. 4:8. (2.) A priest whose family returned from the Babylonian exile. He is named as the head of the seventh of the twenty-four divisions of priests established by David (1 Chr. 24:10). His priestly line could not prove its genealogy at the return and was therefore excluded from the priesthood until a ruling could be obtained by Urim and Thummim (Ezra 2:61-62; Neh. 7:63-64). Despite this disqualification, a descendant named Meremoth son of Uriah — himself a son of Hakkoz — is listed among those who helped repair the walls of Jerusalem under Nehemiah (Neh. 3:4, 21), suggesting the family was eventually restored to standing.</p>"
    },
}

wrote = skipped = 0
for slug, data in ARTICLES.items():
    article = {
        "id": slug,
        "term": data["term"],
        "category": data["category"],
        "intro": data["intro"],
        "hitchcock_meaning": data.get("hitchcock_meaning"),
        "source_ids": data.get("source_ids", {}),
        "key_refs": data.get("key_refs", []),
        "sections": []
    }
    if merge_article(slug, article):
        wrote += 1
    else:
        skipped += 1

print(f"BP k2: Korhites -> Koz: wrote {wrote}, skipped {skipped} existing.")
