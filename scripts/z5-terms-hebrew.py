#!/usr/bin/env python3
"""
scripts/z5-terms-hebrew.py — write scholarly user_notes for all Hebrew
terms with dispute_level >= 2 into data/translation/glossary-hebrew.json.

Run once; idempotent (re-run overwrites with same content).
After running: python3 scripts/seed-glossary.py
"""

import json
from pathlib import Path

ROOT  = Path(__file__).parent.parent
PATH  = ROOT / 'data' / 'translation' / 'glossary-hebrew.json'

# Scholarly notes keyed by Strong's code.
# Dispute levels: L4 = deepest disagreement, L2 = meaningful but narrower.
NOTES = {
    # ── L4 ────────────────────────────────────────────────────────────────
    'H430': (
        "אֱלֹהִים is a grammatically plural form used with singular verbs when referring to "
        "the God of Israel, and with plural verbs for pagan gods. The classical polytheistic "
        "explanation (remnant of an older pantheon) conflicts with the theological reading "
        "(plural of majesty/intensity — 'the Almighty One'). Trinitarian interpreters "
        "from the church fathers onward have seen a foreshadowing of plurality-in-unity; "
        "Jewish and critical scholars firmly reject this as eisegesis. The divine council "
        "background (Ps 82:1, 6; Job 1-2) shows the term can refer to heavenly beings in "
        "the divine assembly. Heiser's 'divine council' framework has renewed scholarly "
        "interest in these texts. The LXX consistently renders it θεός (singular) for YHWH, "
        "flattening the grammatical tension."
    ),
    'H2617': (
        "חֶסֶד is one of the most lexically rich words in the OT and resists single-word "
        "translation. It combines loyal covenant love, steadfast mercy, kindness, and "
        "faithfulness. Nelson Glueck's landmark study argued it is strictly covenantal "
        "(obligation between parties); Katharine Sakenfeld and others showed it also describes "
        "gratuitous generosity beyond obligation. The KJV renders it 'lovingkindness,' "
        "the ESV often 'steadfast love,' the NASB 'faithfulness' or 'kindness' contextually. "
        "In Hos 6:6 ('I desire חֶסֶד, not sacrifice') it carries covenantal-moral weight "
        "that Jesus cites twice (Matt 9:13; 12:7). The Hebrew concept arguably has no "
        "single English equivalent and may require a gloss note in any translation."
    ),
    'H3068': (
        "יְהוָה (the Tetragrammaton, YHWH) is the personal covenant name of the God of "
        "Israel. Its pronunciation was lost in post-exilic practice; 'Jehovah' is a hybrid "
        "of the consonants with the vowels of אֲדֹנַי. Modern scholarly consensus favors "
        "'Yahweh' as the most plausible pronunciation based on Greek transcriptions "
        "(Ἰαβέ, Origen) and theophoric names. Rendering YHWH as 'LORD' (small caps) follows "
        "the LXX's κύριος tradition, which the NT authors adopt when citing the OT and "
        "applying YHWH texts to Jesus (e.g. Rom 10:13; Phil 2:11). Some traditions "
        "(e.g. Jehovah's Witnesses, Sacred Name movement) use 'Yahweh' or 'Jehovah' in the "
        "NT as well. The substitution 'LORD' risks obscuring the place-name and narrative "
        "identity of the divine name in the OT storyline."
    ),
    'H7307': (
        "רוּחַ means wind, breath, or spirit and is grammatically feminine. It is used for "
        "the Spirit of God hovering over the waters (Gen 1:2), life-breath given to Adam "
        "(Gen 2:7), prophetic inspiration (Num 11:25), and the human spirit. The key debates: "
        "(1) Is רוּחַ אֱלֹהִים in Gen 1:2 'the Spirit of God' (personal, Trinitarian) or "
        "'a mighty wind' (NJPS)? Context and syntax are genuinely ambiguous. "
        "(2) In the prophets, does the Spirit come upon the Messiah as an anointing (Isa 11:2; "
        "61:1) in a way continuous with or distinct from NT pneumatology? "
        "(3) The OT evidence for the Spirit as a distinct divine person is debated; "
        "Waltke argues for it, Dunn and others see this as a later Trinitarian reading."
    ),

    # ── L3 ────────────────────────────────────────────────────────────────
    'H1285': (
        "בְּרִית (covenant) is the structural backbone of biblical theology. The primary "
        "debate: are biblical covenants bilateral (conditional: 'if you obey…') or unilateral "
        "(unconditional divine commitment)? Scholars like Mendenhall and Hillers connect "
        "Israel's covenants to ancient Near Eastern suzerain-vassal treaties (bilateral); "
        "others like Williamson distinguish royal grant covenants (unilateral, Abrahamic/"
        "Davidic) from Mosaic treaty covenants (bilateral). The new covenant of Jer 31:31-34 "
        "is central to NT hermeneutics: how much continuity exists between old and new? "
        "Dispensationalism, covenant theology, and new covenant theology all answer differently."
    ),
    'H5315': (
        "נֶפֶשׁ is usually rendered 'soul' but its semantic range is much broader: living "
        "creature, throat/appetite, person, life, self. In Gen 2:7 'man became a living נֶפֶשׁ' "
        "(not 'received a soul'), suggesting that נֶפֶשׁ is not a separable immaterial "
        "component but the whole animated person. This supports anthropological 'monism' "
        "(no immortal soul distinct from body) against Platonic dualism. However, passages "
        "like Ps 16:10 ('you will not abandon my נֶפֶשׁ to Sheol') suggest some form of "
        "personal continuity beyond death. The debate directly bears on the nature of the "
        "intermediate state, soul sleep, and the resurrection hope."
    ),
    'H5769': (
        "עוֹלָם means long duration, antiquity, or indefinite future—not necessarily "
        "'eternity' in the philosophical sense of timelessness. Olam ha-ba ('the age to "
        "come') is a temporal category in Jewish thought, not a timeless realm. "
        "Ramelli's argument (parallel to αἰώνιος) that עוֹלָם and its Greek counterpart "
        "do not inherently mean 'endless' affects how one reads 'everlasting punishment,' "
        "'everlasting covenant,' and 'from everlasting to everlasting' (Ps 90:2). "
        "Most traditional translations retain 'eternal/everlasting' without qualification; "
        "conditionalist and annihilationist readings lean on the durational/age-based sense."
    ),
    'H6666': (
        "צְדָקָה (righteousness) shares the root צדק with צַדִּיק (righteous person) and "
        "צֶדֶק (justice). The OT sense is primarily relational and covenantal: acting "
        "rightly within a relationship. In the prophets (Amos 5:24; Isa 1:27) it encompasses "
        "justice for the vulnerable—a dimension the English 'righteousness' can lose. "
        "The debate mirrors that of δικαιοσύνη (G1343): is God's righteousness primarily "
        "his judicial perfection (Reformed), his covenant faithfulness (Wright), or his "
        "saving action on behalf of the oppressed (liberation theology)? "
        "Isa 45:8; 46:13; 51:5-8 use צְדָקָה in close parallel with יְשׁוּעָה (salvation), "
        "highlighting the salvific/restorative dimension."
    ),

    # ── L2 ────────────────────────────────────────────────────────────────
    'H539': (
        "אָמַן (believe, trust, be firm) is the root of both אֱמֶת (truth) and אָמֵן (amen). "
        "The hiphil form הֶאֱמִין means to count someone reliable, to trust. Gen 15:6 "
        "('Abraham believed/trusted God and it was counted to him as righteousness') is "
        "cited in Rom 4, Gal 3, and Jas 2. Whether this is intellectual assent, relational "
        "trust, or covenantal fidelity shapes the broader faith-works discussion. "
        "The root's connection to 'firmness/stability' (like a nursing mother, Num 11:12) "
        "suggests trust grounded in demonstrated faithfulness."
    ),
    'H571': (
        "אֶמֶת (truth, faithfulness, reliability) overlaps with חֶסֶד in covenantal contexts "
        "(they appear together in Ps 25:10; 85:10; John 1:14's χάρις καὶ ἀλήθεια likely "
        "renders חֶסֶד וֶאֱמֶת). Unlike the Greek ἀλήθεια, which tends toward propositional "
        "correspondence, אֶמֶת emphasizes reliability and trustworthiness—truth as what "
        "proves faithful over time. This affects how Pilate's question 'What is truth?' "
        "(John 18:38) is contextualized: Jesus as אֶמֶת/ἀλήθεια (John 14:6) means "
        "reliable covenant presence, not merely correct information."
    ),
    'H2580': (
        "חֵן (grace, favor) is God's or a superior's gratuitous good will toward someone, "
        "often expressed in the phrase 'find favor in someone's eyes' (Gen 6:8; Exod 33:12). "
        "It is distinguished from חֶסֶד by being more spontaneous/unearned rather than "
        "covenantally obligated. The NT χάρις (G5485) draws on both words. "
        "The pairing חֵן וָחֶסֶד occurs in Ps 45:2 and Prov 3:4; together they span "
        "spontaneous gift and covenant loyalty."
    ),
    'H3045': (
        "יָדַע (know) has a semantic range extending from intellectual cognition to relational "
        "intimacy and even sexual union (Gen 4:1). The covenantal sense—'I have known you by "
        "name' (Exod 33:17), 'You only have I known of all the families' (Amos 3:2)—implies "
        "elected, intimate relationship rather than mere acquaintance. This affects "
        "interpretation of Matt 7:23 ('I never knew you') and John 10:14 ('I know my sheep'): "
        "the issue is relational belonging, not informational knowledge."
    ),
    'H3519': (
        "כָּבוֹד (glory, weight, honor) denotes the manifest presence and weighty reality of "
        "God—the Shekinah cloud-pillar tradition. In Isa 6:3 the whole earth is 'full of his "
        "כָּבוֹד.' The LXX renders it δόξα, which in classical Greek meant human opinion or "
        "reputation; the LXX use transforms δόξα into the luminous, overwhelming presence of "
        "God. John 1:14 ('we beheld his glory') and the Transfiguration draw on this OT "
        "background. The reduction of כָּבוֹד to 'fame' or 'reputation' loses the ontological "
        "weight the word carries."
    ),
    'H4428': (
        "מֶלֶךְ (king) and the concept of מַלְכוּת (kingdom) are foundational to both OT "
        "theocracy and NT 'kingdom of God' proclamation. The OT tension: YHWH is the true "
        "King of Israel (1 Sam 8:7), yet human kingship is accommodated and eventually "
        "centered on the Davidic covenant (2 Sam 7). NT kingdom debates parallel these: "
        "is the kingdom primarily present (inaugurated eschatology) or future (thoroughgoing "
        "eschatology)? Realized, ethical, theocratic, and apocalyptic readings all begin "
        "with how מֶלֶךְ/βασιλεία is construed in the OT background."
    ),
    'H6944': (
        "קֹדֶשׁ (holiness, sacredness) is the primary OT term for that which belongs to God "
        "and is set apart from the common (חֹל) and the unclean (טָמֵא). The holiness code "
        "(Lev 17-26) commands Israel to 'be holy as YHWH is holy' (Lev 19:2). "
        "Debates: (1) Is holiness primarily moral purity or ontological 'otherness'? "
        "Rudolph Otto's 'holy' as mysterium tremendum et fascinans emphasizes the numinous "
        "dimension; Reformed theology foregrounds moral perfection. "
        "(2) Does the NT democratize holiness (all believers are ἅγιοι, G40) in a way that "
        "breaks from OT priestly stratification, or continue and fulfill it?"
    ),
    'H7965': (
        "שָׁלוֹם is frequently translated 'peace' but encompasses wholeness, completeness, "
        "well-being, and right relationship. It is not merely the absence of conflict but "
        "the positive flourishing of persons and community under God's blessing. "
        "The prophetic vision (Isa 9:6-7; 52:7; Mic 5:5) links שָׁלוֹם to the Messiah's "
        "reign. In NT soteriology, 'peace with God' (Rom 5:1, εἰρήνη) translates the "
        "covenant-restoration dimension of שָׁלוֹם. The modern reduction of peace to "
        "political non-violence loses the creational/eschatological depth of the term."
    ),
    'H8199': (
        "שָׁפַט (judge, rule, govern) and its noun מִשְׁפָּט (justice, judgment, ordinance) "
        "cover both judicial verdict and social justice. YHWH as שֹׁפֵט (judge, Gen 18:25) "
        "means the righteous arbiter of all, which grounds Abraham's intercessory appeal. "
        "The prophets use מִשְׁפָּט alongside צְדָקָה as the twin demands of the covenant: "
        "Amos 5:24 ('let justice/מִשְׁפָּט roll like a river'). Whether this is primarily "
        "legal/procedural justice or distributive/restorative justice is contested between "
        "traditional and liberation readings."
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

    print(f'Updated {updated} Hebrew entries with scholarly user_notes.')
    if not_found:
        print(f'Not found: {not_found}')
    print('Next: python3 scripts/seed-glossary.py')

if __name__ == '__main__':
    main()
