"""
MKT Original Language Commentary — John chapters 3–4
Run: python3 scripts/zc-original-john-3-4.py

Source data used:
- data/interlinear/john.json
- data/translation/glossary-greek.json (disputed terms)
- data/translation/notes/john.json (all verses have token-level data)
- data/translation/draft/mediating/john.json (MKT text for reference)

Key decisions in this range:
- ἄνωθεν (3:3): left untranslated in prose commentary; both meanings ("again" and "from above")
  are active in the narrative — Nicodemus hears "again," the Evangelist means "from above"
- σάρξ (3:6): treated as the natural human realm (not Pauline "sinful nature"), disp=4
- πνεῦμα (3:5, 3:6, 3:8, 3:34, 4:23, 4:24): context-driven; wind/Spirit wordplay in 3:8 is
  deliberate and discussed; capitalized "Spirit" when divine referent is clear
- αἰώνιος (3:15, 3:16, 3:36, 4:14, 4:36): "eternal" as qualitative ("belonging to the age to
  come") not merely quantitative duration; disp=3 — noted where relevant
- ἔργα (3:19–21): "deeds" — not limited to moral acts but the whole orientation of life
- λόγος (4:37, 4:39, 4:41, 4:50): context-determined; "saying" (proverb) in 4:37,
  "word/statement" (Jesus's utterance) in 4:39–50
- ἐγώ εἰμι (4:26): noted as the first explicit self-disclosure in John
- ὁ φίλος τοῦ νυμφίου (3:29): shōshbîn — the specific Jewish role of the bridegroom's
  designated friend/intermediary
- οὕτως (3:16): "in this way" not "so much" — the adverb of manner, not degree
- Source: Ellicott's commentary consulted for philological notes on 3:3, 3:8, 3:13, 3:16
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(source, book):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(source, book, data):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    """Merge new_data into existing without overwriting present entries."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html


JOHN = {
  "3": {
    "1": '<p><strong>ἄρχων τῶν Ἰουδαίων</strong> — <em>archōn tōn Ioudaiōn</em>, "a ruler of the Jews." <em>Archōn</em> designates a member of the Sanhedrin, the supreme Jewish council. Combined with <strong>Φαρισαῖος</strong> (<em>Pharisaios</em>), both identifiers mark Nicodemus as an insider of the religious establishment — the opposite of the fishermen disciples.</p>',

    "2": '<p><strong>νυκτός</strong> (<em>nyktos</em>) — genitive of time, "by night." The Evangelist places this early and does not explain the motive. Whether shame, caution, or a desire for privacy without crowds, the darkness frames a scene that will turn on the contrast between light and dark (3:19–21).</p><p><strong>Ῥαββί</strong> (<em>Rabbi</em>) — "my great one," a title of respect; Nicodemus addresses Jesus as an equal teacher, not yet as a superior. His opening acknowledgment — "we know you are a teacher come from God" — is accurate but incomplete: the Evangelist has already identified Jesus as far more.</p>',

    "3": '<p><strong>ἄνωθεν</strong> (<em>anōthen</em>) — the hinge word of the dialogue. The term means both "again" (temporal, a second time) and "from above" (spatial/theological, from heaven). Nicodemus hears the temporal sense in v.4; the Evangelist intends the theological sense throughout. The ambiguity is not a translation problem but a literary device the Evangelist uses to expose the gap between what Jesus says and what a listener embedded in the natural realm can hear.</p><p><strong>ἰδεῖν τὴν βασιλείαν τοῦ θεοῦ</strong> — "to see the kingdom of God." The verb is <em>horaō</em> (aorist infinitive), perception and experience rather than mere observation. The kingdom is not yet entered; it is first seen — a claim that will be sharpened in v.5.</p>',

    "4": '<p><strong>δεύτερον</strong> (<em>deuteron</em>) — "a second time." Nicodemus has taken ἄνωθεν as "again" (temporal) and pushed it to its most literal extreme: physical re-entry into the womb. His question is not ridicule but genuine incomprehension — he is working with only one semantic register of the word Jesus used.</p><p><strong>γέρων ὤν</strong> (<em>gerōn ōn</em>) — "being old." The present participle concedes his own situation: the natural impossibility is compounded by age. Nicodemus frames the question in terms of biological limits, which is exactly what Jesus\'s answer will transcend.</p>',

    "5": '<p><strong>ἐξ ὕδατος καὶ πνεύματος</strong> — "of water and Spirit." No article before either noun; the Greek pairs them as complementary agents of the new birth, not as two separate acts. The pairing has generated debate: water as physical birth (amniotic fluid), water as baptism, or water as cleansing/purification imagery from Ezek 36:25–27, which pairs water-washing with the gift of Spirit. The Ezekiel background is strong given the rebuke in v.10 ("you are Israel\'s teacher").</p><p><strong>εἰσελθεῖν εἰς τὴν βασιλείαν τοῦ θεοῦ</strong> — "to enter the kingdom of God." The step from "see" (v.3) to "enter" (v.5) is progression: perception precedes participation. The kingdom requires a specific mode of entry.</p>',

    "6": '<p><strong>σάρξ</strong> (<em>sárx</em>, G4561, dispute level 4) — "flesh." Here σάρξ designates the natural human realm: all that is generated by human origin and human capacity. It is not yet Paul\'s term for the sin-power (as in Rom 8); in John\'s usage it denotes creatureliness and finitude. The chiastic structure is deliberate: "born of flesh / is flesh; born of Spirit / is spirit" — the new birth does not repair the old nature but introduces a categorically different origin.</p><p><strong>τὸ γεγεννημένον ἐκ τοῦ πνεύματος</strong> — "that which has been born of the Spirit." The perfect passive participle <em>gegenēmenon</em> marks the completed new birth with ongoing effect: the person so born carries that origin permanently.</p>',

    "7": '<p><strong>ὑμᾶς</strong> (<em>hymas</em>) — the pronoun shifts to plural: "you [all] must be born again." Jesus has been addressing Nicodemus individually; the plural extends the necessity beyond this one teacher to all. The individual encounter opens into a universal claim.</p><p><strong>δεῖ</strong> (<em>dei</em>) — "it is necessary." The impersonal verb of divine necessity appears repeatedly in John for what must happen according to God\'s purpose (cf. 4:4; 10:16; 20:9). The new birth is not optional or aspirational.</p>',

    "8": '<p><strong>τὸ πνεῦμα</strong> (<em>to pneuma</em>) — the key wordplay: the same Greek word means both "wind" and "Spirit." Jesus is not using an analogy where wind illustrates Spirit; the same word carries both meanings simultaneously. The verb <strong>πνεῖ</strong> (<em>pnei</em>, "blows") shares the same root as πνεῦμα — "the spirit/wind spirits/blows where it wills." The invisibility of the wind\'s origin and destination mirrors the Spirit\'s freedom and inscrutability.</p><p><strong>τὴν φωνὴν αὐτοῦ ἀκούεις</strong> — "you hear its/his voice." <em>Phōnē</em> properly means "voice" rather than merely "sound." The sentence works for wind (audible gusting) and for the Spirit (the voice that the born-again person hears). The translation settles for one referent; the Greek holds both.</p>',

    "9": '<p>Nicodemus\'s response is a bare question: <strong>Πῶς</strong> (<em>Pōs</em>) — "How?" He offers no objection to the substance of what Jesus says, only incomprehension of the mechanism. The question is honest, not combative. Jesus\'s reply (v.10) does not answer the "how" but redirects to the authority behind the teaching.</p>',

    "10": '<p><strong>ὁ διδάσκαλος τοῦ Ἰσραήλ</strong> — "the teacher of Israel." Both articles are present: not "a teacher" but the teacher, a recognized authoritative figure in the community. The rebuke is gentle but pointed: someone in this role should recognize the categories Jesus is using — they come from Israel\'s own prophetic texts (Ezek 36; Jer 31).</p>',

    "11": '<p><strong>ἡμεῖς</strong> / <strong>ἡμῶν</strong> — "we" / "our." Jesus uses the first-person plural: "we speak of what we know." The shift has puzzled interpreters — does Jesus speak as one voice of a group? Some read the plural as Jesus identifying with the prophetic tradition; others as Jesus speaking as the divine community (Father and Son). The contrast with the plural "you [all]" in the next clause indicates the Evangelist may be addressing the unbelieving audience of his own time through Jesus\'s words.</p>',

    "12": '<p><strong>τὰ ἐπίγεια</strong> / <strong>τὰ ἐπουράνια</strong> — "earthly things" / "heavenly things." The contrast is spatial and also epistemological: earthly things that can be grasped by natural analogy (birth, wind) have already exceeded Nicodemus\'s comprehension. Heavenly things — the descent of the Son, the giving of the Spirit, the mechanics of new birth from above — will be even harder. Jesus names his own restraint in the teaching.</p>',

    "13": '<p><strong>ἀναβέβηκεν</strong> (<em>anabebēken</em>) — perfect tense: "has ascended." The perfect in Greek denotes a past action with a persisting present state. The claim is paradoxical: the one speaking of heavenly things is the one who has "already ascended" — the human perspective on someone who descended from above is that they carry with them the knowledge only ascent could bring.</p><p><strong>ὁ ὢν ἐν τῷ οὐρανῷ</strong> — "who is/being in heaven." This participial phrase ("the one being in heaven") is absent in some early manuscripts (Sinaiticus, Vaticanus). If original, it asserts the Son\'s continuing heavenly reality even while incarnate — a high Christological claim. Its presence or absence does not change the main point but affects how one reads the nature of the Incarnation.</p>',

    "14": '<p><strong>ὑψωθῆναι</strong> (<em>hypsōthēnai</em>) — the aorist passive infinitive of <em>hypsoō</em>: "to be lifted up." This is the first of three Johannine "lifting up" sayings (cf. 8:28; 12:32). The verb does double work: it refers to the physical elevation of crucifixion and simultaneously to exaltation/glorification. The Evangelist does not separate these — in John, the cross is not a defeat requiring a subsequent resurrection vindication; it is itself the moment of glorification.</p><p><strong>καθώς...οὕτως</strong> (<em>kathōs...houtōs</em>) — "just as...so." The comparison establishes a structural parallel: the bronze serpent lifted up in the wilderness (Num 21:8–9) provided physical rescue by looking; the Son lifted up provides eternal life by believing. The καθώς introduces the type; the οὕτως the fulfillment.</p>',

    "15": '<p><strong>ἵνα πᾶς ὁ πιστεύων ἐν αὐτῷ ἔχῃ ζωὴν αἰώνιον</strong> — the prepositional phrase <em>ἐν αὐτῷ</em> ("in him") is syntactically ambiguous: it can modify either "everyone believing in him" or "have life in him." Most translations attach it to the participle (believing in him), but the phrasing in 3:16 — which omits ἐν αὐτῷ — suggests the Evangelist may intend both: belief is directed toward him AND life is located in him.</p><p><strong>ζωὴν αἰώνιον</strong> (<em>zōēn aiōnion</em>, dispute level 2+3) — "eternal life." <em>Aiōnios</em> (disp=3) derives from <em>aiōn</em> (the age, era); the phrase denotes "the life of the coming age" — qualitative first (the kind of life God has; the life of the new creation), quantitative second (endless). The Evangelist will use this phrase seventeen times; it is never merely longevity.</p>',

    "16": '<p><strong>οὕτως</strong> (<em>houtōs</em>) — "in this way," not "so much" or "so greatly." The adverb is of manner, not degree: God loved the world <em>in this manner</em> — namely, by giving the Son. The manner of the love is its measure.</p><p><strong>ἠγάπησεν</strong> (<em>ēgapēsen</em>, aorist) — the giving of the Son is narrated as a single completed historical act, not an ongoing disposition. God did not merely maintain affection; there was a moment of definitive action.</p><p><strong>μονογενῆ</strong> (<em>monogenē</em>) — "only-born," from <em>monos</em> (only) and <em>gennaō</em> (to beget). The word carries both uniqueness and relational weight: what is given is irreplaceable, and the giving is costly precisely because the relationship being risked is the closest conceivable.</p><p><strong>ἵνα μὴ ἀπόληται</strong> — purpose clause with the subjunctive of <em>apollymi</em>: "so that he might not perish." Perishing (<em>apollymi</em>) is the alternative state — not punishment freshly imposed, but the destination of those already on the road of judgment (see v.18). The purpose of the giving is rescue from an existing trajectory.</p>',

    "17": '<p><strong>οὐ γὰρ ἀπέστειλεν...ἵνα κρίνῃ</strong> — "for he did not send...in order to judge." The purpose clause with the subjunctive negates the judicial mission. <em>Krinō</em> (to judge/condemn) and <em>sōzō</em> (to save/rescue) are placed in explicit contrast. The world\'s condemnation is not new — it is the default state (v.18); the mission is to provide a way out of it, not to add to it.</p>',

    "18": '<p><strong>κέκριται</strong> (<em>kekritai</em>) — perfect passive: "has been judged and remains judged." The judgment on the unbeliever is not a future verdict but a present state — Johannine realized eschatology. Belief un-condemns (<em>ou krinetai</em>, present: "is not being judged"); unbelief leaves the person in an already-existing condition of condemnation.</p><p><strong>ὅτι μὴ πεπίστευκεν</strong> — "because he has not believed" (perfect indicative): the present state of un-belief is the grounds for the present state of condemnation. The perfect tense marks a settled posture, not a momentary failure.</p>',

    "19": '<p><strong>αὕτη δέ ἐστιν ἡ κρίσις</strong> — "and this is the verdict." <em>Krisis</em> is "verdict/judgment," not merely "crisis." The Evangelist uses the singular feminine article with the neuter noun φῶς (<em>phōs</em>, light): the verdict is the arrival of Light into the world and the human response to it.</p><p><strong>ἠγάπησαν...τὸ σκότος</strong> — "they loved darkness." The verb is the same (<em>agapaō</em>) used of God\'s love in v.16: humans "loved" darkness rather than light. The use of agapē-love for the wrong object makes the indictment precise — it is not ignorance but an orientation of affection.</p>',

    "20": '<p><strong>ὁ φαῦλα πράσσων</strong> — "everyone who practices evil things." <em>Prassō</em> (to practice/do habitually) contrasts with <em>poieō</em> (to do an act). The one who <em>practices</em> evil has a settled pattern, not just an occasional failure. This habitual orientation is what drives the avoidance of light.</p><p><strong>ἐλεγχθῇ</strong> (<em>elenkhthē</em>) — "might be exposed/convicted." The word can mean both "to expose" (reveal what was hidden) and "to convict" (demonstrate guilt). The one who avoids the light fears both: disclosure of what they have done AND the verdict that follows disclosure.</p>',

    "21": '<p><strong>ὁ δὲ ποιῶν τὴν ἀλήθειαν</strong> — "the one doing the truth." "Doing truth" (<em>poiōn tēn alētheian</em>) is a Semitic idiom (Hebrew: <em>ʿāśâ ʾĕmet</em>) meaning to act faithfully, with integrity — not merely asserting propositions but living in alignment with reality. The idiom surfaces in the Dead Sea Scrolls as well as the LXX.</p><p><strong>ἵνα φανερωθῇ αὐτοῦ τὰ ἔργα</strong> — "that his deeds might be manifested." <em>Phaneroō</em> (to make manifest/visible) is a key Johannine verb for revelation. The one who "does truth" comes to the light not despite their deeds but because they welcome the deeds\' disclosure; they have nothing to hide from God\'s light.</p>',

    "22": '<p>A narrative transition. <strong>μετὰ ταῦτα</strong> (<em>meta tauta</em>) — "after these things" — a loose temporal marker the Evangelist uses frequently. The focus shifts from the Nicodemus dialogue to Jesus\'s ministry in Judaea alongside John\'s continuing work.</p>',

    "23": '<p><strong>Αἰνών</strong> (<em>Ainōn</em>) and <strong>Σαλείμ</strong> (<em>Saleim</em>) — exact location unknown; "Aenon" likely derives from the Aramaic for "springs." The geographic notice "because there was much water there" confirms that John\'s baptism required immersion or at least significant water — a detail with implications for the mode of baptism, though the text does not develop it theologically.</p>',

    "24": '<p>A parenthetical note: John\'s ministry is concurrent with Jesus\'s, not sequentially complete. The Synoptics present John\'s imprisonment before Jesus\'s main Galilean ministry (Mark 1:14), which creates a chronological question the Evangelist does not address. The note simply establishes that both are active at the same time.</p>',

    "25": '<p><strong>ζητήσεως</strong> (<em>zētēseōs</em>) — "question/dispute/inquiry." The term can mean a formal disputation or an argument. It arises <strong>περὶ καθαρισμοῦ</strong> (<em>peri katharismou</em>) — "concerning purification/cleansing." Some manuscripts read "a Jew" (singular) rather than "Jews" (plural) as the other party. The topic — ritual purification — connects John\'s baptism to Jewish purity concerns and frames the question that John\'s disciples bring in v.26.</p>',

    "26": '<p><strong>μαρτυρεῖς</strong> (<em>martyreis</em>) — "you testified" (perfect force in context). John\'s own testimony about Jesus is now being cited against him: the crowds are going to the one John endorsed. The disciples\' framing treats this as a problem; John\'s response in vv.27–30 treats it as completion.</p>',

    "27": '<p><strong>οὐ δύναται ἄνθρωπος λαμβάνειν οὐδὲν</strong> — "a person cannot receive anything." The statement is universal: every role, gift, and sphere of influence is assigned from heaven. John does not claim he could have more; he asserts that what he has is precisely and completely what he was given.</p><p><strong>δεδομένον</strong> (<em>dedomenon</em>) — perfect passive participle: "given and remaining given" — the gift from heaven is not provisional but permanent. John cannot exceed the assignment, and he has no desire to.</p>',

    "28": '<p><strong>οὐκ εἰμί ἐγὼ ὁ Χριστός</strong> — "I am not the Messiah." John uses the strong negation to recall his own earlier testimony (1:20). The contrast is sharp: "I am not" (John) vs. the "I am he" of Jesus in 4:26. John defines himself by negation; Jesus by self-disclosure.</p>',

    "29": '<p><strong>ὁ φίλος τοῦ νυμφίου</strong> — "the friend of the bridegroom." In Jewish custom, the <em>shōshbîn</em> was a designated intermediary who arranged the marriage, carried messages between bride and groom, and at the wedding stood with the bridegroom. His role was complete when the bridegroom arrived. John describes his own ministry in precisely these terms: he arranged the meeting; the bridegroom is here.</p><p><strong>χαρᾷ χαίρει</strong> (<em>charā chairei</em>) — a cognate dative: "rejoices with joy." The construction is emphatic, idiomatic in Greek for the intensity of an emotion. John\'s joy at Jesus\'s ascendancy is not resigned but fully realized. <strong>πεπλήρωται</strong> (<em>peplērōtai</em>, perfect passive) — "has been filled up/completed" — the joy is already full, not anticipated.</p>',

    "30": '<p><strong>αὐξάνειν</strong> (<em>auxanein</em>, present) / <strong>ἐλαττοῦσθαι</strong> (<em>elattousthai</em>, present) — both present infinitives of ongoing processes: "he must keep increasing; I must keep decreasing." The present tense captures a continuous trajectory rather than a single moment. The necessity (<em>dei</em>, "must") is the same divine compulsion as in 3:7 and 4:4.</p>',

    "31": '<p><strong>ὁ ἄνωθεν ἐρχόμενος</strong> — "the one coming from above." Now <em>anōthen</em> (the same word as 3:3) is used explicitly of Jesus\'s heavenly origin — confirming the Evangelist\'s intended meaning in the Nicodemus dialogue. The one who comes <em>from above</em> is above all; the one who is <em>from the earth</em> can only speak from within the limits of earth.</p><p><strong>ἐπάνω πάντων ἐστίν</strong> — "is above all." The phrase appears twice for emphasis. The superiority is ontological, not merely positional.</p>',

    "32": '<p><strong>ὃ ἑώρακεν καὶ ἤκουσεν</strong> — "what he has seen and heard." The perfect and aorist combine: ongoing seeing (perfect <em>heōraken</em>) plus completed hearing (aorist <em>ēkousen</em>). The testimony of the one from above is grounded in direct personal knowledge, not report or inference.</p><p><strong>καὶ τὴν μαρτυρίαν αὐτοῦ οὐδεὶς λαμβάνει</strong> — "and no one receives his testimony." The absolute statement will be qualified in v.33 ("whoever has received it"). The "no one" is hyperbolic — the same rhetorical sweep as "all are going to him" in v.26 — expressing the scale of rejection, not its totality.</p>',

    "33": '<p><strong>ἐσφράγισεν</strong> (<em>esphragisen</em>) — "has sealed/certified." To seal something was to authenticate it, confirming its validity by one\'s own authority. Whoever accepts the testimony of the Son has by that act certified (<em>set their seal to</em>) the truthfulness of God: they have staked their own credibility on God\'s.</p>',

    "34": '<p><strong>οὐ γὰρ ἐκ μέτρου δίδωσιν τὸ πνεῦμα</strong> — "for not by measure does he give the Spirit." The subject is unstated and debated. In context, "he" most naturally refers to God giving the Spirit to the Son (cf. 1:32–33: "I saw the Spirit descending and remaining on him"). The absence of measure signals completeness — the Spirit is not rationed. Contrast the idea that prophets received the Spirit only in measure or for specific tasks.</p>',

    "35": '<p><strong>δέδωκεν</strong> (<em>dedōken</em>, perfect) — "has given and continues to entrust." The perfect tense marks the Father\'s delegation as a settled, present reality: the authority is already in the Son\'s hand and remains there. <strong>εἰς τὴν χεῖρα</strong> — "into the hand" — a Semitic idiom for authority and stewardship (cf. Ps 8:6 LXX).</p>',

    "36": '<p><strong>ἀπειθῶν</strong> (<em>apeithōn</em>, present participle) — "the one who disobeys/disbelieves." The word combines <em>a-</em> (not) and <em>peithō</em> (to persuade, to comply). Unbelief in John is not merely intellectual non-assent but active refusal, closer to disobedience than mere uncertainty. The present tense marks it as an ongoing posture.</p><p><strong>ἡ ὀργὴ τοῦ θεοῦ μένει ἐπ᾽ αὐτόν</strong> — "the wrath of God remains on him." <em>Menō</em> (to remain/abide) is a key Johannine word. The wrath is not newly imposed on the unbeliever; it already rests on humanity apart from Christ. It does not arrive; it stays. This is the same structure as the condemnation in v.18: the default state is under wrath, and faith moves one out of it — not into wrath.</p>'
  },
  "4": {
    "1": '<p><strong>ὡς οὖν ἔγνω</strong> — "when therefore he learned." The aorist <em>egnō</em> (knew/learned) raises the question of how Jesus learned — through normal information channels or divine knowledge. The Evangelist does not specify; the verse functions primarily to explain the transition from Judaea to Galilee via Samaria.</p>',

    "2": '<p>A parenthetical correction: <strong>καίτοιγε Ἰησοῦς αὐτὸς οὐκ ἐβάπτιζεν</strong> — "although Jesus himself was not baptizing." The Evangelist corrects the report the Pharisees had received: the disciples baptized, not Jesus personally. The correction preserves the distinction between Jesus\'s unique baptism (with the Spirit, 1:33) and his disciples\' water baptism.</p>',

    "3": '<p>A simple transitional narrative verse: Jesus leaves Judaea and returns to Galilee. The departure is motivated by the Pharisees\' attention (v.1), but the route chosen (v.4) will prove purposeful.</p>',

    "4": '<p><strong>ἔδει δὲ αὐτὸν διέρχεσθαι διὰ τῆς Σαμαρείας</strong> — "it was necessary for him to pass through Samaria." <strong>ἔδει</strong> (<em>edei</em>) is the imperfect of <em>dei</em> — the impersonal verb of divine necessity. Geographically, a Jew traveling from Judaea to Galilee could route through Peraea east of the Jordan to avoid Samaria. The "necessity" is therefore not geographical but theological: the encounter to come was divinely appointed.</p>',

    "5": '<p><strong>Συχάρ</strong> (<em>Sychar</em>) — the town, possibly Shechem or a nearby village. The note that Jacob gave the plot of land to his son Joseph (Gen 48:21–22; Josh 24:32) establishes the patriarchal depth of the site. The well has been in continuous use for over a millennium; Jesus asks for water at a place saturated with covenant history.</p>',

    "6": '<p><strong>κεκοπιακώς</strong> (<em>kekopiakōs</em>, perfect participle) — "having labored and remaining weary." The perfect tense preserves the weariness as an ongoing state at the moment Jesus sat down. The Incarnation is depicted without softening: the Word-made-flesh sits exhausted by travel, thirsty, in need of rest.</p><p><strong>ὡσεὶ ἕκτη</strong> — "about the sixth hour" — approximately noon by Roman reckoning (counting from midnight or dawn). The midday heat explains why no other women are at the well — an observation that makes the Samaritan woman\'s arrival conspicuous.</p>',

    "7": '<p><strong>Δός μοι πεῖν</strong> — "Give me [something] to drink." A simple imperative, bare and direct. A Jewish man addressing an unknown Samaritan woman in public was a social violation on multiple fronts (gender, ethnicity, purity concerns). Jesus initiates without preamble, which is itself the first thing that arrests the woman\'s attention.</p>',

    "8": '<p>A parenthetical explanation removing the disciples from the scene. <strong>ἀγοράσωσιν τροφάς</strong> — "to buy food." The disciples\' absence is practical narrative: it leaves Jesus and the woman alone for the exchange that follows, and it creates the context for v.31–38 when the disciples return.</p>',

    "9": '<p><strong>Ἰουδαῖος ὤν</strong> — "being a Jew." The woman identifies him by appearance, speech, or dress. The narrator\'s parenthesis clarifies: <strong>οὐ γὰρ συγχρῶνται Ἰουδαῖοι Σαμαρίταις</strong> — "for Jews do not share/associate with Samaritans." <em>Sygchraomai</em> can mean "use together" (the same vessels) or "associate with" broadly. The purity concern was real: Samaritans were regarded by many Jewish authorities as permanently impure.</p>',

    "10": '<p><strong>δωρεά</strong> (<em>dōrea</em>) — "free gift." A specific Greek word for an unearned, unmerited grant — it is the same word used in Rom 5:15–17 and Eph 2:8 for the grace-gift of salvation. If she had known what kind of gift was on offer, the direction of the request would have reversed.</p><p><strong>ὕδωρ ζῶν</strong> (<em>hydōr zōn</em>) — "living water." In contemporary usage, "living water" meant flowing spring water (as opposed to cistern water). The woman hears this natural meaning in v.11. Jesus means the Spirit (7:38–39), which is the "living water" that quenches permanently.</p>',

    "11": '<p><strong>ἄντλημα</strong> (<em>antlēma</em>) — "a vessel for drawing/a bucket." The woman notes the practical obstacle: the well is deep (<em>bathys</em>), Jesus has no equipment, and he is offering living (flowing) water. Her logic is sound on the literal level — the mismatch between the offer and the means is the setup for Jesus\'s clarification of what kind of water he means.</p>',

    "12": '<p><strong>μὴ σύ μείζων εἶ</strong> — "You are not greater than...are you?" The particle <em>mē</em> expects a negative answer: surely he cannot be greater than Jacob? The irony the Evangelist builds here is dense — Jacob gave this well; Jesus is about to offer something Jacob never could. The woman\'s question is more accurate than she knows.</p>',

    "13": '<p><strong>πᾶς ὁ πίνων ἐκ τοῦ ὕδατος τούτου</strong> — "everyone who drinks from this water." The present participle <em>pinōn</em> ("drinking") marks ongoing thirst: drinking from this well is an endless cycle. Physical water satisfies temporarily; <em>dipsēsei palin</em> — "will thirst again" — is the inevitable return.</p>',

    "14": '<p><strong>ἁλλομένου εἰς ζωὴν αἰώνιον</strong> — "welling up/springing up to eternal life." <em>Hallomai</em> (to spring/leap/well up) is a vivid present participle — the water in the person is not static but actively surging upward. The word is used of the lame man\'s leaping in Acts 3:8. The image is not of a placid reservoir but a living, mobile force within the person.</p><p><strong>ζωὴν αἰώνιον</strong> — "eternal life" (disp 2+3). The phrase is now applied to the internal gift: the living water transforms into the life of the age to come within the one who receives it.</p>',

    "15": '<p>The woman\'s response is still literal: <strong>ἵνα μὴ διψῶ μηδὲ ἔρχωμαι ἐνθάδε ἀντλεῖν</strong> — "so that I may not thirst nor come here to draw." She grasps the convenience of the offer — no more daily trips to the well — without yet grasping what is being offered. The misunderstanding is not foolish; it follows naturally from her frame of reference. The Evangelist uses it to continue the dialogue toward deeper disclosure.</p>',

    "16": '<p><strong>Ὕπαγε φώνησον τὸν ἄνδρα σου</strong> — "Go, call your husband." The abrupt command shifts the subject without explanation. Jesus moves from abstract teaching to specific personal knowledge. The imperative is plain; what follows will reveal that Jesus already knows the answer to his own request.</p>',

    "17": '<p><strong>ἄνδρα οὐκ ἔχω</strong> — "I have no husband." A technically accurate statement, as Jesus immediately confirms: <strong>καλῶς εἶπες</strong> — "you have spoken well/rightly." The MKT renders this affirmation literally. Jesus validates her evasion by exploiting its precise truth to expose what it conceals.</p>',

    "18": '<p><strong>πέντε γὰρ ἄνδρας ἔσχες</strong> — "for you have had five husbands." The aorist <em>eshes</em> covers the past; the present <em>echeis</em> covers the current situation. The present partner (<strong>ὃν νῦν ἔχεις</strong>) is not her husband. The statement is factual, not condemnatory in tone — Jesus does not rebuke her but simply names reality. Whatever the causes of the five marriages (death, divorce, abandonment), the disclosure establishes that Jesus possesses knowledge he could not naturally have.</p>',

    "19": '<p><strong>θεωρῶ ὅτι προφήτης εἶ σύ</strong> — "I perceive that you are a prophet." <em>Theōreō</em> ("to observe, discern") marks a step in her understanding — she moves from "a Jew" (v.9) to "a prophet" (v.19). The Samaritan tradition expected a prophet like Moses (Deut 18:15–18) called the Taheb. Her next move — the worship question (v.20) — is what one would naturally bring to a prophet.</p>',

    "20": '<p><strong>ἐν τῷ ὄρει τούτῳ</strong> — "on this mountain." Gerizim, the sacred mountain of the Samaritans where they had their own temple until it was destroyed by John Hyrcanus in 128 BC. The dispute between Samaritans and Jews over the correct place of worship (Gerizim vs. Jerusalem) was ancient and bitter. She brings the defining theological question of her community to the one she has identified as a prophet.</p>',

    "21": '<p><strong>ἔρχεται ὥρα</strong> — "the hour is coming." The Johannine eschatological formula. Unlike in v.23 where it is doubled with <em>kai nyn estin</em> ("and now is"), here v.21 states only the future aspect: worship will no longer be location-bound. The worship dispute between Gerizim and Jerusalem will become irrelevant.</p>',

    "22": '<p><strong>ὑμεῖς προσκυνεῖτε ὃ οὐκ οἴδατε</strong> — "you worship what you do not know." The bluntness is deliberate. Samaritan worship used only the Pentateuch and had a truncated knowledge of Israel\'s history of revelation. <strong>ἡμεῖς προσκυνοῦμεν ὃ οἴδαμεν</strong> — "we worship what we know." Jesus identifies with the Jewish tradition of revelation: <strong>ἡ σωτηρία ἐκ τῶν Ἰουδαίων ἐστίν</strong> — "salvation is from the Jews." The definite article before <em>Ioudaiōn</em> makes the claim specific: the history of covenant, Scripture, and Messiah runs through Israel.</p>',

    "23": '<p><strong>ἐν πνεύματι καὶ ἀληθείᾳ</strong> — "in Spirit and truth." Both nouns are anarthrous (no article), marking them as qualitative — the mode of the new worship. The preposition <em>en</em> indicates the medium or sphere: worship occurs within the Spirit and within truth, not at a location. <em>Alētheia</em> (truth) in John is not a generic virtue but the revelation that Christ himself embodies (14:6: "I am the truth"). Worship in truth is worship aligned with who Christ is.</p><p><strong>καὶ γὰρ ὁ πατὴρ τοιούτους ζητεῖ τοὺς προσκυνοῦντας αὐτόν</strong> — "for the Father seeks such worshipers." <em>Zēteō</em> (to seek, to look for) applied to the Father is remarkable: the Father is the one actively pursuing the worshipers, not merely the object they must find. The initiative is divine.</p>',

    "24": '<p><strong>πνεῦμα ὁ θεός</strong> — word order in Greek: "Spirit [is] God." The predicate (<em>pneuma</em>) precedes the subject (<em>ho theos</em>). By Colwell\'s rule, an anarthrous predicate noun preceding the verb tends to be definite: "God is [the kind of being who is] Spirit." Not "a spirit" among others, but Spirit as the ontological category that defines what God is — without physical form, without location-dependence, not contained by temples built with hands.</p><p>This statement grounds the demand for Spirit-and-truth worship: since God himself is Spirit, worship that is geographical, material, or merely external is fundamentally mismatched to the one being worshiped.</p>',

    "25": '<p><strong>Μεσσίας</strong> (<em>Messias</em>) — the transliteration of the Hebrew/Aramaic <em>Māšīaḥ</em> (anointed one); the narrator glosses it as <em>Christos</em>. The Samaritan expectation of a coming figure called the Taheb ("the restorer" or "the returning one") was based on Deut 18:15–18. She reaches for the highest category available to her: the coming one will clarify everything. This sets up Jesus\'s declaration in v.26 as a direct answer to that expectation.</p>',

    "26": '<p><strong>ἐγώ εἰμι</strong> (<em>egō eimi</em>) — "I am [he]." The explicit "I" (<em>egō</em>) is redundant in Greek (the verb already includes the subject) and therefore emphatic. This is the first time in John that Jesus explicitly identifies himself as the Messiah — and he says it not to the Sanhedrin or his disciples but to a Samaritan woman at a well. The self-disclosure is unguarded and complete: "I, the one speaking to you — I am he." No parable, no riddling language.</p>',

    "27": '<p><strong>ἐθαύμαζον</strong> (<em>ethaumazon</em>, imperfect) — "they were marveling/kept marveling." The disciples\' surprise is ongoing. <strong>μετὰ γυναικός</strong> — "with a woman." The prohibition in rabbinic sources was against prolonged conversation with women in public, particularly unknown women. The disciples\' silence (<em>oudeis</em> asked) is itself noteworthy — they perceived that a challenge to Jesus would be out of place.</p>',

    "28": '<p><strong>ἀφῆκεν τὴν ὑδρίαν αὐτῆς</strong> — "she left her water jar." The detail is small and vivid: she came to draw water and leaves without it. The jar represents the purpose she came with; she departs with something else entirely. The practical forgetfulness signals that she is now occupied with something more urgent than the errand she came for.</p>',

    "29": '<p><strong>ὃς εἶπέν μοι πάντα ἃ ἐποίησα</strong> — "who told me everything I ever did." The claim is rhetorically shaped for maximum effect — "everything I did" is the village\'s way of hearing what was actually a targeted disclosure about her marriages. She reports the encounter in terms that will be maximally compelling to others.</p><p><strong>μήτι οὗτός ἐστιν ὁ Χριστός;</strong> — "Could this be the Messiah?" The particle <em>mēti</em> introduces a question that expects a hesitant or negative answer, but invites the listener to consider the positive. She does not proclaim; she raises the question and lets the townspeople investigate. Her testimony is framed as a possibility, not a certainty — honest to her own incomplete understanding.</p>',

    "30": '<p>A simple narrative verse. <strong>ἐξῆλθον</strong> (aorist, "they went out") / <strong>ἤρχοντο</strong> (imperfect, "they were coming") — the sequence shows the townspeople responding immediately and approaching. The imperfect of continuous movement sets the scene for the harvest imagery in vv.35–38: the fields (of people) are already moving toward Jesus.</p>',

    "31": '<p><strong>ἠρώτων</strong> (<em>ērōtōn</em>, imperfect) — "kept asking/urging." The disciples\' persistent request ("Rabbi, eat") sets up the discourse on a different kind of food (vv.32–38), just as the woman\'s misunderstanding of water set up the discourse on living water.</p>',

    "32": '<p><strong>βρῶσιν φαγεῖν ἣν ὑμεῖς οὐκ οἴδατε</strong> — "food to eat that you do not know about." <em>Brōsis</em> is a general term for food/eating. Jesus does not explain immediately, allowing the disciples\' confusion in v.33 to frame the explanation in v.34. The pattern mirrors the misunderstandings with Nicodemus and the Samaritan woman: natural category → literal misunderstanding → theological disclosure.</p>',

    "33": '<p>The disciples\'s question to one another — "could someone have brought him food?" — is not stupid; it is the only natural reading of what Jesus said. The Evangelist uses their misunderstanding as a foil to make Jesus\'s answer in v.34 stand out as the correction.</p>',

    "34": '<p><strong>ἐμὸν βρῶμά ἐστιν ἵνα ποιήσω τὸ θέλημα τοῦ πέμψαντός με</strong> — "my food is to do the will of the one who sent me." Doing the Father\'s will is what sustains Jesus — the metaphor of food for what nourishes and energizes.</p><p><strong>τελειώσω αὐτοῦ τὸ ἔργον</strong> — "and to complete his work." <em>Teleioō</em> (to complete, perfect, bring to its end) anticipates the cross cry of 19:30: <em>τετέλεσται</em> ("it is finished/completed"). The work the Father sent him to do is not yet complete at Sychar — but the verb points toward its ultimate fulfillment.</p>',

    "35": '<p><strong>λευκαί εἰσιν πρὸς θερισμόν</strong> — "they are white/ripe for harvest." The present tense: the harvest is already here. The proverb ("four months until harvest") belongs to the natural agricultural cycle; Jesus inverts the timeline. As the Samaritans approach across the fields (visible to the disciples), they are the illustration: the mission-harvest does not wait for a future season.</p><p><strong>ἐπάρατε τοὺς ὀφθαλμοὺς ὑμῶν</strong> — "lift up your eyes." The aorist imperative demands immediate, decisive looking. Physical sight of what is coming (the Samaritans) corresponds to spiritual perception of what the approach means.</p>',

    "36": '<p><strong>καρπὸν εἰς ζωὴν αἰώνιον</strong> — "fruit for eternal life." The harvest metaphor shifts from grain to the produce of mission: people gathered into the life of the age to come. The sower and reaper rejoicing together (<em>hina...chairē</em>) anticipates the unity of mission across generations.</p>',

    "37": '<p><strong>ὁ λόγος ἐστὶν ἀληθινός</strong> — "the saying is true." Here <em>logos</em> (disp=3) functions as "proverb" or "saying" — existing wisdom being quoted and affirmed. The word is not the divine Logos of 1:1 but the human category of received wisdom. The proverb ("one sows and another reaps") is being applied to the mission context: those who prepared Israel received no harvest; those sent now will reap from prior labor.</p>',

    "38": '<p><strong>κεκοπιάκασιν</strong> (<em>kekopiākasin</em>, perfect) — "have labored [and their labor remains]." The perfect tense preserves the prior workers\' effort as an ongoing legacy. Who are the others? The prophets of Israel, John the Baptist, perhaps Jesus himself in the preceding Samaritan encounter. The disciples inherit fruit they did not plant.</p>',

    "39": '<p><strong>διὰ τὸν λόγον τῆς γυναικός</strong> — "because of the word/testimony of the woman." <em>Logos</em> here is the woman\'s spoken report — her word generated the faith of many. The progression from her testimony (v.39) to Jesus\'s own word (v.41) mirrors the progression from human witness to direct encounter that the Evangelist traces throughout John (cf. 1:37–42).</p>',

    "40": '<p><strong>ἔμεινεν ἐκεῖ δύο ἡμέρας</strong> — "he remained there two days." <em>Menō</em> (to remain/abide) is a key Johannine word for dwelling relationship. The two days is concrete and narrated; the result is a deeper, broader faith in the community.</p>',

    "41": '<p><strong>διὰ τὸν λόγον αὐτοῦ</strong> — "because of his word." The shift from the woman\'s <em>logos</em> (v.39) to Jesus\'s own <em>logos</em> is explicit. Both are "word," but the effect of the second is greater: "many more believed." Witness testimony leads to encounter; encounter deepens belief.</p>',

    "42": '<p><strong>σωτὴρ τοῦ κόσμου</strong> — "Savior of the world." The genitive <em>tou kosmou</em> ("of the world") marks universal scope, not just Samaritan or Jewish scope. This is the climax of the pericope: the Samaritans, excluded from the covenant people, name Jesus with the most universal title used of him in any Gospel narrative. <em>Sōtēr</em> was also used of Roman emperors and benefactor deities — the Evangelist places it on the lips of Samaritans for a Jewish-Samaritan figure from Galilee.</p><p><strong>οὐκέτι διὰ τὴν σὴν λαλιάν</strong> — "no longer because of your word." The Samaritans distinguish between the woman\'s testimony (the trigger) and their own direct hearing (the foundation). They do not dismiss her report but they have moved beyond it to personal encounter.</p>',

    "43": '<p>A transition: two days complete, Jesus departs for Galilee. The note is brief, preparing for the Galilean reception and the second sign.</p>',

    "44": '<p><strong>αὐτὸς γὰρ Ἰησοῦς ἐμαρτύρησεν</strong> — "for Jesus himself testified." The Evangelist cites a known saying of Jesus about a prophet having no honor in his own country (<em>patris</em>, homeland). The irony of the saying here is complex: Jesus goes to Galilee, is welcomed by Galileans, and yet the saying suggests his own people will not truly honor him — the welcome is framed in terms of having seen signs (v.45), not the kind of faith Jesus seeks.</p>',

    "45": '<p><strong>ἑωρακότες πάντα ἃ ἐποίησεν ἐν Ἱεροσολύμοις</strong> — "having seen all that he did in Jerusalem." The Galileans\' welcome is sign-based: they were at the Passover and saw the works. The Evangelist notes this without endorsing it as the deepest faith; the royal official in vv.46–54 will model the better kind (belief from the word alone).</p>',

    "46": '<p><strong>βασιλικός</strong> (<em>basilikos</em>) — "royal [official]" — someone in the service of Herod Antipas or another Herodian ruler. The designation is social and political. His son is at Capernaum, approximately 25 miles from Cana. He has traveled a significant distance based on a report that Jesus had returned to Galilee from Judaea.</p>',

    "47": '<p><strong>ἤμελλεν γὰρ ἀποθνῄσκειν</strong> — "for he was about to die." The imperfect <em>ēmellen</em> (was on the point of) with the present infinitive marks imminent death. The father\'s urgency is understandable: "come down before my child dies" (v.49) — before the final threshold is crossed.</p>',

    "48": '<p><strong>σημεῖα καὶ τέρατα</strong> (<em>sēmeia kai terata</em>) — "signs and wonders." The pairing is common in Jewish and Hellenistic literature for miraculous acts. Jesus\'s challenge is addressed to the plural "you" — the Galilean crowd (cf. v.45) who seek sign-based faith. The rebuke is not to the official personally but to the crowd whose faith requires visible displays before belief is possible.</p>',

    "49": '<p><strong>κύριε, κατάβηθι πρὶν ἀποθανεῖν τὸ παιδίον μου</strong> — "Sir/Lord, come down before my child dies." <em>Kyrie</em> is formal address; whether the official intends the full confessional weight of "Lord" is unclear. His request is for physical presence — he has not yet grasped that Jesus\'s word alone is sufficient. The narrative withholds the healing until the word alone is all he has.</p>',

    "50": '<p><strong>ἐπίστευσεν ὁ ἄνθρωπος τῷ λόγῳ ὃν εἶπεν αὐτῷ ὁ Ἰησοῦς</strong> — "the man believed the word which Jesus spoke to him." The dative <em>tō logō</em> identifies the content of his faith: not a sign, not a presence, not a performance — just the word Jesus spoke. This is the faith that does not require sight (cf. 20:29). He turned and went, on the strength of a sentence.</p>',

    "51": '<p><strong>ἤδη δὲ αὐτοῦ καταβαίνοντος</strong> — "while he was still going down." The genitive absolute construction marks the timing: the servants meet him en route, before he arrives home. The healing was complete before he saw it. The narrative structure preserves the priority of the word over the sight.</p>',

    "52": '<p><strong>ἐπύθετο οὖν τὴν ὥραν παρ᾽ αὐτῶν</strong> — "he inquired therefore from them the hour." The official investigates the timing. <strong>ἕβδομος</strong> (<em>hebdomos</em>, seventh hour) — approximately 1 PM in Roman reckoning. The coincidence is not approximate — it is exact. The father will recognize this in v.53.</p>',

    "53": '<p><strong>ἔγνω οὖν ὁ πατήρ ὅτι ἐκείνῃ τῇ ὥρᾳ</strong> — "the father therefore knew that at that very hour." The moment of recognition: the word and the healing were simultaneous. The result is household-wide faith: <strong>ἐπίστευσεν αὐτὸς καὶ ἡ οἰκία αὐτοῦ ὅλη</strong> — "he believed, and his whole household." The aorist episteusen marks the point of decisive belief; the scope extends beyond the individual.</p>',

    "54": '<p><strong>δεύτερον σημεῖον</strong> (<em>deuteron sēmeion</em>) — "second sign." The Evangelist counts the signs deliberately: the first sign was the water-to-wine at Cana (2:11); the second is this long-distance healing. Both signs occur in Galilee, bracket the Jerusalem-Samaria section of chapters 2–4, and both involve an initial challenge to the mode of faith being sought. The counting is a structural signal, not just a chronological note.</p>'
  }
}


def main():
    existing = load_comm('mkt-original', 'john')
    merge_comm(existing, JOHN)
    save_comm('mkt-original', 'john', existing)
    print('John 3–4 mkt-original written.')

if __name__ == '__main__':
    main()
