# Biblepedia Gap Analysis — Progress Tracker

Last updated: 2026-06-13 — Phase 3 complete. 425 stub-needed gaps in 9 BP Phase 2 units. BPG loop DONE.

Read before starting: **BPG_AGENT_GUIDE.md** → **BPG_SCRIPT_GUIDE.md** → this file.

---

## Summary

| Phase | Description | Status |
|---|---|---|
| Phase 1 — Compute | Run bpg-compute-gaps.py → gaps.json | complete (8,344 gaps) |
| Phase 2 — Curate | Review gaps.json and assign statuses | **complete** (C01–C81, all 8,344 gaps) |
| Phase 3 — Populate | Transfer stub-needed gaps to BP_PROGRESS.md Phase 2 | **complete** (9 units, 425 stubs added) |

---

## Phase 1: Compute gaps

Single run, ~30 seconds. No content authoring required.

| Task | Status | Notes |
|---|---|---|
| Run bpg-compute-gaps.py | complete | `python3 scripts/bpg-compute-gaps.py` |
| Verify gaps.json has > 1,000 entries | complete | 8,344 entries |
| Verify top 10 entries are major doctrine/concept gaps | complete | Top: Angel [70], Obedience [70], Judgment [60], Afflictions [50], Jesus the Christ [50] |

Phase 2 is now open. Curation batches below.

---

## Phase 2: Curate the gap list

Work through `data/biblepedia/gaps.json` in batches of ~100 gaps per session.
Each session claims a batch, writes a `bpg-curate-{N}.py` script, runs it, and marks the batch done.

Estimated total: ~2,500 gaps to review. At 100/session ≈ 25 curation sessions.

| Batch | Gap ID Range | Count | Status | Script |
|---|---|---|---|---|
| C01 | angel-a-spirit → aznothtabor (gaps 1–100, priority 70–35) | 100 | complete | scripts/bpg-curate-01.py |
| C02 | azor → elpaal (gaps 101–200, smith-person/place, A–E names) | 100 | complete | scripts/bpg-curate-02.py |
| C03 | elpalet → ishod (gaps 201–300, smith-person/place, E–I names) | 100 | complete | scripts/bpg-curate-03.py |
| C04 | ishpan → letushim (gaps 301–400, smith-person/place, I–L names) | 100 | complete | scripts/bpg-curate-04.py |
| C05 | linus → sharon (gaps 401–500, smith-person/place, L–S names) | 100 | complete | scripts/bpg-curate-05.py |
| C06 | shashai → presumption (gaps 501–600, smith S–Z + doctrine/concept) | 100 | complete | scripts/bpg-curate-06.py |
| C07 | prudence → besor-the-brook (gaps 601–700, score-30 concepts + score-25 smith-scholarly A–B) | 100 | complete | scripts/bpg-curate-07.py |
| C08 | bethezel → genealogy (gaps 701–800, score-25 smith-scholarly B–G) | 100 | complete | scripts/bpg-curate-08.py |
| C09 | gerzites → lacedaemonians (gaps 801–900, score-25 smith-scholarly G–L) | 100 | complete | scripts/bpg-curate-09.py |
| C10 | lantern → principality (gaps 901–1000, score-25 smith-scholarly L–P) | 100 | complete | scripts/bpg-curate-10.py |
| C11 | proconsul → urim-and-thummim (gaps 1001–1100, score-25 smith-scholarly P–U) | 100 | complete | scripts/bpg-curate-11.py |
| C12 | uta → nephish (gaps 1101–1199, score-25 Z names + score-20 concepts/persons) | 99 | complete | scripts/bpg-curate-12.py |
| C13 | ar → shaalbonite (gaps 1200–1299, score-20 concepts + score-15 isbe) | 100 | complete | scripts/bpg-curate-13.py |
| C14 | shalim → asiarchae (gaps 1300–1398, score-15 isbe + score-10 smith-scholarly) | 99 | complete | scripts/bpg-curate-14.py |
| C15 | amath → civil-service (gaps 1399–1498, score-10 smith-scholarly A–C) | 100 | complete | scripts/bpg-curate-15.py |
| C16 | clothing → fraternity (gaps 1499–1598, score-10 smith-scholarly C–F) | 100 | complete | scripts/bpg-curate-16.py |
| C17 | friends → intolerance-religious (gaps 1599–1698, score-10 smith-scholarly F–I) | 100 | complete | scripts/bpg-curate-17.py |
| C18 | irony → magic-magicians (gaps 1699–1798, score-10 smith-scholarly I–M) | 100 | complete | scripts/bpg-curate-18.py |
| C19 | mahavite-the → phares-pharez-or-perez (gaps 1799–1898, score-10 smith-scholarly M–P) | 100 | complete | scripts/bpg-curate-19.py |
| C20 | pharzites-the → shemidaites-the (gaps 1899–1998, score-10 smith-scholarly P–S) | 100 | complete | scripts/bpg-curate-20.py |
| C21 | shemitic-languages → troop-band (gaps 1999–2098, score-10 smith-scholarly S–T) | 100 | complete | scripts/bpg-curate-21.py |
| C22 | trouble → abiron (gaps 2099–2198, final score-10 S–Z + score-8/5 ISBE A entries) | 100 | complete | scripts/bpg-curate-22.py |
| C23 | abisei → aelia (gaps 2199–2298, score-5 isbe-scholarly A entries) | 100 | complete | scripts/bpg-curate-23.py |
| C24 | aeon → amerce (gaps 2299–2398, score-5 isbe-scholarly A entries continued) | 100 | complete | scripts/bpg-curate-24.py |
| C25 | american-revised-version → apply (gaps 2399–2498, score-5 isbe-scholarly A entries) | 100 | complete | scripts/bpg-curate-25.py |
| C26 | appoint → ashhur (gaps 2499–2598, score-5 isbe-scholarly A entries) | 100 | complete | scripts/bpg-curate-26.py |
| C27 | ashkelonites → awa (gaps 2599–2698, score-5 isbe-scholarly A entries) | 100 | complete | scripts/bpg-curate-27.py |
| C28 | await → barnabas-gospel-of (gaps 2699–2798, score-5 isbe-scholarly A–B entries) | 100 | complete | scripts/bpg-curate-28.py |
| C29 | barodis → berries (gaps 2799–2898, score-5 isbe-scholarly B entries) | 100 | complete | scripts/bpg-curate-29.py |
| C30 | berytus → blood-revenge (gaps 2899–2998, score-5 isbe-scholarly B entries) | 100 | complete | scripts/bpg-curate-30.py |
| C31 | bloodguiltiness → broken (gaps 2999–3098, score-5 isbe-scholarly B entries) | 100 | complete | scripts/bpg-curate-31.py |
| C32 | brokenfooted → carry (gaps 3099–3198, score-5 isbe-scholarly B–C entries) | 100 | complete | scripts/bpg-curate-32.py |
| C33 | casdim → chimney (gaps 3199–3298, score-5 isbe-scholarly C entries) | 100 | complete | scripts/bpg-curate-33.py |
| C34 | chinnereth → commit (gaps 3299–3398, score-5 isbe-scholarly C entries) | 100 | complete | scripts/bpg-curate-34.py |
| C35 | commodious → countenance (gaps 3399–3498, score-5 isbe-scholarly C entries) | 100 | complete | scripts/bpg-curate-35.py |
| C36 | counter-charm → dagger (gaps 3499–3598, score-5 isbe-scholarly C–D entries) | 100 | complete | scripts/bpg-curate-36.py |
| C37 | daily → delusion (gaps 3599–3698, score-5 isbe-scholarly D entries) | 100 | complete | scripts/bpg-curate-37.py |
| C38 | demand → door (gaps 3699–3798, score-5 isbe-scholarly D entries) | 100 | complete | scripts/bpg-curate-38.py |
| C39 | doorpost → eleutherus (gaps 3799–3898, score-5 isbe-scholarly D–E entries) | 100 | complete | scripts/bpg-curate-39.py |
| C40 | eleven-the → ephraim-forest-of (gaps 3899–3998, score-5 isbe-scholarly E entries) | 100 | complete | scripts/bpg-curate-40.py |
| C41 | ephrath;-ephrathah → express (gaps 3999–4098, score-5 isbe-scholarly E entries) | 100 | complete | scripts/bpg-curate-41.py |
| C42 | exquisite → fire-lake-of (gaps 4099–4198, score-5 isbe-scholarly E–F entries) | 100 | complete | scripts/bpg-curate-42.py |
| C43 | fire-strange → frock (gaps 4199–4298, score-5 isbe-scholarly F entries) | 100 | complete | scripts/bpg-curate-43.py |
| C44 | frontier → gilead-mount (gaps 4299–4398, score-5 isbe-scholarly F–G entries) | 100 | complete | scripts/bpg-curate-44.py |
| C45 | gileadites → guide (gaps 4399–4498, score-5 isbe-scholarly G entries) | 100 | complete | scripts/bpg-curate-45.py |
| C46 | guile → healing-gifts-of (gaps 4599–4698, score-5 isbe-scholarly G–H entries) | 100 | complete | scripts/bpg-curate-46.py |
| C47 | health → holy-spirit (gaps 4699–4798, score-5 isbe-scholarly H entries) | 100 | complete | scripts/bpg-curate-47.py |
| C48 | holyday → infanticide (gaps 4799–4898, score-5 isbe-scholarly H–I entries) | 100 | complete | scripts/bpg-curate-48.py |
| C49 | infidel → jacimus (gaps 4899–4998, score-5 isbe-scholarly I–J entries) | 100 | complete | scripts/bpg-curate-49.py |
| C50 | jackal → joadanus (gaps 5099–5198, score-5 isbe-scholarly J entries) | 100 | complete | scripts/bpg-curate-50.py |
| C51 | joannes → kenosis (gaps 5099–5198, score-5 isbe-scholarly J–K entries) | 100 | complete | scripts/bpg-curate-51.py |
| C52 | keras → law-judicial (gaps 5299–5398, score-5 isbe-scholarly K–L entries) | 100 | complete | scripts/bpg-curate-52.py |
| C53 | law-roman → maareh-geba (gaps 5399–5498, score-5 isbe-scholarly L–M entries) | 100 | complete | scripts/bpg-curate-53.py |
| C54 | maasai → marrow (gaps 5499–5598, score-5 isbe-scholarly M entries) | 100 | complete | scripts/bpg-curate-54.py |
| C55 | marsh → midianitish-woman (gaps 5699–5798, score-5 isbe-scholarly M entries) | 100 | complete | scripts/bpg-curate-55.py |
| C56 | midnight → nabataeans (gaps 5699–5803, score-5 isbe-scholarly M–N entries) | 105 | complete | scripts/bpg-curate-56.py |
| C57 | nabathites → noah-2 (gaps 5804–5903, score-5 isbe-scholarly N entries) | 100 | complete | scripts/bpg-curate-57.py |
| C58 | noah-book-apocalypse-of → oreb;-zeeb (gaps 5904–6008, score-5 isbe-scholarly N–O entries) | 105 | complete | scripts/bpg-curate-58.py |
| C59 | ornament → pelishtim (gaps 6009–6108, score-5 isbe-scholarly O–P entries) | 100 | complete | scripts/bpg-curate-59.py |
| C60 | pence;-penny → plagues-of-egypt (gaps 6109–6213, score-5 isbe-scholarly P entries) | 105 | complete | scripts/bpg-curate-60.py |
| C61 | plain-of-moab → prognosticators-monthly (gaps 6214–6313, score-5 isbe-scholarly P entries) | 100 | complete | scripts/bpg-curate-61.py |
| C62 | prologue → rearward (gaps 6314–6418, score-5 isbe-scholarly P–R entries) | 105 | complete | scripts/bpg-curate-62.py |
| C63 | reason;-reasonable;-reasoning → rock-badger (gaps 6419–6523, score-5 isbe-scholarly R entries) | 105 | complete | scripts/bpg-curate-63.py |
| C64 | rod → sanctity-legislation-of (gaps 6524–6628, score-5 isbe-scholarly R–S entries) | 105 | complete | scripts/bpg-curate-64.py |
| C65 | sand → selemias (gaps 6629–6733, score-5 isbe-scholarly S entries) | 105 | complete | scripts/bpg-curate-65.py |
| C66 | seleucidae → shemida;-shemidah;-shemidaites (gaps 6734–6838, score-5 isbe-scholarly S entries) | 105 | complete | scripts/bpg-curate-66.py |
| C67 | shemites → sirach-book-of (gaps 6839–6943, score-5 isbe-scholarly S entries) | 105 | complete | scripts/bpg-curate-67.py |
| C68 | siren → spiritual-songs (gaps 6944–7048, score-5 isbe-scholarly S entries) | 105 | complete | scripts/bpg-curate-68.py |
| C69 | spiritual-man → summer (gaps 7049–7153, score-5 isbe-scholarly S entries) | 105 | complete | scripts/bpg-curate-69.py |
| C70 | summer-house → terah-1 (gaps 7154–7258, score-5 isbe-scholarly S–T entries) | 105 | complete | scripts/bpg-curate-70.py |
| C71 | terah-2 → tower-of-shechem (gaps 7259–7363, score-5 isbe-scholarly T entries) | 105 | complete | scripts/bpg-curate-71.py |
| C72 | tower-of-siloam → uzzen-sheerah (gaps 7364–7468, score-5 isbe-scholarly T–U entries) | 105 | complete | scripts/bpg-curate-72.py |
| C73 | uzziah;-azariah → weight (gaps 7469–7573, score-5 isbe-scholarly U–W entries) | 105 | complete | scripts/bpg-curate-73.py |
| C74 | well-jacobs → zedekiah-2 (gaps 7574–7678, score-5 isbe-scholarly W–Z entries) | 105 | complete | scripts/bpg-curate-74.py |
| C75 | zela-zelah → beth-joab (gaps 7679–7783, score-5 Z + score-3 concept-no-article A–B entries) | 105 | complete | scripts/bpg-curate-75.py |
| C76 | betrayal → creed (gaps 7784–7893, score-3 concept-no-article B–C entries) | 110 | complete | scripts/bpg-curate-76.py |
| C77 | creeping-things → exports (gaps 7894–7998, score-3 concept-no-article C–E entries) | 105 | complete | scripts/bpg-curate-77.py |
| C78 | expostulation → ingathering-feast-of (gaps 7999–8103, score-3 concept-no-article E–I entries) | 105 | complete | scripts/bpg-curate-78.py |
| C79 | ingrafting → mite-a-lepta (gaps 8104–8208, score-3 concept-no-article I–M entries) | 105 | complete | scripts/bpg-curate-79.py |
| C80 | miter → propagation (gaps 8209–8318, score-3 concept-no-article M–P entries) | 110 | complete | scripts/bpg-curate-80.py |
| C81 | prophetesses → zodiac (gaps 8319–8344, score-3 concept-no-article P–Z entries) — FINAL | 226 | complete | scripts/bpg-curate-81.py |

---

## Phase 3: Populate BP Phase 2

Once all curation is done:
1. Count `stub-needed` gaps
2. Group into topic domains (~50 gaps each)
3. Add rows to `BP_PROGRESS.md` Phase 2 Work Queue
4. Mark Phase 3 `complete` here

| Task | Status |
|---|---|
| Count stub-needed gaps | complete — 425 stubs |
| Group into BP Phase 2 units | complete — 9 units (gap-doctrine, gap-persons, gap-ethics, gap-smith-a, gap-smith-b, gap-ot-context, gap-nt-context, gap-isbe-theology, gap-minor) |
| Update BP_PROGRESS.md | complete — Phase 2 Work Queue populated |

---

## Expected gap counts (from pre-run analysis, 2026-06-10)

| Gap type | Estimated count | Notes |
|---|---|---|
| Nave-only topics | ~1,001 | Topics with no dict article |
| Smith-only entries | ~2,038 | In Smith but not Easton |
| ISBE-only entries | ~5,496 | Scholarly entries not in Easton/Smith |
| High-priority stubs expected | ~300–500 | After curation |

Top 15 highest-priority gaps (by Nave verse count):

| Term | Nave Verses | Gap Type | Expected Status |
|---|---|---|---|
| Jesus, the Christ | 2471 | doctrine | stub-needed |
| Afflictions and Adversities | 862 | practice | stub-needed |
| Minister, Christian | 846 | doctrine | stub-needed |
| Wicked (People) | 761 | concept | stub-needed |
| Righteous | 560 | concept | stub-needed |
| Zeal, Religious | 417 | virtue | stub-needed |
| Israel, Prophecies Concerning | 361 | prophetic | stub-needed |
| Obedience | 295 | virtue | stub-needed |
| Backsliders | 256 | concept | stub-needed |
| Thankfulness | 240 | virtue | stub-needed |
| Angel (a Spirit) | 237 | concept | probably in Easton as "Angel" — verify |
| Hypocrisy | 224 | concept | stub-needed |
| Commandments | 212 | doctrine | stub-needed |
| Pride | 202 | vice | stub-needed |
| Judgment | 154 | doctrine | stub-needed |
