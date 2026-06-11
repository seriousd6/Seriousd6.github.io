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

GUTENBERG_URL_PATTERNS = [
  'https://www.gutenberg.org/files/{id}/{id}-h/{id}-h.htm',
  'https://www.gutenberg.org/cache/epub/{id}/pg{id}-images.html',
  'https://www.gutenberg.org/files/{id}/{id}.htm',
]

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
_ACTS_BASE = 'Nicene and Post-Nicene Fathers: Series I/Volume XI/On the Acts of the Apostles/'
_DP_BASE   = 'Ante-Nicene Fathers/Volume IV/Origen/Origen De Principiis/'
_TRENT_BASE = 'The Catechism of the Council of Trent/'


def _roman(n):
  """Convert integer to uppercase Roman numeral string."""
  vals = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
          (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
  r = ''
  for v, s in vals:
    while n >= v: r += s; n -= v
  return r


def _imit_pages(book, lo, hi):
  """Build a list of Imitation of Christ chapter page titles."""
  return [f'{_IMIT_BASE}/Book {book}/Chapter {_roman(i)}' for i in range(lo, hi + 1)]


_AC_BASE = 'Ante-Nicene Fathers/Volume IV/Origen/Origen Against Celsus'

def _ac_pages(book_roman, lo, hi, preface=False):
  """Build Wikisource page list for one book of Against Celsus."""
  pages = []
  if preface:
    pages.append(f'{_AC_BASE}/Book {book_roman}/Preface')
  pages += [f'{_AC_BASE}/Book {book_roman}/Chapter {_roman(i)}' for i in range(lo, hi + 1)]
  return pages


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

  # ─── APOSTOLIC FATHERS — 4 remaining Ignatius letters ────────────────────────
  {
    'id':   'ignatius-romans',
    'page': 'Ante-Nicene Christian Library/Epistle to the Romans',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'IgnR', 'title': 'Letter to the Romans',
      'year': 108, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Ignatius of Antioch',
      'desc': 'Ignatius\'s most passionate letter — written en route to martyrdom, pleading with Rome not to prevent his death so he may be "ground by the teeth of wild beasts" as wheat into bread for Christ.',
    },
  },
  {
    'id':   'ignatius-philadelphians',
    'page': 'Ante-Nicene Christian Library/Epistle to the Philadelphians',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'IgnPh', 'title': 'Letter to the Philadelphians',
      'year': 108, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Ignatius of Antioch',
      'desc': 'On unity around the one bishop, the danger of Judaizing schism, and the one Eucharist as the flesh of Christ and the one cup as his blood.',
    },
  },
  {
    'id':   'ignatius-smyrnaeans',
    'page': 'Ante-Nicene Christian Library/Epistle to the Smyrnaeans',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'IgnSm', 'title': 'Letter to the Smyrnaeans',
      'year': 108, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Ignatius of Antioch',
      'desc': 'The strongest anti-Docetic letter — Christ truly suffered and rose bodily; without the bishop there is no valid Eucharist, baptism, or love-feast.',
    },
  },
  {
    'id':   'ignatius-polycarp',
    'page': 'Ante-Nicene Christian Library/Epistle to Polycarp',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'IgnPo', 'title': 'Letter to Polycarp',
      'year': 108, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Ignatius of Antioch',
      'desc': 'Personal counsel from a martyr-bishop to a younger bishop on pastoral vigilance, duties of the flock, marriage in the Lord, and the spiritual warfare of ministry.',
    },
  },

  # ─── Athenagoras ──────────────────────────────────────────────────────────────
  {
    'id':   'athenagoras-writings',
    'subpages': [
      {'page': 'Ante-Nicene Christian Library/Plea for the Christians (Athenagoras)',
       'heading': 'A Plea for the Christians'},
      {'page': 'Ante-Nicene Christian Library/Treatise on the Resurrection of the Dead (Athenagoras)',
       'heading': 'On the Resurrection of the Dead'},
    ],
    'index_meta': {
      'abbrev': 'AthPl', 'title': 'Writings of Athenagoras',
      'year': 177, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Athenagoras of Athens',
      'desc': 'Two works: A Plea for the Christians (to Marcus Aurelius, refuting charges of atheism, incest, and cannibalism) and On the Resurrection of the Dead — the most philosophically polished early apology.',
    },
  },

  # ─── Justin Martyr — Dialogue with Trypho ────────────────────────────────────
  {
    'id':   'justin-dialogue-trypho',
    'page': 'Ante-Nicene Christian Library/Dialogue with Trypho',
    'split_h': 'h2', 'max_sections': 6,
    'index_meta': {
      'abbrev': 'JustDT', 'title': 'Dialogue with Trypho',
      'year': 155, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Justin Martyr',
      'desc': 'The longest surviving Christian apologetic dialogue — Justin debates a learned Jew on Christ as the fulfilment of Old Testament prophecy, the true circumcision, the two advents, and the calling of the Gentiles.',
    },
  },

  # ─── Irenaeus — Against Heresies ─────────────────────────────────────────────
  {
    'id': 'irenaeus-against-heresies',
    'grouped_pages': [
      {'heading': 'Book I — The Gnostic Systems Described and Exposed',
       'pages':   ['Ante-Nicene Christian Library/Against Heresies (Irenæus)/Book 1']},
      {'heading': 'Book II — Refutation of the Gnostic Systems',
       'pages':   ['Ante-Nicene Christian Library/Against Heresies (Irenæus)/Book 2']},
      {'heading': 'Book III — The Rule of Faith and Apostolic Tradition',
       'pages':   ['Ante-Nicene Christian Library/Against Heresies (Irenæus)/Book 3']},
      {'heading': 'Book IV — The Unity of the Two Testaments',
       'pages':   ['Ante-Nicene Christian Library/Against Heresies (Irenæus)/Book 4']},
      {'heading': 'Book V — The Resurrection and the Recapitulation',
       'pages':   ['Ante-Nicene Christian Library/Against Heresies (Irenæus)/Book 5']},
    ],
    'index_meta': {
      'abbrev': 'IrenAH', 'title': 'Against Heresies',
      'year': 180, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Irenaeus of Lyons',
      'desc': 'The foundational anti-Gnostic work in five books — exposing Valentinian and other Gnostic systems, then refuting them through the Rule of Faith, apostolic succession, and the unity of Scripture.',
    },
  },

  # ─── Tertullian ───────────────────────────────────────────────────────────────
  {
    'id': 'tertullian-apology',
    'grouped_pages': [
      {'heading': 'Chapters I–XII — Christians Are Not Criminals',
       'pages': [f"Ante-Nicene Fathers/Volume III/Apologetic/Apology/Chapter {r}"
                 for r in ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']]},
      {'heading': 'Chapters XIII–XXIV — Roman Religion and Christian Worship',
       'pages': [f"Ante-Nicene Fathers/Volume III/Apologetic/Apology/Chapter {r}"
                 for r in ['XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI','XXII','XXIII','XXIV']]},
      {'heading': 'Chapters XXV–XXXVIII — The Gods and the State',
       'pages': [f"Ante-Nicene Fathers/Volume III/Apologetic/Apology/Chapter {r}"
                 for r in ['XXV','XXVI','XXVII','XXVIII','XXIX','XXX','XXXI','XXXII','XXXIII','XXXIV','XXXV','XXXVI','XXXVII','XXXVIII']]},
      {'heading': 'Chapters XXXIX–L — Christian Community and Death',
       'pages': [f"Ante-Nicene Fathers/Volume III/Apologetic/Apology/Chapter {r}"
                 for r in ['XXXIX','XL','XLI','XLII','XLIII','XLIV','XLV','XLVI','XLVII','XLVIII','XLIX','L']]},
    ],
    'index_meta': {
      'abbrev': 'TertAp', 'title': 'Apology',
      'year': 197, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Tertullian',
      'desc': 'The greatest Latin apology — addressed to the governors of the Roman provinces, defending Christians against all legal and social charges and arguing that Christianity is the true philosophy.',
    },
  },
  {
    'id': 'tertullian-prescription',
    'grouped_pages': [
      {'heading': 'Chapters I–XXII — The Rule of Faith and Heretical Method',
       'pages': [f'Ante-Nicene Fathers/Volume III/Anti-Marcion/The Prescription Against Heretics/Chapter {r}'
                 for r in ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI','XXII']]},
      {'heading': 'Chapters XXIII–XLIV — The Prescription and Apostolic Tradition',
       'pages': [f'Ante-Nicene Fathers/Volume III/Anti-Marcion/The Prescription Against Heretics/Chapter {r}'
                 for r in ['XXIII','XXIV','XXV','XXVI','XXVII','XXVIII','XXIX','XXX','XXXI','XXXII','XXXIII','XXXIV','XXXV','XXXVI','XXXVII','XXXVIII','XXXIX','XL','XLI','XLII','XLIII','XLIV']]},
    ],
    'index_meta': {
      'abbrev': 'TertPH', 'title': 'The Prescription Against Heretics',
      'year': 200, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Tertullian',
      'desc': 'Tertullian\'s brilliant juridical argument that heretics have no legal standing to use Scripture — the apostolic churches possess the faith; heretics are trespassers. Foundational for the concept of tradition.',
    },
  },

  # ─── Origen ───────────────────────────────────────────────────────────────────
  {
    'id': 'origen-against-celsus',
    # grouped_pages: each group is a pair of books; each book's chapters fetched individually
    # (the book-level Wikisource pages are TOCs, not content — chapters must be fetched one by one)
    'grouped_pages': [
      {'heading': 'Books I–II — The Charges of Celsus Answered',
       'pages':   _ac_pages('I', 1, 71, preface=True) + _ac_pages('II', 1, 79)},
      {'heading': 'Books III–IV — Scripture, Miracles, and Prophecy',
       'pages':   _ac_pages('III', 1, 81) + _ac_pages('IV', 1, 99)},
      {'heading': 'Books V–VI — On the Soul, the Devil, and Greek Philosophy',
       'pages':   _ac_pages('V', 1, 65) + _ac_pages('VI', 1, 81)},
      {'heading': 'Books VII–VIII — On Prayer, Worship, and the Final Refutation',
       'pages':   _ac_pages('VII', 1, 70) + _ac_pages('VIII', 1, 76)},
    ],
    'index_meta': {
      'abbrev': 'OrigCC', 'title': 'Against Celsus',
      'year': 248, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Origen',
      'desc': 'Eight books answering Celsus\'s comprehensive attack on Christianity — the most extensive and systematic early Christian apologetic, covering history, philosophy, Scripture, miracles, and the nature of God.',
    },
  },

  # ─── Cyprian ──────────────────────────────────────────────────────────────────
  {
    'id':   'cyprian-on-unity',
    'page': 'Ante-Nicene Fathers/Volume V/Cyprian/The Treatises of Cyprian/On the Unity of the Church',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'CypU', 'title': 'On the Unity of the Church',
      'year': 251, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Cyprian of Carthage',
      'desc': '"He cannot have God for his father who has not the Church for his mother" — the foundational treatise on ecclesiology, written during the Novatianist schism, arguing that the one Church is the body of Christ.',
    },
  },
  {
    'id':   'cyprian-on-the-lapsed',
    'page': 'Ante-Nicene Fathers/Volume V/Cyprian/The Treatises of Cyprian/On the Lapsed',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'CypL', 'title': 'On the Lapsed',
      'year': 251, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Cyprian of Carthage',
      'desc': 'On the pastoral handling of those who lapsed during the Decian persecution — repentance, discipline, and the mercy of the Church toward those who fell and wish to return.',
    },
  },

  # ─── Athanasius ───────────────────────────────────────────────────────────────
  {
    'id': 'athanasius-on-incarnation',
    'subpages': [
      {'page': 'Nicene and Post-Nicene Fathers: Series II/Volume IV/Incarnation of the Word/Introduction',
       'heading': 'Introduction'},
      {'page': 'Nicene and Post-Nicene Fathers: Series II/Volume IV/Incarnation of the Word/On the Incarnation of the Word',
       'heading': 'On the Incarnation of the Word'},
    ],
    'index_meta': {
      'abbrev': 'AthInc', 'title': 'On the Incarnation',
      'year': 318, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Athanasius of Alexandria',
      'desc': '"He became what we are that He might make us what He is" — the young Athanasius\'s masterwork on why the Word became flesh, the nature of the Atonement, and the proof of the Resurrection. C.S. Lewis called it a masterpiece.',
    },
  },
  {
    'id': 'athanasius-life-of-antony',
    'grouped_pages': [
      {'heading': 'Preface and Chapters 1–35 — The Desert Calling and Early Contests',
       'pages': ['Nicene and Post-Nicene Fathers: Series II/Volume IV/Life of Antony/Vita Antoni/Preface'] +
                [f'Nicene and Post-Nicene Fathers: Series II/Volume IV/Life of Antony/Vita Antoni/Chapter {i}' for i in range(1, 36)]},
      {'heading': 'Chapters 36–70 — Miracles, Counsels, and the Arian Controversy',
       'pages': [f'Nicene and Post-Nicene Fathers: Series II/Volume IV/Life of Antony/Vita Antoni/Chapter {i}' for i in range(36, 71)]},
      {'heading': 'Chapters 71–94 — Last Years, Death, and Athanasius\'s Testimony',
       'pages': [f'Nicene and Post-Nicene Fathers: Series II/Volume IV/Life of Antony/Vita Antoni/Chapter {i}' for i in range(71, 95)]},
    ],
    'index_meta': {
      'abbrev': 'AthLA', 'title': 'Life of Antony',
      'year': 360, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Athanasius of Alexandria',
      'desc': 'The biography of St. Antony of Egypt that launched Christian monasticism — his combat with demons, his counsel to monks, and his long life of desert contemplation as a mirror of the spiritual warfare every Christian faces.',
    },
  },

  # ─── Gregory of Nazianzus — Five Theological Orations ────────────────────────
  {
    'id': 'gregory-nazianzus-orations',
    'grouped_pages': [
      {'heading': 'Prolegomena and Early Orations (Or. 1–3, 7–8)',
       'pages': [
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Prolegomena',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 1',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 2',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 3',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 7',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 8',
       ]},
      {'heading': 'Pastoral and Occasional Orations (Or. 12–21)',
       'pages': [
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 12',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 16',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 18',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 21',
       ]},
      {'heading': 'The Five Theological Orations (Or. 27–31)',
       'pages': [
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Introduction to the Theological Orations',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 27',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 28',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 29',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 30',
       ]},
      {'heading': 'Later Orations (Or. 32–45)',
       'pages': [
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 32',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 33',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 34',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 37',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 38',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 39',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 40',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 41',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 42',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 43',
         'Nicene and Post-Nicene Fathers: Series II/Volume VII/Orations of Gregory Nazianzen/Oration 45',
       ]},
    ],
    'index_meta': {
      'abbrev': 'GNazO', 'title': 'Orations of Gregory of Nazianzus',
      'year': 380, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Gregory of Nazianzus',
      'desc': 'The complete surviving orations including the Five Theological Orations (27–31) on the incomprehensibility of God, the eternal generation of the Son, and the full deity of the Spirit — the works that earned him the title "The Theologian."',
    },
  },

  # ─── Basil of Caesarea — On the Holy Spirit ──────────────────────────────────
  {
    'id': 'basil-on-holy-spirit',
    'grouped_pages': [
      {'heading': 'Chapters 1–15 — The Spirit in Scripture and Tradition',
       'pages': [f'Nicene and Post-Nicene Fathers: Series II/Volume VIII/De Spiritu Sancto/Chapter {i}' for i in range(1, 16)]},
      {'heading': 'Chapters 16–30 — The Deity and Worship of the Spirit',
       'pages': [f'Nicene and Post-Nicene Fathers: Series II/Volume VIII/De Spiritu Sancto/Chapter {i}' for i in range(16, 31)]},
    ],
    'index_meta': {
      'abbrev': 'BasHS', 'title': 'On the Holy Spirit',
      'year': 375, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Basil of Caesarea',
      'desc': 'Basil\'s defense of the full deity of the Holy Spirit — the doxological controversy, the Spirit as Lord and Life-giver, and the Spirit\'s indispensable role in sanctification and worship. Foundational for the Niceno-Constantinopolitan Creed.',
    },
  },

  # ─── Gregory of Nyssa ─────────────────────────────────────────────────────────
  {
    'id': 'gregory-nyssa-great-catechism',
    'grouped_pages': [
      {'heading': 'Prologue and Chapters I–XX — The Trinity, Creation, and the Fall',
       'pages': [
         'Nicene and Post-Nicene Fathers: Series II/Volume V/Apologetic Works/The Great Catechism/Prologue',
       ] + [f'Nicene and Post-Nicene Fathers: Series II/Volume V/Apologetic Works/The Great Catechism/Chapter {r}'
            for r in ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX']]},
      {'heading': 'Chapters XXI–XL — The Incarnation, Atonement, Baptism, and Eucharist',
       'pages': [f'Nicene and Post-Nicene Fathers: Series II/Volume V/Apologetic Works/The Great Catechism/Chapter {r}'
                 for r in ['XXI','XXII','XXIII','XXIV','XXV','XXVI','XXVII','XXVIII','XXIX','XXX','XXXI','XXXII','XXXIII','XXXIV','XXXV','XXXVI','XXXVII','XXXVIII','XXXIX','XL']]},
    ],
    'index_meta': {
      'abbrev': 'GNysC', 'title': 'The Great Catechism',
      'year': 385, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Gregory of Nyssa',
      'desc': 'A systematic apologetic theology — the Trinity, creation and the fall, the Incarnation and Atonement, baptism, and the Eucharist — written as a manual for catechists converting pagans, Jews, and heretics.',
    },
  },

  # ─── Cyril of Jerusalem — Catechetical Lectures ──────────────────────────────
  {
    'id': 'cyril-catechetical-lectures',
    'grouped_pages': [
      {'heading': 'Procatechesis and Lectures 1–8 — Baptismal Preparation and Sin',
       'pages': [f'Nicene and Post-Nicene Fathers: Series II/Volume VII/S. Cyril/Lecture {i}' for i in range(1, 9)]},
      {'heading': 'Lectures 9–18 — The Creed (God, Christ, the Holy Spirit)',
       'pages': [f'Nicene and Post-Nicene Fathers: Series II/Volume VII/S. Cyril/Lecture {i}' for i in range(9, 19)]},
      {'heading': 'Lectures 19–23 — The Mystagogical Catecheses (Baptism, Eucharist)',
       'pages': [f'Nicene and Post-Nicene Fathers: Series II/Volume VII/S. Cyril/Lecture {i}' for i in range(19, 24)]},
    ],
    'index_meta': {
      'abbrev': 'CyrCL', 'title': 'Catechetical Lectures',
      'year': 350, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Cyril of Jerusalem',
      'desc': '24 lectures delivered to candidates for baptism — a systematic introduction to the faith through the Creed, Scripture, the sacraments, and the Holy Spirit. The most complete surviving example of 4th-century catechesis.',
    },
  },

  # ─── Ambrose of Milan — On the Duties of the Clergy ─────────────────────────
  {
    'id': 'ambrose-on-duties',
    'grouped_pages': [
      {'heading': 'Book I — The Foundational Virtues',
       'pages':   ['Nicene and Post-Nicene Fathers: Series II/Volume X/Works/On the Duties of the Clergy/Book I']},
      {'heading': 'Book II — The Virtues in Their Social Expression',
       'pages':   ['Nicene and Post-Nicene Fathers: Series II/Volume X/Works/On the Duties of the Clergy/Book II']},
      {'heading': 'Book III — The Highest Good and the Perfect Man',
       'pages':   ['Nicene and Post-Nicene Fathers: Series II/Volume X/Works/On the Duties of the Clergy/Book III']},
    ],
    'index_meta': {
      'abbrev': 'AmbD', 'title': 'On the Duties of the Clergy',
      'year': 391, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Ambrose of Milan',
      'desc': 'Three books on clerical ethics modeled on Cicero\'s De Officiis but radically Christianized — the four cardinal virtues, true honor, charity as the highest good, and the example of the patriarchs and Christ.',
    },
  },

  # ─── Vincent of Lerins ────────────────────────────────────────────────────────
  {
    'id':   'vincent-of-lerins-commonitory',
    'page': 'Nicene and Post-Nicene Fathers: Series II/Volume XI/The Commonitory of Vincent of Lerins',
    'split_h': 'h2', 'max_sections': 4,
    'index_meta': {
      'abbrev': 'VinC', 'title': 'The Commonitory',
      'year': 434, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Vincent of Lerins',
      'desc': 'The "Vincentian Canon" — that true Catholic faith is what has been believed "everywhere, always, and by all." A concise guide to distinguishing orthodox development of doctrine from heretical innovation.',
    },
  },

  # ─── Augustine — City of God ──────────────────────────────────────────────────
  {
    'id': 'augustine-city-of-god',
    'grouped_pages': [
      {'heading': 'Books I–V — Against Paganism and Roman Virtue',
       'pages':   [f'Nicene and Post-Nicene Fathers: Series I/Volume II/City of God/Book {b}'
                   for b in ['I','II','III','IV','V']]},
      {'heading': 'Books VI–X — The Futility of Pagan Religion',
       'pages':   [f'Nicene and Post-Nicene Fathers: Series I/Volume II/City of God/Book {b}'
                   for b in ['VI','VII','VIII','IX','X']]},
      {'heading': 'Books XI–XIV — Origin of the Two Cities',
       'pages':   [f'Nicene and Post-Nicene Fathers: Series I/Volume II/City of God/Book {b}'
                   for b in ['XI','XII','XIII','XIV']]},
      {'heading': 'Books XV–XVIII — History of the Two Cities',
       'pages':   [f'Nicene and Post-Nicene Fathers: Series I/Volume II/City of God/Book {b}'
                   for b in ['XV','XVI','XVII','XVIII']]},
      {'heading': 'Books XIX–XXII — The End and Eternal Destiny of the Two Cities',
       'pages':   [f'Nicene and Post-Nicene Fathers: Series I/Volume II/City of God/Book {b}'
                   for b in ['XIX','XX','XXI','XXII']]},
    ],
    'index_meta': {
      'abbrev': 'AugCG', 'title': 'The City of God',
      'year': 426, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Augustine of Hippo',
      'desc': '22 books written in the wake of Rome\'s sack — demolishing pagan religion, tracing the two cities (love of God vs. love of self) through all history, and culminating in the eternal Sabbath of the City of God.',
    },
  },

  # ─── Augustine — On the Trinity ───────────────────────────────────────────────
  {
    'id': 'augustine-on-trinity',
    'grouped_pages': [
      {'heading': 'Books I–IV — The Scriptural Witness to the Trinity',
       'pages': [f'Nicene and Post-Nicene Fathers: Series I/Volume III/Doctrinal Treatises of St. Augustin/On the Holy Trinity/Book {r}' for r in ['I','II','III','IV']]},
      {'heading': 'Books V–VIII — The Eternal and Co-Equal Trinity',
       'pages': [f'Nicene and Post-Nicene Fathers: Series I/Volume III/Doctrinal Treatises of St. Augustin/On the Holy Trinity/Book {r}' for r in ['V','VI','VII','VIII']]},
      {'heading': 'Books IX–XII — Psychological Analogies: Mind, Knowledge, Love',
       'pages': [f'Nicene and Post-Nicene Fathers: Series I/Volume III/Doctrinal Treatises of St. Augustin/On the Holy Trinity/Book {r}' for r in ['IX','X','XI','XII']]},
      {'heading': 'Books XIII–XV — Word, Wisdom, Memory, and Eternal Contemplation',
       'pages': [f'Nicene and Post-Nicene Fathers: Series I/Volume III/Doctrinal Treatises of St. Augustin/On the Holy Trinity/Book {r}' for r in ['XIII','XIV','XV']]},
    ],
    'index_meta': {
      'abbrev': 'AugTr', 'title': 'On the Trinity',
      'year': 419, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Augustine of Hippo',
      'desc': '15 books — the first seven establishing Trinitarian doctrine from Scripture, the remaining eight exploring psychological analogies of the Trinity in memory, understanding, and will. Augustine\'s greatest speculative work.',
    },
  },

  # ─── Augustine — On Christian Doctrine ───────────────────────────────────────
  {
    'id': 'augustine-on-christian-doctrine',
    'subpages': [
      {'page': 'Nicene and Post-Nicene Fathers: Series I/Volume II/On Christian Doctrine/Book I',   'heading': 'Book I — Signs and Things'},
      {'page': 'Nicene and Post-Nicene Fathers: Series I/Volume II/On Christian Doctrine/Book II',  'heading': 'Book II — How to Interpret Signs'},
      {'page': 'Nicene and Post-Nicene Fathers: Series I/Volume II/On Christian Doctrine/Book III', 'heading': 'Book III — Ambiguous Signs'},
      {'page': 'Nicene and Post-Nicene Fathers: Series I/Volume II/On Christian Doctrine/Book IV',  'heading': 'Book IV — Christian Eloquence'},
    ],
    'index_meta': {
      'abbrev': 'AugCD', 'title': 'On Christian Doctrine',
      'year': 397, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Augustine of Hippo',
      'desc': 'The foundational text of Christian hermeneutics — how to read Scripture, the distinction between signs and things, the primacy of love in interpretation, and the cultivation of wisdom and eloquence for preaching.',
    },
  },

  # ─── Augustine — Enchiridion ──────────────────────────────────────────────────
  {
    'id':   'augustine-enchiridion',
    'page': 'Nicene and Post-Nicene Fathers: Series I/Volume III/Doctrinal Treatises of St. Augustin/The Enchiridion',
    'split_h': 'h2', 'max_sections': 4,
    'index_meta': {
      'abbrev': 'AugEn', 'title': 'Enchiridion (Faith, Hope, and Love)',
      'year': 421, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Augustine of Hippo',
      'desc': '"What should be believed, what hoped for, and what loved" — Augustine\'s compact handbook of Christian doctrine organized around the three theological virtues: the Creed (faith), the Lord\'s Prayer (hope), and the two great commandments (love).',
    },
  },

  # ─── Eusebius — Church History ────────────────────────────────────────────────
  {
    'id': 'eusebius-church-history',
    'grouped_pages': [
      {'heading': 'Books I–III — Christ, the Apostles, and the First Persecutions',
       'pages': [f'Nicene and Post-Nicene Fathers: Series II/Volume I/Church History of Eusebius/Book {r}' for r in ['I','II','III']]},
      {'heading': 'Books IV–VI — Second-Century Martyrs, Heresies, and Origen',
       'pages': [f'Nicene and Post-Nicene Fathers: Series II/Volume I/Church History of Eusebius/Book {r}' for r in ['IV','V','VI']]},
      {'heading': 'Books VII–X — The Great Persecution to the Triumph of Constantine',
       'pages': [f'Nicene and Post-Nicene Fathers: Series II/Volume I/Church History of Eusebius/Book {r}' for r in ['VII','VIII','IX','X']]},
    ],
    'index_meta': {
      'abbrev': 'EusEH', 'title': 'Ecclesiastical History',
      'year': 313, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Eusebius of Caesarea',
      'desc': '10 books tracing the history of the Church from the apostles to Constantine — the succession of bishops, the martyrs, the heresies refuted, and the providential triumph of Christianity. The founding document of church history.',
    },
  },

  # ─── John Cassian — Conferences ───────────────────────────────────────────────
  {
    'id': 'cassian-conferences',
    'grouped_pages': [
      {'heading': 'Conferences I–X — Discretion, Prayer, and the Spiritual Combat',
       'pages': [
         'Nicene and Post-Nicene Fathers: Series II/Volume XI/John Cassian/Conferences of John Cassian, Part I/Preface',
       ] + [f'Nicene and Post-Nicene Fathers: Series II/Volume XI/John Cassian/Conferences of John Cassian, Part I/Conference {r}'
            for r in ['I','II','III','IV','V','VI','VII','VIII','IX','X']]},
      {'heading': 'Conferences XI–XVII — Knowledge, Perfection, and the Grace Debates',
       'pages': [
         'Nicene and Post-Nicene Fathers: Series II/Volume XI/John Cassian/Conferences of John Cassian, Part II/Preface',
       ] + [f'Nicene and Post-Nicene Fathers: Series II/Volume XI/John Cassian/Conferences of John Cassian, Part II/Conference {r}'
            for r in ['XI','XII','XIII','XIV','XV','XVI','XVII']]},
      {'heading': 'Conferences XVIII–XXIV — Mortification, Friendship, and Spiritual Gifts',
       'pages': [
         'Nicene and Post-Nicene Fathers: Series II/Volume XI/John Cassian/Conferences of John Cassian, Part III/Preface',
       ] + [f'Nicene and Post-Nicene Fathers: Series II/Volume XI/John Cassian/Conferences of John Cassian, Part III/Conference {r}'
            for r in ['XVIII','XIX','XX','XXI','XXII','XXIII','XXIV']]},
    ],
    'index_meta': {
      'abbrev': 'CasC', 'title': 'The Conferences',
      'year': 420, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'John Cassian',
      'desc': '24 recorded conversations with the Egyptian desert fathers on discretion, prayer, the eight deadly thoughts, friendship, and grace — the foundational text of Western monastic spirituality, deeply formative for Benedict of Nursia.',
    },
  },

  # ─── Leo the Great — Sermons ──────────────────────────────────────────────────
  {
    'id': 'leo-sermons',
    'grouped_pages': [
      {'heading': 'Sermons 1–28 — On His Ordination, Fasting, and Christmas',
       'pages': ['Nicene and Post-Nicene Fathers: Series II/Volume XII/Leo the Great/Sermons/Sermon ' + str(n)
                 for n in [1,2,3,9,10,12,16,17,19,21,22,23,24,26,27,28]]},
      {'heading': 'Sermons 31–51 — Lent, Passion, and Easter',
       'pages': ['Nicene and Post-Nicene Fathers: Series II/Volume XII/Leo the Great/Sermons/Sermon ' + str(n)
                 for n in [31,33,34,36,39,40,42,46,49,51]]},
      {'heading': 'Sermons 54–75 — Pentecost, the Apostles, and Almsgiving',
       'pages': ['Nicene and Post-Nicene Fathers: Series II/Volume XII/Leo the Great/Sermons/Sermon ' + str(n)
                 for n in [54,55,58,59,62,63,67,68,71,72,73,74,75]]},
      {'heading': 'Sermons 77–95 — On Watchfulness, the Incarnation, and Epiphany',
       'pages': ['Nicene and Post-Nicene Fathers: Series II/Volume XII/Leo the Great/Sermons/Sermon ' + str(n)
                 for n in [77,78,82,84,85,88,90,91,95]]},
    ],
    'index_meta': {
      'abbrev': 'LeoS', 'title': 'Sermons of Leo the Great',
      'year': 461, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Leo I of Rome',
      'desc': '96 sermons on the Incarnation, the Lord\'s Prayer, Lent, the Passion, and Easter — a treasury of patristic preaching that shaped the Western liturgical year and the theology of Christ\'s two natures.',
    },
  },

  # ─── Gregory the Great — Pastoral Rule ───────────────────────────────────────
  {
    'id': 'gregory-great-pastoral-rule',
    'subpages': [
      {'page': 'Nicene and Post-Nicene Fathers: Series II/Volume XII/Gregory the Great/The Book of Pastoral Rule/Part I',   'heading': 'Part I — Who Ought and Who Ought Not to Undertake Pastoral Rule'},
      {'page': 'Nicene and Post-Nicene Fathers: Series II/Volume XII/Gregory the Great/The Book of Pastoral Rule/Part II',  'heading': 'Part II — The Life of the Shepherd'},
      {'page': 'Nicene and Post-Nicene Fathers: Series II/Volume XII/Gregory the Great/The Book of Pastoral Rule/Part III', 'heading': 'Part III — How the Shepherd Should Teach and Admonish'},
      {'page': 'Nicene and Post-Nicene Fathers: Series II/Volume XII/Gregory the Great/The Book of Pastoral Rule/Part IV',  'heading': 'Part IV — How the Shepherd Must Return to Himself'},
    ],
    'index_meta': {
      'abbrev': 'GregPR', 'title': 'The Book of Pastoral Rule',
      'year': 591, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Gregory the Great',
      'desc': 'Four parts on who should undertake pastoral office, the inner life of the shepherd, how to address the different conditions of hearers, and how to return to oneself after engagement with the world. Alfred the Great called it essential reading.',
    },
  },

  # ─── Boethius ─────────────────────────────────────────────────────────────────
  {
    'id':   'boethius-consolation',
    'gutenberg_id': 14328,
    'split_h': 'h2', 'max_sections': 5,
    'index_meta': {
      'abbrev': 'BoeCo', 'title': 'The Consolation of Philosophy',
      'year': 524, 'type': 'father', 'tradition': 'catholic', 'era': 'medieval',
      'author': 'Boethius',
      'desc': 'Written in prison awaiting execution — Lady Philosophy visits Boethius, argues against Fortune\'s wheel, and leads him through providence, free will, and the highest good to the vision of God as the true source of all happiness. The most read philosophical text of the Middle Ages.',
    },
  },

  # ─── Pascal ───────────────────────────────────────────────────────────────────
  {
    'id':   'pascal-pensees',
    'gutenberg_id': 18269,
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'PasPen', 'title': 'Pensées',
      'year': 1670, 'type': 'apologetics', 'tradition': 'catholic', 'era': 'post-reformation',
      'author': 'Blaise Pascal',
      'desc': 'Posthumous fragments of a never-completed apology — the wager, the reasons of the heart, the two infinites, the misery and greatness of man, and the God of Abraham, Isaac, and Jacob vs. the God of the philosophers. One of the greatest works of Christian thought.',
    },
  },

  # ─── Brother Lawrence ─────────────────────────────────────────────────────────
  {
    'id': 'brother-lawrence-practice',
    'grouped_pages': [
      {'heading': 'Introduction and Preface',
       'pages': [
         'The Practice of the Presence of God/Introduction',
         'The Practice of the Presence of God/Preface',
       ]},
      {'heading': 'The Conversations',
       'pages': [
         'The Practice of the Presence of God/First Conversation',
         'The Practice of the Presence of God/Second Conversation',
         'The Practice of the Presence of God/Third Conversation',
         'The Practice of the Presence of God/Fourth Conversation',
       ]},
      {'heading': 'Letters 1–8',
       'pages': [
         'The Practice of the Presence of God/First Letter',
         'The Practice of the Presence of God/Second Letter',
         'The Practice of the Presence of God/Third Letter',
         'The Practice of the Presence of God/Fourth Letter',
         'The Practice of the Presence of God/Fifth Letter',
         'The Practice of the Presence of God/Sixth Letter',
         'The Practice of the Presence of God/Seventh Letter',
         'The Practice of the Presence of God/Eighth Letter',
       ]},
      {'heading': 'Letters 9–15',
       'pages': [
         'The Practice of the Presence of God/Ninth Letter',
         'The Practice of the Presence of God/Tenth Letter',
         'The Practice of the Presence of God/Eleventh Letter',
         'The Practice of the Presence of God/Twelfth Letter',
         'The Practice of the Presence of God/Thirteenth Letter',
         'The Practice of the Presence of God/Fourteenth Letter',
         'The Practice of the Presence of God/Fifteenth Letter',
       ]},
    ],
    'index_meta': {
      'abbrev': 'BrLaw', 'title': 'The Practice of the Presence of God',
      'year': 1692, 'type': 'father', 'tradition': 'catholic', 'era': 'post-reformation',
      'author': 'Brother Lawrence',
      'desc': 'Letters and conversations of a humble lay brother in a Paris monastery on cultivating unbroken awareness of God\'s presence in the midst of kitchen work and daily life. One of the most beloved short spiritual classics.',
    },
  },

  # ─── Bunyan — The Holy War ────────────────────────────────────────────────────
  {
    'id':   'bunyan-holy-war',
    'gutenberg_id': 395,
    'split_h': 'h2', 'max_sections': 6,
    'index_meta': {
      'abbrev': 'BunHW', 'title': 'The Holy War',
      'year': 1682, 'type': 'father', 'tradition': 'baptist', 'era': 'post-reformation',
      'author': 'John Bunyan',
      'desc': 'The allegory of Mansoul — its creation, fall to Diabolus, siege and redemption by Emmanuel, and the ongoing war for its streets and gates. Bunyan\'s second great allegory, often considered his most theological.',
    },
  },

  # ─── Bunyan — Grace Abounding (Gutenberg #654) ────────────────────────────────
  {
    'id':   'bunyan-grace-abounding',
    'gutenberg_id': 654,
    'split_h': 'h2', 'max_sections': 4,
    'index_meta': {
      'abbrev': 'BunGA', 'title': 'Grace Abounding to the Chief of Sinners',
      'year': 1666, 'type': 'father', 'tradition': 'baptist', 'era': 'post-reformation',
      'author': 'John Bunyan',
      'desc': 'Bunyan\'s spiritual autobiography — years of spiritual torment, Satanic temptations, wrestling with Scripture, and the final assurance of grace "abounding" to the chief of sinners. The direct source from which Pilgrim\'s Progress grew.',
    },
  },

  # ─── Calvin — Institutes Book 1 (Wikisource chapters) ───────────────────────
  {
    'id': 'calvin-institutes-book1',
    'grouped_pages': [
      {'heading': 'Book I — Chs. 1–6: Knowledge of God; Scripture',
       'pages': [f'Institutes of the Christian Religion (1845)/Book 1/Chapter {i}' for i in range(1, 7)]},
      {'heading': 'Book I — Chs. 7–13: Scripture; Trinity; Creation',
       'pages': [f'Institutes of the Christian Religion (1845)/Book 1/Chapter {i}' for i in range(7, 14)]},
      {'heading': 'Book I — Chs. 14–18: Angels, Providence, and Human Wisdom',
       'pages': [f'Institutes of the Christian Religion (1845)/Book 1/Chapter {i}' for i in range(14, 19)]},
    ],
    'index_meta': {
      'abbrev': 'InstI', 'title': 'Institutes — Book I: Knowledge of God the Creator',
      'year': 1559, 'type': 'father', 'tradition': 'reformed', 'era': 'reformation',
      'author': 'John Calvin',
      'desc': 'Book I of Calvin\'s Institutes — the knowledge of God and of ourselves, Scripture as the spectacles of faith, the Trinity, creation, providence, and angels. The opening of the most comprehensive work of Reformed theology.',
    },
  },

  # ─── Calvin — Institutes Vols 1–2 (Gutenberg #45001 + #64392) ───────────────
  {
    'id':   'calvin-institutes-vol1',
    'gutenberg_id': 45001,
    'split_h': 'h2', 'max_sections': 8,
    'index_meta': {
      'abbrev': 'InstV1', 'title': 'Institutes of the Christian Religion — Vol. I (Books I–II)',
      'year': 1559, 'type': 'father', 'tradition': 'reformed', 'era': 'reformation',
      'author': 'John Calvin',
      'desc': 'Books I–II of the Institutes — the knowledge of God the Creator and Redeemer. The Trinity, Scripture, the fall, the law, the Mosaic economy, and the two natures of Christ.',
    },
  },
  {
    'id':   'calvin-institutes-vol2',
    'gutenberg_id': 64392,
    'split_h': 'h2', 'max_sections': 8,
    'index_meta': {
      'abbrev': 'InstV2', 'title': 'Institutes of the Christian Religion — Vol. II (Books III–IV)',
      'year': 1559, 'type': 'father', 'tradition': 'reformed', 'era': 'reformation',
      'author': 'John Calvin',
      'desc': 'Books III–IV of the Institutes — the way we receive Christ\'s grace (faith, justification, sanctification, election) and the external means by which God invites us into the society of Christ (the Church, ministry, sacraments, civil government).',
    },
  },

  # ─── Fox's Book of Martyrs (Gutenberg #22400) ────────────────────────────────
  {
    'id':   'fox-book-of-martyrs',
    'gutenberg_id': 22400,
    'split_h': 'h2', 'max_sections': 8,
    'index_meta': {
      'abbrev': 'FoxBM', 'title': "Fox's Book of Martyrs",
      'year': 1563, 'type': 'father', 'tradition': 'reformed', 'era': 'reformation',
      'author': 'John Foxe',
      'desc': 'The great Protestant martyrology — from the early church through the Marian persecution in England, recording the sufferings of those who died for the Protestant faith. Hugely formative for Anglophone Protestant identity.',
    },
  },

  # ─── Andrew Murray — Ministry of Intercession (Gutenberg #29296) ─────────────
  {
    'id':   'murray-ministry-of-intercession',
    'gutenberg_id': 29296,
    'split_h': 'h2', 'max_sections': 4,
    'index_meta': {
      'abbrev': 'MurMI', 'title': 'The Ministry of Intercession',
      'year': 1897, 'type': 'father', 'tradition': 'reformed', 'era': 'modern',
      'author': 'Andrew Murray',
      'desc': 'Murray\'s call to the church to recover the ministry of intercession — why the Church fails to pray, how to pray with power, and how every believer can become a channel of God\'s grace to the world through persistent intercession.',
    },
  },

  # ─── Andrew Murray — Lord, Teach Us to Pray (Gutenberg #26709) ───────────────
  {
    'id':   'murray-lord-teach-us-to-pray',
    'gutenberg_id': 26709,
    'split_h': 'h2', 'max_sections': 4,
    'index_meta': {
      'abbrev': 'MurLP', 'title': 'Lord, Teach Us to Pray',
      'year': 1895, 'type': 'father', 'tradition': 'reformed', 'era': 'modern',
      'author': 'Andrew Murray',
      'desc': 'Thirty-one meditations on the Lord\'s Prayer and the life of prayer — working through each petition to show how the Lord\'s Prayer is both a model of prayer and a school of the entire Christian life.',
    },
  },

  # ─── Newman — Apologia Pro Vita Sua (Gutenberg #22088) ───────────────────────
  {
    'id':   'newman-apologia',
    'gutenberg_id': 22088,
    'split_h': 'h2', 'max_sections': 6,
    'index_meta': {
      'abbrev': 'NewA', 'title': 'Apologia Pro Vita Sua',
      'year': 1865, 'type': 'father', 'tradition': 'catholic', 'era': 'modern',
      'author': 'John Henry Newman',
      'desc': 'Newman\'s intellectual autobiography — the Oxford Movement, Tract 90, the Via Media, his gradual loss of confidence in Anglicanism, doctrinal development, and his reception into the Roman Catholic Church. The most compelling conversion narrative in English literature.',
    },
  },

  # ─── John of Damascus — Exposition of the Orthodox Faith ─────────────────────
  {
    'id': 'john-of-damascus-exposition',
    'grouped_pages': [
      {'heading': 'Books I–II — God, Trinity, Creation, and Angels',
       'pages': [
         'Nicene and Post-Nicene Fathers: Series II/Volume IX/John of Damascus/Exposition of the Orthodox Faith/Book I',
         'Nicene and Post-Nicene Fathers: Series II/Volume IX/John of Damascus/Exposition of the Orthodox Faith/Book II',
       ]},
      {'heading': 'Book III — The Incarnation',
       'pages': [
         'Nicene and Post-Nicene Fathers: Series II/Volume IX/John of Damascus/Exposition of the Orthodox Faith/Book III',
       ]},
      {'heading': 'Book IV — The Two Natures, Sacraments, and the Defense of Icons',
       'pages': [
         'Nicene and Post-Nicene Fathers: Series II/Volume IX/John of Damascus/Exposition of the Orthodox Faith/Book IV',
       ]},
    ],
    'index_meta': {
      'abbrev': 'JoDam', 'title': 'An Exact Exposition of the Orthodox Faith',
      'year': 743, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'John of Damascus',
      'desc': 'The first systematic theology of Eastern Christianity — God and the Trinity, creation and human nature, the Incarnation, the two wills of Christ, the sacraments, and the defense of icons against the iconoclasts.',
    },
  },

  # ─── Bonaventure — Itinerarium Mentis in Deum ────────────────────────────────
  {
    'id':   'bonaventure-itinerarium',
    'page': 'The Soul\'s Journey into God',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'Itin', 'title': 'The Soul\'s Journey into God',
      'year': 1259, 'type': 'father', 'tradition': 'catholic', 'era': 'medieval',
      'author': 'Bonaventure',
      'desc': 'Written on La Verna after Francis received the stigmata — six stages of contemplation ascending through creation, the soul, and being itself to the mystical darkness of union with the crucified Christ.',
    },
  },

  # ─── Teresa of Ávila — The Interior Castle (Gutenberg #243) ──────────────────
  {
    'id':   'teresa-interior-castle',
    'gutenberg_id': 243,
    'split_h': 'h2', 'max_sections': 7,
    'index_meta': {
      'abbrev': 'IC', 'title': 'The Interior Castle',
      'year': 1588, 'type': 'father', 'tradition': 'catholic', 'era': 'reformation',
      'author': 'Teresa of Ávila',
      'desc': 'Teresa\'s seven-mansioned castle of the soul — from self-knowledge and vocal prayer through the prayer of quiet and union to the spiritual marriage and Trinitarian indwelling.',
    },
  },

  # ─── John of the Cross — Dark Night of the Soul (Gutenberg #700) ─────────────
  {
    'id':   'john-of-cross-dark-night',
    'gutenberg_id': 700,
    'split_h': 'h2', 'max_sections': 4,
    'index_meta': {
      'abbrev': 'DN', 'title': 'Dark Night of the Soul',
      'year': 1579, 'type': 'father', 'tradition': 'catholic', 'era': 'reformation',
      'author': 'John of the Cross',
      'desc': 'The poem and its commentary — active and passive purgations of sense and spirit, the nada way, and the transformation of the soul into God through the dark night of loving union.',
    },
  },

  # ─── Abraham Kuyper — Lectures on Calvinism (Gutenberg #58670) ───────────────
  {
    'id':   'kuyper-calvinism',
    'gutenberg_id': 58670,
    'split_h': 'h2', 'max_sections': 6,
    'index_meta': {
      'abbrev': 'KuypC', 'title': 'Lectures on Calvinism',
      'year': 1898, 'type': 'father', 'tradition': 'reformed', 'era': 'modern',
      'author': 'Abraham Kuyper',
      'desc': 'Calvinism as a comprehensive life-system, the doctrine of sphere sovereignty, and the Reformed vision for science, art, and the state — the Stone Lectures at Princeton.',
    },
  },

  # ─── Thomas Watson — A Body of Divinity (Gutenberg #26691) ───────────────────
  # Long work (~300 pages): split into 2 parts by thematic halves
  {
    'id':   'watson-body-of-divinity-vol1',
    'gutenberg_id': 26691,
    'split_h': 'h2', 'max_sections': 12,
    'index_meta': {
      'abbrev': 'WatBD1', 'title': 'A Body of Divinity — Vol. I',
      'year': 1692, 'type': 'father', 'tradition': 'reformed', 'era': 'post-reformation',
      'author': 'Thomas Watson',
      'desc': 'Watson\'s warm and clear exposition of the Westminster Shorter Catechism — the first half covering God\'s nature and attributes, creation, the covenant of grace, sin, and the person of Christ.',
    },
  },

  # ─── John Owen — Of the Mortification of Sin in Believers (Gutenberg #36809) ─
  {
    'id':   'owen-mortification',
    'gutenberg_id': 36809,
    'split_h': 'h2', 'max_sections': 4,
    'index_meta': {
      'abbrev': 'Owen', 'title': 'Of the Mortification of Sin in Believers',
      'year': 1656, 'type': 'father', 'tradition': 'reformed', 'era': 'post-reformation',
      'author': 'John Owen',
      'desc': 'Owen\'s Puritan masterpiece on killing sin — the Spirit as the sole agent of mortification, the danger of unmortified sin, and union with Christ as the root of all true holiness.',
    },
  },

  # ─── David Brainerd — Life and Journal (Gutenberg #65066) ───────────────────────
  {
    'id':   'brainerd-journal',
    'gutenberg_id': 65066,
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'BrainJ', 'title': 'The Life of David Brainerd',
      'year': 1749, 'type': 'devotional', 'tradition': 'reformed', 'era': 'modern',
      'author': 'David Brainerd',
      'desc': 'Jonathan Edwards\' edition of Brainerd\'s diary and missionary journal — spiritual anguish and deep prayer, pioneer work among Native Americans, and a life of total consecration that shaped Hudson Taylor, Jim Elliot, and a generation of missionaries.',
    },
  },

  # ─── William Carey — An Enquiry (Gutenberg #11449) ────────────────────────────
  {
    'id':   'carey-enquiry',
    'gutenberg_id': 11449,
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'CareyE', 'title': 'An Enquiry into the Obligations of Christians',
      'year': 1792, 'type': 'father', 'tradition': 'reformed', 'era': 'modern',
      'author': 'William Carey',
      'desc': 'The founding document of the modern Protestant missions movement — Carey argues from the Great Commission that the obligation to evangelize the nations is permanent and binding, surveys the current state of the world, and calls for a missionary society.',
    },
  },

  # ─── Bernard of Clairvaux — On Loving God (CCEL) ─────────────────────────────
  {
    'id': 'bernard-on-loving-god',
    'ccel_grouped': [
      {'heading': 'On Loving God — Complete Text',
       'base_url': 'https://ccel.org/ccel/bernard/loving_god/',
       'pages': [f'loving_god.{r}.html' for r in [
         'i','ii','iii','iv','v','vi','vii','viii','ix','x',
         'xi','xii','xiii','xiv','xv','xvi','xvii','xviii',
       ]]},
    ],
    'index_meta': {
      'abbrev': 'BernLG', 'title': 'On Loving God',
      'year': 1135, 'type': 'father', 'tradition': 'catholic', 'era': 'medieval',
      'author': 'Bernard of Clairvaux',
      'desc': 'Bernard\'s meditation on the nature and degrees of love — why God is to be loved without limit and the four ascending degrees from self-love to loving even oneself only for God\'s sake.',
    },
  },

  # ─── Francis de Sales — Introduction to the Devout Life (CCEL) ───────────────
  {
    'id': 'francis-de-sales-devout-life',
    'ccel_grouped': [
      {'heading': 'Preface and Part I — Counsels and Practices for Entering Devotion',
       'base_url': 'https://ccel.org/ccel/desales/devout_life/',
       'pages': ['devout_life.i.html', 'devout_life.i.i.html', 'devout_life.iii.html'] +
                [f'devout_life.iii.{r}.html' for r in [
                  'i','ii','iii','iv','v','vi','vii','viii','ix','x',
                  'xi','xii','xiii','xiv','xv','xvi','xvii','xviii','xix','xx',
                  'xxi','xxii','xxiii','xxiv',
                ]]},
      {'heading': 'Part II — Prayer and the Sacraments',
       'base_url': 'https://ccel.org/ccel/desales/devout_life/',
       'pages': ['devout_life.iv.html'] +
                [f'devout_life.iv.{r}.html' for r in [
                  'i','ii','iii','iv','v','vi','vii','viii','ix','x',
                  'xi','xii','xiii','xiv','xv','xvi','xvii','xviii','xix','xx','xxi',
                ]]},
      {'heading': 'Part III — The Practice of Virtue',
       'base_url': 'https://ccel.org/ccel/desales/devout_life/',
       'pages': ['devout_life.v.html'] +
                [f'devout_life.v.{r}.html' for r in [
                  'i','ii','iii','iv','v','vi','vii','viii','ix','x',
                  'xi','xii','xiii','xiv','xv','xvi','xvii','xviii','xix','xx',
                  'xxi','xxii','xxiii','xxiv','xxv','xxvi','xxvii','xxviii','xxix','xxx',
                  'xxxi','xxxii','xxxiii','xxxiv','xxxv','xxxvi','xxxvii','xxxviii','xxxix','xl','xli',
                ]]},
      {'heading': 'Parts IV–V — Temptations, Renewal, and Conclusion',
       'base_url': 'https://ccel.org/ccel/desales/devout_life/',
       'pages': ['devout_life.vi.html'] +
                [f'devout_life.vi.{r}.html' for r in [
                  'i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii','xiv','xv',
                ]] +
                ['devout_life.vii.html'] +
                [f'devout_life.vii.{r}.html' for r in [
                  'i','ii','iii','iv','v','vi','vii','viii','ix','x',
                  'xi','xii','xiii','xiv','xv','xvi','xvii','xviii',
                ]] +
                ['devout_life.viii.html']},
    ],
    'index_meta': {
      'abbrev': 'IDL', 'title': 'Introduction to the Devout Life',
      'year': 1609, 'type': 'father', 'tradition': 'catholic', 'era': 'post-reformation',
      'author': 'Francis de Sales',
      'desc': 'The gentle bishop\'s guide to sanctity in ordinary life — five parts on devotion, prayer, the sacraments, the practice of virtue, temptations, and annual renewal. Written for the married, the widowed, and the active, not only for monastics.',
    },
  },

  # ─── Jonathan Edwards — Religious Affections (CCEL) ──────────────────────────
  {
    'id': 'edwards-religious-affections',
    'ccel_grouped': [
      {'heading': 'Introduction and Part I — The Nature of Religious Affections',
       'base_url': 'https://ccel.org/ccel/edwards/affections/',
       'pages': ['affections.i.html', 'affections.ii.html', 'affections.iii.html']},
      {'heading': 'Part II — No Certain Signs Either Way',
       'base_url': 'https://ccel.org/ccel/edwards/affections/',
       'pages': ['affections.iv.html'] +
                [f'affections.iv.{r}.html' for r in [
                  'i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii',
                ]]},
      {'heading': 'Part III — The Twelve Distinguishing Signs of Gracious Affections',
       'base_url': 'https://ccel.org/ccel/edwards/affections/',
       'pages': ['affections.v.html', 'affections.vi.html'] +
                [f'affections.vi.{r}.html' for r in [
                  'i','ii','iii','iv','v','vi','vii','viii','ix','x','xi',
                ]] +
                ['affections.vii.html', 'affections.viii.html', 'affections.viii.i.html']},
    ],
    'index_meta': {
      'abbrev': 'RA', 'title': 'Religious Affections',
      'year': 1746, 'type': 'father', 'tradition': 'reformed', 'era': 'post-reformation',
      'author': 'Jonathan Edwards',
      'desc': 'Edwards\'s masterwork on the nature of genuine religion — Part I on the nature and importance of the affections, Part II on twelve unreliable signs, and Part III on the twelve reliable marks of truly gracious and holy affections.',
    },
  },

  # ─── Jonathan Edwards — Freedom of the Will (CCEL) ───────────────────────────
  {
    'id': 'edwards-freedom-of-will',
    'ccel_grouped': [
      {'heading': 'Part I — Terms, Nature of the Will, and Necessity',
       'base_url': 'https://ccel.org/ccel/edwards/will/',
       'pages': ['will.i.html', 'will.ii.html'] +
                [f'will.ii.{r}.html' for r in ['i','ii','iii','iv','v']]},
      {'heading': 'Part II — Against Arminian Freedom of the Will',
       'base_url': 'https://ccel.org/ccel/edwards/will/',
       'pages': ['will.iii.html'] +
                [f'will.iii.{r}.html' for r in [
                  'i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii',
                ]]},
      {'heading': 'Part III — The Calvinistic Doctrine Defended',
       'base_url': 'https://ccel.org/ccel/edwards/will/',
       'pages': ['will.iv.html'] +
                [f'will.iv.{r}.html' for r in ['i','ii','iii','iv','v','vi','vii']]},
      {'heading': 'Parts IV–V — Objections Answered and Conclusion',
       'base_url': 'https://ccel.org/ccel/edwards/will/',
       'pages': ['will.v.html'] +
                [f'will.v.{r}.html' for r in ['i','ii','iii','iv','v','vi','vii']] +
                ['will.vi.html', 'will.vi.i.html', 'will.vi.ii.html']},
    ],
    'index_meta': {
      'abbrev': 'FW', 'title': 'Freedom of the Will',
      'year': 1754, 'type': 'father', 'tradition': 'reformed', 'era': 'post-reformation',
      'author': 'Jonathan Edwards',
      'desc': 'The most rigorous philosophical defence of Calvinist determinism in the English language — Edwards argues that moral necessity is compatible with genuine freedom, that Arminian self-determination is incoherent, and that God\'s sovereignty over the will is essential to all true virtue.',
    },
  },

  # ─── Origen — De Principiis (On First Principles), ANF Vol. IV ───────────────
  {
    'id': 'origen-de-principiis',
    'grouped_pages': [
      {'heading': 'Preface and Book I — God, the Son, the Holy Spirit',
       'pages': [_DP_BASE + 'Preface'] +
                [_DP_BASE + f'I/Chapter {i}' for i in range(1, 11)]},
      {'heading': 'Book II — The World, Incarnate Soul, and the Resurrection',
       'pages': [_DP_BASE + f'II/Chapter {i}' for i in range(1, 12)]},
      {'heading': 'Book III — Free Will, Evil, and the Progress of Souls',
       'pages': [_DP_BASE + f'III/Chapter {i}' for i in range(1, 9)]},
      {'heading': 'Book IV — Scripture and the Mystical Theology of the Word',
       'pages': [_DP_BASE + 'IV/Chapter 1', _DP_BASE + 'IV/Chapter 2',
                 _DP_BASE + 'IV/Chapter 3', _DP_BASE + 'Elucidations']},
    ],
    'index_meta': {
      'abbrev': 'DP', 'title': 'On First Principles (De Principiis)',
      'year': 225, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Origen',
      'desc': 'The first systematic Christian theology — four books on God and the Trinity, the soul and the world, free will and redemption, and the spiritual interpretation of Scripture. Controversial in its speculative daring; foundational for all later Christian thought.',
    },
  },

  # ─── Chrysostom — Homilies on the Acts of the Apostles, NPNF I/XI ─────────────
  {
    'id': 'chrysostom-homilies-acts',
    'grouped_pages': [
      {'heading': 'Homilies I–XI — Ascension, Pentecost, and the Early Jerusalem Church (Acts 1–4)',
       'pages': [_ACTS_BASE + h for h in [
         'Homily I on Acts i. 1, 2', 'Homily II on Acts i. 6', 'Homily III on Acts i. 12',
         'Homily IV on Acts ii. 1, 2', 'Homily V on Acts ii. 14', 'Homily VI on Acts ii. 22',
         'Homily VII on Acts ii. 37', 'Homily VIII on Acts iii. 1', 'Homily IX on Acts iii. 12',
         'Homily X on Acts iv. 1', 'Homily XI on Acts iv. 23',
       ]]},
      {'heading': 'Homilies XII–XXII — Stephen, Philip, and Paul\'s Conversion (Acts 4–9)',
       'pages': [_ACTS_BASE + h for h in [
         'Homily XII on Acts iv. 36, 37', 'Homily XIII on Acts v. 17, 18',
         'Homily XIV on Acts v. 34', 'Homily XV on Acts vi. 8', 'Homily XVI on Acts vii. 6, 7',
         'Homily XVII on Acts vii. 35', 'Homily XVIII on Acts vii. 54',
         'Homily XIX on Acts viii. 26, 27', 'Homily XX on Acts ix. 10, 12',
         'Homily XXI on Acts ix. 26, 27', 'Homily XXII on Acts x. 1-4',
       ]]},
      {'heading': 'Homilies XXIII–XXXIII — Peter\'s Gentile Mission and the First Journey (Acts 10–15)',
       'pages': [_ACTS_BASE + h for h in [
         'Homily XXIII on Acts x. 23, 24', 'Homily XXIV on Acts x. 44, 46',
         'Homily XXV on Acts xi. 19', 'Homily XXVI on Acts xii. 1, 2',
         'Homily XXVII on Acts xii. 18, 19', 'Homily XXVIII on Acts xiii. 4, 5',
         'Homily XXIX on Acts xiii. 16, 17', 'Homily XXX on Acts xiii. 42',
         'Homily XXXI on Acts xiv. 14, 15', 'Homily XXXII on Acts xv. 1',
         'Homily XXXIII on Acts xv. 13, 15',
       ]]},
      {'heading': 'Homilies XXXIV–XLIII — The Second and Third Missionary Journeys (Acts 15–19)',
       'pages': [_ACTS_BASE + h for h in [
         'Homily XXXIV on Acts xv. 35', 'Homily XXXV on Acts xvi. 13, 14',
         'Homily XXXVI on Acts xvi. 25, 26', 'Homily XXXVII on Acts xvii. 1, 2, 3',
         'Homily XXXVIII on Acts xvii. 16, 17',
         'Homily XXXIX on Acts xvii. 32-34. xviii. 1',
         'Homily XL on Acts xviii. 18', 'Homily XLI on Acts xix. 8, 9',
         'Homily XLII on Acts xix. 21, 23', 'Homily XLIII on Acts xx. 1',
       ]]},
      {'heading': 'Homilies XLIV–LV — Paul\'s Farewell and Journey to Rome (Acts 20–28)',
       'pages': [_ACTS_BASE + h for h in [
         'Homily XLIV on Acts xx. 17-21', 'Homily XLV on Acts xx. 32',
         'Homily XLVI on Acts xxi. 18, 19', 'Homily XLVII on Acts xxi. 39, 40',
         'Homily XLVIII on Acts xxii. 17-20', 'Homily XLIX on Acts xxiii. 6-8',
         'Homily L on Acts xxiii. 31-33', 'Homily LI on Acts xxiv. 22, 23',
         'Homily LII on Acts xxv. 23', 'Homily LIII on Acts xxvi. 30-32',
         'Homily LIV on Acts xxviii. 1', 'Homily LV on Acts xxviii. 17-20',
       ]]},
    ],
    'index_meta': {
      'abbrev': 'ChrysActs', 'title': 'Homilies on the Acts of the Apostles',
      'year': 400, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'John Chrysostom',
      'desc': '55 homilies on the Acts of the Apostles — the greatest ancient commentary on the missionary expansion of the Church, rich in practical exhortation on prayer, almsgiving, unity, and bold witness to the resurrection.',
    },
  },

  # ─── Aquinas — Summa Theologica (all 4 Parts, Gutenberg Dominican Province tr.) ─
  # Gutenberg HTML uses <h5> for both TREATISE and QUESTION headings; split there
  # so each Question becomes one navigable section in the paginated reader.
  {
    'id':   'aquinas-summa-part-i',
    'gutenberg_id': 17611,
    'split_h': 'h5', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'STh-I', 'title': 'Summa Theologica — Part I (Prima Pars)',
      'year': 1274, 'type': 'father', 'tradition': 'catholic', 'era': 'medieval',
      'author': 'Thomas Aquinas',
      'desc': 'Questions 1–119 — Sacred doctrine, the existence and nature of God, the Trinity, creation, angels, human nature, and divine governance. The most systematic treatment of natural theology and Trinitarian doctrine in the Western tradition.',
    },
  },
  {
    'id':   'aquinas-summa-part-i-ii',
    'gutenberg_id': 17897,
    'split_h': 'h5', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'STh-I-II', 'title': 'Summa Theologica — Part I–II (Prima Secundae)',
      'year': 1274, 'type': 'father', 'tradition': 'catholic', 'era': 'medieval',
      'author': 'Thomas Aquinas',
      'desc': 'Questions 1–114 — The last end of man, human acts, the passions, habits and virtue, law (eternal, natural, human, divine), and the grace of God. The most thorough medieval treatment of moral theology.',
    },
  },
  {
    'id':   'aquinas-summa-part-ii-ii',
    'gutenberg_id': 18755,
    'split_h': 'h5', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'STh-II-II', 'title': 'Summa Theologica — Part II–II (Secunda Secundae)',
      'year': 1274, 'type': 'father', 'tradition': 'catholic', 'era': 'medieval',
      'author': 'Thomas Aquinas',
      'desc': 'Questions 1–189 — The three theological virtues (faith, hope, charity) and the four cardinal virtues (prudence, justice, fortitude, temperance), with each virtue examined in detail alongside its opposing vices.',
    },
  },
  {
    'id':   'aquinas-summa-part-iii',
    'gutenberg_id': 19950,
    'split_h': 'h5', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'STh-III', 'title': 'Summa Theologica — Part III (Tertia Pars)',
      'year': 1274, 'type': 'father', 'tradition': 'catholic', 'era': 'medieval',
      'author': 'Thomas Aquinas',
      'desc': 'Questions 1–90 plus the Supplement — The Incarnation, the life of Christ, the sacraments (Baptism, Confirmation, Eucharist, Penance, Extreme Unction, Orders, Matrimony), and the last things. Left incomplete at Aquinas\'s death; Supplement drawn from his Commentary on the Sentences.',
    },
  },

  # ─── Chesterton — The Everlasting Man (Gutenberg #65688) ─────────────────────
  {
    'id':   'chesterton-everlasting-man',
    'gutenberg_id': 65688,
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'EM', 'title': 'The Everlasting Man',
      'year': 1925, 'type': 'father', 'tradition': 'catholic', 'era': 'modern',
      'author': 'G.K. Chesterton',
      'desc': 'Man as qualitatively different from animals, pagan myth as groping anticipation of Christ, and the Incarnation as the hinge of all history — the book that put C.S. Lewis on the road to conversion.',
    },
  },

  # ─── Chesterton — Heretics (Wikisource, 20 chapters) ────────────────────────
  {
    'id': 'chesterton-heretics',
    'subpages': [
      {'page': 'Heretics/1',  'heading': 'Chapter 1 — Introductory Remarks on the Importance of Orthodoxy'},
      {'page': 'Heretics/2',  'heading': 'Chapter 2 — On the Negative Spirit'},
      {'page': 'Heretics/3',  'heading': 'Chapter 3 — On Mr. Rudyard Kipling and Making the World Small'},
      {'page': 'Heretics/4',  'heading': 'Chapter 4 — Mr. Bernard Shaw'},
      {'page': 'Heretics/5',  'heading': 'Chapter 5 — Mr. H. G. Wells and the Giants'},
      {'page': 'Heretics/6',  'heading': 'Chapter 6 — Christmas and the Aesthetes'},
      {'page': 'Heretics/7',  'heading': 'Chapter 7 — Omar and the Sacred Vine'},
      {'page': 'Heretics/8',  'heading': 'Chapter 8 — The Mildness of the Yellow Press'},
      {'page': 'Heretics/9',  'heading': 'Chapter 9 — The Moods of Mr. George Moore'},
      {'page': 'Heretics/10', 'heading': 'Chapter 10 — On Sandals and Simplicity'},
      {'page': 'Heretics/11', 'heading': 'Chapter 11 — Science and the Savages'},
      {'page': 'Heretics/12', 'heading': 'Chapter 12 — Paganism and Mr. Lowes Dickinson'},
      {'page': 'Heretics/13', 'heading': 'Chapter 13 — Celts and Celtophiles'},
      {'page': 'Heretics/14', 'heading': 'Chapter 14 — On Certain Modern Writers and the Institution of the Family'},
      {'page': 'Heretics/15', 'heading': 'Chapter 15 — On Smart Novelists and the Smart Set'},
      {'page': 'Heretics/16', 'heading': 'Chapter 16 — On Mr. McCabe and a Divine Frivolity'},
      {'page': 'Heretics/17', 'heading': 'Chapter 17 — On the Wit of Whistler'},
      {'page': 'Heretics/18', 'heading': 'Chapter 18 — The Fallacy of the Young Nation'},
      {'page': 'Heretics/19', 'heading': 'Chapter 19 — Slum Novelists and the Slums'},
      {'page': 'Heretics/20', 'heading': 'Chapter 20 — Concluding Remarks on the Importance of Orthodoxy'},
    ],
    'index_meta': {
      'abbrev': 'Herit', 'title': 'Heretics',
      'year': 1905, 'type': 'apologetics', 'tradition': 'catholic', 'era': 'modern',
      'author': 'G.K. Chesterton',
      'desc': 'Chesterton\'s polemical precursor to Orthodoxy — twenty witty essays exposing the hidden heresies of leading modern thinkers (Shaw, Wells, Kipling, Whistler) and arguing that every practical man has a philosophy, whether he admits it or not.',
      'series': 'chesterton',
      'series_title': 'Works of G.K. Chesterton',
      'volume': 3, 'volume_label': 'Heretics',
    },
  },

  # ─── Apology of Aristides (Wikisource, ANF Vol IX — Syriac translation) ─────
  {
    'id': 'aristides-apology',
    'page': 'Ante-Nicene Fathers/Volume IX/Apology of Aristides/Translated from the Syriac',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'ArAp', 'title': 'Apology of Aristides',
      'year': 140, 'type': 'apologetics', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Aristides of Athens',
      'desc': 'One of the earliest surviving Christian apologies — addressed to Emperor Hadrian, arguing from creation and moral order that the Christians alone worship the true God, superior to Greek, Chaldean, Egyptian, and Jewish religion.',
    },
  },

  # ─── Octavius by Minucius Felix (Wikisource ANF Vol IV, 41 chapters) ──────────
  {
    'id': 'minucius-felix-octavius',
    'grouped_pages': [
      {'heading': 'The Octavius — Chapters 1–20',
       'pages': [f'Ante-Nicene Fathers/Volume IV/Minucius Felix/The Octavius of Minucius Felix/Chapter {i}'
                 for i in range(1, 21)]},
      {'heading': 'The Octavius — Chapters 21–41',
       'pages': [f'Ante-Nicene Fathers/Volume IV/Minucius Felix/The Octavius of Minucius Felix/Chapter {i}'
                 for i in range(21, 42)]},
    ],
    'index_meta': {
      'abbrev': 'Oct', 'title': 'The Octavius',
      'year': 200, 'type': 'apologetics', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Minucius Felix',
      'desc': 'The most rhetorically polished early Latin apology — a Ciceronian dialogue between the pagan Caecilius and the Christian Octavius, defending monotheism, Christian morality, and the resurrection against pagan charges of atheism and immorality.',
    },
  },

  # ─── Butler — The Analogy of Religion (Gutenberg) ────────────────────────────
  {
    'id': 'butler-analogy',
    'gutenberg_id': 3237,
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'ButAn', 'title': 'The Analogy of Religion',
      'year': 1736, 'type': 'apologetics', 'tradition': 'anglican', 'era': 'modern',
      'author': 'Joseph Butler',
      'desc': 'The most influential 18th-century apologetic — Butler argues by analogy that the same objections raised against revealed religion apply equally to natural religion, making the honest doubter\'s position incoherent. Enormously influential on Newman and 19th-century Anglican thought.',
    },
  },

  # ─── Paley — Natural Theology (Gutenberg) ────────────────────────────────────
  {
    'id': 'paley-natural-theology',
    'gutenberg_id': 35201,
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'PalNT', 'title': 'Natural Theology',
      'year': 1802, 'type': 'apologetics', 'tradition': 'anglican', 'era': 'modern',
      'author': 'William Paley',
      'desc': 'The classical design argument — the watchmaker analogy argues that the complexity of living organisms requires an intelligent designer, just as a watch found on a heath requires a watchmaker. Essential for understanding the apologetic tradition and Darwin\'s specific intellectual target.',
    },
  },

  # ─── Roman Catechism (Catechism of the Council of Trent) — Wikisource ────────
  {
    'id': 'roman-catechism',
    'grouped_pages': [
      {'heading': 'Preface and Part I — The Apostles\' Creed (Articles 1–12)',
       'pages': [_TRENT_BASE + 'Preface to the Catechism'] +
                [_TRENT_BASE + f'Part 1: Article {i}' for i in range(1, 13)]},
      {'heading': 'Part II — The Seven Sacraments',
       'pages': [_TRENT_BASE + p for p in [
         'Part 2', 'Part 2: Baptism', 'Part 2: Confirmation', 'Part 2: The Holy Eucharist',
         'Part 2: Penance', 'Part 2: Extreme Unction', 'Part 2: Holy Orders', 'Part 2: Holy Matrimony',
       ]]},
      {'heading': 'Part III — The Ten Commandments',
       'pages': [_TRENT_BASE + p for p in [
         'Part 3', 'Part 3: The First Commandment', 'Part 3: The Second Commandment',
         'Part 3: The Third Commandment', 'Part 3: The Fourth Commandment',
         'Part 3: The Fifth Commandment', 'Part 3: The Sixth Commandment',
         'Part 3: The Seventh Commandment', 'Part 3: The Eighth Commandment',
         'Part 3: The Ninth and Tenth Commandment',
       ]]},
      {'heading': 'Part IV — The Lord\'s Prayer',
       'pages': [_TRENT_BASE + p for p in [
         'Part 4', 'Part 4: Our Father who art in heaven', 'Part 4: Hallowed be Thy Name',
         'Part 4: Thy Kingdom Come', 'Part 4: Thy will be done on earth as it is in heaven',
         'Part 4: Give us this day our daily bread',
         'Part 4: Forgive our trespasses as we forgive those who trespass against us',
         'Part 4: And lead us not into temption', 'Part 4: But deliver us from evil',
         'Part 4: Amen', 'Praxis Catechismi',
       ]]},
    ],
    'index_meta': {
      'abbrev': 'RomCat', 'title': 'Roman Catechism',
      'year': 1566, 'type': 'catechism', 'tradition': 'catholic', 'era': 'post-reformation',
      'desc': 'The Catechism of the Council of Trent in four parts — the Apostles\' Creed, the seven sacraments, the ten commandments, and the Lord\'s Prayer. The definitive Counter-Reformation catechesis, written for pastors rather than children.',
    },
  },

  # ─── Baltimore Catechism No. 3 (Gutenberg #14553) ────────────────────────────
  {
    'id':   'baltimore-catechism',
    'gutenberg_id': 14553,
    'split_h': 'h3', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'BalCat', 'title': 'Baltimore Catechism',
      'year': 1885, 'type': 'catechism', 'tradition': 'catholic', 'era': 'modern',
      'desc': 'The standard American Catholic catechism for nearly a century — God, creation, the Creed, the sacraments, the commandments, and the last things in Q&A form. Catechism No. 3 (the adult edition).',
    },
  },

  # ─── Ignatius — Three remaining letters (Ephesians, Magnesians, Trallians) ───
  {
    'id':   'ignatius-ephesians',
    'page': 'Ante-Nicene Christian Library/Epistle to the Ephesians',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'IgnE', 'title': 'Letter to the Ephesians',
      'year': 108, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Ignatius of Antioch',
      'desc': 'On unity with the bishop, faith and love as the beginning and end of life, and the medicine of immortality — Christ our physician who has triumphed over death.',
    },
  },
  {
    'id':   'ignatius-magnesians',
    'page': 'Ante-Nicene Christian Library/Epistle to the Magnesians',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'IgnM', 'title': 'Letter to the Magnesians',
      'year': 108, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Ignatius of Antioch',
      'desc': 'Against Judaizing; on respecting a youthful bishop; living on the Lord\'s Day not the Sabbath — Christ is our only teacher.',
    },
  },
  {
    'id':   'ignatius-trallians',
    'page': 'Ante-Nicene Christian Library/Epistle to the Trallians',
    'split_h': 'h2', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'IgnT', 'title': 'Letter to the Trallians',
      'year': 108, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Ignatius of Antioch',
      'desc': 'On obedience to bishop and deacons; against Docetism — Christ truly suffered, died, and rose; his suffering was not mere appearance.',
    },
  },

  # ── Julian of Norwich ─────────────────────────────────────────────────────
  {
    'id': 'julian-revelations',
    'ccel_grouped': [
      {'heading': 'Showings I–V — The Passion, the Trinity, and the Hazelnut',
       'base_url': 'https://ccel.org/ccel/julian/revelations/',
       'pages': [f'revelations.{r}.html' for r in ['ii','iii','iv','v','vi','vii','viii']]},
      {'heading': 'Showings VI–XII — Sin, Suffering, and Divine Compassion',
       'base_url': 'https://ccel.org/ccel/julian/revelations/',
       'pages': [f'revelations.{r}.html' for r in ['ix','x','xi','xii','xiii','xiv','xv']]},
      {'heading': 'Showings XIII–XV — The Lord and the Servant; All Shall Be Well',
       'base_url': 'https://ccel.org/ccel/julian/revelations/',
       'pages': [f'revelations.{r}.html' for r in ['xvi','xvii','xviii','xix','xx','xxi']]},
      {'heading': 'Showing XVI — Love Is the Meaning',
       'base_url': 'https://ccel.org/ccel/julian/revelations/',
       'pages': [f'revelations.{r}.html' for r in ['xxii','xxiii','xxiv','xxv','xxvi']]},
    ],
    'index_meta': {
      'abbrev': 'JulR', 'title': 'Revelations of Divine Love',
      'year': 1393, 'type': 'father', 'tradition': 'catholic', 'era': 'medieval',
      'author': 'Julian of Norwich',
      'desc': '"All shall be well, and all shall be well, and all manner of thing shall be well." — The first book written in English by a woman: 16 showings of divine love, the hazelnut, the lord and the servant, and the motherhood of God.',
    },
  },

  # ── Ignatius of Loyola — Spiritual Exercises (CCEL) ──────────────────────
  {
    'id': 'ignatius-spiritual-exercises',
    'ccel_grouped': [
      {'heading': 'Annotations, Presupposition, and Foundation',
       'base_url': 'https://ccel.org/ccel/ignatius/exercises/',
       'pages': ['exercises.ii.html','exercises.ii.i.html','exercises.ii.ii.html','exercises.ii.iii.html']},
      {'heading': 'First Week — Principle, Foundation, Sin, and Hell',
       'base_url': 'https://ccel.org/ccel/ignatius/exercises/',
       'pages': ['exercises.iii.html'] + [f'exercises.iii.{r}.html' for r in ['i','ii','iii','iv','v','vi','vii']]},
      {'heading': 'Second Week — The Kingdom, Election, and the Life of Christ',
       'base_url': 'https://ccel.org/ccel/ignatius/exercises/',
       'pages': ['exercises.iv.html'] + [f'exercises.iv.{r}.html' for r in ['i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii','xiv','xv']]},
      {'heading': 'Third and Fourth Weeks — The Passion and the Resurrection',
       'base_url': 'https://ccel.org/ccel/ignatius/exercises/',
       'pages': ['exercises.v.html','exercises.vi.html','exercises.vii.html','exercises.viii.html','exercises.ix.html']},
    ],
    'index_meta': {
      'abbrev': 'SpiEx', 'title': 'Spiritual Exercises',
      'year': 1548, 'type': 'father', 'tradition': 'catholic', 'era': 'reformation',
      'author': 'Ignatius of Loyola',
      'desc': 'The four-week retreat program that formed the Jesuits — meditations on sin, the two standards, election, the life of Christ, the Passion, and the Contemplation to Attain Love.',
    },
  },

  # ── William Law — A Serious Call (CCEL) ───────────────────────────────────
  {
    'id': 'william-law-serious-call',
    'ccel_grouped': [
      {'heading': 'Chapters I–VIII — The Nature and Neglect of Devotion',
       'base_url': 'https://ccel.org/ccel/law/serious_call/',
       'pages': [f'serious_call.{r}.html' for r in ['i','ii','iii','iv','v','vi','vii','viii']]},
      {'heading': 'Chapters IX–XVI — The Right Use of Time and Occupation',
       'base_url': 'https://ccel.org/ccel/law/serious_call/',
       'pages': [f'serious_call.{r}.html' for r in ['ix','x','xi','xii','xiii','xiv','xv','xvi']]},
      {'heading': 'Chapters XVII–XXIV — Prayer, Humility, and the Spirit of Love',
       'base_url': 'https://ccel.org/ccel/law/serious_call/',
       'pages': [f'serious_call.{r}.html' for r in ['xvii','xviii','xix','xx','xxi','xxii','xxiii','xxiv']]},
    ],
    'index_meta': {
      'abbrev': 'LawSC', 'title': 'A Serious Call to a Devout and Holy Life',
      'year': 1729, 'type': 'father', 'tradition': 'anglican', 'era': 'modern',
      'author': 'William Law',
      'desc': 'The book that converted John Wesley and moved C.S. Lewis — bringing every hour, occupation, and relationship under the rule of devotion to God.',
    },
  },

  # ── Martin Luther — The Bondage of the Will (CCEL) ────────────────────────
  {
    'id': 'luther-bondage-of-will',
    'ccel_grouped': [
      {'heading': "Introduction — Luther to Erasmus; Erasmus's Scepticism",
       'base_url': 'https://ccel.org/ccel/luther/bondage/',
       'pages': ['bondage.v.html','bondage.vi.html','bondage.vii.html','bondage.viii.html','bondage.ix.html','bondage.x.html']},
      {'heading': 'Discussion Part I — Free Will in Scripture',
       'base_url': 'https://ccel.org/ccel/luther/bondage/',
       'pages': ['bondage.xi.html'] + [f'bondage.xi.{r}.html' for r in ['i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii']]},
      {'heading': 'Discussion Part II — The Bound Will and Sovereign Grace',
       'base_url': 'https://ccel.org/ccel/luther/bondage/',
       'pages': ['bondage.xii.html'] + [f'bondage.xii.{r}.html' for r in ['i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii','xiv','xv','xvi','xvii']]},
      {'heading': "Discussion Part III — Conclusion and Luther's Final Argument",
       'base_url': 'https://ccel.org/ccel/luther/bondage/',
       'pages': ['bondage.xiii.html','bondage.xiv.html']},
    ],
    'index_meta': {
      'abbrev': 'LutBW', 'title': 'The Bondage of the Will',
      'year': 1525, 'type': 'father', 'tradition': 'lutheran', 'era': 'reformation',
      'author': 'Martin Luther',
      'desc': "Luther's reply to Erasmus — the book he himself considered his most important: the will is bound to sin apart from grace; salvation is entirely of God from first to last.",
      'series': 'luther', 'series_title': 'Works of Martin Luther',
      'volume': 5, 'volume_label': 'Bondage of the Will',
    },
  },

  # ── George Whitefield — Selected Sermons (CCEL) ───────────────────────────
  {
    'id': 'whitefield-sermons',
    'ccel_grouped': [
      {'heading': 'Sermons on Faith and the New Birth',
       'base_url': 'https://ccel.org/ccel/whitefield/sermons/',
       'pages': ['sermons.iii.html','sermons.iv.html','sermons.v.html','sermons.xv.html','sermons.xvi.html','sermons.xvii.html']},
      {'heading': 'Sermons on the Christian Life and Duty',
       'base_url': 'https://ccel.org/ccel/whitefield/sermons/',
       'pages': ['sermons.vi.html','sermons.xi.html','sermons.xiii.html','sermons.xiv.html']},
    ],
    'index_meta': {
      'abbrev': 'WhiS', 'title': 'Selected Sermons',
      'year': 1737, 'type': 'father', 'tradition': 'methodist', 'era': 'modern',
      'author': 'George Whitefield',
      'desc': "Ten sermons from the Great Awakening preacher — Walking with God, The Lord Our Righteousness, Abraham's faith, the new birth, and the duty of holy living.",
    },
  },

  # ── Richard Baxter — The Reformed Pastor (CCEL) ───────────────────────────
  {
    'id': 'baxter-reformed-pastor',
    'ccel_grouped': [
      {'heading': 'Part I — The Oversight of Ourselves',
       'base_url': 'https://ccel.org/ccel/baxter/pastor/',
       'pages': ['pastor.i.html','pastor.i.i.html','pastor.i.ii.html','pastor.i.iii.html']},
      {'heading': 'Part II — The Oversight of the Flock: Catechizing and Instruction',
       'base_url': 'https://ccel.org/ccel/baxter/pastor/',
       'pages': ['pastor.ii.html','pastor.ii.i.html','pastor.ii.ii.html']},
      {'heading': 'Part III — The Manner of Our Oversight',
       'base_url': 'https://ccel.org/ccel/baxter/pastor/',
       'pages': ['pastor.iii.html','pastor.iii.i.html','pastor.iii.ii.html','pastor.iii.iii.html']},
      {'heading': 'Part IV — Motives to the Oversight of the Flock',
       'base_url': 'https://ccel.org/ccel/baxter/pastor/',
       'pages': ['pastor.iv.html','pastor.iv.i.html','pastor.iv.ii.html',
                 'pastor.iv.iii.html','pastor.iv.iv.html','pastor.iv.v.html',
                 'pastor.v.html','pastor.v.i.html']},
    ],
    'index_meta': {
      'abbrev': 'BaxRP', 'title': 'The Reformed Pastor',
      'year': 1656, 'type': 'father', 'tradition': 'reformed', 'era': 'post-reformation',
      'author': 'Richard Baxter',
      "desc": "The Puritan masterwork on pastoral ministry — overseeing yourself before your flock; diligent personal catechizing of every household as the heart of the pastor's work.",
    },
  },

  # ── The Rule of St. Benedict (CCEL) ──────────────────────────────────────
  {
    'id': 'benedict-rule',
    'ccel_grouped': [
      {'heading': 'Prologue and Chapters 1–20 — The Abbot, the Kinds of Monks, and Liturgy',
       'base_url': 'https://ccel.org/ccel/benedict/rule/',
       'pages': [f'rule.{r}.html' for r in [
         'i','ii','iii','iv','v','vi','vii','viii','ix','x',
         'xi','xii','xiii','xiv','xv','xvi','xvii','xviii','xix','xx',
       ]]},
      {'heading': 'Chapters 21–48 — Discipline, Excommunication, Prayer, and Work',
       'base_url': 'https://ccel.org/ccel/benedict/rule/',
       'pages': [f'rule.{r}.html' for r in [
         'xxi','xxii','xxiii','xxiv','xxv','xxvi','xxvii','xxviii','xxix','xxx',
         'xxxi','xxxii','xxxiii','xxxiv','xxxv','xxxvi','xxxvii','xxxviii','xxxix','xl',
         'xli','xlii','xliii','xliv','xlv','xlvi','xlvii','xlviii',
       ]]},
      {'heading': 'Chapters 49–73 — Lenten Practice, Community Life, and the Good Zeal',
       'base_url': 'https://ccel.org/ccel/benedict/rule/',
       'pages': [f'rule.{r}.html' for r in [
         'xlix','l','li','lii','liii','liv','lv','lvi','lvii','lviii',
         'lix','lx','lxi','lxii','lxiii','lxiv','lxv','lxvi','lxvii','lxviii',
         'lxix','lxx','lxxi','lxxii','lxxiii',
       ]]},
    ],
    'index_meta': {
      'abbrev': 'BenR', 'title': 'The Rule of St. Benedict',
      'year': 530, 'type': 'father', 'tradition': 'catholic', 'era': 'patristic',
      'author': 'Benedict of Nursia',
      'desc': 'The foundational rule of Western monasticism — governing prayer, work, humility, community life, and the abbot\'s office with extraordinary wisdom. Followed continuously for 1,500 years.',
    },
  },

  # ── Pseudo-Dionysius the Areopagite — Works (CCEL) ───────────────────────
  {
    'id': 'pseudo-dionysius-works',
    'ccel_grouped': [
      {'heading': 'The Celestial Hierarchy',
       'base_url': 'https://ccel.org/ccel/dionysius/works/',
       'pages': ['works.i.html'] + [f'works.i.{r}.html' for r in [
         'i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii','xiv','xv',
       ]]},
      {'heading': 'The Ecclesiastical Hierarchy',
       'base_url': 'https://ccel.org/ccel/dionysius/works/',
       'pages': ['works.ii.html'] + [f'works.ii.{r}.html' for r in [
         'i','ii','iii','iv','v','vi','vii',
       ]]},
      {'heading': 'The Divine Names',
       'base_url': 'https://ccel.org/ccel/dionysius/works/',
       'pages': ['works.iii.html'] + [f'works.iii.{r}.html' for r in [
         'i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii',
       ]]},
    ],
    'index_meta': {
      'abbrev': 'DiW', 'title': 'Works of Pseudo-Dionysius',
      'year': 500, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Pseudo-Dionysius the Areopagite',
      'desc': 'The anonymous Syrian theologian whose Celestial Hierarchy, Divine Names, and Mystical Theology became foundational for all subsequent Christian mysticism — East and West — and profoundly shaped Aquinas, Eckhart, and the hesychast tradition.',
    },
  },

  # ── The Cloud of Unknowing (Wikisource) ───────────────────────────────────
  {
    'id': 'cloud-of-unknowing',
    'grouped_pages': [
      {'heading': 'Chapters 1–30 — The Cloud, Contemplation, and the Work',
       'pages': [f'The Cloud of Unknowing/Chapter {i}' for i in range(1, 31)]},
      {'heading': 'Chapters 31–75 — Distractions, Charity, and the Perfect Will',
       'pages': [f'The Cloud of Unknowing/Chapter {i}' for i in range(31, 76)]},
    ],
    'index_meta': {
      'abbrev': 'CldU', 'title': 'The Cloud of Unknowing',
      'year': 1375, 'type': 'father', 'tradition': 'catholic', 'era': 'medieval',
      'desc': 'The anonymous 14th-century English masterwork of apophatic mysticism — contemplating God not through ideas but through love alone, in the "cloud of unknowing" where all thought must cease.',
    },
  },

  # ── Catherine of Siena — The Dialogue (CCEL) ─────────────────────────────
  {
    'id': 'catherine-dialogue',
    'ccel_grouped': [
      {'heading': 'Part I — The Treatise on Discretion and Obedience',
       'base_url': 'https://ccel.org/ccel/catherine/dialog/',
       'pages': ['dialog.iv.html'] + [f'dialog.iv.{r}.html' for r in [
         'i','ii','ii.i','ii.ii','ii.iii','ii.iv','ii.v','ii.vi',
       ]]},
      {'heading': 'Part II — The Treatise on Prayer and the Three Stairs',
       'base_url': 'https://ccel.org/ccel/catherine/dialog/',
       'pages': [f'dialog.iv.{r}.html' for r in [
         'iii','iii.i','iii.ii','iii.iii','iii.iv','iii.v',
         'iv','iv.i','iv.ii','iv.iii',
       ]]},
      {'heading': 'Part III — The Treatise on Divine Providence and Tears',
       'base_url': 'https://ccel.org/ccel/catherine/dialog/',
       'pages': [f'dialog.iv.{r}.html' for r in [
         'v','v.i','v.ii','v.iii','v.iv','v.v','v.vi','v.vii','v.viii','v.ix','v.x','v.xi','v.xii',
       ]]},
    ],
    'index_meta': {
      'abbrev': 'CatD', 'title': 'The Dialogue',
      'year': 1378, 'type': 'father', 'tradition': 'catholic', 'era': 'medieval',
      'author': 'Catherine of Siena',
      'desc': 'Dictated in ecstasy — a dialogue between Catherine\'s soul and God the Father on discretion, prayer, the Three Stairs of the soul, divine providence, and the Blood of Christ. Doctor of the Church.',
    },
  },

  # ── Meister Eckhart — Sermons (CCEL) ─────────────────────────────────────
  {
    'id': 'meister-eckhart-sermons',
    'ccel_grouped': [
      {'heading': 'Sermons I–VII',
       'base_url': 'https://ccel.org/ccel/eckhart/sermons/',
       'pages': [f'sermons.{r}.html' for r in ['v','vi','vii','viii','ix','x']]},
    ],
    'index_meta': {
      'abbrev': 'EckS', 'title': 'Sermons',
      'year': 1300, 'type': 'father', 'tradition': 'catholic', 'era': 'medieval',
      'author': 'Meister Eckhart',
      'desc': 'German Dominican sermons on the birth of the Word in the soul, detachment, and the ground of the soul — the most radical and influential of the medieval German mystics.',
    },
  },

  # ── Jeremy Taylor — Holy Living & Holy Dying (CCEL) ──────────────────────
  {
    'id': 'taylor-holy-living',
    'ccel_grouped': [
      {'heading': 'Chapter I — General Instruments and Means Serving to a Holy Life',
       'base_url': 'https://ccel.org/ccel/taylor/holy_living/',
       'pages': ['holy_living.ii.html'] + [f'holy_living.ii.{r}.html' for r in [
         'i','ii','iii','iv',
       ]]},
      {'heading': 'Chapter II — Christian Sobriety',
       'base_url': 'https://ccel.org/ccel/taylor/holy_living/',
       'pages': ['holy_living.iii.html'] + [f'holy_living.iii.{r}.html' for r in [
         'i','i.i','i.ii','i.iii','ii','ii.i','ii.ii','ii.iii','iii','iii.i',
       ]]},
      {'heading': 'Chapter III — Christian Justice and Religion',
       'base_url': 'https://ccel.org/ccel/taylor/holy_living/',
       'pages': ['holy_living.iv.html','holy_living.v.html','holy_living.vi.html'] + [
         f'holy_living.{r}.html' for r in ['vi.i','vi.ii','vi.iii','vi.iv','vi.v','vi.vi']
       ]},
    ],
    'index_meta': {
      'abbrev': 'TayHL', 'title': 'Holy Living',
      'year': 1650, 'type': 'father', 'tradition': 'anglican', 'era': 'post-reformation',
      'author': 'Jeremy Taylor',
      'desc': 'The greatest Anglican devotional classic — the means of holy living, sobriety, justice, and religion in daily life, with rules and prayers for every part of ordinary Christian existence.',
    },
  },

  # ── Gallican / French Confession of Faith (1559) — Wikisource ────────────
  {
    'id':   'gallican-confession',
    'page': 'The Creeds of Christendom: with a History and Critical Notes/Volume III/The Gallican Confession, A.D. 1559',
    'split_h': 'h3', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'GallC', 'title': 'Gallican Confession',
      'year': 1559, 'type': 'confession', 'tradition': 'reformed', 'era': 'reformation',
      'author': 'Theodore de Bèze (rev. John Calvin)',
      'desc': 'The confession of the French Reformed Churches — 40 articles adopted by the first National Synod in Paris (1559), revised by Calvin; the foundational document of French Protestantism.',
    },
  },

  # ── Scots Confession (1560) — Wikisource ─────────────────────────────────
  {
    'id':   'scots-confession',
    'page': 'Scots Confession',
    'split_h': 'h3', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'ScotsC', 'title': 'Scots Confession',
      'year': 1560, 'type': 'confession', 'tradition': 'reformed', 'era': 'reformation',
      'author': 'John Knox et al.',
      'desc': 'The confession of the Scottish Reformation — 25 articles drafted by Knox and colleagues in 1560 and accepted by Parliament; foundational for Scottish Presbyterianism.',
    },
  },

  # ── New Hampshire Baptist Confession of Faith (1833) — Wikisource ─────────
  {
    'id':   'new-hampshire-confession',
    'page': 'New Hampshire Baptist Confession of Faith (1833)',
    'split_h': 'h3', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'NHConf', 'title': 'New Hampshire Confession of Faith',
      'year': 1833, 'type': 'confession', 'tradition': 'baptist', 'era': 'modern',
      'author': 'John Newton Brown',
      'desc': 'The most widely adopted American Baptist confession — 18 articles covering Scripture, God, salvation, the church, and eschatology; shaped Baptist doctrine throughout the 19th–20th centuries.',
    },
  },

  # ── Abstract of Principles (1858) — Wikisource ─────────────────────────────
  {
    'id':   'abstract-of-principles',
    'page': 'Abstract of Principles',
    'split_h': 'h3', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'AbstP', 'title': 'Abstract of Principles',
      'year': 1858, 'type': 'confession', 'tradition': 'baptist', 'era': 'modern',
      'author': 'Basil Manly Jr.',
      'desc': 'The confessional standard of The Southern Baptist Theological Seminary — 20 articles on Scripture, God, election, sin, salvation, and the church; still binding on faculty.',
    },
  },

  # ── Methodist Articles of Religion (1784) — Wikisource ─────────────────────
  {
    'id':   'methodist-articles-of-religion',
    'page': 'Articles of Religion (Methodist)',
    'split_h': 'h3', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'MethAR', 'title': 'Methodist Articles of Religion',
      'year': 1784, 'type': 'confession', 'tradition': 'methodist', 'era': 'modern',
      'author': 'John Wesley',
      'desc': "Wesley's 25-article adaptation of the Church of England's Thirty-Nine Articles, adopted at the Baltimore Conference of 1784 — the founding confessional document of American Methodism.",
    },
  },

  # ── Melanchthon — Apology of the Augsburg Confession (Gutenberg #6744) ────
  {
    'id':          'apology-augsburg-confession',
    'gutenberg_id': 6744,
    'split_h': 'h2', 'max_sections': 12,
    'index_meta': {
      'abbrev': 'ApAC', 'title': 'Apology of the Augsburg Confession',
      'year': 1531, 'type': 'confession', 'tradition': 'lutheran', 'era': 'reformation',
      'author': 'Philip Melanchthon',
      'desc': 'Melanchthon\'s detailed defence of the Augsburg Confession against the Catholic Confutation — the longest document in the Book of Concord, with special depth on justification by faith.',
    },
  },

  # ── Luther — Large Catechism (Gutenberg #1722, Bente/Dau tr., 1529) ───────
  {
    'id':          'luther-large-catechism',
    'gutenberg_id': 1722,
    'split_h': 'h5', 'max_sections': 0,
    'index_meta': {
      'abbrev': 'LrgCat', 'title': 'Large Catechism',
      'year': 1529, 'type': 'confession', 'tradition': 'lutheran', 'era': 'reformation',
      'author': 'Martin Luther',
      'desc': 'Luther\'s comprehensive exposition of the Ten Commandments, Creed, Lord\'s Prayer, Baptism, and Lord\'s Supper — the adult companion to the Small Catechism, written for pastors and teachers.',
    },
  },

  # ── Book of Common Prayer (1662) — key services from Wikisource 1892 facsimile ─
  {
    'id': 'book-of-common-prayer',
    'subpages': [
      {'page': 'Book of Common Prayer (1892)/Morning Prayer',
       'heading': 'Morning Prayer'},
      {'page': 'Book of Common Prayer (1892)/Evening Prayer',
       'heading': 'Evening Prayer'},
      {'page': 'Book of Common Prayer (1892)/The Communion',
       'heading': 'The Holy Communion'},
      {'page': 'Book of Common Prayer (1892)/The Litanie',
       'heading': 'The Litany'},
    ],
    'index_meta': {
      'abbrev': 'BCP62', 'title': 'Book of Common Prayer (1662)',
      'year': 1662, 'type': 'liturgy', 'tradition': 'anglican', 'era': 'post-reformation',
      'author': 'Church of England',
      'desc': 'The 1662 revision of the Church of England\'s liturgical standard — the most '
              'influential Protestant worship text in the English language. Included here: '
              'Morning Prayer, Evening Prayer, Holy Communion, and the Litany.',
    },
  },

  # ── Theophilus of Antioch — To Autolycus (c. 180) — ANF Vol II, Wikisource ──────
  {
    'id': 'theophilus-autolycus',
    'grouped_pages': [
      {'heading': 'Book I — Existence and Nature of God',
       'pages': ['Ante-Nicene Fathers/Volume II/Theophilus to Autolycus/Book I']},
      {'heading': 'Book II — Creation, Scripture, and Pagan Mythology',
       'pages': ['Ante-Nicene Fathers/Volume II/Theophilus to Autolycus/Book II']},
      {'heading': 'Book III — Moral Superiority of Christian Teaching',
       'pages': ['Ante-Nicene Fathers/Volume II/Theophilus to Autolycus/Book III']},
    ],
    'index_meta': {
      'abbrev': 'TheophA', 'title': 'To Autolycus',
      'year': 180, 'type': 'father', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Theophilus of Antioch',
      'desc': 'Three books addressed to the pagan Autolycus — the earliest surviving Christian '
              'apology to a named individual. Theophilus argues for the existence and nature of '
              'God from creation, defends Scripture against pagan mythology, and demonstrates '
              'the moral superiority of Christian teaching. Contains the first recorded use of '
              'the word "Trinity" (τριάς) in Christian literature.',
    },
  },

  # ── James Orr — The Christian View of God and the World (1893) — CCEL ──────────
  {
    'id': 'orr-christian-view',
    'ccel_grouped': [
      {'heading': 'Preface, Introduction, and Lecture I — The Christian View of the World',
       'base_url': 'https://ccel.org/ccel/orr/view/',
       'pages': ['view.ii.html', 'view.iii.html', 'view.v.html',
                 'view.vii.html', 'view.viii.html']},
      {'heading': 'Lectures II–III — Alternatives and the Theistic Postulate',
       'base_url': 'https://ccel.org/ccel/orr/view/',
       'pages': ['view.ix.html', 'view.x.html', 'view.xi.html', 'view.xii.html']},
      {'heading': 'Lectures IV–V — Nature, Man, and Sin',
       'base_url': 'https://ccel.org/ccel/orr/view/',
       'pages': ['view.xiii.html', 'view.xiv.html', 'view.xv.html']},
      {'heading': 'Lectures VI–VII — The Incarnation',
       'base_url': 'https://ccel.org/ccel/orr/view/',
       'pages': ['view.xvi.html', 'view.xvii.html', 'view.xviii.html']},
      {'heading': 'Lectures VIII–IX and Appendix — Redemption and Human Destiny',
       'base_url': 'https://ccel.org/ccel/orr/view/',
       'pages': ['view.xix.html', 'view.xx.html', 'view.xxi.html']},
    ],
    'index_meta': {
      'abbrev': 'OrrCVGW', 'title': 'The Christian View of God and the World',
      'year': 1893, 'type': 'father', 'tradition': 'reformed', 'era': 'modern',
      'author': 'James Orr',
      'desc': 'Nine Kerr Lectures presenting Christianity as a unified world-view against '
              'materialist and idealist alternatives — covering the theistic postulate, the '
              'nature of man and sin, the Incarnation, redemption, and human destiny. '
              'The most systematic conservative Reformed apologetic of the 19th century.',
    },
  },

  # ── Apostolic Constitutions (c. 380) — ANF Vol VII, Wikisource section pages ──
  {
    'id': 'apostolic-constitutions',
    'grouped_pages': [
      {'heading': 'Introductory Notice and Book I — On the Laity',
       'pages': [
         'Ante-Nicene Fathers/Volume VII/Constitutions of the Holy Apostles/Introductory Notice',
         'Ante-Nicene Fathers/Volume VII/Constitutions of the Holy Apostles/Book I/Sec. I',
         'Ante-Nicene Fathers/Volume VII/Constitutions of the Holy Apostles/Book I/Sec. II',
         'Ante-Nicene Fathers/Volume VII/Constitutions of the Holy Apostles/Book I/Sec. III',
       ]},
      {'heading': 'Book II — On Bishops, Presbyters, and Deacons',
       'pages': [
         f'Ante-Nicene Fathers/Volume VII/Constitutions of the Holy Apostles/Book II/Sec. {r}'
         for r in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
       ]},
      {'heading': 'Books III–V — On Widows, Orphans, Confession, and Martyrs',
       'pages': (
         ['Ante-Nicene Fathers/Volume VII/Constitutions of the Holy Apostles/Book III/Sec. I',
          'Ante-Nicene Fathers/Volume VII/Constitutions of the Holy Apostles/Book III/Sec. II'] +
         ['Ante-Nicene Fathers/Volume VII/Constitutions of the Holy Apostles/Book IV/Sec. I',
          'Ante-Nicene Fathers/Volume VII/Constitutions of the Holy Apostles/Book IV/Sec. II'] +
         [f'Ante-Nicene Fathers/Volume VII/Constitutions of the Holy Apostles/Book V/Sec. {r}'
          for r in ['I', 'II', 'III']]
       )},
      {'heading': 'Book VI — On Schism, Heresy, and the Christian Life',
       'pages': [
         f'Ante-Nicene Fathers/Volume VII/Constitutions of the Holy Apostles/Book VI/Sec. {r}'
         for r in ['I', 'II', 'III', 'IV', 'V', 'VI']
       ]},
      {'heading': 'Book VII — On the Eucharist and Christian Initiation',
       'pages': [
         f'Ante-Nicene Fathers/Volume VII/Constitutions of the Holy Apostles/Book VII/Sec. {r}'
         for r in ['I', 'II', 'III', 'IV', 'V']
       ]},
      {'heading': 'Book VIII — Ordination, Gifts, and the Apostolic Canons',
       'pages': (
         [f'Ante-Nicene Fathers/Volume VII/Constitutions of the Holy Apostles/Book VIII/Sec. {r}'
          for r in ['I', 'II', 'III', 'IV', 'V']] +
         ['Ante-Nicene Fathers/Volume VII/Constitutions of the Holy Apostles/Book VIII/'
          'The Ecclesiastical Canons of the Same Holy Apostles']
       )},
    ],
    'index_meta': {
      'abbrev': 'ApCon', 'title': 'Apostolic Constitutions',
      'year': 380, 'type': 'liturgy', 'tradition': 'patristic', 'era': 'patristic',
      'author': 'Unknown (attributed to Clement of Rome)',
      'desc': 'The most comprehensive early church order in eight books — prescribing conduct '
              'for the laity, clergy, widows, and orphans; addressing martyrdom, heresy, and '
              'schism; and culminating in the Eucharistic prayer, baptismal rites, ordination '
              'formularies, and 85 Apostolic Canons. The fullest window into 3rd–4th-century '
              'Christian worship and polity.',
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
  """Return True if tag is a div wrapping (only) the target heading level.
  Handles Wikisource div.mw-heading and Gutenberg div.chapter (heading-only form)."""
  if tag.name != 'div':
    return False
  classes = tag.get('class', [])
  # Wikisource modern format
  if 'mw-heading' in classes and tag.find(split_h) is not None:
    return True
  # Gutenberg div.chapter where the div contains only the heading (+ optional page markers)
  _MAX_EXTRA_CHARS = 10  # page numbers like "iii", "45" are ≤10 chars
  if 'chapter' in classes:
    h = tag.find(split_h)
    if h is None:
      return False
    extra = tag.get_text(strip=True).replace(h.get_text(strip=True), '', 1).strip()
    return len(extra) <= _MAX_EXTRA_CHARS
  return False


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
  - Gutenberg <div class="chapter"> structure (each div is one section)

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
  # INTENT: Emit BSW library v2 format: each section's first child must be
  #   <h2 class="lib-section__title"> per R3 validation rule.
  from html import escape as _escape
  parts = []
  for s in sections:
    heading     = s['heading'].replace('"', '&quot;')
    title_text  = s['heading'] or 'Preface'
    title_tag   = f'<h2 class="lib-section__title">{_escape(title_text)}</h2>\n'
    parts.append(f'<section data-heading="{heading}">\n{title_tag}{s["html"]}\n</section>')
  return '\n\n'.join(parts) + '\n'


# ---------------------------------------------------------------------------
# Project Gutenberg fetch
# ---------------------------------------------------------------------------

_GUTENBERG_STRIP_SEL = [
  '#pg-header', '#pg-footer', '#pg-machine-header',
  '#pg-start-separator', '#pg-end-separator',
  '.pg-header', '.pg-footer',
  '.tnotes',   # transcriber's notes
  'pre',
]
# Markers that signal the start of the Gutenberg end-of-document license block
_GUTENBERG_END_MARKERS = [
  '*** END OF THE PROJECT GUTENBERG',
  '*** END OF THIS PROJECT GUTENBERG',
  'End of Project Gutenberg',
  'End of the Project Gutenberg',
]
# Markers that signal the start of actual book content (strip anything before)
_GUTENBERG_START_MARKERS = [
  '*** START OF THE PROJECT GUTENBERG',
  '*** START OF THIS PROJECT GUTENBERG',
  '***START OF THE PROJECT GUTENBERG',
  '***START OF THIS PROJECT GUTENBERG',
]

def _clean_gutenberg_soup(soup):
  for sel in _GUTENBERG_STRIP_SEL:
    for el in soup.select(sel):
      el.decompose()
  for img in soup.find_all('img'):
    img.decompose()
  # Remove the start-marker element and its preceding siblings (Gutenberg boilerplate header)
  for text_node in soup.find_all(string=True):
    s = str(text_node)
    if any(m in s for m in _GUTENBERG_START_MARKERS):
      for sib in list(text_node.parent.find_previous_siblings()):
        try: sib.decompose()
        except Exception: pass
      try: text_node.parent.decompose()
      except Exception: pass
      break
  # Truncate at the end-of-document license marker
  for text_node in soup.find_all(string=True):
    s = str(text_node)
    if any(m in s for m in _GUTENBERG_END_MARKERS):
      for el in list(text_node.parent.find_all_next()):
        try: el.decompose()
        except Exception: pass
      try: text_node.parent.decompose()
      except Exception: pass
      break
  return soup


def _fetch_gutenberg_soup(gutenberg_id):
  """Try Gutenberg URL patterns in order; return a cleaned BeautifulSoup."""
  last_err = None
  for pattern in GUTENBERG_URL_PATTERNS:
    url = pattern.format(id=gutenberg_id)
    try:
      resp = requests.get(url, headers=HEADERS, timeout=60, allow_redirects=True)
      if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        _clean_gutenberg_soup(soup)
        print(f'    fetched from {url}')
        return soup
    except requests.RequestException as e:
      last_err = e
  raise ValueError(f'Could not fetch Gutenberg #{gutenberg_id}: {last_err}')


# ---------------------------------------------------------------------------
# CCEL (Christian Classics Ethereal Library) fetch
# ---------------------------------------------------------------------------

_CCEL_STRIP_SEL = [
  '#reader-toc', 'nav.navbar', '.navbar', '.collapse',
  'script', 'style', '.btn', 'form',
  'a[href*="ccel.org/search"]', 'a[href*="/about/"]',
]

def _fetch_ccel_page_html(url):
  """Fetch one CCEL chapter page, extract #book-section content, return cleaned HTML str."""
  resp = requests.get(url, headers=HEADERS, timeout=30, allow_redirects=True)
  if resp.status_code != 200:
    raise ValueError(f'HTTP {resp.status_code} fetching {url}')
  soup = BeautifulSoup(resp.text, 'html.parser')

  # Extract the main book content div
  section = soup.find(id='book-section') or soup.find(class_='contentSection')
  if not section:
    section = soup.find(id='content')
  if not section:
    return ''

  # Strip CCEL chrome left inside the content div
  for sel in _CCEL_STRIP_SEL:
    for el in section.select(sel):
      el.decompose()
  for img in section.find_all('img'):
    img.decompose()
  # Remove the anchor tag CCEL injects at the top (e.g. <a name="iii.i">)
  for a in section.find_all('a', attrs={'name': True}):
    a.decompose()
  # Remove empty paragraphs
  for p in section.find_all('p'):
    if not p.get_text(strip=True):
      p.decompose()

  return _inner_html_of(section).strip()


def _fetch_ccel_grouped(ccel_groups):
  """
  Process a ccel_grouped manifest entry.
  Each group: {'heading': str, 'base_url': str, 'pages': [filename, ...]}
  Returns a list of {'heading': str, 'html': str} sections.
  """
  sections = []
  for group in ccel_groups:
    heading  = group['heading']
    base_url = group['base_url']
    pages    = group['pages']
    print(f'  group: {heading[:60]}…')
    parts = []
    for page in pages:
      url = base_url + page
      try:
        html = _fetch_ccel_page_html(url)
        if html:
          parts.append(html)
      except Exception as e:
        print(f'    WARN: {url}: {e}')
      time.sleep(RATE_DELAY)
    if parts:
      sections.append({'heading': heading, 'html': '\n'.join(parts)})
      print(f'    → {len(pages)} pages fetched')
  return sections


# ---------------------------------------------------------------------------
# Wikisource fetch
# ---------------------------------------------------------------------------

def _fetch_page_soup(page_title):
  """Fetch and clean a Wikisource page, returning a BeautifulSoup.

  Tries action=parse first (rendered HTML).  On API error or empty content,
  falls back to action=query&prop=revisions (raw wikitext converted to minimal
  HTML paragraphs) so that pages blocked by the renderer still yield something.
  """
  import random

  def _parse_attempt():
    params = {
      'action':             'parse',
      'page':               page_title,
      'prop':               'text',
      'disableeditsection': 'true',
      'disabletoc':         'true',
      'format':             'json',
    }
    for attempt in range(4):
      try:
        resp = requests.get(WS_API, params=params, headers=HEADERS, timeout=45)
        resp.raise_for_status()
        if not resp.text:
          raise ValueError('Empty response body')
        return resp.json()
      except (requests.RequestException, ValueError) as e:
        if attempt < 3:
          delay = 3 * (attempt + 1) + random.uniform(0, 1.5)
          print(f'    retry {attempt+1} after error: {e} (wait {delay:.1f}s)')
          time.sleep(delay)
        else:
          raise

  def _wikitext_fallback():
    """Fetch raw wikitext and convert to basic paragraph HTML."""
    params = {
      'action':  'query',
      'titles':  page_title,
      'prop':    'revisions',
      'rvprop':  'content',
      'rvslots': 'main',
      'format':  'json',
    }
    resp = requests.get(WS_API, params=params, headers=HEADERS, timeout=45)
    resp.raise_for_status()
    data = resp.json()
    pages = data.get('query', {}).get('pages', {})
    for pid, page in pages.items():
      revs = page.get('revisions', [])
      if revs:
        wikitext = revs[0].get('slots', {}).get('main', {}).get('*', '') or revs[0].get('*', '')
        if wikitext:
          # Strip wiki markup and return as paragraph-wrapped plain text
          wikitext = re.sub(r'\{\{[^}]*\}\}', '', wikitext)   # templates
          wikitext = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', wikitext)  # links
          wikitext = re.sub(r"'''+", '', wikitext)             # bold/italic
          wikitext = re.sub(r'={2,6}([^=]+)={2,6}', r'\n\n\1\n\n', wikitext)  # headings
          wikitext = re.sub(r'<ref[^>]*>.*?</ref>', '', wikitext, flags=re.S)
          wikitext = re.sub(r'<[^>]+>', '', wikitext)          # HTML tags
          paras = [p.strip() for p in re.split(r'\n{2,}', wikitext) if p.strip()]
          html  = '\n'.join(f'<p>{p}</p>' for p in paras)
          soup  = BeautifulSoup(f'<div class="mw-parser-output">{html}</div>', 'html.parser')
          print(f'    [wikitext fallback] {len(paras)} paragraph(s)')
          return soup
    raise ValueError('No wikitext content found')

  # ── Primary path: rendered HTML ───────────────────────────────────────────
  try:
    data = _parse_attempt()
  except Exception as e:
    print(f'    parse failed ({e}), trying wikitext fallback…')
    return _wikitext_fallback()

  if 'error' in data:
    code = data['error'].get('code', '')
    info = data['error'].get('info', '')
    if code == 'missingtitle':
      raise ValueError(f'Wikisource API error [{code}]: {info}')
    # Non-fatal API error: try wikitext fallback
    print(f'    API error [{code}]: {info} — trying wikitext fallback…')
    return _wikitext_fallback()

  html = data['parse']['text']['*']
  soup = BeautifulSoup(html, 'html.parser')
  _clean_soup(soup)

  # If we got a nearly-empty page (index/disambiguation), try wikitext
  text_content = (soup.find(class_='mw-parser-output') or soup).get_text(strip=True)
  if len(text_content) < 200:
    print(f'    rendered page suspiciously short ({len(text_content)} chars), trying wikitext fallback…')
    try:
      return _wikitext_fallback()
    except Exception:
      pass  # stick with the (short) rendered result

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
  if 'gutenberg_id' in entry:
    print(f'  mode: gutenberg #{entry["gutenberg_id"]}')
  elif 'ccel_grouped' in entry:
    cg = entry['ccel_grouped']
    total = sum(len(g['pages']) for g in cg)
    print(f'  mode: ccel_grouped ({len(cg)} groups, {total} pages)')
  elif 'grouped_pages' in entry:
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
    if 'gutenberg_id' in entry:
      soup      = _fetch_gutenberg_soup(entry['gutenberg_id'])
      split_h   = entry.get('split_h', 'h2')
      max_secs  = entry.get('max_sections', 0)
      # Use the body as the content root (no mw-parser-output)
      body = soup.find('body') or soup
      sections = _split_into_sections(body, split_h=split_h, max_sections=max_secs)
      print(f'  {len(sections)} section(s)')

    elif 'ccel_grouped' in entry:
      sections = _fetch_ccel_grouped(entry['ccel_grouped'])

    elif 'grouped_pages' in entry:
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
        try:
          soup    = _fetch_page_soup(sp['page'])
          content = soup.find(class_='mw-parser-output') or soup
          html    = str(content)
          sections.append({'heading': sp['heading'], 'html': html})
          print(f' OK ({len(content.find_all("p"))}p)')
        except Exception as e:
          print(f' SKIP ({e})')

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
      if 'ccel_grouped' in e:
        n = sum(len(g['pages']) for g in e['ccel_grouped'])
        mode = f"ccel ({len(e['ccel_grouped'])} groups, {n} pages)"
      elif 'grouped_pages' in e:
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
