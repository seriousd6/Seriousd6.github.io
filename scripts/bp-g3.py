"""
BP Article Synthesis — g3: Greece → Gutter
Covers Easton entries: Greece through Gutter (11 entries)

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

Script: scripts/bp-g3.py
Run: python3 scripts/bp-g3.py
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
    "greece": {
        "id": "greece",
        "term": "Greece",
        "category": "places",
        "intro": "<p>Greece in its classical sense comprised four main regions: Macedonia, Epirus, Achaia, and the Peloponnese. In the Old Testament, Greece appears as Javan (Hebrew <em>Yavan</em>), a son of Japheth and grandson of Noah (Genesis 10:2), whose descendants are identified with the Greeks. Daniel's prophecies refer to Greece as the kingdom that would arise to overthrow Persia (Daniel 8:21; 10:20; 11:2), which was fulfilled in Alexander the Great's conquests (334–323 BC). By New Testament times, Greece had been absorbed into the Roman province of Achaia, with Corinth as its capital.</p><p>The Hellenistic world created by Alexander's conquests profoundly shaped the context of the New Testament: Greek became the common language (<em>koine</em>) of the entire eastern Mediterranean, enabling the rapid spread of the gospel. Paul's missionary journeys took him through Macedonia and Achaia — Thessalonica, Berea, Athens, and Corinth (Acts 17–18; 20:2). His encounter with Athenian philosophers at the Areopagus (Acts 17:16–34) represents one of the most significant encounters between the gospel and Greek intellectual culture in the apostolic period.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "greece"},
        "key_refs": ["Acts 20:2", "Genesis 10:2", "Daniel 8:21"]
    },
    "greek": {
        "id": "greek",
        "term": "Greek",
        "category": "concepts",
        "intro": "<p>In the New Testament, a distinction is observed between \"Greek\" (<em>Hellēn</em>) and \"Grecian\" or \"Hellenist\" (<em>Hellēnistēs</em>). A \"Greek\" (<em>Hellēn</em>) was a non-Jew — a Gentile — whether ethnically Greek or simply a Greek-speaking member of the broader Hellenistic world. Paul uses the pairing \"Jew and Greek\" as a comprehensive term for all humanity (Romans 1:14, 16; 10:12; 1 Corinthians 1:22–24; Galatians 3:28), expressing that Christ's salvation breaks down the fundamental ethnic and cultural division of the ancient world.</p><p>A \"Hellenist\" or \"Grecian\" (Acts 6:1; 9:29), by contrast, was a Greek-speaking Jew — a member of the diaspora who had adopted Greek language and culture but retained Jewish religious identity. The tension between Hellenist and Hebrew-speaking Jewish Christians in the Jerusalem church over the care of widows (Acts 6:1) was one of the first internal challenges the early church faced, resolved by the appointment of the seven deacons. Timothy, born of a Jewish mother and a Greek father (Acts 16:1), exemplified the mixed heritage common in diaspora communities.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "greek"},
        "key_refs": ["Acts 16:1", "Romans 1:14", "Romans 2:9", "Galatians 3:28"]
    },
    "greyhound": {
        "id": "greyhound",
        "term": "Greyhound",
        "category": "concepts",
        "intro": "<p>Greyhound appears in the King James Version at Proverbs 30:31 as one of four things that \"go well\" or move with a stately bearing: \"A greyhound; an he goat also; and a king, against whom there is no rising up.\" The Hebrew <em>zarzir mothnayim</em> (literally \"girded as to the loins\") is an uncertain term whose precise referent has been debated by translators and commentators throughout history. Many modern translations render it as \"strutting rooster\" (ESV, NIV, NASB) rather than greyhound, based on comparison with ancient Near Eastern imagery of roosters as proud, upright animals.</p><p>The context in Proverbs 30:29–31 is a numerical proverb of observation — things in the created world that exhibit a characteristic grace or power in motion. Whether the animal is a greyhound, a rooster, or (as some ancient translations suggest) a war-horse, the point is the same: each creature in its proper element moves with a dignity that serves as a natural analogy for the authority of a rightful king. The passage illustrates the wisdom tradition's habit of finding moral and regal analogies in careful observation of the natural world.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "greyhound", "smith": "greyhound"},
        "key_refs": ["Proverbs 30:31"]
    },
    "grind": {
        "id": "grind",
        "term": "Grind",
        "category": "concepts",
        "intro": "<p>Grinding grain was one of the most labor-intensive daily tasks in the ancient household, performed by women using a hand mill consisting of two circular millstones. The lower stone was fixed while the upper stone rotated, crushing the grain between them. The sound of millstones was a constant background noise of village life, so much so that Jeremiah uses the cessation of \"the sound of the millstones\" as a mark of utter desolation (Jeremiah 25:10; Revelation 18:22). The task was so fundamental that two women grinding at a mill became a common picture of ordinary daily life (Matthew 24:41).</p><p>Grinding also appears in Scripture in specific narratives: the Israelites ground the golden calf to powder (Exodus 32:20; Deuteronomy 9:21), and Samson was put to grinding in prison after his capture by the Philistines (Judges 16:21) — the lowest work assigned to slaves. Isaiah 3:5 uses grinding as a metaphor for oppression of the poor: \"the people shall be oppressed, every one by another... the child shall behave himself proudly against the ancient.\" The image of grinding suggests reduction, subjugation, and labor without dignity — making it a powerful figure for both spiritual destruction and social exploitation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "grind"},
        "key_refs": ["Exodus 32:20", "Judges 16:21", "Isaiah 3:5", "Matthew 24:41"]
    },
    "grizzled": {
        "id": "grizzled",
        "term": "Grizzled",
        "category": "concepts",
        "intro": "<p>Grizzled means party-colored or streaked with grey and white, applied in Scripture to animals. In Genesis 31:10 and 12, Jacob's dream vision shows him the breeding pattern of Laban's flocks: the rams that mated with the speckled, spotted, and grizzled she-goats would produce the parti-colored offspring that would become Jacob's wages — a dream that Jacob understood as divine guidance and vindication in his conflict with Laban. The grizzled coloring thus marks the animals God designated as Jacob's portion in the disputed livestock agreement.</p><p>Grizzled horses appear in Zechariah 6:3 and 6 as part of the vision of four chariots with horses of different colors — red, black, white, and grizzled — going out to patrol the earth. The grizzled and white horses go out toward the south country. The vision depicts divine governance of the nations through angelic agencies, with the varied colors of the horses representing the different directions of divine attention. The precise symbolic meaning of each color has been variously interpreted, but the grizzled horses' direction toward the south suggests activity in relation to Egypt or the southern powers.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "grizzled"},
        "key_refs": ["Genesis 31:10", "Genesis 31:12", "Zechariah 6:3", "Zechariah 6:6"]
    },
    "grove": {
        "id": "grove",
        "term": "Grove",
        "category": "concepts",
        "intro": "<p>\"Grove\" in the King James Version most frequently translates the Hebrew <em>asherah</em> (plural <em>asherim</em>), which refers not to a natural grove of trees but to a wooden image or sacred pole representing Asherah — the Canaanite goddess of fertility and consort of Baal. The association of Asherah worship with trees and high places led early translators to render the term as \"grove,\" but modern translations consistently use \"Asherah pole\" or \"Asherah image.\" These cult objects were planted or erected near altars on high places throughout Canaan, and Israel's repeated adoption of Asherah worship is one of the persistent targets of prophetic condemnation and covenantal prohibition (Exodus 34:13; Deuteronomy 7:5; 16:21).</p><p>Gideon's first act of reform was to cut down his father's Asherah beside the altar of Baal (Judges 6:25–26). King Manasseh erected an Asherah in the temple itself (2 Kings 21:7) — among the most extreme acts of covenant violation recorded in the monarchy, reversed by Josiah's reform (2 Kings 23:4–6). The term occasionally does refer to a literal grove of trees: Abraham planted a tamarisk tree at Beersheba (Genesis 21:33), and Samuel's annual judicial circuit included spots associated with ancient trees (1 Samuel 7:16–17). Context determines which meaning applies in each passage.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "grove", "smith": "grove"},
        "key_refs": ["2 Kings 21:7", "2 Kings 23:4", "Exodus 34:13", "Judges 6:25"]
    },
    "guard": {
        "id": "guard",
        "term": "Guard",
        "category": "concepts",
        "intro": "<p>Guard in the Old Testament translates several Hebrew terms referring to military or official protective functions. The most significant is <em>tabbah</em> — literally \"cook\" or \"slaughterer,\" but used as a title for the captain of the royal bodyguard, whose role included both protection of the king and execution of royal sentences. Potiphar (Genesis 37:36; 39:1) and Nebuzaradan (2 Kings 25:8; Jeremiah 40:1) both held this title, connecting it to figures of significant political and military power. Daniel 2:14 also refers to the captain of this guard.</p><p>In the New Testament context, guards appear at significant moments: the soldiers who kept watch at Jesus's tomb (Matthew 27:65–66; 28:4, 11–15), whose report to the chief priests after the resurrection resulted in the bribe to propagate the rumor that the disciples had stolen the body; and the prison guards of Peter (Acts 12:6) and Paul (Acts 16:23–27), whose custody was dramatically broken by divine intervention. The praetorian guard (<em>praitorion</em>) mentioned in Philippians 1:13 was the elite imperial bodyguard to whom Paul's chains had become known, with the gospel reaching them through his Roman imprisonment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "guard"},
        "key_refs": ["Genesis 37:36", "2 Kings 25:8", "Matthew 27:65", "Philippians 1:13"]
    },
    "guest-chamber": {
        "id": "guest-chamber",
        "term": "Guest-chamber",
        "category": "concepts",
        "intro": "<p>The guest-chamber was the spare room typically located on the upper floor (<em>hyperōon</em>) of a Near Eastern dwelling, reserved for receiving visitors and travelers. In a culture where hospitality was a paramount social obligation, maintaining a dedicated guest space was expected in any household of moderate means. Luke 2:7 notes that Mary and Joseph found \"no room in the inn\" (<em>kataluma</em>) at Bethlehem — the same word used for the guest-chamber in Mark 14:14 and Luke 22:11, suggesting the term covers both a private guest room and an inn's common guest space.</p><p>The guest-chamber (or upper room) becomes theologically significant in the Gospel narratives: it was in such a room that Jesus celebrated his final Passover with his disciples and instituted the Lord's Supper (Mark 14:14–15; Luke 22:11–12). The disciples were instructed to tell the owner of the house that \"the Teacher\" asked where the guest-room was — a cryptic arrangement that suggests prior understanding or divine orchestration. The upper room (Acts 1:13) where the disciples gathered after the ascension and received the Holy Spirit at Pentecost (Acts 2:1) likely refers to the same or a similar space, making the upper room a recurring setting for decisive moments in the early Christian story.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "guest-chamber"},
        "key_refs": ["Mark 14:14", "Luke 22:11", "Luke 2:7", "Acts 1:13"]
    },
    "gur": {
        "id": "gur",
        "term": "Gur",
        "category": "places",
        "intro": "<p>Gur (meaning <em>a whelp</em> or <em>the young of a beast</em>) was a place near Ibleam in the territory of Manasseh where Jehu's servants overtook and mortally wounded King Ahaziah of Judah during Jehu's coup against the house of Ahab (2 Kings 9:27). Ahaziah had been visiting Joram king of Israel at Jezreel when Jehu's rebellion broke out; he fled in his chariot toward Beth-haggan but was shot by Jehu's bow. He managed to reach Megiddo before dying there. The mention of Gur as the site of the wounding is one of the geographically precise details that marks the historical character of the account of Jehu's revolution in 2 Kings 9–10.</p>",
        "hitchcock_meaning": "the young of a beast; a whelp",
        "source_ids": {"easton": "gur", "smith": "gur"},
        "key_refs": ["2 Kings 9:27"]
    },
    "gur-baal": {
        "id": "gur-baal",
        "term": "Gur-baal",
        "category": "places",
        "intro": "<p>Gur-baal (meaning <em>sojourn of Baal</em>) was a place in Arabia mentioned in 2 Chronicles 26:7 in the account of King Uzziah's military campaigns: \"God helped him against the Philistines, and against the Arabians that dwelt in Gur-baal, and the Mehunims.\" The site was located in the Arabian desert, likely south or southeast of Judah, and appears to have been a settlement associated with Baal worship — as its name suggests. Beyond this single reference, Gur-baal is not mentioned elsewhere in the biblical text, and its precise location has not been identified by modern archaeology.</p><p>The verse places Gur-baal in the context of Uzziah's remarkable military success during the period of his faithful reign — a period during which God prospered him against traditional enemies on multiple fronts before his fatal act of presumption in entering the temple to burn incense (2 Chronicles 26:16–21).</p>",
        "hitchcock_meaning": "the governor's whelp",
        "source_ids": {"easton": "gur-baal"},
        "key_refs": ["2 Chronicles 26:7"]
    },
    "gutter": {
        "id": "gutter",
        "term": "Gutter",
        "category": "concepts",
        "intro": "<p>Gutter (Hebrew <em>tsinnor</em>) appears in 2 Samuel 5:8 in the account of David's capture of Jerusalem from the Jebusites: \"Whosoever getteth up to the gutter, and smiteth the Jebusites...\" The word has been interpreted as a water shaft, conduit, or tunnel — possibly the vertical water shaft connecting the city of Jebus to the Gihon Spring below, through which David's warriors may have climbed to take the city by surprise. This interpretation is supported by archaeological discoveries at Jerusalem, including Warren's Shaft (discovered in 1867), a natural vertical shaft connected to the ancient water system that may be the passage referenced.</p><p>The same Hebrew word (<em>tsinnor</em>) occurs in Psalm 42:7 in the plural: \"deep calleth unto deep at the noise of thy waterspouts (<em>tsinnor</em>)\" — where it describes the rushing of waters, consistent with a channel or conduit. In Genesis 30:38, 41, a different but related word appears for the gutters or troughs Jacob placed before the flocks as part of his selective breeding strategy. The Siloam tunnel, Hezekiah's famous engineering project, is the most celebrated water channel system in ancient Jerusalem, though it dates later than the David narrative.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "gutter"},
        "key_refs": ["2 Samuel 5:8", "Psalms 42:7", "Genesis 30:38"]
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
    print(f'BP {__doc__.split(chr(10))[1].strip()}: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
