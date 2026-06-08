"""
Combined OT Phase 2 script: Deuteronomy, Jeremiah, Ezekiel, Daniel — all four layers.
These four books have the highest NT echo density of all remaining OT books.
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

# ============================================================
# DEUTERONOMY
# ============================================================

DEUT_ECHO = {
  "6": {
    "4": [
      {"type": "allusion", "target": "Mark 12:29", "note": "Hear O Israel the LORD our God the LORD is one — Jesus cites the Shema (Deut 6:4-5) as the first and greatest commandment; the Shema frames the entire law in the context of YHWH's singular Lordship over Israel"},
      {"type": "allusion", "target": "1 Cor 8:6", "note": "One God the Father from whom are all things and one Lord Jesus Christ through whom are all things — Paul's expansion of the Shema incorporates Jesus into the divine identity: the 'one Lord' of the Shema is now differentiated into Father and Son"}
    ]
  },
  "18": {
    "15": [
      {"type": "fulfillment", "target": "Acts 3:22", "note": "A prophet like me will the LORD your God raise up for you — Peter cites Deut 18:15 as fulfilled in Jesus; the eschatological prophet-like-Moses was the figure Israel expected, and Peter declares Jesus to be that prophet"},
      {"type": "fulfillment", "target": "Acts 7:37", "note": "God will raise up for you a prophet like me from your brothers — Stephen's speech identifies the prophet-like-Moses promise as the Christological center of Moses's ministry; Israel's rejection of Moses typifies their rejection of Jesus"}
    ]
  },
  "21": {
    "23": [
      {"type": "fulfillment", "target": "Gal 3:13", "note": "Cursed is everyone who hangs on a tree — Paul cites Deut 21:23 as fulfilled in the crucifixion: Christ redeemed us from the curse of the law by becoming a curse for us, for cursed is everyone who hangs on a tree; the cross is the site of curse-absorption"}
    ]
  },
  "30": {
    "12": [
      {"type": "allusion", "target": "Rom 10:6-8", "note": "Do not say in your heart who will go up to heaven — Paul adapts Deut 30:12-14 Christologically: the word that is near you, in your heart and mouth, is the word of faith we proclaim; what Deuteronomy said of the Torah-command is now said of Christ and his gospel"}
    ]
  },
  "32": {
    "21": [
      {"type": "fulfillment", "target": "Rom 10:19", "note": "I will make you jealous of those who are not a nation — Paul cites the Song of Moses (Deut 32:21) as the OT basis for the Gentile mission provoking Israel to jealousy; the unexpected reversal of Gentile blessing is Moses's own warning"}
    ],
    "43": [
      {"type": "fulfillment", "target": "Rom 15:10", "note": "Rejoice O Gentiles with his people — Paul cites Deut 32:43 LXX as one of four OT texts (Rom 15:9-12) proving that Gentile inclusion in the worship of God was always the divine plan from Moses through the Psalms and Isaiah"}
    ]
  }
}

DEUT_ORIGINAL = {
  "8": {
    "1": "<p><strong>kol-hamitzvah</strong> (<em>kol-hammitswāh</em>): 'every commandment' — the singular collective noun treats the entire law as one unified demand, not a menu of options. The opening command is <em>tishmeru la'asot</em> ('be careful to do'), the twin verbs of covenant obedience: guarding (<em>shamar</em>) and performing (<em>asah</em>). The purpose clause — 'so that you may live and multiply and take possession' — makes obedience the path to the promised inheritance; the three verbs describe ascending covenantal fullness.</p>",
    "2": "<p><strong>anah</strong> (<em>ʿānāh</em>): 'to humble, afflict' — the wilderness is here interpreted as intentional divine pedagogy; YHWH afflicted Israel <em>lema'an da'at et-asher bi-levavcha</em>, 'to know what was in your heart.' <strong>Nasah</strong> (<em>nāsāh</em>): 'to test' — not to acquire information YHWH lacked, but to reveal to Israel itself what its heart contained. The wilderness is the diagnostic chamber of the covenant, not a punishment for Sinai apostasy alone.</p>",
    "3": "<p><strong>lo al-halachem levaddo yichyeh ha-adam ki al-kol-motsa pi-YHWH</strong>: 'Not by bread alone does man live, but by every word from the mouth of YHWH.' The manna (<em>man</em>) is a word-substitute — it teaches that divine provision flows through divine speech, not natural process. Jesus quotes this verse verbatim (Deut LXX) at his first temptation (Matt 4:4), redirecting Satan's bread-test to the prior authority of the word that already commands and provides. The <em>motsa</em> ('going forth, utterance') of YHWH's mouth is the creative and sustaining word behind all physical provision.</p>",
    "4": "<p><strong>simlathecha lo valah</strong> (<em>simlāṯĕkā lōʾ bāletāh</em>): 'your garment did not wear out' — <em>valah</em> means to decay, wear out, become old (the same root in 'vile'); the preservation of clothing alongside manna provision extends the miracle into every dimension of physical existence. The forty-year span frames the miracle: nothing natural survives forty years of wilderness use. The verse stands without elaboration — its brevity is its witness.</p>",
    "5": "<p><strong>yasar</strong> (<em>yāsar</em>): 'to discipline, instruct, chasten' — the father-son metaphor for the wilderness discipline is the theological key to chapter 8. <em>Ka'asher yeyaser ish et-beno</em>, 'as a man disciplines his son' — paternal discipline is the interpretive framework for Exodus hardship. Proverbs 3:11-12 develops this directly (<em>musar YHWH beni al-tima'as</em>, 'do not despise the LORD's discipline'); Hebrews 12:5-11 quotes Prov 3:11-12 and applies it to Christian suffering, completing the typological arc that begins here.</p>",
    "6": "<p><strong>lalechet bidrachav</strong> (<em>lāleket bidrākāyw</em>): 'to walk in his ways' — the walk-metaphor (<em>halakh</em>) is Deuteronomy's primary ethics image; the covenant life is conceived as a path to travel, not a set of rules to memorize. Three covenant acts are specified: keeping (<em>shamar</em>), walking (<em>halakh</em>), fearing (<em>yare'</em>) — cognitive, behavioral, and affective dimensions of the covenant relationship.</p>",
    "7": "<p><strong>eretz tovah</strong> (<em>ʾereṣ ṭôbāh</em>): 'a good land' — the threefold repetition of <em>tov</em> in Deut 8:7-10 (good land, v7; you eat and are satisfied, v10; the good land, v10) echoes Genesis 1's creation declaration. The land is described through its water systems: <em>nachalei mayim</em> (streams of water), <em>ayanot</em> (springs), <em>tehomot</em> (deeps/underground sources) — a complete hydrological portrait. The eschatological land of promise is paradigmatically a well-watered garden.</p>",
    "8": "<p>The seven species — wheat, barley, vines, figs, pomegranates, olive oil, and honey — constitute Israel's agricultural canon. These are not random but are the covenantally significant products of the land; the later agricultural festivals (firstfruits, Pentecost, Tabernacles) are organized around them. <strong>Devash</strong> (<em>dĕbaš</em>): 'honey' — may be date-honey rather than bee-honey; in any case, the sweetness principle: the land's produce is not merely adequate but pleasurable.</p>",
    "9": "<p><strong>lo techsar kol-ba</strong> (<em>lōʾ teḥsar kol-bāh</em>): 'you will lack nothing in it' — the categorical sufficiency of the land; nothing is missing. The geological detail — rocks containing iron (<em>barzel</em>), hills yielding copper (<em>nechoshet</em>) — specifies material abundance in a pre-industrial economy where metal was the index of civilizational power. The Promised Land is both agriculturally and industrially complete.</p>",
    "10": "<p><strong>berakhta et-YHWH Eloheicha</strong> (<em>ûbēraktā ʾeṯ-Yhwh ʾĕlōhêkā</em>): 'you shall bless the LORD your God' — the command to bless YHWH <em>after</em> eating (<em>ve-akhalta ve-savata</em>) is the rabbinic basis for the Birkat Hamazon (grace after meals), considered a Toraitic obligation. The sequence — eat, be satisfied, bless — reverses the anxiety sequence of hoarding: you may eat fully because the giver is reliable, and the proper response to satiation is gratitude rather than expanded appetite.</p>",
    "11": "<p><strong>pen tishkach et-YHWH Eloheicha</strong> (<em>pen-tiškaḥ ʾeṯ-Yhwh ʾĕlōhêkā</em>): 'beware lest you forget the LORD your God' — the forget/remember axis is the backbone of Deuteronomy. <em>Zakhor</em> (remember) and <em>shakhach</em> (forget) are the two poles of covenant faithfulness and failure. Forgetting YHWH is defined specifically as failing to keep the commandments (<em>lishmore mitzvotav u-mishpatav ve-chuqqotav</em>) — it is not primarily an intellectual lapse but a behavioral drift.</p>",
    "12": "<p>The prosperity spiral begins: eating to the full, building fine houses, settling. <strong>Batim tovim</strong> (<em>bāttîm ṭôbîm</em>): 'fine houses' — the same <em>tov</em> (good/fine) that characterized the land now describes human constructions; the danger is when man's productions rival the land's gift. The five verbs (ate, built, settled, increased, multiplied, v13) trace the arc of prosperity that threatens covenant memory.</p>",
    "13": "<p>Material expansion continues — the triad of flock, silver, gold — the classic markers of patriarchal prosperity (cf. Gen 13:2, Abraham). <strong>Kesef ve-zahav</strong> (<em>kesep wĕzāhāb</em>): 'silver and gold' — the two monetary metals that summarize wealth. The expansion is not condemned; prosperity is a covenant blessing. The danger lies not in the wealth but in the heart-response it generates (v14).</p>",
    "14": "<p><strong>veram levavecha</strong> (<em>wĕrām lĕbābĕkā</em>): 'your heart will become proud/lifted up' — <em>rum</em> is elevation; pride is the heart lifting itself above its proper creaturely position. The result is forgetting YHWH (<em>vishkachta et-YHWH Eloheicha</em>). The anatomy of apostasy: prosperity → proud heart → forgetting → idolatry/disobedience. The identification of Egypt as <em>beit avadim</em> (house of slaves) reminds that the prosperity was not earned but given from a state of utter dependency.</p>",
    "15": "<p><strong>nachash saraph</strong> (<em>nāḥāš śārāp</em>): 'venomous/fiery serpent' — <em>saraph</em> means burning, fiery; probably describing the burning sensation of the venom (cf. Num 21:6-9, the bronze serpent). The wilderness is not merely difficult but actively hostile — snakes, scorpions, thirst, no water. Against this backdrop, the flint-water miracle (<em>hamotz'i lecha mayim mi-tsur hachalamish</em>) is the measure of YHWH's transforming provision: water from the hardest rock.</p>",
    "16": "<p>The manna returns as interpretive summary: its purpose was <em>le'anothecha u-lensasothecha</em> ('to humble and test you'), <em>leheitiv lecha be'acharitecha</em> ('to do you good in the end'). The wilderness suffering is teleological — oriented toward a good end that the sufferer cannot see in the moment. This is the theodicy of Deuteronomy 8: affliction serves formation, formation serves inheritance.</p>",
    "17": "<p><strong>kochi ve'otsem yadi asah li et-hachayil hazeh</strong> (<em>kōḥî wĕʿōṣem yādî ʿāśāh lî ʾeṯ-haḥayil hazzeh</em>): 'My power and the strength of my hands produced this wealth for me' — the formula of self-sufficiency; the precise inversion of covenant acknowledgment. <em>Chayil</em> means both wealth and valor/strength; the self-made-man ideology claims that human <em>chayil</em> generates its own <em>chayil</em>. This verse is the theological ground of every false gospel of self-reliance.</p>",
    "18": "<p><strong>koach la'asot chayil</strong> (<em>kōaḥ laʿăśôṯ ḥāyil</em>): 'ability to produce wealth' — the corrective: productive capacity itself is YHWH's gift. The purpose is specified: <em>lema'an hakim et-brito</em>, 'in order to confirm his covenant' — the covenant, not human ambition, is the framework within which prosperity occurs. What looks like human achievement is YHWH keeping his Abrahamic promise; wealth as covenant faithfulness demonstration.</p>",
    "19": "<p><strong>avod tovedun</strong> (<em>ʾābōd tōbēdûn</em>): 'you will certainly perish' — the absolute infinitive + finite verb construction is Hebrew's device for emphasis and certainty. The apostasy chain: forget YHWH → follow other gods → serve them → bow down to them — four steps of progressive idolatrous commitment. Each step deepens the covenant breach; the terminus is national death. The <em>ha'idoti vakhem hayom</em> ('I solemnly warn you today') invokes the treaty-witness formula.</p>",
    "20": "<p>The nations-parallel closes the chapter: Israel will perish <em>ka-goyim</em> (like the nations) — not as a special covenant people but as just another failed kingdom — <em>asher YHWH mavid mipneihem</em> (which YHWH is destroying before you). The nations are destroyed for their covenant violations with the created order; Israel can be destroyed for its covenant violation with YHWH. Covenant privilege does not exempt from covenant accountability.</p>"
  },
  "9": {
    "1": "<p><strong>shema Yisrael</strong> (<em>šĕmaʿ yiśrāʾēl</em>): 'Hear, O Israel' — the Shema-formula opens every major address in Deuteronomy; hearing (obedient attention) is the covenant stance. <strong>La'avotar goyim</strong> (<em>lĕhaḵrît gôyim</em>): 'to dispossess nations greater and mightier' — <em>gadol</em> (greater) and <em>atzum</em> (mightier) are exactly the terms used at Kadesh-barnea to describe the paralyzing impossibility; now they introduce a possibility in YHWH's strength.</p>",
    "2": "<p>The Anakites (<em>anakim</em>) — the giant-descendants of Anak; the spies' report had made them the paradigm of military impossibility (Num 13:33: 'we were like grasshoppers in our own eyes'). The proverb <em>'mi yityatzev lifnei benei Anak?'</em> ('who can stand before the sons of Anak?') preserves the cultural terror these warriors generated. Deuteronomy answers the rhetorical question: YHWH can, and Israel will, because YHWH fights for them.</p>",
    "3": "<p><strong>esh okhlah</strong> (<em>ʾēš ʾōkelāh</em>): 'a consuming fire' — the first occurrence of this theophanic description in Deuteronomy 9; it recurs in 4:24 and Heb 12:29. The fire-character of YHWH is his holiness in active engagement with what resists him. <em>Ha-over lefanecha</em> ('going before you') — YHWH as the advance combat force; Israel follows the divine warrior's trail. The promise is triple: destroy (<em>yashmid</em>), subdue (<em>yakniyam</em>), and drive out (<em>vehorashtam</em>).</p>",
    "4": "<p><strong>al-tomar bilevavcha betzidqati</strong> (<em>ʾal-tōmar bilibabĕkā bĕṣidqāṯî</em>): 'do not say in your heart because of my righteousness' — the conquest of Canaan tempts Israel to interpret divine favor as moral achievement. The correction: the nations' dispossession is <em>berishtat haggoyim</em> ('because of the wickedness of these nations'), not Israel's merit. This verse is the anthropological ground for Paul's argument in Romans: before God, no one can say 'because of my righteousness.'</p>",
    "5": "<p><strong>lo betzidqatcha uveyosher levavcha</strong> (<em>lōʾ bĕṣidqāṯĕkā ûbĕyōšer lĕbābĕkā</em>): 'not because of your righteousness or the uprightness of your heart' — the double denial eliminates both behavioral righteousness (<em>tzaddiq</em>) and motivational integrity (<em>yashar</em>) as grounds for the gift. The positive ground is twofold: (1) <em>berishtat haggoyim</em> (the nations' wickedness); (2) <em>lema'an hakim et-hadavar</em> (to fulfill the covenant oath to the patriarchs). Grace, not merit, is always the covenantal operative.</p>",
    "6": "<p><strong>am qesheh oref</strong> (<em>ʿam qĕšēh-ʿōrep</em>): 'stiff-necked people' — the defining characterization that Moses levels at Israel; the ox that will not yield its neck to the yoke. This designation first appears at Exod 32:9 after the golden calf; Deuteronomy 9 returns to it as the theological counter to any self-congratulatory interpretation of the conquest. Stephen's use of this exact phrase in Acts 7:51 shows its enduring force as the diagnosis of Israel's pattern of resistance.</p>",
    "7": "<p><strong>zakhor al-tishkach</strong> (<em>zĕkor ʾal-tiškaḥ</em>): 'remember, do not forget' — the two imperatives set up the antithetical pairing that structures Deuteronomic ethics. <em>Mamrim heyitem</em> ('you have been rebellious'): <em>marah</em> means to rebel, to be bitter, to be defiant — the full weight of covenant-legal disobedience. <em>Meyom da'ati etchem</em> ('from the day I knew you') — Moses's pastoral knowledge as witness; the entire history is a cumulative record.</p>",
    "8": "<p><strong>Chorev</strong> (<em>ḥōrēb</em>): Deuteronomy's name for Sinai; the same site where YHWH revealed himself in fire and gave the law. <em>Le'hashmidechem</em> ('to destroy you'): the same root (<em>shamad</em>) used for the nations Israel will displace. The parallel is deliberate: Israel's faithlessness makes them liable to the same destruction as the nations. The difference is intercessory grace (v18-19, 25-29).</p>",
    "9": "<p><strong>luchot avanim luchot ha-berit</strong> (<em>luḥôṯ ʾăbānîm luḥôṯ habbĕrîṯ</em>): 'tablets of stone, the covenant tablets' — the apposition identifies the stone tablets as the material form of the covenant; to receive the tablets is to receive the covenant. <em>Lechem lo akhalty umayim lo shatiti</em> ('bread I did not eat and water I did not drink') — the complete fast matches the duration; Moses sustained on divine presence alone, a proleptic sign of the eschatological feast where YHWH is the provision.</p>",
    "10": "<p><strong>ketuvim be-etzbah Elohim</strong> (<em>kĕṯûbîm bĕʾeṣbaʿ ʾĕlōhîm</em>): 'written by the finger of God' — the identical phrase as Exod 31:18; the Decalogue's divine authorship is emphasized precisely where it would become most important: Israel has just demonstrated why they need a law they cannot write themselves. The <em>etzbah</em> (finger) of God that writes the law is the same <em>etzbah</em> that drove out Egypt's plagues (Exod 8:19) and that Jesus invokes in Luke 11:20.</p>",
    "11": "<p>The forty days concluded: <em>vayyitten YHWH elai et-shney luchot ha-avanim luchot ha-berit</em> ('the LORD gave me the two stone tablets, the covenant tablets'). The handing over (<em>natan</em>) is formal and deliberate — the covenant document transferred from divine hand to human mediator. Verse 11 is the structural hinge: the tablets given just as the people below have abandoned them.</p>",
    "12": "<p><strong>maher saru min-haderekh</strong> (<em>māher sārû min-haddārek</em>): 'they have quickly turned from the way I commanded them' — <em>maher</em> (quickly, soon) is the word of shocking speed: Moses has not even descended with the covenant tablets when Israel constructs its replacement. <em>Pesel masekah</em> ('cast metal idol') — the melted earrings shaped into the calf constitute the precise inversion of the covenant tablets: human-made versus God-written, metal image versus invisible word.</p>",
    "13": "<p><strong>am qesheh oref</strong> (<em>ʿam qĕšēh-ʿōrep</em>): 'a stiff-necked people' — repeated from v6 for emphasis; YHWH's own diagnosis of Israel's character. The repeated assessment both explains the apostasy (they are constitutionally resistant) and grounds the need for grace (there is no remedy from within Israel's own nature). This is the OT anthropology that Paul assumes in Romans 7.</p>",
    "14": "<p><strong>herepha mimmenni veashmidem</strong> (<em>herepeʾ mimmennî wĕʾašmîdēm</em>): 'leave me alone that I may destroy them' — YHWH presents himself as restrained by Moses's presence; the intercessory posture of the mediator as the space between divine wrath and its object. <em>Emcheh et-shemam</em> ('I will blot out their name'): name-erasure is covenant death — to have no name in Israel is to have no future; compare Rev 3:5 (not blot out from the book of life). The Moses-replacement offer (a mightier nation from Moses) anticipates the new creation community.</p>",
    "15": "<p>Moses descends <em>veha-har bor be-esh</em> ('while the mountain was burning with fire'), the two covenant tablets in his hands — the physical tension between the covenant-document in his grip and the covenant-broken scene below. The fire-mountain is the covenant's witness; Moses descends from YHWH's presence into the catastrophe that presence indicts.</p>",
    "16": "<p><strong>chet'em laYHWH Eloheichem</strong> (<em>ḥăṭāʾtem laYhwh ʾĕlōhêkem</em>): 'you had sinned against the LORD your God' — the covenant-legal vocabulary; <em>chata</em> is missing the mark, failing the covenant standard. <em>Egel masekah</em> ('a cast calf') — the bull-image of El/YHWH syncretism; not the worship of another god but the worship of YHWH under a prohibited form. The sin is representational before it is substitutional.</p>",
    "17": "<p>Moses's tablet-breaking: <em>va'etpos bishnei haluchot va'ashlikh otam me'al shetei yadai</em> ('I seized the two tablets and threw them from both my hands') — the enacted covenant-dissolution; shattering the treaty document was the ancient Near Eastern symbolic act for covenant termination. Moses breaks the tablets before the people's eyes as a prophetic sign-act: you have already broken what these tablets contain. The breaking is not anger management but theology in action.</p>",
    "18": "<p>The second prostration — forty days and forty nights; the threefold parallel with v9 and v25 structures the intercession narrative. <em>Kol-chatatechem asher chatatum la'asot hara be'einei YHWH</em> ('all your sin that you committed by doing what was evil in the sight of the LORD') — the comprehensive summary; <em>ra be'einei YHWH</em> ('evil in the eyes of YHWH') is Deuteronomy's standard formula for covenant breach.</p>",
    "19": "<p><strong>chamat YHWH ve-apo</strong> (<em>ḥămaṯ Yhwh wĕʾappô</em>): 'the fury of the LORD and his anger' — the pairing of <em>chemah</em> (burning wrath) and <em>af</em> (anger/nostril-flaring) intensifies the danger; YHWH's wrath is not mild discomfort but covenant-breach consequence. <em>Vayyishma YHWH elai gam bappa'am hazeh</em> ('the LORD listened to me that time as well') — the effectiveness of intercession; prayer changes the divine-human trajectory. Moses's intercessory effectiveness is the OT type of Christ's high-priestly prayer (Heb 7:25).</p>",
    "20": "<p><strong>be'Aharon hitanaf meod l'hashmido</strong> (<em>bĕʾahărōn hiṯʾannaṯ mĕʾōd lĕhašmîdô</em>): 'very angry with Aaron to destroy him' — Aaron's priestly leadership of the calf-construction makes him secondarily liable for the covenant disaster. Moses intercedes specifically for Aaron (<em>va'etpallel gam be'ad Aharon ba'et hahiv</em>, 'I prayed also for Aaron at that same time'). The high priest is saved by intercessory prayer; the greater High Priest (Heb 5:1) is himself the intercessor who cannot be destroyed.</p>",
    "21": "<p>The destruction of the calf follows a precise protocol: burned (<em>saraph ba'esh</em>), crushed (<em>khatash</em>), ground fine (<em>tachon heitev</em>), scattered in the stream. The thoroughness mirrors the herem-destruction of Canaanite idols commanded in Deut 7:5, 25. Total destruction is the only adequate response to the idol; partial preservation leaves the possibility of return. The dust thrown into the stream recalls Exod 32:20 — the consuming of the idol by its former worshippers.</p>",
    "22": "<p>The catalog of wilderness failures: Taberah (<em>tab'erah</em>, 'burning' — the fire incident of Num 11:1-3), Massah (<em>massah</em>, 'testing' — the water-from-rock complaint of Exod 17:1-7), Kibroth-hattaavah (<em>qibrot hatta'avah</em>, 'graves of craving' — the quail-excess of Num 11:31-35). Each place-name is a theological memory: the wilderness geography is sin-geography, the landscape of Israel's pattern of provoking YHWH.</p>",
    "23": "<p><strong>lo-he'emantem lo velo shmahtem beqolo</strong> (<em>lōʾ heʾĕmantem lô wĕlōʾ šmaʿtem bĕqōlô</em>): 'you did not trust him and did not obey his voice' — the two verbs of covenant failure at Kadesh: unbelief (<em>aman</em> hiphil, to trust/believe) and disobedience (<em>shama</em> to listen/obey). The Kadesh failure is not primarily military but theological: the spies' report was believed over YHWH's promise. Hebrews 3:16-19 uses this as the definitive example of the unbelief-disobedience connection.</p>",
    "24": "<p><strong>mamrim heyitem im-YHWH meyom da'ati etchem</strong> (<em>mamrim hĕyîtem ʿim-Yhwh miyyôm daʿtî ʾeṯkem</em>): 'you have been rebellious against the LORD from the day I first knew you' — the sweeping pastoral indictment; Moses's entire relationship with Israel has been a relationship with rebels. <em>Da'ati</em> ('from my knowing you') frames it relationally: Moses knows Israel not as a supervisor knows employees but as a shepherd knows sheep. The rebellion is all the more grievous for its relational context.</p>",
    "25": "<p>The second extended intercession: forty days and forty nights, prostrate before YHWH (<em>va'etnapal lifnei YHWH et arba'im hayom ve'et arba'im halaylah asher hitnapalti</em>). The three prostration periods (vv9, 18, 25) structure chapter 9's narrative of grace through intercession. Moses's physical posture — face-to-the-ground — enacts the absolute vulnerability of the mediator before the covenant-keeping God on behalf of the covenant-breaking people.</p>",
    "26": "<p><strong>Adonai YHWH al-tashchet ammecha venachalatecha</strong> (<em>ʾăḏōnāy Yhwh ʾal-tašḥēṯ ʿammĕkā wĕnaḥălāṯekā</em>): 'O Lord GOD, do not destroy your people and your inheritance' — the double divine name (<em>Adonai YHWH</em>) of solemn address; the same formula Moses used at Deut 3:24. The intercessory argument is possessive: they are <em>your</em> people, <em>your</em> inheritance. YHWH's own honor is at stake in their preservation. <em>Asher padita begadolecha</em> ('whom you redeemed by your greatness'): the exodus-redemption as the basis for the appeal.</p>",
    "27": "<p><strong>zechor la'avadeicha le-Avraham le-Yitzchak ule-Ya'aqov</strong> (<em>zĕkor lĕʿăbādêkā lĕʾabrāhām lĕyiṣḥāq ûlĕyaʿăqōb</em>): 'remember your servants Abraham, Isaac, and Jacob' — the covenant-history argument; the patriarchal promise creates a divine obligation that cannot be abandoned without self-contradiction. <em>Al-tefen el-qeshiyut ha'am hazeh</em> ('do not consider the stubbornness of this people') — Moses asks YHWH to look past the present character evidence to the prior covenant commitment.</p>",
    "28": "<p><strong>pen yomru ha'aretz asher hotzeitanu mishsam</strong> (<em>pen-yōmrû hāʾāreṣ ʾăšer hôṣēʾṯānû miššām</em>): 'lest the land from which you brought us say...' — the nations-as-audience argument; the watching world will interpret Israel's destruction as evidence of YHWH's inability (<em>mibli yecholet YHWH</em>, 'because YHWH was not able') or hatred (<em>umissin'ato otam</em>). Divine reputation in the watching world is grounds for covenant preservation. This argument recurs in Moses's intercession at Num 14:13-16 and in the exile-passages of Ezek 36:20-23.</p>",
    "29": "<p><strong>vehem ammecha venachalatecha</strong> (<em>wĕhēm ʿammĕkā wĕnaḥălāṯekā</em>): 'but they are your people and your inheritance' — the closing possessive assertion; the intercessory prayer ends with the same possessive argument it began with (v26). The prayer's logic: they belong to you, you redeemed them, your reputation requires their survival, your covenant to the patriarchs demands their continuation. The bare possessives — <em>your</em> people, <em>your</em> inheritance — are the ultimate appeal: ownership creates obligation.</p>"
  },
  "10": {
    "1": "<p><strong>pesol lecha shney luchot avanim karishonim</strong> (<em>psol lĕkā šĕnê-luḥôṯ ʾăbānîm kāriʾšōnîm</em>): 'chisel out two stone tablets like the first ones' — the covenant renewal requires human preparation; Moses chisels, YHWH writes. The distinction preserves both human agency and divine authorship in the covenant-making process. <em>Aron etz</em> ('a wooden chest') — the first mention of the ark's construction in Deuteronomy; its purpose is to house the covenant document, making the covenant portable and central to Israel's movement.</p>",
    "2": "<p><strong>ektov al-haluchot et-hadevarim asher hayu al-haluchot harishonim</strong> (<em>wĕʾeḵtōb ʿal-halluḥôṯ ʾeṯ-haddĕbārîm ʾăšer hāyû ʿal-halluḥôṯ hāriʾšōnîm</em>): 'I will write on the tablets the same words as were on the first ones' — the covenant is renewed without revision; grace restores without lowering the standard. The broken tablets represented covenant rupture; the new tablets represent covenant renewal on identical terms — not a new, easier arrangement but the same demanding covenant given again.</p>",
    "3": "<p><strong>va'a'as aron atzei shittim</strong> (<em>wāʾaʿaś ʾărôn ʿăṣê šiṭṭîm</em>): 'I made an ark of acacia wood' — <em>shittim</em> (acacia) is the same wood specified in Exod 25:10 for the tabernacle ark; Moses makes a simpler version here. The narrative conflates or summarizes the tabernacle construction; the key point is that the ark precedes the tablets — covenant-storage is prepared before covenant-document is received. Preparation for receiving the word of God is itself a covenant act.</p>",
    "4": "<p><strong>aseret ha-devarim</strong> (<em>ʿăśereṯ haddĕbārîm</em>): 'the ten words/commands' — the technical OT term for the Decalogue (used also at Exod 34:28, Deut 4:13); <em>devarim</em> (words/matters) rather than <em>mitzvot</em> (commandments) emphasizes their character as divine speech before they are legal demands. Written again by YHWH from the fire; the second giving of the Decalogue is an enacted grace — the destroyed covenant document replaced by the covenant-keeping God.</p>",
    "5": "<p><strong>va'asem et-haluchot ba'aron</strong> (<em>wāʾāśem ʾeṯ-halluḥôṯ bāʾārôn</em>): 'I placed the tablets in the ark' — the ark as the covenant's home; the law at the center of the community's physical structure. The closing note — <em>vayyihyu sham ka'asher tzivvani YHWH</em> ('and there they remain, just as the LORD commanded me') — grounds continuing covenant faithfulness on the original divine command, not periodic human recommitment.</p>",
    "6": "<p>The travel notation records Aaron's death at Moserah (cf. Num 33:30-38 where Hor is the site; the discrepancy may reflect different naming traditions for the same or adjacent sites). <em>Va'yekahein Eleazar beno tachtav</em> ('Eleazar his son took over the priestly ministry'): the Aaronic priesthood continues through biological succession; the covenant institution survives the death of its founding figure. Death does not interrupt the divine program — it transfers to the next generation.</p>",
    "7": "<p>The travel list — Gudgodah (<em>gudgodah</em>) to Jotbathah (<em>yotvathah</em>), a land of flowing streams (<em>eretz nachalei mayim</em>) — provides geographical specificity that resists abstraction. The mention of water-rich Jotbathah after the wilderness narrative is a micro-movement from scarcity to provision; the promise-land motif appears in the travelogue itself.</p>",
    "8": "<p><strong>hivdil YHWH et-shevet ha-Levi</strong> (<em>hibdîl Yhwh ʾeṯ-šēbeṯ halēwî</em>): 'the LORD set apart the tribe of Levi' — <em>hivdil</em> (to separate, set apart) is the vocabulary of holiness-creation; the Levites are made holy by divine designation, not natural superiority. Three functions enumerated: (1) carry the ark (<em>laset et-aron berit YHWH</em>); (2) stand before YHWH to minister (<em>la'amed lifnei YHWH lesharto</em>); (3) bless in his name (<em>levarekh bishmov</em>). The priestly function is simultaneously spatial (standing before), relational (serving), and verbal (blessing).</p>",
    "9": "<p><strong>YHWH hu nachalato</strong> (<em>Yhwh hûʾ naḥălāṯô</em>): 'the LORD himself is his inheritance' — the Levitical principle: no land portion, YHWH instead. This is the highest possible exchange: finite territory given up for the infinite God. The principle is eschatological: Rev 21:3 ('they will be his people and God himself will be with them') generalizes the Levitical condition to all of the new creation people. In Christ, all believers become a royal priesthood (1 Pet 2:9) for whom God is the inheritance.</p>",
    "10": "<p><strong>velo ava YHWH hashchetecha</strong> (<em>wĕlōʾ-ʾābāh Yhwh hašḥîṯĕkā</em>): 'the LORD was unwilling to destroy you' — the intercession's result; YHWH's will is changed by prayer. This is one of the Bible's most direct statements that intercessory prayer alters the divine course of action. The theological question (does prayer change God?) is answered here: yes, within the framework of covenant faithfulness. Moses's successful intercession is the OT type of Christ's ever-living intercession (Heb 7:25).</p>",
    "11": "<p><strong>qum lekh le'neso'a ha'am</strong> (<em>qûm lēk lĕnasoaʿ hāʿām</em>): 'get up and lead the people on their journey' — the renewal enables mission; after intercession comes commission. The covenant forgiveness does not merely restore the status quo ante but recommissions Moses and Israel to the original purpose. <em>Asher nishbati la'avotam latet lahem</em> ('which I swore to give to their fathers') — the inheritance-promise is renewed; the failure did not cancel the intention.</p>",
    "12": "<p><strong>mah YHWH Eloheicha sho'el me'imcha</strong> (<em>mā Yhwh ʾĕlōhêkā šōʾēl mēʿimmāk</em>): 'what does the LORD your God ask of you?' — the great rhetorical question; the answer is the Deuteronomic summary of the covenant life. Five verbs: fear (<em>liyre'ah</em>), walk (<em>lalechet</em>), love (<em>le'ahavah</em>), serve (<em>la'avod</em>) with all your heart and soul, and keep (<em>lishmor</em>) the commandments. Micah 6:8 compresses this to three: justice, loyalty, humble walking. Jesus further compresses it to two (love God, love neighbor), calling these 'all the Law and the Prophets.'</p>",
    "13": "<p><strong>letov lach</strong> (<em>lĕṭôb lāk</em>): 'for your good' — the covenant commandments are not arbitrary impositions but the path to human flourishing. The covenant law is characterized throughout Deuteronomy as gift before obligation: YHWH gives the commandments <em>for your own good</em>. Paul's statement in Romans 7:12 (<em>the law is holy and the commandment is holy, righteous, and good</em>) restores this positive characterization after his analysis of the law's limitations.</p>",
    "14": "<p><strong>YHWH Eloheicha hashamayim ushmei hashamayim ha'aretz vekhol-asher bah</strong> (<em>Yhwh ʾĕlōhêkā haššāmayim ûšmê haššāmayim hāʾāreṣ wĕkol-ʾăšer-bāh</em>): 'To the LORD your God belong the heavens, even the highest heavens, the earth and everything in it' — the universal sovereignty statement; <em>shmei hashamayim</em> ('the heavens of heavens') is Hebrew superlative: the uttermost sky. The paradox of the next verse: this cosmic God specifically chose Abraham's descendants among all peoples. Universal sovereignty and particular election are not in tension; they explain each other.</p>",
    "15": "<p><strong>raq ba'avotecha chashaq YHWH le'ahavah otam</strong> (<em>raq bāʾăbōṯêkā ḥāšaq Yhwh lĕʾahăbāh ʾōṯām</em>): 'yet the LORD delighted in your fathers and loved them' — <em>chashaq</em> is a strong word: attachment, desire, binding affection; it appears only 11 times in the OT and always carries emotional intensity. The election love is prior (<em>raq</em> = 'only', 'nevertheless' — despite their smallness) and generational (the patriarchs chosen, their descendants chosen in them). This is sovereign grace: the object does not explain the choice.</p>",
    "16": "<p><strong>umaltem et arlat levavechem</strong> (<em>ûmaltĕṯem ʾeṯ ʿŏrlaṯ lĕbabĕkem</em>): 'circumcise your hearts' — the inner circumcision command; the physical rite that marks covenant membership (Gen 17) points to the inner transformation it cannot produce. <em>Arlah</em> (foreskin/uncircumcision) applied to the heart means the same obstruction that physical uncircumcision represents: exclusion from the covenant community's inner life. Jer 4:4, 9:25-26 develop this; Romans 2:29 completes it: the true circumcision is of the heart, by the Spirit. Deuteronomy 10:16 is the OT's clearest pointer to the new covenant necessity.</p>",
    "17": "<p><strong>Elohei ha-elohim va'Adonei ha-adonim</strong> (<em>ʾĕlōhê hāʾĕlōhîm waʾăḏōnê hāʾăḏōnîm</em>): 'God of gods and Lord of lords' — the double superlative; the only place in the Hebrew Bible where both titles appear together. Revelation 17:14 and 19:16 apply them both to Christ: <em>Lord of lords and King of kings</em>. <em>Ha-gadol ha-gibbor veha-nora</em> ('the great, mighty, and awesome'): the Deuteronomic divine-attribute triad that becomes the liturgical formula of the Amidah prayer and Nehemiah 9:32.</p>",
    "18": "<p><strong>oseh mishpat yatom ve'almanah</strong> (<em>ʿōśeh mišpaṭ yāṯôm wĕʾalmānāh</em>): 'he upholds justice for the fatherless and the widow' — the marginalized triad of Deuteronomy: the orphan, widow, and foreigner (<em>ger</em>). YHWH's own character is defined by this justice-work; his ethics of inclusion precede and ground Israel's. <em>Oheiv ger</em> ('loves the foreigner'): YHWH's love for the outsider makes the command to love the foreigner (v19) a participation in YHWH's own disposition, not merely a humanitarian policy.</p>",
    "19": "<p><strong>va'ahavtem et-hager ki gerim heyitem be'eretz Mitzraim</strong> (<em>waʾăhebtem ʾeṯ-hagger kî-gērîm hĕyîṯem bĕʾereṣ miṣrāyim</em>): 'love the foreigner, for you were foreigners in Egypt' — the experiential basis for social ethics: Israel's own memory of marginalization generates the ethical obligation toward the marginalized. This is the double-movement of covenantal compassion: what YHWH did for you when you were powerless, you must enact for others who are now powerless. The Exodus is not only a theological event but an ethical resource.</p>",
    "20": "<p><strong>u'vo tidbaq</strong> (<em>ûbô ṯiḏbāq</em>): 'hold fast to him' — <em>daveq</em> (to cling, cleave) is the same root as Genesis 2:24's <em>ve-davaq be'ishto</em> ('he shall hold fast to his wife') — the marital-union vocabulary applied to the YHWH-Israel relationship. <em>Devequt</em> (cleaving/attachment) becomes a central category in Jewish mysticism; here it is the covenant's relational core: not merely obeying commands but <em>cleaving</em> to the person who gives them. Deut 10:20 is the OT ground for Paul's <em>joined to the Lord</em> language (1 Cor 6:17).</p>",
    "21": "<p><strong>hu tehillatecha vehu Eloheicha</strong> (<em>hûʾ ṯĕhillāṯĕkā wĕhûʾ ʾĕlōhêkā</em>): 'he is your praise and he is your God' — the double identification: YHWH is both the content of Israel's praise and Israel's God. The equation of God-ness and praiseworthiness is the confession that the being who deserves praise is the one who acts for you. <em>Asher asah ittecha et-hagedolot ve'et-hanora'ot ha'eleh asher ra'u eineicha</em> ('who has done these great and awe-inspiring things your own eyes have seen'): the eyewitness element grounds the praise in history, not abstraction.</p>",
    "22": "<p><strong>bishiv'im nefesh yardu avoteicha Mitzraimah</strong> (<em>bĕšibʿîm nep̄eš yārĕḏû ʾăbōṯêkā miṣrāymāh</em>): 'your fathers went down to Egypt as seventy souls' — the historical baseline (Exod 1:5, Gen 46:27); from seventy to as numerous as the stars (<em>kekochvei hashamayim larov</em>) is the Abrahamic promise fulfilled (Gen 15:5, 22:17). The numerical explosion across centuries is YHWH's demonstration that his covenant promises are not rhetorical: he counted seventy and made them millions. The God who counts the stars (Ps 147:4) counts and multiplies his covenant people.</p>"
  },
  "6": {
    "4": "<p><strong>shema yisrael YHWH eloheinu YHWH echad</strong> (<em>šĕmaʿ yiśrāʾēl Yhwh ʾĕlōhênû Yhwh ʾeḥād</em>): 'Hear O Israel: YHWH our God, YHWH is one.' The Shema is the foundational confession of Jewish faith, recited morning and evening by observant Jews. <em>Echad</em> (one) is the standard Hebrew numeral one — it allows for internal distinction (as in <em>yom echad</em>, one day, composed of evening and morning; Gen 2:24, <em>basar echad</em>, one flesh, composed of two persons) but asserts the unity of the divine being against all polytheism. Paul's expansion in 1 Cor 8:6 ('one God the Father ... and one Lord Jesus Christ') is not an abandonment of monotheism but a Christological reconfiguration: the Shema's single divine identity now encompasses both Father and Son.</p>"
  },
  "18": {
    "15": "<p><strong>navi mikirbecha meacheicha kamoni yaqim lecha YHWH eloheicha elav tishmaun</strong> (<em>nābîʾ miqqirbĕkā mēʾahêkā kāmōnî yāqîm lĕkā Yhwh ʾĕlōhêkā ʾēlāw tišmāʿûn</em>): 'A prophet like me will YHWH your God raise up for you from among your brothers; to him you shall listen.' The singular prophet (<em>navi</em>) can be read as: (1) a category or series of prophets who will continue Moses's role; (2) an individual eschatological figure. The Qumran community awaited a specific prophetic figure alongside the Messiah and the Aaronic priest (1QS 9:11). Peter and Stephen in Acts 3 and 7 take reading (2): the specific individual is Jesus, whose coming makes the definitive Torah-interpretation that Moses could only anticipate.</p>"
  },
  "30": {
    "15": "<p><strong>reeh natati lefanecha hayom et-hahayyim veet-hatov veet-hamot veet-hara</strong> (<em>rĕʾēh nātattî lĕpānêkā hayyôm ʾet-hahayyîm wĕʾet-haṭṭôb wĕʾet-hammāwet wĕʾet-hārāʿ</em>): 'See I have set before you today life and good, and death and evil.' The covenant's binary choice — life or death, blessing or curse — is Israel's definitive moral situation. Paul's Christological reading of Deut 30 in Romans 10:6-8 is one of his most daring hermeneutical moves: the Torah's own accessibility-language ('not up in heaven, not across the sea, but very near you') is applied to the word of Christ — the gospel is the <em>Torah's own principle</em> of accessibility now embodied in the proclaimed word of faith.</p>"
  }
}

DEUT_CONTEXT = {
  "1": {
    "1": "<p>Deuteronomy is the fifth book of the Torah and claims to be Moses's farewell addresses on the plains of Moab before Israel enters Canaan (Deut 1:1-5). Its genre is that of a suzerainty treaty — a literary form well-attested in Hittite treaties of the second millennium BCE (Meredith Kline's groundbreaking work showed the structural parallels): preamble (1:1-5), historical prologue (1:6-4:49), stipulations (5-26), sanctions/blessings-curses (27-30), succession arrangements (31-34). The treaty-form supports an early date for Deuteronomy's core. The 'Deuteronomistic History' (Joshua through Kings) shares Deuteronomy's theological vocabulary and framework — its editors used Deuteronomy as the lens for evaluating Israel's kings.</p>"
  },
  "18": {
    "20": "<p>The test for a true prophet (18:21-22: if the word does not come to pass, it is not from YHWH) is applied in the NT to Jesus in a reversed form: his words came to pass, validating his prophetic authority. The false-prophet warning (18:20: the prophet who presumes to speak in YHWH's name a word I have not commanded him — that prophet shall die) is the background for Paul's 'if anyone preaches a gospel contrary to the one you received, let him be accursed' (Gal 1:8-9) — the apostolic test of false teaching applies Deuteronomic prophet-testing logic.</p>"
  },
  "34": {
    "10": "<p>'There has not arisen a prophet since in Israel like Moses, whom YHWH knew face to face' (34:10) is Deuteronomy's own closing judgment — the book ends by declaring Moses's prophetic incomparable greatness, which simultaneously points forward to the one greater prophet who is still awaited (18:15). The ending creates an anticipation: Moses is the greatest so far; the prophet-like-Moses is still coming. Hebrews 3:3 completes the comparison: Jesus has been counted worthy of more glory than Moses, as the builder of a house has more honor than the house.</p>"
  }
}

DEUT_CHRIST = {
  "18": {
    "15": "<p>A fulfillment: 'YHWH your God will raise up for you a prophet like me from among you, from your brothers — it is to him you shall listen.' Moses is the OT's supreme mediator — prophet (spoke YHWH's word), priest (offered sacrifice), and king (led the nation). The prophet-like-Moses is therefore the one who fulfills and exceeds all three mediatorial roles. Jesus is explicitly this prophet (Acts 3:22; 7:37), and exceeds him: as the Sermon on the Mount places Jesus's authority above Moses's ('you have heard it said ... but I say to you'), so Hebrews (3:3-6) places Christ's glory above Moses's as Son above servant. The Mosaic mediation was provisional; the Christological mediation is final and complete.</p>"
  },
  "21": {
    "23": "<p>A fulfillment: 'A hanged man is cursed by God.' Paul's citation of Deut 21:23 in Galatians 3:13 is one of his most audacious Christological moves: the cross is the cursed man's tree, and Christ became the curse for us by hanging on it. The law's curse-category — designed for criminals — is the very location where Christ absorbs all covenant-curses. The cross is not a circumvention of Torah-logic but its fulfillment: the law had always required a curse-bearer for the covenant community's sin, and Christ is that bearer. The Deuteronomic law that seemed to disqualify Jesus (a hanged criminal is cursed by God) becomes, in Paul's reading, the very mechanism of redemption.</p>"
  },
  "30": {
    "15": "<p>A direct revelation: 'See I have set before you today life and good, and death and evil.' Deuteronomy's covenant-choice reaches its eschatological fullness in Jesus: 'I am the way, and the truth, and the life' (John 14:6); 'I came that they may have life and have it abundantly' (John 10:10). The choice Moses set before Israel — life or death — is now embodied in a person. To choose Christ is to choose life in the covenant's deepest sense; to reject him is to choose the death that Moses warned of. The binary structure of Deut 30 (life vs. death, blessing vs. curse) is not dissolved in the NT but given its ultimate personal form in Christ.</p>"
  }
}

# ============================================================
# JEREMIAH
# ============================================================

JER_ECHO = {
  "1": {
    "5": [
      {"type": "allusion", "target": "Gal 1:15", "note": "Before I formed you in the womb I knew you, before you were born I consecrated you — Paul describes his own apostolic call with the same language: he was set apart before his birth; the prophetic-call pattern of Jeremiah's consecration becomes the pattern for Paul's apostolic election"}
    ]
  },
  "7": {
    "11": [
      {"type": "fulfillment", "target": "Matt 21:13", "note": "Has this house become a den of robbers in your eyes? — Jesus quotes Jer 7:11 in the temple-cleansing: my house shall be called a house of prayer, but you have made it a den of robbers; the Jeremianic temple-sermon's judgment of Israel's false security in the temple is Jesus's own indictment of the Herodian temple system"}
    ]
  },
  "31": {
    "15": [
      {"type": "fulfillment", "target": "Matt 2:18", "note": "A voice was heard in Ramah, weeping and loud lamentation, Rachel weeping for her children — Matthew cites Jer 31:15 as fulfilled in Herod's massacre of the infants of Bethlehem; Rachel weeping for her exiled children (the Babylonian deportation) is now Rachel weeping for the slaughtered children of Bethlehem"},
      {"type": "allusion", "target": "Luke 23:28", "note": "Jesus's warning to the daughters of Jerusalem to weep not for him but for themselves and their children echoes the Jeremianic pattern of future lamentation over Jerusalem (Jer 9:1; 14:17; 31:15); the weeping-for-Israel motif runs from Jeremiah through Luke's passion narrative"}
    ],
    "31": [
      {"type": "fulfillment", "target": "Heb 8:8-12", "note": "Behold the days are coming when I will make a new covenant with the house of Israel — Hebrews cites Jer 31:31-34 in full (the longest OT quotation in the NT) as the scriptural demonstration that the Mosaic covenant was designed to be superseded; the new covenant's promise (law on hearts, universal knowledge of YHWH, permanent forgiveness) is fulfilled in Christ"},
      {"type": "fulfillment", "target": "Luke 22:20", "note": "This cup is the new covenant in my blood — Jesus at the Last Supper identifies the cup with Jer 31:31-34's new covenant; the blood of Christ is the blood of the covenant Jeremiah announced, making the Lord's Supper the enacted new covenant seal"}
    ]
  }
}

JER_ORIGINAL = {
  "31": {
    "31": "<p><strong>hinei yamim baim neum YHWH vekharati et-beit Yisrael veet-beit Yehudah berit hadasha</strong> (<em>hinnēh yāmîm bāʾîm nĕʾum Yhwh wĕkārattî ʾet-bêt yiśrāʾēl wĕʾet-bêt yĕhûdāh bĕrît ḥădāšāh</em>): 'Behold the days are coming, declares YHWH, when I will make a new covenant with the house of Israel and the house of Judah.' <em>Berit hadasha</em> (new covenant): the only occurrence of this exact phrase in the OT. <em>Hadash</em> (new) can mean 'renewed' (as in the new moon, <em>hodesh</em>) or 'qualitatively different.' Jeremiah's contrast makes it the latter: 'not like the covenant I made with their fathers ... which they broke' (v. 32). The new covenant is distinguished by three characteristics: (1) internalized law (v. 33: on the heart, not stone); (2) universal direct knowledge of YHWH (v. 34: no longer 'know the LORD'); (3) permanent forgiveness (v. 34: I will remember their sin no more).</p>"
  }
}

JER_CONTEXT = {
  "1": {
    "1": "<p>Jeremiah prophesied ca. 627-586 BCE (from the 13th year of Josiah through the fall of Jerusalem and beyond), the most turbulent period in Judah's history. He witnessed Josiah's reform (621 BCE, 2 Kings 22-23) and its collapse, the defeats at Megiddo (609 BCE) and Carchemish (605 BCE), Nebuchadnezzar's three deportations (605, 597, 586 BCE), the destruction of Jerusalem and the temple (586 BCE), and the assassination of Gedaliah. His call at the outset of his ministry and his suffering throughout (the 'Confessions', Jer 11-20) make him the most personal of the prophets — his inner life is more visible in Scripture than any other OT figure. The 'new covenant' oracle (31:31-34) is addressed to a people in the ruins of the Babylonian exile.</p>"
  },
  "31": {
    "34": "<p>The three promises of Jer 31:33-34 in their historical context: (1) the Torah internalized on hearts rather than carved on tablets solves the problem that generated the exile — Israel kept the external law while their hearts were far from YHWH; (2) the universal knowledge of YHWH solves the class-stratification of covenantal knowledge (prophets, priests, sages knew; the people often did not); (3) the permanent forgiveness ('I will remember their sin no more') solves the accumulated sin-debt that the Mosaic sacrificial system could cover but not finally remove (Heb 10:1-4: the law has a shadow ... sacrifices cannot make perfect those who draw near). The new covenant addresses precisely the structural deficiencies of the Mosaic covenant.</p>"
  }
}

JER_CHRIST = {
  "31": {
    "31": "<p>A direct revelation: 'Behold the days are coming when I will make a new covenant with the house of Israel and the house of Judah.' The new covenant is the Christological center of the OT's prophetic program: Jesus at the Last Supper explicitly claims to enact this covenant (Luke 22:20: 'This cup that is poured out for you is the new covenant in my blood'), and Hebrews quotes all of Jer 31:31-34 (8:8-12) as the scriptural proof that the old covenant's priesthood and sacrificial system were provisional and superseded. The three elements of the new covenant are fulfilled in Christ: (1) law on hearts → the Spirit writes Christ's character in the believer; (2) universal knowledge of YHWH → all who come to Christ know the Father (John 17:3); (3) permanent forgiveness → the once-for-all sacrifice of Christ (Heb 9:26-28; 10:14).</p>"
  }
}

# ============================================================
# EZEKIEL
# ============================================================

EZEK_ECHO = {
  "11": {
    "19": [
      {"type": "fulfillment", "target": "2 Cor 3:3", "note": "I will remove the heart of stone and give them a heart of flesh — the new heart/new spirit promise of Ezek 11:19 and 36:26 is fulfilled in the Spirit's ministry that Paul describes: written not on stone tablets but on tablets of human hearts"}
    ]
  },
  "34": {
    "11": [
      {"type": "fulfillment", "target": "John 10:11", "note": "I myself will search for my sheep and seek them out — YHWH's own shepherding (Ezek 34:11-16) is enacted by Jesus as the Good Shepherd; what YHWH promised to do for his abandoned sheep (I myself will shepherd them) is what Jesus claims to be doing: I am the good shepherd"}
    ]
  },
  "36": {
    "25": [
      {"type": "fulfillment", "target": "John 3:5", "note": "I will sprinkle clean water on you and you shall be clean; I will give you a new spirit — the new birth of water and Spirit in John 3:5 is the fulfillment of Ezek 36:25-27; what Ezekiel prophesied as the new covenant's cleansing and Spirit-filling is what Jesus announces as the necessary birth for entering the kingdom"}
    ]
  },
  "37": {
    "1": [
      {"type": "allusion", "target": "John 11:43-44", "note": "The valley of dry bones that come to life at YHWH's breath-word — Jesus's command 'Lazarus, come out' is the personal enactment of the eschatological resurrection vision of Ezek 37; the Spirit's breath (John 20:22) that animates the church repeats the pattern of Ezek 37:9-10"}
    ]
  },
  "47": {
    "1": [
      {"type": "fulfillment", "target": "Rev 22:1", "note": "The river of water flowing from the temple — Ezekiel's visionary river (increasingly deep, bringing life to everything it touches) is fulfilled in Revelation's river of life flowing from the throne of God and the Lamb; Jesus is himself the source of living water (John 7:38-39)"}
    ]
  }
}

EZEK_ORIGINAL = {
  "1": {
    "28": "<p><strong>ke-mareh haqeshet asher yihyeh beanav beyom hagashem ken mareh hanog saviv hu mareh demut kevod YHWH</strong>: 'Like the appearance of the bow that is in the cloud on the day of rain, so was the appearance of the brightness all around. Such was the appearance of the likeness of the glory of YHWH.' Ezekiel's theophany of the divine chariot-throne (<em>merkabah</em>) is the foundation of Jewish mystical speculation. His careful qualification of language — 'likeness of the glory of YHWH' rather than 'glory of YHWH' — maintains divine transcendence even in the vision. John of Revelation reuses Ezekiel's visionary vocabulary (the four living creatures of Ezek 1 reappear in Rev 4:6-8; the rainbow around the throne in Rev 4:3 echoes Ezek 1:28), grounding the Christological throne-vision in the Ezekielian framework.</p>"
  },
  "36": {
    "26": "<p><strong>venathati lachem lev hadash veruach hadasha etten bekirbechem vahashirothi et-lev haeben mivsarchem venatati lachem lev basar</strong>: 'And I will give you a new heart and a new spirit I will put within you. And I will remove the heart of stone from your flesh and give you a heart of flesh.' The new heart-new spirit promise is the Ezekielian new covenant (parallel to Jer 31:31-34). <em>Lev hadash</em> (new heart): the decision-making center (<em>lev</em>) of human personhood is replaced — not repaired, not improved, but new. <em>Ruach hadasha</em> (new spirit): YHWH's own Spirit placed within (v. 27: 'I will put my Spirit within you and cause you to walk in my statutes'). This is Pentecost prophesied — the Spirit's indwelling that replaces external Torah-motivation with internal Spirit-empowered desire and ability to obey.</p>"
  }
}

EZEK_CONTEXT = {
  "1": {
    "1": "<p>Ezekiel was a priest who was deported to Babylon in the first deportation (597 BCE) and received his call-vision in 593 BCE by the Chebar canal in Babylonia ('the thirtieth year', 1:1 — possibly his own thirtieth year, the age for priestly service). He prophesied to the exilic community ca. 593-571 BCE. His priestly background shapes his theology: the book is preoccupied with divine glory (<em>kavod</em>), the departure of the Shekinah from the temple (chs. 8-11), and its eschatological return (chs. 40-48). The merkabah vision (ch. 1) was the most influential single vision in subsequent Jewish mysticism — the Hekhalot literature built an entire tradition of heavenly ascent around it. The four living creatures (lion, ox, eagle, human) reappear in Irenaeus's identification of the four Gospel symbols.</p>"
  },
  "37": {
    "1": "<p>The valley of dry bones vision (37:1-14) is addressed to the exilic community that had concluded 'our bones are dried up, our hope is lost, we are indeed cut off' (v. 11). The corporate resurrection metaphor — national restoration envisioned as bodily resurrection — uses the imagery of physical resurrection for Israel's return from exile. This is not a straightforward prophecy of individual eschatological resurrection (though the same imagery is applied there in Isa 26:19; Dan 12:2), but a bold use of resurrection as the metaphor for what only divine creative power could accomplish for the exiled nation. The NT develops the resurrection-from-exile typology: Christ's resurrection is both personal and the beginning of the great return-from-death that Ezekiel envisioned.</p>"
  }
}

EZEK_CHRIST = {
  "34": {
    "11": "<p>A direct revelation: 'For thus says the Lord GOD: Behold I, I myself will search for my sheep and seek them out ... I will rescue them from all places where they have been scattered ... I will seek the lost and I will bring back the strayed and I will bind up the injured and I will strengthen the weak.' Jesus's 'I am the good shepherd' (John 10:11) and the parable of the lost sheep (Luke 15:4-6) are the incarnational enactment of Ezek 34's promise. What YHWH said he himself would do (in contrast to the failed shepherds of Israel's leaders) is what Jesus does: the divine shepherd-promise is fulfilled by the Son who is YHWH present in person, doing what YHWH promised he personally would do for the scattered flock.</p>"
  },
  "36": {
    "27": "<p>A direct revelation: 'And I will put my Spirit within you and cause you to walk in my statutes and be careful to obey my rules.' Pentecost is Ezekiel 36:27 enacted. The Spirit's indwelling is not merely motivational but causally efficacious: 'I will cause you to walk' — the Hebrew Hiphil form makes YHWH the enabling cause of the obedience that follows. This is the new covenant's answer to the old covenant's demand without the enabling Spirit: the same Torah-standard now fulfilled because the Spirit from within enables what the law from without could only command. Paul's 'the righteous requirement of the law might be fulfilled in us who walk not according to the flesh but according to the Spirit' (Rom 8:4) is the Christological-pneumatological fulfillment of Ezek 36:27.</p>"
  },
  "47": {
    "9": "<p>A type: 'And wherever the river goes, every living creature that swarms will live, and there will be very many fish. For this water goes there, that the waters of the sea may become fresh; so everything will live where the river goes.' The eschatological temple-river of Ezekiel's vision (ch. 47), increasingly deep and life-giving, is the OT type for the water that flows from Christ. Jesus at Tabernacles (John 7:38-39) applies the Spirit-water promise to himself: 'rivers of living water will flow from within him' — and John explains this is the Spirit. Revelation's new creation river (22:1) flowing from the throne of God and the Lamb completes the Ezekiel type: the new temple's river is Christ himself, and all who drink from him live.</p>"
  }
}

# ============================================================
# DANIEL
# ============================================================

DAN_ECHO = {
  "2": {
    "44": [
      {"type": "fulfillment", "target": "Luke 1:33", "note": "The God of heaven will set up a kingdom that shall never be destroyed — the stone that becomes a great mountain filling the whole earth (Dan 2:35, 44) is fulfilled in the kingdom announced by the angel: his kingdom will have no end"},
      {"type": "fulfillment", "target": "Rev 11:15", "note": "The kingdom of the world has become the kingdom of our Lord and of his Christ — the seventh trumpet's announcement is the explicit fulfillment of Dan 2:44's never-to-be-destroyed kingdom of heaven"}
    ]
  },
  "7": {
    "13": [
      {"type": "fulfillment", "target": "Matt 26:64", "note": "You will see the Son of Man seated at the right hand of Power and coming on the clouds of heaven — Jesus applies Dan 7:13 to himself before the Sanhedrin; the coming on the clouds of heaven is the exaltation of the Son of Man to the divine throne, which the high priest recognizes as blasphemy"},
      {"type": "fulfillment", "target": "Acts 1:9", "note": "A cloud took him out of their sight — the ascension cloud echoes the Son of Man coming with the clouds of Dan 7:13; the ascension is the enthronement, not a departure to a distant location"},
      {"type": "fulfillment", "target": "Rev 1:7", "note": "Behold he is coming with the clouds — Revelation combines Dan 7:13 with Zech 12:10 to describe the parousia as the final manifestation of the Son of Man's cloud-coming that began at the ascension"}
    ]
  },
  "9": {
    "24": [
      {"type": "allusion", "target": "Luke 4:18", "note": "To anoint a most holy place — the seventy weeks leading to the anointing of the most holy one (or most holy place) has been interpreted as pointing to Christ's anointing at baptism; the messianic anointing is the fulfillment of Daniel's eschatological program"},
      {"type": "allusion", "target": "Heb 9:26", "note": "To finish transgression, put an end to sin, and atone for iniquity — the six goals of Daniel's seventy weeks (9:24) are summarized in Hebrews: he has appeared once for all at the end of the ages to put away sin by the sacrifice of himself"}
    ]
  },
  "12": {
    "2": [
      {"type": "fulfillment", "target": "John 5:28-29", "note": "Many who sleep in the dust of the earth shall awake, some to everlasting life and some to shame and everlasting contempt — Jesus's promise of a resurrection of all the dead, some to life and some to judgment, applies Dan 12:2's general resurrection language to himself as the one who gives life and judges"}
    ]
  }
}

DAN_ORIGINAL = {
  "7": {
    "13": "<p><strong>hazeh haveit bechezwe leylaya vaara im-anane shemayya kebar enash ateh vead attiq yomaya matah uqdamoy haytivuhi</strong> (Aramaic): 'I saw in the night visions, and behold, with the clouds of heaven there came one like a son of man, and he came to the Ancient of Days and was presented before him.' The 'one like a son of man' (<em>kebar enash</em>, Aramaic for 'like a human being') in Daniel 7 contrasts with the four beasts (lions, bears, leopards, a terrible beast) that rise from the sea — representing successive human empires. The human figure comes from heaven, not the sea, and receives the dominion the beasts claimed. The NT application (Jesus's self-designation as 'Son of Man' in all four Gospels) is the consistent claim that Jesus is this figure who receives eternal dominion from the Ancient of Days — a claim recognized as divine by the Sanhedrin (Mark 14:62-64).</p>"
  },
  "9": {
    "24": "<p><strong>shivim shavuim nechetach al-amecha vehal ir qadshecha lekale happesha ulehatem chataut velchapper avon ulehavi tsdeq olamim velachtom chazot venavia velimshoach qodesh qodashim</strong>: 'Seventy weeks are decreed about your people and your holy city, to finish the transgression, to put an end to sin, to atone for iniquity, to bring in everlasting righteousness, to seal both vision and prophet, and to anoint a most holy place.' The six infinitives of Dan 9:24 have generated centuries of calculation and debate. The <em>shavuim</em> (weeks/sevens) are most naturally weeks of years (seven-year units), giving 490 years from the decree to rebuild Jerusalem. The six goals — which are systematically soteriological and eschatological — align most naturally with Christ's work: atonement (to finish transgression, atone for iniquity), righteousness (bring in everlasting righteousness), and the end of the prophetic age (seal vision and prophet).</p>"
  }
}

DAN_CONTEXT = {
  "1": {
    "1": "<p>The book of Daniel is set in the Babylonian exile (605-538 BCE) and narrates the experiences of four young Jewish men under Nebuchadnezzar, Belshazzar, Darius the Mede, and Cyrus of Persia. The historical reliability of Daniel's court settings has been debated (Darius the Mede is unattested by name in Babylonian records; some details seemed anachronistic). The primary critical alternative: Daniel was composed ca. 167-164 BCE during the Maccabean revolt, as <em>vaticinium ex eventu</em> (prophecy after the fact) using the fictional setting of the sixth century. Conservative scholars argue for a sixth century date and understand the Darius question as a secondary title for Cyrus or an otherwise unrecorded official. The book's affinities with the Aramaic of the fifth-fourth centuries and the absence of Greek loanwords that would be expected in a second century BCE composition support an early composition.</p>"
  },
  "7": {
    "1": "<p>Daniel 7-12 contains four major apocalyptic visions. The genre of apocalypse (from Greek <em>apokalypsis</em>, unveiling) is characterized by: symbolic or heavenly visions mediated by an angel, disclosure of the heavenly perspective on historical events, periodization of history into fixed sequences, and imminent divine intervention. Daniel is the OT's primary apocalyptic text; its imagery (beasts from the sea, the Ancient of Days, the Son of Man, the four kingdoms) was enormously influential on Jewish and Christian apocalyptic (1 Enoch, 4 Ezra, 2 Baruch, and the NT's Revelation). Jesus's eschatological discourse (Mark 13 and parallels) draws extensively from Daniel, particularly the abomination of desolation (Dan 11:31; 12:11 → Mark 13:14) and the coming of the Son of Man (Dan 7:13 → Mark 13:26).</p>"
  }
}

DAN_CHRIST = {
  "7": {
    "13": "<p>A direct revelation: 'One like a son of man came with the clouds of heaven and came to the Ancient of Days and was presented before him. And to him was given dominion and glory and a kingdom, that all peoples, nations, and languages should serve him; his dominion is an everlasting dominion, which shall not pass away, and his kingdom one that shall not be destroyed.' Jesus's consistent self-identification as 'the Son of Man' throughout the Gospels is a deliberate claim to be this figure — the one who receives from the Ancient of Days the universal, eternal dominion. The ascension is the receiving of this dominion; Pentecost is the beginning of its exercise; the parousia is its final manifestation. The 'Son of Man' claim is Jesus's most characteristic and most Christologically loaded self-designation.</p>"
  },
  "9": {
    "26": "<p>A fulfillment: 'After sixty-two weeks, an anointed one shall be cut off and shall have nothing.' The phrase 'cut off' (<em>yikaret</em>) is the judicial-death vocabulary of Torah (used for capital offenses). The anointed one is cut off not for his own sins (the grammar allows 'and there is nothing to him' or 'but not for himself') — the same pattern as Isa 53:8 ('cut off out of the land of the living ... for the transgression of my people'). Regardless of the precise calculation of the seventy weeks, the Christological core is the same: the anointed one (the Messiah) dies, is cut off, apparently without inheriting anything — and yet this death is the very mechanism by which the six goals of v. 24 are accomplished. The cross is Daniel's predicted event.</p>"
  },
  "12": {
    "2": "<p>A direct revelation: 'And many of those who sleep in the dust of the earth shall awake, some to everlasting life and some to shame and everlasting contempt.' Daniel 12:2 is the OT's clearest statement of a general resurrection with differentiated outcomes — resurrection to life and resurrection to judgment. Jesus applies this directly to himself: 'The hour is coming when all who are in the tombs will hear his voice and come out, those who have done good to the resurrection of life and those who have done evil to the resurrection of judgment' (John 5:28-29). Christ is the voice that summons from the tombs — the executor of Daniel's two-outcome resurrection — and his own resurrection is the first fruits of what Dan 12:2 prophesied for the final eschatological hour.</p>"
  }
}

def main():
    books_data = [
        ('deuteronomy', DEUT_ECHO, DEUT_ORIGINAL, DEUT_CONTEXT, DEUT_CHRIST),
        ('jeremiah', JER_ECHO, JER_ORIGINAL, JER_CONTEXT, JER_CHRIST),
        ('ezekiel', EZEK_ECHO, EZEK_ORIGINAL, EZEK_CONTEXT, EZEK_CHRIST),
        ('daniel', DAN_ECHO, DAN_ORIGINAL, DAN_CONTEXT, DAN_CHRIST),
    ]
    for book, echo_d, orig_d, ctx_d, chr_d in books_data:
        e = load_echo(book)
        merge_echo(e, echo_d)
        save_echo('', e) if False else save_echo(book, e)

        c = load_comm('mkt-original', book)
        merge_comm(c, orig_d)
        save_comm('mkt-original', book, c)

        c = load_comm('mkt-context', book)
        merge_comm(c, ctx_d)
        save_comm('mkt-context', book, c)

        c = load_comm('mkt-christ', book)
        merge_comm(c, chr_d)
        save_comm('mkt-christ', book, c)
        print(f'{book}: all 4 layers written')

if __name__ == '__main__':
    main()
