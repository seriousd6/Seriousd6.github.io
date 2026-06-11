# Biblepedia Article Synthesis — Progress Tracker

Last updated: 2026-06-10 — Infrastructure initialized. No articles generated yet.

Read before starting: **BP_AGENT_GUIDE.md** → **BP_SCRIPT_GUIDE.md** → this file.

---

## Summary

| Phase | Work Units | Complete | In Progress | Not Started |
|---|---|---|---|---|
| Phase 1 — Easton Main Dictionary (A–Z) | 65 | 0 | 0 | 65 |
| Phase 2 — Gap Articles (Nave/Smith-only) | TBD (run BPG first) | 0 | 0 | TBD |

**Total articles target:** ~4,000 (Phase 1) + ~1,000 (Phase 2 gaps, after BPG)

---

## Phase 1 Work Queue — Easton A–Z

One unit = one Python script covering ~75 entries. Script name: `scripts/bp-{unit}.py`
Output: `data/biblepedia/articles/{slug}.json` per entry in the unit.

| Unit | Range | Count | Status | Script |
|---|---|---|---|---|
| A1 | Aaron → Acre | 75 | in-progress @ 2026-06-10T00:00:00Z | scripts/bp-a1.py |
| A2 | Acts of the Apostles → Ahitub | 75 | not started | scripts/bp-a2.py |
| A3 | Ahlab → Anakim | 75 | not started | scripts/bp-a3.py |
| A4 | Anamim → Areopagus | 75 | not started | scripts/bp-a4.py |
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
| (run BPG first — see BPG_PROGRESS.md) | | | | |
