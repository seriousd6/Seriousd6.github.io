#!/usr/bin/env python3
"""
Enrich all 66 book intro JSONs with improved timeline data:
  - timeline.period   — one of 11 redemptive-historical eras
  - timeline.before   — expanded to 3 items with {label, ref?, year?, type}
  - timeline.after    — expanded to 3 items with {label, ref?, year?, type}

Types: "book" | "event" | "world"
Run: python3 scripts/enrich-timelines.py [--overwrite]
"""
import json, os, sys

OUT = os.path.join(os.path.dirname(__file__), '..', 'data', 'books', 'introductions')
OVERWRITE = '--overwrite' in sys.argv

# period values must match JS ERAS array slugs exactly
# "creation" | "patriarchs" | "moses" | "conquest" | "monarchy" | "exile"
# | "restoration" | "intertestamental" | "gospels" | "church" | "consummation"

TIMELINES = {
  "genesis": {
    "period": "patriarchs",
    "date": "Events: ~4000–1700 BC",
    "before": [
      {"label": "Before creation: the eternal God", "year": "Eternity", "type": "event"},
    ],
    "after": [
      {"label": "The Exodus from Egypt", "ref": "Exodus 3:1", "year": "c. 1446 BC", "type": "event"},
      {"label": "Sinai Covenant — God's law given to Israel", "ref": "Exodus 19:1", "year": "c. 1446 BC", "type": "event"},
      {"label": "Israel enters the Promised Land", "ref": "Joshua 1:1", "year": "c. 1406 BC", "type": "event"},
    ]
  },
  "exodus": {
    "period": "moses",
    "date": "Events: c. 1446 BC",
    "before": [
      {"label": "Jacob's family settles in Egypt", "ref": "Genesis 46:1", "year": "c. 1700 BC", "type": "event"},
      {"label": "Israel enslaved under a new Pharaoh", "ref": "Exodus 1:8", "year": "c. 1570 BC", "type": "event"},
      {"label": "God's covenant with Abraham, Isaac, Jacob", "ref": "Genesis 15:1", "year": "c. 2000 BC", "type": "event"},
    ],
    "after": [
      {"label": "Leviticus — Israel's worship system established", "ref": "Leviticus 1:1", "year": "c. 1446 BC", "type": "book"},
      {"label": "Numbers — forty years in the wilderness", "ref": "Numbers 1:1", "year": "c. 1446–1406 BC", "type": "book"},
      {"label": "Tabernacle completed; God's glory fills it", "ref": "Exodus 40:34", "year": "c. 1445 BC", "type": "event"},
    ]
  },
  "leviticus": {
    "period": "moses",
    "date": "c. 1446 BC (Sinai)",
    "before": [
      {"label": "Israel redeemed from Egypt by the Passover lamb", "ref": "Exodus 12:1", "year": "c. 1446 BC", "type": "event"},
      {"label": "The Sinai covenant ratified in blood", "ref": "Exodus 24:1", "year": "c. 1446 BC", "type": "event"},
      {"label": "Tabernacle constructed and consecrated", "ref": "Exodus 40:1", "year": "c. 1445 BC", "type": "event"},
    ],
    "after": [
      {"label": "Numbers — wilderness census and journey", "ref": "Numbers 1:1", "year": "c. 1446 BC", "type": "book"},
      {"label": "Aaron's sons Nadab and Abihu judged", "ref": "Leviticus 10:1", "year": "c. 1446 BC", "type": "event"},
      {"label": "Day of Atonement established as annual rite", "ref": "Leviticus 16:1", "year": "c. 1446 BC", "type": "event"},
    ]
  },
  "numbers": {
    "period": "moses",
    "date": "Events: c. 1446–1406 BC",
    "before": [
      {"label": "Israel at Sinai — law and tabernacle given", "ref": "Leviticus 27:34", "year": "c. 1446 BC", "type": "event"},
      {"label": "The wilderness generation numbered", "ref": "Numbers 1:1", "year": "c. 1445 BC", "type": "event"},
      {"label": "Spies sent into Canaan; the people rebel", "ref": "Numbers 13:1", "year": "c. 1444 BC", "type": "event"},
    ],
    "after": [
      {"label": "Deuteronomy — Moses' final sermons before death", "ref": "Deuteronomy 1:1", "year": "c. 1406 BC", "type": "book"},
      {"label": "New generation numbered for conquest", "ref": "Numbers 26:1", "year": "c. 1406 BC", "type": "event"},
      {"label": "Israel enters Canaan under Joshua", "ref": "Joshua 1:1", "year": "c. 1406 BC", "type": "event"},
    ]
  },
  "deuteronomy": {
    "period": "moses",
    "date": "c. 1406 BC (Plains of Moab)",
    "before": [
      {"label": "Forty years of wilderness wandering end", "ref": "Numbers 33:1", "year": "c. 1406 BC", "type": "event"},
      {"label": "The wilderness generation dies; new generation ready", "ref": "Numbers 26:64", "year": "c. 1406 BC", "type": "event"},
      {"label": "Sinai covenant given — law and tabernacle", "ref": "Exodus 19:1", "year": "c. 1446 BC", "type": "event"},
    ],
    "after": [
      {"label": "Moses dies; Joshua leads Israel into Canaan", "ref": "Joshua 1:1", "year": "c. 1406 BC", "type": "event"},
      {"label": "Joshua — conquest and settlement of the land", "ref": "Joshua 1:2", "year": "c. 1406–1380 BC", "type": "book"},
      {"label": "Covenant renewed at Shechem under Joshua", "ref": "Joshua 24:1", "year": "c. 1380 BC", "type": "event"},
    ]
  },
  "joshua": {
    "period": "conquest",
    "date": "Events: c. 1406–1380 BC",
    "before": [
      {"label": "Moses' death; Joshua commissioned as his successor", "ref": "Deuteronomy 34:1", "year": "c. 1406 BC", "type": "event"},
      {"label": "Deuteronomy — covenant renewed before entering the land", "ref": "Deuteronomy 1:1", "year": "c. 1406 BC", "type": "book"},
      {"label": "God's promise of the land to Abraham's descendants", "ref": "Genesis 12:7", "year": "c. 2000 BC", "type": "event"},
    ],
    "after": [
      {"label": "Joshua's death; covenant faithfulness tested", "ref": "Judges 1:1", "year": "c. 1380 BC", "type": "event"},
      {"label": "Judges — cycles of apostasy and deliverance", "ref": "Judges 2:1", "year": "c. 1380–1050 BC", "type": "book"},
      {"label": "Land distributed among the twelve tribes", "ref": "Joshua 13:1", "year": "c. 1400 BC", "type": "event"},
    ]
  },
  "judges": {
    "period": "conquest",
    "date": "Events: c. 1380–1050 BC",
    "before": [
      {"label": "Joshua dies; tribal settlement incomplete", "ref": "Judges 1:1", "year": "c. 1380 BC", "type": "event"},
      {"label": "Covenant at Shechem — Israel pledges loyalty", "ref": "Joshua 24:15", "year": "c. 1380 BC", "type": "event"},
      {"label": "Joshua — Promised Land entered and divided", "ref": "Joshua 1:1", "year": "c. 1406 BC", "type": "book"},
    ],
    "after": [
      {"label": "Ruth — faithful loyalty in the dark days of the judges", "ref": "Ruth 1:1", "year": "c. 1100 BC", "type": "book"},
      {"label": "Samuel born; Eli's corrupt priesthood ends", "ref": "1 Samuel 1:1", "year": "c. 1100 BC", "type": "event"},
      {"label": "Israel demands a king", "ref": "1 Samuel 8:5", "year": "c. 1050 BC", "type": "event"},
    ]
  },
  "ruth": {
    "period": "conquest",
    "date": "Events: c. 1100 BC",
    "before": [
      {"label": "The period of the judges — moral darkness and apostasy", "ref": "Judges 21:25", "year": "c. 1380–1050 BC", "type": "event"},
      {"label": "Judges — cycles of faithlessness and deliverance", "ref": "Judges 2:11", "year": "c. 1380 BC", "type": "book"},
      {"label": "Boaz's ancestor Rahab shelters the Israelite spies", "ref": "Joshua 2:1", "year": "c. 1406 BC", "type": "event"},
    ],
    "after": [
      {"label": "Obed born — David's grandfather in Bethlehem", "ref": "Ruth 4:17", "year": "c. 1080 BC", "type": "event"},
      {"label": "1 Samuel — Samuel, Saul, and the rise of David", "ref": "1 Samuel 1:1", "year": "c. 1105 BC", "type": "book"},
      {"label": "David anointed king; dynasty established", "ref": "1 Samuel 16:13", "year": "c. 1025 BC", "type": "event"},
    ]
  },
  "1samuel": {
    "period": "monarchy",
    "date": "Events: c. 1105–1010 BC",
    "before": [
      {"label": "Eli's corrupt priesthood; ark of the covenant captured", "ref": "1 Samuel 4:11", "year": "c. 1080 BC", "type": "event"},
      {"label": "Judges — Israel's final judge-era cycles", "ref": "Judges 21:25", "year": "c. 1050 BC", "type": "book"},
      {"label": "Ruth — David's ancestry through Boaz and Ruth", "ref": "Ruth 4:17", "year": "c. 1100 BC", "type": "event"},
    ],
    "after": [
      {"label": "2 Samuel — David's reign over united Israel", "ref": "2 Samuel 1:1", "year": "c. 1010 BC", "type": "book"},
      {"label": "Saul's kingship ends in failure and death", "ref": "1 Samuel 31:6", "year": "c. 1010 BC", "type": "event"},
      {"label": "David anointed king over all Israel", "ref": "2 Samuel 5:3", "year": "c. 1003 BC", "type": "event"},
    ]
  },
  "2samuel": {
    "period": "monarchy",
    "date": "Events: c. 1010–971 BC",
    "before": [
      {"label": "Saul's death; David mourns and is anointed king", "ref": "2 Samuel 1:1", "year": "c. 1010 BC", "type": "event"},
      {"label": "1 Samuel — Samuel, Saul, and David's anointing", "ref": "1 Samuel 1:1", "year": "c. 1105 BC", "type": "book"},
      {"label": "The ark of the covenant brought to Jerusalem", "ref": "2 Samuel 6:1", "year": "c. 1003 BC", "type": "event"},
    ],
    "after": [
      {"label": "1 Kings — Solomon's temple, wisdom, and apostasy", "ref": "1 Kings 1:1", "year": "c. 971 BC", "type": "book"},
      {"label": "Davidic Covenant — an eternal throne promised", "ref": "2 Samuel 7:12", "year": "c. 1000 BC", "type": "event"},
      {"label": "Solomon born; Bathsheba's son becomes heir", "ref": "2 Samuel 12:24", "year": "c. 990 BC", "type": "event"},
    ]
  },
  "1kings": {
    "period": "monarchy",
    "date": "Events: c. 971–853 BC",
    "before": [
      {"label": "David's reign — Jerusalem established as capital", "ref": "2 Samuel 5:9", "year": "c. 1003 BC", "type": "event"},
      {"label": "Davidic Covenant — promise of an eternal throne", "ref": "2 Samuel 7:12", "year": "c. 1000 BC", "type": "event"},
      {"label": "2 Samuel — David's wars, failures, and faithfulness", "ref": "2 Samuel 1:1", "year": "c. 1010 BC", "type": "book"},
    ],
    "after": [
      {"label": "2 Kings — the decline and fall of both kingdoms", "ref": "2 Kings 1:1", "year": "c. 853 BC", "type": "book"},
      {"label": "Kingdom divides under Rehoboam; Jeroboam's golden calves", "ref": "1 Kings 12:1", "year": "c. 931 BC", "type": "event"},
      {"label": "Elijah confronts Ahab and Baal worship at Carmel", "ref": "1 Kings 18:1", "year": "c. 869 BC", "type": "event"},
    ]
  },
  "2kings": {
    "period": "exile",
    "date": "Events: c. 853–561 BC",
    "before": [
      {"label": "1 Kings — Solomon, division of the kingdom, Elijah", "ref": "1 Kings 1:1", "year": "c. 971 BC", "type": "book"},
      {"label": "Elijah taken up to heaven; Elisha's ministry begins", "ref": "2 Kings 2:11", "year": "c. 850 BC", "type": "event"},
      {"label": "Assyria rises as the dominant world power", "ref": "2 Kings 15:29", "year": "c. 745 BC", "type": "world"},
    ],
    "after": [
      {"label": "Fall of Samaria — Israel exiled to Assyria", "ref": "2 Kings 17:6", "year": "722 BC", "type": "event"},
      {"label": "Fall of Jerusalem — Judah exiled to Babylon", "ref": "2 Kings 25:11", "year": "587 BC", "type": "event"},
      {"label": "Ezra — return from exile under Cyrus", "ref": "Ezra 1:1", "year": "c. 538 BC", "type": "book"},
    ]
  },
  "1chronicles": {
    "period": "restoration",
    "date": "Written: c. 450–400 BC (covers ~2000–971 BC)",
    "before": [
      {"label": "Return from exile under Zerubbabel", "ref": "Ezra 2:1", "year": "c. 538 BC", "type": "event"},
      {"label": "Temple foundation laid; rebuilding stalls for 16 years", "ref": "Ezra 3:10", "year": "c. 536 BC", "type": "event"},
      {"label": "2 Samuel — David's reign; the events Chronicles revisits", "ref": "2 Samuel 5:1", "year": "c. 1010 BC", "type": "book"},
    ],
    "after": [
      {"label": "2 Chronicles — Solomon through the fall of Jerusalem", "ref": "2 Chronicles 1:1", "year": "c. 450 BC", "type": "book"},
      {"label": "David prepares the temple order; Levitical guilds organized", "ref": "1 Chronicles 25:1", "year": "c. 990 BC", "type": "event"},
      {"label": "Ezra — the post-exilic community reconstituted", "ref": "Ezra 1:1", "year": "c. 538 BC", "type": "book"},
    ]
  },
  "2chronicles": {
    "period": "restoration",
    "date": "Written: c. 450–400 BC (covers ~971–538 BC)",
    "before": [
      {"label": "1 Chronicles — David's preparations and the temple vision", "ref": "1 Chronicles 29:1", "year": "c. 450 BC", "type": "book"},
      {"label": "Solomon builds and dedicates the temple", "ref": "1 Kings 8:1", "year": "c. 959 BC", "type": "event"},
      {"label": "Return from exile; temple rebuilding begins", "ref": "Ezra 1:1", "year": "c. 538 BC", "type": "event"},
    ],
    "after": [
      {"label": "Cyrus's decree — 'Let him go up'", "ref": "2 Chronicles 36:23", "year": "538 BC", "type": "event"},
      {"label": "Ezra — return, temple completion, Torah restoration", "ref": "Ezra 1:1", "year": "c. 458 BC", "type": "book"},
      {"label": "Nehemiah — walls rebuilt, covenant renewed", "ref": "Nehemiah 1:1", "year": "c. 445 BC", "type": "book"},
    ]
  },
  "ezra": {
    "period": "restoration",
    "date": "Events: c. 538–458 BC",
    "before": [
      {"label": "Fall of Babylon to Persia under Cyrus", "ref": "2 Chronicles 36:22", "year": "539 BC", "type": "world"},
      {"label": "Jeremiah's seventy-year exile prophecy fulfilled", "ref": "Jeremiah 25:11", "year": "538 BC", "type": "event"},
      {"label": "Zerubbabel leads the first wave of exiles home", "ref": "Ezra 2:2", "year": "c. 538 BC", "type": "event"},
    ],
    "after": [
      {"label": "Temple completed and dedicated", "ref": "Ezra 6:16", "year": "516 BC", "type": "event"},
      {"label": "Nehemiah rebuilds Jerusalem's walls", "ref": "Nehemiah 2:17", "year": "c. 445 BC", "type": "event"},
      {"label": "Ezra publicly reads the Law — covenant renewal", "ref": "Nehemiah 8:1", "year": "c. 444 BC", "type": "event"},
    ]
  },
  "nehemiah": {
    "period": "restoration",
    "date": "Events: c. 445–430 BC",
    "before": [
      {"label": "Ezra returns to Jerusalem; temple in operation", "ref": "Ezra 7:1", "year": "c. 458 BC", "type": "event"},
      {"label": "Jerusalem's walls still broken sixty years after the return", "ref": "Nehemiah 1:3", "year": "c. 445 BC", "type": "event"},
      {"label": "Ezra — Torah restoration and community reformation", "ref": "Ezra 1:1", "year": "c. 538 BC", "type": "book"},
    ],
    "after": [
      {"label": "Ezra reads the Law publicly; the people weep", "ref": "Nehemiah 8:8", "year": "c. 444 BC", "type": "event"},
      {"label": "Malachi — last OT prophet challenges the restored community", "ref": "Malachi 1:1", "year": "c. 450–430 BC", "type": "book"},
      {"label": "Four hundred years of prophetic silence begin", "ref": "Malachi 4:6", "year": "c. 430 BC", "type": "event"},
    ]
  },
  "esther": {
    "period": "restoration",
    "date": "Events: c. 483–479 BC",
    "before": [
      {"label": "Jews remain scattered in Persia after Cyrus's decree", "ref": "Ezra 1:3", "year": "c. 538 BC", "type": "event"},
      {"label": "Ahasuerus (Xerxes I) reigns over the Persian empire", "ref": "Esther 1:1", "year": "c. 486 BC", "type": "world"},
      {"label": "Ezra — the temple rebuilt; some Jews remain in diaspora", "ref": "Ezra 6:16", "year": "516 BC", "type": "event"},
    ],
    "after": [
      {"label": "Feast of Purim established as a perpetual memorial", "ref": "Esther 9:26", "year": "c. 479 BC", "type": "event"},
      {"label": "Ezra journeys to Jerusalem to restore the Torah", "ref": "Ezra 7:9", "year": "c. 458 BC", "type": "event"},
      {"label": "Nehemiah rebuilds Jerusalem's walls", "ref": "Nehemiah 2:17", "year": "c. 445 BC", "type": "event"},
    ]
  },
  "job": {
    "period": "patriarchs",
    "date": "Setting: Patriarchal era (~2000–1700 BC?)",
    "before": [
      {"label": "Creation: God makes the good world and its inhabitants", "ref": "Genesis 1:1", "year": "Primeval", "type": "event"},
      {"label": "The fall: suffering, toil, and death enter creation", "ref": "Genesis 3:17", "year": "Primeval", "type": "event"},
      {"label": "Abraham called; the covenant promises given", "ref": "Genesis 12:1", "year": "c. 2000 BC", "type": "event"},
    ],
    "after": [
      {"label": "The Psalms — wisdom and lament in the covenant community", "ref": "Psalms 1:1", "year": "c. 1000 BC", "type": "book"},
      {"label": "Proverbs — creation-order wisdom and the fear of the LORD", "ref": "Proverbs 1:7", "year": "c. 950 BC", "type": "book"},
      {"label": "Ecclesiastes — the limits of wisdom under the sun", "ref": "Ecclesiastes 1:2", "year": "c. 935 BC", "type": "book"},
    ]
  },
  "psalms": {
    "period": "monarchy",
    "date": "Composed: c. 1000–400 BC",
    "before": [
      {"label": "David anointed king; covenant with Abraham's line", "ref": "2 Samuel 7:12", "year": "c. 1000 BC", "type": "event"},
      {"label": "The Tabernacle established as the centre of worship", "ref": "Exodus 40:34", "year": "c. 1445 BC", "type": "event"},
      {"label": "2 Samuel — David's reign; his psalms composed in its context", "ref": "2 Samuel 1:1", "year": "c. 1010 BC", "type": "book"},
    ],
    "after": [
      {"label": "Solomon's temple — Psalms sung in formal temple worship", "ref": "1 Kings 8:1", "year": "c. 959 BC", "type": "event"},
      {"label": "Jesus quotes or alludes to Psalms more than any other OT book", "ref": "Matthew 22:44", "year": "c. AD 30", "type": "event"},
      {"label": "Revelation — heavenly worship draws on the Psalms", "ref": "Revelation 15:3", "year": "c. AD 95", "type": "event"},
    ]
  },
  "proverbs": {
    "period": "monarchy",
    "date": "Composed: c. 950–700 BC",
    "before": [
      {"label": "Solomon's God-given wisdom at Gibeon", "ref": "1 Kings 3:9", "year": "c. 960 BC", "type": "event"},
      {"label": "Psalms — Israel's hymnbook and wisdom poetry", "ref": "Psalms 1:1", "year": "c. 1000 BC", "type": "book"},
      {"label": "Creation: God establishes the order that wisdom discerns", "ref": "Genesis 1:1", "year": "Primeval", "type": "event"},
    ],
    "after": [
      {"label": "Ecclesiastes — wisdom tested to its limits", "ref": "Ecclesiastes 1:2", "year": "c. 935 BC", "type": "book"},
      {"label": "Jesus as Wisdom incarnate — 'something greater than Solomon'", "ref": "Matthew 12:42", "year": "c. AD 29", "type": "event"},
      {"label": "James — the NT wisdom letter applying Proverbs' ethics", "ref": "James 1:5", "year": "c. AD 48", "type": "book"},
    ]
  },
  "ecclesiastes": {
    "period": "monarchy",
    "date": "c. 935 BC or later (Solomonic persona)",
    "before": [
      {"label": "Proverbs — wisdom's positive side: the fear of the LORD", "ref": "Proverbs 1:7", "year": "c. 950 BC", "type": "book"},
      {"label": "Solomon's wealth and achievement at their peak", "ref": "1 Kings 10:23", "year": "c. 950 BC", "type": "event"},
      {"label": "Job — suffering and the limits of human understanding", "ref": "Job 38:1", "year": "Patriarchal era", "type": "book"},
    ],
    "after": [
      {"label": "Song of Solomon — human love as God's good gift", "ref": "Song of Solomon 1:1", "year": "c. 935 BC", "type": "book"},
      {"label": "Resurrection and resurrection hope — death answered", "ref": "1 Corinthians 15:54", "year": "c. AD 54", "type": "event"},
      {"label": "Romans — God's purposes are not vanity but glory", "ref": "Romans 8:20", "year": "c. AD 57", "type": "event"},
    ]
  },
  "songofsolomon": {
    "period": "monarchy",
    "date": "c. 935 BC (Solomonic)",
    "before": [
      {"label": "Genesis — marriage given as God's good gift at creation", "ref": "Genesis 2:24", "year": "Primeval", "type": "event"},
      {"label": "Proverbs — the worthy woman and the call of Wisdom", "ref": "Proverbs 31:10", "year": "c. 950 BC", "type": "book"},
      {"label": "Hosea — God's covenant love as marriage", "ref": "Hosea 2:19", "year": "c. 755 BC", "type": "book"},
    ],
    "after": [
      {"label": "Isaiah — covenant as marriage: God betrothed to his people", "ref": "Isaiah 54:5", "year": "c. 740 BC", "type": "event"},
      {"label": "Ephesians — marriage as an image of Christ and the church", "ref": "Ephesians 5:32", "year": "c. AD 60", "type": "event"},
      {"label": "Revelation — the marriage supper of the Lamb", "ref": "Revelation 19:7", "year": "c. AD 95", "type": "event"},
    ]
  },
  "isaiah": {
    "period": "exile",
    "date": "c. 740–680 BC",
    "before": [
      {"label": "Uzziah's death — the stable era of Judah's prosperity ends", "ref": "Isaiah 6:1", "year": "740 BC", "type": "event"},
      {"label": "Fall of Samaria — northern Israel exiled to Assyria", "ref": "2 Kings 17:6", "year": "722 BC", "type": "event"},
      {"label": "Amos and Hosea preach judgment in the northern kingdom", "ref": "Amos 1:1", "year": "c. 760–750 BC", "type": "event"},
    ],
    "after": [
      {"label": "Sennacherib's siege of Jerusalem; Hezekiah's prayer", "ref": "Isaiah 37:1", "year": "701 BC", "type": "event"},
      {"label": "Jeremiah — the fall of Jerusalem and exile to Babylon", "ref": "Jeremiah 1:1", "year": "c. 627 BC", "type": "book"},
      {"label": "Cyrus's decree of return — Isaiah's prophecy fulfilled", "ref": "Ezra 1:1", "year": "538 BC", "type": "event"},
    ]
  },
  "jeremiah": {
    "period": "exile",
    "date": "c. 627–580 BC",
    "before": [
      {"label": "Josiah's reform — the last window for national repentance", "ref": "2 Chronicles 34:1", "year": "c. 621 BC", "type": "event"},
      {"label": "Isaiah — judgment and redemption announced a century earlier", "ref": "Isaiah 1:1", "year": "c. 740 BC", "type": "book"},
      {"label": "Josiah dies at Megiddo; reform unravels", "ref": "2 Chronicles 35:23", "year": "609 BC", "type": "event"},
    ],
    "after": [
      {"label": "Fall of Jerusalem; temple destroyed by Nebuchadnezzar", "ref": "Jeremiah 52:12", "year": "587 BC", "type": "event"},
      {"label": "Lamentations — grief over Jerusalem's destruction", "ref": "Lamentations 1:1", "year": "c. 587 BC", "type": "book"},
      {"label": "New Covenant fulfilled in Christ's Last Supper", "ref": "Luke 22:20", "year": "c. AD 30", "type": "event"},
    ]
  },
  "lamentations": {
    "period": "exile",
    "date": "c. 587 BC",
    "before": [
      {"label": "Jerusalem falls — walls breached, temple destroyed, king blinded", "ref": "Jeremiah 52:12", "year": "587 BC", "type": "event"},
      {"label": "Jeremiah's decades of unheeded warnings fulfilled", "ref": "Jeremiah 7:14", "year": "c. 600 BC", "type": "event"},
      {"label": "Judah's leadership exiled to Babylon by Nebuchadnezzar", "ref": "2 Kings 25:11", "year": "587 BC", "type": "event"},
    ],
    "after": [
      {"label": "Ezekiel — prophesying among the exiles in Babylon", "ref": "Ezekiel 1:1", "year": "c. 593 BC", "type": "book"},
      {"label": "Daniel — Jews in the Babylonian court maintaining faithfulness", "ref": "Daniel 1:1", "year": "c. 605 BC", "type": "book"},
      {"label": "Cyrus's decree; exiles begin returning to Jerusalem", "ref": "Ezra 1:1", "year": "538 BC", "type": "event"},
    ]
  },
  "ezekiel": {
    "period": "exile",
    "date": "c. 593–571 BC",
    "before": [
      {"label": "First wave of deportation to Babylon under Jehoiachin", "ref": "2 Kings 24:15", "year": "597 BC", "type": "event"},
      {"label": "Jeremiah — preaching judgment in Jerusalem simultaneously", "ref": "Jeremiah 1:1", "year": "c. 627 BC", "type": "book"},
      {"label": "God's glory fills Solomon's temple — then departs", "ref": "Ezekiel 10:18", "year": "c. 592 BC", "type": "event"},
    ],
    "after": [
      {"label": "Jerusalem falls — Ezekiel's ministry shifts to restoration", "ref": "Ezekiel 33:21", "year": "587 BC", "type": "event"},
      {"label": "Cyrus conquers Babylon; the exile ends", "ref": "Ezra 1:1", "year": "539 BC", "type": "world"},
      {"label": "Pentecost — Spirit poured out fulfilling Ezek 36:26–27", "ref": "Acts 2:1", "year": "c. AD 30", "type": "event"},
    ]
  },
  "daniel": {
    "period": "exile",
    "date": "Events: c. 605–530 BC",
    "before": [
      {"label": "First Babylonian deportation — Daniel taken to Babylon", "ref": "Daniel 1:1", "year": "605 BC", "type": "event"},
      {"label": "Nebuchadnezzar destroys Jerusalem and the temple", "ref": "2 Kings 25:1", "year": "587 BC", "type": "event"},
      {"label": "Jeremiah — exile and restoration prophesied", "ref": "Jeremiah 25:11", "year": "c. 605 BC", "type": "book"},
    ],
    "after": [
      {"label": "Fall of Babylon to Cyrus the Persian", "ref": "Daniel 5:30", "year": "539 BC", "type": "world"},
      {"label": "Cyrus's decree; exiles return under Zerubbabel", "ref": "Ezra 1:1", "year": "538 BC", "type": "event"},
      {"label": "Jesus claims to be the 'Son of Man' of Daniel 7", "ref": "Mark 14:62", "year": "c. AD 30", "type": "event"},
    ]
  },
  "hosea": {
    "period": "monarchy",
    "date": "c. 755–720 BC",
    "before": [
      {"label": "Jeroboam II's prosperous reign masks deep apostasy", "ref": "2 Kings 14:23", "year": "c. 793–753 BC", "type": "event"},
      {"label": "Amos — social justice condemned in the northern kingdom", "ref": "Amos 1:1", "year": "c. 760 BC", "type": "book"},
      {"label": "Baal worship entrenched since Ahab and Jezebel's era", "ref": "1 Kings 18:19", "year": "c. 865 BC", "type": "event"},
    ],
    "after": [
      {"label": "Fall of Samaria — Israel exiled to Assyria", "ref": "2 Kings 17:6", "year": "722 BC", "type": "event"},
      {"label": "Isaiah preaches the same themes in Judah simultaneously", "ref": "Isaiah 1:2", "year": "c. 740 BC", "type": "book"},
      {"label": "Matthew — 'Out of Egypt I called my son' fulfilled", "ref": "Matthew 2:15", "year": "c. AD 2", "type": "event"},
    ]
  },
  "joel": {
    "period": "restoration",
    "date": "c. 400 BC (post-exilic, disputed)",
    "before": [
      {"label": "Locust plague devastates the land — the immediate crisis", "ref": "Joel 1:4", "year": "uncertain", "type": "event"},
      {"label": "Malachi — the post-exilic community's spiritual drift", "ref": "Malachi 1:1", "year": "c. 450 BC", "type": "book"},
      {"label": "Zechariah — post-exilic visions and the coming Day", "ref": "Zechariah 14:1", "year": "c. 520 BC", "type": "book"},
    ],
    "after": [
      {"label": "Pentecost — the Spirit poured on all flesh as Joel promised", "ref": "Acts 2:16", "year": "c. AD 30", "type": "event"},
      {"label": "Paul — 'Everyone who calls on the name of the Lord will be saved'", "ref": "Romans 10:13", "year": "c. AD 57", "type": "event"},
      {"label": "Revelation — the great Day of the LORD's final arrival", "ref": "Revelation 6:17", "year": "c. AD 95", "type": "event"},
    ]
  },
  "amos": {
    "period": "monarchy",
    "date": "c. 760–750 BC",
    "before": [
      {"label": "Jeroboam II's long and prosperous reign in Israel", "ref": "2 Kings 14:23", "year": "c. 793–753 BC", "type": "event"},
      {"label": "Social stratification and exploitation of the rural poor grow", "ref": "Amos 2:6", "year": "c. 760 BC", "type": "event"},
      {"label": "Elijah and Elisha — prophetic opposition to royal apostasy", "ref": "1 Kings 18:1", "year": "c. 869 BC", "type": "event"},
    ],
    "after": [
      {"label": "Hosea — covenant faithlessness and God's pursuing love", "ref": "Hosea 1:1", "year": "c. 755 BC", "type": "book"},
      {"label": "Fall of Samaria — Israel's judgment arrives", "ref": "2 Kings 17:6", "year": "722 BC", "type": "event"},
      {"label": "James cites Acts 15 (Amos 9:11) — Gentiles included in David's tent", "ref": "Acts 15:16", "year": "c. AD 49", "type": "event"},
    ]
  },
  "obadiah": {
    "period": "exile",
    "date": "c. 587–585 BC",
    "before": [
      {"label": "Jerusalem falls; Edom gloats and plunders", "ref": "Obadiah 10", "year": "587 BC", "type": "event"},
      {"label": "Esau and Jacob — the ancient rivalry between twin brothers", "ref": "Genesis 25:23", "year": "c. 1900 BC", "type": "event"},
      {"label": "Edom's hostility during Israel's exodus from Egypt", "ref": "Numbers 20:20", "year": "c. 1446 BC", "type": "event"},
    ],
    "after": [
      {"label": "Malachi — Edom's later desolation confirmed", "ref": "Malachi 1:3", "year": "c. 450 BC", "type": "event"},
      {"label": "Kingdom of God established over all nations", "ref": "Obadiah 21", "year": "eschatological", "type": "event"},
      {"label": "Revelation — the nations judged and the kingdom comes", "ref": "Revelation 11:15", "year": "c. AD 95", "type": "event"},
    ]
  },
  "jonah": {
    "period": "monarchy",
    "date": "c. 785–750 BC (Jeroboam II's era)",
    "before": [
      {"label": "Jeroboam II expands Israel's territory — Jonah's other prophecy", "ref": "2 Kings 14:25", "year": "c. 785 BC", "type": "event"},
      {"label": "Nineveh: capital of Assyria, Israel's most feared enemy", "ref": "Jonah 1:2", "year": "c. 785 BC", "type": "world"},
      {"label": "Elijah flees to Horeb — the despairing prophet God pursues", "ref": "1 Kings 19:4", "year": "c. 865 BC", "type": "event"},
    ],
    "after": [
      {"label": "Nahum — Nineveh's eventual permanent destruction prophesied", "ref": "Nahum 1:1", "year": "c. 660 BC", "type": "book"},
      {"label": "The sign of Jonah — Jesus' death and resurrection", "ref": "Matthew 12:40", "year": "c. AD 30", "type": "event"},
      {"label": "Acts — the gospel proclaimed to the nations as God intended", "ref": "Acts 1:8", "year": "c. AD 30", "type": "event"},
    ]
  },
  "micah": {
    "period": "exile",
    "date": "c. 735–700 BC",
    "before": [
      {"label": "Isaiah — contemporaneous preaching in Jerusalem's courts", "ref": "Isaiah 1:1", "year": "c. 740 BC", "type": "book"},
      {"label": "Fall of Samaria — the northern kingdom gone", "ref": "2 Kings 17:6", "year": "722 BC", "type": "event"},
      {"label": "Rural poor exploited by Jerusalem's urban elites", "ref": "Micah 2:1", "year": "c. 735 BC", "type": "event"},
    ],
    "after": [
      {"label": "Hezekiah's reforms — Micah cited as their catalyst", "ref": "Jeremiah 26:18", "year": "c. 701 BC", "type": "event"},
      {"label": "Jesus born in Bethlehem — Micah 5:2 fulfilled", "ref": "Matthew 2:6", "year": "c. 5 BC", "type": "event"},
      {"label": "Micah 6:8 — 'do justice, love kindness, walk humbly'", "ref": "Matthew 23:23", "year": "c. AD 30", "type": "event"},
    ]
  },
  "nahum": {
    "period": "exile",
    "date": "c. 660–615 BC",
    "before": [
      {"label": "Fall of Thebes (No-Amon) to Assyria — cited as recent past", "ref": "Nahum 3:8", "year": "663 BC", "type": "world"},
      {"label": "Jonah preaches at Nineveh; the city repents temporarily", "ref": "Jonah 3:5", "year": "c. 785 BC", "type": "event"},
      {"label": "Sennacherib's siege of Jerusalem; Assyria at its height", "ref": "2 Kings 19:35", "year": "701 BC", "type": "world"},
    ],
    "after": [
      {"label": "Nineveh falls to Babylon and the Medes", "ref": "Nahum 3:19", "year": "612 BC", "type": "world"},
      {"label": "Habakkuk — Babylonian rise and the problem of theodicy", "ref": "Habakkuk 1:1", "year": "c. 605 BC", "type": "book"},
      {"label": "Battle of Carchemish — Babylon becomes the world power", "ref": "Jeremiah 46:2", "year": "605 BC", "type": "world"},
    ]
  },
  "habakkuk": {
    "period": "exile",
    "date": "c. 605 BC",
    "before": [
      {"label": "Nineveh falls — Assyrian dominance ends", "ref": "Nahum 3:19", "year": "612 BC", "type": "event"},
      {"label": "Battle of Carchemish — Babylon becomes world's superpower", "ref": "Jeremiah 46:2", "year": "605 BC", "type": "world"},
      {"label": "Josiah's death at Megiddo — the reform era ends", "ref": "2 Chronicles 35:23", "year": "609 BC", "type": "event"},
    ],
    "after": [
      {"label": "Nebuchadnezzar's first deportation of Jerusalem's leadership", "ref": "Daniel 1:1", "year": "605 BC", "type": "event"},
      {"label": "The righteous live by faith — quoted in Romans, Galatians, Hebrews", "ref": "Romans 1:17", "year": "c. AD 57", "type": "event"},
      {"label": "Zephaniah — Josiah's era; the coming Day of the LORD", "ref": "Zephaniah 1:1", "year": "c. 630 BC", "type": "book"},
    ]
  },
  "zephaniah": {
    "period": "exile",
    "date": "c. 630–620 BC (Josiah's reign)",
    "before": [
      {"label": "Manasseh's 55-year reign — the worst idolatry Judah had seen", "ref": "2 Kings 21:2", "year": "c. 697–642 BC", "type": "event"},
      {"label": "Josiah's reform begins — pagan altars torn down", "ref": "2 Chronicles 34:3", "year": "c. 628 BC", "type": "event"},
      {"label": "Nahum — Nineveh's judgment announced", "ref": "Nahum 1:1", "year": "c. 660 BC", "type": "book"},
    ],
    "after": [
      {"label": "Josiah's law-book discovery — reform intensified", "ref": "2 Chronicles 34:14", "year": "621 BC", "type": "event"},
      {"label": "Jerusalem falls to Babylon; the Day of the LORD arrives", "ref": "Jeremiah 52:12", "year": "587 BC", "type": "event"},
      {"label": "Pentecost — 'pure speech for all peoples' (Zeph 3:9) fulfilled", "ref": "Acts 2:4", "year": "c. AD 30", "type": "event"},
    ]
  },
  "haggai": {
    "period": "restoration",
    "date": "520 BC",
    "before": [
      {"label": "First return under Zerubbabel — temple work stalls for 16 years", "ref": "Ezra 4:24", "year": "c. 536–520 BC", "type": "event"},
      {"label": "Ezra — Persian court endorses the rebuilding project", "ref": "Ezra 6:1", "year": "c. 520 BC", "type": "book"},
      {"label": "Post-exilic community: economic hardship and misplaced priorities", "ref": "Haggai 1:6", "year": "520 BC", "type": "event"},
    ],
    "after": [
      {"label": "Temple construction resumes immediately after Haggai's word", "ref": "Ezra 5:2", "year": "520 BC", "type": "event"},
      {"label": "Zechariah — eight visions confirm God's return to Zion", "ref": "Zechariah 1:1", "year": "520 BC", "type": "book"},
      {"label": "Second temple completed and dedicated", "ref": "Ezra 6:16", "year": "516 BC", "type": "event"},
    ]
  },
  "zechariah": {
    "period": "restoration",
    "date": "c. 520–518 BC; chs. 9–14 possibly later",
    "before": [
      {"label": "Haggai — temple rebuilding resumes under God's word", "ref": "Haggai 1:14", "year": "520 BC", "type": "book"},
      {"label": "First exiles return; temple foundation laid", "ref": "Ezra 3:10", "year": "c. 536 BC", "type": "event"},
      {"label": "God's glory departs from Jerusalem — Ezekiel's vision", "ref": "Ezekiel 11:23", "year": "c. 592 BC", "type": "event"},
    ],
    "after": [
      {"label": "Second temple completed and dedicated to the LORD", "ref": "Ezra 6:16", "year": "516 BC", "type": "event"},
      {"label": "Jesus rides into Jerusalem on a donkey — Zech 9:9 fulfilled", "ref": "Matthew 21:5", "year": "c. AD 30", "type": "event"},
      {"label": "Revelation — the pierced one (Zech 12:10) returns in glory", "ref": "Revelation 1:7", "year": "c. AD 95", "type": "event"},
    ]
  },
  "malachi": {
    "period": "restoration",
    "date": "c. 450–430 BC",
    "before": [
      {"label": "Nehemiah's reforms — community reconstituted around the Torah", "ref": "Nehemiah 13:1", "year": "c. 445 BC", "type": "event"},
      {"label": "Zechariah — messianic visions of the coming king", "ref": "Zechariah 9:9", "year": "c. 520 BC", "type": "book"},
      {"label": "Temple rebuilt and in operation; religious routine sets in", "ref": "Ezra 6:16", "year": "516 BC", "type": "event"},
    ],
    "after": [
      {"label": "Four hundred years of prophetic silence", "ref": "Malachi 4:6", "year": "c. 430–5 BC", "type": "event"},
      {"label": "John the Baptist arrives — the Elijah-forerunner of Mal 4:5", "ref": "Luke 1:17", "year": "c. 27 BC", "type": "event"},
      {"label": "Jesus enters the temple — 'the Lord whom you seek' arrives", "ref": "Malachi 3:1", "year": "c. AD 30", "type": "event"},
    ]
  },
  "matthew": {
    "period": "gospels",
    "date": "c. AD 80–90 (events: ~6 BC – AD 30)",
    "before": [
      {"label": "The OT closes; 400 years of prophetic silence", "ref": "Malachi 4:6", "year": "c. 430 BC", "type": "event"},
      {"label": "John the Baptist prepares the way in the wilderness", "ref": "Matthew 3:1", "year": "c. AD 27", "type": "event"},
      {"label": "Caesar Augustus orders a census — Jesus born in Bethlehem", "ref": "Luke 2:1", "year": "c. 5 BC", "type": "world"},
    ],
    "after": [
      {"label": "Pentecost — the Great Commission begins to be fulfilled", "ref": "Acts 2:1", "year": "c. AD 30", "type": "event"},
      {"label": "Acts — gospel spreads from Jerusalem to Rome", "ref": "Acts 1:8", "year": "c. AD 30–62", "type": "book"},
      {"label": "Destruction of the temple — Matthew 24 fulfilled", "ref": "Matthew 24:2", "year": "AD 70", "type": "world"},
    ]
  },
  "mark": {
    "period": "gospels",
    "date": "c. AD 65–70 (events: c. AD 27–30)",
    "before": [
      {"label": "John the Baptist's ministry begins in the wilderness", "ref": "Mark 1:2", "year": "c. AD 27", "type": "event"},
      {"label": "Jesus baptized by John in the Jordan River", "ref": "Mark 1:9", "year": "c. AD 27", "type": "event"},
      {"label": "Isaiah 40 — 'A voice of one calling in the desert'", "ref": "Isaiah 40:3", "year": "c. 740 BC", "type": "event"},
    ],
    "after": [
      {"label": "Pentecost — the gospel proclaimed with power", "ref": "Acts 2:1", "year": "c. AD 30", "type": "event"},
      {"label": "Nero's persecution in Rome — Mark's probable context", "ref": "1 Peter 5:13", "year": "c. AD 64", "type": "world"},
      {"label": "Acts — the Way spreads throughout the Roman world", "ref": "Acts 1:8", "year": "c. AD 30–62", "type": "book"},
    ]
  },
  "luke": {
    "period": "gospels",
    "date": "c. AD 80–90 (events: c. 5 BC – AD 30)",
    "before": [
      {"label": "Gabriel announces John the Baptist's birth to Zechariah", "ref": "Luke 1:11", "year": "c. 5 BC", "type": "event"},
      {"label": "Isaiah 61 — the Spirit-anointed Servant who proclaims liberty", "ref": "Isaiah 61:1", "year": "c. 680 BC", "type": "event"},
      {"label": "Caesar Augustus: Roman peace (Pax Romana) as historical setting", "ref": "Luke 2:1", "year": "c. 27 BC–AD 14", "type": "world"},
    ],
    "after": [
      {"label": "Acts — Luke's second volume; gospel to the ends of the earth", "ref": "Acts 1:1", "year": "c. AD 30–62", "type": "book"},
      {"label": "Ascension of Jesus; disciples commissioned and equipped", "ref": "Luke 24:50", "year": "c. AD 30", "type": "event"},
      {"label": "Pentecost — Spirit poured out on all flesh as Joel promised", "ref": "Acts 2:1", "year": "c. AD 30", "type": "event"},
    ]
  },
  "john": {
    "period": "gospels",
    "date": "c. AD 90–100 (events: c. 27–30 AD)",
    "before": [
      {"label": "Expulsion from the synagogue — John's community context", "ref": "John 9:22", "year": "c. AD 85–90", "type": "world"},
      {"label": "In the beginning was the Word — John 1:1 echoes Genesis 1:1", "ref": "Genesis 1:1", "year": "Primeval", "type": "event"},
      {"label": "Isaiah's vision of YHWH's glory — John 12:41 applies it to Jesus", "ref": "Isaiah 6:1", "year": "740 BC", "type": "event"},
    ],
    "after": [
      {"label": "Resurrection appearances; Thomas confesses 'My Lord and my God'", "ref": "John 20:28", "year": "c. AD 30", "type": "event"},
      {"label": "Pentecost — the Paraclete arrives as Jesus promised", "ref": "Acts 2:1", "year": "c. AD 30", "type": "event"},
      {"label": "1 John — the Johannine community applies the gospel", "ref": "1 John 1:1", "year": "c. AD 90", "type": "book"},
    ]
  },
  "acts": {
    "period": "church",
    "date": "Events: c. AD 30–62",
    "before": [
      {"label": "Resurrection and 40-day ministry of the risen Christ", "ref": "Acts 1:3", "year": "c. AD 30", "type": "event"},
      {"label": "Jesus' Great Commission — 'to the ends of the earth'", "ref": "Acts 1:8", "year": "c. AD 30", "type": "event"},
      {"label": "Joel 2:28–32 — Spirit poured on all flesh; the 'last days' begin", "ref": "Joel 2:28", "year": "c. 400 BC", "type": "event"},
    ],
    "after": [
      {"label": "Paul's letters written from within the Acts narrative", "ref": "Romans 1:1", "year": "c. AD 49–60", "type": "event"},
      {"label": "Paul arrives in Rome — the gospel reaches the empire's capital", "ref": "Acts 28:16", "year": "c. AD 60", "type": "event"},
      {"label": "Nero's persecution; Peter and Paul martyred in Rome", "ref": "2 Timothy 4:6", "year": "c. AD 64–67", "type": "world"},
    ]
  },
  "romans": {
    "period": "church",
    "date": "c. AD 57 (from Corinth)",
    "before": [
      {"label": "Paul's third missionary journey; Corinthian correspondence", "ref": "Acts 18:1", "year": "c. AD 50–57", "type": "event"},
      {"label": "1–2 Corinthians — Paul addresses the church's problems", "ref": "1 Corinthians 1:1", "year": "c. AD 54–55", "type": "book"},
      {"label": "Genesis 15 — Abraham credited as righteous through faith", "ref": "Genesis 15:6", "year": "c. 2000 BC", "type": "event"},
    ],
    "after": [
      {"label": "Paul journeys to Jerusalem with the Gentile collection", "ref": "Acts 21:1", "year": "c. AD 57", "type": "event"},
      {"label": "Paul arrested in Jerusalem; two years of Roman custody begin", "ref": "Acts 21:33", "year": "c. AD 57", "type": "event"},
      {"label": "Prison letters: Ephesians, Philippians, Colossians, Philemon", "ref": "Ephesians 3:1", "year": "c. AD 60–62", "type": "event"},
    ]
  },
  "1corinthians": {
    "period": "church",
    "date": "c. AD 54–55 (from Ephesus)",
    "before": [
      {"label": "Paul founds the Corinthian church during his second journey", "ref": "Acts 18:1", "year": "c. AD 50–51", "type": "event"},
      {"label": "Chloe's people bring disturbing news of divisions", "ref": "1 Corinthians 1:11", "year": "c. AD 54", "type": "event"},
      {"label": "A previous letter (now lost) precedes this one", "ref": "1 Corinthians 5:9", "year": "c. AD 53", "type": "event"},
    ],
    "after": [
      {"label": "Paul's painful visit to Corinth follows this letter's failure", "ref": "2 Corinthians 2:1", "year": "c. AD 55", "type": "event"},
      {"label": "2 Corinthians — Paul defends his ministry; reconciliation", "ref": "2 Corinthians 1:1", "year": "c. AD 55–57", "type": "book"},
      {"label": "Jerusalem Council — Jewish-Gentile tensions resolved apostolically", "ref": "Acts 15:1", "year": "c. AD 49", "type": "event"},
    ]
  },
  "2corinthians": {
    "period": "church",
    "date": "c. AD 55–57 (from Macedonia)",
    "before": [
      {"label": "1 Corinthians — divisions, disorders, and the cross as answer", "ref": "1 Corinthians 1:1", "year": "c. AD 54", "type": "book"},
      {"label": "Paul's painful visit fails; a severe letter written", "ref": "2 Corinthians 2:4", "year": "c. AD 55", "type": "event"},
      {"label": "Timothy reports the Corinthians' repentance to Paul", "ref": "2 Corinthians 7:6", "year": "c. AD 56", "type": "event"},
    ],
    "after": [
      {"label": "Paul's third visit to Corinth to complete the collection", "ref": "Acts 20:2", "year": "c. AD 57", "type": "event"},
      {"label": "Romans — written from Corinth at the end of this journey", "ref": "Romans 1:1", "year": "c. AD 57", "type": "book"},
      {"label": "Jerusalem journey with the Gentile collection; Paul arrested", "ref": "Acts 21:17", "year": "c. AD 57", "type": "event"},
    ]
  },
  "galatians": {
    "period": "church",
    "date": "c. AD 48–49 or AD 53–55 (debated)",
    "before": [
      {"label": "Paul's first missionary journey plants churches in Galatia", "ref": "Acts 13:14", "year": "c. AD 47–48", "type": "event"},
      {"label": "Jewish-Christian teachers demand Gentiles be circumcised", "ref": "Galatians 1:6", "year": "c. AD 48", "type": "event"},
      {"label": "Peter withdraws from Gentiles at Antioch — the incident Paul describes", "ref": "Galatians 2:11", "year": "c. AD 47", "type": "event"},
    ],
    "after": [
      {"label": "Jerusalem Council — the gospel for the Gentiles formally affirmed", "ref": "Acts 15:1", "year": "c. AD 49", "type": "event"},
      {"label": "Romans — the fullest development of justification by faith", "ref": "Romans 1:1", "year": "c. AD 57", "type": "book"},
      {"label": "Ephesians — the new humanity of Jew and Gentile in Christ", "ref": "Ephesians 2:14", "year": "c. AD 60", "type": "event"},
    ]
  },
  "ephesians": {
    "period": "church",
    "date": "c. AD 60–62 (Roman imprisonment)",
    "before": [
      {"label": "Paul's long ministry in Ephesus — three years (Acts 19)", "ref": "Acts 19:10", "year": "c. AD 52–55", "type": "event"},
      {"label": "Paul's arrest in Jerusalem; two years in Caesarean custody", "ref": "Acts 24:27", "year": "c. AD 57–59", "type": "event"},
      {"label": "Colossians — the cosmic supremacy of Christ established", "ref": "Colossians 1:15", "year": "c. AD 60", "type": "book"},
    ],
    "after": [
      {"label": "Philippians — joy from prison; the mind of Christ", "ref": "Philippians 1:1", "year": "c. AD 61", "type": "book"},
      {"label": "Paul released; Pastoral Epistles written", "ref": "1 Timothy 1:1", "year": "c. AD 62–65", "type": "event"},
      {"label": "Revelation — the church as Christ's bride, the new Jerusalem", "ref": "Revelation 19:7", "year": "c. AD 95", "type": "event"},
    ]
  },
  "philippians": {
    "period": "church",
    "date": "c. AD 60–62 (Roman imprisonment)",
    "before": [
      {"label": "Paul founds the Philippian church — first in Europe (Acts 16)", "ref": "Acts 16:12", "year": "c. AD 49", "type": "event"},
      {"label": "Philippians' generous support throughout Paul's ministry", "ref": "Philippians 4:15", "year": "c. AD 49–60", "type": "event"},
      {"label": "Epaphroditus nearly dies delivering the Philippians' gift", "ref": "Philippians 2:27", "year": "c. AD 60", "type": "event"},
    ],
    "after": [
      {"label": "Colossians — Christ's cosmic supremacy; the letter sent with Tychicus", "ref": "Colossians 4:7", "year": "c. AD 60", "type": "book"},
      {"label": "Paul's release from prison; further travels in the east", "ref": "Philemon 22", "year": "c. AD 62", "type": "event"},
      {"label": "Paul's second imprisonment and martyrdom under Nero", "ref": "2 Timothy 4:6", "year": "c. AD 66–67", "type": "event"},
    ]
  },
  "colossians": {
    "period": "church",
    "date": "c. AD 60–62 (Roman imprisonment)",
    "before": [
      {"label": "Epaphras founds the Colossian church and reports its crisis to Paul", "ref": "Colossians 1:7", "year": "c. AD 55", "type": "event"},
      {"label": "A syncretistic philosophy threatens the church's Christ-centredness", "ref": "Colossians 2:8", "year": "c. AD 60", "type": "event"},
      {"label": "Ephesians — the cosmic church and Christ's universal lordship", "ref": "Ephesians 1:21", "year": "c. AD 60", "type": "book"},
    ],
    "after": [
      {"label": "Philemon — Onesimus sent back; the letter carried with Colossians", "ref": "Colossians 4:9", "year": "c. AD 60", "type": "book"},
      {"label": "Paul's release from prison; the Pastoral Epistles follow", "ref": "1 Timothy 1:1", "year": "c. AD 62–65", "type": "event"},
      {"label": "Letter read aloud in the Laodicean church as well", "ref": "Colossians 4:16", "year": "c. AD 60", "type": "event"},
    ]
  },
  "1thessalonians": {
    "period": "church",
    "date": "c. AD 50–51 (from Corinth)",
    "before": [
      {"label": "Paul in Thessalonica — forced to leave after a brief stay", "ref": "Acts 17:1", "year": "c. AD 50", "type": "event"},
      {"label": "Timothy reports the Thessalonians' faith and love to Paul", "ref": "1 Thessalonians 3:6", "year": "c. AD 50", "type": "event"},
      {"label": "Galatians — the earliest Pauline letter (or contemporary)", "ref": "Galatians 1:1", "year": "c. AD 48–49", "type": "book"},
    ],
    "after": [
      {"label": "2 Thessalonians — follow-up addressing eschatological confusion", "ref": "2 Thessalonians 1:1", "year": "c. AD 51", "type": "book"},
      {"label": "Paul's continued ministry in Corinth and beyond", "ref": "Acts 18:1", "year": "c. AD 50–52", "type": "event"},
      {"label": "Joel 2:28–32 — fulfilled at Pentecost; Day of the LORD still coming", "ref": "Joel 2:28", "year": "c. AD 30", "type": "event"},
    ]
  },
  "2thessalonians": {
    "period": "church",
    "date": "c. AD 51 (from Corinth)",
    "before": [
      {"label": "1 Thessalonians — faith commended; eschatological hope established", "ref": "1 Thessalonians 1:1", "year": "c. AD 50", "type": "book"},
      {"label": "A forged letter claims the Day of the Lord has already come", "ref": "2 Thessalonians 2:2", "year": "c. AD 51", "type": "event"},
      {"label": "Some members stop working, relying on others' generosity", "ref": "2 Thessalonians 3:11", "year": "c. AD 51", "type": "event"},
    ],
    "after": [
      {"label": "1 Corinthians — Paul writes the churches in Corinth and Achaia", "ref": "1 Corinthians 1:1", "year": "c. AD 54", "type": "book"},
      {"label": "Jerusalem Council — Jewish-Gentile relations clarified", "ref": "Acts 15:1", "year": "c. AD 49", "type": "event"},
      {"label": "Daniel's 'man of lawlessness' — Paul draws on Daniel's visions", "ref": "Daniel 7:25", "year": "c. 550 BC", "type": "event"},
    ]
  },
  "1timothy": {
    "period": "church",
    "date": "c. AD 62–65",
    "before": [
      {"label": "Paul released from first Roman imprisonment", "ref": "Acts 28:30", "year": "c. AD 62", "type": "event"},
      {"label": "Paul leaves Timothy in Ephesus to address false teachers", "ref": "1 Timothy 1:3", "year": "c. AD 62", "type": "event"},
      {"label": "Paul's long Ephesian ministry — three years of teaching", "ref": "Acts 20:31", "year": "c. AD 52–55", "type": "event"},
    ],
    "after": [
      {"label": "2 Timothy — Paul's second imprisonment; his final letter", "ref": "2 Timothy 1:1", "year": "c. AD 66–67", "type": "book"},
      {"label": "Titus — similar instructions for churches in Crete", "ref": "Titus 1:1", "year": "c. AD 63–65", "type": "book"},
      {"label": "Paul's martyrdom under Nero in Rome", "ref": "2 Timothy 4:6", "year": "c. AD 67", "type": "event"},
    ]
  },
  "2timothy": {
    "period": "church",
    "date": "c. AD 66–67 (Paul's final letter)",
    "before": [
      {"label": "1 Timothy — Timothy left in Ephesus; church order established", "ref": "1 Timothy 1:3", "year": "c. AD 62", "type": "book"},
      {"label": "Paul's second Roman arrest under Nero's persecution", "ref": "2 Timothy 1:8", "year": "c. AD 66", "type": "world"},
      {"label": "Everyone in Asia has abandoned Paul; only Luke remains", "ref": "2 Timothy 1:15", "year": "c. AD 66", "type": "event"},
    ],
    "after": [
      {"label": "Paul's execution in Rome — the race finished, the crown received", "ref": "2 Timothy 4:7", "year": "c. AD 67", "type": "event"},
      {"label": "Timothy carries on the ministry; the torch passed", "ref": "2 Timothy 2:2", "year": "c. AD 67", "type": "event"},
      {"label": "Hebrews — the epistle of Christ's superiority, written near this era", "ref": "Hebrews 1:1", "year": "c. AD 60–70", "type": "book"},
    ]
  },
  "titus": {
    "period": "church",
    "date": "c. AD 63–65",
    "before": [
      {"label": "Paul and Titus work together on Crete; Titus left behind", "ref": "Titus 1:5", "year": "c. AD 63", "type": "event"},
      {"label": "1 Timothy — parallel instructions for a different context", "ref": "1 Timothy 1:1", "year": "c. AD 62", "type": "book"},
      {"label": "Paul's release from Roman imprisonment; resumed travels", "ref": "Acts 28:30", "year": "c. AD 62", "type": "event"},
    ],
    "after": [
      {"label": "Titus sent to Dalmatia — his final appearance in Paul's letters", "ref": "2 Timothy 4:10", "year": "c. AD 66", "type": "event"},
      {"label": "2 Timothy — Paul's farewell and charge to Timothy", "ref": "2 Timothy 1:1", "year": "c. AD 66–67", "type": "book"},
      {"label": "Grace of God appeared — fulfilled fully at Christ's return (Titus 2:13)", "ref": "Titus 2:13", "year": "eschatological", "type": "event"},
    ]
  },
  "philemon": {
    "period": "church",
    "date": "c. AD 60–62 (Roman imprisonment)",
    "before": [
      {"label": "Onesimus flees from Philemon to Rome; meets Paul there", "ref": "Philemon 10", "year": "c. AD 60", "type": "event"},
      {"label": "Colossians — written from the same imprisonment; Onesimus named", "ref": "Colossians 4:9", "year": "c. AD 60", "type": "book"},
      {"label": "Paul founds the Colossian house-church through Epaphras", "ref": "Colossians 1:7", "year": "c. AD 52", "type": "event"},
    ],
    "after": [
      {"label": "Galatians 3:28 — 'neither slave nor free' becomes social reality", "ref": "Galatians 3:28", "year": "c. AD 48", "type": "event"},
      {"label": "Christianity's eventual role in abolishing slavery in the West", "ref": "Philemon 16", "year": "historical", "type": "world"},
      {"label": "Paul released and hopes to visit Philemon in Colossae", "ref": "Philemon 22", "year": "c. AD 62", "type": "event"},
    ]
  },
  "hebrews": {
    "period": "church",
    "date": "c. AD 60–70 (before the temple fell)",
    "before": [
      {"label": "Jewish-Christian community under pressure to return to Judaism", "ref": "Hebrews 10:25", "year": "c. AD 60", "type": "event"},
      {"label": "The Jerusalem temple still standing and functioning", "ref": "Hebrews 9:8", "year": "c. AD 60–70", "type": "event"},
      {"label": "Leviticus — the Aaronic priesthood and Day of Atonement", "ref": "Leviticus 16:1", "year": "c. 1446 BC", "type": "book"},
    ],
    "after": [
      {"label": "Destruction of the temple — Hebrews' argument confirmed historically", "ref": "Matthew 24:2", "year": "AD 70", "type": "world"},
      {"label": "Jeremiah's new covenant — fully explained in Hebrews 8–10", "ref": "Jeremiah 31:31", "year": "c. 600 BC", "type": "event"},
      {"label": "Revelation — the heavenly temple and the Lamb's sacrifice", "ref": "Revelation 21:22", "year": "c. AD 95", "type": "event"},
    ]
  },
  "james": {
    "period": "church",
    "date": "c. AD 45–49 (earliest NT letter)",
    "before": [
      {"label": "Pentecost and the scattered Jerusalem church", "ref": "Acts 8:1", "year": "c. AD 35", "type": "event"},
      {"label": "James leads the Jerusalem church as its primary elder", "ref": "Acts 15:13", "year": "c. AD 49", "type": "event"},
      {"label": "Jesus' Sermon on the Mount — the conceptual matrix of the letter", "ref": "Matthew 5:1", "year": "c. AD 28", "type": "event"},
    ],
    "after": [
      {"label": "Jerusalem Council — James presides over the church's first major dispute", "ref": "Acts 15:13", "year": "c. AD 49", "type": "event"},
      {"label": "James martyred by Herod Agrippa or by the high priest Ananus", "ref": "Acts 12:2", "year": "c. AD 62", "type": "event"},
      {"label": "1 Peter — suffering and diaspora life addressed similarly", "ref": "1 Peter 1:1", "year": "c. AD 62–64", "type": "book"},
    ]
  },
  "1peter": {
    "period": "church",
    "date": "c. AD 62–64 (from Rome)",
    "before": [
      {"label": "Nero's persecution begins after the great fire of Rome", "ref": "1 Peter 4:12", "year": "AD 64", "type": "world"},
      {"label": "Christians experience social ostracism throughout Asia Minor", "ref": "1 Peter 1:1", "year": "c. AD 62", "type": "event"},
      {"label": "Isaiah 53 — the suffering servant whose pattern Peter applies", "ref": "Isaiah 53:5", "year": "c. 700 BC", "type": "event"},
    ],
    "after": [
      {"label": "2 Peter — Peter's farewell; false teachers warned against", "ref": "2 Peter 1:1", "year": "c. AD 65–67", "type": "book"},
      {"label": "Peter martyred in Rome under Nero", "ref": "2 Peter 1:14", "year": "c. AD 64–68", "type": "event"},
      {"label": "Revelation — the exiled church, faithful under pressure", "ref": "Revelation 2:10", "year": "c. AD 95", "type": "event"},
    ]
  },
  "2peter": {
    "period": "church",
    "date": "c. AD 65–67",
    "before": [
      {"label": "1 Peter — suffering and identity of God's exiled people", "ref": "1 Peter 1:1", "year": "c. AD 62–64", "type": "book"},
      {"label": "Peter present at the Transfiguration — his eyewitness basis", "ref": "2 Peter 1:16", "year": "c. AD 29", "type": "event"},
      {"label": "False teachers infiltrating and denying the Lord's return", "ref": "2 Peter 2:1", "year": "c. AD 65", "type": "event"},
    ],
    "after": [
      {"label": "Peter's martyrdom in Rome — anticipated in 1:14", "ref": "2 Peter 1:14", "year": "c. AD 65–68", "type": "event"},
      {"label": "Jude — written around the same time; shares much of Peter's content", "ref": "Jude 3", "year": "c. AD 65–80", "type": "book"},
      {"label": "Revelation — the Day of the LORD's arrival in fullness", "ref": "Revelation 20:11", "year": "c. AD 95", "type": "event"},
    ]
  },
  "1john": {
    "period": "church",
    "date": "c. AD 90–100 (Ephesus)",
    "before": [
      {"label": "John's Gospel — Jesus as the Word made flesh, seen and touched", "ref": "John 1:14", "year": "c. AD 90", "type": "book"},
      {"label": "Schism: docetists leave the Johannine community", "ref": "1 John 2:19", "year": "c. AD 90", "type": "event"},
      {"label": "Expulsion of Jewish Christians from the synagogue", "ref": "John 9:22", "year": "c. AD 85–90", "type": "world"},
    ],
    "after": [
      {"label": "2 John — apply the truth test to travelling teachers", "ref": "2 John 1", "year": "c. AD 90–100", "type": "book"},
      {"label": "3 John — hospitality and the conflict with Diotrephes", "ref": "3 John 1", "year": "c. AD 90–100", "type": "book"},
      {"label": "Revelation — John's vision of the victorious Christ from Patmos", "ref": "Revelation 1:1", "year": "c. AD 95", "type": "book"},
    ]
  },
  "2john": {
    "period": "church",
    "date": "c. AD 90–100",
    "before": [
      {"label": "1 John — the three tests of genuine faith established", "ref": "1 John 4:1", "year": "c. AD 90–100", "type": "book"},
      {"label": "Travelling teachers propagating docetic Christology", "ref": "2 John 7", "year": "c. AD 90", "type": "event"},
      {"label": "John's Gospel — Jesus Christ came in the flesh; saw, heard, touched", "ref": "John 1:14", "year": "c. AD 90", "type": "event"},
    ],
    "after": [
      {"label": "3 John — the hospitality question viewed from the other side", "ref": "3 John 1", "year": "c. AD 90–100", "type": "book"},
      {"label": "Revelation — John receives the climactic vision from Patmos", "ref": "Revelation 1:1", "year": "c. AD 95", "type": "book"},
      {"label": "Early church councils — the Incarnation becomes a creedal test", "ref": "1 John 4:2", "year": "c. AD 325", "type": "world"},
    ]
  },
  "3john": {
    "period": "church",
    "date": "c. AD 90–100",
    "before": [
      {"label": "2 John — limits of hospitality; truth as the condition of welcome", "ref": "2 John 10", "year": "c. AD 90–100", "type": "book"},
      {"label": "1 John — love as the life of the community", "ref": "1 John 4:7", "year": "c. AD 90–100", "type": "book"},
      {"label": "John's Gospel — Jesus the true shepherd who serves rather than lords", "ref": "John 10:11", "year": "c. AD 90", "type": "event"},
    ],
    "after": [
      {"label": "Revelation — John's final canonical word from Patmos", "ref": "Revelation 1:1", "year": "c. AD 95", "type": "book"},
      {"label": "The canonical Johannine corpus completed (Gospel + 3 letters)", "ref": "1 John 1:1", "year": "c. AD 100", "type": "event"},
      {"label": "Ignatius of Antioch — early church navigates similar authority issues", "ref": "3 John 9", "year": "c. AD 107", "type": "world"},
    ]
  },
  "jude": {
    "period": "church",
    "date": "c. AD 65–80",
    "before": [
      {"label": "Antinomian teachers creep into the community", "ref": "Jude 4", "year": "c. AD 65", "type": "event"},
      {"label": "2 Peter — the same threat addressed from a similar angle", "ref": "2 Peter 2:1", "year": "c. AD 65–67", "type": "book"},
      {"label": "James — Jude's own brother established the Jerusalem church", "ref": "James 1:1", "year": "c. AD 45", "type": "event"},
    ],
    "after": [
      {"label": "Revelation — contending for the faith amid imperial pressure", "ref": "Revelation 2:2", "year": "c. AD 95", "type": "book"},
      {"label": "The doxology of 24–25 — Christ able to keep us from stumbling", "ref": "Jude 24", "year": "eschatological", "type": "event"},
      {"label": "Early church: the Apostles' Creed as public contending for the faith", "ref": "Jude 3", "year": "c. AD 150", "type": "world"},
    ]
  },
  "revelation": {
    "period": "consummation",
    "date": "c. AD 95 (Domitian's reign)",
    "before": [
      {"label": "Domitian's imperial cult; Christians refuse to worship the emperor", "ref": "Revelation 13:4", "year": "c. AD 95", "type": "world"},
      {"label": "Destruction of the Jerusalem temple — the old age has ended", "ref": "Matthew 24:2", "year": "AD 70", "type": "world"},
      {"label": "Paul, Peter, James martyred — the apostolic generation passes", "ref": "2 Timothy 4:6", "year": "c. AD 64–68", "type": "event"},
    ],
    "after": [
      {"label": "The canon closed — 'Do not add to these words' (22:18)", "ref": "Revelation 22:18", "year": "c. AD 100", "type": "event"},
      {"label": "Christ's return — 'Surely I am coming soon. Amen. Come, Lord Jesus!'", "ref": "Revelation 22:20", "year": "eschatological", "type": "event"},
      {"label": "New heavens and new earth — all things made new", "ref": "Revelation 21:5", "year": "Consummation", "type": "event"},
    ]
  },
}


def update(book_id, tl_data):
    path = os.path.join(OUT, book_id + '.json')
    if not os.path.exists(path):
        print(f'  SKIP  {book_id} (file not found)')
        return
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    tl = data.setdefault('timeline', {})
    if not OVERWRITE and tl.get('period'):
        print(f'  skip  {book_id} (already has period)')
        return
    tl['period'] = tl_data['period']
    tl['date'] = tl_data['date']
    tl['before'] = tl_data.get('before', [])
    tl['after'] = tl_data.get('after', [])
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'  updated: {book_id}')


for book_id, tl_data in TIMELINES.items():
    update(book_id, tl_data)

print(f'\nDone — {len(TIMELINES)} books processed')
