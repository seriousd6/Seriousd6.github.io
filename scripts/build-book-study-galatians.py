"""
Book Study Data — Galatians
book_id: galatians
lang: greek

Run: python3 scripts/build-book-study-galatians.py

Notes:
- Key vocabulary selected from Paul author group peaks plus Galatians-specific terms
- Galatians is the Magna Carta of Christian liberty; vocabulary centers on justification,
  the law/faith antithesis, and freedom
- πίστις Χριστοῦ (2:16; 2:20; 3:22) carries the contested 'faith of/in Christ' ambiguity
- G3807 παιδαγωγός is the ancient guardian-slave, not a schoolteacher (mistranslation alert)
"""

import json, os, sys

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
    "bookId": "galatians",

    "key_vocabulary": [
        {
            "code": "G331",
            "lemma": "ἀνάθεμα",
            "translit": "anathema",
            "gloss": "accursed",
            "significance": "The letter opens not with the usual thanksgiving but with ἀνάθεμα — 'let him be accursed' — pronounced twice in 1:8–9 against anyone who preaches a different gospel. The word denotes something placed under divine ban, devoted to destruction (cf. the LXX use for the Hebrew חֵרֶם). Paul applies it without hesitation even to himself hypothetically ('even if we or an angel from heaven'). This double curse in the salutation signals that Paul regards the Judaizers' teaching as not merely wrong but as a fundamental corruption of the gospel that calls down divine judgment."
        },
        {
            "code": "G2098",
            "lemma": "εὐαγγέλιον",
            "translit": "euangelion",
            "gloss": "gospel",
            "significance": "In Galatians, εὐαγγέλιον is not primarily a message-category but an exclusive referent: there is only one genuine gospel, and anything that adds to it 'perverts' it (1:7). Paul insists he received his εὐαγγέλιον 'through a revelation of Jesus Christ' (1:12) — not from human tradition — precisely because his opponents questioned his authority by questioning his apostolic pedigree. The stakes of the argument are what makes Galatians unique: if the Judaizers are right, the εὐαγγέλιον Paul preached from the beginning was incomplete, and every Gentile church he planted rests on an insufficient foundation."
        },
        {
            "code": "G1344",
            "lemma": "δικαιόω",
            "translit": "dikaioō",
            "gloss": "justify",
            "significance": "The verb δικαιόω (to declare/render righteous, to justify) is the theological engine of Galatians. The key statement appears three times in 2:16: 'a person is not justified by works of the law but through faith in Jesus Christ.' The verb is forensic — a court declaration of standing, not a moral improvement. Galatians introduces the debate that Paul expands in Romans: whether covenant membership and right standing before God come through Torah observance (the Judaizers' position) or through the faithfulness of Christ received by faith. On this question Paul admits no middle ground."
        },
        {
            "code": "G4102",
            "lemma": "πίστις",
            "translit": "pistis",
            "gloss": "faith",
            "significance": "πίστις appears ~22 times in Galatians and carries a debated genitive construction at 2:16, 2:20, and 3:22: πίστις Χριστοῦ, which can be read as 'faith in Christ' (subjective genitive: the believer's faith) or 'the faithfulness of Christ' (objective genitive: Christ's own faithful obedience). If the latter, Paul's argument is that justification rests on Christ's covenantal faithfulness, not the believer's act of believing — a distinction with theological weight. In either reading, πίστις is the antithesis of the 'works of the law' that Paul rejects as the basis for covenant standing."
        },
        {
            "code": "G3551",
            "lemma": "νόμος",
            "translit": "nomos",
            "gloss": "law",
            "significance": "νόμος appears approximately 32 times in Galatians — more per verse than in Romans. Paul's argument is not that the Torah was evil ('Is the law then against the promises of God? Certainly not!', 3:21) but that it served a bounded, preparatory function. The phrase 'works of the law' (ἔργα νόμου, 2:16; 3:2, 5, 10) may specifically refer to Torah boundary-markers (circumcision, food laws, calendar) that distinguished Jew from Gentile — the practices the Judaizers were requiring of Gentile converts. Paul's 'freedom from the law' is freedom from the law as a system of boundary-maintenance, not freedom from moral accountability."
        },
        {
            "code": "G4061",
            "lemma": "περιτομή",
            "translit": "peritomē",
            "gloss": "circumcision",
            "significance": "περιτομή is the presenting crisis that provoked the letter. In Second Temple Judaism, circumcision was the covenant-entry rite for male Gentile converts who wished to become full members of the Jewish community. The Judaizers were requiring it of Gentile believers in Christ, implying that faith in Christ alone was insufficient for full covenant standing. Paul's response is radical: if you accept circumcision as necessary for salvation, 'Christ will be of no advantage to you' (5:2), because circumcision signals commitment to the whole system of Torah observance — you 'are severed from Christ' (5:4). The stakes are all-or-nothing."
        },
        {
            "code": "G1657",
            "lemma": "ἐλευθερία",
            "translit": "eleutheria",
            "gloss": "freedom",
            "significance": "ἐλευθερία is the positive counterpart to the law's bondage. 'For freedom Christ has set us free; stand firm therefore, and do not submit again to a yoke of slavery' (5:1) is the practical summary of the entire letter. The freedom Paul describes is not moral autonomy — he immediately qualifies it: 'do not use your freedom as an opportunity for the flesh, but through love serve one another' (5:13). The freedom is freedom from the law as a system of covenantal boundary-maintenance and condemnation, exercised within the community of love governed by the Spirit."
        },
        {
            "code": "G2671",
            "lemma": "κατάρα",
            "translit": "katara",
            "gloss": "curse",
            "significance": "κατάρα appears at 3:10 and 3:13, forming the theological heart of Paul's argument. In 3:10 he cites Deuteronomy 27:26: ‘Cursed is everyone who does not abide by all things written in the Book of the Law.’ The law, rather than providing blessing, pronounces a curse on the one who fails to keep it completely. Paul’s solution in 3:13 is the substitutionary exchange: ‘Christ redeemed us from the curse of the law by becoming a curse for us — for it is written, Cursed is everyone who is hanged on a tree’ (Deut 21:23). The cross is the place where the law’s curse is absorbed and exhausted."
        },
        {
            "code": "G1860",
            "lemma": "ἐπαγγελία",
            "translit": "epangelia",
            "gloss": "promise",
            "significance": "ἐπαγγελία (promise) appears ~10 times in Galatians and is the positive alternative to the law as the basis for covenant membership. Paul's argument in chapter 3 is chronological: Abraham believed God and it was counted as righteousness (Gen 15:6) — 430 years before the Mosaic law. The law cannot annul a prior covenant or promise (3:17). Therefore the inheritance comes through the ἐπαγγελία to Abraham, and those who belong to Christ are 'Abraham's offspring, heirs according to promise' (3:29). The promise is the eschatological category; the law is the interim administration that served until Christ came."
        },
        {
            "code": "G3807",
            "lemma": "παιδαγωγός",
            "translit": "paidagōgos",
            "gloss": "guardian",
            "significance": "παιδαγωγός is regularly mistranslated 'schoolmaster' or 'tutor,' suggesting the law teaches us something we carry forward. The Greco-Roman παιδαγωγός was a household slave assigned to escort a child to school and back — responsible for keeping the child safe and obedient, but not actually teaching. The role ended when the child became an adult heir. Paul's point in 3:24–25 is precisely this temporal limitation: 'the law was our παιδαγωγός until Christ came, in order that we might be justified by faith. But now that faith has come, we are no longer under a παιδαγωγός.' The law did not teach what faith teaches — it escorted Israel to the point of receiving it."
        },
        {
            "code": "G5207",
            "lemma": "υἱός",
            "translit": "huios",
            "gloss": "son",
            "significance": "υἱός in Galatians is the status-word that the law and the ἐπαγγελία both point toward. 'You are all sons of God through faith in Christ Jesus' (3:26) is the destination of Paul's entire argument: adoption as adult sons with full inheritance rights. In 4:1–7 Paul develops the metaphor: under the law, the heir is 'no different from a slave' until the appointed time. The Spirit of God's Son sent into believers' hearts cries 'Abba, Father' (4:6) — the intimacy of sonship rather than the fear of slavery. The υἱός language also connects to Christ as the singular 'seed' (σπέρμα) of Abraham in whom all nations are blessed."
        },
        {
            "code": "G2818",
            "lemma": "κληρονόμος",
            "translit": "klēronómos",
            "gloss": "heir",
            "significance": "κληρονόμος (heir) in chapters 3–4 ties together the promise, sonship, and inheritance arguments. If believers are Abraham's seed through Christ (3:29), they are κληρονόμοι of the promise — legal heirs, not servants or slaves. Paul's contrast in 4:7 is the climax: 'You are no longer a slave but a son, and if a son, then an heir through God.' The Judaizers' requirement of Torah observance is, in Paul's frame, a demand to return to the 'elementary principles' of the world (4:3, 9) — to trade the status of heir for that of slave. The inheritance language connects the Christian's eschatological hope to the Abrahamic covenant."
        },
        {
            "code": "G4561",
            "lemma": "σάρξ",
            "translit": "sarx",
            "gloss": "flesh",
            "significance": "σάρξ in Galatians operates on two levels that must be distinguished. In chapters 1–4 it refers to the physical realm of circumcision and ethnic identity: 'in the flesh' means the domain of the Judaizers' boundary-markers. In chapters 5–6 it shifts to the moral domain: the 'works of the flesh' (5:19–21) are the expressions of the self-directed will that stands in opposition to the Spirit. The two uses reinforce each other: to require 'fleshly' boundary-markers (circumcision) is to operate in the realm of the σάρξ in both senses — the physical and the spiritual. Paul's ethic in chapter 5 is to 'walk by the Spirit' rather than gratify the desires of the σάρξ."
        },
        {
            "code": "G2590",
            "lemma": "καρπός",
            "translit": "karpos",
            "gloss": "fruit",
            "significance": "The 'fruit of the Spirit' (5:22–23) is a deliberately organic metaphor: καρπός is not produced by effort but grows from a living source. The list — love, joy, peace, patience, kindness, goodness, faithfulness, gentleness, self-control — is offered in deliberate contrast to the 'works' (ἔργα) of the flesh. The asymmetry is intentional: the flesh produces 'works' (striving, effort, production), while the Spirit produces 'fruit' (organic growth from union with Christ). Against such fruit 'there is no law' (5:23) — the law finds nothing to condemn in what the Spirit grows, because the law's purpose is to restrain the flesh, not the Spirit."
        }
    ],

    "language_notes": (
        "<p>Galatians is the only Pauline letter that lacks an opening thanksgiving. Paul moves directly from salutation to rebuke: 'I am astonished that you are so quickly deserting him who called you' (1:6). The absence of thanksgiving is a deliberate rhetorical signal — in ancient letter conventions, the thanksgiving oriented the recipients toward the letter's main purpose and established goodwill. Its omission signals urgency and alarm. This is not generic unfriendliness but a carefully calculated break from convention that alerts the reader: this letter is unlike the others.</p>"
        "<p>The phrase <strong>ἔργα νόμου</strong> ('works of the law,' 2:16; 3:2, 5, 10) has been extensively debated since the discovery of the Dead Sea Scrolls, where the Hebrew equivalent (מַעֲשֵׂי הַתּוֹרָה, <em>ma'aseh ha-Torah</em>) appears in a legal context. Some scholars argue Paul means specifically the Torah's identity-boundary markers — circumcision, food laws, Sabbath — not law-keeping in general. Others read it as any system of achieving merit before God through observance. The narrower reading would make the opponents' demand for circumcision the specific 'work of the law' that Paul is refuting; the broader reading would encompass any works-based approach to covenant standing.</p>"
        "<p>The <strong>πίστις Χριστοῦ</strong> construction (2:16, 20; 3:22) is one of the most contested grammatical questions in NT Greek. The genitive Χριστοῦ (of Christ) can be subjective ('the faithfulness that Christ exercised') or objective ('faith directed toward Christ'). Most English translations choose objective ('faith in Christ'), but a growing scholarly consensus reads it as subjective — Christ's own covenantal faithfulness — which would shift the ground of justification from the believer's act of faith to Christ's faithful obedience. Both readings are grammatically defensible; the interpretive choice affects whether faith is primarily the human act of reception or the prior divine act of Christ's obedience.</p>"
        "<p>Chapter 3's argument from <strong>σπέρμα</strong> (seed/offspring) in 3:16 depends on a subtle reading of Genesis 22:18 LXX: 'in your seed (σπέρματι) shall all the nations be blessed.' Paul argues that σπέρμα is singular — 'seed,' not 'seeds' — and therefore refers specifically to Christ, not to Abraham's collective descendants. This is a rabbinic-style pesher argument from the number of a noun. Modern readers may find it strained; for Paul's audience, trained in midrashic interpretation, the close reading of a single word's grammatical number was a recognized and respected hermeneutical move.</p>"
    ),

    "reception": (
        "<p><strong>Patristic:</strong> Galatians was the most contested of Paul's letters in the early church because its antithesis of law and gospel raised urgent questions about the Hebrew scriptures' continuing validity. Marcion used Galatians as his primary Pauline text to argue that the God of the OT was a different, inferior deity — a reading the orthodox Fathers strenuously rejected. Chrysostom and Augustine both wrote on Galatians, but their interpretations diverged sharply: Augustine's reading in his early commentary was more synergistic (faith plus works); his later work (post-Pelagian controversy) emphasized grace alone, moving him closer to what Luther would later call the 'true' Galatians.</p>"
        "<p><strong>Reformation:</strong> Luther called Galatians 'my own epistle' and wrote the most influential Reformation commentary on it (1535), identifying Paul's Judaizers with medieval Catholic teachings on meritorious works. His reading of the law/gospel antithesis — law kills, gospel gives life; law convicts, gospel justifies — became the structural principle of Lutheran theology. Calvin's commentary (1548) agreed on justification by faith but read the law more positively: not merely a judge but also a guide for Christian living. The Luther/Calvin divergence on the 'third use of the law' (law as guide for the Christian) traces directly to their different readings of Galatians 3–5.</p>"
        "<p><strong>Modern debates:</strong> The 'New Perspective on Paul' (E. P. Sanders, James Dunn, N. T. Wright, from the 1970s onward) has transformed the reading of Galatians. Sanders argued that Second Temple Judaism was not a religion of merit-earning works-righteousness — Jews understood they were in the covenant by grace and stayed in it by obedience. Dunn and Wright followed by arguing that Paul's 'works of the law' targeted the social boundary-markers that separated Jew from Gentile (circumcision, food laws), not a general moralism. Critics of the New Perspective argue this narrows Paul's argument too much. The debate remains active and has generated an enormous secondary literature.</p>"
    ),

    "reading_guide": (
        "<p>Galatians rewards reading in a single sitting — it is short enough (6 chapters) and emotionally intense enough that its argument builds on itself. Before reading, understand the presenting issue: teachers have told the Galatians that faith in Christ is not enough — they must also be circumcised and keep the Torah to be fully God's people. Paul's entire letter is a response to this one claim. Every argument, every illustration, every emotional appeal serves this single polemical purpose.</p>"
        "<p>Track two pairs of contrasts as you read: <strong>faith versus works of the law</strong> (the justification argument, chapters 1–4) and <strong>Spirit versus flesh</strong> (the ethical argument, chapters 5–6). These are not separate topics — Paul's point is that the same grace that justifies by faith also produces the fruit of the Spirit. The Judaizers who require circumcision are attempting to perfect by the flesh what was begun by the Spirit (3:3). The ethical section of chapters 5–6 is therefore the completion of the theological argument, not a new topic.</p>"
        "<p>The most common misreading of Galatians is hearing Paul say that rules and structure are bad for Christians. He says nothing of the kind. What he opposes is using Torah observance as the basis for <em>covenant standing before God</em> — the ground of justification. He explicitly commends fulfilling 'the law of Christ' through bearing one another's burdens (6:2) and says that love fulfills the whole law (5:14). Watch for how he ends the letter in his own handwriting (6:11–18): the cross is the only ground for boasting, and 'the Israel of God' is the new community in Christ.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('galatians')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('galatians', merged)

main()
