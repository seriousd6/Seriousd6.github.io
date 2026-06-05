"""
MKT Context — 1 John chapters 1–4 (historical/cultural background)
Output: data/commentary/mkt-context/1john.json

Historical setting: Johannine community late 1st century (ca. 85-95 CE),
probably Ephesus. Primary threat: proto-Docetic secessionists (1:6, 2:19, 4:1-3)
who deny the fleshly reality of Christ. Possible connection to Cerinthus
(Irenaeus Haer. 1.26.1, 3.11.1 — Cerinthus taught Christ descended on Jesus
at baptism and departed before the cross).

Second context: Hellenistic dualism (light/darkness from Platonic and Stoic sources),
Jewish apocalypticism (light/darkness at Qumran 1QS 3-4), and Gnostic tendencies
all converging in the Johannine milieu.
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
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

DATA = {
  "1": {
    "1": '<p>The eyewitness claim ("what we have seen and touched") confronts a proto-Docetic position in which the flesh of Jesus was apparent rather than real. Docetism (<em>dokein</em> = to seem) was not yet the later organized Gnosticism but already present in various forms: Cerinthus (according to Irenaeus) distinguished between the human Jesus and a divine Christ-spirit that descended at baptism and departed before the crucifixion. John\'s insistence on handling (<em>epselaphesen</em>) the Word of life directly counters any spiritualizing that would make the incarnation non-physical. The letter\'s opening is apologetic before it is devotional.</p>',
    "5": '<p>Light/darkness dualism pervades both the Johannine community\'s milieu and the broader Hellenistic world. At Qumran, the Community Rule (1QS 3:13-4:26) divided all humanity into children of light and children of darkness under two spirits — an apocalyptic dualism from Jewish soil. Plato\'s cave analogy in the Republic (514a-520a) used light as the metaphor for true knowledge vs. the shadows of ignorance. Stoic cosmology identified divine reason with light. John uses the dualism but anchors it theologically in God\'s character ("God is light") rather than in cosmic forces — making the ethical implications (walking in light) follow from the nature of God, not from cosmological fate.</p>',
    "7": '<p>The language of blood cleansing evokes the Yom Kippur ritual, the daily Levitical washings, and the Passover blood on the doorposts — all of which were part of the cultic apparatus of Second Temple Judaism that the Johannine community had left behind. The radical claim is that a single historical event (the crucifixion) accomplishes continuously ("cleanses," present tense) what the entire sacrificial system performed cyclically. For Jewish-background members of the community, this was the hermeneutical key to why they could leave the temple system; for Gentile members, it gave the blood-language its thick covenant meaning.</p>'
  },
  "2": {
    "1": '<p>The <em>parakletos</em> title for Christ as heavenly advocate reflects legal culture familiar to both Jewish and Greco-Roman audiences. In Roman law, a <em>patronus</em> (patron) would speak on behalf of a client before a magistrate; in Jewish legal practice, an <em>intercessor</em> (<em>melits</em> in Hebrew) could plead a defendant\'s case before the divine judge (cf. Job 16:19-21, 33:23-28). The transfer of the Paraclete title from the Spirit (John 14-16) to Christ here suggests a two-advocate theology: the Spirit advocates within the community\'s hearts (John 14:16-17), Christ advocates in the divine court. This would have resonated with both Roman patronage culture and Jewish court theology.</p>',
    "15": '<p>The prohibition of love for "the world" (<em>ho kosmos</em>) must be read against the social pressures on the Johannine community in Ephesus: the Roman imperial cult (emperor worship), the guild system (participation in trade guilds required honoring patron deities), and the cultural prestige of Hellenistic philosophical education all constituted "the world" that demanded loyalty. The threefold catalog that follows (desire of the flesh, desire of the eyes, pride of life — 2:16) maps onto these social pressures: the pleasures, the spectacles, and the status claims of Greco-Roman urban life. The prohibition is not asceticism for its own sake but covenant loyalty against cultural assimilation.</p>',
    "18": '<p>The "antichrist" figure combines Jewish expectations of an eschatological adversary (Belial in Qumran, the man of lawlessness in 2 Thess 2) with the immediate historical crisis of secessionists leaving the community (2:19). In Qumran literature (1QS, CD), Belial is both a present spiritual force and a future eschatological figure whose power intensifies toward the end. John\'s innovation is the plural: "many antichrists have come" — the final Antichrist\'s spirit is already present in the false teachers, making the eschatological battle a present community crisis rather than a distant apocalyptic event.</p>',
    "19": '<p>"They went out from us but were not of us" — the phenomenon of sectarian departure was recognized and interpreted in Second Temple Judaism through the lens of covenant election. Those who left the community (as Qumran understood deserters from the community as those who were never truly of the covenant) were identified retrospectively as never having belonged. This is not a persecution scenario but an internal crisis of schism — the Johannine community lost members to a more sophisticated-seeming spirituality that John identifies as anti-Christian despite its Christian vocabulary.</p>'
  },
  "3": {
    "1": '<p>"Because the world did not know him" — the social alienation of the Johannine community from wider Ephesian society is the lived experience behind this verse. Refusal to participate in the imperial cult, withdrawal from guild festivals, and exclusive monotheism all made the community culturally conspicuous and socially marginalized. John interprets this alienation not as social failure but as participation in the world\'s rejection of God himself — the community\'s strangeness to the world mirrors God\'s strangeness to the world as demonstrated in the rejection of the incarnate Son.</p>',
    "4": '<p>The definition of sin as lawlessness (<em>anomia</em>) is a deliberately Jewish-covenantal framing against any spiritualizing tendency that would define sin in Platonic terms (ignorance or materiality rather than moral rebellion). In the Greek moral tradition, sin was often <em>hamartia</em> as missing the mark (Aristotle, Nicomachean Ethics), which could be corrected by better knowledge or practice. John insists that sin is specifically lawlessness — anti-covenantal defiance of God\'s revealed will — which requires atonement rather than education, forgiveness rather than enlightenment. This had direct polemical relevance against any proto-Gnostic system that located sin in materiality rather than in moral rebellion.</p>',
    "12": '<p>Cain as the paradigm of murderous hatred connects to a rich Second Temple tradition. Philo (On the Sacrifices of Cain and Abel) interpreted Cain as the embodiment of the self-loving, godless orientation; 4 Maccabees uses brotherly love vs. hatred as a moral category. The Midrash Rabbah developed extensive reflection on the Cain-Abel narrative. For John, Cain\'s hatred of Abel (motivated by jealousy that Abel\'s offering was accepted) mirrors the world\'s hatred of the community (because the community\'s righteousness exposes the world\'s unrighteousness). The paradigm is sociological as well as theological: visible faithfulness provokes hostility from those whose faithlessness it indicts.</p>'
  },
  "4": {
    "1": '<p>Spirit-testing had precedent in prophetic tradition (Deut 13:1-3, Jer 23:9-40, Ezek 13) and in early Christian practice (1 Thess 5:21, 1 Cor 12:10, 14:29). The Didache (written near this period, ca. 90-110 CE) devotes chapters 11-13 to testing traveling prophets: how long they stay, whether they ask for money, whether their character matches their prophecy. The Johannine community faced a more theological test: not merely behavioral but doctrinal — does the prophet confess the incarnation? This doctrinal criterion for spirit-discernment was a significant development in early Christian epistemology, anchoring charismatic authenticity to creedal content.</p>',
    "2": '<p>The anti-Docetic confession "Jesus Christ has come in the flesh" was likely a liturgical test formula in the Johannine community, functioning as a boundary marker between the community and the secessionists. Pliny the Younger (Epistulae 10.96, ca. 112 CE), in his report to Trajan about Christians in Bithynia, mentions that they sang hymns to Christ as to a god and recited formulaic declarations — suggesting that confessional tests were built into early Christian liturgical practice. The Docetic teachers would have claimed to affirm Christ while understanding "flesh" spiritually; John\'s criterion specifically requires the material, historical reality of the incarnation.</p>',
    "20": '<p>The logic of the visible neighbor as the test of love for the invisible God addresses a spiritual-escapism common in Hellenistic religion. Mystery cults (Eleusinian, Orphic, Mithraic) promised direct mystical encounter with the divine through initiation rites, often disdaining ordinary social relationships as distractions from the divine quest. Gnostic systems emphasized the escape from material entanglement, including familial and social bonds, toward pure spiritual existence. John insists that love of God is not verified in mystical experience but in the mundane practice of loving the visible human being — specifically the brother. This is not anti-mystical but grounds mystical experience in ethical life.'
  }
}

def main():
    existing = load_comm('mkt-context', '1john')
    merge_comm(existing, DATA)
    save_comm('mkt-context', '1john', existing)
    total = sum(len(v) for v in existing.values())
    print(f'1 John mkt-context: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
