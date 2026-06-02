#!/usr/bin/env python3
"""
build-parallels.py
Generates data/parallels/{bookId}.json from a hardcoded curated list of
parallel Bible passages, fulfillment pairs, and quotation pairs.

Usage:
    python3 scripts/build-parallels.py            # generate all, skip existing
    python3 scripts/build-parallels.py --force    # overwrite all
    python3 scripts/build-parallels.py matthew luke  # specific books only
"""

import json
import os
import re
import sys
from collections import defaultdict

# ── Paths ─────────────────────────────────────────────────────────────────────
REPO_ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR    = os.path.join(REPO_ROOT, 'data', 'parallels')
BOOKS_JSON = os.path.join(REPO_ROOT, 'data', 'bible', 'books.json')

# ── Load books and build lookup ───────────────────────────────────────────────
def load_book_lookup():
    """Return dict: normalized string -> bookId (same logic as loadBooks in bible.js)."""
    with open(BOOKS_JSON, encoding='utf-8') as f:
        books = json.load(f)
    lookup = {}
    for book in books:
        # canonical name lowercase
        lookup[book['name'].lower()] = book['id']
        # canonical name lowercase, no spaces
        lookup[book['name'].lower().replace(' ', '')] = book['id']
        # id itself
        lookup[book['id']] = book['id']
        # each abbreviation lowercase
        for abbr in book.get('abbrevs', []):
            lookup[abbr.lower()] = book['id']
    return lookup

# ── Ref parser ────────────────────────────────────────────────────────────────
# Handles:
#   "Book Ch:V"
#   "Book Ch:V-V2"
#   "Book Ch:V-Ch2:V2"   (cross-chapter)
#   "Book Ch:V-Ch2"      (e.g. "1 Chronicles 15:25-16:3")  treated as Ch2:1 end
#
# Returns dict with keys: bookId, ch (str), v (str), endCh (str|None), endV (str|None)
# All numeric values kept as strings to match JSON key expectations.

_BOOK_LOOKUP = None  # populated lazily

def _get_lookup():
    global _BOOK_LOOKUP
    if _BOOK_LOOKUP is None:
        _BOOK_LOOKUP = load_book_lookup()
    return _BOOK_LOOKUP

# Pattern for "Book Ch:V..."
# Book name: optional leading digit + space, then letters/spaces
_REF_RE = re.compile(
    r'^((?:\d\s+)?[A-Za-z][A-Za-z\s]*?)\s+'   # book name (group 1)
    r'(\d+):(\d+)'                              # ch:v (groups 2,3)
    r'(?:-(?:(\d+):(\d+)|(\d+)))?$'            # optional end: ch2:v2 OR v2 (groups 4,5,6)
)

def parse_ref(ref_str):
    """
    Parse a reference string and return a dict, or None on failure.
    Keys: bookId, ch, v, endCh (may be None), endV (may be None)
    """
    ref_str = ref_str.strip()
    m = _REF_RE.match(ref_str)
    if not m:
        return None

    raw_book, ch, v, end_ch2, end_v2_cross, end_v2_simple = m.groups()
    book_key = raw_book.strip().lower().replace('  ', ' ')
    # also try without internal spaces
    book_id = _get_lookup().get(book_key) or _get_lookup().get(book_key.replace(' ', ''))
    if not book_id:
        return None

    result = {
        'bookId': book_id,
        'ch':     ch,
        'v':      v,
        'endCh':  None,
        'endV':   None,
    }

    if end_ch2 is not None and end_v2_cross is not None:
        # cross-chapter: "Ch2:V2"
        result['endCh'] = end_ch2
        result['endV']  = end_v2_cross
    elif end_v2_simple is not None:
        # simple verse range: "-V2"
        result['endV'] = end_v2_simple
    # else single verse — endV stays None

    return result

# ── Curated data ──────────────────────────────────────────────────────────────

# Section A: Gospel + OT Historical Parallels
# Each tuple: (label, [ref_str, ...])
PARALLEL_GROUPS = [
    # ── Gospel Parallels ──────────────────────────────────────────────────────
    ("Genealogy of Jesus",                      ["Matthew 1:1-17",    "Luke 3:23-38"]),
    ("Baptism of Jesus",                        ["Matthew 3:13-17",   "Mark 1:9-11",    "Luke 3:21-22"]),
    ("Temptation of Jesus",                     ["Matthew 4:1-11",    "Mark 1:12-13",   "Luke 4:1-13"]),
    ("John the Baptist's ministry",             ["Matthew 3:1-6",     "Mark 1:1-6",     "Luke 3:1-6"]),
    ("John's proclamation",                     ["Matthew 3:7-12",    "Luke 3:7-17"]),
    ("Beginning of Galilean ministry",          ["Matthew 4:12-17",   "Mark 1:14-15",   "Luke 4:14-15"]),
    ("Call of first disciples",                 ["Matthew 4:18-22",   "Mark 1:16-20"]),
    ("Call of Levi/Matthew",                    ["Matthew 9:9-13",    "Mark 2:13-17",   "Luke 5:27-32"]),
    ("Question about fasting",                  ["Matthew 9:14-17",   "Mark 2:18-22",   "Luke 5:33-39"]),
    ("Plucking grain on Sabbath",               ["Matthew 12:1-8",    "Mark 2:23-28",   "Luke 6:1-5"]),
    ("Healing on the Sabbath",                  ["Matthew 12:9-14",   "Mark 3:1-6",     "Luke 6:6-11"]),
    ("Appointment of the Twelve",               ["Matthew 10:1-4",    "Mark 3:13-19",   "Luke 6:12-16"]),
    ("Healing paralytic (Capernaum)",           ["Matthew 9:1-8",     "Mark 2:1-12",    "Luke 5:17-26"]),
    ("Healing of leper",                        ["Matthew 8:1-4",     "Mark 1:40-45",   "Luke 5:12-16"]),
    ("Peter's mother-in-law",                   ["Matthew 8:14-15",   "Mark 1:29-31",   "Luke 4:38-39"]),
    ("Evening healings",                        ["Matthew 8:16-17",   "Mark 1:32-34",   "Luke 4:40-41"]),
    ("Centurion's servant",                     ["Matthew 8:5-13",    "Luke 7:1-10"]),
    ("Stilling the storm",                      ["Matthew 8:23-27",   "Mark 4:35-41",   "Luke 8:22-25"]),
    ("Gadarene demoniac",                       ["Matthew 8:28-34",   "Mark 5:1-20",    "Luke 8:26-39"]),
    ("Jairus's daughter and the woman",         ["Matthew 9:18-26",   "Mark 5:21-43",   "Luke 8:40-56"]),
    ("Sending out the Twelve",                  ["Matthew 10:5-15",   "Mark 6:7-13",    "Luke 9:1-6"]),
    ("Feeding the five thousand",               ["Matthew 14:13-21",  "Mark 6:30-44",   "Luke 9:10-17",  "John 6:1-15"]),
    ("Walking on water",                        ["Matthew 14:22-33",  "Mark 6:45-52",   "John 6:16-21"]),
    ("Syrophoenician woman",                    ["Matthew 15:21-28",  "Mark 7:24-30"]),
    ("Feeding the four thousand",               ["Matthew 15:32-39",  "Mark 8:1-10"]),
    ("Peter's confession at Caesarea Philippi", ["Matthew 16:13-20",  "Mark 8:27-30",   "Luke 9:18-21"]),
    ("First passion prediction",                ["Matthew 16:21-23",  "Mark 8:31-33",   "Luke 9:22"]),
    ("Transfiguration",                         ["Matthew 17:1-9",    "Mark 9:2-9",     "Luke 9:28-36"]),
    ("Healing the epileptic boy",               ["Matthew 17:14-21",  "Mark 9:14-29",   "Luke 9:37-43"]),
    ("Second passion prediction",               ["Matthew 17:22-23",  "Mark 9:30-32",   "Luke 9:43-45"]),
    ("Third passion prediction",                ["Matthew 20:17-19",  "Mark 10:32-34",  "Luke 18:31-34"]),
    ("Rich young ruler",                        ["Matthew 19:16-22",  "Mark 10:17-22",  "Luke 18:18-23"]),
    ("Healing of Bartimaeus",                   ["Matthew 20:29-34",  "Mark 10:46-52",  "Luke 18:35-43"]),
    ("Beatitudes",                              ["Matthew 5:3-12",    "Luke 6:20-26"]),
    ("Love of enemies",                         ["Matthew 5:43-48",   "Luke 6:27-36"]),
    ("Judging others",                          ["Matthew 7:1-5",     "Luke 6:37-42"]),
    ("Two builders",                            ["Matthew 7:24-27",   "Luke 6:47-49"]),
    ("Lord's Prayer",                           ["Matthew 6:9-13",    "Luke 11:2-4"]),
    ("Anxiety — seek first the kingdom",        ["Matthew 6:25-34",   "Luke 12:22-32"]),
    ("Ask, seek, knock",                        ["Matthew 7:7-11",    "Luke 11:9-13"]),
    ("Triumphal entry into Jerusalem",          ["Matthew 21:1-9",    "Mark 11:1-10",   "Luke 19:28-40", "John 12:12-19"]),
    ("Cleansing of the Temple",                 ["Matthew 21:12-13",  "Mark 11:15-17",  "Luke 19:45-46"]),
    ("Question about authority",                ["Matthew 21:23-27",  "Mark 11:27-33",  "Luke 20:1-8"]),
    ("Parable of the tenants",                  ["Matthew 21:33-46",  "Mark 12:1-12",   "Luke 20:9-19"]),
    ("Tribute to Caesar",                       ["Matthew 22:15-22",  "Mark 12:13-17",  "Luke 20:20-26"]),
    ("Sadducees and the resurrection",          ["Matthew 22:23-33",  "Mark 12:18-27",  "Luke 20:27-40"]),
    ("Greatest commandment",                    ["Matthew 22:34-40",  "Mark 12:28-34",  "Luke 10:25-28"]),
    ("David's son",                             ["Matthew 22:41-46",  "Mark 12:35-37",  "Luke 20:41-44"]),
    ("Warning against scribes",                 ["Matthew 23:1-7",    "Mark 12:38-40",  "Luke 20:45-47"]),
    ("Widow's offering",                        ["Mark 12:41-44",     "Luke 21:1-4"]),
    ("Signs of the end — beginning",            ["Matthew 24:1-8",    "Mark 13:1-8",    "Luke 21:5-11"]),
    ("Warning of persecution",                  ["Matthew 24:9-14",   "Mark 13:9-13",   "Luke 21:12-19"]),
    ("The abomination of desolation",           ["Matthew 24:15-22",  "Mark 13:14-20",  "Luke 21:20-24"]),
    ("Coming of the Son of Man",                ["Matthew 24:29-31",  "Mark 13:24-27",  "Luke 21:25-28"]),
    ("Lesson from the fig tree",                ["Matthew 24:32-35",  "Mark 13:28-31",  "Luke 21:29-33"]),
    ("The unknown hour",                        ["Matthew 24:36-44",  "Mark 13:32-37"]),
    ("Anointing at Bethany",                    ["Matthew 26:6-13",   "Mark 14:3-9",    "John 12:1-8"]),
    ("Institution of the Lord's Supper",        ["Matthew 26:26-29",  "Mark 14:22-25",  "Luke 22:14-20"]),
    ("Prediction of betrayal",                  ["Matthew 26:20-25",  "Mark 14:17-21",  "Luke 22:21-23",  "John 13:21-30"]),
    ("Gethsemane",                              ["Matthew 26:36-46",  "Mark 14:32-42",  "Luke 22:39-46"]),
    ("Arrest of Jesus",                         ["Matthew 26:47-56",  "Mark 14:43-52",  "Luke 22:47-53",  "John 18:1-11"]),
    ("Before the high priest",                  ["Matthew 26:57-68",  "Mark 14:53-65",  "Luke 22:54-71"]),
    ("Peter's denial",                          ["Matthew 26:69-75",  "Mark 14:66-72",  "Luke 22:55-62",  "John 18:15-18"]),
    ("Jesus before Pilate",                     ["Matthew 27:11-14",  "Mark 15:2-5",    "Luke 23:1-5",    "John 18:33-38"]),
    ("Crucifixion",                             ["Matthew 27:32-44",  "Mark 15:21-32",  "Luke 23:26-43",  "John 19:17-27"]),
    ("Death of Jesus",                          ["Matthew 27:45-56",  "Mark 15:33-41",  "Luke 23:44-49",  "John 19:28-30"]),
    ("Burial of Jesus",                         ["Matthew 27:57-61",  "Mark 15:42-47",  "Luke 23:50-56",  "John 19:38-42"]),
    ("The empty tomb",                          ["Matthew 28:1-8",    "Mark 16:1-8",    "Luke 24:1-12",   "John 20:1-10"]),

    # ── OT Historical Parallels ───────────────────────────────────────────────
    ("David made king over all Israel",         ["2 Samuel 5:1-3",    "1 Chronicles 11:1-3"]),
    ("Capture of Jerusalem",                    ["2 Samuel 5:6-10",   "1 Chronicles 11:4-9"]),
    ("David's mighty men",                      ["2 Samuel 23:8-39",  "1 Chronicles 11:10-47"]),
    ("Ark brought to Jerusalem",                ["2 Samuel 6:1-19",   "1 Chronicles 15:25-16:3"]),
    ("Davidic covenant",                        ["2 Samuel 7:1-16",   "1 Chronicles 17:1-15"]),
    ("David's victories",                       ["2 Samuel 8:1-18",   "1 Chronicles 18:1-17"]),
    ("Census and plague",                       ["2 Samuel 24:1-25",  "1 Chronicles 21:1-30"]),
    ("Solomon at Gibeon — wisdom",              ["1 Kings 3:4-15",    "2 Chronicles 1:1-13"]),
    ("Building the Temple",                     ["1 Kings 6:1-38",    "2 Chronicles 3:1-17"]),
    ("Dedication of the Temple",                ["1 Kings 8:1-21",    "2 Chronicles 5:2-6:11"]),
    ("Hezekiah and Sennacherib",                ["2 Kings 18:13-37",  "2 Chronicles 32:1-22",  "Isaiah 36:1-22"]),
    ("Hezekiah's prayer and deliverance",       ["2 Kings 19:1-37",   "Isaiah 37:1-38"]),
    ("Hezekiah's illness and recovery",         ["2 Kings 20:1-11",   "Isaiah 38:1-8"]),
    ("Josiah's reform",                         ["2 Kings 22:1-23:30","2 Chronicles 34:1-35:27"]),
    ("Fall of Jerusalem",                       ["2 Kings 24:18-25:21","2 Chronicles 36:11-21", "Jeremiah 52:1-30"]),
    ("Cyrus's decree",                          ["2 Chronicles 36:22-23","Ezra 1:1-4"]),
    ("Psalm 18 — David's song of deliverance",  ["Psalm 18:1-50",     "2 Samuel 22:1-51"]),
    ("Psalm 14 — the fool",                     ["Psalm 14:1-7",      "Psalm 53:1-6"]),
    ("Psalm 40:13-17 — plea for help",          ["Psalm 40:13-17",    "Psalm 70:1-5"]),
    ("Psalm 57:7-11 and 60:5-12",               ["Psalm 57:7-11",     "Psalm 108:1-5"]),
    ("Isaiah 2:1-4 — mountain of the Lord",     ["Isaiah 2:1-4",      "Micah 4:1-3"]),
]

# Section C: Prophecy / Fulfillment
# Each tuple: (ot_ref, nt_ref, label)
FULFILLMENT_PAIRS = [
    ("Isaiah 7:14",        "Matthew 1:23",       "Born of a virgin"),
    ("Isaiah 9:1-2",       "Matthew 4:15-16",    "Light to Galilee"),
    ("Isaiah 40:3",        "Matthew 3:3",         "Voice crying in the wilderness"),
    ("Isaiah 40:3",        "Mark 1:3",            "Voice crying in the wilderness"),
    ("Isaiah 40:3",        "Luke 3:4-6",          "Voice crying in the wilderness"),
    ("Isaiah 40:3",        "John 1:23",           "Voice crying in the wilderness"),
    ("Isaiah 53:4",        "Matthew 8:17",        "He took our infirmities"),
    ("Isaiah 53:7-8",      "Acts 8:32-33",        "Led as a sheep to the slaughter"),
    ("Isaiah 61:1-2",      "Luke 4:18-19",        "The Spirit of the Lord is upon me"),
    ("Micah 5:2",          "Matthew 2:6",         "Born in Bethlehem"),
    ("Zechariah 9:9",      "Matthew 21:5",        "Your king comes riding on a donkey"),
    ("Zechariah 9:9",      "John 12:15",          "Your king comes riding on a donkey"),
    ("Zechariah 11:12-13", "Matthew 27:9-10",     "Thirty pieces of silver"),
    ("Zechariah 12:10",    "John 19:37",          "They will look on the one they pierced"),
    ("Zechariah 12:10",    "Revelation 1:7",      "They will look on the one they pierced"),
    ("Jeremiah 31:15",     "Matthew 2:18",        "Rachel weeping for her children"),
    ("Hosea 11:1",         "Matthew 2:15",        "Out of Egypt I called my son"),
    ("Psalm 22:1",         "Matthew 27:46",       "My God, my God, why have you forsaken me"),
    ("Psalm 22:1",         "Mark 15:34",          "My God, my God, why have you forsaken me"),
    ("Psalm 22:7-8",       "Matthew 27:39-43",    "Mocking at the cross"),
    ("Psalm 22:18",        "Matthew 27:35",       "They divided my garments"),
    ("Psalm 22:18",        "John 19:24",          "They divided my garments"),
    ("Psalm 22:22",        "Hebrews 2:12",        "Declaring God's name to the brethren"),
    ("Psalm 16:10",        "Acts 2:27-28",        "You will not abandon me to the grave"),
    ("Psalm 16:10",        "Acts 13:35",          "You will not abandon me to the grave"),
    ("Psalm 69:21",        "Matthew 27:34",       "Vinegar mixed with gall"),
    ("Psalm 69:21",        "John 19:29",          "They gave me vinegar to drink"),
    ("Psalm 110:1",        "Matthew 22:44",       "The Lord said to my Lord"),
    ("Psalm 110:1",        "Mark 12:36",          "The Lord said to my Lord"),
    ("Psalm 110:1",        "Acts 2:34-35",        "The Lord said to my Lord"),
    ("Psalm 110:1",        "Hebrews 1:13",        "The Lord said to my Lord"),
    ("Psalm 118:22-23",    "Matthew 21:42",       "The stone the builders rejected"),
    ("Psalm 118:22-23",    "Mark 12:10-11",       "The stone the builders rejected"),
    ("Psalm 118:22-23",    "Acts 4:11",           "The stone the builders rejected"),
    ("Psalm 118:22-23",    "1 Peter 2:7",         "The stone the builders rejected"),
    ("Psalm 118:26",       "Matthew 21:9",        "Blessed is he who comes in the name of the Lord"),
    ("Daniel 7:13-14",     "Matthew 24:30",       "Son of Man coming on the clouds"),
    ("Daniel 7:13-14",     "Revelation 1:7",      "Son of Man coming on the clouds"),
    ("Genesis 12:3",       "Galatians 3:8",       "All nations blessed through Abraham"),
    ("Deuteronomy 18:15",  "Acts 3:22",           "A prophet like Moses"),
    ("Deuteronomy 18:15",  "Acts 7:37",           "A prophet like Moses"),
    ("Deuteronomy 21:23",  "Galatians 3:13",      "Cursed is everyone who is hanged on a tree"),
    ("Leviticus 18:5",     "Romans 10:5",         "The man who does these things will live"),
    ("Leviticus 18:5",     "Galatians 3:12",      "The man who does these things will live"),
    ("Habakkuk 2:4",       "Romans 1:17",         "The righteous shall live by faith"),
    ("Habakkuk 2:4",       "Galatians 3:11",      "The righteous shall live by faith"),
    ("Habakkuk 2:4",       "Hebrews 10:38",       "The righteous shall live by faith"),
    ("Isaiah 28:16",       "Romans 9:33",         "A cornerstone in Zion"),
    ("Isaiah 28:16",       "1 Peter 2:6",         "A cornerstone in Zion"),
    ("Isaiah 53:1",        "John 12:38",          "Lord, who has believed our report?"),
    ("Isaiah 53:1",        "Romans 10:16",        "Lord, who has believed our report?"),
    ("Jeremiah 31:31-34",  "Hebrews 8:8-12",      "The new covenant"),
    ("Jeremiah 31:31-34",  "Hebrews 10:16-17",    "The new covenant"),
]

# Section D: NT Quotations of OT
# Each tuple: (ot_ref, nt_ref, label)
QUOTATION_PAIRS = [
    ("Exodus 20:12-16",     "Matthew 19:18-19",   "The Ten Commandments (summary)"),
    ("Deuteronomy 6:4-5",   "Mark 12:29-30",      "The Shema — greatest commandment"),
    ("Deuteronomy 6:5",     "Matthew 22:37",      "Love the Lord your God"),
    ("Isaiah 6:9-10",       "Matthew 13:14-15",   "Hearing but never understanding"),
    ("Isaiah 6:9-10",       "John 12:40",         "He has blinded their eyes"),
    ("Isaiah 6:9-10",       "Acts 28:26-27",      "Hearing but never understanding"),
    ("Isaiah 29:13",        "Matthew 15:8-9",     "These people honor me with their lips"),
    ("Isaiah 29:13",        "Mark 7:6-7",         "These people honor me with their lips"),
    ("Isaiah 56:7",         "Matthew 21:13",      "My house shall be called a house of prayer"),
    ("Isaiah 56:7",         "Mark 11:17",         "My house shall be called a house of prayer"),
    ("Jeremiah 7:11",       "Matthew 21:13",      "Den of robbers"),
    ("Jeremiah 7:11",       "Mark 11:17",         "Den of robbers"),
    ("Malachi 3:1",         "Matthew 11:10",      "I will send my messenger ahead of you"),
    ("Malachi 3:1",         "Mark 1:2",           "I will send my messenger ahead of you"),
    ("Malachi 3:1",         "Luke 7:27",          "I will send my messenger ahead of you"),
]

# Section E: Allusions — NT passages that refer to OT events/people without
# direct quotation or prophecy fulfillment. Bidirectional: both sides get
# type="allusion" so the panel shows "Allusion" on each end.
# Each tuple: (nt_ref, ot_ref, label)
ALLUSION_PAIRS = [
    # ── Hebrews 11 — Hall of Faith ────────────────────────────────────────────
    ("Hebrews 11:4",       "Genesis 4:3-5",        "Abel's offering accepted by faith"),
    ("Hebrews 11:5",       "Genesis 5:21-24",      "Enoch taken without seeing death"),
    ("Hebrews 11:7",       "Genesis 6:13-22",      "Noah builds the ark by faith"),
    ("Hebrews 11:8-10",    "Genesis 12:1-5",       "Abraham's call to leave his homeland"),
    ("Hebrews 11:11-12",   "Genesis 21:1-7",       "Sarah conceives Isaac in old age"),
    ("Hebrews 11:17-19",   "Genesis 22:1-14",      "Abraham offers Isaac — faith in resurrection"),
    ("Hebrews 11:20",      "Genesis 27:27-40",     "Isaac blesses Jacob and Esau by faith"),
    ("Hebrews 11:21",      "Genesis 47:31",        "Jacob worships leaning on his staff"),
    ("Hebrews 11:22",      "Genesis 50:24-25",     "Joseph's dying command about his bones"),
    ("Hebrews 11:23",      "Exodus 2:1-2",         "Moses' parents hide him by faith"),
    ("Hebrews 11:24-26",   "Exodus 2:11-15",       "Moses chooses suffering with God's people"),
    ("Hebrews 11:28",      "Exodus 12:21-30",      "Moses institutes the Passover by faith"),
    ("Hebrews 11:29",      "Exodus 14:21-31",      "Israel crosses the Red Sea"),
    ("Hebrews 11:30",      "Joshua 6:1-20",        "Jericho's walls fall by faith"),
    ("Hebrews 11:31",      "Joshua 2:1-21",        "Rahab shelters the spies by faith"),
    ("Hebrews 11:32",      "Judges 6:11-7:25",     "Gideon defeats the Midianites"),
    ("Hebrews 11:32",      "Judges 4:1-24",        "Barak defeats Sisera"),
    ("Hebrews 11:32",      "Judges 16:23-31",      "Samson's final act of faith"),
    ("Hebrews 11:32",      "Judges 11:1-33",       "Jephthah defeats the Ammonites"),
    ("Hebrews 11:32",      "1 Samuel 17:32-50",    "David defeats Goliath"),
    ("Hebrews 11:32",      "1 Samuel 1:1-28",      "Samuel dedicated to the Lord"),
    ("Hebrews 11:33-34",   "Daniel 6:16-23",       "Daniel in the lions' den"),
    ("Hebrews 11:33-34",   "Daniel 3:16-27",       "Three men in the fiery furnace"),
    ("Hebrews 11:37",      "1 Kings 19:1-18",      "Prophets persecuted — Elijah flees Jezebel"),
    # ── James ─────────────────────────────────────────────────────────────────
    ("James 2:21-24",      "Genesis 22:1-18",      "Abraham justified by works — offering Isaac"),
    ("James 2:25",         "Joshua 2:1-21",        "Rahab justified by sheltering the spies"),
    ("James 5:11",         "Job 1:1-2:13",         "Job's patience under suffering"),
    ("James 5:17-18",      "1 Kings 17:1",         "Elijah prays and rain stops"),
    ("James 5:17-18",      "1 Kings 18:41-45",     "Elijah prays and rain returns"),
    # ── Romans ────────────────────────────────────────────────────────────────
    ("Romans 4:3",         "Genesis 15:6",         "Abraham believed God — faith counted as righteousness"),
    ("Romans 4:17",        "Genesis 17:5",         "Abraham father of many nations"),
    ("Romans 4:18",        "Genesis 15:5",         "Your offspring will be like the stars"),
    ("Romans 9:7",         "Genesis 21:12",        "Isaac — children of promise not natural descent"),
    ("Romans 9:9",         "Genesis 18:10",        "Sarah will have a son — promise at set time"),
    ("Romans 9:12",        "Genesis 25:23",        "The older will serve the younger — Jacob and Esau"),
    ("Romans 11:3",        "1 Kings 19:10",        "Elijah's complaint — I am the only one left"),
    ("Romans 11:4",        "1 Kings 19:18",        "Seven thousand reserved who have not bowed to Baal"),
    # ── 1 Corinthians ─────────────────────────────────────────────────────────
    ("1 Corinthians 10:1-5", "Exodus 13:21-22",    "Israel under the cloud and through the sea"),
    ("1 Corinthians 10:6-10", "Numbers 21:4-9",    "Israel's wilderness failures as warnings"),
    # ── Galatians ─────────────────────────────────────────────────────────────
    ("Galatians 4:21-31",  "Genesis 21:1-21",      "Hagar and Sarah — two covenants"),
    # ── 2 Peter ───────────────────────────────────────────────────────────────
    ("2 Peter 2:4",        "Genesis 6:1-4",        "Angels who sinned confined to darkness"),
    ("2 Peter 2:5",        "Genesis 6:9-7:24",     "Noah — righteous man preserved through flood"),
    ("2 Peter 2:6-8",      "Genesis 19:1-29",      "Lot rescued from Sodom's destruction"),
    ("2 Peter 2:15-16",    "Numbers 22:1-41",      "Balaam's donkey — a prophet rebuked"),
    # ── Jude ──────────────────────────────────────────────────────────────────
    ("Jude 1:5",           "Numbers 14:1-38",      "Israel destroyed in the wilderness for unbelief"),
    ("Jude 1:6",           "Genesis 6:1-4",        "Angels who abandoned their position"),
    ("Jude 1:7",           "Genesis 19:1-29",      "Sodom and Gomorrah as examples of judgment"),
    ("Jude 1:11",          "Genesis 4:3-8",        "The way of Cain — murder from envy"),
    ("Jude 1:11",          "Numbers 22:1-41",      "Balaam's error — false prophecy for profit"),
    ("Jude 1:11",          "Numbers 16:1-35",      "Korah's rebellion against God's order"),
    # -- Revelation -- OT imagery and allusions --------------------------------
    ("Revelation 1:13-16",  "Daniel 10:5-6",        "Son of Man figure with gold sash and face like lightning"),
    ("Revelation 4:6-8",    "Ezekiel 1:5-14",       "Four living creatures before the throne"),
    ("Revelation 4:8",      "Isaiah 6:2-3",         "Six-winged creatures crying Holy holy holy"),
    ("Revelation 6:12-14",  "Isaiah 13:10",         "Sun darkened and stars fall -- day of the Lord imagery"),
    ("Revelation 6:14",     "Isaiah 34:4",          "The sky rolls up like a scroll"),
    ("Revelation 7:3",      "Ezekiel 9:4",          "Seal on the forehead of God's servants"),
    ("Revelation 9:7-9",    "Joel 2:4-5",           "Locusts like warhorses -- army of devastation"),
    ("Revelation 10:9-10",  "Ezekiel 2:8-3:3",      "Eating the scroll -- sweet as honey but bitter in the stomach"),
    ("Revelation 11:4",     "Zechariah 4:2-3",      "Two olive trees and two lampstands before the Lord"),
    ("Revelation 12:1-6",   "Isaiah 66:7-8",        "Woman giving birth before labor -- nation born at once"),
    ("Revelation 13:1-2",   "Daniel 7:3-7",         "Beast rising from the sea -- composite of Daniel's four beasts"),
    ("Revelation 14:14-16", "Joel 3:13",            "Harvest sickle swung -- grain of the earth reaped"),
    ("Revelation 17:4",     "Jeremiah 51:7",        "Golden cup full of abominations -- Babylon the seductress"),
    ("Revelation 18:2",     "Isaiah 21:9",          "Babylon has fallen -- the prophetic announcement"),
    ("Revelation 18:4",     "Jeremiah 51:45",       "Come out of her my people -- do not share in her sins"),
    ("Revelation 18:7-8",   "Isaiah 47:7-9",        "I sit as queen and will never mourn -- plagues in one day"),
    ("Revelation 19:11-16", "Isaiah 63:1-3",        "Rider in blood-stained robe -- winepress of God's wrath"),
    ("Revelation 20:7-9",   "Ezekiel 38:2-9",       "Gog and Magog surround the holy city -- defeated by fire"),
    ("Revelation 21:3",     "Ezekiel 37:27",        "God will dwell among his people -- the tabernacle of God"),
    ("Revelation 22:1-2",   "Ezekiel 47:1-12",      "River flowing from the throne -- trees bearing fruit monthly"),
    ("Revelation 22:2",     "Genesis 2:9",          "Tree of life restored -- what was lost in Eden is regained"),
    # -- John -- Gospel allusions to OT ----------------------------------------
    ("John 10:11",          "Psalm 23:1",           "The Lord is my shepherd -- Jesus claims the role of the shepherd psalm"),
    ("John 15:1",           "Psalm 80:8-11",        "You brought a vine out of Egypt -- Jesus as the True Vine"),
    # -- Luke -- Magnificat drawn from Hannah's prayer -------------------------
    ("Luke 1:46-55",        "1 Samuel 2:1-10",      "Mary's Magnificat echoes Hannah's prayer of praise"),
    # -- 1-2 Thessalonians -----------------------------------------------------
    ("1 Thessalonians 4:16","Daniel 12:2",          "Dead will rise -- multitude asleep in the dust will awake"),
    ("1 Thessalonians 5:3", "Isaiah 13:8",          "Sudden destruction like labor pains -- day of the Lord"),
    ("2 Thessalonians 2:3-4","Daniel 11:36",        "Man of lawlessness exalts himself above every god"),
    ("2 Thessalonians 1:8", "Isaiah 66:15",         "Flaming fire punishing those who do not know God"),
    # -- 1 John ----------------------------------------------------------------
    ("1 John 3:12",         "Genesis 4:8",          "Cain who murdered his brother -- do not be like Cain"),
]

# Section F: Additional Fulfillment Pairs — OT prophecies fulfilled in NT
# Format: (ot_ref, nt_ref, label)  same as FULFILLMENT_PAIRS
FULFILLMENT_PAIRS_EXTRA = [
    # ── Isaiah 53 — Suffering Servant ────────────────────────────────────────
    ("Isaiah 53:3",        "John 1:11",            "He came to his own and was rejected"),
    ("Isaiah 53:4-5",      "1 Peter 2:24-25",      "By his wounds we are healed"),
    ("Isaiah 53:6",        "1 Peter 2:25",         "We all like sheep have gone astray"),
    ("Isaiah 53:7",        "John 19:9",            "He did not open his mouth — before Pilate"),
    ("Isaiah 53:9",        "Matthew 27:57-60",     "Buried in a rich man's tomb"),
    ("Isaiah 53:9",        "1 Peter 2:22",         "No deceit found in his mouth"),
    ("Isaiah 53:12",       "Luke 22:37",           "Numbered with transgressors"),
    ("Isaiah 53:12",       "Mark 15:27-28",        "Crucified between thieves"),
    # ── Psalms — Messianic ────────────────────────────────────────────────────
    ("Psalm 2:1-2",        "Acts 4:25-27",         "Nations conspire against the Lord's Anointed"),
    ("Psalm 2:7",          "Hebrews 1:5",          "You are my Son; today I have become your Father"),
    ("Psalm 2:7",          "Hebrews 5:5",          "Christ did not glorify himself — declared Son"),
    ("Psalm 2:7",          "Acts 13:33",           "Raised Jesus — as written in Psalm 2"),
    ("Psalm 8:2",          "Matthew 21:16",        "From the lips of children you have ordained praise"),
    ("Psalm 8:4-6",        "Hebrews 2:6-8",        "Mankind crowned with glory — fulfilled in Jesus"),
    ("Psalm 16:10",        "Acts 2:27",            "You will not let your Holy One see decay"),
    ("Psalm 22:8",         "Matthew 27:43",        "He trusts in God — let God rescue him"),
    ("Psalm 31:5",         "Luke 23:46",           "Into your hands I commit my spirit"),
    ("Psalm 34:20",        "John 19:36",           "Not one of his bones will be broken"),
    ("Psalm 35:19",        "John 15:25",           "They hated me without reason"),
    ("Psalm 40:6-8",       "Hebrews 10:5-7",       "Sacrifice not desired — I have come to do your will"),
    ("Psalm 41:9",         "John 13:18",           "He who shared my bread has lifted his heel against me"),
    ("Psalm 45:6-7",       "Hebrews 1:8-9",        "Your throne, O God, will last forever"),
    ("Psalm 68:18",        "Ephesians 4:8",        "He ascended on high and gave gifts to men"),
    ("Psalm 69:9",         "John 2:17",            "Zeal for your house will consume me"),
    ("Psalm 69:9",         "Romans 15:3",          "Insults of those who insult you fall on me"),
    ("Psalm 69:21",        "John 19:28-29",        "They gave me vinegar for my thirst"),
    ("Psalm 78:2",         "Matthew 13:35",        "I will open my mouth in parables"),
    ("Psalm 102:25-27",    "Hebrews 1:10-12",      "Lord, you laid the foundations of the earth"),
    ("Psalm 104:4",        "Hebrews 1:7",          "He makes his angels winds, servants flames of fire"),
    ("Psalm 110:4",        "Hebrews 5:6",          "A priest forever in the order of Melchizedek"),
    ("Psalm 110:4",        "Hebrews 7:17",         "You are a priest forever — Jesus' eternal priesthood"),
    ("Psalm 118:22-23",    "1 Peter 2:7",          "The stone the builders rejected is the cornerstone"),
    ("Psalm 132:11",       "Acts 2:30",            "God swore to place David's descendant on his throne"),
    # ── Zechariah ─────────────────────────────────────────────────────────────
    ("Zechariah 11:13",    "Matthew 27:9-10",      "Thirty pieces of silver thrown to the potter"),
    ("Zechariah 13:7",     "Matthew 26:31",        "Strike the shepherd and the sheep scatter"),
    ("Zechariah 13:7",     "Mark 14:27",           "Strike the shepherd and the sheep scatter"),
    # ── Isaiah ────────────────────────────────────────────────────────────────
    ("Isaiah 8:14",        "Romans 9:33",          "A stone that causes stumbling — to Israel"),
    ("Isaiah 8:14",        "1 Peter 2:8",          "A stone that causes people to stumble"),
    ("Isaiah 11:10",       "Romans 15:12",         "The Root of Jesse will stand as a banner for the peoples"),
    ("Isaiah 25:8",        "1 Corinthians 15:54",  "Death has been swallowed up in victory"),
    ("Isaiah 25:8",        "Revelation 21:4",      "He will wipe every tear from their eyes"),
    ("Isaiah 28:16",       "1 Peter 2:6",          "See, I lay a stone in Zion — a chosen cornerstone"),
    ("Isaiah 40:3-4",      "Luke 3:4-6",           "Prepare the way of the Lord"),
    ("Isaiah 40:6-8",      "1 Peter 1:24-25",      "All flesh is like grass — the word endures forever"),
    ("Isaiah 40:13",       "Romans 11:34",         "Who has known the mind of the Lord?"),
    ("Isaiah 40:13",       "1 Corinthians 2:16",   "We have the mind of Christ"),
    ("Isaiah 42:1-4",      "Matthew 12:17-21",     "My servant whom I uphold — justice for the nations"),
    ("Isaiah 45:23",       "Romans 14:11",         "Every knee will bow, every tongue confess"),
    ("Isaiah 45:23",       "Philippians 2:10-11",  "At the name of Jesus every knee should bow"),
    ("Isaiah 49:6",        "Acts 13:47",           "I have made you a light for the Gentiles"),
    ("Isaiah 52:7",        "Romans 10:15",         "How beautiful are the feet of those who bring good news"),
    ("Isaiah 52:15",       "Romans 15:21",         "Those who were not told about him will see"),
    ("Isaiah 54:1",        "Galatians 4:27",       "Rejoice, barren woman — children of promise"),
    ("Isaiah 56:7",        "Luke 19:46",           "My house shall be called a house of prayer"),
    ("Isaiah 59:20-21",    "Romans 11:26-27",      "The deliverer will come from Zion"),
    ("Isaiah 61:1-2",      "Luke 4:18-19",         "The Spirit of the Lord is on me"),
    ("Isaiah 65:1",        "Romans 10:20",         "Found by those who did not seek me"),
    ("Isaiah 65:2",        "Romans 10:21",         "All day I held out my hands to a disobedient people"),
    # ── Jeremiah / Ezekiel ────────────────────────────────────────────────────
    ("Jeremiah 9:24",      "1 Corinthians 1:31",   "Boast only in knowing the Lord"),
    ("Jeremiah 9:24",      "2 Corinthians 10:17",  "Let the one who boasts boast in the Lord"),
    # ── Minor Prophets ────────────────────────────────────────────────────────
    ("Hosea 11:1",         "Matthew 2:15",         "Out of Egypt I called my son"),
    ("Hosea 13:14",        "1 Corinthians 15:55",  "Where, O death, is your sting?"),
    ("Joel 2:28-32",       "Acts 2:17-21",         "I will pour out my Spirit on all people"),
    ("Joel 2:32",          "Romans 10:13",         "Everyone who calls on the name of the Lord will be saved"),
    ("Amos 9:11-12",       "Acts 15:16-17",        "Restoration of David's fallen tent — Gentiles included"),
    ("Micah 5:2",          "Matthew 2:6",          "Bethlehem — ruler of Israel will come from you"),
    ("Haggai 2:6",         "Hebrews 12:26",        "Once more I will shake not only the earth but the heavens"),
    ("Malachi 4:5-6",      "Luke 1:17",            "Elijah before the great day of the Lord — John the Baptist"),
    # ── Genesis ────────────────────────────────────────────────────────────────
    ("Genesis 3:15",       "Galatians 4:4",        "Seed of the woman — born of a woman under the law"),
    ("Genesis 12:3",       "Acts 3:25",            "All peoples on earth blessed through Abraham's offspring"),
    ("Genesis 22:18",      "Galatians 3:16",       "To Abraham and his Seed — meaning Christ"),
    # ── Deuteronomy ────────────────────────────────────────────────────────────
    ("Deuteronomy 18:15",  "John 6:14",            "The Prophet who is to come into the world"),
    ("Deuteronomy 18:15",  "Acts 3:22",            "God will raise up for you a prophet like me"),
    # ── Daniel ─────────────────────────────────────────────────────────────────
    ("Daniel 7:13-14",     "Matthew 26:64",        "Son of Man coming on the clouds of heaven"),
    ("Daniel 7:13-14",     "Mark 13:26",           "Son of Man coming in clouds with great power"),
    ("Daniel 9:25-26",     "John 11:51",           "The anointed one cut off — atoning death foretold"),
]

# Section G: Additional Quotation Pairs — direct OT quotes in NT epistles
# Format: (ot_ref, nt_ref, label)
QUOTATION_PAIRS_EXTRA = [
    # ── Hebrews — OT citations about Christ ──────────────────────────────────
    ("Psalm 2:7",          "Hebrews 1:5",          "You are my Son; today I have become your Father"),
    ("2 Samuel 7:14",      "Hebrews 1:5",          "I will be his Father, and he will be my Son"),
    ("Psalm 104:4",        "Hebrews 1:7",          "He makes his angels winds and servants flames"),
    ("Psalm 45:6-7",       "Hebrews 1:8-9",        "Your throne, O God, will last forever and ever"),
    ("Psalm 102:25-27",    "Hebrews 1:10-12",      "You laid the foundations of the earth, O Lord"),
    ("Psalm 110:1",        "Hebrews 1:13",         "Sit at my right hand until I make your enemies a footstool"),
    ("Psalm 8:4-6",        "Hebrews 2:6-8",        "What is man that you are mindful of him?"),
    ("Isaiah 8:17-18",     "Hebrews 2:13",         "I will put my trust in him — I and the children"),
    ("Psalm 95:7-11",      "Hebrews 3:7-11",       "Do not harden your hearts as in the rebellion"),
    ("Genesis 2:2",        "Hebrews 4:4",          "God rested on the seventh day from all his works"),
    ("Psalm 110:4",        "Hebrews 5:6",          "You are a priest forever in the order of Melchizedek"),
    ("Genesis 22:17",      "Hebrews 6:14",         "I will surely bless you and give you many descendants"),
    ("Psalm 40:6-8",       "Hebrews 10:5-7",       "Sacrifice and offering you did not desire — I have come"),
    ("Proverbs 3:11-12",   "Hebrews 12:5-6",       "Do not make light of the Lord's discipline"),
    ("Haggai 2:6",         "Hebrews 12:26",        "Once more I will shake the earth and heavens"),
    ("Deuteronomy 31:6",   "Hebrews 13:5",         "Never will I leave you; never will I forsake you"),
    ("Psalm 118:6",        "Hebrews 13:6",         "The Lord is my helper; I will not be afraid"),
    # ── Romans — OT citations ─────────────────────────────────────────────────
    ("Psalm 51:4",         "Romans 3:4",           "So that you may be justified in your words"),
    ("Psalm 14:1-3",       "Romans 3:10-12",       "There is no one righteous, not even one"),
    ("Psalm 5:9",          "Romans 3:13",          "Their throat is an open grave; lips full of deceit"),
    ("Psalm 140:3",        "Romans 3:13",          "The poison of vipers is on their lips"),
    ("Psalm 10:7",         "Romans 3:14",          "Their mouths are full of cursing and bitterness"),
    ("Isaiah 59:7-8",      "Romans 3:15-17",       "Their feet are swift to shed blood"),
    ("Psalm 36:1",         "Romans 3:18",          "There is no fear of God before their eyes"),
    ("Psalm 32:1-2",       "Romans 4:7-8",         "Blessed are those whose transgressions are forgiven"),
    ("Psalm 44:22",        "Romans 8:36",          "For your sake we face death all day long"),
    ("Exodus 33:19",       "Romans 9:15",          "I will have mercy on whom I have mercy"),
    ("Exodus 9:16",        "Romans 9:17",          "I raised you up for this very purpose — Pharaoh"),
    ("Hosea 2:23",         "Romans 9:25",          "I will call them my people who are not my people"),
    ("Hosea 1:10",         "Romans 9:26",          "Children of the living God — Hosea applied to Gentiles"),
    ("Isaiah 10:22-23",    "Romans 9:27-28",       "Though Israel's number be like the sand — a remnant saved"),
    ("Isaiah 1:9",         "Romans 9:29",          "Unless the Lord had left us descendants"),
    ("Deuteronomy 30:12-14","Romans 10:6-8",       "The word is near you — righteousness by faith"),
    ("Isaiah 28:16",       "Romans 10:11",         "Anyone who trusts in him will never be put to shame"),
    ("Joel 2:32",          "Romans 10:13",         "Everyone who calls on the Lord will be saved"),
    ("Isaiah 52:7",        "Romans 10:15",         "How beautiful are the feet of those who bring good news"),
    ("Psalm 19:4",         "Romans 10:18",         "Their voice has gone out into all the earth"),
    ("Deuteronomy 32:21",  "Romans 10:19",         "I will make you envious by a nation not a nation"),
    ("Isaiah 65:1",        "Romans 10:20",         "Found by those who did not seek me"),
    ("Isaiah 65:2",        "Romans 10:21",         "All day long I held out my hands to a disobedient people"),
    ("Isaiah 29:10",       "Romans 11:8",          "God gave them a spirit of stupor — eyes that do not see"),
    ("Psalm 69:22-23",     "Romans 11:9-10",       "May their table become a snare and a trap"),
    ("Isaiah 59:20-21",    "Romans 11:26-27",      "The deliverer will come from Zion and remove ungodliness"),
    ("Isaiah 40:13",       "Romans 11:34",         "Who has known the mind of the Lord?"),
    ("Deuteronomy 32:35",  "Romans 12:19",         "It is mine to avenge; I will repay"),
    ("Proverbs 25:21-22",  "Romans 12:20",         "If your enemy is hungry, feed him — heap burning coals"),
    ("Exodus 20:13-17",    "Romans 13:9",          "Commandments summed up in love for neighbor"),
    ("Isaiah 45:23",       "Romans 14:11",         "Every knee will bow before me, every tongue confess"),
    ("Psalm 18:49",        "Romans 15:9",          "I will praise you among the Gentiles"),
    ("Deuteronomy 32:43",  "Romans 15:10",         "Rejoice, you Gentiles, with his people"),
    ("Psalm 117:1",        "Romans 15:11",         "Praise the Lord, all you Gentiles"),
    ("Isaiah 11:10",       "Romans 15:12",         "The Root of Jesse will stand as a banner for the peoples"),
    # ── 1 Corinthians ─────────────────────────────────────────────────────────
    ("Isaiah 29:14",       "1 Corinthians 1:19",   "I will destroy the wisdom of the wise"),
    ("Jeremiah 9:24",      "1 Corinthians 1:31",   "Let the one who boasts boast in the Lord"),
    ("Isaiah 64:4",        "1 Corinthians 2:9",    "No eye has seen, no ear heard what God has prepared"),
    ("Job 5:13",           "1 Corinthians 3:19",   "He catches the wise in their craftiness"),
    ("Psalm 94:11",        "1 Corinthians 3:20",   "The Lord knows the thoughts of the wise are futile"),
    ("Deuteronomy 25:4",   "1 Corinthians 9:9",    "Do not muzzle an ox while it treads out grain"),
    ("Exodus 32:6",        "1 Corinthians 10:7",   "The people sat to eat and drink and rose to play"),
    ("Psalm 24:1",         "1 Corinthians 10:26",  "The earth is the Lord's and everything in it"),
    ("Isaiah 28:11-12",    "1 Corinthians 14:21",  "Through foreign lips he will speak to this people"),
    ("Psalm 8:6",          "1 Corinthians 15:27",  "God placed all things under his feet"),
    ("Genesis 2:7",        "1 Corinthians 15:45",  "The first man Adam became a living being"),
    ("Hosea 13:14",        "1 Corinthians 15:55",  "Where, O death, is your victory?"),
    # ── 2 Corinthians ─────────────────────────────────────────────────────────
    ("Psalm 116:10",       "2 Corinthians 4:13",   "I believed; therefore I have spoken"),
    ("Isaiah 49:8",        "2 Corinthians 6:2",    "In the time of my favor I heard you"),
    ("Leviticus 26:12",    "2 Corinthians 6:16",   "I will be their God and they will be my people"),
    ("Isaiah 52:11",       "2 Corinthians 6:17",   "Come out from them and be separate"),
    ("2 Samuel 7:14",      "2 Corinthians 6:18",   "I will be a Father to you, and you will be my children"),
    ("Exodus 16:18",       "2 Corinthians 8:15",   "Whoever gathered much did not have too much — manna"),
    ("Psalm 112:9",        "2 Corinthians 9:9",    "He has scattered abroad his gifts to the poor"),
    ("Deuteronomy 19:15",  "2 Corinthians 13:1",   "Every matter established by two or three witnesses"),
    # ── Galatians ─────────────────────────────────────────────────────────────
    ("Genesis 15:6",       "Galatians 3:6",        "Abraham believed God — it was credited as righteousness"),
    ("Deuteronomy 27:26",  "Galatians 3:10",       "Cursed is everyone who does not continue in the law"),
    ("Genesis 21:10",      "Galatians 4:30",       "Get rid of the slave woman — Hagar cast out"),
    ("Leviticus 19:18",    "Galatians 5:14",       "Love your neighbor as yourself"),
    # ── Ephesians ─────────────────────────────────────────────────────────────
    ("Psalm 4:4",          "Ephesians 4:26",       "In your anger do not sin; do not let the sun go down"),
    ("Genesis 2:24",       "Ephesians 5:31",       "A man will leave his parents and be united to his wife"),
    ("Exodus 20:12",       "Ephesians 6:2-3",      "Honor your father and mother — first commandment with promise"),
    # ── 1 Peter ───────────────────────────────────────────────────────────────
    ("Leviticus 11:44",    "1 Peter 1:16",         "Be holy, because I am holy"),
    ("Isaiah 40:6-8",      "1 Peter 1:24-25",      "All flesh is like grass — the word of the Lord endures"),
    ("Exodus 19:5-6",      "1 Peter 2:9",          "A royal priesthood, a holy nation, God's special possession"),
    ("Isaiah 53:9",        "1 Peter 2:22",         "No sin was found in his mouth — no deceit"),
    ("Psalm 34:12-16",     "1 Peter 3:10-12",      "Whoever would love life — turn from evil and do good"),
    ("Isaiah 8:12-13",     "1 Peter 3:14-15",      "Do not fear what they fear — sanctify Christ as Lord"),
    ("Proverbs 11:31",     "1 Peter 4:18",         "If the righteous are barely saved, what of the ungodly?"),
    ("Proverbs 3:34",      "1 Peter 5:5",          "God opposes the proud but shows favor to the humble"),
    # ── James ─────────────────────────────────────────────────────────────────
    ("Leviticus 19:18",    "James 2:8",            "Love your neighbor as yourself — the royal law"),
    ("Genesis 15:6",       "James 2:23",           "Abraham believed God — counted as righteousness"),
    ("Proverbs 3:34",      "James 4:6",            "God opposes the proud but gives grace to the humble"),
    # ── 2 Peter ───────────────────────────────────────────────────────────────
    ("Proverbs 26:11",     "2 Peter 2:22",         "A dog returns to its vomit"),
    # -- Acts -- OT quotations in apostolic speeches ---------------------------
    ("Genesis 12:1",        "Acts 7:3",             "Leave your country and people -- Stephen's speech"),
    ("Genesis 15:14",       "Acts 7:7",             "They will serve as slaves -- Stephen on the exodus"),
    ("Exodus 3:6",          "Acts 7:32",            "I am the God of your fathers -- Stephen's speech"),
    ("Amos 5:25-27",        "Acts 7:42-43",         "Did you bring me sacrifices 40 years -- Stephen's speech"),
    ("Isaiah 66:1-2",       "Acts 7:49-50",         "Heaven is my throne -- Stephen: God does not live in houses made by hands"),
    ("Isaiah 55:3",         "Acts 13:34",           "Holy blessings promised to David -- fulfilled in the resurrection"),
    ("Habakkuk 1:5",        "Acts 13:41",           "Look you scoffers, wonder and perish -- Paul's synagogue warning"),
    ("1 Samuel 13:14",      "Acts 13:22",           "A man after my own heart -- David appointed as king"),
    ("Psalm 34:8",          "1 Peter 2:3",          "Taste and see that the Lord is good -- come to the living Stone"),
    ("Isaiah 65:17",        "2 Peter 3:13",         "New heavens and a new earth -- Peter points to Isaiah's promise"),
    # -- Sermon on the Mount antitheses ----------------------------------------
    ("Exodus 20:13",        "Matthew 5:21",         "Do not murder -- Jesus deepens this to anger and contempt"),
    ("Exodus 20:14",        "Matthew 5:27",         "Do not commit adultery -- Jesus deepens this to lustful intent"),
    ("Deuteronomy 24:1",    "Matthew 5:31",         "Give a certificate of divorce -- Jesus tightens the standard"),
    ("Exodus 21:24",        "Matthew 5:38",         "Eye for an eye -- Jesus calls to non-retaliation"),
    # -- Jesus' key OT quotations -----------------------------------------------
    ("Hosea 6:6",           "Matthew 9:13",         "I desire mercy not sacrifice -- Jesus defends eating with sinners"),
    ("Hosea 6:6",           "Matthew 12:7",         "If you had known what these words mean -- Jesus on the Sabbath"),
    ("Exodus 3:6",          "Matthew 22:32",        "I am the God of Abraham -- God of the living not the dead"),
    ("Exodus 3:6",          "Mark 12:26",           "God of Abraham Isaac and Jacob -- resurrection implied"),
    ("Exodus 3:6",          "Luke 20:37",           "Even Moses showed at the burning bush -- God of the living"),
    ("Genesis 1:27",        "Matthew 19:4",         "Made them male and female -- Jesus on marriage and divorce"),
    ("Genesis 1:27",        "Mark 10:6",            "From the beginning of creation male and female"),
    ("Genesis 2:24",        "Matthew 19:5",         "A man will leave his parents -- Jesus on the permanence of marriage"),
    ("Genesis 2:24",        "Mark 10:7-8",          "Two will become one flesh -- Jesus on divorce"),
    ("Psalm 82:6",          "John 10:34",           "I said you are gods -- Jesus answers the charge of blasphemy"),
    ("Leviticus 19:18",     "Matthew 22:39",        "Love your neighbor as yourself -- second great commandment"),
    ("Leviticus 19:18",     "Mark 12:31",           "Love your neighbor as yourself -- the second commandment"),
    # -- Pastoral Epistles ------------------------------------------------------
    ("Deuteronomy 25:4",    "1 Timothy 5:18",       "Do not muzzle an ox -- the worker deserves his wages"),
    ("Numbers 16:5",        "2 Timothy 2:19",       "The Lord knows those who are his -- Korah's rebellion recalled"),
    ("Psalm 130:8",         "Titus 2:14",           "He will redeem Israel from all iniquity -- Jesus redeems a pure people"),
]

# Section H: OT Typological Fulfillments — the major shadows and types in the
# Pentateuch, historical books, and prophets that the NT explicitly identifies
# as fulfilled or realised in Christ.
# Format: (ot_ref, nt_ref, label)  — same as FULFILLMENT_PAIRS
FULFILLMENT_PAIRS_OT = [
    # ── Genesis — Creation & Covenant types ──────────────────────────────────
    ("Genesis 1:1",        "John 1:1-3",           "In the beginning — all things made through the Word"),
    ("Genesis 1:3",        "2 Corinthians 4:6",    "Let there be light — God shines his light in our hearts"),
    ("Genesis 1:26-27",    "Colossians 1:15",      "Made in the image of God — Christ the image of the invisible God"),
    # ── Genesis — Fall, redemption, promise ──────────────────────────────────
    ("Genesis 3:15",       "Romans 16:20",         "Seed of woman crushes the serpent — God will crush Satan"),
    ("Genesis 3:15",       "Revelation 12:9",      "Ancient serpent — the dragon, that old serpent, cast down"),
    ("Genesis 3:21",       "Hebrews 9:22",         "God covered them with skins — without blood no forgiveness"),
    # ── Genesis — Noah ───────────────────────────────────────────────────────
    ("Genesis 6:13-22",    "1 Peter 3:20-21",      "Noah saved through water — type of baptism that now saves you"),
    # ── Genesis — Abraham and the covenant ───────────────────────────────────
    ("Genesis 12:1-3",     "Acts 3:25",            "All families of earth blessed — fulfilled in Christ's resurrection"),
    ("Genesis 17:10-11",   "Colossians 2:11",      "Physical circumcision — spiritual circumcision in Christ"),
    ("Genesis 22:8",       "John 1:29",            "God will provide the Lamb — Lamb of God who takes away sin"),
    ("Genesis 22:13-14",   "John 3:16",            "Isaac spared, ram in his place — God gave his only Son"),
    # ── Genesis — Melchizedek ────────────────────────────────────────────────
    ("Genesis 14:18-20",   "Hebrews 7:1-10",       "Melchizedek priest of God Most High — type of Christ's priesthood"),
    ("Genesis 14:18-20",   "Hebrews 7:15-17",      "Priest in the order of Melchizedek — Jesus' eternal priesthood"),
    # ── Genesis — Jacob and the ladder ───────────────────────────────────────
    ("Genesis 28:12",      "John 1:51",            "Ladder between heaven and earth — angels ascending on the Son of Man"),
    # ── Genesis — Joseph, a type of Christ ───────────────────────────────────
    ("Genesis 37:3-4",     "John 3:35",            "Father's beloved son rejected by brothers — Son loved by the Father"),
    ("Genesis 41:39-44",   "Philippians 2:9-11",   "Joseph exalted to rule over all — Christ exalted above every name"),
    ("Genesis 50:20",      "Acts 2:23",            "You meant evil — God meant it for good; deliberate plan of God"),
    # ── Genesis — the Lion of Judah ──────────────────────────────────────────
    ("Genesis 49:10",      "Revelation 5:5",       "Lion of Judah, the scepter — the Lamb who is the conquering Lion"),
    ("Genesis 49:10",      "Luke 1:32-33",         "Scepter from Judah forever — throne of David given to Jesus"),
    # ── Exodus — the Passover and Exodus types ───────────────────────────────
    ("Exodus 12:3-7",      "1 Corinthians 5:7",    "Passover lamb slain — Christ our Passover sacrificed for us"),
    ("Exodus 12:46",       "John 19:36",           "No bone of the Passover lamb broken — fulfilled at the cross"),
    ("Exodus 16:4-5",      "John 6:31-35",         "Manna from heaven — Jesus the true bread come down from heaven"),
    ("Exodus 17:5-6",      "1 Corinthians 10:4",   "Water from the rock — that rock was Christ"),
    ("Exodus 24:8",        "Hebrews 9:18-20",      "Blood of the covenant — new covenant sealed by Christ's blood"),
    ("Exodus 25:40",       "Hebrews 8:5",          "Pattern shown on the mountain — tabernacle a shadow of the heavenly"),
    ("Exodus 34:29-35",    "2 Corinthians 3:13-18","Moses' veil over his face — veil removed in Christ"),
    # ── Leviticus — sacrificial system ───────────────────────────────────────
    ("Leviticus 16:15-16", "Hebrews 9:11-12",      "High priest enters Most Holy Place — Christ entered once for all"),
    ("Leviticus 16:27",    "Hebrews 13:12",        "Bodies burned outside the camp — Jesus suffered outside the gate"),
    ("Leviticus 17:11",    "Hebrews 9:22",         "Life is in the blood — without shedding of blood no forgiveness"),
    # ── Numbers ──────────────────────────────────────────────────────────────
    ("Numbers 21:8-9",     "John 3:14-15",         "Bronze serpent lifted up — Son of Man must be lifted up"),
    ("Numbers 24:17",      "Matthew 2:2",          "A star will rise out of Jacob — the Magi follow Christ's star"),
    ("Numbers 24:17",      "Revelation 22:16",     "Star of Jacob — Jesus the bright and Morning Star"),
    # ── Deuteronomy ──────────────────────────────────────────────────────────
    ("Deuteronomy 8:3",    "Matthew 4:4",          "Man shall not live by bread alone — Jesus quotes in temptation"),
    ("Deuteronomy 6:16",   "Matthew 4:7",          "Do not put the Lord to test — Jesus quotes in temptation"),
    ("Deuteronomy 6:13",   "Matthew 4:10",         "Worship the Lord your God only — Jesus quotes in temptation"),
    # ── 2 Samuel — the Davidic covenant ─────────────────────────────────────
    ("2 Samuel 7:12-13",   "Luke 1:32-33",         "David's son on his throne forever — throne given to Jesus"),
    ("2 Samuel 7:12-13",   "Acts 2:30",            "Descendant to sit on David's throne — fulfilled in the resurrection"),
    # ── Psalms (additional types) ────────────────────────────────────────────
    ("Psalm 2:6",          "Acts 13:33",           "I have installed my King on Zion — raised Jesus as declared in Ps 2"),
    ("Psalm 89:3-4",       "Luke 1:69",            "David's line established forever — horn of salvation from David's house"),
    ("Psalm 89:26-27",     "Colossians 1:18",      "My firstborn, highest of the kings — Christ the firstborn from the dead"),
    # ── Isaiah (additional types) ────────────────────────────────────────────
    ("Isaiah 53:5",        "Romans 5:6-8",         "Pierced for our transgressions — Christ died for the ungodly"),
    ("Isaiah 60:1-3",      "Luke 2:32",            "Light for the Gentiles — Simeon: a light of revelation to the Gentiles"),
    # ── Minor prophets (additional) ──────────────────────────────────────────
    ("Micah 5:2",          "Luke 2:4-7",           "From Bethlehem a ruler — Jesus born there of Mary"),
    ("Zechariah 9:9",      "Luke 19:35-38",        "Your king comes on a donkey — Palm Sunday entry in Luke"),
    # -- Jonah -- sign of Jonah ------------------------------------------------
    ("Jonah 1:17",          "Matthew 12:39-40",     "Three days in the fish -- sign of Jonah for this generation"),
    ("Jonah 1:17",          "Luke 11:29-30",        "Sign of Jonah -- as Jonah was a sign to the Ninevites"),
    ("Jonah 3:5-10",        "Luke 11:32",           "Nineveh repented at Jonah's preaching -- greater than Jonah is here"),
    # -- Ezekiel -- fulfilled in Christ ----------------------------------------
    ("Ezekiel 34:11-16",    "John 10:11-16",        "I will search for my sheep -- Jesus the Good Shepherd fulfills this"),
    ("Ezekiel 36:25-27",    "John 3:3-5",           "Sprinkle clean water and give a new spirit -- born of water and Spirit"),
    ("Ezekiel 37:24-25",    "John 10:16",           "One shepherd over them all -- one flock and one shepherd"),
    # -- Numbers -- additional type --------------------------------------------
    ("Numbers 19:9",        "Hebrews 9:13",         "Ashes of the heifer for purifying -- how much more Christ's blood"),
    # -- Isaiah (additional) ---------------------------------------------------
    ("Isaiah 5:1-7",        "John 15:1-8",          "Song of the Vineyard -- Jesus the True Vine replaces unfaithful Israel"),
    ("Isaiah 44:6",         "Revelation 1:17",      "I am the First and the Last -- Jesus claims the divine title"),
    ("Isaiah 65:17",        "Revelation 21:1",      "New heavens and a new earth -- John sees the new creation"),
]

# ── Entry builder ─────────────────────────────────────────────────────────────

def make_entry(parsed, end_v, end_ch, label, entry_type, refs):
    """
    Build a single parallel entry dict.
    parsed  - result of parse_ref() for the anchor ref
    end_v   - end verse string (from parsed endV), or None
    end_ch  - end chapter string (from parsed endCh), or None
    label   - section label string
    entry_type - "parallel" | "fulfillment" | "prophecy-source" | "quotation"
    refs    - list of dicts {"passage": str, "label": str}
    """
    entry = {}
    # end verse: prefer explicit end_v, else use start verse
    if end_v is not None:
        entry['end'] = int(end_v)
    else:
        entry['end'] = int(parsed['v'])

    if end_ch is not None and end_ch != parsed['ch']:
        entry['endCh'] = int(end_ch)

    entry['label'] = label
    entry['type']  = entry_type
    entry['refs']  = refs
    return entry

# ── Accumulator ───────────────────────────────────────────────────────────────
# book_data[bookId][ch_str][v_str] = list of entry dicts

def new_accumulator():
    return defaultdict(lambda: defaultdict(list))

def add_entry(acc, parsed, label, entry_type, refs):
    """Insert an entry into the accumulator for book bookId at ch/v."""
    entry = make_entry(
        parsed,
        parsed['endV'],
        parsed['endCh'],
        label,
        entry_type,
        refs
    )
    acc[parsed['bookId']][parsed['ch']][parsed['v']].append(entry)

# ── Process all data into accumulator ─────────────────────────────────────────

def build_accumulator():
    acc = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    # Section A+B: parallel groups
    for label, ref_strs in PARALLEL_GROUPS:
        parsed_refs = []
        for rs in ref_strs:
            p = parse_ref(rs)
            if p is None:
                print(f'  WARN: cannot parse ref "{rs}" in group "{label}" — skipping ref', file=sys.stderr)
            else:
                parsed_refs.append((rs, p))

        # For each ref_i, create entry pointing to all other refs
        for i, (rs_i, p_i) in enumerate(parsed_refs):
            other_refs = [
                {"passage": rs_j, "label": label}
                for j, (rs_j, p_j) in enumerate(parsed_refs)
                if j != i
            ]
            if not other_refs:
                continue
            entry = make_entry(p_i, p_i['endV'], p_i['endCh'], label, 'parallel', other_refs)
            acc[p_i['bookId']][p_i['ch']][p_i['v']].append(entry)

    # Section C: fulfillment pairs
    for ot_str, nt_str, label in FULFILLMENT_PAIRS:
        p_ot = parse_ref(ot_str)
        p_nt = parse_ref(nt_str)
        if p_ot is None:
            print(f'  WARN: cannot parse OT ref "{ot_str}" in fulfillment "{label}" — skipping', file=sys.stderr)
            continue
        if p_nt is None:
            print(f'  WARN: cannot parse NT ref "{nt_str}" in fulfillment "{label}" — skipping', file=sys.stderr)
            continue

        # OT entry: type="fulfillment", points to NT
        entry_ot = make_entry(p_ot, p_ot['endV'], p_ot['endCh'], label, 'fulfillment',
                              [{"passage": nt_str, "label": label}])
        acc[p_ot['bookId']][p_ot['ch']][p_ot['v']].append(entry_ot)

        # NT entry: type="prophecy-source", points to OT
        entry_nt = make_entry(p_nt, p_nt['endV'], p_nt['endCh'], label, 'prophecy-source',
                              [{"passage": ot_str, "label": label}])
        acc[p_nt['bookId']][p_nt['ch']][p_nt['v']].append(entry_nt)

    # Section D: quotation pairs
    for ot_str, nt_str, label in QUOTATION_PAIRS:
        p_ot = parse_ref(ot_str)
        p_nt = parse_ref(nt_str)
        if p_ot is None:
            print(f'  WARN: cannot parse OT ref "{ot_str}" in quotation "{label}" — skipping', file=sys.stderr)
            continue
        if p_nt is None:
            print(f'  WARN: cannot parse NT ref "{nt_str}" in quotation "{label}" — skipping', file=sys.stderr)
            continue

        # OT entry: this OT passage is the source being quoted
        entry_ot = make_entry(p_ot, p_ot['endV'], p_ot['endCh'], label, 'quotation-source',
                              [{"passage": nt_str, "label": label}])
        acc[p_ot['bookId']][p_ot['ch']][p_ot['v']].append(entry_ot)

        # NT entry: this NT passage does the quoting
        entry_nt = make_entry(p_nt, p_nt['endV'], p_nt['endCh'], label, 'quotation',
                              [{"passage": ot_str, "label": label}])
        acc[p_nt['bookId']][p_nt['ch']][p_nt['v']].append(entry_nt)

    # Section E: allusion pairs — NT alludes to OT; OT is the source being alluded to
    for nt_str, ot_str, label in ALLUSION_PAIRS:
        p_nt = parse_ref(nt_str)
        p_ot = parse_ref(ot_str)
        if p_nt is None:
            print(f'  WARN: cannot parse NT ref "{nt_str}" in allusion "{label}" — skipping', file=sys.stderr)
            continue
        if p_ot is None:
            print(f'  WARN: cannot parse OT ref "{ot_str}" in allusion "{label}" — skipping', file=sys.stderr)
            continue
        entry_nt = make_entry(p_nt, p_nt['endV'], p_nt['endCh'], label, 'allusion',
                              [{"passage": ot_str, "label": label}])
        acc[p_nt['bookId']][p_nt['ch']][p_nt['v']].append(entry_nt)
        # OT gets allusion-source: this passage is referenced in the NT
        entry_ot = make_entry(p_ot, p_ot['endV'], p_ot['endCh'], label, 'allusion-source',
                              [{"passage": nt_str, "label": label}])
        acc[p_ot['bookId']][p_ot['ch']][p_ot['v']].append(entry_ot)

    # Section F: additional fulfillment pairs (same logic as Section C)
    for ot_str, nt_str, label in FULFILLMENT_PAIRS_EXTRA:
        p_ot = parse_ref(ot_str)
        p_nt = parse_ref(nt_str)
        if p_ot is None:
            print(f'  WARN: cannot parse OT ref "{ot_str}" in fulfillment_extra "{label}" — skipping', file=sys.stderr)
            continue
        if p_nt is None:
            print(f'  WARN: cannot parse NT ref "{nt_str}" in fulfillment_extra "{label}" — skipping', file=sys.stderr)
            continue
        entry_ot = make_entry(p_ot, p_ot['endV'], p_ot['endCh'], label, 'fulfillment',
                              [{"passage": nt_str, "label": label}])
        acc[p_ot['bookId']][p_ot['ch']][p_ot['v']].append(entry_ot)
        entry_nt = make_entry(p_nt, p_nt['endV'], p_nt['endCh'], label, 'prophecy-source',
                              [{"passage": ot_str, "label": label}])
        acc[p_nt['bookId']][p_nt['ch']][p_nt['v']].append(entry_nt)

    # Section G: additional quotation pairs (same logic as Section D)
    for ot_str, nt_str, label in QUOTATION_PAIRS_EXTRA:
        p_ot = parse_ref(ot_str)
        p_nt = parse_ref(nt_str)
        if p_ot is None:
            print(f'  WARN: cannot parse OT ref "{ot_str}" in quotation_extra "{label}" — skipping', file=sys.stderr)
            continue
        if p_nt is None:
            print(f'  WARN: cannot parse NT ref "{nt_str}" in quotation_extra "{label}" — skipping', file=sys.stderr)
            continue
        entry_ot = make_entry(p_ot, p_ot['endV'], p_ot['endCh'], label, 'quotation-source',
                              [{"passage": nt_str, "label": label}])
        acc[p_ot['bookId']][p_ot['ch']][p_ot['v']].append(entry_ot)
        entry_nt = make_entry(p_nt, p_nt['endV'], p_nt['endCh'], label, 'quotation',
                              [{"passage": ot_str, "label": label}])
        acc[p_nt['bookId']][p_nt['ch']][p_nt['v']].append(entry_nt)

    # Section H: OT typological fulfillments (same logic as Section C/F)
    for ot_str, nt_str, label in FULFILLMENT_PAIRS_OT:
        p_ot = parse_ref(ot_str)
        p_nt = parse_ref(nt_str)
        if p_ot is None:
            print(f'  WARN: cannot parse OT ref "{ot_str}" in ot_fulfillment "{label}" — skipping', file=sys.stderr)
            continue
        if p_nt is None:
            print(f'  WARN: cannot parse NT ref "{nt_str}" in ot_fulfillment "{label}" — skipping', file=sys.stderr)
            continue
        entry_ot = make_entry(p_ot, p_ot['endV'], p_ot['endCh'], label, 'fulfillment',
                              [{"passage": nt_str, "label": label}])
        acc[p_ot['bookId']][p_ot['ch']][p_ot['v']].append(entry_ot)
        entry_nt = make_entry(p_nt, p_nt['endV'], p_nt['endCh'], label, 'prophecy-source',
                              [{"passage": ot_str, "label": label}])
        acc[p_nt['bookId']][p_nt['ch']][p_nt['v']].append(entry_nt)

    return acc

# ── Serialise ─────────────────────────────────────────────────────────────────

def serialise_book(book_acc):
    """
    Convert a book's defaultdict(defaultdict(list)) into a plain dict
    with chapters and verses sorted numerically.
    """
    out = {}
    for ch in sorted(book_acc.keys(), key=lambda x: int(x)):
        out[ch] = {}
        for v in sorted(book_acc[ch].keys(), key=lambda x: int(x)):
            out[ch][v] = book_acc[ch][v]
    return out

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    force = '--force' in args
    filter_books = [a.lower().replace(' ', '') for a in args if not a.startswith('--')]

    os.makedirs(OUT_DIR, exist_ok=True)

    print('Building parallel data...')
    acc = build_accumulator()

    books_written = 0
    books_skipped = 0

    for book_id, book_acc in sorted(acc.items()):
        # Apply book filter
        if filter_books:
            # match if the bookId contains any of the filter terms
            if not any(f in book_id for f in filter_books):
                continue

        out_path = os.path.join(OUT_DIR, f'{book_id}.json')

        if os.path.exists(out_path) and not force:
            print(f'  skip  {book_id}.json (exists; use --force to overwrite)')
            books_skipped += 1
            continue

        data = serialise_book(book_acc)
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, separators=(',', ':'))

        # Count total entries for summary
        total = sum(len(vs) for ch in data.values() for vs in ch.values())
        print(f'  wrote {book_id}.json  ({total} entries)')
        books_written += 1

    print(f'\nDone. {books_written} file(s) written, {books_skipped} skipped.')

if __name__ == '__main__':
    main()
