"""
Book Study Data — Job
book_id: job
lang: hebrew

Run: python3 scripts/build-book-study-job.py

Notes:
- Author group: Wisdom (Job-Ecclesiastes) in author-freq-hebrew.json
- Wisdom peaks are generic wisdom words; vocabulary selected for Job's
  specific literary-theological program: the forensic challenge to God,
  the lament tradition, the divine-name distribution, and the whirlwind answer
- 12 vocab entries; Hebrew translit fields blank in glossary — supplied manually
- H3198 yakah: THE legal word of Job (18+ occurrences); Job wants to "argue
  his case (yakach)" with God; 9:33 longs for a mokiach (one who decides,
  from yakach root); drives the book's forensic structure
- H410 el: the dialogue sections (chs. 3-37) use El/Eloah/Shaddai overwhelmingly
  rather than YHWH — the prologue/epilogue use YHWH; this distribution is
  theologically deliberate, mirroring the sufferer's distance from the personal God
- H582 enosh: deliberate echo of Psalm 8 (same word, reversed valence — wonder vs. anguish)
- H6030 anah: appears ~100x in Job — no OT book approaches this density
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
    "bookId": "job",

    "key_vocabulary": [
        {
            "code": "H3198",
            "lemma": "יָכַח",
            "translit": "yākaḥ",
            "gloss": "argue/decide",
            "significance": "יָכַח (yakah, &lsquo;to be right; reciprocally, to argue a case; causatively, to decide, justify, reprove — the verb that covers the entire spectrum from forensic dispute to judicial verdict&rsquo;) is the controlling word of Job&rsquo;s legal challenge to God. The book uses yakah more than any other OT book: Job demands a judicial encounter in 13:3 (&lsquo;I desire to argue [yakach] my case with God&rsquo;) and in 13:15 (&lsquo;I will defend my ways to his face&rsquo;). The noun derived from this root — mokiach (one who arbitrates/decides) — appears in Job&rsquo;s most plaintive cry at 9:33: &lsquo;There is no arbiter (mokiach) between us, who might lay his hand on us both.&rsquo; Job longs for a third party who could preside over his dispute with God — a figure who has a hand on both the divine and human party and can bring them into a just settlement. This is the first OT articulation of the need for a mediator — the very role 1 Timothy 2:5 assigns to Christ: &lsquo;there is one God, and there is one mediator (mesitēs) between God and men, the man Christ Jesus.&rsquo; The divine speeches are the yakah-answer: not a legal verdict but an overwhelming counter-interrogation that transforms the relationship from lawsuit to encounter."
        },
        {
            "code": "H582",
            "lemma": "אֱנוֹשׁ",
            "translit": "ʾĕnôš",
            "gloss": "mortal man",
            "significance": "אֱנוֹשׁ (enosh, &lsquo;a man in general — but specifically a frail, mortal human being; the word carries connotations of weakness, sickness, and creaturely transience that the more dignified adam does not&rsquo;) is used in Job&rsquo;s most audacious intertextual move. 7:17-18: &lsquo;What is mortal man (enosh) that you make so much of him, and that you set your heart on him, visiting him every morning and testing him every moment?&rsquo; This is a deliberate, anguished reversal of Psalm 8:4: &lsquo;What is man (enosh) that you are mindful of him?&rsquo; In Psalm 8, the question is asked with wondering worship — God condescends to glorify frail humanity with dominion and glory. In Job 7, the same question with the same word is asked with anguish: God&rsquo;s relentless attention to this enosh is not an honor but a torment. Job 14:1 extends this: &lsquo;Man (adam) who is born of a woman is few of days and full of trouble; he comes out like a flower and withers.&rsquo; The distinction between enosh and adam in wisdom literature is the difference between humanity as image-bearer (adam) and humanity as mortal creature (enosh). Job inhabits both — the book forces the tension between human dignity and human fragility to the surface."
        },
        {
            "code": "H7379",
            "lemma": "רִיב",
            "translit": "rîb",
            "gloss": "lawsuit",
            "significance": "רִיב (rib, &lsquo;a contest, whether personal or legal; a lawsuit; also the formal complaint filed in a covenant lawsuit&rsquo;) is Job&rsquo;s legal metaphor for his relationship with God. Job&rsquo;s rib against God is the spine of the dialogue: he is not merely complaining but making a formal legal charge of injustice. The rib-form in the OT is associated with covenant lawsuit: YHWH files ribs against Israel (Hos 4:1: &lsquo;Hear the word of the LORD, O children of Israel, for YHWH has a rib [lawsuit] against the inhabitants of the land&rsquo;; Mic 6:2: &lsquo;Hear, O mountains, the rib of YHWH&rsquo;). Job audaciously inverts the direction: the creature files a rib against the Creator. 31:35 is the legal climax: &lsquo;Here is my signature — let the Almighty answer me! Let my adversary write out his indictment (sefer rib)!&rsquo; Job demands a written legal answer. The book&rsquo;s resolution does not provide the legal verdict Job requested — instead, God&rsquo;s answer transforms the rib into an encounter, and Job&rsquo;s final speech (42:1-6) is not a legal retraction but an act of worship from someone who has met, not merely argued with, God."
        },
        {
            "code": "H7585",
            "lemma": "שְׁאוֹל",
            "translit": "šĕʾôl",
            "gloss": "realm of the dead",
            "significance": "שְׁאוֹל (sheol, &lsquo;the realm of the dead — whether conceived as a subterranean place, a state of existence, or a power that claims all the living; not necessarily a place of punishment but of shadowy non-existence where God&rsquo;s presence is absent&rsquo;) is used in Job with a paradoxical logic that makes it theologically unique. Job&rsquo;s desire for sheol is not suicidal but strategic: 14:13: &lsquo;Oh, that you would hide me in sheol, that you would conceal me until your wrath is past, that you would appoint me a set time, and remember me!&rsquo; Job wants to flee into death as a hiding place from God&rsquo;s attention, hoping that after his death God&rsquo;s wrath might abate and God might &lsquo;remember&rsquo; (zakar) him. This is the desperate inversion of Psalm 139:8: &lsquo;if I make my bed in sheol, you are there.&rsquo; Where Psalm 139 finds comfort in the impossibility of fleeing God, Job finds terror in the same truth. The sheol-logic reaches its climax at 19:25-27: Job hopes to see God after his skin has been destroyed — a post-mortem encounter with a reconciled God. This hope, uttered from within the despair of sheol-longing, is the first OT expression of resurrection hope as the answer to the problem of divine justice: what cannot be resolved in this life will be resolved beyond it."
        },
        {
            "code": "H6030",
            "lemma": "עָנָה",
            "translit": "ʿānāh",
            "gloss": "answer",
            "significance": "עָנָה (anah, &lsquo;to pay attention, to heed; by implication, to answer, respond, testify — the most common Hebrew word for giving a verbal response&rsquo;) is the book of Job&rsquo;s structuring word. It appears approximately 100 times in Job — no other OT book approaches this density for a single verb. The entire book is built around the question of whether God will &lsquo;answer&rsquo; (anah) Job. Job demands an answer repeatedly (13:22: &lsquo;Then call, and I will answer; or let me speak, and you reply to me&rsquo;). The three friends &lsquo;answer&rsquo; each other in the three dialogue cycles. The divine speeches are introduced with the explicit claim that God &lsquo;answered&rsquo; (anah) Job from the whirlwind (38:1; 40:6). Job &lsquo;answers&rsquo; God at the end (40:3; 42:1). The anah-density tracks the book&rsquo;s fundamental claim: divine sovereignty does not mean divine silence. The God who allows catastrophic suffering is the same God who speaks from the whirlwind — and that speaking, even when it does not provide philosophical explanation, is itself the answer. The NT deepens this: &lsquo;Long ago, at many times and in many ways, God spoke (elálēsen) to our fathers by the prophets, but in these last days he has spoken to us by his Son&rsquo; (Heb 1:1-2) — the definitive anah."
        },
        {
            "code": "H1870",
            "lemma": "דֶּרֶךְ",
            "translit": "dɛrɛk",
            "gloss": "way",
            "significance": "דֶּרֶךְ (derek, &lsquo;a road as trodden; figuratively, a course of life, a manner of action — used both concretely and as a moral/theological metaphor for conduct and direction&rsquo;) is the word that Job seeks and cannot find. 23:8-10: &lsquo;If I go forward, he is not there; backward, I cannot perceive him; on the left hand when he is working, I do not behold him; he turns to the right hand, but I cannot see him. But he knows the way (derek) that I take; when he has tested me, I shall come out as gold.&rsquo; Job cannot find God&rsquo;s derek — the divine direction is hidden from him — but he trusts that God knows his derek: his innocence is transparent to the one he cannot locate. Chapter 28 (the Wisdom hymn) asks the ultimate derek-question: &lsquo;But where shall wisdom be found? And where is the place (derek) of understanding?&rsquo; (28:12). The answer: &lsquo;Behold, the fear of the Lord, that is wisdom, and to turn away from evil is understanding&rsquo; (28:28). The derek the book points toward is not the discovery of God&rsquo;s philosophical reasons but the posture of fear-and-trust — which Job already inhabits before the divine speeches and which the divine speeches confirm."
        },
        {
            "code": "H6662",
            "lemma": "צַדִּיק",
            "translit": "ṣaddîq",
            "gloss": "righteous",
            "significance": "צַדִּיק (tsaddiq, &lsquo;just, righteous — both in the forensic sense (in the right, acquitted) and in the moral sense (living uprightly); the OT&rsquo;s comprehensive term for the person who is in a right relationship with God and others&rsquo;) is the contested status at the heart of Job. The book opens with the divine verdict: Job is tsaddiq (1:1, 8; 2:3 — &lsquo;blameless and upright, one who fears God and turns away from evil&rsquo;). The three friends&rsquo; entire argument rests on the assumption that a tsaddiq cannot suffer like Job is suffering: suffering proves sin; therefore Job is not as tsaddiq as he claims. Job insists: 27:6: &lsquo;I hold fast my righteousness (tsedaqah) and will not let it go; my heart does not reproach me for any of my days.&rsquo; The book&rsquo;s verdict in 42:7-8 vindicates Job: the friends &lsquo;have not spoken of me what is right (nachon)&rsquo; while Job did. This is a radical reversal of the friends&rsquo; retribution theology: the tsaddiq can suffer without it being evidence against his righteousness. The NT&rsquo;s justification (the forensic declaration of tsaddiq-status before God, apart from works) is the systematization of what Job narrates: the person declared righteous before God is righteous — regardless of appearances to the contrary."
        },
        {
            "code": "H410",
            "lemma": "אֵל",
            "translit": "ʾēl",
            "gloss": "God",
            "significance": "אֵל (el, &lsquo;strength; as adjective, mighty; in its theological use, the divine name that emphasizes power and transcendence rather than covenant relationship&rsquo;) is the dominant divine name in Job&rsquo;s dialogue section, and its distribution is theologically deliberate. The prologue and epilogue (chs. 1-2, 42) use YHWH — the intimate covenant name — 32 times. The dialogue section (chs. 3-37) uses El (32×), Eloah (a rare singular form appearing 41× in Job but only 16 times in the rest of the OT), and Shaddai (the Almighty, 31×) overwhelmingly; YHWH appears in the dialogue only 6 times. This distribution mirrors Job&rsquo;s experience: the personal covenant God (YHWH) of his earlier life has been replaced in his experience by the powerful, transcendent, distant El. The YHWH-frame of prologue and epilogue tells the reader that the personal God has never left; Job&rsquo;s dialogue names signal his experiential loss of that intimacy. The resolution in 42:5 — &lsquo;now my eye sees you&rsquo; — restores the personal encounter: the El of the whirlwind is revealed as the YHWH who never abandoned him. The NT&rsquo;s &lsquo;My God, my God, why have you forsaken me?&rsquo; (Matt 27:46) is the Son&rsquo;s cry from within the same divine-absence experience — and the resurrection is the YHWH-restoration."
        },
        {
            "code": "H7879",
            "lemma": "שִׂיחַ",
            "translit": "śîaḥ",
            "gloss": "complaint",
            "significance": "שִׂיחַ (siach, &lsquo;a contemplation; by implication, an utterance — the act of musing, meditating, or speaking freely, often of distress&rsquo;) is the word Job uses for his unbounded lament. 7:13: &lsquo;my couch will ease my complaint (siach)&rsquo;; 10:1: &lsquo;I will give free rein to my complaint (siach); I will speak in the bitterness of my soul.&rsquo; The siach-vocabulary covers the full range from quiet meditation (Ps 119:15: &lsquo;I will meditate [asiach] on your precepts&rsquo;) to anguished complaint (Ps 55:2: &lsquo;attend to me, and answer me; I am restless in my complaint [besiachi]&rsquo;). Job&rsquo;s use of siach establishes his lament as authorized speech — the same kind of musing/utterance that the psalms channel before God. Crucially, God does not rebuke Job for his siach: in 42:7-8, God vindicates Job&rsquo;s speech over the friends&rsquo; pious platitudes. This is the book&rsquo;s strongest pastoral argument: honest siach (complaint, musing, unbounded utterance of distress) before God is more pleasing to him than formulaic reassurances. The Psalter canonizes this with its lament psalms; Job dramatizes it. The NT equivalent is Paul&rsquo;s &lsquo;the Spirit himself intercedes for us with groanings too deep for words&rsquo; (Rom 8:26) — the inarticulable siach carried by the Spirit."
        },
        {
            "code": "H120",
            "lemma": "אָדָם",
            "translit": "ʾādām",
            "gloss": "humanity",
            "significance": "אָדָם (adam, &lsquo;ruddy; a human being, an individual, or the species — humanity; derived from adamah, ground/soil, carrying the connotation of earthliness and creaturely origin&rsquo;) appears in Job&rsquo;s most concentrated reflection on human creatureliness. 14:1: &lsquo;Man (adam) who is born of a woman is few of days and full of trouble (amal); he comes out like a flower and withers; he flees like a shadow and continues not.&rsquo; The adam-imagery in Job is consistently associated with brevity, limitation, and dependence: adam is the creature who comes from adamah and returns to it (Gen 3:19: &lsquo;you are dust, and to dust you shall return&rsquo;). The divine speeches (chs. 38-41) do not refute Job&rsquo;s suffering but situate it: adam&rsquo;s questions arise from within a creation whose scope and complexity he has not seen. 38:26: &lsquo;to bring rain on a land where no adam is&rsquo; — YHWH governs a cosmos that exists independently of human comprehension or consent. The Joban adam-theology is the existential basis for worship: the creature who knows he is adam-from-adamah is the creature who can stand before the El of the whirlwind without demanding equal standing. Psalm 8 fuses adam&rsquo;s lowliness with the divine image-bearing dignity — the tension Job holds throughout."
        },
        {
            "code": "H2820",
            "lemma": "חָשַׂךְ",
            "translit": "ḥāśak",
            "gloss": "withhold",
            "significance": "חָשַׂךְ (chasak, &lsquo;to restrain or refrain; by implication, to refuse, spare, preserve — the act of withholding something from someone, whether from restraint, care, or judgment&rsquo;) appears at crucial boundaries of the book. In the prologue, YHWH&rsquo;s permission to the adversary is bounded: &lsquo;all that he has is in your hand; only against him do not stretch out your hand&rsquo; (1:12; 2:6) — YHWH withholds (chasak) Job&rsquo;s life from the adversary. Job does not know this limit is in place; from inside his suffering it appears that God has given everything over. Job&rsquo;s own refusal to restrain his speech is his most defiant act of trust: 7:11: &lsquo;I will not restrain (chasak) my mouth; I will speak in the anguish of my spirit.&rsquo; The book&rsquo;s pastoral theology of chasak is that God&rsquo;s withholding of protection is never total: there is always a limit — &lsquo;only against him do not stretch out your hand.&rsquo; Paul&rsquo;s &lsquo;God is faithful; he will not let you be tested beyond your ability, but with the testing he will also provide the way of escape&rsquo; (1 Cor 10:13) is the explicit doctrinal formulation of what Job&rsquo;s prologue demonstrates: YHWH&rsquo;s chasak bounds every trial."
        },
        {
            "code": "H1342",
            "lemma": "גָּאָה",
            "translit": "gāʾāh",
            "gloss": "be exalted",
            "significance": "גָּאָה (gaah, &lsquo;to mount up; hence, in general, to rise, to be majestic — of water surging, of the divine majesty ascending, of pride puffing up&rsquo;) appears at the climax of the divine speeches as the word for YHWH&rsquo;s overwhelming transcendence. The great cosmic creatures — Behemoth and Leviathan — symbolize primordial chaos; Leviathan is the chaos-beast par excellence. 41:34: &lsquo;He looks on everything that is high; he is king over all the sons of pride (bene shahats) — he [Leviathan, or YHWH over Leviathan] is exalted (gaah) over all.&rsquo; The gaah of YHWH over the chaos-monster answers Job not with explanation but with display: the God who governs Leviathan is the God who governs Job&rsquo;s suffering. Gaah is the word of the Song of Moses: &lsquo;YHWH is highly exalted (gaah ga&rsquo;ah)&rsquo; (Exod 15:1) — the victory song over Egypt&rsquo;s chaos-waters. The whirlwind speeches achieve their effect through the same gaah-logic: before the display of divine majesty over all creation, Job&rsquo;s rib (lawsuit) is not dismissed but transcended. Job&rsquo;s response in 42:5-6 is not defeat but encounter: &lsquo;now my eye sees you&rsquo; — the gaah that silenced his complaint also gave him what he had wanted throughout: the personal presence of the God he could not locate."
        }
    ],

    "language_notes": (
        "<p>The most linguistically striking feature of Job is its <strong>distribution of divine names</strong>. The prologue and epilogue (chs. 1&ndash;2, 42) use <strong>YHWH</strong> — the intimate covenant name — 32 times. The dialogue section (chs. 3&ndash;37) shifts dramatically: Job and his friends use <strong>El</strong> (mighty/God), <strong>Eloah</strong> (a rare singular form appearing 41 times in Job but only 16 times in all other OT books combined), and <strong>Shaddai</strong> (the Almighty, 31 times), while YHWH appears in the dialogue only 6 times. This distribution is not accident but theology: the narrative frame shows the reader the personal covenant God who is present throughout; the dialogue section shows what the sufferer <em>experiences</em> — a powerful, transcendent, distant El rather than the intimate YHWH of his earlier life. The resolution in 42:5 (&lsquo;now my eye sees you&rsquo;) restores personal encounter without contradicting the dialogue&rsquo;s named distance.</p>"
        "<p>Job has the <strong>highest concentration of hapax legomena</strong> (words appearing only once in the entire Hebrew Bible) of any OT book. Estimates range from 100 to over 150 unique vocabulary items. This extraordinary density suggests deliberate archaic styling — the author reaches into ancient or rare Hebrew to situate Job in a world before Israelite covenant history. The vocabulary includes astronomical terms (Pleiades, Orion, Bear — 38:31-32), obscure words for the mine (28:1-11), and technical language for the primordial waters (38:8-11). The hapax density is one reason Job&rsquo;s translation is the most contested in the Hebrew Bible: almost every paragraph contains words whose meaning is debated. Where translation is uncertain, the English versions often diverge sharply, and the original Hebrew rewards patient attention.</p>"
        "<p>The <strong>legal/forensic vocabulary system</strong> in Job is uniquely developed. The book uses yakah (argue/decide), rib (lawsuit/contention), mishpat (justice/verdict), the noun mokiach (arbiter/one who decides, from yakah), and the legal metaphor of &lsquo;signing one&rsquo;s name to an indictment&rsquo; (31:35) in a sustained legal-literary structure. Scholars debate whether Job belongs to a genre influenced by ancient covenant-lawsuit forms; regardless of formal classification, the forensic metaphor is more developed here than anywhere else in the OT. The irony is structural: Job demands a legal hearing and gets the whirlwind instead — which is the only &lsquo;answer&rsquo; that could actually satisfy, because the problem was not lack of information but lack of encounter.</p>"
        "<p>Job&rsquo;s <strong>poetic structure</strong> makes sustained use of the <em>qinah</em> meter (3+2 beats per bicolon) — the meter of lament, also used in Lamentations — in Job&rsquo;s most anguished speeches. The three dialogue cycles use standard synonymous and antithetical parallelism; the divine speeches shift to catalogue-form (&lsquo;Where were you when I laid the foundations of the earth? Have you entered the storehouses of the snow?&rsquo; — 38:4, 22) — rhetorical question piled on rhetorical question, building an overwhelming sense of divine scope. The contrast between the friends&rsquo; increasingly formal and repetitive poetry and Job&rsquo;s increasingly desperate and inventive poetry is itself part of the argument: Job&rsquo;s language <em>changes</em> under pressure while the friends&rsquo; language grows more rigid.</p>"
    ),

    "reception": (
        "<p><strong>Patristic and Medieval:</strong> No OT book received more sustained patristic attention than Job. Gregory the Great&rsquo;s <em>Moralia in Job</em> (c. 590 AD) runs to 34 books — an exhaustive allegorical and moral commentary that shaped medieval interpretation for centuries. Gregory read Job as a type of Christ: Job&rsquo;s suffering without sin prefigures Christ&rsquo;s passion; the three friends represent heretics who misrepresent God; the whirlwind speeches are the voice of divine transcendence. Chrysostom wrote homilies on Job emphasizing patient endurance. The phrase &lsquo;the patience of Job&rsquo; (James 5:11) shaped patristic and popular reception, sometimes at the expense of Job&rsquo;s most characteristic feature: his sustained, defiant lament.</p>"
        "<p><strong>Reformation:</strong> Calvin preached 159 sermons on Job (1554&ndash;1555) — by far his most sustained treatment of any OT book. He shifted decisively away from allegorical reading toward a literal, theological reading: Job is about the real question of why God allows the righteous to suffer, and the friends represent a false theology of merit-and-reward that Calvin saw as a Protestant polemic target. Calvin took Job&rsquo;s lament seriously as legitimate speech, though he was uncomfortable with the more audacious challenges. Luther found Job troubling — the book&rsquo;s apparent challenge to divine justice made him uneasy — but acknowledged that &lsquo;no one has suffered like Job.&rsquo;</p>"
        "<p><strong>Modern scholarship:</strong> Contemporary scholarship has focused on the Elihu problem (chs. 32&ndash;37 — are they original? They are unannounced in the prologue, ignored in the epilogue, and stylistically distinct), the relationship to ANE wisdom parallels (the &lsquo;Babylonian Job&rsquo; known as <em>Ludlul bel nemeqi</em> and the Egyptian &lsquo;Dialogue of a Man with His Soul&rsquo;), and the question of whether the ending is satisfying. The restoration of Job (42:10-17) — doubled wealth, new children — has seemed to many readers to reinstate the retribution principle the book has just dismantled. Literary readings increasingly argue the ending is intentionally ambiguous rather than a simple reversal; the new children cannot replace the dead ones; the restoration is real but not without remainder.</p>"
    ),

    "reading_guide": (
        "<p>Read the <strong>prologue (chs. 1&ndash;2) as the interpretive key</strong> to everything that follows. Job never learns about the heavenly court scene — his suffering is opaque to him but transparent to the reader. Keeping the prologue in view as you read the dialogues shows you what Job does not know: his suffering is bounded, permitted, not punitive, and held within a purpose he cannot see. Every time Job reaches for God and finds absence, you hold the knowledge that he is seen and known in that absence.</p>"
        "<p>The <strong>three friends are not villains</strong> — they represent the best of conventional wisdom theology, and their arguments are not stupid. Track how each friend&rsquo;s position hardens across the three cycles: Eliphaz begins with gentle suggestion (ch. 4-5) and ends with open accusation (ch. 22); Bildad&rsquo;s speeches grow shorter and more dismissive; Zophar disappears after the second cycle. The progressive breakdown of the friends&rsquo; discourse <em>is</em> their refutation: their theology cannot accommodate real encounter with suffering. Also note that God&rsquo;s rebuke of the friends (42:7) is specifically about speech about God, not cruelty to Job — theology, not pastoral failure, is their indicted sin.</p>"
        "<p>The <strong>whirlwind answer (chs. 38&ndash;41) does not answer Job&rsquo;s question</strong>. &ldquo;Why am I suffering?&rdquo; receives no response. Instead, God asks: &ldquo;Where were you when I laid the foundations of the earth?&rdquo; This is intentional — the book replaces the question &ldquo;why?&rdquo; with the question &ldquo;who?&rdquo; The answer to suffering in Job is not an explanation but a presence: Job encounters the God he had demanded to meet, and that encounter is sufficient. Watch for Job&rsquo;s two responses (40:3-5 and 42:1-6) — they track the stages of encounter: first silence, then transformed sight (&ldquo;now my eye sees you&rdquo;).</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('job')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('job', merged)

main()
