"""
Book Study Data — Romans
book_id: romans
lang: greek
author_group: Paul

Run: python3 scripts/build-book-study-romans.py

Notes:
- Vocabulary selected from top Paul-peaked Greek words; filtered to those with
  specific load in Romans' argument (justification, sin, law, Spirit, faith).
- language_notes focuses on three features distinctive to Romans: diatribe
  structure, Paul's dense particle use (gamma/oun rhythm), and the γεγ- perfect
  tense theology in chs 3-5.
- reception highlights Augustine (sin/grace), Luther (sola fide catalyst),
  Barth (Romans commentary as theological earthquake).
"""

import json, os

# ── boilerplate ──────────────────────────────────────────────────────────────

def load_book_study(book_id):
    path = f'data/workshop/book-study/{book_id}.json'
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

def save_book_study(book_id, data):
    os.makedirs('data/workshop/book-study', exist_ok=True)
    path = f'data/workshop/book-study/{book_id}.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'wrote {path} ({len(data.get("key_vocabulary", []))} vocab entries)')

def merge_book_study(existing, new_data):
    """Fill only fields not already present. Safe to re-run."""
    result = dict(existing)
    for key, val in new_data.items():
        if key not in result or not result[key]:
            result[key] = val
    return result

# ── content ──────────────────────────────────────────────────────────────────

BOOK_STUDY = {
    "bookId": "romans",

    "key_vocabulary": [
        {
            "code": "G1343",
            "lemma": "δικαιοσύνη",
            "translit": "dikaiosynē",
            "gloss": "righteousness",
            "significance": "Romans uses this word 33 times — Paul's highest concentration anywhere in his letters. In Romans the word is consistently forensic: it names what God declares over the believer, not a moral quality the believer develops. Understanding it as a courtroom verdict rather than a character trait transforms how chapters 3–5 read."
        },
        {
            "code": "G3551",
            "lemma": "νόμος",
            "translit": "nomos",
            "gloss": "law",
            "significance": "Appears 74 times in Romans — more than in any other book of the Bible. Paul uses it in at least four distinct senses: the Mosaic Torah, a principle or pattern, the law written on Gentile hearts, and the 'law of Christ' or Spirit. Tracking which sense Paul intends in each clause is the key hermeneutical task of chs 2–8."
        },
        {
            "code": "G4102",
            "lemma": "πίστις",
            "translit": "pistis",
            "gloss": "faith",
            "significance": "The single most contested word in Romans. Three interpretive options for πίστις Χριστοῦ (3:22, 3:26): (1) faith placed in Christ (objective genitive — majority view), (2) Christ's own faithfulness/obedience (subjective genitive — Hays, Wright), (3) both simultaneously. The stakes are significant: the subjective reading makes Christ the primary agent of justification, the objective reading emphasizes human response. Romans 3:22–26 is the crux passage."
        },
        {
            "code": "G3056",
            "lemma": "λόγος",
            "translit": "logos",
            "gloss": "word",
            "significance": "In Romans, Paul uses λόγος specifically for the proclaimed gospel word (1:2, 9:6, 10:17). The phrase 'the word of God has not failed' (9:6) is the hinge of chs 9–11. Paul's argument that Israel's unbelief does not nullify God's λόγος holds together the entire theodicy section."
        },
        {
            "code": "G4561",
            "lemma": "σάρξ",
            "translit": "sarx",
            "gloss": "flesh",
            "significance": "Paul uses σάρξ in two registers in Romans that English 'flesh' collapses: (1) ethnic/genealogical descent ('descended from Abraham according to the flesh,' 1:3, 4:1, 9:3), and (2) the sinful disposition of the unregenerate person (7:5, 8:3–8). Chapters 7–8 make no sense without tracking which register is active in each verse."
        },
        {
            "code": "G4151",
            "lemma": "πνεῦμα",
            "translit": "pneuma",
            "gloss": "Spirit",
            "significance": "Romans 8 is the densest concentration of Spirit-language in the NT (21 occurrences in 39 verses). Crucially, Paul moves from 'Spirit of God' to 'Spirit of Christ' to 'Christ in you' in 8:9–10, treating them as interchangeable — one of the strongest Pauline bases for the Trinity. The Spirit's role in groaning intercession (8:26–27) is unique to Romans."
        },
        {
            "code": "G266",
            "lemma": "ἁμαρτία",
            "translit": "hamartia",
            "gloss": "sin",
            "significance": "Paul personifies sin as a ruling power (5:12–21) using language that would apply to a tyrant or slave-master. This is not rhetorical decoration — Paul's entire argument in chs 6–7 depends on sin being a dominion that enslaves, not merely a list of wrong acts. 'Sin reigned' (5:21), 'sin shall not have dominion' (6:14), 'freed from sin' (6:22) are the key structural markers."
        },
        {
            "code": "G1342",
            "lemma": "δίκαιος",
            "translit": "dikaios",
            "gloss": "righteous",
            "significance": "The adjective from the same root as δικαιοσύνη, used in 1:17's citation of Habakkuk 2:4 ('the righteous shall live by faith') — the thesis verse of the entire letter. The LXX and MT of Hab 2:4 are slightly different, and Paul's use of the LXX form changes the emphasis from God's faithfulness (MT) to human faith (LXX). This citation is the exegetical key to Romans 1–4."
        },
        {
            "code": "G1347",
            "lemma": "δικαίωσις",
            "translit": "dikaiōsis",
            "gloss": "justification",
            "significance": "Appears only twice in the NT, both in Romans (4:25 and 5:18). The noun form of the act of declaring righteous — more dynamic than δικαιοσύνη. Romans 4:25 is one of the most compact soteriological statements in the Bible: 'delivered for our trespasses and raised for our justification.' The resurrection is here presented as the ground of justification, not merely its proof."
        },
        {
            "code": "G2596",
            "lemma": "κατά",
            "translit": "kata",
            "gloss": "according to",
            "significance": "A small preposition that carries enormous theological weight in Romans. 'According to the flesh' vs 'according to the Spirit' is the fundamental antithesis of chs 8. 'According to the works of the law' vs 'according to grace' (4:4, 11:6) is the justification antithesis. Every κατά phrase in Romans signals which realm or principle Paul is invoking."
        },
        {
            "code": "G3771",
            "lemma": "οὖν",
            "translit": "oun",
            "gloss": "therefore",
            "significance": "The most important single word for tracking Paul's argument structure in Romans. Every οὖν draws an inference from the preceding theological claim and launches the next section. 'Therefore, there is now no condemnation' (8:1) concludes the entire argument of chs 1–7. 'Therefore I urge you' (12:1) pivots from doctrine to ethics. The placement of each οὖν is an outline in miniature."
        },
        {
            "code": "G1063",
            "lemma": "γάρ",
            "translit": "gar",
            "gloss": "for",
            "significance": "Paul uses γάρ (ground/reason) 147 times in Romans — one of the highest densities in the NT. Nearly every theological claim is immediately grounded: 'I am not ashamed of the gospel, <em>for</em> it is the power of God.' Reading each γάρ as a load-bearing reason rather than a loose connective reveals the density of Paul's argument and prevents surface-level interpretations."
        },
        {
            "code": "G1344",
            "lemma": "δικαιόω",
            "translit": "dikaioō",
            "gloss": "justify",
            "significance": "The verb 'to justify' appears 15 times in Romans, always in the sense of a judicial declaration — God pronouncing a verdict of 'not guilty / in the right.' The Hiphil analogue in Hebrew (הִצְדִּיק) confirms the forensic register: it never means 'make righteous' but always 'declare righteous.' This distinction is the hinge of Reformation-era debates and remains central to modern exegesis."
        },
        {
            "code": "G2222",
            "lemma": "ζωή",
            "translit": "zōē",
            "gloss": "life",
            "significance": "Romans pairs life and death as the two dominions (5:12–21, 6:23, 8:2, 8:6). ζωή αἰώνιος ('eternal life') is used in Romans (2:7, 5:21, 6:22–23) to mean not endless duration but the life of the age to come — the resurrection order that Christ inaugurated. Death reigned (5:14, 5:17); through Christ, life reigns instead."
        },
        {
            "code": "G5485",
            "lemma": "χάρις",
            "translit": "charis",
            "gloss": "grace",
            "significance": "Used 24 times in Romans, always against the backdrop of the patron-client social world. Grace is God's unconditional benefaction that creates loyalty not through obligation but through the gift of righteousness itself. Romans 11:6 makes the antithesis absolute: 'If by grace, it is no longer by works; otherwise grace is no longer grace.' The entire letter is an argument for why grace cannot be mixed with works-merit without destroying the grace."
        }
    ],

    "language_notes": (
        "<p>Romans is written in Paul's most formal and sustained Greek. Three features of the original language are essential for reading it well. First, Paul uses the <strong>diatribe</strong> — a rhetorical device where an imaginary interlocutor raises objections that Paul then demolishes. Phrases like 'What then shall we say?' (3:5, 6:1, 7:7, 9:14) and 'By no means!' (μὴ γένοιτο — 3:4, 6, 3:31, 6:2, 7:7) are diatribe markers, not genuine dialogue. Recognizing the diatribe prevents reading the rhetorical questions as Paul's own doubts rather than as foils for his argument.</p>"
        "<p>Second, Paul's argument is carried by <strong>discourse particles</strong>. The γάρ / οὖν rhythm is nearly musical: γάρ grounds every major claim ('for the righteousness of God is revealed'), and οὖν draws the inference that launches the next section ('therefore, there is now no condemnation'). Reading Romans without tracking these particles is like reading sheet music without the time signature — the notes are there but the structure is invisible.</p>"
        "<p>Third, Paul uses the Greek <strong>perfect tense</strong> with precision in chs 3–5 to argue that the justification accomplished in the past has permanent present standing. 'It has been credited' (λελόγισται, 4:3, 4:23) — the Abrahamic precedent stands and is still standing. 'We have been justified' (δεδικαιωμένοι, 5:1) — this is a completed action whose effects are currently in force. English simple past ('it was credited') loses the present-ongoing force that perfect tense carries.</p>"
        "<p>A fourth feature specific to Romans 9–11: Paul quotes the LXX (Greek OT) rather than the Hebrew MT in several places where the texts differ. In 9:33 and 10:11 he combines Isa 28:16 and Isa 8:14 in a way only possible if working with the LXX text. Knowing which version Paul is citing — and why — resolves several apparent interpretive difficulties in the theodicy argument.</p>"
    ),

    "reception": (
        "<p><strong>Patristic:</strong> Augustine's reading of Romans 5:12 ('in whom all sinned') became the western doctrine of original sin — a reading shaped by the Latin translation 'in quo' (in whom, i.e., Adam) rather than the Greek ἐφ᾽ ᾧ (because, or on the basis that). Chrysostom, working from the Greek, emphasized human responsibility more than inherited guilt. The East-West divergence on original sin traces largely to this verse.</p>"
        "<p><strong>Reformation:</strong> Luther's tower experience — reading Romans 1:17 and finally grasping that 'the righteousness of God' is what God <em>gives</em> rather than what God <em>demands</em> — is the origin point of the Protestant Reformation. His 1515–16 lectures on Romans remain one of the most influential pieces of biblical exposition in Christian history. Calvin's commentary (1540) is the most thorough exegetical treatment from the Reformation period and repays careful study.</p>"
        "<p><strong>Modern debates:</strong> E.P. Sanders' <em>Paul and Palestinian Judaism</em> (1977) launched the New Perspective on Paul by arguing that Paul misrepresented Judaism as works-righteousness. N.T. Wright and James Dunn developed this into a reading where Paul's target is 'works of the law' as ethnic boundary markers (circumcision, food laws, calendar) rather than merit-based soteriology. The Traditional Perspective (Tom Schreiner, John Piper) argues Paul's concern is broader: any human contribution to justification, not just ethnic markers. Romans remains the primary battleground for this dispute.</p>"
    ),

    "reading_guide": (
        "<p>The single most important preparation before reading Romans: understand that Paul is writing to a mixed Jewish-Gentile congregation in Rome experiencing ethnic tension (the Edict of Claudius expelled Jews from Rome c. AD 49; they returned to find Gentile Christians in charge). Much of Romans 9–11 and 14–15 is addressing this concrete pastoral situation, not merely rehearsing abstract theology.</p>"
        "<p>As you read verse by verse, track two things: (1) every γάρ and οὖν — they map the argument; (2) which sense of νόμος (law) Paul is using in each clause. When you hit a puzzling statement, ask 'which law is he talking about?' before reaching for a theological category.</p>"
        "<p>The most common misreading: treating Romans 7 as Paul's description of normal Christian experience ('I do what I do not want to do'). Read the verbs in past tense ('I <em>was</em> sold under sin') and notice the absence of the Spirit until ch. 8 — Paul is describing the law-era situation, not the normal post-resurrection Christian life. Romans 8 is the answer to Romans 7, not a continued problem.</p>"
        "<p>If approaching Romans for the first time, start with 1:1–17 (thesis), then jump to 3:21–31 (the heart of the gospel), then 8:1–39 (the Spirit-life of the justified), then circle back to fill in the argument of 1:18–3:20 and 5–7. The soteriological core is clearer if you see the destination before you trace the full argument.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('romans')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('romans', merged)

main()
