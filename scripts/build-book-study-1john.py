"""
Book Study Data — 1 John
book_id: 1john
lang: greek

Run: python3 scripts/build-book-study-1john.py

Notes:
- Author group: John (peak in author-freq-greek.json)
- 12 vocab entries
- Structure is a spiral, not linear: same themes (light/darkness, love/hate, truth/lie,
  commandment/sin) revisited and deepened across three cycles
- ἀντίχριστος (2:18, 22; 4:3) appears to be a Johannine coinage — 4 of 5 NT uses in 1-2 John
- ἱλασμός (2:2; 4:10) appears only twice in the NT, both in 1 John
- μένω ('abide') concentrates uniquely in the Johannine corpus — 24 of ~118 NT uses in 1 John
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
    "bookId": "1john",

    "key_vocabulary": [
        {
            "code": "G25",
            "lemma": "ἀγαπάω",
            "translit": "agapáō",
            "gloss": "love",
            "significance": "ἀγαπάω ('to love with moral commitment and self-giving') is the governing verb of 1 John, appearing 28 times in 5 chapters — the highest density of any NT book. The love 1 John commands and describes is consistently grounded in divine initiative: 'We love because he first loved us' (4:19). John never calls the community to love each other on the basis of the other person's lovableness but on the basis of what God has done: 'this is love: not that we loved God, but that he loved us' (4:10). The verb also appears in the negative warning: 'do not love the world or the things in the world' (2:15) — love directed wrongly at the wrong object is idolatry. ἀγαπάω in 1 John is not sentiment but orientation: whom you love defines you."
        },
        {
            "code": "G26",
            "lemma": "ἀγάπη",
            "translit": "agápē",
            "gloss": "love",
            "significance": "ἀγάπη (the noun 'love') makes 1 John's most compressed and audacious theological claim: <em>ὁ θεὸς ἀγάπη ἐστίν</em> — 'God is love' (4:8, 16). This is not an analogy ('God is like love') or an attribute ('God has love') but an identity statement. Love is not a quality God happens to have; it is what God is. The statement must be held alongside the equally unqualified 'God is light' (1:5) — 1 John does not collapse God into love and ignore his holiness; both declarations are equally fundamental. The practical implication is reciprocal: 'whoever abides in love abides in God, and God abides in him' (4:16). The community's mutual love is not merely a social virtue; it is the site where God himself is present and dwells."
        },
        {
            "code": "G3306",
            "lemma": "μένω",
            "translit": "ménō",
            "gloss": "abide",
            "significance": "μένω ('to remain, stay, abide, dwell') is the Johannine distinctive for the Christian's relational union with God. Of the NT's approximately 118 uses of μένω, 24 appear in 1 John alone — an extraordinary concentration. The word frames the Christian life as a sustained dwelling rather than an episodic connection: 'abide in him, so that when he appears we may have confidence' (2:28); 'whoever keeps his commandments abides in God, and God in him' (3:24); 'God is love, and whoever abides in love abides in God, and God abides in him' (4:16). The mutuality — God abiding in the believer, the believer abiding in God — is uniquely Johannine. μένω answers the question: what does an ongoing relationship with God look like? It looks like abiding — dwelling, remaining, not departing."
        },
        {
            "code": "G2434",
            "lemma": "ἱλασμός",
            "translit": "hilasmós",
            "gloss": "propitiation",
            "significance": "ἱλασμός ('propitiation, atoning sacrifice, means of expiation') appears only twice in the NT, and both occurrences are in 1 John — 2:2 and 4:10. The word describes an act that averts divine wrath by satisfying the conditions of justice: 'He is the propitiation for our sins, and not for ours only but also for the sins of the whole world' (2:2). Translators debate 'propitiation' (which includes wrath-averting) vs. 'expiation' (which emphasizes sin-removing) — the Greek word carries both senses, but the surrounding context of divine holiness and human sin in 1 John supports the fuller reading. In 4:10, the word appears in 1 John's most concentrated love statement: 'this is love, not that we have loved God but that he loved us and sent his Son to be the propitiation for our sins.' The ἱλασμός is both the measure of God's love and the ground of the community's assurance."
        },
        {
            "code": "G500",
            "lemma": "ἀντίχριστος",
            "translit": "antíchristos",
            "gloss": "antichrist",
            "significance": "ἀντίχριστος ('opponent of Christ, antichrist') appears to be a Johannine coinage — 4 of its 5 NT occurrences are in 1-2 John (1 John 2:18, 22; 4:3; 2 John 7). The word joins ἀντί ('against, in place of') and Χριστός to describe a figure who either opposes or counterfeit-replaces the true Christ. John's use is striking: the antichrist is not a future apocalyptic figure but a present reality embodied by the secessionists — 'even now many antichrists have come' (2:18). The test for the spirit of antichrist is doctrinal: 'every spirit that does not confess Jesus is not from God — this is the spirit of the antichrist' (4:3). The plural ('many antichrists') shows John is not primarily describing an individual end-times figure but a spirit — a theological orientation that denies Christ's true identity — that can be embodied by anyone. The term he coins gives the church precise vocabulary for this danger."
        },
        {
            "code": "G2222",
            "lemma": "ζωή",
            "translit": "zōḗ",
            "gloss": "life",
            "significance": "ζωή ('life, especially divine/eternal life') appears 13 times in 1 John — more than any other NT letter — and frames the entire document. The prologue declares Jesus the 'word of life' (1:1) and the 'eternal life which was with the Father and was made manifest to us' (1:2). The letter's explicit purpose statement (5:13) reveals why: 'I write these things to you who believe in the name of the Son of God, that you may know that you have eternal life.' The letter is an assurance document — it wants believers to <em>know</em> they possess eternal life now, not merely hope they will eventually. The false teachers apparently claimed a superior spiritual life while failing John's three tests; John insists that genuine eternal life is visible in righteousness, love, and right belief — not in claims to spiritual elevation."
        },
        {
            "code": "G3670",
            "lemma": "ὁμολογέω",
            "translit": "homologéō",
            "gloss": "confess",
            "significance": "ὁμολογέω ('to agree, confess, acknowledge publicly') carries two distinct confessional weights in 1 John. In 1:9, it is the ongoing confession of sin that opens access to forgiveness: 'if we confess our sins, he is faithful and just to forgive us our sins and to cleanse us from all unrighteousness.' In 4:2-3, it is the christological confession that separates truth from error: 'every spirit that confesses that Jesus Christ has come in the flesh is from God.' These two confessions — of sin and of Christ — define the community. The false teachers apparently failed at both: they claimed to be without sin (1:8, 10) and they denied the full humanity of Jesus (4:2). The word's legal background ('to speak the same as' — to agree with what is true) gives it weight: confession is not merely reciting a formula but publicly aligning with what is actually the case."
        },
        {
            "code": "G266",
            "lemma": "ἁμαρτία",
            "translit": "hamartía",
            "gloss": "sin",
            "significance": "ἁμαρτία ('sin, missing the mark, violation of God's will') appears 17 times in 5 chapters, making it one of 1 John's most frequent substantive terms. The letter holds two affirmations in tension that have puzzled interpreters. First: 'if we say we have no sin, we deceive ourselves' (1:8) — believers sin, and pretending otherwise is self-deception. Second: 'whoever abides in him does not sin' (3:6); 'no one born of God makes a practice of sinning' (3:9). The resolution: 1:8 speaks of the ongoing reality that believers sin and need the Advocate (2:1); 3:6-9 speaks of the direction of a transformed life — not habitual, willful, unrepentant sin as a pattern. The false teachers apparently claimed sinlessness (a proto-Gnostic position: the spirit is pure regardless of bodily acts); John's corrective refuses both their antinomian sinlessness and any perfectionism that denies ordinary ongoing need for forgiveness."
        },
        {
            "code": "G2889",
            "lemma": "κόσμος",
            "translit": "kósmos",
            "gloss": "world",
            "significance": "κόσμος ('world, ordered universe, humanity, the present age in opposition to God') appears 23 times in 1 John in its characteristic Johannine sense — the world as the realm of opposition to God and his people: 'do not love the world or the things in the world' (2:15); 'we know that we are from God, and the whole world lies in the power of the evil one' (5:19). But John also holds the world as the object of God's transforming love: 'God sent his Son into the world' (4:9) and Christ 'is the propitiation for our sins, and not for ours only but also for the sins of the whole world' (2:2). These are not contradictory uses: in John's theology, the same world that is estranged from God is the world God moves toward in love. The community is not to love the world (as a value system) but to know that God loves the world (as a people)."
        },
        {
            "code": "G5457",
            "lemma": "φῶς",
            "translit": "phōs",
            "gloss": "light",
            "significance": "φῶς ('light, luminousness') opens the letter's first major theological declaration: <em>ὁ θεὸς φῶς ἐστιν</em> — 'God is light, and in him is no darkness at all' (1:5). Like 'God is love' (4:8), this is not an attribute but an identity claim. Light in John's theological lexicon carries the freight of holiness, truth, and the self-revealing character of God: light exposes what is hidden, makes things visible, and cannot coexist with darkness. The practical consequence follows immediately: 'if we say we have fellowship with him while we walk in darkness, we lie' (1:6); 'if we walk in the light as he is in the light, we have fellowship with one another' (1:7). Walking in the light is both ethical (living in accordance with God's holy character) and relational (maintaining genuine community). The false teachers apparently claimed fellowship with God while their moral conduct and christological denial put them in darkness."
        },
        {
            "code": "G225",
            "lemma": "ἀλήθεια",
            "translit": "alḗtheia",
            "gloss": "truth",
            "significance": "ἀλήθεια ('truth, reality, what accords with the facts') functions in 1 John as the criterion for genuine Christianity. It appears in the negative as a devastating diagnostic: 'if we say we have fellowship with him while we walk in darkness, we lie and do not practice the truth' (1:6); 'if we say we have not sinned, we make him a liar, and his word is not in us' (1:10). Positively, truth is the Spirit's domain: 'the Spirit is the truth' (5:6); and the Spirit of truth enables the community to discern what is true (4:6). The false teachers have a particular relationship to truth: 'who is the liar but he who denies that Jesus is the Christ?' (2:22). In 1 John, truth is not merely propositional (correct doctrine) but relational and moral — a person who lives wrongly does not practice (or possess) the truth, regardless of what they claim."
        },
        {
            "code": "G5583",
            "lemma": "ψεύστης",
            "translit": "pseústēs",
            "gloss": "liar",
            "significance": "ψεύστης ('liar, deceiver, one who speaks falsely') is used in 1 John with unusual directness. The letter applies the word to three classes of person: those who claim fellowship with God while walking in darkness ('we lie,' 1:6); those who claim to know God while not keeping his commandments ('he is a liar,' 2:4); those who deny that Jesus is the Christ ('who is the liar but he who denies that Jesus is the Christ?' 2:22); and those who claim to love God while hating their brother ('he is a liar,' 4:20). In 5:10, John comes closest to the most serious charge: the one who does not believe the testimony of God 'has made him a liar.' The ethical force of the word in its ancient honor-shame context was severe — calling someone a liar was a social and moral condemnation. John's use of it for both theological error and moral inconsistency shows that he does not separate the two: to live wrongly is to lie about what God is like."
        }
    ],

    "language_notes": (
        "<p>1 John is written in simple Greek — short declarative sentences, minimal subordination, heavy repetition of the same vocabulary — but the simplicity is deliberate and profound, not rudimentary. The letter's style is <strong>meditative and spiral</strong>: rather than building a single linear argument, John returns to the same cluster of words and themes (light/darkness, love/hate, truth/lie, knowing God, abiding, commandment, sin, eternal life) again and again, each pass adding a new dimension or angle. Three roughly parallel cycles traverse the same material from 1:5 to 5:12. The effect is cumulative rather than progressive: John does not build up to a conclusion so much as he saturates the reader in a set of interlocking realities until their mutual implication becomes clear. To read 1 John for a linear argument is to miss what it is doing.</p>"
        "<p>The two great declarations of the letter — <strong>ὁ θεὸς φῶς ἐστιν</strong> ('God is light,' 1:5) and <strong>ὁ θεὸς ἀγάπη ἐστίν</strong> ('God is love,' 4:8, 16) — are among the most compressed theological statements in the NT. The construction uses <em>εἰμί</em> with a predicate noun (not predicate adjective): light and love are not qualities God possesses but what God is. This is an identity statement, not a description. John makes these claims without qualification, subordination, or hedging — the simplicity of the syntax enacts the absoluteness of the claim. The rest of the letter unpacks the implications: if God is light, walking in darkness while claiming fellowship with him is self-contradiction; if God is love, failing to love one another while claiming to love God is self-contradiction.</p>"
        "<p>The verb <strong>ἵνα</strong> ('in order that') is the letter's most characteristic grammatical marker for purpose and consequence. John structures his appeals around ἵνα clauses: 'I write these things to you... <em>ἵνα</em> you may know that you have eternal life' (5:13); 'these things we write to you <em>ἵνα</em> our joy may be complete' (1:4); 'if anyone does sin, we have an advocate... so that your sins may be forgiven' — the goal always hovers in view. John is not merely describing the Christian life; he is aiming at outcomes: assurance, joy, continued fellowship, right confession, and love. The pastoral intention behind each section is usually made explicit through an ἵνα clause.</p>"
        "<p>The <strong>perfect tense</strong> appears frequently in 1 John for states that began in the past and continue to define the present. In 1:1-4, the prologue uses perfect tenses for the apostolic experience of Jesus: 'that which we have heard, which we have seen with our eyes' (ἀκηκόαμεν, ἑωράκαμεν) — the seeing happened once and remains true and authoritative. Similarly, 'your sins are forgiven' and 'you know him who is from the beginning' (2:12-14) are perfect tense — accomplished states with ongoing validity. This distinguishes the letter&rsquo;s assurance: it is not based on present feeling but on completed actions (the incarnation, the atonement, the apostolic witness) whose effects abide.</p>"
    ),

    "reception": (
        "<p><strong>Patristic:</strong> 1 John was used extensively in the anti-Gnostic controversy of the second and third centuries. Irenaeus drew on 1 John 4:2 (&lsquo;Jesus Christ come in the flesh&rsquo;) as a criterion for testing teaching against the Valentinian and Docetic proposals that had separated the spiritual Christ from the physical Jesus. Polycarp, writing against Marcion, cited 1 John&rsquo;s ἀντίχριστος language. Tertullian used the letter against those who denied Christ&rsquo;s physical body. The letter thus served as the NT&rsquo;s primary resource for the early church&rsquo;s most pressing theological dispute: whether the fully divine could be fully human, and why it mattered. Augustine engaged 1 John deeply in his <em>Ten Homilies on the Epistle of John</em> (c. 415 CE) and derived from it his celebrated aphorism: <em>ama et fac quod vis</em> (&lsquo;love, and do what you will&rsquo;) — a reading of 1 John&rsquo;s love ethic as the comprehensive summary of Christian obligation.</p>"
        "<p><strong>Reformation:</strong> Luther and Calvin both commented on 1 John and valued it for its clear presentation of assurance (5:13), its theology of advocacy (2:1-2), and its grounding of ethics in the indicative of love (4:19). Calvin&rsquo;s commentary is particularly attentive to the three-tests structure and the letter&rsquo;s pastoral aim: he reads it as John&rsquo;s answer to the question &lsquo;how do I know I am a Christian?&rsquo; by redirecting believers from introspection about their feelings to observable marks (right belief, love for brothers, pattern of obedience). The Reformation debates about assurance found in 1 John both comfort (the believer can know they have eternal life) and a warning against cheap assurance (the tests are real).</p>"
        "<p><strong>Modern debates:</strong> Contemporary scholarship debates the identity of the secessionists John opposes. The traditional identification with Cerinthus (who taught that the divine Christ descended on the human Jesus at baptism and departed before the crucifixion) remains plausible but unconfirmed. Others propose proto-Docetism (the body of Jesus was an illusion), Johannine Gnosticism, or a local pneumatic movement that over-emphasized spiritual experience. The debate matters for interpretation: if the opponents were Docetists, &lsquo;come in the flesh&rsquo; (4:2) is the key test; if they were Cerinthians, the focus shifts to the water and blood (5:6). Regardless, most scholars agree that 1 John&rsquo;s three-tests framework (moral, social, doctrinal) provides the structural key to the letter.</p>"
    ),

    "reading_guide": (
        "<p>1 John rewards slow, meditative reading rather than analytical study. The letter is not a theological treatise with a linear argument; it is closer to a long sermon that circles the same themes in wider and wider loops. When you reach 4:7 and read &lsquo;let us love one another,&rsquo; recognize that you have heard this before (2:10; 3:11, 14, 18, 23) — but now it arrives with a different depth: you have passed through a discussion of testing the spirits, the incarnation, the death of Christ as the demonstration of love, and the coming of the Spirit. The repetition is deliberate formation, not redundancy.</p>"
        "<p>The <strong>three tests</strong> are the key to the letter&rsquo;s structure and purpose: (1) the doctrinal test — does this person confess Jesus Christ come in the flesh? (4:2); (2) the moral test — does this person keep his commandments and walk as Jesus walked? (2:3-6; 3:4-10); (3) the social test — does this person love the brothers? (2:9-11; 3:11-18; 4:20). These tests are not a works-based checklist for earning assurance; they are the natural expressions of a life genuinely connected to the God who is light and love. Hold them together: anyone can claim one without the others (the Gnostic secessionists apparently claimed spiritual knowledge while failing the moral and social tests). Genuine faith integrates all three.</p>"
        "<p>Two common misreadings: First, reading 1:9 (&lsquo;if we confess our sins, he is faithful and just to forgive us&rsquo;) as addressed to non-Christians who need initial salvation. In context, the letter is addressed to believers throughout, and 1:9 is the ongoing provision for Christians who sin — the ever-open access to forgiveness through the Advocate (2:1). Second, reading 3:6 (&lsquo;whoever abides in him does not sin&rsquo;) as sinless perfectionism. John has just said in 1:8 that denying sin is self-deception. The resolution: 3:6 describes the characteristic direction of a transformed life — not sinning as a settled pattern and practice — not the absence of any failure ever. The letter&rsquo;s combination of realism about sin (1:8-9) and confidence about transformation (3:6-9) is not contradiction but the full pastoral picture.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('1john')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('1john', merged)

main()
