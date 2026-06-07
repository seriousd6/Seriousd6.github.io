"""
Combined script: 1 Timothy, 2 Timothy, Titus, Philemon — all four layers.
Output: echoes + mkt-original + mkt-context + mkt-christ for all four letters.

The Pastoral Epistles (ca. 60-67 CE or deutero-Pauline ca. 80-100 CE)
address church order, ministry qualifications, sound doctrine, and personal
discipleship. Key theological contributions: the faithful sayings (pistoi logoi),
the appearing (epiphaneia) Christology, and the portrait of Paul as exemplary sufferer.
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
# 1 TIMOTHY
# ============================================================

ONETIM_ECHO = {
  "2": {
    "5": [
      {"type": "fulfillment", "target": "Job 9:33", "note": "There is one mediator between God and people, the man Christ Jesus — Job's lament 'there is no arbiter between us who might lay his hand on us both' is answered: the mediator Job could not find is Christ, who as the man Christ Jesus bridges the divine-human gap"},
      {"type": "fulfillment", "target": "Isa 53:12", "note": "Who gave himself as a ransom for all — the Servant who poured out his soul to death and bore the sin of many; the ransom-giving fulfills the Servant's self-offering on behalf of the many"}
    ]
  },
  "3": {
    "16": [
      {"type": "allusion", "target": "Ps 24:3-4", "note": "He was manifested in the flesh, vindicated by the Spirit — the hymn of 1 Tim 3:16 celebrates the incarnation-exaltation pattern; the Psalm's ascent to YHWH's holy hill resonates with the vindicated Christ ascending to the heavenly Zion"},
      {"type": "allusion", "target": "Isa 52:15", "note": "Proclaimed among the nations, believed on in the world — the Servant's proclamation that would cause kings to shut their mouths; the worldwide proclamation of the exalted Christ fulfills the Servant's mission reaching to all nations"}
    ]
  }
}

ONETIM_ORIGINAL = {
  "2": {
    "5": "<p><strong>heis gar theos heis kai mesites theou kai anthropon anthropos Christos Iesous</strong> (<em>heis gar theos, heis kai mesitēs theou kai anthrōpōn, anthrōpos Christos Iēsous</em>): 'For there is one God and one mediator between God and people, the man Christ Jesus.' The <em>mesites</em> (mediator) terminology was used in both Hellenistic contract law (a third party who guarantees a transaction) and in LXX usage for Moses's mediating role at Sinai (Gal 3:19-20). The Christological uniqueness: there is <em>one</em> mediator — contra the Greco-Roman polytheistic model of multiple divine intermediaries, and contra any Jewish or emerging Gnostic scheme of angelic mediators. The qualifier <em>anthrōpos</em> (man) before Christ Jesus emphasizes the genuine humanity that enables the mediation: the mediator must be able to touch both parties.</p>"
  },
  "3": {
    "16": "<p><strong>homologoumenos mega estin to tes eusebeias mysterion</strong>: 'Great indeed, as we confess, is the mystery of godliness.' What follows (vv. 16b-c) is almost certainly a pre-Pauline hymn or creedal fragment in six lines, possibly arranged in two strophes of three: (1) manifested in flesh / vindicated by Spirit / seen by angels; (2) proclaimed among nations / believed in the world / taken up in glory. The six verbs are all aorist passives — divine actions done to Christ. The structure mirrors Phil 2:6-11's humiliation-exaltation pattern: the first triad (incarnation, vindication, heavenly witness) parallels the descending and ascending of the Christ-hymn.</p>"
  },
  "6": {
    "15": "<p><strong>ho makarios kai monos dynamastes ho basileus ton basileonton kai kyrios ton kyrieonton</strong> (<em>ho makarios kai monos dynastēs, ho basileus tōn basileuontōn kai kyrios tōn kyrieuontōn</em>): 'the blessed and only Sovereign, the King of kings and Lord of lords.' The doxology of 6:15-16 applies to the epiphaneia of Jesus the titles that Hellenistic rulers and the Roman emperor claimed. <em>Dynastēs</em> (Sovereign/potentate) was used of divine-right rulers in the Hellenistic east. <em>King of kings and Lord of lords</em> echoes Deut 10:17 (YHWH as God of gods and Lord of lords) and Daniel 2:37, 47 (the God of heaven as King over kings). The doxology places the Roman emperor's pretensions under the sovereignty of Christ.</p>"
  }
}

ONETIM_CONTEXT = {
  "1": {
    "3": "<p>1 Timothy is addressed to Timothy in Ephesus — Paul's extended base of ministry (Acts 19, ca. 52-55 CE; and likely again ca. 60-65 CE if the Pastoral Epistles reflect a release from Roman imprisonment). Ephesus was the largest city in the province of Asia and the site of the Artemis temple; it had a large Jewish community, numerous mystery cult associations, and by the late first century a substantial Christian community (see Revelation 2:1-7). The false teachers Timothy must address are described as teaching 'different doctrine' (<em>heterodidaskale</em>), focusing on 'myths and endless genealogies' (1:4) and 'what they call knowledge' (<em>pseudonymos gnōsis</em>, 6:20), possibly an early form of Jewish-Gnostic speculation.</p>"
  },
  "5": {
    "17": "<p>The 'double honor' for elders who rule well (v. 17) — especially those who labor in preaching and teaching — reflects the early church's emerging distinction between lay elders and teaching-preaching elders. The citation of Deut 25:4 (do not muzzle an ox when it treads grain) and the dominical saying 'the laborer deserves his wages' (Luke 10:7) as dual warrant for paying ministers indicates that by the Pastoral period, apostolic-era oral tradition (Jesus's teaching) was already cited alongside Torah as authoritative Scripture.</p>"
  }
}

ONETIM_CHRIST = {
  "1": {
    "15": "<p>A direct revelation: 'The saying is trustworthy and deserving of full acceptance, that Christ Jesus came into the world to save sinners, of whom I am the foremost.' The first of the Pastoral Epistles' five 'faithful sayings' (<em>pistos ho logos</em>) is a Christological mission-statement: the incarnation's purpose is soteriological — Christ came into the world (implying pre-existence, like John 1:14) specifically to save sinners. Paul's self-designation as 'the foremost of sinners' makes the statement an autobiographical proof: if Christ saved me (the persecutor of the church), his saving purpose is as wide as the worst sinner.</p>"
  },
  "2": {
    "5": "<p>A direct revelation: 'There is one mediator between God and people, the man Christ Jesus, who gave himself as a ransom for all.' The two Christological claims together: (1) Christ is the unique, sole mediator — no competing spiritual hierarchy is needed or valid; (2) his mediation was accomplished through self-giving as a ransom (<em>antilytron</em>, substitutionary ransom-payment). <em>Antilytron</em> (found only here in NT) intensifies <em>lytron</em> (ransom, Mark 10:45) with the <em>anti</em> prefix indicating substitution: a ransom given in place of others. The universality ('for all', <em>hyper pantōn</em>) combined with the singularity ('one mediator') is the Christological center of 1 Timothy's soteriology.</p>"
  },
  "3": {
    "16": "<p>A direct revelation: 'He was manifested in the flesh, vindicated by the Spirit, seen by angels, proclaimed among the nations, believed on in the world, taken up in glory.' The Christological hymn traces the entire arc of Christ's work in six compressed phrases: incarnation → resurrection-vindication → heavenly acknowledgment → worldwide proclamation → faith-response → ascension. The hymn is the doctrinal center of the household-of-God section (3:14-16): sound church order and ministry is grounded in the Christological mystery that the church has received and proclaims.</p>"
  },
  "6": {
    "1": "<p>The theme of God's name: enslaved Christians honoring their masters so 'God's name and our teaching may not be slandered' — the church's social behavior is testimony. The pattern runs from Israel's calling to embody YHWH's character among the nations (Ezek 36:22-23) through to NT missional ethics: the visible life of the community is an argument for the reality of the Lord they proclaim. The church's credibility as witness to Christ's lordship rests partly on whether its members live the social ethics the gospel demands.</p>",
    "2": "<p>The theme of brotherhood overcoming social hierarchy: Christian masters are to be served 'even better' precisely because they are believers — the common life in Christ creates an obligation of excellence that honors the shared Lord. This represents the same logic as Paul's more radical statement in Philemon: the gospel generates a brotherhood (<em>adelphos</em>) that puts social categories under pressure. The Christological transformation is at work even within unchanged social structures, redirecting their energy toward love.</p>",
    "3": "<p>A direct revelation: the standard for sound teaching is 'the sound instruction of our Lord Jesus Christ.' Christ is named as the authoritative source of the teaching-tradition Timothy must guard. Any teaching that diverges from his instruction is by definition heterodox. The Christological criterion of orthodoxy: the content of Christ's own teaching — transmitted through the apostolic tradition — is the measuring rule by which all doctrine is evaluated.</p>",
    "4": "<p>The theme of doctrinal corruption generating moral decay: the false teachers are 'conceited and understand nothing,' their theological error producing envy, strife, and malicious talk. This pattern is theologically consistent with NT anthropology — idolatry (misidentifying the source of truth and life) distorts every downstream faculty. Right doctrine about Christ restores the mind; wrong doctrine corrupts it. The vices enumerated are the relational fruits of teaching that has lost its Christological center.</p>",
    "5": "<p>The theme of false gain: the false teachers 'think that godliness is a means to financial gain' — the perversion of religion as an instrument of wealth. The OT prophets regularly condemned this pattern (Mic 3:11: priests who taught for hire, prophets who divined for money). Jesus warned against mammon as rival lord (Matt 6:24). The Christological standard: the servant-pattern of Christ — who had nowhere to lay his head (Matt 8:20) and who gave himself as a ransom — is the inverse of the prosperity-religion the false teachers embody.</p>",
    "6": "<p>The theme of contentment as covenantal wealth: 'godliness with contentment is great gain.' The wisdom literature identified true prosperity as fellowship with YHWH — better a little with the fear of the Lord than great treasure with trouble (Prov 15:16). Jesus's beatitude of the poor in spirit (Matt 5:3) and his teaching on lilies and sparrows (Matt 6:25-33) establish that the kingdom citizen's provision comes from the Father. Contentment (<em>autarkeia</em>) is the experiential fruit of trusting God's provision rather than wealth.</p>",
    "7": "<p>The theme of creation's limit defining wealth's scope: 'we brought nothing into the world, and we can take nothing out.' This naked-entry, naked-exit framing echoes Job 1:21 and Eccl 5:15, grounding the anti-materialism argument in the structural reality of human creatureliness. The theological corollary: if wealth belongs to the created order that death ends, it cannot serve as ultimate security. Only what transcends death — life in Christ, 'the life that is truly life' (v. 19) — provides a foundation that death cannot dismantle.</p>",
    "8": "<p>The theme of sufficiency: basic provision — food and clothing — as grounds for contentment. This is precisely the provision that Jesus promised to those who seek first the kingdom (Matt 6:31-33: 'all these things will be added to you'). The minimum standard of material sufficiency that the Father provides is sufficient ground for trust. The Christian community is called to embody this contentment, demonstrating that their security rests in the living God rather than accumulated wealth.</p>",
    "9": "<p>The theme of avarice as a trap and a drowning: those who want to be rich 'fall into temptation and a trap' and are 'plunged into ruin and destruction.' The trap (<em>pagis</em>) is the same word used in 3:7 for the devil's snare — the desire for wealth is a structural mechanism of the adversary. The eschatological language 'ruin and destruction' (<em>olethron kai apōleian</em>) places the love of money within the category of judgment. Jesus's warning in the parable of the soils (wealth chokes the word, Mark 4:19) describes the same mechanism.</p>",
    "10": "<p>The theme of money as idolatrous root: 'the love of money is a root of all kinds of evil.' Jesus's teaching that 'you cannot serve both God and money' (Matt 6:24 / Luke 16:13) identifies wealth as a rival lord. When devotion to wealth displaces devotion to God, it generates every other disorder. Those who have 'wandered from the faith' are those who replaced the living God with the false security of wealth — the movement from faith to love-of-money is a movement from Christ to idolatry.</p>",
    "11": "<p>The theme of the man of God as prophetic office: 'you, man of God (<em>anthrōpe theou</em>), flee from all this.' The OT title designates those who spoke and acted on YHWH's behalf — Moses (Deut 33:1), Samuel (1 Sam 9:6), Elijah (1 Kgs 17:18), Elisha (2 Kgs 4:7). Applied to Timothy, the title places him in the succession of covenant spokespersons. The virtues Timothy is charged to pursue — righteousness, godliness, faith, love, endurance, gentleness — are the character of the Servant of YHWH and of Christ himself.</p>",
    "12": "<p>The theme of faithful confession: 'Fight the good fight of the faith. Take hold of the eternal life to which you were called when you made your good confession in the presence of many witnesses.' Timothy's confession at baptism or ordination becomes the anchor for the present charge. The 'good fight' (<em>kalos agōn</em>) echoes Paul's own race-metaphor (2 Tim 4:7) and Christ's endurance to the end (Heb 12:1-2). 'Eternal life' is the Christological prize — the life of the age to come, inaugurated in Christ's resurrection. The call and confession that initiated Timothy's ministry now sustain it toward the end.</p>",
    "13": "<p>A direct revelation: 'Christ Jesus, who while testifying before Pontius Pilate made the good confession.' The explicit historical grounding of Christ's own faithful witness under judicial pressure is the paradigm for Timothy's charge. Jesus's testimony before Pilate (John 18:33-37: 'for this I was born, and for this I came into the world — to bear witness to the truth') is the pattern that Timothy's confession must match. The God 'who gives life to everything' — the creator who sustains all life — is the same God who raised Jesus from death: the resurrection grounds the command to confess.</p>",
    "14": "<p>A direct revelation: 'Keep this command without spot or blame until the appearing (<em>epiphaneia</em>) of our Lord Jesus Christ.' The Pastoral Epistles use <em>epiphaneia</em> for both the Incarnation (2 Tim 1:10; Titus 2:11) and the Parousia. Here it is the Parousia: Christ's return is the temporal horizon that frames the entire charge to Timothy. Faithful ministry is eschatologically oriented — it serves the community between the two appearances of Christ, keeping the first in view until the second arrives.</p>",
    "15": "<p>A direct revelation: the divine sovereignty titles — 'King of kings and Lord of lords' — drawn from OT predicates of YHWH (Deut 10:17; Dan 2:37, 47) are applied to the God who will bring about Christ's appearing. Rev 17:14 and 19:16 explicitly transfer this same title to the returning Christ, completing the transfer. The doxology situates the Parousia under absolute divine sovereignty: the timing and manner of Christ's return belong to God alone (cf. Matt 24:36 — no one knows the day or hour except the Father).</p>",
    "16": "<p>A revelation of God: 'who alone has immortality and dwells in unapproachable light, whom no one has seen or can see.' The divine attributes — immortality, unapproachable light, invisibility — recall the OT disclosure of YHWH's transcendence (Exod 33:20; Ps 104:2). John 1:18 resolves the invisibility: 'no one has ever seen God; the only God who is at the Father's side has made him known.' The incarnate Christ is the epiphany of the unapproachable God — the one who dwells in unapproachable light becomes approachable in the Word made flesh (John 1:14).</p>",
    "17": "<p>The theme of Creator-provision as the ground of generosity: 'put your hope in God, who richly provides us with everything for our enjoyment.' The Creator who declared creation 'very good' (Gen 1:31) and who provides for sparrows and lilies (Matt 6:26-30) is the ground on which the rich are to rest rather than their wealth. The NT teaching: God's lavish provision is not an argument for accumulation but for generous distribution — having received richly, we give richly. The theology of giving flows from the character of the giving God revealed in Christ's self-gift.</p>",
    "18": "<p>The theme of wealth redefined: 'to be rich in good deeds, generous and willing to share.' The paradox of kingdom economics: true wealth is constituted by generous giving, not accumulation. Jesus's instruction on storing up treasure in heaven (Matt 6:19-21; Luke 12:33) inverts the ordinary wealth-logic. Those 'rich in good deeds' embody the character of Christ himself, who 'though he was rich, yet for your sake he became poor' (2 Cor 8:9) — the supreme pattern of liberality that the wealthy are called to replicate in their human sphere.</p>",
    "19": "<p>The theme of eschatological treasure: 'as a firm foundation for the coming age, so that they may take hold of the life that is truly life.' The 'coming age' is the age of resurrection and consummation inaugurated by Christ. Generosity in the present age 'lays up treasure' (Matt 6:19-21; Luke 12:33) in the age to come — an investment in the economy of the kingdom that Christ has already opened. 'The life that is truly life' (<em>tēs ontos zōēs</em>) is the eschatological life of the resurrection, the <em>zōē aiōnios</em> that is Christ's own life shared with his people.</p>",
    "20": "<p>The theme of faithful stewardship of revealed truth: 'guard what has been entrusted to your care' (<em>tēn parathēkēn phulaxon</em>). The deposit-image places Timothy in the succession of covenant recipients charged to guard and transmit what God has entrusted: Moses receiving and transmitting Torah, prophets receiving and transmitting YHWH's word, apostles receiving and transmitting the gospel. Timothy's stewardship of the apostolic gospel-tradition is structurally continuous with this covenantal pattern. The false knowledge (<em>pseudōnymos gnōsis</em>) is the counterfeit that threatens the genuine deposit.</p>",
    "21": "<p>The revelation of God in the closing benediction: 'Grace be with you all.' The Pastoral greeting of 'grace' (<em>charis</em>) transforms the standard Greek letter salutation (<em>chairein</em>) into a theological declaration. Grace is the covenantal term for the unmerited divine favor that creates and sustains all Christian life — the attribute of God most fully and finally displayed in the self-giving of Christ (2 Cor 8:9; 13:14). The closing grace-wish is a prayer that what God has begun in Christ will continue in the congregation Timothy serves.</p>"
  }
}

# ============================================================
# 2 TIMOTHY
# ============================================================

TWOTIM_ECHO = {
  "2": {
    "8": [
      {"type": "fulfillment", "target": "2 Sam 7:12-13", "note": "Jesus Christ, risen from the dead, the offspring of David — the Davidic promise (I will raise up your offspring after you and establish his throne forever) is fulfilled in the resurrection of David's descendant Jesus; the risen Christ is the Davidic heir whose kingdom will have no end"}
    ]
  },
  "3": {
    "16": [
      {"type": "allusion", "target": "Deut 31:19-22", "note": "All Scripture is breathed out by God — the divine-origin claim for Scripture echoes YHWH's instruction to Moses to write down the Song (Deut 31:19) as a witness; the written word as YHWH's own testimony against and for Israel; now extended to all Scripture"}
    ]
  },
  "4": {
    "8": [
      {"type": "allusion", "target": "Isa 40:10", "note": "Henceforth there is laid up for me the crown of righteousness which the Lord, the righteous judge, will award — YHWH coming with his reward, his recompense before him; Paul's awaited crown from the righteous judge at the parousia echoes the Isaianic expectation of the Lord's coming with vindication for the righteous"}
    ]
  }
}

TWOTIM_ORIGINAL = {
  "2": {
    "15": "<p><strong>spoudason seauton dokimon parastēsai to theo ergaten anepaiskunton orthotomounta ton logon tes aletheias</strong> (<em>spoudason seauton dokimon parastēsai tō theō, ergatēn anepaiskunton, orthotomounta ton logon tēs alētheias</em>): 'Do your best to present yourself to God as one approved, a worker who has no need to be ashamed, rightly handling the word of truth.' <em>Orthotomounta</em> (rightly dividing/handling/cutting): used in LXX Prov 3:6 ('he will make straight your paths') and 11:5. The word evokes a craftsman cutting or laying material in a straight line — a road-builder, a carpenter, a surgeon. The image: the handling of the word of truth requires the precision and skill of a craftsman who cuts straight rather than crooked. Historically, the King James 'rightly dividing' was applied dispensationally; the original metaphor is about competent, accurate, straight-course exposition.</p>"
  },
  "3": {
    "16": "<p><strong>pasa graphe theopneustos kai ophelimos</strong> (<em>pāsa graphē theopneustos kai ōphelimos</em>): 'All Scripture is God-breathed (<em>theopneustos</em>) and profitable.' <em>Theopneustos</em> is a Pauline coinage (hapax legomenon) combining <em>theos</em> (God) and <em>pneō</em> (breathe) — 'God-breathed' or 'breathed out by God.' The breath-metaphor echoes Gen 2:7 (YHWH breathed into Adam's nostrils) and the Spirit-wind of Ezekiel's valley of bones: the Scriptures are alive with divine breath, not merely human compositions. The primary referent is the OT (which Timothy was taught from childhood, v. 15); the claim's extension to apostolic writings is implicit in 2 Pet 3:16's treatment of Paul's letters as <em>graphe</em>.</p>"
  }
}

TWOTIM_CONTEXT = {
  "1": {
    "8": "<p>2 Timothy is widely regarded as Paul's final letter — written from a second Roman imprisonment ca. 66-67 CE, shortly before his death (4:6-8). The tone differs markedly from 1 Timothy: more personal, more urgent, more reflective of approaching death. The suffering-motif pervades the letter: Paul's chains (1:8, 16; 2:9), his abandonment by former associates (1:15; 4:10-16), his awareness of impending execution (4:6-8). If authentic (and most scholars accept 2 Timothy as more likely Pauline than 1 Timothy or Titus), it is the most personal surviving Pauline document. The mention of specific people (Hymenaeus, Philetus, Alexander the coppersmith, Demas, Luke, Mark) and personal items (the cloak at Troas, the books and parchments, 4:13) suggests authentic personal memory.</p>"
  },
  "3": {
    "1": "<p>The 'last days' (<em>eschatais hēmerais</em>) characterized by moral collapse (vv. 1-9: lovers of self, lovers of money, proud, arrogant, abusive, disobedient to parents, ungrateful, unholy, heartless, unappeasable...) represents a conventional form in Jewish and early Christian eschatological literature called the 'signs of the end' tradition — cf. 1 Enoch 91-93 (the Apocalypse of Weeks), 2 Baruch 27-30, and rabbinic descriptions of the era before Messiah's coming. Paul's use of this tradition applies it to the present crisis in Timothy's ministry, not a distant future: the last days have already begun in the false teachers' behavior.</p>"
  }
}

TWOTIM_CHRIST = {
  "1": {
    "10": "<p>A direct revelation: 'Our Savior Christ Jesus abolished death and brought life and immortality to light through the gospel.' The Christological declaration concentrates the gospel: Christ 'abolished' (<em>katargēsantos</em>) death — not merely defeated it but rendered it inoperative; brought life and immortality 'to light' (<em>phōtisantos</em>) — these were previously hidden in God's eternal purpose (v. 9) but are now disclosed through the proclamation. The Christology of 2 Timothy: the epiphany of the Savior is the historical moment when death's power was broken and life was made publicly visible.</p>"
  },
  "2": {
    "8": "<p>A direct revelation: 'Remember Jesus Christ, risen from the dead, the offspring of David, as preached in my gospel.' Paul's summary of the gospel in one sentence unites the two great OT streams: Davidic messiahship (the royal covenant of 2 Sam 7) and resurrection (the prophetic expectation of Isa 26:19; Dan 12:2). 'Remember' (<em>mnemoneue</em>) is imperative — not a passive recollection but an active, sustaining focus on the Christological fact that generates Paul's willingness to suffer (v. 9-10: I endure everything for the sake of the elect). The risen Davidic Christ is the content of endurance.</p>"
  },
  "4": {
    "8": "<p>A direct revelation: 'Henceforth there is laid up for me the crown of righteousness, which the Lord, the righteous judge, will award to me on that Day — and not only to me but also to all who have loved his appearing.' The parousia of Christ (the <em>epiphaneia</em> that Paul loved) is the moment of final vindication. The 'crown of righteousness' is not earned by Paul's sufferings but 'laid up' (<em>apokeitai</em>) — already determined, awaiting award. The righteous judge who will confer it is Christ himself. The Christological movement of 2 Timothy: from the first epiphaneia (incarnation, 1:10) through present endurance to the final epiphaneia where the judge vindicates the faithful.</p>"
  }
}

# ============================================================
# TITUS
# ============================================================

TITUS_ECHO = {
  "2": {
    "14": [
      {"type": "fulfillment", "target": "Exod 19:5", "note": "To purify for himself a people of his own possession — YHWH's Sinai declaration 'you shall be my treasured possession' (LXX: laos periousios, exactly the term used here); the new covenant community is the fulfillment of what the Sinai covenant pointed toward"},
      {"type": "fulfillment", "target": "Ezek 37:23", "note": "Who gave himself to redeem us from all lawlessness — YHWH's promise to cleanse Israel from all their backslidings; the redemption from lawlessness fulfills Ezekiel's new covenant cleansing promise"}
    ]
  },
  "3": {
    "5": [
      {"type": "fulfillment", "target": "Ezek 36:25-27", "note": "Renewing of the Holy Spirit whom he poured out on us richly — YHWH's promise to sprinkle clean water, put his Spirit within, and cause Israel to walk in his statutes; the new birth through the Spirit fulfills Ezekiel's new covenant restoration"}
    ]
  }
}

TITUS_ORIGINAL = {
  "2": {
    "13": "<p><strong>prosdechomenoi ten makarian elpida kai epiphaneian tes doxes tou megalou theou kai soteros hemon Iesou Christou</strong> (<em>prosdechomenoi tēn makarian elpida kai epiphaneian tēs doxēs tou megalou theou kai sōtēros hēmōn Iēsou Christou</em>): 'waiting for our blessed hope, the appearing of the glory of our great God and Savior Jesus Christ.' The Greek syntax — <em>tou megalou theou kai soteros hemon Iesou Christou</em> — with the single definite article governing both 'God' and 'Savior' (the Granville Sharp rule) most naturally refers to one person: 'our great God and Savior, Jesus Christ.' This is one of the most explicit divine predications of Jesus in the NT — calling him directly 'our great God.' <em>Epiphaneia</em> (appearing/manifestation) is the distinctive Pastoral Christological term for the Incarnation (1 Tim 3:16; 2 Tim 1:10) and the parousia (1 Tim 6:14; 2 Tim 4:1, 8) — a term the Hellenistic world used for the appearance of a deity or the arrival of a king.</p>"
  }
}

TITUS_CONTEXT = {
  "1": {
    "5": "<p>Titus in Crete: the island of Crete had a significant Jewish community (Acts 2:11; Josephus mentions Cretan Jews). Paul's description of Cretans — citing the Cretan poet Epimenides ('Cretans are always liars, evil beasts, lazy gluttons', v. 12) — uses an ancient ethnic stereotype familiar to his Greco-Roman audience. The church-planting task in Crete required appointing elders in 'every town' (<em>kata polin</em>), indicating a widespread but organizationally young mission. The Pastoral Epistles' emphasis on <em>episkopos</em> (overseer), <em>presbyteros</em> (elder), and <em>diakonos</em> (deacon) reflects the institutionalization of church leadership as the apostolic generation aged and died.</p>"
  },
  "3": {
    "5": "<p>The 'washing of regeneration and renewing of the Holy Spirit' (<em>loutron palingenesias kai anakainōseōs Pneumatos Hagiou</em>) combines Jewish purification-immersion imagery (<em>mikveh</em>) with the OT new-covenant Spirit-promise (Ezek 36:25-27; Joel 2:28-29). <em>Palingenesia</em> (regeneration/new birth) appears only here and Matt 19:28 (the renewal of all things at the eschatological restoration) in the NT — linking individual new birth with cosmic new creation. <em>Paliggenesia</em> was also a Stoic term for the cyclical renewal of the cosmos after the ekpyrosis (cosmic fire) — Paul's use may deliberately appropriate the Stoic vocabulary and fill it with Christological content: the Spirit's renewal is the eschatological new creation arriving in individual conversion.</p>"
  }
}

TITUS_CHRIST = {
  "2": {
    "14": "<p>A direct revelation: 'Who gave himself for us to redeem us from all lawlessness and to purify for himself a people of his own possession who are zealous for good works.' The Christological mission-statement of Titus: the self-giving of Christ (<em>edōken heauton</em>) accomplishes two things — ransom from lawlessness and purification-for-possession. The people-of-God language (laos periousios = treasured possession, Exod 19:5) is deliberately applied to the new covenant community formed by Christ's self-gift. Christ does not merely save individuals but creates a community that embodies his purposes — 'zealous for good works' completes the Christological transaction with an ethical telos.</p>"
  },
  "3": {
    "4": "<p>A direct revelation: 'But when the goodness and loving kindness of God our Savior appeared, he saved us, not because of works done by us in righteousness, but according to his own mercy, by the washing of regeneration and renewing of the Holy Spirit.' The 'appearance' (<em>epephanē</em>) of God's goodness is the Incarnation — the divine character made visible in Jesus. The Christological-Trinitarian movement: God the Savior's goodness appeared → he saved by mercy (not merit) → through the washing of the Spirit → poured out richly through Jesus Christ our Savior. The threefold divine action (God, Spirit, Christ) grounds salvation entirely outside human achievement.</p>"
  }
}

# ============================================================
# PHILEMON
# ============================================================

PHILEMON_ECHO = {
  "1": {
    "16": [
      {"type": "allusion", "target": "Lev 19:34", "note": "No longer as a slave but more than a slave, as a dear brother — the Levitical command to treat the alien among you as the native; the Onesimus-Philemon relationship after conversion exceeds the Torah's ethnic solidarity by requiring brotherly love between master and enslaved person"},
      {"type": "allusion", "target": "Deut 23:15-16", "note": "Receive him no longer as a slave but as a dear brother — Deuteronomy's command not to return a runaway slave to his master but to let him dwell wherever he chooses; Paul's appeal works within Roman law while nudging toward a more radical Christian brotherhood that subverts the institution"}
    ]
  }
}

PHILEMON_ORIGINAL = {
  "1": {
    "16": "<p><strong>ouketi hos doulon alla hyper doulon adelphon agapeton</strong> (<em>ouketi hōs doulon alla hyper doulon, adelphon agapēton</em>): 'no longer as a slave but more than a slave, as a dear brother.' The grammatical structure — <em>ouketi ... alla hyper</em> (no longer ... but beyond) — expresses a qualitative transformation, not just a label change. Onesimus remains in a social relationship with Philemon but that relationship is now defined by a different primary category: <em>adelphos agapētos</em> (beloved brother). Paul does not directly command emancipation, but the logic of brotherhood makes slavery an anomaly: how can you own your brother? The letter is the most politically charged use of household-code language in Paul — Christian kinship (<em>adelphos</em>) is placed in deliberate tension with Roman social institution (<em>doulos</em>).</p>",

    "18": "<p><strong>ei de ti edikesen se e opheilei touto emoi ellogei</strong> (<em>ei de ti ēdikēsen se ē opheilei, touto emoi ellogei</em>): 'If he has wronged you at all or owes you anything, charge that to my account.' <em>Ellogei</em> (charge to my account / impute) is a commercial-accounting term used only here and Rom 5:13 (sin is not <em>ellogeitai</em> when there is no law) in the NT. Paul offers to absorb Onesimus's debt as a surety. The theological parallel is explicit in the letter's rhetoric: as Paul stands in for Onesimus absorbing his debt-liability, Christ stands in for sinners absorbing their debt before God. Philemon is the NT's most compressed illustration of imputed righteousness in a human-relational register.</p>"
  }
}

PHILEMON_CONTEXT = {
  "1": {
    "10": "<p>Onesimus was enslaved in Philemon's household in Colossae (cf. Col 4:9: 'Onesimus, our faithful and dear brother, who is one of you'). The traditional reading: Onesimus ran away from Philemon, somehow encountered Paul in prison (Rome or Ephesus), was converted, and is now being returned. A minority reading (B. Winter, A. Callahan): Onesimus was sent by Philemon to assist Paul in prison (a known practice, cf. Phil 2:25-30 — Epaphroditus sent to serve Paul), and Paul now appeals for him to be released permanently for gospel ministry. Either way, the letter navigates Roman slave-law (the <em>Lex Petronia</em> of ca. 61 CE and related legislation governed runaways) while applying theological pressure through the rhetoric of Christian brotherhood.</p>",

    "16": "<p>Roman slavery in the first century CE: approximately 1-2 million enslaved people in Italy alone (roughly 30-35% of the Italian population, Scheidel's estimate); enslaved persons could be freed by manumission (<em>manumissio</em>) through various legal mechanisms. Freed persons became Roman citizens with some legal restrictions. The distinction Paul makes — 'both in the flesh and in the Lord' — is the Christian social ontology: Onesimus has both a new spiritual identity (brother in Christ) and an unchanged social location (in Philemon's household). Paul does not directly call for legal manumission, but the category 'dear brother' both in the flesh and in the Lord strains against the institution's dehumanizing premise.</p>"
  }
}

PHILEMON_CHRIST = {
  "1": {
    "17": "<p>A revelation of God: 'If you consider me your partner, receive him as you would receive me.' Paul's intercession for Onesimus reveals a pattern of representative substitution: the apostle places himself in the position of the offender and asks to be treated as Onesimus's surety. This is not strictly a direct Christological statement, but Paul consciously patterns his intercession on the Christological movement of divine advocacy — as Christ stands for sinners before the Father, Paul stands for Onesimus before Philemon. The letter reveals the social logic of atonement-theology as it should reshape human relationships.</p>",

    "18": "<p>A direct revelation: 'If he has wronged you at all, or owes you anything, charge that to my account.' The imputation-language (<em>ellogei</em>) makes this the most concrete illustration in the NT of the substitutionary logic that governs Paul's soteriology. The Christ-event logic: Christ receives the charge of our debt against God's account; Paul enacts this same logic with Onesimus's debt to Philemon. The atonement is not merely a doctrinal formula but a relational pattern that should generate analogous acts of substitutionary absorption of another's debt. Philemon is called to receive Onesimus 'as you would receive me' (v. 17) — Christ-likeness enacted in the ordinary economy of first-century household relationships.</p>"
  }
}

def main():
    books = [
        ('1timothy', ONETIM_ECHO, ONETIM_ORIGINAL, ONETIM_CONTEXT, ONETIM_CHRIST),
        ('2timothy', TWOTIM_ECHO, TWOTIM_ORIGINAL, TWOTIM_CONTEXT, TWOTIM_CHRIST),
        ('titus', TITUS_ECHO, TITUS_ORIGINAL, TITUS_CONTEXT, TITUS_CHRIST),
        ('philemon', PHILEMON_ECHO, PHILEMON_ORIGINAL, PHILEMON_CONTEXT, PHILEMON_CHRIST),
    ]
    for book, echo_d, orig_d, ctx_d, chr_d in books:
        e = load_echo(book)
        merge_echo(e, echo_d)
        save_echo(book, e)

        c = load_comm('mkt-original', book)
        merge_comm(c, orig_d)
        save_comm('mkt-original', book, c)
        print(f'{book} original: {len(c)} chs, {sum(len(v) for v in c.values())} vs')

        c = load_comm('mkt-context', book)
        merge_comm(c, ctx_d)
        save_comm('mkt-context', book, c)
        print(f'{book} context: {len(c)} chs, {sum(len(v) for v in c.values())} vs')

        c = load_comm('mkt-christ', book)
        merge_comm(c, chr_d)
        save_comm('mkt-christ', book, c)
        print(f'{book} christ: {len(c)} chs, {sum(len(v) for v in c.values())} vs')

if __name__ == '__main__':
    main()
