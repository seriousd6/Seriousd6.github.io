"""
mkt-context layer — Acts all 28 chapters
Output: data/commentary/mkt-context/acts.json

Acts situates the early church in a world of Roman provincial administration,
Second Temple Jewish sectarianism, Hellenistic religion, and Diaspora synagogue
networks. Luke-Acts is the most historically verifiable NT document — Ramsay's
19th-century archaeological work vindicated Luke on dozens of specific details.
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

CONTEXT = {
  "1": {
    "4": "<p>The forty-day post-resurrection period (1:3) before Pentecost matches the Omer count (Lev 23:15-16) — fifty days from Passover to Shavuot (Weeks/Pentecost). Whether the chronological match was providential design or Luke's deliberate framing, the Spirit's arrival at the feast when Jews celebrated the giving of Torah at Sinai is theologically loaded: the new law is the Spirit written on hearts (Jer 31:33; Ezek 36:26-27).</p>",

    "12": "<p>The Mount of Olives was associated in prophetic tradition with eschatological events (Zech 14:4); its proximity to the temple (a Sabbath's journey ≈ 2,000 cubits / 880 meters, m. 'Eruvin 4:3) meant the disciples returned to the symbolic center of Jewish religious life. The upper room (<em>hyperōon</em>) was likely a substantial space — Jerusalem houses of the affluent had rooftop rooms used for private prayer and assembly. The eleven plus women plus Mary and brothers (total ~120, v. 15) represents a deliberately quorate gathering: ten men was the minimum for a synagogue <em>minyan</em>.</p>"
  },
  "2": {
    "1": "<p>Shavuot (Pentecost/Weeks) was one of three pilgrimage festivals requiring attendance at Jerusalem (Deut 16:16); the diaspora Jews catalogued in vv. 9–11 represent the full geographic range of Jewish settlement — from Parthia in the east to Rome in the west. Philo (De Specialibus Legibus 2.176-188) describes the festival crowds and the joy of first-fruits offering. Luke's list of nations in 2:9–11 closely mirrors ancient ethnographic schemes (cf. the Table of Nations, Gen 10) and may function as an implicit counter-Babel: the scattered nations are now hearing in their own tongues.</p>",

    "14": "<p>Peter's sermon in 2:14–36 is the most carefully constructed apologetic speech in Acts. Its structure: appeal to LXX citation (Joel 2:28-32), witness testimony (v. 32), Ps 16:8-11 proof (vv. 25-28), Ps 110:1 proof (vv. 34-35), conclusion (v. 36). This is the pesher method of biblical interpretation developed at Qumran (1QpHab): a text → 'this is that' (<em>touto estin to eiremenon</em>) → identifying the historical referent. Peter's pesher identifies the referent as Jesus of Nazareth, crucified and risen.</p>",

    "46": "<p>Daily temple attendance (<em>proseuchomenoi kata ten horan tes thysias</em>, 3:1 — at the ninth hour prayer, 3:00 pm) alongside house-church eucharist reflects the earliest community's dual allegiance: they remained observant Jews attending temple liturgy while also practicing distinctively Christian fellowship. This dual practice continued until the temple's destruction in 70 CE made it impossible. The breaking of bread <em>kat' oikon</em> (house to house) documents the earliest Christian meeting architecture: private homes, not dedicated buildings.</p>"
  },
  "3": {
    "1": "<p>The Beautiful Gate (<em>horaia pyle</em>) is not directly identified in first-century sources. The Mishnah (m. Middot 2:3) describes the Nicanor Gate between the Court of Women and the Court of Israel as exceptional in bronze and size; many scholars identify this with Luke's 'Beautiful Gate'. It was the main thoroughfare for Jewish worshippers proceeding inward — a highly visible location for a beggar dependent on the alms-giving piety of pilgrims. The ninth-hour prayer (3:00 pm) was the afternoon Tamid sacrifice, drawing maximum temple traffic.</p>",

    "17": "<p>Peter's 'you acted in ignorance' (<em>kata agnoian epraxate</em>) corresponds to the Torah's distinction between inadvertent (<em>bishegagah</em>) and high-handed (<em>beyad ramah</em>) sins (Num 15:27-31; Lev 5:15-19). Inadvertent sins had sacrificial remedy; deliberate high-handed sins did not. Peter's appeal gives his audience a path: the crucifixion, done in ignorance, can be covered by the same mercy that covers inadvertent sin — if they now respond to the revelation of who Jesus was.</p>"
  },
  "4": {
    "36": "<p>Barnabas ('son of encouragement' — Luke's translation of Aramaic <em>Bar-Nabas</em>; though some argue the Aramaic root is <em>naba</em>/prophet, making him 'son of a prophet') is introduced as a Levite from Cyprus. Levites theoretically could not own land (Num 18:20), but Diaspora conditions had long made this impractical; his property sale represents voluntary conformity to the community ideal rather than strict Torah compliance. He becomes the key bridge figure between Paul and the Jerusalem apostles (9:27; 11:22-26) and co-missionary on the first journey.</p>"
  },
  "5": {
    "34": "<p>Gamaliel I (the Elder) was one of the most respected Pharisaic teachers of the early first century (Paul studied under him, 22:3). The Mishnah (m. Avot 1:16; m. Sanhedrin 2:6) preserves traditions of his teachings. His advice — wait and see whether this movement is from God — represents the classical Pharisaic strategy of avoiding premature judgment. His two historical examples: Theudas and Judas the Galilean. Josephus (Ant. 20.97-98) places Theudas under Fadus (44-46 CE), creating a chronological problem since this Gamaliel speech is set ca. 30-32 CE. Either Luke has a different Theudas, or Josephus's Theudas is the same person misdated, or there was an earlier failed Theudas movement.</p>"
  },
  "7": {
    "1": "<p>Stephen's speech (7:1-53) is the longest speech in Acts and the most complex LXX survey in the NT. Its structure: Abraham narrative (vv. 2-8), Joseph narrative (vv. 9-16), Moses narrative (vv. 17-43), tabernacle/temple argument (vv. 44-50), accusation (vv. 51-53). The cumulative argument: Israel has consistently rejected the prophets, preferred idols to YHWH, and confused God's dwelling with a human building. The heroes (Abraham, Joseph, Moses) are all figures of rejection and vindication — typological of Jesus. Stephen's speech is widely recognized as independent tradition (its Christology is archaic: 'the Righteous One', 7:52; 'the Son of Man', 7:56).</p>",

    "58": "<p>Saul's first appearance in Acts is as a passive witness: <em>hoi de martyres apethento ta himatia autōn para tous podas neaniou kaloumenou Saulou</em> ('the witnesses laid their garments at the feet of a young man called Saul'). He is <em>neanias</em> — probably 25-40 years old. His 'consent' (<em>syneudokōn</em>, 8:1) marks him as an approving bystander who will become the active persecutor of 8:3. The contrast between Stephen's death (full of Spirit, seeing the Son of Man, forgiving his killers) and Saul's role in it frames the conversion of ch. 9 as the more dramatic precisely because of this starting point.</p>"
  },
  "8": {
    "26": "<p>The Ethiopian eunuch: Ethiopia (<em>Aithiopia</em>) in Greek-Roman geography referred to the Nubian kingdom south of Egypt (modern Sudan); the Candace was the queen-mother title of the ruling dynasty (Meroitic <em>ktke</em>; several queens held this title historically — Strabo 17.1.54; Pliny NH 6.186). As court treasurer (<em>dynastes</em>) he held significant administrative power. As a eunuch he was excluded from full Jewish assembly participation (Deut 23:1) but Isa 56:3-8 had promised eunuchs a 'monument and a name better than sons and daughters'. Philip's baptism of him is the first recorded fulfillment of that Isaianic promise: the Spirit-led inclusion of the excluded.</p>"
  },
  "9": {
    "1": "<p>Paul's conversion on the Damascus road is recounted three times in Acts (9:1-19; 22:6-16; 26:12-18), each with slightly different emphases depending on the audience. The three accounts together give: a blinding light (9:3; 22:6; 26:13 — brighter than the noon sun), a voice in Aramaic/Hebrew (26:14: <em>te Hebraidi dialektō</em> — 'in the Hebrew language'), the question 'Saul, Saul why do you persecute me?', and the self-identification 'I am Jesus'. The Damascus road experience is Paul's foundational 'seeing the Lord' (1 Cor 9:1; 15:8) that qualifies him as an apostle — he received a resurrection appearance as authoritative as those given to the Twelve.</p>"
  },
  "10": {
    "1": "<p>Cornelius is a Roman centurion of the Cohors Italica — an auxiliary unit stationed in Caesarea Maritima (Herod's coastal capital of Judea). Inscriptions attest an <em>Italica</em> cohort in Syria-Palestine in the first century (CIL III 14137). He is described as <em>eusebēs kai phoboumenos ton theon</em> ('devout and God-fearing') — the latter a technical designation in Acts (10:2, 22, 35; 13:16, 26) for Gentile sympathizers with Judaism who had not undergone full conversion (circumcision). God-fearers attended synagogues, gave alms to Jewish causes, observed some practices, but remained Gentiles. Cornelius's acceptance of the Spirit without prior circumcision becomes the precedent cited at the Jerusalem Council (15:7-11).</p>",

    "28": "<p>Jewish food laws and purity regulations created social barriers preventing shared table fellowship between observant Jews and Gentiles. The Mishnah (m. Avodah Zarah) regulated business and social contact with idolaters; meals in Gentile homes risked defilement through non-kosher food and vessels. Peter's vision of the sheet with unclean animals (10:11-16) — 'what God has made clean, do not call common' (<em>ha ho theos ekatharisen sy me koinou</em>) — addresses both food laws and their social function. Peter's insight (v. 28) that he should not call <em>any person</em> common or unclean shows he understood the vision's primary referent was not food but people.</p>"
  },
  "13": {
    "1": "<p>The Antioch church leadership list (13:1) is strikingly diverse: Barnabas (Levite from Cyprus), Simeon called Niger (African; Niger = black in Latin, likely from North Africa), Lucius of Cyrene (another North African), Manaen (a court associate of Herod Antipas — remarkable social connection), and Saul. This is intentional Lukan sociology: the first sending church includes every stratum — Diaspora Jew, African, royal court, persecutor-turned-apostle. <em>Prophets and teachers</em> are distinguished from the Twelve (1:2) — these are second-generation leaders operating under the Spirit's direction through liturgical discernment (<em>leitourgountōn</em>, worshipping, v. 2).</p>"
  },
  "15": {
    "1": "<p>The Jerusalem Council (ca. 48-49 CE) addressed the most critical ecclesiological question of the first generation: must Gentiles become Jews (via circumcision and Torah observance) to be Christians? The Pharisaic position (v. 5) was consistent with the synagogue practice for <em>gerim</em> (resident aliens) who underwent full conversion. Peter's response (vv. 7-11) deployed the Cornelius precedent (8-10 years earlier) as the Spirit's own verdict. James's ruling (vv. 13-21) cited Amos 9:11-12 in LXX form (which differs significantly from the MT, reading 'the rest of humanity' instead of 'the remnant of Edom') as the scriptural warrant for Gentile inclusion without circumcision.</p>",

    "20": "<p>The Jerusalem Council's four prohibitions (<em>apechesthai eidolotytōn kai haimatos kai pniktōn kai porneias</em>: abstain from food sacrificed to idols, from blood, from strangled animals, and from sexual immorality) are best understood as the Noahide commands (Gen 9:1-17) as formalized in later rabbinic tradition (b. Sanhedrin 56a: seven Noahide laws include prohibitions on idolatry, sexual immorality, and blood). The decree does not require full Torah observance but marks the minimum for table fellowship between Jewish and Gentile believers.</p>"
  },
  "17": {
    "16": "<p>The Areopagus speech (17:22-31) is Luke's showpiece of Pauline apologetics to a Hellenistic philosophical audience. Athens in the mid-first century CE, though politically reduced to a Roman provincial town, remained the symbolic center of Greek philosophical tradition — Plato's Academy, Aristotle's Lyceum, Epicurean and Stoic schools. Paul's audience included both Epicureans (no divine providence or afterlife; atoms and void) and Stoics (divine Logos permeating all things; cosmic rationality). The altar 'To an Unknown God' (<em>Agnōstō Theō</em>: attested by Diogenes Laertius 1.110 and Pausanias 1.1.4 as a practice in Athens) provides Paul his exordium without alienating his audience.</p>"
  },
  "18": {
    "12": "<p>Gallio (Lucius Junius Annaeus Gallio Novatus), proconsul of Achaia, is one of the most important chronological anchors for NT chronology. A Delphi inscription (SIG3 801) records Gallio as proconsul of Achaia during the 26th acclamation of Claudius, datable to 51-52 CE. Paul appeared before Gallio ca. 51-52 CE; working backward from this gives Paul's Corinthian stay (18 months, v. 11) as ca. 50-52 CE, and his Damascus road conversion ca. 33-34 CE. Gallio's refusal to adjudicate Jewish theological disputes ('if it were a matter of wrongdoing or vicious crime I would have reason to accept your complaint', v. 14) established a legal precedent: Christianity is an internal Jewish dispute, not a new illegal religion.</p>"
  },
  "19": {
    "23": "<p>Ephesus was the administrative capital of the Roman province of Asia (western Turkey) and home to the Artemis temple (one of the Seven Wonders of the ancient world; rebuilt by Croesus; the Ephesian Artemis was a fertility goddess distinct from the Greek Artemis). The silversmith Demetrius's complaint exposes the economic dimension of religious conflict: the <em>naopouloi</em> (temple-business workers) who made <em>naoi</em> (small silver shrines of Artemis) for pilgrims and votaries faced economic ruin if Ephesians converted. The Ephesian assembly (<em>ekklesia</em>) is an authentic Roman civic body — the use of the same word <em>ekklesia</em> for the Christian community was deliberately countercultural.</p>"
  },
  "21": {
    "37": "<p>The Antonia Fortress (named for Mark Antony by Herod the Great) stood at the northwest corner of the temple mount, connected to the temple porticoes by staircases that appear here (21:35; cf. Josephus War 5.238-247). The Roman tribune's surprise that Paul speaks Greek (rather than the Aramaic he expected from a Jerusalem arrest) opens the Lysias-Paul relationship. The tribune's misidentification of Paul as 'the Egyptian' (v. 38) who led 4,000 sicarii into the desert is confirmed by Josephus (War 2.261-263; Ant. 20.169-172): the Egyptian pseudo-prophet gathered 30,000 followers (Jewish War's number) or 4,000 (Antiquities — matching Acts) to the Mount of Olives, was dispersed by Felix, and disappeared.</p>"
  },
  "27": {
    "9": "<p>The 'fast' (<em>nesteia</em>) that had already passed indicates the Day of Atonement (Yom Kippur, Lev 16:29-31), which falls on the 10th of Tishri (September/October). Navigation in the ancient Mediterranean was dangerous after mid-September and effectively halted from November through March (Mare clausum). Vegetius (Epitoma Rei Militaris 4.39) gives September 14 to November 11 as the 'unsafe' period; Acts 27's shipwreck narrative is the most detailed ancient account of Mediterranean sailing and storm-survival, displaying accurate knowledge of winds, shipping routes, and seamanship (the Alexandrian grain ship carrying 276 people, v. 37-38, is consistent with Lucian's descriptions of grain fleet vessels).</p>"
  },
  "28": {
    "1": "<p>Malta (<em>Melitē</em>): a Phoenician colony 90 km south of Sicily, part of the Roman province of Sicily, whose population Luke calls <em>barbaroi</em> — not 'barbarians' in the negative sense but simply 'non-Greek-speakers' (a Semitic Punic dialect was spoken there). Luke's notation that they showed <em>unusual kindness</em> (<em>philanthropian ou tēn tychousian</em>) may implicitly contrast Mediterranean hospitality norms with the Roman world Paul has been navigating. The three-month winter stay (v. 11) before the Alexandrian grain ship (with the Dioscuri figurehead — Castor and Pollux, patrons of sailors) departs places the shipwreck in late October/early November and the Malta stay through January/February.</p>",

    "30": "<p>Acts closes with Paul in Rome under house arrest (<em>en idiō misthōmati</em>, 'in his own rented lodging') for two years — a deliberate literary conclusion that declares the gospel has reached the center of the empire 'unhindered' (<em>akōlytōs</em>). Luke does not narrate Paul's death (presumably because it had not yet occurred when he finished writing, or because the death was not his theme). The final verse's <em>akōlytōs</em> (unhindered) is the note of triumph: Roman law, Jewish opposition, storm, and shipwreck did not stop the word. The ending is not incomplete — it is programmatic: the mission continues beyond the page.</p>"
  }
}

def main():
    existing = load_comm('mkt-context', 'acts')
    merge_comm(existing, CONTEXT)
    save_comm('mkt-context', 'acts', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Acts mkt-context: {len(existing)} chapters, {total} verses.')

if __name__ == '__main__':
    main()
