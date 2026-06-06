"""
MKT Christ Commentary — 1 John chapter 5
Run: python3 scripts/zc-christ-1john-5-5.py

Source data used:
- data/interlinear/1john.json
- data/translation/draft/mediating/1john.json
- data/commentary/mkt-christ/1john.json (existing entries incl. chs 1-4)

Key decisions in ch 5:
- 5:1 "born of God" = birth through faith in the incarnate Christ (John 1:12-13)
- 5:4 "victory that overcomes the world = our faith" (aorist: accomplished in Christ's
  cross/resurrection, appropriated through faith)
- 5:6 "water and blood" = baptism and crucifixion — both historical events constitute
  the full Christ-event against Cerinthian water-only Christology
- 5:7-8 three witnesses: Spirit (inward), water+blood (historical) — converging on
  the one person Jesus Christ
- 5:13 purpose of the letter = assurance through the name of the Son of God
- 5:16 "sin unto death" = apostasy (deliberate rejection of the incarnate Christ)
- 5:18 "the One born of God keeps them safe" = Christ, not the believer
- 5:20 "we are in him who is true" = the community's union with the Son
- 5:21 "idols" = any rival to the true God revealed in Christ
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

JOHNI_CH5 = {
  "5": {
    "1": '<p>A direct revelation: everyone who believes that Jesus is the Christ is born of God. The belief-criterion is the anti-Cerinthian confession in compressed form — the human Jesus is identical with the divine Christ. Those who separate them (as the secessionists do) cannot make this confession and therefore demonstrate they are not born of God. The new birth (John 1:12-13; 3:3-8) has a specifically Christological object: it is birth through faith in the one who came in the flesh, not birth through mystical illumination or esoteric gnosis about a heavenly Christ separate from the human Jesus.</p>',
    "2": '<p>A revelation of God: we know we love the children of God by loving God and keeping his commands. The mutual-verification structure of Johannine ethics is Christological at its core: the commands are Christ\'s commands (John 13:34; 15:10-12), and the God loved is the God revealed in Christ. The ethical coherence test — love of God / love of neighbor / obedience — is the test of whether the community genuinely knows the Christ who both commanded the love and modeled it at the cross. Disintegration of any element (as in the secessionists) reveals the whole as hollow.</p>',
    "3": '<p>A revelation of God: love for God means keeping his commands, and his commands are not burdensome. The non-burdensome character of the commands is Christological: they flow from love (Christ\'s own love, communicated through the Spirit) rather than from external legal imposition. Christ himself said "my yoke is easy and my burden is light" (Matt 11:30) — the one who keeps the commands does so as a participant in Christ\'s own orientation toward the Father, not as a slave under law. The commands become bearable because the indwelling life of the Son makes them the expression of a new nature rather than an external demand.</p>',
    "4": '<p>A direct revelation: everyone born of God overcomes the world. This is the victory that has overcome the world — our faith. The aorist participle "having-overcome" (nikesasa) points to a victory already accomplished: Christ\'s cross and resurrection have overcome the world (John 16:33). Faith is the means by which the community appropriates and lives within this accomplished victory — not a power they generate but a trust in the one who has already won. The community\'s social marginalization in Roman Ephesus is not their defeat but their participation in the world-overcoming of the crucified and risen one.</p>',
    "5": '<p>A direct revelation: who overcomes the world except the one who believes that Jesus is the Son of God? The overcoming faith is specifically trust in the incarnate Son. The Cerinthian position — affirming a heavenly Christ while relativizing the human Jesus — cannot produce this faith, because the world-overcoming faith is trust in the one who entered the world fully and suffered its worst (the crucifixion). No alternative Christology generates the overcoming faith: only trust in the fully incarnate Son of God, who is both human enough to die and divine enough to conquer death, produces the life that overcomes the world.</p>',
    "6": '<p>A direct revelation: this is he who came by water and blood — Jesus Christ; not by water only but by water and blood. The Cerinthian position accepted the water (the Spirit\'s descent at baptism making Jesus the Christ) while rejecting the blood (the crucifixion as the Christ\'s act — Cerinthus taught the Christ departed before the cross). John insists on both: the one who came is Jesus Christ — the same person through the water and through the blood. The incarnation is complete only when the full Christ-event is affirmed: not just the Spirit-anointed ministry but the blood-shedding death that is the atonement.</p>',
    "7": '<p>A direct revelation: there are three that testify. The juridical framework (witnesses establishing truth) grounds the Christological claim in legal terms: Deuteronomy 19:15 required two or three witnesses to establish any matter. John provides three converging witnesses for the identity of Jesus Christ. The implied setting is a divine court in which the secessionists\' alternative Christology is being tried — the apostolic community presents its three-fold testimony in rebuttal. The community\'s confidence in the genuine Christ rests not on a single witness but on three that agree.</p>',
    "8": '<p>A direct revelation: the Spirit, the water, and the blood — and the three agree. The Spirit\'s witness is inward — the Paraclete who was promised (John 14:26; 15:26) and who now testifies within the community to the identity of Jesus Christ as the incarnate Son. Water (the baptism) and blood (the crucifixion) are the two historical events that constitute the Christ-event: the Spirit descending on Jesus in the Jordan and the blood poured out at Calvary. Against Cerinthus who affirmed the water-testimony but not the blood-testimony, John insists that the three witnesses converge on the one person Jesus Christ through both historical events.</p>',
    "9": '<p>A direct revelation: we accept human testimony; God\'s testimony is greater, because this is God\'s testimony about his Son. The a-fortiori argument from human to divine testimony grounds the community\'s confidence in the most secure possible foundation: not human assessment of Jesus but God\'s own self-testimony about his Son. The Father testified at the baptism (Matt 3:17: "This is my Son") and at the transfiguration (Matt 17:5), and now testifies through the Spirit and through the completed Christ-event. The secessionists\' counter-Christology is one human construction against God\'s own triple testimony.</p>',
    "10": '<p>A direct revelation: whoever believes in the Son of God has this testimony in themselves. The internal reception of the divine testimony is the Spirit\'s work — the Paraclete testifies within the community member who believes, confirming the identity of Jesus Christ from within. Rejecting this testimony (as the secessionists do by their alternative Christology) is calling God a liar — a stark characterization that escalates the stakes of the Christological dispute from theological disagreement to an implicit charge of divine deception. The genuine Christ and the divine testimony about him are inseparable.</p>',
    "11": '<p>A direct revelation: God gave us eternal life, and this life is in his Son. The Christological claim is locative: eternal life is not a quality distributed generally or a state achieved through gnosis, but a life that exists specifically in the person of the Son and is received only by being in him. This directly counters any Gnostic or Cerinthian arrangement in which eternal life is accessed through spiritual knowledge or mystical experience apart from the historical Jesus. Life is inseparable from the person — you cannot have the life without having him who is the life (John 11:25; 14:6).</p>',
    "12": '<p>A direct revelation: whoever has the Son has life; whoever does not have the Son of God does not have life. The exclusive either/or directly addresses the community situation: those who have departed from the Johannine Christological confession no longer "have the Son" in John\'s sense. Their Christological redefinition means, in John\'s terms, they do not have the Son — and therefore do not have the life they claim to possess through their superior gnosis. The alternative christ of the secessionists cannot communicate the life that is in the Son, because life is in the person, not in a doctrine about him.</p>',
    "13": '<p>A direct revelation: I write these things so that you may know that you have eternal life — you who believe in the name of the Son of God. The stated purpose of the letter is assurance for the community that has been destabilized by the secessionists\' claims. The community\'s assurance rests not on their spiritual experience but on their having believed in (and remained in) the authentic name of the Son of God. Believing in the name is covenantal trust in the person that the name identifies: Jesus Christ, the fully incarnate, crucified, and risen Son. The letter itself is a Christological assurance document.</p>',
    "14": '<p>A direct revelation: this is the confidence we have in approaching him — that if we ask anything according to his will, he hears us. The parresia (confidence) in approaching God is the community\'s experience of the access that Christ opened (Heb 10:19-22). Prayer "according to his will" is prayer in alignment with the will of the one who himself always did the Father\'s will (John 4:34; 8:29) — the community prays as those who are in Christ and who share his orientation toward the Father. The confidence is not in their technique but in the one through whom they approach.</p>',
    "15": '<p>A direct revelation: we know that if he hears us in whatever we ask, we know that we have the requests we have asked of him. The assured reception of answered prayer is the community\'s experience of prayer in Christ — offered through the one who intercedes for them (2:1) and who promised "whatever you ask in my name, I will do it" (John 14:13-14). The confidence of v.14 (he hears) produces the further confidence of v.15 (we have what we asked). Both rest on the same Christological ground: the community prays as those who are in the Son and through the Son.</p>',
    "16": '<p>A revelation of God: if anyone sees a brother sinning a sin not unto death, they should ask and God will give him life. Intercessory prayer for the sinning community member is the community\'s practice of the love-ethic (3:16-17) in the prayer-dimension: laying down for one another in prayer as Christ laid down for them. The God who hears (v.15) responds to intercession for sinning community members, giving them life through the prayer of the community. The community\'s pastoral care through prayer is a participation in Christ\'s own intercessory ministry (2:1; Heb 7:25) on behalf of those who sin.</p>',
    "17": '<p>A revelation of God: all wrongdoing is sin, and there is sin not unto death. The clarification that all wrongdoing is sin — against any proto-Gnostic position that spiritual persons are above moral categories — is paired with the recognition that not all sin is the apostasy-unto-death. The Christological significance: Christ\'s atonement covers the sins of those who remain in faith (1:9), and the community\'s intercessory prayer is effective for those who sin in this way. The "sin unto death" — the deliberate rejection of the incarnate Christ — places the apostate outside the scope of the community\'s intercessory prayer because they have rejected the very ground of forgiveness.</p>',
    "18": '<p>A direct revelation: anyone born of God does not keep on sinning — the One born of God keeps them safe, and the evil one does not touch them. The "One born of God" who keeps the community safe is best read as Christ — the uniquely born-of-God Son who protects those born of God. This is a pastoral reassurance for a community under doctrinal attack: the Son himself is the guardian of those who belong to him, not merely through their own moral vigilance but through his active, ongoing protection against the evil one\'s inroads. The community\'s safety is Christological, not self-achieved.</p>',
    "19": '<p>A direct revelation: we know that we are of God and the whole world lies in the power of the evil one. The community\'s different allegiance (of God vs. of the world) is Christological at its root: they are "of God" because they have been born of God through faith in the Son (v.1), and their different genealogy produces a different orientation. The world under the evil one is the world that rejected the Son (John 1:10-11; 3:19-20) — the same world that the Son overcame by his cross (John 16:33). The community stands on the winning side of this cosmic conflict because they are in the victor.</p>',
    "20": '<p>A direct revelation: we know that the Son of God has come and has given us understanding, so that we may know him who is true. And we are in him who is true — in his Son Jesus Christ. He is the true God and eternal life. The "understanding" (dianoia) given by the Son is not esoteric knowledge but the capacity to know the true God — knowledge that is inaccessible apart from the Son who reveals him (John 1:18; 14:9). The community\'s union with the true God is mediated through their union with the Son (in him who is true, in his Son Jesus Christ). The letter closes with the same Christological identification it opened with: Christ is the eternal life that was from the beginning.</p>',
    "21": '<p>A direct revelation: dear children, keep yourselves from idols. The closing command is Christological in its logic: an idol is any substitute for the true God revealed in Christ. Having identified the Son of God as the true God and eternal life (v.20), John warns the community against any counter-claim — including the alternative christ of the secessionists, who offers a spiritualized version of Christ separated from the historical Jesus and the cross. The secessionists\' christ is the primary "idol" in view: a constructed image of Christ that is not the true one, which the community must guard themselves against by holding to the original apostolic testimony about who Jesus Christ is.</p>'
  }
}

def main():
    existing = load_comm('mkt-christ', '1john')
    merge_comm(existing, JOHNI_CH5)
    save_comm('mkt-christ', '1john', existing)
    total = sum(len(v) for v in existing.values())
    print(f'1 John mkt-christ ch 5: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
