#!/usr/bin/env python3
"""
fetch-library-docs.py — Fetch public-domain texts from Wikisource and
convert them into <section data-heading="..."> HTML files for lib-browser.js.

Supports three source modes per manifest entry:
  page      → single Wikisource page (split into sections by h2/mw-heading divs)
  subpages  → list of {page, heading} dicts, each fetched as one section
  (future)  page_range — not yet implemented

Usage:
  python3 scripts/fetch-library-docs.py               # fetch all missing
  python3 scripts/fetch-library-docs.py --all          # re-fetch everything
  python3 scripts/fetch-library-docs.py --doc ignatius-romans
  python3 scripts/fetch-library-docs.py --dry-run
  python3 scripts/fetch-library-docs.py --list
  python3 scripts/fetch-library-docs.py --update-index  # patch data/library/index.json
"""

import argparse
import json
import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT   = os.path.dirname(SCRIPT_DIR)
HTML_DIR    = os.path.join(REPO_ROOT, 'data', 'library', 'html')
INDEX_PATH  = os.path.join(REPO_ROOT, 'data', 'library', 'index.json')

WS_API      = 'https://en.wikisource.org/w/api.php'
HEADERS     = {'User-Agent': 'bible-study-library-builder/1.0 (dse.saved@gmail.com)'}
RATE_DELAY  = 1.5   # seconds between API requests

# ---------------------------------------------------------------------------
# Document manifest
# ---------------------------------------------------------------------------
# Entry fields:
#   id           → output filename without .html; must match data-doc-id
#   page         → Wikisource page title (single-page mode)
#   subpages     → list of {page, heading} (each subpage → one section)
#   split_h      → heading level for single-page splitting ('h2' or 'h3')
#   max_sections → cap section count after splitting (0 = no cap)
#   index_meta   → fields merged into data/library/index.json entry
# ---------------------------------------------------------------------------

_CHRYSOSTOM_BASE = (
    'Nicene and Post-Nicene Fathers: Series I/Volume IX/'
    'Concerning the Christian Priesthood/Book '
)
_CONFESSIONS_BASE = 'The Confessions of Saint Augustine (Outler)/Book '
_IMIT_BASE = 'Of the Imitation of Christ'
_CDH_BASE  = 'Cur Deus Homo'
_PP_BASE   = "The Pilgrim's Progress (1890)/The "


def _roman(n):
  """Convert integer to uppercase Roman numeral string (for Imitation chapter paths)."""
  vals = [(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
  r = ''
  for v, s in vals:
    while n >= v: r += s; n -= v
  return r


def _imit_pages(book, lo, hi):
  """Build a list of Imitation of Christ chapter page titles."""
  return [f'{_IMIT_BASE}/Book {book}/Chapter {_roman(i)}' for i in range(lo, hi + 1)]


MANIFEST = [

  # ── Apostolic Fathers ─────────────────────────────────────────────────────
  {
    'id':   'clement-first-epistle',
    'page': 'Ante-Nicene Christian Library/First Epistle to the Corinthians (Clement)',
    'split_h': 'h2', 'max_sections': 6,
    'index_meta': {
      'abbrev': '1Clem', 'title': 'First Epistle of Clement',
      'year': 96, 'type': 'father', 'tradition': 'patristic',
      'author': 'Clement of Rome',
      'desc': 'A pastoral letter from the Roman church to Corinth on order, humility, and obedience — one of the earliest post-apostolic writings.',
    },
  },
  {
    'id':   'polycarp-philippians',
    'page': 'Ante-Nicene Christian Library/Epistle of Polycarp to the Philippians',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'PolPh', 'title': 'Letter to the Philippians',
      'year': 110, 'type': 'father', 'tradition': 'patristic',
      'author': 'Polycarp of Smyrna',
      'desc': 'A letter to the church at Philippi on righteousness, avoiding heresy, and enduring persecution faithfully.',
    },
  },
  {
    'id':   'martyrdom-of-polycarp',
    'page': 'Ante-Nicene Christian Library/The Martyrdom of Polycarp',
    'split_h': 'h2', 'max_sections': 5,
    'index_meta': {
      'abbrev': 'MartP', 'title': 'Martyrdom of Polycarp',
      'year': 155, 'type': 'father', 'tradition': 'patristic',
      'author': 'Smyrnaean Church',
      'desc': 'The earliest detailed account of Christian martyrdom — Polycarp\'s arrest, trial, and death at age 86.',
    },
  },

  # ── Justin Martyr ─────────────────────────────────────────────────────────
  {
    'id':   'justin-first-apology',
    'page': 'Ante-Nicene Christian Library/The First Apology of Justin Martyr',
    'split_h': 'h2', 'max_sections': 6,
    'index_meta': {
      'abbrev': 'JustFA', 'title': 'First Apology',
      'year': 155, 'type': 'father', 'tradition': 'patristic',
      'author': 'Justin Martyr',
      'desc': 'Addressed to Emperor Antoninus Pius — defence of Christians, the Logos doctrine, baptism, and the Eucharist.',
    },
  },
  {
    'id':   'justin-second-apology',
    'page': 'Ante-Nicene Christian Library/The Second Apology of Justin Martyr',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'JustSA', 'title': 'Second Apology',
      'year': 161, 'type': 'father', 'tradition': 'patristic',
      'author': 'Justin Martyr',
      'desc': 'A brief supplement responding to three recent executions and defending Christian philosophy against Crescens.',
    },
  },

  # ── John Chrysostom ───────────────────────────────────────────────────────
  {
    'id': 'chrysostom-on-priesthood',
    'subpages': [
      {'page': _CHRYSOSTOM_BASE + 'I',   'heading': 'Book I — The Weight of the Office'},
      {'page': _CHRYSOSTOM_BASE + 'II',  'heading': 'Book II — The Physician of Souls'},
      {'page': _CHRYSOSTOM_BASE + 'III', 'heading': 'Book III — The Preacher and His Labours'},
      {'page': _CHRYSOSTOM_BASE + 'IV',  'heading': 'Book IV — Defending the Choice'},
      {'page': _CHRYSOSTOM_BASE + 'V',   'heading': 'Book V — The Life of the Shepherd'},
      {'page': _CHRYSOSTOM_BASE + 'VI',  'heading': 'Book VI — The Contemplative and the Active'},
    ],
    'index_meta': {
      'abbrev': 'ChrysP', 'title': 'On the Priesthood',
      'year': 390, 'type': 'father', 'tradition': 'patristic',
      'author': 'John Chrysostom',
      'desc': 'Six books on the high calling and terrible weight of pastoral ministry — why Chrysostom fled ordination.',
    },
  },

  # ── Augustine of Hippo ────────────────────────────────────────────────────
  {
    'id': 'augustine-confessions',
    'subpages': [
      {'page': _CONFESSIONS_BASE + 'I',    'heading': 'Book I — Infancy and Childhood'},
      {'page': _CONFESSIONS_BASE + 'II',   'heading': 'Book II — Adolescence and the Theft of Pears'},
      {'page': _CONFESSIONS_BASE + 'III',  'heading': 'Book III — Carthage and the Manichees'},
      {'page': _CONFESSIONS_BASE + 'IV',   'heading': 'Book IV — Grief, Friendship, and Restlessness'},
      {'page': _CONFESSIONS_BASE + 'V',    'heading': 'Book V — Leaving Carthage; Rome and Milan'},
      {'page': _CONFESSIONS_BASE + 'VI',   'heading': 'Book VI — Ambrose and the Approach to Truth'},
      {'page': _CONFESSIONS_BASE + 'VII',  'heading': 'Book VII — Neo-Platonism and the Vision of God'},
      {'page': _CONFESSIONS_BASE + 'VIII', 'heading': 'Book VIII — The Conversion in the Garden'},
      {'page': _CONFESSIONS_BASE + 'IX',   'heading': 'Book IX — Baptism, Monica\'s Death, and Praise'},
      {'page': _CONFESSIONS_BASE + 'X',    'heading': 'Book X — Memory, Temptation, and the Mediator'},
      {'page': _CONFESSIONS_BASE + 'XI',   'heading': 'Book XI — Time and Eternity'},
      {'page': _CONFESSIONS_BASE + 'XII',  'heading': 'Book XII — Creation and Scripture'},
      {'page': _CONFESSIONS_BASE + 'XIII', 'heading': 'Book XIII — The Six Days and the Sabbath Rest'},
    ],
    'index_meta': {
      'abbrev': 'AugCon', 'title': 'Confessions',
      'year': 400, 'type': 'father', 'tradition': 'patristic',
      'author': 'Augustine of Hippo',
      'desc': '"Our heart is restless until it rests in Thee" — autobiography, prayer, and meditation on grace across 13 books.',
    },
  },

  # ── Medieval ──────────────────────────────────────────────────────────────
  {
    'id':   'anselm-proslogion',
    'page': 'Proslogion',
    'split_h': 'h2', 'max_sections': 6,
    'index_meta': {
      'abbrev': 'AnsPro', 'title': 'Proslogion',
      'year': 1078, 'type': 'father', 'tradition': 'catholic',
      'author': 'Anselm of Canterbury',
      'desc': 'The ontological argument for God\'s existence: "that than which nothing greater can be conceived" — faith seeking understanding.',
    },
  },

  # ── Reformation ───────────────────────────────────────────────────────────
  {
    'id':   'luther-95-theses',
    'page': 'Works of Martin Luther, with introductions and notes/Volume 1/Disputation on Indulgences',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': '95T', 'title': 'Ninety-Five Theses',
      'year': 1517, 'type': 'confession', 'tradition': 'lutheran',
      'era': 'reformation',
      'author': 'Martin Luther',
      'desc': 'The 95 propositions challenging indulgences that sparked the Reformation — posted at Wittenberg, October 1517.',
    },
  },

  # ── More Apostolic Fathers ────────────────────────────────────────────────
  {
    'id':   'didache',
    'page': 'Didache (Lightfoot translation)',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'Did', 'title': 'Didache',
      'year': 100, 'type': 'father', 'tradition': 'patristic',
      'era': 'patristic',
      'desc': '"The Teaching of the Twelve Apostles" — the earliest known manual of Christian ethics, baptism, Eucharist, and church order.',
    },
  },
  {
    'id':   'epistle-of-barnabas',
    'page': 'Ante-Nicene Christian Library/Epistle of Barnabas',
    'split_h': 'h2', 'max_sections': 4,
    'index_meta': {
      'abbrev': 'Barn', 'title': 'Epistle of Barnabas',
      'year': 130, 'type': 'father', 'tradition': 'patristic',
      'era': 'patristic',
      'desc': 'An early letter reading the Old Testament typologically — the covenant, circumcision, and sabbath fulfilled in Christ.',
    },
  },
  {
    'id':   'epistle-to-diognetus',
    'page': 'Ante-Nicene Fathers/Volume I/Epistle to Diognetus',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'Diog', 'title': 'Epistle to Diognetus',
      'year': 150, 'type': 'father', 'tradition': 'patristic',
      'era': 'patristic',
      'desc': '"What the soul is to the body, Christians are to the world" — an elegant early apology on the Christian way of life.',
    },
  },
  {
    'id':   'shepherd-of-hermas',
    'subpages': [
      {'page': 'Shepherd of Hermas: Book of Visions (Lightfoot translation)',   'heading': 'Book I — The Visions'},
      {'page': 'Shepherd of Hermas: Book of Mandates (Lightfoot translation)',   'heading': 'Book II — The Mandates'},
      {'page': 'Shepherd of Hermas: Book of Similitudes (Lightfoot translation)','heading': 'Book III — The Similitudes'},
    ],
    'index_meta': {
      'abbrev': 'Herm', 'title': 'The Shepherd of Hermas',
      'year': 140, 'type': 'father', 'tradition': 'patristic',
      'era': 'patristic',
      'desc': 'Visions, Mandates, and Similitudes — an influential early Christian apocalypse on repentance and the church as a building under construction.',
    },
  },

  # ── Medieval ──────────────────────────────────────────────────────────────
  {
    'id':   'anselm-cur-deus-homo',
    # grouped_pages: fetch chapters individually and concatenate into sections
    'grouped_pages': [
      {'heading': 'Preface',
       'pages':   [_CDH_BASE + '/Preface']},
      {'heading': 'Book I — Why God Must Become Man',
       'pages':   [f'{_CDH_BASE}/Book First/Chapter {i}' for i in range(1, 26)]},
      {'heading': 'Book II — How God Became Man',
       'pages':   [f'{_CDH_BASE}/Book Second/Chapter {i}' for i in range(1, 26)]},
    ],
    'index_meta': {
      'abbrev': 'AnsCDH', 'title': 'Cur Deus Homo',
      'year': 1098, 'type': 'father', 'tradition': 'catholic',
      'era': 'medieval',
      'author': 'Anselm of Canterbury',
      'desc': '"Why Did God Become Man?" — the foundational satisfaction theory of the Atonement, presented as a dialogue.',
    },
  },
  {
    'id':   'imitation-of-christ',
    # grouped_pages: each book becomes one section (Book III split due to length)
    'grouped_pages': [
      {'heading': 'Book I — Admonitions Profitable for the Spiritual Life',
       'pages':   _imit_pages('I', 1, 25)},
      {'heading': 'Book II — Admonitions Concerning the Inner Life',
       'pages':   _imit_pages('II', 1, 12)},
      {'heading': 'Book III — Of Internal Consolation (Ch. 1–30)',
       'pages':   _imit_pages('III', 1, 30)},
      {'heading': 'Book III — Of Internal Consolation (Ch. 31–59)',
       'pages':   _imit_pages('III', 31, 59)},
      {'heading': 'Book IV — Of the Sacrament of the Altar',
       'pages':   _imit_pages('IV', 1, 18)},
    ],
    'index_meta': {
      'abbrev': 'Imit', 'title': 'The Imitation of Christ',
      'year': 1427, 'type': 'father', 'tradition': 'catholic',
      'era': 'medieval',
      'author': 'Thomas à Kempis',
      'desc': 'The most-read Christian devotional after the Bible — four books on forsaking the world, following Christ inwardly, and the Eucharist.',
    },
  },

  # ── More Reformation ──────────────────────────────────────────────────────
  {
    'id':   'luther-freedom-christian',
    'page': 'Concerning Christian Liberty',
    'split_h': 'h2', 'max_sections': 1,
    'index_meta': {
      'abbrev': 'LutFC', 'title': 'The Freedom of a Christian',
      'year': 1520, 'type': 'confession', 'tradition': 'lutheran',
      'era': 'reformation',
      'author': 'Martin Luther',
      'desc': '"A Christian is a perfectly free lord of all, subject to none; a perfectly dutiful servant of all, subject to all."',
    },
  },

  # ── Post-Reformation / Puritan ────────────────────────────────────────────
  {
    'id':   'pilgrims-progress',
    'subpages': [
      {'page': _PP_BASE + 'First Stage',   'heading': 'Stage 1 — The Burden and the Wicket Gate'},
      {'page': _PP_BASE + 'Second Stage',  'heading': 'Stage 2 — The House Beautiful'},
      {'page': _PP_BASE + 'Third Stage',   'heading': 'Stage 3 — The Valley of Humiliation'},
      {'page': _PP_BASE + 'Fourth Stage',  'heading': 'Stage 4 — Doubting Castle'},
      {'page': _PP_BASE + 'Fifth Stage',   'heading': 'Stage 5 — The Delectable Mountains'},
      {'page': _PP_BASE + 'Sixth Stage',   'heading': 'Stage 6 — Vanity Fair'},
      {'page': _PP_BASE + 'Seventh Stage', 'heading': 'Stage 7 — By-Path Meadow'},
      {'page': _PP_BASE + 'Eighth Stage',  'heading': 'Stage 8 — Beulah Land'},
      {'page': _PP_BASE + 'Ninth Stage',   'heading': 'Stage 9 — The Celestial City (Part II begins)'},
      {'page': _PP_BASE + 'Tenth Stage',   'heading': 'Stage 10 — The End of the Journey'},
    ],
    'index_meta': {
      'abbrev': 'PilProg', 'title': "Pilgrim's Progress",
      'year': 1678, 'type': 'father', 'tradition': 'baptist',
      'era': 'post-reformation',
      'author': 'John Bunyan',
      'desc': "The great allegorical journey of Christian from the City of Destruction to the Celestial City.",
    },
  },
  {
    'id':   'edwards-sinners',
    'page': 'Sinners in the Hands of an Angry God',
    'split_h': 'h2', 'max_sections': 1,
    'index_meta': {
      'abbrev': 'EdwSin', 'title': 'Sinners in the Hands of an Angry God',
      'year': 1741, 'type': 'father', 'tradition': 'reformed',
      'era': 'post-reformation',
      'author': 'Jonathan Edwards',
      'desc': 'The most famous sermon of the Great Awakening — on God\'s wrath, sovereign mercy, and the urgency of repentance.',
    },
  },

  # ── Lutheran ───────────────────────────────────────────────────────────────
  {
    'id':   'luther-small-catechism',
    'page': 'Concordia Triglotta/The Small Catechism',
    'split_h': 'h2', 'max_sections': 6,
    'index_meta': {
      'abbrev': 'SC', 'title': 'Small Catechism',
      'year': 1529, 'type': 'catechism', 'tradition': 'lutheran',
      'era': 'reformation',
      'author': 'Martin Luther',
      'desc': 'Luther\'s brief instruction for household heads — the Ten Commandments, Creed, Lord\'s Prayer, Baptism, Confession, and the Lord\'s Supper.',
    },
  },

  # ── Reformed / Puritan ────────────────────────────────────────────────────
  {
    'id': 'machen-christianity-liberalism',
    'subpages': [
      {'page': 'Christianity and Liberalism/Chapter 1', 'heading': 'Chapter 1 — Liberalism'},
      {'page': 'Christianity and Liberalism/Chapter 2', 'heading': 'Chapter 2 — Doctrine'},
      {'page': 'Christianity and Liberalism/Chapter 3', 'heading': 'Chapter 3 — God and Man'},
      {'page': 'Christianity and Liberalism/Chapter 4', 'heading': 'Chapter 4 — The Bible'},
      {'page': 'Christianity and Liberalism/Chapter 5', 'heading': 'Chapter 5 — Christ'},
      {'page': 'Christianity and Liberalism/Chapter 6', 'heading': 'Chapter 6 — Salvation'},
      {'page': 'Christianity and Liberalism/Chapter 7', 'heading': 'Chapter 7 — The Church'},
    ],
    'index_meta': {
      'abbrev': 'MachCL', 'title': 'Christianity and Liberalism',
      'year': 1923, 'type': 'father', 'tradition': 'reformed',
      'era': 'modern',
      'author': 'J. Gresham Machen',
      'desc': 'The classic defence of historic Christianity against early twentieth-century theological liberalism — arguing they are two distinct religions.',
    },
  },

  # ── Anglican Evangelical ──────────────────────────────────────────────────
  {
    'id': 'ryle-holiness',
    # grouped_pages: group into 4 sections by thematic clusters
    'grouped_pages': [
      {'heading': 'Part 1 — Introduction and Sin (Introduction, Ch. 1–5)',
       'pages': [
         'Holiness: Its Nature, Hindrances, Difficulties and Roots/Introduction',
       ] + [f'Holiness: Its Nature, Hindrances, Difficulties and Roots/Chapter {i}' for i in range(1, 6)]},
      {'heading': 'Part 2 — The Nature of Holiness (Ch. 6–10)',
       'pages': [f'Holiness: Its Nature, Hindrances, Difficulties and Roots/Chapter {i}' for i in range(6, 11)]},
      {'heading': 'Part 3 — Examples of Holiness (Ch. 11–15)',
       'pages': [f'Holiness: Its Nature, Hindrances, Difficulties and Roots/Chapter {i}' for i in range(11, 16)]},
      {'heading': 'Part 4 — Practical Holiness (Ch. 16–20)',
       'pages': [f'Holiness: Its Nature, Hindrances, Difficulties and Roots/Chapter {i}' for i in range(16, 21)]},
    ],
    'index_meta': {
      'abbrev': 'RyleH', 'title': 'Holiness',
      'year': 1879, 'type': 'father', 'tradition': 'anglican',
      'era': 'modern',
      'author': 'J. C. Ryle',
      'desc': 'The Victorian bishop\'s thorough and searching treatment of sin, sanctification, the fight of faith, and practical godliness — deeply Puritan in spirit.',
    },
  },

  # ── Chesterton ────────────────────────────────────────────────────────────
  {
    'id': 'chesterton-orthodoxy',
    'subpages': [
      {'page': 'Orthodoxy/Chapter 1', 'heading': 'Chapter 1 — Introduction in Defence of Everything Else'},
      {'page': 'Orthodoxy/Chapter 2', 'heading': 'Chapter 2 — The Maniac'},
      {'page': 'Orthodoxy/Chapter 3', 'heading': 'Chapter 3 — The Suicide of Thought'},
      {'page': 'Orthodoxy/Chapter 4', 'heading': 'Chapter 4 — The Ethics of Elfland'},
      {'page': 'Orthodoxy/Chapter 5', 'heading': 'Chapter 5 — The Flag of the World'},
      {'page': 'Orthodoxy/Chapter 6', 'heading': 'Chapter 6 — The Paradoxes of Christianity'},
      {'page': 'Orthodoxy/Chapter 7', 'heading': 'Chapter 7 — The Eternal Revolution'},
      {'page': 'Orthodoxy/Chapter 8', 'heading': 'Chapter 8 — The Romance of Orthodoxy'},
      {'page': 'Orthodoxy/Chapter 9', 'heading': 'Chapter 9 — Authority and the Adventurer'},
    ],
    'index_meta': {
      'abbrev': 'Orth', 'title': 'Orthodoxy',
      'year': 1908, 'type': 'father', 'tradition': 'catholic',
      'era': 'modern',
      'author': 'G.K. Chesterton',
      'desc': 'Chesterton\'s intellectual autobiography of faith — the argument from wonder, the paradoxes of Christianity, and why orthodoxy is the most adventurous idea in the world.',
    },
  },

  # ── Andrew Murray ─────────────────────────────────────────────────────────
  {
    'id':   'murray-humility',
    'page': 'Humility (Murray)',
    'split_h': 'h2', 'max_sections': 4,
    'index_meta': {
      'abbrev': 'MurH', 'title': 'Humility',
      'year': 1895, 'type': 'father', 'tradition': 'reformed',
      'era': 'modern',
      'author': 'Andrew Murray',
      'desc': 'Murray\'s searching study of the one virtue that underlies all others — Christ as the model of humility, and self-emptying as the path to union with God.',
    },
  },
  {
    'id':   'murray-deeper-christian-life',
    'page': 'The Deeper Christian Life',
    'split_h': 'h2', 'max_sections': 4,
    'index_meta': {
      'abbrev': 'MurDCL', 'title': 'The Deeper Christian Life',
      'year': 1895, 'type': 'father', 'tradition': 'reformed',
      'era': 'modern',
      'author': 'Andrew Murray',
      'desc': 'Murray\'s practical guide to Spirit-filled living — daily fellowship with God, the fullness of the Spirit, abiding in Christ, and the consecrated life of service.',
    },
  },

  # ── Spurgeon ──────────────────────────────────────────────────────────────
  {
    'id': 'spurgeon-all-of-grace',
    'subpages': [
      {'page': f'All of Grace/Chapter {i}', 'heading': f'Chapter {i}'}
      for i in range(1, 21)
    ],
    'index_meta': {
      'abbrev': 'AoG', 'title': 'All of Grace',
      'year': 1886, 'type': 'father', 'tradition': 'baptist',
      'era': 'modern',
      'author': 'Charles Spurgeon',
      'desc': 'Spurgeon\'s most-read work — a plain-hearted appeal to sinners to receive the free grace of God in Christ, without money and without price.',
    },
  },

  # ── John Wesley ───────────────────────────────────────────────────────────
  {
    'id': 'wesley-sermons',
    'subpages': [
      {'page': 'Salvation by Faith',               'heading': 'Sermon 1 — Salvation by Faith'},
      {'page': 'The Almost Christian (Wesley)',     'heading': 'Sermon 2 — The Almost Christian'},
      {'page': 'Scriptural Christianity',           'heading': 'Sermon 3 — Scriptural Christianity'},
      {'page': 'The Means of Grace',                'heading': 'Sermon 4 — The Means of Grace'},
      {'page': 'The Circumcision of the Heart',     'heading': 'Sermon 5 — The Circumcision of the Heart'},
      {'page': 'Catholic Spirit',                   'heading': 'Sermon 6 — Catholic Spirit'},
    ],
    'index_meta': {
      'abbrev': 'WesS', 'title': 'Selected Sermons',
      'year': 1746, 'type': 'father', 'tradition': 'methodist',
      'era': 'modern',
      'author': 'John Wesley',
      'desc': 'Six of Wesley\'s Forty-Four Standard Sermons — salvation by faith, scriptural Christianity, the means of grace, and the catholic spirit of Christian unity.',
    },
  },

]

# ---------------------------------------------------------------------------
# HTML cleaning
# ---------------------------------------------------------------------------

_STRIP_SELECTORS = [
  # Wikisource chrome
  '.mw-editsection',
  '#toc', '.toc',
  '.navbox', '.navbox-inner',
  '.reflist', '.references', '.mw-references-wrap',
  '.printfooter',
  '#catlinks',
  '.sister-project',
  '.noprint',
  'sup.reference', 'sup.cite_ref',
  '.mw-empty-elt',
  '.ws-noexport',
  # Running header / footer / navigation
  '.ws-header', '.ws-footer', '.wst-header-structure', '.wst-header',
  '.wst-footer',
  # Decorative and metadata elements
  '.wst-custom-rule',     # ornamental dividers
  '.wst-gap',             # horizontal gap spans in two-column tables
  '.pagenum', '.ws-pagenum',
  '.wst-nop',             # empty page spacers
  'span.anchor',          # invisible anchor spans
  # License and collapsible metadata boxes
  '.licenseContainer', '.mw-collapsible-box', '.mw-collapsible',
  # Sister-project banners
  '.sister-project',
]

def _is_footnote_div(div):
  """True if a prp-pages-output div contains only footnotes/references."""
  text = div.get_text(strip=True)
  if not text:
    return True
  # Footnote divs typically start with an arrow (↑) or are very short
  if text.startswith('↑') or text.startswith('†'):
    return True
  paras = div.find_all('p')
  text_paras = [p for p in paras if len(p.get_text(strip=True)) > 30]
  # If almost no substantial paragraphs, it's probably just notes
  return len(text_paras) == 0


def _inner_html_of(tag):
  """Return the inner HTML of a tag (its children as a string)."""
  return ''.join(str(c) for c in tag.children)


def _extract_content_from_prp_pages(content):
  """
  For pages that store text in .prp-pages-output divs, extract the substantive
  inner HTML so that heading divs (wst-center, mw-heading) become top-level
  elements in the returned string.  Returns (html_string, is_two_column).
  """
  # Detect two-column ANCL layout (shorter + longer recension side by side).
  has_two_col = bool(content.find(class_='wst-gap'))
  if has_two_col:
    parts = []
    for table in content.find_all('table'):
      for row in table.find_all('tr'):
        cells = [td for td in row.find_all('td', recursive=False)]
        if len(cells) == 3:
          # Last cell = longer recension; unwrap prp-pages-output
          pp = cells[2].find(class_='prp-pages-output')
          if pp and not _is_footnote_div(pp):
            parts.append(_inner_html_of(pp))
        elif len(cells) == 1:
          # Heading row shared between columns
          pp = cells[0].find(class_='prp-pages-output')
          if pp and not _is_footnote_div(pp):
            parts.append(_inner_html_of(pp))
    return '\n'.join(parts), True

  # Single-column: concatenate inner HTML of all substantive prp-pages-output divs
  pp_divs = content.find_all(class_='prp-pages-output')
  if pp_divs:
    parts = [_inner_html_of(d) for d in pp_divs if not _is_footnote_div(d)]
    return '\n'.join(parts), False

  return None, False


def _clean_soup(soup):
  # Remove inline style/link/meta tags injected by MediaWiki
  for tag in soup.find_all(['style', 'link', 'meta']):
    tag.decompose()
  # Remove all images (decorative rules, icons, etc.)
  for img in soup.find_all('img'):
    img.decompose()
  # Remove HTML comments (contains parser stats, etc.)
  for comment in soup.find_all(string=lambda t: isinstance(t, type(t)) and
                                                str(t).startswith(('\n<!--', '<!--'))):
    try: comment.extract()
    except Exception: pass

  for sel in _STRIP_SELECTORS:
    for el in soup.select(sel):
      el.decompose()

  # Remove empty paragraphs
  for p in soup.find_all('p'):
    if not p.get_text(strip=True):
      p.decompose()

  return soup


def _inner_html(tag):
  return ''.join(str(c) for c in tag.children)


# ---------------------------------------------------------------------------
# Section splitting from a single page
# ---------------------------------------------------------------------------

def _is_heading_div(tag, split_h):
  """Return True if tag is a div.mw-heading wrapping the target heading level."""
  if tag.name != 'div':
    return False
  classes = tag.get('class', [])
  return 'mw-heading' in classes and tag.find(split_h) is not None


def _is_wst_chapter_heading(tag):
  """Return True if tag is a div.wst-center that looks like a chapter title."""
  if tag.name != 'div':
    return False
  classes = tag.get('class', [])
  if 'wst-center' not in classes:
    return False
  text = tag.get_text(strip=True)
  # Short centred text that starts with "Chap." or "Chapter" is a heading.
  # Longer wst-center blocks are document titles — skip them.
  return bool(text) and len(text) < 120 and (
    text.lower().startswith(('chap.', 'chapter ', 'sect.', 'part '))
    or (len(text) < 80 and '.' not in text[:3])
  )


def _heading_text_from(tag, split_h):
  """Extract clean heading text from various heading wrapper forms."""
  if tag.name == split_h:
    return tag.get_text(separator=' ', strip=True)
  inner = tag.find(split_h)
  if inner:
    return inner.get_text(separator=' ', strip=True)
  return tag.get_text(separator=' ', strip=True)


def _split_into_sections(soup, split_h='h2', max_sections=0):
  """
  Split content into {heading, html} sections.  Handles:
  - Bare <h2> or <h3>
  - Modern <div class="mw-heading"><h2> wrappers (new Wikisource format)
  - <div class="wst-center"> chapter headings (ANCL/Proofread pages)
  - prp-pages-output multi-div layout

  If the page uses .prp-pages-output divs, extract and concatenate their
  content first, then split by headings within that content.
  """
  content = soup.find(class_='mw-parser-output') or soup

  # Pages with prp-pages-output: extract the main text first
  pp_html, two_col = _extract_content_from_prp_pages(content)
  if pp_html:
    # Re-parse the extracted HTML for further splitting
    content = BeautifulSoup(pp_html, 'html.parser')

  sections        = []
  current_heading = ''
  current_nodes   = []

  def _flush():
    if current_nodes:
      html = ''.join(str(n) for n in current_nodes).strip()
      if html:
        sections.append({'heading': current_heading, 'html': html})

  for child in list(content.children):
    if not isinstance(child, (Tag, NavigableString)):
      continue
    if isinstance(child, NavigableString):
      if str(child).strip():
        current_nodes.append(child)
      continue

    is_heading = (
      child.name == split_h
      or _is_heading_div(child, split_h)
      or _is_wst_chapter_heading(child)
    )
    if is_heading:
      _flush()
      current_heading = _heading_text_from(child, split_h)
      current_nodes   = []
    else:
      current_nodes.append(child)

  _flush()

  # Fallback: no sections found — whole content is one section
  if not sections:
    html = pp_html if pp_html else str(content)
    sections = [{'heading': '', 'html': html}]

  # Remove leading empty/boilerplate sections (no text content)
  while sections and not BeautifulSoup(sections[0]['html'], 'html.parser').get_text(strip=True):
    sections.pop(0)

  # Cap section count using even distribution (not tail-merge)
  if max_sections and len(sections) > max_sections:
    n          = len(sections)
    group_size = n / max_sections
    groups     = []
    for i in range(max_sections):
      start = round(i * group_size)
      end   = round((i + 1) * group_size)
      chunk = sections[start:end]
      if chunk:
        groups.append({
          'heading': chunk[0]['heading'],
          'html':    '\n'.join(s['html'] for s in chunk),
        })
    sections = groups

  return sections


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def _wrap_sections(sections):
  parts = []
  for s in sections:
    heading = s['heading'].replace('"', '&quot;')
    parts.append(f'<section data-heading="{heading}">\n{s["html"]}\n</section>')
  return '\n\n'.join(parts) + '\n'


# ---------------------------------------------------------------------------
# Wikisource fetch
# ---------------------------------------------------------------------------

def _fetch_page_soup(page_title):
  """Fetch and clean a Wikisource page, returning a BeautifulSoup."""
  params = {
    'action':             'parse',
    'page':               page_title,
    'prop':               'text',
    'disableeditsection': 'true',
    'disabletoc':         'true',
    'format':             'json',
  }
  for attempt in range(3):
    try:
      resp = requests.get(WS_API, params=params, headers=HEADERS, timeout=30)
      resp.raise_for_status()
      if not resp.text:
        raise ValueError('Empty response body')
      data = resp.json()
      break
    except (requests.RequestException, ValueError) as e:
      if attempt < 2:
        print(f'    retry {attempt+1} after error: {e}')
        time.sleep(3)
      else:
        raise

  if 'error' in data:
    code = data['error'].get('code', '')
    info = data['error'].get('info', '')
    raise ValueError(f'Wikisource API error [{code}]: {info}')

  html  = data['parse']['text']['*']
  soup  = BeautifulSoup(html, 'html.parser')
  _clean_soup(soup)
  return soup


# ---------------------------------------------------------------------------
# Index patching
# ---------------------------------------------------------------------------

def _load_index():
  with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    return json.load(f)


def _save_index(index):
  with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    json.dump(index, f, indent=2, ensure_ascii=False)
    f.write('\n')


def _patch_index(doc_id, html_filename, meta):
  index    = _load_index()
  existing = next((d for d in index if d['id'] == doc_id), None)
  if existing:
    existing['html_url'] = html_filename
    for k, v in meta.items():
      existing.setdefault(k, v)
    print(f'  [index] updated {doc_id}')
  else:
    index.append({'id': doc_id, 'html_url': html_filename, **meta})
    print(f'  [index] added   {doc_id}')
  _save_index(index)


# ---------------------------------------------------------------------------
# Core fetch logic
# ---------------------------------------------------------------------------

def fetch_doc(entry, dry_run=False, update_index=False):
  doc_id   = entry['id']
  meta     = entry.get('index_meta', {})
  out_file = doc_id + '.html'
  out_path = os.path.join(HTML_DIR, out_file)

  print(f'\n[{doc_id}]')

  # ── Determine source mode ──────────────────────────────────────────────
  if 'grouped_pages' in entry:
    gp_list = entry['grouped_pages']
    total_pages = sum(len(g['pages']) for g in gp_list)
    print(f'  mode: grouped_pages ({len(gp_list)} groups, {total_pages} pages)')
  elif 'subpages' in entry:
    sp_list = entry['subpages']
    print(f'  mode: subpages ({len(sp_list)} pages)')
    for sp in sp_list:
      print(f'    {sp["heading"]} ← {sp["page"]}')
  else:
    print(f'  mode: single page')
    print(f'  page: {entry["page"]}')

  if dry_run:
    print('  [dry-run] skipping fetch')
    return True

  # ── Fetch content ──────────────────────────────────────────────────────
  try:
    if 'grouped_pages' in entry:
      # Each group becomes one section; missing chapter pages are skipped silently
      gp_list   = entry['grouped_pages']
      sections  = []
      req_count = 0
      for group in gp_list:
        print(f'  group: {group["heading"][:60]}…', flush=True)
        html_parts = []
        for page_title in group['pages']:
          if req_count > 0:
            time.sleep(RATE_DELAY)
          req_count += 1
          try:
            soup    = _fetch_page_soup(page_title)
            content = soup.find(class_='mw-parser-output') or soup
            html_parts.append(str(content))
          except ValueError as e:
            if 'missingtitle' in str(e):
              pass  # missing chapter — skip quietly
            else:
              print(f'    skip [{page_title}]: {e}')
        if html_parts:
          sections.append({'heading': group['heading'], 'html': '\n'.join(html_parts)})
          print(f'    → {len(html_parts)} pages fetched')

    elif 'subpages' in entry:
      sections = []
      for i, sp in enumerate(entry['subpages']):
        if i > 0:
          time.sleep(RATE_DELAY)
        print(f'  fetching {sp["heading"]}…', end='', flush=True)
        soup    = _fetch_page_soup(sp['page'])
        content = soup.find(class_='mw-parser-output') or soup
        html    = str(content)
        sections.append({'heading': sp['heading'], 'html': html})
        print(f' OK ({len(content.find_all("p"))}p)')

    else:
      split_h   = entry.get('split_h', 'h2')
      max_secs  = entry.get('max_sections', 0)
      soup      = _fetch_page_soup(entry['page'])
      sections  = _split_into_sections(soup, split_h=split_h, max_sections=max_secs)
      print(f'  {len(sections)} section(s): ' + ', '.join(
        repr(s['heading'][:40]) for s in sections
      ))

  except Exception as e:
    print(f'\n  ERROR: {e}')
    return False

  # ── Write output ───────────────────────────────────────────────────────
  os.makedirs(HTML_DIR, exist_ok=True)
  with open(out_path, 'w', encoding='utf-8') as f:
    f.write(_wrap_sections(sections))
  print(f'  wrote {out_path}')

  if update_index:
    _patch_index(doc_id, out_file, meta)

  return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
  parser = argparse.ArgumentParser(description='Fetch library docs from Wikisource')
  parser.add_argument('--doc',          help='Fetch only this doc id')
  parser.add_argument('--all',          action='store_true', help='Re-fetch even existing files')
  parser.add_argument('--dry-run',      action='store_true', help='Print plan without fetching')
  parser.add_argument('--update-index', action='store_true', help='Patch data/library/index.json')
  parser.add_argument('--list',         action='store_true', help='List manifest entries')
  args = parser.parse_args()

  if args.list:
    for e in MANIFEST:
      exists = '✓' if os.path.exists(os.path.join(HTML_DIR, e['id'] + '.html')) else ' '
      if 'grouped_pages' in e:
        n = sum(len(g['pages']) for g in e['grouped_pages'])
        mode = f"{len(e['grouped_pages'])} groups ({n} pages)"
      elif 'subpages' in e:
        mode = f"{len(e['subpages'])} subpages"
      else:
        mode = e.get('page', '')[:50]
      print(f"  [{exists}] {e['id']:45s}  {mode}")
    return

  entries = MANIFEST
  if args.doc:
    entries = [e for e in MANIFEST if e['id'] == args.doc]
    if not entries:
      print(f'ERROR: "{args.doc}" not found in manifest')
      sys.exit(1)

  total = ok = 0
  for i, entry in enumerate(entries):
    out_path = os.path.join(HTML_DIR, entry['id'] + '.html')
    if not args.all and not args.dry_run and os.path.exists(out_path):
      print(f"[{entry['id']}] already exists — skipping (--all to re-fetch)")
      ok += 1; total += 1
      continue

    total += 1
    if i > 0 and not args.dry_run:
      time.sleep(RATE_DELAY)
    if fetch_doc(entry, dry_run=args.dry_run, update_index=args.update_index):
      ok += 1

  print(f'\nDone: {ok}/{total} documents processed')


if __name__ == '__main__':
  main()
