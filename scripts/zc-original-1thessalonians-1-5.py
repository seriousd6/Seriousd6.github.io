"""
MKT Original Language Commentary — 1 Thessalonians chapters 1–5 (complete)
Run: python3 scripts/zc-original-1thessalonians-1-5.py

Source data used:
- data/interlinear/1thessalonians.json
- data/translation/glossary-greek.json (agapē G26 dispute_level=3; elpis G1680 dispute_level=2;
  hagios G40 dispute_level=2; skeuos G4632 vessel/wife dispute)
- data/translation/notes/1thessalonians.json (translation decisions per verse)
- data/translation/draft/mediating/1thessalonians.json (MKT text for quoting)

Also retains original multi-layer script content below (for 2 Thessalonians layers).

Key decisions in this range:
- agapē (G26, dispute_level=3): MKT uses "love"; covenantal-active sense flagged where significant
- elpis (G1680, dispute_level=2): confident expectation, not mere wish
- skeuos (4:4): body-reading preferred; wife-reading noted as live ancient interpretation
- hagioi (3:13): "holy ones" kept deliberately ambiguous (angels vs glorified saints)
- parousia (4:15-16): imperial/royal-visit terminology noted
- 2:7 nēpioi vs ēpioi: nēpioi (infants) treated as original lectio difficilior
- 4:15 "Lord's word": apostolic agraphon not in the canonical Gospels
- 5:23 tripartite anthropology: totality expression, not technical trichotomy
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
# 1 THESSALONIANS — comprehensive original-language commentary
# ============================================================

ONETHESS_ORIGINAL_FULL = {
  "1": {
    "1": '<p>Paul opens with the simplest of his letter salutations — no lengthy apostolic title. The community is addressed as being "in God the Father and the Lord Jesus Christ" — a double prepositional phrase that locates the assembly within the divine persons rather than merely under their authority. This construction is unprecedented in Greek epistolary convention.</p>',
    "2": '<p>"We always give thanks" (<em>eucharistoumen pantote</em>) — <em>pantote</em> (always) holds first position in the sentence for emphasis; thanksgiving is continuous. "Mention you in our prayers" (<em>mneian poioumenoi</em>) — <em>mneia</em> covers both remembering and mentioning in prayer; the two acts are inseparable for Paul.</p>',
    "3": '<p>The triad <em>pistis</em> (faith), <em>agapē</em> (love), <em>elpis</em> (hope) appears here in its earliest Pauline occurrence, listed in reverse order from 1 Cor 13:13 — as "work of faith, labor of love, endurance of hope." <em>Ergon</em> (work), <em>kopos</em> (toil — the more strenuous word for exhausting labor), and <em>hypomonē</em> (patient endurance) characterize each virtue\'s activity respectively.</p><p><em>Agapē</em> (G26, dispute_level=3): glossary notes lit="love," tho="self-giving love." Here it drives exhausting communal labor — the covenantal-active sense is primary. <em>Elpis</em> (G1680, dispute_level=2): not a wish but confident expectation grounded in the resurrection (v.10); it generates endurance because it is certain.</p>',
    "4": '<p>"Loved by God" (<em>ēgapēmenoi hypo theou</em>) — perfect passive participle: God\'s completed act of love with permanent present result. "Chosen" (<em>eklogēn</em>) — election noun; <em>eklogē</em> is the LXX term for Israel\'s covenant election. Paul applies it to a Gentile community in a Greek city — a deliberate transfer of election-vocabulary.</p>',
    "5": '<p>"Not simply with words but also with power, with the Holy Spirit and deep conviction" — three instrumental datives: <em>dynamei</em> (power), <em>pneumati hagiō</em> (Holy Spirit), <em>plērophoria pollē</em> (full assurance). <em>Plērophoria</em> is a compound: <em>plēroō</em> (fill) + bearing = complete, thorough conviction. This is Paul\'s first use of this rare word; it names the quality of internal certainty that distinguishes genuine apostolic proclamation from mere rhetoric.</p>',
    "6": '<p>"Imitators" (<em>mimētai</em>) — discipleship through imitation of apostolic behavior. "Welcomed the message in the midst of severe suffering with the joy given by the Holy Spirit" — the paradox: <em>en thlipsei pollē meta charās pneumatos hagiou</em>. The joy is pneumatically caused (<em>pneumatos hagiou</em> is a genitive of source); it is not stoic endurance but Spirit-produced delight that coexists with affliction without denying it.</p>',
    "7": '<p>"You became a model" (<em>typon</em>) — singular; the community functions as a single die-stamp impression (<em>typos</em> = the impression left by a die; our word "type" derives from this). The Thessalonians are not one among several examples but the paradigmatic pattern for the surrounding region.</p>',
    "8": '<p>"Rang out from you" (<em>exēchētai</em>) — perfect passive of <em>exēcheō</em>: has sounded out and continues reverberating. The verb contains <em>ēchē</em> (echo, sound); the gospel has spread like a trumpet blast from Thessalonica. "In every place" (<em>en panti topō</em>) — hyperbolic but indicating spread beyond the immediate regions named.</p>',
    "9": '<p>"Turned to God from idols" (<em>epestrespsate pros ton theon apo tōn eidōlōn</em>) — <em>epistrephō</em> is the LXX term for Israel\'s covenant "return" to YHWH after apostasy (Hos 3:5; Jer 4:1). Paul applies it to Gentile conversion — the pagan-to-God movement uses the vocabulary of Israel\'s return to covenant. <em>Eidōla</em> (idols) contrasts with "the living and true God" (<em>theō zōnti kai alēthinō</em>) — two adjectives naming what idols lack: life and truth.</p>',
    "10": '<p>"Wait for his Son from heaven" — <em>anamenein</em> is a NT hapax (only occurrence); more intensive than <em>menō</em> alone; waiting-toward, waiting-in-anticipation. "Whom he raised from the dead" — the resurrection grounds the eschatological waiting; the returning Son is historically grounded.</p><p>"Rescues us from the coming wrath" (<em>ton ryomenon hēmas ek tēs orgēs tēs erchomenēs</em>) — present participle <em>ryomenon</em>: rescuing is an ongoing characteristic, not only future. The wrath is "coming" (<em>erchomenēs</em>, present participle) — already in motion.</p>'
  },
  "2": {
    "1": '<p>"Not without results" (<em>ou kenē gegonen</em>) — <em>kenē</em> = empty/vain; the perfect tense (<em>gegonen</em>) states a completed fact with present standing. Paul will use <em>kenē</em> again (1 Cor 15:14) for gospel proclamation that would be empty without the resurrection. Here it asserts the abiding fruitfulness of his visit.</p>',
    "2": '<p>"Suffered and been treated outrageously in Philippi" — <em>propathontes</em> and <em>hybristhentes</em> (aorist participles): past completed actions summarizing Acts 16. <em>Hybrizō</em> (to outrage) is a strong term for deliberate public humiliation. "We dared" (<em>eparrēsiasametha</em>) — <em>parrēsia</em> = frank, free, bold speech; the noun names the courage of speaking plainly regardless of risk.</p>',
    "3": '<p>The three negatives are formal disclaimers of the sophist\'s standard vices: not from "error" (<em>planēs</em> — moral delusion), not from "impure motives" (<em>akatharsias</em>), not through "deceit" (<em>dolō</em> — bait, trick). These three categories correspond to the accusations commonly made against wandering teachers in the Greco-Roman world.</p>',
    "4": '<p>"Approved by God" (<em>dedokimasmetha hypo tou theou</em>) — perfect passive of <em>dokimazō</em>: tested and having been found genuine, approved. The metallurgical image is of assaying metal — heating to certify purity. "Who tests our hearts" (<em>tō dokimazonti tas kardias hēmōn</em>) — present participle; God\'s testing is ongoing, making human approval irrelevant.</p>',
    "5": '<p>"Flattery" (<em>kolakeias</em>) — NT hapax; the obsequious behavior of those who say what audiences want to hear for personal advantage. "Mask to cover up greed" (<em>prophasis pleonexias</em>) — <em>prophasis</em> = pretext/cover-story; <em>pleonexia</em> = greediness. Together: a cover story concealing desire for financial or social gain.</p>',
    "6": '<p>"Assert our authority" (<em>en barei einai hōs Christou apostoloi</em>) — literally "to be in weight/heaviness"; <em>baros</em> = burden/weight, both financially (demanding material support) and socially (pulling rank). Paul deliberately waived the authority-claim that was his right as an apostle.</p>',
    "7": '<p>The significant textual variant: <em>nēpioi</em> (infants, the harder reading) vs <em>ēpioi</em> (gentle). If <em>nēpioi</em> is original (lectio difficilior principle), the mixed metaphor is dramatic: infants who became a nursing mother. A nursing mother (<em>trophos</em>) is warm, physically intimate, and self-giving — no itinerant sophist would have used this image for himself.</p>',
    "8": '<p>"Share with you... our lives as well" (<em>tas heautōn psychas</em>) — <em>psychas</em> = souls/lives; Paul offered not just a message but his whole person. "Because we loved you so much" (<em>dioti agapētoi hēmin egenēthēte</em>) — perfect passive: you became and remain beloved to us. The community was not a mission target but persons who became dear.</p>',
    "9": '<p>"Toil and hardship" (<em>kopos kai mochthos</em>) — a fixed pair (also 2 Cor 11:27; 2 Thess 3:8): <em>kopos</em> = wearying labor, <em>mochthos</em> = hardship/drudgery. "Working night and day" (<em>nyktos kai hēmeras</em>) — genitive of time throughout the night and day; probably tent-making (Acts 18:3), which distinguishes Paul from philosophers who received patron support.</p>',
    "10": '<p>"Holy, righteous and blameless" (<em>hosiōs kai dikaiōs kai amemptōs</em>) — three adverbs of manner: <em>hosiōs</em> (devoutly toward God), <em>dikaiōs</em> (righteously toward people), <em>amemptōs</em> (blamelessly, without accusation). The triad covers the vertical God-relation and horizontal human-relation of integrity.</p>',
    "11": '<p>Three participles for fatherly formation: <em>parakaloumenoi</em> (exhorting/encouraging), <em>paramythoumenoi</em> (comforting/consoling — the warmer word), <em>martyromenoi</em> (earnestly urging, bearing witness-like testimony to). Each describes a distinct mode of apostolic care for individual community members.</p>',
    "12": '<p>"Live lives worthy of God" (<em>peripatein axiōs tou theou</em>) — <em>peripateō</em> (walk/conduct life) is Paul\'s preferred ethical verb; <em>axiōs</em> means proportionately, fittingly — in a manner commensurate with. "His kingdom and glory" — both dimensions shape the ethical demand: present participation in the kingdom-reality and future eschatological glory.</p>',
    "13": '<p>"Word of God... at work in you" (<em>ho kai energeitai en hymin tois pisteuousin</em>) — <em>energeitai</em> is present tense: the word is actively energizing (our "energy" is from this root). The word received is not inert information but a dynamic agent working in recipients. "Not as a human word" — Paul distinguishes the divine origin from the human medium.</p>',
    "14": '<p>"Suffered from your own people" (<em>hypo tōn idiōn symphyletōn</em>) — <em>symphyletai</em> = fellow-tribesmen, those of the same ethnic/civic group. The Thessalonians\' persecutors are their own Gentile neighbors, creating suffering-solidarity with the Judean Jewish-Christian communities who faced opposition from their own people.</p>',
    "15": '<p>"Who killed the Lord Jesus and the prophets" — the sequence is striking: Jesus named first, then the prophets; chronologically reversed but theologically ordered. The death of Jesus is the climax of a pattern of prophetic rejection embedded in Israel\'s history (cf. Matt 23:37). Paul speaks as a Jew himself using intra-Jewish prophetic critique.</p>',
    "16": '<p>"Wrath has come upon them at last" (<em>ephthasen de ep\' autous hē orgē eis telos</em>) — <em>ephthasen</em> is aorist: arrived, reached. <em>Eis telos</em> = finally, to the uttermost, completely. The verb <em>phthanō</em> (to arrive, come upon) generates debate: prophetic perfect (future wrath spoken as arrived) or reference to a specific event Paul knew. The wrath is presented as a completed arrival, not merely imminent threat.</p>',
    "17": '<p>"Orphaned by being separated from you" (<em>aporphanisthentes aph\' hymōn</em>) — <em>aporphanizō</em> = to be made an orphan; NT hapax. The parting-of-parent-from-child image recalls the nursing-mother and father metaphors of 2:7-11; the separation is experienced as bereavement, not inconvenience. "For a short time in person, not in thought" (<em>pros kairon hōras, prosōpō ou kardia</em>) — the physical absence does not sever the relational bond; the idiom "face but not heart" makes visible what is invisible.</p>',
    "18": '<p>"Satan blocked our way" (<em>enekopsen hēmas ho Satanas</em>) — <em>enkoptō</em> (to cut into, block, hinder): a military term for cutting a road to stop an advancing army. Satan is presented as an active personal agent who physically impeded apostolic travel; Paul does not speculate about how. The acknowledgment of Satanic agency in thwarting ministry plans is direct and without embarrassment.</p>',
    "19": '<p>"Our hope, our joy, or the crown in which we will glory" (<em>elpis hē chairē kai stephanos kauchēseōs</em>) — the three nouns of eschatological celebration: hope, joy, and the victory-crown. <em>Stephanos</em> (wreath/crown) is the athletic or civic crown of victory or honor, not the royal diadem (<em>diadēma</em>). The crown of boasting (<em>kauchēseōs</em>) is the honor that Paul will carry to present before the Lord at the parousia — and that honor is the community itself.</p>',
    "20": '<p>"You are our glory and joy" (<em>hymeis gar este hē doxa hēmōn kai hē chara</em>) — the declarative statement completes the rhetorical question of v.19. The community is not merely the occasion of Paul\'s joy but constitutes it: <em>este</em> = you are (present: now and ongoing). The apostle\'s eschatological glory is his converts standing before Christ. The community is the apostle\'s crown.</p>'
  },
  "3": {
    "1": '<p>"When we could stand it no longer" (<em>mēketi stegontes</em>) — <em>stegō</em> = to cover, contain, bear; "we could no longer contain/bear it." The idiom expresses emotional pressure beyond capacity. The decision to stay alone in Athens involves real cost — Timothy was Paul\'s most trusted co-worker.</p>',
    "2": '<p>"Co-worker in God\'s service" (<em>synergon tou theou</em>) — the more striking manuscripts read "God\'s co-worker" (with the genitive of God). Timothy is named as working together with God — an elevation of apostolic labor into divine partnership that is remarkable in its directness.</p>',
    "3": '<p>"Destined for them" (<em>keimetha</em>) — present tense of <em>keimai</em>: to lie, to be set/placed. Paul and his companions are positioned in affliction by divine appointment. The passive and the image of being laid in a specific position conveys intentionality behind the suffering — it is placed, not random.</p>',
    "4": '<p>"We kept telling you" (<em>proelegomen</em>) — imperfect of repeated telling: we were continually foretelling. "We are going to be afflicted" (<em>mellomen thlibesthaii</em>) — <em>mellō</em> + infinitive = certainty of imminent future; the persecution was foretold and its arrival is confirmation, not refutation, of the apostolic announcement.</p>',
    "5": '<p>"The tempter" (<em>ho peirazōn</em>) — present participle as a title: the one whose defining ongoing activity is temptation. "Our efforts might have been useless" (<em>eis kenon genētai ho kopos hēmōn</em>) — <em>kenon</em> (into emptiness): the labor might become void. The concern is for the community\'s perseverance, not the apostle\'s reputation.</p>',
    "6": '<p>"Good news" (<em>euangelisamenou</em>) — Paul uses the gospel-verb itself for Timothy\'s report. The community\'s condition is news cast in gospel terms: it is itself good news. This reverse-gospel (community to apostle) is a unique usage that reveals how thoroughly Paul\'s language is shaped by the proclamation.</p>',
    "7": '<p>"Because of your faith" (<em>dia tēs hymōn pisteōs</em>) — the causal preposition: their faith is the mechanism of Paul\'s consolation. The Thessalonians\' steadfastness sustains the apostle in his own distress — a striking inversion of the expected teacher-student flow.</p>',
    "8": '<p>"Now we really live" (<em>nun zōmen</em>) — emphatic present. "Since you are standing firm in the Lord" (<em>ean hymeis stēkete en kyriō</em>) — <em>stēkō</em> (stand firm) is the military posture of holding ground; <em>en kyriō</em> specifies where the standing occurs: in the sphere of the Lord\'s presence. Their steadiness in the Lord is the condition of Paul\'s vitality.</p>',
    "9": '<p>"How can we thank God enough" (<em>tina gar eucharistian dynametha tō theō antapodounai</em>) — <em>antapodounai</em> = to give back in return; thanksgiving as unpayable debt. The rhetorical question implies the answer: no adequate return is possible. The community\'s existence generates more joy than can be adequately returned to God in thanksgiving.</p>',
    "10": '<p>"Supply what is lacking in your faith" (<em>katartisai ta hysterēmata tēs pisteōs hymōn</em>) — <em>katartizō</em> = to mend, restore, complete (used for mending fishing nets, Matt 4:21). Faith has elements not yet fully formed; the apostle\'s desire is to complete, not merely maintain, what has begun.</p>',
    "11": '<p>"Clear the way" (<em>kateuthinai tēn hodon hēmōn</em>) — <em>kateuthynō</em> = to make straight, direct (Prov 4:26 LXX; 2 Thess 3:5). Both God the Father and the Lord Jesus are addressed equally as agents of providential guidance — a high Christological assumption embedded without argument in a prayer.</p>',
    "12": '<p>"Increase and overflow" (<em>pleonasai kai perisseuai</em>) — two verbs of superabundance: <em>pleonazō</em> (become more, multiply) + <em>perisseuō</em> (abound, overflow). Neither sufficiency nor adequacy is the standard; love is to be in excess of what the situation demands. "For each other and for everyone else" — intra-community and outward to all.</p>',
    "13": '<p>"Holy ones" (<em>hagiōn</em>) — deliberately ambiguous: angels (cf. Zech 14:5 LXX where the LORD comes with his holy ones in an angelic context) or glorified saints. The MKT preserves "holy ones" to maintain the productive ambiguity that the Greek sustains. Either reading implies the parousia is attended by a heavenly entourage.</p><p>"Blameless and holy" (<em>amemptous en hagiōsynē</em>) — <em>amemptos</em> (without accusation) + <em>hagiōsynē</em> (abstract noun of <em>hagios</em>): standing before God without accusation requires the holiness that is God\'s own character. The prayer asks God to produce what the parousia will require.</p>'
  },
  "4": {
    "1": '<p>"Walk in order to please God" (<em>peripatein kai areskein theō</em>) — the ethical-walk metaphor (<em>peripateō</em>) is Paul\'s consistent frame for moral conduct; Hellenistic philosophy also used "walking" metaphorically. "Pleasing God" is the positive formulation: not conformity to law as such but alignment with the divine character and purpose.</p>',
    "2": '<p>"Instructions we gave by the authority of the Lord Jesus" (<em>dia tou kyriou Iēsou</em>) — the preposition <em>dia</em> (through) marks mediation: the instructions come through the apostle but have their authority from the Lord Jesus. This is not Paul\'s personal teaching program but transmission of the Lord\'s instructions — an apostolic claim of derived authority.</p>',
    "3": '<p>"God\'s will is your sanctification" (<em>touto gar estin thelēma tou theou, ho hagiasmos hymōn</em>) — crisp: this [thing] is God\'s will, the sanctification of you. <em>Hagiasmos</em> (G38): the process and state of being set apart as holy; glossary range = "purification, the state of purity." The divine will is not primarily a set of rules but a state of being — separation unto God.</p>',
    "4": '<p><em>Skeuos</em> (G4632): "vessel/instrument/body/wife" — the lexical dispute. Glossary notes it can mean "a wife as contributing to the husband\'s usefulness." Two main interpretations: (1) each person should control/possess their own body in holiness (dominant modern reading); (2) each man should acquire a wife in a holy manner (patristic reading, followed by some modern scholars). Either way, the qualifiers are identical.</p><p>"Holy and honourable" (<em>en hagiasmai kai timē</em>) — holiness (set-apartness for God) and honor (<em>timē</em> = worth, dignity). The contrast with "passionate lust" (<em>pathei epithymias</em>, v.5) establishes the antithesis: the body or marital life conducted in the sphere of God vs. conducted in the sphere of unbridled desire.</p>',
    "5": '<p>"Not in passionate lust like the pagans who do not know God" — <em>pathos</em> (passion) + <em>epithymia</em> (desire/lust) = the compound of uncontrolled desire; <em>ta ethnē</em> (the Gentiles/pagans) are defined here specifically as those "not knowing God." Ignorance of God is the source of the ethical failure; knowing God produces a different orientation to bodily life.</p>',
    "6": '<p>"Wrong or take advantage of a brother or sister in this matter" (<em>to mē hyperainein kai pleonektein en tō pragmati ton adelphon autou</em>) — <em>hyperainō</em> (go beyond boundaries) + <em>pleonekteō</em> (take advantage, defraud). The context of the sexual ethics section suggests this refers to defrauding a fellow-believer by sexual transgression against him or his household. <em>Pragma</em> (matter) can be a euphemism for sexual activity.</p>',
    "7": '<p>"Not aimed at impurity, but within holiness" (<em>epi akatharsiai all\' en hagiasmai</em>) — the preposition shift: <em>epi</em> + dative of purpose vs <em>en</em> + dative of sphere. The calling was not aimed at impurity as its purpose; it takes place within holiness as its environment. Holiness is the sphere of the calling, not merely its goal.</p>',
    "8": '<p>"Gives his Holy Spirit" (<em>ton didonta to pneuma autou to hagion</em>) — present participle <em>didonta</em>: the giving is continuous, ongoing. God is characteristically and currently the Spirit-giver; the Spirit-gift is an ongoing provision, not only a past event. The one who rejects the apostolic word therefore rejects the God who is now giving the Spirit.</p>',
    "9": '<p>"Taught by God to love" (<em>theodidaktoi</em>) — NT hapax; Paul coins the compound: <em>theos</em> + <em>didaktos</em> (God-taught). This likely echoes Isa 54:13 ("all your children will be taught by the LORD") and Jer 31:34 ("they will all know me") — the new covenant promise of direct divine teaching being fulfilled in the community\'s Spirit-formed love.</p>',
    "10": '<p>"You do love all of God\'s family throughout Macedonia" — the network of believers in Macedonia (Philippi, Beroea, and others) is held together by <em>philadelphia</em> (brotherly love) already practiced. "Yet urge you to do so more and more" (<em>perisseuein mallon</em>) — more-and-more-abundant is consistently the Pauline standard; present sufficiency is never the limit.</p>',
    "11": '<p>"Lead a quiet life" (<em>philotimeisthai hēsychazein</em>) — paradoxical construction: <em>philotimeomai</em> = to be ambitious, eager for honor (carrying Greco-Roman honor-competition connotations). Paul calls for ambitious pursuit of <em>hēsychia</em> (quietness). "Work with your hands" — specifically manual labor; counter-cultural in a world where artisanal work was low-status.</p>',
    "12": '<p>"Win the respect of outsiders" (<em>euschemōnōs peripatēin pros tous exō</em>) — <em>euschemōnōs</em> = in a well-formed, fitting, decorous manner. The community\'s visible conduct matters to those outside it. "Not dependent on anybody" (<em>mēdenos chreian echēte</em>) — economic self-sufficiency as honorable community life; dependence on others created social indebtedness in the ancient patron-client system.</p>',
    "13": '<p>"Those who sleep in death" (<em>koimōmenōn</em>) — <em>koimaomai</em> (sleep) as Paul\'s preferred term for Christian death throughout this section. It is not a euphemism that denies death\'s reality but one that reframes it within the resurrection hope: sleep implies waking. "Do not grieve like those who have no hope" — not between grief and no grief but between grief-without-hope and grief-transformed-by-hope; mourning is not eliminated but its character changes.</p>',
    "14": '<p>"We believe that Jesus died and rose again" (<em>pisteuomen hoti Iēsous apethanen kai anestē</em>) — unusually blunt: <em>apethanen</em> (died, plain aorist) without the usual softening. <em>Anestē</em> (stood up, arose) is the intransitive form of resurrection. The creedal formula (cf. 1 Cor 15:3-4) is here applied to the parousia-hope: resurrection solidarity means God will bring the sleeping-in-Jesus with him.</p>',
    "15": '<p>"According to the Lord\'s word" (<em>en logō kyriou</em>) — Paul appeals to a saying of the Lord, likely an agraphon (unwritten tradition) not preserved in the canonical Gospels. This is one of the clearest examples of Paul knowing and transmitting dominical tradition independently of the written Gospel narratives.</p><p>"We who are still alive... will certainly not precede those who have fallen asleep" — Paul includes himself in the "we" of survivors, apparently expecting to be alive at the parousia; he leaves the question of exact timing open throughout.</p>',
    "16": '<p><em>Parousia</em> (G3952): the Greek technical term for a royal or imperial visit; when a king came to a city, an official <em>parousia</em> was announced and the city went out to meet him. Paul uses this politically charged term for Christ\'s coming: it implies authority, public announcement, and the obligation of the community to receive the arriving King.</p><p>Three auditory signals: <em>keleusma</em> (a shout of command — used of military orders and rowing commands), <em>phōnē archangelou</em> (voice of the archangel — only NT occurrence of the archangel\'s voice as a distinct signal), <em>salpinx theou</em> (trumpet of God — the eschatological shofar of Isa 27:13; Matt 24:31; 1 Cor 15:52). The triple signal marks an arrival of cosmic, unmistakable significance.</p>',
    "17": '<p>"Caught up" (<em>harpagēsometha</em>) — future passive of <em>harpazō</em>: to seize, snatch, carry off suddenly (used of Philip in Acts 8:39; Paul\'s heavenly experience in 2 Cor 12:4; Rev 12:5). The community does not ascend by its own power but is seized by divine initiative.</p><p>"To meet the Lord in the air" (<em>eis apantēsin tou kyriou eis aera</em>) — <em>apantēsis</em> is the technical term for the civic delegation that went out to meet a visiting dignitary and escort him back into the city. The spatial image is of the community going out to receive the arriving King and escort him — not of permanent departure from earth.</p>',
    "18": '<p>"Encourage one another with these words" — <em>parakaleite</em>: the same word that names the Holy Spirit\'s Paraclete-function. The eschatological teaching is given for pastoral use — not theological curiosity but mutual consolation in the face of grief at loss. Doctrine functions here as comfort.</p>'
  },
  "5": {
    "1": '<p>"Times and dates" (<em>chronōn kai tōn kairōn</em>) — the dual terminology: <em>chronos</em> (chronological time, duration) and <em>kairos</em> (appointed time, the critical moment). The same pairing in Acts 1:7. The combination covers both duration and the decisive character of the end-time period.</p>',
    "2": '<p>"Day of the Lord will come like a thief in the night" — <em>hēmera kyriou</em> is the LXX phrase for the Day of YHWH (Amos 5:18; Joel 2:1; Isa 13:6; Zeph 1:14); Paul transfers the Jewish Day-of-YHWH expectation directly to the parousia of Christ. "Like a thief" (<em>hōs kleptēs</em>) — this comparison appears in Jesus\'s own teaching (Matt 24:43; Lk 12:39-40); Paul may be drawing on dominical tradition.</p>',
    "3": '<p>"Destruction will come on them suddenly" (<em>aiphnidios autois ephistatai olethros</em>) — <em>aiphnidios</em> (sudden, unforeseen) + <em>ephistatai</em> (present: stands upon, is approaching). The destruction is already approaching before it arrives. "Labor pains on a pregnant woman" — the OT prophetic image for sudden, unavoidable, intensifying judgment (Isa 13:8; 26:17; Jer 4:31; 6:24). Once begun, birth pains cannot be stopped or reversed.</p>',
    "4": '<p>"Not in darkness so that this day should surprise you like a thief" — <em>en skotei</em> (in darkness): not merely ignorance but the moral-eschatological state of those alienated from God. Being not-in-darkness means the Day\'s arrival will not be an ambush. The community\'s eschatological situation is different in kind from the world around it.</p>',
    "5": '<p>"Children of the light and children of the day" (<em>huioi phōtos... huioi hēmeras</em>) — "sons of" is a Semitic idiom for belonging to a category or being characterized by it. The dualistic light/darkness, day/night language echoes the Community Rule at Qumran (1QS 1:9-10), though Paul\'s use is not deterministic. What matters is behaving consistently with one\'s ontological status.</p>',
    "6": '<p>"Let us not be like others, who are asleep" — the sleep/wakefulness metaphor now operates on two levels simultaneously: literal night-sleep (v.7) and spiritual/moral somnolence. The play on <em>koimōmenoi</em> (sleeping in death, ch.4) and <em>katheudōsin</em> (spiritually unaware, ch.5) is deliberate and productive.</p>',
    "7": '<p>"Those who sleep, sleep at night, and those who get drunk, get drunk at night" — the observation functions as a social-cosmological axiom: night is the domain of sleep and intoxication. Day-people who conduct themselves as night-people have confused their ontological status. The logic is: be what you are; live according to the light to which you belong.</p>',
    "8": '<p>"Breastplate of faith and love... helmet of hope of salvation" (<em>endysamenoi thōraka pisteōs kai agapēs kai perikephalian elpida sōtērias</em>) — Paul adapts the divine warrior\'s armor from Isa 59:17 (where God wears righteousness as a breastplate and salvation as a helmet) to the Christian community. The three theological virtues reappear: faith-love form the breastplate (protecting the vital center); hope-of-salvation is the helmet (protecting the mind against despair).</p>',
    "9": '<p>"God did not appoint us to suffer wrath but to receive salvation through our Lord Jesus Christ" — <em>etheto hēmas</em>: divine intentionality behind the community\'s destiny. The contrast is absolute: <em>orgē</em> (eschatological judgment-wrath) vs <em>peripoiēsin sōtērias</em> (acquisition/obtaining of salvation). The community is destined for salvation; the wrath is real but is not their destination.</p>',
    "10": '<p>"Whether we are awake or asleep" — picking up the sleep/wake imagery but now meaning alive or dead (the same ambiguity as 4:13-15). The constant regardless of condition is union with Christ: "we may live together with him" (<em>hama syn autō zōmen</em>). The parousia-hope is not primarily about events but about eternal communion with the Lord.</p>',
    "11": '<p>"Build each other up" (<em>oikodomeite heis ton hena</em>) — <em>oikodomeō</em> (to build a house/edifice) is Paul\'s architectural metaphor for community formation, dominant in 1 Cor 14. "Just as in fact you are doing" — the indicative before the imperative: you already do this; continue and intensify. Paul affirms existing practice before calling for more.</p>',
    "12": '<p>Three participles describing community leaders without formal titles: <em>kopiontas</em> (laboring exhaustingly — the same word as Paul\'s own toil in 2:9), <em>proistamenous</em> (being set over, leading/caring — the leadership-root that appears in Rom 12:8; 1 Tim 5:17), <em>nouthetountas</em> (warning, putting in mind — <em>nous</em> + <em>tithēmi</em>). Functional descriptions consistent with 1 Thessalonians\' early date before institutionalized church offices.</p>',
    "13": '<p>"Hold them in the highest regard" (<em>hēgeisthai en agapē huperekperissou</em>) — <em>huperekperissou</em> is a triple compound: <em>hyper</em> (above) + <em>ek</em> (out of) + <em>perissos</em> (exceeding) = superabundantly-beyond-measure. One of Paul\'s characteristic push-past-the-limit compounds. The ground is "their work" (<em>dia to ergon autōn</em>) — the labor itself justifies the high regard, not merely their position or status.</p>',
    "14": '<p>Four imperatives for community practice: "warn the idle" (<em>noutheteite tous ataktous</em> — <em>ataktos</em> = disorderly, out of rank; a military term for soldiers out of formation; likely those who abandoned work because of eschatological excitement), "encourage the disheartened" (<em>paramytheisthe tous oligopsychous</em> — small-spirited, faint-hearted), "help the weak" (<em>antechesthe tōn asthenōn</em> — hold fast to/support the weak), "be patient with everyone" (<em>makrothymeite pros pantas</em> — long-tempered toward all, without exception).</p>',
    "15": '<p>"Make sure nobody pays back wrong for wrong" (<em>mē apodidontes kakon anti kakou</em>) — <em>anti</em> = in place of, in exchange for; the retaliation-logic of equivalence. "Always strive to do what is good" (<em>to agathon diōkete</em>) — <em>diōkō</em> = pursue, chase after; the same verb used for persecution. Good is to be pursued with the intensity that persecutors pursue harm.</p>',
    "16": '<p>"Rejoice always" (<em>pantote chairete</em>) — imperative mood makes joy a command. <em>Pantote</em> allows no exception. The brevity (two words in Greek) is itself significant — no qualification, no condition. Paul will elaborate (Phil 4:4) but here the command is bare and unqualified.</p>',
    "17": '<p>"Pray continually" (<em>adialeiptōs proseuchesthe</em>) — <em>adialeiptos</em> = without interruption, without let-up; the same adverb as in 1:2-3. Not a command for unbroken verbal prayer but for a prayerful orientation of the whole life — a disposition of continual address to God that underlies all activity.</p>',
    "18": '<p>"Give thanks in all circumstances" (<em>en panti eucharistite</em>) — <em>en panti</em> = in everything (not for everything, which would make suffering itself the object of thanks, but in every circumstance). "This is God\'s will for you in Christ Jesus" — the divine will specified here is the three-part triad of joy, prayer, thanksgiving; not primarily a set of rules but a posture of relationship.</p>',
    "19": '<p>"Do not quench the Spirit" (<em>to pneuma mē sbennyte</em>) — <em>sbennymi</em> (to extinguish fire) applied to the Spirit; the Spirit-as-fire is standard imagery (Matt 3:11; Acts 2:3-4). The verb acknowledges that the community has the capacity to suppress the Spirit\'s activity — quenching implies neglecting or suppressing, particularly prophetic speech (v.20).</p>',
    "20": '<p>"Do not treat prophecies with contempt" (<em>prophēteias mē exoutheneite</em>) — <em>exoutheneō</em> = to treat as nothing, nullify. The connection with v.19 (Spirit) and v.20 (prophecy) suggests that quenching the Spirit and despising prophecy are related acts. The Spirit\'s primary public expression is prophetic speech; suppressing it suppresses the Spirit.</p>',
    "21": '<p>"Test them all; hold on to what is good" (<em>panta dokimazete, to kalon katechete</em>) — <em>dokimazō</em> (test and if genuine, approve — the same word as 2:4 for God\'s testing of Paul). Prophecy is not to be uncritically received; the community bears discernment responsibility. <em>Katechō</em> (hold fast) = secure hold on the tested-and-approved good.</p>',
    "22": '<p>"Reject every kind of evil" (<em>apo pantos eidous ponērou apechesthe</em>) — <em>eidos</em> = form, kind, species: every species/form of evil, not merely obvious manifestations. <em>Apechō</em> (hold away from, abstain from) is an active distancing; the verb appears in contract papyri meaning "to receive in full and keep at a distance" — the transactional note is absent here but the active withdrawal remains.</p>',
    "23": '<p>"Whole spirit, soul and body" (<em>to pneuma kai hē psychē kai to sōma</em>) — unique in Paul (elsewhere body/spirit or body/soul). This tripartite formula is probably a totality expression rather than a technical trichotomous anthropology: Paul is praying for comprehensive sanctification of the whole person, not defining the parts of the human with philosophical precision. The emphasis is on "through and through" (<em>holoteleis</em> — entirely complete) and "whole" (<em>holoklēron</em> — entire, without missing part).</p><p>"Blameless at the coming (<em>parousia</em>) of our Lord Jesus Christ" — the sanctification prayer is eschatologically oriented: completeness at the parousia is the horizon. The sanctification is God\'s work (v.23a) grounded in God\'s faithfulness (v.24).</p>',
    "24": '<p>"The one who calls you is faithful, and he will do it" (<em>pistos ho kalōn humas, hos kai poiēsei</em>) — <em>pistos</em> (faithful) as a divine attribute grounds the eschatological confidence. "He will do it" — future active indicative; unqualified. The God who calls is the same God who completes; calling and completing are both acts of the same faithful character.</p>',
    "25": '<p>"Brothers and sisters, pray for us" (<em>adelphoi, proseuchesthe kai peri hēmōn</em>) — Paul who has been praying for the Thessalonians (1:2; 3:10-13) requests their prayer in return. Apostolic and communal prayer is mutually constitutive; the apostle is not above the need for the community\'s intercession.</p>',
    "26": '<p>"Greet all God\'s people with a holy kiss" (<em>aspasasthe tous adelphous pantas en philēmati hagiō</em>) — the <em>philēma hagion</em> (holy kiss) appears in all four letters containing greetings (Rom 16:16; 1 Cor 16:20; 2 Cor 13:12). It was a standard greeting in Jewish and early Christian assemblies, physically enacting community belonging; "holy" distinguishes it from ordinary social greeting by its covenantal context.</p>',
    "27": '<p>"I charge you before the Lord to have this letter read to all" (<em>enorkizō hymas ton kyrion</em>) — <em>enorkizō</em> (to put under oath, adjure): a solemn charge by appeal to the Lord himself. The command for public reading to all members ensures the letter\'s authority is not limited to the literate or the leaders. This is one of the earliest explicit instructions for what became the practice of public scripture-reading in Christian assemblies.</p>',
    "28": '<p>"The grace of our Lord Jesus Christ be with you" — the closing benediction echoes and expands the opening salutation (1:1: "Grace and peace to you from God and the Lord Jesus Christ"). The letter that began with grace-and-peace ends with grace alone; the single-term benediction sends the assembly forward in what the letter began with.</p>'
  }
}

# ============================================================
# 1 THESSALONIANS — original / context / christ (sparse, pre-existing)
# ============================================================

ONETHESS_ORIGINAL = {
  "1": {
    "9": "<p><strong>eis to douleuein theo zōnti kai alēithinō kai anameinai ton huion autou ek ton ouranon</strong>: 'to serve a living and true God and to wait for his Son from heaven.' The Thessalonian conversion summary (turned from idols → serve the living God → await the Son) is Paul's earliest explicit parousia-expectation statement. The three-fold movement frames the Christian life: conversion, present service, and eschatological waiting. <em>Anamenein</em> (to await/wait for) is a word of eager, sustained expectation — not passive resignation but active orientation toward the returning Son."
  },
  "4": {
    "14": "<p><strong>ei gar pisteuomen hoti Iesous apethanen kai aneste houtōs kai ho theos tous koimēthentas dia tou Iesou axei syn auto</strong>: 'For since we believe that Jesus died and rose again, even so, through Jesus, God will bring with him those who have fallen asleep.' The first explicit eschatological argument in Paul's letters grounds the resurrection of believers in the resurrection of Jesus: the same God who raised Jesus will raise the dead. The verb sequence — <em>apethanen</em> (died) + <em>aneste</em> (rose) — is the primitive creedal formula (cf. 1 Cor 15:3-4), here applied to the parousia-hope.</p>",

    "16": "<p><strong>en keleusmati en phōnē archangelou kai en salpinggi theou katabēsetai</strong>: 'with a cry of command, with the voice of an archangel, and with the sound of the trumpet of God, he will descend.' Three apocalyptic signals accompany the parousia: <em>keleuema</em> (a command-shout, used of military orders and of the divine word of creation), <em>archaggelou phōnē</em> (archangel's voice — the archangel Michael as warrior-herald in Dan 10:13, 21; 12:1; Rev 12:7), and <em>salpinx theou</em> (the trumpet of God — the shofar-gadol of Isa 27:13; Matt 24:31; 1 Cor 15:52 — the eschatological signal for gathering). All three signals assert the unmistakable, cosmic, publicly announced character of the return.</p>"
  },
  "5": {
    "2": "<p><strong>he hemera kyriou hos kleptes en nykti houtōs erchetai</strong>: 'the day of the Lord comes like a thief in the night.' The 'Day of the Lord' (<em>hemera kyriou</em>) is Paul's use of the prophetic Day-of-YHWH tradition (Amos 5:18-20; Isa 2:12-22; Joel 2:11; Zeph 1:14-18) — originally a day of divine judgment. The 'thief in the night' image for its unexpectedness appears also in Jesus's eschatological teaching (Matt 24:43-44; Luke 12:39-40) and later NT texts (2 Pet 3:10; Rev 3:3; 16:15), indicating a shared tradition. Paul applies it to the parousia: its timing is unknown, its arrival will be sudden, and preparedness (not calculation of dates) is the appropriate response.</p>"
  }
}

ONETHESS_CONTEXT = {
  "2": {
    "1": "<p>Thessalonica (modern Thessaloniki) was the capital of the Roman province of Macedonia, its largest city (population ca. 40,000-65,000), and a major port on the Via Egnatia. As a 'free city' (<em>civitas libera</em>) with its own civic assembly (<em>demos</em>), it had significant autonomy within the Roman provincial system. Paul's accusers before the city authorities (Acts 17:6: 'these who have turned the world upside down') charge him with treason: 'they are all acting against the decrees of Caesar, saying that there is another king, Jesus.' The messianic claim of Jesus's kingship was politically dangerous in a city with a significant imperial cult presence (worshippers of Julius Caesar, Augustus, and the emperors were established in Thessalonica).</p>"
  },
  "4": {
    "13": "<p>The specific concern Paul addresses (those who have died before the parousia, vv. 13-18) arose because the Thessalonian community expected the parousia imminently and was distressed that some of their number had died before it arrived. This is the earliest written evidence of Christians struggling with delayed parousia and the death of community members. Paul's response does not retreat from imminent expectation but uses it to comfort: the dead have not missed the parousia — they will be raised first at the Lord's descent. The passage gave rise to later controversies about soul-sleep vs intermediate state, but Paul's primary concern is comfort (<em>parakaleite</em>, v. 18), not metaphysical precision about the intermediate state.</p>"
  }
}

ONETHESS_CHRIST = {
  "4": {
    "14": "<p>A direct revelation: 'Since we believe that Jesus died and rose again, even so, through Jesus, God will bring with him those who have fallen asleep.' The resurrection of the dead is grounded directly in the resurrection of Jesus — not as an analogy but as a causal mechanism. The same God who raised Jesus exercises the same resurrection-power toward those who died in Jesus. The eschatological hope of 1 Thessalonians is not abstract immortality but the specific, Jesus-mediated, bodily resurrection that the first Christian creed announced. Christology is the foundation of eschatology.</p>",

    "16": "<p>A direct revelation: 'The Lord himself will descend from heaven with a cry of command.' <em>Autos ho Kyrios</em> (the Lord himself) — Paul emphasizes personal presence: the parousia is not a divine energy-event or angelic visitation but the personal return of the same Lord who ascended. The 'Lord' (<em>Kyrios</em>) is Jesus, the risen and ascended one, now enthroned at the right hand of the Father (Phil 2:9-11), who will come personally to complete his saving work. The three apocalyptic signals (cry, archangel, trumpet) frame the personal return in cosmic-eschatological context.</p>"
  },
  "5": {
    "9": "<p>A direct revelation: 'God has not destined us for wrath but to obtain salvation through our Lord Jesus Christ, who died for us so that whether we are awake or asleep we might live with him.' The Christological ground of assurance: the Day-of-the-Lord warning (vv. 2-3) does not apply to believers because God's purpose for them is not wrath but salvation. The mechanism: Christ died for us (<em>hyper hemon</em>) — the substitutionary death is the basis for the assurance. 'Live with him' (<em>hama syn auto zōmen</em>) — the eschatological communion with Christ is both the goal and the ground of present courage in the face of the Day.</p>"
  }
}

# ============================================================
# 2 THESSALONIANS — echo + original + context + christ
# ============================================================

TWOTHESS_ECHO = {
  "1": {
    "7": [
      {"type": "fulfillment", "target": "Isa 66:15", "note": "When the Lord Jesus is revealed from heaven with his mighty angels in flaming fire — the Day-of-the-Lord theophany of Isa 66:15 (the LORD will come in fire and his chariots like the whirlwind) is applied to the parousia of Jesus; the YHWH-theophany becomes the Christ-parousia"},
      {"type": "allusion", "target": "Dan 7:10", "note": "A thousand thousands served him and ten thousand times ten thousand stood before him — the Danielic throne-room with innumerable angels; Paul's 'mighty angels' at the parousia echoes the angelic army of Daniel's vision"}
    ]
  },
  "2": {
    "4": [
      {"type": "allusion", "target": "Dan 11:36", "note": "Who opposes and exalts himself against every so-called god — Daniel's description of the willful king who exalts himself above every god; the man of lawlessness of 2 Thess 2 is Paul's application of the Danielic anti-God figure to the eschatological opponent"},
      {"type": "allusion", "target": "Ezek 28:2", "note": "I am a god, I sit in the seat of the gods — the prince of Tyre's self-deification in Ezekiel; the man of lawlessness who seats himself in God's temple echoes this prophetic type of human self-exaltation"}
    ],
    "8": [
      {"type": "fulfillment", "target": "Isa 11:4", "note": "The Lord Jesus will kill him with the breath of his mouth — YHWH's messianic king who smites the earth with the rod of his mouth and with the breath of his lips kills the wicked; Paul applies this messianic judgment-action directly to the parousia of Jesus destroying the lawless one"}
    ]
  }
}

TWOTHESS_ORIGINAL = {
  "2": {
    "3": "<p><strong>he apostasia prōton kai apokaluphthē ho anthropos tes anomias ho huios tes apōleias</strong> (<em>hē apostasia prōton kai apokaluphthē ho anthrōpos tēs anomias ho huios tēs apōleias</em>): 'the rebellion (<em>apostasia</em>) comes first, and the man of lawlessness, the son of destruction, is revealed.' <em>Apostasia</em> — in LXX political rebellion and religious apostasy are both covered by this word; whether Paul means a final cosmic falling-away from faith or a political rebellion is debated. <em>Ho huios tes apōleias</em> (son of destruction) is the same phrase used of Judas in John 17:12 — linking the ultimate opponent to the prototypical betrayer. <em>Apokaluphthē</em> (is revealed): the passive suggests God controls even the timing of the opponent's disclosure.</p>",

    "6": "<p><strong>to katechon / ho katechon</strong>: 'what is restraining / he who restrains' — the most debated phrase in 2 Thessalonians. The neuter (<em>to katechon</em>, v. 6) and masculine (<em>ho katechon</em>, v. 7) alternate, suggesting either a power/principle and a personal restrainer, or a rhetorical variation for the same referent. Major interpretive proposals: (1) the Roman empire/emperor (the power that prevents chaos — Tertullian, Chrysostom); (2) Paul's own missionary preaching that must be completed first; (3) the Holy Spirit who restrains evil until the end; (4) a divine decree or angel. The deliberate vagueness may be security-conscious rhetoric — naming the restrainer directly in a letter could be politically dangerous.</p>"
  }
}

TWOTHESS_CONTEXT = {
  "2": {
    "1": "<p>2 Thessalonians was apparently written shortly after 1 Thessalonians (ca. 50-51 CE) to address a new crisis: someone had claimed (perhaps with a forged letter from Paul, v. 2) that 'the day of the Lord has come'. This eschatological collapse-of-tense caused some Thessalonians to abandon work (<em>ataktōs peripatountas</em>, 3:11: living in idleness) in anticipation of the immediate end. Paul's response establishes preconditions for the Day: the apostasia and the revelation of the lawless one must come first. Whether 2 Thessalonians is authentically Pauline or deutero-Pauline is contested; stylistic differences from 1 Thessalonians and the elaborate eschatological schema have led some scholars to posit a later pseudonymous author, though early attestation and close similarity to 1 Thess language support Pauline authorship.</p>",

    "9": "<p>The 'signs and wonders and false miracles' (<em>sēmeia kai terata kai dynameis</em>) of the lawless one mirror the authentic apostolic credentials Paul cites for his own ministry (2 Cor 12:12: signs, wonders, and mighty works). The mirror-imagery is deliberate: the eschatological opponent operates as a satanic parody of apostolic ministry, complete with sign-works that deceive those who refuse to love the truth (v. 10). Second Temple Jewish literature (4 Ezra; the Testament of Moses; and later rabbinic material) preserves traditions of a final demonic figure who deceives Israel before divine deliverance — Paul's 'man of lawlessness' belongs to this tradition.</p>"
  }
}

TWOTHESS_CHRIST = {
  "1": {
    "7": "<p>A direct revelation: 'When the Lord Jesus is revealed from heaven with his mighty angels in flaming fire, inflicting vengeance on those who do not know God and on those who do not obey the gospel of our Lord Jesus.' The parousia of Jesus is described using the vocabulary of YHWH's theophanic judgment in Isa 66 and Daniel — the same fire, angels, and judgment associated with YHWH's Day of the Lord are now associated with Jesus's return. The Christological identification is complete: the Day of the Lord is the Day of the Lord Jesus; the theophanic judge is Christ.</p>"
  },
  "2": {
    "8": "<p>A direct revelation: 'The Lord Jesus will kill him with the breath of his mouth and bring him to nothing by the appearance of his coming.' Paul applies the messianic victory-text of Isa 11:4 (the rod of his mouth, the breath of his lips) to Jesus at his parousia. The eschatological adversary — however powerful his signs and wonders and however extensive his deception — is annihilated by the mere breath-word of Jesus. The Christological power asymmetry is absolute: the lawless one's satanic-energy miracles against the breath of Christ's mouth. The parousia is therefore not a cosmic battle in which the outcome is uncertain but a disclosure that definitively ends the charade of the opponent's authority.</p>",

    "14": "<p>A direct revelation: 'To this end God called you through our gospel, so that you may obtain the glory of our Lord Jesus Christ.' The goal of calling is sharing Christ's glory (<em>peripoiēsin doxēs tou kyriou hemon Iesou Christou</em>). This echoes the Christological trajectory of Romans 8:30 (glorified) and Philippians 3:21 (conformed to Christ's glorious body). Christ's glory is not merely admired from outside but participated in — the eschatological destiny of believers is Christomorphic glory. The calling-gospel-glory chain frames Christian identity as Christologically determined from initiation to consummation.</p>"
  }
}

def main():
    # 1 Thessalonians — comprehensive original-language commentary first
    c = load_comm('mkt-original', '1thessalonians')
    merge_comm(c, ONETHESS_ORIGINAL_FULL)
    merge_comm(c, ONETHESS_ORIGINAL)   # also merge the sparse pre-existing entries
    save_comm('mkt-original', '1thessalonians', c)
    print(f'1Thess original: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-context', '1thessalonians')
    merge_comm(c, ONETHESS_CONTEXT)
    save_comm('mkt-context', '1thessalonians', c)
    print(f'1Thess context: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-christ', '1thessalonians')
    merge_comm(c, ONETHESS_CHRIST)
    save_comm('mkt-christ', '1thessalonians', c)
    print(f'1Thess christ: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    # 2 Thessalonians (all four layers)
    e = load_echo('2thessalonians')
    merge_echo(e, TWOTHESS_ECHO)
    save_echo('2thessalonians', e)

    c = load_comm('mkt-original', '2thessalonians')
    merge_comm(c, TWOTHESS_ORIGINAL)
    save_comm('mkt-original', '2thessalonians', c)
    print(f'2Thess original: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-context', '2thessalonians')
    merge_comm(c, TWOTHESS_CONTEXT)
    save_comm('mkt-context', '2thessalonians', c)
    print(f'2Thess context: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-christ', '2thessalonians')
    merge_comm(c, TWOTHESS_CHRIST)
    save_comm('mkt-christ', '2thessalonians', c)
    print(f'2Thess christ: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

if __name__ == '__main__':
    main()
