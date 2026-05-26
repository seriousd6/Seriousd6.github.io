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

        # OT entry
        entry_ot = make_entry(p_ot, p_ot['endV'], p_ot['endCh'], label, 'quotation',
                              [{"passage": nt_str, "label": label}])
        acc[p_ot['bookId']][p_ot['ch']][p_ot['v']].append(entry_ot)

        # NT entry
        entry_nt = make_entry(p_nt, p_nt['endV'], p_nt['endCh'], label, 'quotation',
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
