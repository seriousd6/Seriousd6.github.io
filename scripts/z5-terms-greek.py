#!/usr/bin/env python3
"""
scripts/z5-terms-greek.py — write scholarly user_notes for all Greek
terms with dispute_level >= 2 into data/translation/glossary-greek.json.

Run once; idempotent (re-run overwrites with same content).
After running: python3 scripts/seed-glossary.py
"""

import json
from pathlib import Path

ROOT  = Path(__file__).parent.parent
PATH  = ROOT / 'data' / 'translation' / 'glossary-greek.json'

# Scholarly notes keyed by Strong's code.
# Dispute levels: L4 = deepest disagreement, L2 = meaningful but narrower.
NOTES = {
    # ── L4 ────────────────────────────────────────────────────────────────
    'G1343': (
        "δικαιοσύνη carries both a forensic sense (declared righteous before God's tribunal) "
        "and a transformative/ethical sense (right conduct flowing from covenant relationship). "
        "The Reformation debate between Luther's 'alien righteousness' (iustitia aliena) and "
        "Roman Catholic infused grace remains live. N. T. Wright reads it as 'covenant "
        "faithfulness,' stressing the relational/eschatological dimension over the purely "
        "forensic; John Piper and others (traditional Reformed) insist imputed righteousness is "
        "the lexical and theological core. The Hebrew background (צְדָקָה H6666) supports both "
        "poles—it can mean 'in the right' judicially and 'acting rightly' relationally. "
        "Key passages: Rom 1:17; 3:21-26; Matt 5:6, 20; Phil 3:9."
    ),
    'G4561': (
        "σάρξ spans a wide semantic range: (1) physical flesh/meat (1 Cor 15:39); "
        "(2) the human body or person (Gal 2:20); (3) earthly descent/ethnic identity "
        "(Rom 9:3); (4) the sinful disposition opposing the Spirit (Rom 8:3-8; Gal 5:16-19). "
        "Sense 4 is theologically contested: does Paul personify σάρξ as an almost demonic "
        "force, or simply as unaided human nature? Bultmann reads it as the whole person "
        "oriented away from God; Dunn ties it more closely to ethnic boundary markers. "
        "The translator must decide whether 'flesh,' 'sinful nature,' 'human nature,' or a "
        "context-driven rendering best preserves the force of each use."
    ),
    'G1342': (
        "δίκαιος (righteous/just) is ambiguous between a legal verdict ('acquitted') and a "
        "moral quality ('upright'). In the LXX it translates צַדִּיק, which can describe both "
        "God's judicial verdict and a person's actual moral standing. The Reformation sharpened "
        "this: is the person δίκαιος because God declares it (forensic) or because they are "
        "actually becoming righteous (transformative)? Both senses coexist in Matthew (5:45; "
        "25:37, 46) and Paul (Rom 5:7; Phil 4:8). The related term δικαιόω (justify) is the "
        "sharper flashpoint—Paul's 'justify' versus James's 'justify' (Jas 2:21-24) has "
        "occupied exegetes from Augustine onward."
    ),

    # ── L3 ────────────────────────────────────────────────────────────────
    'G4102': (
        "πίστις is rendered 'faith' or 'faithfulness' depending on context. The genitive "
        "construction πίστις Ἰησοῦ Χριστοῦ (e.g. Gal 2:16; Rom 3:22) divides scholars: "
        "the 'subjective genitive' reading ('the faithfulness of Jesus Christ') is championed "
        "by Hays, Hooker, and Wright; the 'objective genitive' reading ('faith in Jesus "
        "Christ') is defended by Dunn, Schreiner, and the traditional Reformation view. "
        "The distinction is not merely grammatical—it reframes whether Paul grounds "
        "justification in the human act of believing or in Christ's own covenantal obedience. "
        "Both readings are grammatically possible; context and theological framework drive "
        "the decision."
    ),
    'G3551': (
        "νόμος most often refers to the Mosaic Torah but can mean 'principle/rule' (Rom 3:27; "
        "7:21-23) or specific OT texts (John 10:34; 12:34). The key dispute: when Paul writes "
        "negatively about 'works of the law' (ἔργα νόμου), does he target Torah observance as "
        "a merit system (traditional Reformation reading: law as ladder to self-righteousness), "
        "or Jewish ethnic boundary markers—circumcision, food laws, calendar (New Perspective: "
        "Dunn, Wright)? The answer shapes the entire structure of Paul's soteriology. "
        "Galatians and Romans are the primary battleground; the Dead Sea Scrolls' 4QMMT "
        "uses the exact phrase מעשי התורה (works of the law) in a halakhic context, supporting "
        "a sociological reading without excluding the moral dimension."
    ),
    'G26': (
        "ἀγάπη is frequently distinguished from ἔρος (passionate desire) and φιλία "
        "(friendship/affection) in popular theology, but this sharp separation is not "
        "uniformly supported by the lexical evidence—the LXX uses ἀγαπάω for Amnon's lust "
        "(2 Sam 13:15) and Hosea's covenant love alike. C. S. Lewis's fourfold schema "
        "('The Four Loves') is influential but goes beyond strict lexicography. "
        "Theologically, ἀγάπη in the NT (esp. 1 Cor 13; John 3:16; 1 John 4:8) connotes "
        "self-giving, volitional love rooted in God's character rather than the beloved's "
        "worthiness. Whether this is a distinctly 'Christian' redefinition of the word or "
        "a natural extension of its Septuagintal range is debated."
    ),
    'G166': (
        "αἰώνιος is traditionally rendered 'eternal/everlasting' but the word derives from "
        "αἰών (age/era) and can mean 'belonging to the [coming] age' rather than strictly "
        "'unending in time.' Ilaria Ramelli and David Konstan (Ramelli, 2013) argue it "
        "consistently means 'pertaining to the age' and that 'eternal punishment' (Matt "
        "25:46) should be read as 'punishment of the age [to come],' opening the door to "
        "conditionalism or universalism. The traditional view (Mounce, Schreiner) holds "
        "that by the first century αἰώνιος had lexicalized to mean 'without end.' "
        "The same word applies symmetrically to 'eternal life' and 'eternal punishment' in "
        "Matt 25:46, making the rendering high-stakes for eschatology."
    ),
    'G4151': (
        "πνεῦμα means breath, wind, or spirit and is used for the human spirit, angelic/demonic "
        "spirits, and the Holy Spirit. The key exegetical debates: (1) Is 'spirit' in Rom 8 "
        "the Holy Spirit or the regenerate human spirit? Context usually distinguishes, but "
        "Rom 8:16 ('the Spirit himself bears witness with our spirit') requires careful "
        "differentiation. (2) Does 'spiritual body' (σῶμα πνευματικόν, 1 Cor 15:44) mean "
        "'immaterial' or 'animated/transformed by the Spirit'? N. T. Wright and Anthony Thiselton "
        "argue strongly for the latter. (3) Pneumatology debates (procession, gifts, tongues) "
        "all hinge on specific uses of this term."
    ),
    'G3056': (
        "λόγος covers word, reason, account, speech, and the divine Logos of John 1. "
        "The Johannine Prologue's identification of λόγος with Christ draws on both the "
        "Greek philosophical tradition (Heraclitus, Stoics, Philo) and the Hebrew דָּבָר "
        "(dabar — divine word as creative/prophetic agent, e.g. Ps 33:6; Isa 55:11). "
        "Whether John primarily intends a Jewish or Hellenistic audience shapes the reading. "
        "Modalists and Arians historically exploited λόγος to subordinate the Son; "
        "Nicene theology distinguishes the eternal generation of the Son as λόγος from "
        "creaturely subordination. In non-Johannine contexts (e.g. 'give an account' in "
        "Matt 12:36; Rom 14:12) the forensic sense dominates."
    ),

    # ── L2 ────────────────────────────────────────────────────────────────
    'G3498': (
        "νεκρός (dead) is used literally of physical death and metaphorically of spiritual "
        "death (Eph 2:1; Col 2:13). The debate: does 'dead in trespasses' imply total "
        "inability to respond to God (Reformed/Calvinist reading) or simply moral corruption "
        "without loss of libertarian free will (Arminian/Molinist reading)? The metaphor's "
        "force—whether a corpse can 'choose' anything—is central to Calvinist anthropology. "
        "Most scholars agree on the metaphorical force without agreeing on its theological "
        "implications for the will."
    ),
    'G2316': (
        "θεός is the standard LXX/NT word for God but can also denote pagan deities, "
        "powerful beings, or (controversially) humans in a divine role (John 10:34-35, citing "
        "Ps 82:6). The Granville Sharp rule and Colwell's rule bear on whether θεός in "
        "John 1:1c ('the Word was θεός') implies identity with the Father or a qualitative "
        "predicate. Jehovah's Witnesses render it 'a god' (indefinite); Trinitarian scholars "
        "(Wallace, Mounce) read it as qualitative—the Word possesses the nature of God without "
        "being identical to 'the God' (ὁ θεός) of v.1b. This is one of the most lexically "
        "contested single clauses in the NT."
    ),
    'G2842': (
        "κοινωνία is translated 'fellowship,' 'communion,' 'participation,' or 'sharing.' "
        "The range matters: in 1 Cor 10:16 it denotes actual participation/sharing in Christ's "
        "body and blood (sacramental reading versus merely commemorative). In Phil 1:5 and "
        "2 Cor 9:13 it can mean financial sharing/contribution. Hauck (TDNT) emphasizes the "
        "concrete sharing dimension over against a merely sentimental 'fellowship.' "
        "Ecumenical dialogues (Lutheran-Catholic, Anglican-Orthodox) have used κοινωνία "
        "extensively as an ecclesiological category; the term carries more freight in those "
        "contexts than the Greek lexicon alone supports."
    ),
    'G1680': (
        "ἐλπίς in biblical Greek is not wishful uncertainty but confident expectation grounded "
        "in God's promises and past acts. This distinguishes it from colloquial English 'hope.' "
        "The debate is less about translation and more about theological weight: "
        "Moltmann's Theology of Hope grounds the entire eschatological dimension of "
        "Christianity in this concept. The 'already/not yet' tension of NT eschatology means "
        "ἐλπίς always points forward without being speculative."
    ),
    'G5485': (
        "χάρις primarily means gift/favor/grace and is central to Pauline soteriology. "
        "The key dispute: is grace 'irresistible' (efficacious grace, Reformed) or resistible "
        "(prevenient grace, Arminian; infused grace, Catholic)? Paul's use in Rom 11:6 "
        "('if by grace, no longer from works') implies grace and merit are mutually exclusive "
        "categories. Catholic theology distinguishes actual grace (momentary divine assistance) "
        "from sanctifying grace (habitual disposition). The Greek word itself does not "
        "adjudicate between these theologies; context and systematic framework do."
    ),
    'G3670': (
        "ὁμολογέω means to say the same thing, agree, confess, or profess. In 1 John 1:9 "
        "('if we confess our sins') it implies agreeing with God's assessment of sin. "
        "In Rom 10:9-10 it is parallel to πιστεύω (believe), raising the question of "
        "whether public confession is salvifically necessary or an expected expression of "
        "saving faith. The mouth/heart parallelism in Romans 10 is exegetically debated: "
        "are the two actions redundant (hendiadys) or distinct acts?"
    ),
    'G2222': (
        "ζωή in the NT carries the sense of the life of the age to come, not merely biological "
        "existence (βίος). 'Eternal life' (ζωὴ αἰώνιος) in John is often presented as "
        "a present possession ('has eternal life,' John 5:24) rather than a future state alone, "
        "fueling debates about realized versus future eschatology. John 10:10 ('life abundantly') "
        "is used in prosperity theology contexts; exegetes like Carson note the context is "
        "about security and knowing the Shepherd, not material blessing."
    ),
    'G40': (
        "ἅγιος means holy, set apart, sacred. Applied to believers (ἅγιοι = saints/holy ones), "
        "it does not necessarily imply moral perfection but consecration to God. The Catholic "
        "tradition reserves 'saint' for canonized individuals; Protestant usage extends it to "
        "all believers (Eph 1:1; Phil 1:1). In contexts like 1 Cor 6:2 ('the saints will judge "
        "the world') the eschatological dimension is primary. The concept of God's holiness "
        "(e.g. Isa 6:3; Rev 4:8) involves his moral perfection and 'otherness' (Rudolph Otto's "
        "'mysterium tremendum') — both dimensions belong to the word."
    ),
    'G2041': (
        "ἔργον (work/deed) is the crux of the faith-works debate. Paul argues no one is "
        "justified by ἔργα νόμου (works of law, Gal 2:16); James says faith without ἔργα "
        "is dead (Jas 2:17). Luther famously called James an 'epistle of straw.' "
        "The standard harmonization: Paul addresses ἔργα as the basis of justification "
        "(before God); James addresses ἔργα as the evidence of justification (before people/God). "
        "The New Perspective reads Paul's 'works of law' as Jewish ethnic markers specifically, "
        "not good works generically, which narrows the apparent tension with James."
    ),
    'G3340': (
        "μετανοέω means to change one's mind, turn around, or repent. "
        "The LXX often uses it to translate נָחַם (nacham, relent/be sorry) and שׁוּב "
        "(shuv, return/turn). The debate: does NT repentance primarily mean intellectual "
        "change of mind (metanoia as rethinking), emotional remorse, or volitional turning? "
        "Zane Hodges argued μετανοέω in Acts requires only intellectual change, not sorrow "
        "or behavioral change; mainstream evangelicals (MacArthur, Grudem) insist genuine "
        "repentance involves the whole person. The lordship salvation controversy turns "
        "partly on this word's semantic range."
    ),
    'G3962': (
        "πατήρ (father) is used of God as Father of Israel, Father of Jesus (unique sonship), "
        "and Father of believers (adoptive). The distinction between the eternal Father-Son "
        "relationship (ontological Trinity) and the adoptive fatherhood of believers is "
        "crucial. Feminist theologians (Sallie McFague, Elizabeth Johnson) argue 'Father' is "
        "a metaphor that should be supplemented or replaced; traditional theology (Torrance, "
        "Bavinck) holds that Jesus's own use of Ἀββά marks this as the revealed name of God, "
        "not merely a cultural metaphor. The Lord's Prayer and the Johannine discourse ground "
        "this debate exegetically."
    ),
}

def main():
    with open(PATH, encoding='utf-8') as f:
        gloss = json.load(f)

    updated = 0
    not_found = []

    for code, note in NOTES.items():
        if code not in gloss:
            not_found.append(code)
            continue
        gloss[code]['user_notes'] = note
        updated += 1

    with open(PATH, 'w', encoding='utf-8') as f:
        json.dump(gloss, f, ensure_ascii=False, separators=(',', ':'))

    print(f'Updated {updated} Greek entries with scholarly user_notes.')
    if not_found:
        print(f'Not found: {not_found}')
    print('Next: python3 scripts/seed-glossary.py')

if __name__ == '__main__':
    main()
