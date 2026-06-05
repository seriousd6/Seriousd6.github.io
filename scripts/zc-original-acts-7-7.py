"""
mkt-original layer — Acts all 28 chapters
Output: data/commentary/mkt-original/acts.json

Acts is Luke's second volume; Greek is polished but deliberately registers
vernacular voices in speeches. Key philological zones: Pentecost terminology,
martys/martyria witness-vocabulary, the Spirit-language cluster,
and 20:28's unique "blood of his own" Christology.
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

ORIGINAL = {
  "1": {
    "8": "<p><strong>dynamis</strong> (<em>dynamis</em>) is not courage or willpower but the divine capacity to perform what exceeds human ability — the same word used for the Spirit's creative power in the Incarnation (Luke 1:35). The promise is not merely empowerment but an endowment that makes the disciples constitutively capable witnesses. <strong>martyres</strong> (<em>martyres</em>) will become the defining identity-word for believers in Acts (1:22; 2:32; 3:15; 5:32; 10:39; 13:31; 22:15; 26:16): those who testify to what they have personally seen. The geographic progression — Jerusalem → Judea → Samaria → ends of the earth — is the structural outline of all twenty-eight chapters.</p>",

    "11": "<p><strong>ho Galilaioi</strong> (<em>hoi Galilaioi</em>): the angelic address specifies their provincial origin; in first-century Judaism, Galileans were regarded with mild condescension by Jerusalem's educated elite. The disciples who will shake the empire are identified as uneducated provincials — Acts' characteristic irony. <strong>analepsis</strong> (<em>analēpsis</em>) — the same word Luke used in 9:51 for the 'assumption' toward which Jesus set his face — frames the ascension as completion of the entire travel-narrative begun in Luke's central section.</p>"
  },
  "2": {
    "1": "<p><strong>homothymadon</strong> (<em>homothymadon</em>, 'with one accord/purpose') appears eleven times in Acts and only once elsewhere in the NT (Rom 15:6). It is not merely spatial togetherness but a deliberate unity of will and disposition — the kind of communal harmony that Ps 133:1 calls 'good and pleasant'. Luke signals that Pentecost descends on a community already in relational order.</p>",

    "4": "<p><strong>heterais glossais</strong> (<em>heterais glōssais</em>, 'other/different tongues') identifies actual foreign languages — confirmed by the catalogue in vv. 9–11 of identifiable nations who each hear 'in our own tongue' (<em>tē hēmeterā dialektō</em>). This is distinct from the ecstatic glossolalia of 1 Cor 14. The Pentecost miracle partially reverses Babel (Gen 11:1–9): where Babel dispersed by language confusion, the Spirit unifies across language boundaries. <strong>apophthengesthai</strong> (<em>apophtheggesthai</em>, 'to utter', 2:4, 14) is a semi-technical term for inspired prophetic speech; used of the Delphic oracle and in LXX for prophetic utterance (Mic 5:12; Ezek 13:9).</p>",

    "38": "<p><strong>metanoeite</strong> (<em>metanoeite</em>) is the same imperative John and Jesus used (Mark 1:15; Luke 13:3,5); here it opens the community's first public invitation. <strong>baptistheto ... eis aphesin hamartion</strong>: the preposition <em>eis</em> marks direction or purpose — baptism toward/for forgiveness of sins, not a meritorious cause. <strong>dorea</strong> (<em>dōrea</em>, 'gift') marks the Spirit as freely bestowed, not earned; the same word for God's indescribable gift in 2 Cor 9:15. The sequence metanoia → baptism → forgiveness → Spirit-gift became the pattern by which Acts measures conversion.</p>",

    "42": "<p><strong>te didache ton apostolon ... te koinonia ... te klasei tou artou ... tais proseuchais</strong>: Luke lists four activities of the Jerusalem community in asyndeton (no conjunctions), giving them equal structural weight. <strong>koinonia</strong> (<em>koinōnia</em>) is not merely 'fellowship' but participatory sharing — of goods (v. 44–45), of the Lord's Supper, of the Spirit (2 Cor 13:14). <strong>klasis tou artou</strong> is a Semitic phrase for breaking bread at meals; in Luke 24:35 it was the Emmaus recognition moment, suggesting eucharistic weight here.</p>"
  },
  "3": {
    "15": "<p><strong>archegos tes zoes</strong> (<em>archēgon tēs zōēs</em>): <em>archēgos</em> means pioneer, founder, or champion — one who blazes a trail others follow. In Heb 2:10 and 12:2, Christ is archēgos of salvation and faith. Peter's phrase is therefore not merely 'author of life' (as if life were a text Jesus wrote) but 'pioneer of life' — the one who broke through death to open the way. The audience had killed the pioneer of life; God reversed the verdict by resurrection. The irony is Luke's sharpest Christological paradox in Acts.</p>",

    "22": "<p><strong>propheten ... hos eme</strong> (<em>prophētēn ... hōs eme</em>): Peter quotes Deut 18:15 and links it to Jesus. The 'prophet like Moses' in Deuteronomic expectation was to bring a new word from YHWH with authority like the Sinai revelation. The rabbinic tradition expected this prophet at the eschaton (1QS 9:11 — the Qumran community awaited the prophet along with the Messiah). Peter claims the eschatological prophet has arrived: the new Moses not merely like him but surpassing him.</p>"
  },
  "4": {
    "12": "<p><strong>ouk estin en allo oudeni he soteria</strong> (<em>ouk estin en allō oudeni hē sōtēria</em>): 'in no other is there salvation' — Peter's exclusive soteriological claim before the Sanhedrin. <strong>onoma</strong> (<em>onoma</em>) carries Semitic weight: the name is the person, their character and authority concentrated. <strong>hypo ton ouranon</strong> ('under heaven'): the spatial comprehensiveness marks this as a universal claim, not a parochial Jewish sectarian position. The statement is the more remarkable for being made to the very council that approved Jesus's execution.</p>",

    "32": "<p><strong>kardia kai psyche mia</strong> (<em>kardia kai psychē mia</em>, 'one heart and soul'): a Hellenistic friendship ideal (Aristotle's 'one soul in two bodies') now applied to the entire community. Luke's vocabulary of voluntary property-sharing (<em>koina</em>, all things in common; 2:44) differs structurally from the Qumran model where members transferred property to the community permanently. Jerusalem believers retained ownership (<em>idios</em>) and voluntarily brought proceeds as needs arose (5:4 confirms private property was not abolished).</p>"
  },
  "5": {
    "29": "<p><strong>peitharchein dei theo mallon e anthropois</strong> (<em>peitharchein dei theō mallon ē anthrōpois</em>): 'we must obey God rather than human beings'. <em>dei</em> is divine necessity, not preference — the same <em>dei</em> that drove Jesus's entire ministry (Luke 2:49; 4:43; 9:22). <em>peitharchein</em> (obey authority) is the compound of <em>peitho</em> (persuade/trust) + <em>archē</em> (ruling authority), carrying the nuance that legitimate authority deserves compliance — but God's authority supersedes all human authority structures.</p>"
  },
  "7": {
    "55": "<p><strong>hestota ek dexion tou theou</strong> (<em>hestōta ek dexiōn tou theou</em>, 'standing at the right hand of God'): every NT text on Christ's post-ascension position describes him <em>seated</em> (Ps 110:1; Eph 1:20; Col 3:1; Heb 1:3). Here alone he is <em>standing</em>. The contrast is intentional and has generated two main interpretations: (1) Christ rises to welcome Stephen the proto-martyr — a gesture of reception; (2) Christ stands as judge in the heavenly court to give favorable testimony on Stephen's behalf. Either reading shows the risen Christ responding actively to earthly events from his exalted position.</p>"
  },
  "8": {
    "35": "<p><strong>arxamenos apo tes graphes tautes euengelisato auto ton Iesoun</strong> (<em>arxamenos apo tēs graphēs tautēs euēngelisato autō ton Iēsoun</em>): 'beginning from this Scripture he proclaimed good news about Jesus'. Philip's method is the apostolic hermeneutic: Isa 53 → Jesus. <em>euangelizomai</em> here has its full weight as announcement of a decisive new development — the Servant's identity is now disclosed. The Ethiopian eunuch's question ('of himself or another?') echoes the pesher method of Qumran: Scripture requires an identified referent to unlock its meaning.</p>"
  },
  "10": {
    "34": "<p><strong>prosopolemptes</strong> (<em>prosōpolēmptēs</em>, 'one who shows partiality/face-receiver'): a NT coinage from the LXX idiom <em>lambanein prosopon</em> (lift the face = receive favorably), itself a calque of Hebrew <em>nasa' panim</em>. The word appears in Paul (Rom 2:11; Eph 6:9; Col 3:25) and Jas 2:1. Peter's declaration that God is not a <em>prosopolēmptēs</em> marks the theological breakthrough of the Cornelius episode: the ethnic boundary between Jew and Gentile is not the boundary of divine acceptance.</p>",

    "44": "<p><strong>epepesen to Pneuma to Hagion</strong> (<em>epepesen to Pneuma to Hagion</em>, 'the Holy Spirit fell upon'): the same verb as Acts 2 (2:3, <em>epesen</em>); Luke deliberately signals that Cornelius's household receives the identical Pentecost as the Jerusalem community. <em>epipiptō</em> (fall upon) is striking in its physicality — the Spirit is not merely invited or requested but descends sovereignly, surprising Peter mid-sermon. The circumcised believers are <em>exestēsan</em> (astonished) because the gift precedes any formal completion of conversion rites, vindicating God's impartial acceptance.</p>"
  },
  "13": {
    "39": "<p><strong>en touto pas ho pisteuon dikaioutai</strong> (<em>en toutō pas ho pisteuōn dikaioutai</em>): Acts' only occurrence of <em>dikaioō</em> (justify). Luke's vocabulary is normally <em>sōzō</em> (save) and <em>aphesis</em> (forgiveness); the appearance of Pauline justification language in Paul's first major sermon confirms Luke knew Paul's theological categories and represents them accurately. <strong>apo pantōn hōn ouk ēdunēthēte en nomō Mōuseōs dikaiōthenai</strong>: 'from everything from which you could not be justified by the law of Moses' — the law's incompleteness is the foil that makes Christ's justification complete and universally available.</p>"
  },
  "15": {
    "11": "<p><strong>dia tes charitos tou kyriou Iesou pisteuomen sothenai</strong> (<em>dia tēs charitos tou kyriou Iēsou pisteuomen sōthēnai</em>): Peter's climactic speech at the Jerusalem council: 'we believe that through the grace of the Lord Jesus we are saved, just as they are'. The <em>kathos kakeinoi</em> ('just as they also') is the decisive reversal — not Gentiles saved like Jews, but Jews saved like Gentiles: by grace through faith, not by Torah-observance. <em>Charis</em> (grace) as the mode, <em>pisteuomen</em> (we believe) as the means, <em>sōthēnai</em> (to be saved) as the end — Pauline soteriology in Petrine formulation.</p>"
  },
  "17": {
    "28": "<p><strong>en autō gar zōmen kai kinoumentha kai esmen</strong> (<em>en autō gar zōmen kai kinoumentha kai esmen</em>): Paul quotes the Cretan poet Epimenides (<em>in him we live and move and have our being</em>). <strong>tou gar kai genos esmen</strong>: from Aratus's <em>Phaenomena</em> (<em>for we are indeed his offspring</em>). Paul's Areopagus speech uses pagan poets as partial witnesses to what the gospel discloses fully: universal human dependence on and kinship with the God who made from one (<em>ex henos</em>) all nations. The strategy is not syncretism but apologetic appropriation — common ground that the specific proclamation of resurrection then exceeds.</p>"
  },
  "20": {
    "28": "<p><strong>ten ekklesian tou theou hen peripoiesato dia tou haimatos tou idiou</strong> (<em>tēn ekklēsian tou theou hēn peripoiesato dia tou haimatos tou idiou</em>): arguably the most theologically dense sentence in Acts. <em>Ekklesia tou theou</em> is Paul's normal Corinthian usage. <em>Peripoieomai</em> (acquire for oneself) echoes LXX Isa 43:21 and Exod 19:5 where YHWH acquires Israel as his special possession. Critically: <em>dia tou haimatos tou idiou</em> — 'through his own blood'. <em>Idios</em> (own/personal) can modify the understood subject (God, whose Son's blood is 'his own') or be read as 'the blood of the one who is his own [Son]'. Either reading makes this the most explicit Acts Christology: God-who-owns-the-blood, or blood that belongs to God himself. The elders of Ephesus are charged to shepherd what God purchased at this cost.</p>"
  },
  "26": {
    "18": "<p><strong>epistrephai apo skotous eis phos kai tes exousias tou Satana epi ton theon</strong> (<em>epistrepsai apo skotous eis phōs kai tēs exousias tou Satana epi ton theon</em>): Paul's mission-summary before Agrippa. <em>Epistrephō</em> (turn) is the LXX-standard verb for Israel's repentance/return (<em>shub</em>). The dual transfer — darkness to light, Satan's authority to God — frames conversion as a cosmic jurisdiction-change, not merely moral improvement. <em>Aphesis hamartion</em> (forgiveness of sins) and <em>klēron en tois hēgiasmenois</em> (inheritance among the sanctified) complete the fourfold result: light, God's side, forgiveness, inheritance. The inheritance-language echoes Deut 33:3-4 and the Wisdom literature of Second Temple Judaism.</p>"
  },
  "28": {
    "26": "<p><strong>poreutheti pros ton laon touton kai eipon</strong> (<em>poreuthēti pros ton laon touton kai eipon</em>): Paul's final quotation of Isa 6:9-10 to the Roman Jewish community. This is the third time Acts invokes the Isaianic hardening: Jesus used it in Luke 8:10; Acts 28 closes the narrative with it. The pattern is the 'to you and to them' logic: the gospel comes first to the Jew (Rom 1:16 priority) and when resisted turns outward. Luke does not say Israel is abandoned — Paul is still quoting Scripture to Jews — but the structural conclusion of Acts is the Gentile mission unhindered (<em>akōlytōs</em>, the book's last word).</p>"
  }
}

def main():
    existing = load_comm('mkt-original', 'acts')
    merge_comm(existing, ORIGINAL)
    save_comm('mkt-original', 'acts', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Acts mkt-original: {len(existing)} chapters, {total} verses.')

if __name__ == '__main__':
    main()
