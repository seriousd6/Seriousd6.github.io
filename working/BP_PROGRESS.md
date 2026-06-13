# Biblepedia Article Synthesis — Progress Tracker

Last updated: 2026-06-10 — Infrastructure initialized. No articles generated yet.

Read before starting: **BP_AGENT_GUIDE.md** → **BP_SCRIPT_GUIDE.md** → this file.

---

## Summary

| Phase | Work Units | Complete | In Progress | Not Started |
|---|---|---|---|---|
| Phase 1 — Easton Main Dictionary (A–Z) | 65 | 0 | 0 | 65 |
| Phase 2 — Gap Articles (Nave/Smith-only) | 9 units (425 stubs) | 0 | 0 | 9 |

**Total articles target:** ~4,000 (Phase 1) + ~1,000 (Phase 2 gaps, after BPG)

---

## Phase 1 Work Queue — Easton A–Z

One unit = one Python script covering ~75 entries. Script name: `scripts/bp-{unit}.py`
Output: `data/biblepedia/articles/{slug}.json` per entry in the unit.

| Unit | Range | Count | Status | Script |
|---|---|---|---|---|
| A1 | Aaron → Acre | 75 | in-progress @ 2026-06-13T13:15:00Z | scripts/bp-a1.py |
| A2 | Acts of the Apostles → Ahitub | 75 | in-progress @ 2026-06-13T13:15:30Z | scripts/bp-a2.py |
| A3 | Ahlab → Anakim | 75 | in-progress @ 2026-06-13T13:18:28Z | scripts/bp-a3.py |
| A4 | Anamim → Areopagus | 75 | in-progress @ 2026-06-13T13:20:00Z | scripts/bp-a4.py |
| A5 | Aretas → Azaziah | 75 | not started | scripts/bp-a5.py |
| A6 | Azekah → Azur and Azzur | 6 | not started | scripts/bp-a6.py |
| B1 | Baal → Barsabas | 75 | not started | scripts/bp-b1.py |
| B2 | Bartholomew → Berechiah | 75 | not started | scripts/bp-b2.py |
| B3 | Bered → Bless | 75 | not started | scripts/bp-b3.py |
| B4 | Blind → By-word | 70 | not started | scripts/bp-b4.py |
| C1 | Cab → Census | 75 | not started | scripts/bp-c1.py |
| C2 | Centurion → Chub | 75 | not started | scripts/bp-c2.py |
| C3 | Chun → Corinthians, First Epistle to the | 75 | not started | scripts/bp-c3.py |
| C4 | Corinthians, Second Epistle to the → Cyrus | 53 | not started | scripts/bp-c4.py |
| D1 | Daberath → Diamond | 75 | not started | scripts/bp-d1.py |
| D2 | Diana → Dye | 71 | not started | scripts/bp-d2.py |
| E1 | Eagle → Eliphelet | 75 | not started | scripts/bp-e1.py |
| E2 | Elisabeth → Eshtaol | 75 | not started | scripts/bp-e2.py |
| E3 | Eshtemoa → Ezri | 47 | not started | scripts/bp-e3.py |
| F1 | Fable → Foreknowledge of God | 75 | not started | scripts/bp-f1.py |
| F2 | Forerunner → Fury | 28 | not started | scripts/bp-f2.py |
| G1 | Gaal → Gibbethon | 75 | not started | scripts/bp-g1.py |
| G2 | Gibeah → Grecians | 75 | not started | scripts/bp-g2.py |
| G3 | Greece → Gutter | 11 | not started | scripts/bp-g3.py |
| H1 | Habakkuk → Harbona | 75 | not started | scripts/bp-h1.py |
| H2 | Hare → Hebrews, Epistle to | 75 | not started | scripts/bp-h2.py |
| H3 | Hebron → Hill of Evil Counsel | 75 | not started | scripts/bp-h3.py |
| H4 | Hillel → Hyssop | 69 | not started | scripts/bp-h4.py |
| I | Ibhar → Izrahite | 65 | not started | scripts/bp-i.py |
| J1 | Jaakan → Jediael | 75 | not started | scripts/bp-j1.py |
| J2 | Jedidiah → Jezreel, Fountain of | 75 | not started | scripts/bp-j2.py |
| J3 | Jezreel, Portion of → Justice | 75 | not started | scripts/bp-j3.py |
| J4 | Justice of God → Juttah | 4 | not started | scripts/bp-j4.py |
| K1 | Kabzeel → Kore | 75 | not started | scripts/bp-k1.py |
| K2 | Korhites → Koz | 2 | not started | scripts/bp-k2.py |
| L1 | Laban → Lip | 75 | not started | scripts/bp-l1.py |
| L2 | Litter → Lystra | 41 | not started | scripts/bp-l2.py |
| M1 | Maachah → Marcus | 75 | not started | scripts/bp-m1.py |
| M2 | Mareshah → Merchant | 75 | not started | scripts/bp-m2.py |
| M3 | Mercurius → Misham | 75 | not started | scripts/bp-m3.py |
| M4 | Misheal → Mystery | 68 | not started | scripts/bp-m4.py |
| N1 | Naam → Nero | 75 | not started | scripts/bp-n1.py |
| N2 | Net → Nymphas | 47 | not started | scripts/bp-n2.py |
| O | Oak → Ozni | 63 | not started | scripts/bp-o.py |
| P1 | Paarai → Peor | 75 | not started | scripts/bp-p1.py |
| P2 | Perazim, Mount → Plain | 75 | not started | scripts/bp-p2.py |
| P3 | Plain of Mamre → Pygarg | 59 | not started | scripts/bp-p3.py |
| Q | Quails → Quotations | 10 | not started | scripts/bp-q.py |
| R1 | Raamah → Resurrection of Christ | 75 | not started | scripts/bp-r1.py |
| R2 | Resurrection of the dead → Rye | 53 | not started | scripts/bp-r2.py |
| S1 | Sabachthani → Scrip | 75 | not started | scripts/bp-s1.py |
| S2 | Scripture → Sharon, Saron | 75 | not started | scripts/bp-s2.py |
| S3 | Shaveh, Valley of → Shiphtan | 75 | not started | scripts/bp-s3.py |
| S4 | Ships → Soap | 75 | not started | scripts/bp-s4.py |
| S5 | Socho → Sychar | 75 | not started | scripts/bp-s5.py |
| S6 | Sychem → Syrophenician | 8 | not started | scripts/bp-s6.py |
| T1 | Taanach → Testimony, Tabernacle of | 75 | not started | scripts/bp-t1.py |
| T2 | Tetrarch → Tooth | 75 | not started | scripts/bp-t2.py |
| T3 | Topaz → Tyropoeon Valley | 38 | not started | scripts/bp-t3.py |
| U | Ucal → Uzziel | 23 | not started | scripts/bp-u.py |
| V | Vagabond → Vulture | 17 | not started | scripts/bp-v.py |
| W | Wafers → Writing | 63 | not started | scripts/bp-w.py |
| Y | Yarn → Yoke-fellow | 5 | not started | scripts/bp-y.py |
| Z1 | Zaanaim → Zibia | 75 | not started | scripts/bp-z1.py |
| Z2 | Zibiah → Zurishaddai | 42 | not started | scripts/bp-z2.py |

---

## Phase 2 Work Queue — Gap Articles

Populated after BPG loop runs. See `BPG_PROGRESS.md`.

When `data/biblepedia/gaps.json` exists, each high-priority gap becomes a row here.
Gap scripts use the naming scheme: `scripts/bp-gap-{topic-group}.py`

| Unit | Topic Group | Count | Status | Script |
|---|---|---|---|---|
| gap-doctrine | Core doctrines, major virtues, prophetic themes (score 33–70) | 27 | not started | scripts/bp-gap-doctrine.py |
| gap-persons | Named biblical persons and places — Smith score-35 | 34 | not started | scripts/bp-gap-persons.py |
| gap-ethics | Character, virtue, vice, and conduct topics (score 20–30) | 49 | not started | scripts/bp-gap-ethics.py |
| gap-smith-a | Smith Bible Dictionary A–H culture/history/ritual (score 25) | 35 | not started | scripts/bp-gap-smith-a.py |
| gap-smith-b | Smith Bible Dictionary I–Z persons/places/books (score 25) | 69 | not started | scripts/bp-gap-smith-b.py |
| gap-ot-context | OT practices, law, places, and prophetic books (score 10) | 54 | not started | scripts/bp-gap-ot-context.py |
| gap-nt-context | NT epistles, persons, practices, and intertestamental (score 10) | 61 | not started | scripts/bp-gap-nt-context.py |
| gap-isbe-theology | ISBE scholarly theology, Christology, and textual studies (score 5) | 65 | not started | scripts/bp-gap-isbe.py |
| gap-minor | Score-3 Nave stubs, minor concepts, and low-priority terms | 31 | not started | scripts/bp-gap-minor.py |
