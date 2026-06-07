"""
Book Study Data — Philemon
book_id: philemon
lang: greek

Run: python3 scripts/build-book-study-philemon.py

Notes:
- Shortest Pauline letter at 25 verses; 8 vocab entries per BS_AGENT_GUIDE.md for short letters
- The letter is a masterpiece of Greek rhetoric (ethos, pathos, logos)
- Paul exploits honor-shame conventions, patronage-client language, and legal/commercial
  vocabulary (logizesthai, charge to account) to achieve his goal without commanding it
- The pun on Onesimus's name (v. 11: achrestos/euchrestos) is the letter's most famous
  linguistic feature
- Do not reproduce: the introduction already covers the Onesimus background,
  purpose (return as beloved brother), and themes in full
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
    "bookId": "philemon",

    "key_vocabulary": [
        {
            "code": "G3870",
            "lemma": "παρακαλέω",
            "translit": "parakaléō",
            "gloss": "appeal",
            "significance": "παρακαλέω ('to call alongside, appeal, beseech, encourage') is the letter's rhetorical pivot at vv. 9-10: 'Although I am bold enough in Christ to command (ἐπιτάσσειν) you to do what is required, yet for love's sake I prefer to appeal (παρακαλῶ).' The contrast with ἐπιτάσσω ('to command with authority') is deliberate. Paul has the apostolic authority to issue a binding command; instead he chooses an appeal that leaves Philemon's agency intact. This is not weakness — it is the rhetorical strategy that makes love possible. An obligatory act of compliance is not love; an appeal that requires free choice is. The whole letter is a παρακλήσις, and Paul's decision to use it rather than a command is the letter's chief argument about the nature of Christian community."
        },
        {
            "code": "G4698",
            "lemma": "σπλάγχνον",
            "translit": "splánchnon",
            "gloss": "heart",
            "significance": "σπλάγχνα ('intestines, inward parts') is used in Greek as the seat of the deep emotions — what English calls the heart or the gut. It appears three times in 25 verses: 'the hearts (σπλάγχνα) of the saints have been refreshed through you' (v. 7); 'I am sending him back to you — my very heart (σπλάγχνα)' (v. 12); 'refresh my heart (σπλάγχνα) in Christ' (v. 20). The three uses build an emotional escalation: Philemon refreshes the saints' hearts (established fact) → Onesimus is Paul's own heart (identification of Paul with Onesimus) → Paul asks Philemon to refresh Paul's heart by receiving Onesimus (the appeal). By calling Onesimus 'my very heart,' Paul makes refusing Onesimus equivalent to refusing Paul himself."
        },
        {
            "code": "G2842",
            "lemma": "κοινωνία",
            "translit": "koinōnía",
            "gloss": "partnership",
            "significance": "κοινωνία ('fellowship, participation, sharing, partnership') appears in two critical places. In v. 6, Paul prays that 'the sharing (κοινωνία) of your faith may become effective.' In v. 17, Paul makes the decisive request: 'So if you consider me your partner (κοινωνόν), receive him as you would receive me.' The word-family links Philemon's spiritual fellowship with his financial-social obligation. The κοινωνία of faith they share in Christ (and which Paul helped create in Philemon) is the ground on which Paul asks Philemon to treat Onesimus as an equal partner. The letter's logic: if Philemon truly shares the faith that has made Onesimus a brother in Christ, that κοινωνία must manifest in how Onesimus is received."
        },
        {
            "code": "G80",
            "lemma": "ἀδελφός",
            "translit": "adelphós",
            "gloss": "brother",
            "significance": "ἀδελφός ('brother') is the letter's most socially explosive word, applied to Onesimus in v. 16: 'no longer as a slave, but better than a slave, as a dear brother — dear to me, but even dearer to you, both as a man and as a brother in the Lord.' The jump from δοῦλος (slave) to ἀδελφός (brother) is the letter's central move. In Roman society, δοῦλος and ἀδελφός occupied opposite ends of the social hierarchy — slaves were property, brothers were family. Paul's claim is that the gospel creates a new kinship that supersedes the slave-master relation without formally abolishing it: Onesimus is simultaneously a slave (legally) and a brother (in Christ), and the second reality is meant to transfigure the first."
        },
        {
            "code": "G1401",
            "lemma": "δοῦλος",
            "translit": "doûlos",
            "gloss": "slave",
            "significance": "δοῦλος ('slave') appears at the letter's hinge point in v. 16: Onesimus was a δοῦλος and Paul does not deny it — 'no longer as a slave, but better than a slave.' The 'better than' (ὑπὲρ δοῦλον) does not erase the δοῦλος category; it adds a new category above it. The Roman slave was legally a person's property, with no family, no standing in court, no name of honor. Paul's argument is that the gospel introduces a reality that relativizes without immediately abolishing this legal status. The phrase 'no longer as a slave' tells Philemon how to treat Onesimus; the legal situation is left to Philemon's own conscience, shaped by the appeal Paul has made. This is why the letter has been read both as endorsing and as subverting the slave system."
        },
        {
            "code": "G2173",
            "lemma": "εὔχρηστος",
            "translit": "eúchrēstos",
            "gloss": "useful",
            "significance": "εὔχρηστος ('useful, profitable') appears in v. 11 alongside its antonym ἄχρηστος ('useless, unprofitable') in one of the NT's most celebrated wordplays: 'Formerly he was useless (ἄχρηστόν) to you, but now he is indeed useful (εὔχρηστον) to you and to me.' The pun is on Onesimus's name — Ὀνήσιμος means 'profitable' or 'useful' in Greek. The runaway slave had failed to be what his name promised; now, converted, he is finally living up to his name. There is a secondary phonetic pun available to Greek ears: ἄχρηστος sounds like 'un-Christly' and εὔχρηστος like 'Christly' (from Χριστός, Christ). Whether Paul intended both levels of wordplay, the name-pun is unmistakable and shows Paul's playful rhetorical skill even in the most serious appeal."
        },
        {
            "code": "G373",
            "lemma": "ἀναπαύω",
            "translit": "anapaúō",
            "gloss": "refresh",
            "significance": "ἀναπαύω ('to rest, cease, refresh, give rest') binds the letter's emotional argument together. In v. 7, 'the hearts of the saints have been refreshed (ἀναπέπαυται) through you, brother.' Paul's prayer opens by establishing Philemon's track record as a refresher of weary believers. In v. 20, the appeal closes: 'refresh (ἀνάπαυσόν) my heart in Christ.' The framing is deliberate: the man who refreshes saints' hearts is being asked to refresh Paul's own heart. The word's range includes rest from labor and relief from distress — in the LXX it translates the Hebrew נוּחַ (rest, related to Noah's name). By using the same word twice, Paul structures his appeal as a test of whether Philemon's established character will hold."
        },
        {
            "code": "G3049",
            "lemma": "λογίζομαι",
            "translit": "logízomai",
            "gloss": "charge",
            "significance": "λογίζομαι ('to count, reckon, calculate, charge to an account') appears in v. 18 in the letter's most theologically resonant moment: 'If he has wronged you at all, or owes you anything, charge that to my account (ἐμοὶ ἐλλόγα).' Paul offers to assume Onesimus's debt — whatever the runaway slave owed his master (the cost of his flight, lost labor, possibly the slave's market value) — Paul puts on his own ledger. The commercial-legal vocabulary (λογίζομαι is the same word used in Romans for the reckoning of righteousness, and ἐλλογάω appears only here in the NT) creates an implicit analogy: as Paul stands surety for Onesimus's debt, so Christ stands surety for the believer's debt before God. The theological echo is almost certainly deliberate."
        }
    ],

    "language_notes": (
        "<p>Philemon is a masterpiece of Greek <strong>rhetoric</strong> — one of the most skilled pieces of persuasive writing in the NT. Paul uses all three Aristotelian modes of persuasion in sequence: <em>ethos</em> (establishing his character and relationship with Philemon, vv. 4-7), <em>pathos</em> (emotional appeal through σπλάγχνα and the identification of himself with Onesimus, vv. 8-16), and <em>logos</em> (the logical argument that partnership obliges reception, and the financial surety offer, vv. 17-20). The letter is structured chiastically — Paul opens with praise for Philemon's love and closes with confidence in Philemon's obedience (v. 21), framing the request with expressions of trust that make refusal a betrayal of one's own stated character.</p>"
        "<p>The most celebrated linguistic feature of the letter is the <strong>wordplay on Onesimus's name</strong> in v. 11: <em>ἄχρηστόν</em> ('useless') and <em>εὔχρηστον</em> ('useful'). Ὀνήσιμος in Greek means 'profitable, useful' — a common slave name in the Roman world, often given ironically. Paul's pun notes that the runaway had not lived up to his name; now, converted, he finally has. A secondary pun is available in the sound of <em>ἄ-χρηστος</em> / <em>εὔ-χρηστος</em> against <em>Χριστός</em> (Christ): the formerly unchristly one is now christly. Whether Paul intended both layers, ancient readers attuned to wordplay would have heard both.</p>"
        "<p>The letter deploys <strong>legal and commercial vocabulary</strong> in v. 18-19 with theological significance. <em>λογίζομαι</em> ('reckon, count, charge to account') is the accounting term used across Greek commerce for recording debits; <em>ἐλλογάω</em> (v. 18, 'charge to my account') is a NT hapax legomenon. Paul writes 'I, Paul, write with my own hand: I will repay it' — authenticating a legal promissory note. The same vocabulary cluster (<em>λογίζομαι</em>, imputation, debt, surety) appears in Romans 4-5 for the reckoning of righteousness; the parallel between Paul's legal pledge for Onesimus and Christ's standing surety for believers is almost certainly intentional, even if not made explicit.</p>"
        "<p>Paul's deliberate choice of <strong>appeal (παρακαλέω) over command (ἐπιτάσσω)</strong> in vv. 8-9 is itself a rhetorical move: 'Although I am bold enough to command, yet for love's sake I prefer to appeal.' By naming the command he is not giving, Paul makes Philemon aware that he could face an order — and then does not issue one. The appeal then arrives with the full weight of what Paul is choosing not to do. This is the letter's subtlest move: the absence of the command does more rhetorical work than the command would have done.</p>"
    ),

    "reception": (
        "<p><strong>Patristic:</strong> Philemon nearly missed inclusion in the NT canon — its lack of explicit theological teaching led some in the early church to question its apostolicity. Origen and Chrysostom were among its most influential defenders. Chrysostom devoted three homilies to the letter, reading it as an example of apostolic pastoral wisdom and a model for Christian social relations. He praised Paul's restraint in not issuing a command, seeing it as evidence of the gospel's ethical method: transformation from the inside rather than legal compulsion. The letter was also read allegorically — Philemon as the soul, Onesimus as the sinful nature, Paul as Christ the intercessor — a reading that gave it theological substance for those who found it too domestic for apostolic scripture.</p>"
        "<p><strong>Slavery debates:</strong> No biblical text has been more contested in the antislavery debates of modern history. Those who defended slavery cited Philemon as evidence that Paul accepted the institution: he returns the runaway slave and does not call for abolition. Abolitionists countered that Paul's appeal to receive Onesimus 'no longer as a slave but as a dear brother' (v. 16) created a moral obligation that the slave system could not survive. The letter became a key text in the American antislavery argument: if the gospel makes enslaved and enslaver brothers, slavery is incompatible with the gospel even where it is not legally abolished. The debate forced exegetes to read the letter with unusual care for the difference between what Paul says and what Paul implies.</p>"
        "<p><strong>Modern interpretation:</strong> Contemporary scholarship reads Philemon as Paul's most direct engagement with the social implications of the gospel. The letter is no longer read as an endorsement of slavery but as a subversive document that creates conditions — the new kinship of brotherhood in Christ — that make the slave-master relationship untenable. The question of what exactly Paul was requesting of Philemon (manumission? permanent loan? simply a warm welcome?) remains debated. N. T. Wright and others have argued that v. 21 ('knowing that you will do even more than I say') implies Paul was expecting manumission, making the letter an implicit call for Onesimus's freedom without ever saying it directly.</p>"
    ),

    "reading_guide": (
        "<p>Read Philemon slowly and in a single sitting — it takes 5 minutes and rewards close attention. The letter is 25 verses, but every verse carries rhetorical weight. As you read, watch for the escalating ways Paul places himself in solidarity with Onesimus: Onesimus is Paul's child in the faith (v. 10), Paul's heart (v. 12), Paul's representative (v. 13), and someone whom Paul will personally guarantee financially (v. 18-19). By the end of the letter, refusing Onesimus and refusing Paul are the same act.</p>"
        "<p>The theological center is vv. 15-16: 'For this is perhaps why he was parted from you for a while, that you might have him back forever, no longer as a slave but better than a slave, as a dear brother.' The 'perhaps' is pastoral humility, not uncertainty — Paul is offering Philemon a way to reframe an embarrassing social situation (his slave ran away) as providential. The temporary separation has produced an eternal gain. The movement from slave (δοῦλον) to brother (ἀδελφόν) in a single sentence is the gospel's social logic compressed into its most personal and concrete form.</p>"
        "<p>Two common misreadings: First, treating the letter as a political statement about slavery in general, when it is a specific pastoral appeal about a specific person. The universal implications are real but should be derived from the specific case, not read back into it. Second, reading Paul's restraint (appeal rather than command) as timidity. Paul is not afraid to use apostolic authority — he does so throughout his letters. His choice here is principled: love that is commanded is not love. The entire letter is structured around getting Philemon to act freely out of love, and that requires Paul to stop short of the command he has the right to give.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('philemon')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('philemon', merged)

main()
